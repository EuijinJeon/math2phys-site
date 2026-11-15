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
_carries_spec = importlib.util.spec_from_file_location('proofmap_carries', Path(__file__).with_name('carries.py'))
carries_mod = importlib.util.module_from_spec(_carries_spec)
_carries_spec.loader.exec_module(carries_mod)
REPO = Path(__file__).resolve().parents[3]

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


def auto_layout(g):
    """layout 이 없는 node에 자리를 준다: edge를 따라 가장 긴 경로의 깊이를 열(col)로, 같은 열 안의 순서를 행(row)으로.
    저장된 layout 이 있는 node는 건드리지 않는다. 원본은 바꾸지 않는다(사본에만 쓴다)."""
    missing = [n for n in g["nodes"] if "layout" not in n]
    if not missing:
        return
    ids = [n["id"] for n in g["nodes"]]
    preds = {i: set() for i in ids}
    for e in g["edges"]:
        if e.get("from") in preds and e.get("to") in preds and e["from"] != e["to"]:
            preds[e["to"]].add(e["from"])
    depth = {}

    def d(i, seen=()):
        if i in depth:
            return depth[i]
        if i in seen:
            return 0
        depth[i] = 0 if not preds[i] else 1 + max(d(p, seen + (i,)) for p in preds[i])
        return depth[i]

    for i in ids:
        d(i)
    rows = {}
    for n in g["nodes"]:
        if "layout" in n:
            continue
        c = depth[n["id"]]
        n["layout"] = {"col": c, "row": rows.get(c, 0)}
        rows[c] = rows.get(c, 0) + 1


def first_file(ref, default="decorrelation.tex"):
    got = carries_mod.parse_ref(ref)
    return got[0][0] if got else default


