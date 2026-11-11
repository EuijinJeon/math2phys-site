---
id: x:model-depth-zero
kind: convention
title: '$r=0$ (replica symmetric) 경우: $\mathcal B_0(\zeta)$, $\Phi_0$'
uses: [model:functional, model:chain, model:vs, model:ve]
provides: 'main:theorem의 $\inf_{r\ge0}$ 에 $r=0$ 을 포함시킴. reduction:stability("including $r=0$"), model:trial-bounds'
math: |
  $r=0$ 에서는 message들이 공통 법칙 $\zeta\in\mathcal P(\mathbb R)$ 를 갖는 독립 변수이고 연산자 $T_d$ 는 생략한다. 이것이 $\mathcal B_0(\zeta)=\log2+\mathbb E\log V_{\rm s}-\alpha(p-1)\mathbb E\log V_{\rm e}$ 와 $\Phi_0=\inf_\zeta\mathcal B_0(\zeta)$ 를 정한다.
physics: |
  replica symmetric(RS) Bethe free entropy: cavity field가 한 분포 $\zeta$ 에서 독립으로 뽑힌다([[g:order-parameter]]의 $r=0$, [[g:rsb-steps|RSB 단계 수]] 0).
gap: |
  $\mathcal B_0$ 의 식은 (2.11)에서 $T_0$ 을 지운 것으로 작성자가 적었다. 원문은 "the operators $T_d$ are omitted; this defines $\mathcal B_0(\zeta)$ and $\Phi_0$"라고만 쓴다. 물리의 RS 해는 정류점이고 여기서는 inf다.
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [118, 120]}
status: proposed
---
