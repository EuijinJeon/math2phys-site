# 검토 2 — §10 consequences 카드와 overview 카드 (독립 검토)

대상: `cards/models.*.md` 14장, `cards/x.cons-*.md` 4장(§10, 18장), `cards/x.overview-*.md` 7장. 모두 25장.
기준: `source/sections/consequences.tex`(138줄)·`overview.tex`(51줄)·`model.tex`(140줄)·`introduction.tex`(86줄) 전체, `upper.tex` 1–40·112–128, `cavity.tex` 1–70, `reduction.tex` 1–20·40–87, `trees.tex` 1–30·286–340·393–420·455–525, `perturbations.tex` 1–30·250–270·426–450, `decorrelation.tex` 1–95·296–360·520–623, `comparison.tex` 1–140·155–175·205–246, `references.bib` 의 `OpenAIThreeSAT2026`. `layers/L0.md`, `L1.md`, `rules.md`, 용어집 네 항목, `uses` 가 가리키는 §2 카드 9장도 읽었다.
"확인"은 원문과 한 줄씩 대조했거나 손으로 다시 계산했다는 뜻이다.

기계 검사: `tools/check.py --sections consequences,overview --out <scratchpad>` 는 형식·정초·포함·연결·순환·사전·단면·용어 통과, 의존은 경고 2건인데 둘 다 `comparison.tex:227` 의 `\cref{model:section}` (`comp:bounded-lower`, `comp:section`)이고 이 25장과 무관하다. consequences.tex 필요한 99줄, overview.tex 0줄 모두 덮임.

## 요약

- 읽은 카드: 25 / 25 (머리말과 본문 모두).
- **§10 수식 전사**: 따름정리 10.1–10.3의 진술, 모형 정의, $\theta_\beta$·$h_\beta$, 짝수 $p$·$K$, "모든 $\beta>0$", $J$ 대칭·$J,H$ 독립, 독립 공정 부호·$W\ge0$ 이 부호와 독립, $\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert<\infty$·$\mathbb EW<\infty$, $\mathcal E_N$ 두 식, $Z_N(\beta)=\sum_\sigma e^{\beta\mathcal E_N}$, (10.1), 폭 $[g,g+\log2/\beta]$, "$-g$ 는 단위 가중치 SAT의 변수당 최소 위반 수 기대값의 극한"을 원문과 대조했다. `math` 칸에서 부호·계수·양화사·한정어가 어긋나는 곳은 **찾지 못했다**.
- **가정 확인 표**(`models:section` 본문, 지시문의 작성자 표): spin $a=\cosh\beta J$, $b=\tanh\beta J$, $f_\ell(s)=s$, $\lvert b\rvert<1$ a.s., 홀수 moment 0·짝수 moment $\ge0$, $B=\beta\lvert J\rvert$, $\lvert h\rvert=\beta\lvert H\rvert$ (원문 25–32). SAT $a=1$, $b=e^{-\beta W}-1$, $f_\ell=(1+\varepsilon_\ell s)/2$, $0\le-b<1$, $B=\beta W$, $h=0$ (원문 52–63). 한 항목씩 원문과 같고, 직접 계산해도 맞다(아래 "다시 한 계산").
- **`models:ground`**: "각 $\beta$ 에서 따로 inf, 우변의 극한 순서는 $N\to\infty$ 다음 $\beta\to\infty$, 폭 $[g,g+\log2/\beta]$" 는 원문 88–100, 112–123, 127–129와 맞다. inf와 극한의 교환을 원문보다 많이 말하는 곳은 없다. 다만 좌변 $g$ 가 $\beta=\infty$ 에서 직접 정의된 양이라는 점이 차이 칸에 빠져 있다(F6).
- **작성자가 보탠 계산**은 모두 다시 했다. **틀린 계산은 없다.** "$J$·$H$ 의 독립을 증명이 쓰지 않는다"는 읽기도 맞다(model.tex 21 "All families in this definition are mutually independent", 82 "Take independent … $\theta,\theta_1,\ldots$, and $h$").
- **분해**: 세 증명 모두 원문 순서 그대로 빠짐없이 덮는다(spin 24–30/30–31/31–34, sat 51–58/59–62/62–64, ground 103–111/112–119/120–123/123–125). `uses` 에 순환 없음, 없는 ID 없음, 빠진 필수 의존 없음.
- **과장**: §10 카드에 1RSB, 영온도 cavity 공식, satisfiability threshold 와의 연결을 원문보다 강하게 쓴 곳은 없다(유일한 언급은 `models:section` gap (5)의 "원문은 비교하지 않는다"). Remark 10.4는 원문이 말하는 만큼만 옮겼다.
- **overview**: 문단 카드 6장의 `math` 는 해당 줄을 빠짐없이 옮겼다(한 군데 "any" 누락, F2). "가리키는 곳"의 대상은 한 곳(F1)을 빼고 그 문장이 가리키는 본문 결과다. `uses` 에 예고가 든 곳 없음.
- **용어 규율**: "상태"는 `x:overview-step3` 에만 나오고 모두 `g:state`(보조 계층 prefix) 뜻이며 차이 칸 (3)이 물리적 pure state가 아님을 적는다. Ruelle, Ghirlanda–Guerra, stochastic stability, "clustering", "self-average", "처방된 tree 항등식", 주어로서의 "connected correlation", R번호는 25장에 없다. "ultrametric"은 `x:overview-strategy` gap (2)의 introduction.tex 76–77 영문 인용 한 곳뿐이다(`physics` 칸이 아니므로 규율 3에 걸리지 않는다).
- 지적 10건. 통과 15장, 지적이 걸린 카드 10장. **높음 0, 중간 1, 낮음 9.**

