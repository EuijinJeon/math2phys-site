---
id: tree:section
kind: section
title: '§3 유한 tree 위의 미적분'
uses: [model:chain, x:tree-path-kernels, x:tree-sampling, tree:multioverlap, tree:original-tilt, tree:Y-recursion, x:tree-extra-variables, tree:first-variation, x:tree-analytic-bounds, x:tree-differentiation-rule, tree:telescoping, tree:Q-rule, x:tree-extension-history, x:tree-reference-paths, x:tree-cancellation-example, x:tree-regular-shape]
provides: '§4 upper (tree:log-expansion과 그것을 통한 tree:Y-recursion, tree:Q-rule, x:tree-sampling; \ref 없이 tree:insertion의 증분 log Y_0와 단조·동차, x:tree-extra-variables, tree:original-tilt), §5 cavity (tree:insertion과 그 단조성, tree:Y-recursion, tree:original-tilt, x:tree-extra-variables, x:tree-sampling), §6 perturbations (tree:insertion의 W_T(A)와 단조성, x:tree-extra-variables, tree:extension-expansion과 그 해석적 경계, x:tree-extension-history), §7 decorrelation (tree:extension-expansion, tree:reference-total, tree:charging, tree:multioverlap, x:tree-sampling), §8 comparison (tree:log-expansion과 꼬리, tree:Q-rule, tree:regular-shapes, tree:averaging-remark, tree:Y-recursion). overview.tex 24가 이 절 전체를 가리킨다'
math: |
  받는 것. 고정 $L\ge1$, 지수 $0=m_0<m_1<\cdots<m_L=1$, 임의의 확률 kernel 열 $K_1,\ldots,K_L$ (root 분포 고정, x:tree-path-kernels)뿐이다. 모형의 가정(factorization, positivity, 짝수 $p$, 섭동)은 하나도 쓰지 않는다. model:chain은 시행 법칙의 $\eta_d$, $x$를 깊이 $d$, $r$의 변수로 읽는 대응(trees.tex 26–27)에만 나온다. tilted kernel은 임의의 leaf 분배함수와 prior kernel에서 만든다(tree:original-tilt).

  내놓는 것.
  (1) insertion calculus (tree:insertion): tilted kernel에서 $A$를 곱하면 root log가 $\log Y_0$만큼 바뀌고, kernel은 $K_d^A=(Y_d/Y_{d-1})^{m_d}K_d$, tree 밀도는 $W_{\mathcal T}(A)=\prod_aA^a\prod_\beta Y_\beta^{\gamma_\beta}$, $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$. recursion은 단조·동차.
  (2) log 전개 (tree:log-expansion): $A=1+tD$, $|t|\|D\|_\infty<1$에서 $\log Y_0=\sum_{k\ge1}\frac{(-1)^{k-1}t^k}{k}\mathbb E_{Q_k}E_{\mathcal T}\prod_{a=1}^kD^a$ (root 조건부), $|t|\|D\|_\infty\le c<1$이면 $K$차 뒤 나머지 $\le\sum_{k>K}c^k/k$.
  (3) canceled-anchor 전개 (tree:extension-expansion): $\partial_{t_1}\cdots\partial_{t_k}E_{\mathcal T}^{A_{\boldsymbol t}}[H/A_{\boldsymbol t}^{a_*}]|_{\boldsymbol t=0}=\sum_Ec_EE_{\mathcal T_E}[H\prod_jD_j^{a_j(E)}]$, 좌변은 복소 근방에서 kernel에 균등하게 해석적·유계.
  (4) reference 합 (tree:reference-total): 한 걸음 $m_d-jm_{d+1}$, 처방 모양 $S$ 전체 $\kappa(S)=\prod_{v\in\operatorname{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$, old tree에 무관.
  (5) charging (tree:charging, $m_d=d/L$): old branching 깊이가 아닌 지정 vertex $b$개면 $\sum|c_E|\le C_{q,k}\delta^b$, 그리고 $m_{d_v}\ge\eta$이면 $|J|^{-1}\sum|c_E|\le C_{q,k,\eta}$.
  (6) 깊이 분포 (tree:regular-shapes, tree:averaging-remark, $m_d=d/L$): $Q_k\{\text{not regular}\}\le C_k(\eta+L^{-1})$, 배정 하나의 확률 $\le C_kL^{-a}$, 지워도 regular.
  (7) tree 표본 규칙과 multioverlap (x:tree-sampling, tree:multioverlap).
physics: |
  [[g:power-mean|power mean]] 안에 넣은 [[g:insertion|insertion]]의 효과를, 깊이 $L$ [[g:hierarchy|보조 계층]]에서 [[g:state|상태]]를 공유하는 [[g:replica|replica]] tree 위의 기대값으로 정확히 전개하는 미적분이다. 섭동 미분 한 번이 replica 하나를 더하고(기존 replica 재사용 계수 1, 새 갈라짐 계수 $\gamma_\beta$), log 전개의 tree 법칙은 [[g:tree-law|$Q_k$]]이다. 지정한 갈라짐 구조에 대한 계수 합은 닫힌 꼴 $\kappa(S)$이고, 갈라짐 깊이를 old 갈라짐에서 떼면 절댓값 합도 작게 묶인다.
gap: |
  유한 깊이와 임의의 확률 kernel 열에서 증명한 정확한 항등식과 부등식이다. $n\to0$ 해석적 연속도, 무한 계층도, Gibbs 측도의 [[g:physical-pure-state|물리적 pure state]] 분해도 쓰지 않는다(trees.tex 7–12). 물리 계산에서 이 자리를 차지하는 도구(power mean, $\gamma_\beta$, $Q_k$의 물리 이름)와의 대응은 [[g:power-mean]], [[g:tree-coefficient]], [[g:tree-law]]의 물리 대응 칸에 intuition으로만 있고 증명에 쓰이지 않는다. 계수의 부호 있는 합은 큰 상쇄를 품는다(−δ 대 2+δ). 이것을 다루는 (5), (6)은 [[g:grid|균등 격자]] $m_d=d/L$에서만 진술된다. physics 칸은 해석적 경계, 수렴 영역, 상수를 뺐다.
abstraction: weakening
children: [tree:insertion, tree:log-expansion, tree:extension-expansion, tree:reference-total, tree:charging, tree:regular-shapes, tree:averaging-remark]
source:
  - {file: trees.tex, lines: [1, 525]}
status: proposed
---

**뼈대.** 두 전개가 한 미분 규칙에서 나온다(trees.tex 3–6). 
- §3.1 틀과 삽입: [[x:tree-path-kernels]] → [[x:tree-sampling]], [[tree:multioverlap]] → [[tree:original-tilt]], [[tree:Y-recursion]] → [[tree:insertion]] (root log의 변화, 바뀐 kernel, tree 밀도 $W_{\mathcal T}$). [[x:tree-extra-variables]]는 원래 없던 변수를 쓰는 삽입을, [[tree:first-variation]]은 $\partial\log Y_d$를 새 path 하나로 읽는 법을, [[x:tree-analytic-bounds]]는 복소 영역의 경계를 준다.
- §3.2 두 전개: [[x:tree-differentiation-rule]] (protected leaf, fresh path 계수 $\gamma_\beta$) → [[tree:telescoping]]과 [[tree:Q-rule]] → [[tree:log-expansion]]. 그리고 [[x:tree-extension-history]] → [[tree:extension-expansion]].
- §3.3 계수 합: [[x:tree-reference-paths]], [[x:tree-cancellation-example]] → [[tree:reference-total]] (부호 있는 합) → [[tree:charging]] (절댓값 합).
- §3.4 깊이 분포: [[x:tree-regular-shape]] → [[tree:regular-shapes]] → [[tree:averaging-remark]].

**밖에서 받는 것.** 사실상 없다. `\ref`로 밖을 가리키는 곳은 trees.tex 26의 `model:chain` 하나이고, 이는 시행 법칙이 이 틀의 한 예라는 대응일 뿐이다. 인용(MP01, PT04, Ruelle87, trees.tex 8–10)은 선행 연구의 소개이고 증명에 쓰이지 않는다.

**밖에 내주는 것** (`\ref` 위치와 `\ref` 없는 사용).

| 받는 곳 | 쓰는 것 | 원문 위치 |
|---|---|---|
| §4 upper:bound | [[tree:log-expansion]] (정규화된 증분의 $Y_0$, 차수 $n$ 계수, $Q_n$이 세 삽입에 공통, 절대수렴) | upper.tex 81, 97, 121 |
| §4 upper:bound (`\ref` 없음) | [[tree:insertion]]: 삽입 증분이 $\log Y_0$이고 단조성으로 $\lvert\cdot\rvert\le B(\theta)$ ("the recursion preserves multiplicative bounds"); 단조성과 동차성으로 (upper:regularization)이 $2B(\theta)$ 이하. [[x:tree-extra-variables]]: 독립 message 과정을 tilted tree에 덧붙여도 원래 tilt가 그 prior를 바꾸지 않으므로 edge 증분이 $\log T_0V_{\rm e}$. [[tree:original-tilt]]: 보간된 spin 분배함수의 backward power-mean recursion과 "the unperturbed tilted tree". [[tree:Y-recursion]], [[tree:Q-rule]], [[x:tree-sampling]]: tree:log-expansion을 통해 ($Y_0$, $Q_n$이 세 삽입에 공통, replica tree) | upper.tex 51–54, 91–92; 67–68; 41–43, 68; 81, 97–112, 120–121 |
| §5 cavity:increment | [[tree:insertion]] ("the insertion identity for the power means"), 단조성에서 $\lvert\log Y_0\rvert$ 상계, [[tree:Y-recursion]] ($Y_{0,\rm s}$, $Y_{0,\rm b}$, "insertion recursion"), [[tree:original-tilt]] ("tilted reservoir kernels"), [[x:tree-extra-variables]] ("independent new root disorder"), [[x:tree-sampling]] | cavity.tex 53–57, 105–110, 117–118 (`\ref` 없음) |
| §5 cavity (`\ref` 없음) | [[tree:original-tilt]]: 섭동된 leaf 분배함수에 power-mean recursion을 적용해 $P_N^{L,\mathbf u}$를 정의(34–35). [[tree:insertion]]의 단조성: 섭동 없는 spin weight와 점별 비교 후 recursion을 적용해 (cavity:negligible), 섭동 하나의 추가·삭제가 root log를 $\log2$ 이하로 바꿈. [[x:tree-extra-variables]]: 쓰지 않는 보조 변수는 prior로 적분해 없앨 수 있음 | cavity.tex 34–38, 95–98 |
| §6 pert:palm, pert:analytic, 제약 | [[tree:insertion]]과 (tree:density), [[x:tree-extra-variables]], [[tree:extension-expansion]]의 해석적 경계와 계수 $c_E$, [[x:tree-extension-history]] | perturbations.tex 334–338, 370, 391, 433 |
| §6 섭동 구성 (`\ref` 없음) | [[tree:insertion]]의 단조성: factor 경계 $1/2<\psi_\nu<3/2$로 power mean을 거쳐 항별 비교 ("as in (cavity:negligible)") | perturbations.tex 64–65 |
| §7 decorrelation | [[tree:extension-expansion]], [[tree:reference-total]] (tree:K, 반복), [[tree:charging]] (relative-charging), [[tree:multioverlap]], 표본 규칙 | decorrelation.tex 61, 332, 348, 414; [[x:decor-tree-sampling]] |
| §8 comparison | [[tree:log-expansion]]과 (tree:log-tail), [[tree:Q-rule]], [[tree:regular-shapes]], [[tree:averaging-remark]]의 논법, (tree:Y-recursion) | comparison.tex 123, 141–148, 175, 205–211 |

§9 reduction.tex 34–35 "The power means preserve these root-measurable bounds"와 39–40 "the physical constants factor out … of every power mean"은 이 표에 넣지 않았다. 대상이 시행 functional의 연산자 $T_d$(model.tex 92–95)이고, 그 곱셈 경계 보존은 §2가 스스로 진술한다(model.tex 123–127, `model:trial-bounds`). 상수가 power mean 밖으로 나오는 것은 power mean 정의에서 바로 나오는 성질이라 §3의 lemma를 부를 필요가 없다.

**§7 카드와의 대조.** §7 카드가 이 절에서 기대하는 진술을 원문과 맞춰 보았다. [[decor:conditional-concentration.s2.s1]]의 계수($-c_d=m_d-2m_{d+1}$, unary $-\delta$, anchor 혼자 $-\delta$)는 [[x:tree-cancellation-example]]과 같다. [[decor:conditional-concentration.s3.s2]]의 $J=\kappa(S^+)^2$와 인자 크기 $(j-1)m_{d_v}+j\delta$는 [[tree:reference-total]]과 trees.tex 452와 같다. [[decor:conditional-concentration.s3.s3]]의 상대 비용은 [[tree:charging]]을 $q=2k$, $2b$개 지정 vertex, $J=\kappa(S^+)^2$로 적용한 것이고 가정(지정 깊이가 old branching 깊이가 아님, $m_{d_v}$의 하계)이 맞는다. [[decor:conditional-concentration.s5.s3]]의 기준 모양 계수 $(m_d-m_{d+1})\kappa(S^+)^2$와 [[decor:overlap-concentration.s2.s1]]의 $C(S,e)=(m_{e-1}-m_e)\kappa(S)=-\delta\kappa(S)$는 (tree:K)를 해당 처방 모양에 적용한 값과 같다. 어긋남은 찾지 못했다. [[x:decor-tree-sampling]]의 `uses`는 이 섹션 카드 전체를 가리키고 있었으나 내용상 해당 노드인 [[x:tree-sampling]]으로 고쳤다(검토 2 대응).
