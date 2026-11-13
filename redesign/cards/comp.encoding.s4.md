---
id: comp:encoding.s4
kind: step
title: 'root 혼합의 보존, (comp:single-label-moments), label마다의 독립 사본'
uses: [comp:encoding.s3, tree:multioverlap, model:chain, cavity:increment]
provides: 'comp:patterns.s1 ($\bar\pi=\mathbb E\pi$ 의 근거 식, comparison.tex 110), comp:insertion-comparison.s1.s1 (독립 label과 새 물리 disorder의 독립)'
math: |
  $\zeta_{L,N}=\operatorname{Law}(\eta_0)$ 로 두면 root 혼합도 보존된다. 특히 leaf의 모든 부분집합 $S$ 에 대해
  $$\mathbb E\prod_{a\in S}\tau^a=\frac1N\sum_{i=1}^N\mathbb E\prod_{a\in S}\sigma_i^a=\mathbb ER_S.\tag{comp:single-label-moments}$$
  여기서 $\tau^a$ 는 trial label 하나의 leaf $a$ spin이다(작성자; 원문은 $\tau$ 를 정의하지 않고 17–24행 lemma의 "single-label spin process"에서 읽음). 서로 다른 label에는 reservoir root와 균일 site를 포함한 전체 구성의 독립 사본을 쓴다. 그렇게 얻은 message들은 cavity insertion의 새 물리 disorder와 독립이다.
physics: |
  trial label 하나의 replica spin 곱의 평균은 reservoir의 [[g:multioverlap|multioverlap]] 평균 $\mathbb ER_S$ 와 같다. 이웃 site마다 서로 독립인 cavity field 사본을 쓰고, 이 사본들은 cavity 삽입의 새 물리 [[g:disorder|disorder]]와도 독립이다.
gap: |
  첫 등식은 균일 site $i$ 의 평균이다. 독립 사본은 구성상의 선택이고, reservoir의 서로 다른 site들이 독립이라는 주장이 아니다(그 차이가 comp:patterns의 오차다).
abstraction: exact
children: []
source:
  - {file: comparison.tex, lines: [73, 83]}
status: proposed
---

첫 등식: $i$ 가 $\mathscr G_0$ 에 든 독립 균일 변수이므로 $i$ 에 대해 먼저 평균하면 $\frac1N\sum_i$ 가 된다. 둘째 등식은 [[tree:multioverlap]]의 정의 $R_S=\frac1N\sum_i\prod_{a\in S}\sigma_i^a$ 와 기대값의 선형성이다. 첫 등식의 좌변은 [[comp:encoding.s3]]의 출력 법칙 보존을 $\mathscr G_0$ 위에서 평균한 것이다(작성자 풀이). 기대값 $\mathbb E$ 는 양쪽 모두 root와 tree 표본추출을 포함한다.

"new physical disorder in the cavity insertions"는 [[cavity:increment]]의 $A_{\rm s}$, $A_{\rm b}$ 의 $h,\theta_j,K$ 와 index다. 서로 다른 label이 독립이라는 것은 [[model:chain]]의 "각 message label $\omega$ 마다 독립으로"와 같은 구조다.
