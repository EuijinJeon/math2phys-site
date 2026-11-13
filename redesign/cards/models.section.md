---
id: models:section
kind: section
title: '§10 명명 모형과 영온도 극한'
uses: [model:hamiltonian, model:integrability, model:factorization, model:positivity, x:model-hypotheses, model:functional, x:model-depth-zero, main:theorem]
provides: 'introduction.tex 29–34 (명명 모형과 그 ground-state 극한, `\cref{models:section}` 34행). L0의 모형 따름정리와 영온도 따름정리, g:named-models, g:ground-state. §2 카드의 예(model:factorization, model:positivity, x:model-moment-finiteness의 명명 예)'
math: |
  받는 것 (§2). 모형 (2.2)와 그 Poisson 개수·복원추출 (model:hamiltonian), 가정 (2.1)–(2.4) (model:integrability, model:factorization, model:positivity; 묶음 x:model-hypotheses), functional (2.11)과 $r=0$ 판 (model:functional, x:model-depth-zero), 주정리 (2.13) (main:theorem). 다른 섹션의 증명 노드는 쓰지 않는다.

  내놓는 것.
  (i) models:spin: 짝수 $p\ge2$, $\alpha>0$, 독립인 $J,H$, $J$ 는 대칭, $\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert<\infty$ 일 때 모든 $\beta>0$ 에서 $\theta_\beta=\beta J\prod_\ell s_\ell$, $h_\beta=\beta H$ 의 모형이 (2.13)을 만족한다. $p=2$ 가 Viana–Bray.
  (ii) models:sat: 짝수 $K\ge2$, $\alpha>0$, 독립 공정 부호 $\varepsilon_\ell$, 그것과 독립인 $W\ge0$, $\mathbb EW<\infty$ 일 때 모든 $\beta>0$ 에서 $\theta_\beta=-\beta W\prod_\ell(1+\varepsilon_\ell s_\ell)/2$, $h=0$ 이 (2.13)을 만족한다. $W=1$ 이 soft random 짝수 $K$-SAT.
  (iii) models:ground: 두 모형에서 $g=\lim_N\frac1N\mathbb E\max_\sigma\mathcal E_N(\sigma)$ 이 존재하고 $\frac1\beta\inf_{r\ge0}\inf_{\zeta,\mathbf m}\mathcal B_{r,\beta}\in[g,g+\log2/\beta]$, 따라서 (10.1).
physics: |
  주정리를 구체적인 [[g:named-models|명명 모형]]에 적용한다: 대칭 coupling의 희석 짝수 $p$-spin glass(Viana–Bray 포함)와 soft random 짝수 $K$-SAT에서, 모든 온도 $\beta>0$ 에서 quenched [[g:pressure|pressure]]의 열역학 극한이 모든 유한 [[g:rsb-steps|RSB 단계 수]]의 Mézard–Parisi 시행값([[g:functional]])의 [[g:phi|inf]]이다. 이어서 $\beta\to\infty$ 로 보내, ground-state 에너지 밀도의 기대값 $-g$([[g:ground-state]])의 열역학 극한이 존재하고 $g$ 가 그 inf를 $\beta$ 로 나눈 것의 $\beta\to\infty$ 극한임을 얻는다.
gap: |
  물리 문장은 다음 내용을 생략한 약화다: 두 명명 모형의 독립성·1차 moment 가정 전체와 영온도 오차 폭 $\log2/\beta$ 를 생략한 개요다.
  (1) 새로운 확률 논증은 없다. 각 모형에서 주정리의 [[g:hypotheses|가정]]([[g:factorization|전개]] (2.3), [[g:positivity|부호 조건]] (2.4), 1차 moment (2.1))을 확인하고(짝수 체수는 진술이 고정할 뿐 §10의 증명에 쓰이지 않는다), 영온도 극한은 $2^N$ 개 배치에서 오는 끼움으로 얻는다. (2) 한정어는 원문 그대로다: 두 모형 모두 "모든 $\beta>0$", spin 모형은 대칭 $J$, SAT는 짝수 $K$. 홀수 $K$(3-SAT)는 제외된다(x:cons-3sat-remark). (3) 모형은 Poisson 개수와 복원추출이다(x:cons-standard-examples). 고정 연결도나 고정 개수 앙상블은 다루지 않는다. (4) 영온도 공식은 각 $\beta$ 의 inf를 따로 취하고 inf의 달성이나 극한 계층을 요구하지 않는다(x:cons-ground-scope). (5) 원문은 이 섹션에서 물리 문헌의 예측(예: 특정 온도에서의 1RSB 해, 영온도 cavity 공식)과 결과를 비교하지 않는다. 선행 연구는 "factorization의 표준 예는 [FL03], [PT04]의 모형"(4–6행)과 3-SAT 동반 논문(131–138행)으로만 나온다.
