# ED-SC 2.0 Cross-Scale Test #1 — AFM Protocol for Thin-Film Polymer Dewetting

**Status.** Operational protocol for Route 3 of the AFM empirical track (ED's highest-certainty near-term test). This document translates the strategic framing in [`ED-Orientation.md`](../../docs/ED-Orientation.md) 2026-04-20 update entry and [`ED-SC-2.0.md`](../../docs/ED-SC-2.0.md) §3–§5 into a session-ready procedure that an operator can execute at any academic AFM core facility.

**Relationship to prior work.**
- **Concept / prediction:** [`ED-SC-2.0.md`](../../docs/ED-SC-2.0.md) §2 — the motif-conditioned median `r* ≈ −1.30 ∈ [−1.50, −1.10]` claim.
- **Pilot (undecidable outcome):** [`analysis/scripts/ed_arch_r2/ThinFilm_Pilot_Memo.md`](../../analysis/scripts/ed_arch_r2/ThinFilm_Pilot_Memo.md) — N=1, pseudo-height from image brightness, `L_coh ≈ 40 px` too small for the canonical filter → 0 motif-admitted saddles. This protocol fixes the root cause: **proper AFM gives physical scale, multiple frames, and `L_coh`-resolved sampling** (`Δx ≤ L_coh/8`).
- **Three-route strategy (from orientation doc):** Route 1 (check 2023 *Nat Comm Phys* paper for accessible data — 5 min), Route 2 (email Jacobs group), **Route 3 (this protocol)** — the guaranteed-success path because it does not depend on any third party.
- **Strategy-level entry point:** the 2026-04-20 entry at the top of `ED-Orientation.md` and the AFM row in §7 empirical-status table.

**What this document does not change.**
- The canonical ED-SC 2.0 motif-filter parameters are **pre-registered** and **not tunable**: `α = 0.25, L_ray = 2, δ = 0.10`. See [`ED-SC-2.0.md`](../../docs/ED-SC-2.0.md) §1.4 and §4.
- The band `[−1.50, −1.10]` around `r* = −1.30` is the only adjustable-by-none falsification window. See [`ED-SC-2.0.md`](../../docs/ED-SC-2.0.md) §4.
- Any deviation from these parameters is a **revision of ED-SC 2.0**, not an execution of it. Route 3 runs the canonical test.

---

## 1. The prediction in one paragraph

Spin-coated polystyrene on silicon, annealed above `T_g` into the **spinodal pre-rupture regime**, forms a thickness field `h(x, y)` whose Morse saddles have Hessian-eigenvalue ratios `r(x*) = λ_large / λ_small`. ED-SC 2.0 predicts that the **motif-conditioned** subset of those ratios — saddles whose compression-axis neighbourhoods drop below `h̄ − 0.25·σ_h` and whose expansion-axis neighbourhoods rise above `h̄ + 0.25·σ_h` within two lattice steps — has median `r* ∈ [−1.50, −1.10]`. The reference value is `−1.304`, measured on the canonical Scenario-D lattice at `(n*, σ*) = (2.7, 0.0556)`. The thin-film `h(x, y)` and the Scenario-D `p(x, y)` are architecturally equivalent systems separated by ~20 orders of magnitude in physical scale; both should give the same median. A measured median outside the band on a properly-sampled dataset falsifies the cross-scale invariance claim at the filamentary-dewetting scale.

## 2. Pre-registered test parameters

These are copied from [`ED-SC-2.0.md`](../../docs/ED-SC-2.0.md) §1.4 and §2 **without modification**. Operators must use these exact values.

| Parameter | Value | Role |
|:---|:---|:---|
| Non-degeneracy threshold `δ` | `0.10` | Reject saddles where `|λ_min|/|λ_max| < δ` |
| Motif-filter amplitude `α` | `0.25` | Threshold in units of `σ_h`: `E_hi = h̄ + α·σ_h`, `E_lo = h̄ − α·σ_h` |
| Motif-filter ray length `L_ray` | `2` lattice steps | Along each principal-axis direction at the saddle |
| Sampling condition | `Δx ≤ L_coh/8` | Where `L_coh = 1/⟨‖∇h‖⟩` (see §5.3) |
| Minimum admitted saddles per frame | ≥ 10 | Below this, the frame is under-resolved |
| Expected median | `r* ≈ −1.30` | Band: `r* ∈ [−1.50, −1.10]` |
| Invariance tolerance | `ε_med = 0.20` | Sum of per-system biases |

**Reference measurement.** Scenario D at `(n* = 2.7, σ* = 0.0556)` on a 64×64 periodic lattice with `α = 0.03, γ = 0.5, dt = 0.05, seed = 77`, mobility-weighted update, uniform IC `[0.3, 0.7]`, 500 steps: **`med(ℛ_motif) = −1.304`**. Reproduction: `analysis/scripts/ed_arch_r2/r2_canonical.py` + `r2_motif_filter.py`.

---

## 3. Stage 1 — Sample preparation (off-site; before the AFM session)

**Location.** Most AFM core facilities do not do polymer film prep. Easiest path: a soft-matter or polymer group at your institution (or any collaborator with a spin-coater and a hotplate). Prep takes ~30 min per sample; budget a half-day for 4–8 samples across different anneal conditions.

### 3.1 Materials

| Item | Specification |
|:---|:---|
| Substrate | Polished Si wafer (Si or thermally-oxidised Si/SiOₓ), ~1 cm². Clean with piranha or RCA-1, or use as-received and rinse with isopropanol. |
| Polymer | Polystyrene (PS). Molecular weight **2–100 kg/mol** (see §3.3 for MW selection). Sigma-Aldrich or Polymer Source standard. |
| Solvent | Toluene, HPLC grade. |
| Solution | PS dissolved in toluene at **0.5–2 wt%**. Prepare fresh; filter through 0.2 µm PTFE if particulates are visible. |

### 3.2 Spin-coat

| Parameter | Value |
|:---|:---|
| Dispense | ~0.1 mL of PS-toluene solution on the static wafer |
| Spin speed | **2000–4000 rpm** |
| Spin time | 30 s |
| Expected film thickness | **5–30 nm** (depends on concentration and spin rate) |

Target a film thickness comparable to the polymer's `L_coh / 10` at the anneal temperature, so that the spinodal wavelength (which goes as `h^2` for a van-der-Waals-dominated system) falls in the AFM sweet spot of 1–10 µm. For MW = 10 kg/mol PS at 1 wt% and 3000 rpm, expect `h ≈ 15 nm` and `L_spinodal ≈ 2 µm`.

### 3.3 Annealing — the critical step

Heat the spin-coated wafer above PS glass transition (`T_g ≈ 100 °C`). **Let the hotplate temperature stabilise for ≥ 60 s before starting the anneal timer** — PS is a glassy former and a short transient below `T_g` will suppress spinodal development.

**Anneal temperature.** `T_anneal = 130 °C` is standard. Higher `T_anneal` (up to ~160 °C) accelerates growth by lowering viscosity; lower `T_anneal` (e.g., 110 °C) slows it. Stay well below 180 °C to avoid PS degradation.

**Anneal time — MW-dependent, not universal.** Copilot's recipe suggested "5, 10, 20, 30 min" as a universal time sweep. This is correct for **MW ≈ 10 kg/mol PS at 130 °C** and starting-point film thicknesses of ~15 nm. For other conditions the window shifts:

| MW (kg/mol) | `T_anneal` | Approximate pre-rupture window |
|:---|:---|:---|
| 2 | 130 °C | 30 s – 5 min |
| 10 | 130 °C | 5 – 30 min |
| 50 | 130 °C | 30 – 120 min |
| 100 | 130 °C | 1 – 8 hours |

The viscosity of PS scales approximately as `η ∝ MW^{3.4}` above the entanglement MW (~18 kg/mol), and the spinodal dewetting timescale is `τ ∝ η · h^5 / (γ · L_coh²)`. **Always prep 4–6 samples at logarithmically-spaced anneal times** spanning at least two decades around the expected window. Optical inspection (§3.4) picks the usable ones.

### 3.4 Pre-rupture regime verification — quantitative, not just visual

The **critical constraint** is that the film has developed thickness modulations but **holes have not yet formed and coalesced**. Copilot's recipe describes this visually; the following objective test is more reliable:

**Optical microscope check (required for every sample).**

1. Image the sample under a bright-field microscope at 10× and 50× before the AFM session.
2. Compute the image histogram of grayscale intensity `I(x, y)`.
3. **Pass (pre-rupture):** the histogram is unimodal or weakly skewed; no distinct dark-pixel population below `⟨I⟩ − 2·σ_I`; the surface shows **texture / waviness** at the ~µm scale but no isolated round dark spots.
4. **Fail (post-rupture):** a distinct secondary peak appears in the histogram at low intensity, corresponding to the dry patches exposed by hole formation. Visually: **holes with bright rims** are clearly separable from the unruptured film.
5. **Fail (pre-spinodal):** histogram is narrowly unimodal with no visible waviness at any magnification. The film is either too thin, too young, or below `T_g` during anneal.

**Save an optical image per sample.** This provides a paper trail that the sample was in the right regime before AFM. Name the image `<sample_id>_optical_<anneal_min>min.png`.

### 3.5 Sample labelling and record

Each sample gets a label: `YYYYMMDD-<MW>-<wt%>-<rpm>-<Tanneal>C-<anneal_min>min-<substrate>-<repN>`.

Example: `20260501-10kg-1pct-3000rpm-130C-15min-Si-rep2`.

Keep a bench notebook (paper or markdown) with one line per sample: label, optical-check outcome (pass / fail / ambiguous), notes on any deviations from the recipe. This feeds directly into the post-session metadata file (§6.2).

### 3.6 If you can't prep on-site

PS-on-Si is one of the most-studied model systems in soft matter. Any polymer or soft-matter group will either (a) know the recipe cold, (b) have samples sitting in a drawer, or (c) know who does. Possible contacts:
- A thin-films lab at your institution's physics / materials-science department.
- A MEMS / microfluidics group (they spin-coat PS for lithography).
- A wetting / interfaces group (Jacobs group at Saarland is the canonical reference; other groups exist at most research universities).
- A polymer-chemistry lab (Sigma-Aldrich representatives can point you to their academic customers).

---

## 4. Stage 2 — AFM scan parameters

### 4.1 Booking the session

When you book the facility, explicitly request the following. Walking in without pre-specified parameters is a common failure mode — the operator's defaults may be set for a different kind of sample.

### 4.2 Instrument configuration

| Parameter | Value | Rationale |
|:---|:---|:---|
| **Mode** | Tapping mode (intermittent contact) | Non-destructive; required for soft polymer films |
| **Tip** | Silicon, `k ≈ 26 N/m`, `f_0 ≈ 300 kHz` (e.g., Olympus OMCL-AC160TS, or NanoAndMore PPP-NCHR equivalent) | Most academic cores stock these |
| **Scan size** | `10 × 10 µm` to `20 × 20 µm` | Big enough for ≥ 5 `L_spinodal` wavelengths; small enough for fine pixel resolution |
| **Pixel resolution** | **512 × 512 minimum** (256² is marginal) | At 10 µm scan, gives `Δx ≈ 20 nm` per pixel |
| **Scan rate** | 0.5 – 1 Hz (lines/s) | Slow enough for stable polymer imaging; faster rates cause tip ring-down artefacts |
| **Integral gain** | Adjust to minimise tracking error; rule of thumb: as high as it goes before the image develops horizontal noise streaks | Standard AFM practice |

### 4.3 Sampling-condition check

With `Δx ≈ 20 nm` and `L_coh ≈ 2 µm`, the ratio `Δx / L_coh ≈ 0.01` — **a factor of 10 better than the ED-SC 2.0 requirement `Δx ≤ L_coh/8`**. A 256² scan at 20 µm gives `Δx ≈ 78 nm` which is still a factor of 3 inside the requirement. 512² is preferred for safety margin and saddle-count statistics.

**Per-sample sampling-condition verification (do this at the instrument).** The AFM software shows a live gradient histogram; `L_coh ≈ 1 / mean(|∇h|)`. If it reports `L_coh < 8·Δx` on a live scan, **the frame will not pass the pre-analysis check (§5.3)**. Stop, increase pixel resolution or decrease scan size, and re-scan.

### 4.4 Frames per sample — `N > 1` is essential

The pilot's single data point (N=1, pseudo-height from a movie frame) is flagged in the orientation doc as the main caveat of the pilot result. Route 3 fixes this.

**Minimum 5, target 10, frames per sample.** Independent areas — different locations on the same wafer separated by at least the scan size plus `~10 µm`. If you have multiple samples (which you should, from §3.3), aim for `N_samples × N_frames ≥ 30` total frames in the session. This gives ensemble statistics and per-sample reproducibility.

### 4.5 Session budget

A typical 1–2 day AFM session at an academic core covers:
- Day 1 morning: operator training / tip loading / thermal equilibration (~2 hr).
- Day 1 afternoon: scan 3–4 samples × 5–10 frames each (~4 hr at 5 min/frame).
- Day 2 (optional): additional samples, replication of interesting frames, or zoom-in scans on regions of interest.

If the facility charges by the hour, expect 6–12 hr of instrument time for a complete run with ~30 frames.

---

## 5. Stage 3 — Data export and post-session analysis

### 5.1 Export format — the common failure mode

This is where many AFM sessions produce unusable data. **Be explicit with the operator.**

**Required exports, per frame:**

1. **Raw height data `h(x, y)` as a 2D array.** Native vendor format is fine as a primary save (`.ibw` for Asylum, `.nid` for Nanosurf, `.spm` for Bruker, `.gwy` for Gwyddion), but **you must also export a universal format** that your analysis script can read without the vendor software installed.
2. **Universal export formats accepted by the analysis pipeline:** `.txt` (ASCII grid), `.csv`, or `.h5` (HDF5). **`.png` / `.jpg` screenshots are NOT sufficient** — they are processed images, not raw arrays, and the pilot's failure was partly caused by exactly this kind of degraded input.
3. **Metadata (separate file or HDF5 attributes):**
   - Scan size in µm (both axes)
   - Pixel resolution (both axes)
   - Vertical scale (nm per unit)
   - Whether plane-flatten was applied (and which order)
   - Tip model, drive amplitude, setpoint, feedback gains
   - Sample label (matches the bench-notebook entry from §3.5)
   - Scan timestamp

### 5.2 On-instrument processing — minimal, pre-declared

Apply the following and nothing else:

| Step | Action | Reason |
|:---|:---|:---|
| **Plane flatten** | **Single global 1st-order plane fit** subtracted from the full image. Do NOT use line-by-line 1st-order subtraction by default. | Line-by-line subtraction introduces artificial horizontal ridges and can bias saddle-point morphology along the scan axis. A single global plane is more conservative for Hessian statistics. If line-by-line is unavoidable due to persistent drift, declare it in the metadata and expect residual anisotropy in the Hessian. |
| **Zero-offset** | Subtract `min(h)` so all heights are ≥ 0 (optional, purely cosmetic) | Does not affect Hessian |
| **Median / Gaussian smoothing** | **DO NOT apply.** | Smoothing alters the high-frequency Hessian content that the motif filter depends on. |
| **Bandpass / notch filters** | **DO NOT apply** unless you have a specific artefact (e.g., 60 Hz line noise appearing as horizontal stripes); if applied, declare it in metadata and expect it to be a covariate on the result. |

### 5.3 Pre-analysis quality gates (run before the main analysis)

For every exported frame, compute the following and drop frames that fail any of:

| Gate | Criterion | Rationale |
|:---|:---|:---|
| **Coherence length** | `L_coh := 1/⟨‖∇h‖⟩ ≥ 8·Δx` | ED-SC 2.0 §3 sampling condition. If `L_coh/Δx < 8`, the frame is sub-Nyquist for the canonical filter and will under-admit saddles (the pilot's failure mode). |
| **Morse-saddle count** | `N_Morse ≥ 10` after `δ = 0.10` degeneracy filter | ED-SC 2.0 §3 minimum. Fewer than 10 saddles gives unreliable median statistics. |
| **Spinodal-peak quality check** | Radial power spectrum `S(q)` has a single clear peak at `q* ∈ [π/L_coh, 4π/L_coh]` | Confirms the sample is in the spinodal regime, not post-rupture or pre-spinodal. A broad or missing peak indicates the sample is not in the pre-registered regime and the test should not be run on it. |
| **Height distribution** | `h(x, y)` histogram is approximately Gaussian (excess kurtosis `|κ| < 1`) | Large kurtosis indicates hole formation (bimodal distribution) or tip artefact. Reject. |
| **Scan artefact check** | FFT shows no dominant horizontal or vertical stripe peaks beyond ±10% of the spinodal peak amplitude | Indicates tip tracking is unstable or line-by-line plane-fit artefacts remain. |

**Frames that fail any gate are dropped**, not tuned to pass. Log the drop reason in the metadata.

### 5.4 Main analysis — motif-conditioned median per frame

Script: [`analysis/scripts/ed_arch_r2/cross_scale_01_thinfilm_pilot.py`](../../analysis/scripts/ed_arch_r2/cross_scale_01_thinfilm_pilot.py) — the same script used for the N=1 pilot. It already implements:
- 2D polynomial detrend (degree 2) — optional; disable if the instrument-level plane fit is deemed sufficient
- Central-difference gradient sign-flips → Morse-saddle candidates
- 5-point Hessian stencil
- Morse + degeneracy filter (`det H < 0`, `|λ_min|/|λ_max| ≥ δ`)
- Canonical motif filter (`α = 0.25, L_ray = 2`)
- Output: `thinfilm_pilot_ratios_all.npy` (all Morse-saddle ratios) and `thinfilm_pilot_ratios_motif.npy` (motif-admitted subset)

**Per frame, compute and store:**

- `r_all[] = saddle ratios before motif filter` (full distribution)
- `r_motif[] = saddle ratios after motif filter` (the pre-registered distribution)
- `median(r_all)`, `IQR(r_all)`, `N_all`
- `median(r_motif)`, `IQR(r_motif)`, `N_motif`
- % in `[−1.50, −1.10]` for both
- `L_coh` for this frame (for later sanity-check on sampling condition)

**Expected pattern, if ED-SC 2.0 is correct:**

- `median(r_all)` ≈ −2.0 (matches Scenario D's raw saddle distribution; pilot reported −2.149 matching Scenario D's −2.063)
- **`median(r_motif)` ≈ −1.30 ± 0.10 per frame**, with `N_motif ≥ 10` per frame
- `% in band` for `r_motif` should be `≥ 50%`; for `r_all` only `~20%`

### 5.5 Ensemble statistics across frames

After running all frames through §5.4:

| Statistic | Definition | Pass criterion |
|:---|:---|:---|
| **Mean of per-frame medians** | `r̄ = mean_f median(r_motif[f])` | `r̄ ∈ [−1.50, −1.10]` |
| **Frame-to-frame std** | `s_f = std_f median(r_motif[f])` | No strict cutoff, but `s_f / √N_frames < 0.15` (uncertainty on `r̄` < half band width) |
| **Per-sample mean** | For each sample, mean of medians across its frames | ≥ 4/5 samples have per-sample mean in band (catches sample-specific biases) |
| **Total motif-admitted saddle count** | `N_motif_total = Σ_f N_motif[f]` | ≥ 200 across the full ensemble (gives reliable aggregate median) |
| **Aggregate median** | `median(r_motif[all frames])` (pool ratios across all frames) | `∈ [−1.50, −1.10]` AND within `0.10` of `r̄` |

### 5.6 Outcome decision tree

| Outcome | Interpretation |
|:---|:---|
| **PASS:** `r̄ ∈ [−1.50, −1.10]` AND per-sample criterion met AND `N_motif_total ≥ 200` | **ED-SC 2.0 confirmed at the thin-film dewetting scale.** Cross-scale invariance is empirically supported across ~20 orders of magnitude (Scenario-D lattice → PS-on-Si film). This is the first lab-bench confirmation of ED-SC 2.0 outside the canonical reference system. |
| **NEAR-PASS:** `r̄ ∈ [−1.80, −1.50]` or `[−1.10, −0.90]` (just outside band) | **Partial support.** The test is sensitive to the motif-filter parameters and the pre-rupture window; a mis-calibrated anneal time or a slightly-rough sample could bias by this amount. Options: re-run on additional samples at different anneal times; tighten the pre-rupture window using the histogram / power-spectrum gates of §5.3; report as "consistent in direction, outside strict band." |
| **FAIL:** `r̄` outside `[−1.80, −0.90]` but `N_motif_total ≥ 200` and sampling-condition gates pass | **ED-SC 2.0 is falsified at the thin-film scale.** The cross-scale invariance claim of §2 is rejected at the measured precision; a class partition (§4 of ED-SC-2.0.md) must be declared, or the claim must be narrowed to systems that do match Scenario D. Write a falsification memo; freeze the dataset; flag for revision of ED-SC 2.0. |
| **UNDECIDABLE:** `N_motif_total < 200` OR sampling-condition gates systematically fail | **Cannot evaluate.** This is the pilot's outcome, carried over. Root cause is under-resolution or sample preparation out of regime. Diagnose; re-scan or re-prep; do not report a verdict. |
| **SPLIT:** mean in band but per-sample medians bi-modally distributed (some in band, some far out) | **Class partition detected.** Some samples are architecturally equivalent to Scenario D, others are not. Try to identify the partitioning covariate (anneal time? MW? spin speed?) and report as a narrowed claim. |

A `PASS` outcome is a publishable empirical result for ED. A `FAIL` is also a publishable empirical result — it narrows the cross-scale claim. `UNDECIDABLE` is not a result; it just means re-run.

---

## 6. Deliverables

### 6.1 Raw data deliverables

Per-sample subfolder under `data/ED-Data-ED-SC-AFM/<sample_label>/`:

```
<sample_label>/
├── optical/
│   └── <sample_label>_optical_<anneal_min>min.png   # §3.4 microscope check
├── afm/
│   ├── frame_01.h5     # raw h(x,y) + metadata
│   ├── frame_01.txt    # ASCII backup
│   ├── frame_02.h5
│   ├── ...
│   └── metadata.json   # §6.2 schema
└── analysis/
    ├── per_frame.csv    # one row per frame: medians, IQRs, counts, L_coh, gate outcomes
    ├── ensemble.json    # §5.5 ensemble statistics
    └── verdict.md       # §5.6 outcome + decision tree output
```

### 6.2 Per-sample metadata schema (`metadata.json`)

```json
{
  "sample_label": "20260501-10kg-1pct-3000rpm-130C-15min-Si-rep2",
  "date": "2026-05-01",
  "substrate": {"material": "Si/SiOₓ", "cleaning": "piranha", "size_mm2": 100},
  "polymer": {"type": "PS", "mw_kg_mol": 10, "source": "Polymer Source P-12345"},
  "solvent": {"type": "toluene", "grade": "HPLC"},
  "solution": {"wt_pct": 1.0},
  "spin_coat": {"rpm": 3000, "time_s": 30, "expected_thickness_nm": 15},
  "anneal": {"T_C": 130, "time_min": 15, "stabilisation_s": 90},
  "optical_check": {"result": "pass", "image": "optical/20260501-10kg-1pct-3000rpm-130C-15min-Si-rep2_optical_15min.png"},
  "afm_session": {
    "facility": "<core name>",
    "instrument": "<vendor model>",
    "tip": "OMCL-AC160TS",
    "mode": "tapping",
    "scan_size_um": [10, 10],
    "pixel_resolution": [512, 512],
    "delta_x_nm": 19.5,
    "scan_rate_Hz": 0.75,
    "n_frames": 10
  },
  "processing": {
    "plane_fit": "global_1st_order",
    "smoothing": "none",
    "other_filters": "none"
  },
  "notes": "<free text>"
}
```

### 6.3 Ensemble result deliverable (`ensemble.json`)

```json
{
  "n_samples": 5,
  "n_frames_total": 43,
  "n_frames_gate_passed": 38,
  "n_motif_total": 612,
  "r_bar_mean_of_medians": -1.28,
  "r_bar_std_of_medians": 0.14,
  "r_bar_uncertainty_on_mean": 0.023,
  "aggregate_median": -1.31,
  "per_sample_means": [-1.26, -1.35, -1.29, -1.22, -1.31],
  "per_sample_in_band_count": 5,
  "percent_in_band_motif": 0.68,
  "percent_in_band_all": 0.23,
  "verdict": "PASS",
  "notes": "..."
}
```

### 6.4 Repo-level deliverables

When the session is complete:

1. Create `papers/ED-SC-AFM/` folder with:
   - `paper.md` — single-paper write-up (concept, prediction, methods, data, result, discussion, 6–10 pages).
   - `figures/` — per-frame h(x,y) renderings, saddle-overlay visualisations, median distributions, ensemble summary plot.
2. Update `data/ED-Data-ED-SC-AFM/README.md` with a data-provenance note.
3. Update [`docs/ED-Orientation.md`](../../docs/ED-Orientation.md) §7 "Empirical status at a glance" with the outcome (and move the existing AFM row from ⏳ to ✓ or ✗).
4. If `PASS`: update `RESULTS.md` at the repo root.

---

## 7. Budget and timeline

| Phase | Effort | Cost (rough) |
|:---|:---|:---|
| Sample prep (4–6 samples via collaborator) | 2 hr your time + 4 hr collaborator | Trivial, possibly free |
| Optical-microscope check | 30 min | Trivial (walk-up microscope) |
| AFM session (8 hr instrument time, with operator) | 1 session day | $400–$800 at most academic cores |
| Data export, gates, main analysis | 4 hr | Your time only |
| Ensemble analysis + verdict | 2 hr | Your time only |
| Paper write-up | 1–2 days | Your time only |

Total outside-your-time cost: ~$500 for a complete N=5 samples × 10 frames run. This is **the least expensive canonical cross-scale ED test that can be run today** given current repo infrastructure.

---

## 8. Risks and their mitigations

| Risk | Probability | Mitigation |
|:---|:---|:---|
| No soft-matter collaborator available for sample prep | Low | PS-on-Si is a textbook system; a polymer-chemistry department at any research university will have the recipe |
| All samples annealed past rupture | Medium | §3.3 anneal-time sweep with 4–6 conditions; §3.4 optical check before AFM |
| AFM facility exports only PNG/JPG | Low (but real) | §5.1 pre-session explicit request; verify during the first frame that you're getting raw arrays, not screenshots |
| `L_coh < 8·Δx` on exported frames | Low if §4.3 sampling check is done at instrument | Re-scan at higher pixel resolution or smaller scan size |
| `N_motif < 10` per frame (pilot's failure mode) | Low on proper AFM (pilot's issue was pseudo-height image) | §5.3 gate rejects these; if systematic, diagnose (sample out of regime? `L_coh` estimate wrong?) |
| Tip contamination mid-session | Medium | Change tips between samples; budget one spare tip per sample |
| Ambiguous verdict (`r̄` just outside band) | Medium | §5.6 NEAR-PASS decision tree; run additional samples at different anneal times |
| Sampling covariate (e.g., only some anneal times match) | Medium | §5.6 SPLIT decision tree — publishable as a narrowed claim |

---

## 9. Connection to the broader ED program

**Why this test matters.** ED-SC 2.0 is the architectural heart of the ED program: the claim that cross-scale invariants exist at the level of motif-conditioned Hessian statistics, separating ED from every physics framework that treats scales as independent. An AFM confirmation — or falsification — is the first lab-bench datum for this claim. Previous evidence is simulation-only (Scenario D) or inferred (Local Group mass sheet from cosmological reconstructions).

**How this fits with the other empirical tracks.**
- **ED-XX environment-sourcing (§6 of orientation):** cosmological; decades-long timescale for WL + BTFR test programs.
- **Cluster Merger-Lag (repo Cluster Merger-Lag):** already in hand; 7 clusters + Finner aggregate.
- **UDM soft-matter (repo Universal_Mobility_Law):** already in hand; 10 materials, R² > 0.986.
- **ED-09.5 quantum-classical sharp transition:** Vienna ecosystem program map; year+ timescale.
- **FRAP reanalysis:** Lomb-Scargle on literature curves; day-of-work but dependent on external dataset quality.
- **AFM (this protocol):** ~1 week sample-prep + 1–2 day session + ~1 week analysis. **Self-contained; no third-party dependencies.** The fastest path to a new empirical result in the ED program.

**Expected timeline from protocol adoption to publishable result:** 4–6 weeks, including facility booking lead time.

---

## 10. References

- [`ED-SC-2.0.md`](../../docs/ED-SC-2.0.md) — the canonical ED-SC 2.0 invariance statement; §1.4 motif filter, §2 claim, §3 domain of applicability, §4 falsification, §5 cross-scale test protocol.
- [`ED-Orientation.md`](../../docs/ED-Orientation.md) §6.9 — ED-SC 2.0 summary for orientation; §7 AFM row in empirical-status table; 2026-04-20 top-of-doc entry on the three-routes strategy.
- [`analysis/scripts/ed_arch_r2/ThinFilm_Pilot_Memo.md`](../../analysis/scripts/ed_arch_r2/ThinFilm_Pilot_Memo.md) — the N=1 pilot result and its undecidable verdict; motivates this protocol.
- [`analysis/scripts/ed_arch_r2/cross_scale_01_thinfilm_pilot.py`](../../analysis/scripts/ed_arch_r2/cross_scale_01_thinfilm_pilot.py) — the re-runnable analysis script; already implements §5.4's full pipeline.
- Jacobs et al., Saarland — canonical PS-on-Si dewetting group; see the 2023 *Nat Comm Phys* paper referenced in the orientation doc's Route 1 for accessible data alternatives.
- Seemann, R., Herminghaus, S., Jacobs, K. (2001). *Dewetting patterns and molecular forces.* J. Phys. Condens. Matter 13 4925 — foundational paper on PS-on-Si spinodal dewetting, with anneal-time windows.

---

*This protocol is the operational translation of ED-SC 2.0 Route 3. It does not modify the canonical ED-SC 2.0 parameters, claims, or falsification criteria. If a result in contradiction with the canonical parameters is produced, document it in a separate memo and propose a revision — do not modify this document in place.*
