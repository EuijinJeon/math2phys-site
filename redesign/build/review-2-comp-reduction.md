# 검토 2 — §8 comparison · §9 reduction 노드 카드 (독립 검토)

대상: `cards/comp.*.md` 27장과 `cards/x.comp-standing.md` (§8, 28장), `cards/reduction.*.md` 5장과 `cards/x.reduction-power-mean-scaling.md` (§9, 6장). 모두 34장.
기준: `source/sections/comparison.tex`(246줄)·`reduction.tex`(87줄) 전체, `model.tex`·`cavity.tex` 전체, `trees.tex` 1–150·200–262·455–525, `perturbations.tex` 1–65·245–300, `decorrelation.tex` 1–125·283–292, `overview.tex` 20–51.
"확인"은 원문과 한 줄씩 대조했거나 손으로 다시 계산했다는 뜻이다.

주의: 다른 섹션 카드(`cavity:section`, `tree:section`, `pert:section`, `model:section`, `main:theorem*`)와 `layers/` 는 내가 읽은 시점의 문구로 인용한다. `tools/check.py --sections comparison,reduction --out <scratchpad>` 결과: 형식·정초·포함·연결·순환·사전·단면·용어 통과, 의존 경고 2건(둘 다 comparison.tex 227의 `\cref{model:section}`; 아래 "의존 경고 2건").

## 요약

- 읽은 카드: 34 / 34 (머리말과 본문 모두). §8 28장, §9 6장.
- `math` 칸의 식 전사: (8.1), (comp:single-label-moments), $\pi$ 의 두 표현, (comp:pattern-error), telescoping의 $a$ 와 $\frac a2$, (comp:shape-error), (comp:shape-error-bound), (comp:increment-comparison), $C=H+BM$·$z=\cosh C$·$c=\tanh C$, $pM$, $\sum_{k>q}c^k/k$, $2\mathbb E[(H+BK)\mathbf1_{\{K>M\}}]$, 따름정리와 고정 $L$ 부등식, (reduction:free-stability)의 $\alpha D+d$, (reduction:trial-stability)의 $\alpha(2p-1)D+d$, (reduction:shift)의 $-\alpha\mathbb Ec$ 를 원문과 대조했다. 식 번호 (2.5)–(2.13), (5.5), (8.1)의 대응도 세어 확인했다. 부호, 계수, 첨자, 양화사, 극한 순서, 균일성의 범위가 어긋나는 곳은 **찾지 못했다**.
- 극한 순서: 작성자의 장부는 원문과 한 줄씩 맞는다(아래 "극한 순서").
- 작성자가 보탠 계산은 모두 다시 계산했다. **틀린 계산은 없다.** `x:reduction-power-mean-scaling` 의 (a)(b)와 결론은 옳고 reduction.tex 34–35, 39–40이 쓰는 성질과 일치한다(진술의 정의역에 대한 낮은 지적 F4).
- 증명 분해에 논리의 구멍은 없다. 다섯 증명(encoding, patterns, shape-error, insertion-comparison, bounded-lower)과 stability 증명 모두 원문 순서 그대로 덮는다. 구조에 대한 낮은 지적 하나(F5).
- `uses`: 순환 없음, 존재하지 않는 ID 없음. 직접 쓰는데 빠진 의존은 찾지 못했다. §8의 어떤 카드도 `model:section`, `main:theorem`, `upper:*`, `reduction:*` 을 `uses` 에 넣지 않는다(grep 확인).
- 용어 규율: Ruelle cascade, Ghirlanda–Guerra, stochastic stability, ultrametricity, "clustering", "self-average", "처방된 tree 항등식", 주어로서의 "connected correlation", "RSB 계층", R번호는 34장에 없다. $\mathbf u$ 를 root 변수로 쓴 곳도 없다(`comp:encoding` 본문, `comp:shape-error` gap (3), `comp:insertion-comparison` 본문이 모두 "선택된 값으로 고정"이라 적는다). "상태"는 두 곳이 걸린다(F1, F2).
- 지적 8건. 높음 0, 중간 1, 낮음 7. 지적이 걸린 카드 12장, 통과 22장(§8 18장, §9 4장).

| 유형 | 건수 | 번호 |
|---|---|---|
| 틀림 (식·진술) | 0 | — |
| 구멍 (증명 논리) | 0 | — |
| 부정확한 묘사 (physics) | 1 | F1 |
| 용어 규율 | 1 | F2 |
| 낡은·빠진 인터페이스 표 (누수) | 2 | F3, F6 |
| 진술의 정의역 | 1 | F4 |
| 구조 (`source`·ID) | 1 | F5 |
| 유형 (`abstraction`) | 1 | F7 |
| "작성자" 표시 누락 | 1 | F8 |

| 심각도 | 건수 | 번호 |
|---|---|---|
| 높음 | 0 | — |
| 중간 | 1 | F1 |
| 낮음 | 7 | F2–F8 |

## 지적 (심각도 순)

