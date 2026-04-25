# Phase-2 Extensions Roadmap

**Date:** 2026-04-24
**Location:** `quantum/foundations/phase2_extensions_roadmap.md`
**Status:** Planning document. Defines the research arcs that extend ED beyond the completed Phase-1 scope (non-relativistic single-particle QM + Lindblad open-system dynamics). Establishes dependencies, milestones, and expected deliverables for each arc.
**Purpose:** Provide a master reference for future work following the Phase-1 structural closure. Not itself a derivation; sets the scope and sequence for derivations that follow.

---

## 1. Overview

### 1.1 Phase 1 status

Phase 1 of the QM-emergence program is structurally complete as of 2026-04-24. Its content consists of:

- **Primitive stack** (Primitives 01–13) — the ontological basis.
- **Five-step QM-emergence chain** — Schrödinger, Born, Bell/Tsirelson, Heisenberg, all FORCED at the structural level.
- **Tightening program** — U1, U2, U5, and Step-3 phase-independence FORCED; U3 FORCED modulo inherited ℏ; U4 structurally FORCED with chain-mass SPECULATIVE.
- **Lindblad extension** — the open-system master equation FORCED from primitives; extends U3 beyond the isolated-chain thin-participation limit.
- **Platform-bridge infrastructure** — matter-wave, BEC, SC-qubit, and optomechanical scaffolds, with the BEC bridge completed as the first Phase-2-type platform-bridge derivation.

**What is covered in Phase 1:** closed-system and open-system non-relativistic single-particle quantum mechanics. The form of the Schrödinger equation, the Lindblad master equation, the Born rule, Bell/Tsirelson correlations, and Heisenberg uncertainty relations are all derived as structural consequences of the participation-measure framework. The numerical values of ℏ and m are inherited via the ED Dimensional Atlas.

**What Phase 1 does not cover:** relativistic effects (Klein-Gordon, Dirac), multi-particle / quantum-field-theoretic content (field operators, particle creation/annihilation, second quantization), the primitive-level origin of particle masses (chain-mass derivation), and non-Markovian memory effects (corrections to Lindblad).

### 1.2 Phase 2 purpose

**Phase 2 extends the ED QM-emergence framework to the four regimes not covered by Phase 1.** Each extension target is a structural-content addition: a new form of equation, a new class of predictions, or a primitive-level derivation of a previously-inherited constant.

Phase 2 is not empirically-distinguishing work (that remains the Phase-3 retrodiction program). Phase 2 is structural: it aims to derive, from ED primitives, the form of equations that QM uses in regimes Phase 1 did not cover.

---

## 2. The four major arcs

### 2.1 Arc R — Relativistic Extension

**Goal.** Derive the Klein-Gordon equation (scalar relativistic wave equation) and the Dirac equation (spinor relativistic wave equation) as thin-participation limits of a Lorentz-covariant participation measure.

**Target equations.**
- Klein-Gordon: `(∂_μ ∂^μ + m²c²/ℏ²) φ = 0`
- Dirac: `(iγ^μ ∂_μ − mc/ℏ) ψ = 0`

**Key structural commitments to derive.**
- Lorentz-covariant form of the participation measure P_K(x^μ) on four-dimensional spacetime events.
- Covariant four-band decomposition (Primitive 04 extended to Lorentz-indexed bands).
- Relativistic dispersion `E² = p²c² + m²c⁴` forced by Poincaré invariance + analyticity at $p^μ = 0$.
- Spinor structure of the participation measure for fermionic chains (requires extending Primitive 07 rule-type classification).
- Klein-Gordon: second-order covariant wave equation from scalar participation measure.
- Dirac: first-order covariant wave equation from spinor participation measure; γ-matrix algebra from Clifford structure on the participation graph.

**Primitives involved.**
- Primitive 02 (chain identity) extended to Lorentz-covariant worldlines.
- Primitive 04 (four-band decomposition) extended to include time-like and space-like bands.
- Primitive 06 (ED gradient) extended to four-gradient ∂_μ.
- Primitive 13 (relational timing) reinterpreted in a Lorentz-invariant framework.
- Primitive 07 (channel) extended for spinor rule-types.

