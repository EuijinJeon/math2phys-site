# 검토 2 응답 — layers/glossary.md

기준은 `source/sections/*.tex`, `main.tex`. 지적마다 검토자가 인용한 줄을 직접 열어 읽었다. 검토자의 행 번호는 대체로 맞았다. 다른 곳은 아래 "좁힘의 근거"와 표의 근거 칸에 적었다. 수정 뒤 `python3 redesign/tools/check.py --sections decorrelation --out /tmp/check-glossary-fix.md`는 형식·정초·포함·의존·연결·순환·사전·단면 8종이 통과한다. 용어 검사에는 오류 5건이 남는데, 모두 §3 카드(`tree.*`, `x.tree-*`)가 아직 용어집에 없는 `g:protected-leaf`, `g:reference-path`를 가리키는 것이다. 이 이 작업 범위 밖이다(아래 "넘긴 것"). 이 작업이 쓴 파일에서 나온 오류는 0이다. 승인 표시는 모두 `proposed` 그대로이고, R번호는 쓰지 않았다.

| # | 판정 | 근거 | 고친 파일 |
|---|---|---|---|
| 1 `g:tree-identity` 역할 범위 | 반영 | `decorrelation.tex` 4–9("this section")는 §7에만 해당한다. §8은 `cavity:identity`(`comparison.tex` 195–196, 221–222), `comp:low-increments`(13–15, 235–236), encoding, `comp:patterns`, log 전개, 유계성 $C=H+BM$·절단(198–217)을 더 받는다. "§7 이후가 받는 유일한 입력"을 "§7이 받는 유일한 입력"으로, "이 항등식 하나에서"를 §8의 입력 목록으로 바꿨다. 무관성의 근거로는 `cavity.tex` 13–14, `overview.tex` 46–48을 달았다. | glossary.md; rules.md P7 차이, "확신이 낮은 대응" P7; L1 수 4(인용을 §7은 `decorrelation.tex` 8–9, 수 6은 `cavity.tex` 13–14로 나눔), L1 끝 문단("항등식과 tree 표본 규칙만으로") |
| 2 `g:tree-coefficient` 부호 | 반영 | `trees.tex` 204–209 "All summands are positive", 245–246 "all $k-1$ fresh coefficients are negative". 그래서 $\gamma_\beta<0$ 이다. $\kappa(S)$ 의 인자는 $j\ge1$ 에서 모두 음수다(`tree:K`, 349–352). 부호가 섞이는 것은 $c_E$ 다(264–268, 317–329). | glossary.md (`g:tree-coefficient`, `g:extension-history`) |
| 3 `g:tree-identity` "고정 깊이 집중도 나오지 않는다" | 좁혀서 반영 | 아래 좁힘의 근거 1 | glossary.md |
| 4 `g:eta-regular` 역할 | 반영 | 하한 $\lvert m_d-jm_{d+1}\rvert\ge\eta$ 는 $m_{d_v}\ge\eta$ 하나에서 나온다(`trees.tex` 410, 449–455). 간격 조건이 하는 일은 따로 있다: fresh unary split을 강제하고(`decorrelation.tex` 345–347), 중간 모양의 조상 관계와 $\eta/2$-regular를 지킨다(44–47, 201–203). 두 역할을 나눠 적었다. 기저의 $c_d\ge\eta$(288)도 아래 경계에서 나온다는 것을 보탰다. | glossary.md |
| 5 `g:state` 조건부 독립 | 반영 | `trees.tex` 32–35. 깊이 $d$ prefix를 공유하는 replica는 더 깊은 vertex도 공유할 수 있다. 조건부 독립은 깊이 $d$ vertex의 서로 다른 자식 아래 묶음들 사이에서만 성립한다. | glossary.md |
| 6 `g:power-mean` moment 조건 | 반영 | `model.tex` 122–128 "without any moment assumption on the trial messages"; 상계 $\lvert h\rvert+\sum_jB(\theta_j)$. | glossary.md |
| 7 `g:root-logarithm` | 반영 | root logarithm은 깊이 0의 값 $X_0$ 이다(`trees.tex` 51–56; `perturbations.tex` 121 "random root log partition function"). $P_N^{L,\mathbf u}$ 는 그 기대값이다(`cavity.tex` 34–35, `perturbations.tex` 251). 하한은 $L\ge2$(`cavity.tex` 16)만 쓴다. $L=1$ 문장은 "섭동된 계의 $\mathbb E\log Z$"로 고쳤다. 표제어 이름은 그대로 두고 기호만 보탰다. | glossary.md |
| 8 `g:interpolation` | 반영 | `upper.tex` 42–43 "expected root logarithm divided by $N$". | glossary.md |
| 9 `g:anchor` 인용 노드 | 반영 | singleton은 `decor:overlap-concentration` 증명 첫 문단(`decorrelation.tex` 533–535, 카드 `.s1`, P9)이다. 상태 안 귀납은 `decor:conditional-concentration`(265, 296–297, P8)이다. | glossary.md |
| 10 "clustering"이 일반 뜻으로 샘 | 반영(범위 넓힘) | "clustering"은 원문에 없다. 용어집 `g:clustering`은 이 말을 Prop 7.4의 결론에만 쓰기로 정했다. `g:physical-pure-state` 뜻과 `g:three-copy` 물리 대응 칸을 풀어 썼다. 같은 누수가 카드 두 장에도 있었다: `decor:contractions` physics·gap("overlap이 요동하지 않으면 clustering", "overlap 집중 ⇔ clustering")과 `decor:projection-bound` physics·gap("각 가지가 clustering하면(자식의 $v_N$ 이 작으면)"). 두 카드 모두 "connected correlation / $v_N$ 이 작다"로 고쳤고, Prop 7.4의 결론을 말하는 곳에서만 [[g:clustering]]을 가리키게 했다. 표제어는 바꾸지 않았다. | glossary.md; cards/decor.contractions.md, cards/decor.projection-bound.md |
| 11 `g:encoded-law`, `g:rsb-steps` exact | 반영 | 부호화와 시행 법칙 쪽은 exact가 맞다(`comparison.tex` 19–25, 75–79; `model.tex` 70–81; `trees.tex` 24–25). reservoir의 보조 계층(`cavity.tex` 20–24)을 물리의 RSB 계층으로 읽는 것은 `introduction.tex` 75–77에 비추어 intuition이다. 그래서 두 항목 모두 유형을 exact와 intuition으로 나눴다. P10 차이 칸에도 같은 한 문장을 넣었다(유형 `exact`는 유지). | glossary.md; rules.md P10 |
| 12 `g:hypergraph` 국소 구조 | 반영 | 원문에 없는 문장이다. P11 차이 칸도 스스로 그렇게 적는다. "증명에 쓰이지 않는다는 데서 읽은 것"이라고 표시했다. | glossary.md |
| 13 `g:hierarchy` 쓰지 않는 뜻 | 반영 | `introduction.tex` 75–77은 둘째 문장만 뒷받침한다. 원문 표현을 인용하고, "분해가 아니다"는 그 인용에서 읽은 것이라고 표시했다. | glossary.md |
| 14 `g:named-models` 독립 | 반영 | `consequences.tex` 12–14 "independent real random variables $J,H$", "For every $\beta>0$"(14, 40–41). L0의 정확한 진술 줄에도 같은 누락이 있었다. | glossary.md; L0.md |
| 15 `g:depth-continuity` 가정 | 반영 | `decorrelation.tex` 148 "for all sufficiently large $L$", 155–165(평가 깊이는 initial unary stretch 위, $C$ 는 vertex 수·이동 수에만 의존). | glossary.md |
| 16 `g:mark`, `g:reservoir` | 좁혀서 반영 | 아래 좁힘의 근거 2 | glossary.md |
| 17 누락: root와 기대값 표기 | 반영(새 항목) | `trees.tex` 20, 23, 33–34, 48–49; `cavity.tex` 29–31; `perturbations.tex` 9–10, 60–62, 83–85. 새 항목 `g:root`를 만들었다. 만들면서 더 찾은 것은 아래 "검토 밖에서 고친 것" 1, 2. | glossary.md(새 항목과 링크); rules.md P9; cards 7장(아래) |
| 18 누락: split 깊이 | 반영 | `trees.tex` 34–35. `g:replica` 뜻 칸에 한 문장을 넣었고 `g:depth`에서 그곳을 가리킨다. | glossary.md |
| 19 누락: Palm 항등식, Taylor 계수 소거 | 반영(새 항목) | `perturbations.tex` 40–43, 314–425, 472–535. 새 항목 `g:palm-identity`를 만들었다. 원문 lemma 이름 "Palm identity"를 살리고, 쓰이는 결론이 부등식이라고 적었다. `g:score`, `g:selected-sequence`의 "Palm 부등식"은 "Palm 항등식(`pert:palm`)의 부등식"으로 고쳤다. "유일한 다리"라고는 쓰지 않았다. | glossary.md; rules.md "규칙으로 못 옮긴 것" Taylor 항목 |
| 20 누락: canceled-anchor 어휘 | 반영 | `trees.tex` 259–261, 270–271, 311–315; `decorrelation.tex` 94, 208, 253–257. 넣은 곳: old tree·old path·old leaf·fresh path·reference path는 `g:extension-history`, unary vertex·initial stem·자식 모양은 `g:topology`, target은 `g:depth-delay`, $V_{k,L}(\eta)$ 는 `g:clustering` 역할 칸. | glossary.md |
| 21 누락: $P_{\mathcal T}$, $B_{\mathcal T}$ | 반영 | `upper.tex` 62–66, 98–112. `g:factorization` 역할 칸에서 정의했다. | glossary.md |

