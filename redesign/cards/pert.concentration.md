---
id: pert:concentration
kind: lemma
title: '매개변수 평균한 score 집중 (Lemma 6.1)'
uses: [pert:error, x:pert-parameter-measure, x:pert-standing, pert:score, pert:factor, pert:parameters, tree:original-tilt, x:tree-path-kernels, tree:insertion, x:tree-extra-variables]
provides: 'pert:selection.s2 (Markov 선택; perturbations.tex 282). 규칙 P5, L1 수 3'
math: |
  각 고정 $L$ 과 각 고정 type $\nu$ 에 대해
  $$\int e_{\nu,N}(\mathbf u)\,\pi(d\mathbf u)\longrightarrow0.$$
  이 주장은 원래 계에서와 마찬가지로 reservoir에서도 성립한다. 상수는 $L$ 이나 $\nu$ 에 균등할 필요가 없다.
physics: |
  [[x:pert-standing]]의 유계 모형과 그 [[g:reservoir|reservoir]]에서, 섭동 매개변수를 [[g:perturbation|그 구간]]들 위에서 균일하게 평균하면, 각 type의 [[g:score|score]]는 크기 $N\to\infty$ 에서 [[g:concentration|집중]]한다: 기대 개수로 정규화한 score의 path 요동과 [[g:root]] 요동이 함께 0으로 간다. 근거는 [[g:root-logarithm|root logarithm]]이 $u_\nu$ 의 함수로서 (작은 보정을 더하면) 볼록이고, 그 2차 미분이 score의 path 분산을 포함한다는 것이다.
gap: |
  (1) 매개변수 평균 $\int\cdot\,d\pi$ 의 진술이다. 특정 $\mathbf u$ 에서의 집중을 말하지 않는다. 한 점을 고르는 것은 pert:selection의 일이다. (2) type마다, $L$ 마다의 진술이고 상수는 $1/m_1=L$, $|I_\nu|$, $c_\nu$ 에 의존한다. $L$ 이나 type에 균등하지 않다. (3) 정규화된 평균 절대 편차($L^1$)의 수렴이며 disorder 표본 하나에 대한 거의 확실한 수렴이 아니다. (4) $N\to\infty$ 는 모든 크기를 따른 것이다(아직 [[g:selected-sequence|선택된 수열]]이 없다). (5) $L\ge2$ 의 root logarithm은 보통 뜻의 free entropy가 아니고 path 기대값은 tilt된 [[g:hierarchy|보조 계층]] 위의 것이다.
abstraction: weakening
children: [pert:concentration.s1, pert:concentration.s2, pert:concentration.s3, pert:concentration.s4]
source:
  - {file: perturbations.tex, lines: [95, 104]}
  - {file: perturbations.tex, lines: [106, 244]}
status: proposed
---

**증명의 뼈대.** type 하나를 고정하고 $u=u_\nu$ 만 움직인다($\lambda_\nu=c_\nu s_N$).
- [[pert:concentration.s1]]: $u$ 가 놓이는 열린 구간 $J_\nu$ 에서 path마다 $|D_\nu|\le2n$, $-4n\le\partial_uD_\nu\le0$.
- [[pert:concentration.s2]] (path 요동): root logarithm $X_0$ 의 미분 공식 $X_0'=\langle D_\nu\rangle$, $X_0''\ge m_1\operatorname{Var}(D_\nu\mid\mathscr F_0)-4n$ 을 구간에서 적분하면 구간 평균한 path 평균 절대 편차가 $O(\lambda_\nu^{1/2})$ 이다.
- [[pert:concentration.s3]] (root 요동의 재료): $G=X_0+2nu^2$ 는 볼록이고 $\operatorname{Var}G(u)\le C_\nu N$(Efron–Stein과 Poisson 개수), $|\mathbb E_{\mathbf u}G'|\le C_\nu\lambda_\nu$.
- [[pert:concentration.s4]]: 볼록 함수의 차분몫으로 $G'$ 의 요동을 $G$ 의 요동과 평균 도함수의 증가량으로 누르고 $\rho=N^{-1/8}$ 을 고르면, $\lambda_\nu=c_\nu N^{3/4}$ 로 나눈 root 기여가 0으로 간다. 두 기여를 합하고 나머지 매개변수로 적분한다.

핵심은 규모의 차이다: root logarithm의 root 분산은 $O(N)$ 이지만 score는 $\lambda_\nu\sim N^{3/4}$ 규모이므로 $\sqrt N/\rho+\rho\lambda_\nu$ 를 $\lambda_\nu$ 로 나눈 것이 0으로 갈 수 있다. 이것이 $s_N=N^{3/4}$ 를 고른 이유로 읽힌다(작성자 읽기; 원문은 이유를 따로 적지 않는다).

"reservoir에서도"는 [[x:pert-standing]]의 reservoir 구조(평균 $O(N)$ 의 독립 Poisson 상호작용, $N$ 개 독립 유계 장)가 s3.s3의 "root 변수 개수가 $O(N)$"을 그대로 주기 때문이다.
