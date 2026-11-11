---
id: decor:conditional-concentration.s3.s2
kind: step
title: '정규화 $J=\kappa(S^+)^2$의 하계'
uses: [decor:conditional-concentration.s3.s1, tree:reference-total, x:decor-mesh, x:decor-eta-regular]
provides: 'conditional-concentration.s3.s3, s6 (J로 나눔)'
math: |
  $\kappa(T)=\prod_{v\in\operatorname{Br}(T)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$ (tree:K)에 대해 $J=\kappa(S^+)^2$. 각 vertex의 $j=1$ 인자는 $-\delta$이고, $j\ge2$ 인자는 $|m_{d_v}-jm_{d_v+1}|=(j-1)m_{d_v}+j\delta\ge\eta/2$이다 ($L$이 크면, $d_v=q_v+1$). 따라서 $b=b(S)$에 대해 $|J|\ge c_{k,\eta}\delta^{2b}>0$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [332, 344]}
status: proposed
---

$j\ge2$ 인자의 수는 크기에만 의존하므로 그 곱은 $\eta$와 $k$에만 의존하는 양수로 아래가 눌린다. $\delta$ 인자는 vertex마다 하나, 두 사본이므로 $2b$개다. 실제로는 $m_{q_v+1}>\eta$이므로 $\eta/2$보다 나은 하계 $\eta$도 성립한다. 원문의 $\eta/2$는 약한 형태로 충분하다.
