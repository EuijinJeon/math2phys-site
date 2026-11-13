---
id: upper:remainder
kind: step
title: '볼록성: 나머지항의 $n$차 계수 (4.3)와 부호'
uses: [upper:regularization, upper:derivative.s1, upper:bound.s1, tree:log-expansion, tree:Q-rule, x:tree-sampling, model:factorization, model:positivity, model:chain, x:model-message, x:model-depth-zero]
provides: 'upper:derivative ($\lambda\uparrow1$ 에서 (4.1)). 규칙 P2'
math: |
  정규화된 증분에 tree:log-expansion을 적용한다. replica leaf $n$ 개의 tree $\mathcal T$ 위에서
  $$P_{\mathcal T}=\frac1N\sum_{i=1}^N\mathbb E_f\prod_{a=1}^nf(\sigma_i^a),\qquad B_{\mathcal T}=\mathbb E_{f,x}\prod_{a=1}^n\bar f(x^a).$$
  $\mathbb E_f$ 는 새 함수 $f$ 하나를 평균하며 곱의 $n$ 개 replica 인자가 그것을 공유한다. $\mathbb E_{f,x}$ 는 root를 포함해 새 message-label tree 전체도 평균한다. 이 함수와 message tree는 서로 독립이고 옛 tilted 계와도 독립이다. 따라서 $B_{\mathcal T}$ 는 고정 tree에서 결정적이고 $P_{\mathcal T}$ 는 옛 spin replica에 의존한다. $r=0$ 에서는 message 자체가 모든 replica leaf가 공유하는 root 변수다. 독립 균일 index와 $f$, 새 message label의 독립 사본을 평균하면 세 삽입에서 각각 $P_{\mathcal T}^p$, $P_{\mathcal T}B_{\mathcal T}^{p-1}$, $B_{\mathcal T}^p$ 가 나온다. 삽입된 $b$ 는 이 변수들과 독립이다. 그래서 결합된 정규화 증분의 $n$차 계수는
  $$-\frac{\lambda^n}{n}\mathbb E[(-b)^n]\,\mathbb E_{Q_n}\mathbb E\bigl[P_{\mathcal T}^p-pP_{\mathcal T}B_{\mathcal T}^{p-1}+(p-1)B_{\mathcal T}^p\bigr]\tag{4.3}$$
  이다. 정규화된 기준항들은 상쇄된다. tree 법칙 $Q_n$ 은 tree:log-expansion의 것이고 세 삽입에 공통이다. $\lambda<1$ 이면 급수는 절대수렴하고 각 삽입은 $\sum_{n\ge1}\lambda^n/n$ 으로 눌린다. $p$ 가 짝수이므로 $x\mapsto x^p$ 의 볼록성이 괄호를 0 이상으로 만들고, (2.4)가 (4.3)을 0 이하로 만든다. $\lambda\uparrow1$ 이 (4.1)을 증명한다.
physics: |
  $\lambda<1$ 로 정규화한 나머지항([[upper:regularization]])을 [[g:tree-law|tree 법칙]] $Q_n$ 으로 뽑은 $n$ 개 [[g:replica|replica]]의 tree 위에서 전개하면, $n$차 계수는 실제 spin 쪽 평균 $P$ 와 시행 [[g:message|message]] 쪽 평균 $B$ 에 대한 볼록성 잔차 $P^p-pPB^{p-1}+(p-1)B^p$ (짝수 $p$ 에서 $\ge0$)의 평균에 $-\frac{\lambda^n}{n}\mathbb E[(-b)^n]$ 을 곱한 것이다. [[g:positivity|부호 조건]]이 모든 차수에서 이것을 0 이하로 만들고, 급수는 $\lambda<1$ 에서 절대수렴한다. $\lambda\uparrow1$ 은 [[upper:regularization]]의 적분 가능한 지배 한계 $2B(\theta)$ 와 dominated convergence로 보내 (4.1)을 얻는다.
gap: |
  같은 내용이다. $P_{\mathcal T}$ 는 보간된 계에서 tilted kernel로 뽑은 replica tree 위의 무작위 양이고 $B_{\mathcal T}$ 는 고정 tree에서 결정적이다. 짝수 $p$ 와 (2.4)가 둘 다 여기서 쓰인다(홀수 $p$ 에서 괄호의 부호는 보장되지 않는다). $Q_n$ 을 물리 그림의 overlap tree 법칙으로 읽는 것은 [[g:tree-law]]의 물리 대응 칸에 intuition으로만 있다.
abstraction: exact
children: []
source:
  - {file: upper.tex, lines: [96, 126]}
status: proposed
---

**확인 (작성자).** 실제 상호작용에서 $\prod_{a=1}^nD^a=b^n\prod_{\ell=1}^p\prod_af_\ell(\sigma^a_{i_\ell})$ 이고, $i_\ell$ 은 독립 균일, $f_\ell$ 은 독립 사본이므로 $\ell$ 마다 $\frac1N\sum_i\mathbb E_f\prod_af(\sigma_i^a)=P_{\mathcal T}$ 가 되어 $P_{\mathcal T}^p$. cavity 상호작용은 spin 인자 하나($P_{\mathcal T}$)와 새 message 인자 $p-1$ 개($B_{\mathcal T}^{p-1}$), edge는 $B_{\mathcal T}^p$. 새 message tree가 $\mathcal T$ 의 모양을 따라 prefix를 공유하므로 $B_{\mathcal T}$ 가 $\mathcal T$ 에 의존한다([[x:tree-sampling]]). 기준항 $-\log(1+\lambda D_*)=\sum_n(-1)^n\lambda^nD_*^n/n$ 의 기대값은 세 삽입에서 같은 법칙이라 계수 $1-p+(p-1)=0$ 으로 상쇄된다. $(-1)^{n-1}b^n=-(-b)^n$ 이 (4.3)의 앞 부호다.

볼록성: $x^p$ 는 짝수 $p$ 에서 $\mathbb R$ 위 볼록이므로 $x^p\ge y^p+py^{p-1}(x-y)$, 곧 $x^p-pxy^{p-1}+(p-1)y^p\ge0$ ($x=P_{\mathcal T}$, $y=B_{\mathcal T}$).

수렴 영역: 원문이 따로 적지 않는 조건 $\lvert\lambda D\rvert<1$ (root 조건부)은 $\lvert D\rvert\le\lvert b\rvert\prod_\ell M_\ell<1$ 에서 온다([[upper:bound.s1]]의 곱 한계). $\lambda\uparrow1$ 에서 급수의 각 항이 0 이하이므로 극한도 0 이하다; 극한 교환은 [[upper:regularization]]의 dominated convergence다.

$r=0$: 원문 108–109 "the message itself is a root variable shared by all replica leaves"는 $B_{\mathcal T}=\mathbb E_{f,x}\bar f(x)^n$ 이 된다는 뜻으로 읽었다([[x:model-depth-zero]]).