통과 항목 메모 가운데 맞는 것도 반영했다: `g:clustering`의 singleton 인용을 286–290에서 287–290으로 바꿨다. "판단 10"의 `g:physical-pure-state` 역할 "만들지 않는다"는 원문 그대로 "만들어져 있다고 가정하지 않는다"(`model.tex` 138–140)로 고쳤다.

## 좁힘의 근거

1. **지적 3.** 검토자의 말대로 인용한 `decorrelation.tex` 81–82는 고정 깊이의 결과("concentrate the remaining conditional mean at each fixed depth")를 말한다. 83 "Averaging over depths is essential"은 깊이 평균이 필요하다는 쪽을 뒷받침하므로 인용 전체가 틀린 것은 아니다. 고친 문장은 이렇다: $\lvert S\rvert\ge2$ 에서는 고정 깊이 집중을 *얻지 않는다*(63–75; `overview.tex` 46). 고정 깊이로 나오는 것은 singleton의 $\operatorname{Var}(R_S)\to0$(72–74, 533–535)과 $\operatorname{Var}(M)\to0$(563–566)이다. 검토자는 셋째로 singleton의 $v_N(S,d)\le\delta/\eta+o_N(1)$(287–289)도 들었지만 이것은 빼었다. 이 상계는 고정 $L$ 에서 0이 아니라 $1/(\eta L)$ 이므로 "고정 깊이 집중"이 아니다.
2. **지적 16.** 기존 문장 "mark 기대값이 'a,b가 깊이 $d$ vertex를 공유'의 지시함수"는 틀리지 않았다. 원문의 "split depth is at least $d$"(`perturbations.tex` 496–498)와 같은 사건이다. 빠진 것은 두 가지였다: 정확한 split 깊이를 $H_d-H_{d+1}$ 과 곱·일차결합으로 고른다는 단계(514–520), 그리고 $g$, $g_0$ 가 좌표가 아니라 좌표의 유리수값 함수라는 점(28–35). 이 둘을 보탰다. `g:reservoir`는 "type $\nu$ 마다 평균 $c_\nu s_N$ 개(합계 Poisson$(s_N)$)"로 썼다(`cavity.tex` 20–28).

