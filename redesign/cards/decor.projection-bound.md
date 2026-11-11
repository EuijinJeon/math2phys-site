---
id: decor:projection-bound
kind: lemma
title: '첫 갈라짐에서 자식을 평균으로 바꾸는 오차'
uses: [decor:projection-definition, decor:contractions, x:decor-tree-sampling, x:decor-spin-product]
provides: 'conditional-concentration.s4.s1 (target 측 사영, S^+와 e+1), s7.s1과 s7.s2 (옛 측 사영), overlap-concentration.s3 (B=1)'
math: |
  decor:projection-definition의 상황에서, $B\in[-1,1]^N$가 $\mathscr F_e$가 주어지면 $S$의 깊이 $e$ 아래 continuation과 조건부 독립인 확률 벡터이면
  $$\|(A_S-a_{S,e})\cdot B\|_{L^2}\le p_N(S,e).$$
  특히 $B=\mathbf1$일 때, 그리고 $B$가 $e$ 이전에 갈라진 다른 측에서 뽑은 $[-1,1]^N$ 벡터일 때 성립한다. 두 측 I, II가 각각 같은 모양 $S$의 사본이고 $e$ 이전(예: 깊이 $d<e$)에서 갈라졌으면, $\|A_S^{\rm I}\cdot A_S^{\rm II}-a^{\rm I}_{S,e}\cdot a^{\rm II}_{S,e}\|_{L^2}\le2p_N(S,e)$. 마지막으로 $|f|\le1$인 임의의 스칼라 $f$ (오차와 상관이 있어도 됨)에 대해 $\mathbb E|f\,Z|\le\|Z\|_{L^2}$이므로, 위 오차에 $f$를 곱해도 $L^1$ 상계는 커지지 않는다.
physics: |
  첫 갈라짐 깊이 $e$의 상태 안에서 각 가지가 clustering하면(자식의 $v_N$이 작으면), overlap을 계산할 때 각 가지의 spin 곱을 그 상태의 평균(국소 자화의 곱)으로 바꿔도 된다. cavity 계산에서 "상태 안에서는 평균장으로 대체"하는 단계다.
gap: |
  math는 대체 오차를 $\sum_jv_N(T_j,e)^{1/4}$로 정량적으로 준다. 그것도 $e$ 아래 continuation과 조건부 독립인 벡터와의 축약에 대해서만이다. 각 가지가 실제로 clustering하는지는 이 lemma가 말하지 않고 decor:conditional-concentration이 깊이 평균의 의미로 따로 준다.
abstraction: approximation
children: []
source:
  - {file: decorrelation.tex, lines: [216, 230]}
status: proposed
---

**근거.** $A_S=\prod_jA_{T_j}$ (좌표별)이므로 자식을 하나씩 평균으로 바꾸는 망원 합
$$A_S-a_{S,e}=\sum_{r=1}^s\Bigl(\prod_{j<r}\mu_{e,T_j}\Bigr)(A_{T_r}-\mu_{e,T_r})\Bigl(\prod_{j>r}A_{T_j}\Bigr)$$
을 쓴다. $r$번째 항을 $B$와 축약하면 $(A_{T_r}-\mu_{e,T_r})\cdot B_r$ 꼴이다. 여기서 $B_r=B\prod_{j<r}\mu_{e,T_j}\prod_{j>r}A_{T_j}\in[-1,1]^N$는 $\mathscr F_e$가 주어지면 $T_r$의 continuation과 조건부 독립이다([[x:decor-tree-sampling]]). [[decor:contractions]]의 축약 부등식으로 각 항은 $v_N(T_r,e)^{1/4}$ 이하이고, 삼각부등식으로 합하면 된다. 두 측의 경우: 먼저 $B=A_S^{\rm II}$로 측 I을 사영하고, 다음에 $B=a^{\rm I}_{S,e}$로 측 II를 사영한다. 두 측의 $p_N$은 aligned depth 때문에 같은 법칙을 가지므로 같은 값이다.
