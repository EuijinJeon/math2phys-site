# 용어집 독립 검토 (review-2)

대상: `layers/glossary.md` 62항목(8묶음). 기준: `source/main.tex`, `source/sections/*.tex` 전부(11개 파일을 끝까지 읽었다). 보조로 `SCHEMA.md`, `HANDOFF.md`, `layers/L0.md`, `L1.md`, `rules.md`, `build/glossary-response.md`, `cards/` 의 제목·source·physics·gap 칸을 보았다. 줄 번호는 모두 각 `.tex` 파일 안의 번호다.

기계적으로 확인한 것: 항목 수 62, 묶음 8. 용어집이 백틱으로 인용한 노드 ID 90개는 모두 원문 `\label` 이거나 카드 ID다. 인용한 `.tex` 행 범위는 모두 파일 안에 있다. 다른 문서가 쓰는 `g:` slug 가운데 항목이 없는 것은 없고, 쓰이지 않는 항목도 없다. 행 범위는 인용된 곳을 직접 열어 내용이 맞는지 보았다(아래 지적에 적은 것 말고는 맞았다).

## 요약

- 항목 62개 가운데 지적이 붙은 항목 22개, 통과 40개.
- 지적 21건(한 건이 두 항목에 걸친 것이 2건 있다).

| 유형 | 건수 | 번호 |
|---|---|---|
| 틀림 | 1 | 2 |
| 과장 | 4 | 1, 3, 11, 12 |
| 가정 누락 | 3 | 6, 14, 15 |
| 정의 위치(인용 노드) 오류 | 1 | 9 |
| 규율 위반·항목 사이 모순 | 1 | 10 |
| 누락 | 5 | 17, 18, 19, 20, 21 |
| 기타(부정확한 서술) | 6 | 4, 5, 7, 8, 13, 16 |

| 심각도 | 건수 | 번호 |
|---|---|---|
| 높음 | 0 | |
| 중간 | 4 | 1, 2, 11, 17 |
| 낮음 | 17 | 나머지 |

전체 평가: 뜻 칸의 정의·양화사·극한 순서는 원문과 잘 맞는다. 수식이 원문과 다른 곳은 찾지 못했다. "상태"가 `g:state` 이외의 뜻으로 쓰인 곳도 용어집 안에는 없다. 문제는 주로 (a) `g:tree-identity` 역할 칸의 범위가 원문 문장(§7 한정)보다 넓은 것, (b) tree 계수의 부호에 대한 한 줄, (c) 여러 항목이 정의 없이 쓰는 기본 어휘(root, 기대값 표기, split 깊이)다.

## 지적 목록

### 1. `g:tree-identity` — 과장 — 중간

- 용어집: "§7 이후가 모형에서 받는 유일한 입력이다", "L1 수 5–6은 bounded·순열 불변 상호작용에 대해 이 항등식 하나에서 모형의 구체적 꼴과 무관하게 따라 나온다."
- 원문: `decorrelation.tex` 8–9 "The argument uses only these identities and the tree sampling rules; in particular, it does not use the interaction factorization." 이 문장은 §7("this section")에 대한 것이다. §8은 항등식(을 거친 집중) 말고도 모형 쪽 입력을 따로 받는다: 증분 항등식 `cavity:identity`(`comparison.tex` 195–196 "By \eqref{cavity:identity}, it remains to compare…", 221–222), 낮은 증분 `comp:low-increments`(13–15, 235–236), 유계성 $C=H+BM$ 과 $\lvert\log\rvert\le H+BK$(200, 215–217).
- 판단: 같은 칸이 "균일 site 표본, encoding, log 전개"를 더한다고 적어 두었지만 `cavity:identity`(P4)와 `pert:selection`(i)(P5)가 빠졌고, 첫 문장과 끝 문장("유일한 입력", "항등식 하나에서")은 그 목록과도 어긋난다. L1 수 4의 문장("수 5의 입력의 전부")은 원문과 맞다.
- 제안: "§7이 모형에서 받는 유일한 입력이다(`decorrelation.tex` 8–9)"로 범위를 §7로 줄인다. 수 6에 대해서는 "§8은 §7의 집중에 P4(`cavity:identity`), P5(i)(`comp:low-increments`), P10(encoding), 균일 site 표본, log 전개를 더하며, 그 어느 것도 factorization이나 positivity를 쓰지 않는다"로 쓴다. "이 항등식 하나에서"는 지운다.

