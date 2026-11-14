# diff 채우기 초안 — 작업 기록

2026-11-14. 초안 `diff.json` 은 graph `diff` 객체 전체다. 새 하위 graph는 만들지 않았다. 검증용 사본 `diff.trial.json` 은 `graphs/move4.json` 에서 diff만 초안으로 갈아 끼운 것이다. 원본과 다른 기존 파일은 고치지 않았고 커밋하지 않았다.

초안 생성 스크립트는 저장소 밖 scratchpad에 두었다. 고정 자료(D2, D4, XO, diff-e3/e4/e5/e7/e8/e9, 문맥 FD)가 원본과 같은지, 새 edge에 `fit`/`substitution` 키가 없는지 스크립트 안에서 assert로 확인했다.

## 결과 요약

| vertex | 상태 | 이유 |
|---|---|---|
| D1 밀도의 로그를 미분 | sketch (유도 5줄 작성) | top.O1이 $d_\beta$, $n_\beta$, $Y_\beta$의 뜻을 싣지 않는다 |
| D3 leaf 항: 상쇄와 protected | sketch (유도 6줄 작성) | top.O1이 $E_{\mathcal T}$를 정의하지 않는다 |
| S1 tree 표본 규칙 | sketch (fact, 유도 없음) | 원문이 인용만 한다. 필요한 정의도 O1에 없다 |
| OUT 미분 규칙 | complete (유도 3줄) | diff-e6, diff-e7만으로 닫힌다 |

- edge: diff-e1, diff-e2, diff-e6을 새 형식(`complete:true`, `statement`, `defines`)으로 다시 썼다. 새 edge 셋은 diff-e10(XO→D3, 정의), diff-e11(D2→D1, `output_ref` kernel_form), diff-e12(XO→S1, 정의)다. 새 node는 없다.
- node `inputs` 변경: D1 `["XO","D2"]`, D3 `["D1","XO"]`, S1 `["XO"]`.
- `check.py diff.trial.json`: 오류 0, 경고 11. 원래 있던 `[OUTPUT_CONTRACT] ... 재검토 필요` 경고 10개는 그대로이고, 새 경고는 `[diff] edge diff-e11 [OUTPUT_CONTRACT]: 내부 증명 변경 후 출력 대응 재검토 필요` 하나다. 이유는 아래 "새 경고" 절에 적었다.
- 검토 지문: 원본과 사본에서 출력 지문 4개(top.O1.fv_inputs, diff.D2.kernel_form, fv.TM, fv.PM)가 모두 같다는 것을 계산으로 확인했다. 기존 `reviewed_fingerprint`·`proof_review` 는 그대로 두었다.

## 가정 검사 (사본에서만)

- H0: 초안에서 D1, D3의 status만 complete로 바꾸면 `SYMBOL_UNDEFINED` 오류 10개가 난다. D1에서는 `Y_beta`, `d_beta`, `n_beta`, D3에서는 `E_T` 다. sketch로 둔 이유가 기계 검사에서도 그대로 드러난다.
- H1: diff-e1에 "$d_\beta$ 깊이, $n_\beta$ 자식 수, $Y_\beta=Y_{d_\beta}$(β의 prefix)"를, diff-e10에 "$E_{\mathcal T}$ 정의"를 덧붙이고 `defines` 를 더한 뒤 D1, D3을 complete로 바꾸면 오류 0이다. 새 경고는 diff-e11 하나뿐이다. D1은 입력 2/2, D3은 입력 2/2를 쓴다. 이 검사는 기호 색인이 맞는다는 확인일 뿐이다. 수학적으로 맞는지는 판정하지 않는다.

## vertex별 기록

### D1 — 밀도의 로그를 미분

- 대조한 원문: trees.tex 92–96($d_\beta$, $n_\beta$, $\gamma_\beta$), 97–105(밀도와 "$Y_\beta$ is $Y_{d_\beta}$ evaluated on the prefix at β"), 107–110(단조성 경계), 142–154(첫 변분), 156–176(해석적 경계, 비교용), 184–191($\partial\log W$ 식).
- 유도: 식 1 로그 전개, 식 2 $\partial\log A^a=D_j^a/A^a$, 식 3 diff-e11에 $d=d_\beta$ 대입, 식 4 $\partial\log W$ 식, 식 5 $U$ 위 균일 경계.
- author_filled
  - 식 3: $|\partial\log Y_\beta|\le\|D_j\|_\infty/a$. 원문은 미분 가능성을 156–176의 복소 영역 해석적 경계로 정당화한다. 초안은 실수 근방에서 첫 변분 출력(D2)을 쓰는 다른 길로 갔다.
  - 식 5: $0<W\le b^{|\mathrm{Leaves}|}a^{\sum\gamma_\beta}$, $|\partial\log W|$ 의 경계. 원문 173–176은 이를 해석적 경계로 말할 뿐 식을 적지 않는다.
