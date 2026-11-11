---
id: decor:depth-continuity.s4
kind: step
title: '여러 이동과 더 큰 tree'
uses: [decor:depth-continuity.s3, x:decor-average-comparisons, x:decor-tree-sampling]
provides: 'decor:depth-continuity의 첫째 부등식 (branch-depth-continuity) 일반형'
math: |
  $U=\{v_1,\ldots,v_u\}$이면 $S=S^{U_0},S^{U_1},\ldots,S^{U_u}=S^U$ ($U_r=\{v_1,\ldots,v_r\}$)로 하나씩 바꾸고 $\|\sum_{r=1}^u x_r\|^2\le u\sum_r\|x_r\|^2$를 쓴다. regularity 때문에 중간 모양들은 같은 조상 관계를 갖고, $L$이 크면 그 깊이 배정은 $\eta/2$-regular이다 (x:decor-average-comparisons (ii)). 그래서 각 항에 $\eta/2$ 영역에서의 s3을 적용해 $\mathcal A_{L,\eta}\mathbb E\|\mu_{d,S^U}-\mu_{d,S}\|_N^2\le u^2C/L$. 한 prefix의 marginal law는 다른 sampled branch를 빼도 바뀌지 않으므로 이 추정은 더 큰 sampled tree 안에서도 성립한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [199, 206]}
status: proposed
---

정수 이동은 $\eta$-regular 배정을 단사로 $\eta/2$-regular 배정에 보낸다. 그래서 $\mathcal A_{L,\eta}$ 아래의 중간 모양 평균은 $\mathcal A_{L,\eta/2}$ 아래의 한 이동 평균으로 눌린다. "더 큰 tree" 문장이 필요한 이유: §7.3–7.4에서 $\mu$들은 두 사본이나 확장된 tree 안에서 계산되는데, 비교하는 양이 한 prefix의 marginal에만 의존하므로 단일 사본 추정이 그대로 적용된다.
