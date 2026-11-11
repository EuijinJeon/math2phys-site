# Readability 논의 정리

어려운 내용을 엄밀하고 self-contained하게 유지하면서 읽을 수 있게 만드는 구조에 대한 논의 기록.
1부는 정의, 2부는 분야별 레슨과 출처, 3부는 math2phys 해석 작업에의 적용, 4부는 열린 질문이다.

표기: **[문헌]** 은 검색으로 확인한 결과, **[유추]** 는 논의 중 세운 대응 관계(검증 안 됨), **[기억]** 은 출처를 다시 확인하지 않은 것.

---

## 1부. 정의

### 1.1 Readability

Readability는 텍스트의 속성이 아니라 **(문서, 독자, 목적)** 쌍의 속성이다.
배경 B인 독자가 내용 C를 검증 가능한 수준으로 이해하는 데 드는 총비용(읽는 양 + 해독 노력 + 길 찾기)이 작을수록 readable하다.

독자마다 최적 텍스트가 다르므로 보편적으로 readable한 것은 한 편의 글이 아니라 **구조**다.
문서는 단위들의 의존 그래프이고, 독자는 자기 배경에 맞는 깊이에서 자른 **단면(cut)** 을 읽는다.

### 1.2 구조가 만족해야 할 조건

| 조건 | 내용 |
|---|---|
| 닫힘 | 모든 단면이 그 자체로 참이고, 쓰인 용어가 그 단면 안에서 해결된다 |
| 정초성 | 어떤 용어든 유한 번 펼치면 명시된 바닥(공통 기초)에 닿는다 |
| 인터페이스 충분성 | 단위의 축약문만 알면 그것을 쓰는 모든 곳을 따라갈 수 있다 |
| 역할 명시 | 각 단위가 전체에서 무엇의 입력이고 출력인지가 본문보다 먼저 나온다 |

### 1.3 축약은 다른 계산 체계다

이미 증명된 내용의 축약판은 "증명을 줄인 것"이 아니다. 자기 어휘와 자기 규칙을 가진 별개의 체계이고, 그 규칙들이 원래 체계의 정리이며, 결론의 참은 원본이 보증한다. 물리가 수학에 대해 갖는 관계와 같다.

축약이 틀리지 않으려면 다음 넷 중 하나여야 하고, 어느 것인지 표시해야 한다.

| 유형 | 내용 | 참인 이유 | 펼침 방식 |
|---|---|---|---|
| 약화 | 덜 말하지만 정확함 | 상세의 논리적 귀결 | 삽입 |
| 블랙박스 | 진술은 정확, 증명만 숨김 | 진술 자체가 정리 | 삽입 |
| 근사 | 유효 영역과 오차를 명시 | 조건부 진술로서 참 | 치환 |
| 직관·비유 | 논증에 쓰이지 않음을 표시 | 주장이 아님 | 삽입 |

원칙: **세부는 잃어도 되지만 참은 잃으면 안 된다.**

### 1.4 적법성과 선호의 분리

"어떤 축약이 허용되는가"(건전성, 닫힘)와 "허용된 것 중 무엇이 좋은가"(목적, 독자)는 다른 질문이다.
음악 이론(GTTM의 well-formedness / preference 규칙)과 지도학(hard / soft constraint)이 독립적으로 같은 분리에 도달했다.

### 1.5 두 개의 축

| 축 | 성질 | 예 | 배치 |
|---|---|---|---|
| 입도 | 거의 연속, 단조 | 단계를 얼마나 보여주나 | 한 장의 stretchtext |
| 이론 | 이산, 부분순서(격자) | 무엇을 원시 규칙으로 삼나 (열역학 대 통계역학) | 판 사이 번역 사상을 가진 여러 장 |

손잡이가 연속이어도 축약의 종류는 문턱에서 불연속으로 바뀐다(지도에서 면이 점으로 바뀌는 지점).

### 1.6 Stretchtext로 배치 가능할 조건 [유추]

