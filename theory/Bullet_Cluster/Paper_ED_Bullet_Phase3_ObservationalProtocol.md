# Testing the Offset–Velocity Law: A Phase-3 Observational Protocol for Merging Clusters

**Author:** Allen Proxmire
**Arc:** Bullet_Arc (ED-Bullet-01) — Phase-3 (observational)
**Status:** Protocol / experiment-ready sharpening of the Phase-2 synthesis (`Paper_ED_Bullet_TopologicalDefect`)
**Purpose:** Turn the offset–velocity law from a stated prediction into a test an observer can actually run: the exact observable, the real dataset, the discriminating statistic, the sample-size reality, and the honest confounds.

---

## 0. What this document is

Phase-2 (`Paper_ED_Bullet_TopologicalDefect`, §6–7) ended with a prediction and a one-paragraph sketch of the test: "measure the lensing–gas offset and the merger velocity for many clusters and plot one against the other." That is the right idea and not yet a protocol. This document supplies the missing operational layer, so the claim reads as *an experimentalist could run this*, not *someone should look into this*. It changes no physics; it makes the Phase-2 prediction executable and states plainly where it is hard.

The one-line prediction under test: **across the population of merging clusters, the mass–gas offset as a function of merger velocity traces a specific shape — flat below a threshold, a near-linear rise above it, a ceiling at the freeze-out scale — with a *sharp knee* at the turn-on that neither ΛCDM (scatter) nor MOND-EFE (smooth roll-off) produces.**

## 1. The one robustness fact that sets the whole test design

From Phase-2 §7.1: the two open substrate ingredients (the super-linear shock response and the two-timescale core/dressing structure) float the **location** of the knee but not its **existence**. Concretely, v_crit sits somewhere in **~15 to ~1500 km/s** depending on how those resolve, and the ceiling height ξ_KZ moves with them, but the three-regime *shape* — knee, line, ceiling — survives every resolution.

This dictates the test's priorities, and it is the single most important design consequence:

- **Do not test the knee's predicted value.** The theory does not yet pin v_crit tightly, so a test that asks "is the knee at 150 km/s?" is testing an open ingredient, not the mechanism.
- **Test the knee's existence and character.** The ED-distinctive, ingredient-robust claims are (F1) *there is a knee at all*, and (F2) *the turn-on is sharp, not gradual*. These are what separate ED from its rivals regardless of how the open ingredients resolve.
- **Rank F2 highest.** Sharpness is the cleanest discriminator: a topological (all-or-nothing) mechanism gives a step; MOND-EFE gives a ramp; ΛCDM gives no clean transition. F2 is where the three columns most differ and where the answer is least contaminated by the open theory.

## 2. The observable, defined so it cannot be run wrong

**The offset (the ED-relevant one, and a common mis-pairing to avoid).** ED's Δr_offset is the **mass–gas** offset: the projected separation between the total-mass peak (weak-lensing convergence peak) and the hot-gas peak (X-ray surface-brightness peak, Chandra/XMM). Two cautions:

1. This is *not* the DM–galaxy offset that the self-interacting-dark-matter literature reports (Harvey et al. 2015; Wittman et al. 2018). Those papers measure whether the lensing mass *lags the galaxies* to constrain a DM self-interaction cross-section. That is a different quantity built from the same maps. The ED test needs mass-peak minus gas-peak, which is the quantity that *defines* a dissociative merger and is recoverable from the same lensing + X-ray data.
2. Report both the two-defect separation (peak-to-peak, the Bullet's ~700 kpc) and the per-subcluster gas-lag (mass-peak minus its own gas, the Bullet's ~110 kpc). Phase-2 §5.5 shows both come from the same advection scale; the protocol should track the gas-lag as the primary Δr because it is defined per subcluster and less sensitive to how many peaks a system has.

**The velocity.** v_rel is the relative collision speed near pericenter. Sources, in order of directness: (i) the shock Mach number from a detected X-ray shock front or a radio relic (relics trace merger shocks and give a Mach number directly), converted to a shock speed; (ii) hydrodynamic reconstruction of the individual system (many well-studied mergers have bespoke sims); (iii) the line-of-sight velocity difference of the two BCGs as a lower bound (projection-limited). Each carries a different systematic; record which was used per system.

**The time since pericenter, t_post.** The linear (mid-speed) regime predicts Δr ≈ v_rel × t_post, so t_post is needed to place a system on the curve. It comes from the same hydro reconstructions (shock displacement / relic separation over shock speed). Where t_post is unavailable, the system still constrains F1/F2 through v_rel alone but not the linear slope.

