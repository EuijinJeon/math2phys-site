# 논문 전체 계약: 외부 입력 닫기 — 2026-11-15

앞 보고서: `checks/2026-11-15-move5-contract/`, `-move5-cost/`, `-move5-cards/` 의 `REPORT.md`. 증명은 열지 않는다. 모든 근거는 `proposed`, 모든 node는 `sketch`.

## 0. 통과 기준 (작업 시작 전에 적음)

"닫힘"(사용자 동의): node의 입력 하나가 (1) 논문 안 다른 node의 출력 항목(원문 줄 포함), (2) 논문 전체 기호·정의 표의 항목(정의 위치 하나), (3) 선언한 바닥(인용 정리: 인용 표기와 인용하는 원문 줄 / 표준 사실) 가운데 하나에 묶이면 닫힌 것이다. (3)은 "표시를 단 닫힘"으로 따로 센다. 어디에도 묶이지 않으면 열림으로 남긴다.

| # | 기준 | 판정 방법 |
|---|---|---|
| Q1 | 뼈대가 LLM 없이 재현된다 | 뼈대 생성 스크립트를 두 번 돌려 같은 출력(`cmp`). 11개 절의 `extract_tex.py` node 후보(S·E) 전부가 `paper.json` 의 node다 |
| Q2 | 모든 입력이 분류된다 | node마다 `contract.needs` 의 입력 하나하나가 종류 1/2/3 또는 열림 가운데 정확히 하나. 분류 없는 입력 0이면 통과 |
| Q3 | **열림 0 (목표)** | 열림 수 = 0 이면 "모두 닫음". 0이 아니면 이 목표는 실패로 적고 열림 목록 전부를 싣는다. 억지로 묶지 않는다 |
| Q4 | 묶음마다 원문 줄 | 닫힌 입력마다 쓰이는 원문 줄(`used_at`)과 묶인 곳의 위치(출력 항목 `lines`, 기호 `defined_at`, 바닥의 인용 줄)가 있다. 없는 것 0이면 통과 |
| Q5 | 독립 확인 | 작성에 관여하지 않은 다른 모델 agent가 무작위 15개 이상(종류 1·2·3 각 5개 이상)을 원문 줄과 대조. 틀린 묶음 ≤ 1개(약 7% 이하)면 통과. 수와 비율을 그대로 적는다 |
| Q6 | 무효화 0 | 뒤 절 처리 중 앞 node의 기존 출력 항목 내용·조건 변경 = 0 이면 통과. 항목 추가는 통과 판정 없이 센다 |
| Q7 | 카드 의존 대조 | 카드 `uses` 가 말하는 의존마다 원문 쓰임 줄을 찾았거나, 못 찾아 넣지 않았음을 센다. 세지 않은 카드 의존 0이면 통과 |
| Q8 | 구조 검사·회귀 | `check.py graphs/paper.json` 오류 0. 기존 시험 실패 수 1/2/3(test_check/test_output_contracts/test_viewer)이 늘지 않고 `test_source_ref` 통과, move4 경고 11·move5 경고 5 그대로 |
| Q9 | 화면 | `build/paper.html` 을 브라우저에서 열어 절마다 node·edge 패널이 펼쳐지고, `audit_refs.js` 기준 맨몸 참조 0 |
| Q10 | 대응표 | `move4.json`·`move5.json` 의 외부 입력 node마다 `paper.json` 의 node·항목 대응 또는 "대응 없음". 대응 없는 수를 센다(판정 없음) |
| Q11 | 정직성 | 모든 grounding `proposed`, 완결로 올린 node 0. 원문에 없는 걸음은 `author_filled` |

측정(판정 없이 적음): 단계별 토큰(대리값이면 밝힘), 입력 총수와 종류별 닫힘·열림 수, 의존 출처별 수(기계/카드/LLM), 카드·원문 어긋남 수, 항목 추가·내용 변경 횟수, 수 5 계약(`move5.json` top)과 `paper.json` 의 decorrelation 절의 어긋남.

## 1. 결과 요약

표기: **확인** = 파일·도구 출력·브라우저로 확인한 것. **추론** = 확인한 것에서 끌어낸 것. **추측** = 근거가 약한 예상.

**열림 6, 바닥 27종(쓰임 42), 독립 확인에서 틀린 묶음 0 / 18 (부분적으로 맞음 5).**

