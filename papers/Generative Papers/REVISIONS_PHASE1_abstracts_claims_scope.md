# Phase-1 Revisions: Abstracts, §2 Claims, §3 Scope for Papers #1–#17

**Purpose.** Bring abstracts, claim sentences, and scope sections into line with what is actually proven. Eliminate the "displaced-postulate" overclaim by foregrounding which substrate primitives are load-bearing inputs to each forcing argument (and are not themselves derived in that paper).

**Methodology.** Each paper gets:

1. A revised **Abstract** that names the load-bearing primitives in the conditional clause ("Given substrate primitives [list], ...").
2. A revised **§2 Claim** sentence that makes the conditional explicit and points to a future "Primitive-Forcing Meta-Paper" for upstream forcing of the primitives.
3. A revised **§3 Scope** that adds a new subsection **§3.0 Primitive Inputs (load-bearing, not derived here)** before the existing FORCED / INHERITED / OUT OF SCOPE breakdown, so reviewers can see at a glance what is being assumed.

**Proofs, derivations, vocabulary, substrate-class definitions, and downstream content are untouched.** Only the framing changes.

---

## Paper #1 — The Participation Measure

### Revised Abstract

Standard quantum mechanics opens with a postulate: the state of a system is a complex-valued wavefunction $\psi(x)$ whose squared modulus is a probability density. The complex-valued range, the squared exponent, and the inner-product structure are all assumed. This paper shows that, **given substrate primitives that supply (i) a non-negative additive bandwidth quantity $b_K$ (Primitive P04), (ii) a $U(1)$-valued angular polarity $\pi_K$ (Primitive P09) as the unique angular primitive in the substrate, and (iii) a channel structure on which both live (Primitives P03 + P07)**, the wavefunction-class object is not a postulate but a uniqueness theorem. Real-valued, quaternionic, signed-measure, phase-only, and non-quadratic alternatives are each excluded by an explicit structural argument. The unique survivor — the **participation measure** $P_K(x,t) = \sqrt{b_K(x,t)} \cdot e^{i\pi_K(x,t)}$ — has squared modulus equal to bandwidth and phase equal to polarity. The claim is conditional: the substrate primitives themselves (in particular the $U(1)$-valued character of P09 and the additive non-negative character of P04) are upstream commitments, not consequences of this paper. Why those primitives and not others is the subject of a separate Primitive-Forcing Meta-Paper. What this paper establishes is that *no other amplitude carrier is consistent with those primitives*, and that every Hilbert-space-arena theorem downstream (Born, Bell-Tsirelson, Heisenberg, Schrödinger) rests structurally on this conditional uniqueness.

### Revised §2 Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: bandwidth (P04) as a non-negative additive scalar, polarity (P09) as the unique $U(1)$-valued angular primitive, and channel structure (P03+P07)*. Then the amplitude carrier on that substrate is, uniquely up to a global phase convention, the complex-valued participation measure
> $$P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i\pi_K(x, t)}$$
> with $|P_K|^2 = b_K$ and $\arg(P_K) = \pi_K$.
>
> *The substrate primitives are load-bearing inputs to this theorem and are themselves treated upstream in the Primitive-Forcing Meta-Paper. The present paper establishes conditional uniqueness given those primitives.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

The forcing argument of this paper is conditional on the following substrate-level structural facts, which it takes as given:

- **P04 (bandwidth as non-negative additive scalar).** The substrate supplies a real-valued non-negative quantity $b_K \geq 0$ on each channel, additive under channel decomposition. *Why bandwidth and not some other non-additive carrier of "amount of participation"* is upstream content treated in the Primitive-Forcing Meta-Paper.
- **P09 ($U(1)$-valued polarity as the unique angular primitive).** The substrate supplies an angular variable $\pi_K \in U(1) \cong S^1$, and this is the substrate's *only* angular primitive. *Why $U(1)$ and not $\mathbb{Z}_n$, $\mathbb{R}$, or no angular content at all* is upstream content.
- **P03 + P07 (channel and locus indexing).** The substrate supplies a discrete index set of channels and a (discrete or continuous) index set of loci. *Why channels and loci with these formal properties* is upstream content.

The forcing theorem here is: *given these primitives*, the complex polar participation measure is the unique amplitude carrier. The theorem does **not** establish that the primitives themselves are necessary; it establishes that, conditional on them, the carrier is unique.

(Existing §3.1 What is FORCED, §3.2 What is INHERITED, §3.3 What is OUT OF SCOPE — unchanged.)

---

## Paper #2 — The Born Rule

### Revised Abstract

The Born rule — that the probability of a measurement outcome $K$ is the squared modulus $|\psi_K|^2$ of the corresponding amplitude — is the bridge between the wavefunction and observable frequencies. Gleason's theorem (1957) and Busch's POVM extension (2003) derive its quadratic form, but only by *assuming* the complex Hilbert space at the outset. This paper shows that, **given the substrate primitives of Paper #1 plus Primitive P11 (commitment as a discrete substrate-level event with environmental phase-randomization at commitment) and the participation-measure result $|P_K|^2 = b_K$**, the Born rule is forced via two parallel routes — a direct definitional route from bandwidth fractions, and a Gleason-Busch reconstruction performed on the participation manifold rather than on a postulated Hilbert space. Linear, higher-power, contextual, signed, non-additive, and phase-dependent alternatives are each excluded. The unique survivor is $\text{Prob}(K) = |P_K|^2/\sum_K |P_K|^2$. The claim is conditional: the quadratic form is forced *given* the substrate's bandwidth-additivity primitive (P04) and the commitment-with-phase-randomization mechanism (P11). These primitives are themselves load-bearing inputs; why they have the structural character they do is upstream content for the Primitive-Forcing Meta-Paper. The present paper establishes that no *other* probability rule on commitment outcomes is consistent with those primitives.

