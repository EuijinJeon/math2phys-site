# 그래프 작업 기록 하네스 0.1

로컬 명령 기록기 + 기록 검사기 + 계층별 검토 화면 + 생성/수정 파일럿을 구현했다. Node.js 18 이상과 Git을 사용한다. 별도 패키지 설치는 없다. `DESIGN.md`는 전체 목표이며 이 README는 실제 구현 범위를 설명한다.

## 바로 시험하기

저장소 뿌리에서:

```bash
make check-graph-harness
node workflow-review/harness/tools/pilot.cjs
```

파일럿은 실행마다 `harness/.local/pilot-<시각>/` 아래에 생성 run과 수정 run, 대상 graph.json을 만든다. 명령이 출력하는 각 `review.html`을 열면 전체 과정 → 단계 → 호출·반환·스냅샷을 확인할 수 있다. 로컬 파일 열기가 제한된 브라우저에서는 해당 파일럿 디렉터리만 임시 로컬 서버로 제공한다. 공개 사이트에 올리지 않는다.

파일럿은 **사전 작성한 예제**다. 실제 명령을 실행하고 실제 반환을 저장하지만 LLM이 자율적으로 그래프를 설계하는 시험은 아니다. 생성 후 수정 과정에 잘못된 edge를 의도적으로 넣고 검사 실패 → 복구 → 재검사를 남긴다. 원문 파일과 graph-tool.cjs도 실행 시작 시 스냅샷을 저장한다.

## 실제 작업에 사용하는 순서

CLI는 `node workflow-review/harness/tools/record.cjs 명령 RUN_DIRECTORY SPEC.json` 형식이다. spec은 JSON 파일이다. 공개하거나 Git에 추가할 자료와 분리해 `.local/` 안에 둔다. 명령 자체도 로그에 남으므로 토큰이나 비밀 값을 인자로 전달하지 않는다. 기록기는 명령의 권한을 부여하거나 사용자 승인 절차를 대신하지 않는다.

1. `init`: 아래 run 양식을 저장해 실행한다. run 디렉터리는 없어야 하며 상위 디렉터리는 미리 만든다.
2. `start`: 실행 **전** 목적·입력·완료 조건을 기록한다. file 입력은 실제 바이트 스냅샷으로 저장된다.
3. `exec`: 실제 명령을 argv 배열로 실행한다. shell 치환을 사용하지 않는다. 입력·수정할 파일을 files에 명시하면 전후 스냅샷을 저장한다. 반환 event ID를 확인한다. 실패하면 CLI도 0이 아닌 종료 상태를 반환한다.
4. `finish`: 실제 event ID를 참조해 출력과 판단을 기록한다. 실패한 호출의 step을 completed로 종료할 수 없다. 실패 step을 남기고 새 ID/attempt/retry_of로 다시 시도한다.
5. `check RUN`: 사건 쌍·참조·해시·완료 상태를 검사한다. 미종료 호출/단계는 경고하고 CLI는 실패한다.
6. `close`: summary와 delivery를 기록한다. 구조 검사 성공을 내용 검증·게시 성공으로 바꾸지 않는다.
7. `node workflow-review/harness/tools/review.cjs RUN`: 검토 JSON과 HTML을 생성한다. 생성물에 비공개 원문·명령·반환이 포함되므로 로컬 전용이다.
8. 설명 정정은 `annotate`로 기존 event ID와 text를 추가한 뒤 검토 화면을 재생성한다. 원래 event를 수정하지 않는다.

## JSON 양식

run (`init`):

```json
{"id":"graph-create-001","mode":"create","request":"작은 그래프를 만든다","cwd":"/absolute/workspace","files":["source.md","graph.json"],"domain_rules":"사용한 규칙의 버전 또는 스냅샷 참조"}
```

step (`start`):

```json
{"id":"READ","title":"원문 읽기","purpose":"노드 분해의 근거 확보","done_when":"대상 구간과 생략 범위 확보","inputs":[{"label":"입력 원문","file":"source.md"}]}
```