| # | 판정 | 값 |
|---|---|---|
| Q1 | 기준을 지남 | `skeleton.py` 두 번 실행 결과가 같다(`cmp`). `extract_tex.py` 의 node 후보 50개는 모두 들어갔고, 같은 문단에 있는 참조 번호 식은 node 하나로 합쳤다(6쌍, 아래 3절 1). 그래서 node는 43개다 |
| Q2 | 기준을 지남 | 입력 436개는 모두 종류가 정해졌다: node 234, symbol 154, floor 42, open 6. 분류 없는 입력 0 |
| Q3 | **목표 실패** | 열림 6개(아래 목록). 번호 없는 진술 셋에서 나온다 |
| Q4 | 기준을 지남 | 닫힌 입력 430개 모두 `used_at` 이 있고 묶인 곳에 위치가 있다. `check.py` 의 묶음 검사 오류 0, `merge.py` 의 bad_binding 0, no_used_at 0 |
| Q5 | 기준(틀림 ≤ 1)을 지남 | Opus 검토자(작성 agent는 Sonnet, 표본은 seed 고정 무작위로 종류마다 6개)가 18개를 원문과 대조했다. correct 13, **partial 5**, wrong 0. partial은 "지남"으로 세지 않고 2절에 따로 적는다 |
| Q6 | 기준을 지남 | 앞 node 기존 항목의 내용 변경 요청 0. 항목 추가 6회(같은 agent 안 5, 뒤 단계 요청 1). 통합자 보정 1(아래 3절 2) |
| Q7 | **실패** | 카드 의존 인스턴스 702건 가운데 묶음으로 받아들인 것 656건(node 묶음 396, 주인 없는 카드의 원문 줄과 겹치는 기호·열림 260), 거절 22건, **기계로 추적되지 않은 것 24건(서로 다른 쌍 12)**(`card-account.txt`) |
| Q8 | **실패(오류 1)** | `check.py graphs/paper.json`: 오류 1 `[top] 순환: S_model → S_upper → S_model`, 경고 12(열림 6, 고립 node 2, 9개 기준 2, 보내는 edge 없음 2). 회귀: test_check 1, test_output_contracts 2, test_viewer 3 실패로 앞과 같다. test_source_ref 8 통과, 새 test_bindings 9 통과, 경로 시험 통과. move4 오류 0·경고 11, move5 오류 0·경고 5로 앞과 같다 |
| Q9 | 기준을 지남 | 내장 브라우저에서 `build/paper.html` 을 열었다. graph 10개, node 81개, edge 138개의 패널에서 맨몸 참조 0이다. 닫힌 펼침 81개를 실제로 눌러 모두 열렸다. node 패널의 "입력과 묶인 곳"은 436개로 모두 그려졌고 묶인 곳을 못 찾은 것은 0이다. "그 node 열기" 단추 4개를 눌러 4개 모두 해당 node가 열렸다. 화면 두 장을 눈으로 확인했다(decor:overlap-concentration의 입력 패널, 맨 위 edge T15). 감사 처음 판에서는 맨몸 참조 15가 나왔다(`main:formula` label 펼침 누락, MAIN 항목 이름 불일치). 고친 뒤 0이 되었다 |
| Q10 | 기록 | move4·move5 외부 입력과 선언 입력 항목 15개 가운데 대응 없음 0. consumer 4개(XM5, XM6, move5 OUT)는 입력이 아니라서 세지 않았다(`correspondence.md`) |
| Q11 | 기준을 지남 | 모든 grounding `proposed`, 안쪽 node는 모두 `sketch`. 원문에 없는 내용 표시(`author_filled`)가 붙은 출력 항목 1 |

**답 (추론).** 논문 전체를 계약 수준으로 훑으면 입력 436개 가운데 430개가 원문 안의 node·기호 표·바닥에 묶인다. 남는 6개는 모두 "정리처럼 쓰이는데 번호가 없는 문단" 셋(model.tex 65–66, trees.tex 156–176, 178–202)에서 온다. 이 셋을 node로 받을지(node 종류 확장)는 사용자 판정 대상이다. 앞 절의 기존 항목 내용을 바꿔야 한 일은 없었다. 이번에도 전파는 모두 "추가" 꼴이었다(6회). 다만 이것은 작성 agent가 낸 계약 위의 결과다. 표본 18개 대조에서 틀림은 0이고 부분은 5다. 436개 전체의 정확도는 재지 않았다.

## 2. 측정

### 단계별 토큰

