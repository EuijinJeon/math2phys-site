# 형식 규약

`redesign/`의 모든 파일이 따르는 형식. 도구(`tools/`)와 작성물(`cards/`, `layers/`)이 이 문서로 맞물린다.

## 디렉터리

| 경로 | 내용 | 만드는 주체 |
|---|---|---|
| `source/` | 원문 .tex (수정 금지) | 복사 |
| `cards/` | 노드 카드, 노드당 파일 하나 | 작성 |
| `layers/` | 단면 문서: `L0.md`, `L1.md`, `rules.md`, 이후 `L2.md` | 작성 |
| `build/` | 추출 결과: `graph.json`, `sentences.json`, `check-report.md` | `tools/extract.py`, `tools/check.py` |
| `site/` | 생성된 HTML | `tools/build.py` |
| `tools/` | 스크립트 | 작성 |

## 노드 ID

- 원문에 `\label`이 있는 노드는 그 라벨이 ID다. 예: `decor:overlap-concentration`.
- 증명 단계 노드는 부모 ID에 `.s1`, `.s2`, …를 붙인다. 더 내려가면 `.s2.s1`.
- 라벨 없는 노드(작성자가 새로 묶은 것)는 `x:<섹션 접두어>-<짧은 이름>`. 예: `x:decor-limit-order`.
- 파일 이름은 ID에서 `:`를 `.`로 바꾼 것 + `.md`. 예: `cards/decor.overlap-concentration.md`.

## 카드

YAML 머리말 + 자유 본문(markdown). 수식은 `$...$`, `$$...$$`.

```yaml
---
id: decor:overlap-concentration
kind: theorem            # theorem | proposition | lemma | corollary | definition | remark
                         # | assumption | step | device | convention | section
title: 모든 multioverlap의 집중
uses: [pert:tree-identity, decor:conditional-concentration]   # 이 노드가 쓰는 노드 ID
provides: "§8에서 site 표지를 독립 사본으로 바꾸는 근거"        # 누가 무엇에 쓰는지 한 줄
math: |
  정확한 진술. 필요하면 약화하되 틀리면 안 된다.
physics: |
  물리 언어의 대응 진술. 대응이 없으면 null.
gap: |
  physics와 math가 어긋나는 곳, 유효 범위. physics가 null이면 null.
abstraction: approximation   # exact | weakening | blackbox | approximation | intuition
children: [decor:overlap-concentration.s1, decor:overlap-concentration.s2]   # 펼침. 잎이면 []
source:
  - {file: decorrelation.tex, lines: [63, 83]}    # 진술의 원문 범위 (1부터, 양끝 포함)
  - {file: decorrelation.tex, lines: [526, 612]}  # 증명의 원문 범위
status: proposed         # proposed | confirmed | unverified
---
```

칸별 규칙:

- `uses`: 진술이나 증명이 실제로 기대는 노드만. 섹션 범위의 약속(예: "이 섹션 내내 $m_d=d/L$")에 기대면 그 약속을 `convention` 노드로 만들어 여기에 넣는다.
- `math`: `uses`에 든 노드와 용어집만으로 읽혀야 한다. 다른 카드의 본문에 기대지 않는다.
- `abstraction`: `physics` 문장이 `math`에 대해 갖는 관계.
  - `exact` 같은 내용의 다른 표기
  - `weakening` 덜 말하지만 정확함
  - `blackbox` 진술은 정확하고 증명만 숨김
  - `approximation` 유효 범위 안에서만 맞음 (`gap` 필수)
  - `intuition` 논증에 쓰이지 않는 그림
- `children`: 3–7개를 목표로 하되 논리적 경계가 우선이다(짧은 증명은 2개도 된다). 각 child는 자기 카드를 가진다.
- `physics`가 null이면 `gap`은 null, `abstraction`은 `blackbox`로 둔다.
- 증명 안의 식 라벨을 다른 노드가 인용하면, 인용하는 쪽 `uses`에 그 식을 담은 단계 카드를 넣는다.
- `source`: 모든 카드는 원문 범위에 닿아야 한다. 잎 `step`의 범위를 합치면 부모 증명 범위를 빠짐없이 덮어야 한다.
- `status`: 작성자는 `proposed`로 둔다. `confirmed`는 사용자만 붙인다.

본문에는 칸에 안 들어가는 메모, 그림, 검증 기록을 쓴다. 다른 노드를 가리킬 때는 `[[id]]`.

## 규칙 표 (`layers/rules.md`)

물리판이 증명 없이 쓰는 명제들. markdown 표 하나, 열은 고정:

| 열 | 내용 |
|---|---|
| `rule` | `P1`, `P2`, … |
| `물리 규칙` | 물리 언어 한 문장 |
| `수학 노드` | 대응하는 노드 ID (여럿이면 쉼표) |
| `차이` | 어긋나는 곳, 유효 범위 |
| `유형` | `abstraction` 값 |
| `상태` | `proposed` / `confirmed` |

## 단면 문서 (`layers/L0.md`, `L1.md`)

- `L0.md`: 한 문단. 결과와 의미.
- `L1.md`: 한 쪽. 번호 붙은 수(move) 목록. 각 수는 "무엇을 하는가 / 어떤 규칙(P번호)을 쓰는가 / 어떤 노드가 근거인가(`[[id]]`)"를 가진다.
- 두 문서 모두 첫머리에 전제하는 배경(바닥)을 한 줄로 선언한다.
- 쓰이는 기호는 그 문서 안에서 정의하거나 역할 표(R-ID)를 가리킨다.

## 적법성 검사 (`tools/check.py`)

| 검사 | 통과 조건 |
|---|---|
| 정초 | 모든 카드에 `source`가 있고 범위가 실제 파일 안에 있다 |
| 포함 | 대상 섹션에서 증명의 모든 줄이 어떤 잎 카드의 `source`에 들고, 정리류 진술의 모든 줄이 어떤 카드(보통 그 정리 카드 자신)의 `source`에 든다 |
| 의존 | 카드의 `source` 범위 안에 나오는 `\ref`류가 가리키는 노드가 `uses`(또는 조상·자손의 `uses`)에 있다. 본문에서 원문상 뒤에 나오는 대상을 가리키는 참조는 예고이므로 제외한다 |
| 연결 | `uses`, `children`, `[[id]]`, 규칙 표의 수학 노드가 모두 존재하는 ID다 |
| 순환 | `uses` 그래프에 순환이 없다 |
| 사전 | 규칙 표의 모든 행에 수학 노드와 차이가 있다. `physics`가 있는 카드는 `gap`과 `abstraction`이 있다 |
| 단면 | `L1.md`의 모든 수가 규칙이나 노드를 하나 이상 가리킨다 |
