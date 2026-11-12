# 검토 2 — §6 perturbations 노드 카드 (독립 검토)

대상: `cards/pert.*.md` 36장, `cards/x.pert-*.md` 8장, 모두 44장.
기준: `source/sections/perturbations.tex`(547줄) 전체, `cavity.tex` 전체, `trees.tex` 전체, `decorrelation.tex` 1–95·255–310·520–623, `comparison.tex` 1–60·120–135·185–246, `overview.tex` 전체. `model.tex` 는 $F_N$ 의 정의만 필요해서 카드 `model:hamiltonian` 을 거쳐 확인했다.
"확인"은 원문과 한 줄씩 대조했거나 손으로 다시 계산했다는 뜻이다.

주의: `layers/glossary.md`, `layers/rules.md`, `cards/tree.section.md`, §3·§5·§7 카드는 다른 작업으로 바뀌는 중일 수 있다. 그 파일의 인용은 내가 읽은 시점의 문구다. `tools/check.py --sections perturbations --out <scratchpad>` 결과: 형식·정초·포함·의존·연결·순환·사전·단면 통과. 용어만 실패 2건인데 둘 다 §5 카드의 `[[g:bounded-law]]` 이고 §6 카드와 무관하다.

## 요약

- 읽은 카드: 44 / 44 (머리말과 본문 모두).
- `math` 칸의 식 전사: (6.1)–(6.18) 전부, (6.6)의 $2n$·$4n$, (6.8)의 $m_d$ 가중과 $-4n$, (6.9)의 $4\lambda_\nu(1+b-a)/m_1$, (6.10), (6.11), (6.12), $\rho=N^{-1/8}$, $s_N=N^{3/4}$, $j^{-3}$·$j^{-1}$·$j^{-2}$, $2Cj^{-j}$, polarization 계수 $k^k/(2^kk!)$, $R_E$ 의 두 경우를 원문과 대조했다. 부호, 계수, 지수, 첨자, 양화사, 극한 순서, 균일성의 범위가 어긋나는 곳은 **찾지 못했다**.
- `pert:selection` 의 구조("고정한 모든 $L\ge2$, $\varepsilon>0$ / 수열이 있어 / (ii) 모든 고정 type, reservoir / (iii) reservoir, 깊이 $L$ 의 모든 고정 유한 tree")는 원문 255–267 그대로다. `pert:tree-identity` 는 고정 $L$·tree·제약에서 율 없는 $\to0$ 만 말하고 물리 칸은 `approximation` 에 차이 칸 (1)이 그것을 적는다.
- 세 평균의 구별: 44장 어디에서도 $\mathbf u$ 를 root 변수로 쓰지 않았다. $\pi$ 적분은 `pert:concentration` 과 `pert:selection.s1`–`s2` 에만 나오고 원문(99, 150, 227, 240–243, 273, 276, 287–297)과 일치한다. "Lemma 6.1은 매개변수 평균만 증명하고 점별 수렴은 (ii)에서 나온다"는 작성자 주장은 맞다(원문 97–101, 262, 290–299).
- 작성자가 보탠 계산은 모두 다시 계산했다. **틀린 계산은 없다.** 다만 계산 옆에 붙인 설명 문장 두 곳이 틀렸다(F1).
- 증명 분해에 구멍은 없다. 다섯 증명 모두 원문 순서 그대로 빠짐없이 덮는다(아래 "분해").
- `uses` 그래프: 순환 없음(스크립트와 손으로 확인). 존재하지 않는 ID 없음.
- 용어 규율: Ghirlanda–Guerra, stochastic stability는 `pert:section` 본문의 원문 17–24행 인용 한 곳에만 나온다. "상태"는 `pert:selection` 의 차이 칸에 "이 수열은 상태가 아니다"로 한 번, `g:state` 링크와 함께 나온다. "clustering", "self-average", "처방된 tree 항등식", 주어로서의 "connected correlation", Ruelle cascade, ultrametricity, R번호는 없다.
- 지적 8건. 통과 34장, 지적이 걸린 카드 10장.

