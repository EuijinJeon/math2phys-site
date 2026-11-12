---
id: pert:analytic.s2
kind: step
title: 'Taylor 계수의 수렴과 극한 해석함수 $H$'
uses: [pert:analytic.s1, pert:selection, tree:extension-expansion, tree:multioverlap, pert:palm-expression]
provides: 'pert:analytic.s3'
math: |
  $H_N(t,0)$ 의 각 Taylor 계수는 prescribed tree 위 multioverlap moment와 그런 moment 두 개의 곱의 유한 일차결합이다. 그 계수는 고정 tree, 지수, mark 법칙, 다항식 시험으로 정해지고 $N$ 에 무관하다. 실제로 canceled anchor 전개는 고정된 차수마다 유한 개의 확장을 주고, 독립 insertion site를 평균하면 그 spin 곱이 multioverlap이 된다. 이 계수들은 pert:selection (iii)으로 수렴한다. 그러면 균등 해석적 경계가 Taylor 꼬리의 기하 경계를 통해 $H_N(t,0)$ 이 각 더 작은 원판에서 해석함수 $H(t)$ 로 균등 수렴함을 함의한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [399, 409]}
status: proposed
---

읽기(작성자). $k$ 차 계수는 [[tree:extension-expansion]]에서 같은 방향 $D=g\sigma_i$ 의 $t^k$ 계수(우변을 $k!$ 로 나눈 것)이다. 각 history $E$ 의 항 $E_{\mathcal T_E}[fg_0^{a_*}S_0^{a_*}\prod_j(g\sigma_i)^{a_j(E)}]$ 에서 mark 기대값은 tree의 vertex 공유 구조로 정해지는 수가 되고(mark는 base reservoir와 독립), 새 site $i$ 의 균일 평균이 $\frac1N\sum_i\sigma_i^{a_*}\prod_j\sigma_i^{a_j}$ 같은 multioverlap을 만든다. $f$ 가 multioverlap 다항식이므로 결과는 유한 tree 위 multioverlap 곱의 기대값이다. 두 moment의 곱은 $\mathbb Ef\cdot J_{N,\{a_*\}}$ 쪽에서 나온다. 극한 $H$ 는 존재만 알고 값은 모른다. Cauchy 추정: 균등 경계 $M$ 이면 $k$ 차 계수가 $M\rho^{-k}$ 이하라 작은 원판에서 꼬리가 기하급수로 작고, 각 계수의 수렴과 합쳐 균등 수렴한다.
