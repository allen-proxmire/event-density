# Mass Ratio Constraints

**Stage M.1.3 — Arc M Sub-Memo**
**Status:** Evaluation memo. Honest verdict: ED primitives + R.2 taxonomy produce **no equality constraints** on mass ratios σ_{τ_1}/σ_{τ_2} for massive rule-types. Three weak structural inequalities survive (M-Order-1, M-Order-2, M-Order-3); these are FORCED but produce only orderings/inequalities, not numerical ratios. The strong ratio claims (R3-A through R3-F) are systematically REFUTED, REJECTED, or relegated to SPECULATIVE. This is the cleanest negative-result memo of Arc M.

---

## 1. Goal

Stage M.0 identified Hypothesis H3 (mass ratios constrained by taxonomy features) as one of three candidate origin hypotheses, with prior plausibility "low-moderate." Stage M.1.1 constructed the bandwidth signature σ_τ; Stage M.1.2 evaluated masslessness. Stage M.1.3 now evaluates H3 directly:

(Q-H3) Do ED primitives + R.2 taxonomy impose **any** structural constraints on the ratio σ_{τ_1} / σ_{τ_2} between two massive rule-types?

The evaluation is systematic: enumerate every primitive-level lever that could carry ratio information, and for each test the strongest claim it could support.

This memo does **not** attempt fits to empirical mass data. It evaluates whether ED *structurally* constrains ratios, irrespective of empirical match.

---

## 2. Setup

### 2.1 Master formula recap

From Stage M.1.1:

  σ_τ = ℏ · √( Σ_X w_τ^X · ⟨ (∂_μ ln b_τ^X)(∂^μ ln b_τ^X) ⟩_τ ).                (1)

The ratio of two rule-type signatures:

  σ_{τ_1} / σ_{τ_2} = √[ Σ_X w_{τ_1}^X · ⟨(∂ ln b^X)²⟩_{τ_1} ] / √[ Σ_X w_{τ_2}^X · ⟨(∂ ln b^X)²⟩_{τ_2} ].   (2)

For (2) to be **structurally** constrained, the rule-type-data inputs (w_τ^X and ⟨(∂ ln b^X)²⟩_τ) must have primitive-level relationships across rule-types.

### 2.2 Available structural levers

Six candidate ratio-constraint levers, drawn from R.2 taxonomy + Primitive 04/07/10:

- **L-R1.** Representation dimension dim(j_L, j_R)_τ = (2j_L+1)(2j_R+1).
- **L-R2.** Spin value s_τ.
- **L-R3.** Case-P vs Case-R class membership.
- **L-R4.** Fierz-class structure of Γ_τ.
- **L-R5.** Band-weight pattern {w_τ^X}.
- **L-R6.** Participation-graph adjacency / individuation threshold geometry.

### 2.3 Candidate ratio claims

Six strongest-form ratio claims to evaluate:

- **R3-A.** σ_τ ∝ dim(j_L, j_R)_τ.
- **R3-B.** σ_τ ∝ s_τ or σ_τ ∝ s_τ + 1 (Casimir-like).
- **R3-C.** σ_τ(Case R) systematically > or < σ_τ(Case P).
- **R3-D.** σ_τ determined by Γ_τ (Fierz class).
- **R3-E.** σ_τ determined by w_τ^X pattern via a structural rule.
- **R3-F.** σ_τ constrained by adjacency/individuation geometry.

For each claim: structural mechanism, evaluation, verdict.

---

## 3. Evaluation per lever / claim

### 3.1 L-R1 / R3-A — Representation dimension

**Mechanism candidate.** A higher-dimensional internal index space might carry more bandwidth content per chain, leading to σ_τ ∝ dim_τ.

