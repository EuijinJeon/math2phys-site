---
id: tree:regular-shapes.s3
kind: step
title: 'leaf를 지워도 regular'
uses: [x:tree-regular-shape]
provides: 'tree:regular-shapes의 마지막 문장. §8 comparison.tex 142–143 ("every induced subtree retains the interior and separation conditions")'
math: |
  지운 뒤 남은 branching vertex는 원래 tree에서 이미 같은 깊이의 branching vertex였다. 그 깊이 좌표는 옛 좌표의 부분집합이므로 regularity가 보존된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [511, 514]}
status: proposed
---

regular의 두 조건(각 정규화 깊이가 $(\eta,1-\eta)$ 안, 서로 다른 vertex의 정규화 깊이 차 $>\eta$)은 좌표 집합의 부분집합으로 내려가도 유지된다.
