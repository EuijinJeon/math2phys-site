---
id: x:cons-ground-scope
kind: remark
title: '영온도 공식이 요구하지 않는 것'
uses: [models:ground]
provides: 'L0, g:ground-state의 "쓰지 않는 뜻" 칸(inf는 각 $\beta$ 에서 따로)'
math: |
  (10.1)의 inf는 각 양의 온도에서 따로 모든 유한 계층에 대해 취한다. 이 공식은 inf의 달성이나 극한 계층을 요구하지 않는다.
physics: |
  영온도 공식은 각 온도의 시행값 [[g:phi|inf]]를 $\beta$ 로 나누고 $\beta\to\infty$ 로 보낸 것일 뿐이다. 최적 [[g:order-parameter|order parameter]]가 존재하거나, 그것이 $\beta\to\infty$ 에서 어떤 영온도 order parameter로 수렴할 필요가 없다.
gap: |
  정확하다. 원문은 "does not require"라고 쓴다. 그런 극한 계층이 존재한다고도, 존재하지 않는다고도 말하지 않는다. [[g:rsb-steps|RSB 단계 수]] $r$ 도 각 $\beta$ 에서 따로 inf를 취하므로 $\beta$ 에 따라 다른 $r$ 이 거의 최적일 수 있다(작성자 읽기).
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [127, 129]}
status: proposed
---
