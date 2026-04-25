# ED-Dimensional-01-Ext — v0.4 Expansion Plan

**Status:** PLANNING DOCUMENT (2026-04-20). Roadmap from the stabilised v0.3 memo ([`ED-Dimensional-01-Ext.md`](ED-Dimensional-01-Ext.md)) to a paper-scope v0.4 draft. No content is expanded in this document; it catalogues what needs to be added, where, and at what depth. Authoritative content remains in the v0.3 memo until v0.4 lands.

**Scope decision.** v0.4 is the paper-scope expansion: the memo becomes a standalone publishable document, self-contained and not requiring the rest of the ED corpus as prerequisite reading. Sections that v0.3 left as sketches or references-to-elsewhere should be derived in place; where v0.3 cites an ED document (e.g., `docs/ED-09-5-Observable-Sharpening.md` §22.3 for the Aspelmeyer derivation), v0.4 should reproduce the key results self-contained.

**Cross-references.** See the v0.3 memo for current content. This planning document references v0.3 section numbers throughout.

---

## 1. Expansion assessment per section

### §1 Purpose (v0.3 → v0.4)
- **v0.3 status:** terse, ~2 paragraphs, memo-scope framing.
- **v0.4 need:** introduction-scope motivation. What problem the paper solves (the Atlas's silent `D_nd`), why this matters (without it, ED is under-constrained in non-quantum regimes), what the paper's contribution is (a template that ports across five regimes and recovers known thresholds as instances of a single PDE bifurcation).
- **Depth target:** ~5 paragraphs with proper citations into the ED corpus.
- **New content required:** problem statement, explicit differentiation from Madelung-anchoring, forecast of the cross-regime result.

### §2 Template (v0.3 → v0.4)
- **v0.3 status:** six-step bullet list + structural invariants footnote.
- **v0.4 need:** proper derivation. The template was derived in `ED-09-5-Observable-Sharpening.md` §22.3 for the Aspelmeyer regime; that derivation should be reproduced here with its linearisation of the canonical PDE onto the mechanical-cavity rotating-frame equations. A diagram showing the (ρ, v) mapping would help.
- **Depth target:** ~2 pages with the linearisation explicit, plus a template-architecture diagram.
- **New content required:**
  - Reproduction of the `[[-DP₀, H], [-P₀/τ, -ζ/τ]]` matrix match from the Aspelmeyer derivation, done self-contained.
  - Explicit statement of which template steps are forced and which are interpretive (e.g., step 3 γ_dec choice is a physical judgment; step 4 1/τ is typically forced by the mediating mode's equation of motion).
  - Diagram: `(ρ, v)` architectural roles + the rate-balance construction.
  - Statement of the three cross-checks the template passed in Aspelmeyer (ζ agreement, exact ζ match with ED-Phys-17/19, N_osc cross-derivation).

### §3 Cavity QED / Haroche (v0.3 → v0.4)
- **v0.3 status:** canonical identification + F0 envelope + cross-checks + aside on κ = Γ. Clean but sketch.
- **v0.4 need:** proper Jaynes-Cummings linearisation showing the match to the canonical PDE template, parallel to what §22.3 did for optomechanics. Table of real cavity-QED experimental systems (Haroche Rydberg, Walther ions, Kimble/Rempe optical tweezers) with their (Γ, 2g, κ) values and computed D.
- **Depth target:** ~2 pages.
- **New content required:**
  - Linearised Jaynes-Cummings matching (2×2 system in slow-envelope basis).
  - Experimental systems table: ~6–8 cavity-QED setups from the literature with their computed D positions and inferred F0 envelope predictions.
  - Connection to existing cavity-QED strong-coupling-threshold literature (citation pass needed).
  - Aside on κ = Γ stays as in v0.3.

### §4 Condensed matter (v0.3 → v0.4)
- **v0.3 status:** general Debye/RC table, FRAP exception, conclusion that template doesn't port for pure Debye.
- **v0.4 need:** additional participation-channel exceptions (the FRAP class) to show the template's reach isn't limited to one biomolecular case; and a principled sorting criterion for when a condensed-matter system is Debye (penalty-only, template fails) vs participation-type (template applies).
- **Depth target:** ~2 pages.
- **New content required:**
  - **Additional candidate exception regimes** (proposed, each to be evaluated in v0.4):
    1. **Spin glasses near the freezing transition** — magnetisation as system, long-range spin correlation as mediating mode. γ_dec = individual spin-flip rate; ω_sys = correlation-length crossing time. Plausibly near-bifurcation near T_g.
    2. **Superconducting films near T_c** — local Cooper-pair density as system, Meissner-screening field as mediating. γ_dec = phase-slip rate; ω_sys = plasma frequency in the film.
    3. **Liquid crystals near the nematic-isotropic transition** — local orientational order as system, bulk director field as mediating. γ_dec = rotational diffusion rate; ω_sys = director relaxation across a domain.
    4. **Bose-Einstein condensates at finite T** — condensate fraction as system, thermal cloud as mediating. γ_dec = thermal scattering rate; ω_sys = condensate oscillation (breathing / quadrupole modes).
    5. **Active matter with collective modes** (nematics, swarms) — local alignment as system, bulk-flow mode as mediating. Speculative but potentially a new regime.
  - **Sorting criterion:** participation-channel applies when the mediating mode has its own dynamics on a timescale distinct from the local mode's; pure Debye applies when the mean field is slaved to the local dynamics (no independent τ).
  - Which of the five candidates above has the strongest empirical hook. My first-pass assessment: (1) spin glasses and (2) SC films are the best-grounded; (3) liquid crystals tractable; (4) BEC tractable; (5) active matter speculative.

### §5 Galactic (v0.3 → v0.4)
- **v0.3 status:** MW/dwarf/cluster table with γ_env, D spread from 0.04 to 0.9. ED-XX flagged as input, not output.
- **v0.4 need:** quantitative D-ranges tied to published astronomical samples (SPARC, Finner cluster sample, dwarf spheroidals), specific F0 observable (not just "BTFR residual vs age"), and an honest treatment of the `H₀` vs `γ_env` combined-form question.
- **Depth target:** ~2.5 pages.
- **New content required:**
  - **Quantitative D values for published samples:**
    - SPARC 175-galaxy sample: compute D = γ_env/(γ_env + 1/t_cross) galaxy-by-galaxy using v_circ, L₀, and environmental metadata. Report histogram of D values.
    - Finner 25-subcluster sample: compute D for cluster-scale dynamics. Cross-reference with the cluster merger-lag result.
    - Dwarf spheroidal sample (Fornax, Sculptor, Draco, etc.): compute D across the local-group dwarfs. Cross-reference ED-04.5 D_outer ~ 53% Active-vs-Quiet separation — is D ~ 0.3 (the dwarf value) consistent with the D_outer observation?
  - **F0 observable specification.** The ~15 Myr envelope period is potentially detectable via BTFR residual vs SFH age, binned at ~5–10 Myr resolution. Need specific protocol: (a) SFH inference method (STECKMAP / MILES / etc.), (b) BTFR-residual computation, (c) statistical test for periodic signature.
  - **`H₀` vs `γ_env` combined form.** Derive from first principles whether γ_dec = γ_env + H₀ (independent decoherence channels add), γ_dec = max(γ_env, H₀) (dominant channel), or γ_dec = some convolution. This is a real physics question worth resolving.
  - **Map to ED-XX source-scale `σ ≥ 1–3 Mpc`.** γ_env = v_env/σ_env makes the σ-scale explicit. Verify consistency with the ED-XX scan table (source width → flatness error).
  - **Connection to the ED-I-27 weak-lensing interpretation.** Is D at the galactic scale inferable from weak-lensing extent? (The Mistele+2024 flat-velocity extent to 1 Mpc suggests the environmental temporal-tension field is coherent over ~Mpc scales, which is roughly σ_env; consistent with γ_env computation.)

### §6 Cosmological (v0.3 → v0.4)
- **v0.4 need:** cosmological-perturbation-theory derivation of γ_dec(k), connection to observed matter power spectrum P(k), and specific observational protocol for testing the k_* ~ 2π/10 Mpc prediction.
- **Depth target:** ~3 pages (most expansion; currently weakest section).
- **New content required:**
  - **CPT derivation of γ_dec(k).** In linear cosmological perturbation theory (Peebles, Dodelson, Ma-Bertschinger), the damping rate of δρ/ρ at wavenumber k has several contributions:
    1. Hubble drag: `H(a)` (all k)
    2. Silk damping (baryon-photon): `k² η_γ / (a ρ_γ)` for sub-horizon baryon modes
    3. Free-streaming (warm dark matter / neutrinos): `k · v_th(a)`
    4. Shear viscosity (imperfect fluid): `k² η_visc / ρ`
    5. Non-linear mode-coupling damping (quasilinear regime)
  - Which of these plays the "γ_dec" role in the ED template? First-pass: (3) free-streaming for warm-dark-matter or neutrino contributions, (4) shear-viscosity for baryonic modes. Both scale as `k^n` for some n, consistent with v0.3's first-pass identification `γ_dec(k) ~ k·v_pec`.
  - Need proper derivation: which is dominant at the cosmic-web scale 10 Mpc? Free-streaming or shear viscosity? What is `v_pec` physically — is it the peculiar-velocity field of cosmic-web structure, the thermal velocity of warm DM, or something else?
  - **Connection to matter power spectrum P(k).** The predicted k_* should show up as a feature or transition in P(k) at wavelength ~10 Mpc. Compare against:
    - Late-time linear P(k) from DES / Euclid / DESI.
    - The BAO peak at ~150 Mpc (scale-separation: BAO is 15× larger than k_*, so they don't obviously conflict, but the cosmic-web scale may appear as sub-BAO structure).
    - The transition from linear to non-linear regime (~5–10 Mpc typically) — does the ED prediction k_* align with this empirically?
  - **Redshift evolution of k_*.** As H(z) and v_pec(z) evolve, k_* shifts. Predicts a redshift-dependent cosmic-web scale, testable via redshift-binned P(k) or cosmic-web statistics.
  - **Matter-dominated vs dark-energy era mapping (quantitative).** Anchor the qualitative narrative with H(z), v_pec(z), and k_*(z) computed explicitly.

### §7 Cross-regime synthesis (v0.3 → v0.4)
- **v0.3 status:** cross-regime table + 5 structural results + atlas-extension status + open issues.
- **v0.4 need:** unified cross-regime diagram showing D vs characteristic scale across ~30 OOM; explicit ζ-universality discussion (new architectural question from v0.3); implications connected to the broader ED program (ED-09.5, ED-SC-00, ED-XX, ED-Arch).
- **Depth target:** ~2 pages + figure.
- **New content required:**
  - **Cross-regime diagram.** D values on [0, 1] y-axis; characteristic scale on log x-axis from 10⁻¹⁵ m (atomic) to 10²⁶ m (cosmological). Horizontal line at D_crit = 0.5. Each regime as a labeled point (or horizontal band for scale-dependent regimes like cosmology). Visual argument for the five structural results.
  - **ζ universality.** §22.3 gave `ζ = 1/2` for cavity-mode-mediated regimes. §4, §5, §6 all flagged `ζ` as not derivable. Is there a unifying argument? First-pass hypothesis: `ζ = 1/2` is universal when the mediating mode is a complex scalar with canonical damping; ζ ≠ 1/2 signals a different damping structure. Test against the specific regimes.
  - **Implications for ED-09.5.** The cross-regime template unifies the Q-C transition prediction across cavity QED, optomechanics, FRAP, and cosmology. All five regimes have the same bifurcation at D_crit = 0.5, landing at different physical thresholds.
  - **Implications for ED-SC-00.** Each cross-scale correspondence in ED-SC-00 Table 1 (22 micro↔macro pairs) is in principle verifiable by checking that both endpoints have the same D. This gives ED-SC-00 a quantitative backbone.
  - **Implications for ED-XX.** The galactic regime (§5) shows the template is consistent with ED-XX's environmental source-attribution — consistency, not derivation.
  - **Implications for ED-Arch / ED-SC 2.0.** The motif-conditioned median `r* = −1.304` from ED-SC 2.0 is a property of 2D scalar density fields at spatial stationary points. Does the rate-balance template predict anything about this? If r* depends on D, different regimes might have different r* — potentially falsifiable.
  - **Implications for Tier-1 experimental programs.** Each regime has an accessible test (FRAP, cavity QED time-domain, Aspelmeyer raw heterodyne, galactic BTFR-residual-vs-age, cosmological P(k) at 10 Mpc).

---

## 2. Specific proposals

### 2.1 Additional examples for §4 (ordered by tractability)

| System | System mode `ρ` | Mediating mode `v` | `γ_dec` (est.) | `ω_sys` (est.) | Estimated D | Empirical hook |
|:-------|:----------------|:-------------------|:---------------|:---------------|:-----------:|:---------------|
| FRAP (already in v0.3) | fluorophore density | bulk diffusion mode | 10–100 Hz | 10 Hz | 0.3–0.6 | Creative Proteomics protocol |
| Spin glass near T_g | local magnetisation | long-range spin correlation | 10⁶–10⁹ Hz (spin-flip) | depends on correlation length | varies near T_g | aging experiments, noise spectra |
| SC film near T_c | Cooper-pair density | Meissner screening field | phase-slip rate | plasma frequency in film | regime-dependent | Berezinskii-Kosterlitz-Thouless transition |
| Liquid crystal near N-I transition | orientational order | bulk director | rotational diffusion | director relaxation | regime-dependent | dynamic light scattering |
| BEC at finite T | condensate fraction | thermal cloud | thermal scattering | breathing mode | regime-dependent | Bragg spectroscopy, collective mode detection |
| Active matter | local alignment | bulk flow | collision rate | coherent flow rate | speculative | rheometry, flow spectroscopy |

Priority: FRAP (done) → spin glass (strong empirical hook via aging) → SC films (BKT connection clean) → BEC (theoretically clean but experimentally expensive) → liquid crystals → active matter.

v0.4 should include **three** of the five additional examples at full depth (template matching + D calculation + predicted observable). My recommendation: **spin glass, SC film, BEC.**

### 2.2 Quantitative D-ranges and observables for §5

**Published samples to compute D for:**

| Sample | N galaxies | D distribution (predicted) | Observable test |
|:-------|:----------:|:--------------------------:|:----------------|
| SPARC rotation curves | 175 | log-histogram, peaks near MW-class value ~0.04 | BTFR residual vs age, 10-Myr bins, activity-correlated subsample |
| Finner 25-subcluster sample | 25 | D ~ 0.5–0.9 (cluster regime) | merger-lag `ℓ = D_T/v` revisited with D-mapping |
| Local Group dwarfs | ~25 | D ~ 0.2–0.4 (near bifurcation) | D_outer separation (ED-04.5) re-interpreted |
| Galaxy groups (e.g., CLoGS catalogue) | 50+ | D ~ 0.3–0.5 (near bifurcation) | intra-group dynamics vs activity |

**F0 observable specification (BTFR vs age):**
- Step 1: SFH inference via STECKMAP or similar on SDSS / MaNGA sample.
- Step 2: BTFR residual `Δ V_∞ = V_obs - V_BTFR` computed per galaxy.
- Step 3: Bin `Δ V_∞` by stellar-population age in 5-Myr windows.
- Step 4: Test for a ~15 Myr periodic signature using Lomb-Scargle or similar.
- Predicted signature: `Δ V_∞ ∝ cos(2π · t / 15 Myr)` with envelope amplitude ~3–6% of V_∞ (from the third-harmonic ratio in the §1.5 framing).

### 2.3 Cosmological perturbation-theory anchors for §6

**Required derivation:**
- Full CPT treatment of damping at sub-horizon scales in the matter-dominated era.
- Identify which damping channel dominates at k ~ 2π/10 Mpc: Silk damping, free-streaming, shear viscosity, or non-linear mode-coupling.
- Express γ_dec(k) explicitly in terms of cosmological parameters.
- Compute k_* as a function of redshift from a ΛCDM background.

**Observational anchors:**
- Late-time matter power spectrum P(k) from Euclid / DESI / DES. Feature at ~10 Mpc would be the ED signature; need to predict whether it's enhanced, suppressed, or structurally distinct from ΛCDM.
- BAO peak at ~150 Mpc is far from k_* — no obvious degeneracy.
- Cosmic-web statistics (filament length distribution, void-size function) from SDSS / Illustris / Bolshoi simulations.
- Quantitative prediction: the cosmic-web scale should show a specific redshift-dependent shift consistent with k_*(z).

### 2.4 ζ interpretations across regimes

**Open architectural question.** Is `ζ = 1/2` universal?

Candidate universal argument:
- If `v(t)` is a single complex scalar field with canonical Wiener-like damping (`dv/dt = -γ_v · v/2 + noise`), then ζ = 1/2 follows from normalising the quadrature variance.
- This applies when the mediating mode is a bosonic single-mode field (cavity in cavity-QED and optomechanics; possibly the environmental temporal-tension field in galactic).
- Does NOT obviously apply when the mediating mode is multi-mode (bulk diffusion in FRAP, cosmic flow in cosmology).

Test in v0.4:
- Check each regime individually. Compute ζ from first principles where possible.
- Regimes with single-mode cavity-like mediating mode: cavity QED ✓ (confirmed), optomechanics ✓ (confirmed).
- Regimes with multi-mode mediating: FRAP, galactic, cosmological. Predict ζ per regime and see if a pattern emerges.
- If pattern: propose a universal principle (single-mode bosonic → ζ = 1/2). If no pattern: document as an open architectural problem for ED-Arch.

### 2.5 Unified cross-regime diagram

**Proposed figure.**

- **Axes:** x = log(characteristic scale / m), from −10 to +26. y = D, from 0 to 1.
- **Horizontal reference line:** D = 0.5 (bifurcation).
- **Plot points (one per regime):** Cavity QED (D spans bifurcation at ~10⁻⁶ m), Aspelmeyer optomechanics (D ~ 10⁻⁶ at ~10⁻⁷ m scale), FRAP (D ~ 0.3–0.6 at ~10⁻⁶ m), MW (D ~ 0.04 at ~10¹⁹ m), dwarf (D ~ 0.3 at ~10¹⁹ m), cluster (D ~ 0.9 at ~10²² m), cosmic-web scale (D ~ 0.5 at ~10²³ m).
- **Regime bands:** shaded regions showing where each regime class operates (condensed matter covers 10⁻⁹ to 10⁻³ m, galactic covers 10¹⁸ to 10²³ m, etc.).
- **Annotations:** each point labeled with the physical threshold its bifurcation corresponds to (strong coupling, sideband resolution, diffusion-vs-exchange, dwarf/group scale, cosmic-web scale).

Purpose: convey the cross-regime structural unity (the same D_crit = 0.5 showing up at radically different scales and via radically different physical rates) in a single image.

---

## 3. Paper outline (proposed)

**Working title:** *Anchoring the Dimensionless Channel Weight Across Regimes: A Rate-Balance Template for the Event Density Atlas*

**Target venue:** philosophy-of-physics or interdisciplinary (Foundations of Physics, Entropy, Scientific Reports), given that the paper is architectural rather than reporting a single empirical result.

**Proposed structure:**

### Abstract (200–300 words)
ED's canonical PDE contains a dimensionless channel weight `D` (`D + H = 1`) with a sharp bifurcation at `D_crit = 0.5` (Canon principle P6). The Dimensional Atlas anchors regime-specific physical units via Madelung-style correspondences in the quantum regime but leaves `D` free in non-quantum regimes. This paper derives a **rate-balance template** `D = γ_dec/(γ_dec + ω_sys)` that fixes `D` from each regime's characteristic rates, and applies it across five regimes: cavity QED, optomechanics, condensed matter (FRAP and exceptions), galactic (post-ED-XX), and cosmological. The template ports across four of five regimes (pure Debye/RC is a documented scope limit). In every regime the bifurcation `D_crit = 0.5` corresponds to a known physical threshold (strong coupling, sideband resolution, diffusion-vs-exchange, intra-group environmental scale, cosmic-web scale). The cross-regime synthesis spans ~30 orders of magnitude in scale and recovers ED-XX's environmental source-attribution as a consistency check. Implications for ED-09.5's quantum-classical transition, ED-SC-00's scale-correspondence program, and the Tier-1 experimental agenda are discussed.

### 1. Introduction
- The Atlas's silent `D_nd` problem.
- Madelung anchoring works in the quantum regime; no analogue exists for other regimes.
- What this paper provides: a rate-balance template + five-regime application.
- Structure of the paper.

### 2. The Rate-Balance Template
- Statement of the canonical PDE and P1–P7.
- `D + H = 1` dimensionless channel weight vs dimensional `D_phys`.
- The template's six steps.
- Derivation via linearised matching to the optomechanics rotating-frame equations (reproducing §22.3 of Observable-Sharpening memo self-contained).
- The three non-trivial cross-checks from the Aspelmeyer case (ζ, ζ = 0.5 match with ED-Phys-17/19, N_osc).
- Template-architecture diagram.

### 3. Regime applications
- **3.1 Cavity QED / Haroche.** Jaynes-Cummings linearisation, template matching, experimental-systems table, strong-coupling threshold, F0 envelope prediction. Aside on the good-cavity/bad-cavity boundary (not the ED bifurcation).
- **3.2 Optomechanics / Aspelmeyer.** The original case. Derivation summary. `(ρ, v) ↔ (mechanical, X_cav)` identification. Sideband-resolution threshold. Cross-checks. F0 envelope.
- **3.3 Condensed matter.** Pure Debye/RC as a documented scope limit (no identifiable ω_sys). Participation-channel exceptions: FRAP (worked in depth), spin glasses (BKT-like transitions), superconducting films (T_c region), BECs (finite-T). Sorting criterion for Debye-vs-participation.
- **3.4 Galactic (post-ED-XX).** Environmental `γ_env` replaces `H₀` as the operative decoherence rate. MW/dwarf/cluster D-spread. SPARC and Finner sample applications. BTFR-residual-vs-SFH-age observable. Connection to ED-XX.
- **3.5 Cosmological.** Scale-dependent `γ_dec(k)` from cosmological perturbation theory. Bifurcation at cosmic-web scale `~2π/10 Mpc`. Redshift evolution. Observational hooks: matter power spectrum at ~10 Mpc, cosmic-web statistics, BAO-independence.

### 4. Cross-regime synthesis
- Cross-regime diagram (D vs log scale, horizontal bifurcation line, labeled points).
- Unified statement of the five structural results.
- `ζ` universality question and proposed resolution (single-mode-bosonic argument).
- Comparison with the `D_phys · T₀/L₀² = 0.3` dimensional invariant (both span 5 regimes, 61 OOM).

### 5. Implications
- For ED's empirical program (unifies Q-C transition across four regimes).
- For ED-SC-00 (quantitative backbone for scale-correspondence).
- For ED-XX (consistency confirmation).
- For ED-Arch (possible connection to r* = −1.304 invariant).
- For experimental programs (Tier-1 protocols in each regime).

### 6. Open questions
- ζ universality across regimes (single-mode bosonic hypothesis).
- Debye/RC scope limit — which condensed-matter systems are exceptions?
- CPT grounding of γ_dec(k) (beyond first-pass free-streaming / shear-viscosity).
- Connection to ED-Arch Hessian invariant r* = −1.304.
- Quantitative D-values for specific ED-SC-00 Table-1 correspondences.

### 7. Conclusion

### Appendix A: Linearised derivations per regime
- Cavity QED Jaynes-Cummings matching.
- Optomechanics rotating-frame matching (from Aspelmeyer).
- FRAP telegraph reduction.
- Galactic rate-balance computation.
- Cosmological γ_dec(k) derivation.

### Appendix B: Numerical tables
- Cavity-QED experimental systems (~8 groups, D values).
- SPARC 175-galaxy D histogram.
- Finner 25-subcluster D values.
- Predicted cosmic-web k_* at redshifts z = 0, 1, 2, 3.

### Appendix C: Cross-regime reference table
- Regime, γ_dec, ω_sys, D, bifurcation threshold, F0 envelope prediction, testability.

---

## 4. v0.5+ deferrals

Items explicitly deferred from v0.4 to prevent scope creep:

- **Full cosmological-perturbation-theory paper.** v0.4 will derive γ_dec(k) to first-pass physical level (free-streaming + shear viscosity at cosmic-web scale). A proper CPT treatment — ΛCDM background, full transfer function, redshift-dependent k_*, comparison with Euclid / DESI / DES — is paper-scope on its own. v0.5 target.

- **Experimental protocol papers per regime.** v0.4 names the observable in each regime (e.g., FRAP envelope extraction, BTFR-residual-vs-age, cavity-QED photon-counting). Full experimental protocols with noise-budget analysis are methods-paper scope. Deferred.

- **Statistical reanalysis of SPARC / Finner / dwarf data.** v0.4 includes the D histograms computed from published catalogues. Full Bayesian inference of D per galaxy with uncertainties, population-level D distribution, and correlation with environmental parameters — deferred to a separate data paper.

- **Direct ED-SC-00 Table-1 verification.** v0.4 proposes that each of the 22 micro↔macro correspondences in SC-00 Table 1 should have matching D values at both endpoints. Actual computation of D for each pair is deferred — it's 22 independent derivations, each requiring specific (ρ, v) identification. v0.6 target.

- **Connection to ED-Arch r* = −1.304.** v0.4 flags the question (does r* depend on D?). Actual derivation or simulation — deferred. ED-Arch extension paper.

- **Numerical simulation of the envelope prediction per regime.** v0.4 uses analytical F0 estimates. Full simulation of the coupled (ρ, v) system at each regime's parameters, with envelope-extraction analysis, is simulation-paper scope. Possibly a natural ED-SIM-04 target.

- **Connection to foundations of QM.** The ED-09.5 identification of `D_crit = 0.5` with the quantum-classical transition has foundational implications. v0.4 alludes to these; a proper treatment is a philosophy-of-physics paper of its own.

---

## 5. Timeline estimate

Paper-scope v0.4 from v0.3 baseline:

| Section | Expansion effort |
|:-------:|:----------------:|
| §1 Purpose → Introduction | 1 day |
| §2 Template → self-contained derivation + diagram | 2 days |
| §3 Cavity QED → Jaynes-Cummings derivation + systems table | 2 days |
| §4 Condensed matter → 3 additional examples | 3 days |
| §5 Galactic → sample computations + F0 observable | 3 days |
| §6 Cosmological → CPT first-pass + observational hooks | 4 days |
| §7 Synthesis → cross-regime diagram + ζ discussion | 2 days |
| Appendices A–C | 2 days |
| Editing / cold-reader pass | 3 days |
| **Total** | **~3 weeks** |

If pursued in single-topic sessions spaced across normal work, this is a ~1.5–2 month project. If condensed, ~3 weeks focused. Cold-reader passes per section (as we did for v0.2 and v0.3) recommended before moving to the next section.

---

## 6. Go/no-go decisions — RESOLVED 2026-04-20

All six decisions made. v0.4 expansion **GREENLIT**.

- [x] **Cold-reader pass on §4–§6** — done in v0.3.
- [x] **§4 condensed-matter examples** — Spin glass, SC film, BEC. (Liquid crystals and active matter deferred to v0.5+ if needed.)
- [x] **§3 cavity-QED experimental-systems table** — **skipped**. Keep §3 at structural-derivation level only; literature-survey table deferred to a future methods paper.
- [x] **Target venue** — **deferred** until v0.4 draft exists. Tone calibrated to "interdisciplinary physics with ED-corpus context" (between *Foundations of Physics* and *Entropy*); final venue choice made after the draft is reviewable.
- [x] **Claude's role on the byline** — **Acknowledgements** only. ("Derivations and structural reviews developed in collaboration with Anthropic's Claude.")
- [x] **ED-corpus cross-references** — **Hybrid.** Minimal inline references throughout the body, plus a **1-page "ED Framework Background" section** in the front matter (after the Introduction, before §2 Template). The Background should cover: P1–P7 in one paragraph, the unified PDE in one display equation with annotations, ED-09.5 / ED-XX / ED-SC-00 / ED-Arch in one paragraph each, and a one-sentence statement of where this paper sits in the corpus.
- [x] **Effort commitment** — **Start now.** No prerequisite milestone; v0.4 work begins in the next session.

### Implications of the decisions for the paper outline (§3 of this plan)

- **Add "ED Framework Background"** as a new front-matter section between §1 Introduction and §2 Template (per decision #5). ~1 page. Self-contained orientation for readers without ED-corpus familiarity.
- **§3 stays at structural-derivation depth** (per decision #2). Jaynes-Cummings linearisation + canonical mapping + F0 envelope + the κ = Γ aside. No experimental-systems table; cite a few representative groups inline only.
- **§4 condensed matter** develops three exceptions: spin glass near T_g, SC film near T_c, BEC at finite T (per decision #1). Each gets a six-row template table + D calculation + predicted observable, parallel to FRAP.
- **Acknowledgements section** added per decision #4. Standard form.
- **Effort estimate adjustment from decisions #1 and #2:** §3 gets ~1 day shorter (no systems table); §4 stays at 3 days (3 examples were already the recommended default); new ED Framework Background adds ~0.5 day. Revised total: still ~3 weeks focused.

---

*Decisions logged 2026-04-20. v0.4 expansion begins in the next session. v0.3 memo is now the v0.4 baseline; expansions will be appended/expanded in place rather than versioning a new file (consistent with the convention used for `docs/ED-09-5-Observable-Sharpening.md`).*
