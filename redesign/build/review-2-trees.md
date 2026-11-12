# 검토 2 — §3 trees 노드 카드 (독립 검토)

대상: `cards/` 의 `tree.*.md` 30장, `x.tree-*.md` 9장, 모두 39장.
기준: `source/sections/trees.tex` 전체(525줄), 그리고 카드가 인용하는 `upper.tex` 36–128, `cavity.tex` 10–121, `perturbations.tex` 55–70·314–450, `decorrelation.tex` 14–30·55–62·268–352·405–422, `comparison.tex` 20–35·58–76·120–215, `reduction.tex` 26–42, `model.tex` 68–78, `overview.tex` 18–26.
"확인"은 원문과 직접 대조하거나 손으로 다시 계산했다는 뜻이다.

주의: `layers/glossary.md` 는 검토 중에 다른 작업으로 바뀌고 있었다. 용어집 인용은 내가 읽은 시점(494줄 판)의 문구다.

## 요약

- 읽은 카드: 39 / 39 (머리말과 본문 모두).
- `math` 칸의 식 전사: (tree:multioverlap), (tree:original-tilt), (tree:Y-recursion), (tree:updated-kernel), $\gamma_\beta$, (tree:density), (tree:first-variation), 해석적 경계의 $\vartheta$·$a_{d-1}$, $\partial\log W$, (tree:telescoping), (tree:Q-rule), (tree:log-series)·(tree:log-tail), 확장 규칙 (i)(ii), (tree:mixed-expansion), 두 path 예, (tree:one-reference-total), (tree:K), (tree:charging-bound), $J$, (tree:relative-charging), (tree:irregular-probability), (tree:assignment-probability)를 원문과 한 줄씩 대조했다. 부호, 계수, 첨자, 양화사, 합 범위, 가정이 어긋나는 곳은 **찾지 못했다**.
- 작성자가 보탠 계산은 모두 다시 계산했고 **틀린 것을 찾지 못했다**(아래 "작성자 보탬 검산").
- 증명 분해(lemma 여섯 개의 단계 카드 16장)에 구멍은 없다. 단계의 `source` 범위는 원문 증명을 빠짐없이 덮고 논리 순서를 바꾸지 않는다.
- `uses` 그래프(39장)를 손으로 따라갔다. 순환은 없다. 쓰지 않는 의존도 찾지 못했다. 빠진 의존이 세 군데 있다(F3, F4, F5).
- "상태"는 모두 깊이 $d$ prefix의 뜻으로만 쓰였다. Ruelle cascade, Ghirlanda–Guerra, ultrametricity, stochastic stability는 `physics`·`gap` 어디에도 없다(`tree:section` 본문의 "인용(MP01, PT04, Ruelle87)은 선행 연구의 소개"는 원문 8–10의 서지 언급을 옮긴 것이라 문제없다).
- 지적 10건. 통과 26장, 지적이 걸린 카드 13장.

| 유형 | 건수 | 번호 |
|---|---|---|
| 틀림 | 1 | F1 |
| 과장 | 3 | F6, F7, F8 |
| 구멍 | 0 | — |
| 누수 (인터페이스·`uses`·표 누락) | 5 | F2, F3, F4, F5, F9 |
| 유형·ID 오류 | 0 | — |
| 용어 | 1 | F10 |

| 심각도 | 건수 | 번호 |
|---|---|---|
| 높음 | 0 | — |
| 중간 | 3 | F1, F2, F3 |
| 낮음 | 7 | F4–F10 |

## 지적 (심각도 순)

### F1. 틀림 — `tree:multioverlap` (gap), `x:tree-path-kernels` (본문) · 중간
- 카드 (`tree:multioverlap` gap): "$\mathbb E$는 root(쓰이는 곳에서는 disorder와 매개변수)까지 평균한 것이다."
- 카드 (`x:tree-path-kernels` 본문): "쓰이는 곳에서 root는 disorder와 매개변수를 포함한다."
- 원문: cavity.tex 29–31 "Counts, types, and sites are root variables. The parameters of the factors are denoted by $\mathbf u$ and are fixed, not quenched random variables, unless a parameter average is explicitly taken." perturbations.tex 68–69 "We use $\pi$ to select deterministic parameter vectors, not as part of their quenched law." 섭동 매개변수는 root 변수가 아니고 $\mathbb E$는 그것을 평균하지 않는다. 삽입 매개변수 $t_j$ 도 무작위가 아니다. 용어집 `g:root`(읽은 시점)도 "섭동 매개변수 $\mathbf u$ 는 root 변수가 아니라 고정된 결정적 값"이라 적고, §7 카드 `x:decor-tree-sampling` 의 `math` 도 같다. 두 문장은 이들과 어긋난다.
- 제안: "root(쓰이는 곳에서는 물리 disorder와 섭동의 개수·type·site; 섭동 매개변수 $\mathbf u$ 는 root가 아니라 고정값이다, cavity.tex 29–31)"로 고친다. 두 곳 모두.

