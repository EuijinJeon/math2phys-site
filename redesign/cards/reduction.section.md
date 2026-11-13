---
id: reduction:section
kind: section
title: '§9 정규화, truncation, 증명의 완성'
uses: [comp:bounded-lower, upper:bound, x:cavity-bounded, model:integrability, model:hamiltonian, model:factorization, model:positivity, model:chain, model:site-message, model:edge, model:vs, model:ve, model:power-means, model:functional, x:model-depth-zero, model:trial-bounds]
provides: 'main:theorem (reduction:stability가 main:theorem.s3에 들어감; reduction.tex 45–87은 main:theorem.s1–s4). 규칙 P12, L1 수 7'
math: |
  받는 것. bounded이고 순열 불변인 상호작용의 하한 comp:bounded-lower, 상한 upper:bound, 그리고 §2의 모형·가정·시행 functional.

  내놓는 것 (1–44행). reduction:stability: (2.1)을 만족하는 법칙들의 결합에서 $\lvert F_N-F_N'\rvert\le\alpha D+d$, $\lvert\mathcal B_r-\mathcal B_r'\rvert\le\alpha(2p-1)D+d$ ($N$, $r$, 시행 법칙에 균일), 상수 이동 $\widehat F_N=F_N-\alpha\mathbb Ec$, $\widehat{\mathcal B}_r=\mathcal B_r-\alpha\mathbb Ec$.

  45–87행은 주정리의 증명이고 main:theorem 카드(단계 main:theorem.s1–s4)가 맡는다: 상수 이동으로 승수 $a$ 를 없애 순열 불변으로 만들고, $[-K,K]$ 로 truncation해 comp:bounded-lower를 적용하고, 안정성으로 $K\to\infty$ 를 보내 $\liminf_NF_N\ge\inf_r\Phi_r$, upper:bound와 합쳐 $\lim_NF_N=\inf_{r\ge0}\Phi_r$.
physics: |
  하한은 [[g:bounded-law|유계]]이고 입력에 대칭([[g:permutation-invariance|순열 불변]])인 [[g:interaction|상호작용]]에서만 증명되어 있고, 상한은 [[g:factorization|전개]]와 [[g:positivity|부호 조건]]을 쓴다. 에너지 원점의 무작위 [[g:constant-shift|상수 이동]]과 [[g:truncation|truncation]], 그리고 pressure와 시행 [[g:functional|functional]]의 [[g:stability|$L^1$ 안정성]]이 두 진술을 같은 [[g:hypotheses|가정]] 아래로 잇는다.
gap: |
  물리 문장은 다음 내용을 생략한 약화다: 정량 안정성 상수와 최종 liminf/limsup 조립식을 생략한 개요다.
  정확하다. 상한은 원래 법칙에 바로 쓰고, 상수 이동과 truncation은 하한 쪽에만 쓴다. 시행 쪽 안정성 상수가 모든 $r$ 과 시행 법칙에 균일하다는 것이 inf와 $K\to\infty$ 를 바꾸는 근거다. 물리 유도는 보통 이 단계를 생략한다.
abstraction: weakening
children: [x:reduction-power-mean-scaling, reduction:stability, main:theorem]
source:
  - {file: reduction.tex, lines: [1, 87]}
status: proposed
---

**뼈대와 겹침 처리.** 이 섹션의 고유 카드는 1–44행만 다룬다: 서두(4–7, 이 카드), [[reduction:stability]](진술 9–26, 증명 28–43을 [[reduction:stability.s1]]–[[reduction:stability.s3]]가 덮음), 그리고 power mean 성질을 정의에서 읽은 [[x:reduction-power-mean-scaling]]. 45–87행(Proof of main:theorem)은 이미 [[main:theorem]]의 단계 카드 [[main:theorem.s1]](45–59), [[main:theorem.s2]](60–69), [[main:theorem.s3]](70–84), [[main:theorem.s4]](85–87)가 덮으므로 새 카드를 만들지 않고 children에서 [[main:theorem]]을 가리킨다. 그래서 [[main:theorem]]은 [[model:section]]과 이 카드 두 섹션의 자식이다.

**밖에서 받는 것** (`\ref` 위치와 `\ref` 없는 사용). 1–44행에서:

