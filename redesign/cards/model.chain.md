---
id: model:chain
kind: definition
title: '시행 법칙: $\mathcal M_j$, $\zeta\in\mathcal M_{r+1}$, $\mathbf m$, label별 사슬 (2.7)'
uses: [x:model-message, model:hamiltonian]
provides: 'model:vs, model:ve, model:power-means의 message와 $\eta$. x:tree-path-kernels (trees.tex 26–27: 시행 사슬이 path kernel의 한 예: $\eta_d$ 는 깊이 $d$, $x$ 는 깊이 $r$), comparison.tex 72(comp:encoding의 재귀가 이것의 branching 판)'
math: |
  $\mathcal P(E)$ 는 $E$ 위의 Borel 확률측도들이다. $\mathcal M_1=\mathcal P(\mathbb R)$, $\mathcal M_{j+1}=\mathcal P(\mathcal M_j)$ 로 두고 각각 약수렴 위상과 그 Borel $\sigma$-field를 준다. $r\ge1$, $\zeta\in\mathcal M_{r+1}$, $0<m_1<\cdots<m_r<1$ 을 고정한다. 각 message label $\omega$ 마다 독립으로
  $$\eta_0^\omega\sim\zeta,\qquad\eta_{d+1}^\omega\mid\eta_d^\omega\sim\eta_d^\omega\ \ (0\le d\le r-2),\qquad x^\omega\mid\eta_{r-1}^\omega\sim\eta_{r-1}^\omega\tag{2.7}$$
  를 뽑는다. $r=1$ 이면 각 label이 먼저 법칙 $\zeta$ 의 무작위 확률측도 $\eta_0$ 를 뽑고, 다음에 법칙 $\eta_0$ 의 $x$ 를 뽑는다. 더 높은 단계는 측도 뽑기를 반복한다. 이 변수들은 모두 물리적 disorder와 독립이다. $x_1,\ldots,x_p$ 와 $x_\ell^j$ ($j\ge1$, $1\le\ell<p$) 에는 서로 다른 label을 쓴다.
physics: |
  $r$단 RSB의 시행 [[g:order-parameter|order parameter]]: $r=1$ 이면 cavity field의 "분포의 분포"(population of populations)이고, $\mathbf m$ 은 [[g:parisi-parameters|Parisi parameter]]이다. label이 다른 [[g:message|message]]는 서로 독립이고 [[g:disorder|disorder]]와도 독립이다.
gap: |
  (1) 시행 법칙은 임의다. 실제 계에서 만든 것이 아니고 moment 조건도 없다. (2) 사슬의 깊이 $d$ 를 [[g:physical-pure-state|물리적 pure state]] 계층의 단계와 동일시하지 않는다. $\mathbf m$ 은 여기서 임의이고(inf의 범위), 하한에서는 최적화하지 않고 $m_d=d/L$ 로 고정한다([[g:grid]]). (3) $r=0$ 은 이 카드가 아니라 x:model-depth-zero에서 따로 정한다.
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [68, 81]}
status: proposed
---

$\eta_d^\omega$ 는 $\mathcal M_{r-d}$ 의 값을 갖는다($\eta_0\in\mathcal M_r$, $\eta_{r-1}\in\mathcal M_1$). 원문에 명시되어 있지 않고 (2.7)에서 읽은 것이다. label 집합은 $\{1,\ldots,p\}\sqcup\{(j,\ell):j\ge1,\ 1\le\ell<p\}$ 로 가산 무한이다: model.tex 80–81은 $x_\ell^j$ 의 첨자를 $j\le k$ 가 아니라 $j\ge1$ 로 잡고, 82행도 $\theta,\theta_1,\ldots$ 를 $k$ 와 독립인 무한열로 잡는다. 사슬들은 label끼리 i.i.d.이고 $k$ 와 독립이므로(71, 79–80행) $V_{\rm s}$ 는 처음 $k$ 개 묶음만 쓰는 함수이고, $\mathscr F_d$(90–91행)는 가산 개 변수가 생성하는 $\sigma$-field다. $V_{\rm s}$ 의 label과 $V_{\rm e}$ 의 label도 서로 다르다(80–81행). upper.tex 40, comparison.tex 182도 서로 다른 label의 약속을 쓴다.
