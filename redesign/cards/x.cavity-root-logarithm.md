---
id: x:cavity-root-logarithm
kind: definition
title: '섭동된 계의 기대 root logarithm $P_N^{L,\mathbf u}$'
uses: [cavity:factor-bounds, x:cavity-root-convention, cavity:grid, tree:original-tilt, model:hamiltonian]
provides: 'cavity:negligible, cavity:increment ($\Delta_N^{L,\mathbf u}=P_{N+1}^{L,\mathbf u}-P_N^{L,\mathbf u}$). pert:selection(perturbations.tex 270–277)의 $P_N^{L,\mathbf u}$'
math: |
  섭동을 더한 leaf 분배함수에 power-mean recursion을 적용한다. 그 root logarithm의 기대값을 $P_N^{L,\mathbf u}$ 로 쓴다.
physics: |
  $P_N^{L,\mathbf u}$ 는 섭동된 $N$-spin 계의 계층 free entropy(밀도가 아닌 전체량)이다: 섭동 factor의 보조 변수를 지수 $m_d=d/L$ 의 [[g:power-mean|power mean]]으로 차례로 적분한 [[g:root-logarithm|root logarithm]]을 disorder에 대해 평균한 것.
gap: |
  $L\ge2$ 에서는 보통 뜻의 섭동된 계의 $\mathbb E\log Z$ 가 아니다(보조 변수를 tilt해서 적분한다, [[g:root-logarithm]]). 기대값은 [[g:root]] 전체(물리 disorder, 섭동 개수·type·site)에 대한 것이고 $\mathbf u$ 는 고정이다(x:cavity-root-convention).
abstraction: approximation
children: []
source:
  - {file: cavity.tex, lines: [34, 35]}
status: proposed
---

recursion은 [[tree:original-tilt]]의 $X_{L-1}=\log Z$, $X_{d-1}=m_d^{-1}\log P_de^{m_dX_d}$ 이다. 원문 34행의 "the power-mean recursion"을 이 식으로 읽었다(작성자 읽기, `\ref` 없음).
