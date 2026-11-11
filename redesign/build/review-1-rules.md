# 검토 1 — rules.md / L1.md / L0.md

대상: `layers/rules.md`, `layers/L1.md`, `layers/L0.md`. 기준: `source/sections/*.tex`.
확인 범위: introduction, model, overview, cavity, upper, perturbations, trees, comparison, reduction, consequences는 전문을 읽었다. decorrelation은 진술(1–140행, 141–165행, 230–356행, 525–625행)과 라벨 목록만 읽었고, 귀납 증명 본문(357–524행)은 읽지 않았다. 인용된 라벨은 스크립트로 전부 tex에 존재함을 확인했다.

## 요약 표

| rule | 판정 | 문제 요약 |
|---|---|---|
| P1 | 수정 필요 | 가설 누락($\lvert b\prod f_\ell\rvert<1$, $f_\ell$ i.i.d., $b\perp f$, "모든 $n\ge1$"). 차이 칸의 "factorization은 상한에만 쓰인다"는 틀림(F2). |
| P2 | 수정 필요 | 진술·상수는 맞음. "부호는 볼록성과 positivity에서만 나온다"는 과장(factorization과 독립 구조도 필요). |
| P3 | 통과 | $(\log2)N^{3/4}$, $[1/2,3/2]$, $s_N$ 모두 일치. "pressure"가 power-mean 뒤의 $P_N$이라는 표기 보강만. |
| P4 | 통과 | 증분 식, Poisson$(\alpha p)$/Poisson$(\alpha(p-1))$, $\rho_N$, 가정 모두 일치. |
| P5 | 수정 필요 | 규칙 문장의 "근처로 유지"는 양쪽 주장인데 tex는 상한뿐. (iii) 모멘트 수렴, "reservoir에서"가 빠짐. |
| P6 | 수정 필요(가벼움) | $\gamma_\beta$, 수렴 영역 일치. "power mean = Ruelle cascade 평균", "cascade에서 뽑은 tree"는 인용 노드가 증명하지 않는 동일시인데 `exact`로 표시. |
| P7 | 수정 필요 | "원하는 branching pattern"은 과장(제약은 anchor와 새 색 사이에만). "나머지 replica의 시험함수"도 부정확. |
| P8 | 수정 필요(가벼움) | 평균·극한 순서는 맞음. 선택된 부분수열, reservoir, $d$가 첫 split 이전이라는 제한이 차이 칸에 없음. |
| P9 | 수정 필요(가벼움) | 식·극한 순서·singleton 예외 일치. 부분수열과 $\eta$의 지위가 빠짐. |
| P10 | 통과 | `comp:encoding`, `comp:single-label-moments`와 일치. |
| P11 | 수정 필요(가벼움) | 식·오차·극한 순서 일치. "상관 감쇠가 아니라"는 부정확. 필수 노드 누락(`cavity:identity`, `tree:log-expansion`, `decor:overlap-concentration`). |
| P12 | 통과(대응 보강) | $\alpha D+d$, $\alpha(2p-1)D+d$, $-\alpha\mathbb Ec$ 일치. 대칭화 단계를 P12에 숨긴다면 `main:theorem` 증명을 노드로 넣어야 함. |

건수: 틀림 1, 과장 7, 유형 오류 1, 대응 오류 1, 구멍 2, 표기 2.

## 발견 (심각도 순)

### F1 [과장] L0, P1 — 정리의 가설이 빠져 있다
- 주장: L0 "가정은 factor weight가 $e^\theta=a(1+b\prod_\ell f_\ell(s_\ell))$ 로 전개되고 $\mathbb E[(-b)^n]\ge0$ 이라는 것". P1도 같은 두 조건만 적는다. R5도 독립 구조를 말하지 않는다.
- tex: `model.tex:26-37` — "$\lvert b\prod_{\ell=1}^p f_\ell(s_\ell)\rvert<1$ a.s. … the $f_\ell$ are independent copies of one random function, $b$ is independent of them, and $\mathbb E[(-b)^n]\ge0\ (n\ge1)$". 정리는 "Under \eqref{model:integrability}--\eqref{model:positivity}"(`model.tex:131`)이다.
- 왜 문제인가: 엄격한 곱 한계와 독립 구조는 상한 증명에서 쓰이고(`upper.tex:25-34`의 본질적 유계성, `upper.tex:110-114`의 $P^p$, $PB^{p-1}$, $B^p$ 분해), 순열 불변성에도 쓰인다(`reduction.tex:56-58`). 지금 문장대로면 논문보다 넓은 모형 류에 대해 정리를 주장한다.
- 수정안(L0, P1 공통): "…$e^\theta=a(1+b\prod_\ell f_\ell(s_\ell))$, 단 a.s. $\lvert b\prod_\ell f_\ell\rvert<1$, $f_\ell$ 은 한 무작위 함수의 독립 사본, $b$ 는 $f_\ell$ 들과 독립, $a>0$ 은 임의($\log a$ 적분 가능성 불요), 그리고 모든 $n\ge1$ 에 대해 $\mathbb E[(-b)^n]\ge0$."

