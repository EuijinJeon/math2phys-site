---
id: tree:insertion.s3
kind: step
title: '단조성과 동차성'
uses: [tree:Y-recursion]
provides: 'tree:insertion의 마지막 문단. §4 upper.tex 53–54, 91–92; §5 cavity.tex 37–38, 95–96, 108–109의 log Y_0 상계; §6 perturbations.tex 64–65 (모두 \ref 없는 사용)'
math: |
  단조성과 동차성은 (tree:Y-recursion)에서 backward induction으로 바로 나온다: $a\le Y_d\le b$이면 $a^{m_d}\le K_dY_d^{m_d}\le b^{m_d}$이므로 $a\le Y_{d-1}\le b$ ($a,b$는 root-가측이므로 kernel 적분에서 상수). $A\mapsto cA$이면 $Y_d\mapsto cY_d$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [131, 133]}
status: proposed
---

원문은 "follow at once by backward induction"(131–132)이라고만 쓴다. math 칸의 한 줄 유도는 작성자가 풀어 쓴 것이다.
