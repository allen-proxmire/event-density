# U4: The Forced Structure of the Non-Relativistic Hamiltonian

**Allen Proxmire**

*April 2026*

---

## Abstract

We present the structural derivation of the non-relativistic single-particle Hamiltonian $\hat{H} = \hbar^2 |\hat{p}|^2 / (2m) + V(\hat{x})$ from the Event-Density (ED) primitive stack and the now-FORCED upstream items U1, U2, U5, and Theorem 10. Operating under Framing 1 (U4 conditional on the existence of a Hermitian Hamiltonian generator, which is sibling CANDIDATE U3's content), we decompose U4 into five sub-features — channel–momentum identification (F1), plane-wave eigenfunctions (F2), quadratic-in-$|\hat{p}|^2$ kinetic structure (F3), specific coefficient $1/(2m)$ (F4), and kinetic + potential decomposition (F5) — and derive each from primitive-level inputs plus standard mathematical infrastructure. F1 follows from Stone's theorem applied to translation symmetry on the U2 Hilbert space, transferring directly from the U5 Memo 03 §1 derivation; F2 is mathematical; F5 follows from translation invariance + locality. F3 is established via four constraints (translation, rotation, analyticity, non-relativistic-limit), with all candidate alternatives — linear-in-$|\hat{p}|$, anisotropic, higher-even-power, full relativistic dispersion — explicitly dismissed within the non-relativistic scope. F4 is the methodologically distinctive content: **the factor of 2 in $1/(2m)$ is forced by integration of the Galilean commutator condition $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ against the boost generator $\hat{K} = m\hat{x} - t\hat{p}$, with the factor of 2 emerging as the integration Jacobian rather than as a convention borrowed from classical mechanics.** All seven falsifiers are dispatched within the stated scope conditions. The U4 verdict is **FORCED with form-FORCED-value-INHERITED framing**: the kinetic-energy form is uniquely derived from primitives + symmetry + scope; the mass parameter $m$ is inherited per Arc M's "form FORCED, values INHERITED" methodology, and $\hbar$ is inherited via the dimensional-atlas Madelung anchoring. The arc introduces no new structural CANDIDATEs; the conditionalities are all inherited (U3 sibling, non-relativistic-single-particle scope, gauge-coupling-free scope, mass and $\hbar$ values). The active upstream-CANDIDATE inventory of the QM-emergence Phase-1 program reduces from {U3, U4} + continuum gauge to **{U3} + continuum gauge** — one upstream item remains to close the entire Phase-1 structural-foundations program. With U4 closed, the Phase-1 theorem inventory stands at 15 forced structural theorems; Schrödinger emergence is now FORCED conditional on U3 alone. The U4 arc is the sixth and most delicate of the structural-foundations cycle (born_gleason → U2-Discrete → U2-Continuum → U5 → U1 → U4) and validates the structural-derivation methodology against six substantively different structural questions, with **dynamical content** — the form of the time-evolution generator — added to the methodology's demonstrated reach.

---

## 1. Introduction

The Schrödinger equation is one of the most directly tested structures in physics. Its non-relativistic single-particle form, $i\hbar \partial_t \psi = \hat{H} \psi$ with $\hat{H} = -\hbar^2 \nabla^2 / (2m) + V(\hat{x})$, has been used in calculations of atomic spectra, molecular bonding, semiconductor physics, neutron interferometry, and countless other empirical settings for nearly a century. The Hamiltonian's specific form — the squared-momentum kinetic energy with the specific factor $1/(2m)$, plus the additive position-dependent potential — is the structural anchor that connects the abstract evolution equation to physical observables.

In standard quantum mechanics, this Hamiltonian form is *imported* rather than derived. The kinetic-energy expression $T = p^2/(2m)$ is taken from classical mechanics, where it is the kinetic energy of a non-relativistic point particle; the operator-replacement $p \to \hat{p}$ promotes it to operator status. The factor of 2 in $1/(2m)$ is borrowed from the classical formula without further justification — it is what classical mechanics says, and quantum mechanics inherits it. The Schrödinger equation thus depends on a postulate that connects classical and quantum descriptions, with the classical form taken as primitive.

The Event-Density (ED) program asks whether this structural form can be derived rather than postulated. The QM-emergence Phase-1 framework [1] presents non-relativistic single-particle quantum mechanics as a structural consequence of a primitive ontology consisting of micro-events, participation relations, bandwidth, channels, polarity, and several auxiliary primitives. The framework's *upstream-commitment inventory* — the set of structural assumptions used in the original Phase-1 derivation — included five items labeled U1 through U5. Five arcs of the structural-foundations cycle (born_gleason [2], U2-Discrete [3], U2-Continuum [3], U5 [4], U1 [5]) have promoted the participation-measure carrier, its inner-product structure, the Born rule (Theorem 10), the adjacency-band Fourier-conjugate partition (U5), and the participation-measure construction itself (U1) from CANDIDATE to FORCED status. With the structural-foundations cycle's first five arcs closed, **two upstream commitments remained**: U3 (the participation-measure evolution equation $i\hbar \partial_t P_K = \hat{H}_K P_K + \sum V_{KK'} P_{K'}$, supplying existence + linear-first-order structure of the time-evolution generator) and U4 (the specific Hamiltonian form $\hat{H} = \hbar^2 |\hat{p}|^2 / (2m) + V(\hat{x})$, supplying the dynamical content of the kinetic energy). This paper presents the U4 arc and its verdict.

The U4 arc is the sixth and most delicate of the structural-foundations cycle. It is the first arc whose verdict is naturally framed as conditional on a *sibling CANDIDATE* (U3) — methodologically novel for the cycle — and it is the first arc whose load-bearing content concerns *dynamical structure* (the time-evolution generator's form) rather than kinematic structure (basis choice, inner product, partition). The arc's substantive structural finding is the derivation of the factor of 2 in $1/(2m)$ as an *integration Jacobian* of the Galilean Lie algebra commutator condition, rather than as a convention borrowed from classical mechanics. The arc closes FORCED at the form level, with the mass parameter $m$ and the constant $\hbar$ inherited per established ED-program methodology (Arc M for $m$; the dimensional-atlas Madelung anchoring for $\hbar$).

The paper is organized as follows. Section 2 states the U4 question precisely. Section 3 inventories the structural inputs available under Framing 1 (the methodological choice handling U3 as a sibling CANDIDATE). Section 4 decomposes U4 into five sub-features and classifies their structural status. Section 5 introduces the seven falsifiers attached to the sub-features. Sections 6–10 derive the five sub-features in turn, with Sections 9 and 10 carrying the load-bearing content (F3 quadratic structure; F4 factor-of-2 via Galilean integration). Section 11 consolidates the falsifier dispatches. Section 12 documents the conditionality ledger. Section 13 states the final U4 theorem. Section 14 documents the downstream cascade and the updated active CANDIDATE inventory. Section 15 discusses the result's significance for the Phase-1 program.

---

## 2. Statement of the U4 Question

### 2.1 The target form

The QM-emergence Phase-1 framework's Step 2 (Schrödinger emergence) targets the standard non-relativistic single-particle Hamiltonian:

$$
\hat{H} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x}) \qquad (\text{U4})
$$

with the kinetic operator $T(\hat{p}) = \hbar^2 |\hat{p}|^2 / (2m)$ depending only on momentum and the potential operator $V(\hat{x})$ depending only on position. The participation-measure framework's evolution equation (U3) is

