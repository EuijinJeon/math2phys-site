---
id: decor:conditional-concentration.s2.s2
kind: step
title: '기저의 마무리: 세 사본 부등식'
uses: [decor:conditional-concentration.s2.s1, decor:contractions, x:decor-eta-regular, decor:average-definition]
provides: 'decor:conditional-concentration.s2'
math: |
  $\ell=d$이면 경로 1, 2, 3은 $\mathscr F_d$가 주어지면 조건부 독립이고 같은 조건부 법칙을 가지므로 decor:contractions (b)에서 $\mathbb E(X-X_d)^2\ge2v_N(S,d)$. $d/L>\eta$이므로 $c_d=(d+2)\delta\ge\eta$. s2.s1의 다른 항은 음이 아니므로 $v_N(S,d)\le\delta/\eta+o_N(1)$ (고정 $L,d$). 질량 $\le1$인 평균을 취하면 $V_{1,L}(\eta)\le\delta/\eta$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [287, 291]}
status: proposed
---

$X=\sigma^1\cdot\sigma^2$, $X_d=\sigma^1\cdot\sigma^3$이고 세 경로가 깊이 $d$에서 서로 갈라지므로 세 사본 부등식이 바로 적용된다. 다른 $\ell$ 항은 버린다. 이 버림이 가능한 것은 항등식이 음이 아닌 항들의 합으로 정리되었기 때문이다.
