---
id: x:pert-standing
kind: convention
title: '§6의 약속: 유계 모형, 고정 깊이 $L\ge2$, 두 계, 고정 매개변수의 기대값'
uses: [x:cavity-bounded, cavity:grid, cavity:increment, x:cavity-tree-sampling]
provides: '§6 전체. 특히 pert:concentration의 "reservoir에서도 성립"(perturbations.tex 102)과 그 증명의 Efron–Stein 논증(물리 disorder의 구조), pert:selection의 reservoir 진술, x:pert-parameter-measure와 x:pert-selected-limits의 "고정한 채" 기대값'
math: |
  이 절 내내 상호작용과 장은 유계이고(x:cavity-bounded), 깊이 $L\ge2$ 는 고정이다(cavity:grid). 논증은 $N$-spin 계와 cavity:increment의 reservoir 모두에 적용된다. reservoir의 물리적 disorder는 평균 $O(N)$ 의 Poisson 개수를 갖는 독립 유계 상호작용들과 $N$ 개의 독립 유계 장으로 이루어진다. 지정된 매개변수 벡터에서의 진술에 나오는 모든 기대값은 그 벡터를 고정한 채 취한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [4, 10]}
status: proposed
---

"depth $L\ge2$ is fixed"의 $L$ 은 §5가 고정한 깊이이고, 지수는 cavity:grid의 $m_d=d/L$ 이다. 다만 §6의 증명이 지수에 대해 쓰는 것은 $0<m_1\le m_d$ 와 $m_L=1$ 뿐이다([[pert:concentration.s2.s1]]). 이 절의 상수가 $L$ 에 의존하는 것은 $1/m_1=L$ 을 통해서다(perturbations.tex 152, 159; 작성자 읽기).

reservoir에 대한 문장(6–8행)은 [[x:cavity-tree-sampling]](cavity.tex 117–121 "Thus the concentration argument applies to its slightly modified interaction mean as well")과 같은 내용을 §6 쪽에서 다시 적은 것이다. 이것이 [[pert:concentration.s3.s3]]의 "root 변수 개수가 $O(N)$"에 쓰인다.

마지막 문장(9–10행)은 [[x:cavity-root-convention]](cavity.tex 29–31, 매개변수는 고정값이고 매개변수 평균은 명시할 때만)과 짝이다. [[g:root]]의 기대값 $\mathbb E$, $\mathbb E_{\mathbf u}$ 는 $\mathbf u$ 를 평균하지 않는다. 매개변수 평균은 $\pi$ 로 쓸 때만이다([[x:pert-parameter-measure]]).
