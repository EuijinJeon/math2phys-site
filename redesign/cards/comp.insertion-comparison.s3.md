---
id: comp:insertion-comparison.s3
kind: step
title: 'log 전개의 차수별 비교와 차수 절단'
uses: [comp:insertion-comparison.s2, tree:log-expansion, tree:Q-rule, comp:patterns, comp:shape-error, comp:encoding, cavity:increment, x:comp-standing]
provides: 'comp:insertion-comparison.s4 (고정 $M$, $q$ 에서 남은 유한 개 전개 항의 극한과 꼬리 경계)'
math: |
  tree:log-expansion의 각 차수 $k$ 에서, $D$ 의 $k$ 사본의 곱은 많아야 $pM$ 개 label의 replica-spin pattern과 독립인 insertion disorder의 유계 함수다. comp:patterns에 의해 고정 tree 위에서 그 평가 오차는 $pM\sum_{S\ne\varnothing}\mathbb E\lvert R_S-\mathbb ER_S\rvert$ 이하다. 그러므로 (comp:shape-error)가 tree 평균한 오차를 순서 있는 극한에서 0으로 보낸다. 모든 고정 $M$ 에 대해, 전개를 $q$ 항 뒤에서 자르면 양쪽 모두에서 오차가 $N,L$ 에 균일하게 많아야 $\sum_{k>q}c^k/k$ 다.
physics: |
  삽입 log를 [[g:tree-law|tree 법칙]] $Q_k$ 위 [[g:replica|replica]] 평균의 급수로 쓰면, 각 항은 이웃 site들의 [[g:spin-pattern|spin pattern]]의 유계 함수다. 그래서 차수마다 이웃을 독립 사본으로 바꾸는 비용은 tree 평균한 [[g:multioverlap|multioverlap]] 요동이고, 그것은 극한에서 사라진다.
gap: |
  (1) 차수별 비교는 고정 $k$ 에서만 하고 높은 차수는 균일한 기하 꼬리로 버린다. 그래서 $M$ 이 고정이어야 한다($c=\tanh(H+BM)$). (2) "순서 있는 극한"은 고정 $L$ 의 선택된 수열 위 $\limsup_N$ 뒤 $L\to\infty$ 다([[g:order-of-limits]]). (3) 이웃 수가 $pM$ 으로 유한한 것은 절단 덕분이다.
abstraction: approximation
children: []
source:
  - {file: comparison.tex, lines: [205, 213]}
status: proposed
---

**양쪽의 같은 꼴 (작성자 읽기).** [[tree:log-expansion]]은 임의의 kernel 열에서 성립하는 root 조건부 항등식이라, reservoir 쪽(tilted reservoir kernel)과 trial 쪽(trial kernel)에 같은 $t=1$, 같은 $D$ 의 꼴로 적용된다. 두 쪽의 $Q_k$ 는 같은 지수열 $m_d=d/L$ 의 같은 법칙이다([[tree:Q-rule]]은 $\mathbf m$ 만으로 정해진다). 차수 $k$ 항은 $\frac{(-1)^{k-1}}k\mathbb E\,\mathbb E_{Q_k}E_{\mathcal T}\prod_{a=1}^kD^a$ 이고, $\mathcal T$ 를 고정하면 $\mathbb E\,E_{\mathcal T}\prod_aD^a$ 가 [[comp:patterns]]의 "고정 tree 위 관측량의 기대값"이다: 관측량 $\mathbf1_{\{K\le M\}}\prod_aD^a$ 는 절댓값 1 이하이고 $k$ 개 leaf의 pattern을 site label마다 쓴다. reservoir 쪽 site label은 [[cavity:increment]]의 독립 균일 index이고 trial 쪽은 [[comp:encoding]]의 독립 label이다.

$pM$: site 삽입은 $(p-1)K_{\rm s}\le(p-1)M$ 개, bond 삽입은 $pK_{\rm b}\le pM$ 개 label을 쓴다.

꼬리: $\lvert\frac1k\mathbb E_{Q_k}E_{\mathcal T}\prod D^a\rvert\le c^k/k$ ([[tree:log-expansion]]의 나머지 경계).
