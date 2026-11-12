---
id: comp:insertion-comparison.s1.s2
kind: step
title: 'site 쪽: $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$'
uses: [comp:insertion-comparison.s1.s1, model:vs, model:site-message, model:power-means, tree:Y-recursion, cavity:grid]
provides: 'comp:insertion-comparison.s1.s3 (site 항)'
math: |
  terminal spin 전이에서 $\widetilde A_{\rm s}$ 를 그 독립 trial spin에 대해 평균하면 정확히 (2.8)의 $V_{\rm s}$ 가 된다. 그러므로 $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$ 이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [178, 180]}
status: proposed
---

**확인 (작성자).** $m_L=1$ 이므로 recursion의 첫 걸음 $\widetilde Y_{L-1}=K_L\widetilde A_{\rm s}$ 는 terminal spin에 대한 보통 기대값이다. trial spin $\tau^{j,\ell}\sim q_{x_\ell^j}$ 가 서로 독립이므로
$$\mathbb E_\tau\exp\Bigl(\sum_j\theta_j(\tau^{j,1},\ldots,\tau^{j,p-1},\varepsilon)\Bigr)=\prod_j\sum_{s}e^{\theta_j(s,\varepsilon)}\prod_\ell q_{x_\ell^j}(s_\ell)=\exp\Bigl(\sum_jU_{\theta_j}(x_1^j,\ldots,x_{p-1}^j;\varepsilon)\Bigr),$$
그리고 $\frac12\sum_\varepsilon e^{h\varepsilon}$ 를 곱하면 (2.8)이다([[model:site-message]], [[model:vs]]). 그 위의 걸음 $\widetilde Y_{d-1}=(K_d\widetilde Y_d^{m_d})^{1/m_d}$ ($d=r,\ldots,1$, $m_d=d/L$)는 (2.10)의 $T_{d-1}$ 과 같은 꼴이다: 조건부 기대값이 깊이 $d$ 의 사슬 변수만 적분하고 물리 disorder는 고정된다([[model:power-means]]). 그래서 $\widetilde Y_0=T_0V_{\rm s}$ 이고 지수열은 $\mathbf m^{(L)}$ 이다.
