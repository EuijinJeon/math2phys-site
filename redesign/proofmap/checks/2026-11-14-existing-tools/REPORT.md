# 기존 도구와 PM vertex의 대응 확인

2026-11-14. **입출력 graph의 기존 엔진을 재사용할 수 있음은 실행으로 확인했다. PM의 미분 증명이나 현재 proofmap 전체를 바로 대체할 수 있음은 확인하지 않았다.**

## 실제로 실행한 것: Incredible Proof Machine

[공개 엔진](https://incredible.pm/logic.js)을 임시 폴더에 받아 Node의 VM 안에서 실행했다. 사용한 API와 JSON 필드는 [실제 디코더](https://github.com/nomeata/incredible/blob/master/logic/ConvertAeson.hs) 및 [타입 정의](https://github.com/nomeata/incredible/blob/master/logic/Types.hs)와 대조했다. 저장소의 SPEC과 현재 디코더 사이에는 차이가 있어, 현재 블록의 `number` 및 연결의 `sortKey` 필드를 사용했다.

PM의 한 깊이에서의 전제를 다음 다섯 입력으로 옮겼다.

| proofmap 내용 | PM 블록의 입력 포트 |
|---|---|
| FF 문맥 | frame |
| e1: Y의 재귀 | rec |
| e2: 바뀐 kernel의 정의 | tilt |
| e3: 양의 하한·상한 | bounds |
| 현재 깊이의 미분 가능성과 도함수 경계 | ih |

마지막 입력은 d=L이면 e4L, 그 뒤에는 직전 단계 e4에서 받는다. 두 입력을 동시에 요구하는 것으로 번역하지 않았다. 출력은 `identity`와 `next`의 두 포트다. 문맥은 별도 입력으로 승격했으므로, 원본의 받는 edge 다섯 개와 물리적으로 일대일인 포트 다섯 개는 아니다.

수학 식은 `pm-port-mapping.json`에 보존했다. 엔진에 넣는 명제는 고정된 원자 이름이며 **PM 추론 규칙은 신뢰하는 기본 규칙으로 등록**했다. 미적분이나 적분 정리를 엔진에 구현하지 않았다.

| 실행 조건 | 엔진 결과 | 확인한 것 |
|---|---|---|
| 정상 연결 | qed=true | 등록된 규칙을 올바르게 연결 가능 |
| e2 연결 삭제 | qed=false; pm.tilt가 미연결 | 필요한 입력 누락 탐지 |
| e2 대신 재귀 명제를 연결 | qed=false; 해당 연결 failed | 명제 불일치 탐지 |
| 깊이 구별을 지우고 next를 ih로 직접 환류 | qed=false; cycle 1개 | 자기 고리를 귀납으로 자동 해석하지 않음 |
| 근거 없는 무전제 PM 규칙을 의도적으로 등록 | qed=true | 엔진은 등록한 규칙 자체의 미분 정당성을 검증하지 않음 |

선택한 내부 PM 블록만 감싸는 `incredibleNewRule` 호출에서도 입력 5개·출력 2개의 재사용 가능한 블록을 얻었다. 이것은 인터페이스 추출이며 새로운 수학 증명은 아니다. 전체 결과와 엔진 SHA-256은 `incredible-results.json`에 있다.

귀납은 원본의 자기 고리 주석을 그대로 연결하면 안 된다. 고정된 유한 L에서는 깊이별 인스턴스로 펼치거나, 일반 L에서는 기초·귀납 단계의 정당성을 가진 별도 규칙으로 표현해야 한다. 따라서 포트 연결 검사·선택 영역의 블록화는 재사용 후보지만 귀납 어댑터와 한국어/LaTeX 상세·출처·검토 상태는 추가 작업이 필요하다는 판단이다.

## 문서·표현 형식과 대조한 것

### TLAPS

PM의 `문맥 + 입력 ⊢ 출력`은 TLAPS의 국소 proof obligation과 대응한다. 정의 e1/e2는 정의 확장, 사실 e3과 귀납 가정은 명시적 인용, 여섯 계산은 하위 증명 단계에 대응시킬 수 있다. `BY ... DEF ...`는 인용한 사실과 정의로 실제 주장이 따라오는지 검사하는 구조다. [공식 튜토리얼](https://proofs.tlapl.us/doc/web/content/Documentation/Tutorial/A_simple_proof.html), [계층형 증명](https://proofs.tlapl.us/doc/web/content/Documentation/Tutorial/Hierarchical_proofs.html).

대응표는 `tlaps-correspondence.json`에 저장했다. 이는 실행 가능한 TLA+ 파일이 아니다. 현지 PATH에 tlapm은 없었다. PM의 LaTeX를 그대로 검사할 수 있다는 결론은 내리지 않는다. 확률 kernel·미분·적분과 필요한 해석 정리를 형식 언어로 옮기는 비용은 별도로 남는다. 당장 빌려 쓸 핵심은 시스템 설치보다 국소 증명 의무와 명시 입력이라는 규격이다.

### Verso Blueprint

공식 [매뉴얼](https://github.com/leanprover/verso-blueprint/blob/v4.35.0/doc/MANUAL.md)의 definition/lemma_/proof, uses, parent 문법에 맞춰 `PMBlueprint.lean`을 만들었다. 입력·바닥·여섯 줄·두 출력을 14개 비형식 항목으로 옮기고 하나의 group 안에 넣었다. 한국어와 기존 식은 비형식 본문에 보존했다. Lean 검증 코드와 완료 상태는 붙이지 않았다.

이는 문서 출판·의존 관계 표현의 변환 초안이다. 현지 PATH에 Lean/lake가 없어 컴파일·렌더는 하지 않았다. 네이티브 구문으로 작성했다는 것과 도구가 실제로 받아들였다는 것을 구별한다. 우리 edge의 부분 출력 계약은 별도 label의 항목으로 펼쳤으므로 자료 구조가 일대일로 유지되지는 않는다. 문서화 기반 후보로는 유효하지만 이 초안만으로 즉시 전환을 결정할 근거는 부족하다.

### Tinker / PSGraph

공식 [도구 설명](https://ggrov.github.io/tinker/)에 따르면 node는 tactic이고 연결은 goal의 이동 경로다. PM은 하나의 tactic, 여섯 계산은 하위 전략으로 대응시킬 수 있지만, 먼저 각 계산을 실행할 prover 측 tactic이 필요하다. 현재의 수학 진술 graph를 그대로 넣는 JSON 호환 도구로 보기는 어렵다. [설치 문서](https://github.com/ggrov/tinker)는 오래된 Isabelle/Java 환경을 전제로 한다. 설치나 실행은 하지 않았으며, 현 환경에서 동작하지 않는다고 단정하는 것도 아니다. 계층·library 설계의 참고 사례로 남긴다.

## 이번 확인에 따른 권고

1. 현재 JSON을 원본으로 유지하고 큰 구조 변경은 아직 하지 않는다.
2. graph 편집·연결 검사 도입을 추진한다면 **Incredible 포트 모델을 재사용하는 방안**이 이번 후보 중 실행 근거가 가장 구체적이다. 수학 검증 역할과 구별한다.
3. 검증 규격은 **TLAPS식 국소 증명 의무**를 기준으로 대조한다. 형식 증명 도입 여부는 별도 선택이다.
4. 문서화 도구로 전환한다면 **Verso 초안을 실제 컴파일·렌더한 뒤** 화면과 손실된 계약 표현을 확인해야 한다. 현재는 그 단계 전이다.

보고서의 도입 판단은 위 시험과 문서에서의 추론이다. 후보 전체의 기능 부재를 증명한 전수조사가 아니며, 이번에는 기존 graph·도구·공개 사이트를 교체하지 않았다.

## 재현

공개 엔진을 별도로 준비한 뒤 다음을 실행한다. 엔진 파일은 12MB 가량으로 저장소에 넣지 않았다.

```sh
node redesign/proofmap/checks/2026-11-14-existing-tools/run-incredible.cjs /absolute/path/to/logic.js
```

이 실행은 결과 JSON을 다시 쓴다. 현재 검증 결과는 보존되어 있다. 다른 도구의 초안은 실행하지 않았으므로 이 명령의 성공으로 해당 도구들까지 통과했다고 읽지 않는다.