### 2. `g:tree-coefficient` — 틀림 — 중간

- 용어집(쓰지 않는 뜻): "부호가 일정하지 않다. 부호 있는 합의 상쇄가 [[g:depth-delay]]의 대상이다."
- 원문: 이 항목의 대상 $\gamma_\beta$ 와 $\kappa(S)$ 는 부호가 정해져 있다. `trees.tex` 204–209: $\sum_\beta(n_\beta m_{d_\beta+1}-m_{d_\beta})=n$, "All summands are positive." 곧 $\gamma_\beta<0$ 이 항상 성립한다. 245–246: "At order $k$, all $k-1$ fresh coefficients are negative." $\kappa(S)$ 의 인자 $m_{d_v}-jm_{d_v+1}$ 도 모두 음수이므로 $\kappa(S)$ 의 부호는 topology만으로 $(-1)^{\sum_v(a_v-1)}$ 로 정해진다. 부호가 섞이는 것은 extension history의 계수 $c_E$ 다: old leaf 선택은 계수 $1$(264–265), fresh path는 음수 계수라서 합이 상쇄된다(317–329: 부호 있는 합 $-\delta$, 절댓값 합 $2+\delta$).
- 제안: "$\gamma_\beta$ 는 항상 음수다(`trees.tex` 204–209). 부호가 섞이는 것은 [[g:extension-history]]의 $c_E$ 다(old leaf 계수 $+1$ 과 fresh path의 음수 계수). 그 합의 상쇄가 [[g:depth-delay]]의 대상이다." `g:extension-history` 에도 같은 한 줄을 두면 좋다.

### 3. `g:tree-identity` — 과장 — 낮음

- 용어집(쓰지 않는 뜻): "고정 깊이 집중도 나오지 않는다(깊이 평균만, `decorrelation.tex` 82–83)."
- 원문: 81–83 "We then use a marker anchor to concentrate the remaining conditional mean at each fixed depth. Averaging over depths is essential when combining the two estimates." 인용한 줄은 오히려 고정 깊이 결과를 말한다. 항등식에서 고정 깊이로 나오는 것이 셋 있다: singleton의 $\operatorname{Var}(R_S)\to0$(72–74, 533–535), singleton의 $v_N(S,d)\le\delta/\eta+o_N(1)$ "at each fixed $L,d$"(287–289), $\operatorname{Var}(M)\to0$ "at each fixed $L,S,e$"(563–566). 또 원문은 $\lvert S\rvert\ge2$ 의 고정 깊이 집중이 "나오지 않는다"고 하지 않고, 얻지 않을 뿐이다(`overview.tex` 46 "No uniform concentration in the depth is needed").
- 이 문장은 `g:clustering`, `g:overlap-concentration` 의 singleton 서술과도 겉보기에 어긋난다.
- 제안: "$\lvert S\rvert\ge2$ 의 multioverlap에 대해 논문은 고정 깊이 배정마다의 집중을 얻지 않는다(깊이 평균만). singleton과 prefix 평균 $M$ 은 고정 깊이에서 집중한다(`decorrelation.tex` 72–74, 563–566)."

### 4. `g:eta-regular` — 기타 — 낮음

- 용어집(역할): "경계 근처와 서로 가까운 깊이를 빼서 $\lvert m_d-jm_{d+1}\rvert\ge\eta$ $(j\ge2)$ 를 보장한다(`trees.tex` 449–455)."
- 원문: 그 하한은 $m_{d_v}\ge\eta$ 하나에서 나온다(`trees.tex` 410 "If $m_{d_v}\ge\eta>0$ at all of them", 449–453). 서로 떨어져 있다는 조건은 다른 일을 한다: 한 칸 미룬 깊이가 old tree의 어떤 branching 깊이와도 겹치지 않게 해서 fresh unary split을 강제하고(`decorrelation.tex` 345–347), 중간 모양들의 조상 관계와 $\eta/2$-regular를 유지한다(201–203, 46–47).
- 제안: 두 역할을 나눠 적는다.

### 5. `g:state` — 기타 — 낮음

