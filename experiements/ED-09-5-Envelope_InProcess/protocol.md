# ED-09.5 Participation-Envelope Test — Operational Protocol

> **⚠ Update 2026-04-22.** The canonical value of the bifurcation is corrected to `D_crit(ζ=1/4) ≈ 0.896` (from the retired heuristic 0.5). See [`D_crit_Resolution_Memo.md`](../../theory/D_crit_Resolution_Memo.md). This protocol's **envelope prediction `ω_v = 2π·N_osc·γ_dec` is unaffected** — it is derived from the good-cavity `γ_dec << ω_sys` limit, not from the numerical location of the critical point. The "sharp-bifurcation exists" structural claim survives. Only the regime-classification label and the numerical value in §2 Table change; the test itself is unchanged.

**Status.** Operational protocol for the participation-channel envelope test of the ED canonical PDE's sharp damping bifurcation (Canon principle P6, `D_crit(ζ=1/4) ≈ 0.896`). Covers **two parallel reanalysis paths**:

- **Track A — Cavity-coupled optomechanics** (Pillar A of the Vienna program map): reanalysis of raw heterodyne `x(t)` from cooled-nanoparticle experiments (Delic 2020, Magrini 2021) once access is obtained. Dependent on Aspelmeyer collaboration.
- **Track B — FRAP-side high-frequency residual**: Lomb-Scargle periodogram of the residual of public FRAP recovery curves at `80–800 Hz`. Self-contained; no third-party dependency; runs today.

**Relationship to prior work.**
- [`ED-09-5-Experimental-Strategy.md`](../../docs/ED-09-5-Experimental-Strategy.md) — the three-tier strategy, draft emails, pre-send checklist.
- [`ED-09-5-Observable-Sharpening.md`](../../docs/ED-09-5-Observable-Sharpening.md) — the v0.9 theory memo with Arndt/Aspelmeyer derivations; §15 derives `ω_v = 2π·N_osc·γ_dec`; §22 selects the `v ↔ X_cav` candidate identification.
- [`ED_Vienna_Program_Map.md`](../../docs/ED_Vienna_Program_Map.md) — 12-target Vienna ecosystem map (T1 / T1* / T2 / THEORY / CLOSED).
- **This protocol is NOT the same as [`UDM-FRAP protocol`](../FRAP-High-BSA_InProcess/protocol.md).** That one tests the **mobility** channel via `R(t) ~ t^(1/6)` front propagation on new BSA data. **This** doc's Track B uses the same class of instrument (FRAP) but a completely different observable (high-frequency residual on the 1D recovery curve, not the 2D spatial front) and tests a different channel (participation, not mobility). Disambiguation is critical; do not conflate.

**What this document does.** Translates §15 of the Observable-Sharpening memo ("`ω_v = 2π·N_osc·γ_dec`") into session-ready reanalysis procedures with per-track pass/fail decision trees. Does **not** modify the derivation of the prediction — that is locked in the Observable-Sharpening memo.

---

## 1. The prediction in one paragraph

The canonical ED PDE has a sharp damping-discriminant bifurcation at `(D − ζ)² = 4(1 − D)`, equivalently **`D_crit(ζ) = √(2−ζ)·(2−√(2−ζ))`**, which gives `D_crit ≈ 0.896` at canon-default `ζ = 1/4` (Canon P6; corrected 2026-04-22 — see [`D_crit_Resolution_Memo.md`](../../theory/D_crit_Resolution_Memo.md)). The bifurcation separates an oscillatory regime (`D < 0.1`: underdamped, reversible, `N_osc ∈ [8, 19]` transient cycles, `Q ≈ 3.5–6.3`, third-harmonic content 3–6%) from a parabolic regime (`D ≥ 0.5`: overdamped, irreversible, Barenblatt spreading). **ED-09.5's identification: this bifurcation IS the physical quantum-classical transition.** All currently cooled optomechanical systems and all concentrated FRAP samples sit **deep on the quantum/oscillatory side** (`D ~ 10⁻⁹` and `D ~ 10⁻³` respectively). On that side, the participation field `v(t)` carries a **slow envelope modulation** at frequency `ω_v = 2π·N_osc·γ_dec` on top of the fast system dynamics, with `N_osc ≈ 8` (single-mode, full-cycle convention per ED-Phys-17 and ED-Phys-19 cross-derivation). The test is whether this envelope is present in the raw data at the predicted frequency with the predicted `Q_v`, harmonic ratio, and triad coupling.