| 유형 | 건수 | 번호 |
|---|---|---|
| 틀림 (식·진술) | 0 | — |
| 구멍 | 0 | — |
| 틀린 설명 (차이 칸·본문) | 1 | F1 |
| 부정확한 묘사 | 3 | F2, F5, F6 |
| 누수 (`uses`·표) | 2 | F3, F4 |
| 유형 (`abstraction`) | 1 | F7 |
| "작성자" 표시 누락 | 1 | F8 |

| 심각도 | 건수 | 번호 |
|---|---|---|
| 높음 | 0 | — |
| 중간 | 1 | F1 |
| 낮음 | 7 | F2–F8 |

## 지적 (심각도 순)

### F1. 틀린 설명 — `pert:concentration.s3` (gap), `pert:concentration.s4` (본문) · 중간
- 카드 (`s3` gap): "분산 상계 $O(N)$ 은 score의 규모 $\lambda_\nu=c_\nu N^{3/4}$ 보다 크다. 그래서 이 상계만으로는 score의 root 요동이 작다는 것이 나오지 않고, 볼록성을 쓰는 s4가 필요하다."
- 카드 (`s4` 본문): "$G$ 자체의 root 요동은 $\sqrt N$ 규모로 score 규모 $N^{3/4}$ 보다 작지 않지만 그 차이가 $\rho$ 로 나뉘는 대신, 도함수의 요동은 …"
- 원문: perturbations.tex 172 "$\operatorname{Var}(G(u))\leq C_\nu N$", 229–235 "$C_\nu(\sqrt N/\rho+\rho\lambda_\nu/|I_\nu|)$ … take $\rho=N^{-1/8}$ … After division by $\lambda_\nu=c_\nu N^{3/4}$, both terms tend to zero."
- 두 문장은 규모 비교가 틀렸다. 견줄 것은 분산 $N$ 이 아니라 표준편차 $\sqrt N$ 이고, $\sqrt N$ 은 $N^{3/4}$ 보다 **작다**. 바로 그래서 $\sqrt N/(\rho\lambda_\nu)=c_\nu^{-1}N^{-1/8}\to0$ 이 된다. 볼록성이 필요한 까닭은 규모가 아니라 대상이다: (6.11)은 함수 $G$ 의 요동을 누르는데 필요한 것은 도함수 $G'=\langle D_\nu\rangle+4nu$ 의 요동이고, 함수값의 요동 상계는 볼록성 없이는 도함수의 요동을 누르지 못한다. 부모 `pert:concentration` 본문("root 분산은 $O(N)$ 이지만 score는 $N^{3/4}$ 규모이므로 $\sqrt N/\rho+\rho\lambda_\nu$ 를 $\lambda_\nu$ 로 나눈 것이 0으로 갈 수 있다")과 `s4.s2` 의 지수 계산은 옳아서, 같은 증명 안에서 서로 어긋난다.
- 제안: `s3` gap을 "이 상계는 함수 $G$ 의 root 요동(표준편차 $O(\sqrt N)$)에 대한 것이고 그 도함수인 score 평균의 요동에 대한 것이 아니다. 도함수로 옮기려면 볼록성을 쓰는 s4가 필요하다. $\sqrt N\ll\lambda_\nu\sim N^{3/4}$ 이라는 것이 s4에서 $\rho$ 를 고를 여지를 준다."로. `s4` 본문을 "$G$ 의 root 요동은 $\sqrt N$ 규모로 score 규모 $N^{3/4}$ 보다 작다. 차분몫으로 도함수로 옮기면 이것이 $\rho$ 로 나뉘고, 볼록성 덕분에 나머지는 평균 도함수의 변화 $\rho\lambda_\nu$ 로만 남는다."로.

