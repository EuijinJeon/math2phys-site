# 시범 v1 정확성 검토 (수 4: L2 §6, rules P6·P6′·P7)

검토 대상: `layers/L2.md` 212–437행(§6), `layers/rules.md` P6·P6′·P7 행(커밋 708f173). 대조: `git show 49d7ade:redesign/layers/{L2,rules}.md`, `source/sections/trees.tex`, `perturbations.tex`, `decorrelation.tex`, 카드 `x:tree-cancellation-example` 외. answer-key는 보지 않았다.

## 요약

- 지적 **10건**: 높음 0, **중간 1**, 낮음 9.
- **개정 전 단서는 하나도 빠지지 않았다**(아래 대조표 25항목 모두 개정본에 있음).
- 새 주 식, 정의, 단계 0–5, "anchor를 왜 상쇄하는가"는 원문과 맞는다. 과장, 증명되지 않은 부정, 금지된 동일시(Ruelle, GG, ultrametricity, pure state)는 §6에 없다.
- "(산수)" 계산 9개를 모두 손으로 다시 했고 맞았다. 따로 P6′ ①을 $L=2$, 3값 변수, 무작위 kernel·$D_1,D_2$·$G$ 로 수치 검산했다. old tree 둘($s=0,1$) 각각에서 $k=1$ 과 $k=2$ 모두 좌변(유한 차분)과 우변이 $10^{-7}$ 까지 맞았다($h^2$ 오차 수준). 작성자가 확인하지 않은 $k=2$ 도 여기서 확인됐다. 확인된 것: "현재 tree의 자식 수", "anchor path에서 fresh 가능", "우변은 원래 kernel".
- 단계 순서(P6′ 전개를 Taylor 계수 소거 앞에 둔 것)는 원문 논리와 맞다(아래 5절).
- 중간 1건: 6.2 ③의 "무엇이 작고 무엇이 균일한가" 표와 그 앞 "같은 차수" 문장이 $\lvert J_{\rm sep}\rvert$ 의 하한을 조건 $m_{d_v}\ge\eta$ 없이 적었다.

## 1. 단서 대조표 (개정 전 → 개정본)

