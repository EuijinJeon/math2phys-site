---
id: pert:error
kind: definition
title: 'score 오차 $e_{\nu,N}(\mathbf u)$ 와 기대값 $\langle\cdot\rangle$, $\mathbb E_{\mathbf u}$ (6.4)'
uses: [pert:score, x:pert-standing]
provides: 'pert:concentration (진술과 s4.s2), pert:selection (ii)와 s2, pert:score-identity, pert:palm, pert:analytic.s3'
math: |
  $\langle\cdot\rangle$ 은 root가 주어진 조건부로 tilted path 하나를 따른 기대값, $\mathbb E_{\mathbf u}$ 는 고정된 $\mathbf u$ 에서 root를 평균하는 것이다.
  $$e_{\nu,N}(\mathbf u)=\frac{1}{c_\nu s_N}\mathbb E_{\mathbf u}\Big\langle\big|D_\nu-\mathbb E_{\mathbf u}\langle D_\nu\rangle\big|\Big\rangle.$$
physics: |
  score 오차 $e_{\nu,N}$ 은 [[g:score|score]]를 기대 개수 $c_\nu s_N$ 으로 나눈 것이 전체 평균에서 벗어나는 평균 절대 편차다. [[g:root]]가 주어졌을 때의 path 요동과 root 자체(물리 disorder, 섭동 개수·type·site)의 요동을 함께 잰다. $e_{\nu,N}\to0$ 이 score의 [[g:concentration|집중]]이다.
gap: |
  섭동 매개변수 $\mathbf u$ 는 고정되고 평균하지 않는다. $\langle\cdot\rangle$ 은 $L\ge2$ 에서 [[g:hierarchy|보조 계층]]의 변수를 tilt해 적분한 path 기대값이라 보통의 Gibbs 평균이 아니다. 정규화가 기대 개수 $c_\nu s_N\sim N^{3/4}$ 이므로 $e_{\nu,N}\to0$ 은 score의 상대 요동에 대한 $L^1$ 진술이다.
abstraction: exact
children: []
source:
  - {file: perturbations.tex, lines: [83, 93]}
status: proposed
---

중심이 $\langle D_\nu\rangle$ 이 아니라 $\mathbb E_{\mathbf u}\langle D_\nu\rangle$(root까지 평균한 상수)이므로 두 요동이 함께 들어간다. [[pert:concentration.s4.s2]]는 삼각부등식 $\mathbb E_{\mathbf u}\langle|D-\mathbb E_{\mathbf u}\langle D\rangle|\rangle\le\mathbb E_{\mathbf u}\langle|D-\langle D\rangle|\rangle+\mathbb E_{\mathbf u}|\langle D\rangle-\mathbb E_{\mathbf u}\langle D\rangle|$ 로 둘을 따로 누른다(작성자 풀이). "tilted path 하나"의 법칙은 tree에서 leaf 하나를 남긴 사영과 같다([[x:tree-sampling]]의 사영 일관성). 이것이 [[pert:score-identity]]의 "anchor marginal is always one tilted path"에 쓰인다.
