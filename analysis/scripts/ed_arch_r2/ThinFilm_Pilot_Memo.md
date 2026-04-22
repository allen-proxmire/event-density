# ED-SC 2.0 Cross-Scale Test #1 — Thin-Film Dewetting (PILOT)

**Date:** 2026-04-17. **Mode:** PILOT / demo. **Status:** completed; verdict below.

**Source field:** `outputs/thinfilm_pilot_input.png` (187 × 178 px). Cropped AFM-like thin-film frame described by the user as "770 s". Pixel brightness is interpreted as relative height `h(x, y)`. This is **not** a canonical AFM dataset — absolute heights, physical grid spacing, and sample identification are unknown. Pilot demonstrates the pipeline only.

## Procedure

1. **Grayscale conversion.** Image loaded via PIL and converted to L-mode. Values normalized to `[0, 1]`.
2. **Detrending.** 2D polynomial fit (degree 2) subtracted to remove large-scale tilt and background gradients. Result re-normalized to `[0, 1]`.
3. **Smoothing.** Light Gaussian filter with `σ = 0.8` pixels (wrap boundary) to stabilize central-difference derivatives.
4. **Saddle detection.** Central-difference gradient sign-flips in both `x` and `y`; Hessian via 5-point stencil; Morse condition `det(H) < 0` with non-degeneracy `|λ_min|/|λ_max| ≥ δ`, `δ = 0.10`.
5. **Motif filter (canonical, per ED-SC 2.0 §1.4).** `α = 0.25`, `L_ray = 2`, periodic wrap. Thresholds `E_hi = h̄ + α·σ_h`, `E_lo = h̄ − α·σ_h`. Admit saddle iff both `±ê_neg` ray endpoints are `< E_lo` and both `±ê_pos` ray endpoints are `> E_hi`.

No filter parameters were retuned. The canonical `(α, L_ray, δ)` triple was used exactly as written in `docs/ED-SC-2.0.md`.

## Field statistics after preprocessing

| Quantity | Value |
|:---|:---|
| Shape | 178 × 187 |
| `h̄` | 0.59161 |
| `σ_h` | 0.12556 |
| range | `[0.021, 0.982]` |
| `E_lo` | 0.56022 |
| `E_hi` | 0.62300 |
| coherence length `L_coh = 1/⟨‖∇h‖⟩` | ~40 px |

## Morse-saddle population (before motif filter)

| Quantity | Value |
|:---|:---|
| `N_Morse` (after degeneracy filter) | **148** |
| median `r` | **−2.149** |
| IQR | `[−3.959, −1.465]` |
| fraction in ED-SC 2.0 window `[−1.5, −1.1]` | **23.0%** |

This distribution is quantitatively similar to Scenario D's raw Morse-saddle distribution (median −2.063, IQR `[−3.43, −1.49]`, 21.7% in window — see `R2_Motif_Verdict.md`). The thin-film pseudo-field and the canonical Scenario-D simulation field share similar raw saddle-ratio statistics.

## Motif-conditioned distribution `ℛ_motif`

| Quantity | Value |
|:---|:---|
| `N_motif` | **0** |
| median | undefined |
| IQR | undefined |
| fraction in window | undefined |

**No saddle passes the canonical motif filter on this image.**

## Verdict (pilot mode)

**Undecidable under the canonical ED-SC 2.0 filter.** The `(α = 0.25, L_ray = 2)` filter admits zero saddles, so `ℛ_motif` is empty and the median invariant cannot be computed. Under the pre-registration rules of `docs/ED-SC-2.0.md` §4, filter parameters cannot be retuned to recover a sample, so the test cannot produce a PASS or FAIL verdict on this input.

**This is NOT a falsification of ED-SC 2.0.** It is a "cannot-evaluate" outcome stemming from a filter-resolution mismatch between the canonical parameters (calibrated on a 64×64 Scenario-D lattice with `L_coh ≈ 178` lattice units) and this 187-pixel natural image (with `L_coh ≈ 40` pixels). The `L_ray = 2 px` ray length is ~1/20 of the coherence scale here, too short to reach above/below the 0.25-σ threshold in the smooth-field background.

**Candidates for why the canonical filter under-admits on this image, in priority order:**

1. **Ray-length / coherence-length mismatch.** On Scenario D the motif filter was calibrated at a specific ratio `L_ray / L_coh`. Here that ratio is much smaller. A scale-aware reformulation (e.g., `L_ray ∝ L_coh`) would be a future refinement of the filter, but is NOT part of the canonical ED-SC 2.0 specification.
2. **Image-derived noise character.** AFM images have imaging noise that is not the same as the Gaussian Langevin noise of Scenario D. The local field smoothness may not match the Scenario D architectural assumption.
3. **Small n_holes.** Only ~3 dewetting holes are visible. Motif saddles in ED-Arch are expected at junctions between well-formed pockets; a frame with 3 isolated holes may simply have few such junctions in the first place, before any filter is applied.

## Caveats (as-built)

- Pseudo-heightmap derived from image brightness; absolute height and physical scale are unknown.
- Cropped frame at 770 s from a movie; boundary effects may be non-trivial at 187 px without the surrounding frame context.
- No physical grid spacing `Δx`, so `L_coh` is reported in pixels only.
- Periodic-wrap boundary imposed artificially; real AFM imagery does not respect it.
- 2D polynomial detrend (degree 2) was used; higher or lower degree would slightly change the baseline.
- Light smoothing (σ = 0.8 px) was applied; without smoothing the gradient noise dominates the Hessian estimate.

## Artifacts

Written under `analysis/scripts/ed_arch_r2/`:

- `cross_scale_01_thinfilm_pilot.py` — pilot script (re-runnable).
- `thinfilm_pilot_h.npy` — preprocessed `h(x, y)` field.
- `thinfilm_pilot_ratios_all.npy` — saddle ratios before the motif filter.
- `thinfilm_pilot_ratios_motif.npy` — motif-admitted ratios (empty for this pilot).

## What this result means for the ED-SC 2.0 program

Under the strict pre-registration framework, the pilot is **not a PASS and not a FAIL — it is a test that cannot be executed as specified on this input** because the canonical filter produces an empty sample. Two next steps are consistent with ED-SC 2.0:

1. **Try a canonical AFM dataset** with resolution `Δx ≤ L_coh/8` per §3. A proper dewetting AFM scan with more holes and a grid-to-coherence ratio closer to Scenario D's may yield a non-empty `ℛ_motif`.
2. **Develop a scale-aware motif filter** (e.g., `L_ray` scaled to a fixed fraction of `L_coh`). This would be a **revision** of ED-SC 2.0, requiring a new calibration of `r*` on Scenario D under the new filter. Out of scope for the pilot.

Neither change affects the validity of the ED-SC 2.0 statement on Scenario D or on systems where the canonical filter admits non-empty samples.
