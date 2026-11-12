---
id: pert:concentration.s3.s2
kind: step
title: '개수에 조건을 건 Efron–Stein 부등식'
uses: [pert:concentration.s3.s1, pert:factor]
provides: 'pert:concentration.s3.s3'
math: |
  첫 추정을 증명하려고 물리적 개수와 섭동 총 개수에 조건을 건다. 섭동 총 개수가 주어지면 그 type과 site는 독립 label이고, label 하나를 바꾸면 유계 인자 하나가 바뀐다. Efron–Stein 분산 부등식
  $$\operatorname{Var}Z\le\frac12\sum_j\mathbb E(Z-Z^{(j)})^2$$
  을 쓴다. $Z^{(j)}$ 는 $j$ 번째 입력을 독립으로 다시 뽑아 얻는다. 완전성을 위해: 독립 입력 $X_1,\ldots,X_k$ 에 대해 $E_j$ 는 $X_j$ 만 적분하고 $\mathscr G_j=\sigma(X_1,\ldots,X_j)$ 라 하자. Doob 차분은 $D_j=\mathbb E[Z-E_jZ\mid\mathscr G_j]$ 이다. 직교성과 Jensen이
  $$\operatorname{Var}Z=\sum_j\mathbb ED_j^2\le\sum_j\mathbb E(Z-E_jZ)^2=\frac12\sum_j\mathbb E(Z-Z^{(j)})^2$$
  을 준다. 이 독립 입력 분해는 같은 법칙도 대칭 통계량도 요구하지 않는다(Efron–Stein, Section 2).
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [176, 191]}
status: proposed
---

이 카드의 $D_j$ 는 Doob 차분이고 score $D_\nu$ 와 무관하다(원문의 기호 겹침). 조건을 거는 이유(작성자 읽기): Poisson 개수 자체는 "입력 하나"로 다루기 어렵다. 개수를 고정하면 각 항의 label(type, site; 물리 상호작용이면 그 함수와 index, 장)이 독립 입력이 되어 Efron–Stein이 바로 적용된다. type과 site가 총 개수가 주어졌을 때 독립 label이라는 것은 독립 Poisson 족을 합친 과정의 성질이다([[pert:factor]]의 type별 독립 Poisson 개수와 $\sum c_\nu=1$). 개수의 요동은 [[pert:concentration.s3.s3]]에서 따로 다룬다. 원문 인용 `EfronStein`은 외부 문헌이다.
