# Alternative 1 Execution Plan — Nonlinear RLC Third-Harmonic Generation

## 1. Parts List

### 1A. Reused from AstroAI Kit (ordered 2026-04-22)

- Resistor kit — pick values per §1C
- Capacitor kit — pick values per §1C
- Breadboard (830-point or equivalent)
- Jumper wires

### 1B. New Components to Acquire

- **Primary nonlinearity** — 2 × 1N4148 small-signal diodes (anti-parallel pair), ~$0.10 each
- **Inductor** — 10 mH ± 5%, ≥ 100 mA current rating (fixed or Bourns RFB0807-103L-class), ~$2
- **Optional asymmetric-variant diode** — 1 × 1N4148 alone, ~$0.05 (for A₂ extraction in a second run)
- **Drive source** — function generator (lab bench or ~$30 USB PC-controlled JDS6600/FY6900-class) capable of sine at 1–10 kHz with ≤ 0.1% THD
- **Acquisition** — USB oscilloscope or PC line-in at ≥ 48 kS/s with ≥ 14-bit resolution (Digilent Analog Discovery, PicoScope 2204, or modern PC soundcard)
- **Optional differential probe** — if acquisition ground is not isolated from drive ground

### 1C. Component Values (Primary Run)

- `L = 10 mH`, `R = 10 Ω` (series with L), `C = 1 μF`
- Natural frequency `f₀ = 1/(2π√LC) ≈ 1591 Hz`
- Quality factor `Q = (1/R)·√(L/C) ≈ 10` (underdamped, clean resonance)
- Third-harmonic frequency `3f₀ ≈ 4.77 kHz` (well below Nyquist at 48 kS/s)

## 2. Circuit Topology

### 2A. Core RLC Loop (Linear Baseline)

- Drive source `V_s(t) = V_drive·sin(2π f₀ t)` connects to node A
- Series: A → R (10 Ω) → L (10 mH) → B
- Parallel: B → C (1 μF) → ground
- Measurement node — V_C across the capacitor (ground to B)

### 2B. Nonlinearity Injection

- **Primary (symmetric)** — anti-parallel pair of 1N4148 diodes across C (B to ground), provides odd-symmetric clipping at ±0.6 V
- **Alternative (asymmetric)** — single 1N4148 across C, cathode to ground, provides asymmetric clipping (activates A₂ channel)
- Both variants leave the linear RLC operating point at `V_C < 0.5 V` peak; nonlinearity engages as drive amplitude increases into the 0.6–2 V range

### 2C. ASCII Schematic

```
           R         L
  V_s ----/\/\------mmm------+------+------+
   |                          |      |      |
   |                          C     D1     D2
   |                          |      |(rev)|
   GND -------------------------+----+-----+-----+
                                      |          |
                              measure V_C    (D1 || D2 reversed)
```

- **Probe point** — V_C (node B to ground)
- **Optional** — also probe V_R (across R) for current-proxy measurement if differential probe available

## 3. Drive-Frequency Selection

- Drive at `f₀ = 1591 Hz` (resonance of the linear RLC)
- Verify measured `f₀` with a pre-run amplitude-frequency sweep at low drive (10 mV) before triad runs
- If measured `f₀` differs from nominal by > 2%, update scripts with the measured value
- Stay ≥ 5% away from integer multiples of 60 Hz (or 50 Hz in EU) — at 1591 Hz this is satisfied automatically

## 4. Amplitude Sweep Plan

### 4A. Sweep Points (6 amplitudes, ≥ 1.5 decades)

| Point | `V_drive` (peak) | Role |
|:---|:---|:---|
| 1 | 20 mV | Linear-regime baseline; used to measure instrument + circuit THD floor |
| 2 | 50 mV | Low-end triad; V_C peak well below diode knee |
| 3 | 150 mV | Threshold regime |
| 4 | 400 mV | Diode knee approach |
| 5 | 1.0 V | Active clipping |
| 6 | 2.0 V | Strong clipping; saturation-regime cross-check |

### 4B. Per-Point Settling and Dwell

- Change amplitude; wait ≥ 0.5 s for steady-state transient to die (>> 10·Q/f₀ ≈ 6 ms)
- Acquire ≥ 100 drive periods per point (~63 ms at 1591 Hz)
- Repeat acquisition 3 times per point; retain per-repeat record for statistics

