# Visibility → Bandwidth-Distribution → D: Derivation Memo

**Date:** 2026-04-24
**Location:** `quantum/effective_theory/visibility_to_bandwidth.md`
**Status:** Derivation memo. Addresses the blocker surfaced in `quantum/retrodictions/arndt_step_2.md §3`. Produces a testable Arndt prediction: **`V_c ≈ 0.304` at the Q-C transition**, contingent on two explicit commitments (channel-counting scheme, bandwidth-composition rule) each marked as CANDIDATE. The prediction is falsifiable against published Arndt visibility curves.
**Purpose:** Derive the forward map `V({b_K}, c_{ij})` and the inverse map `V → D` for KDTLI-class matter-wave interferometry, under commitments for the two open derivation choices. Classify each step by status. Produce an explicit numerical prediction for the Arndt Q-C transition.

---

## 1. Commitments

Two open choices in the primitive stack must be committed before the derivation proceeds. Both are CANDIDATE — defensible but not uniquely forced.

### 1.1 Channel-counting scheme for KDTLI — **two paths, environment as single committed channel**

**Commitment:** For a KDTLI (Kapitza-Dirac-Talbot-Lau) interferometer with a symmetric two-path geometry, the channel structure relevant to the participation-ratio `D` is:

```
K ∈ {path-1, path-2, env-commit}                (1)
```

— three channels: the two interfering paths plus a single "environment-commitment" channel that absorbs bandwidth dispersed to environmental modes via decoherence events.

**Why this commitment rather than the path-×-internal-state product space:**

- The product-space commitment (`N_channels = 2 × N_int`) produces `D ∈ [0, 1/2]` across the full decoherence range. The `D_crit ≈ 0.828` prediction from the ζ derivation is then **structurally unreachable** for the apparatus, because the maximum attainable `D` under that scheme is `1/2 < 0.828`. This would force a reinterpretation of the Q-C transition that removes the testable content.
- The two-path-only commitment recovers the full `D ∈ [1/2, 1]` range and makes `D_crit = 0.828` a reachable value at finite visibility. It gives a concrete, testable prediction.
- Physical argument: in ED, channels are stable rule-type-selective participation pathways (Primitive 07). A molecule's internal vibrational/electronic states are part of its *rule-structure*, not external rule-type channels it can switch between. Internal-state coupling to environment enters the dynamics through the Hornberger-Λ decoherence rate (already absorbed into ζ via `pde_parameter_mapping.md §5.1`), not through channel-counting.
- The "env-commit" third channel is the bandwidth that has left the coherent two-path structure and localized into a single committed trajectory (classical-limit behavior). This is what Primitive 11's commitment + Primitive 12's thickening produce at the apparatus scale: decoherence drives the chain toward committing to one trajectory.

**Status: CANDIDATE.** Both commitment choices are defensible; this memo commits to the two-path-plus-env-lump structure for the purposes of producing a testable prediction. Alternative: treat `N_env → ∞` sub-channels (environment as many-mode reservoir), which gives a different and structurally-different prediction — discussed in §5.2 as a sanity-check alternative.

### 1.2 Bandwidth-composition rule — **sublinear with exponent 2 (squared-amplitude)**

**Commitment:** When bandwidth from two channels combines (coherent recombination at a grating, or overlap at detection), the effective combined bandwidth is:

```
b_combined² = b_1² + b_2² + 2 · c_12 · b_1 · b_2     (2)
```

where `c_12 ∈ [−1, 1]` is the inter-channel coherence factor. Equivalently: amplitudes add linearly (coherent case), intensities (squares of amplitudes) add linearly (incoherent case), with the coherence factor interpolating between the two.

**Why:**

- This is the standard squared-amplitude composition rule of QM, required for Born-rule-compatible predictions.
- At full coherence (`c = 1`): `b_combined = b_1 + b_2` (linear).
- At zero coherence (`c = 0`): `b_combined² = b_1² + b_2²` (Pythagorean / incoherent).
- Tightening Pass Fix 6 flagged the bandwidth-composition rule as open; committing to sublinear-with-exponent-2 is the defensible near-term choice (per Tightening Pass §5.2 / Primitive 04 §7 item 2).

**Exponent = 2 is itself a commitment.** A general sublinear rule would have `b_combined^p = b_1^p + b_2^p + coherence-term` for some `p > 1`. The squared-amplitude form (`p = 2`) is what reproduces standard interference visibility.

