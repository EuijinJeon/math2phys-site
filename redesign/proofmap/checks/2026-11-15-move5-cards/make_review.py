#!/usr/bin/env python3
"""G2 눈가림 대조 묶음. 두 CON 하위 graph를 A/B로만 이름 붙여 원문과 함께 한 파일에 넣는다.

    python3 make_review.py OLD.json NEW.json OUT.md KEY.json

어느 쪽이 새 방식인지는 KEY.json 에만 적는다(검토 agent에게는 주지 않는다).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[3] / "redesign/source/sections/decorrelation.tex"


def slim(path):
    g = json.loads(Path(path).read_text(encoding="utf-8"))["graph"]
    keep_n = ("id", "kind", "title", "statement", "derivation", "output_items", "grounding", "status", "author_filled", "local_symbols")
    keep_e = ("id", "from", "to", "statement", "grounding")
    nodes = [{k: v for k, v in n.items() if k in keep_n} for n in g["nodes"]]
    edges = [{k: v for k, v in e.items() if k in keep_e} for e in g["edges"]]
    return {"nodes": nodes, "edges": edges}


def main():
    old, new, out, key = sys.argv[1:5]
    lines = SRC.read_text(encoding="utf-8").splitlines()
    src = "\n".join(f"{i:4d}  {lines[i - 1]}" for i in list(range(108, 126)) + list(range(127, 141)))
    A, B = slim(old), slim(new)   # A = 지금 방식, B = 새 방식 (검토자에게 알리지 않음)
    text = f"""# 대조 과제

수학 논문 한 lemma의 증명을 두 사람이 각각 작은 graph(node = 증명의 걸음, edge = 넘기는 내용)로 옮겼다. 판 A와 판 B다. 너는 둘을 **원문과 대조**한다. 이 파일 밖의 것은 쓰지 않는다.

센 것을 아래 JSON 하나로만 답한다(앞뒤 설명 없이).

```json
{{"A": {{"misstatements": [{{"where": "node 또는 edge id", "what": "원문과 어긋난 내용", "lines": "원문 줄"}}],
        "missed_dependencies": [{{"what": "증명이 쓰는데 graph의 어떤 node·edge에도 없는 것", "lines": "원문 줄"}}],
        "unsupported_additions": [{{"where": "...", "what": "원문에 없고 author_filled 표시도 없는 주장"}}]}},
 "B": {{...같은 꼴...}},
 "notes": "판단이 갈린 곳만 짧게"}}
```

정의:
- **misstatement**: node·edge의 진술이나 유도 줄이 원문과 수학적으로 다르다(조건 빠짐, 부등호·지수·상수 틀림, 대상 바뀜). 표기 차이·번역 문체는 세지 않는다.
- **missed dependency**: 원문 증명이 쓰는 사실·가정·정의 가운데 그 판의 어느 node·edge에도 나타나지 않는 것.
- **unsupported addition**: 원문에 없는 주장인데 `author_filled` 표시가 없는 것. 표시가 있으면 세지 않는다.

## 원문 (decorrelation.tex)

```tex
{src}
```

## 판 A

```json
{json.dumps(A, ensure_ascii=False, indent=1)}
```

## 판 B

```json
{json.dumps(B, ensure_ascii=False, indent=1)}
```
"""
    Path(out).write_text(text, encoding="utf-8")
    Path(key).write_text(json.dumps({"A": old, "B": new}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(out, len(text))


if __name__ == "__main__":
    main()