- 용어집(뜻): "같은 상태를 공유하는 replica들은 깊이 $d$ 까지 같은 vertex를 지나고 그 아래로는 조건부 독립으로 뽑힌다."
- 원문: `trees.tex` 32–35 "At each vertex, different children are drawn independently… A split at depth $d$ means that the last common vertex is at depth $d$." 깊이 $d$ prefix를 공유하는 replica는 더 깊은 vertex도 공유할 수 있고, 그러면 $\mathscr F_d$ 가 주어져도 독립이 아니다. 조건부 독립은 깊이 $d$ 에서 서로 다른 자식으로 갈라지는 replica에 대한 것이다.
- 제안: "…깊이 $d$ 까지 같은 vertex를 지난다. 그 가운데 정확히 깊이 $d$ 에서 갈라지는(서로 다른 자식으로 들어가는) replica들은 $\mathscr F_d$ 가 주어지면 조건부 독립이다."

### 6. `g:power-mean` — 가정 누락 — 낮음

- 용어집(역할): "곱셈적 상·하한을 보존해서 $\mathcal B_r$ 이 moment 조건 없이 유한하다(`model:trial-bounds`)."
- 원문: `model.tex` 122–123 "finite without any moment assumption on the trial messages." 물리 disorder의 1차 moment(`model:integrability`)는 여전히 필요하다(상계가 $\lvert h\rvert+\sum_jB(\theta_j)$ 다).
- 제안: "시행 message에 대한 moment 조건 없이".

### 7. `g:root-logarithm` — 기타 — 낮음

- 용어집: 표제 "root logarithm $P_N^{L,\mathbf u}$", 뜻 "…recursion을 적용한 뒤 root logarithm의 기대값이다", 물리 대응 "$L=1$ 이면 보통의 $\mathbb E\log Z$".
- 원문: `cavity.tex` 34–35 "Write $P_N^{L,\mathbf u}$ for its expected root logarithm." `perturbations.tex` 121 "the random root log partition function" $X_0$, 251 "root-averaged perturbed log partition function". 곧 root logarithm은 recursion의 깊이 0 값 $X_0$(root에 대해 무작위)이고 $P$ 는 그 기대값이다. 용어집은 표제어를 $P$ 와 같게 놓고 뜻 칸에서 표제어로 자기를 정의한다. 또 `cavity.tex` 16 "Fix $L\ge2$" 이므로 $L=1$ 은 원문 범위 밖이고, $L=1$ 로 읽어도 섭동 factor가 든 계의 $\mathbb E\log Z$ 이지 "보통의" 것이 아니다.
- 제안: "root logarithm은 leaf 분배함수에 power-mean recursion을 적용해 얻은 깊이 0의 값 $X_0$(`trees.tex` 51–56)이고, $P_N^{L,\mathbf u}=\mathbb EX_0$ 다." 물리 대응의 $L=1$ 문장은 "섭동된 계의 $\mathbb E\log Z$"로 고치거나 뺀다.

### 8. `g:interpolation` — 기타 — 낮음

- 용어집(뜻): "$\varphi(t)$ 는 power-mean recursion 뒤의 root logarithm을 $N$ 으로 나눈 것이다."
- 원문: `upper.tex` 42–43 "denote its expected root logarithm divided by $N$ by $\varphi(t)$."
- 제안: "root logarithm의 기대값을".

### 9. `g:anchor` — 정의 위치(인용 노드) 오류 — 낮음

- 용어집(역할): "spin anchor는 singleton 집중과 상태 안 귀납(P8, `decor:overlap-concentration.s1`)에…"
- 원문·카드: singleton 집중은 `decor:overlap-concentration` 증명의 첫 문단(`decorrelation.tex` 533–535, 카드 `.s1`)이고 P9 쪽이다. 상태 안 귀납은 `decor:conditional-concentration` 증명이다(265 "with path 1 a spin anchor", 296–297 "Fix an old leaf in I as the spin anchor").
- 제안: "spin anchor는 singleton 집중(P9, `decor:overlap-concentration.s1`)과 상태 안 귀납(P8, `decor:conditional-concentration`)에".

### 10. `g:physical-pure-state`, `g:three-copy` — 규율 위반·항목 사이 모순 — 낮음

