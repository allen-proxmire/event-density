# Chain-Mass Synthesis — Arc M Closure

**Stage M.2 — Arc M Synthesis and Closure Memo**
**Status:** Closure memo. Final verdict: ED fixes the **structure** of mass (Lorentz-scalar form, dimensional anchoring, statistics-class-determined mechanism, Fierz-class-determined type, conditional existence of a massless slot) but does **not** fix mass **values**, **ratios**, **hierarchies**, or **occupancy** of the massless slot. Arc M closes H1-dominant: most numerical mass content is inherited, with structural constraints limited to type classification and conditional existence claims. Optional Stage M.1.4 deemed not necessary; Arc M closes without it.

---

## 1. Purpose

Arc M opened with `chain_mass_scoping.md` (M.0) identifying three candidate mass-origin hypotheses:

- **H1** (mass fully inherited): high prior plausibility.
- **H2** (mass = bandwidth signature, m_τ = σ_τ/c²): moderate prior.
- **H3** (mass ratios constrained by taxonomy): low-moderate prior.

Three sub-memos then evaluated the structural content available:

- **M.1.1** (`bandwidth_signature_construction.md`): constructed the candidate σ_τ as a Lorentz-scalar functional of the four-band content; FORCED form, CANDIDATE specifics, INHERITED values.
- **M.1.2** (`massless_rule_types.md`): two structurally-admissible massless mechanisms (MR-R chiral, MR-P gauge); existence of a massless slot FORCED conditional on the gauge-field-as-rule-type hypothesis (GRH); identification of occupants NOT FORCED.
- **M.1.3** (`mass_ratio_constraints.md`): six strong ratio claims R3-A through R3-F systematically REFUTED; H3 in equality form rejected; three weak inequality candidates (M-Order-2, M-Order-3, M-Fierz-1) survive only as CANDIDATE.

Stage M.2 integrates these into a single closure verdict, records the final FORCED/REFUTED/CANDIDATE/INHERITED/SPECULATIVE separation, fixes the dependency structure for downstream arcs, and marks Arc M as closed.

---

## 2. Verdict on the three hypotheses

### 2.1 H1 (mass fully inherited)

**Status: substantially supported.** Arc M's structural analysis confirms that:

- The numerical value of σ_τ (and hence m_τ under the σ_τ/c² identity) for any specific rule-type depends on chain-initial-condition data via the spectral-rate average ⟨(∂ ln b^X)²⟩_τ (M.1.1).
- ED primitives + R.2 taxonomy do not constrain σ_τ ratios (M.1.3).
- ED primitives do not identify which rule-types occupy the massless slot (M.1.2).

H1 is the **dominant** outcome. Arc M does not refute it; it constrains it only at the level of structure (form, type, statistics-class mechanism), not at the level of values.

### 2.2 H2 (m_τ = σ_τ/c²)

**Status: provisional CANDIDATE.** σ_τ is constructed in M.1.1 with the right form to play this role, but:

- The specific functional choice (logarithmic-derivative spectral rate) is CANDIDATE not FORCED.
- Promotion of m_τ = σ_τ/c² to FORCED would require deriving the identity from primitives, which has not been achieved in Arc M.
- M.1.4 (`mass_signature_identity.md`) was envisioned to attempt this derivation; M.1.3's negative result on ratios makes the per-rule-type identity less informative — even if it holds, it carries no comparative predictive power.

**Decision (this memo):** Stage M.1.4 is **optional and deferred**. The σ_τ/c² identity remains CANDIDATE, attached to the σ_τ construction but not promoted to FORCED. Future work may revisit if a sharper σ_τ construction is found.

### 2.3 H3 (mass ratios constrained by taxonomy)

**Status: substantially refuted.** Stage M.1.3 systematically refuted the six strong-form ratio claims (R3-A through R3-F). Three weak ordering candidates (M-Order-2, M-Order-3, M-Fierz-1) survive but:

- They produce **inequalities or type classifications**, not numerical ratios.
- They are CANDIDATE, not FORCED.
- They depend on auxiliary hypotheses (commitment-band-dominance, Compton-wavelength dimensional analogy) that are not themselves derived from primitives.

H3 in equality form is rejected. H3 in inequality form survives as weak CANDIDATE. ED does not predict mass hierarchies, generation counts, or specific empirical ratios.

### 2.4 Match to M.0 expected verdict distribution