## 2. Pre-registered test parameters (locked by Observable-Sharpening §15 v0.9)

| Parameter | Value | Source |
|:---|:---|:---|
| Damping discriminant | `(D − ζ)² − 4(1 − D) = 0` at critical | Canon P6 (corrected 2026-04-22) |
| Bifurcation | `D_crit(ζ) ≈ 0.896` at canon `ζ = 1/4` | [`D_crit_Resolution_Memo.md`](../../theory/D_crit_Resolution_Memo.md) |
| Quantum-side transient count | `N_osc = 8` (single-mode clean) or `[8, 19]` (multi-mode) | ED-Phys-17 §4.1; full-cycle convention confirmed via code-trace |
| Envelope-decoherence timescale | `τ_v = 1/γ_dec` | Observable-Sharpening §15; good-cavity limit |
| **Envelope frequency** | **`ω_v = 2π·N_osc·γ_dec`**, so **`ω_v/(2π) = 8·γ_dec`** | §15 derivation |
| Envelope Q-factor | `Q_v ∈ [4, 9]` (central value 6.3 per ED-Phys-19 low-k single-mode limit) | §21.3; `√(K_eff·τ)/ζ = 6.32` at canonical parameters |
| Third-harmonic ratio | `3–6%` of fundamental envelope amplitude | Canon P7 triad coupling |
| Triad coupling coefficient | `C ≈ 0.03`, falsification range `[0.01, 0.05]` | ED-Phys-16 |
| `ζ` (damping) | `0.5` (cavity-derived, exact match to canon default) | Observable-Sharpening §22.3 |

**Falsification criteria F0–F5 (from Observable-Sharpening §16):**

- **F0 — No envelope at predicted frequency.** Falsified if no envelope feature at `ω_v/2π ≈ 8·γ_dec ± factor-of-2`.
- **F1 — No envelope at any frequency.** Weakest falsification; the entire §1.5 framing is wrong.
- **F2 — Wrong transient count.** Falsified if `N_osc` outside `[6, 12]` for single-mode systems.
- **F3 — Wrong envelope Q.** Falsified if `Q_v` outside `[4, 9]`.
- **F4 — Wrong harmonic ratio.** Falsified if third-harmonic content outside `[3%, 6%]`.
- **F5 — Wrong triad coupling.** Falsified if cross-frequency power outside `[0.01, 0.05]`.

**Independence structure.** F0 | {F2 ∧ F3} | {F4 ∧ F5} — three genuinely independent dimensions of test, with F2↔F3 and F4↔F5 cross-checked via the internal `N_osc(α) = (Q_v/π)·ln(1/α)` and triad-cross-coupling relations. Partial-confirmation outcomes are well-defined (see §5.3 below).

---

# TRACK A — Cavity-Coupled Optomechanics Reanalysis

Status: **blocked on raw data access**. Aspelmeyer email v3 drafted in strategy doc §7, not yet sent (pending affiliation line + cold-reader pass). Both the Delic 2020 and Magrini 2021 theses are publicly downloadable but raw `x(t)` is not in any public deposit (verified 2026-04-20 via 5-step search; see Observable-Sharpening §20).

## 3. Target datasets and numerical predictions

From Observable-Sharpening §13 and §15:

| System (year) | `ω_m/2π` | `γ_dec` | `D` | Predicted `ω_v/(2π)` | Predicted envelope period `T_v` | Required record length `≥ 3T_v` |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Chan 2011 (Si OM crystal) | 3.68 GHz | ~95 kHz | ~4×10⁻⁶ | **~760 kHz** | ~1.3 µs | ~4 µs |
| **Delic 2020 (levitated SiO₂)** | **305 kHz** | **~2 mHz** | **~10⁻⁹** | **~16 mHz** | **~63 s** | **~200 s** |
| **Magrini 2021 (real-time control)** | **~300 kHz** | **~2 mHz** | **~10⁻⁹** | **~16 mHz** | **~63 s** | **~200 s** |
| Membrane-in-middle (cryo) | 100 kHz | ~30 mHz | ~5×10⁻⁸ | ~240 mHz | ~4.2 s | ~13 s |

**Priority targets for Track A:** Delic 2020 and Magrini 2021 are the cleanest Aspelmeyer-class candidates because:
- Both are at the **deepest quantum side** (`D ~ 10⁻⁹`), so the envelope prediction is cleanest.
- Magrini 2021's real-time feedback architecture **continuously records `x(t)`** — the most plausible source of long contiguous records.
- Both have publicly downloadable theses for context, but **raw heterodyne `x(t)` lives only in group archives**.
- The predicted 63-second envelope period is the **most demanding** detection — requires ≥ 200 s of contiguous record.

