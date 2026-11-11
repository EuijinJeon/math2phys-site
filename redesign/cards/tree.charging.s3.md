---
id: tree:charging.s3
kind: step
title: '반복 합: $C_{q,k}\delta^b$'
uses: [tree:charging.s1, tree:charging.s2]
provides: 'tree:charging의 (tree:charging-bound), tree:charging.s4'
math: |
  고정된 배정마다, 지정된 걸음이 배정된 깊이에서 unary split를 만든다는 것만 남기고 모든 제약을 버려 history family를 넓힌다. 그 걸음의 합을 $(q+k)\delta$로, 다른 모든 걸음의 합을 $2(q+k)$로 누른다. 선택에 대해 반복해 합하면
  $$\frac{k!}{(k-b)!}(q+k)^b\bigl(2(q+k)\bigr)^{k-b}\delta^b$$
  이하다. 이것이 (tree:charging-bound)를 증명한다. 배정된 깊이가 겹쳐도 지정된 걸음들은 서로 다르므로 성립한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [438, 447]}
status: proposed
---

반복 합(작성자 풀이): 넓힌 family에서 마지막 걸음부터 합하면 각 걸음의 절댓값 합 상계가 그 앞 선택에 무관하므로 곱으로 떨어진다. family를 넓혀도 절댓값 합은 줄지 않으므로 원래 허용 history의 합을 누른다. 배정에 대해 합하면 $k!/(k-b)!$가 붙는다. 상수 $C_{q,k}=\max_{b\le k}\frac{k!}{(k-b)!}(q+k)^b(2(q+k))^{k-b}$는 $L$과 깊이에 무관하다.
