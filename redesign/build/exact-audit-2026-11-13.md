# `abstraction: exact` 판정과 이전 변경 검증 (2026-11-13)

대상: 중단된 이전 작업의 변경 전부(`git diff fada529 bbc603b -- cards layers SCHEMA.md`: 카드 21장, `layers/glossary.md`, `layers/rules.md`, `SCHEMA.md` 한 줄)와 지금 `exact`인 카드 76장 전부. 원문 줄은 `source/sections/*.tex`를 직접 열어 대조했다. 식 번호 (2.x), (4.x), (5.x)는 `main.tex`의 `\numberwithin{equation}{section}`과 절 순서(introduction §1, model §2, overview는 §2의 subsection, trees §3, upper §4, cavity §5)로 확인했다.

손대지 않은 것: 규칙 P6 행, L1 수 4, `tools/`, `site/`, `build/check-report.md`. `status`는 모두 `proposed` 그대로다.

## 요약

- **이전 변경**: 덩어리 39개(카드 22, 용어집 15, 규칙 표 2, SCHEMA 1)를 모두 **채택**했다. 되돌린 것 0, 고쳐서 채택한 것 2(`tree:extension-expansion`, `decor:depth-continuity.s1`의 문구 보완).
- **유형 변경**: 이전 작업의 `exact → weakening` 3장(`cavity:increment`, `tree:extension-expansion`, `x:decor-topology`)이 맞다고 판정했다. 이번에 더 바꾼 유형은 없다. `approximation`으로 내려야 할 카드는 찾지 못했다(물리 문장이 증명보다 많이 말하는 곳 0).
- **이번에 고친 카드 4장**(물리 문장만, 수식·`math` 불변): `comp:encoding.s4`, `tree:extension-expansion`, `x:tree-differentiation-rule`, `decor:depth-continuity.s1`.
- 이전 작업과 이번 작업을 합쳐 바뀐 카드는 23장(이전 21장 + 새로 바뀐 2장 `comp:encoding.s4`, `x:tree-differentiation-rule`)이다.
- **exact 76장 재훑기**: 76장 모두 원문과 대조했다. 결과는 exact 유지 76(이 가운데 이전 변경을 채택한 문장 수정 17, 이번 문장 수정 3).
- 맡긴 일 1–5: 1(의심 8장)·3(SCHEMA)·4(`tree:section` §8 행)·5(P7·P11 차이 칸, 용어집 정의 위치 칸)는 이전 변경으로 끝나 있었고 검증만 했다. 2(전체 재훑기)는 이번에 76장을 모두 끝냈다.
- 검사: `python3 tools/check.py --out /tmp/exact-check.md` → **오류 0**. 지금 도구는 검사 10종(다른 에이전트가 `대칭`을 더했다)을 돌리고, 9종은 통과(경고 0), `대칭`은 경고 48(오류 0)이다. 아래 "검사" 절 참조.

## 판정 기준

- `exact`: `physics`가 `math`의 내용을 빠짐없이 물리 언어로 다시 쓴 것. 정의·가정 카드에서는 가정의 성분을 빠뜨리지 않아야 한다.
- `weakening`: `physics`가 `math`의 일부(딸린 진술, 균일성, 가정의 세부)를 말하지 않되 말한 것은 모두 참.
- `approximation`: `physics`가 증명된 것보다 많이 말함. 이번 재훑기에서는 해당 0.
- 이전 작업은 빠진 성분을 (a) `physics`에 넣고 `exact`로 두거나(`model:factorization`, `reduction:stability`, `main:theorem.s4`, `tree:log-expansion`, `model:integrability`) (b) `gap`에 적고 `weakening`으로 내렸다(`cavity:increment`, `tree:extension-expansion`, `x:decor-topology`). 둘 다 원칙에 맞으므로 각 카드에서 바꾸지 않았다. 어느 쪽을 기본으로 할지는 아래 "넘기는 것" 3.

## 표 1. 이전 변경 판정

