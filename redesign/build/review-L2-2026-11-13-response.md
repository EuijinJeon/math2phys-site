# L2 검토 반영 — 2026-11-13

반영자: Claude Opus(L2 작성자·검토자와 별개 실행). 입력: `build/review-L2-2026-11-13.md`(검토), `build/L2-author-notes-2026-11-13.md`(작성자 제안 1–10), `HANDOFF.md` 0·3.2절. 각 지적을 원문(`source/sections/*.tex`)과 다시 대조해 판정했다. 행 번호는 원문 파일의 것이다.

고친 파일: `layers/L2.md`, `layers/L1.md`, `layers/L0.md`, `layers/rules.md`, `layers/glossary.md`. 카드·tools·SCHEMA·HANDOFF·site는 고치지 않았다. status는 모두 proposed 그대로다.

판정 집계: 검토 지적 15건(반영 12, 좁힘 3, 기각 0). 규칙 표 문제 R1–R8(반영 7, 좁힘 1). 작성자 제안 1–8, 10(반영 7, 좁힘 1, 기록만 유지 1; 9는 도구 제안이라 범위 밖).

---

## 1. 검토 지적 15건

### 중간

| # | 판정 | 원문 대조 | 고친 곳 |
|---|---|---|---|
| M1 | **반영** | `decorrelation.tex` 356–359("controls every projection error after division"), 446–457($C_{L,k,\eta}\varepsilon_{N,L,k}$, "tends to zero at fixed $L$"), 613–622. 검토자 말대로 $L$ 에 균일한 것은 사영 오차뿐이다 | L2 7.2 "증명의 모양"; L1 수 5(같은 문장). 둘 다 "사영 오차"로 좁히고 항등식 오차는 고정 $L$ 에서 먼저 없앤다는 문장을 붙임 |
| M2 | **반영** | `decorrelation.tex` 63–75(깊이 평균만), `introduction.tex` 75–80. 논문은 Parisi 그림과의 대응을 말하지 않는다 | L2 7.3 P9 문단에서 문장 삭제, 7.3 끝 직관 상자에 [[g:overlap-concentration]] 물리 대응 칸을 가리키는 구절로 합침(상자를 새로 만들지 않고 있던 상자에 넣어 분량 절약). 규칙 P9(R2)와 용어집도 함께 |
| M3 | **반영** | `perturbations.tex` 103("Constants need not be uniform in $L$ or $\nu$"), 311–312("No uniformity … is asserted"); `decorrelation.tex` 621–622("No rate … uniform in $L$ is used"); `overview.tex` 45–46 | L2 5절("균일성은 주장되지 않는다"), 6.3절(같음), 8.4절("증명에 없다… 이 증명 안에서는 순서를 바꿀 근거가 없다", 표의 "수렴 속도는 주어지지 않음"), 1.5의 1("~에서 0이 된다는 것만 증명된다"), 1.5의 4("순서로 증명된다"), 10절("이 증명에서 … 순서로 얻어지고"). L1 끝 문단의 "깊이 평균으로만, … 순서로만 얻어진다"도 같은 꼴로. 규칙 P5·P7, 용어집 `g:selected-sequence` 는 R3 |
| M4 | **반영** | `cavity.tex` 16("use $r=L-1$ auxiliary levels"), `trees.tex` 24–25("In an $r$-level application, $L=r+1$"), `comparison.tex` 236–245(고정 $L$ 잔차 부등식). (a)(b) 모두 맞다 | L2 1.5의 1 전체 재작성(장치는 원문대로 $r=L-1$; 구별할 것은 "물리적 RSB 단수로 읽는 것은 증명되지 않는다"와 "정리의 $r$ 은 inf의 변수"; 고정 $L$ 에는 잔차 부등식이 있고 잔차는 $L\to\infty$ 에서 0이 된다는 것만 증명; 그래서 유한 단수 하한 명제가 **진술되어 있지 않다**). L2 2.3절의 "$L$ 은 $r$ 이 아니다" 삭제. 검토자 제안 문장의 "하한은 $L\to\infty$ 를 거쳐야 닫히고"는 "이 증명에서 하한은 … 거쳐 닫히고"로 한 번 더 좁혔다("거쳐야"는 필요성 주장이라 원칙에 걸린다). 같은 문제가 있던 L1 기호 줄 "$L=r+1$ 은 보조 계층의 깊이"와 규칙 머리(R4)도 고침 |
| M5 | **반영**(제안 5와 함께) | `trees.tex` 317–332. 상쇄 예의 맥락(두 old path가 $d$ 에서 갈라지고 anchor가 그 하나, 새 color가 anchor와 정확히 $d$ 에서 갈라짐), 미루기는 "required split is delayed to $d+1<L$" 곧 split 깊이 $d+1$ 의 다른 목표, 남는 선택은 anchor path 위 unary vertex의 fresh split 하나(계수 $-\delta$). 절댓값 합 $2+\delta$ 를 다시 계산해 확인 | 용어집 `g:depth-delay` 뜻 칸에 예 전체(조건 $d+1<L$, "다른 목표" 포함)를 넣고 `g:tree-coefficient` 쓰지 않는 뜻에 "미루기 전의 예"를 명시. 그 뒤 L2 6.2 문장을 이 칸만으로 닫히게 고치고 출처를 "(P6′; [[g:depth-delay]] 뜻)"으로 바꿈. 규칙 R6, L1 끝 문단 "($-\delta$ 대 $2+\delta$)"도 "미루기 전"을 붙임 |

