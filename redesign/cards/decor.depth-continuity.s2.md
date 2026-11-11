---
id: decor:depth-continuity.s2
kind: step
title: '갈라짐 하나를 한 칸 늦추는 효과'
uses: [decor:depth-continuity.s1, x:decor-product-difference, x:decor-tree-sampling]
provides: 'decor:depth-continuity.s3'
math: |
  깊이 $q$의 branching vertex가 자식 모양 $T_1,\ldots,T_s$를 갖고 그 나중 깊이들을 고정한다. 그 vertex 아래 spin 곱의 원래 조건부 평균은 $\prod_j\mu_{q,T_j}$ (좌표별)이다. 갈라짐을 $q+1$로 늦추면 같은 깊이-$q$ prefix에서의 조건부 평균은 $\mathbb E[\prod_j\mu_{q+1,T_j}\mid\mathscr F_q]$이다 (자식 평균은 공통 한 걸음 continuation 위에서 계산). 그리고
  $$\mathbb E\Bigl\|\prod_j\mu_{q,T_j}-\mathbb E\Bigl[\prod_j\mu_{q+1,T_j}\Bigm|\mathscr F_q\Bigr]\Bigr\|_N^2\le s\sum_j\mathbb E\|\mu_{q+1,T_j}-\mu_{q,T_j}\|_N^2.$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [178, 193]}
status: proposed
---

갈라지는 순간 자식들은 조건부 독립이므로 평균이 곱으로 분해된다. 갈라짐을 늦추면 자식들이 한 걸음을 공유한 뒤 독립이 된다. martingale 성질 $\mu_{q,T_j}=\mathbb E[\mu_{q+1,T_j}\mid\mathscr F_q]$ 때문에 차이는 $\mathbb E[\prod x_j-\prod y_j\mid\mathscr F_q]$ 꼴이다. 조건부 Jensen으로 제곱을 안으로 넣고 곱 차이 부등식([[x:decor-product-difference]])을 쓰면 된다.
