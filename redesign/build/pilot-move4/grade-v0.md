# 채점 v0: 수 4 독자 시험 (Sonnet, Haiku)

채점 대상: `reader-v0-sonnet.md`, `reader-v0-haiku.md`. 두 독자가 읽은 글: `/tmp/reader-in-v0/` 의 L0, L1, L2, rules, glossary. 기준: `answer-key.md`.
행 번호는 `/tmp/reader-in-v0/` 의 파일 기준이다. L2 §6은 다음 행에 있다: 6.1 = 216–226 (P6 = 222–224), 6.2 = 228–240 (도입 230, 전개 232, 모양별 총합 234, 계수 한계 236, "왜 필요한가" 238), 6.3 = 244–256 (P7 246–248, 처방 250, 성립 범위 252, "어디서 오는가" 254), 6.4 = 258–262. rules.md의 P6′ 은 22행, P7은 23행이다.

**채점 관례 두 가지.**
- rules.md와 glossary도 독자에게 준 글이다. 그래서 L2에 없고 rules나 glossary에만 있는 내용이라도 독자가 그 위치를 정확히 짚었으면 "글에 적혀 있음"으로 인정했다. L2에 없다는 사실은 결함 목록에 따로 올렸다.
- 3번은 계산 문항이라 "추론" 말고는 정직한 출처 표시가 있을 수 없다. 그래서 쓴 규칙(선택지, 계수, $n_\beta$, $m_0,m_L$)이 글에 있고 계산이 맞으면 2점을 줬다.

**독자가 자기 지식으로 메운 곳이 있는지 확인했다.** "글에 적혀 있음"이라고 표시한 주장을 원문에서 하나씩 찾아봤다. 실제로는 없는데 "적혀 있음"이라고 한 경우는 핵심 답에서 나오지 않았다. 아래 세 군데는 표시만 지나쳤고 점수는 깎지 않았다.
- Sonnet Q7: 수 2에서 P3·P4를 받는다고 쓰고 "글에 적혀 있음"으로 표시했다. §6 본문은 P3·P4를 인용하지 않는다. L2 §1.3이 수 2–3을 묶어 (P3, P4, P5)라고 적은 데서 끌어온 것으로 보인다.
- Haiku Q2: $n_\beta$ 의 시점 근거로 glossary g:extension-history와 g:tree-coefficient(326–352행)를 함께 들었다. 그런데 그 시점을 적은 곳은 rules.md 22행뿐이다.
- Haiku Q1: "혼합 미분은 이 순서 있는 확장 규칙 그대로"를 L2 230행이라고 했다. 실제로는 232행이다.

---

## 1. 점수표

