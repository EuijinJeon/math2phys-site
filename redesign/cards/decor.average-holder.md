---
id: decor:average-holder
kind: lemma
title: '깊이 평균의 분수 거듭제곱 부등식'
uses: [decor:average-definition]
provides: '분수 거듭제곱 (v^{1/4}, v^{1/2})을 평균 밖으로 꺼낼 때: decor:conditional-concentration.s7.s3 (fiber bound)'
math: |
  음이 아닌 $z$와 $0<\gamma\le1$에 대해 $\mathcal A_{L,\eta}(z^\gamma)\le(\mathcal A_{L,\eta}z)^\gamma$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [36, 43]}
status: proposed
---

$\mathcal A_{L,\eta}$는 질량 $M\le1$인 측도에 대한 적분이다. $t\mapsto t^\gamma$가 오목하므로 Jensen에서 $\mathcal A(z^\gamma)\le M^{1-\gamma}(\mathcal Az)^\gamma\le(\mathcal Az)^\gamma$. 합 범위가 다른 정칙성 조건(예: $\eta/2$)으로 바뀌어도 같은 논증이 성립한다.
