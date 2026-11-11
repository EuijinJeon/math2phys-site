---
id: main:theorem.s2
kind: step
title: 'truncation과 bounded 하한의 적용'
uses: [main:theorem.s1, comp:bounded-lower, model:integrability]
provides: 'main:theorem.s3($D_K,d_K\to0$ 과 잘린 모형의 하한)'
math: |
  $K>0$ 에 대해 $\widehat\theta$ 의 각 값과 $h$ 를 $[-K,K]$ 로 잘라 $\widehat\theta^{(K)}$, $h^{(K)}$ 를 얻는다. 순열 불변성은 보존된다. bounded 법칙의 하한 comp:bounded-lower는 truncation이 factorization을 보존하든 말든 적용된다. dominated convergence로
  $$D_K=\mathbb E\max_s\lvert\widehat\theta(s)-\widehat\theta^{(K)}(s)\rvert\longrightarrow0,\qquad d_K=\mathbb E\lvert h-h^{(K)}\rvert\longrightarrow0.$$
physics: |
  큰 coupling과 장을 잘라 bounded 모형으로 바꾼다([[g:truncation]]). 잘린 모형은 여전히 입력에 대해 대칭이므로([[g:permutation-invariance]]) bounded 하한이 적용된다.
gap: |
  하한(comp:bounded-lower)이 factorization과 positivity를 쓰지 않으므로 잘린 상호작용이 (2.3), (2.4)를 만족하는지 따질 필요가 없다. dominated convergence의 지배 함수는 $B(\widehat\theta)$ 와 $\lvert h\rvert$ 이고 main:theorem.s1과 (2.1)로 적분 가능하다(원문은 지배 함수를 적지 않는다).
abstraction: exact
children: []
source:
  - {file: reduction.tex, lines: [60, 69]}
status: proposed
---