| 문항 | Sonnet | 이유 | Haiku | 이유 |
|---|---|---|---|---|
| 1 주 식 | **1** | 식과 좌변(tilt된 법칙, $H/A^{a_*}$, $\boldsymbol t=0$ 혼합 미분)은 정확하고 rules 22행을 짚었다. 그러나 우변이 **섭동 없는 원래 법칙**의 기대값이라는 핵심을 말하지 않았다. | **1** | 식은 맞고 rules 22행을 짚었다. 마찬가지로 우변이 원래 법칙이라는 점이 빠졌고, $a_j(E)$ 는 "찾지 못함"이라고 했다. |
| 2 $c_E$ | **2** | 두 선택지, $+1$/$\gamma_\beta$, 곱을 모두 맞게 썼다. $n_\beta$ 가 그 걸음 시점의 현재 tree(old 포함)에서 센 자식 수라는 것을 rules 22행에서 정확히 짚었다. | **2** | 내용이 같고 $n_\beta$ 의 시점도 맞다. 덧붙여 $\sum_\beta(-\gamma_\beta)=2$(잎 수)라는 정규화 확인도 했다. 출처 표시는 조금 장황하지만 위치는 맞다. |
| 3 계산 | **2** | history $2L-s$ 개를 나열했고, 갈라지는 vertex에서 $n=2$, 총합 $-1$, 좌변 $-1$ 이 모두 맞다. 상수 $A$ 에서 kernel이 변하지 않는다는 것을 g:insertion과 g:power-mean의 동차성에서 끌어냈다. 모양별 합과 $2+\delta$ 도 재현했다. | **2** | history 표, $2L-s$, telescoping 합 $1+m_0-2m_L=-1$, 좌변 $-1$ 이 모두 맞다. 좌변 단계(정규화된 tilt 기대값)는 "내가 가정"이라고 표시했지만 글의 recursion에서 끌어낼 수 있다. |
| 4 anchor | **2** | Palm 항등식으로 $J_{N,\mathcal T}$ 와 $J_{N,\{a_*\}}$ 를 거쳐 $H_N$, Taylor 계수, P6′, P7의 두 합으로 가는 사슬을 $H=f$ 판과 anchor 하나 판까지 연결했다. "왜 anchor만 상쇄하나"는 추론이라고 정직하게 표시했고, 그 추론(score $=\partial_u\log A$ 가 anchor path 위의 값)도 방향이 맞다. | **1** | Palm 항등식 → $H_N$ → Taylor → P6′ → P7 사슬은 맞다. 그러나 좌변이 P7에서 $H=f$ 인 old tree 판과 anchor 하나 판이 된다는 대응을 말하지 않았다. 상쇄 이유는 "회계상의 편의"라고 추측했는데 틀린 방향이다(오해 목록 M1). |
| 5 $\kappa(S)$ | **2** | "모양 $S$ 를 갖는 모든 history의 $c_E$ 합"과 telescoping으로 $m_{d+1}$ 이 된다는 것을 썼다. $\kappa=m_d-m_{d+1}=-\delta$ 도 맞다. $a_v$ 는 추론이라고 표시했고 Q3의 직접 합으로 확인했다. | **2** | 같은 답이다. $a_v=2$ 는 "추측"이라고 표시했지만, $d<s$, $d=s$, $d>s$ 세 경우를 직접 세어 독립으로 확인했다. |
| 6 P7 | **2** | $f$, $R_E$, $c_E$, 두 합의 범위, "분리된다"는 뜻, 선택된 수열 위의 고정 $L$·tree·제약, 율 없음, 균일성 없음을 모두 정확히 썼다. | **2** | 같다. 모든 요소가 L2 246–252행에 있다. |
| 7 흐름 | **2** | P5 (ii)·(iii)과 P6·P6′ 이 수 4 안에서 쓰인다는 것, 그리고 P7, tree 표본 규칙, $\kappa$·계수 한계, 확률 부등식을 수 5로 넘긴다는 것을 썼다. 수 2(P3·P4) 표시는 조금 과장했다(위 참고). | **2** | P5 (ii)·(iii)을 받고, P7과 tree 표본 규칙(260행 인용)과 $\kappa$·계수 한계를 넘긴다고 썼다. P6·P6′ 을 "받는 것"으로 따로 들지는 않았지만 넘기는 쪽에 들어 있다. |
| 8 계수 한계 | **2** | $\sum\lvert c_E\rvert\le C_{q,k}\delta^b$ 와 그 조건, $\lvert J\rvert\sim\delta^b$ 이며 균일한 하한이 없다는 것, $L$ 에 균일한 것은 비율 $\le C_{q,k,\eta}$($m_{d_v}\ge\eta$)라는 것을 맞게 썼다. 236행의 문장을 두고 고민했다(D9). | **2** | 같다. glossary의 $\delta^{2b}$($J=\kappa(S^+)^2$)를 함께 인용했지만 섞어 쓰지는 않았다. |
| **합** | **15 / 16** | | **14 / 16** | |

두 독자 모두 1번에서 1점을 잃었고, 이유가 같다. Haiku는 4번에서도 1점을 잃었다.

---

## 2. 글의 결함 목록 (심각도 순)

[공통]은 두 독자가 모두 막혔거나 실패한 곳이다.

