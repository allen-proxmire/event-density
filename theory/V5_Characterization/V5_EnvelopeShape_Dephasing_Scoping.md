# Arc: V5's spatial envelope shape from phase dephasing (fresh angle)

**Opened 2026-07-08** at AP's direction. Crank-rail ON. This is the last open structural piece of V5 (existence = P10 posit, retardation = P11-forced, gauge phase = P05+P09, attractive sign = derived this session; the envelope SHAPE and the reach VALUE remain). Known-hard: the `V5_Envelope_Shape_From_P11_Scoping.md` thread ran four passes and was DOWNGRADED.

## Why this is a fair next attempt, not a rehash

The earlier thread's wall (its own final verdict): it framed V1/V5 as the Green's function of a **passively diffusing field**, which fails because the certified substrate has no passive spreading (`rho` changes ONLY where fronts commit; the update is discrete winner-take-all, not diffusion). Its closing recommendation: "a fair next attempt should start from the substrate's actual character, discrete, competitive, trajectory-based, rather than importing continuum field-theory machinery by analogy."

This angle does exactly that, and it is enabled by work that did not exist when that thread ran:
- **V5's coupling IS the cross-chain coherence** (closed this session, `V5_ForwardDerivation_Scoping.md` G1). So V5's spatial envelope `F_V5(σ/ℓ_V5²)` is simply how the cross-chain coherence `C(r)` decays with separation `r`. No field-diffusion analogy needed.
- **The decay mechanism is trajectory-based dephasing.** In the Step 3/4 probes (`p12_phase_coherence_probe_v2_intrinsic.py`), the P05 connection carries quenched substrate disorder that random-walks the transported phase along the active-front growth paths. This is precisely the "discrete, competitive, trajectory-based" character the old verdict called for, applied to V5 (cross-chain), not V1 (single-chain self-memory, which has no seat in the certified code).

So this is not the failed passive-field route; it is the old verdict's own recommended direction, now runnable because V5's coupling has been identified with the coherence.

## The claim (precise)

**V5's spatial envelope `F_V5` is exponential (shape form-forced), with scale `ℓ_V5 = ξ` set by the substrate's quenched-disorder variance (value-inherited).**

**Mechanism / analytic backing.** The cross-chain coherence between two chains at separation `r` is `C(r) = ⟨cos(Δφ)⟩`, where `Δφ` is the relative phase after transport of the P05 holonomy along the connecting path (the gauge-invariant, connection-dressed phase from the G1 result). For quenched disorder with approximately independent zero-mean per-edge holonomy increments, the accumulated `Δφ` over a path of `r` edges is approximately Gaussian with variance `V(r) ∝ r` (sum of independent variances). The characteristic function of a Gaussian gives
`C(r) = ⟨cos Δφ⟩ = e^{−V(r)/2}`,
so `V(r) ∝ r ⟹ C(r) = e^{−r/(2ξ)}`, a pure exponential, with `ξ` set by the per-edge variance `D`: `ξ = 1/D` (in the `V(r)=Dr` normalization, `C=e^{−Dr/2}`, `ξ=2/D`). Exponential SHAPE forced by dephasing; SCALE inherited from the disorder. This is the same "form-forced, value-inherited" pattern as everywhere else in ED, and it matches Paper_090's own statement that `F_V5`'s form is structural while `ℓ_V5` is inherited.

**Note vs the earlier exponential guess.** The old thread also guessed exponential, but from P11-as-a-gap in a diffusion equation, which failed empirically (the diffusion equation does not govern the substrate). This derivation routes the exponential through DEPHASING of a transported phase, a different and substrate-faithful mechanism, and it is directly testable because `C(r)` is an observable the probes already produce.

## The test (build)

Use the edge-adjacent dephasing probe (reach = nearest-neighbor deposition, so there is NO imposed spatial envelope; any decay of `C(r)` is emergent from dephasing, not put in by hand). Measure, over a large grid, single seed, no thermal noise, several disorder strengths `κ`:
1. **`C(r) = ⟨cos(φ_i − φ_j)⟩`** binned by distance (the envelope).
2. **`V(r) = Var(φ_i − φ_j)`** binned by distance (the accumulated dephasing).
3. **Dephasing relation:** is `C(r) ≈ e^{−V(r)/2}`? (tests the mechanism directly, not just the shape).
4. **Shape:** is `V(r) ∝ r` (→ exponential `C`), or `∝ r²` (→ Gaussian), or sublinear (→ stretched)? Fit `ln C(r)` vs `r` over the positive-`C` range for `ξ`.
5. **Scale law:** `ξ(κ)`. Dephasing predicts `ξ ∝ 1/κ²` (holonomy `∝ κ`, variance `∝ κ²`). Compare.

