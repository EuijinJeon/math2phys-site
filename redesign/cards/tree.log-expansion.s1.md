---
id: tree:log-expansion.s1
kind: step
title: '$k$차 도함수 = $(-1)^{k-1}(k-1)!\,\mathbb E_{Q_k}$'
uses: [tree:first-variation, x:tree-differentiation-rule, tree:telescoping, tree:Q-rule]
provides: 'tree:log-expansion.s2'
math: |
  (tree:first-variation)에 의해 1차 도함수는 updated path 하나 위의 $D/A$의 기대값이다. 그 leaf를 protected로 둔다. 이후의 모든 도함수는 fresh path를 붙이는 것밖에 할 수 없다. 현재의 leaf가 모두 protected이기 때문이다. 차수 $k$에서 $k-1$개의 fresh 계수는 모두 음이다. (tree:telescoping)으로 정규화하면 그 절댓값의 곱은 $Q_k$의 확률의 $(k-1)!$배다. 따라서
  $$\left.\frac{d^k}{dt^k}\log Y_0\right|_{t=0}=(-1)^{k-1}(k-1)!\,\mathbb E_{Q_k}E_{\mathcal T}\prod_{a=1}^kD^a.$$
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [241, 253]}
status: proposed
---

$n$개 leaf가 있을 때 vertex $\beta$의 fresh 계수는 $\gamma_\beta=-(n_\beta m_{d_\beta+1}-m_{d_\beta})=-n\,Q(\beta)$이고($Q(\beta)$는 [[tree:Q-rule]]의 선택 확률), $n=1,\ldots,k-1$에 대해 곱하면 $(-1)^{k-1}(k-1)!\prod Q$. $t=0$에서 모든 $A$와 $Y$가 1이므로 $E^A$는 $E$가 되고 남는 것은 leaf의 $D^a$들이다. 차례로 붙는 path의 순서가 $Q_k$의 label 순서와 같다(작성자 풀이).
