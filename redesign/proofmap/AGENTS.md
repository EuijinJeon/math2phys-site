# AGENTS.md — 증명 유도 지도 작업 입구

AI 도구(ChatGPT, Codex, Claude 등)가 이 폴더에서 일할 때 **이 파일 하나만 먼저 읽는다.** 아래 표에서 요청 종류를 찾아 거기 적힌 것만 읽는다.

## 1. 지금 다루는 것

- 지도: `redesign/proofmap/build/decor-thm-derivation.html`
  논문 §7의 Theorem `decor:overlap-concentration`(모든 multioverlap의 깊이 평균 집중)의 유도. node 34, edge 61. 확대·이동, node 선택 시 조상 강조, 오른쪽 패널에 진술과 원문 행.
- 원문: `redesign/source/sections/decorrelation.tex` (§7, 623행). 밖에서 받는 결과는 `trees.tex`, `perturbations.tex`.
- node·edge 전체 표: `redesign/proofmap/checks/2026-11-16-thm-derivation-map/NODES.md` (생성물)
- 상세 절차(필요할 때만): 같은 폴더 `PROCEDURE.md`

**읽지 말 것** (이 작업에는 필요 없고 길다): `redesign/HANDOFF.md`, `redesign/proofmap/HANDOFF.md`, `redesign/cards/`, `graphs/*.json`, `build/move*.html`, `build/paper.html`.

## 2. 요청별 경로

| 사용자 요청 | 읽을 것 | 고칠 것 |
|---|---|---|
| "node X 설명을 더 해 줘" | `NODES.md` 에서 X의 행 → 그 `src` 의 원문 행만 | HTML의 `N` 배열에서 `id:'X'` 의 `body` |
| "X를 더 잘게 나눠 줘" | 위와 같음 + 이웃 edge | `N` 에 node 추가, `E` 고침, `POS` 에 자리 추가 |
| "이 선이 틀렸다 / 빠졌다" | 양끝 node의 원문 행 | `E` 배열 |
| "대화로 설명만 해 줘" | 위의 읽을 것만 | 고치지 않음. 단, 설명을 지도에 남길지 물어본다 |

사용자가 node를 화면 제목이나 원문 라벨(예: `eq decor:marker-variance-identity`)로 부를 수 있다. `NODES.md` 에서 찾아 id로 바꾼다.

## 3. HTML 안 자료의 형식

`<script>` 안, `const R=String.raw;` 부터 `const COLGAP=` 앞까지가 자료다. **이 범위 밖(배치·보기 코드)은 고치지 않는다.**

```js
const N=[ {id, g, cls, tag, t, f, body, src}, ... ];   // node
const E=[ [보냄id, 받음id, '라벨', 종류], ... ];        // edge. 종류: 'key' | 'note' | 생략(입력)
const POS={ id:[띠, 열], ... };                        // 띠 0 위, 1 아래, 2 밖 node 세로 가운데
```

- `g`: 묶음 `ext` `s71` `s72` `s73` `s74` 또는 `null`. `cls`: `ext` `key` `goal` `note` 또는 생략.
- `t` 제목, `f` node에 보이는 대표식(길면 `<br>` 로 줄 나눔, node 폭 최대 340px), `body` 패널 설명(HTML), `src` 원문 행.
- **TeX가 들어가는 문자열은 반드시 ``R`…` `` 로 쓴다.** `'…'` 에 쓰면 `\eta` 의 백슬래시가 사라지고 `\to` 는 탭이 된다.
- 모든 edge는 열 번호가 커지는 방향(왼쪽→오른쪽)이어야 한다. 같은 칸(띠·열)의 node는 `N` 순서대로 위에서 아래로 쌓인다.
- 정리 증명의 사슬(§7.4 안, 정리로 들어가는 선)은 `'key'`, 정의·보조 결과를 넘기는 선은 종류 생략.

## 4. 내용 규칙 (어기면 안 됨)

1. 원문이 증명한 것보다 많이 말하지 않는다. 원문에 없는 걸음을 채우면 `body` 에 `<p class="warn">작성자 보충: …</p>` 로 표시한다.
2. 원문이 증명하지 않은 동일시(RPC, Ghirlanda–Guerra, ultrametricity, pure state)를 이름으로 쓰지 않는다.
3. 극한 순서: 고정 $L$ 에서 $N\to\infty$ 먼저, 그 뒤 깊이 평균과 $L\to\infty$. 하한은 $\liminf$/$\limsup$ 꼴로만.
4. 원문 용어(anchor, prefix, fresh, extension, multioverlap)는 영어 그대로. 문장은 한국어 평서문("-다").
5. 모든 수정은 `proposed`. 확정은 사용자만 한다.

## 5. 고친 뒤 할 일

저장소 뿌리에서:

```bash
T=redesign/proofmap/checks/2026-11-16-thm-derivation-map
H=redesign/proofmap/build/decor-thm-derivation.html
node $T/tools/check_graph.cjs $H                 # "오류 0" 이어야 끝
node $T/tools/dump_table.cjs  $H > $T/NODES.md   # 표 갱신
```

화면 확인(선택, Playwright 필요): `node $T/tools/render_check.cjs $H <출력폴더> <mathjax@3.2.2 tex-svg.js 경로>`

그리고 아래 6절에 한 줄 적는다.

명령을 실행할 수 없는 환경(파일을 업로드받은 채팅 등)이면: 고친 `N`/`E`/`POS` 부분만 코드 블록으로 돌려주고, 3절 규칙(``R`…` ``, 왼쪽→오른쪽, id 존재)을 스스로 점검했다고 적는다.

## 6. 변경 기록

새 줄을 위에 더한다. 형식: 날짜 · 요청 요지 · 바꾼 id · 원문 밖 보충 여부 · 검사 결과.

- 2026-11-16 · 지도 처음 작성 · 전체 · 보충 1건(`T_C`: $C(S,e)\neq0$ 근거) · check 오류 0
