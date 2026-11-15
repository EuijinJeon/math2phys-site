"""carries 참조 펼치기 (SPEC 7.7 [제안], 2026-11-15).

저장(JSON)에서는 계약 출력 항목의 진술을 그 node의 `contract.outputs` 한 곳에만 둔다.
edge는 `carries: [{node, item, used_at}]` 로 가리키기만 한다. 검사·보기·묶음을 만들기 전에
이 모듈이 사본을 메모리에서 만든다(원본 파일은 바꾸지 않는다).

- edge `statement` 가 없고 `carries` 가 있으면: 각 항목의 진술을 "[node.item] 진술" 꼴로 이어 붙인다.
- edge `summary` 가 없으면: 항목 이름을 쉼표로 잇는다.
- node `statement` 가 없고 `contract.outputs` 가 있으면: 출력 진술을 이어 붙인다.
- 원문 줄 조각: `source_text(root, ref)` 가 "decorrelation.tex 287–290, 300; trees.tex 28–39" 꼴을 읽어 줄을 돌려준다.
"""
import copy
import re
from pathlib import Path


def item_index(doc):
    idx = {}
    for g in doc.get("graphs", []):
        for n in g.get("nodes", []):
            for o in n.get("contract", {}).get("outputs", []):
                idx[(g["id"], n["id"], o["id"])] = o
    return idx


def resolve(doc):
    doc = copy.deepcopy(doc)
    idx = item_index(doc)
    graphs = {g["id"]: g for g in doc.get("graphs", [])}
    for g in doc.get("graphs", []):
        resolve_source_refs(g, graphs, idx)
        for n in g.get("nodes", []):
            outs = n.get("contract", {}).get("outputs")
            if outs and not n.get("statement"):
                n["statement"] = " ".join(o["statement"] for o in outs)
            if outs and not n.get("summary") and n.get("kind") == "external":
                n["summary"] = ", ".join(o["id"] for o in outs)
        for e in g.get("edges", []):
            cs = e.get("carries")
            if not cs or not all(isinstance(c, dict) and c.get("node") for c in cs):
                continue
            if not e.get("statement"):
                parts = []
                for c in cs:
                    o = idx.get((c.get("graph", g["id"]), c["node"], c["item"]))
                    parts.append(f"[{c['node']}.{c['item']}] " + (o["statement"] if o else "(항목 없음)"))
                e["statement"] = " ".join(parts)
            if not e.get("summary"):
                e["summary"] = ", ".join(c["item"] for c in cs)
    return doc


def resolve_source_refs(g, graphs, idx):
    """SPEC 7.8: 원문 참조 판.
    - `lines: [lo, hi]` 를 가진 node는 그 원문 줄이 진술이다(`source_file`, 기본 decorrelation.tex).
    - edge의 `carries` 가 문자열 목록이면:
        보낸 node가 원문 참조 node → 내용 = 그 node의 원문 줄("result").
        보낸 node가 import_edge 를 가진 external → 내용 = 부모 edge가 싣는 같은 이름 항목의 진술.
      내용을 모두 찾으면 `complete: true`, `content_ref` 를 단다. 하나라도 못 찾으면 complete 를 건드리지 않는다.
    """
    nodes = {n["id"]: n for n in g.get("nodes", [])}
    parent = g.get("parent")
    pg = graphs.get(parent["graph"]) if parent else None
    for n in g.get("nodes", []):
        if n.get("lines") and not n.get("statement"):
            lo, hi = n["lines"][0], n["lines"][-1]
            n["statement"] = f"(원문 {n.get('source_file', 'decorrelation.tex')} {lo}–{hi})"
            n["content_ref"] = "source"
    for e in g.get("edges", []):
        cs = e.get("carries") or []
        if not cs or not all(isinstance(c, str) for c in cs) or e.get("statement"):
            continue
        src = nodes.get(e.get("from"), {})
        parts, ok = [], True
        if src.get("lines"):
            lo, hi = src["lines"][0], src["lines"][-1]
            parts.append(f"[{src['id']} 의 결과] 원문 {src.get('source_file', 'decorrelation.tex')} {lo}–{hi}")
            kind = "source"
        elif src.get("kind") == "external" and src.get("import_edge") and pg:
            pe = next((x for x in pg["edges"] if x["id"] == src["import_edge"]), None)
            kind = "item"
            for c in cs:
                pc = next((x for x in (pe or {}).get("carries", []) if isinstance(x, dict) and x.get("item") == c), None)
                o = idx.get((pg["id"], pc["node"], pc["item"])) if pc else None
                if o:
                    parts.append(f"[{pc['node']}.{c}] {o['statement']}")
                else:
                    ok = False
        else:
            ok = False
        if ok and parts:
            e["statement"] = " ".join(parts)
            e["complete"] = True
            e["content_ref"] = kind


REF = re.compile(r"([A-Za-z0-9_.-]+\.tex)\s+([0-9–\-, ]+)")


def parse_ref(ref):
    """'a.tex 1–3, 5; b.tex 7' → [(a.tex, 1, 3), (a.tex, 5, 5), (b.tex, 7, 7)]"""
    out = []
    for m in REF.finditer(str(ref)):
        for part in m.group(2).split(","):
            part = part.strip()
            if not part:
                continue
            a, _, b = part.replace("-", "–").partition("–")
            try:
                lo = int(a)
                hi = int(b) if b.strip() else lo
            except ValueError:
                continue
            out.append((m.group(1), min(lo, hi), max(lo, hi)))
    return out


def source_lines(root, ranges, cache=None):
    cache = {} if cache is None else cache
    got = {}
    for f, lo, hi in ranges:
        if f not in cache:
            p = Path(root) / f
            cache[f] = p.read_text(encoding="utf-8").splitlines() if p.exists() else []
        lines = cache[f]
        for i in range(lo, min(hi, len(lines)) + 1):
            got.setdefault(f, {})[i] = lines[i - 1]
    return got
