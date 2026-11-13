---
id: cavity:grid
kind: convention
title: '깊이 $L\ge2$, $r=L-1$, 균등 격자 $m_d=d/L$ (5.1)'
uses: [x:tree-path-kernels]
provides: 'cavity:factor-bounds의 "hierarchy", x:cavity-root-logarithm의 $P_N^{L,\mathbf u}$. x:decor-mesh (§7 전체의 $m_d=d/L$, $\delta=1/L$), x:pert-standing (perturbations.tex 3–5: "the depth $L\ge2$ is fixed"), comparison.tex의 $\mathbf m^{(L)}$, $\mathcal B_{L-1}$'
math: |
  $L\ge2$ 를 고정하고 $r=L-1$ 개의 보조 단계를
  $$m_d=d/L\quad(0\le d\le L),\qquad\delta=1/L\tag{5.1}$$
  로 쓴다.
physics: |
  하한은 [[g:parisi-parameters|Parisi parameter]]를 최적화하지 않고 간격 $1/L$ 의 [[g:grid|균등 격자]]에 고정한 $(L-1)$단 [[g:hierarchy|보조 계층]]에서 진행한다([[g:rsb-steps]]: 깊이 $L=r+1$).
gap: |
  같은 내용이다. 이 계층은 섭동 factor의 보조 변수로 만든 것이고(cavity:factor-bounds), 계의 물리적 $(L-1)$단 RSB 구조로 읽는 것은 증명되지 않는다([[g:rsb-steps]]의 물리 대응 칸). $m_0=0$, $m_L=1$ 은 끝점이고 시행 법칙의 매개변수는 $m_1,\ldots,m_{L-1}$ 이다.
abstraction: exact
children: []
source:
  - {file: cavity.tex, lines: [16, 19]}
status: proposed
---

$L=r+1$ 의 대응은 trees.tex 24와 같다. 격자가 시행 법칙의 $\mathbf m^{(L)}=(1/L,\ldots,(L-1)/L)$ 가 되는 것은 §8(comparison.tex)의 일이다.
