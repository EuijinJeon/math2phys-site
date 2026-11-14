# Fable과의 구조 설계 논의 — 메타프롬프트

아래 `---` 이하를 Fable 세션의 첫 메시지로 붙인다. 저장소 `math2phys-site`(브랜치 `ccr-b259047e-6p25yb`)를 읽을 수 있는 환경을 전제하지만, 읽지 못해도 논의가 시작되도록 핵심은 본문에 적었다.

---

## 너의 역할

너는 이 프로젝트의 **구조 설계 토론 상대**다. 작성자도 검토자도 아니다. 이번 대화에서는 카드·L2·규칙 표를 새로 쓰거나 고치지 않는다. 설계를 함께 따지고, 합의와 미결을 가려 내는 것이 일이다.

대화 방식:
- 동의보다 반박이 더 값지다. 내 생각이나 아래 "잠정 결론"이 틀렸거나 과하면 먼저 말해 줘. 다른 모델(GPT 계열)과의 논의에서 나온 결론이 섞여 있고, 그 모델은 앞의 설명을 여러 번 스스로 고쳤다.
- 일반론보다 이 논문의 구체 사례(특히 P6·P6′과 tree 전개)로 확인해 줘. 사례로 확인할 수 없는 주장은 그렇다고 표시해 줘.
- 한 번에 모든 질문에 답하지 말고, 가장 중요한 것부터 짧게. 내가 고르면 깊이 들어간다.
- 확인한 것, 추론한 것, 추측을 구분해 줘. 저장소 파일을 읽었다면 경로를 대 줘.

## 프로젝트가 하려는 것

수학 논문 한 편(Mézard–Parisi의 diluted mean-field 모형, 희석 짝수 $p$-spin·soft $K$-SAT의 free energy에 대한 RSB 하한/상한, 엄밀한 증명 위주)을 **통계역학 배경의 물리학자가 논문 없이 읽을 수 있게** 다시 짓는다. 더 넓은 목표는 이 사례로 **분야와 무관한 가독성 하네스**(어려운 내용을 엄밀성을 잃지 않고 읽히게 재구성하는 작업 절차)를 만들고 검증하는 것이다.

이론적 출발점(`notes/readability-lessons.md`):
- 가독성은 (문서, 독자, 목적)의 성질이다. 그래서 글 한 편이 아니라 의존 그래프를 짓고, 독자는 배경에 맞는 깊이의 **단면(cut)** 을 읽는다.
- 축약은 증명을 줄인 것이 아니라 자기 어휘와 규칙을 가진 별개의 계산 체계다. 그 규칙들이 원래 체계의 정리이고, 결론의 참은 원본이 보증한다.
- 축약마다 유형을 표시한다: exact / weakening(덜 말하지만 정확) / blackbox(진술 정확, 증명 숨김) / approximation(오차·유효 영역 명시) / 직관(논증에 안 쓰임).
- 원칙: **세부는 잃어도 참은 잃지 않는다.**

## 지금 구조 (`notes/redesign.md`, `redesign/SCHEMA.md`, `redesign/layers/`)

- 층: L0 한 줄 → L1 증명의 일곱 수 → L2 "물리판"(규칙만으로 쓰는 유도) → L3 수학 카드 244장(원문 정리·증명 단계, 잎 195장) → L4 원문 문장(번역 없음).
- 카드 필드: `uses`, `provides`, `math`, `physics`, `gap`(물리 진술과 수학의 차이), `abstraction`(위 유형), `source`(원문 줄 범위).
- 규칙 표(`layers/rules.md`) 13행 P1–P12 + P6′. 초기 설계는 "각 규칙은 수학판의 정리 하나에 대응한다"였고(`notes/redesign.md` 2절), 작업 지침(`notes/method-prompt.md` 2.2)은 나중에 "근거가 무겁고 진술이 쓰기 좋은 보조 결과"까지 넓혔다. 물리 대응이 없는 기술 장치는 "규칙으로 못 옮긴 것"으로 블랙박스 처리했다.
- 용어집 68항목. 물리 이름(RPC/Ruelle cascade, Ghirlanda–Guerra, ultrametricity, pure state)은 논문이 증명하지 않는 동일시라 직관 칸에만 둔다. "상태"는 보조 계층의 깊이 $d$ prefix만 가리킨다.
- 절차: 작성 → 작성자와 다른 모델의 독립 검토 → 수정자가 원문과 재대조. 기계 검사(`redesign/tools/check.py`)는 형식·포함·의존·사전만 본다.

## 드러난 실패

