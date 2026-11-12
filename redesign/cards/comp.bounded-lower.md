---
id: comp:bounded-lower
kind: corollary
title: 'bounded 법칙의 하한: $\liminf_NF_N\ge\inf_{r\ge0}\Phi_r$'
uses: [x:cavity-bounded, model:hamiltonian, model:chain, model:functional, x:model-depth-zero, model:trial-bounds, cavity:grid, x:comp-standing, comp:low-increments, comp:encoding, comp:insertion-comparison]
provides: 'main:theorem.s2, main:theorem.s3 (reduction.tex 64, 76: 잘린 모형의 하한), reduction:section (reduction.tex 4). model:section의 주정리 증명 경로. 규칙 P11(차이 칸), L1 수 6'
math: |
  모든 bounded이고 순열 불변인 상호작용 법칙과 bounded 장 법칙에 대해, (2.11)과 그 $r=0$ 판으로 정의한 functional로
  $$\liminf_{N\to\infty}F_N\ge\inf_{r\ge0}\Phi_r.$$
physics: |
  [[g:bounded-law|유계]]이고 입력에 대해 대칭([[g:permutation-invariance|순열 불변]])인 [[g:interaction|상호작용]]과 유계 [[g:field|장]]에서, quenched [[g:pressure|pressure]]의 liminf는 모든 유한 단계 시행값의 inf([[g:phi]]) 이상이다.
gap: |
  (1) 하한만이고 극한의 존재는 상한(upper:bound)과 합칠 때 나온다. (2) [[g:factorization|전개]]와 [[g:positivity|부호 조건]]을 쓰지 않는다. 일반 법칙으로는 reduction.tex의 상수 이동·truncation·안정성으로 넘어간다(main:theorem.s1–s3). (3) 결론은 모든 $N$ 에 대한 liminf다: 증명은 깊이마다의 [[g:selected-sequence|선택된 수열]]을 거치지만 비교 기준 $\underline F$ 가 모든 크기의 liminf이기 때문이다. (4) inf의 달성이나 최적 order parameter는 주장하지 않는다. 증명에 쓰인 시행 법칙 $\zeta_{L,N}$ 은 inf에 대한 상계로만 쓰인다.
abstraction: exact
children: [comp:bounded-lower.s1, comp:bounded-lower.s2]
source:
  - {file: comparison.tex, lines: [225, 231]}
  - {file: comparison.tex, lines: [233, 246]}
status: proposed
---

**증명의 뼈대.** [[comp:bounded-lower.s1]]: $A=\inf_{r\ge0}\Phi_r$ 는 유한하고, 부호화된 시행값 $\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$ 은 $A$ 이상이다. (8.1)과 합쳐 각 고정 $L$ 에서 $A\le\underline F+2\varepsilon+\limsup_N\lvert\Delta_N-\mathcal B_{L-1}\rvert$ (안쪽은 그 깊이의 선택된 수열). [[comp:bounded-lower.s2]]: comp:insertion-comparison으로 $L\to\infty$, 그다음 $\varepsilon\downarrow0$.

**하한 조립의 극한 순서 (바깥에서 안쪽).** $\varepsilon\downarrow0$ ← $L\to\infty$ ← 고정 $(L,\varepsilon)$ 의 선택된 수열 위 $\limsup_N$. $\eta\downarrow0$, $M$, $q$ 는 이 조립에 나오지 않는다: 그것들은 comp:shape-error와 comp:insertion-comparison 안에서 이미 소진되어 $\lim_L\limsup_N\lvert\Delta_N-\mathcal B_{L-1}\rvert=0$ 이라는 $\eta$, $M$, $q$ 없는 진술로 들어온다. $\underline F$ 는 수열, $L$, $\varepsilon$ 과 무관한 고정 수다([[x:comp-standing]]).

**순환을 피하는 연결.** 진술의 "with the functionals defined in \cref{model:section}"(227)은 섹션 전체를 가리키지만, 이 카드는 [[model:functional]]과 [[x:model-depth-zero]](그리고 사슬 [[model:chain]])만 `uses`에 넣는다. [[model:section]]은 주정리를 자식으로 갖고 그 증명이 이 카드를 받으므로, 섹션을 넣으면 `uses` 순환이 생긴다. 기계 의존 검사는 227행의 `\cref{model:section}`을 이 연결로 해소하지 못하고 경고를 낸다(보고 대상).
