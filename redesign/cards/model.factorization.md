---
id: model:factorization
kind: assumption
title: 'factor weight 전개 (2.3)'
uses: [model:integrability]
provides: 'upper:bound(upper.tex 63: 세 삽입을 $a(1+D)$ 꼴로, 나머지항 분해), main:theorem.s1(상수 이동으로 $a$ 제거와 순열 불변성), model:positivity의 $b$'
math: |
  모든 spin 조 $(s_1,\ldots,s_p)$ 에 대해
  $$e^{\theta(s_1,\ldots,s_p)}=a\Bigl(1+b\prod_{\ell=1}^pf_\ell(s_\ell)\Bigr),\qquad\Bigl\lvert b\prod_{\ell=1}^pf_\ell(s_\ell)\Bigr\rvert<1\quad\text{a.s.}\tag{2.3}$$
  인 표현이 존재한다. 여기서 $a>0$ 과 $b$ 는 실수 확률변수, $f_\ell:\{-1,1\}\to\mathbb R$ 은 한 무작위 함수의 독립 사본이고, $b$ 는 $f_\ell$ 들과 독립이다.
physics: |
  factor의 Boltzmann weight가 high-temperature(tanh) 전개 꼴 $a(1+b\prod_\ell f_\ell(s_\ell))$ 를 갖는다는 가정이다([[g:factorization]]). 가정에는 엄격한 곱 한계(모든 spin 조에서 a.s. $\lvert b\prod_\ell f_\ell(s_\ell)\rvert<1$)와 독립 구조($a>0$ 과 $b$ 는 실수 확률변수, $f_\ell$ 은 한 무작위 함수의 독립 사본, $b$ 는 $f_\ell$ 들과 독립)가 들어 있다. Viana–Bray에서는 $a=\cosh\beta J$, $b=\tanh\beta J$, $f(s)=s$ 이다.
gap: |
  예의 대응은 exact이고(models:spin 증명), 일반 꼴을 loop 전개로 읽는 것은 그림이다. 엄격한 곱 한계와 독립 구조는 가정의 일부이고 실제로 쓰인다: 비퇴화 경우(곱 항 $b\prod_\ell f_\ell$ 이 a.s. 0이 아닌 경우, 곧 $b=0$ a.s. 도 $\max_s\lvert f(s)\rvert=0$ a.s. 도 아닌 경우; model.tex 39–43)에 둘이 함께 $b$ 와 $\max_s\lvert f(s)\rvert$ 를 본질적으로 유계로 만들고(upper:bound.s1, upper.tex 24–34), $f_\ell$ 의 i.i.d.와 $b$ 의 독립이 상수 이동 뒤 법칙의 순열 불변성을 준다(main:theorem.s1, reduction.tex 56–58). 이 가정은 상한(P2)과 주정리 증명의 상수 이동에만 쓰이며, bounded 하한(§5–§8)은 쓰지 않는다(cavity.tex 13–14). $a$ 의 자유도와 $\log a$ 에 대한 조건 없음은 [[x:model-hypothesis-remarks]]에 있다.
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [25, 34]}
status: proposed
---

"모든 spin 조에 대해 a.s."의 엄격한 곱 한계는 각 $\ell$ 에서 $\lvert f_\ell(s_\ell)\rvert$ 를 최대로 하는 조를 택하면 $\lvert b\rvert\prod_\ell\max_s\lvert f_\ell(s)\rvert<1$ a.s. 와 같다. upper.tex 25–34가 이 꼴을 쓴다.
