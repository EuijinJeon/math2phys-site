---
id: decor:contractions
kind: lemma
title: '축약 부등식과 세 사본 부등식'
uses: [decor:covariance-definition, x:decor-spin-product]
provides: 'decor:projection-bound (축약 부등식). conditional-concentration.s2.s2와 s7.s2 (세 사본 부등식으로 v_N을 overlap 차이로 누름)'
math: |
  (a) $d$가 $S$의 initial stem 위의 깊이이고 확률 벡터 $B\in[-1,1]^N$가 $\mathscr F_d$가 주어지면 $A_S$와 조건부 독립이면
  $$\bigl\|(A_S-\mu_{d,S})\cdot B\bigr\|_{L^2}\le v_N(S,d)^{1/4}.$$
  (b) $X,Y,Z$가 $\sigma$-field $\mathscr G$가 주어지면 조건부 독립이고 같은 조건부 법칙을 갖는 유계 확률 벡터($\mathbb R^N$ 값)이고 $C$가 그 조건부 공분산 행렬이면
  $$\mathbb E(X\cdot Y-X\cdot Z)^2\ge\frac2{N^2}\mathbb E\sum_{i,j}C_{ij}^2.$$
physics: |
  (b) 같은 조건($\sigma$-field $\mathscr G$; 쓰이는 곳에서는 [[g:state|상태]] $\mathscr F_d$)이 주어지면 조건부 i.i.d.인 [[g:replica|replica]] 세 개 $X,Y,Z$에 대해 [[g:multioverlap|overlap]] $R_{XY}$와 $R_{XZ}$의 차이 제곱 평균은 그 조건 아래 [[g:conditional-covariance|조건부 공분산]] 제곱 평균의 두 배 이상이다. 따라서 상태 안에서 overlap이 요동하지 않으면 상태 안 조건부 공분산 제곱 평균 $v_N$ 도 작다. (a) 반대로 $v_N$ 이 작으면 replica를 상태 평균으로 바꿔도 조건부 독립인 벡터와의 축약이 거의 변하지 않는다. (이 lemma 자체는 어떤 $v_N$ 도 작다고 말하지 않는다. $v_N$ 의 깊이 평균이 0으로 간다는 결론은 decor:conditional-concentration, 곧 [[g:conditional-decorrelation|조건부 decorrelation]]이다.)
gap: |
  (b)의 조건은 일반 $\sigma$-field $\mathscr G$ 이고, 상태([[g:hierarchy|보조 계층]] prefix $\mathscr F_d$)는 그 특수한 경우다. (b)는 한 방향 부등식뿐이고, (a)의 오차는 $v_N^{1/4}$라는 약한 거듭제곱이다. 물리의 "조건이 주어졌을 때 overlap 집중 ⇔ 조건부 상관 소멸"의 양방향 등가를 정량적 한 방향 부등식 두 개로 나눈 형태다.
abstraction: weakening
children: [decor:contractions.s1, decor:contractions.s2]
source:
  - {file: decorrelation.tex, lines: [108, 125]}
  - {file: decorrelation.tex, lines: [127, 140]}
status: proposed
---

**증명의 뼈대.** (a)는 [[decor:contractions.s1]]: 조건부 2차 모멘트가 $N^{-2}\sum C_{ij}B_iB_j$이고 이를 $C$의 Hilbert–Schmidt 노름으로 누른 뒤 prefix에 대해 Jensen을 쓴다. (b)는 [[decor:contractions.s2]]: 조건부 2차 모멘트가 정확히 $\frac2{N^2}\operatorname{tr}((C+\mu\mu^{\mathsf T})C)$이고 $\mu^{\mathsf T}C\mu\ge0$이다. 증명이 짧아 단계는 두 개다.