### 낮음

| # | 판정 | 원문 대조 | 고친 곳 |
|---|---|---|---|
| L1 | **반영** | `upper.tex` 18–34: "If $b=0$ a.s. or $M=0$ a.s., the interaction is a spin-independent random constant … $F_N=\mathcal B_r$ for every trial law. Otherwise …" | L2 3절 "부호", 1.4절 표 (2.3)행. 규칙 P1·P2 차이, 용어집 `g:factorization` 역할·`g:bounded-law` 쓰지 않는 뜻(R5) |
| L2 | **반영** | `upper.tex` 70–74("Subtract $c$ from each insertion increment … cancel in the combination with coefficients $1,-p,p-1$"), 75–94(λ 정규화, "Dominated convergence therefore recovers"), 122–126("absolutely convergent for $\lambda<1$") | L2 3절 "$\log a$ 피하기". L1 수 1, 규칙 P2 차이와 "상한의 정규화" 묶음(R5) |
| L3 | **반영** | `comparison.tex` 20–24("with the reservoir root disorder averaged, there is a deterministic trial law"), 80–82("independent copies of the entire construction, including the reservoir root and uniform site") | L2 8.1 P10 문단 끝. 규칙 P10 차이(R7) |
| L4 | **반영** | `comparison.tex` 87–97(고정 prescribed tree, "observable of absolute value at most one"); 규칙 표 "확신이 낮은 대응" P11 항목의 단서 | L2 8.2 "왜 바꿀 수 있는가" |
| L5 | **반영** | `perturbations.tex` 350–356(`pert:palm`: $\lvert H_N(t_\nu,u_\nu)\rvert\le\lVert f\rVert_\infty e_{\nu,N}$), 411–424 | L2 6.3 "어디서 오는가" |
| L6 | **반영** | `reduction.tex` 49–50("The constant is integrable, since $\lvert c\rvert\le B(\theta)$"), 59($\mathbb EB(\widehat\theta)\le2\mathbb EB(\theta)$) | L2 1.4절 표 (2.1)행 하한 칸 |
| L7 | **좁힘** | 머리말 부분: 제안 1·2를 용어집에 반영해 2절과 가정 번호가 용어집만으로 닫히게 되었고, M5로 6.2도 용어집으로 닫힌다. 그래서 머리말에 "(2절은 카드)"를 더하는 대신 `(카드)` 표지 자체를 없앴다(읽는 법에서 정의 삭제, 본문의 카드 표지 16곳 교체: 1.1 2곳, 2절 13곳, 4절 머리의 `x:cavity-bounded` 1곳은 `g:bounded-law` 로 닫힘). 10절 부분은 반영: `decorrelation.tex` 4–9와 6.4절에 맞게 "모형과 무관한 확률 부등식" 추가 | L2 머리 "읽는 법", 1.1, 2절 전체, 4절 머리, 10절 |
| L8 | **반영** | `decorrelation.tex` 72–74(singleton 고정 $L$), 562–566($\operatorname{Var}(M)\to0$ 각 고정 $L,S,e$); score 집중 `perturbations.tex` 98–103 | L2 1.5의 4("잎이 둘 이상인 $S$ 의 집중 진술(P8, P9)은 …; score 집중(P5), singleton, $\operatorname{Var}(M)\to0$ 은 고정 $L$ 의 진술") |
| L9 | **반영** | `trees.tex` 233("This identity is conditional on the root"); `perturbations.tex` 51–60($t_\nu=1/j$, $1/2<\psi_\nu<3/2$, $s_N=N^{3/4}$)은 구성의 사실 | L2 6.1 P6 식 앞에 "(root가 주어진 조건부 항등식)"; 4.2 상자 둘째 문장을 상자 밖 섭동 정의 문단으로 옮김 |
| L10 | **반영** | `perturbations.tex` 258–259($\mathbf u_j$), 309–311; `comparison.tex` 8–15($\mathbf u_{L,N}$) | L2 1.5의 2 |

