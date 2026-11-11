---
id: decor:conditional-concentration.s5.s2
kind: step
title: 'class 안에서 결합 법칙이 고정됨'
uses: [decor:conditional-concentration.s5.s1, x:decor-tree-sampling]
provides: 'decor:conditional-concentration.s5.s3, s6'
math: |
  고정된 확장 이력 $E$에서 모든 옛 경로와 target II 첫 경로의 깊이-$e$ prefix만 남기고 나머지 새 가지를 지워도, 옛 경로와 사영된 prefix들의 결합 법칙은 바뀌지 않는다. 남는 tree는 class에만 의존한다(깊이 $\ell<e$에 fresh stem이 붙은 old tree, 또는 old tree 자체). 따라서 $\mathbb E[f\cdot(a\cdot b_\ell)]$, $\mathbb E[f\cdot(a\cdot b)]$는 class 안에서 일정하고, 사영된 항의 합은 class별 (사영된 기대값)×(class의 총 부호 계수)의 합이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [401, 413]}
status: proposed
---

지운 부분 tree는 자기 확률 kernel로 적분하면 1이고, 재사용된 옛 leaf는 새 변수를 들이지 않는다. target I의 사영 $a$는 이미 old anchor prefix에만 의존한다. 이력은 표본값에 대한 조건이 아니라 조합적 선택이다. 그래서 이력마다 tree 모양만 다르고 그 위의 법칙은 표본 규칙이 정한다.