## 4. Track A analysis pipeline (runs once raw data is obtained)

### 4.1 Input specification

Required from Aspelmeyer group (one of):

- Contiguous raw heterodyne `x(t)` time series, duration ≥ 200 s (Delic) or shorter for higher-`γ_dec` systems.
- Sampling rate ≥ 10× `ω_m/(2π)` (so ≥ 3 MHz for Delic, 1 MHz for Magrini) — heterodyne bandwidth typically exceeds this requirement by orders of magnitude.
- Phase information preserved (amplitude-only demodulated data lose the envelope structure).
- Metadata: experimental parameters (particle mass, mode frequencies, cooling laser powers, inferred `γ_dec` and `n̄`), cooling protocol, any applied feedback.

### 4.2 Pipeline steps

```
Raw x(t) (N samples at f_s ≥ 10·ω_m/(2π))
    │
    ▼
Quality gate: check sampling rate, record length ≥ 3·T_v, no gaps
    │
    ▼
Heterodyne demodulation at ω_m → complex envelope z(t) = x_hetdy(t)·e^(-iω_m t) low-passed
    │ (bandwidth of LPF: 10·ω_v predicted ≈ 160 mHz for Delic)
    ▼
Amplitude envelope: A(t) = |z(t)|
Phase: φ(t) = arg(z(t))
    │
    ▼
Envelope detrend: remove slow drifts over record (polynomial order 2 or high-pass at 0.1·ω_v)
    │
    ▼
Envelope PSD: Welch-estimated power spectrum of A(t)
    │
    ▼
F0 test: peak-find in PSD in band [ω_v/3, 3ω_v]
    │
    ▼
Fit envelope PSD peak to Lorentzian → extract ω_v_measured and Q_v
    │
    ▼
Ringdown fit on envelope: A(t) = A_0·e^(-γ_v t)·cos(ω_v t + φ) + noise
    │ → measure N_osc (full cycles of envelope in record)
    ▼
Third-harmonic: PSD amplitude at 3·ω_v_measured relative to fundamental
    │
    ▼
Bispectrum / triad coupling: cross-frequency power for triples satisfying ω_3 = ω_1 + ω_2
    │ in PSD peaks
    ▼
Report: (ω_v_measured, Q_v, N_osc, harmonic_ratio, triad_coupling) with 95% bootstrap CIs
    │
    ▼
Decision tree: F0 through F5 per §5.3
```

### 4.3 Script

Write `analysis/scripts/ed_09_5/optomechanics_envelope_reanalysis.py`. Inputs: HDF5 or CSV of raw `x(t)` + metadata JSON. Outputs:

- `envelope_result.json` — all measured quantities with CIs.
- Figures: raw `x(t)` segment, demodulated `z(t)`, envelope `A(t)`, envelope PSD with predicted `ω_v` marker, Lorentzian fit, ringdown fit, bispectrum.
- `decision.md` — F0–F5 outcomes with explicit interpretation.

## 5. Track A decision tree

| Outcome | F0 | F2 ∧ F3 | F4 ∧ F5 | Interpretation |
|:---|:---:|:---:|:---:|:---|
| **Full PASS** | pass | pass | pass | **ED-09.5 confirmed in optomechanics.** All three independent dimensions of test match the ED prediction. This is the highest-impact positive outcome in the ED empirical program to date. Full paper; immediate outreach. |
| **Linear PASS** | pass | pass | fail | Envelope exists at predicted frequency with predicted linear dynamics, but cubic (triad) structure absent. Suggests ED's linear sector is correct; triad coupling `C` is regime-suppressed in optomechanics. Interesting partial result; publishable as narrowed claim. |
| **Frequency PASS** | pass | fail | (either) | Envelope exists at predicted frequency, but `N_osc` or `Q_v` do not match. Suggests §15 anchoring is right but ED-Phys-17 parameter set does not transfer; needs regime-specific `N_osc` derivation. |
| **FAIL (structural)** | fail | — | — | No envelope at predicted `ω_v`. §15 anchoring `τ_v = 1/γ_dec` is wrong in this regime. Two sub-cases: (a) envelope exists at different frequency → §15 revision needed; (b) no envelope anywhere → F1 falsified. |
| **UNDECIDABLE** | — | — | — | Record too short for ≥ 3 envelope cycles OR sampling rate insufficient OR SNR inadequate. Request longer / cleaner trace. |
| **Candidate-(c) salvage** | fail (in multiple datasets) | — | — | Candidate (b) `v ↔ X_cav` identification (§22) is wrong. Shift to candidate (c) `v ↔ internal triad mode` — re-derive predicted `ω_v` from internal-mode coupling. Different regime (matter-wave, Pillar B of Vienna map). |

