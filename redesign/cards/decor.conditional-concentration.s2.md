---
id: decor:conditional-concentration.s2
kind: step
title: '기저: 잎 하나, $V_{1,L}(\eta)\le\delta/\eta$'
uses: [decor:conditional-concentration.s1, pert:tree-identity, tree:extension-expansion, decor:contractions, x:decor-mesh, x:decor-eta-regular]
provides: '귀납의 기저 (conditional-concentration.s7.s4)'
math: |
  singleton $S$와 $\eta$-regular $d$에 대해 각 고정 $L,d$에서 $v_N(S,d)\le\delta/\eta+o_N(1)$이다. 따라서 $V_{1,L}(\eta)\le\delta/\eta$.
physics: |
  고정 $L$에서, 깊이 $d$ ($d/L\in(\eta,1-\eta)$)의 각 상태 안에서 단일 spin의 connected correlation $\langle\sigma_i\sigma_j\rangle_d-\langle\sigma_i\rangle_d\langle\sigma_j\rangle_d$의 제곱을 site 쌍에 대해 평균한 양은 $N\to\infty$에서 $1/(\eta L)$ 이하다. 깊이 평균 없이 각 깊이에서 성립한다는 점에서 부모 명제(깊이 평균)보다 강한 정보다.
gap: |
  (1) "상태"는 perturbed reservoir의 보조 계층 prefix $\mathscr F_d$(root 포함)이고 $\langle\cdot\rangle_d$는 그 prefix에 대한 조건부 기대값이다. 물리적 pure state가 아니다. (2) 성립하는 것은 선택된 수열을 따른 고정 $L$의 $\limsup_N$이고, 상계 $1/(\eta L)=\delta/\eta$는 $L\to\infty$에서만 0이 된다. 고정 $L$에서는 clustering이 완전하다고 말하지 않는다. (3) $N^{-2}\sum_{ij}\operatorname{Cov}^2$의 $L^2$ 평균 의미이고, 상태와 disorder에 대해서도 평균한다. (4) $\eta$-regular $d$, 즉 경계 근처 깊이를 뺀 깊이에서만이다. 상계는 $c_d=(d+2)\delta\ge\eta$에 기대므로 $\eta$가 작을수록 약하다.
abstraction: approximation
children: [decor:conditional-concentration.s2.s1, decor:conditional-concentration.s2.s2]
source:
  - {file: decorrelation.tex, lines: [263, 291]}
status: proposed
---

**증명의 뼈대.** [[decor:conditional-concentration.s2.s1]]이 한 층 항등식 $\frac12\sum_{\ell=d}^{L-1}c_\ell\mathbb E(X-X_\ell)^2\le\delta+o_N(1)$을 준다. 좌변의 모든 항은 음이 아니다. $\ell=d$ 항만 남기면 [[decor:conditional-concentration.s2.s2]]에서 세 사본 부등식으로 $c_dv_N(S,d)\le\delta+o_N(1)$이 되고 $c_d\ge\eta$이다. 평균의 질량이 1 이하이므로 $V_{1,L}(\eta)\le\delta/\eta$.
