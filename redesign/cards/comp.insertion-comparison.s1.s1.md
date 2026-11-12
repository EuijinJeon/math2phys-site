---
id: comp:insertion-comparison.s1.s1
kind: step
title: 'reservoir spin을 trial spin 과정으로 바꾸기: $\widetilde A$, $\widetilde Y_0$'
uses: [cavity:increment, comp:encoding, comp:encoding.s4, tree:Y-recursion, x:tree-path-kernels, model:chain, cavity:grid]
provides: 'comp:insertion-comparison.s1.s2, s1.s3, s2'
math: |
  cavity:increment의 각 삽입($A_{\rm s}$, $A_{\rm b}$)에서 그 site label의 reservoir spin을 comp:encoding의 독립 spin 과정으로 바꾼다. 결과를 trial 삽입 $\widetilde A_{\rm s}$, $\widetilde A_{\rm b}$ 라 하고, (tree:Y-recursion)으로 계산한 그 recursion을 $\widetilde Y_{0,\rm s}$, $\widetilde Y_{0,\rm b}$ 라 한다. 이 recursion은 trial kernel을 쓴다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [170, 176]}
status: proposed
---

**trial kernel의 뜻 (작성자 읽기).** label $\omega$ 마다 사슬 $\eta_0^\omega\sim\zeta_{L,N}$, $\eta_{d+1}^\omega\mid\eta_d^\omega\sim\eta_d^\omega$, $x^\omega\mid\eta_{r-1}^\omega\sim\eta_{r-1}^\omega$ ([[model:chain]], $r=L-1$)와 깊이 $L$ 의 terminal spin $\tau^\omega\sim q_{x^\omega}$ 를 둔다. 모든 label의 깊이 $d$ 변수를 묶은 것이 path의 깊이 $d$ 변수이고([[x:tree-path-kernels]]: $\eta_d$ 는 깊이 $d$, $x$ 는 깊이 $r$), root는 $\eta_0^\omega$ 들과 insertion의 물리 disorder다. 지수는 [[cavity:grid]]의 $m_d=d/L$ 이다. 원문은 "These recursions use the trial kernels"라고만 적는다. reservoir 쪽 recursion은 [[cavity:increment]]대로 tilted reservoir kernel과 독립인 새 root disorder를 쓴다.

바꾸는 것은 site label에 붙은 spin뿐이다. 개수 $K_{\rm s},K_{\rm b}$, 상호작용 $\theta_j$, 장 $h$ 는 그대로 두고, label마다 독립 사본을 쓴다(서로 다른 index가 같은 site를 가리켜도 trial 쪽에서는 독립 label이다; 작성자 읽기, 원문 "independent spin processes"). label들이 새 물리 disorder와 독립인 것은 [[comp:encoding.s4]].
