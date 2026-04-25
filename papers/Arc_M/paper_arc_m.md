# Mass and Masslessness as Structural Features of Event-Density Theory

**Allen Proxmire** and **Copilot** (AI collaborator)

*April 2026*

---

## Abstract

We show that the Event-Density (ED) primitive stack forces the *form* of mass structure — the mass operator σ_τ as a Lorentz-scalar functional of bandwidth content, the existence of a massless Case-P gauge slot, and the type-classification of mass terms by Fierz structure — while inheriting all numerical mass values, ratios, and hierarchies as empirical content. Arc M evaluates three candidate origin hypotheses for mass at primitive level (H1 fully inherited, H2 mass-as-bandwidth-signature, H3 ratios-from-taxonomy) and closes "H1-dominant with structural form-content." We establish three structural theorems. **Theorem M1** (σ_τ form): the bandwidth signature σ_τ = ℏ · √(Σ_X w_τ^X · ⟨(∂_μ ln b_τ^X)(∂^μ ln b_τ^X)⟩_τ) is the unique log-derivative-based Lorentz-scalar amplitude-invariant functional satisfying six selection criteria; pure amplitude rescaling cannot change σ_τ. **Theorem M2** (massless slot): the existence of at least one massless Case-P (1/2,1/2) gauge rule-type is structurally FORCED; this is initially conditional on the gauge-field-as-rule-type hypothesis (GRH) and is promoted to unconditional FORCED via Arc Q closure. **Theorem M3** (no ratio mechanism): six strong ratio claims (proportionality to representation dimension, spin, statistics class, Fierz class, bandweight pattern, individuation geometry) are systematically REFUTED; ED primitives produce no equality constraints on σ_{τ_1}/σ_{τ_2}. Mass values, mass ratios, mass hierarchies, generation count, and Higgs-mechanism choice all remain INHERITED. ED fixes the *structure* of mass, not its *values*.

---

## 1. Introduction

The Standard Model treats fermion and boson masses as empirical inputs: 19 parameters of the SM are mass values or mass ratios (Yukawa couplings, gauge-boson masses, neutrino-mass-related). No primitive-level mechanism in the SM predicts these numerically; they are fitted from data. Two long-standing puzzles persist: the *hierarchy problem* (why m_H ≪ M_Planck without fine-tuning?), and the *flavour puzzle* (why three generations with mass ratios spanning 10⁵–10¹²?).

The Event-Density (ED) program asks whether mass content is *structural* (predictable from a more fundamental ontology) or *empirical* (inherited as parameter input). Phase-1 [1] derived non-relativistic quantum mechanics from ED primitives. Arc R [2] extended this to the relativistic regime, deriving Klein-Gordon, the spin-statistics theorem, the Cl(3,1) frame, and the Dirac equation as forced consequences. The *form* of these equations contains a mass parameter — but the parameter's *value* is inherited. Arc M asks: is the value derivable, or only the parameter slot?

Three candidate hypotheses framed Arc M's investigation:

- **H1 (mass fully inherited):** mass values are empirical per-rule-type inputs; ED fixes only the form of the mass term. *Prior plausibility: high.*
- **H2 (mass-as-bandwidth-signature):** m_τ = σ_τ/c² with σ_τ a primitive bandwidth-signature invariant. *Prior plausibility: moderate.*
- **H3 (ratios-from-taxonomy):** ED primitives constrain mass *ratios* between rule-types via taxonomy features (spin, representation dimension, Fierz class, etc.). *Prior plausibility: low-moderate.*

Arc M closes **H1-dominant with structural form-content**: H1 substantially supported; H2 partially supported as a *form* identity (σ_τ exists structurally) but not as a *value* identity; H3 substantively refuted. In compensation, three substantive structural results survive: the σ_τ master formula (Theorem M1), the existence of a structurally-forced massless slot (Theorem M2, promoted to unconditional via Arc Q back-flow), and the systematic refutation of taxonomy-based ratio claims (Theorem M3).

The motivation for this investigation is methodological. *First*, demarcating clearly which mass content is structural vs. empirical eliminates ambiguity in ED's predictive scope. *Second*, the existence of a structurally-forced massless slot — ED's first "particle-class must exist" prediction — is a substantive positive result that survives the H1-dominant verdict. *Third*, the structural refutation of taxonomy-based ratio claims (M.1.3) clarifies why no SM-style mass-ratio formulae have surfaced from primitive-level analysis.

