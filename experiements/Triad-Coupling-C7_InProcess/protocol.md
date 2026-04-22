# Nonlinear Triad Coupling Test — Canon Axiom C7 Protocol

**Status.** Operational protocol for the next predictive experiment identified by the Test-to-Axiom Mapping Project. Targets **Canon axiom C7 — Nonlinear Triad Coupling**, the most load-bearing under-tested axiom in the current four-test ED empirical program.

**Relationship to prior work.**
- **Origin document** — [`docs/ED-Test-to-Axiom-Mapping-v1.0.md`](../../docs/ED-Test-to-Axiom-Mapping-v1.0.md) §6–§7 (Stage 4 next-experiment generator and recommendations).
- **Theoretical basis** — 00.2 Architectural Canon P7 (`M′(ρ)|∇ρ|²` generates k=3 from k=1 with invariant triad ratio); ED-Phys-16 measured coupling ~0.03 with third-harmonic amplitude 3–6% of fundamental.
- **Analogue-5 survival** — qualitative triad coupling structure + v–δ frequency match survive the 2026-04-22 retraction of the FPv2 §8.4 quantitative "54% renormalization" claim (root cause: spurious `params.D *` at [`edsim/phys/analogues/telegraph_pme.py:162`](../../edsim/phys/analogues/telegraph_pme.py)).
- **Reused apparatus** — Top-1 reuses the AFM-Dewetting pipeline ([`AFM-Dewetting-ED-SC_InProcess/protocol.md`](../AFM-Dewetting-ED-SC_InProcess/protocol.md)). Alternative 1 reuses the RLC benchtop rig ([`ED-RLC-Analogue_InProcess/`](../ED-RLC-Analogue_InProcess/)) with the 2026-04-22 AstroAI kit. Alternative 2 extends the FRAP protocol ([`FRAP-High-BSA_InProcess/protocol.md`](../FRAP-High-BSA_InProcess/protocol.md)).

**Coverage gain.** Executing any of the three routes upgrades C7's row in the Stage 2 coverage matrix from all-indirect/none to direct in at least one test column. Top-1 is the recommended path: $0–500 incremental cost, 1–6 week timeline, reuses existing samples and pipeline.

---

## 1. The prediction in one paragraph

The Architectural Canon's P7 principle requires the ED operator to contain a `M′(ρ)|∇ρ|²` term that mixes spatial modes at cubic order. For a field `ρ(x,y)` dominated by a single wavevector `k_s`, this term sources a third-harmonic response at `3k_s` with amplitude ratio `A(3k_s)/A(k_s) ∈ [0.02, 0.08]` and scaling `A₃ ∝ A₁²`. The same triad appears in the temporal domain of any lumped analogue driven at a single frequency `f₀`, producing `A(3f₀)/A(f₀)` in the same band. Absence of this response — or appearance of a dominant `A₂` instead, or independent decay of `A₃` uncoupled to `A₁` — falsifies C7. The triad is architecturally invariant: its ratio must not drift with sample, temperature, or drive amplitude within the canonical regime.

## 2. Pre-registered test parameters

**Revised 2026-04-22 against simulation calibration** ([`analysis/scripts/telegraph_pme/triad_calibration/memo.md`](../../analysis/scripts/telegraph_pme/triad_calibration/memo.md)). The original `A₃/A₁ ∈ [0.02, 0.08]` band inherited from ED-Phys-16 was shown to be a saturation-regime measurement, not a scale-free invariant. The invariant is the dimensionless triad coefficient `K = A₃/A₁³`.

