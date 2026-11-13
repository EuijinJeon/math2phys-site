# 닫힘 시험 판정 — 2026-11-13

판정자: Claude Opus. 입력: 독자 A(Claude Sonnet, `build/closure-reader-A-2026-11-13.md`, 원본 `/tmp/closure-reader-A.md` 그대로 복사), 독자 B(GPT, `/tmp/closure-reader-B-astra.md`). 두 독자는 `layers/rules.md`, `glossary.md`, `L0.md`, `L1.md` 만 읽었다. 판정자는 그 넷에 더해 원문 `source/sections/*.tex` 과 카드(`tree.extension-expansion`, `x.tree-extension-history`, `x.tree-differentiation-rule`, `tree.charging`, `x.reduction-power-mean-scaling`)를 대조했다. 카드는 다른 에이전트가 지금 고치고 있으므로 카드 인용은 오늘 오후 시점의 내용이다. 이 보고서는 규칙·L1·카드를 고치지 않는다. 아래 "초안"은 모두 [제안]이다.

판정 용어:
- **닫힘**: 규칙·용어집 문장만으로 수가 추론된다.
- **블랙박스로 닫힘**: 규칙 문장이 결론을 진술하고, 증명은 `rules.md` "규칙으로 못 옮긴 것"의 묶음에 숨는다. 묶음 이름을 적는다.
- **구멍**: 수가 쓰는 입력이 규칙 표에도 "못 옮긴 것"에도 제자리가 없거나, 규칙 문장이 원문과 어긋난다.

---

## 1. 요약

| 수 | 최종 판정 |
|---|---|
| 1 상한 | 블랙박스로 닫힘(P2; 묶음 "상한의 정규화"). |
| 2 reservoir와 증분 | 블랙박스로 닫힘(P3, P4). P3은 power mean 단조·동차성이 규칙에 한 줄 있으면 직접 검산된다(원문 `tree:insertion` 에 진술 있음). |
| 3 선택된 수열 | 블랙박스로 닫힘(P5; 묶음 "score 집중의 증명"). A가 요구한 "좋은 $N$ 의 양의 밀도"는 원문에 필요 없다(A의 틀린 추론). |
| 4 prescribed-tree 항등식 | (i) 블랙박스로 닫힘(P7). (ii) P5·P6→P7은 블랙박스로 닫힘(묶음 "Taylor 계수 추출"). 그러나 L1이 "계수 한계(P6)"라고 적은 것은 **구멍**이다: P6에 그 내용이 없다. P6′ 로 메운다. |
| 5 multioverlap 집중 | (i) 블랙박스로 닫힘(P8, P9). (ii) P6·P7→P8·P9는 지금 문구로는 **구멍**이다. 계수 입력(extension 전개, $\kappa$, charging)이 규칙 표 밖에 있다. P6′ 를 더하면 입력은 메워지고, 조립은 묶음 "깊이 미루기"(`decor:J-*` 부분), "잎 개수 귀납과 사영", "marker anchor", "깊이 방향 연속성", "깊이 평균의 회계"로 닫힌다. |
| 6 독립 cavity message | 블랙박스로 닫힘(P11 포함; 묶음 "깊이 평균의 회계", "나머지 절단과 부호화의 측도론"). P11 문장에 $\varepsilon$ 이 빠져 있어 양화사 보충이 필요하다(L2 전에 필수). |
| 7 일반화와 맞붙이기 | 블랙박스로 닫힘(P1, P2, P12; 묶음 "곱셈 인수 $a$ 제거와 대칭화"). power mean 성질 한 줄이 있으면 P12 균일성까지 직접 검산된다. |

두 독자는 실질에서 갈리지 않는다. B의 "Pass"는 모두 "선언된 규칙을 블랙박스로 받으면"이라는 뜻이다(B 머리말과 "open items" 3, 4). A의 "구멍"은 한 단계 아래, 곧 규칙에서 규칙을 유도하는 (ii) 수준에 대한 것이다. 원문으로 보면 두 판단이 다 맞다. 다만 A는 그 과정에서 원문보다 강한 결론을 세 군데 끌어냈다(2.3절).

---

## 2. 수별 채점표

### 수 1 — 상한 (P1, P2)

| 항목 | A | B | 원문 대조 |
|---|---|---|---|
| 추론 | P2를 블랙박스로 받고 부호 구조를 검산했다. | 같다. | `upper.tex` 119–127: 나머지항 (upper:remainder), "Since $p$ is even, convexity …", positivity가 부호를 준다. 두 독자 모두 맞다. |
| 원문보다 강한 결론 | 없음 | 없음 | — |
| "규칙 밖에서 필요" | $U_\theta$ 의 식. A는 $\log\sum_s e^{\theta(s,\varepsilon)}\prod q_{x_\ell}(s_\ell)$ 로 채웠다. | $r=0$ 규약을 식으로. | $U_\theta$: `model.tex` 59–63에 A가 채운 식 그대로 있다. 용어집 `g:site-term` 은 말로만 적었다. **실제 빈칸이고 A의 채움은 맞다.** $r=0$: `model.tex` 118–120 "the operators $T_d$ are omitted". L0에 말("$\mathbf m$ 과 $T_0$ 는 없다")은 있고 식은 없다. **실제 빈칸이다(표기 수준).** |
| 판정 | 블랙박스로 닫힘 | Pass | **블랙박스로 닫힘.** |

### 수 2 — reservoir와 증분 (P3, P4)

