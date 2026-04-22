# ED-RLC-Analogue — Pre-Registered Measurement Reference

**Status:** locked pre-bench predictions for the four-run RLC sweep. Use this document as the single source of truth when the parts arrive and the bench work begins.

**Version:** 1.0, 2026-04-21. **Source:** `rlc_predictions.py` + `memo.md` §3.2. **Figures:** `rlc_predictions/predicted_run_{A,B,C,D}.png` + `rlc_predictions/all_runs_combined.png`. **Machine-readable summary:** `rlc_predictions/summary_table.json`.

---

## Purpose

These four runs test the ED uniform-limit → RLC isomorphism at four distinct points in (L, R, C) space. Each run produces a **specific predicted ringdown trace** with specific measurable quantities (oscillation frequency, decay rate, Q factor). If the measured quantities match the predictions at ≥ 3 of the 4 runs within component tolerance, the ED→RLC mapping is confirmed in hardware. If they disagree systematically, the mapping has a bug.

## The mapping (from `memo.md` §3.2)

For a series-RLC benchtop realization with step input or ringdown from pre-charged capacitor:

$$2\gamma = R/L, \qquad \omega_0^2 = 1/(LC), \qquad \omega = \sqrt{\omega_0^2 - \gamma^2}, \qquad Q = \omega_0/(2\gamma)$$

This is mathematically identical to the ED uniform-limit eigenmode structure

$$2\gamma = DP_0 + \zeta/\tau, \qquad \omega_0^2 = (DP_0 \zeta + H\kappa)/\tau$$

under the correspondence (memo §3.2)

$$DP_0 \leftrightarrow 1/(R_P C), \qquad H \leftrightarrow -1/C, \qquad \kappa/\tau \leftrightarrow 1/L, \qquad \zeta/\tau \leftrightarrow R_L/L$$

## The four runs

All runs use **C = 1 µF** (built from parallel 0.47 µF + 0.56 µF from the kit). L and R vary.

| Run | L | R_external | R_total (incl. DCR) | Predicted f | Predicted Q | Period | Envelope τ | Cycles to 1% |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **A** | 10 mH | 0 Ω | ~30 Ω (DCR only) | **1574 Hz** | **3.33** | 635 µs | 667 µs | ~4.9 |
| **B** | 10 mH | 50 Ω | ~80 Ω | 1459 Hz | 1.25 | 685 µs | 250 µs | ~1.8 (near-critical) |
| **C** | 1 mH | 0 Ω | ~3 Ω (DCR only) | **5027 Hz** | **10.5** | 199 µs | 667 µs | ~15 |
| **D** | 100 µH | 0 Ω | ~0.5 Ω (DCR only) | **15911 Hz** | **20.0** | 63 µs | 400 µs | ~29 |

(DCR values are typical manufacturer specs for Bourns RLB0913 series — measure with the DE-5000 before first run and record in the summary JSON.)

## Distinctive fingerprints (what you should see on the scope)

| Run | Scope appearance | Timebase setting |
|:---|:---|:---:|
| A | ~5 clear cycles of damped sinusoid, period visibly ~0.6 ms | 500 µs/div |
| B | 1–2 cycles before envelope dies; nearly critically damped; looks like a heavy-damped "thump" | 200 µs/div |
| C | ~15 clean cycles at audio frequency (~5 kHz); sustained oscillation | 100 µs/div |
| D | ~30 cycles at 16 kHz, very clean and fast | 20 µs/div |

If what you see on the scope doesn't match the described fingerprint, check: (1) C is correctly 1 µF (measure with LCR), (2) L matches the expected inductor (DE-5000 can confirm to 1%), (3) the circuit topology is correct.

## Measurement protocol (per run)