The M.0 honest prior was: ~50% mixed / ~30% H1-dominant / ~15% H2 partial / ~5% H3-surprise.

Arc M closes closer to **H1-dominant with H2 partial flavour and H3 refuted**. This sits between the "mixed" and "H1-dominant" scenarios — slightly more skeptical than the M.0 prior median. The closure is consistent with M.0's honest framing that primitive inputs may be too thin to force much.

---

## 3. What Arc M has FORCED

The structural achievements of Arc M, all FORCED at primitive level:

### 3.1 Existence of σ_τ as a structural invariant (from M.1.1)

- **F-M1.** A Lorentz-scalar bandwidth-signature functional σ_τ exists and is constructible from Primitive 04 (four-band content) and Primitive 07 (rule-type structure).
- **F-M2.** σ_τ has units of energy via ℏ × frequency.
- **F-M3.** σ_τ is independent of overall bandwidth amplitude (logarithmic-derivative form).
- **F-M4.** σ_τ admits Case-P and Case-R variants distinguished by which scalar bilinear (|Ψ|² vs |Ψ̄ΓΨ|) carries the mass content.

### 3.2 Structural admissibility of masslessness (from M.1.2)

- **F-M5.** σ_τ = 0 is a structurally accessible solution of the σ_τ master formula.
- **F-M6.** Two distinct primitive-level massless mechanisms exist: MR-R (chiral, Case R) and MR-P (gauge, Case P).
- **F-M7.** MR-R and MR-P are mutually exclusive per rule-type and tentatively exhaustive in 3+1D.
- **F-M8.** Existence of at least one massless Case-P rule-type is FORCED conditional on the gauge-field-as-rule-type hypothesis (GRH). [F-M8 promotes to unconditional FORCED upon GRH closure at Arc Q.]

### 3.3 Mass-term type classification (from M.1.3)

- **F-M9.** Fierz class Γ_τ ∈ {𝟙, γ^μ, σ^{μν}, γ^μγ^5, γ^5} structurally distinguishes mass-term TYPES: Dirac mass (Γ = 𝟙), Majorana mass (charge-conjugation bilinear), pseudoscalar mass (Γ = γ^5), tensor / vector bilinears (non-mass-like).
- **F-M10.** Statistics class (Case P / Case R) determines which massless mechanism applies (MR-P / MR-R respectively), if the rule-type is massless.

### 3.4 Form-fixing of dynamical equations

- **F-M11.** The mass term in Klein-Gordon and Dirac equations (Stage R.1, R.3) is FORCED at the **form** level: m²c²/ℏ² in KG, mc/ℏ in Dirac. Numerical m is rule-type data.

---

## 4. What Arc M has REFUTED

The structural negative results of Arc M, FORCED at primitive level:

### 4.1 Strong ratio claims (from M.1.3)

- **R-M1.** σ_τ ∝ representation dimension dim(j_L, j_R) — REFUTED.
- **R-M2.** σ_τ ∝ spin s or s(s+1) — REFUTED.
- **R-M3.** σ_τ ordered by Case-P / Case-R class — REFUTED.
- **R-M4.** σ_τ determined by Fierz class as a ratio — REFUTED.
- **R-M5.** σ_τ determined by band-weight pattern as a ratio — REFUTED.
- **R-M6.** σ_τ constrained by individuation geometry as a ratio — REFUTED.

### 4.2 Identification claims (from M.1.2)

- **R-M7.** No specific ED rule-type is structurally forced to be massless on the basis of Primitives 02, 04, 06, 07, 10, 11, 13 alone (without GRH).
- **R-M8.** ED does not pick MR-R over MR-P (or vice versa) as the canonical massless route.
- **R-M9.** ED does not predict the count of massless rule-types.

### 4.3 Hierarchy claims

- **R-M10.** No structural mass-hierarchy mechanism in Arc M. Mass orderings (m_t ≫ m_b ≫ m_c, etc.) are not derivable.
- **R-M11.** No generation-count derivation. Three generations is not forced by Arc M.
- **R-M12.** No primitive-level Higgs analogue identified in Arc M.

---

## 5. What remains CANDIDATE

CANDIDATE items survive Arc M closure either because they are structurally plausible but not yet forced, or because their evaluation requires Arc Q content:

### 5.1 σ_τ functional specifics

