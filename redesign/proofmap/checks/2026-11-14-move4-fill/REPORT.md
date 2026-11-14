# 수 4 남은 부분 채우기 — 첫 차례 (2026-11-14)

graph 셋(`top`, `p7`, `diff`)을 하위 모델 셋에 하나씩 맡겨 초안을 받고, 통합 담당(Claude Fable 5.2)이 합쳤다. `diff`·`p7`은 Claude Opus, `top`은 Claude Sonnet이 썼다.

## 파일

- `move4.before.json` — 합치기 전 원본.
- `drafts/{top,p7,diff}.json`, `drafts/*.notes.md` — 하위 모델의 초안과 대조 기록. 원문 줄 범위, 발견한 문제, 판단을 넘긴 항목이 여기 있다.
- `merge.py` — 원본에 초안을 끼우고 통합 때 더한 것을 적용한다. 다시 돌리면 같은 `graphs/move4.json` 이 나온다.

## 바뀐 것

| graph | 전 | 후 |
|---|---|---|
| `top` | edge 12 (내용 실음 1) | edge 17 (내용 실음 17). O1→R2/R3/R4/F1/F2 정의 edge 5개 추가. R2·R3·F1·F2 `sketch` 명시 |
| `p7` | node 15, edge 15 (내용 실음 0) | node 16, edge 27 (내용 실음 25). 밖 node XF(섭동족) 추가, 문맥 `provides` 제거. 안쪽 9개 모두 `sketch` |
| `diff` | 안쪽 완결 2 | 안쪽 완결 4 (D1, D3 추가), S1은 인용 fact로 `sketch`. edge 9 → 15, 모두 내용 실음 |

통합 때 더한 것:

- `top.O1.outputs.tree_defs` — O1 진술에 빠져 있던 정의 일곱 항목($\operatorname{Leaves}$/$\operatorname{Int}$, $E_{\mathcal T}$, 사영 일관성, 위첨자 $A$, $d_\beta$·$n_\beta$, 밀도, $Y_\beta$)을 `role: "given"` 출력으로 더했다. 통합 담당이 trees.tex 29–39, 79–82, 92–105와 직접 대조했다. O1의 진술은 건드리지 않아 기존 지문은 그대로다.
- `diff-e13`–`e15` — 그 항목을 골라 D1, D3, S1에 주는 정의 edge. 이것으로 D1·D3을 `complete` 로 올렸다. 수신 검토 지문은 통합 담당이 기록했다.
- `D2.produces` 에 `diff-e11` 추가.
- `\beta` 등이 backspace 문자로 깨져 있던 네 곳(`diff-e5`, `diff.S1`, `fresh.fp-sampling`, `fresh.FP_SAMPLE`) 복구.
- `viewer/edge-labels.json` 에 새 edge 23개의 표시 ID와 핵심어.

## 검사

- `check.py`: 오류 0, 경고 11. 전에는 오류 0, 경고 10. 새 경고 하나는 `diff-e11` 이 아래의 묵은 지문 경고를 물려받은 것이다.
- 시험: `test_check` 21개 중 1 실패, `test_output_contracts` 12개 중 2 실패, `test_viewer` 11개 중 3 실패. **이 여섯은 합치기 전에도 똑같이 실패했다.** `test_edge_only` 15, `test_local_growth` 5, 경로 회귀는 통과.
- 화면은 열어 보지 않았다. KaTeX 렌더링도 확인하지 않았다.

## 이 차례 전부터 있던 문제

`diff.D2.outputs.kernel_form`, `fv.TM`, `fv.PM` 의 `proof_review` 지문이 현재 증명 자료와 맞지 않는다(edge 전용 PoC 뒤 갱신되지 않은 것으로 보인다 — 추론). 그래서 경고 10개와 시험 실패 6개가 나오고, 보기는 `fv`·`cp`·`fresh`·`diff` 의 모든 vertex를 "재검토 필요"로 미완결 표시한다. D1·D3도 선언은 `complete` 지만 화면에서는 이 때문에 미완결로 보인다. 지문 갱신은 그 대응을 다시 검토했다는 기록이라 이번에 하지 않았다.

## 원문이 보증하지 않는 것

- `diff` D1 식 3·5, D3 식 3·4 (`author_filled`): 원문은 미분 가능성과 교환을 trees.tex 156–176의 해석적 경계로 정당화한다. 초안은 실수 근방의 균일 경계와 유계 수렴으로 갔다.
- `p7` T2·T4·T5: 평균과 미분의 교환을 원문이 말로 적지 않는다. note와 `review.open` 에 표시.
- `p7-e3`(Palm), `p7-e11`(polarization): 원문은 이름과 적용한 식만 준다. 일반형은 초안 작성자가 적었으므로 `complete: false`.

## 알려진 어긋남 2번의 판정 (p7)

(a) 단계 1의 한계는 단계 3으로 — 맞음, 반영. (b) 단계 2 → 단계 4 edge — **원문과 다름, 반영하지 않음.** 단계 4(perturbations.tex 474–492)는 단계 2의 결과를 쓰지 않고, 혼합 전개는 단계 5(526–529)에서 쓴다. `p7-e12` 를 XC→T4에서 XC→T5로 옮겼다. `drafts` 의 O2는 원문과 다른 재구성이다. (c) 맞음, 반영. (d) 맞음, 표시.

## 남은 것

1. 보내는 node가 없는 내용: 복소 재귀와 해석적 경계(trees.tex 156–176), telescoping 항등식(204–208), regular-shapes lemma(458–525). R2의 첫 걸음이 쓰는 첫 변분은 R1의 출력이 아니다.
2. `top` 의 새 정의 edge(e13–e17)와 `p7`/`diff` 의 평문 정의 edge는 O1 본문 진술보다 많이 싣는 곳이 있다. `tree_defs` 참조로 바꾸는 일은 `diff` 에서만 했다.
3. node 진술 보충: R3(같은 방향 계수 $/k!$, $c_E$ 의 의존), XFAM(원문 26–71), XP5($e_{\nu,N}$, $D_\nu$), R4($R_E$, $f$), R1의 conditions(균등 양성).
4. 하위 graph: `top` 의 R2, R3, F1, F2와 `p7` 의 T0–T5. p7 초안의 제안 순서는 T2, T5, T3.
5. `F` 기호가 `fv` 에서는 $\mathscr F_d$, `fresh`·`diff` 에서는 protected $F$ 다.
6. 독립 검토와 사용자 확인은 없다. 모든 근거는 `proposed` 다.
