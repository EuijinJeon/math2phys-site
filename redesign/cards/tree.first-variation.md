---
id: tree:first-variation
kind: lemma
title: '첫 변분: $\partial_{t_j}\log Y_d$ 는 새 path 하나의 조건부 기대값'
uses: [tree:Y-recursion]
provides: 'x:tree-differentiation-rule (내부 vertex 항을 fresh path로 읽기), tree:log-expansion.s1 (1차 도함수)'
math: |
  $A_{\boldsymbol t}=1+\sum_{j=1}^kt_jD_j$이고 실수 path 함수 $D_j$가 유계일 때, $A_{\boldsymbol t}$가 균등하게 양인 실수 근방 어디서나 미분하면
  $$\partial_{t_j}\log Y_d=E^{A_{\boldsymbol t}}\left[\left.\frac{D_j}{A_{\boldsymbol t}}\right|\mathscr F_d\right].$$
  우변의 조건부 기대값은 지정된 prefix 아래로 새 path 하나를 따른다. 실제로 power mean 하나를 미분하면 $\partial_{t_j}\log Y_{d-1}=K_d^{A_{\boldsymbol t}}\partial_{t_j}\log Y_d$이고, 말단 도함수는 $D_j/A$이다.
physics: |
  [[g:insertion|insertion]] $A$의 효과 $\log Y_d$를 섭동 방향 $D_j$로 미분한 것은, 깊이 $d$ [[g:state|상태]]가 주어졌을 때 바뀐 법칙으로 새로 뽑은 [[g:replica|replica]] 하나에서 $D_j/A$의 기대값이다($D_j$는 유계 실수 path 함수, $A_{\boldsymbol t}$가 균등하게 양인 실수 $\boldsymbol t$ 근방에서). $L=1$, $d=0$이면 $\partial_t\log\langle A\rangle=\langle D\rangle/\langle A\rangle$, 곧 재가중된 Gibbs 측도에서의 1점 평균이다.
gap: |
  $A_{\boldsymbol t}$가 균등하게 양인 실수 근방에서의 진술이다. 복소 근방과 고차 도함수의 정당화는 [[x:tree-analytic-bounds]]가 한다.
abstraction: exact
children: []
source:
  - {file: trees.tex, lines: [142, 154]}
status: proposed
---

한 단계 계산(작성자): $\log Y_{d-1}=m_d^{-1}\log K_dY_d^{m_d}$이므로 $\partial\log Y_{d-1}=K_d[Y_d^{m_d}\partial\log Y_d]/K_dY_d^{m_d}=K_d[(Y_d/Y_{d-1})^{m_d}\partial\log Y_d]=K_d^{A}\partial\log Y_d$. 이것을 깊이 $L$까지 이어 붙이면 바뀐 kernel로 path 하나를 끝까지 뽑은 $D_j/A$의 조건부 기대값이 된다. 원문의 증명은 이 두 문장(151–154)이다.
