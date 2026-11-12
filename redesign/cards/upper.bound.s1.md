---
id: upper:bound.s1
kind: step
title: '퇴화 경우와 $b$, $M$ 의 본질적 유계성'
uses: [model:factorization, model:integrability, model:hamiltonian, model:functional, model:vs, model:ve]
provides: 'upper:regularization, upper:remainder (모든 moment의 유한성). x:model-moment-finiteness가 예고한 증명(model.tex 39–41)'
math: |
  $M=\max_{s=\pm1}\lvert f(s)\rvert$ 로 둔다. $b=0$ a.s. 이거나 $M=0$ a.s. 이면 상호작용은 spin 무관인 무작위 상수 $c$ 이고, 모든 시행 법칙에 대해
  $$F_N=\mathcal B_r=\log2+\mathbb E\log\cosh h+\alpha\mathbb Ec.$$
  그렇지 않으면 $\mathbb P(M\ge u)>0$, $\mathbb P(\lvert b\rvert\ge v)>0$ 인 $u,v>0$ 을 고른다. $\lvert b\rvert\prod_{\ell=1}^pM_\ell<1$ a.s. 이므로 독립성에서
  $$\lVert b\rVert_\infty\le u^{-p},\qquad\lVert M\rVert_\infty\le(vu^{p-1})^{-1}.$$
  실제로 어느 한계든 양의 확률 집합에서 어기고 나머지 독립 인자를 이 하계로 제한하면 엄격한 곱 조건을 어기게 된다. 따라서 이후에 쓰는 모든 moment는 유한하다.
physics: |
  [[g:factorization|factor 전개]]의 곱 항이 없으면 factor는 spin과 무관한 상수 $e^c$ 이고, [[g:pressure|pressure]]와 모든 시행값([[g:functional]])이 같은 값 $\log2+\mathbb E\log\cosh h+\alpha\mathbb Ec$ 가 된다. 곱 항이 있으면 $b$ 와 $f$ 가 서로 독립이고 곱이 a.s. 1 미만이라는 데서 둘 다 본질적으로 유계다.
gap: |
  같은 내용이다. 유계 상수 $u^{-p}$, $(vu^{p-1})^{-1}$ 은 1보다 클 수 있다($f\mapsto\lambda f$, $b\mapsto\lambda^{-p}b$ 의 척도 자유, x:model-moment-finiteness 카드의 관찰). "$b$ 가 tanh처럼 1 미만"을 말하는 것은 아니다.
abstraction: exact
children: []
source:
  - {file: upper.tex, lines: [17, 34]}
status: proposed
---

**확인 (작성자가 보탠 것).** 퇴화 경우: (2.3)에서 $e^{\theta}=a$ 이므로 $c=\log a=\theta(s)$ 이고 $\lvert c\rvert\le B(\theta)$ 라 적분 가능하다. $Z_N=e^{\sum_{k\le M_N}c_k}\prod_i2\cosh h_i$ 이므로 $F_N=\alpha\mathbb Ec+\log2+\mathbb E\log\cosh h$. 시행 쪽은 $U_{\theta_j}=c_j$, $C_\theta=e^c$ 이므로 $V_{\rm s}=\cosh h\,e^{\sum_{j\le k}c_j}$ 가 message에 의존하지 않아 $T_0V_{\rm s}=V_{\rm s}$, $\mathbb E\log T_0V_{\rm s}=\mathbb E\log\cosh h+\alpha p\,\mathbb Ec$, $\mathbb E\log T_0V_{\rm e}=\mathbb Ec$ 이고 $\mathcal B_r=\log2+\mathbb E\log\cosh h+\alpha p\mathbb Ec-\alpha(p-1)\mathbb Ec$ 가 같은 값이다.

비퇴화 경우의 논증: $\mathbb P(\lvert b\rvert>u^{-p})>0$ 이면 $b$ 와 독립인 $M_1,\ldots,M_p$ 를 모두 $M_\ell\ge u$ 로 제한한 사건(확률 $>0$)에서 $\lvert b\rvert\prod_\ell M_\ell>1$ 이 된다. $M$ 쪽도 $\lvert b\rvert\ge v$ 와 $M_\ell\ge u$ ($\ell\ne1$)로 제한한다. 곱 한계의 꼴 $\lvert b\rvert\prod_\ell M_\ell<1$ 은 [[model:factorization]] 본문 메모에 있다.

"degenerate"의 원문 조건은 "$b=0$ almost surely or $M=0$ almost surely"이다. model.tex 41–42의 "product term vanishes identically"([[x:model-hypothesis-remarks]] (ii))와 같은 경우를 가리키지만, 이 단계는 그 카드를 쓰지 않고 스스로 처리한다.
