---
id: models:spin.s2
kind: step
title: '대칭 coupling으로 (2.4) 확인'
uses: [models:spin.s1, model:positivity]
provides: 'models:spin.s3 (가정 (2.4))'
math: |
  대칭성 때문에 $b$ 의 모든 홀수 moment는 0이다. 짝수 moment는 음이 아니다.
physics: |
  $J$ 의 분포가 대칭이면 $b=\tanh(\beta J)$ 도 대칭이라 $\mathbb E[(-b)^n]$ 은 홀수 $n$ 에서 0, 짝수 $n$ 에서 $\mathbb E[b^n]\ge0$ 이다. 그래서 [[g:positivity|부호 조건]]이 모든 온도에서 성립한다.
gap: |
  정확하다. 원문은 두 사실만 적는다. "$\tanh$ 가 홀함수라 $b$ 의 분포가 대칭"과 "$\lvert b\rvert<1$ 이라 모든 moment가 유한한 실수"(model:positivity의 해석)는 작성자가 채운 연결이다. 대칭이 아닌 $J$ 에서 (2.4)가 성립하는지는 이 단계가 말하지 않는다.
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [30, 31]}
status: proposed
---