---

## 2. 규칙 표 문제 R1–R8

| # | 판정 | 원문 대조 | 규칙 표에서 바뀐 것 |
|---|---|---|---|
| R1 | **반영** | `model.tex` 3, `upper.tex` 123–124. HANDOFF 3.2의 4의 정정 문구와 맞춤 | "확신이 낮은 대응" P1 짝수 $p$ 항목: "직접 쓰이는 곳은" → "증명 안에서 명시적으로 부르는 곳은 상한의 볼록성 단계(`upper.tex` 123–124)뿐이지만" |
| R2 | **반영** | `decorrelation.tex` 63–75, `introduction.tex` 75–80 | P9 물리 규칙 칸에서 Parisi 그림 문장 삭제. P9 차이 칸 끝에 "견주는 읽기는 [[g:overlap-concentration]]의 물리 대응 칸(intuition)에 있다". 용어집 그 칸을 approximation → **intuition** 으로 바꾸고 단서(물리 그림은 물리적 pure state tree 위 고정 깊이 진술, 여기는 보조 계층·깊이 평균, 논문은 대응을 말하지 않음)를 붙임. P9 유형(approximation)은 그대로: 규칙 문장의 "branching pattern을 정하면 … 집중"이 깊이 평균 진술을 넓게 말하므로 |
| R3 | **반영** | `perturbations.tex` 103, 311–312 | P5 차이: "균일하지 않다" → "균일성은 주장되지 않는다(`perturbations.tex` 103, 311–312)". P7 차이: "오차는 균일하지 않다" → "오차의 균일성은 주장되지 않는다". 용어집 `g:selected-sequence` 쓰지 않는 뜻 같은 문장 |
| R4 | **반영** | `cavity.tex` 16, `introduction.tex` 75–77 | 머리 기호 목록: "$L\ge2$ 는 보조 계층의 깊이($r=L-1$단 RSB)" → "보조 계층의 깊이다(encoding이 이것을 $r=L-1$단 시행 법칙으로 옮긴다, P10)". L1 기호 줄의 "$L=r+1$ 은 보조 계층의 깊이"도 같은 이유로 고침 |
| R5 | **반영** | `upper.tex` 18–34, 70–94, 122–126 | P1 차이: 본질적 유계성에 "(비퇴화 경우)". P2 차이: 비퇴화/퇴화 구분, $c$ 빼기(세 삽입 계수 $1,-p,p-1$ 에서 상쇄)와 $\lambda$(절대수렴, $\lambda\uparrow1$ 지배수렴)의 역할 분리. "상한의 정규화" 묶음 문장도 같게. L1 수 1 동일 |
| R6 | **반영** | `trees.tex` 317–332 | "규칙으로 못 옮긴 것"의 깊이 미루기 묶음: "차이를 없앤다" → "처방 split을 old branching 깊이에서 떼어 놓아 허용되는 선택을 줄인다; 미루기 전 $-\delta$/$2+\delta$, $d+1<L$ 로 미룬 다른 목표에서 $\delta$" |
| R7 | **반영** | `comparison.tex` 20–24, 80–82 | P10 차이에 "$\zeta_{L,N}$ 은 reservoir root(disorder와 균일 site)까지 평균한 결정적 법칙, label 사이는 구성 전체의 독립 사본. P11의 '독립 사본'은 이 뜻" |
| R8 | **좁힘** | `model.tex` 25–34(일반 꼴), `consequences.tex` 24–29(spin만 tanh), 59–62(SAT는 $e^{-\beta W}-1$) | P1 물리 규칙 칸: "tanh 전개 $e^\theta=…$" → "전개 $e^\theta=…$([[g:factorization]])". 검토자가 든 두 대안 중 표시어 쪽. 같은 이름 붙임이 L0("factor weight의 tanh형 전개")에도 있어 "factor weight의 전개(spin 모형에서는 tanh 전개)"로 고침 |

