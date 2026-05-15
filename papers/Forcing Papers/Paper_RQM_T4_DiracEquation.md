# Paper RQM-T4 — Dirac Equation $(i\gamma^\mu \partial_\mu - mc/\hbar)\Psi = 0$

**Series:** Wave-3 Relativistic-QM Bridge — Theorem T4
**Status:** Wave-3 generative paper; **M2 (Intermediate Path C)** verdict — structural mechanism identified; explicit substrate-V1 → Dirac closed-proof reduction OPEN
**Companions:** Paper_RQM_T1 (Spin–statistics), Paper_RQM_T2 (Cl(3,1)), Paper_RQM_T5 (Klein–Gordon), Paper_RQM_T7 (Lorentz reps), Arc-R Stage R.3.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived.** They are postulated per Paper_087.
2. **No claim that the Dirac equation is forced from nothing.** The result is conditional on T1 + T2 + T5 + Paper_017 + Paper_089 V1 kernel inheritance + standard QFT first-order-equation machinery.
3. **No claim of numerical-content derivation beyond what is explicitly INHERITED.** Specific particle masses (electron, muon, etc.) are INHERITED via empirical matching.
4. **No claim that the §3.7 substrate-V1 → Dirac derivation is closed.** The substrate-graph-to-Dirac derivation is asserted via standard substrate-Lorentz-covariantization (Paper_017 inheritance); the explicit substrate-V1 → Dirac chain is OPEN in this paper.
5. **No claim that ED is the only consistent substrate ontology.** Other substrate ontologies are conceivable.
6. **No claim of empirical adequacy outside the regime stated in §2.2.** Curved-acoustic-metric Dirac (Arc GR-Dirac), Majorana / Weyl extensions are deferred.

---

## Abstract

Paper RQM-T4 establishes the Dirac equation $(i\gamma^\mu \partial_\mu - mc/\hbar)\Psi = 0$ as the first-order Lorentz-covariant equation governing spinor rule-types in $D = 3+1$, with structural form FORM-FORCED by composition of T1 (spin–statistics) + T2 (Cl(3,1) frame uniqueness) + T5 (Klein–Gordon) + Paper_017 Lorentz covariantization + Paper_089 V1 kernel content. The substrate-level mechanism: spinor rule-types' four-component Cl(3,1) structure (T2) requires a first-order equation factorizing the KG operator (T5) for probability-current conservation and Stone-theorem compatibility; the Dirac operator $D = i\gamma^\mu \partial_\mu - mc/\hbar$ is the unique such factorization. Mass parameter $m$ is VALUE-INHERITED via empirical matching. Verdict tier: **M2 (Intermediate Path C)** per Paper_095 — structural mechanism identified, but the explicit substrate-V1 → Dirac closed-proof reduction is OPEN (§3.7's V1-kernel-to-Dirac chain is asserted via inheritance, not closed). The result joins the Wave-3 Relativistic-QM Bridge family as the first-order spinor equation companion to T5 (scalar KG), extending via T6 (minimal coupling) and classified via T7 (Lorentz representations). This paper is in the substrate-ontology research-program lineage of 't Hooft, Wolfram, and the causal-set program — not in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §1 Statement of Result

**Claim.** Spinor rule-types in $D = 3+1$ — those carrying half-integer intrinsic-rotation quantum number $s = 1/2$ — propagate according to the Dirac equation
$$(i\gamma^\mu \partial_\mu - mc/\hbar)\Psi = 0 ,$$
with gamma-matrices supplied by the unique Cl(3,1) representation (Paper_RQM_T2) and mass parameter $m$ INHERITED via empirical matching. The structural form of the equation — first-order, Lorentz-covariant, factorizing the Klein–Gordon operator — is FORM-FORCED by the substrate's spinor rule-type structure under Arc-R Stage R.3.

Verdict: **M2 (Intermediate Path C)** — structural mechanism identified; explicit substrate-V1 → Dirac closed-proof reduction OPEN (§3.7). No new postulates.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P05 (Polarity-transport along edges)** — substrate-level transport carrying spinor polarity.
- **P06 (Spatial dimension $D = 3+1$)** — supplies four-gradient $\partial_\mu$.
- **P09 ($U(1)$-valued polarity)** — supplies the phase target on which Dirac evolution acts.
- **P10 (Rule-type primitive)** — spinor rule-type as carrier.
- **P13 (Time homogeneity)** — supplies temporal-translation symmetry on which mass parameter is defined.

### 2.2 Upstream Dependencies

- **I-087:** 13-primitive position paper.
- **I-RQM-T1:** Spin–statistics dichotomy.
- **I-RQM-T2:** Cl(3,1) frame uniqueness.
- **I-RQM-T5:** Klein–Gordon equation (Paper_RQM_T5).
- **I-RQM-T7:** Lorentz representations.
- **I-089:** V1 finite-width retarded kernel.
- **I-Stone:** Standard Stone's theorem on unitary one-parameter groups.
- **I-Dirac:** Standard Dirac-equation machinery (standard physics).

---

## §3 Derivation

### 3.1 Spinor rule-type structure

