---
id: decor:section
kind: section
title: '§7 처방된 tree 위의 decorrelation'
uses: [pert:selection, pert:tree-identity, tree:extension-expansion, tree:reference-total, tree:charging, tree:multioverlap, x:decor-mesh, x:decor-limit-order, x:decor-tree-sampling]
provides: '§8: comparison.tex 123–158에서 decor:overlap-concentration으로 comp:shape-error를 얻고, 이것으로 cavity 삽입의 site 표지를 독립 사본으로 바꾼다 (comp:insertion-comparison)'
math: |
  받는 것 (§6, §3). 각 고정 $L\ge2$에서 $N\to\infty$ 극한은 pert:selection의 수열을 따라 취하고, 그 수열에서 pert:tree-identity의 처방된 tree 항등식이 모든 고정 old tree, anchor, 유계 multioverlap 다항식 $f$, 유한 개 added color, 제약에 대해 성립한다 (x:decor-limit-order). 그 밖에는 §3의 tree 표본 규칙 (x:decor-tree-sampling)과 확장 계수의 계산 (tree:extension-expansion, tree:reference-total, tree:charging)만 쓴다. interaction factorization은 쓰지 않는다. 이 절 전체에서 $m_d=d/L$, $\delta=L^{-1}$ (x:decor-mesh).

  내놓는 것 (§8로). 모든 고정 labeled topology $S$와 모든 $\eta>0$에 대해
  $$\lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}\operatorname{Var}(R_S)=0,$$
  여기서 $\mathcal A_{L,\eta}$는 $S$의 $b(S)$개 branching depth에 대한 $\eta$-regular 깊이 평균이다. singleton $S$이면 각 고정 $L$에서 $\operatorname{Var}(R_S)\to0$ ($N\to\infty$). (decor:overlap-concentration)
physics: |
  계층 깊이 $L$의 cavity reservoir에서 replica들이 어느 계층 깊이에서 같은 상태를 공유하는지(ultrametric tree의 모양과 갈라짐 깊이)를 정하면, 그 replica들의 모든 multioverlap은 self-average한다. 이것은 두 물리 가정의 합이다: 각 계층 상태 안에서 spin들은 clustering한다 (상태 안 요동 없음), 그리고 상태 평균 overlap은 상태와 disorder에 따라 요동하지 않는다.
gap: |
  (1) 고정 깊이 배정마다의 진술이 아니라 $\eta$-regular 깊이 배정에 대한 평균 $\mathcal A_{L,\eta}$의 진술이다 (tex 11–12, 83 "Averaging over depths is essential"). 경계 근처 깊이와 서로 가까운 깊이는 제외된다. (2) 극한 순서는 고정 $L$에서 선택된 수열을 따라 $N\to\infty$, 그다음 $L\to\infty$이고 $N$에 대한 $L$-균등 속도는 없다 (decor:order-of-limits). (3) 대상은 perturbation을 넣은 reservoir의 보조 계층(tilted kernel의 prefix)이지 섭동 없는 Gibbs 측도의 pure state 분해가 아니다. (4) pair overlap만이 아니라 모든 유한 multioverlap에 대한 진술이다. 다만 극한값이 무엇인지, 깊이만의 함수 $q_d$로 수렴하는지는 말하지 않는다. 평균 주위로 집중한다는 것만 말한다.
abstraction: approximation
children: [decor:contractions, decor:depth-continuity, decor:projection-bound, decor:conditional-concentration, decor:overlap-concentration, decor:order-of-limits]
source:
  - {file: decorrelation.tex, lines: [1, 623]}
status: proposed
---

**증명의 뼈대.** 목표는 [[decor:overlap-concentration]]이다. 세 도구를 먼저 준비한다. [[decor:contractions]]는 조건부 공분산 제곱 $v_N(S,d)$가 작으면 spin 곱 벡터를 조건부 평균으로 바꿀 수 있고(축약 부등식), 반대로 조건부 i.i.d. 세 사본의 overlap 차이가 $v_N$을 위에서 누른다(세 사본 부등식)고 말한다. [[decor:depth-continuity]]는 branching depth나 평가 깊이를 한 칸 옮겨도 조건부 평균이 깊이 평균의 의미로 $C/L$만 바뀐다고 말한다. [[decor:projection-bound]]는 첫 갈라짐 $e$에서 $A_S$를 자식 평균의 곱 $a_{S,e}$로 바꾸는 오차를 자식들의 $v_N$으로 누른다.

이 도구와 처방된 tree 항등식으로 [[decor:conditional-concentration]]($\mathcal A_{L,\eta}v_N(S,d)\to0$)을 잎 수에 대한 귀납으로 얻는다. 이것이 "상태 안" 요동의 제어다. [[decor:overlap-concentration]]은 marker anchor 항등식으로 한 칸 앞 prefix에서의 조건부 평균 $M$의 분산을 0으로 보내고("상태 사이" 요동), 남은 조건부 분산을 projection-bound와 depth-continuity, 그리고 conditional-concentration으로 누른다. [[decor:order-of-limits]]는 전 과정에서 $L$에 의존하는 작은 분모가 항등식 오차에만 붙고, 그 오차는 고정 $L$에서 먼저 사라진다는 점을 정리한다.
