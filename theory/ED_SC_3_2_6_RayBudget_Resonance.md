# ED-SC 3.2.6 — Ray-Budget Resonance Diagnostic

**Status:** Pre-registered — execution pending
**Parent:** `theory/ED_SC_3_2_5_G3_G4_Transition.md`
**Scope reference:** `theory/ED_SC_3_0_Scope.md` rev. 2 §5.2
**Simulator of record:** `r2_grf_falsifier_tests.py` +
`ED_Update_Rule.ed_step_mobility`
**Driver:** `analysis/scripts/ed_sc_3_2_6_resonance_scan.py`
**Outputs:** `outputs/ed_sc_3_2_6/resonance_summary.json`

---

## 1. Purpose

ED-SC 3.2.5 resolved the G3→G4 transition of the coarse scan into
**two sharp shoulders** separating three locally stable plateaus:

- Transition 1 at `L_ray/ξ ≈ 1.50` (absolute `L_ray ≈ 2.64` lu)
- Transition 2 at `L_ray/ξ ≈ 2.10` (absolute `L_ray ≈ 3.69` lu)

(using `ξ = 1.758` lu from `outputs/ed_sc_3_1/xi_canonical.json`.)

**Hypothesis** (pre-registered). These are **integer-lattice-shell
resonances** of the 4-ray motif filter (`N_req = 4`). Under the
canonical filter, each admitted saddle contributes four ray
endpoints at lattice offsets `(round(e·L_ray_i), round(e·L_ray_j))`
from the saddle centre, where `e ∈ {e_neg, e_pos}`. As `L_ray`
grows, these endpoint offsets transition through integer-valued
lattice shells (radii `√2 ≈ 1.41`, `2`, `√5 ≈ 2.24`, `√8 ≈ 2.83`,
`3`, `√10 ≈ 3.16`, …). Each shell-crossing reconfigures the
admitted-motif set in an integer-valued jump and produces a step
in `f(ρ | ξ, filter)`.

The transitions at `L_ray ≈ 2.64` and `≈ 3.69` are consistent with
ray endpoints crossing the √8 → 3 shell boundary (≈ 2.83–3.0)
and the √13 → 4 or √14 → 4 shell boundary (≈ 3.6–4.0),
respectively. This memo tests that correspondence explicitly.

ED-SC 3.3 is blocked until this memo delivers a verdict.

---

## 2. Operating grid (sub-lattice resolution)

Two sub-lattice windows bracketing the two shoulders:

- **Window A:** `L_ray ∈ [2.50, 2.80]` at `Δ = 0.02` — 16 points
- **Window B:** `L_ray ∈ [3.50, 3.90]` at `Δ = 0.02` — 21 points

Converting to `L_ray/ξ` with `ξ = 1.758`:

- Window A: `L_ray/ξ ∈ [1.422, 1.593]`
- Window B: `L_ray/ξ ∈ [1.991, 2.219]`

The user-specified 32-point total is extended to 37 to keep
both windows symmetric around the nominal shoulder (2.64 is
interior to A; 3.69 is interior to B). No meaningful compute
cost — the 10-seed field cache is shared across all points.

---

## 3. Simulator of record

- **File:** `analysis/scripts/ed_arch_r2/r2_grf_falsifier_tests.py`
- **Step rule:** `ED_Update_Rule.ed_step_mobility`
- **Canonical parameters (read-only from `fr.*`):**
  - α = 0.03, γ = 0.5, σ = 0.0556
  - M(p) = (1 − p)^{2.7}
  - steps = 500, DT = 0.05
  - size = 64 × 64, boundary = periodic
  - p_min = 0.01, p_max = 1.0
- **Seeds (10):** {77, 101, 123, 234, 456, 789, 1011, 1213, 1415, 2021}
- **Module constants not mutated.** ED-SC 3.1 rev. 2 §6 guardrail
  applies.

---

## 4. Filter geometry

- α_filt = 0.25
- N_req = 4
- Saddle detection: `fr.find_morse_saddles(E)` on smoothed field
  `E = fr.smooth_field(p)`
- Motif admission: `fr.motif_pass(s, E, p_hat, p_std, α_filt,
  L_ray_val, N_req)` — only `L_ray_val` varies.
- Four principal-axis rays per saddle with endpoint offsets
  `(round(e_x · L_ray), round(e_y · L_ray))` for
  `e ∈ {e_neg, e_pos}` and signs `±`.

---

## 5. Protocol

### 5.1 Per grid point

For each `L_ray` in windows A and B:

1. Use the shared 10-seed field cache
   (evolve once, re-use across all grid points).
2. For each seed: compute smoothed E, `p_hat`, `p_std`;
   detect Morse saddles.
3. Apply motif filter at this `L_ray`; admit saddles passing
   `N_req = 4`.
4. For every admitted motif, record:
   - seed
   - saddle centre `(i, j)`
   - eigenvalues `λ₁, λ₂` (as `lam_neg`, `lam_pos`)
   - ratio `ρ = max(|λ|)/min(|λ|) · sign`
   - **four ray-endpoint integer offsets**
     `(di_k, dj_k), k ∈ {1,2,3,4}` — lattice coordinates
     relative to the saddle centre
   - **four endpoint shell radii**
     `r_k = √(di_k² + dj_k²)`
5. Pool ratios across seeds; bootstrap S1 (median), S2 (IQR),
   S3 (upper-tail log-slope) with 4000 resamples.
