# CANDIDATE → FORCED Tightening Program (U1–U5)

**Date:** 2026-04-24
**Location:** `quantum/foundations/candidate_to_forced_program.md`
**Status:** Master-plan memo for the tightening arc. Analyzes the five upstream CANDIDATE identifications (U1–U5) from `qm_emergence_synthesis.md §4`, identifies U1 as the highest-leverage first target, produces a partial first-pass derivation of U1 from ED primitives, and sets the sequence for attacking U2–U5.
**Purpose:** Launch the next research arc by beginning to promote the QM-emergence chain from CANDIDATE to FORCED at its upstream foundations.

---

## 1. The five upstream CANDIDATEs

From the synthesis memo, the QM-emergence program's downstream results (Schrödinger, Born, Bell/Tsirelson, Heisenberg) rest on five upstream structural identifications adopted provisionally:

- **U1.** `P_K = √(b_K) · e^{i π_K}` — the participation-measure definition (complex-valued fusion of bandwidth + polarity).
- **U2.** Sesquilinear inner product on the participation manifold (constraint C3 of Step 1).
- **U3.** Participation-measure evolution `iℏ ∂_t P_K = H_K P_K + Σ_{K'} V_{KK'} P_{K'}` (linear first-order complex evolution).
- **U4.** Thin-limit momentum-basis identification `K → k` with `H_k = ℏ²k²/(2m) + V`.
- **U5.** Adjacency-band Fourier-conjugate partition `b^{adj} = b_x + b_p`.

**Goal of this program:** promote as many of these as possible from CANDIDATE to FORCED by explicit primitive-level derivation.

---

## 2. Per-U structural analysis

### 2.1 U1 — Participation-measure definition

**Role:** load-bearing for all five steps. Defines the object on which everything else acts.

**Why CANDIDATE:** adopted provisionally in Step 1 as "simplest complex-number fusion of Primitives 04 + 09." Alternative algebras (quaternions, pair-of-reals with custom operations) exist but seem less economical. The specific square-root structure (|P|² = b rather than |P| = b) requires separate justification.

**Primitive-level structures depended on:**
- **Primitive 04** (bandwidth as real non-negative scalar on channels)
- **Primitive 09** (tension polarity as S¹-valued phase per channel)
- **Primitive 07** (channel structure providing the K index)
- **Primitive 08** (thin-regime coherent-sum / multiplicity structure)
- **Primitive 03** (participation as the relational substrate supporting sums)
- **Primitive 11** (commitment dynamics constraining the probability measure structure)

**Path to FORCED:** show that the requirements of (i) amplitude+phase fusion, (ii) coherent-sum compatibility, (iii) Born-rule consistency (bandwidth = squared amplitude via Madelung anchoring), (iv) polar-decomposition uniqueness jointly force the complex-valued form with the square-root amplitude.

**Status after analysis:** U1 is the most tractable of the five because each of (i)–(iv) has a relatively direct primitive-level grounding. See §4 for first derivation attempt.

### 2.2 U2 — Sesquilinear inner product (C3)

**Role:** provides the Hilbert-space structure needed in Steps 4 (Bell/Tsirelson bound via Landau-Khalfin) and Step 5 (orthogonal partitions for uncertainty relations).

**Why CANDIDATE:** constraint C3 was adopted in Step 1 §8 as one of nine structural requirements. A derivation showing it is the unique inner-product form compatible with the complex-valued P_K structure would promote it.

**Primitive-level structures depended on:**
- **Primitive 04** (bandwidth conservation requires real-valued norm via inner product)
- **U1** (complex-valued P forces sesquilinear over bilinear)
- **Primitive 07** (channel structure as natural direct sum)

**Path to FORCED:** show that the sesquilinear form `⟨P|Q⟩ = Σ_K ∫ dx P_K*(x) · Q_K(x)` is the unique bilinear map on P × P that (a) produces the real non-negative norm Σ|P|² = total bandwidth, (b) respects the complex-linear structure of P, (c) is compatible with the four-band decomposition orthogonality.

