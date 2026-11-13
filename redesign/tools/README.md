# tools/

표준 라이브러리만 쓴다 (PyYAML이 있으면 쓰고, 없으면 내장 최소 파서). 어느 디렉터리에서 실행해도 된다.

| 스크립트 | 하는 일 | 출력 |
|---|---|---|
| `extract.py` | `source/`의 .tex를 읽어 정리류·절·수식 노드, `\ref`류·`\cite` 간선, 문장 분할을 뽑는다 | `build/graph.json`, `build/sentences.json` |
| `check.py` | 적법성 검사(정초·포함·의존·**대칭**·연결·순환·사전·단면·용어, 그리고 머리말 형식) | `build/check-report.md` (오류가 있으면 종료 코드 1) |
| `build.py` | `layers/`, `cards/`, `graph.json`으로 정적 HTML을 만든다(`glossary.html` 포함) | `site/` |
| `render_maps.py` + `render_maps.js` | 증명 지도(섹션 지도 + 섹션별 지도)의 Mermaid 텍스트를 미리 SVG로 그린다 | `build/artifact/maps/*.mmd`, `*.svg` |
| `export_artifact.py` | `site/`의 쪽들을 해시 라우팅 한 파일로 묶고, 미리 그린 지도 SVG를 끼운다(게시용). `--root`/`M2P_ROOT` 지원 | `build/artifact/mezard-parisi.html` |
| `verify_site.py` + `verify_site.js` | 지은 사이트를 헤드리스 Chromium으로 열어 수식 오류·깨진 링크·390px 넘침·콘솔 오류를 센다 | 표준 출력, `--json` |
| `tests/` | 도구 시험(fixture). `python3 -m unittest discover -s tools/tests -v` | |
| `common.py` | 공유 파서: 카드, 규칙 표, 용어집(`parse_glossary`), R번호·`[[g:…]]` 탐지 | |

## 실행

```
python3 tools/extract.py                        # 원문이 바뀔 때만
python3 tools/check.py                          # 카드가 있는 모든 파일에 포함 검사
python3 tools/check.py --sections decorrelation # 포함 검사 대상을 파일 stem으로 지정 (쉼표 구분)
python3 tools/build.py                          # site/index.html 에서 시작
python3 tools/render_maps.py                    # build/artifact/maps/ 에 지도 SVG
python3 tools/export_artifact.py                # build/artifact/mezard-parisi.html
python3 tools/verify_site.py --build            # /tmp/m2p-site 에 지어서 브라우저 검증
python3 -m unittest discover -s tools/tests -v  # 도구 시험
```

최종 재생성 순서(원문이 안 바뀌었다고 가정): `check.py` → `build.py` → `render_maps.py` → `export_artifact.py` → `verify_site.py --site site` 와 `verify_site.py --artifact build/artifact/mezard-parisi.html`. `build.py` 는 `build/check-report.md` 를 `site/check-report.html` 로 싣고, `export_artifact.py` 는 `site/` 와 `build/artifact/maps/` 를 읽으므로 앞 단계가 먼저여야 한다.

- `--root DIR`(또는 환경변수 `M2P_ROOT`): `cards/`, `layers/`, `build/check-report.md`, `site/`를 이 디렉터리에서 읽고 쓴다. `source/`와 `build/graph.json`은 항상 실제 것을 쓴다. 시험용 fixture에 쓴다.
- `check.py --out FILE`, `build.py --out DIR`: 출력 위치 지정.
- `cards/`나 `layers/`가 비어 있어도 죽지 않고 "아직 카드 없음"으로 보고한다. 머리말이 깨진 카드는 오류로 기록하고 계속 간다.

## 대칭 검사 (`check.py`, 경고만)

SCHEMA는 `\ref` 없는 사용을 받는 쪽 `uses`, 주는 쪽 `provides`, 섹션 카드의 "밖에서 받는 것 / 밖에 내주는 것" 표에 손으로 적으라고 한다. 기계가 `\ref`로 못 잡는 이 세 곳이 서로 맞물리는지 본다. **오류가 아니라 경고**이고 종료 코드에 영향이 없다. `provides` 는 자유 문장이라 읽기가 휴리스틱이다.