| 항목 | A | B | 원문 대조 |
|---|---|---|---|
| 추론 | P3을 "단조 + 상수 이동 등변"이면 검산된다고 봤다. P4는 개수만 검산했다. | P3, P4를 받고 $\rho_N$ 주의를 짚었다. | `cavity.tex` 36–38: "Comparing pointwise with the unperturbed spin weight and then applying the recursion". 이 단계가 쓰는 성질은 `tree:insertion` 마지막 문단(`trees.tex` 112–115)에 진술되어 있다: "The recursion is monotone and homogeneous: if $a\le A\le b$, for positive root-measurable $a,b$, then $a\le Y_d\le b$ …". |
| 원문보다 강한 결론 | 없음 | 없음 | — |
| "규칙 밖에서 필요" | (1) $A_{\rm s}$, $A_{\rm b}$ 의 식, (2) reservoir $K_d$ 구성, (3) $s_{N+1}\ne s_N$ 의 처리. | $Y_0$ 가 보통 Gibbs log 비가 아니라는 주의. | (1) `cavity.tex` 59–68에 있다. 용어집 `g:site-bond-insertion` 에는 말만 있다. 조립에는 필요 없고 검산에만 필요하다. (2) `g:hierarchy`·`g:insertion`·`trees.tex` 54–64가 다룬다. 용어집으로 충분하다(A가 덜 읽었다). (3) `cavity.tex` 87–94 "$O(N^{-1/4})$". A의 채움이 원문과 같고, P4의 $o(1)$ 안에 들어 있으므로 규칙에 따로 둘 필요가 없다. B의 $Y_0$ 주의는 맞다: `cavity.tex` 56–58 "The insertion recursion uses the tilted reservoir kernels". $L\ge2$ 에서 $\log Y_0$ 는 $\log(Z'/Z)$ 가 아니다. |
| 판정 | 블랙박스로 닫힘 | Pass | **블랙박스로 닫힘.** power mean 성질 한 줄(4절 항목 1)과 L1 $Y_0$ 표기(항목 7)를 권한다. |

### 수 3 — 선택된 수열 (P5)

| 항목 | A | B | 원문 대조 |
|---|---|---|---|
| 추론 | (i)을 점별 $\Delta_N$ 의 망원합으로 설명한 뒤 "(i)–(iii)를 동시에 만족하려면 좋은 $N$ 들의 양의 밀도가 필요"하다고 했다. | P5 그대로 받았다. | `perturbations.tex` 269–301: (a) $\liminf_N\frac1N\int P_N\,d\pi=\underline F$ 에서 **매개변수 평균한** 증분 $\int\Delta_N\,d\pi\le\underline F+\varepsilon$ 인 $N$ 이 무한히 많다. (b) 평균 score 집중(`pert:concentration`)은 **모든** $N\to\infty$ 에서 성립하므로 그 무한집합 안에서 $N_j$ 를 충분히 크게 고른다. (c) Markov로 좋은 집합 $G_j$ 의 보집합 측도 $\le j^{-2}$, $G_j$ 위 조건부 평균 증분 $\le\underline F+2\varepsilon$ 에서 한 점을 고른다. (d) 대각 부분수열로 (iii). |
| 원문보다 강한 결론 | **있음.** 양의 밀도는 필요 없다. 무한히 많은 $N$ 으로 충분하다. 또 원문의 망원합은 점별 $\Delta_N(\mathbf u)$ 가 아니라 $\pi$-평균 증분에 대한 것이다. | 없음 | 규칙 문장이 원인일 수 있다: P5 차이 칸은 "집중은 먼저 매개변수 평균으로 증명되고, Markov 부등식으로 한 점을 고르며"라고만 적어서, 낮은 증분도 매개변수 평균으로 먼저 찾는다는 것이 빠져 있다. |
| "규칙 밖에서 필요" | 양의 밀도. | 없음 | 필요 없다(위). 표기 충돌 지적($j$ 가 type 지수이자 수열 지수)은 맞다. 원문 자체가 겹쳐 쓴다(`perturbations.tex` 44–49의 $j$ 와 279–284의 $N_j$, $\nu\le j$). |
| 판정 | 블랙박스로 닫힘 | Pass | **블랙박스로 닫힘.** P5 차이 칸에 선택 기구 한 줄(항목 3)을 권한다. |

### 수 4 — prescribed-tree 항등식 (P6, P7)

| 항목 | A | B | 원문 대조 |
|---|---|---|---|
| 추론 | (i) P7 블랙박스면 닫힘. (ii) P5·P6→P7은 구멍: canceled-anchor 전개, Palm, Taylor 소거, polarization이 규칙 밖. | P7을 선언된 입력으로 받아 Pass. | P7 차이 칸이 부호 있는 합의 꼴을 진술하므로 (i)은 닫힌다. (ii)의 Palm·analytic·polarization은 "못 옮긴 것"의 "Taylor 계수 추출" 묶음에 이미 있다. 따라서 그 부분은 블랙박스로 닫힌다. 남는 것은 canceled-anchor 전개(`tree:extension-expansion`) 자체다. P6 노드 칸에 이름은 있지만 P6 문장은 $\log$ 전개와 $Q_k$ 만 말한다. P7은 "$c_E$ 는 P6의 tree 계수"라고 적는데, $c_E$ 는 $\gamma_\beta$ 와 old leaf 재사용 계수 $+1$ 의 곱이다(`trees.tex` 259–276). 정의는 용어집 `g:extension-history` 에만 있다. |
| 원문보다 강한 결론 | 없음(수 4 안에서는). | 없음 | — |
| "규칙 밖에서 필요" | (1) 전개 진술과 조합 인자, (2) Palm, (3) Taylor 소거, (4) polarization. `tree:reference-total` 의 old tree 무관성 이유는 확인하지 못했다. | 없음 | (1) **실제 빈칸이다** → P6′. 조합 인자는 원문에 있다: 혼합 미분은 순서 있는 확장 규칙 그대로이고 "there is no additional factorial"(`perturbations.tex` 491–492). $D_j=D$ 이면 $t^k$ 계수는 우변$/k!$ 이다(`trees.tex` 290–292). (2)–(4)는 묶음에 있다(A가 블랙박스 경계를 너무 낮게 잡았다). reference-total의 이유: `trees.tex` 359–375. reference를 담지 않은 old 부분 tree(깊이 $d+1$ 에서 시작, leaf $q$ 개)의 선택 계수 합이 telescoping으로 $q+\sum_\beta\gamma_\beta=m_{d+1}$ 이 되어 old tree 모양이 지워진다. 원문에 있으니 P6′ 차이 칸에 넣는다. |
| 규칙 문장의 문제 | L1 수 4 "이 항등식과 tree 표본 규칙·계수 한계(P6)가 수 5의 입력의 전부다": (a) P6에는 계수 한계가 없다. (b) "전부"는 L1 수 5 자신의 문장("수 4의 항등식, tree 표본 규칙, 유한 tree 조합, 모형과 무관한 확률 부등식뿐")보다 좁고 원문보다 강하다. `decorrelation.tex` 8–9 "uses only these identities and the tree sampling rules"는 모형에서 받는 입력을 말한 것이다. §7은 그 밖에 §3의 조합(`tree:reference-total`, `tree:charging`)과 확률 부등식(`decor:contractions`, martingale)을 쓴다. | | |
| 판정 | (i) 닫힘 / (ii) 구멍 | Pass | **(i) 블랙박스로 닫힘(P7). (ii) 블랙박스로 닫힘(Taylor 계수 추출). 규칙 인용의 구멍 1건**(L1 "계수 한계(P6)"; 전개 진술이 규칙 표 밖). P6′ 로 메운다. |

### 수 5 — 모든 multioverlap의 집중 (P6, P8, P9)

| 항목 | A | B | 원문 대조 |
|---|---|---|---|
| 추론 | (i) P8·P9 블랙박스. (ii) 구멍: 전개, $c_E$ 연결, charging, $\kappa$ 의 이유, P7→P8 조립. | P8·P9를 선언된 정리로 받아 Pass. 내부 증명은 감사할 수 없다고 명시했다. | `decorrelation.tex` 236–513(조건부 공분산 귀납), 524–612(marker anchor). 조립이 쓰는 것: 항등식(P7), `tree:reference-total`(331–413의 $\kappa(S^+)$), `tree:charging`(348–350), `decor:contractions`, `decor:depth-continuity`, `decor:fiber-bound`. |
| 원문보다 강한 결론 | **있음(P6′ 초안 (e)에서).** (1) "$\lvert J\rvert\ge c_{k,\eta}>0$". 원문은 $\lvert J\rvert\ge c_{k,\eta}\delta^{2b}$(`decorrelation.tex` 336–341, (decor:J-lower-bound))이고 `tree:charging` 에서는 $\lvert J\rvert\ge\delta^b\eta^{\sum_v(a_v-2)}$(`trees.tex` 449–455)다. $L$ 에 균일한 양의 하한은 없다. 균일한 것은 비율 $\frac1{\lvert J\rvert}\sum\lvert c_E\rvert$ 뿐이다. marker 단계도 "no uniform lower bound as $L\to\infty$ is needed"(568–569)라고 쓴다. (2) "각 새 split이 인자 $\delta$ 하나를 내고 부호 있는 합은 $-\delta$, 절댓값 합은 $2+\delta$". 두 계산이 섞였다. $-\delta$ 대 $2+\delta$ 는 미루기 **전**의 예이고, 미루면 절댓값 합이 $\delta$ 가 된다(`trees.tex` 317–329). (3) "$\eta$-regular한 모든 target에서". charging의 조건은 $\eta$-regular가 아니라 (가) 지정 vertex의 깊이가 old tree의 branching 깊이가 아님, (나) $m_{d_v}\ge\eta$ 다. | 없음 | 규칙 문장 쪽 원인: 용어집 `g:depth-delay` 기호 칸이 $J=\kappa(S^+)^2$ 와 상대 비용만 적고 $\lvert J\rvert$ 의 크기를 적지 않는다. 독자가 $J$ 를 $O(1)$ 로 읽기 쉽다. |
| "규칙 밖에서 필요" | $J$ 로 나누기, 합 범위, 상수 의존성. $\eta$-regular 모호. singleton 불일치. L1 "각 고정 깊이" 오독. | 없음 | $J$·상수: **실제 빈칸이다** → P6′. $\eta$-regular: 원문 `decorrelation.tex` 21–28 "the normalized depths of distinct branching vertices differ by more than $\eta$". 서로 다른 두 vertex 모두(조상 관계 여부와 무관)이고, 용어집 문장도 같다. 원문은 모호하지 않다. 용어집에 "모든 쌍"을 넣으면 오독을 막는다. 추가 prefix 깊이와 aligned 사본 조건은 용어집에 원문대로 있다(A가 놓쳤다). singleton: 용어집 `g:conditional-decorrelation` 이 이미 "이때는 더 강하게 각 고정 $L$ … $\limsup_Nv_N\le1/(\eta L)$"라고 적는다(`decorrelation.tex` 283–289). 불일치가 아니다(A가 놓쳤다). "각 고정 깊이": 원문 82행의 문구 그대로지만 대상은 $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$ 의 $\operatorname{Var}(M)\to0$(각 고정 $L,S,e$; 563–566)뿐이다. 최종 결론은 깊이 평균이다. **오독 위험은 실제로 있다** → 항목 6. |
| 판정 | (i) 블랙박스 / (ii) 구멍 | Pass | **(i) 블랙박스로 닫힘(P8, P9). (ii) 지금은 구멍**(계수 입력이 규칙 표 밖이고, L1이 그것을 P6으로 잘못 인용한다). P6′ 뒤에는 블랙박스로 닫힌다(묶음: 깊이 미루기의 `decor:J-*` 부분, 잎 개수 귀납과 사영, marker anchor, 깊이 방향 연속성, 깊이 평균의 회계). |

### 수 6 — 독립 cavity message로 바꾸기 (P4, P5, P6, P9, P10, P11)

| 항목 | A | B | 원문 대조 |
|---|---|---|---|
| 추론 | 연쇄 부등식은 규칙만으로 검산된다. P11은 블랙박스여야 한다(P9·P10·P6에서 유도하면 정규화 $A=z(1+D)$, 절단 순서, shape 지배 부등식이 빠진다). | P11을 받아 Pass. "Without P11 this would be a real gap". | `comp:bounded-lower`(`comparison.tex` 226–246)가 L1 표시식과 같다. `comp:insertion-comparison` 증명(198–223): $K\le M$ 절단, $C=H+BM$, $A=z(1+D)$, $\lvert D\rvert\le c=\tanh C$, "first choose $M$ …, then $q$ …, and then take the limits in $N$ and $L$". A가 채운 exact 부분(독립 label이면 terminal 평균이 $V_{\rm s}$, bond는 label 군마다 power mean을 통과해 인수분해)은 `comparison.tex` 170–185와 같다. |
| 원문보다 강한 결론 | 없음 | 없음 | — |
| 두 독자가 갈린 곳 | A: "P9만 블랙박스로는 부족하고 P9와 P11이 블랙박스여야 닫힌다". | B: P11 수용으로 Pass. | 같은 판단이다. B도 P11 없이는 구멍이라고 말한다. 원문으로 보아도 P11의 증명은 P9·P10·P6만으로 서지 않는다: 정규화와 절단(묶음 "나머지 절단과 부호화의 측도론"), $Q_k$ 평균을 $\mathcal A_{L,\eta}$ 로 누르는 `tree:assignment-probability`·`comp:shape-error-bound`(묶음 "깊이 평균의 회계")가 더 든다. **두 수준 (i)은 P11까지 블랙박스로 받아야 닫힌다.** |
| "규칙 밖에서 필요" | $\varepsilon$ 이 P8·P9·P11 문장에 없다. | 없음 | 맞다. `comparison.tex` 8–11 "Fix $\varepsilon>0$. At each depth $L\ge2$, use the sequence … The choices may depend on $L$". P11이 말하는 $\zeta_{L,N}$, $\Delta_N^{L,\mathbf u_{L,N}}$ 는 그 수열 위의 것이다. P8·P9 쪽은 원문이 "along every sequence from Lemma pert:selection"(`perturbations.tex` 455, `decorrelation.tex` 4–7)이므로 어느 $\varepsilon$ 의 수열이든 성립한다. **실제 빈칸이다**(항목 4). |
| 판정 | P11 블랙박스면 닫힘 | Pass | **블랙박스로 닫힘(P11 포함).** P11에 $\varepsilon$ 양화사가 필요하다. |

### 수 7 — 일반 상호작용으로 넓히고 맞붙이기 (P1, P2, P12)

| 항목 | A | B | 원문 대조 |
|---|---|---|---|
| 추론 | 조립 $2\alpha pD_K+2d_K$ 를 재구성했다. | 같다. $\widehat\theta$ 식을 P1에서 썼다. | `reduction.tex` 46–85와 같다. |
| 원문보다 강한 결론 | 약한 부정확 1건: "$\mathscr F_d$-가측 양수 인수의 상수 등변성 $T_d(cV)=cT_dV$". 반복된 $T_0$ 를 통과하려면 $c$ 가 $\mathscr F_0$-가측(원문 "root-measurable", `reduction.tex` 34–35)이어야 한다. 실제로 쓰이는 $c$ 는 물리 disorder의 함수라 모든 $\mathscr F_d$ 에 든다(`x:reduction-power-mean-scaling`). 결론에는 영향이 없다. | 없음 | — |
| "규칙 밖에서 필요" | power mean 단조·동차성. $U_\theta$ 식(상수 이동 $-\alpha\mathbb Ec$ 검산용). | 없음 | power mean: 원문 §2에는 절대 곱셈 한계 보존만 있다(`model.tex` 123–124). 두 시행값의 상대 비교(`reduction.tex` 34–35)와 상수 분리(39–40)는 원문이 진술 없이 쓴다. `x:reduction-power-mean-scaling` 이 작성자 정식화로 갖고 있고, 같은 성질이 §3 `tree:insertion` 에 $Y_d$ 에 대해 진술되어 있다. 용어집 `g:power-mean` 에는 "곱셈적 상·하한을 보존"만 있다. **부분 빈칸이다**(항목 1). 상수 이동은 `reduction.tex` 41–43이 site $-\alpha p\mathbb Ec$, edge $+\alpha(p-1)\mathbb Ec$ 로 A의 계산과 같다. |
| 짝수 $p$ | A는 HANDOFF 쪽 문구(호출자 주의)와 규칙 표 문구가 어긋난다고 지적했다. | — | 4절 항목 10. |
| 판정 | 블랙박스로 닫힘 | Pass | **블랙박스로 닫힘.** |

---

## 3. 두 수준의 판정

### (i) P8·P9(와 P11)를 블랙박스로 받을 때 상한·하한 조립

**닫힘.** 두 독자의 재구성이 원문 `comp:bounded-lower`, `main:theorem` 증명과 줄 단위로 맞는다:
- 하한: 고정 $\varepsilon$, 각 $L$ 의 선택된 수열에서 $\inf_r\Phi_r\le\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\le\underline F+2\varepsilon+\lvert\Delta_N-\mathcal B_{L-1}\rvert$ 이다. 그다음 $\limsup_N$(그 $L$ 의 수열), $L\to\infty$(P11), $\varepsilon\downarrow0$ 순으로 보낸다. 극한의 존재는 가정하지 않는다. $\underline F$ 는 모든 크기에 대한 $\liminf$ 다(`comparison.tex` 11–12).
- P11 내부 순서: $\eta$ 고정 → $N$ → $L$ → $\eta\downarrow0$(`comparison.tex` 153–156). 절단은 $M$ → $q$ → $N,L$ 이다.
- 일반화: $\liminf\widehat F_N\ge\widehat I-2\alpha pD_K-2d_K$, $K\to\infty$, 상수 이동 되돌림, 수 1의 $\limsup$ 와 맞붙임.

조건: P8·P9만으로는 부족하고 **P11도 블랙박스여야 한다**(A의 판단이 맞다. B도 같은 경계를 쓴다). 문장 보충 셋이 필요하다: P11의 $\varepsilon$ 양화사(필수), $r=0$ 식(필수), power mean 성질(검산용).

### (ii) P6·P7 → P8·P9

**지금은 구멍이다. P6′ 를 더하면 블랙박스로 닫힌다.**
- 지금 문구에서 수 5의 입력 가운데 셋이 규칙 표 밖에 있다. (a) canceled-anchor 전개와 $c_E$(P6 노드 칸에 이름만 있다), (b) 한 걸음 총합과 $\kappa(S)$(P6 노드 칸에 이름만 있다), (c) 계수 한계 `tree:charging`. (c)는 "못 옮긴 것" 묶음 1에 있으면서 L1은 이것을 P6으로 인용한다. HANDOFF 3.2의 1(B-1)이 말한 그대로이고, 원문(`decorrelation.tex` 331–350, 395–413)이 확인해 준다.
- P6′ 뒤에 남는 것은 조립이다. 두 사본의 깊이 미루기 선택, $J$ 로 나눈 항등식의 정리(`decor:induction-identity`), 사영과 세 사본, 귀납 재귀 $V_{k,L}(\eta)\le C(L^{-1/2}+V_{k-1,L}(\eta/2)^{1/4})$, marker anchor, martingale 연속성, fiber bound가 여기에 든다. 이것들은 "못 옮긴 것" 묶음 1(`decor:J-*`, `decor:shift-figure`), 2, 3, 4, 5에 이미 있다. 따라서 P8·P9는 블랙박스로 남는 것이 맞다. A의 결론("P6′ 이 구멍 1–4를 메우고 5만 남는다")은 원문과 맞는다.

---

## 4. P6′ 확정안

### 4.1 A 초안의 [ ] 항목 확정

| A 초안 | 확정 | 근거 |
|---|---|---|
| (b) 조합 인자, 수렴 영역 | 혼합 미분 $\partial_{t_1}\cdots\partial_{t_k}|_{\boldsymbol t=0}$ 이 순서 있는 history 합과 같다(추가 factorial 없음). $D_j=D$ 이면 $t^k$ 계수는 우변$/k!$ 이다. 해석 영역은 $\sum_j\lvert t_j\rvert\lVert D_j\rVert_\infty<1$ 이고 경계는 kernel에 균일하다. color 순서는 어떤 고정 순서여도 된다. 빈 확장의 무게는 1이다. | `trees.tex` 152–176, 278–296; `perturbations.tex` 491–492 |
| (b) 전개되는 양 | A는 "임의의 유계 $G$"라고 썼다. 정확히는 **anchor 인자를 상쇄한 tree 기대값** $E^{A_{\boldsymbol t}}_{\mathcal T}[H/A^{a_*}_{\boldsymbol t}]$ 이다. $H$ 는 old tree 변수의 유계 함수로 삽입 매개변수에 무관하다. root가 주어진 조건부 항등식이다($E_{\mathcal T}$, $\mathbb E$ 아님). | `trees.tex` 280–289 |
| (d) old leaf $+1$ 합이 old tree와 무관한 이유 | reference를 담지 않은 old 부분 tree 하나(깊이 $d+1$ 뿌리, leaf $q$ 개)의 선택 계수 합은 telescoping으로 $q+\sum_\beta\gamma_\beta=m_{d+1}$ 이다. 지정 vertex의 fresh 선택 $m_d-nm_{d+1}$ 과 더하면 $m_d-jm_{d+1}$ 이다. 일반 격자 $0=m_0<\cdots<m_L=1$ 에서 성립한다. | `trees.tex` 337–375 |
| (d) $\kappa$ 의 부호 | 맞다. 인자가 모두 음수라 $(-1)^{\sum_v(a_v-1)}$ 이다. 원문에 명시는 없고 식에서 읽은 것이다(용어집에도 그렇게 적혀 있다). P6′ 문장에는 넣지 않는다. | `tree:K` |
| (e) $\lvert J\rvert$ 하한 | **A 초안은 틀렸다.** $\lvert J\rvert\ge\delta^b\eta^{\sum_v(a_v-2)}$(`tree:charging`)이고, §7의 두 사본에서는 $\lvert J\rvert\ge c_{k,\eta}\delta^{2b}$ 이다. $L$ 에 균일한 양의 하한은 없다. | `trees.tex` 449–455; `decorrelation.tex` 336–341 |
| (e) 합 범위와 old leaf | 합은 처방한 reference 모양(과 허용 확장의 추가 제한)을 지키는 모든 history이고, old leaf 재사용도 포함한다. 단계마다 절댓값 합 $\le2(q+k)$, 지정 깊이의 unary fresh split로 제한하면 $\le(q+k)\delta$ 다. | `trees.tex` 417–447 |
| (e) 상수 의존성 | $\sum\lvert c_E\rvert\le C_{q,k}\delta^b$. $C_{q,k}$ 는 **old tree의 leaf 수 $q$** 와 color 수 $k$ 에 의존하고, $L$, 지정 깊이, 서로 다른 vertex의 깊이 일치와는 무관하다. 상대 한계는 $C_{q,k,\eta}$ 다(§7에서는 $q=2k$ 라 $C_{k,\eta}$). | `trees.tex` 393–415 |
| (e) 조건 | "$\eta$-regular한 모든 target"이 아니다. (가) 지정 vertex $b$ 개의 깊이가 old tree 어디에서도 branching 깊이가 아님, (나) 상대 한계에는 그 vertex들에서 $m_{d_v}\ge\eta$, (다) 격자 $m_d=d/L$. §7에서 (가)를 보장하는 것이 한 칸 미루기와 $\eta$-regularity다(`decorrelation.tex` 342–345). | 같은 곳 |
| (e) "$-\delta$ 대 $2+\delta$" | 미루기 전의 예다. 미루면 절댓값 합이 $\delta$ 다. P6′ 에는 일반형(지정 vertex마다 $\delta$)만 둔다. | `trees.tex` 317–329 |
| (a) 미분 규칙 | A 초안이 맞다. $n_\beta$ 는 그 걸음의 **현재** tree(안 쓴 old path와 이미 더한 path 포함)의 자식 수다. 같은 vertex라도 앞선 선택에 따라 계수가 달라진다. | `trees.tex` 178–202, 270–276; `x:tree-extension-history` |

### 4.2 확정안 (rules.md 표의 열 구성: rule | 물리 규칙 | 수학 노드 | 차이 | 유형 | 승인)

```
| P6′ | (extension history 전개와 계수 한계) anchor replica 하나의 섭동 인자를 상쇄한 replica tree 기대값을 섭동 크기로 전개하면, 새 replica를 하나씩 붙이는 방법([[g:extension-history|extension history]] $E$)마다 계수 $c_E$ 가 붙은 tree 기대값의 합이 정확히 나온다. 한 걸음에서 새 replica는 anchor가 아니고 아직 쓰지 않은 old replica를 다시 쓰거나(계수 $+1$) 현재 tree의 내부 vertex $\beta$ 에서 새로 갈라지고(계수 $\gamma_\beta<0$, P6), $c_E$ 는 그 곱이라 부호가 섞인다. anchor와 새 replica들이 이룰 모양 $S$ 를 처방하면 계수 합은 old tree와 무관한 $\kappa(S)$([[g:tree-coefficient]])다. 하한의 격자 $m_d=d/L$ 에서, 처방한 branching vertex 가운데 $b$ 개의 깊이가 old tree의 어느 branching 깊이와도 겹치지 않으면 계수 절댓값 합은 (old tree 크기와 replica 수에만 의존하는 상수)$\times\delta^b$ 이하다($\delta=1/L$, 계수 한계). | tree:extension-expansion, x:tree-extension-history, x:tree-differentiation-rule, tree:reference-total, tree:charging | 정확한 꼴(`tree:extension-expansion`): old tree $\mathcal T$, anchor $a_*$, old tree 변수의 유계 함수 $H$(삽입 매개변수에 무관), 유계 실수 path 함수 $D_1,\ldots,D_k$, $A_{\boldsymbol t}=1+\sum_jt_jD_j$ 에 대해 $\partial_{t_1}\cdots\partial_{t_k}E^{A_{\boldsymbol t}}_{\mathcal T}[H/A^{a_*}_{\boldsymbol t}]\big|_{\boldsymbol t=0}=\sum_Ec_E\,E_{\mathcal T_E}[H\prod_jD_j^{a_j(E)}]$ 이다. root가 주어진 조건부 항등식이고 임의의 유한 kernel 열에서 정확하다. color는 어떤 고정 순서로 붙여도 되고, $D_j=D$ 이면 $t^k$ 계수는 우변을 $k!$ 로 나눈 것이며, 빈 확장의 무게는 1이다. 좌변은 $\sum_j\lvert t_j\rvert\lVert D_j\rVert_\infty<1$ 에서 해석적이고 그 경계는 kernel에 균일하다. $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$ 의 $n_\beta$ 는 그 걸음의 현재 tree(안 쓴 old path와 이미 붙인 path 포함)의 자식 수다. anchor는 처음부터 상쇄되어 있어(protected, [[g:protected-leaf]]) 다시 고를 수 없다. P6의 $\log$ 전개와 같은 미분 규칙(`x:tree-differentiation-rule`)에서 나온다(`trees.tex` 2–5). 한 걸음 총합(`tree:reference-total`): 다음 replica가 reference([[g:reference-path]]: anchor와 이미 color를 받은 path)의 prefix를 깊이 $d$ 까지 따른 뒤 reference를 담은 $j\ge1$ 개 자식과 다른 자식으로 들어가야 하고 그 밖에는 제약이 없으면, 허용 선택의 계수 합은 $m_d-jm_{d+1}$ 이다. reference가 없는 old 부분 tree의 선택 계수 합이 telescoping으로 $m_{d+1}$ 이 되어 old tree 모양이 지워지기 때문이다(`trees.tex` 359–375). 그래서 처방 모양 $S$ 의 전체 계수 합은 어느 old tree에서든, color 순서와 무관하게 $\kappa(S)=\prod_{v\in\mathrm{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$ 이다. 제약은 reference와의 split 깊이만 지정하고 같은 조상 관계의 안 쓴 old path를 구별하지 않는다. 이 두 결과는 일반 격자에서 성립한다. 계수 한계(`tree:charging`, $m_d=d/L$): leaf $q$ 개인 old tree에 replica $k$ 개를 붙이고 reference 모양을 처방할 때(허용 확장에 추가 제한이 있어도 된다), 지정 vertex $b$ 개의 깊이가 old tree의 branching 깊이가 아니면 $\sum_{E\text{ 허용}}\lvert c_E\rvert\le C_{q,k}\delta^b$ 이다. $C_{q,k}$ 는 $L$, 지정 깊이, 서로 다른 vertex의 깊이 일치와 무관하다. 그 $b$ 개 vertex의 $J=\prod_v\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$ 은 모든 $v$ 에서 $m_{d_v}\ge\eta>0$ 이면 $\lvert J\rvert\ge\delta^b\eta^{\sum_v(a_v-2)}$ 이고 $\frac1{\lvert J\rvert}\sum\lvert c_E\rvert\le C_{q,k,\eta}$ 다. $\lvert J\rvert$ 자체는 $\delta^b$ 크기로 작아지고 $L$ 에 균일한 양의 하한이 없다. 균일한 것은 이 비율뿐이다. 쓰임: 수 4에서 혼합 미분이 이 순서 있는 확장 규칙 그대로다(추가 factorial 없음, `perturbations.tex` 491–492). 수 5에서 귀납의 정규화 $J=\kappa(S^+)^2$($\lvert J\rvert\ge c_{k,\eta}\delta^{2b}$)와 상대 비용 $\le C_{k,\eta}$(`decorrelation.tex` 331–350), marker 계수 $C(S,e)=-\delta\kappa(S)$(547)가 이 행에서 나온다. 깊이를 한 칸 미뤄 지정 깊이를 old branching 깊이와 떼어 놓는 선택과 $J$ 로 나눈 뒤의 조립은 이 행이 아니라 P8의 증명에 숨는다([[g:depth-delay]], "규칙으로 못 옮긴 것"). 물리 대응은 없다: $c_E$ 는 확률 가중치가 아니고(부호가 섞인다), 이 전개는 replica 수 $n\to0$ 의 해석적 연속을 쓰지 않는다. | weakening | proposed |
```

유형을 `weakening` 으로 둔 이유: 물리 규칙 칸은 $H$, color 순서, 해석 영역, 상수의 정확한 의존성, $J$ 하한을 말하지 않지만 말하는 것은 모두 참이다. 정확한 진술은 차이 칸에 있다. `blackbox` 로 볼 수도 있다(확신 낮은 곳 2).

### 4.3 함께 바꿀 곳

- **P6 수학 노드 칸**: `tree:insertion, tree:log-expansion, tree:extension-expansion, tree:reference-total` 에서 뒤의 둘을 P6′ 로 옮긴다. P6 문장은 바꾸지 않는다.
- **P7 차이 칸**: "$c_E$ 는 P6의 tree 계수"를 "$c_E$ 는 P6′ 의 extension 계수($\gamma_\beta$ 와 old replica 재사용 계수 $+1$ 의 곱)"로 바꾼다.
- **"규칙으로 못 옮긴 것" 묶음 1**: `tree:charging`, `tree:relative-charging` 을 빼고 "(계수 한계 자체는 P6′)"를 덧붙인다. `decor:J-definition`, `decor:J-lower-bound`, `decor:relative-absolute-cost`, `decor:shift-figure` 는 P8 증명의 적용 부분으로 남긴다.
- **용어집 `g:depth-delay` 기호 칸**: $\lvert J\rvert\ge c_{k,\eta}\delta^{2b}$ 를 덧붙인다(A의 오독 원인).

### 4.4 L1 수 4·5 문구 제안

수 4, "무엇을 하는가"의 마지막 문장:
> 현재: 이 항등식과 tree 표본 규칙·계수 한계(P6)가 수 5의 입력의 전부다: …
>
> 제안: 수 5가 모형에서 받는 입력은 이 항등식과 tree 표본 규칙뿐이고(`decorrelation.tex` 8–9), 여기에 extension 계수의 합 $\kappa$ 와 계수 한계(P6′)라는 유한 tree 조합과 모형 무관한 확률 부등식만 더한다. 수 5는 상호작용의 꼴(factorization 등)을 쓰지 않고, 수 6이 더하는 입력(증분 식, 선택된 수열, encoding, 균일 site 표본, log 전개)도 factorization과 positivity를 쓰지 않는다(`cavity.tex` 13–14).

수 4 "쓰는 규칙": `P6, P7` → `P6, P6′, P7`.

수 5, "무엇을 하는가"의 해당 구절:
> 현재: … 절댓값 계수 합의 상대 한계([[tree:charging]])가 나눈 뒤의 오차를 제어한다 …
>
> 제안: … 정규화 계수 $J=\kappa(S^+)^2$ 는 $\delta^{2b}$ 만큼 작지만, 절댓값 계수 합의 상대 한계(P6′ 의 계수 한계, [[tree:charging]])가 $J$ 로 나눈 뒤의 오차를 $L$ 에 균일하게 제어한다 …

수 5 "쓰는 규칙": `P6, P8, P9` → `P6′, P7, P8, P9`. §7은 $Q_k$ 를 쓰지 않고, 쓰는 것은 항등식(P7)과 P6′ 다.

---

## 5. 규칙·L1 수정 제안 목록

우선순위: **필수** = L2 전에 필수, **함께** = L2와 함께, **나중**.

| # | 대상 | 원문 근거 | 고칠 문장 초안 | 우선 |
|---|---|---|---|---|
| 0 | P6′ 추가와 4.3의 연동 수정 | 4절 | 4.2, 4.3 | **필수** |
| 0′ | L1 수 4·5 문구와 "쓰는 규칙" 칸 | 4.4 | 4.4 | **필수** |
| 1 | power mean 성질(P3, P12). 용어집 `g:power-mean` 역할 칸, 또는 rules 머리의 기호 목록 | `trees.tex` 112–115(`tree:insertion`: $Y_d$ 의 단조·동차, root-가측 한계와 상수); `model.tex` 123–124(곱셈 한계 보존); `reduction.tex` 34–35, 39–40(진술 없이 사용); `x:reduction-power-mean-scaling`(T_d에 대한 작성자 정식화) | "power-mean 재귀($T_d$ 와 $Y_d$)는 단조이고 root-가측 양의 상수에 대해 동차다: $a\le A\le b$($a,b$ root-가측)이면 $a\le Y_d\le b$, $A\mapsto cA$ 이면 $Y_d\mapsto cY_d$(`tree:insertion`; 시행 functional의 $T_d$ 에 대해서는 `x:reduction-power-mean-scaling`, 작성자 정식화). 그래서 $\log$ 쪽에서 root-가측 상수 이동과 등변이고 root-가측 곱셈 비교를 보존한다. P3의 $(\log2)N^{3/4}$, P4의 증분 유계, P12의 $\alpha(2p-1)D+d$ 와 상수 이동이 이것을 쓴다." | 함께 |
| 2 | 용어집 `g:site-term`, `g:site-bond-insertion` 에 식 | `model.tex` 59–63; `cavity.tex` 59–68 | $U_\theta(x_1,\ldots,x_{p-1};\varepsilon)=\log\sum_{s\in\{\pm1\}^{p-1}}e^{\theta(s,\varepsilon)}\prod_\ell q_{x_\ell}(s_\ell)$, $q_x(s)=e^{xs}/2\cosh x$; $A_{\rm s}=\frac12\sum_\varepsilon\exp(h\varepsilon+\sum_{j\le K_{\rm s}}\theta_j(\sigma_{i_{1,j}},\ldots,\sigma_{i_{p-1,j}},\varepsilon))$, $A_{\rm b}=\exp\sum_{j\le K_{\rm b}}\theta_j(\sigma_{i_{1,j}},\ldots,\sigma_{i_{p,j}})$ | 함께 |
| 3 | P5 차이 칸, 선택 기구 | `perturbations.tex` 269–301 | "선택은 다음 순서다: (`cavity:negligible` 로) 매개변수 평균한 증분 $\int\Delta_N\,d\pi$ 가 $\underline F+\varepsilon$ 이하인 $N$ 이 무한히 많다. 평균 score 집중은 모든 $N$ 에서 성립하므로 그 무한집합에서 $N_j$ 를 충분히 크게 고르고, Markov로 score 오차가 작은 매개변수 집합(측도 $\ge1-j^{-2}$)에서 증분이 $\underline F+2\varepsilon$ 이하인 점을 고른다. 좋은 $N$ 의 양의 밀도는 필요 없다." 덧붙임: 원문은 $j$ 를 type 첨자(`pert:parameters`)와 수열 첨자에 겹쳐 쓴다. 규칙·L1에서는 수열을 $N_n$ 등으로 바꿔 쓰기를 권한다. | 함께 |
| 4 | P8, P9, P11의 $\varepsilon$ 와 $(L,\varepsilon)$ 의존 | `comparison.tex` 8–11 "Fix $\varepsilon>0$. At each depth $L\ge2$ …"; `perturbations.tex` 455 "along every sequence from Lemma"; `decorrelation.tex` 4–7 | P11 차이 칸 첫머리에: "$\varepsilon>0$ 을 고정하고 각 $L$ 에서 P5가 고른 수열(곧 $(L,\varepsilon)$ 마다 다른 수열)과 그 위의 결정적 $\mathbf u_{L,N}$ 을 쓴다. $\Delta_N$, $\zeta_{L,N}$ 은 그 수열 위의 것이다." P8·P9 차이 칸의 "모든 $N$ 극한은 P5가 $L$ 마다 고른 수열을 따르고"를 "모든 $N$ 극한은 P5가 $(L,\varepsilon)$ 마다 고른 수열을 따른다(P7과 같이 그런 수열이면 어느 것이어도 된다)"로 바꾼다. | **필수**(P11), 함께(P8, P9) |
| 5 | 용어집 `g:eta-regular`, "모든 쌍" | `decorrelation.tex` 21–28 "distinct branching vertices"; `trees.tex` 462–464 "any two distinct branching vertices" | "서로 다른 두 branching vertex는 조상 관계이든 아니든 모두 정규화 깊이 차가 $\eta$ 보다 크다." 덧붙임: `trees.tex` 의 regular shape(tree 하나, $Q_k$ 용)와 §7의 $\eta$-regular 깊이 배정(추가 prefix 깊이, aligned 사본 포함)은 같은 조건을 다른 대상에 건 것이다. | 함께 |
| 6 | L1 수 5 "각 고정 깊이에서 집중" | `decorrelation.tex` 82, 548–569 | "… 이어서 marker anchor를 쓴 두 번째 항등식으로 첫 split 한 칸 앞 prefix의 조건부 평균 $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$ 의 분산을 각 고정 $L,S,e$ 에서 0으로 보낸다($\operatorname{Var}(M)\to0$). 그 prefix 아래의 남은 요동은 조건부 decorrelation과 깊이 연속성으로 깊이 평균에서만 제어되므로, 결론은 고정 깊이가 아니라 $\lim_L\limsup_N\mathcal A_{L,\eta}\operatorname{Var}(R_S)=0$ 이다(singleton만 고정 $L$)." | **필수** |
| 7 | L1 수 2의 $Y_0$ 표기 | `cavity.tex` 56–58; `trees.tex` 84–90 | 수 2 끝에: "$Y_{0,\rm s}$, $Y_{0,\rm b}$ 는 site·bond 삽입 $A_{\rm s}$, $A_{\rm b}$ 에 reservoir의 tilted kernel로 power-mean 재귀를 적용한 root 값이다([[g:insertion]]). $L\ge2$ 에서는 보통의 분배함수 비 $Z'/Z$ 가 아니다($L=1$ 일 때만 같다)." | **필수**(저비용) |
| 8 | $r=0$ 규약을 식으로. L0 본문 또는 용어집 `g:functional` | `model.tex` 118–120 | "$r=0$ 이면 모든 message가 공통 법칙 $\zeta\in\mathcal P(\mathbb R)$ 로 독립이고 $T_d$ 를 빼서 $\mathcal B_0(\zeta)=\log2+\mathbb E\log V_{\rm s}-\alpha(p-1)\mathbb E\log V_{\rm e}$ 다." | **필수** |
| 9 | 용어집 `g:depth-delay` 기호 칸에 $J$ 의 크기 | `decorrelation.tex` 336–341 | "$\lvert J\rvert\ge c_{k,\eta}\delta^{2b}$($L$ 에 균일한 양의 하한은 없고, 균일한 것은 상대 비용이다)" | 함께(P6′ 와 같이) |
| 10 | 짝수 $p$: rules.md "확신이 낮은 대응" 대 HANDOFF 3.2의 4 | 아래 | 아래 | **필수**(HANDOFF), 나중(rules) |
| 11 | singleton 서술(A의 열린 항목 10) | `decorrelation.tex` 283–289 | 고칠 것 없음. 용어집이 이미 "더 강하게 …"라고 적는다. | — |
| 12 | P11 증명 재료(정규화 $A=z(1+D)$, 절단 순서) | `comparison.tex` 198–223 | P11은 블랙박스로 두므로 고치지 않는다. 지금 묶음 "나머지 절단과 부호화의 측도론"에 있다. | 나중 |

### 항목 10 — 짝수 $p$ 문구의 어긋남

원문 확인:
- `model.tex` 3: "Fix an even integer $p\ge2$". 전역 가정이다.
- 증명 안에서 짝수성을 명시적으로 부르는 곳은 `upper.tex` 123–124("Since $p$ is even, convexity …") 하나다. 다른 절에서 "even"은 따름정리의 모형 진술에만 나온다(grep 확인).
- `reduction.tex` 4–6: "The lower bound … requires bounded permutation-invariant interactions, whereas the upper bound uses the factorization and positivity hypotheses." 짝수성은 이 문장에 없다.
- `cavity.tex` 13–14: "Neither the factorization nor the positivity assumption is used in the lower bound." 짝수성은 이 문장에도 없다.
- 하한이 홀수 $p$ 에서 선다는 문장은 원문에 없다(`consequences.tex` 132 "The even-arity hypothesis … excludes random 3-SAT").

판정: **두 문서의 사실 판단은 같고 표현이 어긋난다.** HANDOFF 3.2의 4는 "짝수 $p$ 와 부호 조건 (2.4)는 상한에서만 쓰인다(upper.tex 123–124)"라고 짝수 $p$ 와 positivity를 한 문장에 묶는다. 그런데 positivity가 하한에 쓰이지 않는다는 것은 원문이 명시하고(`cavity.tex` 13–14, `reduction.tex` 4–6), 짝수 $p$ 쪽은 원문이 그렇게 말하지 않는다. 짝수 $p$ 에 대해서는 명시적 사용이 없다는 것을 읽어 낸 것뿐이다. 인용 행 upper.tex 123–124도 "상한에서 쓰인다"만 받쳐 주고 "상한에서만"은 받쳐 주지 않는다. rules.md는 바로 이 문장을 피하기로 했다("P1 차이 칸은 '짝수 $p$ 는 상한에만 쓰인다'고 쓰지 않았다"). 독자 A에게 주어진 주의 문구가 HANDOFF 쪽 표현이었다. L2 작성자는 HANDOFF를 읽으므로 HANDOFF 쪽을 고친다.

HANDOFF 3.2의 4 초안:
> **가정이 쓰이는 곳의 비대칭.** 부호 조건 (2.4)는 상한에서만 쓰인다. 원문이 명시한다(`cavity.tex` 13–14, `reduction.tex` 4–6). 짝수 $p$ 를 증명 안에서 명시적으로 부르는 곳은 상한의 볼록성 단계(`upper.tex` 123–124)뿐이지만, 논문은 $p$ 를 처음부터 짝수로 고정하고(`model.tex` 3) 하한이 홀수 $p$ 에서 선다고 말하지 않는다. 그래서 "짝수 $p$ 는 상한에만 쓰인다"고 쓰지 않는다(rules.md "확신이 낮은 대응"과 같은 판단). factorization (2.3)은 상한과, 하한 쪽 순열 불변성 양쪽에서 쓰인다(`reduction.tex` 54–58). "하한은 가정 없이 선다"고 쓰면 틀린다.

rules.md "확신이 낮은 대응"의 P1 짝수 $p$ 항목에서는 "짝수 $p$ 가 직접 쓰이는 곳은 … 뿐이지만"을 "원문이 짝수성을 명시적으로 부르는 곳은 상한의 볼록성 단계(`upper.tex` 123–124)뿐이지만"으로 바꿀 것을 권한다. 텍스트에 대한 주장으로 바꿔 검증할 수 있게 하는 것이다(나중).

---

## 6. 확신이 낮은 곳

1. **P8·P9가 "어느 $\varepsilon$ 의 수열이든" 성립한다는 읽기.** `pert:tree-identity` 는 "along every sequence from Lemma pert:selection"이라고 명시한다. §7은 "all limits in $N$ are along the sizes and parameter choices supplied by pert:selection"이라고 쓴다. 따라서 P8·P9도 같은 범위로 읽었다. §7이 이것을 따로 문장으로 말하지는 않는다. 항목 4의 P8·P9 문구는 이 읽기에 기댄다.
2. **P6′ 의 유형.** `weakening` 으로 두었다. 차이 칸이 정확한 진술을 모두 담고 물리 규칙 칸이 그것을 줄인 것이므로 `blackbox`(진술 정확, 증명 숨김)로 보는 판단도 가능하다. P6이 같은 성격의 행을 `exact` 로 둔 것과 맞출지는 사용자가 정할 일이다.
3. **P6′ 의 "물리 규칙" 칸이 물리 언어인가.** 이 행은 물리 대응이 없는 조합 진술이다(`g:extension-history`, `g:depth-delay` 의 물리 대응 "없음"). replica 어휘로 썼지만 SCHEMA의 "물리 언어 한 문장"보다 길고 수학적이다. 사용자가 P6′ 를 더하기로 정했으므로 그대로 두었다.
4. **카드 상태.** 카드는 지금 다른 에이전트가 고치고 있다. 4.1에 인용한 카드 내용(`tree.charging` 의 "$J=\kappa(S^+)^2$ 가 정확히 이 lemma의 $J$", `x.reduction-power-mean-scaling` 의 작성자 정식화)은 오늘 읽은 시점의 것이다. 확정안의 근거는 원문 행 번호로 적었으므로 카드가 바뀌어도 서야 한다.
5. **수 6의 정확한 부분(독립 label 삽입 $=\mathcal B_{L-1}$).** `comparison.tex` 160–193을 훑어 A의 채움과 같은 논법임을 확인했지만 한 줄씩 대조하지는 않았다. P11 블랙박스 판정에는 영향이 없다.
6. **수 1의 interpolation 내부**(`upper.tex` 21–118)는 대조하지 않았다. P2 블랙박스 판정에는 영향이 없다.
7. **B의 신뢰도.** B는 자기 시험의 한계를 정확히 적었고, 원문보다 강한 결론을 내지 않았다. 대신 블랙박스 경계를 시험하지 않았으므로 (ii) 수준의 정보는 B에게서 얻을 수 없다. (ii) 판정은 A와 원문 대조에 기댄다.
