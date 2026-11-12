---
id: cavity:increment.s3
kind: step
title: '증분 항등식 (5.5)'
uses: [cavity:increment.s1, cavity:increment.s2, x:cavity-root-logarithm, tree:insertion, tree:original-tilt, x:tree-extra-variables]
provides: 'cavity:increment의 (5.5)'
math: |
  따라서 새 index가 반복된 상호작용을 버리고, 섭동을 맞추고, 두 삽입 개수의 평균을 극한값으로 바꾸는 데 드는 기대 비용은 모두 합해 $O(N^{-1/4})$ 이다. 새 spin에 대해 합하면 $2A_{\rm s}$ 가 나오고, 옛 계의 보정은 $A_{\rm b}$ 를 준다. 인수 $2$ 가 증분의 $\log2$ 항을 준다. 이제 power mean의 insertion 항등식이 (5.5)를 증명한다.
physics: |
  새 spin이 두 번 이상 들어간 factor를 버리고, 섭동 개수를 [[g:reservoir|reservoir]]에 맞추고, 두 삽입 개수의 평균을 극한값 $\alpha p$, $\alpha(p-1)$ 로 바꾸면 기대 비용이 모두 합해 $O(N^{-1/4})$ 이다. 그렇게 바꾼 뒤에는 $N+1$ 계의 새 spin을 합해 없애면 reservoir에 site 삽입 $2A_{\rm s}$ 를 곱한 것이 되고, $N$ 계는 reservoir에 bond 삽입 $A_{\rm b}$ 를 곱한 것이다([[g:site-bond-insertion]]). [[g:insertion|insertion]] 하나가 [[g:root-logarithm|계층 free entropy]]를 정확히 $\log Y_0$ 만큼 바꾸므로 두 계의 차는 $\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}$ 에 $O(N^{-1/4})$ 을 더한 것이다.
gap: |
  오차 $O(N^{-1/4})$ 은 물리 문장에도 적었고 $L$, $\mathbf u$ 에 균일하다(원문은 lemma에서 $o_N(1)$ 로만 진술한다). $\log Y_0$ 는 [[g:root-logarithm|root logarithm]]의 변화이고 tilted reservoir kernel로 계산한다.
abstraction: exact
children: []
source:
  - {file: cavity.tex, lines: [100, 107]}
status: proposed
---

**풀이 (작성자).** 개수 평균을 극한으로 바꾸는 비용: 평균 차가 $O(N^{-1})$ 이고 상호작용당 비용 $B$ ([[cavity:increment.s2]]). 반복된 새 index 항도 평균 $O(N^{-1})$ 개에 비용 $B$. 지배적인 것은 섭동 맞춤의 $O(N^{-1/4})\cdot\log2$ 다.

$\sum_{\varepsilon=\pm1}e^{h\varepsilon+\sum_j\theta_j(\ldots,\varepsilon)}=2A_{\rm s}$ 를 reservoir spin weight에 곱한 것이 맞춘 뒤의 $(N+1)$-spin weight이다. $2$ 는 root-가측 상수라서 [[tree:insertion]]의 동차성으로 $\log2$ 를 따로 낸다. 새 spin의 장과 $\theta_j$, index는 reservoir 보조 변수와 독립인 새 root 변수다([[x:tree-extra-variables]]). 원문 105–106의 "the insertion identity for the power means"를 [[tree:insertion]]의 첫 문단(root log의 변화 $=\log Y_0$)으로 읽었다(`\ref` 없음).
