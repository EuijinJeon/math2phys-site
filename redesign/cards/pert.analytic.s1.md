---
id: pert:analytic.s1
kind: step
title: '균등한 해석적 경계'
uses: [tree:extension-expansion, pert:analytic-difference, pert:palm-expression, x:pert-selected-limits]
provides: 'pert:analytic.s2 (기하 꼬리), s3 (u-도함수 경계 C)'
math: |
  tree:extension-expansion이 복소 근방 $|t|,|u|<\rho$ 를 주고, 거기서 (6.15)의 함수들은 해석적이며 $N$ 과 선택된 매개변수 벡터에 균등하게 유계다. $\rho$ 를 줄이면 그 $u$-도함수에도 균등한 경계가 나온다. 이 상수들은 고정 tree, $L$, $\|f\|_\infty$ 에 의존해도 되지만 mark specification 안의 type 첨자 $j$ 에는 의존하지 않는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [390, 397]}
status: proposed
---

읽기(작성자). [[tree:extension-expansion]]은 $A_{\boldsymbol t}=1+\sum_jt_jD_j$ 꼴의 좌변에 kernel에 균등한 해석적 경계를 준다고 말한다(경계 자체는 [[x:tree-analytic-bounds]]: $\sum_j|t_j|\|D_j\|_\infty<1$ 에서 해석, 더 작은 영역에서 도함수 경계). 여기서는 $D_1=g\sigma_i$, $D_2=g_0S_0$, $\|D_j\|_\infty\le1$ 이므로 $|t|+|u|<1$ 의 영역이 된다. "kernel에 균등"이 "$N$ 과 선택된 벡터에 균등"으로 바뀌는 것은 reservoir의 tilted kernel이 $N$ 과 벡터에 따라 바뀌어도 경계가 kernel에 의존하지 않기 때문이다. $j$ 무관: $g,g_0,S_0$ 은 specification에만 의존하고 $t,u$ 는 이제 자유 변수다. "Shrinking $\rho$"는 Cauchy 추정으로 읽었다(x:tree-analytic-bounds 카드의 읽기와 같음). 좌변의 $H$ 자리에 오는 $fg_0^{a_*}S_0^{a_*}$ 는 insertion 변수를 포함하지만 [[x:tree-extra-variables]]로 넓힌 tree 위의 유계 함수이고 insertion 매개변수에 의존하지 않는다.