**Evaluation.** The master formula (1) involves Σ_X w_τ^X with Σ w = 1 (normalisation). The rep dimension does not enter the band-weighting; it indexes the Lorentz-rep content of the participation-measure module, not the bandwidth-partition pattern. The bandwidth content b_K = |Ψ|² (Case P) or |Ψ̄ΓΨ| (Case R) is **scalar-valued** by construction — the rep dimension has been "consumed" in forming the scalar bilinear (M.1.1 §5.4).

Therefore dim(j_L, j_R) does not appear in σ_τ via (1). The L-R1 lever cannot force any ratio.

**Empirical disconfirmation.** Standard-Model data: spin-1/2 fermions have dim = 4 (Dirac); spin-1 W boson has dim = 4 ((1/2,1/2)); same dimension, vastly different masses. spin-0 Higgs has dim = 1 and m ≈ 125 GeV; spin-1/2 electron has dim = 4 and m ≈ 0.0005 GeV. No dim-mass correlation.

**Verdict R3-A: REFUTED.** σ_τ does not depend on representation dimension structurally.

### 3.2 L-R2 / R3-B — Spin value

**Mechanism candidate.** Spin enters the Lorentz-Casimir labelling via P_μP^μ = m²c² and W² = −m²s(s+1)ℏ². The W² Casimir suggests a possible σ_τ ∝ s(s+1) or σ_τ ∝ s relationship.

**Evaluation.** The Pauli-Lubanski Casimir W² is **proportional** to m² in the form W² = −m²s(s+1)ℏ². This is an identity, not a constraint: given m and s independently, W² is determined; given m alone, s is unconstrained; given s alone, m is unconstrained. There is no structural constraint linking s and m.

Furthermore, σ_τ in (1) does not contain s explicitly. Spin enters σ_τ only via (M.1.1 §5.4) Case-P vs Case-R selection of the relevant bilinear and the chirality / gauge constraint structure. Within a given statistics class, σ_τ is independent of s.

**Empirical disconfirmation.** All charged leptons have s = 1/2 with m_e ≈ 0.5 MeV, m_μ ≈ 106 MeV, m_τ ≈ 1.78 GeV — same spin, mass spread of ~3500×. spin-0 Higgs ≈ 125 GeV; spin-1 W ≈ 80 GeV; spin-1/2 top ≈ 173 GeV — different spins, comparable masses. No s-mass relationship.

**Verdict R3-B: REFUTED.** σ_τ does not depend on spin structurally.

### 3.3 L-R3 / R3-C — Case-P vs Case-R class

**Mechanism candidate.** Different bilinears (|Ψ|² vs |Ψ̄ΓΨ|) might produce systematically different scales.

**Evaluation.** The bilinears differ in **sign structure** (positive-definite for Case P, sign-indefinite for Case R) but not in **magnitude scale**. Both are scalar fields whose log-derivatives are extracted by (1); the scaling is set by chain-specific bandwidth amplitudes, not by the bilinear class.

The L-R3 lever does not produce a magnitude asymmetry.

**Empirical disconfirmation.** Heaviest known fermion (top, Case R) ≈ 173 GeV; heaviest known boson (Higgs, Case P) ≈ 125 GeV; lightest charged fermion (electron, Case R) ≈ 0.5 MeV; massless boson (photon, Case P) = 0. The mass spectrum is interleaved with no clean P-vs-R separation.

**Verdict R3-C: REFUTED.** Statistics class does not order σ_τ.

### 3.4 L-R4 / R3-D — Fierz class

**Mechanism candidate.** Different Γ_τ ∈ {𝟙, γ^μ, σ^{μν}, γ^μγ^5, γ^5} couple to different sectors of the Cl(3,1) algebra. This is the most structurally rich lever — different Fierz channels are genuinely distinct objects, not just labels.

**Evaluation.** From M.1.1 §5.2:
- Γ = 𝟙 → Dirac mass term Ψ̄Ψ; relevant to standard massive fermions.
- Γ = γ^5 → pseudoscalar Ψ̄γ^5Ψ; chirality-flipping; relevant to axion-like or pseudoscalar masses.
- Other Γ → tensorial / vectorial bilinears; not pure rest-frame mass-term-like structure.

