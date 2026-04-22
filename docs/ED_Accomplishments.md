# Event Density — Scientific Accomplishments

*Structured inventory of the scientific payload of the Event Density (ED) program: ideas, formulas, numbers, invariants, matches, predictions, derivations, cross-scale correspondences, solver results, and empirical confirmations. Organised by domain for navigation; content preserved verbatim from the accomplishments audit.*

*Generated 2026-04-22; expanded 2026-04-22 (fourth and fifth passes) with the ED-10 geometry / QFT arc closure + acoustic-analogue experimental program. Companion to `ED-Orientation.md` (living program-state reference) — this document lists *what has been demonstrated*; the orientation lists *where it lives and how to re-enter the work*.*

---

## Architectural & Axiomatic

- **Uniqueness theorem for the canonical ED PDE** — the unique second-order scalar PDE satisfying seven derivation axioms (locality, isotropy, gradient-driven flow, dissipative structure, single scalar field, minimal coupling, dimensional consistency); proof by constructive elimination. *Significance:* the PDE is forced by the axioms, not fitted; removes degrees of freedom in the theoretical construction.

- **Three-channel decomposition of the canonical ED PDE** — mobility `M(ρ)∇²ρ + M'(ρ)|∇ρ|²`, penalty `P(ρ)`, participation `H·v(t)` map one-to-one onto *geometry, calculus, dynamics* respectively. Each channel is independently activatable by setting the relevant parameter to zero. *Significance:* enables the six falsifiable structural analogues.

- **Sharp damping-discriminant bifurcation — ζ-parametrised form (2026-04-22 third-pass resolution).** The Canon P6 heuristic `Δ = D + 2ζ → D_crit = 1 − 2ζ = 0.5` is retired. Linearising the canonical PDE around homogeneous equilibrium, Fourier-decomposing, and evaluating the 2×2 coupled eigenvalue discriminant yields the underdamping condition `(D − ζ)² < 4(1 − D)` at reference mode `ε_k·τ = 1`, with critical threshold **`D_crit(ζ) = √(2−ζ)·(2 − √(2−ζ))`**. At canon-default `ζ = 1/4`, **`D_crit ≈ 0.896`**. At `ζ = 0`, `D_crit = 2√2 − 2 ≈ 0.828`. At `ζ → 1`, `D_crit → 1`. Full derivation in [`theory/D_crit_Resolution_Memo.md`](../theory/D_crit_Resolution_Memo.md). The 00.2 heuristic's ~80% error traced to the additive form dropping the coupled `(D − ζ)²` cross-term, flipping the sign of `−2Dζ` → `+4Dζ`, and over-weighting `ζ` by ~2×. Regime A (D=1, H=0) has λ = −ε_k ∈ ℝ<0 unconditionally overdamped (D_crit not defined); Regime B (0<D<1) is where the corrected formula applies. Three verification hooks pass (limits at ζ=0, ζ=1, monotonicity in ζ). *Significance:* closes the highest-priority v0.5+ theory issue (flagged 2026-04-20 in ED-Dimensional-01-Ext Appendix A); the PDE bifurcation is now correctly specified and the ED-09.5 Q-C transition prediction is re-calibrated.

- **Nine architectural laws L1–L9 as theorems of the Canon** — unique attractor (L1), multi-functional Lyapunov dissipation (L2), three-stage spectral concentration (L3), factorial mode-coupling dilution (L4), gradient-dissipation dominance at late times (L5), topological conservation (L6), horizon formation at capacity bound (L7), blobs→filaments→sheets→uniform morphology (L8), sheet-filament oscillation in oscillatory regime (L9). *Significance:* shifts ED from "a PDE" to "a PDE class with proved dynamical consequences."

- **Five universality classes span the complete behaviour of the canonical PDE**: PME, RC, Stefan, Telegraph, Void. No additional classes exist at any parameter choice (X5D/Factor Skyline verification). *Significance:* bounds the phenomenology — any ED-generated dynamics must fall in one of five known classes.

