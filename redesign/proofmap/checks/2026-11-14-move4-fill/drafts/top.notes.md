# top graph edge 초안 — 대조 기록과 판정

2026-11-14. 범위는 graph `top`의 edge 내용이다. 확인한 것은 원문 줄을 직접 읽고 대조한 것이고, 추론은 "추론"이라고 적었다. 기존 파일은 고치지 않았다. 산출물은 `top.json`(교체용 top graph), `top.edge-labels.json`, 이 문서, 시험용 사본 `top.trial.json`이다.

## 0. 검증 결과

- `python3 redesign/proofmap/tools/check.py redesign/proofmap/checks/2026-11-14-move4-fill/drafts/top.trial.json` → 오류 0, 경고 10. 경고 10개는 원본의 `[OUTPUT_CONTRACT] ... 재검토 필요` 10개와 같다(diff-e4, fv o1·f2·f4, cp b0·s0, fresh fp-first, diff.D2, fv.TM, fv.PM). 새 경고 없음. 검토 지문과 `proof_review`는 건드리지 않았다.
- 시험용 사본에서 `top` 밖의 graph, 문서 머리 필드, node O1·R1·R4, edge `top-e9`는 원본과 같다(코드로 비교해 확인).
- `build_viewer.py`로 시험용 사본을 임시 위치에 생성해 오류 없이 만들어짐을 확인했다. 화면은 보지 않았다.
- top의 안쪽 node는 7개로 그대로다(기준 9).

## 1. 고친 node 필드 (edge 밖)

- R2, R3, F1, F2: `status: "sketch"` 추가.
- F1, F2: `inputs` 에 `O1` 추가(`["R3","O1"]`). 새 edge top-e16, top-e17 이 O1 → F1/F2 로 들어온다.
- XM6: `inputs` 를 `["R2"]` 로 채웠다. top-e12 가 이미 들어오는데 목록이 비어 있었다. 이 항목은 요청 범위 밖일 수 있어 통합 담당이 되돌려도 된다. 되돌려도 check.py 결과는 같다(추론: 입력 목록은 viewer의 "입력 edge 없음" 진단에만 쓰인다).
- O1, R1, R4 와 top-e9 는 바꾸지 않았다.

## 2. edge별 대조한 원문 줄 범위

| edge | 대조한 줄 | 비고 |
|---|---|---|
| top-e1 O1→R1 | trees.tex 16–23, 29–39, 67–82, 92–110, 142–154, 180–183 | O1 진술 전체를 싣는다. R1의 하위 graph `diff`의 XO가 O1 진술 전체를 상속하고 diff-e1/e8/e9 가 그 부분을 쓴다 |
| top-e2 R1→R2 | trees.tex 178–202, 242–253 | R1의 일반 진술. 대입은 R2의 몫 |
| top-e3 R1→R3 | trees.tex 178–202, 298–304 | 같은 일반 진술. 대입은 R3의 몫 |
| top-e4 R3→F1 | trees.tex 259–276 | history 정의와 계수 |
| top-e5 R3→F2 | trees.tex 259–276 | 같은 정의 |
| top-e6 R3→R4 | trees.tex 156–176, 259–304; perturbations.tex 391–398, 478–492 | 전개, 순서 무관, $1/k!$, factorial 없음, 균일 해석적 경계 |
| top-e7 XP5→R4 | perturbations.tex 75–93, 255–267, 301–312, 538–546; decorrelation.tex 4–7 | (ii), (iii)와 $e_{\nu,N}$ 의 정의 |
| top-e8 XFAM→R4 | perturbations.tex 26–70, 538–546 | mark specification, type, Poisson, $\psi_\nu$ |
| top-e10 F1→XM5 | trees.tex 337–386; decorrelation.tex 332–334, 414–423, 546–549 | 한 걸음 총합과 $\kappa(S)$ |
| top-e11 F2→XM5 | trees.tex 388–456; decorrelation.tex 332–359, 456–457 | 절댓값 합과 상대 한계 |
| top-e12 R2→XM6 | trees.tex 204–256; comparison.tex 123–129, 195–222 | $\log Y_0$ 급수, $Q_k$, 나머지 |
| top-e13~e17 | 아래 3절 | 새 edge |

