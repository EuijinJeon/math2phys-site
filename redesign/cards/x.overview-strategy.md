---
id: x:overview-strategy
kind: section
title: '§2.2 증명 전략 (Proof strategy)'
uses: [main:theorem, model:hamiltonian, model:integrability, model:factorization, model:positivity, model:chain, model:power-means, model:functional]
provides: 'layers/L1.md(일곱 수)가 이 소절에 고정되어 있다. 원문에서는 introduction.tex 84–86("The proof strategy following main:theorem explains ...")이 이 소절을 가리킨다'
math: |
  저자가 쓴 증명 전략 요약이다. 증명은 없다.
  상한: interpolation 상한은 모든 계 크기와 모든 유한 깊이에서 성립하고, $\log a$ 의 적분 가능성을 가정하지 않는 정규화를 포함해 다시 증명한다 (x:overview-upper).
  하한 네 단계: (1) cavity reservoir를 고르고, sublinear 유계 Poisson 섭동 아래 증분이 원래 pressure liminf를 거의 넘지 않으며 모든 score가 집중하는 크기와 결정적 매개변수를 고른다 (x:overview-step1). (2) 유한 tree 계산과 독립 mark, score 집중으로 처방된 branching pattern의 부호 있는 합에 대한 항등식을 얻는다 (x:overview-step2). (3) 깊이를 한 단계 늦추는 장치와 상대 계수 한계로, replica 수에 대한 귀납으로 조건부 공분산을 없애고 두 번째 항등식으로 조건부 평균을 집중시킨다 (x:overview-step3). (4) 한 site의 계층을 부호화하고 site label을 독립 사본으로 바꿔 선택된 증분에 가까운 시행값을 얻는다 (x:overview-step4).
  마무리: 3단계의 추정은 깊이 평균이지만 4단계에 충분하다. 하한은 유계·순열 불변 상호작용에서 factorization과 positivity 없이 성립하고, 정규화와 균일 추정으로 1차 moment 가정 아래 main:theorem에 이른다 (x:overview-closing).
physics: |
  상한은 Guerra–Franz–Leone–Panchenko–Talagrand [[g:interpolation|interpolation]]이다. 하한은 cavity 비교다: 섭동된 [[g:reservoir|reservoir]]에서 [[g:selected-sequence|선택된 수열]]을 고르고, [[g:tree-identity|prescribed-tree 항등식]]으로 모든 [[g:multioverlap|multioverlap]]을 [[g:concentration|집중]]시킨 뒤, 이웃 cavity field를 독립 사본으로 바꿔([[g:independent-copies]]) [[g:increment|증분]]을 시행 [[g:functional|functional]] 값과 비교한다. 물리 유도가 [[g:physical-pure-state|물리적 pure state]]들의 계층과 그 안의 독립성을 가정해 건너뛰는 단계를, 논문은 그 가정 없이 섭동으로 만든 [[g:hierarchy|보조 계층]] 위의 항등식으로 대신한다.
gap: |
  (1) 이 소절은 요약이고, 각 문장의 정확한 진술은 가리키는 본문 노드에 있다(아래 표와 자식 카드의 표). (2) 물리 문장의 마지막 문장(물리적 pure state 계층을 보조 계층으로 대신한다)은 이 소절이 아니라 introduction.tex 75–77("Their branching is part of the construction; no ultrametric organization of the physical Gibbs states is assumed")에 근거한다. 논문은 보조 계층과 물리적 pure state의 관계를 증명하지 않는다. (3) "상한은 Guerra–Franz–Leone–Panchenko–Talagrand"라는 계보는 upper.tex 3–6과 introduction.tex 17–22에 있고 이 소절에는 없다. (4) 모든 하한 진술의 극한 순서는 고정 $L$ 에서 $N\to\infty$, 그다음 $L\to\infty$ 다(x:overview-closing, introduction.tex 83–84).
abstraction: approximation
children: [x:overview-upper, x:overview-step1, x:overview-step2, x:overview-step3, x:overview-step4, x:overview-closing]
source:
  - {file: overview.tex, lines: [1, 51]}
status: proposed
---

