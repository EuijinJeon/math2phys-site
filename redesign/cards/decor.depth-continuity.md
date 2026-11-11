---
id: decor:depth-continuity
kind: lemma
title: '깊이에 대한 평균 연속성'
uses: [decor:covariance-definition, decor:average-definition, x:decor-eta-regular, x:decor-tree-sampling, x:decor-product-difference, x:decor-average-comparisons]
provides: 'conditional-concentration.s4.s1 (S^+에서 S로, 평가 깊이 e+1에서 e로 되돌리는 비용 h_N). overlap-concentration.s3 (G에서 G_-로, martingale energy). decor:order-of-limits의 C/L'
math: |
  topology $S$와 branching vertex의 부분집합 $U$를 고정한다. 각 $\eta$-regular 깊이 배정에 대해 $S^U$는 같은 topology에서 $U$의 vertex 깊이를 1씩 늘린 것이다. 평가 깊이 $d$가 $S$와 $S^U$ 둘 다의 initial stem 위에 있으면(ancestral), 같은 sampled prefix에서 두 평균을 비교한다. 그러면 충분히 큰 $L$ ($L\ge L_0(\eta,S,U)$, tex 148 "for all sufficiently large $L$")에서
  $$\mathcal A_{L,\eta}\,\mathbb E\|\mu_{d,S^U}-\mu_{d,S}\|_N^2\le C/L.$$
  평균은 모든 branching depth에 대해, 그리고 $d$가 범위를 가지면 $d$에 대해서도 취하며, 그렇지 않으면 $d$는 고정이다. $d$가 $S$의 initial unary 구간을 따라 움직이면($d+1$도 initial stem 위)
  $$\mathcal A_{L,\eta}\,\mathbb E\|\mu_{d+1,S}-\mu_{d,S}\|_N^2\le C/L$$
  (평균은 $d$와 모든 branching depth에 대해, 두 평균은 같은 sampled path 위에서). 상수 $C$는 vertex 수와 이동 수에만 의존하며 $N$, 평가 깊이, transition kernel에 균등하다. 같은 부등식은 $S$를 포함한 더 큰 sampled tree 안에서 계산해도 성립한다.
physics: |
  상태 평균은 계층 깊이에 대해 평균적으로 연속이다. 깊이를 한 단계 옮겨도 상태 평균이 크게 바뀌는 깊이는 드물다. 계층을 따라 쌓이는 정보(martingale 증분의 에너지)가 전체로 유계이기 때문이다.
gap: |
  math는 고정 깊이에서의 연속성을 주지 않는다. 깊이 평균 $\mathcal A_{L,\eta}$에서 $C/L$만 준다("드물다"는 이 평균 상계의 Markov 부등식 꼴 읽기다). "상태"는 보조 계층의 prefix이고 물리적 pure state가 아니다. 이 lemma는 모형과 무관하게 임의의 kernel에 대해 성립하는 martingale 사실이며, $q(x)$나 Parisi 측도를 쓰지 않는다. 덧붙이는 그림(intuition, 논증에 쓰이지 않고 math가 함의하지도 않음): Parisi 함수 $q(x)$가 단조 유계라서 큰 점프가 많을 수 없다는 그림과 닮았다. 실제로 쓰이는 단조 유계량은 $q(x)$가 아니라 깊이별 자기 overlap $\mathbb E\|\mu_{t,T}\|_N^2$이다 (decor:depth-continuity.s1).
abstraction: weakening
children: [decor:depth-continuity.s1, decor:depth-continuity.s2, decor:depth-continuity.s3, decor:depth-continuity.s4]
source:
  - {file: decorrelation.tex, lines: [142, 166]}
  - {file: decorrelation.tex, lines: [168, 206]}
status: proposed
---

**증명의 뼈대.** [[decor:depth-continuity.s1]]: initial stem을 따른 $\mu_{t,T}$는 유계 vector martingale이고 증분 에너지의 합이 1 이하다. 이것을 $d$에 대해 합하고 $L$로 나누면 둘째 부등식이 나온다. [[decor:depth-continuity.s2]]: 깊이 $q$의 branching vertex 하나를 $q+1$로 늦춘 효과는 자식 평균들의 한 걸음 증분으로 눌린다. 여기서 자식 모양은 root에서 그 vertex까지의 경로를 stem으로 갖는 topology이고(x:decor-topology), $\mathscr F_q$, $\mu_{q,T_j}$는 decor:covariance-definition을 그 모양에 적용한 것이다. [[decor:depth-continuity.s3]]: 그 증분을 $q$에 대해 합하면 s1에 의해 유계이고, 바뀐 부분 tree 평균을 조상 깊이 $d$까지 올리는 연산(조건부 기대값과 $|\cdot|\le1$ 인자의 곱)은 제곱 노름을 줄인다. 그래서 이동 하나의 비용은 $C/L$이다($\eta L\ge1$이면 늦춘 깊이 $q+1$이 자식의 initial stem 위에 있다. 이 조건은 작성자 유도). [[decor:depth-continuity.s4]]: 이동 여러 개는 하나씩 바꾸고 제곱 삼각부등식으로 합한다. 중간 모양은 regularity 덕분에 같은 조상 관계를 갖고, $L$이 크면 $\eta/2$-regular 영역에 놓인다(원문이 "large $L$"을 부르는 곳, tex 201–203). 더 큰 tree 안에서도 한 prefix의 marginal law가 같으므로 성립한다.
