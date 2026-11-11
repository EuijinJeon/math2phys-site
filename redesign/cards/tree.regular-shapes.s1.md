---
id: tree:regular-shapes.s1
kind: step
title: '비정칙 확률의 union bound'
uses: [tree:Q-rule, x:tree-regular-shape]
provides: 'tree:regular-shapes의 (tree:irregular-probability)'
math: |
  현재 tree의 leaf가 $n$개라 하자. 새 branching vertex는 다음 path가 unary vertex에서 갈라질 때 정확히 만들어진다. (tree:Q-rule)에 의해 그런 선택은 각각 확률 $\delta/n$이다. 어떤 깊이에도 vertex는 많아야 $n$개다. 그러므로 깊이 집합 $B$에 대해 다음 path가 $B$ 안 깊이에 branching vertex를 만들 확률은 $|B|\delta$ 이하다. 처음 $k-1$ 걸음 각각에서, 경계 깊이와 앞선 어떤 branching vertex에서 정규화 거리 $\eta$ 안에 있는 깊이들은 크기 $C_k(\eta L+1)$ 이하의 집합을 이룬다. 이 금지된 생성 사건이 하나도 일어나지 않으면 최종 tree는 regular다. union bound가 (tree:irregular-probability)를 증명한다. 이미 branching인 vertex에서의 divergence는 새 좌표를 만들지 않으므로 추가로 뺄 필요가 없다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [486, 499]}
status: proposed
---

unary vertex에서 $n_\beta=1$이므로 확률은 $(m_{d+1}-m_d)/n=\delta/n$. 합: $(k-1)\cdot C_k(\eta L+1)\cdot\delta=C_k'(\eta+L^{-1})$(작성자 풀이). "경계 깊이"는 정규화 깊이가 $(\eta,1-\eta)$ 밖인 깊이들, 곧 약 $2\eta L+2$개다. 앞선 branching vertex는 $k-2$개 이하이고 각각 $2\eta L+1$개 이하의 깊이를 금지한다.
