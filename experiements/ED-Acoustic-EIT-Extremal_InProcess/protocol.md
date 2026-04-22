# EIT Extremal-Horizon Differential Test — ED Acoustic-Metric Protocol

**Status.** Operational protocol for Experiment 1 of the ED acoustic-analogue experimental program. Tests ED's extremal-horizon prediction (`κ = 0` at a smooth interior-maximum of the signal-speed profile) in a slow-light / EIT atomic system with a **within-apparatus differential** (extremal configuration vs. monotonic configuration in the same cell).

**Relationship to prior work.**
- **Strategic framing** — [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../../theory/ED_Acoustic_Analogue_Experimental_Program.md) §5.1 (Experiment 1) and §8.1 (top-priority rationale).
- **Theoretical basis** — [`theory/ED_Effective_Acoustic_Metric.md`](../../theory/ED_Effective_Acoustic_Metric.md) (g^eff derivation) + [`theory/ED_Acoustic_Metric_Curvature.md`](../../theory/ED_Acoustic_Metric_Curvature.md) (Gaussian-bump curvature) + [`theory/ED_Schwarzschild_Obstruction.md`](../../theory/ED_Schwarzschild_Obstruction.md) (what the acoustic metric is *not*).
- **Scope guardrails** — [`memory/project_ed10_geometry_qft_scope.md`](../../.claude/projects/C--Users-allen-GitHub-Event-Density/memory/project_ed10_geometry_qft_scope.md). Claims are (ii)-grade kinematic acoustic-metric consistency, not Einstein-dynamics or Hawking-from-curved-spacetime claims.

**One-paragraph honesty statement.** The result `κ = 0 at a smooth c_s-maximum` is a kinematic property of any acoustic metric — it is a shared prediction of ED and standard analogue gravity for this horizon class, not an ED-unique claim. The ED-specific content is the **prediction of which physical regimes populate the interior-maximum class** (mobility-collapse P4 horizons), not the geometric fact itself. A null emission in the extremal configuration supports the acoustic-metric reading, which ED adopts; a non-null emission in that same configuration would be inconsistent with ED's P4-is-extremal identification. The EIT toggle is the cleanest *within-apparatus* discriminator currently available.

---

## 1. The prediction in one paragraph

In an EIT atomic medium with spatially shaped control field `Ω_c(x)`, the probe group velocity is `v_g(x) ∝ |Ω_c(x)|² / ρ_OD(x)` (Hau-Lukin-Harris formula; schematic). Two control-field profiles are engineered in the same cell:

- **(M) Monotonic configuration** — `Ω_c(x)` drops linearly across the cell so that `v_g(x)` decreases monotonically and reaches `v_g = 0` at a sharp transition point. Visser surface gravity `κ_M = (1/2)|dv_g²/dx|_horizon > 0`. Hawking-analogue temperature `T_M = ℏκ_M/(2π k_B)`.
- **(E) Extremal configuration** — `Ω_c(x)` is shaped so that `v_g²(x)` has a **smooth local minimum** at the cell centre with `v_g → 0` at that smooth minimum. By construction `d v_g²/dx = 0` at the stopping point, so `κ_E = 0` and `T_E = 0`.

**ED prediction:** the ratio of thermal-emission rates `R_E / R_M → 0` in the limit of ideal extremal profile and sufficient averaging, and both configurations share the same probe spectrum, noise floor, and detection chain. A nonzero, drive-independent `R_E / R_M` above the measurement floor falsifies the extremal reading for this platform.

## 2. Pre-registered test parameters

| Parameter | Value | Role |
|:---|:---|:---|
| **Primary observable** | Thermal-emission ratio `R_E / R_M` | Falsifier: ≤ 0.1 within 1σ is PASS; ≥ 0.5 is FAIL |
| **Secondary observable** | Pair-correlation peak amplitude `G_H(x, x')` at null-ray locus | In (M): clear peak; in (E): suppressed below noise floor |
| **Surface-gravity ratio** `κ_E / κ_M` (extracted from mode-mixing) | `< 0.1` | Independent check on the primary observable |
| **Curvature check** | `v_g²` profile fit to `v_g²(x) = A·(x − x_0)² / (1 + (x − x_0)²/σ²)` near the minimum | Gaussian-bump-analogue parameters `A, σ` must match the ED `R(0) = −a/[σ²(1−a)]` formula where `a = 1 − v_g,min² / v_g,max²` |
| **Probe spectral resolution** | `Δω / ω_probe ≤ 10⁻⁶` | Resolves thermal tail against monochromatic background |
| **Detection chain** | Photon-counting avalanche photodiode (APD) with timing resolution `< 1 ns` | Enables coincidence counting for pair correlations |
| **Minimum photon budget** | ≥ `10⁶` detected photons per configuration | SNR floor for `R_E / R_M < 0.1` discrimination |
| **Control-field profile accuracy** | Extremal minimum position stable to `< 10⁻³ · L_cell` | Position jitter dominates at long averaging |
| **Cell-pair equivalence** | Same cell, same alignment, toggle period `< 1 s` | Eliminates long-term drift between (M) and (E) |
| **Extremal-profile smoothness** | `|d³v_g² / dx³|` at `x_0` below a calibrated threshold | Ensures the "smooth" assumption of §3 analysis |

