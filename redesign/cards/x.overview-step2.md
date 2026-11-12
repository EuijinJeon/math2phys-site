---
id: x:overview-step2
kind: remark
title: '전략 2단계: branching pattern 처방'
uses: []
provides: 'x:overview-strategy. L1 수 4'
math: |
  유한 확률 tree에 대한 초등적 계산이 insertion을 추가된 replica path들에 대한 부호 있는 합으로 전개한다. 독립 mark가 임의의 지정된 branching pattern을 고른다. 그러면 score 집중이 이 부호 있는 합들에 대한 항등식을 준다.
physics: |
  섭동 하나를 [[g:power-mean|power mean]] 안에 넣은 효과는 새 [[g:replica|replica]] path를 붙이는 방법([[g:extension-history|extension history]])에 대한 부호 있는 합으로 정확히 전개된다([[g:tree-coefficient|tree 계수]]). 깊이별 무작위 부호 [[g:mark|mark]]로 원하는 갈라짐 깊이를 골라내고, [[g:score|score]]의 [[g:concentration|집중]]을 넣으면 [[g:tree-identity|prescribed-tree 항등식]]이 나온다.
gap: |
  (1) "any prescribed branching pattern"(22–23행)은 원문의 요약 표현이다. 본문의 제약은 [[g:anchor|anchor]]와 추가 color들로 이루어진 집합 안의 쌍별 split 깊이(추가 color끼리의 쌍 포함)를 일관되는 한 임의로 지정하고, 다른 old replica가 관여하는 쌍은 지정하지 않는다(perturbations.tex 433–436, trees.tex 311–315, pert:tree-identity 차이 칸 (3), mark 깊이는 $1,\ldots,L-1$). (2) 항등식은 [[g:selected-sequence|선택된 수열]]을 따라, 고정 $L$, tree, 제약마다 $N\to\infty$ 에서만 성립한다(pert:tree-identity). (3) 계층 구조 자체는 이 항등식에서 나오지 않고 [[g:hierarchy|보조 계층]]의 구성에 들어 있다.
abstraction: approximation
children: []
source:
  - {file: overview.tex, lines: [20, 24]}
status: proposed
---

**가리키는 곳.**

| 문장 | 본문 노드 | overview.tex |
|---|---|---|
| 유한 확률 tree의 계산, 부호 있는 합으로의 전개 | [[tree:section]], [[tree:insertion]], [[tree:extension-expansion]] | 21–22 |
| 독립 mark가 pattern을 고른다 | [[x:pert-mark-specification]], [[x:pert-colored-extensions]] (제약 $\mathcal C$), [[x:tree-reference-paths]], [[pert:tree-identity.s2]] (selector), [[pert:tree-identity.s3]] | 22–23 |
| score 집중에서 항등식 | [[pert:analytic]], [[pert:tree-identity]] | 23–24 (`\cref{tree:section,pert:tree-identity}`) |

물리 문장이 원문 요약보다 좁다(mark가 고르는 것은 "원하는 갈라짐 깊이"). 그래도 "원하는"이 본문의 제약 범위보다 넓게 읽힐 수 있어 `approximation` 으로 두고 차이 칸 (1)에 범위를 적었다.
