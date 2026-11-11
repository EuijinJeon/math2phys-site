---
id: decor:conditional-concentration.s5.s3
kind: step
title: 'class별 계수 합 ($-c_\ell J$, $m_eJ$)'
uses: [decor:conditional-concentration.s5.s1, decor:conditional-concentration.s3.s2, tree:reference-total, x:decor-mesh]
provides: 'decor:conditional-concentration.s6'
math: |
  tree:reference-total에 의해, 첫 경로의 각 선택마다 나중 target II color들의 계수를 거꾸로 합하면 $\kappa(S^+)$이고, target I color들의 계수 합은 또 하나의 $\kappa(S^+)$이다. 그래서 class $\ell$의 총 계수는 $-c_\ell J$이다. 기준 모양 전체의 계수는 $(m_d-m_{d+1})\kappa(S^+)^2=-\delta J$이고 이는 old tree에서나 anchor 혼자에서나 같다. $\sum_{\ell=d}^{e-1}c_\ell=(e+1)\delta=m_e+\delta$이므로 나머지 class "old prefix through $e$"의 총 계수는 $-\delta J+(m_e+\delta)J=m_eJ$이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [414, 433]}
status: proposed
---

tree:reference-total의 핵심은 한 걸음 계수 합이 현재 reference tree에만 의존하고 어떤 old 경로나 fresh 경로가 그것을 실현했는지에 무관하다는 것이다. 그래서 class를 고정하면 나머지 color들의 합이 곱 인자 $\kappa(S^+)$로 떨어진다. 남은 class의 계수는 직접 세지 않고 전체에서 뺀다. 확인: $\sum c_\ell=(d+2)\delta+(e-1-d)\delta=(e+1)\delta$.
