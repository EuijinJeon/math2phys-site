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
  각 계층 깊이의 [[g:state|상태]]([[g:hierarchy|보조 계층]]의 깊이-$d$ prefix) 안에서 spin들(과 그 아래에서 뽑은 [[g:replica|replica]]들의 spin 곱)은 [[g:clustering|clustering]]한다: 상태 안 [[g:conditional-covariance|connected correlation]]의 제곱을 site 쌍에 대해 평균한 양이, 서로 떨어진 깊이들에 대해 평균하면 0으로 간다. decor:[[g:multioverlap|overlap]]-concentration 증명에서 이것은 "상태 안" 요동을 지우는 절반이다.
gap: |
  (1) $|S|\ge2$에서는 고정 깊이 $d$와 고정 [[g:topology|깊이 배정]]마다가 아니라 $\eta$-[[g:eta-regular|regular]] 깊이에 대한 평균 $\mathcal A_{L,\eta}$로만 증명된다. singleton은 예외다: 각 고정 $L$과 각 $\eta$-regular $d$에서 점별로 $v_N(S,d)\le\delta/\eta+o_N(1)$, 즉 $\limsup_Nv_N(S,d)\le1/(\eta L)$이다 (tex 288–289, decor:conditional-concentration.s2). $|S|\ge2$이면 $d$는 첫 갈라짐보다 $\eta L$ 넘게 앞이어야 하고, singleton이면 $d/L\in(\eta,1-\eta)$이어야 한다. (2) clustering은 $N^{-2}\sum_{ij}\operatorname{Cov}^2\to0$이라는 $L^2$ 평균의 의미다. "멀리 떨어진 두 spin이 독립"이라는 점별 진술이 아니며 거리 개념도 쓰지 않는다. (3) [[g:order-of-limits|극한 순서]]: 고정 $L$에서 [[g:selected-sequence|선택된 수열]]을 따라 $N\to\infty$, 그다음 $L\to\infty$. 수렴 속도는 귀납 단계마다 4제곱근을 거쳐 매우 느리다. (4) "상태"는 perturbed [[g:reservoir|reservoir]]의 보조 계층 prefix다. [[g:physical-pure-state|물리적 pure state]]가 아니다. (5) cavity method의 "이웃 site들의 [[g:message|cavity field]]는 서로 독립"이라는 가정([[g:independent-copies]])은 이 명제 혼자서 나오지 않는다. 논문에서 그 독립성은 decor:overlap-concentration(모든 multioverlap의 집중, 이 명제는 그 증명의 한 재료)과 §8의 comp:patterns(균일한 무작위 site 표본추출, comparison.tex 87–120)에서 나오고, comparison.tex 153이 decor:overlap-concentration을 적용한다. 이 명제는 site 쌍 평균 조건부 공분산 제곱만 다루고 여러 site의 결합 법칙을 말하지 않는다.
abstraction: approximation
children: [decor:conditional-concentration.s1, decor:conditional-concentration.s2, decor:conditional-concentration.s3, decor:conditional-concentration.s4, decor:conditional-concentration.s5, decor:conditional-concentration.s6, decor:conditional-concentration.s7]
source:
  - {file: decorrelation.tex, lines: [234, 245]}
  - {file: decorrelation.tex, lines: [247, 524]}
status: proposed
---

**증명의 뼈대.** 잎 수 $k$에 대한 귀납이다. [[decor:conditional-concentration.s1]]은 $V_{k,L}(\eta)=\max_{|S|\le k}\limsup_N\mathcal A_{L,\eta}v_N(S,d)$를 두고 명제를 $V_{k,L}(\eta)\to0$으로 바꾼다. [[decor:conditional-concentration.s2]]는 기저 $V_{1,L}(\eta)\le\delta/\eta$를 한 층 항등식과 [[g:three-copy|세 사본 부등식]]으로 얻는다. $k\ge2$에서는 두 aligned 사본 I, II를 old tree로 두고 target으로 깊이를 한 칸 늦춘 $S^+$ 두 사본을 요구한다. [[decor:conditional-concentration.s3]]은 정규화 $J=\kappa(S^+)^2$에 대해 상대 절댓값 비용 $\frac1{|J|}\sum|c_E|\le C_{k,\eta}$를 준다. [[decor:conditional-concentration.s4]]는 모든 확장에서 target overlap을 [[g:projection|사영]]된 $a$, $b$꼴 축약으로 바꾸는 오차가 $2p_N(S^+,e+1)+h_N(S)$이고 $\mathcal A_{L,\eta}h_N^2\le C_k/L$임을 준다. [[decor:conditional-concentration.s5]]는 확장을 target-II 첫 경로의 prefix로 분류하고 class별 계수 합($-c_\ell J$, $m_eJ$)을 구한다. [[decor:conditional-concentration.s6]]은 이것과, [[g:anchor|anchor]] 혼자인 쪽의 모든 확장이 같은 법칙의 target($d$에서 분리된 $S^+$ 두 사본)을 주어 그 합이 $-\delta J\,\mathbb ER_{\rm target}$으로 묶인다는 s5의 사실을 항등식에 넣고 $J$로 나누어 사영된 항등식과 오차 $\rho_N$의 상계를 얻는다. [[decor:conditional-concentration.s7]]은 $f$를 $a\cdot b$로 바꿔 좌변을 음이 아닌 세 사본 양으로 만들고, $v_N(S,d)$를 $\delta$, 자식의 $p_N$, $h_N$, 항등식 오차로 누른 뒤 [[g:depth-average|깊이 평균]]을 취하고, 고정 $L$에서 $\mathcal A_{L,\eta}$가 유한 합이라 $\limsup_N$과 바꿀 수 있다는 것(decor:identity-error)을 써서 $V_{k,L}(\eta)\le C_{k,\eta}(L^{-1/2}+V_{k-1,L}(\eta/2)^{1/4})$을 얻는다. 기저와 함께 귀납이 닫힌다.
