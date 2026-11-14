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
5. 쓰는 기호가 모두 받는 edge, 문맥, 그 node 안에서 정의된다. (명시한 목록의 국소 정의 위치를 기계 검사. 수식에서 기호를 자동 추출하지 않는다.)

**닿는 면.** 하위 graph의 `external` node들의 `external_ref` 와 문맥의 `provides` 를 모은 집합이 상위 node의 `inputs` 와 같아야 한다. 하위 graph에는 `output` node가 있어야 한다.

완결은 아래에서 위로 쌓인다. 모르는 것은 `sketch` 나 `open` 으로 적는다. 어느 시점의 graph든 틀리지 않은 부분 증명이어야 한다.

## 7. 도구

```bash
python3 redesign/proofmap/tools/check.py redesign/proofmap/graphs/move4.json
```

```bash
python3 redesign/proofmap/tools/build_viewer.py redesign/proofmap/graphs/move4.json redesign/proofmap/build/move4.html
```

`check.py` 가 보는 것: 필드 값, id 중복, edge의 양 끝, 받는 것이 가리키는 곳, 닿는 면, 순환과 고리, 쓰이지 않는 node, `complete` 의 조건 1–4, 한 장의 node 수(안쪽 9개 기준). 아래의 명시 참조가 있는 원자 node는 기호의 국소 정의 위치와 입력 사용 여부도 보고한다. 진술이 수학적으로 맞는지는 보지 않는다.

### 7.1 명시 기호·참조 검사 (0.1의 선택적 확장)

원자 node에 `reference_check: true`를 붙이면 산문의 부분 문자열 검색 대신 다음 필드를 검사한다. 예전 자료는 그대로 읽되 **명시 기호·참조 미검사**라고 보고한다. 현재 `fv`, `cp`, `fresh`의 원자 node 여덟 개는 모두 이 검사를 사용한다. 하위 graph를 갖는 복합 node는 원자 node 검사 대상이 아니다.

```json
{
  "reference_check": true,
  "derivation": [{
    "expr": "...", "by": "사람이 읽는 근거",
    "uses": ["edge:e2", "context:FF", "line:1", "floor:1"],
    "uses_symbols": ["K_A", "Y"]
  }],
  "produces": [{"edge": "o1", "by": "식 1–5", "lines": [1, 2, 3, 4, 5]}]
}
```

`uses`에는 실제로 이 node에 들어오는 edge의 정확한 id, 이 node를 포함하는 같은 graph의 문맥 id, **앞선** 유도 줄 번호, node의 `floor_used` 항목 번호만 적는다. 번호는 1부터 센다. 빈 근거, 존재하지 않는 참조, 같은 줄·미래 줄 참조는 오류다. 받는 edge 가운데 어떤 줄의 `uses`에도 없는 것은 `EDGE_UNUSED` 경고다. “필요하지 않다”라고 산문에서 언급한 것은 사용으로 세지 않는다. 귀납의 시작·반복 입력은 양쪽 모두 명시하며, 어느 경우에 쓰는지는 `by`가 설명한다. 기계는 귀납의 수학적 타당성을 판정하지 않는다.

edge와 문맥의 `defines: ["Y", "K_A"]`는 해당 진술에서 의미를 주는 기호 목록이다. 유도 줄도 `defines: ["h"]`로 그 줄의 새 기호를 선언할 수 있다. `uses_symbols`의 각 기호는 적용되는 문맥, 받는 edge, 현재·앞선 유도 줄에서 정의되어야 한다. 다른 node나 다른 graph의 선언은 자동 상속하지 않는다. 필요한 내용은 문맥 또는 실제 입력 edge로 들여온다. 기호의 정의 위치를 보고서에 모두 나열하며, 같은 기호가 여러 입력에서 반복되면 모든 위치를 표시한다.

기호 id는 대소문자를 구별하는 정확한 문자열이다. 예컨대 `Y`는 깊이에 따라 색인된 $Y_d$ 가족, `K_A`는 $K_d^A$, `E_A`는 $E^A$, `F`는 $\mathscr F_d$, `partial`은 고정한 방향의 미분을 뜻한다. 아래첨자까지 서로 다른 기호로 구별해야 한다면 별개의 id를 쓴다. `cp` 문맥의 `K_A`는 입력 항등식들을 이어 붙일 때 사용하는 연산자 가족의 표기이며, 그 확률 법칙의 재증명은 `cp`의 역할이 아니다.

