# §7 정리의 유도 지도: 만든 과정과 다시 만드는 법

2026-11-16. 사용자의 요청: "7장의 그래프에서 multioverlap의 깊이 평균 집중에 대한 derivation 그래프로 그려줘. 확대할수있도록." 그다음 요청: "어떤 과정으로 그래프를 생성했는지 디테일하게 정리해서 똑같이 따라할 수 있게 문서(들)로 만들어줘."

이 폴더는 그 지도를 **같은 방법으로 다시 만들거나 다른 정리에 적용**하기 위한 기록이다.

## 산출물

| 무엇 | 경로 |
|---|---|
| 지도 (한 파일 HTML, 자료·배치·보기가 모두 안에 있음) | `redesign/proofmap/build/decor-thm-derivation.html` |
| 게시본 (비공개, 소유자만 열림) | https://claude.ai/artifact/UUFaUgGGjFnDZZjGZ8Ko6n |
| 처음 만든 커밋 | `9695be6` (브랜치 `ccr-9aa9b310-d8u9tb`) |

지도는 Theorem `decor:overlap-concentration`(decorrelation.tex 63–76)의 유도다. node 34개, edge 61개이고 그 가운데 정리 증명의 주된 사슬(`key`)은 18개다. THM의 조상은 32개다.

## 이 폴더의 문서

| 파일 | 내용 |
|---|---|
| `README.md` | 이 문서. 개요와 빠른 재현 |
| `PROCEDURE.md` | **단계별 절차.** 원문 찾기 → 읽기 → node·edge 고르기 → 자료 쓰기 → 배치 → 보기 → 검사 → 게시. 실제로 겪은 시행착오와 다른 정리에 적용하는 점검표 |
| `NODES.md` | node·edge 전체 표 (생성물. `tools/dump_table.cjs` 로 만든다) |
| `tools/load_graph.cjs` | 지도 HTML에서 자료(`GROUPS`, `N`, `E`, `POS`)를 꺼내는 모듈 |
| `tools/check_graph.cjs` | 구조 검사 (없는 node, 자리 없는 node, 오른쪽으로 가지 않는 edge, 순환, 목표에 닿지 않는 node, TeX 백슬래시 사고, `$` 짝) |
| `tools/dump_table.cjs` | `NODES.md` 생성기 |
| `tools/render_check.cjs` | 헤드리스 Chromium으로 데스크톱·다크·휴대폰 폭을 열고 스크린샷과 수치를 남긴다 |

## 빠른 재현 (지도가 이미 있을 때 검사와 표 다시 만들기)

저장소 뿌리에서:

```bash
T=redesign/proofmap/checks/2026-11-16-thm-derivation-map
H=redesign/proofmap/build/decor-thm-derivation.html

node $T/tools/check_graph.cjs $H            # 기대: "오류 0"
node $T/tools/dump_table.cjs  $H > $T/NODES.md

# 화면 확인 (MathJax를 로컬에 받아 둔다. cdnjs가 열린 환경이면 받지 않아도 되지만 스크립트는 로컬 경로를 요구한다)
mkdir -p /tmp/mj && (cd /tmp/mj && npm init -y >/dev/null && npm i mathjax@3.2.2 >/dev/null)
node $T/tools/render_check.cjs $H /tmp/rc /tmp/mj/node_modules/mathjax/es5/tex-svg.js
# 기대: desk/dark/phone 세 줄 모두 "오류 없음", nodes 34, mathjax 96 안팎
```

`render_check.cjs` 는 Playwright를 쓴다(`require('playwright')`). 이 작업 환경에는 미리 깔려 있었다.

## 상태

- 내용은 작성 모델이 원문과 대조해 옮긴 것이다. **독립 검토는 받지 않았다.** 모든 근거는 `proposed` 다.
- 원문에 없는 걸음 하나를 채웠고 지도에 경고색으로 표시했다: $C(S,e)\neq0$ 의 근거(`PROCEDURE.md` 5.4).
- 게시된 페이지 자체는 열어 보지 않았다. 확인은 로컬 사본으로 했다(`PROCEDURE.md` 8).
- 기존 `graphs/*.json`, 카드, 규칙 표는 고치지 않았다. 이 지도는 proofmap/0.1 JSON 규격을 따르지 않는 **독립 한 장**이다(`PROCEDURE.md` 10.2).