---

# TRACK B — FRAP-Side Lomb-Scargle Reanalysis (self-contained)

**Status: runs today.** No third-party dependency. Requires only public FRAP recovery curves from the cell-biology literature. This track is fundamentally different from Track A in physical observable (1D recovery curve residual, not 2D field) and accessibility (public data, not group-archived raw).

## 6. Conceptual mapping: optomechanics → FRAP

The §15 derivation `ω_v = 2π·N_osc·γ_dec` is regime-agnostic — it follows from the ED PDE's damping-discriminant structure and is not specific to cavity-coupled systems. For FRAP in the condensed-matter regime:

| Optomechanics | FRAP analogue |
|:---|:---|
| Mechanical mode `x(t)` | Recovery curve `I(t)` (normalised ROI intensity) |
| Mechanical frequency `ω_m` | Characteristic diffusion frequency `1/τ_D` (ms–s for BSA regime) |
| Decoherence rate `γ_dec` | Participation-channel damping inferred from the mobility-bound-derived `D_eff` |
| Predicted envelope `ω_v` | High-frequency residual oscillation on top of the smooth recovery |

**Predicted `ω_v` for FRAP-BSA regime:** `γ_dec` at BSA volume fractions `φ ∈ [0.15, 0.25]` in the condensed-matter regime is of order `10–100 s⁻¹` (from the mobility-channel timescale at these fractions). Giving predicted `ω_v/(2π) = 8·γ_dec` in the **~80–800 Hz** range. This is the origin of the orientation doc's §7 "80–800 Hz" target band.

**Observable:** subtract the best-fit standard recovery model `I_model(t)` (e.g. Soumpasis 1983 exponential, or PME-Barenblatt if UDM is confirmed) from the recovered curve `I(t)`, then compute the Lomb-Scargle periodogram of the residual `r(t) = I(t) − I_model(t)`. ED-09.5 predicts a peak in the residual PSD at `ω_v/(2π) ∈ [80, 800] Hz` with `Q_v ∈ [4, 9]` and 3–6% third-harmonic content.

## 7. Target datasets for Track B

**Self-acquired (from UDM-FRAP session, once CP returns data).**

- 20 acquisitions from [`UDM-FRAP protocol`](../FRAP-High-BSA_InProcess/protocol.md) (4 concentrations × 5 replicates) at frame rates 10 Hz initial, 0.5 Hz tail.
- **Problem: frame rate is too slow.** At 10 Hz the Nyquist is 5 Hz, far below the predicted 80–800 Hz envelope. **Track B on UDM-FRAP data is not viable without a dedicated high-framerate acquisition.**
- **V2 UDM-FRAP amendment (if CP agrees):** request one acquisition per concentration at **≥ 2 kHz** frame rate on a smaller ROI (e.g. 64 × 64 pixels) for 1–5 seconds, as an add-on to the main 5-minute 10-Hz acquisition. This gives Nyquist at 1 kHz, covering the full predicted 80–800 Hz band.

**Public datasets (preferred for initial Track B execution):**

High-framerate (≥ 1 kHz) FRAP datasets from the cell-biology literature where raw or minimally-processed recovery curves have been deposited. Candidates to survey:

- **Mueller et al. 2008 PNAS** (p53 FRAP at ~100 Hz) — supplementary data.
- **Kang et al. 2012 Biophys J** (membrane-protein FRAP at 100–1000 Hz) — various supplementary datasets.
- **Wachsmuth et al. 2003 J Cell Biol** (chromatin-binding protein FRAP) — some curves at 100 Hz.
- **Reviewer note:** most published FRAP is in the dilute regime (low `D`, hence low predicted `ω_v`). The 80–800 Hz prediction is for **concentrated** systems — finding literature data matching the concentration requirement is the main search challenge.

**Track B is realistically viable today only on:**
1. Our own UDM-FRAP acquisition if we add a high-framerate add-on (V2 amendment to CP submission).
2. A targeted literature dig for existing high-framerate concentrated-FRAP datasets.

