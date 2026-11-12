---
id: cavity:section
kind: section
title: '§5 섭동된 cavity reservoir'
uses: [model:hamiltonian, model:integrability, x:tree-path-kernels, x:tree-sampling, tree:original-tilt, tree:Y-recursion, tree:insertion, x:tree-extra-variables]
provides: '§6 perturbations (cavity:increment의 reservoir와 균일 유계성, cavity:negligible, cavity:factor-bounds·x:cavity-root-convention의 섭동 틀, cavity:grid, x:cavity-bounded, x:cavity-tree-sampling), §7 decorrelation (cavity:grid → x:decor-mesh, x:cavity-tree-sampling → x:decor-tree-sampling), §8 comparison (cavity:increment, cavity:identity, $A_{\rm s}$, $A_{\rm b}$, x:cavity-tree-sampling), §9 reduction (x:cavity-bounded가 거기서 풀린다). overview.tex 18'
math: |
  받는 것 (§2, §3). 모형 model:hamiltonian과 $B(\theta)$ (model:integrability), 그리고 §3의 틀: path kernel과 지수열 (x:tree-path-kernels), 분배함수에서 만든 tilted kernel과 backward recursion (tree:original-tilt), insertion recursion $Y_d$ (tree:Y-recursion), insertion 항등식과 단조·동차성 (tree:insertion), 새 root 변수의 약속 (x:tree-extra-variables), tree 표본 규칙 (x:tree-sampling). (2.3), (2.4)는 쓰지 않는다.

  가정 (x:cavity-bounded). reduction:section까지 $B(\theta)\le B$, $\lvert h\rvert\le H$ a.s., $\theta$ 의 법칙은 좌표 순열에 불변.

  내놓는 것. 고정 $L\ge2$, $m_d=d/L$ (cavity:grid)에서 평균 $c_\nu N^{3/4}$ 의 섭동 factor $1/2\le\psi_\nu\le3/2$ (cavity:factor-bounds; 개수·type·site는 root, $\mathbf u$ 는 고정, x:cavity-root-convention)를 더한 기대 root logarithm $P_N^{L,\mathbf u}$ (x:cavity-root-logarithm)에 대해
  $$\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)s_N\qquad\text{(cavity:negligible)},$$
  $$\Delta_N^{L,\mathbf u}=\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}+o_N(1),\quad\sup_{N,L,\mathbf u}\lvert\Delta_N^{L,\mathbf u}\rvert<\infty\qquad\text{(cavity:increment)}.$$
  그리고 이후 모든 spin tree를 이 reservoir에서 뽑는다는 약속 (x:cavity-tree-sampling).
physics: |
  Aizenman–Sims–Starr식 cavity 비교의 준비다: 크기 $N$ 과 $N+1$ 의 계를 공통 $N$-spin [[g:reservoir|reservoir]]로 비교해, [[g:increment|증분]]을 site 삽입과 bond 삽입([[g:site-bond-insertion]])의 차로 쓴다. 이 비교를 [[g:grid|균등 격자]]의 [[g:hierarchy|보조 계층]] 위에서 하려고 sublinear한 수의 유계 [[g:perturbation|섭동]] factor를 넣는다. 섭동은 [[g:root-logarithm|root logarithm]]의 밀도를 $o(1)$ 만 옮기고 증분 식을 보존한다.
gap: |
  (1) 원문은 이 비교가 Aizenman–Sims–Starr 변분 틀과 Panchenko의 spin 분포 꼴을 "따른다"고만 적고(cavity.tex 4–6), 그 결과를 증명에 쓰지 않는다. (2) 대상은 [[g:bounded-law|유계]]이고 [[g:permutation-invariance|순열 불변]]인 상호작용이다(x:cavity-bounded). (3) $P_N^{L,\mathbf u}$ 와 $\log Y_0$ 는 보조 변수를 tilt해 적분한 양이라 $L\ge2$ 에서 보통 뜻의 pressure와 그 변화가 아니다. (4) reservoir의 평균 상호작용 수는 $\rho_N\ne\alpha N$. (5) 물리의 $\lim F_N=\lim\Delta_N$ 은 주장하지 않는다. (6) 섭동 매개변수 $\mathbf u$ 는 고정값이고 평균하지 않는다. 보조 계층을 [[g:physical-pure-state|물리적 pure state]] 계층으로 읽는 것은 증명되지 않는다.