| 유형 | 건수 | 번호 |
|---|---|---|
| 틀림 (식·진술) | 0 | — |
| 구멍 (증명 분해) | 0 | — |
| 가리키는 곳 (표의 대상) | 1 | F1 |
| 부정확한 묘사 | 5 | F2, F3, F4, F6, F7 |
| 과장 (문구) | 1 | F5 |
| 한정어 누락 (`physics`) | 1 | F8 |
| "작성자" 표시 누락·문구 | 1 | F9 |
| 형식 (ID 접두사) | 1 | F10 |

| 심각도 | 건수 | 번호 |
|---|---|---|
| 높음 | 0 | — |
| 중간 | 1 | F1 |
| 낮음 | 9 | F2–F10 |

## 다시 한 계산 (모두 일치)

- $x=\pm1$ 에서 $e^{\beta Jx}=\cosh\beta J+x\sinh\beta J=\cosh\beta J\,(1+x\tanh\beta J)$. $p$ 가 짝수든 홀수든 $\prod_\ell s_\ell=\pm1$ 이라 성립한다. **짝수 $p$ 는 §10의 어느 증명에도 쓰이지 않는다.** 진술이 고정할 뿐이고(12, 38행), 필요한 까닭은 model.tex 3행이 $p$ 를 짝수로 고정하고 upper.tex 123–124("Since $p$ is even, convexity of $x\mapsto x^p$ makes the bracket nonnegative")가 그것을 쓰기 때문이다. 표의 "짝수 체수: 진술에서 고정"은 정확하다.
- (2.4)가 요구하는 것은 모든 $n\ge1$ 에서 $\mathbb E[(-b)^n]\ge0$ (유한 실수 기대값, model.tex 35–38). spin: $J$ 대칭 ⇒ $\tanh$ 가 홀함수라 $b$ 대칭 ⇒ 홀수 $n$ 에서 $\mathbb E[(-b)^n]=-\mathbb E[b^n]=0$, 짝수 $n$ 에서 $\mathbb E[b^n]\ge0$; $\lvert b\rvert<1$ 이라 유한. SAT: $W\ge0$, $\beta>0$ ⇒ $-b=1-e^{-\beta W}\in[0,1)$ ⇒ $(-b)^n\in[0,1)$ 점별.
- (2.3) 구조: spin의 $f_\ell(s)=s$ 는 결정적이라 독립 사본·$b$ 와 독립이 자명. SAT의 $f_\ell$ 은 $\varepsilon_\ell$ 이 i.i.d.라 독립 사본, $W\perp\varepsilon$ 이라 $b\perp f$. $f_\ell\in\{0,1\}$ 이라 $\lvert b\prod f_\ell\rvert\le\lvert b\rvert<1$.
- 위반 약속: $(1+\varepsilon_\ell s_\ell)/2=1\iff s_\ell=\varepsilon_\ell$, 아니면 0. 그래서 $I_\varepsilon(s)=1\iff$ 모든 $\ell$ 에서 $s_\ell=\varepsilon_\ell$. $e^{-\beta WI}=1+(e^{-\beta W}-1)I$ ($I\in\{0,1\}$). $B(\theta_\beta)=\beta W$ 는 $s=\varepsilon$ 에서 달성.
- $-H_N=\beta\mathcal E_N$: (2.2)에 $\theta_\beta$, $h_\beta$ 를 넣으면 두 모형 모두 성립.
- $\lvert g_N\rvert\le\alpha\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert$ (spin), $\le\alpha\mathbb EW$ (SAT): $\mathbb E\sum_{k\le M_N}\lvert J_k\rvert=\alpha N\mathbb E\lvert J\rvert$. 끼움 $\beta\max\mathcal E_N\le\log Z_N\le N\log2+\beta\max\mathcal E_N$.
- $\beta\to\infty$: 모든 $\beta$ 에서 $\limsup_Ng_N-\liminf_Ng_N\le\log2/\beta$, $g_N$ 균일 유계 ⇒ 유한한 극한 $g$. 환산 $I(\beta)/\beta\in[g,g+\log2/\beta]\iff f(\beta)\in[-g-\log2/\beta,-g]$ 도 맞다.
- 복원추출이라 한 clause 안에 같은 변수가 되풀이될 수 있다는 관찰: model.tex 10–11, 21–22와 맞다.
- 덧붙임(카드에 없음, 제안 아님): SAT 증명은 부호의 **공정함**을 쓰지 않는다. 쓰는 것은 $\varepsilon_\ell$ 이 i.i.d.이고 $W$ 와 독립이라는 것뿐이다. `models:spin` 의 "$J$·$H$ 독립" 읽기와 같은 종류의 관찰이다. 진술은 원문대로 "fair"를 유지해야 한다.