### F2 [틀림] rules.md P1 차이 칸 — "factorization은 상한(P2)에만 쓰인다"
- 주장: "짝수 $p$, factorization, positivity는 상한(P2)에만 쓰이고, 하한은 bounded이며 입력 순열에 대해 불변인 상호작용 법칙만 요구한다".
- tex: bounded 하한에 대해서는 맞다(`cavity.tex:11-14` "Neither the factorization nor the positivity assumption is used in the lower bound", `overview.tex:46-48`). 그러나 정리의 하한은 factorization을 쓴다: `reduction.tex:46-58` "the original interaction law need not be permutation invariant … Independence and identical distribution of the $f_\ell$, and their independence of $b$, show that the law of $\widehat\theta$ is invariant under permutations of its inputs."
- 같은 파일의 "곱셈 인수 $a$ 제거" 항목과 L1 수 7이 이 단계를 인정하므로 P1 차이 칸이 자기 문서와도 어긋난다.
- 수정안: "짝수 $p$ 와 positivity는 상한(P2)에만 쓰인다. factorization은 상한에 쓰이고, 하한 쪽에서는 한 번, $c=\theta(1,\ldots,1)$ 을 뺀 법칙을 순열 불변으로 만드는 데 쓰인다(`main:theorem` 증명). 그 뒤의 bounded 하한(`comp:bounded-lower`)은 bounded이고 순열 불변인 법칙만 요구한다."

### F3 [구멍] L1 수 7 — 순열 불변성이 P1에서 나오지 않는다
- 수 7은 "상수를 빼 $a$ 를 없애고 순열 불변으로 만든 뒤"라고 하고 P1, P12를 든다. 순열 불변성은 $f_\ell$ i.i.d.와 $b\perp f$ 에서 나오는데(`reduction.tex:56-58`) P1에 그 가설이 없다(F1). 원래 $\theta$ 의 법칙은 순열 불변이 아닐 수 있다(`reduction.tex:46-47`).
- 수정안: F1대로 P1에 독립 구조를 넣고, 수 7에 "순열 불변성은 $f_\ell$ 의 i.i.d.와 $b$ 의 독립에서 나온다"를 한 구절 추가.

### F4 [구멍] L1 수 3, 6 — $\varepsilon$, $\eta$ 와 극한의 조립이 빠졌다
- 주장: 수 3 "$\Delta_{N_j}\le\liminf F_N+2\varepsilon$", 수 6 "수 3과 합치면 $\liminf F_N\ge\inf_r\Phi_r$".
- tex 조립(`comparison.tex:233-245`): 고정 $\varepsilon$, 고정 $L$ 에서 $A\le\underline F+2\varepsilon+\limsup_N\lvert\Delta_N-\mathcal B_{L-1}\rvert$, 그다음 $L\to\infty$, 마지막에 $\varepsilon\downarrow0$. 수열은 $L$(과 $\varepsilon$)마다 다르다(`comparison.tex:8-12`). $\eta$ 는 $L\to\infty$ 뒤에 0으로 보낸다(`comparison.tex:153-156`).
- L1에는 $\varepsilon$ 의 정의도, $\varepsilon\downarrow0$ 도, 부등식 사슬 $\inf_r\Phi_r\le\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\le\Delta_N+\lvert\cdot\rvert\le\underline F+2\varepsilon+\lvert\cdot\rvert$ 도 없다. 부등식 방향 자체는 맞다.
- 수정안(수 6 끝): "고정한 $\varepsilon,L$ 에서 $\inf_r\Phi_r\le\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\le\liminf F_N+2\varepsilon+\lvert\Delta_N-\mathcal B_{L-1}\rvert$. $N\to\infty$(그 $L$ 의 수열), $L\to\infty$, $\varepsilon\downarrow0$ 순으로 보낸다."