6. Aggregate the set of shell radii `{r_k}` across all admitted
   motifs and compute its empirical histogram.

### 5.2 Per-seed ξ guardrail (rev. 2 — canonical method)

**ξ_seed must be computed using the canonical 40-snapshot average
method (matching ED-SC 3.1 rev. 2). Single-snapshot ξ is not
permitted for guardrail evaluation.**

Specifically, per-seed ξ is computed identically to
`analysis/scripts/ed_sc_3_1_xi_canonical.py`:

- **Channel:** density field `p` (primary; *not* the smoothed
  field `E`).
- **Decay definition:** GR-SC 1.7 radial half-decay of the 2D
  autocorrelation
  `C(r) = FFT⁻¹{|FFT(p − ⟨p⟩)|²} / N²`, normalised so `C(0) = 1`,
  with `ξ` the first integer-radius crossing of `C(r) = 0.5`
  (linear-interpolated).
- **Snapshotting:** burn-in of 100 steps, then snapshot every
  10 steps for the remaining 400 steps → **40 snapshots per seed**.
- **Per-seed ξ:** arithmetic mean of `xi_halfdecay` across the
  40 snapshots (NaN-safe).
- **Guardrail:** require

  \[
  \frac{|\xi_{\text{seed}} - 1.758|}{1.758} < 0.20
  \]

  on ≥ 9 of 10 seeds.

Single-snapshot ξ measured on the final-step field is a
systematically shorter, noisier statistic and is **explicitly
disallowed** for guardrail purposes. (ED-SC 3.2.6 v1 failed the
guardrail 9/10 solely because of this methodology mismatch; the
underlying field is canonical.)

Violation of the guardrail under the canonical method invalidates
the resonance diagnostic and forces a re-anchor of `ξ_canonical`.

### 5.3 Resonance verdict

Confirmed if all three conditions hold:

- **(R1)** Each S2 jump larger than `3×` the median neighbouring
  derivative in its window coincides (within `ΔL_ray ≤ 0.04`) with
  the crossing of an integer-lattice shell by one or more principal
  ray endpoints.
- **(R2)** On each side of a detected jump, the dominant shell
  radii `{r_k}` histogram differs by at least one integer shell,
  and the admitted-motif count `N` steps in an integer-valued way.
- **(R3)** The plateau structure (A: pre-1.5 plateau vs post-1.5
  plateau; B: pre-2.1 plateau vs post-2.1 plateau) is stable across
  each plateau's interior, with |dS1| and |dS2| per step below the
  median derivative outside the resonance neighbourhood.

Refuted if R1 fails, or if R1 passes but R2/R3 reveal smooth
drift inside the windows rather than plateau-jump-plateau.

---

## 6. Deliverables

- `analysis/scripts/ed_sc_3_2_6_resonance_scan.py` — driver.
- `outputs/ed_sc_3_2_6/resonance_summary.json` — master summary:

  ```
  {
    "method": "...",
    "simulator": "...",
    "xi_canonical_lattice_units": 1.7575...,
    "xi_guardrail": { "pass": bool, "per_seed": {...} },
    "window_A": {
      "L_ray_grid": [...],
      "L_ray_over_xi_grid": [...],
      "per_grid": {
        "Lray_2.50": {
          "N_motifs": ...,
          "S1_median": ..., "S1_ci16_84": [...],
          "S2_iqr": ...,    "S2_ci16_84": [...],
          "S3_tail_slope": ...,
          "endpoint_shell_radii": [...],
          "shell_histogram": { "1.0": k, "1.414": k, ... },
          "pool_ratios": [...],
          "per_motif": [ { "seed":..., "i":..., "j":..., "lam_neg":..., "lam_pos":..., "ratio":..., "endpoints":[[di,dj,r],...] }, ... ]
        },
        ...
      }
    },
    "window_B": { ... },
    "resonance_verdict": "Confirmed" | "Refuted",
    "wall_seconds_total": ...
  }
  ```

- Per-grid CSV export on demand (optional, disabled by default to
  keep the tree clean; the JSON contains all per-motif rows).

---

## 7. Registered interpretation

This memo does **not** evaluate S-F2. S-F2 was already re-scoped in
ED-SC 3.0 rev. 2 §5.1 as a within-regime tolerance. The purpose
of this memo is solely to determine whether the G3→G4 and G4→G5
jumps are caused by discrete ray-budget geometry (integer lattice
shells) or by some other mechanism.

A **Confirmed** verdict means ED-SC 3.3 must pre-register
"resonance windows" as forbidden operating regions for its
α_filt / N_req sweeps. A **Refuted** verdict means the resonance
explanation fails and a separate mechanism hunt must be opened.
Either way, ED-SC 3.3 unblocks **after** this memo's verdict.

---

## 8. Next steps (decision tree)

- **Confirmed:** open ED-SC 3.3 pre-registration with the
  resonance-window exclusion list derived from the shell
  histogram. Cite this memo's verdict.
- **Refuted:** open `theory/ED_SC_3_2_7_Mechanism_Hunt.md`
  to investigate alternative causes (candidate: p̂-drift under
  large L_ray; candidate: smoothing-kernel aliasing at large
  endpoint offsets).

Either way, ED-SC 3.1 rev. 3 minor patch follows, citing
ED-SC 3.2.5 plateau certification and this memo's verdict as
the canonical-operating-point stability evidence.
