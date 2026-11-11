---
id: tree:charging.s4
kind: step
title: '$|J|$ 하계와 상대 경계'
uses: [tree:charging.s3]
provides: 'tree:charging의 (tree:relative-charging)'
math: |
  지정된 각 vertex에서 $j=1$ 인자의 절댓값은 $\delta$이고, $j\geq2$이면
  $$|m_d-jm_{d+1}|=(j-1)m_d+j\delta\geq\eta.$$
  뒤쪽 인자의 수는 크기에만 의존한다. 따라서 $|J|\geq\delta^b\eta^{\sum_v(a_v-2)}$이고 결과가 따라 나온다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [449, 456]}
status: proposed
---

$m_d-jm_{d+1}=m_d-j(m_d+\delta)=-(j-1)m_d-j\delta$이고 $j\ge2$, $m_d\ge\eta$이므로 크기 $\ge m_d\ge\eta$. vertex $v$의 인자는 $j=1$ 하나와 $j=2,\ldots,a_v-1$의 $a_v-2$개다. 그래서 $\frac1{|J|}\sum|c_E|\le C_{q,k}\delta^b/(\delta^b\eta^{\sum(a_v-2)})$이고 $\sum_v(a_v-2)$는 $q,k$로 유계이다(작성자 풀이; $\eta\le1$에서 $\eta^{\sum(a_v-2)}$는 그 지수의 최댓값으로 아래에서 누른다).
