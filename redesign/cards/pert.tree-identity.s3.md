---
id: pert:tree-identity.s3
kind: step
title: '정확한 split 깊이 $H_d-H_{d+1}$ 과 모양의 선택'
uses: [pert:tree-identity.s2, pert:tree-identity.s1, x:pert-mark-specification, x:tree-sampling]
provides: 'pert:tree-identity.s4'
math: |
  $H_d(a,b)$ 를 (6.18)의 공유 지시함수라 하고, 서로 다른 replica 위치에 대해 $H_0=1$, $H_L=0$ 으로 둔다. 이것은 sampled tree 안의 위치이며, 그 spin 배치가 우연히 같아도 그렇다. 깊이 $d$ 에서의 정확한 갈라짐은 $0\le d\le L-1$ 에 대해 $H_d-H_{d+1}$ 로 표현된다. 따라서 곱과 유한 일차결합이 지정된 임의의 일관된 colored 모양이나 허용 모양의 모임을 고른다. 이 유한 일차결합의 각 항에서 함수 $g_0,\ldots,g_k$ 는 부호의 곱이므로 값이 $\{-1,1\}$ 에 있다. 이 함수들과 그 polarization 평균은 절의 처음에 고정한 mark 족에 든다. 상수 mark가 $k=0$ 을 덮는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [514, 524]}
status: proposed
---

풀이(작성자). $H_0=1$ 은 모든 path가 root를 공유하기 때문이고, $H_L=0$ 은 서로 다른 leaf 위치는 깊이 $L$ vertex를 공유하지 않기 때문이다(값이 같아도 위치는 다르다, [[x:tree-sampling]]). 그래서 $H_d$ 는 깊이 $1,\ldots,L-1$ 의 selector로만 실현하면 된다. 일차결합 $\prod(H_{d}-H_{d+1})$ 을 전개하면 각 항이 selector 곱이고, 각 항마다 다른 mark specification이 쓰인다. 각 항에 [[pert:tree-identity.s1]]의 polarization을 적용해야 하므로 polarization 평균이 족 안에 있다는 확인이 필요하다.
