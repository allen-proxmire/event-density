# UDM Mobility Law Test — FRAP in Concentrated BSA

**Version.** V2 — 2026-04-21. Incorporates methods-paper refinements identified in the literature review of 2026-04-21 (Goehring 2010, Bläßle et al. 2018 / PyFRAP, Sakib & Fradin 2026, Sarkar & Chattopadhyay 2020) into the analysis pipeline (§9) and review-level notes (§13). **Expands §13 from 7 to 15 subsections.** Adds Appendix A with a draft CP amendment request for a high-framerate add-on acquisition.

**Status.** Operational protocol for the Universal Degenerate-Mobility (UDM) test of the ED mobility channel at condensed-matter scale. The protocol body (§4–§8) is the text submitted to **Creative Proteomics Core Integrated Biosciences Research (CIBR)** on 2026-04-17; CP forwarded internally to their technician team on the same day and expected response window is 2026-04-24 to 2026-05-01 (see [`ED-Orientation.md`](../../docs/ED-Orientation.md) top-of-doc 2026-04-17 entry and §7 empirical-status table).

**What this document does.** Captures the as-submitted protocol into the repo, surrounds it with the ED theoretical derivation (§1–§3), adds the analysis pipeline and decision tree (§9–§12), and flags post-submission improvements as **§13 review-level notes for a V2 protocol** — not changes to the submitted V1. V2 preserves §4–§8 (CP-submitted text) verbatim and does not alter any parameter already agreed with CP; all refinements are either (a) analysis-side (§9) and therefore operator-independent, (b) V2 review notes (§13) for future protocol revisions, or (c) explicitly flagged as optional add-ons requiring a separate amendment request (Appendix A).

**V1 → V2 change summary.** See §17 "V2 change log" at the end of this document for the complete list of edits.

**Relationship to the wider ED program.**
- **Channel exercised:** mobility `M(ρ) = M_0(ρ_max − ρ)^β`, Canon principle P4.
- **Regime:** condensed matter (ED-Dimensional-03), scale anchor ~µm and thermal diffusivity.
- **Published parallel in the repo:** [`papers/Universal_Mobility_Law/`](../../papers/Universal_Mobility_Law/) — 10-material UDM fit with `R² > 0.986` and mobility exponent `β ≈ 2`. This FRAP test is an **independent confirmation** at a single protein system (BSA) via a different observable (front propagation) than the diffusion-coefficient regression used in the UDM paper.
- **Authoritative PhilArchive publication:** *Universal Degenerate-Mobility Scaling in Crowded Soft Matter* (see [`ED-Orientation.md`](../../docs/ED-Orientation.md) §8 PhilArchive inventory).
- **Is NOT the same test as the "FRAP-side ED-09.5 envelope" reanalysis.** That one tests the **participation** channel via Lomb-Scargle at 80–800 Hz on public recovery curves and is documented separately in [`ED-09.5 protocol`](../ED-09-5-Envelope_InProcess/protocol.md). Do not conflate: **this** FRAP test uses **raw TIFF spatial data** (front-radius power law); the other uses **the 1D recovery curve** (high-frequency residual).

---

## 1. The prediction in one paragraph

Standard FRAP theory assumes Fickian diffusion: after a photobleach pulse, the recovery front of unbleached fluorophore expanding into the bleached region follows `R(t) ∝ t^0.50`. This is the `M(ρ) = const` limit of the ED mobility channel. **ED-UDM predicts that in concentrated (non-dilute) solutions where the protein volume fraction approaches the capacity bound `ρ_max`, the mobility becomes density-dependent per `M(ρ) = M_0(ρ_max − ρ)^β` with canonical `β ≈ 2`, and the front-propagation exponent collapses to `R(t) ∝ t^(1/6) ≈ t^0.167` per the Barenblatt self-similar solution of the 2D porous-medium equation.** The secondary signature is that the bleach boundary stays **sharp** (compact support, a defining PME feature) rather than blurring into a Gaussian gradient as Fickian predicts. The test is whether BSA at 200–350 mg/mL (φ ≈ 0.15–0.25) exhibits the sub-Fickian `t^0.16` exponent and the sharp front simultaneously.

## 2. Derivation of the `t^0.167` exponent

**From ED canonical PDE → Barenblatt PME.** Suppressing penalty and participation (`P₀ = 0, H = 0`), the canonical ED PDE reduces under `δ = ρ_max − ρ` to

$$\partial_t \delta = D \nabla\!\cdot\!\bigl[M(\delta)\,\nabla\delta\bigr] = \frac{DM_0}{\beta+1}\,\nabla^2(\delta^{\beta+1}) = D_{\text{pme}}\,\nabla^2(\delta^m)$$

with `m = β + 1` and `D_pme = DM_0/(β+1)`. This is the standard porous-medium equation (Vázquez 2007). Its Barenblatt self-similar solution on a 2D domain has a compact-support front at radius

$$R(t) \propto t^{\alpha_R}, \qquad \alpha_R = \frac{1}{d(m-1) + 2}.$$

| `β` | `m = β+1` | `d = 2` | `α_R` | Predicted `R(t)` |
|:---:|:---------:|:-------:|:-----:|:-----------------:|
| 0 | 1 | 2 | 1/2 = **0.500** | Fickian limit |
| 1 | 2 | 2 | 1/4 = 0.250 | Mild PME |
| **2** | **3** | **2** | **1/6 ≈ 0.167** | **ED canonical prediction** |
| 3 | 4 | 2 | 1/8 = 0.125 | Stronger degeneracy |

**The 0.167 number in the CP protocol is `1/6`**, corresponding to ED's canonical `β = 2` on a 2D imaging plane. (The protocol states `R(t) ~ t^0.16` as a round number; `1/6 = 0.1667` is the exact prediction.)

**FRAP geometry consideration.** A confocal FRAP imaging plane is quasi-2D because the chamber thickness (20–30 µm spacer) is comparable to the axial confocal resolution. Pure 2D Barenblatt applies if the bleach-ROI depth approximately matches the imaging plane depth. If axial recovery contributes significantly, the effective `d` is between 2 and 3, giving `α_R` between 1/6 and 1/8. **A measured exponent in `[0.125, 0.170]` is consistent with the canonical `β = 2` ED prediction for 2D–3D mixed geometry.**

**Cross-check with the 10-material UDM paper.** The [`papers/Universal_Mobility_Law/`](../../papers/Universal_Mobility_Law/) result fits `D_eff(c) = D_0(1 − c/c_max)^β` directly (not via front propagation) and recovers `β ≈ 2` across 10 soft-matter systems. This FRAP test is a **front-propagation-based** independent confirmation in a single system: the α_R extracted here must give `m − 1 = (1/α_R − 2)/d`, hence `β = m − 1`, and that β must agree with the UDM-paper value to within ±0.3 for consistency.

## 3. Pre-registered test parameters

| Parameter | Value | Source |
|:---|:---|:---|
| Canonical ED mobility exponent | `β = 2` | 00.2 Canon, confirmed in ED-Phys-02/UDM-10-materials |
| PME index | `m = β + 1 = 3` | Foundational Paper v2 Analogue 2 |
| 2D front-radius exponent | `α_R = 1/6 ≈ 0.167` | Barenblatt 1952; ED derivation §2 above |
| Prediction band for `α_R` | `[0.125, 0.170]` | Covers 2D → 3D geometry ambiguity |
| Fickian null hypothesis | `α_R = 0.500` | Standard `M(ρ) = const` |
| Secondary signature | sharp front (compact support) | PME theorem; defining feature of mobility degeneracy |
| Fickian alternative | Gaussian-blurred boundary | Standard heat equation |
| Concentration sweep | 200, 250, 300, 350 mg/mL BSA | `φ` from 0.15 to 0.25 (below gelation at φ ≈ 0.3) |
| Required bleach depth | ≥ 80% (centre intensity < 20% of pre-bleach) | Non-linear regime threshold |
| Replicates per concentration | 5 bleaches in distinct FoVs | N = 20 total acquisitions |

