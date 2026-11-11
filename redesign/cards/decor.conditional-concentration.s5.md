---
id: decor:conditional-concentration.s5
kind: step
title: '부호 있는 확장 합과 계수 표'
uses: [decor:conditional-concentration.s3, decor:conditional-concentration.s4, tree:reference-total, tree:extension-expansion, x:decor-tree-sampling]
provides: 'decor:conditional-concentration.s6'
math: |
  $f$를 옛 leaf $2k$개 전체의 overlap $A^{\rm I}_S\cdot A^{\rm II}_S$로 둔다. 확장을 target II 첫 경로의 깊이-$e$ prefix로 분류하면, 각 class 안에서 $\mathbb E[f\cdot P_E]$는 일정하고 class별 총 계수는 다음과 같다. class $\ell$ ($d\le\ell<e$, fresh divergence at $\ell$): 사영된 overlap $a\cdot b_\ell$, 총 계수 $-c_\ell J$. class "old prefix through $e$": 사영된 overlap $a\cdot b$, 총 계수 $m_eJ$. 여기서 $c_d=(d+2)\delta$, $c_\ell=\delta$ ($d<\ell<e$)이고 $b_\ell$은 새 stem 위의 $a_{S,e}$로 old II와 깊이 $\ell$까지 prefix를 공유한다. $\ell=d$이면 $a,b,b_d$를 나르는 세 stem은 $d$ 아래에서 조건부 독립이다. 전체 계수는 old tree에서도 anchor 혼자에서도 $-\delta J$이다. anchor 혼자인 쪽에서는 확장된 tree 전체가 target이고 제약이 그 모양($d$에서 분리된 $S^+$ 두 사본, anchor는 원래 자리)을 정하므로, x:decor-tree-sampling에 의해 anchor 혼자인 쪽의 모든 확장에서 target overlap $R_E$는 같은 법칙을 갖는다. 그 공통 기대값을 $\mathbb ER_{\rm target}$이라 하면 anchor 혼자인 쪽의 합은 $\sum_Ec_E\,\mathbb ER_E=-\delta J\,\mathbb ER_{\rm target}$이다 (tex 362–363 "In every extension", 418–419, 444–445).
physics: null
gap: null
abstraction: blackbox
children: [decor:conditional-concentration.s5.s1, decor:conditional-concentration.s5.s2, decor:conditional-concentration.s5.s3]
source:
  - {file: decorrelation.tex, lines: [386, 433]}
status: proposed
---

**증명의 뼈대.** [[decor:conditional-concentration.s5.s1]]이 target II 첫 경로의 가능한 prefix를 세 종류로 나눈다. [[decor:conditional-concentration.s5.s2]]는 같은 class의 확장들이 사영된 항에 대해 같은 결합 법칙을 주므로 class별 계수 합만 필요함을 보인다. [[decor:conditional-concentration.s5.s3]]이 tree:reference-total로 class별 계수 합을 계산하고, anchor 혼자인 쪽의 모든 확장이 같은 법칙의 target을 주어 그 합이 $-\delta J\,\mathbb ER_{\rm target}$으로 묶임을 적는다.
