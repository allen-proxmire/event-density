# D-Variable Disambiguation

**Date:** 2026-04-24
**Location:** `quantum/effective_theory/d_variable_disambiguation.md`
**Status:** Derivation memo. Resolves Problem 1 identified in `distinguishing_signatures.md §2`. Proposes an affine mapping between the two D variables, classified CANDIDATE. Partially unblocks the distinguishing-signature path but leaves Problem 2 (temporal vs. spatial) unresolved.
**Purpose:** Distinguish the two `D` variables that have been treated as one in the derivation chain, determine whether they are identical / coarse-graining-related / fundamentally distinct, and produce a corrected derivation-chain diagram with updated reach.

---

## 1. The two D variables, defined explicitly

### 1.1 D_participation (primitive / mapping layer)

**Origin:** Primitive 08 (Multiplicity); formalized in `visibility_to_bandwidth.md §3.1`; appears in `pde_parameter_mapping.md §4.1`.

**Mathematical definition:**

```
D_participation(x) = Σ_K b_K²(x) / (Σ_K b_K(x))² = 1 / M_eff(x)       (1)
```

where `b_K(x)` is the bandwidth in channel K at position x, summed over all available channels, and `M_eff` is the participation ratio (standard statistical-mechanics quantity).

**Physical meaning:** a scalar that measures how concentrated the chain's bandwidth is into a single dominant channel vs. spread across many competing channels. `D_participation = 1` means a single channel carries all bandwidth (committed). `D_participation = 1/N` means bandwidth is equidistributed across N channels (maximally spread).

**Domain:** participation-graph level; a local field over the emergent manifold (or discrete over the participation graph).

**Range:** `D_participation ∈ [1/N, 1]` where N is the number of channels. Under the three-channel KDTLI commitment (`visibility_to_bandwidth.md §1.1`), `D_participation ∈ [1/3, 1]`.

**Notation used hereafter:** `D_P` (for Participation).

### 1.2 D_PDE (canonical two-channel PDE)

**Origin:** The canonical ED PDE, formalized in `theory/D_crit_Resolution_Memo.md §2`. Appears in the Q-C Boundary paper's predictions (`quantum/papers/Q-C Boundary_Transition. Theory, Prediction, Path.pdf`).

**Mathematical definition:**

The canonical two-channel PDE is:

```
∂_t ρ = D · F[ρ] + H · v                            (2a)
∂_t v = (F[ρ] − ζ · v) / τ                          (2b)
F[ρ] = M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ)              (2c)
D + H = 1                                           (2d)
```

`D` here is the fraction of `F[ρ]` routed through the direct-ρ channel (eq. 2a first term). `H = 1 - D` is routed through the participation-v channel (eq. 2a second term).

**Physical meaning:** a constitutive coupling weight of the PDE. `D_PDE = 1` means all ρ-evolution proceeds through local F[ρ]-driven diffusion; participation-field `v` is decoupled. `D_PDE = 0` means all ρ-evolution proceeds through mean-field v-coupling; direct local dynamics are suppressed.

**Domain:** PDE-level; a constitutive choice, typically treated as a scalar parameter (may vary in x, t in principle).

**Range:** `D_PDE ∈ [0, 1]` by the `D + H = 1` constraint.

**Notation hereafter:** `D_E` (for Equation / PDE).

### 1.3 Side-by-side

| Property | `D_P` | `D_E` |
|---|---|---|
| Origin | Primitive 08 / mapping layer | PDE (2a–2d) / constitutive layer |
| Mathematical form | Σb²/(Σb)² = 1/M_eff | constitutive coupling weight |
| Physical meaning | channel-bandwidth concentration | direct-vs-participation routing |
| Domain | local field over participation graph | constitutive parameter of the PDE |
| Range | [1/N, 1] (N = channel count) | [0, 1] (by D + H = 1) |
| At "committed" limit | D_P = 1 | D_E = 1 |
| At "maximally coherent" limit | D_P = 1/N | D_E = 0 |

---

## 2. Are these the same quantity?

