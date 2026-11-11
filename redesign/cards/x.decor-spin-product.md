---
id: x:decor-spin-product
kind: definition
title: 'spin 곱 벡터 $A_S$, 내적 $x\cdot y$, $R_S$'
uses: [tree:multioverlap, x:decor-topology]
provides: '§7의 모든 축약과 노름. decor:overlap-concentration의 대상 R_S'
math: |
  $(S,\mathbf q)$의 sampled copy에 대해 $A_S=\bigl(\prod_{a\in S}\sigma_i^a\bigr)_{i\le N}\in\{-1,1\}^N$, $x\cdot y=N^{-1}\sum_{i=1}^Nx_iy_i$, $\|x\|_N^2=x\cdot x$로 둔다. 그러면 tree:multioverlap의 multioverlap은 $R_S=\mathbf1\cdot A_S$다. $\mathbb E$는 root(disorder와 선택된 매개변수)와 tree 표본추출을 모두 포함하고, $\operatorname{Var}(R_S)$는 고정된 $(S,\mathbf q)$에 대한 이 $\mathbb E$ 아래의 분산이다. $\|\cdot\|_{L^2}=(\mathbb E|\cdot|^2)^{1/2}$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [60, 61]}
  - {file: decorrelation.tex, lines: [87, 92]}
status: proposed
---

두 측 I, II의 spin 곱 벡터의 축약 $A^{\rm I}\cdot A^{\rm II}$은 두 측의 모든 leaf의 multioverlap이다. 증명에서 시험함수 $f$와 target overlap이 모두 이 꼴이다.