abstraction: weakening
children: [x:cons-standard-examples, models:spin, models:sat, x:cons-energy-score, models:ground, x:cons-ground-scope, x:cons-3sat-remark]
source:
  - {file: consequences.tex, lines: [1, 138]}
status: proposed
---

**뼈대.** 약속 [[x:cons-standard-examples]] (4–8) → 모형 따름정리 [[models:spin]] (10–34; 단계 [[models:spin.s1]] (2.3), [[models:spin.s2]] (2.4), [[models:spin.s3]] (2.1)과 적용), [[models:sat]] (36–64; 단계 [[models:sat.s1]] 위반 지시함수, [[models:sat.s2]] (2.3)·(2.4), [[models:sat.s3]] (2.1)과 적용) → 정의 [[x:cons-energy-score]] (66–84) → [[models:ground]] (86–125; 단계 [[models:ground.s1]] 끼움, [[models:ground.s2]] 주정리, [[models:ground.s3]] $\beta\to\infty$, [[models:ground.s4]] SAT의 뜻) → 범위 주석 [[x:cons-ground-scope]] (127–129), [[x:cons-3sat-remark]] (131–138, Remark 10.4). 제목 1–2행만 이 섹션 카드에만 든다.

**각 모형에서 원문이 확인한 가정.**

| 모형 | (2.3) 전개 | (2.4) 부호 | (2.1) 1차 moment | 짝수 체수 | 한정어 |
|---|---|---|---|---|---|
| [[models:spin]] (Viana–Bray는 $p=2$) | $a=\cosh\beta J$, $b=\tanh\beta J$, $f_\ell(s)=s$, $\lvert b\rvert<1$ a.s. (25–30) | $J$ 대칭으로 홀수 moment 0, 짝수 moment $\ge0$ (30–31) | $B(\theta_\beta)=\beta\lvert J\rvert$, $\lvert h_\beta\rvert=\beta\lvert H\rvert$ (31–32), 가정 $\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert<\infty$ (14) | 진술에서 고정 (12) | 모든 $\beta>0$; $J,H$ 독립; $J$ 대칭 |
| [[models:sat]] (soft SAT는 $W=1$) | $a=1$, $b=e^{-\beta W}-1$, $f_\ell(s)=(1+\varepsilon_\ell s)/2$, 독립 사본이고 $b$ 와 독립 (59–61) | $0\le-b<1$ (61–62) | $B(\theta_\beta)=\beta W$ (63), 가정 $\mathbb EW<\infty$ (40), $h=0$ | 진술에서 고정 (38) | 모든 $\beta>0$; 부호 독립·공정; $W\ge0$ 은 부호와 독립 |
| [[models:ground]] | 위 둘을 그대로 씀 | 같음 | $g_N$ 의 유한·균일 유계에 씀 (105–106) | 같음 | 각 $\beta$ 에서 inf; (10.1) 우변의 극한 순서 $N\to\infty$ 다음 $\beta\to\infty$. 좌변 $g$ 는 최댓값으로 직접 정의된 양의 $N$ 극한(88–91)이고, 두 순서가 같은 값을 준다는 것이 내용이다(작성자 읽기, [[models:ground]] 차이 칸 (1)) |

원문은 엄격한 곱 한계를 spin 모형에서는 $\lvert b\rvert<1$ 로(30행), SAT에서는 "the strict product condition ... hold"로(61–62행) 확인한다. 두 경우 모두 $\max_s\lvert f(s)\rvert=1$ 이다(작성자 확인; 원문에 없다).

