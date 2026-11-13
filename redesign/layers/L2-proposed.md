# L2 제안 초안 — cavity 증분에서 변분 공식까지

**상태: proposed.** 사용자 승인 전의 연구·검토용 초안이다. 기존 L1이나 규칙 표를 대체하지 않는다. 바닥은 대학원 통계역학과 cavity/replica 계산의 기초다. 아래에서는 규칙의 **정량 진술**을 입력으로 받아 주정리를 유도한다. P8·P9의 증명을 다시 했다는 뜻은 아니다. 사용한 입력과 정의를 여기에 적었으므로 근거 링크를 열지 않고도 마지막 부등식 조립을 따라갈 수 있다. 원문 순서는 §2 모형 → §4 상한 → §5 cavity → §6 섭동 → §7 집중 → §8 비교 → §9 일반화다.

## 1. 목표와 계산할 값

독립적인 $M_N\sim\operatorname{Pois}(\alpha N)$개의 $p$체 상호작용과 독립 장으로
$$-H_N(\sigma)=\sum_{j=1}^{M_N}\theta_j(\sigma_{i_{1,j}},\ldots,\sigma_{i_{p,j}})+\sum_{i=1}^Nh_i\sigma_i,\qquad F_N=N^{-1}\mathbb E\log\sum_\sigma e^{-H_N(\sigma)}$$
를 정의한다. 각 index는 $[N]$에서 복원 균일 표본추출한다. $p\ge2$는 짝수이고
$$\mathbb E\max_s|\theta(s)|+\mathbb E|h|<\infty,\quad e^{\theta(s)}=a\Bigl(1+b\prod_{\ell=1}^pf_\ell(s_\ell)\Bigr),\quad \Bigl|b\prod_\ell f_\ell(s_\ell)\Bigr|<1.$$
$f_\ell$은 i.i.d., $b$는 그들과 독립, $a>0$은 그들에게 의존해도 되며 $\mathbb E[(-b)^n]\ge0$($n\ge1$)이다. $\log a$의 별도 적분 가능성은 요구하지 않는다. 이것이 **P1**이다.

메시지 $x$는 $q_x(s)=e^{xs}/(2\cosh x)$를 뜻한다. 독립 메시지 label들에 대해
$$C_\theta(\mathbf x)=\sum_{s\in\{-1,1\}^p}e^{\theta(s)}\prod_\ell q_{x_\ell}(s_\ell),\qquad U_\theta(\mathbf x;\epsilon)=\log\sum_{s\in\{-1,1\}^{p-1}}e^{\theta(s,\epsilon)}\prod_\ell q_{x_\ell}(s_\ell),$$
$$V_{\rm s}=\tfrac12\sum_{\epsilon=\pm1}\exp\Bigl(h\epsilon+\sum_{j=1}^{K_{\rm s}}U_{\theta_j}(\mathbf x^j;\epsilon)\Bigr),\quad K_{\rm s}\sim\operatorname{Pois}(\alpha p),\qquad V_{\rm e}=C_\theta(\mathbf x).$$
시행 법칙은 $\mathcal M_1=\mathcal P(\mathbb R)$, $\mathcal M_{j+1}=\mathcal P(\mathcal M_j)$ 위의 $\zeta\in\mathcal M_{r+1}$이다. label마다 독립적으로 $\eta_0\sim\zeta$를 뽑고, 각 측도에서 다음 측도를 뽑는 일을 반복하여 $x$를 얻는다. 물리 disorder와 label들은 독립이다. $0<m_1<\cdots<m_r<1$에 대해, 물리 disorder와 깊이 $d$까지의 모든 label 변수를 고정한 조건부 기대를 사용하여
$$T_rV=V,\qquad T_dV=\bigl(\mathbb E[(T_{d+1}V)^{m_{d+1}}\mid\mathscr G_d]\bigr)^{1/m_{d+1}}\quad(d=r-1,\ldots,0)$$
로 둔다. $r=0$이면 $x$를 $\zeta\in\mathcal P(\mathbb R)$에서 독립 표본추출하고 $T$를 생략한다. 목표는
$$\mathcal B_r=\log2+\mathbb E\log T_0V_{\rm s}-\alpha(p-1)\mathbb E\log T_0V_{\rm e},\quad \Phi_r=\inf_{\zeta,\mathbf m}\mathcal B_r,\quad I=\inf_{r\ge0}\Phi_r,\qquad \boxed{\lim_NF_N=I}.$$
이 정의와 $|\log T_0V_{\rm s}|\le|h|+\sum_j\max|\theta_j|$, $|\log T_0V_{\rm e}|\le\max|\theta|$에서 $I$가 유한하다. inf의 달성이나 최적 법칙의 존재는 필요 없다. [정의·직접 부등식; [[model:functional]], [[model:trial-bounds]]]