- 닫지 못한 것
  - O1이 $d_\beta$, $n_\beta$, $\mathrm{Leaves}(\mathcal T)$, $\mathrm{Int}(\mathcal T)$, $Y_\beta$의 정의를 싣지 않는다. O1의 $W$ 식은 이 기호들을 정의 없이 쓴다.
  - D2의 `produces` 는 diff-e4만 적는다. diff-e11을 더하려면 D2를 고쳐야 해서 하지 않았다. `check.py` 는 하위 graph를 가진 node의 produces를 검사하지 않으므로 오류로 나오지 않는다. 하지만 SPEC 6절 조건 4("보내는 edge가 모두 produces에 있다")에는 어긋난다. 사본에서 D2.produces에 diff-e11 항목을 더해 보았는데 출력 지문은 바뀌지 않았다.
- 판단: 통합 담당은 D2→D3을 예로 들었다. 초안은 D2→D1 하나로 했다. $\log Y_\beta$의 미분 가능성과 경계가 처음 필요한 곳이 D1이고, D3은 D1이 diff-e2로 넘기는 경계만 쓰면 된다. D2에서 나가는 edge가 하나로 줄어든다.

### D3 — leaf 항: 상쇄와 protected

- 대조한 원문: trees.tex 32–34($E_{\mathcal T}$), 67–82(위첨자 $A$), 173–176, 180–196(protected, $F$ 꼴, 상쇄와 남은 leaf 항).
- 유도: 식 1 $F=E_{\mathcal T}[G\Psi]$, 식 2 $\partial\log\Psi$(상쇄), 식 3 $\partial(G\Psi)$와 균일 경계, 식 4 미분과 기대값의 교환, 식 5 leaf 항을 $F[\mathcal T,C\cup\{a\},GD_j^a]$로 바꾸고 내부 항을 $E^A$ 꼴로 쓰기, 식 6 합.
- author_filled
  - 식 3: 균일 경계.
  - 식 4: 교환의 정당화(평균값 정리와 유계 수렴). 원문 184–194는 교환을 말없이 쓴다.
- 닫지 못한 것: O1이 $E_{\mathcal T}$(원래 kernel로 자식을 독립으로 뽑는 root 조건부 표본 평균)를 정의하지 않는다. O1에는 $E^A_{\mathcal T}=E_{\mathcal T}[\cdot\,W]$만 있다. 이것은 $E_{\mathcal T}$를 써서 $E^A_{\mathcal T}$를 정의하는 식이지 $E_{\mathcal T}$의 정의가 아니다.
- 판단: 교환은 PM의 선례처럼 같은 node 안에 두었다. 교환을 따로 떼어 node를 하나 더 둘지는 통합 담당이 정한다. 그렇게 하면 edge가 둘 늘어난다.

### S1 — tree 표본 규칙

- 대조한 원문: trees.tex 29–39(tree, 자식들의 독립 표본, $E_{\mathcal T}$, 38–39 사영 일관성), 76–82(삽입 후 kernel, 위첨자 $A$), 97–100(밀도), 196–202(인용).
- 판단: 첫 문장(자식들의 독립)은 32–33의 정의다. 사영 일관성(38–39)은 원문이 증명 없이 적는다. 200–202는 둘을 "conditional independence of children and the projectivity of tree sampling"로 인용만 한다. 그래서 유도 없이 근거 줄 범위를 적은 fact로 두었다. 지운 부분을 확률 kernel로 적분하면 1이 된다는 짧은 계산으로 유도할 수는 있지만 원문에 없어서 쓰지 않았다.
- author_filled: 없음.
- 닫지 못한 것: diff-e12가 O1에서 실을 수 있는 것은 path·kernel·tree·$K_d^A$·확률 kernel·$E^A_{\mathcal T}=E_{\mathcal T}[\cdot W]$·root 고정까지다. S1에 필요한 조건부 독립, $E_{\mathcal T}$, 사영 일관성, 위첨자 $A$의 뜻, 밀도라는 사실은 O1에 없다.
- 진술의 `\beta` 가 원본 JSON에서 `\b`(backspace)로 읽히던 오류는 초안 S1에서만 고쳤다. 그 밖의 문자는 바꾸지 않았다.

### OUT — 미분 규칙

