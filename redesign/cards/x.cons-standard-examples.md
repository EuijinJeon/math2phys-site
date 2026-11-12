---
id: x:cons-standard-examples
kind: convention
title: '명명 모형도 Poisson 개수와 복원추출을 유지한다'
uses: [model:hamiltonian, model:factorization]
provides: 'models:spin, models:sat, x:cons-energy-score, models:ground (모형 (2.2)의 Poisson 개수 $M_N$ 과 복원추출 index $i_{\ell,k}$ 를 그대로 쓴다는 약속)'
math: |
  factorization (2.3)의 표준 예는 Franz–Leone과 Panchenko–Talagrand의 희석 spin 모형과 random satisfiability 모형이다(원문 인용 [FL03, PT04]). 이 섹션은 (2.2)에 정한 Poisson 개수와 복원추출을 그대로 유지한다.
physics: |
  이 섹션의 [[g:named-models|명명 모형]]은 [[g:factorization|tanh형 전개]]의 표준 예인 희석 spin 모형과 random SAT 모형이고, 모두 factor 개수가 Poisson$(\alpha N)$ 이며 각 factor의 site를 복원추출로 뽑는 Poisson [[g:hypergraph|hypergraph]] 위에 놓인다.
gap: |
  원문은 이 모형들이 (2.3)의 "표준 예"라고만 말하고, 이 자리에서 [FL03], [PT04]의 결과와 비교하지 않는다. factor 개수를 $\alpha N$ 으로 고정하거나 한 factor 안의 site를 서로 다르게 뽑는 모형과의 동치는 다루지 않는다(model:hamiltonian의 차이 칸과 같다).
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [4, 8]}
status: proposed
---

8행의 `\eqref{model:hamiltonian}` 이 이 카드의 유일한 `\ref` 이다. 여기서 [[model:factorization]]은 "the standard examples of the factorization"(4행)의 대상으로만 들어간다. 각 예가 (2.3)을 실제로 만족한다는 확인은 [[models:spin.s1]], [[models:sat.s2]]에 있다.
