---
id: decor:projection-bound
kind: lemma
title: '첫 갈라짐에서 자식을 평균으로 바꾸는 오차'
uses: [decor:projection-definition, decor:contractions, x:decor-tree-sampling, x:decor-spin-product, x:decor-eta-regular]
provides: 'conditional-concentration.s4.s1 (target 측 사영, S^+와 e+1), s7.s1과 s7.s2 (옛 측 사영), overlap-concentration.s3 (B=1)'
math: |
  decor:projection-definition의 상황에서, $B\in[-1,1]^N$가 $\mathscr F_e$가 주어지면 $S$의 깊이 $e$ 아래 continuation과 조건부 독립인 확률 벡터이면
  $$\|(A_S-a_{S,e})\cdot B\|_{L^2}\le p_N(S,e).$$
  특히 $B=\mathbf1$일 때, 그리고 $B$가 $e$ 이전에 갈라진 다른 측에서 뽑은 $[-1,1]^N$ 벡터일 때 성립한다. 두 측 I, II가 각각 같은 모양 $S$의 사본이고, 깊이 배정이 aligned이며(대응하는 vertex가 깊이 좌표 하나를 공유, x:decor-eta-regular) $e$ 이전(예: 깊이 $d<e$)에서 갈라졌으면, $\|A_S^{\rm I}\cdot A_S^{\rm II}-a^{\rm I}_{S,e}\cdot a^{\rm II}_{S,e}\|_{L^2}\le2p_N(S,e)$. 마지막으로 $|f|\le1$인 임의의 스칼라 $f$ (오차와 상관이 있어도 됨)에 대해 $\mathbb E|f\,Z|\le\|Z\|_{L^2}$이므로, 위 오차에 $f$를 곱해도 $L^1$ 상계는 커지지 않는다.
physics: |
  첫 갈라짐 깊이 $e$의 [[g:state|상태]] 안에서 각 가지의 [[g:conditional-covariance|조건부 공분산]] 제곱 평균(자식의 $v_N$)이 작으면, [[g:multioverlap|overlap]]을 계산할 때 각 가지 $T_j$의 [[g:replica|replica]]들 spin 곱을 그 상태 평균으로 바꿔도 된다([[g:projection]]; $T_j$가 replica 하나뿐이면 이것은 국소 자화이고, 그때 $a_{S,e}$는 국소 자화의 곱이다). cavity 계산에서 "한 물리적 pure state 안에서는 spin을 평균장으로 대체"하는 단계에 해당하고, 여기서는 [[g:hierarchy|보조 계층]] prefix가 물리적 pure state 자리에 있다.
gap: |
  math는 대체 오차를 $\sum_jv_N(T_j,e)^{1/4}$로 정량적으로 준다. 그것도 $e$ 아래 continuation과 조건부 독립인 벡터와의 축약에 대해서만이다. 각 가지의 $v_N$ 이 실제로 작은지는 이 lemma가 말하지 않고 decor:conditional-concentration([[g:conditional-decorrelation]])이 [[g:depth-average|깊이 평균]]의 의미로 따로 준다. "상태"는 perturbed [[g:reservoir|reservoir]]의 보조 계층 prefix $\mathscr F_e$([[g:root]] 포함)이며 [[g:physical-pure-state|물리적 pure state]]가 아니다. 일반적인 $T_j$에서 상태 평균은 단일 spin의 자화가 아니라 $T_j$의 여러 replica spin 곱의 조건부 평균이다.
abstraction: approximation
children: []
source:
  - {file: decorrelation.tex, lines: [216, 230]}
status: proposed
---

**근거.** $A_S=\prod_jA_{T_j}$ (좌표별)이므로 자식을 하나씩 평균으로 바꾸는 망원 합
$$A_S-a_{S,e}=\sum_{r=1}^s\Bigl(\prod_{j<r}\mu_{e,T_j}\Bigr)(A_{T_r}-\mu_{e,T_r})\Bigl(\prod_{j>r}A_{T_j}\Bigr)$$
을 쓴다. $r$번째 항을 $B$와 축약하면 $(A_{T_r}-\mu_{e,T_r})\cdot B_r$ 꼴이다. 여기서 $B_r=B\prod_{j<r}\mu_{e,T_j}\prod_{j>r}A_{T_j}\in[-1,1]^N$는 $\mathscr F_e$가 주어지면 $T_r$의 continuation과 조건부 독립이다([[x:decor-tree-sampling]]). [[decor:contractions]]의 [[g:three-copy|축약 부등식]]으로 각 항은 $v_N(T_r,e)^{1/4}$ 이하이고, 삼각부등식으로 합하면 된다. 두 측의 경우: 먼저 $B=A_S^{\rm II}$로 측 I을 사영하고, 다음에 $B=a^{\rm I}_{S,e}$로 측 II를 사영한다. 두 측의 $p_N$은 aligned depth 때문에 같은 값이다($p_N$은 기대값이므로 모양과 [[g:topology|깊이 배정]]에만 의존한다). 그래서 합이 $2p_N(S,e)$이다 (tex 226–228; 문맥의 두 측은 aligned 사본이다, tex 26–28, 295–296). 깊이 배정이 다르면 같은 논법은 $p_N^{\rm I}+p_N^{\rm II}$만 준다(작성자 유도). 그래서 aligned 조건을 `math`에 넣었다.