| 단계 | 값 | 종류 |
|---|---|---|
| 1. 기계 뼈대(`skeleton.py`, `extract_tex.py` ×11) | LLM 0 | 확인 |
| 2a. agent A (model·trees·upper·cavity, 17 node, Sonnet) | 189,898 | 완료 알림의 `subagent_tokens` |
| 2b. agent B (perturbations·decorrelation, 15 node, Sonnet) | 228,221 | 같음 |
| 2c. agent C (comparison·reduction·주정리·consequences, 11 node, Sonnet) | 212,209 | 같음 |
| 3. 독립 확인 (Opus, 18개) | 99,131 | 같음 |
| 작성 세션 전체(읽기·도구·통합·화면 확인) | 끝날 때 문맥 288,478 | **대리값**: 앱이 보고한 문맥 크기. 시작값은 재지 않았다. 청구 토큰과 같지 않다 |

계약 작성 agent 셋의 합은 630,328이다. node당 약 14.7k이고, 입력 하나당 약 1.4k다(확인값으로 나눈 값). 수 5 PoC의 계약 단계(node 7개, 작성 세션 약 35k)와 직접 비교할 수는 없다. 이번에는 작성 세션이 원문을 읽지 않았고 agent가 읽었다.

### 입력과 출처

| | node | symbol | floor | open | 합 |
|---|---|---|---|---|---|
| 입력 | 234 | 154 | 42 | 6 | 436 |
| 출처 기계(`\ref`)만 | 3 | 0 | 0 | 0 | 3 |
| 기계 + 카드 | 74 | 0 | 0 | 0 | 74 |
| 카드만 | 94 | 122 | 1 | 6 | 223 |
| LLM 보충 | 63 | 32 | 41 | 0 | 136 |

- `\ref` 기계 추출이 잡은 것은 node 사이 의존 234개 가운데 77개(33%)다. 수 5만 볼 때의 약 41%보다 낮다.
- 카드가 말한 의존 가운데 원문에서 쓰임을 못 찾아 넣지 않은 것은 17건(서로 다른 쌍 16)이다. 카드·원문 어긋남은 6건이다. 수 5 카드 PoC는 decorrelation 한 절에서 15곳을 적었다. 이번 agent B는 같은 절에서 2건만 적었다. **추론:** 이번 지시는 의존 쪽 어긋남만 요구했고, 카드의 진술 경계까지는 보게 하지 않았다. 그래서 같은 기준으로 잰 수가 아니다.
- 바닥 27종 가운데 인용 정리는 Efron–Stein 하나다(perturbations.tex 179). 나머지 \cite 18곳은 서론·절 머리의 문헌 소개라서 증명이 쓰는 입력이 아니다(확인: `grep '\\cite'`). 표준 사실 26종은 LLM이 찾은 것이 41/42 쓰임이다.
- 기호·정의 표는 35항목이다. 같은 id가 절마다 다른 뜻인 경우(이름 충돌)는 0으로 기계 확인했다. 다만 독립 확인 k=11은 "root는 개수·type·site다"가 cavity.tex 29와 perturbations.tex 60–61 두 곳에 정의되어 있다고 지적했다. **정의 위치 하나**를 기계는 검사하지 못하고 표 작성 agent의 판단에 맡겨져 있다.

### 독립 확인 18개 (`independent-check.json`)

| 종류 | correct | partial | wrong |
|---|---|---|---|
| node | 4 | 2 (k=2, 5) | 0 |
| symbol | 4 | 2 (k=9, 11) | 0 |
| floor | 5 | 1 (k=17) | 0 |

partial의 내용:
- k=2: 주정리가 쓰는 "승수 a는 비대칭 의존 가능" 은 model.tex 43–44에 있는데, 묶인 항목 범위(25–34) 밖이다.
- k=5: 검토자는 묶인 node가 `model:chain`(72행)이라 `model:functional`(112행)과 다르다고 보았다. 실제로는 같은 문단의 두 label을 node 하나로 합친 결과다(3절 1). 항목 `functional` 은 112–116을 가리킨다. 표본 파일이 합친 사실을 보이지 않아서 생긴 오해로 **추론**한다. 그대로 partial로 센다.
- k=9: 84행은 그 약속을 스스로 정한다. 바깥 입력으로 쓰는 줄은 89행뿐이다.
- k=11: 같은 약속이 두 곳에 정의되어 있다(위).
- k=17: Efron–Stein은 인용되지만, 논문이 181–190에서 "For completeness"로 직접 증명한다. 순수 인용 바닥이라기보다 node 자신의 증명에 가깝다.

### 항목 추가와 내용 변경

추가 6회, 내용 변경 0회, 통합자 보정 1회. 추가 목록은 아래에 있다. 뒤 단계가 앞 단계 node에 항목을 요청한 것은 `cavity:increment.log_insertion_bound`(comparison이 요청) 1건이다.