## 8. Track B analysis pipeline

### 8.1 Input specification

Recovery curve `I(t)` with:
- Sampling rate ≥ 2 kHz.
- Duration ≥ 1 second (for ≥ 100 cycles at the low end of the band, ≥ 800 cycles at the high end).
- Pre-bleach baseline ≥ 0.5 s for normalisation.
- Known or estimable `D_eff` for the system (to compute expected `γ_dec`).

### 8.2 Pipeline

```
Raw I(t) at sampling rate f_s ≥ 2 kHz
    │
    ▼
Normalise: I_norm(t) = (I(t) − I_min) / (I_pre − I_min)
    │
    ▼
Fit standard recovery model (Soumpasis / PME-Barenblatt / two-component exponential)
    │ → I_model(t) with residual r(t) = I(t) − I_model(t)
    ▼
Residual quality gate: check |r(t)| / σ_I < 0.05 on average (not dominated by fit error)
    │
    ▼
Lomb-Scargle periodogram of r(t), frequency grid [10, 2000] Hz
    │
    ▼
Identify peak(s) in [80, 800] Hz band → measure ω_v, peak height, 95% bootstrap CI
    │
    ▼
Predict ω_v from system γ_dec = f(D_eff, volume fraction) via §6 mapping
    │
    ▼
F0 test: ω_v_measured within factor-of-2 of ω_v_predicted?
    │
    ▼
Fit Lorentzian to peak → Q_v; compute N_osc from ringdown of r(t) filtered near ω_v
    │
    ▼
F2–F3 tests on N_osc, Q_v
    │
    ▼
Third-harmonic test (F4): Lomb-Scargle peak at 3·ω_v
    │
    ▼
Triad test (F5): bispectral cross-coupling in residual
    │
    ▼
Report + decision tree
```

### 8.3 Script

Write `analysis/scripts/ed_09_5/frap_envelope_lombscargle.py`. Inputs: CSV of `(t, I)` + metadata (system `D_eff` estimate). Outputs:

- `lombscargle_result.json` — per-dataset measurements with CIs.
- Figures: raw curve + model fit, residual time series, Lomb-Scargle PSD with predicted-band highlight, Lorentzian fit, third-harmonic/triad check.
- `decision.md` — F0–F5 per §5.3 adapted for Track B.

## 9. Track B decision tree

Same structure as Track A (§5.3) but with Track-B-specific interpretations:

| Outcome | F0 | F2 ∧ F3 | F4 ∧ F5 | Interpretation |
|:---|:---:|:---:|:---:|:---|
| **Full PASS** | pass | pass | pass | **ED-09.5 confirmed in condensed-matter regime.** This is actually a STRONGER result than Track A PASS because: (a) self-contained — no collaboration risk; (b) multiple independent datasets possible; (c) regime-bridging — matches the cross-regime ED prediction. Major publishable result. |
| **Linear PASS** | pass | pass | fail | Envelope at predicted frequency with matching dynamics, but no triad structure. Partial support; publishable as narrowed ED-09.5 claim. |
| **Frequency PASS** | pass | fail | — | Envelope at right frequency, wrong dynamics. Suggests §15 anchoring is correct but `N_osc = 8` does not transfer to condensed-matter regime. |
| **FAIL (structural)** | fail | — | — | No envelope at predicted `ω_v`. Needs re-examination of the condensed-matter mapping of `γ_dec` (§6). |
| **UNDECIDABLE** | — | — | — | Residual dominated by fit error, or frame rate insufficient, or dataset too short. Request different dataset. |
| **PARTIAL-DATASET** | mixed across datasets | — | — | If Track B is run on multiple literature datasets and they disagree, flag the disagreement as a regime-splitting indicator. |

## 10. Why Track B can be executed this week

Unlike Track A, Track B has no blocking dependency:

1. **No facility time required** — reanalyses existing data.
2. **No collaboration required** — the orientation's "runs without anyone's permission" framing applies.
3. **Script complexity is low** — Lomb-Scargle is a one-function standard-library call (`scipy.signal.lombscargle` or `astropy.timeseries.LombScargle`).
4. **Main blocker is finding high-framerate concentrated-FRAP data in the literature.** ~1 day of literature search.

**Recommended Track B execution sequence:**

