# Chain-Mass Scoping

**Arc M Stage M.0 — Opening Scoping Memo**
**Status:** Scoping only. No derivations attempted; no mass values predicted. Identifies the mass problem at primitive level, enumerates candidate origin hypotheses (H1–H3), and lays out the Arc M roadmap. Honest framing: Arc M is the first ED arc where the likely answer is "mostly inherited" rather than "mostly structural"; this memo says so up front.

---

## 1. The chain-mass problem

### 1.1 Where "mass" has appeared so far in ED

Mass has entered ED as an **inherited dimensional anchor** at two points:

- **Stage Q.2 (non-relativistic QM, `u3_evolution_derivation.md`):** the Schrödinger kinetic coefficient ℏ²/(2m) couples ED's PDE parameter D to inertial mass via the Madelung anchoring D_phys = ℏ/(2m). m enters as a free parameter per rule-type, fitted not derived.
- **Stage R.1 (Klein-Gordon, `klein_gordon_emergence.md`):** the mass term m²c²/ℏ² in (□ + m²c²/ℏ²)Ψ = 0 is the Casimir eigenvalue fixing the rule-type's timelike four-momentum. Again m is a rule-type parameter, not primitive-derived.
- **Stage R.3 (Dirac, `dirac_emergence.md`):** the mass term mc/ℏ in (iγ^μ∂_μ − mc/ℏ)Ψ = 0 is the same parameter, transferred into the first-order form.

In all three cases the **form** of the equation is primitive-forced; the **numerical value** of m is inherited. Arc M asks whether this can be tightened.

### 1.2 What "mass" means at primitive level

Three candidate primitive-level definitions, each operationally distinct:

**(a) Rest mass** m_rest. The Casimir eigenvalue of the Poincaré algebra acting on the rule-type's participation-measure module: P_μ P^μ = m_rest² c². This is the most-used notion in R.1/R.3 and is Lorentz-invariant by construction.

**(b) Inertial mass** m_inert. The coefficient controlling the rule-type's resistance to four-acceleration in response to an applied four-force. Operationally visible in ED as the coefficient in the commitment-dynamics update law linking ∂_τ u^μ (worldline four-acceleration) to applied interaction content.

**(c) Bandwidth signature** σ_τ. A rule-type-specific structural invariant built from the bandwidth content b_K of a chain of rule-type τ — specifically the τ-characteristic energy scale associated with the rule-type's internal structure (bandwidth norm, interface-coupling amplitude, or adjacency-partition spectral scale, depending on which structural feature dominates).

σ_τ is a primitive-level object; m_rest and m_inert are dynamical-equation-level objects. The central question of Arc M is how these connect.

### 1.3 The candidate structural identity m_τ = σ_τ / c²

The natural conjecture is

  **m_τ = σ_τ / c²**                                                            (1)

— the rest mass of a rule-type τ equals its bandwidth-signature energy scale divided by c². This is the Arc M analogue of E = mc² at the rule-type level.

**Status of (1):** Currently a **working hypothesis**. It is:
- *Not a structural identity* — ED primitives do not directly equate σ_τ to a dynamical mass parameter.
- *Not a derived result* — no memo has shown m ≡ σ_τ/c² follows from anything.
- *A CANDIDATE* — structurally plausible and consistent with the Dimensional Atlas; Arc M's first job is to evaluate whether it can be promoted to FORCED or must stay CANDIDATE.

The Einstein mass-energy relation E = mc² is inherited from Lorentz covariance in Stage R.1 (it is built into the KG Casimir). Equation (1) is a **sharper** claim: that the particular energy σ_τ extracted from rule-type bandwidth content is the one that equals mc². Sharpness comes from identifying *which* energy scale it is, not from the existence of an energy-mass equivalence.

### 1.4 Why Arc M is the hardest arc so far (in a different sense)

