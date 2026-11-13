# 적법성 검사 보고서

카드 244개 (머리말 정상 244개, 잎 195개).

| 검사 | 결과 | 문제 수 |
|---|---|---|
| 형식 (머리말) | 통과 | 오류 0 |
| 정초 | 통과 | 오류 0 |
| 포함 | 통과 | 오류 0 |
| 의존 | 통과 | 오류 0 |
| 대칭 | 경고 | 오류 0, 경고 4 |
| 연결 | 통과 | 오류 0 |
| 순환 | 통과 | 오류 0 |
| 사전 | 통과 | 오류 0 |
| 단면 | 통과 | 오류 0 |
| 용어 | 통과 | 오류 0 |

## 형식 (머리말) — 통과

문제 없음.

## 정초 — 통과

문제 없음.

## 포함 — 통과

- 참고: 대상 섹션(파일): cavity, comparison, consequences, decorrelation, model, overview, perturbations, reduction, trees, upper
- 참고: 카드 244개 중 잎 195개
- 참고: cavity.tex: 필요한 70줄 모두 덮임
- 참고: comparison.tex: 필요한 176줄 모두 덮임
- 참고: consequences.tex: 필요한 99줄 모두 덮임
- 참고: decorrelation.tex: 필요한 476줄 모두 덮임
- 참고: model.tex: 필요한 7줄 모두 덮임
- 참고: overview.tex: 필요한 0줄 모두 덮임
- 참고: perturbations.tex: 필요한 357줄 모두 덮임
- 참고: reduction.tex: 필요한 75줄 모두 덮임
- 참고: trees.tex: 필요한 266줄 모두 덮임
- 참고: upper.tex: 필요한 112줄 모두 덮임

## 의존 — 통과

문제 없음.

## 대칭 — 경고

- 참고: (S1) provides → uses 어긋남 0건, (S2) uses → provides·섹션 표 어긋남 4건. 정의는 check.py `symmetry_warnings` 의 docstring
- 경고: `decor:conditional-concentration.s3.s1`.uses 의 `x:pert-colored-extensions` 를 `x:pert-colored-extensions`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `decor:overlap-concentration.s2.s1`.uses 의 `x:pert-colored-extensions` 를 `x:pert-colored-extensions`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-standing`.uses 의 `cavity:increment` 를 `cavity:increment`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-standing`.uses 의 `x:cavity-tree-sampling` 를 `x:cavity-tree-sampling`.provides 도, 양쪽 섹션 표도 가리키지 않는다

## 연결 — 통과

문제 없음.

## 순환 — 통과

문제 없음.

## 사전 — 통과

문제 없음.

## 단면 — 통과

- 참고: 수 7개

## 용어 — 통과

- 참고: 항목 68개, 링크 1059개