def expand_refs(doc):
    """SPEC 7.7 [제안]: 화면에서 참조를 그 자리에 펼치기 위한 자료. 원본은 바꾸지 않는다.
    돌려주는 것: node별 추가 칸, edge별 추가 칸, 실을 원문 줄, 카드 번역."""
    root = REPO / doc.get("source", {}).get("root", "redesign/source/sections")
    sym = {x["id"]: x for x in doc.get("symbols", [])}
    graphs = {g["id"]: g for g in doc["graphs"]}
    nodes_of = {g["id"]: {n["id"]: n for n in g["nodes"]} for g in doc["graphs"]}
    ranges, cards = [], {}
    node_extra, edge_extra = {}, {}

    def rng(file, lines):
        if not lines:
            return None
        lo, hi = (lines[0], lines[-1]) if isinstance(lines, list) else (lines, lines)
        if not isinstance(lo, int) or not isinstance(hi, int):
            return None
        r = [file, min(lo, hi), max(lo, hi)]
        ranges.append(tuple(r))
        return r

    def used(file, xs):
        xs = sorted({x for x in xs if isinstance(x, int)})
        out, cur = [], None
        for x in xs:
            if cur and x <= cur[2] + 1:
                cur[2] = x
            else:
                cur = [file, x, x]
                out.append(cur)
        ranges.extend(tuple(r) for r in out)
        return out

    def refs(text):
        out = [list(r) for r in carries_mod.parse_ref(text)]
        ranges.extend(tuple(r) for r in out)
        return out

    def item_full(gid, nid, item):
        n = nodes_of[gid].get(nid)
        if not n:
            return None
        o = next((o for o in n.get("contract", {}).get("outputs", []) if o["id"] == item), None)
        if not o:
            return None
        f = first_file(n.get("grounding", {}).get("source", ""))
        return {"from": n["title"], "item": item, "statement": o["statement"], "lines": rng(f, o.get("lines")),
                "flag": o.get("author_filled", "")}

    floors = {x["id"]: x for x in doc.get("floors", [])}
    where = {}
    for g in doc["graphs"]:
        for n in g["nodes"]:
            lab = n.get("contract", {}).get("source_label")
            if lab and n.get("kind") != "external":
                where.setdefault(lab, (g["id"], n["id"]))

    def need_full(d, nf):
        """paper.json 의 입력 하나(contract.needs[] 에 binding 이 있는 꼴)를 화면용으로 펼친다."""
        b = d["binding"]
        out = {"what": d.get("what", d.get("id", "")), "type": b.get("type"), "origin": d.get("origin", []),
               "used": used(d.get("used_file", nf), d.get("used_at", []))}
        if b.get("type") == "node":
            gn = where.get(b.get("node"))
            out["target"] = item_full(gn[0], gn[1], b.get("item")) if gn else None
            out["jump"] = list(gn) if gn else None
            out["label"] = b.get("node")
        elif b.get("type") == "symbol":
            s = sym.get(b.get("symbol"))
            out["target"] = {"tex": s.get("tex") or s["id"], "text": s["text"], "at": refs(s["defined_at"])} if s else None
        elif b.get("type") == "floor":
            f = floors.get(b.get("floor"))
            out["target"] = {"statement": f.get("statement", ""), "kind": f.get("kind", ""), "cite": f.get("cite", ""),
                             "at": refs(f.get("cited_at", ""))} if f else None
        else:
            out["why"] = b.get("why", "")
        return out

    card_dir = REPO / "redesign/cards"
    for g in doc["graphs"]:
        gid = g["id"]
        parent = g.get("parent")
        for n in g["nodes"]:
            x = {}
            if n.get("contract", {}).get("outputs"):
                x["contract"] = [item_full(gid, n["id"], o["id"]) for o in n["contract"]["outputs"]]
            if n.get("symbols") or n.get("local_symbols"):
                x["symbols"] = [{"tex": sym[s].get("tex") or s, "text": sym[s]["text"], "at": refs(sym[s]["defined_at"])}
                                for s in n.get("symbols", []) if s in sym]
                x["symbols"] += [{"tex": s.get("tex", s.get("id")), "text": s.get("text", ""), "at": refs(s.get("defined_at", "")), "local": True}
                                 for s in n.get("local_symbols", [])]
            if n.get("kind") == "external" and n.get("import_edge") and parent:
                pe = next((e for e in graphs[parent["graph"]]["edges"] if e["id"] == n["import_edge"]), None)
                if pe:
                    want = set(n.get("items", [])) or {c["item"] for c in pe.get("carries", [])}
                    x["items"] = [item_full(parent["graph"], c["node"], c["item"]) for c in pe.get("carries", []) if c["item"] in want]
            if n.get("kind") == "external" and n.get("source_node"):
                # 2026-11-16 [제안]: 보내는 node 하나당 external 하나. 그 node 의 싣는 항목을 펼치고 원래 node 로 가는 단추를 둔다.
                sg, sn = n["source_node"]["graph"], n["source_node"]["node"]
                x["items"] = [it for it in (item_full(sg, sn, i) for i in n.get("items", [])) if it]
                x["jump"] = [sg, sn]
            if n.get("output_items") and parent:
                x["contract"] = [item_full(parent["graph"], parent["node"], i) for i in n["output_items"]]
            if n.get("lines"):
                x["lines"] = rng(n.get("source_file", "decorrelation.tex"), n["lines"])
            nf = first_file(n.get("grounding", {}).get("source", ""))
            needs = [d for d in n.get("contract", {}).get("needs", []) if isinstance(d, dict) and d.get("binding")]
            if needs:
                x["needs"] = [need_full(d, nf) for d in needs]
            if n.get("card"):
                p = card_dir / (n["card"].replace(":", ".") + ".md")
                if p.exists():
                    head = p.read_text(encoding="utf-8").split("---")[1]
                    import re as _re
                    m = _re.search(r"^math: \|\n((?:  .*\n)+)", head, _re.M)
                    t = _re.search(r"^title: '?(.*?)'?$", head, _re.M)
                    cards[n["card"]] = {"title": t.group(1) if t else n["card"], "math": "\n".join(l[2:] for l in m.group(1).splitlines()) if m else ""}
                x["card"] = n["card"]
            af = n.get("author_filled")
            if isinstance(af, list):
                x["filled"] = [a if isinstance(a, str) else (a.get("what", "") + (" " + a["expr"] if a.get("expr") else "")) for a in af]
            elif af:
                x["filled"] = [af]
            x["groundingRefs"] = refs(n.get("grounding", {}).get("source", ""))
            node_extra[(gid, n["id"])] = x
        for e in g["edges"]:
            cs = e.get("carries") or []
            y = {"srcRefs": refs(e.get("grounding", {}).get("source", ""))}
            ef = first_file(nodes_of[gid].get(e.get("to"), {}).get("grounding", {}).get("source", ""))
            if cs and isinstance(cs[0], dict) and cs[0].get("node"):
                y["carries"] = [dict(item_full(c.get("graph", gid), c["node"], c["item"]) or {"item": c["item"]},
                                     used=used(c.get("used_file", ef), c.get("used_at", [])), origin=c.get("origin", ""))
                                for c in cs]
            elif cs:
                src_node = next((m for m in g["nodes"] if m["id"] == e["from"]), {})
                pe = None
                if src_node.get("kind") == "external" and src_node.get("import_edge") and parent:
                    pe = next((x for x in graphs[parent["graph"]]["edges"] if x["id"] == src_node["import_edge"]), None)
                y["carries"] = []
                for c in cs:
                    name = c if isinstance(c, str) else c.get("item")
                    u = used("decorrelation.tex", (e.get("used_at", []) if isinstance(c, str) else c.get("used_at", [])))
                    full = None
                    if pe:
                        pc = next((x for x in pe.get("carries", []) if x["item"] == name), None)
                        full = item_full(parent["graph"], pc["node"], pc["item"]) if pc else None
                    if full:
                        y["carries"].append(dict(full, used=u))
                    elif src_node.get("lines"):
                        # 구조만 판(C): 앞 node의 결과 = 그 node의 원문 줄. 이름만 두지 않고 원문을 붙인다.
                        y["carries"].append({"item": name, "used": u, "fromTitle": src_node.get("title", e["from"]),
                                             "fromRange": rng("decorrelation.tex", src_node["lines"])})
                    else:
                        y["carries"].append({"item": name, "used": u})
            edge_extra[(gid, e["id"])] = y
    # 진술 글 안에 남은 원문 label(예: pert:selection)과 [NODE.item] 꼴을 화면에서 펼치기 위한 색인.
    import re as _re
    _ext_spec = importlib.util.spec_from_file_location('proofmap_extract', Path(__file__).with_name('extract_tex.py'))
    ext = importlib.util.module_from_spec(_ext_spec)
    _ext_spec.loader.exec_module(ext)
    text = json.dumps(doc, ensure_ascii=False) + json.dumps(cards, ensure_ascii=False)  # 카드 번역 안의 id도 펼친다
    wanted = set(_re.findall(r"\b((?:decor|pert|tree|comp|cavity|model|upper|reduction|cons|intro|over|main|x)[a-z]*:[a-z0-9.-]*[a-z0-9])", text))
    labels = {}
    for f in sorted(root.glob("*.tex")):
        _, envs, labs, _ = ext.scan(f)
        for lab in labs:
            if lab["label"] not in wanted:
                continue
            span = (lab["line"], lab["line"])
            if lab["within"]:
                env = next((e for e in envs if e["start"] == lab["within"][-1][1] and e["env"] == lab["within"][-1][0]), None)
                if env and env["end"]:
                    span = (env["start"], env["end"])
            labels[lab["label"]] = [f.name, span[0], span[1]]
            ranges.append((f.name, span[0], span[1]))
    # 글 안에 나오는 카드 id(예: x:decor-topology)는 카드 제목과 번역(math)으로 펼친다. 카드는 읽기만 한다.
    for _depth in range(3):  # 카드 번역 안에 나오는 카드도 세 겹까지
        for cid in sorted(wanted):
            cp = card_dir / (cid.replace(":", ".") + ".md")
            if cid not in cards and cp.exists():
                head = cp.read_text(encoding="utf-8").split("---")[1]
                m = _re.search(r"^math: \|\n((?:  .*\n)+)", head, _re.M)
                t = _re.search(r"^title: '?(.*?)'?$", head, _re.M)
                cards[cid] = {"title": t.group(1) if t else cid, "math": "\n".join(l[2:] for l in m.group(1).splitlines()) if m else ""}
        wanted |= set(_re.findall(r"\b((?:decor|pert|tree|comp|cavity|model|upper|reduction|cons|intro|over|main|x)[a-z]*:[a-z0-9.-]*[a-z0-9])", json.dumps(cards, ensure_ascii=False)))
    items = {}
    top = doc["graphs"][0]
    for n in top["nodes"]:
        for o in n.get("contract", {}).get("outputs", []):
            items[f"{n['id']}.{o['id']}"] = item_full(top["id"], n["id"], o["id"])
    label_node = {n.get("contract", {}).get("source_label"): n["id"] for n in top["nodes"] if n.get("contract", {}).get("source_label")}
    node_titles = {}
    for n in top["nodes"]:
        for lab in n.get("contract", {}).get("labels", []):
            label_node.setdefault(lab, n["id"])
    for g in doc["graphs"][1:]:
        for n in g["nodes"]:
            c = n.get("contract", {})
            if n.get("kind") == "external" or not c.get("source_label"):
                continue
            for lab in [c["source_label"]] + c.get("labels", []):
                if lab not in label_node:
                    label_node[lab] = [g["id"], n["id"]]
                    node_titles[n["id"]] = n["title"]
    by_file = {}
    for f, lo, hi in ranges:
        by_file.setdefault(f, []).append((f, lo, hi))
    src = {}
    cache = {}
    for f, rs in by_file.items():
        got = carries_mod.source_lines(root, rs, cache)
        src.update(got)
    cards["__labels__"] = labels
    cards["__items__"] = items
    cards["__label_node__"] = label_node
    cards["__top_nodes__"] = {n["id"]: n["title"] for n in top["nodes"]}
    cards["__node_titles__"] = node_titles
    cards["__top__"] = top["id"]
    return node_extra, edge_extra, src, cards