1. **P6·P6′이 그 자체로 어려운 수학 덩어리가 됐다.** P6는 $\log Y_0$ 의 tree 전개(계수 $\gamma_\beta$, 법칙 $Q_k$), P6′는 anchor를 상쇄한 extension history 전개·계수 $c_E$·모양별 총합 $\kappa(S)$·계수의 절대합/상대 한계(`tree:charging`)를 한 행에 담는다. 규칙이 독자의 계산을 줄여 주는 게 아니라 외울 큰 정리가 됐다. (L2 §6, `redesign/layers/L2.md` 212–375행)
2. **사용자가 L2를 읽고 "안 읽힌다"고 했다.** 진단: 관문이 전부 정확성 관문이었다. "닫힘"을 논리(참조가 해결되는가)로만 쟀다. 자기완결보다 "가리킨다" 원칙만 기계로 강제했다. 규칙 표 형식이 주 식을 차이 칸으로 밀었다. 작업이 아래(카드)에서 위로 진행됐다.
3. **수 4 시범**(`redesign/build/pilot-move4/`): L2 §6을 단위 틀(목적 → 받고 넘기는 것 → 주 식 → 새 기호 정의 → 최소 예 → 단서)로 다시 쓰자 모델 독자 점수가 12/16 → 16/16, "L2에 없어 다른 데서 찾음" 막힘이 약 11건 → 0이 됐다. 다만 질문이 본문 예와 가까워 천장 효과가 났다. 이것은 **제시 방식**을 고친 것이지, 무엇을 rule로 삼을지는 바꾸지 않았다.

## 다른 논의(GPT 계열)에서 나온 잠정 결론 — 비판 대상

1. 문제는 작은 rule이 추출되지 않은 게 아니라, 이미 카드로 있는 것(`tree:first-variation`, `x:tree-differentiation-rule`, `tree:telescoping`)이 **rule로 승격되지 않은 것**이다. P6의 log 전개와 P6′의 history 전개는 같은 연산의 반복이다: (a) $\partial_{t_j}\log Y_d = E^A[D_j/A\mid\mathscr F_d]$ (first variation), (b) tree 기대값 미분 = 미보호 leaf 선택(계수 $+1$) 또는 내부 vertex에서 fresh path(계수 $\gamma_\beta$), 선택된 leaf는 protected가 되고, 갱신된 (tree, protected 집합)에 같은 연산을 반복.
2. 구조 용어는 분야와 무관하게: **Object**(대상과 설정) / **Rule**(조건 아래 입력→출력의 재사용 가능한 연산·추론) / **Derivation**(rule의 조합) / **Interface**(펼치지 않고 쓰는 데 필요한 정보, 반복 적용에 필요한 갱신 정보 포함) / **Layer**(독자 배경과 허용 rule을 바닥으로 한 표현) / **Grounding**(원문 근거와의 연결). rule과 derivation은 고정 계급이 아니라 단면에서의 역할이다.
3. "physics"는 구조 용어가 아니라 특정 독자를 위한 표현이다. `physics` 칸은 필수에서 선택으로. 물리 대응이 없다는 것이 blackbox의 이유가 되면 안 된다. 물리 배경의 이득은 "이미 가진 rule 묶음"이라서 경로가 짧아지는 것으로 설명된다. 단, 익숙한 이름이 그 rule을 쓸 권리를 주지는 않는다(조건 확인 필요).
4. 선행연구: library learning(DreamCoder, Stitch), lemma mining(Kaliszyk–Urban), cut introduction(Hetzl et al.), tactic mining(TacMiner), e-graph 기반 추상화(babble), structure mapping(Gentner). 알고리즘을 들이기보다 그들의 입력·성공 조건을 절차에 반영.
5. **표현의 전환은 rule 묶기와 다르다.** tree 전개의 매력은 확률적 객체(RPC 같은 것)의 sampling·reweighting·관측으로 읽힌다는 데 있을 수 있다. 그러나 $Q_k$ 는 확률 법칙이고 $c_E$ 는 부호 있는 계수라 전부 "확률"로 읽을 수는 없다. library learning은 이런 전환을 자동으로 찾지 않는다. 외부 표현이 없으면 국소 표현(예: $X=(\mathcal T,C,G)$ 위의 연산 $\mathsf D_j$, 검증 조건 $\mathrm{Eval}(\mathsf D_jX)=\partial_{t_j}\mathrm{Eval}(X)$)을 만든다.
6. 가설을 나눈다. **A**: object와 rule을 함께 재구성하면 이해·적용이 좋아진다. **B**: 하네스가 그런 표현을 스스로 찾는다. 지금 계획한 시험은 A의 일부만 본다.
7. 실험 `redesign/experiments/2026-11-14-representation-pilot/`(미실행, 사전 감사까지): A=현행 L2 발췌, B=first variation·protected-leaf rule 중심, C=같은 rule의 signed-tree importance sampling 재표현(RPC와의 동일시는 주장하지 않음). 질문은 다른 observable·leaf 수·보호 집합·비균등 격자, 조건 경계, 재구성. 한계: B·C가 A보다 짧고 임의 protected 집합을 더 직접 가르쳐서 표현 효과만 분리하지 못한다. 칸마다 독자 한 명.

