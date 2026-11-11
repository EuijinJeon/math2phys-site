---
id: tree:Q-rule
kind: definition
title: 'tree 법칙 $Q_k$'
uses: [tree:telescoping]
provides: 'tree:log-expansion (급수의 tree 평균), tree:regular-shapes, tree:averaging-remark. §4 upper.tex 121 ("The tree law Q_n ... common to the three insertions"), §8 comparison.tex 123 이하'
math: |
  leaf label이 $1,\ldots,k$인 tree 위의 확률 법칙 $Q_k$를 다음과 같이 정한다. path 하나로 시작한다. 현재 tree의 leaf가 $n$개일 때 내부 vertex $\beta$를 확률
  $$\frac{n_\beta m_{d_\beta+1}-m_{d_\beta}}{n}$$
  로 골라 거기에 새 자식을 만들고, 깊이 $L$까지 완전히 새 path로 잇는다. 그 말단 vertex에 label $n+1$을 준다. 항등식 (tree:telescoping)이 정규화를 확인한다. 무작위 tree는 그 위에서 나중에 뽑히는 모든 변수와 독립으로 선택된다. 예: $Q_2$ 아래에서 두 path는 $0\le d<L$에 대해 확률 $m_{d+1}-m_d$로 깊이 $d$에서 갈라진다. $m_d=d/L$이면 이 split은 깊이에 대해 균등하다.
physics: |
  [[g:tree-law|tree 법칙]] $Q_k$: [[g:replica|replica]]를 하나씩 붙여 가며, $n$개가 있을 때 새 replica가 내부 vertex $\beta$(깊이 $d_\beta$, 자식 $n_\beta$개)에서 갈라질 확률이 $(n_\beta m_{d_\beta+1}-m_{d_\beta})/n$이다. 두 replica가 깊이 $d$ [[g:state|상태]]까지 공유하고 거기서 갈라질 확률은 $m_{d+1}-m_d$다. [[g:grid|균등 격자]]에서는 갈라짐 깊이가 균등하다.
gap: |
  $Q_k$는 지수열 $\mathbf m$만으로 정해지는 유한 tree 위의 법칙이고, kernel이나 spin과 무관하다. 이것을 물리 그림의 replica overlap tree 법칙으로 읽는 것은 [[g:tree-law]]와 [[g:parisi-parameters]]의 물리 대응 칸에 intuition으로만 있다. 갈라짐 "깊이"는 보조 계층의 정수 깊이이지 overlap 값이 아니다([[g:depth]]).
abstraction: exact
children: []
source:
  - {file: trees.tex, lines: [209, 222]}
status: proposed
---

확률이 양인 것과 합이 1인 것은 [[tree:telescoping]]이다. "내부 vertex"는 root와 unary vertex를 포함한다([[x:tree-sampling]]). unary vertex($n_\beta=1$)에서 확률은 $(m_{d+1}-m_d)/n$, 균등 격자에서 $\delta/n$이고, 이것이 [[tree:regular-shapes]]의 증명에 쓰인다.

$L=1$이면 내부 vertex는 root뿐이고 확률은 $(n\cdot1-0)/n=1$: 모든 replica가 root에서 갈라진다(독립 Gibbs 표본).
