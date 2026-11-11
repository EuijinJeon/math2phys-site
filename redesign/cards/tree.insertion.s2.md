---
id: tree:insertion.s2
kind: step
title: 'edge 밀도비의 곱 → $W_{\mathcal T}(A)$'
uses: [tree:Y-recursion, x:tree-sampling]
provides: 'tree:insertion의 (tree:density)'
math: |
  (tree:updated-kernel)의 edge 밀도비를 tree 위에서 곱한다. 양의 깊이 $d$의 내부 vertex는 들어오는 edge에서 지수 $m_d$를, 나가는 edge들에서 지수 $-n_\beta m_{d+1}$를 받는다. root에는 들어오는 edge가 없고 이는 $m_0=0$과 맞는다. 각 말단 vertex는 지수 $m_L=1$을 받는다. 이것이 (tree:density)를 증명한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [126, 131]}
status: proposed
---

tree 법칙이 edge kernel들의 곱이라는 것은 자식이 prefix가 주어지면 독립으로 뽑힌다는 표본 규칙([[x:tree-sampling]])에서 온다(원문은 이 근거를 이 자리에서 다시 말하지 않는다). 깊이 $d$ vertex로 들어가는 edge의 비는 $(Y_d/Y_{d-1})^{m_d}$이고, 분모 $Y_{d-1}$은 부모 vertex의 값이다. 그래서 부모 $\beta$(깊이 $d_\beta$)는 자식 수만큼 $Y_\beta^{-m_{d_\beta+1}}$을 받는다. 말단에서 $Y_L=A$이므로 leaf 인자는 $A^a$다.