## 지적 (심각도 순)

### F1. 가리키는 곳 — `x:overview-closing` ("가리키는 곳" 표 2·3행) · 중간 (확신 중간)
- 카드: "깊이에 균일한 집중은 필요 없음 | [[decor:order-of-limits]] | 45–46", "예외적 tree의 확률이 사라져 평균으로 충분 | [[tree:regular-shapes]] (`tree:irregular-probability`), [[comp:shape-error]], [[comp:shape-error-bound]] | 44–45".
- 원문: overview.tex 43–46 "The estimates in Step~3 are averages over separated interior branching depths. The insertion expansion assigns vanishing probability to the exceptional trees, so these averages are sufficient for Step~4. No uniform concentration in the depth is needed." decorrelation.tex 613–622 (`decor:order-of-limits`): "All uncancelled small denominators … No rate of convergence in $N$ uniform in $L$ is used." trees.tex 516–524 (`tree:averaging-remark`): "… Together with \eqref{tree:irregular-probability}, this allows averaged estimates on regular depth assignments to be used in the logarithmic expansion."
- `decor:order-of-limits` 는 "$N$ 수렴 속도가 $L$ 에 균일할 필요가 없다"는 주석이다. overview 45–46은 앞 두 문장에 이어 "branching 깊이마다(균일하게) 집중할 필요가 없고 깊이 평균이면 된다"로 읽는 것이 자연스럽고, 카드의 `physics` 와 `x:overview-strategy` 표 C3("고정 깊이가 아니라 깊이 평균으로만")도 그렇게 읽는다. 그러면 표의 대상이 카드 자신의 읽기와 다른 진술을 가리킨다. "the depth"를 $L$ 로 읽으면 지금 대상이 맞으므로 확신은 중간이다. 또 44–45행의 본문 짝은 trees.tex 516–524의 `tree:averaging-remark`(깊이 평균을 $Q_k$ 평균으로 옮기는 바로 그 주석)인데 표에 없다.
- 제안: 2행에 [[tree:averaging-remark]] 를 더한다. 3행의 대상을 [[tree:averaging-remark]], decorrelation.tex 11–13·82–83("Averaging over depths is essential when combining the two estimates", `decor:section`/[[decor:overlap-concentration]])으로 바꾸고, `decor:order-of-limits` 는 "$L$ 에 균일한 $N$ 속도도 필요 없다는 관련 주석"으로 따로 적는다.

### F2. 부정확한 묘사 — `x:overview-step2` (math, gap 1), `x:overview-strategy` (표 2c) · 낮음
- 카드 (`step2` gap 1): "본문의 제약은 anchor와 추가 color들 사이의 split 깊이만 지정하고 다른 old replica와의 관계는 지정하지 않는다(trees.tex 310–313 …)". (`strategy` 표 2c): 'L1은 "anchor와 새 replica들 사이의 split 깊이"로 좁혀 적는다.' (`step2` math): "독립 mark가 처방된 branching pattern을 고른다."
- 원문: perturbations.tex 433–436 "A constraint $\mathcal C$ prescribes any consistent collection of their pairwise split depths, involving only the added colors and the anchor. It imposes no extra restrictions involving the other old replicas." trees.tex 311–313 "the anchor and the already colored paths are called reference paths. Constraints on the new color will only specify its splitting depths with these paths." overview.tex 22–23 "select **any** prescribed branching pattern".
- (a) "anchor와 추가 color들 사이"는 anchor–color 쌍만으로 읽힐 수 있다. 제약은 추가 color끼리의 쌍도 처방한다(§6 검토의 F2와 같은 지적이고, 그 뒤 L1 수 4와 P7은 "anchor와 새 replica들로 이루어진 집합 안의 쌍별 split 깊이(새 replica끼리 포함)"로 고쳐졌다). (b) 표 2c의 따옴표 안 문구는 지금 `layers/L1.md` 39행에 없다. 옛 문구이거나 의역이다. (c) `math` 칸은 전사인데 "any"가 빠졌다. 차이 칸이 바로 그 "any"를 논하므로 `math` 에 있어야 한다. (d) 근거 줄로는 trees.tex 310–313보다 제약의 정의인 perturbations.tex 433–436이 직접적이다.
- 제안: gap 1을 "본문의 제약은 anchor와 추가 color들로 이루어진 집합 안의 쌍별 split 깊이를 일관된 한 임의로 지정하고(추가 color끼리 포함), 다른 old replica가 관여하는 쌍은 지정하지 않는다(perturbations.tex 433–436, trees.tex 311–315)"로. 표 2c의 인용을 L1의 지금 문구로. `math` 를 "독립 mark가 임의의 처방된 branching pattern을 고른다"로. "가리키는 곳" 2행에 [[x:pert-colored-extensions]], [[x:tree-reference-paths]] 를 더한다.

