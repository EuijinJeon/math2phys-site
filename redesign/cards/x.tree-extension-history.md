---
id: x:tree-extension-history
kind: definition
title: 'canceled-anchor 확장 규칙과 extension history $E$'
uses: [x:tree-sampling, tree:insertion]
provides: 'tree:extension-expansion의 합 범위와 c_E. x:tree-reference-paths, tree:reference-total, tree:charging. §6 x:pert-colored-extensions (perturbations.tex 427–436: added color의 배치와 𝔈(T,a_*,C))'
math: |
  anchor leaf $a_*$를 가진 tree $\mathcal T$를 고정한다. 그 모든 old path에서 시작해 color $1,\ldots,k$를 그 순서로 준다. 다음 color에 대해 다음 둘 중 하나를 할 수 있다.
  (i) $a_*$가 아닌, 아직 쓰지 않은 old leaf를 고른다. 계수 $1$.
  (ii) 현재 tree의 임의의 내부 vertex $\beta$에서 fresh path를 만든다. 계수 $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$.
  각 fresh path는 갈라지는 vertex에서 새 자식을 쓰고 그보다 깊은 모든 깊이에서 새 vertex를 쓴다. 고른 leaf는 그 color를 받고 다시 고를 수 없다. 현재 tree는 쓰지 않은 것을 포함한 모든 old path와 이미 더한 모든 path를 포함한다. extension history $E$는 이 선택들을 기록한다. $a_j(E)$는 color $j$를 가진 leaf, $\mathcal T_E$는 최종 tree, $c_E$는 계수들의 곱이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [259, 276]}
status: proposed
---

[[g:extension-history|extension history]]. $n_\beta$는 그 시점의 현재 tree(쓰지 않은 old path와 이미 더한 path를 모두 포함)에서의 자식 수다. 그래서 같은 vertex라도 앞선 선택에 따라 계수가 달라진다. anchor $a_*$는 처음부터 [[g:protected-leaf|protected]]이므로(그 인자 $A^{a_*}$가 상쇄되어 있다) (i)에서 고를 수 없다. 이 규칙이 [[x:tree-differentiation-rule]]을 $C=\{a_*\}$에서 시작해 반복한 결과와 같다는 것이 [[tree:extension-expansion]]이다.

§6은 이 규칙을 그대로 받아 anchor를 color 0으로 두고 제약 $\mathcal C$로 허용 history를 고른다(perturbations.tex 429–436).