- 용어집: `g:clustering` 뜻 "이 사이트의 'clustering'은 `decor:conditional-concentration`의 결론 하나만 가리킨다." 그런데 `g:physical-pure-state` 뜻 "극단적(clustering) 성분", `g:three-copy` 물리 대응 "'overlap이 요동하지 않으면 clustering'의 정량적 한 방향 판"은 같은 낱말을 물리의 일반 뜻으로 쓴다.
- 원문: "clustering"이라는 낱말은 원문에 없다(전 파일 확인). 따라서 원문 위반은 아니고 용어집 내부의 일관성 문제다.
- 제안: 두 곳을 "connected correlation이 사라지는 성분", "overlap이 요동하지 않으면 조건부 공분산이 작다"처럼 풀어 쓰거나, 아래 판단 5에 따라 표제어를 바꾼다.

### 11. `g:encoded-law`, `g:rsb-steps` — 과장(유형 표시) — 중간, 확신 낮음

- 용어집: `g:encoded-law` 물리 대응 "exact — 무작위 site의 계층별 cavity field 분포를 order parameter로 쓴 것." `g:rsb-steps` 물리 대응 "exact — 깊이 $L$ 의 계층은 $(L-1)$단 RSB다."
- 원문: 부호화 자체는 정확하다(`comparison.tex` 19–25, 75–79). 그러나 여기서 "계층"은 섭동 mark로 만든 보조 계층이다(`cavity.tex` 23–24). 그것을 물리의 RSB 계층에 따른 cavity field 분포로 읽는 것은 `introduction.tex` 75–77("Their branching is part of the construction; no ultrametric organization of the physical Gibbs states is assumed")에 비추어 논문이 증명하지 않는 동일시다. 같은 용어집의 `g:state`, `g:depth`, `g:hierarchy` 는 바로 이 읽기를 intuition으로 둔다.
- 판단: 시행 법칙 쪽($r$단 사슬 = $r$단 RSB 시행 order parameter, `model.tex` 70–81; "In an $r$-level application, $L=r+1$", `trees.tex` 24–25)은 exact가 맞다. reservoir의 보조 계층을 물리의 RSB 단계로 읽는 부분만 문제다. 유형 칸의 뜻(SCHEMA: physics 문장이 math에 대해 갖는 관계)을 어떻게 읽느냐에 따라 달라질 수 있어 확신은 낮다.
- 제안: `g:encoded-law` 를 "exact(부호화: 한 label이 $\mathbb ER_S$ 를 보존한다) / intuition(이것을 계의 RSB order parameter로 읽는 것; 깊이는 보조 계층의 것이다)"로 나눈다. `g:rsb-steps` 는 "exact(시행 법칙에서) — reservoir의 깊이 $L$ 보조 계층에 대해서는 [[g:depth]] 참조"로 한다.

### 12. `g:hypergraph` — 과장(원문 문장이 아닌 것을 단정) — 낮음

- 용어집(쓰지 않는 뜻): "증명은 이 그래프의 국소 tree 구조를 쓰지 않는다(P11 차이)."
- 원문: 이 문장은 원문에 없다. `rules.md` P11 차이 칸은 "논문이 이를 문장으로 말하지는 않는다"고 스스로 적는다. 내가 §5–§8을 읽은 바로도 국소 구조를 쓰는 단계는 없으므로 내용은 맞다고 본다.
- 제안: "(논문의 문장이 아니라 증명에 쓰이지 않는다는 데서 읽은 것)"을 덧붙인다.

### 13. `g:hierarchy` — 기타 — 낮음, 확신 낮음

- 용어집(쓰지 않는 뜻): "물리적 Gibbs 측도의 분해가 아니다. 계층의 branching은 구성의 일부이고 유도된 것이 아니다(`introduction.tex` 75–77)."
- 원문: 75–77은 둘째 문장만 뒷받침한다. 첫 문장을 말하는 원문 문장은 찾지 못했다. $m_d<1$ 의 tilt 때문에 path 하나의 spin 주변분포가 일반적으로 Gibbs 측도가 아니라는 점에서 수학적으로는 맞을 것이나, 원문에서 확인한 것은 아니다.
- 제안: 첫 문장에 "원문의 문장은 아니다"를 표시하거나, 원문 표현("no ultrametric organization of the physical Gibbs states is assumed")으로 바꾼다.

### 14. `g:named-models` — 가정 누락 — 낮음

- 용어집: "`models:spin`은 대칭 $J$, $\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert<\infty$ …"
- 원문: `consequences.tex` 12–13 "independent real random variables $J,H$ such that $J$ has a symmetric distribution". $J$ 와 $H$ 의 독립이 빠졌다. 두 따름정리 모두 "For every $\beta>0$"(14, 40–41)이다.
- 제안: "서로 독립인 $J$, $H$" 를 넣는다.