1. **중첩성**: 거친 판이 정밀한 판에 그대로 들어 있다 (successive refinement).
2. **삽입 대 치환**: 약화·블랙박스는 삽입으로, 근사는 치환으로 펼쳐진다.
3. **가환성**: A만 펼치고 B는 접어둔 혼합 상태도 참이고 읽힌다. 축약 경계가 조건부 독립 경계여야 한다.
4. **트리 대 DAG**: 공유되는 보조정리는 트리로 풀면 중복 폭발이 나므로 참조를 허용해야 한다.

### 1.7 존재 조건과 한계

닫힌 축약의 존재는 내용의 성질(스케일 분리, 모듈성, 재사용되는 보조정리)에 달린 우연적 사실이다.
- 위계가 없는 내용(대량 경우 분석)은 "참이다"라는 블랙박스 외에 충실한 짧은 판이 없다.
- 의존이 촘촘히 얽힌 내용은 어떤 순서로도 열린 항목이 많아 나선형으로 여러 번 도는 수밖에 없다.
- 축약은 목적 의존적이라 목적이 여럿이면 축약 체계도 여럿이다.
- 가장 짧은 기술은 해독 계산이 가장 길다(logical depth). 최소화 대상은 길이가 아니라 길이 + 해독 시간이다.

---

## 2부. 분야별 레슨

### 2.1 물리

- **유효이론**: 좋은 축약은 그 스케일에서 계산이 완결된다. 미시 세부는 몇 개의 매개변수로만 들어온다.
- **Sloppy models** [문헌]: Fisher 정보 고유값이 기하급수적 위계를 이루어 소수의 stiff 방향만 예측을 좌우한다. 유효이론이 가능한 이유.
- **RG = 정보 병목** [문헌]: IB 압축이 찾는 relevant 자유도가 스케일링 차원이 가장 낮은 연산자와 일치한다.
- **근사가 틀리지 않는 이유**: 유효 영역과 오차 크기를 함께 말하기 때문.
- 이 레포의 예: cavity field 분포는 그래프 나머지 전체의 요약이고, 그 요약만으로 다음 단계가 닫힌다.

### 2.2 정보이론

- 독자에게 드는 길이는 조건부 복잡도 K(C | B). 배경이 side information.
- 저자는 B를 모르므로 한 번에 최적 부호화할 수 없다. 수신자가 필요한 만큼 더 요청하는 방식이어야 한다. "펼쳐볼 수 있어야 한다"의 근거.
- **Successive refinement** [문헌]: 층화가 손실 없이 되는 원천(Gaussian 등)이 있고 안 되는 원천도 있다. 안 되어도 손실은 상수로 유계(Lastras–Berger).
- **Sufficient statistic / information bottleneck**: 하류가 상세에 의존하는 방식이 축약을 통해서만일 때 축약이 유효하다.
- **Logical depth** (Bennett) [기억]: 짧을수록 해독이 오래 걸린다.
- IB의 β는 연속이지만 최적 표현은 임계값에서 구조가 바뀐다 [기억].

### 2.3 수학·논리

- 보조정리는 인터페이스. 쓰는 쪽은 진술만 필요하다.
- **Cut 제거** [문헌]: 보조정리를 없애면 증명이 지수적(1차 논리에서는 비초등적)으로 커진다. 좋은 보조정리가 있으면 계층적 서술이 그만큼 짧다.
- **Gödel speed-up** [기억]: 증명된 정리를 규칙으로 승격하는 것은 더 강한 체계로 옮기는 것이고, 더 강한 체계는 더 짧은 증명을 준다.
- Lamport의 structured proof, TLA+의 계층 증명 [문헌]: 증명을 층화해 각 층이 완결된 논증이 되게 한다.
- Lean blueprint [문헌]: 비형식 진술과 형식 증명을 의존 DAG로 잇는다.
- 증명 제시 연구(Ωmega/P.rex, granularity-adaptive presentation) [문헌]: 입도 축을 직접 다룬다.

### 2.4 추상화의 형식 이론