### F1. 부정확한 묘사 — `comp:encoding.s3` (physics) · 중간
- 카드: "그 replica들이 site $i$ 에서 보는 spin의 결합 법칙은 깊이마다 '자식 상태들이 서로 독립으로 같은 법칙 $\eta_d$ 에서 뽑힌다'는 계층 cavity field 사슬로 그대로 재현된다." 유형 `exact`.
- 원문: comparison.tex 44–48 "$\eta_d=\operatorname{Law}(\eta_{d+1}\mid\mathscr G_d)$", 61–67 "Conditional independence of children gives … $G_T(\eta_d)=\prod_\ell\int G_{T_\ell}(\nu)\,\eta_d(d\nu)$".
- $\eta_d$ 에서 뽑히는 것은 자식 상태(깊이 $d+1$ prefix)가 아니라 자식 vertex에 딸린 측도 $\eta_{d+1}$(깊이 $r$ 에서는 $x$)이다. 자식 prefix 자체는 tilted reservoir kernel로 뽑히고 $\eta_d$ 는 그 prefix의 함수 $\eta_{d+1}$ 의 조건부 법칙이다. 지금 문장은 `g:state`(prefix)가 $\eta_d$ 의 표본이라고 말하므로 `exact` 인 물리 문장으로는 틀리게 읽힌다. 같은 카드 본문의 "각 자식의 $\eta_{d+1}^{(\ell)}$ 의 조건부 법칙이 정의상 $\eta_d$" 는 옳다.
- 제안: "… 깊이마다 '자식 상태들에 딸린 다음 단계의 field 법칙 $\eta_{d+1}$(마지막 단계에서는 field $x$)이 서로 독립으로 같은 법칙 $\eta_d$ 에서 뽑힌다'는 계층 cavity field 사슬로 그대로 재현된다."

### F2. 용어 규율 — `comp:encoding.s2` (math) · 낮음
- 카드: "모든 상태 공간이 standard Borel이므로".
- 원문 52–53 "All state spaces are standard Borel". SCHEMA 용어 규율 2: "상태"는 `g:state` 하나만 가리킨다.
- 여기의 "state space"는 확률변수의 값 공간이지 prefix가 아니다. 제안: "모든 값 공간(변수들이 값을 갖는 공간)이 standard Borel이므로".

### F3. 낡은 대조 — `comp:section` (본문 "인터페이스 대조"의 §5 항) · 낮음
- 카드: "다만 §8은 [[x:cavity-bounded]](200, 215–216, 226)와 [[cavity:grid]](162 …), [[cavity:increment.s4]]의 상계(215–216)도 `\ref` 없이 쓴다. cavity:section의 provides는 x:cavity-bounded를 §9 쪽에만 적는다".
- 지금 `cavity:section` 의 "밖에 내주는 것" 표에는 `cavity:grid`(comparison.tex 162), `x:cavity-bounded`(200), `cavity:increment.s4`(215–216) 행이 이미 있다(§5 검토 반영으로 들어간 것으로 보인다). 그래서 이 문단은 지금 파일과 맞지 않는다. 아직 빠진 것은 아래 (a)에 적었다.
- 제안: 이 항을 "(a)" 의 결론대로 고친다: 표에는 있고, `provides` 줄과 123·226행만 빠져 있다.

### F4. 진술의 정의역 — `x:reduction-power-mean-scaling` (math) · 낮음
- 카드: "$0\le d<r$ 과 양의 $V,V'$ 에 대해 … (b) 동차성: $\lambda>0$ 이 물리적 disorder만의 함수이면".
- 원문: model.tex 92–95 (정의), 122–127 ("finite … power-mean operators preserve pointwise multiplicative bounds"), reduction.tex 34–35 "root-measurable bounds".
- 두 가지. (i) "양의 $V$" 만으로는 $T_dV$ 가 유한하지 않을 수 있고 그러면 결론의 $\log$ 차가 뜻이 없다. 쓰이는 곳의 $V_{\rm s},V_{\rm e}$ 는 (2.12)로 물리 disorder만의 함수인 양의 상수 사이에 끼어 있다. 진술에 "$V,V'$ 는 물리 disorder만의 함수인 양의 유한 상수 사이에 있다(쓰이는 곳에서는 (2.12))"를 넣는다. `uses` 에 `model:trial-bounds` 를 더하면 된다(순환 없음). (ii) (b)는 $\mathscr F_0$-가측인 $\lambda$ 전체에서 성립하고(같은 증명), 원문의 낱말 "root-measurable"은 그쪽이다. 카드는 본문에서 이것을 설명하지만 진술은 좁다. 틀리지 않았고 쓰이는 곳에는 충분하다. 진술을 "$\mathscr F_0$-가측(특히 물리 disorder만의 함수)"으로 넓히면 원문 낱말과 맞는다.
- (a), (b)의 증명과 결론 $\lvert\log T_0V'-\log T_0V\rvert\le\delta$ 는 다시 유도해 확인했다. 옳다.

