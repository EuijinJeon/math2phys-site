---
id: tree:extension-expansion.s2
kind: step
title: '$\boldsymbol t=0$ 에서 계수만 남는다'
uses: [tree:extension-expansion.s1, tree:Y-recursion]
provides: 'tree:extension-expansion의 (tree:mixed-expansion)'
math: |
  $\boldsymbol t=0$에서 모든 인자 $A$와 $Y$는 $1$이다. 이것이 주장한 규칙과 그 계수를 증명한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [302, 304]}
status: proposed
---

$A_{\boldsymbol 0}=1$이면 (tree:Y-recursion)에서 모든 $Y_d=1$이고 $K_d^A=K_d$이므로 $E^{A}_{\mathcal T_E}=E_{\mathcal T_E}$, 분모 $A^a$도 모두 1이다. 같은 방향 $D_j=D$일 때 $t^k$ 계수가 우변$/k!$인 것은 Taylor 계수의 정의다.
