---
id: pert:section
kind: section
title: '§6 섭동과 prescribed tree 위의 항등식'
uses: [x:pert-standing, x:pert-mark-specification, pert:parameters, pert:factor, x:pert-parameter-measure, pert:score, pert:error, x:pert-increment, x:pert-selected-limits, x:pert-test-setup, pert:palm-expression, pert:analytic-difference, x:pert-colored-extensions, x:cavity-bounded, cavity:grid, cavity:increment, cavity:negligible, cavity:factor-bounds, x:cavity-root-convention, x:cavity-root-logarithm, x:cavity-tree-sampling, model:hamiltonian, x:tree-path-kernels, x:tree-sampling, tree:multioverlap, tree:original-tilt, tree:Y-recursion, tree:insertion, x:tree-extra-variables, x:tree-extension-history, tree:extension-expansion]
provides: '§7 decorrelation (pert:selection, pert:tree-identity, \ref 없이 x:pert-colored-extensions), §8 comparison (pert:selection과 그 (i), x:pert-selected-limits, \ref 없이 x:pert-mark-specification·pert:factor·x:pert-increment의 $\underline F$ 와 $\Delta_N$). overview.tex 18, 24. 규칙 P5, P7, L1 수 3–4'
math: |
  받는 것 (§5, §3, §2). 유계·순열 불변 상호작용과 유계 장(x:cavity-bounded), 고정 깊이 $L\ge2$ 와 지수 $m_d$(cavity:grid; 증명은 $0<m_1\le m_d$, $m_L=1$ 만 씀, 작성자 읽기), cavity:increment의 reservoir와 증분의 균등 유계성, cavity:negligible $|P_N^{L,\mathbf u}-NF_N|\le(\log2)s_N$ ($\mathbf u$ 에 균등), 섭동 틀(cavity:factor-bounds, x:cavity-root-convention: 개수·type·site는 root, $\mathbf u$ 는 고정값), $P_N^{L,\mathbf u}$(x:cavity-root-logarithm), $F_N$(model:hamiltonian). §3에서 power-mean recursion과 tilted kernel(tree:original-tilt, x:tree-path-kernels), tree 표본 규칙과 multioverlap(x:tree-sampling, tree:multioverlap), insertion calculus와 그 단조성(tree:Y-recursion, tree:insertion), 추가 변수의 약속(x:tree-extra-variables), canceled-anchor 전개와 그 해석적 경계(tree:extension-expansion, x:tree-extension-history).

  내놓는 것. (1) pert:selection: 고정 $L\ge2$, $\varepsilon>0$ 마다 $N_j\uparrow\infty$ 와 결정적 $\mathbf u_j$ 가 있어 (i) $\Delta_{N_j}(\mathbf u_j)\le\underline F+2\varepsilon$, (ii) 모든 고정 type $\nu$ 에서 reservoir의 $e_{\nu,N_j}(\mathbf u_j)\to0$, (iii) reservoir의 깊이 $L$ 유한 prescribed tree 위 multioverlap 유한곱의 기대값이 수렴. (2) pert:tree-identity: 그런 모든 수열을 따라, 모든 고정 old tree $\mathcal T$, spin/marker anchor $a_*$, 유계 multioverlap 다항식 $f$, 유한 개 순서 붙은 추가 color, anchor와 추가 color들로 이루어진 집합 안의 쌍별 split 깊이의 일관된 제약 $\mathcal C$ 에 대해
  $$\sum_{E\in\mathfrak E(\mathcal T,a_*,\mathcal C)}c_E\,\mathbb E[fR_E]-\mathbb Ef\sum_{E\in\mathfrak E(\{a_*\},a_*,\mathcal C)}c_E\,\mathbb E[R_E]\longrightarrow0,$$
  오차는 고정 $L$, tree, 제약에서 $N\to\infty$ 로 사라진다. 기대값은 선택된 벡터에서의 reservoir 기대값이다(x:pert-selected-limits).
