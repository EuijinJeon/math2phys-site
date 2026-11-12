---
id: comp:shape-error
kind: proposition
title: 'tree 법칙 평균한 multioverlap 요동이 사라진다 (shape error)'
uses: [x:comp-standing, x:pert-selected-limits, cavity:grid, tree:log-expansion, tree:Q-rule, tree:regular-shapes, tree:averaging-remark, x:tree-regular-shape, x:tree-sampling, tree:multioverlap, decor:overlap-concentration, decor:average-definition, x:decor-eta-regular, x:decor-topology, x:decor-spin-product, x:decor-limit-order]
provides: 'comp:insertion-comparison.s3 (comparison.tex 209–211: 차수별 tree 평균 오차가 순서 있는 극한에서 0). 규칙 P11, L1 수 6'
math: |
  $Q_k$ 를 tree:log-expansion의 tree 법칙($m_d=d/L$)이라 하자. 모든 고정 $k$ 에 대해
  $$\lim_{L\to\infty}\limsup_{N\to\infty}\mathbb E_{Q_k}\sum_{\varnothing\ne S\subseteq[k]}\mathbb E\lvert R_S-\mathbb ER_S\rvert=0\qquad(k\text{ fixed}).\tag{comp:shape-error}$$
  여기와 아래에서 안쪽 극한은 고정 $L$ 의 선택된 수열을 따른다. 안쪽 $\mathbb E$ 는 $Q_k$ 로 뽑은 tree $\mathcal T$ 를 고정한 채 root와 그 tree의 표본추출에 대한 기대값이다.
physics: |
  log 전개의 [[g:tree-law|tree 법칙]] $Q_k$ 로 뽑은 $k$ 개 [[g:replica|replica]]의 tree 위에서, 모든 [[g:multioverlap|multioverlap]]의 평균 절대 요동을 tree 평균하면 $L\to\infty$ 에서 사라진다. 고정 깊이마다가 아니라 깊이 평균으로만 아는 [[g:overlap-concentration|multioverlap 집중]]이 log 전개에는 충분하다.
gap: |
  (1) [[g:order-of-limits|극한 순서]]: 각 고정 $L$ 에서 [[g:selected-sequence|선택된 수열]]을 따라 $\limsup_N$, 그다음 $L\to\infty$. 증명 안에서는 [[g:eta-regular|regularity]] 매개변수 $\eta$ 를 고정한 채 이 두 극한을 취한 뒤 $\eta\downarrow0$ 한다. $L$ 에 균일한 $N$ 수렴 속도는 없다. (2) 고정 tree마다의 진술이 아니라 $Q_k$ 평균이다: 예외적 깊이의 tree(경계 근처, 서로 가까운 갈라짐)는 확률 $C_k(\eta+L^{-1})$ 로만 처리된다. (3) 기대값은 선택된 매개변수를 고정한 [[g:root]]·tree 기대값이다. (4) 극한값이나 overlap이 깊이만의 함수로 수렴한다는 것을 말하지 않는다.
abstraction: approximation
children: [comp:shape-error-bound, comp:shape-error.s1]
source:
  - {file: comparison.tex, lines: [123, 130]}
  - {file: comparison.tex, lines: [131, 156]}
status: proposed
---

**원문에서의 위치.** 정리 환경이 아니라 본문의 주장이다("We need the following consequence of the decorrelation theorem", 123–124). 증명도 본문(130–156)이다. 그래서 기계 검사의 포함 대상은 아니지만, 이 카드와 자식이 모든 줄을 덮는다.

**증명의 뼈대.** 첫 단계는 원문의 식 라벨이 있어 그 라벨을 ID로 쓴다.
- [[comp:shape-error-bound]]: 고정 $0<\eta<1/2$ 에서 좌변 $\le C_k\bigl(\eta+L^{-1}+\sum_{U\in\mathfrak S_k}(\mathcal A_{L,\eta}\operatorname{Var}(R_U))^{1/2}\bigr)$.
- [[comp:shape-error.s1]]: [[decor:overlap-concentration]]을 고정 $\eta$ 에서 ($N$ 먼저, 그다음 $L$) 적용하고, 마지막에 $\eta\downarrow0$.

**§7에서 받는 것 (확인).** [[decor:overlap-concentration]](각 $U\in\mathfrak S_k$ 와 고정 $\eta$, singleton은 좌표 없음), [[decor:average-definition]](정규화 $L^{-a'}$, 질량 $\le1$), [[x:decor-eta-regular]](§7의 regular가 trees.tex의 regular와 같은 조건), [[x:decor-topology]](labeled topology, 깊이 배정), [[x:decor-spin-product]]($\operatorname{Var}(R_U)$ 는 고정 깊이 배정에서 root를 포함한 분산), [[x:decor-limit-order]](안쪽 극한은 고정 $L$ 의 선택된 수열). §3에서 [[tree:Q-rule]], [[tree:regular-shapes]], [[tree:averaging-remark]]의 논법, [[x:tree-sampling]]의 사영 일관성.