### 15. `g:depth-continuity` — 가정 누락 — 낮음

- 용어집: "갈라짐 깊이나 평가 깊이를 한 칸 옮기는 비용은 깊이 평균으로 $C/L$ 이다."
- 원문: `decorrelation.tex` 148 "for all sufficiently large $L$", 163–165 "The constant depends only on the number of vertices and shifts, uniformly in $N$, the evaluation depth, and the transition kernels." 평가 깊이 쪽은 $d$ 가 initial unary stretch 위를 움직일 때의 진술이다(155–162).
- 제안: "충분히 큰 $L$ 에서", "$C$ 는 vertex 수와 이동 수에만 의존"을 넣는다.

### 16. `g:mark` — 기타 — 낮음

- 용어집: 기호 칸에 "$g$, $g_0$"를 mark와 나란히 두고, 뜻 칸에서 "두 color $a,b$ 의 factor에 같은 좌표를 넣으면 mark 기대값이 '$a,b$ 가 깊이 $d$ vertex를 공유'의 지시함수가 되어(selector), 원하는 split 깊이 제약 $\mathcal C$ 를 고른다."
- 원문: `perturbations.tex` 28–32. mark specification은 (Rademacher 좌표들, 각 좌표의 깊이, 좌표의 함수 $g,g_0:\{-1,1\}^n\to\mathbb Q\cap[-1,1]$, $S_0\in\{1,\sigma_i\}$)의 묶음이다. $g,g_0$ 는 좌표가 아니라 좌표의 함수다. 지시함수는 "split 깊이 $\ge d$"(496–498)이고, 정확히 깊이 $d$ 의 split은 $H_d-H_{d+1}$ 과 그 유한 일차결합으로 고른다(514–520).
- 제안: "$g$, $g_0$ 는 좌표의 유리수값 함수", "공유 지시함수 $H_d$ 의 차 $H_d-H_{d+1}$ 과 곱·일차결합으로 정확한 split 깊이 제약 $\mathcal C$ 를 고른다"로 보탠다. `g:reservoir` 의 "평균 $c_\nu s_N$ 개의 섭동 factor"도 "type $\nu$ 마다 평균 $c_\nu s_N$ 개(합계 Poisson$(s_N)$)"로 쓰면 원문(`cavity.tex` 20–23, 28)과 같아진다.

### 17. 누락: root 와 기대값 표기 ($\mathbb E$, $E_{\mathcal T}$, $\langle\cdot\rangle$, $\mathbb E_{\mathbf u}$) — 누락 — 중간

- 쓰임: 용어집 안에서 "root"가 15번 나오고(`g:state`, `g:self-average`, `g:overlap-concentration`, `g:root-logarithm` 등), `rules.md` 4번, 카드 7장의 physics·gap에 나온다. 항목은 없다. `g:depth` 가 "0은 root"라고만 한다. `g:prescribed-tree` 는 기호 칸에 $E_{\mathcal T}$ 를 올리고 뜻을 적지 않았다.
- 원문: `trees.tex` 20 "Its depth-zero variable is the root", 23 "The root distribution is fixed throughout all insertions", 33–34 "$E_{\mathcal T}$ for this sampling expectation conditional on the root", 48–49 "An unspecified expectation $\mathbb E$ below includes the root and the sampling of the indicated tree." `cavity.tex` 29 "Counts, types, and sites are root variables." `perturbations.tex` 83–85 "$\langle\cdot\rangle$ denote expectation along one tilted path conditional on the root, and let $\mathbb E_{\mathbf u}$ average the root at fixed $\mathbf u$."
- 왜 중요한가: "분산은 root와 tree 표본추출 전부에 대한 것"(`g:overlap-concentration`), "$\mathbb E_{\mathbf u}\langle\cdot\rangle$"(`g:score`) 같은 정량 진술의 뜻이 이 약속에 달려 있고, 물리 독자에게 root는 quenched disorder에 해당하는 말이다.
- 제안: `g:root` 항목을 만든다(깊이 0 변수: 물리 disorder, 섭동 개수·type·site; 삽입 내내 고정; 물리 대응은 quenched 변수). 네 기대값 표기를 거기에 모은다.