1. **Day 1**: literature search for candidate datasets (criteria: FRAP in concentrated regime, sampling ≥ 1 kHz, raw recovery curve deposited). Target ~5 candidates.
2. **Day 2–3**: write `frap_envelope_lombscargle.py` and validate on a synthetic dataset (known `ω_v` injected, recovered).
3. **Day 4–5**: run on candidate datasets; report per-dataset F0–F5.
4. **Day 6–7**: write up result (paper, memo, or null-result report) depending on outcome.

**Total: 1 week** for a complete self-contained ED-09.5 test with a binary outcome. This is **the fastest path to a new ED empirical result in the entire program.**

---

# 11. Deliverables (both tracks)

## 11.1 Raw-data deliverables

```
data/ED-Data-ED-09-5/
├── TrackA_optomechanics/
│   ├── delic_2020/
│   │   ├── x_t_raw.h5             # from Aspelmeyer (pending)
│   │   ├── metadata.json
│   │   └── analysis_output/
│   ├── magrini_2021/
│   │   └── (same structure)
│   └── README.md
├── TrackB_frap/
│   ├── literature_datasets/
│   │   ├── mueller_2008/
│   │   │   ├── recovery_curves.csv
│   │   │   ├── metadata.json
│   │   │   └── source.bib
│   │   ├── kang_2012/
│   │   └── (others)
│   ├── in_house_udm_frap/         # if V2 amendment with high-framerate add-on
│   │   └── (per concentration × replicate)
│   └── README.md
└── session_log.md
```

## 11.2 Analysis scripts

```
analysis/scripts/ed_09_5/
├── optomechanics_envelope_reanalysis.py   # Track A pipeline
├── frap_envelope_lombscargle.py           # Track B pipeline
├── synthetic_envelope_validation.py       # unit test with known ω_v injected
├── tests/
│   └── test_envelope_pipelines.py
└── README.md
```

## 11.3 Result deliverables (per dataset)

```json
{
  "dataset_id": "magrini_2021_run_01",
  "track": "A",
  "system_params": {
    "omega_m_Hz": 3.0e5,
    "gamma_dec_Hz": 2.0e-3,
    "n_bar_cooled": 0.5,
    "D_computed": 6.67e-9
  },
  "predicted": {
    "omega_v_Hz": 1.6e-2,
    "T_v_s": 62.8,
    "Q_v": 6.3,
    "harmonic_ratio": 0.045
  },
  "measured": {
    "omega_v_Hz": null,
    "Q_v": null,
    "N_osc": null,
    "harmonic_ratio": null,
    "triad_coupling": null
  },
  "falsification_results": {
    "F0": "pending",
    "F2": "pending",
    "F3": "pending",
    "F4": "pending",
    "F5": "pending"
  },
  "verdict": "pending",
  "notes": "..."
}
```

## 11.4 Repo-level deliverables

On **Full PASS** (Track A or B or both):
- `papers/ED-09-5-Envelope/paper.md` — the manuscript.
- Update [`RESULTS.md`](../../RESULTS.md) with ED-09.5 as a confirmed participation-channel result.
- Update [`ED-Orientation.md`](../../docs/ED-Orientation.md) §7: row(s) from ⏳ to ✓.
- **Consider immediate outreach:** this is the single most distinctive ED prediction; confirmation is publication-quality at a level that changes the program's external profile.

On **FAIL**:
- Narrow ED-09.5 to the regimes where it survives (or retract if both tracks fail).
- Document as "ED-09.5 falsified in regime X" memo in `papers/ED-09-5-Envelope/falsification_memo.md`.
- ED's other evidence legs (UDM, Cluster Merger-Lag) remain intact; the single most distinctive prediction is either gone or narrowed — still a scientifically useful outcome.

---

# 12. Budget and timeline

| Track | Phase | Effort | Cost | Calendar |
|:---|:---|:---|:---|:---|
| **A** | Draft & send Aspelmeyer email v3 | 2–4 hr your time | $0 | 1–2 weeks (cold-reader pass + polish) |
| **A** | Aspelmeyer response window | — | $0 | 2 weeks – 3 months (unknown) |
| **A** | Reanalysis on raw `x(t)` (once received) | 1 week | $0 | 1 week post-receipt |
| **A** | Write-up | 1–2 weeks | $0 | 1–2 weeks |
| **Total Track A** | — | ~3 weeks of your time | $0 | **2–6 months** (gated by Aspelmeyer response) |
| **B** | Literature search for candidate datasets | 1 day | $0 | Day 1 |
| **B** | Write + validate pipeline | 2 days | $0 | Days 2–3 |
| **B** | Run on candidates + analysis | 2 days | $0 | Days 4–5 |
| **B** | Write-up (or null memo) | 2–3 days | $0 | Days 6–7 |
| **Total Track B** | — | **~1 week** | **$0** | **1 week from today** |
| **B (with V2 FRAP amendment)** | Add high-framerate acquisition | — | 1–2 hr extra scope time (~$200) | +2–3 weeks after UDM-FRAP |

