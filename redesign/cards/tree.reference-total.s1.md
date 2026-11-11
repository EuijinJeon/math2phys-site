---
id: tree:reference-total.s1
kind: step
title: '한 걸음 합 $m_d-jm_{d+1}$'
uses: [x:tree-extension-history, tree:telescoping]
provides: 'tree:reference-total의 (tree:one-reference-total), tree:reference-total.s2'
math: |
  지정된 갈라짐 vertex에서 전체 현재 tree의 자식 수를 $n$이라 하자. 제외되는 $j$개 자식이 그 vertex를 지나는 모든 reference를 담는다. 나머지 $n-j$개 자식은 각각 reference가 없는 부분 tree의 뿌리다. 그 말단 vertex는 따라서 쓰지 않은 old leaf다. 그런 부분 tree가 깊이 $d+1$에 뿌리를 두면 허용되는 선택은 계수 $1$의 old leaf, 또는 부분 tree 안 내부 vertex에서의 fresh divergence다. leaf가 $q$개이면 그 안의 망원 합이
  $$q+\sum_{\beta\text{ internal in the subtree}}(m_{d_\beta}-n_\beta m_{d_\beta+1})=m_{d+1}$$
  을 준다. 이 공식은 자식이 말단인 경우(양변이 $1$)도 포함한다. 이 기여들을 지정 vertex에서의 fresh 선택에 더하면
  $$m_d-nm_{d+1}+(n-j)m_{d+1}=m_d-jm_{d+1}.$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [359, 375]}
status: proposed
---

부분 tree 망원 합은 [[tree:telescoping]]을 깊이 $d+1$의 vertex를 뿌리로 하는 부분 tree에 적용한 판이다(작성자 확인: 뿌리 아닌 vertex의 $m$ 합에서 내부 vertex의 $m$ 합을 빼면 $q-m_{d+1}$). 원래 항등식은 root가 깊이 0이라 $m_0=0$이 빠졌지만 여기서는 뿌리의 $m_{d+1}$이 남는다.

"그 말단 vertex는 쓰지 않은 old leaf"인 이유: color를 받은 leaf와 anchor는 모두 reference이고, 그것들은 제외된 $j$개 자식 안에 있다.
