---
id: pert:concentration.s2
kind: step
title: 'path 요동: 2차 미분이 조건부 분산을 누른다'
uses: [pert:concentration.s1, tree:original-tilt, x:tree-path-kernels, x:pert-parameter-measure]
provides: 'pert:concentration.s4.s2 ((6.10)의 path 기여), s3.s1 (G의 볼록성에 (6.8)을 씀)'
math: |
  $X_0(u)$ 를 root 기대값을 취하기 전의 무작위 root log 분배함수, $M_d=\langle D_\nu\mid\mathscr F_d\rangle$ 라 하면
  $$X_0'(u)=\langle D_\nu\rangle,\qquad X_0''(u)=\langle\partial_uD_\nu\rangle+\sum_{d=1}^{L}m_d\langle(M_d-M_{d-1})^2\rangle\ge m_1\operatorname{Var}(D_\nu\mid\mathscr F_0)-4n.$$
  $I_\nu=[a,b]$ 에서 적분하면
  $$\int_a^b\mathbb E_{\mathbf u}\operatorname{Var}(D_\nu\mid\mathscr F_0)\,du\le\frac{4\lambda_\nu(1+b-a)}{m_1},$$
  따라서 구간 평균한 thermal 평균 절대 편차를 $\lambda_\nu$ 로 나눈 것은
  $$\left(\frac{4(1+|I_\nu|)}{m_1|I_\nu|\lambda_\nu}\right)^{1/2}$$
  이하다.
physics: |
  [[g:root]]를 고정하면 [[g:root-logarithm|root logarithm]]의 섭동 세기에 대한 2차 미분은 [[g:score|score]]의 path 분산(깊이별 가중 $m_d\ge m_1$)을 포함한다. 통계역학에서 free energy의 2차 미분이 요동을 주는 관계와 같은 꼴이다. 1차 미분이 score의 평균이라 $O(n)$ 으로 유계이므로, 2차 미분을 구간에서 적분한 것도 $O(\lambda_\nu)$ 이고, 정규화한 path 요동은 구간 평균으로 $O(\lambda_\nu^{-1/2})$ 이다.
gap: |
  $L\ge2$ 이면 2차 미분은 보통의 Gibbs 분산이 아니라 [[g:hierarchy|보조 계층]]의 깊이별 martingale 차분 분산에 $m_d$ 를 곱한 합이다. 하계에 쓰는 것은 $m_d\ge m_1$ 뿐이고 상수는 $1/m_1$ 에 의존한다($m_d=d/L$ 이면 $L$). 결론은 $u_\nu$ 에 대한 구간 평균에서만 성립하고, 특정 $u$ 에서의 진술이 아니다. 이 부분은 score의 root 요동을 다루지 않는다(s3, s4).
abstraction: approximation
children: [pert:concentration.s2.s1, pert:concentration.s2.s2]
source:
  - {file: perturbations.tex, lines: [120, 161]}
status: proposed
---

**뼈대.** [[pert:concentration.s2.s1]]: backward 한 단계의 미분 공식에서 (6.7), (6.8). [[pert:concentration.s2.s2]]: (6.8)을 $I_\nu$ 에서 적분하고 $|X_0'|\le2n$ 을 써서 (6.9), Cauchy–Schwarz로 (6.10).

"thermal mean absolute deviation"을 $\frac1{|I_\nu|}\int_{I_\nu}\mathbb E_{\mathbf u}\langle|D_\nu-\langle D_\nu\rangle|\rangle\,du$ 로 읽었다($\langle\cdot\rangle=\mathbb E[\cdot\mid\mathscr F_0]$, 원문은 식으로 적지 않는다; 작성자 읽기). 여기서 "thermal"은 root를 고정한 path 요동을 가리키는 원문의 낱말이고, [[pert:error]]에서 root 요동과 대비된다.
