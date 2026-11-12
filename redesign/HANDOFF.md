# 인계 문서

새 세션이 이 작업을 이어받을 때 먼저 읽는 문서. 대화 기록 없이 이 파일과 여기서 가리키는 파일만으로 이어갈 수 있어야 한다.

## 새 세션을 시작하는 법

브랜치 `claude/sharp-feynman-x1cirk`에서 새 세션을 열고 아래를 붙여 넣는다.

> `redesign/HANDOFF.md`를 읽고 이어서 진행해줘. 이 세션은 조율만 하고 작성·검토·도구 작업은 하위 에이전트에 맡겨줘. 로드맵과 진행 기록은 `redesign/ROADMAP.md`에 계속 갱신해줘.

## 무엇을 하는 작업인가

수학 논문 "The Mézard–Parisi formula for diluted spin glasses"를 물리학자가 읽을 수 있는 self-contained 자료로 다시 짓는다. 뼈대는 원문 순서가 아니라 주장들의 의존 그래프다.

| 읽을 것 | 내용 |
|---|---|
| `notes/readability-lessons.md` | 왜 이렇게 하는가: readability의 정의, 축약의 네 유형, 분야별 근거 |
| `notes/redesign.md` | 설계: 노드 카드, 물리판과 수학판, 단면 L0–L4, 재배열 규칙 |
| `notes/method-prompt.md` | 이 작업에서 얻은 일반 방법론. 다른 원문에 같은 작업을 시작할 때 넘기는 프롬프트 |
| `redesign/SCHEMA.md` | 형식 규약: 카드 칸, ID, 규칙 표, 용어집, 용어 규율, 적법성 검사 |
| `redesign/ROADMAP.md` | 단계별 계획, 결정 기록, 날짜별 진행 기록, 시범 결과 |

## 지켜야 할 원칙

1. **세부는 잃어도 참은 잃지 않는다.** 물리 진술이 증명된 것보다 많이 말하면 차이 칸에 적고 유형을 `approximation`으로 한다.
2. **논문이 증명하지 않는 동일시는 이름으로 쓰지 않는다.** Ruelle cascade, Ghirlanda–Guerra, stochastic stability, ultrametricity는 용어집의 물리 대응 칸에 직관으로만.
3. **"상태"는 보조 계층의 깊이 $d$ prefix만 가리킨다.** 물리적 pure state는 그렇게 풀어 쓴다.
4. **기존 사이트의 역할 표(R1–R22)는 쓰지 않는다.** 생성물이지 원문이 아니다. 용어집(`layers/glossary.md`)이 대신한다.
5. **`confirmed`는 사용자만 붙인다.** 작성물은 모두 `proposed`.
6. **작성 → 독립 검토 → 수정자가 원문과 재대조.** 기계 검사는 형식과 포함만 본다. 건전성과 인터페이스 누수는 독립 검토에서만 나온다. 검토자도 틀린다.
7. **윗단면이 부풀면 풀어 쓰지 말고 가리킨다.**

## 작업 방식

- 이 세션은 조율만 한다: 형식 규약을 정하고, 에이전트에 일을 나누고, 결과를 검사하고 통합하고 커밋한다.
- 코딩은 sonnet, 원문을 정독해야 하는 작성은 opus, 독립 검토는 작성자와 다른 모델에 맡겼다.
- 에이전트에게는 쓸 수 있는 디렉터리를 명시하고 git 명령을 금지한다. 커밋과 푸시는 조율 세션이 한다.
- 에이전트 여럿을 한꺼번에 돌리면 사용 한도에 걸릴 수 있다(한 번 걸렸다). 두세 개씩.

## 도구

```
python3 redesign/tools/extract.py                          # source/ → build/graph.json, sentences.json
python3 redesign/tools/check.py --sections decorrelation   # 적법성 검사 → build/check-report.md
python3 redesign/tools/build.py                            # → site/
python3 redesign/tools/export_artifact.py                  # site/ → build/artifact/mezard-parisi.html (게시용 한 파일)
```

