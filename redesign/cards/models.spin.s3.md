---
id: models:spin.s3
kind: step
title: '(2.1) 확인과 주정리 적용'
uses: [models:spin.s1, models:spin.s2, model:integrability, x:model-hypotheses, main:theorem]
provides: 'models:spin의 결론 (2.13)'
math: |
  $B(\theta_\beta)=\beta\lvert J\rvert$, $\lvert h_\beta\rvert=\beta\lvert H\rvert$ 이다. 따라서 main:theorem의 모든 가정이 성립한다.
physics: |
  coupling과 장의 1차 moment가 유한하면 ([[g:interaction|상호작용]]의 최대 크기가 $\beta\lvert J\rvert$, [[g:field|장]]이 $\beta H$) 1차 moment 조건 (2.1)이 성립하고, s1–s2와 합쳐 주정리의 [[g:hypotheses|가정]]이 모두 갖추어진다.
gap: |
  정확하다. $\mathbb EB(\theta_\beta)+\mathbb E\lvert h_\beta\rvert=\beta(\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert)<\infty$ 는 원문이 등식만 적고 남긴 한 줄이다(작성자 확인). 짝수 $p$ 는 진술에서 고정되어 있다.
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [31, 34]}
status: proposed
---