`produces[].lines`는 실제 존재하는 유도 줄 번호를 적는다. 없는 출력 edge를 가리키거나 유도 범위 밖의 줄을 적으면 오류다.

**한계:** 이 선언들은 사람이 작성하는 색인이다. 기계는 `expr`와 `by`에서 누락된 기호를 찾아내거나, `defines`가 진짜 정의를 담는지, 두 정의가 서로 일치하는지, 참조한 식이 결론을 증명하는지를 판정하지 않는다. 따라서 명시 목록의 검사 통과를 수학적 완결의 자동 인증으로 읽지 않는다. 정의를 일부러 잘못 옮기거나 `uses_symbols`에서 아예 빠뜨린 경우에는 별도의 내용 검토가 필요하다.

회귀 시험: `python3 redesign/proofmap/tools/test_check.py`. 원본을 메모리에서 복사해 edge·정의·참조를 지운 경우를 검사하며 저장된 graph와 독립 검증 packet은 바꾸지 않는다.

`build_viewer.py` 는 JSON에서 혼자 열리는 HTML을 만든다. HTML은 생성물이라 직접 고치지 않는다. 둘 다 표준 라이브러리만 쓴다.

### 7.2 생성 화면의 상태와 edge 식별자

보기 생성기는 각 node의 선언과 연결을 함께 진단한다. 실제 입력 edge가 없는 `inputs`, 내용 미작성·열린 edge, 미완결 하위 vertex, 상위·하위 입력 경계 불일치를 화면과 생성 로그에 표시한다. 완결 선언 없이 내부 증명만 끝났다고 바깥 vertex를 자동 승격하지 않는다. 예를 들어 `diff.D2`는 **내부 3/3 완결 · 외곽 미완결 · 입력 edge 누락**으로 표시된다. 이는 수학적 자동 검증이 아니며 자료의 status나 사용자 전용 confirmed를 바꾸지 않는다. 외부 입력과 출력은 국소 완결 개수에서 제외한다.

기본 edge 표시는 **지도 안에서 고정된 짧은 ID + 핵심어**다. 예: `e4 · 첫 변분`, `e9 · 극한 순서`. `?`는 내용 미작성, `!`는 열린 연결을 뜻한다. 핵심어 표시를 끄면 ID와 상태 기호만 남는다. 전체 수식은 선택 패널에서 읽는다. edge 내용 완결과 보낸·받는 vertex의 완결을 구분한다.

축약 대응표는 `viewer/edge-labels.json`에 별도로 둔다. 원본 graph의 id와 수학적 내용은 유지한다. 표시 ID는 지도마다 유일해야 하며 edge 배열 순서를 바꿔도 바뀌지 않는다. 선택 패널과 원자 vertex 상세는 원래 ID도 함께 제공한다. 따라서 다른 지도에서 같은 `e4`를 쓸 수 있지만, 외부에서 위치를 지정할 때는 `diff / e4` 또는 원본 `diff-e4`를 쓴다.

`check.py`의 오류 0만으로 graph 전체를 완결로 표시하지 않는다. 생성기의 상태 진단은 node별 미완결을 드러내는 별도 표시다. 회귀 시험은 `python3 redesign/proofmap/tools/test_viewer.py`로 실행한다.

### 7.3 이름 붙은 출력과 수신 요구 (선택적 확장)

`diff.D2 → diff-e4 → diff.D4` 및 실제 대입을 하는 `fresh.FP_BIND`에 시범 적용했다. 수학적 진술과 성립 조건은 node의 `outputs.kernel_form` 한 곳에 둔다. node 본문의 `statement_ref`, 전달 edge의 `output_ref`, 받는 node의 `input_ports`가 같은 출력 항목을 가리킨다.

```json
{
  "output_ref": {"graph": "diff", "node": "D2", "output": "kernel_form"}
}
```