def to_viewer(doc):
    """예전 시험(test_viewer.py)과 같은 (maps, vertex) 를 돌려준다."""
    return to_viewer_full(doc)[:2]


def to_viewer_full(doc):
    maps, vertex = {}, {}
    doc = carries_mod.resolve(doc)
    for g in doc["graphs"]:
        auto_layout(g)
    node_extra, edge_extra, src_lines, card_text = expand_refs(doc)
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
                "x": node_extra.get((g['id'], n['id']), {}),
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
                 "outputRef": e.get('output_ref'), "useNote": e.get('use_note', ''),
                 "x": edge_extra.get((g['id'], e['id']), {})}
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
    return maps, vertex, src_lines, card_text


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    src, dst = sys.argv[1], sys.argv[2]
    doc = json.load(open(src, encoding="utf-8"))
    maps, vertex, src_lines, card_text = to_viewer_full(doc)
    here = os.path.dirname(os.path.abspath(__file__))
    template = open(os.path.join(here, "..", "viewer", "template.html"), encoding="utf-8").read()
    dump = lambda x: json.dumps(x, ensure_ascii=False).replace("</", "<\\/")
    data = f"const MAPS = {dump(maps)};\nconst VERTEX = {dump(vertex)};\nconst SRCLINES = {dump(src_lines)};\nconst CARDTEXT = {dump(card_text)};\n"
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