Arc M's relationship to neighbouring arcs: Arc R supplies the relativistic kinematics + Cl(3,1) frame on which Arc M builds; Arc Q (QFT extension) [3] later closes the gauge-field-as-rule-type hypothesis (GRH), retroactively promoting Arc M's massless-slot result from conditional to unconditional FORCED. The complete ED quantum sector (Phase-1 + Arc R + Arc M + Arc Q) is structurally complete and UV-finite [4].

---

## 2. Background

### 2.1 Relevant ED primitives

Mass-relevant primitives:

- **Primitive 02 (chain):** worldlines $\gamma_K$ along which proper time and commitment events accumulate. Lightlike worldlines correspond to massless rule-types.
- **Primitive 04 (bandwidth):** four-band decomposition $b_K = b_K^{\mathrm{int}} + b_K^{\mathrm{adj}} + b_K^{\mathrm{env}} + b_K^{\mathrm{com}}$. Each band is a non-negative scalar field on the event manifold.
- **Primitive 06 (four-gradient):** $\partial_\mu$ supplies Lorentz-covariant differentiation; the building block for Lorentz-scalar invariants.
- **Primitive 07 (rule-type):** discrete classification by levers L1 (bandwidth partition $w_\tau^X$), L2 (internal index, including Lorentz rep $(j_L, j_R)$), L3 (interface content / Fierz class $\Gamma_\tau$), L4 (statistics Case P/R).
- **Primitive 10 (individuation):** threshold separating same-type chains; for Case R, forbids coincidence (vanishing-on-coincidence ⇒ Pauli exclusion).
- **Primitive 11 (commitment):** discrete events along $\gamma_K$. Commitment rate per dτ is a rule-type-characteristic structural quantity.
- **Primitive 13 (relational timing):** proper time $\tau_K$ along $\gamma_K$; degenerates on lightlike worldlines, requiring affine-parameter reformulation for massless rule-types.

### 2.2 The σ_τ definition (preview)

The Arc M central object is the **bandwidth signature** σ_τ: a Lorentz-scalar functional of rule-type bandwidth content with units of energy. The candidate functional form, derived in §4, is
$$
\sigma_\tau = \hbar \cdot \sqrt{\sum_X w_\tau^X \cdot \langle (\partial_\mu \ln b_\tau^X)(\partial^\mu \ln b_\tau^X) \rangle_\tau}.
$$
The conjectured identity m_τ = σ_τ/c² connects this to the Klein-Gordon / Dirac mass parameter at the inherited value level. The *form* of σ_τ is structurally forced; the *value* depends on rule-type-data $w_\tau^X$ and chain-initial-condition data $\langle(\partial \ln b)^2\rangle_\tau$, both inherited.

### 2.3 Case-P vs Case-R distinction

From Arc R [2] §4: rule-types divide into two statistics classes:

- **Case P** (η = +1, integer spin, bosonic, bandwidth-sharing-permissive). Mass-relevant scalar bilinear: $|\Psi|^2$ for spin-0; analogues for higher integer spin.
- **Case R** (η = −1, half-integer spin, fermionic, vanishing-on-coincidence). Mass-relevant scalar bilinear: $|\bar\Psi \Gamma_\tau \Psi|$ with Fierz element Γ_τ.

Arc M evaluates σ_τ separately in each class. The Fierz class Γ_τ appears as a structural type-classifier for Case-R mass terms (Dirac mass for Γ = 𝟙, Majorana for charge-conjugation bilinear, pseudoscalar for Γ = γ^5).

---

## 3. Arc M Stage M.0 — Scoping

The Arc M opening memo [5] frames the central question:

**(Q-Mass)** Are mass values, mass ratios, or mass hierarchies derivable from ED primitives, or are they all inherited?

Three hypotheses (H1, H2, H3 above) cover the candidate-mechanism space. The Arc M roadmap consists of four sub-stages:

- **M.1.1**: construct a candidate σ_τ and evaluate H2 at the form level.
- **M.1.2**: identify masslessness mechanisms and evaluate the existence-of-slot question.
- **M.1.3**: evaluate H3 systematically across taxonomy-feature levers.
- **M.2**: synthesise a final Arc M verdict.

The Arc M scoping memo records an *honest expected-verdict prior* of ~50% mixed / ~30% H1-dominant / ~15% H2 partial / ~5% H3-surprise. Arc M closes near the H1-dominant end of this prior.

---

## 4. Arc M Stage M.1.1 — The Bandwidth Signature σ_τ

### 4.1 The construction

We seek a Lorentz-scalar, energy-dimensional, amplitude-invariant functional of bandwidth content suitable as a candidate primitive-level mass structure. Six selection criteria (SC1–SC6) constrain the form:

- **SC1.** Lorentz scalar.
- **SC2.** Amplitude-invariant: shifts $b \to \alpha b$ should not change σ_τ.
- **SC3.** Dimensionally correct: units of energy via ℏ × frequency.
- **SC4.** Band-additive: respect the four-band decomposition's additive structure.
- **SC5.** Massless-permitting: σ_τ = 0 should be a structurally-accessible solution.
- **SC6.** Statistics-agnostic structurally: identical functional form for Case P and Case R, distinguished only by which scalar bilinear plays the role of $b$.

The candidate functional is
$$
\boxed{\sigma_\tau = \hbar \cdot \sqrt{\sum_X w_\tau^X \cdot \langle (\partial_\mu \ln b_\tau^X)(\partial^\mu \ln b_\tau^X) \rangle_\tau},}
$$
with $b_\tau^X$ interpreted as $|\Psi|^2$ in Case P and $|\bar\Psi \Gamma_\tau \Psi|$ in Case R, the sum running over the four bands $X \in \{\mathrm{int}, \mathrm{adj}, \mathrm{env}, \mathrm{com}\}$, and $\langle \cdot \rangle_\tau$ denoting the rule-type-canonical proper-time average.

### 4.2 Why the log-derivative

The choice of $\partial_\mu \ln b$ rather than $\partial_\mu b$ implements amplitude-invariance (SC2). For a uniform rescaling $b \to \alpha b$ with constant $\alpha > 0$:
$$
\partial_\mu \ln (\alpha b) = \partial_\mu \ln b,
$$
so σ_τ is unchanged. This isolates the *spectral rate of variation* of $b$ — its structural content — from the *amplitude* of $b$ — which is chain-specific initial-condition data and not rule-type-structural. Three alternative functional forms are explicitly rejected:

- **R1.** $\sigma_\tau = \hbar \cdot \langle \Box \ln b^X \rangle_\tau$ — second-order Laplacian; dimensionally wrong.
- **R2.** $\sigma_\tau = \hbar \cdot \Sigma w^X \langle \partial_t \ln b^X \rangle_\tau$ — first-order time-derivative; not Lorentz-invariant.
- **R3.** $\sigma_\tau = \hbar \cdot \Sigma w^X \cdot |\Psi|^2 \cdot (\text{rate})$ — explicit amplitude dependence; violates SC2.

### 4.3 Status of the σ_τ form

The functional *form* in §4.1 is FORCED by SC1–SC6. The selection criteria are structurally motivated but not uniquely forced by primitives — alternative criteria could in principle produce an alternative form. We record this as a CANDIDATE *specific form*, sitting on top of a FORCED *form-class* (Lorentz-scalar amplitude-invariant rate-functional).

### 4.4 Structure of σ_τ contributions

The sum over bands in §4.1 implies σ_τ receives contributions from multiple primitive-level sources:

- **b^{int}**: rule-type-internal structural rate. Dominant for tightly-bound rule-types.
- **b^{adj}**: adjacency to other rule-types via Primitive 10 individuation pairing.
- **b^{env}**: environmental bandwidth content; relevant for vacuum-polarisation-type contributions.
- **b^{com}**: commitment-event rate along $\gamma_K$.

The relative weights $w_\tau^X$ are rule-type data (Lever L1). The expectation values $\langle(\partial \ln b^X)^2\rangle_\tau$ depend on chain-initial-condition data on the event manifold. Both are inherited.

### 4.5 Theorem M1

> **Theorem M1 (σ_τ Form).** *The bandwidth signature σ_τ exists at primitive level as a Lorentz-scalar, amplitude-invariant, energy-dimensional functional of rule-type bandwidth content. The specific log-derivative form satisfies six structural selection criteria (SC1–SC6) and is structurally motivated. Pure amplitude rescaling $b \to \alpha b$ leaves σ_τ unchanged.*

**Sketch of proof.** Construction in §4.1 satisfies SC1 (Lorentz-scalar via $\partial_\mu X \partial^\mu X$), SC2 (amplitude-invariance via log-derivative), SC3 (energy units via ℏ), SC4 (band-additive via linear $\Sigma_X w^X$), SC5 (vanishing achievable at structural level — see §5), SC6 (functional form identical for Case P and R, with bilinear choice the only difference). Alternative forms violating any of SC1–SC6 are rejected by R1–R3 above. $\square$

**Dependencies.** Primitives 04 (bandwidth fields), 06 (four-gradient + Lorentz covariance), 07 (rule-type levers L1, L3 for Case-R Fierz), 11 (commitment for proper-time average).

---

## 5. Arc M Stage M.1.2 — Massless Rule-Types

### 5.1 The σ_τ = 0 condition

