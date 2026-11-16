# 노드 질문을 유도 지도와 웹페이지에 반영하는 절차

이 문서는 **이미 있는 지도**의 노드에 대해 “왜?”, “더 자세히”, “선이 잘못됐다”라는 질문을 받았을 때 쓰는 작업 순서다. 처음부터 정리 전체의 지도를 만드는 방법과 당시의 선택은 [PROCEDURE.md](PROCEDURE.md)에 남겨 두었다. 작업의 짧은 입구와 내용 규칙은 [../../AGENTS.md](../../AGENTS.md)가 기준이다. 이 문서는 그 규칙을 실제 명령과 검토 순서로 펼친 것이다.

현재 범위는 §7 정리의 상위 지도 `decor-thm`과 세부 지도 `b-con`, `b-dc`다. 원본 자료는 `redesign/proofmap/graphs/*.json`, 공통 화면 코드는 `viewer/decor-thm-template.html`, 생성물은 `build/*-derivation.html`이다. 아래 경로와 명령은 **저장소 뿌리**에서 실행한다. 수학적 해석은 사용자가 확정하며, 지도 변경은 proposed 상태다.

## 0. 작업 준비와 범위 확정

1. 대상 브랜치와 기존 수정 사항을 확인한다. 다른 브랜치에서 작업 중이면 해당 작업을 덮지 않는다.

   ```bash
   git fetch origin
   git switch ccr-9aa9b310-d8u9tb
   git pull --ff-only origin ccr-9aa9b310-d8u9tb
   git status --short
   cat redesign/proofmap/AGENTS.md
   ```

   Git 작업 공간이 없는 환경에서는 연결된 GitHub 도구로 **같은 브랜치**의 파일과 최신 head를 읽고 변경한다. 현재 checkout이 저장소인지 확인하지 않고 다른 브랜치로 push하지 않는다.

2. 질문을 유형으로 분류한다. “왜 그런가?”는 먼저 근거를 읽어 수학적으로 답한다. 원문의 한두 문장을 풀어 주는 정도면 노드의 `body`를 보강한다. 독립적인 추론 걸음이 둘 이상이면 세부 그래프를 만든다. edge 지적은 양끝 노드와 원문을 대조한다. **대화로만 답해 달라는 요청이면 저장소를 바꾸지 않는다.**
3. 설명의 목표를 문장으로 적는다. 예: “B_DC에서 갈라짐 깊이를 한 칸 늦출 때 왜 평균 제곱 오차가 `C/L`인가?” 이렇게 하면 다른 정리의 물리 해석으로 범위가 번지지 않는다.

## 1. 노드, 이웃, 원문을 찾는다

노드 ID를 알면 한 번에 현재 진술·설명·받고 보내는 edge·원문 행을 출력한다.

```bash
node redesign/proofmap/tools/show_node.cjs B_DC
node redesign/proofmap/tools/show_node.cjs B_DC/DC_ONE
```

ID를 모르면 화면의 node 또는 선택 패널에서 ID를 보고 **참조 복사**를 누른다. 제목이나 원문 라벨만 있으면 `NODES.md`에서 찾는다.

```bash
rg -n 'depth-continuity|깊이에 대한 평균 연속성' redesign/proofmap/checks/2026-11-16-thm-derivation-map/NODES.md
```

1. 출력의 **진술**을 질문과 대조한다. 같은 이름의 다른 식이나 부모/세부 노드를 혼동하지 않는다.
2. **받는 edge**의 선행 결과를 필요한 것만 조회한다. B_DC라면 B_ME의 martingale energy, A_CMP의 regularity 이동, X_SAMP의 prefix 주변법칙을 확인한다. **보내는 edge**를 보면 이 결과를 다음 단계가 어떤 형태로 쓰는지 알 수 있다.
3. `src`의 원문 행을 읽는다. 조회 도구는 긴 범위를 최대 80행까지만 보여 주므로 생략된 부분은 해당 구간만 연다. 원문 증명이 다른 식을 `\eqref`, `\cref`, 이름으로 부르면 그 결과의 진술과 필요한 증명까지 따라간다.

   ```bash
   nl -ba redesign/source/sections/decorrelation.tex | sed -n '168,206p'
   rg -n 'label\{decor:martingale-energy\}|product difference|one-vertex-shift' redesign/source/sections/*.tex
   ```

