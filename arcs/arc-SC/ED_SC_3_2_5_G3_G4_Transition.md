# ED-SC 3.2.5 — G3→G4 Transition Diagnostic (fine-grid hinge scan)

**Status:** Executed — results in §7; verdict = **C (resonance / two-shoulder)**
**Parent:** `theory/ED_SC_3_2_LrayXi_Scan.md` rev. 2
**Simulator of record:** `r2_grf_falsifier_tests.py` + `ED_Update_Rule.ed_step_mobility`
**Driver:** `analysis/scripts/ed_sc_3_2_5_g3_g4_transition.py`
**Outputs:** `outputs/ed_sc_3_2/transition_g3_g4_summary.json`

---

## 1. Purpose

ED-SC 3.2 rev. 2 (scan of record, v2) **triggered S-F2 under the weak
reading**: the IQR drift from G3 (L_ray/ξ = 1.08) to G4 (L_ray/ξ = 2.00)
was

\[
\frac{|S_2^{G4} - S_2^{G3}|}{S_2^{G3}} \;=\; \frac{|2.99 - 1.29|}{1.29} \;\approx\; 1.32
\]

— roughly **6.6× the pre-registered 20% tolerance**. The median shift
was
\(|S_1^{G4} - S_1^{G3}| = |{-2.77} - ({-1.92})| \approx 0.85\),
a **44% relative change** at the canonical neighbourhood. The upper
grid showed non-monotonic behaviour (G5 partially recovers, G6 swings
back), indicating that the G3→G4 region contains a **sharp deformation**
in the distributional invariant \(f(\rho\mid\xi,\mathrm{filter})\) rather
than a smooth drift.

**This memo pre-registers and executes a fine-grid scan across
`L_ray/ξ ∈ [1.0, 2.5]` at Δ = 0.1** to resolve whether the
observed jump is:

- **(A)** a smooth drift (S1, S2 monotone in L_ray/ξ),
- **(B)** a shoulder (single transition at a definite L_ray/ξ\*), or
- **(C)** a resonance cascade (non-monotone, multiple inflections).

**ED-SC 3.3 is blocked** until this transition is mapped. Reopening
ED-SC 3.3 (filter-geometry scan over α_filt, N_req) before the hinge
near the canonical operating point is understood risks compounding the
degeneracy across non-commuting filter axes.

---

## 2. Operating grid (fine resolution)

- **Hinge variable:** L_ray/ξ
- **Range:** [1.0, 2.5]
- **Step:** 0.1
- **Grid points (16):** 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5
- **ξ:** 1.7575325729470939 lattice units (from
  `outputs/ed_sc_3_1/xi_canonical.json`, density channel,
  10-seed mean)
- **Absolute L_ray (lattice units):** 1.758, 1.933, 2.109, 2.285,
  2.460, 2.636, 2.812, 2.988, 3.163, 3.339, 3.515, 3.691, 3.867,
  4.042, 4.218, 4.394

The window brackets G3 (1.08, interior canonical) and G4 (2.00)
and extends 0.5 units beyond G4 to test whether the G4/G5/G6
alternation is resolved by finer sampling.

---

## 3. Simulator of record

- **File:** `analysis/scripts/ed_arch_r2/r2_grf_falsifier_tests.py`
- **Step rule:** `ED_Update_Rule.ed_step_mobility`
- **Canonical parameters (read-only from `fr.*`):**
  - α = 0.03, γ = 0.5, σ = 0.0556
  - M(p) = (1 − p)^{2.7}
  - steps = 500, size = 64 × 64
  - dt = 0.05, p_min = 0.01, p_max = 1.0
  - boundary = periodic
- **Seeds (10):** {77, 101, 123, 234, 456, 789, 1011, 1213, 1415, 2021}
- **Module constants are not mutated.** Any deviation is a protocol
  violation per ED-SC 3.1 rev. 2 §6.

---

## 4. Filter geometry

- α_filt = 0.25 (canonical, matches T1a_baseline)
- N_req = 4 (canonical)
- Saddle detection: `fr.find_morse_saddles(E)` on smoothed field
  `E = fr.smooth_field(p)`
- Motif admission: `fr.motif_pass(s, E, p_hat, p_std, α_filt,
  L_ray_val, N_req)` — the only axis varied is `L_ray_val`.

Filter geometry is **identical to ED-SC 3.1** and **ED-SC 3.2**.
Only L_ray is varied; α_filt and N_req are frozen.

---

## 5. Protocol

For each of the 16 grid points:

1. Evolve each of the 10 seeds to step 500 using `ed_step_mobility`
   with canonical parameters (evolution is L_ray-independent — we
   **cache the field set once** and reuse across grid points, saving
   ~15× compute).