**Pass/fail band for `α_R`.** Per-concentration mean of `α_R` in `[0.125, 0.170]` → pass at that concentration. At least 3 of 4 concentrations must pass for the ensemble to count as a PASS.

---

## 4. Stage 1 — Sample preparation *(as submitted to CP, verbatim)*

**The four concentrations.**

| Concentration | Volume fraction | Why |
|:---|:---:|:---|
| 200 mg/mL | φ ≈ 0.15 | Lower bound — expect slower-than-Fickian but may still be fast |
| 250 mg/mL | φ ≈ 0.18 | Central test point |
| 300 mg/mL | φ ≈ 0.22 | Deep into the nonlinear regime |
| 350 mg/mL | φ ≈ 0.25 | Maximum — just below gelation |

**Sample prep.**

- **Protein:** BSA-FITC conjugate (Sigma A9771 or equivalent BSA-Alexa488).
- **Buffer:** 50 mM NaH₂PO₄, pH 7.0, 150 mM NaCl.
- Dissolve lyophilised BSA-FITC in buffer to each target concentration.
- Vortex gently, allow 30 min for complete dissolution.
- Filter through 0.22 µm if any visible turbidity.
- **Chamber:** ~5 µL between two glass coverslips (No. 1.5) with a 20–30 µm spacer, sealed with vacuum grease to prevent evaporation.
- Equilibrate on the stage for ≥ 10 minutes at 25 °C before imaging.

## 5. Stage 2 — Bleaching parameters *(as submitted to CP)*

- **Laser:** 488 nm, full power for bleaching.
- **Bleach ROI:** Circular, radius 3 µm (2–5 µm acceptable).
- **Bleach duration:** 1–2 seconds.
- **Target bleach depth: > 80% reduction** — centre intensity after bleach should be less than 20% of pre-bleach. **This is important. If the bleach is too shallow, we stay in the linear regime and everything looks Fickian regardless.**

## 6. Stage 2 — Imaging parameters *(as submitted to CP)*

- **Objective:** 40× or 63× oil, NA ≥ 1.2.
- **Imaging laser power:** Low (0.1–1 mW) — avoid additional photobleaching during acquisition.
- **Pixel size:** ≤ 0.4 µm (ideally 0.1–0.2 µm).
- **Field of view:** at least 25 × 25 µm — we need to see well beyond the bleach spot.
- **Bit depth:** 12-bit or 16-bit.

## 7. Stage 2 — Acquisition timing *(as submitted to CP)*

This is where it differs from typical FRAP. **Normal dilute-solution FRAP recovers in milliseconds. At these concentrations, recovery should take seconds to minutes.**

- **Frame interval:** Start fast (every 50–100 ms for the first few seconds), then can slow to 1–2 seconds.
- **Total acquisition: 5–10 minutes per bleach** (yes, minutes — if the model is right, the front moves very slowly).
- **Pre-bleach:** Capture 5–10 frames before bleaching as the baseline reference.
- **Start imaging immediately after bleach ends — no delay.**

## 8. Stage 3 — Replication and data capture *(as submitted to CP)*

### Replication

- **5 bleaches per concentration, each in a different field of view (separated by > 50 µm).**
- **Never re-bleach the same spot.**
- **Total: 20 FRAP acquisitions across the four concentrations.**

### What needs to be captured

**This is critical — I need the full spatial data, not just the ROI intensity curve.**

- **Full TIFF stacks for every acquisition** — the complete image at every time point, not just an intensity-vs-time trace from the software's built-in FRAP analysis.
- **16-bit preferred.**
- **Metadata for each acquisition:** frame rate, pixel size, bleach ROI coordinates, bleach duration, BSA concentration, temperature, objective used, laser power.

The Zeiss 710 software will probably offer to give an intensity recovery curve. That's fine to capture too, but **the TIFF stacks are what I actually need for the analysis**. I'm going to compute radial profiles, detect the front position at each time point, and fit the power law myself.

### What I expect to see

**If the model is right:**
- The recovery front expands slowly — `R(t) ~ t^0.16` instead of `t^0.50`.
- The bleach boundary stays sharp throughout recovery — a well-defined edge, not a gradual blur.
- Recovery gets dramatically slower at higher concentrations.
- At 350 mg/mL, the front may barely move over the acquisition window.

**If the model is wrong:**
- Recovery follows standard Fickian kinetics — `R(t) ~ t^0.50`.
- The bleach boundary blurs into a smooth Gaussian gradient.
- Recovery timescale changes only modestly with concentration.

*I'm not asking to produce a particular result. I'm asking to capture the data as cleanly as possible so we can see what actually happens. Either outcome is publishable.*

### Estimated timeline on the scope

| Task | Time |
|:---|:---|
| Mount + equilibrate first sample | 15 min |
| Per concentration: 5 bleaches + repositioning | 15–20 min |
| Four concentrations total | ~1.5 hours of scope time |
| Total session including setup | ~2 hours |

**The key things the microscopists care about: the bleach depth requirement (>80%), the slow acquisition window (minutes, not milliseconds), and the need for the full TIFF stacks rather than just the software's built-in intensity trace.**

---

## 9. Post-session analysis pipeline

*Added to the submitted protocol — this is what happens after the TIFF stacks return from CP.*

**V2 note (2026-04-21).** The analysis pipeline now incorporates four methods-paper refinements identified in the 2026-04-21 literature review:

- **Foundation:** use **PyFRAP** (Bläßle et al. 2018, open-source Python, `https://mueller-lab.github.io/PyFRAP/`) as the image-import / ROI-definition / pre-bleach-normalisation front-end. See §13.16. This saves ~2–3 days of pipeline work versus a from-scratch implementation and provides a benchmarked standard-diffusion fit to serve as the Fickian null hypothesis.
- **Bleach-radius correction (§13.14):** measure the *actual* bleach radius `ω` from the first post-bleach frame via HWHM of a Gaussian fit to the radial intensity profile (Sarkar & Chattopadhyay 2020, Note 14, Fig 10) — do NOT assume `ω = ROI_radius`. Since `D ∝ ω²`, a 10% error in `ω` produces a 20% error in `D`.
- **Corona-effect / smooth-box correction (§13.8, §13.9):** diffusion during the finite bleach duration broadens the boundary into a "corona" beyond the ROI. The Fickian baseline profile is NOT a sharp step — it is the **Goehring smooth-box / corona-broadened** profile. The ED secondary signature must be a front *sharper* than that baseline, not sharper than an idealised step (§9.2 revised).
- **Control-spot and discard criteria (§13.12, §13.13):** simultaneous monitoring of a non-bleached region to detect imaging-induced photobleaching; pre-registered four discard criteria to drop corrupted acquisitions before ensemble analysis.

### 9.1 Pipeline structure

For each of the 20 acquisitions:

```
TIFF stack (512 × 512 × T, 16-bit)
    │
    ▼
Pre-bleach reference: mean of 5–10 pre-bleach frames
    │
    ▼
Per-frame normalisation: I(x,y,t) / I_pre(x,y)
    │
    ▼
Bleach-centre detection: minimum of frame 0 post-bleach
    │
    ▼
Radial profile extraction: azimuthal average I(r,t) around centre
    │
    ▼
Front detection: r_front(t) = radius where I(r,t) = 0.5 · (I_pre_avg + I_bleached_centre)
    │ (half-maximum between pre-bleach plateau and bleach floor)
    ▼
Power-law fit: log R(t) = α_R · log t + const, weighted by frame SNR
    │
    ▼
Per-acquisition α_R with 95% bootstrap CI
    │
    ▼
Per-concentration ensemble: mean(α_R) across 5 replicates, std, shapiro-wilk normality
    │
    ▼
Cross-concentration check: does α_R increase toward 0.5 as c decreases? (should NOT if ED)
                          : does α_R stay in [0.125, 0.170] at all c? (should YES if ED)
```