### Revised §2 Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: the participation-measure structure of Paper #1, bandwidth additivity (P04), and commitment-with-environmental-phase-randomization (P11)*. Then the probability that a commitment event at locus $u$ selects channel $K^*$ from the available-channel set $\mathcal{K}(u)$ is, uniquely up to normalization convention,
> $$\text{Prob}(K^* \mid u) = \frac{|P_{K^*}(u)|^2}{\sum_{K \in \mathcal{K}(u)} |P_K(u)|^2}.$$
>
> *The phase-randomization at commitment is a substrate-level primitive (P11), not derived here. It is load-bearing in the operational route; why the substrate has commitment with this character is upstream content (Primitive-Forcing Meta-Paper).*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Participation-measure structure from Paper #1.** The identity $|P_K|^2 = b_K$ is taken as input. The quadratic form of the Born rule inherits from this identity *directly* in the operational route; Paper #1's primitives (P04 + P09) are therefore upstream of this paper.
- **P11 (commitment as a discrete primitive substrate event with environmental phase-randomization).** The mechanism by which interference cross-terms are killed at commitment is a substrate-level primitive, not derived here. *Why the substrate has commitment with this specific character — discreteness, irreversibility, environmental phase-randomization on a uniform $U(1)$ distribution — is upstream content.* The uniform-$U(1)$ character of the phase distribution is itself a non-trivial structural commitment closely related to the load-bearing P09 polarity primitive.
- **Bandwidth additivity (P04).** Needed for $\sigma$-additivity of the probability rule. Upstream content.

The Gleason-Busch route operates structurally: once Paper #1 supplies the Hilbert-space arena and bandwidth additivity supplies $\sigma$-additivity, standard Gleason 1957 + Busch 2003 produces the quadratic form. This is honest — the route is "Gleason on the participation manifold." The novelty is the *substrate-level origin of the arena*, not the Gleason machinery itself.

(Existing §3.1 What is FORCED, §3.2 What is INHERITED, §3.3 What is OUT OF SCOPE — unchanged.)

---

## Paper #3 — Sesquilinear Inner Product + Tsirelson Bound

### Revised Abstract