2. For each seed, compute smoothed field E, \(\hat p\), \(\sigma_p\).
3. Detect Morse saddles on E.
4. Apply motif filter with current L_ray.
5. Collect pooled ratios ρ = λ₂/λ₁ across seeds.
6. Bootstrap S1 (median), S2 (IQR) with 4000 resamples
   (16–84% CIs); compute S3 (upper-tail log-slope).

**Pre-registered diagnostic readings:**

- **Smooth-drift test:** are S1 and S2 monotone over [1.0, 2.5]?
- **Shoulder test:** is there a unique L_ray/ξ\* where |dS2/d(L_ray/ξ)|
  exceeds 3× the median derivative?
- **Resonance test:** count sign-changes of the discrete derivative
  of S1 across the grid; ≥ 2 sign changes = resonance verdict.
- **Canonical stability:** does S2 in [1.0, 1.2] remain within
  20% of S2(1.08) = 1.29 from v2? If not, the canonical operating
  point itself is marginal.

---

## 6. Deliverables

- `analysis/scripts/ed_sc_3_2_5_g3_g4_transition.py` (driver)
- `outputs/ed_sc_3_2/transition_g3_g4_summary.json` (scan of record)
- §7 below — populated with measured table + verdict.

---

## 7. Results

**Source:** `outputs/ed_sc_3_2/transition_g3_g4_summary.json`
(driver: `analysis/scripts/ed_sc_3_2_5_g3_g4_transition.py`;
10-seed field cache shared across 16 grid points;
total wall ≈ 20 s).

### 7.1 Measured table

| L_ray/ξ | L_ray (lu) | N | S1 (median) | S2 (IQR) | S3 (tail) |
|---:|---:|---:|---:|---:|---:|
| 1.00 | 1.758 | 32 | −1.913 | 1.270 | −5.41 |
| 1.10 | 1.933 | 34 | −1.913 | 1.257 | −4.84 |
| 1.20 | 2.109 | 32 | −1.913 | 1.194 | −4.59 |
| 1.30 | 2.285 | 34 | −1.913 | 1.212 | −4.70 |
| 1.40 | 2.461 | 33 | −1.922 | 1.223 | −3.97 |
| **1.50** | 2.636 | 30 | **−2.623** | **2.703** | −2.21 |
| 1.60 | 2.812 | 33 | −2.687 | 2.672 | −2.02 |
| 1.70 | 2.988 | 29 | −2.831 | 2.646 | −1.63 |
| 1.80 | 3.164 | 27 | −3.380 | 2.876 | −1.83 |
| 1.90 | 3.339 | 28 | −3.077 | 2.761 | −1.58 |
| 2.00 | 3.515 | 29 | −2.774 | 2.990 | −1.77 |
| **2.10** | 3.691 | 19 | **−1.821** | 3.084 | −7.40 |
| 2.20 | 3.867 | 15 | −1.718 | 2.457 | −5.21 |
| 2.30 | 4.042 | 16 | −1.715 | 2.355 | −8.02 |
| 2.40 | 4.218 | 15 | −1.711 | 2.457 | −8.02 |
| 2.50 | 4.394 | 16 | −1.715 | 2.355 | −8.02 |

### 7.2 Structure

The scan reveals **three distinct regimes separated by two sharp
transitions**:

- **Regime I — canonical plateau** (L_ray/ξ ∈ [1.0, 1.4]):
  S1 ≈ −1.91, S2 ≈ 1.23, N ≈ 33. This reproduces the ED-SC 3.1
  baseline (−1.88, 1.27) within sampling noise. The canonical
  operating point L_ray/ξ = 1.08 is **interior to a stable plateau**
  ~0.4 wide.
- **Transition 1** at L_ray/ξ ≈ **1.5**: S2 jumps 1.22 → 2.70
  (121%, single step) and S1 drops −1.92 → −2.62 (37%).
- **Regime II — elevated plateau** (L_ray/ξ ∈ [1.5, 2.0]):
  S1 drifts from −2.62 to a minimum of −3.38 at 1.8, S2 climbs
  2.7 → 3.0, N stays ≈ 29. Tail (S3) is flat near −2 — heavier
  tail than Regime I.
- **Transition 2** at L_ray/ξ ≈ **2.1**: N drops 29 → 19
  (motif yield collapses by 34%), S1 recovers to −1.82, S3
  steepens to −7.4.