| 카드/파일 | 변경 요지 | 판정 | 원문 줄 | 이유 |
|---|---|---|---|---|
| `cavity:increment` | `gap` 앞에 "(1)과 (3)을 말하지 않는다" 추가, exact→weakening | 채택 | cavity.tex 43–69 | 물리 문장이 증분 자체의 균일 유계(44–45), 오차의 $L,\mathbf u$ 균일성(55), $\rho_N$(47–49)을 말하지 않는다. 말한 것(site−bond 차 + $\log2$ + $o(1)$, Poisson$(\alpha p)$, Poisson$(\alpha(p-1))$)은 모두 참이다 |
| `comp:encoding` | `physics`에 고정 $N,L$, 선택된 매개변수, root disorder를 평균한 결정적 법칙, label 독립 추가 | 채택 | comparison.tex 19–25 | lemma 진술의 성분을 물리 문장에 옮긴 것. exact 유지 |
| `comp:patterns` | `physics`에 tree 고정, 독립 균일 label, 절댓값 1 이하, 식 (comp:pattern-error), 새 삽입 disorder 의존 허용 추가. "모든 multioverlap"을 "그 tree의 multioverlap"으로 | 채택 | comparison.tex 87–97 | 진술과 일치. "모든"을 고친 것은 정확해졌다(합은 그 tree의 부분집합 $S$ 위) |
| `decor:depth-continuity.s1` | `physics`에 평가 깊이 연속성 $\mathcal A_{L,\eta}\mathbb E\lVert\mu_{d+1,S}-\mu_{d,S}\rVert_N^2\le1/L$ 추가 | 수정 후 채택 | decorrelation.tex 30–35, 44–45, 168–177 | 내용은 맞다(정규화 $L^{-a}$, 쓰지 않는 좌표는 $L$로 상쇄). 문구 "평가 깊이 $d$까지 넣어"를 "initial stem 위를 움직이는 평가 깊이 $d$도 평균 좌표에 넣어"로 고쳤다(156–162) |
| `main:theorem.s2` | "큰 coupling과 장을 자른다"를 "상수 이동한 $\widehat\theta$의 값과 장을 $[-K,K]$로 자른다"로, $D_K,d_K\to0$ 추가 | 채택 | reduction.tex 61–69 | 원문은 $\widehat\theta$의 각 값과 $h$를 자른다. 옛 문구("큰 coupling")는 대상을 흐렸다 |
| `main:theorem.s4` | `physics`에 limsup·liminf를 따로 적고 "그래서 극한이 존재한다"로 | 채택 | reduction.tex 84–86, upper.tex 11–14 | 극한의 존재를 가정하지 않고 두 부등식에서 끌어낸다. 의심 6 해소. exact 유지 |
| `model:factorization` | `physics`에 엄격한 곱 한계와 독립 구조, `gap`에 그 쓰임 추가 | 채택 | model.tex 25–34, 38–41; upper.tex 24–34; reduction.tex 56–58 | 의심 1 해소. 가정의 성분이 모두 물리 문장에 들어 exact가 맞다. `gap`의 두 쓰임 인용 줄 확인 |
| `model:integrability` | `physics`에 짝수 $p\ge2$, $\alpha>0$, 식 (2.1) 명시 | 채택 | model.tex 3–8 | 의심 7 해소. exact 유지 |
| `models:ground.s1` | `physics`에 "1차 moment 가정으로 $g_N$ 유한·균일 유계" 추가 | 채택 | consequences.tex 105–106 | 원문 문장 그대로 |
| `reduction:stability` | `physics`에 (2.1) 가정, $D,d$ 정의, 두 상수 $\alpha D+d$, $\alpha(2p-1)D+d$, 균일성 범위, 적분 가능한 $c$ 추가. `gap`에 (2.1)의 역할 | 채택 | reduction.tex 9–26 | 의심 5 해소. 진술 전체가 물리 문장에 있다 |
| `tree:Y-recursion` | `physics`에 "양의 path 함수, root 조건부로 위로 유계이고 0에서 떨어짐" | 채택 | trees.tex 67–74 | 정의의 전제 |
| `tree:extension-expansion` | `physics`에 $H$와 $\boldsymbol t=0$, `gap`에 빠진 딸린 진술 넷, exact→weakening | 수정 후 채택 | trees.tex 259–296 | 의심 3 해소. 빠진 것(색 순서 무관, $k!$, 해석적 경계의 균등성, 빈 확장 무게 1)이 `gap`에 정확히 적혔다. 재사용 선택지 (i)가 "anchor가 아닌" 옛 leaf(264)라는 한정이 물리 문장에 없어 이번에 넣었다 |
| `tree:first-variation` | `physics`에 "$D_j$ 유계 실수, $A_{\boldsymbol t}$가 균등하게 양인 실수 근방" | 채택 | trees.tex 142–150 | 원문 조건 그대로 |
| `tree:insertion` | `physics`에 tilted kernel·말단 Gibbs kernel 전제, $A$의 유계 가정, 단조·동차성 추가 | 채택 | trees.tex 84–111 | lemma의 세 번째 문단(107–110)이 빠져 있었다. 이제 진술 전체 |
| `tree:log-expansion` | `physics`에 수렴 영역과 꼬리 한계 $\sum_{k>K}c^k/k$ | 채택 | trees.tex 224–239 | 의심 4 해소. exact 유지 |
| `tree:original-tilt` | `provides`에 §8 `comp:encoding`·`comp:encoding.s1`의 사용 추가 | 채택 | comparison.tex 29–30, 36, 39–40 | "tilted reservoir auxiliary kernels", "leaf Gibbs expectation", "terminal spin transition at depth $L$" 확인 |
| `tree:regular-shapes` | `physics`에 균등 격자, $0<\eta<1/2$, $C_k$가 $L,\eta$에 무관 | 채택 | trees.tex 460–475 | 원문 그대로 |
| `tree:section` (`provides`) | §8 목록 끝에 `tree:original-tilt`, `x:tree-path-kernels` | 채택 | 아래 표 행과 같음 | 맡긴 일 4 |
| `tree:section` (표 §8 `\ref` 없음 행) | 두 카드의 쓰임과 근거 줄 추가 | 채택 | comparison.tex 29–30, 36, 39–40; 30–32, 39–40, 44–51; trees.tex 23–27 | `$\mathscr G_d$`(30–31), 깊이 $r=L-1$의 $x$(32, 39), $\eta_d$의 깊이(44–51) 확인. 맡긴 일 4 끝 |
| `upper:remainder` | `physics`에 $\lambda<1$ 정규화, "$n$차 계수는", 절대수렴과 $\lambda\uparrow1$ | 채택 | upper.tex 76–94, 96–126 | 원문 순서 그대로. (4.1)=`upper:derivative`, (4.3)=`upper:remainder` 번호 확인 |
| `x:decor-topology` | `gap`에 "정의 낱말은 `math`에만" 추가, exact→weakening | 채택 | decorrelation.tex 18–28 | 물리 문장은 대상의 그림만 주고 깊이 배정의 엄격 증가 조건, $b(S)$, regular 등은 말하지 않는다. 말한 것은 참 |
| `x:tree-path-kernels` | `provides`에 §8 `comp:encoding`·`.s1`의 사용 | 채택 | comparison.tex 30–32, 39–40, 44–51 | 위와 같음 |
| `SCHEMA.md` 단면 문서 절 | "역할 표(R-ID)를 가리킨다" → "용어집 항목(`[[g:slug]]`, `layers/glossary.md`)을 가리킨다" | 채택 | — | 같은 문서 "용어집" 절과 어긋나던 문장. 맡긴 일 3 끝 |
| `glossary` `g:hypergraph` 역할 | `cavity:reservoir-mean` → `cavity:increment`의 (5.4) | 채택 | cavity.tex 47–49 | (5.4) 번호 확인 |
| `glossary` 165행 정의 위치 | `main:formula` → `main:theorem`의 (2.13) | 채택 | model.tex 133 | |
| `glossary` 266행 정의 위치 | `cavity:reservoir-mean` → `cavity:increment`(5.4, 47–49) | 채택 | cavity.tex 47–49 | |
| `glossary` 288행 정의 위치 | `cavity:identity` → `cavity:increment`(5.5, 51–54) | 채택 | cavity.tex 51–54 | |
| `glossary` 295행 정의 위치 | site·bond insertion 라벨 → `cavity:increment`의 (5.6), (5.7), (5.5) | 채택 | cavity.tex 51–66 | |
| `glossary` 319행 정의 위치 | `tree:updated-kernel`, `tree:density` → 담는 카드와 줄 | 채택 | trees.tex 76–80, 98–104 | |
| `glossary` 326행 정의 위치 | `tree:K` → `tree:reference-total`의 식 | 채택 | trees.tex 349–352 | |
| `glossary` 382행 역할 | `cavity:identity` → `cavity:increment`의 (5.5) | 채택 | cavity.tex 51–54 | |
| `glossary` 391행 정의 위치 | J 식 라벨 셋 → `decor:conditional-concentration.s3.s2`(332–344), `.s3.s3`(345–360) | 채택 | decorrelation.tex 335, 343, 352 | 두 카드의 `source`가 세 라벨 줄을 덮는다 |
| `glossary` 460행 정의 위치 | 두 부등식 라벨 → `decor:contractions`의 식 | 채택 | decorrelation.tex 115, 123 | |
| `glossary` 467행 정의 위치 | `decor:martingale-energy` → `decor:depth-continuity.s1`의 식 | 채택 | decorrelation.tex 174 | |
| `glossary` 484–485행 | `comp:single-label-moments` → `comp:encoding.s4`의 식(75–79) | 채택 | comparison.tex 75–79 | |
| `glossary` 496행 기호 | `comp:pattern-error` → `comp:patterns`의 식 | 채택 | comparison.tex 92–94 | |
| `glossary` 509행 정의 위치 | `reduction:shift` → `reduction:stability`의 식(20–25) | 채택 | reduction.tex 20–25 | |
| `glossary` 523행 정의 위치 | 두 안정성 라벨 → `reduction:stability`의 식(14–18) | 채택 | reduction.tex 14–18 | |
| `rules.md` P7 차이 | `cavity:identity` → `cavity:increment`의 (5.5) | 채택 | cavity.tex 51–54 | 규칙 문장 불변. 맡긴 일 5 |
| `rules.md` P11 차이 | `comp:pattern-error` → `comp:patterns`의 식, `tree:irregular-probability` → `tree:regular-shapes`의 식 | 채택 | comparison.tex 92–94; trees.tex 472–475 | 규칙 문장 불변. 맡긴 일 5 |