옛 edge의 `fit`·`substitution` 문장을 원문과 대조했고 모두 원문과 어긋나지 않았다. 그 내용이 이제 놓일 곳은 다음과 같다. e2의 fit(첫 path의 leaf가 이미 protected, 이후 fresh만 남고 계수의 절댓값을 정규화한 것이 $Q_k$ 의 확률, trees.tex 242–253)은 R2의 하위 graph. e3의 fit는 R3의 하위 graph(298–304). e4의 fit(reference가 없는 부분 tree의 합이 telescoping으로 $m_{d+1}$, 366–371)은 F1의 증명. e5의 fit(떨어진 vertex는 fresh로 갈라져야 하고 계수 $-\delta$, 424–445)은 F2의 증명. e6, e7, e8의 fit는 p7(T1, T2, T3, P1, P2). e10, e11의 fit는 받는 쪽(decorrelation.tex 332–359). e12의 fit는 받는 쪽(comparison.tex 205–213).

## 3. 새 edge와 이유

`inputs` 목록과 실제로 들어오는 edge를 맞춘 결과 다음이 비어 있었다.

| edge | 입력 | 이유 |
|---|---|---|
| top-e13 O1→R2 | R2.inputs 에 O1 있음, edge 없음 | R2의 진술이 $Y_0$ 재귀, $E_{\mathcal T}$, $\gamma_\beta$, $n_\beta$ 를 쓰고, R1 규칙을 부르려면 $F[\mathcal T,C,G]$ 의 뜻이 필요하다 |
| top-e14 O1→R3 | R3.inputs 에 O1 있음, edge 없음 | R3의 진술이 $E^{A_{\boldsymbol t}}_{\mathcal T}$, $E_{\mathcal T_E}$, $\gamma_\beta$ 를 쓴다 |
| top-e15 O1→R4 | R4.inputs 에 O1 있음, edge 없음 | R4/p7이 $W_{\mathcal T}(A)$, 재귀 $Y$, $E^A_{\mathcal T}$, 새 변수를 쓰는 삽입(perturbations.tex 331–337)을 쓴다 |
| top-e16 O1→F1 | F1.inputs 에 없음(추가) | F1의 진술이 $m_d$, 깊이 $d_v$, 자식 수 $a_v$ 를 쓰고 e4가 실은 history 정의가 $\gamma_\beta$, $n_\beta$, $d_\beta$ 를 쓴다 |
| top-e17 O1→F2 | F2.inputs 에 없음(추가) | 같은 이유(F2는 $\delta$, $m_d$, $\gamma_\beta$ 를 쓴다) |

R1의 입력 O1은 이미 top-e1 이 연결한다. XM5의 입력 R4, F1, F2 는 e9, e10, e11 이 연결한다. XP5, XFAM, XM6 의 상류(수 3, 4.2절)는 top 안에 node가 없다.

`top-e13`~`e17` 은 모두 `kind: definition`, `status: connected`, `complete: true` 이다. 내용은 O1의 진술(trees.tex 해당 줄)을 부분집합으로 옮긴 것이다. 단 5절의 "O1에 없는 것"은 원문에서 옮겼다.

## 4. complete:false 로 남긴 edge

없다. 11개 edge 모두 원문 줄에서 내용을 확정했다. 다만 다음은 **edge 쪽이 아니라 보내는 node 쪽의 공백**이다. 그 공백이 있는 동안 해당 vertex는 완결이 아니다(R2, R3, F1, F2 는 sketch).

1. R2가 첫 걸음에 쓰는 첫 변분 $\partial_{t}\log Y_0=E^A[D/A]$ (trees.tex 242–244)는 R1의 출력이 아니다. R1의 하위 graph `diff.D2` 의 출력(`kernel_form`)이고 R1 내부에서 D4로만 간다. top-e2 는 R1의 출력(규칙)만 싣는다. 제안: (a) R1에 둘째 출력을 열어 R1→R2 edge가 싣게 하거나 (b) 첫 변분을 top의 독립 fact node로 올려 O1에서 받아 R1과 R2 모두에 보낸다. (b)는 안쪽 node를 8개로 만든다. 이번에는 세우지 않았다.
2. 복소 $A$ 로 확장한 재귀(주 가지 거듭제곱)와 해석적 경계(trees.tex 156–176)가 O1의 진술에 없다. R3의 출력(top-e6에 실었다)과 R2의 급수 수렴("Analyticity proves", 254)이 이것에 기댄다. 어느 node도 이 경계를 증명하거나 입력으로 받지 않는다. 제안: R3의 하위 graph에서 증명하되 O1에서 복소 재귀 정의를 받는다.
3. telescoping 항등식 $\sum_\beta(n_\beta m_{d_\beta+1}-m_{d_\beta})=n$ (204–208)은 R2의 $Q_k$ 정규화(218), F1의 증명(366–371), F2의 증명(418–421)이 쓴다. 어느 node도 출력하지 않는다. $\gamma_\beta$ 의 정의에서 나오는 대수라 O1의 하위 사실로 보는 편이 낫다(추론).
4. tree:regular-shapes (trees.tex 458–525, $Q_k$ 아래 비정규 tree의 확률 $\le C_k(\eta+L^{-1})$)는 수 6이 comparison.tex 141 에서 R2의 $Q_k$ 위에서 직접 쓴다. top에 이 lemma에 해당하는 node가 없다. top-e12 는 이것을 싣지 않는다고 not_carried 에 적었다. 제안: R2 뒤에 fact node를 두고 XM6 로 edge를 단다. 안쪽 node가 8개가 된다.

