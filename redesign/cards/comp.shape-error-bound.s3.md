---
id: comp:shape-error-bound.s3
kind: step
title: 'Cauchy–Schwarz와 유한 합으로 (comp:shape-error-bound)'
uses: [comp:shape-error-bound.s1, comp:shape-error-bound.s2, decor:average-definition, x:decor-spin-product]
provides: 'comp:shape-error-bound의 결론'
math: |
  Cauchy–Schwarz가 평균 절대 편차의 그 평균을 $\bigl(\mathcal A_{L,\eta}\operatorname{Var}(R_U)\bigr)^{1/2}$ 로 누른다. 유한 개의 topology와 부분집합에 대해 더하고, regular가 아닌 tree에서는 각 편차를 2로 누르면 (comp:shape-error-bound)가 증명된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [149, 153]}
status: proposed
---

Cauchy–Schwarz의 두 번 (작성자 풀이): $\mathbb E\lvert R_U-\mathbb ER_U\rvert\le\operatorname{Var}(R_U)^{1/2}$, 그리고 [[decor:average-definition]]의 질량 $\mathcal A_{L,\eta}1\le1$ 로 $\mathcal A_{L,\eta}(w^{1/2})\le(\mathcal A_{L,\eta}w)^{1/2}(\mathcal A_{L,\eta}1)^{1/2}\le(\mathcal A_{L,\eta}w)^{1/2}$. $\operatorname{Var}(R_U)$ 는 고정 깊이 배정에서 root와 tree 표본추출을 포함한 분산이다([[x:decor-spin-product]]). 같은 $U$ 가 여러 $(\tau,S)$ 에서 나오는 중복은 유한하므로 $C_k$ 에 흡수된다.