- **Factor-Skyline evaluation passes all six criteria** (Minimality, Locality, Determinism, Generative Sufficiency, Envelope Tightness, Structural Optimality). 28 constraints, ~18 independent, 8 free parameters → overdetermination ratio **2.25**. *Significance:* ED is a structurally over-determined theory in the meta-architectural sense; more constraints than parameters.

- **Two distinct P1–P7 axiom sets cleanly disambiguated** — derivation axioms (determine the PDE form) vs Architectural Canon (specify the structural relations a valid PDE must have); same labels, complementary roles. *Significance:* removes a source of persistent confusion across the paper series and clarifies the axiom-stack layering.

- **18-axiom stack fully enumerated** — 4 ED-05 pre-PDE axioms + 7 derivation axioms + 7 Canon principles. *Significance:* the complete foundational commitments of the framework made explicit and non-overlapping.

- **Test-to-Axiom Mapping Project executed (2026-04-22 second pass)** — four-stage structured project mapping the 18-axiom stack against the four-then-five-now-six empirical tests. Full report at [`docs/ED-Test-to-Axiom-Mapping-v1.0.md`](ED-Test-to-Axiom-Mapping-v1.0.md). **Findings:** (1) Pre-PDE layer (A1–A4) is structurally untested — 0 direct cells across all test columns, 15/20 cells `none`; expected (pre-PDE axioms live on a bare event domain below any PDE-level test). (2) Derivation layer has strong indirect coverage but thin direct coverage (4 direct / 26 indirect / 5 none). (3) Canon layer has densest direct coverage (10 direct / 13 indirect / 12 none), but **C3 Penalty Equilibrium and C7 Nonlinear Triad Coupling have 0 direct cells**. (4) **C7 selected as highest-leverage next-experiment target** on three criteria: most distinctive mechanistic claim (`M′(ρ)|∇ρ|²` generates k=3 from k=1), survives the 2026-04-22 FPv2 §8.4 retraction as the qualitative mechanism, directly measurable via spatial or temporal harmonic analysis. Three execution routes drafted with marginal-coverage-gain-per-unit-cost ranking. *Significance:* converts the ED axiom stack from "18 principles" into a structured coverage matrix with identified under-tested gaps; promotes next-experiment selection from qualitative argument to data-driven prioritization.

- **Pre-registered ED-SC 2.0 motif-filter parameters** — `α = 0.25, L_ray = 2, δ = 0.10` with explicit falsification window `[−1.50, −1.10]` and non-tunability clause. *Significance:* methodological hygiene — the filter cannot be retuned to recover a match, making falsification binding.

- **"Does not derive" list explicit** — ED does not derive general relativity, the Standard Model, measurement-problem resolution, or quantum mechanics as a whole. *Significance:* calibrated scope — the framework knows what it is and is not claiming, which is distinctive among speculative unification proposals.

- **ED-10 geometry / QFT / U(1) / curvature / Schwarzschild arc closed (2026-04-22)** — seven memos closing what ED-10 can and cannot support at the level of explicit calculation. Five durable structural results: (1) kinematic acoustic metric `g^eff_μν = diag(−M(ρ_0(x)), 1, 1, 1)` is real but dynamical geometry is not; (2) Schwarzschild is unreachable under any coordinate transformation via three independent invariant obstructions (flat Euclidean 3-section, Ricci-flat class admits only Minkowski, Kretschmann form incompatible with `48(GM)²/r⁶`); (3) QFT in the reversible slice (`D = 0, ζ = 0`) is free-scalar Klein-Gordon whose canonical quantisation is consistent with Schrödinger-picture evolution — a consistency result, not a derivation of QM; (4) no α, no charge, no local U(1) gauge structure (four structural absences); (5) interior-maximum P4 horizons are acoustically extremal (`κ = 0, T_H = 0` by Visser formula + symmetry). *Significance:* a complete closure of the most speculative interpretive stratum of the framework into (ii)-grade kinematic consistency claims, with hard guardrails against re-drift in future sessions.

