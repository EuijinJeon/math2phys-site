---
id: model:ve
kind: definition
title: 'edge 항 $V_{\rm e}$ (2.9)'
uses: [model:edge, model:chain, model:integrability]
provides: 'model:functional의 $-\alpha(p-1)\mathbb E\log T_0V_{\rm e}$. upper:derivative, comparison.tex 181–192(bond 삽입)'
math: |
  $\theta$ (model:vs와 같은 줄에서 잡은 독립 사본)와 서로 다른 label의 message $x_1,\ldots,x_p$ 에 대해
  $$V_{\rm e}=C_\theta(x_1,\ldots,x_p).\tag{2.9}$$
physics: |
  $p$ 개의 독립 cavity field 아래 factor 하나를 붙이는 분배함수, Bethe free entropy의 factor 항([[g:edge-term]])이다.
gap: |
  정의는 같은 내용이다.
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [82, 83]}
  - {file: model.tex, lines: [88, 89]}
status: proposed
---
