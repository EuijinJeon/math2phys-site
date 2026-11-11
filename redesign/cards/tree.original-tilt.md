---
id: tree:original-tilt
kind: definition
title: '분배함수에서 만든 tilted kernel'
uses: [x:tree-path-kernels]
provides: 'tree:insertion의 가정 (kernel이 power mean의 tilted kernel). §5 cavity의 tilted reservoir kernel (cavity.tex 55–56, 117–118)'
math: |
  $P_d$ ($1\le d<L$)를 보조 prior kernel이라 하고 $X_{L-1}=\log Z$로 두고 재귀적으로
  $$X_{d-1}=m_d^{-1}\log P_de^{m_dX_d}\qquad(1\le d<L)$$
  로 정한다. 대응하는 tilted kernel은
  $$K_d(dz\mid\mathscr F_{d-1})=e^{m_d(X_d(z)-X_{d-1})}P_d(dz\mid\mathscr F_{d-1}),\qquad 1\le d<L$$
  이다. recursion에 의해 확률 kernel이다. 마지막 kernel $K_L$은 보조 prefix가 주어진 spin 배치의 Gibbs 분포다. $L=1$이면 이 마지막 kernel만 있다.
physics: |
  깊이 $d$의 보조 변수 $z$를 prior $P_d$에서 뽑되 그 아래 계층의 반복 log $X_d(z)$에 대해 $e^{m_dX_d}$로 재가중한다. 정규화 $X_{d-1}=m_d^{-1}\log P_de^{m_dX_d}$가 깊이 $d$의 [[g:power-mean|power mean]]이다. 마지막 깊이에서는 보조 [[g:state|상태]]가 주어진 Gibbs 분포로 spin을 뽑는다.
gap: |
  $X_d$는 보조 prefix가 주어진 반복 log이고, $L\ge2$에서는 보통 뜻의 free entropy가 아니다([[g:root-logarithm]]). 재가중되는 것은 보조 변수의 값이지 [[g:physical-pure-state|물리적 pure state]]가 아니다. 이 재가중을 물리의 $Z^m$ 재가중과 같은 꼴로 읽는 것은 [[g:hierarchy]]의 물리 대응 칸에 intuition으로만 있다.
abstraction: exact
children: []
source:
  - {file: trees.tex, lines: [51, 65]}
status: proposed
---

$Z$는 보조 prefix 전체(깊이 $L-1$까지)에 의존하는 leaf 분배함수다. 원문은 "a partition function"(51)이라고만 쓴다. 확률 kernel임은 $\int e^{m_d(X_d(z)-X_{d-1})}P_d(dz)=e^{-m_dX_{d-1}}P_de^{m_dX_d}=1$에서 바로 나온다.