4. 원문의 **대상과 조건**을 적는다. 무엇을 고정하고(`T_j`의 나중 깊이 등), 무엇을 평균하는지(`q`, `d`, 다른 깊이), 두 양이 같은 prefix/path에서 결합되는지, 상수의 의존 대상, `N\to\infty`와 `L\to\infty`의 순서를 구별한다. 원문이 한 줄로 넘긴 부등식은 실제로 전개해 확인한다.
5. 원문에 없는 새 주장을 써야 한다면 그 사실을 분리한다. 근거 없는 물리적 동일시를 증명의 edge처럼 추가하지 않는다.

처음부터 긴 HANDOFF, 카드 전체, 큰 graph 파일을 읽을 필요가 없다. 조회 출력에서 빠진 **특정** 정의나 원문 행이 있을 때만 읽는 범위를 넓힌다.

## 2. 유도를 먼저 검산하고 node 경계를 정한다

수정 전에 아래 네 칸을 메모하거나 초안에 적는다. 그래프를 그리는 순서보다 이 검산이 먼저다.

| 칸 | 확인할 것 | B_DC의 예 |
|---|---|---|
| 입력 | 정확히 쓰는 선행 결과 | `B_ME`의 제곱 증분 합, 자식 평균의 곱 표현 |
| 변환 | 각 등식·부등식의 이유 | 조건부 Jensen, 곱 차이, 제곱합 |
| 출력 | 이 걸음에서 처음 얻는 결과 | 한 vertex 이동의 제곱 오차, 깊이 평균 `C/L` |
| 조건 | 같은 표본, regularity, 평균 좌표 | 같은 한 단계 continuation, `\eta/2` 영역 |

한 노드의 `body`에 한두 문장을 더하면 끝나는 경우에는 기존 ID를 유지한다. 새 식·대상·부등식이 각각 다음 걸음의 입력이 되는 경우에는 세부 지도에서 **한 결과당 한 node**로 나눈다. B_DC에서는 `DC_ME → DC_EVAL`과 `DC_PROD → DC_ONE → DC_SUM → DC_ALL`을 분리했다. 원문 순서와 의존 순서가 다르면 edge는 의존 순서대로 놓고 각 node의 `src`에 원래 행을 남긴다.

각 edge의 라벨은 “증명에 필요함” 같은 설명 대신 **전달하는 내용**을 짧게 적는다. 원문에 있는 증명과 원문 밖에서 채운 걸음을 구별한다. 후자는 해당 node에 `"supplement": true`와 `<p class="warn">작성자 보충: …</p>`를 함께 둔다. 근거가 부족하면 단정하는 node를 만들지 말고 막힌 지점을 답변에 남긴다.

## 3. JSON만 편집한다

상위 지도 노드의 진술·설명·edge는 `graphs/decor-thm.json`에서 고친다. 기존 세부 노드는 해당 `graphs/b-con.json` 또는 `graphs/b-dc.json`에서 고친다. `build/*.html`의 데이터나 보기 코드를 손으로 수정하지 않는다.

### 3.1 짧은 설명

`body`는 패널의 HTML이며 `f`는 지도 카드의 대표식이다. 원문에서 무엇을 고정하고 어떤 연산으로 결론이 나는지 서술하고, `src`를 실제 원문 행으로 좁힌다. 진술 자체가 달라진 경우에만 `f`도 바꾼다. JSON에서 TeX의 백슬래시는 두 개로 적는다. 예: `"$\\mathbb E\\|D_t\\|_N^2$"`.

HTML 문자열 속에는 원시 `<`를 쓰지 않는다. 예를 들어 `$s<t$`를 `body`에 넣으면 브라우저가 그 뒤를 태그로 해석해 문단이 사라질 수 있다. `$s\\lt t$` 또는 `$s&lt;t$`로 적고 공개 페이지에서 확인한다. 따옴표와 `$…$` 짝도 점검한다.

### 3.2 세부 지도 추가

