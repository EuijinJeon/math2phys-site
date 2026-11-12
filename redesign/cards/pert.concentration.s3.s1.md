---
id: pert:concentration.s3.s1
kind: step
title: '$G=X_0+2nu^2$ 의 볼록성과 두 추정의 진술'
uses: [pert:concentration.s2.s1, pert:concentration.s1]
provides: 'pert:concentration.s3.s2–s3.s3 (첫 추정의 증명), s4.s1 (볼록성과 (6.11))'
math: |
  남은 일은 $X_0'$ 을 root에 대해 집중시키는 것이다. (6.8)에 의해 무작위 함수
  $$G(u)=X_0(u)+2nu^2$$
  는 $J_\nu$ 에서 볼록이다. $u\in J_\nu$ 와 다른 모든 매개변수에 균등하게
  $$\operatorname{Var}(G(u))\le C_\nu N,\qquad|\mathbb E_{\mathbf u}G'(u)|\le C_\nu\lambda_\nu.$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [163, 175]}
status: proposed
---

$G''=X_0''+4n\ge m_1\operatorname{Var}(D_\nu\mid\mathscr F_0)\ge0$ ([[pert:concentration.s2.s1]], 작성자 풀이). 이 카드는 진술만 담고, 첫 추정의 증명은 s3.s2–s3.s3, 둘째 추정은 s3.s3 끝(perturbations.tex 207–209)에 있다.
