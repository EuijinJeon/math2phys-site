---
id: x:pert-order-of-choices
kind: remark
title: '선택의 순서 (Remark 6.6)'
uses: [pert:factor, x:pert-parameter-measure, pert:selection, pert:analytic, pert:tree-identity]
provides: 'g:order-of-limits(§6 안의 j 극한), g:selected-sequence의 정의 위치. §7 decorrelation.tex 4–9, 613–623이 같은 순서(고정 $L$에서 $N$ 먼저)를 스스로 다시 적는다(§7 카드가 받아 쓰지는 않는다)'
math: |
  mark specification과 그 양의 가중치 $c_\nu$ 는 고정된 $L$ 에 대해 먼저 고정된다. 그다음 매개변수 평균이 모든 type이 집중하고 모든 유한 overlap moment가 수렴하는 선택된 수열 하나를 준다. 해석적 논증은 각 $j$ 를 고정하고 $N\to\infty$ 한 뒤 $j\to\infty$ 로 보낸다. 그렇게 얻은 prescribed-tree 항등식이 세워진 뒤에야 $L$ 을 키운다. 가산 족 전체에 균등한 집중 추정은 필요 없다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [538, 547]}
status: proposed
---

순서를 한 줄로 쓰면: $L$ 고정 → 족과 $c_\nu$ 고정 → ($\varepsilon$ 고정) → $\pi$ 평균으로 수열 선택 → 각 $j$ 에서 $N\to\infty$ → $j\to\infty$ → 항등식 → (§7, §8에서) $L\to\infty$. [[g:order-of-limits]]. "모든 type이 집중"은 type마다의 수렴이다(type에 균등하지 않다).
