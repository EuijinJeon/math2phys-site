---
id: comp:insertion-comparison.s4
kind: step
title: 'Poisson 꼬리와 극한의 조립'
uses: [comp:insertion-comparison.s1.s3, comp:insertion-comparison.s2, comp:insertion-comparison.s3, cavity:increment, cavity:increment.s4, x:cavity-bounded, tree:insertion, model:trial-bounds]
provides: 'comp:insertion-comparison의 결론 (comp:increment-comparison)'
math: |
  개수 절단 밖에서 원래의 삽입 logarithm은 양쪽 모두 $H+BK$ 로 유계다. 그 기대 기여는 많아야 $2\mathbb E[(H+BK)\mathbf1_{\{K>M\}}]$ 이고 $M\to\infty$ 에서 0으로 간다. 이것이 기대 삽입 logarithm의 수렴을 증명한다. 구체적으로, 먼저 Poisson 꼬리를 다루도록 $M$ 을 고르고, 그다음 기하 꼬리를 다루도록 $q$ 를 고르고, 그다음 남은 유한 개 전개 항에 대해 $N$ 과 $L$ 의 극한을 취한다. 위의 trial 항등식과 (5.5)와 합치면 (comp:increment-comparison)이 증명된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [215, 223]}
status: proposed
---

**양쪽의 상계 (작성자 확인).** reservoir 쪽: $\lvert\log Y_{0,\rm s}\rvert\le H+BK_{\rm s}$, $\lvert\log Y_{0,\rm b}\rvert\le BK_{\rm b}$ 는 [[cavity:increment.s4]]에 적혀 있다(cavity.tex 109–110; [[tree:insertion]]의 단조성). trial 쪽: $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$ 이므로 [[model:trial-bounds]]의 $\lvert\log T_0V_{\rm s}\rvert\le\lvert h\rvert+\sum_jB(\theta_j)\le H+BK_{\rm s}$, bond는 인자마다 $\lvert\log T_0C_{\theta_j}\rvert\le B$ 라 $BK_{\rm b}$ 이하. "on both sides"는 이 둘을 가리킨다고 읽었다. $\mathbb E[(H+BK)\mathbf1_{\{K>M\}}]\to0$ 은 $K$ 가 Poisson이라 적분 가능하기 때문이다(dominated convergence).

**극한의 순서.** [[comp:insertion-comparison]]의 조립된 부등식에서 보듯, $M$ 과 $q$ 는 $N$, $L$ 과 무관한 오차만 남기고, $N$ 과 $L$ 의 극한(선택된 수열을 따른 $\limsup_N$, 그다음 $L\to\infty$)은 유한 개 항에만 걸린다. 원문 순서("first choose $M$, then $q$, then take the limits")는 $M$ 과 $q$ 를 $\varepsilon'$ 에 맞춰 고른 뒤 극한을 취하는 것과 같다.