### 18. 누락: split 깊이 — 누락 — 낮음

- 쓰임: 용어집 8번(`g:replica`, `g:mark`, `g:tree-identity`, `g:grid`, `g:depth` 등), `rules.md` 3번. 정의하는 항목이 없다.
- 원문: `trees.tex` 34–35 "A split at depth $d$ means that the last common vertex is at depth $d$."
- 제안: `g:replica` 나 `g:topology` 의 뜻 칸에 한 문장으로 넣는다.

### 19. 누락: Palm 항등식과 Taylor 계수 소거 (`pert:palm`, `pert:analytic`) — 누락 — 낮음

- 쓰임: `g:score` 역할과 `g:selected-sequence` 역할이 "Palm 부등식"을 쓰고, `g:perturbation` 이 "같은 factor의 $t$ 전개가 Taylor 계수 항등식을 낸다"고 한다. 항목은 없다. score 집중(ii)에서 항등식(P7)으로 넘어가는 유일한 다리다.
- 원문: `perturbations.tex` 350–360 "Lemma (Palm identity)… $\lvert H_N(t_\nu,u_\nu)\rvert\le\lVert f\rVert_\infty e_{\nu,N}$", 383–388 "every Taylor coefficient at $t=0$ of $H_N(t,0)$ tends to zero along the selected sequence", 40–43 "Taking $u$ smaller than every fixed power of $t$ will force each limiting Taylor coefficient to vanish."
- 이름: 원문의 lemma 이름은 "Palm identity"다. 내용은 부등식이므로 "Palm 부등식"이 틀린 것은 아니지만 원문 이름과 다르다.
- 제안: `g:score` 나 `g:perturbation` 에 두 문장으로 넣거나 항목 하나를 만든다. 이름은 "Palm 항등식(`pert:palm`)의 부등식"처럼 원문 이름을 살린다.

### 20. 누락: canceled-anchor 전개의 어휘 — 누락 — 낮음

- 쓰임: "old tree"(용어집 3번, 카드 15장), "initial stem"(`g:topology` 기호, `g:conditional-covariance` 뜻), "fresh path", "unary vertex", "reference path", "target", "color". `g:extension-history` 가 color와 anchor는 설명하지만 old tree, fresh path, reference path는 정의하지 않는다. `g:clustering` 역할의 $V_{k-1,L}(\eta/2)$ 도 정의 없이 나온다(`decor:V-definition`, `decorrelation.tex` 253–257).
- 원문: `trees.tex` 259–276(old paths, fresh path, color), 311–315("the anchor and the already colored paths are called reference paths").
- 범위: 카드의 physics·gap 칸에서는 이 낱말들이 쓰이지 않았다(스크립트로 확인). 그래서 용어 규율 1의 위반은 아니고, 용어집 자체가 정의 없이 쓰는 문제다.
- 제안: `g:extension-history` 뜻 칸에 old tree, fresh path, reference path를 한 줄씩 넣는다.

### 21. 누락: $P_{\mathcal T}$, $B_{\mathcal T}$ — 누락 — 낮음

- 쓰임: `g:factorization` 역할 "나머지항을 $P^p-pPB^{p-1}+(p-1)B^p$ 꼴로 나누고". $P$, $B$ 가 용어집 어디에도 정의되어 있지 않다(`rules.md` P2는 그 자리에서 풀어 쓴다).
- 원문: `upper.tex` 98–107. $P_{\mathcal T}=\frac1N\sum_i\mathbb E_f\prod_af(\sigma_i^a)$, $B_{\mathcal T}=\mathbb E_{f,x}\prod_a\bar f(x^a)$.
- 제안: `g:interpolation` 이나 `g:factorization` 에 한 줄로 정의한다.

## 통과한 항목

`g:interaction`, `g:field`, `g:pressure`, `g:hypotheses`, `g:positivity`, `g:permutation-invariance`, `g:ground-state`, `g:lower-pressure`, `g:message`, `g:site-term`, `g:edge-term`, `g:order-parameter`, `g:parisi-parameters`, `g:functional`, `g:phi`, `g:depth`, `g:replica`, `g:topology`, `g:grid`, `g:perturbation`, `g:increment`, `g:site-bond-insertion`, `g:insertion`, `g:tree-law`, `g:extension-history`, `g:depth-delay`, `g:multioverlap`, `g:spin-product`, `g:conditional-covariance`, `g:clustering`, `g:depth-average`, `g:self-average`, `g:overlap-concentration`, `g:projection`, `g:order-of-limits`, `g:spin-pattern`, `g:independent-copies`, `g:constant-shift`, `g:truncation`, `g:stability`

