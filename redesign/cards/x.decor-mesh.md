---
id: x:decor-mesh
kind: convention
title: '균등 격자 $m_d=d/L$, $\delta=1/L$'
uses: [pert:selection, cavity:grid]
provides: '§7의 모든 계수 계산 (c_ℓ, J, κ, C(S,e))과 tree:charging의 가정'
math: |
  이 절 전체에서 $L\ge2$이고 (pert:selection, cavity:grid의 "Fix $L\ge2$"; decorrelation.tex 4에는 $L\ge2$가 따로 적혀 있지 않다) tree의 exponent는 균등 격자 $m_d=d/L$ ($0\le d\le L$)이며 $\delta=L^{-1}$로 쓴다. 따라서 unary vertex에서의 fresh 계수는 $m_d-m_{d+1}=-\delta$이다.
physics: |
  [[g:parisi-parameters|Parisi 매개변수]]를 $x$-축에서 간격 $1/L$의 [[g:grid|균등 격자]]로 둔, 깊이 $L$의 계층, 즉 $r=L-1$개 보조 단계의 $(L-1)$단 RSB이다 (cavity.tex 16 "use $r=L-1$ auxiliary levels", trees.tex 23 "$L=r+1$", comparison.tex 162–166의 $\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$). $L\ge2$이고 $L\to\infty$는 계층을 촘촘히 하는 극한이다. unary vertex의 fresh 계수는 $m_d-m_{d+1}=-1/L$이다.
gap: |
  격자는 최적화된 Parisi 매개변수가 아니라 고정된 선택이다. 연속 극한은 §8 이후 $L\to\infty$에서만 취한다. 물리에서의 $q(x)$ 최적화나 정류점 조건은 여기에 없다.
abstraction: exact
children: []
source:
  - {file: decorrelation.tex, lines: [4, 4]}
status: proposed
---

이 절의 모든 작은 계수는 $\delta$의 거듭제곱이다. 정규화 계수 $J$가 $\delta^{2b}$ 정도로 작아도 상대 절댓값 비용이 $L$에 균등하게 유계라는 것([[decor:conditional-concentration.s3.s3]])이 균등 격자에서 계산된다.
