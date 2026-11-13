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
| 물리판 | 경고 | 오류 0, 경고 61 |
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

## 물리판 — 경고

- 참고: 절 11개, 단락 231개 중 규칙·링크 없음 61개 (기준: 빈 줄로 나뉜 단락·목록 항목 중 수식·표지를 뺀 글자 12자 이상, 끝이 `:` 인 목록 머리·표·첫 `##` 앞 머리글 제외)
- 참고: 규칙 13개 중 L2 본문이 쓰지 않은 것 0개: 없음
- 경고: L2.md 줄 224 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**목적.** spin weight에 인자 $A$ 를 곱했을 때 root logarithm…」
- 경고: L2.md 줄 226 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**설정(6절 전체가 쓴다).**…」
- 경고: L2.md 줄 230 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- **tree 표본 규칙.** 각 vertex에서 서로 다른 자식은 그 prefix가 주…」
- 경고: L2.md 줄 234 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「로 정하면, 삽입은 root logarithm을 정확히 $\log Y_0$ 만큼 바꾸고 k…」
- 경고: L2.md 줄 240 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「좌변은 삽입이 root logarithm에 준 변화다. 우변의 $k$ 차 항은 leaf가 …」
- 경고: L2.md 줄 242 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**tree 법칙 $Q_k$.** path 하나에서 시작한다. 현재 tree의 leaf가 …」
- 경고: L2.md 줄 246 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**최소 예.** $L=1$ 이면 kernel은 Gibbs 평균 $\langle\cdot\…」
- 경고: L2.md 줄 248 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「이다. 대괄호 안이 $\mathbb E_{Q_2}E_{\mathcal T}[D^1D^2]$…」
- 경고: L2.md 줄 251 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- root가 주어진 조건부 항등식이다. $A$ 는 root가 주어졌을 때 위로 유계이고 …」
- 경고: L2.md 줄 254 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- replica 수 $n\to0$ 의 해석적 연속을 쓰지 않는다. 계층은 무한 계층이 아…」
- 경고: L2.md 줄 255 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $L\ge2$ 에서 $\log Y_0$ 는 보통의 분배함수 비의 로그가 아니다(4.3절…」
- 경고: L2.md 줄 261 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**받는 것 / 넘기는 것.** 받는 것은 6.1의 설정뿐이고 모형은 들어오지 않는다. 넘…」
- 경고: L2.md 줄 268 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- **좌변.** $A_{\boldsymbol t}$ 의 삽입으로 **바뀐 법칙** $E^…」
- 경고: L2.md 줄 273 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $G$ 는 old tree 위 변수의 유계 함수이고 $\boldsymbol t$ 에 의…」
- 경고: L2.md 줄 274 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- **color.** 새로 붙는 replica에 붙인 번호 $1,\ldots,k$ 다. …」
- 경고: L2.md 줄 276 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**extension history와 $c_E$.** old tree에서 시작해 color…」
- 경고: L2.md 줄 283 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- **현재 tree**는 old path 전부(color를 받지 않은 것과 anchor …」
- 경고: L2.md 줄 284 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- **$n_\beta$ 는 그 걸음을 하기 직전 현재 tree에서 $\beta$ 가 가진…」
- 경고: L2.md 줄 285 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- color를 받은 leaf는 다시 고를 수 없고, anchor leaf는 처음부터 고를…」
- 경고: L2.md 줄 286 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- history $E$ 는 이 선택들의 기록이다. $a_j(E)$ 는 color $j$ …」
- 경고: L2.md 줄 287 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- (i)은 $+1$, (ii)는 음수라서 $c_E$ 는 **부호가 섞인다**. 확률 가중…」
- 경고: L2.md 줄 291 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**계산 예 1: old leaf 둘, $k=1$.** old tree가 anchor $a…」
- 경고: L2.md 줄 303 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「좌변을 따로 계산한다. $A=1+t$ 는 상수이므로 모든 깊이에서 $Y_d=1+t$ 이고 …」
- 경고: L2.md 줄 305 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**계산 예 2: $L=1$, anchor 하나.** old tree가 anchor뿐이고 …」
- 경고: L2.md 줄 307 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**factorial.** 위 식은 color의 순서를 어떻게 정해도 성립하고, 좌변의 혼…」
- 경고: L2.md 줄 311 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**목적.** 6.3의 항등식은 "anchor와 새 replica들이 어느 깊이에서 갈라지…」
- 경고: L2.md 줄 317 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「이다. $\operatorname{Br}(S)$ 는 $S$ 의 branching verte…」
- 경고: L2.md 줄 319 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**왜 old tree와 무관한가.** 한 걸음을 본다. 새 color가 깊이 $d$ 의 …」
- 경고: L2.md 줄 324 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- anchor와 새 replica 하나가 깊이 $d$ 에서 갈라지는 모양: branchi…」
- 경고: L2.md 줄 325 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- anchor와 새 replica 둘이 한 vertex(깊이 $d$)에서 세 갈래로 갈라…」
- 경고: L2.md 줄 329 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**목적.** 수 5는 항등식을 $\kappa$ 꼴의 작은 수로 나눈다. 나눈 뒤 오차를 …」
- 경고: L2.md 줄 331 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**왜 필요한가: 상쇄 예.** 예 1의 old tree(anchor와 $a'$ 이 깊이 …」
- 경고: L2.md 줄 337 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「그 $b_{\rm sep}$ 개의 vertex에 대해 $J_{\rm sep}=\prod_v…」
- 경고: L2.md 줄 341 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**무엇이 작고 무엇이 균일한가.**…」
- 경고: L2.md 줄 350 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「상쇄 예에 대면, 깊이 $s$ 처방은 $b_{\rm sep}=0$ 이라 한계가 $C_{q,…」
- 경고: L2.md 줄 352 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**기호 주의.** $b_{\rm sep}$, $J_{\rm sep}$ 는 원문의 $b$,…」
- 경고: L2.md 줄 354 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**성립 범위와 단서 (6.2 전체).**…」
- 경고: L2.md 줄 355 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- ①과 ②는 root가 주어진 조건부로 정확하고, 임의의 유한 kernel 열과 일반 격…」
- 경고: L2.md 줄 356 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $G$ 는 유계이고 old tree의 변수만의 함수이며 삽입 매개변수에 의존하지 않는다…」
- 경고: L2.md 줄 358 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- ②의 $\kappa(S)$ 는 color의 순서와 무관하다. 처방한 split 깊이들은…」
- 경고: L2.md 줄 359 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- ③의 상수 $C_{q,k}$ 는 $L$, 처방한 깊이, 서로 다른 vertex의 깊이가…」
- 경고: L2.md 줄 361 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $c_E$ 와 extension history에는 물리 대응이 없다. 이 전개는 rep…」
- 경고: L2.md 줄 377 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $\mathbb E$ 는 선택된 수열의 reservoir에서 root 평균과 tree …」
- 경고: L2.md 줄 378 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $\mathcal T$ 는 고정한 old tree, $a_*$ 는 그 anchor다. …」
- 경고: L2.md 줄 379 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- **anchor 종류.** 삽입 인자 $1+tg\sigma_i+ug_0S_0$ 에서 $…」
- 경고: L2.md 줄 380 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $k\ge0$ 은 새로 붙이는 color의 수다. **제약** $\mathcal C$ …」
- 경고: L2.md 줄 381 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $\mathfrak E(\mathcal T,a_*,\mathcal C)$ 는 old t…」
- 경고: L2.md 줄 382 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $R_E$ 는 history가 고른 leaf들의 multioverlap이다. spin …」
- 경고: L2.md 줄 384 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**말로.** 첫째 합은 old tree가 있는 자리에서 anchor 옆에 새 replic…」
- 경고: L2.md 줄 389 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- $k=0$, spin anchor. history는 빈 것 하나, 계수 1, $R_E=…」
- 경고: L2.md 줄 390 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- 상쇄 예의 설정($k=1$, spin anchor, old tree는 anchor와 $…」
- 경고: L2.md 줄 392 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「이 된다. 부호 있는 합이 양의 양들 사이의 관계로 바뀌고, 우변에 정규화 $\delta$…」
- 경고: L2.md 줄 394 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**어디서 오는가.** score에서 항등식까지 여섯 단계다. mark specificat…」
- 경고: L2.md 줄 402 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「이다. 마지막 꼴이 6.2 ①의 좌변에서 $G=f\,g_0^{a_*}S_0^{a_*}$ 로…」
- 경고: L2.md 줄 404 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「로 둔다. 입력: 단계 0. 출력: 그 type의 매개변수값에서 $\lvert\Xi_N(t…」
- 경고: L2.md 줄 410 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**단계 4 — polarization: 한 방향에서 여러 방향으로.** 섭동족의 삽입은 …」
- 경고: L2.md 줄 412 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**단계 5 — selector와 site 평균.** $g_0,\ldots,g_k$ 를 m…」
- 경고: L2.md 줄 416 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「**두 매개변수의 역할.** $u$ 로 미분해 집중하는 score를 만들고, $t$ 로 삽…」
- 경고: L2.md 줄 419 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- 고정한 $L$, old tree, anchor 종류, $f$, color 수 $k$, …」
- 경고: L2.md 줄 421 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- mark 깊이는 $1,\ldots,L-1$ 뿐이다. 지정할 수 있는 것은 anchor와…」
- 경고: L2.md 줄 423 절 「6. 수 4 — prescribed-tree 항등식」: 규칙 번호도 [[링크]]도 없는 단락 「- 논문이 이 항등식의 선행 연구로 드는 것과의 관계는 증명되지 않으며 유도에 쓰이지 않는…」

## 용어 — 통과

- 참고: 항목 68개, 링크 1228개