## Honest expectations + crank caveats (named up front)

- The Step-3 data already shows the naive exponential is INCOMPLETE: `C(r)` dips slightly NEGATIVE at mid-range (e.g. `C(12)≈−0.02`), which a pure exponential (always positive) cannot produce. So expect exponential-at-short-range with a real deviation to characterize (anti-correlation, damped-oscillatory, or path-geometry effect), not a clean textbook exponential.
- The Step-3 `ξ(κ)` (κ=0.5→ξ≈5, κ=2→ξ≈2) does NOT match `ξ ∝ 1/κ²` (would predict a 16× drop, observed ~2.5×). So the per-edge increments are likely NOT independent (front paths are correlated, the quenched field is spatially structured, or accumulation is sub-diffusive). This is the real thing to diagnose, and a mismatch is informative, not a failure.
- **Scope:** this addresses V5's SPATIAL envelope only. The TEMPORAL envelope `F_V5(Δt/τ_V5)` (memory decay) and V1's single-chain self-memory envelope remain separate and open (the latter has no seat in the certified code, per the earlier thread's fourth pass).
- **Best realistic outcome:** shape forced to an exponential FAMILY (possibly stretched/damped), scale inherited, mechanism (dephasing) confirmed via the `C ≈ e^{−V/2}` relation. Partial win acceptable and expected.
- Tier target: MEASURED for the shape/mechanism on the polarity-extended rule; do NOT claim the bare kernel `F_V5` is derived from nothing.

---

## Build 1 (DONE 2026-07-08) — the clean dephasing-exponential claim is NOT confirmed; the envelope is domain-correlation (partial/negative)

`v5_envelope_shape_probe.py` (reuses the certified edge-adjacent dephasing `run_fill` verbatim; 80×80, single seed, no thermal noise, no imposed envelope; measures `C(r)`, the exponential fit, the shape exponent `α` via `V_eff=-2\ln C ~ r^α`, the C<0 onset, and the `ξ(κ)` scale law).

**Results.**

| κ_bw | exp-fit R² (ln C vs r) | shape α | C<0 onset r | exp-fit ξ |
|---|---|---|---|---|
| 0.3 | 0.89 | 1.38 | 17 | 4.85 |
| 0.5 | 0.945 | 1.33 | 12 | 3.76 |
| 1.0 | 0.83 | 0.68 | 7 | 10.6 (unreliable) |
| 2.0 | 0.57 | 0.71 | 5 | 6.15 (unreliable) |

Scale law: `ξ(κ)` log-log slope = **+0.28** (dephasing predicts −2.0), and ξ is non-monotonic (fits unreliable once R² drops).

**Three findings, honest.**
1. **The mid-range NEGATIVE dip is robust and fatal to the pure-exponential/pure-dephasing model.** `C(r)` crosses zero and goes weakly negative (≈ −0.08) at the domain scale in every run. A pure exponential (or any monotone dephasing decorrelation) is strictly positive; it cannot produce anti-correlation. So the envelope is NOT a screened-propagator exponential.
2. **The short-range decay is only approximately exponential, and Gaussian-leaning.** At low disorder the positive-range exponential fit is decent (R²≈0.9) but `α≈1.3–1.4`, between exponential (1) and Gaussian (2): a mildly-super-exponential coherent core, not the clean `α=1` independent-increment dephasing prediction. At high disorder `α<1` (stretched) and the field is nearly white within 1–2 steps.
3. **The dephasing scale law fails.** `ξ ∝ 1/κ²` is not observed (slope +0.28, wrong sign; even the reliable low-κ points 4.85→3.76 for κ 0.3→0.5 do not match the predicted 2.8× drop). So the reach is not controlled by simple independent-increment phase variance.

**What this DOES characterize (the positive residue).** V5's spatial envelope is the **correlation function of a finite phase domain**, the Knots-safe finite-reach structure established in Step 4: an approximately-exponential core within the domain (ξ≈4–5 at moderate disorder), a zero-crossing at the domain scale, a weak anti-correlation dip, then a flat-zero tail. This is a domain-correlation shape (competitive front growth + quenched-disorder dephasing produce finite domains), not a screened Yukawa exponential. The scale ξ is inherited (set by disorder), consistent with 090.

**Tier verdict: PARTIAL / mostly-NEGATIVE.** The clean claim ("F_V5 exponential, forced by independent-increment dephasing, ξ∝1/κ²") is refuted: the negative dip, α≠1, and the failed scale law all say the simple dephasing derivation does not control the full envelope. What survives is a characterization, not a derivation: the envelope is domain-correlation with an approximately-exponential core, scale inherited. The envelope-SHAPE question remains OPEN (now on its fifth pass), but is narrowed: it is not a screened-propagator exponential; it is the correlation function of the substrate's finite phase domains, whose own shape (core exponent + domain-scale zero-crossing) is set by the competitive growth dynamics, not by a clean gap/dephasing law. Consistent with the earlier thread's four negatives: the envelope keeps resisting a clean closed-form derivation.

**Honest next options (not yet run):** (1) measure the domain-size distribution directly and ask whether the zero-crossing scale, not a fit-ξ, is the physical reach (a cleaner observable than the exponential fit); (2) separate the coherent core from the domain structure (the α≈1.3 core may have its own clean law even though the full C(r) does not); (3) accept the partial characterization and mark the closed-form shape as a standing open item. Do NOT force an exponential onto data that shows a zero-crossing.

## Saddle-geometry connection (AP hunch, 2026-07-08) — a real bridge, not (yet) a derivation

AP flagged that the corpus's saddle-geometry / saddle-invariance ideas may link to the envelope. They do, at the conceptual level, and it explains the negative result. The envelope `C(r)` is a **two-point correlation of a field with domain (basin/saddle) structure**; such correlations generically have a zero-crossing at the basin/saddle spacing, which is exactly why the envelope is domain-correlation rather than a screened exponential. The corpus already has the machinery for this object:
- **SC-4.9 / `Paper_ED_Dyn_01_SaddleDynamics`**: Morse/Hessian classification of the ED field's topography (motifs = `find_morse_saddles` centers; S1 basin / S2 saddle / S3 dome by Hessian signature; a characteristic length `ℓ_saddle`).
- **arc-SC 3.4 two-point (`ED_SC_3_4_twopoint`) / GR-SC redshift**: the two-point correlation `C_redshift(r) = 2[1 − ξ_φ(r)/σ₀²]` between saddle-centered motifs, with a half-rise scale `r_½`. This is the SAME kind of object as the envelope `C(r)`; the envelope's zero-crossing scale ↔ `ℓ_saddle` / `r_½`.

**Reframe:** V5's envelope shape = the two-point correlation of the coherence field's basin/saddle geometry; reach ~ characteristic saddle spacing.

**Two blockers keep this a bridge, not a derivation (crank rail):**
1. **Uncalibrated simulators.** The saddle/two-point machinery lives on the MOBILITY-PDE engine (`ED_Update_Rule.ed_step_mobility`); the envelope was measured on the certified discrete Σ-participation graph. No established shared length scale between them (open-targets map item #9). So the link is cross-substrate ANALOGY, and making it a derivation depends on solving that calibration problem (a separate hard open item).
2. **Documented saddle-invariant negatives.** The r* motif-conditioned saddle-ratio was CLOSED as not a real invariant (`Universal_Invariants.md`: R²≈−1.88, a filter-conditioned GRF-linearization statistic, not a derivation); the field is non-Gaussian in phases (GRF-Gaussianity test). So "a saddle-conditioned invariant pins the envelope" has failed once and carries a caution.

**Possible within-substrate test (self-contained, avoids blocker 1):** Morse-classify the certified coherence field directly, find its basins/saddles, and check the characteristic saddle spacing equals the envelope's zero-crossing scale. Likely re-expresses the domain finding in saddle language rather than deriving the shape (the domains ARE the basins), but would confirm the reframe on one substrate. Not run; recorded as a lead.
