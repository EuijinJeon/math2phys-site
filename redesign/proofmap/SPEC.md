# 증명 지도 자료 규격 — proofmap/0.1

증명 지도(proof map)는 증명을 node와 edge와 문맥으로 나타낸 graph이고, node를 열면 더 미시적인 graph가 나온다. 이 문서는 그 자료를 JSON으로 적는 규격이다. 사람이든 AI 도구든 이 문서만 읽고 graph를 만들 수 있게 쓴다.

- 형식: JSON(UTF-8). 기계용 정의는 `schema/proofmap.schema.json`(JSON Schema 2020-12).
- 수식: 문자열 안에 LaTeX. `$...$` 는 줄 안, `$$...$$` 는 따로 세운 식. KaTeX가 그릴 수 있는 범위로 쓴다. JSON에서는 역사선을 두 번 쓴다(`"$\\partial_t$"`).
- 키는 영어, 내용은 문서의 언어(`language`)로 쓴다.
- 설계의 이유는 `notes/proof-map-design-2026-11-14.md` 에 있다.

## 1. 용어

| 한국어 | 영어 (JSON) | 뜻 |
|---|---|---|
| 증명 지도 | proof map, graph | node, edge, 문맥으로 된 한 장 |
| 상자 | node | 진술 하나, 또는 추론 한 걸음 |
| 화살표 | edge | node 사이를 건너가는 진술. 내용을 스스로 갖는다 |
| 문맥(틀) | context | 구역 전체에 걸린 전제: 고정한 것, 극한의 순서 |
| vertex | — | 받는 edge + node + 보내는 edge. 완결을 따지는 단위 |
| 확대 | subgraph | node를 증명하는 하위 graph |
| 닿는 면 | boundary | 하위 graph가 밖에서 받는 것과 내보내는 것 |
| 바닥 | floor | 더 파지 않는 곳. 독자의 바닥과 원문의 바닥 |
| 원자 node | atomic node | 다른 정리를 부르지 않는 계산 하나 |

## 2. 문서

```json
{
  "format": "proofmap/0.1",
  "id": "move4",
  "title": "수 4 — prescribed-tree 항등식",
  "language": "ko",
  "source": {"root": "redesign/source/sections"},
  "floor": {"reader": ["연쇄 법칙", "..."], "source": "원문이 적은 수준"},
  "graphs": [ ... ]
}
```

`graphs` 의 첫 항목이 맨 위 graph다. 나머지는 어떤 node의 하위 graph이고 `parent` 로 그 node를 가리킨다.

## 3. graph

| 키 | 필수 | 뜻 |
|---|---|---|
| `id`, `title` | 예 | |
| `summary` | | 한두 문장 |
| `parent` | | `{"graph": "...", "node": "..."}`. 맨 위 graph는 `null` |
| `contexts` | | 문맥의 목록 |
| `nodes`, `edges` | 예 | |
| `drafts` | | 자유 형식의 작업 중 자료. 규격의 일부가 아니다 |

### 문맥

```json
{"id": "FF", "text": "깊이 $L$ 과 kernel 열 고정. $N\\to\\infty$ 먼저, 그다음 $L$.", "nodes": ["A", "B"], "provides": ["XFAM"]}
```

`nodes` 는 이 문맥 안에 있는 node들이다. `provides` 는 상위 node의 입력 가운데 이 문맥이 안의 모든 node에 대 주는 것이다(닿는 면 검사에 쓰인다).

## 4. node

| 키 | 필수 | 뜻 |
|---|---|---|
| `id`, `title` | 예 | `id` 는 graph 안에서 유일 |
| `kind` | 예 | 아래 표 |
| `summary` | | 지도 위에 보이는 한 줄 |
| `statement` | | 이 node가 주는 것 전체 |
| `conditions` | | 성립 조건의 목록 |
| `inputs` | | 받는 node의 id 목록 |
| `abstraction` | | `exact` / `weakening` / `blackbox` / `approximation` |
| `status` | | `complete` / `sketch`. 없으면 아직 평가하지 않음 |
| `grounding` | | `{"cards": [...], "source": "trees.tex 151–154", "state": "proposed"}` |
| `library` | | 밖의 library에 있는 짝과 차이. 없으면 `"없음"` |
| `subgraph` | | 이 node를 증명하는 graph의 id |
| `external_ref` | 밖 node | 상위 graph에서 이 node가 가리키는 node의 id |
| `inherit_statement` | | `true` 이면 진술과 조건을 상위 node에서 가져온다 |
| `layout` | | `{"col": 1, "row": 0}`. 보기용 격자 자리. 증명과 무관 |

