#!/usr/bin/env python3
"""증명 지도 JSON에서 혼자 열리는 보기(HTML)를 만든다. 표준 라이브러리만 쓴다.

    python3 redesign/proofmap/tools/build_viewer.py redesign/proofmap/graphs/move4.json redesign/proofmap/build/move4.html

자료의 원본은 JSON이다. HTML은 생성물이므로 직접 고치지 않는다.
보기의 틀은 redesign/proofmap/viewer/template.html 이다. 수식 글꼴(KaTeX)만 인터넷에서 받는다.
"""
import json
import os
import sys
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location('proofmap_contracts', Path(__file__).with_name('output_contracts.py'))
contracts = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(contracts)
_integration_spec = importlib.util.spec_from_file_location('proofmap_integration', Path(__file__).with_name('integration_status.py'))
integration = importlib.util.module_from_spec(_integration_spec)
_integration_spec.loader.exec_module(integration)

NODE_KIND = {"object": "obj", "external": "ext", "output": "out", "rule": "rule", "fact": "fact", "step": "step"}
EDGE_TYPE = {"definition": "def", "flow": "flow", "call": "call"}
EDGE_WORD = {"definition": "정의", "flow": "흐름", "call": "사실"}
STATUS = {"complete": "완결", "sketch": "미완결"}


def completion_audit(doc):
    """표시용 구조 진단. 완결 선언을 승격하거나 수학적 참을 인증하지 않는다."""
    graphs = {g['id']: g for g in doc['graphs']}
    result, active = {}, set()
    bindings = contracts.contract_audit(doc)

    def audit(gid, nid):
        key = (gid, nid)
        if key in result:
            return result[key]
        if key in active:
            return {'state': 'incomplete', 'label': '미완결', 'issues': ['확대 연결 순환'], 'missing': []}
        active.add(key)
        g = graphs[gid]
        n = next(n for n in g['nodes'] if n['id'] == nid)
        inc = [e for e in g['edges'] if e['to'] == nid]
        incident = inc + [e for e in g['edges'] if e['from'] == nid]
        supplied = {s for c in g.get('contexts', []) if nid in c['nodes'] for s in c.get('provides', [])}
        missing = sorted(set(n.get('inputs', [])) - {e['from'] for e in inc} - supplied)
        issues = [f'입력 edge 없음: {i} → {nid}' for i in missing]
        issues.extend(bindings['nodes'].get((gid,nid), []))
        for e in {e['id']: e for e in incident}.values():
            if e.get('status') == 'open':
                issues.append(f"열린 edge: {e['id']}")
            if not e.get('complete'):
                issues.append(f"edge 내용 미작성: {e['id']}")
        child = None
        if n.get('subgraph'):
            sub = graphs.get(n['subgraph'])
            if sub is None:
                issues.append('확대 graph 없음')
            else:
                inner = [m for m in sub['nodes'] if m['kind'] not in ('external', 'output')]
                done = sum(audit(sub['id'], m['id'])['state'] == 'complete' for m in inner)
                child = {'done': done, 'total': len(inner), 'complete': done == len(inner)}
                if done != len(inner):
                    issues.append(f'하위 vertex 미완결: {len(inner) - done}/{len(inner)}')
                have = {m.get('external_ref') for m in sub['nodes'] if m['kind'] == 'external'}
                have |= {s for c in sub.get('contexts', []) for s in c.get('provides', [])}
                if have != set(n.get('inputs', [])):
                    issues.append('상위·하위 입력 경계 불일치')
        if n.get('status') == 'complete' and not n.get('subgraph') and not n.get('derivation'):
            issues.append('완결 선언에 유도 없음')
        if n['kind'] == 'external':
            state, label = 'external', '외부 입력'
        elif n['kind'] == 'output':
            state, label = 'output', '출력'
        elif issues or n.get('status') == 'sketch':
            state, label = 'incomplete', '미완결'
        elif n.get('status') == 'complete':
            state, label = 'complete', '국소 완결'
        else:
            state, label = 'unassessed', '미평가'
        value = {'state': state, 'label': label, 'issues': issues, 'missing': missing,
                 'declared': n.get('status'), 'child': child,
                 'contractIssues': bindings['nodes'].get((gid,nid), [])}
        result[key] = value
        active.remove(key)
        return value

    for gid, g in graphs.items():
        for n in g['nodes']:
            audit(gid, n['id'])
    return result


