---
id: x:overview-upper
kind: remark
title: '전략: 상한은 모든 크기·모든 유한 깊이에서'
uses: [model:hamiltonian, model:functional, model:factorization]
provides: 'x:overview-strategy. L1 수 1'
math: |
  interpolation 상한은 모든 계 크기와 모든 유한 깊이에서 성립한다. 이 논문은 그것을 upper:section에서 다시 증명하고, 승수 $\log a$ 의 적분 가능성을 가정하지 않게 하는 정규화를 포함한다. 하한은 네 단계다.
physics: |
  [[g:interpolation|interpolation]] 상한 $F_N\le\mathcal B_r(\zeta,\mathbf m)$ 은 극한이 아니라 모든 $N$ 과 모든 유한 [[g:rsb-steps|RSB 단계 수]]에서 성립한다. [[g:factorization|전개]]의 승수 $a$ 에는 적분 조건을 걸지 않는다.
gap: |
  예고 문장이다. 정확한 진술과 가정은 upper:bound에 있고, 정규화는 upper:regularization이다. "하한은 네 단계"는 x:overview-step1–step4가 받고, 하한을 일반 상호작용으로 넓히는 마무리는 x:overview-closing이 받는다.
abstraction: weakening
children: []
source:
  - {file: overview.tex, lines: [3, 6]}
status: proposed
---

**가리키는 곳** (예고이므로 `uses` 가 아니다).

| 문장 | 본문 노드 | overview.tex |
|---|---|---|
| 상한은 모든 크기, 모든 유한 깊이 | [[upper:bound]] (`\cref{upper:section}`, [[upper:section]]) | 3–4 |
| $\log a$ 의 적분 가능성 없이 정규화 | [[upper:regularization]] | 4–6 |
| 하한은 네 단계 | [[x:overview-step1]]–[[x:overview-step4]] | 6 |
