# 증명 지도 작업 입구

현재 지도: `build/decor-thm-derivation.html` (§7, `decor:overlap-concentration`). `B_CON`, `B_DC`, `DC_ONE`의 세부 지도는 각각 `build/b-con-derivation.html`, `build/b-dc-derivation.html`, `build/dc-one-derivation.html`. 자료 원본은 같은 이름의 `graphs/*.json`이고, 네 페이지는 같은 `viewer/decor-thm-template.html`에서 만든다. 모든 수정은 **proposed**이며 확정은 사용자만 한다.

| 요청 | 읽을 것 | 고칠 것 | 끝낼 때 |
|---|---|---|---|
| “X 단계 설명 더” | `node redesign/proofmap/tools/show_node.cjs X` 출력(원문 행 포함) | 해당 JSON의 X `body` | `make check` |
| “X를 더 잘게” | 위 출력과 아래의 분해 규칙 | `graphs/X.json`과 부모·자식 왕복 링크 | `make check` |
| “선이 틀렸다/빠졌다” | 양끝 node의 조회 출력 | JSON의 `edges` | `make check` |
| 대화로만 설명 | 해당 node 조회 출력 | 없음 | 설명을 저장하라는 요청이면 위 행을 따른다 |

ID는 화면 node와 선택 패널에서 보이며 패널의 **참조 복사**로 복사한다. 제목·원문 라벨만 알면 `NODES.md`에서 ID를 찾는다. 처음부터 긴 `redesign/HANDOFF.md`, `proofmap/HANDOFF.md`, 카드 244장, 큰 `move*.json`과 `paper.json`을 읽지 않는다. 필요할 때만 해당 원문을 더 연다.

## 내용과 분해 규칙

- 원문의 한두 문장을 풀어 쓰면 해당 node의 `body`를 고친다. 독립적인 추론 걸음이 둘 이상이면 별도 JSON 지도를 만들고 같은 보기 틀로 별도 HTML을 빌드한다. 부모 node의 `links`와 자식 지도의 `meta.parent`에 왕복 상대 링크를 둔다. 모바일 패널 안에 그래프를 끼워 넣지 않는다. `B_CON` 페이지가 예시다.
- 원문 밖 보충은 해당 node에 `"supplement": true`와 `body`의 `<p class="warn">작성자 보충: …</p>`를 함께 둔다. 화면에서 경고색으로 보인다. 원문이 증명하지 않은 RPC, Ghirlanda–Guerra, ultrametricity, pure state와의 동일시는 쓰지 않는다.
- 극한은 고정 $L$에서 $N\to\infty$ 먼저, 다음 깊이 평균과 $L\to\infty$. 하한은 $\liminf$/$\limsup$로 쓴다. anchor, prefix, fresh, extension, multioverlap은 영어 그대로 두고 한국어 평서문으로 쓴다.
- JSON의 TeX 백슬래시는 `\\`로 적는다. `make check`가 JSON 문법, node/edge 참조, 열 방향, 순환, 수식 사고를 검사한다. JSON만 편집한다.
- 선택한 node는 `#node=ID` 주소로 다시 열 수 있다. 부모의 `links`에 `{ "label": "…", "href": "자식파일.html" }`, 자식 `meta.parent`에 `{ "label": "…", "href": "부모파일.html#node=ID" }`를 둔다. 공개 URL에서는 링크 복사를 쓴다.

저장소 뿌리에서 `make check`를 실행한다. 검사 오류 0이면 HTML 빌드와 `NODES.md` 표 갱신까지 끝난다. 화면 확인은 선택 사항이며 CDN이 막히면 로컬 MathJax가 필요하다. 요청 한 건마다 `CHANGELOG.md`에 날짜 · 요청 원문 · 바꾼 ID · 원문 밖 보충 여부를 한 줄 추가한다.

질문에서 공개 웹페이지 갱신까지의 명령과 검토 순서는 `checks/2026-11-16-thm-derivation-map/UPDATE-PROCEDURE.md`에 있다. 첫 지도 작성의 기록은 같은 폴더의 `PROCEDURE.md`다.
