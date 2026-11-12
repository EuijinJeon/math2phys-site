---
id: comp:section
kind: section
title: '§8 독립 계층 message와 cavity 비교'
uses: [pert:selection, x:pert-selected-limits, x:pert-increment, x:pert-mark-specification, pert:factor, x:cavity-bounded, cavity:grid, cavity:increment, cavity:increment.s4, x:cavity-tree-sampling, x:tree-path-kernels, x:tree-sampling, tree:multioverlap, tree:original-tilt, x:tree-extra-variables, tree:Y-recursion, tree:insertion, tree:log-expansion, tree:Q-rule, tree:regular-shapes, tree:averaging-remark, x:tree-regular-shape, decor:overlap-concentration, decor:average-definition, x:decor-eta-regular, x:decor-topology, x:decor-spin-product, x:decor-limit-order, model:hamiltonian, model:chain, x:model-message, model:site-message, model:edge, model:vs, model:ve, model:power-means, model:functional, x:model-depth-zero, model:trial-bounds]
provides: '§9와 주정리: comp:bounded-lower (reduction.tex 4; main:theorem.s2, s3 = reduction.tex 64, 76). 규칙 P10, P11, L1 수 6'
math: |
  받는 것. x:cavity-bounded의 유계·순열 불변 모형, $m_d=d/L$ (cavity:grid), 고정 $\varepsilon$ 과 깊이마다 pert:selection의 선택된 수열과 그 (i) (x:comp-standing, comp:low-increments), cavity:increment의 reservoir·삽입 $A_{\rm s},A_{\rm b}$·(5.5)·$\lvert\log Y_0\rvert$ 상계, §3의 recursion과 log 전개와 $Q_k$ 의 깊이 분포, §7의 깊이 평균 multioverlap 집중, §2의 시행 사슬·$V_{\rm s}$·$V_{\rm e}$·$T_d$·$\mathcal B_r$·(2.12).

  내놓는 것. 모든 bounded 순열 불변 상호작용 법칙과 bounded 장 법칙에서
  $$\liminf_{N\to\infty}F_N\ge\inf_{r\ge0}\Phi_r\qquad\text{(comp:bounded-lower)}.$$
  중간 결과: 부호화 $\zeta_{L,N}\in\mathcal M_L$ 과 (comp:single-label-moments) $\mathbb E\prod_{a\in S}\tau^a=\mathbb ER_S$ (comp:encoding), pattern 비교 (comp:pattern-error) (comp:patterns), (comp:shape-error), 그리고 $\lim_L\limsup_N\lvert\Delta_N^{L,\mathbf u_{L,N}}-\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\rvert=0$ (comp:insertion-comparison).
physics: |
  cavity [[g:reservoir|reservoir]]에서 무작위 site 하나의 계층 [[g:message|cavity field]] 법칙을 시행 [[g:order-parameter|order parameter]]로 부호화하고([[g:encoded-law]]), [[g:site-bond-insertion|site·bond 삽입]]의 이웃 spin을 그 독립 사본으로 바꾼다([[g:independent-copies]]). 바꾼 삽입이 정확히 시행 [[g:functional|functional]]이고, 바꾸는 비용은 모든 [[g:multioverlap|multioverlap]]의 [[g:concentration|집중]]이 없앤다. 낮은 [[g:increment|증분]]의 [[g:selected-sequence|선택된 수열]]과 합치면 pressure의 하한이 시행값의 inf가 된다.
gap: |
  (1) [[g:order-of-limits|극한 순서]]: 고정 $\varepsilon$, 고정 $L$ 의 선택된 수열 위 $\limsup_N$, 그다음 $L\to\infty$, 마지막 $\varepsilon\downarrow0$. shape error의 $\eta$(안쪽 명제 안에서 $L\to\infty$ 뒤에 $\eta\downarrow0$), 개수 절단 $M$, 전개 차수 $q$ 는 안쪽 명제에서 이미 소진되어 조립에는 $\eta$, $M$, $q$ 없는 진술로 들어온다. (2) 이웃 cavity field의 독립은 가정이 아니라 균일 site 표본과 tree 평균 집중에서 증명된다. 국소 tree 구조나 거리 감쇠는 쓰지 않는다. (3) "계층"은 섭동 [[g:mark|mark]]로 만든 [[g:hierarchy|보조 계층]]이고 Parisi parameter는 [[g:grid|균등 격자]]로 고정된다. 보조 계층을 [[g:physical-pure-state|물리적 pure state]]의 계층으로, $\zeta_{L,N}$ 을 계의 물리적 order parameter로 읽는 것은 증명되지 않는다. (4) 유계·순열 불변 상호작용에 한한다. (5) 하한만 준다.
abstraction: approximation
children: [x:comp-standing, comp:low-increments, comp:encoding, comp:patterns, comp:shape-error, comp:insertion-comparison, comp:bounded-lower]
source:
  - {file: comparison.tex, lines: [1, 246]}
status: proposed
---