The **type** of mass term (Dirac vs Majorana vs pseudoscalar) is determined by Γ_τ. But the **magnitude** σ_τ within any given Γ-class is set by ⟨(∂ ln |Ψ̄Γ_τΨ|)²⟩_τ — which depends on chain-specific bandwidth dynamics, not on Γ_τ itself.

Different Γ_τ produce **structurally different** mass mechanisms (Dirac mass vs Majorana mass have different chirality content), but ED primitives do not fix a numerical ratio between, e.g., a Dirac-class rule-type's σ and a γ^5-class rule-type's σ.

**Partial structural content (CANDIDATE M-Fierz-1):** Within a fixed rule-type, the Γ_τ choice determines whether Ψ̄Ψ vs Ψ^T C Ψ vs Ψ̄γ^5Ψ etc. is the relevant scalar; this is a **type** distinction, not a ratio constraint.

**Verdict R3-D: PARTIALLY SUPPORTED as TYPE classifier; REFUTED as RATIO predictor.** Fierz class distinguishes mass-term structures (Dirac vs Majorana vs pseudoscalar) but does not constrain ratios between massive rule-types of different Fierz classes.

### 3.5 L-R5 / R3-E — Band-weight pattern

**Mechanism candidate.** Different rule-types have different w_τ^X partitions across the four bands {int, adj, env, com}. If w_τ patterns cluster systematically (e.g., quark-like rule-types have w_τ^adj > 0.5, lepton-like have w_τ^adj < 0.1), σ_τ ratios could reflect this.

**Evaluation.** w_τ^X is rule-type data (Lever L1), not primitive-derived. ED primitives admit any (w^int, w^adj, w^env, w^com) with non-negativity and Σ w = 1 (and w^adj > 0 for Case R, M.1.1 §4.1 W3). Within those constraints, no specific pattern is forced.

If empirical data revealed a systematic w-pattern correlating with mass, that would be empirical content, not structural. ED's primitives do not provide the correlation.

**Possible weak structural content (CANDIDATE M-Order-1):** Within a fixed rule-type, increasing w_τ^com at fixed bandwidth amplitude tends to increase commitment-rate spectral content, plausibly increasing σ_τ via (1). But this is "increasing one variable while holding another fixed" — not a ratio constraint between rule-types.

**Possible inequality (CANDIDATE M-Order-2):** A rule-type with w_τ^com = 0 has σ_τ contributions only from non-commitment bands. If commitment-band content is the dominant primitive source of mass-relevant rate variation, this might force σ_τ(w^com=0) < σ_τ(w^com>0) all else equal. Tentative; depends on which band dominates ⟨(∂ ln b^X)²⟩_τ in practice.

**Verdict R3-E: REFUTED as ratio predictor; weak inequality M-Order-2 survives as CANDIDATE.**

### 3.6 L-R6 / R3-F — Adjacency / individuation geometry

**Mechanism candidate.** Primitive 10's individuation threshold sets a spatial scale ℓ_ind which, by Compton-wavelength-like inversion, corresponds to a mass scale m ~ ℏ/(c·ℓ_ind). If different rule-types have different ℓ_ind, a structural ratio could emerge.

**Evaluation.** Primitive 10's individuation threshold is rule-type-specific: it depends on what counts as "same rule-type" for individuation purposes (Case-R restricts coincidence; Case-P permits). The threshold scale ℓ_ind,τ is a candidate primitive-level mass-relevant quantity.

However:
- ℓ_ind,τ is rule-type data, not primitive-derived. Primitive 10 provides the **structure** of individuation (a threshold exists, applied per rule-type) but not the **value** of the threshold per rule-type.
- The Compton-wavelength inversion m ~ ℏ/(c·ℓ_ind) is a dimensional analogy, not a derived identity. The σ_τ formula (1) does not directly contain ℓ_ind.

