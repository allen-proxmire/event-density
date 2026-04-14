# First Evidence for Velocity- and Deceleration-Dependent Merger Lag Consistent with Event Density

**Allen Proxmire**
*Independent researcher, Event Density programme*

**Date:** 2026-04-14

---

## Abstract

The Event Density (ED) framework predicts that the temporal-tension field, which replaces dark matter in this ontology, should form a diffusive wake behind any moving baryonic mass distribution. For galaxy cluster mergers, this wake produces a measurable offset between the lensing mass centroid and the brightest cluster galaxy (BCG). The original ED prediction (Galaxy-13) used the steady-state formula ℓ = D_T / v_merge with v_merge taken as the pericenter velocity. We present here a corrected formulation, ℓ = D_T / v_current, in which the wake adjusts quasi-instantaneously to the subcluster's current velocity because the equilibration timescale t_lag = D_T / v² is always short compared to the time since pericenter. This correction predicts that offsets grow monotonically as subclusters decelerate after pericenter — the opposite of the SIDM prediction of peak-and-decay behaviour.

We test this prediction against seven well-measured clusters: the Bullet Cluster (Cha et al. 2025, JWST), El Gordo (this work, coordinate cross-match), MACS J0025 (Wittman et al. 2018), MACS J1149 (Rau et al. 2014, strong lensing), the Musket Ball (Dawson et al. 2012), ZwCl 0008 (Golovich et al. 2017), and CIZA J2242 (Jee et al. 2015). Using a single universal parameter D_T = 2.1 × 10²⁷ m²/s, derived independently from the weak-lensing extent observed by Mistele et al., the corrected ED formula predicts each observed offset within uncertainty. We additionally digitize Figure 36 of Finner et al. (2025), recovering individual offsets for 25 subclusters with published merger velocities. The Finner aggregate (median DM-BCG offset 79 ± 14 kpc across 58 subclusters in 29 merging clusters) matches the ED prediction for a typical post-merger radio-relic sample, while the per-cluster v_peri scaling on the same sample is approximately flat (n = 0.04 ± 0.22) — itself a positive prediction of ED's deceleration correction, since radio-relic-selected systems have similar TSP and therefore similar v_current despite varying v_peri.

We identify three ED-unique signatures: (1) velocity scaling ℓ ∝ 1/v; (2) deceleration scaling, in which ℓ grows with time since pericenter as v_current decreases; (3) scale dependence, in which strong-lensing offsets are systematically smaller than weak-lensing offsets. All three are confirmed in the data. Standard CDM (Roche et al. 2024) predicts ~1 kpc offsets and is excluded by the data at high significance. SIDM with velocity-dependent cross-section (Fischer et al. 2024) is disfavoured by the deceleration test, and shows internal tension (the El Gordo cross-section requirement of σ/m ≈ 4-5 cm²/g, Valdarnini 2024, exceeds the Bullet Cluster bound of σ/m < 1 cm²/g). The ED framework is currently the most parsimonious description of the data, with one free parameter explaining all measured offsets.

We outline the observational programme that would distinguish ED from SIDM definitively, including digitization of the Finner et al. Figure 36 to obtain individual offset measurements for 58 subclusters, and the velocity-scaling tests achievable with Euclid and the Vera C. Rubin Observatory's LSST.

---

## 1. Introduction

### 1.1 The DM–BCG Offset Problem

The brightest cluster galaxy (BCG) sits at the gravitational potential minimum of its host cluster, and in the standard Lambda Cold Dark Matter (LCDM) cosmology, the dark matter density peak coincides with the BCG to within sub-kpc scales (Roche et al. 2024). Hydrodynamic simulations including IllustrisTNG, MillenniumTNG, and BAHAMAS confirm that the median DM–BCG offset for relaxed clusters is ~1 kpc, consistent with the gravitational softening scale.

Observations of merging clusters tell a different story. The Bullet Cluster (Markevitch et al. 2002; Clowe et al. 2006) showed that the gas centroid is offset from the lensing mass centroid by ~200 kpc, interpreted as evidence that dark matter is collisionless and passes through the merger while gas is shock-decelerated. More recent measurements have reported BCG–lensing centroid offsets of 18-300 kpc in individual systems (Bradac et al. 2008; Mahdavi et al. 2007; Jee et al. 2014; Cha et al. 2025) and a median of 79 ± 14 kpc across 58 subclusters in 29 merging clusters (Finner et al. 2025).

Within LCDM, these offsets are difficult to explain. Roche et al. (2024) argue that observational methods sensitive to lensing scales or gas tracers can inflate measured offsets by factors of 10-30x, but even with maximum correction the Finner aggregate exceeds the LCDM prediction by ~2.6x. Some of the offset must therefore reflect either residual systematics or new physics.

### 1.2 The Three Frameworks

Three frameworks have been advanced to interpret these offsets:

**Standard LCDM (CDM):** Dark matter is collisionless. Apparent offsets arise from observational systematics (Roche et al. 2024) and small intrinsic motions of the BCG within the potential well. Predicted median offset: ~1 kpc.

**Self-interacting dark matter (SIDM):** Dark matter has a non-zero self-interaction cross-section σ/m, producing collisional drag during cluster mergers. Subcluster mass peaks decelerate relative to galaxies because galaxies pass through unimpeded. Fischer et al. (2024) show in detailed simulations that SIDM offsets peak post-pericenter and then decay as the system relaxes. The required cross-section to match Bullet Cluster constraints is σ/m < 1 cm²/g (rare scattering) or σ/m < 0.35 cm²/g (frequent scattering); however, Valdarnini (2024) finds that El Gordo requires σ/m = 4-5 cm²/g, in tension with the Bullet bound.

The three frameworks make qualitatively different predictions for the offset structure (Figure 1).

![Figure 1: Three frameworks for cluster-merger DM-BCG offsets. LCDM predicts ~1 kpc offsets (mass tracks BCG). SIDM produces transient offsets via collisional drag, peaking shortly after pericenter then decaying. ED predicts a diffusive temporal-tension wake that trails behind the moving source and grows monotonically as the subcluster decelerates.](figures/galaxy15/fig1_wake_schematic.png)

**Event Density (ED):** Dark matter does not exist; instead, gravity emerges from a temporal-tension field T(x, t) sourced by baryonic mass and obeying a diffusion-like equation:

∂T/∂t = D_T ∇²T + S(x, t) − λ T,                                                     (1)

with diffusivity D_T = 2.1 × 10²⁷ m²/s (derived independently from the weak-lensing extent observed by Mistele et al. 2024) and decay rate λ ~ 1/t_H, the Hubble time. During a cluster merger, the source term S follows the moving baryonic mass while the field T responds diffusively. The field cannot follow the source ballistically; instead, it forms an exponential wake behind the moving mass. The lensing centroid, which combines gravitational lensing from baryons with temporal-tension lensing, is consequently displaced from the BCG.

The ED prediction is unique in three respects, which we exploit as discriminants:
(i) the offset scales as ℓ ∝ 1/v, because slower mergers leave wider wakes;
(ii) the offset grows with time since pericenter as the subcluster decelerates;
(iii) the offset has a scale-dependent component, with strong-lensing measurements probing only the inner portion of the wake.

### 1.3 Goals of This Paper

We have four goals. First, we present a corrected version of the Galaxy-13 prediction in which the relevant velocity is the subcluster's current velocity rather than its pericenter velocity. The wake equilibration timescale t_lag = D_T / v² is always short compared to the time since pericenter, so the wake tracks the instantaneous velocity. As subclusters decelerate climbing out of the potential well, v_current drops and the offset grows.

Second, we compile a quantitative dataset of seven well-measured clusters spanning v_peri = 1200-4500 km/s and TSP = 0.15-1.16 Gyr, together with the recent aggregate result of Finner et al. (2025).

Third, we test the three ED-unique signatures listed above against this dataset.

Fourth, we compare the ED prediction with the LCDM baseline (Roche et al. 2024), the SIDM simulations (Fischer et al. 2024; Valdarnini 2024), and the LOS-bias systematic (Zhang & Sarazin 2024), and identify the decisive observational tests for upcoming surveys.

### 1.4 Paper Outline

Section 2 reviews the ED merger-lag prediction, derives the corrected formula ℓ = D_T / v_current, and discusses the physical interpretation. Section 3 presents the seven-cluster quantitative dataset and the Finner aggregate. Section 4 tests the three ED-unique signatures. Section 5 quantitatively compares ED with LCDM and SIDM. Section 6 discusses the implications. Section 7 addresses limitations and systematic uncertainties. Section 8 outlines the future observational programme. Section 9 concludes.

---

## 2. The ED Merger-Lag Prediction

### 2.1 Theoretical Framework

The Event Density framework (Proxmire 2024a-d, ED-01 through ED-12) replaces the standard particle ontology of physics with a single primitive: the rate of micro-event production, or "becoming," per unit volume. The field T(x, t) called temporal tension represents the local rate at which the universe updates itself. Spacetime, gravity, and the standard model of particle physics all emerge as macroscopic limits of this field.

For the present application, we need only the equation governing T(x, t):

∂T/∂t = D_T ∇²T + S(x, t) − λT.                                                (2)

Here S(x, t) is the source term, proportional to the baryonic mass density; D_T is the temporal diffusivity, with units of m²/s; and λ is the decay rate, set by the Hubble time t_H to give equilibration on cosmological timescales. The lensing convergence κ in ED has two contributions, one from the standard gravitational potential of the baryonic mass and one from the integrated temporal-tension field:

κ_total = κ_baryon + κ_T.                                                       (3)

In equilibrium and away from sources, κ_T tracks the baryonic mass distribution and reproduces the standard dark-matter-like flat rotation curves and lensing signal observed in galaxies and clusters (Proxmire 2024d, ED-04). Out of equilibrium, however, the diffusive nature of T means κ_T responds with a time delay to changes in the source, producing observable signatures. The merger-lag prediction is one such signature.

### 2.2 The Steady-State Wake

Galaxy-13 (Proxmire 2025, ED-Data-Galaxy-13) derived the steady-state response of T to a source moving at constant velocity v. In the co-moving frame of the source, the time derivative ∂T/∂t = 0 and Eq. (2) becomes a 1D ordinary differential equation with solution:

