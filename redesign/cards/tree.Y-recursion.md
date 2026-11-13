---
id: tree:Y-recursion
kind: definition
title: 'insertion recursion $Y_d$ 와 바뀐 kernel $K_d^A$'
uses: [x:tree-path-kernels]
provides: 'tree:insertion, tree:first-variation, x:tree-analytic-bounds, tree:log-expansion (Y_0). §4 upper:regularization의 Y_0, §8 comp:insertion-comparison의 trial recursion (comparison.tex 175). 이 카드는 tree:updated-kernel도 담는다'
math: |
  양의 path 함수 $A$에 대해
  $$Y_L=A,\qquad Y_{d-1}=\bigl(K_dY_d^{m_d}\bigr)^{1/m_d},\qquad d=L,\ldots,1$$
  로 정의한다. 처음에는 $A$가 root가 주어진 조건부로 위로 유계이고 0에서 떨어져 있다고 가정한다. 그러면 아래 모든 식이 잘 정의된다. insertion 뒤의 kernel을
  $$K_d^A(dz\mid\mathscr F_{d-1})=\left(\frac{Y_d(z)}{Y_{d-1}}\right)^{m_d}K_d(dz\mid\mathscr F_{d-1})$$
  로 쓴다. recursion이 이것들이 확률 kernel임을 보인다. tree 기대값의 위첨자 $A$는 이 kernel을 쓴다는 뜻이다.
physics: |
  양의 path 함수인 [[g:insertion|insertion]] $A$([[g:root]]가 주어진 조건부로 위로 유계이고 0에서 떨어져 있다고 둔다)의 효과를 아래에서 위로 적분한다: 말단 kernel로 $A$를 평균한 $Y_{L-1}=K_LA$($m_L=1$)를 구하고, 그 위로 깊이마다 지수 $m_d$의 [[g:power-mean|power mean]]을 취한다. 바뀐 kernel은 $(Y_d/Y_{d-1})^{m_d}$로 재가중한다: 깊이 $d<L$에서는 깊이 $d$ [[g:state|상태]]의 무게를, $d=L$에서는 spin 배치의 무게를.
gap: |
  $A$가 root가 주어진 조건부로 위아래로 유계라는 가정 아래의 정의다. 정의는 임의의 kernel 열에 대한 것이다. $K_LA$를 Gibbs 평균으로 읽는 것은 kernel을 분배함수에서 만든 경우, 곧 $K_L$이 prefix가 주어진 Gibbs kernel인 경우([[tree:original-tilt]], trees.tex 63–64)의 것이다. 복소 매개변수의 $A=1+\sum_jt_jD_j$로 넓히는 것은 [[x:tree-analytic-bounds]]가 한다.
abstraction: exact
children: []
source:
  - {file: trees.tex, lines: [67, 82]}
status: proposed
---

식 (tree:updated-kernel)은 이 카드의 범위(76–79)에 있으므로 따로 카드를 두지 않았다. $K_d^A$가 확률 kernel인 것은 $K_dY_d^{m_d}=Y_{d-1}^{m_d}$에서 바로 나온다.

$d=L$에서 $K_L^A=(A/Y_{L-1})K_L$은 Gibbs 분포를 $A$로 재가중한 것이다($m_L=1$).