### F2. 누수 (표 누락) — `tree:section` ("밖에 내주는 것" 표, `provides`), `tree:insertion` (`provides`) · 중간
- 카드 (`tree:section` 표): §4 행이 "[[tree:log-expansion]] (…) | upper.tex 81, 97, 121"뿐이다. `tree:insertion` 의 `provides` 도 §5, §6만 든다.
- 원문에서 `\ref` 없이 §3을 쓰는 곳이 더 있다.
  - upper.tex 51–54 "Poisson differentiation gives $\varphi'(t)/\alpha$ as the expected insertion increment … Each increment has absolute value at most $B(\theta)$, since the recursion preserves multiplicative bounds." 증분이 $\log Y_0$ 라는 것은 `tree:insertion` 의 첫 문단이고, 상계는 그 단조성이다.
  - upper.tex 67–68 "the independent message process is appended to the unperturbed tilted tree, so its increment is $\log T_0V_{\rm e}$" — `x:tree-extra-variables` 의 약속(원래 tilt가 추가 변수의 prior를 바꾸지 않는다).
  - upper.tex 91–92 "It follows that (upper:regularization) is bounded in absolute value by $2B(\theta)$" — 단조성과 동차성.
  - cavity.tex 37–38 "Comparing pointwise with the unperturbed spin weight and then applying the recursion gives", 95–98 "Deleting or adding a perturbation changes the root logarithm by at most $\log2$ … An unused auxiliary variable can simply be integrated out with its prior" — 단조성과 `x:tree-extra-variables`.
  - perturbations.tex 64–65 "The factor bound permits termwise comparison through the power means" — 단조성.
  - (확신 낮음) reduction.tex 34–35 "The power means preserve these root-measurable bounds", 39–40 "the physical constants factor out of the spin partition function and of every power mean". 이것은 시행 functional의 $T_d$ 에 대한 말이라 §2의 `model:trial-bounds` 로 귀속하는 편이 맞을 수 있다. reservoir 쪽 안정성에 §3의 단조·동차가 쓰이는지는 확정하지 못했다.
- 이 섹션의 인터페이스는 `\ref` 로 잡히지 않는 사용이 많다는 것이 핵심인데, 표가 §5에 대해서만 그것을 적고 §4, §6의 같은 종류를 빠뜨렸다. `tree:section` 의 `math` "내놓는 것 (1)"에는 단조·동차가 들어 있으므로 진술 자체가 빠진 것은 아니다.
- 제안: 표의 §4 행에 `tree:insertion`(증분 $=\log Y_0$, 단조·동차; upper.tex 51–54, 91–92)과 `x:tree-extra-variables`(67–68)를 더하고, §5 행에 cavity.tex 37–38, 95–98, §6 행에 perturbations.tex 64–65를 더한다. `tree:insertion`, `tree:insertion.s3`, `x:tree-extra-variables` 의 `provides` 도 맞춘다.

### F3. 누수 — `x:tree-analytic-bounds` (math, `uses`) · 중간
- 카드: "위의 식들은 복소 영역 $\sum_j|t_j|\|D_j\|_\infty<1$ 위에서 해석적이며 … 더 작은 닫힌 영역에서 $A$의 argument는 …". `uses: [tree:Y-recursion, tree:insertion]`.
- `math` 는 $t_j$, $D_j$, $A$ 를 정의 없이 쓴다. $A_{\boldsymbol t}=1+\sum_jt_jD_j$ 와 "$D_j$ 는 유계 실수 path 함수"는 trees.tex 143–144에 있고, 그것을 담은 카드는 `tree:first-variation` 인데 `uses` 에 없다. "위의 식들"("The expressions", trees.tex 157)이 가리키는 대상($Y_d$ 와 그 로그 도함수)도 카드 안에서는 알 수 없다. SCHEMA: "`math`: `uses` 에 든 노드와 용어집만으로 읽혀야 한다."
- 제안: `math` 첫 문장을 "$A_{\boldsymbol t}=1+\sum_jt_jD_j$ ($D_j$ 유계) 에 대해 $Y_d$ 와 (tree:first-variation)의 식들은 …"로 풀어 쓰고 `uses` 에 `tree:first-variation` 을 넣는다. 순환은 생기지 않는다(`tree:first-variation` 의 `uses` 는 `tree:Y-recursion` 뿐이다).

