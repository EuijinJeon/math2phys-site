---
id: tree:telescoping
kind: lemma
title: '망원 항등식 $\sum_\beta(n_\beta m_{d_\beta+1}-m_{d_\beta})=n$'
uses: [x:tree-sampling, x:tree-path-kernels]
provides: 'tree:Q-rule의 정규화, tree:log-expansion.s1 ((k−1)!), tree:reference-total.s1 (부분 tree 판), tree:charging.s1 (fresh 선택의 절댓값 합 = s)'
math: |
  leaf가 $n$개인 tree $\mathcal T$ (x:tree-sampling)에서 $\operatorname{Int}(\mathcal T)$를 내부 vertex(root와 unary vertex 포함)의 집합, 내부 vertex $\beta$의 깊이를 $d_\beta$, 자식 수를 $n_\beta$라 하자(trees.tex 92–93의 정의). 망원 합이
  $$\sum_{\beta\in\operatorname{Int}(\mathcal T)}\bigl(n_\beta m_{d_\beta+1}-m_{d_\beta}\bigr)=n$$
  을 준다. 모든 항은 양이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [204, 209]}
status: proposed
---

원문은 "telescoping gives"(204)라고만 쓴다. 작성자 확인: root가 아닌 vertex는 정확히 한 내부 vertex의 자식이므로 $\sum_\beta n_\beta m_{d_\beta+1}=\sum_{v\ne\text{root}}m_{d_v}$. 여기서 $\sum_\beta m_{d_\beta}$(root 포함, $m_0=0$)를 빼면 root 아닌 내부 vertex들이 지워지고 leaf들만 남아 $n\cdot m_L=n$. 양수인 이유: $n_\beta\ge1$이고 $m_{d+1}>m_d$.

이 양들은 [[tree:insertion]]의 $\gamma_\beta$의 부호를 바꾼 것이다: $n_\beta m_{d_\beta+1}-m_{d_\beta}=-\gamma_\beta$. 따라서 모든 $\gamma_\beta<0$이고 $\sum_\beta|\gamma_\beta|=n$.
