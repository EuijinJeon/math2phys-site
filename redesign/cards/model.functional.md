---
id: model:functional
kind: definition
title: '시행 functional $\mathcal B_r$ 와 변분값 $\Phi_r$ (2.11)'
uses: [model:power-means, model:vs, model:ve, model:hamiltonian]
provides: 'main:theorem의 우변. upper:bound($F_N\le\mathcal B_r$), comp:insertion-comparison($\Delta_N\approx\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$), comp:bounded-lower, reduction:stability, models:ground($\mathcal B_{r,\beta}$, consequences.tex 83)'
math: |
  $$\mathcal B_r(\zeta,\mathbf m)=\log2+\mathbb E\log T_0V_{\rm s}-\alpha(p-1)\,\mathbb E\log T_0V_{\rm e},\qquad\Phi_r=\inf_{\zeta,\,\mathbf m}\mathcal B_r(\zeta,\mathbf m).\tag{2.11}$$
  $\mathbb E$ 는 물리적 disorder와 $\eta_0$ 을 평균한다($T_0$ 이 나머지 보조 변수를 적분했다). inf는 모든 $\zeta\in\mathcal M_{r+1}$ 과 $0<m_1<\cdots<m_r<1$ 에 대한 것이다.
physics: |
  $r$단 RSB Mézard–Parisi(Bethe) free entropy를 시행 [[g:order-parameter|order parameter]]에서 계산한 값([[g:functional]]): [[g:site-term|site 항]]에서 [[g:edge-term|edge 항]]의 $\alpha(p-1)$ 배를 뺀다. $\alpha(p-1)$ 은 spin 하나를 넣을 때 평균 $\alpha p$ 개 factor 중 새로 생기는 factor 수 $\alpha$ 를 뺀 중복분이다. $\Phi_r$ 는 단계 수 $r$ 에서의 inf([[g:phi]])다.
gap: |
  물리는 정류점(saddle point)에서 평가한 값을 free entropy로 쓰고, 여기서는 모든 시행값의 inf를 쓴다. 모든 시행값이 pressure의 상한(upper:bound)이라는 것이 inf를 정당화한다. inf의 달성이나 최적 $(\zeta,\mathbf m)$ 의 존재는 주장하지 않는다. "새로 생기는 factor 수 $\alpha$" 계산은 작성자의 읽기다(원문은 edge 항이 중복을 보정한다고만 한다, model.tex 50–52). $\Phi_r$ 이 $r$ 에 대해 단조인지 원문은 말하지 않는다.
abstraction: approximation
children: []
source:
  - {file: model.tex, lines: [111, 117]}
status: proposed
---

$\mathbb E\log T_0V$ 가 잘 정의되고 유한하다는 것은 [[model:trial-bounds]]에서 온다. $r=0$ 판은 [[x:model-depth-zero]].
