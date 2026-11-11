---
id: x:decor-eta-regular
kind: definition
title: '$\eta$-regular 깊이 배정'
uses: [x:decor-topology]
provides: 'decor:average-definition의 합 범위. tree:charging 적용 조건(shifted depth가 old branching depth와 다름)과 c_d ≥ η의 근거'
math: |
  $\eta>0$을 고정한다. 깊이 배정 $\mathbf q$가 $\eta$-regular라는 것은 모든 $v$에 대해 $q_v/L\in(\eta,1-\eta)$이고 서로 다른 branching vertex $v\ne w$에 대해 $|q_v-q_w|/L>\eta$라는 뜻이다. 추가 prefix depth $d$가 지정되면 $d$도 같은 조건을 만족해야 한다: $d/L\in(\eta,1-\eta)$, 모든 $v$에 대해 $|d-q_v|/L>\eta$. 한 topology의 두 사본이 aligned depth를 쓰면 대응하는 vertex는 깊이 좌표 하나를 공유하고, regularity는 이 서로 다른 좌표들에 부과한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [21, 28]}
status: proposed
---

trees.tex 460–467의 regular shape 정의와 같은 조건이다(그쪽은 $0<\eta<1/2$로 제한하고(462) "A singleton is regular"를 명시한다(465). §8은 $0<\eta<1/2$만 쓴다, comparison.tex 131; 같은 조건임은 comparison.tex 141–143). 거기서는 $Q_k$로 뽑은 tree에 대해 비정칙 확률이 $C_k(\eta+L^{-1})$임을 보이고(tree:regular-shapes), §8이 그것으로 비정칙 배정을 버린다. regularity 자체에는 물리 대응이 없다: 경계 근처와 서로 가까운 갈라짐을 기술적으로 빼는 조건이다.
