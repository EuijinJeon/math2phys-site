---
id: decor:overlap-concentration.s1
kind: step
title: 'singleton: 추가 color 없는 spin anchor'
uses: [pert:tree-identity, x:decor-spin-product]
provides: 'decor:overlap-concentration의 singleton 경우'
math: |
  singleton $S$에서 old tree를 $S$ 자신, spin anchor를 그 leaf, added color 없음, $f=R_S$로 둔 pert:tree-identity는 $\mathbb ER_S^2-(\mathbb ER_S)^2\to0$, 즉 각 고정 $L$에서 $\operatorname{Var}(R_S)\to0$을 준다.
physics: |
  자화 $R_S=N^{-1}\sum_i\sigma_i$는 self-average한다(disorder와 상태 선택에 대해 요동하지 않는다).
gap: |
  선택된 perturbed 수열을 따라서만, 각 고정 $L$에서 성립한다. 이 경우에는 깊이 평균이 필요 없다.
abstraction: approximation
children: []
source:
  - {file: decorrelation.tex, lines: [532, 536]}
status: proposed
---

빈 확장은 계수 1이고 spin anchor에서 $k=0$이면 $R_E=R_{\{a_*\}}=R_S$이다. 항등식 $\mathbb E[fR_S]-\mathbb Ef\,\mathbb ER_S\to0$에 $f=R_S$를 넣으면 된다.