## 5. Acquisition Parameters

- **Sample rate** — 48 kS/s minimum (preferred 96 kS/s); resolves harmonics up to 24 kHz
- **Bit depth** — 14 bits minimum (16 bits preferred for low-amplitude points)
- **Record length per point** — ≥ 100 drive periods per capture
- **Trigger** — drive-signal zero-crossing, rising edge; ensures consistent phase reference across amplitude sweep
- **Coupling** — AC to remove DC offset; verify no clipping at the ADC (use ≥ 10% headroom above expected peak)
- **Grounding** — common ground between drive, RLC, and scope; avoid ground loops by using one power strip
- **Temperature** — record ambient T at start and end; diode Vf shifts ~2 mV/°C

## 6. THD Floor Calibration (Pre-Triad Baseline)

### 6A. Instrument-Only Baseline

- Drive the function generator directly into the acquisition input (no RLC, no diodes)
- Acquire at each amplitude in §4A
- Measure A₃/A₁ and A₂/A₁ — this is the instrument-level harmonic floor
- Record values as `thd_floor.csv` — must be < 0.003 (0.3%) at the smallest drive for the test to be valid

### 6B. Linear-RLC Baseline (Diodes Removed)

- Build the circuit without diodes; drive and acquire V_C across the amplitude sweep
- Expected A₃/A₁ ≈ instrument floor (RLC is linear; adds no distortion)
- Record as `rlc_linear_baseline.csv`
- If this baseline differs from §6A by > factor 2, trace the source (inductor saturation? capacitor dielectric absorption?) before proceeding

### 6C. Go/No-Go Gate

- Both §6A and §6B must return A₃/A₁ ≤ 0.003 at `V_drive = 20 mV`
- If not met, replace instrument or lower lowest-amplitude point until resolved

## 7. Analysis Pipeline

### 7A. Per-Capture Processing

- Load captured `V_C(t)` and `V_drive(t)` per point
- Detect exact drive period from zero-crossings; crop to integer-period window
- Apply Hann window over the cropped window
- Compute FFT; identify bins at `f₀`, `2f₀`, `3f₀`
- Extract complex amplitudes `Ṽ₁, Ṽ₂, Ṽ₃` at those bins
- Convert to magnitudes — `A₁ = |Ṽ₁|, A₂ = |Ṽ₂|, A₃ = |Ṽ₃|`
- Extract phases — `φ₁ = arg(Ṽ₁), φ₃ = arg(Ṽ₃)`
- Subtract instrument THD floor in quadrature — `A_k^corrected = √(A_k² − A_k_floor²)`

### 7B. Per-Point Aggregation

- Average `A_k` and `φ_k` across the 3 repeats per point; record mean and SD
- Compute `K_instant = A₃ / A₁³` and `K₂_instant = A₂ / A₁²` at this point
- Compute `Δφ = φ₃ − 3·φ₁`, wrap to `(−π, π]`

### 7C. Cross-Amplitude Scaling Fit

- Filter points where `A₃ > 5·A₃_floor` (noise gate) and `A₁ < V_clip` (retain clean regime only; drop V_drive ≥ 1 V if needed)
- Fit `log A₃ = α_3 · log A₁ + log K` across retained points; report slope `α_3`, intercept `K`, R² of fit
- Fit `log A₂ = α_2 · log A₁ + log K₂`; report `α_2, K₂, R²`
- Report phase statistics — `⟨Δφ⟩, SD(Δφ)` across retained points

### 7D. Mapping to Decision Rules ([protocol.md §6](experiements/Triad-Coupling-C7_InProcess/protocol.md))

- **PASS** — `α_3 ∈ [2.8, 3.2]` AND `SD(Δφ) < π/4` AND `K` derivable (note: `K` value will be circuit-specific, not the ED-operator value 0.015); also expect `A₂ ≪ A₃` for symmetric-diode variant
- **FAIL** — `α_3 ∉ [2.5, 3.5]` OR phase-lock absent
- **UNDECIDABLE** — noise-limited at smallest `A₁` (SNR at `3f₀` < 20 dB) OR saturation intruding too early (retain fewer than 4 points in clean regime)
- **SPLIT** — scaling holds over partial range only; investigate sub-ranges

