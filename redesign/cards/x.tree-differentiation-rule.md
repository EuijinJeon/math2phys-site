---
id: x:tree-differentiation-rule
kind: lemma
title: '미분 규칙: protected leaf와 fresh path'
uses: [tree:insertion, tree:first-variation, x:tree-sampling]
provides: 'tree:log-expansion.s1과 tree:extension-expansion.s1이 "the preceding rule"로 부르는 규칙'
math: |
  tree 밀도의 leaf 인자 $A^a$가 분모 $A^a$로 상쇄되면 그 leaf를 protected라 한다. protected leaf의 집합 $C$와 유계이고 매개변수에 무관한 함수 $G$에 대해 $E_{\mathcal T}^A[G\prod_{a\in C}(A^a)^{-1}]$를 생각한다. (tree:density)를 미분하면
  $$\partial_{t_j}\log W_{\mathcal T}(A)=\sum_{a\in\operatorname{Leaves}(\mathcal T)}\frac{D_j^a}{A^a}+\sum_{\beta\in\operatorname{Int}(\mathcal T)}\gamma_\beta\,\partial_{t_j}\log Y_\beta.$$
  $E_{\mathcal T}^A[G\prod_{a\in C}(A^a)^{-1}]$의 도함수에서 $a\in C$의 leaf 항은 분모의 미분과 정확히 상쇄된다. 남은 각 leaf 항은 $D_j^a/A^a$를 넣고 그 leaf를 protected로 만든다. (tree:first-variation)에 의해 내부 vertex 항은 $\beta$ 아래에 독립인 updated path 하나를 붙이고 그 말단 vertex에 인자 $D_j/A$를 더한 같은 기대값이다. 이것이 정확히 $\beta$에서의 fresh path이고 계수는 $\gamma_\beta$이며, 새 leaf는 protected다. 자식들의 조건부 독립과 tree 표본추출의 사영 일관성이, $G$가 $\beta$의 다른 자식들을 쓰는 경우에도 이 표현을 정당화한다.
physics: |
  매개변수에 무관한 유계 함수 $G$를 곱한 tree 기대값에서 leaf 인자 $A^a$를 분모로 상쇄한 leaf를 [[g:protected-leaf|protected leaf]]라 하자. 섭동 매개변수로 한 번 미분하면 아직 protected가 아닌 기존 [[g:replica|replica]]에 $D_j/A$를 붙이거나(계수 1), [[g:prescribed-tree|tree]]의 내부 vertex $\beta$에서 updated kernel로 새 path를 독립으로 뽑아 그 leaf에 $D_j/A$를 붙인다(계수 $\gamma_\beta$, [[g:tree-coefficient]]). 두 경우 모두 그 leaf를 protected로 만든다. 기존 protected leaf의 미분항은 분모의 미분과 상쇄된다.
gap: |
  계수 $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$는 $m_{d_\beta}<m_{d_\beta+1}$이므로 항상 음이고, 옛 replica 재사용의 계수 $+1$과 섞여 전개 전체는 부호 있는 합이 된다. 확률 혼합으로 읽을 수 없다. $n\to0$ 해석적 연속 없이 유한 tree 위에서 정확히 성립한다. 매개변수에 무관한 $G$와 protected leaf 회계가 있어야 반복 적용이 닫힌다.
abstraction: exact
children: []
source:
  - {file: trees.tex, lines: [178, 202]}
status: proposed
---

이 규칙은 원문에 이름이 없다("the preceding rule", trees.tex 300). leaf 항과 분모의 상쇄: $\partial(A^a)^{-1}=-(D_j^a/A^a)(A^a)^{-1}$이 $W$의 미분에서 나온 $+D_j^a/A^a$와 지운다. 내부 vertex 항: $\partial\log Y_\beta=E^A[D_j/A\mid\mathscr F_{d_\beta}]$를 tree 기대값 안에 넣으면, 조건부 독립 때문에 $\beta$의 prefix에서 새 자식을 하나 더 뽑은 tree의 기대값이 된다. 새 tree에서 $n_\beta$는 하나 늘지만 표현은 원래 tree의 $\gamma_\beta$를 계수로 갖는다.

반복 적용할 때 넣은 $D_j^a$는 $G$에 흡수된다($G$는 계속 매개변수에 무관). 그래서 규칙이 차수마다 그대로 다시 쓰인다.