- **Acoustic surface gravity identified with ED P4 mobility collapse surface** — horizon locus of the kinematic acoustic metric coincides with Canon P4 (mobility capacity) collapse surface, which coincides with the ED-06 decoupling surface. Three independent structural identifications of the same geometric object. *Significance:* unifies the ED ontology of horizons (decoupling → capacity bound → null-cone collapse) at the kinematic-geometry level.

- **`c_s = √M_0 = c_0 = c/0.6` identification sharpened** — the ED-Dimensional-01 dictionary's `c_0 = L_0/T_0 = c/0.6` is literally the signal speed of the acoustic metric. The 60% mismatch with physical `c` is a **named structural feature** of current ED, not an approximation to be tightened. *Significance:* removes a long-standing ambiguity about the status of the `c/0.6` factor; it is now the explicit acoustic-metric identification, not a hidden scaling.

- **Generative Closure Theorem for the Emergence Universe sandbox** — **exactly 10 sub-mechanism types** exist in the discrete N-particle ring universe; no 11th is possible. Three coordinates (λ temporal regime × 3 approach directions × 3 PBC modes × 3 trajectory regimes) × 98.7% cross-layer consistency. *Significance:* a closure theorem in a proof-of-concept universe demonstrating the thesis that architecture forces laws.

- **Laws I–XIV of the Emergence Universe derived empirically** including Law VIII (five descriptive manifolds unify into one with 98.7% cross-layer agreement), Law IX (the `λ` invariant controls complexity flow), Law XIV (grid-dependent power-law collapse-time scaling `χ ~ λ^p` with `p = −7/3` or `p = −2.81`). *Significance:* demonstrates that "laws as emergent invariants of architecture" is not a philosophical slogan but a rigorously-characterisable phenomenon.

---

## PDE & Numerical

- **Penalty channel ≡ RC discharge at machine precision** — decoupled limit gives `dδ/dt = −DP₀·δ`, λ = DP₀ matched at **0.00%** (identity, not approximation) across multiple H values and amplitudes. *Significance:* an exact mathematical identity between a channel of an ontologically-motivated PDE and a textbook circuit equation.

- **Mobility channel reduces exactly to the 2D porous-medium equation** with exponent `m = β + 1` and effective diffusivity `D_pme = D·M₀/(β+1)` under substitution `δ = ρ_max − ρ`. Barenblatt self-similar front exponent `α_R = 1/(d(m−1)+2)` matched to **1.1%** at `β = 1`. *Significance:* the capacity-bound mobility is not ad-hoc — it reproduces a textbook nonlinear-PDE solution exactly.

- **Mobility + penalty produces Stefan-type transient horizons** with sharp amplitude threshold `A_c = 0.400` predicted, measured `0.410` (**2.5%** error); horizon lifetime monotonic in drive amplitude. *Significance:* ED horizons are a derived free-boundary phenomenon, not an imposed discontinuity.

- **Oscillatory horizons are structurally forbidden (negative result, Analogue 4)** — horizon lifetime `τ_H ~ 0.3–1.5` is shorter than telegraph period `T_osc ~ 2–6` at all tested parameters; L1 (unique attractor) proves the impossibility. *Significance:* ED is falsifiable against its own architectural limits, not just confirmations.

- **Emergent nonlinear-mobility pair repulsion (Analogue 6)** — two-bump initial condition produces centre-of-mass drift rate `+0.168 → +0.066` (decaying with separation) at `H = 0`; telegraph-modulated attraction/repulsion at `H > 0` with `v`–drift correlation `> 0.5`. *Significance:* an emergent effective interaction law not predicted from any single channel in isolation.

- **2D structural analogues extend to 3D without modification** — Barenblatt PME, Stefan horizons, and temporal-tension pair interaction all recur in 3D with only `d`-dependent Laplacian parameter shifts. *Significance:* dimensional consistency (axiom P7) is empirically validated, not merely stipulated.

