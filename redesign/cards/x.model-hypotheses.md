---
id: x:model-hypotheses
kind: assumption
title: '주정리의 가정 묶음'
uses: [model:integrability, model:hamiltonian, model:factorization, model:positivity]
provides: 'main:theorem의 가정. upper:bound 진술의 "Under the hypotheses of main:theorem"(upper.tex 12)이 실제로 받는 것'
math: |
  고정한 짝수 $p\ge2$, $\alpha>0$ 과 model:hamiltonian의 모형에 대해 (2.1) $\mathbb EB(\theta)+\mathbb E\lvert h\rvert<\infty$, (2.3)의 표현과 엄격한 곱 한계, (2.4) $\mathbb E[(-b)^n]\ge0$ $(n\ge1)$ (유한한 실수 기대값으로 해석). 원문 표현은 "Under (2.1)–(2.4)"(식 라벨 model:integrability–model:positivity)이며 이 범위가 (2.1)–(2.4)이므로 (2.2) 모형 정의도 포함한다.
physics: |
  [[g:hypotheses|가정]]: 짝수 $p$, 상호작용과 장의 1차 moment, tanh형 [[g:factorization|factor 전개]], 그 전개 계수 $b$ 의 [[g:positivity|부호 조건]].
gap: |
  역할이 갈린다. 상한(upper:bound)은 모두 쓴다. 하한은 bounded이고 [[g:permutation-invariance|순열 불변]]인 상호작용과 bounded 장만 요구하며(comp:bounded-lower) factorization과 positivity를 쓰지 않는다. 주정리 증명은 factorization을 상수 이동의 대칭화에 한 번 쓰고(main:theorem.s1), (2.1)을 [[g:truncation|truncation]]의 dominated convergence에 쓴다(main:theorem.s2).
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [3, 8]}
  - {file: model.tex, lines: [25, 38]}
  - {file: model.tex, lines: [130, 131]}
status: proposed
---

이 카드는 원문에 없는 묶음이다. `upper:bound` 카드가 `main:theorem` 대신 이 카드를 `uses`에 넣으면 `main:theorem` → `upper:bound` 방향과 순환하지 않는다. 원문 범위는 가정의 진술(model.tex 3–8의 (2.1), 25–38의 (2.3)·(2.4))과 그것을 이름으로 부르는 `main:theorem`의 줄 130–131이다. 뒤의 범위를 함께 두는 것은 의존 검사가 대상 라벨(`main:theorem`, model.tex 130)의 위치가 `uses`한 카드의 범위에 드는지로 허용 여부를 보기 때문이다. (2.2) 모형 정의(9–23)는 가정이 아니라 대상이므로 `uses`의 model:hamiltonian으로 가리키고 범위에 넣지 않았다.