- 대조한 원문: trees.tex 178–202, 299–301("Apply the preceding rule successively, incorporating each new $D_j$ in $G$").
- 유도: 식 1 diff-e6, 식 2 각 β 항에 diff-e7 대입(R1의 식), 식 3 출력이 다시 $F$ 꼴이라 반복 적용됨.
- author_filled: 없음.
- 닫지 못한 것: 없음. 다만 아래 두 가지가 있다.
  - diff-e7에 `defines` 가 없다. 그래서 식 2가 $x$(=$x_\beta$)와 $\mathcal T\oplus\beta$(`T_plus`)를 표기로 다시 선언한다.
  - 합산을 output node 안의 유도로 했다. 대입은 node여야 한다. 그런데 diff-e7의 도착점(OUT)을 바꿀 수 없어서 별도 합산 step node를 두지 못했다. 보기 생성기는 output node의 완결을 평가하지 않고 "output"으로만 표시한다.

### edge

| id | 무엇 | 근거 줄 |
|---|---|---|
| diff-e1 (다시 씀) | XO→D1. O1 진술의 path·tree·Y 재귀·$W$·$\gamma_\beta<0$·단조성 경계, fv_inputs.insertion의 $D_j$ 유계와 $U$ | 16–23, 67–72, 92–110, 142–145 |
| diff-e2 (다시 씀) | D1→D3. $\partial\log A^a$, $\partial\log W$ 식, $\gamma_\beta$ 상수, 균일 경계 $M_W$ | 98–110, 142–154, 184–191 |
| diff-e6 (다시 씀) | D3→OUT. D3의 진술과 $GD_j^a$ 유계·매개변수 무관 | 180–196 |
| diff-e10 (새) | XO→D3. $E^A_{\mathcal T}=E_{\mathcal T}[\cdot W]$, $F$ 정의, $G$·$D_j$ 조건, $U$ | 67–82, 142–145, 180–183 |
| diff-e11 (새) | D2→D1. diff-e4와 같은 `output_ref` 방식. 받는 D1에 `input_ports.first_variation` | 142–154 |
| diff-e12 (새) | XO→S1. path·tree·$K_d^A$ 확률 kernel·$E^A_{\mathcal T}=E_{\mathcal T}[\cdot W]$·root 고정 | 20–23, 29–30, 76–82 |

XO에서 나가는 평문 edge(e1, e10, e12)는 O1의 진술과 O1.outputs.fv_inputs 항목의 문장만 옮겼다. 출처는 각 진술 끝에 적었다.

## 새 경고

`[diff] edge diff-e11 [OUTPUT_CONTRACT]: 내부 증명 변경 후 출력 대응 재검토 필요`

- 원인: `D2.outputs.kernel_form` 의 `proof_review.proof_fingerprint` 가 원본에서 이미 맞지 않는다(원래 경고 `[diff] node D2 출력 kernel_form`). 그 출력을 참조하는 edge는 모두 이 경고를 물려받는다. diff-e4, fv.f2/f4/o1, fresh.fp-first가 이미 같은 경고를 낸다.
- 없애려면 `proof_review` 를 갱신해야 한다. 지시대로 갱신하지 않았다.
- D1의 `input_ports.first_variation.reviewed_fingerprint` 에는 현재 kernel_form 지문 `16c4ad3b…`을 적었다. D4·FP_BIND·fv.OUT의 기존 값과 같은 값이다. 기존 기록을 갱신한 것이 아니라 새 port의 기록이다. 작성자가 이 판의 kernel_form을 읽고 D1 식 3의 대입에 썼다는 뜻이다. 이 값을 빼면 `수신 재검토 필요` 경고가 하나 더 생긴다. 넣을지 말지는 통합 담당이 정한다.

## 건드리지 않은 자료에서 발견한 문제

