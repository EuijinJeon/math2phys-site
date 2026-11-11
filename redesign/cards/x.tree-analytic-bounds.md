---
id: x:tree-analytic-bounds
kind: lemma
title: '해석적 경계 (복소 영역에서의 $Y_d$)'
uses: [tree:Y-recursion, tree:insertion]
provides: 'tree:log-expansion.s2 (해석성으로 급수 확정), tree:extension-expansion (좌변의 해석적 경계). §6 pert:analytic (perturbations.tex 391–394: 복소 근방 |t|,|u|<ρ 위의 해석성과 N에 균등한 유계)'
math: |
  위의 식들은 복소 영역
  $$\sum_j|t_j|\|D_j\|_\infty<1$$
  위에서 해석적이며, 경계는 kernel에 대해 균등하다. 이 합이 $\rho<1$ 이하인 더 작은 닫힌 영역에서 $A$의 argument는 $\vartheta=\arcsin\rho<\pi/2$ 이하이고 modulus는 $1-\rho$와 $1+\rho$ 사이다. $Y_d$의 argument가 $[-\vartheta,\vartheta]$에 있으면 principal power를 써서 $K_dY_d^{m_d}$의 argument는 $[-m_d\vartheta,m_d\vartheta]$에 있다. 그것은 0이 아니고, $1/m_d$ 거듭제곱을 취하면 $Y_{d-1}$에 같은 argument 경계가 나온다. 정량적으로, modulus 하계 $a_d>0$은 하계
  $$a_{d-1}=a_d\cos(m_d\vartheta)^{1/m_d}>0$$
  을 주고, modulus 상계 $1+\rho$는 보존된다. 이 경계들이 각 단계의 해석함수 적분과 이후의 모든 미분을 정당화한다. 또 (tree:density), 아래의 상쇄된 판들, 그리고 더 작은 영역에서 그 도함수들을 깊이, 지수, tree 크기, 삽입 함수의 경계를 고정하면 kernel에 대해 균등하게 누른다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [156, 176]}
status: proposed
---

argument 경계: $|A-1|\le\rho$이면 $|\arg A|\le\arcsin\rho$. 부채꼴 $\{|\arg z|\le m_d\vartheta\}$는 $m_d\vartheta<\pi/2$이므로 볼록이고, kernel 적분은 볼록 결합이라 그 안에 머문다. modulus 하계는 $\operatorname{Re}K_dY_d^{m_d}\ge K_d|Y_d|^{m_d}\cos(m_d\vartheta)\ge a_d^{m_d}\cos(m_d\vartheta)$에서 온다(작성자 풀이). 시작은 $a_L=1-\rho$.

"이후의 모든 미분"과 "더 작은 영역에서 도함수의 균등 경계"는 Cauchy 추정으로 읽었다(원문은 방법을 명시하지 않는다). 하계가 깊이마다 $\cos(m_d\vartheta)^{1/m_d}$배씩 줄므로 균등성은 고정된 깊이 $L$과 지수에서의 것이다. $W_{\mathcal T}$의 음의 지수 $\gamma_\beta$ 때문에 modulus 하계가 필요하다.
