---
id: decor:overlap-concentration.s4
kind: step
title: '분산 추정 $\limsup_N\mathcal A\operatorname{Var}(R_S)\le C_k(L^{-1}+V_{k-1,L}^{1/2})$'
uses: [decor:overlap-concentration.s2, decor:overlap-concentration.s3, decor:conditional-concentration.s1, decor:conditional-concentration.s7.s3, decor:conditional-concentration, x:decor-average-comparisons, decor:average-holder, decor:identity-error]
provides: 'decor:overlap-concentration.s5'
math: |
  조건부 기대값이 최적 $L^2$ 사영이므로 $\mathbb E(R_S-M)^2\le\mathbb E(R_S-G_-)^2\le2p_N(S,e)^2+2\mathbb E(G-G_-)^2$이다. 분산 분해 $\operatorname{Var}(R_S)=\mathbb E(R_S-M)^2+\operatorname{Var}(M)$와 s2, s3, 그리고 고정 $L$에서 유한 합인 $\mathcal A_{L,\eta}$와 $\limsup_N$의 교환(decor:identity-error: 각 고정 배정에서 $\operatorname{Var}(M)\to0$이므로 $\limsup_N\mathcal A_{L,\eta}\operatorname{Var}(M)=0$)에서, $L$이 충분히 크면
  $$\limsup_{N\to\infty}\mathcal A_{L,\eta}\operatorname{Var}(R_S)\le C_k\bigl(L^{-1}+V_{k-1,L}(\eta/2)^{1/2}\bigr).$$
  여기서 $p_N(S,e)^2\le s\sum_jv_N(T_j,e)^{1/2}$와 fiber bound(conditional-concentration.s7.s3)를 $\gamma=1/2$로 쓴다. 이번에는 $d$가 없으므로 전체 평균은 $D=b(S)$개 좌표, 자식 항은 여전히 $D_j=b(T_j)+1$개 좌표를 쓴다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [591, 609]}
status: proposed
---

$G_-$는 $\mathscr F_{e-1}$-가측인 후보이므로 $M$보다 $R_S$에 가까울 수 없다. 이것이 $e$의 사영과 $e-1$의 조건부 평균을 잇는 다리다. $\operatorname{Var}(M)\to0$은 각 고정 배정에서 성립하고 고정 $L$에서 $\mathcal A_{L,\eta}$는 유한 합이므로 평균 후에도 $\limsup_N$이 0이다. 자식 항의 좌표 $(e,\mathbf q|_{T_j})$는 $\eta$-regular 배정의 부분이므로 $\eta$-regular이고, 따라서 $\eta/2$-regular다. 즉 $e$가 $T_j$의 "첫 갈라짐 앞 추가 깊이" 역할을 한다.
