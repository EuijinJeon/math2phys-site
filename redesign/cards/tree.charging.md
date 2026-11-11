---
id: tree:charging
kind: lemma
title: 'Charging fresh splits (fresh split에 작은 인자 매기기)'
uses: [x:tree-extension-history, x:tree-reference-paths, tree:telescoping]
provides: '§7 decor:conditional-concentration.s3.s3 (relative-charging: 상대 절댓값 비용 ≤ C_{k,η}), decor:conditional-concentration (decorrelation.tex 348). glossary g:depth-delay'
math: |
  ($m_d=d/L$, $\delta=L^{-1}$로 둔다.) $q$개 leaf를 가진 old tree에서 시작해 canceled-anchor 확장 규칙으로 $k$개 color를 준다. anchor와 color들의 reference 모양을 처방한다. 허용 확장에 추가 제한이 있어도 된다. 그 모양의 지정된 branching vertex $b$개의 깊이가 old tree 어디에서도 branching 깊이가 아니라고 하자. 그러면
  $$\sum_{E\text{ allowed}}|c_E|\leq C_{q,k}\delta^b.$$
  상수는 $L$, 처방된 깊이, 서로 다른 vertex에서의 깊이 일치에 무관하다.

  특히 이 $b$개 vertex에 대해
  $$J=\prod_v\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$$
  라 하자. 그 모두에서 $m_{d_v}\geq\eta>0$이면 $J\ne0$이고
  $$\frac{1}{|J|}\sum_{E\text{ allowed}}|c_E|\leq C_{q,k,\eta}.$$
physics: null
gap: null
abstraction: blackbox
children: [tree:charging.s1, tree:charging.s2, tree:charging.s3, tree:charging.s4]
source:
  - {file: trees.tex, lines: [388, 391]}
  - {file: trees.tex, lines: [393, 415]}
  - {file: trees.tex, lines: [417, 456]}
status: proposed
---

**왜 필요한가** (trees.tex 388–391). 처방된 항등식을 작은 reference 계수로 나눈 뒤 오차를 제어하려면 절댓값 합의 상계가 필요하다. target branching 깊이를 모든 old branching 깊이에서 떼어 놓으면 그 vertex는 fresh unary split로만 생길 수 있고, 이 lemma가 그런 vertex마다 작은 인자 $\delta$ 하나를 매긴다. [[x:tree-cancellation-example]]의 둘째 계산(절댓값 합 $\delta$)의 일반화이고, [[g:depth-delay|깊이 미루기]]의 핵심이다. 물리 대응은 없다.

**증명의 뼈대.** [[tree:charging.s1]]: 한 걸음의 절댓값 계수 합은 제한이 없으면 $2(q+k)$ 이하, 지정 깊이의 unary fresh split로 제한하면 $(q+k)\delta$ 이하. [[tree:charging.s2]]: 허용 history에서 각 target vertex는 어느 한 걸음에서 fresh unary split로 처음 branching이 되고, 서로 다른 vertex는 서로 다른 걸음이다. 배정은 $k!/(k-b)!$가지 이하. [[tree:charging.s3]]: 배정마다 제약을 줄인 큰 family에서 걸음별 상계를 곱해 $C_{q,k}\delta^b$. [[tree:charging.s4]]: $J$의 하계 $\delta^b\eta^{\sum_v(a_v-2)}$로 나눈다.

§7에서의 쓰임: target이 $S^+$ 두 사본이고 $2b$개 shifted 깊이가 old branching 깊이와 다르며, $J=\kappa(S^+)^2$가 정확히 이 lemma의 $J$다([[decor:conditional-concentration.s3.s3]]). 거기서 $\eta$ 자리에는 $L$이 클 때의 하계가 들어간다(decor 카드는 $\eta/2$를 쓴다).