검토자가 "규칙 표 밖이지만 같은 문장"으로 든 L1 수 5 두 곳: M1 문장 반영, "$R_S$ 가 branching pattern으로 정해진다는 결론" → "$R_S$ 가 평균 $\mathbb ER_S$ 주위로 집중한다는 결론"으로 반영.

### 사용자가 승인할 13행에서 바뀐 것 (행별)

| 행 | 바뀐 칸 | 내용 |
|---|---|---|
| 머리 | 기호 목록 | $L$ 의 괄호(R4) |
| P1 | 물리 규칙 | "tanh 전개" → "전개"(R8) |
| P1 | 차이 | 본질적 유계성 "(비퇴화 경우)"(R5) |
| P2 | 차이 | interpolation 귀속(제안 8), 비퇴화/퇴화, $c$ 와 $\lambda$ 역할 분리(R5) |
| P3, P4 | — | 바뀌지 않음 |
| P5 | 차이 | 선택 순서 문장으로 교체(제안 3: 평균 증분이 낮은 $N$ 이 무한히 많다 → 그 안에서 $N_j$ → Markov로 한 점 → 대각 부분수열; 양의 밀도는 쓰지 않는다), "균일성은 주장되지 않는다"(R3) |
| P6, P6′ | — | 바뀌지 않음(P6′ 유형은 제안 10, 아래 사용자 판단) |
| P7 | 차이 | "오차의 균일성은 주장되지 않는다"(R3) |
| P8 | — | 바뀌지 않음 |
| P9 | 물리 규칙 | Parisi 그림 문장 삭제(R2) |
| P9 | 차이 | 끝에 용어집 물리 대응 칸 가리키기 한 문장(R2) |
| P10 | 차이 | 결정적 법칙·독립 사본의 뜻(R7) |
| P11, P12 | — | 바뀌지 않음 |
| 규칙으로 못 옮긴 것 | 머리, 묶음 4개 이름, 깊이 미루기·상한의 정규화 문장 | 묶음 이름 고정(제안 7), R6, R5 |
| 확신이 낮은 대응 | P1 짝수 $p$ 항목 | R1 |

유형 칸과 승인 칸은 어느 행도 바꾸지 않았다.

---

## 3. 작성자 제안

