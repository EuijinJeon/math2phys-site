---
id: models:ground.s2
kind: step
title: '각 $\beta$ 에서 주정리: $\limsup_Ng_N\le I(\beta)/\beta\le\liminf_Ng_N+\log2/\beta$'
uses: [models:ground.s1, main:theorem, models:spin, models:sat, x:cons-energy-score]
provides: 'models:ground.s3'
math: |
  고정한 각 $\beta>0$ 에서 main:theorem이 $P_N(\beta)\to I(\beta)$ 를 준다. 여기서 $I(\beta)=\inf_{r,\zeta,\mathbf m}\mathcal B_{r,\beta}(\zeta,\mathbf m)$ 이다. 그러므로
  $$\limsup_Ng_N\le\frac{I(\beta)}\beta\le\liminf_Ng_N+\frac{\log2}\beta.$$
physics: |
  각 온도에서 [[g:pressure|pressure]]의 극한이 변분값([[g:phi]])이라는 주정리를 s1의 끼움에 넣는다. 아직 $g_N$ 의 수렴은 모른다.
gap: |
  정확하다. 주정리의 [[g:hypotheses|가정]]은 models:spin, models:sat이 각 $\beta$ 에서 확인했다(원문은 main:theorem만 가리킨다). $P_N(\beta)$ 는 그 모형의 $F_N$ 이고 $I(\beta)=\inf_{r\ge0}\Phi_r$ 이다.
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [112, 119]}
status: proposed
---
