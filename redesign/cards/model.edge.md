---
id: model:edge
kind: definition
title: 'edge 분배함수 $C_\theta$ (2.5)'
uses: [x:model-message, model:integrability]
provides: 'model:ve. comparison.tex 181–192(bond 삽입이 $\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ 가 됨), upper.tex(edge 삽입)'
math: |
  $$C_\theta(x_1,\ldots,x_p)=\sum_{s\in\{-1,1\}^p}e^{\theta(s)}\prod_{\ell=1}^pq_{x_\ell}(s_\ell).\tag{2.5}$$
physics: |
  $p$ 개 spin이 각각 cavity field $x_\ell$ 의 분포 $q_{x_\ell}$ 를 독립으로 따를 때 factor 하나를 붙이는 분배함수, 곧 Bethe free entropy의 factor 항([[g:edge-term]])이다.
gap: |
  정의 자체는 같은 내용이다. 여기서 $x_\ell$ 들이 서로 다른 message label을 가져 독립이라는 것은 model:ve의 약속이다.
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [55, 58]}
status: proposed
---