### 수 5 계약(`move5.json` top)과 paper의 decorrelation 절

확인(스크립트 출력 비교):
- 7 node의 진술·증명 줄 범위는 모두 같다.
- node 사이 의존: 수 5 계약의 의존(외부 X_* 포함)은 paper에 모두 있다. paper에만 있는 것은 셋이다. THM ← `decor:average-holder`(68, 585, 600행; 수 5 카드 PoC가 "THM ← AVG 정규화"를 찾았으나 넣지 않고 열림으로 둔 것), CC·THM ← `tree:multioverlap`. THM ← L² 사영, 전체 분산 법칙은 바닥으로 새로 적었다. 기호 수준의 차이는 비교하지 않았다.
- 출력 항목 경계가 다르다. 수 5의 `DC.larger_tree`(203–205)와 `CC.V_to_zero`(522–523)는 paper에서 출력 항목이 아니다. `CC.relative_cost` 345–353 대 paper `relative_absolute_cost` 332–352다. THM의 `main` 은 paper에서 `overlap_concentration` + `singleton` 둘로 나뉜다. 외부 쪽에서는 move5 `X_CH.relative_charging`(406–414)이 paper에서 `J_nonzero`(406–410) + `relative_charging`(411–414)로 나뉜다. `X_TI.identity`(452–470)는 paper에서 `tree_identity` 454–464다.
- 수 5에서 열림으로 남은 "κ(S) ≠ 0 의 근거"(HANDOFF 4절 6)를 paper가 닫았는지는 이번에 확인하지 않았다.

### move4·move5 외부 입력 대응표

`correspondence.md`(손으로 적은 `correspondence.json` 을 `correspond.py` 가 paper.json에 대조). 입력·선언 입력 15개 모두 대응이 있다. 그 가운데 6개는 node가 아니라 기호에 대응한다(XFAM, X_TI.anchor_constraint, X_EXT.rule, X_SAMP 둘, O1 일부). 대응은 작성자가 정했고 독립 확인은 하지 않았다.

## 3. 실패한 것, 결정이 맞지 않은 곳 (고치지 않고 적음)

1. **같은 문단의 참조 번호 식 합치기(작성자 판단).** `extract_tex.py` 는 label 하나마다 E node를 만든다. 같은 문단(같은 줄 범위)의 둘은 한 node로 합쳤다(model:integrability+hamiltonian, model:factorization+positivity, model:chain+vs+functional, tree:Y-recursion+updated-kernel, tree:telescoping+Q-rule, comp:shape-error+shape-error-bound). 결정 1의 "번호 식 = node"를 글자 그대로 따르면 node가 49개 남짓이 된다. 독립 확인 k=5의 오해가 이 합치기에서 나왔다.
2. **순환 오류(Q8 실패).** model.tex 38–41은 "positivity의 기대값이 유한하다는 것은 upper:bound에서 보인다"고 쓴다. 그래서 `model:factorization` 이 `upper:bound` 의 항목 `bounded_factors` 를 받고, `upper:bound` 는 `model:factorization` 을 받는다. 항목 단위로는 순환이 없다(factorization 정의 → upper 증명 → 유한성 주장). node 단위와 절 단위에서는 순환이다. 억지로 끊지 않았다. 바깥 사용처가 node를 항목 단위로 다루게 할지, 이런 앞 참조 주장을 따로 둘지는 사용자 판정 대상이다.
3. **통합자 보정 1.** agent A는 upper.tex 12의 "Under the hypotheses of main:theorem"을 `main:theorem` 에 새 항목 `hypotheses` 를 추가해 묶었다. 그러면 MAIN → upper → MAIN 순환이 생긴다. 통합자가 이 묶음을 `model:integrability.integrability` 로 바꾸었다(factorization·positivity는 같은 node가 이미 따로 묶었다; `corrections.json`, 원래 묶음은 `binding_by_author` 에 보존). 그 뒤 agent B·C에는 주정리에 묶지 말라고 지시했다. 지시가 결과를 움직였다.
4. **Q7 실패.** 카드 의존 12쌍(24건)이 받아들임·거절 어느 쪽으로도 기계 추적되지 않는다. 대부분은 이렇다. `x:model-hypotheses`(주정리·upper·consequences): agent는 model node 항목에 묶었지만 카드 id를 적지 않았다. `x:comp-standing`: 원문 줄이 comp node 범위 안이라 주인 없는 카드가 아니다. `x:reduction-power-mean-scaling`: 바닥으로 묶었다(어긋남으로 보고됨). 하나는 실제 누락일 수 있다. `decor:conditional-concentration ← tree:extension-expansion` 은 묶이지도 거절되지도 않았다(paper는 기호 `extension_history` 를 쓴다). 지시가 "card_ids 에 쓴 카드 id"를 강제하지 않아 추적이 끊겼다.
5. **"열림 0"을 얻지 못한 이유는 결정 1의 node 종류.** 번호 없는 진술 셋은 각각 둘 이상 node가 쓴다(해석적 경계는 log-expansion·extension-expansion; pert:analytic은 extension-expansion의 항목을 거친다). 이것을 node로 세우면 6개는 모두 종류 1로 닫힐 것이다(**추론**).
6. **remark와 절 머리.** 60개 가운데 35개를 기호 표로 받았고 25개는 목록에 남겼다(아래). 남은 것은 대부분 문헌 소개·개요·그림·"말하지 않는 것" remark다. 그 가운데 decor 613–623(극한 순서 remark)과 pert 538–547(선택 순서 remark)은 다른 node가 쓰는 극한 순서 약속과 내용이 겹친다. 이번에는 둘 다 기호(`decor_limit_order`, `pert_selected_limits`)가 절 머리·본문 줄로 받았다.
7. **카드·원문 어긋남 수는 수 5 PoC와 같은 기준이 아니다**(2절).
8. **서론·개관(introduction.tex, overview.tex)은 번호 붙은 진술이 없다.** 맨 위 graph에 edge 없는 node로 두었다(경고 2). 그 안의 \ref 12개는 앞·뒤를 가리키는 안내다.
9. 보기와 도구를 고쳤다. `carries.py`: carries 항목의 `graph`. `build_viewer.py`: 원문 파일을 decorrelation.tex로 고정하던 곳, node의 "입력과 묶인 곳" 펼침, 하위 graph label 이동, `main:` label, 기호 tex 없을 때. `template.html`: `needBlock`. `check.py`: `check_bindings`. 기존 시험 실패 수는 같다. `build/move4.html`·`move5.html` 은 새 틀로 다시 만들지 않았다.

