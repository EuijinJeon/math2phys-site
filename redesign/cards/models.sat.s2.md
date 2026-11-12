---
id: models:sat.s2
kind: step
title: '(2.3)과 (2.4) 확인: $0\le-b<1$'
uses: [models:sat.s1, model:factorization, model:positivity]
provides: 'models:sat.s3 (가정 (2.3), (2.4))'
math: |
  $a=1$, $b=e^{-\beta W}-1$, $f_\ell(s)=(1+\varepsilon_\ell s)/2$ 로 둔다. 함수들은 독립 사본이고 $b$ 와 독립이다. $0\le-b<1$ 이므로 엄격한 곱 조건과 모든 부호 부등식이 성립한다.
physics: |
  soft SAT의 factor weight는 이미 [[g:factorization|전개]] 꼴 $1+b\prod_\ell f_\ell$ 이다: $f_\ell$ 은 $\ell$ 번째 변수가 위반 값을 갖는지의 지시함수, $b=e^{-\beta W}-1\in(-1,0]$ 은 위반 한 번의 weight 감소다. $-b\ge0$ 이라 모든 $n$ 에서 $(-b)^n\ge0$ 이고 [[g:positivity|부호 조건]]이 점별로 성립한다.
gap: |
  정확하다. 원문이 한 문장으로 묶은 것을 풀면(작성자 확인): $f_\ell$ 은 $\varepsilon_\ell$ 이 i.i.d.라 한 무작위 함수의 독립 사본이고, $W$ 가 부호와 독립이라 $b$ 는 $f_\ell$ 들과 독립이다. $W\ge0$, $\beta>0$ 이면 $e^{-\beta W}\in(0,1]$ 이라 $0\le-b<1$ 이다. $f_\ell\in\{0,1\}$ 이므로 $\lvert b\prod_\ell f_\ell(s_\ell)\rvert\le\lvert b\rvert<1$ 이고, $(-b)^n\in[0,1)$ 이라 $\mathbb E[(-b)^n]$ 은 유한하고 음이 아니다.
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [59, 62]}
status: proposed
---
