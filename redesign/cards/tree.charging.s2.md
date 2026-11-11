---
id: tree:charging.s2
kind: step
title: 'target vertex를 생성 걸음에 배정'
uses: [x:tree-extension-history]
provides: 'tree:charging.s3'
math: |
  허용된 history 하나와 그 지정된 target branching vertex 하나를 생각한다. 그 vertex는 old tree에서 이미 branching일 수 없다. 현재 tree에서 그것이 처음 branching이 된 걸음에서, 따라서 fresh path가 그것이 unary일 때 거기서 갈라졌어야 한다. 그 vertex 자체는 더 앞서 새 unary path의 일부로 만들어졌을 수 있다. 그때도 같은 결론이 성립한다. 서로 다른 target vertex는 서로 다른 걸음에서 branching이 된다. fresh path 하나는 branching vertex를 하나만 만들기 때문이다. $b$개 vertex 각각을 그 생성 걸음에 배정한다. 가능한 배정은 많아야 $k!/(k-b)!$가지다(그리고 반드시 $b\leq k$).
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [427, 436]}
status: proposed
---

"old tree에서 이미 branching일 수 없다"는 가정(지정 깊이가 old tree의 어떤 branching 깊이도 아니다)에서 온다. 옛 leaf를 재사용하는 걸음(계수 1)은 새 branching vertex를 만들지 않는다. old leaf는 old tree에 이미 있는 가지를 쓰기 때문이다(작성자 풀이). 그래서 branching을 만드는 걸음은 unary vertex에서의 fresh divergence뿐이다.