## 2. 남은 목표는 하한 하나다

**입력 P2 → 출력 $\limsup_NF_N\le I$.** P1 아래에서 모든 $N,r,\zeta,\mathbf m$에 $F_N\le\mathcal B_r$이다. 따라서 바로 $F_N\le I$다. P2의 interpolation 증명은 여기서 블랙박스다. 짝수 $p$의 볼록성과 부호 조건은 이 입력의 정당화에 쓰인다. [ [[upper:bound]] ]

하한은 먼저 **bounded이고 입력 순열에 대해 법칙이 불변인 $\theta$, bounded $h$**에 대해 보인다. 이 중간 모형에 factorization·부호 조건을 추가로 요구하지 않는다. 원래 모형으로 돌아가는 일은 7절에서 한다.

## 3. pressure를 거의 넘지 않는 cavity 증분을 고른다

**입력 P3·P4·P5 → 출력 낮은 증분과 선택된 수열.** 깊이 $L\ge2$의 유한 보조 kernel 계층을 만들고, $m_d=d/L$로 둔다. $L$은 이 증명 장치의 깊이다. 뒤의 부호화가 $r=L-1$단 시행 functional을 내놓는다는 것은 유한 재귀의 단계 수 계산이며, 실제 Gibbs 측도의 물리적 RSB 계층을 가정하는 말이 아니다.

평균 $N^{3/4}$개의 단일 site 섭동 factor($[1/2,3/2]$ 값)를 더한 뒤 power mean을 적용한 root logarithm 기대값을 $P_N^{L,\mathbf u}$라 하자. P3는 $|P_N^{L,\mathbf u}-NF_N|\le(\log2)N^{3/4}$를 준다. 이는 밀도 차이가 0이라는 말이다. **$\mathbf u$는 고정 매개변수이며 root 무작위변수가 아니다.**

공통 $N$-spin reservoir에 대한 site·bond 삽입의 power-mean 변화량을 $Y_{0,\rm s},Y_{0,\rm b}$라 하면 P4는
$$\Delta_N^{L,\mathbf u}=P_{N+1}^{L,\mathbf u}-P_N^{L,\mathbf u}=\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}+o_N(1)$$
을 준다. site 삽입 factor 수는 $\operatorname{Pois}(\alpha p)$, bond 쪽은 $\operatorname{Pois}(\alpha(p-1))$다. $o_N(1)$은 $L,\mathbf u$에 균일하다. 이 식만으로 pressure 극한이나 증분 극한을 주장하지 않는다.

$\underline F=\liminf_{N\to\infty}F_N$은 **모든 크기**의 liminf다. $\varepsilon>0,L$마다 P5로 $N_j\uparrow\infty$와 결정적 $\mathbf u_j$를 골라
$$\Delta_{N_j}^{L,\mathbf u_j}\le\underline F+2\varepsilon$$
이면서 모든 고정 섭동 type의 score 오차가 0으로 가고, 모든 유한 prescribed tree의 multioverlap 모멘트가 수렴하게 한다. 이후 $N$은 이 수열을 뜻한다. 수열은 $(L,\varepsilon)$마다 다르다. [ [[cavity:negligible]], [[cavity:increment]], [[pert:selection]] ]

## 4. 집중 규칙이 주는 것과 주지 않는 것