짝수 체수 열의 "진술에서 고정"은 §10의 증명이 짝수를 쓰지 않는다는 뜻이다(spin의 $e^{\beta Jx}=\cosh\beta J\,(1+x\tanh\beta J)$ 는 $x=\pm1$ 이면 $p$ 의 홀짝과 무관하다). 짝수 체수가 쓰이는 곳은 상한의 볼록성이다: upper.tex 123–124 "Since $p$ is even, convexity of $x\mapsto x^p$ makes the bracket nonnegative"([[upper:remainder]]; 고정은 model.tex 3행, [[model:integrability]]).

**밖에서 받는 것** (원문의 실제 참조와 `\ref` 없는 사용).

| 받는 것 | 카드 | 원문 위치 |
|---|---|---|
| Poisson 개수와 복원추출 | [[model:hamiltonian]] | consequences.tex 8 (`\eqref`); 68–70, 75–77의 $M_N$, $i_{\ell,k}$, 81의 $Z_N$ (`\ref` 없음) |
| 변분 공식 (2.13) | [[main:theorem]] (식 `main:formula`) | 19, 47 (`\eqref`) |
| 주정리 적용 | [[main:theorem]] | 33, 63, 112 (`\cref`) |
| 가정 (2.1)–(2.4) | [[x:model-hypotheses]], [[model:integrability]], [[model:factorization]], [[model:positivity]] | 25–33, 52–63 (`\ref` 없음; "all hypotheses of main:theorem", "the strict product condition and every positivity inequality"), 32, 63의 $B(\theta)$ |
| functional (2.11) | [[model:functional]] | 83 (`\eqref`; $\mathcal B_{r,\beta}$), 137 (`\eqref`; 동반 논문의 functional이 이것과 다르다는 비교) |
| $r=0$ 판 | [[x:model-depth-zero]] | 95, 114의 $\inf_{r\ge0}$ (`\ref` 없음) |

§2 [[model:section]] 카드의 export 표(consequences.tex 8, 19, 47, 33, 63, 112, 83, 137)는 `\ref` 기준으로 위와 맞는다. 차이 한 가지: 그 표는 137행을 [[model:functional]]의 사용 "($\mathcal B_{r,\beta}$)"로 묶어 적지만, 137행은 $\mathcal B_{r,\beta}$ 를 쓰는 곳이 아니라 Remark 10.4에서 동반 논문의 functional이 (2.11)과 다르다고 비교하는 곳이다. 또 그 표에는 `\ref` 없는 사용(가정 확인, $B(\theta)$, $M_N$·$i_{\ell,k}$, $r=0$)이 없었다. 둘 다 검토 2 반영에서 그 카드에 고쳐 넣었다(137행을 따로 적고, 표 아래 "기호로만 쓰는 곳" 문장에 §10을 더함).

**밖에 내주는 것.**

| 받는 곳 | 쓰는 것 | 위치 |
|---|---|---|
| 원문 introduction | [[models:spin]], [[models:sat]] ("includes the Viana–Bray model, diluted even-spin models with symmetric couplings, and soft random even-$K$ SAT at every positive temperature"), [[models:ground]] ("expected ground-state limits"), 섹션 전체 (`\cref{models:section}`) | introduction.tex 29–34 |
| 원문 다른 섹션의 증명 | 없음 (§10은 증명 그래프의 잎이다) | — |
| redesign 문서 | [[models:spin]], [[models:sat]], [[models:ground]], [[x:cons-ground-scope]] | `layers/L0.md`, 용어집 [[g:named-models]], [[g:ground-state]], [[g:positivity]]·[[g:factorization]]의 물리 대응 칸 |
| §2 카드의 예 | [[models:spin.s1]]–[[models:spin.s2]], [[models:sat.s2]] | [[model:factorization]], [[model:positivity]], [[x:model-moment-finiteness]]의 차이 칸과 본문, [[main:theorem]]의 provides |

**ID.** 원문 라벨 접두사는 `models:`다(§2의 `model:`과 다르다). 라벨 없는 노드는 `x:models-*` 대신 `x:cons-*` 로 써서 §2의 `x:model-*` 와 헷갈리지 않게 했다. (10.1)의 식 라벨 `models:ground-formula`는 [[models:ground]] 카드가 담는다. Remark 10.4는 graph.json에서 `x:consequences-L131`이고 카드 ID는 [[x:cons-3sat-remark]]다.
