---
id: reduction:stability.s3
kind: step
title: '상수 이동 (reduction:shift)'
uses: [model:hamiltonian, model:site-message, model:edge, model:vs, model:ve, model:power-means, model:functional, x:model-depth-zero, model:integrability, x:reduction-power-mean-scaling]
provides: 'reduction:stability의 셋째 주장'
math: |
  (reduction:shift)에 대해: 물리 상수는 spin 분배함수와 모든 power mean 밖으로 나온다. functional에서 site 항은 $-\alpha p\mathbb Ec$ 만큼 이동하고 edge 항은 $+\alpha(p-1)\mathbb Ec$ 를 보태므로 알짜 이동은 $-\alpha\mathbb Ec$ 다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: reduction.tex, lines: [38, 43]}
status: proposed
---

**풀이 (작성자).** pressure: $-\widehat H_N=-H_N-\sum_{k\le M_N}c_k$ 이고 $\sum_kc_k$ 는 spin에 무관하므로 $\log\widehat Z_N=\log Z_N-\sum_{k\le M_N}c_k$, $\widehat F_N=F_N-\frac1N\mathbb E\sum_{k\le M_N}c_k=F_N-\alpha\mathbb Ec$. 시행 쪽: $U_{\widehat\theta}=U_\theta-c$, $C_{\widehat\theta}=e^{-c}C_\theta$ 이므로 $\widehat V_{\rm s}=e^{-\sum_{j\le k}c_j}V_{\rm s}$, $\widehat V_{\rm e}=e^{-c}V_{\rm e}$. 상수가 물리 disorder만의 함수라 [[x:reduction-power-mean-scaling]] (b)로 $T_0$ 밖으로 나오고, $\mathbb E\log T_0\widehat V_{\rm s}=\mathbb E\log T_0V_{\rm s}-\alpha p\mathbb Ec$, $-\alpha(p-1)\mathbb E\log T_0\widehat V_{\rm e}=-\alpha(p-1)\mathbb E\log T_0V_{\rm e}+\alpha(p-1)\mathbb Ec$. 합 $-\alpha\mathbb Ec$. $\mathbb E\lvert c\rvert<\infty$ 가 이 기대값들과 $\widehat\theta$ 의 (2.1)을 보장한다.
