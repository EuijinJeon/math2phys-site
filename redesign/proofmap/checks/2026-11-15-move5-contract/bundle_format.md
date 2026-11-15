## 0. 할 일과 규칙

수학 논문 한 절의 증명 지도(proof map)를 짓는 중이다. 맨 위 graph의 node 하나를 **연다**: 그 node의 증명 블록을 한 층 아래의 하위 graph로 옮긴다. 이 묶음에 있는 것만 쓴다. 다른 파일, 다른 원문, 기억하는 문헌을 쓰지 않는다. 묶음에 없는 것이 필요하면 지어내지 말고 아래 `missed_dependencies` 나 `parent_change_requests` 에 적는다.

- 하위 graph의 안쪽 node는 원문 증명의 걸음이다. 원문 순서와 문단 경계를 따르고 9개 안팎으로 둔다. 물리 해석의 이름을 붙이지 않는다.
- 모든 진술은 5절의 원문 줄과 대조해 옮긴다. 각 node·edge에 줄 범위(`grounding.source`, 예 `"decorrelation.tex 287–290"`)를 단다.
- 원문이 적지 않은 걸음을 채웠으면 그 node 또는 유도 줄에 `author_filled` 로 무엇을 채웠는지 적는다.
- 안쪽 node의 `status` 는 기본 `sketch`. `complete` 는 그 node가 다른 정리를 부르지 않는 한 걸음이고 `derivation` 의 모든 줄의 근거(`by`)가 받는 edge id, 앞선 줄, 바닥(Cauchy–Schwarz 같은 기초 사실, `floor_used` 에 적음) 가운데 있을 때만 쓴다. 망설여지면 `sketch`.
- `grounding.state` 는 언제나 `"proposed"`.
- 상위 graph의 받는 edge(2절)마다 하위 graph에 `external` node 하나를 둔다: `external_ref` = 그 edge의 `from`, `import_edge` = 그 edge의 `id`, `items` = 하위에서 실제로 쓰는 그 edge의 carries 항목 이름. 2절의 모든 `from` 이 빠짐없이 external로 있어야 한다(쓰지 않으면 그렇다고 `note` 에 적는다).
- 1절 계약의 출력 항목마다 `output` node 하나 또는 하나의 `output` node가 여러 항목을 맡게 하고, `output_items` 에 항목 이름을 적는다. 3절의 보내는 edge가 싣는 항목이 모두 어느 output에서 나와야 한다.
- edge는 `{id, from, to, kind: flow|call|definition, statement, carries: [{item, used_at: [줄]}], grounding, status: "connected", complete: true|false}`. `statement` 에 싣는 내용을 다 적었으면 `complete: true`.
- 기호는 4절 기호 표의 id로 참조한다(`symbols`). 증명 안에서만 쓰는 새 기호는 node의 `local_symbols: [{id, tex, defined_at, text}]` 에 적는다. 기호 표에 있어야 할 것(밖에서도 쓰는 것)이 빠졌으면 `parent_change_requests` 에.

## 0.1 산출 (JSON 하나)

```json
{
  "graph": {"id": "<NODE 소문자>", "title": "...", "parent": {"graph": "top", "node": "<NODE>"},
            "summary": "...", "nodes": [...], "edges": [...]},
  "parent_change_requests": [
    {"target": "edge t5 | node AVG | symbol mu | new edge X→NODE | new symbol",
     "kind": "add_item | change_item | new_edge | new_symbol | change_symbol | other",
     "detail": "무엇을 어떻게", "reason": "왜 필요한가", "source_lines": "decorrelation.tex 287"}
  ],
  "missed_dependencies": [
    {"what": "증명이 쓰는데 받는 edge에 없는 것", "used_at": "decorrelation.tex 287", "likely_from": "node id 또는 '모름'"}
  ],
  "notes": "자유. 확신이 낮은 곳."
}
```

`parent_change_requests` 는 상위 graph(이 node의 계약, 받는/보내는 edge, 다른 node, 기호 표)를 바꿔야 할 때만 적는다. 이 node의 계약 출력 항목 문구가 원문과 다르면 `change_item` 으로 적는다. 바꿀 필요가 없으면 빈 배열.