- **Penalty + participation channels are dimension-independent to machine precision** across `d = 1, 2, 3`; mobility channel shifts per `α_R = 1/(d(m−1) + 2)` exactly. *Significance:* cleanly separates what scales with dimension from what doesn't, at the level of the PDE's coupling structure.

- **ED uniform-limit system is exactly isomorphic to an RLC circuit** — mapping `DP₀ ↔ 1/(R_P C)`, `H ↔ −1/C`, `κ/τ ↔ 1/L`, `ζ/τ ↔ R_L/L`. Machine-precision match at `H = 0.3, 1.0, 5.0` in simulation. *Significance:* converts an abstract ontological PDE into a physically buildable benchtop experiment.

- **Solver-independence result for Analogue 5** — across **three independent numerical methods** (explicit Euler + Neumann, spectral ETDRK2 + periodic, MOL-BDF + periodic), `ω_measured / ω_linear = 1.01 ± 0.04` across 15 runs at `H ∈ {10, 20, 50}`. Linear eigenmode prediction `ω = √((DP₀ζ + HP₀)/τ − γ²)` verified. *Significance:* a specific quantitative claim survives transfer across solver families with no algorithmic overlap.

- **FPv2 §8.4 "54% renormalization" — root cause identified at line level + one-character patch (2026-04-22 first pass).** Traced to [`edsim/phys/analogues/telegraph_pme.py:162`](../edsim/phys/analogues/telegraph_pme.py) — `F_avg = spatial_average(params.D * F_local, dx)` inserts a spurious factor of `D` into the participation ODE's forcing, shifting the off-diagonal coupling from `P₀/τ` to `DP₀/τ`. The resulting eigenmode `ω_coded = √(DP₀(H+ζ)/τ − γ²)` matches all three FPv2 table values (0.1662, 0.2400, 0.3842 at H=10/20/50) to 4-sig-fig precision and asymptotes to `√D · ω_linear ≈ 0.548 · ω_linear` — this is the "54%." **One-character patch applied** (`params.D *` removed) restores `ω_measured ≈ ω_linear` at FFT-bin resolution. Forensic memo at [`analysis/scripts/telegraph_pme/v1.4_bug_diagnosis/memo.md`](../analysis/scripts/telegraph_pme/v1.4_bug_diagnosis/memo.md). **FPv2 §8.4 quantitative 54% claim is retracted**; Analogue-5 qualitative coupling structure + v–δ frequency match survive. *Significance:* supersedes the prior "reclassified as protocol-specific" diagnosis with an exact line-level explanation; demonstrates that the ED program treats its own numerical artifacts with full forensic transparency.

- **v–δ frequency match (the qualitative core of Analogue 5) survives solver-independence audit** — both `v(t)` and `ρ_center(t)` peak in the same FFT bin at every H across all three solvers. *Significance:* the architectural claim (coupled-channel frequency locking) is robust even when one specific quantitative claim is retracted.

- **Scenario-D canonical reference measurement `(n*, σ*) = (2.7, 0.0556)`** with saddle peak at step 457, curvature ratio κ_∥/κ_⊥ ≈ −1.3 ± 0.2. *Significance:* provides a reproducible calibration point for every downstream cross-scale comparison.