**No — they are not the same at face value.** The mathematical definitions, physical meanings, and natural ranges differ. `D_P` is a distribution-concentration measure; `D_E` is a PDE coupling weight. They share:

- The same symbol convention (both written `D` in the literature)
- The same conceptual direction (higher values = "more committed", lower = "more coherent")
- The same range boundaries (both approach 1 at the committed limit, both approach a lower bound at the coherent limit)

But their underlying content is different.

### 2.1 Why the conflation occurred in the derivation chain

The Q-C Boundary paper uses `D` without specifying which. Our derivation chain:

- `pde_parameter_mapping.md §4.1` committed to `D = Σb²/(Σb)² = D_P`.
- `visibility_to_bandwidth.md §3.1` used this to compute `D(V) = V⁴/2 + (1−V²)²`.
- `arndt_step_2.md §2.3` set `D_crit(ζ) = √(2-ζ)(2-√(2-ζ))` from the D_crit resolution memo, whose `D` is actually `D_E`.
- The comparison `D(V) = D_crit` in `visibility_to_bandwidth.md §3.3` treated `D_P = D_E` implicitly.

**This conflation is the source of Problem 1 in `distinguishing_signatures.md`.** When I computed D(V)_min = 1/3 and concluded "D < 0.1 is unreachable," I was computing `D_P_min` under the three-channel scheme. `D_E < 0.1` is a constraint on a different variable that may or may not correspond to `D_P < 0.1`.

---

## 3. Coarse-graining relationship

### 3.1 Proposed mapping (CANDIDATE)

**Hypothesis:** `D_E` is the coarse-grained thick-regime shadow of `D_P`, normalized so that `D_P = 1/N` (maximally distributed) maps to `D_E = 0` (pure participation-channel dynamics), and `D_P = 1` (fully concentrated) maps to `D_E = 1` (pure direct-channel dynamics).

The natural affine rescaling:

```
D_E = (N · D_P − 1) / (N − 1)                       (3)
```

where `N` is the channel count under the adopted counting scheme.

**Properties:**

- `D_P = 1/N  →  D_E = 0` ✓
- `D_P = 1    →  D_E = 1` ✓
- Monotone increasing in `D_P`
- Linear (affine)

**Under the three-channel KDTLI scheme (N = 3):**

```
D_E = (3 · D_P − 1) / 2 = 1.5 · D_P − 0.5           (4)
```

**Under the product-space scheme (N = 2·N_int, large N_int):**

```
D_E ≈ D_P                                           (5)
```

— at large channel count, `D_E` and `D_P` become approximately identical.

### 3.2 Why affine, not general?

The affine form (3) is the minimum-complexity coarse-graining that (a) matches the endpoints and (b) preserves monotonicity. It has no free parameters beyond the channel-count N. More general forms (quadratic, exponential, etc.) introduce free parameters that would be tuning knobs.

**Caveats:**

- A derivation of `D_E` from `D_P` via an explicit PDE-coarse-graining argument would likely produce a specific non-affine form. I am not executing that derivation here; the affine mapping is a first-pass hypothesis.
- The channel-count N enters asymmetrically: at low N (small ensembles), `D_E` deviates from `D_P` substantially; at high N, they coincide. Whether KDTLI physics is best described by N = 3 (our three-channel commitment) or N large remains an open question.

### 3.3 Status classification

| Step | Status |
|---|---|
| Both D variables exist as distinct mathematical objects | FORCED |
| They share conceptual direction (high = committed) | FORCED |
| Their ranges can be affinely rescaled to match | FORCED |
| The specific affine mapping (3) | CANDIDATE |
| The affine mapping as the physically correct coarse-graining | SPECULATIVE |
| Derivation of the PDE-coarse-graining form | NOT DONE |

---

## 4. Application to Eibenberger 2013 and Fein 2019

### 4.1 Re-examining "D < 0.1 unreachable"

From `distinguishing_signatures.md §2.1`: `D_P(V) = V⁴/2 + (1-V²)²` has minimum 1/3. Under the three-channel scheme, `D_P ∈ [1/3, 1]`.

Under the affine mapping (4):

