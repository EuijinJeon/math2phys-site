---
id: comp:patterns.s1
kind: step
title: '균일 site pattern의 경험분포 $\pi$ 와 $\bar\pi=\mathbb E\pi$'
uses: [comp:encoding.s4, tree:multioverlap, x:tree-sampling]
provides: 'comp:patterns.s2'
math: |
  표본으로 뽑은 reservoir 배치가 주어지면 균일 site의 pattern $\boldsymbol\sigma_i=(\sigma_i^1,\ldots,\sigma_i^k)$ 의 경험분포는
  $$\pi(\boldsymbol e)=\frac1N\sum_i\prod_{b=1}^k\frac{1+e_b\sigma_i^b}{2}=2^{-k}\sum_{S\subseteq[k]}R_S\prod_{b\in S}e_b,\qquad\boldsymbol e\in\{-1,1\}^k$$
  이다. (comp:single-label-moments)에 의해 trial label의 분포는 $\bar\pi=\mathbb E\pi$ 다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [99, 110]}
status: proposed
---

둘째 등식은 곱을 전개한 것이다: $\prod_b\frac{1+e_b\sigma_i^b}2=2^{-k}\sum_S\prod_{b\in S}e_b\sigma_i^b$, site 평균이 $R_S$ 를 준다($R_\varnothing=1$, [[tree:multioverlap]]). trial 쪽: label 하나의 pattern $(\tau^1,\ldots,\tau^k)$ 의 확률은 같은 전개에서 $2^{-k}\sum_S\mathbb E[\prod_{b\in S}\tau^b]\prod_{b\in S}e_b$ 이고 (comp:single-label-moments)로 $\mathbb E\pi(\boldsymbol e)$ 와 같다(작성자 풀이). 기대값은 root와 고정된 tree의 표본추출을 포함한다.