- **C7 Nonlinear Triad-Coupling simulation calibration (2026-04-22 second pass).** Monochromatic k=1 seed on the canonical F[ρ] operator (β=2, H=0, 1D periodic spectral) with A₁ swept across three decades yields sharp quantitative invariants: **`K = A₃/A₁³ ≈ 0.0148 ± 0.0005`** (cubic scaling slope = 3.0 ± 0.05 across 3 decades of drive amplitude), companion **`K₂ = A₂/A₁² ≈ 0.279`** (quadratic, constant to 4 sig fig), **exact phase lock `φ₃ − 3φ₁ = π`** (SD ~ 10⁻⁶ rad), and saturation-regime onset at `A₁ ≳ 0.15·ρ_max` where `A₃/A₁` enters the historical ED-Phys-16 "3–6%" band. **The ED-Phys-16 band is therefore a saturation-regime measurement, not a scale-free invariant.** Two protocol corrections forced by the simulation: (a) the scale-free invariant is `K = A₃/A₁³`, not the amplitude-dependent `A₃/A₁`; (b) the original "A₂ < A₃ by odd symmetry" claim is **inverted** — `M′(ρ)|∇ρ|²` sources the second harmonic directly via the DC+2k structure, so `A₂ > A₃` in the clean regime by ~200× (at A₁=0.1, A₂ ≈ 2.4e-3 vs A₃ ≈ 1.2e-5). Simulation code at [`analysis/scripts/telegraph_pme/triad_calibration/`](../analysis/scripts/telegraph_pme/triad_calibration/). *Significance:* upgrades C7 from "qualitative triad-coupling claim" to pre-registered scale-free invariants with 4-sig-fig simulation calibration; the C7 experimental protocol is now quantitatively specified against first-principles simulation rather than retrofit to the historical band.

---

## Cross-Scale Structural

- **Universal nondimensional invariant `D_phys · T₀ / L₀² = 0.3`** holds to machine precision across five regimes — Quantum, Planck, Condensed Matter, Galactic, Cosmological. *Significance:* a single canonical structural parameter anchors physics across **61 orders of magnitude** in length scale via the Dimensional Atlas.

- **Quantum-regime Madelung anchoring: `D_phys = ℏ/(2m)`** derived as a mathematical *theorem* (continuity equation for `|ψ|²` has exactly this diffusion coefficient), not an analogy; combined with `L₀ = ℏ/(mc)` (reduced Compton wavelength) and `T₀ = 0.6 · ℏ/(mc²)`. *Significance:* the quantum-regime anchor is not adjustable — it falls out of existing physics.

- **Planck-regime recovery as a special case of the quantum regime** — substituting the Planck mass gives `L₀ = ℓ_Pl`, `T₀ ≈ 0.6 · t_Pl`. *Significance:* two distinct canonical regimes collapse to one parameter (particle mass).

- **Motif-conditioned median of field-space Hessian eigenvalue ratios `r* ≈ −1.30`** — canonical Scenario D measurement `−1.304` at `(n*, σ*) = (2.7, 0.0556)`; falsification band `[−1.50, −1.10]`; motif filter pre-registered at `α = 0.25, L_ray = 2, δ = 0.10`. *Significance:* a quantitative, pre-registered cross-scale invariant with an explicit algorithmic definition.

- **Cross-scale recurrence of `r* ≈ −1.30`** across **~20 orders of magnitude** — Scenario D simulation, Local Group mass-sheet reconstruction, Casimir-cavity equilibria. *Significance:* the same specific number recurs across three physically unrelated systems; treated as structural identity, not analogy.

- **Twenty-two micro↔cosmological correspondences** catalogued — superconductivity ↔ cosmic filaments, entanglement ↔ void synchronization, Casimir self-assembly ↔ filament formation, etc. *Significance:* a structured vocabulary of scale-free architectural motifs.

---

## Empirical

- **Universal Degenerate-Mobility law `D(c) = D₀(1 − c/c_max)^β`** — mean exponent **β = 1.72 ± 0.37** across **10 chemically distinct soft-matter systems spanning 8 distinct physical mechanisms** (steric jamming, H-bond viscosity, hydrodynamic crowding, short-range attraction, electrostatic + steric, entanglement, polymer crowding, depletion, viscosity divergence). All **R² > 0.986**; range [0.986, 0.999]; zero materials excluded. *Significance:* the canonical mobility form is not curve-fitted per-material; a single functional form works mechanism-agnostically.

