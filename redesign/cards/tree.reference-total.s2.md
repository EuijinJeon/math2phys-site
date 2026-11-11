---
id: tree:reference-total.s2
kind: step
title: '거꾸로 합하기 → $\kappa(S)$'
uses: [tree:reference-total.s1, x:tree-reference-paths]
provides: 'tree:reference-total의 (tree:K)와 "임의의 reference 집합에서 반복"'
math: |
  모든 reference path와의 갈라짐 깊이가 일관되게 처방되면, 가장 깊은 요구 공통 prefix가 갈라지는 vertex와 그 제외 reference 자식들을 정한다. 따라서 한 걸음 합은 현재 reference tree에만 의존하고, 어떤 old path나 fresh path가 그것을 실현했는지에는 의존하지 않는다. 연속된 선택을 거꾸로 합한다. 최종 처방 tree의 branching vertex에서, 새 자식 무리에 처음 들어갈 때의 제외 reference 자식 수는 정확히 $1,\ldots,a_v-1$이다. 그 인자들이 (tree:K)를 color 순서와 무관하게 준다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [377, 386]}
status: proposed
---

거꾸로 합하는 이유(작성자 풀이): 마지막 color의 선택에 대해 먼저 합하면 그 합은 그 앞까지의 reference tree에만 의존하는 상수 $m_d-jm_{d+1}$이다. 그것을 빼내고 하나 앞 color로 가는 일을 반복한다. 이미 있는 자식 무리(reference가 있는 가지)로 들어가는 color는 $v$에서 인자를 내지 않고 더 깊은 vertex에서 낸다. 그래서 $v$에서는 새 가지를 여는 $a_v-1$번(처음 $v$를 지난 reference가 이미 차지한 가지를 빼고)만 인자를 낸다.