### F3. 부정확한 묘사 — `x:overview-step3` (gap 1, 표 1행) · 낮음
- 카드 (gap 1): "두 결론 모두 고정 깊이가 아니라 $\eta$-regular 깊이에 대한 깊이 평균의 진술이고 극한 순서는 $\lim_L\limsup_N$ 이다".
- 원문: decorrelation.tex 81–83 "We then use a marker anchor to concentrate the remaining conditional mean **at each fixed depth**. Averaging over depths is essential when combining the two estimates." 562–569 "$\operatorname{Var}(M)\to0$ at each fixed $L,S,e$ … Division by $C(S,e)$ is made only at fixed $L$". 72–74 "For a singleton … $\operatorname{Var}(R_S)\to0$ as $N\to\infty$ at every fixed $L$."
- `physics` 가 든 두 결론은 "조건부 공분산의 소멸"과 "조건부 평균의 집중"이다. 뒤의 것(두 번째 항등식)은 고정 $L$·고정 깊이에서 성립하고, 깊이 평균이 필요한 것은 앞의 것과 둘을 합친 최종 결과다. 잎 하나인 경우도 예외다. "두 결론 모두"는 그래서 틀리게 읽힌다.
- 제안: "조건부 공분산의 소멸(`decor:conditional-concentration`)과 최종 결과(`decor:overlap-concentration`)는 고정 깊이가 아니라 $\eta$-regular 깊이 평균의 진술이고 극한 순서는 $\lim_L\limsup_N$ 이다(잎 하나인 경우만 고정 $L$). 두 번째 항등식이 주는 조건부 평균의 집중은 고정 $L$·고정 깊이에서 성립하며, 둘을 합칠 때 깊이 평균이 필요하다(decorrelation.tex 81–83, 562–569)."
- 곁들여: 표 1행 "계산의 본보기는 trees.tex 315–333 ([[tree:section]])"의 정확한 카드는 [[x:tree-cancellation-example]] (trees.tex 317–335)이다.

### F4. 부정확한 묘사 — `x:overview-step4` (gap 2) · 낮음
- 카드: "독립 사본의 근거는 국소 tree 구조나 상관 감쇠가 아니라 균일 site 표본과 multioverlap 집중이다(comp:patterns)."
- 근거: comparison.tex 87–96, 109–118(오차는 $a\sum_S\mathbb E\lvert R_S-\mathbb ER_S\rvert$). `layers/rules.md` 의 "확신이 낮은 대응" P11 항: "P9의 증명은 P8(보조 계층 prefix 안의 조건부 공분산 소멸)을 재료로 쓰므로 '상관 감쇠와 무관하다'고 읽으면 안 된다 … 쓰이지 않는 것은 그래프 거리에 따른 상관 감쇠다."
- 한정어 없는 "상관 감쇠가 아니라"는 규칙 표가 스스로 금한 읽기다. 같은 묶음의 `x:overview-step3` 가 "조건부 공분산이 사라진다"를 3단계의 재료로 적고 있어 두 카드가 어긋나 보인다.
- 제안: "…국소 tree 구조나 그래프 거리에 따른 상관 감쇠가 아니라…"로.

### F5. 과장 (문구) — `x:overview-strategy` (physics 마지막 문장) · 낮음
- 카드: "물리 유도가 물리적 pure state들의 계층과 그 안의 독립성으로 가정하는 부분을, 섭동으로 만든 보조 계층 위의 항등식으로 증명한다."
- 원문: introduction.tex 75–77 "Their branching is part of the construction; no ultrametric organization of the physical Gibbs states is assumed."
- "가정하는 부분을 … 증명한다"는 가정의 내용(물리적 pure state 계층, 그 안의 독립)을 증명한다는 뜻으로 읽힐 수 있다. 논문이 하는 일은 그 가정 없이 같은 공식에 이르는 것이다. 차이 칸 (2)가 바로잡고는 있지만 `physics` 문장 자체가 증명된 것보다 많이 말한다. L1 마지막 문단의 문구("논문은 이 계층을 가정하지 않는다. 대신 …")가 안전하다.
- 제안: "물리 유도가 물리적 pure state들의 계층과 그 안의 독립성을 가정해 건너뛰는 단계를, 논문은 그 가정 없이 섭동으로 만든 보조 계층 위의 항등식으로 대신한다."

