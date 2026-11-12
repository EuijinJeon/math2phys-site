---
id: pert:tree-identity.s1
kind: step
title: '$k=0$ 과 polarization: 혼합 도함수를 같은 방향 계수로'
uses: [pert:analytic, pert:analytic-difference, x:pert-mark-specification, tree:extension-expansion]
provides: 'pert:tree-identity.s4 (혼합 도함수 → 0), s3 (polarization 평균이 족 안에 있어야 함)'
math: |
  $k=0$ 이면 주장은 상수 mark를 쓴 pert:analytic의 상수 계수 소멸이다. $k\ge1$ 이면 서로 다른 colored mark를 뽑는 법을 설명한다. 모두 1 이하로 유계이고 같은 유한 개 보조 mark 모임에서 함께 만든 유리수값 함수 $g_0,g_1,\ldots,g_k$ 를 고정한다. 혼합 insertion은 $A=1+\sum_{j=1}^kz_jg_j\sigma_i$ 를 쓴다. 모든 $z_j$ 에 대한 그 혼합 도함수는 단일 $g$ 에 대한 $k$ 차 계수를 polarization해서 얻는 대칭 다중선형 형식이다. 구체적으로 $Q_N(g)=k![t^k]H_N(t,0)$ 이면 혼합 도함수는
  $$\frac{k^k}{2^kk!}\sum_{\epsilon\in\{-1,1\}^k}\left(\prod_{j=1}^k\epsilon_j\right)Q_N\left(k^{-1}\sum_{j=1}^k\epsilon_jg_j\right)$$
  이다. $Q_N$ 의 모든 인자는 유리수값이고 1 이하로 유계이므로, 그 결과 각 쌍 $(g,g_0)$ 은 고정된 mark 족에 든다. pert:analytic이 위의 혼합 도함수를 0으로 보낸다. 혼합 도함수의 전개는 정확히 순서 붙은 확장 규칙이다: 그 계수에 추가 factorial은 없다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [472, 492]}
status: proposed
---

풀이(작성자). $Q_N(g)$ 는 $g$ 에 대해 $k$ 차 동차이므로 $Q_N(g)=F(g,\ldots,g)$ 인 대칭 다중선형 $F$ 가 있고 표준 polarization 공식 $F(g_1,\ldots,g_k)=\frac1{2^kk!}\sum_\epsilon(\prod_j\epsilon_j)Q_N(\sum_j\epsilon_jg_j)$ 에 $k^{-1}$ 배의 동차성 $Q_N(k^{-1}h)=k^{-k}Q_N(h)$ 를 넣은 것이 위 식이다. 인자를 $k^{-1}$ 로 줄이는 것은 값이 $[-1,1]$ 에 머물게 해서 [[x:pert-mark-specification]]의 족 안에 두기 위해서다. "혼합 도함수"는 $u=0$, $z=0$ 에서 $H_N$ 의 혼합 판(같은 $g_0$, $S_0$)의 것으로 읽었다. "추가 factorial이 없다"는 [[tree:extension-expansion]]의 "같은 방향이면 $t^k$ 계수는 우변을 $k!$ 로 나눈 것"과 짝이다: $Q_N$ 에 $k!$ 을 곱해 두었으므로 혼합 도함수의 history 합에 그대로 맞는다. 각 $Q_N(\cdot)$ 이 0으로 가는 것은 그 인자로 만든 specification마다 [[pert:analytic]]을 쓴 것이고, 합은 유한($2^k$ 항)이다.
