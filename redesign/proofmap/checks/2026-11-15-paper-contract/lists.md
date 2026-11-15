### 열림 전부 (6)

| node | 입력 | 쓰는 줄 | 이유 |
|---|---|---|---|
| `model:trial-bounds` | $\|\log C_\theta\|,\|U_\theta\|\le B(\theta)$ (message 에 대해 균등) | 126, 127 | 번호 없는 진술, model.tex 65–66 |
| `tree:log-expansion` | protected leaf 가 있을 때의 미분 규칙: 남는 항은 새 fresh path 뿐이고 계수는 $\gamma_\beta$ | 244, 245, 246 | 번호 없는 진술, trees.tex 178–202 |
| `tree:log-expansion` | 복소 영역에서의 해석성과 균등 경계 (수렴 영역) | 231, 254 | 번호 없는 진술, trees.tex 156–176 |
| `tree:extension-expansion` | protected leaf 가 있을 때의 미분 규칙 | 299, 300, 301 | 번호 없는 진술, trees.tex 178–202 |
| `tree:extension-expansion` | 해석적 경계 | 294, 295 | 번호 없는 진술, trees.tex 156–176 |
| `upper:bound` | $\|\log C_\theta\|,\|U_\theta\|\le B(\theta)$ (message 에 균등) | 53, 54, 88, 89 | 번호 없는 진술, model.tex 65–66 |

### 바닥 전부 (27개, 쓰임 42회)