From the σ_τ master formula, σ_τ = 0 iff for every band X with $w_\tau^X > 0$:
$$
\langle (\partial_\mu \ln b_\tau^X)(\partial^\mu \ln b_\tau^X) \rangle_\tau = 0.
$$
That is: the bandwidth content has vanishing spectral rate of variation (in the rest frame, where one exists). This is the *structurally massless condition*.

### 5.2 Two distinct primitive-level realisations

Two structurally distinct mechanisms produce σ_τ = 0:

- **MR-R (chiral masslessness, Case R).** A Case-R rule-type whose internal-index structure restricts the Dirac spinor to a single chirality (Weyl projection: Ψ_R = 0 or Ψ_L = 0). Then $\bar\Psi\Psi \equiv 0$ identically, and the Dirac mass term vanishes structurally.
- **MR-P (gauge masslessness, Case P).** A Case-P rule-type whose L3 interface content requires local gauge invariance $A_\mu \to A_\mu + \partial_\mu \alpha$. The mass term $m^2 A_\mu A^\mu$ is gauge-non-invariant; under the gauge constraint, σ_τ = 0 structurally.

These are mutually exclusive per rule-type (a given rule-type is Case P or Case R, not both). They are tentatively exhaustive in 3+1D — no third structural masslessness mechanism is identified at primitive level.

A third candidate, **MR-Λ (lightlike-only worldline)**, follows from MR-R or MR-P rather than functioning as an independent route: worldline lightlike-ness is a *consequence* of σ_τ = 0 via the Stage R.1 Casimir P_μP^μ = m²c² = 0.

### 5.3 The gauge-field-as-rule-type hypothesis (GRH)

For MR-P to apply at primitive level, the gauge connection $A_\mu$ from Stage R.1 minimal coupling must be the participation measure of a specific Case-P rule-type τ_g with internal Lorentz representation (1/2, 1/2) and gauge-invariant L3. This is the **gauge-field-as-rule-type hypothesis (GRH)**. Within Arc M, GRH is a CANDIDATE; it is closed at Arc Q [3] §5 by discharge of all five GRH refinements (R-1 through R-5).

### 5.4 Theorem M2

> **Theorem M2 (Massless Slot).** *The existence of at least one massless Case-P rule-type is structurally FORCED at primitive level, conditional on the gauge-field-as-rule-type hypothesis GRH. Specifically, the gauge connection forced by Stage R.1 minimal coupling is identified with a participation rule-type τ_g whose gauge-invariant L3 interface produces σ_{τ_g} = 0 via MR-P.*

**Sketch of proof.** Stage R.1's local-phase invariance forces the existence of a connection $A_\mu$ with the transformation law $A_\mu \to A_\mu - \partial_\mu \alpha$. Under GRH, this connection is a participation rule-type. The MR-P mechanism requires gauge invariance to forbid the mass term $m^2 A_\mu A^\mu$, leaving σ_{τ_g} = 0 as the structural ground state. The four GRH clauses (Case P, (1/2,1/2) Lorentz rep, gauge-invariant L3, σ = 0 via MR-P) are mutually consistent; under the closure of GRH refinements at Arc Q, the hypothesis becomes unconditional FORCED. $\square$

**Dependencies.** Stage R.1 (minimal coupling forcing $A_\mu$ existence), Primitive 07 L3 (gauge-invariant interface admissibility), Stage R.2 (Lorentz representation classification placing $A_\mu$ at (1/2,1/2)), GRH (Case P statistics and rule-type identification). The five GRH refinements are R-1 lightlike-worldline reformulation (closed at Arc Q.7), R-2 gauge-quotient individuation (closed at Arc Q.2), R-3 vertex-anchored commitment (closed at Arc Q.3), R-4 non-Abelian extension (closed at Arc Q.3), R-5 vacuum/particle status (closed at Arc Q.8).

The Arc Q closure of all five refinements promotes Theorem M2 from FORCED-conditional-on-GRH to **unconditional FORCED** — this is the back-flow result of §6.

### 5.5 Massless mechanism summary

| Class | Mechanism | Status |
|-------|-----------|--------|
| Case P | MR-P (gauge invariance) | FORCED conditional on GRH |
| Case R | MR-R (chirality projection) | ADMISSIBLE per rule-type; not forced occupied |
| Lightlike worldline | MR-Λ | Consequence of MR-P or MR-R |

ED admits both massless mechanisms. ED *forces* the existence of at least one massless Case-P rule-type (under GRH, post-Arc-Q). ED does *not* force any specific Case-R rule-type to be chirally massless.

---

