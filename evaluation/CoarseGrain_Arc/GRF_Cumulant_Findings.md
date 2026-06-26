# #5c — GRF Gaussianity Cumulant Test: Result (Qualified Mild Support)

**Evaluation result — the cheap could-say-no test from research-map #5c. Sim: `grf_cumulant_test.py` (reuses the certified Σ-rule substrate via `coarsegrain_test.ensemble_run`). Tests the S1-motif arc's GRF *regime hypothesis* (the coarse-grained participation field is Gaussian — assumed, not measured) by reading skewness, excess kurtosis, and a spatial Wick-factorization residual off the certified dynamical event-density field, swept across the coarse-graining scale R_cg. Result: a *qualified, mild* support — the field is weakly non-Gaussian at fine scale and the one-point cumulants Gaussianize under coarse-graining, but a small (~5–9%) spatial Wick residual persists. "Assumed → measured as an approximate, coarse-graining-window property," which is the todo's best-realistic outcome, and slightly more favorable than the committal/trapping prior expected. Not a clean "Gaussian"; not a refutation. Honest scope caveats below.**

> **CORRECTION (firming test, `grf_cumulant_deposit_test.py`, same day).** The "qualified mild support" below is **overturned.** Pressure-testing the surprise (deposit-density sweep) shows the base test's config (seedfrac = 0.04) sits **near a skew zero-crossing** — at sparse seeding (0.01) the field is **strongly skewed (+0.95)**, and at dense seeding (0.25) the excess kurtosis **grows under coarse-graining (0.12 → 0.77, anti-CLT)**. So the field is **non-Gaussian across deposit densities**, and coarse-graining does **not** Gaussianize it — **vindicating the committal/trapping prior**. The GRF regime hypothesis is **NOT robustly supported**; the base test's mildness was a config artifact. See §Firming below; read the §Result and §Verdict beneath it as the *superseded* base run. This is the **"honesty result"** the map (#5c) flagged as the more interesting outcome — it bounds the S1 motif sub-arc.

---

## What was tested

The literal r* GRF-linearization pipeline (`ED_Update_Rule` / `r2_grf_falsifier_tests`) is **not on disk** (never committed). The *meaningful* target is whether ED's **dynamical** field is Gaussian — and the certified Σ-rule substrate the CoarseGrain arc used **is** on disk (`event-density/Bits/simulator`). So: 10 dynamical realizations (uniform IC — the fair homogeneous start), late 40% of frames, the coarse-grained event-density field, fluctuations demeaned per frame, cumulants pooled across seeds+frames (large N) at each block size R_cg.

Diagnostics (all 0 for a Gaussian field): skewness; excess kurtosis (= normalized connected 4-pt at coincidence); Wick residual (does `⟨f²(x)f²(x+r)⟩` factor as `⟨f²⟩² + 2⟨f(x)f(x+r)⟩²`).

## Result

| R_cg | cells | skewness | excess kurtosis | Wick residual |
|---|---|---|---|---|
| 1 | 14641 | −0.262 | −0.193 | −0.089 |
| 2 | 3600 | −0.174 | −0.273 | −0.075 |
| 3 | 1600 | −0.152 | −0.220 | −0.051 |
| 4 | 900 | −0.147 | −0.163 | −0.049 |
| 6 | 400 | −0.121 | −0.068 | −0.041 |
| 8 | 225 | −0.129 | −0.022 | −0.066 |
| 11 | 121 | −0.089 | +0.086 | −0.089 |

- **One-point cumulants are weak and Gaussianize.** Skewness magnitude 0.26 → 0.09; excess kurtosis −0.19 → ~0 (crossing zero). Both trend toward Gaussian under coarse-graining — consistent with the CLT route (#5c route 1). The pooled sample is ~23k values even at the coarsest block, so this is a stable measurement, not small-N noise.
- **A small spatial Wick residual persists.** ~−5% to −9%, no clear trend to zero — the squared-field 4-point sits slightly *below* the Gaussian factorization throughout. A mild, persistent spatial non-Gaussianity.

## Honest verdict

**The coarse ED field is *approximately* Gaussian in the hydrodynamic window (one-point cumulants within ~0.1 in standardized units, Gaussianizing with R_cg), carrying a small persistent spatial-4-point residual.** This is a **qualified, mild support** for the GRF regime hypothesis — "assumed → measured as an approximate, coarse-graining-window property," exactly the todo's stated best-realistic outcome. It is *not* a clean "Gaussian" (the Wick residual doesn't vanish) and *not* a refutation (no heavy tails or strong skew).

**Flag the surprise (crank-rail).** The prior — from the CoarseGrain/Shadow arc (ED dynamics are committal/trapping, ballistic worldline deposits, sub-diffusive) — was *non-Gaussian or persistent*. The field came out *milder and more Gaussianizing* than that. When a result beats the prior, scrutinize it: the most likely reason the non-Gaussianity is weak is that the uniform-IC field is sparse-deposit-on-smooth-background (n_seed_frac=0.04), so most cells are near-Gaussian background and the filamentary deposits are a minority — the test may be under-weighting exactly the committal structure the prior was about.

## Scope caveats (what would firm it)

- **One IC, one field, one config.** Uniform IC is the fair homogeneous choice, but only one; the field is event-density ρ (the most direct dynamical scalar), not the r* pipeline's specific Ψ-construction (not on disk).
- **The committal structure may be under-represented** (sparse deposits on smooth background) — a deposit-dominated or denser-seed regime would test the filamentary, trapping structure directly; that's where non-Gaussianity, if it's real, should show.
- **Firming steps (cheap):** larger lattice (cleaner large-R_cg + more filament room); a denser-seed / deposit-focused regime; the actual r* Ψ field if the pipeline is ever reconstructed.

## Tier

**Assumed → measured-as-approximate-window-property (qualified, mild support), one config, with a small persistent spatial residual and a flagged surprise vs the committal prior.** A real first measurement that upgrades the GRF hypothesis from pure assumption to "approximately holds in the coarse window, measured" — not a clean confirmation, not a refutation. Could-say-no honored: it could have shown heavy tails (it didn't), and it could have shown clean Gaussian (it didn't either).

---

## Firming (the correcting run) — `grf_cumulant_deposit_test.py`

Pressure-test of the base surprise: sweep the **deposit density** (seed fraction) and also read the **deposited-increment** field (late − initial, isolating the committal structure from the static background). 5 seeds, uniform IC, fine (R=1) and coarse (R=4).

| seedfrac | tot R1 skew/exk | tot R4 skew/exk | inc R1 skew/exk | inc R4 skew/exk |
|---|---|---|---|---|
| 0.01 | **+0.95** / −0.33 | **+0.86** / +0.32 | **+1.08** / +0.15 | **+0.87** / +0.36 |
| 0.04 | −0.27 / −0.19 | −0.16 / −0.21 | −0.08 / −0.38 | −0.14 / −0.22 |
| 0.10 | −0.10 / +0.11 | −0.18 / +0.25 | −0.07 / 0.00 | −0.17 / +0.22 |
| 0.25 | −0.07 / +0.12 | −0.19 / **+0.77** | −0.06 / +0.06 | −0.19 / **+0.74** |

**What it shows:**
1. **Sparse (0.01) is strongly skewed** (+0.95 to +1.08) — isolated high-ρ filament deposits on a low background. Clearly non-Gaussian.
2. **seedfrac = 0.04 (the base test's exact config) sits near a skew zero-crossing** (+0.95 → −0.27 as density rises). The base test's "mild" cumulants were an artifact of landing there, not a generic property.
3. **Dense (0.25) is heavy-tailed, and the kurtosis GROWS under coarse-graining** (R1 +0.12 → R4 +0.77; same at 0.10: +0.11 → +0.25). This is **anti-CLT** — coarse-graining makes it *more* non-Gaussian, the signature of spatially-correlated filaments (block-averaging concentrates the tails rather than washing them out). Exactly the committal/trapping behaviour the CoarseGrain/Shadow arc measured ("locks configs, doesn't decorrelate").
4. **Increment ≈ total** — at developed times the field *is* mostly deposits, so isolating the increment doesn't change the picture.

## Corrected verdict

**The GRF regime hypothesis is NOT robustly supported.** ED's coarse field is **non-Gaussian across deposit densities** — strongly skewed when deposits are sparse (filaments), heavy-tailed when dense — and **coarse-graining does not Gaussianize it; the kurtosis grows (anti-CLT)**. The base test's "approximately Gaussian" was a config artifact (seedfrac = 0.04 near a skew zero-crossing). This **vindicates the committal/trapping prior** (ED doesn't mix/decorrelate, so the CLT route to Gaussianity is blocked — the *same wall* as PDE-emergence). It is the **"honesty result"** outcome #5c flagged: Gaussianity false as a robust property ⇒ **the S1 motif sub-arc's GRF assumption holds at best in a narrow accidental window and should be treated as a bounded, regime-conditional approximation, not a generic property.** Lesson logged: pressure-testing the surprise was load-bearing — the first run's favorable reading did not survive it.

---

*#5c cumulant test (`grf_cumulant_test.py`, certified Σ-substrate, 10 seeds, uniform IC). One-point cumulants weak and Gaussianizing under coarse-graining (skew 0.26→0.09, exkurt −0.19→~0); spatial Wick residual small but persistent (~−5 to −9%). Verdict: coarse field APPROXIMATELY Gaussian in the hydrodynamic window with a small persistent spatial residual — qualified mild support for the GRF regime hypothesis ("assumed → measured-approximate"), the todo's best-realistic outcome, slightly beating the committal/trapping prior. NOT clean-Gaussian, NOT refuted. Scrutiny flag: weak non-Gaussianity may be because uniform-IC field is sparse-deposit-on-smooth-background, under-weighting the committal structure; firm with a deposit-dominated regime + larger lattice + the actual Ψ. Scope: one IC/field/config; literal r* pipeline not on disk so tested the certified dynamical ρ field (the meaningful dynamical target). Crank-rail: reported the qualified reading, not the script's eager auto-verdict.*
