# tools/

표준 라이브러리만 쓴다 (PyYAML이 있으면 쓰고, 없으면 내장 최소 파서). 어느 디렉터리에서 실행해도 된다.

| 스크립트 | 하는 일 | 출력 |
|---|---|---|
| `extract.py` | `source/`의 .tex를 읽어 정리류·절·수식 노드, `\ref`류·`\cite` 간선, 문장 분할을 뽑는다 | `build/graph.json`, `build/sentences.json` |
| `check.py` | 적법성 검사(정초·포함·의존·연결·순환·사전·단면·용어, 그리고 머리말 형식) | `build/check-report.md` (오류가 있으면 종료 코드 1) |
| `build.py` | `layers/`, `cards/`, `graph.json`으로 정적 HTML을 만든다(`glossary.html` 포함) | `site/` |
| `export_artifact.py` | `site/`의 쪽들을 해시 라우팅 한 파일로 묶는다(게시용). `--root`/`M2P_ROOT` 지원 | `build/artifact/mezard-parisi.html` |
| `common.py` | 공유 파서: 카드, 규칙 표, 용어집(`parse_glossary`), R번호·`[[g:…]]` 탐지 | |

## 실행

```
python3 tools/extract.py                        # 원문이 바뀔 때만
python3 tools/check.py                          # 카드가 있는 모든 파일에 포함 검사
python3 tools/check.py --sections decorrelation # 포함 검사 대상을 파일 stem으로 지정 (쉼표 구분)
python3 tools/build.py                          # site/index.html 에서 시작
python3 tools/render_maps.py                     # 한 파일 내보내기에 쓸 SVG 12개
python3 tools/export_artifact.py                 # build/artifact/mezard-parisi.html
```

- `--root DIR`(또는 환경변수 `M2P_ROOT`): `cards/`, `layers/`, `build/check-report.md`, `site/`를 이 디렉터리에서 읽고 쓴다. `source/`와 `build/graph.json`은 항상 실제 것을 쓴다. 시험용 fixture에 쓴다.
- `check.py --out FILE`, `build.py --out DIR`: 출력 위치 지정.
- `render_maps.py --root DIR --mermaid FILE`: 같은 root의 카드에서 지도를 만든다. Node의 Playwright와 Chromium 및 Mermaid 10.9.3이 필요하다. `--mermaid`를 생략하면 `M2P_MERMAID`, root의 vendor, npm 순서로 찾는다. `CHROME`, `NODE_PATH`를 지정할 수 있다. 도중에 실패해도 기존 그림은 유지한다.
- `export_artifact.py --root DIR`: `DIR/site` 및 `DIR/build/artifact/maps`를 읽는다. 현재 카드로 만든 Mermaid 원문과 저장된 `.mmd`를 비교하고 SVG가 없거나 원문이 다르면 중단한다. 같은 원문에 맞춰 생성된 SVG라는 전제이며 SVG 자체의 출처를 검증하지는 않는다. 다른 root의 그림을 대신 쓰지 않는다.
- 격리 시험은 `--root`와 `--out`을 함께 쓴다. export는 항상 `<root>/site`를 읽으므로 build 출력도 거기에 둔다. `python3 tools/tests/test_dependencies.py`는 별도 임시 카드로 섹션 참조의 직접·조상 의존과 누락 경고를 확인한다.
- `cards/`나 `layers/`가 비어 있어도 죽지 않고 "아직 카드 없음"으로 보고한다. 머리말이 깨진 카드는 오류로 기록하고 계속 간다.

## 용어집 (`layers/glossary.md`)

- 형식은 SCHEMA.md의 "용어집". `[[g:slug]]`는 노드 ID가 아니라 용어집 링크이므로 연결 검사에서 노드로 세지 않는다.
- `check.py`의 **용어** 검사: (a) 모든 `[[g:slug]]`(코드 밖; layers 전부와 카드 머리말·본문)가 항목에 있다, (b) 항목마다 뜻·역할·정의 위치가 비지 않았다, (c) 수식·코드 밖에 R1–R22 참조가 없다, (d) 정의 위치의 노드 ID(`접두어:이름`)가 graph.json이나 카드에 있다(경고), (e) 슬러그 중복·깨진 제목은 오류, (f) 어디서도 링크되지 않은 항목은 참고. 용어집이 없고 `[[g:…]]`도 없으면 "해당 없음".
- R번호 탐지: `$…$`, `$$…$$`, `\[…\]`, `\(…\)`, 코드 블록·인라인 코드를 먼저 지운 뒤 `(?<![A-Za-z0-9_\\:/#])R(\d{1,2})(?![A-Za-z0-9_^{(])` 로 찾고 1–22만 센다.
- `build.py`: `[[g:slug]]` → `glossary.html#g-slug` 링크(표제어를 보이고 `title`에 뜻). 모르는 slug는 붉은 물결 밑줄로 표시.
- `export_artifact.py`: 한 파일 안에서는 쪽+앵커를 못 쓰므로 용어 링크를 `href="#glossary" data-term="g-slug"`로 바꾸고, 라우터가 용어집 쪽을 연 뒤 그 항목으로 스크롤하고 2초간 강조한다.

## graph.json 구조

- `nodes`: `section`/`subsection`/정리류(`theorem` … `remark`)/`equation`/`figure`/`label`. 정리류는 `number`("Lemma 7.2"), `lines`(진술), `proof`(첫 증명 범위 또는 null), `proofs`(전부)를 가진다. 라벨이 없으면 id는 `x:<파일>-L<줄>`.
- `edges`: `src`(가장 안쪽 노드), `dst`(라벨), `dst_container`(라벨이 든 정리류/절), `role`(`statement`/`proof`/`text`), `file`, `line`.
- `cites`, `proofs`(어느 노드에도 안 붙은 증명 포함), `labels`.

## 알려진 한계

- 문장 분할은 휴리스틱이다(수식·약어는 보호하지만 완벽하지 않다). 결정적이다.
- 수식 번호는 `\notag`/`\nonumber`/`\tag`까지 반영하지만 `subequations`, `alignat` 열 수 등은 다루지 않는다.
- Mermaid·MathJax는 CDN에서 불러오므로 사이트를 보려면 인터넷이 필요하다.
- `provides`는 자유 서술이며 일부 축약 ID·설명·규칙 번호를 함께 담는다. 따라서 `uses`와의 대칭을 정확하게 기계 검증하지 않는다. 양쪽 연결과 `\ref` 없는 의존은 사람이 대조해야 한다.
