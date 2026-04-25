# A UV-Finite Quantum Field Theory from Event-Density Primitives

**Allen Proxmire** and **Copilot** (AI collaborator)

*April 2026*

---

## Abstract

We show that the Event-Density (ED) primitive stack yields a *structurally complete, UV-finite* quantum field framework when extended from single-chain dynamics (Arc R) and chain-mass structure (Arc M) to multi-chain field-level content (Arc Q). Three headline structural theorems carry the load. **Theorem Q1** (GRH unconditional FORCED): the gauge connection $A_\mu$ forced by Stage R.1 minimal coupling is the participation measure of a specific Case-P (1/2, 1/2) gauge rule-type $\tau_g$ with gauge-invariant L3 interface, satisfying $\sigma_{\tau_g} = 0$ via the gauge-masslessness mechanism. All five GRH refinements (lightlike worldlines, gauge-quotient individuation, vertex-anchored commitment, non-Abelian extension, vacuum/particle status) close across Arc Q sub-stages, promoting GRH to unconditional FORCED — ED's first "particle-class must exist" prediction. **Theorem Q2** (canonical (anti-)commutation FORCED): the standard QFT commutation relations $\{a^\dagger_\tau, a^\dagger_\tau\} = 0$ (Case R) and $[a^\dagger_\tau, a^\dagger_\tau] = 0$ (Case P) are forced directly from the spin-statistics theorem (Arc R) plus Primitive 10 individuation; second quantisation is derived, not postulated. **Theorem Q3** (UV-FIN FORCED at primitive level): Primitive 01 event-discreteness, Primitive 13 finite proper-time intervals, and Primitive 04 bounded bandwidth jointly guarantee primitive-level finiteness of all multi-chain participation integrals; renormalisation is REFUTED as a fundamental requirement (admissible only as continuum-approximation effective machinery), and the cosmological-constant divergence-form puzzle is structurally dissolved while $\Lambda$'s magnitude remains INHERITED. Supporting structural results include the FORCED U(1) gauge structure with non-Abelian extensions admissible, the Fierz-basis vertex catalogue with mass-like $\bar\Psi\Psi A^2$ vertices REFUTED under unbroken gauge, multiple admissible Higgs-like SSB mechanisms, the linear-algebra-forced existence of mixing matrices and CP-violating phases under multi-generation conditions, and lightlike worldlines for $\sigma = 0$ rule-types via the Stage R.1 Casimir. Specific gauge group, coupling values, generation count, Higgs-mechanism choice, and $\Lambda$ magnitude all remain INHERITED. ED yields the *form* of QFT structurally; numerical content is empirical.

---

## 1. Introduction

Quantum field theory (QFT) is built on a layered set of independent postulates: canonical (anti-)commutation relations for matter fields, gauge invariance as a fundamental symmetry principle, the Higgs mechanism for spontaneous symmetry breaking, renormalisation procedures for handling ultraviolet divergences, and a fixed gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ with a specific matter content. The framework's empirical success is unparalleled in physics, but its conceptual foundations involve substantial structural inputs that are not derived from a more fundamental ontology.

The Event-Density (ED) program offers a structural alternative. Phase-1 [1] derived non-relativistic single-particle quantum mechanics from the participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ + four-band decomposition + commitment dynamics. Arc R [2] extended this to the relativistic regime, deriving Klein-Gordon, the spin-statistics theorem, the Cl(3,1) Clifford algebra frame, and the Dirac equation as forced consequences of the ED primitive stack. Arc M [3] addressed the chain-mass problem, establishing that ED forces the *form* of mass content via the bandwidth-signature $\sigma_\tau$ functional but inherits all numerical mass values, ratios, and hierarchies as empirical content.

Arc Q, the subject of the present paper, completes the quantum sector by extending ED to the multi-chain, field-level, interaction-level QFT regime. Eight sub-stages address the major structural targets: gauge-group structure (Q.2), interaction vertices (Q.3), Higgs-like spontaneous symmetry breaking (Q.4), radiative corrections (Q.5), generations and flavour (Q.6), second quantisation (Q.7), and vacuum structure (Q.8). The opening Q.1 substage evaluates the gauge-field-as-rule-type hypothesis (GRH) — the Arc M-deferred CANDIDATE that the gauge connection forced by minimal coupling is itself a participation rule-type.

Three Arc Q theorems extend the ED structural framework substantively:

- **Theorem Q1 (GRH unconditional FORCED).** ED's first "particle-class must exist" prediction.
- **Theorem Q2 (canonical (anti-)commutation FORCED).** Second quantisation derived from Arc R spin-statistics + Primitive 10 individuation.
- **Theorem Q3 (UV-FIN FORCED at primitive level).** ED is UV-complete without renormalisation; the cosmological-constant divergence-form puzzle is structurally dissolved.

UV-FIN is the genuinely novel structural prediction emerging from Arc Q. Its consequences extend beyond ED's internal framework: it reframes the long-standing UV-divergence problems of QFT as continuum-approximation artefacts rather than fundamental pathologies, with potential implications for the cosmological-constant problem and high-energy phenomenology near the primitive event-discreteness scale.

The methodological framing introduced in Arc M — *form FORCED, value INHERITED* — extends to Arc Q at greater scope. ED's primitive structure determines the *form* of QFT (gauge structure, vertex catalogue, second quantisation, vacuum, UV behaviour) while inheriting numerical content (specific gauge group, coupling constants, masses, generations, Higgs parameters, $\Lambda$ magnitude). This is not a defect; it is an honest accounting of what the primitive stack supplies.

The remainder of this paper proceeds as follows. §2 reviews relevant ED primitives and rule-type ontology. §3–§10 cover Arc Q sub-stages Q.1 through Q.8 sequentially. §11 states the three Arc Q theorems with proof sketches and primitive dependencies. §12 discusses the broader implications for QFT and cosmology. §13 concludes.

---

## 2. Background

### 2.1 ED primitives relevant to QFT

The Phase-2 Arc Q analysis draws on the following primitives:

