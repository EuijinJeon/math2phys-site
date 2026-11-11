---
id: decor:conditional-concentration
kind: proposition
title: '조건부 decorrelation: $\mathcal A_{L,\eta}v_N(S,d)\to0$'
uses: [decor:covariance-definition, decor:average-definition, x:decor-eta-regular, x:decor-limit-order, x:decor-mesh, pert:tree-identity, tree:extension-expansion, tree:reference-total, tree:charging, decor:contractions, decor:projection-bound, decor:depth-continuity, decor:identity-error, decor:average-holder, x:decor-average-comparisons]
provides: 'decor:overlap-concentration.s4-s5 (V_{k-1,L}(η/2)→0으로 상태 안 분산을 지움). fiber bound (s7.s3)는 overlap-concentration.s4가 다시 쓴다. relative-absolute-cost (s3.s3)는 decor:order-of-limits가 가리킨다'
math: |
  모든 고정 labeled topology $S$와 모든 $\eta>0$에 대해
  $$\lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}v_N(S,d)=0.$$
  평균은 $S$의 모든 branching depth와, 첫 갈라짐보다 엄격히 앞인 추가 깊이 $d$에 대해 취하며 $(d,\mathbf q)$ 전체가 $\eta$-regular이다. singleton이면 평균은 $d$에 대해서만 취한다. $N$ 극한은 x:decor-limit-order의 수열을 따른다.
physics: |
  각 계층 깊이의 상태 안에서 spin들(과 그 아래에서 뽑은 replica들의 spin 곱)은 clustering한다: 상태 안 connected correlation의 제곱 평균이 0으로 간다. cavity method가 "한 상태 안에서 cavity field들은 서로 독립"이라고 가정하는 근거다 (R22, 제안 해석).
gap: |
  (1) 고정 깊이 $d$와 고정 깊이 배정마다가 아니라 $\eta$-regular 깊이에 대한 평균 $\mathcal A_{L,\eta}$로만 성립한다. $d$는 첫 갈라짐보다 $\eta L$ 넘게 앞이어야 한다. (2) clustering은 $N^{-2}\sum_{ij}\operatorname{Cov}^2\to0$이라는 $L^2$ 평균의 의미다. "멀리 떨어진 두 spin이 독립"이라는 점별 진술이 아니며 거리 개념도 쓰지 않는다. (3) 극한 순서: 고정 $L$에서 선택된 수열을 따라 $N\to\infty$, 그다음 $L\to\infty$. 수렴 속도는 귀납 단계마다 4제곱근을 거쳐 매우 느리다. (4) "상태"는 perturbed reservoir의 보조 계층 prefix다.
abstraction: approximation
children: [decor:conditional-concentration.s1, decor:conditional-concentration.s2, decor:conditional-concentration.s3, decor:conditional-concentration.s4, decor:conditional-concentration.s5, decor:conditional-concentration.s6, decor:conditional-concentration.s7]
source:
  - {file: decorrelation.tex, lines: [234, 245]}
  - {file: decorrelation.tex, lines: [247, 524]}
status: proposed
---

**증명의 뼈대.** 잎 수 $k$에 대한 귀납이다. [[decor:conditional-concentration.s1]]은 $V_{k,L}(\eta)=\max_{|S|\le k}\limsup_N\mathcal A_{L,\eta}v_N(S,d)$를 두고 명제를 $V_{k,L}(\eta)\to0$으로 바꾼다. [[decor:conditional-concentration.s2]]는 기저 $V_{1,L}(\eta)\le\delta/\eta$를 한 층 항등식과 세 사본 부등식으로 얻는다. $k\ge2$에서는 두 aligned 사본 I, II를 old tree로 두고 target으로 깊이를 한 칸 늦춘 $S^+$ 두 사본을 요구한다. [[decor:conditional-concentration.s3]]은 정규화 $J=\kappa(S^+)^2$에 대해 상대 절댓값 비용 $\frac1{|J|}\sum|c_E|\le C_{k,\eta}$를 준다. [[decor:conditional-concentration.s4]]는 모든 확장에서 target overlap을 사영된 $a$, $b$꼴 축약으로 바꾸는 오차가 $2p_N(S^+,e+1)+h_N(S)$이고 $\mathcal A_{L,\eta}h_N^2\le C_k/L$임을 준다. [[decor:conditional-concentration.s5]]는 확장을 target-II 첫 경로의 prefix로 분류하고 class별 계수 합($-c_\ell J$, $m_eJ$)을 구한다. [[decor:conditional-concentration.s6]]은 이것을 항등식에 넣고 $J$로 나누어 사영된 항등식과 오차 $\rho_N$의 상계를 얻는다. [[decor:conditional-concentration.s7]]은 $f$를 $a\cdot b$로 바꿔 좌변을 음이 아닌 세 사본 양으로 만들고, $v_N(S,d)$를 $\delta$, 자식의 $p_N$, $h_N$, 항등식 오차로 누른 뒤 깊이 평균을 취해 $V_{k,L}(\eta)\le C_{k,\eta}(L^{-1/2}+V_{k-1,L}(\eta/2)^{1/4})$을 얻는다. 기저와 함께 귀납이 닫힌다.