| id (쓰임) | 종류 | 인용 | 진술 |
|---|---|---|---|
| `poisson_splitting` (2) | standard | — | Poisson 과정의 분할(thinning)과 중첩, 평균이 다른 두 Poisson 과정을 공통점으로 결합하면 서로 다른 점의 기대 개수는 평균의 차이 이하. |
| `regular_conditional_probability` (1) | standard | comparison.tex 52–53 | 표준 Borel 공간 위에서 조건부 확률분포(확률 kernel)는 가측 버전을 가진다. |
| `tv_product_telescoping` (1) | standard | comparison.tex 112–118 | 곱측도의 전변 거리: $\\|\mu^{\otimes a}-\nu^{\otimes a}\\|_{\rm TV}\le a\\|\mu-\nu\\|_{\rm TV}$ (망원합). |
| `tv_bounded_integral` (1) | standard | comparison.tex 119 | 절댓값이 1 이하인 함수의 두 확률측도에 대한 적분의 차는 전변 거리의 2 배 이하이다. |
| `wald_identity` (2) | standard | comparison.tex 186–190 | 독립인 Poisson 개수 $K$ 와 같은 법칙의 (적분가능한) 항들의 합에서 $\mathbb E\sum_{j\le K}X_j=\mathbb EK\cdot\mathbb EX_1$ (Wald). |
| `jensen` (2) | standard | — | Jensen 부등식: 오목 함수 (예: $x\mapsto x^\gamma$, $0<\gamma\le1$) 에 대해 평균의 함수 값이 함수 값의 평균 이상 (질량 $\le1$ 인 측도에도 성립); 조건부 기댓값은 제곱 노름을 줄인다. |
| `martingale_orthogonality` (1) | standard | — | 유계 (벡터) martingale 의 증분은 서로 직교하므로 증분 제곱의 합은 마지막 값의 제곱 노름 이하이다. |
| `l2_projection` (1) | standard | — | 조건부 기댓값 $\mathbb E[X\mid\mathcal G]$ 는 $L^2$ 에서 $\mathcal G$-가측 함수 중 $X$ 에 가장 가까운 것이다. |
| `product_difference` (3) | standard | — | $x_j,y_j\in[-1,1]$ 이면 $\|\prod_jx_j-\prod_jy_j\|\le\sum_j\|x_j-y_j\|$ (따라서 제곱 노름은 $s\sum_j$ 로 누를 수 있다). |
| `power_mean_scaling` (2) | standard | — | 조건부 거듭제곱 평균 $(\mathbb E[X^m\mid\mathcal G])^{1/m}$ 은 $X$ 에 대해 단조이고, $\mathcal G$-가측 양수 인자를 곱하면 그 인자만큼 곱해진다 (동차). |
| `efron_stein` (1) | cited | EfronStein perturbations.tex 179 | Efron–Stein 분산 부등식: 독립 입력의 함수 $Z$ 에 대해 $\operatorname{Var}Z\le\frac12\sum_j\mathbb E(Z-Z^{(j)})^2$ ($Z^{(j)}$ 는 $j$ 번째 입력을 독립으로 다시 뽑은 것; 동일 분포나 대칭 통계량은 필요 없다). |
| `total_variance` (2) | standard | — | 전체 분산 법칙: $\operatorname{Var}Z=\mathbb E\operatorname{Var}(Z\mid\mathcal G)+\operatorname{Var}(\mathbb E[Z\mid\mathcal G])$. |
| `convex_derivative_monotone` (1) | standard | — | 볼록 함수의 도함수는 단조 증가하고 차분몫은 양쪽 도함수 사이에 끼인다. |
| `fubini` (1) | standard | — | Fubini–Tonelli: 유계(또는 음이 아닌) 가측 함수의 곱측도 적분은 순서를 바꿔도 같다. |
| `markov_inequality` (1) | standard | — | Markov 부등식: $X\ge0$ 이면 $\mathbb P(X>a)\le\mathbb EX/a$. |
| `diagonal_subsequence` (1) | standard | — | 유계 실수열은 수렴 부분수열을 가지며, 가산 개의 유계 수열 족에는 대각선 논법으로 모두 동시에 수렴하는 공통 부분수열이 있다. |
| `cauchy_schwarz` (4) | standard | — | Cauchy–Schwarz 와 Jensen: $\mathbb E\|X\|\le(\mathbb EX^2)^{1/2}$, 합과 적분에 대한 $\sum\|x_iy_i\|\le(\sum x_i^2)^{1/2}(\sum y_i^2)^{1/2}$. |
| `poisson_moments` (1) | standard | — | Poisson 확률변수는 모든 moment 가 유한하고 분산은 평균과 같다. |
| `poisson_add_one` (1) | standard | — | Poisson add-one (Mecke/Palm) 항등식: 평균 $\lambda$ 인 Poisson 개수 $n$ 의 점들에 대한 합 $\mathbb E\sum_{q\le n}F(\xi_q,\text{나머지})$ 는 독립인 새 점 $\xi$ 를 더한 계에서 $\lambda\,\mathbb EF(\xi,\text{나머지}\cup\{\xi\})$ 와 같다. |
| `cauchy_estimates` (1) | standard | — | 원판에서 $\|f\|\le M$ 인 해석 함수의 Taylor 계수는 $\|a_k\|\le M\rho^{-k}$ (Cauchy 추정), 더 작은 원판에서 Taylor 꼬리는 기하급수적으로 작고 도함수도 균등하게 유계이다. |
| `polarization` (1) | standard | — | 분극 항등식: 대칭 $k$-선형 형식 $\mathcal L$ 과 $Q(g)=\mathcal L(g,\ldots,g)$ 에 대해 $\mathcal L(g_1,\ldots,g_k)=\frac{1}{2^kk!}\sum_{\epsilon\in\{\pm1\}^k}\bigl(\prod_j\epsilon_j\bigr)Q\bigl(\sum_j\epsilon_jg_j\bigr)$. |
| `diff_under_expectation` (2) | standard | — | 유계 함수의 적분(기댓값) 안에서 매개변수로 미분할 수 있다 (유계 지배에 의한 적분 기호 아래 미분). |
| `analytic_taylor` (2) | standard | — | 원판에서 해석적인 함수는 그 원판 위에서 Taylor 급수와 같고, 계수는 $k$ 차 도함수를 $k!$ 로 나눈 값이다. |
| `poisson_derivative` (1) | standard | — | Poisson 평균에 대한 미분: 유계 $g$ 에 대해 $\frac{d}{d\lambda}\mathbb E\,g(\mathrm{Pois}(\lambda))=\mathbb E[g(\mathrm{Pois}(\lambda)+1)-g(\mathrm{Pois}(\lambda))]$. |
| `dominated_convergence` (3) | standard | — | 지배 수렴 정리. |
| `convex_even_power` (1) | standard | — | $p$ 가 짝수이면 $x\mapsto x^p$ 는 $\mathbb R$ 위에서 볼록이다. |
| `mean_value` (2) | standard | — | $[0,1]$ 에서 연속이고 $(0,1)$ 에서 미분가능한 $\varphi$ 의 $\varphi^{\prime}$ 가 위에서 $c$ 로 막히면 $\varphi(1)-\varphi(0)\le c$ (적분 또는 평균값 정리). |