```
D_E(V) = 1.5 · D_P(V) − 0.5 = 1.5 · [V⁴/2 + (1-V²)²] − 0.5    (6)
```

- At `V = 1`: `D_P = 1/2`, `D_E = 0.25`
- At `V = √(2/3) ≈ 0.816`: `D_P = 1/3`, `D_E = 0`  (minimum of D_E)
- At `V = 0`: `D_P = 1`, `D_E = 1`

**`D_E < 0.1` condition:**

```
1.5 · [V⁴/2 + (1-V²)²] − 0.5 < 0.1
V⁴/2 + (1-V²)² < 0.4
```

This is reachable. From `distinguishing_signatures.md §2.1` algebra (setting the equation to 0.4):

```
u² - (4/3)u + 0.4 = 0   (with u = V²)
u = (4/3 ± √(16/9 - 1.6))/2
  = (1.333 ± 0.400)/2
  = 0.867  or  0.467
V = 0.931  or  0.683
```

So `D_E < 0.1` is reached for `V ∈ [0.683, 0.931]`. **This is a substantial portion of the visibility range.**

### 4.2 Eibenberger and Fein locations under the affine mapping

| Experiment | V_coh | D_P | D_E under (4) |
|---|---|---|---|
| Eibenberger L12 | 0.82 | 0.333 | ~0.00 |
| Fein 25kDa | 0.76 | 0.345 | ~0.018 |

**Both experiments fall within the `D_E < 0.1` regime under the affine mapping.** This is the OPPOSITE of the `distinguishing_signatures.md §2.2` finding — which was based on treating `D_P = D_E`.

### 4.3 Implication for distinguishing signatures

**If the affine mapping (4) is correct:**

- Eibenberger L12 and Fein 25kDa are both in the `D_E < 0.1` regime where ED predicts `N_osc ≈ 9`, `Q ≈ 3.5`, and 3–6% third-harmonic.
- The distinguishing signatures should be present in these datasets — IF they project onto observables that matter-wave fringe data captures.
- Problem 1 (reachability) is resolved. Problem 2 (spatial vs. temporal) is not.

**If the affine mapping is wrong:**

- `D_E` could still be unrelated to `D_P` in a way that places Eibenberger / Fein outside the signature-prediction regime.
- The signatures may apply only to a different experimental class.

The correct move: **treat Problem 1's resolution as contingent on the affine mapping being approximately correct**, and pursue the follow-up derivation that would promote (3) from CANDIDATE to FORCED.

---

## 5. Are the two D variables fundamentally distinct?

### 5.1 Evidence they are related

- Shared directional semantics (both move toward 1 as the system commits)
- Shared dimensionless-and-bounded range [something, 1]
- Both appear in the "Q-C transition" framing of ED's matter-physics predictions
- Both have a natural "maximally coherent" limit

### 5.2 Evidence they may be distinct

- Different mathematical definitions (distribution measure vs. PDE coupling weight)
- Different domains (participation-graph-local vs. PDE-constitutive)
- `D_E` appears with specific paired parameter `H = 1 − D_E`; `D_P` has no such natural complement
- `D_E` is part of a coupled-PDE system with `v, ζ, τ`; `D_P` is computed from bandwidth distribution without reference to those PDE variables
- In different regimes (small-N vs. large-N), the affine rescaling required differs

### 5.3 Most defensible position

**They are distinct quantities that are related by a coarse-graining, with the specific form of the coarse-graining dependent on the channel-counting scheme.** This is the position this memo adopts.

**Consequence:** predictions framed in `D_E` cannot be directly tested against data that measures `D_P`-level observables (like fringe visibility) without the coarse-graining map. The affine mapping (3) is the simplest candidate; correct-form derivation is Phase 2 work.

---

## 6. Corrected derivation-chain diagram

