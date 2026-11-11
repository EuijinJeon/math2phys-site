---
id: x:model-cavity-bounds
kind: remark
title: '$\lvert\log C_\theta\rvert,\ \lvert U_\theta\rvert\le B(\theta)$'
uses: [model:edge, model:site-message, model:integrability]
provides: 'model:trial-bounds의 재료. upper.tex와 reduction:stability(각 cavity 상호작용과 edge 로그가 sup-norm 차이만큼만 변함)'
math: |
  $\lvert\log C_\theta\rvert$ 와 $\lvert U_\theta\rvert$ 는 message에 대해 균일하게 $B(\theta)$ 이하이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: model.tex, lines: [65, 66]}
status: proposed
---

원문은 근거를 적지 않는다. 확인(작성자가 보탠 것): $C_\theta$ 와 $e^{U_\theta}$ 는 각각 확률 가중치 $\prod_\ell q_{x_\ell}(s_\ell)$(합이 1)로 $e^{\theta(s)}$ 를 평균한 것이고 $e^{-B(\theta)}\le e^{\theta(s)}\le e^{B(\theta)}$ 이므로 두 값이 $[e^{-B(\theta)},e^{B(\theta)}]$ 안에 있다.
