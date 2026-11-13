---
id: model:site-message
kind: definition
title: 'cavity log-weight $U_\theta$ (2.6)'
uses: [x:model-message, model:integrability]
provides: 'model:vs. upper.tex의 cavity 상호작용 $U_\theta(x_1,\ldots,x_{p-1};\sigma_i)$'
math: |
  $\varepsilon\in\{-1,1\}$ 에 대해
  $$U_\theta(x_1,\ldots,x_{p-1};\varepsilon)=\log\sum_{s\in\{-1,1\}^{p-1}}e^{\theta(s_1,\ldots,s_{p-1},\varepsilon)}\prod_{\ell=1}^{p-1}q_{x_\ell}(s_\ell).\tag{2.6}$$
  새 spin $\varepsilon$ 은 $\theta$ 의 마지막($p$ 번째) 좌표에 놓인다.
physics: |
  새 spin을 상호작용의 마지막 좌표에 두고 나머지 $p-1$ 개 spin이 cavity field 분포 $q_{x_\ell}$ 를 독립으로 따를 때 factor 하나가 새 spin $\varepsilon$ 에 주는 log-weight, 곧 factor→spin cavity bias([[g:site-term]]의 $U_\theta$)이다.
gap: |
  물리의 $u$-message는 보통 $U_\theta(\cdot;+1)-U_\theta(\cdot;-1)$ 의 절반을 field로 쓴다. 여기서는 두 값을 그대로 둔다. 새 spin을 마지막 좌표에 두는 것은 일반 $\theta$ 에서 좌표를 고르는 약속이고, 순열 불변인 $\theta$ 에서는 어느 좌표든 법칙이 같다(작성자의 관찰).
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [59, 64]}
status: proposed
---