### F6. 부정확한 묘사 (누락) — `models:ground` (gap 1), `models:section` (표의 "한정어" 칸) · 낮음
- 카드 (`models:ground` gap 1): "극한 순서는 각 고정 $\beta$ 에서 $N\to\infty$, 그다음 $\beta\to\infty$ 다." (`models:section` 표): "각 $\beta$ 에서 inf; 극한 순서 $N\to\infty$ 다음 $\beta\to\infty$".
- 원문: 88–91 "the limit $g=\lim_{N\to\infty}\frac1N\mathbb E\max_\sigma\mathcal E_N(\sigma)$ exists", 93–97 (10.1), 108–110 $g_N\le P_N(\beta)/\beta\le g_N+\log2/\beta$.
- 틀린 말은 아니다. 다만 이 순서는 (10.1)의 **우변**에만 해당한다. 좌변 $g$ 는 $\beta$ 없이 최댓값으로 직접 정의된 양의 $N$ 극한이고, 끼움에서 $g_N=\lim_{\beta\to\infty}P_N(\beta)/\beta$ 이므로 따름정리의 내용은 "두 극한 순서가 같은 값을 준다"이다. 지금 문구만 읽으면 영온도 값이 $N\to\infty$ 다음 $\beta\to\infty$ 의 순서로만 정의되는 것처럼 읽힌다. 물리 독자에게는 이 구별이 결과의 핵심이다.
- 제안: gap 1에 "(10.1) 우변의 순서다. 좌변 $g$ 는 유한 크기에서 최댓값을 먼저 취한 양의 $N$ 극한이고(끼움에서 $g_N=\lim_\beta P_N(\beta)/\beta$, 작성자 확인), 따름정리는 두 순서가 일치함을 말한다"를 더한다.

### F7. 부정확한 묘사 (부호) — `models:section` (physics 마지막 문장) · 낮음
- 카드: "이어서 $\beta\to\infty$ 로 보내 ground-state 에너지 밀도([[g:ground-state]])가 존재하고 그 inf를 $\beta$ 로 나눈 것의 극한임을 얻는다."
- 원문: 81행 $Z_N(\beta)=\sum_\sigma e^{\beta\mathcal E_N(\sigma)}$, 93–97행. inf$/\beta$ 의 극한은 $g$ (최댓값 밀도)이고 ground-state 에너지 밀도는 $-g$ 다. 자식 `models:ground` 의 `physics` 와 용어집 `g:ground-state`("ground-state 에너지 밀도의 부호를 바꾼 것")는 부호를 맞게 적는데 섹션 카드만 부호가 빠졌다. 또 "기대값의 밀도"라는 한정도 없다.
- 제안: "…ground-state 에너지 밀도(의 기대값) $-g$ 의 열역학 극한이 존재하고, $g$ 가 그 inf를 $\beta$ 로 나눈 것의 $\beta\to\infty$ 극한임을 얻는다."

### F8. 한정어 누락 — `models:sat` (physics) · 낮음
- 카드: "clause 밀도 $\alpha$ 의 random 짝수 $K$-SAT(…)에서, 각 clause $k$ 는 모든 자리 $\ell$ 에서 $\sigma_{i_{\ell,k}}=\varepsilon_{\ell,k}$ 일 때 위반되고 … $W$ 가 부호와 독립이고 $\mathbb EW<\infty$ 이면 …"
- 원문: 38–40 "Let $\varepsilon_1,\ldots,\varepsilon_K$ be independent fair signs and let $W\ge0$ be independent of the signs".
- `abstraction: exact` 인데 `physics` 에 부호가 "독립이고 공정하다"는 가정이 없다("random"에 묻혀 있다). `models:spin` 의 `physics` 는 대칭·독립·moment를 모두 적어 두 카드가 고르지 않다. `math`, L0, `g:named-models` 에는 있다.
- 제안: "…각 clause의 부호 $\varepsilon_{\ell,k}$ 는 독립인 공정한 부호이고, …"를 넣는다.

### F9. "작성자" 표시 누락·문구 — `models:spin` (본문), `models:section` (본문), `x:cons-3sat-remark` (본문, physics) · 낮음
- `models:spin` 본문: "짝수 $p$ 는 진술에서 고정한다(12행). 이것이 (2.1)–(2.4)와 함께 [[model:integrability]]의 전제다." 문장이 뜻하는 것은 "짝수 $p$ 는 (2.1)–(2.4)와 함께 주정리의 전제이고, 그 고정은 `model:integrability` 카드(model.tex 3행)가 담는다"일 텐데 지금 문구는 짝수 $p$ 가 (2.1)의 전제라고 읽힌다. 제안: 그렇게 고쳐 쓴다.
- `models:section` 본문: "두 경우 모두 $\max_s\lvert f(s)\rvert=1$ 이다." 맞지만 원문에 없다. "(작성자 확인)"을 붙인다.
- `x:cons-3sat-remark` 본문: "홀수 $K$ 가 제외되는 직접적인 이유는 주정리가 짝수 $p$ 를 고정하는 데 있다(…; 짝수 $p$ 는 상한의 볼록성에 쓰인다, [[upper:remainder]])." 내용은 맞다(model.tex 3, upper.tex 123–124). 원문 remark에 없는 설명이므로 "(작성자 읽기)"를 붙인다. `physics` 의 "**같은** Poisson 개수·복원추출 앙상블"에서 "같은"도 원문에 없다(원문 134–136은 "a Poisson number of clauses whose variable positions are sampled independently with replacement"라고만 한다). "같은 종류의"로 낮추거나 차이 칸에 작성자 읽기로 적는다.

