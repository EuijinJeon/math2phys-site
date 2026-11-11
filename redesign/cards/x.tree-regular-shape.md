---
id: x:tree-regular-shape
kind: definition
title: 'tree 하나의 regular shape (§3.4, $m_d=d/L$)'
uses: [x:tree-sampling]
provides: 'tree:regular-shapes, tree:averaging-remark. §7 x:decor-eta-regular와 §8 comparison.tex 131, 141–143이 같은 조건을 쓴다'
math: |
  여전히 $m_d=d/L$로 둔다. unary 구간은 모양을 유한한 topology와 그 branching-depth 좌표로 기술할 때만 억누른다. $0<\eta<1/2$에 대해, 모든 branching 깊이를 $L$로 나눈 값이 $(\eta,1-\eta)$에 있고 서로 다른 두 branching vertex의 정규화 깊이가 $\eta$보다 더 차이 나면 모양을 regular라 한다. singleton은 regular다. 이것은 tree 하나를 뽑을 때 쓰는 regularity이고, 뒤에서는 대응하는 깊이 배정을 일부러 맞춘(aligned) 두 사본도 쓴다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [458, 467]}
status: proposed
---

[[g:eta-regular|$\eta$-regular]]의 tree 하나 판이다. "서로 다른 두 branching vertex"는 같은 가지 위에 있든 다른 가지 위에 있든 모두 해당한다. aligned 두 사본에서는 대응 vertex가 깊이 좌표를 공유하므로 조건은 서로 다른 좌표에 건다([[x:decor-eta-regular]]). 정규화 깊이가 $\eta$보다 크다는 것은 $m_{d_v}=d_v/L>\eta$이므로 [[tree:charging]]의 가정 $m_{d_v}\ge\eta$를 준다. 물리 대응은 없다: 경계 근처와 서로 가까운 갈라짐을 기술적으로 빼는 조건이다.