### 절 머리·remark·번호 없는 문단 가운데 기호 표로 받지 못한 것 (25 / 60)

| 절 | 줄 | 내용 |
|---|---|---|
| cavity | 3–9 | 절 머리: reservoir 비교의 소개와 문헌, 섭동을 더해 spin tree 의 항등식을 얻는다는 약속 |
| comparison | 4–6 | 절 머리의 약속: 세 단계(부호화, multioverlap 집중으로 site 분리, insertion logarithm 비교)로 reservoir 를 시행 법칙으로 바꾼다는 개요 |
| comparison | 140–140 | singleton 의 평균은 깊이 좌표가 없다는 주의 (decor:overlap-concentration 의 singleton 항목이 담음) |
| consequences | 127–129 | 식 (10.1) 의 infimum 은 각 양의 온도에서 유한 hierarchy 전체에 대해 취하며 달성이나 극한 hierarchy 를 요구하지 않는다 (진술 뒤 문단) |
| consequences | 131–138 | Remark 10.4: 짝수 arity 가정이 random 3-SAT 을 제외한다는 주의 (외부 논문 인용) |
| decorrelation | 8–9 | 논증은 이 항등식과 tree 표본 규칙만 쓰며 상호작용 인수분해는 쓰지 않는다 (범위 주장) |
| decorrelation | 11–13 | 목표: 분리된 내부 branching 깊이에 대한 평균에서 모든 유한 multioverlap 의 집중 (§8 비교에 쓰임) |
| decorrelation | 77–83 | 증명 개요 (공분산 귀납, 한 단계 늦추기, marker anchor, 깊이 평균의 필수성) |
| decorrelation | 105–106 | 이어지는 lemma 가 제곱 공분산을 귀납량으로 삼는 이유를 설명하는 문장 |
| decorrelation | 305–330 | 그림: 목표 갈라짐을 한 칸 늦출 때의 국소 효과 (계수 $-\delta$) |
| decorrelation | 526–530 | §7.3 도입: 공분산 추정과 marker anchor, 평균 연속성의 결합 |
| decorrelation | 613–623 | Remark: 극한의 순서 (작은 분모는 항등식 오차에만, $N$ 극한은 $L$ 에 균등하지 않음) |
| main | 138–140 | 주정리가 말하지 않는 것: 우변은 유한 hierarchy 위 infimum 이며 달성이나 무한 깊이 극한 Gibbs 상태의 구성을 가정하지 않는다 (remark) |
| model | 3–5 | 절 머리 약속: $p$ 짝수, $\alpha>0$, $\theta$, $h$, $B(\theta)$ (node model:integrability 의 출력 setting 으로도 받음) |
| model | 65–66 | 번호 없는 사실 진술: $\|\log C_\theta\|,\|U_\theta\|\le B(\theta)$ (message 에 균등) |
| model | 138–140 | 주정리가 말하지 않는 것 (remark; main:theorem 단계 몫) |
| perturbations | 12–24 | 전략 요약 단락 (집중에서 항등식으로, 부호로 깊이 선택)과 선행 연구(GG98, AC98, BarraDeSanctis07, Pan13) 언급 |
| perturbations | 538–547 | Remark: 선택의 순서 (mark 와 $c_\nu$ 먼저, 수열 선택, $N\to\infty$ 후 $j\to\infty$, 그 뒤에 $L$) |
| reduction | 4–7 | 절 머리의 약속: bounded·순열 불변 하한과 factorization·positivity 상한을 상수 이동과 균등 근사로 잇는다는 개요 |
| trees | 3–12 | 절 머리: 두 전개의 소개와 문헌, 유한 kernel 열에서 직접 유도한다는 약속 |
| trees | 156–176 | 번호 없는 사실 진술: 복소 영역에서의 해석성과 균등 경계 (Analytic bounds) |
| trees | 184–202 | 번호 없는 사실 진술: protected leaf 와 fresh path 가 있을 때의 미분 규칙 |
| trees | 317–335 | 두 path 예: 부호 있는 합 $-\delta$ 대 절댓값 합 $2+\delta$ (remark 성 계산 예) |
| trees | 516–525 | remark tree:averaging-remark: 깊이 평균을 $Q_k$ 평균으로 옮기기 |
| upper | 3–9 | 절 머리: 문헌 소개와 완전한 시행 법칙 클래스를 다룬다는 약속 |

