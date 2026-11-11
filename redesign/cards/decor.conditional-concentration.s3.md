---
id: decor:conditional-concentration.s3
kind: step
title: '이동된 사본과 정규화 $J$의 상대 비용'
uses: [decor:conditional-concentration.s1, pert:tree-identity, tree:reference-total, tree:charging, x:decor-eta-regular, x:decor-mesh]
provides: 'conditional-concentration.s5 (구성과 J), s6 (상대 비용으로 사영 오차를 J로 나눈 뒤에도 제어)'
math: |
  $|S|=k\ge2$, 첫 갈라짐 $e>d$, proper child shape $T_1,\ldots,T_s$. old tree는 stem이 깊이 $d$에서 갈라지고 내부 깊이가 aligned인 $S$의 두 사본 I, II이며, I의 한 옛 leaf가 spin anchor다. $S^+$는 모든 내부 branching depth를 1 늘린 $S$다. 제약 $\mathcal C$: anchor와 added color $2k-1$개가 $d$에서 분리된 $S^+$ 두 사본을 이루고 anchor는 첫 사본의 원래 labeled 자리에 있다. $J=\kappa(S^+)^2$ ($\kappa$는 tree:reference-total의 tree:K)라 하면, $b=b(S)$에 대해 $L\ge L_0(k,\eta)$에서
  $$|J|\ge c_{k,\eta}\delta^{2b}>0,\qquad\frac1{|J|}\sum_{E\ \text{allowed}}|c_E|\le C_{k,\eta}.$$
  전체 부호 있는 기준 계수는 $(m_d-m_{d+1})J=-\delta J$이다.
physics: null
gap: null
abstraction: blackbox
children: [decor:conditional-concentration.s3.s1, decor:conditional-concentration.s3.s2, decor:conditional-concentration.s3.s3]
source:
  - {file: decorrelation.tex, lines: [292, 360]}
status: proposed
---

**증명의 뼈대.** [[decor:conditional-concentration.s3.s1]]이 old tree와 제약을 세운다. [[decor:conditional-concentration.s3.s2]]가 $J$의 하계 $|J|\ge c_{k,\eta}\delta^{2b}$를 준다. [[decor:conditional-concentration.s3.s3]]은 shifted depth가 old tree의 어떤 branching depth와도 다르므로 $2b$개 target vertex가 모두 fresh unary split로 만들어져야 함을 보이고, tree:charging으로 상대 비용 상계를 얻는다. 깊이를 늦추는 이유가 여기 있다. 늦추지 않으면 target vertex가 옛 branching vertex와 겹쳐 계수 1인 옛 leaf 재사용이 생기고, 절댓값 합이 $|J|$와 같은 차수가 되지 않는다.