command (`exec`):

```json
{"step":"READ","argv":["cat","source.md"],"files":["source.md"],"timeout_ms":30000}
```

step 종료 (`finish`; e3은 예시이며 실제 exec 반환 ID로 바꾼다):

```json
{"id":"READ","status":"completed","summary":"반환된 본문을 다음 설계의 근거로 지정함. 내용 타당성 검증은 별도.","outputs":[{"id":"source-text","label":"원문 텍스트","kind":"artifact","event":"e3","channel":"stdout"}],"evidence":["e3"],"affected":[]}
```

후속 step의 inputs는 `[{"label":"읽은 원문","from":{"step":"READ","output":"source-text"}}]`로 앞 출력을 참조한다. 이 연결은 작성자가 지정한 의존 관계이며 프로그램이 LLM의 인지적 사용을 관찰한 것은 아니다. 도구 없이 설계만 기록하면 output의 kind는 `agent_report`다. 파일 산출물은 channel 대신 `file:"graph.json"`과 해당 반환 event를 지정한다. `affected`에는 대상 그래프의 수정 node/edge ID를 적는다.

`close` 예: `{"summary":"생성과 구조 검사 완료","delivery":{"published":false,"content_review":"미실시","screen_review":"미실시"}}`.

`annotate` 예: `{"target":"e4","text":"이 선택의 설명을 보강함. 원래 명령·반환은 유지."}`.

## 사실의 범위

- recorder 사건은 이 래퍼가 실행한 명령에 한한다. provider call ID는 없으며 임의로 만들지 않는다. 브라우저·앱·직접 편집 호출, 래퍼 밖 명령은 자동 수집하지 않는다.
- 목적·판단·영향 ID·입출력 의존 관계는 agent_report다. 파일 전후 스냅샷과 실제 명령 반환은 recorder 자료다.
- 출력은 명령당 16 MiB 제한이다. 초과 시 truncated/error를 남긴다. timeout과 signal도 보존한다. 프로세스 강제 종료로 반환이 없으면 미완료로 남고 검사기가 경고한다.
- writer lock으로 동시 기록을 거부한다. 프로세스가 강제 종료돼 lock이 남으면 다른 writer가 없음을 확인한 후 그 lock만 수동 제거한다. 누락 반환을 만들어 채우지 않는다.
- 해시 체인은 우발적 변경과 누락 탐지용이다. 서명·외부 감사 또는 악의적 재작성 방지 기능은 아니다.
- base commit과 tracked diff를 저장한다. 지정하지 않은 untracked 파일, 전체 환경 변수, 설치 패키지 전체는 보관하지 않는다. 지정 파일과 명령을 재확인할 수 있지만 완전한 실행 환경 재현을 보장하지 않는다.
- annotations는 v0.1에서 별도 파일 대신 같은 append-only event stream에 저장한다. `review.json`은 현재 별도 `graph-work-review/0.1` 투영 형식이다. 기존 공개 workflow-review JSON과의 통합 어댑터는 후속 작업이다.
- 자동 재실행, 게시, 현재 Codex 도구의 전면 가로채기, 수학 내용 자동 검증은 구현하지 않았다.

## 독립 세션 시험

새 세션에 이 README와 `DESIGN.md`를 읽게 한 뒤 다음 과제를 준다:

“예제와 다른 작은 그래프를 새로 만들고 edge 하나를 수정하라. 모든 작업 단계를 실행 전에 start로 기록하고, 관련 로컬 명령은 exec를 거쳐 실행하라. 원문·실행 도구·대상 그래프를 스냅샷으로 남겨라. 판단은 보고로 구별하고 실제 반환 ID로 출력 참조를 연결하라. check와 review를 실행하고 기록만으로 재구성되지 않는 부분을 보고하라. raw 기록은 공개하지 말라.”

독립 세션 시험은 아직 수행하지 않았다. 사용자에게 보여 줄 항목은 대상 그래프, 두 run의 review.html, 검사 결과, 수집에서 빠진 작업 목록이다.
