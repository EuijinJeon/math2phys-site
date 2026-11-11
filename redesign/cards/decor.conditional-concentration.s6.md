---
id: decor:conditional-concentration.s6
kind: step
title: '사영된 항등식과 오차 $\rho_N$'
uses: [decor:conditional-concentration.s3, decor:conditional-concentration.s4, decor:conditional-concentration.s5, pert:tree-identity, decor:identity-error, decor:projection-bound]
provides: 'decor:conditional-concentration.s7'
math: |
  $$\sum_{\ell=d}^{e-1}c_\ell\,\mathbb E\bigl[f(a\cdot b-a\cdot b_\ell)\bigr]=\delta\bigl(\mathbb E[f(a\cdot b)]-\mathbb Ef\,\mathbb ER_{\rm target}\bigr)+\rho_N(S,d),$$
  여기서 $R_{\rm target}$은 anchor 혼자인 확장의 target overlap이고 $|R_{\rm target}|\le1$이다. 이 식은 pert:tree-identity의 이 사례 $\sum_Ec_E\mathbb E[fR_E]-\mathbb Ef\cdot(-\delta J\,\mathbb ER_{\rm target})=O(\varepsilon_{N,L,k})$에서 나온다. 둘째 항은 s5의 사실(anchor 혼자인 쪽의 모든 확장이 같은 법칙의 target을 주고 총 계수가 $-\delta J$)로 묶인 것이고, 첫째 항의 $R_E$를 s4의 사영 $P_E$로 바꾼 뒤 s5의 class별 표를 쓰고 $J$로 나눈다. 오차는
  $$|\rho_N(S,d)|\le C_{k,\eta}\bigl(p_N(S^+,e+1)+h_N(S)\bigr)+C_{L,k,\eta}\,\varepsilon_{N,L,k}.$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [434, 458]}
status: proposed
---

pert:tree-identity를 이 사례에 쓰면 $\sum_Ec_E\mathbb E[fR_E]+\delta J\,\mathbb Ef\,\mathbb ER_{\rm target}$이 오차 $\varepsilon_{N,L,k}$ 안에서 0이다([[g:anchor|anchor]] 혼자인 쪽은 모든 확장이 같은 법칙의 target을 주고 총 계수가 $-\delta J$, s5의 `math`). 각 $R_E$를 [[g:projection|사영]]된 $P_E$로 바꾸는 비용은 $|f|\le1$이므로 $\|R_E-P_E\|_{L^2}\le2p_N(S^+,e+1)+h_N(S)$이다. 이것을 절댓값 계수로 합하고 $|J|$로 나누면 상대 비용 상계 $C_{k,\eta}$가 붙는다. 사영된 항은 s5의 표로 $-\sum c_\ell J\,\mathbb E[f\,a\cdot b_\ell]+m_eJ\,\mathbb E[f\,a\cdot b]$가 된다. $J$로 나누고 $m_e=\sum c_\ell-\delta$로 정리하면 위 식이다. 원래 항등식 오차를 $J$로 나눈 항은 $L$에 의존하는 상수를 갖지만 고정 $L$에서 0으로 간다.