## 5. 문맥 → edge 판정 (문맥은 지우지 않았다)

- **FA** ("깊이 $L$, 수 $0=m_0<\cdots<m_L=1$, 유한 kernel 열 고정. root가 주어진 조건부. 모형은 들어오지 않는다.", 노드 O1, R1, R2, R3, F1, F2).
  - 받는 node가 실제로 쓰는 것은 $L$, 수 $m_d$, 확률 kernel 열, root 고정이다. 이것을 edge로 옮겼다: top-e1, e13, e14, e15(`S_SETTING` 문장), e16, e17(`S_COMB`). 따라서 FA의 이 부분은 중복이다.
  - "root가 주어진 조건부"는 R2(trees.tex 233)와 R3(298)의 항등식 성질이라 e12의 진술에 "각 root 값에서"로 실었다.
  - "모형은 들어오지 않는다"는 받는 node가 수학적으로 쓰지 않는 범위 선언이라 edge로 옮기지 않았다. 문맥에 남긴다.
  - FA는 F2도 담는데 F2는 균등 격자만 쓴다. 충돌은 아니다(F2의 조건 목록이 더 좁다). e11 이 $m_d=d/L$ 을 자기 조건으로 적었다.
- **FB** ("선택된 수열, $N\to\infty$", 노드 R4). 받는 node가 쓰는 것은 P5의 수열과 결정적 $\mathbf u$ 이고 top-e7 이 싣는다. 옮겼다. 문맥은 R4 진술의 범위 선언으로 남는다.
- **FCROSS** (수 5, 노드 XM5). 균등 격자, 고정 topology와 $\eta$, 극한 순서는 e9(R4→XM5)와 e10, e11 의 진술이 싣는다. 증폭 상수의 $L$ 의존은 e9 에 있다. 문맥은 XM5의 목표 선언으로 남는다.
- **p7의 문맥 FP** 는 범위 밖이다. 다만 `provides: XFAM` 은 top-e8 과 같은 내용이다.

## 6. 문맥을 넘는 edge

- **top-e7 (수 3 → R4)**: 고정 $L\ge2$, $\varepsilon$. 수열은 $L$ 마다 다를 수 있다. $\mathbf u_j$ 는 고정된 결정적 값. $N\to\infty$ 는 고정 $L$ 에서만. $L$, 경로 수, type에 대한 균일성은 없고 (ii)는 type마다 따로. (i) 낮은 증분은 싣지 않는다.
- **top-e8 (4.2절 → R4)**: 족은 고정한 $L$ 에 대해 먼저 정해진다. $t_\nu, I_\nu, c_\nu$ 는 $N$ 에 무관, $N$ 은 $s_N$ 과 $u_\nu$ 의 선택으로만 들어온다. $u_\nu$ 는 $t_\nu$ 의 고정 거듭제곱보다 작다.
- **top-e10 (F1 → 수 5)**: 고정 $L$ 의 정확한 항등식. old tree, color 순서, 일관된 처방 깊이에 균일. $L$ 에 대해서는 균일하지 않다. 균등 격자 대입과 큰 $L$ 의 하한은 받는 쪽.
- **top-e11 (F2 → 수 5)**: $L$, 처방 깊이, 깊이 겹침에 균일. 상수는 $q, k, \eta$ 에 의존. $|J_{\rm sep}|\ge\delta^{b}\eta^{\sum(a_v-2)}$ 외에 $L$ 균일 하한은 없다. 극한 없음.
- **top-e12 (R2 → 수 6)**: 정확한 항등식(각 $L$, 각 root, 임의의 유한 kernel 열). 나머지 한계는 $c, K$ 만의 함수. 받는 쪽은 $M$ → $q$ 고정 후 $N$ 먼저, 그다음 $L\to\infty$ (comparison.tex 218–221).

## 7. 대입 확인과 대입 node 제안

원칙은 "대입은 node"이다. 받는 node의 `statement`/`note` 가 대입을 담는지 확인했다.

