---
id: pert:concentration.s4
kind: step
title: '볼록 함수에서 도함수로, 그리고 두 기여의 합'
uses: [pert:concentration.s1, pert:concentration.s3, pert:concentration.s2, pert:error, x:pert-parameter-measure]
provides: 'pert:concentration의 결론 (6.5)'
math: |
  $\bar G=\mathbb E_{\mathbf u}G$ 로 두면
  $$\frac1{|I_\nu|}\int_{I_\nu}\mathbb E_{\mathbf u}|G'(u)-\mathbb E_{\mathbf u}G'(u)|\,du\le C_\nu\left(\frac{\sqrt N}{\rho}+\frac{\rho\lambda_\nu}{|I_\nu|}\right)$$
  이고, $\rho=N^{-1/8}$ 과 $\lambda_\nu=c_\nu N^{3/4}$ 에서 $\lambda_\nu$ 로 나눈 양이 0으로 간다. $G'$ 의 보정을 없애는 비용은 $C_\nu\lambda_\nu^{-1/2}$ 이하다. 그래서 (6.4)의 root 기여가 0으로 가고, (6.10)과 합쳐 $u_\nu$ 적분 뒤 결과가 나온다. 모든 추정이 다른 매개변수에 균등하므로 나머지 곱측도로 적분해 (6.5)를 얻는다.
physics: null
gap: null
abstraction: blackbox
children: [pert:concentration.s4.s1, pert:concentration.s4.s2]
source:
  - {file: perturbations.tex, lines: [211, 244]}
status: proposed
---

**뼈대.** [[pert:concentration.s4.s1]]: 볼록 함수의 앞·뒤 차분몫으로 $|G'-\bar G'|$ 을 $Z=G-\bar G$ 의 세 값과 $\bar G'$ 의 증가량으로 누르고, $\bar G'$ 의 단조성으로 증가량의 구간 적분을 $2\rho$ 배로 줄인다. [[pert:concentration.s4.s2]]: $\rho$ 를 고르고, 보정을 빼고, path 기여(s2)와 합친다.

볼록성이 하는 일(작성자 읽기): (6.11)은 함수 $G$ 의 값의 root 요동을 누를 뿐 도함수 $G'$ 의 요동은 누르지 않는다. 일반 함수라면 값이 거의 같아도 기울기는 크게 다를 수 있다. $G$ 가 볼록이면 $G'(u)$ 가 간격 $\rho$ 의 앞·뒤 차분몫 사이에 끼므로, 도함수의 요동은 차분몫으로 옮긴 값의 요동($\sqrt N/\rho$ 규모)과 평균 도함수 $\bar G'$ 의 변화(구간 적분으로 $\rho\lambda_\nu$ 규모)로만 눌린다. $G$ 의 root 요동은 $\sqrt N$ 규모로 score 규모 $N^{3/4}$ 보다 작으므로, $\rho\to0$ 이면서 $\sqrt N/\rho\ll\lambda_\nu$ 가 되게 $\rho$ 를 고를 수 있다. $\rho=N^{-1/8}$ 은 $\lambda_\nu$ 로 나눈 두 항을 같은 차수 $N^{-1/8}$ 로 맞춘다([[pert:concentration.s4.s2]]의 지수 계산). 볼록성은 [[g:root-logarithm|root logarithm]]의 2차 미분이 분산을 포함한다는 s2.s1의 결과에서 온다.
