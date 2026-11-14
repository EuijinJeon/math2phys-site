#!/usr/bin/env python3
"""증명 지도 JSON에서 혼자 열리는 보기(HTML)를 만든다. 표준 라이브러리만 쓴다.

    python3 redesign/proofmap/tools/build_viewer.py redesign/proofmap/graphs/move4.json redesign/proofmap/build/move4.html

자료의 원본은 JSON이다. HTML은 생성물이므로 직접 고치지 않는다.
보기의 틀은 redesign/proofmap/viewer/template.html 이다. 수식 글꼴(KaTeX)만 인터넷에서 받는다.
"""
import json
import os
import sys

NODE_KIND = {"object": "obj", "external": "ext", "output": "out", "rule": "rule", "fact": "fact", "step": "step"}
EDGE_TYPE = {"definition": "def", "flow": "flow", "call": "call"}
EDGE_WORD = {"definition": "정의", "flow": "흐름", "call": "사실"}
STATUS = {"complete": "완결", "sketch": "미완결"}


def to_viewer(doc):
    maps, vertex = {}, {}
    for g in doc["graphs"]:
        nodes = {n["id"]: n for n in g["nodes"]}
        m = {"title": g["title"], "intro": g.get("summary", ""), "frames": [], "nodes": [], "edges": []}
        if g.get("parent"):
            m["parent"] = {"map": g["parent"]["graph"], "node": g["parent"]["node"]}
        for c in g.get("contexts", []):
            m["frames"].append({"id": c["id"], "cap": "문맥: " + c["text"], "nodes": c["nodes"], "provides": c.get("provides", [])})
        for n in g["nodes"]:
            gr = n.get("grounding", {})
            v = {
                "id": n["id"], "kind": NODE_KIND[n["kind"]], "title": n["title"], "short": n.get("summary", ""),
                "in": n.get("inputs", []), "cond": n.get("conditions", []), "out": n.get("statement", ""),
                "type": n.get("abstraction") or "-", "cards": gr.get("cards", []), "source": gr.get("source", ""),
                "lib": n.get("library") or "-", "col": n.get("layout", {}).get("col", 0), "row": n.get("layout", {}).get("row", 0),
            }
            for a, b in (("note", "note"), ("example", "example"), ("external_ref", "ref"), ("subgraph", "zoom")):
                if n.get(a):
                    v[b] = n[a]
            if n.get("inherit_statement"):
                v["pull"] = True
            if n.get("status"):
                v["status"] = STATUS[n["status"]]
            m["nodes"].append(v)
            if n.get("derivation"):
                name = lambda e: e.get("label", e["id"])
                produced = {p["edge"]: p["by"] for p in n.get("produces", [])}
                inc = [e for e in g["edges"] if e["to"] == n["id"]]
                out = [e for e in g["edges"] if e["from"] == n["id"]]
                vertex[n["id"]] = {
                    "map": g["id"], "atomic": True, "title": n["title"], "label": "완결된 vertex 보기" if n.get("status") == "complete" else "vertex 보기 (미완결)",
                    "where": n.get("note", ""), "source": gr.get("source", ""),
                    "context": n.get("local_context", []), "floor": n.get("floor_used", []),
                    "edgesIn": [{"id": name(e), "kind": EDGE_WORD[e["kind"]],
                                 "from": (nodes[e["from"]]["title"] + (" (귀납의 고리: " + e["loop"]["step"] + ")" if e.get("loop") else "")),
                                 "stmt": e.get("statement", ""), "src": e.get("grounding", {}).get("source", "")} for e in inc],
                    "node": {"kind": "원자 node — 계산 하나",
                             "chain": [{"expr": d["expr"], "by": d["by"], **({"flag": d["author_filled"]} if d.get("author_filled") else {})} for d in n["derivation"]]},
                    "edgesOut": [{"id": name(e), "kind": EDGE_WORD[e["kind"]],
                                  "to": (nodes[e["to"]]["title"] + (" (귀납의 고리: " + e["loop"]["step"] + ")" if e.get("loop") else "")),
                                  "stmt": e.get("statement", ""), "by": produced.get(e["id"], ""), "src": e.get("grounding", {}).get("source", "")} for e in out],
                    "checks": [[c["question"], c["answer"]] for c in n.get("review", {}).get("checks", [])],
                    "open": n.get("review", {}).get("open", []),
                }
        for e in g["edges"]:
            v = {"from": e["from"], "to": e["to"], "type": EDGE_TYPE[e["kind"]]}
            if e.get("complete"):
                v.update({"id": e.get("label", e["id"]), "short": e.get("summary", ""), "stmt": e.get("statement", ""),
                          "src": e.get("grounding", {}).get("source", ""), "nottaken": e.get("not_carried", "")})
                if e.get("in_complete_vertex"):
                    v["member"] = True
            else:
                v.update({"label": e.get("label", ""), "pass": e.get("statement", ""), "fit": e.get("fit", "")})
                if e.get("substitution"):
                    v["inst"] = e["substitution"]
            m["edges"].append(v)
        for d in g.get("drafts", []):
            if "payload" in d and d["node"] not in vertex:
                vertex[d["node"]] = d["payload"]
        maps[g["id"]] = m
    return maps, vertex


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    src, dst = sys.argv[1], sys.argv[2]
    doc = json.load(open(src, encoding="utf-8"))
    maps, vertex = to_viewer(doc)
    here = os.path.dirname(os.path.abspath(__file__))
    template = open(os.path.join(here, "..", "viewer", "template.html"), encoding="utf-8").read()
    dump = lambda x: json.dumps(x, ensure_ascii=False).replace("</", "<\\/")
    data = f"const MAPS = {dump(maps)};\nconst VERTEX = {dump(vertex)};\n"
    top = doc["graphs"][0]["id"]
    html = template.replace("/*__DATA__*/", data).replace("__TITLE__", "증명 지도 — " + doc["title"])
    html = html.replace("let cur = 'top',", f"let cur = {json.dumps(top)},").replace("MAPS.top.nodes", f"MAPS[{json.dumps(top)}].nodes").replace(": MAPS.top;", f": MAPS[{json.dumps(top)}];")
    os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(html)
    print(f"{dst}: graph {len(maps)}개, vertex 보기 {len(vertex)}개")


if __name__ == "__main__":
    main()