- **Theoretical β = 2 agrees with measured mean β = 1.72 ± 0.37 within 1σ.** *Significance:* a first-principles structural prediction matches an empirical mean across independent material systems.

- **UDM cross-technique consistency for BSA — Material #11 Roosen-Runge (2026-04-22 first pass).** Neutron-backscattering BSA fit: **β = 2.15, R² = 0.923** across 5 points in φ ∈ [0.07, 0.30] (Roosen-Runge et al. 2011 PNAS). Cross-technique consistent with the published fluorescence BSA fit (β = 2.12): Δβ = 0.03, within fit uncertainty. **The UDM exponent for BSA is measurement-technique-independent.** Logged in [`experiements/Universal_Mobility_Law_Evidence/UDM_Extension_Log.md`](../experiements/Universal_Mobility_Law_Evidence/UDM_Extension_Log.md) with seven candidate systems (#12–18) pending manual extraction and one rejected dataset (Price 2001 lysozyme) retained with methodological lesson: **UDM requires monomeric conditions; crystallization/aggregation confounds crowding.** *Significance:* upgrades the UDM claim from "single-technique fit per material" to "cross-technique consistent per material"; adds a falsifier (technique-dependent β would break the UDM thesis) that has now been passed by the strongest available independent test for BSA.

- **Cluster merger-lag formula `ℓ = D_T / v_current`** — parameter-free prediction reproduces 7-cluster offset distribution and Finner+25 aggregate of 58 subclusters simultaneously. *Significance:* a single formula derived from the penalty + temporal-tension channels predicts a single-parameter scaling observed in independent datasets.

- **Galactic-regime diffusivity anchor `D_T = 2.1 × 10²⁷ m²/s`** — set independently from Mistele weak-lensing extent, feeds back to predict `D₀` of soft-matter mobility law through the Dimensional Atlas. *Significance:* no fitting between the two regimes — the same constant bridges them.

- **Finner A1.0b pipeline validation** — HP4 7-cluster sample gives `n = −0.90 ± 0.04` vs published `−1.07 ± 0.20` at < 1σ agreement. *Significance:* independent re-analysis using the corrected apocenter-capped formula confirms the published result at higher precision.

- **Dwarf SPARC D_outer separation** — `⟨D_outer⟩_Active = 6.01` vs `⟨D_outer⟩_Quiet = 3.94` across N = 46 dwarf galaxies — **53% separation**. *Significance:* an activity-dependent signature in a regime-bridging sample; qualitative survival under ED-XX environment-sourcing revision.

- **BTFR exponent 1/4 recovered naturally** via the participation-channel interpretation of weak-lensing velocities. *Significance:* ED reproduces a tight empirical scaling without invoking a dark-matter particle or a MOND scale.

- **Environment-sourcing revision of temporal tension (ED-XX)** — 3D Green's function `T(r) ∝ (1/r)·exp(−r/ℓ_T)` shows `1/r` dilution dominates over exponential decay; galactic sources (5–20 kpc) cannot produce flat `T(r)` at 30–1000 kpc; requires source width `σ ≥ 1–3 Mpc` (cosmic web). *Significance:* a self-correction forced by 3D geometry, overturning the earlier galaxy-sourced hypothesis; tightens ED's predictions quantitatively.

- **ED-XX quantitative flatness scan** — flatness error drops from 258% at σ=5 kpc → 71% at 50 kpc → 18% at 500 kpc → **2.7% at σ = 2 Mpc**. *Significance:* a specific source-scale prediction with orders-of-magnitude selectivity.

---

## Predictive

- **ED-09.5 sharp quantum-classical transition** — identification of the canonical PDE's `D_crit = 0.5` bifurcation with the physical quantum-classical boundary. Distinguished from standard decoherence (smooth) and from GRW/CSL/Diósi-Penrose (stochastic) in at least **four jointly measurable signatures**: `N_osc ∈ [8, 19]`, `Q ≈ 3.5–6.3`, third-harmonic content **3–6%**, transition sharpness at specific `D(x) = 0.5`. *Significance:* a novel prediction no existing Q-C account makes in exactly this form.

