---
id: decor:contractions.s1
kind: step
title: '축약 부등식'
uses: [decor:covariance-definition]
provides: 'decor:contractions (a)'
math: |
  $C=\operatorname{Cov}(A_S\mid\mathscr F_d)$라 하면, $B$의 조건부 독립성에서 $\mathbb E\bigl[((A_S-\mu_{d,S})\cdot B)^2\mid\mathscr F_d,B\bigr]=N^{-2}\sum_{ij}C_{ij}B_iB_j\le N^{-2}\sum_{ij}|C_{ij}|\le\bigl(N^{-2}\sum_{ij}C_{ij}^2\bigr)^{1/2}$. 기대값을 취하고 Jensen을 쓰면 $\mathbb E((A_S-\mu_{d,S})\cdot B)^2\le v_N(S,d)^{1/2}$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [127, 131]}
status: proposed
---

$B$가 $A_S$와 조건부 독립이므로 $B$를 상수처럼 다룰 수 있다. Cauchy–Schwarz는 두 번 쓰인다: $N^2$개 항에 대해 한 번, [[g:state|prefix]]에 대한 기대값에 대해 $\mathbb E\sqrt{\cdot}\le\sqrt{\mathbb E\cdot}$로 한 번. 그래서 지수가 $1/4$로 떨어진다.
