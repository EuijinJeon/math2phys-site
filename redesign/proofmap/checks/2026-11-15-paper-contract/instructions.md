# 지시: 절 단위 계약 채우기 (증명은 열지 않는다)

저장소 루트: `/Users/euijinjeon/math2phys-site`. 원문: `redesign/source/sections/<절>.tex`. 카드(읽기만, 고치지 않는다): `redesign/cards/<id 의 ':' 를 '.' 로>.md`.

너의 일: 맡은 절의 node마다 **계약**을 적는다 — 진술 범위, 출력 항목, 그리고 node가 밖에서 받는 입력 하나하나를 어디에 묶는지. 증명의 유도는 쓰지 않는다. 증명 본문은 빠진 의존을 찾으려고 한 번 읽는다.

## 읽을 것

1. 묶음 파일(지시문이 경로를 준다): 맡은 node의 기계 뼈대(`skeleton`), 논문 전체 node 목록(`catalog`), 주인 없는 카드 목록(`unowned_cards`), 앞 단계가 이미 만든 출력 항목·기호·바닥(`prior`, 있으면).
2. 맡은 절의 tex 전체(줄 번호와 함께, 예: `cat -n`).
3. 묶음이 가리키는 카드 파일은 단서로만 읽는다. 카드는 틀릴 수 있다. 모든 주장은 원문 줄로 확인한다.
4. 다른 절의 tex 는 묶는 곳(출력 항목·정의)의 줄을 확인할 때만, 그 줄 근처만 읽는다.
5. 그 밖(`redesign/proofmap` 의 JSON·문서, L2, 용어집)은 읽지 않는다.

## node 와 출력 항목

- node 는 뼈대가 준 것만이다(번호 붙은 theorem·lemma·proposition·corollary와 밖에서 참조되는 번호 식의 문단). 새 node를 만들지 않는다. 뼈대의 줄 범위가 틀렸으면 고치고 `span_fix` 에 적는다.
- `outputs`: 그 node의 진술(문단)이 내놓는 항목. 번호 식 하나, 또는 진술의 주장 하나가 항목 하나다. `id` 는 짧은 영문 snake_case, `statement` 는 한국어 + TeX(`$...$`)로 원문과 같은 뜻만(더 말하지 않는다), `lines` 는 [시작, 끝]. 원문 label 이 있으면 `label` 에 적는다. 증명 안의 번호 식을 밖에서 참조하면 그 node의 항목으로 두고 `exported: true`.
- 원문에 없는 내용을 적어야 하면 `author_filled` 에 무엇을 채웠는지 적는다.

## 입력 (`needs`)

입력 하나 = node의 진술이나 증명이 **그 node 범위 밖에서** 가져다 쓰는 것 하나: 다른 곳의 결과(식·lemma), 또는 다른 곳에서 정의된 개념·기호·관례. 개념 단위로 센다(기호 글자마다가 아니다). $\mathbb E$, $\log$, Poisson 분포 같은 표준 표기는 입력이 아니다. 표준 정리를 증명에서 실제로 쓰면(예: Cauchy–Schwarz, Jensen, 지배 수렴, Fubini) 입력이고 바닥에 묶는다.

각 입력을 정확히 하나에 묶는다:

| `binding.type` | 묶는 곳 | 필요한 것 |
|---|---|---|
| `node` | `catalog` 의 다른 node 의 출력 항목 | `node`(label), `item`. 그 항목이 `prior` 나 네 산출에 없으면 `new_item: {statement, lines}` 를 같이 적는다(그 node 범위 안의 줄) |
| `symbol` | 논문 전체 기호·정의 표의 항목 | `symbol` id. 표에 없으면 `symbols_new` 에 추가: `{id, tex, defined_at: "파일.tex 줄–줄", text}`. 정의 위치는 하나. 같은 기호가 절마다 다른 뜻이면 다른 id 로 두고 `note` 에 적는다 |
| `floor` | 선언한 바닥 | `floor` id. 없으면 `floors_new` 에 추가: `{id, kind: "cited"|"standard", statement, cite: "\\cite 키"(cited 일 때), cited_at: "파일.tex 줄"}`. 인용 정리는 원문이 `\cite` 로 인용하는 줄을 적는다 |
| `open` | 어디에도 못 묶음 | `why`. 억지로 묶지 않는다 |