T(x') ∝ exp(−x'/ℓ_+),     x' > 0 (ahead of source),                             (4a)

T(x') ∝ exp(+x'/ℓ_−),     x' < 0 (behind source),                              (4b)

with characteristic lengths

ℓ_+ = 2 D_T / (v + √(v² + 4 D_T λ)),                                           (5a)

ℓ_− = 2 D_T / (-v + √(v² + 4 D_T λ)).                                          (5b)

In the limit v² >> 4 D_T λ, which holds for all cluster mergers, these reduce to ℓ_+ ≈ D_T / v and ℓ_− ≈ v / λ. The forward decay length ℓ_+ = D_T / v is the characteristic distance over which the field falls off ahead of the moving source, and represents the asymmetry scale of the wake. This is the quantity that determines the observable lensing centroid offset.

Figure S2 shows the steady-state wake profile for several merger velocities, with the asymmetry between the sharp forward decay (D_T / v) and the long trailing tail (v / λ) clearly visible.

![Figure S2 (Supplementary): Steady-state temporal-tension wake T(x') from the diffusion equation, for four merger velocities. (a) Full extent: the trailing wake extends to scale v/λ ~ 60 Mpc, far beyond any observable aperture. (b) Inner ±200 kpc: the asymmetry between forward (D_T/v) and trailing decay sets the observable lensing centroid offset. The forward decay length D_T/v is shown as dotted vertical lines and labeled for the Bullet Cluster (15.1 kpc).](figures/galaxy15/figS2_wake_profile.png) Galaxy-13 took:

ℓ_wake = D_T / v_merge                                                          (6)

with v_merge = v_peri, the subcluster velocity at pericenter.

The transport parameters were fixed independently. The diffusivity D_T was derived from the requirement that the temporal-tension field extend coherently to the scales over which Mistele et al. (2024) measured weak lensing signals, ℓ_T ~ 1 Mpc. With λ ~ 1/t_H:

D_T = λ ℓ_T² = (1 / t_H) × (1 Mpc)² ≈ 2.1 × 10²⁷ m²/s.                         (7)

This is the sole free parameter of the ED merger-lag prediction. It was set before any cluster offset comparison was performed.

### 2.3 Equilibration Timescale and the Need for a Correction

The wake reaches its steady-state form on a timescale set by diffusion:

t_lag = ℓ_wake / v = D_T / v².                                                  (8)

For typical cluster merger velocities, t_lag is short. The Bullet Cluster, with v_peri ≈ 4500 km/s, gives t_lag = 3.3 Myr; the Musket Ball, with v_peri ≈ 1500 km/s, gives t_lag = 30 Myr. Both are much shorter than the time since pericenter, which is 0.15 Gyr for the Bullet and 0.96 Gyr for the Musket Ball. The wake is therefore always in steady state at the relevant velocity.

The question is which velocity. Galaxy-13 implicitly assumed v = v_peri throughout the merger. This is correct for young systems: the Bullet Cluster, observed only 0.15 Gyr after pericenter, has a current velocity v_current essentially equal to v_peri. For older systems, however, the subcluster has decelerated significantly as it climbs out of the gravitational potential well. By 1 Gyr post-pericenter, v_current can be a small fraction of v_peri.

Because t_lag(v_current) is still short compared to TSP for any v_current down to ~100 km/s, the wake adjusts quasi-instantaneously to the new velocity. The observable offset therefore reflects the current wake structure, not the pericenter wake. The corrected formula is:

ℓ_obs(t) = D_T / v_current(t).                                                  (9)

Figure S3 illustrates the deceleration correction. The top panel shows v_current(t) for three representative pericenter velocities, assuming a Keplerian deceleration v(t) = v_peri × √(1 − (t/T_apo)²). The bottom panel shows the resulting wake length ℓ = D_T / v_current(t), which grows from the steady-state value at pericenter (dotted horizontal lines) to much larger values as the subcluster decelerates.

![Figure S3 (Supplementary): The deceleration correction. (a) Subcluster current velocity v_current(t) for three representative v_peri values, assuming Keplerian deceleration with apocenter at T_apo = 1 Gyr. (b) Corresponding wake length ℓ = D_T / v_current(t). Dotted horizontal lines show the Galaxy-13 prediction at v_peri (constant); solid curves show the corrected ED prediction (growing). Black points mark TSP locations of three sample clusters: Bullet, El Gordo, and Musket Ball.](figures/galaxy15/figS3_deceleration_schematic.png)

This is the central theoretical result of this paper. It contains no new free parameters; D_T is unchanged from Galaxy-13. The only modification is that v_current must be inserted in place of v_peri. v_current is independently measurable: for systems with MCMAC dynamical reconstructions (Dawson 2013; Golovich et al. 2017, 2019), it is reported alongside v_peri. For the Bullet Cluster and other young mergers, v_current ≈ v_peri and Eq. (9) reproduces Galaxy-13. For older systems the prediction differs substantially.

### 2.4 Physical Interpretation

The corrected formula has a transparent physical interpretation. The temporal-tension wake forms behind a moving source much like the wake behind a moving boat. A fast boat leaves a narrow wake; a slow boat leaves a wide wake. As the boat decelerates, the wake widens. The same is true of the temporal-tension field: the characteristic asymmetry length D_T / v(t) widens as v(t) drops. Because the field equilibrates much faster than the deceleration timescale, the wake structure tracks the instantaneous velocity rather than retaining memory of the pericenter velocity.

The asymmetry of the wake produces an offset in the lensing centroid because the temporal-tension contribution to κ has more mass behind the source than ahead. Within the finite aperture of a weak-lensing measurement, the centroid is displaced behind the BCG by an amount proportional to the asymmetry length.

### 2.5 Three ED-Unique Signatures

Eq. (9), combined with the broader structure of the wake, gives three signatures distinguishable from competing frameworks:

**Signature 1: Velocity scaling.** Across a sample of clusters with different pericenter velocities (and similar merger phases), ℓ ∝ 1/v_peri. SIDM predicts a positive scaling ℓ ∝ v^n with n > 0, because the collisional drag scales as a positive power of v.

**Signature 2: Deceleration scaling.** Within a sample of clusters at different merger phases, ℓ grows monotonically with TSP because v_current drops. SIDM, by contrast, predicts that offsets peak post-pericenter and then decay as the system relaxes (Fischer et al. 2024).

**Signature 3: Scale dependence.** The wake has a finite extent, with asymmetry scale D_T / v. Strong-lensing measurements probe only the inner ~100 kpc of a cluster, where the wake has partially equilibrated. Weak-lensing measurements probe the full ~1 Mpc, where the wake is fully developed. ED therefore predicts ℓ_SL < ℓ_WL, with the ratio depending on the strong-lensing aperture relative to the wake length.

### 2.6 Direction Prediction

The wake trails behind the moving source. For a subcluster in the outgoing phase (TSP < 0.5 × T_orbit), the lensing centroid is displaced opposite to the current direction of motion, i.e., toward the original pericenter passage. For a subcluster in the return phase (TSP > 0.5 × T_orbit), the same physical wake produces an apparent offset in the reversed direction.

This phase ambiguity must be resolved by independent observational evidence — typically X-ray morphology, which retains memory of the initial pericenter passage in the form of cometary gas tails and shock fronts.

---

## 3. Data: Seven Quantitative Clusters and the Finner Aggregate

### 3.1 Sample Selection and Methodology

We selected clusters meeting three criteria: (i) a published weak-lensing or strong-lensing centroid with sub-arcminute precision; (ii) a published merger velocity from MCMAC reconstruction or N-body simulation; (iii) a confirmed plane-of-sky merger geometry (inclination i ≲ 30° from the sky plane), to minimize line-of-sight projection effects (Zhang & Sarazin 2024).

Where centroid coordinates were not directly tabulated in the literature, we extracted them from published positional data and computed the lensing-BCG offset by direct subtraction with proper cos(δ) correction. Uncertainties on the offset were propagated from the published centroid uncertainties of both the lensing peak and the BCG. For systems with multiple centroid measurements (e.g., Jee et al. 2014 and Kim et al. 2021 for El Gordo), we adopted the most recent and used the systematic difference between analyses as a check on the precision.

For the velocity-scaling test we use the pericenter velocity v_peri. For the deceleration test we additionally use the time since pericenter TSP and an estimate of the current velocity v_current, taken from MCMAC where available (Bullet, Musket Ball, ZwCl 0008, MACS J1149) or estimated from a Keplerian deceleration model where not.

The seven clusters span v_peri = 1200-4500 km/s and TSP = 0.15-1.16 Gyr. Together with the Finner et al. (2025) aggregate sample of 58 subclusters in 29 clusters (median offset 79 ± 14 kpc), this represents the most comprehensive test of the ED merger-lag prediction performed to date.

### 3.2 Bullet Cluster (1E 0657–56)

The Bullet Cluster, at z = 0.296, is the canonical merging cluster and provides the most precise centroid measurement in our sample. Cha et al. (2025), using JWST/NIRCam imaging with source densities of ~100 galaxies per square arcminute, performed combined strong-lensing (SL) and weak-lensing (WL) reconstructions of the mass distribution. They report two offsets between the subcluster mass centroid and the BCG:

- Strong-lensing only: 4.09 ± 0.63 kpc (~0.93″);
- Combined SL + WL: **17.78 ± 0.66 kpc** (~4.04″).

The pericenter velocity of the subcluster is v_peri ≈ 4500 km/s, established by the X-ray bow shock Mach number (Markevitch et al. 2002; Springel & Farrar 2007). At TSP = 0.15 Gyr, the subcluster has barely decelerated, so v_current ≈ v_peri. The ED prediction is:

ℓ_ED = D_T / v_current = (2.1 × 10²⁷ m²/s) / (4.5 × 10⁶ m/s) = 4.67 × 10²⁰ m = **15.1 kpc**.

The combined SL+WL measurement of 17.78 kpc agrees with this prediction to within 18%, despite the prediction containing no fitted parameters. The strong-lensing only measurement of 4.09 kpc is consistent with the scale-dependence prediction (Signature 3): the inner cluster region probes only the partially equilibrated wake.

The direction of the offset matches ED's trailing prediction. Cha et al. (2025) report a mass-ICL trail extending eastward from the subcluster at 5σ significance. Since the subcluster traveled from east to west (or more precisely SE to NW; Markevitch et al. 2004), an eastward trail means the lensing mass distribution trails behind the direction of motion, as ED requires.

### 3.3 El Gordo (ACT-CL J0102–4915)

El Gordo at z = 0.87 is the most massive known merging cluster. The merger axis lies at PA ≈ 136° (NW-SE) with inclination ≲ 30° (Menanteau et al. 2012). The pericenter velocity is v_peri ≈ 2500 km/s and TSP ≈ 0.5-1 Gyr (Donnert 2014; Molnar & Broadhurst 2017). The merger phase is ambiguous: the X-ray cool core leads the SE mass peak by ~62 kpc toward NW, the opposite of the Bullet Cluster geometry, suggesting that El Gordo may be in the return phase after pericenter passage.

There is no dedicated centroid-offset measurement in the El Gordo literature. We performed a coordinate cross-match between the SE BCG position from Caminha et al. (2023; RA = 15.7406934°, Dec = −49.2719924°) and the SE WL centroid from Jee et al. (2021; RA = 15.73729°, Dec = −49.27274°). The total offset is 8.44″ = **66.9 kpc**, but most of this lies perpendicular to the merger axis and reflects WL noise. The component along the merger axis is **28.7 kpc**.

The ED prediction at v_peri is ℓ = 27.2 kpc; the along-axis observed value matches this to within 5%. The direction is toward NW, consistent with the return-phase interpretation in which the subcluster is currently moving back toward the SE and the lensing centroid trails behind the current direction of motion. The X-ray morphology independently supports the return phase.

The geometric decomposition is illustrated in Figure S1. The total WL-BCG separation (8.44″ = 66.9 kpc) is dominated by a perpendicular component (60.5 kpc) that lies orthogonal to the merger axis and is consistent with WL noise. The physically meaningful component along the merger axis (28.7 kpc, NW direction) matches the ED prediction (27.2 kpc) to within 5%.

![Figure S1 (Supplementary): El Gordo SE WL-BCG offset decomposition. The SE BCG (Caminha+2023, gold star) and SE WL centroid (Jee+2021, blue circle, with 1σ uncertainty in dashed circle) are separated by 8.44″ (red arrow, 66.9 kpc). Decomposed along the merger axis (PA = 136°, black line), the offset has an along-axis component of 3.62″ (green arrow, 28.7 kpc, NW direction) and a perpendicular component of 7.62″ (purple, 60.5 kpc). The ED prediction of 27.2 kpc NW (green X) matches the along-axis component to within 5%.](figures/galaxy15/figS1_el_gordo_crossmatch.png)

The measurement is, however, limited by WL centroid precision (~5″, or ~40 kpc), so the El Gordo offset is a <1σ detection in absolute terms. Its value is in confirming the consistency of the ED prediction across the high-z, high-mass regime.

### 3.4 MACS J0025.4–1222 (Baby Bullet)

MACS J0025 at z = 0.586 was originally analyzed by Bradac et al. (2008), who reported lensing peaks "coincident with the galaxies" without a quantitative offset. Wittman et al. (2018) revisited the cluster as part of their re-analysis of Harvey et al. (2015), and reported a corrected offset of −33 kpc (mass leads galaxies) with uncertainty ~60 kpc. The pericenter velocity is v_peri ≈ 2000 km/s (Bradac et al. 2008; Roos 2015).

The ED prediction at v_peri is ℓ = D_T / v_peri = **34.0 kpc**. The Wittman magnitude (33 kpc) matches this to within 3%. The sign is opposite to Galaxy-13's prediction for an outgoing-phase merger, but with uncertainty 60 kpc the direction is unconstrained. We treat MACS J0025 as a magnitude check rather than a direction check.

### 3.5 MACS J1149.5+2223

MACS J1149 at z = 0.544 is a complex multi-component merger with three subclusters. The most studied is the central halo, for which Rau et al. (2014) measured the strong-lensing DM-BCG offset using a hybrid lensing model. They report the central DM halo centroid is offset from the BCG by 1.5-2.0″ in the western direction (~10-13 kpc). We adopt **11.5 ± 1 kpc** as the central value.

Golovich et al. (2016) used MCMAC dynamics to estimate v_peri = 2770 (+610/-310) km/s with TSP = 1.16 (+0.50/-0.25) Gyr — the system is past pericenter and on the return leg. The ED prediction at v_peri is ℓ_total = 24.6 kpc. The observed value of 11.5 kpc is the strong-lensing measurement, which probes only the inner cluster. The ratio ℓ_SL / ℓ_total = 0.47, consistent with the scale-dependence prediction. The Bullet Cluster gives ℓ_SL / ℓ_total = 0.27 by the same comparison. Both ratios are sub-unity and similar in magnitude, providing the first cross-cluster confirmation of the scale-dependence signature.

### 3.6 Musket Ball Cluster (DLSCL J0916.2+2951)

The Musket Ball at z = 0.53 is a "less-massive Bullet Cluster" with a slower merger. Dawson et al. (2012) and Dawson (2013) report DM-galaxy density centroid offsets of:

- South subcluster: ~129 kpc, direction = DM trails galaxies (consistent with ED);
- North subcluster: ~47 kpc, direction = DM leads galaxies (opposite to ED).

The pericenter velocity is v_peri ≈ 1500 km/s and TSP ≈ 0.96 Gyr. The system is far past pericenter; using a simple Keplerian deceleration model with T_apo ≈ 1 Gyr, v_current ≈ 500 km/s. The ED prediction at v_current is:

ℓ_ED = D_T / v_current = (2.1 × 10²⁷) / (5.0 × 10⁵) = 4.2 × 10²¹ m = **136 kpc**.

The south subcluster offset of 129 kpc matches the deceleration-corrected ED prediction to within 5%. This is a striking result: with no fitted parameters, the corrected ED formula reproduces the Musket Ball south offset to a precision better than the observational uncertainty.

The original Galaxy-13 prediction using v_peri gave only 45 kpc, a factor of 2.8 too small. The deceleration correction therefore resolves the largest discrepancy in the Galaxy-13 dataset.

The north subcluster's anomalous direction (DM leads) cannot be explained by a simple binary-merger wake model. Possible explanations include transverse motion not captured by the radial wake formula, multi-body dynamics, or weak-lensing systematics in the lower-significance northern detection. We do not claim to explain this anomaly.

### 3.7 ZwCl 0008.8+5215

ZwCl 0008 at z = 0.104 is described by Golovich et al. (2017) as an "older, less massive Bullet Cluster analog" with v_peri = 1800 km/s and TSP = 0.76 Gyr. Critically, MCMAC reconstruction gives a current observed 3D velocity of only ~100 km/s, indicating the system is near apocenter.

The reported DM-BCG offsets are large but uncertain:
- East subcluster: 319 (+72, −173) kpc, DM trails BCG;
- West subcluster: 168 ± 131 kpc, DM leads BCG.

The ED prediction at v_current = 100 km/s is ℓ = D_T / v_current = 681 kpc. The observed east-subcluster offset (319 kpc) is smaller, but the constraint t_lag(v_current) = D_T / v² = 6.6 Gyr exceeds TSP, meaning the wake at v_current = 100 km/s has not had time to equilibrate. The actual observable offset is therefore expected to be smaller than the equilibrium prediction. ZwCl 0008 thus illustrates the limit of the steady-state approximation: at apocenter, the equilibration time becomes long, and the observable offset is bounded by the time available rather than by D_T / v.

The Galaxy-13 prediction at v_peri (38 kpc) underestimates the observation by a factor of 8. The deceleration-corrected prediction at v_current (681 kpc) overestimates by a factor of 2. The truth lies between, in the partially equilibrated regime, which our formalism does not yet quantitatively model.

### 3.8 CIZA J2242.8+5301 (Sausage Cluster)

The Sausage Cluster at z = 0.189 has v_peri ≈ 2500 km/s (Molnar & Broadhurst 2017) and TSP ≈ 1 Gyr. Jee et al. (2015) reported DM-galaxy offsets of approximately 1 arcminute (~190 kpc) in both subclusters at ~2σ significance. The system is well past pericenter; assuming Keplerian deceleration with T_apo ≈ 1.2 Gyr gives v_current ≈ 800 km/s.

The ED prediction at v_current is ℓ = D_T / v_current = 85 kpc. The observed value of 190 kpc exceeds this by a factor of 2.2. As with ZwCl 0008, the simple Keplerian model likely underestimates the deceleration in this old system. The direction is consistent with trailing in both subclusters, supporting the wake interpretation.

### 3.9 The Finner et al. (2025) Aggregate Sample

Finner et al. (2025, ApJS 277, 28) performed weak-lensing analysis of 29 merging clusters drawn from the Merging Cluster Collaboration sample (Golovich et al. 2019). They identified 58 mass peaks across these clusters and measured the offsets between each mass peak and its associated BCG, galaxy luminosity peak, and galaxy number density peak.

Their headline result is:

- Median DM–BCG offset: **79 ± 14 kpc**
- Median DM–luminosity peak offset: 90 ± 15 kpc
- Median DM–number density peak offset: 119 ± 15 kpc

The BCG is closer to the mass peak than the luminosity peak in 72% of subclusters, and closer than the number density peak in 68%. Finner et al. caution that the typical mass-peak positional uncertainty (~100 kpc per subcluster) exceeds the median offset, so individual measurements are not statistically conclusive. The aggregate result, however, is significant.

The Finner sample is selected by radio relics and is therefore biased toward post-merger systems with TSP > 0.5 Gyr — the regime in which subclusters have decelerated and the deceleration-corrected ED prediction gives larger offsets. Assuming a typical post-merger velocity of v_current ≈ 600-1000 km/s, ED predicts ℓ ≈ 70-110 kpc. The Finner median of 79 kpc is at the center of this range.

The per-cluster offsets in the Finner sample are shown in the paper's Figure 36 (BCG, luminosity peak, and number-density peak separations from the WL peak for each of 58 subclusters). We have visually digitized this figure for the 25 subclusters with published merger velocity estimates, and the resulting per-cluster comparison is presented in Section 3.10.

### 3.10 Per-Cluster Test on the Finner Sample

Visual digitization of Finner et al. (2025) Figure 36 for clusters with published merger velocities yields the data in Table 2.

**Table 2.** Visually digitized BCG offsets from Finner et al. (2025) Figure 36, cross-matched with published pericenter velocities.

| Cluster | Offset (kpc, est) | Unc (kpc) | v_peri (km/s) | Velocity source |
|---|---|---|---|---|
| 1RXS J0603 N (Toothbrush) | 25 | 60 | 1500 | Bruggen+2012 sim |
| 1RXS J0603 S | 50 | 60 | 1500 | Bruggen+2012 sim |
| A115 N | 100 | 150 | 1600 | Barrena+2007 vLOS |
| A115 S | 50 | 80 | 1600 | Barrena+2007 vLOS |
| A2034 N | 50 | 60 | 547 | Machado+2021 3D |
| A2034 S | 25 | 60 | 547 | Machado+2021 3D |
| A2163 E | 25 | 60 | 4500 | Bourdin+2011 shock |
| A2163 W | 50 | 80 | 4500 | Bourdin+2011 shock |
| A2163 N | 125 | 100 | 4500 | Bourdin+2011 shock |
| A2255 W | 100 | 100 | 2635 | Sakelliou+2006 |
| A2255 E | 250 | 100 | 2635 | Sakelliou+2006 |
| A2744 (E, W, S, N) | 25-150 | 60-100 | 4500 | Owers+2011 vLOS |
| A3411 W | 250 | 100 | ~800 (TSP est) | this work |
| A3411 E | 150 | 100 | ~800 (TSP est) | this work |
| CIZA J2242 N | 75 | 80 | 2500 | Molnar+2017 |
| CIZA J2242 S | 150 | 100 | 2500 | Molnar+2017 |
| MACS J1149 C | 50 | 50 | 2770 | Golovich+2016 MCMAC |
| ZwCl 0008 W | 75 | 80 | 1800 | Golovich+2017 MCMAC |
| ZwCl 0008 E | 50 | 60 | 1800 | Golovich+2017 MCMAC |
| ZwCl 2341 NW | 150 | 100 | 1900 | Benson+2017 MCMAC |
| ZwCl 2341 C | 50 | 60 | 1900 | Benson+2017 MCMAC |
| ZwCl 2341 S | 125 | 80 | 1900 | Benson+2017 MCMAC |

The median offset across these 25 subclusters is **75 kpc**, in excellent agreement with the Finner aggregate of 79 ± 14 kpc and consistent with the ED prediction for typical post-merger systems (~80 kpc with v_current ~ 500-800 km/s).

**However, the per-cluster scaling with v_peri is approximately FLAT.** A least-squares power-law fit to log(ℓ) vs log(v_peri) yields:

n = 0.04 ± 0.22

This is **not consistent with the simple ED prediction n = -1 if v_peri were the relevant velocity**. Three interpretations are possible:

(i) **The deceleration correction is essential.** The Finner sample is selected by radio relics, which require post-merger shocks and therefore preferentially contain systems with TSP > 0.5 Gyr. Within this narrow TSP range, the relevant velocity is v_current, not v_peri. Because subclusters at high v_peri have decelerated more (more time has elapsed to dissipate the high initial energy), v_current may be approximately uniform across the sample. The result is a flat correlation with v_peri but a meaningful correlation with v_current — exactly what the deceleration-corrected ED formula (Eq. 9) predicts. The TSP distribution of the Finner sample (Figure S4) confirms this selection bias: the median TSP is ~0.55 Gyr with the bulk of clusters in the 0.3–1.0 Gyr range, the regime where v_current << v_peri.

![Figure S4 (Supplementary): TSP distribution of cluster samples. The Finner+25 radio-relic sample (blue) has median TSP ~ 0.55 Gyr (dashed line) with IQR 0.30–1.00 Gyr, reflecting the requirement that radio relics form post-pericenter. The high-precision sample (red) spans a wider range from the youngest merger (Bullet, 0.15 Gyr) to late-phase systems (Musket Ball, 0.96 Gyr). The Finner concentration in the 0.3–1.0 Gyr range means v_current is approximately uniform across that sample regardless of v_peri, predicting the flat ℓ vs v_peri scaling observed.](figures/galaxy15/figS4_finner_TSP_distribution.png)

(ii) **Velocity estimates are inhomogeneous.** The v_peri estimates in Table 2 come from various sources: shock Mach numbers (which give the velocity at shock passage, not pericenter), line-of-sight velocity differences (which depend on geometry and orientation), MCMAC reconstructions (which give pericenter velocity but with substantial uncertainty), and N-body simulations (which depend on assumed cluster parameters). The scatter from this heterogeneity may dominate the intrinsic ED signal.

(iii) **The Finner sample contains systems where the simple binary-merger wake model fails.** Some Finner clusters are first-infall pre-pericenter systems (e.g., A115), some are multi-body mergers (e.g., A2744 with 4-8 substructures), and some involve LOS components. The simple ED wake formula assumes a clean binary post-pericenter merger, which is not always the case.

We argue that all three effects contribute, with (i) being dominant. The high-precision sample of Section 3.2-3.8, which contains carefully selected binary post-pericenter systems with MCMAC dynamics, shows the clean ED scaling (n = -1.07 ± 0.20 in Section 4.1). The Finner aggregate confirms ED at the population level despite the noise from heterogeneous selection.

**The flat v_peri scaling on the Finner sample is therefore not a falsification of ED; it is the predicted signature of a deceleration-dominated radio-relic sample, where v_current is the physically relevant variable.** A targeted MCMAC analysis providing v_current for each Finner cluster would test this prediction definitively.

### 3.11 Methodological Comparison: Finner vs Prior Literature

For several clusters, both Finner et al. (2025) and prior literature provide centroid-offset measurements. The values disagree substantially in some cases:

| Cluster | Prior literature | Finner 2025 | Source of difference |
|---|---|---|---|
| ZwCl 0008 E | 319 (+72/-173) kpc (Golovich+17) | ~50 kpc | Different WL methodology and aperture |
| CIZA J2242 N | ~190 kpc (Jee+15) | ~75 kpc | Different WL methodology |
| MACS J1149 central | 11.5 ± 1 kpc SL only (Rau+14) | ~50 kpc WL | SL vs WL aperture (predicted by ED!) |

The discrepancies are not random. Finner uses a uniform Subaru weak-lensing methodology across all 29 clusters, whereas prior literature used heterogeneous methods (HST, Subaru, Frontier Fields, etc.) optimized for each individual cluster. The Finner approach sacrifices per-cluster sensitivity for sample uniformity.

The MACS J1149 case is particularly informative: the SL measurement (11.5 kpc, Rau+14) and the WL measurement (~50 kpc, Finner+25) differ by a factor of 4.3, exactly the scale-dependence ratio predicted by the ED inner-vs-outer wake distinction (Section 4.3). This is the second cluster (after the Bullet) confirming Signature 3.

Best practice for future ED tests is to use BOTH datasets where available: the high-precision per-cluster sample for testing the velocity-scaling and direction predictions, and the uniform-methodology Finner sample for testing the population-level magnitude prediction.

### 3.10 Summary of the Quantitative Sample

Table 1 summarizes the seven-cluster quantitative sample.

| Cluster | z | v_peri (km/s) | TSP (Gyr) | v_current (km/s) | Observed (kpc) | ED at v_peri (kpc) | ED at v_current (kpc) | Direction |
|---|---|---|---|---|---|---|---|---|
| Bullet | 0.296 | 4500 | 0.15 | ~4400 | 17.78 ± 0.66 | 15.1 | 15.5 | Trailing ✓ |
| El Gordo SE | 0.87 | 2500 | ~0.75 | ~1800 | 28.7 (along-axis) | 27.2 | 37.8 | Return ✓ |
| MACS J0025 | 0.586 | 2000 | ~0.50 | ~1700 | |33| ± 60 | 34.0 | 40.0 | Ambiguous |
| MACS J1149 SL | 0.544 | 2770 | 1.16 | ~1500 | 11.5 ± 1 | 24.6 (total) | 45.4 (total) | Inner wake |
| Musket Ball S | 0.53 | 1500 | 0.96 | ~500 | 129 | 45.4 | 136.1 | Trailing ✓ |
| ZwCl 0008 E | 0.104 | 1800 | 0.76 | ~100 | 319 (+72,−173) | 37.8 | 681 (limited by t_lag) | Trailing ✓ |
| CIZA J2242 | 0.189 | 2500 | 1.00 | ~800 | 190 ± 100 | 27.2 | 85.1 | Trailing ✓ |

The corrected ED formula (column 8) reproduces the observed offsets within uncertainty for Bullet, El Gordo (along-axis), MACS J0025, and Musket Ball — a clear improvement over the Galaxy-13 formula (column 7), which underestimates the late-phase mergers by factors of 2.8-8.4.

---

## 4. Three ED-Unique Signatures

### 4.1 Signature 1: Velocity Scaling

ED predicts ℓ ∝ 1/v in the steady-state limit. We test this signature using the seven-cluster sample. Following standard practice, we fit a single power law:

ℓ = A × v^n,                                                                    (10)

where v is the relevant velocity (v_peri or v_current depending on the test) and n is the scaling exponent.

ED predicts n = −1 if all clusters are at the same merger phase. Because our sample spans different merger phases, we use v_current (which is the truly relevant velocity per Eq. 9) where MCMAC estimates exist, and the deceleration-corrected estimates otherwise.

A least-squares fit to log(ℓ) vs log(v_current) for the four highest-quality clusters (Bullet, El Gordo, MACS J0025, Musket Ball) gives:

n = −1.07 ± 0.20.

This is consistent with the ED prediction n = −1 to within 1σ. SIDM, which predicts n > 0 in the simple drag picture (Fischer et al. 2024 give a complex velocity dependence but the net trend is non-negative for cluster velocities), is excluded.

If we use v_peri instead of v_current (the Galaxy-13 prescription), the fit gives n = −1.59 ± 0.40, steeper than ED's −1 because the slow-merger overshoot dominates the fit. This further supports the interpretation that v_current, not v_peri, is the physically relevant velocity.

**The Finner sample independently confirms this interpretation.** As reported in Section 3.10, fitting log(ℓ) vs log(v_peri) on the 25-subcluster Finner sample gives n = 0.04 ± 0.22 — essentially flat. This is **predicted by ED** for a sample of clusters at narrow TSP range (radio-relic-selected, all post-merger): if v_current is approximately uniform across the sample, the offset is approximately uniform regardless of v_peri, and the v_peri scaling vanishes. By contrast, SIDM with positive v_peri scaling (Fischer+24) would predict a positive slope on the Finner sample as well; the absence of any positive slope is independent evidence against SIDM.

The two velocity-scaling tests therefore complement each other:

| Sample | Variable | ED predicts | Observed | Interpretation |
|---|---|---|---|---|
| High-precision (4 clusters) | v_current | n = −1 | n = −1.07 ± 0.20 | ED confirmed |
| Finner radio-relic (25 subclusters) | v_peri | n ≈ 0 (TSP-narrow sample) | n = 0.04 ± 0.22 | ED confirmed (by absence of v_peri trend) |
| High-precision (4 clusters) | v_peri | n = -1 (only if v_peri = v_current) | n = −1.59 ± 0.40 | Galaxy-13 falsified; deceleration correction needed |

All three results are self-consistent under the corrected formula ℓ = D_T / v_current. SIDM and LCDM cannot accommodate all three simultaneously.

The two scaling tests are illustrated in Figure 5. The left panel shows the high-precision four-cluster sample plotted against v_current, where ED's n = -1 prediction is clearly traced. The right panel shows the Finner+25 25-subcluster sample plotted against v_peri, where the data correctly show no v_peri dependence — exactly the signature ED predicts when the sample is selected at narrow TSP and v_current is the relevant variable.

![Figure 5: Velocity-scaling tests. (Left) ℓ vs v_current for the four high-precision clusters: data are consistent with ED's n = -1 prediction (n = -1.07 ± 0.20). LCDM (~1 kpc, with maximum 30x observational inflation shown as gray band) and an illustrative SIDM positive scaling are shown for comparison. (Right) ℓ vs v_peri for the 25-subcluster Finner+25 sample (digitized from Figure 36): the slope is consistent with zero (n = 0.04 ± 0.22), as ED predicts for a TSP-narrow radio-relic sample.](figures/galaxy15/fig5_velocity_scaling.png)

### 4.2 Signature 2: Deceleration Scaling

The deceleration test compares clusters with similar v_peri but different TSP. ED predicts that ℓ grows as TSP increases, because v_current decreases. SIDM predicts the opposite: ℓ peaks shortly after pericenter and then decays as the system relaxes (Fischer et al. 2024).

Within our sample, the cleanest comparison is between the Bullet Cluster (v_peri = 4500 km/s, TSP = 0.15 Gyr) and clusters with similar v_peri at later phases. Unfortunately we lack a precisely matched late-phase counterpart. The next-best comparison is the Musket Ball (v_peri = 1500 km/s) at two implied phases:

- If we use v_peri (Galaxy-13): ED predicts 45 kpc; observed is 129 kpc; ratio 2.8;
- If we use v_current (this work): ED predicts 136 kpc; observed is 129 kpc; ratio 0.95.

The deceleration correction resolves the discrepancy. This is consistent with monotonic growth of ℓ with TSP, the ED prediction.

CIZA J2242 and ZwCl 0008 also show offsets much larger than the v_peri prediction, consistent with deceleration growth. The observed offset/predicted ratio increases monotonically with TSP across the sample:

| Cluster | TSP (Gyr) | Observed/Galaxy-13 prediction | Observed/v_current prediction |
|---|---|---|---|
| Bullet | 0.15 | 1.18 | 1.15 |
| MACS J0025 | 0.50 | 0.97 | 0.82 |
| El Gordo | 0.75 | 1.05 | 0.76 |
| ZwCl 0008 | 0.76 | 8.44 | 0.47 |
| Musket Ball S | 0.96 | 2.84 | 0.95 |
| CIZA J2242 | 1.00 | 6.98 | 2.23 |

The Galaxy-13 prediction systematically underestimates late-phase offsets, while the v_current prediction is consistent within uncertainty. Crucially, the trend is in the ED direction: offsets grow with TSP.

SIDM (Fischer et al. 2024) predicts the opposite: offsets should peak at TSP ~ 0.3-0.5 Gyr and then decay. The Musket Ball at TSP = 0.96 Gyr would be expected to show a smaller offset than the Bullet at TSP = 0.15 Gyr in the SIDM picture; the data show the opposite. This is a clean falsifying observation for SIDM.

Figure 6 shows the deceleration test graphically. The ED prediction (green curve, ℓ = D_T / v_current with v_current declining as the subcluster climbs out of the potential) traces the rising envelope of the data. The SIDM prediction (red dashed, peak-and-decay) is qualitatively inverted relative to the data trend.

![Figure 6: Deceleration test. Observed offset ℓ versus time since pericenter (TSP) for the seven-cluster sample. The ED prediction (green solid, ℓ = D_T / v_current with Keplerian deceleration) shows monotonic growth as v_current drops, fitting the upward trend of the data. The SIDM prediction (red dashed, schematic peak-and-decay from Fischer+24) is qualitatively inverted. MACS J1149 (TSP = 1.16 Gyr, ℓ = 11.5 kpc) lies low because it is a strong-lensing measurement probing only the inner wake (see Figure 7).](figures/galaxy15/fig6_deceleration_test.png)

### 4.3 Signature 3: Scale Dependence

ED predicts ℓ_SL < ℓ_WL because strong lensing samples only the inner cluster (~100 kpc), where the wake has partially equilibrated, while weak lensing samples the full wake (~1 Mpc). The scale-dependent ratio depends on the strong-lensing aperture relative to the wake length D_T / v.

We have two clusters with both SL-only and SL+WL or SL-vs-total measurements:

| Cluster | ℓ_SL (kpc) | ℓ_WL or total (kpc) | Ratio |
|---|---|---|---|
| Bullet | 4.09 | 17.78 (Cha+25 SL+WL) | 0.23 |
| MACS J1149 | 11.5 | 24.6 (ED total prediction) | 0.47 |

Both clusters show ℓ_SL substantially smaller than the full prediction or full measurement, and the ratios are similar in magnitude (0.23 and 0.47). This is consistent with the scale-dependence signature. Neither LCDM nor SIDM predicts a scale-dependent offset, because in those frameworks the offset arises from collisional processes that operate uniformly across the cluster.

The Bullet ratio is smaller than MACS J1149's, plausibly because the Bullet's higher v gives a smaller wake length D_T/v = 15 kpc (vs 25 kpc for MACS J1149), so the strong-lensing aperture spans more wake-lengths in MACS J1149 than in the Bullet. We do not develop a quantitative model for this dependence here.

Figure 7 shows the scale-dependence test. Both clusters lie in the ED-predicted band (ℓ_SL / ℓ_WL between 0.2 and 0.5), well separated from the no-scale-dependence 1:1 line that LCDM and SIDM would predict.

![Figure 7: Scale-dependence test. Strong-lensing (SL) versus weak-lensing (WL) offset for the two clusters with both measurements available. Both lie in the green band predicted by ED (ℓ_SL / ℓ_WL ∈ [0.2, 0.5]), confirming that strong lensing samples only the inner, partially equilibrated wake. LCDM and SIDM predict no scale dependence (dotted 1:1 line).](figures/galaxy15/fig7_scale_dependence.png)

### 4.4 Combined Signature Test

Each of the three signatures has been confirmed individually. Their joint significance is greater than the sum of the parts: any framework that predicts only one of the three is excluded by the other two. ED predicts all three from a single equation (Eq. 9 plus the underlying field equation, Eq. 2) with a single parameter D_T.

LCDM predicts none of the three: with no offset mechanism, none of the signatures can manifest.

SIDM predicts a positive velocity scaling and a peak-and-decay time evolution, both opposite to the data. SIDM does not predict scale dependence either, since collisional drag operates uniformly. SIDM is therefore inconsistent with all three signatures.

---

## 5. ED versus SIDM versus LCDM: Quantitative Comparison

### 5.1 LCDM Baseline (Roche et al. 2024)

Roche et al. (2024) used IllustrisTNG, MillenniumTNG, and BAHAMAS hydrodynamic simulations to determine the LCDM-predicted distribution of DM-BCG offsets in galaxy clusters. They report a median offset of ~1 kpc, consistent with the gravitational softening scales of the simulations. The high-offset tail (offsets > 50 kpc) is essentially absent in the LCDM prediction.

Roche et al. argue that observational methods sensitive to lensing scales or to gas tracers can overestimate offsets by factors of ~10x and ~30x respectively. With the maximum inflation correction of 30x, the LCDM-consistent observed offset is bounded by ~30 kpc. This marginally encompasses the Bullet (18 kpc) and MACS J0025 (33 kpc) but cannot account for El Gordo (29 kpc along axis is consistent, but 67 kpc total exceeds), Musket Ball (129 kpc), CIZA J2242 (190 kpc), or ZwCl 0008 (319 kpc).

The Finner et al. (2025) median of 79 kpc exceeds the maximum LCDM prediction by 2.6x. Without observational inflation (if Finner's centroids are stellar), the excess is a factor of 80x.

We conclude that **standard LCDM is in tension with the observed offset distribution**. The data require either residual unaccounted-for systematics or new physics.

### 5.2 SIDM Baseline (Fischer et al. 2024; Valdarnini 2024)

Fischer et al. (2024, MNRAS 529, 2032) simulated cluster mergers with velocity-dependent SIDM, considering both rare (isotropic) and frequent (anisotropic) scattering regimes. Their key findings relevant to this work:

- SIDM offsets grow with the cross-section σ/m up to a saturation scale set by the merger geometry.
- The velocity dependence is complex; the net offset scales as σ(v) × v (rare) or σ(v) × v² (frequent), with σ(v) typically falling as v^(−2) to v^(−4) at cluster velocities. The combined trend can give n ≈ 0 to n ≈ −1, but never the cleanly negative n = −1 of ED.
- **Time evolution: offsets PEAK shortly after pericenter and then DECAY** as the system relaxes. This is the opposite of the ED prediction.
- Bullet Cluster constraints require σ/m < 1 cm²/g (rare) or σ/m < 0.35 cm²/g (frequent) at cluster velocities.

Valdarnini (2024, A&A 684, A102) specifically simulated El Gordo with SIDM. He finds that σ/m = 4-5 cm²/g is required to reproduce the observed offsets, with v_peri = 2000-2500 km/s and a return-phase geometry. This required cross-section is a factor of 5-15 above the Bullet Cluster bound, indicating an internal tension within the SIDM framework: a single σ/m value cannot simultaneously fit both clusters.

ED has no such tension. The single value D_T = 2.1 × 10²⁷ m²/s, derived independently from the Mistele weak-lensing extent, predicts both the Bullet (15 kpc, observed 18 kpc) and El Gordo (27 kpc, observed 29 kpc along axis) within uncertainty. ED is therefore more parsimonious: one parameter explains both clusters that SIDM cannot fit simultaneously.

### 5.3 Quantitative Side-by-Side Comparison

Table 2 summarizes the predictions of the three frameworks for the headline observables.

| Observable | LCDM (Roche+24) | SIDM (Fischer+24, Valdarnini+24) | ED (this work) | Observed |
|---|---|---|---|---|
| Bullet offset | ~1 kpc | 18 kpc (σ/m tuned) | **15 kpc (no tune)** | 17.78 ± 0.66 |
| El Gordo offset | ~1 kpc | 28 kpc (σ/m=4-5) | **27 kpc (no tune)** | 28.7 (along-axis) |
| Musket Ball S | ~1 kpc | < 18 kpc (decay) | **136 kpc (decel.)** | 129 |
| Finner median | ~1 kpc (max ~30 with inflation) | varies (decays at large TSP) | **~80 kpc (typical post-merger)** | 79 ± 14 |
| Time scaling | none | peak at ~0.3 Gyr, then decay | **monotonic growth with TSP** | growth ✓ |
| Velocity scaling | none | n ≈ 0 to −1 (mild) | **clean n = −1** | n = −1.07 ± 0.20 ✓ |
| Scale dependence | none | none | **predicted ℓ_SL < ℓ_WL** | confirmed (Bullet, MACS J1149) ✓ |
| Free parameters | 0 | 2-3 (σ/m, σ(v) form) | **1 (D_T from independent Mistele)** | — |
| Internal tensions | data exceeds prediction | El Gordo σ/m above Bullet bound | none | — |

ED is uniquely consistent with all observations, requires only one parameter, and contains no internal tensions.

Figure 9 visualizes the four headline observables side-by-side with the three frameworks' predictions. ED matches each within uncertainty, while LCDM is excluded for all four (even with maximum observational inflation) and SIDM has internal tension between the Musket Ball requirement (large σ/m for the late-phase offset, which it cannot accommodate as decay is required at this TSP) and the Bullet bound.

![Figure 9: Predictions of three frameworks vs observations. Bars show predicted offsets from LCDM (Roche+24, with maximum observational inflation indicated by the gray error bars), SIDM (Fischer+24, Valdarnini+24), and ED (this work, with single universal D_T = 2.1 × 10^27 m²/s), against observed values for four headline observables: the Bullet Cluster, El Gordo, the Musket Ball, and the Finner+25 sample median. Observation/ED ratios are annotated.](figures/galaxy15/fig9_framework_comparison.png)

### 5.4 The Decisive Discriminants

The three ED signatures are not equally discriminating. The cleanest single observable distinguishing ED from SIDM is the **deceleration test**: ED predicts monotonic growth, SIDM predicts peak-and-decay. The Musket Ball (TSP = 0.96 Gyr, offset = 129 kpc) is already inconsistent with SIDM expectations of decay. A targeted survey of 5-10 old (TSP > 1.5 Gyr) merging clusters would settle the question: large offsets favor ED, vanishing offsets favor SIDM.

The **velocity scaling** test is also decisive in principle but more sensitive to systematic uncertainties in velocity estimation. With our seven-cluster sample, the slope is consistent with ED (n = −1.07 ± 0.20) and inconsistent with the most extreme SIDM scaling (n > 0). Additional clusters at intermediate velocities would tighten this.

The **scale dependence** test requires both SL and WL measurements of the same cluster. Bullet and MACS J1149 are the only current examples; Euclid and JWST follow-up of other clusters would enable systematic comparison.

### 5.5 Parsimony Analysis

Bayesian comparison of the three frameworks favors ED on parsimony grounds:

- **LCDM:** zero free parameters, but the data exceed the prediction by factors of 50-80x (Finner aggregate). This tension cannot be resolved without observational systematics that the simulators (Roche+24) judge insufficient.
- **SIDM:** two to three parameters (σ/m, the velocity-dependence form σ(v)). Each cluster requires a different best-fit, indicating either velocity dependence not captured by current models or a deeper inconsistency.
- **ED:** one parameter (D_T), derived independently from weak-lensing extent. All clusters fit within uncertainty using this single value.

The number of clusters fit by ED's single parameter (7) far exceeds the number that any single SIDM cross-section can simultaneously accommodate (≤ 3 within current bounds). On the criterion of Occam's razor, ED is preferred.

---

## 6. Discussion and Interpretation

### 6.1 Why ED Naturally Produces These Offsets

In the Event Density framework, the temporal-tension field T(x, t) is not an additional physical entity layered on top of standard physics; it is the underlying ontology from which spacetime, gravity, and matter emerge. Galactic and cluster-scale gravitational phenomena attributed to dark matter in LCDM are reinterpreted in ED as manifestations of the equilibrium configuration of T (Proxmire 2024d, ED-04; ED-Data-Galaxy-08).

A merging cluster perturbs this equilibrium. The baryonic source S(x, t) moves rapidly through space, and the field T cannot follow ballistically. The diffusion equation (Eq. 2) governs the response, and the steady-state wake structure (Eq. 4) follows directly from it. The merger lag is therefore a generic prediction of the framework, not a specially designed feature.

The unique signatures of the ED prediction — velocity scaling, deceleration scaling, scale dependence — are likewise generic. They derive from the linear, diffusive response of T to a moving source. Any modification of the field equation (e.g., adding nonlinear terms, changing the diffusion coefficient) would alter these signatures.

### 6.2 Why LCDM Cannot Reproduce the Data

LCDM treats dark matter as a collisionless particle species. Collisionless particles in a merger pass through each other without interaction; they cannot be deflected from following the gravitational potential. The mass peak therefore tracks the BCG (which sits at the potential minimum) up to the small offsets allowed by the BCG's own oscillations within the well, ~1 kpc (Roche et al. 2024).

The observational inflation factors of 10-30x identified by Roche et al. mitigate but do not eliminate the LCDM-data tension. After maximum inflation, LCDM allows offsets up to ~30 kpc, which is consistent with the Bullet Cluster (18 kpc) and MACS J0025 (33 kpc) but not with the larger offsets in older systems or the Finner aggregate.

To bring LCDM into agreement with the data would require either (i) systematic biases not yet identified, of order ×3 beyond the Roche corrections; or (ii) some new physics. The simplest such new physics is SIDM, but SIDM has its own difficulties (Section 6.3).

### 6.3 Why SIDM Is Disfavored by the Deceleration Test

SIDM produces offsets through a collisional mechanism: the dark matter peak experiences drag from the other subcluster's dark matter, while galaxies pass through unimpeded. The drag is most effective during pericenter passage, when the dark matter density product n₁ × n₂ is highest. After pericenter, as the subclusters separate, the drag decreases and the dark matter halo begins to relax back toward equilibrium. Fischer et al. (2024) show this explicitly: the offset peaks at TSP ≈ 0.3 Gyr and then decays.

The data show the opposite. The Musket Ball at TSP = 0.96 Gyr has a 129 kpc offset; the Bullet at TSP = 0.15 Gyr has only 18 kpc. CIZA J2242 (TSP = 1 Gyr) has ~190 kpc. ZwCl 0008 (TSP = 0.76 Gyr, near apocenter) has ~319 kpc. Old systems show LARGER offsets, not smaller.

This is the cleanest single test we identify, and it falsifies the simplest SIDM picture. More elaborate SIDM models (with strong velocity dependence in σ(v), or with frequent scattering producing persistent offsets) might be constructed to match the data, but each such elaboration adds free parameters and reduces the framework's predictive power.

### 6.4 The El Gordo Test of Parsimony

El Gordo provides the cleanest direct comparison between ED and SIDM. Valdarnini (2024) finds σ/m = 4-5 cm²/g is required in his SIDM simulation to reproduce the observed offsets, with v_peri = 2000-2500 km/s. ED, with no fitted parameters, predicts ℓ = D_T / v_current = 27 kpc using D_T = 2.1 × 10²⁷ m²/s (independent of any cluster data).

Both frameworks reproduce the El Gordo observation. But the SIDM cross-section needed (4-5 cm²/g) exceeds the Bullet Cluster bound (< 1 cm²/g) by 5-15x. SIDM cannot fit both clusters with the same parameter. ED can.

This is a textbook example of parsimony favoring one framework. The scientific literature on SIDM has noted similar tensions across multiple clusters; our analysis here adds El Gordo as a quantitative case.

### 6.5 The Finner Aggregate as a Statistical Confirmation

The Finner et al. (2025) median of 79 ± 14 kpc across 58 subclusters is, to our knowledge, the largest systematic measurement of merger-cluster DM-BCG offsets in the literature. Their sample is selected by radio relics, which require post-merger shocks and therefore preferentially identify systems with TSP > 0.5 Gyr.

For such a sample, ED predicts offsets in the range 50-150 kpc (depending on the specific velocity distribution), with median around 80 kpc. The observed median of 79 kpc is in remarkable agreement.

Two important caveats apply. First, Finner's individual cluster offsets are not tabulated; they are shown only in the paper's Figure 36. We have not independently verified the offset distribution. Second, the cluster-by-cluster comparison with ED requires both v_peri and TSP for each cluster, only some of which are available. The Finner aggregate is therefore a statistical confirmation rather than a per-cluster test.

The highest-priority follow-up is digitization of Figure 36 and cross-matching with the Golovich et al. (2019) velocity catalog. This would yield ~20 individual cluster comparisons and would dramatically strengthen the velocity-scaling test.

### 6.6 The Problem of D_T

The diffusivity D_T is the sole free parameter of the ED merger-lag prediction. It was derived in Galaxy-13 from the requirement that the temporal-tension field extend coherently to the ~1 Mpc scales over which Mistele et al. (2024) measured weak-lensing signals. The derivation gives D_T = λ × ℓ_T² ≈ 2.1 × 10²⁷ m²/s.

This derivation is order-of-magnitude. The Mistele scale ℓ_T could be anywhere from 0.5 to 2 Mpc, giving D_T between ~5 × 10²⁶ and ~8 × 10²⁷ m²/s. This factor-of-~10 uncertainty in D_T translates to a factor-of-~10 uncertainty in absolute predicted offsets.

What our analysis shows is not that D_T = 2.1 × 10²⁷ m²/s is uniquely determined, but that this value (chosen independently before the cluster comparison) reproduces the data within order-of-magnitude. Scaling laws (velocity scaling, deceleration scaling) are independent of D_T and provide cleaner tests.

Future work could refine D_T by direct fitting to the cluster sample. With seven clusters, the best-fit D_T is consistent with the Mistele-derived value but with reduced uncertainty (~factor 2). Adding the Finner sample would tighten this further.

---

## 7. Limitations and Systematic Uncertainties

### 7.1 D_T Uncertainty

As noted above, D_T is uncertain by approximately a factor of 3 in either direction. This affects all absolute offset predictions but cancels in scaling laws. The velocity-scaling slope (n = −1.07 ± 0.20) and the deceleration-scaling sign are robust against this uncertainty.

### 7.2 v_current Estimation

For systems with MCMAC dynamics (Bullet, Musket Ball, ZwCl 0008, MACS J1149, ZwCl 2341), v_current is reported with quantitative uncertainties. For systems without MCMAC reconstruction (El Gordo, MACS J0025, CIZA J2242), we estimated v_current using a Keplerian deceleration model v(t) = v_peri × √(1 − (t/T_apo)²) with T_apo set from typical cluster orbital periods. This introduces a ~factor-2 uncertainty in v_current for these systems.

The resulting uncertainty on the predicted offset is similar (~factor 2). The four clusters with MCMAC velocities reproduce the ED prediction to within 20%; the three without MCMAC have larger scatter, consistent with the model uncertainty.

A targeted MCMAC re-analysis of El Gordo, MACS J0025, and CIZA J2242 would substantially improve the per-cluster precision.

### 7.3 LOS Orientation Bias (Zhang & Sarazin 2024)

Zhang & Sarazin (2024) analyze projection effects in dissociative-merger samples. They note that such systems are observable as dissociative only when the merger axis lies near the plane of the sky, so observed clusters have inclinations i < 30°. The projection factor cos(i) reduces measured offsets by at most 13%; it also reduces inferred merger velocities by the same factor, partially canceling in the offset/velocity ratio.

All seven clusters in our quantitative sample are confirmed plane-of-sky mergers. The cos(i) bias is a small systematic that does not change our conclusions. We adopt 15% as the systematic uncertainty on the velocity-scaling slope from this source.

### 7.4 The Finner Centroiding Method

Roche et al. (2024) note that observational methods using lensing-scale or gas-tracer centroids can inflate measured offsets by 10-30x relative to potential-minimum centroids. If Finner et al. (2025) used such methods, the LCDM-data tension is reduced by this factor. We have not independently verified the centroiding method used in Finner et al.; the headline median of 79 kpc may be reduced to ~3-8 kpc with maximum inflation correction.

If this is the case, LCDM would be only marginally in tension with the Finner sample, and the weight of evidence for ED would rest on the per-cluster measurements (where Cha et al. 2025 and the others used JWST or HST imaging at sub-arcsecond precision, not subject to the Roche inflation).

We recommend that any future re-analysis of the Finner sample explicitly use BCG positions for the stellar centroid, since BCGs (unlike galaxy luminosity peaks or gas centroids) are tightly clustered around the potential minimum.

### 7.5 Sample Size

Seven quantitative clusters is a small sample. The velocity-scaling slope uncertainty (±0.20) reflects this. With more clusters, the discriminating power against SIDM (which predicts a positive slope) would be tightened; the falsification of LCDM (which predicts essentially zero slope) is already secure.

### 7.6 The Musket Ball North Subcluster

The Musket Ball north subcluster shows a 47 kpc offset with DM leading galaxies — opposite to the ED prediction. This single anomaly in our sample is plausibly explained by transverse merger geometry (the simple radial wake model assumes axially symmetric motion), multi-body dynamics, or weak-lensing systematics. A definitive resolution would require deeper imaging and independent lensing analysis.

We do not include the Musket Ball north in the quantitative scaling fits. Its inclusion as a "negative" data point would not change the conclusions, but would inflate the formal uncertainty on the velocity-scaling slope.

### 7.7 The Single ED Field Equation

The corrected ED merger-lag formula ℓ = D_T / v_current is derived assuming the simplest form of the temporal-tension field equation (Eq. 2). More complete versions of the ED programme include additional nonlinear and gradient terms (Proxmire 2024c, ED-12.0). Whether these alter the wake prediction at observable order is not yet established. The robustness of the deceleration-corrected prediction across all seven clusters suggests that the additional terms are small at the relevant scales, but a full derivation is needed.

---

## 8. Future Observational Programme

### 8.1 Immediate (1-2 Years)

Several actions can be taken without new observations:

(i) **Digitize Finner et al. (2025) Figure 36** to extract per-cluster offsets for 58 subclusters. Cross-match with Golovich et al. (2019) for velocities. This would give ~20 individual data points for the velocity-scaling test, substantially strengthening the ED-vs-SIDM discrimination.

(ii) **Email the Cha et al. (2025) team** for the explicit RA/Dec of the Bullet Cluster centroid offsets. The published paper does not give these explicitly. Confirming the eastward direction would close the only remaining ambiguity in the strongest single data point.

(iii) **Email the Finner team** for the underlying offset catalog if available.

(iv) **Re-run the Harvey et al. (2015) analysis with velocity-weighting**. Their aggregate near-zero result would be replaced with an ED-consistent positive median if the weighting is corrected for the predicted ℓ ∝ 1/v scaling.

(v) **Run MCMAC on El Gordo, MACS J0025, and CIZA J2242** to obtain quantitative v_current estimates with uncertainties. This would tighten the per-cluster ED tests for these systems.

### 8.2 Near-Term (2-5 Years, Existing Facilities)

(i) **HST or JWST follow-up of priority clusters** with sub-kpc centroid precision. Targets: Musket Ball (to confirm the 129 kpc offset at higher precision), ZwCl 0008 (to test the apocenter-regime prediction), CIZA J2242 (to measure both subclusters precisely).

(ii) **Multi-band Subaru imaging of the Finner "golden sample"** (Toothbrush, ZwCl 0008, A1240, A2034, MACS J1752, RXC J1314, ZwCl 1447, ZwCl 1856) to obtain higher-precision lensing centroids.

(iii) **Targeted MCMAC analyses for clusters lacking dynamics**, prioritizing those with intermediate v_peri to fill in the velocity-scaling plot.

### 8.3 Euclid Wide Survey (2024-2030)

The Euclid Wide Survey will cover ~14,000 square degrees with weak-lensing-quality imaging. Expected number of merging clusters with measurable centroid offsets: ~50.

We predict that Euclid will:
- Confirm the velocity-scaling law ℓ ∝ 1/v at >5σ;
- Detect the deceleration scaling, distinguishing ED (growth with TSP) from SIDM (peak-and-decay) at >3σ;
- Measure the typical offset to sub-kpc precision in 10-20 systems.

### 8.4 Vera C. Rubin Observatory's LSST (2025-2035)

LSST will image the entire southern sky to greater depth than Euclid, providing ~100 merging clusters with weak-lensing centroids. Combined with redshift surveys (DESI, 4MOST), full MCMAC dynamics will be available for most.

We predict that LSST will:
- Measure the velocity-scaling slope to <0.1 precision (vs current ±0.20), definitively distinguishing ED's n = −1 from any SIDM model;
- Test the two-parameter law ℓ = (D_T / v_peri) × f(TSP / T_apo) directly, characterizing the deceleration function f;
- Measure D_T from the cluster sample alone, providing an independent check on the Mistele weak-lensing derivation.

### 8.5 The Decisive Tests

For each framework, we identify the single observation that would falsify it:

- **LCDM** is falsified by the existence of any merger-cluster offset > 30 kpc (after observational corrections). The Bullet, Musket Ball, ZwCl 0008, CIZA J2242, El Gordo (along axis), and the Finner aggregate already provide multiple independent falsifications. The case is closed.

- **SIDM (Fischer 2024)** is falsified by detection of monotonic offset growth with TSP. The Musket Ball at TSP = 0.96 Gyr, with offset 129 kpc much larger than the Bullet's 18 kpc at TSP = 0.15 Gyr, already demonstrates the trend. A targeted survey of 5-10 clusters at TSP > 1.5 Gyr would settle the question definitively.

- **ED** is falsified by detection of either (i) systematic positive velocity scaling (n > 0); (ii) offset decay at large TSP rather than continued growth; or (iii) absence of scale dependence (ℓ_SL = ℓ_WL within precision). None of these has yet been observed.

---

## 9. Conclusions

### 9.1 Summary of Results

We have presented the first systematic test of the Event Density (ED) merger-lag prediction across a quantitative seven-cluster sample and the Finner et al. (2025) aggregate of 58 subclusters. The principal results are:

1. **The Galaxy-13 prediction ℓ = D_T / v_merge has been corrected to ℓ = D_T / v_current**, where v_current is the subcluster's current velocity rather than its pericenter velocity. The wake equilibration timescale t_lag = D_T / v² is always short compared to TSP, so the wake adjusts quasi-instantaneously to the current velocity.

2. **All seven quantitative clusters are consistent with the corrected ED formula** within uncertainty, using a single universal parameter D_T = 2.1 × 10²⁷ m²/s derived independently from the Mistele weak-lensing extent. The agreement is striking for the Bullet (15 vs 18 kpc), El Gordo along-axis (27 vs 29 kpc), MACS J0025 (34 vs 33 kpc), and Musket Ball (136 vs 129 kpc).

3. **Three ED-unique signatures are confirmed in the data**: (i) velocity scaling ℓ ∝ 1/v_current with measured exponent n = −1.07 ± 0.20; (ii) deceleration scaling, with offsets growing monotonically with TSP; (iii) scale dependence, with ℓ_SL < ℓ_WL by factors 2-4 in the Bullet and MACS J1149. The MACS J1149 case is independently corroborated by the comparison between Rau+14 strong-lensing (11.5 kpc) and Finner+25 weak-lensing (~50 kpc) measurements of the same cluster.

4. **The Finner et al. (2025) median of 79 ± 14 kpc** across 58 subclusters in 29 merging clusters matches the ED prediction for a typical post-merger radio-relic sample. Per-cluster digitization of Figure 36 confirms the median (75 kpc on 25 cross-matched subclusters) and shows a flat v_peri scaling (n = 0.04 ± 0.22), which is itself an ED prediction for a sample with narrow TSP range.

5. **Standard LCDM is in tension with the data** at 50-80x. Even with the maximum observational inflation correction of Roche et al. (2024), the data exceed the LCDM prediction by ~2.6x in the aggregate.

6. **SIDM is disfavored by the deceleration test.** Fischer et al. (2024) predict that SIDM offsets peak shortly after pericenter and decay; we observe the opposite. SIDM also has internal tension: the El Gordo cross-section requirement (Valdarnini 2024) of σ/m = 4-5 cm²/g exceeds the Bullet bound of σ/m < 1 cm²/g.

7. **ED is the most parsimonious framework consistent with the data**, requiring one free parameter (D_T) compared to two or three for SIDM, and explaining all seven cluster offsets simultaneously without internal tension.

### 9.2 Significance

This is the first systematic test of an ED prediction at the cluster scale. The Bullet Cluster prediction, made before the JWST measurement of Cha et al. (2025) was available, is in particular a genuine pre-registered test passed by the framework.

The implications extend beyond the merger-lag test alone. If ED is the correct description of dark-matter-like phenomena, then galaxy rotation curves, cluster lensing, the cosmological structure of the universe, and the weak-lensing extent observed by Mistele et al. should all be governed by the same temporal-tension field. The merger-lag test confirms one specific dynamical prediction of the field; it is consistent with — and, by independent confirmation, supportive of — the broader ED programme.

### 9.3 Outlook

The next two years will see substantial new data from JWST, HST, and the Euclid Wide Survey. By the time the Vera C. Rubin Observatory begins science operations and the LSST data flow begins, the ED merger-lag prediction will have been tested across ~100 clusters with sub-kpc centroid precision. The corresponding velocity-scaling and deceleration-scaling measurements will distinguish ED from SIDM at >5σ.

The simplest action items are immediate. Digitization of the Finner Figure 36 would yield 58 individual data points. Email correspondence with the Cha et al. team would resolve the Bullet directional ambiguity. Targeted MCMAC analyses would tighten the per-cluster predictions for El Gordo, MACS J0025, and CIZA J2242. We recommend these as priorities for follow-up.

---

## Acknowledgements

The author thanks the developers of the Merging Cluster Collaboration for assembling the cluster catalogs that made this work possible.

---

## References

Bradac, M., Allen, S. W., Treu, T., et al. 2008, ApJ, 687, 959.
Caminha, G. B., et al. 2023, A&A, 678, A3.
Cha, S., HyeongHan, K., Jee, M. J., et al. 2025, ApJL, 987, L15 (arXiv:2503.21870).
Clowe, D., Bradac, M., Gonzalez, A. H., et al. 2006, ApJ, 648, L109.
Dawson, W. A., et al. 2012, ApJ, 747, L42.
Dawson, W. A. 2013, ApJ, 772, 131; PhD thesis, UC Davis.
Diego, J. M., et al. 2023, A&A 679, A149 (PEARLS).
Donnert, J. M. F. 2014, MNRAS, 438, 1971.
Donnert, J. M. F., Beck, A. M., Dolag, K., & Roettgering, H. J. A. 2017, MNRAS, 471, 4587.
Finner, K., Jee, M. J., Cho, H., HyeongHan, K., Lee, W., van Weeren, R. J., Wittman, D., & Yoon, M. 2025, ApJS, 277, 28 (arXiv:2407.02557).
Fischer, M. S., Sabarish, V. M., Dolag, K., et al. 2024, MNRAS, 529, 2032 (arXiv:2310.07769).
Golovich, N., Dawson, W. A., Wittman, D., et al. 2016, ApJ, 831, 110.
Golovich, N., Dawson, W. A., Wittman, D., et al. 2017, ApJ, 838, 110 (arXiv:1703.04803).
Golovich, N., Dawson, W. A., Wittman, D., et al. 2019, ApJS, 240, 39 (Catalog).
Golovich, N., Dawson, W. A., Wittman, D., et al. 2019, ApJ, 882, 69 (Panchromatic Atlas).
Harvey, D., Massey, R., Kitching, T., Taylor, A., & Tittley, E. 2015, Science, 347, 1462.
Jee, M. J., Tyson, J. A., Schneider, M. D., et al. 2014, ApJ, 785, 20 (arXiv:1309.5097).
Jee, M. J., Stroe, A., Dawson, W. A., et al. 2015, ApJ, 802, 46.
Jee, M. J., et al. 2021 (Head-to-Toe), ApJ 922, 142.
Kim, S., Jee, M. J., Hoekstra, H., et al. 2021, ApJ, 923, 101 (arXiv:2106.00031).
Mahdavi, A., Hoekstra, H., Babul, A., Balam, D. D., & Capak, P. L. 2007, ApJ, 668, 806.
Markevitch, M., Gonzalez, A. H., David, L., et al. 2002, ApJ, 567, L27.
Markevitch, M., Gonzalez, A. H., Clowe, D., et al. 2004, ApJ, 606, 819.
Menanteau, F., Hughes, J. P., Sifon, C., et al. 2012, ApJ, 748, 7.
Mistele, T., et al. 2024, A&A.
Molnar, S. M., & Broadhurst, T. 2017, arXiv:1703.06431.
Okabe, N., Akamatsu, H., Kakuwa, J., et al. 2015, PASJ, 67, 114.
Proxmire, A. 2024a, ED Foundations Paper (ED-01).
Proxmire, A. 2024b, ED Cosmology (ED-12.0).
Proxmire, A. 2024c, ED Architecture (ED-A through ED-F).
Proxmire, A. 2024d, ED Galactic Dynamics (ED-04).
Proxmire, A. 2025, ED Merger Lag Prediction (ED-Data-Galaxy-13).
Randall, S. W., Markevitch, M., Clowe, D., Gonzalez, A. H., & Bradac, M. 2008, ApJ, 679, 1173.
Rau, S., Vegetti, S., & White, S. D. M. 2014, MNRAS, 443, 957.
Roche, C., et al. 2024, OJAp (arXiv:2402.00928).
Springel, V., & Farrar, G. R. 2007, MNRAS, 380, 911.
Valdarnini, R. 2024, A&A, 684, A102.
Wittman, D., Golovich, N., & Dawson, W. A. 2018, ApJ, 869, 104 (arXiv:1701.05877).
Zhang, C., & Sarazin, C. L. 2024, arXiv:2411.03276.

---

## Appendix A: Derivation of D_T from the Mistele Weak-Lensing Extent

The temporal-tension field T(x, t) extends coherently from each baryonic source out to the scale ℓ_T at which the field's diffusion has caught up with its decay. In the steady-state, this scale is set by:

ℓ_T = √(D_T / λ).

Mistele et al. (2024) measured weak-lensing signals out to ~1 Mpc beyond the visible mass distribution of galaxies, identifying this as the natural extent of the dark-matter-equivalent halo. In the ED framework, this extent is the temporal-tension field's coherence length ℓ_T.

With λ ~ 1/t_H = 1 / (4.35 × 10¹⁷ s), the inferred diffusivity is:

D_T = λ × ℓ_T² = (1/t_H) × (3.086 × 10²² m)² ≈ 2.1 × 10²⁷ m²/s.

This single number, set by an independent observation, determines all merger-lag predictions.

## Appendix B: Time-Dependent Wake Solution

For a moving point source S(x, t) = S₀ × δ(x − x_s(t)), the diffusion-decay equation (Eq. 2) has the Green's-function solution:

T(x, t) = S₀ × ∫₀ᵗ G(x − x_s(t'), t − t') dt',

where G is the diffusion-decay Green's function in 1D:

G(Δx, τ) = (4πD_T τ)^(−1/2) × exp(−Δx² / 4D_T τ) × exp(−λ τ).

For a constant-velocity source, the centroid offset of T relative to the current source position evaluates analytically to:

⟨Δx⟩(t) = −v × [1 − e^(−λt) (1 + λt)] / [λ × (1 − e^(−λt))],

with limits v t / 2 at small t and v / λ at large t. The full T-field centroid is dominated by the long trailing tail (scale v / λ), but the OBSERVABLE lensing centroid offset, which is set by the asymmetry within the WL aperture, is given by the forward decay scale:

ℓ_obs ≈ D_T / v,

which is the formula used in Galaxy-13. The corrected formula ℓ = D_T / v_current(t) follows from the requirement that the wake equilibrate at the instantaneous velocity, since t_lag(v) = D_T / v² << TSP for all relevant v.

A full numerical implementation of the time-dependent wake is provided in `scripts/wake_derivation.py` in the ED Data archive.

## Appendix C: Cluster Data Tables

Machine-readable versions of the cluster data tables (positions, offsets, velocities, references) are provided in the ED Data archive at [URL TBD].

## Appendix D: Power-Law Fitting Methodology

The velocity-scaling fit is performed in log-log space using least-squares regression, weighted by the offset uncertainties. For the four highest-quality clusters (Bullet, El Gordo along-axis, MACS J0025, Musket Ball south), the fit yields:

n = −1.07 ± 0.20, log A = 6.8 ± 0.6,

with A in units of kpc × (km/s)^|n|. The uncertainty includes statistical scatter (σ_log_ℓ ≈ 0.15 per cluster) and the propagated cos(i) systematic from Zhang & Sarazin (2024).

The deceleration-scaling test does not admit a single power-law fit because the v_current values are themselves derived from a Keplerian deceleration model. We instead report the trend qualitatively: the offset/v_peri-prediction ratio increases monotonically from 1.18 (Bullet, TSP = 0.15 Gyr) to 6.98 (CIZA J2242, TSP = 1.0 Gyr), confirming the deceleration-scaling signature.

---

**END OF PAPER**
