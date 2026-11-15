#!/usr/bin/env python3
"""tex 원문에서 증명 지도의 node 후보와 참조 edge 후보를 기계로 뽑는다 (LLM 없음).

    python3 redesign/proofmap/tools/extract_tex.py \
        redesign/source/sections decorrelation.tex OUT.json

표준 라이브러리만 쓴다. 판정 규칙(2026-11-15 수 5 PoC, HANDOFF 5절 [확정] 1–2):

node 후보
  S  theorem / lemma / proposition / corollary / definition 환경 하나와,
     바로 뒤(빈 줄만 사이에 둔) proof 환경 또는 `[Proof of \\cref{label}]` 로
     그 진술을 가리키는 proof 환경. 줄 범위 = 진술 시작 ~ 증명 끝.
  E  진술·증명 환경 밖(본문)의 번호 식 가운데 다른 곳에서 \\ref/\\eqref/\\cref 로
     참조되는 것. 줄 범위 = 그 식을 품은 빈 줄 사이의 문단.
  진술 환경 안의 번호 식은 그 node의 출력 항목이다.
  증명 블록 안의 번호 식은 그 node의 내부 식이다. 블록 밖에서 참조되면
  "내보낸 내부 식"(exported)으로 표시하고 node를 따로 세우지 않는다.
  remark, figure, 참조되지 않는 본문 식은 node가 아니다(제외 목록에 남긴다).

edge 후보
  범위 파일의 참조 하나 = (참조된 label 을 가진 node) → (참조가 있는 줄을 품은 node).
  같은 node 안의 참조는 내부 참조로 세고 edge를 만들지 않는다.
  범위 밖 label 은 외부 입력 node(EXT:<label>)로 둔다.
  다른 파일이 범위의 label 을 참조하면 외부 출력 node(OUT:<file>)로 둔다.
  어느 node에도 들지 않는 줄의 참조는 'unassigned_refs' 로 남긴다.
"""
import json
import re
import sys
from pathlib import Path

STATEMENT_ENVS = {"theorem", "lemma", "proposition", "corollary", "definition"}
EQ_ENVS = {"equation", "align", "gather", "multline", "equation*", "align*"}
BEGIN = re.compile(r"\\begin\{([A-Za-z*]+)\}(\[[^\]]*\])?")
END = re.compile(r"\\end\{([A-Za-z*]+)\}")
LABEL = re.compile(r"\\label(?:\[[^\]]*\])?\{([^}]+)\}")
REF = re.compile(r"\\(eqref|ref|cref|Cref|autoref)\{([^}]+)\}")


def scan(path):
    """환경(시작·끝 줄, 깊이), label(줄, 감싼 환경들), 참조(줄, 명령)를 모은다."""
    lines = path.read_text(encoding="utf-8").splitlines()
    envs, stack, labels, refs = [], [], [], []
    for no, raw in enumerate(lines, 1):
        line = raw.split("%")[0] if not raw.lstrip().startswith("%") else ""
        for m in BEGIN.finditer(line):
            env = {"env": m.group(1), "opt": (m.group(2) or "")[1:-1], "start": no, "end": None}
            stack.append(env)
            envs.append(env)
        for m in LABEL.finditer(line):
            labels.append({"label": m.group(1), "line": no,
                           "within": [(e["env"], e["start"]) for e in stack]})
        for m in REF.finditer(line):
            for lab in m.group(2).split(","):
                refs.append({"label": lab.strip(), "line": no, "cmd": m.group(1)})
        for m in END.finditer(line):
            for i in range(len(stack) - 1, -1, -1):
                if stack[i]["env"] == m.group(1):
                    stack[i]["end"] = no
                    del stack[i:]
                    break
    return lines, envs, labels, refs


