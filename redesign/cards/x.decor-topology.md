---
id: x:decor-topology
kind: definition
title: 'topology, 깊이 배정, $b(S)$, 자식 모양'
uses: [x:decor-tree-sampling]
provides: '§7의 모든 진술이 다루는 대상 (S, T_j, S^+, S^U)'
math: |
  topology $S$는 labeled leaf를 가진 유한 rooted tree에서 unary vertex를 지운 것이다. $\operatorname{Br}(S)$는 branching vertex의 집합, $b(S)=|\operatorname{Br}(S)|$, $|S|$는 leaf 수다. 깊이 배정 $\mathbf q=(q_v)_{v\in\operatorname{Br}(S)}$는 각 branching vertex에 $\{0,\ldots,L-1\}$의 정수를 주며 모든 가지를 따라 엄격히 증가한다. $(S,\mathbf q)$의 sampled copy는 x:decor-tree-sampling의 규칙으로 뽑은, leaf가 $S$의 leaf이고 갈라짐이 정확히 깊이 $q_v$에서 일어나는(그 밖의 vertex는 unary) 깊이-$L$ tree다. $S$의 initial stem은 root에서 첫 branching vertex(깊이 $e$)까지의 경로다. 그 vertex 아래의 부분 topology $T_1,\ldots,T_s$ ($s\ge2$, 각각 첫 branching vertex를 거치는 경로를 root부터 공유)를 proper child shape라 한다. singleton은 $|S|=1$, $b(S)=0$이고 initial stem이 경로 전체다. 더 일반적으로, 임의의 branching vertex $v$ (깊이 $q_v$) 아래의 부분 모양은 root에서 $v$까지의 경로를 initial stem으로 갖는 topology로 본다. 그래서 $q_v$는 그 부분 모양의 initial stem 위에 있고, $v$의 자식 부분 모양들은 root에서 $v$까지 prefix를 공유한다. 첫 branching vertex의 proper child shape는 이 약속의 특수한 경우다.
physics: |
  ultrametric replica tree: replica들이 계층의 어느 깊이까지 같은 상태(같은 prefix)를 공유하는지를 나타낸 그림이다 (R11, R19의 사전에서 깊이 $d$ = 상태 계층의 $d$단계).
gap: |
  깊이는 보조 계층의 정수 단계이지 overlap 값이 아니다. "같은 상태를 공유한다"는 보조 chain의 prefix를 공유한다는 뜻이며 Gibbs 측도의 pure state 분해를 가정하지 않는다.
abstraction: exact
children: []
source:
  - {file: decorrelation.tex, lines: [18, 21]}
status: proposed
---

initial stem과 proper child shape의 정의는 tex 94, 208에서 쓰이는 용어를 이 카드에 모았다. 첫 갈라짐이 아닌 vertex의 자식 모양에 대한 약속은 tex 179–184 (lemma 7.3 증명의 "a branching vertex at depth $q$ with child shapes $T_1,\ldots,T_s$ … $\prod_j\mu_{q,T_j}$")가 암묵적으로 쓰는 것을 명시했다(검토 1 F8). 자식 모양 $T_j$는 root에서 깊이 $e$까지 $S$의 stem을 함께 갖는 topology로 읽는다. 그래야 $\mu_{e,T_j}$와 $v_N(T_j,e)$가 정의된다([[decor:projection-definition]]).
