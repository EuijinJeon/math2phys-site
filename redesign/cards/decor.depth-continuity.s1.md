---
id: decor:depth-continuity.s1
kind: step
title: 'martingale energy와 평가 깊이 연속성'
uses: [decor:covariance-definition, decor:average-definition]
provides: 'depth-continuity의 둘째 부등식 (evaluation-depth-continuity). s3의 q에 대한 합. overlap-concentration.s3의 (adjacent-prefix-error)'
math: |
  모양 $T$의 나중 branching depth를 고정하고 initial stem을 따라 한 경로를 뽑으면 $t\mapsto\mu_{t,T}$는 그 stem의 prefix filtration $(\mathscr F_t)$에 대한 vector martingale이고 좌표가 $[-1,1]$에 있다. 증분의 직교성에서
  $$\sum_t\mathbb E\|\mu_{t+1,T}-\mu_{t,T}\|_N^2=\mathbb E\|\mu_{t_1,T}\|_N^2-\mathbb E\|\mu_{t_0,T}\|_N^2\le1$$
  (합은 initial stem 위의 $t,t+1$에 대해, $t_0$, $t_1$은 그 범위의 처음과 끝). 특히 $t\mapsto\mathbb E\|\mu_{t,T}\|_N^2$는 증가한다(각 증분이 $\mathbb E\|\mu_{t+1,T}-\mu_{t,T}\|_N^2\ge0$). 이것을 범위를 갖는 $d$에 대해 합하고 정규화 $L^{-1}$을 곱하면, 나머지 좌표의 합은 $L$의 거듭제곱으로 상쇄되어 $\mathcal A_{L,\eta}\mathbb E\|\mu_{d+1,S}-\mu_{d,S}\|_N^2\le1/L$.
physics: |
  깊이 $t$ [[g:state|상태]] 평균의 자기 [[g:multioverlap|overlap]] $q_t=\mathbb E\|\mu_{t,T}\|_N^2$ ($T$가 [[g:replica|replica]] 하나면 $\mathbb E\,N^{-1}\sum_i\langle\sigma_i\rangle_t^2$)은 계층 깊이를 따라 증가하고, 그 증가분의 합은 1 이하다. 한 깊이에서 다음 깊이로 상태 평균이 바뀌는 양의 제곱 평균이 정확히 그 증가분이다.
gap: |
  "상태"는 [[g:hierarchy|보조 계층]]의 prefix $\mathscr F_t$([[g:root]] 포함)이고 [[g:physical-pure-state|물리적 pure state]]가 아니다. $q_t$는 보조 계층 깊이 $t$의 양이며 Parisi 함수 $q(x)$의 값으로 식별되지 않는다. $T$가 여러 leaf를 가지면 $\mu_{t,T}$는 여러 replica spin 곱의 조건부 평균이다.
abstraction: exact
children: []
source:
  - {file: decorrelation.tex, lines: [168, 177]}
status: proposed
---

직교 증분의 등식은 원문 (tex 171–173) "Orthogonality of its increments gives"의 내용을 풀어 적은 것이다. 핵심은 이 합이 깊이 수 $L$과 무관하게 1로 유계라는 것이다. 따라서 깊이에 대해 평균하면 $1/L$이 된다. 개별 깊이에서는 증분이 클 수 있다.