### F4. 누수 — `tree:telescoping`, `tree:Q-rule` (math, `uses`) · 낮음
- 카드 (`tree:telescoping`): "$\sum_{\beta\in\operatorname{Int}(\mathcal T)}(n_\beta m_{d_\beta+1}-m_{d_\beta})=n$", `uses: [x:tree-sampling, x:tree-path-kernels]`. `tree:Q-rule` 은 `uses: [tree:telescoping]`.
- $d_\beta$(깊이), $n_\beta$(자식 수), $\operatorname{Int}(\mathcal T)$ 는 trees.tex 92–93, 102에서 lemma `tree:insertion` 의 진술 안에 정의된다. 두 카드의 `uses` 사슬에는 그 카드가 없다. `tree:Q-rule` 의 `physics` 는 "깊이 $d_\beta$, 자식 $n_\beta$개"라고 풀어 쓰지만 `math` 는 그렇지 않다.
- 제안: `tree:telescoping` 의 `math` 에 "$d_\beta$ 는 내부 vertex $\beta$ 의 깊이, $n_\beta$ 는 자식 수(root와 unary vertex 포함)"를 한 구절 넣는다. `uses` 에 `tree:insertion` 을 넣는 것보다 낫다(이 항등식은 삽입과 무관한 순수 조합 사실이다).

### F5. 누수 — `tree:reference-total.s1` (`uses`) · 낮음
- 카드: "제외되는 $j$개 자식이 그 vertex를 지나는 모든 reference를 담는다 …", `uses: [x:tree-extension-history, tree:telescoping]`.
- "reference"는 `x:tree-reference-paths`(trees.tex 311–315)의 말인데 이 단계의 `uses` 에 없다. 부모 `tree:reference-total` 에는 있어서 기계 검사(조상의 `uses` 인정)는 통과하겠지만, 단계의 `math` 를 혼자 읽을 수는 없다.
- 제안: `uses` 에 `x:tree-reference-paths` 를 더한다.

### F6. 과장 — `tree:regular-shapes` (physics, `abstraction: exact`) · 낮음
- 카드: "정해진 갈라짐 구조와 깊이 배정 하나의 확률은 $C_kL^{-a}$ 이하다: 각 갈라짐 깊이가 대략 균등하게 퍼진다."
- 원문: trees.tex 476–481은 배정 하나의 확률에 대한 상계만 준다. "대략 균등"은 하계까지 포함하는 말이고 증명되지 않았다. `gap` 은 "상계일 뿐이며 깊이 분포의 극한 꼴을 말하지 않는다"고 옳게 적었지만 `physics` 문장과 유형 `exact` 는 그대로다.
- 제안: "어느 한 깊이 배정에도 확률이 몰리지 않는다($C_kL^{-a}$ 이하)"로 바꾼다. 그러면 `exact` 를 유지할 수 있다.

### F7. 과장 (부정확한 묘사) — `tree:extension-expansion` (physics) · 낮음
- 카드: "anchor replica에 섭동을 넣고 그 anchor 인자를 상쇄한 뒤 $k$개 섭동 방향으로 미분하면 …"
- 원문: trees.tex 87–88 "Multiplying each spin weight by $A$", 98–103의 $W_{\mathcal T}(A)=\prod_aA^a\prod_\beta Y_\beta^{\gamma_\beta}$, 283–287의 좌변 $E_{\mathcal T}^{A_{\boldsymbol t}}[H/A_{\boldsymbol t}^{a_*}]$. insertion은 spin weight에 들어가므로 tree의 모든 leaf가 인자 $A^a$ 를 받고, 그 가운데 anchor의 인자만 분모로 지워진다. "anchor replica에 섭동을 넣는다"는 것은 이 구조와 다르다(§6에서도 perturbations.tex 368–370: 새 insertion의 score가 anchor에 붙고 "the anchor factor $A^{a_*}$ cancels").
- 제안: "insertion $A_{\boldsymbol t}$ 로 바뀐 tree 법칙에서 anchor의 인자 $A^{a_*}$ 만 상쇄한 기대값을 $k$개 방향으로 미분하면 …".

