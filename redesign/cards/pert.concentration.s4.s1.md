---
id: pert:concentration.s4.s1
kind: step
title: '차분몫과 단조성으로 얻는 (6.12)'
uses: [pert:concentration.s1, pert:concentration.s3.s1, pert:concentration.s3.s3, x:pert-parameter-measure]
provides: 'pert:concentration.s4.s2'
math: |
  $\bar G=\mathbb E_{\mathbf u}G$, $Z=G-\bar G$ 로 둔다. $u\pm\rho$ 가 $J_\nu$ 안에 있으면 앞·뒤 차분몫이
  $$|G'(u)-\bar G'(u)|\le\frac{|Z(u-\rho)|+2|Z(u)|+|Z(u+\rho)|}{\rho}+\bar G'(u+\rho)-\bar G'(u-\rho)$$
  를 준다. $\bar G'$ 의 단조성이
  $$\int_a^b[\bar G'(u+\rho)-\bar G'(u-\rho)]\,du\le2\rho[\bar G'(b+\rho)-\bar G'(a-\rho)]$$
  를 준다. (6.11)과 함께 이것이
  $$\frac1{|I_\nu|}\int_{I_\nu}\mathbb E_{\mathbf u}|G'(u)-\mathbb E_{\mathbf u}G'(u)|\,du\le C_\nu\left(\frac{\sqrt N}{\rho}+\frac{\rho\lambda_\nu}{|I_\nu|}\right)$$
  를 증명한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [211, 232]}
status: proposed
---

풀이(작성자). 볼록 $G$ 에 대해 $\frac{G(u)-G(u-\rho)}\rho\le G'(u)\le\frac{G(u+\rho)-G(u)}\rho$ 이고 $\bar G$ 도 볼록이라 $\frac{\bar G(u+\rho)-\bar G(u)}\rho\le\bar G'(u+\rho)$, $\frac{\bar G(u)-\bar G(u-\rho)}\rho\ge\bar G'(u-\rho)$. 두 방향을 합치면 위 부등식이다. $\mathbb E_{\mathbf u}|Z(v)|\le(\operatorname{Var}G(v))^{1/2}\le(C_\nu N)^{1/2}$, 그리고 $\bar G'$ 의 증가량 $\le2C_\nu\lambda_\nu$((6.11)의 둘째 추정). 여기서 $\mathbb E_{\mathbf u}$ 는 점 $u$ 마다 그 점의 벡터를 고정한 root 평균이고 $u$ 의 구간 평균과는 따로 취한다(원문의 $\bar G$ 는 $u$ 의 함수로서의 root 평균이다).
