## 0. 할 일과 규칙 (구조만 쓰는 판)

수학 논문 한 절의 증명 지도(proof map)를 짓는 중이다. 맨 위 graph의 node 하나를 **연다**: 그 node의 증명 블록을 한 층 아래의 하위 graph로 옮긴다. 이 묶음에 있는 것만 쓴다. 다른 파일, 다른 원문, 기억하는 문헌을 쓰지 않는다. 묶음에 없는 것이 필요하면 지어내지 말고 `missed_dependencies` 나 `parent_change_requests` 에 적는다.

**원문과 카드가 이미 말한 것을 다시 쓰지 않는다.** 화면은 node의 원문 줄과 카드의 번역(`math`)을 그 자리에 펼쳐 보여 준다. 너는 다음만 쓴다:

1. **경계**: 어느 원문 줄 범위가 안쪽 node 하나인가. 원문 증명 순서와 문단 경계를 따르고 9개 안팎. 7절 카드 가운데 그 범위와 맞는 것이 있으면 `card` 에 id를 적는다(카드의 경계가 원문과 맞지 않으면 원문을 따르고 `note` 에 적는다).
2. **의존**: 무엇이 무엇에 쓰이는가. edge는 보낸 쪽의 무엇을(받는 edge의 항목 이름, 또는 앞 node의 결과) 받는 쪽의 어느 줄에서 쓰는지만 적는다.
3. **원문에 없는 걸음**: 원문이 적지 않았는데 그 걸음이 서려면 필요한 것. 이것만 문장과 식으로 쓴다(`author_filled`).

`title` 은 15자 안팎의 짧은 이름. `statement` 칸은 쓰지 않는다. 원문 줄이 그 node의 진술이다.

## 0.1 산출 (JSON 하나)

```json
{
  "graph": {"id": "<NODE 소문자>", "parent": {"graph": "top", "node": "<NODE>"},
    "nodes": [
      {"id": "s1", "kind": "step", "title": "짧은 이름", "lines": [533, 535], "card": "카드 id 또는 null",
       "status": "sketch",
       "author_filled": [{"what": "원문에 없는 걸음 한 줄", "expr": "필요하면 식"}],
       "note": "필요할 때만"},
      {"id": "x_PB", "kind": "external", "external_ref": "PB", "import_edge": "t13", "items": ["projection"]},
      {"id": "out", "kind": "output", "output_items": ["main"], "lines": [65, 74]}
    ],
    "edges": [
      {"id": "e1", "from": "x_PB", "to": "s6", "carries": ["projection"], "used_at": [580]},
      {"id": "e2", "from": "s5", "to": "s9", "carries": ["result"], "used_at": [597]}
    ]},
  "parent_change_requests": [{"target": "...", "kind": "add_item | change_item | new_edge | new_symbol | other", "detail": "...", "source_lines": "..."}],
  "missed_dependencies": [{"what": "...", "used_at": "...", "likely_from": "node id 또는 '모름'"}],
  "notes": "확신이 낮은 곳만, 짧게"
}
```

- 받는 edge(2절)마다 external node 하나: `external_ref` = 그 edge의 `from`, `import_edge` = 그 edge의 `id`, `items` = 실제로 쓰는 항목 이름. 2절의 모든 `from` 이 external로 있어야 한다.
- 1절 계약의 출력 항목은 output node의 `output_items` 가 맡는다. 3절의 보내는 edge가 싣는 항목이 모두 어느 output에서 나와야 한다.
- 안쪽 node에서 나오는 edge의 `carries` 는 `["result"]` 처럼 그 node의 결과를 가리키면 된다(그 node의 원문 줄이 내용이다).
- `status` 는 `sketch`. `grounding.state` 는 쓰지 않는다(모두 `proposed` 로 취급).
- 기호는 4절 기호 표의 id로만 가리킨다. 증명 안에서 새로 정의되는 기호는 node의 `defines: ["기호", ...]` 에 이름만 적는다(정의는 그 node의 원문 줄에 있다).