### F2. 부정확한 묘사 — `pert:tree-identity` (physics, gap 3), `pert:section` (math, gap 3, "§7 카드와의 대조") · 낮음
- 카드 (`pert:tree-identity` physics): "깊이별 mark로 anchor와 새 replica들 사이의 split 깊이를 임의로 지정할 수 있다." gap (3): "제약은 anchor와 새 color 사이의 split 깊이만 지정하고". `pert:section` math: "anchor와 추가 color 사이의 split 깊이 제약 $\mathcal C$", gap (3) "제약은 anchor와 새 color 사이만 지정한다", 본문 "제약은 모두 anchor와 추가 color 사이의 split 깊이만 처방한다."
- 원문: 434–435 "A constraint $\mathcal C$ prescribes any **consistent** collection of their **pairwise** split depths, involving only the added colors and the anchor." 495–496 "For a pair of colors $a,b\in\{0,\ldots,k\}$".
- 제약은 $\{0,\ldots,k\}$ 안의 모든 쌍, 곧 추가 color끼리의 쌍도 처방한다. "anchor와 새 color 사이"는 anchor–color 쌍만으로 읽힐 수 있다. §7의 사용(decorrelation.tex 298–302의 $S^+$ 두 사본, 540–541의 $S$ 사본 전체)은 color끼리의 split 깊이를 처방하므로 이 구별이 실제로 쓰인다. 또 "임의로"는 "일관된"이 빠졌다. `x:pert-colored-extensions` 의 `math`("추가 color들과 anchor만 관여하는 쌍별 split 깊이의 임의의 일관된 모임")는 정확하다.
- 제안: "anchor와 추가 color들로 이루어진 집합 안의 쌍별 split 깊이를 일관된 한 임의로 지정할 수 있다(다른 old replica가 관여하는 쌍은 지정하지 못한다)"로 통일한다. 읽은 시점의 `g:mark` 역할 칸, 규칙 P7 문장, L1 수 4도 같은 문구("anchor와 새 color/replica들 사이")를 쓴다. 함께 고치도록 조율에 넘긴다.

### F3. 누수 — `pert:analytic.s1`, `pert:tree-identity.s2`, `pert:concentration.s3.s2` (`uses`) · 낮음
- `pert:analytic.s1`: 본문 "경계 자체는 [[x:tree-analytic-bounds]]", "Shrinking $\rho$는 Cauchy 추정". `uses` 에 `x:tree-analytic-bounds` 가 없다. $u$-도함수의 균등 경계는 lemma 진술(trees.tex 294–295 "The analytic bounds established above apply to its left-hand side")이 아니라 trees.tex 173–176("They also bound \eqref{tree:density}, its canceled versions below, and their derivatives on smaller domains, uniformly over the kernels")에 있고 그 줄을 담은 카드가 `x:tree-analytic-bounds` 다. `tree:extension-expansion` 을 거쳐 전이적으로 닿지만 이 단계가 직접 쓰는 사실이다. 제안: `uses` 에 넣는다.
- `pert:tree-identity.s2`: 본문 "mark가 base reservoir와 독립이라는 것은 [[pert:palm-expression]]의 …". `uses` 에 없다(원문 512 "All marks in this calculation are independent of the base reservoir"의 근거는 336–338). 제안: 넣는다.
- `pert:concentration.s3.s2`: `math` "물리적 개수와 섭동 총 개수에 조건을 건다"는 물리 disorder의 구조(평균 $O(N)$ 의 Poisson 개수, 원문 6–8)에 기댄다. `uses` 는 `[pert:concentration.s3.s1, pert:factor]` 뿐이다. 형제 `s3.s3` 에는 `x:pert-standing` 이 있다. 제안: 넣는다.
- 세 곳 모두 순환은 생기지 않는다.

### F4. 누수 — `pert:section` ("밖에 내주는 것" 표) · 낮음
- 카드: 표의 §5 행은 "cavity.tex 32 … (예고)" 하나다. 본문 "[[pert:concentration]], [[pert:palm]], [[pert:analytic]]은 이 절 밖에서 쓰이지 않는다".
- 원문: cavity.tex 119–121 "The reservoir retains an independent Poisson interaction process of mean $O(N)$ and $N$ independent bounded fields. Thus the concentration argument applies to its slightly modified interaction mean as well." 이것은 Lemma 6.1의 Efron–Stein 논증(perturbations.tex 176–206)을 가리키는 예고다. 읽은 시점의 `x:cavity-tree-sampling` 의 `provides` 도 "score 집중의 Efron–Stein 논증이 reservoir에도 적용"이라 적는다. "받는 것" 표에는 이 행이 있는데 "내주는 것" 표에는 짝이 없다.
- 제안: 표에 "§5 cavity.tex 119–121 | '`the concentration argument`' → [[pert:concentration]] (예고, `\ref` 없음)" 행을 더하고 위 문장을 "예고(cavity.tex 119–121)를 빼면 이 절 밖에서 쓰이지 않는다"로 고친다.
- 덧붙임(§7 쪽, 고치지 않는 파일): `provides` 는 `x:pert-colored-extensions` 를 `decor:overlap-concentration.s1`, `s2.s1`, `decor:conditional-concentration.s2.s1`, `s3.s1` 에 내준다고 적는데, 읽은 시점에 그 네 카드의 `uses` 에는 이 ID가 없다(`pert:tree-identity` 를 거쳐 전이적으로만 닿는다). "spin anchor", "marker anchor", "added color"의 정의가 이 카드에만 있으므로 §7 카드에 넣을지 조율에서 정한다. 진술의 내용은 어긋나지 않는다.