- **C-M1.** Specific form of σ_τ as logarithmic-derivative spectral-rate (M.1.1's master formula M). Selection criteria SC1–SC6 motivate but do not uniquely force.
- **C-M2.** Hypothesis Mλ: σ_τ = 0 ⟺ no rest-frame commitment AND no rest-frame internal evolution. Equivalent to "MR-R or MR-P".
- **C-M3.** Refined Case-R formula via |Ψ̄Γ_τΨ|. Specific Γ_τ assignment is rule-type data.

### 5.2 GRH (gauge-field-as-rule-type)

- **C-M4.** GRH: minimal-coupling A_μ is the participation measure of a Case-P (1/2,1/2) rule-type with gauge-invariant L3 interface. Closes at Arc Q.

### 5.3 Mass-signature identity

- **C-M5.** m_τ = σ_τ/c² as a structural identity. Optional Stage M.1.4 deferred; not promoted to FORCED in Arc M.

### 5.4 Weak orderings

- **C-M6.** M-Order-2: rule-types with w_τ^com = 0 have systematically smaller σ_τ. Inequality, conditional on commitment-band-dominance.
- **C-M7.** M-Order-3: σ_τ ordering inversely tracks ℓ_ind,τ via Compton-wavelength dimensional analogy. Inequality, dimensional only.
- **C-M8.** M-Fierz-1: Fierz class determines mass-term TYPE. Type classification, not ratio.

### 5.5 Massless mechanism exhaustiveness

- **C-M9.** {MR-R, MR-P} are exhaustive primitive-level massless mechanisms in 3+1D. Closure plausible but not proven.

---

## 6. What is INHERITED

Arc M explicitly demarcates the inherited content:

- **I-M1.** Numerical values of m_τ for any specific rule-type. Inherited per-rule-type.
- **I-M2.** Band-weight values w_τ^X for any specific rule-type. Inherited (Lever L1 data).
- **I-M3.** Fierz-class assignment Γ_τ for Case-R rule-types. Inherited (Lever L3 data).
- **I-M4.** Spectral-rate values ⟨(∂ ln b^X)²⟩_τ. Inherited from chain-initial bandwidth data.
- **I-M5.** Numerical values of ℏ, c (Dimensional Atlas / Stage R.1 metric normalisation).
- **I-M6.** Charge q per rule-type. Inherited.
- **I-M7.** Empirical identification of rule-types with Standard-Model species. Empirical / Arc Q.
- **I-M8.** Mass ratios m_{τ_1}/m_{τ_2}. Inherited (M.1.3 refutes structural derivability).
- **I-M9.** Generation count. Inherited (no structural mechanism in Arc M).

---

## 7. What remains SPECULATIVE

Items that are not FORCED, not CANDIDATE in any concrete sense, and not refuted — purely speculative possibilities open to future investigation:

- **S-M1.** Generation count (3) has a hidden primitive-level origin (e.g., a structural lever beyond L1–L4).
- **S-M2.** Fermion mass hierarchy is structurally derivable from a yet-unidentified mechanism.
- **S-M3.** Higgs mechanism has an ED-primitive analogue (Arc Q to evaluate).
- **S-M4.** Neutrino mass smallness reflects a near-MR-R structure (small Majorana sector dominating).
- **S-M5.** A modified σ_τ functional (alternative to M.1.1's master formula) carries ratio content. Would require revising M.1.1 selection criteria.
- **S-M6.** Mass ratios derivable from boundary conditions on bandwidth fields at cosmological scales.
- **S-M7.** Graviton-like rule-type exists and is massless in extended ED structure.
- **S-M8.** Supersymmetric pairing structure relates Case-P and Case-R rule-type masses.

These are speculative but listed honestly; future arcs may discharge or refute any of them.

---

## 8. Final classification table

| Category    | Item                                                                                  | Source       |
|-------------|---------------------------------------------------------------------------------------|--------------|
| **FORCED**  | F-M1: σ_τ exists as Lorentz-scalar invariant                                          | M.1.1        |
|             | F-M2: σ_τ has energy units                                                            | M.1.1        |
|             | F-M3: σ_τ is amplitude-invariant                                                      | M.1.1        |
|             | F-M4: Case-P / Case-R bilinear distinction                                            | M.1.1        |
|             | F-M5: σ_τ = 0 is structurally accessible                                              | M.1.2        |
|             | F-M6: MR-R and MR-P are admissible massless mechanisms                                | M.1.2        |
|             | F-M7: MR-R / MR-P are mutually exclusive per rule-type                                | M.1.2        |
|             | F-M8: Massless Case-P rule-type FORCED conditional on GRH                             | M.1.2        |
|             | F-M9: Fierz class fixes mass-term TYPE                                                | M.1.3        |
|             | F-M10: Statistics class determines massless mechanism                                 | M.1.3        |
|             | F-M11: Form of m-term in KG / Dirac                                                   | R.1, R.3     |
| **REFUTED** | R-M1 to R-M6: strong ratio claims R3-A through R3-F                                   | M.1.3        |
|             | R-M7: no specific rule-type forced massless without GRH                               | M.1.2        |
|             | R-M8: no canonical choice between MR-R and MR-P                                       | M.1.2        |
|             | R-M9: no structural prediction of massless count                                      | M.1.2        |
|             | R-M10: no mass hierarchy mechanism                                                    | M.1.3        |
|             | R-M11: no generation-count derivation                                                 | M.1.3        |
|             | R-M12: no primitive Higgs analogue in Arc M                                           | M.1.3        |
| **CANDIDATE** | C-M1: specific σ_τ functional form                                                  | M.1.1        |
|             | C-M2: hypothesis Mλ                                                                  | M.1.1        |
|             | C-M3: Case-R |Ψ̄Γ_τΨ| refinement                                                      | M.1.1        |
|             | C-M4: GRH                                                                            | M.1.2        |
|             | C-M5: m_τ = σ_τ/c² identity                                                          | M.1.1, M.2   |
|             | C-M6: M-Order-2 (commitment-band-dominance)                                          | M.1.3        |
|             | C-M7: M-Order-3 (Compton-wavelength dimensional analogy)                             | M.1.3        |
|             | C-M8: M-Fierz-1 (Fierz class as TYPE classifier)                                     | M.1.3        |
|             | C-M9: exhaustiveness of {MR-R, MR-P}                                                 | M.1.2        |
| **INHERITED** | I-M1: numerical m_τ values                                                          | all          |
|             | I-M2: w_τ^X values                                                                   | M.1.1, M.1.3 |
|             | I-M3: Γ_τ assignment                                                                 | M.1.1, M.1.3 |
|             | I-M4: ⟨(∂ ln b^X)²⟩_τ values                                                         | M.1.1        |
|             | I-M5: ℏ, c numerical values                                                          | R.1, R.3     |
|             | I-M6: charge q                                                                        | R.1          |
|             | I-M7: rule-type ↔ SM-species map                                                     | Arc Q        |
|             | I-M8: mass ratios                                                                    | M.1.3        |
|             | I-M9: generation count                                                                | empirical    |
| **SPECULATIVE** | S-M1 to S-M8: various open possibilities                                          | M.2          |

---

## 9. Dependency diagram

```
                    Stage R.2 (rule-type taxonomy, closed)
                                       │
                                       ▼
                    Stage R.3 (Dirac emergence, closed)
                                       │
                                       ▼
                    Arc M Stage M.0 (scoping, closed)
                                       │
                                       ▼
        Arc M Stage M.1.x (structural evaluations)
          ├── M.1.1 (σ_τ construction, closed)
          ├── M.1.2 (massless rule-types, closed)
          └── M.1.3 (mass-ratio refutation, closed)
                                       │
                                       ▼
                Arc M Stage M.2 (synthesis — this memo)
                                       │
                                       ▼
                            Arc M closed (H1-dominant)
                                       │
                                       ▼
                       Arc Q (QFT extension)
          ├── GRH closure → F-M8 unconditional FORCED
          ├── Yukawa / Higgs / radiative corrections (inherited content)
          ├── Gauge-group specification (rule-type data)
          └── Multi-generation structure (Arc Q + empirical)
```

### 9.1 Arc M unblocks

- **Arc Q (QFT):** Inherits Arc M's clean separation between structural form and inherited values. Arc Q can use Arc M's σ_τ form, Fierz-class type classification, and conditional massless-slot existence as structural inputs without re-deriving them.

### 9.2 Arc M does not unblock (recorded honestly)

- **Numerical mass predictions:** Arc M provides no mechanism. Arc Q + empirical fits.
- **Mass hierarchy / generation count:** No mechanism in Arc M. Possibly Arc Q + cosmological boundary conditions; possibly intrinsically empirical.

---

## 10. Stage M.2 closure statement

### 10.1 Arc M is structurally closed

All four Arc M sub-memos (M.0, M.1.1, M.1.2, M.1.3) are written and closed. Stage M.1.4 is **declined** (deferred indefinitely): given M.1.3's refutation of ratio constraints, the per-rule-type m_τ = σ_τ/c² identity carries no comparative predictive power, and Arc M closes cleanly without it.

The closure verdict is **H1-dominant with structural type/form constraints**:

- ED fixes the **form** of mass terms (Lorentz-scalar Casimir, KG/Dirac mass-term shape).
- ED fixes the **type** classification of mass terms (Dirac / Majorana / pseudoscalar via Fierz class).
- ED fixes the **mechanism** for masslessness (chirality for Case R, gauge for Case P).
- ED forces the **existence** of a massless slot conditional on GRH.
- ED does **not** fix mass values, ratios, hierarchies, generations, or massless-occupancy.

### 10.2 Comparison with R.2 closure

R.2 closed with the spin-statistics theorem η = (−1)^{2s} as a primitive-FORCED structural equality — a strong positive-content closure. Arc M closes with mostly negative or conditional results — a structurally-honest H1-dominant closure.

The asymmetry is genuine and informative: ED's primitive structure produces classifications, dichotomies, and structural type-content cleanly (the strength of R.2), but does not produce continuous numerical relationships (the limit demonstrated by Arc M). This is not a defect; it is a clear-eyed map of what ED's primitive stack can and cannot deliver.

### 10.3 What this means for the broader QM-emergence program

Combined Phase-1 + Phase-2 (Arc R + Arc M) closure establishes:

- **FORCED:** Form of QM equations (Schrödinger, KG, Dirac, Pauli), spin-statistics, gauge-covariant minimal coupling, conserved currents, structural taxonomy of rule-types, Cl(3,1) frame, mass-term type classification.
- **INHERITED:** ℏ, c, m, q, gauge-group choice, rule-type ↔ species assignments, mass values, mass ratios.
- **DEFERRED:** Arc Q (QFT, gauge-group structure, Higgs, radiative corrections), Arc N (non-Markovian platform-specific), generations, neutrino-mass details.

ED derives the **structural skeleton** of relativistic quantum theory cleanly. It does not derive its **numerical flesh**. This is the honest closure of the QM-emergence program through Arc M.

---

## 11. Hand-off

### 11.1 To Arc Q (next major arc)

Arc Q opens with:
- GRH closure as its first deliverable (promotes F-M8 to unconditional FORCED).
- Gauge-group specification (SU(3)×SU(2)×U(1) as empirical / rule-type-data input).
- Spontaneous symmetry breaking / Higgs mechanism evaluation (S-M3).
- Yukawa / radiative-correction / multi-generation structure.

Arc Q inherits Arc M's clean structure-vs-value separation as a working principle.

### 11.2 To Arc N (independent thread)

Arc N (non-Markovian memory kernel) is independent of Arc M at primitive level. It uses inherited masses directly via Stage R.1 / R.3 mass terms; no Arc M closure required.

### 11.3 To memory and orientation

Memory updates queued (now substantially overdue):
- `MEMORY.md` → `project_qm_emergence_arc.md` update: Arc M closed H1-dominant; Arc Q and Arc N now the active threads.
- New entry: `project_arc_m.md` (or merge into existing arc-tracking memory).
- `docs/ED-Orientation.md` → add Arc M closure entry.
- `docs/ED_Accomplishments.md` → new "Arc M (Chain-Mass)" subsection under "QM-Emergence Program".

---

## 12. Cross-references

- Arc M memos: `chain_mass_scoping.md` (M.0), `bandwidth_signature_construction.md` (M.1.1), `massless_rule_types.md` (M.1.2), `mass_ratio_constraints.md` (M.1.3), `chain_mass_synthesis.md` (this memo, M.2).
- Upstream closures: `arc_r_stage1_synthesis.md` (R.1), `rule_type_taxonomy_synthesis.md` (R.2.5), `dirac_emergence.md` (R.3).
- Phase-1 anchor: `qm_emergence_closure.md`, `u3_evolution_derivation.md`.
- Downstream placeholders: Arc Q scoping (forthcoming).

---

## 13. One-line summary

**Arc M shows that ED fixes the *structure* of mass but not its *values*: σ_τ exists as a Lorentz-scalar invariant with statistics-class-determined massless mechanism and Fierz-class-determined type, but mass values, ratios, hierarchies, generations, and massless-slot occupancy are inherited or deferred to Arc Q — a clean, honest, H1-dominant closure of Arc M.**
