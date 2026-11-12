---
id: comp:patterns.s2
kind: step
title: '곱측도의 telescoping과 총변동 경계'
uses: [comp:patterns.s1]
provides: 'comp:patterns의 결론 (comp:pattern-error)'
math: |
  독립 균일 복원추출은 reservoir 안에서 조건부로 $\pi^{\otimes a}$ 를 주고, trial 분포는 $\bar\pi^{\otimes a}$ 다. 곱측도의 초등적 telescoping 경계가
  $$\lVert\pi^{\otimes a}-\bar\pi^{\otimes a}\rVert_{\rm TV}\le a\lVert\pi-\bar\pi\rVert_{\rm TV}\le\frac a2\sum_{\varnothing\ne S\subseteq[k]}\lvert R_S-\mathbb ER_S\rvert$$
  를 준다. 1 이하로 유계인 함수를 적분하는 비용은 총변동의 두 배 이하다. 독립인 insertion disorder를 조건으로 걸면 마지막 주장이 증명된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [111, 121]}
status: proposed
---

둘째 부등식(작성자 확인): $\lVert\pi-\bar\pi\rVert_{\rm TV}=\frac12\sum_{\boldsymbol e}\lvert\pi(\boldsymbol e)-\bar\pi(\boldsymbol e)\rvert\le\frac12\sum_{\boldsymbol e}2^{-k}\sum_{S\ne\varnothing}\lvert R_S-\mathbb ER_S\rvert=\frac12\sum_{S\ne\varnothing}\lvert R_S-\mathbb ER_S\rvert$ ($S=\varnothing$ 항은 상쇄). 그러면 기대값의 차는 $\mathbb E[2\lVert\pi^{\otimes a}-\bar\pi^{\otimes a}\rVert_{\rm TV}]\le a\sum_{S\ne\varnothing}\mathbb E\lvert R_S-\mathbb ER_S\rvert$ 이다. 총변동은 $\frac12\ell^1$ 로 정규화했다고 읽었다(원문은 정규화를 적지 않지만 "twice total variation"과 $\frac a2$ 가 이 정규화와 맞는다).
