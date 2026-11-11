---
id: tree:insertion
kind: lemma
title: 'Insertion calculus (삽입 미적분)'
uses: [tree:original-tilt, tree:Y-recursion, x:tree-sampling]
provides: '§5 cavity:increment (cavity.tex 105–106 "the insertion identity for the power means", 108–109의 |log Y_0| 상계는 단조성에서). §6 pert:palm (perturbations.tex 334–335, 370의 W_T(A)와 anchor 인자 상쇄). §3 안에서 x:tree-differentiation-rule, x:tree-analytic-bounds, x:tree-extension-history(γ_β)'
math: |
  leaf 분배함수를 지수 $m_1,\ldots,m_{L-1}$의 power mean으로 반복하고 $K_1,\ldots,K_{L-1}$이 그 tilted kernel (tree:original-tilt), $K_L$이 말단 Gibbs kernel이라 하자. 각 spin weight에 $A$를 곱하면 반복된 root logarithm이 $\log Y_0$만큼 바뀐다. 여기서 (tree:Y-recursion)은 insertion 전의 kernel을 쓴다. 새 kernel은 (tree:updated-kernel)이다.

  처방된 tree의 내부 vertex $\beta$에 대해 $d_\beta$를 깊이, $n_\beta$를 자식 수라 하고
  $$\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$$
  로 둔다. 바뀐 tree 법칙의 조건부 결합 밀도는
  $$W_{\mathcal T}(A):=\frac{dP_{\mathcal T}^A}{dP_{\mathcal T}}=\prod_{a\in\operatorname{Leaves}(\mathcal T)}A^a\prod_{\beta\in\operatorname{Int}(\mathcal T)}Y_\beta^{\gamma_\beta}$$
  이다. $Y_\beta$는 $\beta$의 prefix에서 계산한 $Y_{d_\beta}$다.

  recursion은 단조이고 동차다: root-가측인 양의 $a,b$에 대해 $a\le A\le b$이면 모든 깊이에서 $a\le Y_d\le b$이다. $A$에 root-가측인 양의 상수를 곱하면 모든 $Y_d$가 그 상수배가 된다.

  (가정: tree:Y-recursion의 대로 $A$는 양이고, root가 주어진 조건부로 위로 유계이며 0에서 떨어져 있다.)
physics: |
  spin의 Boltzmann 무게에 양의 함수 $A$를 곱하는 [[g:insertion|insertion]]은 [[g:power-mean|power mean]]으로 반복한 root log를 정확히 $\log Y_0$만큼 바꾸고, 각 깊이의 kernel을 $(Y_d/Y_{d-1})^{m_d}$로 재가중한다. $L=1$이면 $\log Y_0=\log\langle A\rangle$이고 새 kernel은 $A$로 재가중한 Gibbs 측도다. [[g:replica|replica]] tree의 법칙은 leaf마다 $A$, 내부 vertex마다 $Y_\beta^{\gamma_\beta}$를 곱한 만큼 바뀐다([[g:tree-coefficient|계수]] $\gamma_\beta$).
gap: |
  kernel이 그 leaf 분배함수의 power mean에서 나온 tilted kernel이어야 한다(임의의 kernel 열에 대한 $Y$ recursion은 정의되지만 "root log의 변화 $=\log Y_0$"는 tilted kernel에서만 뜻이 있다). $A$는 root가 주어진 조건부로 위아래로 유계여야 한다. $L\ge2$의 root log는 보통 뜻의 free entropy가 아니다([[g:root-logarithm]]).
abstraction: exact
children: [tree:insertion.s1, tree:insertion.s2, tree:insertion.s3]
source:
  - {file: trees.tex, lines: [84, 111]}
  - {file: trees.tex, lines: [113, 133]}
status: proposed
---

**증명의 뼈대.** [[tree:insertion.s1]]: 말단에서 분배함수 비가 $K_LA=Y_{L-1}$이고, power mean에 대입해 backward induction하면 backward log의 차가 $\log Y_d$이다. 이것이 $\log Y_0$ 공식과 바뀐 kernel을 준다. [[tree:insertion.s2]]: edge마다 밀도비 $(Y_d/Y_{d-1})^{m_d}$를 tree 위에서 곱하고 vertex마다 지수를 모은다. [[tree:insertion.s3]]: 단조성과 동차성은 recursion에 대한 backward induction이다.

$n_\beta\ge1$이고 $m_d<m_{d+1}$이므로 모든 내부 vertex에서 $\gamma_\beta<0$이다: unary vertex($n_\beta=1$)에서 $\gamma_\beta=m_d-m_{d+1}$, root에서 $\gamma=-n m_1$. 확장 계수 $c_E$의 부호가 섞이는 것은 계수 $1$(옛 leaf 재사용)과 음의 $\gamma_\beta$(fresh path)가 함께 나오기 때문이다. 이 계수가 이후 모든 확장의 계수가 된다([[x:tree-differentiation-rule]], [[x:tree-extension-history]]).

§5는 이 lemma를 `\ref` 없이 쓴다: cavity.tex 105–106 "The insertion identity for the power means then proves (cavity:identity)", 108–109의 $|\log Y_{0,\rm s}|\le H+BK_{\rm s}$는 단조성에서 나온다(작성자 읽기).