| # | 판정 | 원문 대조 | 고친 곳 |
|---|---|---|---|
| 1 | **반영** | `consequences.tex` 24–34(spin: $a=\cosh\beta J$, $b=\tanh\beta J$, $f_\ell=s$, $B(\theta_\beta)=\beta\lvert J\rvert$, $\lvert h_\beta\rvert=\beta\lvert H\rvert$), 51–64(SAT: $I_\varepsilon$, $e^{\theta_\beta}=1+(e^{-\beta W}-1)I_\varepsilon$, $a=1$, $b=e^{-\beta W}-1$, $f_\ell=(1+\varepsilon_\ell s)/2$, $0\le-b<1$, $B(\theta_\beta)=\beta W$), 6–8(Poisson·복원추출 유지), 131–138(3-SAT 제외) | 용어집 `g:named-models` 뜻 칸에 두 모형의 $(a,b,f_\ell)$, (2.1)–(2.4) 확인; 쓰지 않는 뜻 칸 신설(비대칭 $J$, 고정 연결도, $\beta=\infty$, 필요한 RSB 단수는 말하지 않음; 짝수 $K$ 가 3-SAT 제외). 이로써 L2 2절의 카드 표지 13곳을 모두 용어집 링크로 바꿈(카드 링크는 절 머리의 "증명은 [[models:spin]], [[models:sat]]" 하나만 남김). 영온도 문단의 `models:ground` 카드 표지는 `g:ground-state` 역할 칸으로 이미 닫혀 지움 |
| 2 | **반영** | `main.tex` 20(`\numberwithin{equation}{section}`), 62–64(introduction이 §1, model이 §2, overview는 §2 안의 subsection), `model.tex` 3–44의 식 순서 integrability, hamiltonian, factorization, positivity. 짝수 $p$ 는 (2.1) 앞 3행에서 고정. (2.1)–(2.4) 번호가 맞음을 조판 규칙까지 확인 | 용어집 `g:hypotheses` 뜻 칸에 번호 대응. L2 1.1의 "번호는 카드 [[x:model-hypotheses]]", "(카드 [[model:hamiltonian]], [[model:integrability]])"를 [[g:hypotheses]]로 |
| 3 | **반영** | `perturbations.tex` 269–301("Hence infinitely many $N$ satisfy $\int\Delta_N\,d\pi\le\underline F+\varepsilon$"; 평균 score 집중 98–100은 모든 $N$; Markov로 $G_j$, 측도 $\ge1-j^{-2}$; 대각 부분수열). "양의 밀도"는 원문에 나오지 않고 증명이 쓰지 않는다(그래서 "필요 없다"가 아니라 "쓰지 않는다"로 씀) | 규칙 P5 차이, L2 5절 "선택의 모양" |
| 4 | **좁힘**(검토자가 좁힌 꼴) | `comparison.tex` 236–245(고정 $L$ 잔차 부등식), `decorrelation.tex` 82–83("Averaging over depths is essential" — 두 추정을 합칠 때의 말), 613–622. "$L\to\infty$ 가 본질적"은 받지 않음 | 용어집 `g:rsb-steps` 쓰지 않는 뜻 신설: "유한 단수에서 닫히는 하한 명제가 진술되어 있지 않다; 고정 $L$ 에는 잔차 부등식이 있고 잔차는 $L\to\infty$ 에서 0이 된다는 것만 증명; $N$ 극한 뒤에도 남는 오차 한계($1/(\eta L)$, $C/L$, $C_k(\eta+L^{-1})$ 등)는 $L\to\infty$ 에서 0이 되는 양". 검토자 문장의 "모든 오차 한계"는 score 오차·$\operatorname{Var}(M)$ 처럼 고정 $L$ 에서 사라지는 것도 있어 "$N$ 극한 뒤에도 남는"으로 한 번 더 좁힘(원문 613–622의 "Errors that survive the $N$ limit"). L2 1.5의 1이 이 칸을 가리킴 |
| 5 | **반영** | `trees.tex` 317–332 | M5 참조 |
| 6 | **반영** | `perturbations.tex` 44–49($t_\nu=j^{-1}$), 411–424($H_N(j^{-1},0)$: 삽입 크기 변수를 $t=j^{-1}$ 에서 봄), `upper.tex` 41–60(interpolation 시간) | 용어집 `g:perturbation` 쓰지 않는 뜻 신설(세 쓰임과 그 만나는 곳). L2 1.5의 2에서 세 쓰임을 한 줄로 나열하고 그 칸을 가리킴(예전 L2는 $t_\nu$ 를 빼먹었다) |
| 7 | **반영**(짧게) | — | "규칙으로 못 옮긴 것" 머리에 "굵은 글씨가 묶음 이름이고 L2는 그대로 인용한다"를 두고, 긴 이름 4개를 짧은 고정 이름으로: "깊이 미루기", "잎 개수 귀납과 사영", "marker anchor 단계", "깊이 연속성"(설명은 이름 뒤 괄호로). L2의 ▣ 줄과 부록 A를 이 이름으로 맞춤 |
| 8 | **반영** | `upper.tex` 3–5: "The interpolation method of Guerra, adapted to diluted systems by Franz and Leone and to arbitrary finite levels by Panchenko and Talagrand". `introduction.tex` 17–18도 같은 귀속. 용어집 `g:interpolation` 물리 대응 칸은 이미 이 꼴 | 규칙 P2 차이("Guerra–Franz–Leone interpolation" → 원문 귀속), L2 1.3("Guerra; Franz–Leone, Panchenko–Talagrand"). 카드 `x:overview-strategy` 의 "Guerra–Franz–Leone–Panchenko–Talagrand" 계보 표현은 카드라 손대지 않음 |
| 10 | **기록만 유지** | — | 규칙 표 "확신이 낮은 대응" P6′ 항목에 이미 `weakening`/`blackbox` 둘 다 가능하다는 기록이 있다. 유형은 바꾸지 않음. 사용자 판단 |
| 9 | 범위 밖 | 도구 제안 | 손대지 않음 |

---

## 4. 분량

