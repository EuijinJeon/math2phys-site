---
id: x:pert-colored-extensions
kind: definition
title: 'spin/marker anchor, 추가 color, 제약 $\mathcal C$, 허용 history와 $R_E$'
uses: [x:pert-test-setup, x:pert-mark-specification, tree:extension-expansion, x:tree-extension-history, tree:multioverlap]
provides: 'pert:tree-identity의 진술과 s2–s4. \ref 없이 §7: decorrelation.tex 81, 265, 298–302, 529–560 (spin anchor, marker anchor, added color, 제약), decor:overlap-concentration.s1, s2.s1, decor:conditional-concentration.s2.s1, s3.s1'
math: |
  $S_0=\sigma_i$ 일 때 anchor를 spin anchor, $S_0=1$ 일 때 marker anchor라 부른다. 추가 color는 $1,\ldots,k$ 로 순서가 있고 anchor는 color $0$ 이다. 추가 color들은 tree:extension-expansion의 canceled-anchor 확장 규칙에 따라, anchor와 같지 않은 서로 다른 replica 위치를 차지한다. 제약 $\mathcal C$ 는 추가 color들과 anchor만 관여하는 쌍별 split 깊이의 임의의 일관된 모임을 처방한다. 다른 old replica가 관여하는 추가 제한은 두지 않는다. $\mathfrak E(\mathcal T,a_*,\mathcal C)$ 를 허용된 extension history의 집합, $c_E$ 를 그 lemma의 계수라 하자. history $E$ 에 대해
  $$R_E=\frac1N\sum_{i=1}^N\begin{cases}\sigma_i^{a_*}\prod_{j=1}^k\sigma_i^{a_j(E)},&\text{spin anchor},\\ \prod_{j=1}^k\sigma_i^{a_j(E)},&\text{marker anchor}.\end{cases}$$
  $k=0$ 이면 이것은 각각 $R_{\{a_*\}}$ 와 $1$ 이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [429, 449]}
status: proposed
---

확장 규칙 자체(old leaf 재사용 계수 1, fresh path 계수 $\gamma_\beta$)는 [[x:tree-extension-history]]에 있고, 원문은 그것을 lemma [[tree:extension-expansion]]의 이름으로 가리킨다. "anchor와 같지 않은 서로 다른 위치"는 anchor가 protected라 재사용되지 않고 고른 leaf가 다시 고를 수 없다는 규칙에서 온다. [[g:anchor]], [[g:extension-history]], [[g:mark]].

제약이 "anchor와 추가 color 사이"로 한정되는 이유(작성자 읽기): selector([[pert:tree-identity.s2]])는 mark 함수 $g_0,g_1,\ldots,g_k$ 를 통해서만 작동하고, mark 함수는 anchor(color 0)와 추가 color의 path에만 붙는다. old replica에는 mark 함수가 붙지 않으므로 그것과의 관계는 지정할 수 없다. §3의 [[x:tree-reference-paths]]도 같은 한정을 둔다.

$R_E$ 는 tree $\mathcal T_E$ 의 [[g:multioverlap]]이다(spin anchor이면 anchor 포함). marker anchor에서 $k=0$ 이면 $R_E=1$ 이므로 그 경우의 항등식은 자명하다.