**Possible structural content (CANDIDATE M-Order-3):** Within a fixed rule-type-class, smaller individuation thresholds correlate with larger mass scales by dimensional analogy. Structurally weak; produces orderings, not ratios.

**Verdict R3-F: REFUTED as ratio predictor; weak inequality M-Order-3 survives as CANDIDATE (dimensional analogy only).**

---

## 4. Summary of strong ratio claims

| Claim | Mechanism | Verdict |
|-------|-----------|---------|
| R3-A | σ_τ ∝ dim(j_L, j_R) | **REFUTED** (rep dim consumed in scalar bilinear; empirical counterexamples) |
| R3-B | σ_τ ∝ s or s(s+1) | **REFUTED** (Casimir is identity not constraint; empirical counterexamples) |
| R3-C | σ_τ ordered by P/R class | **REFUTED** (P/R differs in sign not magnitude; empirical interleaving) |
| R3-D | σ_τ determined by Fierz class | **PARTIALLY SUPPORTED as TYPE classifier; REFUTED as ratio predictor** |
| R3-E | σ_τ determined by w-pattern | **REFUTED as ratio; weak inequality M-Order-2 CANDIDATE** |
| R3-F | σ_τ constrained by ℓ_ind | **REFUTED as ratio; weak inequality M-Order-3 CANDIDATE** |

No strong ratio claim survives. The structural levers that distinguish rule-types in R.2 taxonomy do not, individually or jointly, constrain σ_τ ratios at the equality level.

---

## 5. Surviving structural orderings

Three weak structural orderings survive evaluation as CANDIDATE inequalities:

### 5.1 M-Order-1 (within-rule-type, between bands)

Within a single rule-type, σ_τ depends monotonically on the band-weighted spectral content. This is tautological from (1); not a constraint between rule-types.

### 5.2 M-Order-2 (commitment-active vs commitment-inactive)

If commitment-band content dominates the spectral rate ⟨(∂ ln b^X)²⟩_τ for typical rule-types, then rule-types with w_τ^com = 0 (massless candidates) systematically have σ_τ < σ_τ for rule-types with w_τ^com > 0. This is consistent with massless ↔ no rest-frame commitment (Mλ from M.1.1 §6.2).

**Status:** CANDIDATE inequality, not a ratio. Depends on band-dominance hypothesis (currently untested).

### 5.3 M-Order-3 (Compton-wavelength dimensional analogy)

Dimensional argument: σ_τ ~ ℏ c / ℓ_ind,τ implies σ_τ orderings inversely track ℓ_ind,τ orderings. Heavier rule-types have smaller individuation thresholds.

**Status:** CANDIDATE inequality via dimensional analogy. Not a derivation; the ~ relation is inheritance, not structural.

### 5.4 What the orderings do not give

None of M-Order-1/2/3 produces:
- A specific numerical ratio between any two rule-type signatures.
- A bound on the ratio (e.g., 0.1 ≤ σ_{τ_1}/σ_{τ_2} ≤ 10).
- A derivation of any empirically observed ratio (e.g., m_μ/m_e ≈ 207).

They provide ordering content only, and even that is conditional on rule-type-data inputs not being primitive-derived.

---

## 6. Why ED structurally cannot predict ratios

### 6.1 Structural argument

The σ_τ master formula (1) factors into:

  σ_τ² / ℏ² = Σ_X w_τ^X · ⟨(∂ ln b^X)²⟩_τ.

Both factors per rule-type — the band weights w_τ^X and the spectral rates ⟨(∂ ln b^X)²⟩_τ — are rule-type data and chain-initial-condition data respectively. Neither is primitive-derived.

For ED to constrain σ_τ ratios structurally, it would need to constrain at least one of:
- (a) Cross-rule-type relationships among {w_τ^X}_τ,
- (b) Cross-rule-type relationships among {⟨(∂ ln b^X)²⟩_τ}_τ,
- (c) Cross-rule-type relationships among the chain-initial bandwidth content.

