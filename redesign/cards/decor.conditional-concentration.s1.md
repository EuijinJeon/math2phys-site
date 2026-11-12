---
id: decor:conditional-concentration.s1
kind: step
title: '귀납량 $V_{k,L}(\eta)$'
uses: [decor:covariance-definition, decor:average-definition, decor:average-holder, x:decor-average-comparisons]
provides: 'conditional-concentration.s2 (k=1), s7.s4 (점화식)'
math: |
  $$V_{k,L}(\eta)=\max_{1\le|S|\le k}\limsup_{N\to\infty}\mathcal A_{L,\eta}v_N(S,d)$$
  로 둔다. 최대는 유한 개 labeled topology에 대해 취한다. $0\le V_{k,L}(\eta)\le1$이고, 명제는 모든 $k,\eta$에 대해 $\lim_{L\to\infty}V_{k,L}(\eta)=0$인 것과 동치다. 아래에서 쓰는 잎 수 $\le k-1$인 모양의 공분산 평균(안 쓰는 좌표가 더해진 평균, 이동된 깊이의 평균 포함)은 x:decor-average-comparisons와, 분수 거듭제곱이 나오면 decor:average-holder로 $V_{k-1,L}(\eta/2)$의 거듭제곱으로 눌린다 (구체적 형태는 s7.s3).
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [247, 262]}
status: proposed
---

귀납 전략의 요약이 이 구간에 있다: 각 proper child를 조건부 평균으로 바꾸고, 깊이를 늦춘 두 사본에 [[g:tree-identity|prescribed-tree 항등식]]을 적용한 뒤, 부호 있는 계수를 합하면 음이 아닌 세 사본 추정이 된다. $\max$를 $|S|\le k$ 전체에 대해 취하므로 $V_{k,L}$은 $k$에 대해 단조이다. 이 점이 s7.s4에서 작은 모양을 흡수할 때 쓰인다.