physics: |
  [[x:pert-standing]]의 유계 모형에서, [[g:reservoir|reservoir]]에 평균 $N^{3/4}$ 개의 유계 [[g:perturbation|섭동]] 인자를 넣고, 크기와 섭동 매개변수를 골라([[g:selected-sequence|선택된 수열]]) cavity [[g:increment|증분]]을 낮게 유지하면서 모든 섭동 type의 [[g:score|score]]가 [[g:concentration|집중]]하게 한다. 그 집중을 새 섭동 하나의 [[g:insertion|insertion]]에 대한 Taylor 계수 항등식으로 바꾸고, 깊이별 [[g:mark|mark]]로 갈라짐 깊이를 지정해 [[g:replica|replica]] tree 위의 [[g:tree-identity|prescribed-tree 항등식]]을 얻는다.
gap: |
  (1) 수열 선택은 존재 진술이고 매개변수 평균($\pi$)은 점을 고르는 데만 쓰인다. 결론은 고른 점에서의 [[g:root]]·path 기대값에 대한 것이다. (2) 모든 극한은 고정 $L$(과 $\varepsilon$)에서 $N\to\infty$ 이고 type, $L$, path 수에 균등하지 않다. §6 안에서는 $j$ 고정 $N\to\infty$ 뒤 $j\to\infty$ 다([[g:order-of-limits]]). (3) 항등식은 [[g:extension-history|extension history]] 위의 부호 있는 합이고, 제약은 anchor와 추가 color들로 이루어진 집합 안의 쌍별 split 깊이(추가 color끼리의 쌍 포함)만 지정하고 다른 old replica가 관여하는 쌍은 지정하지 못한다. (4) 계층 구조는 [[g:hierarchy|보조 계층]]의 구성에 들어 있고 항등식에서 유도되지 않는다. 물리적 Gibbs 측도의 [[g:physical-pure-state|물리적 pure state]] 구조나 overlap 극한값은 나오지 않는다. (5) 원문이 드는 선행 연구와의 관계(perturbations.tex 17–22)는 [[g:tree-identity]]의 물리 대응 칸에 intuition으로만 있다. 섭동 인자는 무한소가 아니라 $O(1)$ 크기이고 작은 것은 개수 밀도다.
abstraction: approximation
children: [pert:concentration, pert:selection, pert:score-identity, pert:palm, pert:analytic, pert:tree-identity, x:pert-order-of-choices]
source:
  - {file: perturbations.tex, lines: [1, 547]}
status: proposed
---

**뼈대.** 원문 12–16행의 요약 그대로: 도함수가 집중하는 섭동을 고르고, 동시에 cavity 증분을 섭동 없는 liminf보다 임의로 작은 오차 이상 넘지 않게 고른다. Poisson insertion이 집중을 Taylor 계수 항등식으로 바꾼다. 삽입된 path들 위의 독립 부호가 처방된 갈라짐 깊이를 고른다.
- §6.1 섭동 족: [[x:pert-standing]] → [[x:pert-mark-specification]] → [[pert:parameters]] → [[pert:factor]] → [[x:pert-parameter-measure]].
- §6.2 score 집중: [[pert:score]], [[pert:error]] → [[pert:concentration]] (path 요동은 2차 미분, root 요동은 Efron–Stein과 볼록성).
- §6.3 수열 하나: [[x:pert-increment]] → [[pert:selection]] → [[x:pert-selected-limits]].
- §6.4 Poisson insertion과 해석적 추출: [[x:pert-test-setup]] → [[pert:score-identity]] → [[pert:palm-expression]], [[pert:analytic-difference]] → [[pert:palm]] → [[pert:analytic]].
- §6.5 colored tree 처방: [[x:pert-colored-extensions]] → [[pert:tree-identity]] (polarization, mark selector, 조립) → [[x:pert-order-of-choices]].

