---
id: decor:projection-definition
kind: definition
title: '첫 갈라짐에서의 사영 $a_{S,e}$와 오차량 $p_N(S,e)$'
uses: [decor:covariance-definition, x:decor-tree-sampling, x:decor-topology]
provides: 'decor:projection-bound, conditional-concentration의 사영 단계, overlap-concentration.s3의 G'
math: |
  $|S|\ge2$이고 $S$가 깊이 $e$에서 처음 갈라져 proper child shape $T_1,\ldots,T_s$를 갖는다고 하자. $e$는 각 $T_j$의 initial stem 위에 있다. 자식들은 $\mathscr F_e$가 주어지면 조건부 독립이므로 $\mu_{e,S}=\prod_j\mu_{e,T_j}$ (좌표별 곱)이다.
  $$a_{S,e}=\prod_{j=1}^s\mu_{e,T_j},\qquad p_N(S,e)=\sum_{j=1}^sv_N(T_j,e)^{1/4}.$$
  $0\le p_N(S,e)\le s\le|S|$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [208, 215]}
status: proposed
---

$a_{S,e}$는 깊이-$e$ prefix의 함수다. 같은 깊이 배정을 쓰는 서로 다른 stem 위에서 계산하면 같은 법칙을 갖는다. 증명에서 $a$, $b$, $b_\ell$이 그렇게 놓인 사본들이다.