$$
i\hbar \partial_t P_K = \hat{H} P_K + \sum_{K'} V_{KK'} P_{K'}.
$$

U4 specifies the *form* of $\hat{H}$ entering this equation; U3 supplies the *existence + linear-first-order structure* of the equation itself.

### 2.2 The five sub-features

U4 packages five structurally distinct sub-claims:

- **F1 (Channel–momentum identification).** In the thin/continuum limit, the channel index $K$ admits a continuous momentum-space coordinate $k$ via Stone's theorem on the participation graph's translation group.
- **F2 (Plane-wave eigenfunctions).** The eigenfunctions of the translation generator $\hat{p}$ in position representation are plane waves $\langle x | k \rangle = (2\pi\hbar)^{-d/2} e^{i k x / \hbar}$.
- **F3 (Quadratic-in-$|\hat{p}|^2$ kinetic structure).** $T(\hat{p}) \propto |\hat{p}|^2$, with linear-in-$|\hat{p}|$, higher-even-power ($|\hat{p}|^4, |\hat{p}|^6, \ldots$), anisotropic, and full relativistic alternatives all excluded in the non-relativistic regime.
- **F4 (Specific coefficient $1/(2m)$).** $T(\hat{p}) = \hbar^2 |\hat{p}|^2 / (2m)$ — the factor of 2 in the denominator is structural, not conventional.
- **F5 (Kinetic + potential decomposition).** $\hat{H} = T(\hat{p}) + V(\hat{x})$ with no cross terms, in the gauge-coupling-free scope.

### 2.3 The seven falsifiers

The structural status of U4 is tested by seven explicit falsifiers, each targeting a specific sub-feature:

- **Fal-1.** No momentum-basis identification (channel index does not map to momentum-space).
- **Fal-2.** Linear-in-$|\hat{p}|$ kinetic term (e.g., $T = c |\hat{p}|$, the photon-like dispersion).
- **Fal-3.** Higher-even-power terms (e.g., $T \supset c |\hat{p}|^4$ in the non-relativistic regime).
- **Fal-4.** Coefficient $\neq 1/(2m)$ — wrong factor (e.g., $T = |\hat{p}|^2 / m$ or $T = |\hat{p}|^2 / (3m)$).
- **Fal-5.** Anisotropic kinetic energy (direction-dependent).
- **Fal-6.** Position-momentum cross terms in $\hat{H}$ (e.g., $\hat{p} \hat{x}$ or $\hat{x} \hat{p}$ products in the free-plus-external-potential structure).
- **Fal-7.** Full relativistic dispersion in non-relativistic regime ($\hat{H}_\mathrm{kin} = \sqrt{|\hat{p}|^2 c^2 + m^2 c^4} - mc^2$ instead of its non-relativistic expansion).

The arc's verdict requires all seven to be dispatched within the stated scope conditions.

### 2.4 Framing 1: U4 conditional on sibling CANDIDATE U3

The U4 arc adopts **Framing 1**: U4 is derived *given* that a Hermitian Hamiltonian generator $\hat{H}$ exists on the participation-measure Hilbert space. The existence question is U3's content; U4 specifies the form. This framing is methodologically novel within the structural-foundations cycle — U4 is the first arc whose verdict is naturally framed as conditional on a sibling CANDIDATE rather than being unconditional.

Under Framing 1, U3 cannot be invoked as a *derivation input* for U4 (that would be circular: using U3 to derive the form of the operator that U3 supplies the existence of), but the existence of a Hermitian generator can be assumed as the starting point. The verdict is then "U4 FORCED conditional on U3"; promoting U3 in a subsequent arc would make U4 fully unconditional. This sibling-CANDIDATE conditionality framework is structurally analogous to the standard pattern in foundations programs where a more specific claim is conditioned on a more general existence claim that is in process.

---

## 3. Structural Inputs

The U4 arc operates with the following structural inputs, all primitive-level kinematic + inherited from prior FORCED items + standard mathematical infrastructure.

### 3.1 Primitives

- **Primitive 03 (Participation).** The participation relation between micro-events. Supplies graph homogeneity — no vertex is privileged at the primitive level. This kinematic homogeneity is the structural anchor for translation symmetry on the participation graph.
- **Primitive 06 (ED Gradient).** $\nabla \rho$ supplies a spatial direction with no preferred origin. The gradient structure underlies the spatial-axis content of the participation graph.
- **Primitive 09 (Tension Polarity).** The $U(1)$-valued polarity phase $\pi(K, x, t)$ entering the participation-measure construction $P_K = \sqrt{b_K} e^{i \pi_K}$ via U1.
- **Primitive 13 (Relational Timing).** Supplies the time-axis structure of the participation graph. Used in the F4 derivation to combine with Primitive 03's spatial translation symmetry into the full Galilean group.

### 3.2 Inherited FORCED upstream items

The U4 arc has access to all five FORCED items closed in prior arcs of the structural-foundations cycle:

- **U1 [5]:** Participation-measure construction $P_K(x, t) = \sqrt{b_K(x, t)} \cdot e^{i \pi(K, x, t)}$.
- **U2-Discrete and U2-Continuum [3]:** Sesquilinear inner product on the participation-measure space, in the discrete regime and the continuum regime (the latter with explicit conformal gauge structure).
- **U5 [4]:** Adjacency-band Fourier-conjugate partition. Particularly Memo 03 §1's Stone's-theorem derivation of the translation generator on the U2 Hilbert space, which transfers directly to F1 of the present arc.
- **Theorem 10 [2]:** Born rule via Gleason–Busch path. Used in F4 indirectly via the bandwidth-density identification $b_x \propto |\Psi(x)|^2$.

### 3.3 Mathematical infrastructure

- **Stone's theorem on one-parameter unitary groups** (Stone 1932) [10]. Used in F1 (translation generator on the U2 Hilbert space) and in F4 (Galilean unitarity).
- **Standard functional calculus on self-adjoint operators.**
- **Galilean Lie algebra and central extension** (Bargmann 1954) [11]. Used in F4 for the integration-Jacobian factor-of-2 derivation.
- **Standard Fourier transform on $L^2(\mathbb{R}^d)$.**

### 3.4 Scope conditions

Two scope conditions are inherited from Phase-1 Step 2's framing and condition U4's verdict:

- **Non-relativistic single-particle scope.** $|\hat{p}|^2 / (mc)^2 \ll 1$. Inherited from Phase-1 Step 2; conditions F3 (suppresses higher-even-power terms; rules out $|\hat{p}| c$ massless dispersion; rules out full relativistic dispersion) and F4 (selects Galilean boost structure over Lorentzian; absolute time preserved).
- **Gauge-coupling-free scope.** Magnetic vector potentials $A(\hat{x})$ would produce $T(\hat{p} - eA(\hat{x})/c)$, coupling position and momentum. F5's clean kinetic + potential decomposition holds in the absence of such gauge couplings. Gauge field theory is downstream content (Phase-2 Arc R, QFT extension), not Phase-1 Step 2.

### 3.5 Inherited values

Two numerical constants enter the U4 form expression and are inherited from prior structural commitments rather than derived within U4:

- **Mass $m$:** per Arc M's "form FORCED, values INHERITED" methodology [12]. Arc M established that ED forces the *form* of mass structure but inherits all numerical mass values, ratios, and hierarchies. U4 inherits this framing for the mass parameter in the Hamiltonian.
- **$\hbar$:** inherited via the dimensional-atlas Madelung anchoring. The numerical value of $\hbar$ is not derived from primitives; it is the structural constant that emerges via the Madelung-form correspondence between the participation-measure evolution and standard quantum mechanics.

These inheritances are the precise structural content of the form-FORCED-value-INHERITED methodological framing used throughout the cycle.

### 3.6 Forbidden inputs (under Framing 1)

The following inputs are explicitly forbidden as derivation inputs to U4:

- **U3 (sibling CANDIDATE).** The participation-measure evolution equation. Cannot be used as a derivation input — that would be circular under Framing 1. May be invoked only as a conditional ("given that a Hermitian Hamiltonian generator exists").
- **The classical Hamiltonian $H = p^2/(2m) + V(x)$ as a postulate.** Would assume the answer.
- **The Schrödinger equation in textbook form.** Would assume U3 + U4 jointly.
- **The relativistic dispersion as a derivation input.** Phase-2 Arc R's relativistic content is invoked only via the non-relativistic-limit scope; not as a derivation input directly.

---

## 4. Sub-Feature Decomposition

We summarize the five-sub-feature decomposition of U4 with explicit structural status:

| Sub-feature | Status | Structural inputs | Falsifiers |
|---|---|---|---|
| **F1** Channel–momentum identification | FORCED | Primitives 03 + 06 (translation symmetry, kinematic) + U2 (FORCED) + Stone's theorem; explicitly U3-independent | Fal-1 |
| **F2** Plane-wave eigenfunctions | FORCED (automatic given F1) | F1 + standard mathematical consequence | (none) |
| **F3** Quadratic-in-$|\hat{p}|^2$ kinetic structure | FORCED | C1 translation invariance + C2 rotation invariance + C3 analyticity + C4 non-relativistic-limit scope | Fal-2, Fal-3, Fal-5, Fal-7 |
| **F4** Specific coefficient $1/(2m)$ | FORCED form (factor of 2 derived); $m$ INHERITED per Arc M; $\hbar$ INHERITED per dimensional-atlas Madelung | Primitives 03 + 13 + non-rel scope (uniqueness of Galilean over Lorentzian) + U2 unitarity + Galilean Lie algebra integration | Fal-4 |
| **F5** Kinetic + potential decomposition | FORCED (gauge-coupling-free scope) | Translation invariance (free part) + locality (potential part) | Fal-6 |

The arc's load-bearing content is concentrated in F3 and F4. F1, F2, F5 close cleanly via established techniques.

---

## 5. Falsifier Inventory

Each of the seven falsifiers targets a specific physical alternative to the U4 form. We document what each would mean physically and how each is tested structurally.

| Falsifier | Physical meaning | Structural test | Memo |
|---|---|---|---|
| **Fal-1** No momentum-basis identification | Channel index has no momentum-space interpretation; the participation-measure framework lacks a translation-eigenstate basis | Stone's theorem on the U2 Hilbert space's translation group must produce a self-adjoint generator | Memo 02 §1 |
| **Fal-2** Linear-in-$|\hat{p}|$ kinetic term | Massless photon-like dispersion in a regime supposed to describe massive particles | Rotation invariance excludes vector-linear $\alpha \cdot \hat{p}$; analyticity at low momentum + non-rel scope excludes scalar $|\hat{p}| c$ | Memo 03 §2.4 |
| **Fal-3** Higher-even-power terms ($|\hat{p}|^4, \ldots$) | Relativistic corrections appearing in a regime supposed to be non-relativistic | Non-relativistic-limit scope suppresses all $a_n |\hat{p}|^{2n}$ for $n \geq 2$ by powers of $(v/c)^{2(n-1)}$ | Memo 03 §2.5 |
| **Fal-4** Coefficient $\neq 1/(2m)$ | Wrong proportionality between kinetic energy and momentum-squared; contradicts classical-quantum correspondence | Galilean Lie algebra commutator $[\hat{H}, \hat{K}] = -i\hbar \hat{p}$ integrated against $\hat{K} = m\hat{x} - t\hat{p}$ produces unique factor of 2 | Memo 03 §3.7 |
| **Fal-5** Anisotropic kinetic energy | Kinetic energy depends on direction of $\hat{p}$; preferred direction in space | Rotation invariance forces $T(\hat{p}) = f(|\hat{p}|^2)$ — function of squared magnitude only | Memo 03 §2.3 |
| **Fal-6** Position-momentum cross terms | Cross terms like $\hat{p} \hat{x}$ or $\hat{x} \hat{p}$ in the Hamiltonian; no clean kinetic vs potential separation | Translation invariance forbids $\hat{x}$ in free-particle Hamiltonian; locality forbids $\hat{p}$ in external potential | Memo 02 §3 |
| **Fal-7** Full relativistic dispersion in non-rel regime | $\hat{H}_\mathrm{kin} = \sqrt{|\hat{p}|^2 c^2 + m^2 c^4} - mc^2$ instead of non-relativistic expansion | Non-relativistic-limit scope: full dispersion Taylor-expands and reduces to leading $|\hat{p}|^2/(2m)$ in $c \to \infty$ limit | Memo 03 §2.6 |

---

## 6. Derivation of F1 (Momentum Identification)

### 6.1 The claim

In the thin/continuum limit of the participation-measure framework, the channel index $K$ admits a continuous momentum-space coordinate $k$. The basis-change between channel-representation and momentum-representation on the U2 Hilbert space is the standard Fourier transform, with the translation generator $\hat{p}$ a self-adjoint operator identified by Stone's theorem.

### 6.2 Translation symmetry as a kinematic property

Define spatial translation $T_a$ acting on the participation-measure space by

$$
(T_a P)_K(u) := P_K(u - a).
$$

Primitive 03's homogeneity guarantees that the participation relation does not privilege any vertex, so $T_a$ is well-defined on $\mathcal{H}$ for every translation vector $a$ in the spatial tangent space. The set $\{T_a : a \in \mathbb{R}^d\}$ forms a $d$-parameter abelian Lie group under composition.

### 6.3 Translation acts unitarily on the U2 Hilbert space

For any $P, Q \in \mathcal{H}$ and any translation $a$:

$$
\langle T_a P \mid T_a Q \rangle = \sum_K \int du \; P_K^*(u - a) \, Q_K(u - a) = \sum_K \int du' \; P_K^*(u') \, Q_K(u') = \langle P \mid Q \rangle
$$

(under change of variables $u' = u - a$). The translation group preserves the U2 inner product. Continuity of $T_a$ in $a$ follows from continuity of the participation-measure field.

### 6.4 Stone's theorem identifies the translation generator

**Theorem (Stone 1932).** *Every strongly continuous one-parameter unitary group on a Hilbert space has a unique self-adjoint generator.*

Applied to the spatial translation group, with the ED-program convention placing $\hbar$ in the exponential:

$$
T_a = \exp\!\left( \frac{i \hat{p} \cdot a}{\hbar} \right). \qquad (1)
$$

The eigenstates $|k\rangle$ of $\hat{p}$ satisfy $\hat{p} \, |k\rangle = k \, |k\rangle$ and form a complete orthonormal basis on $\mathcal{H}$. **In the thin/continuum limit, the channel index $K$ is identified with the momentum eigenvalue $k$:**

$$
K \leftrightarrow k. \qquad (2)
$$

### 6.5 Explicit U3-independence

The derivation invokes Primitives 03 + 06 (homogeneity, spatial axis), U2 (inner product preserved by translations), and Stone's theorem. **No time-evolution operator, no Hamiltonian, no Schrödinger equation appears in the argument.** Stone's theorem identifies $\hat{p}$ kinematically on the U2 Hilbert space; whether $\hat{p}$ commutes with a time-evolution generator is a U3-level question, separate from F1's content.

### 6.6 Theorem statement

> **Theorem (F1).** *Let $\mathcal{H}$ be the U2 Hilbert space of participation measures. Let $\{T_a : a \in \mathbb{R}^d\}$ be the spatial translation group acting on $\mathcal{H}$ with $T_a$ defined by $(T_a P)_K(u) := P_K(u - a)$. Then $\{T_a\}$ is a strongly continuous one-parameter unitary group on $\mathcal{H}$, and there exists a unique self-adjoint operator $\hat{p}$ such that $T_a = \exp(i \hat{p} \cdot a / \hbar)$. The eigenstates of $\hat{p}$ form a complete orthonormal basis on $\mathcal{H}$, and in the thin/continuum limit the channel index $K$ is identified with the eigenvalue $k$ of $\hat{p}$.*

**Falsifier Fal-1 dispatched.**

---

## 7. Derivation of F2 (Plane-Wave Eigenfunctions)

### 7.1 Position-representation form of $\hat{p}$

Given F1's identification of $\hat{p}$ as the translation generator, the position-representation form of $\hat{p}$ is determined by the relation between $T_a$ and translation in $x$:

$$
T_a \psi(x) = \psi(x - a) = \exp\!\left( -a \cdot \nabla \right) \psi(x)
$$

(Taylor expansion of the translated argument). Comparing with $T_a = \exp(i \hat{p} \cdot a / \hbar)$:

$$
\frac{i \hat{p} \cdot a}{\hbar} = -a \cdot \nabla \quad \Longrightarrow \quad \hat{p} = -i \hbar \nabla. \qquad (3)
$$

### 7.2 Eigenfunctions

The eigenvalue equation $\hat{p} \, |k\rangle = k \, |k\rangle$ becomes, in position representation,

$$
-i \hbar \nabla \langle x | k \rangle = k \langle x | k \rangle,
$$

with solution

$$
\langle x | k \rangle = (2\pi\hbar)^{-d/2} \cdot e^{i k \cdot x / \hbar}. \qquad (4)
$$

The normalization constant $(2\pi\hbar)^{-d/2}$ is fixed by the orthonormality requirement $\langle k | k' \rangle = \delta(k - k')$ together with the Fourier-transform convention.

### 7.3 Theorem statement

> **Theorem (F2).** *In the position representation of the U2 Hilbert space, the translation generator $\hat{p}$ takes the form $\hat{p} = -i \hbar \nabla$. The eigenfunctions of $\hat{p}$ are plane waves $\langle x | k \rangle = (2\pi\hbar)^{-d/2} \cdot e^{i k \cdot x / \hbar}$, with normalization fixed by the standard orthonormality convention.*

F2 introduces no new structural commitment beyond F1. The result is a mathematical consequence of Stone's theorem applied in the position basis.

---

## 8. Derivation of F5 (Kinetic + Potential Decomposition)

### 8.1 Translation invariance forces the free part to depend only on $\hat{p}$

In the absence of an external potential, $\hat{H}_\mathrm{free}$ commutes with translations: $[\hat{H}_\mathrm{free}, T_a] = 0$ for every translation $T_a$. This is a structural statement: the participation graph itself is translation-invariant (Primitive 03 homogeneity), and without external coupling, $\hat{H}_\mathrm{free}$ inherits this invariance.

Any operator commuting with the translation generator $\hat{p}$ depends on $\hat{p}$ alone via standard functional calculus on self-adjoint operators (a function of $\hat{x}$ would generically not commute with $\hat{p}$, since $[\hat{x}, \hat{p}] = i\hbar$). Therefore

$$
\hat{H}_\mathrm{free} = T(\hat{p}) \qquad (5)
$$

for some function $T : \mathbb{R}^d \to \mathbb{R}$ acting via spectral functional calculus on $\hat{p}$.

### 8.2 Locality forces external potentials to depend only on $\hat{x}$

Locality is a primitive-level structural property of the participation graph: edges in the edge set $E$ connect adjacent vertices, and external influences couple to the participation measure at specific locations. This locality is encoded structurally in Primitive 03's edge structure — participation relations are local, not action-at-a-distance.

In operator language, the local action of a potential on the wavefunction takes the form $(V \psi)(x) = V(x) \psi(x)$ — multiplication by a position-dependent function. This is the form $V(\hat{x})$, depending only on $\hat{x}$.

A potential depending on $\hat{p}$ would be non-local in position representation (a momentum-space multiplication corresponds to a convolution in position space). Convolution-type non-local potentials are structurally distinct from local external potentials and do not arise in the standard non-relativistic-single-particle scope.

### 8.3 Cross terms forbidden

Combining §§8.1–8.2: any cross term $\hat{p} \hat{x}$ or $\hat{x} \hat{p}$ in the Hamiltonian would violate either translation invariance (if interpreted as part of the free Hamiltonian — the $\hat{x}$ factor breaks translation symmetry) or locality (if interpreted as part of the potential — the $\hat{p}$ factor introduces non-local momentum-coupling).

### 8.4 Scope caveat: gauge-coupling structure

In the presence of magnetic vector potentials $A(\hat{x})$, the kinetic operator becomes $T(\hat{p} - e A(\hat{x})/c)$ — a function of *both* $\hat{p}$ and $\hat{x}$ via the gauge field $A$. The scope condition for U4's F5 is *non-relativistic single-particle Schrödinger emergence without gauge couplings*. Gauge field theory is downstream content, addressed by other arcs.

### 8.5 Theorem statement

> **Theorem (F5).** *Within the gauge-coupling-free non-relativistic single-particle scope of Phase-1 Step 2, the Hamiltonian operator $\hat{H}$ on the U2 Hilbert space admits the unique additive decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$, with the kinetic part depending only on the translation generator $\hat{p}$ and the potential part depending only on the position operator $\hat{x}$. Cross terms involving products of $\hat{p}$ and $\hat{x}$ are forbidden. The form of $V(\hat{x})$ is structural (a scalar function of $\hat{x}$); the specific $V$ for a given physical system is inherited from external context.*

**Falsifier Fal-6 dispatched.**

---

## 9. Derivation of F3 (Quadratic Kinetic Structure)

### 9.1 The four constraints

After F1 + F5, the Hamiltonian has the form $\hat{H} = T(\hat{p}) + V(\hat{x})$ with $T(\hat{p})$ a function of $\hat{p}$ alone. The remaining question is the specific form of $T$. We use four structural constraints:

- **C1 Translation invariance.** Already established (F5). $T = T(\hat{p})$ alone.
- **C2 Rotation invariance.** The participation graph supports rotations as a kinematic symmetry (graph isotropy from Primitive 03 + Primitive 06's spatial-axis structure with no preferred direction). $T(\hat{p})$ must commute with rotations.
- **C3 Analyticity at low momentum.** $T(\hat{p}) = f(|\hat{p}|^2)$ is analytic in $|\hat{p}|^2$ at $\hat{p} = 0$. Regularity assumption — physically motivated and standard in non-relativistic QM.
- **C4 Non-relativistic-limit scope condition.** $|\hat{p}|^2 / (mc)^2 \ll 1$. Inherited from Phase-1 Step 2's scope.

### 9.2 C1 + C2 reduce to $f(|\hat{p}|^2)$

By C1, $T = T(\hat{p})$. By C2, $T$ is invariant under rotations of $\hat{p}$. The unique rotational invariant of a vector operator $\hat{p}$ (up to powers) is the squared magnitude $|\hat{p}|^2 = \hat{p} \cdot \hat{p}$. Therefore:

$$
T(\hat{p}) = f(|\hat{p}|^2) \qquad (6)
$$

for some function $f : \mathbb{R}_{\geq 0} \to \mathbb{R}$.

**Anisotropic alternatives dismissed.** Any anisotropic candidate — e.g., $T = c_x \hat{p}_x^2 + c_y \hat{p}_y^2 + c_z \hat{p}_z^2$ with $c_x \neq c_y \neq c_z$, or $T = (\hat{p} \cdot \hat{n})^2$ for a fixed direction $\hat{n}$ — fails C2 by selecting a preferred direction in space. **Falsifier Fal-5 dispatched.**

### 9.3 C3 forces Taylor expansion with no half-integer powers

By C3, $f$ is analytic at $|\hat{p}|^2 = 0$, admitting a Taylor expansion:

$$
f(|\hat{p}|^2) = a_0 + a_1 |\hat{p}|^2 + a_2 (|\hat{p}|^2)^2 + a_3 (|\hat{p}|^2)^3 + \ldots \qquad (7)
$$

The constant term $a_0$ is an additive zero-point energy; convention sets $a_0 = 0$.

**Half-integer powers excluded.** A candidate term $a_{1/2} |\hat{p}|$ — i.e., proportional to $\sqrt{|\hat{p}|^2}$ — is *not analytic* in $|\hat{p}|^2$ at the origin (the square-root function has a branch point). Such a term is excluded by C3. Physically, the $|\hat{p}| c$ form is the photon-like dispersion of a massless particle — relativistic massless behavior, incompatible with the non-relativistic massive-particle scope condition C4.

The vector linear $\alpha \cdot \hat{p}$ is also excluded by C2 (rotation invariance forbids vector terms unless $\alpha = 0$). **Falsifier Fal-2 dispatched.**

### 9.4 C4 suppresses higher-even-power terms

In the non-relativistic regime $|\hat{p}|^2 / (mc)^2 \ll 1$, the relative size of the $a_n (|\hat{p}|^2)^n$ term to the $a_1 |\hat{p}|^2$ term is, with the natural dimensional scaling $a_n \sim a_1/(mc)^{2(n-1)}$:

$$
\frac{a_n (|\hat{p}|^2)^n}{a_1 |\hat{p}|^2} \sim \left( \frac{|\hat{p}|^2}{(mc)^2} \right)^{n-1} = \left( \frac{v}{c} \right)^{2(n-1)}.
$$

Higher-order terms are suppressed by powers of $(v/c)^2$. **In the strict non-relativistic limit $c \to \infty$ (with $v$ fixed), all $a_n$ for $n \geq 2$ vanish.** Only the leading $a_1 |\hat{p}|^2$ term survives. **Falsifier Fal-3 dispatched.**

### 9.5 Relativistic dispersion in non-relativistic regime

A candidate alternative to the polynomial Taylor expansion: the full relativistic dispersion

$$
T_\mathrm{rel}(\hat{p}) = \sqrt{|\hat{p}|^2 c^2 + m^2 c^4} - m c^2.
$$

Expanding in $|\hat{p}|^2 / (mc)^2 \ll 1$:

$$
T_\mathrm{rel}(\hat{p}) = \frac{|\hat{p}|^2}{2m} - \frac{|\hat{p}|^4}{8 m^3 c^2} + O\!\left( \frac{|\hat{p}|^6}{m^5 c^4} \right).
$$

In the strict non-relativistic limit $c \to \infty$, only the leading $|\hat{p}|^2/(2m)$ term survives. The relativistic dispersion *reduces* to the U4 form in the non-relativistic limit, consistent with U4's scope condition. **Falsifier Fal-7 dispatched.**

### 9.6 Theorem statement

> **Theorem (F3).** *In the non-relativistic single-particle gauge-coupling-free scope, the kinetic-energy operator $T(\hat{p}) = f(|\hat{p}|^2)$ on the U2 Hilbert space takes the unique form*
>
> $$T(\hat{p}) = a_1 |\hat{p}|^2$$
>
> *with $a_1 > 0$ a real constant determined by F4. All candidate alternatives — anisotropic, linear-in-$|\hat{p}|$, higher-even-power, full relativistic — are excluded by the four constraints C1 (translation invariance), C2 (rotation invariance), C3 (analyticity), and C4 (non-relativistic limit).*

**Falsifiers Fal-2, Fal-3, Fal-5, Fal-7 dispatched.**

---

## 10. Derivation of F4 (Coefficient $1/(2m)$)

### 10.1 The factor-of-2 question

Dimensional analysis fixes $a_1 \propto 1/m$ with $\hbar^2$ supplying the dimensional bridge:

$$
a_1 = c_1 \cdot \frac{\hbar^2}{m}
$$

with $c_1$ a dimensionless constant. The standard non-relativistic kinetic-energy form is $T(\hat{p}) = \hbar^2 |\hat{p}|^2 / (2m)$, corresponding to $c_1 = 1/2$. **The factor of $1/2$ is the load-bearing question** — dimensional analysis alone does not fix it.

The 2026-04-24 tightening-program memo for U4 silently adopted the factor of 2 by *convention* (matching classical Hamiltonian mechanics: $T_\mathrm{classical} = p^2/(2m)$). Under the structural-derivation methodology, this is insufficient: the factor must be derived from primitive-level inputs, not borrowed by convention from classical mechanics (which is downstream content not available as input under Framing 1).

### 10.2 Galilean Lie algebra as the load-bearing input

The Galilean Lie algebra is generated by:

- **Spatial translation generators** $\hat{P}_i$, with $[\hat{P}_i, \hat{P}_j] = 0$.
- **Time translation generator** $\hat{H}$ (under Framing 1: existence assumed; F4 specifies form).
- **Spatial rotation generators** $\hat{J}_i$.
- **Galilean boost generators** $\hat{K}_i$.

The substantive structural fact is the central-extension commutator between boosts and translations:

$$
[\hat{K}_i, \hat{P}_j] = i \hbar m \, \delta_{ij}. \qquad (8)
$$

The mass $m$ enters as the structure constant of the central extension. The boost generator takes the form

$$
\hat{K}_i = m \hat{x}_i - t \hat{p}_i. \qquad (9)
$$

The other Galilean commutators include the load-bearing relation

$$
[\hat{H}, \hat{K}_i] = -i \hbar \hat{p}_i. \qquad (10)
$$

### 10.3 Galilean is uniquely forced within the non-relativistic scope

We argue that within the non-relativistic scope condition (C4 + absolute time), the Galilean group is the unique consistent boost-translation algebra.

**Argument.** Boost-translation algebras compatible with absolute time fall into two categories:

- **Galilean group $\mathrm{Gal}(d)$.** Boosts and translations generate the Galilean Lie algebra with commutator (8). Time is absolute. Mass is the central charge.
- **Lorentzian group $\mathrm{ISO}(d, 1)$.** Boosts mix space and time. Time is *not* absolute; observers in different inertial frames see different time intervals.

In the non-relativistic regime, time is absolute by scope condition (C4). Lorentzian boost structure is therefore ruled out. The Galilean group is the unique remaining alternative within the non-relativistic scope.

Within the Galilean group, the central extension is unique up to the choice of central charge. The central charge is identified with mass $m$, inherited per Arc M.

### 10.4 Galilean transformations act unitarily on the U2 Hilbert space

The Galilean transformations must act unitarily on the U2 Hilbert space for the Galilean algebra to be a symmetry of the participation-measure framework:

- **Translations $\hat{p}$:** unitary by F1 (Stone's theorem).
- **Time translations $\hat{H}$:** assumed self-adjoint under Framing 1.
- **Spatial rotations $\hat{J}$:** unitary by C2 (rotation symmetry).
- **Galilean boosts $\hat{K} = m \hat{x} - t \hat{p}$:** the position operator $\hat{x}$ is self-adjoint (multiplication by a real coordinate); $\hat{p}$ is self-adjoint (Stone's theorem); $\hat{K}$ is self-adjoint as a real-coefficient linear combination. Therefore boosts act unitarily on $\mathcal{H}$.

All Galilean transformations are unitary on the U2 Hilbert space.

### 10.5 Momentum transformation under boosts

Under an infinitesimal Galilean boost with velocity $v$, the momentum operator transforms as

$$
\hat{p}_j \to \hat{p}_j' = e^{i \hat{K} \cdot v / \hbar} \hat{p}_j e^{-i \hat{K} \cdot v / \hbar}.
$$

Expanding to first order in $v$ and using (8):

$$
\hat{p}_j' = \hat{p}_j + \frac{i v_i}{\hbar} [\hat{K}_i, \hat{p}_j] + O(v^2) = \hat{p}_j + \frac{i v_i}{\hbar} \cdot i \hbar m \, \delta_{ij} + O(v^2) = \hat{p}_j - m v_j + O(v^2).
$$

For a finite boost:

$$
\hat{p} \to \hat{p} - m v. \qquad (11)
$$

The mass $m$ enters as the proportionality factor between boost velocity and momentum shift — exactly as in classical kinematics.

### 10.6 The integration that fixes the factor of 2

The Hamiltonian $\hat{H} = T(\hat{p})$ must satisfy the Galilean commutation relation (10):

$$
[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i.
$$

Substituting $\hat{K}_i = m \hat{x}_i - t \hat{p}_i$ and using $[\hat{H}, \hat{p}_i] = 0$ (since $\hat{H} = T(\hat{p})$ depends on $\hat{p}$ alone):

$$
[\hat{H}, \hat{K}_i] = m [T(\hat{p}), \hat{x}_i] - t [T(\hat{p}), \hat{p}_i] = m [T(\hat{p}), \hat{x}_i].
$$

Using the canonical commutation $[\hat{x}_i, \hat{p}_j] = i \hbar \delta_{ij}$ and the identity $[T(\hat{p}), \hat{x}_i] = -i\hbar (\partial T/\partial \hat{p}_i)$:

$$
[\hat{H}, \hat{K}_i] = -i \hbar m \, \frac{\partial T(\hat{p})}{\partial \hat{p}_i}.
$$

Setting equal to $-i\hbar \hat{p}_i$:

$$
\frac{\partial T(\hat{p})}{\partial \hat{p}_i} = \frac{\hat{p}_i}{m}. \qquad (12)
$$

Equation (12) is a system of differential equations for $T(\hat{p})$. Using the F3 result $T = f(|\hat{p}|^2)$, so $\partial T / \partial \hat{p}_i = 2 \hat{p}_i f'(|\hat{p}|^2)$:

$$
2 \hat{p}_i f'(|\hat{p}|^2) = \frac{\hat{p}_i}{m} \quad \Longrightarrow \quad f'(|\hat{p}|^2) = \frac{1}{2m}.
$$

Integrating with the convention $f(0) = 0$:

$$
f(|\hat{p}|^2) = \frac{|\hat{p}|^2}{2m}. \qquad (13)
$$

**The factor of 2 emerges from the integration.** Specifically: the coefficient $1/(2m)$ in $T = |\hat{p}|^2/(2m)$ comes from integrating $f'(|\hat{p}|^2) = 1/(2m)$ — the factor of 2 is the *Jacobian* relating the chain-rule derivative $\partial T/\partial \hat{p}_i = 2 \hat{p}_i f'(|\hat{p}|^2)$ to the form of the Galilean commutator. **It is not a convention; it is the result of integrating the differential equation that Galilean invariance demands.**

### 10.7 Form-FORCED, value-INHERITED

Combining F3 and F4, restoring $\hbar$ explicitly:

$$
T(\hat{p}) = \frac{\hbar^2 |\hat{p}|^2}{2m} \qquad (14)
$$

with $m$ inherited per Arc M and $\hbar$ inherited per the dimensional-atlas Madelung anchoring. The form of the kinetic-energy operator is FORCED; the values of $m$ and $\hbar$ are INHERITED. **Falsifier Fal-4 dispatched.**

### 10.8 Theorem statement

> **Theorem (F4).** *Under Framing 1 and within the non-relativistic single-particle scope, the kinetic-energy operator $T(\hat{p}) = a_1 |\hat{p}|^2$ established by F3 has*
>
> $$a_1 = \frac{\hbar^2}{2m}$$
>
> *uniquely. The factor of 2 in the denominator emerges from integrating the Galilean commutator condition $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ against the boost generator $\hat{K} = m\hat{x} - t\hat{p}$, with the factor of 2 the chain-rule Jacobian of the differentiation $\partial / \partial \hat{p}_i$ acting on $f(|\hat{p}|^2)$. The mass $m$ is inherited per Arc M; the constant $\hbar$ is inherited via the dimensional-atlas Madelung anchoring.*

---

## 11. Falsifier Resolution Table

We consolidate all seven falsifiers with their dispatch arguments and memo locations:

| Falsifier | Target sub-feature | Dispatch argument | Memo |
|---|---|---|---|
| **Fal-1** No momentum-basis identification | F1 | Stone's theorem on the U2 Hilbert space's translation group produces a unique self-adjoint $\hat{p}$; channel-momentum identification follows from the eigenstate structure | Memo 02 §1 |
| **Fal-2** Linear-in-$|\hat{p}|$ kinetic term | F3 | Vector $\alpha \cdot \hat{p}$ excluded by C2 rotation invariance; scalar $|\hat{p}| c$ excluded by C3 analyticity (branch-point at $\hat{p} = 0$) plus C4 non-relativistic-limit | Memo 03 §2.4 |
| **Fal-3** Higher-even-power terms | F3 | C4 non-relativistic-limit suppresses all $a_n |\hat{p}|^{2n}$ terms for $n \geq 2$ by powers of $(v/c)^{2(n-1)}$ | Memo 03 §2.5 |
| **Fal-4** Coefficient $\neq 1/(2m)$ — wrong factor | F4 | Integration of Galilean commutator $[\hat{H}, \hat{K}] = -i\hbar \hat{p}$ against $\hat{K} = m\hat{x} - t\hat{p}$ yields $T'(|\hat{p}|^2) = 1/(2m)$; factor of 2 is the integration Jacobian | Memo 03 §3.7 |
| **Fal-5** Anisotropic kinetic energy | F3 | C2 rotation invariance forces $T(\hat{p}) = f(|\hat{p}|^2)$; direction-dependent terms violate isotropy | Memo 03 §2.3 |
| **Fal-6** Position-momentum cross terms in $\hat{H}$ | F5 | Translation invariance forbids $\hat{x}$ in free-particle Hamiltonian; locality forbids $\hat{p}$ in external potential. Cross terms violate one or the other (gauge-coupling-free scope) | Memo 02 §3 |
| **Fal-7** Relativistic dispersion in non-rel regime | F3 | C4 non-relativistic-limit scope: relativistic dispersion Taylor-expands as $|\hat{p}|^2/(2m) + O((v/c)^2)$ and reduces to U4 form in $c \to \infty$ limit | Memo 03 §2.6 |

**All seven falsifiers dispatched within the stated scope conditions.** No physical-distinction alternative survives.

---

## 12. Conditionality Ledger

The U4 verdict is FORCED, conditional on the following — *all of which are inherited from prior structural commitments, not introduced by U4*:

### 12.1 U3 (sibling CANDIDATE; Framing 1)

U3 supplies the existence of a Hermitian Hamiltonian generator $\hat{H}$ in the participation-measure evolution equation. U4 specifies the *form* of $\hat{H}$ given that $\hat{H}$ exists. Promoting U3 in a subsequent arc would make U4 fully unconditional.

This is the natural sibling-CANDIDATE conditionality. U4 is the first arc in the structural-foundations cycle whose verdict is naturally framed as conditional on a sibling CANDIDATE — methodologically novel — but U3 was already in the active inventory before U4 closed; no new upstream item is introduced.

### 12.2 Non-relativistic single-particle scope

Phase-1 Step 2's scope condition. Conditions:
- F3: suppresses higher-even-power terms; rules out massless $|\hat{p}| c$ dispersion; rules out full relativistic $\sqrt{|\hat{p}|^2 c^2 + m^2 c^4}$.
- F4: selects Galilean boost structure over Lorentzian (absolute time preserved).

The non-relativistic scope is itself a regime choice, inherited from Phase-1 Step 2's framing.

### 12.3 Gauge-coupling-free scope

F5's kinetic + potential decomposition $\hat{H} = T(\hat{p}) + V(\hat{x})$ holds in the absence of magnetic vector potentials. With gauge couplings, the kinetic operator becomes $T(\hat{p} - eA(\hat{x})/c)$ — coupling position and momentum via the gauge field $A$. Gauge field theory is downstream content, not within Phase-1 Step 2's scope.

### 12.4 Inherited values

- **Mass $m$:** per Arc M's "form FORCED, values INHERITED" methodology [12]. The U4 verdict is at the form level; specific mass values are inherited.
- **$\hbar$:** inherited via the dimensional-atlas Madelung anchoring. The numerical value of $\hbar$ is not derived from primitives.

### 12.5 No new conditionalities introduced

**U4 introduces no new structural CANDIDATEs.** All four conditionalities listed above are inherited from prior structural commitments. The methodological discipline of the structural-foundations cycle — *introduce zero new CANDIDATEs* — is preserved by U4.

---

## 13. Final U4 Theorem (Canonical Statement)

> **Theorem 15 (U4; Specific Hamiltonian Form).** *Let the ED primitive stack supply: bandwidth (Primitive 04), spatial structure (Primitive 06), participation relations (Primitive 03), channel index (Primitive 07), tension polarity (Primitive 09), and relational timing (Primitive 13), together with the now-FORCED upstream items U1, U2-Discrete, U2-Continuum, U5, and Theorem 10. Within the non-relativistic single-particle scope of Phase-1 Step 2 (gauge-coupling-free), and conditional on the existence of a Hermitian Hamiltonian generator (sibling CANDIDATE U3, Framing 1), the Hamiltonian operator on the participation-measure Hilbert space takes the unique form*
>
> $$\hat{H} = \frac{\hbar^2 |\hat{p}|^2}{2m} + V(\hat{x})$$
>
> *with the following structural properties:*
>
> 1. ***Channel–momentum identification.*** *In the thin/continuum limit, the channel index $K$ is identified with the momentum eigenvalue $k$ via Stone's theorem on the translation group. Plane-wave eigenfunctions $\langle x | k \rangle = (2\pi\hbar)^{-d/2} e^{i k x / \hbar}$ supply the position-momentum basis change.*
>
> 2. ***Kinetic + potential decomposition.*** *$\hat{H} = T(\hat{p}) + V(\hat{x})$ — kinetic depending only on momentum, potential depending only on position. Translation invariance forces the free part; locality forces the potential part. Cross terms forbidden.*
>
> 3. ***Quadratic-in-$|\hat{p}|^2$ kinetic structure.*** *$T(\hat{p}) = a_1 |\hat{p}|^2$ uniquely, by the four constraints C1 (translation invariance) + C2 (rotation invariance) + C3 (analyticity) + C4 (non-relativistic-limit). Linear-in-$|\hat{p}|$, higher-even-power, anisotropic, and relativistic-dispersion alternatives all dismissed.*
>
> 4. ***Specific coefficient $\hbar^2/(2m)$.*** *$a_1 = \hbar^2/(2m)$, with the factor of 2 forced by integration of the Galilean commutator condition $[\hat{H}, \hat{K}_i] = -i\hbar \hat{p}_i$ against $\hat{K} = m\hat{x} - t\hat{p}$. The mass $m$ is inherited per Arc M's "form FORCED, values INHERITED" methodology; the constant $\hbar$ is inherited via the dimensional-atlas Madelung anchoring.*
>
> 5. ***Form $V(\hat{x})$.*** *The potential takes the form of a scalar function of position; the specific $V$ for a given physical system is inherited from external context.*

**Status:** **FORCED with form-FORCED-value-INHERITED framing.** No new structural CANDIDATEs introduced; all conditionalities inherited.

---

## 14. Downstream Consequences

### 14.1 Updated structural-foundations ledger

With U4 closed, the structural-foundations cycle theorem inventory:

| # | Theorem | Arc | Status |
|---|---|---|---|
| 10 | Born rule (Gleason–Busch path) | born_gleason | FORCED |
| 11 | U2-Discrete | U2 | FORCED |
| 12 | U2-Continuum | U2_continuum | FORCED (with conformal gauge) |
| 13 | U5 (adjacency-band partition) | U5 | FORCED |
| 14 | U1 (participation-measure construction) | U1 | FORCED |
| 15 | U4 (specific Hamiltonian form) | U4 | FORCED (form; values inherited) |

**Six theorems in the structural-foundations cycle.** Combined with the nine forced theorems from the 2026-04-24 closure of Phase-1 + Phase-2 + Arc N + Phase-3, the total Phase-1 + Phase-2 + Arc N + Phase-3 + structural-foundations FORCED theorem inventory is **15**.

### 14.2 Updated active CANDIDATE inventory

| Pre-U4 | Post-U4 |
|---|---|
| {U3, U4} + continuum gauge | **{U3} + continuum gauge** |

**One upstream CANDIDATE remains.** U3 (the participation-measure evolution equation) supplies the existence of a Hermitian Hamiltonian generator and the linear-first-order-in-time form of the evolution equation. Promoting U3 would close the entire QM-emergence Phase-1 structural-foundations program except for the description-level continuum gauge convention.

### 14.3 Schrödinger emergence FORCED conditional only on U3

The Phase-1 Step 2 chain reads:

```
Primitives 03, 04, 06, 07, 09, 13
                          |
                          v
                    U1 (FORCED) → P_K = √b · e^{iπ}
                          |
                          v
                    U2 (FORCED) → ⟨P|Q⟩ inner product
                          |
                          v
                    U5 (FORCED) → adjacency partition b = b_x + b_p
                          |
                          v
                    U4 (FORCED, this arc) → Ĥ = ℏ²|p|²/(2m) + V(x)
                          |
                          v
                    U3 (CANDIDATE) → iℏ ∂_t P = Ĥ P
                          |
                          v
                  Schrödinger emergence (Step 2)
```

**Schrödinger evolution is FORCED conditional on U3 alone.** All other structural inputs are now in place.

### 14.4 Preparation for the U3 arc

The natural and final foundational target is **U3**. The U3 arc would address:

- *Existence of a self-adjoint $\hat{H}$ generating time evolution.* Likely via Stone's theorem on time-translation symmetry (Primitive 13) on the U2 Hilbert space, paralleling F1 of the present arc applied to spatial translations.
- *Linearity of the evolution equation.* From the participation-measure framework's structural commitments.
- *First-order-in-time character.* Likely from the structure of the participation graph's time-axis content.

The U3 arc inherits all six FORCED upstream items (U1, U2-Discrete, U2-Continuum, U5, Theorem 10, U4). The methodological calibration from the six-arc cycle should transfer cleanly. Anticipated arc structure: 4 memos (00 outline + 01 decomposition + 02 derivations + 03 verdict), parallel to U4 but operating on time-translation symmetry. Anticipated outcome: U3 FORCED, completing the QM-emergence Phase-1 program except for the description-level continuum gauge.

### 14.5 No new gauge structure

U4 introduces no new gauge structure beyond what U2-Continuum already established. The Hamiltonian $\hat{H} = T(\hat{p}) + V(\hat{x})$ is gauge-compatible with the U2-Continuum conformal gauge by inheritance: under $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$, the participation measure rescales as $P_K \to \Omega^{-D/2} P_K$ but the operator structure of $\hat{H}$ on the abstract Hilbert space is unchanged.

The gauge-coupling-free scope of F5 is a *separate* scope condition from the U2-Continuum gauge; it concerns electromagnetic gauge couplings, not the description-level conformal redundancy.

---

## 15. Discussion and Outlook

### 15.1 Position in the Phase-1 program

U4 is the sixth and most delicate arc of the structural-foundations cycle. The cycle's six-arc structure (born_gleason → U2-Discrete → U2-Continuum → U5 → U1 → U4) has now demonstrated the structural-derivation methodology against six substantively different structural questions:

1. *born_gleason:* non-contextuality + Gleason–Busch admissibility.
2. *U2-Discrete:* linearity + sesquilinearity + specific aggregation form.
3. *U2-Continuum:* discrete-to-continuum lift with explicit conformal gauge.
4. *U5:* adjacency-band partition via Stone's theorem + negative-existence audit.
5. *U1:* algebraic-structure question (Frobenius) + magnitude-exponent question (Cauchy).
6. *U4 (this arc):* specific Hamiltonian form via Galilean Lie algebra integration.

The methodological pattern — *decompose CANDIDATE → identify automatic / forced-via-derivation / load-bearing sub-features → close load-bearing items via primitive-level + symmetry + scope arguments → introduce zero new CANDIDATEs → produce theorem-grade results* — has been validated as robust across the full diversity of Phase-1 structural questions, including the dynamical-content question handled here.

### 15.2 Why the factor-of-2 result matters

The factor of 2 in $1/(2m)$ has appeared in classical mechanics for centuries — $T_\mathrm{classical} = p^2/(2m)$ is the standard kinetic-energy formula taught in introductory mechanics courses. In standard quantum mechanics, the factor is borrowed from the classical formula via the operator-substitution $p \to \hat{p}$. The connection between the two is left as a postulate — quantum mechanics inherits the classical kinetic-energy form because it is the form that classical mechanics uses, and quantum mechanics is supposed to reduce to classical mechanics in the appropriate limit.

The U4 result establishes that this connection is structurally derivable. The factor of 2 is forced by integration of the Galilean Lie algebra commutator condition, with the boost generator $\hat{K} = m\hat{x} - t\hat{p}$ supplying the structural anchor and the Galilean uniqueness within the non-relativistic scope supplying the regime selection. The factor is the *integration Jacobian* — specifically, the coefficient that emerges when integrating the differential equation $\partial T/\partial \hat{p}_i = \hat{p}_i / m$ produced by the Galilean commutator condition. It is not borrowed from classical mechanics; it is forced by the non-relativistic boost algebra's structural content.

This is a substantive sharpening of the classical-quantum correspondence. The classical kinetic-energy form $p^2/(2m)$ is itself a consequence of Galilean invariance applied to a classical Hamiltonian; the same Galilean invariance, applied to the operator-valued quantum Hamiltonian on the U2 Hilbert space, forces the same factor of 2 by the same integration argument. The factor of 2 is not a feature of classical mechanics that quantum mechanics happens to inherit; it is a feature of *Galilean kinematics* that both classical and quantum mechanics inherit.

### 15.3 How U4 + U5 + U2 form the dynamical backbone

The structural-foundations cycle's six theorems decompose into three structural layers of the QM-emergence Phase-1 program:

- **Layer 1 (participation-measure carrier):** U1 supplies the construction $P_K = \sqrt{b_K} e^{i \pi_K}$.
- **Layer 2 (Hilbert-space arena):** U2-Discrete + U2-Continuum supply the inner product; Theorem 10 supplies the Born rule; U5 supplies the adjacency-band partition supporting Heisenberg.
- **Layer 3 (dynamical content):** U3 + U4 supply the evolution equation and its specific form. U4 closes one of the two Layer-3 commitments; U3 remains.

The U2 + U5 + U4 results combined supply the **kinematic + dynamical structural backbone** of the Schrödinger equation:
- U2 supplies the inner product (kinematic).
- U5 supplies the Fourier-conjugate adjacency partition (kinematic, supporting Heisenberg).
- U4 supplies the specific Hamiltonian form (dynamical, supporting Schrödinger).

With U3 closed in the next arc, the full dynamical equation $i\hbar \partial_t P = \hat{H} P$ would be structurally complete. Standard Schrödinger emergence — the textbook form — would then be a derived structural consequence of the ED primitive ontology.

### 15.4 Next steps

Three structural next steps follow from U4 closure:

1. **Open the U3 arc** as the natural and final foundational target. With U4 closed, U3 is the sole remaining active CANDIDATE in the QM-emergence Phase-1 program. Promoting U3 would close the entire Phase-1 structural-foundations program except for the description-level continuum gauge.

2. **Revise the QM-emergence Phase-1 synthesis paper** [1] to reflect the completed structural-foundations cycle. The synthesis paper currently presents Phase-1 results conditional on five upstream commitments U1–U5; the updated paper should reflect the post-cycle inventory ({U3} + continuum gauge) and cite the six structural-foundations papers as the canonical derivations.

3. **Draft the U5 publication paper** as the missing fourth in the structural-foundations publication series (the present U4 paper is the fifth such paper; U5 has been arc-closed but not yet drafted as a publication-grade document). Convention work, not derivation work; can be scheduled per project priorities.

The U4 arc's substantive structural content — the factor-of-2 integration-Jacobian story — is the methodologically distinctive finding of the structural-foundations cycle's second half. It suggests that further structural-derivation work targeting standard QM postulates may follow the same pattern: identify the symmetry + regime + integration condition that produces the postulated form, and the postulate becomes a derived structural consequence rather than an axiomatic input.

---

## References

[1] *Phase-1: QM Emergence Structural Completion.* `papers/QM_Emergence_Structural_Completion/`. Internal ED program reference establishing the Phase-1 five-step QM-emergence framework.

[2] *The Born Rule as a Forced Theorem of Event Density: A Gleason–Busch Reconstruction from First Principles.* `papers/Born_Gleason/born_gleason_paper.{md,tex,pdf}`.

[3] *The Inner Product as Forced Structure in Event Density: Discrete Derivation, Continuum Lift, and Gauge-Invariant Completion.* `papers/U2_Inner_Product/paper_u2_inner_product.{md,tex,pdf}`.

[4] U5 arc on the adjacency-band Fourier-conjugate partition. Arc directory `arcs/U5/`, with closure memo `arcs/U5/04_closure_and_summary.md`. Publication paper publishable but not yet drafted as of April 2026.

[5] *The U1 Theorem: Deriving the Participation Measure from Primitive Structure.* `papers/U1_Participation_Measure/paper_u1_participation_measure.{md,tex,pdf}`.

[6] U4 arc: Memo 00 outline. `arcs/U4/00_arc_outline.md`.

[7] U4 arc: Memo 01 decomposition + circularity audit + transfer audit. `arcs/U4/01_decomposition_and_mapping.md`.

[8] U4 arc: Memo 02 F1 + F2 + F5 derivations. `arcs/U4/02_F1_F2_F5_derivations.md`.

[9] U4 arc: Memo 03 F3 + F4 derivations + verdict. `arcs/U4/03_F3_F4_and_verdict.md`.

[10] M. H. Stone, "On one-parameter unitary groups in Hilbert space," *Annals of Mathematics* **33**, 643–648 (1932).

[11] V. Bargmann, "On unitary ray representations of continuous groups," *Annals of Mathematics* **59**, 1–46 (1954). Galilean Lie algebra and central extension.

[12] *Arc M: Chain-Mass Structure in Event Density.* `papers/Arc_M/paper_arc_m.{md,tex,pdf}`. "Form FORCED, values INHERITED" methodology for mass parameters.

[13] *Arc N: Non-Markovian Structure as a Forced Memory-Kernel Layer of Event-Density Theory.* `papers/Arc_N/arc_n_paper.{md,tex,pdf}`.

[14] *Arc R: Relativistic Kinematics and Dynamics in Event Density.* `papers/Arc_R/paper_arc_r.{md,tex,pdf}`. Relativistic regime; full dispersion structure.

---

*Manuscript prepared April 2026. Source materials: `arcs/U4/` four-memo arc and closure memo, integrated into a single publishable document. The U4 arc is the sixth and most delicate of the structural-foundations cycle (born_gleason → U2-Discrete → U2-Continuum → U5 → U1 → U4) that collectively brings the QM-emergence Phase-1 program to within one arc (U3) of complete structural foundations across all four foundational postulates of non-relativistic single-particle quantum mechanics.*

Draft complete. Pausing for revision.