## 4. 목록

전부 `lists.md` 에 있다. 열림 6, 바닥 27, 받지 못한 remark·절 머리 25, 카드 의존 거절 17, 카드·원문 어긋남 6, 항목 추가 6. 열림과 바닥은 아래에 그대로 옮긴다.

### 열림 전부 (6)

| node | 입력 | 쓰는 줄 | 이유 |
|---|---|---|---|
| `model:trial-bounds` | $\|\log C_\theta\|,\|U_\theta\|\le B(\theta)$ (message 에 대해 균등) | 126, 127 | 번호 없는 진술, model.tex 65–66 |
| `tree:log-expansion` | protected leaf 가 있을 때의 미분 규칙: 남는 항은 새 fresh path 뿐이고 계수는 $\gamma_\beta$ | 244, 245, 246 | 번호 없는 진술, trees.tex 178–202 |
| `tree:log-expansion` | 복소 영역에서의 해석성과 균등 경계 (수렴 영역) | 231, 254 | 번호 없는 진술, trees.tex 156–176 |
| `tree:extension-expansion` | protected leaf 가 있을 때의 미분 규칙 | 299, 300, 301 | 번호 없는 진술, trees.tex 178–202 |
| `tree:extension-expansion` | 해석적 경계 | 294, 295 | 번호 없는 진술, trees.tex 156–176 |
| `upper:bound` | $\|\log C_\theta\|,\|U_\theta\|\le B(\theta)$ (message 에 균등) | 53, 54, 88, 89 | 번호 없는 진술, model.tex 65–66 |

### 바닥 전부 (27개, 쓰임 42회)