| Parameter | Value | Role |
|:---|:---|:---|
| **Triad coefficient invariant** `K = A₃/A₁³` | `∈ [0.010, 0.025]` | Scale-free C7 invariant; simulated value at β=2 is 0.015 ± 0.001 |
| **Companion second-order invariant** `K₂ = A₂/A₁²` | `∈ [0.20, 0.40]` | Architectural signature of `M′|∇ρ|²`; simulated value 0.279 |
| **Scaling law (primary)** `log A₃ vs log A₁` slope | `∈ [2.8, 3.2]` | Cubic enslaving of k=3 to k=1 source |
| **Scaling law (companion)** `log A₂ vs log A₁` slope | `∈ [1.8, 2.2]` | Quadratic k=2 source |
| **Phase lock** `φ₃ − 3φ₁` | within `π/8` of `±π`, SD < `π/4` | Canonical triad signature; M′ < 0 → phase π |
| **Symmetry ordering** | `A₂ > A₃` in clean regime | Direct quadratic dominates cubic in `M′|∇ρ|²` operator |
| **Minimum dynamic-range sweep** | ≥ 1 decade in `A₁` | Required to validate scaling |
| **Spectral SNR floor** | ≥ 40 dB at `3f₀` or `3k_s` | Separates signal from noise at lowest `A₁` point |
| **Spatial oversampling** (spatial realizations) | `Δx ≤ λ_s / 6` | Resolves k=3 without aliasing |
| **Amplitude dynamic range** | ≥ 10 bits on fundamental | Instrument floor |
| **Saturation-regime cross-check** (optional) | `A₃/A₁ ∈ [0.02, 0.08]` at `A₁ ≳ 0.15·ρ_max` | Historical ED-Phys-16 band; reached only near mobility bound |

These parameters are pre-registered. Any deviation is a **revision** of the C7 test specification, not an execution of it.

---

## 3. Stage 1 — Route selection

Three execution routes, ranked by marginal coverage gain per unit cost. Select one based on current operational state.

### 3.1 Top-1 — AFM Spinodal-Dewetting Fourier Triad Reanalysis

- **What** — take existing or newly-acquired AFM dewetting frames, Fourier-decompose each frame, identify the dominant spinodal wavevector `k_s`, measure `A(3k_s)/A(k_s)`, check `A₁²` scaling across frames where `A(k_s)` varies naturally during spinodal evolution.
- **Cost** — $0 incremental if T1 frames are already in hand; ~$500 if a new dewetting run is required.
- **Timeline** — 1–2 weeks analysis-only; 4–6 weeks if new samples are needed.
- **Coverage cell upgraded** — T1 × C7 from `indirect` → `direct`.
- **Dependency** — sample prep and acquisition at [`AFM-Dewetting-ED-SC_InProcess/protocol.md`](../AFM-Dewetting-ED-SC_InProcess/protocol.md) Stage 1–4.

### 3.2 Alternative 1 — Nonlinear RLC Third-Harmonic Generation

- **What** — add a saturating inductor or reverse-biased diode to the AstroAI RLC kit, drive sinusoidally at `f₀` near the circuit's natural frequency, sweep drive amplitude, measure `A(3f₀)/A(f₀)` at steady state.
- **Cost** — ~$20 incremental over the existing RLC rig; 1–2 days bench time.
- **Coverage cell upgraded** — T4 × C7 from `none` → `direct` (participation-channel analogue).
- **Dependency** — RLC rig from `ED-RLC-Analogue_InProcess/`; add a 1N4148 diode or saturating ferrite core.

### 3.3 Alternative 2 — Patterned-FRAP k=3 Recovery

- **What** — confocal FRAP with structured-illumination bleaching imprints a k=1 spatial pattern on a high-BSA sample; recovery of k=1 and k=3 spatial Fourier components measured independently.
- **Cost** — ~$2000–5000 via Creative Proteomics; requires prior confirmation of patterned-bleach capability.
- **Coverage cell upgraded** — T2 × C7 from `indirect` → `direct` in the canonical PME setting where M′(ρ) is the UDM β=2 mobility.
- **Dependency** — sample prep at [`FRAP-High-BSA_InProcess/protocol.md`](../FRAP-High-BSA_InProcess/protocol.md) Stage 1–3; patterned-bleach capability confirmed with vendor.

### 3.4 Theoretical companion — Telegraph-PME Triad Simulation — **COMPLETED 2026-04-22**

