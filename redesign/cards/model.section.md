---
id: model:section
kind: section
title: '§2 모형과 변분 원리'
uses: [upper:bound, comp:bounded-lower, reduction:stability]
provides: '논문 전체의 입력과 목표. 모형(model:hamiltonian)과 가정(x:model-hypotheses)은 upper:bound·reduction:stability·consequences가, 시행 법칙과 functional(model:chain, model:vs, model:ve, model:power-means, model:functional, x:model-depth-zero, model:trial-bounds)은 trees.tex 26·comparison.tex(comp:encoding, comp:insertion-comparison, comp:bounded-lower)·reduction.tex·consequences.tex가, 주정리 main:theorem과 main:formula는 consequences.tex(models:spin, models:sat, models:ground)가 받아 쓴다'
math: |
  정의하는 것 (이 섹션에서 끝남). 짝수 $p\ge2$, $\alpha>0$, 상호작용 $\theta$ 와 장 $h$ 의 법칙에 대해 $-H_N$, $Z_N$, $F_N=\frac1N\mathbb E\log Z_N$ (model:hamiltonian). 가정 (2.1)–(2.4) (model:integrability, model:factorization, model:positivity; 묶음은 x:model-hypotheses). message $x$ 와 $q_x$ (x:model-message), $C_\theta$, $U_\theta$ (model:edge, model:site-message), 시행 사슬 $\zeta\in\mathcal M_{r+1}$, $0<m_1<\cdots<m_r<1$ (model:chain), $V_{\rm s}$, $V_{\rm e}$ (model:vs, model:ve), power mean $T_d$ (model:power-means),
  $$\mathcal B_r(\zeta,\mathbf m)=\log2+\mathbb E\log T_0V_{\rm s}-\alpha(p-1)\mathbb E\log T_0V_{\rm e},\qquad\Phi_r=\inf_{\zeta,\mathbf m}\mathcal B_r(\zeta,\mathbf m)$$
  (model:functional), $r=0$ 의 경우 (x:model-depth-zero), 그리고 moment 조건 없는 유한성 (2.12) (model:trial-bounds).

  주장 (main:theorem). (2.1)–(2.4) 아래 $\lim_{N\to\infty}F_N$ 이 존재하고 $=\inf_{r\ge0}\Phi_r$.

  받는 것 (밖에서). 이 섹션의 정의들은 다른 섹션에 기대지 않는다. 한 군데 예외: "비퇴화 경우 $b$ 와 $\max_s\lvert f_1(s)\rvert$ 가 본질적으로 유계"라는 주석은 upper:bound 증명에서 보인다고 원문이 미리 말한다 (model.tex 39–41, x:model-moment-finiteness). 이 주석을 받아 쓰는 카드는 없다. 주정리의 증명은 이 섹션에 없고 reduction.tex 45–87에 있으며, 거기서 upper:bound (상한), comp:bounded-lower (bounded·순열 불변 하한), reduction:stability (pressure 안정성, 시행 functional 안정성, 상수 이동)를 받는다 (main:theorem.s1–s4).

  내주는 것 (밖으로). 위 provides 칸.
physics: |
  계는 Poisson random [[g:hypergraph|factor graph]] 위의 짝수 $p$체 Ising spin glass이고, 목표 양은 quenched [[g:pressure|pressure]] $F_N$($=-\beta f$)이다. 변분 쪽은 $r$단 RSB의 Mézard–Parisi(Bethe) free entropy를 시행 [[g:order-parameter|order parameter]] $\zeta$ 와 [[g:parisi-parameters|Parisi parameter]] $\mathbf m$ 에서 계산한 값 $\mathcal B_r$([[g:functional]])이다: [[g:site-term|site 항]](새 spin 하나와 그 Poisson$(\alpha p)$개 factor)에서 [[g:edge-term|edge 항]](중복으로 센 factor) $\alpha(p-1)$ 배를 뺀다. 주정리는 pressure의 열역학 극한이 이 시행값들의 inf([[g:phi]])라고 말한다.
gap: |
  (1) 물리의 정류점(saddle point) 선택이 아니라 모든 유한 $r$ 과 모든 시행 법칙에 대한 inf다. inf의 달성, [[g:rsb-steps|RSB 단계 수]] $r\to\infty$ 의 극한 order parameter, 극한 Gibbs 측도는 주장하지 않는다(model.tex 138–140). (2) [[g:hypotheses|가정]]에 [[g:factorization|tanh형 전개]]와 [[g:positivity|부호 조건]]이 들어간다. 부호 조건은 상한에만 쓰인다(upper.tex 125). 전개는 상한(upper.tex 63)과, 하한 쪽에서는 주정리 증명의 상수 이동이 상호작용 법칙을 순열 불변으로 만드는 데 한 번 쓰인다(main:theorem.s1, reduction.tex 54–58). bounded 하한 자체(comp:bounded-lower)는 둘 다 쓰지 않는다(P1). (3) power mean의 cascade 해석은 이 섹션에도 증명에도 쓰이지 않는다([[g:power-mean]]의 물리 대응 칸). (4) 시행 functional의 [[g:message|message]] $x$ 는 실제 계에서 계산한 cavity field가 아니라 임의의 법칙에서 뽑은 변수다. (5) edge 항을 "중복으로 센 factor"로 읽는 것은 작성자의 읽기다(원문은 "corrects for interactions counted in that insertion", model.tex 51–52; 셈은 model:functional 차이 칸).
