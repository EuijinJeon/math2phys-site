---
id: decor:overlap-concentration
kind: theorem
title: '모든 multioverlap의 깊이 평균 집중'
uses: [x:decor-topology, x:decor-eta-regular, decor:average-definition, x:decor-spin-product, x:decor-limit-order, x:decor-mesh, pert:tree-identity, tree:reference-total, decor:projection-bound, decor:depth-continuity, decor:conditional-concentration, decor:identity-error]
provides: '§8: comparison.tex 153에서 comp:shape-error-bound의 우변을 0으로 보내 comp:shape-error를 얻고, comp:insertion-comparison에서 reservoir site 표지를 독립 사본으로 바꾸는 근거'
math: |
  모든 고정 labeled topology $S$에 대해
  $$\lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}\operatorname{Var}(R_S)=0\qquad(\eta>0),$$
  여기서 $\mathcal A_{L,\eta}$는 $S$의 $b(S)$개 branching depth만을 $\eta$-regular 배정에 대해 평균하고, $N$ 극한은 x:decor-limit-order의 수열을 따른다. singleton이면 (평균에 좌표가 없고) 각 고정 $L$에서 $\operatorname{Var}(R_S)\to0$ ($N\to\infty$).
physics: |
  replica들이 계층의 어느 깊이에서 같은 상태를 공유하는지(ultrametric tree의 topology와 갈라짐 깊이)를 정하면, 그 replica들의 모든 multioverlap $R_S$는 요동하지 않는다(self-averaging). 상태 안 clustering(decor:conditional-concentration)과 상태 평균 overlap의 집중(marker anchor 항등식)이 합쳐진 결과다.
gap: |
  (1) 깊이 평균: 고정 깊이 배정마다 $\operatorname{Var}(R_S)\to0$이 아니라 $\eta$-regular 배정에 대한 평균 $\mathcal A_{L,\eta}$가 0으로 간다 (tex 72 "only the $b(S)$ branching depths are averaged", 83 "Averaging over depths is essential"). 원문은 평균이 필수라고 말할 뿐, 점별 진술이 거짓이라고 말하지는 않는다. 다만 증명은 점별 진술을 주지 않는다. (2) 극한 순서: 고정 $L$에서 pert:selection이 고른 수열을 따라 $N\to\infty$, 그다음 $L\to\infty$. $L$-균등한 $N$ 속도는 없다 (decor:order-of-limits). (3) 대상은 perturbed cavity reservoir의 보조 계층(tilted kernel의 prefix)이며 섭동 없는 Gibbs 측도의 pure state 분해가 아니다. (4) pair overlap뿐 아니라 모든 유한 multioverlap에 대한 진술이다(희석 모형에서 필요). 반면 극한값을 식별하거나 overlap이 깊이만의 함수 $q_d$로 수렴한다고 말하지 않는다. 평균 $\mathbb ER_S$ 주위로 집중한다는 것만 말한다. (5) $\operatorname{Var}$는 root(disorder, 선택된 매개변수)와 tree 표본추출 전부에 대한 분산이다.
abstraction: approximation
children: [decor:overlap-concentration.s1, decor:overlap-concentration.s2, decor:overlap-concentration.s3, decor:overlap-concentration.s4, decor:overlap-concentration.s5]
source:
  - {file: decorrelation.tex, lines: [63, 83]}
  - {file: decorrelation.tex, lines: [526, 530]}
  - {file: decorrelation.tex, lines: [532, 611]}
status: proposed
---

**증명의 뼈대.** singleton은 [[decor:overlap-concentration.s1]]: 추가 color 없는 spin anchor 항등식이 바로 $\operatorname{Var}(R_S)\to0$을 준다. $|S|=k\ge2$이고 첫 갈라짐이 $e$라 하자. $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$로 분산을 $\operatorname{Var}(R_S)=\mathbb E(R_S-M)^2+\operatorname{Var}(M)$으로 나눈다. [[decor:overlap-concentration.s2]]: marker anchor 항등식이 각 고정 $L,e$에서 $\operatorname{Var}(M)\to0$을 준다(상태 사이). [[decor:overlap-concentration.s3]]: $G=\mathbf1\cdot\prod_j\mu_{e,T_j}$, $G_-=\mathbf1\cdot\prod_j\mu_{e-1,T_j}$라 하면 $\mathbb E(R_S-G)^2\le p_N(S,e)^2$, $\mathcal A_{L,\eta}\mathbb E(G-G_-)^2\le C_k/L$이고 $G_-$는 $\mathscr F_{e-1}$-가측이다. [[decor:overlap-concentration.s4]]: $L^2$ 사영의 최적성으로 $\mathbb E(R_S-M)^2\le2p_N^2+2\mathbb E(G-G_-)^2$이고, 고정 $L$에서 유한 합인 깊이 평균과 $\limsup_N$을 바꾸어(각 배정의 $\operatorname{Var}(M)\to0$이 평균 뒤에도 남지 않는다) fiber bound로 $\limsup_N\mathcal A_{L,\eta}\operatorname{Var}(R_S)\le C_k(L^{-1}+V_{k-1,L}(\eta/2)^{1/2})$. [[decor:overlap-concentration.s5]]: decor:conditional-concentration이 $V_{k-1,L}(\eta/2)\to0$을 주므로 끝난다.