| 주는 곳 | 쓰는 것 | 원문 위치 |
|---|---|---|
| §8 [[comp:bounded-lower]] | bounded 순열 불변 하한 | 4 (`\cref`) |
| §4 [[upper:bound]] | 상한이 factorization과 positivity를 씀 | 5–6 (`\ref` 없음) |
| §2 [[model:integrability]] | (2.1) | 11 (`\eqref`) |
| §2 [[model:hamiltonian]] | $F_N$, 같은 개수와 index의 결합 | 15, 29–32 |
| §2 [[model:site-message]], [[model:edge]], [[model:vs]], [[model:ve]], [[model:chain]] | cavity 상호작용 $U_\theta$, edge logarithm $\log C_\theta$, site 항의 평균 $\alpha p$ 개 상호작용 | 33–36, 40–42 (`\ref` 없음) |
| §2 [[model:power-means]] | 곱셈적 비교의 보존과 상수 인자의 분리 ([[x:reduction-power-mean-scaling]]로 읽음) | 34–35, 39–40 (`\ref` 없음) |
| §2 [[model:functional]], [[x:model-depth-zero]] | $\mathcal B_r$, $r=0$ 포함 | 16, 19, 24, 40–42 |
| §2 [[model:trial-bounds]] | $\mathcal B_r$ 의 유한성(차를 잡는 데 필요) | (`\ref` 없음, 작성자 읽기) |
| §5 [[x:cavity-bounded]] | "Until reduction:section"이 가리키는 가정. 이 섹션이 그것을 푼다 | cavity.tex 11 (예고), reduction.tex 4–7 |

45–87행이 받는 것(comp:bounded-lower 64·76, upper:bound 85, main:formula 86, model:factorization 50–51, model:integrability)은 [[main:theorem]]과 그 단계 카드의 `uses`에 있다.

**밖에 내주는 것.**

| 받는 곳 | 쓰는 것 | 원문 위치 |
|---|---|---|
| [[main:theorem.s3]] | [[reduction:stability]]의 세 식 (`\ref` 없이 "the uniform trial estimate", "the pressure estimate", "Undoing the constant shift") | reduction.tex 72–84 |
| 규칙 P12, L1 수 7 | [[reduction:stability]] | layers |
| overview.tex 마지막 문단 | 이 절 전체: 정규화와 모든 시행 법칙에 균일한 추정이 유계성을 없애 주정리를 줌 | overview.tex 48–51 (51 `\cref`) |
| §5 서두 (예고) | 유계·순열 불변 가정이 이 절까지만 유지됨 ([[x:cavity-bounded]]) | cavity.tex 11 (`\cref`) |

**인터페이스 대조.** [[main:theorem]]은 [[comp:bounded-lower]], [[reduction:stability]], [[upper:bound]]를 `uses`에 넣는다. 실제 사용과 맞는다. [[main:theorem.s3]]이 쓰는 세 부등식의 상수($\alpha D+d$, $\alpha(2p-1)D+d$, $-\alpha\mathbb Ec$)는 [[reduction:stability]]의 진술과 같다. [[model:section]]의 표는 reduction.tex 11(`model:integrability`)과 86(`main:formula`)을 적는다. 맞는다. 다만 1–44행은 그 밖에 §2의 정의들(위 표)을 `\ref` 없이 쓴다. [[x:cavity-bounded]]의 provides는 "이 가정을 푸는 것은 reduction.tex(main:theorem.s1–s3)"라 적는다. 맞는다.

**power mean 성질 (지시받은 확인).** reduction.tex 34–35의 "power means preserve these root-measurable bounds"는 model.tex 123–124 "the power-mean operators preserve pointwise multiplicative bounds"([[model:trial-bounds]])와 가장 가깝지만 같지 않다: §2는 절대 한계($e^{-c}\le V\le e^c$)의 보존만 말하고, 여기서 필요한 것은 두 값의 상대 비교다. 39–40의 동차성(상수가 power mean 밖으로 나옴)은 §2 어디에도 진술이 없다(model.tex 92–95는 정의만 준다). 둘 다 [[x:reduction-power-mean-scaling]]에서 정의로부터 직접 읽었고 "작성자" 표시를 붙였다.
