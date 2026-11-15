#!/usr/bin/env python3
"""입력 묶음 둘째 판: 같은 진술을 한 번만 넣는다.

    python3 make_bundle2.py DOC.json NODE MODE OUT.md [--indent]

MODE
  dedup      앞 판(make_bundle.py)과 같은 형식 지시(bundle_format.md)와 같은 정보.
             다만 node 진술(출력 항목의 이어 붙임)과 edge statement(항목 사본)를 빼고,
             참조된 출력 항목의 진술을 '항목 사전'에 한 번씩만 넣는다.
  structure  C 시험용. 형식 지시는 format_structure.md. dedup 내용에 더해
             그 node의 원문 범위에 걸친 카드(redesign/cards)의 id·제목·math·원문 줄·uses·children 을 넣는다.
JSON은 기본으로 한 줄씩(compact), --indent 이면 앞 판처럼 indent=1.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SRC = ROOT / "redesign/source/sections"
CARDS = ROOT / "redesign/cards"


def dump(x, indent):
    return json.dumps(x, ensure_ascii=False, indent=1 if indent else None)


def src_lines(lo, hi):
    lines = (SRC / "decorrelation.tex").read_text(encoding="utf-8").splitlines()
    return "\n".join(f"{i:4d}  {lines[i - 1]}" for i in range(lo, hi + 1))


def card_fields(path):
    """카드 앞머리(YAML 비슷한 꼴)에서 필요한 칸만 손으로 읽는다(표준 라이브러리만)."""
    text = path.read_text(encoding="utf-8")
    head = text.split("---")[1]
    out, key = {}, None
    for line in head.splitlines():
        m = re.match(r"^([a-z_]+):\s?(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2)
            out[key] = "" if val in ("|", "") else val
        elif key and line.startswith("  "):
            out[key] = (out[key] + "\n" + line.strip()).strip()
    lines = [tuple(map(int, m)) for m in re.findall(r"file: decorrelation\.tex, lines: \[(\d+), (\d+)\]", head)]
    keep = {k: out.get(k, "").strip("'") for k in ("id", "title", "math", "uses", "children")}
    keep["source_lines"] = lines
    return keep


def main():
    doc_path, nid, mode, out = sys.argv[1:5]
    indent = "--indent" in sys.argv
    doc = json.loads(Path(doc_path).read_text(encoding="utf-8"))
    g = doc["graphs"][0]
    nodes = {n["id"]: n for n in g["nodes"]}
    node = nodes[nid]
    inc = [e for e in g["edges"] if e["to"] == nid]
    outg = [e for e in g["edges"] if e["from"] == nid]
    sym = {s["id"]: s for s in doc["symbols"]}
    c = node["contract"]

    # 항목 사전: 받는 edge가 싣는 남의 출력 항목. 진술은 여기 한 번만.
    items = {}
    for e in inc:
        for ci in e["carries"]:
            o = next(o for o in nodes[ci["node"]]["contract"]["outputs"] if o["id"] == ci["item"])
            src = nodes[ci["node"]]["grounding"]["source"]
            items[f"{ci['node']}.{ci['item']}"] = {"statement": o["statement"], "lines": o["lines"], "source": src}
    strip_edge = lambda e: {k: v for k, v in e.items() if k not in ("statement", "summary")}
    fmt_file = "bundle_format.md" if mode == "dedup" else "format_structure.md"
    fmt = (HERE.parent / "2026-11-15-move5-contract/bundle_format.md").read_text(encoding="utf-8") if mode == "dedup" \
        else (HERE / fmt_file).read_text(encoding="utf-8")
    own = {k: node[k] for k in ("id", "kind", "title", "inputs", "symbols")}
    if mode == "dedup":
        own["outputs"] = c["outputs"]
    else:
        own["outputs"] = [{"id": o["id"], "lines": o["lines"]} for o in c["outputs"]]
    own |= {"statement_span": c["statement_span"], "proof_span": c["proof_span"]}
    parts = [f"# 입력 묶음: top.{nid} 를 연다\n", fmt,
             "\n## 1. 여는 node의 계약 (top graph). 출력 항목의 진술은 여기에만 있다\n", "```json", dump(own, indent), "```",
             "\n## 2. 받는 edge (이 vertex로 들어오는 것 전부). 싣는 항목의 진술은 6절 항목 사전에 있다\n", "```json",
             dump([strip_edge(e) for e in inc], indent), "```",
             "\n## 3. 보내는 edge (이 vertex에서 나가는 것 전부). 싣는 항목의 진술은 1절에 있다\n", "```json",
             dump([strip_edge(e) for e in outg], indent), "```",
             "\n## 4. 기호 표의 해당 항목\n", "```json", dump([sym[s] for s in node["symbols"]], indent), "```",
             "\n## 5. 원문 줄 범위 (decorrelation.tex, 줄 번호 포함)\n"]
    spans = [c["statement_span"]] + ([c["proof_span"]] if c["proof_span"] else [])
    for lo, hi in spans:
        parts += [f"### {lo}–{hi}", "```tex", src_lines(lo, hi), "```"]
    parts += ["\n## 6. 항목 사전 (받는 edge가 싣는 남의 출력 항목, 하나에 한 번)\n", "```json", dump(items, indent), "```"]
    if mode == "structure":
        lo_all = min(s[0] for s in spans)
        hi_all = max(s[1] for s in spans)
        cards = []
        for p in sorted(CARDS.glob("decor.*.md")) + sorted(CARDS.glob("x.decor-*.md")):
            f = card_fields(p)
            if any(lo <= a and b <= hi for lo, hi in spans for a, b in f["source_lines"]):
                cards.append(f)
        parts += ["\n## 7. 이 범위의 카드 (redesign/cards 의 앞머리 일부: id, 제목, math(번역), 원문 줄, uses, children)\n",
                  "```json", dump(cards, indent), "```"]
    text = "\n".join(parts) + "\n"
    Path(out).write_text(text, encoding="utf-8")
    print(f"{nid} {mode} {'indent' if indent else 'compact'}: {len(text)} 글자")


if __name__ == "__main__":
    main()
