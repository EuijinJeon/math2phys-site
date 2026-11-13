---
id: x:cavity-bounded
kind: assumption
title: '하한의 유계·순열 불변 가정 ($B(\theta)\le B$, $\lvert h\rvert\le H$)'
uses: [model:integrability, model:hamiltonian]
provides: '§5–§8 전체("Until reduction:section"): cavity:increment.s2–s4의 상수 $B$, $H$, cavity:increment.s1의 새 입력을 마지막 좌표에 두는 일, x:cavity-tree-sampling의 "bounded fields". x:pert-standing (perturbations.tex 3–8), x:pert-increment (perturbations.tex 249–250 "for the bounded model"), comparison.tex 200·226의 bounded 가정. 이 가정을 푸는 것은 reduction.tex(main:theorem.s1–s3)'
math: |
  reduction:section까지 $B(\theta)\le B$ 와 $\lvert h\rvert\le H$ 가 a.s. 성립하고, $\theta$ 의 법칙이 $p$ 개 좌표의 순열에 대해 불변이라고 가정한다. 하한에서는 factorization도 positivity 가정도 쓰지 않는다.
physics: |
  하한 쪽(§5–§8)은 [[g:bounded-law|유계]]이고 입력에 대해 대칭([[g:permutation-invariance|순열 불변]])인 [[g:interaction|상호작용]]과 유계 [[g:field|장]]만 다룬다. [[g:factorization|factor 전개]]와 [[g:positivity|부호 조건]]은 쓰지 않는다.
gap: |
  같은 내용이다. "쓰지 않는다"는 원문이 미리 하는 말이고 §5–§8 카드 전체에서 확인할 일이다(이 카드 자체는 증명하지 않는다). 일반 법칙으로의 확장은 [[g:constant-shift|상수 이동]]과 [[g:truncation|truncation]]으로 reduction.tex에서 한다(main:theorem.s1–s3). 짝수 $p$ 는 논문 전체의 고정 가정으로 남아 있다(model:integrability).
abstraction: exact
children: []
source:
  - {file: cavity.tex, lines: [11, 14]}
status: proposed
---

11행의 `\cref{reduction:section}`은 원문상 뒤에 나오는 절을 가리키는 예고라서 `uses`에 넣지 않았다.
