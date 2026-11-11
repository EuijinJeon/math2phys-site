---
id: x:tree-extra-variables
kind: convention
title: '원래 모형에 없던 변수를 쓰는 insertion'
uses: [tree:insertion, tree:original-tilt]
provides: '§5 cavity:increment ("independent new root disorder", cavity.tex 55–57), §6 pert:palm ("extended by the independent insertion variables with their prior kernels", perturbations.tex 336–338)'
math: |
  insertion은 원래 모형에 없던 추가 변수를 쓸 수 있다. lemma (tree:insertion)을 적용하기 전에 각 path kernel을 그 변수들의 독립 prior kernel로 넓힌다. 원래의 backward logarithm은 이 변수들에 의존하지 않으므로 원래의 tilt는 그 조건부 prior kernel을 바꾸지 않는다. 추가 root 변수는 quenched로 남는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [135, 140]}
status: proposed
---

"quenched로 남는다"는 추가 root 변수가 root의 일부로서 $E_{\mathcal T}$의 조건 안에 들어가고(root가 주어진 조건부 기대값), 바깥 $\mathbb E$에서만 평균된다는 뜻으로 읽었다. §5의 새 root disorder(새 spin의 장, 상호작용 $\theta_j$, 균일 index)와 §6의 새 site와 [[g:mark|mark]] 과정이 이 약속으로 들어온다.