**Inherited content.**
- Speed of light c (empirically anchored; Dimensional Atlas relativistic regime).
- Particle mass m (inherited at the species level, as in Phase 1).

**Difficulty.** Medium-high. The Klein-Gordon derivation is analogous to Phase 1's Schrödinger derivation with non-relativistic dispersion replaced by relativistic. The Dirac derivation is harder because it requires deriving spinor structure from primitives, which connects to the rule-type taxonomy (Primitive 07 §7.4, currently open).

**Expected memos.**
- `relativistic_participation_measure.md` — Lorentz-covariant P_K(x^μ).
- `klein_gordon_emergence.md` — Klein-Gordon as scalar-case thin-limit.
- `dirac_emergence.md` — Dirac as spinor-case thin-limit (contingent on rule-type taxonomy progress).

**Scope estimate.** Multi-session; approximately 4–6 memos including foundations.

### 2.2 Arc Q — QFT Extension

**Goal.** Extend the participation-measure framework to multi-chain / multi-particle systems, deriving the creation/annihilation operator structure, the vacuum state, and the field-operator formalism as primitive-level consequences.

**Target equations.**
- Field expansion: `φ̂(x) = Σ_k (a_k e^{ikx} + a_k† e^{-ikx}) / √(2ω_k)`
- Canonical commutation: `[a_k, a_k'†] = δ(k − k')`
- Vacuum: `a_k |0⟩ = 0`

**Key structural commitments to derive.**
- Multi-chain joint participation measure `P^{(N)}_{K_1, …, K_N}(x_1, …, x_N, t)` for N-chain ensembles.
- Vacuum state as the maximally-sparse participation configuration (no chains active).
- Creation operator as the primitive-level operation of adding a chain to an existing configuration.
- Annihilation operator as the inverse (chain removal, committed to environmental absorption).
- Canonical commutation relations derived from the algebra of creation/annihilation acting on multi-chain participation measures.
- Bosonic vs fermionic statistics from symmetrization/antisymmetrization of joint participation under chain-exchange; ties to the rule-type taxonomy (Primitive 07).
- Field operators as the continuum limit of creation/annihilation acting on a participation-graph location.

**Primitives involved.**
- Primitive 03 (participation) extended for multi-endpoint shared structure.
- Primitive 07 (channel) with extended rule-type classification (bosonic vs fermionic).
- Primitive 10 (individuation) at the multi-chain level (identical particles, exchange symmetry).
- Primitive 11 (commitment) for creation/annihilation as commit-event types.

**Inherited content.**
- Particle species content (electron, photon, quarks, etc.) — inherited until the chain-mass program closes.

**Dependencies.**
- Likely requires Arc R (relativistic extension) as groundwork, since standard QFT is Lorentz-covariant.
- Intertwined with Arc M (chain-mass derivation) for species content.

**Difficulty.** Multi-year research program. This is arguably the largest Phase-2 extension.

**Expected memos.**
- `qft_participation_measure.md` — multi-chain joint structure.
- `creation_annihilation.md` — operator structure from chain-add / chain-remove primitives.
- `vacuum_state_derivation.md` — maximally-sparse participation.
- `exchange_statistics.md` — bosons vs fermions from primitive-level symmetry.
- `field_operator_continuum_limit.md` — continuum field emergence.
- `standard_model_emergence_scoping.md` — path toward Standard-Model content.

**Scope estimate.** Multi-year; approximately 10–15 memos over the arc.

### 2.3 Arc M — Chain-Mass Derivation

**Goal.** Derive the numerical values of elementary-particle rest masses from ED primitive-level structure. Close the sole SPECULATIVE item in Phase 1's U4 derivation.

**Target result.**
- First-principles derivation of `m_τ` (mass of chain rule-type τ) from a primitive-level quantity σ_τ (rule-type bandwidth signature) via the Einstein relation `m_τ = σ_τ / c²`.
- Explanation of specific mass ratios in the observed spectrum (e.g., `m_p / m_e ≈ 1836`).
- Eventual connection to the Higgs mechanism, which in the Standard Model generates particle masses via electroweak-symmetry-breaking.