의심 8 `x:cavity-tree-sampling`은 파일이 바뀌지 않았다. 이번에 판정했다: 물리 문장의 "뒤의 집중 논증이 그대로 적용된다"는 원문 문장(cavity.tex 119–121 "Thus the concentration argument applies to its slightly modified interaction mean as well")이고 perturbations.tex 102 "The assertion holds for the reservoir as well as for the original system"에서 증명된다. `gap`이 증명 위치를 적고 있으므로 exact 유지.

## 표 2. `exact` 76장 재훑기

"유지"는 원문과 대조해 고칠 것이 없었다는 뜻이다. "유지(이전 수정 채택)"는 표 1의 변경이 들어간 상태로 유지한다는 뜻이다. "문장 수정"은 이번에 고친 것이다.

| 카드 | 결과 | 근거 |
|---|---|---|
| `cavity:factor-bounds` | 유지 | cavity.tex 20–27. 평균 $c_\nu N^{3/4}$, 보조 변수, $[1/2,3/2]$ 모두 있음 |
| `cavity:grid` | 유지 | 16–19. 고정 격자와 $L=r+1$ |
| `cavity:increment.s1` | 유지 | 71–85. 세 평균과 $\alpha N-\rho_N$; 음 아님(85)은 `gap` |
| `cavity:increment.s3` | 유지 | 100–107. 비용 $O(N^{-1/4})$, $2A_{\rm s}$, $A_{\rm b}$, $\log2$ |
| `comp:bounded-lower` | 유지 | comparison.tex 225–246. liminf 꼴, 극한 존재를 주장하지 않음 |
| `comp:encoding` | 유지(이전 수정 채택) | 19–25 |
| `comp:encoding.s1` | 유지 | 27–43. 한 site의 one-site 법칙, 조건부 독립 |
| `comp:encoding.s3` | 유지 | 58–72. 자식 법칙 $\eta_{d+1}$이 $\eta_d$에서 독립 |
| `comp:encoding.s4` | **문장 수정** | 80–82 "independent of the new physical disorder in the cavity insertions"가 물리 문장에 없었다. `comp:patterns`(95–96, 120)가 이 독립을 쓴다. 한 구절 추가 |
| `comp:insertion-comparison.s1` | 유지 | 170–196. $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$, edge 인수분해 |
| `comp:insertion-comparison.s1.s3` | 유지 | 181–196 |
| `comp:low-increments` | 유지 | 11–15. 상한뿐, 극한 주장 없음 |
| `comp:patterns` | 유지(이전 수정 채택) | 87–97 |
| `decor:covariance-definition` | 유지 | decorrelation.tex 94–104. singleton 예의 식 확인 |
| `decor:depth-continuity.s1` | 유지(이전 수정 채택) + **문장 수정** | 표 1 |
| `main:theorem` | 유지 | model.tex 130–136. "Ising spin glass"라는 이름은 원문 도입부(introduction.tex 3)의 틀과 같다. 넘기는 것 4 |
| `main:theorem.s1` | 유지 | reduction.tex 45–59 |
| `main:theorem.s2` | 유지(이전 수정 채택) | 61–69 |
| `main:theorem.s3` | 유지 | 70–84 |
| `main:theorem.s4` | 유지(이전 수정 채택) | 84–86 |
| `model:chain` | 유지 | model.tex 68–81. $r=1$의 분포의 분포 |
| `model:edge` | 유지 | 55–58 |
| `model:factorization` | 유지(이전 수정 채택) | 25–34 |
| `model:hamiltonian` | 유지 | 9–23. 이름 문제는 `main:theorem`과 같음 |
| `model:integrability` | 유지(이전 수정 채택) | 3–8 |
| `model:site-message` | 유지 | 59–64 |
| `model:ve` | 유지 | 82–89 |
| `model:vs` | 유지 | 82–87 |
| `models:ground` | 유지 | consequences.tex 86–101. $f(\beta)\in[-g-\log2/\beta,-g]$는 $I(\beta)/\beta\in[g,g+\log2/\beta]$와 같음 |
| `models:ground.s1` | 유지(이전 수정 채택) | 103–111 |
| `models:ground.s2` | 유지 | 112–119 |
| `models:ground.s3` | 유지 | 120–123 |
| `models:ground.s4` | 유지 | 123–124 |
| `models:sat` | 유지 | 36–49. 위반 조건 $\sigma=\varepsilon$ 확인 |
| `models:sat.s1` | 유지 | 51–58 |
| `models:sat.s2` | 유지 | 59–62 |
| `models:sat.s3` | 유지 | 62–64 |
| `models:section` | 유지 | 1–138 |
| `models:spin` | 유지 | 10–22 |
| `models:spin.s1` | 유지 | 24–30 |
| `models:spin.s2` | 유지 | 30–31 |
| `models:spin.s3` | 유지 | 31–34 |
| `pert:error` | 유지 | perturbations.tex 83–93. $\mathbf u$ 고정, 평균하지 않음 |
| `pert:score` | 유지 | 75–82. $\partial_u\log\psi=g_0S_0/\psi$ |
| `reduction:section` | 유지 | reduction.tex 1–87 |
| `reduction:stability` | 유지(이전 수정 채택) | 9–26 |
| `tree:Q-rule` | 유지 | trees.tex 209–222 |
| `tree:Y-recursion` | 유지(이전 수정 채택) | 67–82 |
| `tree:first-variation` | 유지(이전 수정 채택) | 142–154 |
| `tree:insertion` | 유지(이전 수정 채택) | 84–111 |
| `tree:log-expansion` | 유지(이전 수정 채택) | 224–239. $L=1$의 $\langle D\rangle^k$ 확인 |
| `tree:multioverlap` | 유지 | 41–49. $\mathbf u$는 root가 아님(`gap`) |
| `tree:original-tilt` | 유지(이전 `provides` 보충 채택) | 51–65 |
| `tree:reference-total` | 유지 | 337–386. 재사용과 fresh 분기의 상쇄(367–375) |
| `tree:regular-shapes` | 유지(이전 수정 채택) | 469–484 |
| `upper:bound` | 유지 | upper.tex 11–15. 모든 $N$, 모든 시행 법칙 |
| `upper:bound.s1` | 유지 | 17–34 |
| `upper:bound.s2` | 유지 | 36–49 |
| `upper:derivative` | 유지 | 58–61. 기대값 부등식의 물리 문장 부호 확인 |
| `upper:derivative.s1` | 유지 | 62–68 |
| `upper:remainder` | 유지(이전 수정 채택) | 96–126 |
| `x:cavity-bounded` | 유지 | cavity.tex 11–14 |
| `x:cavity-root-convention` | 유지 | 28–32. $\mathbf u$ 고정 |
| `x:cavity-tree-sampling` | 유지 | 117–121, perturbations.tex 102. 의심 8, 위 참조 |
| `x:cons-energy-score` | 유지 | consequences.tex 66–84. $-H_N=\beta\mathcal E_N$ |
| `x:cons-ground-scope` | 유지 | 127–129 |
| `x:cons-standard-examples` | 유지 | 4–8 |
| `x:decor-mesh` | 유지 | decorrelation.tex 4 |
| `x:model-depth-zero` | 유지 | model.tex 118–120 |
| `x:model-hypotheses` | 유지 | 3–8, 25–38, 130–131. 가정의 성분은 `g:factorization`과 `model:factorization`이 가리킨다 |
| `x:model-message` | 유지 | 46–54 |
| `x:model-moment-finiteness` | 유지 | 38–41 |
| `x:model-theorem-scope` | 유지 | 138–140, introduction.tex 75–77 |
| `x:tree-differentiation-rule` | **문장 수정** | trees.tex 142–145, 178–202. "섭동 매개변수로 미분"을 "insertion $A_{\boldsymbol t}=1+\sum_jt_jD_j$의 매개변수 $t_j$로 미분"으로. 고정값인 섭동 매개변수 $\mathbf u$와 헷갈리지 않게 |
| `x:tree-path-kernels` | 유지(이전 `provides` 보충 채택) | 14–27 |
| `x:tree-sampling` | 유지 | 29–39 |

