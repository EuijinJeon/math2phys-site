---
id: decor:conditional-concentration.s7
kind: step
title: '귀납 닫기: 점화식 $V_{k,L}\le C(L^{-1/2}+V_{k-1,L}^{1/4})$'
uses: [decor:conditional-concentration.s1, decor:conditional-concentration.s2, decor:conditional-concentration.s4, decor:conditional-concentration.s6, decor:projection-bound, decor:contractions, decor:identity-error, decor:average-holder, x:decor-average-comparisons]
provides: 'decor:conditional-concentration의 결론. fiber bound (s7.s3)는 overlap-concentration.s4가 다시 쓴다'
math: |
  $L$이 충분히 크면 $V_{k,L}(\eta)\le C_{k,\eta}\bigl(L^{-1/2}+V_{k-1,L}(\eta/2)^{1/4}\bigr)$. 이것과 $V_{1,L}(\eta)\le\delta/\eta$에서 귀납으로 모든 고정 $k,\eta$에 대해 $V_{k,L}(\eta)\to0$ ($L\to\infty$).
physics: null
gap: null
abstraction: blackbox
children: [decor:conditional-concentration.s7.s1, decor:conditional-concentration.s7.s2, decor:conditional-concentration.s7.s3, decor:conditional-concentration.s7.s4]
source:
  - {file: decorrelation.tex, lines: [459, 524]}
status: proposed
---

**증명의 뼈대.** [[decor:conditional-concentration.s7.s1]]: s6의 $f$를 $a\cdot b$로 바꾸면 좌변이 음이 아닌 $\frac12\sum c_\ell\mathbb E(a\cdot b-a\cdot b_\ell)^2$가 되고, $\ell=d$ 항이 $C_\eta(\delta+p_N(S,e)+|\rho_N|)$로 눌린다. [[decor:conditional-concentration.s7.s2]]: 세 사본 부등식과 사영으로 $v_N(S,d)\le C_{k,\eta}(\delta+p_N(S,e)+p_N(S^+,e+1)+h_N(S))+C_{L,k,\eta}\varepsilon_{N,L,k}$. [[decor:conditional-concentration.s7.s3]]: 자식 항의 깊이 평균은 단일 사본 평균으로 눌린다(fiber bound). [[decor:conditional-concentration.s7.s4]]: $\gamma=1/4$로 평균하고, 고정 $L$에서 유한 합인 $\mathcal A_{L,\eta}$와 $\limsup_N$을 바꾸어(항등식 오차 항이 평균 뒤에도 사라진다) 점화식을 얻고 귀납을 닫는다.
