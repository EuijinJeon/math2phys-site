# 규칙 표 갱신 — 2026-11-13

닫힘 시험 판정(`build/closure-test-2026-11-13.md`, 이하 "판정")의 "L2 전에 필수" 7건과 거기 딸린 변경을 반영했다. 사용자 결정: P6′ 행 추가, 규칙 표 승인은 L2 초안 뒤 일괄, 모든 status는 `proposed`.

고친 파일: `layers/rules.md`, `layers/L1.md`, `layers/L0.md`, `layers/glossary.md`. 카드·`tools/`·`SCHEMA.md`·`site/`·`HANDOFF.md` 는 건드리지 않았다.

검사: `python3 tools/check.py --out /tmp/rules-check.md`. 오류 0, 경고 4(대칭, 알려진 것: `x:pert-colored-extensions` 2건, `x:pert-standing` 2건). 규칙 표는 13행으로 읽히고 P6′ 의 수학 노드 5개가 모두 실재한다(연결·사전 통과). 새 용어집 링크(`g:protected-leaf`, `g:reference-path`, `g:grid` 등)도 용어 검사를 통과한다.

---

## 1. P6′ 행 (판정 0, 4.2–4.3)

### 원문 재대조

판정의 확정안을 출발점으로 다음 원문과 카드를 다시 대조했다.

| 내용 | 원문 | 카드 | 결과 |
|---|---|---|---|
| 확장 규칙 (i) 계수 1, (ii) $\gamma_\beta$, 현재 tree의 정의 | `trees.tex` 259–276 | `x:tree-extension-history` | 일치. $n_\beta$ 는 현재 tree(안 쓴 old path 포함)의 자식 수 |
| 전개 식, color 순서, $/k!$, 해석 경계, 빈 확장 무게 1 | `trees.tex` 278–296, 증명 298–304 | `tree:extension-expansion` | 일치. $H$ 는 old tree 변수의 유계 함수로 삽입 매개변수에 무관 |
| 미분 규칙, protected leaf | `trees.tex` 178–202 | `x:tree-differentiation-rule` | 일치. 두 전개가 한 규칙에서 나온다는 문장은 `trees.tex` 2–6 |
| 해석 영역 $\sum_j\lvert t_j\rvert\lVert D_j\rVert_\infty<1$, kernel에 균일 | `trees.tex` 156–176 | — | 일치 |
| 조건부(root 주어짐) | `trees.tex` 72–74, 98("conditional joint density") | — | 일치 |
| 한 걸음 합 $m_d-jm_{d+1}$, $\kappa(S)$, telescoping 이유, 일반 격자 | `trees.tex` 337–357, 증명 359–386 | `tree:reference-total` | 일치. $m_d=d/L$ 가정 없음 |
| 계수 한계 $C_{q,k}\delta^b$, 상수 의존성, $J$, 상대 한계, $\lvert J\rvert\ge\delta^b\eta^{\sum(a_v-2)}$ | `trees.tex` 393–415, 증명 417–456(하한은 449–455) | `tree:charging` | 일치. $m_d=d/L$ 가정은 이 lemma에만 있다 |
| 미루기 전 $-\delta$ 대 $2+\delta$, 미룬 뒤 $\delta$ | `trees.tex` 317–335 | `x:tree-cancellation-example` | 일치. P6′ 에는 일반형만 둠 |
| 혼합 미분 = 순서 있는 확장 규칙, 추가 factorial 없음 | `perturbations.tex` 491–492 | — | 일치 |
| $J=\kappa(S^+)^2$, $\lvert J\rvert\ge c_{k,\eta}\delta^{2b}$, 상대 비용 $\le C_{k,\eta}$ | `decorrelation.tex` 332–359 | — | 일치. **판정의 행 번호(331–350, 336–341)는 조금 어긋난다**: 정의 333–335, 하한 337–343, 상대 비용 344–352, 두 사본 설명 354–359 |
| marker 계수 $C(S,e)=-\delta\kappa(S)$ | `decorrelation.tex` 546–548 | — | 일치(판정은 547) |

