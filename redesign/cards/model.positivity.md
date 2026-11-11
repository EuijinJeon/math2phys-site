---
id: model:positivity
kind: assumption
title: '부호 조건 (2.4)'
uses: [model:factorization]
provides: 'upper:bound(upper.tex 125: 나머지항 \eqref{upper:remainder}가 0 이하). main:theorem의 가정'
math: |
  (2.3)의 $b$ 에 대해
  $$\mathbb E[(-b)^n]\ge0\qquad(n\ge1).\tag{2.4}$$
  이 기대값들은 유한한 실수 기대값으로 해석한다.
physics: |
  coupling의 tanh $b$ 에 대한 부호 조건([[g:positivity]])이다. 대칭 coupling(홀수 moment가 0, 짝수 moment는 자동으로 $\ge0$)과 soft SAT($-1<b\le0$)에서 성립한다(models:spin, models:sat 증명).
gap: |
  "frustration이 대칭이거나 반강자성 쪽"이라는 읽기는 그림이고 일반적인 동치 조건이 아니다. 이 조건은 상한에만 쓰이고 하한에는 쓰이지 않는다(cavity.tex 13–14). 기대값의 유한성이 자동인 경우는 [[x:model-hypothesis-remarks]].
abstraction: weakening
children: []
source:
  - {file: model.tex, lines: [35, 38]}
status: proposed
---

soft SAT에서는 $a=1$, $b=e^{-\beta W}-1$, $f_\ell(s)=(1+\varepsilon_\ell s)/2$ 이고 $0\le-b<1$ 이라 모든 $n$ 에서 $(-b)^n\ge0$ 이다(consequences.tex 52–61). 대칭 coupling에서는 $b=\tanh\beta J$ 의 홀수 moment가 0이고 짝수 moment가 $\ge0$ 이다(consequences.tex 26–32).