### F8. 과장 — `tree:Y-recursion` (physics, `abstraction: exact`) · 낮음
- 카드: "말단에서 $A$의 Gibbs 평균 $Y_{L-1}=K_LA$ … 바뀐 kernel은 깊이 $d$ [[g:state|상태]]의 무게를 $(Y_d/Y_{d-1})^{m_d}$로 재가중한다."
- 원문: trees.tex 67–80의 정의는 임의의 kernel 열에 대한 것이고(`uses` 도 `x:tree-path-kernels` 뿐이다), $K_L$ 이 Gibbs 분포인 것은 분배함수에서 만든 경우다(63–64). 또 $d=L$ 에서 재가중되는 것은 spin 배치이지 상태가 아니다(용어집 `g:state`, 읽은 시점: "깊이 $d$ $(0\le d<L)$ 까지의 prefix").
- 제안: `gap` 에 "Gibbs 평균이라는 읽기는 $K_L$ 이 Gibbs kernel인 경우([[tree:original-tilt]])의 것이다"를 넣고, "깊이 $d<L$ 에서는 상태의 무게를, $d=L$ 에서는 spin 배치의 무게를"로 나눈다.

### F9. 누수 — `tree:extension-expansion.s1`, `.s2` (math) · 낮음
- 부모 `math` 의 세 문장 "이 공식은 color의 어떤 고정된 순서에서도 성립한다", "같은 방향이면 $t^k$ 의 계수는 우변을 $k!$ 로 나눈 것", "빈 확장의 무게는 1"의 근거가 단계 카드의 **본문**에만 있다(s1 본문 "미분 순서를 바꿔도 좌변은 같으므로", s2 본문 "Taylor 계수의 정의다", 부모 본문의 $k=0$ 읽기). 원문 증명(trees.tex 298–304)도 이 셋을 따로 논하지 않으므로 분해의 구멍은 아니다. 다만 자식 `math` 만으로 부모 진술을 다 얻을 수 없다.
- 제안: s1의 `math` 끝에 "(작성자) 혼합 편미분은 순서에 무관하므로 어떤 color 순서로도 같은 좌변을 준다", s2의 `math` 끝에 "(작성자) $D_j=D$ 이면 좌변은 $s=\sum t_j$ 의 함수의 $k$계 도함수이므로 $t^k$ 계수는 우변$/k!$; $k=0$ 이면 유일한 항은 빈 history($c=1$, $\mathcal T_E=\mathcal T$)"를 올린다.

### F10. 용어 — `g:protected-leaf`, `g:reference-path` (제안 문서와 링크) · 낮음
- 읽은 시점의 `layers/glossary.md` 에 두 항목이 없다. 카드 여섯 장(`x:tree-differentiation-rule`, `tree:log-expansion`, `x:tree-extension-history`, `x:tree-reference-paths`, `tree:reference-total` 등)이 `[[g:protected-leaf]]`, `[[g:reference-path]]` 를 걸고 있어 용어집에 들어가기 전에는 "용어" 검사가 통과하지 못한다. 그 밖에 §3 카드가 건 `[[g:…]]` 와 `[[id]]` 는 모두 실재한다(확인).
- 제안 항목의 내용은 원문과 맞는다(뜻: trees.tex 180–181, 195–200; 311–315. 역할의 perturbations.tex 370–371, 433–436, decorrelation.tex 332–335도 확인). 두 가지만 고친다.
  - `g:reference-path` 뜻: "쓰지 않은 old path는 구별하지 않는다" → 원문은 "does not distinguish unused old paths **with the same specified ancestry**"(314–315)다. 한정어를 넣는다(카드 `x:tree-reference-paths` 의 `math` 는 옳게 옮겼다).
  - 용어집 `g:extension-history` 의 뜻 칸(읽은 시점)이 이미 reference path를 같은 줄(311–315)로 정의한다. 새 항목을 넣을 때 그쪽은 `[[g:reference-path]]` 를 가리키게 줄여 정의가 두 곳에 있지 않게 한다.

## 통과 카드 (26장)

원문과 줄 단위로 대조해 고칠 것을 찾지 못한 카드:

- 정의·약속: `x:tree-sampling`, `tree:original-tilt`, `x:tree-extra-variables`, `x:tree-extension-history`, `x:tree-reference-paths`, `x:tree-regular-shape`.
- 본문에 증명된 주장: `tree:first-variation`, `x:tree-differentiation-rule`.
- lemma와 단계: `tree:insertion.s1`, `.s2`, `.s3`; `tree:log-expansion`, `.s1`, `.s2`; `tree:reference-total`, `.s2`; `tree:charging`, `.s1`, `.s2`, `.s3`, `.s4`; `tree:regular-shapes.s1`, `.s2`, `.s3`.
- remark: `x:tree-cancellation-example`, `tree:averaging-remark`.

