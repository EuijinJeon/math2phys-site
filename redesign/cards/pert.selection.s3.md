---
id: pert:selection.s3
kind: step
title: '대각 부분수열로 모든 유한 tree moment를 수렴시키기'
uses: [pert:selection.s2, tree:multioverlap, x:tree-sampling]
provides: 'pert:selection (iii) → pert:analytic.s2 (Taylor 계수의 수렴)'
math: |
  고정 $L$ 에서 유한 labeled tree 모양과 그 multioverlap의 유한곱은 가산 모임을 이룬다. 각 곱은 절댓값이 1 이하다. 대각 부분수열이 (iii)을 주고 (i)이나 (ii)에 영향을 주지 않는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [301, 306]}
status: proposed
---

$|R_S|\le1$([[tree:multioverlap]])이므로 각 기대값 수열은 유계이고, 가산 개의 유계 수열에 대해 Bolzano–Weierstrass와 대각 논법으로 모두 수렴하는 부분수열을 얻는다. (i)은 각 항의 성질이고 (ii)는 수렴이므로 부분수열로 보존된다. 극한값은 식별되지 않는다. 유한 tree는 [[x:tree-sampling]]의 것이고 깊이는 $L$ 이다(작성자 풀이).
