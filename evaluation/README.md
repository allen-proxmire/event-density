# ED Substrate — Architectural Distillation Evaluation

Substrate-level Architectural Distillation (AD) evaluation of **Event Density (ED)**. Two layers live here: a **structural** evaluation (the `Phase_*` design docs) that located ED's *determinability boundary*, and a set of **empirical/quantitative arcs** (the subfolders) that measure and probe that boundary and ED's other structural commitments.

Throughout: **crank-safe, graph-first, structural/form parallels only.** ED is examined as a finite-reach/finite-memory relational substrate; claims are tiered and honestly bounded. The recurring discipline note — ED↔FS (Factor Skyline) parallels are *structural form only* (shared abstract class, never a content claim that ED explains primes or FS explains physics).

---

## The arcs (empirical / quantitative)

| Arc | Folder | Question | Verdict (one line) |
|---|---|---|---|
| **Bits** | [`Bits/`](Bits/) | Can the determinability boundary be measured in bits? | Across-boundary MI **M2 ≈ 0** — a robust, observable-*independent* perfect severance. There is **no single intrinsic scalar Δ** (it's observable-dependent, 0.17–0.98 bits). ED quantifies the boundary *structurally* — and the structural answer is the zero. |
| **A1** (in Bits) | [`Bits/docs/A1_ChannelCapacity_Results.md`](Bits/docs/A1_ChannelCapacity_Results.md) | Does channel *capacity* (observable-independent) give a positive intrinsic invariant? | **No — capacity is exactly zero**, within strata *and* across the boundary, by ED locality. The boundary is an **observational common-cause** structure, not a transmission channel. Empirically confirms "no nonlocal influence." |
| **B4** | [`B4_Arc/`](B4_Arc/) | Is electric charge a discrete topological invariant on the participation graph? | ED realizes the **topological *skeleton*** of charge (winding ∈ ℤ, quantized, conserved, irreversibility-protected, integral Gauss law) and withholds the **metrical *flesh*** (local field, Coulomb) — *outside ED by construction*, blocked by orientation-blindness + P11 irreversibility. |
| **Primes** | [`Primes_Arc/`](Primes_Arc/) | What does a finite substrate's ceiling look like, measured against the integers? | Finite memory **saturates the template** (1.700-bit invariant reproduced; lpf-ladder exact) and **fails the escape** (best μ-correlator → 0, Sarnak-in-class; twin density needs 2C₂). Ceiling located exactly where known mathematics places it. |

### The unifying thread
The arcs triangulate on one property: **ED's hard ceiling on long-range / global information**, a consequence of finite reach + finite memory + orientation-blind irreversible commitment.

- **A1 + Primes** measure the *same* finite-reach ceiling two ways — A1 *inside* ED (controlled capacity = 0), Primes against an *external, math-certified* ruler (Möbius disjointness). Together: *can ED finite-memory produce an infinite-memory system like primes?* → **template yes, escape no; the *no* is load-bearing.**
- **Bits** locates the determinability boundary and shows its invariant content is a zero, not a scalar.
- **B4** shows the same architecture that makes ED a determinacy engine (orientation-blind selection + irreversible commitment) is *precisely* what gives charge its topological skeleton while foreclosing a continuous field. The complementarity is the point.

---

## The structural evaluation (`Phase_*` docs)

The original substrate-level AD pass that located the determinability boundary and specified the certified simulator the arcs build on:

- `Memo_00_ED_Substrate_AD_Scoping.md` — scoping.
- `Phase_A_CriterionMapping.md`, `Phase_A1_SubstrateLevel_AD_Criteria.md`, `Phase_A2_DiscreteExtraction_Modes.md` — criteria mapping.
- `Phase_B_ArchitecturalSpecification.md` — architecture.
- `Phase_C_EnvelopeExtraction.md`, `Phase_D_ExtremalDynamics.md` (the real Σ = Coh − Str − Grad selection rule), `Phase_E_ConstraintSurface.md` (the decoupling-surface boundary).
- `Phase_F_CriteriaEvaluation.md`, `Phase_G_Generalization.md` — evaluation + generalization.
- `Phase_OrientationPrimitivity_Resolution.md`, `Phase_TieBreak_Specification.md`, `Phase_Bits_DeterminabilityBoundaryMeasurementPlan.md` — supporting resolutions and the bits-measurement plan.

The certified simulator (7 modules, 20/20 correctness gates) lives in [`Bits/simulator/`](Bits/simulator/); all three arcs reason against it (B4 and Primes use purpose-built minimal models where the certified sim is the wrong tool — noted in their docs).

---

## Status

All three arcs are **closed and committed**: Bits (`84ce395`), A1 (`af2f067`), B4 (`c8d61e2`), Primes (`aa0f545`). Each subfolder carries its own README and results docs. Possible future arcs are flagged at the end of each arc's docs (e.g. B4's ED-I synthesis / U(1)-vs-Z₂ question) and are *new* arcs, not continuations.