통과 항목에 대한 메모(지적은 아니다):
- `g:clustering` 의 singleton 인용 "`decorrelation.tex` 286–290"은 정확히는 287–290이다(286은 `\end{equation}`).
- `g:extension-history`, `g:topology`, `g:reservoir` 는 지적 2, 18, 20, 16의 제안에서 문장을 보탤 자리로 언급했을 뿐, 지금 적힌 내용은 원문과 맞다(`g:reservoir` 만 지적 16에 표현 수정 하나가 있어 통과 목록에서 뺐다).
- 물리 대응 칸의 Ruelle cascade(`g:power-mean`, `g:tree-law`), Ghirlanda–Guerra·stochastic stability(`g:tree-identity`), ultrametric(`g:physical-pure-state`)은 모두 intuition으로 표시되어 있고 "증명되지 않는다 / 쓰이지 않는다"가 붙어 있다. 원문 인용(`trees.tex` 7–12, `perturbations.tex` 17–21, `introduction.tex` 77)도 맞다. 이 이름들이 뜻·역할 칸에 나오는 곳은 없다.
- `g:selected-sequence` 의 "예전 판의 'generic 상태'가 이것이다"는 낱말을 언급한 것이지 사용한 것이 아니라서 규율 위반으로 보지 않았다.

## "판단이 필요한 것" 10건에 대한 의견

1. **"선택된 수열"**: 원문에 충실하다. 원문 표현은 "a sequence from Lemma pert:selection"(`perturbations.tex` 308–309), "the selected sequence"(387), "one selected sequence"(540–541), "the selected fixed-$L$ sequence"(`comparison.tex` 130)다. "선택된 섭동계"는 원문에 없는 말이다("the selected deterministic vector", "selected parameter vector"만 있다). 쓰더라도 지금처럼 같은 항목 안의 파생어로 두는 것이 맞다. 카드의 "선택된 perturbed 수열"은 "선택된 수열"로 통일하는 편이 낫다.

2. **항등식 이름**: 원문은 정리 제목 "Identity on prescribed trees"(`perturbations.tex` 451)와 "prescribed-tree identities"(`trees.tex` 309, `perturbations.tex` 544, `decorrelation.tex` 615)를 쓴다. "prescribed-tree 항등식"이 원문 그대로이고, 용어집이 "prescribed tree"를 번역하지 않으므로 이쪽으로 통일하는 것이 일관된다. "처방된"은 카드에만 있고 용어집에는 한 번도 나오지 않는다.

3. **rules.md의 `상태` 열**: 지금의 `SCHEMA.md`(규칙 표 절)와 `rules.md` 는 이미 열 이름이 `승인`이다. 이 건은 해결된 것으로 보인다. 응답 문서의 서술이 낡았다.

4. **규칙 표 안의 링크 꼴**: 원문과 무관한 표시 문제라 원문 근거로는 의견이 없다. 다만 "clustering([[g:clustering]])" 꼴은 판단 5에서 표제어를 바꾸면 중복 표시 문제가 함께 줄어든다.

5. **"clustering"**: 원문에 이 낱말은 없다. 원문은 절 제목 "Decorrelation on prescribed trees", 소절 제목 "Conditional decorrelation"(`decorrelation.tex` 232), "Conditional covariance then decays by induction"(`overview.tex` 31–32)을 쓴다. 원문에 더 충실한 것은 "조건부 decorrelation"이다. 지적 10처럼 용어집 안에서도 "clustering"이 물리의 일반 뜻으로 두 번 새어 나왔으므로, 표제어를 "조건부 decorrelation"으로 하고 "clustering"은 물리 대응 칸에만 두기를 권한다.

6. **"connected correlation"**: 원문은 "squared conditional covariance of the spin-product vector"(`decorrelation.tex` 78–79)라고만 한다. 지금 `g:conditional-covariance` 의 처리(표제어는 조건부 공분산, 물리 이름은 물리 대응 칸에서 singleton에 한정)는 원문에 충실하다. 남는 문제는 규칙 P8의 문장이 "spin 곱들의 connected correlation"을 주어로 쓰는 것인데, 거기서도 "조건부 공분산"을 주어로 하는 편이 원문에 가깝다.

