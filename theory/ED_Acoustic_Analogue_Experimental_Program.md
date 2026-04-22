# ED Acoustic-Metric Analogue-Gravity Experimental Program

**Status.** Memo, 2026-04-22. Companion to [`ED_Effective_Acoustic_Metric.md`](ED_Effective_Acoustic_Metric.md), [`ED_Acoustic_Metric_Curvature.md`](ED_Acoustic_Metric_Curvature.md), and [`ED_Schwarzschild_Obstruction.md`](ED_Schwarzschild_Obstruction.md). Scope: experimental program, not new theory.

**One-line purpose.** Map ED's kinematic acoustic metric and its extremal-horizon result onto real analogue-gravity platforms (BEC, water-tank, optical pulse, slow-light EIT, phononic crystal), and identify which platforms can test which ED predictions.

**What this memo is / is not.**

- **Is:** a translation layer from ED primitives (`M(ρ_0), ρ_0, F[ρ]`) to analogue observables (`c_s(x), n(x), v_g(x)`); a per-platform list of experimental signatures; a taxonomy of what would falsify vs. support the ED reading.
- **Is not:** a derivation of GR dynamics, a claim that ED uniquely predicts κ = 0 at extremal points (it doesn't — that is a kinematic property of any acoustic metric with a smooth c_s maximum), or a rebadging of standard analogue gravity as ED. The ED-specific content is in *which systems* produce interior-maximum horizons and *why*, not in the geometric fact itself.

---

## 1. Analogue-gravity platforms overview

All five platforms below share the same underlying structure: a field (density, refractive index, group velocity, flow) varies across space; small fluctuations on top of that background propagate according to an effective Lorentzian metric whose null cones are set by a local signal speed. They differ in which physical field plays the role of `c_s` and in how horizons are engineered.

### 1.1 Bose-Einstein condensate (BEC) acoustic horizons

- **Underlying field:** condensate density `n(x)` and superfluid flow velocity `v(x)`.
- **Signal speed:** sound speed `c_s(x) = √(g·n(x)/m)` (Gross-Pitaevskii, dilute regime).
- **Horizon mechanism:** transonic crossing `v(x) = c_s(x)` — acoustic black hole (supersonic downstream) or white hole (supersonic upstream).
- **Reference experiments:** Steinhauer 2014, 2016, 2019 (stimulated and spontaneous Hawking-pair correlations in a flowing BEC).
- **Horizon type naturally produced:** monotonic (transonic crossing with `v − c_s` passing through zero linearly). **κ ≠ 0 generically.** Interior-maximum horizons require engineered trap profiles and are *not* the default.

### 1.2 Water-tank horizons (gravity waves on flowing water)

- **Underlying field:** water depth `h(x)` and flow velocity `v(x)`.
- **Signal speed:** long-wavelength gravity-wave speed `c_w(x) = √(g·h(x))`.
- **Horizon mechanism:** subcritical-to-supercritical flow transition `v = c_w` (e.g. over an obstacle).
- **Reference experiments:** Weinfurtner et al. 2011 (stimulated Hawking radiation at a white-hole horizon); Euvé et al. 2016 (spontaneous).
- **Horizon type naturally produced:** monotonic (driven by obstacle geometry). Interior-maximum horizons are possible with carefully shaped bathymetry but require fine-tuning.

### 1.3 Optical pulse analogues (refractive-index horizons)

- **Underlying field:** refractive-index profile `n(x, t)`, often a co-moving bright pulse.
- **Signal speed:** group velocity `v_g(x) = c/n_g(x)` in the pulse frame.
- **Horizon mechanism:** probe photons unable to overtake the pulse because the pulse locally raises the group index — horizon where `v_g,probe = v_pulse`.
- **Reference experiments:** Philbin et al. 2008 (fibre-optic analogue horizon); Belgiorno et al. 2010 (controversial: filament-induced blackbody claim).
- **Horizon type naturally produced:** **interior-maximum** if the pulse has a smooth bell-shape (e.g. Gaussian). The effective horizon sits at the pulse flank, but the refractive-index profile across the full pulse *is* an interior maximum. This is the most natural platform for ED's extremal-horizon class.

### 1.4 Slow-light / EIT media (group-velocity horizons)

- **Underlying field:** atomic coherence `ρ_ab(x)` controlled by an EIT control field, giving a position-dependent group velocity `v_g(x)`.
- **Signal speed:** `v_g(x)` for a probe pulse.
- **Horizon mechanism:** `v_g → 0` (stopped light) or `v_g = v_probe` in the co-moving frame.
- **Reference experiments:** Hau et al. 1999 (stopped light); theoretical proposals by Leonhardt & Piwnicki for EIT horizons.
- **Horizon type naturally produced:** adjustable — control-field shaping can produce monotonic or interior-maximum profiles at will. This is the **most experimentally controllable** platform for testing ED's extremal-horizon prediction.

### 1.5 Optomechanical / phononic crystals (engineered dispersion)

- **Underlying field:** periodic mechanical structure with engineered band gaps; local parameter modulation sets an effective dispersion relation.
- **Signal speed:** phonon group velocity near a band edge, which vanishes quadratically (`v_g ∝ √(ω − ω_edge)`).
- **Horizon mechanism:** position-dependent band edge — phonon cannot propagate into a region where its frequency is in the gap.
- **Reference experiments:** Aspelmeyer-group and others on engineered phononic crystals for cavity optomechanics (not yet exploited as analogue-horizon platforms at scale).
- **Horizon type naturally produced:** **extremal by construction.** Band-edge vanishing of `v_g` is smooth and symmetric; κ = 0 is the generic case, not the exception. This is the cleanest platform for confirming ED's extremal-horizon structure — but also the platform where the prediction is least distinctive.

---

## 2. Mapping ED → analogue variables

The ED acoustic metric derived in [`ED_Effective_Acoustic_Metric.md`](ED_Effective_Acoustic_Metric.md) is:

    g^eff_μν = diag(−M(ρ_0(x)), 1, 1, 1)    (v_0 = 0, F[ρ_0] = 0)

so ED-fluctuations propagate with local signal speed `c_s² = M(ρ_0(x))`.

### 2.1 Dictionary

| ED primitive | Analogue-gravity correspondent | Comment |
|---|---|---|
| Mobility `M(ρ_0(x))` | Local signal-speed-squared `c_s²(x)` | Direct identification in the v_0 = 0 class. |
| Density field `ρ_0(x)` | Condensate density / fluid depth / refractive index / control-field amplitude | Platform-specific; see §2.2. |
| Canon P4 mobility-collapse surface `M(ρ_0) = 0` | Signal-speed zero `c_s(x) = 0` | Horizon locus. |
| Interior-max P4 horizon (smooth local max of ρ_0 with M vanishing at the max) | Smooth interior maximum of `c_s(x)` where `c_s → 0` | Extremal class (κ = 0). |
| Stationarity `F[ρ_0] = 0, v_0 = 0` | Time-independent background, no background flow | ED restricts to this class; analogue platforms with v_0 ≠ 0 test a larger metric class (see §2.3). |
| Acoustic curvature `R[g^eff]` | Second derivative of `c_s²` in the propagation direction, `∂²_x c_s² / c_s²` (schematic) | Exact formula in [`ED_Acoustic_Metric_Curvature.md`](ED_Acoustic_Metric_Curvature.md) for the Gaussian-bump case. |
| Visser surface gravity `κ = (1/2)|∂_n c_s²|_horizon` | Same formula | Shared with analogue-gravity literature. |
| Hawking-analogue temperature `T_H = ℏκ/(2π k_B)` | Same formula | Shared. |

### 2.2 Per-platform mapping

| Platform | ED `ρ_0(x)` ↔ | ED `M(ρ_0)` ↔ |
|---|---|---|
| BEC | Condensate density `n(x)` | `g·n(x)/m` (linear in density, dilute regime) — *monotonic*, no natural mobility-collapse max |
| Water tank | Water depth `h(x)` | `g·h(x)` — *monotonic*, no natural collapse max |
| Optical pulse | Pulse refractive-index profile `n(x)` | `c²/n_g²(x)` — extremum at pulse peak |
| Slow light / EIT | Atomic coherence density | `v_g²(x)` — fully controllable |
| Phononic crystal | Position-dependent band-gap structure | Phonon group-velocity-squared near band edge — vanishes quadratically at edge |

**Critical observation.** The BEC and water-tank platforms have *monotonic* `M(ρ)` — the natural signal speed rises with the field. To realize an ED interior-maximum horizon in these systems, one must use transonic crossing with an engineered extremal flow profile, not a mobility-collapse zero. Optical pulse, slow light, and phononic-crystal platforms natively support ED's mobility-collapse structure.

### 2.3 What this mapping does not cover

The ED acoustic metric in its current (v_0 = 0) derivation is a **static** metric. Analogue-gravity experiments with background flow (`v_0 ≠ 0`) probe a richer metric class: `g^eff_μν` acquires off-diagonal `v·dx·dt` terms. Extending the ED derivation to moving backgrounds is deferred; the experimental program below focuses on the static class where the ED mapping is sharp. See §8 for the deferred extension.

---

## 3. The extremal-horizon prediction — what is ED-specific and what is not

This section is the most important for honesty about the experimental program. The claim "ED predicts κ = 0 at interior-maximum horizons" has a precise content that must not be oversold.

### 3.1 The geometric fact (not ED-specific)

If `c_s²(x)` has a smooth local maximum at `x = x_*` where `c_s²(x_*) = 0`, then `∂_x c_s²(x_*) = 0` (smoothness), and the Visser formula gives κ = 0. This is **a kinematic property of any acoustic metric**, not a prediction of ED. Any analogue-gravity framework using the same `g^eff` formula derives the same result.

### 3.2 The ED-specific content

ED's specific contribution is in **identifying which physical configurations natively produce interior-maximum horizons**. The ED-specific claims are:

1. **Canon P4 (mobility capacity) forces `M(ρ) → 0` at a structural maximum `ρ_max`** — mobility-collapse is native to ED's PDE architecture, not engineered. Analogue systems whose signal speed has an analogous structural zero (optical pulse peaks, EIT stopped light, phononic band edges) inherit the extremal-horizon behaviour.

2. **Stationary ED profiles `F[ρ_0] = 0` with mobility collapse at an interior point are generic.** Barenblatt-like solutions and their relatives produce smooth interior maxima of ρ_0 as the *natural* stationary configuration — not as fine-tuned exceptions. Thus ED *predicts* that mobility-dominated regimes populate the extremal-horizon class rather than the monotonic/transonic class.

3. **ED links multiple regimes under one PDE.** The same P4 collapse structure appears across condensed-matter (UDM), galactic (ED-XX), and quantum (ED-Dimensional-01) regimes. So an analogue-gravity test at one scale constrains ED's cross-regime architecture, not just a single platform.

### 3.3 What a successful experiment shows (and does not show)

A platform that realizes an interior-maximum c_s-profile and observes `κ = 0, T_H = 0`:

- **Confirms** the kinematic acoustic-metric formula for that class of profile (a test of analogue gravity, not uniquely ED).
- **Is consistent with** ED's claim that P4 horizons sit in the extremal class.
- **Does not prove** ED uniquely, because standard analogue gravity predicts the same outcome.

A platform that realizes an interior-maximum profile and observes **thermal emission or κ ≠ 0 extracted from mode-mixing**:

- **Falsifies** either the acoustic-metric formulation itself (for that system) or the extremal-horizon reading.
- **Is inconsistent with** ED's P4-horizon-is-cold claim and forces a re-examination.
- This is the genuinely informative outcome direction.

### 3.4 Where ED and analogue gravity could diverge

If ED's curvature prediction (e.g. the Gaussian-bump `R(0) = −a/[σ²(1−a)]` from [`ED_Acoustic_Metric_Curvature.md`](ED_Acoustic_Metric_Curvature.md)) is matched to a platform's engineered profile, the quantitative curvature at the horizon is a **joint** ED + acoustic-metric prediction. If curvature extraction (via higher-order mode-mixing beyond the surface-gravity leading term) disagrees with ED's specific profile-shape formula, that would falsify ED's mapping even if the leading κ = 0 result survives.

---

## 4. Testable predictions per platform

### 4.1 BEC acoustic horizons

- **Profile needed for ED extremal test:** density `n(x)` with a smooth interior maximum *and* a flow profile `v(x)` such that `v² − c_s² = 0` occurs at the smooth maximum. Requires engineered trap + flow protocol.
- **Natively extremal?** No. Standard Steinhauer-style setups produce monotonic transonic horizons with κ ≠ 0.
- **Analogue of κ:** extracted from the slope of `v² − c_s²` across the horizon, typically via Bogoliubov-mode analysis on density-density correlation functions `G(x, x')`.
- **Signature of κ = 0:** absence of the long-range Hawking-pair correlations that peak along null rays in `G(x, x')`. Instead, correlations should show a finite-range structure consistent with normal mode scattering, not thermal entanglement across a horizon.
- **Expected Hawking emission at extremal:** `T_H = 0` → no thermal phonon tail. Observable via the two-point density-density correlator or momentum-distribution tails.
- **Distinguishing from noise:** compare to a control monotonic-horizon protocol in the same apparatus; the extremal profile should show a suppressed correlation peak vs. the monotonic profile.

### 4.2 Water-tank horizons

- **Profile needed:** bathymetry + flow such that `v² − c_w²` has a smooth maximum through zero at a single point (soft horizon).
- **Natively extremal?** No. Engineered.
- **Analogue of κ:** extracted from the scattering coefficients of converted-mode amplitudes (Weinfurtner-style extraction).
- **Signature of κ = 0:** scattering matrix approaches the identity on a narrowing frequency band near the extremal point — no Hawking-converted output mode.
- **Expected emission:** absent for soft-horizon configuration.
- **Distinguishing from noise:** stationary flow with sub-pixel bathymetry resolution; compare to a control steep-horizon configuration.

### 4.3 Optical pulse analogues

- **Profile needed:** bright pulse with smooth bell-shape (Gaussian, sech², etc.) in a fibre with sufficient nonlinearity. The pulse natively provides an interior-maximum refractive-index profile.
- **Natively extremal?** **Yes — the pulse peak gives an interior max by default.** However, the operational "horizon" is on the pulse flank where `v_g,probe = v_pulse`, not at the peak. The ED-relevant test is whether *peak-level* interactions (not flank interactions) produce mode conversion or thermal spectra.
- **Analogue of κ:** extracted from probe-photon frequency shifts near the horizon.
- **Signature of κ = 0:** absence of spontaneous photon pair emission from the peak region; photon pair emission observed on the pulse flanks (κ ≠ 0) but suppressed in the extremal peak region.
- **Expected emission:** thermal at flanks, cold at peak. A **within-experiment differential** is possible in a single pulse geometry.
- **Distinguishing from noise:** frequency-resolved pair counting with coincidence timing; compare flank-emitted vs. peak-emitted photon statistics.
- **Caveat:** the Belgiorno et al. 2010 controversy warns that spurious blackbody-like spectra can arise from filamentation and Raman scattering. Peak-vs.-flank differential is precisely what discriminates.

### 4.4 Slow-light / EIT media

- **Profile needed:** spatially shaped control field produces `v_g(x)` with an interior smooth max and `v_g → 0` at the max. EIT natively stops light at a chosen position.
- **Natively extremal?** **Fully controllable.** The control field can be shaped to give monotonic *or* interior-max profiles.
- **Analogue of κ:** extracted from probe-pulse reflection/transmission as a function of control-field gradient at the stopping point.
- **Signature of κ = 0:** pure reflection with zero mode-conversion amplitude at the smooth stopping point; thermal emission absent.
- **Expected emission:** zero for smooth extremal stopping; finite for sharp edge.
- **Distinguishing from noise:** same apparatus toggled between monotonic and extremal control-field profiles. **This is the cleanest differential test.**

### 4.5 Phononic / optomechanical crystals

- **Profile needed:** engineered band-gap modulation producing a position-dependent band-edge frequency. Phonon enters a region where its frequency is gapped out.
- **Natively extremal?** **Yes — band-edge vanishing of `v_g` is smooth and quadratic by construction.**
- **Analogue of κ:** reflection coefficient near the band edge; thermal versus elastic scattering statistics.
- **Signature of κ = 0:** elastic reflection only; no thermal phonon emission from the band-edge interface.
- **Expected emission:** generically zero by dispersion-engineering choice — this platform confirms the kinematic result but is the **weakest discriminator** between ED and generic analogue gravity because every band-edge horizon is extremal.
- **Distinguishing from noise:** not needed; baseline scattering is well-characterized by band-structure calculations.

---

## 5. Proposed experiments

Listed in order of **ED-distinguishing power** (not cost):

### Experiment 1 — Slow-light / EIT differential test (highest distinguishing power)

**Platform:** cold atomic ensemble or warm atomic vapour cell with EIT control + probe laser setup (existing Lukin-group or Hau-group-style apparatus).

**Protocol:**
1. Prepare a standard EIT medium.
2. Toggle control-field spatial profile between two shapes:
   - **(M)** Monotonic: control-field intensity drops linearly across the cell, giving monotonic `v_g(x)` with sharp stopping point.
   - **(E)** Extremal: control-field intensity has a smooth Gaussian dip in the centre, giving interior-minimum `v_g(x)` with smooth stopping at the dip centre.
3. Inject probe pulses in both configurations.
4. Measure probe-photon statistics at the output: thermal emission rate, pair-correlation function, reflection coefficient.

**Prediction:**
- Configuration (M): finite κ_M, thermal-like emission, Hawking-analogue correlations.
- Configuration (E): κ_E ≈ 0, no thermal emission, no Hawking correlations.
- The **ratio** of thermal rates (E)/(M) should be near zero.

**Budget / timeline:** Moderate. If existing EIT apparatus available, ~3–6 months. Collaboration with a slow-light group (Lukin, Hau, Halfmann) is the natural path.

### Experiment 2 — Optical pulse peak-vs-flank differential (native platform, single-apparatus test)

**Platform:** nonlinear optical fibre with pulse-induced refractive-index change (Philbin setup or equivalent).

**Protocol:**
1. Generate a bright bell-shaped pulse (Gaussian or sech²) in a photonic-crystal fibre.
2. Inject probe photons co-propagating with the pulse.
3. Frequency-resolve and coincidence-count output photons from:
   - Flank horizon regions (κ ≠ 0).
   - Peak region (interior max of n_g, κ ≈ 0).

**Prediction:**
- Flank: Hawking-like spectrum with characteristic `T_H ∝ κ_flank`.
- Peak: no spontaneous pair emission above shot-noise background.

**Budget / timeline:** Requires collaboration with a fibre-nonlinear-optics group (Philbin, König). ~6–12 months. The Belgiorno controversy means careful noise-characterization is mandatory.

### Experiment 3 — BEC engineered extremal horizon

**Platform:** Steinhauer-style 1D elongated BEC with modified trap protocol.

**Protocol:**
1. Instead of a standard step-potential transonic setup, engineer a trap + flow profile where `v(x) − c_s(x)` has a smooth second-order zero at an interior point.
2. Measure density-density correlation function `G(x, x')` following Steinhauer protocols.

**Prediction:**
- Standard setup: peaked Hawking-pair correlations along null rays.
- Extremal setup: correlations suppressed or absent along those same null rays.

**Budget / timeline:** Requires Steinhauer-group or Westbrook-group collaboration. ~1–2 years including trap engineering. Highest technical bar of the three platforms; highest profile if successful.

### Experiment 4 — Phononic-crystal band-edge baseline (confirmatory, low distinguishing power)

**Platform:** engineered phononic crystal (existing optomechanics labs).

**Protocol:** inject phonon pulses into a gradient-band-edge structure; measure elastic-vs-thermal reflection statistics.

**Prediction:** pure elastic reflection; no thermal tail.

**Role:** not distinguishing; confirms the kinematic acoustic-metric formula in a controllable substrate. Useful as a **baseline calibration** for the other three experiments, not as an ED-specific test.

### Experiment 5 — Water-tank soft-horizon reanalysis

**Platform:** Weinfurtner-Unruh water-tank apparatus.

**Protocol:** redesign bathymetry for a soft transonic profile; rerun stimulated Hawking protocol; compare to published monotonic-horizon dataset.

**Prediction:** suppressed Hawking-amplitude conversion at soft-horizon frequency relative to monotonic control.

**Budget / timeline:** ~6 months if existing apparatus is available. Accessible academic-scale cost.

---

## 6. What would falsify ED's extremal-horizon prediction

- **Thermal emission with `T_H > 0` from an interior-maximum horizon** in any of the platforms above, with surface-gravity extraction showing `κ ≠ 0` despite the smooth-maximum geometry. This would either (a) invalidate the acoustic-metric formulation in that regime, or (b) show that mode-conversion at extremal points proceeds via a non-thermal but analogue-Hawking-like channel that the current ED reading misses.
- **Non-zero κ extracted from mode-mixing at a certifiably smooth c_s-maximum.** Would force a re-examination of the Visser formula's applicability or reveal higher-order curvature contributions ED has not accounted for.
- **Systematic observation of thermal phonon emission at phononic-crystal band edges** despite the extremal structure of the band-edge dispersion. Would rupture the weakest but most basic version of the prediction.
- **Quantitative curvature mismatch** at the horizon: if the extracted acoustic curvature disagrees with ED's specific profile-shape formula (e.g. Gaussian-bump `R(0) = −a/[σ²(1−a)]`) beyond experimental error.
- **Any analogue system where the signal-speed profile has a smooth local max but κ extracted from scattering ≠ 0.** This would falsify the kinematic reading directly.

---

## 7. What would support ED

- **Cross-platform consistency**: repeated observation across two or more of (BEC, optical pulse, EIT, phononic crystal) that interior-maximum horizons are cold (`T_H = 0` within experimental resolution).
- **Mode-mixing suppression at extremal points** matching the Visser-formula prediction.
- **Curvature localization matching ED's formulas** for specific engineered profiles — a Gaussian bump with measured `R(0)` agreeing with `−a/[σ²(1−a)]` to within experimental tolerance.
- **Within-experiment differentials** (EIT toggle, optical peak-vs-flank, BEC soft-vs-sharp horizon) showing **contrast** between extremal and monotonic configurations — this is the strongest support because the apparatus is the same on both sides.
- **Detection of the P4 mobility-collapse structural signature** — i.e. a system where M(ρ) has a natural collapse max (not engineered flow), producing an interior-max horizon, matching ED's prediction that this is the generic stationary configuration.

A positive result across platforms supports the acoustic-metric formulation and ED's P4-is-extremal reading, without proving ED uniquely over competing acoustic-metric frameworks. That is acceptable — ED's broader claim (cross-regime invariance under one PDE) does not rest on uniqueness at any single platform.

---

## 8. Recommendations

### 8.1 Priority ranking (ED-distinguishing power × experimental tractability)

1. **Slow-light / EIT toggle experiment** (Experiment 1) — highest priority. Clean differential, full control, existing apparatus, widely available groups.
2. **Optical pulse peak-vs-flank** (Experiment 2) — second priority. Native platform, single-apparatus differential, but Belgiorno-controversy noise-budget requires care.
3. **Water-tank soft-horizon reanalysis** (Experiment 5) — third priority. Accessible cost, existing dataset for comparison, moderate distinguishing power.
4. **BEC engineered extremal horizon** (Experiment 3) — fourth priority. Highest profile but highest technical bar; best as a follow-up after cheaper tests have narrowed the parameter space.
5. **Phononic-crystal baseline** (Experiment 4) — calibration only; not a discriminating test on its own.

### 8.2 Suggested collaborations

- **EIT / slow light:** Lukin (Harvard), Hau (Harvard), Halfmann (Darmstadt), Lvovsky (Oxford).
- **Optical-pulse analogue:** Philbin (St Andrews), König (St Andrews), Faccio (Glasgow).
- **BEC acoustic:** Steinhauer (Technion), Westbrook (Institut d'Optique), Cornell / Jin (JILA).
- **Water tank:** Weinfurtner (Nottingham), Unruh (UBC).
- **Phononic / optomechanics:** Aspelmeyer (Vienna — already ED-09.5 Track A contact), Painter (Caltech).

### 8.3 Measurable quantities that correspond directly to ED invariants

| ED invariant | Analogue observable | Primary extraction method |
|---|---|---|
| Mobility zero `M(ρ_max) = 0` | Signal-speed zero `c_s(x_*) = 0` | Direct measurement of dispersion / group-velocity profile |
| Canon P4 horizon locus | Smooth-maximum of `c_s²(x)` | Profile engineering + scan |
| Surface gravity `κ = 0` | Absence of Hawking-like spectrum at horizon | Pair-correlation function or scattering coefficients |
| Acoustic curvature `R[g^eff]` | Higher-order mode mixing beyond the leading thermal term | Frequency-resolved spectroscopy |
| `c_s = √M_0 = c_0 = c/0.6` (ED-Dimensional-01) | In a calibrated condensed-matter regime, the effective signal speed in absolute units | Cross-regime numerical comparison, not a single-experiment test |

### 8.4 One-paragraph program summary

**The highest-leverage single experiment is the EIT differential test (Experiment 1):** it gives a within-apparatus extremal-vs-monotonic contrast, uses widely available equipment, has no known systematic that fakes a κ = 0 signature, and tests the cleanest formulation of the ED prediction (mobility-collapse → smooth-max horizon → extremal → no thermal emission). A null-emission result in the extremal configuration + thermal-emission in the monotonic configuration from the same apparatus, same measurement chain, would be the strongest possible single-experiment support for ED's acoustic-metric / P4 reading. The optical-pulse experiment is a natural follow-up because the platform is native-extremal, and the BEC experiment is the highest-profile follow-up once the parameter space is narrowed.

---

## 9. Deferred extensions

- **Moving-background acoustic metric.** The current derivation is v_0 = 0. Transonic (v ≠ 0) horizons in BEC and water tank require extending the linearisation to moving backgrounds. This is standard in analogue gravity (Unruh 1981, Visser 1998) but needs an explicit re-derivation in ED notation before BEC / water-tank tests can be mapped cleanly. Flagged as the next theory-memo target.
- **Mode-mixing beyond leading κ.** Curvature-level predictions from [`ED_Acoustic_Metric_Curvature.md`](ED_Acoustic_Metric_Curvature.md) need translation into analogue-gravity mode-conversion amplitudes (grey-body factors, higher-l scattering). Currently only leading-order κ = 0 is mapped.
- **Cross-regime scale check.** The `c_s = c/0.6` identification (ED-Dimensional-01) is a structural feature; whether analogue-platform signal speeds calibrate to the same ratio in their respective regimes is a latent test, not obviously extractable from any single experiment but potentially visible in a meta-analysis once multiple platforms have been measured.

---

## 10. Verdict

- The ED acoustic metric is a well-defined kinematic object testable in five analogue-gravity platforms with varying degrees of native support for ED's interior-maximum horizon class.
- The extremal-horizon result (`κ = 0` at smooth maxima) is a shared prediction of ED and standard analogue gravity; it is **not** ED-specific in isolation but **is** the right testable claim once paired with ED's P4 mobility-collapse prediction for *which systems* produce such horizons.
- Two experiments (EIT differential, optical pulse peak-vs-flank) deliver within-apparatus differentials and are the highest-priority targets.
- The program is honestly (ii)-grade in the Scoping-Memo taxonomy: kinematic acoustic-metric tests, not tests of Einstein-equation emergence or quantum gravity. Claims must stay in this envelope.
- Guardrails from [`project_ed10_geometry_qft_scope.md`](../memory/project_ed10_geometry_qft_scope.md) apply: no Hawking-radiation claim for generic ED horizons (only interior-max cold / monotonic thermal); no Einstein-dynamics claim; no α or gauge mileage from these tests.