- **Optomechanics channel-weight mapping `D = γ_dec / (γ_dec + ω_m)`** derived under candidate-(b) identification `v ↔ X_cav`; bifurcation at sideband-resolution threshold `γ_dec = ω_m` — a regime boundary already known in the optomechanics field, now identified with a PDE bifurcation. *Significance:* maps a PDE-internal sharp transition onto an experimental regime boundary that is independently established.

- **Envelope-frequency derivation `ω_v = 2π · N_osc · γ_dec`** for cavity-coupled optomechanics. Predicted envelope period `~63 s` for Delic 2020, `~4 s` for cryogenic membrane. *Significance:* a specific frequency prediction on raw heterodyne `x(t)` invisible to standard optomechanics analysis pipelines.

- **Cavity-derived damping ratio `ζ ≈ 0.5`** (from `Ẋ_cav = −(κ/2) X_cav`) matches canon default `ζ ≈ 0.45` to ~11% — an independent cross-check between the optomechanics identification and the pre-registered ED parameter defaults. *Significance:* consistency check that was not built in by construction.

- **AFM dewetting test protocol** — predicts `med(ℛ_motif) ∈ [−1.50, −1.10]` on PS-on-Si pre-rupture `h(x, y)`; ~$500, ~5 weeks; 5-outcome decision tree. *Significance:* a lab-bench cross-scale test of ED-SC 2.0 executable at undergraduate-lab scale.

- **UDM-FRAP test protocol** — predicts front-radius scaling `R(t) ~ t^(1/6) ≈ t^0.167` in 200–350 mg/mL BSA vs Fickian `t^0.50` — **factor of 3 separation in the exponent**, at `t = 10 s` gives `R_ED ≈ 4.3 µm` vs `R_Fickian ≈ 9.5 µm`, easily resolved by confocal microscopy. *Significance:* a first-principles structural prediction (no free parameters after β fit) testable in one 2-hour session.

- **UDM-FRAP secondary signature: sharp vs Gaussian-blurred bleach boundary** — PME compact support is a qualitative signature independent of β. *Significance:* a second, independent falsification path from the same dataset.

- **ED-09.5 dual-track predictive program** — Track A (Aspelmeyer raw `x(t)` reanalysis at `ω_v ≈ 8·γ_dec`) and Track B (Lomb-Scargle on public FRAP residuals at 80–800 Hz) test the *same* envelope prediction at regimes separated by **~10 orders of magnitude** in `γ_dec`. *Significance:* the same structural claim manifest at different absolute frequencies in different regimes — cross-regime validation built into the experimental program.

- **RLC benchtop pre-registered predictions (four runs)** — Run A: `f = 1574 Hz, Q = 3.3`; Run B: near-critical `Q = 1.25`; Run C: `f = 5027 Hz, Q = 10.5`; Run D: `f = 15911 Hz, Q = 20`. Pass criterion ±10% on all three of ω, γ, Q. *Significance:* hardware-verifiable predictions at ~$50 cost with two decades of L variation and one decade of Q variation.

---

## Interpretive

- **Photonics reframed as five "channel moves"** — removal (bandgap), inversion (negative index), redirection (cloaking), encoding (metasurface phase), composition (generalised metasurface) — each identifying a landmark photonic phenomenon with a specific ED-channel operation. *Significance:* pre-existing physics is recoverable as special cases of a single ED vocabulary, not requiring new mechanism per phenomenon.

- **Quantum-information moves reframed as channel-geometry operations** — global access (superposition), global constraint extraction (Deutsch–Jozsa), rewrite-on-measurement (BB84), identity reassignment (teleportation), symmetry extraction (Shor). *Significance:* quantum-computing primitives are recovered structurally without postulating additional axioms.

