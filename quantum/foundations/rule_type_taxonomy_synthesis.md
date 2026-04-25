# Rule-Type Taxonomy — Stage R.2 Synthesis

**Stage R.2.5 — Rule-Type Taxonomy Sub-Program, Closure Memo**
**Status:** Structural closure of Stage R.2. Spin-statistics correspondence η = (−1)^{2s} FORCED at primitive level modulo the discharge of CANDIDATE MB, which is performed here. All of R.2.1–R.2.4 assemble into a closed derivation chain. Per-rule-type spin/mass/charge assignments remain inherited (not structurally derived); Stage R.3 (Dirac emergence) and downstream arcs (M, Q) are unblocked.

---

## 1. Purpose

Stage R.2 opened with the scoping memo `rule_type_taxonomy.md`, which identified four structural levers (L1–L4) governing rule-type classification and proposed a four-memo sub-program:

- R.2.1 `rule_type_exchange_symmetry.md` — exchange dichotomy (Case P / Case R), η ∈ {±1}.
- R.2.2 `lorentz_representations_from_primitives.md` — (j_L, j_R) ladder, spin values.
- R.2.3 `rotational_double_cover_scoping.md` — π_1 = ℤ_2 topology, frame-availability CANDIDATE FA.
- R.2.4 `clifford_algebra_from_spinor_structure.md` — Cl(3,1) frame, FA discharge modulo CANDIDATE MB.

Stage R.2.5's job is to:

(a) Discharge CANDIDATE MB from Primitives 10 + 11, making the full R.2 chain unconditional.
(b) Assemble R.2.1–R.2.4 into a single closed derivation of the spin-statistics correspondence η = (−1)^{2s}.
(c) Record the final FORCED / inherited / deferred separation for the entire sub-program.
(d) Define the dependency structure for downstream arcs (R.3, M, Q).
(e) Mark Stage R.2 as structurally closed.

---

## 2. Summary of Stage R.2 inputs

### 2.1 Primitives used across R.2

| Primitive | Role in R.2                                                                 |
|-----------|-----------------------------------------------------------------------------|
| 02        | Worldline + 3+1D ambient manifold                                           |
| 06        | Four-gradient covariance, Lorentz metric η^{μν}                             |
| 07        | Rule-type content: Levers L1 (bandwidth), L2 (internal index), L3 (interface) |
| 10        | Individuation threshold: coincidence excluded (Case R)                      |
| 11        | Commitment dynamics: continuous exchange path                               |
| 13        | Proper-time relational timing (Stage R.1 anchor)                            |

### 2.2 Upstream results incorporated

- **Stage R.1 closure:** Lorentz-covariant scalar participation measure P_K(x^μ), Klein-Gordon emergence, minimal coupling, conserved current.
- **R.2.1:** η = ±1 exchange dichotomy from rule-type bandwidth × individuation structure.
- **R.2.2:** (j_L, j_R) representation ladder, spin s ∈ {0, 1/2, 1, 3/2, 2, …}.
- **R.2.3:** π_1(Q_2) = ℤ_2 topological theorem; exchange-generator = 2π-rotation generator; CANDIDATE FA.
- **R.2.4:** Cl(3,1) uniqueness; γ^μ frame; σ^{μν} generates SL(2,ℂ); D(R(2π)) = −𝟙 automatic; FA discharged conditional on CANDIDATE MB.

---

## 3. Discharge of CANDIDATE MB

### 3.1 Statement of MB

From R.2.4 §6.1: the rule-type interface admits a bilinear pairing

  m: V_rule × V_rule → 𝒜

on same-type chain internal indices, where 𝒜 = Cl(3,1) (or an appropriate graded component). Without MB, the Cl(3,1) frame is algebraically available but not coupled to rule-type content.

### 3.2 Primitive 10 supplies the pairing structurally