The sesquilinear inner product on the state space of quantum mechanics and the Tsirelson bound $|S| \leq 2\sqrt{2}$ on bipartite CHSH correlations are normally either postulated (in the case of the inner product) or derived from operator algebra that assumes it (in the case of Tsirelson's bound). This paper shows that, **given the substrate primitives of Papers #1–#2 plus the four-band orthogonality structure of Primitive P04 §1.5**, both facts are forced: the sesquilinear inner product is the unique pairing on the participation manifold consistent with the substrate's four-band orthogonality and bandwidth-additivity primitives, and the Tsirelson bound is its structural consequence via the Landau-Khalfin operator-norm algebra. Real-bilinear, non-sesquilinear, non-positive, PR-box, and superquantum alternatives are each excluded. The bound $2\sqrt{2}$ is forced as the unique ceiling — neither relaxed nor strengthened — by the joint action of the substrate-derived inner-product structure and bandwidth normalization. The claim is conditional on the substrate primitives; in particular, on the four-band partition's primitive-level orthogonality, which the substrate adopts as a structural commitment and which is itself upstream content for the Primitive-Forcing Meta-Paper.

### Revised §2 Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#2 results plus four-band orthogonality (P04 §1.5)*. Then:
> - **(IP)** The unique inner product on the participation manifold consistent with substrate primitives is sesquilinear:
>   $$\langle P \mid Q \rangle = \sum_K \sum_u P_K^*(u)\, Q_K(u).$$
> - **(Ts)** For any bipartite joint participation measure $P^{AB}$ normalized to $\langle P^{AB} \mid P^{AB} \rangle = 1$, the CHSH correlation satisfies $|S| \leq 2\sqrt{2}$.
>
> *The four-band orthogonality is a primitive-level substrate fact (P04 §1.5), not derived here. Why the substrate partitions into exactly four mutually orthogonal bands is upstream content (Primitive-Forcing Meta-Paper).*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#2 results.** The participation measure ($|P_K|^2 = b_K$) and the Born rule supply the structural arena on which the inner product is built.
- **Four-band orthogonality (P04 §1.5).** The substrate's bandwidth decomposes into four mutually orthogonal bands (internal, adjacency, environmental, commitment-reserve). This orthogonality is a primitive-level structural commitment; it is the substrate-level source of inner-product orthogonality on the participation manifold. *Why four bands and not three or five, and why orthogonal at the primitive level, is upstream content.*
- **Bandwidth additivity (P04).** Provides the $\ell^2$ summation structure that supports the sesquilinear pairing.

The Tsirelson bound emerges from standard Landau-Khalfin operator-norm algebra applied to the substrate-derived inner-product structure. The novelty is again the substrate-level origin of the arena, not the Landau-Khalfin machinery itself.

(Existing §3.1 What is FORCED, §3.2 What is INHERITED, §3.3 What is OUT OF SCOPE — unchanged.)

---

## Paper #4 — Schrödinger Equation (Stone-Theorem Route)

### Revised Abstract

The Schrödinger equation $i\hbar\,\partial_t \psi = \hat{H}\psi$ is the dynamical postulate of non-relativistic quantum mechanics: linear, first-order in time, unitary, with a Hermitian generator. This paper shows that, **given the substrate primitives of Papers #1–#3 plus time-homogeneity (P13)**, the entire structure is forced via Stone's theorem applied to the substrate's time-translation symmetry: linearity, unitarity, first-order-in-time form, and Hermiticity of the generator each follow from the substrate-derived Hilbert-space arena together with strongly continuous one-parameter symmetry. Nonlinear, higher-order, non-unitary, non-Hermitian, real-vector-space, and quaternionic alternatives are excluded. The unique surviving dynamical law is the linear unitary one-parameter group whose differential form is $i\hbar\,\partial_t P = \hat{H} P$. The claim is conditional: the substrate's time-homogeneity primitive (P13) is load-bearing — without it, Stone's theorem cannot be invoked. Why the substrate has time-homogeneity rather than time-inhomogeneous primitive structure is upstream content for the Primitive-Forcing Meta-Paper.

### Revised §2 Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#3 results and time-homogeneity (P13)*. Then the unique time-evolution law on the participation manifold is the linear unitary one-parameter group $\{U_t\}_{t \in \mathbb{R}}$ whose differential form is
> $$i\hbar\,\partial_t P(t) = \hat{H}\,P(t).$$
>
> *Linearity, first-order-in-time form, unitarity, and Hermiticity of the generator are forced via Stone's theorem applied to the substrate-derived Hilbert space + time-homogeneity. The time-homogeneity primitive is load-bearing input, not derived here.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#3 results.** The participation measure, Born rule, and sesquilinear inner product supply the Hilbert-space arena on which Stone's theorem operates.
- **Time-homogeneity (P13).** The substrate's primitive time-translation symmetry — that the laws governing chain dynamics are independent of the absolute time coordinate. *Why the substrate is time-homogeneous (rather than time-inhomogeneous, or having no preferred time direction at all) is upstream content.*
- **Strong continuity of time-translation operators on the participation manifold.** A regularity condition on how time-translation acts on the Hilbert-space arena; required for Stone's theorem to apply. Treated as inherited from the substrate's primitive-level continuity properties.

The Stone-theorem machinery itself is standard mathematics; the substrate's contribution is the arena and the time-homogeneity primitive that justifies invoking Stone in the first place.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #5 — Gauge Fields (Theorem 17)

### Revised Abstract

The gauge structure of standard physics — local symmetry, gauge potentials $A_\mu$, covariant derivatives, field strengths, minimal coupling — is normally a list of postulates. This paper shows that, **given the substrate primitives of Papers #1–#4 plus the substrate's primitive rule-type structure (the substrate supports multiple structural rule-types $\tau_g$ with their own participation measures)**, the entire gauge architecture is forced as Theorem 17 with nine load-bearing clauses: the gauge potential is the participation measure of a rule-type $\tau_g$; the group structure admits non-Abelian Lie algebras with Killing-form / Jacobi closure; the matter-gauge vertex is vertex-anchored minimal coupling; the field strength is the commutator of transported phases; the worldline structure for massless excitations is lightlike; the vacuum sector carries a gauge-invariant UV-finite V1-form fluctuation envelope; all four channels respect a single unified gauge-quotient. The specific gauge group (U(1), SU(2), SU(3), or otherwise) and coupling magnitudes are inherited from the value layer. The claim is conditional: the rule-type primitive — that the substrate supports gauge-rule-types alongside matter-rule-types — is itself a primitive-level structural commitment, not derived here. Postulated-gauge, global-only-symmetry, non-connection-based, and quaternionic alternatives are each excluded *given that primitive*. Whether the rule-type primitive itself is necessary (and what forces it from a deeper layer) is upstream content for the Primitive-Forcing Meta-Paper.

### Revised §2 Claim

> **Theorem 17 (Gauge-Field-as-Rule-Type, T17).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#4 results plus the rule-type primitive (the substrate supports multiple structural rule-types $\tau_\bullet$ with their own participation measures)*. Then there exists a rule-type $\tau_g$ whose participation measure $A_\mu$ is FORCED to satisfy clauses C1–C9 (see body). The form of the gauge structure is forced. The specific gauge group, coupling magnitudes, and matter-content selections are inherited.
>
> *The rule-type primitive is load-bearing; why the substrate has multiple rule-types is upstream content (Primitive-Forcing Meta-Paper).*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#4 results.** The participation-manifold Hilbert space and its dynamics.
- **Rule-type primitive.** The substrate supports multiple structural rule-types — distinct classes of channel structure, each with its own participation measure. Matter and gauge are *different rule-types*, not different states of the same rule-type. *Why the substrate has this multi-rule-type structure is upstream content.*
- **Polarity-transport between adjacent loci (substrate-level connection structure).** The mechanism by which polarity at one locus is transported to a neighboring locus along edges of the participation graph. The substrate-level analog of a connection; load-bearing for the field-strength clause C5.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #6 — Hamiltonian Form + Mass

### Revised Abstract

The non-relativistic Hamiltonian $\hat{H} = \hat{p}^2/(2m) + V(\hat{x})$ — quadratic kinetic operator, factor of $1/(2m)$, additive potential — together with the appearance of inertial mass as a Lorentz-scalar parameter, is normally a postulate. This paper shows that, **given the substrate primitives of Papers #1–#4 plus the Galilean Lie algebra acting on the participation manifold and the four-band partition (P04 §1.5)**, the entire structure is forced: the kinetic-plus-potential decomposition follows from translation invariance plus locality; the quadratic dependence on $\hat{p}$ follows from rotational invariance plus the non-relativistic-limit scope; the factor of $1/(2m)$ falls out of the Galilean commutator $[\hat{H}, \hat{K}] = -i\hbar\hat{p}$ as the integration Jacobian; and mass appears structurally as a Lorentz-scalar bandwidth-signature functional $\sigma_\tau$ with units of energy. Numerical mass values, mass ratios, and generation counts are inherited from the value layer. The claim is conditional: the Galilean symmetry structure is treated here as a property of the substrate's primitive symmetry content rather than as a derived result. Why the substrate carries Galilean symmetry at the non-relativistic scope (and Poincaré at the relativistic scope) is upstream content for the Primitive-Forcing Meta-Paper.

### Revised §2 Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#4 results, Galilean symmetry of the participation manifold, four-band partition (P04 §1.5)*. Then the self-adjoint Hamiltonian generator of Paper #4 is uniquely (up to inherited numerical values) the operator
> $$\hat{H} = \frac{\hbar^2\,|\hat{p}|^2}{2m} + V(\hat{x}),$$
> with mass $m$ appearing as a Lorentz-scalar bandwidth-signature functional.
>
> *Galilean symmetry of the participation manifold is treated as a property of the substrate's primitive symmetry content (load-bearing input). Why the substrate has this symmetry is upstream content.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#4 results.**
- **Galilean Lie algebra acting on the participation manifold.** The substrate's symmetry content at non-relativistic scope. *Why Galilean (and not, say, Carrollian or non-symmetric) is upstream content.*
- **Four-band partition (P04 §1.5).** Enters for the bandwidth-signature mass identification.
- **Locality of $\hat{H}$ as a constraint on substrate-level dynamics.** The Hamiltonian acts locally on the participation graph. A substrate-level structural commitment.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #7 — Dirac Equation + g = 2

### Revised Abstract

The Dirac equation and the electron gyromagnetic ratio $g = 2$ are normally derived from the Clifford algebra construction with relativistic covariance and the spinor module postulated alongside. This paper shows that, **given the substrate primitives of Papers #1–#6 plus the substrate's spatial-dimension primitive (P06, the spatial axis is $\mathbb{R}^3$), Poincaré symmetry at the relativistic scope, and the individuation-exclusion primitive on two-chain configuration space**, the entire structure is forced: two-chain configuration-space topology forces $\pi_1(Q_2) = \mathbb{Z}_2$ and the spin-statistics dichotomy; the exchange-class generator coincides with the $2\pi$-rotation generator, forcing $SL(2,\mathbb{C})$ as the admissible covariance group for fermionic rule-types; Cl(3,1) is the unique frame algebra realizing the spinor representation; the Dirac equation is the unique first-order Lorentz-covariant linear equation using the Cl(3,1) frame; and the half-angle factor produces the Zeeman coefficient $q\hbar/(2m)$ in the non-relativistic limit, fixing $g = 2$. The claim is conditional on the spatial-dimension primitive (the spatial axis is specifically three-dimensional) and on the substrate's Poincaré symmetry at relativistic scope. Why the substrate has these specific symmetry and dimensional commitments is upstream content for the Primitive-Forcing Meta-Paper. Radiative corrections to $g$ are downstream of QED and out of scope.

### Revised §2 Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#6 results, P06 spatial dimension $=3$, Poincaré symmetry at relativistic scope, and individuation-exclusion on $Q_2$*. Then:
> - **(D)** The unique first-order Lorentz-covariant linear wave equation on a fermionic-rule-type participation measure is the Dirac equation.
> - **(g)** Minimal electromagnetic coupling produces, in the non-relativistic limit, $g = 2$ at the structural (tree-level) value.
>
> *The spatial-dimension and Poincaré-symmetry primitives are load-bearing; both are upstream content.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#6 results.**
- **Spatial dimension (P06).** The substrate's spatial axis is $\mathbb{R}^3$. This dimensional value is load-bearing — $\pi_1(Q_2) = \mathbb{Z}_2$ specifically in $D = 3$; in $D = 2$ it is the braid group, yielding anyons. *Why $D = 3$ at the primitive level is upstream content.*
- **Poincaré symmetry at relativistic scope.** The substrate's primitive symmetry content. Galilean is the non-relativistic limit (Paper #6); the relativistic scope requires Poincaré.
- **Individuation-exclusion on two-chain configuration space.** That two indistinguishable fermionic chains cannot coincide in the participation graph — a substrate-level structural commitment generating $Q_2 = (\mathbb{R}^3 \times \mathbb{R}^3 \setminus \Delta)/S_2$.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #8 — DCGT Gauge Translation

### Revised Abstract

The continuum gauge potential $A_\mu(x)$, the field strength $F_{\mu\nu}(x)$, and the covariant derivative $D_\mu$ are the standard objects of classical electrodynamics and Yang-Mills theory. They are normally postulated as continuum primitives with their transformation properties imposed as axioms. This paper shows that, **given the discrete gauge-rule-type structure of Paper #5 plus the hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ and the standard regularity assumptions of the Diffusion Coarse-Graining Theorem (DCGT, Arc D)**, the continuum gauge structure is forced as the unique hydrodynamic-window coarse-graining of the discrete substrate connection. Non-local-limit, non-connection-limit, non-tensorial, and non-covariant alternatives are excluded. The claim is conditional on the hydrodynamic-window assumption: outside that scale separation, the substrate-to-continuum bridge does not apply, and the discrete substrate content is what is fundamental. The hydrodynamic-window assumption is itself empirically robust (covers all observed gauge phenomena down to the Planck scale) but is a load-bearing input, not derived here.

### Revised §2 Claim

> **Forcing Theorem (DCGT, gauge sector, conditional on substrate primitives + hydrodynamic-window).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Paper #5 discrete gauge-rule-type structure, plus hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$*. Then the discrete substrate gauge content coarse-grains uniquely to the standard continuum gauge structure $(A_\mu, F_{\mu\nu}, D_\mu)$ with the standard local-gauge transformation laws.
>
> *The hydrodynamic-window assumption is load-bearing. Outside its applicability, discrete substrate content is fundamental and continuum gauge fields are not defined.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Paper #5 discrete gauge-rule-type structure.** Provides the substrate-level discrete connection content.
- **Hydrodynamic-window scale separation.** The assumption $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. Empirically robust at all observed scales but a load-bearing structural assumption: in regimes where this separation fails (e.g., near Planck-scale curvature or in highly turbulent gauge fields with $L_\mathrm{flow} \sim \ell_P$), the DCGT bridge does not apply.
- **DCGT regularity assumptions (Arc D).** Standard smoothness and boundedness conditions on the coarse-graining kernel; treated as inherited from Arc D's closure.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #9 — Newton's $G$ + $a_0$ + BTFR + ECR

> *Note: Paper #9 is a wedge paper — it produces structural content that standard QM reconstruction programs do not touch (Newton's $G$ from substrate constants, $a_0$ from cosmological parameters, slope-4 BTFR). The honesty revision is lighter here because the existing framing already names the substrate-level mechanisms; the change is to make explicit that the holographic counting bound and the dipole-mode projection are themselves load-bearing primitives.*

### Revised Abstract

Newton's law of gravitation, the MOND-class transition acceleration $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$, and the slope-4 baryonic Tully-Fisher relation $v_\mathrm{flat}^4 = G M a_0$ are normally three independent empirical facts: Newton as a postulate, $a_0$ as a phenomenological parameter, and BTFR as an observed correlation. This paper shows that, **given the substrate primitives of Papers #1–#8 plus (i) a holographic participation-count bound on closed 2-surfaces, (ii) a cosmic decoupling surface at radius $R_H = c/H_0$ with dipole-mode projection onto an accelerating chain's adjacency structure, and (iii) the substrate-level stability landscape $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$**, all three are forced: Newton's law arises from cumulative-strain reading of the stability landscape combined with the holographic bound, with $G = c^3\ell_P^2/\hbar$; the transition acceleration $a_0 = cH_0/(2\pi)$ arises from the dipole-mode projection; the slope-4 BTFR follows from composing these with the ED Combination Rule (a substrate-level multiplicative combination law for bilocal source contributions). Dark-matter, MOND-as-phenomenology, emergent-gravity, and modified-inertia alternatives are excluded by substrate-condition violation. The claim is conditional: the holographic counting, the decoupling-surface dipole projection, and the stability-landscape primitive are upstream substrate-level structural commitments. They are load-bearing for the forcing chain; why the substrate has them at the primitive level is upstream content for the Primitive-Forcing Meta-Paper.

### Revised §2 Claim

> **Forcing Theorem (Substrate Gravity, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#8 results plus holographic participation-count bound, cosmic decoupling surface with dipole projection, and stability-landscape primitive*. Then:
> - **(T19)** $a_N = GM/R^2$ with $G = c^3\ell_P^2/\hbar$.
> - **(T20)** $a_0 = cH_0/(2\pi)$.
> - **(ECR)** $a = \sqrt{a_N \cdot a_0}$ in the deep-MOND regime.
> - **(T21)** $v_\mathrm{flat}^4 = GMa_0$ (slope-4 BTFR).
>
> *Holographic counting, dipole projection, and stability landscape are substrate-level load-bearing primitives, not derived here.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#8 results.** Especially DCGT (substrate-to-continuum bridge for canonical-ED dynamical content).
- **Holographic participation-count bound.** The number of channels connecting a source at $M$ to a distant chain at $R$ is bounded by $N = 4\pi R^2/\ell_\mathrm{ED}^2$. A substrate-level structural commitment.
- **Cosmic decoupling surface + dipole-mode projection.** The substrate's primitive cosmological boundary at $R_H = c/H_0$ and the leading anisotropic projection mode on an accelerating chain. Load-bearing for $a_0$.
- **Stability landscape $\Sigma$.** Substrate-level functional whose extrema govern chain dynamics. Treated as a substrate primitive.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #10 — Black-Hole Architecture + Hawking Spectrum

> *Note: Paper #10 is a wedge paper — substrate-level mechanism for horizons, Hawking spectrum via V5 imaginary-time periodicity, trans-Planckian resolution, and Planck-mass remnant. The honesty revision names the V1/V5 kernel structure and DCGT as load-bearing primitives.*

### Revised Abstract

Black holes carry the strongest structural puzzles in modern physics: horizons, singularities, thermality, the information paradox, the trans-Planckian problem. The standard treatment derives Hawking radiation from quantum field theory on a curved background, with the curved background, the matter-field modes, and the unitarity of the underlying theory all taken as inputs. This paper shows that, **given the substrate primitives of Papers #1–#9 plus the V1/V5 kernel structure (V1 retarded vacuum kernel, V5 cross-chain correlation kernel) and the DCGT substrate-to-continuum bridge**, the entire black-hole architecture and the Hawking spectrum are forced from substrate primitives. Horizons are decoupling surfaces of substrate cross-bandwidth, not geometric boundaries. Singularities are excluded by substrate gradient saturation. Information is blocked from crossing horizons but entanglement straddles, dissolving the information paradox. The Hawking spectrum at $T_H = \kappa/(2\pi)$ follows from V5-kernel imaginary-time periodicity. The trans-Planckian problem is resolved by the V5 cutoff. A Planck-mass remnant is forced as the late-time evaporation endpoint via higher-order resummation. The verdict is **regulated completion** of semiclassical Hawking. The claim is conditional: the V1/V5 kernel primitives are upstream substrate-level structural commitments. They are load-bearing here; why the substrate has these specific kernel rule-types is upstream content for the Primitive-Forcing Meta-Paper.

### Revised §2 Claim

> **Forcing Theorem (BH Architecture + Hawking Spectrum, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#9 results, V1 retarded vacuum kernel, V5 cross-chain correlation kernel, DCGT*. Then BH-2 (decoupling-surface horizons), BH-3 (no singularities), BH-4 (information blocking + entanglement straddling), BH-5 (area-law form), H-1 ($T_H = \kappa/(2\pi)$), greybody factors, Page curve, trans-Planckian resolution, and Planck-mass remnant are all forced.
>
> *V1/V5 kernel structure is load-bearing substrate primitive content, not derived here.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#9 results.**
- **V1 retarded vacuum kernel.** Finite-width, retarded-support vacuum-fluctuation kernel (Theorems N1 + T18, written up in Papers #18–#19). Load-bearing for vacuum-sector content and the trans-Planckian cutoff.
- **V5 cross-chain correlation kernel.** Substrate primitive supporting cross-chain temporal correlations; load-bearing for imaginary-time periodicity → KMS → Planck distribution chain.
- **DCGT substrate-to-continuum bridge.** Load-bearing for identifying substrate Hawking flux with semiclassical Hawking at leading order.
- **Hydrodynamic-window scale separation.** Required for DCGT applicability (cf. Paper #8).

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #11 — Heisenberg Uncertainty

### Revised Abstract

The Heisenberg uncertainty relation $\Delta x\,\Delta p \geq \hbar/2$ is normally presented as a theorem about Fourier transforms on Hilbert space, or as an operator-algebraic identity following from $[\hat{x},\hat{p}] = i\hbar$. This paper shows that, **given the substrate primitives of Papers #1–#4 plus the four-band partition (P04 §1.5), specifically its primitive adjacency-band content with Fourier-conjugate $b_x$ / $b_p$ structure**, the uncertainty relation is recovered at the substrate level via the bandwidth-allocation inequality, with the standard Weyl-Fourier inequality emerging as its continuum form after identifying $b_x \propto |\Psi|^2$ and $b_p \propto |\tilde\psi|^2$ via the Born rule (Paper #2). The honest framing: the mathematical content of the bound is the standard Weyl-Fourier inequality on $L^2$; ED's substantive contribution is the substrate-level locus where the inequality lives (the adjacency-band Fourier-conjugate partition is the substrate-level source of the position-momentum conjugate pair). Operator-algebraic alternatives, real-valued alternatives, and non-Fourier-conjugate alternatives are excluded by substrate-condition violation. The claim is conditional on the four-band partition primitive and on the Fourier-conjugate substrate structure of the adjacency band, which are upstream content for the Primitive-Forcing Meta-Paper.

### Revised §2 Claim

> **Forcing Theorem (Heisenberg from Four-Band Partition, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#4 results plus four-band partition with adjacency-band Fourier-conjugate $b_x/b_p$ structure (P04 §1.5)*. Then the bandwidth-allocation inequality on the Fourier-conjugate adjacency-band partition, identified with $|\Psi|^2$ and $|\tilde\psi|^2$ via the Born rule, produces
> $$\Delta x\,\Delta p \geq \hbar/2.$$
>
> *The substantive contribution is the substrate-level origin of the conjugate-variable pair (the adjacency-band partition). The $\hbar/2$ value follows from the standard Weyl-Fourier inequality once $b_x \propto |\Psi|^2$ and $b_p \propto |\tilde\psi|^2$ are identified via Born — i.e., the inequality's mathematical content is standard $L^2$ Fourier analysis, with ED supplying the substrate-level locus.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#4 results.**
- **Four-band partition with adjacency-band Fourier-conjugate structure (P04 §1.5).** Load-bearing — the substrate-level conjugate-variable pair $(b_x, b_p)$ is the primitive carrier of the position-momentum content.
- **Standard $L^2$ Weyl-Fourier inequality.** Mathematical infrastructure (Weyl 1928); ED does not rederive it. The substrate's contribution is supplying the conjugate-variable structure on which the inequality is then standard.

**Honest reading.** This paper does not derive a new uncertainty inequality. It derives the substrate-level origin of the standard inequality's conjugate-variable pair. The $\hbar/2$ value follows from standard Fourier-transform normalization applied to substrate-derived continuum amplitudes — i.e., from standard $L^2$ Fourier analysis combined with the Born-rule identification. The novel content is *where the inequality lives at the substrate level*, not the inequality itself.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #12 — Momentum Operator

### Revised Abstract

The momentum operator $\hat{p} = -i\hbar\nabla$ is the structural backbone of position-momentum quantum mechanics. This paper shows that, **given the substrate primitives of Papers #1–#3 plus spatial homogeneity (P03 + P06)**, the operator is forced by Stone's theorem applied to the substrate's spatial-translation symmetry. The derivation is the spatial analog of Paper #4's time-translation argument. Nonlinear, higher-order, real-valued, non-unitary, and non-Stone-theorem alternatives are excluded. The claim is conditional on spatial-homogeneity primitive content; why the substrate is spatially homogeneous (rather than having spatial inhomogeneity at the primitive level) is upstream content for the Primitive-Forcing Meta-Paper. As with Paper #4, the Stone-theorem machinery is standard mathematics — the substrate's contribution is supplying the arena and the spatial-homogeneity primitive that justifies invoking Stone.

### Revised §2 Claim

> **Forcing Theorem (Momentum Operator, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#3 results, spatial homogeneity (P03 + P06)*. Then the unique self-adjoint generator of spatial translations is $\hat{p} = -i\hbar\nabla$.
>
> *Spatial homogeneity is load-bearing input, not derived here.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#3 results.**
- **Spatial homogeneity (P03 + P06).** The substrate's primitive spatial-translation symmetry. Load-bearing — Stone's theorem requires this.
- **Strong continuity of spatial-translation operators.** Regularity condition on the substrate's primitive-level continuity. Treated as inherited.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #13 — Schrödinger Emergence in Thin-Participation Limit

### Revised Abstract

The Schrödinger equation $i\hbar\,\partial_t\Psi = \hat{H}\Psi$ was forced in Paper #4 via Stone's theorem applied to the participation-manifold Hilbert space. This paper supplies a structurally distinct route: the Schrödinger equation emerges as the **continuum limit of substrate-level discrete-channel dynamics in the thin-participation regime**. **Given the substrate primitives of Papers #1–#4 plus the thin-participation regime ($M_\mathrm{eff} \to \infty$, $b_\mathrm{env} \to 0$, $\Gamma_\mathrm{commit} \to 0$) and the substrate-level per-channel evolution rule $i\hbar\,\partial_t P_K = H_K P_K + \sum_{K'} V_{KK'} P_{K'}$**, the continuum limit produces the standard Schrödinger PDE on the coherent-sum wavefunction $\Psi(x,t) = \sum_K P_K(x,t)$. The two routes (Stone's theorem on the assumed arena, thin-limit continuum coarse-graining) converge on the same equation; together they over-determine the result. The claim is conditional on the per-channel evolution rule, which is itself a substrate-level structural commitment derived from bandwidth conservation + commitment-event timing. The thin-participation regime is empirically robust for canonical QM (single-particle Schrödinger experiments operate in this regime); outside it, the substrate's discrete-channel content is what is fundamental.

### Revised §2 Claim

> **Forcing Theorem (Schrödinger from Thin-Participation Limit, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#4 results, thin-participation regime, per-channel evolution rule*. Then the coherent-sum wavefunction satisfies the standard Schrödinger PDE.
>
> *The thin-participation regime is load-bearing; outside it (e.g., environmental decoherence, active commitment events), discrete substrate content dominates and continuum Schrödinger does not apply.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#4 results.**
- **Thin-participation regime ($M_\mathrm{eff} \to \infty$, $b_\mathrm{env} \to 0$, $\Gamma_\mathrm{commit} \to 0$).** Substrate-level limit in which continuum Schrödinger emerges. Outside this regime, substrate-level discrete dynamics dominate.
- **Per-channel evolution rule.** Substrate-level dynamical equation; treated as a primitive-derived structural commitment.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #14 — Born Rule via Participation-Bandwidth Ratio

### Revised Abstract

The Born rule was forced in Paper #2 via two routes (direct + Gleason-Busch). This paper supplies a standalone forcing of the **operational route**: the rule is read off as the bandwidth-fraction governing commitment-event outcomes. **Given the substrate primitives of Paper #1 plus Primitive P11 (commitment with environmental phase-randomization on a uniform $U(1)$ distribution) and bandwidth additivity (P04)**, the quadratic form is forced by the participation-measure identity $|P_K|^2 = b_K$ — bandwidth is the substrate-level non-negative additive quantity, and the participation-measure identity makes the rule quadratic by *construction*. The substantive substrate content is therefore: the rule is quadratic because $|P_K|^2 = b_K$ at the primitive level. Linear, higher-power, contextual, signed, and non-additive alternatives are excluded. The claim is conditional: the phase-randomization-on-uniform-$U(1)$ primitive (P11) is load-bearing. Why the substrate has uniform-$U(1)$ phase-randomization is upstream content for the Primitive-Forcing Meta-Paper. **Honest reading**: this paper does not derive the Born rule independently of P11; it shows that *given* P11's uniform-phase-randomization, the quadratic form is forced. The uniform-$U(1)$ assumption is itself a substantial structural commitment closely tied to the P09 polarity primitive.

### Revised §2 Claim

> **Forcing Theorem (Born via Bandwidth Ratio, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Paper #1 result, bandwidth additivity (P04), commitment-with-uniform-$U(1)$-phase-randomization (P11)*. Then operational frequencies of commitment outcomes converge to the bandwidth-fraction
> $$\text{Prob}(K \mid u) = b_K(u)/\sum_{K'} b_{K'}(u) = |P_K(u)|^2/\sum_{K'} |P_{K'}(u)|^2.$$
>
> *The uniform-$U(1)$ phase-randomization is load-bearing; it is what kills cross-channel coherence and produces the quadratic rule. Why the substrate has this primitive is upstream content.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Paper #1 result ($|P_K|^2 = b_K$).** The quadratic form inherits directly.
- **Bandwidth additivity (P04).** Needed for $\sigma$-additivity.
- **Commitment with uniform-$U(1)$-phase-randomization (P11).** Load-bearing — this is the mechanism producing the post-commitment incoherent mixture. The uniform-$U(1)$ character of the phase distribution is itself a substantial structural commitment closely related to the P09 polarity primitive. *Why this primitive has this character is upstream content.*

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #15 — Adjacency-Bandwidth Kinetic Structure

### Revised Abstract

The non-relativistic kinetic-energy operator $\hat{T} = \hat{p}^2/(2m)$ was forced in Paper #6 via Galilean Lie algebra closure on the participation-manifold Hilbert space. This paper supplies a structurally distinct route via the **adjacency-bandwidth partition** of Primitive P04 §1.5. **Given the substrate primitives of Papers #1–#6 plus the adjacency-band partition with Fourier-conjugate $b_x$ / $b_p$ structure (Paper #11), Galilean covariance, and rotational isotropy**, bandwidth-flow between position-adjacency and momentum-adjacency components produces the unique quadratic kinetic operator with the standard $1/(2m)$ scaling. The two routes (Paper #6's Galilean Lie algebra, this paper's adjacency-bandwidth-flow) converge on the same operator. Linear, higher-order, non-local, real-valued, and non-Galilean alternatives are excluded. The claim is conditional on the adjacency-band partition and Galilean symmetry primitives; both are upstream content for the Primitive-Forcing Meta-Paper.

### Revised §2 Claim

> **Forcing Theorem (Adjacency-Bandwidth Kinetic Structure, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#6 results, adjacency-band Fourier-conjugate $b_x/b_p$ structure (Paper #11), Galilean covariance, rotational isotropy*. Then bandwidth-flow between position-adjacency and momentum-adjacency produces $\hat{T} = -\hbar^2\nabla^2/(2m)$.
>
> *Adjacency-band partition and Galilean symmetry are load-bearing substrate primitives.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#6 results.**
- **Adjacency-band Fourier-conjugate structure (P04 §1.5 + Paper #11).** Load-bearing — supplies the conjugate-variable pair.
- **Galilean covariance + rotational isotropy of the substrate symmetry content.** Load-bearing for the specific quadratic + $1/(2m)$ scaling.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #16 — Phase-Independence of Bandwidth

### Revised Abstract

That physical observables in quantum mechanics depend only on $|\psi|^2$ and are invariant under $\psi \to e^{i\theta}\psi$ — the global $U(1)$ phase redundancy — is one of QM's foundational structural facts. This paper shows that, **given the substrate primitives of Papers #1–#2 — specifically the structural distinction between bandwidth (P04, real, non-negative) and polarity (P09, $U(1)$-valued angular), and the participation-measure identity $|P_K|^2 = b_K$ from Paper #1** — phase-independence of bandwidth values is forced. The argument is structurally short: bandwidth is the substrate-level real-valued non-negative primitive, the participation measure carries it as the squared modulus, and the squared modulus is by construction $U(1)$-invariant. Bandwidth-derived observables (Born outcomes, kinetic content, uncertainty variances) inherit phase-independence. The claim is conditional on the substrate-level distinction between bandwidth and polarity as separate primitive quantities — itself a non-trivial structural commitment. **Honest reading**: this paper does not derive the global $U(1)$ gauge redundancy from "nothing"; it shows that *given* the substrate's primitive-level distinction between bandwidth (real, non-negative) and polarity ($U(1)$-angular), the redundancy is structurally inevitable. The result is closer to *making explicit* a consequence already latent in P04 + P09 + Paper #1 than to a new forcing theorem; we present it because the resulting clarity matters for downstream gauge structure.

### Revised §2 Claim

> **Forcing Theorem (Phase-Independence, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#2 results, P04 bandwidth as real-non-negative scalar, P09 polarity as $U(1)$-angular*. Then bandwidth values are invariant under all phase transformations:
> $$b_K(u) = |P_K(u)|^2 = |e^{i\theta_K(u)}P_K(u)|^2.$$
> Bandwidth-derived observables inherit this phase-independence, forcing the global $U(1)$ gauge redundancy of the substrate-derived Hilbert-space arena.
>
> *Honest framing: this is making explicit a consequence of P04 + P09 + Paper #1, not deriving a new theorem from independent primitives.*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **Papers #1–#2 results.**
- **P04 (bandwidth as real-valued non-negative primitive).** Load-bearing — phase-independence follows because bandwidth is *not* the angular primitive.
- **P09 (polarity as $U(1)$-valued angular primitive, distinct from bandwidth).** The substrate-level primitive distinction between bandwidth and polarity is what makes phase-independence non-trivially structural rather than tautological.

**Honest reading.** The result is structurally short because the work is done by P04 + P09 + Paper #1. We present it as a standalone clarification because foregrounding the substrate-level origin of $U(1)$ gauge redundancy matters for downstream gauge structure (Paper #5).

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

## Paper #17 — Four Postulates Unified (Synthesis)

### Revised Abstract

Standard quantum mechanics is built on four logically independent postulates: state space, dynamics, measurement, and composition. This paper shows that, **given the full substrate primitive set $\{P03, P04, P06, P07, P09, P11, P13\}$ together with the four-band partition (P04 §1.5) and the participation-measure result of Paper #1**, all four postulates arise jointly and uniquely from a single substrate object — the participation measure $P_K(u) = \sqrt{b_K(u)} \cdot e^{i\pi_K(u)}$ — together with its associated substrate-level primitives. The unification is structural rather than rhetorical: two foundational substrate-level identities — the squared-modulus identity $|P_K|^2 = b_K$ and the joint symmetry-and-partition content (time + spatial homogeneity, four-band orthogonality, commitment events) — together force all four postulates as facets of one structure. Mainstream axiomatic and reconstruction programs (Dirac-von Neumann, Hardy 2001, Masanes-Müller 2011, Chiribella-D'Ariano-Perinotti, Coecke-Kissinger, QBism, GPT) are compared substantively, with ED's distinguishing features located in *(i)* the substrate-level origin of the Hilbert-space arena (vs. operational reconstruction taking the arena as given), and *(ii)* the structural rather than postulational character of the four-postulate unification. **The honest framing**: ED is a substrate-ontology + reconstruction program. The "four postulates" of standard QM are unified at the substrate level, but the substrate primitives that do the unifying (especially P04, P09, P11, P13, and the four-band partition) are themselves load-bearing inputs, not consequences of this paper. Why those specific primitives — and not others — is the subject of the Primitive-Forcing Meta-Paper.

### Revised §2 Claim

> **Forcing Theorem (Unification of the Four QM Postulates, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: primitive set $\{P03, P04, P06, P07, P09, P11, P13\}$ + four-band partition (P04 §1.5) + participation-measure structure (Paper #1)*. Then the four standard QM postulates — state space, dynamics, measurement, composition — arise jointly and uniquely from the participation measure and its associated substrate primitives, via two foundational substrate-level identities:
> - **Pillar 1**: $|P_K|^2 = b_K$.
> - **Pillar 2**: substrate symmetry-and-partition content.
>
> *The substrate primitives are load-bearing; why those primitives (and not others) is upstream content (Primitive-Forcing Meta-Paper).*

### Revised §3 Scope (add §3.0; existing 3.1–3.3 unchanged)

**3.0 Primitive Inputs (load-bearing, not derived in this paper)**

- **The full substrate primitive set $\{P03, P04, P06, P07, P09, P11, P13\}$.** Each is doing load-bearing work in at least one of the four postulates.
- **Four-band partition (P04 §1.5).** Load-bearing for inner-product orthogonality, kinetic structure, and adjacency-band uncertainty content.
- **Participation-measure structure ($|P_K|^2 = b_K$ from Paper #1).** Load-bearing for the quadratic form of the Born rule, the global $U(1)$ gauge redundancy, and the Heisenberg $\hbar/2$ bound.

**Honest reading.** ED's substantive synthesis claim is that the four QM postulates, normally presented as logically independent, are *facets of one substrate object* — once the substrate primitives are in place. This is a genuine structural insight not present in postulational QM. It is also conditional: the substrate primitives themselves remain load-bearing inputs, not derived from a deeper layer in any paper of the current series. ED is therefore best characterized as a **substrate ontology + reconstruction program**, with the substrate-level synthesis as its distinguishing structural content.

(Existing §3.1, §3.2, §3.3 — unchanged.)

---

# Summary of the Revision Pattern

Across all 17 papers, the revisions share a uniform structure:

1. **Abstracts** open with the physics result, then state "Given substrate primitives [explicit list], the result is forced" rather than "Forced from substrate primitives alone." Each explicitly names which primitives are load-bearing for that paper.

2. **§2 Claims** preserve the proven content unchanged but add an explicit conditional clause naming the load-bearing primitives, plus a one-line acknowledgment that those primitives are upstream content for the Primitive-Forcing Meta-Paper.

3. **§3 Scopes** add a new **§3.0 Primitive Inputs (load-bearing, not derived here)** before the existing FORCED / INHERITED / OUT OF SCOPE subsections. The new subsection lists exactly which substrate-level commitments the paper takes as input, so reviewers can see at a glance what the conditional rests on.

**No proofs, derivations, vocabulary, substrate-class definitions, or §§4–10 content are altered.** The forcing theorems themselves are unchanged. What changes is the abstract framing of what those theorems prove — from "forced from substrate primitives alone" to "forced conditional on a named set of substrate primitives, whose own upstream forcing is treated in a separate meta-paper."

This eliminates the displaced-postulate overclaim without weakening any actual result.
