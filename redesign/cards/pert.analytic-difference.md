---
id: pert:analytic-difference
kind: definition
title: '차 $H_N(t,u)=J_{N,\mathcal T}-\mathbb Ef\,J_{N,\{a_*\}}$ (6.15)'
uses: [pert:palm-expression, x:pert-test-setup]
provides: 'pert:palm (H_N의 경계), pert:analytic (Taylor 계수), pert:tree-identity.s1, s4'
math: |
  $$H_N(t,u)=J_{N,\mathcal T}(t,u)-\mathbb Ef\,J_{N,\{a_*\}}(t,u).$$
  single-anchor 식 $J_{N,\{a_*\}}$ 에서 시험함수는 $1$ 이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [343, 348]}
status: proposed
---

$J_{N,\{a_*\}}$ 는 old tree를 anchor 하나로 된 tree로 바꾼 것이다. 두 항의 차가 [[pert:tree-identity]]의 좌변 꼴(old tree 쪽 합 빼기 $\mathbb Ef$ 곱하기 anchor 하나 쪽 합)의 원형이다. [[g:palm-identity]].
