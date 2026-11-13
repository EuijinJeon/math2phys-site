---
id: x:pert-selected-limits
kind: convention
title: '이후의 $N\to\infty$ 는 선택된 수열을 따른다'
uses: [pert:selection, x:pert-standing]
provides: 'pert:score-identity, pert:palm, pert:analytic, pert:tree-identity의 모든 N 극한과 기대값의 뜻. §7 decorrelation.tex 4–9(선택 보조정리에서 직접 받아 적은 같은 약속, 이 카드를 받지 않는다), §8 comparison.tex 8–15, 130, 243과 같은 약속'
math: |
  이제부터 $L$ 은 고정이고, $N\to\infty$ 는 pert:selection의 한 수열을 따른 수렴을 뜻한다. 아래 기대값은 선택된 결정적 벡터에서 계산하며 그 $N$ 의존은 표기에서 생략한다. 이 극한들에 대해 $L$, path 수, 섭동 type에 대한 균등성은 주장하지 않는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [308, 312]}
status: proposed
---

$\varepsilon$ 도 고정된 채다(pert:selection의 수열이 $L$, $\varepsilon$ 마다 하나씩이므로; 작성자 읽기). [[pert:analytic.s3]]의 $u_{\nu,N}$ 은 생략된 $N$ 의존을 다시 적은 것으로, 선택된 벡터 $\mathbf u_j$ 의 $\nu$ 성분이다. [[g:selected-sequence]], [[g:order-of-limits]].
