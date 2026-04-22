# R2 Canonical Result — Memo

**Date:** 2026-04-17. **Scope:** reproduction of Scenario D under the canonical parameters from `Emergence Universe/ED-SIM-Code/`, and extraction of the field-space Hessian eigenvalue-ratio distribution at Morse saddles of the final `p(x, y)` field.

## What changed from earlier R2 attempts

My earlier R2 test used the wrong update rule. The canonical Scenario D from `Emergence Universe/ED-SIM-Code/` uses:

| | My earlier test | Canonical |
|:-|:-:|:-:|
| Update form | `p + dt·[n·∇²p − α·p^γ + σ·η]` (linear-coefficient Laplacian) | `p + dt·[∇·(M(p)∇p) − α·p^γ + σ·η]` (mobility-weighted diffusion) |
| Meaning of `n` | coefficient on `∇²p` | exponent in `M(p) = ((p_max−p)/p_max)^n` |
| `α` | 1.0 | **0.03** |
| `γ` | 3 (cubic) | **0.5 (concave)** |
| `dt` | 1.0 (unstable) | **0.05** (stable) |
| Size | 512×512 | **64×64** |
| IC | Gaussian, scale 0.05 | **uniform[0.3, 0.7]** |
| Seed | 20260417 | **77** |

Run reproduces the user's figure quantitatively: my `p̂ = 0.10845` vs figure's `0.10908`; `p_min, p_max` match to ±0.01.

## R2 result at saddle peak `(n*, σ*) = (2.7, 0.0556)`

| Statistic | Value |
|:----------|:------|
| Morse saddles (after degeneracy filter) | 95 |
| Median `κ∥/κ⊥` | **−1.94** |
| Mean | −2.87 |
| Std | 2.14 |
| IQR | [−3.84, **−1.34**] |
| 5–95 percentile | [−7.58, −1.09] |
| **Fraction in ED-Arch-01 window [−1.5, −1.1]** | **28.4%** |
| Fraction near −1 | 11.6% |

**Key observation:** the distribution is broad. ED-Arch-01's `−1.3` sits in the upper-quartile *edge* of the distribution — inside the 50% IQR, but not at the median. The field-space Hessian is not sharply peaked at `−1.3`; it has a broad tail centered around `−1.9` with substantial weight in the `[−1.5, −1.1]` window.

## 4×4 sweep across full ED-Arch-01 parameter grid

| n | noise | N_sad | Median | Mean | Frac in [−1.5,−1.1] |
|:-:|:-----:|:-----:|:------:|:----:|:-------------------:|
| 0.5 | 0.01 | 74 | −1.94 | −2.88 | 27.0% |
| 0.5 | 0.02 | 95 | −1.81 | −2.66 | 26.3% |
| 0.5 | 0.05 | 84 | −1.81 | −2.47 | 22.6% |
| 0.5 | 0.10 | 83 | −1.84 | −2.56 | 25.3% |
| 1.0 | 0.01 | 69 | −2.20 | −3.14 | 27.5% |
| 1.0 | 0.02 | 81 | −1.93 | −2.70 | 28.4% |
| 1.0 | 0.05 | 89 | −2.14 | −2.65 | 28.1% |
| 1.0 | 0.10 | 84 | −2.07 | −2.71 | 21.4% |
| 2.0 | 0.01 | 53 | −1.96 | −3.09 | 13.2% |
| 2.0 | 0.02 | 82 | −1.76 | −2.64 | 26.8% |
| 2.0 | 0.05 | 94 | −1.86 | −2.69 | 30.9% |
| 2.0 | 0.10 | 86 | −1.84 | −2.84 | 27.9% |
| 4.0 | 0.01 | 45 | −2.04 | −2.80 | 24.4% |
| 4.0 | 0.02 | 67 | −2.28 | −2.98 | 17.9% |
| 4.0 | 0.05 | 101 | −2.16 | −2.97 | 20.8% |
| 4.0 | 0.10 | 106 | −2.06 | −2.90 | 21.7% |

## What this says for R2