### F5. 부정확한 묘사 — `pert:concentration.s3.s3` (본문) · 낮음
- 카드: "보정 $2nu^2$ 는 $n$ 의 Lipschitz 함수이고 $u$ 가 유계이므로 같다."
- 원문: 176–178 "condition on the physical and total perturbation counts. Conditional on the latter count, its types and sites are independent labels", 207 "The correction $2nu^2$ obeys the same estimates."
- $n=n_\nu$ 는 조건을 건 두 개수(물리 개수, 섭동 **총** 개수) 가운데 하나가 아니다. 총 개수가 주어지면 $n_\nu$ 는 type label들의 함수다. 그래서 "같은 추정"은 두 부분이다: label 하나를 다시 뽑으면 $n_\nu$ 가 많아야 1 바뀌어 보정이 $2u^2$ 이하로 바뀌고(Efron–Stein 쪽), 총 개수가 1 바뀌면 조건부 평균이 $2u^2$ 이하로 바뀐다(Lipschitz 쪽). 결론은 같다.
- 제안: "보정 $2nu^2$: 총 개수가 주어지면 $n_\nu$ 는 type label의 함수라 label 하나를 바꾸면 보정이 $2u^2$ 이하로 바뀌고, 총 개수에 대해서도 같은 상수로 Lipschitz다. 그래서 같은 두 추정을 따른다(작성자 풀이)."

### F6. 부정확한 묘사 — `pert:palm.s1` (본문) · 낮음, 확신 낮음
- 카드: "여기서 점 $x$ 는 type-$\nu$ 항 하나(균일 site, mark 과정 사본)이고".
- 원문: 60–62 "Counts, types, and sites belong to the root; the mark variables are sampled with their product priors at their assigned auxiliary depths." 367–368 "The distinguished term becomes an independent new insertion".
- Poisson 과정은 root의 것이고 그 점이 지니는 root label은 site(와 type)다. mark 값은 root 변수가 아니라 path를 따라 뽑히는 보조 변수이고, 계의 tilt를 받는다. 점 $x$ 에 "mark 과정 사본"을 값으로 넣어 읽으면 mark가 root에서 미리 뽑힌 것처럼 보인다. 같은 문단의 뒤 문장("새 항이 쓰는 변수는 [[x:tree-extra-variables]]대로 prior로 붙음")은 옳다.
- 제안: "점 $x$ 는 type-$\nu$ 항 하나의 root label(균일 site)이다. 그 항의 mark 변수는 root가 아니라 보조 깊이의 새 변수이고, 점을 더한 계에서는 prior로 덧붙인 뒤 insertion으로 다룬다."

### F7. 유형 — `x:pert-mark-specification` (`abstraction: intuition`) · 낮음, 확신 낮음
- 카드 physics: "… 무작위 부호(mark)와, 그 부호들의 유리수값 함수를 site 하나의 spin(또는 상수 1)에 붙인 탐침이다. 두 replica path가 그 깊이의 vertex를 공유하면 같은 부호를 보고, 아니면 독립인 부호를 본다." 유형 `intuition`.
- SCHEMA: `intuition` 은 "논증에 쓰이지 않는 그림". 둘째 문장은 원문 33–34("the value of a coordinate is shared at a shared vertex and is independent at different vertices")의 정확한 옮김이고 selector(494–511)의 근거로 논증에 쓰인다. "탐침"만 그림이다.
- 제안: 유형을 `weakening` 으로 바꾸고 차이 칸의 "물리적 국소장이 아니다"는 그대로 둔다. `g:mark` 의 물리 대응 칸이 intuition인 것("탐침장")과는 따로다.