**뼈대.** 원문 4–6행의 세 걸음 그대로: (a) reservoir의 one-site branching law 전체를 부호화한다, (b) multioverlap 집중으로 site들을 떼어 낸다, (c) 삽입 logarithm을 비교한다.
- 서두: [[x:comp-standing]] → [[comp:low-increments]].
- §8.1 부호화: [[comp:encoding]] (s1 균일 site와 $x$, s2 거꾸로 쌓은 측도, s3 branching 확인, s4 (comp:single-label-moments)).
- §8.2 pattern: [[comp:patterns]] (s1 $\pi$ 와 $\bar\pi$, s2 telescoping) → [[comp:shape-error]] ([[comp:shape-error-bound]]의 s1–s3, 그리고 [[comp:shape-error.s2]]의 극한).
- §8.3 비교: [[comp:insertion-comparison]] (s1 trial 항등식 s1.s1–s1.s3, s2 절단과 정규화, s3 차수별 비교, s4 꼬리와 조립) → [[comp:bounded-lower]] (s1 고정 $L$, s2 $L\to\infty$, $\varepsilon\downarrow0$).

**밖에서 받는 것** (`\ref` 위치와 `\ref` 없는 사용).

| 주는 곳 | 쓰는 것 | 원문 위치 |
|---|---|---|
| §6 [[pert:selection]] | 깊이마다의 수열과 결정적 매개변수, (i) | 8–9 (`\cref`), 12–15 |
| §6 [[x:pert-increment]], [[x:pert-selected-limits]] | $\underline F$ (모든 크기의 liminf), $\Delta_N$; 안쪽 극한은 고정 $L$ 의 수열, 기대값은 선택된 벡터에서 | 11–12; 20, 130, 243 (`\ref` 없음) |
| §6 [[x:pert-mark-specification]], [[pert:factor]] | 보조 prior가 실현된 root마다 유한 mark 공간의 유한곱 | 53–56 (`\ref` 없음) |
| §5 [[x:cavity-bounded]] | $B(\theta)\le B$, $\lvert h\rvert\le H$, 순열 불변 | 200, 215–216, 226 (`\ref` 없음) |
| §5 [[cavity:grid]] | $m_d=d/L$ 이므로 $\mathbf m^{(L)}$, $Q_k$ 의 깊이 분포 | 123, 162 (`\ref` 없음) |
| §5 [[cavity:increment]] | reservoir root disorder, 삽입 $A_{\rm s},A_{\rm b}$ 와 그 독립 균일 index, (5.5) (`cavity:identity`) | 20–21, 82, 171 (`\cref`), 195, 222 (`\eqref`) |
| §5 [[cavity:increment.s4]] | $\lvert\log Y_{0,\rm s}\rvert\le H+BK_{\rm s}$, $\lvert\log Y_{0,\rm b}\rvert\le BK_{\rm b}$ | 215–216 (`\ref` 없음) |
| §5 [[x:cavity-tree-sampling]] | tilted reservoir 보조 kernel과 terminal Gibbs kernel로 tree를 뽑음 | 29–30, 36 (`\ref` 없음) |
| §3 [[tree:log-expansion]], [[tree:Q-rule]] | $Q_k$, 차수별 급수, 꼬리 $\sum_{k>q}c^k/k$ | 123 (`\cref`), 205 (`\cref`), 211–213 |
| §3 [[tree:regular-shapes]], [[x:tree-regular-shape]], [[tree:averaging-remark]] | 비정칙 확률, 배정 확률 $C_kL^{-a}$, 지워도 regular; 정규화 $L^{-a'}$ 의 논법 | 141 (`\cref`), 142–148 (`\ref` 없음) |
| §3 [[tree:Y-recursion]], [[tree:insertion]] | trial recursion; 동차성($\log z$ 상쇄)과 단조성 | 175 (`\eqref`); 203, 215–216 (`\ref` 없음) |
| §3 [[x:tree-sampling]], [[tree:multioverlap]], [[x:tree-path-kernels]], [[tree:original-tilt]], [[x:tree-extra-variables]] | 자식의 조건부 독립, 사영 일관성(유도된 부분 tree), $R_S$, path 깊이, tilted kernel, 추가 root 변수 | 28–31, 62, 78, 101–106, 142–150 (`\ref` 없음) |
| §7 [[decor:overlap-concentration]] | 각 $U\in\mathfrak S_k$ 와 고정 $\eta$ 의 깊이 평균 분산 소멸 | 153 (`\cref`) |
| §7 [[decor:average-definition]], [[x:decor-eta-regular]], [[x:decor-topology]], [[x:decor-spin-product]], [[x:decor-limit-order]] | $\mathcal A_{L,\eta}$ (정규화 $L^{-a'}$, 질량 $\le1$, singleton은 좌표 없음), regular의 뜻, labeled topology, $\operatorname{Var}(R_U)$ 의 뜻, 같은 수열 | 131–156 (`\ref` 없음) |
| §2 [[model:chain]] | $\mathcal M_j$, 사슬 (2.7)과 그 branching 판, 서로 다른 label | 50–51, 72 (`\eqref`), 182 |
| §2 [[x:model-message]], [[model:site-message]], [[model:edge]] | $q_x$; $U_\theta$, $C_\theta$ (trial 평균) | 40, 60; 179–183 (`\ref` 없음) |
| §2 [[model:vs]], [[model:ve]], [[model:power-means]] | $V_{\rm s}$; $V_{\rm e}$; 조건부 power mean $T_0$ | 180 (`\eqref`); 189; 184–185 (`\ref` 없음) |
| §2 [[model:functional]], [[x:model-depth-zero]] | $\mathcal B_{L-1}$, $\Phi_r$ ($r\ge0$) | 166, 192, 227 (`\cref{model:section}`), 229 |
| §2 [[model:trial-bounds]] | $A=\inf_r\Phi_r$ 의 유한성; trial 쪽 $\lvert\log T_0V_{\rm s}\rvert\le H+BK$ | 235 (`\eqref`), 215–216 |
| §2 [[model:hamiltonian]] | $F_N$ | 229 |

**밖에 내주는 것.**

| 받는 곳 | 쓰는 것 | 원문 위치 |
|---|---|---|
| reduction:section 서두 | [[comp:bounded-lower]] | reduction.tex 4 (`\cref`) |
| [[main:theorem.s2]] | [[comp:bounded-lower]]가 truncation이 factorization을 보존하든 말든 적용됨 | reduction.tex 63–65 (`\cref`) |
| [[main:theorem.s3]] | [[comp:bounded-lower]] (잘린 모형의 $\liminf_NF^{(K)}_N\ge I_K$) | reduction.tex 76 (`\cref`) |
| 규칙 P10, P11, L1 수 6 | [[comp:encoding]], [[comp:patterns]], [[comp:shape-error]], [[comp:insertion-comparison]] | layers |
| overview.tex Step 4 | 이 절 전체: 부호화, 독립 사본으로 바꾸기, 선택된 증분에 가까운 시행값 | overview.tex 36–40 (40 `\cref`) |
| §7 서두 (예고) | 깊이 평균 multioverlap 집중이 이 절의 비교에 필요한 평균이라는 것 | decorrelation.tex 11–13 (13 `\cref`) |

나머지 카드(encoding, patterns, shape-error, insertion-comparison)는 이 절 밖의 원문에서 쓰이지 않는다.

**인터페이스 대조 (다른 섹션 카드가 적은 export와 실제 사용).** 검토 2(comp·reduction)의 (a)–(e) 대응으로 다른 섹션 카드의 export를 고친 뒤의 대조다.
- §7 [[decor:section]]: 내주는 것으로 [[decor:overlap-concentration]], [[decor:average-definition]], [[x:decor-eta-regular]], [[x:decor-topology]], [[x:decor-spin-product]], [[x:decor-limit-order]]을 적는다. 실제 사용과 맞는다(153행 하나만 `\cref`, 나머지는 `\ref` 없이 131–156에서). 같은 수열이라는 점([[x:decor-limit-order]]와 [[x:comp-standing]])과 $\eta$ 범위($0<\eta<1/2$ ⊂ $\eta>0$)도 맞는다.
- §6 [[pert:section]]: comparison.tex 8–15, 20, 130, 243과 53–56, 그리고 11–14의 $\underline F$·$\Delta_N$ 의 출처 [[x:pert-increment]]를 적는다. 맞는다. ([[x:pert-increment]] 카드 자신의 provides에는 §8이 아직 없다. 그 카드는 이번 수정 범위 밖이다.)
- §5 [[cavity:section]]: provides 줄과 "밖에 내주는 것" 표가 [[cavity:increment]](reservoir, $A_{\rm s}$, $A_{\rm b}$, (5.5)), [[x:cavity-tree-sampling]], [[cavity:grid]](123, 162), [[x:cavity-bounded]](200, 215–216, 226), [[cavity:increment.s4]](215–216)를 적는다. 맞는다.
- §3 [[tree:section]]: [[tree:log-expansion]]과 꼬리, [[tree:Q-rule]], [[tree:regular-shapes]], [[tree:averaging-remark]], (tree:Y-recursion)에 더해 `\ref` 없는 사용으로 [[tree:insertion]]의 동차성(203; 215–216의 단조성은 [[cavity:increment.s4]]와 [[model:trial-bounds]]를 거침), [[x:tree-sampling]]의 자식 독립과 사영 일관성(62, 142–150), [[tree:multioverlap]], [[x:tree-regular-shape]], [[x:tree-extra-variables]](28)를 적는다. 맞는다.
- §2 [[model:section]]: comparison.tex 72/180/227/235의 `\ref` 에 더해 `\ref` 없는 사용([[model:ve]], [[model:power-means]], [[model:functional]], [[x:model-depth-zero]], [[x:model-message]], [[model:site-message]], [[model:edge]], [[model:hamiltonian]])을 적는다. 맞는다.

**순환.** [[comp:bounded-lower]]는 [[model:section]]이나 [[main:theorem]]이 아니라 해당 정의 노드를 `uses`에 넣는다. 이 절의 어떤 카드도 model:section, main:theorem, upper:bound, reduction 카드를 `uses`에 넣지 않는다.
