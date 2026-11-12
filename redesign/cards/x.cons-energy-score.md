---
id: x:cons-energy-score
kind: definition
title: '$\beta$ 를 뗀 에너지 점수 $\mathcal E_N$ 과 $\mathcal B_{r,\beta}$'
uses: [x:cons-standard-examples, model:hamiltonian, models:spin, models:sat, model:functional, x:model-depth-zero]
provides: 'models:ground ($\mathcal E_N$, $Z_N(\beta)$, $\mathcal B_{r,\beta}$), g:ground-state의 기호'
math: |
  spin 모형에서는
  $$\mathcal E_N(\sigma)=\sum_{k=1}^{M_N}J_k\prod_{\ell=1}^p\sigma_{i_{\ell,k}}+\sum_{i=1}^NH_i\sigma_i,$$
  satisfiability 모형에서는
  $$\mathcal E_N(\sigma)=-\sum_{k=1}^{M_N}W_k\prod_{\ell=1}^K\frac{1+\varepsilon_{\ell,k}\sigma_{i_{\ell,k}}}{2}$$
  로 둔다(unscaled energy score). 이 점수와 그 disorder 법칙은 $\beta$ 에 의존하지 않고, 두 경우 모두 분배함수는 $Z_N(\beta)=\sum_\sigma e^{\beta\mathcal E_N(\sigma)}$ 이다. $\mathcal B_{r,\beta}$ 는 역온도 $\beta$ 에서 해당 법칙에 대한 functional (2.11)이다.
physics: |
  $\mathcal E_N$ 은 역온도를 뗀 에너지의 부호를 바꾼 것이다: $-H_N=\beta\mathcal E_N$. spin 모형에서는 coupling과 장의 에너지 이득, SAT에서는 위반된 clause 가중치 합의 음수다. [[g:disorder|disorder]]($M_N$, site, $J_k$, $H_i$, $W_k$, $\varepsilon_{\ell,k}$)는 온도와 무관하게 한 번 뽑고 $\beta$ 만 바꾼다. $\mathcal B_{r,\beta}$ 는 역온도 $\beta$ 의 시행 [[g:functional|functional]]이다.
gap: |
  정확하다. $-H_N=\beta\mathcal E_N$ 은 (2.2)에 $\theta_\beta$, $h_\beta$ 를 넣으면 나온다(작성자 확인; 원문은 $Z_N(\beta)$ 의 꼴만 적는다). $\mathcal B_{r,\beta}$ 에서 $r=0$ 은 x:model-depth-zero의 $\mathcal B_0$ 이다(작성자 읽기: models:ground의 $\inf_{r\ge0}$).
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [66, 84]}
status: proposed
---

$M_N$, $i_{\ell,k}$ 는 (2.2)의 Poisson 개수와 복원추출 index이고([[x:cons-standard-examples]]), $J_k$, $H_i$, $W_k$, $\varepsilon_{\ell,k}$ 는 [[models:spin]], [[models:sat]]의 법칙에서 뽑은 독립 사본이다. 원문은 이것을 기호로만 쓴다. 83행의 `\eqref{model:functional}` 이 이 카드의 유일한 `\ref` 다.
