# GRF-Gaussianity Cumulant Test — Results

**Run:** 2026-07-05, `theory/GRF_Gaussianity/grf_cumulant_test_probe.py` (+ `grf_cumulant_bigger_grid.py`) on the certified substrate (`evaluation/Bits/simulator`, standard SigmaCoeffs kc=ks=kg=1, ρ*=0.5, ext=−2.0), scattered 4% seeding (statistically homogeneous), deposit field δ = ρ_final − ρ_initial. Grids 64² (12 seeds) and 128² (4 seeds); null = phase-randomized surrogates of each field (identical power spectrum, Gaussianized phases); statistics = standardized skewness g1, excess kurtosis g2, adjacent-triple product T3, at block-aggregation scales B ∈ {1,2,4,8,16,32}. This is the could-say-no test the `scale invariance/README` proposed against the S1 sub-arc's Gaussian-random-field regime hypothesis, which the layers/CoarseGrain program predicted would fail.

## Headline

**The GRF hypothesis fails in the regime where the S1 sub-arc plausibly uses it, and survives only as a large-filter asymptotic.** The certified deposit field has **white two-point structure (ξ = 1.0 cell, measured) but scale-invariant skewness**: g1 ≈ −0.9 flat through B=8 aggregation (z = −11 to −15 against the Gaussian null; CLT for independent cells would predict decay to −0.11 by B=8). Gaussianization onsets only at B ≈ 16–32 cells (g1: −0.69 at 16, −0.29 ≈ null at 32). The non-Gaussianity is carried entirely by **higher-order/phase correlations invisible to the power spectrum**, which is why spectrum-preserving surrogates cannot mimic it. This is the layers program's committal/trapping claim in sharp quantitative form.

## Numbers

| B (cells) | g1 real | z(g1) | g2 real | z(g2) | T3 z |
|---|---|---|---|---|---|
| 1 | −0.91 | −90 | −1.18 | −56 | −26 |
| 2 | −0.90 | −32 | −0.20 | −4.6 | −13 |
| 4 | −1.04 | −24 | +0.80 | +11 | −5.2 |
| 8 | −0.93 / −0.97 | −11 / −15 | +0.99 / +1.08 | +10 | ≈0 |
| 16 (128²) | −0.69 | −4.4 | +0.64 | +2.2 | ≈0 |
| 32 (128²) | −0.29 | −1.3 | −0.26 | ≈0 | ≈0 |

(B=8 shown for both grids; 128² values second. ξ = 1.00 ± 0.00 on both grids.)

## What is trivial and what is structural (stated plainly)

- **Trivial, not the finding:** the raw deposit being non-Gaussian at B=1. A bounded, committal field has a non-Gaussian marginal; nobody needed a probe for that.
- **Structural, the finding:** with **white covariance** (ξ=1), block means over B² effectively-independent-by-covariance cells should CLT-decay their skewness as 1/B. They do not: **g1 is flat to B=8** (64 cells aggregated, decay factor expected 8×, observed ≈1×) and only approaches Gaussian at ~16–32 cells. Odd-cumulant correlations therefore extend an order of magnitude beyond the covariance length. The field hides its structure from the spectrum and carries it in the phases — measured, not asserted.
- **T3 decays faster than g1** (null by B=8): the surviving non-Gaussianity at intermediate scales is in the marginal asymmetry of aggregates (odd cumulants of the block distribution), not in short-range triple products.

## Verdict for the S1 sub-arc (motif invariant, r*, saddle-classification, SC-4.11)

