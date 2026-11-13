---
id: comp:insertion-comparison.s1.s3
kind: step
title: 'bond 쪽의 인수분해와 trial 증분 $=\mathcal B_{L-1}$'
uses: [comp:insertion-comparison.s1.s1, comp:insertion-comparison.s1.s2, model:ve, model:edge, model:power-means, model:functional, model:chain, cavity:increment]
provides: 'comp:insertion-comparison.s4 (trial 항등식), comp:insertion-comparison의 결론'
math: |
  $\widetilde A_{\rm b}$ 에서는 같은 전이가 서로 겹치지 않는 message label을 가진 $K_{\rm b}$ 개 edge 인자의 곱을 준다. 한 깊이에서 물리 disorder와 모든 message prefix가 주어지면 이 label 묶음들은 독립으로 남는다. 그러므로 그 곱은 각 조건부 power mean을 마지막 단계부터 첫 단계까지 차례로 통과해 인수분해된다. 따라서
  $$\mathbb E\log\widetilde Y_{0,\rm b}=\alpha(p-1)\mathbb E\log T_0V_{\rm e},\qquad\log2+\mathbb E\log\widetilde Y_{0,\rm s}-\mathbb E\log\widetilde Y_{0,\rm b}=\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)}).$$
  (5.5)에 의해 남은 일은 reservoir와 trial의 삽입 logarithm을 주어진 극한에서 비교하는 것이다.
physics: |
  서로 다른 factor의 이웃 cavity field들이 독립 사본이므로 bond 삽입의 계층 free entropy는 factor마다 [[g:edge-term|edge 항]] $\log T_0V_{\rm e}$ 의 합이 되고, 평균 factor 수가 $\alpha(p-1)$ 이다. [[g:power-mean|power mean]]이 독립 인자의 곱을 곱으로 보내기 때문이다.
gap: |
  물리 문장은 다음 내용을 생략한 약화다: bond 항의 인수분해는 말하지만 site 항과 합친 시행 functional 전체의 등식은 재진술하지 않는다.
  정확하다. 인수분해에는 "같은 prefix 아래 label 묶음들이 조건부 독립"이라는 구성상의 독립이 필요하다. reservoir 쪽에서는 이것이 성립하지 않으며(같은 배치를 공유), 그 차이는 s2–s4가 다룬다.
abstraction: weakening
children: []
source:
  - {file: comparison.tex, lines: [181, 196]}
status: proposed
---

**인수분해의 한 걸음 (작성자가 풀어 씀).** 깊이 $d$ 에서 $\widetilde Y_d=\prod_{j\le K_{\rm b}}Y_d^{(j)}$ 이고 $Y_d^{(j)}$ 가 $\mathscr F_{d-1}$ 이 주어지면 조건부 독립이라 하자. 그러면 $\mathbb E[\prod_j(Y_d^{(j)})^{m_d}\mid\mathscr F_{d-1}]=\prod_j\mathbb E[(Y_d^{(j)})^{m_d}\mid\mathscr F_{d-1}]$ 이고 $1/m_d$ 거듭제곱이 곱을 보존한다. 깊이 $L$ 에서 $Y_{L-1}^{(j)}=C_{\theta_j}(x^{j}_1,\ldots,x^{j}_p)$ ([[model:edge]]) 이므로 귀납으로 $\widetilde Y_{0,\rm b}=\prod_{j\le K_{\rm b}}T_0C_{\theta_j}$. $K_{\rm b}\sim\mathrm{Pois}(\alpha(p-1))$ 가 나머지와 독립이고 각 인자가 (2.9)의 $V_{\rm e}$ 와 같은 법칙이므로 $\mathbb E\log\widetilde Y_{0,\rm b}=\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ (Wald; 적분 가능성은 $\lvert\log T_0C_\theta\rvert\le B(\theta)$). 둘째 식은 s1.s2와 이것을 (2.11)에 $r=L-1$, $\zeta=\zeta_{L,N}$, $\mathbf m=\mathbf m^{(L)}$ 로 넣은 것이다. $\mathbf m^{(L)}$ 은 $0<1/L<\cdots<(L-1)/L<1$ 이고 $\zeta_{L,N}\in\mathcal M_L=\mathcal M_{r+1}$ 이므로 [[model:functional]]의 정의역 안에 있다.

power mean이 조건부 독립인 인자의 곱을 인수분해한다는 성질은 §2에 진술되어 있지 않고 이 행(184–185)에서 처음 쓰인다. [[model:power-means]]의 provides 칸도 이 사용을 적는다.