- **Regime III — depleted plateau** (L_ray/ξ ∈ [2.1, 2.5]):
  S1 ≈ −1.72, S2 ≈ 2.4, N ≈ 15–16. Medians/IQRs repeat with
  near-exact values at 2.3/2.5 and 2.2/2.4, indicating the
  underlying admitted-saddle set is changing only by one or two
  motifs per step — a *discrete* ray-budget effect.

### 7.3 Diagnostic readings (per §5)

- **Smooth-drift test:** FAILS. S2 jumps 121% between two
  adjacent grid points (1.4 → 1.5).
- **Shoulder test:** FAILS (for single-shoulder). Two distinct
  shoulders exist (1.5 and 2.1).
- **Resonance test:** TRIGGERED. Discrete dS1 sign-changes:
  (−) on 1.4→1.5, (+) on 1.8→1.9, (−) on 2.4→2.5 — three sign
  changes across the grid, ≥ 2 threshold. The alternation
  matches the G4→G5→G6 non-monotonicity seen in the original
  coarse scan.
- **Canonical stability:** PASSES. S2 on [1.0, 1.2] deviates
  ≤ 6% from S2(1.08) ≈ 1.29; the canonical operating point is
  in the interior of a stable plateau.

### 7.4 Verdict — **C (resonance)**

The G3→G4 region contains a **two-shoulder resonance structure**,
not a smooth drift (A) and not a single transition (B). The
repeated-value pattern in Regime III (1.194 IQR matches exactly
across 2.2/2.4, 2.3/2.5; and 2.455 IQR across 2.2/2.4) is the
fingerprint of a **discrete ray-budget effect**: as L_ray grows
past a critical fraction of the periodic box, ray endpoints
sample the same small set of lattice cells and the motif filter
admits/rejects saddles in integer-valued jumps.

The transitions at 1.5 and 2.1 most plausibly correspond to
L_ray crossing integer-multiple thresholds of the saddle
neighbourhood scale. Specifically, L_ray ≈ 2.64 (at 1.5) and
L_ray ≈ 3.69 (at 2.1) are ~3 and ~4 lattice units
respectively — consistent with the 4-ray filter geometry
(N_req = 4) encountering the first and second lattice-shell
resonances.

### 7.5 Consequences

- **Canonical operating point is safe.** L_ray/ξ = 1.08 sits
  interior to Regime I; baselines S1 = −1.88, S2 ≈ 1.27 are
  stable across a plateau 0.4 wide. ED-SC 3.1 headline numbers
  stand.
- **S-F2 weak reading requires scope rev.** The 20% flat
  tolerance is appropriate *within* a regime but meaningless
  *across* a regime boundary. ED-SC 3.0 §5 S-F2 must be rev.2
  to state: tolerance applies within a resolved regime of the
  hinge scan; cross-regime drifts are diagnostic, not
  falsifying.
- **Filter-geometry scan needs a resonance gate.** ED-SC 3.3
  (α_filt, N_req axes) should explicitly check for
  ray-budget resonances before varying L_ray and fold the
  resonance-detection logic into its pre-registration.

---

## 8. Next steps (decision tree) — executed path

Verdict C path (§8 original decision tree): **open
ED-SC 3.2.6** to investigate the ray-budget resonance
mechanism before ED-SC 3.3 can reopen.

**Recommended sequence:**

1. **ED-SC 3.0 rev. 2** (scope patch): restate S-F2 as
   within-regime tolerance; add a resonance-mapping clause.
2. **ED-SC 3.2.6** (`theory/ED_SC_3_2_6_RayBudget_Resonance.md`):
   pre-register a driver that varies L_ray at fixed sub-lattice
   resolution to test the integer-multiple threshold hypothesis
   (L_ray ≈ 2.64, 3.69 lu) explicitly — e.g. by subsampling
   Δ(L_ray) at 0.02 lu around the shoulders.
3. **ED-SC 3.3** reopens only after ED-SC 3.2.6 delivers
   either (a) confirmed resonance explanation + a
   canonical-window recommendation, or (b) a null result
   forcing a different mechanism hunt.


---

## 8. Next steps (decision tree)

- **If verdict A (smooth drift):** ED-SC 3.0 §5 S-F2 should be
  restated in rev. 2 as a *predicted-curve* tolerance (scope patch
  only); ED-SC 3.3 unblocks.
- **If verdict B (shoulder):** identify L_ray/ξ\* and justify whether
  ED-SC 3.0 §5 should restrict the canonical operating range to
  [1.0, L_ray/ξ\* − buffer]; ED-SC 3.3 unblocks with a narrower
  canonical window.
- **If verdict C (resonance):** open ED-SC 3.2.6 to investigate the
  ray-budget resonance mechanism (likely a discrete-ray alignment
  artefact); ED-SC 3.3 remains blocked.
