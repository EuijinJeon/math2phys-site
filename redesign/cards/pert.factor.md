---
id: pert:factor
kind: definition
title: 'Poisson 섭동 factor $\psi_\nu=1+t_\nu g\sigma_i+u_\nu g_0S_0$ (6.2)'
uses: [pert:parameters, x:pert-mark-specification, cavity:factor-bounds, x:cavity-root-convention, cavity:negligible, tree:insertion]
provides: '§5 cavity:factor-bounds의 틀을 채우는 구체적 섭동(cavity.tex 32 "The factors needed later are specified in pert:section"). pert:score, pert:concentration.s3.s2–s3.s3 (개수·type·site가 root의 독립 label), pert:palm.s1 (Poisson add-one), x:pert-order-of-choices (c_ν를 먼저 고정)'
math: |
  type들을 $\nu\in\mathbb N$ 으로 번호 매기고 $c_\nu>0$, $\sum_\nu c_\nu=1$ 인 상수를 고른다. type마다 독립으로 $n_\nu\sim\operatorname{Poisson}(c_\nu s_N)$, $s_N=N^{3/4}$ 로 둔다. 각 항은 독립 균일 site $i\in[N]$ 와 자기 mark 과정의 독립 사본을 가진다. leaf에서 각 항은 spin weight에
  $$\psi_\nu=1+t_\nu g\sigma_i+u_\nu g_0S_0$$
  를 곱한다. 특히 $1/2<\psi_\nu<3/2$ 이다. 개수, type, site는 root에 속하고, mark 변수는 product prior로 배정된 보조 깊이에서 뽑힌다. 총 개수가 $\operatorname{Poisson}(s_N)$ 이므로 이 구성은 거의 확실히 유한 개의 항만 쓴다. factor 경계는 (cavity:negligible)에서처럼 power mean을 거친 항별 비교를 허락한다.
physics: |
  평균 $N^{3/4}$ 개(곧 site당 밀도 $N^{-1/4}$)의 단일 site [[g:perturbation|섭동]] 인자를 Boltzmann 무게에 곱한다. 각 인자는 무작위 site 하나의 spin과 [[g:hierarchy|보조 계층]]의 [[g:mark|mark]] 부호에 의존하며 값이 $(1/2,3/2)$ 안에 있다. 인자 하나를 넣거나 빼도 [[g:root-logarithm|root logarithm]]은 유계만큼만 바뀐다.
gap: |
  무한소 섭동이 아니다: 인자 하나의 크기는 $O(1)$ 이고($|t_\nu|\le1/4$), 작은 것은 개수의 밀도다. 개수·type·site는 [[g:root]] 변수이고 mark는 보조 변수다. 섭동 매개변수 $\mathbf u$ 는 무작위가 아니라 고정값이다(x:pert-parameter-measure). 이 섭동이 root logarithm 밀도를 $o(1)$ 만 옮긴다는 것은 cavity:negligible의 몫이다. "유계만큼"의 정량($\log2$ 이하)은 cavity.tex 95–96에 있고 이 카드의 원문은 항별 비교가 가능하다는 것만 말한다.
abstraction: weakening
children: []
source:
  - {file: perturbations.tex, lines: [51, 65]}
status: proposed
---

$1/2<\psi_\nu<3/2$: $|t_\nu g\sigma_i|\le1/4$, $|u_\nu g_0S_0|\le2j^{-j}\le2\cdot4^{-4}$ 이므로 $|\psi_\nu-1|<1/2$(작성자 계산). §5의 [[cavity:factor-bounds]]는 $1/2\le\psi_\nu\le3/2$ 를 요구하므로 이 섭동이 그 틀에 든다.

"termwise comparison through the power means, as in (cavity:negligible)"는 [[tree:insertion]]의 단조성(root-가측 상수로 위아래가 묶인 insertion은 모든 $Y_d$ 를 같은 상수로 묶는다)을 `\ref` 없이 쓰는 것이다(tree:section의 내주는 것 표와 같은 읽기). 인자 하나는 $\log(3/2)$, $\log2$ 안에서 root logarithm을 바꾼다.

"Counts, types, and sites belong to the root"는 [[x:cavity-root-convention]](cavity.tex 29)과 같은 약속이다. [[g:root]] 항목도 이 행을 정의 위치로 든다.
