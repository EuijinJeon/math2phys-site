---
id: cavity:increment.s4
kind: step
title: '$\lvert\log Y_0\rvert$ 상계와 증분의 균일 유계성'
uses: [tree:insertion, x:cavity-bounded, cavity:increment.s2, cavity:increment.s3, cavity:negligible]
provides: 'cavity:increment의 첫 문장(균일 유계). pert:selection(perturbations.tex 277)의 상수 $C$. comp:insertion-comparison(comparison.tex 215–216: 원래 insertion logarithm의 상계 $H+BK$ 를 다시 씀, `\ref` 없음)'
math: |
  끝으로
  $$\lvert\log Y_{0,\rm s}\rvert\le H+BK_{\rm s},\qquad\lvert\log Y_{0,\rm b}\rvert\le BK_{\rm b}.$$
  coupling 추정과 함께 이것이 큰 $N$ 에서 증분을 누르고, 상수를 키우면 나머지 크기도 덮는다. 모든 추정은 $L$ 과 $\mathbf u$ 에 균일하다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: cavity.tex, lines: [108, 115]}
status: proposed
---

**풀이 (작성자).** $e^{-H-BK_{\rm s}}\le A_{\rm s}\le e^{H+BK_{\rm s}}$, $e^{-BK_{\rm b}}\le A_{\rm b}\le e^{BK_{\rm b}}$ 이고 한계가 root-가측이므로 [[tree:insertion]]의 단조성이 같은 한계를 $Y_0$ 에 준다. 기대값은 $\mathbb E\lvert\log Y_{0,\rm s}\rvert\le H+B\alpha p$, $\mathbb E\lvert\log Y_{0,\rm b}\rvert\le B\alpha(p-1)$ 이다. 이것을 [[cavity:increment.s3]]의 (5.5)(오차 $O(N^{-1/4})$, 맞춤 비용은 [[cavity:increment.s2]])에 넣으면 큰 $N$ 에서 $\lvert\Delta_N\rvert\le\log2+H+B\alpha(2p-1)+1$ 같은 상수가 나온다.

"increasing the constant covers the remaining sizes": 남은 유한 개의 $N$ 각각에서 $\lvert\Delta_N^{L,\mathbf u}\rvert$ 가 $L,\mathbf u$ 에 균일하게 유한해야 한다. 근거는 원문에 없다(112–114). 작성자 읽기: [[cavity:negligible]]($\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)s_N$ 균일)과 $\lvert F_N\rvert\le\log2+\alpha B+H$ 에서 $\lvert\Delta_N\rvert\le(\log2)(s_{N+1}+s_N)+(2N+1)(\log2+\alpha B+H)$ 가 나온다고 읽어 `uses`에 넣었다. 다른 길도 된다: 맞춤 추정 자체가 각 $N\ge1$ 에서 유한하고 $L,\mathbf u$ 에 균일하다(검토 2의 의견). 원문은 어느 쪽도 적지 않는다.