| # | 개정 전 단서 (49d7ade §6) | 개정본 위치 | 판정 |
|---|---|---|---|
| 1 | prescribed tree는 공통 root와 깊이 $L$ 에서 끝나는 유한 labeled path | 6.1 설정 "tree" (229) | 있음 |
| 2 | 표본 규칙 두 성질(자식은 조건부 독립, leaf를 지워도 법칙 불변) | 6.1 설정 "tree 표본 규칙" (230) | 있음 |
| 3 | split 깊이 = 마지막 공통 vertex의 깊이 | 229 | 있음 |
| 4 | $R_S$ 정의, $\lvert S\rvert=2,1$, 희석 모형에는 모든 $R_S$ 가 필요 | 231 | 있음 |
| 5 | P6은 root가 주어진 조건부 항등식 | 251 첫 항목 | 있음 |
| 6 | $D$ 는 유계 실수 path 함수, $\lvert t\rvert\lVert D\rVert_\infty<1$ | 238–239, 252 | 있음(나머지 한계까지 더함) |
| 7 | $\gamma_\beta<0$ ($n_\beta\ge1$) | 236, 244 | 있음 |
| 8 | $n\to0$ 해석적 연속 없음, 유한 tree, 임의의 kernel 열 | 251, 254 | 있음 |
| 9 | 보조 계층은 무한 계층이 아니라 깊이 $L$ 의 유한 kernel 열 | 254 | 있음 |
| 10 | 수 4·5가 쓰는 것은 log 전개가 아니라 그 변형 | 218–219 표, 259 | 있음 |
| 11 | 재사용 $+1$ / fresh $\gamma_\beta<0$, $c_E$ 부호 섞임, 확률 가중치가 아님 | 278–287 | 있음 |
| 12 | anchor는 protected, 다시 고를 수 없음 | 285, 289 | 있음 |
| 13 | 혼합 미분에 factorial 없음 | 307, 단계 4 (410) | 있음 |
| 14 | $\kappa(S)$ 는 old tree와 무관, 처방은 reference path와의 split만, telescoping $m_{d+1}$, 일반 격자 | 313–321, 355 | 있음 |
| 15 | 계수 한계는 균등 격자에서만 | 335, 355 | 있음 |
| 16 | $C_{q,k}$ 는 $q,k$ 에만, $L$·지정 깊이와 무관 | 345, 359 | 있음(깊이 일치 무관까지) |
| 17 | 상대 한계와 조건 $m_{d_v}\ge\eta$ | 337–338 | 있음(표에서는 조건이 빠짐: 지적 1) |
| 18 | $\lvert J\rvert\sim\delta^b$, $L$ 에 균일한 양의 하한 없음 | 347 | 있음 |
| 19 | 상쇄 예: 부호 있는 합 $-\delta$, 절댓값 합 $2+\delta$, 미루면 $\delta$ | 331–333 | 있음 |
| 20 | P7은 선택된 수열 위, 고정 old tree·anchor 종류·$f$·새 replica 수·제약마다 | 373, 378–380, 419 | 있음 |
| 21 | 둘째 합은 anchor 하나뿐인 tree, $R_E$ 는 spin anchor이면 anchor 포함 | 381–382 | 있음 |
| 22 | 지정 범위: anchor와 color 집합 안의 쌍별 split(color끼리 포함), 일관된 한. old replica가 관여하는 쌍은 아님. mark 깊이 $1..L-1$ | 386, 421 | 있음 |
| 23 | 고정 $L$·tree·제약, 선택된 수열의 $N\to\infty$ 에서만. 율 없음. $L$ 균일성 주장 없음 | 419–420 | 있음(path 수, type까지 더함. `perturbations.tex` 311–312와 같음) |
| 24 | 계수의 극한 존재는 P5 (iii)이 준다(가정하지 않음). $t$ 는 전개 변수, $\mathbf u$ 는 고정값 | 408, 422, 377, 416 | 있음 |
| 25 | 수 5 입력은 항등식과 표본 규칙뿐. 수 5–6은 (2.3)(2.4)를 안 씀. Gibbs 계층 구조·overlap 극한값은 나오지 않음. 선행 연구와 꼴이 다름 | 429–435 | 있음 |

rules.md P6·P6′·P7 행의 옛 단서도 전부 새 행에 있다(P6: 해석적 연속 없음, 유한 kernel 열, 물리 이름은 intuition. P6′: 조건부·임의 kernel, 딸린 진술 넷, 균등 격자, 상수 의존성, $\lvert J\rvert$ 하한과 균일 하한 없음, 깊이 미루기는 P8 증명, 물리 대응 없음. P7: mark 깊이, 율·균일성 없음, §7 범위, P11 입력, 계층은 구성에 들어 있음).

## 2. 새 내용의 원문 대조

