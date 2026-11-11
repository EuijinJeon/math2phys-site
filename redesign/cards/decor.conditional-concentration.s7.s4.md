---
id: decor:conditional-concentration.s7.s4
kind: step
title: '점화식과 귀납의 완성'
uses: [decor:conditional-concentration.s1, decor:conditional-concentration.s2, decor:conditional-concentration.s4, decor:conditional-concentration.s7.s2, decor:conditional-concentration.s7.s3, decor:identity-error, decor:average-holder]
provides: 'decor:conditional-concentration의 결론'
math: |
  s7.s2를 $\mathcal A_{L,\eta}$로 평균하고 s7.s3을 $\gamma=1/4$로 쓴 뒤 $\limsup_N$을 취한다. 고정 $L$에서 $\mathcal A_{L,\eta}$는 유한 합이므로 decor:identity-error에 의해 $\limsup_N\mathcal A_{L,\eta}\le\mathcal A_{L,\eta}\limsup_N$이고, $C_{L,k,\eta}\varepsilon_{N,L,k}$ 항은 평균 뒤에도 사라진다. 또 $\limsup_N(\cdot)^{1/4}=(\limsup_N\cdot)^{1/4}$이다. $\mathcal A_{L,\eta}h_N\le(\mathcal A_{L,\eta}h_N^2)^{1/2}\le(C_k/L)^{1/2}$이고 $\varepsilon_{N,L,k}\to0$이므로, $L$이 크면
  $$V_{k,L}(\eta)\le C_{k,\eta}\bigl(L^{-1/2}+V_{k-1,L}(\eta/2)^{1/4}\bigr).$$
  $V_{k,L}$ 정의의 더 작은 모양들은 공분산이 1 이하이므로 우변에 흡수된다. 기저 $V_{1,L}(\eta)\le\delta/\eta$와 이 점화식에서, 모든 $\eta'$에 대해 $V_{k-1,L}(\eta')\to0$이면 $V_{k,L}(\eta)\to0$이다. 그러므로 모든 고정 $k,\eta$에 대해 $V_{k,L}(\eta)\to0$이고 명제가 증명된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [512, 524]}
status: proposed
---

흡수의 근거: 잎이 $k-1$ 이하인 모양의 항은 $V_{k-1,L}(\eta)\le V_{k-1,L}(\eta/2)\le V_{k-1,L}(\eta/2)^{1/4}$ (값이 $[0,1]$이고 x:decor-average-comparisons (iii)). $\limsup_N$과 유한 합 $\mathcal A_{L,\eta}$는 $\limsup_N\mathcal A\le\mathcal A\limsup_N$, 또 $\limsup_N(\cdot)^{1/4}=(\limsup_N\cdot)^{1/4}$로 다룬다. 귀납 단계마다 4제곱근이 들어가므로 정량적 속도는 매우 느리지만 진술은 정성적 극한만 주장한다.
