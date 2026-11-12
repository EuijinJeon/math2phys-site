---
id: pert:parameters
kind: definition
title: '섭동 type $\nu$ 와 매개변수 $t_\nu=1/j$, $u_\nu\in[j^{-j},2j^{-j}]$ (6.1)'
uses: [x:pert-mark-specification]
provides: 'pert:factor, x:pert-parameter-measure, pert:score, pert:concentration.s1 (구간 J_ν), pert:analytic.s3 (u_ν가 t_ν의 모든 고정 거듭제곱보다 작음)'
math: |
  두 매개변수의 역할은 다르다: $u$ 에 대한 미분은 집중하는 score를 내고, $t$ 의 값들은 insertion의 Taylor 전개를 탐침한다. $u$ 를 $t$ 의 모든 고정 거듭제곱보다 작게 잡으면 각 극한 Taylor 계수가 0이 된다. 각 specification마다 모든 정수 $j\ge4$ 로 첨자 붙은 type을 둔다. specification과 $j$ 에 대응하는 type $\nu$ 는
  $$t_\nu=j^{-1},\qquad I_\nu=[j^{-j},2j^{-j}],\qquad u_\nu\in I_\nu$$
  를 가진다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [40, 50]}
status: proposed
---

같은 mark specification의 type들은 $j$ 만 다르고 같은 함수 $g,g_0$, 같은 $S_0$ 을 쓴다. 이 점이 [[pert:palm]]의 "$H_N(t,u)$ 는 그 모든 type $j$ 에 대해 같다"와 [[pert:analytic.s3]]의 논법(같은 해석함수를 점 $t=1/j$ 들에서 보고, $u_\nu\le2j^{-j}$ 가 $j^{-q}$ 보다 빨리 작아짐)을 가능하게 한다. 40–43행의 역할 설명은 그 논법의 예고다.

$j\ge4$ 이므로 $|t_\nu|\le1/4$, $|u_\nu|\le2\cdot4^{-4}$ 이고, 이것이 [[pert:factor]]의 $1/2<\psi_\nu<3/2$ 를 준다(작성자 계산).
