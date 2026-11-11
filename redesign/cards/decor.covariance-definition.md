---
id: decor:covariance-definition
kind: definition
title: '조건부 평균 $\mu_{d,S}$와 조건부 공분산 제곱 $v_N(S,d)$'
uses: [x:decor-spin-product, x:decor-topology]
provides: 'decor:contractions, decor:projection-definition, decor:conditional-concentration의 귀납량'
math: |
  $d$가 $S$의 initial stem 위의 깊이(첫 branching depth 포함)일 때, $\mathscr F_d$는 root와 그 stem의 깊이 $d$까지의 sampled prefix가 생성하는 $\sigma$-field다.
  $$\mu_{d,S}=\mathbb E[A_S\mid\mathscr F_d],\qquad v_N(S,d)=\frac1{N^2}\mathbb E\sum_{i,j=1}^N\operatorname{Cov}(A_{S,i},A_{S,j}\mid\mathscr F_d)^2.$$
  바깥 기대값은 root를 포함한다. $A_S$와 $\mu_{d,S}$의 모든 좌표는 절댓값이 1 이하이고 $0\le v_N(S,d)\le1$이다.
physics: |
  깊이 $d$의 [[g:state|상태]](prefix)가 주어졌을 때 $\mu_{d,S}$는 spin 곱의 상태 평균이고, $v_N(S,d)$는 그 상태 안 [[g:conditional-covariance|connected correlation]]의 제곱을 site 쌍에 대해 평균한 것이다. singleton이면 $\frac1{N^2}\sum_{ij}(\langle\sigma_i\sigma_j\rangle_d-\langle\sigma_i\rangle_d\langle\sigma_j\rangle_d)^2$($\langle\cdot\rangle_d$ 는 그 prefix에 대한 조건부 기대값)를 상태와 disorder에 대해 평균한 값이다.
gap: |
  "상태"는 perturbed [[g:reservoir|reservoir]]의 [[g:hierarchy|보조 계층]] prefix $\mathscr F_d$이며 root(disorder)를 포함한다. [[g:physical-pure-state|물리적 pure state]] 분해를 가정하지 않는다. $S$가 여러 leaf를 가지면 $A_S$는 깊이 $d$ 아래에서 뽑은 여러 [[g:replica|replica]]의 spin 곱이다. $i=j$ 항도 포함한다(그 기여는 $N^{-1}$ 이하).
abstraction: exact
children: []
source:
  - {file: decorrelation.tex, lines: [94, 106]}
status: proposed
---

$0\le v_N\le1$인 이유: 조건부 공분산의 절댓값은 좌표가 $[-1,1]$에 있으므로 1 이하다. 제곱 공분산을 귀납량으로 쓰는 이유는 [[decor:contractions]]의 두 부등식이 이 양을 정확히 위아래에서 잇기 때문이다.
