---
id: pert:tree-identity.s2
kind: step
title: 'mark selector (6.18)'
uses: [x:pert-mark-specification, x:pert-colored-extensions, x:tree-sampling]
provides: 'pert:tree-identity.s3 (H_d), s4 (mark 평균). g:mark의 정의 위치'
math: |
  mark에 대한 기대값이 $\mathcal C$ 를 만족하는 확장만 정확히 고르게 하는 일이 남았다. color 쌍 $a,b\in\{0,\ldots,k\}$ 와 깊이 $1\le d\le L-1$ 에 대해, 그 split 깊이가 $d$ 이상이라는 사건은 두 color가 깊이 $d$ 의 vertex를 공유한다는 사건이다. 그 깊이에 새 독립 Rademacher 좌표를 도입하고 $g_a$ 와 $g_b$ 모두에 그 인자를 준다. 그것이 둘의 결합 mark 기대값에 주는 기여는 vertex가 공유되면 $1$, 아니면 $0$ 이다. 이런 요구의 유한 모임에 대해서는 서로 다른 요구에 서로 다른 독립 좌표를 쓰고 각 $g_a$ 를 그에게 배정된 인자들의 곱으로 정의한다. 그러면
  $$\mathbb E_{\rm marks}\left[g_0^{a_*}\prod_{j=1}^kg_j^{a_j(E)}\right]=\prod_{(a,b,d)\ {\rm required}}\mathbf1_{\{a,b\text{ share their depth-}d\text{ vertex}\}}.$$
  이 계산의 모든 mark는 base reservoir와 독립이다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [494, 512]}
status: proposed
---

풀이(작성자). 좌표 $\xi$ 는 path가 깊이 $d$ 에서 지나는 vertex마다 독립인 값을 가진다([[x:pert-mark-specification]]). $a$, $b$ 가 같은 vertex를 지나면 $\xi^a\xi^b=\xi^2=1$, 다른 vertex면 독립 평균 0인 두 값의 곱이라 기대값 0이다. 좌표마다 정확히 두 color에 배정되므로 기대값이 요구별로 곱해진다. "split 깊이 $\ge d$ $\Leftrightarrow$ 깊이 $d$ vertex 공유"는 [[x:tree-sampling]]의 split 정의(마지막 공통 vertex의 깊이)에서 온다. mark가 base reservoir와 독립이라는 것은 [[pert:palm-expression]]의 "independent insertion variables with their prior kernels"이고, 기대값이 $t=0$ 의 전개 계수에서 계산되므로 tilt의 영향이 없다.