| 받는 node | 옛 edge의 대입 | 확인 결과 |
|---|---|---|
| R2 | $C$ = 모든 leaf, $D_j=D$, $G=\prod D^a$ | statement와 note에 없다. note는 "수 4의 유도에서는 쓰이지 않는다"뿐이다 |
| R3 | $C=\{a_*\}$, $G$ = old tree의 함수, $j=1,\ldots,k$ | note 한 줄("$C=\{a_*\}$ 에서 시작해 $k$ 번 적용")만 있다. $D_j^a$ 를 $G$ 에 흡수하는 단계와 $\boldsymbol t=0$ 평가(trees.tex 298–304)는 없다 |
| R4 | $G=f\,g_0^{a_*}S_0^{a_*}$, $D_j=g_j\sigma_i$, old tree와 anchor 하나, 두 번 | R4의 statement에는 없지만 하위 graph p7의 T2($u=0$, $D=g\sigma_i$, $G=f\,g_0^{a_*}S_0^{a_*}$), T4($D_j=g_j\sigma_i$), T1(old tree와 anchor 하나, 두 번)이 담는다. 확인했다. 단 p7-e6, p7-e12 에 예전 `substitution` 키가 남아 있다 |

**대입 node 제안**(세우지 않았다): R2와 R3의 대입은 각자의 하위 graph(아직 없음)에 둔다. 상위 `top` 에 두면 안쪽 node가 7 + 2 = 9, 위 4절의 첫 변분·regular-shapes node까지 더하면 11이 되어 기준 9를 넘는다(추론: 기준은 check.py의 `MAX_INNER_NODES`). R2의 하위 graph에는 대입 node 하나("$C$ = 모든 leaf, $D_j=D$, $G=\prod D^a$, $k-1$ 회 되풀이")와 $Q_k$ 정규화·해석성 node가 필요하다. R3의 하위 graph에는 대입 node 하나("$C=\{a_*\}$, $G=H$, $D_j^a$ 흡수, $t=0$ 평가")가 필요하다. R4는 p7 쪽이 이미 있다.

## 8. O1, R1, R4, top-e9 에서 발견한 문제 (고치지 않았다)

**O1**
- 진술이 다음을 담지 않는다. 그런데 받는 node가 쓰고 원문에는 있다: $E_{\mathcal T}$ 의 정의(trees.tex 33–35), 내부 vertex가 자식 하나인 것을 포함(30–32), 서로 다른 자식의 독립 표집(33–34), 위첨자 $a$ 의 뜻, 새 변수를 쓰는 삽입(135–140), 깊이 $L$ 이 spin 배치일 때 replica 위치(35–37), 기대값 $\mathbb E$ 의 뜻(48–49), 복소 재귀와 해석적 경계(156–176), telescoping(204–208). 이 가운데 앞 일곱은 edge top-e1, e13~e17 의 use_note 에 표시했다.
- `grounding.source` 가 위 줄들(29–49, 135–140, 204–219)을 포함하지 않는다.
- $F[\mathcal T,C,G]$ 라는 이름은 원문에 없다(원문은 $E^A_{\mathcal T}[G\prod_{a\in C}(A^a)^{-1}]$ 로만 쓴다, 180–183). 지도 작성자의 표기다.
- $E^A[h\mid\mathscr F_d]:=K^A_{d+1}\cdots K^A_L[h]$ 의 합성 식은 원문의 "follows one new path below the specified prefix"(151–152)를 풀어 쓴 것이다. 원문에 식으로는 없다.
- `fv_inputs.insertion` 이 $A_{\boldsymbol t}$ 의 형태를 정하고 `U` 근방을 쓰는 것은 trees.tex 143–145 의 "any real neighborhood where $A$ is uniformly positive"와 맞는다(어긋남 아님).

**R1**
- `conditions` 에 "$A_{\boldsymbol t}$ 가 균등하게 양인 실수 근방"이 없다(원문 143–145). 하위 graph의 문맥 FD에만 있다. top-e2, e3 은 이 조건을 진술에 실었다.
- 진술, 부호, 예(L=1, $G=1$, $D_1=D_2=1$; $\partial_{t_1}\partial_{t_2}(1+t_1+t_2)^{-1}\rvert_0=2$)는 직접 계산해 확인했다.

**R4**
- 진술이 $f$, $R_E$, $\mathfrak E(\cdot,\cdot,\mathcal C)$, $E$, $c_E$, spin anchor와 marker anchor를 정의하지 않고 쓴다. 정의는 perturbations.tex 429–449 에 있고 top-e9 가 싣는다. `grounding.source` 가 "L2 6.3, rules.md P7" 이고 tex 줄이 없다.
- 진술의 식(456–464)과 조건(선택된 수열, 고정 $L$, 균일성 없음, mark 깊이 $1,\ldots,L-1$)은 원문과 맞는다.