- **What** — monochromatic k=1 seed on canonical F[ρ] operator (β=2, H=0), FFT decomposition, A₁ sweep across three decades.
- **Script** — [`analysis/scripts/telegraph_pme/triad_calibration/run_triad_calibration.py`](../../analysis/scripts/telegraph_pme/triad_calibration/run_triad_calibration.py)
- **Memo** — [`analysis/scripts/telegraph_pme/triad_calibration/memo.md`](../../analysis/scripts/telegraph_pme/triad_calibration/memo.md)
- **Result** — `K = A₃/A₁³ ≈ 0.015 ± 0.001` across 3 decades of A₁; phase lock `φ₃ − 3φ₁ = π` exact; `A₂/A₁² ≈ 0.28` clean. Saturation regime reproduces the historical ED-Phys-16 "3–6%" band.
- **Role** — pre-registered §2 parameters are now calibrated against this simulation. Experimental routes should be evaluated against these invariants, not the retired `A₃/A₁ ∈ [0.02, 0.08]` band.

---

## 4. Stage 2 — Acquisition (route-specific)

### 4.1 Top-1 acquisition

- Reuse AFM frames from the T1 pipeline (`h(x, y)`, 512×512 or larger, physical-scale calibrated).
- Require ≥ 5 frames spanning the spinodal pre-rupture regime where the dominant mode amplitude varies naturally by ≥ 1 decade. If fewer, acquire new frames per [`AFM-Dewetting-ED-SC_InProcess/protocol.md`](../AFM-Dewetting-ED-SC_InProcess/protocol.md) §4.
- Verify `Δx ≤ λ_s / 6` per frame (sampling floor for k=3 resolution). If violated, reject frame.

### 4.2 Alternative 1 acquisition

- Set RLC natural frequency `f₀` in the 1–10 kHz band to keep harmonic analysis clean of line noise.
- Sweep drive amplitude over ≥ 1 decade, 6 logarithmically-spaced points.
- Acquire ≥ 10 periods at each amplitude with oscilloscope or USB-DAQ, ≥ 10-bit resolution, sample rate ≥ 20·`f₀`.
- Record ambient temperature and drive-source THD to bound instrument-level harmonic contamination (must be < `A₃/A₁` prediction band).

### 4.3 Alternative 2 acquisition

- Imprint k=1 pattern with structured bleach at `λ_1 ≥ 6·Δx_pixel`.
- Image at `Δx_pixel ≤ λ_1 / 6` to resolve `3k_1`.
- Time-series acquisition at ≥ 10 Hz frame rate over the full recovery window.
- Repeat at ≥ 3 initial bleach depths to vary `A₁` for the scaling test.

---

## 5. Stage 3 — Analysis pipeline

### 5.1 Fourier decomposition (spatial realizations)

1. For each frame, compute `ρ̂(k) = FFT2(ρ(x,y))`.
2. Identify dominant wavevector `k_s = argmax|ρ̂(k)|` excluding DC.
3. Extract `A₁ = |ρ̂(k_s)|` and `A₃ = |ρ̂(3k_s)|` with directional averaging over the `k_s` isotropic shell.
4. Record phase of `A₁` and `A₃` relative to the frame origin.

### 5.2 Harmonic extraction (temporal realizations)

1. Acquire steady-state time series `v(t)` at each drive amplitude.
2. Compute `V̂(f) = FFT(v(t))` with Hann window; length ≥ 10 drive periods.
3. Extract `A₁ = |V̂(f₀)|` and `A₃ = |V̂(3f₀)|`.
4. Subtract quadrature-calibrated instrument-level `A₃_inst/A₁` floor (vendor spec or in-line passive-load calibration).

### 5.3 Scaling fit

1. Plot `log A₃` vs `log A₁` across frames or drive amplitudes.
2. Fit slope `m`; C7 predicts `m = 2 ± 0.2`.
3. Fit intercept; C7 predicts `A₃/A₁² = K` with `K` system-independent within ε_triad (see §6).

### 5.4 Phase-lock test

1. For each acquisition, compute phase offset `Δφ = arg(A₃) − 3·arg(A₁)`.
2. Across the ensemble, `Δφ` must be clustered with standard deviation < π/4. Broadband noise gives uniform `Δφ`.

### 5.5 Sanity checks before decision