### F10. 형식 (ID 접두사) — `x:cons-*` 4장 · 낮음
- 카드 (`models:section` 본문): "라벨 없는 노드는 `x:models-*` 대신 `x:cons-*` 로 써서 §2의 `x:model-*` 와 헷갈리지 않게 했다."
- 규약: SCHEMA.md 20행 "라벨 없는 노드 … `x:<섹션 접두어>-<짧은 이름>`". 다른 섹션의 관행은 모두 **라벨 접두사**다(`x:tree-*`, `x:pert-*`, `x:decor-*`, `x:comp-*`; 파일 stem `trees`, `perturbations`, `decorrelation`, `comparison` 이 아니다). 그 관행대로면 `x:models-*` 다. `cons` 는 라벨 접두사도 파일 stem(`consequences`)도 아니다.
- 이유(§2의 `x:model-*` 와 한 글자 차이)는 타당하고 검사도 통과하므로 바꾸라고 하지는 않는다. 다만 규약의 예외이니 SCHEMA.md "노드 ID"에 한 줄("§10은 라벨 접두사 `models:` 가 §2의 `model:` 과 헷갈리므로 `x:cons-*`")을 적어 두도록 조율에 넘긴다.
- 함께 확인한 것(문제 없음): 식 라벨 `models:ground-formula` 를 `models:ground` 카드가 담는 것은 진술 안의 식이고 `main:formula`/`main:theorem` 의 전례와 같으며, 인용하는 `x:cons-ground-scope` 가 `models:ground` 를 `uses` 에 넣었다. Remark 10.4의 카드 ID `x:cons-3sat-remark` 대 graph.json의 `x:consequences-L131` 은 `x:pert-order-of-choices` 대 `x:perturbations-L538` 과 같은 관행이고, 포함 검사는 원문 범위로 맞추므로 통과한다.

## 통과 카드 (15장)

§10: `models:spin.s1`, `models:spin.s2`, `models:spin.s3`, `models:sat.s1`, `models:sat.s2`, `models:sat.s3`, `models:ground.s1`, `models:ground.s2`, `models:ground.s3`, `models:ground.s4`, `x:cons-energy-score`, `x:cons-ground-scope`, `x:cons-standard-examples` (F10의 ID 주석만 해당).
overview: `x:overview-upper`, `x:overview-step1`.

지적이 걸린 10장: `models:section` (F6, F7, F9), `models:spin` (F9), `models:sat` (F8), `models:ground` (F6), `x:cons-3sat-remark` (F9), `x:overview-step2` (F2), `x:overview-step3` (F3), `x:overview-step4` (F4), `x:overview-closing` (F1), `x:overview-strategy` (F2, F5). 이 10장도 `math` 칸의 진술은 `x:overview-step2` 의 "any" 하나를 빼고 원문과 맞다.

## 항목별 의견

### ❓ 두 곳 (`x:cons-3sat-remark`)
"finite rational trials", "sign-indexed message pairs"의 뜻을 정할 근거는 원문에 **없다**. `source/` 전체에서 "rational"은 perturbations.tex 37, 475, 488(mark의 유리수값 함수)에만 나오고 이 remark와 무관하다. "sign-indexed"는 consequences.tex 136 한 곳뿐이다. `references.bib` 의 항목은 제목("Computing the Random 3-SAT Threshold")과 주소만 준다. 제목에 threshold가 있지만 remark는 그 논문의 soft-pressure 공식(Theorem 8.4)만 인용하므로, 카드가 threshold를 언급하지 않은 것이 옳다. ❓ 를 그대로 두고, 뜻을 추측해 채우지 않는 것이 맞다.

### `models:section` 의 "받는 것 / 내주는 것" 표 (지시 7)
원문과 맞다. `\ref` 는 8, 19, 33, 47, 63, 83, 112, 137행이 전부이고 표가 모두 담았다. `\ref` 없는 사용(25–33·52–63의 가정 확인, 32·63의 $B(\theta)$, 68–70·75–77의 $M_N$·$i_{\ell,k}$, 81의 $Z_N$, 95·114의 $r\ge0$)도 맞다. "내주는 것": `source/` 에서 §10을 가리키는 곳은 introduction.tex 34의 `\cref{models:section}` 하나뿐이고(29–34 문장), 다른 섹션의 증명은 §10을 쓰지 않는다. `x:model-moment-finiteness` 가 두 명명 예를 든다는 것도 확인했다(그 카드 gap).

