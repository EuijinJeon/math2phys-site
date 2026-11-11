---
id: tree:regular-shapes.s2
kind: step
title: '특정 깊이 배정의 확률 $\le C_kL^{-a}$'
uses: [tree:Q-rule]
provides: 'tree:regular-shapes의 (tree:assignment-probability)'
math: |
  (tree:assignment-probability)를 위해, 지정된 최종 labeled tree를 unary 구간을 모두 남긴 채 leaf $1,\ldots,n$으로 제한한다. 이 제한들이 (tree:Q-rule) 아래의 연속된 history를 정한다. $a$개 branching vertex 각각은 처음에 unary divergence로 만들어지고 그 확률은 $\delta$ 이하다. 다른 모든 전이 확률은 $1$ 이하다. 따라서 지정된 history의 확률은 $\delta^a$ 이하다. topology 기술이 동치인 자식 순서들을 같게 보면, 그 수는 $k$만으로 유계이고 이것이 $C_k$를 붙인 판을 준다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [501, 510]}
status: proposed
---

$Q_k$의 tree는 label 순서대로 자라므로, 최종 tree를 leaf $1,\ldots,n$에 제한한 것이 $n$번째 걸음 뒤의 tree다. 그래서 최종 tree 하나에 history가 하나다. $\delta/n\le\delta$. 모든 leaf가 깊이 $L$에 있으므로 labeled topology와 branching 깊이가 (자식 순서를 빼면) 최종 tree를 정한다(작성자 풀이).