- **Instrument harmonic floor** verified < 0.005.
- **Aliasing** ruled out — spatial `Δx ≤ λ_s/6`; temporal `f_sample ≥ 20·f₀`.
- **Linear regime** confirmed — test at smallest `A₁` that gives SNR ≥ 40 dB; at that amplitude, `A₃/A₁` must be finite and in-band, not zero.
- **A₂ check** — extract `A₂ = |ρ̂(2k_s)|` or `|V̂(2f₀)|` and confirm `A₂ < A₃` per §2 symmetry constraint.

---

## 6. Decision tree

| Outcome | Criteria | Action |
|:---|:---|:---|
| **PASS** | `K = A₃/A₁³ ∈ [0.010, 0.025]` AND `log A₃ vs log A₁` slope ∈ [2.8, 3.2] AND phase-lock SD < π/4 AND `A₂ > A₃` in clean regime | C7 corroborated; write up, upgrade Stage 2 matrix cell; plan second-route confirmation |
| **FAIL** | `K` scaling not cubic (slope ∉ [2.5, 3.5]) OR phase-lock absent OR `A₂` and `A₃` both follow same scaling exponent | C7 falsified in this regime; document; revisit ED-Phys-16 coupling measurement; potential Canon P7 revision |
| **UNDECIDABLE** | Noise-limited at smallest `A₁` (SNR at 3k_s < 20 dB) OR insufficient amplitude range for scaling fit | Upgrade instrumentation or acquire more frames; do not publish as evidence |
| **SPLIT** | `K` in band but scaling exponent or phase-lock criterion fails | Flag partial-support; investigate whether a non-canonical nonlinearity (e.g., cubic direct `ρ³` or `M″ = 0`) is producing the ratio; not a clean C7 confirmation |

**Invariance cross-check (if two routes executed).** The triad ratio `A₃/A₁` on PASS outcomes must agree between routes within `ε_triad = 0.03` (sum of per-system biases). Disagreement beyond this band indicates that one route is sampling a system-specific artifact rather than the architectural invariant.

---

## 7. Budget and timeline summary

| Route | Cost | Wall time | Coverage delta |
|:---|:---|:---|:---|
| Simulation companion (§3.4) | $0 | 1–3 days | Calibration only |
| Top-1 AFM reanalysis | $0–500 | 1–6 weeks | T1×C7 → direct |
| Alt-1 Nonlinear RLC | ~$20 | 1–2 weeks | T4×C7 → direct |
| Alt-2 Patterned FRAP | ~$2000–5000 | 4–8 weeks | T2×C7 → direct |

**Recommended execution order.** (1) Simulation companion to calibrate the band. (2) Top-1 AFM reanalysis to attempt the first direct C7 measurement. (3) If Top-1 PASSes or is UNDECIDABLE, execute Alt-1 for independent cross-check in the temporal/participation domain. (4) Alt-2 only if Alt-1 is inconclusive and budget permits.

---

## 8. Review-level notes for a v2 protocol

- **Band width.** The [0.02, 0.08] prediction band is wide (factor ~4). A sharper v2 prediction requires deriving `K = A₃/A₁²` from first principles at fixed `M, M′, P`, not quoting ED-Phys-16's measured range. Simulation companion (§3.4) is the path to this.
- **A₂ symmetry constraint** assumes the exact odd symmetry of `M′·|∇ρ|²`. If the constitutive form is modified (SY2 penalty introduces new parity structure), `A₂` may be non-zero at sub-`A₃` level. v2 should predict `A₂/A₁` explicitly.
- **Invariance claim.** The "triad ratio is architecturally invariant" statement is currently inherited from the Canon without a dedicated cross-system derivation. v2 should tabulate the expected `K` across the four-test systems and specify the spread that would still count as invariance.
- **Top-1 caveat.** Spinodal dewetting has a mode-selection mechanism that may couple to non-ED nonlinearities (van der Waals, thin-film lubrication). A PASS on Top-1 must be verified by Alt-1 in the RLC participation channel to rule out dewetting-specific artifact.

---

*Protocol version: v1.0. Source: Stage 4 of the Test-to-Axiom Mapping Project ([`docs/ED-Test-to-Axiom-Mapping-v1.0.md`](../../docs/ED-Test-to-Axiom-Mapping-v1.0.md)). Revise by incrementing the version number in this footer and the title.*
