---
id: reduction:stability.s2
kind: step
title: '시행 functional 안정성 (reduction:trial-stability)'
uses: [model:site-message, model:edge, model:vs, model:ve, model:chain, model:power-means, model:functional, x:model-depth-zero, model:trial-bounds, model:integrability, x:reduction-power-mean-scaling]
provides: 'reduction:stability의 둘째 부등식'
math: |
  각 cavity 상호작용 $U_\theta$ 는 대응하는 상호작용 sup-norm 차이 이하로 바뀌고, 각 edge logarithm $\log C_\theta$ 도 그렇다. power mean은 이 root-가측 한계를 보존한다. site 항은 평균 $\alpha p$ 개의 상호작용을 갖고 edge 항의 계수는 $\alpha(p-1)$ 이므로 (reduction:trial-stability)가 나온다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: reduction.tex, lines: [33, 37]}
status: proposed
---

**풀이 (작성자).** 같은 $k$, 같은 message, 결합된 $(\theta_j,\theta_j')$, $(h,h')$ 로 $V_{\rm s}$, $V_{\rm s}'$ 를 만든다. (2.6)은 $e^{\theta(\cdot,\varepsilon)}$ 의 확률 가중 평균의 log이므로 $\lvert U_\theta-U_{\theta'}\rvert\le\max_s\lvert\theta(s)-\theta'(s)\rvert$; (2.5)의 $\log C_\theta$ 도 같다([[model:site-message]], [[model:edge]]). 그러면 (2.8)에서 $e^{-\delta}V_{\rm s}\le V_{\rm s}'\le e^\delta V_{\rm s}$, $\delta=\lvert h-h'\rvert+\sum_{j\le k}\max_s\lvert\theta_j-\theta_j'\rvert$ 이고, $\delta$ 는 물리 disorder만의 함수다. [[x:reduction-power-mean-scaling]]으로 $\lvert\log T_0V_{\rm s}-\log T_0V_{\rm s}'\rvert\le\delta$, 기대값은 $d+\alpha pD$ ($k\sim\mathrm{Pois}(\alpha p)$ 가 독립, Wald). edge 항은 $\lvert\log T_0V_{\rm e}-\log T_0V_{\rm e}'\rvert\le\max_s\lvert\theta-\theta'\rvert$, 계수 $\alpha(p-1)$ 을 곱해 $\alpha(p-1)D$. 합 $\alpha(2p-1)D+d$. 시행 법칙 $(\zeta,\mathbf m)$ 과 $r$ 이 경계에 들어가지 않으므로 균일하고, $r=0$ 에서는 $T$ 없이 같은 계산이다([[x:model-depth-zero]]). 두 functional이 유한하다는 것은 (2.12)와 (2.1)에서 온다([[model:trial-bounds]]).

원문은 이 계산을 네 문장으로 적는다. 위 풀이에서 결합의 구체적 방식(같은 $k$ 와 message)은 작성자가 보탠 것이다.