- 읽는 법: `provides` 안에 적힌 카드 ID(맨 ID든 `[[id]]`든, 실재하는 카드만)를 "이 카드를 받아 쓰는 쪽"으로 본다.
- 섹션: `kind: section` 카드의 자손 관계로 정한다(`main:theorem` 은 두 섹션에 속한다). 섹션 카드의 자손이 아닌 카드는 첫 `source` 파일을 덮는 섹션 카드에 속한 것으로 본다. 두 카드의 섹션 집합이 겹치면 같은 섹션이라 보지 않는다. 가족 fam(X) = X와 그 조상·자손.
- **S1** `A.provides` 가 다른 섹션의 카드 R 을 가리키는데 fam(R) 의 카드 어느 것도 `uses` 에 fam(A) 의 카드를 갖지 않는다.
- **S2** 카드 B 가 다른 섹션의 카드 A 를 `uses` 에 넣었는데 (a) `A.provides` 가 fam(B) 를 가리키지도, (b) A 의 섹션 카드 머리말·본문이 fam(B) 를 가리키지도, (c) B 의 섹션 카드 머리말·본문이 fam(A) 를 가리키지도 않는다. (b)(c) 가 "표에 적혔다"의 기계적 근사다.
- 예외: `x:overview-*` 는 예고를 `uses` 가 아닌 표로 잇는 약속이라 양쪽에서 뺀다.
- 알려진 오탐: `provides` 가 "예" 나 "근거" 로 다른 섹션 카드를 언급하면(받는 쪽이 아니어도) S1 이 걸린다. 경고를 보고 `provides` 문장을 고치거나 받는 쪽 `uses` 를 보충한다.
- 한 섹션 안의 맞물림은 보지 않는다(카드 수가 많아 소음이 크다).

## 증명 지도: 두 단계, 미리 그리기

- `build.py` 는 `map.html`(섹션 단위 지도)과 `map-<파일 stem>.html`(섹션별 지도)을 쓴다. 섹션별 지도는 그 섹션의 정리류 카드(증명 단계 제외)와, 밖의 섹션과의 연결(섹션당 한 노드, 점선)을 보인다. 지도의 Mermaid 텍스트는 `build.all_maps()` 가 만들고 `build.py`(브라우저가 CDN의 Mermaid로 그림)와 `render_maps.py` 가 같은 것을 쓴다.
- **섹션 단위 지도**: 노드는 섹션 카드와 "주정리" 묶음. 간선은 카드 쌍 단위 `uses` 를 섹션끼리 모은 것이고 숫자가 그 수다. 두 부모를 가진 `main:theorem`(`model:section` 과 `reduction:section` 의 자식)과 그 증명 단계는 한 번만, "주정리" 묶음에만 센다(카드 전체 244장이 한 번씩). 섹션 카드의 `uses` 에서 자손이 쓰는 것은 뺀다(자손 쪽에서 센다). **`remark` 카드와 `x:overview-*` 카드의 `uses` 는 점선("주석 n")** 으로 따로 그리고 순환 판정에서 뺀다. 뒤의 결과를 미리 가리키는 주석이 §2 ↔ §4, §2 ↔ 주정리 같은 가짜 순환을 만들었기 때문이다(카드 단위로는 순환이 없다). 실선만으로는 섹션 단위 순환이 없다. 지도 쪽이 순환 성분이 있으면 적는다.
- `render_maps.py`: `build.all_maps()` 의 텍스트를 `build/artifact/maps/<이름>.mmd` 로 쓰고 `render_maps.js`(노드, Playwright의 헤드리스 Chromium)가 `<이름>.svg` 로 그린다. 이름은 `sections`(섹션 지도)와 `sec-<stem>`(섹션별, 11개, 주정리는 `sec-main`). 옵션: `--root DIR`(카드를 읽을 root), `--out DIR`(그림을 쓸 곳, 기본 `<root>/build/artifact/maps`), `--mermaid 파일`. Mermaid 는 `--mermaid` > `M2P_MERMAID` > `<root>/build/artifact/vendor/mermaid.min.js` > npm에서 `mermaid@10.9.3` 받기 순으로 찾는다(CDN이 막혀도 npm 레지스트리는 열려 있을 수 있다). Chromium 은 `CHROME` 환경변수나 `/opt/pw-browsers` 아래 것을 쓰고 설치하지 않는다. 옛 `build/artifact/map.svg` 가 있으면 지운다(`--out` 을 줬을 때는 건드리지 않는다).
- `export_artifact.py`: `site/` 의 쪽마다 한 `<section id>` 로 묶고 `<pre class="mermaid" data-map="이름">` 자리를 `<out>/maps/<이름>.svg` 로 바꾼다. 그림이 없으면 `build/artifact/maps/` 의 실제 것을, 그것도 없으면 "지도 그림 없음" 안내만 남기고 끝에 이름을 나열한다. Mermaid 스크립트는 한 파일에 넣지 않는다. 지도 SVG의 `click-href` 는 `href` 로 바꾸고 쪽 링크는 `#슬러그` 로 바뀐다. 옵션: `--root DIR`, `--site DIR`(site/ 대신), `--out DIR`(build/artifact/ 대신), `--maps DIR`. **카드나 `build.py` 가 바뀌면 `render_maps.py` 를 다시 돌려야 한다**(그림이 낡는다).