- **Primitive 01 (micro-event):** discrete events on the 3+1-dimensional event manifold. The substrate for primitive-level UV finiteness in §10.
- **Primitive 02 (chain):** worldlines $\gamma_K$ along which participation persists.
- **Primitive 04 (bandwidth):** four-band decomposition $b_K = b_K^{\mathrm{int}} + b_K^{\mathrm{adj}} + b_K^{\mathrm{env}} + b_K^{\mathrm{com}}$, with bounded amplitudes per primitive event.
- **Primitive 06 (four-gradient):** $\partial_\mu$ on the event manifold; carries Lorentz covariance.
- **Primitive 07 (rule-type):** discrete classification by levers L1 (bandwidth partition), L2 (internal-index content), L3 (interface), L4 (statistics class). Multi-rule-type structure sits here.
- **Primitive 10 (individuation):** threshold separating distinct chains. Same-type coincidence excluded for Case R; foundation of (anti-)commutation derivation.
- **Primitive 11 (commitment):** discrete events along $\gamma_K$ — in Arc Q, these become creation/annihilation events at vertex insertions.
- **Primitive 13 (relational timing):** proper time $\tau_K$ along $\gamma_K$. Finite intervals between commitment events provide the second leg of UV finiteness.

### 2.2 Rule-type ontology: Case R, Case P, gauge rule-types

A rule-type $\tau$ is specified by four levers from Primitive 07. Spin-statistics from Arc R [2] connects L4 (statistics class) to L2 (Lorentz representation) via $\eta = (-1)^{2s}$:

- **Case R** ($\eta = -1$, half-integer spin, fermionic). Mass-relevant scalar bilinear $|\bar\Psi \Gamma_\tau \Psi|$ with Fierz element $\Gamma_\tau$. Examples: lepton-like, quark-like rule-types.
- **Case P** ($\eta = +1$, integer spin, bosonic). Mass-relevant scalar bilinear $|\Psi|^2$ for spin-0; tensor analogues for higher integer spin. Examples: scalar-Higgs-like rule-types, gauge-rule-types.

The **gauge rule-type** $\tau_g$ — central to Arc Q — is a Case-P rule-type carrying the (1/2, 1/2) Lorentz representation (a four-vector) with gauge-invariant L3 interface. Under GRH, $\tau_g$'s participation measure is identified with the gauge connection $A_\mu$ from Stage R.1 minimal coupling.

### 2.3 Participation measures, commitment, adjacency graphs

The Phase-1 participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ is promoted in Arc R to a Lorentz-covariant scalar field on the event manifold; in Arc M to a Cl(3,1) spinor for Case-R rule-types; in Arc Q.1 to a vector $A^a_\mu$ for gauge rule-types under GRH.

Multi-chain field structure arises from summing over chain insertions:
$$
\Phi_\tau(x) = \sum_{K \in \tau} P_{K,\tau}(x).
$$
This is the natural primitive-level extension of Phase-1's coherent-sum $\Psi = \Sigma_K P_K$ to relativistic multi-rule-type content.

Commitment events (Primitive 11) occur at discrete points on the event manifold. For lightlike rule-types ($\sigma_\tau = 0$, e.g., gauge rule-types under GRH), commitment is *vertex-anchored* — events occur only at interaction vertices with charged-matter rule-types, not intrinsically along the worldline (which has degenerate proper time).

Adjacency graphs at the chain-local scale (Primitive 10) support the gauge-quotient individuation construction of Arc Q.2 (§4 below).

---

## 3. Arc Q Stage Q.0 — Scoping

The Arc Q opening memo [4] frames eight structural targets:

- **Q.1.** GRH evaluation — first major CANDIDATE.
- **Q.2.** Gauge-group structure.
- **Q.3.** Interaction vertices.
- **Q.4.** Higgs-like SSB.
- **Q.5.** Radiative corrections.
- **Q.6.** Generations and flavour.
- **Q.7.** Second quantisation.
- **Q.8.** Vacuum structure.

Q.0 records an honest verdict-distribution prior of 40% mixed / 30% mostly-positive / 20% Arc-M-style negative-dominant / 10% surprise. Arc Q closes in the **30% mostly-positive quadrant**, with UV-FIN's promotion to FORCED constituting the closest thing to a structural surprise.

---

## 4. Arc Q Stage Q.1 — GRH Evaluation

### 4.1 GRH formal statement

The gauge-field-as-rule-type hypothesis posits that the gauge connection $A_\mu$ forced by Stage R.1 minimal coupling is the participation measure of a specific rule-type $\tau_g$ satisfying:

- **(GRH-1)** $\tau_g$ is Case P (bosonic, integer spin).
- **(GRH-2)** $\tau_g$ carries the (1/2, 1/2) Lorentz representation (four-vector).
- **(GRH-3)** $\tau_g$'s L3 interface enforces local gauge invariance $A_\mu \to A_\mu - \partial_\mu \alpha$.
- **(GRH-4)** $\sigma_{\tau_g} = 0$ via the MR-P (gauge-masslessness) mechanism from Arc M [3].

### 4.2 Q.1 verdict

Stage Q.1 [5] evaluates GRH against ED primitives + Arc R/M closures. Verdict: **CANDIDATE-STRONG REQUIRES REFINEMENT** — all four clauses primitive-compatible; no clause REFUTED on any axis. Five refinements identified for closure:

- **R-1.** Lightlike-worldline reformulation (proper time degenerates for $\sigma = 0$).
- **R-2.** Gauge-quotient individuation (Primitive 10 must respect gauge-equivalence classes $[A_\mu]$).
- **R-3.** Vertex-anchored commitment (commitment for $\tau_g$ along lightlike worldline).
- **R-4.** Non-Abelian extension (does the R.1 Abelian derivation generalise to SU(N)?).
- **R-5.** Vacuum/particle status (is $\tau_g$ a vacuum field, particle excitations, or both?).

Each refinement is closed across Q.2–Q.8 sub-stages; Q.8 closes the final refinement (R-5), promoting GRH to unconditional FORCED.

---