def to_viewer(doc):
    maps, vertex = {}, {}
    audits = completion_audit(doc)
    bindings = contracts.contract_audit(doc)
    coverage = integration.integration_status(doc, contracts, bindings)
    doc = contracts.resolve_document(doc)
    label_file = os.path.join(os.path.dirname(__file__), '..', 'viewer', 'edge-labels.json')
    with open(label_file, encoding='utf-8') as f:
        labels = json.load(f).get(doc.get('id'), {})
    for g in doc["graphs"]:
        nodes = {n["id"]: n for n in g["nodes"]}
        m = {"title": g["title"], "intro": g.get("summary", ""), "frames": [], "nodes": [], "edges": [],
             "premiseMode":g.get('premise_mode','legacy'),"coverage":coverage['graphs'][g['id']]}
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
                "audit": audits[(g['id'], n['id'])],
                "outputs": n.get('outputs', {}),
                "inputPorts": n.get('input_ports', {}),
                "importEdge": n.get('import_edge'), "statementRef": n.get('statement_ref'),
                "coverage":coverage['nodes'][(g['id'],n['id'])],
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
                name = lambda e: labels.get(g['id'], {}).get(e['id'], {}).get('id', e['id'].removeprefix(g['id'] + '-'))
                produced = {p["edge"]: p["by"] for p in n.get("produces", [])}
                inc = [e for e in g["edges"] if e["to"] == n["id"]]
                out = [e for e in g["edges"] if e["from"] == n["id"]]
                vertex[n["id"]] = {
                    "map": g["id"], "atomic": True, "title": n["title"], "label": "국소 완결 vertex 보기" if audits[(g['id'], n['id'])]['state'] == 'complete' else "vertex 보기 (미완결)",
                    "where": n.get("note", ""), "source": gr.get("source", ""),
                    "context": n.get("local_context", []), "floor": n.get("floor_used", []),
                    "premiseMode":g.get('premise_mode','legacy'), "introductions":n.get('introductions',[]),
                    "edgesIn": [{"id": name(e), "rawId": e['id'], "kind": EDGE_WORD[e["kind"]],
                                 "from": (nodes[e["from"]]["title"] + (" (귀납의 고리: " + e["loop"]["step"] + ")" if e.get("loop") else "")),
                                 "stmt": e.get("statement", ""), "src": e.get("grounding", {}).get("source", "")} for e in inc],
                    "node": {"kind": "원자 node — 계산 하나",
                             "chain": [{"expr": d["expr"], "by": d["by"], **({"flag": d["author_filled"]} if d.get("author_filled") else {})} for d in n["derivation"]]},
                    "edgesOut": [{"id": name(e), "rawId": e['id'], "kind": EDGE_WORD[e["kind"]],
                                  "to": (nodes[e["to"]]["title"] + (" (귀납의 고리: " + e["loop"]["step"] + ")" if e.get("loop") else "")),
                                  "stmt": e.get("statement", ""), "by": produced.get(e["id"], ""), "src": e.get("grounding", {}).get("source", "")} for e in out],
                    "checks": [[c["question"], c["answer"]] for c in n.get("review", {}).get("checks", [])],
                    "open": n.get("review", {}).get("open", []),
                }
        for e in g["edges"]:
            compact = labels.get(g['id'], {}).get(e['id'], {})
            default_id = e['id'].removeprefix(g['id'] + '-')
            v = {"from": e["from"], "to": e["to"], "type": EDGE_TYPE[e["kind"]],
                 "id": e['id'], "displayId": compact.get('id', default_id),
                 "caption": compact.get('caption', EDGE_WORD[e['kind']]),
                 "contentComplete": bool(e.get('complete')), "open": e.get('status') == 'open',
                 "contractIssues": bindings['edges'].get((g['id'],e['id']), []),
                 "outputRef": e.get('output_ref'), "useNote": e.get('use_note', '')}
            if e.get("complete"):
                v.update({"short": e.get("summary", ""), "stmt": e.get("statement", ""),
                          "src": e.get("grounding", {}).get("source", ""), "nottaken": e.get("not_carried", "")})
                if e.get("in_complete_vertex"):
                    v["member"] = True
            else:
                v.update({"label": e.get("label", ""), "pass": e.get("statement", ""), "fit": e.get("fit", "")})
                if e.get("substitution"):
                    v["inst"] = e["substitution"]
            m["edges"].append(v)
        display_ids = [e['displayId'] for e in m['edges']]
        if any(not isinstance(i, str) or not i for i in display_ids) or len(display_ids) != len(set(display_ids)):
            raise ValueError(f"[{g['id']}] edge 표시 ID는 비어 있지 않고 지도 안에서 유일해야 한다")
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
    with open(os.path.join(here, '..', 'viewer', 'edge-routing.js'), encoding='utf-8') as f:
        html = html.replace('/*__ROUTING__*/', f.read())
    html = html.replace("let cur = 'top',", f"let cur = {json.dumps(top)},").replace("MAPS.top.nodes", f"MAPS[{json.dumps(top)}].nodes").replace(": MAPS.top;", f": MAPS[{json.dumps(top)}];")
    os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(html)
    print(f"{dst}: graph {len(maps)}개, vertex 보기 {len(vertex)}개")
    for gid, m in maps.items():
        inner = [n for n in m['nodes'] if n['kind'] not in ('ext', 'out')]
        counts = {s: sum(n['audit']['state'] == s for n in inner) for s in ('complete', 'incomplete', 'unassessed')}
        print(f"  [{gid}] 국소 완결 {counts['complete']}, 미완결 {counts['incomplete']}, 미평가 {counts['unassessed']}")
        for n in inner:
            if n['audit']['missing']:
                print(f"    {n['id']}: {'; '.join(n['audit']['issues'])}")


if __name__ == "__main__":
    main()
