---
id: upper:derivative
kind: step
title: '핵심 부등식 $\varphi^\prime(t)+\alpha(p-1)\mathbb E\log T_0V_{\rm e}\le0$ (4.1)'
uses: [upper:bound.s2, upper:bound.s3, model:ve, model:power-means]
provides: 'upper:bound.s4 (적분). 규칙 P2, L1 수 1'
math: |
  모든 $t\in(0,1)$ 에서
  $$\varphi'(t)+\alpha(p-1)\mathbb E\log T_0V_{\rm e}\le0.\tag{4.1}$$
  (작성자 정리: upper:bound.s3와 함께 읽으면, 보간된 계에 실제 상호작용 하나, 균일 site의 cavity 상호작용 하나, edge 삽입 하나를 넣는 증분을 $I_{\rm real}$, $I_{\rm cav}$, $I_{\rm e}$ 라 할 때 $\mathbb E[I_{\rm real}-pI_{\rm cav}+(p-1)I_{\rm e}]\le0$ 과 같다. $I_{\rm e}=\log T_0V_{\rm e}$ 는 upper:derivative.s1.)
physics: |
  [[g:interpolation|interpolation]] 경로의 각 점에서, 실제 $p$체 factor 하나를 더하는 효과는 [[g:site-term|cavity factor]] $p$ 개를 더하는 효과에서 [[g:edge-term|edge 항]] $p-1$ 개만큼을 뺀 것을 넘지 않는다. 그래서 $\varphi$ 의 기울기가 $-\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ 이하다.
gap: |
  같은 내용이다. 증분은 보통 Gibbs 평균의 free entropy 변화가 아니라 [[g:power-mean|power mean]] recursion을 거친 root logarithm의 변화([[g:insertion]]의 $\log Y_0$)다.
abstraction: exact
children: [upper:derivative.s1, upper:regularization, upper:remainder]
source:
  - {file: upper.tex, lines: [58, 61]}
  - {file: upper.tex, lines: [62, 126]}
status: proposed
---

**증명의 뼈대.** [[upper:derivative.s1]]: (2.3) 아래 세 삽입이 모두 $a(1+D)$ 꼴이다(실제: $D=b\prod_\ell f_\ell(\sigma_{i_\ell})$, cavity: $p-1$ 개 인자를 $\bar f(x)$ 로, edge: $p$ 개 모두). [[upper:regularization]]: $a$ 를 기대값 전에 떼고 $c=\theta(1,\ldots,1)$ 을 빼 정규화한 뒤 $\lambda<1$ 로 정규화한 증분 (4.2)를 쓴다. 한계 $2B(\theta)$ 와 dominated convergence로 $\lambda\uparrow1$ 에서 원래 증분을 회복한다. [[upper:remainder]]: [[tree:log-expansion]]으로 전개하면 $n$차 계수가 $-\frac{\lambda^n}{n}\mathbb E[(-b)^n]\mathbb E_{Q_n}\mathbb E[P_{\mathcal T}^p-pP_{\mathcal T}B_{\mathcal T}^{p-1}+(p-1)B_{\mathcal T}^p]$ (4.3)이고, 짝수 $p$ 의 볼록성과 (2.4)가 그것을 0 이하로 만든다. $\lambda\uparrow1$ 이 (4.1)을 준다.

이 카드의 원문 범위 중 58–61(주장)은 잎 [[upper:derivative.s1]]도 덮는다(포함 검사가 증명 줄을 잎으로 요구하기 때문).
