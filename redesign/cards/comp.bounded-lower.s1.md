---
id: comp:bounded-lower.s1
kind: step
title: '고정 $L$ 의 부등식 $A\le\underline F+2\varepsilon+\limsup_N\lvert\Delta_N-\mathcal B_{L-1}\rvert$'
uses: [model:trial-bounds, model:functional, x:model-depth-zero, model:chain, cavity:grid, comp:encoding, comp:low-increments, x:comp-standing, x:cavity-bounded]
provides: 'comp:bounded-lower.s2'
math: |
  $A=\inf_{r\ge0}\Phi_r$ 로 쓴다. (2.12)에 의해 유한하다. 부호화된 각 시행값은 $A$ 이상이므로, (8.1)이 모든 고정 $L$ 에서
  $$A\le\underline F+2\varepsilon+\limsup_{N\to\infty}\Bigl\lvert\Delta_N^{L,\mathbf u_{L,N}}-\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\Bigr\rvert$$
  를 준다. 안쪽 극한은 그 깊이의 선택된 수열을 쓴다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [233, 242]}
status: proposed
---

**풀이 (작성자).** $\zeta_{L,N}\in\mathcal M_L$ ([[comp:encoding]])이고 $\mathbf m^{(L)}$ 은 엄격히 증가하며 $(0,1)$ 안에 있으므로 $\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\ge\Phi_{L-1}\ge A$. 선택된 수열 위의 각 $N$ 에서
$$A\le\mathcal B_{L-1}\le\Delta_N+\lvert\Delta_N-\mathcal B_{L-1}\rvert\le\underline F+2\varepsilon+\lvert\Delta_N-\mathcal B_{L-1}\rvert$$
((8.1)), 그리고 그 수열을 따라 $\limsup_N$. $A$ 가 유한하다는 것: (2.12)의 점별 한계와 bounded 가정으로 모든 $\mathcal B_r$ 이 $\log2\pm(H+\alpha pB+\alpha(p-1)B)$ 안에 있다(작성자 계산, 원문은 "finite by (2.12)"만 적는다). 위에서 유한한 것만 필요하다면 $\Phi_r$ 하나가 유한하면 되고, 아래에서 유한해야 $A=-\infty$ 라는 공허한 경우가 빠진다. $\underline F$ 도 bounded 모형에서 유한하다($\lvert F_N\rvert\le\log2+\alpha B+H$, 작성자).
