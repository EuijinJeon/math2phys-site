---
id: models:sat
kind: corollary
title: 'soft random 짝수 $K$-SAT (Corollary 10.2)'
uses: [x:cons-standard-examples, model:hamiltonian, model:integrability, model:factorization, model:positivity, x:model-hypotheses, model:functional, main:theorem]
provides: 'models:ground (consequences.tex 88: 대상 모형, $\mathbb EW<\infty$), x:cons-energy-score (법칙 $W$, $\varepsilon_\ell$), x:cons-3sat-remark (consequences.tex 132: 짝수 체수 가정). introduction.tex 30–31("soft random even-$K$ SAT at every positive temperature"), L0, g:named-models, g:positivity의 물리 대응 칸. §2 부호 조건의 명명 예시이지만 §2 카드가 받아 쓰지는 않는다'
math: |
  짝수 정수 $K\ge2$ 와 $\alpha>0$ 을 고정한다. $\varepsilon_1,\ldots,\varepsilon_K$ 는 독립인 공정한 부호이고, $W\ge0$ 은 부호들과 독립이며 $\mathbb EW<\infty$ 이다. 모든 $\beta>0$ 에 대해 상호작용
  $$\theta_\beta(s_1,\ldots,s_K)=-\beta W\prod_{\ell=1}^K\frac{1+\varepsilon_\ell s_\ell}{2},\qquad h=0$$
  은 (2.13)을 만족한다. $W=1$ 이 soft random 짝수 $K$-SAT 모형이고, 일반 $W$ 는 독립인 음이 아닌 clause 가중치를 준다.
physics: |
  clause 밀도 $\alpha$ 의 random 짝수 $K$-SAT([[x:cons-standard-examples]]의 Poisson 개수·복원추출)에서, 각 clause의 부호 $\varepsilon_{\ell,k}$ 는 독립인 공정한 부호이고, 각 clause $k$ 는 모든 자리 $\ell$ 에서 $\sigma_{i_{\ell,k}}=\varepsilon_{\ell,k}$ 일 때 위반되고, 위반된 clause마다 에너지 $W_k\ge0$ 을 치른다(Boltzmann weight $e^{-\beta W_k}$ 의 soft constraint, 외부장 없음). $W$ 가 부호와 독립이고 $\mathbb EW<\infty$ 이면 모든 온도 $\beta>0$ 에서 quenched [[g:pressure|pressure]]의 열역학 극한이 존재하고 모든 유한 [[g:rsb-steps|RSB 단계 수]]의 시행값([[g:functional]])의 [[g:phi|inf]]와 같다.
gap: |
  (1) $K$ 는 짝수다. 3-SAT 같은 홀수 $K$ 는 제외된다(x:cons-3sat-remark). (2) "모든 $\beta>0$"이 원문의 범위다. $\beta=\infty$ 의 hard constraint(해의 존재나 해 공간)는 이 따름정리가 다루지 않고, 영온도 쪽은 models:ground의 최댓값 밀도로만 다룬다. (3) clause 개수는 Poisson$(\alpha N)$ 이고 변수는 복원추출이라 한 clause 안에 같은 변수가 되풀이될 수 있다(작성자 관찰). 고정 개수·서로 다른 변수의 표준 앙상블과의 동치는 다루지 않는다. (4) 어느 온도에서 몇 단 RSB가 필요한지, inf가 달성되는지는 말하지 않는다(x:model-theorem-scope). (5) 증명은 주정리의 [[g:hypotheses|가정]]을 확인할 뿐이다.
abstraction: exact
children: [models:sat.s1, models:sat.s2, models:sat.s3]
source:
  - {file: consequences.tex, lines: [36, 49]}
  - {file: consequences.tex, lines: [51, 64]}
status: proposed
---

**증명의 뼈대.**

- [[models:sat.s1]]: 곱 $I_\varepsilon(s)$ 가 위반 지시함수이므로 $e^{\theta_\beta}=1+(e^{-\beta W}-1)I_\varepsilon$.
- [[models:sat.s2]]: $a=1$, $b=e^{-\beta W}-1$, $f_\ell(s)=(1+\varepsilon_\ell s)/2$ 로 (2.3)의 구조, 그리고 $0\le-b<1$ 에서 엄격한 곱 한계와 (2.4).
- [[models:sat.s3]]: $B(\theta_\beta)=\beta W$ 로 (2.1), 그러므로 [[main:theorem]]이 적용된다.

모형의 체수 $p$ 가 여기서는 $K$ 다. 장은 $h=0$(0에 놓인 점질량)이라 $\mathbb E\lvert h\rvert=0$ 이다.

**위반의 약속.** $I_\varepsilon(s)=1$ 은 모든 $\ell$ 에서 $s_\ell=\varepsilon_\ell$ 일 때다(작성자 확인: 각 인자 $(1+\varepsilon_\ell s_\ell)/2$ 는 $s_\ell=\varepsilon_\ell$ 이면 1, 아니면 0). 원문은 이것을 "indicates a violated clause"라고만 적는다(54행). 그러니 $\varepsilon_\ell$ 은 clause를 위반하게 하는 $\ell$ 번째 변수의 값이다.
