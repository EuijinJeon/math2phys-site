---
id: upper:derivative.s1
kind: step
title: '세 삽입의 꼴 $a(1+D)$ 와 edge 증분 $\log T_0V_{\rm e}$'
uses: [model:factorization, model:site-message, model:edge, model:ve, x:model-message, tree:insertion, x:tree-extra-variables, model:power-means]
provides: 'upper:regularization ($D$, $D_*$), upper:remainder (각 삽입의 $D^a$ 꼴)'
math: |
  주장 (4.1)을 세운다(upper:derivative). (2.3) 아래 세 삽입은 모두 $a(1+D)$ 꼴이다. 실제 상호작용이면 $D=b\prod_\ell f_\ell(\sigma_{i_\ell})$, cavity 상호작용이면 $p-1$ 개 인자를
  $$\bar f(x)=\sum_sf(s)q_x(s)$$
  로 바꾸고, edge 삽입이면 $p$ 개 모두 바꾼다. 마지막 경우 독립 message 과정은 섭동되지 않은 tilted tree에 덧붙여지므로 그 증분은 $\log T_0V_{\rm e}$ 이다.
physics: |
  실제 factor는 $p$ 개 실제 spin에, [[g:site-term|cavity factor]]는 실제 spin 하나와 $p-1$ 개 독립 [[g:message|cavity field]]에, [[g:edge-term|edge 항]]은 $p$ 개 cavity field에만 붙는다. [[g:factorization|factor 전개]] 덕에 셋 모두 $a(1+b\prod(\text{spin 인자}))$ 꼴이고, cavity field 쪽 인자는 그 field 아래의 평균 $\bar f(x)$ 다.
gap: |
  같은 내용이다. edge 삽입은 spin에 의존하지 않으므로 그 증분은 보조 message 변수만의 [[g:power-mean|power mean]] $\log T_0V_{\rm e}$ 다.
abstraction: exact
children: []
source:
  - {file: upper.tex, lines: [58, 68]}
status: proposed
---

**확인 (작성자).** cavity 상호작용: (2.6)에 (2.3)을 넣으면 $e^{U_\theta(x;\varepsilon)}=\sum_se^{\theta(s,\varepsilon)}\prod_{\ell<p}q_{x_\ell}(s_\ell)=a\bigl(1+bf_p(\varepsilon)\prod_{\ell<p}\bar f_\ell(x_\ell)\bigr)$. edge: $C_\theta=a(1+b\prod_\ell\bar f_\ell(x_\ell))$. 세 경우 모두 $\sum_sq_x(s)=1$ 을 쓴다.

"appended to the unperturbed tilted tree"는 [[x:tree-extra-variables]]의 약속(새 변수의 독립 prior kernel로 path kernel을 넓힘)으로 읽었다. 새 message는 원래 backward logarithm에 들어 있지 않으므로 그 조건부 kernel은 prior 그대로이고, [[tree:insertion]]의 $Y$ recursion이 바로 (2.10)의 $T_d$ 가 되어 $\log Y_0=\log T_0V_{\rm e}$ 다. $a$ 는 새 상호작용의 disorder(새 root 변수)라서 recursion을 통과한다. 원문은 이 두 연결을 `\ref` 없이 쓴다.