### L1 대응표 (지시 10)
표의 26행을 overview.tex·L1.md·본문과 한 줄씩 대조했다. 대응과 "맞음/빠뜨림/더 말함" 판정은 표 2c의 L1 인용(F2)을 빼고 모두 맞다. "L1이 overview와 어긋나 틀린 곳은 없다"는 결론에 동의한다.

- **L1이 빠뜨린 것** — 세 건 모두 확인: (i) overview 4–6의 $\log a$ 정규화는 수 1에 없고 P2 차이 칸과 "규칙으로 못 옮긴 것"에만 있다. (ii) 27–29의 깊이 늦추기와 "같은 작은 인자"는 수 5에 없고 마지막 문단에 "$-\delta$ 대 $2+\delta$"로만 있다. 본문 근거는 trees.tex 328–332, decorrelation.tex 337–338·354–358이고 카드의 "$\delta$ 로 읽기"는 맞다. (iii) 32–33의 두 번째 항등식(marker anchor)은 수 5에 없다(본문 decorrelation.tex 81–82, 528–530, 537–569).
- **L1이 더 말한 것** — 모두 본문이 뒷받침한다: 수 2의 증분 식(cavity.tex 51–54), 수 3의 유한 tree moment 수렴(perturbations.tex 263–265), 수 6의 부등식 사슬과 $\eta\downarrow0$ 의 순서(comparison.tex 155–156, 234–245), 수 7의 상수 이동·순열 불변·맞붙임(reduction.tex 49–59, 80, 84–86).
- **"any prescribed branching pattern"(22–23)이 본문보다 넓은 요약이라는 판단**: 대체로 동의하되 "넓다"보다 "범위를 적지 않았다"가 정확하다. 앞 문장(21–22)이 "added replica paths"를 말하므로 문맥상 pattern은 추가 path들과 anchor의 것이고, 그렇게 읽으면 본문(perturbations.tex 433–436)과 어긋나지 않는다. overview가 생략한 것은 (a) "consistent"라는 조건, (b) 다른 old replica가 관여하는 쌍은 지정하지 못한다는 것, (c) mark 깊이가 $1,\ldots,L-1$ 뿐이라는 것(perturbations.tex 29)이다. 본문과 맞는 쪽이 L1이라는 결론은 옳다.
- **L1을 고칠 것인가**: 고칠 만하다. 셋 다 한 구절씩이라 단면이 부풀지 않는다. 제안 문구:
  - 수 1 "무엇을 하는가" 끝에: "$\log a$ 의 적분 가능성은 가정하지 않는다: 상수 $c=\theta(1,\ldots,1)$ 을 빼고 매개변수 $\lambda\uparrow1$ 로 정규화해 피한다(`upper:regularization`)." 근거 노드에 [[upper:regularization]] 추가.
  - 수 5 첫 문장을: "수 4의 항등식에 잎 개수 귀납을 걸되, target tree의 내부 branching 깊이를 한 칸씩 늦춘다([[g:depth-delay]]): 늦춘 깊이의 새 split마다 계수 $\delta=1/L$ 이 하나씩 나와 정규화 계수와 같은 크기가 되고, 절댓값 계수 합의 상대 한계(`tree:relative-charging`) 덕에 정규화 계수로 나눈 뒤에도 오차가 제어된다. 이렇게 상태 안 조건부 decorrelation(…)을 얻고, 이어서 marker anchor를 쓴 두 번째 항등식으로 남은 조건부 평균을 집중시켜(각 고정 깊이) $R_S$ 가 branching pattern으로 정해진다는 것을 얻는다."
  - (확신 낮음) 수 4의 "tree 표본 규칙·계수 한계(P6)": P6의 수학 노드(`tree:insertion`, `tree:log-expansion`, `tree:extension-expansion`, `tree:reference-total`)에는 절댓값 계수 합의 한계(`tree:charging`)가 없고 그것은 "규칙으로 못 옮긴 것"에 있다. "계수 한계(`tree:charging`; P8의 증명에 숨음)"로 적는 편이 표와 맞는다. overview 카드의 문제가 아니라 L1·rules 사이의 일이다.

### overview 카드의 `uses` 와 `main:theorem` (지시 9)
`uses` 에 든 것은 model.tex의 정의(`model:hamiltonian`, `model:power-means`, `model:chain`, `model:functional`, `model:integrability`, `model:factorization`, `model:positivity`)와 `main:theorem` 뿐이다. 뒤 섹션의 결과는 하나도 없고 모두 "가리키는 곳" 표로 뺐다. 순환 없음(검사와 손으로 확인: `main:theorem` 과 그 자손·조상은 overview 카드를 쓰지 않는다).
`main:theorem` 을 `uses` 에 넣은 것은 받아들일 만하다. overview.tex 50의 `\cref{main:theorem}` 은 원문 순서상 뒤를 향한 참조가 아니므로 의존 검사가 요구하고, 카드 본문이 "결론으로 이름을 부르는 진술이지 증명에 기대는 것이 아니다"라고 밝힌다. 다만 SCHEMA의 "`uses`: 진술이나 증명이 실제로 기대는 노드만"과는 뜻이 다르다(전략 요약이 자기가 요약하는 정리에 "기댄다"고 그래프에 그려진다). 증명 지도(DAG)를 그릴 때 `x:overview-*` → `main:theorem` 간선이 논리적 의존으로 보이지 않게, overview 묶음을 지도에서 빼거나 간선 종류를 달리하도록 조율에 알린다.