| id (쓰임) | 종류 | 인용 | 진술 |
|---|---|---|---|
| `poisson_splitting` (2) | standard | — | Poisson 과정의 분할(thinning)과 중첩, 평균이 다른 두 Poisson 과정을 공통점으로 결합하면 서로 다른 점의 기대 개수는 평균의 차이 이하. |
| `regular_conditional_probability` (1) | standard | comparison.tex 52–53 | 표준 Borel 공간 위에서 조건부 확률분포(확률 kernel)는 가측 버전을 가진다. |
| `tv_product_telescoping` (1) | standard | comparison.tex 112–118 | 곱측도의 전변 거리: $\\|\mu^{\otimes a}-\nu^{\otimes a}\\|_{\rm TV}\le a\\|\mu-\nu\\|_{\rm TV}$ (망원합). |
| `tv_bounded_integral` (1) | standard | comparison.tex 119 | 절댓값이 1 이하인 함수의 두 확률측도에 대한 적분의 차는 전변 거리의 2 배 이하이다. |
| `wald_identity` (2) | standard | comparison.tex 186–190 | 독립인 Poisson 개수 $K$ 와 같은 법칙의 (적분가능한) 항들의 합에서 $\mathbb E\sum_{j\le K}X_j=\mathbb EK\cdot\mathbb EX_1$ (Wald). |
| `jensen` (2) | standard | — | Jensen 부등식: 오목 함수 (예: $x\mapsto x^\gamma$, $0<\gamma\le1$) 에 대해 평균의 함수 값이 함수 값의 평균 이상 (질량 $\le1$ 인 측도에도 성립); 조건부 기댓값은 제곱 노름을 줄인다. |
| `martingale_orthogonality` (1) | standard | — | 유계 (벡터) martingale 의 증분은 서로 직교하므로 증분 제곱의 합은 마지막 값의 제곱 노름 이하이다. |
| `l2_projection` (1) | standard | — | 조건부 기댓값 $\mathbb E[X\mid\mathcal G]$ 는 $L^2$ 에서 $\mathcal G$-가측 함수 중 $X$ 에 가장 가까운 것이다. |
| `product_difference` (3) | standard | — | $x_j,y_j\in[-1,1]$ 이면 $\|\prod_jx_j-\prod_jy_j\|\le\sum_j\|x_j-y_j\|$ (따라서 제곱 노름은 $s\sum_j$ 로 누를 수 있다). |
| `power_mean_scaling` (2) | standard | — | 조건부 거듭제곱 평균 $(\mathbb E[X^m\mid\mathcal G])^{1/m}$ 은 $X$ 에 대해 단조이고, $\mathcal G$-가측 양수 인자를 곱하면 그 인자만큼 곱해진다 (동차). |
| `efron_stein` (1) | cited | EfronStein perturbations.tex 179 | Efron–Stein 분산 부등식: 독립 입력의 함수 $Z$ 에 대해 $\operatorname{Var}Z\le\frac12\sum_j\mathbb E(Z-Z^{(j)})^2$ ($Z^{(j)}$ 는 $j$ 번째 입력을 독립으로 다시 뽑은 것; 동일 분포나 대칭 통계량은 필요 없다). |
| `total_variance` (2) | standard | — | 전체 분산 법칙: $\operatorname{Var}Z=\mathbb E\operatorname{Var}(Z\mid\mathcal G)+\operatorname{Var}(\mathbb E[Z\mid\mathcal G])$. |
| `convex_derivative_monotone` (1) | standard | — | 볼록 함수의 도함수는 단조 증가하고 차분몫은 양쪽 도함수 사이에 끼인다. |
| `fubini` (1) | standard | — | Fubini–Tonelli: 유계(또는 음이 아닌) 가측 함수의 곱측도 적분은 순서를 바꿔도 같다. |
| `markov_inequality` (1) | standard | — | Markov 부등식: $X\ge0$ 이면 $\mathbb P(X>a)\le\mathbb EX/a$. |
| `diagonal_subsequence` (1) | standard | — | 유계 실수열은 수렴 부분수열을 가지며, 가산 개의 유계 수열 족에는 대각선 논법으로 모두 동시에 수렴하는 공통 부분수열이 있다. |
| `cauchy_schwarz` (4) | standard | — | Cauchy–Schwarz 와 Jensen: $\mathbb E\|X\|\le(\mathbb EX^2)^{1/2}$, 합과 적분에 대한 $\sum\|x_iy_i\|\le(\sum x_i^2)^{1/2}(\sum y_i^2)^{1/2}$. |
| `poisson_moments` (1) | standard | — | Poisson 확률변수는 모든 moment 가 유한하고 분산은 평균과 같다. |
| `poisson_add_one` (1) | standard | — | Poisson add-one (Mecke/Palm) 항등식: 평균 $\lambda$ 인 Poisson 개수 $n$ 의 점들에 대한 합 $\mathbb E\sum_{q\le n}F(\xi_q,\text{나머지})$ 는 독립인 새 점 $\xi$ 를 더한 계에서 $\lambda\,\mathbb EF(\xi,\text{나머지}\cup\{\xi\})$ 와 같다. |
| `cauchy_estimates` (1) | standard | — | 원판에서 $\|f\|\le M$ 인 해석 함수의 Taylor 계수는 $\|a_k\|\le M\rho^{-k}$ (Cauchy 추정), 더 작은 원판에서 Taylor 꼬리는 기하급수적으로 작고 도함수도 균등하게 유계이다. |
| `polarization` (1) | standard | — | 분극 항등식: 대칭 $k$-선형 형식 $\mathcal L$ 과 $Q(g)=\mathcal L(g,\ldots,g)$ 에 대해 $\mathcal L(g_1,\ldots,g_k)=\frac{1}{2^kk!}\sum_{\epsilon\in\{\pm1\}^k}\bigl(\prod_j\epsilon_j\bigr)Q\bigl(\sum_j\epsilon_jg_j\bigr)$. |
| `diff_under_expectation` (2) | standard | — | 유계 함수의 적분(기댓값) 안에서 매개변수로 미분할 수 있다 (유계 지배에 의한 적분 기호 아래 미분). |
| `analytic_taylor` (2) | standard | — | 원판에서 해석적인 함수는 그 원판 위에서 Taylor 급수와 같고, 계수는 $k$ 차 도함수를 $k!$ 로 나눈 값이다. |
| `poisson_derivative` (1) | standard | — | Poisson 평균에 대한 미분: 유계 $g$ 에 대해 $\frac{d}{d\lambda}\mathbb E\,g(\mathrm{Pois}(\lambda))=\mathbb E[g(\mathrm{Pois}(\lambda)+1)-g(\mathrm{Pois}(\lambda))]$. |
| `dominated_convergence` (3) | standard | — | 지배 수렴 정리. |
| `convex_even_power` (1) | standard | — | $p$ 가 짝수이면 $x\mapsto x^p$ 는 $\mathbb R$ 위에서 볼록이다. |
| `mean_value` (2) | standard | — | $[0,1]$ 에서 연속이고 $(0,1)$ 에서 미분가능한 $\varphi$ 의 $\varphi^{\prime}$ 가 위에서 $c$ 로 막히면 $\varphi(1)-\varphi(0)\le c$ (적분 또는 평균값 정리). |

