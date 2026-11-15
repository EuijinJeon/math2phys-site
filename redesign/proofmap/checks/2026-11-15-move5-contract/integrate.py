#!/usr/bin/env python3
"""여는 작업의 산출(open-<NODE>.out.json)을 graphs/move5.json 에 넣고 둘레를 잰다.

    python3 .../integrate.py NODE            # 검사·삽입
    python3 .../integrate.py --diff A.json B.json NODE   # 둘레 밖 변경 세기

삽입은 하위 graph를 graphs 에 더하고 부모 node 에 subgraph 를 다는 일만 한다.
parent_change_requests 는 자동 적용하지 않는다(작성자가 판정해 JSON에서 고치고 센다).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOC = HERE.parents[1] / "graphs/move5.json"


def count_author_filled(g):
    n = 0
    for node in g["nodes"]:
        n += bool(node.get("author_filled"))
        n += sum(bool(d.get("author_filled")) for d in node.get("derivation", []))
    n += sum(bool(e.get("author_filled")) for e in g["edges"])
    return n


def insert(nid):
    doc = json.loads(DOC.read_text(encoding="utf-8"))
    res = json.loads((HERE / f"open-{nid}.out.json").read_text(encoding="utf-8"))
    sub = res["graph"]
    # 묶음 지시(bundle_format.md)가 derivation 줄의 꼴을 정하지 않았다. 규격 꼴(expr, by 문자열)로
    # 기계적으로 옮기고 원래 목록은 by_refs 에 남긴다. 내용은 바꾸지 않는다.
    normalized = 0
    for node in sub["nodes"]:
        for d in node.get("derivation", []):
            if "expr" not in d and "line" in d:
                d["expr"] = d.pop("line")
                normalized += 1
            if isinstance(d.get("by"), list):
                d["by_refs"] = d["by"]
                d["by"] = "; ".join(d["by"])
                normalized += 1
    # 묶음 지시가 produces 를 요구하지 않았다. 보내는 edge가 하나뿐인 complete node는
    # 마지막 유도 줄을 produces 로 기계 보충하고 표시한다. 둘 이상이면 sketch 로 내린다.
    produced_filled, downgraded = 0, []
    for node in sub["nodes"]:
        if node.get("status") != "complete" or node.get("produces"):
            continue
        outs_ = [e["id"] for e in sub["edges"] if e["from"] == node["id"]]
        if len(outs_) == 1 and node.get("derivation"):
            node["produces"] = [{"edge": outs_[0], "by": "마지막 줄 (통합 단계에서 기계 보충)"}]
            produced_filled += 1
        else:
            node["status"] = "sketch"
            downgraded.append(node["id"])
    top = doc["graphs"][0]
    pnode = next(n for n in top["nodes"] if n["id"] == nid)
    inc = {e["id"]: e for e in top["edges"] if e["to"] == nid}
    outg = [e for e in top["edges"] if e["from"] == nid]
    problems = []
    if sub.get("parent") != {"graph": "top", "node": nid}:
        problems.append(f"parent 가 top.{nid} 가 아니다: {sub.get('parent')}")
    ext = [n for n in sub["nodes"] if n["kind"] == "external"]
    refs = {n.get("external_ref") for n in ext}
    if refs != set(pnode.get("inputs", [])):
        problems.append(f"닿는 면: 하위 {sorted(refs - {None})} / 상위 {pnode.get('inputs', [])}")
    for n in ext:
        e = inc.get(n.get("import_edge"))
        if e is None:
            problems.append(f"{n['id']}: import_edge {n.get('import_edge')} 가 받는 edge가 아니다")
            continue
        have = {c["item"] for c in e["carries"]}
        extra = set(n.get("items", [])) - have
        if extra:
            problems.append(f"{n['id']}: {e['id']} 가 싣지 않는 항목 {sorted(extra)}")
        if not n.get("items"):
            problems.append(f"{n['id']}: 쓰는 항목이 없다 ({e['id']})")
    outs = [n for n in sub["nodes"] if n["kind"] == "output"]
    covered = {i for n in outs for i in n.get("output_items", [])}
    contract_items = {o["id"] for o in pnode["contract"]["outputs"]}
    sent = {c["item"] for e in outg for c in e["carries"]}
    if sent - covered:
        problems.append(f"보내는 edge 항목 중 output 이 없는 것: {sorted(sent - covered)}")
    if covered - contract_items:
        problems.append(f"계약에 없는 출력 항목: {sorted(covered - contract_items)}")
    inner = [n for n in sub["nodes"] if n["kind"] not in ("external", "output")]
    st = {s: sum(1 for n in inner if n.get("status") == s) for s in ("complete", "sketch")}
    stats = {"node": nid, "inner_nodes": len(inner), "status": st, "edges": len(sub["edges"]),
             "externals": len(ext), "outputs": len(outs), "format_normalized": normalized, "produces_filled": produced_filled, "downgraded": downgraded,
             "author_filled": count_author_filled(sub),
             "parent_change_requests": len(res.get("parent_change_requests", [])),
             "missed_dependencies": len(res.get("missed_dependencies", [])),
             "uncovered_contract_items": sorted(contract_items - covered),
             "problems": problems}
    doc["graphs"] = [g for g in doc["graphs"] if g["id"] != sub["id"]] + [sub]
    pnode["subgraph"] = sub["id"]
    DOC.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=1))


def diff(a, b, nid):
    """top graph와 기호 표에서 vertex nid 둘레 밖의 변경을 센다."""
    A, B = (json.loads(Path(p).read_text(encoding="utf-8")) for p in (a, b))
    ta, tb = A["graphs"][0], B["graphs"][0]

    def perimeter(t):
        return {e["id"] for e in t["edges"] if nid in (e["from"], e["to"])}

    per = perimeter(ta) | perimeter(tb)
    strip = lambda n: {k: v for k, v in n.items() if k not in ("subgraph", "layout")}
    na, nb = ({n["id"]: strip(n) for n in t["nodes"]} for t in (ta, tb))
    ea, eb = ({e["id"]: e for e in t["edges"]} for t in (ta, tb))
    sa, sb = ({s["id"]: s for s in X["symbols"]} for X in (A, B))
    out = {"nodes_changed": [], "nodes_added": [], "edges_changed": [], "edges_added": [],
           "symbols_changed": [], "symbols_added": [], "inside_perimeter": []}
    for k in nb:
        if k not in na:
            out["nodes_added"].append(k)
        elif na[k] != nb[k]:
            (out["inside_perimeter"] if k == nid else out["nodes_changed"]).append(k)
    for k in eb:
        if k not in ea:
            (out["inside_perimeter"] if k in per else out["edges_added"]).append(k)
        elif ea[k] != eb[k]:
            (out["inside_perimeter"] if k in per else out["edges_changed"]).append(k)
    for k in sb:
        if k not in sa:
            out["symbols_added"].append(k)
        elif sa[k] != sb[k]:
            out["symbols_changed"].append(k)
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    if sys.argv[1] == "--diff":
        diff(*sys.argv[2:5])
    else:
        insert(sys.argv[1])
