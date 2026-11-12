---
id: comp:encoding.s2
kind: step
title: '거꾸로 쌓은 측도 $\eta_d$ 와 $\zeta_{L,N}=\operatorname{Law}(\eta_0)\in\mathcal M_L$'
uses: [comp:encoding.s1, model:chain, x:pert-mark-specification, pert:factor]
provides: 'comp:encoding.s3 ($\eta_d$ 와 그 가측성), comp:encoding.s4 ($\zeta_{L,N}$)'
math: |
  무작위 측도를 거꾸로
  $$\eta_{r-1}=\operatorname{Law}(x\mid\mathscr G_{r-1}),\qquad\eta_d=\operatorname{Law}(\eta_{d+1}\mid\mathscr G_d)\quad(0\le d<r-1)$$
  로 정의한다. 그러면 $\eta_d\in\mathcal M_{r-d}$ 이므로 $\zeta_{L,N}=\operatorname{Law}(\eta_0)\in\mathcal M_L$ 이다. 모든 상태 공간이 standard Borel이므로 이 조건부 확률 kernel들은 가측 판을 갖는다. 여기서 쓰는 보조 prior는 실현된 각 root에서 유한 mark 공간의 유한곱으로 잡을 수 있다. 따라서 같은 주장은 root 개수를 조건으로 건 유한합으로도 바로 나온다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [44, 57]}
status: proposed
---

$\mathcal M_1=\mathcal P(\mathbb R)$, $\mathcal M_{j+1}=\mathcal P(\mathcal M_j)$ 는 [[model:chain]]의 것이다. $x$ 는 실수이므로 $\eta_{r-1}\in\mathcal M_1$, 귀납으로 $\eta_d\in\mathcal M_{r-d}$, $\eta_0\in\mathcal M_r$, 그 법칙은 $\mathcal M_{r+1}=\mathcal M_L$ 에 있다. $r=1$($L=2$)이면 둘째 정의는 쓰이지 않고 $\eta_0=\operatorname{Law}(x\mid\mathscr G_0)$ 이다(작성자 확인).

"finite products of finite mark spaces at each realized root"는 [[x:pert-mark-specification]](좌표 수 유한, 값 $\pm1$)과 [[pert:factor]](섭동 항이 거의 확실히 유한 개, 개수·type·site는 root)에서 `\ref` 없이 온다. 이것이 맞으면 깊이 $1,\ldots,r$ 의 보조 변수가 실현된 root마다 유한 집합에 값을 가지므로 조건부 법칙이 유한합으로 정해진다(작성자 읽기; standard Borel 논법과 이 유한합 논법은 원문에서 둘 다 제시되며, 어느 하나로 충분하다).