- **Topological phases as global invariants of multiply-connected ED channel geometry** — AB, Berry, AC, Tonomura unified as four variants of "global curvature around a multiply-connected channel." *Significance:* topology in physics emerges from a single ED-geometric concept, not four separate mechanisms.

---

## Meta-Architectural

- **Laws, symmetries, and conservation quantities reframed as emergent** — Noether's theorem, gauge invariance, Lorentz symmetry, the Second Law, and conserved quantities (energy, momentum, charge) all derivable as architectural consequences of ED gradient + participation + compositional rules, rather than postulated. *Significance:* a single meta-claim that unifies the empirical, interpretive, and scale-correspondence tracks into one program.

- **"Becoming is primitive" as an ontology inversion** — physics is made of activity (events) before it is made of things (particles/fields); space = participation adjacency, time = commitment order, distance = participation resistance, curvature = gradient structure. *Significance:* a coherent, minimal alternative ontology that is constructive (produces a specific PDE) rather than merely contrarian.

- **Three-track program structure** — empirical (predictions), interpretive (reframings), scale-correspondence (architectural invariants). All three share the same PDE canon and ontology; differ only in goal. *Significance:* a navigation structure that prevents the three kinds of claim from being conflated (a common failure mode in speculative frameworks).

- **Logic-flow diagram as a communication invariant** — 6-step pipeline (4 primitives → 7 demands → unique PDE → 3 channels → empirical anchors → falsifiable predictions) with equation-rich companion. *Significance:* makes the architectural spine legible in a single figure for non-specialist audiences.

- **Complete operational-protocol set for the four-test empirical program** — AFM / UDM-FRAP / ED-09.5-Track-A / ED-09.5-Track-B / RLC — all with pre-registered pass/fail bands, analysis pipelines, decision trees, and cost/timeline estimates. *Significance:* the empirical program is execution-ready at the session-start level; no protocol design remains as a blocker between "theory exists" and "experiment begins."

- **ED Acoustic-Analogue Experimental Program drafted (2026-04-22)** — parent memo at [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../theory/ED_Acoustic_Analogue_Experimental_Program.md) surveys five analogue-gravity platforms (BEC / water tank / optical pulse / slow-light EIT / phononic crystal) and maps ED primitives to analogue observables. Three sibling experiment folders created: **EIT Extremal (full protocol, top priority)**, Optical-Pulse (stub), BEC-Extremal (stub). The EIT experiment toggles a control-field spatial profile within the same atomic cell between monotonic (κ_M > 0) and extremal (κ_E = 0) configurations and compares thermal-emission rates — a within-apparatus differential with PASS criterion `R_E / R_M < 0.1`. *Significance:* pushes the kinematic acoustic-metric result outward into directly testable analogue systems; brings the total pre-registered test count to six (AFM / UDM-FRAP / ED-09.5-A / ED-09.5-B / C7-Triad / EIT-Extremal).

- **Extremal-horizon honesty framing established** — the `κ = 0 at smooth c_s-maximum` result is a **shared** prediction of ED and standard analogue gravity, not ED-unique in isolation. The ED-specific content is the prediction of *which* physical regimes populate the interior-maximum class (Canon P4 mobility-collapse natively produces such horizons in stationary ED profiles). Called out explicitly in the parent memo §3 and in every experiment-folder protocol. *Significance:* prevents future overclaiming — a PASS on an EIT-style test supports the ED-adopted acoustic-metric reading but does not uniquely distinguish ED from other kinematic analogue-gravity frameworks at a single platform. Cross-regime consistency is the real differentiator.

- **Within-apparatus differential methodology adopted as the ED-analogue-test design pattern** — the EIT toggle experiment is the first ED experiment to use within-apparatus differentials (same cell, same detection chain, toggled configuration) instead of absolute measurements with external controls. Same methodology flagged for the Optical-Pulse peak-vs-flank test. *Significance:* a cleaner class of experiment because the most systematic drifts cancel in the ratio; a pattern other ED predictions should be re-examined against.
