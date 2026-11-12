---
id: x:pert-mark-specification
kind: definition
title: 'mark specification (깊이별 Rademacher 좌표와 그 함수 $g$, $g_0$, $S_0$)'
uses: [x:tree-path-kernels, x:tree-sampling, x:pert-standing]
provides: 'pert:parameters(type의 첨자), pert:factor(각 항의 mark 과정), pert:palm-expression, x:pert-colored-extensions, pert:tree-identity.s1–s3(polarization 인자와 selector가 이 모임 안에 있음). \ref 없이 §8 comparison.tex 53–56 (보조 prior를 유한 mark 공간의 유한곱으로 잡을 수 있음)'
math: |
  mark specification은 다음으로 이루어진다: 유한 개 $n\ge0$ 의 이름 붙은 Rademacher 좌표, 각 좌표에 배정된 $\{1,\ldots,L-1\}$ 의 깊이, 두 함수
  $$g,g_0:\{-1,1\}^n\to\mathbb Q\cap[-1,1],$$
  그리고 $S_0=1$ 또는 $S_0=\sigma_i$ 의 선택. 각 좌표는 보조 path를 따라 배정된 깊이에서 뽑힌다. 서로 다른 좌표는 독립이다. 한 좌표의 값은 공유된 vertex에서는 공유되고 서로 다른 vertex에서는 독립이다. $n=0$ 은 상수 함수를 포함한다. 이런 specification을 모두 쓴다. 각 부호 정의역이 유한하므로 이것은 가산 모임이다. 부호의 곱과 그 유리수 평균이 이 모임에 든다. 이것들이 branching pattern을 고른다.
physics: |
  [[g:hierarchy|보조 계층]]의 지정된 깊이마다 놓인 무작위 부호([[g:mark|mark]])와, 그 부호들의 유리수값 함수를 site 하나의 spin(또는 상수 1)에 붙인 탐침이다. 두 [[g:replica|replica]] path가 그 깊이의 vertex를 공유하면 같은 부호를 보고, 아니면 독립인 부호를 본다.
gap: |
  물리적 국소장이 아니다. 부호는 보조 계층의 변수이고 [[g:root]] 변수가 아니다(pert:factor). 함수값을 유리수로 제한한 것은 모임을 가산으로 만들어 pert:selection의 대각 논법과 type 번호 매기기를 가능하게 하려는 것이다. "branching pattern을 고른다"는 것은 pert:tree-identity.s2–s3의 selector 구성으로만 실현된다.
abstraction: intuition
children: []
source:
  - {file: perturbations.tex, lines: [28, 38]}
status: proposed
---

"Each coordinate is sampled at its assigned depth along an auxiliary path"는 path마다 그 깊이의 vertex에 좌표값이 하나씩 붙는다는 뜻으로 읽었다. 그래서 같은 vertex를 지나는 path들은 값을 공유한다([[x:tree-sampling]]의 "각 vertex에서 서로 다른 자식은 독립"과 같은 구조). 이 공유 규칙이 [[pert:tree-identity.s2]]의 selector(공유하면 기대값 1, 아니면 0)의 근거다.

"Products of signs and their rational averages belong to this collection"은 [[pert:tree-identity.s1]]의 polarization 인자 $k^{-1}\sum_j\epsilon_jg_j$ 와 [[pert:tree-identity.s3]]의 부호 곱이 다시 이 모임 안에 있다는 것을 미리 확인해 두는 문장이다.

§8의 comparison.tex 53–56("The auxiliary priors used here may be taken to be finite products of finite mark spaces at each realized root")은 이 정의(좌표 수 $n$ 유한, 값 $\pm1$)와 [[pert:factor]](root가 주어지면 항이 유한 개)에서 온다(`\ref` 없음, 작성자 읽기).