**Track B is the cheapest and fastest ED empirical test in the entire program.** Its only dependency is finding suitable literature data.

---

# 13. Risks and mitigations

## Track A risks

| Risk | Probability | Mitigation |
|:---|:---|:---|
| Aspelmeyer declines data request | Medium | Email v3 framing (§7 of strategy doc) makes the ask proportionate; offer co-authorship; publicly-available thesis basis strengthens request |
| Aspelmeyer responds slowly | High | Parallel execution of Track B; timeline buffered |
| Raw `x(t)` doesn't preserve phase | Medium | Ask explicitly; if amplitude-only, run on the envelope directly (no demodulation), with reduced discriminating power |
| Record length too short for Delic | Medium | Request Magrini 2021 instead (real-time feedback architecture → continuous recording) |
| `γ_dec` estimate in §3 table off by factor 5 | Low | Check against Delic 2020 Methods supplementary; widen F0 search band to factor-of-10 to start |
| Candidate-(b) identification wrong | Medium (§20 manual thesis skim was null) | Pre-registered fallback: candidate (c) `v ↔ internal triad mode` (Pillar B of Vienna map), different regime |

## Track B risks

| Risk | Probability | Mitigation |
|:---|:---|:---|
| No public concentrated-FRAP data at ≥ 1 kHz | Medium-high | V2 amendment to UDM-FRAP for in-house high-framerate add-on; possibly open new CP request for a dedicated high-framerate session |
| Lomb-Scargle peak buried in fit-model error | Medium | Use multiple recovery models and check consistency; PME-Barenblatt from UDM result gives tighter residual than Soumpasis |
| Frame-rate drift in literature data | Low | Standard Lomb-Scargle handles unevenly sampled data natively |
| `γ_dec` estimate wrong for BSA at ~300 mg/mL | Medium | Use the orientation doc's "80–800 Hz" band as the pre-registered search range; if null in this band, scan wider and report |
| Partial confirmation (some datasets pass, others fail) | Medium | §9 decision tree PARTIAL-DATASET interpretation: publishable as regime-splitting indicator |

---

# 14. Connection to the broader ED empirical program

**This is test 3+4 of the 4 ED predictive experiments.** Track A and Track B are listed separately below because they test the same physical prediction in different regimes with different accessibility profiles.

| # | Test | Channel | Track | Status |
|:---:|:---|:---|:---|:---|
| 1 | AFM dewetting | architectural / mobility-curvature | — | [Protocol](../AFM-Dewetting-ED-SC_InProcess/protocol.md) |
| 2 | UDM FRAP (BSA) | mobility | — | [Protocol sent to CP](../FRAP-High-BSA_InProcess/protocol.md) |
| **3** | **ED-09.5 Aspelmeyer optomechanics envelope** | **participation** | **Track A (this doc)** | **Aspelmeyer email pending** |
| **4** | **ED-09.5 FRAP-side Lomb-Scargle** | **participation** | **Track B (this doc)** | **Self-contained; 1 week to result** |

**Why the participation channel has TWO entries in the empirical program:**

The participation channel `v(t)` is the ED PDE's most distinctive feature — a **global, non-local mode** that modulates the local dynamics via a telegraph-oscillation structure. Its sharp-transition prediction (ED-09.5) is the single most distinctive ED prediction. Because the participation-envelope frequency `ω_v` is determined by the system's decoherence rate `γ_dec`, the **same** prediction manifests at very different absolute frequencies in different regimes:

- Optomechanics at `γ_dec ~ 2 mHz`: `ω_v ~ 16 mHz`, envelope period ~63 s — requires contiguous long records from a specialised facility.
- Concentrated FRAP at `γ_dec ~ 10–100 Hz`: `ω_v ~ 80–800 Hz` — requires high-framerate FRAP acquisition.

The two tracks are **not redundant**; they are independent tests of the same ED-09.5 prediction at different regime endpoints. **A Full PASS on both tracks would be the strongest possible evidence for ED-09.5** — the same participation-mode prediction confirmed across 10+ orders of magnitude in `γ_dec`.

