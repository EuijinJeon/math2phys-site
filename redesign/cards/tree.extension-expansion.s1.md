---
id: tree:extension-expansion.s1
kind: step
title: '미분 규칙의 반복: 선택지는 old leaf 또는 fresh path'
uses: [x:tree-differentiation-rule, x:tree-extension-history]
provides: 'tree:extension-expansion.s2'
math: |
  $C=\{a_*\}$, $G=H$에서 시작한다. 앞의 규칙(x:tree-differentiation-rule)을 차례로 적용하며 각 새 $D_j$를 $G$에 넣는다. fresh leaf는 곧바로 protected이므로 protected가 아닌 leaf는 쓰지 않은 old leaf뿐이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [298, 302]}
status: proposed
---

$\partial_{t_j}$ 한 번이 color $j$ 하나를 놓는다. leaf 항은 protected가 아닌 leaf에만 생기므로 (i) "anchor가 아닌 쓰지 않은 old leaf, 계수 1"이 되고, 내부 vertex 항은 (ii) "fresh path, 계수 $\gamma_\beta$"가 된다. 미분 순서를 바꿔도 좌변은 같으므로 어떤 고정된 color 순서에서도 성립한다.
