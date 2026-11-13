---
id: reduction:stability
kind: lemma
title: 'Stability ($L^1$ 안정성과 상수 이동)'
uses: [model:integrability, model:hamiltonian, model:chain, model:site-message, model:edge, model:vs, model:ve, model:power-means, model:functional, x:model-depth-zero, model:trial-bounds, x:reduction-power-mean-scaling]
provides: 'main:theorem.s3 (reduction.tex 72–84: $\lvert\widehat I-I_K\rvert\le\alpha(2p-1)D_K+d_K$, $\widehat F_N\ge F^{(K)}_N-\alpha D_K-d_K$, 상수 이동 되돌리기). 규칙 P12, L1 수 7'
math: |
  $p$ 와 $\alpha$ 를 고정하고, 각각 (2.1)을 만족하는 두 상호작용 법칙 $\theta,\theta'$ 와 두 장 법칙 $h,h'$ 를 결합한다. $D=\mathbb E\max_s\lvert\theta(s)-\theta'(s)\rvert$, $d=\mathbb E\lvert h-h'\rvert$ 로 두면
  $$\lvert F_N-F_N'\rvert\le\alpha D+d,\tag{reduction:free-stability}$$
  $$\lvert\mathcal B_r(\zeta,\mathbf m)-\mathcal B_r'(\zeta,\mathbf m)\rvert\le\alpha(2p-1)D+d\tag{reduction:trial-stability}$$
  가 $N$, $r$, 모든 시행 법칙에 균일하게 성립한다($r=0$ 포함). $c$ 가 상호작용에 딸린 적분 가능한 무작위 상수이고 $\widehat\theta=\theta-c$ 이면
  $$\widehat F_N=F_N-\alpha\mathbb Ec,\qquad\widehat{\mathcal B}_r=\mathcal B_r-\alpha\mathbb Ec.\tag{reduction:shift}$$
physics: |
  1차 moment 가정 (2.1)([[model:integrability]])을 각각 만족하는 두 [[g:interaction|상호작용]] 법칙과 두 [[g:field|장]] 법칙을 결합해 $D=\mathbb E\max_s\lvert\theta(s)-\theta'(s)\rvert$, $d=\mathbb E\lvert h-h'\rvert$ 로 두면, quenched [[g:pressure|pressure]]의 차는 $\alpha D+d$ 이하이고 같은 시행 법칙에서 잰 시행 [[g:functional|functional]]의 차는 $\alpha(2p-1)D+d$ 이하다([[g:stability]]). 두 한계는 $N$, 모든 [[g:rsb-steps|RSB 단계 수]]($r=0$ 포함), 모든 시행 order parameter에 균일하다. 적분 가능한 spin 무관 무작위 상수 $c$ 를 상호작용에서 빼면([[g:constant-shift|상수 이동]]) pressure와 functional이 같은 양 $-\alpha\mathbb Ec$ 만큼 움직인다.
gap: |
  정확하다. $D$, $d$ 는 두 법칙의 한 결합(coupling) 아래의 $L^1$ 차이이고, 어떤 결합을 써도 부등식이 성립한다. (2.1)은 $F_N$, $\mathcal B_r$ 과 $D$, $d$ 가 유한하도록 하는 가정이다. 상수 $c$ 는 각 상호작용 사본에 딸린 무작위 상수이고 적분 가능해야 한다. $\mathcal B_r$ 과 $\mathcal B_r'$ 은 같은 시행 법칙 $(\zeta,\mathbf m)$ 에서 비교한다.
abstraction: exact
children: [reduction:stability.s1, reduction:stability.s2, reduction:stability.s3]
source:
  - {file: reduction.tex, lines: [9, 26]}
  - {file: reduction.tex, lines: [28, 43]}
status: proposed
---

**증명의 뼈대.** [[reduction:stability.s1]]: 같은 개수와 index로 두 Hamiltonian을 결합하면 log-weight 차이가 점별로 sup-norm 차이와 장 차이의 합 이하이고 $\log Z$ 가 그것을 보존한다. [[reduction:stability.s2]]: cavity 상호작용과 edge logarithm이 각각 sup-norm 차이 이하로 바뀌고 power mean이 그 한계를 보존한다; site 항은 평균 $\alpha p$ 개, edge 항은 계수 $\alpha(p-1)$. [[reduction:stability.s3]]: 상수는 분배함수와 모든 power mean 밖으로 나오고, site 항 $-\alpha p\mathbb Ec$, edge 항 $+\alpha(p-1)\mathbb Ec$.

**power mean 성질의 출처.** s2와 s3이 쓰는 성질(두 시행 값의 곱셈적 비교가 $T_0$ 를 통과함, 물리 상수가 $T_d$ 밖으로 나옴)은 §2에 명시 진술이 없다. model.tex 123–124(model:trial-bounds)는 절대 곱셈 한계의 보존만 말한다. 그래서 정의 (2.10)에서 직접 읽은 [[x:reduction-power-mean-scaling]](작성자 정식화)을 근거로 둔다.

$D$, $d$ 의 유한성은 (2.1)에서 온다($D\le\mathbb EB(\theta)+\mathbb EB(\theta')$).
