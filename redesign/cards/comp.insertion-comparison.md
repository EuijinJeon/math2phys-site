---
id: comp:insertion-comparison
kind: proposition
title: '삽입 logarithm의 비교: $\Delta_N\approx\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$'
uses: [x:comp-standing, cavity:grid, x:cavity-bounded, cavity:increment, cavity:increment.s4, x:cavity-tree-sampling, comp:encoding, comp:patterns, comp:shape-error, tree:Y-recursion, tree:insertion, tree:log-expansion, model:chain, model:vs, model:ve, model:power-means, model:functional, model:trial-bounds]
provides: 'comp:bounded-lower.s2 (comparison.tex 244). 규칙 P11, L1 수 6'
math: |
  comp:encoding의 시행 법칙과 $\mathbf m^{(L)}=(1/L,\ldots,(L-1)/L)$ 에 대해
  $$\lim_{L\to\infty}\limsup_{N\to\infty}\Bigl\lvert\Delta_N^{L,\mathbf u_{L,N}}-\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\Bigr\rvert=0.\tag{comp:increment-comparison}$$
  안쪽 극한은 각 $L$ 의 선택된 수열을 따른다(x:comp-standing).
physics: |
  [[g:reservoir|reservoir]]의 [[g:site-bond-insertion|site 삽입과 bond 삽입]]에서 이웃 site들의 [[g:replica|replica]] spin을 [[g:encoded-law|encoded law]]의 서로 독립인 사본으로 바꿔도([[g:independent-copies]]) 기대 삽입 log는 극한에서 변하지 않는다. 바꾼 삽입은 정확히 $(L-1)$단 시행 [[g:functional|functional]] $\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$ 를 준다(site 항 $T_0V_{\rm s}$, bond 항 $\alpha(p-1)\mathbb E\log T_0V_{\rm e}$). 그러므로 [[g:increment|cavity 증분]]은 이 시행값에 가까워진다.
gap: |
  (1) "가까워진다"는 $\lim_L\limsup_N$ 의 뜻이고, 안쪽 $N$ 극한은 고정 $L$ 의 [[g:selected-sequence|선택된 수열]]을 따른다. 고정 $L$ 에서 차이가 0으로 간다는 말이 아니다([[g:order-of-limits]]). 증명 안에서는 Poisson 개수 절단 $M$ 과 전개 차수 $q$ 를 먼저 고정한다. (2) 독립성의 근거는 국소 tree 구조나 거리에 따른 상관 감쇠가 아니라 균일 무작위 site 표본(comp:patterns)과 tree 법칙 평균한 multioverlap [[g:concentration|집중]](comp:shape-error)이다. (3) Parisi parameter는 [[g:grid|균등 격자]]로 고정되고 최적화되지 않는다. (4) [[g:bounded-law|유계]]이고 순열 불변인 상호작용의 진술이다(x:cavity-bounded). (5) "정확히 $\mathcal B_{L-1}$" 부분만 exact이고, 비교 전체는 위 극한의 뜻이다. 보조 계층을 [[g:physical-pure-state|물리적 pure state]]의 계층으로 읽는 것은 증명되지 않는다.
abstraction: approximation
children: [comp:insertion-comparison.s1, comp:insertion-comparison.s2, comp:insertion-comparison.s3, comp:insertion-comparison.s4]
source:
  - {file: comparison.tex, lines: [158, 168]}
  - {file: comparison.tex, lines: [170, 223]}
status: proposed
---

**증명의 뼈대.**
- [[comp:insertion-comparison.s1]]: trial 삽입 $\widetilde A_{\rm s}$, $\widetilde A_{\rm b}$ 를 정의하고 정확한 trial 항등식 $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$, $\mathbb E\log\widetilde Y_{0,\rm b}=\alpha(p-1)\mathbb E\log T_0V_{\rm e}$, $\log2+\mathbb E\log\widetilde Y_{0,\rm s}-\mathbb E\log\widetilde Y_{0,\rm b}=\mathcal B_{L-1}$ 을 얻는다. (5.5)로 남은 일은 reservoir와 trial의 삽입 log 비교다.
- [[comp:insertion-comparison.s2]]: 개수 $K\le M$ 으로 절단하고 $A=z(1+D)$, $\lvert D\rvert\le c<1$ 로 정규화한다. $\log z$ 는 비교에서 지워진다.
- [[comp:insertion-comparison.s3]]: [[tree:log-expansion]]의 차수 $k$ 항마다 [[comp:patterns]]와 [[comp:shape-error]]로 비교하고, $q$ 차 뒤의 꼬리는 $\sum_{k>q}c^k/k$.
- [[comp:insertion-comparison.s4]]: 절단 밖의 Poisson 꼬리 $2\mathbb E[(H+BK)\mathbf1_{\{K>M\}}]$ 와 극한의 조립: $M$, 그다음 $q$, 그다음 $N$ 과 $L$.

**조립된 부등식 (작성자 정식화).** 각 삽입($\rm s$ 또는 $\rm b$)과 고정 $M$, $q$ 에서, $c=c_M=\tanh(H+BM)$ 로
$$\bigl\lvert\mathbb E\log Y_0-\mathbb E\log\widetilde Y_0\bigr\rvert\le2\mathbb E[(H+BK)\mathbf1_{\{K>M\}}]+2\sum_{k>q}\frac{c_M^k}k+\sum_{k\le q}\frac{pM}{k}\,\mathbb E_{Q_k}\sum_{S\ne\varnothing}\mathbb E\lvert R_S-\mathbb ER_S\rvert.$$
앞의 두 항은 $N$, $L$ 에 무관하고 마지막 항은 (comp:shape-error)로 $\lim_L\limsup_N$ 에서 0이다. 그러므로 $\lim_L\limsup_N$ 의 값은 $M,q$ 에 대해 inf를 취해 0이다. (5.5)의 $o_N(1)$ 은 $L,\mathbf u$ 에 균일하므로 $\lvert\Delta_N-\mathcal B_{L-1}\rvert\le\sum_{\rm s,b}\lvert\mathbb E\log Y_0-\mathbb E\log\widetilde Y_0\rvert+o_N(1)$ 에 그대로 들어간다. 원문은 이 식을 쓰지 않고 순서를 말로만 적는다(218–222). 차수 $k$ 항의 계수 $1/k$ 와 $\lvert D\rvert\le c\le1$ 로 관측량 $\prod_aD^a$ 가 1 이하라는 점은 작성자가 확인한 것이다.

**평균의 종류.** $\mathbb E\log Y_0$ 의 $\mathbb E$ 는 reservoir root와 새 insertion disorder(개수 $K$, $\theta_j$, $h$, index)에 대한 것이고, 섭동 매개변수는 선택된 $\mathbf u_{L,N}$ 으로 고정된다. trial 쪽 $\mathbb E$ 는 insertion disorder와 $\eta_0^\omega$ 들에 대한 것이고, 나머지 보조 변수는 recursion(power mean)이 적분한다. log 전개는 root가 주어진 조건부 항등식이고, 그 위에 바깥 $\mathbb E$ 를 취한다.
