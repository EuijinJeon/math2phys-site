---
id: decor:depth-continuity.s1
kind: step
title: 'martingale energy와 평가 깊이 연속성'
uses: [decor:covariance-definition, decor:average-definition]
provides: 'depth-continuity의 둘째 부등식 (evaluation-depth-continuity). s3의 q에 대한 합. overlap-concentration.s3의 (adjacent-prefix-error)'
math: |
  모양 $T$의 나중 branching depth를 고정하고 initial stem을 따라 한 경로를 뽑으면 $t\mapsto\mu_{t,T}$는 그 stem의 prefix filtration $(\mathscr F_t)$에 대한 vector martingale이고 좌표가 $[-1,1]$에 있다. 증분의 직교성에서
  $$\sum_t\mathbb E\|\mu_{t+1,T}-\mu_{t,T}\|_N^2\le1$$
  (합은 initial stem 위의 $t,t+1$에 대해). 이것을 범위를 갖는 $d$에 대해 합하고 정규화 $L^{-1}$을 곱하면, 나머지 좌표의 합은 $L$의 거듭제곱으로 상쇄되어 $\mathcal A_{L,\eta}\mathbb E\|\mu_{d+1,S}-\mu_{d,S}\|_N^2\le1/L$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [168, 177]}
status: proposed
---

직교 증분에서 $\sum_t\mathbb E\|\mu_{t+1}-\mu_t\|_N^2=\mathbb E\|\mu_{\rm last}\|_N^2-\mathbb E\|\mu_{\rm first}\|_N^2\le1$이다. 핵심은 이 합이 깊이 수 $L$과 무관하게 1로 유계라는 것이다. 따라서 깊이에 대해 평균하면 $1/L$이 된다. 개별 깊이에서는 증분이 클 수 있다.