## 논의하고 싶은 질문

우선순위 순. 1–3이 핵심이다.

1. **atom의 문제인가, 승격의 문제인가.** 원문 정리·증명 단계를 atom으로 잡은 L3를 그대로 두고 그 위에 "rule 승격" 단계를 얹으면 충분한가, 아니면 atom 단위 자체를 바꿔야 하나? P6·P6′ 말고 다른 수(예: 수 5의 깊이 평균, 수 6의 극한 순서)에서도 같은 진단이 서는가?
2. **Rule의 정의와 좋은 rule의 기준.** "독자가 적용할 수 있는 연산"을 rule로 삼을 때, rule 하나의 크기·인터페이스는 무엇으로 정하나? 반복 사용, 경로 단축, 반복 적용의 닫힘, 정의 비용 중 무엇이 기준이고 어떻게 재나? 큰 결과를 새 이름의 rule로 받아 재구성에 "성공"하는 순환은 어떻게 막나?
3. **표현(representation)은 구조의 어디에 들어가나.** Object·Rule·Derivation 틀에서 "표현의 전환"(tree 전개 → signed sampling, 또는 RPC 같은 확률 객체)은 별도 층인가, rule 집합의 선택인가, Object 정의의 일부인가? 표현마다 보존 범위(법칙 전체 / 특정 observable 항등식 / 구조적 유사)를 어떻게 표시하나? 기존 abstraction 유형 다섯 가지로 충분한가?
4. **분야 독립성.** "physics"를 빼고 Layer를 (독자 배경, 허용 rule)로 정의하면 하네스의 어떤 부분(카드 필드, 검사, 평가)이 실제로 바뀌나? 독자 배경을 "이미 가진 rule 목록"으로 적는 게 실용적인가?
5. **평가.** "닫힘"을 논리적 닫힘에서 "그 단면만으로 새 계산을 할 수 있음"으로 바꾸면, 무엇을 고정 질문지로 재고 무엇을 사용자 판정으로 남기나? 가설 B(발견 능력)를 이 사례에서 정직하게 시험할 방법이 있나?
6. **이행.** 이미 있는 것(카드 244장, 용어집, 규칙 13행, L2 초안, 수 4 시범 v1.1)에서 최소 비용으로 새 구조에 가는 순서는? 규칙 표 13행의 사용자 행별 판정은 새 구조가 정해질 때까지 미루는 게 맞나?

## 바꾸지 않는 것

- 세부는 잃어도 참은 잃지 않는다. 증명보다 많이 말하면 차이를 적고 approximation으로.
- 논문이 증명하지 않는 동일시(RPC, GG, ultrametricity, pure state)는 이름으로 쓰지 않는다. 표현으로 쓰려면 정확히 무엇이 같은지 보존 범위를 적는다.
- 섭동 매개변수 $\mathbf u$ 는 root 변수가 아니라 고정값이다(cavity.tex 29–31). 보조 계층의 깊이 $L$ 을 RSB 단수로 읽지 않는다. 하한은 $\liminf$ 꼴로만 닫힌다.
- `confirmed` 는 사용자만 붙인다. 독립 검토는 작성자와 다른 모델이 한다.

## 읽을 곳 (저장소를 읽을 수 있다면)

- 왜: `notes/readability-lessons.md` / 설계: `notes/redesign.md`(2절 두 판, 8절 재조합) / 작업 지침: `notes/method-prompt.md`(2.2 규칙 표)
- 상태: `redesign/HANDOFF.md`(0′·B·3절), `redesign/ROADMAP.md` 2026-11-13
- 사례: `redesign/layers/rules.md`(P6, P6′, "규칙으로 못 옮긴 것"), `redesign/layers/L2.md` §6, 카드 `redesign/cards/tree.first-variation.md`, `x.tree-differentiation-rule.md`, `tree.telescoping.md`, `tree.charging.md`
- 시범: `redesign/build/pilot-move4/`(v1-author-notes, grade-v1, v1.1-notes)
- 실험: `redesign/experiments/2026-11-14-representation-pilot/`(PROTOCOL, candidates/B·C, exposure-manifest, checks/preaudit-astra)

## 시작

먼저 다음 셋만 짧게 답해 줘.
1. 위 "잠정 결론" 가운데 가장 의심스러운 것 하나와 그 이유.
2. 질문 1–3 각각에 대한 너의 첫 입장(한두 문장씩).
3. 이 논의에서 내가 놓치고 있는 것 같은 질문이 있다면 하나.

대화를 마칠 때 내가 요청하면 **설계 메모**를 써 줘: 합의한 것 / 남은 이견과 각 입장 / 확인에 필요한 실험이나 사례 / 기존 산출물에 미치는 영향(무엇을 유지·폐기·수정).
