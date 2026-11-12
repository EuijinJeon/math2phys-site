---
id: pert:score-identity
kind: lemma
title: 'anchor score와 시험함수의 분리 부등식 (6.13)'
uses: [x:pert-test-setup, pert:error, pert:score, pert:factor, x:pert-selected-limits, pert:selection]
provides: 'pert:palm.s2 ((6.16)은 (6.13)에서 나옴)'
math: |
  (6.4)는 각 고정 type $\nu$ 에 대해
  $$\left|\frac{\mathbb E[fD_\nu^{a_*}]-\mathbb Ef\,\mathbb E\langle D_\nu\rangle}{c_\nu s_N}\right|\le\|f\|_\infty e_{\nu,N}\longrightarrow0$$
  을 함의한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [321, 329]}
status: proposed
---

풀이(작성자). $D_\nu^{a_*}$ 는 anchor path 위에서 계산한 score다. $\mathbb E[fD^{a_*}_\nu]-\mathbb Ef\,\mathbb E\langle D_\nu\rangle=\mathbb E[f(D_\nu^{a_*}-\mathbb E\langle D_\nu\rangle)]$ 이고 $|f|\le\|f\|_\infty$ 이며, anchor marginal이 tilted path 하나이므로 $\mathbb E|D_\nu^{a_*}-\mathbb E\langle D_\nu\rangle|=\mathbb E_{\mathbf u}\langle|D_\nu-\mathbb E_{\mathbf u}\langle D_\nu\rangle|\rangle$ 이다([[x:pert-test-setup]]). 부등식 자체는 모든 $N$ 과 $\mathbf u$ 에서 성립하고, "$\to0$"은 [[pert:selection]] (ii)를 따른 것이다([[x:pert-selected-limits]]). 이 카드는 원문의 정리류 환경이 아니라 본문의 식이지만 다른 증명이 인용하므로 따로 둔다.