`wc -m`(글자 수): L2 57,667 → 57,639(줄어듦). L1 10,046 → 10,357(M1·R4·R5 반영으로 늘어남). 비율 5.74 → 5.57. 작성자 노트의 37,100/7,186(5.2배)은 다른 세는 법(수식·링크 제외로 보임)이라 직접 비교하지 않았다. 늘어난 문장을 상쇄하려고 줄인 곳:
- 부록 A에서 "증명 카드" 열을 지우고 "증명 카드는 괄호 안 절의 ▣ 줄에 있다"로 가리킴(▣ 줄과 완전히 겹치던 정보).
- 10절 첫 두 문단을 하나로 합치고 L1 끝 문단을 가리킴.
- 2절 각 항목의 카드 표지 제거, 2.3의 중복 문장("원문이 하지 않는 일이고, 주정리는 어느 $r$ 이 …") 축약.
- 7.3절 직관 상자를 새로 만들지 않고 기존 상자에 합침.

---

## 5. 검사

`python3 tools/check.py --out /tmp/l2r-check.md`: 오류 0. 경고는 대칭 4건뿐(카드 `uses`/`provides` 맞물림, 알려진 것). 물리판: 오류 0, 경고 0, 단락 149개 중 규칙·링크 없음 0, 13개 규칙 모두 본문에서 쓰임. 용어: 통과(항목 68, 링크 1228).

---

## 6. 사용자 판단으로 넘기는 것

1. **P6′ 유형**(`weakening` 대 `blackbox`, 작성자 제안 10). 검토자 판정대로 어느 쪽이든 참을 잃지 않는다. 지금은 `weakening` 이고 "확신이 낮은 대응"에 두 읽기가 기록되어 있다.
2. **P9 유형을 `approximation` 으로 둘 것인가.** 물리 규칙 칸에서 Parisi 그림 문장을 뺀 뒤에도 "branching pattern을 정하면 … 집중한다"가 깊이 평균 진술을 넓게 말하므로 `approximation` 을 유지했다. 용어집 `g:overlap-concentration` 물리 대응 칸은 intuition으로 바꿨다(그 칸은 Parisi 그림과의 견줌만 다루므로).
3. **`(카드)` 표지를 L2에서 없앤 것.** 2절과 가정 번호의 내용을 용어집(`g:named-models`, `g:hypotheses`)에 넣어 L2가 규칙·용어집만으로 닫히게 했다. 용어집이 따름정리 증명의 확인 내용까지 담는 것이 용어집의 범위로 괜찮은지.
4. **부록 A의 카드 열 삭제.** 분량 상한 때문에 ▣ 줄로 가리키게 했다. 한 표에서 카드까지 보고 싶다면 되돌리고 다른 곳을 줄여야 한다.
5. **묶음 이름 고정**(제안 7). 짧은 이름 4개를 새로 정했다. 확정 용어 목록에 넣을지.

## 7. HANDOFF에 고칠 문장 (고치지 않음)

- 3.4 "위험한 경로" 첫 항목: "하한 증명은 유한 단수에서 닫히지 않는다. 깊이 평균과 $\delta=1/L$ 장치 때문에 $L\to\infty$ 가 본질적이고, 논문에 'RS 하한'이나 '1RSB 하한'에 해당하는 중간 명제가 없다." → "논문에는 유한 단수에서 닫히는 하한 명제가 진술되어 있지 않다. 고정 $L$ 에서 있는 것은 잔차항이 붙은 부등식(`comparison.tex` 236–245)이고, 이 증명에서 잔차와 남는 오차 한계는 $L\to\infty$ 에서 0이 된다는 것만 증명된다(용어집 `g:rsb-steps` 쓰지 않는 뜻)." 뒤의 "여기서는 단순해지지 않는다"도 "단순해진다는 근거가 원문에 없다"로.
- 3.2의 6: "보조 계층의 깊이 $L$ 과 시행 법칙의 단수 $r$ 은 다른 것이다." → "원문은 장치를 $r=L-1$ 단으로 쓰지만(`cavity.tex` 16), 장치의 단수 $L-1$ 을 계의 물리적 RSB 단수로 읽는 것은 증명되지 않고, 정리의 $r$ 은 inf의 변수다."
- 3.2의 1(B-1)은 P6′ 행 추가로 이미 낡았다(이번 작업과 별개, 기록만).