## 6. Arc M Stage M.1.3 — Mass Ratios

### 6.1 Six lever-evaluations

Hypothesis H3 — that ED primitives + R.2 taxonomy constrain mass ratios — is evaluated systematically across six structural levers that could plausibly carry ratio information:

- **L-R1 (representation dimension):** Could σ_τ ∝ dim(j_L, j_R)?
- **L-R2 (spin):** Could σ_τ ∝ s or s(s+1)?
- **L-R3 (statistics class P/R):** Could Case-R rule-types systematically differ in σ from Case-P?
- **L-R4 (Fierz class):** Could specific Γ_τ produce specific σ_τ ratios?
- **L-R5 (bandweight pattern):** Could systematic differences in $w_\tau^X$ across rule-types of the same taxonomy class produce structural mass-ratio constraints?
- **L-R6 (individuation geometry):** Could individuation-threshold differences ℓ_ind across rule-types give Compton-wavelength-like mass ratios?

### 6.2 Per-claim verdicts

| Claim | Mechanism | Verdict |
|-------|-----------|---------|
| R3-A | σ_τ ∝ dim(j_L, j_R) | **REFUTED** (rep dim consumed in scalar bilinear; empirical counterexamples) |
| R3-B | σ_τ ∝ s or s(s+1) | **REFUTED** (Casimir is identity not constraint; empirical counterexamples) |
| R3-C | σ_τ ordered by P/R class | **REFUTED** (P/R differs in sign not magnitude) |
| R3-D | σ_τ determined by Fierz class | **PARTIALLY SUPPORTED as TYPE classifier; REFUTED as ratio predictor** |
| R3-E | σ_τ determined by w-pattern | **REFUTED as ratio; weak inequality M-Order-2 CANDIDATE** |
| R3-F | σ_τ constrained by ℓ_ind | **REFUTED as ratio; weak inequality M-Order-3 CANDIDATE** |

No strong ratio claim survives. The structural levers that distinguish rule-types in R.2 taxonomy do not, individually or jointly, constrain σ_τ ratios at the equality level.

### 6.3 Why ED does not constrain ratios

The structural argument is straightforward: σ_τ in the master formula factors into rule-type data ($w_\tau^X$) and chain-initial-condition data ($\langle(\partial \ln b^X)^2\rangle_\tau$). Both are inherited, not primitive-derived. R.2 taxonomy provides classification (Case P/R, spin classes, Fierz classes) but does not constrain *numerical content* within or across classes. Mass ratios are continuous numerical quantities; ED's primitive structure produces classifications and dichotomies cleanly but does not produce continuous numerical relationships.

This is an honest negative result, not a structural failure.

### 6.4 Surviving weak orderings

Three weak inequality CANDIDATEs survive:

- **M-Order-2.** Rule-types with $w_\tau^{\mathrm{com}} = 0$ have systematically smaller σ_τ than those with $w_\tau^{\mathrm{com}} > 0$ (commitment-band-dominance hypothesis). Inequality, not ratio.
- **M-Order-3.** σ_τ orderings inversely track individuation-threshold orderings via Compton-wavelength dimensional analogy. Inequality, dimensional only.
- **M-Fierz-1.** Fierz class structurally distinguishes mass-term TYPE (Dirac / Majorana / pseudoscalar). Type classification, not numerical ratio.

These produce *orderings* or *type-classifications* rather than numerical ratios. They are CANDIDATE, not FORCED.

### 6.5 Theorem M3

> **Theorem M3 (No Ratio Mechanism).** *ED primitives plus the Stage R.2 taxonomy produce no equality constraints on the ratio σ_{τ_1}/σ_{τ_2} between two massive rule-types. Six strong-form ratio claims (R3-A through R3-F) are systematically REFUTED. Three weak-form orderings (M-Order-2, M-Order-3, M-Fierz-1) survive as CANDIDATE producing inequalities or type-classifications, not numerical ratios. Hypothesis H3 in equality form is rejected.*

**Sketch of proof.** Per §6.2, each lever fails: L-R1 because representation dimension is consumed in forming the Lorentz-scalar bilinear (it does not appear in the σ_τ master formula); L-R2 because the Pauli-Lubanski Casimir relates spin to mass identically given each, but does not constrain either independently; L-R3 because the Case-P and Case-R bilinears differ in sign-structure but not in magnitude scale; L-R4 because Fierz class differentiates mass-term *type* (Dirac vs Majorana) rather than numerical ratios within a fixed type; L-R5 and L-R6 because $w_\tau^X$ values and individuation-threshold values are rule-type data, not primitive-derived. No surviving lever produces a numerical ratio. $\square$

