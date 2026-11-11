---
id: x:tree-cancellation-example
kind: remark
title: '두 path 예: 부호 있는 합 $-\delta$ 대 절댓값 합 $2+\delta$'
uses: [x:tree-extension-history, x:tree-reference-paths]
provides: 'tree:reference-total과 tree:charging이 일반화하는 두 계산. §7 decor:conditional-concentration.s2.s1이 같은 구성을 쓴다. rules.md의 "−δ 대 2+δ"'
math: |
  깊이 $d$에서 갈라지는 old path 두 개로 시작하고 첫째를 anchor로 둔다. added color 하나가 anchor와 정확히 깊이 $d$에서 갈라지도록 요구한다. 그 color는 둘째 old leaf를 쓰거나, 깊이 $d$ vertex에서 fresh path를 만들거나, 둘째 old path를 따라가다 깊이 $\ell>d$에서 떠날 수 있다. 각각의 계수를 더하면
  $$1+(m_d-2m_{d+1})+\sum_{\ell=d+1}^{L-1}(m_\ell-m_{\ell+1})=m_d-m_{d+1}.$$
  균등 격자 $m_d=d/L$, $\delta=L^{-1}$에서 이 부호 있는 합은 $-\delta$이지만 절댓값 계수의 합은 $2+\delta$다. 요구한 split을 $d+1<L$로 미루면 허용되는 선택은 anchor path 위 unary인 깊이 $(d+1)$ vertex에서의 fresh split 하나뿐이다. 그 계수는 $-\delta$이므로 절댓값 합은 이제 $\delta$다. 다음 두 lemma가 이 두 계산을 넓힌다: 첫째는 부호 있는 합을 계산하고, 둘째는 지정된 split이 old branching 깊이에서 떨어져 일어날 때 절댓값 합을 제어한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [317, 335]}
status: proposed
---

검산(작성자): 망원 합 $\sum_{\ell=d+1}^{L-1}(m_\ell-m_{\ell+1})=m_{d+1}-m_L=m_{d+1}-1$이므로 총합은 $1+m_d-2m_{d+1}+m_{d+1}-1=m_d-m_{d+1}$. 절댓값: $1+(d+2)\delta+(L-1-d)\delta=1+(L+1)\delta=2+\delta$. 미룬 경우 둘째 old path는 anchor와 깊이 $d$에서 이미 갈라졌으므로 쓸 수 없고, 깊이 $d+1$의 anchor 쪽 vertex는 anchor만 지나는 unary vertex다.

이 예가 [[g:depth-delay|깊이 미루기]]의 동기다: 부호 있는 합은 작은데($-\delta$) 절댓값 합은 $O(1)$이라, 작은 정규화로 나누면 오차가 커진다. split을 old branching 깊이가 아닌 곳으로 미루면 절댓값 합도 정규화와 같은 크기가 된다.