### F5. 구조 — `comp:shape-error-bound`, `comp:shape-error.s1` (`source`, ID) · 낮음
- `comp:shape-error-bound` 는 `source: [131, 153]` 한 범위를 가진 `step` 이고 자식 잎은 140–142, 142–148, 149–153을 덮는다. 131–139(고정 $\eta$, $\mathfrak S_k$ 의 정의, 주장의 식)는 어떤 잎에도 없다. 정리 환경이 아니라 기계 검사는 통과하지만, SCHEMA "잎 `step`의 범위를 합치면 부모 증명 범위를 빠짐없이 덮어야"와 맞추려면 `source` 를 진술 `[131, 139]` 와 증명 `[140, 153]` 두 범위로 나누는 것이 정리류 카드의 관례와 같다.
- `comp:shape-error` 의 자식이 `[comp:shape-error-bound, comp:shape-error.s1]` 이라 둘째 단계의 ID가 `.s1` 이다. 적법하지만 "s1 = 첫 단계"로 읽힌다. 본문에 한 줄("첫 단계는 식 라벨을 ID로 쓰므로 `.s1` 이 둘째 단계다")을 더하거나 `.s2` 로 바꾼다.
- 구조 자체(본문 주장 123–156을 카드로 세우고 식 라벨을 ID로 쓴 것)는 적절하다고 본다. 아래 "분해".

### F6. 빠진 행 — `comp:section`, `reduction:section` ("밖에 내주는 것" 표) · 낮음
- 원문: overview.tex 40 "(\cref{comp:section})", decorrelation.tex 13 "the comparison with independent messages in \cref{comp:section}"(예고), overview.tex 51 "(\cref{reduction:section})", cavity.tex 11 "Until \cref{reduction:section}"(예고).
- 두 표에 이 행들이 없다(`reduction:section` 은 cavity.tex 11을 "받는 것" 표에만 적는다). 다른 섹션 카드는 overview.tex의 참조를 `provides` 에 적는다. 제안: 네 행을 더한다.

### F7. 유형 — `comp:insertion-comparison.s3` (`abstraction: weakening`) · 낮음, 확신 낮음
- 카드 physics: "차수마다 이웃을 독립 사본으로 바꾸는 비용은 tree 평균한 multioverlap 요동이고, 그것은 극한에서 사라진다."
- 같은 내용을 말하는 `comp:shape-error`, `comp:insertion-comparison`, 규칙 P9·P11은 모두 `approximation` 이다("사라진다"가 $\lim_L\limsup_N$ 과 선택된 수열 안에서만 맞음). 이 카드만 `weakening` 이다. gap이 범위를 적고 있으므로 `approximation` 으로 맞추는 것이 원칙 1과 일관된다.

### F8. "작성자" 표시 누락 — `math` 칸에 표시 없이 보탠 문구 · 낮음
모두 옳고 필요한 보탬이지만 `math` 칸 안에 원문에 없는 문구가 표시 없이 들어 있다.
- `comp:shape-error-bound`: "$L$, $\eta$, $N$ 에 무관한 $C_k$ 가 있어", "($\mathcal A_{L,\eta}z=z$)". 원문 133–140은 "$C_k$" 와 "has no depth coordinates"만 적는다. 무관성의 근거는 trees.tex 469–471이다(본문에는 설명이 있다).
- `comp:low-increments`: "그 수열 위의 모든 $N$ 에 대해". 원문 12–15는 식만 적는다. 근거는 perturbations.tex 299 "Relabeling the tail proves (i)"다.
- `comp:shape-error`: "안쪽 $\mathbb E$ 는 $Q_k$ 로 뽑은 tree $\mathcal T$ 를 고정한 채 root와 그 tree의 표본추출에 대한 기대값이다". 근거는 trees.tex 48–49.
- `comp:encoding.s4`: "여기서 $\tau^a$ 는 trial label 하나의 leaf $a$ spin이다". 원문은 $\tau$ 를 정의하지 않는다.
- `x:comp-standing`: "그 크기의 선택된 벡터를 $\mathbf u_{L,N}$ 으로 쓴다"(표기는 14행에 처음 나오고 이 카드의 `source` 는 8–12).
- 제안: 각 문구 뒤에 "(작성자; 근거 …)"를 붙인다.

## 극한 순서 (확인 2)

작성자의 장부를 원문과 맞춘 결과다. 어긋나는 곳은 없다.

| 극한·매개변수 | 취해지는 카드 | 원문 |
|---|---|---|
| $\varepsilon>0$ 고정, 깊이 $L$ 마다 선택된 수열 | `x:comp-standing` | 8–12 "Fix $\eps>0$. At each depth $L\ge2$ … The choices may depend on $L$" |
| (8.1)이 수열 위 모든 $N$ 에서 | `comp:low-increments` | 13–15; perturbations.tex 258, 299 |
| $\eta$ 고정 → $\limsup_N$(고정 $L$ 의 수열) → $L\to\infty$ → $\eta\downarrow0$ | `comp:shape-error-bound`, `comp:shape-error.s1` | 130–131, 153–156 "first at fixed $\eta$, taking the fixed-$L$ limit in $N$ before $L\to\infty$, and then let $\eta\downarrow0$" |
| $M$ → $q$ → ($N$, $L$) | `comp:insertion-comparison.s2`–`s4` | 198–199, 211–213, 218–221 "first choose $M$ …, then $q$ …, and then take the limits in $N$ and $L$" |
| 고정 $L$ 에서 수열 위 $\limsup_N$ | `comp:bounded-lower.s1` | 236–243 "at every fixed $L$ … The inner limit uses that depth's selected sequence" |
| $L\to\infty$, 그다음 $\varepsilon\downarrow0$ | `comp:bounded-lower.s2` | 243–245 |

