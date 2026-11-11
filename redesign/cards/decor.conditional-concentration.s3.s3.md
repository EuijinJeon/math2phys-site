---
id: decor:conditional-concentration.s3.s3
kind: step
title: '상대 절댓값 비용 (relative absolute cost)'
uses: [decor:conditional-concentration.s3.s1, decor:conditional-concentration.s3.s2, tree:charging, x:decor-eta-regular]
provides: 'conditional-concentration.s6 (사영 오차 합을 J로 나눈 뒤 C_{k,η}로 제어). decor:order-of-limits가 가리키는 균등 상계'
math: |
  $L$이 크면 regularity 때문에 각 shifted depth $q_v+1$은 old tree의 모든 branching depth($d$와 모든 $q_w$)와 다르다. 그래서 target의 $2b$개 branching vertex는 모두 fresh unary split로 만들어져야 하고, tree:charging의 (relative-charging) 부등식에서
  $$\frac1{|J|}\sum_{\text{allowed extensions}}|c_E|\le C_{k,\eta}$$
  ($C_{k,\eta}$는 $L$과 깊이 배정에 무관). 전체 부호 있는 계수에는 깊이 $d$에서의 분리 인자 $-\delta$가 더 붙는다. 이 인자는 $J$로 나눈 뒤에도 항등식 안에 남긴다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [345, 360]}
status: proposed
---

$|q_v+1-q_w|\ge\eta L-1>0$ ($w\ne v$), $q_v+1-q_v=1$, $q_v+1-d>\eta L$이다. 두 사본은 깊이를 공유하지만 branching vertex는 서로 다르다. 그래서 각 vertex가 자기 $\delta$를 하나씩 내고, 절댓값 합이 $\delta^{2b}$ 차수, 즉 $|J|$와 같은 차수가 된다. 깊이 $d$의 target vertex는 old tree에서도 branching이므로 charge되지 않는다. 그래서 $J$에 들어가지 않는다.