판정 확정안에서 바꾼 것:
- **물리 규칙 칸**: "섭동 크기로 전개하면"을 "섭동 크기 $t_1,\ldots,t_k$ 로 한 번씩 미분해 $\boldsymbol t=0$ 에서 보면"으로 고쳤다. lemma는 $\boldsymbol t=0$ 에서의 혼합 도함수 항등식이다. "anchor replica 하나의 섭동 인자"를 "삽입 인자"로 바꿨다($A^{a_*}$ 는 insertion 인자). 상수를 "old tree 크기"가 아니라 "old tree의 leaf 수"로 적었다($C_{q,k}$ 의 $q$). $\delta=1/L$ 을 적었다.
- **차이 칸 줄이기**: 딸린 진술 넷(color 순서, $/k!$, 빈 확장, 해석 경계)과 $n_\beta$ 회계는 한 구절씩만 두고 카드(`tree:extension-expansion`, `x:tree-extension-history`)를 가리켰다. 한 걸음 총합의 서술은 결론과 이유 한 문장으로 줄였다. 유지한 것: 정확한 식, 조건부·임의 kernel, $\kappa$ 의 일반 격자, 계수 한계의 격자 가정과 상수 의존성, $\lvert J\rvert$ 가 $\delta^b$ 크기이고 균일 하한이 없다는 것, 쓰임(수 4·5), P8에 숨는 것, 물리 대응 없음. 1847자(판정 확정안의 약 3분의 2).
- **더한 정확성**: $\lvert J\rvert$ 가 $\delta^b$ "크기"라는 것은 하한만이 아니라 vertex마다 $j=1$ 인자가 정확히 $-\delta$ 라는 데서 나온다(`trees.tex` 449–451). 그래서 "$\delta^b$ 크기이고 $L$ 에 균일한 양의 하한이 없다"고 적었다.
- **행 번호**: `decorrelation.tex` 332–359, 546–548로 고쳤다.
- **유형**: `weakening`. 이유: 물리 규칙 칸은 $H$, color 순서, 해석 영역, 상수의 의존성, $\lvert J\rvert$ 의 크기와 상대 한계를 말하지 않지만 말하는 것은 모두 참이다(SCHEMA의 "덜 말하지만 정확함"). `blackbox`("진술 정확, 증명만 숨김")는 물리 칸이 진술 전체를 담을 때 맞는데 여기서는 그렇지 않다. 이 판단과 대안(`blackbox`)을 "확신이 낮은 대응"에 새 항목 "P6′ (유형과 물리 언어)"로 적었다.

### 딸린 변경 (판정 4.3)

| 파일 | 전 | 후 |
|---|---|---|
| rules.md P6 수학 노드 | `tree:insertion, tree:log-expansion, tree:extension-expansion, tree:reference-total` | `tree:insertion, tree:log-expansion` (뒤의 둘은 P6′). P6 문장은 그대로 |
| rules.md P7 차이 | "$c_E$ 는 P6의 tree 계수" | "$c_E$ 는 P6′ 의 extension 계수($\gamma_\beta$ 와 old replica 재사용 계수 $+1$ 의 곱)". 또 "유한 tree 조합"에 "(P6′)"을 붙였다 |
| rules.md "못 옮긴 것" 묶음 1 | `tree:charging`, `tree:relative-charging` 포함 | 둘을 빼고 "계수 한계 자체(`tree:charging`)는 P6′ 다. 여기 남은 것은 그것을 §7의 두 사본에 적용하는 부분이다"를 덧붙였다. `decor:J-*`, `decor:shift-figure` 는 남김 |
| rules.md "못 옮긴 것" 해석적 경계 묶음 | "P6의 증명" | "P6, P6′ 의 증명(`tree:charging` 의 증명 단계도 P6′ 에 숨는다)". `tree:mixed-expansion` 은 `tree:extension-expansion` 의 식이므로 P6′ 의 증명에도 속한다 (지시 밖의 딸린 변경) |
| rules.md "확신이 낮은 대응" | — | "P6′ (유형과 물리 언어)" 항목 추가(판정 6절 2, 3) |
| glossary `g:depth-delay` 기호 | $J$, 상대 비용만 | $\lvert J\rvert\ge c_{k,\eta}\delta^{2b}$ ($\delta^{2b}$ 크기, 균일 하한 없음, `decorrelation.tex` 337–343)와 "상대 비용은 $L$ 에 균일" 추가. 역할 칸에 "계수 한계는 P6′, 미루기의 선택과 적용은 P8의 증명" 한 문장 |
| glossary `g:extension-history`, `g:tree-coefficient` 역할 | P6/P7만 | "(P6′)" 표기 추가 |

`tree:relative-charging` 은 식 라벨이고 카드가 없다(`trees.tex` 411). 묶음 목록에서 빼는 것만으로 충분하다.

## 2. L1 수 4·5 (판정 0′, 4.4, 5절 6)

