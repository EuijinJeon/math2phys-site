# 적법성 검사 보고서

카드 244개 (머리말 정상 244개, 잎 195개).

| 검사 | 결과 | 문제 수 |
|---|---|---|
| 형식 (머리말) | 통과 | 오류 0 |
| 정초 | 통과 | 오류 0 |
| 포함 | 통과 | 오류 0 |
| 의존 | 통과 | 오류 0 |
| 대칭 | 경고 | 오류 0, 경고 48 |
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

- 참고: (S1) provides → uses 어긋남 21건, (S2) uses → provides·섹션 표 어긋남 27건. 정의는 check.py `symmetry_warnings` 의 docstring
- 경고: `cavity:section`.provides 가 `x:decor-tree-sampling` 를 가리키지만 `x:decor-tree-sampling` 쪽 uses(조상·자손 포함)에 `cavity:section` 가 없다
- 경고: `model:power-means`.provides 가 `tree:Y-recursion` 를 가리키지만 `tree:Y-recursion` 쪽 uses(조상·자손 포함)에 `model:power-means` 가 없다
- 경고: `models:sat`.provides 가 `model:positivity` 를 가리키지만 `model:positivity` 쪽 uses(조상·자손 포함)에 `models:sat` 가 없다
- 경고: `models:section`.provides 가 `model:factorization` 를 가리키지만 `model:factorization` 쪽 uses(조상·자손 포함)에 `models:section` 가 없다
- 경고: `models:section`.provides 가 `model:positivity` 를 가리키지만 `model:positivity` 쪽 uses(조상·자손 포함)에 `models:section` 가 없다
- 경고: `models:section`.provides 가 `x:model-moment-finiteness` 를 가리키지만 `x:model-moment-finiteness` 쪽 uses(조상·자손 포함)에 `models:section` 가 없다
- 경고: `models:spin`.provides 가 `model:factorization` 를 가리키지만 `model:factorization` 쪽 uses(조상·자손 포함)에 `models:spin` 가 없다
- 경고: `models:spin`.provides 가 `model:positivity` 를 가리키지만 `model:positivity` 쪽 uses(조상·자손 포함)에 `models:spin` 가 없다
- 경고: `pert:factor`.provides 가 `cavity:factor-bounds` 를 가리키지만 `cavity:factor-bounds` 쪽 uses(조상·자손 포함)에 `pert:factor` 가 없다
- 경고: `x:cavity-tree-sampling`.provides 가 `x:decor-tree-sampling` 를 가리키지만 `x:decor-tree-sampling` 쪽 uses(조상·자손 포함)에 `x:cavity-tree-sampling` 가 없다
- 경고: `x:decor-eta-regular`.provides 가 `tree:charging` 를 가리키지만 `tree:charging` 쪽 uses(조상·자손 포함)에 `x:decor-eta-regular` 가 없다
- 경고: `x:decor-mesh`.provides 가 `tree:charging` 를 가리키지만 `tree:charging` 쪽 uses(조상·자손 포함)에 `x:decor-mesh` 가 없다
- 경고: `x:model-cavity-bounds`.provides 가 `reduction:stability` 를 가리키지만 `reduction:stability` 쪽 uses(조상·자손 포함)에 `x:model-cavity-bounds` 가 없다
- 경고: `x:model-hypothesis-remarks`.provides 가 `upper:bound` 를 가리키지만 `upper:bound` 쪽 uses(조상·자손 포함)에 `x:model-hypothesis-remarks` 가 없다
- 경고: `x:model-hypothesis-remarks`.provides 가 `upper:regularization` 를 가리키지만 `upper:regularization` 쪽 uses(조상·자손 포함)에 `x:model-hypothesis-remarks` 가 없다
- 경고: `x:model-moment-finiteness`.provides 가 `upper:bound` 를 가리키지만 `upper:bound` 쪽 uses(조상·자손 포함)에 `x:model-moment-finiteness` 가 없다
- 경고: `x:pert-order-of-choices`.provides 가 `decor:order-of-limits` 를 가리키지만 `decor:order-of-limits` 쪽 uses(조상·자손 포함)에 `x:pert-order-of-choices` 가 없다
- 경고: `x:pert-order-of-choices`.provides 가 `x:decor-limit-order` 를 가리키지만 `x:decor-limit-order` 쪽 uses(조상·자손 포함)에 `x:pert-order-of-choices` 가 없다
- 경고: `x:pert-selected-limits`.provides 가 `x:decor-limit-order` 를 가리키지만 `x:decor-limit-order` 쪽 uses(조상·자손 포함)에 `x:pert-selected-limits` 가 없다
- 경고: `x:tree-cancellation-example`.provides 가 `decor:conditional-concentration.s2.s1` 를 가리키지만 `decor:conditional-concentration.s2.s1` 쪽 uses(조상·자손 포함)에 `x:tree-cancellation-example` 가 없다
- 경고: `x:tree-regular-shape`.provides 가 `x:decor-eta-regular` 를 가리키지만 `x:decor-eta-regular` 쪽 uses(조상·자손 포함)에 `x:tree-regular-shape` 가 없다
- 경고: `decor:conditional-concentration.s3.s1`.uses 의 `x:pert-colored-extensions` 를 `x:pert-colored-extensions`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `decor:overlap-concentration.s2.s1`.uses 의 `x:pert-colored-extensions` 를 `x:pert-colored-extensions`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `pert:factor`.uses 의 `cavity:factor-bounds` 를 `cavity:factor-bounds`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `pert:factor`.uses 의 `x:cavity-root-convention` 를 `x:cavity-root-convention`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `pert:factor`.uses 의 `cavity:negligible` 를 `cavity:negligible`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `pert:factor`.uses 의 `tree:insertion` 를 `tree:insertion`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `pert:palm-expression`.uses 의 `tree:insertion` 를 `tree:insertion`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `pert:palm-expression`.uses 의 `tree:Y-recursion` 를 `tree:Y-recursion`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `pert:palm-expression`.uses 의 `x:tree-extra-variables` 를 `x:tree-extra-variables`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `pert:score`.uses 의 `tree:original-tilt` 를 `tree:original-tilt`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-colored-extensions`.uses 의 `tree:extension-expansion` 를 `tree:extension-expansion`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-colored-extensions`.uses 의 `x:tree-extension-history` 를 `x:tree-extension-history`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-colored-extensions`.uses 의 `tree:multioverlap` 를 `tree:multioverlap`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-increment`.uses 의 `model:hamiltonian` 를 `model:hamiltonian`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-increment`.uses 의 `x:cavity-bounded` 를 `x:cavity-bounded`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-increment`.uses 의 `x:cavity-root-logarithm` 를 `x:cavity-root-logarithm`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-increment`.uses 의 `cavity:increment` 를 `cavity:increment`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-mark-specification`.uses 의 `x:tree-path-kernels` 를 `x:tree-path-kernels`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-mark-specification`.uses 의 `x:tree-sampling` 를 `x:tree-sampling`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-parameter-measure`.uses 의 `x:cavity-root-convention` 를 `x:cavity-root-convention`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-standing`.uses 의 `x:cavity-bounded` 를 `x:cavity-bounded`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-standing`.uses 의 `cavity:grid` 를 `cavity:grid`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-standing`.uses 의 `cavity:increment` 를 `cavity:increment`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-standing`.uses 의 `x:cavity-tree-sampling` 를 `x:cavity-tree-sampling`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-test-setup`.uses 의 `x:tree-sampling` 를 `x:tree-sampling`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:pert-test-setup`.uses 의 `tree:multioverlap` 를 `tree:multioverlap`.provides 도, 양쪽 섹션 표도 가리키지 않는다
- 경고: `x:tree-path-kernels`.uses 의 `model:chain` 를 `model:chain`.provides 도, 양쪽 섹션 표도 가리키지 않는다

## 연결 — 통과

문제 없음.

## 순환 — 통과

문제 없음.

## 사전 — 통과

문제 없음.

## 단면 — 통과

- 참고: 수 7개

## 용어 — 통과

- 참고: 항목 68개, 링크 1045개
