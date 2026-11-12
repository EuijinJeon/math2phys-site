---
id: models:sat.s1
kind: step
title: '위반 지시함수로 factor weight 쓰기'
uses: []
provides: 'models:sat.s2 ($e^{\theta_\beta}=1+(e^{-\beta W}-1)I_\varepsilon$)'
math: |
  곱 $I_\varepsilon(s)=\prod_\ell(1+\varepsilon_\ell s_\ell)/2$ 는 $\{0,1\}$ 에 값을 갖고 위반된 clause를 가리킨다. 그러므로
  $$e^{\theta_\beta(s)}=1+(e^{-\beta W}-1)I_\varepsilon(s).$$
physics: |
  clause가 만족되면 weight 1, 위반되면 $e^{-\beta W}$ 이다. 이 두 값을 지시함수 하나로 쓴 것이다.
gap: |
  정확하다. $\theta_\beta=-\beta WI_\varepsilon$ 이고 $I_\varepsilon\in\{0,1\}$ 이라 $e^{-\beta WI_\varepsilon}=1+(e^{-\beta W}-1)I_\varepsilon$ 이다(작성자 확인).
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [51, 58]}
status: proposed
---
