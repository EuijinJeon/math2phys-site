---
id: decor:overlap-concentration.s5
kind: step
title: '마무리: conditional-concentration 적용'
uses: [decor:overlap-concentration.s4, decor:conditional-concentration]
provides: 'decor:overlap-concentration'
math: |
  decor:conditional-concentration (s1의 동치 형태)에서 $\lim_{L\to\infty}V_{k-1,L}(\eta/2)=0$이므로 s4의 우변이 $L\to\infty$에서 0으로 가고 정리가 증명된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [609, 611]}
status: proposed
---

s4는 $|S|=k$인 모양의 분산을 잎이 $k-1$ 이하인 모양의 공분산 평균으로 누른다. 그래서 명제가 모든 크기에 대해 이미 성립하면 정리에는 귀납이 따로 필요 없다.