`kind`:

| 값 | 뜻 |
|---|---|
| `object` | 대상과 기호의 정의 |
| `rule` | 손으로 실행할 수 있는 연산. 출력이 다시 입력 꼴 |
| `fact` | 인용해서 쓰는 진술 |
| `step` | 유도의 한 단계 |
| `external` | 이 graph 밖에서 오는 것, 또는 밖으로 나가는 곳 |
| `output` | 하위 graph의 출력. 상위 node의 진술과 같다 |

`grounding.state` 의 `confirmed` 는 사용자만 붙인다. 도구는 `proposed` 만 쓴다.

### 원자 node

더 쪼개지 않는 node는 유도를 안에 갖는다.

```json
{
  "id": "PM", "kind": "step", "title": "power mean 하나를 미분", "status": "complete",
  "local_context": ["깊이 $d$ 와 prefix 고정.", "..."],
  "floor_used": ["연쇄 법칙", "적분 기호 아래의 미분"],
  "derivation": [
    {"expr": "$$\\log Y_{d-1}=\\frac1{m_d}\\log K_d[Y_d^{m_d}]$$", "by": "e1. $m_d>0$, e3으로 $Y_d\\ge a>0$."},
    {"expr": "$$...$$", "by": "연쇄 법칙. (e3, e4)", "author_filled": "균일 유계를 확인하는 부분은 원문에 없다."}
  ],
  "produces": [{"edge": "o1", "by": "식 1–5"}, {"edge": "e4", "by": "식 2, 6"}],
  "review": {"checks": [{"question": "...", "answer": "..."}], "open": ["..."]}
}
```

- `derivation` 의 줄마다 `by` 에 근거를 적는다. 근거는 **받는 edge의 id, 문맥, 바닥** 가운데 있어야 한다.
- 원문이 적지 않은 걸음을 채웠으면 `author_filled` 에 무엇을 채웠는지 적는다. 원문이 보증하지 않는 부분이라는 표시다.
- `produces` 는 보내는 edge마다 어느 줄에서 나오는지다.

## 5. edge

edge는 내용을 스스로 갖는 대상이다. edge의 내용이 node 안에만 적혀 있으면 그 vertex는 완결이 아니다.

| 키 | 필수 | 뜻 |
|---|---|---|
| `id`, `from`, `to` | 예 | `from`, `to` 는 같은 graph의 node id |
| `kind` | 예 | `flow`: 결과가 입력이 된다 / `call`: rule이나 사실을 쓴다 / `definition`: 대상이 기호를 정한다 |
| `label` | | 화면에 보일 이름(`id` 와 다를 때) |
| `summary` | | 지도 위에 보이는 짧은 내용 |
| `statement` | | 이 edge가 싣는 내용 **전체** |
| `not_carried` | | 보낸 node의 출력 가운데 이 edge가 싣지 않는 것과 그것이 가는 곳 |
| `grounding` | | `{"source": "..."}` |
| `status` | | `connected` / `open`(줄 node가 아직 없음) |
| `complete` | | `true`: `statement` 가 내용 전체 / `false`: 이름이나 요약뿐 |
| `loop` | 고리 | `from == to` 일 때 필수. `{"index": "d", "step": "d → d−1"}` |

규칙:

- **edge는 보낸 node의 출력 가운데 일부만 싣는다.** 받는 node가 실제로 쓰는 만큼만 적는다.
- **대입은 node다.** 일반 진술을 받아 대입한 진술을 내는 원자 node를 따로 둔다. `substitution` 과 `fit` 은 예전 형식(`complete: false`)의 edge에만 남아 있다.
- **고리는 귀납이다.** 줄어드는 지표를 `loop` 에 적는다. 그 밖의 순환은 오류다.
- **문맥을 넘는 edge**는 무엇에 대해 균일한지와 극한의 순서를 `statement` 에 싣는다.