These parameters are pre-registered. Any deviation is a **revision** of the EIT extremal test specification, not an execution of it.

---

## 3. Stage 1 — Apparatus selection

### 3.1 Baseline EIT system

Any of the standard three-level-Λ EIT setups works in principle:

- **Cold atomic ensemble** (Rb MOT or Rb BEC). Cleanest; lowest decoherence; highest profile; most expensive. Lukin-group, Hau-group style.
- **Warm atomic vapour cell** (Rb or Cs). Accessible; lower cost; Doppler broadening handled by co-propagating geometry. Halfmann-group, Lvovsky-group style.
- **Solid-state EIT** (Pr:YSO, NV in diamond, rare-earth doped crystal). Ultra-long coherence in Pr:YSO; harder to shape control-field spatial profile.

**Recommendation:** warm Rb vapour cell with co-propagating control + probe — lowest barrier to execution, sufficient coherence for 10⁶-photon coincidence statistics at reasonable integration times.

### 3.2 Control-field spatial shaping

The key capability is programmable spatial intensity profile for the control field. Two options:

- **Spatial light modulator (SLM)** — phase-only or amplitude-modulation SLM images an arbitrary intensity profile onto the cell. Switching (M) ↔ (E) profiles is a single frame update, sub-millisecond.
- **Fibre-bundle / structured illumination** — discrete spatial modes combined with intensity control at each mode. Slower reconfiguration but lower loss.

**Recommendation:** SLM. Sub-second toggling between (M) and (E) configurations is essential for within-apparatus differential.

### 3.3 Required spatial resolution

Along the propagation direction `x`, resolve `v_g²(x)` to `Δx ≤ σ / 6` where `σ` is the width of the smooth minimum in (E). For typical cell lengths `L_cell ~ 10 cm` and `σ ~ 1 mm`, this is `Δx ~ 150 µm` — easily achieved by SLM pixel pitch projected through the cell.

---

## 4. Stage 2 — Profile design

### 4.1 Monotonic configuration (M)

`|Ω_c(x)|² = Ω_0² · (1 − x/L_cell)` for `x ∈ [0, L_cell]`

Probe group velocity: `v_g(x) ∝ (1 − x/L_cell)` (linear).

Surface gravity at stopping point `x = L_cell`:

    κ_M = (1/2)|dv_g² / dx|_{x = L_cell} = v_{g,max}² / L_cell

For `v_{g,max} ~ 100 m/s` and `L_cell ~ 10 cm`, `κ_M ~ 10⁵ s⁻¹`, giving Hawking-analogue temperature `T_M ~ ℏκ_M / (2π k_B) ~ 100 nK`.

### 4.2 Extremal configuration (E)

`|Ω_c(x)|² = Ω_0² · [1 − exp(−(x − x_0)² / (2σ²))]` with `x_0 = L_cell / 2, σ ≈ L_cell / 20`.

Probe group velocity: `v_g²(x)` has a smooth Gaussian minimum at `x_0` with `v_g(x_0) = 0` (by Ω_c minimum at x_0).

Surface gravity at stopping point `x = x_0`:

    κ_E = (1/2)|dv_g² / dx|_{x = x_0} = 0    (smooth minimum)

Hawking-analogue temperature `T_E = 0`.

### 4.3 Profile-smoothness sanity check

Before execution, numerically verify:

- (M) profile produces a **linear** zero-crossing in `v_g²(x)` at the stopping point with nonzero slope.
- (E) profile produces a **quadratic** zero-crossing at `x_0`, i.e. `v_g²(x) ∝ (x − x_0)²` near the minimum.

Fit residual to both functional forms; quadratic-form fit to (E) should be ≥ 10× tighter than linear-form fit.

---

## 5. Stage 3 — Measurement protocol