| 위치 | 전 | 후 | 근거 |
|---|---|---|---|
| 머리 바닥 줄 | "규칙 P1–P12는" | "규칙 P1–P12와 P6′ 은" | — |
| 수 4 마지막 문장 | "이 항등식과 tree 표본 규칙·계수 한계(P6)가 수 5의 입력의 전부다: …" | "수 5가 모형에서 받는 입력은 이 항등식과 tree 표본 규칙뿐이고(`decorrelation.tex` 8–9), 수 5는 여기에 extension 계수의 합 $\kappa$ 와 계수 한계(P6′)라는 유한 tree 조합과 모형과 무관한 확률 부등식만 더한다. …" ("전부" 과장 제거) | `decorrelation.tex` 8–9 |
| 수 4 쓰는 규칙 | P6, P7 | P6, P6′, P7 | — |
| 수 5 $J$ 서술 | "상대 한계([[tree:charging]])가 나눈 뒤의 오차를 제어한다" | "정규화 계수 $J=\kappa(S^+)^2$ 는 $\delta^{2b}$ 만큼 작지만($b$ 는 $S$ 의 branching vertex 수), 상대 한계(P6′ 의 계수 한계, [[tree:charging]])가 $J$ 로 나눈 뒤의 오차를 $L$ 에 균일하게 제어한다" | `decorrelation.tex` 337–352 |
| 수 5 marker 단계 | "남은 조건부 평균을 각 고정 깊이에서 집중시켜" | "$S$ 의 첫 split 깊이 $e$ 보다 한 칸 앞 prefix의 조건부 평균 $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$ 의 분산을 각 고정 $L,S,e$ 에서 0으로 보낸다. 그 prefix 아래의 남은 요동은 … 깊이 평균에서만 제어되므로, 결론은 고정 깊이가 아니라 깊이 평균으로 나온다(singleton만 고정 $L$)" | `decorrelation.tex` 537–569, 570–601 |
| 수 5 쓰는 규칙 | P6, P8, P9 | P6′, P7, P8, P9 (§7은 $Q_k$ 를 쓰지 않는다) | 판정 4.4 |

## 3. ε 양화사 (판정 5절 4)

| 위치 | 변경 | 근거 |
|---|---|---|
| P11 물리 규칙 칸 | 첫머리에 "여유 $\varepsilon>0$ 을 고정하고 각 $L$ 에서 P5가 고른 선택된 수열 위에서" | `comparison.tex` 8–11 "Fix $\varepsilon>0$. At each depth $L\ge2$, use the sequence … The choices may depend on $L$" |
| P11 차이 칸 첫머리 | "고정한 $\varepsilon>0$ 에 대해, 각 $L\ge2$ 에서 P5가 고른 크기 수열과 결정적 $\mathbf u_{L,N}$ 을 쓴다. 이 수열은 $(L,\varepsilon)$ 마다 다르고 $\Delta_N=\Delta_N^{L,\mathbf u_{L,N}}$, $\zeta_{L,N}$ 은 그 수열 위의 것이다. … 결론은 각 고정 $\varepsilon$ 마다 성립하고, 하한은 그다음 $\varepsilon\downarrow0$" | 같은 곳; `comparison.tex` 160–167, 235–246 |
| P8, P9 차이 칸 | "P5가 $L$ 마다 고른 수열" → "P5가 $(L,\varepsilon)$ 마다 고른 수열(P7과 같이 P5가 준 수열이면 어느 $\varepsilon$ 의 것이어도 된다, `decorrelation.tex` 4–7)" | `decorrelation.tex` 4–7; `perturbations.tex` 454 "along every sequence from Lemma" |

P8·P9의 "어느 $\varepsilon$ 이든" 읽기는 판정 6절 1과 같은 읽기에 기댄다(§7은 $\varepsilon$ 을 따로 말하지 않는다).

## 4. $r=0$ 규약 (판정 5절 8)

원문 `model.tex` 118–120: "At $r=0$, the messages are independent with common law $\zeta\in\mathcal P(\mathbb R)$ and the operators $T_d$ are omitted".

| 위치 | 변경 |
|---|---|
| L0 본문 | "$r=0$ 이면 $\zeta$ 는 $x$ 의 분포 하나이며 $\mathbf m$ 과 $T_0$ 는 없다" → "$r=0$ 이면 $\zeta\in\mathcal P(\mathbb R)$ 는 $x$ 의 분포 하나이고 모든 message가 이 공통 법칙으로 독립이며, $\mathbf m$ 이 없고 $T_d$ 를 빼서 괄호 안은 $\mathcal B_0(\zeta)=\log2+\mathbb E\log V_{\rm s}-\alpha(p-1)\mathbb E\log V_{\rm e}$ 다" |
| glossary `g:functional` 기호 | $\mathcal B_0(\zeta)$ 식 추가 |
| glossary `g:order-parameter` 뜻 | "모든 label의 message가 이 공통 법칙으로 독립" 추가 |