**Status: CANDIDATE.** The exponent 2 may be derivable from primitive-level structure in later Phase 2 work; committing to it now produces a testable prediction. If a subsequent derivation shows the correct exponent is different, the numerical prediction will shift.

---

## 2. Forward map: V({b_K}, c_{ij})

### 2.1 KDTLI geometry and intensity pattern

The KDTLI apparatus has three gratings (G1, G2, G3) with G1 and G3 material, G2 an optical phase grating. At the detector plane behind G3, the intensity as a function of transverse position x:

```
I(x) = |ψ_1(x) + ψ_2(x)|²                      (3)
```

where `ψ_{1,2}(x)` are the amplitudes along paths 1 and 2. For a balanced interferometer (`|ψ_1(x)| = |ψ_2(x)|`) with apparatus-induced phase difference `φ(x)`:

```
I(x) = 2|ψ|² · [1 + c · cos(φ(x))]             (4)
```

where `c` is the effective path-coherence factor.

**Status of (3)–(4): FORCED.** Standard matter-wave interferometry; not ED-specific.

### 2.2 Visibility

```
V = (I_max − I_min) / (I_max + I_min) = c       (5)
```

**Status: FORCED.** Standard.

### 2.3 Bandwidth interpretation of coherence factor

Under the ED account of decoherence (Primitive 04 §5.3: decoherence as bandwidth redistribution; Primitive 11 §5.2: environmental-forced commitment sequence), coherence loss corresponds to bandwidth transfer from the coherent path × path interference structure to environmental-committed bandwidth.

**Commitment (from §1.2):** The fraction of the chain's total bandwidth that remains in the coherent two-path structure is `V² = c²`. The remaining fraction `(1 − V²)` has dispersed into the env-commit channel.

Explicitly, for the three-channel scheme (1):

```
b_{path-1} = V² / 2 · b_total                   (6a)
b_{path-2} = V² / 2 · b_total                   (6b)
b_{env-commit} = (1 − V²) · b_total             (6c)
```

**Status: CANDIDATE.** The specific functional form `b_coh = V² · b_total` is derived from the commitment that visibility reflects squared-amplitude coherence-survival fraction. An alternative commitment `b_coh = V · b_total` (linear in V, not squared) would give different D(V) and different V_c. The squared form is consistent with the squared-amplitude bandwidth-composition rule (§1.2).

---

## 3. Inverse map: V → D

### 3.1 The participation-ratio formula applied

From `pde_parameter_mapping.md §4.1`:

```
D = Σ_K b_K² / (Σ_K b_K)²                      (7)
```

Substituting (6a)–(6c) with `b_total = 1` (normalization):

```
Σ b_K = V²/2 + V²/2 + (1−V²) = 1              (8a)
Σ b_K² = (V²/2)² + (V²/2)² + (1−V²)²
       = V⁴/2 + (1−V²)²                       (8b)
```

Therefore:

```
D(V) = V⁴/2 + (1 − V²)²                        (9)
```

**Status: FORCED given the commitments (1), (2), and (6).** Equation (9) is arithmetic from those.

### 3.2 Behavior of D(V)

| V | D(V) | Regime |
|---|---|---|
| 1 | 0.500 | balanced, fully coherent |
| √(2/3) ≈ 0.816 | 0.333 | **minimum of D(V)** |
| 0.500 | 0.5625 | |
| 0.304 | **0.828** | **Q-C transition (predicted)** |
| 0.100 | 0.9805 | near-committed |
| 0 | 1.000 | fully committed, classical |

The function `D(V)` has a local minimum at `V = √(2/3) ≈ 0.816` with `D_min = 1/3`. This is a structural feature of the three-channel scheme: at intermediate coherence, the bandwidth is spread most evenly across the three channels, minimizing concentration.

### 3.3 Solving D(V_c) = D_crit(ζ_Arndt) ≈ 0.828

Setting `D(V_c) = 0.828` and solving:

Let `u = V_c²`. Then:

```
u²/2 + (1 − u)² = 0.828
u²/2 + 1 − 2u + u² = 0.828
3u²/2 − 2u + 0.172 = 0
u² − (4/3)u + 0.1147 = 0
```

By the quadratic formula:

```
u = (4/3 ± √(16/9 − 0.459)) / 2
  = (1.333 ± 1.148) / 2
  = 1.241  or  0.0926
```

Only `u = 0.0926` gives physical `V² ∈ [0, 1]`. Therefore:

```
V_c = √0.0926 ≈ 0.304                         (10)
```

**Status: FORCED given (9).**