### 5.1 Integration cycle

For each configuration (M) and (E):

1. Set SLM pattern; wait for profile to stabilise (< 100 ms).
2. Inject probe coherent state at constant photon flux (matched between configurations).
3. Collect output photons for a pre-registered integration time `τ_int`.
4. Record photon arrival times for coincidence analysis.
5. Toggle SLM to the other configuration; repeat.

Alternate (M) ↔ (E) with toggle period `τ_toggle ~ 1 s`. Total dataset: `N_cycles ≥ 100` per configuration, giving `≥ 10⁶` detected photons per configuration.

### 5.2 Baseline subtraction

Control datasets:

- **(0) Null**: probe on, control-field off — pure absorptive background.
- **(U) Uniform**: control-field at constant `|Ω_c|²` across the cell (no horizon) — baseline transparency, no Hawking production.

Emission rates in (M) and (E) are compared against (U), not (0).

### 5.3 Noise-floor characterization

Characterize the measurement floor of `R_E / R_M` by:

- Thermal photon background from blackbody cavity (detector-dark rate).
- Residual probe leakage into the signal band.
- Decoherence-induced spontaneous emission (independent of horizon structure).

Target floor: `R_E / R_M ≤ 0.05` at measurement level, giving a `> 10×` margin for the `< 0.1` PASS criterion.

---

## 6. Stage 4 — Analysis pipeline

### 6.1 Primary analysis — emission-rate ratio

1. For each configuration, compute photon arrival-time histogram binned at detector resolution.
2. Subtract baseline (U) and null (0) histograms.
3. Integrate signal band (frequencies corresponding to Hawking-analogue thermal spectrum).
4. Emission rate `R_i = N_signal,i / τ_int,i` for `i ∈ {M, E}`.
5. Compute ratio `R_E / R_M` with Poisson error bars.

### 6.2 Secondary analysis — pair correlations

1. Compute two-point photon correlation function `g²(Δt)` within each integration window.
2. Look for non-Poisson correlations at `Δt` matching the null-ray traversal time across the horizon.
3. In (M): expect a correlation peak at the predicted `Δt_H`.
4. In (E): peak should be suppressed by a factor `(T_E / T_M)^2 ~ 0`.

### 6.3 Surface-gravity extraction

From the scattering coefficients of upgoing / downgoing probe modes at the horizon, extract κ via the Unruh-de Witt detector response function or the Bogoliubov-coefficient formula. Compare `κ_E / κ_M` to the geometric prediction.

### 6.4 Curvature check

Fit the measured `v_g²(x)` near the stopping point in (E) to:

    v_g²(x) = c_max² · (x − x_0)² / [(x − x_0)² + σ²]

Extract `σ` and bump-amplitude `a = 1 − v_g,min²/v_g,max²`. Compute predicted ED curvature `R_ED(x_0) = −a/[σ²(1−a)]` from [`ED_Acoustic_Metric_Curvature.md`](../../theory/ED_Acoustic_Metric_Curvature.md). Extract measured curvature from second-derivative of fitted `v_g²(x)`. Compare.

---

## 7. Stage 5 — Decision tree

| Outcome | Criteria | Interpretation |
|:---|:---|:---|
| **PASS** | `R_E / R_M < 0.1` AND `κ_E / κ_M < 0.1` AND curvature matches ED within 20% | Extremal-horizon prediction supported. Strengthens ED's acoustic-metric / P4-is-extremal reading. |
| **NEAR-PASS** | `R_E / R_M < 0.3` but profile-smoothness check failed (residual `d³v_g²/dx³` present) | Inconclusive; extremal profile not achieved in hardware. Redesign SLM pattern. |
| **FAIL** | `R_E / R_M > 0.5` OR `κ_E` extracted from mode-mixing is comparable to `κ_M` | Extremal-reading falsified for this platform. Forces re-examination of the acoustic-metric identification or identification of a non-thermal mode-conversion channel at smooth maxima. |
| **UNDECIDABLE** | Measurement floor for `R_E / R_M` above 0.2 due to dark-count / leakage | Upgrade detector or extend integration. Do not report as PASS or FAIL. |
| **SPLIT** | Primary observable PASSes, secondary (pair-correlation or curvature) FAILS | Most informative outcome. Suggests the kinematic κ prediction is correct but higher-order structure disagrees with ED. Requires memo follow-up. |

---

## 8. Stage 6 — Collaboration / execution path

### 8.1 Primary collaboration targets

