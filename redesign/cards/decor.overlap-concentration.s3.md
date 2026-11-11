---
id: decor:overlap-concentration.s3
kind: step
title: 'prefix 아래의 조건부 분산: $G$와 $G_-$'
uses: [decor:projection-bound, decor:projection-definition, decor:depth-continuity, decor:depth-continuity.s1, x:decor-product-difference, decor:average-definition]
provides: 'decor:overlap-concentration.s4'
math: |
  $|S|=k\ge2$, 첫 갈라짐 $e$, 자식 $T_1,\ldots,T_s$에 대해 $G=\mathbf1\cdot\prod_j\mu_{e,T_j}$, $G_-=\mathbf1\cdot\prod_j\mu_{e-1,T_j}$로 둔다. $G_-$는 $\mathscr F_{e-1}$-가측이고, decor:projection-bound ($B=\mathbf1$)에서 $\mathbb E(R_S-G)^2\le p_N(S,e)^2$이다. 자식 깊이를 고정하고 곱 차이 부등식과 martingale energy를 쓰면 $L$이 클 때
  $$\mathcal A_{L,\eta}\,\mathbb E(G-G_-)^2\le C_k/L.$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [571, 590]}
status: proposed
---

자식 공분산은 깊이 $e$에서 평가한다. $e$는 자식들의 모든 branching depth와 $\eta L$ 넘게 떨어져 있어서 $V$의 정의에 맞는다. $e$에서 $e-1$로 옮기는 것은 공분산 추정 대신 martingale 연속성으로 한다. $(\mathbf1\cdot x)^2\le\|x\|_N^2$, 곱 차이 부등식, 그리고 $e$ 자체가 평균하는 좌표이므로 한 걸음 증분을 $e$에 대해 합한 뒤 $L$로 나눈다(depth-continuity.s1의 martingale energy, 또는 depth-continuity의 평가 깊이 부등식을 각 $T_j$에 적용).
