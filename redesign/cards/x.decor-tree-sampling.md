---
id: x:decor-tree-sampling
kind: convention
title: 'tree 표본 규칙 (조건부 독립과 사영 일관성)'
uses: [tree:section]
provides: '조건부 독립에 기댄 모든 단계: decor:projection-definition, decor:projection-bound, depth-continuity, 확장 합의 class별 법칙 고정 (conditional-concentration.s5.s2), marker anchor 단계'
math: |
  §3의 규칙. 처방된 유한 tree $\mathcal T$는 공통 root(깊이 0 변수: disorder와 섭동의 개수·type·site. 섭동 매개변수는 root 변수가 아니라 선택된 고정값이다, cavity.tex 29–31)와 깊이 $L$에서 끝나는 labeled path들로 이루어진다. 각 vertex에서 서로 다른 children은 그 vertex까지의 prefix가 주어지면 kernel $K_{d+1}$로 서로 조건부 독립으로 뽑힌다. 깊이 $L$의 leaf에는 spin 배치 $\sigma^a\in\{-1,1\}^N$이 놓인다. 일부 leaf와 그것들만 쓰는 경로 부분을 지워도 나머지 tree의 표본 법칙은 바뀌지 않는다. 특히 한 경로(또는 한 부분 tree)의 법칙은 그것을 포함한 더 큰 tree에 무관하고, 어떤 vertex 아래의 부분 tree는 그 vertex까지의 prefix(root 포함)가 주어지면 tree의 나머지 전부와 조건부 독립이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [8, 9]}
  - {file: trees.tex, lines: [28, 40]}
status: proposed
---

마지막 문장(부분 tree가 [[g:state|prefix]]([[g:root]] 포함)가 주어지면 나머지와 조건부 독립)은 유도로서 옳다고 검토 1에서 확인되었다. 근거: kernel은 prefix 전체(root 포함)에 의존한다(trees.tex 20–22), "different children are drawn independently"(trees.tex 31–32), "Conditional independence of children and the projectivity of tree sampling"(trees.tex 200–201). decorrelation.tex도 이 형태로 쓴다: 209, 216–217 "independent of the continuation of $S$ given its prefix at $e$", 550–551.