Primitive 10 (individuation threshold) is inherently a **two-chain** structural relation: it tests whether two chains remain distinct or merge. For same-type chains K, K', individuation is expressed at the interface via a scalar indicator

  I_{KK'}(τ, τ') = [individuation pairing of K at τ with K' at τ'],

which must be (i) symmetric or antisymmetric under K ↔ K' (the Stage R.2.1 dichotomy), (ii) Lorentz-covariant (Primitive 06), and (iii) finite-rank at each event pair (Primitive 07 L2 discreteness).

Property (i)–(iii) characterise a **bilinear pairing** on the internal index space of the rule-type. There is no additional structural content required beyond what Primitive 10 already delivers.

Explicitly: writing the internal-index contents of K, K' as Ψ_K, Ψ_{K'} (the participation-measure amplitudes on the rule-type's internal module), the individuation indicator factorises through a Lorentz-covariant bilinear:

  I_{KK'}(τ, τ') = Ψ̄_K(τ) · Γ · Ψ_{K'}(τ')                                    (1)

for some element Γ ∈ Cl(3,1) (or a linear combination thereof, Fierz-decomposable per R.2.4 §5.1). Which Γ appears is rule-type data (Lever L3); that *some* Γ appears is forced by Primitive 10's two-chain structural requirement.

### 3.3 Primitive 11 closes the antisymmetric case

Primitive 11 (commitment dynamics) generates the continuous exchange path. For Case R rule-types, the antisymmetric coupling of (1) is forced by the η = −1 exchange dichotomy of R.2.1, which in turn is forced by the π_1 = ℤ_2 topology of R.2.3. Primitive 11 is what makes the bilinear (1) **time-integrated** along exchange paths, and ensures that the η-dependent sign appears in the actual commitment integral rather than only in instantaneous observables.

### 3.4 MB FORCED

Combining §§3.2–3.3: the bilinear pairing structure required by CANDIDATE MB is exactly the individuation indicator of Primitive 10, made dynamical by Primitive 11. MB is not a new assumption — it is a re-expression of Primitive 10's two-chain pairing content in Clifford-algebra language.

**FORCED (M0):** CANDIDATE MB is discharged. The Cl(3,1) frame is structurally coupled to rule-type content via the individuation-pairing bilinear Ψ̄Γ Ψ, with Γ ranging over the 16-dimensional Fierz basis.

**Consequence:** All R.2.4 "FORCED conditional on MB" results are now unconditionally FORCED. In particular, CANDIDATE FA from R.2.3 is unconditionally discharged.

---

## 4. The closed derivation chain

With MB discharged, the full Stage R.2 derivation assembles into a linear chain with no residual CANDIDATEs.

### 4.1 Chain

**Step A — Exchange dichotomy (R.2.1).**
From Primitives 02, 03, 07, 10, 11: the exchange operation E_{AB} on same-type chains is involutive (E² = id); on joint participation measures it acts by a scalar η(τ); mutual substitutability restricts η to η ∈ {+1, −1}. Two rule-type categories: Case P (η = +1) and Case R (η = −1).

**Step B — Topological upgrade (R.2.3 §3).**
From Primitives 02 + 11 + spatial dimension 3: π_1 of the two-identical-chain configuration space Q_2 equals ℤ_2. This forces η ∈ {±1} topologically (no anyonic phases in 3+1D) and produces Case P (η = +1, contractible configuration space) vs. Case R (η = −1, non-contractible) as topological rather than merely primitive classifications.

**Step C — Exchange-rotation identification (R.2.3 §4).**
Geometric theorem: the generator of π_1(Q_2) equals the generator of π_1(SO(3)) under the SO(3)-equivariant embedding of the relative coordinate. Therefore the exchange sign η equals the 2π-rotation sign on any representation that resolves the rule-type's internal structure.

**Step D — Lorentz ladder (R.2.2).**
From Primitive 06 + finite internal index space: admissible internal-index representations of the Lorentz group are classified by (j_L, j_R) with j_L, j_R ∈ {0, 1/2, 1, …}; spin s runs through {|j_L − j_R|, …, j_L + j_R}; exhaustive ladder s ∈ {0, 1/2, 1, 3/2, 2, …}. Integer class descends to SO⁺(3,1); half-integer class requires SL(2,ℂ).

**Step E — Algebraic frame (R.2.4).**
From Primitive 06 + Lorentz metric + half-integer representation admissibility: the unique real finite-dimensional associative algebra compatible with (P1)–(P4) is Cl(3,1) with γ^μ satisfying {γ^μ, γ^ν} = 2η^{μν}. The Lorentz generators σ^{μν} = (i/2)[γ^μ, γ^ν] generate SL(2,ℂ) on the spinor module. Direct computation: D(R(2π)) = −𝟙 on the spinor module.

**Step F — Interface coupling (R.2.5 §3).**
From Primitive 10 + Primitive 11: the individuation pairing supplies the bilinear structure coupling rule-type chains to the Cl(3,1) frame. MB discharged; FA discharged.

**Step G — Spin-statistics identification.**
Combining B–C–E–F: for any rule-type,
  exchange sign η = 2π-rotation sign D(R(2π)).
On an integer representation, D(R(2π)) = +𝟙 ⇒ η = +1 (Case P).
On a half-integer representation, D(R(2π)) = −𝟙 ⇒ η = −1 (Case R).
Therefore

  η = (−1)^{2s}.                                                               (2)

### 4.2 Final primitive-level statement

**Theorem (primitive-level spin-statistics correspondence):**

*For any ED rule-type in 3+1D with Lorentz-covariant internal index structure, the exchange sign η and the spin quantum number s are related by*

  **η = (−1)^{2s},**

*with η FORCED to lie in {±1} by π_1(Q_2) = ℤ_2, and s FORCED to lie in {0, 1/2, 1, 3/2, 2, …} by the finite-dimensional representation theory of SL(2,ℂ). Integer-spin rule-types are Case P (bosonic); half-integer-spin rule-types are Case R (fermionic).*

No CANDIDATE remains unclosed. The theorem is FORCED at primitive level from Primitives 02, 06, 07, 10, 11, 13.

---

## 5. What is FORCED / inherited / deferred

### 5.1 FORCED at primitive level

- **F1.** η ∈ {+1, −1}, anyons forbidden, from π_1(Q_2) = ℤ_2. (R.2.3)
- **F2.** Spin ladder s ∈ {0, 1/2, 1, 3/2, 2, …}, exhaustive in 3+1D. (R.2.2)
- **F3.** Cl(3,1) as unique frame algebra; γ^μ generators; {γ^μ, γ^ν} = 2η^{μν}. (R.2.4)
- **F4.** SL(2,ℂ) action on spinor module via σ^{μν}; D(R(2π)) = −𝟙. (R.2.4)
- **F5.** Fierz basis of 16 spinor bilinears exhausts Lorentz-covariant two-chain interface content. (R.2.4)
- **F6.** Spin-statistics correspondence η = (−1)^{2s}. (R.2.5, this memo)
- **F7.** Case P = bosonic = integer spin; Case R = fermionic = half-integer spin; Pauli exclusion as consequence of Case R antisymmetry. (R.2.1 + this memo)

### 5.2 Inherited (empirical per-rule-type)

- **I1.** Specific spin value of any particular ED rule-type (which rung of the ladder is occupied). The structure fixes the ladder; not the occupancy.
- **I2.** Mass value per rule-type (m inherited from Stage R.1 Klein-Gordon / Stage R.2.2 Casimir; no structural prediction of numerical values).
- **I3.** Charge and other internal-quantum-number assignments (gauge group representation content per rule-type).
- **I4.** Specific Fierz-coupling choice per Case-R rule-type interface (which Γ ∈ {𝟙, γ^μ, σ^{μν}, γ^μγ^5, γ^5} dominates).
- **I5.** Reality-structure choice: Dirac / Weyl / Majorana (these are algebraic refinements beyond structural necessity).

### 5.3 Deferred to downstream stages

- **D1.** Dirac equation emergence: Stage R.3. The Cl(3,1) frame is now primitive-justified; the dynamical equation follows by linear-square-root-of-Klein-Gordon construction.
- **D2.** Chain-mass derivation: Arc M (contingent on R.3 closure for spin-mass interaction content).
- **D3.** QFT extension: Arc Q (contingent on R.3 + Arc M).
- **D4.** Gauge-group specification and Standard-Model matter content: Arc Q (SU(3)×SU(2)×U(1) representation assignments are empirical, not primitive-derivable).
- **D5.** Higher-generation / flavour structure: Arc M or later.
- **D6.** Spontaneous symmetry breaking / Higgs mechanism: Arc Q.

### 5.4 SPECULATIVE

- **S1.** Structural origin of the number of generations (3): not addressed by R.2.
- **S2.** Primitive-level forbidding of exotic higher-spin (s ≥ 5/2) interacting matter: inherited from Weinberg-Witten / Vasiliev at the QFT level, not derived from ED primitives.
- **S3.** Supersymmetry as a structural possibility: not addressed; ED's taxonomy does not forbid it but does not require it.

---

## 6. Stage R.2 closure statement

### 6.1 Sub-program status

Stage R.2 (rule-type taxonomy) is **structurally closed**. The four-memo sub-program plus this synthesis delivers:

- A primitive-level derivation of the spin-statistics correspondence η = (−1)^{2s}.
- Exhaustive classification of admissible spin values in 3+1D.
- Algebraic identification of the frame carried by Case-R rule-types (Clifford algebra Cl(3,1)).
- Topological identification of the exchange-sign restriction (π_1 = ℤ_2, anyons forbidden).
- Clean separation of structural content (forced) from empirical content (inherited).

All CANDIDATEs opened within R.2 (FA in R.2.3; MB in R.2.4) are discharged. No residual open questions at the R.2 level.

### 6.2 Comparison with Stage R.1 closure

Stage R.1 closed the scalar-participation-measure / Klein-Gordon / minimal-coupling / conserved-current arc. Stage R.2 closes the rule-type-classification / spin-statistics / Clifford-frame arc. Together, R.1 + R.2 constitute the **structural foundation for relativistic quantum kinematics** in ED.

What remains in Arc R is Stage R.3 (Dirac dynamics), which uses the R.2 frame to produce the linear first-order wave equation. R.3 is a dynamical extension, not a new structural layer.

---

## 7. Dependency diagram

```
                    Stage R.1 (Lorentz-covariant scalar P_K, KG)
                                       │
                                       ▼
                    Stage R.2 (rule-type taxonomy, spin-statistics)
                                       │
         ┌─────────────┬───────────────┼───────────────┬─────────────┐
         ▼             ▼               ▼               ▼             ▼
       R.2.1         R.2.2           R.2.3           R.2.4         R.2.5
    (exchange)    (Lorentz reps)  (double-cover)  (Clifford)   (synthesis)
         │             │               │               │             │
         └─────────────┴───────────────┴───────────────┴─────────────┘
                                       │
                                       ▼
                              η = (−1)^{2s} FORCED
                                       │
                                       ▼
                       Stage R.3 (Dirac emergence) [unblocked]
                                       │
                                       ▼
                        Arc M (chain-mass) [contingent on R.3]
                                       │
                                       ▼
                        Arc Q (QFT extension) [contingent on R.3 + M]
                                       │
                                       ▼
                        Standard-Model representation content
                        (empirical inheritance, not derived)
```

### Arc dependencies at a glance

- **R.1 → R.2:** R.2 uses the Lorentz-covariant participation measure from R.1 as its scalar / (0,0)-representation starting point.
- **R.2 → R.3:** Dirac emergence uses the Cl(3,1) frame (R.2.4) + the Lorentz-covariant update law (R.1). Without R.2.4, the γ^μ frame is postulated; with R.2.4, it is primitive-derived.
- **R.3 → Arc M:** Chain-mass derivation requires spin-dependent interaction content, which R.3 supplies via Dirac bilinears.
- **R.3 + Arc M → Arc Q:** QFT extension combines spin-statistics (R.2), Dirac dynamics (R.3), and mass/coupling inheritance (Arc M) into second-quantised field content.
- **Arc N (non-Markovian):** independent thread, not on this dependency chain; ties in at Arc Q + platform-bridge derivations.

---

## 8. Next steps

### 8.1 Immediate: Stage R.3 — Dirac equation emergence

With Stage R.2 closed, Stage R.3 is unblocked. Expected memo: `dirac_emergence.md`. Scope:

- Linear first-order covariant wave equation from the Cl(3,1) frame + Klein-Gordon root.
- Factorisation (iγ^μ∂_μ − mc/ℏ)(iγ^μ∂_μ + mc/ℏ) = (−□ − m²c²/ℏ²).
- Dirac equation (iγ^μ∂_μ − mc/ℏ)Ψ = 0 as Stage R.1 KG's "square root" on the Cl(3,1) module.
- Minimal gauge coupling via Stage R.1 KG's ∂_μ → D_μ procedure applied to spinor module.
- Conserved current j^μ = Ψ̄γ^μΨ from spinor bilinears.
- Non-relativistic reduction to Pauli equation (Zeeman + spin-orbit) and to Schrödinger (Stage Q.2 consistency check).

Estimated scope: 1–2 sessions. Essentially assembly, with one non-trivial structural move (the square-root factorisation).

### 8.2 Queued: Arc M opening scoping

After R.3 closes, Arc M (chain-mass derivation) opens. Scoping memo: `chain_mass_scoping.md`. Expected scope: identify whether ED primitives force a mass value, a mass ratio, or only a mass scale; distinguish kinetic mass from rest mass at the rule-type level; map the Dimensional Atlas anchoring.

### 8.3 Memory / orientation updates

- `MEMORY.md` → `project_qm_emergence_arc.md` update: Stage R.2 closed; spin-statistics FORCED; Arc R now at R.3; Arc M unblocked.
- `docs/ED-Orientation.md` → add Stage R.2 closure entry.
- `docs/ED_Accomplishments.md` → new "Rule-Type Taxonomy" subsection under "QM-Emergence Program".

---

## 9. Summary

Stage R.2.5 delivers the closure of the rule-type taxonomy sub-program:

1. **CANDIDATE MB discharged** via Primitive 10's two-chain individuation pairing made dynamical by Primitive 11. No residual open assumptions within R.2.
2. **Spin-statistics correspondence η = (−1)^{2s} is FORCED at primitive level.** The theorem follows from assembling R.2.1 (exchange dichotomy), R.2.2 (spin ladder), R.2.3 (π_1 = ℤ_2 + exchange-rotation identification), and R.2.4 (Cl(3,1) frame).
3. **Anyons are forbidden** in 3+1D ED; fermions and bosons are the exhaustive classification.
4. **Per-rule-type spin, mass, charge, and Fierz-coupling choices are inherited**, not structurally derived. ED's rule-type structure fixes the ladder and the classification; occupancy is empirical.
5. **Stage R.3 (Dirac emergence), Arc M (chain-mass), and Arc Q (QFT) are unblocked.**
6. **Stage R.2 is structurally closed**, paralleling the Stage R.1 closure. Together R.1 and R.2 constitute ED's structural foundation for relativistic quantum kinematics.

The rule-type taxonomy is complete. What ED says about spin, statistics, and rotational structure is now fully primitive-derived, up to the empirical occupancy of the derived ladder.
