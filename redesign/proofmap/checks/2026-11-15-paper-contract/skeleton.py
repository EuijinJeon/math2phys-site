#!/usr/bin/env python3
"""논문 전체 계약의 기계 뼈대 (LLM 없음).

    python3 skeleton.py OUT.json

1. `tools/extract_tex.py` 를 11개 절에 돌린다(산출은 이 폴더 extract/).
2. 모든 node 후보(S·E)를 논문 전체 label 표로 모은다. 다른 절을 가리키는 `\\ref` 는
   그 label 을 가진 node 로 푼다(기계 edge).
3. 카드(redesign/cards, 읽기만)를 node 에 붙인다: 카드 id 의 앞부분이 node label 이거나
   그 node 의 출력·내부 식 label 이면 그 node, 아니면 카드의 원문 줄이 node 범위 안에 들면
   그 node. 어느 쪽도 아니면 "주인 없는 카드"(관례·가정·remark·정의 문단 등)로 둔다.
4. 카드 `uses` 로 의존 후보를 만든다: 다른 node 의 카드 → node 의존(origin card),
   주인 없는 카드 → 기호·관례·바닥 후보.
5. 절 단위 의존 순서(위상 순서)를 계산한다.
"""
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PM = HERE.parents[1]
RED = PM.parent
SEC = RED / "source/sections"
CARDS = RED / "cards"
FILES = ["introduction", "model", "overview", "trees", "upper", "cavity", "perturbations",
         "decorrelation", "comparison", "reduction", "consequences"]


def read_card(path):
    text = path.read_text(encoding="utf-8")
    head = text.split("---")[1]
    get = lambda k: (re.search(rf"^{k}:\s*(.*)$", head, re.M) or [None, ""])[1].strip()
    lst = lambda k: [x.strip() for x in get(k).strip("[]").split(",") if x.strip()]
    return {"id": get("id"), "title": get("title").strip("'"), "kind": get("kind"),
            "uses": lst("uses"), "children": lst("children"),
            "lines": [(f, int(a), int(b)) for f, a, b in
                      re.findall(r"\{file: ([\w.]+), lines: \[(\d+), (\d+)\]\}", head)]}


