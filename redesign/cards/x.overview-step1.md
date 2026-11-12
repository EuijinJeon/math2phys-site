---
id: x:overview-step1
kind: remark
title: '전략 1단계: cavity reservoir 고르기'
uses: [model:hamiltonian, model:power-means]
provides: 'x:overview-strategy. L1 수 2, 3'
math: |
  reservoir는 크기 $N$ 과 $N+1$ 의 계를 비교하는 데 쓰는 공통 $N$-spin Gibbs 계다. 유계 상호작용 법칙과 장 법칙에 대해, 개수가 계 크기에 대해 sublinear인 유계 Poisson 섭동을 더한다. 그 효과는 pressure에서 사라진다. 각 고정 계층 깊이에서, 보조 power-mean 재귀 뒤의 연속한 기대 로그의 차가 원래 pressure liminf를 임의로 작은 오차보다 더 넘지 않게 하는 계 크기와 결정적 섭동 매개변수를 고른다. 같은 선택이 모든 perturbation score의 집중을 준다.
physics: |
  [[g:bounded-law|유계]] 상호작용·장에서, 크기 $N$ 과 $N+1$ 을 공통 [[g:reservoir|reservoir]]로 비교한다. sublinear 개수의 유계 [[g:perturbation|섭동]]은 밀도를 바꾸지 않는다. 깊이 $L$ 을 고정할 때마다 크기와 섭동 매개변수를 골라, [[g:power-mean|power mean]] 재귀 뒤의 [[g:increment|증분]]이 [[g:lower-pressure|$\underline F$]]를 거의 넘지 않고 모든 [[g:score|score]]가 [[g:concentration|집중]]하게 한다. 이것이 [[g:selected-sequence|선택된 수열]]이다.
gap: |
  (1) "pressure에서 사라진다"의 정확한 대상은 섭동된 계의 pressure가 아니라 power-mean 재귀 뒤의 [[g:root-logarithm|root logarithm]] 기대값이고, 진술은 $\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)s_N$ 이다(cavity:negligible). (2) "임의로 작은 오차"는 pert:selection (i)의 $\Delta_{N_j}\le\underline F+2\varepsilon$ 이다. 상한뿐이고 증분의 극한은 말하지 않는다. (3) 선택은 $L$ 과 $\varepsilon$ 마다 다르다. score 집중은 type마다이고 균등하지 않다(pert:selection (ii)). (4) pert:selection (iii)(유한 tree moment의 수렴)은 이 문단에 없다. (5) 원문 문단은 [[g:permutation-invariance|순열 불변성]]을 여기서 말하지 않는다. 하한 전체의 가정으로는 x:overview-closing(46–48행)과 x:cavity-bounded에 있다.
abstraction: weakening
children: []
source:
  - {file: overview.tex, lines: [8, 18]}
status: proposed
---

8행은 `\begin{enumerate}` 이다.

**가리키는 곳.**

| 문장 | 본문 노드 | overview.tex |
|---|---|---|
| reservoir의 정의 | [[cavity:increment]] (reservoir), [[cavity:section]] | 10–11 |
| 유계 법칙, 유계 Poisson 섭동, sublinear 개수 | [[x:cavity-bounded]], [[cavity:factor-bounds]], [[x:cavity-root-convention]] ($s_N=N^{3/4}$) | 12–13 |
| 효과가 사라진다 | [[cavity:negligible]], [[x:cavity-root-logarithm]] | 13–14 |
| 크기와 결정적 매개변수의 선택, 증분 $\le\underline F+$ 오차 | [[pert:selection]] (i), 증분은 [[cavity:increment]] | 14–17 |
| score 집중 | [[pert:concentration]], [[pert:selection]] (ii) | 17–18 (`\cref{cavity:section,pert:selection}`) |