**The combined variable.** Because the mid-regime prediction is Δr ∝ v_rel · t_post, plot Δr against **v_rel · t_post** where t_post exists (tests the linear slope and the ceiling), and against **v_rel** alone for the full sample (tests the knee's existence and sharpness). Two plots, two questions.

## 3. The three hypotheses as data signatures

| Feature to measure | Event Density | ΛCDM (particle DM) | MOND-EFE |
|---|---|---|---|
| Low-v behavior | flat at ≈0 up to a threshold | offset present, set by per-merger geometry (scatter) | offset fades smoothly toward 0 |
| Transition | **sharp knee** (step) | none | gradual ramp |
| Mid-v behavior | near-linear in v_rel·t_post | no universal line | smooth monotonic |
| High-v behavior | ceiling at ξ_KZ; fastest may show >2 peaks | no ceiling | no ceiling |

The decisive cell is the **transition row**: step (ED) vs none (ΛCDM) vs ramp (MOND). Everything else is corroborating.

## 4. The discriminating statistic (how you actually decide)

Fit the population with three nested/competing models and compare:

- **M0 (ΛCDM null):** Δr = constant + intrinsic scatter, uncorrelated with v_rel. (Offset driven by impact parameter, viewing angle, mass ratio, not speed.)
- **M1 (MOND-EFE):** Δr = a smooth monotonic function of v_rel (e.g. a power law or saturating-exponential), no threshold.
- **M2 (ED):** Δr = a segmented/broken-line: zero below v_crit, linear above, plateau above v_sat. v_crit, slope, and plateau are free (respecting the ~15–1500 km/s prior on v_crit).

Decide by penalized model comparison (BIC/AIC, or Bayesian evidence with the stated priors). **F1** = does M2 or M1 beat M0 (is offset velocity-dependent at all)? **F2** = does M2 (broken line, sharp) beat M1 (smooth) — the sharpness test, run by densely sampling near the inferred v_crit. **F3** = is there a plateau (ceiling) at high v_rel, and do the fastest systems show multiplicity >2? A formal change-point test (segmented regression with an F-test on the breakpoint, or a Bayesian broken-line with a breakpoint posterior) is the natural instrument for the knee.

## 5. The real dataset, and what to pull from it

**Ensemble offset catalog.** Harvey et al. (2015, *Science* 347:1462) assembled ~30 merging clusters (72 substructures) from the HST/Chandra archive; Wittman et al. (2018, *ApJ* 869:104) reanalyzed the same sample, corrected substantial offset-measurement errors, and is the more reliable offset source. Use Wittman's offsets, re-projected to the mass–gas pairing.

**Well-characterized individual dissociative mergers** (each with lensing + X-ray maps and, for many, a shock/relic velocity and a hydro reconstruction): the Bullet (1E 0657-558), MACS J0025.4-1222, Abell 520 (the "Train Wreck"), Abell 2744 (Pandora), Abell 1758N, the Musket Ball (DLSCL J0916.2+2951), El Gordo (ACT-CL J0102-4915), the Sausage (CIZA J2242.8+5301), Abell 2034, Abell 2163, Abell 56. These anchor the high-velocity end and several have Mach numbers from radio relics.

**Velocity source.** Cross-match the offset sample against radio-relic / X-ray-shock Mach-number catalogs (relic surveys give shock speeds directly) and the published per-system hydro reconstructions for v_rel and t_post.

**Deliverable table (the thing to build):** one row per system — {Δr_mass-gas (kpc), projection flag, v_rel (km/s) + source, t_post (Gyr) + source, mass ratio, impact-parameter estimate, number of offset peaks}. That table, which does not yet exist in one place for the mass–gas pairing, *is* the Phase-3 dataset. Assembling it is the bulk of the observational work; the statistics of §4 are cheap once it exists.

## 6. The feasibility reality (the honest hard part)

There is a selection effect that makes this test hard exactly where it is most diagnostic, and the protocol must state it up front:

**Dissociative mergers are velocity-selected.** A cluster earns the label "dissociative" (a visible mass–gas offset) largely by being a *fast* merger — slow mergers do not separate their components enough to stand out. So the observed catalog is concentrated at high v_rel (roughly 1000–4500 km/s), which is the **ceiling/saturation regime**, and is sparse-to-empty near and below the knee, which is the **turn-on regime** where F1/F2 live. The very selection that builds the sample pushes it past the feature that most distinguishes ED.

Consequences, stated plainly:

- **F3 (ceiling, multiplicity) is testable now**, with the existing fast-merger sample — the ED prediction of a plateau and occasional >2 peaks at the extreme high-velocity end can be checked against El Gordo–class systems.
- **F1/F2 (the knee) need the under-populated low/marginal-v regime**: mergers caught pre-dissociation, minor mergers, low-Mach systems, and *near-zero-offset* clusters that current catalogs discard as "relaxed." These are the diagnostic points, and they are the ones nobody has systematically measured, precisely because a small offset is undramatic.
- **This is a survey-era test.** Rubin/LSST weak lensing, Euclid, and eROSITA X-ray will multiply the merging-cluster sample and, critically, fill in the low-offset / low-velocity systems the current archive misses. The knee test becomes statistically feasible when the sample includes the marginal mergers, not just the spectacular ones.

Naming this is not a hedge; it is the value of the protocol. It converts "measure the relation" into "measure the relation *including the boring low-offset systems*, because the knee lives where the drama does not."

## 7. Confounds and controls

- **Projection.** Measured Δr ≤ true 3D Δr; systems seen off the plane of sky have compressed offsets. Control: use the plane-of-sky mergers (MACS J0025, the Sausage) as a cleaner sub-sample; carry a per-system projection flag; or de-project statistically with a viewing-angle prior.
- **Impact parameter and mass ratio.** Both modulate Δr independently of v_rel and are the source of the ΛCDM scatter. Control: record them per system and marginalize; the ED signal is a *threshold in v_rel* that survives marginalization over these, whereas ΛCDM has no such threshold.
- **t_post spread.** Systems are caught at different times since pericenter; the linear regime is in v_rel·t_post, so t_post must be folded in, not ignored. The gas-lag Δr (per subcluster) is less t_post-sensitive than the peak-to-peak separation.
- **Measurement systematics.** The Harvey→Wittman revision is a live warning that offset measurements are hard and method-dependent. Control: use a single uniform offset-measurement pipeline across the sample (Wittman's or a successor), not a heterogeneous literature compilation.
- **Selection (the §6 effect), stated again as a control:** explicitly include archival low-offset / "relaxed-looking" mergers rather than only catalogued dissociative ones, or the knee is unobservable by construction.

## 8. Honest scope

- The test targets the **shape** (knee existence, knee sharpness, ceiling), which is the ED-distinctive and open-ingredient-robust content — not the knee's numerical location, which the theory does not yet pin (§1).
- A clean **null** (offset uncorrelated with velocity, M0 wins) challenges ED and favors ΛCDM. A **smooth** velocity dependence with no sharp turn-on (M1 wins) favors MOND-EFE over ED. A **sharp broken-line** (M2 wins), especially a demonstrated step at the transition, is the ED signature and is not predicted by either rival.
- Two theory items would sharpen the prediction from "there is a knee somewhere in 15–1500 km/s" to "the knee is at v_crit ± δ": deriving the substrate's super-linear shock response and the defect's two-timescale stabilization (Phase-2 §7.1). Those are the theory-side next steps; this protocol is the observation-side one, and the two are independent — the shape test can run before the location is pinned.
- This is a *proposed* measurement. Its worth is that it is falsifiable, it is ED-distinctive (a claim neither rival makes), and it names exactly what data would decide it. It is not a claim that the measurement has been made.

## 9. One-paragraph statement of record

The Event Density topological-defect account of the Bullet predicts that, across the merging-cluster population, the mass–gas offset rises from zero through a **sharp knee** to a **ceiling** as a function of merger velocity — a shape neither particle dark matter (which predicts velocity-independent scatter) nor MOND-EFE (which predicts a smooth roll-off) produces. The decisive, theory-robust test is the *sharpness of the turn-on*, measured by densely sampling mergers near the transition. The observable is the weak-lensing-mass minus X-ray-gas offset (distinct from the DM–galaxy offset of the self-interaction literature), the velocity comes from shock/relic Mach numbers and hydro reconstructions, and the existing Harvey/Wittman ensemble plus the well-characterized dissociative mergers supply the high-velocity anchor. The binding limitation is that dissociative mergers are velocity-selected into the ceiling regime, so the knee itself lives in the under-measured low-offset population that current archives discard and that Rubin/Euclid/eROSITA will fill in. The measurement is not yet made; the protocol states exactly how to make it and what each outcome would mean.