## 5. 파일

- `skeleton.py` → `skeleton.json`(기계 뼈대: node 43, 입력 후보 269, 주인 없는 카드 60, 절 의존 순서), `extract/*.json`(1단계 출력)
- `instructions.md`, `make_bundle.py` → `bundle-{A,B,C}.json`(절 묶음), `out/*.json`(agent 산출 원본)
- `merge.py` → `graphs/paper.json`, `stats.json`. `corrections.json`(통합자 보정 1)
- `sample.py` → `sample.json`, `independent-check.json`(독립 확인)
- `card_account.py` → `card-account.txt`(Q7), `correspondence.json`·`correspond.py` → `correspondence.md`(Q10), `make_lists.py` → `lists.md`
- 보기 `build/paper.html`. 검사 `tools/check.py graphs/paper.json`, 시험 `tools/test_bindings.py`

```bash
python3 redesign/proofmap/checks/2026-11-15-paper-contract/merge.py && python3 redesign/proofmap/tools/check.py redesign/proofmap/graphs/paper.json
```

## 6. 2026-11-16 — external node를 보내는 진술 단위로 쪼갬

요청(상위 세션이 옮긴 사용자의 말): "절 바깥에서 온거는 그냥 바깥에서 온거라고 퉁치는데 이러면 안되지않나". 고치기 전 판의 스냅샷은 `paper.v1-section-externals.json` 과 `paper.v1.html` 이다.

**한 것 (확인).**
- `merge.py`: 절 graph의 external node를 **보내는 node 하나당 하나**로 만든다. id는 `X_<label>`(예: `X_cavity_increment`)다. 제목은 "§절번호 + 그 진술의 제목"이고, 주정리는 제목 그대로다. 각 external은 `source_node: {graph, node}` 와, 그 절로 싣는 항목 `items` 를 갖는다. `external_ref`(보낸 절)와 `import_edge`(맨 위 edge)는 그대로다. 그래서 `check.py` 의 닿는 면 검사가 그대로 통한다. 기호 표와 바닥에 묶인 입력은 바꾸지 않았다.
- 내용은 바꾸지 않았다. 스냅샷과 비교한 결과 안쪽 node의 `contract`, 기호 35, 바닥 27, 맨 위 edge 22개가 모두 같다. 함께 바꾼 것은 MAIN 제목의 "주정리 주정리" 중복 하나뿐이다.
- 보기(`build_viewer.py`, `template.html`): `source_node` 가 있는 external을 누르면 싣는 항목이 진술·원문 줄과 함께 그 자리에 펼쳐진다. 원래 절의 그 node로 가는 단추 "원래 절의 그 node 열기"도 있다. 같은 절에서 온 external은 절 순서, 그 안에서는 원문 줄 순서로 놓인다. 그래서 지도 왼쪽 열에 이웃해 서고, 제목 앞의 "§n"으로 어느 절에서 왔는지 보인다. 테두리로 묶어 보이게 하지는 않았다.
- 맨 위 절 → 절 edge는 이미 "진술 — 항목" 쌍 전부를 펼친다. 바꾸지 않고 확인만 했다. 22개 edge의 펼침 수 합 107은 JSON의 `carries` 합 107과 같다. 펼침 없는 edge는 0이다.

