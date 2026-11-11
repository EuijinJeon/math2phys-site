---
id: decor:order-of-limits
kind: remark
title: '극한 순서에 관한 주의'
uses: [x:decor-limit-order, decor:identity-error, decor:conditional-concentration, decor:conditional-concentration.s3.s3, decor:depth-continuity]
provides: '§7 전체의 극한 순서가 맞다는 점검. §8에서 같은 순서(고정 L에서 N 먼저)로 decor:overlap-concentration을 적용한다 (comparison.tex 153–155)'
math: |
  이 절에서 상쇄되지 않는 작은 분모($J=\kappa(S^+)^2$, $C(S,e)$로 나누기)는 처방된 tree 항등식의 오차에만 붙는다. 고정 $L$에서 관련 tree는 유한 개이므로 그 오차는 깊이 평균이나 $L$ 극한보다 먼저 $N\to\infty$에서 사라진다 (decor:identity-error). $N$ 극한 후에 남는 오차는 균등한(uniform) 상대 절댓값 비용 상계 (conditional-concentration.s3.s3), 더 작은 모양의 공분산 평균, martingale 추정 $C/L$ (decor:depth-continuity)로 제어된다. $N$에 대한 $L$-균등 수렴 속도는 어디에도 쓰지 않는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [613, 623]}
status: proposed
---

물리적으로는 "열역학 극한을 먼저, 계층을 촘촘히 하는 극한을 나중에"라는 순서다. 이 순서는 결과의 유효 범위(gap)에 들어가며, 규칙 표에서는 decor:[[g:multioverlap|overlap]]-concentration의 차이 열에 기록된다. 별도의 물리 진술은 두지 않는다.

**균등성의 범위.** 원문(tex 618–621)에서 "uniform"은 상대 절댓값 비용 상계에만 붙는다. 그 상계의 상수 $C_{k,\eta}$가 $L$과 [[g:topology|깊이 배정]]에 무관하다는 것은 [[decor:conditional-concentration.s3.s3]]의 `math`가 준다. 더 작은 모양의 공분산 평균 $V_{k-1,L}(\eta/2)$와 $C/L$은 $L$의 함수이고 $L\to\infty$에서 0으로 가는 양이므로 "$L$에 균등"하다고 쓰지 않는다. 이들에 곱하는 상수가 $L$에 무관하다는 것은 점화식 (tex 516–517, 601)과 lemma 7.3의 상수 진술(tex 164–165)에서 읽히지만, 이 remark 자체가 말하는 내용은 아니므로 `math`에 넣지 않았다.
