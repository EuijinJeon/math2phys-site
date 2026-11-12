# 용어집 추가 제안 — §6 perturbations

새 항목은 없다. §6 카드는 기존 항목(`g:perturbation`, `g:mark`, `g:score`, `g:concentration`, `g:selected-sequence`, `g:palm-identity`, `g:tree-identity`, `g:anchor`, `g:extension-history`, `g:root`, `g:hierarchy`, `g:root-logarithm`, `g:increment`, `g:lower-pressure`, `g:reservoir`, `g:order-of-limits` 등)만으로 링크를 건다. 물리 칸에 쓴 "path 요동 / root 요동"은 용어로 세우지 않고 매번 풀어 썼다(root가 주어졌을 때의 tilted path 요동과, root 자체의 요동).

## 기존 항목에 대한 메모 (고치지 않았음)

- `g:selected-sequence` 역할 칸: "(ii)는 Palm 항등식(`pert:palm`)의 부등식을 거쳐 [[g:tree-identity]]"라고 쓴다. Palm 부등식 $\lvert H_N(t_\nu,u_\nu)\rvert\le\lVert f\rVert_\infty e_{\nu,N}$ 자체는 모든 $N$, 모든 $\mathbf u$ 에서 성립한다(`pert:palm`, `pert:score-identity`). (ii)가 실제로 쓰이는 곳은 그 우변을 0으로 보내는 `pert:analytic` 증명(perturbations.tex 411–418, 카드 `pert:analytic.s3`)이다. "Palm 부등식의 우변을 0으로 보내 Taylor 계수 소거(`pert:analytic`)에"로 고치면 정확하다.
- `g:concentration`: score의 집중을 $e_{\nu,N}\to0$ 으로 정의한다. `pert:concentration`(Lemma 6.1)이 증명하는 것은 그 매개변수 평균 $\int e_{\nu,N}\,d\pi\to0$ 이고, 점별 $e_{\nu,N_j}(\mathbf u_j)\to0$ 은 `pert:selection` (ii)에서 비로소 나온다. 카드 `pert:concentration`의 물리 칸은 "매개변수를 평균하면 … 집중"이라고 쓰고 차이 칸 (1)에 이 구별을 적었다. 용어집 항목의 정의 위치(`pert:error`)에 "점별 수렴은 `pert:selection` (ii)"를 덧붙이면 오해가 줄어든다.
- `g:perturbation` 물리 대응 칸 "무한소 섭동장"(intuition): 인자 하나의 크기는 $O(1)$($t_\nu\le1/4$)이고 작은 것은 개수 밀도 $N^{-1/4}$ 다(카드 `pert:factor`). 지금 문장도 "여기서는 개수 $N^{3/4}$, 값 $(1/2,3/2)$ 의 구체적인 factor"라고 덧붙여 틀리지는 않는다.
- `g:mark` 정의 위치의 `pert:mark-selector`는 증명 안의 식 라벨이다. 그 식을 담은 카드는 `pert:tree-identity.s2`다.