- 게시본: https://claude.ai/artifact/1TRCZJL8dEreBp21LLGmhW (비공개). 다른 세션에서 갱신하려면 Artifact 도구에 이 주소를 `url`로 넘긴다.
- 증명 지도 그림 `build/artifact/map.svg`는 헤드리스 브라우저로 미리 그린 것이다. 그래프가 바뀌면 다시 그려야 한다(절차는 ROADMAP 진행 기록의 "게시" 항목).
- 원문 포크 `EuijinJeon/math`(읽기 전용)의 `notes/221-mezard-parisi/`에 사용자의 기존 소절별 노트가 있다. 참고용이고 원문이 우선이다.

## 현재 위치

`ROADMAP.md` 맨 아래 진행 기록의 마지막 항목을 본다. 이 파일의 아래 절은 조율 세션이 단계가 바뀔 때마다 고쳐 쓴다.

### 지금 상태 (2026-11-12)

- 1단계(시범) 완료. 용어집 독립 검토와 반영 완료(68항목). 이름 선택 확정·적용 완료(`build/rename-2026-11-12.md`).
- 2단계 진행 중. 섹션별 상태는 `ROADMAP.md`의 2단계 표가 정본이다.
  - §2 model(25장), §3 trees(39장): 작성 → 독립 검토 → 수정 반영까지 끝. 수정본의 재검토는 하지 않음.
  - §4 upper(10장), §5 cavity(13장): 초안 완료, 독립 검토 중.
  - §6 perturbations: 작성 중.
  - §8 comparison, §9 reduction, §10 consequences, overview.tex: 아직.
- 다음 할 일, 순서대로:
  1. §4·§5 검토 반영(수정자가 원문과 재대조). `build/glossary-additions-upper-cavity.md`의 `g:bounded-law` 합치기.
  2. §6 독립 검토 → 반영. 새 용어 합치기.
  3. §8·§9·§10 작성 → 검토 → 반영. §9는 `main:theorem.s1`–`s4`가 이미 덮는 reduction.tex 45–87을 겹쳐 쓰지 않는다.
  4. overview.tex("Proof strategy") 담당 정하기. 증명 지도(전체 DAG) 다시 그리기, 게시본 갱신.
- 섹션 작성 지시에 넣을 것(이번에 배운 것):
  - 기계 검사는 `\ref` 없는 사용과 같은 파일 안 의존을 잡지 못한다. `uses`는 작성자가 손으로 맞추고 검토자가 손으로 확인한다.
  - 섭동 매개변수는 root 변수가 아니라 고정값이다(cavity.tex 29–31). 여러 작성자가 같은 실수를 했다.
  - 작성 에이전트는 `layers/glossary.md`를 고치지 않고 `build/glossary-additions-<섹션>.md`에 제안한다. 수정자가 합친다.
  - 한도: 에이전트 셋을 동시에 돌리면 5시간 한도에 자주 걸린다(이 세션에서 세 번). 멈춘 에이전트는 SendMessage로 재개한다.

### 사용자가 정한 것

- 역할 표는 새 구조에 넣지 않는다. 제거하거나 새 목적에 맞게 다시 쓴다.
- 용어는 정의가 있어야 하고, 각 용어가 무슨 역할로 쓰이는지 용어집에서 보여야 한다.
- "상태"는 보조 계층의 prefix 이름으로만 쓴다.
- P5(수열 선택)는 당연하지 않지만 증명이 무겁고 진술이 쓰기 좋으므로 물리 규칙과 같은 층에 둔다.
- 이름(2026-11-12, 검토자 권고대로): "prescribed-tree 항등식"으로 통일. "clustering" → "조건부 decorrelation"(`g:conditional-decorrelation`). `g:self-average` → "집중"(`g:concentration`). "선택된 수열" 유지. P8의 주어는 "조건부 공분산". 고전적 GG 요약 삭제. 옛 낱말(clustering, self-averaging, connected correlation)은 해당 용어집 항목의 물리 대응 칸에만 남긴다.
- 2단계 진행("이어서 진행").

### 사용자 확인을 기다리는 것

- 규칙 표 12행의 확정(`layers/rules.md`의 승인 열).
- "branching pattern"을 유지할지 "shape"로 바꿀지(지금은 유지하고 "원문의 shape에 해당" 주석).
- 기존 노트 07-1의 두 문장이 원문보다 강하다는 지적.
