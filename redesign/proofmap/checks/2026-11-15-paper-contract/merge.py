#!/usr/bin/env python3
"""절 산출(out/*.json)을 `graphs/paper.json` 으로 합치고 측정값을 낸다.

    python3 merge.py            # graphs/paper.json, stats.json 을 쓴다

- 맨 위 graph `top`: 절 node 11개 + 주정리 node `MAIN`(model.tex 의 main:theorem). 절 → 절 edge 는
  절을 건너는 입력의 항목을 싣는다(`carries[].graph` = 보낸 node 가 있는 하위 graph).
- 하위 graph `s_<절>`: 그 절의 node, 다른 절마다 external 하나(`external_ref` = 그 절, `import_edge` = 맨 위 edge),
  output node 하나(밖에서 쓰는 항목을 받는다).
- 입력(`contract.needs[]`)은 산출 그대로 두고 `binding` 을 검사한다. node 묶음의 항목이 대상에 없으면
  `new_item` 으로 **추가**하고 센다. 내용 변경 요청은 적용하지 않고 센다.
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PM = HERE.parents[1]
SECS = ["introduction", "model", "overview", "trees", "upper", "cavity", "perturbations",
        "decorrelation", "comparison", "reduction", "consequences"]
TITLES = {"introduction": "§1 서론", "model": "§2 모형과 변분 원리", "overview": "§2.2 증명 전략",
          "trees": "§3 유한 tree 위의 미적분", "upper": "§4 interpolation 상한", "cavity": "§5 섭동된 cavity reservoir",
          "perturbations": "§6 섭동과 prescribed tree 위의 항등식", "decorrelation": "§7 prescribed tree 위의 decorrelation",
          "comparison": "§8 독립 계층 message와 cavity 비교", "reduction": "§9 정규화, truncation, 증명의 완성",
          "consequences": "§10 명명 모형과 영온도 극한"}
MAIN = "main:theorem"


def span_text(file, spans):
    return file + " " + ", ".join(f"{a}–{b}" for a, b in spans if a is not None)


def main():
    sk = json.loads((HERE / "skeleton.json").read_text(encoding="utf-8"))
    skn = {n["id"]: n for n in sk["nodes"]}
    outs = {}
    for p in sorted((HERE / "out").glob("*.json")):
        outs[p.stem] = json.loads(p.read_text(encoding="utf-8"))
    log = defaultdict(list)

    # node 모으기
    node, sec_of = {}, {}
    for sec, d in outs.items():
        for n in d["nodes"]:
            if n["id"] in node:
                log["duplicate_node"].append(n["id"])
                continue
            node[n["id"]] = n
            sec_of[n["id"]] = "MAIN" if n["id"] == MAIN else skn[n["id"]]["section"]
    missing = [k for k in skn if k not in node]
    label_to = {}
    for k, s in skn.items():
        for lab in [k] + s.get("merged_labels", []) + s["output_labels"] + s["exported"] + s["internal"]:
            label_to[lab] = k

    def outputs(nid):
        return node[nid].setdefault("outputs", [])

    for nid, n in node.items():
        for o in outputs(nid):
            if o.get("added_by"):
                log["item_added"].append({"node": nid, "item": o["id"], "by": o["added_by"], "where": "same_agent"})

    # 기호·바닥: 같은 id 가 다른 정의 위치면 이름을 갈라 둔다.
    symbols, sym_rename, floors, floor_rename = {}, {}, {}, {}
    for sec, d in outs.items():
        for s in d.get("symbols_new", []):
            if s["id"] in symbols:
                if symbols[s["id"]]["defined_at"] == s["defined_at"]:
                    log["symbol_dup_same"].append({"id": s["id"], "sec": sec})
                    continue
                new = f"{s['id']}@{sec}"
                sym_rename[(sec, s["id"])] = new
                log["symbol_dup_diff"].append({"id": s["id"], "sec": sec, "first": symbols[s["id"]]["defined_at"], "this": s["defined_at"]})
                s = dict(s, id=new)
            symbols[s["id"]] = dict(s, section=sec)
        for f in d.get("floors_new", []):
            if f["id"] in floors:
                if floors[f["id"]].get("statement") == f.get("statement"):
                    log["floor_dup_same"].append({"id": f["id"], "sec": sec})
                    continue
                new = f"{f['id']}@{sec}"
                floor_rename[(sec, f["id"])] = new
                log["floor_dup_diff"].append({"id": f["id"], "sec": sec})
                f = dict(f, id=new)
            floors[f["id"]] = dict(f, section=sec)
        for c in d.get("change_requests", []):
            log["change_request"].append(dict(c, from_section=sec))
        for u in d.get("unplaced", []):
            log["unplaced"].append(dict(u, section=sec))

    # 통합자 보정 (corrections.json): 묶음 하나를 바꾸고 센다.
    corr = json.loads((HERE / "corrections.json").read_text(encoding="utf-8")) if (HERE / "corrections.json").exists() else []
    for c in corr:
        n = node.get(c["node"])
        nd = next((x for x in (n or {}).get("needs", []) if x.get("id") == c["need"]), None)
        if nd is None:
            log["correction_missed"].append(c)
            continue
        nd["binding_by_author"] = nd["binding"]
        nd["binding"] = dict(c["binding"])
        nd["integrator_note"] = c["why"]
        log["correction"].append(c)

    # 입력 검사와 항목 추가
    for sec, d in outs.items():
        for n in d["nodes"]:
            for nd in n.get("needs", []):
                b = nd.setdefault("binding", {"type": "open", "why": "binding 없음"})
                t = b.get("type")
                if t == "symbol":
                    b["symbol"] = sym_rename.get((sec, b.get("symbol")), b.get("symbol"))
                    if b["symbol"] not in symbols:
                        log["bad_binding"].append({"node": n["id"], "need": nd.get("id"), "why": f"기호 {b['symbol']} 없음"})
                elif t == "floor":
                    b["floor"] = floor_rename.get((sec, b.get("floor")), b.get("floor"))
                    if b["floor"] not in floors:
                        log["bad_binding"].append({"node": n["id"], "need": nd.get("id"), "why": f"바닥 {b['floor']} 없음"})
                elif t == "node":
                    tgt = b.get("node")
                    if tgt not in node and tgt in label_to:
                        b["label_cited"], tgt = tgt, label_to[tgt]
                        b["node"] = tgt
                    if tgt not in node:
                        log["bad_binding"].append({"node": n["id"], "need": nd.get("id"), "why": f"node {tgt} 없음"})
                        continue
                    if tgt == n["id"]:
                        log["bad_binding"].append({"node": n["id"], "need": nd.get("id"), "why": "자기 자신"})
                        continue
                    have = {o["id"] for o in outputs(tgt)}
                    if b.get("item") not in have:
                        ni = b.get("new_item")
                        if ni:
                            outputs(tgt).append({"id": b["item"], "statement": ni["statement"], "lines": ni.get("lines"),
                                                 "added_by": n["id"], **({"author_filled": ni["author_filled"]} if ni.get("author_filled") else {})})
                            log["item_added"].append({"node": tgt, "item": b["item"], "by": n["id"], "where": "request"})
                        else:
                            log["bad_binding"].append({"node": n["id"], "need": nd.get("id"), "why": f"항목 {tgt}.{b.get('item')} 없음"})
                    b.pop("new_item", None)
                elif t != "open":
                    log["bad_binding"].append({"node": n["id"], "need": nd.get("id"), "why": f"종류 {t}"})
                if t != "open" and not nd.get("used_at"):
                    log["no_used_at"].append({"node": n["id"], "need": nd.get("id")})

    # graph 짓기
    gid = lambda s: "top" if s == "MAIN" else f"s_{s}"
    top_nodes, top_edges, subs = [], {}, {}
    used_out = defaultdict(lambda: defaultdict(set))  # (sec) -> node -> items 밖에서 쓰임
    for sec in SECS:
        nids = [k for k in node if sec_of[k] == sec]
        nids.sort(key=lambda k: skn[k]["span"][0][0])
        tn = {"id": sec, "kind": "step" if nids else "object", "title": TITLES[sec],
              "summary": f"번호 붙은 진술 {len(nids)}개" if nids else "번호 붙은 진술 없음(산문)",
              "inputs": [], "abstraction": "exact", "status": "sketch",
              "grounding": {"source": f"{sec}.tex 1–{sum(1 for _ in open(PM.parent / 'source/sections' / (sec + '.tex'), encoding='utf-8'))}", "state": "proposed"},
              "library": "미대조"}
        if nids:
            tn["subgraph"] = gid(sec)
        top_nodes.append(tn)

    def pnode(nid):
        n, s = node[nid], skn[nid]
        sp = [n.get("statement_span") or s["span"][0]]
        if n.get("proof_span"):
            sp.append(n["proof_span"])
        file = n.get("proof_file") if False else s["file"]
        src = span_text(file, [sp[0]]) + (f"; {n['proof_file']} {n['proof_span'][0]}–{n['proof_span'][1]}" if n.get("proof_file") else (", " + f"{sp[1][0]}–{sp[1][1]}" if len(sp) > 1 else ""))
        syms = sorted({x["binding"]["symbol"] for x in n.get("needs", []) if x["binding"].get("type") == "symbol" and x["binding"].get("symbol") in symbols})
        out = {"id": nid, "kind": "step" if s["rule"] == "S" else "object", "title": n.get("title", nid),
               "inputs": [], "abstraction": "exact", "status": "sketch",
               "grounding": {"source": src, "state": "proposed"}, "library": "미대조",
               "contract": {"source_label": nid, "labels": [l for l in [nid] + s.get("merged_labels", []) + s["output_labels"] + s["exported"] if l != nid],
                            "extraction_rule": s["rule"], "env": s["env"],
                            "statement_span": n.get("statement_span"), "proof_span": n.get("proof_span"),
                            **({"proof_file": n["proof_file"]} if n.get("proof_file") else {}),
                            "outputs": n.get("outputs", []), "needs": n.get("needs", [])},
               "symbols": syms}
        for k in ("span_fix", "card_deps_rejected", "card_mismatches"):
            if n.get(k):
                out["contract"][k] = n[k]
        return out

    # 입력을 edge 로
    sub_edges = defaultdict(dict)
    ext_src = defaultdict(dict)  # 하위 graph → external id → (보낸 절, 보낸 node)
    for nid, n in node.items():
        rs = sec_of[nid]
        for nd in n.get("needs", []):
            b = nd["binding"]
            if b.get("type") != "node" or b.get("node") not in node or b["node"] == nid:
                continue
            src = b["node"]
            ss = sec_of[src]
            carry = {"node": src, "item": b["item"], "used_at": nd.get("used_at", []), "origin": "+".join(nd.get("origin", []))}
            if nd.get("used_file"):
                carry["used_file"] = nd["used_file"]
            if ss == rs:
                key = (src, nid)
                e = sub_edges[gid(rs)].setdefault(key, {"from": src, "to": nid, "carries": []})
                if (src, b["item"]) not in {(c["node"], c["item"]) for c in e["carries"]}:
                    e["carries"].append(carry)
            else:
                te = top_edges.setdefault((ss, rs), {"carries": []})
                c2 = dict(carry, graph=gid(ss))
                if ss == "MAIN":
                    c2["node"] = "MAIN"
                if nd.get("used_file"):
                    c2["used_file"] = nd["used_file"]
                if (c2["node"], b["item"]) not in {(c["node"], c["item"]) for c in te["carries"]}:
                    te["carries"].append(dict(c2, used_at=[]) if rs != "MAIN" else c2)
                if ss != "MAIN":
                    used_out[ss][src].add(b["item"])
                if rs != "MAIN":
                    # 2026-11-16: external node 는 보내는 node 하나당 하나(절 하나당 하나가 아니다).
                    xid = "X_" + c2["node"].replace(":", "_")
                    ext_src[gid(rs)][xid] = (ss, c2["node"])
                    key = (xid, nid)
                    e = sub_edges[gid(rs)].setdefault(key, {"from": xid, "to": nid, "carries": [], "ext": ss})
                    if (c2["node"], b["item"]) not in {(c["node"], c["item"]) for c in e["carries"]}:
                        e["carries"].append(dict(carry, graph=gid(ss), **({"node": "MAIN"} if ss == "MAIN" else {})))
    # MAIN 을 맨 위에
    mainn = pnode(MAIN) if MAIN in node else None
    if mainn:
        mainn["id"] = "MAIN"
        mainn["title"] = mainn["title"] if mainn["title"].startswith("주정리") else "주정리 " + mainn["title"]
        top_nodes.append(mainn)
    top_e = []
    for i, ((a, b), te) in enumerate(sorted(top_edges.items(), key=lambda kv: (SECS.index(kv[0][0]) if kv[0][0] in SECS else 99, SECS.index(kv[0][1]) if kv[0][1] in SECS else 99))):
        eid = f"T{i+1}"
        te["id"] = eid
        top_e.append({"id": eid, "from": a, "to": b, "kind": "call", "carries": te["carries"],
                      "origin": "+".join(sorted({o for c in te["carries"] for o in c["origin"].split("+") if o})),
                      "grounding": {"source": "절을 건너는 입력 항목 (받는 쪽 원문 줄은 하위 graph 의 edge 에)"},
                      "status": "connected"})
    tnmap = {n["id"]: n for n in top_nodes}
    for e in top_e:
        if e["from"] not in tnmap[e["to"]]["inputs"]:
            tnmap[e["to"]]["inputs"].append(e["from"])

    graphs = [{"id": "top", "title": "논문 전체 (절 단위)", "parent": None,
               "summary": "절 → 절 edge 는 절을 건너는 입력 항목을 싣는다. 주정리 MAIN 이 출력이다.",
               "nodes": top_nodes, "edges": top_e}]
    for sec in SECS:
        nids = sorted([k for k in node if sec_of[k] == sec], key=lambda k: skn[k]["span"][0][0])
        if not nids:
            continue
        g = gid(sec)
        ns = [pnode(k) for k in nids]
        exts = []
        order = lambda kv: (SECS.index(kv[1][0]) if kv[1][0] in SECS else 99, skn[kv[1][1]]["span"][0][0] if kv[1][1] in skn else 0)
        for xid, (src_sec, snode) in sorted(ext_src[g].items(), key=order):
            te = next(e for e in top_e if e["from"] == src_sec and e["to"] == sec)
            sn = tnmap["MAIN"] if snode == "MAIN" else node[snode]
            sec_title = tnmap[src_sec]["title"].split(" ")[0]
            items = sorted({c["item"] for (a, _), e in sub_edges[g].items() if a == xid for c in e["carries"]})
            exts.append({"id": xid, "kind": "external", "external_ref": src_sec, "import_edge": te["id"],
                         "source_node": {"graph": gid(src_sec), "node": snode}, "items": items,
                         "title": sn.get("title", snode) if snode == "MAIN" else f"{sec_title} {sn.get('title', snode)}",
                         "summary": f"{snode} ({tnmap[src_sec]['title']})",
                         "abstraction": None,
                         "grounding": {"source": (tnmap["MAIN"]["grounding"]["source"] if snode == "MAIN" else pnode(snode)["grounding"]["source"]), "state": "proposed"}})
        outn = {"id": "OUT", "kind": "output", "title": "이 절 밖에서 쓰는 항목", "abstraction": None,
                "grounding": {"source": tnmap[sec]["grounding"]["source"], "state": "proposed"}}
        es = []
        for i, ((a, b), e) in enumerate(sorted(sub_edges[g].items())):
            es.append({"id": f"e{i+1}", "from": a, "to": b, "kind": "call", "carries": e["carries"],
                       "origin": "+".join(sorted({o for c in e["carries"] for o in c["origin"].split("+") if o})),
                       "grounding": {"source": span_text(skn[b]["file"], [[min(u for c in e["carries"] for u in c["used_at"] or [0]), max(u for c in e["carries"] for u in c["used_at"] or [0])]])},
                       "status": "connected"})
        k = len(es)
        for nid in nids:
            items = sorted(used_out[sec].get(nid, []))
            if items:
                k += 1
                es.append({"id": f"o{k}", "from": nid, "to": "OUT", "kind": "call",
                           "carries": [{"node": nid, "item": it, "used_at": []} for it in items],
                           "grounding": {"source": node[nid].get("title", nid)}, "status": "connected"})
        nm = {n["id"]: n for n in ns + exts + [outn]}
        for e in es:
            if e["from"] not in nm[e["to"]].get("inputs", []) and e["to"] != "OUT":
                nm[e["to"]]["inputs"].append(e["from"])
        graphs.append({"id": g, "title": TITLES[sec], "parent": {"graph": "top", "node": sec},
                       "summary": "번호 붙은 진술이 node 다. 증명은 열지 않았다(모두 sketch).",
                       "nodes": ns + exts + [outn], "edges": es})
    # 맨 위 절 node 의 id 는 S_<절>: 보통 낱말(model, cavity, …)이 화면에서 node 단추로 바뀌지 않게.
    rn = lambda x: f"S_{x}" if x in SECS else x
    for n in graphs[0]["nodes"]:
        n["id"] = rn(n["id"]); n["inputs"] = [rn(i) for i in n["inputs"]]
    for e in graphs[0]["edges"]:
        e["from"], e["to"] = rn(e["from"]), rn(e["to"])
    for g in graphs[1:]:
        g["parent"]["node"] = rn(g["parent"]["node"])
        for n in g["nodes"]:
            if n.get("external_ref"):
                n["external_ref"] = rn(n["external_ref"])
    doc = {"format": "proofmap/0.1", "id": "paper", "title": "논문 전체 계약 (외부 입력 닫기, 증명 열지 않음)",
           "language": "ko", "math_syntax": "TeX ($...$)",
           "source": {"root": "redesign/source/sections", "files": [f"{s}.tex" for s in SECS]},
           "content_note": "2026-11-15 논문 전체 계약 PoC. checks/2026-11-15-paper-contract/REPORT.md. 모든 근거 proposed, 모든 node sketch.",
           "symbols": [{k: v for k, v in s.items() if k != "section"} for s in symbols.values()],
           "floors": [{k: v for k, v in f.items() if k != "section"} for f in floors.values()],
           "graphs": graphs}
    (PM / "graphs/paper.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # 측정
    st = Counter()
    by_type, by_origin, opens, floor_uses = Counter(), Counter(), [], []
    for nid, n in node.items():
        for nd in n.get("needs", []):
            t = nd["binding"].get("type")
            by_type[t] += 1
            for o in nd.get("origin", []) or ["(없음)"]:
                by_origin[o] += 1
            by_origin["+".join(sorted(nd.get("origin", [])))] += 0
            if t == "open":
                opens.append({"node": nid, "need": nd.get("id"), "what": nd.get("what"), "used_at": nd.get("used_at"), "why": nd["binding"].get("why")})
            if t == "floor":
                floor_uses.append({"node": nid, "floor": nd["binding"]["floor"], "what": nd.get("what")})
    combo = Counter("+".join(sorted(nd.get("origin", []))) for n in node.values() for nd in n.get("needs", []))
    rejected = [dict(r, node=nid) for nid, n in node.items() for r in n.get("card_deps_rejected", [])]
    mism = [dict(r, node=nid) for nid, n in node.items() for r in n.get("card_mismatches", [])]
    stats = {"nodes": len(node), "skeleton_nodes_missing": missing, "inputs": sum(by_type.values()),
             "by_type": dict(by_type), "by_origin_any": {k: v for k, v in by_origin.items() if v}, "by_origin_combo": dict(combo),
             "card_deps_rejected": len(rejected), "card_mismatches": len(mism),
             "items_added": len(log["item_added"]), "change_requests": len(log["change_request"]),
             "bad_binding": log["bad_binding"], "no_used_at": log["no_used_at"],
             "symbols": len(symbols), "floors": len(floors), "top_edges": len(top_e),
             "symbol_dup_diff": log["symbol_dup_diff"], "symbol_dup_same": len(log["symbol_dup_same"]),
             "floor_dup_diff": log["floor_dup_diff"],
             "opens": opens, "floor_list": list(floors.values()), "floor_uses": floor_uses,
             "rejected": rejected, "mismatches": mism, "item_added_list": log["item_added"],
             "change_request_list": log["change_request"], "unplaced": log["unplaced"],
             "duplicate_node": log["duplicate_node"], "corrections": len(log["correction"]),
             "correction_missed": log["correction_missed"]}
    (HERE / "stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in stats.items() if not isinstance(v, list) or k in ("skeleton_nodes_missing",)}, ensure_ascii=False))
    print("bad_binding", len(log["bad_binding"]), "no_used_at", len(log["no_used_at"]), "opens", len(opens))


if __name__ == "__main__":
    main()