기각한 지적은 없다.

## 검토 밖에서 고친 것 (`g:root`을 쓰다가 찾은 것)

1. **섭동 매개변수는 root 변수가 아니다.** `cavity.tex` 29–31 "The parameters … are fixed, not quenched random variables", `perturbations.tex` 9–10, 67–69. 그런데 P9 차이 칸은 "분산은 root(disorder와 선택된 섭동 매개변수)… 전부에 대한 것"이라고 써서, 매개변수에 대해서도 평균하는 것처럼 읽혔다. 고친 곳: rules.md P9, `decor:overlap-concentration` gap (5), `g:state` 뜻, `g:overlap-concentration` 뜻. `x:decor-tree-sampling`의 math 칸 "공통 root(깊이 0, disorder와 매개변수 포함)"도 원문과 어긋난다고 확인되어 고쳤다. 구조 칸을 고친 것은 이 한 곳뿐이다.
2. **$\langle\cdot\rangle$ 의 두 뜻.** §6의 괄호는 tilted path 하나를 따른 기대값이다(`perturbations.tex` 83). §8 encoding의 $\operatorname{arctanh}\langle\sigma_i\rangle$ 은 보조 prefix가 주어진 leaf Gibbs 기대값이다(`comparison.tex` 34–36). 둘을 `g:root`에 구별해 적었다.