By T2 (Paper_RQM_T2), spinor rule-types in $D = 3+1$ carry four-component participation amplitudes $\Psi(x)$ on which the Cl(3,1) gamma-matrices act. By T1 (Paper_RQM_T1), these carriers are fermionic with $s = 1/2$.

The substrate-level question: what first-order equation governs $\Psi(x)$'s propagation under V1 kernel content + Lorentz-covariance?

### 3.2 First-order vs second-order: why Dirac, not Klein–Gordon alone

The Klein–Gordon equation $(\square + m^2 c^2/\hbar^2)\Psi = 0$ (T5; Paper_RQM_T5) governs **scalar** (spin-0) rule-types. It is second-order in time. For substrate-level spinor rule-types, a first-order equation is preferred because:

1. **Probability current conservation:** First-order equations admit conserved probability currents (Noether). KG's second-order structure produces a current that is not positive-definite — problematic for substrate-level participation interpretation.

2. **Spinor structure mapping:** The substrate's spinor structure (Cl(3,1) four-component) is naturally accommodated by a first-order matrix equation. Higher-order equations would require additional structural justification.

3. **Stone's theorem at substrate level (I-Stone):** Substrate evolution under V1 kernel + spinor rule-type generates a one-parameter unitary group; its infinitesimal generator is first-order.

### 3.3 Constructing the Dirac operator

To construct a first-order equation that **factorizes** the Klein–Gordon operator (so that solutions satisfy KG as a secondary condition), we require an operator $D$ such that
$$D^\dagger D = -\square + m^2 c^2 / \hbar^2 \;\; \text{(or} \; D^2 = -\square + m^2 c^2/\hbar^2 \text{)}.$$

The factorization
$$D = i\gamma^\mu \partial_\mu - mc/\hbar$$
satisfies
$$D \cdot \bar{D} = (i\gamma^\mu \partial_\mu - mc/\hbar)(i\gamma^\nu \partial_\nu + mc/\hbar) ,$$
which simplifies under the Cl(3,1) anticommutator $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}\mathbb{1}$ to
$$-\square - m^2 c^2/\hbar^2 = -(KG operator).$$

(Sign convention varies with metric signature; the factorization holds.)

Therefore: spinor amplitudes satisfying $D\Psi = 0$ — i.e., the **Dirac equation** $(i\gamma^\mu\partial_\mu - mc/\hbar)\Psi = 0$ — automatically satisfy Klein–Gordon. The Dirac operator is the **square root** of the KG operator on Cl(3,1)-valued spinor structures.

### 3.4 Lorentz covariance

By T7 (Paper_RQM_T7), the spinor representation transforms under the Lorentz group $\mathrm{SL}(2,\mathbb{C})$ (double cover of $\mathrm{SO}(3,1)$) via a specific spinor representation $S(\Lambda)$. Under a Lorentz transformation $x \to \Lambda x$:
$$\Psi(x) \to S(\Lambda)\Psi(\Lambda^{-1}x) , \qquad \gamma^\mu \to \Lambda^\mu_\nu \gamma^\nu .$$

The Dirac equation form is preserved by these transformations (standard result; I-Dirac). The Lorentz covariance is FORM-FORCED by the substrate's Lorentz-covariantization (Paper_017) + the Cl(3,1) gamma-matrix transformation property.

### 3.5 Mass parameter inheritance

The constant $m$ in the Dirac equation is the rule-type's **mass parameter**. It is INHERITED via empirical matching:

- Electron: $m = 9.11 \times 10^{-31}$ kg.
- Muon: $m = 1.88 \times 10^{-28}$ kg.
- Quark masses: per-flavor inherited.

The substrate framework does not derive specific mass values from first principles. The substrate-level claim is the **form** of the Dirac equation; specific masses are matched empirically.

(See also Paper_RQM_Mass-Structure: Arc M H1-dominant — mass structural form is Lorentz-scalar, dimensional-anchored, statistics-class-mechanism, but specific values inherited.)

### 3.6 Arc-R Stage R.3 connection

Arc-R Stage R.3 (relativistic spinor first-order equations) covers the substrate-level construction of first-order spinor equations from rule-type structure + Cl(3,1) algebra. This paper supplies the Dirac equation as the canonical Stage R.3 result.

The full Arc-R sequence:
- **R.1:** Klein–Gordon for scalar rule-types (Paper_RQM_T5).
- **R.2:** Spinor rule-type taxonomy (relativistic spin–statistics, T1+T2+T3).
- **R.3:** Dirac equation for spinor rule-types (this paper).
- **R.4:** Vector / tensor rule-type equations (Maxwell, etc.; future paper).

### 3.7 Substrate-V1 connection

Under V1 substrate kernel propagation (Paper_089), the spinor rule-type amplitude propagates with retarded structure. The Dirac equation is the **continuum limit** of V1-modulated substrate spinor transport under DCGT coarse-graining.

