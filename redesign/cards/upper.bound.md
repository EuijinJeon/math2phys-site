---
id: upper:bound
kind: proposition
title: 'interpolation 상한 $F_N\le\mathcal B_r(\zeta,\mathbf m)$'
uses: [x:model-hypotheses, model:hamiltonian, model:chain, x:model-depth-zero, model:functional, model:factorization, model:positivity, tree:log-expansion, tree:insertion]
provides: 'main:theorem.s4 (reduction.tex 85: $\limsup_NF_N\le\inf_r\Phi_r$). x:model-moment-finiteness (model.tex 39–41의 예고: 비퇴화 경우 $b$, $\max_s\lvert f_1(s)\rvert$ 의 본질적 유계성은 이 증명의 첫 단락 upper:bound.s1에 있다). 규칙 P2, L1 수 1'
math: |
  main:theorem의 가정(x:model-hypotheses) 아래, 모든 $N$ 과 모든 admissible 유한 단계 시행 법칙에 대해
  $$F_N\le\mathcal B_r(\zeta,\mathbf m).$$
  따라서 $F_N\le\inf_{r\ge0}\Phi_r$.
  (작성자 읽기: "admissible"은 원문에 정의가 없다. $r\ge1$ 이면 $\zeta\in\mathcal M_{r+1}$, $0<m_1<\cdots<m_r<1$ (model:chain), $r=0$ 이면 $\zeta\in\mathcal P(\mathbb R)$ (x:model-depth-zero)로 읽었다. 이것이 $\Phi_r$ 의 inf 범위와 같다. 근거: model.tex 70–71, 118–120이 시행 법칙을 그렇게만 정의한다; upper.tex 14 "Consequently $F_N\le\inf_{r\ge0}\Phi_r$"가 따르려면 inf 범위 전체가 admissible이어야 한다; upper.tex 7–9 "the full trial class, including unbounded messages"; overview.tex 39–40과 reduction.tex 19 "all trial laws, including $r=0$". 검토자 동의.)
physics: |
  [[x:model-hypotheses]]의 [[g:hypotheses|가정]] 아래에서, 임의의 $r\ge0$ 단 시행 [[g:order-parameter|order parameter]] $\zeta$ 와 [[g:parisi-parameters|Parisi parameter]] $\mathbf m$ 으로 계산한 Mézard–Parisi Bethe free entropy $\mathcal B_r$([[g:functional]])는 모든 크기 $N$ 에서 quenched [[g:pressure|pressure]] $F_N$ 의 상한이다(free energy로는 하한). 그래서 모든 시행값의 inf([[g:phi]])도 상한이다.
gap: |
  진술은 같은 내용이다. 물리 관습과 다른 점: (1) 정류점(saddle point)에서 평가한 값 하나가 아니라 모든 시행값이 상한이고, 그 inf가 쓰인다. (2) 극한이 아니라 모든 유한 $N$ 에서 성립한다. (3) 시행 message에 moment 조건이 없다(upper.tex 7–8 "including unbounded messages"). (4) 가정은 짝수 $p$ 와 [[g:positivity|부호 조건]]을 포함하고 둘 다 실제로 쓰인다(upper:remainder). 홀수 $p$ 는 다루지 않는다.
abstraction: exact
children: [upper:bound.s1, upper:bound.s2, upper:bound.s3, upper:derivative, upper:bound.s4]
source:
  - {file: upper.tex, lines: [11, 15]}
  - {file: upper.tex, lines: [17, 128]}
status: proposed
---

**증명의 뼈대.** [[upper:bound.s1]]: 곱 항이 없는 퇴화 경우는 직접 같고, 아니면 $b$ 와 $M=\max_s\lvert f(s)\rvert$ 가 본질적으로 유계라 이후의 모든 moment가 유한하다. [[upper:bound.s2]]: 실제 상호작용(평균 $t\alpha N$)과 site별 cavity 상호작용(평균 $(1-t)\alpha p$)을 잇는 [[g:interpolation|interpolation]] $\varphi(t)$ 를 세우고 $\varphi(1)=F_N$, $\varphi(0)=\log2+\mathbb E\log T_0V_{\rm s}$ 를 얻는다. [[upper:bound.s3]]: Poisson 미분으로 $\varphi'(t)/\alpha$ 를 실제 상호작용 하나의 삽입 증분에서 균일 site의 cavity 상호작용 증분 $p$ 배를 뺀 것으로 쓴다. [[upper:derivative]]: 핵심 부등식 $\varphi'(t)+\alpha(p-1)\mathbb E\log T_0V_{\rm e}\le0$. [[upper:bound.s4]]: $t\in[0,1]$ 에서 적분.

**순환을 피하는 연결.** 진술은 원문에서 `\cref{main:theorem}`을 가리키지만 실제로 받는 것은 가정뿐이므로 `uses`에는 [[x:model-hypotheses]]를 넣었다(그 카드의 원문 범위가 model.tex 130–131을 담는다). [[main:theorem]]은 증명에서 이 카드를 쓴다(reduction.tex 85, [[main:theorem.s4]]). model.tex 39–41의 예고("as shown in upper:bound")는 [[x:model-moment-finiteness]]가 이 카드를 `uses`에 넣는 방향으로 연결되고, 이 카드와 자손은 그 주석 카드를 쓰지 않는다. 퇴화 경우와 $\log a$ 에 관한 사실은 증명이 스스로 다시 적으므로([[upper:bound.s1]], [[upper:regularization]]) [[x:model-hypothesis-remarks]]도 `uses`에 넣지 않았다.

`uses`의 tree 노드: 원문이 `\cref`로 가리키는 것은 [[tree:log-expansion]]뿐이다(upper.tex 81, 97, 121). recursion의 단조성·동차성("the recursion preserves multiplicative bounds", 54; $a$ 를 먼저 떼는 것, 71)은 [[tree:insertion]]의 마지막 문단에서 온다고 읽었다(작성자 읽기, `\ref` 없음).
