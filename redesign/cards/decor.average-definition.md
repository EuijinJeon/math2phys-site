---
id: decor:average-definition
kind: definition
title: '깊이 평균 $\mathcal A_{L,\eta}$'
uses: [x:decor-eta-regular]
provides: 'decor:overlap-concentration과 decor:conditional-concentration의 진술. comp:shape-error-bound가 같은 평균을 쓴다'
math: |
  $a$개의 깊이 좌표 위의 음이 아닌 배열 $z(\mathbf q)$에 대해
  $$\mathcal A_{L,\eta}z=L^{-a}\sum_{\mathbf q\ \eta\text{-regular}}z(\mathbf q).$$
  $d<\min_vq_v$ 같은 추가 순서 조건은 합의 범위에 넣는다. $\eta$-regular 배정의 수는 $L^a$ 이하이므로 총 질량 $\mathcal A_{L,\eta}1\le1$이다(정규화하지 않은 평균). $a=0$이면 $\mathcal A_{L,\eta}z=z$.
physics: |
  계층 깊이 $d$는 [[g:parisi-parameters|Parisi 매개변수]] $m_d=d/L$에 대응하므로, $\mathcal A_{L,\eta}$는 갈라짐 위치를 Parisi 변수 $x\in(\eta,1-\eta)$에 대해 균등하게 평균하는 연산이다.
gap: |
  대응은 그림일 뿐 논증에 쓰이지 않는다. 평균은 정규화되지 않았고(질량 $<1$일 수 있음), 서로 $\eta L$보다 가까운 갈라짐은 뺀다.
abstraction: intuition
children: []
source:
  - {file: decorrelation.tex, lines: [30, 38]}
status: proposed
---

정규화하지 않았기 때문에 Hölder 꼴 부등식 [[decor:average-holder]]가 상수 없이 성립한다.
