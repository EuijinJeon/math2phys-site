---
id: decor:overlap-concentration.s2.s2
kind: step
title: '$C(S,e)\operatorname{Var}(M)=o_N(1)$'
uses: [decor:overlap-concentration.s2.s1, pert:tree-identity, x:decor-tree-sampling]
provides: 'decor:overlap-concentration.s4'
math: |
  target 사본과 old 사본은 $\mathscr F_{e-1}$가 주어지면 조건부 독립이고 같은 조건부 법칙을 가진다. $f=R_S$ (old), $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$이면 old 쪽 각 항은 $\mathbb E[fR_E]=\mathbb EM^2$이다. anchor 혼자인 쪽은 marker의 $e-1$ 아래 continuation을 지우면 보통의 target 법칙 $S$가 남아 평균이 $\mathbb ER_S$이다. 따라서
  $$C(S,e)\bigl(\mathbb EM^2-(\mathbb ER_S)^2\bigr)=C(S,e)\operatorname{Var}(M)=o_N(1),$$
  그리고 고정 $L$에서 $C(S,e)\ne0$으로 나누어 $\operatorname{Var}(M)\to0$ (각 고정 $L,S,e$). $L\to\infty$에서 균등한 하계는 필요 없다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [550, 570]}
status: proposed
---

marker anchor는 spin을 내지 않으므로 $R_E$는 target 사본만의 multioverlap이다. 두 사본이 공통 prefix $\mathscr F_{e-1}$를 갖고 그 아래에서 독립이므로 곱의 기대값이 조건부 평균의 제곱이 된다. $\mathbb EM=\mathbb ER_S$이므로 차이가 정확히 $\operatorname{Var}(M)$이다.
