---
id: decor:conditional-concentration.s4
kind: step
title: '두 target 측의 사영'
uses: [decor:conditional-concentration.s3, decor:projection-bound, decor:depth-continuity, x:decor-product-difference, x:decor-tree-sampling]
provides: 'conditional-concentration.s5 (사영된 벡터 a, b, b_ℓ), s6 (오차 2p_N(S^+,e+1)+h_N(S)), s7.s4 (A h_N^2 ≤ C_k/L)'
math: |
  모든 허용 확장 $E$에서 target overlap $R_E$와, 두 target 측 stem 위에서 계산한 $a_{S,e}$ 두 개의 축약 $P_E$의 차이는 $L^2$에서 $2p_N(S^+,e+1)+h_N(S)$ 이하다. 여기서 $h_N(S)\ge0$는 확장 $E$에 무관한 양이고 $L$이 크면 $\mathcal A_{L,\eta}h_N(S)^2\le C_k/L$이다. target I의 사영 벡터는 old I의 $a:=a_{S,e}$와 같다. old II의 $a_{S,e}$를 $b$로 쓴다.
physics: null
gap: null
abstraction: blackbox
children: [decor:conditional-concentration.s4.s1, decor:conditional-concentration.s4.s2]
source:
  - {file: decorrelation.tex, lines: [361, 385]}
status: proposed
---

**증명의 뼈대.** [[decor:conditional-concentration.s4.s1]]: target은 marginal로 $d$에서 분리된 $S^+$ 두 사본이므로 projection-bound로 $e+1$에서 사영하고, depth-continuity로 자식 깊이와 평가 깊이를 되돌린다. [[decor:conditional-concentration.s4.s2]]: 되돌리는 비용 $h_N$은 단일 사본 marginal에만 의존하므로 확장에 균등하다. target I은 anchor의 prefix를 공유하므로 그 사영 벡터는 $a$다.
