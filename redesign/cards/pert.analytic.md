---
id: pert:analytic
kind: lemma
title: 'insertion 계수의 소멸 (Lemma 6.4)'
uses: [pert:analytic-difference, pert:palm, pert:parameters, pert:selection, x:pert-selected-limits, x:pert-mark-specification, tree:extension-expansion, tree:multioverlap]
provides: 'pert:tree-identity.s1, s4 (k=0의 상수 계수, polarization의 각 항). 규칙 P7, L1 수 4'
math: |
  섭동 족에 포함된 모든 mark specification, old tree, anchor, 유계 overlap 다항식 시험 $f$ 에 대해, $H_N(t,0)$ 의 $t=0$ 에서의 모든 Taylor 계수가 선택된 수열을 따라 0으로 간다.
physics: null
gap: null
abstraction: blackbox
children: [pert:analytic.s1, pert:analytic.s2, pert:analytic.s3]
source:
  - {file: perturbations.tex, lines: [383, 388]}
  - {file: perturbations.tex, lines: [390, 425]}
status: proposed
---

**증명의 뼈대.**
- [[pert:analytic.s1]]: [[tree:extension-expansion]]의 해석적 경계로 $J$, $H_N$ 이 $|t|,|u|<\rho$ 에서 해석적이고 $N$ 과 선택된 벡터에 균등하게 유계, $u$-도함수도 균등 유계. 상수는 type 첨자 $j$ 에 무관.
- [[pert:analytic.s2]]: $H_N(t,0)$ 의 각 Taylor 계수는 prescribed tree 위 multioverlap moment(와 그 둘의 곱)의 $N$ 무관 계수 유한 일차결합이라 pert:selection (iii)으로 수렴하고, 해석적 경계로 $H_N(t,0)\to H(t)$ 가 작은 원판에서 균등.
- [[pert:analytic.s3]]: 각 큰 고정 $j$ 에서 Palm 경계와 $|u_\nu|\le2j^{-j}$ 로 $|H(1/j)|\le2Cj^{-j}$. $H$ 의 첫 0 아닌 계수의 차수가 $q$ 면 $|H(1/j)|\ge cj^{-q}$ 이라 모순, 따라서 $H\equiv0$.

**극한 순서.** 각 $j$ 를 고정하고 $N\to\infty$ 한 뒤 $j\to\infty$ 다(s3, [[x:pert-order-of-choices]]). type에 균등한 score 집중은 쓰지 않는다: 쓰는 것은 각 고정 $\nu$ 의 $e_{\nu,N}\to0$ 과, 같은 함수 $H_N$ 이 모든 $j$ 에 쓰인다는 [[pert:palm]]의 둘째 주장이다.

물리 대응은 두지 않았다([[g:palm-identity]]). 이것은 해석함수의 유일성 논법이다: $t$ 의 모든 거듭제곱보다 빨리 작아지는 값을 점열 $t=1/j\to0$ 에서 갖는 해석함수는 0이다.