## 브라우저 검증 (`verify_site.py`)

`python3 tools/verify_site.py --build` 는 `build.py --out /tmp/m2p-site` 로 짓고, 모든 쪽을 390px 폭 Chromium으로 열어 (a) `mjx-merror` 와 정의 안 된 매크로(MathJax 3.2는 빨간 글씨 `mjx-mtext` 로 그린다), (b) 깨진 내부 링크(파일과 `#앵커`, Mermaid가 그린 SVG 링크 포함), (c) `scrollWidth > clientWidth`인 쪽(원인 요소 예시 포함), (d) 콘솔 오류·`pageerror`·실패한 요청·HTTP 4xx 를 센다. 풀리지 않은 `$…$`, Mermaid 오류, MathJax 시간 초과도 센다. 문제가 있으면 종료 코드 1, `--json` 으로 쪽별 결과를 저장한다. 옵션: `--site DIR`, `--artifact FILE`(한 파일 내보내기를 쪽(해시)마다 열어 본다), `--only 정규식`, `--jobs`, `--width`.
CDN이 막힌 환경을 위해 MathJax(3.2.2)와 Mermaid(10.9.3)를 npm에서 받아 `/tmp/m2p-verify-vendor`(또는 `M2P_VENDOR`)에 풀고, 브라우저의 CDN 요청을 가로채 그 파일로 응답한다(`--no-local-cdn` 이면 실제 CDN). 수식은 `startup.promise` 와 웹 폰트 로드가 끝난 뒤에 잰다(그 전에 재면 폭이 일시적으로 넘친다). `typesetPromise()` 를 한 번 더 부르면 assistive MathML 이 중첩되어 수치가 왜곡되므로 부르지 않는다.

## 시험 (`tools/tests/`)

`python3 -m unittest discover -s tools/tests -v` (redesign/ 에서; 약 3초, `test_verify` 는 Chromium·npm이 없으면 건너뛴다).

- `fixture.py`: 실제 `source/`와 `graph.json` 위에 임시 `--root` 디렉터리를 만들어 카드를 새로 쓴다(`reduction.tex` 전부와 `comparison.tex` 225–231 등). 실제 `cards/` 를 읽지 않아서 카드 작업과 독립이다. 기준 fixture는 모든 검사를 오류 0·경고 0으로 통과해야 한다.
- `test_check.py`: 기준 통과, 일부러 깨뜨린 카드(uses 누락, 순환·자기 순환·children 순환, 원문 범위 누락, 진술 범위 누락, 범위 밖 줄, source 없음, 없는 uses·children·`[[id]]`, physics인데 gap 없음, 머리말 깨짐, id 중복)와 완화된 의존 규칙(섹션 라벨 참조는 자손이 uses에 있으면 충족, 그러나 그 밖의 참조에는 적용되지 않음), 대칭 검사(S1·S2, 표로 선언, 같은 섹션·overview 예외)를 시험한다. 빈 `cards/` 에서 죽지 않는지도 본다.
- `test_build.py`: 두 부모를 가진 `main:theorem` 의 카드 수(모든 카드가 정확히 한 번), 주석 간선이 가짜 순환을 만들지 않음, 사이트 쪽의 링크, 빈 root 빌드.
- `test_verify.py`: 일부러 깨뜨린 작은 사이트에서 `verify_site` 가 수식 오류·깨진 링크·넘침·콘솔 오류를 세는지.

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

- 의존 검사는 조상 카드의 `uses` 도 충족으로 친다(SCHEMA의 "조상·자손의 `uses`"). 섹션 카드가 하위 카드가 쓰는 것을 전부 나열하면 하위 카드가 `uses` 를 빠뜨려도 잡히지 않는다(`tests/test_check.py::test_ancestor_uses_cover_descendants`). 의존 검사는 경고만 낸다.
- 포함 검사는 증명이 진술과 다른 파일에 있어도(주정리: 진술 model.tex, 증명 reduction.tex) 증명 줄을 요구한다.
- 문장 분할은 휴리스틱이다(수식·약어는 보호하지만 완벽하지 않다). 결정적이다.
- 수식 번호는 `\notag`/`\nonumber`/`\tag`까지 반영하지만 `subequations`, `alignat` 열 수 등은 다루지 않는다.
- Mermaid·MathJax는 CDN에서 불러오므로 사이트를 보려면 인터넷이 필요하다(한 파일 내보내기는 지도를 미리 그려 끼우므로 Mermaid는 필요 없고 MathJax만 필요하다).
- 좁은 화면에서는 줄바꿈 안 되는 긴 인라인 수식이 쪽을 밀어서, `build.py` 의 쪽마다 작은 스크립트가 넘치는 인라인 수식만 블록(안에서 가로 스크롤)으로 바꾼다(`mjx-container.wide`).