지적이 걸린 13장: `tree:multioverlap`·`x:tree-path-kernels`(F1), `tree:section`·`tree:insertion`(F2), `x:tree-analytic-bounds`(F3), `tree:telescoping`·`tree:Q-rule`(F4), `tree:reference-total.s1`(F5), `tree:regular-shapes`(F6), `tree:extension-expansion`(F7), `tree:Y-recursion`(F8), `tree:extension-expansion.s1`·`.s2`(F9). 이 13장도 `math` 의 식 자체는 원문과 같다. F10은 카드가 아니라 용어집 반영 절차의 문제라 세지 않았다.

## 작성자 보탬 검산

모두 직접 계산했다. 틀린 곳은 없다.

1. `tree:telescoping` 증명: root 아닌 vertex $v$ 는 깊이 $d_v-1$ 의 내부 vertex 하나의 자식이므로 $\sum_\beta n_\beta m_{d_\beta+1}=\sum_{v\ne\text{root}}m_{d_v}$. 여기서 $\sum_{\beta\in\operatorname{Int}}m_{d_\beta}$ 를 빼면 root 아닌 내부 vertex가 지워지고 root는 $m_0=0$ 이라 leaf만 남아 $n\,m_L=n$. 양수성도 맞다. 확인.
2. `tree:reference-total.s1` 부분 tree 판: 깊이 $d+1$ 에 뿌리를 둔 leaf $q$ 개의 부분 tree에서 $\sum_\beta(n_\beta m_{d_\beta+1}-m_{d_\beta})=q-m_{d+1}$ (뿌리 자신의 $m_{d+1}$ 이 빠지지 않는다). 따라서 $q+\sum_\beta(m_{d_\beta}-n_\beta m_{d_\beta+1})=m_{d+1}$. 말단 자식($d+1=L$, $q=1$, 내부 vertex 없음)에서 양변 1. 확인.
3. `tree:insertion.s1`: $P_d=e^{-m_d(X_d-X_{d-1})}K_d$ 를 넣으면 $e^{m_dX^A_{d-1}}=e^{m_dX_{d-1}}K_de^{m_d(X_d^A-X_d)}$. 시작점 $X_{L-1}^A-X_{L-1}=\log K_LA$. 새 kernel $e^{m_d(X_d^A-X_{d-1}^A)}P_d=(Y_d/Y_{d-1})^{m_d}K_d$. 확인.
4. `tree:insertion.s3`: $a,b$ 가 root-가측이므로 kernel 적분에서 상수이고 $a^{m_d}\le K_dY_d^{m_d}\le b^{m_d}$. 확인. `math` 칸에 든 이 한 줄이 작성자 유도라는 표시는 본문에만 있다. 문제 삼지 않는다.
5. `tree:first-variation` 한 단계: $\partial\log Y_{d-1}=m_d^{-1}K_d[m_dY_d^{m_d}\partial\log Y_d]/Y_{d-1}^{m_d}=K_d^A\partial\log Y_d$. 확인.
6. `tree:log-expansion.s1` 의 $(k-1)!$: leaf $n$ 개일 때 $\gamma_\beta=-n\,Q(\beta)$, $n=1,\ldots,k-1$ 의 곱이 $(-1)^{k-1}(k-1)!\prod Q$. 첫 도함수는 계수 1의 path 하나. 확인.
7. `x:tree-analytic-bounds` 본문: 반각 $m_d\vartheta<\pi/2$ 인 부채꼴은 볼록, $\operatorname{Re}K_dY_d^{m_d}\ge a_d^{m_d}\cos(m_d\vartheta)$, 따라서 $|Y_{d-1}|\ge a_d\cos(m_d\vartheta)^{1/m_d}$, $a_L=1-\rho$. 확인.
8. `x:tree-cancellation-example`: 부호 합 $1+m_d-2m_{d+1}+(m_{d+1}-1)=m_d-m_{d+1}$, 절댓값 합 $1+(d+2)\delta+(L-1-d)\delta=2+\delta$. 확인.
9. `tree:charging.s2`–`.s4`: old leaf 재사용은 현재 tree(쓰지 않은 old path를 모두 포함)에 새 branching을 만들지 않는다; 넓힌 family에서 걸음별 상계가 앞 선택에 무관해 곱으로 떨어진다; $|m_d-jm_{d+1}|=(j-1)m_d+j\delta\ge m_d\ge\eta$ ($j\ge2$), $|J|\ge\delta^b\eta^{\sum_v(a_v-2)}$, 지수는 $k$ 로 유계. 확인.
10. `tree:regular-shapes.s1`·`.s2`: unary 선택 확률 $\delta/n$, 금지 깊이는 경계 약 $2\eta L+2$ 개와 앞선 branching vertex($\le k-2$ 개)마다 $2\eta L+1$ 개 이하, 합쳐 $(k-1)C_k(\eta L+1)\delta$. label 순서대로 자라므로 최종 tree의 history는 하나, $\delta/n\le\delta$. 확인.
11. `tree:averaging-remark` 의 둘째 문단(작성자 정식화): $\mathbb E_{Q_k}[z;\tau,\text{regular}]\le C_kL^{-a}\sum_{\mathbf q\text{ regular}}z(\mathbf q)$ 는 (tree:assignment-probability)에서 바로 나온다. $z$ 가 $a'$ 개 좌표에만 의존하면 각 $\mathbf q'$ 의 확장이 $L^{a-a'}$ 개 이하이고 regular 배정의 사영은 regular이므로 $C_kL^{-a'}\sum_{\mathbf q'}z(\mathbf q')$ 이하. comparison.tex 144–148 "each assignment of its depths has at most $L^{a-a'}$ extensions … leaves exactly the normalization $L^{-a'}$"와 같은 논법이다. 확인.
12. $L=1$ 특수화: $Y_0=\langle A\rangle$, $K_1^A$ 는 $A$ 로 재가중한 Gibbs 측도, $\partial_t\log\langle A\rangle=\langle D\rangle/\langle A\rangle$, $Q_k$ 는 root에서만 갈라지고(확률 $(n\cdot1-0)/n=1$), 급수는 $\log(1+t\langle D\rangle)$ 의 Taylor 급수. 확인.