Specifically: the V1 kernel acts on each spinor component $\Psi^\alpha(x)$ via the same finite-width retarded structure as for scalar amplitudes; the gamma-matrices supply the **inter-component coupling** that makes the equation first-order rather than second-order.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P06 $D = 3+1$ | P | Primitive. |
| 2 | P05 polarity-transport | P | Primitive. |
| 3 | P10 spinor rule-type | P | Primitive. |
| 4 | Spinor rule-type structure is four-component Cl(3,1) | I | Paper_RQM_T2. |
| 5 | Spinor rule-types are fermionic, $s = 1/2$ | I | Paper_RQM_T1. |
| 6 | Klein–Gordon governs scalar rule-types | I | Paper_RQM_T5. |
| 7 | First-order equation preferred for spinor sector (probability-current + Stone) | D-via-I | Standard argument. |
| 8 | Factorization $D \bar{D} = -\square + m^2c^2/\hbar^2$ | I | Standard math (I-Dirac). |
| 9 | Dirac operator $D = i\gamma^\mu\partial_\mu - mc/\hbar$ | D | From step 8. |
| 10 | Lorentz covariance via $S(\Lambda)$ spinor rep | I | Standard rep theory (I-Lorentz). |
| 11 | Mass parameter $m$ in Dirac equation | I | Empirical / standard matching. |
| 12 | Specific particle masses (electron, muon, ...) | I | Empirical. |
| 13 | Dirac equation as Arc-R Stage R.3 canonical result | A→position | Framing-claim verdict row (per Paper_095 §3.3): position-statement classification of the result within the Arc-R program, not derivation. |
| 14 | Substrate-V1 propagation produces Dirac structure under DCGT | D-via-I | Paper_089 + Paper_073 coarse-graining (asserted via inheritance). |
| 15 | Substrate-V1 → Dirac equation explicit derivation | OPEN | The §3.7 substrate-V1 connection is asserted via standard substrate-Lorentz-covariantization (Paper_017 inheritance) but the explicit substrate-graph-to-Dirac derivation is not closed in this paper. |

---

## §5 Falsification Criteria

- **F1: Empirical detection of spin-1/2 particle propagation NOT obeying Dirac equation** in regimes where standard QFT predicts Dirac. Would refute the substrate-Dirac identification.

- **F2: Cl(3,1) structure (T2) shown to admit non-Dirac first-order spinor equations.** Would refute the uniqueness of Dirac form.

- **F3: Substrate-level evidence that V1 + DCGT coarse-graining for spinor rule-types produces a non-Dirac PDE.** Would refute §3.7 substrate-V1 connection.

- **F4: Failure of factorization $D \bar{D} = -\square + m^2c^2/\hbar^2$ under any admissible Cl(3,1) realization.** Standard math; would refute I-Dirac.

---

## §6 Position Statement

Paper RQM-T4 establishes the Dirac equation as **M2 (Intermediate Path C)** per Paper_095 — structural mechanism identified, but explicit closed-proof substrate-V1 → Dirac reduction OPEN. Load-bearing primitives: P05 + P06 + P09 + P10 + P13 with no new postulates. The Dirac operator's structural form is FORM-FORCED by composition of T1 (spin–statistics), T2 (Cl(3,1)), and T5 (KG) with standard first-order-equation machinery; mass parameter $m$ is VALUE-INHERITED via empirical matching. The result joins the Wave-3 Relativistic-QM Bridge family as Arc-R Stage R.3, the first-order spinor equation companion to T5 (scalar KG), extending via T6 (minimal coupling) and classified via T7 (Lorentz representations).

This paper does NOT close the substrate-V1 → Dirac derivation at the closed-proof level (flagged OPEN in §3.7 + audit row 15); it does NOT derive specific particle masses; it does NOT extend to curved-acoustic-metric Dirac, Majorana, or Weyl variants (deferred).

This paper is in the Wave-3 Relativistic-QM Bridge series of the Event Density program — a substrate-ontology research program in the lineage of 't Hooft's cellular-automaton interpretation, Wolfram's Ruliad, and the causal-set program (Sorkin et al.); NOT in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §7 Rewrite Note

This paper supplies the Arc-R Stage R.3 spinor-equation result for the substrate framework. Dirac equation form FORM-FORCED; mass values INHERITED.

**Relationship to other RQM-bridge papers:**
- **T1 spin–statistics + T2 Cl(3,1):** supply the algebraic spinor structure.
- **T3 anyon prohibition:** establishes fermion/boson dichotomy at the same dimensional level.
- **T5 Klein–Gordon:** provides the scalar-rule-type companion; Dirac factorizes KG.
- **T7 Lorentz representations:** classifies spinor rep that Dirac transforms under.
- **T6 minimal-coupling:** extends Dirac to interaction with gauge fields.

**Numerical content INHERITED.** Specific particle masses, coupling constants. **Form FORCED.** The Dirac equation structure for spinor rule-types in $D = 3+1$.

**Future work.** Substrate-level audit of Dirac-equation extensions: Majorana, Weyl, gravitational Dirac on curved acoustic metric (Arc GR-Dirac). Also: substrate-derivation of mass parameter $m$ from Arc M H1-dominant structural-form analysis.

Verdict: **M2 (Intermediate Path C)**.

---

**End Paper RQM-T4.**