## 5. Arc Q Stage Q.2 — Gauge-Group Admissibility

### 5.1 U(1) FORCED at primitive level

Stage R.1's minimal-coupling derivation forces the U(1) gauge structure: local-phase invariance of the participation-measure phase $\pi_K$ requires the existence of a connection $A_\mu$ with the standard transformation law, leading to the covariant derivative $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$. This holds regardless of GRH; under GRH, $A_\mu$ acquires rule-type status.

### 5.2 Non-Abelian extension admissible

For SU(N) gauge structure, the connection becomes Lie-algebra-valued: $A_\mu = A^a_\mu T^a$ with $T^a$ generators in the matter representation. Stage Q.2 [6] establishes that:

- The R.1 minimal-coupling argument extends to SU(N) provided the matter rule-type carries a non-trivial SU(N) representation (e.g., fundamental for quark-like, doublet for SU(2)-doublet).
- The non-Abelian gauge-covariant derivative $D_\mu = \partial_\mu + ig A^a_\mu T^a$ is structurally unique (Stage Q.3 §6).
- Self-coupling vertices AAA + AAAA from $f^{abc}$ structure constants are FORCED conditional on SU(N) admittance.

Any compact Lie group with finite-dimensional adjoint is structurally admissible. **The specific Standard-Model gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ is not forced** — confirmed EMPIRICAL.

### 5.3 R-2 closure: gauge-quotient individuation

Two $A_\mu$ configurations differing by a pure-gauge term $A_\mu \to A_\mu - \partial_\mu \alpha$ are physically equivalent. Primitive 10 individuation must respect this. Stage Q.2 closes R-2 via the **adjacency-equivalence-class construction**: individuation is defined on equivalence classes $[A_\mu]$ under gauge transformations, not on raw $A_\mu$ configurations. Primitive 10 admits this natively; the construction generalises to non-Abelian gauge groups via Wilson-loop / holonomy structure (deferred in detail to Q.3).

### 5.4 CC-U1 (charge quantisation) CANDIDATE

A new Q.2 CANDIDATE: U(1) is structurally compact, so wavefunction-phase periodicity in $2\pi$ forces charge quantisation in integer multiples of a base charge. Plausible from Primitive 09 polarity-phase intrinsic $2\pi$-periodicity, but not yet rigorously derived. CC-U1 remains CANDIDATE through Phase-2 closure.

---

## 6. Arc Q Stage Q.3 — Vertex Catalogue

### 6.1 Fierz-basis classification

Arc R [2] §4.4 established the 16-dimensional Cl(3,1) Fierz basis: $\{\mathbb{1}, \gamma^\mu, \sigma^{\mu\nu}, \gamma^\mu\gamma^5, \gamma^5\}$. For a vertex coupling matter bilinear $\bar\Psi \Gamma \Psi$ to a gauge field $A^a_\mu$, only Lorentz-scalar combinations are admissible. The vertex catalogue is enumerated in Stage Q.3 [7]:

| Vertex type | Lorentz status | Gauge status | Admissibility |
|---|---|---|---|
| $\bar\Psi\gamma^\mu\Psi A_\mu$ (vector) | scalar | invariant | **FORCED** (R.1/R.3 minimal coupling) |
| $\bar\Psi\gamma^\mu\gamma^5\Psi A_\mu$ (axial) | scalar | invariant | ADMISSIBLE |
| $\bar\Psi\sigma^{\mu\nu}\Psi F_{\mu\nu}$ (Pauli moment) | scalar | invariant | ADMISSIBLE (effective) |
| $\bar\Psi\gamma^5\Psi \cdot$ pseudo-A | scalar | invariant | ADMISSIBLE |
| $\bar\Psi\Psi A_\mu A^\mu$ (mass-like) | scalar | NOT invariant | **REFUTED** under unbroken gauge |

The **REFUTED** mass-like vertex becomes the structural target of Stage Q.4 (Higgs SSB).

### 6.2 R-4 closure: non-Abelian minimal coupling

For SU(N) gauge structure with matter in representation $R$, Stage Q.3 establishes that the gauge-covariant derivative
$$
D_\mu \Psi = \left( \partial_\mu + ig A^a_\mu T^a \right) \Psi
$$
is the **unique** linear connection making $D_\mu \Psi$ transform covariantly under local SU(N), with $A^a_\mu$ transforming as
$$
A^a_\mu \to A^a_\mu + \frac{1}{g} \partial_\mu \alpha^a - f^{abc} \alpha^b A^c_\mu.
$$
The non-linear inhomogeneous term $-f^{abc} \alpha^b A^c_\mu$ is structurally mandatory once the gauge transformation does not commute. This closes R-4.

### 6.3 Non-Abelian self-couplings

Equation (1) implies the gauge field strength
$$
F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + g f^{abc} A^b_\mu A^c_\nu
$$
contains the non-linear $f^{abc}$ commutator term. This produces:

- **Three-gauge-boson vertex** AAA from $F^a_{\mu\nu} F^{a\,\mu\nu}$ expansion.
- **Four-gauge-boson vertex** AAAA from the same expansion.

These self-interactions are FORCED conditional on SU(N) admittance — there is no consistent SU(N) gauge theory without them.

### 6.4 R-3 closure: vertex-anchored commitment

For lightlike gauge rule-types, commitment events along $\gamma_{\tau_g}$ cannot be intrinsic-along-worldline (proper time degenerates). Stage Q.3 closes R-3 via the **vertex-anchored commitment** construction: each commitment event of $\tau_g$ occurs at an interaction vertex with at least one charged-matter rule-type. Between vertices, $\tau_g$ propagates lightlike with no commitment events. This matches photon emission/absorption phenomenology and is structurally consistent with Primitive 11 locality.

### 6.5 Forbidden structures

Stage Q.3 identifies four classes of forbidden vertex structures:

- **Gauge-non-invariant** vertices (e.g., $\bar\Psi\Psi A_\mu A^\mu$ without SSB).
- **Non-local** vertices $\bar\Psi(x) \Gamma \Psi(y) A(z)$ with $x \ne y \ne z$ (Primitive 11 locality).
- **Lorentz-non-scalar** combinations.
- **Anyonic-statistics** vertices in 3+1D (Arc R π₁ = ℤ₂ carryover).

