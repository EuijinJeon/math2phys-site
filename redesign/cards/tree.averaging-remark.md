---
id: tree:averaging-remark
kind: remark
title: '깊이 평균을 $Q_k$ 평균으로 옮기기'
uses: [tree:regular-shapes, tree:log-expansion, x:tree-regular-shape]
provides: '§8 comp:shape-error-bound (comparison.tex 144–148이 이 논법을 그대로 쓴다: L^{a−a′} 확장, 정규화 L^{−a′}). §7의 깊이 평균 정리를 §8의 log 전개로 넘기는 다리'
math: |
  고정 $k$에 대해 labeled topology는 유한 개다. 그러므로 (tree:assignment-probability)는 $a$개 branching 좌표를 가진 topology에 대한 정규화하지 않은 깊이 평균 $L^{-a}\sum$을 그 topology의 $Q_k$ 아래 기여에 대한 상계로 바꾼다. 부분 모양 위의 오차에 대해서도 같다: 부분 모양이 버리는 좌표에 대해 합하는 비용은 많아야 해당하는 $L$의 거듭제곱이다. (tree:irregular-probability)와 함께, 이것이 regular 깊이 배정 위의 평균 추정을 log 전개에서 쓸 수 있게 한다.

  (작성자 정식화, 원문에 식으로는 없음: 음이 아닌 $z$와 $a$개 좌표의 topology $\tau$에 대해 $\mathbb E_{Q_k}[z;\tau,\text{regular}]\le C_kL^{-a}\sum_{\mathbf q\text{ regular}}z(\mathbf q)$. $z$가 그중 $a'$개 좌표에만 의존하면 우변은 $C_kL^{-a'}\sum_{\mathbf q'}z(\mathbf q')$ 이하.)
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [516, 525]}
status: proposed
---

이 remark가 §7의 [[decor:average-definition|깊이 평균]] $\mathcal A_{L,\eta}$(정규화 $L^{-a}$, 질량 $\le1$)이 왜 그 꼴인지를 설명한다: $Q_k$의 배정 확률 상계 $C_kL^{-a}$가 정확히 그 정규화를 준다. 부분 모양 판은 §8에서 $R_U$($U$는 $[k]$의 부분집합 위 topology)의 분산을 다룰 때 쓰인다. 부분 모양이 regular라는 것은 [[tree:regular-shapes]]의 마지막 문장에서 온다.
