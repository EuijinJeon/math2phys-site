---
id: pert:concentration.s4.s2
kind: step
title: '$\rho=N^{-1/8}$, 보정 제거, 두 기여의 합'
uses: [pert:concentration.s1, pert:concentration.s4.s1, pert:concentration.s2.s1, pert:concentration.s2.s2, pert:error, x:pert-parameter-measure, pert:factor]
provides: 'pert:concentration의 결론 (6.5)'
math: |
  충분히 큰 모든 $N$ 에서 $\rho=N^{-1/8}$ 로 잡으면 이것은 고정된 근방 여유 안에 있다. $\lambda_\nu=c_\nu N^{3/4}$ 로 나누면 두 항 모두 0으로 간다. $G'$ 의 보정을 없애는 비용은 많아야 $C_\nu\mathbb E|n-\lambda_\nu|/\lambda_\nu\le C_\nu\lambda_\nu^{-1/2}$ 이다. 따라서 (6.4)의 root 기여가 0으로 간다. 이것을 (6.10)과 합치면 $u_\nu$ 에 대한 적분 뒤 결과가 증명된다. 모든 추정이 다른 매개변수에 균등하므로 나머지 곱측도에 대해 적분하면 (6.5)가 증명된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [233, 244]}
status: proposed
---

풀이(작성자). $\sqrt N/(\rho\lambda_\nu)=c_\nu^{-1}N^{1/2+1/8-3/4}=c_\nu^{-1}N^{-1/8}$, $\rho\lambda_\nu/(|I_\nu|\lambda_\nu)=N^{-1/8}/|I_\nu|$. 보정: $G'-\mathbb E_{\mathbf u}G'=(X_0'-\mathbb E_{\mathbf u}X_0')+4u(n-\lambda_\nu)$ 이고 Poisson의 $\mathbb E|n-\lambda|\le\lambda^{1/2}$. "root 기여"는 $\frac1{\lambda_\nu}\mathbb E_{\mathbf u}|\langle D_\nu\rangle-\mathbb E_{\mathbf u}\langle D_\nu\rangle|$ 이다($X_0'=\langle D_\nu\rangle$, [[pert:concentration.s2.s1]]). [[pert:error]]의 $e_{\nu,N}$ 은 삼각부등식으로 path 기여 $\frac1{\lambda_\nu}\mathbb E_{\mathbf u}\langle|D_\nu-\langle D_\nu\rangle|\rangle$((6.10), [[pert:concentration.s2.s2]])와 이 root 기여의 합 이하다. 두 기여는 $u_\nu$ 의 구간 평균으로만 0으로 가고, 다른 성분에 균등하므로 $\pi$ 전체로 적분해도 0으로 간다.
