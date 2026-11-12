---
id: x:cavity-tree-sampling
kind: convention
title: '하한의 모든 spin tree는 이 reservoir에서 뽑는다'
uses: [cavity:increment, x:tree-sampling, tree:original-tilt, x:cavity-bounded]
provides: '§6–§8 전체: pert:section(perturbations.tex 3–8의 "the reservoir in cavity:increment", score 집중의 Efron–Stein 논증이 reservoir에도 적용), x:decor-tree-sampling, comp:encoding(comparison.tex 20–29 "reservoir root disorder", "tilted reservoir auxiliary kernels"), comp:insertion-comparison'
math: |
  하한 증명의 나머지에서 모든 spin tree는 이 reservoir에서, 그 tilted 보조 kernel과 terminal Gibbs kernel을 써서 뽑는다. reservoir는 평균 $O(N)$ 의 독립 Poisson 상호작용 과정과 $N$ 개의 독립 유계 장을 그대로 갖는다. 따라서 집중 논증은 조금 바뀐 상호작용 평균에도 적용된다.
physics: |
  하한의 모든 [[g:replica|replica]] tree([[g:prescribed-tree]])는 원래의 $N$-spin 계가 아니라 섭동된 [[g:reservoir|reservoir]]의 [[g:hierarchy|보조 계층]]에서 뽑는다. reservoir는 평균 상호작용 수만 $\alpha N$ 에서 $\rho_N$ 으로 조금 다를 뿐 같은 종류의 무작위 계라서, 뒤의 집중 논증이 그대로 적용된다.
gap: |
  "집중 논증이 적용된다"는 원문이 이 자리에서 미리 하는 말이고 증명은 perturbations.tex(pert:concentration)에 있다. tree의 [[g:state|상태]]는 이 reservoir의 보조 계층 prefix이며 섭동 없는 계의 [[g:physical-pure-state|물리적 pure state]]가 아니다.
abstraction: exact
children: []
source:
  - {file: cavity.tex, lines: [117, 121]}
status: proposed
---

"the concentration argument"는 뒤에 나오는 [[pert:concentration]]을 가리키는 예고로 읽었다(`\ref` 없음). 원문상 뒤의 대상이므로 `uses`에 넣지 않았다.
