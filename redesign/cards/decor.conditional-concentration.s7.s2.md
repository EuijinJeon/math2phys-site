---
id: decor:conditional-concentration.s7.s2
kind: step
title: '$v_N(S,d)$의 귀납 추정'
uses: [decor:conditional-concentration.s7.s1, decor:conditional-concentration.s6, decor:contractions, decor:projection-bound, decor:projection-definition]
provides: 'decor:conditional-concentration.s7.s4'
math: |
  $$v_N(S,d)\le C_{k,\eta}\bigl(\delta+p_N(S,e)+p_N(S^+,e+1)+h_N(S)\bigr)+C_{L,k,\eta}\,\varepsilon_{N,L,k}.$$
  근거: $A_S$의 세 사본을 $d$ 아래에서 조건부 독립으로 뽑으면 decor:contractions (b)로 $\mathbb E(X\cdot Y-X\cdot Z)^2\ge2v_N(S,d)$. 첫 사본이 들어간 두 축약을 사영하면 각각 $L^2$에서 $2p_N(S,e)$ 이하로 바뀌어 $a\cdot b-a\cdot b_d$가 된다. s7.s1, s6의 $\rho_N$ 상계, $p_N(S,e)\le k$를 쓴다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [480, 490]}
status: proposed
---

세 사본의 사영 벡터 $(a,b,b_d)$는 $d$에서 서로 갈라진 세 stem 위의 $a_{S,e}$이므로 s5에서 쓴 $(a,b,b_d)$와 같은 결합 법칙을 갖는다. $p_N^2\le kp_N$이므로 사영 오차의 제곱도 $p_N$ 선형으로 쓸 수 있다. 결과적으로 $S$의 공분산이 잎이 더 적은 자식들의 공분산($p_N$ 안)과 $L\to\infty$에서 작은 항으로 눌린다.