- **Abstract interpretation** [문헌]: "정밀도는 잃어도 정확성은 잃지 않는" 추상화를 Galois connection으로 정의. 추상화들은 격자를 이룬다.
- **계산적 창발** (Rosas 등 2024) [문헌]: 창발적 거시 과정을 인과적·정보적·계산적으로 self-contained한 것으로 정의. 그런 과정들이 격자를 이룬다. "self-contained한 축약"에 가장 가까운 정의.
- **Causal abstraction** (Beckers–Halpern, Geiger) [문헌]: 수준 간 개입 일관성, 근사 추상화.
- **Natural latents** (Wentworth) [문헌]: 관찰자와 무관한 축약의 조건(mediation + redundancy). 정확한 것은 Gaussian계에서 존재하지 않고 작은 분포 차이에 강건하지 않다. 닫힌 축약은 본질적으로 근사 이론이다.

### 2.5 알고리즘·자료구조

- Parnas의 information hiding: 경계는 하류가 세부에 의존하지 않는 곳에 긋는다.
- 독자의 배경 = 캐시, 펼침 = lazy evaluation, 정의 안 된 용어 = dangling pointer.
- **Pebbling** [유추]: 읽는 순서는 의존 DAG의 선형화. 한 시점에 열려 있는 미해결 항목 수가 작업기억 부하(약 4청크).

### 2.6 머신러닝

- Distillation, MDL: 예측력을 유지하는 최소 표현.
- 이해의 조작적 정의: 요약만 보고 하류 질문에 답할 수 있는가.
- LLM은 배경을 통제한 모의 독자로 쓸 수 있다.
- Matryoshka 표현 [문헌]: 접두부가 그 자체로 쓸 수 있는 중첩 표현이 거의 비용 없이 학습된다.

### 2.7 인지과학·교육

- **Expertise reversal effect** [기억]: 초심자에게 도움 되는 상세가 숙련자에게는 방해. 단일 텍스트가 모두에게 최적일 수 없다.
- McNamara·Kintsch [기억]: 지식이 많은 독자는 덜 친절한 글에서 더 깊이 이해한다.
- **Reigeluth의 elaboration theory** [문헌]: 가장 단순하고 본질적인 epitome을 먼저, 그 뒤 단계적 정교화. 줌 렌즈 비유.
- Bruner [기억]: 어떤 내용도 지적으로 정직한 형태로 누구에게나 가르칠 수 있다.

### 2.8 담화·서사·음악·지도

- **Rhetorical Structure Theory** [문헌]: 텍스트는 핵/위성의 재귀적 트리. 핵은 위성 없이 이해되지만 역은 아니다(삭제 검사). 위성을 지우면 의존 단위도 함께 지워야 하는 경우가 있다.
- Kintsch–van Dijk 거시규칙 [기억]: 요약 = 삭제 · 일반화 · 구성.
- **Barthes, Chatman** [문헌]: 서사의 핵(cardinal function, kernel)과 촉매(catalyser, satellite).
- **Schenker, GTTM** [문헌]: 환원된 것도 적법한 음악이어야 한다. 적법성 규칙과 선호 규칙의 분리. 환원을 계산하는 절차는 없다고 저자들이 인정.
- **지도 일반화** [문헌]: 축척이 바뀌어도 위상이 깨지지 않아야 한다. hard / soft constraint. tGAP의 연속 일반화. 면이 점으로 바뀌는 문턱.

### 2.9 철학

- **Surveyability** [문헌]: Wittgenstein의 Übersichtlichkeit, Tymoczko의 4색정리 비판. Teller: 조망 가능성은 정도의 문제이고 독자 의존적.
- **Elgin, *True Enough*** [문헌]: 이상화는 felicitous falsehood. 기준은 목적에 비추어 충분히 참인가. 문턱 설정이 약점.
- **Mach, Chaitin** [문헌]: 과학은 사유의 경제, 이해는 압축. 반론: 압축은 이해의 그림자일 뿐.
- **Thurston 대 Jaffe–Quinn** [문헌]: 증명의 목적은 인간의 이해. 추측–엄밀의 1차원 척도로는 부족.
- Hamami, Avigad, Burgess–De Toffoli [문헌]: 비형식 증명의 엄밀성이 형식화 가능성으로 환원되는가.
- Batterman–Rice 대 Strevens [문헌]: 세부를 버린 모형이 왜 설명력을 갖는가(보편성 대 difference-making).
- 『논고』의 번호 체계 [문헌]: 논리적 트리이자 하이퍼텍스트. 트리 독해와 순차 독해의 논쟁은 진행 중.
- 해석학적 순환: 부분은 전체를, 전체는 부분을 알아야 이해된다. 최상위 요약을 먼저 주어 깬다.