Previous arcs (Phase-1 QM, R.1, R.2, R.3) were hard because the derivations were intricate but the structural inputs were rich enough to force the outputs. Arc M may be hard in the opposite sense: structural inputs are **thin**. ED primitives as articulated do not obviously encode any mass scale beyond whatever is present in the bandwidth content b_K, and b_K's amplitude is itself inherited from initial/boundary conditions on the PDE, not derived from structural closure.

Arc M's honest null hypothesis is that mass is primarily inherited. The arc's job is to find out how much, if anything, can be **structurally constrained** on top of the inheritance.

---

## 2. Primitive-level structures relevant to mass

### 2.1 Primitive 02 — Worldline and proper time

Supplies the worldline γ_K along which a chain persists and its proper time τ_K. The rate at which commitment events accumulate along γ_K (events per dτ) is a natural candidate for the bandwidth signature σ_τ — a rule-type's characteristic "tick rate" in its own rest frame.

*Candidate connection:* σ_τ ∝ (mean commitment rate per dτ at rest).

### 2.2 Primitive 04 — Bandwidth fields b_K

The bandwidth b_K(x) on the event manifold is the squared amplitude of the participation measure: b_K = |P_K|². Its spectral content (Fourier decomposition along γ_K's tangent) defines a characteristic frequency, which by ℏω ↔ energy (Stage Q.2 / R.1 Planck relation) corresponds to an energy scale.

*Candidate connection:* σ_τ ∝ ℏ · (dominant bandwidth frequency at rest).

### 2.3 Primitive 06 — Four-gradient

Provides the ∂_μ whose square appears in the KG operator. Mass enters as the eigenvalue of P_μP^μ; so the Lorentz structural content ties mass to the timelike projection of the rule-type's four-momentum. Primitive 06 does not itself fix m; it provides the geometric slot.

### 2.4 Primitive 07 — Rule-type taxonomy (post R.2 closure)

Now fully closed (Stage R.2.5). Supplies:
- Lever L1 (bandwidth partition): candidate structural source of σ_τ.
- Lever L2 (internal index content): candidate source of spin-mass coupling.
- Lever L3 (interface content / Fierz class): candidate source of mass-generation mechanism at rule-type level.
- Lever L4 (double-cover structure): already discharged; no direct mass content.

Primitive 07 is the richest primitive-level source for mass-structural content if mass depends on rule-type internal structure.

### 2.5 Primitive 10 — Individuation threshold

Sets the scale at which a chain remains distinguishable as a unit. Candidate connection: the individuation threshold is a spatial scale; by ℏ/(mc) ↔ Compton wavelength, this scale corresponds to a mass. If the individuation threshold is rule-type-specific, it could constrain m_τ.

*Candidate structural identity:* λ_ind,τ · m_τ · c ~ ℏ, i.e., individuation threshold ≈ Compton wavelength. Status: speculative; not yet examined.

### 2.6 Primitive 11 — Commitment dynamics

Sets the rate at which commitment events occur along a worldline. If commitment rate is rule-type-specific and tied to bandwidth signature, this is another candidate for σ_τ.

### 2.7 Stage R.2 outputs

- **Spin:** rule-type's s value. Naïve correlation (empirical Standard Model): higher spin ≠ higher mass, but gauge bosons (s = 1) include both massless (γ, g) and massive (W, Z); fermions (s = 1/2) span 13 orders of magnitude in mass. So spin alone does not determine mass.
- **Cl(3,1) frame:** supplies the Dirac mass term's multiplicative structure (mass as coefficient on 𝟙 vs. γ^5, cf. chiral masses).
- **Statistics class (P vs R):** does this distinguish mass origins? See §3.

---

## 3. Three mass-origin hypotheses

Arc M's job is to evaluate these systematically.

### 3.1 H1 — Fully inherited

**Statement:** Mass values m_τ are empirical per-rule-type inputs. ED primitives fix the form of the Dirac/KG mass term but not its numerical value.

**Consequences:**
- Arc M delivers little new structural content.
- Mass spectrum matches Standard Model by fitting.
- Massless rule-types are permitted (Dirac/KG admit m = 0) but not structurally required.
- Mass hierarchies are empirical.

**Falsifiability:** H1 is the null; it "wins" if H2 and H3 fail.

**Prior plausibility:** High. Most field theories inherit mass; ED has no obvious structural mass-generation mechanism analogous to Higgs VEV at the primitive level.

### 3.2 H2 — Mass = bandwidth signature / c²

**Statement:** m_τ = σ_τ / c², with σ_τ a structural invariant of rule-type τ extractable from Primitives 04/07/10/11 content.

**Consequences:**
- Mass is *constrained* by rule-type structure, not free.
- Different rule-types have different σ_τ, hence different masses.
- Massless rule-types correspond to σ_τ = 0, which has a specific structural meaning (e.g., bandwidth content spectrally flat, or interface-coupling amplitude zero).
- Mass hierarchies become hierarchies of σ_τ.

**Falsifiability:** Requires identifying σ_τ concretely and showing it matches empirical m_τ c² for at least one rule-type to prior-free accuracy.

**Prior plausibility:** Moderate. Structurally attractive but requires σ_τ to be concretely computable, which is non-trivial.

### 3.3 H3 — Mass ratios constrained by taxonomy

**Statement:** ED structure predicts mass *ratios* between rule-types but not absolute mass scales.

**Consequences:**
- Absolute mass scale (e.g., electron mass) remains inherited.
- Ratios like m_μ/m_e, m_τ/m_μ, m_p/m_e, etc. become structurally predicted from taxonomy features (spin, representation, Fierz class, adjacency-graph multiplicity, etc.).
- Generation structure (e, μ, τ as three "copies") must correspond to a structural feature — possibly the three discrete choices in Lever L2 (internal-index dimensionality) or a Lever L3 Fierz-structure multiplicity.

**Falsifiability:** Requires a structural mechanism producing specific ratios matching empirical data.

**Prior plausibility:** Low-moderate. Historical attempts (Koide relation, various BSM models) have produced mass-ratio formulae with empirical fits, but a primitive-level ED derivation would need a genuinely new mechanism. Most likely outcome: ED supplies *constraints* on ratios (e.g., monotonicity, orderings) rather than exact formulae.

### 3.4 Mixed hypotheses

H1 and H2 are not mutually exclusive: ED could predict σ_τ structurally for some rule-types (e.g., massless photon-like) while leaving others fully inherited. Similarly H3 might apply only within generations while inter-generation ratios remain inherited.

Arc M's output is most realistically a **partial** structural prediction: some constraints derivable, others inherited.

---

## 4. What Arc M must deliver

### 4.1 Required outputs

Arc M must at minimum answer:

**(Q-M.1)** Is σ_τ structurally determined by Primitives 02/04/07/10/11 alone?
**(Q-M.2)** If yes, does the answer differ between Case P and Case R rule-types?
**(Q-M.3)** Are massless rule-types (σ_τ = 0) structurally forced for specific classes (e.g., certain gauge bosons)?
**(Q-M.4)** Does ED predict mass scales, ratios, both, or neither?
**(Q-M.5)** What inheritance enters — and at what level (Primitive, PDE-parameter, rule-type, or pure empirical)?

These questions define Arc M's success criteria. A clean "no structural prediction" (H1) is a valid answer if honestly reached.

### 4.2 Specific sub-questions

Beyond the Q-M.*, these sharp sub-questions are worth flagging early:

- **Photon mass.** The electromagnetic gauge boson (s = 1, massless) is the cleanest test case: can ED show σ_τ = 0 for the photon-like rule-type structurally?
- **Graviton mass.** Similar question for spin-2 massless gauge content, though ED's gravity content is kinematic (ED-10 arc closed) and does not yet have a primitive-level graviton rule-type.
- **Neutrino mass.** Small but nonzero; any structural prediction should accommodate.
- **Weak gauge bosons (W, Z).** Massive spin-1; Standard Model uses Higgs mechanism. ED does not yet have a Higgs primitive; can mass be generated without one?
- **Fermion mass hierarchy.** 6 orders of magnitude across charged leptons; 12 orders across all fermions. Is any part of this structurally accessible?

### 4.3 Non-goals of Arc M

Arc M does **not** aim to:
- Predict specific numerical values of electron mass, quark masses, etc., to high precision.
- Resolve the hierarchy problem (why m_Higgs << M_Planck).
- Derive the Standard Model Yukawa matrix.
- Settle CP violation or flavour mixing.

These are Arc Q + empirical-fit territory. Arc M's realistic scope is narrower: identify structural content that constrains mass, and clearly demarcate what remains inherited.

---

## 5. Dependency diagram

```
                    Stage R.2 (rule-type taxonomy, closed)
                                       │
                                       ▼
                    Stage R.3 (Dirac emergence, closed)
                                       │
                                       ▼
                    Arc M Stage M.0 (this memo — scoping)
                                       │
                                       ▼
        Arc M Stage M.1 (mass-spectrum derivation)
          ├── Evaluate H1 (null / inherited)
          ├── Evaluate H2 (σ_τ structural)
          └── Evaluate H3 (ratio constraints)
                                       │
                                       ▼
           Arc M Stage M.2 (synthesis + honest verdict)
                                       │
                                       ▼
            Arc Q (QFT: Yukawa, Higgs, radiative corrections)
          ├── Gauge group SU(3)×SU(2)×U(1) content
          ├── Spontaneous symmetry breaking / Higgs mechanism
          └── Loop-level mass renormalisation
```

### 5.1 Downstream dependencies

- **Arc Q** requires Arc M closure to assign rule-type → mass-term-structure mappings; without M, Q would re-open the same questions.
- **Arc N** (non-Markovian) is independent of M at primitive level but ties in when Arc Q's renormalisation is considered.
- **Platform bridges** (matter-wave, SC qubit, optomech, BEC) are independent of M; they use inherited masses directly.

### 5.2 Upstream status

- Stage R.1, R.2, R.3 all closed. M.0 has all required upstream structure.
- Phase-1 QM also closed; Schrödinger mass m enters as inherited parameter per Madelung anchoring.

---

## 6. Honest framing

### 6.1 FORCED now

- **F1.** Form of mass term in KG / Dirac equations (Stage R.1 / R.3).
- **F2.** Mass-energy equivalence E² = p²c² + m²c⁴ (Lorentz-covariant Casimir, R.1).
- **F3.** Mass as Poincaré Casimir eigenvalue (R.1, R.3).
- **F4.** No structural prediction yet of any specific m_τ value.
- **F5.** Rule-type taxonomy permits both massive and massless rule-types (Dirac/KG admit m = 0 cleanly).

### 6.2 CANDIDATE

- **CANDIDATE σ-M (structural bandwidth signature):** σ_τ is a rule-type-specific primitive-level invariant extractable from Primitives 04/07/10/11. Plausibility: moderate; requires concrete construction in Stage M.1.
- **CANDIDATE m = σ/c² (mass-signature identity):** m_τ = σ_τ / c² as a structural identity. Contingent on σ-M; Stage M.1 to evaluate.
- **CANDIDATE photon-massless (gauge-boson structural masslessness):** σ_τ = 0 structurally forced for specific rule-type classes. Plausibility: moderate if σ-M holds; weaker otherwise.
- **CANDIDATE ratio-struct (structural mass ratios):** ED constrains m_τ / m_τ' for certain rule-type pairs. Plausibility: low at present; no concrete mechanism identified.

### 6.3 SPECULATIVE

- **S1.** Generation count (3) has a primitive-level origin.
- **S2.** Fermion mass hierarchy is structurally derivable.
- **S3.** Higgs mechanism has a primitive-level ED analogue.
- **S4.** Neutrino mass smallness (compared to charged leptons) is structurally forced.
- **S5.** Graviton rule-type exists and is massless.

Items S1–S5 are not rejected; they are listed as speculative because no structural mechanism is currently in hand. Arc M will examine S3 (Higgs analogue) as part of Stage M.1 evaluation; S1, S2, S4, S5 are likely Arc Q + empirical.

### 6.4 What Arc M can realistically achieve in the near term

**Realistic scope (Stage M.1 + M.2):**

- **Likely achievable:**
  - Clean statement of which primitive structures can carry mass content (§2 enumeration is step one).
  - Concrete construction (or disproof) of σ_τ as a bandwidth-signature invariant.
  - Verdict on whether photon-like and graviton-like rule-types have σ_τ = 0 structurally.
  - Honest separation of inherited vs. structural in the final mass story.

- **Possibly achievable:**
  - Partial constraint on mass ratios for rule-types sharing taxonomy class (same spin, same Fierz structure).
  - Massless-rule-type structural classification.

- **Unlikely achievable at Arc M level (probably Arc Q):**
  - Numerical prediction of any specific fermion mass to within orders of magnitude.
  - Generation-count derivation.
  - Full Yukawa / Higgs primitive-level mechanism.

### 6.5 Expected verdict distribution

The honest prior on Arc M's final verdict:

- ~50%: Mixed — some massless classes structurally forced (photon, possibly graviton), absolute scales inherited, ratios partially constrained at best.
- ~30%: H1-dominant — mass is almost entirely inherited; Arc M delivers mostly scoping + negative results.
- ~15%: H2 partial — σ_τ structurally defined for simple classes but not for the full rule-type spectrum.
- ~5%: H3-surprise — an unexpected structural mechanism produces non-trivial mass-ratio constraints.

This distribution is a working estimate for calibration; Arc M's job is to produce a verdict grounded in derivations, not this prior.

---

## 7. Arc M roadmap

### Stage M.0 — This memo (scoping). **Complete.**

### Stage M.1 — Mass-spectrum derivation.

Sub-memos (tentative):

- **M.1.1** `bandwidth_signature_construction.md` — Try to construct σ_τ explicitly from Primitives 04/07/10/11. Verdict: does σ_τ exist as a primitive invariant?
- **M.1.2** `massless_rule_types.md` — Evaluate whether σ_τ = 0 is structurally forced for any rule-type class (photon-like, graviton-like).
- **M.1.3** `mass_ratio_constraints.md` — Evaluate H3 systematically: does rule-type taxonomy constrain m_τ / m_τ' for any taxonomy-related pairs?
- **M.1.4** (contingent on M.1.1) `mass_signature_identity.md` — If σ_τ exists, evaluate m_τ = σ_τ / c² as a derived identity.

### Stage M.2 — Synthesis.

- **M.2** `chain_mass_synthesis.md` — Integrate M.1.* results; final verdict on H1/H2/H3; FORCED/inherited/deferred separation; hand-off to Arc Q.

### Estimated scope

- Stage M.1: 3–6 sessions (dominant variability: whether σ_τ is cleanly constructible).
- Stage M.2: 1 session.
- Arc M total: ~4–7 sessions.

This is a lower-complexity arc than R.2 if the verdict trends toward H1, and higher-complexity if toward H2/H3. The scoping is front-loaded in M.0 (this memo) to keep the M.1 sub-memos focused.

---

## 8. Cross-references

- Upstream: `arc_r_stage1_synthesis.md`, `rule_type_taxonomy_synthesis.md`, `dirac_emergence.md`.
- Related Phase-1: `u3_evolution_derivation.md` (mass as Madelung anchor).
- Dimensional Atlas conventions: (see foundational ED documentation; ℏ, c, m inheritance rules).
- Downstream placeholders: `bandwidth_signature_construction.md`, `massless_rule_types.md`, `mass_ratio_constraints.md`, `chain_mass_synthesis.md`.

---

## 9. One-line summary

**Arc M opens with the honest framing that mass is probably largely inherited in ED: the scoping memo enumerates the primitive-level structures relevant to mass, maps three candidate origin hypotheses (H1 inherited, H2 bandwidth-signature, H3 ratio-constrained), and sets a realistic roadmap whose most likely verdict is a mixed result — structural masslessness for specific gauge-boson-like classes, inherited scales for fermions, and partial constraints on ratios at best.**