표시 없이 보탠 곳: 본문에 몇 군데 있다(`tree:insertion` 본문 "모든 내부 vertex에서 $\gamma_\beta<0$, root에서 $-nm_1$", `tree:reference-total` 본문의 $\kappa(S)$ 부호 $(-1)^{\sum_v(a_v-1)}$, `x:tree-sampling` 본문 "tree가 깊이마다 vertex를 다 가진다"). 모두 옳고 `math` 칸 밖이다. `math` 칸 안에 표시 없이 들어간 원문 밖 주장은 찾지 못했다.

## "작성자 읽기" 네 곳

1. **$\mathscr F_d$ = 깊이 $d$ 까지의 prefix가 생성하는 $\sigma$-field (`x:tree-path-kernels`) — 동의.** trees.tex 21–22 "$K_d$ draws the next variable given the whole prefix through depth $d-1$; $\mathscr F_d$ is the prefix sigma-field", 59·77의 $K_d(dz\mid\mathscr F_{d-1})$, 147–149에서 깊이 $d$ prefix의 함수인 $\log Y_d$ 의 도함수가 $[\,\cdot\mid\mathscr F_d]$ 로 쓰인 것이 모두 이 읽기와만 맞는다. 다른 섹션도 명시한다: decorrelation.tex 95 "let $\mathscr F_d$ be generated by the root and the sampled prefix through $d$", comparison.tex 30–31.
2. **"Additional root variables remain quenched" (`x:tree-extra-variables`) — 동의, 한 가지 보탬.** 작성자 읽기(추가 root 변수는 root의 일부로 $E_{\mathcal T}$ 의 조건에 들어가고 바깥 $\mathbb E$ 에서만 평균된다)는 trees.tex 23 "The root distribution is fixed throughout all insertions", 33–34, 그리고 쓰임새 cavity.tex 55–56 "independent new root disorder", upper.tex 40–41 "Counts, interactions, fields, and root message measures are quenched", 107–109 "At $r=0$, the message itself is a root variable shared by all replica leaves"와 맞는다. 보탤 것: 이 문장은 바로 앞 문장(깊이 $\ge1$ 의 추가 변수는 prior kernel로 path에 들어가 power mean으로 적분된다)과의 대비다. root에 놓인 추가 변수는 power mean을 거치지 않고($m_0=0$), tree의 모든 path가 공유하며, 삽입으로 분포가 바뀌지 않는다. 본문에 이 대비를 한 줄 적으면 "quenched"의 뜻이 닫힌다.
3. **이후의 미분을 Cauchy 추정으로 읽은 것 (`x:tree-analytic-bounds`) — 동의, 범위를 나눠 적기를 권함.** "and their derivatives on smaller domains"(trees.tex 173–174)는 영역을 줄여 도함수를 누르는 Cauchy 추정의 표준 표현이고, perturbations.tex 392–393 "Shrinking $\rho$ gives a uniform bound on their $u$-derivatives as well"가 그렇게 쓴다. 한편 "These bounds justify integration of analytic functions at each step and all subsequent differentiations"(171–172)는 유계 해석 피적분함수의 kernel 적분이 해석적이라는 것(적분 기호 아래 미분의 정당화)까지 포함한다. Cauchy 추정은 도함수의 크기 쪽 근거이고, 미분 가능성 쪽 근거는 해석성의 보존이다. 원문이 방법을 명시하지 않는다는 작성자 표시는 옳다.
4. **"빈 확장의 무게 1"을 $k=0$ 으로 읽은 것 (`tree:extension-expansion`) — 동의.** $k=0$ 이면 history는 빈 것 하나이고 $c_E$ 는 빈 곱 1, $\mathcal T_E=\mathcal T$ 이므로 우변은 $E_{\mathcal T}H$ 이고, 좌변은 미분 없이 $\boldsymbol t=0$ 에서 같은 값이다. 쓰임새가 이 읽기를 뒷받침한다: perturbations.tex 449 "For $k=0$ these are respectively $R_{\{a_*\}}$ and $1$", 473 "For $k=0$, the claim is the vanishing constant coefficient", 524 "Constant marks cover $k=0$". 카드 본문의 "좌변이 $E_{\mathcal T}H$ 라는 뜻"은 "우변의 유일한 항이 계수 1의 $E_{\mathcal T}H$ 라는 뜻"으로 적는 편이 문장("extension has weight")에 더 가깝다.

