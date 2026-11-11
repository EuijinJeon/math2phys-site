---
id: decor:depth-continuity.s3
kind: step
title: '이동 하나의 비용 $C/L$'
uses: [decor:depth-continuity.s1, decor:depth-continuity.s2, decor:average-definition]
provides: 'decor:depth-continuity.s4'
math: |
  $|U|=1$, $U=\{v\}$이면 $L\ge L_0$에서 $\mathcal A_{L,\eta}\mathbb E\|\mu_{d,S^U}-\mu_{d,S}\|_N^2\le C/L$ ($C$는 $S$의 vertex 수에만 의존). 근거: s2의 우변을 $q=q_v$에 대해 합하면 각 자식 모양에 대해 s1에 의해 $s\cdot s$ 이하다. 깊이 $q_v$에서 바뀐 부분 tree 평균을 조상 깊이 $d$로 올리는 연산은 조건부 기대값과 절댓값 1 이하 인자의 좌표별 곱뿐이므로 $\mathbb E\|\cdot\|_N^2$를 늘리지 않는다. 나머지 좌표에 대한 평균은 $L$의 거듭제곱으로 상쇄된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [194, 199]}
status: proposed
---

조건부 기대값은 $L^2$ 축약이고(Jensen), $[-1,1]$ 값 인자를 좌표별로 곱해도 각 좌표의 절댓값이 줄 뿐이다. 그래서 바뀐 부분 tree의 차이가 조상으로 전파되어도 커지지 않는다. $q_v$에 대한 합이 $L$에 무관하게 유계이므로 정규화 $L^{-1}$이 남는다. ❓ "$L\ge L_0$"는 갈라짐을 $q_v+1$로 늦춰도 그 자식들의 다음 branching depth보다 앞에 있어야 한다는 조건에서 온다고 읽었다. 원문은 이 단계에서 따로 밝히지 않는다.
