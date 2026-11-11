---
id: decor:conditional-concentration.s7.s1
kind: step
title: '$f$를 $a\cdot b$로 바꾸어 음이 아닌 세 사본 양 얻기'
uses: [decor:conditional-concentration.s6, decor:conditional-concentration.s5, decor:projection-bound, x:decor-eta-regular]
provides: 'decor:conditional-concentration.s7.s2'
math: |
  decor:projection-bound에서 $\|f-a\cdot b\|_{L^2}\le2p_N(S,e)$이고 $\sum_{\ell=d}^{e-1}c_\ell=(e+1)\delta\le1$이다. 그래서 s6의 좌변에서 $f$를 $a\cdot b$로 바꾸는 비용은 $4p_N(S,e)$ 이하이고, 각 $a\cdot b_\ell$이 $a\cdot b$와 같은 marginal law를 가지므로 바뀐 좌변은 $\frac12\sum_{\ell=d}^{e-1}c_\ell\mathbb E(a\cdot b-a\cdot b_\ell)^2$이다. 각 항은 음이 아니고 $c_d\ge\eta$, s6의 우변은 절댓값이 $2\delta+|\rho_N(S,d)|$ 이하이므로
  $$\mathbb E(a\cdot b-a\cdot b_d)^2\le C_\eta\bigl(\delta+p_N(S,e)+|\rho_N(S,d)|\bigr).$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [459, 479]}
status: proposed
---

s2의 기저와 같은 구조다. $f$를 [[g:projection|사영]]된 [[g:multioverlap|overlap]] 자신으로 바꾸면 $\mathbb E[x(x-y)]=\frac12\mathbb E(x-y)^2$ (같은 marginal의 $x,y$)로 부호 있는 합이 음이 아닌 합이 된다. $(a,b_\ell)$은 $d$에서 갈라진 두 stem 위의 $a_{S,e}$이므로 $(a,b)$와 같은 법칙이다. 비용 $4p_N$은 $|a\cdot b-a\cdot b_\ell|\le2$와 $L^1\le L^2$에서 온다.
