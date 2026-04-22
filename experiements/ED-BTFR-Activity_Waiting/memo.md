# ED Pre-BIG-SPARC Combined Test of the Activity-Dependent BTFR Residual

**Status:** Combined analysis changes the sign of the pre-BIG-SPARC headline from `+0.263 ED-supporting` to `opposite of the ED prediction`, once the residual is interpreted in the direction ED actually predicts. Magnitude is modest (|ρ_partial| ≈ 0.18–0.32); a definitive test still awaits BIG-SPARC.
**Date:** 2026-04-17
**Script:** `analysis/scripts/btfr_activity_union.py`
**Data products:** `data/ED-BTFR-Activity/`
**Context:** `data/ED-Data-12-Galactic-Activity/` through `data/ED-Data-17-z0MGS-Names/`, `data/ED-Data-18-BIG-SPARC/` (awaiting release).

---

## Addendum (2026-04-17): Updated Interpretation After ED-XX

This memo analyzes the correlation between **galaxy-intrinsic** activity (log SFR, log sSFR, T-type) and BTFR residuals. After the ED-XX environment-sourcing revision (April 2026), the correct ED prediction is no longer galaxy-level `ρ(sSFR, Δ)` but **environmental-level** `ρ(S_env, V_∞)`, where `S_env` is collective group/filament activity and `V_∞` is the asymptotic velocity set by the megaparsec-scale temporal-tension field. ED-Sim-01's 3D simulation programme showed that no compact galactic source can sustain a flat temporal-tension field — the `1/r` Green's-function dilution overwhelms the exponential decay regardless of parameter choices — so the galaxy-level prediction this memo was designed to test has been superseded. The null result reported here therefore **remains correct for the variable tested but does not test the updated ED prediction**. A proper test requires cross-matching SPARC (or BIG-SPARC) galaxies with group/filament catalogs and evaluating environmental coherence in asymptotic velocities.

