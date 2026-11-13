---
id: model:vs
kind: definition
title: 'site 분배함수 $V_{\rm s}$ (2.8)'
uses: [model:site-message, model:chain]
provides: 'model:functional의 $\mathbb E\log T_0V_{\rm s}$. comparison.tex 180($\widetilde Y_{0,\rm s}=T_0V_{\rm s}$), upper.tex 47–48(interpolation 끝점 $\varphi(0)$)'
math: |
  서로 독립인 $k\sim\mathrm{Pois}(\alpha p)$, $\theta,\theta_1,\ldots$ ($\theta$ 의 사본), $h$ 를 잡고
  $$V_{\rm s}=\frac12\sum_{\varepsilon=\pm1}\exp\Bigl(h\varepsilon+\sum_{j=1}^kU_{\theta_j}(x_1^j,\ldots,x_{p-1}^j;\varepsilon)\Bigr).\tag{2.8}$$
  message $x^j_\ell$ 는 서로 다른 label이다(model:chain).
physics: |
  새 spin $\varepsilon$ 하나를 [[g:field|장]] $h$ 와 Poisson$(\alpha p)$ 개 factor와 함께 넣는 site 분배함수를 $2$ 로 나눈 정규화량([[g:site-term]])이다. 각 factor의 다른 $p-1$ 개 spin은 독립인 cavity field를 따른다. 평균 차수 $\alpha p$ 는 [[g:hypergraph|hypergraph]]의 spin 하나의 평균 차수다.
gap: |
  정의는 같은 내용이다. 앞의 $\frac12$ 과 functional의 $\log2$ 가 합쳐 $\log\sum_\varepsilon$ 이 된다. 물리의 Bethe 공식과 달리 이 값은 power mean $T_0$ 을 거친 뒤에야 functional에 들어간다(model:power-means).
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [82, 87]}
status: proposed
---