**Key structural commitments to derive.**
- Rule-type taxonomy from primitives (Primitive 07 §7.4 is flagged as open). This is the central prerequisite; without a primitive-level classification of rule-types, the mass derivation has no structural basis.
- Rule-bandwidth signature σ_τ as a primitive-level structural quantity for each rule-type.
- Mass anchoring `m_τ = σ_τ / c²` with c from the Dimensional Atlas.
- Mass ratios (m_p/m_e, etc.) from structural relationships between rule-types.
- Potential connection to Higgs mechanism: ED may predict the analog of the Higgs field as a specific participation-structure feature that couples universally to chain rule-types.

**Primitives involved.**
- Primitive 02 (chain) — the object whose mass is derived.
- Primitive 07 (channel + rule-type) — the classification to be derived.
- Primitive 04 (bandwidth) — the source of σ_τ.
- Primitive 12 (thickening) — accumulated structure that may relate to mass.

**Inherited content.**
- Speed of light c (for dimensional conversion).
- Possibly: empirical masses of a small number of "reference" particles, used as calibration against the Dimensional Atlas.

**Dependencies.**
- Strongly depends on Primitive 07 §7.4 rule-type taxonomy derivation — which is itself a prerequisite sub-program.
- Intertwined with Arc Q (QFT extension), where species content lives structurally.
- Independent of Arc R (relativistic extension) at the structural level, though the relativistic mass-energy relation is needed for the `σ_τ / c²` identification.

**Difficulty.** Multi-year frontier research program. The hardest of the four arcs.

**Expected memos.**
- `rule_type_taxonomy.md` — primitive-level classification of rule-types.
- `mass_from_chains.md` — mass derivation via σ_τ.
- `mass_spectrum_predictions.md` — specific ratios (electron/proton, etc.).
- Possibly: `higgs_mechanism_analog.md` — primitive-level analog of electroweak symmetry breaking.

**Scope estimate.** Multi-year; approximately 6–10 memos over the arc.

### 2.4 Arc N — Non-Markovian Extension

**Goal.** Extend the Lindblad master equation to handle non-Markovian environmental coupling. Derive memory-kernel structure from refined ED primitives.

**Target equation.**
- Non-Markovian master equation in the Nakajima-Zwanzig or time-convolutionless form:
  `∂_t ρ̂(t) = ∫_0^t dt' K(t − t') ρ̂(t')`
  where `K(t − t')` is the memory kernel.

**Key structural commitments to derive.**
- Refinement of Primitive 08 high-M bath limit to include finite-mode environmental baths.
- Derivation of the memory kernel as the autocorrelation function of environmental modes.
- Reduction to Lindblad form in the Markov limit (memoryless kernel K(t − t') ∝ δ(t − t')).
- Corrections to Lindblad dynamics from non-zero correlation times.

**Primitives involved.**
- Primitive 04 (four-band decomposition) at finite-mode resolution.
- Primitive 08 (multiplicity) with explicit refinement for finite-bath systems.
- Primitive 11 (commitment) with potential for extended-time correlations in commitment-event statistics.

**Inherited content.**
- Bath correlation timescale (apparatus-level; inherited from physical setup).

**Dependencies.**
- Builds directly on the Lindblad extension (already completed).
- Independent of Arcs R, Q, M.

**Difficulty.** Medium. Closest to Phase 1 in character — extends an existing FORCED result.

