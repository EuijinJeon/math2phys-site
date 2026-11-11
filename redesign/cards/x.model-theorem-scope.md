---
id: x:model-theorem-scope
kind: remark
title: '주정리가 말하지 않는 것'
uses: [main:theorem]
provides: 'L0, L1과 규칙 표의 "inf의 달성, 극한 계층은 주장하지 않음" 문장의 근거. g:phi, g:physical-pure-state의 정의 위치'
math: |
  (2.13)의 우변은 유한 계층에 대한 inf다. 정리는 어떤 시행 법칙이 그것을 달성한다고 가정하지 않으며, 극한 무한 깊이 Gibbs 측도(원문 "a limiting infinite-depth Gibbs state")가 구성되었다고 가정하지 않는다.
physics: |
  변분 공식은 최적 [[g:order-parameter|order parameter]]를 찾지 않고 시행값의 [[g:phi|inf]]만 말한다. 물리의 full-RSB 극한 order parameter나 [[g:physical-pure-state|물리적 pure state]]의 계층 구조는 결과에 들어 있지 않다.
gap: |
  원문은 "does not assume"라고 쓴다. 그런 대상이 존재하지 않는다는 말도, 존재한다는 말도 아니다. 원문의 "Gibbs state"는 여기서 "Gibbs 측도"로 옮겼고, 이 사이트의 [[g:state]](보조 계층의 prefix)와 다른 것이다.
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [138, 140]}
status: proposed
---
