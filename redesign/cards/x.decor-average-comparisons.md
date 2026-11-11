---
id: x:decor-average-comparisons
kind: lemma
title: '깊이 평균의 두 기본 비교 (안 쓰는 좌표, 정수 이동)'
uses: [decor:average-definition, x:decor-eta-regular]
provides: 'depth-continuity.s4 (중간 모양이 η/2-regular), conditional-concentration.s7.s3 (fiber bound), overlap-concentration.s4'
math: |
  (i) 안 쓰는 좌표. $\pi$가 $a$개 좌표 중 $a'$개만 남기는 사영이고 $w\ge0$가 남은 좌표의 함수이면, 각 상이 많아야 $L^{a-a'}$개의 원상을 가지므로 $L^{-a}\sum_{\mathbf q}w(\pi\mathbf q)\le L^{-a'}\sum_{\mathbf y\in\pi(\text{domain})}w(\mathbf y)$.
  (ii) 정수 이동. 좌표의 일부를 고정된 정수만큼 옮기는 사상은 단사이고, $L\ge L_0(\eta,\text{이동량})$이면 $\eta$-regular 배정을 $\eta/2$-regular 배정으로 보낸다 (가지를 따른 엄격한 증가도 보존된다).
  (iii) (작성자 추가, 자명) $\eta'\le\eta$이면 $\eta$-regular 배정은 $\eta'$-regular이므로 $z\ge0$에 대해 $\mathcal A_{L,\eta}z\le\mathcal A_{L,\eta'}z$.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [44, 47]}
status: proposed
---

(ii)의 근거: 이동량이 $t$ 이하이면 정규화 깊이는 $t/L$ 이하로, 두 좌표 사이 간격은 $2t/L$ 이하로 바뀐다. $2t/L\le\eta/2$이면 경계 조건과 간격 조건이 $\eta/2$로 유지된다. 간격이 $\eta L>2t$이므로 순서도 뒤집히지 않는다. (iii)은 원문이 $V_{k-1,L}(\eta)\le V_{k-1,L}(\eta/2)$를 말없이 쓰는 곳에 필요해서 적었다. 검토 1에서 참이고 실제로 쓰인다고 확인되었다: tex 509 "The unshifted term has the same bound without translating the coordinates"($\eta$-[[g:eta-regular|regular]] ⊂ $\eta/2$-regular), 520–522의 흡수, 601·607의 $\gamma=1/2$ 적용.