| # | 위치 | 무엇이 없거나 혼란스러운가 | 이어지는 문항 | 고칠 방향 |
|---|---|---|---|---|
| D1 [공통] | L2 §6.2, 230–232행 | P6′ 의 **식이 L2에 없다**. 말로만 쓰여 있고, 식은 rules 22행의 "차이" 칸 긴 문장 속에만 있다. $H$, $D_j$, $A_{\boldsymbol t}$ 도 L2에서 소개되지 않는다($A_{\boldsymbol t}$ 만 §1.5-2에 있다). | Q1, Q2, Q3 | 230행에 좌변과 우변이 다 들어간 식을 넣고 $H$, $D_j$, $A_{\boldsymbol t}$ 를 한 줄씩 정의한다. |
| D2 [공통] | L2 §6.2, rules 22행, glossary g:protected-leaf 341행 | 좌변 $E^{A_{\boldsymbol t}}_{\mathcal T}$ 는 tilt된 법칙이고 우변 $E_{\mathcal T_E}$ 는 **섭동 없는 원래 법칙**이다. 이 대비가 어디에도 적혀 있지 않다. $E^A_{\mathcal T}$ 표기도 정의되지 않는다(glossary에 기호만 있다). 두 독자 모두 이 핵심을 빠뜨렸다. | Q1(두 독자 모두 1점) | 식 바로 아래에 "좌변은 $A$ 로 바뀐 kernel·밀도 아래, 우변은 원래 kernel 아래의 기대값"이라고 적는다. |
| D3 [공통] | L2 §6.1 224행, §6.2 232행 | "$n_\beta$ 는 자식 수"가 **어느 tree, 어느 시점**의 자식 수인지 L2에 없다(rules 22행에만 있다). Q3의 계산이 이것으로 갈린다($d=s$ 에서 $n=2$). | Q2, Q3 | 232행에 "그 걸음의 현재 tree(안 쓴 old path와 이미 붙인 path 포함)에서 센 자식 수"를 넣는다. |
| D4 [공통] | L2 §6.2 238행, §6.3 254행, glossary g:protected-leaf 343행 | **왜 anchor의 인자만 상쇄하는가**가 설명되지 않는다. score가 anchor path 위의 $\partial_u\log A$ 이므로 Palm 단계에서 $H/A^{a_*}$ 가 나온다는 연결이 빠졌다. glossary의 한 구절("Palm 단계에서 … 이 상황")만 있다. 한 독자는 "찾지 못함 / 회계상 편의"라고 썼고, 다른 독자는 직접 추론했다. | Q4(Haiku 1점, M1) | 254행에 "score $D_\nu$ 는 anchor path 위의 $\partial_u\log A$ 이므로 $\mathbb E[fD^{a_*}]$ 가 $H/A^{a_*}$ 꼴의 tilt 기대값이 된다"는 한 문장을 넣는다. |
| D5 [공통] | L2 §6.3 254행("어디서 오는가") | 한 문단에 Palm, $u\ll t^n$, Taylor, P5(iii), P6′, polarization, selector가 몰려 있다. $H_N(t_\nu,u_\nu)$ 와 $J_{N,\mathcal T}$ 는 L2에서 정의되지 않는다(glossary 376행). 그래서 P6′ 좌변이 $H=f$ 판과 anchor 하나 판의 두 번 쓰인다는 대응이 보이지 않는다. | Q4 | 단계를 번호로 나누고, $H_N=J_{N,\mathcal T}-\mathbb Ef\,J_{N,\{a_*\}}$ 와 "각각의 $t$-계수가 P6′ 좌변($H=f$ / $H=1$, anchor 하나 tree)"이라고 명시한다. |
| D6 [공통] | L2 §6.2 234행, glossary g:tree-coefficient 326행, g:topology 242행 | $\kappa(S)$ 식의 $a_v$ 가 **어디에도 정의되지 않는다**. $\operatorname{Br}(S)$, $d_v$ 는 g:topology의 기호 칸에만 있다. 두 독자 모두 $a_v=2$ 를 추론하거나 추측했다. | Q5, Q8 | 234행에 "$\operatorname{Br}(S)$ = $S$ 의 branching vertex, $a_v$ = 그 자식 수, $d_v$ = 그 깊이"를 넣는다. |
| D7 [공통] | L2 §6.2 232행 vs rules 22행 | "혼합 미분 … 추가 factorial이 붙지 않는다"(L2)와 "$D_j=D$ 이면 $t^k$ 계수는 우변$/k!$"(rules)가 서로 어긋나 보인다. 두 독자 모두 다시 읽었다. | Q1 | 한 문장으로 잇는다: "혼합 미분에는 factorial이 없고, 모두 같은 $D$ 일 때의 $t^k$ Taylor 계수는 그것을 $k!$ 로 나눈 것이다." |
| D8 [Sonnet] | L2 §6.2 238행 | "$-\delta$ 대 $2+\delta$" 예의 **설정이 적혀 있지 않다**(두 old leaf, anchor가 그중 하나, 처방 split 깊이 $=$ old split 깊이). 설정은 glossary g:depth-delay 392행에만 있다. 좌변을 직접 계산한 예도 없다. 독자는 이 예를 역산해서 "내부 vertex"의 범위를 맞췄다. | Q3, Q5 | 238행에 설정을 넣고, 그 예를 Q3 꼴의 짧은 표(history, 계수, 합)로 보여 준다. 두 leaf 합 $-1$ 과 좌변 $\frac{d}{dt}(1+t)^{-1}=-1$ 도 넣는다. |
| D9 [Sonnet] | L2 §6.2 236행 | "$C_{q,k}$ 는 $L$ 에 무관"과 "균일한 것은 이 비율뿐이다"가 충돌하는 듯 읽힌다. "$b$ 개의 깊이가 old tree의 어느 branching 깊이와도 겹치지 않으면"이 무엇과 무엇을 비교하는지(old 깊이 집합인지, 처방 vertex끼리인지)도 모호하다. | Q8 | "비율뿐"을 "$\lvert J\rvert$ 에는 균일 하한이 없으므로, $J$ 로 나눈 뒤 $L$ 에 균일하게 유계인 것은 비율이다"로 바꾼다. "겹침"은 "old tree branching 깊이 집합과 같은 깊이"로 쓴다. |
| D10 [Sonnet] | L2 §6.2 234행 | "reference가 없는 old 부분 tree의 계수 합이 $m_{d+1}$ 로 telescoping"이 "old tree와 무관"의 유일한 근거다. 그런데 어느 vertex 아래 어떤 history의 합인지 알 수 없다. Sonnet은 두 leaf 예를 직접 풀어서야($1-(L-1-s)\delta=m_{s+1}$) 이해했다. | Q5 | 두 leaf 예로 한 줄 보인다: "깊이 $s$ vertex의 다른 자식 아래: 재사용 $+1$ 과 fresh 합 $(m_{s+1}-1)$ 을 더하면 $m_{s+1}$." |
| D11 [Haiku] | L2 §6.1 224행 | "붙이는 **확률**은 tree 계수 $\gamma_\beta$ 로 정해진다"고 쓰는데 바로 다음 문장이 $\gamma_\beta<0$ 이다. 확률은 $-\gamma_\beta/n$ 이다(glossary g:tree-law 335행). 바로 뒤 §6.2의 "$c_E$ 는 확률 가중치가 아니다"와 겹쳐 혼란을 준다. | Q2 | "확률 $(n_\beta m_{d_\beta+1}-m_{d_\beta})/n=-\gamma_\beta/n$"으로 고친다. |
| D12 [Sonnet] | L2 §6.1 218행, §6.2 232행 | "내부 vertex"에 자식이 하나인(unary) vertex가 들어가는지, 깊이 범위가 $0..L-1$ 인지 적혀 있지 않다. 반면 g:topology는 unary vertex를 지운다고 해서 반대로 읽힐 수 있다. Q3의 history 수가 이것으로 정해진다. | Q3 | 218행에 "path는 깊이 $0..L$ 의 모든 깊이에 vertex를 갖고, 내부 vertex는 깊이 $0..L-1$ 의 모든 vertex(unary 포함)"라고 적는다. |
| D13 [공통] | L2 §6.2 232행, §6.3 250행 | "color", "old replica를 **다시 쓴다**", "현재 tree / old tree / 확장 tree"가 본문에서 정의 없이 섞인다(glossary g:extension-history 349행에만 있다). $a_j(E)$ 와 $\mathcal T_E$ 는 glossary 기호 칸에 기호만 있고 뜻이 없다. | Q1, Q2 | 232행에 "새 replica = color $j$; 재사용 = color $j$ 를 old leaf에 준다; $\mathcal T_E$ = 마지막 tree; $a_j(E)$ = color $j$ 의 leaf"를 한 줄로 넣는다. |
| D14 [공통] | L2 §6.3 246–254행, glossary g:tree-identity 383행 | P7 식의 둘째 합 지표 $E'$ 가 정의되지 않는다. $\mathcal C$ 와 $\mathfrak E(\mathcal T,a_*,\mathcal C)$ 는 glossary에만 있다. "anchor 종류"(spin/marker)는 본문에서 정의 없이 나온다. polarization은 어디에도 정의가 없다. | Q6, Q4 | 식을 $\mathfrak E(\cdot)$ 표기로 쓰고, anchor 종류를 한 줄로 정의한다. polarization은 무엇을 하는지(곱 $\prod D_j$ 를 multioverlap 하나씩으로 떼어 내는 것) 한 줄로 적는다. |
| D15 [Sonnet] | L2 전체 | 기호가 겹친다. $b$: §6.2(겹치지 않는 처방 vertex 수), §7.2(S의 branching vertex 수), (2.3)의 계수. $J$: §6.2의 $J\sim\delta^b$ 와 §7.2의 $J=\kappa(S^+)^2\sim\delta^{2b}$ 가 같은 글자다. $H$: Hamiltonian, 시험함수, $H_N(t,u)$. $D$ 와 score $D_\nu$ 의 관계는 설명이 없다. $E$: history, 기대값, $E'$. | Q8, Q4 | §6.2의 $J$·$b$ 를 다른 글자로 바꾸거나 §7.2와의 관계를 적는다. score $D_\nu$ 가 $D_j$ 의 특수한 경우라면 그렇다고 적는다. |
| D16 [Haiku] | L2 §6 전체 | 경계값 $m_0=0$, $m_L=1$ 이 §6에 없다(glossary g:parisi-parameters 142행에만 있다). Q3과 telescoping에 필요하다. | Q3, Q5 | 6.1 끝에 "tree 계산에서는 $m_0=0$, $m_L=1$"을 넣는다. |
| D17 [Haiku] | L2 §7.2 294행 (수 5, 범위 밖) | $S^+$ 와 "깊이 연속성"이 정의 없이 나온다. | (Q7 주변) | v1 범위 밖이지만 기록해 둔다. |