## 새로 만든 항목

- `g:root` — root와 기대값 표기($\mathbb E$, $E_{\mathcal T}$, $\langle\cdot\rangle$, $\mathbb E_{\mathbf u}$). 묶음 "보조 계층"의 `g:state` 앞에 두었다. 링크를 건 곳:
  - 용어집: `g:depth`, `g:hierarchy`, `g:state`, `g:prescribed-tree`, `g:score`, `g:root-logarithm`, `g:self-average`, `g:overlap-concentration`, `g:conditional-covariance`, `g:disorder`
  - rules.md: P9
  - 카드: `decor:conditional-concentration.s2`, `decor:covariance-definition`, `decor:depth-continuity.s1`, `decor:overlap-concentration`, `decor:overlap-concentration.s1`, `decor:overlap-concentration.s2`, `decor:projection-bound`, `x:decor-tree-sampling`
  - L0, L1: 연결하지 않았다. 두 문서는 "root"를 "root logarithm" 안에서만 쓴다.
- `g:palm-identity` — Palm 항등식과 Taylor 계수 소거. 묶음 "Tree 계산과 항등식"의 `g:tree-identity` 앞에 두었다. 링크를 건 곳: 용어집의 `g:perturbation`, `g:score`, `g:selected-sequence`; rules.md의 Taylor 계수 추출 항목.
- `g:disorder` — 물리적 disorder. `build/glossary-additions-model.md`에서 합쳤다. 아래 추가 건 (d).

항목 수는 62에서 65가 되었다.

## 추가 건 (§2·§3 검토에서 온 것)