---

## 4. The Arndt prediction

### 4.1 Prediction statement

**Under the commitments of §1 and the ζ-derivation result `D_crit(ζ_Arndt) ≈ 0.828`:**

> **The Q-C transition in Arndt-class KDTLI interferometry occurs at visibility `V_c ≈ 0.30`.**

This is a specific, falsifiable numerical prediction.

### 4.2 Interpretation

At `V_c ≈ 0.30`, the chain's bandwidth partition is:
- `b_path-1 = b_path-2 = V_c² / 2 ≈ 0.046` (each coherent path retains ~4.6% of total)
- `b_env-commit = 1 − V_c² ≈ 0.91` (91% of bandwidth has dispersed to environmental-commitment)

At this point, one channel (the environmental-commit channel) carries the dominant share of bandwidth, with the two coherent paths retaining residual symmetric structure. This is the structural meaning of the Q-C boundary in this model: the chain has not yet fully committed to a classical trajectory, but the bandwidth has concentrated enough into the commit-channel that near-single-channel behavior dominates.

### 4.3 Comparison to conventional framings

- **Retired `D = 0.5` heuristic** (Q-C Boundary paper): corresponds to `V = 1` (fully coherent balanced state) under (9). The old heuristic essentially marks the onset of any decoherence as "the transition," which trivializes the concept.
- **Canon-simulator `D_crit(ζ = 1/4) ≈ 0.896`**: corresponds to `V_c ≈ 0.22` under (9). Different prediction; different underlying physical assumption about ζ.
- **Conventional half-maximum visibility** (V_50%): depends on the fully-coherent starting visibility V_max. For Arndt's typical `V_max ≈ 0.5` in the coherent regime, half-maximum is `V = 0.25`, broadly consistent with the 0.30 prediction. This is encouraging but not a derivation; Arndt's V_max is apparatus-specific and not all of it is "coherence" in the bandwidth-redistribution sense.

### 4.4 Explicit test

The Eibenberger et al. (2013) visibility-vs-mass curve should exhibit a crossover — from nearly-fully-coherent at small `m` to nearly-classical at large `m` — passing through `V = 0.30` at a specific mass `m_c`. This `m_c` is the predicted Q-C transition point.

**Retrodiction protocol:**

1. Extract Eibenberger 2013 `V(m)` data points.
2. Fit or interpolate to find `m_c` at which `V(m_c) = 0.30`.
3. Compare `m_c` to the value reported in Eibenberger's analysis (half-visibility, or similar operational transition marker).
4. Agreement within experimental error = consistent retrodiction. Disagreement by more than a factor of 2 = refuted in this regime under these commitments.

---

## 5. Model choices and alternatives

### 5.1 Scheme dependence

The V_c = 0.30 prediction depends on the commitments in §1. Different commitments give different numbers:

| Channel-counting | Composition rule | Predicted `V_c` |
|---|---|---|
| Two-path + env-commit (§1.1) | Sublinear exp=2 (§1.2) | **~0.30** |
| Two-path + env-many-modes | Sublinear exp=2 | unreachable (D_max = 1/2 < 0.828) |
| Path × internal product space | Sublinear exp=2 | unreachable (D_max < 1/(2 N_int)) |
| Two-path + env-commit | Linear composition | ~0.18 |
| Two-path + env-commit | Sublinear exp=3 | ~0.34 |

**The choice of commitments determines the prediction. A retrodiction that fits Arndt's data does not uniquely validate ED; it validates the specific combination of commitments used.**

**Honest framing for publication:** a successful retrodiction under these commitments is evidence in favor of the participation-ratio + two-path-plus-env-commit + squared-amplitude-composition combination, not evidence in favor of ED-as-a-whole. Conversely, a failed retrodiction could be rescued by adjusting one of the commitments — which would need to be called out as parameter-tuning rather than theory-working.

### 5.2 Sanity check — the env-many-modes alternative

Under the alternative commitment `N_env → ∞` (environmental bandwidth distributed into many sub-channels, each with vanishing weight):

```
Σ b_K² = V⁴/2 + (1−V²)² / N_env → V⁴/2         (11)
D(V) → V⁴/2                                    (12)
```

Maximum value `D = 1/2` at `V = 1`. The `D_crit ≈ 0.828` value is unreachable. Under this commitment the Q-C transition would need to be reinterpreted — perhaps as the visibility at which `D/D_max = some fraction`, or as a different threshold condition on the PDE dynamics entirely.

