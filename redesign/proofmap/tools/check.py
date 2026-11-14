#!/usr/bin/env python3
"""증명 지도(proofmap/0.1) 검사. 표준 라이브러리만 쓴다.

    python3 redesign/proofmap/tools/check.py redesign/proofmap/graphs/move4.json

오류가 있으면 종료 코드 1. 경고와 상태 보고는 종료 코드에 영향이 없다.
검사하는 것은 구조다. 진술이 수학적으로 맞는지는 보지 않는다.
"""
import json
import sys

NODE_KINDS = {"object", "rule", "fact", "step", "external", "output"}
EDGE_KINDS = {"flow", "call", "definition"}
ABSTRACTIONS = {"exact", "weakening", "blackbox", "approximation", None}
MAX_INNER_NODES = 9


def check(doc):
    errors, warnings, report = [], [], []
    if doc.get("format") != "proofmap/0.1":
        errors.append(f"format 이 proofmap/0.1 이 아니다: {doc.get('format')!r}")
    graphs = {g["id"]: g for g in doc.get("graphs", [])}
    if len(graphs) != len(doc.get("graphs", [])):
        errors.append("graph id가 겹친다")

    for gid, g in graphs.items():
        where = f"[{gid}]"
        nodes = {n["id"]: n for n in g.get("nodes", [])}
        edges = g.get("edges", [])
        if len(nodes) != len(g.get("nodes", [])):
            errors.append(f"{where} node id가 겹친다")
        eids = [e["id"] for e in edges]
        if len(set(eids)) != len(eids):
            errors.append(f"{where} edge id가 겹친다")

        # 낱개 필드
        for n in nodes.values():
            if n.get("kind") not in NODE_KINDS:
                errors.append(f"{where} node {n['id']}: kind {n.get('kind')!r}")
            if n.get("abstraction") not in ABSTRACTIONS:
                errors.append(f"{where} node {n['id']}: abstraction {n.get('abstraction')!r}")
            if n.get("kind") == "external" and not n.get("external_ref") and g.get("parent"):
                errors.append(f"{where} 밖 node {n['id']}: external_ref 가 없다")
            sub = n.get("subgraph")
            if sub:
                if sub not in graphs:
                    errors.append(f"{where} node {n['id']}: subgraph {sub!r} 가 없다")
                elif graphs[sub].get("parent") != {"graph": gid, "node": n["id"]}:
                    errors.append(f"{where} node {n['id']}: subgraph {sub} 의 parent 가 이 node를 가리키지 않는다")
        for e in edges:
            if e.get("kind") not in EDGE_KINDS:
                errors.append(f"{where} edge {e['id']}: kind {e.get('kind')!r}")
            for end in ("from", "to"):
                if e.get(end) not in nodes:
                    errors.append(f"{where} edge {e['id']}: {end} {e.get(end)!r} 가 이 graph에 없다")
            if e.get("from") == e.get("to") and not e.get("loop"):
                errors.append(f"{where} edge {e['id']}: 자기 자신으로 가는데 loop(줄어드는 지표)가 없다")
            if e.get("complete") and not e.get("statement"):
                errors.append(f"{where} edge {e['id']}: complete 인데 statement 가 없다")
        for c in g.get("contexts", []):
            for nid in c.get("nodes", []):
                if nid not in nodes:
                    errors.append(f"{where} 문맥 {c['id']}: node {nid!r} 가 없다")

        # 받는 것이 가리키는 곳
        parent = g.get("parent")
        parent_ids = set()
        if parent:
            pg = graphs.get(parent["graph"])
            if not pg:
                errors.append(f"{where} parent graph {parent['graph']!r} 가 없다")
            else:
                parent_ids = {n["id"] for n in pg["nodes"]}
        for n in nodes.values():
            for i in n.get("inputs", []):
                if i not in nodes and i not in parent_ids:
                    errors.append(f"{where} node {n['id']}: 받는 것 {i!r} 가 이 graph에도 상위 graph에도 없다")

        # 닿는 면
        if parent and parent["graph"] in graphs:
            pnode = next((n for n in graphs[parent["graph"]]["nodes"] if n["id"] == parent["node"]), None)
            if pnode is None:
                errors.append(f"{where} parent node {parent['node']!r} 가 없다")
            else:
                want = set(pnode.get("inputs", []))
                have = {n["external_ref"] for n in nodes.values() if n.get("kind") == "external" and n.get("external_ref")}
                for c in g.get("contexts", []):
                    have |= set(c.get("provides", []))
                if want != have:
                    errors.append(f"{where} 닿는 면 불일치. 하위에 없는 입력: {sorted(want - have)}, 상위 node에 없는 입력: {sorted(have - want)}")
                if not any(n.get("kind") == "output" for n in nodes.values()):
                    errors.append(f"{where} 하위 graph인데 output node가 없다")

        # 순환 (귀납 고리는 뺀다)
        adj = {nid: [] for nid in nodes}
        for e in edges:
            if e.get("from") in nodes and e.get("to") in nodes and e["from"] != e["to"]:
                adj[e["from"]].append(e["to"])
        state = {}

        def dfs(u, path):
            state[u] = 1
            for v in adj[u]:
                if state.get(v) == 1:
                    errors.append(f"{where} 순환: {' → '.join(path[path.index(v):] + [v])}")
                elif v not in state:
                    dfs(v, path + [v])
            state[u] = 2

        for nid in nodes:
            if nid not in state:
                dfs(nid, [nid])

        # 쓰이지 않는 것
        touched = {e["from"] for e in edges} | {e["to"] for e in edges}
        has_out = {e["from"] for e in edges}
        for n in nodes.values():
            if n["id"] not in touched:
                warnings.append(f"{where} node {n['id']}: 어떤 edge에도 닿지 않는다")
            elif n["kind"] not in ("output", "external") and n["id"] not in has_out and parent:
                warnings.append(f"{where} node {n['id']}: 보내는 edge가 없다")

        # 완결이라고 한 node
        for n in nodes.values():
            if n.get("status") != "complete":
                continue
            inc = [e for e in edges if e["to"] == n["id"]]
            out = [e for e in edges if e["from"] == n["id"]]
            if n.get("subgraph"):
                sub = graphs.get(n["subgraph"])
                bad = [m["id"] for m in sub["nodes"] if m["kind"] in ("step", "rule", "fact") and m.get("status") != "complete"] if sub else []
                if bad:
                    errors.append(f"{where} node {n['id']}: 완결이라는데 하위 graph에 미완결 node가 있다: {bad}")
            elif not n.get("derivation"):
                errors.append(f"{where} node {n['id']}: 완결이라는데 derivation 도 subgraph 도 없다")
            for e in inc + out:
                if not e.get("complete"):
                    errors.append(f"{where} node {n['id']}: 완결이라는데 edge {e['id']} 가 내용을 다 싣지 않는다")
                if e.get("status") == "open":
                    errors.append(f"{where} node {n['id']}: 완결이라는데 edge {e['id']} 가 열려 있다")
            if n.get("derivation"):
                text = " ".join(d.get("by", "") for d in n["derivation"])
                for e in inc:
                    names = {e["id"], e.get("label", e["id"])}
                    if not any(nm.split(" ")[0] in text for nm in names):
                        warnings.append(f"{where} node {n['id']}: 받는 edge {e['id']} 를 유도의 근거에서 찾지 못했다")
                produced = {p["edge"] for p in n.get("produces", [])}
                for e in out:
                    if e["id"] not in produced:
                        errors.append(f"{where} node {n['id']}: 보내는 edge {e['id']} 가 어느 줄에서 나오는지(produces) 없다")

        # 상태 보고
        inner = [n for n in nodes.values() if n["kind"] not in ("external", "output")]
        if len(inner) > MAX_INNER_NODES:
            warnings.append(f"{where} 안쪽 node가 {len(inner)}개다(기준 {MAX_INNER_NODES}). 한 층을 더 둘 것")
        st = lambda s: sum(1 for n in inner if n.get("status") == s)
        filled = [f"{n['id']} 식 {i + 1}" for n in nodes.values() for i, d in enumerate(n.get("derivation", [])) if d.get("author_filled")]
        report.append(
            f"{where} {g['title']}: node {len(nodes)}(안쪽 {len(inner)}: 완결 {st('complete')}, 대강 {st('sketch')}, 미평가 {st(None)}), "
            f"edge {len(edges)}(내용 다 실음 {sum(1 for e in edges if e.get('complete'))}, 열림 {sum(1 for e in edges if e.get('status') == 'open')})"
            + (f", 작성자가 채운 줄: {', '.join(filled)}" if filled else "")
        )
    return errors, warnings, report


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    doc = json.load(open(sys.argv[1], encoding="utf-8"))
    errors, warnings, report = check(doc)
    for r in report:
        print("상태  ", r)
    for w in warnings:
        print("경고  ", w)
    for e in errors:
        print("오류  ", e)
    print(f"\n오류 {len(errors)}, 경고 {len(warnings)}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