```
Primitive 04 (bandwidth)
  │
  │ four-band partition; b_int, b_adj, b_env, b_com
  ▼
Primitive 11 (commitment)  ──── Primitive 08 (multiplicity)
  │                                │
  │ J_com→env = α_env · Γ_com      │ M_eff = (Σb)²/Σb²
  │                                │
  ▼                                ▼
ζ = τ · α_env · Γ_com / b_com    D_P = 1/M_eff
  │                                │
  │ (eq. 11 of zeta_derivation)    │
  │                                ▼
  │                             V → D_P map: D_P(V) = V⁴/2 + (1-V²)²
  │                                │ (three-channel KDTLI commitment)
  │                                │
  │                                ▼
  │                             V_env correction: V_measurable = V_env · V_coh
  │                                │
  │                                ▼
  │                             Arndt data (Eibenberger/Fein):
  │                                   V_coh → D_P measurement
  │                                   V_c_raw = 0.304 at D_P_crit
  │                                   → V_c_measurable via envelope
  │
  │                                   ╭─── CANDIDATE affine mapping ───╮
  │                                   │                                │
  ▼                                   ▼                                ▼
D_crit(ζ) from D_crit res memo    D_E = (3·D_P − 1)/2             D_E predictions:
   √(2-ζ)(2-√(2-ζ))                                                N_osc ≈ 9
       │                                                           Q ≈ 3.5
       │                                                           triad ≈ 0.03
       ▼                                                           3–6% third-harmonic
   D_E_crit                                                        (Q-C Boundary paper)
       │                                                                ↑
       │ D_crit at PDE level                                             │
       ▼                                                                 │
   ??? ← ambiguous: does D_crit apply to D_E or D_P? ←──────────────────╯
```

**Critical observation from the diagram:** the D_crit resolution memo's `D_crit(ζ)` formula is derived at the PDE level from linearization of (2a–2d), so `D_crit` is properly a threshold on `D_E`, not `D_P`. Previously we were using `D_crit ≈ 0.83` as the target for our `D_P(V)` comparison (via `D_P(V_c) = 0.83`). Under the affine mapping (4), this would actually correspond to `D_P = (D_E_crit + 0.5)/1.5 = (0.83 + 0.5)/1.5 ≈ 0.887` — not `0.83`.

Re-deriving V_c at `D_P = 0.887`:

```
V⁴/2 + (1-V²)² = 0.887
Let u = V²: u²/2 + (1-u)² = 0.887
u²/2 + 1 - 2u + u² = 0.887
3u²/2 - 2u + 0.113 = 0
u = (2 ± √(4 - 1.017))/3 = (2 ± 1.727)/3
u = 1.242  or  0.091
V = 1.114 (unphysical)  or  V = 0.302
```

**The V_c prediction shifts only slightly under the affine correction:** `V_c ≈ 0.304 → V_c ≈ 0.302`. Within the precision of the CANDIDATE commitments, this is the same number.

**Why so close?** Because D_E_crit ≈ 0.83 and D_P = 0.887 differ at the third digit, and V_c at both D values is dominated by the (1-V²)² term where the final answer is near V ≈ 0.3. The envelope-corrected `V_c_measurable ≈ 0.12` from `apparatus_envelope.md §3.1` is unchanged to two significant figures.

**So the V_c prediction from `visibility_to_bandwidth.md` is approximately preserved under D-disambiguation.** The affine mapping doesn't destroy the retrodiction target.

---

## 7. What remains testable where

### 7.1 Predictions framed at the `D_P` level (participation-ratio / bandwidth-distribution)

These are directly comparable to matter-wave fringe data once the envelope correction is applied:

- **`V_c ≈ 0.304` (coherence fraction at Q-C boundary)** — this memo confirms, with minor adjustment. Matter-wave-testable, pending data in the right regime.
- **Envelope-corrected `V_c_measurable`** — apparatus-specific; matter-wave-testable.
- **Two-point coherence-trajectory extrapolation** — `V_coh(m)` trend → predicts Q-C-crossing mass — matter-wave-testable in principle with a third mass point.

### 7.2 Predictions framed at the `D_E` level (PDE coupling)

These require either:
- The affine mapping (4) to be valid as a coarse-graining, so that `D_E < 0.1` corresponds to specific `D_P` values, OR
- A different experimental platform that measures `D_E` directly, OR
- A temporal rather than spatial observable.

**Specific D_E-level predictions:**