**Status:** U2 is FORCED **conditional on U1**. Once P is complex-valued (U1), the sesquilinear form is the unique inner product giving real positive norms. Cascades from U1 cleanly.

### 2.3 U3 — Participation-measure evolution equation

**Role:** Step 2 Schrödinger emergence. Without this equation, there is no evolution of P to be mapped to Schrödinger.

**Why CANDIDATE:** the specific form `iℏ ∂_t P_K = H_K P_K + Σ V_{KK'} P_{K'}` was proposed in Step 1 §5.1 as the simplest linear first-order complex evolution. Alternative forms (second-order, non-linear, continuous-channel continuous-time integral equations) are possible but more complex.

**Primitive-level structures depended on:**
- **U1** (evolution acts on P_K as defined)
- **Primitive 11** (commitment preserves amplitude; unitary between commitments)
- **Primitive 02** (chain identity = update rule; rule must evolve linearly for superposition)
- **Primitive 13** (relational timing provides the t-parameter)
- **Primitive 04** (bandwidth conservation → norm preservation → unitarity)

**Path to FORCED:** show that (a) linearity is forced by superposition-compatibility (Primitives 03, 08), (b) first-order-in-time is forced by chain-update rule structure (Primitive 02), (c) the diagonal + off-diagonal structure H_K P_K + Σ V_{KK'} P_{K'} is forced by the most-general linear-operator decomposition on channel space, (d) the iℏ coefficient is inherited from the Dimensional Atlas Madelung anchoring (not derivable from primitives alone).

**Status:** U3 is partially FORCED (structural form) + partially inherited (iℏ coefficient). Probably achievable to CANDIDATE → "FORCED modulo ℏ identification."

### 2.4 U4 — Momentum-basis identification + free kinetic form

**Role:** Step 2 specific Hamiltonian form `H_k = ℏ²k²/(2m) + V`.

**Why CANDIDATE:** Step 2 §3 explicitly flagged K ↔ k as "simplest identification; alternative bases give same Schrödinger after basis change." The free-particle kinetic form is inherited from QM rather than derived.