**Expected memos.**
- `memory_kernel_derivation.md` — primitive-level derivation of K(t − t').
- `non_markovian_corrections.md` — explicit corrections to Lindblad dynamics.
- `bath_correlation_scoping.md` — connection to environmental-mode autocorrelations.

**Scope estimate.** 1–2 sessions; approximately 2–3 memos.

### 2.5 Subsidiary item — ℏ-Origin Memo

**Goal.** Clarify (and if possible reduce) the inheritance of the numerical value of ℏ in the ED framework.

**Status.** Not a full arc; a single cross-cutting memo.

**Content.**
- Explicit statement of how ℏ enters U3, U5, and the Lindblad extension.
- The Dimensional Atlas Madelung anchoring as the current inheritance mechanism.
- Candidate approaches to reducing the inheritance: relating ℏ to participation-graph elementary constants; identifying ℏ with a ratio of primitive-level structural quantities.
- Honest assessment: a full derivation of ℏ's numerical value is likely beyond current scope; the memo documents the inheritance structure rather than eliminating it.

**Expected memo.**
- `hbar_origin.md` — one session.

---

## 3. Dependencies

### 3.1 Primitive-level dependencies

| Arc | Primary primitives | Critical open primitive item |
|---|---|---|
| R (Relativistic) | 02, 04, 06, 07, 13 | Covariant form of 06 (ED gradient) and 13 (relational timing) |
| Q (QFT) | 03, 07, 10, 11 | Rule-type taxonomy (Primitive 07 §7.4) |
| M (Chain-mass) | 02, 07, 04, 12 | Rule-type taxonomy (Primitive 07 §7.4) |
| N (Non-Markovian) | 04, 08, 11 | Finite-mode refinement of Primitive 08 |

### 3.2 Inter-arc dependencies

```
Arc N (Non-Markovian) ──── extends ──→ Lindblad (done)
                                       │
                                       ▼
                                   Phase 1 QM-emergence

Arc R (Relativistic) ───────────── extends ──→ Phase 1 Schrödinger
    │
    └── prerequisite for ──→ Arc Q (QFT, Lorentz-covariant)

Arc M (Chain-mass) ───── requires ──→ Rule-type taxonomy (Primitive 07 §7.4)
                                       │
                                       ├── shared with ──→ Arc Q
                                       │
                                       └── shared with ──→ Arc R (Dirac spinors)
```

### 3.3 Parallelization

- **Can proceed in parallel:** Arcs R and N are structurally independent. N extends the Lindblad part; R extends the Schrödinger part. Work on either can begin without waiting for the other.
- **Sequential requirements:** Arc Q benefits from Arc R being completed first (QFT is typically Lorentz-covariant). Arc M requires the rule-type taxonomy, which is a shared prerequisite for Arc Q.
- **Joint work:** the rule-type taxonomy sub-program benefits both Arc M and Arc Q and can be pursued as a shared prerequisite memo or sub-arc.

### 3.4 Recommended sequence

```
1. ℏ-origin memo (low-urgency, but cheap; cleanly closes one piece of inheritance structure)

2. Arc N — Non-Markovian extension (short; extends Lindblad; 1–2 sessions)

3. Arc R — Relativistic extension
   (Klein-Gordon first; Dirac contingent on rule-type taxonomy)

4. Rule-type taxonomy sub-program
   (prerequisite for Arcs M and Q, and Dirac part of Arc R)

5. Arc M — Chain-mass derivation
   (builds on rule-type taxonomy)

6. Arc Q — QFT extension
   (builds on Arcs R and M; multi-year)
```

---

## 4. Milestones

### 4.1 Short-term (1–2 memos, achievable in the next one or two sessions)

- **ℏ-origin memo** — clarifies inheritance structure; low-urgency single memo.
- **Non-Markovian memory kernel derivation** — extends Lindblad; 1–2 memos.
- **Relativistic participation measure scoping** — opening the R arc with a Lorentz-covariant formulation of P_K; 1 memo before full Klein-Gordon work.

### 4.2 Medium-term (multi-session, completable within a focused research period)

- **Klein-Gordon emergence** — scalar relativistic wave equation from Lorentz-covariant participation measure. Multi-session; approximately 3–4 memos.
- **Non-Markovian corrections to specific platforms** — applying the memory-kernel structure to matter-wave, BEC, or SC-qubit platforms to produce distinguishing predictions.
- **Rule-type taxonomy scoping** — opening the primitive-level classification problem; partial derivation of rule-type structure.

### 4.3 Long-term (frontier research; multi-year programs)

- **Dirac equation derivation** — contingent on rule-type taxonomy for spinor rule-types. Multi-year.
- **Chain-mass from primitives** — contingent on rule-type taxonomy completion; possibly connects to Higgs-mechanism analog. Multi-year.
- **Full QFT extension** — second quantization, particle creation/annihilation, vacuum structure, exchange statistics. Multi-year; approximately 10–15 memos over the arc.
- **Standard-Model emergence scoping** — the frontier target combining Arcs M and Q with the rule-type taxonomy. Research-program scale.

### 4.4 Milestone summary

| Milestone | Arc(s) | Scope | Session count |
|---|---|---|---|
| ℏ-origin memo | subsidiary | single memo | 1 |
| Non-Markovian memory kernel | N | 1–2 memos | 1–2 |
| Relativistic P_K scoping | R | single memo | 1 |
| Klein-Gordon emergence | R | multi-memo | 3–4 |
| Rule-type taxonomy scoping | M, Q (shared) | multi-memo | 3–5 |
| Dirac emergence | R | multi-memo | 3–5 |
| Chain-mass derivation | M | multi-memo | 6–10 |
| QFT full extension | Q | multi-memo | 10–15 |

---

## 5. Deliverables

### 5.1 Per-arc deliverables

**Arc R (Relativistic):**
- `quantum/foundations/relativistic_participation_measure.md`
- `quantum/foundations/klein_gordon_emergence.md`
- `quantum/foundations/dirac_emergence.md` (contingent on rule-type taxonomy)

**Arc Q (QFT):**
- `quantum/foundations/qft_participation_measure.md`
- `quantum/foundations/creation_annihilation.md`
- `quantum/foundations/vacuum_state_derivation.md`
- `quantum/foundations/exchange_statistics.md`
- `quantum/foundations/field_operator_continuum_limit.md`
- `quantum/foundations/standard_model_emergence_scoping.md`

**Arc M (Chain-mass):**
- `quantum/foundations/rule_type_taxonomy.md`
- `quantum/foundations/mass_from_chains.md`
- `quantum/foundations/mass_spectrum_predictions.md`
- Possibly: `quantum/foundations/higgs_mechanism_analog.md`

**Arc N (Non-Markovian):**
- `quantum/foundations/memory_kernel_derivation.md`
- `quantum/foundations/non_markovian_corrections.md`
- `quantum/foundations/bath_correlation_scoping.md`

**Subsidiary:**
- `quantum/foundations/hbar_origin.md`

### 5.2 Platform-bridge deliverables (linked to Arc N)

The non-Markovian extension unlocks refined platform bridges. Candidate retrodictions:

- Matter-wave interferometry with non-Markovian environmental decoherence corrections (beyond Hornberger-Joos-Zeh Markov approximation).
- BEC collective-mode decay with memory-kernel corrections to Landau damping.
- Superconducting qubit dynamics with non-Markovian bath corrections to T1/T2.

Each could produce a distinguishing-content retrodiction against current experimental data in regimes where Markov approximations are known to fail.

### 5.3 Synthesis deliverables

Near the completion of each major arc, a synthesis memo integrating the arc's results:

- `relativistic_qm_synthesis.md` (at Arc R closure).
- `qft_emergence_synthesis.md` (at Arc Q closure).
- `chain_mass_synthesis.md` (at Arc M closure).
- `non_markovian_synthesis.md` (at Arc N closure).

Each synthesis memo follows the template established in `qm_emergence_synthesis.md`.

### 5.4 Closure memos

Each major arc receives a closure memo analogous to `qm_emergence_closure.md`, marking the arc's structural completion and logging remaining research frontiers beyond that arc.

---

## 6. Final summary

**Phase 1 is structurally complete.** The non-relativistic single-particle QM-emergence program plus Lindblad open-system extension constitutes a closed structural derivation from ED primitives. Every structural feature of standard non-relativistic quantum mechanics — state, evolution, measurement, observables, open-system decoherence — is derivable from the participation-measure + four-band + commitment framework, with only ℏ and m inherited.

**Phase 2 begins with this roadmap.** Four extension arcs are identified:

- **Arc R (Relativistic):** Lorentz-covariant participation measure; Klein-Gordon and Dirac as thin-limit consequences.
- **Arc Q (QFT):** multi-chain participation, creation/annihilation, vacuum structure, field operators.
- **Arc M (Chain-mass):** rule-type taxonomy derivation; mass spectrum from primitive-level bandwidth signatures.
- **Arc N (Non-Markovian):** memory-kernel extension of Lindblad dynamics.

Dependencies and milestones are established. Short-term deliverables (ℏ-origin memo, non-Markovian extension, relativistic scoping) are achievable within near-term sessions. Medium-term deliverables (Klein-Gordon emergence, rule-type taxonomy scoping) require focused multi-session work. Long-term deliverables (Dirac, chain-mass, full QFT, Standard-Model emergence scoping) are frontier research programs.

**Phase 2 is a larger-scope program than Phase 1.** Where Phase 1 derived non-relativistic single-particle QM, Phase 2 extends to relativistic, multi-particle, and open-system-with-memory regimes, plus the primitive-level origin of particle masses. Completion of all four arcs would produce a primitive-level foundation for essentially the full content of modern physics at the single-particle + field-theoretic level, with the Standard Model's species content as the prospective endpoint.

**Phase 1 status: closed.**
**Phase 2 status: open, with this roadmap as the master reference.**

---

## 7. Cross-references

### Phase 1 completion documents
- QM-emergence synthesis: [`quantum/foundations/qm_emergence_synthesis.md`](qm_emergence_synthesis.md)
- QM-emergence closure: [`quantum/foundations/qm_emergence_closure.md`](qm_emergence_closure.md)
- Lindblad extension: [`quantum/foundations/lindblad_extension.md`](lindblad_extension.md)
- Tightening program master plan: [`quantum/foundations/candidate_to_forced_program.md`](candidate_to_forced_program.md)

### Primitive stack (load-bearing for Phase 2)
- Primitive 02 (Chain — extension target for relativistic worldlines)
- Primitive 04 (Bandwidth — extension target for covariant bands)
- Primitive 06 (ED Gradient — extension target for four-gradient)
- Primitive 07 (Channel + Rule-type — rule-type taxonomy is central open item)
- Primitive 08 (Multiplicity — extension target for finite-mode baths)
- Primitive 13 (Relational Timing — extension target for Lorentz-invariant time)

### External anchoring
- Dimensional Atlas (regime-specific anchoring of c, ℏ, m): [`papers/Dimensional_Atlas/regimes/`](../../papers/Dimensional_Atlas/regimes/)
- Canonical ED PDE: [`theory/D_crit_Resolution_Memo.md`](../../theory/D_crit_Resolution_Memo.md)

### Memory records
- Phase 1 QM-emergence arc: [`memory/project_qm_emergence_arc.md`](../../.claude/projects/C--Users-allen-GitHub-Event-Density/memory/project_qm_emergence_arc.md)
- Platform-bridges program: [`memory/project_platform_bridges.md`](../../.claude/projects/C--Users-allen-GitHub-Event-Density/memory/project_platform_bridges.md)

---

## 8. One-line summary

> **Phase 1 of the QM-emergence program is structurally complete (non-relativistic single-particle QM + Lindblad open-system dynamics); Phase 2 opens with four extension arcs — Relativistic (Klein-Gordon, Dirac), QFT (multi-particle, field operators, second quantization), Chain-mass (rule-type taxonomy + particle masses from primitives), and Non-Markovian (memory-kernel extension of Lindblad). Dependencies: Arc N builds on Lindblad and is independent; Arc R extends Schrödinger and is prerequisite for Arc Q; Arcs M and Q share the rule-type-taxonomy sub-program. Milestones: ℏ-origin memo and non-Markovian extension are near-term; Klein-Gordon emergence and rule-type scoping are medium-term; Dirac, chain-mass, full QFT, and Standard-Model emergence scoping are long-term frontier research. Phase 2 is a larger-scope program than Phase 1; completion of all four arcs would produce a primitive-level foundation for essentially the full content of modern single-particle-plus-field-theoretic physics, with the Standard Model as the prospective endpoint.**