**선행 연구 문단(17–24행).** 원문: "The use of concentration to obtain overlap identities has antecedents in the self-averaging argument of Ghirlanda–Guerra … Related antecedents are the stochastic-stability relations of Aizenman–Contucci and their extensions to diluted multioverlaps by Barra and De Sanctis. Panchenko's spin-distribution identities provide the cavity context. The bounded perturbation family and the identities on colored finite trees needed here are constructed and proved below." 원문은 방법의 선행 연구를 들 뿐이고, 필요한 섭동 족과 항등식은 이 절에서 만들고 증명한다고 쓴다. 그래서 이 사이트의 카드는 그 이름을 물리 진술에 쓰지 않고, 관계는 [[g:tree-identity]]의 물리 대응 칸(intuition)에만 둔다.

**두 평균.** $\pi$ 에 대한 적분이 나오는 곳은 [[pert:concentration]]과 [[pert:selection.s1]]–[[pert:selection.s2]]뿐이다. 나머지 $\mathbb E$, $\mathbb E_{\mathbf u}$, $\langle\cdot\rangle$ 은 매개변수를 고정한 root·path 기대값이고, [[pert:palm.s1]]의 Poisson add-one 항등식이 평균하는 것도 root의 Poisson 개수다.

**밖에서 받는 것** (`\ref` 위치와 `\ref` 없는 사용).

| 주는 곳 | 쓰는 것 | 원문 위치 |
|---|---|---|
| §5 [[x:cavity-bounded]] | 유계 상호작용과 장 | 4 (`\ref` 없음) |
| §5 [[cavity:grid]] | 고정 깊이 $L\ge2$, 지수 $m_d$ (증명은 $m_1>0$, $m_L=1$ 만; 작성자 읽기) | 4–5, 124, 136–138, 152, 159 (`\ref` 없음) |
| §5 [[cavity:increment]] | reservoir와 그 물리 disorder 구조; 증분의 균등 유계 $\lvert\Delta_N\rvert\le C$ | 6–8 (`\cref`), 277–279 (`\Cref`) |
| §5 [[x:cavity-tree-sampling]] | reservoir에서도 집중 논증이 적용됨(같은 내용을 6–8행이 다시 적음) | 6–8, 102 (`\ref` 없음) |
| §5 [[cavity:negligible]] | factor 경계에 의한 항별 비교의 본보기; $\liminf_N\frac1N\int P_N\,d\pi=\underline F$ | 65 (`\eqref`), 271 (`\eqref`) |
| §5 [[cavity:factor-bounds]], [[x:cavity-root-convention]] | 섭동 틀, 개수·type·site는 root, $\mathbf u$ 는 고정값 | 54–62, 67–69 (`\ref` 없음) |
| §5 [[x:cavity-root-logarithm]] | $P_N^{L,\mathbf u}$ ("Recall") | 250–252 (`\ref` 없음) |
| §2 [[model:hamiltonian]] | $F_N$ | 249 (`\ref` 없음) |
| §3 [[tree:original-tilt]], [[x:tree-path-kernels]] | backward recursion $X_{d-1}$, tilted kernel $K_d$, prefix $\mathscr F_d$, 마지막 단계 $m_L=1$ | 121–131 (`\ref` 없음) |
| §3 [[tree:insertion]], [[tree:Y-recursion]] | $Y$, (tree:density)의 $W_{\mathcal T}(A)$, anchor 인자 상쇄; 단조성으로 항별 비교와 유계 차분 | 334–335, 370 (`\ref`); 64–65, 193–194 (`\ref` 없음) |
| §3 [[x:tree-extra-variables]] | insertion 변수를 prior kernel로 덧붙임; 쓰지 않는 mark 변수의 적분 | 336–338, 195–196 (`\ref` 없음) |
| §3 [[tree:extension-expansion]] ([[x:tree-extension-history]]) | 해석적 경계; 확장 규칙과 $c_E$; 고정 차수의 유한 확장; 혼합 도함수 = 순서 붙은 규칙(추가 factorial 없음); 혼합 전개 | 391, 433, 437 (`\ref`); 403–405, 478–492, 526 (`\ref` 없음) |
| §3 [[x:tree-sampling]], [[tree:multioverlap]] | tree, split, 사영 일관성("anchor marginal is always one tilted path"), 위치와 spin 값의 구별; $R_S$, $\mathbb E$ 의 약속 | 316–321, 441–448, 302–304, 516–517 (`\ref` 없음) |
| 외부 문헌 | Efron–Stein 부등식(증명을 함께 적음); 선행 연구 GG98, AC98, BarraDeSanctis07, Pan13(증명에 쓰이지 않음) | 179–191; 17–22 |

