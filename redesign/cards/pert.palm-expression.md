---
id: pert:palm-expression
kind: definition
title: 'insertion 기대값 $J_{N,\mathcal T}(t,u)$ (6.14)'
uses: [x:pert-test-setup, x:pert-mark-specification, tree:insertion, tree:Y-recursion, x:tree-extra-variables]
provides: 'pert:analytic-difference, pert:palm.s1, pert:analytic.s1–s2'
math: |
  고정된 mark specification에 대해 독립인 새 균일 site와 그 mark 과정의 독립 사본을 도입하고 $A=1+tg\sigma_i+ug_0S_0$ 로 둔다. $Y$ 를 tree:insertion의 insertion recursion, $W_{\mathcal T}(A)$ 를 updated-tree 밀도 (tree:density)라 하자. 아래 식의 기대값은 수정하지 않은 reservoir를 독립 insertion 변수와 그 prior kernel로 넓힌 것을 쓴다:
  $$J_{N,\mathcal T}(t,u)=\mathbb E\left[f\,\frac{g_0^{a_*}S_0^{a_*}}{A^{a_*}}W_{\mathcal T}(A)\right].$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [331, 342]}
status: proposed
---

$W_{\mathcal T}(A)=\prod_aA^a\prod_\beta Y_\beta^{\gamma_\beta}$([[tree:insertion]])이므로 $W_{\mathcal T}(A)/A^{a_*}$ 에서 anchor의 leaf 인자가 상쇄된다. 곧 $J_{N,\mathcal T}=\mathbb E\,E^A_{\mathcal T}[fg_0^{a_*}S_0^{a_*}/A^{a_*}]$ 이고 이것이 [[tree:extension-expansion]] 좌변의 꼴이다(작성자 읽기). "extended by the independent insertion variables with their prior kernels"는 [[x:tree-extra-variables]]의 약속이다: 새 site는 root에, mark 좌표는 배정된 보조 깊이에 prior로 들어가고 원래 tilt는 그 prior를 바꾸지 않는다. $Y$ 의 정의 자체는 [[tree:Y-recursion]]에 있다(원문은 tree:insertion을 가리킨다). $J$ 는 $N$ 과 선택된 벡터(base reservoir의 법칙)에 의존한다.