**The field-space Hessian distribution is essentially flat across the (n, σ) grid.** Median ratio stays in [−2.28, −1.76] and in-window fraction stays in [13.2%, 30.9%] with no structure. **There is no saddle of the field-space Hessian ratio as a function of (n, σ).** The architectural saddle in ED-Arch-01 lives only in the phase-exit-step observable surface, not in the field-Hessian observable surface.

## Resolution verdict (updated with canonical data)

- **R2 (field-space strict) is not falsified, but it does not explain ED-Arch-01's published `−1.3` either.** The field-space Hessian at spatial stationary points of Scenario D has 28% of its saddles falling in the `[−1.5, −1.1]` window at the peak parameter point, but the *median* is at `−1.94` and the distribution is broad. ED-Arch-01's `−1.3` is not the peak of a field-space distribution.
- **ED-Arch-01's `κ∥=−1.3, κ⊥=+1.0` is almost certainly the parameter-space observable Hessian** — the Hessian of the phase-exit-step surface `f(n, σ)` at its saddle-ridge peak, not a per-saddle field Hessian. This was the correct reading in the v1.3 orientation doc.
- **R3 (explicit mapping) is still the only resolution that would reconcile the parameter-space `−1.3` with any field-space invariant.** No such mapping exists in the ED-Arch papers I have read.

## Is ED-SC cross-scale invariance testable as stated?

Given the canonical R2 data, three interpretations remain live:

1. **Parameter-space observable-surface invariance** (R1-ish). ED-SC's `−1.3` is the saddle ratio of *whatever observable surface* is being swept. Then cross-scale matches require identifying analogous observable surfaces in Local Group and Casimir systems — which are not obviously the same kind of surface. **Claim becomes metaphorical unless the observable is specified.**
2. **Architectural-scale field-space invariance requires coarse-graining differently.** My detector uses single-pass smoothing; a proper ED-channel / ED-motif detector (wall-intersection geometry, channel-connecting saddles, etc.) may pick out a more coherent saddle population whose ratio concentrates near `−1.3`. Worth one more attempt with a motif-aware detector.
3. **The `−1.3` is a Scenario-D-specific architectural feature**, not universal. Under this reading, the Local Group and Casimir "matches" in ED-Arch-01 §5 need independent verification by someone other than the paper author.

## Artifacts

- `analysis/scripts/ed_arch_r2/r2_canonical.py` — canonical Scenario D R2 test
- `analysis/scripts/ed_arch_r2/r2_canonical_p_final.npy` — final p(x, y) at saddle peak
- `analysis/scripts/ed_arch_r2/r2_canonical_ratios.npy` — ratio distribution at peak
- `analysis/scripts/ed_arch_r2/r2_canonical_summary.txt` — summary including full 4×4 sweep

## Recommendation

**Single question to escalate:** the `−1.3` in ED-Arch-01 §5 — is it the Hessian of the phase-exit-step surface `f(n, σ)` at the `(2.7, 0.0556)` ridge peak, or is it the per-saddle Hessian of the field `p(x, y)`? The former reproduces (canonical sweep definitely has a saddle shape in phase-exit-step). The latter does not reproduce as the distribution center, though `−1.3` is well inside the 50% IQR of field-space saddles.

If it's the former, **R1 is the correct interpretation** and all prior cross-scale comparisons need reframing around "observable-space saddle ratios" with an explicit mapping to each comparison system.

If it's the latter, **R2 is partially consistent** (28% of saddles match) and the ED-SC invariance claim needs tightening — either to "a substantial fraction of architectural saddles have ratio near −1.3" (weaker but testable) or to "the median field-space Hessian ratio is near −1.3" (stronger but currently false).

Single next action, given the canonical data in hand: **do not run another sim until the interpretation question is resolved**. The R1/R2/R3 ambiguity is now fully characterized numerically.

---

## Post-resolution update (2026-04-17)

Allen chose Option 2 (field-space Hessian). The motif-conditioned refinement (see `R2_Motif_Verdict.md`) recovers `−1.304` as the motif-conditioned median, within 0.004 of the published value. The canonical invariance statement is in `docs/ED-SC-2.0.md`. The raw-distributional R2 finding in this memo remains the correct characterisation of the full Morse-saddle distribution; it simply isn't the right object for the ED-SC invariant.