### 7E. Expected Result for the Symmetric Anti-Parallel Pair

- `α_3 ≈ 3.0` (cubic clipping gives cubic harmonic scaling)
- `⟨Δφ⟩ ≈ π` (odd-symmetric clipper; matches ED-operator phase signature)
- `K₂ ≈ 0` (A₂ suppressed by symmetry — distinct from ED-operator value K₂ ≈ 0.28)
- `K` will be circuit-specific; not expected to match the ED-operator value 0.015
- The cross-system invariant being tested is the **scaling exponent** (α_3 = 3) and **phase lock** (Δφ = π), not the `K` absolute value

### 7F. Asymmetric-Variant Follow-Up (Optional Second Run)

- Rebuild circuit with single diode (asymmetric clipper)
- Repeat full amplitude sweep
- Expected `α_2 ≈ 2.0, α_3 ≈ 3.0`, non-zero `K₂`, `⟨Δφ⟩` may differ from π due to asymmetric phase structure
- Second run adds coverage for the `K₂ = A₂/A₁²` invariant distinct from ED-operator structure

## 8. File Manifest — `experiements/Triad-Coupling-C7_InProcess/RLC_Run_<date>/`

### 8A. Input / Setup Files

- `README.md` — run summary, date, operator, component values, one-line verdict
- `bench_setup.md` — photographed / drawn schematic, component lot numbers, ambient T, notes on deviations from §1–§2
- `parts_inventory.csv` — part ID, value, tolerance, source

### 8B. Raw Acquisition

- `baselines/thd_floor_<point>.csv` — per-amplitude instrument-only captures (§6A)
- `baselines/rlc_linear_<point>.csv` — linear-RLC baselines (§6B)
- `raw/antiparallel/point_<N>_rep_<R>.csv` — time-series captures for the symmetric variant; N ∈ {1..6}, R ∈ {1..3}
- `raw/asymmetric/point_<N>_rep_<R>.csv` — same for single-diode variant (optional second run)

### 8C. Analysis Artifacts

- `analysis/fft_extract.py` — script that ingests raw CSVs, produces per-point FFT amplitudes and phases
- `analysis/scaling_fit.py` — fits `α_3, α_2, K, K₂`; outputs `fit_results.json`
- `analysis/fit_results.json` — `{α_3, K, α_2, K₂, ⟨Δφ⟩, SD(Δφ), R², N_retained}`
- `analysis/diagnostic_plots.png` — 4-panel plot: log-log A_k vs A_1, phase offset vs A_1, time traces at 3 amplitudes, FFT spectrum at highest amplitude
- `analysis/decision.md` — one-paragraph mapping to PASS/FAIL/UNDECIDABLE/SPLIT with numerical criteria satisfied

### 8D. Summary

- `verdict.md` — half-page summary: date, variant, amplitudes covered, fit results, decision, coverage-matrix cell delta for [`docs/ED-Test-to-Axiom-Mapping-v1.0.md`](docs/ED-Test-to-Axiom-Mapping-v1.0.md)
- Link back — append one line to [`experiements/Triad-Coupling-C7_InProcess/README.md`](experiements/Triad-Coupling-C7_InProcess/README.md) pointing to this run folder

## 9. Budget and Timeline

- **Incremental cost** — 2 × 1N4148 diodes ($0.20) + 10 mH inductor ($2) + optional USB scope ($0–150 if not on hand) ≈ $2–152 total
- **Bench time** — 1 day: 2 hrs setup and calibration, 2 hrs primary run, 1 hr asymmetric-variant run
- **Analysis time** — 1 day
- **Wall time to decision** — 2–3 days from components-in-hand

## 10. Decision Point for the User

- **Approve as-is** — proceed with anti-parallel diode variant on the already-ordered AstroAI kit plus a $2 diode order
- **Approve with expansion** — add the asymmetric single-diode variant to the same run for K₂ extraction (+1 hr bench time, no extra parts)
- **Defer** — wait until AFM Top-1 acquisition is commissioned and run both in parallel

Plan complete; awaiting decision before any bench execution.