| 새 내용 (L2 행) | 원문 근거 | 판정 |
|---|---|---|
| 6.1 $Y$ 재귀, $K^A_d$, $E^A=E[\cdot W]$, $W_{\mathcal T}$ (233–236) | trees.tex 67–105 | 맞음 |
| 6.1 $Q_k$ 확률 $-\gamma_\beta/n$, telescoping, $Q_2$ 의 split 법칙 (242–244) | trees.tex 204–222 | 맞음 |
| 6.1 $A$ 는 위로 유계·0에서 떨어짐, 추가 변수 허용 (251, 253) | trees.tex 73–74, 135–140 | 맞음 |
| 6.1 나머지 $\sum_{k>K}c^k/k$ (252) | trees.tex 233–238 | 맞음 |
| 6.2 ① 주 식과 선택 표, 현재 tree, $n_\beta$ 시점 (265–287) | trees.tex 259–296 | 맞음(수치 검산으로도 확인) |
| 6.2 ① "규칙이 나오는 곳" (289) | trees.tex 180–202, 146–154, 241–248 | 맞음 |
| 6.2 ② $\kappa(S)$, 한 걸음 합 $m_d-jm_{d+1}$ (315–321) | trees.tex 337–385 | 맞음 |
| 6.2 ③ 주 식 둘, "unary에서 fresh가 $-\delta$" (335–339) | trees.tex 393–455 | 맞음(정의 범위는 지적 4) |
| 6.2 단서의 해석적 경계 균일성 (357) | trees.tex 156–176, 294–295 | 맞음 |
| 6.3 주 식, $R_E$, anchor 종류, $\mathcal C$ (373–382) | perturbations.tex 429–470 | 맞음 |
| 6.3 mark 선택 (386) | perturbations.tex 494–524 | 맞음 |
| 단계 0 | perturbations.tex 75–93, 316–329 | 맞음 |
| 단계 1 (Palm, $\Pi$, $\Xi$, 모든 type에 같은 함수) | perturbations.tex 331–381 | 맞음. "score $=g_0S_0/A$, anchor 인자 상쇄"는 368–370 그대로 |
| 단계 2 (계수는 모멘트와 모멘트 곱의 유한 결합, $N$ 과 무관) | perturbations.tex 399–405 | 맞음 |
| 단계 3 ($\Xi$ 로 균일 수렴, $\lvert\Xi(1/j)\rvert\le2Cj^{-j}$, 모순, $j$ 고정 후 $N\to\infty$) | perturbations.tex 390–424, 538–546 | 맞음 |
| 단계 4 (polarization, 인자가 mark 족 안) | perturbations.tex 474–492 | 맞음. $k^k/(2^kk!)$ 공식은 적지 않았지만 다시 유도해 확인함 |
| 단계 5 (selector, site 평균 $=R_E$, 일차결합) | perturbations.tex 494–535 | 맞음 |
| "anchor를 왜 상쇄하는가" (414) | perturbations.tex 368–377 | 맞음 |
| "두 매개변수의 역할" (416) | perturbations.tex 40–44 | 맞음 |
| "무엇이 작고 무엇이 균일한가" 표 (343–348) | trees.tex 400–455 | 하한 행의 조건이 빠짐(지적 1) |
| 기호 주의 (352) | decorrelation.tex 332–359 | 맞음(큰 $L$ 조건은 지적 5) |
| 6.4 수 5·6의 입력 (429–433) | decorrelation.tex 8–9, introduction.tex 75–77 | 맞음 |

### "(산수)" 계산 검산

| 위치 | 계산 | 결과 |
|---|---|---|
| 6.1 $L=2$ 예 (247–248) | $\frac1m\log K_1(1+tX)^m$ 을 2차까지 전개하면 $tK_1X-\frac{t^2}2[m(K_1X)^2+(1-m)K_1X^2]$. $Q_2$: 깊이 0 확률 $m$, 깊이 1 확률 $1-m$ | 맞음 |
| 예 1 (291–303) | history $1+s+1+2(L-1-s)=2L-s$ 개, 합 $1+m_0-2m_L=-1$. 좌변: 동차성으로 $Y_d=1+t$, $K^A=K$, $\frac{d}{dt}(1+t)^{-1}=-1$ | 맞음 |
| 예 2 (305) | $L=1$: $E^A[1/A]=1/\langle A\rangle$, 미분 $-\langle D\rangle$. 우변 $\gamma_{\rm root}=m_0-m_1=-1$ | 맞음 |
| $a'$ 가지 검산 (321) | $1+(m_{s+1}-1)=m_{s+1}$ | 맞음 |
| $\kappa$, $a_v=2$, $d=s$ (324) | $1+(m_s-2m_{s+1})+(m_{s+1}-1)=m_s-m_{s+1}$. $\sum_d(m_d-m_{d+1})=-1$ | 맞음 |
| $\kappa$, $a_v=3$ (325) | $(-\delta)(-(d+2)\delta)=\delta(m_d+2\delta)$ | 맞음 |
| 상쇄 예 (332–333) | $1+(s+2)\delta+(L-1-s)\delta=1+(L+1)\delta=2+\delta$. $(2+\delta)/\delta=2L+1$ | 맞음 |
| $\lvert J_{\rm sep}\rvert\le k^k\delta^{b_{\rm sep}}$ (347, 359) | $j\ge2$ 인자는 $\lvert m_d-jm_{d+1}\rvert=jm_{d+1}-m_d\le j\le a_v-1\le k$. 그런 인자 수는 $\sum_v(a_v-2)\le k-b$. 따라서 $\le k^{k-b}\delta^b$ | 맞음 |
| P7 두 path 예 (390–392) | 첫째 합 $\mathbb EX^2-\sum c_\ell\mathbb E[XX_\ell]$, 둘째 $-\delta\mathbb EX$. $\sum c_\ell=1+\delta$ 와 $X_\ell\overset{d}=X$ 로 $\tfrac12\sum c_\ell\mathbb E(X-X_\ell)^2=(1+\delta)\mathbb EX^2-\sum c_\ell\mathbb E[XX_\ell]=\delta\operatorname{Var}X+o(1)$. decorrelation.tex 264–286과 같음 | 맞음 |