abstraction: approximation
children: [x:cavity-bounded, cavity:grid, cavity:factor-bounds, x:cavity-root-convention, x:cavity-root-logarithm, cavity:negligible, cavity:increment, x:cavity-tree-sampling]
source:
  - {file: cavity.tex, lines: [1, 121]}
status: proposed
---

**뼈대.** 가정 [[x:cavity-bounded]] → 격자 [[cavity:grid]] → 섭동 틀 [[cavity:factor-bounds]], [[x:cavity-root-convention]] → [[x:cavity-root-logarithm]] → [[cavity:negligible]] → 증분 lemma [[cavity:increment]] (단계 [[cavity:increment.s1]] Poisson 분해, [[cavity:increment.s2]] 섭동 맞춤과 항별 비용, [[cavity:increment.s3]] 증분 항등식, [[cavity:increment.s4]] 균일 유계) → 이후의 표본 약속 [[x:cavity-tree-sampling]].

**밖에서 받는 것.** 이 절은 다른 라벨을 `\ref`로 가리키지 않는다(11행 `reduction:section`, 32행 `pert:section`은 원문상 뒤의 대상을 가리키는 예고). 실제로 쓰는 것은 모두 `\ref` 없이 쓴다.

| 받는 것 | 카드 | 원문 위치 |
|---|---|---|
| 모형, $B(\theta)$, Poisson 상호작용 과정 | [[model:hamiltonian]], [[model:integrability]] | cavity.tex 11, 72–85 |
| 계층 틀, $L=r+1$ | [[x:tree-path-kernels]] | 16–19 |
| power-mean recursion, tilted kernel | [[tree:original-tilt]] | 34–37, 55–56, 117–118 |
| insertion recursion $Y_0$ | [[tree:Y-recursion]] | 53–57 |
| insertion 항등식, 단조·동차성($\lvert\log Y_0\rvert$ 상계) | [[tree:insertion]] | 105–111 |
| 새 root disorder, 안 쓰는 보조 변수 | [[x:tree-extra-variables]] | 56, 96–98 |
| tree 표본 규칙 | [[x:tree-sampling]] | 117–118 |

**밖에 내주는 것** (원문의 실제 참조).

| 받는 곳 | 쓰는 것 | 원문 위치 |
|---|---|---|
| pert:section 서두 | [[cavity:increment]]의 reservoir (같은 논증이 적용) | perturbations.tex 6 (`\cref`) |
| 섭동 정의 | [[cavity:negligible]] (항별 비교의 본보기), [[cavity:factor-bounds]], [[x:cavity-root-convention]] (같은 약속을 다시 적음) | perturbations.tex 52–67 (65 `\eqref`) |
| pert:selection 증명 | [[cavity:negligible]], [[cavity:increment]] (균일 유계) | perturbations.tex 271, 277 |
| §7 | [[cavity:grid]] (x:decor-mesh), [[x:cavity-tree-sampling]] | decorrelation.tex 4 (`\ref` 없음) |
| comp:encoding | reservoir root disorder, tilted reservoir kernel ([[x:cavity-tree-sampling]]) | comparison.tex 20–29 (`\ref` 없음) |
| comp:insertion-comparison 증명 | [[cavity:increment]] ($A_{\rm s}$, $A_{\rm b}$), (5.5) | comparison.tex 171, 195, 222 |
| reduction / main:theorem | [[x:cavity-bounded]]를 푸는 쪽 | reduction.tex 45–87 |

**인터페이스 점검.** [[tree:section]]의 export 표(§5: [[tree:insertion]], $\lvert\log Y_0\rvert$ 상계, [[x:tree-extra-variables]], 표본 규칙)는 이 카드들이 쓰는 것과 맞는다. 다만 그 표에는 [[tree:original-tilt]]("tilted reservoir kernels", 34행의 recursion)와 [[tree:Y-recursion]]이 빠져 있다(provides 칸에는 tree:Y-recursion이 있다). §2에서는 `\ref` 없이 [[model:hamiltonian]], [[model:integrability]]만 받는다. (2.3), (2.4)를 쓰지 않는다는 원문의 말(13–14)과 맞다.

**섭동 매개변수.** 원문 29–31: $\mathbf u$ 는 "fixed, not quenched random variables, unless a parameter average is explicitly taken". 이 절의 모든 균일성("uniform in $L,\mathbf u$")은 고정된 $\mathbf u$ 각각에서의 한계가 $\mathbf u$ 에 무관하다는 뜻이다.
