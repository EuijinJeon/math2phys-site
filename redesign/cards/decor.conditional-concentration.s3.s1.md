---
id: decor:conditional-concentration.s3.s1
kind: step
title: '두 사본 old tree와 $S^+$ 제약의 구성'
uses: [decor:conditional-concentration.s1, pert:tree-identity, x:decor-topology, x:decor-eta-regular]
provides: 'conditional-concentration.s3.s2, s3.s3, s4, s5'
math: |
  $|S|=k\ge2$이고 $(d,\mathbf q)$가 $\eta$-regular이며 $d<e$ ($e$는 $S$의 첫 branching depth)일 때 다음 prescribed-tree 항등식 사례를 쓴다. old tree: $S$의 두 사본 I, II, stem은 깊이 $d$에서 갈라지고 내부 깊이 배정은 같은 좌표 $\mathbf q$를 공유한다. anchor: I의 고정된 옛 leaf (spin anchor). 제약 $\mathcal C$: anchor와 added color들이 $d$에서 분리된 $S^+$ 두 사본(target I, target II)을 이루고, anchor는 target I에서 원래 labeled 자리에 있다. 이 제약은 anchor와 added color 사이의 split depth만 처방하므로 pert:tree-identity의 허용 제약이다. color 순서는 target I 쪽 color 전부, 그다음 target II 쪽이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [292, 331]}
status: proposed
---

이 구간에는 그림 decor:shift-figure가 들어 있다. 그림은 target 갈라짐 하나를 $e$에서 $e+1$로 늦추면, 새 자식이 옛 tree에서 unary였던 깊이-$(e+1)$ vertex에서 fresh로 갈라져야 하고 계수가 $m_{e+1}-m_{e+2}=-\delta$임을 보인다. 서로 다른 target vertex는 깊이가 같아도 따로 계수를 낸다. 나중 target color는 자격이 있는 옛 leaf를 재사용할 수 있다.
