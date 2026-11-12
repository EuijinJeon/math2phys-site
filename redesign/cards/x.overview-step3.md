---
id: x:overview-step3
kind: remark
title: '전략 3단계: 모든 multioverlap의 집중'
uses: []
provides: 'x:overview-strategy. L1 수 5 (깊이 미루기는 L1의 마지막 문단)'
math: |
  target tree의 각 내부 branching 깊이를 한 단계 늦춘다. 각 새 깊이의 첫 fresh split이 정규화 계수와 같은 작은 인자를 낸다. 절대 계수 합의 상대 한계가 나눗셈 뒤에도 오차의 제어를 유지한다. 그러면 조건부 공분산이 replica 수에 대한 귀납으로 감쇠한다. 두 번째 항등식이 남은 조건부 평균을 집중시킨다.
physics: |
  [[g:depth-delay|깊이 미루기]]: target tree의 갈라짐을 한 칸씩 늦추면 새 갈라짐마다 계수 $\delta=1/L$ 하나가 나와, 부호 있는 계수 합과 절댓값 합의 크기가 맞춰진다. 그래서 [[g:tree-identity|prescribed-tree 항등식]]을 정규화 계수로 나누어도 오차가 유계로 남고, replica 수에 대한 귀납으로 [[g:state|상태]] 안 [[g:conditional-covariance|조건부 공분산]]이 사라진다([[g:conditional-decorrelation|조건부 decorrelation]]). 마지막으로 다른 항등식(marker [[g:anchor|anchor]])이 상태 사이의 요동, 곧 조건부 평균의 요동을 없앤다. 합쳐서 모든 [[g:multioverlap|multioverlap]]이 [[g:concentration|집중]]한다([[g:overlap-concentration]]).
gap: |
  (1) 조건부 공분산의 소멸(decor:conditional-concentration)과 최종 결과(decor:overlap-concentration)는 고정 깊이가 아니라 [[g:eta-regular|$\eta$-regular]] 깊이에 대한 [[g:depth-average|깊이 평균]]의 진술이고 극한 순서는 $\lim_L\limsup_N$ 이다. 잎 하나인 경우만 예외다: 조건부 공분산은 각 고정 $L$·깊이에서 $\le\delta/\eta+o_N(1)$ 이고(decorrelation.tex 287–290), multioverlap의 분산은 각 고정 $L$ 에서 0으로 간다(72–74행). 두 번째 항등식이 주는 조건부 평균의 집중은 고정 $L$·고정 깊이에서 성립하며($\operatorname{Var}(M)\to0$, decorrelation.tex 562–569), 깊이 평균은 두 추정을 합칠 때 필요하다(81–83행; x:overview-closing 43–46행). (2) "조건부 공분산이 감쇠한다"의 정확한 양은 site 쌍에 평균한 조건부 공분산 제곱 $v_N(S,d)$ 이다. (3) "상태"는 섭동 mark로 만든 보조 계층의 prefix이고 [[g:physical-pure-state|물리적 pure state]]가 아니다. (4) "정규화 계수와 같은 작은 인자"를 $\delta$ 로 읽는 것은 trees.tex 326–333과 tree:charging에 근거한 작성자의 읽기다. 원문 문단은 $\delta$ 를 적지 않는다.
abstraction: approximation
children: []
source:
  - {file: overview.tex, lines: [26, 33]}
status: proposed
---

**가리키는 곳.**

| 문장 | 본문 노드 | overview.tex |
|---|---|---|
| 내부 branching 깊이를 한 단계 늦춘다 | [[decor:conditional-concentration]] ($S\to S^+$; decorrelation.tex 79–81), 계산의 본보기는 [[x:tree-cancellation-example]] (trees.tex 317–335) | 27 |
| 첫 fresh split이 정규화 계수와 같은 작은 인자 | [[tree:charging]] (fresh split 하나에 $\delta$), 정규화 계수 $J$ (`decor:J-definition`, `decor:J-lower-bound`, [[decor:conditional-concentration]] 안) | 28–29 |
| 절대 계수 합의 상대 한계 | `tree:relative-charging` ([[tree:charging]] 안), `decor:relative-absolute-cost` ([[decor:conditional-concentration]] 안) | 29–30 |
| replica 수에 대한 귀납으로 조건부 공분산 감쇠 | [[decor:conditional-concentration]], [[decor:covariance-definition]] | 30–31 |
| 두 번째 항등식이 남은 조건부 평균을 집중 | [[decor:overlap-concentration]] (marker anchor, [[decor:overlap-concentration.s2]]) | 32–33 (`\cref{decor:section}`, [[decor:section]]) |
