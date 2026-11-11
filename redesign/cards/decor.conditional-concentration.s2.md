---
id: decor:conditional-concentration.s2
kind: step
title: '기저: 잎 하나, $V_{1,L}(\eta)\le\delta/\eta$'
uses: [decor:conditional-concentration.s1, pert:tree-identity, tree:extension-expansion, decor:contractions, x:decor-mesh, x:decor-eta-regular]
provides: '귀납의 기저 (conditional-concentration.s7.s4)'
math: |
  singleton $S$와 $\eta$-regular $d$에 대해 각 고정 $L,d$에서 $v_N(S,d)\le\delta/\eta+o_N(1)$이다. 따라서 $V_{1,L}(\eta)\le\delta/\eta$.
physics: null
gap: null
abstraction: blackbox
children: [decor:conditional-concentration.s2.s1, decor:conditional-concentration.s2.s2]
source:
  - {file: decorrelation.tex, lines: [263, 291]}
status: proposed
---

**증명의 뼈대.** [[decor:conditional-concentration.s2.s1]]이 한 층 항등식 $\frac12\sum_{\ell=d}^{L-1}c_\ell\mathbb E(X-X_\ell)^2\le\delta+o_N(1)$을 준다. 좌변의 모든 항은 음이 아니다. $\ell=d$ 항만 남기면 [[decor:conditional-concentration.s2.s2]]에서 세 사본 부등식으로 $c_dv_N(S,d)\le\delta+o_N(1)$이 되고 $c_d\ge\eta$이다. 평균의 질량이 1 이하이므로 $V_{1,L}(\eta)\le\delta/\eta$.
