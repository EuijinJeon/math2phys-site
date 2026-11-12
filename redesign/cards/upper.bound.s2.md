---
id: upper:bound.s2
kind: step
title: 'interpolation $\varphi(t)$ 와 두 끝점'
uses: [model:chain, model:site-message, model:hamiltonian, model:power-means, model:vs, x:model-depth-zero, tree:original-tilt]
provides: 'upper:bound.s3 (미분할 $\varphi$), upper:derivative (보간된 계), upper:bound.s4 (끝점 값)'
math: |
  시행 법칙을 고정하고 $L=r+1$ 로 둔다. 평균 $t\alpha N$ 의 실제 상호작용과, 각 site $i$ 에서 평균 $(1-t)\alpha p$ 의 독립 cavity 상호작용 $U_\theta(x_1,\ldots,x_{p-1};\sigma_i)$ 사이를 보간한다. 서로 다른 cavity 항은 서로소인 message label을 쓴다. 개수, 상호작용, 장, root message 측도는 quenched이다. spin 분배함수에 backward power-mean recursion을 적용하고, 그 root logarithm의 기대값을 $N$ 으로 나눈 것을 $\varphi(t)$ 로 쓴다. $r=0$ 에서는 모든 message가 quenched이고 보조 recursion이 없다. recursion 전체에서 서로 다른 site가 독립이므로
  $$\varphi(1)=F_N,\qquad\varphi(0)=\log2+\mathbb E\log T_0V_{\rm s}.$$
physics: |
  [[g:interpolation|interpolation]]: $t=1$ 은 실제 계, $t=0$ 은 각 spin이 $p-1$ 개의 독립 [[g:message|cavity field]]를 통해서만 factor를 느끼는 계다. $t=0$ 에서 spin들은 서로 분리되므로 계층 free entropy는 site 하나의 [[g:site-term|site 항]] $N$ 개의 합이다.
gap: |
  $0<t<1$ 에서 $\varphi(t)$ 는 보통 뜻의 pressure가 아니라 message label의 보조 변수를 [[g:power-mean|power mean]]으로 적분한 [[g:root-logarithm|root logarithm]]의 기대값이다($t=1$ 에서만 spin 분배함수가 message에 의존하지 않아 $F_N$ 이 된다). "quenched"는 바깥 $\mathbb E$ 가 평균하고 power mean이 적분하지 않는다는 뜻이다.
abstraction: exact
children: []
source:
  - {file: upper.tex, lines: [36, 49]}
status: proposed
---

**읽기 (작성자).** "root message measures"는 각 label 사슬의 깊이 0 변수 $\eta_0^\omega\sim\zeta$ 로 읽었다([[model:chain]]; [[model:power-means]]에서 $\eta_0$ 은 $\mathscr F_0$ 에 들어 바깥 $\mathbb E$ 가 평균한다). "backward power-mean recursion"은 [[tree:original-tilt]]의 $X_{d-1}=m_d^{-1}\log P_de^{m_dX_d}$ 를 시행 사슬을 prior kernel로 삼아 적용한 것이다(trees.tex 26–27이 시행 사슬을 path kernel의 예로 든다).

끝점의 확인: $t=1$ 이면 cavity 항이 없고 spin 분배함수가 message에 의존하지 않으므로 recursion이 아무것도 하지 않아 root logarithm이 $\log Z_N$ 이다. $t=0$ 이면 실제 상호작용이 없고 $Z=\prod_i\sum_{\sigma_i}\exp(h_i\sigma_i+\sum_jU_{\theta_j}(\cdot;\sigma_i))=\prod_i2V_{\rm s}^{(i)}$ 이며, site마다 message label이 서로소라 power mean이 site별로 인수분해된다(원문은 "Independence between different sites throughout the recursion"이라고만 쓴다). 이 값들이 유한하다는 것은 [[model:trial-bounds]]와 같은 논법이다.