## 5. L1 수 2의 $Y_0$ 주석 (판정 5절 7)

수 2 끝에: "$Y_{0,\rm s}$, $Y_{0,\rm b}$ 는 site·bond 삽입 $A_{\rm s}$, $A_{\rm b}$ 에 reservoir의 tilted kernel로 power-mean 재귀를 적용한 root 값이다([[g:insertion]], `cavity.tex` 56–58). $L\ge2$ 에서는 일반적으로 보통의 분배함수 비 $Z'/Z$ 가 아니다($L=1$ 이면 같다)." 판정 초안의 "아니다"에 "일반적으로"를 넣었다. 원문은 같지 않다고 증명하지 않고, 같다는 것을 $L=1$ 에서만 준다(`trees.tex` 63–64, `g:insertion` 물리 대응 칸).

## 6. 짝수 $p$ (판정 5절 10): 확인만

rules.md "확신이 낮은 대응"의 "P1의 짝수 $p$ 역할" 항목은 원문과 맞다. grep으로 확인: 증명 안의 "even"은 `upper.tex` 123 하나뿐이고, `model.tex` 3이 $p$ 를 짝수로 고정하며, 하한이 홀수 $p$ 에서 선다는 문장은 없다(`consequences.tex` 132는 3-SAT을 배제한다고만 한다). rules.md는 고치지 않았다. 판정이 "나중"으로 권한 문구 변경("짝수 $p$ 가 직접 쓰이는 곳은" → "원문이 짝수성을 명시적으로 부르는 곳은")도 하지 않았다. HANDOFF에 고칠 문장은 아래 10절.

## 7. $V_{\rm s}$ 정규화 (지시 7)

원문 `model.tex` 85: $V_{\rm s}=\frac12\sum_{\varepsilon=\pm1}\exp(\cdots)$. `cavity.tex` 59–62의 $A_{\rm s}$ 도 같은 $\frac12$ 를 갖는다. `layers/` 를 `V_{\rm s}`, "site 분배함수", "분배함수"로 grep했다.

| 위치 | 전 | 후 |
|---|---|---|
| glossary `g:site-term` 뜻 | "$V_{\rm s}$ 는 … 넣는 site 분배함수다" | "… site 분배함수를 $2$ 로 나눈 양이다(앞의 $\frac12$, `model.tex` 85). 그 $\log2$ 는 $\mathcal B_r$ 에 따로 있다" |
| glossary `g:site-term` 물리 대응 | "$V_{\rm s}$ 는 Bethe free entropy의 site 항" | "$\log2+\log V_{\rm s}=\log\sum_\varepsilon(\cdots)$ 가 Bethe free entropy의 site 항" |
| L0 본문 | "$V_{\rm s}$ 는 … 끼워 넣을 때의 site 분배함수" | "… 장 및 Poisson$(\alpha p)$ 개 상호작용과 함께 끼워 넣을 때의 site 분배함수를 2로 나눈 양(그 $\log2$ 가 앞에 따로 있다)" |
| rules.md P11 물리 규칙 칸 | "(site 항 $T_0V_{\rm s}$, bond 항 …)" | "(site 삽입 $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$, bond 삽입 $\mathbb E\log\widetilde Y_{0,\rm b}=\alpha(p-1)\mathbb E\log T_0V_{\rm e}$, $\log2$ 는 P4의 증분 식에 따로 있다)" (`comparison.tex` 178–192). 틀린 문장은 아니었지만 "site 항"이 $\mathcal B_r$ 의 $\log2$ 를 포함한 항으로 읽힐 수 있었다 |

나머지 출현(L1 기호 줄, `g:functional`, `g:interpolation` 의 $\varphi(0)=\log2+\mathbb E\log T_0V_{\rm s}$, `g:field`, `g:site-bond-insertion` 역할 칸)은 정규화와 맞아 고치지 않았다.

## 8. "L2와 함께" 가운데 짧은 것 (판정 5절 1, 2)

