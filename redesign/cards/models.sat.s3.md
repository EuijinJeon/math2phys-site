---
id: models:sat.s3
kind: step
title: '(2.1) 확인과 주정리 적용'
uses: [models:sat.s2, model:integrability, x:model-hypotheses, main:theorem]
provides: 'models:sat의 결론 (2.13)'
math: |
  또 $B(\theta_\beta)=\beta W$ 이므로 main:theorem이 적용된다.
physics: |
  한 clause가 치를 수 있는 최대 에너지는 $\beta W$ 이고 $\mathbb EW<\infty$ 라 1차 moment 조건이 성립한다. s2와 합쳐 주정리의 [[g:hypotheses|가정]]이 모두 갖추어진다.
gap: |
  정확하다. $B(\theta_\beta)=\max_s\lvert\theta_\beta(s)\rvert=\beta W$ 는 $s_\ell=\varepsilon_\ell$ 인 조에서 $I_\varepsilon=1$ 이 되기 때문이고, $\mathbb EB(\theta_\beta)+\mathbb E\lvert h\rvert=\beta\mathbb EW<\infty$ 다(작성자 확인; 원문은 $B(\theta_\beta)=\beta W$ 만 적는다). 짝수 $K$ 는 진술에서 고정되어 있다(이 단계는 짝수를 쓰지 않는다. 쓰이는 곳은 상한의 볼록성, upper.tex 123–124).
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [62, 64]}
status: proposed
---
