---
id: tree:charging.s1
kind: step
title: '한 걸음의 절댓값 계수 합'
uses: [tree:telescoping, x:tree-extension-history]
provides: 'tree:charging.s3'
math: |
  현재 tree의 leaf가 $s$개이면 (tree:telescoping)은 모든 fresh 선택의 절댓값 계수 합이 $s$라고 말한다. 자격 있는 old 선택은 많아야 $s$개다. 그래서 제한 없는 걸음의 절댓값 계수 합은 $2s\leq2(q+k)$ 이하다. 고정된 깊이에는 vertex가 많아야 $s$개다. 걸음을 처방된 깊이의 unary vertex에서의 fresh divergence로 제한하면 절댓값 계수 합은 $s\delta$ 이하다. 그런 divergence의 계수가 각각 $m_d-m_{d+1}=-\delta$이기 때문이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [417, 425]}
status: proposed
---

fresh 계수 $\gamma_\beta$는 모두 음이고 $\sum_\beta|\gamma_\beta|=s$([[tree:telescoping]] 메모). 걸음 중 $s\le q+k$이고, 원문은 뒤에서 $s\delta\le(q+k)\delta$로 쓴다(441).