## 6. 완결

**vertex가 완결**이라는 것은 문맥과 받는 edge만으로 node의 유도를 따라 보내는 edge 전부가 나온다는 뜻이다.

node의 `status` 를 `complete` 로 적으려면:

1. 원자 node이면 `derivation` 이 있고, 줄마다 근거가 받는 edge, 문맥, 바닥 가운데 있다.
2. 원자가 아니면 `subgraph` 가 있고, 그 안의 node가 모두 `complete` 이며 닿는 면이 맞는다.
3. 닿는 edge가 모두 `complete: true` 이고 `open` 이 아니다.
4. 보내는 edge가 모두 `produces` 에 있다.
5. 쓰는 기호가 모두 받는 edge, 문맥, 그 node 안에서 정의된다. (기계 검사 없음)

**닿는 면.** 하위 graph의 `external` node들의 `external_ref` 와 문맥의 `provides` 를 모은 집합이 상위 node의 `inputs` 와 같아야 한다. 하위 graph에는 `output` node가 있어야 한다.

완결은 아래에서 위로 쌓인다. 모르는 것은 `sketch` 나 `open` 으로 적는다. 어느 시점의 graph든 틀리지 않은 부분 증명이어야 한다.

## 7. 도구

```bash
python3 redesign/proofmap/tools/check.py redesign/proofmap/graphs/move4.json
```

```bash
python3 redesign/proofmap/tools/build_viewer.py redesign/proofmap/graphs/move4.json redesign/proofmap/build/move4.html
```

`check.py` 가 보는 것: 필드 값, id 중복, edge의 양 끝, 받는 것이 가리키는 곳, 닿는 면, 순환과 고리, 쓰이지 않는 node, `complete` 의 조건 1–4, 한 장의 node 수(안쪽 9개 기준). 진술이 수학적으로 맞는지는 보지 않는다.

`build_viewer.py` 는 JSON에서 혼자 열리는 HTML을 만든다. HTML은 생성물이라 직접 고치지 않는다. 둘 다 표준 라이브러리만 쓴다.

## 8. 다른 도구로 graph를 만들 때

1. 원문에서 증명할 진술과 그 근거 줄 범위를 정한다.
2. 맨 위 graph를 대강 그린다. node는 아홉 개 안팎. `status` 는 `sketch`.
3. 의심 가는 node나 중요한 node를 골라 `subgraph` 로 연다. `external` node와 `output` node로 닿는 면을 맞춘다.
4. 원자 수준까지 내려간 node에 `derivation` 을 쓴다. 받는 edge를 먼저 내용까지 적고, 유도의 줄마다 그 id를 가리킨다.
5. 조건이 모자라면 받는 edge를 더한다. 줄 node가 같은 graph에 없으면 `external` node를 더하고 상위 node의 `inputs` 도 고친다. 어디에도 없으면 `status: "open"`.
6. `check.py` 를 돌려 오류를 0으로 만든다.
7. 원문과 대조하지 않은 것을 `confirmed` 로 적지 않는다. 원문에 없는 걸음은 `author_filled` 로 표시한다.

가장 작은 예:

```json
{
  "format": "proofmap/0.1", "id": "demo", "title": "예", "language": "ko",
  "graphs": [{
    "id": "top", "title": "예", "parent": null,
    "contexts": [{"id": "C", "text": "$x>0$ 고정.", "nodes": ["A", "B"]}],
    "nodes": [
      {"id": "A", "kind": "fact", "title": "가정", "statement": "$f(x)=x^2$."},
      {"id": "B", "kind": "step", "title": "미분", "inputs": ["A"], "status": "complete",
       "derivation": [{"expr": "$$f'(x)=2x$$", "by": "e1, 거듭제곱의 미분(바닥)."}],
       "floor_used": ["거듭제곱의 미분"], "produces": []}
    ],
    "edges": [
      {"id": "e1", "from": "A", "to": "B", "kind": "flow", "statement": "$f(x)=x^2$.", "status": "connected", "complete": true}
    ]
  }]
}
```
