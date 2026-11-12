---
id: pert:concentration.s3
kind: step
title: 'root 요동의 재료: 볼록 함수 $G$ 와 그 분산 (6.11)'
uses: [pert:concentration.s1, pert:concentration.s2.s1, pert:factor, x:pert-standing, tree:insertion, x:tree-extra-variables]
provides: 'pert:concentration.s4 (6.11)'
math: |
  무작위 함수 $G(u)=X_0(u)+2nu^2$ 는 $J_\nu$ 에서 볼록이고, $u\in J_\nu$ 와 다른 모든 매개변수에 균등하게
  $$\operatorname{Var}(G(u))\le C_\nu N,\qquad|\mathbb E_{\mathbf u}G'(u)|\le C_\nu\lambda_\nu.$$
physics: |
  [[g:root-logarithm|root logarithm]] 자체의 [[g:root]] 요동(물리 disorder와 섭동 항들에 대한 분산)은 $O(N)$, 곧 표준편차로 $O(\sqrt N)$ 이다. root 변수 하나(상호작용 하나, 장 하나, 섭동 항 하나)를 바꾸면 root logarithm이 유계만큼만 바뀌고, 그런 변수의 개수가 $O(N)$ 이기 때문이다.
gap: |
  이 상계는 함수 $G$ 의 값의 root 요동(표준편차 $O(\sqrt N)$)에 대한 것이고, 그 도함수, 곧 score의 root 평균 $X_0'=\langle D_\nu\rangle$ 의 요동에 대한 것이 아니다. 함수값의 요동이 작다는 것만으로는 도함수의 요동이 작다는 것이 나오지 않으므로, 도함수로 옮기려면 볼록성을 쓰는 s4가 필요하다. 규모로는 $\sqrt N$ 이 score 규모 $\lambda_\nu=c_\nu N^{3/4}$ 보다 작고, 이 여유 $\sqrt N\ll\lambda_\nu$ 가 s4에서 차분 간격 $\rho$ 를 고를 자리를 준다. 상수 $C_\nu$ 는 type에 의존한다. 분산은 $\mathbf u$ 를 고정한 root 분산이다.
abstraction: weakening
children: [pert:concentration.s3.s1, pert:concentration.s3.s2, pert:concentration.s3.s3]
source:
  - {file: perturbations.tex, lines: [163, 209]}
status: proposed
---

**뼈대.** [[pert:concentration.s3.s1]]: (6.8)에서 $G''\ge0$, 그리고 (6.11)의 진술. [[pert:concentration.s3.s2]]: 개수에 조건을 건 Efron–Stein 부등식(증명 포함). [[pert:concentration.s3.s3]]: 입력 하나를 다시 뽑을 때 $X_0$ 의 변화가 유계(spin weight에서, 그리고 power mean이 보존), 조건부 평균은 개수의 Lipschitz 함수, Poisson 분산 $=$ 평균으로 $O(N)$. 도함수 경계는 (6.6)에서.