def paragraph(lines, no):
    lo = no
    while lo > 1 and lines[lo - 2].strip():
        lo -= 1
    hi = no
    while hi < len(lines) and lines[hi].strip():
        hi += 1
    return lo, hi


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(2)
    root, target, out = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
    files = sorted(p.name for p in root.glob("*.tex"))
    scanned = {f: scan(root / f) for f in files}
    label_home = {}
    for f, (_, envs, labels, _) in scanned.items():
        for lab in labels:
            label_home[lab["label"]] = {"file": f, "line": lab["line"],
                                        "env": lab["within"][-1][0] if lab["within"] else None}

    lines, envs, labels, refs = scanned[target]
    top_envs = [e for e in envs if e["env"] in STATEMENT_ENVS | {"proof"}]
    stmt_label = {}
    for lab in labels:
        for env, start in lab["within"]:
            if env in STATEMENT_ENVS:
                stmt_label.setdefault(start, lab["label"])

    nodes, used_proofs = [], set()
    proofs = [e for e in envs if e["env"] == "proof"]
    for e in envs:
        if e["env"] not in STATEMENT_ENVS:
            continue
        lab = stmt_label.get(e["start"])
        proof = None
        for p in proofs:
            if lab and lab in p["opt"]:
                proof = p
        if proof is None:
            nxt = [p for p in proofs if p["start"] > e["end"] and not p["opt"]]
            if nxt and all(not lines[i - 1].strip() for i in range(e["end"] + 1, nxt[0]["start"])):
                proof = nxt[0]
        if proof:
            used_proofs.add(proof["start"])
        nodes.append({"id": lab, "rule": "S", "env": e["env"], "title_opt": e["opt"],
                      "statement_span": [e["start"], e["end"]],
                      "proof_span": [proof["start"], proof["end"]] if proof else None,
                      "span": [[e["start"], e["end"]]] + ([[proof["start"], proof["end"]]] if proof else []),
                      "outputs": [], "internal_eqs": [], "exported_eqs": []})

    def owner(no):
        for n in nodes:
            for lo, hi in n["span"]:
                if lo <= no <= hi:
                    return n
        return None

    referenced = {}
    for f, (_, _, _, rs) in scanned.items():
        for r in rs:
            referenced.setdefault(r["label"], []).append({"file": f, "line": r["line"]})

    excluded = []
    for lab in labels:
        envs_in = [x[0] for x in lab["within"]]
        if any(x in STATEMENT_ENVS for x in envs_in):
            n = owner(lab["line"])
            if n and lab["label"] != n["id"]:
                n["outputs"].append({"label": lab["label"], "line": lab["line"]})
            continue
        if "proof" in envs_in:
            n = owner(lab["line"])
            outside = [r for r in referenced.get(lab["label"], [])
                       if not (r["file"] == target and n and any(lo <= r["line"] <= hi for lo, hi in n["span"]))]
            item = {"label": lab["label"], "line": lab["line"], "refs_outside": outside}
            (n["exported_eqs"] if outside else n["internal_eqs"]).append(item)
            continue
        kind = envs_in[-1] if envs_in else None
        if kind in EQ_ENVS and referenced.get(lab["label"]):
            lo, hi = paragraph(lines, lab["line"])
            nodes.append({"id": lab["label"], "rule": "E", "env": kind, "span": [[lo, hi]],
                          "outputs": [{"label": lab["label"], "line": lab["line"]}],
                          "internal_eqs": [], "exported_eqs": []})
        else:
            excluded.append({"label": lab["label"], "line": lab["line"], "env": kind,
                             "referenced": bool(referenced.get(lab["label"]))})
    for e in envs:
        if e["env"] == "proof" and e["start"] not in used_proofs:
            excluded.append({"label": None, "line": e["start"], "env": "proof(주인 없음)"})

    nodes.sort(key=lambda n: n["span"][0][0])
    item_owner = {}
    for n in nodes:
        item_owner[n["id"]] = n["id"]
        for it in n["outputs"] + n["exported_eqs"] + n["internal_eqs"]:
            item_owner[it["label"]] = n["id"]

    edges, internal, unassigned, externals = [], [], [], {}
    for r in refs:
        to = owner(r["line"])
        home = label_home.get(r["label"])
        if home is None:
            unassigned.append({**r, "why": "label 정의 없음"})
            continue
        if home["file"] != target:
            src = "EXT:" + r["label"]
            externals.setdefault(src, {"id": src, "label": r["label"], **home})
        elif r["label"] in item_owner:
            src = item_owner[r["label"]]
        else:
            unassigned.append({**r, "why": "node가 아닌 label(제외 목록)"})
            continue
        if to is None:
            unassigned.append({**r, "why": "어느 node에도 들지 않는 줄", "from": src})
            continue
        if src == to["id"]:
            internal.append({**r, "node": src})
            continue
        edges.append({"from": src, "to": to["id"], "item": r["label"], "ref_line": r["line"], "cmd": r["cmd"]})

    consumers = {}
    for f, (_, _, _, rs) in scanned.items():
        if f == target:
            continue
        for r in rs:
            if r["label"] in item_owner or label_home.get(r["label"], {}).get("file") == target:
                cid = "OUT:" + f
                consumers.setdefault(cid, {"id": cid, "file": f, "uses": []})["uses"].append(
                    {"node": item_owner.get(r["label"]), "item": r["label"], "line": r["line"]})

    covered = sorted({i for n in nodes for lo, hi in n["span"] for i in range(lo, hi + 1)})
    gaps, cur = [], None
    for i in range(1, len(lines) + 1):
        if i not in covered and lines[i - 1].strip():
            if cur and cur[1] == i - 1:
                cur[1] = i
            else:
                cur = [i, i]
                gaps.append(cur)
            continue
        if i not in covered and cur and cur[1] == i - 1:
            cur[1] = i  # 빈 줄로 이어 붙인다
    gaps = [[lo, hi] for lo, hi in gaps if any(lines[j - 1].strip() for j in range(lo, hi + 1))]

    result = {"tool": "extract_tex.py", "root": str(root), "target": target,
              "lines": len(lines), "nodes": nodes, "external_inputs": sorted(externals.values(), key=lambda x: x["id"]),
              "consumers": sorted(consumers.values(), key=lambda x: x["id"]),
              "edges": edges, "internal_refs": internal, "unassigned_refs": unassigned,
              "excluded_labels": excluded, "uncovered_lines": gaps,
              "stats": {"nodes": len(nodes), "edges": len(edges), "internal_refs": len(internal),
                        "unassigned_refs": len(unassigned), "external_inputs": len(externals),
                        "consumers": len(consumers), "refs_total": len(refs)}}
    out.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(result["stats"], ensure_ascii=False))


if __name__ == "__main__":
    main()
