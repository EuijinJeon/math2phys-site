---
id: pert:tree-identity
kind: theorem
title: 'prescribed tree 위의 항등식 (Theorem 6.5)'
uses: [x:pert-colored-extensions, x:pert-test-setup, pert:selection, x:pert-selected-limits, pert:analytic, pert:analytic-difference, x:pert-mark-specification, tree:extension-expansion, x:tree-sampling]
provides: '§7 전체: x:decor-limit-order, decor:identity-error (decorrelation.tex 51), decor:overlap-concentration.s1, s2, s2.s1, s2.s2, decor:conditional-concentration과 s2, s2.s1, s3, s3.s1, s6, decor:section (decorrelation.tex 6–9). overview.tex 24. 규칙 P7, L1 수 4'
math: |
  위에서 정의한 섭동 족에 대해, pert:selection의 모든 수열을 따라
  $$\sum_{E\in\mathfrak E(\mathcal T,a_*,\mathcal C)}c_E\,\mathbb E[fR_E]-\mathbb Ef\sum_{E\in\mathfrak E(\{a_*\},a_*,\mathcal C)}c_E\,\mathbb E[R_E]\longrightarrow0.$$
  이것은 모든 고정 old tree, 두 종류의 anchor 모두, 그 multioverlap의 모든 유계 다항식 $f$, 순서 붙은 추가 color의 모든 유한 개수, 처방된 모든 제약 $\mathcal C$ 에 대해 성립한다. 빈 추가도 허용된다. 오차는 고정 $L$, 고정 tree, 고정 제약에서, $L$ 에 대한 어떤 극한보다도 먼저 0으로 보낸다.
physics: |
  [[g:selected-sequence|선택된 수열]]을 따라 [[g:reservoir|reservoir]]에서 다음이 성립한다. old [[g:prescribed-tree|prescribed tree]]의 [[g:anchor|anchor]] [[g:replica|replica]]에 섭동 방향 $k$ 개를 넣으면 새 replica $k$ 개를 붙이는 모든 방법([[g:extension-history|extension history]])에 대한 부호 있는 계수 합이 나온다. 그 합을 old tree의 overlap 시험함수 $f$ 와 곱해 평균한 것은, 같은 합을 anchor 하나만 있는 tree에서 계산한 것에 $\mathbb Ef$ 를 곱한 것과 같아진다. 깊이별 [[g:mark|mark]]로 anchor와 새 replica들 사이의 split 깊이를 임의로 지정할 수 있다. 이것이 [[g:tree-identity|prescribed-tree 항등식]]이다.
gap: |
  (1) 고정 $L$, tree, 제약, $f$ 마다 $N\to\infty$ 에서만 성립하고 오차율은 주지 않으며 어느 것에도 균등하지 않다([[g:order-of-limits]]). 집중의 근거는 [[g:perturbation|섭동]] score의 type별 집중이다. (2) 꼴은 history 위의 부호 있는 합이다: $c_E$ 는 old leaf 재사용이 $+1$, fresh path가 음수 $\gamma_\beta$ 다([[g:tree-coefficient]]). (3) 제약은 anchor와 새 color 사이의 split 깊이만 지정하고 다른 old replica와의 관계는 지정하지 못한다. mark 깊이는 $1,\ldots,L-1$ 이다. (4) 계층(tree) 구조는 이 항등식에서 나오는 것이 아니라 [[g:hierarchy|보조 계층]]의 구성에 들어 있다. 물리적 Gibbs 측도의 [[g:physical-pure-state|물리적 pure state]] 구조나 overlap의 극한값·분포는 이것에서 나오지 않는다. (5) 원문이 선행 연구로 드는 것과의 관계(perturbations.tex 17–22)는 [[g:tree-identity]]의 물리 대응 칸에 intuition으로만 있고, 원문은 이 항등식이 그것들과 같다거나 그것들에서 나온다고 하지 않는다.
abstraction: approximation
children: [pert:tree-identity.s1, pert:tree-identity.s2, pert:tree-identity.s3, pert:tree-identity.s4]
source:
  - {file: perturbations.tex, lines: [451, 470]}
  - {file: perturbations.tex, lines: [472, 536]}
status: proposed
---

**증명의 뼈대.**
- [[pert:tree-identity.s1]]: $k=0$ 은 [[pert:analytic]]의 상수 계수다(상수 mark). $k\ge1$ 이면 $A=1+\sum_jz_jg_j\sigma_i$ 의 혼합 도함수를 단일 $g$ 의 $k$ 차 계수 $Q_N(g)=k![t^k]H_N(t,0)$ 의 polarization으로 쓴다. 각 항의 인자 $k^{-1}\sum_j\epsilon_jg_j$ 가 mark 족에 들어 있으므로 pert:analytic으로 0으로 간다. 혼합 도함수의 전개가 순서 붙은 확장 규칙이다.
- [[pert:tree-identity.s2]]: 깊이 $d$ 의 새 Rademacher 좌표를 두 color의 $g_a$, $g_b$ 에 함께 넣으면 mark 기대값이 "깊이 $d$ vertex 공유"의 지시함수가 된다(selector, (6.18)).
- [[pert:tree-identity.s3]]: 정확한 split은 $H_d-H_{d+1}$, 그 곱과 일차결합으로 임의의 제약을 고른다. 각 항의 $g$ 는 부호 곱이라 족 안에 있다.
- [[pert:tree-identity.s4]]: 혼합 canceled-anchor 전개를 $H_N$ 에 적용하고 mark를 selector로, insertion site를 균일 평균하면 $R_E$ 가 나와 (6.17). 일차결합으로 다항식 $f$ 로 확장. mark는 깊이 $L-1$ 까지만 필요.

**양화사.** "along every sequence from pert:selection"이므로 (iii)까지 갖춘 선택된 수열이면 어느 것이든 된다. $\mathbb E$ 는 그 수열의 선택된 벡터에서의 reservoir 기대값이다([[x:pert-test-setup]], [[x:pert-selected-limits]]). 원문은 이 정리에 두 라벨(`pert:tree-identity`, `pert:identity`)을 붙였다. 이 카드가 둘 다를 담는다.

**§7이 받는 꼴과의 대조.** §7 카드가 쓰는 사례(singleton spin anchor $k=0$, $f=R_S$; spin anchor $k=1$ split $d$; 두 사본 old tree와 $S^+$ 제약; marker anchor와 $S$ 사본 제약)는 모두 "anchor와 추가 color만 관여하는 제약", "유계 multioverlap 다항식 $f$"의 범위 안이고, §7이 쓰는 것은 고정 $L$ 에서의 $o_N(1)$ 뿐이다. 어긋남은 찾지 못했다(섹션 카드 본문).
