---
id: tree:regular-shapes
kind: lemma
title: 'Regular shapes ($Q_k$ 아래 예외 깊이의 확률)'
uses: [tree:Q-rule, x:tree-regular-shape]
provides: '§8 comp:shape-error-bound (comparison.tex 141–148: 비정칙 tree의 확률, 배정 확률 C_kL^{-a}, induced subtree의 regularity 보존). tree:averaging-remark'
math: |
  ($m_d=d/L$, $0<\eta<1/2$.) 모든 고정 $k$에 대해 $L$과 $\eta$에 무관한 $C_k<\infty$가 있어
  $$Q_k\{\mathcal T\text{ is not regular}\}\leq C_k(\eta+L^{-1}).$$
  $a$개 branching vertex를 가진 특정 labeled topology와 그 깊이의 일관된 배정 하나에 대해
  $$Q_k\{\text{that topology and depth assignment}\}\leq C_kL^{-a}.$$
  regular tree에서 leaf를 지우면, unary가 된 branching vertex를 버린 뒤 regular tree가 나온다.
physics: |
  [[g:tree-law|$Q_k$]]로 뽑은 $k$개 [[g:replica|replica]]의 tree에서 갈라짐 [[g:depth|깊이]]가 경계 근처에 있거나 두 갈라짐 깊이가 서로 가까울 확률은 $C_k(\eta+1/L)$ 이하다. 정해진 갈라짐 구조와 깊이 배정 하나의 확률은 $C_kL^{-a}$ 이하다: 각 갈라짐 깊이가 대략 균등하게 퍼진다. replica 일부를 잊어도 [[g:eta-regular|regular]]함은 남는다.
gap: |
  [[g:grid|균등 격자]] $m_d=d/L$에서만 진술된다. 상수 $C_k$는 명시되지 않고 $k$에만 의존한다. 상계일 뿐이며 깊이 분포의 극한 꼴을 말하지 않는다.
abstraction: exact
children: [tree:regular-shapes.s1, tree:regular-shapes.s2, tree:regular-shapes.s3]
source:
  - {file: trees.tex, lines: [469, 484]}
  - {file: trees.tex, lines: [486, 514]}
status: proposed
---

**증명의 뼈대.** [[tree:regular-shapes.s1]]: 새 branching vertex는 다음 path가 unary vertex에서 갈라질 때만 생기고 그 확률은 vertex마다 $\delta/n$이므로, 깊이 집합 $B$에 새 branching을 만들 확률은 $|B|\delta$ 이하. 금지 깊이 $C_k(\eta L+1)$개를 $k-1$ 걸음에 걸쳐 union bound. [[tree:regular-shapes.s2]]: 지정된 tree의 history는 유일하고, $a$개 branching vertex의 생성마다 확률 $\le\delta$. [[tree:regular-shapes.s3]]: 지운 뒤 남는 branching vertex는 원래의 것이고 깊이도 같다.

원문의 lemma 진술에는 $m_d=d/L$가 다시 적혀 있지 않지만 §3.4 서두 "Still take $m_d=d/L$"(460)이 그 범위를 정한다. $0<\eta<1/2$는 regular의 정의(462)에서 온다.