### 2.10 디자인·업무 구조화

- **Alexander, "A City is Not a Tree"** [문헌]: 살아 있는 구조는 트리가 아니라 겹침을 허용하는 semilattice.
- Simon의 near-decomposability [기억]: 부분 내부 상호작용이 부분 간보다 훨씬 강할 때 이해 가능하다.
- Shneiderman [문헌]: overview first, zoom and filter, then details on demand.
- **임무형 지휘** [문헌]: 지휘관 의도는 3–5문장, 두 단계 아래까지 이해되어야 한다. 이해를 행동으로 검증한다.
- Information Mapping, DITA [문헌]: 유형별 블록과 라벨, 조립 가능한 topic. 입도가 한 층뿐.
- Minto의 MECE, WBS의 100% 규칙 [기억]: 하위 항목의 합이 정확히 상위 항목.
- Stretchtext (Ted Nelson), semantic zoom [문헌]: 제자리에서 늘고 주는 글. LLM 기반 시도는 대부분 데모 수준.
- 탈무드 지면 [문헌]: 본문과 층층의 주석. 다만 주석은 원래 독립 저작이었다.

---

## 3부. math2phys 해석 작업에의 적용

현재 구조(확인한 것): 문장 단위 원문 → 번역 → 물리 해석 → 항별 표, 접힌 섹션 요약(하는 일 · 물리적 의미 · 건너뛰어도 되는지), 물리학자용 길잡이, 역할 표 R1–R22, 검증 태그(✅ 📚 ❓ ⚠ 🔧), 제안 해석 표시, 🧭 물리 직관과의 차이, 고정 번호 체계, 가독성 루프(블라인드 비교, 전략 C).

이미 조건 대부분의 골격이 있다. 아래는 빠진 부분이다.

### 3.1 평가를 적법성 검사와 선호 비교로 나눈다 (1.4)

블라인드 비교는 선호 판정이다. 그 앞에 통과/실패로 판정되는 적법성 검사를 둔다.

- **닫힘**: 섹션 요약과 길잡이에 나오는 모든 기호·용어가 그 블록 안에서 정의되거나 R-ID·용어집·고정 번호로 연결되는가.
- **건전성**: 요약·길잡이의 각 문장이 원문에서 따라 나오는가, 아니면 1.3의 유형 표시가 붙어 있는가.
- **인터페이스 충분성**: 뒤 섹션이 이 섹션에서 인용하는 결과가 모두 섹션 요약의 "알아 둘 결론"에 들어 있는가. 고정 번호와 `find_refs.py`로 기계적으로 확인할 수 있다.

적법성에서 떨어진 판은 선호 비교에 올리지 않는다.

### 3.2 축약 유형을 검증 태그와 별개로 표시한다 (1.3)

현재 태그는 "얼마나 확인했나"를 말한다. "어떤 종류의 축약인가"는 다른 축이다.
물리 해석 문장마다 약화 / 블랙박스 / 근사 / 직관 중 하나임이 드러나야 한다.

§7.1 길잡이의 "정리가 증명하는 것은 이 가정의 깊이 평균·L→∞ 판이다"가 근사 유형의 모범이다: 물리 진술과 정리가 실제로 증명한 것 사이의 차이를 유효 영역으로 적었다. 이것을 모든 "물리로는" 문장의 규칙으로 삼는다.

### 3.3 역할 표를 번역 사상으로 다룬다 (1.5)

수학판과 물리판은 입도 축이 아니라 이론 축의 두 판이고, 역할 표 R1–R22가 그 사이의 번역 사상이다.
- 역할 표에 "대응이 깨지는 곳 / 유효 범위" 열을 둔다. 🧭 항목이 그 내용이다.
- 🔧(물리 대응 없음)은 번역 사상이 정의되지 않는 지점이다. 억지로 해석을 붙이지 않고 블랙박스로 둔다.