### `model:section` 에 overview를 거는 제안 (지시 11)
옳다. graph.json에서 `model:section` 의 `ranges` 는 `model.tex [1,140]` 과 `overview.tex [1,51]` 둘이고, `x:overview-L1`(subsection 2.2)의 `parent` 가 `model:section` 이다. 지금 `model:section` 카드의 `source` 는 model.tex만 담아 graph의 범위보다 좁다. `children` 끝에 `x:overview-strategy`, `source` 에 `{file: overview.tex, lines: [1, 51]}` 을 더하는 것이 SCHEMA("모든 카드는 원문 범위에 닿아야")와 graph에 맞다.
스크래치 사본에 이 두 줄을 넣고 `check.py --sections model,overview,consequences --root <사본>` 을 돌렸다: 모든 검사 통과, 의존 경고는 기존 2건 그대로, 순환 없음.
함께 고쳐야 할 문장: 그 카드 본문 끝 "**overview.tex.** … 이 카드 묶음은 model.tex만 다룬다", `math` 의 "받는 것 (밖에서). 이 섹션의 정의들은 다른 섹션에 기대지 않는다"(전략 소절은 뒤 섹션을 예고한다는 한 줄 추가), 그리고 `x:overview-strategy` 본문 "위치" 문단의 "자식으로 두지 않는다".

### `model:section` 표의 137행과 `\ref` 없는 사용 (지시 13)
작성자의 지적이 맞다. `model:section` 표의 "[[model:functional]] | consequences.tex 83, 137 ($\mathcal B_{r,\beta}$)"에서 83행은 $\mathcal B_{r,\beta}$ 의 정의지만 137행은 Remark 10.4의 "its trial functional differs from \eqref{model:functional}"이다. 제안: "consequences.tex 83 ($\mathcal B_{r,\beta}$), 137 (Remark 10.4: 동반 논문의 functional이 (2.11)과 다르다는 비교)".
`\ref` 없는 사용이 없는 것은 그 표의 제목이 "원문 `\ref` 기준"이라 틀린 것은 아니다. 다만 표 아래 "기호로만 쓰는 곳도 많다" 문장이 cavity.tex와 upper.tex만 들고 §10을 빼놓았다. 제안: "consequences.tex 25–33·52–63은 (2.1)–(2.4)를 `\ref` 없이 확인하고, 32·63은 $B(\theta)$, 68–81은 $M_N$·$i_{\ell,k}$·$Z_N$, 95·114는 $r\ge0$ 을 쓴다"를 더한다.
곁들여: `main:theorem` 의 `provides` 는 consequences.tex 19, 47, 112만 적고 `\cref` 가 있는 33, 63을 빼놓았다.

### L0과 용어집의 §10 서술 (지시 13)
- `g:named-models`: 원문 10–49와 맞다(두 따름정리 모두 "모든 $\beta>0$", 독립·대칭·moment, $W=1$).
- `g:ground-state`: 맞다. 정의 위치 "`models:ground`, consequences.tex 66–101"에 $\mathcal E_N$ 을 정의하는 새 카드 `x:cons-energy-score` 를 더하면 좋다.
- `g:positivity`: 맞다($-1<b\le0$, 원문 30–31, 40, 59–62; "하한에는 쓰이지 않는다"는 cavity.tex 13–14).
- `g:factorization`: 맞다. 물리 대응 칸의 "Viana–Bray에서 $a=\cosh\beta J$ …"는 모든 짝수 $p$ 에서 같으므로 "`models:spin` 의 모형에서(Viana–Bray는 $p=2$)"가 더 정확하다. 사소하다.
- L0: 따름정리 문장과 "정확한 진술" 다섯 줄 모두 원문과 맞다($-H_N=\beta\mathcal E_N$, $[g,g+\log2/\beta]$, "$-g$ 는 최소 위반 수 기대값의 극한", inf는 각 온도에서 따로). 한 군데(낮음): 본문의 "[[g:named-models|Viana–Bray 모형]], 대칭 coupling의 diluted 짝수 $p$-spin 모형, …이 여기에 든다"는 introduction.tex 29–31의 나열을 그대로 옮긴 것인데, 따름정리 10.1이 실제로 덮는 Viana–Bray는 $J$ 가 대칭인 경우($p=2$)뿐이다. 한정어가 뒤 항목에만 걸려 읽힌다. 같은 문단 뒤쪽의 "대칭 coupling의 diluted 짝수 $p$-spin 모형(Viana–Bray 포함)"처럼 쓰는 편이 안전하다. 원문 서론이 같은 식으로 쓰므로 틀림은 아니다.
