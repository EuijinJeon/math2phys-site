---
id: model:trial-bounds
kind: remark
title: 'moment 조건 없는 유한성 (2.12)'
uses: [model:functional, x:model-depth-zero, model:power-means, x:model-cavity-bounds, model:integrability]
provides: 'comp:bounded-lower(comparison.tex 235: $A=\inf_r\Phi_r$ 가 유한), upper:bound.s2("including unbounded messages", upper.tex 7–8: $\varphi(0)$ 의 $\mathbb E\log T_0V_{\rm s}$ 와 $\varphi(t)$ 의 유한성, `\ref` 없음), reduction:stability(power mean이 root-가측 한계를 보존)'
math: |
  (2.11)의 양들은 시행 message에 대한 moment 가정 없이 유한하다. power-mean 연산자가 점별 곱셈적 한계를 보존하고
  $$\lvert\log T_0V_{\rm s}\rvert\le\lvert h\rvert+\sum_{j=1}^kB(\theta_j),\qquad\lvert\log T_0V_{\rm e}\rvert\le B(\theta)\tag{2.12}$$
  이기 때문이다.
physics: |
  시행 [[g:order-parameter|order parameter]]가 아무리 큰 cavity field를 실어도 site 항과 edge 항은 [[g:interaction|상호작용]]과 [[g:field|장]]의 크기만큼만 움직인다. 그래서 RSB free entropy([[g:functional]])는 어떤 시행 법칙에서도 유한하다.
gap: |
  (2.12)는 점별 부등식이고, $\mathcal B_r$ 의 유한성은 그 기대값 $\mathbb E\lvert h\rvert+\alpha p\,\mathbb EB(\theta)$, $\mathbb EB(\theta)$ 가 (2.1)로 유한하다는 데서 나온다. 이 기대값 계산은 원문에 적혀 있지 않다(작성자가 보탬). 물리 문장은 이것을 "유한하다"로 줄였다.
abstraction: weakening
children: []
source:
  - {file: model.tex, lines: [122, 128]}
status: proposed
---

**확인 (작성자가 보탠 것).** $V_{\rm s}$ 는 $\varepsilon=\pm1$ 에 대한 평균이고 지수 안이 $\lvert h\rvert+\sum_jB(\theta_j)$ 로 눌리므로($\lvert U_{\theta_j}\rvert\le B(\theta_j)$, [[x:model-cavity-bounds]]) $e^{-c}\le V_{\rm s}\le e^{c}$, $c=\lvert h\rvert+\sum_{j\le k}B(\theta_j)$ 이다. $c$ 는 물리적 disorder만의 함수라서 모든 $\mathscr F_d$ 에 대해 가측이고, $e^{-c}\le T_{d+1}V\le e^c$ 이면 $T_dV$ 도 같은 범위에 있다. 깊이 $r$ 부터 귀납하면 $T_0V_{\rm s}\in[e^{-c},e^c]$. $V_{\rm e}=C_\theta$ 도 같다. $r=0$ 에서는 $T_0$ 이 없고 같은 한계가 $V$ 에 바로 성립한다. Wald 등식으로 $\mathbb E\sum_{j\le k}B(\theta_j)=\alpha p\,\mathbb EB(\theta)$.