### 3.4 단면을 명시하고 각각 닫혀 있는지 시험한다 (1.2)

현재 단면은 넷이다: 섹션 요약만 / + 길잡이 / + 문장별 해석 / + 원문과 항별 표.
"요약만 읽고 넘어가도 흐름이 이어지게"는 첫 단면이 닫혀 있다는 주장이므로 시험할 수 있다.

- 단면만 떼어 모의 독자(물리 배경, 본문 접근 없음)에게 주고 하류 질문을 풀게 한다. 예: "§8이 §7에서 쓰는 것은 무엇이고 어떤 극한 순서에서 성립하는가".
- 원본과 개선판을 같은 질문 세트로 비교하면 선호가 아닌 측정값이 된다.
- 최상위 단면이 하나 더 필요하다: 증명 전체를 한 쪽으로 쓴 epitome (2.7).

### 3.5 증명 지도는 트리가 아니라 DAG로 (1.6-4)

목차는 트리지만 Lemma 6.2, Theorem 6.5 같은 결과는 여러 섹션에서 재사용된다.
섹션·정리 단위의 의존 그래프를 따로 두고, 각 노드에 "무엇을 받아 무엇을 내놓는가"를 한 줄로 적는다.

### 3.6 열린 항목 수를 가독성 지표로 쓴다 (2.5)

문단마다 "도입되었지만 아직 쓰이지 않은 기호 + 쓰였지만 아직 해결되지 않은 참조"의 수를 센다.
4를 넘는 구간이 길잡이가 필요한 곳이고, 길잡이의 "읽는 법"은 그 구간에서 무엇을 들고 있어야 하는지 말해야 한다.

### 3.7 가환성 점검 (1.6-3)

접힌 블록 안의 내용에 접힌 블록 밖의 문장이 의존하면 안 된다.
"위에서 본", "앞의 논의처럼" 같은 암묵 참조를 고정 번호 참조로 바꾼다.

### 3.8 하지 않을 것

- 요약을 더 짧게 만드는 것 자체를 목표로 삼지 않는다 (logical depth).
- 모든 기술 단계에 물리 해석을 붙이려 하지 않는다 (존재 한계, 1.7).
- 입도 축과 이론 축을 한 손잡이로 합치지 않는다.

---

## 4부. 열린 질문

1. 설명 텍스트에 대해 "닫힌 단면들의 격자"를 정의한 연구가 있는가. 검색에서는 찾지 못했다.
2. 가환성 조건을 텍스트에 대해 정확히 진술할 수 있는가. natural latent의 mediation 조건과의 대응은 유추일 뿐이다.
3. 층화의 비용(중복)에 Lastras–Berger 식의 상한이 있는가.
4. 근사형 축약의 문턱("충분히 참")을 어떻게 정하는가. Elgin에 대한 비판이 그대로 적용된다.
5. 축약의 종류가 바뀌는 문턱을 내용에서 미리 읽어낼 수 있는가.
6. 환원을 계산하는 절차가 없다는 GTTM의 한계가 여기에도 적용되는가. 즉 핵/위성 구분은 판단에 의존할 수밖에 없는가.

---

## 출처

**물리·정보이론**
- Relevance in the Renormalization Group and in Information Theory — https://ar5iv.labs.arxiv.org/html/2012.01447
- Parameter space compression underlies emergent theories — https://www.arxiv.org/pdf/1303.6738
- Sethna, Why is science possible? — https://sethna.lassp.cornell.edu/Sloppy/WhyIsSciencePossible.html
- Multiuser Successive Refinement and Multiple Description Coding — https://ar5iv.arxiv.org/html/0707.4133
- Matryoshka Representation Learning — https://arxiv.org/pdf/2205.13147v3

**추상화 이론**
- Software in the natural world (Rosas et al.) — https://arxiv.org/abs/2402.09090
- Abstracting Causal Models (Beckers & Halpern) — https://arxiv.org/pdf/1812.03789
- Approximate Causal Abstraction — https://www.cs.cornell.edu/info/people/halpern/papers/approximateabs.pdf
- Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability — https://arxiv.org/pdf/2301.04709v3
- Natural Latents — https://arxiv.org/pdf/2509.03780
- Gaussian Natural Latents — https://www.greaterwrong.com/posts/H8ktAMBv8jQr8JymL/introduction-gaussian-natural-latents
- Abstract interpretation notes (Møller) — https://cs.au.dk/~amoeller/spa/10-abstract-interpretation.pdf