## 3. 과장과 동일시

새 과장은 없다. 확인한 것:
- "상쇄는 고른 규약이 아니라 단계 1에서 저절로 생긴다"(414): 원문 368–370이 그대로 말한다. 다만 score를 $\partial_u\log$ 로 잡는 선택은 논문의 설계다(perturbations.tex 40–42). 그래서 "규약이 아니다"는 전개 쪽에만 해당한다. 문장은 참이므로 지적하지 않는다.
- "극한값은 식별되지 않는다"(422), "$L\ge2$ 에서 $\log Y_0$ 는 분배함수 비의 로그가 아니다"(255): 4.3절, P9 차이와 맞고 부정을 증명된 것처럼 말하지 않는다.
- "$\kappa(S)$ 의 부호는 topology만으로 정해진다"(317): 참이다(실은 $(-1)^k$).
- §6에 Ruelle, Ghirlanda–Guerra, stochastic stability, ultrametricity, pure state라는 이름은 없다.

## 4. 바꾼 기호

| 개정 기호 | 원문 | 본문의 대응 문장 | 판정 |
|---|---|---|---|
| $G$ | lemma `tree:extension-expansion` 의 $H$ | 273 "원문과 카드에서는 $H$", rules P6′ 차이 "$G$(원문의 $H$)" | 불완전함(지적 4): 원문 trees.tex 180–202, 299도 $G$ 를 쓴다. 거기서는 $D_j$ 를 흡수해 가는 함수이고 처음 값이 $H$ 다 |
| $b_{\rm sep}$, $J_{\rm sep}$ | `tree:charging` 의 $b$, $J$ | 352, rules P6′ | 정의 범위가 원문보다 좁음(지적 3) |
| $\Pi_{N,\mathcal T}$, $\Xi_N$ | $J_{N,\mathcal T}$, $H_N$ | 404 "$\Pi=J$, $\Xi_N=H_N$" | 맞음. $\Pi_{N,\mathcal T}=J_{N,\mathcal T}$ 로 첨자까지 적으면 더 정확하다. 원문 $\pi$(매개변수 측도)와 글자가 비슷하지만 L2 §6에는 $\pi$ 가 나오지 않는다 |

§7과의 관계: 7.2(465)의 "$J=\kappa(S^+)^2$, $b$ 는 $S$ 의 branching vertex 수, P6′ 의 상대 한계"는 352와 맞는다. decorrelation.tex 345–347에서 떨어진 vertex는 $2b$ 개이고, separation 깊이 $d$ 의 vertex는 old branching 깊이라 떨어진 vertex가 아니다. 그래서 $J_{\rm sep}=\kappa(S^+)^2$ 이고, 나머지 인자 $-\delta$ 는 항등식에 남는다(357–358). 어긋나는 것은 7.3(473)의 "P7의 두 번째 항등식"이다. 새 6.3은 항등식을 하나로 쓰고 anchor 종류로 나누기 때문이다(지적 8).

## 5. 단계 순서