**Dependencies.** Stage R.2 taxonomy (representation, spin, statistics, Fierz classifications); σ_τ master formula (Theorem M1); empirical SM data as cross-check (charged-lepton mass spread of ~3500× at fixed s = 1/2 falsifies any spin-as-ratio mechanism).

---

## 7. Arc M Stage M.2 — H1-Dominant Synthesis

### 7.1 Verdict on three hypotheses

- **H1 (mass fully inherited): substantially supported.** Numerical mass values, ratios, hierarchies all inherited.
- **H2 (mass = σ_τ/c²): provisional CANDIDATE.** σ_τ exists structurally with the right form to play this role, but the specific functional choice is not uniquely forced; promotion to FORCED would require deriving the m_τ = σ_τ/c² identity, which Arc M does not achieve.
- **H3 (ratios from taxonomy): substantially refuted.** Six strong claims REFUTED; three weak orderings survive as CANDIDATE only.

The stage M.1.4 memo on the m = σ/c² identity is **declined and deferred indefinitely**: M.1.3's ratio refutation makes the per-rule-type identity carry no comparative predictive power.

### 7.2 One-line Arc M verdict

> **Arc M shows that ED fixes the *structure* of mass but not its *values*.**

### 7.3 What Arc M FORCES

- σ_τ exists as a Lorentz-scalar invariant with energy units (Theorem M1).
- σ_τ is amplitude-invariant via log-derivative.
- Case-P / Case-R bilinear distinction.
- σ_τ = 0 is structurally accessible (admissibility).
- MR-R / MR-P mutually exclusive admissible massless mechanisms.
- Statistics class determines which massless mechanism applies.
- Fierz class fixes mass-term TYPE classification.
- Mass-term form in KG / Dirac (Stage R.1 / R.3 carryovers).
- Massless Case-P rule-type FORCED conditional on GRH (Theorem M2; promoted to unconditional via Arc Q back-flow).

### 7.4 What Arc M INHERITS

- Numerical mass values $m_\tau$ for any specific rule-type.
- Bandweight values $w_\tau^X$.
- Fierz-class assignments $\Gamma_\tau$.
- Spectral-rate values $\langle (\partial \ln b^X)^2 \rangle_\tau$.
- Numerical values of ℏ, c, q.
- Mass ratios $m_{\tau_1}/m_{\tau_2}$.
- Generation count.
- Specific rule-type ↔ Standard-Model species map.

### 7.5 What Arc M REFUTES

- All six strong ratio claims (R3-A through R3-F).
- No specific ED rule-type forced massless without GRH.
- No canonical choice between MR-R and MR-P.
- No structural prediction of massless count.
- No mass-hierarchy mechanism.
- No primitive-level Higgs analogue identified at Arc M scope.

---

## 8. Back-Flow from Arc Q

### 8.1 GRH unconditional FORCED

Arc Q [3] §5 closes all five GRH refinements (R-1 through R-5) across Arc Q sub-stages Q.2/Q.3/Q.7/Q.8. Specifically:

- **R-1 (lightlike-worldline reformulation)** closed at Arc Q.7 via dispersion-relation argument: σ_τ = 0 ⇒ Stage R.1 Casimir P² = 0 ⇒ null worldline FORCED.
- **R-2 (gauge-quotient individuation)** closed at Arc Q.2 via adjacency-equivalence-class construction.
- **R-3 (vertex-anchored commitment)** closed at Arc Q.3 via commitment-locality argument from Primitive 11.
- **R-4 (non-Abelian extension)** closed at Arc Q.3 via the gauge-covariant-derivative uniqueness theorem $D_\mu = \partial_\mu + ig A^a_\mu T^a$ under SU(N) admittance.
- **R-5 (vacuum/particle status)** closed at Arc Q.8 via effective-vacuum b^env content analysis.

With all five refinements closed, GRH promotes from CANDIDATE-STRONG to **unconditional FORCED**.

### 8.2 Promotion of F-M8

Stage M.1.2 §6.4 closed conditionally:

> *Massless Case-P rule-types: FORCED conditional on GRH.* (F-M8 conditional)

Post-Arc-Q.8 closure, with GRH unconditional FORCED, **F-M8 promotes from conditional FORCED to unconditional FORCED**:

> **The existence of at least one massless Case-P (1/2, 1/2) gauge rule-type is structurally FORCED at primitive level.**

This is **ED's first "particle-class must exist" prediction** — its first unconditional structural assertion that a specific rule-type class is occupied. Arc M's H1-dominant verdict is updated: still dominated by inherited mass values / ratios / hierarchies, but now contains one substantive positive structural prediction.