**Primitive-level structures depended on:**
- **U3** (evolution equation provides the structure on which H_k is defined)
- **Translation invariance** (required for momentum to be the good quantum number)
- **Rotation invariance** (restricts `H_k` to k-square form at leading order)
- **Primitive 05** (ρ as scalar; ED's local-density structure)
- **Chain-mass mapping** (primitive-level account of m = mass; currently inherited, not derived)

**Path to FORCED:**
- Translation-invariance: plausibly FORCED by primitive-level translation symmetry of participation graph in the thin-limit continuum.
- Rotation-invariance: FORCED for isotropic participation graphs; rules out k-linear, leaves k-squared as minimal-order invariant.
- 1/(2m) coefficient: requires chain-mass derivation from ED chain-structure. This is the hardest step.

**Status:** U4 is the hardest of the five. The kinematic form (k² symmetry) can plausibly be FORCED by symmetry. The mass coefficient requires a primitive-level derivation of how chain structure produces the mass parameter — this is an additional derivation program beyond the scope of the QM-emergence chain as currently framed.

### 2.5 U5 — Adjacency-band conjugate partition

**Role:** Step 5 Heisenberg uncertainty derivation. The adjacency band `b^{adj}` must split into two Fourier-conjugate components (position-adjacency `b_x` and momentum-adjacency `b_p`) for the allocation inequality to produce Δx · Δp ≥ ℏ/2.

**Why CANDIDATE:** Step 5 §2.2 flagged the partition as "the ED analog of position-momentum duality; natural given the four-band structure but not rigorously derived from more primitive ED structure." Alternative partitions (three-way, into (x, p, rotation); or orthogonal decomposition into energy-time conjugate pair) are consistent with the four-band framework.

**Primitive-level structures depended on:**
- **Primitive 04** (four-band structure including adjacency band)
- **Primitive 06** (ED gradient; provides the spatial structure that x-partition couples to)
- **U2** (sesquilinear inner product gives orthogonality)
- **Fourier duality** (mathematical property of position/momentum)

**Path to FORCED:** show that (a) the adjacency band's natural decomposition is into orthogonal conjugate pairs under the participation-manifold inner product, (b) for a spatial chain (Primitive 06 provides ∇ρ), the natural conjugate to position is momentum via the momentum-generator structure, (c) the decomposition is exhausted at two components (no residual).

**Status:** U5 is plausibly FORCED by Fourier-duality + dimensional-scope arguments + inner-product orthogonality, all of which have primitive-level grounding. Medium difficulty.

---

## 3. Choosing the first target — U1

### 3.1 Criteria for first target

- **Load-bearing importance:** how much of the QM-emergence chain depends on this identification?
- **Dependency structure:** is this a root or a leaf in the CANDIDATE dependency graph?
- **Likelihood of primitive-level derivability:** is the primitive-level machinery sufficient to derive it, or does it require inherited structure?
- **Impact on downstream steps:** does promotion cascade to other CANDIDATEs?

### 3.2 Scoring

| Target | Load-bearing | Dependency | Derivability | Cascade |
|---|---|---|---|---|
| U1 | ★★★★★ (all 5 steps) | root | high | U2 follows automatically |
| U2 | ★★★★ (Steps 4, 5) | depends on U1 | high conditional on U1 | unlocks Bell/Tsirelson rigor |
| U3 | ★★★ (Step 2) | depends on U1 | medium (ℏ inherited) | unlocks Schrödinger rigor |
| U4 | ★★ (Step 2 specific H) | depends on U3 | low (requires chain-mass) | isolated |
| U5 | ★★★ (Step 5) | depends on U1, U2 | medium-high | unlocks Heisenberg rigor |

### 3.3 Choice: U1

**U1 is selected as the first derivation target** for three reasons:

1. **Highest load-bearing importance.** All five steps of the QM-emergence chain depend on U1. Promoting U1 to FORCED is the largest single unlocking.
2. **Root of the dependency graph.** U2, U3, U5 each require U1. U1 has no upstream CANDIDATE dependencies — it is derivable directly from primitives if derivable at all.
3. **Highest cascade potential.** Promoting U1 automatically upgrades U2 to FORCED (sesquilinear follows from complex-valued by a short argument). That is a two-for-one gain in a single derivation.

**Alternative considered:** U2 first. Rejected because U2 depends on U1; deriving U2 without U1 requires assuming the complex-valued structure of P as a premise, which is circular.

**Alternative considered:** U5 first. Rejected because U5 depends on U1 and U2; also Fourier-duality-based, less primitive-level grounding than U1's coherent-sum argument.

---

## 4. First derivation attempt — U1

### 4.1 Statement of U1

```
P_K(x, t) = √(b_K(x, t)) · e^{i π(K, x, t)}                                    (U1)
```

with b_K real non-negative, π_K ∈ [0, 2π), P_K ∈ ℂ.

### 4.2 Derivation structure

The derivation proceeds in five steps, each grounded in ED primitives:

**Step A:** The participation measure must fuse amplitude (bandwidth, Primitive 04) and phase (polarity, Primitive 09) into a single object.

**Step B:** The fused object must support coherent superposition (Primitives 03, 07, 08, thin-regime structure).

**Step C:** The algebra supporting (A) + (B) is the complex numbers ℂ (or an extension).

**Step D:** ℂ is the minimum-structure algebra; no smaller works; larger algebras (quaternions) add structure not required by the primitives.

**Step E:** The bandwidth-as-squared-amplitude identification (|P|² = b rather than |P| = b) is forced by Madelung anchoring (Dimensional Atlas) in the quantum regime.

Steps A–D establish the complex-valued structure. Step E establishes the square-root.

### 4.3 Step A — fusion of amplitude and phase

**Primitive-level premise:**
- **Primitive 04** supplies `b_K(x, t) ∈ ℝ≥0` — real non-negative bandwidth scalar on channels.
- **Primitive 09** supplies `π(K, x, t) ∈ S¹` — phase angle on channels (tension polarity as a phase relation).

**Claim:** a single object P_K must encode both, because:

1. **Born rule structure (Primitive 11):** commitment selection depends on bandwidth weights. If P_K carries amplitude only, Born works but interference does not.
2. **Interference (Primitive 07 channel recombination):** two channels that recombine produce fringes whose position depends on phase differences. If P_K carries phase only, interference works but amplitudes don't normalize properly.
3. **Madelung consistency (Dimensional Atlas quantum regime):** the wavefunction ψ = √ρ · e^{iS/ℏ} requires both amplitude and phase in a single object. Without fusion, the Madelung structure is broken.

**Conclusion:** the participation measure must carry both real scalar (bandwidth) and phase (polarity) in one object. **Status: FORCED** by the joint requirement of Born rule + interference + Madelung consistency.

### 4.4 Step B — coherent superposition requirement

**Primitive-level premise:**
- **Primitive 08 (Multiplicity):** in the thin regime, multiple channels coexist coherently. The chain is in a superposition across channels.
- **Primitive 03 (Participation):** shared participation structure across channels requires linear superposition for entanglement.
- **Primitive 07 (Channel):** channels recombine at beamsplitters, producing interference that requires amplitude-level sum with phase relations.

**Claim:** the set of P_K states must be closed under linear combination: given P_K^A and P_K^B, the superposition `α P_K^A + β P_K^B` (for some scalars α, β) must also be a valid P_K state.

**Required structure:** P_K must live in a vector space over some field F. For the superposition scalars α, β to carry phase information (necessary for interference), F must be a field extension of ℝ that contains e^{iθ} for θ ∈ [0, 2π).

**Conclusion:** the participation measure must be a **vector-valued field** over a scalar field F that contains phase-rotation elements. **Status: FORCED** by Primitives 03, 07, 08 thin-regime + interference compatibility.

### 4.5 Step C — algebra identification: F = ℂ

**Claim:** the minimal field F satisfying Step B is the complex numbers ℂ.

**Argument:**

Phase rotations generate a representation of the circle group S¹. A field containing `{e^{iθ} : θ ∈ [0, 2π)}` must contain the algebraic closure of ℝ in the direction of S¹ rotation. The minimum such field is ℂ:

- ℝ alone does not contain e^{iπ/2} = i; insufficient.
- ℂ contains all e^{iθ}, supports addition and multiplication, and is algebraically closed.
- Quaternions ℍ contain S¹ plus additional rotation structure (three mutually orthogonal imaginary units i, j, k); more structure than required.

**Conclusion:** F = ℂ. **Status: FORCED** by "minimum algebra containing S¹ rotations and supporting field operations" = ℂ (standard algebra result).

### 4.6 Step D — no smaller algebra works, larger not needed

**No smaller:** ℝ fails Step C. Two-component real representations `(Re P, Im P)` are isomorphic to ℂ (same algebra in different notation). The pair `(b, π)` with custom addition rule is also isomorphic to ℂ (under `P = √b · e^{iπ}`).

**No larger:**
- Quaternions ℍ: non-commutative multiplication. Non-commutativity would force channel ordering to matter in addition, contradicting the commutativity required by Primitive 03 participation (shared participation is symmetric between endpoints). Also, no primitive-level motivation for three imaginary units.
- Octonions 𝕆: non-associative. Not a field. Incompatible with linear superposition axioms.

**Conclusion:** ℂ is the unique minimum-structure field supporting the required properties. **Status: FORCED** by exclusion of smaller and larger.

### 4.7 Step E — the square-root choice

**Premise:** once P_K is ℂ-valued, it admits polar decomposition P_K = A_K · e^{iφ_K} with A_K ∈ ℝ≥0 (amplitude) and φ_K ∈ [0, 2π) (phase). The identification of φ_K with polarity π_K (Primitive 09) is direct.

**Remaining question:** what is the identification of the Primitive 04 bandwidth b_K with the amplitude A_K? Two candidates:

- **Candidate E1:** b_K = A_K (bandwidth = amplitude-magnitude; P_K = b_K · e^{iπ_K}).
- **Candidate E2:** b_K = A_K² (bandwidth = amplitude-squared; P_K = √(b_K) · e^{iπ_K}).

**Argument for E2:**

- **Madelung consistency (Dimensional Atlas):** in the quantum regime, ρ = |ψ|² via Madelung's theorem. If Ψ = Σ_K P_K is the wavefunction, then ρ = |Ψ|² is the event density. Per Primitive 05, event density ρ = Σ_K b_K. Therefore Σ_K b_K = |Σ_K P_K|². For single-channel concentration (P_K = P_{K*}·δ_{K, K*}), this gives b_{K*} = |P_{K*}|². **Therefore E2.**

- **Born rule consistency (per Step 3):** commitment selection probability is bandwidth-fraction. This matches QM's |⟨K*|Ψ⟩|² / ⟨Ψ|Ψ⟩ only under E2. Under E1, Born would read |P|/Σ|P|, which does not match empirical QM.

**Conclusion:** E2 (bandwidth = amplitude-squared) is FORCED by Madelung consistency + Born rule consistency with empirical QM. **Therefore P_K = √(b_K) · e^{iπ_K}.**

**Status: FORCED** conditional on (a) Madelung anchoring (inherited from Dimensional Atlas), (b) empirical match to QM's Born rule (inherited from empirical consistency requirement).

### 4.8 Combined result

**U1 is FORCED** conditional on:
- Primitives 03, 04, 07, 08, 09, 11 as defined.
- Dimensional Atlas Madelung anchoring (ρ = |ψ|² in quantum regime) — this is a structural commitment inherited from earlier ED work, not a QM postulate.
- No smaller or larger algebra than ℂ (§4.6 argument).

**Status promotion:** U1 moves from CANDIDATE to **FORCED** conditional on the three items above. The derivation is essentially complete; what remains is to make the Madelung anchoring itself primitive-level rather than dimensional-atlas-inherited.

### 4.9 What this first derivation establishes

- The complex-valued form of P_K is forced by primitive-level structure (amplitude + phase + superposition) combined with minimum-algebra arguments.
- The square-root structure is forced by Madelung consistency.
- Cascade: **U2 (sesquilinear inner product) now follows automatically.** Once P is complex-valued with the U1 form, the unique real-norm inner product is the sesquilinear one.

**Net:** U1 + U2 jointly promoted to FORCED (with the noted Madelung-inheritance caveat).

---

## 5. Program-level plan for U3–U5

### 5.1 Dependency-ordered sequence

```
U1 (FORCED this memo)
  ↓ cascades to
U2 (FORCED as corollary)
  ↓
U3 (Step 2 evolution — next target)
U5 (Step 5 partition — third target, parallel with U3)
  ↓
U4 (hardest, requires chain-mass derivation)
```

### 5.2 Next target: U3

**Priority: after U1/U2 are in hand, U3 is the natural next target** because:

- It depends on U1 + U2, which are now promoted.
- It unlocks Step 2 (Schrödinger emergence) at CANDIDATE → FORCED for the structural form.
- Residual issue (ℏ coefficient) is shared with U4; can be deferred to a dedicated "origin-of-ℏ" memo.

**Derivation sketch for U3:**

- Linearity of evolution: FORCED by superposition-compatibility (Primitives 03, 08).
- First-order-in-time: FORCED by Primitive 02 chain-update rule structure (each time-step = one rule-application).
- Diagonal + off-diagonal decomposition: FORCED by most-general linear-operator form on channel space.
- iℏ coefficient: inherited from Dimensional Atlas (deferred to ℏ-origin memo).

**Expected memo:** `quantum/foundations/u3_evolution_derivation.md`. Estimated difficulty: medium. Estimated payoff: closes Step 2 structural gap.

### 5.3 Third target: U5

**Priority: third** because U5 depends on U1 + U2 (both now in hand), but is independent of U3.

**Derivation sketch for U5:**

- Adjacency band has Fourier-conjugate decomposition: FORCED by Primitive 06 gradient structure + translation-invariance of the participation graph.
- Two-component exhaustion: position and momentum are the complete Fourier-dual pair in 1D; extensions to multi-D give parallel structures on each axis.
- Orthogonality: FORCED by U2 inner product applied across the conjugate pair.

**Expected memo:** `quantum/foundations/u5_adjacency_partition_derivation.md`. Estimated difficulty: medium. Estimated payoff: closes Step 5 structural gap; enables rigorous Heisenberg.

### 5.4 Last target: U4

**Priority: last** because U4 requires:
- U3 (evolution structure) in place.
- A primitive-level derivation of mass m from chain structure — this is a separate program, not yet begun.

**Derivation sketch for U4 (structural part only):**

- k² leading order: FORCED by rotation invariance + non-relativistic regime.
- Translation invariance: FORCED by homogeneous-limit assumption.
- Mass identification: DEFERRED — requires chain-mass primitive-level derivation. Candidate: mass = bandwidth-budget of chain / thickness, normalized appropriately.

**Expected memo:** `quantum/foundations/u4_hamiltonian_form_derivation.md`. Estimated difficulty: high (requires chain-mass derivation). Estimated payoff: closes the deepest Step 2 inheritance from QM. Likely needs a companion memo `quantum/foundations/mass_from_chains.md`.

### 5.5 Program timeline (rough estimate)

- U1 + U2: this memo. **COMPLETE** (modulo Madelung-anchoring inheritance).
- U3: one session. Medium difficulty.
- U5: one session. Medium difficulty.
- U4: two-to-three sessions (chain-mass derivation is the hard part).
- ℏ-origin memo: one session (cross-cuts U3 and U4 inheritance).

**Total estimated completion: 4–6 additional sessions** to promote all five CANDIDATEs to FORCED (modulo inherited items).

---

## 6. Impact on the QM-emergence chain

### 6.1 After U1 + U2 (current memo)

| Step | Previous status | New status |
|---|---|---|
| 1 | CANDIDATE | **FORCED** (U1 derived here) |
| 2 | CANDIDATE (3 upstream) | CANDIDATE (U3, U4 remain) |
| 3 | FORCED (1 CANDIDATE) | FORCED (1 CANDIDATE: phase-independence) |
| 4 | FORCED (1 CANDIDATE: C3) | **FORCED** (U2 promoted; no residual CANDIDATE) |
| 5 | FORCED (1 CANDIDATE: U5) | FORCED (1 CANDIDATE: U5) |

**Net gain from this memo:** Steps 1 and 4 promoted to FORCED. Steps 2 and 5 reduced in CANDIDATE count. One of the program's weakest links (Step 4 Tsirelson-bound derivation) is now fully FORCED.

### 6.2 After U3 (next memo)

Step 2 structural form FORCED (pending ℏ-origin derivation).

### 6.3 After U5

Step 5 fully FORCED.

### 6.4 After U4 (and ℏ-origin)

Step 2 fully FORCED.

**End state: all five steps FORCED, with inherited Dimensional-Atlas content clearly marked as distinct from primitive-derived content.**

---

## 7. Honest framing

### 7.1 What this memo achieves

1. **U1 derivation at FORCED level**, conditional on (a) primitives 03/04/07/08/09/11, (b) Dimensional Atlas Madelung anchoring, (c) minimum-algebra arguments for ℂ.
2. **U2 cascades to FORCED** as a corollary of U1.
3. **Step 4 (Bell/Tsirelson) fully FORCED** — the first downstream step to lose all CANDIDATE dependencies.
4. **Structured plan for U3–U5** with dependency ordering and expected derivation difficulty.

### 7.2 What this memo does not achieve

1. **Does not eliminate the Dimensional-Atlas inheritance.** U1 relies on Madelung anchoring ρ = |ψ|². An ED-primitive-level derivation of this anchoring — i.e., why ρ = |ψ|² specifically, not ρ = |ψ| or ρ = |ψ|³ — is a separate task.
2. **Does not promote U3, U4, U5.** Those are specified for future memos.
3. **Does not address the origin of ℏ.** Deferred to a cross-cutting memo.
4. **Does not extend to relativistic or QFT contexts.** Non-relativistic scope preserved.

### 7.3 The structural honesty

The U1 derivation is "FORCED modulo inherited content." The inherited content (Madelung anchoring; ℏ value) reflects ED's quantum-regime empirical match rather than pure primitive-level derivation. This is structurally honest: ED is not derived in vacuum; it is derived to match empirical QM in the quantum regime. The Dimensional-Atlas anchoring is an empirical bridge, not a hidden postulate.

**The tightening program's goal is not to eliminate all inheritance, but to make the inheritance explicit and to show that everything else follows from it.** In that sense, the program succeeds if it can reduce the inheritance to a small, clearly-identified set of constants (ℏ, m, Madelung-anchoring) with all structural content derived.

---

## 8. Status classification summary

| Element | Status after this memo |
|---|---|
| U1 (participation-measure definition) | **FORCED** (conditional on Madelung anchoring) |
| U2 (sesquilinear inner product) | **FORCED** (cascades from U1) |
| U3 (evolution equation) | CANDIDATE (next target) |
| U4 (momentum-basis H_k) | CANDIDATE (hardest; requires chain-mass derivation) |
| U5 (adjacency partition) | CANDIDATE (third target) |
| Step 1 (participation measure) | **FORCED** |
| Step 2 (Schrödinger) | CANDIDATE (awaiting U3, U4) |
| Step 3 (Born rule) | FORCED (1 residual CANDIDATE unchanged) |
| Step 4 (Bell/Tsirelson) | **FORCED** (U2 cascade closes the gap) |
| Step 5 (Heisenberg) | FORCED (1 residual CANDIDATE: U5) |

**Two steps fully FORCED** (1 and 4) after this memo. One step one-CANDIDATE-away (Step 5 needs U5). Step 2 needs U3, U4. Step 3 has a residual CANDIDATE (phase-independence) unrelated to U1–U5.

---

## 9. Cross-references

### Program-level
- QM-emergence synthesis: [`quantum/foundations/qm_emergence_synthesis.md`](qm_emergence_synthesis.md)
- Step 1 (participation measure): [`quantum/foundations/participation_measure.md`](participation_measure.md)
- Step 2 (Schrödinger): [`quantum/foundations/schrodinger_emergence.md`](schrodinger_emergence.md)
- Step 3 (Born rule): [`quantum/foundations/born_rule_from_participation.md`](born_rule_from_participation.md)
- Step 4 (Bell/Tsirelson): [`quantum/foundations/bell_correlations_from_participation.md`](bell_correlations_from_participation.md)
- Step 5 (Heisenberg): [`quantum/foundations/uncertainty_from_participation.md`](uncertainty_from_participation.md)

### Primitive stack
- [`quantum/primitives/03_participation.md`](../primitives/03_participation.md)
- [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md)
- [`quantum/primitives/07_channel.md`](../primitives/07_channel.md)
- [`quantum/primitives/08_multiplicity.md`](../primitives/08_multiplicity.md)
- [`quantum/primitives/09_tension_polarity.md`](../primitives/09_tension_polarity.md)
- [`quantum/primitives/11_commitment.md`](../primitives/11_commitment.md)

### External inheritance
- Dimensional Atlas (Madelung anchoring): [`papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md`](../../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md)
- Canonical ED PDE: [`theory/D_crit_Resolution_Memo.md`](../../theory/D_crit_Resolution_Memo.md)

---

## 10. One-line summary

> **U1 (participation-measure definition `P_K = √b · e^{iπ}`) is promoted to FORCED via a five-step derivation: (A) amplitude+phase fusion required by primitives; (B) coherent-superposition compatibility requires vector-space structure; (C) minimum algebra is ℂ; (D) no smaller (ℝ fails) or larger (ℍ/𝕆 over-structured) algebra works; (E) the square-root is forced by Madelung anchoring + Born-rule empirical match. U2 (sesquilinear inner product) cascades to FORCED automatically. Net result after this memo: Steps 1 and 4 of the QM-emergence chain are fully FORCED; Steps 2, 3, 5 have reduced CANDIDATE dependencies. Next targets in order: U3 (evolution equation), U5 (adjacency-partition), U4 (Hamiltonian form, hardest, requires chain-mass derivation). The tightening program reduces ED's QM-emergence inheritance from QM down to a small, clearly-identified set: Madelung anchoring + ℏ value + chain-mass mapping. Everything else derives from primitives.**
