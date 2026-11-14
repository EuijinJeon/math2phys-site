## 공통 부록: 모양별 합, 계수 한계, 사용 경계

다음은 세 후보가 공통으로 받는 진술이며 여기서는 증명을 블랙박스로 둔다. anchor와 color가 만드는 split 모양 S를 처방하되 미사용 old path를 추가로 구별하지 않는다. Br(S)는 branching vertex 집합, a_v는 S에서의 자식 수, d_v는 깊이다. 모양 S를 갖는 history의 signed 계수 총합은 old tree와 무관하게

$$\kappa(S)=\prod_{v\in\mathrm{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1}).$$

uniform mesh m_d=d/L, δ=1/L에서 처방한 branching vertex 중 깊이가 old tree의 어느 branching 깊이와도 같지 않은 것을 b_sep개 고른다. (전부 또는 일부.) old leaf 수 q,color 수 k에 대해

$$\sum_{E\text{ 허용}}|c_E|\le C_{q,k}\delta^{b_{\rm sep}}.$$

고른 vertex의 κ 인자 곱을 J_sep라 하면 그 모든 vertex에서 m_{d_v}≥η>0이라는 조건 아래

$$\frac{\sum_{E\text{ 허용}}|c_E|}{|J_{\rm sep}|}\le C_{q,k,\eta}$$

라는 L-uniform bound를 쓴다. |J_sep| 자체는 δ^{b_sep} 크기로 작아지며 L-uniform 양의 하한이 없다. η 조건 없이는 고차 branching의 j≥2 인자가 추가로 작아질 수 있다. 이 계수 한계는 uniform mesh 전용이며, 미분·log 전개와 κ 항등식은 일반 증가 mesh에서 성립한다. signed 합과 절댓값 합은 다르다. 예컨대 old 두 path가 depth s에서 갈라질 때 color도 anchor와 s에서 갈라지게 하면 signed 합 −δ이지만 절댓값 합 2+δ이다. 목표 split을 s+1<L로 미루면 허용 fresh 하나의 계수 −δ만 남아 절댓값 합 δ다.

P7은 별도 입력인 선택된 수열의 score 집중과 tree 모멘트 수렴, Palm 변환·해석성·polarization·mark selector를 이 미분 전개와 결합해 얻는 prescribed-tree 항등식이다. 이 문서는 그 전체 증명을 재구성하지 않는다. P7의 극한은 고정 L·tree·제약에서 선택된 수열을 따라 N→∞이며 L-uniform 수렴률이 없다. 여기의 유한 보조 tree 계산으로 물리적 Gibbs 측도의 pure-state/RPC 구조나 overlap 극한값이 증명되는 것은 아니다.

근거(열람 불필요): trees.tex tree:reference-total, tree:charging, perturbations.tex pert:tree-identity. 문서 바깥 링크를 열지 않아도 이 시험의 모든 질문을 풀 수 있게 제공한 범위다.
