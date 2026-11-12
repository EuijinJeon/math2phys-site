---
id: x:cons-3sat-remark
kind: remark
title: '짝수 체수 가정은 random 3-SAT을 제외한다 (Remark 10.4)'
uses: [models:sat, model:functional]
provides: '받아 쓰는 카드 없음(범위 주석). models:sat의 차이 칸 (1)'
math: |
  models:sat의 짝수 체수 가정은 random 3-SAT을 제외한다. 그 모형에 대해서는 동반 논문([OpenAIThreeSAT2026, Theorem 8.4])이, clause 개수가 Poisson이고 변수 위치를 독립 복원추출로 뽑는 경우에, 유한 rational 시행에 대한 정확한 soft-pressure 공식을 준다. 그 공식의 부호 첨자 message 쌍은 확률분포를 이루지 않아도 되고, 그 시행 functional은 (2.11)과 다르다.
physics: |
  홀수 체수인 random 3-SAT은 이 논문의 결과 밖이다. 원문은 같은 Poisson 개수·복원추출 앙상블에서 3-SAT의 soft pressure를 다른 시행 [[g:functional|functional]]로 다룬 동반 논문을 가리키기만 한다.
gap: |
  이 사이트는 동반 논문을 검토하지 않았고, 원문도 그 결과를 이 논문에서 쓰지 않는다. "finite rational trials"와 "sign-indexed message pairs"의 정확한 뜻은 이 원문에 정의되어 있지 않다 ❓. 원문은 두 functional의 관계(어느 쪽이 다른 쪽을 포함하는지 등)나 3-SAT의 다른 성질에 대해 아무것도 말하지 않는다.
abstraction: weakening
children: []
source:
  - {file: consequences.tex, lines: [131, 138]}
status: proposed
---

graph.json에서 이 remark의 ID는 `x:consequences-L131` 이다(라벨 없음). 카드 ID는 이 섹션의 작성자 이름 규칙(`x:cons-*`)을 따랐다. 홀수 $K$ 가 제외되는 직접적인 이유는 주정리가 짝수 $p$ 를 고정하는 데 있다([[model:integrability]]; 짝수 $p$ 는 상한의 볼록성에 쓰인다, [[upper:remainder]]). 원문의 이 remark는 이유를 "even-arity hypothesis in models:sat"라고만 적는다.