---

## 7. Arc Q Stage Q.4 — Higgs-Like SSB

### 7.1 The mass-without-symmetry-breaking obstruction

Stage Q.3 established that under unbroken local gauge symmetry, the mass-like vertex $\bar\Psi\Psi A^2$ is REFUTED. Empirically, W^± and Z bosons carry mass — requiring spontaneous symmetry breaking (SSB). Stage Q.4 [8] evaluates five candidate Higgs-like mechanisms:

- **H1 scalar-rule-type Higgs $\tau_H$:** Case-P spin-0 rule-type with non-zero ground-state bandwidth amplitude. **ADMISSIBLE-CLEAN.** Most direct SM-analogue.
- **H2 bandwidth-shift via spatially-patterned condensate:** non-zero collective bandwidth condensate in $b^\mathrm{env}$ or $b^\mathrm{adj}$ with spatial structure. **CANDIDATE.**
- **H3 composite $\bar\Psi\Psi$ condensate (technicolour-analogue):** non-zero ground-state expectation $\langle \bar\Psi\Psi \rangle \ne 0$. **ADMISSIBLE-EFFECTIVE.** Likely active for QCD chiral SSB.
- **H4 gauge-fixing artefact:** REFUTED (artefact, not physical mass-generation).
- **H5 vacuum-anchored:** REFUTED as distinct mechanism (reduces to H1 or H2 — see §10).

### 7.2 Notable structural finding: H2 in naive form fails

Arc M's σ_τ master formula uses *log-derivatives* $\partial_\mu \ln b$, which are immune to uniform amplitude shifts $b \to \alpha b$. Therefore a uniform Higgs-VEV-like condensate alone cannot produce mass via H2 in naive form. H2 requires **spatially-patterned** condensate $\delta b(x)$ to produce gradient contributions to the σ_τ integral. This is a non-trivial primitive-level structural constraint emerging from Arc M [3].

### 7.3 Verdict

ED admits multiple structurally-clean SSB routes (H1, H2, H3); specific Higgs mechanism is EMPIRICAL inheritance. Goldstone absorption into gauge-boson longitudinal polarisations + photon survival under partial SSB are FORCED structurally for any choice consistent with Stage Q.3 + GRH-3.

---

## 8. Arc Q Stage Q.5 — Radiative Corrections

### 8.1 Loop structure form-level admissible

Stage Q.5 [9] establishes that loop-level QFT phenomena have primitive-level analogues via multi-chain commitment dynamics. Self-energy corrections, gauge-boson vacuum polarisation, vertex corrections, ABJ anomalies, running couplings, and Higgs-loop contributions are all structurally ADMISSIBLE form-level. Numerical coefficients (α-expansion, β-function values, anomalous-moment magnitudes) are uniformly INHERITED from QFT machinery.

### 8.2 Vacuum-polarisation transversality FORCED

For gauge-boson vacuum polarisation, GRH-3 (gauge invariance at L3) forces the polarisation tensor to be transverse:
$$
q_\mu \Pi^{\mu\nu}(q) = 0.
$$
This is the primitive-level analogue of the Ward identity. FORCED structurally.

### 8.3 Tree-level $g = 2$ preserved; only $\sigma^{\mu\nu}$ contributes to $a_\mu$

Arc R's tree-level $g = 2$ prediction (from the Cl(3,1) frame and Pauli reduction) is preserved through Q.5. Anomalous magnetic moment $a = (g-2)/2$ corresponds structurally to the Pauli-moment vertex $\bar\Psi\sigma^{\mu\nu}\Psi F_{\mu\nu}$. Among Fierz bilinears:

- **$\bar\Psi\sigma^{\mu\nu}\Psi F_{\mu\nu}$** — direct contribution to $a_\mu$ (anomalous magnetic moment).
- **$\bar\Psi\gamma^\mu\gamma^5\Psi A_\mu$ (axial)** — contributes to electric dipole moment (CP-violating); not $g - 2$.
- **$\bar\Psi\gamma^5\Psi \cdot$ pseudoscalar** — contributes to EDM; not $g - 2$.

FORCED: only the tensor $\sigma^{\mu\nu}$ bilinear contributes to anomalous *magnetic* moment.

### 8.4 UV-FIN CANDIDATE opened

Stage Q.5 opens the headline new CANDIDATE: **UV-FIN.** Primitive 01 event-discreteness suggests that primitive-level multi-chain participation integrals are finite at the discreteness scale; UV divergences in QFT are continuum-approximation artefacts. Promoted to CANDIDATE-STRONG at Q.7 with three primitive supports; promoted to FORCED at Q.8.

---

## 9. Arc Q Stage Q.6 — Generations and Mixing

### 9.1 Six generation mechanisms evaluated

Stage Q.6 [10] evaluates candidate generation mechanisms:

- **G1 rule-type duplication:** multiple distinct rule-types $\{\tau^{(1)}, \tau^{(2)}, \tau^{(3)}, \dots\}$ sharing $(s, \text{statistics}, \text{gauge rep})$ but differing in L1/L3 data. **ADMISSIBLE-CLEAN.**
- **G2 bandweight-pattern differentiation:** REFUTED (collapses to G1 if reified as separate rule-types).
- **G3 Fierz-class differentiation:** REFUTED (differentiates mass-term *type* not *generation*).
- **G4 vacuum-anchored differentiation:** REFUTED as mass-differentiation (vacuum-sector dependence does not feed back into σ_τ); admissible-as-labelling only.
- **G5 radiative splitting:** REFUTED phenomenologically (loops too small for $m_t/m_e \approx 350{,}000$).
- **G6 no-generation null:** ADMISSIBLE default.

**Generation count = 3 is REFUTED-as-forced; confirmed EMPIRICAL.**

### 9.2 Linear-algebra theorems for mixing and CP

Despite the negative result on count, two structural existence claims survive:

