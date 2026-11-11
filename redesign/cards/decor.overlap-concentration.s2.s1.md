---
id: decor:overlap-concentration.s2.s1
kind: step
title: 'marker anchor 구성과 계수 $C(S,e)$'
uses: [pert:tree-identity, tree:reference-total, x:decor-mesh, x:decor-topology]
provides: 'decor:overlap-concentration.s2.s2'
math: |
  old tree는 $S$의 sampled copy, 그 leaf 하나가 marker anchor다. added color $k=|S|$개가 $S$의 사본 하나를 이루고 그 모든 leaf가 anchor와 깊이 $e-1$에서 갈라진다는 제약을 둔다. 그러면 첫 target 경로는 깊이 $e-1$에서 fresh여야 하고(old tree는 거기서 아직 갈라지지 않았고 옛 leaf들은 anchor와 깊이 $e$까지 prefix를 공유하므로 쓸 수 없다), 나머지 target 경로는 그렇게 생긴 fresh 부분 tree 안에 놓인다. 확장 계수의 총합은 old tree 쪽과 anchor 혼자인 쪽 모두
  $$C(S,e)=-\delta\,\kappa(S)\ne0.$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [537, 549]}
status: proposed
---

기준 모양은 깊이 $e-1$에서 두 자식([[g:anchor|anchor]], 새 사본)으로 갈라지고 그 아래 $S$의 사본이 붙은 것이다. tree:reference-total에서 총 계수는 $(m_{e-1}-m_e)\kappa(S)=-\delta\kappa(S)$이고 old tree에 무관하다. $\kappa(S)\ne0$인 이유: $j=1$ 인자는 $-\delta$, $j\ge2$ 인자는 $(j-1)m_{d_v}+j\delta>0$. 한 칸 앞인 $e-1$에서 조건을 거는 이유는 그 vertex가 old tree에서 unary라서 target이 old 가지를 재사용할 수 없기 때문이다.
