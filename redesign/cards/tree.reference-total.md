---
id: tree:reference-total
kind: lemma
title: 'Reference-path totals (reference 경로 합)'
uses: [x:tree-extension-history, x:tree-reference-paths, tree:telescoping]
provides: '§7 decor:conditional-concentration.s3.s2 (J=κ(S^+)^2, tree:K), s5.s3 (class별 합; "임의의 이미 만든 reference 집합에서 반복"), decor:overlap-concentration.s2.s1 (C(S,e)=−δκ(S)). glossary g:tree-coefficient의 κ'
math: |
  다음 color가 지정된 reference prefix를 깊이 $d$까지 따라간 뒤, 그곳에서 reference path를 담은 $j\ge1$개의 자식 모두와 다른 자식으로 들어가야 한다고 하자. 이 조상 제약 말고는 그 이음은 제한이 없다. 그러면 허용된 모든 선택의 계수 합은
  $$m_d-jm_{d+1}$$
  이다. 따라서 anchor와 color들이 처방된 tree $S$를 이루어야 하면, 임의의 old tree의 모든 호환 확장에 대한 총 계수는
  $$\kappa(S)=\prod_{v\in\operatorname{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$$
  이다. 여기서 $a_v$와 $d_v$는 처방된 reference tree의 각 branching vertex의 자식 수와 깊이다. 더 일반적으로, 같은 한 걸음 규칙을 이미 만든 임의의 reference 집합에서 시작해 반복할 수 있다.
physics: |
  새 [[g:replica|replica]]를 지정한 [[g:reference-path|reference]] replica들과 지정한 깊이에서 갈라지게 붙이는 모든 방법의 계수 합은, 갈라지는 깊이 $d$와 그 vertex에서 이미 reference가 차지한 가지 수 $j$만으로 $m_d-jm_{d+1}$이다. 기존 replica를 재사용하는 방법과 새로 갈라지는 방법이 서로 상쇄해서, old tree(이미 있던 replica들의 배치)는 합에서 사라진다. 처방된 갈라짐 구조 $S$ 전체의 합은 닫힌 꼴 $\kappa(S)$([[g:tree-coefficient]])다.
gap: |
  부호 있는 합에 대한 진술이다. 절댓값 합은 훨씬 클 수 있다(두 path 예에서 $-\delta$ 대 $2+\delta$, [[x:tree-cancellation-example]]). 제약은 reference와의 갈라짐 깊이만 지정한다. $\kappa(S)$를 replica 계산의 block counting으로 읽는 것은 [[g:tree-coefficient]]의 물리 대응 칸에 intuition으로만 있다.
abstraction: exact
children: [tree:reference-total.s1, tree:reference-total.s2]
source:
  - {file: trees.tex, lines: [337, 357]}
  - {file: trees.tex, lines: [359, 386]}
status: proposed
---

**증명의 뼈대.** [[tree:reference-total.s1]]: 지정된 vertex에서 현재 tree의 자식이 $n$개이면, fresh 선택은 $m_d-nm_{d+1}$, reference 없는 $n-j$개 자식의 부분 tree는 각각 망원 합으로 $m_{d+1}$을 낸다. 합이 $m_d-jm_{d+1}$이다. [[tree:reference-total.s2]]: 일관된 처방에서는 가장 깊은 공통 prefix가 갈라지는 vertex와 $j$를 정하므로 한 걸음 합이 현재 reference tree에만 의존한다. 거꾸로 합하면 branching vertex $v$마다 $j=1,\ldots,a_v-1$의 인자가 나와 $\kappa(S)$가 된다.

$\kappa(S)$의 부호: 모든 인자 $m_d-jm_{d+1}$는 음이므로 부호는 $(-1)^{\sum_v(a_v-1)}$이다. 균등 격자에서 $j=1$ 인자는 $-\delta$, $j\ge2$ 인자의 크기는 $(j-1)m_d+j\delta$다(trees.tex 452).