**밖에 내주는 것.**

| 받는 곳 | 쓰는 것 | 원문 위치 |
|---|---|---|
| §5 cavity.tex 32 | "The factors needed later are specified in pert:section" → [[pert:factor]], [[x:pert-mark-specification]] (예고) | cavity.tex 32 |
| §5 cavity.tex 119–121 | "the concentration argument applies to its slightly modified interaction mean as well" → [[pert:concentration]]의 Efron–Stein 논증 (예고, `\ref` 없음) | cavity.tex 119–121 |
| §7 [[x:decor-limit-order]], [[x:decor-mesh]], decor:section | [[pert:selection]]의 수열(고정 $L$), [[pert:tree-identity]] | decorrelation.tex 4–9 |
| §7 [[decor:identity-error]] | [[pert:tree-identity]]의 오차를 유한 모임에서 최대로 | decorrelation.tex 51 |
| §7 (`\ref` 없음) | spin anchor, marker anchor, added color, 제약([[x:pert-colored-extensions]]) | decorrelation.tex 81, 265, 298–302, 529–560 |
| §8 comp:low-increments, comp:encoding | [[pert:selection]]과 그 (i); 선택된 매개변수 벡터 | comparison.tex 8–15, 20 |
| §8 (`\ref` 없음) | 고정 $L$ 의 선택된 수열([[x:pert-selected-limits]]); 보조 prior가 유한 mark 공간의 유한곱([[x:pert-mark-specification]], [[pert:factor]]) | comparison.tex 130, 243; 53–56 |
| §8 x:comp-standing, comp:low-increments (`\ref` 없음) | [[x:pert-increment]]: $\underline F$ (선택 전, 모든 크기의 liminf; perturbations.tex 249–250)와 $\Delta_N(\mathbf u)$ (252–253) | comparison.tex 11–14 |
| overview.tex | [[pert:selection]], [[pert:tree-identity]] | overview.tex 18, 24 |

[[pert:concentration]], [[pert:palm]], [[pert:analytic]]은 §5의 예고(cavity.tex 119–121, [[pert:concentration]])를 빼면 이 절 밖에서 쓰이지 않는다(규칙 P5, P7과 L1 수 3–4의 근거 노드로만 나온다).

