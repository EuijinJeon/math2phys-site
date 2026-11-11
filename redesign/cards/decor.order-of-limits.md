---
id: decor:order-of-limits
kind: remark
title: '극한 순서에 관한 주의'
uses: [x:decor-limit-order, decor:identity-error, decor:conditional-concentration, decor:conditional-concentration.s3.s3, decor:depth-continuity]
provides: '§7 전체의 극한 순서가 맞다는 점검. §8에서 같은 순서(고정 L에서 N 먼저)로 decor:overlap-concentration을 적용한다 (comparison.tex 153–155)'
math: |
  이 절에서 상쇄되지 않는 작은 분모($J=\kappa(S^+)^2$, $C(S,e)$로 나누기)는 처방된 tree 항등식의 오차에만 붙는다. 고정 $L$에서 관련 tree는 유한 개이므로 그 오차는 깊이 평균이나 $L$ 극한보다 먼저 $N\to\infty$에서 사라진다 (decor:identity-error). $N$ 극한 후에 남는 오차는 상대 절댓값 비용 상계 (conditional-concentration.s3.s3), 더 작은 모양의 공분산 평균, martingale 추정 $C/L$ (decor:depth-continuity)로 제어되며, 이 셋은 모두 $L$에 균등하다. $N$에 대한 $L$-균등 수렴 속도는 어디에도 쓰지 않는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [613, 623]}
status: proposed
---

물리적으로는 "열역학 극한을 먼저, 계층을 촘촘히 하는 극한을 나중에"라는 순서다. 이 순서는 결과의 유효 범위(gap)에 들어가며, 규칙 표에서는 decor:overlap-concentration의 차이 열에 기록된다. 별도의 물리 진술은 두지 않는다.
