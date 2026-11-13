---
id: tree:extension-expansion
kind: lemma
title: 'Canceled-anchor expansion (anchor 상쇄 전개)'
uses: [x:tree-extension-history, x:tree-differentiation-rule, x:tree-analytic-bounds, tree:Y-recursion]
provides: '§6 pert:analytic (perturbations.tex 391–394: 해석적 경계), perturbations.tex 429–436 (c_E와 허용 history), 따라서 pert:tree-identity. §7 decor:conditional-concentration.s2.s1, s2, s5, s5.s1 (계수 규칙 1, γ_β)'
math: |
  $H$를 old tree 위 변수들의 유계 함수로, 삽입 매개변수가 변해도 고정된 것이라 하자. 유계 실수 path 함수 $D_j$와 $A_{\boldsymbol t}=1+\sum_{j=1}^kt_jD_j$에 대해
  $$\left.\partial_{t_1}\cdots\partial_{t_k}E_{\mathcal T}^{A_{\boldsymbol t}}\frac{H}{A_{\boldsymbol t}^{a_*}}\right|_{\boldsymbol t=0}=\sum_Ec_E\,E_{\mathcal T_E}\left[H\prod_{j=1}^kD_j^{a_j(E)}\right].$$
  이 공식은 color의 어떤 고정된 순서에서도 성립한다. 같은 방향 $D_j=D$이면 $t^k$의 계수는 우변을 $k!$로 나눈 것이다. 위에서 세운 해석적 경계가 좌변에 kernel에 대해 균등하게 적용된다. 빈 확장의 무게는 $1$이다.
physics: |
  [[g:insertion|insertion]] $A_{\boldsymbol t}$로 바뀐 tree 법칙(모든 leaf가 인자 $A^a$를 받는다)에서 [[g:anchor|anchor]] leaf의 인자 $A^{a_*}$만 상쇄한, 섭동 매개변수와 무관한 old tree 위의 유계 함수 $H$의 기대값을 유계 실수 path 함수인 $k$개 섭동 방향으로 한 번씩 미분해 $\boldsymbol t=0$에서 보면, $k$개 새 color를 [[g:replica|replica]] tree에 붙이는 모든 방법([[g:extension-history|extension history]])에 대한 부호 있는 합이 된다: 아직 쓰이지 않은 기존 replica를 재사용하면 계수 1, 내부 vertex $\beta$에서 새로 갈라지면 계수 $\gamma_\beta$([[g:tree-coefficient]]).
gap: |
  $\boldsymbol t=0$에서의 도함수 항등식이다. 물리 문장은 lemma의 딸린 진술 넷을 말하지 않는다: 공식이 color의 어떤 고정된 순서에서도 성립한다는 것, 같은 방향 $D_j=D$이면 $t^k$의 계수가 우변을 $k!$로 나눈 것이라는 것, [[x:tree-analytic-bounds]]의 해석적 경계가 좌변에 kernel에 대해 균등하게 적용된다는 것(§6 pert:analytic이 쓰는 부분), 빈 확장의 무게가 1이라는 것(trees.tex 292–295). 계수 $\gamma_\beta$는 음이고 재사용 계수는 $+1$이라 합은 상쇄를 품는다(그 크기는 [[tree:reference-total]]과 [[tree:charging]]이 다룬다). 유한 tree와 임의의 kernel 열에서 정확하며 $n\to0$ 연속을 쓰지 않는다. 섭동이 실제로 들어오는 방식(Poisson 섭동, score 집중)은 §6의 일이다.
abstraction: weakening
children: [tree:extension-expansion.s1, tree:extension-expansion.s2]
source:
  - {file: trees.tex, lines: [278, 296]}
  - {file: trees.tex, lines: [298, 304]}
status: proposed
---

**증명의 뼈대.** [[tree:extension-expansion.s1]]: $C=\{a_*\}$, $G=H$에서 시작해 [[x:tree-differentiation-rule]]을 차례로 적용하고 새 $D_j$를 $G$에 넣는다. fresh leaf는 곧바로 protected이므로 protected가 아닌 leaf는 쓰지 않은 old leaf뿐이다. 그래서 선택지가 정확히 [[x:tree-extension-history]]의 (i), (ii)다. [[tree:extension-expansion.s2]]: $\boldsymbol t=0$에서 모든 $A$와 $Y$가 1이므로 updated 법칙이 원래 법칙이 되고 계수만 남는다.

"빈 확장의 무게는 1"은 $k=0$에서 history가 빈 것 하나뿐이고 우변의 유일한 항이 계수 $c=1$의 $E_{\mathcal T}H$라는 뜻이다(작성자 읽기; perturbations.tex 449, 473, 524의 $k=0$ 쓰임과 맞는다). 좌변도 미분 없이 $\boldsymbol t=0$에서 같은 값이다. [[tree:log-expansion]]과의 관계: old tree가 anchor 하나이고 $H=1$이면 (i)이 없고 모든 선택이 fresh다.