The **methodology correction in §2 (below) is independent of the interpretive shift**: the sign-flip identity `Δ_M = −B·Δ_V` at fixed M, and the finding that modules ED-Data-12..17 computed residuals in M-space (which inverts ED's directional prediction stated naturally in V-space), hold regardless of whether the source is the galaxy or the environment. Future work on BTFR residuals — including on BIG-SPARC — should still use V-on-M fits and mass-controlled partial correlations.

For the revised sourcing model, see [`docs/ED-Orientation.md`](../../docs/ED-Orientation.md) §6.

---

## 1. Executive Summary

Combining the five usable SPARC × SFR cross-match modules (ED-Data-12, 13, 14, 16, 17) into a single union-sample analysis with one consistent BTFR fit and one SFR value per galaxy, the ED-unique activity-dependence prediction — that at fixed baryonic mass, galaxies with higher SFR rotate faster because the out-of-equilibrium participation field inflates V — is **not detected**. On the Q = 1 primary sample (n = 73), the mass-controlled partial Spearman correlation between rotation-velocity residual and log SFR is

> **ρ(Δ_V, log SFR | log M_b) = −0.18, p ≈ 0.13.**

On module 13's larger Q = all sample (n = 116) with module 13's own SFR values, the same test gives **ρ = −0.32, p = 0.0005** — statistically significant but in the **opposite direction** from ED's prediction.

The previously-reported "positive signal in every module" (e.g. module 13's ρ = +0.263 at p = 0.004) is **reproduced exactly**, but when translated into the residual-direction that ED actually predicts, it flips sign. This is an algebraic identity, not a disagreement between tests.

## 2. The Sign-Flip Identity (the main methodology point)

The BTFR can be fit two ways and residuals computed two ways:

- **V-on-M fit** (`log V = a + b · log M`): residual `Δ_V = log V_obs − log V_pred(M_obs)`. "Is V higher than expected for this mass?"
- **M-on-V fit** (`log M = A + B · log V`, B ≈ 3.72): residual `Δ_M = log M_obs − log M_pred(V_obs)`. "Is M higher than expected for this V?"

At fixed M, these residuals are *algebraically* related by

$$\Delta_M = -B \cdot \Delta_V \qquad \text{(at fixed }M\text{)}.$$

So the partial correlations `ρ(Δ_V, X | M)` and `ρ(Δ_M, X | M)` for any third variable X must be equal in magnitude and opposite in sign. The pipeline verifies this numerically: on the primary union, the two partials are −0.180 and +0.184, summing to +0.004 ≈ 0.

The consequence: the two convention choices do *not* test different hypotheses. They test the same hypothesis with opposite sign conventions. To decide whether the observation is consistent with ED, you need to know which *sign* of which residual ED actually predicts.

## 3. What ED Actually Predicts

From ED-Data-Galaxy-11, §4.3 and §9.1: the participation field amplitude sources `V_temp^4 = G · a_ED · M_b`, and "higher sSFR → higher V_temp (more activity → stronger temporal tension)."

At fixed baryonic mass, therefore:

- ED predicts **V is higher** for active galaxies.
- Equivalently, at fixed V, ED predicts **M is lower** for active galaxies (less mass is needed to reach that V because participation contributes).

Translated into residual signs:

| Convention | ED-predicted sign | ED-predicted `ρ(Δ, log SFR | M)` |
|---|---|---|
| V-on-M, Δ_V = V_obs − V_pred(M) | Δ_V > 0 for active | **positive** |
| M-on-V, Δ_M = M_obs − M_pred(V) | Δ_M < 0 for active | **negative** |

## 4. What We Observe

### 4.1 Union primary (Q = 1, n = 73, SFR precedence z0MGS > calibrated > literature)

| Test | V-on-M (Δ_V) | M-on-V (Δ_M) |
|---|---:|---:|
| Raw Spearman ρ(Δ, log SFR) | −0.096 (p = 0.42) | **+0.230 (p = 0.050)** |
| Partial ρ(Δ, log SFR | log M) | **−0.180** (p = 0.13) | **+0.184** (p = 0.12) |
| Sign-flip identity check (sum) | — | +0.004 ≈ 0 ✓ |

Mass trend in residuals (should be ≈ 0 if fit is properly de-trended):
- V-on-M: ρ(log M, Δ) = −0.02 ✓ clean
- M-on-V: ρ(log M, Δ) = +0.15 (by construction; Δ_M carries mass information)

Main-sequence correlation in the sample: **ρ(log SFR, log M_b) = +0.91** — SFR and M are almost colinear in this sample, so mass control is essential.

### 4.2 Module 13 exact reproduction (n = 116, Q = all, calibrated SFR)

| Test | V-on-M (Δ_V) | M-on-V (Δ_M) |
|---|---:|---:|
| Raw Spearman | −0.12 (p = 0.21) | **+0.263 (p = 0.004)** ← the published signal |
| Partial ρ(·|M_b) | **−0.32** (p = 0.0005) | **+0.32** (p = 0.0004) |

Same pattern, stronger because of the larger sample.

### 4.3 Per-module robustness (Q = 1)

Every individual proxy, when fit V-on-M with proper mass control, gives a negative partial correlation:

- z0MGS-only (n = 25): ρ = −0.10 (p = 0.63, underpowered)
- calibrated only (n = 73): ρ = −0.08 (p = 0.51)
- literature only (n = 50): ρ = −0.15 (p = 0.31)
- T-type ordinal (n = 73): ρ = −0.12 (p = 0.30)

No proxy choice or sample cut recovers the ED-predicted positive V-residual correlation.

## 5. Reconciling the Two Narratives

The repo's pre-existing modules consistently reported a **positive** ρ between `Δ_M` and log SFR, and read this as support for ED's activity prediction. The measurements are reproduced here exactly — they are not wrong. What is wrong is the sign-interpretation: a positive `Δ_M` at fixed V means the galaxy has *more* baryonic mass than predicted from its V, which is equivalent to saying its V is *lower* than predicted from its mass. ED predicts the opposite ("higher V for given M").

Two non-mutually-exclusive reasons the positive `Δ_M`–SFR correlation can exist without ED:

1. **Main-sequence + gas-mass confound.** Active galaxies carry more HI (which enters M_baryon). At fixed V, an HI-rich active galaxy has more M_b. This is a baryon accounting effect, not a velocity-inflation effect.
2. **Residual main-sequence leakage.** With ρ(log SFR, log M_b) = +0.91 in this sample, raw Spearman on un-mass-controlled residuals is dominated by the SFR–M correlation. The module 13 README already noted that ρ(Δ_M, log sSFR) = +0.10 (not significant), consistent with the signal being largely mass-driven.

Neither explanation involves the participation field. Both are consistent with the observed `Δ_M > 0` for active galaxies at fixed V, *and* with the observed `Δ_V < 0` for active galaxies at fixed M.

## 6. Honest Status of the ED Activity Prediction

> At SPARC sample size (n = 73–116), the ED-predicted positive correlation between rotation-velocity residual and SFR at fixed baryonic mass is **not detected**. The mass-controlled partial Spearman is −0.18 to −0.32 (depending on sample size and Q cut), which is in the opposite direction from the ED prediction. At p ≈ 0.0005 on the n = 116 sample this is formally significant, though the partial-correlation machinery interacts with the very strong SFR–M main-sequence (ρ = +0.91) and should be treated cautiously.

A definitive test still requires BIG-SPARC (expected n ≈ 3000–4000 when released, arXiv:2411.13329). With that sample size and uniform z0MGS GALEX+WISE SFR, ρ_partial ≈ 0.05 can be detected at > 3σ. The current pre-BIG-SPARC combined analysis is compatible with either a small null or a small negative correlation; it is not compatible with the ED-predicted positive signal at p < 0.05 in the V-residual direction.

## 7. What This Changes in the Repo

- ED-Data-12 through ED-Data-17 each reported a positive `Δ_M`-SFR correlation as support for ED's activity prediction. The **measurements are correct and reproducible**. The **sign-interpretation relative to ED is incorrect** — the observed sign is actually opposite to what ED predicts from V-inflation.
- The "signal is positive in every module" pattern reflects the main-sequence coupling between SFR and M plus the sign convention of `Δ_M`; it is not an independent confirmation of the ED-unique activity signature.
- BIG-SPARC remains the correct next step. The union pipeline here is ready to re-run on BIG-SPARC with minimal changes (swap the input CSV, keep the Q = 1 filter and V-on-M fit).

## 8. Caveats

1. **Small sample.** n = 73 (Q=1) and n = 116 (Q=all) are both under the size at which partial correlations in the presence of strong main-sequence colinearity give narrow CIs. The Q=1 partial is not significant at 5%; only the Q=all version is. BIG-SPARC closes this.
2. **Partial Spearman with high colinearity.** When SFR–M correlation is +0.91, partial correlation removes most of the signal variance. Residual statistical power is correspondingly lower. The magnitude estimate is robust; the significance estimate is conservative.
3. **No new data.** This is a re-analysis of existing modules with a unified methodology. The conclusions rest on the already-published modules' numbers; no new cross-matches were performed.
4. **The correct ED test may still be elsewhere.** If the "participation field" predicts some signature other than V-inflation at fixed M (e.g. tangential-velocity effects, halo-shape changes, or something at higher-order in sSFR), that would require a different analysis. This memo tests only the velocity-at-fixed-mass prediction as stated in Galaxy-11.

---

*All raw numbers, robustness checks, and plots are preserved under `data/ED-BTFR-Activity/`. The sign-flip identity is verified numerically in the script's console output.*