원문에서 P6′ 은 두 번 쓰인다. (a) `pert:analytic` 의 증명(perturbations.tex 391–405): canceled-anchor 전개가 해석적 경계와 "각 Taylor 계수는 모멘트의 유한 결합"을 주고, 그 뒤에야 P5 (iii)의 수렴과 $j$ 논증으로 계수가 소거된다. (b) `pert:tree-identity` 의 증명(526–531): 혼합 전개, selector, site 평균이 나온다. 개정본의 단계 2(계수의 꼴) → 3(소거) → 4(polarization) → 5(selector)는 (a)와 (b)의 순서와 같다. 맞는 배치다. rules.md P7 차이 칸은 "Taylor 계수가 0으로 감을 보인 뒤 … P6′ ①로 풀고"라고 써서 (b)의 쓰임만 적었다. 틀린 말은 아니지만 L2와 순서가 달라 보인다(지적 9).

## 6. 지적 표

| # | 위치 | 문제 | 원문 근거 | 심각도 | 고칠 문장 |
|---|---|---|---|---|---|
| 1 | L2 343–348 표의 $\lvert J_{\rm sep}\rvert$ 행과 비 행, 339 "같은 차수" | 하한 $\delta^{b_{\rm sep}}\eta^{\sum_v(a_v-2)}$ 와 "비가 $L$ 에 균일하게 유계"를 조건 없이 적었다. 하한은 모든 떨어진 vertex에서 $m_{d_v}\ge\eta$ 일 때만 선다. 반례: $d_v=0$ 이면 $j=2$ 인자가 $2\delta$ 라서 $\lvert J\rvert$ 가 $\delta^{b}$ 보다 작다. 표는 따로 읽히도록 만든 것이라 앞 문단의 조건이 전해지지 않는다 | trees.tex 410, 449–455 | 중간 | 표 머리 아래에 "(아래 둘째·넷째 행은 떨어진 vertex 모두에서 $m_{d_v}\ge\eta>0$ 일 때)"를 넣는다. 339는 "…이것은, 그 vertex들에서 $m_{d_v}\ge\eta$ 이면, 같은 vertex들의 $\kappa$ 인자 $J_{\rm sep}$ 와 같은 차수 $\delta^{b_{\rm sep}}$ 다($\eta$ 에 의존하는 상수배까지)." |
| 2 | L2 324 "셋(재사용, 깊이 $s$ 에서 fresh, $a'$ 가지에서 fresh)", 331 "허용되는 history는 위의 셋이다" | 셋은 종류의 수다. history는 $1+1+(L-1-s)=L+1-s$ 개다. 이 절은 예 1의 표에 개수를 세어 두었으므로, 독자가 history를 셋으로 세면 절댓값 합 $2+\delta$ 를 재현하지 못한다 | trees.tex 319–325 | 낮음 | 324: "세 종류(재사용 1개, 깊이 $s$ 에서 fresh 1개, $a'$ 가지에서 fresh $L-1-s$ 개)의 합". 331: "허용되는 history는 위의 세 종류, 모두 $L+1-s$ 개다." |
| 3 | L2 335 $b_{\rm sep}$ 정의, 352 "원문의 $b$, $J$ 다", rules P6′ ③ | 원문은 "그런 vertex 가운데 $b$ 개"(임의의 부분집합)이고, 개정본은 "그런 vertex 전부의 수"다. 참을 잃지는 않지만 원문보다 좁다. 상대 한계는 떨어진 vertex 전부에서 $m_{d_v}\ge\eta$ 를 요구하게 되는데, 원문은 조건이 맞는 부분집합만 골라 써도 된다 | trees.tex 397–399, 406–410 | 낮음 | 352: "$b_{\rm sep}$, $J_{\rm sep}$ 는 원문의 $b$, $J$ 에서 떨어진 vertex를 모두 고른 경우다(원문은 그 가운데 임의의 $b$ 개를 골라도 된다)." |
| 4 | L2 273 "(원문과 카드에서는 $H$)", rules P6′ "$G$(원문의 $H$)" | 원문 trees.tex 180–202, 299도 $G$ 를 쓴다. 거기서는 미분할 때마다 $D_j/A$ 를 흡수해 커지는 함수이고 처음 값이 $H$ 다. 원문을 펴는 독자는 두 $G$ 를 섞을 수 있다 | trees.tex 183, 299–301 | 낮음 | 273: "(lemma `tree:extension-expansion` 의 $H$. 원문 trees.tex 180–202의 $G$ 는 미분할 때마다 $D_j/A$ 를 흡수해 가는 함수로, 처음 값이 이 $H$ 다)" |
| 5 | L2 352 "거기서는 떨어진 vertex가 $2b$ 개" | 원문은 $L$ 이 충분히 클 때만 그렇다고 한다(정규성으로 밀린 깊이가 old branching 깊이와 달라진다) | decorrelation.tex 339, 345–347 | 낮음 | "거기서는 $L$ 이 충분히 크면(η-정규성으로) 떨어진 vertex가 $2b$ 개이고 …" |
| 6 | L2 220 표 "6.3 받는 것", 371 | 받는 것에서 4.2절 섭동족의 구조가 빠졌다: Poisson 개수(단계 1), $t_\nu=1/j$, $u_\nu\in[j^{-j},2j^{-j}]$(단계 3), 곱과 polarization 평균에 닫힌 유리수 mark 족(단계 4–5). 6.2 ①의 균일 해석적 경계(단계 3)도 빠졌다. 단계 본문은 이것들을 쓴다 | perturbations.tex 28–65, 391–397 | 낮음 | 371: "받는 것은 P5의 (ii)·(iii), 4.2절의 섭동족(Poisson 개수, type 매개변수, mark 족), 6.2 ①의 전개와 균일 해석적 경계다." |
| 7 | L2 214 "유한 tree 위의 정확한 계산 두 개(P6, P6′)" | P6′ ③은 등식이 아니라 부등식이다 | trees.tex 400–414 | 낮음 | "유한 tree 위의 계산 두 개(P6은 정확한 전개, P6′ 은 정확한 전개와 계수 한계)" |
| 8 | L2 473 (§7.3) "P7의 두 번째 항등식" | 새 6.3은 항등식 하나를 쓰고 anchor 종류로 나눈다. "두 번째"가 무엇인지 §6에서 찾을 수 없다(개정 전부터 있던 표현이지만 이제 어긋남이 드러난다) | perturbations.tex 429–470, decorrelation.tex 532–567 | 낮음 | "marker anchor($S_0=1$)로 쓴 P7의 항등식을 쓰면 …" |
| 9 | rules P7 차이 칸 "그 Taylor 계수가 모두 0으로 감을 보인 뒤 … P6′ ①로 풀고" | P6′ ①은 소거 앞(계수의 꼴과 해석적 경계)에도 쓰인다. L2 단계 2–3과 순서가 달라 보인다 | perturbations.tex 391–405 | 낮음 | "… 바꾸고, P6′ ①로 계수의 꼴과 해석적 경계를 얻어 그 Taylor 계수가 모두 0으로 감을 보인 뒤(…), 혼합 미분을 P6′ ①로 풀고 polarization과 mark selector로 제약을 고른다." |
| 10 | rules.md 49 "확신이 낮은 대응" P6′ 항목 | "물리 규칙 칸만 보면 시험함수 $H$ … 상수의 정확한 의존성, $\lvert J\rvert$ 의 크기와 상대 한계를 말하지 않지만"이 새 행과 어긋난다. 새 물리 칸은 $G$, 상수의 $L$ 무관성, 상대 한계를 말한다(작성자도 적어 둠) | — | 낮음 | 해당 문장을 "물리 규칙 칸은 주 식 셋과 상수의 $L$ 무관성을 말하고, color 순서·해석 영역·$\lvert J_{\rm sep}\rvert$ 의 크기는 차이 칸에 둔다"로 바꾼다 |

## 7. 그 밖에 확인한 것 (지적 아님)

- 6.3의 $\mathbb E$ 항목(377)은 "선택된 $\mathbf u_j$ 로 고정, 새 삽입 없음"을 함께 말한다. 따라서 "원래 법칙"이 섭동 없는 계로 읽힐 위험은 본문 안에서 막혀 있다. 원칙 0.8($\mathbf u$ 는 고정값)을 지킨다.
- 6.4의 "수 6은 P6을 직접 쓴다(P11)"는 개정 전 rules P7 차이 칸(comparison.tex 13–15, 195–245)과 맞는다.
- §6 끝의 "이 절이 쓰는 규칙"에 P8, P9, P11이 더해졌다. 6.4가 이 규칙들을 가리키므로 맞다.
