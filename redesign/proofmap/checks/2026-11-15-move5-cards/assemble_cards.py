#!/usr/bin/env python3
"""P2: 카드 뼈대(skeletons.json) + LLM 채움(P2-fill.json) → 원문 참조 판(SPEC 7.8) 하위 graph.

    python3 assemble_cards.py MOVE5.json NODE OUT.json

진술을 새로 쓰지 않는다. 안쪽 node = 카드(원문 줄 + 카드 id), edge = 뼈대 edge + LLM이 찾은 '카드에 없는 의존'.
external이 싣는 항목 이름은 카드가 정하지 않으므로 ITEMS 표(작성자, 손으로)로 정한다.
바닥(floor:...)으로 온 누락은 node의 floor_used 에 넣는다. 모든 안쪽 node는 sketch.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (node, external top id, 받는 걸음) → 싣는 항목. 작성자 판정(LLM의 edge_used_at note 와 원문 줄을 보고 정함).
ITEMS = {
    ("DC", "AVG", "k1"): ["unused_coord"], ("DC", "AVG", "k3"): ["unused_coord"], ("DC", "AVG", "k4"): ["shift_regular"],
    ("DC", "X_SAMP", "k2"): ["children_independent"], ("DC", "X_SAMP", "k4"): ["leaf_removal"],
    ("PB", "X_SAMP", "k1"): ["children_independent"], ("PB", "X_SAMP", "k2"): ["children_independent"],
    ("PB", "CON", "k2"): ["contraction"],
}


def main():
    doc = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    nid, out = sys.argv[2], sys.argv[3]
    sk = json.loads((HERE / "skeletons.json").read_text(encoding="utf-8"))[nid]
    fill = json.loads((HERE / "P2-fill.json").read_text(encoding="utf-8"))[nid]
    top = doc["graphs"][0]
    tn = {n["id"]: n for n in top["nodes"]}
    tedges = {(e["from"], e["to"]): e for e in top["edges"]}
    pnode = tn[nid]
    gid = nid.lower()
    nodes, edges = [], []
    used = {(u["from"], u["to"]): u for u in fill["edge_used_at"]}
    af = {}
    for a in fill["author_filled"]:
        af.setdefault(a["at"], []).append({"what": a["what"]})
    floors = {}
    for m in fill["missing"]:
        if str(m["from"]).startswith("floor:"):
            floors.setdefault(m["to"], []).append(m["from"][6:])
    for x in sk["inner"]:
        nodes.append({"id": x["id"], "kind": "step", "title": x["title"], "lines": x["lines"], "card": x["card"],
                      "status": "sketch", **({"author_filled": af[x["id"]]} if x["id"] in af else {}),
                      **({"floor_used": floors[x["id"]]} if x["id"] in floors else {}),
                      "grounding": {"source": f"decorrelation.tex {x['lines'][0]}–{x['lines'][1]}", "state": "proposed"}})
    ext_items = {}
    seen = set()

    def add_edge(frm, to, carries, lines, origin, note=None):
        key = (frm, to, tuple(carries))
        if key in seen:
            return
        seen.add(key)
        e = {"id": f"c{len(edges) + 1}", "from": frm, "to": to, "kind": "call" if frm.startswith("x_") else "flow",
             "carries": carries, "used_at": lines or [], "origin": origin, "status": "connected"}
        if note:
            e["note"] = note
        edges.append(e)

    for e in sk["edges"]:
        u = used.get((e["from"], e["to"]), {})
        if not u.get("lines"):
            continue  # LLM이 원문에서 쓰임을 못 찾은 뼈대 edge는 넣지 않고 보고서에 센다
        if e["from"].startswith("x_"):
            t = e["from"][2:]
            if t not in pnode.get("inputs", []):
                continue  # 계약이 그 입력을 갖지 않음 → 보고서에 '카드가 말하는 의존, 계약에 없음'으로 센다
            items = ITEMS.get((nid, t, e["to"]))
            if not items:
                items = [c["item"] for c in tedges[(t, nid)]["carries"]]
            ext_items.setdefault(t, set()).update(items)
            add_edge(e["from"], e["to"], items, u["lines"], "card", u.get("note"))
        else:
            add_edge(e["from"], e["to"], ["result"], u["lines"], "card", u.get("note"))
    for m in fill["missing"]:
        if str(m["from"]).startswith("floor:") or m["from"] == "모름":
            continue
        frm = m["from"]
        if "." in frm:
            t, item = frm.split(".", 1)
            if t not in pnode.get("inputs", []):
                continue
            ext_items.setdefault(t, set()).add(item)
            add_edge("x_" + t, m["to"], [item], m.get("lines"), "llm_fill", m["what"])
        else:
            add_edge(frm, m["to"], ["result"], m.get("lines"), "llm_fill", m["what"])
    for t in pnode.get("inputs", []):
        te = tedges[(t, nid)]
        nodes.append({"id": "x_" + t, "kind": "external", "title": tn[t]["title"], "external_ref": t,
                      "import_edge": te["id"], "items": sorted(ext_items.get(t, set()))})
    # 출력: 계약 항목마다, 원문 줄이 들어가는 마지막 안쪽 걸음에서 나온다(기계 대응).
    for o in pnode["contract"]["outputs"]:
        lo, hi = o["lines"]
        src = [x for x in sk["inner"] if x["lines"][0] <= hi and lo <= x["lines"][1]]
        oid = "o_" + o["id"]
        nodes.append({"id": oid, "kind": "output", "title": o["id"], "output_items": [o["id"]], "lines": [lo, hi]})
        if src:
            add_edge(src[-1]["id"], oid, ["result"], [hi], "machine_output")
        else:
            nodes[-1]["note"] = "계약 항목의 줄이 어느 카드 걸음에도 걸치지 않는다(진술 안의 항목). 증명 걸음에서 오지 않는다"
    sub = {"id": gid, "title": f"{pnode['title']} — 카드 뼈대 판", "parent": {"graph": "top", "node": nid},
           "summary": "카드(redesign/cards)의 경계와 의존에서 기계로 만든 뼈대에, LLM이 카드에 없는 의존과 원문에 없는 걸음만 채웠다. 진술은 원문 줄과 카드 번역이다(SPEC 7.8).",
           "build": {"skeleton": "card_skeleton.py", "fill": "P2-fill.json", "assemble": "assemble_cards.py"},
           "card_mismatch": fill["mismatch"],
           "nodes": nodes, "edges": edges}
    Path(out).write_text(json.dumps(sub, ensure_ascii=False, indent=1), encoding="utf-8")
    print(nid, "inner", len(sk["inner"]), "edges", len(edges), "ext", len(pnode.get("inputs", [])))


if __name__ == "__main__":
    main()
