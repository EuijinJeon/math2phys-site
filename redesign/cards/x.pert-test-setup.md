---
id: x:pert-test-setup
kind: convention
title: 'old tree $\mathcal T$, anchor $a_*$, 시험함수 $f$ 의 고정과 $\mathbb Ef$'
uses: [x:pert-selected-limits, x:tree-sampling, tree:multioverlap]
provides: 'pert:score-identity, pert:palm-expression, pert:analytic-difference, pert:palm, pert:analytic, x:pert-colored-extensions, pert:tree-identity'
math: |
  old labeled tree $\mathcal T$, 구별된 leaf $a_*$, 그 old replica들의 multioverlap에 대한 유계 다항식 $f$ 를 고정한다. 다항식과 그 계수는 $N$ 과 insertion 매개변수가 변해도 고정이다. 이 tree 위의 root 평균한 기대값을 간단히 $\mathbb Ef$ 로 쓴다. anchor marginal은 언제나 tilted path 하나다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [316, 321]}
status: proposed
---

"anchor marginal is always one tilted path"는 [[x:tree-sampling]]의 사영 일관성(나머지 leaf를 지워도 남은 tree의 법칙이 보존됨)을 `\ref` 없이 쓴 것이다. 기대값은 [[x:pert-selected-limits]]대로 선택된 벡터에서의 reservoir 기대값이다(root와 tree 표본추출을 포함, [[tree:multioverlap]]의 약속). [[g:anchor]]는 이 $a_*$ 다.
