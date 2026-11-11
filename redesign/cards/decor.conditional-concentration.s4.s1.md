---
id: decor:conditional-concentration.s4.s1
kind: step
title: '$e+1$에서 사영하고 깊이를 되돌리기'
uses: [decor:conditional-concentration.s3.s1, decor:projection-bound, decor:depth-continuity, x:decor-product-difference, x:decor-tree-sampling, x:decor-eta-regular]
provides: 'decor:conditional-concentration.s4.s2'
math: |
  각 허용 확장에서 target tree는 marginal로 보통의 $S^+$ 두 사본이고 $d$ 아래에서 서로 독립이다. 그래서 decor:projection-bound (두 측 형태, 모양 $S^+$, 첫 갈라짐 $e+1$)에서 target overlap은 $e+1$에서의 사영 벡터 $a_{S^+,e+1}$ 두 개의 축약과 $L^2$에서 $2p_N(S^+,e+1)$ 이하로 다르다. 각 측에서 자식 깊이를 1 되돌리고($T_j^+\to T_j$, 첫째 부등식) 평가 깊이를 $e+1$에서 $e$로 옮기면(둘째 부등식. $e$는 aligned 구성의 평균 좌표이고, regularity로 $[e,e+1]$은 각 $T_j$의 initial stem 위에 있으므로 적용된다) 축약은 $L^2$에서 $h_N(S)$ 이하로 바뀐다. $L$이 크면
  $$\mathcal A_{L,\eta}h_N(S)^2\le C_k/L.$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [361, 373]}
status: proposed
---

$S^+$는 $e+1$에서 처음 갈라지고 자식 모양은 내부 깊이가 1씩 늘어난 $T_j^+$이다. 비교는 세 단계다: $\mu_{e+1,T_j^+}\to\mu_{e+1,T_j}$ (branching depth 되돌리기), $\mu_{e+1,T_j}\to\mu_{e,T_j}$ (평가 깊이). 곱 차이 부등식이 자식별 차이를 곱의 차이로 바꾸고, 축약 부등식 $|x\cdot y-x'\cdot y'|\le\|x-x'\|_N+\|y-y'\|_N$이 두 측을 합친다. depth-continuity의 평균은 $S$의 좌표 $(d,\mathbf q)$ 중 일부만 쓰므로 나머지 좌표의 합은 정규화로 상쇄된다. $\mu_{e+1,T_j}$와 $\mu_{e,T_j}$ 비교에서 $e$는 $S$의 branching depth이자 $T_j$의 평가 깊이다. 평가 깊이 연속성(decor:depth-continuity의 둘째 부등식)은 평가 깊이가 평균 좌표이기를 요구한다(tex 155–162 "If $d$ ranges along an initial unary stretch … this average includes $d$"). $e$가 평균 좌표라는 것은 tex 492–493 "$D=b(S)+1$ distinct depth coordinates, including $d$ and $e$"에 있고, 같은 논법을 정리 증명이 명시한다(tex 588–589 "Here $e$ is itself a ranged coordinate, so the one-step increments are summed before division by $L$"). $[e,e+1]$이 $T_j$의 initial stem 위라는 것은 $T_j$의 다음 branching depth가 $e$보다 $\eta L$ 넘게 뒤라는 regularity에서 나온다. 검토 1에서 확인되어 해소되었다.
