---
id: decor:overlap-concentration.s1
kind: step
title: 'singleton: 추가 color 없는 spin anchor'
uses: [pert:tree-identity, x:decor-spin-product]
provides: 'decor:overlap-concentration의 singleton 경우'
math: |
  singleton $S$에서 old tree를 $S$ 자신, spin anchor를 그 leaf, added color 없음, $f=R_S$로 둔 pert:tree-identity는 $\mathbb ER_S^2-(\mathbb ER_S)^2\to0$, 즉 각 고정 $L$에서 $\operatorname{Var}(R_S)\to0$을 준다.
physics: |
  자화 $R_S=N^{-1}\sum_i\sigma_i$는 [[g:self-average|self-average]]한다(root와 그 leaf의 표본추출에 대해 요동하지 않는다).
gap: |
  [[g:selected-sequence|선택된 수열]]을 따라서만, 각 고정 $L$에서 성립한다. 이 경우에는 [[g:depth-average|깊이 평균]]이 필요 없다.
abstraction: approximation
children: []
source:
  - {file: decorrelation.tex, lines: [532, 536]}
status: proposed
---

빈 확장은 계수 1이고 [[g:anchor|spin anchor]]에서 $k=0$이면 $R_E=R_{\{a_*\}}=R_S$이다. 항등식 $\mathbb E[fR_S]-\mathbb Ef\,\mathbb ER_S\to0$에 $f=R_S$를 넣으면 된다.
