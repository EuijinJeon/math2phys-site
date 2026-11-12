---
id: pert:score
kind: definition
title: 'perturbation score $D_\nu$ (6.3)'
uses: [pert:factor, tree:original-tilt]
provides: 'pert:error, pert:concentration (X_0′=⟨D_ν⟩), pert:score-identity (anchor path 위의 D_ν^{a_*}), pert:palm.s1'
math: |
  type $\nu$ 하나에 대해, tilted path(그 말단 Gibbs 배치 포함) 위에서
  $$D_\nu=\sum_{q=1}^{n_\nu}\frac{g_{0,q}S_{0,q}}{1+t_\nu g_q\sigma_{i_q}+u_\nu g_{0,q}S_{0,q}}$$
  로 정의한다.
physics: |
  [[g:score|perturbation score]] $D_\nu$ 는 type $\nu$ [[g:perturbation|섭동]] 인자들의 곱 $\prod_q\psi_{\nu,q}$ 의 $\log$ 를 섭동 세기 $u_\nu$ 로 미분한 것이 path 위에서 갖는 값, 곧 $u_\nu$ 에 짝지어진 섭동 항의 path 값이다.
gap: |
  미분의 정체는 작성자 계산이다($\partial_u\log\psi_{\nu,q}=g_{0,q}S_{0,q}/\psi_{\nu,q}$). root logarithm의 $u_\nu$ 미분이 $\langle D_\nu\rangle$ 이라는 것은 pert:concentration.s2.s1에서 증명된다. $L\ge2$ 에서 그 [[g:root-logarithm|root logarithm]]은 보통 뜻의 free entropy가 아니고 $\langle\cdot\rangle$ 도 보통 Gibbs 평균이 아니다([[g:hierarchy]]).
abstraction: exact
children: []
source:
  - {file: perturbations.tex, lines: [75, 82]}
status: proposed
---

$q$ 는 type-$\nu$ 항의 번호이고 $g_q,g_{0,q},S_{0,q},i_q$ 는 $q$ 번째 항의 mark 함수값, $S_0$ 값, site다(첨자의 뜻은 작성자 풀이). mark 함수값은 그 path가 지나는 vertex의 부호에서 계산되므로 $D_\nu$ 는 path 함수다. [[g:root]] 변수(개수 $n_\nu$, site)와 path 변수(mark, 말단 spin)에 함께 의존한다.