**증명**
- Making proofs without Modus Ponens — https://arxiv.org/pdf/math/9607204
- Pudlák, The lengths of proofs — https://users.math.cas.cz/~pudlak/length.pdf
- Flat vs hierarchical theorem provers — https://arxiv.org/pdf/2602.10512
- Granularity-Adaptive Proof Presentation — https://arxiv.org/pdf/0903.0314
- TLA+ Proofs — https://arxiv.org/pdf/1208.5933
- More Details, Please (autoformalization) — https://mlanthology.org/icmlw/2024/tarrach2024icmlw-more
- Thurston, On proof and progress in mathematics — https://arxiv.org/pdf/math/9404236
- Jaffe & Quinn, Theoretical Mathematics — https://www.arthurjaffe.com/Assets/pdf/Theoretical_Mathematics.pdf

**철학**
- Non-surveyable proof — https://en.wikipedia.org/wiki/Non-surveyable_proof
- Mathematics in the age of the reproduction of intelligence — https://arxiv.org/pdf/2608.16378
- Critique of Hamami's standard view of rigor — https://link.springer.com/article/10.1007/s11229-024-04521-2
- Epistemic Value of Proof — https://philsci-archive.pitt.edu/24324/1/Epistemic_Value_of_Proof.pdf
- Elgin, True Enough (NDPR review) — https://ndpr.nd.edu/reviews/true-enough/
- Minimal Model Explanations (Batterman & Rice) — https://cambridge.org/core/journals/philosophy-of-science/article/abs/minimal-model-explanations/640580F4EA5571EA1AA971C5DC063FA6
- Saatsi & Reutlinger on RG explanations — https://eprints.whiterose.ac.uk/122190/18/697735.pdf
- Compressibility, laws of nature, initial conditions and complexity — https://arxiv.org/pdf/1709.07062
- Tractatus numbering as tree — https://nordicwittgensteinreview.com/article/download/3437/pdf
- University of Iowa Tractatus Map — https://tractatus.lib.uiowa.edu

**담화·서사·음악·지도·교육**
- RST nuclearity (Stede) — https://www.ling.uni-potsdam.de/~stede/Papers/nucl08.pdf
- Discourse tree trimming for summarization — https://preview.aclanthology.org/fix_video/D13-1158.pdf
- On Barthes's Structural Analysis of Narratives — https://amindformadness.com/2015/01/on-barthess-introduction-to-the-structural-analysis-of-narratives-2/
- Marsden, Schenkerian reduction and GTTM — https://fun.repo.nii.ac.jp/record/4822/files/SMC2013-Marsden.pdf
- Continuous generalization with tGAP — https://ris.utwente.nl/ws/files/6783602/CtGAP4interpolation.pdf
- Buttenfield & Wolf, feature dimension change across scale — https://cartogis.org/docs/proceedings/2008/wolf_buttenfield.pdf
- Elaboration Theory (Reigeluth) — https://tecfa.unige.ch/themes/sa2/act-app-dos2-fic-elaborat.htm

**디자인·업무**
- Alexander, A City is Not a Tree — https://www.patternlanguage.com/archive/cityisnotatree.html
- Explorable Explanations (Bret Victor) — https://worrydream.com/ExplorableExplanations/
- Commander's intent (Canadian Army Journal) — https://www.canada.ca/en/army/services/canadian-army-journal/articles/2025/short-bursts-rolls-commanders-intent-redux.html
- DITA chunking — https://www.oxygenxml.com/dita/styleguide/Topics_and_Information_Types/c_How_Chunking_Works.html
- TreeReader — https://arxiv.org/pdf/2507.18945
- Sensecape — https://arxiv.org/pdf/2305.11483
- The layout of a Talmud page — https://hadran.org.il/terms/the-layout-of-a-talmud-page/