- `N_osc ≈ 9` — transient oscillation count in coherence trajectory. **Temporal.** Not testable against matter-wave spatial fringes.
- `Q ≈ 3.5` — quality factor of coherence oscillations. **Temporal.** Same issue.
- `triad ≈ 0.03` — coupling coefficient (ED-Phys-16). Regime: "all regimes" per Q-C Boundary paper. Physical meaning unclear without archive work; may be testable in both D_P and D_E regimes depending on what "triad coupling" is operationally.
- `3–6% third-harmonic` — per the Q-C Boundary paper text, appears to be a harmonic-generation quantity, typically temporal in nonlinear-optics language. **Likely temporal.**

### 7.3 Summary table

| Prediction | D-level | Temporal or spatial? | Testable in KDTLI/LUMI fringe data? | Testable in optomech/cavity-QED? |
|---|---|---|---|---|
| `V_c ≈ 0.304` | D_P | spatial (coherence fraction) | **yes** (pending envelope-corrected mass-sweep) | possibly, with platform-specific envelope |
| Q-C crossing mass `m_c` | D_P | spatial (from mass-sweep) | **yes** (pending data to 140-250 kDa) | different framing |
| Two-point coherence-trajectory extrapolation | D_P | spatial | **yes** (pending third data point) | different framing |
| `N_osc ≈ 9` | D_E | temporal | **no** (fringes are time-averaged) | **yes** — Rabi/Ramsey in cavity QED |
| `Q ≈ 3.5` | D_E | temporal | **no** | **yes** — free-evolution decay |
| `triad ≈ 0.03` | D_E (likely) | unclear | **unclear** — archive work needed | possibly |
| `3–6% third-harmonic` | D_E (likely) | likely temporal | **no** if temporal; unclear if spatial | **yes** if temporal |

---

## 8. Next remediation tasks

### 8.1 Promote (3) from CANDIDATE to FORCED

Derive `D_E` from `D_P` via explicit PDE-coarse-graining. The argument would go: starting from the bandwidth distribution `{b_K}` that defines `D_P`, compute the coarse-grained (ρ, v) dynamics; identify the coupling weight in the reduced PDE; show it equals or approximates the affine form (3).

**Output memo:** `quantum/effective_theory/d_coarse_graining.md`. Phase 2.

### 8.2 Archive reads for ED-Phys-16/17 (Problem 2 from distinguishing_signatures.md)

Read:
- [archive/research_history/ED Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md](../../archive/research_history/ED%20Physics/ED-Phys-16_CoupledOscillators/ED-Phys-16_CoupledOscillators.md)
- [archive/research_history/ED Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md](../../archive/research_history/ED%20Physics/ED-Phys-17_OscillatorCosmology/ED-Phys-17_OscillatorCosmology.md)

Task: determine whether the `N_osc ≈ 9`, `Q ≈ 3.5`, and `3–6% third-harmonic` predictions are temporal (spectra of coherence-trajectory oscillations) or spatial (fringe-pattern harmonics).

Output: update to `distinguishing_signatures.md` Problem 2 section.

### 8.3 Platform selection for D_E predictions

If the D_E-level predictions are temporal, pick the right experimental class:

- **Cavity QED (Haroche-class):** Rabi oscillations of a two-level atom in a cavity. Time-resolved coherence decay is standard.
- **Superconducting qubits (Devoret-Martinis-Clarke):** T1, T2, T2* measurements give free-evolution temporal coherence directly.
- **Optomechanics (Aspelmeyer-class):** mechanical-mode coherence and ring-down measurements.

**Output memo (if pursued):** `quantum/retrodictions/temporal_coherence_platform_survey.md`. Phase 2/3.

### 8.4 Re-examine the V_c prediction under the corrected picture

Under the affine mapping, `D_E_crit = 0.83` maps to `D_P ≈ 0.887`, giving `V_c ≈ 0.302` — nearly identical to the previous 0.304. The ~0.8% correction is absorbed into the CANDIDATE commitments' overall uncertainty.