| 건 | 판정 | 근거 | 고친 곳 |
|---|---|---|---|
| (a) `g:positivity` "soft SAT($b<0$)" | 반영 | `consequences.tex` 40 "$W\ge0$", 59 "$b=e^{-\beta W}-1$", 61 "$0\le-b<1$". 그래서 $-1<b\le0$ 이다. 같은 검토(F13 덧붙임)의 말대로, 두 예에서 성립한다는 것은 증명된 사실이므로(30–31, 61–62) 그 부분의 유형을 weakening으로 나눴다. frustration 읽기는 intuition으로 남겼다. rules.md "확신이 낮은 대응" P1 항목의 같은 표현도 고쳤다. | glossary.md, rules.md |
| (b) `g:site-term` 새 spin의 좌표 | 반영 | `model.tex` 59–63 $e^{\theta(s_1,\ldots,s_{p-1},\varepsilon)}$. 원래 $\theta$ 는 순열 불변이 아닐 수 있고(`reduction.tex` 46–47), 상한은 원래 $\theta$ 에 쓰인다(`upper.tex` 37–39, 62–66). | glossary.md |
| (c) `g:rsb-steps` 정의 위치 | 반영 | `model.tex` 70 "Fix $r\ge1$", $r=0$ 은 118–120. `model:chain`도 넣었다. | glossary.md |
| (d) `g:disorder` 합치기 | 반영(세 가지를 손봄) | 바깥 $\mathbb E$ 는 $\eta_0$ 도 평균한다: $\mathscr F_0$ 이 disorder와 $\eta_0$ 으로 생성되고 $T_0V$ 가 $\mathscr F_0$-가측이다(`model.tex` 90–91). "선택된 매개변수가 root에 더해진다"는 `cavity.tex` 29–31과 어긋나므로 "매개변수는 root의 무작위 변수가 아니라 선택된 고정값"으로 바꾸고 [[g:root]]를 가리켰다. 정의 위치에 `model:vs`와 `model.tex` 82를 더했다. 묶음 "모형" 끝에 두었다. `g:root`에서 이 항목을 가리킨다. 추가 파일 자체는 고치지 않았다. | glossary.md |
| (e1) `g:insertion` 가정 | 반영 | `trees.tex` 73–74(원문이 처음에 두는 가정: $A$ 가 root 조건부로 위로 유계이고 0에서 떨어져 있음), 85–87(kernel은 반복되는 분배함수의 tilted kernel, $K_L$ 은 terminal Gibbs kernel). | glossary.md |
| (e2) `g:hierarchy` 기호 칸 | 반영 | `trees.tex` 58–64: tilt 꼴은 $1\le d<L$ 에서만이고 $K_L$ 은 Gibbs kernel이다. 기호 칸을 둘로 나눴다. | glossary.md |

## 손대지 않고 사용자에게 넘긴 것

- 이름 선택:
  - "선택된 수열". 카드 `decor:overlap-concentration.s2`의 "선택된 perturbed 수열"도 그대로 두었다.
  - "prescribed-tree 항등식"과 "처방된 tree 항등식"의 통일.
  - "clustering"을 "조건부 decorrelation"으로 바꿀지(표제어 그대로).
  - `g:self-average`를 둘지, "집중"으로 바꿀지.
  - "branching pattern"을 "shape"로 바꿀지. 이름은 바꾸지 않았고, `g:topology` 정의 위치에 원문 낱말 "shape"(`trees.tex` 460–462)만 적어 두었다.
- 고전적 GG 요약 한 줄을 지울지: 지우지 않고 "원문에 없는 대조용 요약이고 항등식의 한쪽 항만 말한다"는 표시만 붙였다.
- P8 규칙 문장의 주어 "connected correlation"을 "조건부 공분산"으로 바꿀지(검토 판단 6): 이름 문제라 손대지 않았다.
- §3 작성자의 추가 제안 `build/glossary-additions-trees.md`(`g:protected-leaf`, `g:reference-path`)는 합치라는 지시가 없어 합치지 않았다. 용어 검사에 남은 오류 5건은 모두 이것 때문이다. 합칠 때 두 가지를 알아 두면 좋다. 이번에 `g:extension-history` 뜻 칸에 "reference path"를 한 줄로 정의했으니 `g:reference-path`가 들어오면 그 줄을 그 항목으로 바꾸는 것이 낫다. 또 `g:palm-identity`의 "anchor 인자 상쇄"는 `g:protected-leaf`를 가리킬 자리다.
- 카드 본문 54장 전체의 재검토는 하지 않았다. 고친 것은 위에 적은 문장들뿐이다.