### 카드 의존 거절 (17건)

| node | 카드 → use | 이유 |
|---|---|---|
| `cavity:increment` | `cavity:increment.s4` → `cavity:negligible` | 증명 71–115 에 (5.3) 을 쓰는 줄이 없다: 증분 경계는 $\|\log Y_{0,\rm s}\|\le H+BK_{\rm s}$ 와 coupling 평가(109–113)로만 얻는다. |
| `comp:low-increments` | `comp:low-increments` → `cavity:increment` | 8–15행은 증분의 균등 유계나 reservoir 항등식을 쓰지 않는다. 증분은 $P_{N+1}^{L,\mathbf u}-P_N^{L,\mathbf u}$ 라는 정의로만 쓰이고 그 정의는 pert_increment 로 묶었다. |
| `comp:low-increments` | `x:comp-standing` → `cavity:grid` | 깊이 $L\ge2$ 는 9행이 직접 다시 적는다. 격자 $m_d=d/L$ 은 8–15행에 나오지 않는다. |
| `comp:low-increments` | `x:comp-standing` → `x:pert-selected-limits` | 이 node 가 쓰는 것이 아니라 정의하는 것이다. §8 약속(8–12행)이 pert:selection 을 직접 인용해 $N$ 을 선택된 수열 위의 크기로 정한다(perturbations.tex 308–312 의 약속은 인용하지 않는다). |
| `comp:encoding` | `comp:encoding` → `pert:factor` | 증명이 $\psi_\nu$ 를 직접 쓰지 않는다. 섭동은 reservoir(cavity:increment)와 그 tilted kernel 에 들어 있다. (finite mark 공간은 mark_specification 으로, 가중치 양수성은 perturbation_factors 로 묶었다.) |
| `comp:encoding` | `comp:encoding` → `pert:selection` | '선택된 매개변수 벡터'는 §8 약속(comp_selection)으로 묶었다. 렘마는 벡터가 고정되어 있다는 것만 쓰고 pert:selection 의 (i)–(iii) 를 쓰지 않는다. |
| `comp:shape-error` | `comp:shape-error-bound` → `tree:averaging-remark` | 번호 없는 remark 이고 그 내용(깊이 합→$Q_k$ 평균, 부분 shape 오차)은 tree:regular-shapes 의 assignment_probability 와 irregular_probability 로 이미 묶었다(comparison.tex 141–152). |
| `comp:shape-error` | `comp:shape-error` → `x:decor-limit-order` | §8 이 극한 순서를 직접 적는다(130행, 153–155행: 고정 $L$ 에서 $N$ 극한 후 $L\to\infty$). decorrelation.tex 4–9 의 약속은 인용하지 않으며 comp_selection 과 decor:overlap-concentration 진술로 충분하다. |
| `comp:bounded-lower` | `comp:bounded-lower` → `cavity:grid` | 격자는 원문에 $\mathbf m^{(L)}$ 로만 나타나며 그 정의(comparison.tex 161–162)를 symbol uniform_grid_vector 로 묶었다. |
| `decor:identity-error` | `decor:identity-error` → `decor:average-definition` | 범위(49–58) 안에서 깊이 평균 $\mathcal A$ 를 쓰지 않는다; 오차는 깊이 평균 이전에 유한 족에서 최대화한다. |
| `decor:overlap-concentration` | `decor:overlap-concentration.s4` → `x:decor-average-comparisons` | 증명은 Hölder 형 비교나 좌표 비교 문장을 직접 인용하지 않고 (decor:fiber-bound) 로 받는다 (605–609). |
| `decor:overlap-concentration` | `decor:overlap-concentration.s4` → `decor:average-holder` | 증명은 Hölder 형 비교나 좌표 비교 문장을 직접 인용하지 않고 (decor:fiber-bound) 로 받는다 (605–609). |
| `decor:overlap-concentration` | `decor:overlap-concentration` → `decor:identity-error` | 증명은 $o_N(1)$ 만 쓰고 $\varepsilon_{N,L,k}$ 를 인용하지 않는다 (533–569); 카드가 말한 $\varepsilon$ 최대화는 이 node 의 줄에 없다. |
| `decor:overlap-concentration` | `decor:overlap-concentration.s4` → `decor:identity-error` | 증명은 $o_N(1)$ 만 쓰고 $\varepsilon_{N,L,k}$ 를 인용하지 않는다 (533–569); 카드가 말한 $\varepsilon$ 최대화는 이 node 의 줄에 없다. |
| `decor:projection-bound` | `decor:projection-bound` → `x:decor-eta-regular` | 범위(208–230) 에는 $\eta$-regular 조건이 나오지 않는다; 결과는 정규성 없이 성립한다. |
| `pert:score-identity` | `pert:score-identity` → `pert:factor` | $\psi_\nu$ 는 이 node 범위(316–329)에서 직접 쓰이지 않는다; $D_\nu$ 는 pert:error 의 항목으로 받는다. |
| `pert:analytic` | `pert:analytic.s1` → `x:tree-analytic-bounds` | 원문은 해석적 경계를 별도 문단이 아니라 Lemma tree:extension-expansion (그 진술의 "analytic bounds ... uniformly") 에서 가져온다 (391); 그 입력은 tree:extension-expansion 의 lhs_analytic 로 묶었다. |

