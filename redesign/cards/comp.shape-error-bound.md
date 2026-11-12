---
id: comp:shape-error-bound
kind: step
title: 'shape error를 깊이 평균 분산으로 누르기 (comp:shape-error-bound)'
uses: [cavity:grid, tree:Q-rule, tree:regular-shapes, tree:averaging-remark, x:tree-regular-shape, x:tree-sampling, tree:multioverlap, decor:average-definition, x:decor-eta-regular, x:decor-topology, x:decor-spin-product]
provides: 'comp:shape-error.s1'
math: |
  $0<\eta<1/2$ 를 고정하고 $\mathfrak S_k$ 를 $[k]$ 의 공집합 아닌 부분집합 위의 labeled topology들의 유한 모임이라 하자. $L$, $\eta$, $N$ 에 무관한 $C_k$ 가 있어
  $$\mathbb E_{Q_k}\sum_{\varnothing\ne S\subseteq[k]}\mathbb E\lvert R_S-\mathbb ER_S\rvert\le C_k\Bigl(\eta+L^{-1}+\sum_{U\in\mathfrak S_k}\bigl(\mathcal A_{L,\eta}\operatorname{Var}(R_U)\bigr)^{1/2}\Bigr).\tag{comp:shape-error-bound}$$
  singleton $U$ 에 대한 평균은 깊이 좌표가 없다($\mathcal A_{L,\eta}z=z$).
physics: null
gap: null
abstraction: blackbox
children: [comp:shape-error-bound.s1, comp:shape-error-bound.s2, comp:shape-error-bound.s3]
source:
  - {file: comparison.tex, lines: [131, 153]}
status: proposed
---

**뼈대.** [[comp:shape-error-bound.s1]]: regular가 아닌 tree는 확률 $\le C_k(\eta+L^{-1})$ 이고 거기서 각 편차는 2 이하. [[comp:shape-error-bound.s2]]: regular tree에서는 부분집합 $S$ 가 유도하는 부분 tree $U$ 도 regular이고, 깊이 배정 확률 $\le C_kL^{-a}$ 와 확장 수 $\le L^{a-a'}$ 로 $Q_k$ 기여가 $C_k\mathcal A_{L,\eta}(\mathbb E\lvert R_U-\mathbb ER_U\rvert)$ 이하. [[comp:shape-error-bound.s3]]: Cauchy–Schwarz와 유한 합.

$C_k$ 는 줄마다 커질 수 있는 $k$ 만의 상수다(원문의 관례; [[tree:regular-shapes]]의 상수가 $L$, $\eta$ 에 무관하다는 것이 필요하다).