`statement_ref`와 독립 `statement`, 또는 `output_ref`와 독립 `statement`를 함께 작성하는 것은 오류다. 대입을 어디서 하는지 같은 사용 설명은 edge의 `use_note`에 적으며 수학적 출력과 구별한다. 보기·단독 전달 시에는 `output_contracts.resolve_document`가 참조한 전체 진술과 성립 조건을 펼친다. 생성 과정은 원본을 수정하지 않는다.

출력의 `proof`는 그 출력을 만드는 하위 graph/node를 지정한다. `proof_review`에는 작성자가 그 대응을 확인했을 때의 출력 지문과 증명 자료 지문을 기록한다. 증명 자료에는 해당 graph 및 하위 graph의 유도·입력 edge·문맥뿐 아니라 **상위 vertex에 실제로 들어오는 정의 edge와 그 공급 node의 상속 진술**도 들어간다. 배치 좌표와 검토 지문 자체는 빠진다. 검토 기록을 갱신하는 일이 자기 지문을 다시 바꾸는 순환을 만들지 않기 위해서다. 출력 내용이나 조건, 바깥 입력 또는 내부 증명 자료가 바뀌면 대응 재검토를 요구한다. 지문은 변경을 찾는 장치이며 수학적 함의의 자동 증명이 아니다.

받는 node는 `input_ports.<name>`에 연결 edge, `requires` 출력 참조, 검토 당시 `reviewed_fingerprint`를 둔다. 없는 출력, 다른 출력 전달, 검토 기록 누락, 지문 변경을 진단한다. 문제가 있는 사용처와 그 graph 안의 후속 node를 재검토 대상으로 표시하고, 하위 graph가 미완결이면 바깥 vertex에도 반영한다. 생성기가 검토 지문을 자동 갱신하거나 사용자 전용 confirmed로 바꾸지 않는다. 다른 기존 edge는 여전히 이 검사 범위 밖이다.

검사는 `tools/output_contracts.py`, 결함 주입 회귀 시험은 `tools/test_output_contracts.py`다. `check.py`는 참조 오류를 오류로, 변경 후 재검토는 경고로 보고한다. 보기에서도 edge와 node에 별도로 표시한다.

### 7.4 연결선과 라벨의 위치

`viewer/edge-routing.js`는 다른 node를 가로지르는 직선을 발견하면 node 위·아래의 우회 경로 후보를 평가한다. 라벨은 실제 경로의 길이를 따라 잡은 기준점 근처에 놓는다. 라벨을 선에서 떨어뜨린 경우 짧은 보조선을 그린다. `fresh`의 `c1`처럼 양 끝 사이에 다른 node가 있는 경우에도 라벨만 이동시키지 않는다. 복잡한 모든 graph에서 교차가 없다는 보장은 아니다. 회귀 시험은 `node redesign/proofmap/tools/test_edge_routing.cjs`다.

### 7.5 edge 전용 전제 모델

`fv`와 `cp`는 `premise_mode: "edges_only"`다. 이 모드에서 `contexts`, node의 독립 `conditions`, `local_context`는 전제를 공급할 수 없다. 새로 추가하면 검사 오류와 미완결 표시가 발생한다. 다른 graph의 예전 context 지원은 유지한다.

부모가 제공하는 입력은 공급 node의 `outputs`에 `role: "given"`과 이름 붙은 `clauses`로 선언한다. 각 항목은 `statement`, `defines`, `bindings`를 가진다. 이는 외부 가정·대상 정의·인용한 사실의 선언이며, 파생 결과의 증명이 아니다. 예를 들어 `top.O1.outputs.fv_inputs`는 setting, insertion, terminal, recursion, kernel, bounds, path_mean 항목을 제공한다. 모든 파생 출력은 기존처럼 유도와 검토 기록이 필요하다. 자식의 edge 전용 graph 안에서 새 given 출력을 생성하는 것은 금지한다.

`output_ref.clauses`는 지정 항목을 그대로 선택한다. 선택은 대입이나 새 조건 추가를 수행하지 않는다. 외부 입력 node는 `external_ref`뿐 아니라 **부모 vertex로 실제 들어오는 `import_edge`**와 선택한 `statement_ref`를 적는다. 부모 edge가 공급하는 항목의 부분집합인지 검사한다. 외부 입력의 진술 사본을 따로 쓰지 않는다. 예:

```json
{
  "id": "X1", "kind": "external", "external_ref": "XO",
  "import_edge": "diff-e9",
  "statement_ref": {"graph": "top", "node": "O1", "output": "fv_inputs",
                    "clauses": ["terminal", "recursion"]}
}
```

같은 공급을 여러 계산이 쓰면 공유 입력 node와 실제 fan-out edge를 둔다. 각 수신은 필요한 항목만 선택한다. `fv.CP`가 공통 설정을 받으므로 그 하위 `cp`의 `XS`도 부모 CP의 실제 `g3`에서 가져올 수 있다. 이 입력을 부모에게 먼저 추가하지 않고 자식에서 자유롭게 선언하는 것은 허용되지 않는다.

`bindings`는 표기가 같은 기호의 의미를 식별하는 고정 id다. 수신 node의 `requires_bindings`와 실제 공급 id가 다르거나 충돌하면 오류다. 이는 변수 의미를 자연어에서 추론하는 기능이 아니라 명시적 binding 대응 검사다.

로컬 도입은 두 종류만 허용한다. `notation`은 입력 기호로 만든 약어의 정의이고, `arbitrary_index`는 입력에서 받은 유한 범위 안의 지표 선택이다. `introductions`에는 symbol, scope, 필요한 입력 기호 및 expr 또는 domain을 기록한다. 가정 문장이나 conditions를 넣는 용도로 쓸 수 없다. 유도는 `intro:1`처럼 참조한다. 현재 c 약어는 없애고 경계를 norm/a로 풀어 썼다.

로컬 지표를 밖으로 내보내는 출력에는 `produces.generalizes`로 닫는 scope를 기록한다. 귀납의 자기 edge는 `loop.index_scope`로 그 지표를 지정한다. 도입하지 않은 범위, 다른 scope의 사용, 닫지 않은 지표를 오류로 보고한다. 이 메타데이터만으로 전칭화의 수학적 정당성이 자동 증명되는 것은 아니다.

전체 수학적 진술, 자연어 근거와 기호 목록의 완전성은 여전히 내용 검토 대상이다. 검사기는 등록된 전제·선택·binding·범위 장치의 일관성을 검사하며, 자연어 `by` 안의 임의 주장까지 판정하지 않는다. 회귀 시험은 `checks/2026-11-14-edge-only/test_edge_only.py`다.

### 7.6 입력 동기화의 적용 범위 표시

`integration_status.py`는 원본 JSON에서 다음을 서로 독립적으로 집계한다. 생성 후 펼쳐진 본문으로 집계하지 않는다.

- **전제 전달 방식:** `edges_only` 적용 여부. 기존 graph는 미변환으로 표시한다.
- **부모 입력 참조:** `import_edge`가 실제 부모 vertex의 입력이고, `statement_ref`가 그 edge의 출력 항목 부분집합인지 검사한다. 외부입력 이름만 일치하는 것은 항목 참조 연결에 세지 않는다.
- **출력 참조 범위:** `output_ref` edge 수/전체 수 및 평문 edge 목록. 평문 내용은 자동 동기화되지 않으며 그 자체로 수학적 충돌은 아니다.
- **별도 본문:** given 출력의 소유자가 전체 본문도 저장하거나, 상속 본문과 별개로 출력 항목을 전달하면 의미 대응 미검토로 표시한다. 이는 검출한 모순이 아니라 미검토 범위다.
- **중복 선택:** 같은 given 출력의 같은 항목을 서로 다른 외부입력이 받으면 중복을 표시한다. 이는 수학적 모순과 구별한다.
- **출력 대응 재검토:** 기존 contract 검사 결과를 그대로 싣는다. 화면 생성은 검토 지문을 갱신하지 않는다.

상단 「입력 동기화 · 적용 범위」에서 여섯 graph 현황과 현재 graph의 미적용 edge/참조 충돌/재검토 위치를 확인한다. 외부입력 패널에서는 선택 항목과 실제 부모 입력 edge로 이동할 수 있다. 국소 완결, 참조 연결, 전체 본문의 의미 대응을 한 상태로 합치지 않는다.

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