**§7 카드와의 대조.** §7 카드가 이 절에서 기대하는 것을 원문과 맞춰 보았다.
- 수열: [[x:decor-limit-order]]는 "고정 $L$ (과 고정 $\varepsilon$)에서 pert:selection이 주는 $N_j\uparrow\infty$, 결정적 $\mathbf u_j$ 의 수열"이고 [[pert:tree-identity]]는 "along every sequence from pert:selection"이다. 맞는다. 수열이 $L$ 마다 다를 수 있다는 것도 [[x:pert-selected-limits]]와 같다.
- 양화사: §7이 쓰는 사례(old tree, spin/marker anchor, 유계 multioverlap 다항식 $f$, 유한 개 color, 제약)는 모두 정리의 "every fixed …" 범위 안이다. [[decor:overlap-concentration.s1]]($k=0$, spin anchor, $f=R_S$; anchor 자신도 old replica라 $f$ 에 쓸 수 있다), [[decor:conditional-concentration.s2.s1]]($k=1$, split 깊이 $d$), [[decor:conditional-concentration.s3.s1]](두 사본 old tree, $S^+$ 두 사본 제약), [[decor:overlap-concentration.s2.s1]](marker anchor, $S$ 사본 전체가 anchor와 $e-1$ 에서 갈라짐)의 제약은 모두 anchor와 추가 color들만 관여하는 쌍별 split 깊이를 처방한다. 그 가운데 두 사본 제약과 $S$ 사본 제약은 추가 color끼리의 split 깊이도 처방한다(decorrelation.tex 298–302, 540–541). 원문 제약(perturbations.tex 434–435 "pairwise split depths, involving only the added colors and the anchor", 495–496 "$a,b\in\{0,\ldots,k\}$")이 이 쌍을 포함하므로 허용된다. $k=0$ 에서 두 번째 합의 $\mathbb E[R_{\{a_*\}}]$ 는 anchor 하나 tree의 값이고 사영 일관성으로 $\mathbb ER_S$ 와 같다.
- 오차항: 정리는 고정 $L$, tree, 제약에서 $\to0$ 만 준다(율 없음). §7은 고정 $L$ 의 $o_N(1)$ 과 유한 모임의 최대([[decor:identity-error]])만 쓴다. 맞는다.
- 기대값의 뜻: §7의 $\operatorname{Var}$ 는 root를 포함하고 매개변수는 고정이다. §6의 $\mathbb E$ 는 선택된 벡터에서의 reservoir root·tree 기대값이다. 맞는다.
- 수열 선택의 뜻: §7은 pert:selection의 (ii), (iii)을 직접 쓰지 않고 항등식만 쓴다. [[x:decor-mesh]]는 pert:selection에서 "$L\ge2$"만 받는다(진술의 "For every fixed $L\ge2$"). 맞는다.
내용의 어긋남은 찾지 못했다. 검토 2 대응에서 §7 카드 네 장([[decor:overlap-concentration.s1]], [[decor:overlap-concentration.s2.s1]], [[decor:conditional-concentration.s2.s1]], [[decor:conditional-concentration.s3.s1]])의 `uses` 에 [[x:pert-colored-extensions]]를 더했다. 그 본문이 spin/marker anchor, added color, 제약의 어휘를 쓰고 그 정의는 이 카드에만 있다.

**§3 카드와의 대조.** tree:section의 내주는 것 표(§6 행)는 [[tree:insertion]]과 (tree:density), [[x:tree-extra-variables]], [[tree:extension-expansion]]의 해석적 경계와 $c_E$, [[x:tree-extension-history]](334–338, 370, 391, 433), 단조성(64–65)을 적는다. 실제 사용과 내용은 맞는다. 빠져 있던 사용, 곧 [[x:tree-sampling]]의 사영 일관성(321)과 위치/값 구별(516–517), [[tree:multioverlap]]($f$, $R_E$; 316–317, 441–448), [[tree:original-tilt]]·[[x:tree-path-kernels]]의 recursion 미분(121–132), [[tree:Y-recursion]](333–334의 "insertion recursion"), 단조성과 extra-variables의 둘째 사용(193–196), [[tree:extension-expansion]]의 `\ref` 없는 사용(403–405, 478–492, 526)은 검토 2 대응에서 그 표에 행을 더했다. 또 [[tree:extension-expansion]]의 $H$ 는 "old tree 위 변수의 유계 함수"인데 §6의 $fg_0^{a_*}S_0^{a_*}$ 는 insertion 변수(anchor path의 mark, 새 site)를 포함한다. [[x:tree-extra-variables]]로 넓힌 tree 위에서는 문제가 없다고 읽었다(작성자 읽기).
