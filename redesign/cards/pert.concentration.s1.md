---
id: pert:concentration.s1
kind: step
title: 'type 하나 고정, 구간 $J_\nu$ 와 score 경계 (6.6)'
uses: [pert:score, pert:parameters, pert:factor]
provides: 'pert:concentration.s2.s1 (∂_uD ≥ −4n), s2.s2 (|X_0′| ≤ 2n), s3.s1 (G의 볼록성), s3.s3 (도함수 경계)'
math: |
  다른 매개변수를 고정하고 $u=u_\nu$, $n=n_\nu$, $\lambda_\nu=c_\nu s_N$ 으로 쓴다. $I_\nu$ 를 품는 열린 구간 $J_\nu$ 를 그 폐포 전체에서 $|t_\nu|+|u|<1/2$ 가 되도록 고른다. 이 구간에서 path마다
  $$|D_\nu|\le2n,\qquad -4n\le\partial_uD_\nu=-\sum_{q=1}^{n}\frac{(g_{0,q}S_{0,q})^2}{\psi_{\nu,q}^{2}}\le0.$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [106, 118]}
status: proposed
---

$|t_\nu|+|u|<1/2$ 이면 $\psi_{\nu,q}>1/2$ 이고 $|g_{0,q}S_{0,q}|\le1$ 이므로 각 항이 $2$ 이하, 도함수의 각 항이 $4$ 이하다(작성자 계산). $t_\nu\le1/4$, $\max I_\nu=2j^{-j}\le2\cdot4^{-4}$ 이므로 그런 $J_\nu$ 가 있다. $J_\nu$ 가 $I_\nu$ 보다 조금 넓은 것은 [[pert:concentration.s4.s1]]에서 $u\pm\rho$ 의 차분몫을 쓰기 위해서다.