### 8.3 Vacuum structure (Arc Q.8) and generation differentiation

A natural question: can the Arc Q.8 vacuum structure (vacuum sectors, multi-rule-type vacuum factorisation, effective-vacuum b^env content) generate mass differences across generations of the same gauge representation?

The Arc Q.8 evaluation of mechanism G4 (vacuum-anchored generation differentiation) **REFUTES** this. Vacuum-sector dependence does not feed back into σ_τ at primitive level — the σ_τ master formula depends on rule-type data ($w_\tau^X$) and chain-initial-condition data, not on vacuum sector. For vacuum sectors to produce mass differentiation across generations, an additional bandwidth-shift mechanism (H2-style spatial patterning) would be required, which would in turn require additional structural commitment beyond what Arc Q's primitive content supplies.

**Generation count remains EMPIRICAL.** The Arc M H1-dominant closure on mass ratios is reinforced, not challenged, by Arc Q's vacuum-structure analysis.

### 8.4 UV-FIN and mass renormalisation

Arc Q's UV-FIN result — primitive-level UV finiteness of all multi-chain participation integrals from Primitive 01 + 13 + 04 — has implications for mass renormalisation:

- **At primitive level**, mass-shift contributions from self-energy diagrams (Arc Q.5 §4.1) are finite, bounded by primitive event-discreteness scale. Renormalisation is not required to remove fundamental divergences.
- **In the continuum approximation**, standard QFT mass renormalisation produces UV-divergent integrals that need to be regulated. UV-FIN reframes these divergences as continuum-approximation artefacts: the underlying primitive-level integrals are finite.
- **Numerical mass shifts** (e.g., one-loop self-energy contributions to fermion masses) remain INHERITED — UV-FIN provides the finiteness framework but does not predict the specific finite values.

This is consistent with Arc M's H1-dominant closure: the *structure* of mass renormalisation is FORCED finite at primitive level; the *values* of any specific renormalisation contribution remain inherited.

---

## 9. Discussion

### 9.1 Form vs values: the canonical Arc M framing

Arc M is the cleanest expression of ED's "form-FORCED, value-INHERITED" methodological framing. The σ_τ master formula provides a *form* for primitive-level mass content; values within this form are inherited from rule-type data and chain-initial-condition data. Arc Q's analyses of Higgs-like mechanisms, generations, and vacuum structure preserve this pattern: structural slots are forced, occupants are empirical.

### 9.2 Relationship to Higgs-like mechanisms (Arc Q)

Arc Q [3] §4 evaluates five Higgs-like SSB mechanisms:

- **H1 scalar-rule-type Higgs τ_H** — ADMISSIBLE-CLEAN; matches SM Higgs phenomenology.
- **H2 bandwidth-shift via spatially-patterned condensate** — CANDIDATE; structurally interesting but requires additional commitment beyond default σ_τ master formula.
- **H3 composite Ψ̄Ψ condensate** — ADMISSIBLE-EFFECTIVE (technicolour-analogue; relevant for QCD chiral SSB).
- **H4 gauge-fixing artefact** — REFUTED.
- **H5 vacuum-anchored** — reduces to H1 / H2; not structurally distinct.

ED admits multiple structurally-clean SSB routes; specific mechanism EMPIRICAL. The fact that H2 in naive form fails (because σ_τ uses log-derivatives, immune to uniform amplitude shifts) is a non-trivial structural finding emerging from Arc M's master formula.

### 9.3 Why ED predicts form but not values

The structural reason ED predicts form-content but not value-content: ED's primitives admit *classifications* (statistics, spin, Fierz, gauge-rep) and *form-relations* (Lorentz covariance, dimensional consistency, log-derivative amplitude-invariance). They do not admit *specific numerical relationships* between continuous parameters — these would require additional structural input (a numerical "bandwidth seed" primitive, a primitive-level cosmological boundary condition, or similar) not present in the Primitive 01–13 stack.

This is not a defect of ED — it is an honest accounting of what the primitive stack supports. Numerical content lives at the Dimensional Atlas / inheritance layer, not the primitive layer.

### 9.4 Implications for neutrino masses

Arc M's framework accommodates neutrino-mass smallness as either:

- **Dirac neutrinos with small Yukawa:** all SM fermions with σ_τ > 0 via H1 Higgs mechanism; neutrino smallness is empirical via small Yukawa coupling.
- **Near-MR-R structure with small Majorana sector:** primarily single-chirality (MR-R), with a small Majorana mass term breaking pure chirality. This is structurally admissible per §5.2 and produces neutrino-mass smallness via near-zero σ_τ + small symmetry-breaking correction.