### F5 [과장] L0 마지막 문장 — ground state
- 주장: "…가정하지 않으며, 그 결과 $\beta\to\infty$ 에서 ground-state 에너지 밀도(SAT에서는 위반 clause 최소 개수)도 같은 변분식으로 주어진다."
- tex: `consequences.tex:86-100` — `models:spin`, `models:sat` 두 모형에 한해 $g=\lim_N N^{-1}\mathbb E\max_\sigma\mathcal E_N$ 이 존재하고 $g=\lim_{\beta\to\infty}\beta^{-1}\inf\mathcal B_{r,\beta}$, 괄호 안은 $[g,g+\log2/\beta]$. "For unit-weight SAT, the limiting expected minimum number of violated clauses per variable is $-g$."
- 문제: (1) 일반 모형 류가 아니라 이름 붙은 두 모형에 대한 따름정리다. (2) "그 결과"가 "가정하지 않는다"에 걸려 있어 인과가 틀리다. 근거는 본 정리와 $g_N\le P_N/\beta\le g_N+\log2/\beta$ 다. (3) "같은 변분식"이 아니라 각 $\beta$ 의 변분값을 $\beta$ 로 나눈 것의 극한이다. (4) SAT는 변수당, 기대값, 단위 가중치.
- 수정안: "따름정리로, 대칭 coupling 짝수 $p$-spin 모형과 soft 짝수 $K$-SAT에서는 $\frac1N\mathbb E\max_\sigma\mathcal E_N$ 의 극한 $g$ 가 존재하고 $g=\lim_{\beta\to\infty}\beta^{-1}\inf_{r,\zeta,\mathbf m}\mathcal B_{r,\beta}$ 다(단위 가중치 SAT에서 $-g$ 는 변수당 위반 clause 최소 개수의 기대값 극한)."

### F6 [과장] P2 차이 칸 — "에서만 나온다"
- 주장: "그 부호는 짝수 $p$ 에서 $x\mapsto x^p$ 의 볼록성과 $\mathbb E[(-b)^n]\ge0$ 에서만 나온다."
- tex: `upper.tex:62-67`(세 삽입이 모두 $a(1+D)$ 꼴), `upper.tex:110-114`(독립 index, $f$ 의 독립 사본, "The inserted $b$ is independent of these variables"). 나머지항 `upper:remainder`의 꼴 자체가 factorization과 독립 구조에서 나온다.
- 수정안: "나머지항은 factorization과 $f_\ell$, $b$ 의 독립 덕에 $-\frac{\lambda^n}{n}\mathbb E[(-b)^n]\,\mathbb E[P^p-pPB^{p-1}+(p-1)B^p]$ 꼴이 되고, 부호는 짝수 $p$ 의 볼록성과 positivity가 정한다." (L1 수 1의 "음이다"는 "0 이하"가 정확.)

### F7 [과장] P7 — "원하는 branching pattern", "나머지 replica"
- tex: `perturbations.tex:434-436` "A constraint $\mathcal C$ prescribes any consistent collection of their pairwise split depths, involving only the added colors and the anchor. It imposes no extra restrictions involving the other old replicas." 시험함수는 "bounded polynomial $f$ in multioverlaps of its old replicas"(`perturbations.tex:316-317`)로, anchor를 포함한 old tree 전체의 것이다. mark의 깊이는 $1,\ldots,L-1$ 뿐이다(`perturbations.tex:29`).
- 수정안: "…새 섭동의 효과는 old tree의 overlap 시험함수 $f$ 와 분리된다. 깊이별 mark로 anchor와 새로 붙는 replica들 사이의 split 깊이를 지정할 수 있다(다른 old replica와의 관계는 지정하지 못한다)."

### F8 [과장] P5 — "근처로 유지", (iii) 누락
- tex: `perturbations.tex:260` "(i) $\Delta_{N_j}(\mathbf u_j)\le\underline F+2\varepsilon$" — 상한뿐이다. (ii)는 "in the reservoir"(262행). (iii) 모든 유한 tree의 multioverlap 곱 기대값이 수열을 따라 수렴(263-265행)하고, `pert:analytic`이 이것을 쓴다(406행).
- 수정안(규칙 문장): "…cavity 증분이 $\liminf F_N$ 을 거의 넘지 않으면서, reservoir의 모든 perturbation score가 self-average하고 유한 tree의 multioverlap 모멘트가 수렴하는 크기 수열과 매개변수를 고를 수 있다."

### F9 [유형 오류] P6 — `exact` 안에 증명되지 않은 동일시
- 주장: "계층 평균(power mean = Ruelle cascade 평균, R13) … cascade에서 뽑은 replica tree".
- tex: `trees.tex:7-12` "…the latter uses cascade weights introduced by Ruelle. Here we derive the needed identities directly for finite sequences of arbitrary probability kernels, without assuming an infinite hierarchy." 인용 노드는 kernel 열에 대한 항등식만 세우고 cascade와의 동일시는 증명하지 않는다.
- 수정안: 규칙 문장을 "power mean 안에 넣은 섭동의 효과는 tilted kernel로 뽑은 replica tree에 대한 전개이고…"로 하고 유형 `exact` 유지. cascade/Parisi block 이름은 차이 칸에 `intuition`으로 옮긴다. (확인한 것: $\gamma_\beta$ `trees.tex:95`, $Q_k$ 규칙 `trees.tex:213-214`, 수렴 영역 `trees.tex:231`.)

