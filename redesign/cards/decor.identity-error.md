---
id: decor:identity-error
kind: definition
title: '항등식 오차의 최대 $\varepsilon_{N,L,k}$'
uses: [pert:tree-identity, x:decor-limit-order, x:decor-topology, decor:average-definition]
provides: 'conditional-concentration.s6, s7.s4에서 J로 나눈 항등식 오차를 고정 L에서 지운다. decor:order-of-limits'
math: |
  고정된 $L,k$에 대해, 아래에서 쓰는 pert:tree-identity의 사례들(leaf 수가 $k$에만 의존하는 상한 이하인 labeled topology와 그 $\{0,\ldots,L-1\}$-깊이 배정으로 만든 old tree, anchor, 제약, 차수가 유계인 multioverlap 단항식 $f$, 유계 개수의 added color)은 유한 개다. 그 사례들에 대한 pert:tree-identity-eq 좌변의 절댓값의 최대를 $\varepsilon_{N,L,k}$라 하면, x:decor-limit-order의 수열을 따라 각 고정 $L,k$에서
  $$\varepsilon_{N,L,k}\longrightarrow0\qquad(N\to\infty).$$
  이 오차에 곱하는 상수는 $L$에 임의로 의존해도 된다.
  같은 유한성 때문에, 고정 $L$에서 깊이 평균 $\mathcal A_{L,\eta}$는 유한 개 배정에 대한 합이다. 따라서 음이 아닌 $z_N(\mathbf q)$에 대해 $\limsup_N\mathcal A_{L,\eta}z_N\le\mathcal A_{L,\eta}\limsup_Nz_N$이고, 특히 각 고정 배정에서 $o_N(1)$인 항(예: $C_{L,k,\eta}\varepsilon_{N,L,k}$, 고정 배정마다의 $\operatorname{Var}(M)$)은 깊이 평균을 취한 뒤에도 $N\to\infty$에서 사라진다. 이 교환은 깊이 평균이나 $L$ 극한보다 먼저 한다 (tex 49–52, 616–618).
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [49, 58]}
status: proposed
---

유한 개의 수열이 각각 0으로 가면 그 최대도 0으로 간다. `math`의 사례 집합(크기가 $k$에만 의존하는 상한 이하)은 원문의 "any of the finite collections used below"(tex 49–53)보다 넓게 잡은 유한 집합이다. 실제로 쓰이는 사례(leaf $\le2k$, added color $\le2k-1$, $f$는 특정 [[g:multioverlap|overlap]] 단항식)는 모두 그 안에 있으므로 안전한 쪽이다(검토 1에서 확인). 핵심은 $L$을 먼저 고정한다는 것이다. $J^{-1}$처럼 $L$에 따라 커지는 상수가 이 오차에만 붙으므로 $\limsup_N$에서 사라진다([[decor:order-of-limits]]).
