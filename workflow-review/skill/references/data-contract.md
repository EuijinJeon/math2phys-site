# workflow-review/0.1

`data/review.json`이 검토 자료의 기준이다. 사례(case)는 특정 회고 기록 또는 운영 절차를 뜻하며 실제 실행 ID와 같다고 가정하지 않는다. 현재 사례는 제작 보고와 갱신 절차 두 개다.

- `version`: 게시 데이터 버전. URL의 v가 다르면 경고를 표시한다. 최신 화면만 제공하며 과거 내용은 Git에서 찾는다.
- `documents`: 문서 ID → 저장소 상대 경로, 40자 commit revision, 제목, 당시 원문. 공개 화면은 이 원문 스냅샷을 포함한다.
- `evidence`: 근거 ID → document, 1-based inclusive lines, excerpt, kind. 발췌가 원문과 정확히 일치해야 한다. kind는 report, specification, tool_result, artifact.
- `cases`: id, title, root, kind, description. 사례 간 상세 링크를 금지한다.
- `graphs`: id, case, title, description, nodes, edges, 선택적 parent.
- `nodes`: id, title, summary, body, inputs[], outputs[], position [열, 행], evidence[], status, 선택적 detail(graph ID).
- `edges`: source, target, label, output, input, kind(sequence/data/note). output/input은 출발 노드 출력·도착 노드 입력의 연결별 요약이다. 순서·주석 연결은 직접 데이터 전달을 뜻하지 않는다. 문서에 나타난 서술 순서의 재구성이 실제 타임스탬프를 뜻하지 않는다. v0.1 배치는 왼쪽→오른쪽 그래프에 맞춰져 있다. 순환 실행 시각화는 후속 범위다.
- `parent`: graph와 node. 부모의 detail과 양방향으로 일치해야 한다. 계층 자체에는 순환이 없어야 한다.
- `changes`: date, kind, request, affected[], description. 요청 원문과 변경 의미를 기록한다.

상태: reported(수행 보고), not_done(미수행 명시 보고), specified(규칙에 명시), unknown(확인 불가), observed(직접 실행 기록), verified(결과 직접 확인). v0.1.2에서는 R_SCOPE 관련 호출·반환을 대조한 노드에 observed를 사용한다. 판단 이유에 대한 회고는 reported로 유지한다. 검사기는 직접 근거 없는 승격을 거부하지만 근거 내용의 의미는 별도로 검토해야 한다.

상위 노드와 자식의 상태가 다르면 화면은 mixed로 표시한다. 세부 표현 추가는 상태를 승격시키지 않는다. 원문·근거를 HTML로 실행하지 않고 텍스트로 표시한다.

일반 UI 데이터는 review.json, 개발 진행 데이터는 progress.json에서 관리한다. `tools/build.cjs`가 오프라인으로 열 수 있는 build/index.html, build/progress.html과 PROGRESS.md를 생성한다. 생성물은 직접 편집하지 않는다.