### F8. "작성자" 표시 누락 — `pert:section` (math) · 낮음
- 카드: "지수 $m_d$(cavity:grid; 증명은 $0<m_1\le m_d$, $m_L=1$ 만 씀)".
- 원문은 이 관찰을 적지 않는다(124 "$m_L=1$", 138 "$\geq m_1\operatorname{Var}$", 152·159의 $1/m_1$ 에서 읽어낸 것). 관찰은 옳다(확인). `x:pert-standing` 본문은 같은 말을 "작성자 읽기"로 표시했는데 섹션 카드의 `math` 칸과 "밖에서 받는 것" 표에는 표시가 없다.
- 제안: 괄호 안에 "작성자 읽기"를 붙인다.

## 통과 카드 (34장)

`pert:parameters`, `pert:factor`, `pert:score`, `pert:error`, `pert:concentration`, `pert:concentration.s1`, `pert:concentration.s2`, `pert:concentration.s2.s1`, `pert:concentration.s2.s2`, `pert:concentration.s3.s1`, `pert:concentration.s4.s1`, `pert:concentration.s4.s2`, `pert:selection`, `pert:selection.s1`, `pert:selection.s2`, `pert:selection.s3`, `pert:score-identity`, `pert:palm-expression`, `pert:analytic-difference`, `pert:palm`, `pert:palm.s2`, `pert:analytic`, `pert:analytic.s2`, `pert:analytic.s3`, `pert:tree-identity.s1`, `pert:tree-identity.s3`, `pert:tree-identity.s4`, `x:pert-standing`, `x:pert-parameter-measure`, `x:pert-increment`, `x:pert-selected-limits`, `x:pert-test-setup`, `x:pert-colored-extensions`, `x:pert-order-of-choices`.

지적이 걸린 10장: `pert:section`(F2, F4, F8), `pert:tree-identity`(F2), `pert:concentration.s3`(F1), `pert:concentration.s4`(F1), `pert:concentration.s3.s2`(F3), `pert:concentration.s3.s3`(F5), `pert:analytic.s1`(F3), `pert:tree-identity.s2`(F3), `pert:palm.s1`(F6), `x:pert-mark-specification`(F7).

## 작성자 보탬 검산

모두 다시 계산했고 결과는 맞다.