abstraction: approximation
children: [model:integrability, model:hamiltonian, model:factorization, model:positivity, x:model-moment-finiteness, x:model-hypothesis-remarks, x:model-hypotheses, x:model-message, model:edge, model:site-message, x:model-cavity-bounds, model:chain, model:vs, model:ve, model:power-means, model:functional, x:model-depth-zero, model:trial-bounds, main:theorem, x:model-theorem-scope]
source:
  - {file: model.tex, lines: [1, 140]}
status: proposed
---

**구성.** 앞 절반(model.tex 3–44)은 모형과 가정, 뒤 절반(46–140)은 계층 cavity functional과 주정리다. 정의 카드의 의존 순서는 다음과 같다.

- 모형: [[model:integrability]] ($p$, $\alpha$, $\theta$, $h$, $B(\theta)$, 1차 moment) → [[model:hamiltonian]] ($H_N$, $Z_N$, $F_N$, 독립 구조) ; 가정 [[model:factorization]] → [[model:positivity]] ; 주석 [[x:model-moment-finiteness]] (upper:bound에 기댐), [[x:model-hypothesis-remarks]] ; 묶음 [[x:model-hypotheses]].
- functional: [[x:model-message]] → [[model:edge]], [[model:site-message]] → [[x:model-cavity-bounds]] ; [[model:chain]] → [[model:vs]], [[model:ve]] → [[model:power-means]] → [[model:functional]] → [[x:model-depth-zero]] → [[model:trial-bounds]].
- 주정리: [[main:theorem]] (증명 단계 [[main:theorem.s1]]–[[main:theorem.s4]]는 reduction.tex 45–87), 범위 주석 [[x:model-theorem-scope]].

**밖에서 이 섹션을 쓰는 곳 (원문 `\ref` 기준).**

| 대상 | 쓰는 곳 |
|---|---|
| [[main:theorem]] | upper.tex 12 (`upper:bound` 진술 "Under the hypotheses of"), consequences.tex 33, 63, 112 (`models:spin`, `models:sat`, `models:ground` 증명), introduction.tex 85, overview.tex 50 |
| `main:formula` | reduction.tex 86 (주정리 증명 끝), consequences.tex 19, 47 |
| [[model:factorization]] | upper.tex 63 (삽입을 $a(1+D)$ 꼴로) |
| [[model:positivity]] | upper.tex 125 (나머지항의 부호) |
| [[model:integrability]] | reduction.tex 11 (`reduction:stability`의 가정) |
| [[model:chain]] | trees.tex 26 (시행 사슬을 path kernel의 예로), comparison.tex 72 (`comp:encoding`이 그 branching 판임) |
| [[model:vs]] | comparison.tex 180 ($\widetilde Y_{0,\rm s}=T_0V_{\rm s}$) |
| [[model:functional]] | consequences.tex 83, 137 ($\mathcal B_{r,\beta}$) ; 비교와 축소는 기호 $\mathcal B_r$, $\Phi_r$ 로 쓴다 |
| [[model:trial-bounds]] | comparison.tex 235 (`comp:bounded-lower`에서 $\inf_r\Phi_r$ 의 유한성) |
| [[model:hamiltonian]] | consequences.tex 8 (Poisson 개수와 복원추출을 유지) |
| [[model:section]] | introduction.tex 32, comparison.tex 227 (`comp:bounded-lower` 진술 "with the functionals defined in") |

기호로만 쓰는 곳도 많다: cavity.tex 11–12는 유계 가정 $B(\theta)\le B$, $\lvert h\rvert\le H$ 를 두고 34는 같은 power-mean 재귀를 쓰며, upper.tex는 $V_{\rm s}$, $V_{\rm e}$, $T_0$ 를 그대로 쓴다.

**주의 (순환을 피하는 연결).** `upper:bound` 진술은 `main:theorem`을 가리키지만 실제로 받는 것은 가정뿐이다. 그 카드를 쓸 때는 `main:theorem` 대신 [[x:model-hypotheses]]를 `uses`에 넣으면 `main:theorem` → `upper:bound` 와 순환하지 않는다(x:model-hypotheses의 원문 범위가 `main:theorem`의 줄 130–131을 담아 의존 검사도 통과한다). 같은 이유로 `comp:bounded-lower`는 `model:section` 대신 [[model:functional]]과 [[x:model-depth-zero]]를 가리키는 편이 낫다.

**overview.tex.** 원문 번호로는 overview.tex("Proof strategy")가 §2의 소절이다(graph.json의 `model:section` 범위가 overview.tex 1–51을 포함한다). 이 카드 묶음은 model.tex만 다룬다.