### F10 [과장] P8, P9, P11 — 부분수열, $\eta$, "상관 감쇠가 아니라"
- P8/P9 차이 칸은 $\lim_L\limsup_N$ 을 적지만, $N$ 극한이 P5의 선택된 수열(매 $L$ 다름)을 따른다는 것과 대상이 섭동된 reservoir라는 것을 적지 않는다(`decorrelation.tex:4-8`). $\eta>0$ 는 고정이고(`decorrelation.tex:69`), P8의 $d$ 는 "strictly before its first split"(243행)이다.
- P11 "독립성의 근거는 국소 tree 구조나 상관 감쇠가 아니라": 국소 tree 구조를 쓰지 않는다는 것은 맞다. 그러나 P9는 P8(site 쌍 평균 조건부 공분산의 소멸)에서 나오므로 "상관 감쇠가 아니라"는 틀리게 읽힌다.
- 수정안: P8/P9 차이 칸 끝에 "모든 $N$ 극한은 P5가 $L$ 마다 고른 수열을 따르고, 대상은 섭동된 reservoir다. $\eta>0$ 는 고정한다." P11은 "…근거는 국소 tree 구조나 그래프 거리에 따른 상관 감쇠가 아니라…".

### F11 [과장] L1 수 4 — "유일한 입력"
- tex: `decorrelation.tex:8-9` "The argument uses only these identities and the tree sampling rules". 계수 합과 charging(`tree:reference-total`, `tree:charging`)도 쓴다(`decorrelation.tex:333-352`).
- 수정안: "이 항등식들과 tree 표본 규칙·계수 한계(P6)가 수 5의 입력이다." 수 5의 규칙에 P6 추가.

### F12 [대응 오류] 누락 노드
- P11: 증명이 직접 기대는 `cavity:identity`, `tree:log-expansion`, `decor:overlap-concentration`, `tree:regular-shapes`가 행에 없다(`comparison.tex:141-153, 195, 205`).
- P12: 대칭화 단계를 "P12에 숨는다"고 했으면 `main:theorem`(증명 `reduction.tex:45-87`)을 노드에 넣어야 한다.
- P5: `cavity:negligible`(평균 증분의 liminf), `cavity:increment`(증분의 균일 유계)를 쓴다(`perturbations.tex:271-279`).

### F13 [표기] P3, L1 수 2
- $P_N^{L,\mathbf u}$ 는 섭동된 계의 pressure가 아니라 power-mean 재귀 뒤의 "expected root logarithm"이다(`cavity.tex:34-35`). 수 2의 "$F_N$ 은 그대로다"는 "$P_N/N-F_N\to0$"이 정확하다. "bounded"는 0에서도 떨어져 있다는 뜻($1/2\le\psi\le3/2$)임을 밝힐 것.

### F14 [표기] 자기완결성 — 정의 없는 기호·용어
- L1: $\alpha$, $p$, $\zeta$, $\mathbf m$(R3, R11, R12를 가리키지 않음), $\varepsilon$, $\eta$, $\mathcal A_{L,\eta}$, $Q_k$(R18 미지시), $Y_{0,\rm s}$, $Y_{0,\rm b}$(R20 미지시), $\mathbf m^{(L)}$, "perturbation score", "mark", "prescribed tree", "reservoir".
- rules.md: $\underline F$(P5), $t$, $D$(P6), $c_E$, $E$, $f$, "anchor", "extension history", "type"(P5, P7), $\rho_N$ 의 값, $K$, $M$, $a$(P11의 label 수; P1의 곱셈 인수 $a$ 와 충돌), $C_k$, $\mathbf m^{(L)}$, $\mathcal M_L$(R11은 $\mathcal M_{r+1}$), "perturbation score"(역할 표에 없음), "tilt".
- L0: $r=0$ 에서 $\mathbf m$ 과 $T_0$ 가 없다는 것, $0<m_1<\cdots<m_r<1$ 의 범위가 빠짐. 나머지 기호는 정의됨.

## L1 닫힘 (수별)