**위치.** 원문 번호로는 §2의 소절 2.2이다(graph.json의 `x:overview-L1`, 부모 `model:section`). [[model:section]] 카드는 검토 2 반영에서 이 카드를 마지막 자식으로 두고 `source` 에 overview.tex 1–51을 더했다. 이 소절은 정리류 환경이 없어 포함 검사가 요구하는 줄은 0줄이다.

**예고와 의존.** 이 소절의 `\cref` 가운데 [[main:theorem]](50행)을 뺀 모두(upper, cavity, pert, tree, decor, comp, reduction)는 원문상 뒤의 대상을 가리키는 예고다. 그래서 `uses` 에 넣지 않고 자식 카드의 "가리키는 곳" 표로 잇는다. `uses` 에는 문장이 기대는 §2의 정의와, 결론으로 이름을 부르는 [[main:theorem]]만 넣었다.

**overview 문장 ↔ L1 수.**

| overview 문장 (행) | 카드 | L1 수 | 대응 |
|---|---|---|---|
| U1 상한은 모든 크기·모든 유한 깊이 (3–4) | [[x:overview-upper]] | 1 | 맞음 ("모든 $N$ 과 모든 시행값에서 $F_N\le\mathcal B_r$") |
| U2 $\log a$ 적분 가능성 없는 정규화 (4–6) | [[x:overview-upper]] | 1 | 맞음. 처음에는 L1이 빠뜨렸고(P2 차이 칸에만 있었다) 검토 2 반영에서 수 1 끝에 한 구절과 [[upper:regularization]]을 넣었다 |
| U3 하한은 네 단계 (6) | — | 2–6 | 구조 차이: 1단계 → 수 2+3, 2단계 → 수 4, 3단계 → 수 5, 4단계 → 수 6 |
| 1b reservoir의 정의 (10–11) | [[x:overview-step1]] | 2 (와 기호 줄) | 맞음 |
| 1c 유계 법칙, sublinear 유계 Poisson 섭동 (12–13) | [[x:overview-step1]] | 2 | 맞음. L1이 더 구체적($N^{3/4}$, $[1/2,3/2]$; cavity:factor-bounds와 맞음) |
| 1d 효과가 pressure에서 사라짐 (13–14) | [[x:overview-step1]] | 2 | 맞음. L1이 대상을 더 정확히 적는다(root logarithm $P_N^{L,\mathbf u}$) |
| 1e 크기와 결정적 매개변수 선택, 증분 $\le$ liminf $+$ 오차 (14–17) | [[x:overview-step1]] | 3 | 맞음 ($\Delta_{N_j}\le\underline F+2\varepsilon$) |
| 1f 같은 선택이 score 집중 (17–18) | [[x:overview-step1]] | 3 | 맞음. **L1이 더 말함**: 유한 tree moment 수렴(pert:selection (iii))은 overview에 없다. 본문에는 있다 |
| (없음) 증분 항등식 $\Delta_N=\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}+o(1)$ | — | 2 | **L1이 더 말함.** overview는 증분을 정의로만 쓰고(14–16) 이 식을 적지 않는다. 본문 cavity:increment에 있다 |
| 2b tree 계산이 insertion을 부호 있는 합으로 전개 (21–22) | [[x:overview-step2]] | 4 | 맞음 |
| 2c 독립 mark가 임의의 처방된 pattern을 고름 (22–23) | [[x:overview-step2]] | 4 | 맞음. L1은 "mark가 anchor와 새 replica들로 이루어진 집합 안의 쌍별 split 깊이(새 replica끼리 포함)를 지정한다"로 범위를 적는다. 본문(perturbations.tex 433–436)과 맞는 쪽은 L1이고, overview의 "any"는 범위(일관성, 다른 old replica가 관여하는 쌍은 지정하지 못함, mark 깊이 $1,\ldots,L-1$)를 적지 않은 요약이다 |
| 2d score 집중에서 항등식 (23–24) | [[x:overview-step2]] | 4 | 맞음. L1은 수 5–6이 factorization을 쓰지 않는다는 것도 적는다(overview는 46–48행에서) |
| 3b 내부 branching 깊이를 한 단계 늦춤 (27) | [[x:overview-step3]] | 5 | 맞음. 처음에는 수 5 본문이 빠뜨렸고(마지막 문단의 "깊이 미루기", $-\delta$ 대 $2+\delta$ 에만 있었다) 검토 2 반영에서 수 5 첫 문장에 넣었다 |
| 3c 첫 fresh split이 정규화 계수와 같은 작은 인자 (28–29) | [[x:overview-step3]] | 5 | 맞음. 검토 2 반영에서 수 5에 넣었다("정규화 계수와 같은 작은 인자 $\delta=1/L$") |
| 3d 절대 계수 합의 상대 한계 (29–30) | [[x:overview-step3]] | 4–5 | 맞음. 수 5가 "절댓값 계수 합의 상대 한계"와 [[tree:charging]]을 적는다(수 4의 "계수 한계(P6)"는 그대로) |
| 3e replica 수 귀납으로 조건부 공분산 감쇠 (30–31) | [[x:overview-step3]] | 5 | 맞음 ("잎 개수 귀납", 조건부 decorrelation) |
| 3f 두 번째 항등식이 남은 조건부 평균을 집중 (32–33) | [[x:overview-step3]] | 5 | 맞음. 검토 2 반영에서 수 5에 "marker anchor를 쓴 두 번째 항등식으로 남은 조건부 평균을 각 고정 깊이에서 집중"을 넣었다(P9 차이 칸에도 있다) |
| 4b 한 site의 계층을 조건부 법칙으로 부호화 (36–37) | [[x:overview-step4]] | 6 | 맞음 |
| 4c site label을 독립 사본으로 (37–39) | [[x:overview-step4]] | 6 | 맞음 |
| 4d 선택된 증분에 가까운 시행값 (39–40) | [[x:overview-step4]] | 6 | 맞음. L1이 더 구체적(부등식 사슬, $\limsup_N$, $L\to\infty$, $\varepsilon\downarrow0$; comp:bounded-lower와 맞음) |
| C1 3단계 추정은 떨어진 내부 깊이의 평균 (43–44) | [[x:overview-closing]] | 5 | 맞음 ($\mathcal A_{L,\eta}$) |
| C2 예외적 tree의 확률이 사라져 평균으로 충분 (44–45) | [[x:overview-closing]] | 6 | 맞음 ("수 5의 깊이 평균은 $Q_k$ 평균으로 충분"). 예외적 tree의 확률은 P11 차이 칸에 있다 |
| C3 깊이에 균일한 집중은 필요 없음 (45–46) | [[x:overview-closing]] | 5–6, 마지막 문단 | 맞음. "the depth"를 branching 깊이로 읽으면 L1의 "고정 깊이가 아니라 깊이 평균으로만", 계층 깊이 $L$ 로 읽으면 "$N\to\infty$ 다음 $L\to\infty$ 의 순서로만"(L1 마지막 문단)과 맞는다. 두 읽기는 [[x:overview-closing]] 차이 칸 (5) |
| C4 bounded·순열 불변 하한, factorization·positivity 없이 (46–48) | [[x:overview-closing]] | 2 머리, 4 | 맞음 |
| C5 정규화와 균일 추정으로 유계성 제거, 주정리 (48–51) | [[x:overview-closing]] | 7 | 맞음. **L1이 더 말함**: 상수 이동이 factorization과 $b$ 의 독립으로 순열 불변성을 만든다는 것, 상한과의 맞붙임. 본문(reduction.tex 45–59, 85–87)과 맞다 |
| (없음) $\eta\to0$ 은 $L\to\infty$ 뒤 | — | 6 | **L1이 더 말함.** 본문 comp:shape-error와 맞다 |
| (없음) "수학이 물리보다 더 해야 했던 일" 문단 | — | 마지막 문단 | overview에 없는 L1의 해설. 근거는 introduction.tex 75–84 |

L1이 overview와 어긋나 틀린 곳은 찾지 못했다. 어긋남은 "L1이 본문을 따라 더 말함" 또는 "L1이 overview의 기술적 세부를 빠뜨림"이었다. 빠뜨린 세 가지(상한의 $\log a$ 정규화, 깊이 미루기와 그 작은 인자, 두 번째 marker anchor 항등식)는 검토 2 반영(`build/review-2-cons-overview-response.md`)에서 `layers/L1.md` 수 1과 수 5에 한 구절씩 넣었다.