---

## 3. 오해 목록 (독자가 틀리게 이해한 것)

빈칸보다 위험한 것만 모았다. 출처 표시가 정직한 추론이라도 내용이 틀리면 여기에 넣었다.

- **M1 (Haiku, Q4).** anchor를 처음부터 protected로 두는 것을 "회계상의 편의"로 읽었다. 이것은 틀렸다. 상쇄는 선택이 아니다. score $D_\nu$ 가 anchor path 위의 $\partial_u\log A$, 곧 $\partial_uA/A$ 이기 때문에 Palm 단계에서 $1/A^{a_*}$ 가 저절로 생긴다(glossary g:protected-leaf 343행 "Palm 단계에서 anchor 인자 $A^{a_*}$ 가 상쇄되는 것이 이 상황"). 독자는 이 문장을 인용하지 않았다. 이렇게 읽으면 anchor를 빼는 일이 임의 규약처럼 보이고, P7에서 anchor만 특별한 이유를 잃는다. → D4.
- **M2 (두 독자, Q1).** 오해라기보다 빠진 이해다. 두 독자 모두 우변 $E_{\mathcal T_E}$ 를 "확장된 tree 위 기대값"으로만 읽었고, 그것이 **섭동 없는** 법칙이라는 점을 놓쳤다. 이렇게 읽으면 우변도 tilt된 법칙의 기대값이라고 생각할 수 있다. 그러면 P7에서 극한 $\mathbb E[fR_E]$ 가 원래 reservoir 법칙의 모멘트(P5(iii))로 들어간다는 연결이 끊긴다. → D2.
- **M3 (Sonnet, Q4·Q6, 가벼움).** "$D_j^{a_j}$ 들의 곱이 $R_E$ 로 가는 것은 polarization과 mark selector로"라고 썼다. 글(254행)은 polarization과 selector가 **제약을 고른다**고만 한다. 곱 $\to$ multioverlap 변환이라는 역할 분담은 독자가 짐작한 것이고 글로 확인되지 않는다. 출처 표시는 "찾지 못함"으로 정직했다. → D14.
- **M4 (Haiku, Q7, 가벼움).** "수 4가 수 6에 P6의 log 전개를 넘긴다"고 썼다. 수 6이 P6을 쓰는 것은 맞다(L2 §8.2 336행). 그러나 이것은 수 4의 출력이 아니다. 유한 tree 항등식을 직접 다시 쓰는 것이다. 흐름도로 읽으면 수 4가 수 6의 입력을 공급한다는 잘못된 의존이 생긴다. 출처는 "추론"이라고 표시했다.
- **M5 (Haiku, Q2, 가벼움).** $n_\beta$ 시점의 근거로 glossary 두 항목을 함께 들었다. 그런데 거기에는 시점이 적혀 있지 않다. glossary만 다시 보는 독자는 "자식 수"를 old tree 기준으로 되돌려 읽을 위험이 있다. → D3.

그 밖에 확인한 것: Sonnet이 Q8의 "균일한 것은 이 비율뿐"을 "$C_{q,k}$ 는 균일하지 않다"로 읽을 뻔했지만 스스로 맞게 풀었다(D9). Haiku는 glossary의 $\lvert J\rvert\ge c\,\delta^{2b}$ 를 인용했지만 §6.2의 $J$ 와 섞어 쓰지 않았다(D15). 두 곳 모두 오해로 굳지는 않았다. 그러나 v1에서 다시 확인할 지점이다.