| 위치 | 변경 | 근거 |
|---|---|---|
| glossary `g:power-mean` 역할 | 단조성·root-가측 양의 상수에 대한 동차성 한 단락: $Y_d$ 에 대해서는 원문 진술, $T_d$ 에 대해서는 원문이 진술 없이 씀(작성자 정식화 카드 가리킴), $\log$ 쪽 결과, P3·P12가 씀 | `trees.tex` 112–115; `reduction.tex` 34–35, 39–40; `x:reduction-power-mean-scaling` |
| rules.md P3 차이 | "증명은 (5.2)와 개수만 쓰므로" → "(5.2)와 개수, 그리고 power-mean 재귀의 단조성과 root-가측 양의 상수에 대한 동차성만 쓰므로" | `cavity.tex` 36–38; `trees.tex` 112–115 |
| rules.md P12 차이 | 시행 쪽 비교와 상수 분리가 같은 성질을 쓴다는 한 문장 | `reduction.tex` 34–35, 39–40 |
| glossary `g:site-term` 기호 | $U_\theta=\log\sum_{s\in\{\pm1\}^{p-1}}e^{\theta(s_1,\ldots,s_{p-1},\varepsilon)}\prod_\ell q_{x_\ell}(s_\ell)$ | `model.tex` 59–63 |
| glossary `g:site-bond-insertion` 기호 | $A_{\rm s}$, $A_{\rm b}$ 식(첨자는 $[N]$ 의 독립 균일 index) | `cavity.tex` 59–68 |

## 9. 하지 않은 것과 이유

- **P5 차이 칸의 선택 기구(판정 5절 3)와 $j$ 첨자 겹침**: "함께" 항목이지만 지시가 허용한 짧은 항목(power mean, $U_\theta$, $A_{\rm s}$, $A_{\rm b}$)에 들지 않는다. L2와 함께 한다.
- **`g:eta-regular` 의 "모든 쌍"(판정 5절 5)**: 같은 이유. 지금 문장("서로 다른 branching vertex")도 원문과 맞는다.
- **rules.md 짝수 $p$ 문구 다듬기(판정 5절 10의 "나중")**: 지시가 확인만 하라고 했다.
- **P11 증명 재료(판정 5절 12)**: P11은 블랙박스로 둔다.
- **HANDOFF**: 조율자가 고친다. 문장은 10절.
- **카드**: `tree:charging` 카드 본문의 "$J=\kappa(S^+)^2$ 가 정확히 이 lemma의 $J$" 는 카드 쪽 일이라 손대지 않았다. 원문으로 보면 §7의 $J$ 는 두 사본의 $2b$ 개 vertex에 대한 이 lemma의 $J$ 이고, 하한은 $\eta$ 대신 큰 $L$ 에서의 $\eta/2$ 를 쓴다(`decorrelation.tex` 337–339). 카드도 그렇게 적고 있어 틀린 곳은 보지 못했다.
- **도구의 한계(보고만)**: `check.py` 의 단면 검사는 `\bP\d+\b` 로 규칙을 찾으므로 L1의 "P6′" 을 "P6"로 읽는다. 그래서 L1이 P6′ 을 가리키는지는 기계로 확인되지 않는다. 손으로 확인했다(수 4, 5). `tools/` 는 고치지 않았다.

## 10. HANDOFF에 고칠 문장 (조율자용)

`HANDOFF.md` 150행(3.2의 4), 지금:
> **가정이 쓰이는 곳의 비대칭.** 짝수 $p$ 와 부호 조건 (2.4)는 상한에서만 쓰인다(upper.tex 123–124). …

바꿀 문장(판정 5절 10의 초안을 원문으로 다시 확인함):
> **가정이 쓰이는 곳의 비대칭.** 부호 조건 (2.4)는 상한에서만 쓰인다. 원문이 명시한다(`cavity.tex` 13–14, `reduction.tex` 4–6). 짝수 $p$ 를 증명 안에서 명시적으로 부르는 곳은 상한의 볼록성 단계(`upper.tex` 123–124)뿐이지만, 논문은 $p$ 를 처음부터 짝수로 고정하고(`model.tex` 3) 하한이 홀수 $p$ 에서 선다고 말하지 않는다. 그래서 "짝수 $p$ 는 상한에만 쓰인다"고 쓰지 않는다(rules.md "확신이 낮은 대응"과 같은 판단). factorization (2.3)은 상한과, 하한 쪽 순열 불변성 양쪽에서 쓰인다(`reduction.tex` 54–58). "하한은 가정 없이 선다"고 쓰면 틀린다.

HANDOFF의 "규칙 12행"(25, 95, 106행)도 13행(P6′ 포함)으로 고쳐야 한다.
