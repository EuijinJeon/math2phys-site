---
id: pert:concentration.s2.s1
kind: step
title: 'root logarithm의 미분 공식 (6.7), (6.8)'
uses: [pert:concentration.s1, pert:score, tree:original-tilt, x:tree-path-kernels]
provides: 'pert:concentration.s2.s2 (6.8의 적분), s3.s1 (G의 볼록성, 6.8), s4.s2 (X_0′=⟨D⟩)'
math: |
  $X_0(u)$ 를 root 기대값을 취하기 전의 무작위 root log 분배함수라 하자. 마지막 단계도 미분에 넣기 위해 spin weight의 로그를 $X_L$ 로, spin 분배함수를 지수 $m_L=1$ 의 단계로 본다. backward 한 단계를 미분하면
  $$\partial_uX_{d-1}=K_d(\partial_uX_d),\qquad\partial_u^2X_{d-1}=K_d(\partial_u^2X_d)+m_d\operatorname{Var}_{K_d}(\partial_uX_d).$$
  따라서 $M_d=\langle D_\nu\mid\mathscr F_d\rangle$ 에 대해
  $$X_0'(u)=\langle D_\nu\rangle,\qquad X_0''(u)=\langle\partial_uD_\nu\rangle+\sum_{d=1}^{L}m_d\langle(M_d-M_{d-1})^2\rangle\ge m_1\operatorname{Var}(D_\nu\mid\mathscr F_0)-4n.$$
  조건부 기대값과 분산은 현재 $u$ 의 tilted path 법칙을 쓴다. root를 고정하면 모든 도함수는 유계 score와 그 도함수로 정당화되고, 유한 recursion이 위 미분 공식을 정당화한다. 그 root 기대값은 Poisson 개수의 유한 moment로 정당화된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [120, 145]}
status: proposed
---

풀이(작성자). backward 단계는 [[tree:original-tilt]]의 $X_{d-1}=m_d^{-1}\log P_de^{m_dX_d}$ 이고 tilted kernel이 $K_d=e^{m_d(X_d-X_{d-1})}P_d$ 이므로 한 번 미분하면 $K_d$-평균, 두 번 미분하면 $K_d$-분산에 $m_d$ 가 붙는다. 마지막 단계 $m_L=1$ 에서 $X_L$ 은 spin weight의 로그이고 $K_L$ 은 Gibbs kernel이다. spin weight에서 $u=u_\nu$ 에 의존하는 것은 type-$\nu$ 인자뿐이므로 $\partial_uX_L=D_\nu$, $\partial_u^2X_L=\partial_uD_\nu$. 위로 올라가면 $\partial_uX_d=M_d$ 이고 $\partial_u^2X_0$ 은 각 깊이의 $m_d\operatorname{Var}_{K_d}(M_d)=m_d\langle(M_d-M_{d-1})^2\mid\mathscr F_{d-1}\rangle$ 의 합이다. 부등식은 $m_d\ge m_1$, martingale 차분의 직교성 $\sum_d\langle(M_d-M_{d-1})^2\rangle=\operatorname{Var}(D_\nu\mid\mathscr F_0)$($M_L=D_\nu$, $M_0=\langle D_\nu\rangle$), 그리고 [[pert:concentration.s1]]의 $\partial_uD_\nu\ge-4n$ 에서 온다. $\mathscr F_d$ 는 [[x:tree-path-kernels]]의 prefix $\sigma$-field다.

$L=1$(보조 계층 없음)이면 $X_0''=\langle\partial_uD\rangle+\operatorname{Var}(D)$ 로 보통의 "2차 미분 = 분산" 관계가 된다.