7. **`g:self-average`**: 원문은 score와 multioverlap 모두에 "concentration"을 쓴다("Concentration of each perturbation score", "Concentrate all multioverlaps"). "self-averaging"은 Ghirlanda–Guerra의 antecedent를 말할 때 한 번만 나온다(`perturbations.tex` 18). 그래서 이 낱말을 규칙 문장에 쓰면 원문이 antecedent로만 든 논법의 이름을 끌어오는 셈이 된다. "집중"으로 쓰고 두 정량 항목(`g:score`, `g:overlap-concentration`)을 직접 가리키는 쪽이 원문에 더 충실하다. 항목을 남긴다면 표제어를 "집중"으로 하고 self-averaging은 물리 대응 칸에 둔다.

8. **고전적 GG 항등식의 한 줄 요약**: 원문에 없는 내용이다. 원문은 이름과 인용만 든다(`perturbations.tex` 17–21). 요약 문장 자체도 느슨하다("확률 $1/n$ 으로 기존 replica를 복사"는 항등식의 한쪽 항만 말한다). 이 항목이 하려는 말("같은 꼴이 아니다")은 요약 없이도 성립하므로 지우기를 권한다. 남긴다면 "원문에 없는 대조용 서술"이라고 표시한다.

9. **물리 대응 유형**: $x(q)$ 읽기, cascade 읽기, pure state 묶음 읽기를 intuition으로 둔 것은 원문과 맞다(`trees.tex` 7–12, `introduction.tex` 75–77). $\Phi_r$, $\Delta_N$, multioverlap 집중, 독립 사본 대체의 approximation도 적절하다. 다르게 보는 곳은 지적 11의 두 항목이다(`g:encoded-law`, `g:rsb-steps` 의 exact는 시행 법칙·부호화에 한정하고, reservoir의 보조 계층을 RSB 계층으로 읽는 부분은 intuition).

10. **깨끗하게 정의하지 못한 것**:
    - "branching pattern": 원문은 비공식으로만 쓴다(`introduction.tex` 79, `overview.tex` 20–24, `perturbations.tex` 38, `comparison.tex` 58). (topology, 깊이 배정)으로 정한 것은 이 쓰임들과 어긋나지 않는다. 원문이 이 짝에 붙이는 말은 "shape"다(`trees.tex` 460–462 "describing a shape by a finite topology and its branching-depth coordinates"). 항목에 "원문의 shape에 해당"이라고 적어 두기를 권한다.
    - "평균장": 원문에 없다. 지금처럼 물리 대응 칸에만 두면 된다.
    - "limiting infinite-depth Gibbs state" → "극한 무한 깊이 Gibbs 측도": 이 사이트의 "상태"와 구별하려는 번역으로 타당하다. 다만 `g:physical-pure-state` 역할의 "만들지 않는다고 쓴다"는 원문("The theorem does not assume that … a limiting infinite-depth Gibbs state has been constructed", `model.tex` 138–140)보다 조금 강하다. "만들어져 있다고 가정하지 않는다"가 원문 그대로다. 또 원문 `introduction.tex` 77의 "physical Gibbs states"를 "물리적 pure state"로 옮긴 것은 해석이 들어간 번역이므로, 지금처럼 원문 표현을 함께 인용해 두는 것을 유지해야 한다.

## 확인하지 못한 것

- `g:tree-identity` 물리 대응 칸의 고전적 Ghirlanda–Guerra 항등식 서술과 `g:hierarchy` 의 Monasson 재가중, `g:tree-law` 의 nested Chinese restaurant 읽기는 원문에 없는 물리 쪽 내용이라 원문으로 검증할 수 없었다. intuition으로 표시되어 있다는 것만 확인했다.
- `g:depth-continuity` 물리 대응의 "실제로 쓰는 단조량은 깊이별 자기 overlap $\mathbb E\lVert\mu_{t,T}\rVert_N^2$"는 원문 문장이 아니다. martingale 증분의 직교성(`decorrelation.tex` 170–175)에서 따라 나오는 사실이라 지적하지 않았다.
- 카드 54장의 본문은 제목·source·physics·gap 칸과 "상태" 사용만 보았다. 카드 자체의 검토는 이 검토의 범위가 아니다.
