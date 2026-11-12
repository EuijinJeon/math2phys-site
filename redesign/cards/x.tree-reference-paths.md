---
id: x:tree-reference-paths
kind: definition
title: 'reference path와 제약의 범위'
uses: [x:tree-extension-history]
provides: 'tree:reference-total, tree:charging, x:tree-cancellation-example. §6 perturbations.tex 433–436 ("involving only the added colors and the anchor ... no extra restrictions involving the other old replicas")와 같은 약속'
math: |
  (§3.3의 목표: 아래 lower bound에 쓰이는 prescribed-tree 항등식에서 부호 있는 정규화와 누적 오차를 제어한다.) extension history에서 anchor와 이미 color를 받은 path를 reference path라 한다. 새 color에 대한 제약은 이 path들과의 갈라짐 깊이만 지정한다. 특히 제약은 같은 지정 조상 관계를 갖는 쓰지 않은 old path들을 구별하지 않는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [306, 315]}
status: proposed
---

[[g:reference-path|reference path]]. 이 약속 때문에 한 걸음 계수 합이 old tree가 아니라 현재 reference tree에만 의존한다([[tree:reference-total]]). 쓰지 않은 old leaf는 reference가 아니므로, 제약은 그것을 "다른 old replica"로서 지정하지 못한다. §6의 제약 $\mathcal C$가 "anchor와 added color 사이의 split 깊이만" 지정한다는 것과 같은 내용이다(perturbations.tex 433–436).
