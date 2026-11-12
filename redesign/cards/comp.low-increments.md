---
id: comp:low-increments
kind: remark
title: '선택된 수열 위의 낮은 증분 (8.1)'
uses: [x:comp-standing, pert:selection, x:pert-increment, cavity:increment]
provides: 'comp:bounded-lower.s1 (comparison.tex 236)'
math: |
  x:comp-standing의 선택에서, 각 $L\ge2$ 와 그 수열 위의 모든 $N$ 에 대해(작성자: "모든 $N$"; 근거 perturbations.tex 299 "Relabeling the tail proves (i)")
  $$\Delta_N^{L,\mathbf u_{L,N}}\le\underline F+2\varepsilon.\tag{8.1}$$
physics: |
  고른 [[g:selected-sequence|선택된 수열]] 위에서는 섭동된 계의 [[g:increment|cavity 증분]]이 섭동 없는 pressure의 liminf([[g:lower-pressure]])를 $2\varepsilon$ 보다 더 넘지 않는다.
gap: |
  pert:selection (i)를 §8의 표기로 다시 적은 것이다. 상한뿐이고, 증분의 극한이나 $\lim F_N$ 의 존재를 말하지 않는다. 좌변은 선택된 벡터에서의 섭동된 계의 증분([[g:root-logarithm]]의 차)이고, 우변의 $\underline F$ 는 섭동 없는 bounded 모형의 모든 크기에 대한 liminf다.
abstraction: exact
children: []
source:
  - {file: comparison.tex, lines: [12, 15]}
status: proposed
---

$\Delta_N^{L,\mathbf u}$ 는 [[cavity:increment]]의 증분 $P_{N+1}^{L,\mathbf u}-P_N^{L,\mathbf u}$ 이고 [[x:pert-increment]]의 $\Delta_N(\mathbf u)$ 와 같다. 원문 12행 "In particular"가 이 식을 앞 문단의 선택에서 끌어낸다.