**The Arndt retrodiction predictions are essentially unchanged** by this disambiguation. The envelope-corrected `V_c_measurable ≈ 0.12` stands. The verdicts in `arndt_verdict.md` and `fein2019_verdict.md` remain accurate.

---

## 9. What this memo achieved and did not achieve

**Achieved:**

- Distinguished the two `D` variables explicitly: `D_P` (participation-ratio) and `D_E` (PDE coupling weight).
- Established that they are not identical but are monotonically related.
- Proposed an affine CANDIDATE mapping (eq. 3).
- Re-examined Problem 1 from `distinguishing_signatures.md` and found: **the D_E < 0.1 regime IS reachable** under the affine mapping; the earlier "unreachable" conclusion was an artifact of D-variable conflation.
- Computed Eibenberger and Fein positions in D_E space: both are at D_E < 0.02, well inside the distinguishing-signature regime.
- Confirmed the V_c ≈ 0.304 retrodiction prediction survives D-disambiguation almost unchanged.

**Not achieved:**

- Problem 2 (temporal vs. spatial signatures) is not resolved. Requires archive work on ED-Phys-16/17.
- The affine mapping (3) is CANDIDATE, not FORCED. A PDE-coarse-graining derivation is needed to promote it.
- No distinguishing-signature test has been executed. The remediation steps in §8 are required first.

**Honest bottom line:**

Problem 1 of `distinguishing_signatures.md` is PARTIALLY RESOLVED by this memo. Under the affine mapping hypothesis, the existing Arndt datasets are in the right regime for distinguishing-signature detection. Problem 2 (do the signatures apply to spatial fringe data?) remains unresolved and blocks execution.

**The program now has a cleaner picture of its own internal structure:** two distinct `D` variables, a candidate mapping between them, and a clearer separation between predictions testable in matter-wave interferometry (`D_P`-level) vs. those requiring temporal-coherence platforms (`D_E`-level). This is the kind of internal disambiguation that lets future retrodiction attempts be framed correctly from the start.

---

## 10. Cross-references

- Distinguishing-signature analysis (Problem 1 / Problem 2): [quantum/retrodictions/distinguishing_signatures.md](../retrodictions/distinguishing_signatures.md)
- V → D derivation (D_P definition): [quantum/effective_theory/visibility_to_bandwidth.md](visibility_to_bandwidth.md)
- ζ derivation: [quantum/effective_theory/zeta_derivation.md](zeta_derivation.md)
- PDE parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](pde_parameter_mapping.md)
- D_crit resolution (D_E definition): [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md)
- Q-C Boundary predictions: [quantum/papers/Q-C Boundary_Transition. Theory, Prediction, Path.pdf](../papers/Q-C%20Boundary_Transition.%20Theory,%20Prediction,%20Path.pdf)
- Eibenberger verdict: [quantum/retrodictions/arndt_verdict.md](../retrodictions/arndt_verdict.md)
- Fein verdict: [quantum/retrodictions/fein2019_verdict.md](../retrodictions/fein2019_verdict.md)
- Apparatus envelope: [quantum/effective_theory/apparatus_envelope.md](apparatus_envelope.md)
- Primitive 08 (multiplicity): [quantum/primitives/08_multiplicity.md](../primitives/08_multiplicity.md)

---

## 11. One-line summary

> **The two `D` variables in the ED framework — participation-ratio `D_P` (Primitive 08, matter-wave-testable) and PDE-coupling `D_E` (Q-C Boundary paper, likely temporal-platform-testable) — are distinct but monotonically related. The CANDIDATE affine mapping `D_E = (N·D_P − 1)/(N − 1)` resolves Problem 1 of `distinguishing_signatures.md` (the D_E < 0.1 regime IS reachable; Eibenberger and Fein both sit at D_E < 0.02). The V_c ≈ 0.304 prediction survives disambiguation essentially unchanged. Problem 2 (are the signatures temporal or spatial?) remains open and requires ED-Phys-16/17 archive work. The program now has a cleaner map of what's testable where: `D_P`-level predictions in matter-wave interferometry, `D_E`-level predictions in temporal-coherence platforms (cavity QED, superconducting qubits, optomechanics).**