1. **backspace 문자.** JSON의 `"\beta"` 가 `\b`+`eta` 로 읽혀 backspace가 들어 있다. 위치는 diff-e5.statement, fresh.FP_SAMPLE.statement, fresh.fp-sampling.statement와 summary다. 원본 S1도 같았고 초안에서는 고쳤다. KaTeX에 β가 그려지지 않는다.
2. **diff-e8이 O1보다 많이 싣는다.** 첫 문장 "삽입 후의 $E^A_{\mathcal T}$는 확률 kernel $K_d^A$로 tree를 뽑은 root 조건부 평균이다"는 O1에 없다. O1에는 $E^A_{\mathcal T}=E_{\mathcal T}[\cdot W]$만 있고, 이 문장에는 trees.tex 81–82, 97–100이 필요하다. D4(complete)가 이 문장에 기댄다. D3을 sketch로 둔 기준을 적용하면 D4에도 같은 틈이 있다. fresh.fp-def-*도 같은 문장이다.
3. **D4가 sketch인 S1에 기댄다.** D4는 S1의 내용을 diff-e5로 받는다. 국소 완결 정의로는 문제가 없지만, S1이 인용 fact이고 O1에 근거가 없다는 점은 D4 위쪽으로 남는다.
4. **D2.produces에 diff-e11이 없다.** D1 절에 적었다.
5. **diff-e7에 `defines` 가 없다.** diff-e3, e5, e7, e8의 grounding에는 `state` 가 없다.
6. **XO.grounding.source가 trees.tex 줄 범위가 아니다.** 지금 값은 "L2 6.1"이다.
7. **문맥 FD에 `defines` 가 없다.** FD 텍스트에는 $D_j$ 유계도 없다. 그래서 $D_j$ 유계는 fv_inputs.insertion 문장을 XO edge에 옮겨 받았다. FD를 고치면 kernel_form 지문이 바뀐다. FD는 fv의 경계 문맥이다.
8. **기호 id 충돌.** fv의 binding에서 `F` 는 $\mathscr F_d$다(`fv.input.F`). fresh와 이 초안에서 `F` 는 protected $F$다. 초안은 $\mathscr F_d$에 `Fd` 를 썼다. 원문의 leaf 지표 $a$와 하한 $a$도 겹친다. 초안은 경계 식에서 leaf 지표를 $a'$로 쓰거나 "leaf마다"로 풀었다.
9. **기존 회귀 시험 실패.** `tools/test_check.py` 의 `test_baseline_and_coverage` 가 현재 원본에서 이미 실패한다. 원본에 OUTPUT_CONTRACT 경고 10개가 있기 때문이다. 이번 작업과 무관하다.
10. **보기의 짧은 라벨이 없다.** `viewer/edge-labels.json` 에 diff-e10, e11, e12 항목이 없다. diff-e6의 caption "old leaf"는 새 내용(∂F 전체 식)과 조금 어긋난다.

## 다른 graph에 필요한 변경

### O1에 추가가 필요한 문장과 원문 줄 범위

| 문장 | trees.tex | 필요한 vertex |
|---|---|---|
| tree의 각 internal vertex는 자식이 하나 이상이다. $\mathrm{Leaves}(\mathcal T)$는 깊이 $L$의 끝 vertex, $\mathrm{Int}(\mathcal T)$는 internal vertex의 집합이다 | 29–31 | D1 |
| 각 vertex에서 서로 다른 자식은 해당 kernel로 독립으로 뽑는다. $E_{\mathcal T}$는 이 표본 추출의 root 조건부 기대값이다 | 32–34 | D3, S1 |
| 일부 leaf와 남은 leaf가 쓰지 않는 path 부분을 지우면 남은 tree의 표본 법칙이 보존된다 | 38–39 | S1 |
| tree 기대값의 위첨자 $A$는 삽입 후 kernel $K_d^A$를 쓴다는 뜻이다 | 81–82 | S1 (diff-e8도) |
| internal vertex $\beta$의 깊이 $d_\beta$, 자식 수 $n_\beta$ | 92–93 | D1 |
| $W_{\mathcal T}(A)=dP^A_{\mathcal T}/dP_{\mathcal T}$, 곧 삽입 후 tree 법칙의 조건부 밀도다 | 97–100 | S1 (diff-e8도) |
| $Y_\beta$는 β의 prefix에서 평가한 $Y_{d_\beta}$다 | 105 | D1 |

추가한 뒤에는 diff-e1, diff-e10, diff-e12에 같은 문장과 `defines`(`d_beta`, `n_beta`, `Y_beta`, `E_T` 등)를 더한다. 그러면 D1, D3의 status를 complete로 올릴 수 있다(가정 검사 H1).

### 추가 방법에 따라 지문이 바뀐다 (사본에서 확인)

- **O1의 `statement` 에 덧붙이는 경우.** kernel_form의 증명 지문이 바뀐다. diff.XO가 O1을 상속하고 그 진술이 fv 경계의 `sources` 에 들어가기 때문이다. 그 결과 diff-e4, diff-e11, fv.o1/f2/f4, cp.b0/s0, fresh.fp-first에 `수신 재검토 필요` 경고가 새로 생긴다. 사본에서는 경고가 11개에서 19개로 늘었다.
- **O1에 별도의 `outputs.<새 이름>` 을 두는 경우.** `role:"given"` 과 `clauses` 를 가진 출력이다. 이때 kernel_form 지문은 바뀌지 않는다. `outputs` 는 증명 지문 필드에 들어가지 않는다. 사본에서 경고 11개 그대로임을 확인했다. 이 방식을 쓰면 diff-e1/e10/e12를 `output_ref`(+`clauses`) edge로 바꾸고, D1/D3/S1에 `input_ports` 를 단다.

### 그 밖

- D2.produces에 diff-e11 항목 추가(지문 불변을 확인함).
- diff-e5와 fresh의 `\beta` 이스케이프 수정.
- edge-labels.json에 diff-e10/e11/e12 추가.