**검사 (확인).**
- `check.py graphs/paper.json`: 오류 1(앞과 같은 S_model ↔ S_upper 순환), 경고 12로 앞과 같다.
- 시험 실패 수는 test_check 1, test_output_contracts 2, test_viewer 3으로 앞과 같다. test_bindings·test_source_ref 통과, 경로 시험 통과. move4 경고 11, move5 경고 5로 앞과 같다.
- 브라우저 감사(`audit_refs.js` 와 같은 꼴): graph 10개, node 106개, edge 168개에서 맨몸 참조 0이다. 닫힌 펼침 106개가 모두 열렸다. external 43개 모두 항목이 펼쳐졌고(합 226), "원래 절의 그 node 열기" 단추를 눌러 43개 모두 해당 node가 열렸다.
- 마우스로 직접 눌러 본 것: `s_comparison` 의 §2 시행 법칙 external을 눌러 항목이 펼쳐졌고, 단추를 눌러 `s_model` 의 `model:chain` 으로 건너갔다. `s_decorrelation` 의 §6 tree-identity external을 눌러 항목 4개와 단추를 확인했다.
- `correspondence.md`: 15개 가운데 대응 없음 0으로 깨지지 않았다(external id가 아니라 원문 label·항목으로 대응하기 때문).
- 화면에 따로 보인 것이 있다. external 패널의 "외부 입력" 칸에 "edge 내용 미작성: e1…"이 뜬다. 쪼개기 전에도 모든 edge가 "내용 미작성"이었다(맨 위 칸 "edge 내용 미작성 29/29"). 계약 edge는 `complete` 를 달지 않기 때문이다. 이번 변경과는 무관하다.

**한 장의 node 수 (확인).**

| 절 graph | 안쪽 진술 | external (전 → 후) | output | 한 장 합 |
|---|---|---|---|---|
| s_comparison | 6 | 5 → 13 | 1 | 20 |
| s_perturbations | 8 | 3 → 7 | 1 | 16 |
| s_decorrelation | 7 | 2 → 4 | 1 | 12 |
| s_trees | 10 | 0 → 0 | 1 | 11 |
| s_upper | 1 | 2 → 8 | 1 | 10 |
| s_consequences | 3 | 2 → 4 | 1 | 8 |
| s_model | 4 | 1 → 1 | 1 | 6 |
| s_cavity | 2 | 2 → 3 | 1 | 6 |
| s_reduction | 1 | 3 → 3 | 1 | 5 |

- 한 장 전체(external·output 포함)가 9개를 넘는 절은 **5개**다: comparison, perturbations, decorrelation, trees, upper.
- `check.py` 의 9개 기준은 안쪽 node만 센다. 그 기준으로 넘는 것은 s_trees(10) 하나로 앞과 같다.
- 다시 뭉치지 않았다.

**[제안] 나누는 길 (판정 전, 구현하지 않음).**
1. 9개 기준을 "안쪽 진술"과 "밖에서 온 진술"로 따로 센다. external은 지도의 한 열에 서서 안쪽 구조를 가리지 않는다.
2. 화면에서 같은 절의 external을 접는 틀(예: "§3에서 온 진술 3개")로 묶는다. 펼치면 node가 그대로 나온다. 자료는 지금처럼 node 하나당 하나로 둔다.
3. s_comparison(external 13)은 받는 진술마다 쓰는 external이 갈린다. 그래서 안쪽 진술을 원문 단계(부호화 → 집중 → 비교)로 하위 graph 한 층 더 나누면 장마다 external 수도 함께 준다. 원문 구조로 자르는 규칙과 맞는지는 판정이 필요하다.

**건드리지 않은 것.** 번호 없는 진술 셋, 순환 검사 단위, 바닥 목록은 그대로다. 커밋하지 않았다.
