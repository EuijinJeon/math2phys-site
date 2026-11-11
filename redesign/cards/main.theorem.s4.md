---
id: main:theorem.s4
kind: step
title: '상한과 합쳐 극한의 존재와 (2.13)'
uses: [main:theorem.s3, upper:bound, x:model-hypotheses]
provides: 'main:theorem의 결론'
math: |
  upper:bound(main:theorem의 가정 아래, 모든 $N$ 과 모든 유한 단계 시행 법칙에서 $F_N\le\mathcal B_r(\zeta,\mathbf m)$)가 $\limsup_NF_N\le\inf_r\Phi_r$ 를 준다. main:theorem.s3의 $\liminf_NF_N\ge\inf_r\Phi_r$ 와 합치면 두 극한이 일치하고, 극한의 존재와 (2.13)이 증명된다.
physics: |
  상한(Guerra–Franz–Leone–Panchenko–Talagrand의 [[g:interpolation|interpolation]])과 하한이 같은 값 [[g:phi|$\inf_r\Phi_r$]]에서 만난다.
gap: |
  정확하다. 상한은 원래 $\theta$ 에 대해 바로 쓴다(상수 이동이나 truncation 없이). 상한은 [[g:hypotheses|가정]]을 모두 쓰고, 하한 쪽은 factorization을 main:theorem.s1에서만 쓴다.
abstraction: exact
children: []
source:
  - {file: reduction.tex, lines: [85, 87]}
status: proposed
---
