# AI 업무 검토 지도

완료된 AI 업무를 문서 근거와 함께 검토하는 첫 버전입니다. 기존 증명지도처럼 링크로 상위·세부 지도를 이동하고 원래 노드로 돌아갑니다.

- 온라인: https://euijinjeon.github.io/math2phys-site/workflow-review/
- 진행 상황: https://euijinjeon.github.io/math2phys-site/workflow-review/progress.html
- 로컬: `build/index.html`을 브라우저로 열기. 외부 라이브러리와 서버 없이 동작합니다.
- 개발 기록: [PROGRESS.md](PROGRESS.md)
- 재사용할 스킬: [skill/SKILL.md](skill/SKILL.md). 저장소에 포함된 스킬이며 개인 스킬 디렉터리에 자동 설치하지 않습니다. AI에 이 경로를 지정해 적용할 수 있습니다.

## 작업

저장소 루트에서 `make check-workflow-review`로 검사·빌드합니다. `data/review.json`은 사례와 근거, `data/progress.json`은 개발 진행 상황입니다. `viewer/`는 공통 UI, `build/`는 생성물입니다.

예: `node workflow-review/tools/show-node.cjs creation R_CHECK`

노드의 질문 복사 버튼을 눌러 대화에 붙여 넣으면 대상과 버전, 근거를 지정할 수 있습니다. 화면 자체에 AI 채팅이나 피드백 서버는 없습니다.

## 첫 사례와 한계

PROCEDURE.md의 과거 제작 보고와 UPDATE-PROCEDURE.md의 운영 규칙을 서로 다른 사례로 표시합니다. 원문은 commit에 고정했습니다. 과거 수행 보고를 독립적으로 검증한 것처럼 표시하지 않습니다. 당시 로그·스크린샷은 연결하지 않았습니다.

실행 제어와 자동 로그 수집은 후속 범위입니다. v0.1 URL의 v는 버전 식별과 불일치 알림에 쓰이며 과거 데이터를 온라인에서 재생하지 않습니다. 이전 자료는 Git 이력으로 보존됩니다.

## 게시

GitHub Pages의 최신 `origin/gh-pages`에서 별도 작업 디렉터리를 만들고 `build/index.html`과 `build/progress.html`만 `workflow-review/`에 복사합니다. 기존 페이지를 대체하지 않습니다. 공개 페이지는 공개된 저장소 자료만 포함합니다. 배포 성공과 직접 URL을 확인한 뒤 진행 상황을 완료로 갱신합니다.