- **Lukin group (Harvard)** — cold Rb ensemble EIT, pair-correlation photon detection infrastructure in place.
- **Hau group (Harvard)** — stopped-light expertise; existing spatial-control of EIT coherence.
- **Halfmann group (Darmstadt)** — Pr:YSO solid-state EIT with long coherence time.
- **Lvovsky group (Oxford)** — quantum-memory EIT; photon-counting infrastructure.
- **Giacobino / Bramati (LKB Paris)** — EIT + quantum optics; analogue-gravity-adjacent work.

### 8.2 Outreach draft (when ready)

A one-page outreach memo should accompany a collaboration request. Content to include:

- One-paragraph honesty statement (§0 of this protocol).
- Primary observable and PASS criterion.
- Within-apparatus differential as the methodological strength.
- Budget / instrument asks (SLM + existing EIT cell = cost).
- Timeline (~3–6 months end-to-end).

Do not send outreach until the §2 pre-registered parameters have been reviewed by a domain expert for feasibility on a specific apparatus — the SLM spatial resolution and the `κ_M` magnitude need to be realistic for the target group's cell.

### 8.3 Standalone / in-house analysis option

If no collaboration materialises but public EIT data exist with sufficient spatial resolution, a **retrospective analysis** on published datasets can be attempted:

- Look for published EIT stopped-light measurements where the control-field profile was either linear (standard) or shaped (less common).
- Re-extract `v_g²(x)` from the published figures.
- Compute predicted `κ_M` and `κ_E` from the extracted profiles.
- If any dataset shows an interior-maximum profile, check photon-statistics tails.

Yield unlikely (published EIT work rarely shapes the control-field specifically for this test) but zero-cost first pass.

---

## 9. Known systematics and risks

| Systematic | Effect | Mitigation |
|:---|:---|:---|
| SLM flicker / drift | Position of extremal minimum wanders | Feedback loop from on-cell imaging; toggle period < drift timescale |
| Optical pumping mismatch | Different steady-state populations in (M) vs. (E) | Keep total control-field power matched; equalize integrated intensity |
| Decoherence (collisions, magnetic field) | Adds incoherent emission in both configurations | Cancels in ratio `R_E / R_M`; verify with (U) baseline |
| Imperfect extremal profile | `|d v_g² / dx| > 0` at stopping point | Profile-smoothness check in §4.3; raise minimum-smoothness threshold |
| Pair-correlation confounds | Collision-induced pair emission (not Hawking) | Compare to (U) baseline; collision rate set by buffer-gas / density |
| Doppler broadening in vapour cells | Washes out sharp spatial features | Use cold atoms or longitudinally co-propagating geometry |
| Detector dark count | Raises `R_E` floor | APDs with `< 100 Hz` dark rate; cooled |

---

## 10. Operational follow-ups

- **Curvature-level predictions** — beyond κ = 0, ED predicts a specific profile-shape relation for `R(x_0)` (Gaussian-bump formula). Extending this to higher-order mode-mixing is deferred to a theory follow-up. See [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../../theory/ED_Acoustic_Analogue_Experimental_Program.md) §9.
- **Moving-background extension** — this protocol uses stationary control field (v_0 = 0). Moving-pattern extensions (travelling-wave control field) would test the richer v ≠ 0 metric class and map onto standard analogue-gravity BEC transonic tests. Theory extension required first.
- **Cross-platform cross-check** — a concordant PASS from EIT + optical-pulse + phononic-crystal platforms, each within-apparatus differential, would be the strongest possible support. Single-platform PASS is suggestive but not decisive.

---

## 11. What this protocol does not do

- Does **not** test Einstein-equation emergence from ED. `g^eff` here is kinematic only. See [`theory/ED_Schwarzschild_Obstruction.md`](../../theory/ED_Schwarzschild_Obstruction.md).
- Does **not** test a Hawking-radiation mechanism grounded in curved-spacetime QFT. The prediction is acoustic-metric kinematic; shared with standard analogue gravity.
- Does **not** test ED's cross-regime architecture directly. A PASS here constrains ED's acoustic-metric / P4 reading in *this* regime; extrapolation to other regimes (galactic, quantum) requires separate tests.
- Does **not** derive quantum mechanics from ED. The probe-photon statistics are standard quantum optics; no ED-specific quantization is invoked.

Any claim outside this scope in a published result would violate the [`memory/project_ed10_geometry_qft_scope.md`](../../.claude/projects/C--Users-allen-GitHub-Event-Density/memory/project_ed10_geometry_qft_scope.md) guardrails.