- $1/2<\psi_\nu<3/2$, 구간 $J_\nu$: $j\ge4$ 에서 $t_\nu\le1/4$, $u_\nu\le2\cdot4^{-4}=1/128$, 합이 $1/2$ 보다 작고 여유가 있어 $I_\nu$ 를 품는 열린 $J_\nu$ 가 있다. $\psi>1/2$ 에서 $|D_\nu|\le2n$, $|\partial_uD_\nu|\le4n$.
- (6.7)–(6.8): $X_{d-1}=m_d^{-1}\log P_de^{m_dX_d}$ 를 미분하면 $\partial X_{d-1}=K_d\partial X_d$, $\partial^2X_{d-1}=K_d\partial^2X_d+m_d\operatorname{Var}_{K_d}(\partial X_d)$. $\partial_uX_L=D_\nu$ 에서 $\partial_uX_d=M_d$, $\operatorname{Var}_{K_d}(M_d)=\langle(M_d-M_{d-1})^2\mid\mathscr F_{d-1}\rangle$, martingale 직교성으로 $\sum_d\langle(M_d-M_{d-1})^2\rangle=\operatorname{Var}(D_\nu\mid\mathscr F_0)$, $m_d\ge m_1$.
- (6.9)–(6.10): $\int_a^b\mathbb EX_0''\le4\lambda_\nu$, 하계의 적분 $m_1\int\mathbb E\operatorname{Var}-4\lambda_\nu(b-a)$. Cauchy–Schwarz와 구간 평균의 Jensen으로 (6.10).
- Efron–Stein의 증명 줄, Poisson Lipschitz 부등식 $\operatorname{Var}b(Q)=\frac12\mathbb E(b(Q)-b(Q'))^2\le C^2\operatorname{Var}Q$, 섭동 항 교체의 상수 $\log3$, $|\mathbb EG'|\le(2+4|u|)\lambda_\nu$.
- 차분몫: $G'(u)-\bar G'(u)\le\frac{Z(u+\rho)-Z(u)}\rho+\bar G'(u+\rho)-\bar G'(u)$ 와 대칭 부등식에서 원문 216–218. $\int_a^b[\bar G'(u+\rho)-\bar G'(u-\rho)]du=[\bar G(b+\rho)-\bar G(b-\rho)]-[\bar G(a+\rho)-\bar G(a-\rho)]\le2\rho[\bar G'(b+\rho)-\bar G'(a-\rho)]$.
- 지수: $\sqrt N/(\rho\lambda_\nu)=c_\nu^{-1}N^{1/2+1/8-3/4}=c_\nu^{-1}N^{-1/8}$, $\rho\lambda_\nu/(|I_\nu|\lambda_\nu)=N^{-1/8}/|I_\nu|$. 보정 $4u(n-\lambda_\nu)$, $\mathbb E|n-\lambda|\le\lambda^{1/2}$.
- $e_{\nu,N}$ 의 삼각부등식 분해(path 기여 + root 기여).
- telescoping 모순, Markov($q_j\le j\cdot j^{-3}$), 조건부 평균 $(\underline F+\varepsilon+Cq_j)/(1-q_j)$, (ii)가 $j\ge\nu$ 부터 성립, 대각 논법이 (i)(ii)를 보존.
- (6.13): $\mathbb E[f(D^{a_*}_\nu-\mathbb E\langle D_\nu\rangle)]$ 과 anchor marginal. 부등식은 모든 $N$, $\mathbf u$ 에서 성립하고 "$\to0$"만 (ii)에 기댄다.
- Mecke 항등식의 진술 $\mathbb E\sum_{x\in\Pi}F(x,\Pi)=\lambda\int\mathbb EF(x,\Pi\cup\{x\})\mu(dx)$ 과 그 적용(F6의 문구만 빼고).
- `pert:analytic.s3` 첫 부등식 $|H_N(1/j,0)|\le|H_N(1/j,u_{\nu,N})|+|u_{\nu,N}|\sup|\partial_uH_N|\le\|f\|_\infty e_{\nu,N}+C|u_{\nu,N}|$. $D_1=g\sigma_i$, $D_2=g_0S_0$ 로 영역 $|t|+|u|<1$.
- polarization: 혼합 도함수 $=F(g_1,\ldots,g_k)$($Q_N(\sum c_jg_j)$ 의 $c_1\cdots c_k$ 계수를 $k!$ 로 나눈 것), 표준 공식 $F=\frac1{2^kk!}\sum_\epsilon(\prod\epsilon_j)Q_N(\sum\epsilon_jg_j)$, 동차성 $Q_N(k^{-1}h)=k^{-k}Q_N(h)$. $Q_N$ 이 $g$ 에 대해 $k$ 차 동차인 것은 $H=fg_0S_0$ 이 $g$ 를 포함하지 않기 때문이다.
- selector: 같은 vertex면 $\xi^2=1$, 다른 vertex면 독립 평균 0. 좌표마다 두 color에만 배정되어 요구별로 곱해진다. $H_0=1$, $H_L=0$.

표시 없이 보탠 곳은 F8 하나만 찾았다.

## 분해와 식 라벨

- `pert:concentration`: s1(106–118) / s2(120–161: s2.s1 120–145, s2.s2 147–161) / s3(163–209: s3.s1 163–175, s3.s2 176–191, s3.s3 192–209) / s4(211–244: s4.s1 211–232, s4.s2 233–244). 원문의 세 문단 제목과 일치한다.
- `pert:selection`: s1(269–279) / s2(281–299) / s3(301–306). `pert:palm`: s1(362–377) / s2(378–381). `pert:analytic`: s1(390–397) / s2(399–409) / s3(411–425). `pert:tree-identity`: s1(472–492) / s2(494–512) / s3(514–524) / s4(526–536). 순서와 논리가 원문 그대로다.
- `pert:score-identity`((6.13))를 lemma 카드로 둔 것: 원문에서는 본문의 식이지만 `pert:palm` 증명이 378행에서 인용한다. §3의 `tree:first-variation`, `tree:telescoping` 이 같은 처리(kind `lemma`)다. 적절하다. 321행이 `x:pert-test-setup` 과 겹치는 것은 한 줄에 두 문장이 있어서다.
- 라벨 `pert:identity`: 원문 453행에만 있고 어느 섹션도 `\ref` 하지 않는다. `pert:tree-identity` 카드가 담고 본문에 적어 둔 것으로 충분하다.

## 인터페이스

- `pert:section` 의 "밖에서 받는 것" 표: 행마다 원문 위치를 확인했다. 맞다.
- "밖에 내주는 것" 표: decorrelation.tex 4–9, 51, 81, 265, 298–302, 529–560; comparison.tex 8–15, 20, 53–56, 130, 243; overview.tex 18, 24를 확인했다. 맞다. 빠진 것은 F4의 cavity.tex 119–121 하나다. `reduction.tex`, `consequences.tex`, `introduction.tex`, `upper.tex` 는 §6을 쓰지 않는다.
- §7 카드와의 대조(읽은 시점): `x:decor-limit-order`, `x:decor-mesh`, `decor:identity-error`, `decor:overlap-concentration.s1`, `s2.s1`, `decor:conditional-concentration.s2.s1`, `s3.s1`, `decor:section` 이 기대하는 수열, 양화사, anchor 종류, 오차($o_N(1)$, 고정 $L$)는 `pert:selection`, `pert:tree-identity`, `x:pert-colored-extensions` 의 진술과 맞는다. 작성자의 "어긋남 없음"에 동의한다. 다만 F2의 문구와 F4 덧붙임(§7 카드의 `uses`)이 남는다.

## "작성자 읽기"에 대한 의견

1. **"thermal mean absolute deviation"** $=\frac1{|I_\nu|}\int\mathbb E_{\mathbf u}\langle|D_\nu-\langle D_\nu\rangle|\rangle du$: 동의한다. 155–156행 "interval-averaged … divided by $\lambda_\nu$"와 (6.10)의 꼴, 239–240행에서 이것을 root 기여와 더해 (6.4)를 누르는 쓰임이 이 읽기만 허용한다.
2. **`pert:selection.s2` 의 $e$ 가 reservoir의 것**: 동의한다. 진술 (ii)가 "in the reservoir"이고 102행이 Lemma 6.1을 reservoir에도 준다. (i)의 $\Delta$ 는 $N$·$N+1$ 계의 것이고 같은 $\mathbf u$ 에서 두 대상을 함께 보는 것이다.
3. **"Shrinking $\rho$" = Cauchy 추정**: 동의한다. 읽기라기보다 trees.tex 173–176("their derivatives on smaller domains, uniformly over the kernels")의 직접 인용이다(F3).
4. **$s_N=N^{3/4}$ 를 규모 비교로**: 계산은 맞다. 다만 절반이다. 집중 쪽은 $\sqrt N\ll s_N$ 을 요구하고, $s_N=o(N)$ 은 `cavity:negligible` 과 맞춤 비용 $O(s_N/N)$(cavity.tex 93, 102)이 요구한다. 원문은 이유를 적지 않으므로 "작성자 읽기" 표시가 맞고, "두 조건 $\sqrt N\ll s_N\ll N$ 사이의 한 선택"이라고 쓰면 완전하다. F1의 두 문장은 이 읽기와 어긋난다.
5. **`x:pert-selected-limits` 에서 $\varepsilon$ 도 고정**: 동의한다. 257행 "For every fixed $L\ge2$ and $\varepsilon>0$", comparison.tex 7–8 "Fix $\varepsilon>0$. At each depth $L\ge2$, use the sequence …".
6. **$H=fg_0^{a_*}S_0^{a_*}$ 에 insertion 변수가 들어가도 됨**: 동의한다. trees.tex 135–140이 path kernel을 추가 변수의 prior로 넓히고 "Additional root variables remain quenched"라 하며, perturbations.tex 335–338이 바로 그 확장을 명시한다. anchor path의 mark는 넓힌 old tree의 변수이고 새 site는 root 변수이며 둘 다 $(t,u)$ 에 의존하지 않는다.

## 용어집 메모 (a)–(e)

- **(a) `g:selected-sequence` 역할 칸**: 동의한다. Palm 부등식은 모든 $N$, $\mathbf u$ 에서 성립하고(350–356), (ii)는 우변을 0으로 보내는 데 쓰인다. 쓰이는 줄은 418("Here the score error tends to zero with $j$ fixed")과 (6.13)의 "$\longrightarrow0$"(327) 두 곳이다. 제안 문구에 327을 더한다.
- **(b) `g:concentration`**: 동의한다. Lemma 6.1의 결론은 (6.5) $\int e\,d\pi\to0$ 뿐이다.
- **(c) `g:perturbation`**: 동의한다. $t_\nu=1/j$ 는 $N$ 과 무관한 고정값이다. "무한소"는 intuition 칸에 있으므로 지금 문장도 틀리지는 않는다.
- **(d) `g:mark` 정의 위치**: 동의한다. `pert:mark-selector` 는 식 라벨이고 카드는 `pert:tree-identity.s2` 다. 규칙 P7의 수학 노드 열에도 같은 식 라벨이 있다(읽은 시점). 검사는 통과하지만 카드 ID로 바꾸는 편이 SCHEMA("수학 노드: 대응하는 노드 ID")에 맞다.
- **(e) `tree:section` 의 §6 행**: 읽은 시점의 표(45–46행)는 334–338, 370, 391, 433과 64–65만 적는다. 작성자가 든 빠진 사용을 하나씩 원문에서 확인했고 모두 실제 사용이다: `x:tree-sampling`(321 "anchor marginal is always one tilted path", 516–517 "positions in the sampled tree"), `tree:multioverlap`(317, 441–448), `tree:original-tilt`·`x:tree-path-kernels`(121–131), `tree:Y-recursion`(333–334), 단조성과 `x:tree-extra-variables` 의 둘째 사용(193–196), `tree:extension-expansion` 의 `\ref` 없는 사용(403–405, 478–492, 526). 읽은 시점의 `x:tree-extra-variables` 의 `provides` 도 336–338만 적는다. 표와 `provides` 에 더하는 것이 맞다.

## 규칙 P5·P6·P7, L1 수 3–4 (읽은 시점)

- **P5**: 원문 255–267, 269–306과 맞는다. 차이 칸이 "먼저 매개변수 평균, Markov로 한 점, 대각 부분수열", "type별, 균일하지 않음", "$L$·$\varepsilon$ 마다 다름"을 적는다. 유형 `blackbox` 가 맞다. 작성자의 "맞는다"에 동의한다.
- **P6**: §6이 쓰는 범위에서 틀린 곳은 없다. 의견 하나: 규칙 문장은 $\log Y_0$ 의 전개만 말하는데 §6이 쓰는 것은 canceled-anchor 전개(old leaf 재사용 계수 1을 포함한 $c_E$)다. 수학 노드 열에 `tree:extension-expansion` 이 있고 P7의 차이 칸이 "$c_E$ 는 P6의 tree 계수"라 하므로 닿기는 한다. 문장에 "anchor 인자를 상쇄한 판은 extension history의 합"을 한 구절 넣으면 P7이 가리키는 것이 분명해진다.
- **P7**: 원문 451–470과 맞는다. "고정한 $L$, tree, 제약마다 $N\to\infty$ 에서만, 오차는 균일하지 않다", "mark 깊이는 $1,\ldots,L-1$" 모두 확인했다. 두 가지: F2의 문구("anchor와 새로 붙는 replica들 사이")와 (d)의 `pert:mark-selector`.
- **L1 수 3**: 맞는다. **수 4**: 맞는다. F2와 같은 문구가 있다.

## 그 밖의 확인

- `pert:concentration` 의 물리 칸 "(작은 보정을 더하면) 볼록": 보정 $2nu^2$ 는 $O(\lambda_\nu)$ 로 score 규모와 같은 차수다. "작은"은 $N$ 에 대한 root logarithm($O(N)$)에 견준 말로 읽힌다. 유형이 `weakening` 이고 차이 칸이 상수 의존을 적으므로 지적으로 세우지 않았다.
- `pert:tree-identity` 의 물리 칸 "새 replica $k$ 개를 붙이는 모든 방법": history는 쓰지 않은 old leaf를 고르는 것도 포함한다(trees.tex 264–265). 차이 칸 (2)가 "old leaf 재사용이 $+1$"을 적으므로 `approximation` 아래에서 통과로 두었다.
- `pert:section` 의 `children` 은 정리류 여섯과 remark 하나이고 정의·약속 카드는 `uses` 에 있다. `tree:section`, `decor:section` 과 같은 처리다.
