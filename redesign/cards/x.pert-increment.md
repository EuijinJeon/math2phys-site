---
id: x:pert-increment
kind: definition
title: '$\underline F$ 와 섭동된 증분 $\Delta_N(\mathbf u)$'
uses: [model:hamiltonian, x:cavity-bounded, x:cavity-root-logarithm, cavity:increment]
provides: 'pert:selection (i)과 s1–s2. 규칙 P5, g:lower-pressure의 정의 위치'
math: |
  매개변수 선택은 집중과 낮은 cavity 증분을 동시에 만족해야 한다. $\underline F=\liminf_NF_N$ 은 bounded 모형의 모든 크기에 대한 liminf다. $P_N^{L,\mathbf u}$ 는 root 평균한 섭동된 log 분배함수(x:cavity-root-logarithm)이고
  $$\Delta_N(\mathbf u)=P_{N+1}^{L,\mathbf u}-P_N^{L,\mathbf u}$$
  로 둔다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [248, 253]}
status: proposed
---

$\Delta_N(\mathbf u)$ 는 [[cavity:increment]]의 $\Delta_N^{L,\mathbf u}$ 와 같다. $\underline F$ 는 섭동 없는 bounded 모형([[x:cavity-bounded]])의 $F_N=\frac1N\mathbb E\log Z_N$([[model:hamiltonian]])의 liminf이고, 선택 전의 모든 크기에 대해 취한다(comparison.tex 11–12 "Retain $\underline F$ for the liminf over all system sizes … as before selection"). [[g:lower-pressure]], [[g:increment]].