- 선택된 수열이 $(L,\varepsilon)$ 에 의존한다는 점과의 양립: `comp:shape-error` 와 `comp:insertion-comparison` 은 고정 $\varepsilon$ 의 진술이고 $L$ 마다 다른 수열 위의 $\limsup_N$ 값을 $L$ 의 수열로 본 것이므로 문제가 없다. $L\to\infty$ 의 수렴이 $\varepsilon$ 에 균일할 필요도 없다: $L\to\infty$ 뒤에 남는 부등식 $A\le\underline F+2\varepsilon$ 에는 오차항이 없고 $A$, $\underline F$ 가 $\varepsilon$, $L$, 수열과 무관하기 때문이다(`x:comp-standing` 본문, `comp:bounded-lower.s2` 본문이 이것을 적는다). `decor:overlap-concentration` 은 임의의 선택(임의의 $\varepsilon$)에서 성립한다(decorrelation.tex 4–8).
- $\eta$, $M$, $q$ 의 지위: $\eta$ 는 좌변이 $\eta$ 에 무관한 부등식 (comp:shape-error-bound)의 보조 매개변수이고($\limsup_L\limsup_N\le C_k\eta$ 가 모든 $\eta$ 에서 성립), $M$, $q$ 는 $N$, $L$ 과 무관한 오차만 남기는 절단이다. 셋 다 `comp:bounded-lower` 의 조립에는 나오지 않는다는 작성자의 서술은 옳다. `comp:section` gap (1)의 "안쪽에서 … 먼저 소진된다"는 $\eta$ 에 대해서는 "먼저"가 아니라 "안쪽 명제 안에서 $L\to\infty$ 뒤에"가 정확하다. `comp:bounded-lower` 본문의 표현("이미 소진되어 $\eta$, $M$, $q$ 없는 진술로 들어온다")이 더 낫고 그쪽으로 맞추기를 권한다(지적으로 세지 않았다).
- 결론이 모든 $N$ 의 liminf라는 것: 원문 11–12 "Retain $\underline F$ for the liminf over *all* system sizes". 카드 서술 그대로다.

## 작성자가 보탠 것의 재계산 (확인 4)