---

# 15. References

## Theory

- [`ED-09-5-Experimental-Strategy.md`](../../docs/ED-09-5-Experimental-Strategy.md) — §1.5 formal framing; §6 theory memo scope; §7 Aspelmeyer email draft.
- [`ED-09-5-Observable-Sharpening.md`](../../docs/ED-09-5-Observable-Sharpening.md) — v0.9; full theoretical derivation; §11 channel-weight mapping; §15 `ω_v` derivation; §16 falsification criteria F0–F5; §22 candidate-(b) identification.
- [`ED_Vienna_Program_Map.md`](../../docs/ED_Vienna_Program_Map.md) — 12-target Vienna ecosystem map.
- [`ED-Orientation.md`](../../docs/ED-Orientation.md) §5.5 ED-09.5 summary; §7 empirical-status table.
- [`theory/Architectural_Canon.md`](../../theory/Architectural_Canon.md) — Canon P6 Damping Discriminant.
- PhilArchive: *Event Density and the Quantum-Classical Boundary* (ED-09.5).

## Optomechanics datasets (Track A)

- Delić, U., Reisenbauer, M., Dare, K., Grass, D., Vuletić, V., Kiesel, N. & Aspelmeyer, M. *Cooling of a levitated nanoparticle to the motional quantum ground state.* Science **367**, 892–895 (2020). DOI: `10.1126/science.aba3993`.
- Magrini, L., Rosenzweig, P., Bach, C., Deutschmann-Olek, A., Hofer, S. G., Hong, S., Kiesel, N., Kugi, A. & Aspelmeyer, M. *Real-time optimal quantum control of mechanical motion at room temperature.* Nature **595**, 373–377 (2021). arXiv:[2012.15188](https://arxiv.org/abs/2012.15188).
- Delic, U. *Cavity cooling by coherent scattering of a levitated nanosphere in vacuum.* PhD thesis, Vienna (2019).
- Magrini, L. *Quantum measurement and control of mechanical motion at room temperature.* PhD thesis, Vienna (2021).
- Chan, J., Alegre, T. P. M., Safavi-Naeini, A. H., Hill, J. T., Krause, A., Gröblacher, S., Aspelmeyer, M. & Painter, O. *Laser cooling of a nanomechanical oscillator into its quantum ground state.* Nature **478**, 89–92 (2011).

## FRAP datasets (Track B candidates)

- Mueller, F., Wach, P. & McNally, J. G. *Evidence for a common mode of transcription factor interaction with chromatin as revealed by improved quantitative fluorescence recovery after photobleaching.* Biophys J **94**, 3323–3339 (2008).
- Kang, M., Day, C. A., Kenworthy, A. K. & DiBenedetto, E. *Simplified equation to extract diffusion coefficients from confocal FRAP data.* Traffic **13**, 1589–1600 (2012).
- Wachsmuth, M., Weidemann, T., Müller, G., Hoffmann-Rohrer, U. W., Knoch, T. A., Waldeck, W. & Langowski, J. *Analyzing intracellular binding and diffusion with continuous fluorescence photobleaching.* Biophys J **84**, 3353–3363 (2003).
- Soumpasis, D. M. *Theoretical analysis of fluorescence photobleaching recovery experiments.* Biophys J **41**, 95–97 (1983). — standard FRAP recovery model reference.

## Analysis methods

- Lomb, N. R. *Least-squares frequency analysis of unequally spaced data.* Ap&SS **39**, 447–462 (1976).
- Scargle, J. D. *Studies in astronomical time series analysis. II. Statistical aspects of spectral analysis of unevenly spaced data.* ApJ **263**, 835–853 (1982).
- `scipy.signal.lombscargle`, `astropy.timeseries.LombScargle` — standard implementations.

---

*This protocol mirrors the canonical operational-protocol structure of [`AFM protocol`](../AFM-Dewetting-ED-SC_InProcess/protocol.md) and [`UDM-FRAP protocol`](../FRAP-High-BSA_InProcess/protocol.md). Track A remains blocked on Aspelmeyer response; Track B is executable within one week of protocol adoption. Both tracks test the same underlying ED-09.5 prediction — the sharp damping bifurcation at `D_crit = 0.5` manifesting as a participation-mode envelope at `ω_v = 2π·N_osc·γ_dec` — in regimes separated by 10+ orders of magnitude in `γ_dec`.*
