---
id: reduction:stability.s1
kind: step
title: 'pressure 안정성 (reduction:free-stability)'
uses: [model:hamiltonian, model:integrability]
provides: 'reduction:stability의 첫 부등식'
math: |
  두 Hamiltonian에 같은 개수와 index를 쓴다. 점별 log-weight 차이는 상호작용 sup-norm 차이들과 장 차이들의 합 이하다. 분배함수의 logarithm은 이 한계를 보존하고, 이것이 (reduction:free-stability)를 준다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: reduction.tex, lines: [28, 32]}
status: proposed
---

**풀이 (작성자).** 모든 $\sigma$ 에서 $\lvert(-H_N(\sigma))-(-H_N'(\sigma))\rvert\le\Lambda:=\sum_{k\le M_N}\max_s\lvert\theta_k(s)-\theta_k'(s)\rvert+\sum_{i\le N}\lvert h_i-h_i'\rvert$ 이므로 $e^{-\Lambda}Z_N\le Z_N'\le e^\Lambda Z_N$, 곧 $\lvert\log Z_N-\log Z_N'\rvert\le\Lambda$. $M_N\sim\mathrm{Pois}(\alpha N)$ 이 나머지와 독립이므로 $\mathbb E\Lambda=\alpha ND+Nd$ ([[model:hamiltonian]]의 독립 구조와 Wald). $N$ 으로 나누면 $\lvert F_N-F_N'\rvert\le\alpha D+d$. 결합은 $(\theta_k,\theta_k')$ 와 $(h_i,h_i')$ 를 결합 법칙의 i.i.d. 사본으로 잡는 것이다.
