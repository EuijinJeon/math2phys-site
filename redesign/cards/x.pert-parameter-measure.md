---
id: x:pert-parameter-measure
kind: definition
title: '매개변수 측도 $\pi$ (결정적 벡터를 고르는 데만 씀)'
uses: [pert:parameters, x:cavity-root-convention]
provides: 'pert:concentration (π에 대한 적분), pert:selection.s1–s2 (π-평균 증분과 Markov 선택), x:pert-order-of-choices'
math: |
  $\pi$ 를 구간 $I_\nu$ 위 균일 확률측도들의 곱이라 하고 $\mathbf u=(u_\nu)_\nu$ 로 쓴다. $\pi$ 는 결정적 매개변수 벡터를 고르는 데 쓰며 그 quenched 법칙의 일부가 아니다. 고정된 type마다 각 구간의 길이는 고정된 양수이므로 집중 추정은 그 길이에 의존해도 된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [67, 71]}
status: proposed
---

이 카드가 원칙 "매개변수 평균과 root 기대값을 섞지 않는다"의 원문 근거다. 이 절에서 $\pi$ 에 대한 적분이 나오는 곳은 [[pert:concentration]]의 진술과 증명(구간 $I_\nu$ 위의 $du$ 적분, 그리고 나머지 곱측도에 대한 적분, perturbations.tex 99, 150, 227, 240–243)과 [[pert:selection.s1]]–[[pert:selection.s2]](perturbations.tex 273, 276, 287–297)뿐이다. 그 밖의 모든 $\mathbb E$, $\mathbb E_{\mathbf u}$, $\langle\cdot\rangle$ 은 $\mathbf u$ 를 고정한 [[g:root]]·path 기대값이다([[x:pert-standing]]). pert:selection이 한 점 $\mathbf u_j$ 를 고른 뒤로는 $\pi$ 가 다시 나오지 않는다.
