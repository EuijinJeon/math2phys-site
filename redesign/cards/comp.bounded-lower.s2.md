---
id: comp:bounded-lower.s2
kind: step
title: '$L\to\infty$, 그다음 $\varepsilon\downarrow0$'
uses: [comp:bounded-lower.s1, comp:insertion-comparison, x:comp-standing, x:pert-selected-limits]
provides: 'comp:bounded-lower의 결론'
math: |
  안쪽 극한은 그 깊이의 선택된 수열을 쓴다. comp:insertion-comparison에서 $L\to\infty$ 로 보내면 $A\le\underline F+2\varepsilon$ 이고, 그다음 $\varepsilon\downarrow0$ 이 결론을 증명한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [243, 246]}
status: proposed
---

s1의 부등식에서 좌변 $A$ 와 $\underline F$ 는 $L$ 에 의존하지 않으므로, $L\to\infty$ 를 보내면 (comp:increment-comparison)으로 마지막 항이 0이다. 이 $\lim_L\limsup_N$ 은 고정 $\varepsilon$ 에 대한 진술이고, 각 $L$ 의 수열은 그 $\varepsilon$ 의 것이다([[x:comp-standing]]). $A\le\underline F+2\varepsilon$ 은 모든 $\varepsilon>0$ 에서 성립하므로 $A\le\underline F=\liminf_NF_N$ (모든 크기에 대한 liminf).
