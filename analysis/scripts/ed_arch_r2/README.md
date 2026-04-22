# ED-Arch R2 — Field-Space Hessian Reproduction

This directory contains the code, data, and memos supporting the R2 field-space Hessian test of ED-Arch-01's cross-scale invariance claim. The test resolved the parameter-space vs field-space Hessian ambiguity in ED-Arch-01 §5 / ED-Arch-02 §3 in favour of the field-space form, and then refined the invariance claim to the motif-conditioned median form now canonicalised in `docs/ED-SC-2.0.md`.

## Directory contents

### Canonical scripts (active)

| File | Purpose |
|:-----|:--------|
| `r2_canonical.py` | **Canonical Scenario D reproduction.** Uses the actual update rule from `Emergence Universe/ED-SIM-Code/ED_Update_Rule.py:ed_step_mobility` with parameters `α = 0.03, γ = 0.5, dt = 0.05, size = 64, IC = uniform[0.3, 0.7], seed = 77, boundary = periodic, mobility mode`. Runs the saddle-peak `(n* = 2.7, σ* = 0.0556)` plus the full 4×4 sweep. Writes `r2_canonical_p_final.npy`, `r2_canonical_ratios.npy`, `r2_canonical_summary.txt`. |
| `r2_motif_filter.py` | **Motif-conditioned architectural-saddle filter** on the canonical field. Scans `(α, L_ray, monotone) ∈ {0.25, 0.5, 0.75, 1.0} × {2, 3, 4, 6, 8} × {False, True}`. Reports motif-conditioned ratio distributions. The pre-registered filter parameters for ED-SC 2.0 are `α_filt = 0.25, L_ray = 2, δ = 0.10`. |
| `r2_motif_details.py` | Per-saddle dump and textual histogram at the best motif-filter setting. Lists individual saddle ratios, locations, and Hessian eigenvalues. |

### Data artifacts (canonical run outputs)

| File | Contents |
|:-----|:---------|
| `r2_canonical_p_final.npy` | Final `p(x, y)` field, 64×64, at `(n*, σ*)` with seed 77. Reference field for the ED-SC 2.0 calibration measurement. |
| `r2_canonical_ratios.npy` | Full set of saddle ratios from the canonical run (95 Morse saddles at the peak, ~80–100 at other sweep points). |
| `r2_canonical_summary.txt` | Plain-text summary of the full 4×4 sweep. |
| `r2_motif_summary.txt` | Motif-filter scan results across all `(α, L_ray, monotone)` triples. |

### Memos

| File | Scope |
|:-----|:------|
| `R2_Canonical_Memo.md` | Canonical reproduction method, parameter choices, 4×4-sweep results, resolution verdict (field-space Hessian distribution is broad; parameter-space `−1.3` is not the field-space distribution centre). |
| `R2_Motif_Verdict.md` | Motif-filter application, verdict (motif-conditioned median = −1.304, matches ED-Arch-01 published value within 0.004). Statement of what the filter recovers and what it does not. |

### Deprecated scripts (kept for provenance)

Earlier R2 attempts used an incorrect update rule (linear-coefficient Laplacian with `n` as Laplacian coefficient, `α = 1.0`, `γ = 3`, unstable `dt = 1`). These scripts are retained so the session audit trail is reproducible. **Do not use them for current ED-SC 2.0 work.**

| File | Why deprecated |
|:-----|:---------------|
| `r2_field_hessian_test.py` | Used wrong update rule (linear-coefficient form, not mobility-weighted). The `dt = 1` attempt is numerically unstable at `n = 2.7`. A later edit patched to `dt = 0.1`, but the rule was still wrong. |
| `r2_robustness_check.py` | Scanned (α, γ, seed) under the wrong update rule. Result was robust but wrong. |
| `r2_coarsegrained.py` | Multi-scale coarsening check on the wrong-rule field. |
| `r2_visualize.py` | Generic histogram + field plotter; still works on any saved `.npy` but was used with the deprecated field. |
| `r2_field_full.png`, `r2_visualization.png` | Plots of the deprecated field. |
| `r2_field_hessian_ratios.npy`, `r2_p_final.npy` | Outputs of the deprecated run. |
| `r2_field_hessian_summary.txt`, `r2_robustness_summary.txt` | Summaries of the deprecated runs. |

## How to reproduce the ED-SC 2.0 reference measurement

```bash
cd "C:/Users/allen/GitHub/Event Density"
python analysis/scripts/ed_arch_r2/r2_canonical.py    # runs canonical Scenario D
python analysis/scripts/ed_arch_r2/r2_motif_filter.py # applies motif filter, scans (α, L_ray, mono)
python analysis/scripts/ed_arch_r2/r2_motif_details.py # dumps individual saddle ratios
```

Expected key output from the motif filter at the pre-registered setting `(α=0.25, L_ray=2, mono=False)`:

- `N_motif = 6` admitted saddles
- `median(ℛ_motif) = −1.304`
- IQR = `[−1.940, −1.211]`, width 0.728
- Fraction in ED-Arch-01 window `[−1.5, −1.1]`: 50.0%

**This reproduces the reference measurement for ED-SC 2.0 §7.**

## Dependencies

- Python 3.12 with numpy, scipy.
- The canonical Scenario D code in `C:/Users/allen/GitHub/Emergence Universe/ED-SIM-Code/`. Specifically, `r2_canonical.py` imports `ed_step_mobility` and `coarse_grained_stats` from `ED_Update_Rule.py`. If that repo is not present at the expected path, edit the `ED_SIM_CODE` constant near the top of `r2_canonical.py`.

## Cross-references

- **`docs/ED-SC-2.0.md`** — canonical architectural invariance statement. The motif filter in this directory is the reference implementation for the filter defined in §1.4 of that statement. The output `median(ℛ_motif) = −1.304` is the reference measurement cited in §7.
- **`docs/ED-SC-Hessian-Resolution.md`** — how the parameter-space vs field-space ambiguity was identified.
- **`docs/ED-SC-Clarification-2026-04-17.md`** — the clarification question that was posed and resolved in favour of Option 2.
- **`docs/ED-Orientation.md`** — orientation-level integration of the above.

## Open items (tracked from ED-SC-2.0.md §8)

1. **Ensemble statistics over seeds.** The reference measurement is from seed 77 only. Running 20+ seeds and reporting `median(ℛ_motif)` across the ensemble would give uncertainty on the `−1.304` calibration. Not blocking.
2. **Alternative motif detectors.** The current filter is ray-based with threshold `α = 0.25`. Persistence-based Morse–Smale, TDA, or channel-graph detectors should reproduce the result. Cross-check pending.
3. **First cross-scale test.** Thin-film dewetting AFM data is the recommended first real-data test (see `docs/ED-SC-2.0.md` §5.3). No code yet.
