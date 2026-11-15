#!/usr/bin/env python3
"""여는 작업의 고정 입력 묶음을 만든다 (결정 5).

    python3 .../make_bundle.py NODE_ID OUT.md

묶음 = 그 vertex의 받는 edge 내용 + 원문 줄 범위(줄 번호 포함) + 기호 표의 해당 항목.
여는 node 자신의 계약과 보내는 edge도 넣는다(둘레의 나머지이자 만들어야 할 출력).
그 밖의 문맥(다른 node, 다른 원문, 카드, L2)은 넣지 않는다. 형식 지시는 세 묶음이 같다.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DOC = ROOT / "redesign/proofmap/graphs/move5.json"
SRC = ROOT / "redesign/source/sections"
FORMAT = (HERE / "bundle_format.md").read_text(encoding="utf-8")


def src_lines(fname, lo, hi):
    lines = (SRC / fname).read_text(encoding="utf-8").splitlines()
    return "\n".join(f"{i:4d}  {lines[i - 1]}" for i in range(lo, hi + 1))


def main():
    nid, out = sys.argv[1], Path(sys.argv[2])
    doc = json.loads(DOC.read_text(encoding="utf-8"))
    g = doc["graphs"][0]
    node = next(n for n in g["nodes"] if n["id"] == nid)
    inc = [e for e in g["edges"] if e["to"] == nid]
    outg = [e for e in g["edges"] if e["from"] == nid]
    sym = {s["id"]: s for s in doc["symbols"]}
    c = node["contract"]
    parts = [f"# 입력 묶음: top.{nid} 를 연다\n", FORMAT,
             "\n## 1. 여는 node의 계약 (top graph)\n", "```json",
             json.dumps({k: node[k] for k in ("id", "kind", "title", "statement", "inputs", "symbols")} |
                        {"outputs": c["outputs"], "statement_span": c["statement_span"], "proof_span": c["proof_span"]},
                        ensure_ascii=False, indent=1), "```",
             "\n## 2. 받는 edge (이 vertex로 들어오는 것 전부)\n", "```json",
             json.dumps(inc, ensure_ascii=False, indent=1), "```",
             "\n## 3. 보내는 edge (이 vertex에서 나가는 것 전부)\n", "```json",
             json.dumps(outg, ensure_ascii=False, indent=1), "```",
             "\n## 4. 기호 표의 해당 항목\n", "```json",
             json.dumps([sym[s] for s in node["symbols"]], ensure_ascii=False, indent=1), "```",
             "\n## 5. 원문 줄 범위 (decorrelation.tex, 줄 번호 포함)\n"]
    spans = [c["statement_span"]] + ([c["proof_span"]] if c["proof_span"] else [])
    for lo, hi in spans:
        parts += [f"### {lo}–{hi}", "```tex", src_lines("decorrelation.tex", lo, hi), "```"]
    text = "\n".join(parts) + "\n"
    out.write_text(text, encoding="utf-8")
    print(f"{nid}: {len(text)} 글자, 받는 edge {len(inc)}, 보내는 edge {len(outg)}, 기호 {len(node['symbols'])}")


if __name__ == "__main__":
    main()
