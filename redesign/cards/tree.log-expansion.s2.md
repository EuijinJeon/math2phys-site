---
id: tree:log-expansion.s2
kind: step
title: '해석성, 수렴 영역, 꼬리 경계'
uses: [tree:log-expansion.s1, x:tree-analytic-bounds]
provides: 'tree:log-expansion의 (tree:log-series), (tree:log-tail)'
math: |
  해석성이 (tree:log-series)를 증명한다. 계수의 절댓값은 $\|D\|_\infty^k/k$ 이하이고, 이것이 말한 수렴 영역과 (tree:log-tail)을 증명한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [254, 257]}
status: proposed
---

$\log Y_0$는 $|t|\|D\|_\infty<1$에서 $t$의 해석함수이므로([[x:tree-analytic-bounds]]) 원점의 Taylor 급수가 그 원판에서 수렴해 함수와 같다. $k$차 계수 $\frac{(-1)^{k-1}}{k}\mathbb E_{Q_k}E_{\mathcal T}\prod D^a$의 크기는 $\|D\|_\infty^k/k$ 이하이므로 $|t|\|D\|_\infty\le c$에서 $K$차 뒤의 나머지는 $\sum_{k>K}c^k/k$ 이하다.