1. `graphs/b-dc.json`처럼 새 JSON을 만든다. `meta.title`, `meta.description`, `meta.parent={label,href}`, `groups`, `nodes`, `edges`, `positions`, `subgraphs`를 둔다. 세부 node에는 고유 ID, `tag`, `t`, `f`, `body`, `src`, `g`, `col`을 적는다. `positions`는 `[띠, 열]`이고 edge는 **작은 열에서 큰 열**로만 연결한다. 같은 칸의 node는 `nodes` 배열 순서대로 쌓인다.
2. 부모 node의 `links`에 `{ "label": "…", "href": "새파일-derivation.html" }`을, 자식 `meta.parent.href`에 `"decor-thm-derivation.html#node=부모ID"`를 둔다. 모바일 패널 안에 작은 그래프를 끼워 넣지 않는다. Pages 캐시로 복귀한 부모 HTML이 낡게 보이면 `?v=변경식별자#node=부모ID`처럼 쿼리를 **hash 앞**에 두고 새 버전으로 확인한다. 부모가 다시 바뀌면 그 식별자도 갱신한다.
3. `tools/build_decor.cjs`의 `[source, target]` 목록에 JSON/HTML 쌍을 추가한다. 저장소 뿌리 `Makefile`의 `check_graph.cjs <새 JSON> -`와 `dump_table.cjs <새 JSON> > …/새-NODES.md` 행도 추가한다. `show_node.cjs`는 `graphs/`의 세부 JSON을 찾아 조회하고, `check_decor.cjs`는 부모·자식 왕복 링크를 검사한다.
4. `AGENTS.md`의 현재 지도 목록을 한 줄 갱신한다. 세부 지도 추가 사실은 `CHANGELOG.md`에 기록한다.

edge만 고치는 질문이면 양끝 node를 각각 조회하고, 받는 쪽의 원문이 실제로 보내는 결과를 쓰는지 확인한 다음 `edges` 항목과 라벨을 고친다. 새 node를 넣었다면 `positions`와 필요할 경우 `NODES.md` 표도 함께 갱신한다.

## 4. 검사, 빌드, 화면 확인

```bash
make check
git status --short
git diff --check
git diff --stat
git diff -- redesign/proofmap Makefile
```

`make check`가 (1) 상위 구조와 왕복 링크, (2) 각 세부 지도의 구조, (3) 공통 템플릿으로 HTML 빌드, (4) node 표 재생성을 수행한다. **오류 0**이 필수다. 검사기는 ID 중복, edge 끝, 열 방향, 순환, 일부 TeX 사고를 잡지만 **수학적 타당성과 브라우저에서의 실제 조판을 보증하지 않는다.** 생성된 HTML과 표의 의도치 않은 변경을 `git diff`에서 확인한다.