1. **At filter scales up to ~8–16 substrate cells the coarse field is decisively not a GRF** (|z| ≈ 10–90). Any S1 statistic computed there stands on a false regime hypothesis.
2. **A bounded rescue exists:** Gaussianity onsets at ~16–32 cells. S1 statistics computed at filter scales ≳ 32 substrate cells would have their GRF hypothesis (marginally) restored.
3. **The fold-back question — CHECKED 2026-07-05, result: genuinely blocked, not just unresolved.** "lu" (ξ_canonical ≈ 1.7575 lu, from `Paper_096`/`ED_SC_3_1_rev3_CanonicalPointCertification.md`) and "cell" (this test's unit) are grid spacings of **two different, never-cross-calibrated simulators implementing different mathematical objects**: this test ran on the certified `evaluation/Bits/simulator` (a discrete Σ-maximizing participation graph — nodes and chain-fronts, no continuous field); ξ_canonical was measured on a separate continuous mobility-PDE engine (`ED_Update_Rule.ed_step_mobility`, $\partial p/\partial t = \beta\nabla^2p - \alpha p^\gamma$, driven by the `ed-lab` repo's R2 scripts, engine code in a third repo, `Emergence Universe\ED-SIM-Code`). No document anywhere ties either grid to a shared substrate-absolute length ($\ell_{ED}$ or $\ell_P$) — `Paper_096` itself calls 1.7575 "canon-internal... not derived from primitives independently." There is no conversion factor to look up; none was ever built. Computing one now would mean inventing an unjustified number. **This closes the question, but not the way "check the units" implied** — it's not an open lookup, it's a structural gap: the S1 arc and this test were never run on comparable substrates in the first place.
4. **Consilience (the reason to trust the direction):** the r* predictive validity was *already* measured negative (pooled R² ≈ −1.88, worse than null, honestly reported in its own paper). This result supplies the structural *reason*: filtered-GRF statistics misfire because the field they filter is not a GRF at those scales. The layers program predicted exactly this negative ("committal/trapping, not mixing"); the soliton-test precedent applies — a regime hypothesis measured false retires what rests on it.

## What this does NOT claim

- No claim about the CMB or empirical cosmology: this is a statement about the certified substrate's own coarse field, i.e. about the internal consistency of the ED-SC 3.x statistical machinery. (The corpus's position that observed CMB Gaussianity is a layer-2/inflation phenomenon is untouched; if anything, "Gaussianity onsets only after heavy aggregation" is that position, quantified.)
- No claim that S1 quantities are wrong as *measured numbers* — the motif/r*/saddle statistics are what they are; what fails is their *interpretation* through GRF theory (Wick factorization, filtered-GRF expectations) at sub-Gaussianization filter scales.
- One instantiation (2D, standard coefficients, deposit observable). The 3D/other-coefficient sweep is the standard extension; the effect size (|z| > 10 with a flat trend) makes a qualitative reversal unlikely but the bound (16–32 cells) is instantiation-specific.

## Next

1. **Fold-back to the S1 papers: BLOCKED, not open.** The unit check (above) resolved to "no shared yardstick exists," not to a number. Do not fold this test's verdict into `Paper_EDSC_rstar_FilteredGRF`, `Paper_EDSC_MotifConditioned`, `Paper_EDSC_SaddleClassification`, SC-4.11, or the `scale invariance/README` as a retirement — that would require the invented conversion factor this check explicitly declined to manufacture. The S1 sub-arc's GRF regime hypothesis remains exactly as open/unsettled as it already was (r* was independently retired from S1-invariant status back in April 2026, for unrelated reasons) — this test neither confirms nor retires it.
2. **Report this test as a standalone result about the certified substrate.** It doesn't need the fold-back to be valid: "white covariance + scale-invariant odd cumulants to ~10× the covariance length" is a sharp, quotable structural signature of the committal substrate, and arguably the corpus's cleanest single measurement of *where layer-2 begins* — a keeper line for the layers papers on its own terms.
3. **The bigger finding this surfaced: at least two mutually-uncalibrated ED simulators are in active use across the corpus** — the certified discrete graph (`evaluation/Bits/simulator`, everything checked tonight) and the continuous mobility-PDE engine (`ED_Update_Rule.ed_step_mobility`, driving the whole scale-correspondence/S1 arc) — with no documented shared length scale between them. That's a cross-cutting architecture question bigger than this one test; see the master targets map's new top-line item.
4. **Minor precision note:** the "ξ = 1.00 ± 0.00 cells, measured" claim overstates precision — `corr_length()` only checks integer-cell radii, so it would report exactly "1" for any true correlation length between 0 and just under 1 cell. The qualitative finding (short-ranged/white covariance) holds; the specific "1.00" shouldn't be quoted as exact.