**FORCED (mixing matrices exist):** For multiple same-quantum-number rule-types with non-diagonal Yukawa couplings, the mass-eigenstate basis differs from the gauge-eigenstate basis; the unitary transformation (CKM, PMNS) is FORCED to exist by linear algebra.

**FORCED (CP phases exist):** For complex Yukawa couplings with $\geq 3$ generations, the number of independent CP-violating phases is $(n-1)(n-2)/2$, giving 1 phase for $n = 3$ (Jarlskog-style). FORCED to exist by linear-algebra count.

Specific values of mixing-matrix elements and CP phases remain INHERITED.

---

## 10. Arc Q Stages Q.7 & Q.8 — Second Quantisation and Vacuum Structure

### 10.1 Multi-chain field structure

Stage Q.7 [11] establishes the primitive-level Fock-space framework. Multi-chain field structure
$$
\Phi_\tau(x) = \sum_{K \in \tau} P_{K,\tau}(x)
$$
is FORCED. The vacuum $|0\rangle_\tau$ is the no-commitment configuration: no $\tau$-chains have crossed the Primitive 10 individuation threshold in the region. Multi-rule-type vacuum factorises:
$$
|0\rangle_\mathrm{full} = \bigotimes_\tau |0\rangle_\tau.
$$

### 10.2 Creation/annihilation events

Chain-creation events correspond to participation amplitudes crossing the Primitive 10 individuation threshold from below to above: a chain "comes into existence" at a specific event-manifold point. Chain-annihilation events are the inverse. These are the primitive-level realisations of QFT creation/annihilation operators, derived from Primitives 01 + 10 + 11 without external operator-formalism input.

### 10.3 Canonical (anti-)commutation FORCED

