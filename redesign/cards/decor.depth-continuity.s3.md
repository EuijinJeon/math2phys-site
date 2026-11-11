---
id: decor:depth-continuity.s3
kind: step
title: '이동 하나의 비용 $C/L$'
uses: [decor:depth-continuity.s1, decor:depth-continuity.s2, decor:average-definition, x:decor-eta-regular]
provides: 'decor:depth-continuity.s4'
math: |
  $|U|=1$, $U=\{v\}$이고 깊이 배정이 $\eta'$-regular ($\eta'>0$; 평균도 $\mathcal A_{L,\eta'}$)이면 $\eta'L\ge1$일 때 $\mathcal A_{L,\eta'}\mathbb E\|\mu_{d,S^U}-\mu_{d,S}\|_N^2\le C/L$ ($C$는 $S$의 vertex 수에만 의존). 조건 $\eta'L\ge1$은 작성자 유도다(원문은 이 단계에서 큰 $L$을 따로 부르지 않는다): regularity에서 $v$의 자식의 다음 branching depth $q'$는 $q'-q_v>\eta'L\ge1$이므로 $q_v+1<q'$이고, $q_v<(1-\eta')L$이므로 $q_v+1\le L-1$이다. 그래서 s2의 $\mu_{q_v+1,T_j}$가 정의되고 $S^U$의 깊이 배정이 가지를 따라 엄격히 증가한다. 근거: s2의 우변을 $q=q_v$에 대해 합하면 각 자식 모양에 대해 s1에 의해 $s\cdot s$ 이하다. 깊이 $q_v$에서 바뀐 부분 tree 평균을 조상 깊이 $d$로 올리는 연산은 조건부 기대값과 절댓값 1 이하 인자의 좌표별 곱뿐이므로 $\mathbb E\|\cdot\|_N^2$를 늘리지 않는다. 나머지 좌표에 대한 평균은 $L$의 거듭제곱으로 상쇄된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [194, 199]}
status: proposed
---

조건부 기대값은 $L^2$ 축약이고(Jensen), $[-1,1]$ 값 인자를 좌표별로 곱해도 각 좌표의 절댓값이 줄 뿐이다. 그래서 바뀐 부분 tree의 차이가 조상으로 전파되어도 커지지 않는다. $q_v$에 대한 합이 $L$에 무관하게 유계이므로 정규화 $L^{-1}$이 남는다. $\eta'L\ge1$ 조건의 출처는 위 `math`에 적었다(작성자 유도, 검토 1의 계산과 같다). 원문이 "large $L$"을 실제로 부르는 곳은 여러 이동의 중간 모양을 다루는 tex 201–203이고, 그것은 다음 단계(s4)의 `math`에 있다.
