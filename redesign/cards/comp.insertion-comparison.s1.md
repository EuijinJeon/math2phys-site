---
id: comp:insertion-comparison.s1
kind: step
title: 'trial 삽입과 정확한 trial 항등식'
uses: [cavity:increment, comp:encoding, comp:encoding.s4, tree:Y-recursion, model:chain, model:vs, model:ve, model:power-means, model:functional, cavity:grid]
provides: 'comp:insertion-comparison.s2–s4 (비교할 두 쪽과 trial 쪽의 값 $\mathcal B_{L-1}$)'
math: |
  cavity:increment의 각 삽입에서 그 site label의 reservoir spin을 comp:encoding의 독립 spin 과정으로 바꾼다. 그렇게 얻은 trial 삽입을 $\widetilde A_{\rm s}$, $\widetilde A_{\rm b}$, (tree:Y-recursion)의 recursion을 $\widetilde Y_{0,\rm s}$, $\widetilde Y_{0,\rm b}$ 로 쓴다. 이 recursion은 trial kernel을 쓴다. 그러면 $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$ 이고
  $$\mathbb E\log\widetilde Y_{0,\rm b}=\alpha(p-1)\mathbb E\log T_0V_{\rm e},\qquad\log2+\mathbb E\log\widetilde Y_{0,\rm s}-\mathbb E\log\widetilde Y_{0,\rm b}=\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)}).$$
  (5.5)에 의해 남은 일은 reservoir와 trial의 삽입 logarithm을 주어진 극한에서 비교하는 것이다.
physics: |
  이웃 spin들을 서로 독립인 계층 [[g:message|cavity field]] 사본으로 바꾼 site 삽입은 정확히 [[g:site-term|site 항]] $T_0V_{\rm s}$ 이고, bond 삽입은 Poisson$(\alpha(p-1))$ 개의 독립 [[g:edge-term|edge 항]]으로 갈라진다. 그래서 바꾼 증분은 시행 [[g:functional|functional]] 그 자체다.
gap: |
  정확한 계산이다. "독립 사본"은 구성상 독립이다(comp:encoding.s4). 이것이 실제 reservoir의 증분과 같다는 것은 이 단계가 아니라 s2–s4의 극한 비교다.
abstraction: exact
children: [comp:insertion-comparison.s1.s1, comp:insertion-comparison.s1.s2, comp:insertion-comparison.s1.s3]
source:
  - {file: comparison.tex, lines: [170, 196]}
status: proposed
---

**뼈대.** [[comp:insertion-comparison.s1.s1]] 바꾸기와 표기, [[comp:insertion-comparison.s1.s2]] site 쪽 $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$, [[comp:insertion-comparison.s1.s3]] bond 쪽의 인수분해와 $\mathcal B_{L-1}$.