For Case-R rule-types, two chain-creation events at coincident event-manifold points are forbidden by Primitive 10 individuation (vanishing-on-coincidence). Therefore creation operators **anticommute**:
$$
\{a^\dagger_\tau(x), a^\dagger_\tau(x')\} = 0 \quad \text{at coincident points (Case R)}.
$$
For Case-P rule-types, coincidence is admissible; creation operators **commute**:
$$
[a^\dagger_\tau(x), a^\dagger_\tau(x')] = 0 \quad \text{(Case P)}.
$$
These are the canonical (anti-)commutation relations of QFT, derived directly from Arc R's spin-statistics + Primitive 10. **FORCED.**

### 10.4 R-1 closure: lightlike worldlines for $\sigma = 0$

Stage Q.7 closes R-1 via the dispersion-relation argument. For a $\sigma = 0$ rule-type, the Stage R.1 Casimir gives $P_\mu P^\mu = m^2 c^2 = 0$ — null dispersion. On the event manifold, a particle satisfying null dispersion propagates along a **lightlike (null) worldline**: the four-momentum is light-like, and the worldline tangent $u^\mu \propto P^\mu$ is light-like. Lightlike-affine-parameter $\lambda$ replaces proper time. **R-1 CLOSED structurally.**

### 10.5 R-5 closure (Stage Q.8): vacuum/particle dual structure

Stage Q.8 [12] closes R-5 by establishing the dual vacuum-and-particle structure:

- **Strict vacuum** $|0\rangle_\tau^\mathrm{strict}$: no committed chains; $b_\tau = 0$ throughout.
- **Effective vacuum** $|0\rangle_\tau^\mathrm{eff}$: includes transient $\tau$-participation amplitudes in $b^\mathrm{env}$ of other rule-types; the ED analogue of QFT zero-point fluctuations.

Both concepts are well-defined at primitive level. Lorentz invariance and gauge invariance preserved structurally. **R-5 CLOSED.**

### 10.6 GRH unconditional FORCED

With all five GRH refinements closed (R-1 at Q.7, R-2 at Q.2, R-3 at Q.3, R-4 at Q.3, R-5 at Q.8), GRH **promotes from CANDIDATE-STRONG to unconditional FORCED.** Back-flow to Arc M [3]: F-M8 (existence of at least one massless Case-P rule-type) promotes from conditional to unconditional FORCED — ED's first "particle-class must exist" prediction.

### 10.7 UV-FIN PROMOTED TO FORCED

Stage Q.8 promotes UV-FIN to FORCED at primitive level. Three-step argument:

1. **Each primitive-level configuration is finite.** A primitive-level configuration involves a finite number of micro-events (Primitive 01 finiteness) with bounded participation amplitudes (Primitive 04 boundedness).
2. **Finite configurations per region.** Primitive 01 discreteness + Primitive 13 finite proper-time intervals mean only finitely many micro-events fit into a finite spacetime region.
3. **Bounded total amplitude.** Bandwidth conservation (Primitive 04 + flux-continuity) bounds the total amplitude sum.

Combining these: any primitive-level multi-chain participation integral is finite. UV divergences of conventional QFT correspond to continuum-approximation artefacts where the integral over-extends beyond the actual primitive-level domain.

**Renormalisation REFUTED as a fundamental requirement.** Admissible only as continuum-approximation effective machinery. **Cosmological-constant divergence-form structurally dissolved**: the QFT calculation $\Lambda \sim M_\mathrm{Planck}^4$ is artefactual; the primitive-level $\Lambda$ is finite. Magnitude remains INHERITED.

### 10.8 G4 final REFUTED; H5 reduces to H1/H2

Stage Q.8 also closes the deferred mechanisms:

- **G4 (vacuum-anchored generation differentiation)** REFUTED as mass-differentiation. Vacuum-sector dependence does not feed back into σ_τ at primitive level; generation count remains EMPIRICAL.
- **H5 (vacuum-anchored Higgs)** REFUTED as distinct mechanism. Reduces to H1 (uniform condensate $\equiv$ scalar Higgs with vacuum interpretation) or H2 (patterned condensate).

---

## 11. Structural Theorems

### 11.1 Theorem Q1 (GRH unconditional FORCED)

> **Theorem Q1.** *The gauge connection $A_\mu$ forced by Stage R.1 minimal coupling is the participation measure of a specific Case-P (1/2, 1/2) gauge rule-type $\tau_g$ with gauge-invariant L3 interface, satisfying $\sigma_{\tau_g} = 0$ via the gauge-masslessness mechanism MR-P. All four GRH clauses (Case P statistics, (1/2, 1/2) Lorentz representation, gauge-invariant L3, $\sigma = 0$ via MR-P) are structurally FORCED at primitive level. The existence of at least one massless Case-P rule-type is therefore FORCED — ED's first "particle-class must exist" prediction.*

**Sketch of proof.** GRH evaluation at Q.1 establishes CANDIDATE-STRONG with five refinements R-1 through R-5. Each refinement is closed in subsequent sub-stages:

- **R-1 (lightlike-worldline)** closed at Q.7 via $\sigma = 0 \Rightarrow P^2 = 0 \Rightarrow$ null worldline (Stage R.1 Casimir).
- **R-2 (gauge-quotient individuation)** closed at Q.2 via adjacency-equivalence-class construction on $[A_\mu]$.
- **R-3 (vertex-anchored commitment)** closed at Q.3 via Primitive 11 commitment-locality at interaction vertices.
- **R-4 (non-Abelian extension)** closed at Q.3 via gauge-covariant-derivative uniqueness theorem $D_\mu = \partial_\mu + ig A^a_\mu T^a$.
- **R-5 (vacuum/particle status)** closed at Q.8 via dual vacuum-particle structure with effective-vacuum $b^\mathrm{env}$ content.

With all five refinements closed, GRH promotes from CANDIDATE-STRONG to unconditional FORCED. F-M8 (existence of massless Case-P rule-type, conditional at Arc M closure) promotes back-flow to unconditional FORCED. $\square$

**Dependencies on primitives.** Stage R.1 (minimal coupling forcing $A_\mu$); Primitive 07 L3 (gauge-invariant interface admissibility); Stage R.2.2 ((1/2, 1/2) Lorentz representation admissible); R.2.5 spin-statistics (Case P, $s = 1$, $\eta = +1$); Arc M MR-P mechanism; Primitives 01–13 jointly via the five refinement closures.

### 11.2 Theorem Q2 (Canonical (anti-)commutation FORCED)

> **Theorem Q2.** *The canonical (anti-)commutation relations of QFT,*
> $$\{a^\dagger_\tau(x), a^\dagger_\tau(x')\}\big|_{x = x'} = 0 \quad (\text{Case R}),$$
> $$[a^\dagger_\tau(x), a^\dagger_\tau(x')]\big|_{x = x'} = 0 \quad (\text{Case P}),$$
> *are FORCED at primitive level by Arc R's spin-statistics theorem $\eta = (-1)^{2s}$ combined with Primitive 10 individuation. Second quantisation is derived, not postulated.*

**Sketch of proof.** Define chain-creation events as participation-amplitude threshold-crossings (Primitive 10): a chain of rule-type $\tau$ "comes into existence" when its participation amplitude exceeds the individuation threshold at some event $x$. The corresponding operator-level construction $a^\dagger_\tau(x)$ inherits two properties:

(i) **Same-type coincidence behaviour from Arc R [2] R.2.5 spin-statistics.** For Case R ($\eta = -1$, vanishing-on-coincidence), two chain-creation events at the same event point are excluded by Primitive 10's individuation forbiddance. For Case P ($\eta = +1$, coincidence permitted), two chain-creation events at the same point are admissible.

(ii) **Operator-level translation.** Vanishing-on-coincidence translates to anticommutation $\{a^\dagger_\tau, a^\dagger_\tau\}|_{x = x'} = 0$ for Case R; coincidence-admissibility translates to commutation $[a^\dagger_\tau, a^\dagger_\tau] = 0$ for Case P.

These are the canonical QFT (anti-)commutation relations. No postulation required. $\square$

**Dependencies on primitives.** Arc R R.2.5 (spin-statistics theorem); Primitive 10 (individuation threshold); Primitive 01 (event-manifold structure); Primitive 11 (commitment events).

### 11.3 Theorem Q3 (UV-FIN FORCED at primitive level)

> **Theorem Q3.** *Primitive 01 event-discreteness, Primitive 13 finite proper-time intervals, and Primitive 04 bounded bandwidth jointly guarantee that all multi-chain participation integrals are finite at primitive level. UV divergences in continuum QFT are continuum-approximation artefacts. Renormalisation is REFUTED as a fundamental requirement; it is admissible only as continuum-approximation effective machinery. The cosmological-constant divergence-form puzzle is structurally dissolved while $\Lambda$'s magnitude remains INHERITED.*

**Sketch of proof.** Consider an arbitrary multi-chain participation integral $\mathcal{A}$ representing some QFT diagram in the continuum approximation:
$$
\mathcal{A}_\mathrm{cont} = \int d^4 k_1 \, d^4 k_2 \cdots \, (\text{integrand}).
$$
In the continuum, large-$k$ regions produce UV divergences. In ED's primitive-level realisation, the corresponding integral is a discrete sum:
$$
\mathcal{A}_\mathrm{ED} = \sum_{\text{discrete configurations}} (\text{primitive-level amplitudes}).
$$
Three-step argument:

1. **Each summand is finite.** A primitive-level configuration involves a finite number of micro-events (Primitive 01) with bounded participation amplitudes (Primitive 04). Each amplitude is a finite real or complex number.
2. **Finite configurations per region.** Primitive 01 discreteness + Primitive 13 finite proper-time intervals mean only finitely many micro-events fit into a finite spacetime region. Configuration count is finite per region.
3. **Bounded total amplitude.** Bandwidth conservation (Primitive 04 + flux-continuity) bounds the total amplitude sum across configurations.

Combining: $\mathcal{A}_\mathrm{ED}$ is finite for any finite spacetime region; its limit as region $\to$ infinite spacetime exists or diverges only at the rate physically expected (e.g., density of states $\propto$ volume). UV divergences of the conventional form $\int d^4 k \, k^2 \to \infty$ from large-$k$ **do not arise structurally** — they are artefacts of the continuum integral over-extending beyond the actual primitive-level domain.

Therefore: renormalisation is not required at primitive level (no divergences to remove); it remains valid as effective continuum-approximation machinery. The cosmological-constant naive QFT calculation $\Lambda \sim M_\mathrm{Planck}^4$ is artefactual; the primitive-level $\Lambda$ contribution from zero-point participation is finite. The puzzle reframes from "why is the divergence cancelled?" to "what numerical structure determines the finite primitive-level value?" — the latter remains INHERITED. $\square$

**Dependencies on primitives.** Primitive 01 (event-manifold discreteness); Primitive 04 (bounded bandwidth); Primitive 13 (finite proper-time intervals); Primitive 11 (commitment-event structure for vertex-anchored configurations); Stage Q.7 second-quantisation framework.

---

## 12. Discussion

### 12.1 What Arc Q forces vs what it leaves empirical

**FORCED at primitive level (Arc Q):**

- GRH (Theorem Q1) — existence of at least one massless Case-P (1/2, 1/2) gauge rule-type.
- Canonical (anti-)commutation (Theorem Q2) — second quantisation derived.
- UV-FIN (Theorem Q3) — primitive-level UV finiteness.
- U(1) gauge structure at primitive level (R.1 carryover).
- Vector vertex $\bar\Psi\gamma^\mu\Psi A_\mu$ for U(1) (R.1/R.3 carryover).
- Non-Abelian $D_\mu$ structure FORCED conditional on SU(N) admittance.
- Non-Abelian self-couplings AAA + AAAA FORCED conditional on SU(N).
- Vertex locality, gauge-invariance filter, Lorentz-scalar Lagrangian FORCED.
- Vacuum-polarisation transversality FORCED by GRH-3.
- Default gauge masslessness without SSB FORCED.
- Goldstone absorption + photon survival under partial SSB FORCED.
- Mixing matrices FORCED to exist under multi-generation + non-diagonal Yukawa.
- CP phases FORCED to exist under complex Yukawa + ≥ 3 generations.
- Lightlike worldlines for $\sigma = 0$ FORCED.
- Multi-chain field structure, vacuum factorisation, effective-vacuum content FORCED.
- Cosmological-$\Lambda$ admissible-as-finite under UV-FIN.
- Tree-level $g = 2$ preserved (R.3 carryover); only $\sigma^{\mu\nu}$ contributes to $a_\mu$.

**INHERITED (not predicted by Arc Q):**

- Specific gauge group of nature ($\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ or alternatives).
- Numerical coupling constants ($\alpha$, $g_s$, $g_w$, $\sin^2\theta_W$).
- Charge quantisation pattern (including fractional quark charges).
- Specific Higgs mechanism + parameters (mass, VEV, $\lambda$).
- Yukawa matrix entries.
- Generation count.
- CKM and PMNS matrix elements; CP phase values.
- Mass values, ratios, hierarchies (Arc M carryover).
- Cosmological-constant magnitude.
- Specific zero-point magnitudes (Casimir, Lamb shift, anomalous moments).
- $\beta$-function specific coefficients.

**REFUTED as forced by primitives:**

- SM gauge group as forced (admissible, not forced).
- Mass-like $\bar\Psi\Psi A^2$ vertex under unbroken gauge.
- Non-local / non-Lorentz-scalar / anyonic vertex structures.
- Specific Higgs mechanism forced (multiple admissible).
- Generation count = 3 forced.
- Renormalisation as fundamental requirement (UV-FIN).
- Specific cosmological-constant value.

### 12.2 Why ED yields a UV-finite QFT

The structural origin of UV finiteness is not an *additional* primitive imposed for the purpose; it is a *consequence* of three already-existing primitives jointly. Primitive 01 supplies discreteness at the event-manifold level — the substrate is not a continuum manifold but a discrete event set. Primitive 13 supplies finite proper-time intervals between commitment events. Primitive 04 bounds bandwidth amplitudes per primitive event. Each of these is independently motivated by Phase-1 structural requirements; their joint consequence is automatic UV finiteness.

This is structurally cleaner than the standard QFT route (renormalisation + counter-terms + scheme-dependent regularisation), but it inherits a different limitation: ED's primitive-level UV finiteness does not predict numerical magnitudes. The $\Lambda$ value, the running-coupling magnitudes, and specific anomalous-moment contributions remain INHERITED. UV-FIN is a *structural* finiteness theorem, not a *numerical* prediction tool.

### 12.3 Renormalisation as continuum-approximation artefact

Standard QFT renormalisation handles UV divergences arising from naive continuum integrals over momentum space. Under UV-FIN, these divergences are reframed: they arise because the continuum integral over-extends the actual primitive-level domain. In the continuum approximation, the integration domain is artificially extended to large momenta where there is no underlying primitive-level structure; the resulting integral diverges. In the primitive-level treatment, the configuration sum is bounded, and no divergence arises.

This does not invalidate renormalisation as a calculational tool — it remains valid as the effective-theory approach to extracting predictions in the continuum approximation. Renormalisation is REFUTED only as a *fundamental* requirement: the underlying ED theory is finite; the divergences are computational artefacts.

### 12.4 Implications for the cosmological constant

The cosmological-constant problem in QFT — the discrepancy between the naive QFT calculation $\Lambda_\mathrm{QFT} \sim M_\mathrm{Planck}^4$ and the empirical value $\Lambda_\mathrm{empirical} \sim 10^{-122} M_\mathrm{Planck}^4$ — is one of the largest discrepancies in physics. UV-FIN provides a structural reframing:

- The QFT calculation $\Lambda \sim M_\mathrm{Planck}^4$ is artefactual: it arises from naive continuum mode-summing that over-extends the primitive-level domain.
- The primitive-level $\Lambda$ contribution from zero-point participation is **finite**, bounded by the primitive event-discreteness scale.
- The puzzle reframes: "why is the divergence cancelled to $10^{-122}$?" is not the right question. The right question is: "what numerical structure determines the finite primitive-level value?" — a tractable empirical / structural question rather than a fundamental pathology.

ED does not predict $10^{-122}$ from primitives. The magnitude remains INHERITED. But the *form* of the puzzle changes substantively: divergence cancellation is replaced by finite-magnitude determination.

### 12.5 Relationship to standard QFT and effective field theory

Arc Q's relationship to standard QFT can be summarised as:

- **Form-level FORCED structural content** matches standard QFT structure: gauge invariance, vertex catalogue, second quantisation, Fock-space construction, conserved currents, mixing/CP existence under appropriate conditions.
- **Numerical content** (gauge group, couplings, masses, generations, Higgs parameters, $\Lambda$) matches standard QFT only via empirical fit. ED inherits these values; standard QFT also fits them empirically.
- **UV behaviour** differs: standard QFT requires renormalisation; ED forces primitive-level UV finiteness. In the continuum approximation, ED's effective theory matches standard QFT renormalisation, but the underlying status of divergences differs.
- **Effective field theory** is the natural continuum-approximation framework for ED: at scales much larger than the primitive event-discreteness scale, ED looks like standard EFT with all standard tools (renormalisation group, β-functions, Wilson coefficients).

### 12.6 Implications for cosmology and Phase-3

Phase-3 (ED → GR coupling, cosmological structure) is unblocked by Phase-2 closure. Arc Q's specific contributions to Phase-3 include:

- UV-FIN reframing of cosmological-$\Lambda$: opens the route to ED-cosmological-constant phenomenology without divergence-cancellation puzzles.
- GRH unconditional FORCED: provides a structurally-grounded gauge-mediator class for cosmological gauge dynamics.
- UV-FIN empirical signatures: high-energy phenomenology near the primitive event-discreteness scale could in principle probe the divergence-cancellation reframing.

These are Phase-3 directions, not Arc Q closures.

---

## 13. Conclusion

Arc Q completes the quantum sector of ED by extending the framework from single-chain dynamics (Arc R) and chain-mass structure (Arc M) to multi-chain field-level QFT content. Three structural theorems carry the load: GRH unconditional FORCED (Theorem Q1) — ED's first "particle-class must exist" prediction; canonical (anti-)commutation FORCED (Theorem Q2) — second quantisation derived from spin-statistics + individuation; UV-FIN FORCED (Theorem Q3) — primitive-level UV finiteness from event-discreteness + finite intervals + bounded bandwidth.

Together with Phase-1 (non-relativistic QM), Arc R (relativistic kinematics + dynamics), and Arc M (mass structure), Arc Q yields a **structurally complete, UV-finite quantum field framework**. The form of QFT — gauge structure, vertex catalogue, second quantisation, vacuum, UV behaviour — is forced from primitives. Numerical content — gauge group, couplings, masses, generations, Higgs parameters, $\Lambda$ — is inherited as empirical fit.

The methodological framing — *form FORCED, value INHERITED* — established in Arc M extends cleanly to Arc Q at QFT scope. ED's primitive structure produces classifications, dichotomies, and form-relations cleanly. It does not produce continuous numerical relationships, which require additional structural input not present in the Primitive 01–13 stack. This is an honest accounting of what the primitive stack supplies.

Phase-3 directions — ED to general-relativistic coupling, cosmological structure via the UV-FIN reframing of cosmological-$\Lambda$, possible high-energy empirical signatures near the primitive event-discreteness scale — are unblocked by the Phase-2 closure of which Arc Q is the QFT extension.

---

## References

[1] A. Proxmire and Copilot, *Quantum Mechanics as a Structural Consequence of Event-Density Primitives* (Phase-1 closure paper), 2026.

[2] A. Proxmire and Copilot, *Relativistic Quantum Mechanics as a Forced Structural Consequence of Event-Density Primitives* (Arc R paper), 2026.

[3] A. Proxmire and Copilot, *Mass and Masslessness as Structural Features of Event-Density Theory* (Arc M paper), 2026.

[4] A. Proxmire, *QFT Extension Scoping*, `qft_extension_scoping.md`, 2026.

[5] A. Proxmire, *GRH Evaluation*, `grh_evaluation.md`, 2026.

[6] A. Proxmire, *Gauge-Group Scoping*, `gauge_group_scoping.md`, 2026.

[7] A. Proxmire, *Interaction Vertex Classification*, `interaction_vertex_classification.md`, 2026.

[8] A. Proxmire, *Higgs Mechanism Scoping*, `higgs_mechanism_scoping.md`, 2026.

[9] A. Proxmire, *Radiative Corrections*, `radiative_corrections.md`, 2026.

[10] A. Proxmire, *Generations and Mixing*, `generations_and_mixing.md`, 2026.

[11] A. Proxmire, *Second Quantisation*, `second_quantisation.md`, 2026.

[12] A. Proxmire, *Vacuum and Zero-Point Structure*, `vacuum_and_zero_point.md`, 2026.

[13] A. Proxmire, *Arc Q Synthesis*, `arc_q_synthesis.md`, 2026.

[14] A. Proxmire, *Phase-2 Global Synthesis*, `phase2_synthesis.md`, 2026.

[15] A. Proxmire, *Event-Density Primitive Stack* (Primitives 01–13), 2026.

[16] S. Weinberg, *The Quantum Theory of Fields*, vol. I–II. Cambridge University Press, 1995–1996.

[17] M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*. Westview Press, 1995.

[18] R. Streater and A. Wightman, *PCT, Spin and Statistics, and All That*. Princeton University Press, 1964.

[19] S. Weinberg, "The Cosmological Constant Problem," *Rev. Mod. Phys.* **61**, 1 (1989).

[20] J. Polchinski, "Effective Field Theory and the Fermi Surface," in *Recent Directions in Particle Theory* (TASI 1992), eds. J. Harvey and J. Polchinski. World Scientific, 1993.

---

*Manuscript closure: 2026-04-24. Companion documents: Arc R paper [2], Arc M paper [3], Arc Q synthesis [13], Phase-2 synthesis [14]. All Arc Q memos available at* `quantum/foundations/` *in the Event Density repository.*