## kind lemma 네 장

`tree:first-variation`, `x:tree-analytic-bounds`, `x:tree-differentiation-rule`, `tree:telescoping` 모두 원문이 본문에서 주장하고 근거를 주는 명제이고, SCHEMA의 종류 가운데 `lemma` 가 가장 가깝다. §7의 선례(`decor:average-holder`, `x:decor-product-difference`, `x:decor-average-comparisons` 가 `lemma`)와도 맞는다. ID도 규약대로다: 식 라벨이 있는 둘은 라벨을, 없는 둘은 `x:tree-…` 를 썼다. 적절하다고 본다. 덧붙임: `x:tree-differentiation-rule` 은 정의(protected leaf, 180–181)와 규칙을 한 카드에 담는다. 제안된 `g:protected-leaf` 의 정의 위치가 이 카드를 가리키므로 나눌 필요는 없다. `tree:telescoping` 은 원문에 증명이 없어("telescoping gives") 작성자 증명이 본문에 있는데, 옳다(검산 1).

## 기존 문서에 대한 작성자의 네 가지 지적

- **(a) `decor:section` 의 "trees.tex 38–39, 482–483" — 작성자가 옳다.** `decor:section` 본문 28행: "유도된 subtree의 법칙이 단독 사본과 같다는 것(projectivity)은 §7이 아니라 trees.tex 38–39, 482–483에서 온다." trees.tex 482–483은 "Deleting leaves from a regular tree produces a regular tree, after discarding branching vertices that become unary"로, 표본 법칙이 아니라 regularity의 보존이다. 법칙의 사영 일관성은 38–39 "Removing some leaves … preserves the sampling law of the remaining tree"가 진술이고, 200–201 "Conditional independence of children and the projectivity of tree sampling"이 그것을 이름으로 부르는 곳이다. 제안: "trees.tex 38–39(진술), 200–201(이름으로 부름)"으로 고치고, 482–483은 같은 항목 (4)의 regularity 쪽 근거로 옮긴다. 이 오류는 검토 1(`review-1-cards.md` "§8 인터페이스" 끝 문장)에서 들어온 것이다.
- **(b) `x:decor-tree-sampling` 의 `uses: [tree:section]` — 작성자가 옳다.** 그 카드의 `math` 가 옮기는 것은 trees.tex 28–40(`source` 도 그렇게 적혀 있다)이고, 그 범위의 카드는 `x:tree-sampling` 이다. kernel과 root의 뜻까지 쓰므로 `uses: [x:tree-sampling]` 이면 `x:tree-path-kernels` 가 따라온다. 섹션 카드 전체를 가리키면 의존 검사가 늘 통과해 버린다. 본문이 200–201도 근거로 드므로 `x:tree-differentiation-rule` 을 넣을 수도 있으나, 그 줄은 사영 일관성을 불러 쓰는 곳일 뿐이라 필요하지 않다.
- **(c) `g:insertion` 에 두 가정이 빠졌는가 — 지적은 옳았고, 내가 읽은 시점에는 이미 반영되어 있다.** 읽은 시점의 뜻 칸: "반복할 분배함수의 tilted kernel $K_1,\ldots,K_{L-1}$ 과 terminal Gibbs kernel $K_L$ 을 쓰고(`trees.tex` 85–87), $A$ 가 root가 주어진 조건부로 위로 유계이고 0에서 떨어져 있다고 하자(`trees.tex` 73–74)." 원문과 맞다. 남은 것 하나: 물리 대응 칸 "$L=1$ 이면 $\log Y_0=\log(Z_A/Z)$"는 옳다.
- **(d) `g:hierarchy` 기호 칸 — 지적은 옳았고, 읽은 시점에는 이미 풀려 있다.** 읽은 시점의 기호 칸: "$K_d(dz\mid\mathscr F_{d-1})$ $(1\le d\le L)$; 분배함수에서 만들 때 $1\le d<L$ 에서는 prior kernel $P_d$ 의 tilt …, $K_L$ 은 prefix가 주어진 Gibbs kernel". trees.tex 58–64와 맞고, $d=L$ 까지 tilt 꼴로 읽힐 여지는 없다.

