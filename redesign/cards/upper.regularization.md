---
id: upper:regularization
kind: step
title: '정규화: $a$ 떼기, $c$ 빼기, $\lambda<1$ 정규화 (4.2)'
uses: [upper:derivative.s1, upper:bound.s1, tree:insertion, tree:Y-recursion, tree:log-expansion, model:factorization, model:integrability, x:model-message]
provides: 'upper:remainder (전개할 정규화된 증분과 그 한계, $\lambda\uparrow1$ 극한의 정당화)'
math: |
  기대값을 취하기 전에 $a$ 를 떼므로 $\log a$ 의 적분 가능성은 필요 없다. $D_*=b\prod_\ell f_\ell(1)$, $c=\theta(1,\ldots,1)$ 로 두고 각 삽입 증분에서 $c$ 를 뺀다. 이 적분 가능한 뺄셈은 계수 $1,-p,p-1$ 의 결합에서 상쇄된다. 보간된 계는 고정한다. $0<\lambda<1$ 에 대해 정규화된 증분 각각을
  $$\log Y_0(1+\lambda D)-\log(1+\lambda D_*)\tag{4.2}$$
  로 바꾼다. 여기서 $Y_0$ 는 tree:log-expansion의 insertion recursion이다. 모든 spin 입력에 대해 비
  $$\frac{1+\lambda D}{1+\lambda D_*}=(1-w)+w\frac{1+D}{1+D_*},\qquad w=\frac{\lambda(1+D_*)}{1+\lambda D_*}\in[0,1]$$
  는 $e^{-2B(\theta)}$ 와 $e^{2B(\theta)}$ 사이에 있다. spin 입력의 임의 부분집합을 $q_x$ 들로 평균한 뒤에도 같다. 따라서 (4.2)의 절댓값은 $2B(\theta)$ 이하다. 각 고정 상호작용에 대해 $\lambda\uparrow1$ 의 수렴은 spin 입력과 message에 균일하고 유한 recursion이 그것을 보존한다. dominated convergence가 원하는 정규화된 증분을 회복한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: upper.tex, lines: [70, 94]}
status: proposed
---

**풀이 (작성자).** $a$ 와 $1+\lambda D_*$ 는 새 상호작용의 disorder만의 함수(새 root 변수)이므로 [[tree:insertion]]의 동차성으로 recursion 밖으로 나온다: $\log Y_0(a(1+D))=\log a+\log Y_0(1+D)$, 그리고 $c=\log a+\log(1+D_*)$ 이므로 $\log Y_0(a(1+D))-c=\log Y_0(1+D)-\log(1+D_*)$ 에 $\log a$ 가 없다. $\lvert c\rvert\le B(\theta)$ 라 $c$ 는 적분 가능하고, 세 삽입이 같은 법칙의 새 $\theta$ 를 쓰므로 $\mathbb Ec$ 가 $1-p+(p-1)=0$ 으로 상쇄된다.

$\frac{1+D}{1+D_*}=e^{\theta(s)-\theta(1,\ldots,1)}\in[e^{-2B},e^{2B}]$ 이고, 1과 이 값의 볼록 결합도 같은 구간에 있다. $q_x$ 평균도 볼록 결합이다. 이 root-가측 한계를 recursion이 보존한다([[tree:insertion]]의 단조성). 지배 함수 $2B(\theta)$ 는 (2.1)로 적분 가능하다. $1+D>0$, $1+D_*>0$ 은 $\lvert D\rvert,\lvert D_*\rvert<1$(엄격한 곱 한계와 $\lvert\bar f\rvert\le M$, [[upper:bound.s1]])에서 온다.

원문 81행이 `\cref{tree:log-expansion}`을 부르는 것은 $Y_0$ 의 정의 때문이다. 그 정의 자체는 [[tree:Y-recursion]]에 있다. [[x:model-hypothesis-remarks]] (iii)("$\log a$ 의 별도 적분 가능성은 가정하지 않는다")이 예고한 일이 이 단계다. 이 카드는 그 주석 카드를 쓰지 않고 스스로 처리한다.