**입력 P6·P7, 집중 결론 P8·P9 → 출력 깊이 평균의 multioverlap 요동 제어.** replica 집합 $S$에 대해 $A_{S,i}=\prod_{a\in S}\sigma_i^a$, $R_S=N^{-1}\sum_iA_{S,i}$다. topology는 unary vertex를 억누른 labeled tree다. $a$개 깊이 좌표가 모두 $(\eta L,(1-\eta)L)$ 안에 있고 서로 $\eta L$보다 멀면 regular라 하며
$$\mathcal A_{L,\eta}z=L^{-a}\sum_{\mathbf q\ \eta\text{-regular}}z(\mathbf q)$$
로 **정의**한다. 이 평균의 질량은 1 이하이고 regular 배정의 수로 나누지 않는다. 추가 prefix 깊이 $d$도 평균할 때는 좌표 하나를 더 세고 $d<\min_vq_v$를 요구한다. 두 aligned 사본의 같은 깊이는 좌표 하나다. singleton의 P9 평균에는 좌표가 없다. [정의; [[decor:average-definition]]]

"상태"는 보조 계층의 prefix이고 그 정보가 $\mathscr F_d$다. P8은
$$v_N(S,d)=N^{-2}\mathbb E\sum_{i,j}\operatorname{Cov}(A_{S,i},A_{S,j}\mid\mathscr F_d)^2,\qquad \lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}v_N(S,d)=0$$
을 준다. P9는 각 고정 topology와 $\eta>0$에서
$$\lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}\operatorname{Var}(R_S)=0$$
을 준다. 분산은 선택된 $\mathbf u$를 고정한 root disorder와 tree 표본추출에 대한 것이다. singleton은 더 강하게 각 고정 $L$에서 분산이 0으로 간다. 일반 $S$에서는 고정 깊이별 집중을 얻지 않는다. overlap의 극한값, $q_d$, 물리적 pure state 구조도 식별하지 않는다.

**여기서 숨기는 증명.** P7은 old tree와 anchor에 새 color를 붙이는 history들의 부호 있는 합을 시험함수 $f$와 분리한다. P8·P9는 이를 이용한 별도 정리이며 이 초안에서는 선언된 규칙으로 받아 쓴다. 아래 보충 규칙 제안은 그 증명 경로를 더 펼칠 때 필요한 입력이지, P8·P9 자체의 증명은 아니다.

**보충 규칙 제안 P6′ (proposed, 선택적 증명 입력).** anchor를 제외한 unused old leaf 재사용에는 $+1$, 내부 vertex $\beta$에서 fresh path 생성에는 $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$를 붙인다. 고른 leaf는 재사용하지 않는다. history $E$의 계수 $c_E$는 곱이다. bounded $H,D_j$와 $A_{\mathbf t}=1+\sum_jt_jD_j$에 대해
$$\left.\partial_{t_1}\cdots\partial_{t_k}E_{\mathcal T}^{A_{\mathbf t}}\frac{H}{A_{\mathbf t}^{a_*}}\right|_0=\sum_Ec_EE_{\mathcal T_E}\left[H\prod_jD_j^{a_j(E)}\right].$$
$E_{\mathcal T}^{A}$는 삽입 $A$로 tilt한 kernel들로 해당 tree 변수를 표본추출한 조건부 기대다. anchor와 color가 reference tree $S$를 이루게 하는 모든 history의 총계수는
$$\kappa(S)=\prod_{v\in\operatorname{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$$
다($a_v$는 자식 수). old tree의 leaf 수가 $q$이고 color가 $k$개일 때, 지정한 $b$개 target branching vertex의 깊이가 old tree 어디에서도 branching 깊이가 아니면
$$\sum_{E\ {m allowed}}|c_E|\le C_{q,k}L^{-b}.$$
그 $b$개 vertex의 위 곱을 $J$라 하고 $m_{d_v}\ge\eta>0$이면 $J\ne0$, $\sum|c_E|/|J|\le C_{q,k,\eta}$다. 이는 유한 tree의 정확한 조합·해석 명제들을 증명 없이 묶은 입력이다. [ [[tree:extension-expansion]], [[tree:reference-total]], [[tree:charging]] ]

P6′가 필요한 이유는 signed 합 $-1/L$과 절댓값 합 $2+1/L$이 다르기 때문이다. target split을 한 칸 늦추면 regular 배정에서 old branching 깊이를 피해 fresh unary split의 $-1/L$을 강제한다. 그러나 P8·P9를 직접 유도하려면 여전히 잎 개수 귀납, 세 사본 부등식, 사영, martingale energy, marker anchor 계산을 전개해야 한다. 그 전개를 이 문서가 완수했다고 읽으면 안 된다. [ [[x:tree-cancellation-example]], [[decor:conditional-concentration]], [[decor:overlap-concentration]] ]

## 5. 한 site를 부호화하고 여러 site를 분리한다

**입력 P9·P10·P11 → 출력 $e_{L,N}=|\Delta_N-\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})|$의 소멸.** P10은 균일 site의 $x=\operatorname{arctanh}\langle\sigma_i\rangle$ 조건부 법칙을 거꾸로 쌓아 $\zeta_{L,N}\in\mathcal M_L$을 만든다. 한 trial label의 모든 tree별 spin 곱 기대값이 $\mathbb ER_S$와 같다. 서로 다른 label은 이 전체 부호화의 독립 사본이다. 극한 법칙은 만들 필요 없다.

