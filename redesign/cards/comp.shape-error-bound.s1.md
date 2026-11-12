---
id: comp:shape-error-bound.s1
kind: step
title: 'regular가 아닌 tree의 기여'
uses: [tree:regular-shapes, x:tree-regular-shape, tree:multioverlap, decor:average-definition]
provides: 'comp:shape-error-bound.s3 (항 $C_k(\eta+L^{-1})$)'
math: |
  singleton에 대한 평균은 깊이 좌표가 없다. tree:regular-shapes에 의해 regular가 아닌 tree의 $Q_k$ 확률은 많아야 $C_k(\eta+L^{-1})$ 이다. 그런 tree에서는 각 편차를 $\mathbb E\lvert R_S-\mathbb ER_S\rvert\le2$ 로 누른다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [140, 142]}
status: proposed
---

"bound two for each deviation on nonregular trees"(152)는 이 단계의 몫이다($\lvert R_S\rvert\le1$). 부분집합 $S$ 는 $2^k-1$ 개이므로 기여는 $(2^k-1)\cdot2\cdot C_k(\eta+L^{-1})$ 이고 상수에 흡수된다(작성자 계산). regular의 정의는 [[x:tree-regular-shape]](trees.tex 462–465)이고 singleton은 regular다.
