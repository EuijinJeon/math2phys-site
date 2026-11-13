---
id: x:cavity-root-convention
kind: convention
title: '섭동의 개수·type·site는 root, 매개변수 $\mathbf u$ 는 고정값'
uses: [cavity:factor-bounds]
provides: 'cavity:negligible, cavity:increment (균일성 "in $\mathbf u$"의 뜻), x:cavity-root-logarithm. pert:factor, x:pert-parameter-measure (perturbations.tex 60–70: "Counts, types, and sites belong to the root", $\pi$ 는 매개변수를 고를 때만), g:root, g:disorder의 정의 위치'
math: |
  factor의 총 개수는 $\mathrm{Pois}(s_N)$ 이고 a.s. 유한하다. 개수, type, site는 root 변수다. factor의 매개변수는 $\mathbf u$ 로 쓰며, 매개변수 평균을 명시적으로 취하지 않는 한 quenched 확률변수가 아니라 고정값이다. 뒤에 필요한 factor는 pert:section에서 정한다.
physics: |
  [[g:perturbation|섭동]] factor의 개수·type·site는 [[g:root]] 변수로서 물리 [[g:disorder|disorder]]와 함께 바깥 기대값이 평균한다. 섭동 매개변수 $\mathbf u$ 는 무작위 변수가 아니라 고정된 값이고, 매개변수에 대한 평균은 따로 명시할 때만 취한다.
gap: |
  같은 내용이다. 이 약속 때문에 뒤의 분산과 기대값은 고른 $\mathbf u$ 에서 취하며 $\mathbf u$ 에 대해 평균하지 않는다. 매개변수 평균은 perturbations.tex의 $\pi$ 로 명시될 때만 나온다.
abstraction: exact
children: []
source:
  - {file: cavity.tex, lines: [28, 32]}
status: proposed
---

32행의 `\cref{pert:section}`은 원문상 뒤의 절을 가리키는 예고라서 `uses`에 넣지 않았다.