다음 계산은 P11의 내용을 설명하는 분해다. P11의 정량 결론을 입력으로 쓰면 이 계산 전체를 생략해도 6절은 성립한다.

고정 $k$-leaf tree에서 균일 site의 경험적 pattern 법칙은
$$\pi(\mathbf e)=2^{-k}\sum_{S\subseteq[k]}R_S\prod_{b\in S}e_b,\qquad R_\varnothing=1.$$
trial label의 법칙은 $\bar\pi=\mathbb E\pi$다(P10). 독립 균일 site $n$개의 bounded observable을 바꾸는 오차는 곱측도 telescoping으로 $n\sum_{S\ne\varnothing}\mathbb E|R_S-\mathbb ER_S|$ 이하이다. 이것은 고정 tree에서의 **직접 유도**다. [ [[comp:patterns]] ]

깊이 평균을 log 전개의 tree 법칙 $Q_k$ 평균으로 바꾸는 부분은 P11 안에 든 기술 입력이다. 명시적으로 $Q_k$의 비regular 확률은 $C_k(\eta+L^{-1})$, topology의 $a$개 깊이 배정 하나의 확률은 $C_kL^{-a}$ 이하이고, leaf 삭제는 regularity를 보존한다. 남지 않은 좌표를 합하면 $L$ 인자가 정규화와 상쇄된다. Cauchy–Schwarz와 P9로
$$\mathbb E_{Q_k}\sum_{S\ne\varnothing}\mathbb E|R_S-\mathbb ER_S|\le C_k\left(\eta+L^{-1}+\sum_U(\mathcal A_{L,\eta}\operatorname{Var}(R_U))^{1/2}\right)$$
이다. 합은 유한한 induced labeled topology들이다. 고정 $\eta$에서 $N$, $L$ 순으로 보낸 뒤 $\eta\downarrow0$이면 왼쪽이 0이다. 비regular 확률 하나만으로 이 변환이 되는 것은 아니다. [P11에 포함된 bridge와 직접 유도; [[tree:regular-shapes]], [[comp:shape-error]]]

마지막으로 bounded $|\theta|\le B,|h|\le H$에서 삽입 개수 $K\le M$을 먼저 제한한다. $C=H+BM$, $z=\cosh C$, $c=\tanh C<1$이면 reservoir·trial 삽입 모두 $A=z(1+D)$, $|D|\le c$로 쓴다. P6의 정확한 log 전개는
$$\log Y_0(1+D)=\sum_{k\ge1}\frac{(-1)^{k-1}}k\mathbb E_{Q_k}E_{\mathcal T}\prod_{a=1}^kD^a,$$
이고 $q$차 뒤 tail은 $\sum_{k>q}c^k/k$ 이하이다. $E_{\mathcal T}$는 root를 고정한 tree kernel 기대다. $Q_k$는 single path에서 시작하여 $n$개 leaf일 때 내부 vertex $\beta$를 $(n_\beta m_{d_\beta+1}-m_{d_\beta})/n$ 확률로 골라 fresh path를 붙이는 법칙이다. 각 고정 차수는 최대 $pM$개 site의 bounded pattern observable이므로 앞의 오차가 0으로 간다. 양쪽 log 비교의 tail은 $2\sum_{k>q}c^k/k$, count tail은 $2\mathbb E[(H+BK)\mathbf1_{K>M}]$ 이하이다.

