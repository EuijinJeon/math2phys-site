---
id: x:tree-path-kernels
kind: definition
title: 'path kernel 열, 지수 $m_d$, prefix $\sigma$-field'
uses: [model:chain]
provides: '§3의 모든 카드가 서 있는 틀. §4 upper (message-label tree), §5 cavity (tilted reservoir kernel), §6–§8 (reservoir의 보조 계층)이 이 틀의 사례다'
math: |
  정수 $L\ge1$과 수
  $$0=m_0<m_1<\cdots<m_{L-1}<m_L=1$$
  을 고정한다. path는 깊이 $0,\ldots,L$을 갖고 깊이 0의 변수가 root다. $1\le d\le L$에 대해 확률 kernel $K_d$는 깊이 $d-1$까지의 prefix 전체가 주어지면 다음 변수를 뽑는다. $\mathscr F_d$는 prefix $\sigma$-field다(깊이 $d$까지의 prefix가 생성하는 것으로 읽는다. 그래서 $K_d=K_d(dz\mid\mathscr F_{d-1})$). root의 분포는 모든 insertion 동안 고정된다. $r$단 적용에서는 $L=r+1$이다: 깊이 $1,\ldots,r$에 보조 변수, 깊이 $L$에 Gibbs spin 배치가 놓인다. $r\ge1$인 시행 법칙 (model:chain)에서는 $0\le d<r$에 대해 $\eta_d$가 깊이 $d$ 변수이고 $x$가 깊이 $r$ 변수다.
physics: |
  [[g:hierarchy|보조 계층]]의 뼈대: 깊이 $L=r+1$의 계층이 $r$단 RSB의 자리다([[g:rsb-steps]]). 깊이 $d$까지의 prefix가 [[g:state|상태]]이고, 깊이마다 [[g:parisi-parameters|Parisi parameter]] $m_d$가 하나씩 붙는다($m_0=0$, $m_L=1$).
gap: |
  kernel 열 $K_1,\ldots,K_L$은 임의의 확률 kernel이다. 이 절의 모든 항등식은 이 일반성에서 증명되며 무한 계층의 가중치 구조나 [[g:physical-pure-state|물리적 pure state]] 분해를 가정하지 않는다(trees.tex 10–12 "for finite sequences of arbitrary probability kernels, without assuming an infinite hierarchy"). $m_d$는 power mean의 지수열일 뿐이고, 여기서는 최적화되지 않는다.
abstraction: exact
children: []
source:
  - {file: trees.tex, lines: [14, 27]}
status: proposed
---

"$\mathscr F_d$ is the prefix sigma-field"(trees.tex 22)는 깊이를 명시하지 않는다. $K_d(dz\mid\mathscr F_{d-1})$ 표기(trees.tex 59, 77)와 "given the whole prefix through depth $d-1$"(21–22)에 맞춰 $\mathscr F_d$를 깊이 $d$까지의 prefix $\sigma$-field로 읽었다. root는 깊이 0의 변수이므로 $\mathscr F_0$은 root를 담는다. 쓰이는 곳에서 root는 disorder와 매개변수를 포함한다([[x:tree-extra-variables]]의 "additional root variables remain quenched").

시행 법칙 쪽 대응(26–27)에서 $\eta_0$은 root다. 이 대응은 §4 upper의 message-label tree가 쓴다(upper.tex 97–105).
