#!/usr/bin/env python3
"""P2: 카드 뼈대 + 원문 + 받는 항목으로, LLM이 '카드에 없는 의존'과 '원문에 없는 걸음'만 채우게 하는 지시문을 만든다.

    python3 make_fill_prompt.py MOVE5.json skeletons.json NODE [NODE ...] > fill-prompt.md
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[3] / "redesign/source/sections/decorrelation.tex"

HEAD = """도구를 하나도 쓰지 마. 아래 자료만 보고 답으로 ```json 코드 블록 하나만 낸다(앞뒤 설명 없이).

수학 논문 한 절의 증명 지도를 짓는다. node 몇 개의 증명을 한 층 아래로 열 때, **뼈대(안쪽 걸음과 그 사이의 의존)는 이미 기존 카드에서 기계로 만들었다.** 너는 뼈대를 다시 쓰지 않는다. 원문을 읽고 다음 셋만 쓴다.

1. `edge_used_at`: 뼈대의 edge마다 받는 걸음의 원문에서 그 의존이 실제로 쓰이는 줄. 원문에서 쓰임을 찾지 못하면 `null` 과 짧은 이유.
2. `missing`: 원문의 걸음이 쓰는데 뼈대 edge에 없는 의존. 받는 쪽 걸음 id, 무엇, 원문 줄, 어디서 오는지(`from`: 같은 뼈대의 걸음 id, 아래 '받을 수 있는 항목'의 `NODE.item`, `floor:이름`(초등적 사실), 또는 `모름`).
3. `author_filled`: 원문이 적지 않았는데 그 걸음이 서려면 필요한 것(한 줄씩, 필요하면 식).
4. `mismatch`: 카드의 경계(줄 범위)가 원문 문단·논리와 맞지 않는 곳, 뼈대 edge가 원문과 다른 곳.

진술을 옮겨 적지 않는다. 화면이 원문 줄과 카드 번역을 그 자리에 펼친다.

답의 꼴:
```json
{"<NODE>": {"edge_used_at": [{"from": "...", "to": "...", "lines": [..] , "note": null}],
            "missing": [{"to": "k2", "what": "...", "lines": [..], "from": "..."}],
            "author_filled": [{"at": "k3", "what": "..."}],
            "mismatch": [{"card": "...", "issue": "..."}]},
 "...": {}}
```
"""


def main():
    doc = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    sk = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    lines = SRC.read_text(encoding="utf-8").splitlines()
    top = doc["graphs"][0]
    tn = {n["id"]: n for n in top["nodes"]}
    out = [HEAD]
    for nid in sys.argv[3:]:
        s, n = sk[nid], tn[nid]
        inc = [e for e in top["edges"] if e["to"] == nid]
        items = {}
        for e in inc:
            for c in e["carries"]:
                o = next(o for o in tn[c["node"]]["contract"]["outputs"] if o["id"] == c["item"])
                items[f"{c['node']}.{c['item']}"] = o["statement"]
        sk_small = {"inner": [{k: x[k] for k in ("id", "card", "title", "lines")} for x in s["inner"]],
                    "edges": [{"from": e["from"], "to": e["to"]} for e in s["edges"]],
                    "symbols_from_cards": s["symbols"], "floor_from_cards": s["floor"]}
        c = n["contract"]
        spans = [c["statement_span"]] + ([c["proof_span"]] if c["proof_span"] else [])
        src = "\n".join(f"{i:4d}  {lines[i - 1]}" for lo, hi in spans for i in range(lo, hi + 1))
        out += [f"\n---\n\n# {nid}: {n['title']}\n",
                "뼈대 (x_<NODE> 는 위 graph의 그 node에서 오는 입력):", "```json", json.dumps(sk_small, ensure_ascii=False), "```",
                "받을 수 있는 항목 (이 node로 들어오는 입력 전부):", "```json", json.dumps(items, ensure_ascii=False), "```",
                "원문 (decorrelation.tex):", "```tex", src, "```"]
    print("\n".join(out))


if __name__ == "__main__":
    main()