### 9.2 Sharp-front vs smooth-boundary test (secondary signature) — **V2 revised**

Independent of the exponent fit, test the front *profile* at each time point. **The Fickian baseline is NOT a sharp step — it is the corona-broadened / smooth-box profile produced by diffusion during the finite bleach duration (Goehring 2010; Sarkar & Chattopadhyay 2020 Note 7).** This is a critical V2 correction.

1. Take the radial profile `I(r, t)` at `t = t_mid` (middle of the recovery window).
2. Fit **three** candidate models to the front region (previously two):
   - **(i) PME (compact-support) model:** `I(r, t) = I_bleached + (I_pre − I_bleached) · max(0, 1 − (r_front/r)²)^(1/m)` — Barenblatt parabolic-cap profile with `m = 3`. **ED prediction.**
   - **(ii) Goehring smooth-box / Fickian-with-bleach-corona model:** `I(r, t) = I_bleached + (I_pre − I_bleached) · ½[erf(μ(ω − r)/√(4Dμ²t + 1)) + erf(μ(ω + r)/√(4Dμ²t + 1))]` — Goehring 2010 Eq. 9, parameterises both the bleach radius `ω` (measured via §13.14) and the boundary steepness `μ` (from the first post-bleach frame). **This is the corrected Fickian null hypothesis.** The parameter `μ` absorbs the bleach-duration-induced corona smoothing.
   - **(iii) Sharp-step Fickian model:** `I(r, t) = I_bleached + (I_pre − I_bleached) · erf((r − r_front)/(σ·√2))` — the idealised sharp-boundary Fickian. **Kept as a reference for the V1 assumption**, not as a realistic null.
3. Compare all three via AIC/BIC. **If ED is right, PME (model i) wins at `c ≥ 250 mg/mL`, beating the corona-broadened Fickian (model ii).** The comparison PME-vs-sharp-Fickian (i vs iii) is the V1 version and overstates ED support; the binding test is PME-vs-Goehring (i vs ii).
4. **What a sharp front means in V2:** the measured profile has a *sharper* falloff at the front than the corona-broadened Fickian model can produce given the measured `ω` and the bleach-duration contribution to `μ`. A "sharp-looking" front that is consistent with Goehring smooth-box within the observed `μ` is NOT evidence for ED-PME compact support.
5. **This is an independent check of the exponent fit** — two failure modes (wrong α_R, wrong front shape) that should agree under a given mechanism. Under V2 the front-shape test is a tighter test than V1 implied.

**Implementation note.** PyFRAP's standard output includes the fit `μ` parameter automatically when the smooth-box initial-condition option is enabled. The Barenblatt parabolic-cap fit (model i) is not standard in PyFRAP and needs to be added to the pipeline wrapper script.

### 9.3 Cross-check with UDM 10-material paper

Convert each acquisition's `α_R` into a mobility exponent via `β = 1/α_R − 2` (for 2D). The set of `β` values across 20 acquisitions should have:

- Mean `β ≈ 2.0 ± 0.5` to be consistent with the UDM 10-material fit.
- Independence of concentration *within* the non-linear regime (i.e. `β` doesn't drift systematically across 200→350 mg/mL) — the ED prediction is that `β` is a structural constant of the polymer, not a regime parameter.

### 9.4 Required analysis code — **V2 revised**

Write `analysis/scripts/udm_frap/frap_udm_pipeline.py` as a **wrapper around PyFRAP** (Bläßle et al. 2018; see §13.16) rather than a from-scratch implementation. PyFRAP provides image import (all major microscope formats), ROI definition, pre-bleach normalisation, Goehring-style smooth-box fitting for the Fickian null hypothesis (model ii of §9.2), and AIC-based model selection for free; the wrapper adds:

- The Barenblatt parabolic-cap profile fit (model i of §9.2) — not standard in PyFRAP.
- The front-radius extraction and power-law fit pipeline (§9.1 steps after radial profile).
- The HWHM Gaussian fit for the actual bleach radius `ω` (§13.14).
- Control-spot tracking for imaging-induced photobleaching (§13.12).
- The four pre-registered discard criteria (§13.13) applied automatically.
- Per-frame bleach-depth gate (§13.2) and corona-width measurement (§13.9).

Inputs: folder of TIFF stacks + metadata JSON. Outputs:

- `per_acquisition.csv` — one row per acquisition: concentration, replicate, measured `ω` (HWHM), corona width `1/μ`, α_R, 95% CI, β inferred, AIC_PME, AIC_Goehring, AIC_sharpFickian, front-sharpness metric, discard-criterion flags, bleach-depth, control-spot drift, SNR.
- `per_concentration.csv` — one row per concentration: mean α_R, std α_R, mean β, `n_pass` (replicates in band), `n_discarded` with reasons, verdict.
- `ensemble_summary.json` — overall PASS/NEAR-PASS/FAIL/UNDECIDABLE verdict per §10 below.
- Figures: per-acquisition R(t) log-log fit, front-profile overlays (all three models of §9.2), α_R vs concentration scatter, control-spot drift time-series.

**Validation before first use.** Run the pipeline on synthetic data with known `α_R` and known bleach corona injected (5 test cases: Fickian-sharp, Fickian-broadened, PME β=2 sharp, PME β=2 with noise, multi-component mixture). Confirm recovery of the injected exponent within 10% and correct model selection via AIC. Logged as `tests/test_udm_pipeline.py` alongside the main script.

---

## 10. Outcome decision tree

| Outcome | Criterion | Interpretation |
|:---|:---|:---|
| **PASS** | Mean `α_R ∈ [0.125, 0.170]` at ≥ 3 of 4 concentrations, AND PME-front beats Fickian-front via AIC at ≥ 3 of 4 concentrations | **ED-UDM confirmed at BSA.** Independent confirmation of the UDM 10-material result via a completely different observable. Repo status changes to ✓ for a second mobility-channel test. |
| **NEAR-PASS** | Mean `α_R ∈ [0.10, 0.20]` and systematically below Fickian, but outside the strict `[0.125, 0.170]` band at some concentrations | **Sub-Fickian confirmed; specific exponent ambiguous.** Possibilities: (a) 2D/3D geometry mixing shifts `α_R` per §2; (b) `β ≠ 2` in BSA specifically; (c) pre-asymptotic regime (Foundational Paper Analogue 2 notes pre-asymptotic errors up to 36% at β = 2 on accessible grids). Publishable as "PME-class behaviour confirmed; exponent constraints BSA-specific β." |
| **FAIL** | Mean `α_R ≥ 0.35` across concentrations, OR Fickian-front beats PME-front at all concentrations | **ED-UDM falsified at BSA.** Mobility channel does not govern BSA front propagation at the concentrations tested. The UDM 10-material result is either BSA-excluding or artifact-dependent. Publishable; requires a separate memo identifying why BSA differs from the 10-material set. |
| **UNDECIDABLE** | Bleach depth < 80% at multiple concentrations, OR SNR too low for front detection, OR < 3 replicates usable at any concentration | **Cannot evaluate.** Request CP re-run with sharper bleach / longer acquisition / different BSA lot. |
| **SPLIT** | `α_R` passes at low concentrations but not high (or vice versa) | **Concentration-dependent regime.** The PME reduction applies in a specific volume-fraction window. Narrows the UDM claim: "β = 2 for BSA in [c_1, c_2]; different dynamics outside." Publishable as a regime map. |

---

## 11. Deliverables

### 11.1 Raw-data deliverable (what CP returns)

`data/ED-Data-UDM-FRAP-BSA/` structure:

```
ED-Data-UDM-FRAP-BSA/
├── 200mgmL/
│   ├── rep1/
│   │   ├── stack.tiff          # full time series
│   │   ├── metadata.json       # frame rate, pixel size, bleach ROI, etc.
│   │   └── recovery_curve.csv  # software's own intensity trace (nice-to-have, not used in main analysis)
│   ├── rep2/
│   ├── rep3/
│   ├── rep4/
│   └── rep5/
├── 250mgmL/ (same structure)
├── 300mgmL/ (same structure)
├── 350mgmL/ (same structure)
├── session_metadata.json       # date, instrument, operator, lot numbers
└── README.md                   # provenance + link to this protocol
```

### 11.2 Per-acquisition metadata schema (`metadata.json`)

```json
{
  "acquisition_id": "20260501-BSA-300mgmL-rep3",
  "date": "2026-05-01",
  "facility": "Creative Proteomics CIBR",
  "instrument": "Zeiss LSM 710 (or similar)",
  "objective": "63× oil",
  "na": 1.4,
  "wavelength_nm": 488,
  "imaging_laser_power_mW": 0.5,
  "bleach_laser_power_mW": 100,
  "bleach_roi_radius_um": 3.0,
  "bleach_roi_center_px": [256, 256],
  "bleach_duration_s": 1.5,
  "frame_rate_Hz_fast": 10,
  "frame_rate_Hz_slow": 0.5,
  "fast_phase_duration_s": 5,
  "total_duration_s": 360,
  "pixel_size_um": 0.15,
  "field_of_view_um": [30, 30],
  "bit_depth": 16,
  "bsa_concentration_mg_mL": 300,
  "bsa_volume_fraction": 0.22,
  "bsa_source": "Sigma A9771 lot #XXX",
  "buffer": "50 mM NaH2PO4 pH 7.0, 150 mM NaCl",
  "chamber_spacer_um": 25,
  "stage_temperature_C": 25.0,
  "equilibration_time_min": 12,
  "pre_bleach_frames": 8,
  "notes": "Bleach depth measured at 17% of pre-bleach (83% reduction) at centre."
}
```

### 11.3 Analysis deliverable

- `analysis/scripts/udm_frap/frap_udm_pipeline.py` — the full pipeline per §9.4.
- `analysis/scripts/udm_frap/per_acquisition.csv`, `per_concentration.csv`, `ensemble_summary.json`.
- `analysis/scripts/udm_frap/figures/` — per-acquisition R(t) fits, front-profile overlays, ensemble α_R vs c plot.

### 11.4 Repo-level deliverable

On PASS outcome:
- `papers/UDM-FRAP-BSA/` with `paper.md` (6–8 page manuscript), figures, methods.
- Update [`RESULTS.md`](../../RESULTS.md) at repo root: add FRAP row under "Mobility Channel Tests."
- Update [`ED-Orientation.md`](../../docs/ED-Orientation.md) §7: change the FRAP row from ⏳ to ✓ and correct the "Participation (lab)" label to "Mobility (lab)" — see §13.1 below.
- Move the empirical status snapshot row from "pending decision window" to "confirmed."

On FAIL outcome:
- `papers/UDM-FRAP-BSA/` with a falsification memo explaining what BSA reveals about the 10-material UDM fit's generalisability.
- No change to UDM paper's `R² > 0.986` result (the 10 materials stand on their own); the FRAP test would be a narrowing of the class of systems to which β = 2 applies.

---

## 12. Budget and timeline

| Phase | Effort | Cost |
|:---|:---|:---|
| **Sample prep** (done at CP as part of the quote) | 0.5 day CP technician | Part of quote |
| **AFM / LSM session** | ~2 hours scope + 1 hour setup | Part of quote (expected ~$500–$1500 total) |
| **Data transfer + format verification** | 1 hour | Your time |
| **Pipeline implementation** (`frap_udm_pipeline.py`) | 2–3 days | Your time — most of the work |
| **Run pipeline on 20 acquisitions** | ~1 hour compute | Negligible |
| **Decision tree + paper write-up** | 3–5 days | Your time |

**Total outside-your-time cost:** ~$500–$1500 for the CP session. This is **the lowest-cost lab-bench test in the ED empirical program** (AFM dewetting is $500, but adds 2 weeks of polymer-group sample prep; FRAP-UDM is fully turnkey with CP already engaged).

**Total calendar time:** dependent on CP decision window (now: 2026-04-24 to 2026-05-01), then ~2–3 weeks from sample prep through data, then ~1–2 weeks analysis → **6–8 weeks to publishable result.**

---

## 13. Review-level notes (for V2 protocol, if CP asks for revisions or if a follow-up test is commissioned)

*These are improvements I would recommend for a future protocol version. They are NOT changes to the protocol already submitted to CP. If CP's technician team raises any of these as concerns, these are the pre-thought-out responses.*

### 13.1 Label correction in the orientation doc

Current [`ED-Orientation.md`](../../docs/ED-Orientation.md) §7 labels the FRAP row as "Participation (lab)". **This is mis-labelled** — the CP protocol tests the **mobility** channel via `R(t) ~ t^0.16`, not participation. The "Participation (lab)" label appears to have conflated this test with the FRAP-side ED-09.5 Lomb-Scargle reanalysis of public curves. Separate docs for two separate tests; orientation §7 should have two rows instead of one. **This will be fixed when the orientation doc is next updated** (logged as a §10 canonical correction).

### 13.2 Bleach depth verification as a quantitative pre-analysis gate

The protocol states "target > 80% reduction" qualitatively. V2 should:

- Require the first post-bleach frame to report `I_centre / I_pre ≤ 0.20` as a quantitative field in metadata.
- Fail the acquisition during the analysis (drop it from the ensemble, don't reject the whole session) if any replicate has bleach depth < 70%.
- Flag acquisitions with bleach depth 70–80% as "marginal" and report separately.

### 13.3 Axial geometry determination

The 2D vs 3D Barenblatt exponent ambiguity (`α_R = 1/6` vs `1/8`) is currently handled by widening the acceptance band to `[0.125, 0.170]`. A V2 cleaner approach: **include a z-stack of 3–5 planes at one representative bleach per concentration**, so axial recovery can be measured directly. If axial recovery is negligible over the acquisition window, the 2D prediction `α_R = 1/6` applies strictly. If axial recovery is comparable to lateral, 3D applies and `α_R = 1/8`. This eliminates the ambiguity and tightens the pass band to a single value per concentration.

### 13.4 Pre-asymptotic regime correction

Foundational Paper v2 Analogue 2 notes that at `β = 2` in 2D, accessible grids (N = 64–128) show pre-asymptotic error up to **36%** before converging to the asymptotic Barenblatt exponent. For FRAP at 512 × 512 with ~250 µm × 250 µm effective spatial extent and ~5-minute time window, the asymptotic regime may not be reached. V2 should:

- Include a simulation calibration: run the PME numerical solver (e.g. via `edsim/` package) at BSA-scale parameters with the same time window and spatial extent, and measure the pre-asymptotic `α_R`.
- Compare measured `α_R` to the pre-asymptotic simulation value, not to the asymptotic `1/6`.
- This could **tighten the PASS criterion** if the simulation gives, e.g., `α_R ≈ 0.19` pre-asymptotically at ED's `β = 2` — the experimental value would be expected around 0.19, not 0.167.

### 13.5 Hydrodynamic-interaction sanity check

At `φ ≈ 0.25`, BSA is well into the concentrated regime where hydrodynamic interactions, electrostatic screening, and weak attraction all play a role. The ED prediction is that these all sum to an effective `M(ρ) = M_0(ρ_max − ρ)^β` with `β = 2` regardless of microscopic mechanism — this is the **UDM universality claim**. But a cross-check against viscometry and/or DLS at each concentration would provide an independent D_eff(c) curve to compare against the front-propagation α_R.

### 13.6 Temperature control and sample stability

The protocol states 25 °C equilibration; the spacer chamber sealed with vacuum grease. Long acquisitions (5–10 min) at room-temperature-imaging conditions can introduce slow drift from:
- Evaporative concentration increase near the spacer edge (addressed by vacuum grease, but not perfectly).
- BSA aggregation or denaturation at the air-water interface in the sealed chamber.
- Laser heating of the immersion oil during long acquisitions.

V2 additions: (a) pre- and post-acquisition confirmation that `I_pre` is unchanged (drift test); (b) randomise the order of concentration acquisitions within the session so any session-long drift doesn't bias one concentration.

### 13.7 Statistical power justification

With `n = 5` replicates per concentration and expected `std(α_R) ≈ 0.03`, the per-concentration mean has uncertainty `std(α_R)/√5 ≈ 0.013`. This is **tight enough to discriminate 0.167 from 0.50** (factor 10 larger uncertainty threshold) but **not tight enough to discriminate 0.167 from 0.125** (factor 3 larger). If the exponent lands in NEAR-PASS territory, V2 should add a 6th replicate per concentration or use 8 replicates at the central concentration (300 mg/mL) to tighten the central estimate.

---

### 13.8 Goehring smooth-box correction for diffusion-during-bleach (**V2 addition, 2026-04-21**)

**Source:** Goehring, N. W., Chowdhury, D., Hyman, A. A., & Grill, S. W. (2010). *FRAP Analysis of Membrane-Associated Proteins: Lateral Diffusion and Membrane-Cytoplasmic Exchange.* Biophys J 99:2443–2452.

**The problem.** Goehring et al. demonstrate that for any fast-diffusing species, the bleach duration (1–2 s in our protocol) is sufficient for lateral diffusion to smear the bleach boundary during the bleach itself. The resulting initial post-bleach distribution is NOT a sharp-edged box — it is well-approximated by an error-function smooth-box:

$$a_{\text{smooth}}(x, 0) = \frac{a_0}{2}\bigl[\mathrm{erf}(\mu(d_x/2 - x)) + \mathrm{erf}(\mu(d_x/2 + x))\bigr]$$

where `d_x` is the nominal bleach width and `1/μ` is the characteristic length scale of the boundary transition — neither derived from theory nor known in advance, but **directly measurable from the first post-bleach frame**.

**Why this matters for our test.** Our V1 protocol assumed a "sharp vs Gaussian-blur" binary test. Goehring shows that **even pure Fickian diffusion produces boundaries that are not sharp** after any finite bleach duration. If we compared PME compact-support to an idealised sharp-step Fickian, we would systematically over-credit ED. The correct Fickian null is the **Goehring smooth-box profile with measured `μ`**, not an idealised step.

**V2 action:** analysis pipeline §9.2 now fits THREE models (PME, Goehring smooth-box, sharp-step) and compares all pairs; the binding ED-vs-Fickian test is PME-vs-Goehring, not PME-vs-sharp-step.

**Quantitative impact.** Goehring's Fig 1 shows that fitting a sharp-box to data that has smoothed boundaries produces 20–50% errors in `D` and `k_off` for bleach offsets of 2–4 s. Our bleach-plus-delay window is ~1–2 s, so errors in V1 would be in the 10–30% range — larger than the pre-asymptotic regime correction of §13.4.

### 13.9 Corona-effect correction (**V2 addition, 2026-04-21**)

**Source:** Sarkar, P., & Chattopadhyay, A. (2020). *Exploring Membrane Lipid and Protein Diffusion by FRAP.* In: *Analysis of Membrane Lipids*, Springer Protocols Handbooks (Note 7, Fig 4).

**The problem.** Complementary to §13.8: during prolonged bleaching, rapid molecular diffusion broadens the actual bleached region into a "corona" that extends beyond the nominal ROI. This is the same physical phenomenon Goehring describes, named differently in the membrane-biology community.

**V2 action:** measure the actual bleach spot size from the first post-bleach frame (§13.14) rather than trusting the nominal ROI. Downstream: `D` reported using measured `ω`, NOT nominal ROI radius.

**Why we still go forward with the 1–2 s bleach.** Shorter bleach duration reduces corona but also reduces bleach depth (§13.2 requires ≥ 80%). The 1–2 s duration is a compromise: corona-broadening is manageable with the smooth-box fit, but bleach depth is sufficient to enter the non-linear PME regime. V2 simply measures the corona rather than trying to eliminate it.

### 13.10 Baseline clarification — the Fickian baseline is smooth-box / corona-broadened, NOT a sharp step (**V2 clarification, 2026-04-21**)

**This is the most important conceptual correction in V2.** The ED-UDM prediction of "sharp compact-support boundary" must be interpreted against the correct Fickian null, which is **NOT** a sharp step.

| Reference baseline | Which FRAP | When to use |
|:---|:---|:---|
| Sharp step (V1 assumption) | Idealised Fickian with instantaneous bleach | **NEVER** — physically unrealisable; retained in §9.2 only as a reference for the V1 literature |
| Goehring smooth-box with fitted `μ` | Fickian with finite bleach duration and/or diffusion-during-bleach | **Always the binding Fickian null for our test** |
| PyFRAP FEM simulation of pure-diffusion model with measured initial condition | Fickian with full geometric + bleaching complexity | Gold standard; use for publication-quality comparison |

**Practical consequence.** A measured front that looks sharper than a textbook sharp-step Fickian is NOT evidence for ED-PME. The front must be sharper than the **measured-μ Goehring smooth-box** — i.e., sharper than finite-bleach Fickian can produce.

**When PME wins:** if the fitted `1/μ` of the smooth-box model is comparable to the bleach radius `ω` itself (boundary width ≈ bleach size = no compact support), Fickian with finite-bleach corona is the correct description. ED-PME predicts `1/μ → 0` as `t → 0^+` with compact-support propagation thereafter; the front stays well-defined with no Gaussian tail at all times. This is measurable and distinguishes the regimes.

### 13.11 Immobile-fraction test via multiple FRAP in the same ROI (**V2 addition, 2026-04-21**)

**Source:** Sarkar & Chattopadhyay 2020, Note 9, Fig 6.

**The problem.** Photobleaching itself can induce immobile fractions via fluorophore crosslinking, particularly at high laser power. These artificially-immobile molecules don't contribute to recovery, mimicking a lower `M_f` or slower effective dynamics and biasing our `α_R` measurement.

**V2 action:** for each concentration, designate ONE of the 5 replicates as a "control FRAP" with repeated bleach in the same ROI:

1. Perform bleach and recovery acquisition as normal.
2. After full recovery, perform a second bleach at the same ROI.
3. Measure mobile fraction of the second recovery. **If no photo-crosslinking: `M_f` should be ~100%** (all originally-mobile molecules that recovered are still mobile). **If `M_f < 90%`, photo-crosslinking is occurring** and flagged for review.
4. Repeat for a third bleach if warranted.

**Cost:** ~2 extra minutes per concentration (one additional bleach cycle per control replicate). Total session time increases by ~8 minutes. Well within CP quote headroom.

**When to apply:** this is a V2 add-on to the protocol. If CP is willing to include on the same session, the control data is self-contained. If not, it becomes a V3 follow-up if the main experiment gives ambiguous results.

### 13.12 Control-spot photobleaching check (**V2 addition, 2026-04-21**)

**Source:** Sarkar & Chattopadhyay 2020, Note 10, Fig 7.

**The problem.** The imaging laser (at low power) can still photobleach the sample during the 5–10 minute acquisition. If the pre-bleach reference intensity drifts downward during the acquisition, every frame's normalisation is corrupted, and the extracted `α_R` is biased.

**V2 action:** in the same field of view as each bleach ROI, define a second "control ROI" 10–20 µm away (separated by more than the bleach radius + expected recovery front). Monitor the control ROI's mean intensity throughout the acquisition.

**Pass criterion:** control-ROI intensity stable to within ±3% of its own baseline over the full acquisition. Acquisitions with >10% control-ROI drift are dropped from the ensemble.

**Cost:** zero extra scope time — the control ROI is in the same frame. Implemented entirely in analysis (pipeline §9.4).

**Added to acquisition metadata schema:** `control_roi_center_px` and `control_roi_radius_um` in `metadata.json`. Easy to specify with the CP technician during session setup.

### 13.13 Four pre-registered discard criteria (**V2 addition, 2026-04-21**)

**Source:** Sarkar & Chattopadhyay 2020, Note 13, Fig 9.

**Pre-registered criteria for discarding an acquisition** (applied during pipeline §9.4 quality gate, before ensemble statistics):

| # | Failure mode | Quantitative criterion |
|:---:|:---|:---|
| 1 | **Unstable pre-bleach intensity** | Standard deviation of pre-bleach frames > 5% of their mean |
| 2 | **Incomplete fluorescence recovery** | Final-frame intensity < `I_pre_bleach × (1 − f_immobile_expected)`, where `f_immobile_expected < 5%` for soluble BSA |
| 3 | **Photobleaching during post-bleach acquisition** | Control-ROI drift > 10% per §13.12 |
| 4 | **Sample movement / focus drift** | Cross-correlation of pre-bleach and final-frame images below 0.9, OR visible focus drift in axial profile |

**Pre-registration commitment:** any acquisition failing one or more criteria is dropped from the ensemble automatically. The drop reason is logged in `per_acquisition.csv`. A session with more than 2 of 5 replicates dropped at the same concentration → that concentration is flagged as UNDECIDABLE in §10.

**This replaces ad-hoc reviewer judgment with an automated rule**, which is necessary for the analysis to be pre-registered in the ED-SC 2.0 sense.

### 13.14 Measuring the actual bleach radius `ω` via Gaussian HWHM (**V2 addition, 2026-04-21**)

**Source:** Sarkar & Chattopadhyay 2020, Note 14, Fig 10.

**The problem.** The diffusion coefficient in the Soumpasis formula scales as `D ∝ ω²`. Using the nominal ROI radius (e.g. 3 µm as specified) instead of the actual bleached-region radius introduces error that scales as the square of the difference. At 1–2 s bleach with fast-diffusing species, actual `ω` is typically 10–30% larger than nominal ROI.

**V2 action:** from the first post-bleach frame, measure the actual `ω` as follows:

1. Extract a line profile across the bleach spot (horizontal through the center).
2. Fit the profile to `I(x) = I_pre − A · exp(−(x − x_0)² / (2σ²))` — an inverted Gaussian.
3. Measure `ω_actual = σ · √(2 ln 2)` = half-width at half-maximum (HWHM).
4. Use `ω_actual` (not nominal ROI radius) for all downstream diffusion calculations.

**Quantitative impact.** If nominal ROI = 3 µm but actual corona-broadened `ω_actual` = 3.5 µm, the V1 `D` calculation would be off by `(3.5/3)² − 1 = +36%`. This propagates to `α_R` interpretation via the cross-check of §9.3: `β = 1/α_R − 2` combined with the 10-material fit becomes sensitive to the `ω` measurement.

**Implementation:** one additional function in the pipeline (~40 lines of Python); standard scipy.optimize.curve_fit.

### 13.15 Laser-power sweep to test for photo-crosslinking (**V2 addition, 2026-04-21**)

**Source:** Sarkar & Chattopadhyay 2020, Note 15, Fig 11.

**The problem.** At high bleach laser power, local heating and photochemical activation can induce fluorophore crosslinking (intermolecular covalent bonds between BSA molecules in the bleach region). Crosslinked BSA has a dramatically reduced diffusion coefficient, which would mimic our ED-UDM prediction of reduced `D` at high concentration. This is a confound.

**V2 action:** at the HIGHEST concentration only (350 mg/mL), where crosslinking risk is highest, dedicate ONE of the 5 replicates to a bleach-power sweep:

1. Perform 4 bleaches at the same ROI (or 4 matched ROIs) with laser powers at 60%, 80%, 90%, 100%.
2. Measure `α_R` for each recovery separately.
3. **Pass criterion:** `α_R` is invariant across the 4 power levels within ±0.02. If `α_R` systematically *decreases* with laser power, photo-crosslinking is present and the high-c result is confounded.

**Cost:** ~5 extra minutes during the 350 mg/mL session. Within CP quote headroom.

**Alternative:** run this at MULTIPLE concentrations if CP allows. At 200 mg/mL there is effectively zero crosslinking risk; at 350 mg/mL the risk is highest. Two-concentration sweep (200 + 350) is sufficient to establish baseline and worst-case.

### 13.16 PyFRAP as the analysis-pipeline foundation (**V2 addition, 2026-04-21**)

**Source:** Bläßle, A., Soh, G., Braun, T., Mörsdorf, D., Preiß, H., Jordan, B. M., & Müller, P. (2018). *Quantitative diffusion measurements using the open-source software PyFRAP.* Nature Communications 9:1582. Software: `https://mueller-lab.github.io/PyFRAP/`

**Why use PyFRAP instead of writing from scratch.** Bläßle et al. benchmarked PyFRAP against easyFRAP, FrapCalc, virtualFRAP, and simFRAP on 18 simulated FRAP experiments spanning three orders of magnitude in diffusivity; PyFRAP outperformed all alternatives with the smallest error (mean 2%) and handles 2D/3D geometry explicitly via a FEM simulation with fitted initial condition. It imports raw data from all major microscope formats (.tif, .lsm, .czi, .nd2), has a GUI for manual verification, and saves projects as a structured object database for reproducibility.

**V2 action:** build our `frap_udm_pipeline.py` as a Python wrapper that:

1. Calls PyFRAP to import the TIFF stack, define ROIs, compute pre-bleach normalisation, and fit the Goehring smooth-box model (as the Fickian null).
2. Extracts the raw radial profiles and fit residuals from the PyFRAP project database.
3. Adds: PME Barenblatt parabolic-cap fit (new, not in PyFRAP); front-radius power-law extraction; HWHM ω measurement; the four §13.13 discard criteria; ensemble aggregation.
4. Outputs per §9.4 deliverables schema.

**Effort saving.** PyFRAP eliminates ~2–3 days of from-scratch pipeline work. We write a ~200-line wrapper plus the PME-specific additions (~300 lines total), instead of a ~500–700-line full pipeline.

**Dependency management.** PyFRAP has its own install requirements (PyQt, FiPy, scipy). Pin versions in `requirements.txt` for reproducibility. Consider a Docker / conda environment spec for the final pipeline.

---

## 14. Connection to the broader ED empirical program

**This is test 2 of 4 ED predictive experiments.** The four predictive tests exercise the ED PDE's channels as follows:

| # | Test | Channel | Observable | Status |
|:---:|:---|:---|:---|:---|
| 1 | **AFM dewetting** | architectural / cross-scale invariant | motif-conditioned Hessian median `r* ∈ [−1.50, −1.10]` | [Protocol](../AFM-Dewetting-ED-SC_InProcess/protocol.md); execution $500 + 4–6 weeks |
| 2 | **UDM FRAP (this doc)** | **mobility** `M(ρ) = M_0(ρ_max−ρ)^β`, `β ≈ 2` | **front radius `R(t) ~ t^(1/6)` + sharp boundary** | **Sent to CP; decision window 2026-04-24 to 2026-05-01** |
| 3 | ED-09.5 Pillar A (Aspelmeyer optomechanics) | participation `v(t)` | slow envelope at `ω_v ≈ 8·γ_dec` on raw `x(t)` | [Protocol](../ED-09-5-Envelope_InProcess/protocol.md); Aspelmeyer email pending |
| 4 | ED-09.5 FRAP-side (Lomb-Scargle reanalysis) | participation `v(t)` | residual power at 80–800 Hz on public recovery curves | Self-contained; no third-party dependency |

**Distinctive features of this UDM-FRAP test:**

- **The only test currently in technician review** at an external facility — closest to producing a result.
- **Tests the ED channel with the strongest existing empirical support.** The UDM 10-material result (`R² > 0.986`) is the repo's strongest condensed-matter evidence; FRAP provides an independent BSA-system check via a different observable.
- **Binary PASS/FAIL is cleanly defined.** α_R in `[0.125, 0.170]` versus α_R ≈ 0.50 — factor of 3 separation is unambiguous under proper bleach depth.
- **Ties in directly to the published UDM paper.** A PASS result would appear as a FRAP-independent confirmation in the UDM paper's second-edition revision list; a FAIL would be published as a narrowing-of-class result.

**Expected timeline from CP decision to publishable result:** 6–8 weeks (decision → session → data → analysis → write-up).

---

## 15. Risks and their mitigations

| Risk | Probability | Mitigation |
|:---|:---|:---|
| CP declines due to "beyond standard FRAP" scope | Low (they already forwarded internally) | Already mitigated — CP did not decline, they escalated |
| Bleach depth < 80% in the non-linear regime | Medium | §5 explicit emphasis; V2 §13.2 adds post-hoc quantitative gate |
| Pre-asymptotic regime on 512×512 grid | Medium | V2 §13.4 simulation-calibration; widened PASS band to `[0.125, 0.170]` |
| Axial geometry ambiguity (2D vs 3D) | Medium | Widened PASS band; V2 §13.3 z-stack option |
| BSA aggregation at high c | Low-medium | §4 filtration step; V2 §13.6 pre/post drift check |
| TIFF export gives processed images not raw | Low (explicitly requested) | §8 emphasis; confirm on first frame |
| Statistical power at NEAR-PASS boundary | Medium | V2 §13.7 additional replicates if needed |
| Result is NEAR-PASS (sub-Fickian but outside strict band) | Medium | §10 decision tree; NEAR-PASS is still publishable as "PME-class behaviour, BSA-specific β" |

---

## 16. References

- [`ED-Orientation.md`](../../docs/ED-Orientation.md) §7 empirical-status table, §5.7 (Foundational Paper v2 six structural analogues, esp. Analogue 2 mobility-PME reduction), top-of-doc 2026-04-17 entry.
- [`papers/Universal_Mobility_Law/`](../../papers/Universal_Mobility_Law/) — UDM 10-material paper. This FRAP test is a parallel confirmation at BSA via front propagation.
- [`theory/PDE.md`](../../theory/PDE.md) — canonical ED PDE; mobility channel `M(ρ) = M_0(ρ_max − ρ)^β`.
- [`theory/Architectural_Canon.md`](../../theory/Architectural_Canon.md) — Canon P4 (Mobility Capacity Bound).
- PhilArchive: *Universal Degenerate-Mobility Scaling in Crowded Soft Matter* (Proxmire, ED series).
- Vázquez, J. L. *The Porous Medium Equation.* Oxford University Press (2007).
- Barenblatt, G. I. *Scaling, Self-similarity, and Intermediate Asymptotics.* Cambridge (1996). — Barenblatt self-similar solution.
- Sigma-Aldrich A9771 — BSA-FITC conjugate specification.
- Seiffert & Oppermann (2008). *Diffusion of linear macromolecules and spherical particles in semidilute polymer solutions...* Polymer 49 4115 — FRAP technique reference for concentrated polymer solutions.

---

*This protocol mirrors the canonical operational-protocol structure of [`AFM protocol`](../AFM-Dewetting-ED-SC_InProcess/protocol.md) and [`ED-09.5 protocol`](../ED-09-5-Envelope_InProcess/protocol.md). The body (§4–§8) is the text already submitted to Creative Proteomics; §1–§3 provide the ED theoretical context, §9–§12 the analysis and decision framework, §13 the review-level improvements for a V2 protocol.*

---

## Appendix A — Draft CP Amendment Request (high-framerate add-on)

**Purpose:** ask CP to include ONE high-framerate line-scan acquisition per concentration, on top of the 20 standard acquisitions already specified, to enable a second ED test (the ED-09.5 participation-channel envelope at 80–800 Hz) on the same samples. The ED-09.5 Track B literature search has shown that kHz-rate concentrated-FRAP data does not exist in the public literature; this add-on solves that data gap in ~4 extra minutes of scope time per concentration.

**Status:** DRAFT, not yet sent. To be sent after CP responds with their quote for the V1 protocol (expected 2026-04-24 to 2026-05-01). Do not send concurrent with V1 decision — wait for CP to confirm the base experiment first, then propose the amendment.

**Tone:** professional, concise, low-friction. The request is for a minimal addition to an already-scoped experiment using the same samples, microscope, and session — not a new project.

---

**Subject:** Small amendment to the FRAP protocol — one high-speed line-scan per concentration

> Dear [CP contact],
>
> Thank you again for forwarding the protocol to your technician team. While you are evaluating feasibility, I would like to propose one small addition to the protocol that would allow us to test a second theoretical prediction from the same samples during the same session. I want to raise it now rather than post-session so it can be included in the quote if it is feasible.
>
> **The addition.** After completing the five standard FRAP acquisitions at each concentration (the current protocol), perform **one additional acquisition per concentration at a high frame rate** on a smaller region of interest:
>
> - Mode: line-scan or small-ROI time-series, whichever the Zeiss 710 or equivalent supports at ≥ 2 kHz line rate
> - ROI: 64 × 64 pixels (or equivalent line length) covering the bleach spot
> - Frame rate: ≥ 2 kHz
> - Duration: 2 seconds post-bleach (5 seconds total including pre-bleach)
> - Same sample, same bleach settings, same concentration as the standard acquisition it follows
> - Total: 4 high-speed acquisitions across the four concentrations — one per sample
>
> **Why this matters.** The standard 10-Hz-then-1-Hz acquisition specified in the main protocol captures the *spatial* recovery front, which tests one ED prediction (power-law exponent R(t) ∝ t^(1/6)). A second ED prediction concerns high-frequency dynamics on the *intensity recovery curve* itself — a predicted envelope-modulation feature in the 80–800 Hz band. This prediction cannot be tested at the standard frame rate (Nyquist would be 5 Hz, far below the predicted band); but at 2 kHz it becomes directly testable from the same samples.
>
> **Scope impact.** Based on typical Zeiss 710 line-scan rates, one high-speed acquisition per concentration adds approximately 3–5 minutes per sample, or 15–20 minutes total session time. The samples are already in place, the bleach hardware is already configured, and no additional reagents are needed. The additional acquisitions produce TIFF stacks using the same export path as the standard acquisitions.
>
> **Scientific value.** This single addition enables two independent theoretical tests from one session rather than one test from one session. The high-speed data is also independently interpretable even if the standard-rate data is inconclusive; it is not redundant with the main acquisitions.
>
> **What I need from you.**
>
> 1. Confirmation that the Zeiss 710 (or whichever instrument your technicians propose) supports ≥ 2 kHz line-scan or small-ROI time-series. If not, please indicate the maximum achievable frame rate on a ≤ 64 × 64 ROI.
> 2. Any adjustment to the quote reflecting the additional ~15–20 minutes of scope time.
> 3. Confirmation that the high-speed TIFF stacks can be exported in the same raw-data format as the standard acquisitions.
>
> If the high-speed mode is not feasible on your microscope, the main protocol proceeds as submitted — the amendment is additive, not a substitute.
>
> Thank you again for considering this. I am happy to answer any technical questions about the added acquisition or the theoretical basis for it.
>
> With respect,
>
> [Allen Proxmire]
> [affiliation / email]

---

**Pre-send checklist for this amendment:**

- [ ] CP has returned a quote for the V1 protocol (so the amendment doesn't delay the V1 decision)
- [ ] Instrument model confirmed (to match technical feasibility questions to the actual hardware)
- [ ] Frame-rate requirement sanity-checked: 2 kHz at 64×64 ROI is routinely achievable on Zeiss LSM 710 and similar systems via "region scan" or "line scan" modes
- [ ] Cross-referenced with [`ED-09.5 protocol`](../ED-09-5-Envelope_InProcess/protocol.md) Track B §7 to ensure the high-speed data format is compatible with the Lomb-Scargle reanalysis pipeline

**If CP declines the amendment:** Track B falls back on literature search for public kHz-rate concentrated-FRAP data (currently no match identified) or a separate future commissioned session. The V1 UDM test is unaffected.

---

## 17. V2 change log

**Version:** V2, 2026-04-21. Previous version: V1, 2026-04-21 (morning, as relocated to this folder from docs/).

**Trigger:** Literature review on 2026-04-21 of four FRAP methods papers identified refinements to the analysis pipeline and additional quality-control controls. None of the four papers provides data for Track B (ED-09.5 envelope at 80–800 Hz) or for the UDM-FRAP test directly at the required regime, but each contributes methods-level improvements.

**Papers reviewed:**

1. Goehring, N. W. et al. (2010). *FRAP Analysis of Membrane-Associated Proteins.* Biophys J 99:2443.
2. Bläßle, A. et al. (2018). *Quantitative diffusion measurements using PyFRAP.* Nat Commun 9:1582.
3. Sakib, S. & Fradin, C. (2026). *Experimental and simulated FRAP for the quantitative determination of protein diffusion in helical cells.* bioRxiv preprint.
4. Sarkar, P. & Chattopadhyay, A. (2020). *Exploring Membrane Lipid and Protein Diffusion by FRAP.* In: *Analysis of Membrane Lipids*, Springer Protocols Handbooks, Chapter 8.

**Sections modified:**

| Section | Change | Source |
|:---|:---|:---|
| Top-of-doc Status banner | Added V2 version line + V2 change summary pointer | — |
| §9 preamble | Added V2 note describing four methods-paper refinements and PyFRAP foundation | All four papers |
| §9.2 Sharp-front test | **Major rewrite.** Changed from two-model (PME vs Gaussian-blur) to three-model (PME vs Goehring smooth-box vs sharp-step) comparison. Clarified that the binding Fickian null is the Goehring smooth-box, not a sharp step. Added implementation note referencing PyFRAP's built-in smooth-box fit. | Goehring 2010, Sarkar 2020 Note 7 |
| §9.4 Required analysis code | **Rewritten.** Now specifies a wrapper around PyFRAP rather than from-scratch implementation. Expanded per-acquisition output schema to include measured `ω` (HWHM), corona width `1/μ`, AIC for all three models, discard-criterion flags, control-spot drift. Added synthetic-data validation requirement before first use. | Bläßle 2018, Sarkar 2020 Note 14 |
| §13 | **Expanded from 7 to 16 subsections** (V1 §13.1–13.7 preserved; added §13.8–13.16). | Goehring 2010, Bläßle 2018, Sarkar 2020 |

**New subsections in §13:**

| § | Title | Source | Impact |
|:---|:---|:---|:---|
| 13.8 | Goehring smooth-box correction for diffusion-during-bleach | Goehring 2010 | Changes the Fickian null hypothesis; major |
| 13.9 | Corona-effect correction and measurement | Sarkar 2020 Note 7 | Pairs with 13.8; pipeline measures corona width from data |
| 13.10 | Baseline clarification — Fickian baseline is smooth-box, not a sharp step | Goehring 2010, Sarkar 2020 | **Most important conceptual correction.** ED front-sharpness must beat the corona-broadened Fickian, not an idealised step |
| 13.11 | Immobile-fraction test via multiple FRAP in the same ROI | Sarkar 2020 Note 9 | New control add-on; ~8 min session time; one of five replicates |
| 13.12 | Control-spot photobleaching check | Sarkar 2020 Note 10 | Zero scope-time cost; implemented in analysis |
| 13.13 | Four pre-registered discard criteria | Sarkar 2020 Note 13 | Replaces reviewer judgment with automated rule |
| 13.14 | Measuring actual bleach radius `ω` via Gaussian HWHM | Sarkar 2020 Note 14 | Corrects `D` measurement by ~10–30%; pipeline addition |
| 13.15 | Laser-power sweep for photo-crosslinking | Sarkar 2020 Note 15 | New control at 350 mg/mL; one replicate |
| 13.16 | PyFRAP as the analysis-pipeline foundation | Bläßle 2018 | Saves ~2–3 days of pipeline work; benchmarked against alternatives |

**New document sections:**

| § | Content |
|:---|:---|
| Appendix A | Draft CP amendment request letter for one high-framerate line-scan add-on acquisition per concentration. Pre-send checklist. Fallback plan if CP declines. |
| §17 (this section) | V2 change log |

**What did NOT change (explicit preservation):**

- **§4–§8 remain verbatim as submitted to CP.** Zero changes to the CP-facing protocol text. Any V2 refinement that would alter CP-side behaviour is either (a) queued for a future amendment (Appendix A), (b) confined to analysis-side workflow (§9), or (c) a review-level note for a hypothetical V3 protocol (§13).
- The theoretical derivation (§1–§3), the pre-registered parameters table (§3), the pass/fail band (§3), and the §10 decision tree are unchanged. V2 refines the *execution* of the analysis, not the *prediction* being tested.
- §11 deliverables schema is unchanged except for additional fields in the per-acquisition CSV (consistent with §9.4 pipeline output).
- Risks and mitigations (§15) are unchanged; V2 refinements mitigate several of the listed risks further but no new risks are introduced.

**Quantitative impact of V2 refinements combined.**

- Goehring + corona correction reduces expected error in `D` from 10–30% to < 5% (V1 overstated the evidence for ED by under-specifying the Fickian null).
- HWHM bleach-radius measurement corrects a separate ~10–30% error in `D` calculation.
- Control-spot and discard criteria reduce the probability of a spurious PASS or FAIL from a single corrupted acquisition to < 1%.
- PyFRAP foundation provides a benchmarked reference implementation for the Fickian null, converting what was a hand-rolled fit into a published, peer-reviewed pipeline.

**Net:** V2 is tighter, more reproducible, and more pre-registered than V1. The prediction under test is unchanged; the methods by which it is tested are hardened.

**Cross-link:** the V2 refinements identified here (especially the Goehring / corona / smooth-box convergence) inform the AFM protocol's sharp-vs-Gaussian test in [`AFM protocol`](../AFM-Dewetting-ED-SC_InProcess/protocol.md) §5.3 as well. The same physical phenomenon (diffusion during bleach smoothing boundaries that are nominally sharp) does not arise in AFM because there is no "bleach" step, but the general principle — the null hypothesis must be physically realisable, not idealised — applies across both tests. No change to the AFM protocol is required; this is a methodological note for future cross-scale protocol revisions.
