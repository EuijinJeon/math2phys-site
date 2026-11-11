---
id: decor:conditional-concentration.s4.s2
kind: step
title: '$h_N$의 균등성과 사영 벡터 $a$, $b$'
uses: [decor:conditional-concentration.s4.s1, x:decor-tree-sampling, decor:projection-definition]
provides: 'conditional-concentration.s5, s6'
math: |
  $h_N(S)$는 위 비교들의 유한 개 $L^2(\|\cdot\|_N)$ 거리의 합에 크기 의존 상수를 곱한 것으로 잡을 수 있다. 이 거리들은 단일 사본 marginal 모양에만 의존하므로 $h_N(S)$는 확장에 무관하다. 그래서 old tree와 target tree의 합집합이 regular하지 않아도 $\mathcal A_{L,\eta}h_N(S)^2\le C_k/L$이 확장 합의 모든 비교에 균등하게 성립한다. $a$, $b$를 old stem I, II 위의 $a_{S,e}$라 하자. target I의 stem은 anchor를 포함하므로 old I prefix를 깊이 $e$까지 공유하고, 그 최종 사영 벡터는 $a$이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [374, 385]}
status: proposed
---

target I의 $S^+$는 $e+1$에서야 처음 갈라지므로 target I 전체가 [[g:anchor|anchor]]와 깊이 $e$까지 [[g:state|prefix]]를 공유한다. 그래서 깊이 $e$에서 평가한 자식 평균의 곱은 old I의 것과 같다. 균등성이 중요한 이유: 확장 합에는 $L$에 따라 개수가 늘어나는 확장이 있으므로, 오차가 확장마다 다른 regularity를 요구하면 합을 제어할 수 없다.