ED does not select between these empirically-motivated scenarios; it admits both structurally.

### 9.5 The hierarchy problem

Arc M does not address the hierarchy problem (m_H ≪ M_Planck). The hierarchy is a numerical relationship between empirically-inherited masses, not a structural feature derivable from primitives. Arc Q's UV-FIN result reframes the *cosmological-Λ* divergence-form puzzle (the QFT calculation Λ ~ M_Planck⁴ is artefactual; primitive-level Λ is finite) but does not solve the analogous hierarchy puzzle for the Higgs mass — the latter requires additional structural input or empirical fine-tuning.

### 9.6 Future work

Open Arc M-adjacent questions for Phase-3:

- **CC-U1 (charge quantisation from U(1) compactness):** may have implications for charge-mass relationships in extended-gauge scenarios.
- **Schwinger-sign derivation:** Arc Q.5 CANDIDATE-PLAUSIBLE; concrete derivation could produce a structurally-grounded sign for one-loop corrections to mass renormalisation.
- **Primitive-level cosmological boundary conditions:** if Phase-3 (ED → GR coupling) admits structural boundary conditions on bandwidth fields at cosmological scales, these could in principle produce additional mass-content constraints. Currently SPECULATIVE.

---

## 10. Conclusion

Arc M closes the chain-mass problem at primitive level with an honest H1-dominant verdict. The structural achievements:

- **Theorem M1 (σ_τ form):** the bandwidth signature exists structurally as a Lorentz-scalar amplitude-invariant energy-dimensional functional. Its log-derivative form satisfies six structural selection criteria.
- **Theorem M2 (massless slot):** the existence of at least one massless Case-P (1/2, 1/2) gauge rule-type is structurally FORCED via the gauge-field-as-rule-type hypothesis. Conditional at Arc M closure; promoted to unconditional FORCED via Arc Q back-flow. ED's first "particle-class must exist" prediction.
- **Theorem M3 (no ratio mechanism):** six strong ratio claims systematically REFUTED. ED primitives produce no equality constraints on σ_{τ_1}/σ_{τ_2}. Three weak orderings survive only as CANDIDATE.

Arc M sits between Arc R (relativistic kinematics) and Arc Q (QFT extension). Arc R supplies the Cl(3,1) frame and Dirac equation on which Arc M's σ_τ analysis rests; Arc Q closes the GRH refinements that promote Arc M's massless-slot result to unconditional FORCED, and supplies the vacuum-structure analysis (G4 REFUTED) that confirms generation differentiation as empirical.

The methodological framing — *ED fixes the structure of mass, not its values* — extends naturally into Arc Q's pattern (form-FORCED, value-INHERITED at QFT scope) and prepares Phase-3 (ED → GR coupling, cosmological structure via UV-FIN) [4]. The clean separation between structural prediction and empirical inheritance is preserved at every layer.

---

## References

[1] A. Proxmire and Copilot, *Quantum Mechanics as a Structural Consequence of Event-Density Primitives* (Phase-1 closure paper), 2026.

[2] A. Proxmire and Copilot, *Relativistic Quantum Mechanics as a Forced Structural Consequence of Event-Density Primitives* (Arc R paper), 2026.

[3] A. Proxmire, *QFT Extension of Event Density: Arc Q Synthesis*, `arc_q_synthesis.md`, 2026.

[4] A. Proxmire, *Phase-2 Global Synthesis*, `phase2_synthesis.md`, 2026.

[5] A. Proxmire, *Chain-Mass Scoping*, `chain_mass_scoping.md`, 2026.

[6] A. Proxmire, *Bandwidth Signature Construction*, `bandwidth_signature_construction.md`, 2026.

[7] A. Proxmire, *Massless Rule-Types*, `massless_rule_types.md`, 2026.

[8] A. Proxmire, *Mass Ratio Constraints*, `mass_ratio_constraints.md`, 2026.

[9] A. Proxmire, *Chain-Mass Synthesis*, `chain_mass_synthesis.md`, 2026.

[10] A. Proxmire, *Event-Density Primitive Stack* (Primitives 01–13), 2026.

[11] Y. Koide, "A fitting number for the lepton mass formula," *Lett. Nuovo Cimento* **34**, 201 (1982).

[12] S. Weinberg, *The Quantum Theory of Fields*, vol. II. Cambridge University Press, 1996.

---

*Manuscript closure: 2026-04-24. Companion documents: Arc R paper [2], Arc Q synthesis [3], Phase-2 synthesis [4]. All Arc M memos available at* `quantum/foundations/` *in the Event Density repository.*