`weakening`으로 내린 3장(`cavity:increment`, `tree:extension-expansion`, `x:decor-topology`)은 표 1에 있다.

## 규칙 표·용어집·SCHEMA 변경 목록

- `layers/rules.md`: P7 차이 칸 1곳, P11 차이 칸 2곳(이전 변경, 채택). 규칙 문장(물리 규칙 열)은 바뀌지 않았다. P6 행 불변. 이번 추가 변경 없음.
- `layers/glossary.md`: 15개 줄(이전 변경, 채택). 정의 위치 칸의 카드 없는 식 라벨은 이제 0이다. 이번 추가 변경 없음.
- `SCHEMA.md` "단면 문서" 절 한 줄(이전 변경, 채택). 이번 추가 변경 없음.

## 검사

`python3 tools/check.py --out /tmp/exact-check.md`(카드 244장, 섹션 10개 파일), 이번 수정 뒤에 실행:

| 검사 | 결과 |
|---|---|
| 형식 (머리말) | 통과, 오류 0 |
| 정초 | 통과, 오류 0 |
| 포함 | 통과, 오류 0 |
| 의존 | 통과, 오류 0 |
| 대칭 | 경고 48, 오류 0 |
| 연결 | 통과, 오류 0 |
| 순환 | 통과, 오류 0 |
| 사전 | 통과, 오류 0 |
| 단면 | 통과, 오류 0 |
| 용어 | 통과, 오류 0 |

