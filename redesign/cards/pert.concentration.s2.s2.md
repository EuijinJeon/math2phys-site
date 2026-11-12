---
id: pert:concentration.s2.s2
kind: step
title: '구간 적분과 path 요동의 경계 (6.9), (6.10)'
uses: [pert:concentration.s2.s1, pert:concentration.s1, x:pert-parameter-measure]
provides: 'pert:concentration.s4.s2 (6.10)'
math: |
  (6.8)을 $I_\nu=[a,b]$ 에서 적분하고 $|X_0'|\le2n$ 을 쓰면
  $$\int_a^b\mathbb E_{\mathbf u}\operatorname{Var}(D_\nu\mid\mathscr F_0)\,du\le\frac{4\lambda_\nu(1+b-a)}{m_1}.$$
  따라서 구간 평균한 thermal 평균 절대 편차를 $\lambda_\nu$ 로 나눈 것은
  $$\left(\frac{4(1+|I_\nu|)}{m_1|I_\nu|\lambda_\nu}\right)^{1/2}$$
  이하다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [147, 161]}
status: proposed
---

풀이(작성자). $\int_a^b\mathbb E_{\mathbf u}X_0''\,du=\mathbb E X_0'(b)-\mathbb EX_0'(a)\le4\mathbb En=4\lambda_\nu$ 이고, 하계 $m_1\operatorname{Var}-4n$ 의 적분은 $m_1\int\mathbb E\operatorname{Var}-4\lambda_\nu(b-a)$ 이다. 이로부터 (6.9). 그다음 $\langle|D-\langle D\rangle|\rangle\le\operatorname{Var}(D\mid\mathscr F_0)^{1/2}$ 와 구간 평균에 대한 Jensen으로 (6.10). 여기서 $\mathbb E_{\mathbf u}$ 는 $u_\nu$ 를 포함한 벡터를 고정한 root 평균이고, $du$ 적분이 [[x:pert-parameter-measure]]의 $\pi$ 의 $\nu$ 성분에 해당한다(정규화 $1/|I_\nu|$). 두 평균을 섞지 않는다.