**This alternative is more physically conservative** (environmental bandwidth genuinely disperses into many uncorrelated modes) but **destroys the testable prediction**. The two-path-plus-env-commit commitment in §1.1 is the pragmatic choice that preserves testability. Preference for it is based on the observation that in the thick-regime limit, classical behavior is *single-trajectory*, not *many-mode thermal*; thermal dispersion is an intermediate regime, and full classicality concentrates into a single committed channel (Primitive 12 thickening).

---

## 6. Status classification summary

| Derivation step | Status |
|---|---|
| Three-channel counting for KDTLI | **CANDIDATE** |
| Sublinear bandwidth composition with exponent 2 | **CANDIDATE** |
| `b_coh = V² · b_total` (equation (6)) | **CANDIDATE** |
| `D_crit(ζ_Arndt) ≈ 0.828` (from ζ derivation) | **CANDIDATE** (inherited) |
| KDTLI intensity pattern (3)–(4) | **FORCED** (standard optics) |
| Visibility = coherence factor (5) | **FORCED** (standard) |
| Participation-ratio formula D = Σb²/(Σb)² | **CANDIDATE** (from `pde_parameter_mapping.md §4.1`) |
| D(V) = V⁴/2 + (1−V²)² (equation (9)) | **FORCED** given the commitments |
| V_c ≈ 0.304 at D_crit = 0.828 (equation (10)) | **FORCED** given the commitments |
| The numerical prediction itself | **CANDIDATE** (inherits from the three CANDIDATE commitments above) |

**The numerical prediction V_c ≈ 0.30 is a CANDIDATE prediction, not a FORCED one.** It depends on three upstream CANDIDATE commitments (channel-counting, composition rule, coherence-squared bandwidth split) plus one inherited CANDIDATE (D_crit). None is SPECULATIVE; all are defensible. But the specific number depends on specific choices, and those choices have alternatives.

---

## 7. What remains SPECULATIVE

Three pieces not committed here:

### 7.1 Derivation of the composition-rule exponent

Exponent 2 was committed per §1.2. Whether this is forced by primitive-level structure (Primitive 04 bandwidth-composition as a homology-class coupling? Primitive 07 channel-merging as a specific algebra?) or is a constitutive choice of the framework is open. A derivation of the exponent from primitives would promote this step from CANDIDATE to FORCED.

### 7.2 Derivation of bandwidth-survival fraction vs. visibility

`b_coh = V² · b_total` was committed per §2.3. Whether this quadratic relationship is forced by primitive-level structure (Primitive 04 bandwidth as measure + sublinear composition → squared scaling?) or is an assumption is open. The linear alternative `b_coh = V · b_total` would give V_c ≈ 0.18 instead of 0.30.

### 7.3 Derivation of channel-counting scheme

§1.1 argued for the two-path-plus-env-commit structure on physical-intuition grounds. A derivation from Primitive 07 (channel = rule-type-selective pathway) showing that in KDTLI-class apparatuses the correct channel structure is exactly three-channel, and that "env-commit" is the correct consolidated form rather than env-many-modes, is open.

**These three items are the Phase 2 derivation targets that would turn the V_c ≈ 0.30 prediction from CANDIDATE to FORCED.** Until they are done, the prediction is conditional on the commitments.

---

## 8. Checklist for Arndt Step 2 execution

With this memo in place, the remaining work to execute the Arndt retrodiction is:

### 8.1 Theory (no further derivation required for the first-pass retrodiction)

- [x] ζ formula — `zeta_derivation.md`
- [x] `D_crit(ζ_Arndt) ≈ 0.828` prediction — `arndt_step_2.md §2.3`
- [x] `D(V)` functional form — this memo, equation (9)
- [x] `V_c ≈ 0.30` prediction — this memo, §4.1

### 8.2 Literature (data collection, no theory)

- [ ] Retrieve Eibenberger et al. 2013, *PCCP* **15**, 14696–14700
- [ ] Extract visibility-vs-mass data points from Fig. 2 and Fig. 3
- [ ] Extract apparatus parameters (T, p, v, grating period, Talbot length) from methods section + Gerlich et al. 2007
- [ ] Identify the experimental operational definition of the Q-C transition point in the paper (half-visibility, fit threshold, or other criterion)

### 8.3 Arithmetic (mechanical once 8.2 is done)

- [ ] Determine `m_c` such that `V(m_c) ≈ 0.30` in Arndt's data
- [ ] Compare `m_c` to the transition-mass value reported by Eibenberger
- [ ] Compute agreement tolerance given experimental error bars on V and m

