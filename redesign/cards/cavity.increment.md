---
id: cavity:increment
kind: lemma
title: 'Cavity increments (cavity 증분)'
uses: [x:cavity-bounded, cavity:grid, cavity:factor-bounds, x:cavity-root-convention, x:cavity-root-logarithm, model:hamiltonian, tree:original-tilt, tree:Y-recursion, tree:insertion, x:tree-extra-variables]
provides: 'pert:section (perturbations.tex 6: 같은 논증이 이 reservoir에도 적용), x:pert-increment (perturbations.tex 252–253: 같은 $\Delta_N$ 의 기호), pert:selection (perturbations.tex 277: $\lvert\Delta_N(\mathbf u)\rvert\le C$ 균일), comp:insertion-comparison (comparison.tex 171: $A_{\rm s}$, $A_{\rm b}$ 의 site label을 바꿈; 195, 222: cavity:identity). x:cavity-tree-sampling (reservoir). 규칙 P4, P5, P11, L1 수 2'
math: |
  증분 $\Delta_N^{L,\mathbf u}=P_{N+1}^{L,\mathbf u}-P_N^{L,\mathbf u}$ 는 $N,L,\mathbf u$ 에 대해 균일하게 유계다. 물리 상호작용 개수의 평균이
  $$\rho_N=\alpha(N+1)\Bigl(\frac N{N+1}\Bigr)^p\tag{5.4}$$
  이고 보통의 장과 평균 $c_\nu s_N$ 의 섭동 개수를 갖는 $N$ spin 위의 reservoir가 있어
  $$\Delta_N^{L,\mathbf u}=\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}+o_N(1)\tag{5.5}$$
  이다. 오차는 $L,\mathbf u$ 에 균일하다. insertion recursion은 tilted reservoir kernel과 독립인 새 root disorder를 쓰며, terminal insertion은
  $$A_{\rm s}(\sigma)=\frac12\sum_{\varepsilon=\pm1}\exp\Bigl(h\varepsilon+\sum_{j=1}^{K_{\rm s}}\theta_j(\sigma_{i_{1,j}},\ldots,\sigma_{i_{p-1,j}},\varepsilon)\Bigr),\tag{5.6}$$
  $$A_{\rm b}(\sigma)=\exp\Bigl(\sum_{j=1}^{K_{\rm b}}\theta_j(\sigma_{i_{1,j}},\ldots,\sigma_{i_{p,j}})\Bigr)\tag{5.7}$$
  이다. 여기서 $K_{\rm s}\sim\mathrm{Pois}(\alpha p)$, $K_{\rm b}\sim\mathrm{Pois}(\alpha(p-1))$ 이고 표시된 index는 모두 $[N]$ 의 독립 균일 index다.
physics: |
  [[x:cavity-bounded]]의 유계·순열 불변 가정 아래, 섭동된 계의 $N\to N+1$ [[g:increment|증분]]은 공통 $N$-spin [[g:reservoir|reservoir]]에 새 spin 하나를 [[g:field|장]]과 Poisson$(\alpha p)$ 개 factor와 함께 넣는 site 삽입과, Poisson$(\alpha(p-1))$ 개 factor를 넣는 bond 삽입([[g:site-bond-insertion]])의 [[g:root-logarithm|계층 free entropy]] 변화의 차에 $\log2$ 를 더한 것이고, 오차는 $o(1)$ 이다.
gap: |
  물리 문장은 reservoir의 정확한 평균 개수 (1)과 두 균일성 (3)을 말하지 않는다(덜 말하지만 틀리지 않는다). (1) reservoir의 상호작용 평균 개수는 $\alpha N$ 이 아니라 $\rho_N$ 이다. (2) $\log Y_0$ 는 보통 Gibbs 평균의 free entropy 변화가 아니라 tilted reservoir kernel의 recursion을 거친 [[g:root-logarithm|root logarithm]]의 변화다([[g:insertion]]). (3) $o_N(1)$ 은 $L$, $\mathbf u$ 에 균일하고(실제로 $O(N^{-1/4})$), 증분 자체도 $N,L,\mathbf u$ 에 균일하게 유계다. (4) 이 lemma는 $\lim F_N=\lim\Delta_N$ 을 주지 않는다. 증분 항등식만 준다. (5) 원문은 이 비교가 Aizenman–Sims–Starr 변분 틀과 Panchenko의 spin 분포 꼴을 따른다고 적을 뿐(cavity.tex 4–6), 그 결과를 인용해 증명에 쓰지 않는다.
abstraction: weakening
children: [cavity:increment.s1, cavity:increment.s2, cavity:increment.s3, cavity:increment.s4]
source:
  - {file: cavity.tex, lines: [43, 69]}
  - {file: cavity.tex, lines: [71, 115]}
status: proposed
---

**증명의 뼈대.** [[cavity:increment.s1]]: $(N+1)$-spin 계의 Poisson 상호작용 과정을 새 index의 개수로 쪼갠다. 새 index가 없는 항(평균 $\rho_N$)이 reservoir이고, 하나인 항(평균 $\alpha p+O(N^{-1})$)이 site 삽입이며, 둘 이상인 항은 평균 $O(N^{-1})$ 이다. $N$-spin 계는 reservoir에 평균 $\alpha(p-1)+O(N^{-1})$ 개의 옛 상호작용을 더한 것이다. [[cavity:increment.s2]]: 섭동 개수를 공통 Poisson 점으로 reservoir에 맞추면 어긋나는 factor 수의 기대값이 $O(N^{-1/4})$ 이고, factor 하나의 비용은 $\log2$, 상호작용 하나의 비용은 $B$ 이다. [[cavity:increment.s3]]: 이 비용을 치르고 남은 것에 새 spin 합($2A_{\rm s}$)과 옛 계 보정($A_{\rm b}$)을 넣고 [[tree:insertion]]의 항등식을 쓰면 (5.5). [[cavity:increment.s4]]: 단조성으로 $\lvert\log Y_0\rvert$ 를 누르고 균일 유계성을 얻는다.

식 라벨 (5.4)–(5.7)은 이 진술 안에 있으므로 따로 카드를 두지 않았다. 다른 곳의 `\eqref{cavity:identity}`(comparison.tex 195, 222)는 이 카드를 가리키면 된다.

"tilted reservoir kernels"는 [[tree:original-tilt]]를 reservoir의 leaf 분배함수에 적용한 kernel, "independent new root disorder"는 새 spin의 장, $K_{\rm s}$, $K_{\rm b}$, $\theta_j$, 균일 index이며 [[x:tree-extra-variables]]의 약속으로 들어온다고 읽었다(원문은 `\ref` 없이 쓴다). 이 새 변수들은 reservoir의 보조 변수와 독립이다.
