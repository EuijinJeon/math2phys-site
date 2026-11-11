---
id: decor:contractions.s2
kind: step
title: '세 사본 부등식'
uses: []
provides: 'decor:contractions (b)'
math: |
  $\mu=\mathbb E[X\mid\mathscr G]$라 하면 조건부 독립성에서
  $$\mathbb E[(X\cdot Y-X\cdot Z)^2\mid\mathscr G]=\frac2{N^2}\operatorname{tr}\bigl((C+\mu\mu^{\mathsf T})C\bigr)\ge\frac2{N^2}\operatorname{tr}(C^2),$$
  $C$가 양반정치이므로 $\operatorname{tr}(\mu\mu^{\mathsf T}C)=\mu^{\mathsf T}C\mu\ge0$. 대칭인 $C$에 대해 $\operatorname{tr}(C^2)=\sum_{ij}C_{ij}^2$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [132, 140]}
status: proposed
---

$X\cdot Y-X\cdot Z=X\cdot(Y-Z)$이고 $W=Y-Z$는 조건부 평균 0, 조건부 공분산 $2C$이며 $X$와 조건부 독립이다. 그래서 $\mathbb E[(X\cdot W)^2\mid\mathscr G]=N^{-2}\mathbb E[X^{\mathsf T}(2C)X\mid\mathscr G]=\frac2{N^2}\operatorname{tr}(C\,\mathbb E[XX^{\mathsf T}\mid\mathscr G])$이고, $\mathbb E[XX^{\mathsf T}\mid\mathscr G]=C+\mu\mu^{\mathsf T}$이다.
