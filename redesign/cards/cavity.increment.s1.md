---
id: cavity:increment.s1
kind: step
title: '물리 상호작용의 Poisson 분해'
uses: [model:hamiltonian, x:cavity-bounded]
provides: 'cavity:increment.s3 (reservoir, site 삽입 개수 평균 $\alpha p+O(N^{-1})$, bond 삽입 개수 평균 $\alpha(p-1)+O(N^{-1})$, 버릴 항의 평균 $O(N^{-1})$)'
math: |
  $(N+1)$-spin 계의 Poisson 상호작용 과정을 $N+1$ 과 같은 index의 개수로 쪼갠다. 새 index가 없는 항의 평균은 $\rho_N$ 이다. 새 index가 정확히 하나인 항의 평균은 $\alpha p(N/(N+1))^{p-1}=\alpha p+O(N^{-1})$ 이고, 순열 불변성으로 새 입력을 마지막에 둘 수 있다. 그 항의 다른 index는 $[N]$ 의 독립 균일 index이고 상호작용 함수는 주어진 법칙을 유지한다. 새 index가 둘 이상인 항의 평균 합은 $O(N^{-1})$ 이다. 한편 $N$-spin 계는 같은 reservoir에 평균
  $$\alpha N-\rho_N=\alpha(p-1)+O(N^{-1})$$
  의 Poisson 개수의 옛 상호작용을 더해 얻는다. 이 양들은 충분히 큰 모든 $N$ 에서 음이 아니다.
physics: |
  spin 하나를 더하면 그 spin에 붙는 factor가 평균 $\alpha p$ 개 생기고(평균 차수, [[g:hypergraph]]), 옛 spin들 사이의 factor는 평균 $\alpha N$ 개보다 $\alpha(p-1)$ 개 적다. 그래서 크기 $N$ 과 $N+1$ 의 계는 공통 [[g:reservoir|reservoir]]에 각각 "옛 factor $\alpha(p-1)$ 개"와 "새 spin과 그 factor $\alpha p$ 개"를 더한 것이다.
gap: |
  Poisson 과정의 분해(thinning)라서 정확하다. 평균은 $O(N^{-1})$ 오차를 갖고 그 오차는 cavity:increment.s3에서 상호작용당 비용 $B$ 로 치른다. 새 입력을 마지막 좌표에 두는 데 [[g:permutation-invariance|순열 불변성]]이 쓰인다.
abstraction: exact
children: []
source:
  - {file: cavity.tex, lines: [71, 85]}
status: proposed
---

**확인 (작성자).** 상호작용은 평균 $\alpha(N+1)$ 개이고 각 $p$ 개 index는 $[N+1]$ 에서 독립 균일이다. 새 index가 $j$ 개일 확률은 $\binom pj(N+1)^{-j}(N/(N+1))^{p-j}$ 이므로 Poisson thinning으로 $j=0$ 은 평균 $\rho_N$, $j=1$ 은 $\alpha p(N/(N+1))^{p-1}$, $j\ge2$ 는 $O(N^{-1})$ 이고 서로 독립이다. $\alpha N-\rho_N=\alpha N-\alpha(N+1)(1-\tfrac1{N+1})^p=\alpha(p-1)+O(N^{-1})$. 보통의 장은 옛 site $N$ 개에 그대로 있다.