따라서 허용 오차를 정하면 먼저 $M$으로 Poisson tail, 그다음 $q$로 series tail을 작게 하고, 유한한 남은 차수들에 대해 $N$ 다음 $L$ 극한을 취한다. 이것은 무한급수와 극한을 근거 없이 교환하는 단계가 아니다. 독립 trial 삽입은 정확히 $T_0V_{\rm s}$와 bond 쪽 $\alpha(p-1)\mathbb E\log T_0V_{\rm e}$를 주므로 P4와 합쳐
$$\lim_{L\to\infty}\limsup_{N\to\infty}e_{L,N}=0$$
이다. 이 마지막 결론 자체가 기존 **P11**이다. [ [[tree:log-expansion]], [[comp:insertion-comparison]] ]

## 6. bounded 하한은 한 줄 부등식으로 닫힌다

**입력 3절의 낮은 증분·P11·변분값의 정의 → 출력 $\underline F\ge I$.** 각 선택된 $N,L$에서
$$I\le\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\le\Delta_N+e_{L,N}\le\underline F+2\varepsilon+e_{L,N}.$$
그 $(L,\varepsilon)$의 수열을 따라 $\limsup_N$, 이어 $L\to\infty$, 마지막으로 $\varepsilon\downarrow0$을 취한다. $\underline F$가 전체 크기의 liminf이므로 수열마다 달라지는 trial 법칙에도 $\liminf_NF_N\ge I$가 성립한다. P3만으로 $\lim F_N=\lim\Delta_N$라 놓는 논법은 사용하지 않는다. [ [[comp:bounded-lower]] ]

## 7. 일반 법칙으로 옮겨 상한과 맞춘다

**입력 P1·P12·bounded 하한 → 출력 일반 하한, 이어 P2 → 목표.** $c=\theta(1,\ldots,1)$, $\widehat\theta=\theta-c$로 둔다. $c$는 적분 가능하다. factorization의 $a$가 비율에서 사라지고
$$\widehat\theta(s)=\log\frac{1+b\prod_\ell f_\ell(s_\ell)}{1+b\prod_\ell f_\ell(1)}$$
이므로 P1의 독립·동일분포 구조가 $\widehat\theta$의 입력 순열 불변성을 준다. 각 entry와 장을 $[-K,K]$로 잘라 $\widehat\theta^{(K)},h^{(K)}$를 만든다. 이 자르기는 순열 불변성을 보존하며 factorization 보존은 필요 없다.

$D_K=\mathbb E\max_s|\widehat\theta-\widehat\theta^{(K)}|$, $d_K=\mathbb E|h-h^{(K)}|$는 0으로 간다. P12의 균일 한계
$$|F_N-F_N'|\le\alpha D+d,\qquad |\mathcal B_r-\mathcal B_r'|\le\alpha(2p-1)D+d$$
는 모든 $r$, 같은 시행 법칙에서 성립하므로 해당 inf들에도 두 번째 한계가 성립한다. bounded 하한과 합쳐
$$\liminf_N\widehat F_N\ge\widehat I-2\alpha pD_K-2d_K.$$
$K\to\infty$로 보내고 $\widehat F_N=F_N-\alpha\mathbb Ec$, $\widehat I=I-\alpha\mathbb Ec$를 써 상수 이동을 되돌리면 $\liminf_NF_N\ge I$다. 2절의 $\limsup_NF_N\le I$와 맞아서 **이제** 극한의 존재와 공식이 나온다. [ [[reduction:stability]], [[main:theorem]] ]

이 초안이 재구성한 것은 선언된 규칙에서 주정리로 가는 논증과 P11 오차의 회계다. P5·P7·P8·P9·P10의 증명, 특히 P7에서 집중으로 가는 전체 §7은 남겨 둔 블랙박스다. P6′를 추가하더라도 그 사실은 바뀌지 않는다. 규칙 승인, 독립 내용 검토, 모의 독자 단면 시험은 아직 완료하지 않았다.
