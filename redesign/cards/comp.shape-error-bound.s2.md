---
id: comp:shape-error-bound.s2
kind: step
title: 'regular tree: 유도된 부분 tree로 내려 깊이 평균 $\mathcal A_{L,\eta}$ 를 얻기'
uses: [tree:regular-shapes, tree:averaging-remark, x:tree-regular-shape, x:tree-sampling, decor:average-definition, x:decor-eta-regular, x:decor-topology]
provides: 'comp:shape-error-bound.s3'
math: |
  regular tree에서는 모든 유도된 부분 tree가 그 branching 깊이에 대한 내부 조건과 간격 조건을 유지한다. branching vertex가 $a$ 개인 topology에서 깊이 배정 하나의 확률은 $C_kL^{-a}$ 이하다. 유도된 부분 tree가 branching vertex $a'$ 개를 남기면, 그 깊이 배정 하나는 전체 tree로의 확장을 많아야 $L^{a-a'}$ 개 가진다. 쓰지 않는 좌표를 합해 없애면 $\mathcal A_{L,\eta}$ 의 정규화 $L^{-a'}$ 가 정확히 남는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [142, 148]}
status: proposed
---

**풀어 쓴 부등식 (작성자 정식화, 원문은 말로만 적는다).** 전체 tree의 topology $\tau$($a$ 개 branching vertex)와 부분집합 $S$ 를 고정하고, $S$ 가 유도하는 topology를 $U\in\mathfrak S_k$($a'$ 개 branching vertex, 깊이 $\mathbf q'$)라 하자. 사영 일관성([[x:tree-sampling]]: 일부 leaf를 지워도 남은 tree의 표본 법칙은 보존)에 의해 $\mathbb E\lvert R_S-\mathbb ER_S\rvert$ 는 $(U,\mathbf q')$ 의 sampled copy 위의 값 $z(\mathbf q')=\mathbb E\lvert R_U-\mathbb ER_U\rvert$ 와 같다. 그러면
$$\mathbb E_{Q_k}\bigl[\mathbb E\lvert R_S-\mathbb ER_S\rvert;\ \tau,\ \text{regular}\bigr]\le C_kL^{-a}\sum_{\mathbf q\ \text{regular}}z(\mathbf q')\le C_kL^{-a}\,L^{a-a'}\sum_{\mathbf q'\ \eta\text{-regular}}z(\mathbf q')=C_k\,\mathcal A_{L,\eta}z.$$
가운데 부등식은 $\mathbf q'$ 마다 확장 수가 $L^{a-a'}$ 이하이고 $\mathbf q'$ 가 regular라는 것([[tree:regular-shapes]]의 마지막 주장, unary가 된 vertex를 버린 뒤)을 쓴다. 이것이 [[tree:averaging-remark]]의 부분 모양 판이다. trees.tex의 regular와 §7의 $\eta$-regular는 같은 조건이다([[x:decor-eta-regular]], [[x:tree-regular-shape]]).

"each depth assignment has probability at most $C_kL^{-a}$"는 (tree:assignment-probability), 즉 [[tree:regular-shapes]]의 둘째 주장이다.