## 인터페이스: "밖에 내주는 것" 표의 줄 확인

표가 든 줄은 모두 열어 보았고 실제 사용과 맞는다.

- upper.tex 81, 97, 121: `tree:log-expansion` 을 `\cref` 로 부른다. 맞다. 빠진 사용은 F2.
- cavity.tex 55–57, 105–110, 117–118: "The insertion recursion uses the tilted reservoir kernels and independent new root disorder", "The insertion identity for the power means then proves", "all spin trees are sampled from this reservoir using its tilted auxiliary kernels and its terminal Gibbs kernel". 맞다. $|\log Y_{0,\rm s}|\le H+BK_{\rm s}$ 가 단조성에서 나온다는 작성자 읽기도 맞다($e^{-(H+BK_{\rm s})}\le A_{\rm s}\le e^{H+BK_{\rm s}}$ 이고 $K_{\rm s}$ 는 새 root disorder라 root-가측이다).
- perturbations.tex 334–338, 370, 391, 433: 맞다.
- decorrelation.tex 61, 332, 348, 414: 맞다. `tree:charging` 본문의 "$\eta$ 자리에 $\eta/2$"도 338–339 "at least $\eta/2$ for all sufficiently large $L$"와 맞는다.
- comparison.tex 123, 141–148, 175, 205–211: 맞다.
- overview.tex 24: `\cref{tree:section,pert:tree-identity}`. 맞다.
- `tree:section` 의 "§7 카드와의 대조" 문단 가운데 `decor:overlap-concentration.s2.s1` 의 $C(S,e)=(m_{e-1}-m_e)\kappa(S)$ 는 내가 원문 줄까지 따라가 확인하지 않았다. 나머지($c_d=2m_{d+1}-m_d$, $J=\kappa(S^+)^2$, $q=2k$, $2b$ 개 vertex)는 decorrelation.tex 268–275, 292–300, 332–348에서 확인했다.

## 검토하지 않은 것

- 39장 가운데 읽지 않은 카드는 없다.
- `layers/L0.md`, `L1.md`, `rules.md` 는 읽지 않았다. 용어집은 §3 카드가 건 항목과 (c), (d)의 두 항목만 대조했다.
- `provides` 문구는 줄 번호가 실제 사용과 맞는지만 보았고, §7 카드 ID(`decor:conditional-concentration.s3.s2` 등)가 그 내용을 담는지는 카드가 실재하는지까지만 확인했다.
- `tools/check.py` 를 돌리지 않았다(쓰기 범위 밖의 `build/` 파일을 덮어쓰므로).
- 원 논문 증명 자체의 옳음은 카드와 대조하는 범위에서만 따라갔다.

## 확정 전에 사용자가 직접 봐야 할 것

1. F1: root에 "매개변수"가 든다는 두 문장. `g:root`, `x:decor-tree-sampling` 과 정면으로 어긋난다.
2. F2: §4·§5·§6이 `\ref` 없이 쓰는 단조·동차·추가 변수 약속을 인터페이스 표에 올릴지. reduction.tex 34–35를 §3에 귀속할지 §2에 귀속할지.
3. F3–F5: 같은 파일 안 참조라 기계 검사가 잡지 못한 `uses` 세 군데.
4. (a), (b): §7 카드 두 장의 수정(이 검토의 쓰기 범위 밖이라 고치지 않았다).
5. F10: 새 용어 둘을 용어집에 넣는 일과 `g:extension-history` 와의 중복 정리.