화면에서는 실제 웹페이지에서 대상 `#node=ID`가 선택되는지, 식과 본문이 끝까지 보이는지, 긴 수식이 패널을 깨지 않는지, 모바일 폭에서 선택·스크롤·확대가 되는지 확인한다. 세부 페이지의 **왕복 링크**, 앞뒤 node 링크, **참조 복사/링크 복사**도 확인한다. CDN이 제한된 로컬 환경에서는 HTML을 Chrome에서 파일로 여는 결과를 게시본과 동일하게 취급하지 않는다. 필요하면 [PROCEDURE.md 9.2절](PROCEDURE.md#92-화면-검사)의 로컬 MathJax 렌더 절차를 쓴다.

## 5. 변경 기록과 브랜치 저장

`redesign/proofmap/CHANGELOG.md`에 **요청 한 건당 한 줄**을 쓴다. 날짜, 사용자 요청 원문, 바꾼 ID, 원문 밖 보충 여부, 검사 결과를 남긴다. 예:

> 2026-11-16 · “B_DC 이건 어떻게 유도하지?” · B_DC, DC_ONE, DC_SUM · 원문 밖 보충 없음 · 검사 오류 0

수정한 JSON, 도구, 문서, `make check`가 만든 HTML과 표를 같이 커밋한다. **실제로 검토한 파일만 명시해 stage**하고 다른 작업자의 변경을 포함시키지 않는다. 아래는 B_DC 세부 지도를 처음 추가할 때의 예시이며, 요청에 따라 파일 목록을 바꾼다.

```bash
git add Makefile redesign/proofmap/AGENTS.md redesign/proofmap/CHANGELOG.md
git add redesign/proofmap/graphs/decor-thm.json redesign/proofmap/graphs/b-dc.json
git add redesign/proofmap/tools/build_decor.cjs redesign/proofmap/build/decor-thm-derivation.html redesign/proofmap/build/b-dc-derivation.html
git add redesign/proofmap/checks/2026-11-16-thm-derivation-map/B-DC-NODES.md
git diff --cached --check
git diff --cached --stat
git commit -m "Explain B_DC depth continuity"
git push origin HEAD:ccr-9aa9b310-d8u9tb
```

GitHub 연결 도구만 있는 환경에서는 현재 branch head와 base tree를 읽고, 바뀐 파일로 tree를 만든 뒤 parent가 최신 head인 commit을 생성하고 **expected head를 확인하며** branch ref를 전진시킨다. ref가 바뀌면 최신 상태를 다시 읽고 충돌을 해결한다. 강제 push하지 않는다.

## 6. GitHub Pages에 생성 HTML을 반영한다

이 저장소의 공개 페이지는 **`gh-pages` 브랜치**에서 제공된다. 작업 브랜치의 JSON·HTML을 push하는 것만으로는 공개 URL이 갱신되지 않는다. 게시할 때는 **이번에 바뀐 생성 HTML만** 같은 상대 경로로 복사한다. 아래는 Git CLI 예시다.

```bash
git fetch origin gh-pages
pages_dir=$(mktemp -d)
git worktree add --detach "$pages_dir" origin/gh-pages
mkdir -p "$pages_dir/redesign/proofmap/build"
cp redesign/proofmap/build/decor-thm-derivation.html "$pages_dir/redesign/proofmap/build/"
cp redesign/proofmap/build/b-dc-derivation.html "$pages_dir/redesign/proofmap/build/"
git -C "$pages_dir" add redesign/proofmap/build
git -C "$pages_dir" diff --cached --check
git -C "$pages_dir" diff --cached --stat
git -C "$pages_dir" commit -m "Publish B_DC derivation"
git -C "$pages_dir" push origin HEAD:gh-pages
git worktree remove "$pages_dir"
```

여기서 `b-dc`는 예시다. **실제로 수정된 HTML만** `cp`한다. 작업 브랜치의 `gh-pages`가 아니라 최신 `origin/gh-pages`를 바탕으로 게시한다. push가 non-fast-forward로 거절되면 새 head를 가져와 변경을 재적용한 뒤 다시 push한다. 게시 브랜치에 JSON/원문/검사 문서를 복사할 필요는 없다. GitHub 연결 도구로 게시할 때도 같은 원칙으로 `gh-pages`의 최신 tree에 HTML blob을 넣고 새 commit/ref를 만든다.

GitHub Actions의 **pages build and deployment**가 게시 commit에 대해 성공한 뒤 URL을 확인한다. 예를 들어 `gh run list --branch gh-pages --limit 3` 또는 저장소 Actions 화면에서 게시 commit의 성공을 확인한다. 새 페이지가 잠시 404이거나 이전 설명이 보이면 배포 상태를 먼저 확인하고, `?v=게시커밋` 쿼리를 붙여 캐시를 구별한다. URL 형태는 `https://euijinjeon.github.io/math2phys-site/redesign/proofmap/build/b-dc-derivation.html?v=<게시커밋>#node=DC_ONE`이다. `#node=ID`는 쿼리 뒤에 둔다. 상위·세부 페이지 양쪽을 실제로 열어 왕복 링크가 새 버전으로 연결되는지 확인한다.

## 7. 사용자에게 답한다

대화에는 유도의 핵심 식과 각 부등식의 이유를 **그 자리에서 이해할 수 있게** 설명한다. 무엇을 평균해서 `1/L`이 되는지, 필요한 조건과 원문 밖 보충이 있는지를 분명히 한다. 저장소에 넣었다는 사실, 검사 결과, 공개 페이지의 **검증한 직접 node URL**과 원문 행을 함께 준다. 특정 걸음이 아직 미검증이면 완료했다고 쓰지 않는다.

## 완료 점검표

- [ ] 대상 브랜치와 node ID를 확인하고 `show_node.cjs`로 이웃·원문을 읽었다.
- [ ] 원문의 식·참조·고정 변수·평균 좌표를 따라 유도를 독립적으로 검산했다.
- [ ] `body` 보강 또는 세부 지도 분해를 선택하고 원문 밖 보충을 표시했다.
- [ ] JSON의 수식, node/edge/positions, 부모·자식 왕복 링크를 확인했다.
- [ ] 새 그래프라면 빌드 목록, Makefile, AGENTS, 표 생성 경로를 갱신했다.
- [ ] CHANGELOG에 요청 원문·ID·보충 여부를 한 줄 남겼다.
- [ ] `make check` 오류 0, diff 확인, 작업 브랜치에 커밋·push했다.
- [ ] 바뀐 HTML을 `gh-pages`에 게시하고 Pages 배포 성공을 확인했다.
- [ ] 공개 페이지에서 수식·모바일 배치·노드 선택·왕복 링크를 확인했다.
- [ ] 사용자에게 유도와 검증한 직접 링크를 제공했다.
