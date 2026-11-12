---
id: pert:palm.s1
kind: step
title: 'Poisson add-one 항등식으로 score를 insertion으로'
uses: [pert:score, pert:factor, pert:palm-expression, tree:insertion, x:tree-extra-variables]
provides: 'pert:palm.s2'
math: |
  $D_\nu$ 의 type-$\nu$ 항 합에 Poisson add-one 항등식을 적용한다. 평균 $c_\nu s_N$ 으로 나눈 뒤, 남은 개수는 다시 평균 $c_\nu s_N$ 의 Poisson이고 다른 모든 개수는 바뀌지 않는다. 따라서 남은 모형은 정확히 원래 reservoir 법칙을 가진다. 구별된 항은 매개변수 $t_\nu,u_\nu$ 의 독립 새 insertion이 된다. 그 score는 $g_0^{a_*}S_0^{a_*}/A^{a_*}$ 이다. updated tree 밀도는 (tree:density)이므로 anchor 인자 $A^{a_*}$ 가 상쇄된다. 이로써
  $$\frac{\mathbb E[fD_\nu^{a_*}]}{c_\nu s_N}=J_{N,\mathcal T}(t_\nu,u_\nu),\qquad\frac{\mathbb E\langle D_\nu\rangle}{c_\nu s_N}=J_{N,\{a_*\}}(t_\nu,u_\nu).$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [362, 377]}
status: proposed
---

풀이(작성자). Poisson add-one(Mecke) 항등식: 평균 측도 $\lambda\mu$ 의 Poisson 과정 $\Pi$ 에 대해 $\mathbb E\sum_{x\in\Pi}F(x,\Pi)=\lambda\int\mathbb EF(x,\Pi\cup\{x\})\,\mu(dx)$. 여기서 점 $x$ 는 type-$\nu$ 항 하나(균일 site, mark 과정 사본)이고 $F$ 는 $f\cdot(\text{그 항의 anchor score})$ 다. 점 $x$ 를 더한 계의 tree 법칙은 base reservoir의 tree 법칙에 [[tree:insertion]]의 밀도 $W_{\mathcal T}(A)$ 를 곱한 것이므로(새 항이 쓰는 변수는 [[x:tree-extra-variables]]대로 prior로 붙음) $\mathbb E[fD^{a_*}_\nu]=\lambda\,\mathbb E[f\,(g_0^{a_*}S_0^{a_*}/A^{a_*})W_{\mathcal T}(A)]$ 이다. 둘째 식은 tree를 anchor 하나로 두고 $f=1$ 로 둔 같은 계산이다. 여기서 "기대값"은 고른 벡터를 고정하고 [[g:root]](개수 포함)와 path에 대해 취한다. add-one 항등식이 평균하는 것은 root의 Poisson 개수이지 매개변수가 아니다.
