---
id: x:decor-product-difference
kind: lemma
title: '곱 차이 부등식'
uses: [x:decor-spin-product]
provides: 'depth-continuity.s2, conditional-concentration.s4.s1, overlap-concentration.s3'
math: |
  $x,y\in[-1,1]^s$이면 $\bigl|\prod_jx_j-\prod_jy_j\bigr|\le\sum_j|x_j-y_j|$이고 따라서 $\bigl(\prod_jx_j-\prod_jy_j\bigr)^2\le s\sum_j(x_j-y_j)^2$이다. 좌표별 곱을 취한 벡터 $x_j,y_j\in[-1,1]^N$에 대해서는 $\|\prod_jx_j-\prod_jy_j\|_N^2\le s\sum_j\|x_j-y_j\|_N^2$이다. 또 $x,x',y,y'\in[-1,1]^N$이면 $|x\cdot y-x'\cdot y'|\le\|x-x'\|_N+\|y-y'\|_N$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [186, 187]}
status: proposed
---

원문은 "product difference inequality on $[-1,1]^s$"라고만 쓴다. 증명은 망원 합 $\prod x-\prod y=\sum_r(\prod_{j<r}y_j)(x_r-y_r)(\prod_{j>r}x_j)$와 Cauchy–Schwarz다. 마지막 축약 부등식은 $x\cdot y-x'\cdot y'=(x-x')\cdot y+x'\cdot(y-y')$와 Cauchy–Schwarz에서 나온다. 이 부등식은 작성자가 명시한 것이며, 원문이 같은 단계에서 암묵적으로 쓴다. 검토 1에서 확인되었다: $x\cdot y$가 $N^{-1}$로 정규화되어 있어(tex 91–92) $[-1,1]^N$ 벡터의 $\|\cdot\|_N\le1$이므로 Cauchy–Schwarz가 상수 없이 적용된다. tex 368, 582–583이 이 꼴을 암묵적으로 쓴다.
