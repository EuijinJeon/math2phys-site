---
id: model:integrability
kind: assumption
title: '매개변수 $p$, $\alpha$, 법칙 $\theta$, $h$ 와 1차 moment 가정 (2.1)'
uses: []
provides: '모형의 입력. model:hamiltonian, model:edge, model:site-message의 $\theta$, $B(\theta)$. reduction:stability의 가정(reduction.tex 11). main:theorem의 가정 (2.1)'
math: |
  짝수 정수 $p\ge2$ 와 $\alpha>0$ 을 고정한다. $\theta$ 는 $\{-1,1\}^p$ 위의 무작위 실함수, $h$ 는 실수 확률변수이다. $B(\theta)=\max_s\lvert\theta(s)\rvert$ 로 쓰고
  $$\mathbb E B(\theta)+\mathbb E\lvert h\rvert<\infty\tag{2.1}$$
  를 가정한다.
physics: |
  [[g:interaction|상호작용]] $\theta$ 는 $p$체 factor 하나의 log-weight(역온도 포함), [[g:field|장]] $h$ 는 site별 무작위 외부장(역온도 포함)이다. 둘 다 1차 moment만 유한하면 된다.
gap: |
  물리 유도는 보통 bounded coupling이나 특정 분포를 놓는다. 여기서는 (2.1)만 요구하고, 하한은 먼저 $B(\theta)\le B$, $\lvert h\rvert\le H$ 인 경우(cavity.tex 11–12)에 증명한 뒤 [[g:truncation|truncation]]으로 넘어온다(main:theorem.s2). $p$ 가 짝수라는 것은 상한의 볼록성에 쓰이며(upper.tex 124) 홀수 $p$ 는 다루지 않는다.
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [3, 8]}
status: proposed
---

$B(\theta)$ 는 뒤에서 $\lvert\log C_\theta\rvert$, $\lvert U_\theta\rvert$ 의 상계([[x:model-cavity-bounds]]), $T_0V$ 의 상계([[model:trial-bounds]]), 상수 $c=\theta(1,\ldots,1)$ 의 적분 가능성([[main:theorem.s1]])에 쓰인다.
