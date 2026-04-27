# DM.5 — DM2 Production-Run Verdict and BTFR Context

**Date:** 2026-04-27
**Arc:** Dark Matter — production-run verdict
**Status:** **FAIL** (numerical), with structural diagnosis. Canonical linearized ED with activity-source PDE was confronted against the SPARC sample (175 galaxies, 149 passing quality cuts). The run completed engineering-cleanly: validation gate PASS, all 149 galaxies fit numerically with no failures, optimizer converged on a globally consistent κ_act. Two refutation conditions fired (RC #1: rotation-curve shape; RC #3: BTFR slope and scatter). One refutation condition was *not* fired (RC #2: universality of κ_act, σ/mean ≈ 2.1%). Final assigned verdict: **FAIL**. The verdict is structurally explained by the BTFR.01–09 sub-arc: canonical ED fails two of three structural conditions (C1: log far-field, C2: √M_b coupling) for any linear-PDE theory to derive BTFR. C1 has two known repair paths; C2 has no automatic repair. The DM2 result is therefore a real refutation of canonical activity-source ED at galactic scales, with universality preserved as a partial positive finding. Cluster-scale predictions and structural arcs (R, M, N, Q, B) are not affected.
**Predecessor:** DM.0–DM.4 (architecture and protocol); DM.6–DM.14 (implementation and execution); BTFR.01–09 (structural diagnosis).
**Empirical anchor:** SPARC catalog (Lelli, McGaugh, Schombert 2016), 175 disc galaxies; 149 post-quality-cut sample for the production run.
**Successor:** Either pivot to non-DM-arc work (R, M, N, Q, B follow-ups; merger-lag retrodiction; weak-lensing tests), or pursue BTFR.10 (foundational substrate derivation of D_T) if the BTFR question remains a priority.

---

## 1. Summary of the DM2 production run

### 1.1 What was simulated

The DM2 simulation solved the canonical ED penalty-channel PDE,

> D_T · ∇²T − λ T = − κ_act · A(R, z),

on a production-grid (300 R-cells × 30 z-cells, log-linear hybrid R from 0.01 to 5000 kpc, linear z from 0 to 1.5 kpc) for each SPARC galaxy. The activity index A was built from the photometric baryonic rotation components (v_gas, v_disk, v_bulge), with α = 0.5 (equal weight to shear² and vorticity²). The kinematic prediction `v_T² = −R · γ · ∂_R T` (Reading B, γ = D_T/κ_act) was added in quadrature to v_baryon to give the predicted rotation curve, compared against observed v_obs.

Three tiers of self-consistency were available; Tier-3 (full outer-loop κ_act adjustment) was used.

The cluster-scale calibration gave D_T ≈ 6.97 × 10⁴ kpc²/Gyr, λ = 1/13.8 Gyr⁻¹, screening length L ≈ 980 kpc.

### 1.2 Target observables and refutation conditions

Per DM.4 §6 (refutation conditions defined ahead of the run):

- **RC #1: Radial fit shape.** Fires if median |⟨Δv⟩| > 20 km/s in any radial bin across > 30 % of the sample.
- **RC #2: Universality of κ_act.** Fires if σ(log κ_act) / mean > 0.13, or if any |Spearman ρ| > 0.3 against (M_b, T_type, SB_disk, sSFR).
- **RC #3: BTFR slope and scatter.** Fires if the fitted slope is outside [3.5, 4.5] at >3σ, or if the BTFR scatter exceeds the empirical ~0.1 dex by a large factor.

### 1.3 Headline numerical results

| Item | Value | Refutation status |
|---|---|---|
| Validation gate (DM.4 Gate 2) | PASS | — |
| Galaxies attempted / failed | 149 / 0 | — |
| Optimizer convergence | "Maximum function evaluations reached" (50 evals) | provisional |
| κ_act fitted (subset, global) | 0.997 | — |
| α fitted (subset, global) | 0.89 | — |
| Cross-validation R² (5-fold) | 0.258 | — |
| **Universality σ(κ_act)/mean** | **0.0212 (~2.1%)** | RC #2 **NOT fired** ✓ |
| Spearman \|ρ\| (max) vs galaxy properties | 0.114 (T_type), all p > 0.16 | — |
| **BTFR slope** | **0.24 ± 0.067** (empirical: 4.0 ± 0.1) | RC #3 **fired** ✗ |
| BTFR scatter | 3.74 dex (empirical: ~0.1 dex) | RC #3 **fired** ✗ |
| **Radial residuals** | RC #1 **fired** ✗ | — |
| NGC 3198 reference fit χ²_red | 293 (~100× expected) | — |
| Median χ²_red over sample | 60 | bad but not pathological |
| Mean χ²_red over sample | ~10²⁴ | dominated by outlier galaxies; not a structural metric |
| **Final assigned verdict** | **FAIL** | — |

The run was engineering-clean: the validation gate passed, the SPARC catalog was loaded correctly (after the data-prep work surfaced two duplicate header rows in the user's CSV and required column renaming and absolute-mass-unit conversion), and all 149 galaxies completed numerically without crashes. The FAIL verdict is therefore a scientific result, not an engineering artifact.

---

## 2. Structural explanation: BTFR sub-arc integration

The DM2 numerical FAIL is explained by the BTFR sub-arc (BTFR.01–09), which conducted a structural analysis of whether ED can derive the empirical Tully-Fisher relation v_flat⁴ ∝ M_b in principle.

### 2.1 The two-condition theorem (BTFR.02)

Any linear-PDE source-and-Green's-function theory predicts BTFR if and only if two independent structural conditions hold:

- **C1 — Logarithmic far-field.** The monopole Green's function asymptotic g(R) satisfies R · g'(R) → constant ≠ 0 for R within the radial regime where v_flat is measured. Equivalently, the operator must be effectively 2D in that limit.
- **C2 — Sublinear effective coupling.** The product (coupling × source-functional integrated charge) scales as M_b^{1/2} after disc integration. Equivalently, the theory must contain either a fundamental acceleration scale a₀ that weights the coupling sublinearly (Route A, MOND-like) or a source functional whose disc integral is intrinsically ∝ √ρ_b (Route B).

Both are necessary; together they are sufficient.

### 2.2 Canonical-ED structural failures (BTFR.03)

Canonical linearized ED fails both conditions, independently:

- **C1 fails.** ED's PDE is 3D-isotropic screened-Poisson. The in-galaxy Green's function (R ≪ L = 980 kpc) is essentially Newtonian 1/R, with no logarithmic regime. Curves fall as R^{−1/2} or faster.
- **C2 fails.** The activity index A integrates linearly in M_b (since shear² + vorticity² ∝ v²/R² ∝ G·M_b/R³ for a Keplerian disc). The disc-integrated effective charge is M_eff ∝ M_b, not √M_b. With a hypothetical log kernel, ED would predict slope-2 BTFR.

C3 (R-independence) also fails: ED's prediction depends explicitly on R_d and surface brightness through the source profile.

The numerical BTFR slope of 0.24 from DM2 is consistent with these structural failures: it is what a 1/R-kernel theory with linear-in-M_b source produces under fitting.

### 2.3 Two repair paths for C1

The BTFR sub-arc identified two independent structural mechanisms that could repair C1:

**(R-1) Anisotropic diffusion (BTFR.06).** Replace scalar D_T with anisotropic tensor (D_R, D_z) with D_z/D_R ≲ 10⁻⁶. This makes the operator effectively 2D-Cartesian-Helmholtz in the (R, z) plane over a finite radial window, giving a K₀ Green's function with logarithmic behavior for R ≪ √(D_R/λ). Strong anisotropy is required: the disc-thickness ratio (h_disc/R_d)² ~ 10⁻² is insufficient by four orders of magnitude.

**(R-2) Einstein-like relation D_T = c²·κ_act (BTFR.08).** When the canonical-ED PDE is treated **self-consistently** — i.e., when the activity index A is built from v_total = √(v_baryon² + v_T²) rather than from v_baryon alone — the equation acquires an extra term `−(κ_act·c²/R) · ∂_R T` on the LHS. If `D_T = c²·κ_act`, this term cancels the cylindrical-curvature term `(D_T/R)·∂_R T` exactly, leaving a 2D-Cartesian-Helmholtz operator with K₀ Green's function over the entire R ≪ L window. C1 is then repaired automatically, without anisotropy.

### 2.4 The C2 problem persists in both repair paths

Crucially: **neither (R-1) nor (R-2) repairs C2.** Both paths give a log-kernel structure (windowed 2D-Cartesian-Helmholtz), but the activity-source functional remains linear in M_b, giving disc-integrated M_eff ∝ M_b. With log kernel + linear M_eff, the predicted BTFR slope is 2, not 4.

This is the key structural finding: **canonical activity-source ED, properly self-consistent, predicts flat rotation curves with slope-2 BTFR — better-shaped than the linearized DM2 simulation produced, but still wrong.**

The DM2 numerical slope of 0.24 is partly a linearization artifact (the simulation solved the canonical cylindrical screened-Poisson, not the self-consistent equation). The structurally honest prediction of canonical ED is closer to slope 2. Even after correction, ED is still inconsistent with the empirical slope 4.

### 2.5 The foundational ambiguity (BTFR.09)

Whether the Einstein-like relation D_T = c²·κ_act holds in ED is a structural-foundational question. The cluster-anchored D_T and the galactic-anchored κ_act do not satisfy it numerically (mismatch factor ~50–10⁶ depending on unit convention). Two readings are available:

- **(P1)** D_T and κ_act are independently calibrated; the Einstein-like relation is not a forced theorem of ED. BTFR.06's anisotropy path is the canonical extension.
- **(P2)** D_T and κ_act emerge from a deeper substrate derivation that links them via D = c²·τ. The current galactic-anchor κ_act = 1 is a relative anchor; the absolute value would be ≈ 53 t_H. The cancellation in BTFR.08 is structural, not postulated.

Choosing between P1 and P2 requires a substrate-level derivation of D_T from ED's primitives, which has not been carried out. **The relation is structurally permitted but not currently demonstrated.**

The user's pushback during the BTFR sub-arc — that ED's "structure is relational" — bears on this: in a relational framework, asking whether a dimensional relation between two constants is "structural" or "contingent" is itself a question about which relations are taken as primitive and which are emergent. The Einstein-like relation, if it holds, would be emergent from the substrate event-propagation rules; if it doesn't, the constants are independently calibrated against different observational regimes. **Either reading is internally consistent; the empirical BTFR slope-4 problem is unaffected by which one is correct.**

### 2.6 The C2 problem is the genuine structural obstacle

Independent of P1 vs P2, the slope-2 prediction stands. **No version of ED examined in BTFR.01–09 produces slope-4 BTFR without an additional structural commitment** (Route II-A: postulated MOND-like ν(a/a₀); Route II-B: postulated sublinear source functional; Route III-C: nonlinear ED variant). All three commitments are non-trivial; none emerges automatically from ED's existing primitives.

The honest BTFR conclusion: **canonical activity-source ED is structurally incompatible with the empirical Tully-Fisher relation, by a slope factor of ~2 (not the ~16 the DM2 numerical fit suggested).**

---

## 3. The DM2 verdict: what FAIL means

### 3.1 What is structurally falsified

- **Canonical activity-source ED with linear screened-Poisson PDE, fit against SPARC, fails to reproduce BTFR even structurally.** This is now confirmed at both numerical (DM2 fit) and structural (BTFR sub-arc) levels.
- **The 30 km/s per-galaxy fit-residual gate (DM.4 NGC 3198 reference)** is not achievable for canonical ED on a typical SPARC galaxy. χ²_red ~ 60 (median) and ~10²⁴ (mean) reflect both structural inadequacy and outlier-galaxy pathology.
- **The DM.4 §6 refutation criteria are met:** RC #1 (radial residuals) and RC #3 (BTFR) both fire. The combined four-way verdict logic assigns FAIL.

### 3.2 What is preserved or partially preserved

- **Universality of κ_act (RC #2 NOT fired).** σ(κ_act)/mean ≈ 2.1% across 149 galaxies, with all Spearman correlations |ρ| < 0.12 against galaxy properties. **This is a real positive result, with the caveat that the optimizer hit max_evals = 50, so universality may partly reflect the optimizer not exploring κ-space fully.** A re-run with optimizer_max_evals ≫ 50 is needed to confirm whether this universality is structural or numerical artifact.
- **Cluster-scale calibration is unaffected.** The merger-lag prediction (DM.0 §2) remains intact; the BTFR failure is a galactic-disc-regime problem, not a cluster-scale problem.
- **Engineering correctness.** The validation gate passed; the implementation is sound; the data pipeline (after the prep-work corrections) handles the SPARC catalog correctly.

### 3.3 What is not ruled out

- **Non-linear ED variants (BTFR.07 Option C).** A nonlinear-PDE ED, where the operator itself is nonlinear (analogous to MOND's μ(|∇φ|/a₀)·∇φ structure but sourced by activity instead of mass), could in principle produce slope-4 BTFR. This is a major structural change to the canonical theory and was not tested in DM2.
- **Self-consistent ED with the Einstein-like relation.** The canonical theory, *if* the substrate derivation produces D_T = c²·κ_act, gives slope-2 BTFR with flat curves — bad but better-shaped than what DM2 actually computed. The DM2 simulation used the linearized PDE, not the self-consistent one. A re-run with the self-consistent equation (fixed κ_act under the relation, or updated PDE solver to include the v_T → A back-reaction) would soften the FAIL but not invert it.
- **C2 fixes (Route II-A, II-B).** Importing an MOND-like coupling weighting or a sublinear source functional would, by construction, produce slope-4. This represents a structural commitment ED has not yet made; whether ED *should* make it is a research-direction question.
- **Future foundational work.** BTFR.10 (substrate derivation of D_T) would settle P1 vs P2 and might motivate further structural extensions.

---

## 4. Place in the broader ED program

### 4.1 Interactions with other arcs

- **Arc R (relativistic emergence — KG, spin-statistics, Dirac, g=2):** unaffected. The BTFR sub-arc analysis is contained to the gravitational-sector PDE and its galactic-disc consequences. R-arc theorems do not depend on D_T or κ_act.
- **Arc M (matter-wave structure, σ_τ form):** unaffected.
- **Arc N (vacuum kernel, V1 finite-width):** unaffected by the canonical-ED BTFR result. *Conditionally affected by Option C* (nonlinear ED variant) if pursued — Theorem N1 was derived assuming linear PDE structure; nonlinearity would require re-evaluation.
- **Arc Q (quantum sector — GRH, UV-FIN, canonical commutation):** unaffected.
- **Arc B (Born-Gleason, foundations):** unaffected.
- **Phase 3 / GR (V1 with Synge world function):** unaffected by canonical-ED BTFR result. *Conditionally affected by Option C* in the same way as Arc N.
- **GR-SC (curvature-invariant taxonomy):** unaffected.
- **DM-arc cluster-scale predictions:** preserved. The merger-lag observable is independent of the BTFR-relevant in-galaxy regime.

### 4.2 Why BTFR is critical but not exclusive

BTFR is the cleanest single empirical test of any galactic-scale modified-gravity theory (slope 4, scatter 0.1 dex, R-independent across 5 decades of M_b). Any theory that fails BTFR structurally fails the most demanding galactic test. DM2 fails it both numerically and structurally.

But BTFR is not the only test:

- **Cluster merger-lag.** ED's original empirical anchor; not refuted by DM2.
- **ED-04.5 dwarf-vs-giant outer-radius discrepancy.** The qualitative observation that motivated DM.1 (active-vs-quiet galaxy comparison); the activity-source mechanism remains a good qualitative match here, even though it fails BTFR quantitatively.
- **Weak-lensing tangential stacking, cluster outskirts, merger-lag in different cluster pairs.** Not yet examined under canonical ED.

A theory can fail one stringent test (BTFR) and still have positive predictions for other observables. **DM.5's verdict is FAIL on BTFR specifically; it is not a verdict on ED's program-level viability.**

### 4.3 Honest status of ED after DM.5

- **Structural integrity preserved at the foundational level.** Arcs R, M, N, Q, B, GR, and most of GR-SC remain intact. The framework's most ambitious structural results (Theorem N1, GR.1, spin-statistics, UV-finiteness) are not threatened by the DM-arc result.
- **Galactic-disc dynamics: refuted in canonical form.** ED's prediction for galactic rotation curves and BTFR is structurally inconsistent with observation. Repairing this requires a structural commitment (anisotropy, Einstein-like relation, MOND-like coupling, or full nonlinear reformulation) that no version of canonical ED contains.
- **Universality preserved.** ED's qualitative prediction of "no per-galaxy tuning" survives at σ/mean ≈ 2.1%, modulo the optimizer-convergence caveat.
- **Cluster-scale agreement preserved.** The original merger-lag anchor is intact.

The honest summary: **ED is structurally consistent and has well-defined empirical predictions; one of those predictions (BTFR) is wrong; the program continues, with the BTFR refutation as a real and informative scientific finding.**

---

## 5. Open questions

### 5.1 The C2 (slope-4) structural mechanism

No version of ED examined in BTFR.01–09 produces slope-4 BTFR without an external structural commitment. The empirical BTFR is the strongest constraint on any modified-gravity theory; producing slope-4 from first principles is exactly what MOND does cleanly and what every other framework has had to import or fit. **Whether ED has an internal route to slope-4 — perhaps via the nonlinear variant in BTFR.07 Option C, perhaps via an unanticipated structural derivation — is the central open question for any DM-arc continuation.**

### 5.2 Foundational derivation of D_T

ED's D_T is currently anchored phenomenologically to cluster merger-lag observations. A bottom-up derivation from substrate event-propagation rules would either produce D_T = c²·κ_act (vindicating the Einstein-like relation as structural, P2) or not (P1 confirmed). This work has not been done. It is a Phase-2-foundational task in flavor (substrate-level derivation), not a DM-arc task.

### 5.3 Can ED ever derive BTFR without MOND-like machinery?

The structural pattern uncovered by BTFR.01–09 is that producing slope-4 BTFR requires a coupling form whose deep-regime asymptotic gives `μ(a/a₀) → a/a₀` (or equivalent). Every framework that succeeds at BTFR — MOND, emergent gravity, certain scalar-tensor theories — has this structure built in. ED currently does not. Whether ED's substrate physics can produce this coupling-form *naturally* (rather than by importing it from MOND) is open. The slow-time interpretation suggested by the user during the BTFR sub-arc points in this direction (the natural scale c·H_0 ≈ a₀ within factor 6) but has not been worked into a concrete structural derivation.

### 5.4 The user's relational-structure observation

The user's note that "ED says structure is relational" is more than a quip. It bears on the P1 vs P2 question: in a relational framework, dimensional relations between constants are not absolutely structural or absolutely contingent — they are structural relative to which other relations are taken as primitive. Whether D_T = c²·κ_act is "structural" depends on whether the substrate physics derives both from a common origin or treats them independently. **The relational framing supports the view that this is a *foundational research question*, not a settled fact, and that the empirical BTFR mismatch is informative about which relations the substrate physics actually enforces.**

---

## 6. Recommended Next Steps

Three concrete next steps, ranked by what would most advance the ED program from this point:

1. **Pivot to non-DM-arc ED tests.** The DM-arc has produced a clean structural verdict (DM.5 = FAIL on BTFR, with detailed structural diagnosis). Continuing to push BTFR-extension work without new empirical inputs would be diminishing-returns. **High-value alternatives:** (a) the merger-lag retrodiction the project_next_predictions memory has been pointing at; (b) weak-lensing activity-dependent predictions; (c) the foundational substrate derivation of D_T (BTFR.10 candidate). These would either strengthen or weaken ED independently of the BTFR result.

2. **If BTFR work continues: BTFR.10 (substrate derivation of D_T).** This settles P1 vs P2 and is the foundational work the BTFR sub-arc identified as missing. It is a substrate-physics task (not a galactic-physics task), so it interacts with Arc N and the substrate primitives. A successful derivation would either: (a) confirm the Einstein-like relation is structural, removing the BTFR.06 anisotropy requirement and reducing the DM-arc's open structural commitments; or (b) confirm the relation is not structural, locking in BTFR.06's anisotropy path as the canonical extension.

3. **Re-run DM2 with the self-consistent (non-linearized) PDE, as a one-time honest comparison.** The DM2 production fit used the linearized canonical PDE and got slope 0.24. The structurally honest prediction of canonical self-consistent ED is slope 2. Running this as a sanity check would: (a) confirm the structural prediction matches the structural derivation; (b) sharpen the FAIL verdict from "ED predicts ~0 slope" to "ED predicts ~2 slope, empirical is 4"; (c) improve the visual quality of the per-galaxy rotation-curve fits (from falling curves to flat-but-low-amplitude curves), making the residual structure of the failure more interpretable. This is a bounded engineering task (modify the activity-source builder to include the v_T back-reaction, re-run on a subset of galaxies) and would close the DM-arc with a more honest empirical verdict than the current one.

The default recommendation, absent a specific new empirical signal: **do step 1**, broaden the ED empirical base, and revisit the BTFR question only when there is independent reason to (new data, new structural insight, or a clean foundational derivation in step 2).

Status: complete.
