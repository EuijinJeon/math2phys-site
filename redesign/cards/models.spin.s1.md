---
id: models:spin.s1
kind: step
title: 'tanh 전개로 (2.3) 확인'
uses: [model:factorization]
provides: 'models:spin.s2 ($b=\tanh(\beta J)$, $\lvert b\rvert<1$ a.s.), models:spin.s3'
math: |
  $$a=\cosh(\beta J),\qquad b=\tanh(\beta J),\qquad f_\ell(s)=s$$
  로 둔다. 함수 $f_\ell$ 들은 결정적인 독립 사본이고, $\lvert b\rvert<1$ a.s. 이다.
physics: |
  $\prod_\ell s_\ell=\pm1$ 이므로 factor weight는 고온 전개 $e^{\beta J\prod_\ell s_\ell}=\cosh(\beta J)\bigl(1+\tanh(\beta J)\prod_\ell s_\ell\bigr)$ 이다. 이것이 (2.3)의 [[g:factorization|tanh형 전개]]이고 $\lvert\tanh\rvert<1$ 이 엄격한 곱 한계다.
gap: |
  정확하다. 전개 등식 자체는 원문이 적지 않고 $a,b,f_\ell$ 만 준다. 등식은 $x=\pm1$ 에서 $e^{\beta Jx}=\cosh(\beta J)+x\sinh(\beta J)$ 인 데서 나온다(작성자 확인). $\lvert b\prod_\ell f_\ell(s_\ell)\rvert=\lvert\tanh(\beta J)\rvert<1$ 은 $J$ 가 실수 값이라 a.s. 이다.
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [24, 30]}
status: proposed
---

(2.3)의 나머지 구조 조건도 확인된다(작성자 확인). $a=\cosh(\beta J)>0$ 은 $J$ 에 의존해도 된다([[x:model-hypothesis-remarks]] (iii)이 허용하는 것). $f_\ell$ 은 결정적이므로 "한 무작위 함수의 독립 사본"이고 $b$ 와 독립이라는 조건이 자명하게 성립한다. 원문 29행의 "deterministic independent copies"가 이것을 말한다.