원래의 9종은 오류 0·경고 0이다. `대칭`은 도구를 고치는 다른 에이전트가 새로 더한 검사다(provides↔uses 맞대응). 경고 48건 가운데 이번 범위의 카드는 `tree:original-tilt`(`pert:score`가 uses에 넣지만 provides에 없음)와 `x:tree-path-kernels`(`x:pert-mark-specification`, `model:chain`과의 대응) 둘이다. 이전 변경이 `comp:encoding` 쪽 대응을 채웠으므로 그 경고는 없다. 남은 것은 이번 지시의 범위 밖이라 고치지 않았다.

## 조율 세션에 넘기는 것

1. **사용자 판단 대기(손대지 않음)**: P6 행, L1 수 4.
2. **범위 밖에 남은 식 라벨**: 규칙 표 아래 "규칙으로 못 옮긴 것" 절(rules.md 33–40행)에 카드 없는 식 라벨 약 30개(`decor:J-definition`, `tree:density`, `pert:second-derivative` 등). 용어집의 정의 위치가 아닌 칸에 4곳: 249행 역할(`tree:irregular-probability`), 328행 쓰지 않는 뜻(`tree:K`), 413행 역할(`decor:three-copy-bound`), 420행 역할(`decor:V-definition`). 같은 방식("카드 ID의 식 (라벨)")으로 바꿀지 정해야 한다.
3. **빠진 성분을 처리하는 방식의 기본값**: 물리 문장에 넣고 `exact`로 둘지(5장), `gap`에 적고 `weakening`으로 내릴지(3장)는 카드마다 다르다. 둘 다 원칙에 맞지만 독자에게는 유형의 뜻이 달라 보인다. 하나로 정할지는 사용자가 정한다.
4. **확신이 낮은 것**: `main:theorem`과 `model:hamiltonian`의 물리 문장은 모형을 "Ising spin glass"라고 부른다. 원문 도입부(introduction.tex 3, 26–28)는 "diluted spin glass"라는 틀로 시작하지만 정리의 대상은 "even-arity Ising model class with factorized interactions"이고 강자성 등도 포함할 수 있다. 참을 잃는 문장은 아니라 고치지 않았다. "짝수 $p$체 희석 Ising 모형"으로 바꿀지 정한다.
5. 이번 4장 수정과 이전 21장 변경은 작성자와 다른 모델이 한 번 대조했을 뿐이다. 수정본 재검토의 범위(HANDOFF B-5)에 넣을지 정한다.