- `comp:insertion-comparison` 의 조립된 부등식: 차수 $k$ 항의 계수 $(-1)^{k-1}/k$ (trees.tex 226–229, $t=1$), 관측량 $\mathbf1_{\{K\le M\}}\prod_aD^a$ 의 절댓값 $\le c^k\le1$, label 수 $\le pM$(site 삽입 $(p-1)K_{\rm s}$, bond 삽입 $pK_{\rm b}$), 절단 오차는 쪽마다 $\sum_{k>q}c^k/k$, 절단 밖은 쪽마다 $\mathbb E[(H+BK)\mathbf1_{\{K>M\}}]$. 합이 카드의 식이다. $\lvert\Delta_N-\mathcal B_{L-1}\rvert\le\sum_{\rm s,b}\lvert\mathbb E\log Y_0-\mathbb E\log\widetilde Y_0\rvert+o_N(1)$ 도 (5.5)와 trial 항등식에서 나오고 $o_N(1)$ 은 $L,\mathbf u$ 에 균일하다(cavity.tex 55). 옳다.
- `comp:shape-error-bound.s2` 의 깊이 축소: $\sum_{\mathbf q\,\text{regular}}Q_k(\tau,\mathbf q)z(\mathbf q')\le C_kL^{-a}\sum_{\mathbf q\,\text{regular}}z(\mathbf q')\le C_kL^{-a}L^{a-a'}\sum_{\mathbf q'\,\eta\text{-regular}}z(\mathbf q')=C_k\mathcal A_{L,\eta}z$. 사영이 regular를 $\eta$-regular로 보내는 것은 trees.tex 480–481·511–513, 섬유의 크기는 좌표 하나당 $L$ 이하, $z(\mathbf q')$ 가 $(U,\mathbf q')$ 만의 함수인 것은 trees.tex 38–39. 깊이의 범위($0\le d<L$)와 엄격한 증가 조건도 두 절에서 같다(decorrelation.tex 19–20). 옳다.
- `comp:shape-error-bound.s3` 의 Cauchy–Schwarz 두 번과 질량 $\le1$ (decorrelation.tex 37–43): 옳다. `comp:shape-error.s1` 의 $\limsup$ 과 유한합·제곱근의 교환: 옳다.
- `comp:patterns.s2`: $\lVert\pi-\bar\pi\rVert_{\rm TV}=\frac12\sum_{\boldsymbol e}\lvert\cdot\rvert\le\frac12\sum_{S\ne\varnothing}\lvert R_S-\mathbb ER_S\rvert$. 옳다.
- `s1.s1` 의 시행 kernel과 반복 지표: 깊이 $d$ 변수가 $\eta_d$, 깊이 $r$ 변수가 $x$ 라는 것은 trees.tex 26–27이 직접 말한다. reservoir 쪽에서 index가 겹쳐도 복원추출이라 조건부 법칙이 $\pi^{\otimes a}$ 이고(comparison.tex 110–111), trial 쪽 독립 label이 $\bar\pi^{\otimes a}$ 이므로 겹치는 index를 독립 label로 바꾸는 것이 `comp:patterns` 가 비교하는 바로 그 두 법칙이다. 읽기는 옳다.
- `s1.s2`: $m_L=1$(cavity.tex 18), $\mathbb E_\tau e^{\sum_j\theta_j}=\prod_je^{U_{\theta_j}}$, $Y_{d}=(K_{d+1}Y_{d+1}^{m_{d+1}})^{1/m_{d+1}}$ 와 (2.10)의 대응. 옳다.
- `s1.s3`: 조건부 독립 인자의 인수분해, $Y_{L-1}^{(j)}=C_{\theta_j}$, Wald($K_{\rm b}\sim\mathrm{Pois}(\alpha(p-1))$, cavity.tex 67), $\mathbf m^{(L)}$ 과 $\zeta_{L,N}\in\mathcal M_L=\mathcal M_{r+1}$ 이 (2.11)의 정의역 안. 옳다.
- `s2`: $D\in[-\tanh C,\tanh C]$ ($e^{\pm C}/\cosh C-1=\pm\tanh C$), $\log z$ 의 상쇄는 trees.tex 107–110의 동차성(증명은 "backward induction in (tree:Y-recursion)"이라 trial kernel에도 그대로 적용된다). 옳다.
- `s4`: reservoir 쪽 상계는 cavity.tex 108–111, trial 쪽은 (2.12)와 $\lvert\log T_0C_\theta\rvert\le B$. 옳다.
- `comp:bounded-lower.s1`: $\mathcal B_r\in\log2\pm(H+\alpha pB+\alpha(p-1)B)$, $\lvert F_N\rvert\le\log2+\alpha B+H$. 옳다.
- `comp:encoding.s1`: $q_x$ 의 평균 $\tanh x=\langle\sigma_i\rangle$; 균일 site는 reservoir의 backward logarithm에 들어가지 않으므로 tilt가 바뀌지 않는다(trees.tex 137–140 "Additional root variables remain quenched"). `s2`: $\eta_d\in\mathcal M_{r-d}$, $L=2$ 의 경우. 옳다.
- `reduction:stability.s1`–`s3`: 결합(같은 개수·index, 같은 $k$ 와 message), $\mathbb E\Lambda=\alpha ND+Nd$, $\delta$ 의 기대값 $d+\alpha pD$, edge 쪽 $\alpha(p-1)D$, 상수 이동의 $-\alpha p\mathbb Ec+\alpha(p-1)\mathbb Ec$. 옳다.

## "작성자 읽기"의 판단 (확인 5)

1. **전변동 거리 = $\ell^1$ 노름의 절반**: 근거 있음. comparison.tex 117의 $\frac a2$ 와 119 "costs at most twice total variation"이 이 정규화에서만 (comp:pattern-error)의 계수 $a$ 를 준다.
2. **시행 쪽 tree 표본 법칙**: 근거 있음. comparison.tex 71–72 "the branching version of \eqref{model:chain}"에 trees.tex 26–27(시행 사슬의 깊이 변수)과 32–33("different children are drawn independently using the appropriate kernel")을 합치면 카드의 읽기가 된다. 다른 읽기는 찾지 못했다.
3. **215행 "on both sides"**: reservoir 쪽과 trial 쪽으로 읽은 것이 맞다. 213행 "on either side"가 같은 뜻으로 쓰이고, 두 삽입은 198행에서 "either insertion"이라 부르며, 217행의 계수 2가 두 쪽의 합이다.
4. **"root-measurable"**: trial 쪽 root는 $\eta_0$ 들과 물리 disorder이므로 $\mathscr F_0$-가측으로 읽는 것이 맞다. 실제로 필요한 $\delta$ 가 물리 disorder만의 함수라는 관찰도 맞다. 진술을 원문 낱말에 맞추는 제안은 F4 (ii).
5. 그 밖의 읽기(`comp:insertion-comparison.s3` 의 "두 쪽의 $Q_k$ 는 같은 법칙", `comp:encoding.s2` 의 유한합 논법, `x:comp-standing` 의 "$\varepsilon$ 고정")는 원문과 맞는다. 마지막 것은 8행에 그대로 있어 "읽기" 표시가 필요 없다.

## 분해 (확인 6)

| 증명 | 원문 | 잎 카드 | 판정 |
|---|---|---|---|
| `comp:encoding` | 27–83 | s1 27–43, s2 44–57, s3 58–72, s4 73–83 | 빠짐없음 |
| `comp:patterns` | 99–121 | s1 99–110, s2 111–121 | 빠짐없음 |
| `comp:shape-error` | 131–156 | bound.s1 140–142, bound.s2 142–148, bound.s3 149–153, s1 153–156 | 논리는 빠짐없음. 131–139는 비잎 카드에만 있음(F5) |
| `comp:insertion-comparison` | 170–223 | s1.s1 170–176, s1.s2 178–180, s1.s3 181–196, s2 198–203, s3 205–213, s4 215–223 | 빠짐없음 |
| `comp:bounded-lower` | 233–246 | s1 233–242, s2 243–246 | 빠짐없음 |
| `reduction:stability` | 28–43 | s1 28–32, s2 33–37, s3 38–43 | 빠짐없음 |

`comp:shape-error` 를 카드로 세운 구조: 적절하다. 원문 123–124가 "We need the following consequence of the decorrelation theorem"이라 진술하고 210행과 규칙 P11이 식 라벨로 인용하므로 독립 노드여야 한다. ID가 식 라벨인 것은 SCHEMA("원문에 `\label`이 있는 노드는 그 라벨이 ID")와 맞다. `kind` 는 `proposition` 이어도 무방하다. 첫 단계에 `comp:shape-error-bound` 를 준 것도 같은 규칙과 SCHEMA "증명 안의 식 라벨을 다른 노드가 인용하면 … 그 식을 담은 단계 카드"에 맞고, 규칙 표의 "규칙으로 못 옮긴 것"이 이미 이 ID를 가리킨다.

## §9의 겹침 처리 (확인 7)

- **적법성**: SCHEMA는 부모가 하나여야 한다고 요구하지 않는다. `check.py` 는 부모를 집합으로 다루고(181–184행) `build.py` 는 "상위: model:section, reduction:section"으로 둘 다 보여 준다(516–518행). 포함 검사도 reduction.tex 45–87을 `main:theorem.s1`–`s4` 로 덮은 것으로 센다. 적법하다고 본다. reduction.tex 45–87을 겹쳐 쓰지 않은 판단도 옳다.
- **문제가 될 수 있는 곳** (모두 낮음):
  1. 의존 검사는 조상의 `uses` 를 물려준다. `main:theorem.s*` 가 이제 두 섹션의 `uses` 를 모두 물려받으므로 45–87행의 `\ref` 검사가 느슨해진다. 지금은 `main:theorem` 자신의 `uses` 가 필요한 것을 다 가지고 있어 실제로 가려지는 것은 없다.
  2. 섹션을 한 점으로 줄인 그림(증명 지도)에서는 `model:section` → `comp:bounded-lower`·`reduction:stability`(model:section의 `uses`)와 §8·§9 → §2 정의들이 맞물려 섹션 단위로는 순환이 된다. 카드 단위 `uses` 그래프에는 순환이 없다(기계 검사 통과). 지도를 다시 그릴 때 `main:theorem` 을 §2의 진술 노드와 §9의 증명 노드 어느 쪽에 놓을지 정해야 한다. 증명 단계 s1–s4는 §9 쪽에 그리는 것이 원문 위치와 맞다.
  3. 섹션별 카드 수를 세는 곳에서 `main:theorem` 과 그 단계 4장이 두 번 세어진다.
  4. `main:theorem` 본문의 마지막 문단("§9 카드를 쓸 때 겹쳐 쓰지 않도록 조율이 필요하다")은 이제 해결된 메모다. 고치는 쪽에서 "reduction:section이 이 카드를 자식으로 건다"로 바꾼다.
- **`main:theorem.s1`–`s4` 와 `reduction:stability` 의 맞물림**: 맞는다. s3의 $\lvert\widehat I-I_K\rvert\le\alpha(2p-1)D_K+d_K$ 는 (reduction:trial-stability)를 모든 $r$ 과 시행 법칙에 균일하게 쓴 것이고, $\liminf_N\widehat F_N\ge I_K-\alpha D_K-d_K$ 는 (reduction:free-stability)와 `comp:bounded-lower`, 합 $2\alpha pD_K+2d_K$ 도 맞다. 안정성의 가정 "(2.1)을 만족하는 두 법칙"은 s1의 $\mathbb EB(\widehat\theta)\le2\mathbb EB(\theta)$ 와 잘린 법칙의 유계성이 채우고, 상수 이동의 가정 "적분 가능한 $c$"는 s1의 $\lvert c\rvert\le B(\theta)$ 가 채운다. `comp:bounded-lower` 의 가정(유계, 순열 불변, 유계 장)은 s2가 채운다. `reduction:stability` 는 `x:cavity-bounded` 를 쓰지 않으며 이것은 cavity.tex 11 "Until reduction:section"과 맞다.

## 인터페이스와 `uses` (확인 8)

- 34장의 `uses` 를 본문이 실제로 쓰는 것과 손으로 맞췄다. 식 라벨 인용은 모두 그 식을 담은 카드가 `uses` 에 있다: (comp:single-label-moments) → `comp:patterns.s1` 이 `comp:encoding.s4`; (comp:shape-error-bound) → `comp:shape-error.s1`; (comp:shape-error) → `comp:insertion-comparison.s3`; (comp:low-increments) → `comp:bounded-lower.s1`; (cavity:identity)·(tree:Y-recursion)·(model:vs)·(model:chain)·(model:trial-bounds)도 같다.
- 쓰지 않는데 든 의존: `x:comp-standing` 의 `x:cavity-bounded`, `cavity:grid`(원문 8–12는 말하지 않고 본문의 한 문장이 기댐), `comp:patterns` 의 `cavity:increment`(lemma 자체는 "new insertion disorder"를 추상적으로 말한다). 해롭지 않아 지적으로 세지 않았다.
- 순환 회피 설계는 지켜진다: `comp:bounded-lower` 와 그 단계는 `model:hamiltonian`, `model:chain`, `model:functional`, `x:model-depth-zero`, `model:trial-bounds` 만 넣는다.
- `comp:section` 의 "밖에서 받는 것" 표: 22행을 원문 행 번호와 대조했다. 맞는다(53–56은 54–56이 정확하지만 무해). "밖에 내주는 것"은 F6. `reduction:section` 의 두 표도 맞고 빠진 행은 F6.

### 의존 경고 2건 (comparison.tex 227 `\cref{model:section}`)

`comp:bounded-lower` 와 `comp:section` 이 `model:section` 을 `uses` 에 넣으면 `model:section` 의 `uses`(`comp:bounded-lower`)와 순환이 된다. 카드의 지금 처리(진술이 실제로 기대는 정의 노드 `model:functional`, `x:model-depth-zero`, `model:chain` 을 넣음)가 내용상 옳다: 227행은 "functionals defined in" 을 가리킬 뿐 주정리에 기대지 않는다. 카드를 고치지 말고 도구에서 받는 것이 옳다고 본다. 둘 중 하나:
1. `check.py` 의 의존 검사에 "섹션 라벨을 가리키는 `\ref` 는 `uses` 에 그 섹션의 자손이 하나 이상 있으면 충족"이라는 규칙을 더한다. SCHEMA의 의존 행에도 한 줄 적는다.
2. 그렇게 하지 않는다면 카드 본문에 적힌 사유(이미 `comp:bounded-lower` 에 있다)를 근거로 두 경고를 "알려진 예외"로 보고서에 남긴다.
1을 권한다. `model:section` 의 `uses` 에서 하류 노드를 빼는 방법은 주정리가 그 섹션의 자식이라는 사실을 가릴 뿐이라 권하지 않는다.

## 작성자가 보고한 다른 문서의 누락 (a)–(f)

- **(a) `cavity:section`**: 지금 파일의 "밖에 내주는 것" 표에는 `cavity:grid`(comparison.tex 162), `x:cavity-bounded`(200), `cavity:increment.s4`(215–216) 행이 **있다**. 빠진 것은 (i) `provides` 줄의 §8 목록(여전히 `cavity:increment`, `cavity:identity`, $A_{\rm s}$, $A_{\rm b}$, `x:cavity-tree-sampling` 뿐), (ii) `cavity:grid` 의 123행 사용($Q_k$ 의 깊이 분포가 $m_d=d/L$ 을 전제, trees.tex 460), (iii) `x:cavity-bounded` 의 215–216·226행. 작성자 보고는 일부만 유효하다(F3).
- **(b) `tree:section`**: 보고가 맞다. §8 행은 `tree:log-expansion`·꼬리, `tree:Q-rule`, `tree:regular-shapes`, `tree:averaging-remark`, (tree:Y-recursion)만 적는다. `tree:insertion` 의 동차성(203), `x:tree-sampling` 의 사영 일관성(142–150)과 자식의 독립(62), `tree:multioverlap`(78, 101–106), `x:tree-regular-shape`(141–143), `x:tree-extra-variables`(28)가 없다. 단 215–216의 단조성은 §8이 직접 부르는 것이 아니라 `cavity:increment.s4` 와 `model:trial-bounds` 를 거친다. 직접 쓰는 것은 203의 동차성이다.
- **(c) `pert:section`**: 보고가 맞다. §8 두 행은 `pert:selection`, `x:pert-selected-limits`, `x:pert-mark-specification`, `pert:factor` 만 적고 comparison.tex 11–12의 $\underline F$ 의 출처 `x:pert-increment`(perturbations.tex 249–253)가 없다. `x:pert-increment` 자신의 `provides` 에도 §8이 없다.
- **(d) `model:section`**: 보고가 맞다. 표는 comparison.tex 72/180/227/235와 reduction.tex 11/86만 적는다. `\ref` 없는 사용이 빠져 있다: `model:ve`(189), `model:power-means`(184–185; reduction.tex 34–35, 39–40), `model:functional`(166, 192; reduction.tex 16, 24, 40–42 — 표는 "기호로 쓴다"고만 적는다), `x:model-depth-zero`(229; reduction.tex 19), `x:model-message`(40, 60), `model:site-message`·`model:edge`(179–183; reduction.tex 33–34), `model:hamiltonian`(229; reduction.tex 15, 29). `provides` 줄은 뭉뚱그려 적고 있어 틀린 문장은 없다.
- **(e) `model:trial-bounds` 의 provides**: 보고가 맞다고 본다(확신 중간). model.tex 123–124 "the power-mean operators preserve pointwise multiplicative bounds"는 낱말로는 일반적이지만 그 자리에서 쓰이는 것은 (2.12)의 절대 경계다. reduction.tex 34–35가 필요한 것은 두 값 $V$, $V'$ 사이의 상대 경계이고 39–40은 상수 인자의 정확한 분리다. 그래서 "reduction:stability(power mean이 root-가측 한계를 보존)"는 이 카드가 주는 것보다 많이 적는다. 제안: "reduction:stability(차를 잡는 두 functional의 유한성; 상대 경계의 보존과 상수 분리는 x:reduction-power-mean-scaling)". 같은 이유로 `tree:section` 본문의 "그 곱셈 경계 보존은 §2가 스스로 진술한다(model.tex 123–127)"도 새 카드의 판단과 어긋나므로 함께 맞춘다.
- **(f) `g:order-of-limits` 의 기호 줄**: 기호 "$\lim_{\varepsilon\downarrow0}\lim_{\eta\downarrow0}\lim_{L\to\infty}\limsup_{N\to\infty}$"는 순서로는 틀리지 않다($\eta$ 는 $L$ 뒤, $\varepsilon$ 앞). 그러나 한 양의 네 겹 극한으로 읽히고, 그렇게 읽으면 틀린다: 하한을 닫는 부등식(comparison.tex 238–241)에는 $\eta$ 가 없고, $\eta$ 는 좌변이 $\eta$ 에 무관한 (comp:shape-error-bound)의 보조 매개변수이며, 선택된 수열은 $(L,\varepsilon)$ 에만 의존한다. 작성자의 보고가 맞다. 제안: 기호를 "바깥 조립: $\varepsilon\downarrow0\ \leftarrow\ L\to\infty\ \leftarrow\ \limsup_N$(그 $(L,\varepsilon)$ 의 선택된 수열). 안쪽 명제: (comp:shape-error)에서 고정 $\eta$ 로 $N$, $L$ 뒤 $\eta\downarrow0$; (comp:increment-comparison)에서 $M$, $q$ 를 먼저 고정"으로 두 줄로 나눈다. "뜻" 칸의 문장은 그대로 맞다.

## 규칙 P4, P8–P12와 L0, L1 수 5–7

두 섹션의 원문과 직접 대조했다. 어긋나는 곳은 **찾지 못했다**.
- P4: site Poisson$(\alpha p)$, bond Poisson$(\alpha(p-1))$, $\log2$, $o(1)$ 의 균일성, "선택된 수열에서 $\Delta_N$ 이 $\underline F$ 를 거의 넘지 않는다는 것만 쓴다"(comparison.tex 13–15, 236). 맞다.
- P8, P9: §8과 닿는 문장("독립성은 P9와 P11의 균일 무작위 site 표본추출에서 나온다", "singleton만 고정 $L$ 에서 성립", 선택된 수열, 고정 $\eta$)은 comparison.tex 99–121, 140, 153–156과 맞다. §7 안쪽의 세부(P8의 $1/(\eta L)$ 등)는 이 검토의 범위 밖이라 훑어보기만 했다.
- P10: $\zeta_{L,N}\in\mathcal M_L$, label 하나의 $\mathbb ER_S$, $N$·$L$·$\mathbf u$ 의존, $m_d=d/L$ 고정. 맞다.
- P11: (comp:pattern-error)의 꼴, $C_k(\eta+L^{-1})$, "고정 $\eta$ 에서 $N$, $L$ 순으로 보낸 뒤 $\eta\downarrow0$", "$M$ 과 차수 절단을 먼저 고정", exact인 부분의 범위. 맞다.
- P12: 두 상수, 균일성, $2\alpha pD_K+2d_K$, 상한은 원래 법칙에 적용. 맞다.
- L1 수 5–7: 수 6의 부등식 사슬과 "$\limsup_N$(그 $L$ 의 수열), $L\to\infty$, $\varepsilon\downarrow0$ 순", "$\eta$ 는 $L\to\infty$ 뒤에"가 원문과 맞다. 수 7도 reduction.tex 45–87과 맞다. L0에서 이 두 섹션에 닿는 문장(하한을 더해 등식, inf의 달성은 주장하지 않음)도 맞다.
- (f)의 기호 줄만 위 제안대로 고치면 된다.

## 통과 카드 (22장)

§8 (18장): `comp:encoding`, `comp:encoding.s1`, `comp:patterns`, `comp:patterns.s1`, `comp:patterns.s2`, `comp:shape-error-bound.s1`, `comp:shape-error-bound.s2`, `comp:shape-error-bound.s3`, `comp:insertion-comparison`, `comp:insertion-comparison.s1`, `comp:insertion-comparison.s1.s1`, `comp:insertion-comparison.s1.s2`, `comp:insertion-comparison.s1.s3`, `comp:insertion-comparison.s2`, `comp:insertion-comparison.s4`, `comp:bounded-lower`, `comp:bounded-lower.s1`, `comp:bounded-lower.s2`.

§9 (4장): `reduction:stability`, `reduction:stability.s1`, `reduction:stability.s2`, `reduction:stability.s3`.

| 섹션 | 카드 | 통과 | 지적이 걸린 카드 |
|---|---|---|---|
| §8 | 28 | 18 | `comp:section`(F3, F6), `x:comp-standing`(F8), `comp:low-increments`(F8), `comp:encoding.s2`(F2), `comp:encoding.s3`(F1), `comp:encoding.s4`(F8), `comp:shape-error`(F8), `comp:shape-error-bound`(F5, F8), `comp:shape-error.s1`(F5), `comp:insertion-comparison.s3`(F7) |
| §9 | 6 | 4 | `reduction:section`(F6), `x:reduction-power-mean-scaling`(F4) |
| 합 | 34 | 22 | 12 |

지적이 걸린 12장 가운데 `math` 칸의 식이나 진술이 틀린 카드는 없다.

## 확신이 낮은 지적

- F7(유형): `weakening` 과 `approximation` 의 경계에 대한 판단이다.
- (e): model.tex 123–124의 "pointwise multiplicative bounds"를 상대 경계까지 포함해 읽을 여지가 있다. 그렇게 읽으면 `model:trial-bounds` 의 provides는 틀리지 않고, `x:reduction-power-mean-scaling` 은 그 문장을 풀어 쓴 카드가 된다. 어느 쪽이든 39–40의 동차성은 §2에 진술이 없다.