No such relationships exist at primitive level. The R.2 taxonomy provides classification (sorting rule-types into Case P/R, spin classes, Fierz classes) but does not constrain numerical content within or across classes.

### 6.2 Comparison to R.2 closure

R.2.5 closed with the spin-statistics theorem η = (−1)^{2s} as a primitive-FORCED equality. That theorem worked because the **dichotomies** (η = ±1, integer/half-integer s) are primitive-level structural classifications, and the equality ties them.

Mass ratios are different: they are continuous numerical quantities, not dichotomies. ED's primitive structure produces classifications and dichotomies cleanly, but does not produce continuous numerical relationships. Mass ratios are inherently in the latter category.

This is not a flaw of the R.2.5 / M.1.x analysis; it is an honest accounting of what kind of content ED primitives carry.

### 6.3 What this means for empirical comparisons

- **Koide-relation-style formulae** (m_e + m_μ + m_τ relationships): not derivable from ED primitives at this stage.
- **Mass hierarchies** (m_t ≫ m_b ≫ m_c …): not derivable.
- **Generation-count predictions** (3 generations): not derivable from R.2 + M.0 + M.1.x content.
- **Quark-lepton mass relationships** (m_d/m_e ratios etc.): not derivable.

These are Arc Q + empirical territory, possibly never structurally derivable.

---

## 7. FORCED / CANDIDATE / REFUTED / SPECULATIVE

### 7.1 FORCED

- **F1.** σ_τ ratios depend on rule-type data (w_τ^X, ⟨(∂ ln b^X)²⟩_τ), not on primitive-level structural classifications. (§6.1)
- **F2.** Representation dimension does not enter σ_τ structurally. (§3.1)
- **F3.** Spin does not enter σ_τ structurally beyond Case-P / Case-R selection. (§3.2)
- **F4.** Statistics class does not order σ_τ magnitudes. (§3.3)
- **F5.** Fierz class distinguishes mass-term structures (Dirac vs Majorana vs pseudoscalar) but does not constrain ratios. (§3.4)
- **F6.** No equality constraint on σ_{τ_1}/σ_{τ_2} from primitives + R.2 taxonomy. (§4–§6)

### 7.2 CANDIDATE

- **M-Order-2.** Rule-types with w_τ^com = 0 have systematically smaller σ_τ than those with w_τ^com > 0 (commitment-band-dominance hypothesis). Inequality, not ratio. (§5.2)
- **M-Order-3.** σ_τ orderings inversely track individuation-threshold orderings via Compton-wavelength dimensional analogy. Inequality, not ratio. (§5.3)
- **M-Fierz-1.** Fierz class determines mass-term **type** (Dirac / Majorana / pseudoscalar), not ratio. Type classification only. (§3.4)

### 7.3 REFUTED

- **R3-A.** σ_τ ∝ dim(j_L, j_R). (§3.1)
- **R3-B.** σ_τ ∝ s or s(s+1). (§3.2)
- **R3-C.** σ_τ ordered by Case-P / Case-R. (§3.3)
- **R3-D as ratio predictor.** (§3.4)
- **R3-E as ratio predictor.** (§3.5)
- **R3-F as ratio predictor.** (§3.6)

### 7.4 SPECULATIVE