1. **Verify components with DE-5000 LCR meter.** Record actual L, C, DCR values in the summary JSON before building.
2. **Wire the series RLC on the breadboard.** Battery + pushbutton (or function generator square wave) + L + C + GND; scope probe across C.
3. **Trigger the ringdown:** pushbutton method — charge C to battery voltage, release; single-shot scope capture on falling edge. Square-wave method — continuous trigger on falling edge.
4. **Capture ~5 envelope time constants of data** in a single trace. For Run A that's ~3.3 ms; for Run D it's ~2 ms.
5. **Measurements to extract from the trace:**
   - **Period T** (measure between consecutive zero crossings, or between peak pairs) → `ω_measured = 2π/T`
   - **Envelope decay** (fit `A · exp(-γt)` through peak-by-peak amplitudes, or read `amplitude(t1)/amplitude(t2)` and compute `γ = ln(ratio)/(t2-t1)`)
   - **Visible cycles** before amplitude drops below 1% of initial → gives independent Q check via `N_cycles ≈ Q · ln(100)/π`
6. **Compute ratios:**
   - `ω_measured / ω_predicted`
   - `γ_measured / γ_predicted`
   - `Q_measured / Q_predicted`
7. **Record measurements in the `measured` block** of `rlc_predictions/summary_table.json`.

## Pass / fail criterion

**PASS at run X** if all three measured ratios are within **± 10%** of the predicted value. This tolerance accounts for:
- Component tolerance (±5% on film caps, ±10% on inductors, ±1% on metal-film resistors)
- DCR measurement uncertainty (±5% at 100 Hz LCR test frequency for small inductors)
- Scope resolution (±0.5% on timebase on any modern scope)

**Overall PASS** if ≥ 3 of the 4 runs pass. **FAIL** if any systematic trend in the residuals (e.g., measured ω consistently below predicted at all runs) suggests a missing physical effect.

## What passing means

- Circuit-theoretic ω and γ formulas hold in the hardware at component-tolerance precision.
- The ED→RLC mapping of `memo.md` §3.2 is validated not just in simulation (machine precision, already done in the Foundational Paper v2 Analogue 1) but in the physical world.
- The RLC-analogue bullet on the Aaronson email (and anywhere else the ED program cites it) moves from *"simulation-verified"* to *"confirmed in hardware to ±X% across two decades of L and one decade of Q"*.

## What failing means

- A systematic low-by-factor-K offset (e.g. all measured ω are 0.9 × predicted across runs) likely indicates an unmodeled parasitic (inductor self-capacitance, capacitor ESL, breadboard inductance) rather than a failure of the ED mapping. Document and rerun with tighter component selection.
- A run-dependent pattern (e.g. ω agrees at Run A but fails at Run D) likely indicates a scope bandwidth or sample-rate issue. The Rigol DS1054Z has 1 GSa/s; at Run D's 16 kHz, that's 60000 samples per cycle — plenty. So this failure mode is unlikely with the recommended scope.
- A total miss (measured ω completely wrong) indicates circuit-wiring error or mis-built C. Debug and rerun.

## Deliverables after benchtop run

Write `bench_result.md` in this folder with:

1. Actual L, C, DCR values measured with DE-5000 before each run.
2. Scope screenshots of each run's ringdown (4 PNG files, `scope_run_{A,B,C,D}.png`).
3. Extracted ω_measured, γ_measured, Q_measured per run (table).
4. Ratios measured/predicted per run.
5. Overall pass/fail verdict.
6. Any observations about non-idealities (inductor saturation, ESR, ground-loop artifacts).

The summary_table.json has placeholder `measured` blocks — fill those in programmatically and check ratios with a short script.

## Expected total bench time

- **DE-5000 component characterization:** ~15 min (four inductors, 5 capacitor values).
- **Circuit construction (first run):** ~15 min.
- **Per-run data capture:** ~10 min (swap inductor, verify, capture single-shot, save trace).
- **Analysis:** ~30 min (fit peaks, compute ratios, write up).

**Total: ~2 hours** for the full four-run test.

## Cross-references

- **Derivation:** `memo.md` §§1–4 (ED uniform-limit → RLC)
- **Simulation verification:** Foundational Paper v2 §7 Analogue 1 (machine-precision match at three H values in the ED equations)
- **Shopping list for the hardware:** the project conversation on 2026-04-21 (parts ordered from Amazon + Digi-Key)
- **For the Aaronson email:** the RLC bullet updates from "simulation-verified" → "hardware-verified to ±X%" after the bench run completes.
