---
id: cavity:factor-bounds
kind: definition
title: 'Poisson 섭동 factor 족과 한계 $1/2\le\psi_\nu\le3/2$ (5.2)'
uses: [cavity:grid, model:hamiltonian, tree:original-tilt]
provides: 'x:cavity-root-convention, x:cavity-root-logarithm, cavity:negligible (항별 비용 $\log2$), cavity:increment과 그 증명 s2 (섭동 개수의 맞춤). pert:factor(perturbations.tex 48–67)가 구체적 factor $\psi_\nu=1+t_\nu g\sigma_i+u_\nu g_0S_0$ 로 이 틀을 채운다. 규칙 P3'
math: |
  $(c_\nu)_{\nu\ge1}$ 을 $\sum_\nu c_\nu=1$ 인 양수열로, $s_N=N^{3/4}$ 로 둔다. spin weight에 단일 site factor $\psi_\nu$ 의 독립 Poisson 족을 더한다. 개수의 평균은 $c_\nu s_N$ 이고 site는 $[N]$ 의 독립 균일 site다. 각 factor는 자기 보조 변수를 쓰며, 그 변수는 계층을 따라 곱 prior로 뽑힌다. 각 factor는
  $$1/2\le\psi_\nu\le3/2\tag{5.2}$$
  를 만족한다.
physics: |
  섭동: type $\nu$ 마다 평균 $c_\nu N^{3/4}$ 개(전체 평균 $N^{3/4}$, 곧 sublinear)의 단일 spin factor를 무작위 site에 붙인다([[g:perturbation]]). 각 factor는 자기 [[g:hierarchy|보조 계층]] 변수를 갖고, 값은 $[1/2,3/2]$ 안이다.
gap: |
  같은 내용이다. factor의 구체적 꼴과 보조 변수(mark)는 perturbations.tex에서 정한다(cavity.tex 31–32의 예고). 물리의 "무한소 섭동장"과의 대응은 [[g:perturbation]]의 물리 대응 칸에 intuition으로만 있다.
abstraction: exact
children: []
source:
  - {file: cavity.tex, lines: [20, 27]}
status: proposed
---

"drawn along the hierarchy with product priors"는 보조 변수가 [[tree:original-tilt]]의 prior kernel $P_d$ 를 곱 꼴로 이룬다는 뜻으로 읽었다. 그 뒤 power-mean recursion이 그 prior를 tilt한다([[x:cavity-root-logarithm]]). 섭동이 없으면 leaf 분배함수가 보조 변수에 의존하지 않는다.
