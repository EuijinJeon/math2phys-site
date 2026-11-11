---
id: main:theorem.s3
kind: step
title: '$K\to\infty$ 와 상수 되돌리기: $\liminf_NF_N\ge\inf_r\Phi_r$'
uses: [main:theorem.s1, main:theorem.s2, reduction:stability, comp:bounded-lower, model:functional, x:model-depth-zero]
provides: 'main:theorem.s4의 하한'
math: |
  $\widehat I$ 를 정규화된(상수 이동한) 시행 functional의 모든 깊이와 시행 법칙에 대한 inf, $I_K$ 를 잘린 물리 법칙으로 같은 inf라 하자. 균일한 시행 안정성(reduction:stability의 시행 functional 부등식)이
  $$\lvert\widehat I-I_K\rvert\le\alpha(2p-1)D_K+d_K$$
  를 준다. pressure 안정성(reduction:stability의 $\lvert F_N-F_N'\rvert\le\alpha D+d$)과 comp:bounded-lower는
  $$\liminf_N\widehat F_N\ge I_K-\alpha D_K-d_K\ge\widehat I-2\alpha pD_K-2d_K$$
  를 준다. $K\to\infty$ 로 $\liminf_N\widehat F_N\ge\widehat I=\inf_r\widehat\Phi_r$. 상수 이동을 되돌리면(reduction:stability의 $\widehat F_N=F_N-\alpha\mathbb Ec$, $\widehat{\mathcal B}_r=\mathcal B_r-\alpha\mathbb Ec$) $\liminf_NF_N\ge\inf_r\Phi_r$.
physics: |
  잘린 모형의 하한을 [[g:stability|$L^1$ 안정성]]으로 원래 모형에 옮긴다. 핵심은 시행 쪽 안정성 상수가 모든 $r$ 과 시행 법칙에 균일해서 inf와 극한 $K\to\infty$ 를 바꿀 수 있다는 것이다. [[g:constant-shift|상수 이동]]은 pressure와 [[g:functional|시행 functional]]을 같은 양만큼 옮기므로 되돌려도 부등식이 남는다.
gap: |
  정확하다. 첫 부등식 $\liminf_N\widehat F_N\ge I_K-\alpha D_K-d_K$ 는 $\widehat F_N\ge F_N^{(K)}-\alpha D_K-d_K$ 와 comp:bounded-lower의 $\liminf_NF^{(K)}_N\ge I_K$ 를 합친 것이다(원문은 둘을 한 줄로 쓴다). 되돌리기는 $\widehat F_N=F_N-\alpha\mathbb Ec$ 와 $\widehat{\mathcal B}_r=\mathcal B_r-\alpha\mathbb Ec$ 에서 $\widehat\Phi_r=\Phi_r-\alpha\mathbb Ec$ 이므로 양변의 $-\alpha\mathbb Ec$ 가 지워진다. 마지막 단계는 상수가 $\zeta,\mathbf m,r$ 에 의존하지 않는다는 데 기댄다(작성자가 풀어 씀).
abstraction: exact
children: []
source:
  - {file: reduction.tex, lines: [70, 84]}
status: proposed
---

$2\alpha pD_K+2d_K$ 는 $\alpha D_K+d_K+\alpha(2p-1)D_K+d_K$ 이다.
