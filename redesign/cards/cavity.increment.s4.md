---
id: cavity:increment.s4
kind: step
title: '$\lvert\log Y_0\rvert$ 상계와 증분의 균일 유계성'
uses: [tree:insertion, x:cavity-bounded, cavity:increment.s2, cavity:negligible]
provides: 'cavity:increment의 첫 문장(균일 유계). pert:selection(perturbations.tex 277)의 상수 $C$'
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

**풀이 (작성자).** $e^{-H-BK_{\rm s}}\le A_{\rm s}\le e^{H+BK_{\rm s}}$, $e^{-BK_{\rm b}}\le A_{\rm b}\le e^{BK_{\rm b}}$ 이고 한계가 root-가측이므로 [[tree:insertion]]의 단조성이 같은 한계를 $Y_0$ 에 준다. 기대값은 $\mathbb E\lvert\log Y_{0,\rm s}\rvert\le H+B\alpha p$, $\mathbb E\lvert\log Y_{0,\rm b}\rvert\le B\alpha(p-1)$ 이다. 여기에 [[cavity:increment.s2]]–s3의 $O(N^{-1/4})$ 비용을 더하면 큰 $N$ 에서 $\lvert\Delta_N\rvert\le\log2+H+B\alpha(2p-1)+1$ 같은 상수가 나온다.

"increasing the constant covers the remaining sizes" ❓: 남은 유한 개의 $N$ 각각에서 $\lvert\Delta_N^{L,\mathbf u}\rvert$ 가 $L,\mathbf u$ 에 균일하게 유한해야 한다. 원문은 근거를 적지 않는다. [[cavity:negligible]]($\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)s_N$ 균일)과 $\lvert F_N\rvert\le\log2+\alpha B+H$ 에서 나온다고 읽어 `uses`에 넣었다(작성자 읽기).
