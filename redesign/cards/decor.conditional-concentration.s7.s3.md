---
id: decor:conditional-concentration.s7.s3
kind: step
title: '자식 항의 깊이 평균 (fiber bound)'
uses: [decor:average-holder, x:decor-average-comparisons, decor:average-definition, decor:projection-definition]
provides: 'decor:conditional-concentration.s7.s4 (γ=1/4), decor:overlap-concentration.s4 (γ=1/2, d 없이)'
math: |
  aligned 구성은 $d$와 $e$를 포함해 $D=b(S)+1$개의 서로 다른 깊이 좌표를 갖는다. $T_j$에 속한 항은 $D_j=b(T_j)+1$개 좌표만 쓴다: 이동된 항은 $\pi_j(\mathbf q)=(e+1,(q_v+1)_{v\in\operatorname{Br}(T_j)})$, 이동되지 않은 항은 $(e,(q_v)_{v\in\operatorname{Br}(T_j)})$. 남은 각 배정의 원상은 $L^{D-D_j}$개 이하이고, $L$이 크면 그 좌표는 $\eta/2$-regular이다. $w_j\ge0$가 이 좌표의 함수(자식 공분산)이면 $0<\gamma\le1$에 대해
  $$L^{-D}\sum_{\mathbf q\ \eta\text{-regular}}w_j(\pi_j(\mathbf q))^\gamma\le L^{-D_j}\sum_{\mathbf y\ \eta/2\text{-regular}}w_j(\mathbf y)^\gamma\le\Bigl(L^{-D_j}\sum_{\mathbf y\ \eta/2\text{-regular}}w_j(\mathbf y)\Bigr)^\gamma.$$
  이동되지 않은 항도 같은 상계를 갖는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [491, 511]}
status: proposed
---

첫 부등식은 안 쓰는 좌표의 합과 정수 이동(x:decor-average-comparisons), 둘째는 decor:average-holder다. 요점은 aligned 두 사본이 단일 사본 추정만 쓴다는 것이다. 독립으로 평균한 두 사본을 대각선으로 제한하는 일은 없다. 대각선 제한이었다면 평균에 관한 상계가 대각선 위의 값을 통제하지 못했을 것이다. $w_j$의 정의역에서 $e$ 또는 $e+1$은 $T_j$의 "첫 갈라짐보다 앞의 추가 깊이"이므로, 우변은 $V$의 정의에 쓰인 평균과 같은 꼴이다.
