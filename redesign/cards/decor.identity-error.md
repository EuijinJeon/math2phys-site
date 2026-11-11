---
id: decor:identity-error
kind: definition
title: '항등식 오차의 최대 $\varepsilon_{N,L,k}$'
uses: [pert:tree-identity, x:decor-limit-order, x:decor-topology]
provides: 'conditional-concentration.s6, s7.s4에서 J로 나눈 항등식 오차를 고정 L에서 지운다. decor:order-of-limits'
math: |
  고정된 $L,k$에 대해, 아래에서 쓰는 pert:tree-identity의 사례들(leaf 수가 $k$에만 의존하는 상한 이하인 labeled topology와 그 $\{0,\ldots,L-1\}$-깊이 배정으로 만든 old tree, anchor, 제약, 차수가 유계인 multioverlap 단항식 $f$, 유계 개수의 added color)은 유한 개다. 그 사례들에 대한 pert:tree-identity-eq 좌변의 절댓값의 최대를 $\varepsilon_{N,L,k}$라 하면, x:decor-limit-order의 수열을 따라 각 고정 $L,k$에서
  $$\varepsilon_{N,L,k}\longrightarrow0\qquad(N\to\infty).$$
  이 오차에 곱하는 상수는 $L$에 임의로 의존해도 된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [49, 58]}
status: proposed
---

유한 개의 수열이 각각 0으로 가면 그 최대도 0으로 간다. 핵심은 $L$을 먼저 고정한다는 것이다. $J^{-1}$처럼 $L$에 따라 커지는 상수가 이 오차에만 붙으므로 $\limsup_N$에서 사라진다([[decor:order-of-limits]]).