def main():
    out = Path(sys.argv[1])
    exdir = HERE / "extract"
    exdir.mkdir(exist_ok=True)
    ex = {}
    for f in FILES:
        p = exdir / f"{f}.json"
        subprocess.run([sys.executable, str(PM / "tools/extract_tex.py"), str(SEC), f"{f}.tex", str(p)],
                       check=True, capture_output=True)
        ex[f] = json.loads(p.read_text(encoding="utf-8"))

    nodes, label_owner = {}, {}
    for f in FILES:
        by_span = {}
        for n in ex[f]["nodes"]:
            nid = n["id"]
            # 같은 문단(같은 줄 범위)의 참조되는 번호 식 여럿은 node 하나로 합친다(첫 label 이 id).
            key = (n["rule"], json.dumps(n["span"]))
            if n["rule"] == "E" and key in by_span:
                host = nodes[by_span[key]]
                host["output_labels"] += [o["label"] for o in n["outputs"]]
                host.setdefault("merged_labels", []).append(nid)
                for lab in [nid] + [o["label"] for o in n["outputs"]]:
                    label_owner[lab] = host["id"]
                continue
            by_span[key] = nid
            nodes[nid] = {"id": nid, "file": f"{f}.tex", "section": f, "rule": n["rule"], "env": n["env"],
                          "span": n["span"], "output_labels": [o["label"] for o in n["outputs"]],
                          "exported": [o["label"] if isinstance(o, dict) else o for o in n["exported_eqs"]],
                          "internal": [o["label"] if isinstance(o, dict) else o for o in n["internal_eqs"]],
                          "cards": [], "inputs": {}}
            for lab in [nid] + nodes[nid]["output_labels"] + nodes[nid]["exported"] + nodes[nid]["internal"]:
                label_owner[lab] = nid

    def in_span(nid, file, a, b):
        n = nodes[nid]
        return n["file"] == file and any(lo <= a and b <= hi for lo, hi in n["span"])

    def add_input(nid, key, kind, origin, info):
        d = nodes[nid]["inputs"].setdefault(key, {"key": key, "kind": kind, "origins": [], "machine_refs": [],
                                                  "card_refs": []})
        if origin not in d["origins"]:
            d["origins"].append(origin)
        d["machine_refs" if origin == "machine" else "card_refs"].append(info)

    # 기계 edge: 절 안 + 절 사이. 같은 node 안 참조는 버린다.
    machine_unresolved, head_refs = [], []
    for f in FILES:
        for e in ex[f]["edges"]:
            src = e["from"]
            if src.startswith("EXT:"):
                src = src[4:]
            src = label_owner.get(src)
            to = label_owner.get(e["to"], e["to"])
            if src is None:
                machine_unresolved.append({"file": f, **e})
                continue
            if src == to:
                continue
            add_input(to, src, "node", "machine", {"label": e["item"], "line": e["ref_line"], "cmd": e["cmd"]})
        for r in ex[f]["unassigned_refs"]:
            head_refs.append({"file": f"{f}.tex", "line": r["line"], "label": r["label"], "why": r["why"],
                              "target_node": label_owner.get(r["label"])})

    cards = {c["id"]: c for c in (read_card(p) for p in sorted(CARDS.glob("*.md")))}

    def card_owner(cid):
        c = cards.get(cid)
        base = cid.split(".")[0]
        if base in label_owner:
            return label_owner[base], "label"
        if c:
            for nid in nodes:
                if c["lines"] and all(in_span(nid, fl, a, b) for fl, a, b in c["lines"]):
                    return nid, "lines"
        return None, None

    owner = {}
    for cid, c in cards.items():
        o, how = card_owner(cid)
        owner[cid] = o
        if o:
            nodes[o]["cards"].append({"id": cid, "kind": c["kind"], "how": how})
    unowned = {cid: c for cid, c in cards.items() if owner[cid] is None}

    card_unresolved = []
    for cid, c in cards.items():
        n = owner[cid]
        if not n:
            continue
        for u in c["uses"]:
            if u not in cards:
                card_unresolved.append({"card": cid, "use": u, "why": "카드 없음"})
                continue
            m = owner[u]
            info = {"card": cid, "use": u, "use_lines": cards[u]["lines"]}
            if m is None:
                add_input(n, "card:" + u, "unowned_card", "card", info)
            elif m != n:
                add_input(n, m, "node", "card", info)

    # 절 단위 graph 와 위상 순서
    sec_edges = defaultdict(lambda: {"machine": 0, "card": 0})
    for n in nodes.values():
        for k, d in n["inputs"].items():
            if d["kind"] == "node" and nodes[k]["section"] != n["section"]:
                for o in d["origins"]:
                    sec_edges[(nodes[k]["section"], n["section"])][o] += 1
    deps = defaultdict(set)
    for (a, b) in sec_edges:
        deps[b].add(a)
    order, seen, cyc = [], set(), []

    def visit(s, stack):
        if s in seen:
            return
        if s in stack:
            cyc.append(stack[stack.index(s):] + [s])
            return
        for d in sorted(deps[s], key=FILES.index):
            visit(d, stack + [s])
        seen.add(s)
        order.append(s)

    for s in FILES:
        visit(s, [])

    for n in nodes.values():
        n["inputs"] = sorted(n["inputs"].values(), key=lambda d: d["key"])
    res = {"tool": "skeleton.py", "files": FILES, "topo_order": order, "cycles": cyc,
           "section_edges": [{"from": a, "to": b, **v} for (a, b), v in sorted(sec_edges.items())],
           "nodes": [nodes[k] for k in sorted(nodes, key=lambda k: (FILES.index(nodes[k]["section"]), nodes[k]["span"][0][0]))],
           "unowned_cards": [{"id": cid, "kind": c["kind"], "title": c["title"], "lines": c["lines"],
                              "uses": c["uses"]} for cid, c in sorted(unowned.items())],
           "head_refs": head_refs, "machine_unresolved": machine_unresolved, "card_unresolved": card_unresolved}
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
