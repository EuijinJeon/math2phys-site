---
id: main:theorem
kind: theorem
title: '주정리: $\lim_NF_N=\inf_{r\ge0}\Phi_r$'
uses: [x:model-hypotheses, model:integrability, model:positivity, model:hamiltonian, model:functional, x:model-depth-zero, upper:bound, comp:bounded-lower, reduction:stability]
provides: '논문의 결론. models:spin, models:sat(consequences.tex 19, 47: main:formula를 만족), models:ground(consequences.tex 112), L0, L1 마지막 수'
math: |
  (2.1)–(2.4) 아래 열역학 극한이 존재하고
  $$\lim_{N\to\infty}F_N=\inf_{r\ge0}\Phi_r.\tag{2.13}$$
  여기서 $\Phi_r=\inf_{\zeta,\mathbf m}\mathcal B_r(\zeta,\mathbf m)$ ($r\ge1$), $\Phi_0=\inf_\zeta\mathcal B_0(\zeta)$ 이다.
physics: |
  Poisson [[g:hypergraph|hypergraph]] 위의 짝수 $p$체 Ising spin glass에서 quenched [[g:pressure|pressure]] $F_N$($=-\beta f$)의 열역학 극한이 존재하고, 모든 유한 [[g:rsb-steps|RSB 단계 수]]의 Mézard–Parisi free entropy 시행값([[g:functional]])의 inf([[g:phi]])와 같다.
gap: |
  (1) 물리의 "정류점에서 평가한다"가 아니라 inf다. inf의 달성, 최적 order parameter, $r\to\infty$ 의 극한 order parameter, 극한 무한 깊이 Gibbs 측도는 주장하지 않는다(x:model-theorem-scope). (2) [[g:physical-pure-state|물리적 pure state]]들의 계층 구조는 가정하지도 증명하지도 않는다. (3) [[g:hypotheses|가정]]은 (2.1)–(2.4)이고 짝수 $p$ 를 포함한다. (4) 물리 유도가 흔히 쓰는 $\lim F_N=\lim\Delta_N$ 은 가정하지 않는다. 극한의 존재는 $\limsup F_N\le\inf_r\Phi_r\le\liminf F_N$ 에서 나온다(main:theorem.s4).
abstraction: exact
children: [main:theorem.s1, main:theorem.s2, main:theorem.s3, main:theorem.s4]
source:
  - {file: model.tex, lines: [130, 136]}
  - {file: reduction.tex, lines: [45, 87]}
status: proposed
---

**증명의 뼈대 (reduction.tex 45–87).** 하한은 bounded이고 [[g:permutation-invariance|순열 불변]]인 상호작용에서만 증명되어 있다([[comp:bounded-lower]]). 원래 $\theta$ 는 승수 $a$ 때문에 순열 불변이 아닐 수 있고 bounded도 아니다. 그래서:

1. [[main:theorem.s1]] [[g:constant-shift|상수 이동]] $\widehat\theta=\theta-\theta(1,\ldots,1)$ 로 $a$ 를 없애 순열 불변으로 만든다.
2. [[main:theorem.s2]] $\widehat\theta$ 와 $h$ 를 $[-K,K]$ 로 [[g:truncation|자르고]], 잘린 모형에 bounded 하한을 적용한다.
3. [[main:theorem.s3]] [[g:stability|$L^1$ 안정성]]으로 $K\to\infty$ 를 보내 $\liminf_NF_N\ge\inf_r\Phi_r$ 를 얻는다.
4. [[main:theorem.s4]] 상한 [[upper:bound]] $\limsup_NF_N\le\inf_r\Phi_r$ 와 합친다.

증명 단계 카드의 원문은 reduction.tex에 있다. 이 카드 묶음(§2)에서 함께 썼으므로, §9(reduction) 카드를 쓸 때 겹쳐 쓰지 않도록 조율이 필요하다.
