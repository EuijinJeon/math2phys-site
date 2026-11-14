# PoC 5 — 대강 vertex의 국소 확장

2026-11-14. 대상은 `diff.D4`(내부 vertex 항: fresh path)다. **국소 수학적 완결과 구조 검사는 통과했으나, 수정이 최초 vertex의 둘레 안에만 머물지는 않았다.** 정의를 공급하기 위해 상위 1층까지 보충했다. 독립 모델 감사는 하지 않았고, `diff` 전체의 미분 규칙은 아직 미완결이다.

## 무엇을 펼쳤나

하위 graph `fresh`의 입력은 기존 `D1`(로그 밀도의 내부 항), `D2`(첫 변분), `S1`(tree 표본 규칙)에 `XO`(삽입과 protected F 정의)를 더한 네 개다. 안쪽은 다음 세 vertex다.

1. `FP_BIND`: 일반 첫 변분에 beta의 prefix를 대입하여 h=D/A, partial log Y_beta=Q_beta[h]를 얻는다.
2. `FP_EXT`: H=G product_{a in C}1/A^a라 두고, old tree를 먼저 뽑은 뒤 새 path를 적분하여 E_{T+}^A[H h^x]=E_T^A[H Q_beta h]를 얻는다.
3. `FP_PACK`: old gamma_beta를 그대로 곱하고 새 leaf x의 분모를 protected 집합에 넣어 gamma_beta F[T+,C union {x},G D^x]로 재포장한다.

G가 old tree의 여러 가지를 함께 써도 H를 가지별로 분해할 필요가 없다. 필요한 독립성은 old tree가 주어진 상태에서 prefix 아래에 새로 뽑는 path의 조건부 독립성이다. 새 위치 x의 값이 old 값과 같아지는 경우도 허용한다. 미분을 기대값 안으로 옮기는 단계와 leaf 항의 상쇄는 이 vertex의 범위에 넣지 않았다.

## 확장 범위

| 항목 | 결과 |
|---|---|
| 새 하위 graph | 1개 (`fresh`) |
| 새 node | 8개: 외부 4, 안쪽 3, 출력 1 |
| 새 edge | 하위 10 + 부모 정의 edge 1 = **11개** |
| 기존 edge 내용 보충 | diff-e3, diff-e4, diff-e5, diff-e7: **4개** |
| 기존 node 수정 | diff.D4, diff.S1, top.O1 |
| 수정된 기존 graph | `diff`, `top` 두 개 |
| 목표 graph보다 위로 번진 층 | **1층** (`diff`의 부모 `top`) |
| 아래로 새로 연 층 | 1층 (`fresh`) |

처음 세 입력에는 F[T,C,G] 정의가 실려 있지 않았다. 따라서 XO→D4의 `diff-e8`을 추가했고, XO가 상속하는 `top.O1`에 원문 trees.tex 180–183의 F 정의를 보충했다. S1에는 삽입 후의 확률 kernel에서도 같은 표본 규칙을 쓴다는 내용을 명시했다. D4의 출력 형태와 old 계수는 바꾸지 않았다. 그래프의 나머지 `p7`, `fv`, `cp`는 바꾸지 않았다.

변경 전후 node·edge 해시와 개수는 `baseline-inventory.json`, `after-inventory.json`에 저장했다. `results.json`은 수정 id 목록과 확장 수를 담는다. 따라서 “완전히 국소적인 수정으로 끝났다”는 결론은 내리지 않는다. 이번에는 빠진 정의 하나가 상위 1층에 전파되었다는 관측이다.

## 원문 근거

- trees.tex 20–39: prefix, 자식의 조건부 독립, leaf 삭제의 일관성.
- trees.tex 67–82: Y 재귀, 삽입 후 확률 kernel, E^A의 뜻.
- trees.tex 142–154: 일반 첫 변분과 path 평균.
- trees.tex 180–202: protected 집합, F의 기대값, 내부 계수 항, fresh path 재표현과 G가 다른 가지를 쓰는 경우의 정당화.

이 원문 내용을 국소 적분 계산으로 펼쳤다. 유계성과 양의 하한 아래 H와 h가 유계이므로 선언한 바닥의 유한 kernel 적분/Fubini로 충분하다. 별도의 물리적 독립 가정을 넣지 않았다. 상위에서 가져오는 첫 변분·표본 규칙 자체까지 독립 검증한 작업은 아니다.

## 시험

`test_local_growth.py`: **5 tests, OK**.

- 깊이 2의 비균등 kernel, beta에서 두 old 자식, root의 다른 가지에 old leaf 하나를 둔 유한 예제를 전수 합산했다. G는 old sibling과 다른 가지의 spin을 함께 쓰며 C={a}다. t=-0.2,0,0.19,0.4에서 내부 기여와 fresh protected 기대값이 일치했다.
- fresh sampling 확률을 새 tree의 밀도 W(T+)로 따로 계산해 일치함을 확인했다.
- 첫 변분은 중심차분으로도 대조했다.
- old gamma=m−2를 새 gamma=m−3으로 바꾸는 잘못된 계산은 원래 값과 달랐다. 원래 계수 보존을 확인하는 음성 대조다.
- 추가 edge 수, 수정 graph 범위, 외부 입력 집합과 안쪽 완결 상태를 검사했다.

기존 참조 검사 시험 **21개**, 문맥 건넘 시험 **7개**도 통과했다. 원자 vertex 수가 5개에서 8개로 늘어 기존 coverage 기대값만 8로 갱신했다. 검사기 로직을 완화하지 않았다. 전체 구조 검사는 **오류 0·경고 0**이다. HTML과 확대 연결 데이터도 다시 생성했다. 화면의 시각 검증과 독립 수학 감사는 이번에 하지 않았다.

P8/P9 등 다른 PoC의 범위를 확장하지 않았으며 사용자 전용 confirmed를 바꾸지 않았다. 다섯 PoC의 첫 실행은 여기서 끝났다. 다음 판단 재료는 이 전파 비용과 새 vertex의 실제 가독성이다.