- 번호 없는 진술(정리처럼 쓰이는데 번호·환경이 없는 문단, remark 안의 주장)은 node 가 아니다. 그것이 정의·관례면 `symbol` 로 받고, 사실 주장이면 `open` 으로 남기고 `why` 에 "번호 없는 진술, 파일 줄" 을 적는다.
- 각 입력에 `used_at`(이 node 안에서 쓰는 원문 줄 목록, 정수)을 적는다. 반드시 원문에서 확인한 줄이다.
- `origin`: 뼈대의 `machine_refs` 에서 온 것이면 `"machine"`, 뼈대의 `card_refs` 에서 온 것이면 `"card"`, 네가 증명 본문을 읽고 찾은 것이면 `"llm"`. 둘 이상이면 목록. 카드 의존을 원문에서 확인했으면 `card_ids` 에 그 카드 id.
- 카드가 말하는 의존(뼈대 `card_refs`)을 원문 그 node 범위에서 쓰는 줄을 찾지 못하면 `needs` 에 넣지 말고 `card_deps_rejected: [{card, use, why}]` 에 적는다. 하나도 빠뜨리지 말고 뼈대의 card_refs 하나하나를 받아들이거나 거절한다.
- 카드와 원문이 어긋나는 곳(줄 범위, 진술 경계, 카드가 말하는 내용)은 `card_mismatches: [{card, what}]`.

## 앞 단계 node 에 대한 요청

`prior` 에 있는 node(앞 단계가 만든 것)에 항목이 없으면 `binding.new_item` 으로 항목 **추가**를 요청한다(그것으로 충분하다). 기존 항목의 내용·조건이 틀렸거나 바꿔야 쓸 수 있으면 `change_requests: [{node, item, change, why}]` 에 적는다(고치지 않는다). 네가 맡은 절끼리는 뒤 node 가 앞 node 의 새 항목을 필요로 하면 앞 node 의 `outputs` 에 넣고 그 항목에 `added_by: "<쓰는 node>"` 를 단다.

## 절 머리·remark

맡은 절의 절 머리 관례(첫 문단의 약속)와 remark·번호 없는 정의 문단마다 `unplaced: [{lines, what, handled}]` 한 줄. `handled` 는 `"symbol:<id>"`(기호 표로 받음) 또는 `"list"`(받지 못해 목록에 남김).

## 산출

절마다 파일 하나 `redesign/proofmap/checks/2026-11-15-paper-contract/out/<절>.json`:

```json
{"section": "trees",
 "nodes": [{"id": "tree:insertion", "title": "짧은 한국어 제목", "env": "lemma",
   "statement_span": [84, 111], "proof_span": [113, 133], "span_fix": null,
   "outputs": [{"id": "insertion_identity", "label": "tree:density", "statement": "...", "lines": [90, 95]}],
   "needs": [{"id": "path_kernels", "what": "path kernel 열의 정의", "used_at": [86],
              "binding": {"type": "symbol", "symbol": "path_kernel"}, "origin": ["card"], "card_ids": ["x:tree-path-kernels"]}],
   "card_deps_rejected": [], "card_mismatches": []}],
 "symbols_new": [], "floors_new": [], "change_requests": [], "unplaced": []}
```

수식은 `$...$` 안에 TeX 로 쓴다(유니코드 수식 금지). JSON 이 유효한지 `python3 -m json.tool` 로 확인한다.

맡은 절은 지시문의 순서대로 처리한다(앞 절의 산출을 뒤 절이 쓴다).

**마지막 답은 짧게**: 절마다 node 수, 입력 수, 종류별(node/symbol/floor/open) 수, 거절한 카드 의존 수, 어긋남 수, change_requests 수. 다른 내용은 답에 쓰지 않는다(파일에 있다).