1. 닫힘. `upper:bound`와 일치(`upper.tex:12-14`), 모든 $N$, 모든 $r\ge0$. "음"은 "0 이하"(F6).
2. 닫힘. 식과 가정 일치(`cavity.tex:38-54`). 표현은 F13.
3. 닫힘(P5를 blackbox로 받으면). $\varepsilon$ 미정의(F4). P5가 P3, P4를 쓴다는 것은 숨어 있다(F12).
4. 닫힘. 제약의 범위는 F7, "유일한 입력"은 F11.
5. 닫힘. 결과 식이 `decor:overlap-concentration`과 일치. decorrelation 귀납 본문은 읽지 않았으므로 P8→P9 내부는 진술 수준에서만 확인.
6. 부등식 방향은 맞음. 극한 조립이 빠짐(F4). P9, P4를 "수 5", "수 2"로만 부르고 규칙 목록에는 없음.
7. P1에 독립 구조가 없어 닫히지 않음(F3). 그 밖의 조립은 `reduction.tex:61-86`과 일치: truncate된 법칙에는 하한만 적용하고, 상한은 원래 법칙에 수 1을 적용한다.

저자 개요(`overview.tex`)의 4단계와 L1의 수 2–6은 순서와 내용이 대응한다. 물리판에 없는 논리 단계는 F3, F4 둘이다.

## L0

- 표시된 식은 `main:formula`와 `model:functional`을 합친 것과 같다(`model.tex:112-116, 134`). $-\alpha(p-1)$, $\log2$, Poisson$(\alpha p)$ 일치.
- 가설 누락(F1), ground state 문장(F5), $r=0$ 과 $\mathbf m$ 범위(F14).
- "Panchenko–Talagrand의 등식 추측 해결", 포함되는 세 모형, "가정하지 않는다" 목록은 확인됨(`introduction.tex:24-31, 75-77`, `model.tex:138-140`).

## 표시된 네 주장

- (a) RSB 계층은 보조 구성이고 물리적 Gibbs 상태의 ultrametricity는 가정도 증명도 하지 않는다 — **확인**. `introduction.tex:75-77` "Their branching is part of the construction; no ultrametric organization of the physical Gibbs states is assumed." "증명하지 않는다"는 읽은 범위의 어떤 진술에도 그런 주장이 없다는 뜻에서 확인(`model.tex:138-140`).
- (b) 짝수 $p$, factorization, 부호 조건은 상한에만 쓰인다 — **부분 확인**. 짝수 $p$ 와 positivity는 확인(`upper.tex:123-125`, `cavity.tex:13-14`). factorization은 하한 쪽 대칭화에도 쓰인다(`reduction.tex:46-58`, F2). "하한은 bounded·순열 불변만 요구"는 `comp:bounded-lower`에 한해 확인(`comparison.tex:226-230`). 홀수 $p$ 에서도 하한이 선다는 말은 논문에 없다($p$ 는 처음부터 짝수로 고정, `model.tex:3`).
- (c) 하한에서 Parisi parameter를 최적화하지 않는다 — **확인**. `cavity.tex:16-19` "$m_d=d/L$", `comparison.tex:161-162` "$\mathbf m^{(L)}=(1/L,\ldots,(L-1)/L)$".
- (d) 이웃 cavity field의 독립은 multioverlap 집중과 균일 무작위 site 선택에서 온다 — **확인(표현 한 곳 수정)**. `comparison.tex:99-120`: 경험 분포 $\pi$ 와 $\bar\pi=\mathbb E\pi$, $\lVert\pi^{\otimes a}-\bar\pi^{\otimes a}\rVert_{\rm TV}\le\frac a2\sum_S\lvert R_S-\mathbb ER_S\rvert$. 그래프의 국소 구조는 쓰이지 않는다. "상관 감쇠가 아니라"는 F10대로 고칠 것. 논문이 "국소 tree 구조를 쓰지 않는다"고 직접 말하는 문장은 없고, 증명에 쓰이지 않는다는 데서 읽은 것이다.

## 확정 전에 사용자가 직접 봐야 할 것

1. L0와 P1의 가설 목록(F1): `model.tex:26-44`와 나란히 놓고 볼 것.
2. P1 차이 칸과 주장 (b)(F2): factorization이 하한 쪽 대칭화에 쓰인다는 점을 어떻게 적을지.
3. L1 수 6의 극한 조립(F4): `comparison.tex:233-245`.
4. L0의 ground state 문장(F5).
5. P6–P9에서 "Ruelle cascade", "상태", "GG 항등식"이라는 물리 이름을 규칙 문장에 둘지 차이 칸으로 내릴지(F9, 그리고 rules.md의 "확신이 낮은 대응").
6. decorrelation 귀납 증명 본문(`decorrelation.tex:357-524`)은 이 검토에서 읽지 않았다.