### 카드·원문 어긋남 (6건)

| node | 카드 | 내용 |
|---|---|---|
| `comp:low-increments` | `comp:low-increments` | 카드 source 는 12–15행이지만 뼈대 범위는 8–15행이다(8–12행의 절 약속 카드 x:comp-standing 을 이 node 에 붙였다). 약속 자체는 symbol comp_selection 으로 받았다. |
| `comp:shape-error` | `comp:shape-error` | 카드는 $Q_k$ 정의를 tree:log-expansion 에 건다(원문 123행 \cref). 정의 자체는 trees.tex 209–217 (tree:telescoping 의 Q_rule)이며 log-expansion 은 그것을 쓰는 곳이다. |
| `decor:overlap-concentration` | `decor:overlap-concentration` | 카드는 진술을 63–83 로 잡았으나 77–83 은 증명 개요 문단이고 526–530 도 증명 앞의 도입 문단이다 (진술은 63–75). |
| `decor:overlap-concentration` | `decor:overlap-concentration.s4` | 카드는 591–609 에서 평균 Hölder (36–43), 비교 (44–47) 를 쓴다고 하나 원문은 (decor:fiber-bound) 만 인용한다. |
| `pert:analytic` | `pert:analytic.s1` | 카드는 391–397 의 해석적 경계가 trees.tex 156–176 의 번호 없는 문단 (x:tree-analytic-bounds) 에서 온다고 하나, 원문은 Lemma tree:extension-expansion 를 인용한다. |
| `reduction:stability` | `x:reduction-power-mean-scaling` | 카드는 model.tex 90–97 이 단조·동차성을 말한다고 보지만 그 줄은 $T_d$ 의 정의뿐이고 단조성·동차성은 원문에 진술되어 있지 않다 (카드 자신이 '작성자 정식화'). 표준 사실이므로 floor power_mean_scaling 에 묶었다. |

### 출력 항목 추가 (6건)

| 대상 node | 항목 | 쓰는 node | 경로 |
|---|---|---|---|
| `comp:encoding` | `independent_of_new_disorder` | `comp:insertion-comparison` | 같은 agent 안 |
| `decor:average-holder` | `unused_coordinate` | `decor:conditional-concentration` | 같은 agent 안 |
| `decor:average-holder` | `integer_shift` | `decor:conditional-concentration` | 같은 agent 안 |
| `tree:telescoping` | `subtree_telescoping` | `tree:reference-total` | 같은 agent 안 |
| `upper:bound` | `bounded_factors` | `model:factorization` | 같은 agent 안 |
| `cavity:increment` | `log_insertion_bound` | `comp:insertion-comparison` | 뒤 단계 요청(new_item) |