**top-e9**
- 원문과 대조해 어긋남을 찾지 못했다. 한 가지 표기: 수열 첨자가 e9 는 $(N_n^{(L)},\mathbf u_n^{(L)})$, 새 top-e7 은 원문대로 $N_j,\mathbf u_j$ 다. 통합할 때 한쪽으로 맞출 것.
- e9 는 $\epsilon_{N,L,k}$ 의 최대를 취하는 목록 $\mathcal F_{L,k}$ 를 "수 5의 한 유한 크기 귀납 단계에 실제로 쓰는" 것으로 정의한다. 원문(decorrelation.tex 49–58)은 "any of the finite collections used below"라고 쓴다. 같은 뜻으로 읽었다(추론).

## 9. 원문과 기존 자료가 어긋나는 곳

1. R2의 note "수 6이 직접 쓴다" — 같은 log 전개를 수 1의 상한이 쓴다(upper.tex 70–127, 81, 97, 121에서 `tree:log-expansion`). top에는 그 받는 node가 없다. XM6 title 은 "수 6 — 삽입의 계산 (P11)" 이다. top-e12 의 use_note 에 적었다.
2. R2, R3, F1 의 `grounding.source` 는 "L2 6.1", "L2 6.2 ①", "L2 6.2 ②" 이고 tex 줄이 없다. 해당 줄은 trees.tex 224–257, 259–304, 337–386 이다(F2는 이미 393–455 를 적었다).
3. XFAM 의 `grounding.source` 는 "L2 4.2" 로 tex 줄이 없다. perturbations.tex 26–70 이다.
4. 원문 lemma `tree:extension-expansion` 은 함수를 $H$ 로, R3의 진술은 $G$ 로 쓴다. 원문 증명(299–301)이 $G$ 를 미분마다 $D_j/A$ 를 흡수하는 함수로 쓰기 때문이다. top-e6 에 "원문 lemma의 $H$"로 적었다.
5. L2/rules.md P6′ ③은 "$J_{\rm sep}$ 는 원문의 $J$"라고 쓰고, 수 5의 $J=\kappa(S^+)^2$ 는 $2b$ 개 vertex 전부에 쓴 경우다. 원문 lemma의 $J$ 는 지정한 $b$ 개 vertex의 곱이어서 같은 vertex 집합일 때만 일치한다. top-e11 의 use_note 에 적었다.
6. 위 4절의 공백 네 가지(첫 변분, 복소 재귀·해석적 경계, telescoping, regular-shapes)는 top에 해당 node나 edge가 없다.

## 10. edge 표시 대응 변경 (`viewer/edge-labels.json` 의 `move4.top`)

`top.edge-labels.json` 에 새 edge e13~e17 과 바뀐 두 개를 적었다. e4 는 "모양별 합" → "history 계수"(싣는 내용이 모양별 합이 아니라 history 정의라서), e10 은 "정규화" → "모양별 합"(싣는 내용이 $\kappa(S)$ 라서). 나머지 기존 항목은 그대로다. 통합 때 기존 파일의 해당 두 항목을 바꾸고 다섯 항목을 더하면 된다.

## 11. 통합 담당이 판단할 것

- edge `use_note` 필드를 이 목적(대입 위치, 보내는 쪽 공백 표시)으로 쓴 것이 맞는지. 규격은 `use_note` 를 대입 위치 같은 사용 설명으로 정의한다. 맞지 않으면 이 문서의 5·8절로 옮기고 지워도 check.py에는 영향이 없다.
- F1, F2, XM6 의 `inputs` 수정(1절)을 받을지.
- 4절 공백 네 가지를 node로 올릴지, O1의 출력을 늘릴지(O1을 건드리면 검토 지문이 걸리므로 O1 쪽 수정은 사용자 판단).
- 새 edge e15 는 R4 쪽 diff(p7)의 XB와 함께 읽어야 한다. p7의 외부 입력 node는 O1의 일부(밀도)만 받는다.
- 이 초안의 모든 근거 상태는 `proposed` 이며 독립 감사나 사용자 확인을 거치지 않았다. 의미를 거꾸로 읽은 부분이 없는지는 한 번 더 사람이 볼 것(추론: 긴 진술이라 옮겨 적은 식의 오타 위험이 있어 대조는 원문 줄을 보며 했지만 기계 검사는 없다).