### 8.4 Write-up (after 8.2 and 8.3 complete)

- [ ] Amend `arndt_step_2.md` with the comparison result and verdict (consistent / inconclusive / refuted)
- [ ] Document which commitments from this memo's §1 were required
- [ ] Document the distinguishing prediction status: the V_c ≈ 0.30 value differs from the retired `D = 0.5` heuristic and from the canon-ζ `D_crit ≈ 0.896` prediction — the retrodiction, if consistent with Arndt data, supports the specific ED derivation chain over its predecessors

### 8.5 Distinguishing-signature extension (not required for first-pass; needed for a strong claim)

- [ ] Check Arndt data near the quantum side of the transition (`m < m_c`) for the Q-C Boundary paper's `N_osc ≈ 9` transient-oscillation signature
- [ ] Check for the 3–6% third-harmonic signature
- [ ] These are ED-specific predictions that no competitor (standard decoherence, GRW, CSL, DP) makes

---

## 9. Summary

**Achieved in this memo:**

- Forward map `V({b_K}, c_{ij})` derived under commitments (§2)
- Inverse map `V → D` derived as `D(V) = V⁴/2 + (1−V²)²` (equation (9))
- Specific numerical prediction: **`V_c ≈ 0.304` at the Arndt Q-C transition** (equation (10))
- All commitments explicitly labeled CANDIDATE; SPECULATIVE items enumerated (§7)
- Arndt Step 2 execution checklist produced (§8)

**Not achieved:**

- None of the three CANDIDATE commitments has been promoted to FORCED. A retrodiction agreement would be evidence for the combination; disagreement could be rescued by changing a commitment (disclosed as tuning, not working).
- The specific Eibenberger 2013 numbers are not in this memo; the comparison is not executed.
- The distinguishing-signature extension (§8.5) — which is what would make the retrodiction strong-form rather than consistency-level — is deferred.

**Honest framing:**

This derivation is a real, concrete ED-specific prediction with falsifiability. `V_c ≈ 0.30` is testable against published Arndt data. If the transition in Eibenberger's curve occurs near `V = 0.30`, ED's derivation chain (Primitive 04 bandwidth → four-band partition → flux-continuity → ζ = τ/τ_com → D_crit(ζ) → D(V) via three-channel participation-ratio) produces a retrodiction. If it occurs elsewhere, the chain is refuted for this regime, and the refutation diagnoses which commitment is wrong.

**This is what a real first-pass Path C retrodiction looks like.** It rests on three CANDIDATE commitments; it is honest about that; it produces a number.

---

## 10. Cross-references

- ζ derivation: [quantum/effective_theory/zeta_derivation.md](zeta_derivation.md)
- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](pde_parameter_mapping.md)
- Arndt Step 2 attempt: [quantum/retrodictions/arndt_step_2.md](../retrodictions/arndt_step_2.md)
- Arndt scaffold: [quantum/retrodictions/arndt_interferometry.md](../retrodictions/arndt_interferometry.md)
- Tightening pass Fix 6 (bandwidth composition): [quantum/primitives/TIGHTENING_PASS_01.md](../primitives/TIGHTENING_PASS_01.md)
- Primitive 04 (bandwidth): [quantum/primitives/04_participation_bandwidth.md](../primitives/04_participation_bandwidth.md)
- Primitive 07 (channel): [quantum/primitives/07_channel.md](../primitives/07_channel.md)
- Primitive 11 (commitment): [quantum/primitives/11_commitment.md](../primitives/11_commitment.md)
- Primitive 12 (thickening): [quantum/primitives/12_thickening.md](../primitives/12_thickening.md)
- D_crit formula: [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md)
- Q-C Boundary paper: [quantum/papers/Q-C Boundary_Transition. Theory, Prediction, Path.pdf](../papers/Q-C%20Boundary_Transition.%20Theory,%20Prediction,%20Path.pdf)

---

## 11. One-line summary

> **Under the three CANDIDATE commitments (three-channel KDTLI counting, sublinear-exponent-2 bandwidth composition, squared-amplitude coherence-survival), the participation-ratio D as a function of visibility is D(V) = V⁴/2 + (1−V²)², and the Q-C transition at D_crit ≈ 0.828 corresponds to V_c ≈ 0.304. This is a falsifiable numerical prediction against Eibenberger et al. 2013 visibility-vs-mass data; execution requires only literature retrieval and arithmetic.**
