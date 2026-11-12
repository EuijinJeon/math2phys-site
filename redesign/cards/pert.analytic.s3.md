---
id: pert:analytic.s3
kind: step
title: '$u_\nu\le2j^{-j}$ 로 극한 함수를 0으로'
uses: [pert:analytic.s1, pert:analytic.s2, pert:palm, pert:parameters, pert:selection, x:pert-selected-limits]
provides: 'pert:analytic의 결론'
math: |
  충분히 큰 모든 고정 $j$ 에 대해, 해당 type과 pert:palm이
  $$\limsup_{N\to\infty}|H_N(j^{-1},0)|\le C\limsup_{N\to\infty}|u_{\nu,N}|\le2Cj^{-j}$$
  를 준다. 여기서 score 오차는 $j$ 고정에서 0으로 가고, pert:palm에 의해 모든 $j$ 에 같은 함수 $H_N$ 이 쓰인다. 따라서 $|H(j^{-1})|\le2Cj^{-j}$ 이다. $H$ 의 첫 0 아닌 Taylor 계수가 차수 $q$ 였다면 충분히 큰 모든 $j$ 에서 $|H(j^{-1})|\ge cj^{-q}$ 가 되어 모순이다. 따라서 $H$ 는 0 근처에서 항등적으로 0이고, 이것이 계수마다 주장을 증명한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [411, 425]}
status: proposed
---

풀이(작성자). type $\nu=(\text{specification},j)$ 에서 $|H_N(1/j,0)|\le|H_N(1/j,u_{\nu,N})|+|u_{\nu,N}|\sup|\partial_uH_N|\le\|f\|_\infty e_{\nu,N}+C|u_{\nu,N}|$([[pert:palm]], [[pert:analytic.s1]]). $e_{\nu,N}\to0$ 은 [[pert:selection]] (ii)이고 $u_{\nu,N}\in I_\nu=[j^{-j},2j^{-j}]$ 는 선택된 벡터의 성분이다([[pert:parameters]]). "충분히 큰 $j$"는 $1/j$ 가 s1, s2의 원판 안에 들어가기 위해서다. 상수 $C$ 가 $j$ 에 무관한 것(s1)이 결정적이다: 그래서 $j^{-j}$ 가 $j^{-q}$ 를 이긴다. "$H$ 가 0 근처에서 0"이면 모든 계수가 0이고, s2의 계수 수렴으로 $H_N(t,0)$ 의 각 계수가 0으로 간다.