- **S1.** ED primitives **could** be extended to constrain mass ratios via additional structural content not currently articulated (e.g., a generation lever beyond L1–L4). No mechanism in hand.
- **S2.** Mass ratios might be derivable from boundary conditions on bandwidth fields at Arc Q + cosmological scales. Pure speculation.
- **S3.** A modified σ_τ functional (alternative to M.1.1's master formula) might carry ratio content. Would require revising M.1.1's selection criteria.
- **S4.** Generation count (3) reflects a hidden discrete primitive structure. Pure speculation.

---

## 8. Verdict

### 8.1 Does ED structurally constrain mass ratios?

**No** — at the level of equality constraints. σ_{τ_1}/σ_{τ_2} is unconstrained by ED primitives + R.2 taxonomy.

### 8.2 What constraints survive?

Three weak inequality / ordering candidates (M-Order-2, M-Order-3, M-Fierz-1), all CANDIDATE not FORCED, all producing orderings or type distinctions rather than numerical ratios.

### 8.3 What is the implication for Hypothesis H3?

Hypothesis H3 from `chain_mass_scoping.md` (mass ratios constrained by taxonomy) is **substantially refuted**. The strong-form claims (R3-A through R3-F) are systematically refuted. The weak-form claims (orderings/inequalities) survive as CANDIDATE only.

The Stage M.0 prior plausibility for H3 was "low-moderate." Stage M.1.3 reduces this to: **H3 in equality form is rejected; H3 in inequality form survives only as CANDIDATE pending validation of M-Order-2/3.**

### 8.4 Implications for Arc M closure

Combined with M.1.2 (massless rule-types: existence of slot FORCED conditional on GRH; identification of occupants NOT FORCED), Arc M is shaping toward a closure dominated by **negative results** in the strong sense:

- **Mass values:** inherited (M.1.1's σ_τ depends on chain-initial-condition data).
- **Mass ratios:** unconstrained at equality level (M.1.3, this memo).
- **Massless slot:** existence FORCED conditional on GRH; identification not (M.1.2).
- **Mass type (Dirac/Majorana/pseudoscalar):** classification by Fierz structure FORCED; values within classes not.

Arc M's structural prediction is thus quite limited: it sorts mass content into types and provides existence claims for the massless slot, but does not predict numerical mass values or ratios. This matches the Stage M.0 honest expected verdict distribution (~50% mixed, ~30% H1-dominant); current trend lands closer to H1-dominant.

---

## 9. Hand-off

### 9.1 To Stage M.1.4 (contingent)

`mass_signature_identity.md` would evaluate the m_τ = σ_τ / c² identity. Given M.1.1's construction is provisional and M.1.3 establishes that ratios are unconstrained, the identity (if it holds) would be a per-rule-type statement, not a comparative predictive tool. Stage M.1.4 may be optional rather than required; assess after Stage M.2 synthesis.

### 9.2 To Stage M.2

`chain_mass_synthesis.md` will integrate M.1.1, M.1.2, M.1.3 and deliver the final Arc M verdict. Expected closure: mostly H1-dominant with structural type-classification and conditional massless-slot existence.

### 9.3 To Arc Q

Mass ratios, hierarchies, generations, Yukawa structure, and Higgs mechanism are all explicitly Arc Q + empirical content. Arc M's job is to demarcate this clearly, which Stage M.1.3 does.

---

## 10. Cross-references

- Upstream: `bandwidth_signature_construction.md` (M.1.1), `massless_rule_types.md` (M.1.2), `chain_mass_scoping.md` (M.0), `rule_type_taxonomy_synthesis.md` (R.2.5).
- Phase-1 mass: `u3_evolution_derivation.md`.
- Downstream: `mass_signature_identity.md` (M.1.4 contingent), `chain_mass_synthesis.md` (M.2).

---

## 11. One-line summary

**Stage M.1.3 evaluates Hypothesis H3 (taxonomy-constrained mass ratios) systematically across six structural levers (representation dimension, spin, statistics class, Fierz class, band-weight pattern, individuation geometry) and finds that ED primitives + R.2 taxonomy produce no equality constraints on σ_{τ_1}/σ_{τ_2} for massive rule-types; six strong ratio claims (R3-A through R3-F) are REFUTED; three weak inequality candidates (M-Order-2, M-Order-3, M-Fierz-1) survive only as CANDIDATE producing orderings or type-classifications, not numerical ratios — H3 in equality form is rejected, Arc M's emerging closure is H1-dominant.**
