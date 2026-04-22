# ED Orientation

**Status.** Living single-file orientation reference for the Event Density (ED) framework. Updated in place as the program evolves — no version freezing, no v1.x file chain. Last substantive update: 2026-04-22 (fifth pass — acoustic-analogue experimental program).

**Citation form.** Cite by section, not by version. Example: "ED-Orientation §6.9" for the ED-SC 2.0 invariance statement. If a point-in-time snapshot is ever needed for an external paper citation, use git's commit SHA of this file rather than a version number in the filename.

**How to use.** Read §1 first (scope + discrepancy map with repo). §3.1 disambiguates the two P1–P7 axiom sets (derivation vs. Canon). §5.9 is the meta-claim (laws / symmetries as emergent). §6.9 is the current canonical cross-scale invariance statement (ED-SC 2.0). **§7 is the five-test empirical-status table** with links to all five operational protocols (AFM / UDM-FRAP / ED-09.5 Track A / ED-09.5 Track B / C7 Triad-Coupling). **The Test-to-Axiom Mapping Report at [`docs/ED-Test-to-Axiom-Mapping-v1.0.md`](ED-Test-to-Axiom-Mapping-v1.0.md)** is the 18×5 coverage matrix that drove the C7 addition. §11 is the Emergence-Universe sandbox (pre-ED proof-of-concept). §2 for the paper trajectory. §8 for full inventory (Desktop + PhilArchive + GitHub). §9 for question-type routing.

**Recent substantive updates (in descending chronological order — move each up when you supersede it, delete items once they're fully absorbed into the body text):**

- **2026-04-22 (fifth pass).** **ED acoustic-analogue experimental program drafted — one parent memo + three sibling experiment folders.** Following the seven-memo geometry/QFT/Schwarzschild closure (fourth-pass entry below), the natural expansion direction was chosen over further narrowing: push the kinematic acoustic-metric + extremal-horizon results outward into testable condensed-matter analogue systems. **Parent memo** at [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../theory/ED_Acoustic_Analogue_Experimental_Program.md) surveys five analogue-gravity platforms (BEC, water tank, optical pulse, slow-light EIT, phononic crystal), maps ED primitives (`M(ρ), ρ_0, F[ρ]`) to analogue observables (`c_s(x), n(x), v_g(x)`), and ranks experiments by ED-distinguishing power × tractability. **Critical honesty framing held throughout:** the `κ = 0 at smooth c_s-maximum` result is a kinematic property of any acoustic metric, **not ED-specific in isolation** — it is a shared prediction of ED and standard analogue gravity for the same horizon class. The ED-specific content is (a) Canon P4 mobility-collapse forces interior-maximum horizons natively (not engineered); (b) ED predicts *which physical regimes* populate the interior-max class; (c) cross-regime linkage under one PDE. **Three sibling experiment folders created** under `experiements/`: (1) [`ED-Acoustic-EIT-Extremal_InProcess/`](../experiements/ED-Acoustic-EIT-Extremal_InProcess/) — **full session-ready protocol, top priority** — slow-light / EIT within-apparatus differential toggling control-field spatial profile between monotonic (κ_M > 0) and extremal (κ_E = 0) configurations in the same Rb cell; primary observable `R_E / R_M` (thermal-emission ratio), PASS criterion `< 0.1`; Lukin / Hau / Halfmann / Lvovsky / LKB-Paris collaboration targets; ~3–6 months end-to-end with an SLM-shaped EIT apparatus. (2) [`ED-Acoustic-OpticalPulse_InProcess/`](../experiements/ED-Acoustic-OpticalPulse_InProcess/) — **stub** — fibre-pulse peak-vs-flank within-pulse differential; blocked on Belgiorno-2010-controversy apparatus-specific noise characterization + peak-vs-flank spatial-distinguishability confirmation; Philbin / König / Faccio / Leonhardt targets. (3) [`ED-Acoustic-BEC-Extremal_InProcess/`](../experiements/ED-Acoustic-BEC-Extremal_InProcess/) — **stub** — Steinhauer-style engineered extremal BEC horizon; blocked on (i) moving-background ED theory extension (`v_0 ≠ 0`), (ii) GPE trap+flow co-design, (iii) differential-configuration protocol. **New row for the §7 empirical-status table** will need adding on next pass; currently stands at six tests (AFM / UDM-FRAP / ED-09.5 Track A / ED-09.5 Track B / C7 Triad Coupling / EIT Extremal). **Scope guardrail reiterated in the parent memo and all three experiment folders:** claims are (ii)-grade kinematic acoustic-metric consistency; no Einstein emergence, no Hawking-from-curved-spacetime, no α, no gauge. See [`memory/project_ed10_geometry_qft_scope.md`](../../.claude/projects/C--Users-allen-GitHub-Event-Density/memory/project_ed10_geometry_qft_scope.md). **Deferred theory targets** flagged in parent memo §9: moving-background metric extension (prerequisite for BEC test), curvature-level mode-mixing predictions beyond leading-κ, cross-regime signal-speed consistency check.

- **2026-04-22 (fourth pass).** **ED-10 geometry / QFT / U(1) / curvature / Schwarzschild arc consolidated — seven memos, five durable closures.** The session arc from ED-10's legacy "Einstein's equations = large-scale summary of ED gradients" claim through canonical quantisation, emergent-U(1) scoping, effective acoustic metric, curvature computation, and Schwarzschild coordinate-equivalence is now a closed thread. **Five structural results that must remain stable across future sessions:** (a) **Kinematic geometry is real; dynamical geometry is not.** Linearised ED on a stationary `ρ_0` background carries a genuine acoustic metric `g^eff_μν = diag(−M(ρ_0(x)), 1, 1, 1)`; null cones set fluctuation causality and the horizon locus coincides with Canon P4 mobility-collapse / ED-06 decoupling — but `g^eff` is slaved to `ρ_0`, never dynamical, and no Einstein equation emerges. (b) **Schwarzschild is unreachable under any coordinate transformation** (three independent invariant obstructions: flat Euclidean 3-section, Ricci-flat class admits only Minkowski, Kretschmann form incompatible with `48(GM)²/r⁶`). (c) **QFT in the reversible slice is free scalar, nothing more** — at `D = 0, ζ = 0`, linearised ED is massive Klein-Gordon, canonical quantisation gives Schrödinger-picture evolution of a free-scalar Fock space; this is a **consistency** with QFT, not a derivation of QM from ED axioms. (d) **No α, no charge, no U(1) gauge in ED** — four structural absences (no EM sector, no charge primitive, no local gauge, no Lorentz); the underdamped complex field `ψ` is a complex-diagonalisation tautology; triad coefficients `C ≈ 0.03, K ≈ 0.0148` are **ED's own architectural dimensionless constants, not α** — do not conflate. (e) **Interior-maximum P4 horizons are acoustically extremal** (`κ_acoustic = 0, T_H = 0` by symmetry and by Visser formula); finite Hawking-like temperature requires monotonic/boundary profiles, not generic stationary ED. Plus: the ED-Dimensional-01 `c_0 = L_0/T_0 = c/0.6` dictionary **is** the acoustic-metric signal speed — the 60% mismatch is a structural feature, not an approximation. **Seven authoritative memos (do not re-scope without reading these):** [`theory/ED_Geometry_Emergence_Scoping.md`](../theory/ED_Geometry_Emergence_Scoping.md) (i/ii/iii-grade taxonomy + §8C weak-form ED-10 rewording), [`theory/Fine_Structure_Constant_Scoping.md`](../theory/Fine_Structure_Constant_Scoping.md) (α dead-end + "ED has its own dimensionless constants" language), [`theory/Emergent_U1_in_ED_Scoping.md`](../theory/Emergent_U1_in_ED_Scoping.md) (ψ-phase scoping; global U(1) is tautology, no local gauge), [`theory/ED_Reversible_Sector_QFT.md`](../theory/ED_Reversible_Sector_QFT.md) (canonical quantisation; §7C honest ED-10 rewording), [`theory/ED_Effective_Acoustic_Metric.md`](../theory/ED_Effective_Acoustic_Metric.md) (explicit `g^eff` derivation; horizon ↔ Canon P4 identification), [`theory/ED_Acoustic_Metric_Curvature.md`](../theory/ED_Acoustic_Metric_Curvature.md) (Gaussian-bump closed-form curvature; extremal-horizon finding), [`theory/ED_Schwarzschild_Obstruction.md`](../theory/ED_Schwarzschild_Obstruction.md) (invariant-level proof no ρ₀ reaches Schwarzschild). **Durable memory:** [`memory/project_ed10_geometry_qft_scope.md`](../../.claude/projects/C--Users-allen-GitHub-Event-Density/memory/project_ed10_geometry_qft_scope.md) records the five closures + six guardrails for future sessions. **§5 ontology dictionary lines for "Einstein's equations" and "Schrödinger evolution" updated to their honest weak forms below.**

- **2026-04-22 (third pass).** **D_crit discrepancy resolved — Canon P6 single-number `D_crit = 0.5` retired in favour of the ζ-parametrised linearised form.** Full derivation in [`theory/D_crit_Resolution_Memo.md`](../theory/D_crit_Resolution_Memo.md). Linearising the canonical PDE around homogeneous equilibrium, Fourier-decomposing, and evaluating the 2×2 coupled-eigenvalue discriminant yields the underdamping condition `(D − ζ)² < 4(1 − D)` at reference mode `ε_k·τ = 1`, with critical threshold **`D_crit(ζ) = √(2−ζ)·(2 − √(2−ζ))`**. At canon-default `ζ = 1/4`, `D_crit ≈ 0.896`. At `ζ = 0`, `D_crit = 2√2 − 2 ≈ 0.828`. At `ζ → 1`, `D_crit → 1`. **The 00.2 Canon P6 heuristic `Δ = D + 2ζ, critical at Δ = 1 → D_crit = 1 − 2ζ = 0.5`** is not recoverable as any principled limit of the full discriminant (attempting to match via ε-rescaling yields the quadratic `4ε² − 36ε + 1 = 0` with roots ~8.97 and ~0.028, neither at the canonical `ε = 1`). **Root cause of the heuristic's ~80% error:** the additive form drops the coupled cross-term `(D − ζ)²` of the true discriminant, flips the sign of the cross-coupling (replacing `−2Dζ` with `+4Dζ`), and over-weights `ζ` by ~2×. **Ruled out as sources of the discrepancy:** dimensionality (per-mode eigenvalue problem is scalar in any `d`), mobility form (enters only via `M₀ = M(ρ*)` at linear order — β=1, β=2, SY2 all identical at linear order), penalty form (both linear and SY2 linearise to `P₀·δρ`), definitional ambiguity (both forms use `trace² = 4·det`). **Regime A (D=1, H=0, mobility-penalty only) has λ = −ε_k ∈ ℝ<0** — unconditionally overdamped, `D_crit` not defined in that regime. **Regime B (0<D<1) is where Canon P6 lives** and where the corrected formula applies. **Three verification hooks pass** (limits at ζ=0, ζ=1, monotonicity in ζ). §3 Canon P6 row and §4 three-regimes table updated. The "highest-priority v0.5+ theory issue" flagged 2026-04-20 in [`theory/ED-Dimensional-01-Ext.md`](../theory/ED-Dimensional-01-Ext.md) Appendix A is closed.

- **2026-04-22 (second pass).** **Test-to-Axiom Mapping Project executed; C7 identified as most load-bearing under-tested axiom; triad-coupling simulation calibration completed; experimental protocol drafted.** Four-stage structured project mapping the 18-axiom ED stack (4 ED-05 pre-PDE + 7 derivation + 7 Canon) against the four current empirical tests (AFM, UDM-FRAP, ED-09.5 Track A/B, RLC). Full report at [`docs/ED-Test-to-Axiom-Mapping-v1.0.md`](ED-Test-to-Axiom-Mapping-v1.0.md). **Findings:** (1) Pre-PDE layer (A1–A4) is structurally untested — 0 direct cells across all 5 test columns, 15/20 cells `none`; this is expected (pre-PDE axioms live on a bare event domain below any PDE-level test). (2) Derivation layer has strong indirect coverage but thin direct coverage (4 direct / 26 indirect / 5 none). (3) Canon layer has densest direct coverage (10 direct / 13 indirect / 12 none), but **C3 Penalty Equilibrium and C7 Nonlinear Triad Coupling have 0 direct cells**. (4) **C7 selected as highest-leverage next-experiment target** — most distinctive mechanistic claim (`M′(ρ)|∇ρ|²` generates k=3 from k=1), survives the 2026-04-22 FPv2 §8.4 retraction as the qualitative mechanism behind Analogue 5, and is directly measurable via spatial or temporal harmonic analysis. **Triad-coupling simulation companion run** ([`analysis/scripts/telegraph_pme/triad_calibration/`](../analysis/scripts/telegraph_pme/triad_calibration/)) on the canonical F[ρ] operator (β=2, H=0, 1D periodic spectral) confirms C7 with sharp quantitative invariants: `K = A₃/A₁³ ≈ 0.0148 ± 0.0005` across 3 decades of drive amplitude (cubic scaling slope = 3.0 ± 0.05), companion `K₂ = A₂/A₁² ≈ 0.279` (quadratic, constant to 4 sig fig), exact phase lock `φ₃ − 3φ₁ = π` (SD ~ 10⁻⁶ rad), and saturation-regime onset at `A₁ ≳ 0.15·ρ_max` where `A₃/A₁` enters the historical ED-Phys-16 "3–6%" band — **meaning the ED-Phys-16 band is a saturation-regime measurement, not a scale-free invariant.** **Two protocol corrections forced by the simulation:** (a) the scale-free invariant is `K = A₃/A₁³`, not the amplitude-dependent ratio `A₃/A₁` — the retired `[0.02, 0.08]` band is kept only as an optional saturation-regime cross-check; (b) the original "A₂ < A₃ by odd symmetry" claim is **inverted** — `M′(ρ)|∇ρ|²` sources the second harmonic directly via the DC + 2k structure of `|∇ρ|²`, so `A₂ > A₃` in the clean regime by ~200× (at A₁=0.1, A₂ ≈ 2.4e-3 vs A₃ ≈ 1.2e-5). **New experiment folder created** at [`experiements/Triad-Coupling-C7_InProcess/`](../experiements/Triad-Coupling-C7_InProcess/) with `protocol.md` (full session-ready protocol, revised decision tree with `K, K₂, α₃, α₂, Δφ` criteria), `README.md` (folder-level summary), and [`RLC_ExecutionPlan_v1.0.md`](../experiements/Triad-Coupling-C7_InProcess/RLC_ExecutionPlan_v1.0.md) (concrete bench plan for Alternative 1). **Three execution routes ranked by marginal coverage gain per unit cost:** (1) **Top-1 AFM Spinodal-Dewetting Fourier Triad Reanalysis** — $0–500, 1–6 weeks, reuses T1 pipeline; AFM acquisition specification drafted: 2 samples × 8 logarithmically-spaced anneal frames (30 s to 32 min), 10×10 μm scan at 512², ≤0.1 nm height resolution — **existing pilot data is insufficient** (only 1 frame, no physical-scale calibration, cannot sweep A₁); new acquisition required. (2) **Alt-1 Nonlinear RLC Third-Harmonic Generation** — ~$2–152, 2–3 days, anti-parallel 1N4148 diodes across C in an L=10 mH / C=1 μF / R=10 Ω rig (f₀ ≈ 1591 Hz), 6-point amplitude sweep 20 mV → 2 V, expected `α₃ ≈ 3.0` and `Δφ ≈ π` but `K₂ ≈ 0` because the symmetric clipper suppresses A₂ — note: tests the scaling exponent and phase lock, NOT the K absolute value. (3) **Alt-2 Patterned-FRAP k=3 Recovery** — ~$2000–5000, 4–8 weeks, cleanest mapping to C7 in the UDM β=2 canonical setting, highest cost. **Theoretical companion (simulation) is COMPLETED** 2026-04-22 and the pre-registered §2 test parameters in [`protocol.md`](../experiements/Triad-Coupling-C7_InProcess/protocol.md) are now calibrated against it. **Coverage matrix deltas on execution:** AFM → T1×C7 indirect→direct; RLC → T4×C7 none→direct (scaling only); FRAP-patterned → T2×C7 indirect→direct.

- **2026-04-22.** **Four session captures — FPv2 §8.4 bug root-caused, UDM extended, RLC benchtop procured, CP FRAP quote received.** (1) **FPv2 §8.4 "54% renormalization" root cause identified at line level.** Traced to `edsim/phys/analogues/telegraph_pme.py:162` — `F_avg = spatial_average(params.D * F_local, dx)` inserts a spurious factor of `D` into the participation ODE's forcing, shifting the off-diagonal coupling from `P₀/τ` to `DP₀/τ`. The resulting eigenmode `ω_coded = √(DP₀(H+ζ)/τ − γ²)` matches all three FPv2 table values (0.1662, 0.2400, 0.3842 at H=10/20/50) to 4-sig-fig precision, and asymptotes to `√D · ω_linear ≈ 0.548 · ω_linear` — this is the "54%." **One-character patch applied** (`params.D *` removed) restores `ω_measured ≈ ω_linear` at FFT-bin resolution. Forensic: [`v1.4_bug_diagnosis/memo.md`](../analysis/scripts/telegraph_pme/v1.4_bug_diagnosis/memo.md) + `diagnostic_runs.py`. CHANGELOG `[Unreleased] — 2026-04-22` entry in place. v1.3 architectural-followthrough drop-in correction upgraded from "solver-specific" (general) to "one-character patch" (definitive). **FPv2 §8.4 quantitative 54% claim is retracted**; Analogue-5 qualitative coupling structure + v–δ frequency match survive. §9 routing row "Does Analogue 5 predict a 54% renormalization?" updated with line-level answer. (2) **[`UDM_Extension_Log`](../experiements/Universal_Mobility_Law_Evidence/UDM_Extension_Log.md)** created — running log of post-publication UDM material additions. **Material #11 Roosen-Runge BSA (2011 PNAS, neutron backscattering)** fit added: β = 2.15, R² = 0.923 over 5 points in φ ∈ [0.07, 0.30]. Cross-technique consistent with the published fluorescence BSA fit (β = 2.12): Δβ = 0.03, within fit uncertainty — **the UDM exponent for BSA is measurement-technique-independent.** Seven candidate systems (#12–18: lysozyme Price 1999, SDS Stilbs 1982, CTAB Stilbs 1981, mAb Hung 2024, AOT microemulsion, Ludox 25 nm Philipse 1988, CI2 in crowders McGuffee 2010) logged pending manual extraction. **One rejected dataset (Price 2001 lysozyme)** recorded with methodological lesson: UDM requires monomeric conditions; crystallization/aggregation confounds crowding. Three single-point consistency-check systems (GFP cytoplasm Nenninger 2010, GFP nucleus Bancaud 2009, BSA tracer Balbo 2013) logged separately. §7 + §9 UDM rows updated to link the extension log. (3) **RLC benchtop analogue components ordered from AstroAI** — 180PCS 15-value metallized film capacitor kit + resistor kit + breadboard. Uniform-limit coupling structure (v1.0 linear-regime telegraph PME validates this in a 2D PDE setting) is now procurable as a lab experiment. §7 RLC row updated. (4) **Creative Proteomics UDM-FRAP quote received: ~$1500/sample**, forwarded to technician team for review. Decision window 2026-04-24 to 2026-05-01. §7 UDM-FRAP row updated. **No new body-text sections**; these are operational status captures.

- **2026-04-21 (late, second pass).** **Three operational predictive-experiment protocols captured; FRAP label corrected.** Parallel to the AFM protocol written earlier today, two more session-ready operational docs are now in place covering the complete ED predictive-experiment suite: (1) [`FRAP-High-BSA protocol`](../experiements/FRAP-High-BSA_InProcess/protocol.md) — captures the 2-page protocol submitted to Creative Proteomics on 2026-04-17 (BSA-FITC, 4 concentrations 200–350 mg/mL, 5 bleaches each, full TIFF stacks) verbatim as §4–§8, adds ED theoretical derivation (`R(t) ~ t^(1/6)` from 2D Barenblatt PME with canonical `β = 2`, §2), the post-session analysis pipeline (radial-profile → front-detection → power-law fit → PME-vs-Fickian AIC, §9), a 5-outcome decision tree (§10), and 7 review-level notes for a V2 protocol (§13, including pre-asymptotic regime simulation-calibration and axial-geometry z-stack option); (2) [`ED-09-5-Envelope protocol`](../experiements/ED-09-5-Envelope_InProcess/protocol.md) — two tracks: **Track A** (Aspelmeyer optomechanics raw-`x(t)` reanalysis, blocked on email response) and **Track B** (self-contained Lomb-Scargle on public FRAP recovery-curve residuals at 80–800 Hz). Both tracks test the same §15(β) envelope prediction `ω_v = 2π·N_osc·γ_dec` at regimes separated by 10+ orders of magnitude in `γ_dec`. **Track B runs this week at $0 with no third-party dependency — the fastest path to a new ED empirical result in the program.** **Label correction applied to §7 empirical-status table:** the row previously labelled "Participation (lab) | FRAP protocol" was actually a **mobility-channel** test (UDM `R(t) ~ t^(1/6)`), not a participation test. Corrected to "Mobility (lab, BSA)" and split into two rows to disambiguate from the ED-09.5 FRAP-side participation test. Logged as §10 canonical correction. **The four-test ED empirical program is now fully documented at protocol-execution level:** AFM (architectural, mobility-curvature), UDM-FRAP (mobility), ED-09.5 Track A (participation, cavity-coupled), ED-09.5 Track B (participation, condensed-matter FRAP). Each has a session-ready protocol with pre-registered parameters, analysis pipeline, and decision tree.

- **2026-04-21 (late).** **PhilArchive survey + Emergence-Universe repo absorbed.** Two major gaps closed: (1) full PhilArchive publication list re-fetched (24 papers in attribution order) — **five ED publications that were not in the prior inventory have been added:** ED-01 `Event Density and the Architecture of the Universe` (the true founding paper, pre-dates ED-02), `Event Density: Open Note for Experiments` (falsifiable-test catalogue across all five regimes), `Event Density and the Architecture of Physical Law: Symmetry, Constraint, and Emergent Regularity` (ED-Phys, **symmetries and conservation laws as emergent, not fundamental** — a major philosophical claim missing from the empirical/interpretive/scale-correspondence framing), plus both **Factor Skyline** papers (applied number-theory thread, not physics). (2) **github.com/allen-proxmire/emergence-universe** cloned via the GitHub API — this is the **Emergence Universe / ED-SIM sandbox**, a separate project from `edsim/` in this repo and from the ED-SIM-02/ED-SIM-3D continuum solver. It is a **pre-ED** (or **proto-ED**) deterministic particle-based testbed where "laws are the invariants forced by architecture and constraint" — 36 ED-Arch papers organised as 00 Foundations / 01–19 Developmental / 20–35 fourteen Laws (I–XIV), plus the `ED-SIM-Code/` directory that **contains the reference Scenario-D implementation** referenced in §6.9 ED-SC 2.0 (`ED_Update_Rule.py` is the canonical mobility-weighted 2D-lattice solver). The 14 laws culminate in **Law XIII (Generative Closure): exactly 10 sub-mechanism types exist, no 11th is possible** — a closure theorem for a discrete particle universe. Four new body sections: **§5.9** (Architecture of Physical Law paper), **§11** (Emergence Universe / ED-SIM sandbox + disambiguation from ED-SIM-02/3D), **§12** (Factor Skyline program — number theory), **§2 trajectory table rebuilt** to include ED-01, Open Note, ED-Phys Architecture of Physical Law, UDM paper, Cluster Merger-Lag paper (previously unlabelled as PhilArchive), and the two Factor Skyline entries. §8 PhilArchive inventory also rebuilt. **The most architecturally important addition is §5.9** (Architecture of Physical Law): symmetries, conservation laws, and gauge invariances are *emergent architectural consequences* of ED gradient / participation structure, not fundamental postulates — this unifies the three ED tracks (empirical / interpretive / scale-correspondence) under a single meta-claim about the nature of physical law itself.

- **2026-04-21.** **Desktop/ED Important Papers/ fully read.** Finished absorbing the remaining unread content: `WHAT_IS_ED.md` (one-page overview), `ED_Foundational_Paper.md` (v1) + `ED_Foundational_Paper_v2.md` (expanded with 6 structural analogues), `ED-Math-01_Uniqueness_Well-Posedness_and_Architectural_Laws.md` (Theorem 2.1 + nine laws L1–L9), `ED-Dimensional-01_Quantum_Regime.md` (full quantum dictionary with `D_phys = ℏ/2m` Madelung anchoring), `ED-Dimensional-Master_The_Unified_Atlas.md` (5-regime cross-scale atlas, `D_phys·T₀/L₀² = 0.3` across 61 orders of magnitude), `Appendix_G_3D_Analogues.md` (validates 2D structural analogues in 3D), `ED-Data-01_Condensed_Matter_Mobility_Test.md` (UDM test pipeline), `ED-Data-Galaxy-01_First_Halo_Edge_Test.md` (Barenblatt halo edge prediction — pre-ED-XX framing), `X5D_Evaluation_EventDensity.md` (Factor Skyline structural-optimality evaluation — ED passes all 6 FS criteria, 28 constraints ~18 independent, 8 parameters, 18→8 overdetermination), and spot-reads from `Desktop/ED Archive/` (`what ED Laws are.txt`, `ED in one sentence.txt`, `ED from the outside readme maybe.txt`) plus `Desktop/ED Archive/ED Repo_Claude Review Prompts.md` (eight audience-tuned "what is ED?" prompt variants). **Three new orienting additions to the body of this document:** §3.1 disambiguates the **two distinct P1–P7 axiom sets** (derivation axioms from the Foundational Paper / ED-Math-01 vs. architectural Canon from 00.2 — these are complementary, not contradictory, and the same label has confused prior sessions); §5.6 captures the **nine architectural laws L1–L9** and the **Theorem 2.1 uniqueness statement** from ED-Math-01 (the formal proof that the canonical ED PDE is the unique second-order scalar PDE satisfying the seven derivation axioms); §5.7 captures the **six structural analogues** from Foundational Paper v2 (penalty → RC/Debye @ 0.00% error, mobility → Barenblatt PME @ 1.1%, mobility+penalty → Stefan horizons @ 2.5%, all-three → no oscillatory horizons (negative result), mobility+participation → telegraph-modulated PME @ 0.03% v–δ match, two-peak temporal tension → emergent nonlinear-mobility repulsion); §6.10 captures the **Factor Skyline evaluation** (X5D). §8 inventory updated — all `ED Important Papers/` files are now `✓ read`. ED-Dimensional-01 Quantum's **superluminal `V_0 = c/(2·0.3) ≈ 1.667c`** is explicitly flagged as a consequence of the parabolic PDE's infinite propagation speed (same property as the Schrödinger equation) — it is a scale conversion factor, not a signal speed. No new empirical results; this is a documentation-absorption update.

- **2026-04-20.** **AFM dewetting empirical track is now ED's highest-certainty near-term test.** ED-SC 2.0 §3 specifies a sharp falsification criterion for the motif-conditioned median of the field-space Hessian on 2D scalar density fields: `med(ℛ_motif(h(x,y))) ∈ [−1.50, −1.10]` for thin-film polymer dewetting in the spinodal pre-rupture regime. Standard AFM resolutions (50 nm lateral, 0.1 nm vertical) satisfy the §3 sampling requirement `Δx ≤ L_coh/8` by construction. **Pilot result (N=1, ℛ_all not ℛ_motif):** Scenario D simulation and one thin-film pilot frame agree at median = −2.063 vs −2.149, with overlapping IQRs ([−3.43, −1.49] vs [−3.96, −1.47]) and matching % in target band (21.7% vs 23.0%). The values fail the [−1.5, −1.1] band when read as ℛ_all, but the cross-system agreement is structurally suggestive that ℛ_all may carry architectural information beyond ED-SC 2.0's strict motif-conditioned claim. Real AFM data with `L_coh ≥ ~16 px` would unlock the motif filter. **Three routes to data, in increasing cost and certainty:** (1) browser-check 2023 *Nature Comm Phys* paper for accessible AFM data — 5 minutes; (2) email Jacobs group — second-cheapest, builds field connections; (3) book a 1–2 day session at any academic core facility with PS-on-Si dewetting samples — guaranteed canonical data by construction. **This is structurally separate from the ED-09.5 / Aspelmeyer / FRAP empirical track** — it tests ED-SC 2.0 (architectural invariants), not the Q-C transition. ED now has two independent empirical tracks running. **Operational recommendation:** execute Route 1 immediately; chain to 2/3 based on what Route 1 returns. AFM is the highest-certainty empirical path because it has a guaranteed-success physical-acquisition fallback (Route 3) that doesn't depend on any third party. New row added to §7 empirical-status table. **Route 3 is now operationalized** in [`AFM-Dewetting protocol`](../experiements/AFM-Dewetting-ED-SC_InProcess/protocol.md) — a session-ready canonical protocol (captured 2026-04-21) covering sample prep, scan parameters, data export, pre-analysis quality gates (including the pilot's root-cause fix: the `L_coh ≥ 8·Δx` sampling condition verified per-frame), ensemble statistics, and a five-outcome decision tree (PASS / NEAR-PASS / FAIL / UNDECIDABLE / SPLIT). Budget: ~$500 + ~2 weeks analysis for a complete N=5 samples × 10 frames run. Expected timeline to publishable result: 4–6 weeks from protocol adoption.

- **2026-04-20.** **Vienna ecosystem ED-09.5 program map produced.** Six www.quantumnano.at sub-page reviews (quantum-classical, optomechanics-cooling, single-molecule-detection, quantum-biomolecules, quantum-chemistry, universal-matter-waves) plus an Aspelmeyer-group research-page review. Synthesised into a single operational backbone at [`ED_Vienna_Program_Map.md`](ED_Vienna_Program_Map.md): 12 active targets across two empirical pillars (Pillar A = candidate-(b) cavity-coupled, Pillar B = candidate-(c) internal-mode) plus two cross-checks (OTIMA-vs-KDTL same-molecule cross-instrument; KDTL/LUMI/MUSCLE longitudinal mass meta-analysis) plus a periphery (rotational matter-wave future, single-molecule imaging) and an explicit closure (naïve mass-threshold ED-09.5 in matter-wave is empirically dead per the MUSCLE 175 kDa record). New entries surfaced by the reviews: Riedinger 2016 photon-phonon non-classical correlations as a parallel observable to Delic ringdown; **Schmöle 2016 small-scale gravity** as a candidate Pillar G (ED-XX-extension territory, tests gravity-as-quantum at table-top scales) — needs theoretical extension of ED-XX's 1/r dilution argument from cosmic-web to lab scale. **Aspelmeyer email v3** drafted at [`ED-09-5-Experimental-Strategy.md`](ED-09-5-Experimental-Strategy.md) §7; ready to send pending affiliation/email line + cold-reader pass. Companion v0.4-final memo [`ED-09-5-Observable-Sharpening.md`](ED-09-5-Observable-Sharpening.md) for attachment.

- **2026-04-20.** **Rate-balance template extended to a paper-scope cross-regime atlas.** v0.4-final at [`../theory/ED-Dimensional-01-Ext.md`](../theory/ED-Dimensional-01-Ext.md): full Jaynes-Cummings linearised matching for cavity-QED, four condensed-matter exception classes (FRAP / spin glass / SC film / BEC), galactic six-row tables (MW / dwarf / cluster) with `γ_env + H₀` resolution, cosmological scale-dependent `γ_dec(k) ≈ k v_pec` giving `k_* ≈ 0.23 h Mpc⁻¹` (`λ_* ≈ 27 Mpc`, corrects v0.3's arithmetic-slipped ~10 Mpc), seven-section synthesis with two cross-result consistency checks (ED-04.5 dwarf D_outer 53% separation; cosmic-web scale convergence with ΛCDM `k_NL ≈ 0.2 h Mpc⁻¹`). **Substantive open issue surfaced in Appendix A:** the canonical PDE's 2D linearised underdamping condition `(D − ζ)² < 4(1 − D)` yields `D_crit ≈ 0.9` for canon-default ζ = 1/4, NOT the heuristic `D_crit = 0.5` claimed by Canon P6's `Δ = D + 2ζ → D_crit = 1 − 2ζ`. The heuristic is a ~50% approximation; resolution requires going back to the 00.3 derivation of P6 to determine which discriminant is intended. Logged as the highest-priority v0.5+ theory issue. The v0.4-final paper is **not** for standalone publication — its role is corpus reference and methods-track support for empirical papers (Aspelmeyer email + FRAP reanalysis + AFM). **Honest assessment:** the rate-balance work tightens ED's internal bookkeeping but does not by itself elevate ED externally. Elevation comes from empirical results in the AFM and ED-09.5 tracks above.

- **2026-04-17.** **ED Logic-Flow diagrams — two versions.**
  - Narrative version (Galaxy-15 → Cluster Merger-Lag rename applied): [`figures/ED-Logic-Flow.png`](figures/ED-Logic-Flow.png). Shows the story: four ingredients → seven demands → unique PDE → three channels → evidence, plus four structural forks (D_nd = 0.3, D_crit = 0.5, ED-SC 2.0 saddle, ED-SIM-3D dimensional consistency). Companion walkthrough: [`ED-Logic-Flow.md`](ED-Logic-Flow.md). Source: [`../analysis/scripts/generate_ed_logic_diagram.py`](../analysis/scripts/generate_ed_logic_diagram.py).
  - Equation-rich version (full math pipeline): [`figures/ED-Math-Pipeline.png`](figures/ED-Math-Pipeline.png). Same pipeline with actual math visible — ED-05 axioms + Compositional Rule, Canon P1–P7 each with their equations, the unified PDE showing `F[ρ]` and the coupled `v` ODE, channel reductions written out (PME, Debye/RC, RLC), prediction laws (UDM `D(c)`, Cluster Merger-Lag `ℓ = D_T/v`, FRAP recovery), and six structural forks at the bottom with their formulas. Source: [`../analysis/scripts/generate_ed_math_pipeline.py`](../analysis/scripts/generate_ed_math_pipeline.py).
- **2026-04-17.** **ED-09.5 experimental strategy landed.** Sharp quantum-classical transition remains ED's single most distinctive falsifiable prediction and has no assigned test program. Three-tier strategy, draft emails to Aspelmeyer and Arndt, and theory-memo scope in [`ED-09-5-Experimental-Strategy.md`](ED-09-5-Experimental-Strategy.md). Blocking item: sharpen the "system-dependent internal-complexity threshold" into a specific numerical observable before any Tier-1 reanalysis or Tier-2 collaboration contact. FRAP side: Creative Proteomics Core has forwarded the protocol to their technician team (email 2026-04-17); decision expected ~2026-04-24 to 2026-05-01.
- **2026-04-17.** Added §6.9 — **ED-SC 2.0 canonical invariance statement.** The architectural invariance claim of ED-Arch-01 §5 and ED-Arch-02 §3 is now formalised as the **motif-conditioned median of the field-space Hessian** `∇²E` at spatial stationary points of a 2D real-space density field. Reference measurement: `median(ℛ_motif(p_ScenD)) = −1.304` at `(n* = 2.7, σ* = 0.0556)`. Cross-scale falsification window `[−1.5, −1.1]`. Full statement: [`ED-SC-2.0.md`](ED-SC-2.0.md). Supersedes the cross-scale language of ED-Arch-01 §5 and ED-Arch-02 §3.
- **2026-04-17.** Resolved the `H_param` vs `H_field` ambiguity in ED-Arch-01's published `κ∥ ≈ −1.3`. ED-Arch-01's number was extracted from the parameter-space Hessian of `f(n, σ)`; ED-Arch-02 defines the architectural Hessian as `∇²E` of the field. Under ED-SC 2.0 the invariant is field-space. See [`ED-SC-Hessian-Resolution.md`](ED-SC-Hessian-Resolution.md).
- **2026-04-17.** Corrected Scenario D parameter conventions. `n` is the **mobility exponent** in `M(p) = ((p_max − p)/p_max)^n`, NOT a Laplacian coefficient. Canonical parameters: `α = 0.03, γ = 0.5 (concave), dt = 0.05, size = 64, seed = 77, mobility-weighted`. Code: `C:/Users/allen/GitHub/Emergence Universe/ED-SIM-Code/`.
- **2026-04-17.** Three distinct "Scenario D"s coexist in the ED program (ED-SIM v1 full-atlas, ED-Phys-35 D2D, ED-Arch-01 / ED-Sim-01 architectural-invariants). Disambiguate before answering.
- **2026-04-17.** Excluded from ED-SC 2.0 comparison set: k-space band saddles (graphene, tBLG, kagome, triangular), Lagrange-point potentials, OSCER strain-rate tensors, minimal surfaces, crack-tip stress fields. Reasons in `ED-SC-2.0.md` §3.
- **2026-04-17.** Added §6.8 — ED-Arch / ED-Sim-01 architectural-invariants program (paired: ED-Arch-01 experimental == ED-Sim-01 in content; ED-Arch-02 theoretical). ED-Arch regime taxonomy (hyper-coherent / stable-coherent / marginal / non-individuating) is **distinct from** the 00.3 D_crit regime taxonomy (oscillatory / hybrid / parabolic).
- **2026-04-17.** Added §6.7 — ED-SIM-3D dimensional-consistency validation (axiom P7 across `d = 1, 2, 3`). Penalty + participation channels dimension-independent to machine precision; mobility channel dimension-dependent per `α_R = 1/(d(m-1)+2)`.
- **2026-04-17.** Added §6.6 — ED-SC Scale-Correspondence program (ED-SC-00). Pocket / channel / saddle / divergence-zone / stationary-point / threshold vocabulary. Table 1: 22 micro ↔ cosmological correspondences.
- **2026-04-17.** The ED-XX 1/r Green's-function derivation's source document is **still unlocated** — not in ED-SIM-3D, not in ED-Sim-01 / ED-Arch-01, not in ED-Arch-02. Most likely inside the ED-XX paper itself. Earlier attributions to "ED-Sim-01" in prior orientation drafts were Claude inventions and have been corrected throughout this document.

---

**Purpose.** This document captures ED framework content that lives **outside the repo** — in PhilArchive publications and in the user's local `Desktop/ED Interpretations/` and `Desktop/ED Important Papers/` folders — so that a new Claude Code session can acclimate in one read rather than rediscovering the scope from first principles. The repo is heavily focused on the PDE canon, UDM, merger-lag, and the dimensional atlas; the material below is *complementary* and sometimes *updates* what the repo says.

**The ED framework has three parallel tracks** that the repo does not make visible:

1. **The empirical physics program.** PDE canon → dimensional atlas → empirical tests in five regimes (quantum, Planck, condensed matter, galactic, cosmological). Concrete predictions, concrete falsification criteria. Lives mostly in the repo (UDM, Cluster Merger-Lag) and in 00.1 / 00.2 / 00.3 / ED-02 / ED-04 / ED-XX from the Desktop PDFs.
2. **The interpretive / ontological program.** Reframes existing phenomena in quantum mechanics, optics, information, topology, and spacetime itself as structural consequences of ED participation geometry. Produces structural *explanations*, not new measurements. Lives in ED-10 (spacetime emergence), the ED-I-XX interpretation series (photonics, quantum info, topology, weak lensing), and the PhilArchive philosophical papers (ED-06 / ED-07 / ED-08 / ED-09 / ED-09.5 / ED-13).
3. **The scale-correspondence program (ED-SC).** Identifies architectural invariants that recur across 20+ orders of magnitude. Treats micro ↔ macro correspondences as structural **identity**, not analogy. Lives in ED-SC-XX and the forthcoming scale-free atlas. First paper: ED-SC-00 (March 2026). See §6.6.

All three tracks share the same PDE canon and ontology (becoming, micro-events, participation, ED gradients). They differ in their goal: the empirical track tries to *predict* new measurements; the interpretive track tries to *unify* existing ones under one ontology; the scale-correspondence track tries to *identify architectural invariants* that persist when scale, mechanism, and substrate change.

**How to use this at session start.** Read §1 (scope & discrepancy map) first — it is the critical information. §3.1 (the two P1–P7 axiom sets — critical disambiguation) prevents confusing derivation axioms with the Canon. §5.9 (Architecture of Physical Law) is the **meta-claim** behind all three ED tracks: laws and symmetries are emergent, not fundamental. §6 (ED-XX environment sourcing revision) is the most important empirical-track update. §6.5 (Interpretation Series vocabulary) is the most important interpretive-track update. §11 (Emergence-Universe / ED-SIM sandbox) is the pre-ED proof-of-concept for the architecture-first thesis — disambiguate from the continuum `edsim/` solver. Skim §2–5 for depth. §7 is the empirical status snapshot. §8 is the full paper / code / GitHub map. §9 is the step-by-step checklist + question-type map. §12 is the non-physics Factor Skyline thread (kept for completeness, not session-start reading).

---

## 1. What the repo tells you vs. what the wider work says

### Things where the repo is authoritative and current

- The canonical PDE algebra (`theory/PDE.md`) — mobility, penalty, participation channels.
- UDM / mobility channel empirical fit (10 soft-matter materials, R² > 0.986).
- Cluster Merger-Lag evidence (7-cluster sample + Finner aggregate).
- Dimensional Atlas (5-regime mapping, D·T₀/L₀² = 0.3 invariant).
- Edsim simulation engine.
- Our work this session: RLC analogue memo, BTFR-Activity unified analysis, Finner-A1 test, scale-dependence scoping, etc.

### Things the repo does **not** currently contain (or contains in older form)

| Topic | Repo status | Wider-work status |
|---|---|---|
| **Architectural Canon — 7 irreducible principles (P1–P7)** | Absent | [00.2 Architectural Canon, March 2026] |
| **Canonical restoring penalty** | Linear: `P(ρ) = P₀(ρ−ρ*)` in `theory/PDE.md` | Smoothed / saturating: `P_SY2(ρ) = αγ · (ρ−ρ*)/√((ρ−ρ*)² + ρ₀²)` in [00.3 Unified Cosmological Equation] |
| **Channel-weight parameterization** | `D` is *dimensional diffusivity* (2.1×10²⁷ m²/s) in `theory/PDE.md` | Also `D` is *dimensionless channel weight* with `D+H=1` in [00.2, 00.3]. Two parameterizations of the same architecture — both valid at different abstraction layers. |
| **Oscillation-death threshold** | Not in repo | `D_crit = 0.5` (exact), empirically confirmed in ED-Phys-18, derived analytically in [00.3]. |
| **Universal ground state energy** | Not in repo | `E_ground = αγρ₀`, dimension/regime/IC-independent [00.3]. |
| **Universal relaxation timescale** | Not in repo | `t_rel ≈ ρ₀/(αγ)`, varies < 13% across regimes [00.3]. |
| **Cosmological compositional rule** | Not in repo | Union rule `p(A∪B) = p(A) + p(B) − α∫p^γ − β∫|∇p|² − γ∫∂h(|∇p|)` [00.1 Cosmology]. Drives inflation/structure/expansion/heat-death without metric. |
| **Spacetime-as-emergent dictionary** | Not in repo | Full coarse-graining map: Space = participation adjacency, Time = commitment order, Distance = participation resistance, Curvature = ED gradient structure, Horizons = decoupling surfaces, Information = constraint structure [ED-10]. |
| **Environment-sourcing revision** | Not in repo — but this is the single most important update | [ED-XX, **April 2026**]. The galaxy-sourced temporal-tension hypothesis (ED-02, ED-04) is **overturned** by the 3D Green's-function `1/r` dilution argument. **Source document is STILL UNLOCATED** as of v1.3 — it is NOT ED-SIM-3D (§6.7, dimensional consistency), NOT ED-Sim-01 / ED-Arch-01 (§6.8, architectural invariants), and NOT ED-Arch-02 (§6.8, architectural theory). Most likely lives inside the ED-XX paper itself on Desktop. Temporal tension must be sourced by groups/filaments/cosmic web (σ ≥ 1–3 Mpc). |
| **Architectural-invariants program (ED-Arch / ED-Sim-01)** | Not in repo | [ED-Arch-01 / ED-Sim-01 + ED-Arch-02, **March 2026**]. Paired theory+experiment thread establishing the formal Hessian geometry of saddles, channels, boundaries, and horizons, and demonstrating architectural invariance via a 4×4 Scenario-D parameter sweep. First empirical bridge between ED dynamics and the ED-SC scale-correspondence claim. See §6.8. |
| **Dwarf SPARC D_outer test** | Not in repo | [ED-04.5 / Dwarf paper]. N=46 SPARC dwarfs, ⟨D_outer⟩_Active = 6.01, ⟨D_outer⟩_Quiet = 3.94, 53% separation. Still stands under ED-XX as a proxy for environmental activity. |
| **Weak-lensing interpretation (Mistele+2024)** | Not in repo | [ED-I-27, March 2026]. Interpretation of megaparsec-flat circular velocities as temporal-tension ED-channel. Uses galaxy-sourced framing that ED-XX later revises. |

### Discrepancies you should know about at session start

1. **Penalty form.** The repo's `theory/PDE.md` uses the linear `P₀(ρ−ρ*)` form. The current canonical form per [00.3] is `P_SY2`. These agree near equilibrium but diverge at the mobility ceiling, and the horizon/heat-death arguments in [00.1] depend on SY2's saturation. If a future session touches `theory/PDE.md`, flag this before editing.
2. **What "D" means.** In repo code and repo docs, `D` is dimensional diffusivity (m²/s). In [00.2 Canon] and [00.3 Unified PDE], `D` is the dimensionless channel weight (with `D+H=1`). Context-sensitive.
3. **Galaxy-sourced vs. environment-sourced.** Any repo text or paper that asserts "galaxies generate their own temporal-tension halos" reflects the pre–April-2026 view. [ED-XX] supersedes this — galaxies set the *amplitude* via baryonic identity, the *spatial extent* comes from the cosmic web.

---

## 2. The trajectory (dated papers, in order)

The ED main series is numbered **ED-01 through ED-13** (with ED-04.5 and ED-09.5 as half-steps). The main series is complemented by the **00-series** (foundational cosmology math), the **ED-I series** (interpretive applications to quantum / optical / topological phenomena), the **ED-SC series** (scale-correspondence), the **ED-Arch / ED-Sim series** (architectural-invariants + Emergence-Universe sandbox; see §6.8 and §11), and the **ED-XX** revision. The Cluster Merger-Lag, Universal Degenerate-Mobility, and Open Note papers are empirical / methodological publications. The two **Factor Skyline** papers are a **separate non-physics thread** on multiplicative number theory (see §12 — kept in the inventory because Allen authors them, not because they are ED physics).

| Date | ID | Paper | One-line contribution |
|---|---|---|---|
| **Late 2025 / early 2026** | **ED-01** | **Event Density and the Architecture of the Universe** | **The true founding paper.** "The universe is made of activity before it is made of things." Establishes the four primitives (events / becoming / event density / finite configurations) and the compositional rule before any specific application. Pre-dates ED-02. Not on Desktop under this name; accessible via PhilArchive. |
| **Dec 2025** | ED-02 | Temporal Density and Galactic Curvature | First physical application — speculative DM alternative, nine qualitative predictions. No math. |
| **Feb 2026** | ED-03 | Extensions of Event Density: Structural Consequences Across Physics | First cross-domain synthesis: gravitation, quantum, information, cosmology from a single primitive. Qualitative. |
| **Feb 2026** | ED-04 | Field-Level Account of Dark Matter | Formalization of temporal tension. Distinguishes from CDM/MOND/emergent gravity. Folds in ED-04.5. |
| **Feb 2026** | ED-04.5 | Temporal Tension in Dwarf Galaxies | First empirical test. SPARC n=46, 53% Active-vs-Quiet D_outer. |
| **Feb 2026** | ED-05 | Event Density: A Mathematical Formalization | **Pre-PDE axiomatic layer.** Four measure-theoretic axioms on a bare event domain. |
| **Feb 2026** | ED-06 | Horizons as Event Density Decoupling Surfaces | All horizons (BH / Rindler / cosmological) as ED field discontinuities where participation can't reconcile. |
| **Feb 2026** | ED-07 | Event Density and Relativistic Phenomena | `c` = max rate of causal updates through ED network, not a geometric postulate. Lorentz from participation architecture. |
| **Feb 2026** | ED-08 | Cosmological Structure: Temporal Tension and Expansion | Expansion = cumulative temporal tension across ED gradients. Redshift, acceleration, structure, horizons. |
| **Feb 2026** | ED-09 | Quantum Behavior: Participation, Discreteness, Relational Becoming | Quantum phenomena emerge from micro-event-level participation: superposition = coexisting channels, entanglement = shared bandwidth, measurement = structural commitment. |
| **Feb 2026** | ED-09.5 | The Quantum-Classical Boundary | **Sharp ED transition** distinct from environmental decoherence — a candidate *novel testable prediction*. |
| **Feb 2026** | ED-10 | Emergence of Spacetime, Geometry, Information | Spacetime, geometry, information, arrow-of-time as emergent from ED primitives. Most ambitious paper. |
| **Feb 2026** | 00.1 | Cosmology from the Compositional Rule | Inflation / structure / expansion / heat-death from one union rule. No metric. |
| **Feb 2026** | ED-I-12 | Photonics | Five "photonics moves" (Yablonovitch / Pendry / Capasso as channel manipulations). |
| **Feb 2026** | ED-I-13 | Quantum Information | Five QI moves (Deutsch / BB84 / teleportation / Shor as channel-geometry operations). |
| **Feb 2026** | ED-I-14 | Topological Effects | Four AB/Berry/AC variants as global invariants of ED channel geometry. |
| **March 2026** | ED-I-27 | Weak Lensing | Mistele+2024 reinterpretation as ED-channel (galaxy-sourced framing — superseded by ED-XX). |
| **March 2026** | 00.2 | Architectural Canon | 7 irreducible principles. ED as a class, not a specific PDE. |
| **March 2026** | 00.3 | Unified Cosmological Equation | `ρ̇ = D·F[ρ] + H·v`, `D+H=1`, `D_crit = 0.5`, SY2 penalty. |
| **March 2026** | ED-13 | Event Density as a Physical Ontology | **Master empirical synthesis.** Four primitives + seven axioms → unique dynamical equation. Two sharp predictions: activity-dependent WL velocities + merger-lag lensing. |
| **March 2026** | **ED-Phys** | **Event Density and the Architecture of Physical Law: Symmetry, Constraint, and Emergent Regularity** | **Physics's laws, symmetries, and conservation quantities are not fundamental features of the universe — they are emergent consequences of ED architecture and constraint.** Translates physical "law" into the framework of ED gradients, participation structure, and compositional rules. See §5.9. Pairs naturally with the Emergence-Universe sandbox (§11) whose 14-law closure theorem empirically demonstrates the same claim in a discrete sandbox. |
| **(undated)** | **PhilArchive** | **Event Density: Open Note for Experiments** | **Falsifiable-test catalogue across all five regimes** — a single outward-facing note listing every clean test that could confirm or refute ED. Useful as the outreach counterpart to this orientation; intended to invite experimentalists. Overlaps with `outreach/ED_Falsifiable_Prediction.md` in the repo. |
| **March 2026** | PhilArchive | Universal Degenerate-Mobility Scaling in Crowded Soft Matter | **UDM paper** (10-material soft-matter empirical fit, `R² > 0.986`). The authoritative publication underpinning `papers/Universal_Mobility_Law/`. |
| **(undated)** | PhilArchive | Temporal Tension and Merger Lag in Galaxy Clusters | **Cluster Merger-Lag paper** (7 clusters + Finner aggregate, `ℓ = D_T / v_current`). The authoritative publication underpinning `papers/Cluster_Merger_Lag_Evidence/`. |
| **March 2026** | ED-SC-00 | Scale-Correspondence in Event Density | Scale-correspondence as structural identity, not analogy. New vocabulary (pockets/channels/saddles/divergence zones/stationary points/thresholds). First overlay: Local Group Mass Sheet ↔ Golden Casimir Cavity. Table 1: 22 micro↔cosmological correspondences. See §6.6. |
| **March 2026** | ED-SIM-3D | Canonical PDE 2D/3D Extension and Invariant Mini-Atlas | Dimensional-consistency validation. Extends the ED solver to d=1,2,3; runs 5 invariant tests (Barenblatt PME, RC decay, telegraph oscillation, horizon formation, participation coupling). Penalty + participation channels are dimension-independent to machine precision; mobility channel is dimension-dependent per `α_R = 1/(d(m-1)+2)`. Validates axiom P7. Runs on ED-SIM-02 software package. See §6.7. |
| **March 2026** | ED-Sim-01 / ED-Arch-01 | Architectural Invariants of Becoming: Experimental Probes | **First empirical validation of ED architectural invariants (v1.3).** Same paper filed under two series labels (Simulations + Architecture). 4×4 Scenario-D sweep on 512×512 lattice across mobility exponent `n ∈ {0.5, 1, 2, 4}` and Langevin noise `σ ∈ {0.01, 0.02, 0.05, 0.10}`. Finds a saddle-shaped phase-exit surface with peak at `(n=2.7, σ=0.0556)`, step 457. Curvature ratio κ_∥/κ_⊥ ≈ −1.3 ± 0.2 matches the Local Group mass sheet and Casimir cavity. Four regimes empirically identified. **Does NOT contain the 1/r dilution argument.** See §6.8. |
| **March 2026** | ED-Arch-02 | Architectural Foundations of Event Density | Theoretical counterpart to ED-Arch-01. Defines saddle / channel / boundary / horizon via Hessian geometry (gradient sign-flip, det(H)=0 curves, λ_⊥ > 0 for boundaries, λ_⊥ < 0 for horizons). Derives universality (IC-independence, parameter-deformation stability, noise-threshold robustness, mobility-law invariance, curvature-driven necessity). See §6.8. |
| **April 2026** | ED-XX | Environment Sourcing of Temporal Tension | Major revision. Galaxy-sourced hypothesis overturned by a 3D Green's-function `1/r` dilution argument. **Source document NOT located** — it is NOT ED-SIM-3D, NOT ED-Sim-01 / ED-Arch-01, NOT ED-Arch-02. Likely lives inside the ED-XX paper itself. |
| (in repo) | Cluster Merger-Lag | Cluster Merger-Lag Evidence | 7-cluster sample + Finner aggregate test `ℓ = D_T/v_current`. Currently the primary-cited empirical penalty-channel test. |

**Separate thread — not part of the ED physics program:** Regulated Multiplicity: An Architectural Account of Consciousness (Dec 2025) and Regulated Multiplicity: An AI Systems Architecture (Jan 2026). Confirmed independently as philosophy-of-mind / AI systems work with no physics content.

---

## 3. The Architectural Canon (7 principles) — P1 through P7

From [00.2 March 2026]. Any PDE satisfying these is "architecturally ED," regardless of functional form.

| # | Principle | Statement |
|---|---|---|
| **P1** | Operator Structure | `F[ρ] = M(ρ)∇²ρ + M'(ρ)\|∇ρ\|² − P(ρ)` — curvature-dependent diffusion + nonlinear gradient + restoring force |
| **P2** | Channel Complementarity | `ρ̇ = D·F[ρ] + H·v`, `D + H = 1`, `D,H ∈ [0,1]` — direct + mediated channels, convex weighting |
| **P3** | Penalty Equilibrium | `P(ρ*) = 0` with `P' > 0` — unique globally-attracting equilibrium |
| **P4** | Mobility Capacity Bound | `M(ρ_max) = 0` with `M(ρ) > 0` for `ρ < ρ_max` — horizon at the capacity bound |
| **P5** | Participation Feedback Loop | `v̇ = (1/τ)(F[ρ] − ζv)` — memory channel with exponential decay |
| **P6** | Damping Discriminant | **Linearised form (resolved 2026-04-22, [`theory/D_crit_Resolution_Memo.md`](../theory/D_crit_Resolution_Memo.md)):** underdamped iff `(D − ζ)² < 4(1 − D)` at reference mode `ε_k·τ = 1`; critical threshold `D_crit(ζ) = √(2−ζ)·(2 − √(2−ζ))`; at canon-default `ζ = 1/4`, **`D_crit ≈ 0.896`** (NOT 0.5). The earlier additive heuristic `Δ = D + 2ζ, critical at Δ = 1 → D_crit = 0.5` is retired as quantitative claim (error ~80%); retained only as order-of-magnitude mnemonic. |
| **P7** | Nonlinear Triad Coupling | `M'(ρ)·\|∇ρ\|²` generates k=3 from k=1 with invariant triad ratio. **Calibrated 2026-04-22** — scale-free invariant `K = A₃/A₁³ ≈ 0.0148 ± 0.0005`, companion `K₂ = A₂/A₁² ≈ 0.279`, cubic scaling slope `α₃ = 3.0 ± 0.05`, exact phase lock `φ₃ − 3φ₁ = π` (SD ~ 10⁻⁶ rad), symmetry ordering `A₂ > A₃` in the clean regime (~200× at A₁=0.1 per simulation). The amplitude-dependent ratio `A₃/A₁` is NOT the invariant; the previously-cited ED-Phys-16 "3–6%" band reproduces only in the saturation regime at `A₁ ≳ 0.15·ρ_max`. Operational test: [`experiements/Triad-Coupling-C7_InProcess/protocol.md`](../experiements/Triad-Coupling-C7_InProcess/protocol.md). |

Counterfactual analysis: removing any principle breaks a specific architectural layer (motifs / laws / geometry / invariants). The Canon is minimal and irreducible.

**Why this matters for me:** when I read repo docs that refer to "the ED PDE," I now know this is shorthand for the equivalence class defined by P1–P7. The specific mobility and penalty forms in `theory/PDE.md` are one instance. The RLC-analogue memo I wrote derives P6 (damping discriminant) in dimensional units without knowing it was P6 — worth cross-linking if I revisit it. **P7 addendum (2026-04-22):** the Triad-Coupling-C7 simulation companion at [`analysis/scripts/telegraph_pme/triad_calibration/memo.md`](../analysis/scripts/telegraph_pme/triad_calibration/memo.md) reduced P7 from a qualitative "k=3-from-k=1" claim to a sharp four-observable invariant (`K, K₂, α₃, Δφ`). The historical `A₃/A₁ ∈ [0.02, 0.08]` band inherited from ED-Phys-16 is retired as a primary criterion; `K = A₃/A₁³` is the replacement scale-free invariant. The "A₂ < A₃ by odd symmetry" claim in earlier drafts of the C7 protocol was **inverted** — the quadratic `M′(ρ)|∇ρ|²` sources the second harmonic directly via the DC + 2k structure of `|∇ρ|²`, so `A₂ > A₃` in the clean regime.

### 3.1 The two P1–P7 axiom sets — critical disambiguation

**There are TWO distinct "P1–P7" axiom sets in the ED corpus, used at different layers of the theory.** Prior Claude sessions have conflated them. When reading any ED document that references "P1" through "P7," first determine which set is being invoked:

| Set | Source | Purpose | Symbol for what's constrained |
|:---|:---|:---|:---|
| **Derivation axioms** | `ED_Foundational_Paper(.md / v2.md)` §2.4, `ED-Math-01_Uniqueness_Well-Posedness_and_Architectural_Laws.md` Theorem 2.1, `WHAT_IS_ED.md` | Axioms from which the canonical PDE is **derived**. These determine *what the PDE must look like*. Theorem 2.1 proves the canonical ED PDE is the unique second-order scalar PDE satisfying all seven. | P1 = Locality · P2 = Isotropy · P3 = Gradient-driven flow · P4 = Dissipative structure · P5 = Single scalar field · P6 = Minimal coupling · P7 = Dimensional consistency |
| **Architectural Canon (00.2)** | `00.2 Architectural Canon of the Unified ED Cosmology PDE`, `Desktop/ED Important Papers/The Architectural Canon...pdf` | Principles defining ED as a **class** of PDEs. These specify *what structural features every architecturally-ED PDE must have*. Any PDE satisfying these is "architecturally ED," regardless of specific functional forms. | P1 = Operator Structure · P2 = Channel Complementarity (D+H=1) · P3 = Penalty Equilibrium · P4 = Mobility Capacity Bound · P5 = Participation Feedback Loop · P6 = Damping Discriminant (D_crit = 0.5) · P7 = Nonlinear Triad Coupling |

**They are complementary, not contradictory.** The derivation axioms operate at the level of PDE *form* (what mathematical objects are allowed to appear); the Canon principles operate at the level of PDE *architecture* (what structural relations must hold among those objects). A PDE satisfying only the derivation axioms might not be "architecturally ED" unless it also satisfies the Canon; a PDE satisfying the Canon principles has, by construction, the canonical form the derivation axioms produce.

**The ED-13 "seven axioms" claim** ("four primitives and seven axioms uniquely determine the equation") most naturally refers to the **derivation-axiom set** (ED-Math-01 Theorem 2.1), composed with the four ED-05 pre-PDE axioms (non-negativity, null baseline, monotonicity, subadditivity). The 00.2 Canon is a *structural characterization* of what the derivation yields, not an independent set of axioms layered on top.

**When an ED paper says "P4":**
- If the paper is the Foundational Paper, ED-Math-01, or any uniqueness-theorem context → P4 = Dissipative structure.
- If the paper is 00.2, 00.3, any "Canon" context, or any paper citing `D_crit = 0.5` → P4 = Mobility Capacity Bound.
- **If in doubt, check which set of seven labels appears nearby.** The two sets have no overlapping labels.

The three-track structure documented at the top of this doc (Empirical / Interpretive / Scale-correspondence) generally uses whichever axiom set is most convenient for the current abstraction layer. Both sets are correct; neither is deprecated.

### 3.2 Axioms stack: four ED-05 → seven derivation → seven Canon

For session-start reference, the full axiom stack from pre-PDE to architectural:

1. **Pre-PDE layer (ED-05, Feb 2026, 4 axioms on a bare event domain):** non-negativity, null baseline, monotonicity, subadditivity. No time, geometry, or probability presupposed.
2. **Derivation layer (Foundational Paper / ED-Math-01, 7 axioms):** locality, isotropy, gradient-driven flow, dissipative structure, single scalar field, minimal coupling, dimensional consistency. ED-Math-01 Theorem 2.1: these **uniquely determine** the canonical PDE up to the choice of constitutive functions `M(ρ)` and `P(ρ)`.
3. **Architectural Canon layer (00.2, 7 principles):** operator structure, channel complementarity, penalty equilibrium, mobility capacity bound, participation feedback loop, damping discriminant, nonlinear triad coupling. Specifies the structural *architecture* the derived PDE must exhibit.

A PDE that passes all 4+7+7 is guaranteed to reproduce the ED phenomenology: unique attractor, Lyapunov dissipation, three-stage convergence, oscillation-death at D_crit = 0.5, and the 22-correspondence scale-invariance of ED-SC Table 1.

---

## 4. The Unified Cosmological Equation (00.3 canon)

The canonical PDE in its current cleanest form:

$$\partial_t \rho = D \cdot F[\rho] + H \cdot v, \qquad D + H = 1$$
$$\partial_t v = \frac{1}{\tau}(F[\rho] - \zeta v)$$
$$F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P_{SY2}(\rho)$$
$$P_{SY2}(\rho) = \alpha\gamma \cdot \frac{\rho - \rho^*}{\sqrt{(\rho-\rho^*)^2 + \rho_0^2}}$$

### Three regimes (parameter-determined)

| Regime | Condition (heuristic boundaries, 00.3) | Corrected boundary (2026-04-22) | Behavior |
|---|---|---|---|
| Oscillatory | `D < 0.1` | `D ≪ D_crit(ζ)` — well below threshold | Underdamped, reversible, standing participation waves, 8–19 transient oscillations |
| Transitional / Hybrid | `0.1 ≤ D ≤ 0.4` | `D → D_crit(ζ)` from below | Mixed behavior, smooth interpolation |
| Parabolic | `D ≥ 0.5` | `D ≥ D_crit(ζ) ≈ 0.896` at canon-default `ζ = 1/4` | Overdamped, irreversible, structure-forming, peak merging, basin formation |

**Note (2026-04-22):** The original heuristic boundaries (`< 0.1`, `0.1–0.4`, `≥ 0.5`) were calibrated against the retired `D_crit = 0.5` heuristic. Full linearised analysis places the parabolic/hybrid boundary at `D_crit(ζ) ≈ 0.9` (canon-default). The qualitative three-regime structure survives; the numerical boundaries shift upward by ~0.4 in D. Downstream papers (ED-SIM-3D §6.7, Extended Atlas §5–§7) that used the 0.5 threshold as a regime marker should be re-examined. See [`theory/D_crit_Resolution_Memo.md`](../theory/D_crit_Resolution_Memo.md) §10.

### Universal invariants

- **Equilibrium density** `ρ*` — unique zero of P_SY2, globally attracting across all D ∈ [0,1].
- **Ground state energy** `E_ground = αγρ₀` — independent of dimension, mixing ratio, IC.
- **Relaxation timescale** `t_rel ≈ ρ₀/(αγ)` — varies only ~13% across the entire hybrid parameter space.
- **Horizon behavior** — near `ρ_max`, mobility collapses (diffusion vanishes), but participation v and its inertia survive. This produces oscillating horizons in the oscillatory regime (lifetime extended by ~60%) and collapsing horizons in the parabolic regime.

### Nonlinear structure (weakly coupled)

- Triad resonance `k_3 = k_1 ± k_2`, coupling ~0.03 (measured in ED-Phys-16).
- Harmonic generation at 3–6% of fundamental.
- No mode locking, no chaos, no bifurcations.
- ED is "a weakly nonlinear, weakly coupled, nearly non-dispersive oscillator lattice with reversible participation dynamics."

---

## 5. The ontology (ED-10 emergence map)

Becoming is primitive. Micro-events are atomic units. Participation is the relational substrate. Everything geometric / informational / temporal is emergent.

### Coarse-graining dictionary

| Classical concept | ED substrate |
|---|---|
| Space | stable participation adjacency |
| Time | commitment order (irreversible) |
| Distance | participation resistance |
| Curvature | ED gradient structure |
| Locality | thick participation coherence |
| Mass / energy | patterns of committed micro-events |
| Horizons | decoupling surfaces / participation bottlenecks |
| Einstein's equations | **not** emergent from ED. Only a kinematic acoustic metric `g^eff_μν = diag(−M(ρ_0), 1, 1, 1)` arises (ii-grade, slaved to `ρ_0`, no field equation). Schwarzschild unreachable under any coordinate transformation. See [`ED_Effective_Acoustic_Metric.md`](../theory/ED_Effective_Acoustic_Metric.md) + [`ED_Schwarzschild_Obstruction.md`](../theory/ED_Schwarzschild_Obstruction.md). |
| Schrödinger evolution | **not** derived from ED. In the reversible slice (`D = 0, ζ = 0`), linearised ED is a free massive Klein-Gordon field whose canonical quantisation is consistent with Schrödinger-picture free-scalar QFT — a consistency result, not a derivation of QM. See [`ED_Reversible_Sector_QFT.md`](../theory/ED_Reversible_Sector_QFT.md). |
| Wavefunction collapse | irreversible selection of a participation channel |
| Born rule | participation weights |
| Entanglement | shared uncommitted participation structure |
| Information | constraint on viable commitment histories |
| Holography | constraint imposed by decoupling surfaces |
| Entropy | distribution of viable commitment histories |
| Arrow of time | asymmetry of commitment (ontological, not statistical) |

### Continuum

Quantum → Relational → Classical → Geometric. One substrate (participation), regime-dependent expressions.

**Note on scope.** ED-10 is philosophical/architectural, not empirically discriminating. The empirical program lives in the mobility / penalty / participation tests. ED-10 is what makes the framework a *unifying ontology* rather than just a DM alternative, but claims like "the measurement problem dissolves" are interpretive, not tested.

---

## 5.5 The ED main series — additional papers (ED-03, ED-05 through ED-09.5, ED-13)

These are PhilArchive-only papers that fill in the conceptual spine of the framework *between* the founding paper (ED-02) and the mature canon (00.2 / 00.3 / ED-XX). Each is summarized here at the level a future session needs to navigate without re-reading.

### ED-05 — Mathematical Formalization (Feb 2026) — the pre-PDE axiomatic layer

*Beneath* the PDE canon: a measure-theoretic / categorical structure defining "ED" as a mathematical object before any dynamics are attached.

Four governing axioms on a bare event domain, assigning non-negative density values to finite configurations of events:

1. **Non-negativity** — ED is always ≥ 0.
2. **Null baseline** — the empty configuration has ED = 0.
3. **Monotonicity** — adding events does not decrease ED.
4. **Subadditivity** — `ED(A ∪ B) ≤ ED(A) + ED(B)`, capturing the non-linear relational character of becoming.

No time, geometry, causality, or probability is presupposed. **Morphisms between ED systems** are defined to identify when two systems share underlying structure (categorical perspective).

**Relationship to the 00.2 Architectural Canon:** the Canon's P1–P7 sit at the PDE layer; ED-05's four axioms sit at the pre-PDE layer. ED-13 claims "four primitives and seven axioms" uniquely determine the dynamical equation — this is the composition of ED-05's four axioms (or the four ontological primitives: micro-events, ED gradients, participation, commitment) with the seven Canon principles.

### ED-06 — Horizons as Decoupling Surfaces (Feb 2026)

All horizons are manifestations of the same structural phenomenon: **discontinuities in the ED field where gradients become so steep that participation can no longer be reconciled across a boundary**. The flow of becoming becomes one-way.

Unifies:
- Black hole horizons
- Rindler horizons (accelerated observers)
- Cosmological horizons

In each case, "falling behind the horizon" is *participation decoupling*, not geometric crossing. No information paradox: the network splits into disconnected regions; nothing "falls into" anything. Thermal behavior (Hawking / Unruh temperature) arises from gradient steepness at the boundary, not from field-theoretic pair creation.

**Consistent with** ED-10 §4.4 and 00.1 §8.3, which use the same decoupling-surface framing.

### ED-07 — Relativistic Phenomena (Feb 2026)

Relativistic phenomena emerge from the architecture of becoming, not from a fundamental spacetime geometry:

| Relativistic phenomenon | ED mechanism |
|---|---|
| Invariance of `c` | `c` = maximum rate at which causal updates propagate through the ED network |
| Time dilation | Differences in local rate of becoming |
| Length contraction | Participation-adjacency compression along a motion direction |
| Redshift | Cumulative participation stretching across ED gradients |
| Inertial motion | Gradient-minimizing participation pathway |
| Curvature | Macroscopic imprint of uneven ED flow |
| Lorentz symmetry | Structural consequence of participation architecture |
| Geodesics | Stable participation pathways |

Does *not* modify GR's field equations; reframes what sources them. `c` being an invariant is derived here, not assumed — which is a stronger claim than GR makes.

### ED-08 — Cosmological Structure: Temporal Tension and Expansion (Feb 2026)

Complements 00.1 with a more observationally-oriented account. Cosmology in ED is the long-scale evolution of temporal tension across ED gradients:

- **Cosmic expansion** = cumulative temporal tension accumulating across ED gradients (not metric stretching).
- **Redshift** = cumulative participation stretching (gradient-integrated effect, not Doppler/metric).
- **Acceleration** = steepening of ED gradients over time.
- **Structure formation** = amplification of ED variations.
- **Horizons** = global participation limits (not geometric boundaries).
- **Early universe** = high-ED, fully-coupled state (NOT singularity).
- **Inflation-like behavior** = transition from global coherence to event-structure complexity outpacing event-production capacity.

Maps ED gradients onto FRW-like behavior *without* treating the metric as fundamental.

### ED-09 + ED-09.5 — Quantum behavior and the quantum-classical boundary (Feb 2026)

**ED-09** is the foundational quantum-emergence paper. Quantum behavior arises in low-ED regimes where systems lack the becoming needed to individuate. The vocabulary the ED-I-13 Quantum Information paper uses for specific algorithms originates here:

| Quantum concept | ED mechanism |
|---|---|
| Superposition | Coexisting participation channels |
| Interference | Relational timing between channels |
| Entanglement | Shared participation bandwidth |
| Decoherence | Participation thinning |
| Measurement | Structural commitment to a single stable channel |
| Wavefunction | Coarse-grained summary of participation structure (not a physical object) |

**ED-09.5 is the more interesting paper** because it makes a potentially testable novel prediction. ED posits **two independent phenomena** at the quantum-classical boundary:

1. **Environmental decoherence** — the standard smooth erosion of coherence by coupling to an environment. ED accepts this.
2. **The ED transition** — a *sharp structural boundary* determined by internal event density. When a system's internal complexity outpaces its event-production capacity, participation channels collapse to a single stable configuration. **This is not dynamical collapse, not branching, not environmental.** It is a structural limit of becoming.

Standard quantum mechanics predicts only (1) and describes the quantum-classical transition as smooth. ED-09.5 predicts an additional **sharp** transition at a system-dependent internal-complexity threshold.

> **This is a candidate falsifiable prediction that the repo does not currently mention.** If experimentally confirmed, it would be evidence for ED-specific structure beyond standard QM. If the quantum-classical transition is verified to be smooth under all preparations where (1) is controlled for, ED-09.5 is falsified. Worth flagging to the user next time quantum-foundations or macroscopic quantum behavior comes up.

### ED-13 — Event Density as a Physical Ontology (March 2026) — the master synthesis

The most integrated empirical statement in the PhilArchive set, and the one most directly usable as a reference for the physics program.

**Architectural claim:** From four primitives and seven axioms, the framework yields a unique scalar dynamical equation whose three channels correspond exactly to familiar physical laws:

- Nonlinear diffusion (mobility channel / porous-medium equation)
- Exponential relaxation (penalty channel / Debye-like)
- Telegraph-type oscillation (participation channel / RLC-like)

**Empirical results reported:**

- **Condensed matter:** Diffusivity decline near saturation fits three chemically distinct systems with a common exponent near 2. Porous-medium front-propagation law confirmed in simulation. (Anchors the UDM result.)
- **Galactic:** ED equation coupled to Poisson gravity produces naturally cored halo profiles matching observed dwarf-galaxy cores. Flat weak-lensing velocities to 1 Mpc via the participation mode interpretation. BTFR reproduced with the observed `1/4` exponent.

**Two sharp discriminating predictions that distinguish ED from CDM and MOND:**

1. **Activity-dependent weak-lensing velocities** — galaxies with more collective activity should show higher `V_∞` at fixed baryonic mass. (This is the galaxy-level version of the prediction ED-XX later reframes as environment-level.)
2. **Diffusive lensing lag in merging clusters** — the ED analogue of the merger-lag wake signature. (This is the prediction Cluster Merger-Lag operationalized as `ℓ = D_T / v_current`.)

ED-13 is in a sense the PhilArchive counterpart to the repo's Cluster Merger-Lag + UDM + Dimensional Atlas trio — it covers the same empirical ground in condensed single-paper form. When a future session needs a one-reference citation for the empirical physics program, ED-13 is the paper.

### ED-03 — Extensions of Event Density: Structural Consequences Across Physics (Feb 2026)

The cross-domain overview that preceded the deeper treatments in ED-10 (spacetime), ED-09 (quantum), ED-06 (horizons), ED-08 (cosmology). Four domains treated:

1. **Gravitation** — curvature = macroscopic geometry of ED flow.
2. **Quantum mechanics** — quantum behavior in low-ED regimes.
3. **Information / entropy** — complementary ED expressions; holography from ED gradient concentration at boundaries.
4. **Cosmology** — long-scale ED evolution.

Qualitative, less developed than the domain-specific papers that followed. Useful as the introductory overview; skipable if ED-10 + ED-09 + ED-06 + ED-08 are already in hand.

### 5.6 ED-Math-01 — Uniqueness theorem and the nine architectural laws L1–L9

**Source:** `Desktop/ED Important Papers/ED-Math-01_Uniqueness_Well-Posedness_and_Architectural_Laws.md`. Read 2026-04-21. This is the **formal mathematical layer** of ED — the document that turns the PDE canon into a theorem.

**Theorem 2.1 (Uniqueness).** The canonical ED PDE is the unique second-order scalar PDE satisfying the seven *derivation* axioms (§3.1). Proof by constructive elimination: P1+P2 reduce the operator to functions of `(ρ, |∇ρ|², ∇²ρ)`; P3 determines the principal part; P4 constrains the reaction term; P5 excludes non-scalar fields; P6 determines the coupling form; P7 ensures dimension-independence. Combined with ED-05's pre-PDE axioms and the Canon's structural principles, this provides a closed derivation of the ED PDE from first principles — **no tuning, no fit, no free choice of form**.

**Well-posedness results** (proved per-channel in ED-Math-01):

| Channel | Well-posedness theorem | Condition |
|:---|:---|:---|
| Mobility (PME reduction) | Existence and uniqueness of weak solutions | Follows from Vázquez (2007) once the `M(ρ) → 0` degeneracy is confined to the capacity bound |
| Penalty (RC reduction) | Global-in-time regularity | `P'(ρ*) > 0` (monotone attractor) |
| Participation (coupled ODE-PDE) | Existence via linear superposition onto the mobility+penalty solution | Requires finite `τ`, `ζ > 0` |

**The nine architectural laws L1–L9** (ED-Math-01, also summarized in the Desktop `ED Laws All so far.PNG`). These are *consequences* of the Canon — things every architecturally-ED PDE must exhibit:

| # | Law | Statement |
|:---|:---|:---|
| **L1** | Unique attractor | The penalty channel defines a unique, globally attracting equilibrium `ρ*` |
| **L2** | Energy monotonicity | Multiple simultaneous Lyapunov functionals decay monotonically (gradient, entropy, energy, penalty, participation) |
| **L3** | Spectral concentration | Solutions concentrate onto a low-dimensional invariant spectrum (3-stage convergence theorem) |
| **L4** | Factorial complexity dilution | Mode coupling dilutes as `1/k!`, so high-k structure damps rapidly |
| **L5** | Gradient–dissipation dominance | At late times, dissipation rate tracks `‖∇ρ‖²` — the gradient is the ledger |
| **L6** | Topological conservation | Horizon topology is preserved under smooth ED evolution (no spontaneous horizon birth in the parabolic regime) |
| **L7** | Horizon formation | For `ρ > ρ_crit`, mobility degenerates and a free boundary (transient horizon) forms |
| **L8** | Morphological hierarchy | Hessian eigenvalue morphology follows blobs → filaments → sheets → uniform (confirmed in 2D/3D by ED-SIM-3D §6.7) |
| **L9** | Sheet–filament oscillation | In the oscillatory regime (D < 0.1), sheet and filament morphologies interconvert via telegraph oscillations |

These hold across dimensions d = 1–4 (L7–L9 are partially dimension-dependent per ED-SIM-3D). **Relationship to the Canon:** the L-laws are *theorems* about systems that satisfy the Canon's P-principles, not additional axioms. L1 ↔ P3; L7 ↔ P4; L9 ↔ P5+P6; etc. When a session needs a single reference for the formal mathematical status of the ED PDE, ED-Math-01 is it.

### 5.7 The six structural analogues (Foundational Paper v2)

**Source:** `Desktop/ED Important Papers/ED_Foundational_Paper_v2.md`. Read 2026-04-21. This is the **empirical-structural layer** of the Foundational Paper — six minimal experiments that isolate or combine the three ED channels and check whether the resulting dynamics match a known physical law. This is what makes ED *falsifiable* at the structural level.

| # | Channels exercised | Physical law | Key result |
|:---|:---|:---|:---|
| **1** | Penalty only | RC / Debye exponential decay | `λ = DP₀` matched to **0.00%** (machine precision) including RLC frequencies `ω` at H = 0.3, 1.0, 5.0 |
| **2** | Mobility only | Barenblatt PME `∂_t δ = D_pme ∇²(δ^m)` with `m = β+1` | `α_R = 1/(d(m-1)+2)` matched to **1.1%** at β=1; pre-asymptotic at β=2, 3; compact support confirmed |
| **3** | Mobility + Penalty | Stefan free-boundary / transient horizons | Sharp amplitude threshold `A_c = 0.400` predicted, measured `0.410` (**2.5%**); horizon lifetime monotonic in A |
| **4** | All three | Oscillatory horizon modulation | **Scientifically informative negative result.** Horizons are too short-lived (`τ_H ~ 0.3–1.5`) relative to the telegraph period (`T_osc ~ 2–6`) for boundary oscillation. Structural consequence of L1 (unique attractor) — not a numerical artifact |
| **5** | Mobility + Participation | Telegraph-modulated PME | `ω ∝ H^{0.52}` (predicted `H^{0.50}`, within 4%); v–δ frequency match to **0.03%** at H = 50. Also surfaced the structural identity `bar{F} = 0` when `P₀ = 0` under Neumann BC — participation needs penalty to activate |
| **6** | All three (two-peak) | Emergent pair interaction | **Discovered** nonlinear-mobility repulsion (not anticipated analytically): tail overlap → lower local mobility → outer-edge-faster spreading → centres drift apart. Telegraph coupling at H > 0 modulates this between attraction and repulsion (correlation ~ +0.5 with v(t)) |

**What the six analogues establish:** Each channel corresponds *exactly* (not approximately) to a known physical law at the level of governing equations. The penalty *is* RC discharge; the mobility *is* porous-medium diffusion; the participation *is* a telegraph oscillator. Channel combinations produce higher-level structure (horizons, modulated spreading, effective pair interactions) that is richer than the sum of the individual channels. The one negative result (Analogue 4) is a structural consequence of L1 and is informative, not a failure.

**3D validation (Appendix_G_3D_Analogues.md, read 2026-04-21).** Three of the six analogues (Barenblatt, Horizon, Temporal Tension) were re-run in 3D. All three structural patterns extend to 3D without modification; only numerical parameters shift per the `d`-dependent Laplacian:
- Barenblatt: `α_R = 1/(d(m-1)+2)` predicts `α_R = 0.2` for d=3, β=1; measured `0.1665` (16.7% pre-asymptotic error, same pattern as 2D at β=2). Compact support confirmed.
- Horizon threshold: `A_c` shifts from `0.41` (2D) to `0.45` (3D), consistent with Laplacian-at-peak scaling `−dA/σ²` — 3D dissipates the peak 50% faster.
- Temporal tension: baseline nonlinear-mobility repulsion present in all runs; telegraph-modulated reversal at H = 2 preserved; v-correlation exceeds 0.67 at H = 5. Drift rates slightly lower in 3D than 2D, consistent with solid-angle distribution of tail overlap.

**Axiom P7 (dimensional consistency) is thus empirically validated** — the same constitutive channels produce the same structural analogues in any dimension, with numerical parameters shifting only through the geometry of the Laplacian.

### 5.8 ED-Dimensional-01 Quantum Regime — the first anchored cross-scale mapping

**Source:** `Desktop/ED Important Papers/ED-Dimensional-01_Quantum_Regime.md`. Read 2026-04-21. This is the **first** of the five regime mappings (the others are Planck, condensed matter, galactic, cosmological). The quantum regime is chosen first because it has the strongest anchoring: `D_phys = ℏ/(2m)` is determined by a **mathematical theorem** (the Madelung transformation of the Schrödinger equation), not by physical analogy or experimental fit. Every other regime requires at least one parameter to be set by convention or measurement.

**Three characteristic scales (anchoring):**

| Scale | Formula | Origin |
|:---|:---|:---|
| `L_0` | `ℏ/(mc)` (reduced Compton wavelength) | Smallest length where single-particle probability density is meaningful |
| `D_phys` | `ℏ/(2m)` | **Madelung theorem** — the free-particle Schrödinger equation rewritten as a continuity equation for `|ψ|²` has this exact coefficient. Not an analogy |
| `T_0` | `L₀²·D_nd / D_phys = 2·D_nd·ℏ/(mc²) = 0.6·ℏ/(mc²)` for `D_nd = 0.3` | Derived; ≈ 0.6× Compton time |

**Superluminal `V_0 = c/(2·D_nd) = 1.667c`.** This is **not a physical velocity.** It is a scale conversion factor, a mathematical consequence of the parabolic nature of the PDE. The ED equation and the Schrödinger equation share this property: both are parabolic with infinite propagation speed; neither respects a causal light cone. A relativistic hyperbolic extension would be required for causal propagation. Treat `V_0` as a regime-boundary marker, never as a signal speed.

**The ED-to-quantum dictionary** (full table in the source document; key rows):

| ED parameter | Physical quantity | Status |
|:---|:---|:---|
| `ρ` | `|ψ|²` probability density | Anchored (via `R_0 = L₀^{-d}` so that `∫ρ` over `L₀^d` = 1) |
| `D` = 0.3 | Quantum diffusivity `ℏ/(2m)` | **Exact** (Madelung theorem) |
| `M(ρ) = M₀(1-ρ̂)^β` | Density-dependent probability-diffusion slowing | **ED-specific prediction** — distinguishes ED from standard QM |
| `P(ρ)` | Restoring force (confining-potential analogue) | Anchored |
| `v(t)` | Mean-field / decoherence mode amplitude | Candidate |
| `τ` | Decoherence timescale | Candidate |
| `H` | Environmental / measurement coupling | Candidate |
| `β = 2` | Mobility exponent (PME index `m = β + 1 = 3`) | Structural constitutive choice |

**Numerical values for the electron (d = 2):** `L₀ = 3.862×10⁻¹³ m`, `T₀ = 7.729×10⁻²² s`, `D_phys = 5.788×10⁻⁵ m²/s`. Planck-mass row recovers the Planck scales — the quantum and Planck regimes are connected by a single parameter (the particle mass).

**ED's strongest prediction / weakest link in the quantum regime** is the density-dependent mobility `M(ρ) = M₀(1 - ρ̂)^β`. Standard QM has constant diffusion. ED predicts probability-density transport **slows as `ρ → ρ_max`** (analogous to Pauli blocking / nonlinear Schrödinger dynamics). If observed, this distinguishes ED from standard QM. If no density-dependent slowing is ever observed in quantum systems, `β > 0` is falsified in this regime. No experimental evidence currently supports or refutes this prediction; it is the most testable distinguishing feature.

**Cross-regime validation** (ED-Dimensional-Master, read 2026-04-21): the universal nondimensional invariant `D_phys · T₀ / L₀² = 0.3` holds to machine precision across all five regimes — Quantum (`L₀ = ℏ/mc`, `D = ℏ/2m`), Planck (`L₀ = ℓ_Pl`, `D = √(ℏG/c)`), Condensed matter (user-fit, ~μm and thermal diffusivity), Galactic (1 kpc, `D_T = 2.1×10²⁷ m²/s`), Cosmological (`c/H₀` and `ρ_crit`). This is 61 orders of magnitude in length scale and the same invariant holds throughout. The structure-growth problem at cosmological scale (the monostable penalty cannot generate cosmic structure growth on its own) is flagged as the most fundamental open question of the ED program.

### 5.9 ED-Phys — The Architecture of Physical Law: Symmetry, Constraint, and Emergent Regularity

**Source:** PhilArchive, title *Event Density and the Architecture of Physical Law: Symmetry, Constraint, and Emergent Regularity*. Discovered in the 2026-04-21 PhilArchive survey; not on Desktop under this name. This paper is **philosophically central** to the ED program and had not been captured in prior orientation drafts.

**Central claim.** Physics typically treats its laws, symmetries, and conserved quantities as **fundamental features of the universe** — they are what *must* be true, and everything else is what *happens* to be true. The ED framework inverts this: laws, symmetries, and conservation quantities are **emergent architectural consequences** of ED structure (gradients, participation relations, compositional rule, decoupling surfaces), **not fundamental postulates**. Physics's laws are *what must emerge when the architecture is what it is*, not what must be stipulated.

**What the paper re-derives as emergent (rather than fundamental):**

| Standard framing | ED framing |
|:---|:---|
| Noether's theorem: symmetry → conservation law | Conservation emerges from invariance of ED gradients under participation-preserving transformations. Symmetries are architectural, not postulated. |
| Gauge invariance as fundamental | Gauge structure emerges from the redundancy of participation rules in ED-channel geometry (ED-I-14 / ED-I-13 interpretation). Not postulated; arises from the fact that identity alignment is a structural rather than substantive commitment. |
| Lorentz symmetry as a fundamental spacetime symmetry | Lorentz symmetry is a structural consequence of participation architecture (ED-07). Not a geometric axiom. |
| Conservation of energy / momentum | Emerges from the irreversibility of commitment (ED-10 §6) combined with the architectural constraint that committed micro-events cannot be unmade. |
| Time-translation invariance | Equivalent to the architectural claim that the compositional rule is stationary — which is itself a consequence of the pre-PDE axioms' subadditivity (ED-05 §4). |
| Second law of thermodynamics | Follows structurally from the monotone descent of the ED Lyapunov functionals (Law L2 of §5.6) and the irreversibility of commitment (ED-10 §6). |
| Constants of nature (c, ℏ, G, α...) | Not arbitrary fine-tunings. The dimensional atlas (§5.8) anchors each constant to a regime-specific structural quantity (`D_phys · T₀ / L₀² = 0.3` across 61 orders of magnitude). |

**Why this paper matters for orientation.** It is the **meta-claim that unifies the three ED tracks** documented at the top of this doc:

- **Empirical track** (UDM, Cluster Merger-Lag, BTFR, dwarf D_outer): tests *specific* emergent regularities.
- **Interpretive track** (ED-I-12/13/14/27): reinterprets *specific* phenomena (photonics, quantum info, topology, weak lensing) as ED-channel manipulations.
- **Scale-correspondence track** (ED-SC): identifies *architectural invariants* that recur across scales.

The Architecture-of-Physical-Law paper is **the philosophical claim behind all three tracks**: the reason any of these work is that physical "law" is itself emergent from architecture. When a session encounters a question like "why is physics governed by these specific laws?" or "why should ED be a candidate theory of *everything*, not just a theory of *dark matter*?" — this paper is the reference. The empirical, interpretive, and scale-correspondence tracks all presuppose its central claim.

**How this connects to the Emergence-Universe sandbox (§11).** The ED-SIM sandbox is the **empirical demonstration** of this paper's philosophical claim: in a deterministic minimal universe where the architecture is known and explicit, the 14 laws I–XIV emerge inevitably. No randomness, no external forcing, no imposed symmetries — the laws are "the walls, and the physical laws we observe are just the shape of the space trapped inside them" (README verbatim). The Generative Closure theorem (Law XIII: exactly 10 sub-mechanism types, no 11th possible) is the sandbox-level proof that the architecture *forbids alternatives* — which is the same claim the Architecture-of-Physical-Law paper makes for our universe.

**Reading-order placement.** For a new session, this paper sits between ED-10 (emergence map) and ED-13 (master empirical synthesis). It is the *why* behind ED-10's coarse-graining dictionary: why space, time, curvature, and horizons are architectural outputs, not metaphysical inputs.

## 6. The environment-sourcing revision (ED-XX April 2026) — MOST IMPORTANT UPDATE

### What the ED-XX 3D argument showed

> **Attribution note.** Earlier drafts of this orientation called this "what ED-Sim-01 showed." That attribution is wrong — the actual ED-Sim-01 paper is the Scenario-D architectural-invariants experiment (§6.8), which contains no Green's-function derivation. The 1/r dilution argument's source document is still unlocated; the summary below is reconstructed from ED-XX's own Table (see §6, "Numerical scan") and is presumed to live inside the ED-XX paper itself.

- The 3D steady-state Green's function of the temporal-tension PDE is `T(r) ∝ (1/r)·exp(−r/ℓ_T)`.
- **The `1/r` geometric dilution dominates long before exponential decay kicks in.** This is a geometric fact of 3D, absent in 1D.
- A compact galactic source (5–20 kpc) cannot produce a flat `T(r)` over the 10–1000 kpc range required by rotation curves / weak lensing — regardless of `ℓ_T`. The 1D intuition that motivated ED-02 and ED-04 fails in 3D.
- Flatness at 30–1000 kpc requires source width `σ ≥ 1–3 Mpc`.

### Numerical scan (from ED-XX Table)

| Source width σ | Flatness error over 30–1000 kpc |
|---:|---:|
| 5 kpc | 258% |
| 50 kpc | 71% |
| 500 kpc | 18% |
| 1000 kpc | 6.8% |
| 2000 kpc | **2.7%** |

### What this changes

- Galaxies (5–20 kpc): too small to source their own flat temporal-tension halos.
- Galaxy groups (0.5–2 Mpc), filaments (5–50 Mpc), local cosmic web: the correct source scale.
- **Role split:** the galaxy sets the *amplitude* (via its baryonic identity and internal event density); the environment sets the *spatial extent* (via megaparsec-scale collective activity).

### New predictions that distinguish ED from both CDM and MOND

1. **Activity-dependent weak-lensing velocities** — `V_∞ ∝ √S_env`, not `M_halo^(1/3)` (CDM) and not MOND's `a_0` threshold.
2. **Environmental coherence** — galaxies in the same group/filament share asymptotic V: `V_∞^(i) ≈ V_∞^(j)`. Incompatible with CDM (which gives each galaxy its own halo).
3. **No halo edge** — field is scale-free, no virial truncation.
4. **No MOND transition radius** — no `a = a_0` crossover.
5. **Merger-lag signatures preserved** — cluster mergers ARE the environmental source at cluster scale, so Cluster Merger-Lag work is unaffected.

### Implications for repo-level work

- **BTFR-activity test (ED-Data-12..17 + `papers/ED-BTFR-Activity/memo.md`)** — was testing galaxy-level ρ(sSFR, Δ_BTFR). Under ED-XX the proper variable is *environmental* activity, not individual-galaxy sSFR. Individual-galaxy sSFR correlates with environmental activity but imperfectly; signal is diluted. BIG-SPARC with group/filament cross-match is the right path.
- **Dwarf D_outer (ED-04.5)** — still stands. Qualitative "active" morphology correlates with environmental activity, so the 53% separation survives as an environmental proxy.
- **RLC analogue memo** — unaffected; tests the PDE's uniform-limit coupling structure, not what sources the field.
- **Cluster Merger-Lag** — unaffected; clusters are environmental sources already.
- **ED-I-27 weak-lensing interpretation** — written March 2026 under galaxy-sourced framing. Its core claim (weak lensing detects temporal-tension field, not mass) survives; what changes is the source identification.

---

## 6.5 The Interpretation Series (ED-I): quantum, optical, and topological extensions

The ED-I-XX papers are a *separate thread* from the main empirical program. They take established experimental/theoretical results from photonics, quantum information, and topology, and reinterpret them as manifestations of ED channel geometry. These are **interpretive/structural**, not empirical — they don't claim new measurements, they claim a unifying conceptual account of existing ones. They *do* make speculative predictions (listed below), but those predictions are mostly theoretical extensions rather than falsifiable near-term tests.

These papers introduce operational ED vocabulary not present in the PDE-level theory docs:

| Primitive | Meaning |
|---|---|
| **Chain** | A sequence of micro-events whose update rule maintains coherence along ED-gradients. Photons, electrons, etc. are chains. Identity = the update rule. |
| **Update rule / participation rule** | The specific sequencing logic that defines a chain's identity. |
| **Channel** *(in this context)* | A stable ED-gradient pathway that can instantiate a chain's update rule. Distinct from the PDE's mobility/penalty/participation "channels" — these are pathways, not dynamical terms. |
| **Multiplicity** | How many participation threads a channel can support. High-multiplicity = superposition-analogue. Minimal = one thread, rewrites on conflict. |
| **Identity alignment** | The specific rule a chain is currently committed to. |
| **Unresolved participation rule** | Entanglement = one rule spanning multiple endpoints before individuation. |
| **Rewrite-on-measurement** | Minimal channels cannot preserve incompatible commitments; measurement forces re-commitment. |
| **Global ED-curvature** | Property of a channel, not a local field. Nonzero even when local fields vanish — this is the structural source of topological phases. |
| **Parameter-space channel** | ED-channel defined in Hamiltonian parameter space, not physical space. The domain of Berry-phase-like phenomena. |

### ED-I-12 — Photonics (Feb 2026)

Connects Yablonovitch, Pendry, Capasso. Five "photonics moves" that describe landmark photonic phenomena as ED-channel manipulations:

1. **Removal of channels** — photonic bandgap = absence of viable ED-geometry for the chain's update rule. Chain simply fails to exist as a coherent identity. [Yablonovitch 1987]
2. **Inversion of channels** — negative index = local ED-relaxation reversed, chain follows inverted geometry. No momentum reversal, no causality violation. [Pendry 2000]
3. **Redirection of channels** — cloaking = redirection of ED-flow around a region. The interior is excluded *structurally*, not hidden dynamically. [Pendry 2006]
4. **Encoding of channels** — metasurface = new participation rule imposed directly on ED-structure. Abrupt phase discontinuity is a structural update, not a continuity violation. [Capasso 2011]
5. **Composition of channels** — generalized metasurface = composer of local update rules into a global ED-geometry. [Capasso 2016]

Speculative predictions: non-periodic bandgaps from arbitrary gradient incompatibility; cloaking without metamaterials via direct ED-flow shaping; metasurfaces capable of identity-modifying operations beyond phase control; structural limits on maximum ED-gradient curvature that preserves coherence.

### ED-I-13 — Quantum Information (Feb 2026)

Connects Bennett, Brassard, Deutsch, Jozsa, Shor. Five "quantum information moves":

1. **Global access** — Deutsch's algorithm: superposition = high-multiplicity ED-channel carrying many participation threads. Oracle applies one rule to the whole channel. [Deutsch 1985/1992]
2. **Global constraint extraction** — Deutsch-Jozsa: Hadamard layer is a reconciliation operation that tests whether channel geometry is uniform (constant function) or alternating (balanced function). [Deutsch-Jozsa 1992]
3. **Rewrite-on-measurement** — BB84: conjugate bases = incompatible channel commitments. Eavesdropping forces rewrite, leaves detectable inconsistencies. Security = self-revealing nature of minimal-channel incompatibility. [Bennett & Brassard 1984]
4. **Identity reassignment** — Teleportation: EPR pair = one unresolved rule spanning two endpoints. Bell measurement forces joint individuation; classical bits specify which alignment occurred. No state travels; identity is reassigned across unresolved structure. [Bennett et al. 1993]
5. **Symmetry extraction** — Shor: modular exponentiation imprints periodicity as global ED-symmetry; QFT is a symmetry-resolution operation that aligns threads at frequencies matching the channel's symmetry. [Shor 1994/1996]

Speculative predictions: new algorithmic classes based on symmetry extraction and global constraint resolution; cryptographic primitives based on channel incompatibility (broader than no-cloning); error-correcting codes based on distributed alignment rather than state redundancy.

### ED-I-14 — Topological Effects (Feb 2026)

Connects Aharonov, Berry, Bohm, Casher, Tonomura. Four variants of the same structural pattern:

1. **Curvature around confined flux** — Aharonov-Bohm: the region containing the flux has ED-structure inaccessible to the chain; channel is multiply connected; global ED-curvature is nontrivial. Phase is the ED-curvature enclosed. [AB 1959]
2. **Curvature persists under shielding** — Tonomura: shielding removes local fields but not global ED-curvature. Phase shift is a structural invariant of the channel, not a dynamical effect. [Tonomura 1986]
3. **Parameter-space curvature** — Berry phase: degeneracies act as curvature sources (ED-monopoles); the channel around a degeneracy is multiply connected. Same AB mechanism in parameter space. [Berry 1984]
4. **Dual curvature** — Aharonov-Casher: magnetic moment + line of charge produces curvature via a dual ED-channel geometry. AB and AC are dual manifestations of the same structural mechanism. [AC 1984]

Unifying claim: **topological phases are global invariants of ED-channel geometry**. They arise when a chain traverses a multiply-connected channel with nontrivial global curvature, and they do not require fields, forces, or potentials — only global structure.

Speculative predictions: new topological phases from engineered ED-geometries; non-Abelian generalizations from multi-channel ED-structures; flux quantization as ED-curvature quantization; experimental regimes where shielding modifies local fields but not global curvature.

### How to treat the Interpretation Series in future work

- **These are interpretive extensions, not empirical tests.** A future session should not confuse an ED-I "prediction" with a falsifiable near-term test like UDM or Cluster Merger-Lag. The empirical suite lives in the mobility / penalty / participation program documented in §7; the ED-I papers live in the ontological extension program documented by ED-10.
- **The vocabulary in the table above is useful when reading other ED papers** — "chain," "multiplicity," "identity alignment," etc. appear across the interpretation series. They are *operational* primitives for talking about what micro-event patterns ED's primitives support; they don't replace the PDE-level ρ, v, M, P notation.
- **If the user asks about a quantum/optical phenomenon** (e.g., "what does ED say about the quantum eraser?"), the right reference is ED-I-XX. The right form of answer is an interpretive reframing, not a prediction of a new measurement.
- **One potential convergence point with the physics program** — the Berry-phase / AB / AC machinery (global ED-curvature in multiply-connected channels) could in principle intersect with the cluster-merger wake machinery (a wake is a curved ED-structure around a moving source). I did not see this connection drawn explicitly in any paper I read; if it exists, it would sit at the boundary of I-14 and Cluster Merger-Lag. Worth exploring if the user is looking for a new theoretical direction.

## 6.6 The ED-SC Scale-Correspondence program (ED-SC-00, March 2026)

The ED-SC series is a third architectural program alongside the empirical and interpretive tracks. Its core claim: because ED primitives are scale-free (micro-events don't have a size; participation doesn't have units; ED gradients don't care about orders of magnitude), **the same architectural forms recur wherever ED gradients organize becoming**. Not analogy — structural identity.

When I noted earlier (in §6.5's ED-I discussion) a potential convergence between Berry-phase / AB / AC and Cluster Merger-Lag, this was exactly the convergence ED-SC-00 systematically documents as a research program. ED-SC-00 is the foundational paper of that program.

### Why scale-correspondence is predicted

Four structural reasons from ED-SC-00 §2:

1. **ED gradients are geometric, not material.** A Casimir cavity and a cosmic sheet share no material similarity, but both produce a planar ED channel with a suppressed direction because the geometry of becoming is the same.
2. **Micro-events scale, but ED structures do not.** Production rates vary; the *shape* of the gradient landscape (channels, saddles, divergence zones) does not.
3. **Participation and curvature are relational.** Relations don't depend on scale.
4. **ED thresholds create universal regimes.** Quantum emerges when ED is too sparse to individuate; classical emerges when ED is thick enough to stabilize. The transitions occur at different physical scales in different systems, but the architectural logic is identical.

### New architectural vocabulary (complementary to ED-I's chain/multiplicity/etc.)

Six recurring motifs across all scales:

| Motif | Definition | Examples across scales |
|---|---|---|
| **Pocket** | Region of suppressed or enhanced ED relative to surroundings | Casimir cavity (low-ED), cosmic sheet (high-ED) |
| **Channel** | Participation pathway with dominant direction + suppressed directions | Nanoscale cavity, optical resonator, thin film, galaxy sheet, cosmic filament |
| **Saddle** | Mixed-curvature structure: convergent along one axis, divergent along another | Gravitational potential, Casimir cavity, thin-film instability, Local Group mass sheet |
| **Divergence zone** | Region where flow cannot accumulate | Cosmic void, off-plane regions in mass sheets, forbidden ranges in Casimir systems |
| **Stationary point** | Location where competing ED gradients cancel | Casimir equilibrium thickness, orbital radius, thin-film thickness |
| **Threshold** | ED level where qualitative behavior changes | Individuation (quantum ↔ classical), curvature formation, horizon formation |

These are a DIFFERENT layer from the ED-I vocabulary (chain / multiplicity / identity alignment / rewrite-on-measurement / global ED-curvature). The ED-I primitives describe how *a single chain* interacts with an ED-gradient pathway; the ED-SC primitives describe *the shape* of the gradient pathway itself. Both layers are compatible with the PDE-level canon (P1–P7).

### The ED-SC method (7 steps)

1. **Extract the ED channel** in each system (dominant direction, suppressed directions, stabilizing gradient).
2. **Identify suppressed and open directions** — the pattern of suppression/openness is often the clearest architectural fingerprint.
3. **Identify competing ED contributions** — most ED structures arise from balanced gradients.
4. **Identify the curvature structure** — classify as pocket / channel / saddle / ridge / divergence zone.
5. **Identify the stationary point** where gradients cancel.
6. **Align the structures across systems** — parallel table, row by row.
7. **Extract the scale-free rule** — the architectural invariant that survives when scale/mechanism/substrate are stripped away.

### First overlay (case study): Local Group Mass Sheet ↔ Golden Casimir Cavity

- **Local Group mass sheet** (cosmological, ~10⁷ light-years across): flat ED sheet with divergence zones above/below. Milky Way–Andromeda pair provides inward curvature; extended mass sheet provides outward curvature. Local Group sits in the resulting saddle at the stationary point.
- **Golden Casimir cavity** (nanoscale, ~10 nm thick): gold flake above gold substrate in salt water. Casimir effect lowers ED between plates; electrostatic interactions raise it. Flake stabilizes at the cavity thickness where these gradients cancel.
- **Systems differ by ~20 orders of magnitude.** They share identical ED architecture: planar channel with one suppressed direction + two open directions + competing gradients + curvature saddle + stationary point at gradient cancellation.

**Scale-free rule extracted:** *A planar geometry with one suppressed direction and two competing ED contributions produces a saddle-shaped channel whose flows diverge along the open directions and settle at a stationary point where the gradients cancel.*

### Table 1 — Full micro ↔ cosmological correspondence map (from ED-SC-00 §6)

This is the key table for answering "what does ED say about <quantum/optical phenomenon> at cosmological scale?":

| ED-I (micro-scale) | Cosmological analogue (macro-scale) |
|---|---|
| 001 — Superconductivity | Coherent, low-resistance flow along cosmic filaments |
| 002 — Entanglement | Long-range synchronized behavior between distant voids / filaments |
| 003 — Spin | Galaxy spin alignment across filaments and void boundaries |
| 004 — Quantum–Classical Boundary | Transition zones between void interiors and filament nodes |
| 005 — Magnetism | Directional flow alignment along large-scale filaments |
| 006 — Fields & Forces | Gravitational potentials as tension gradients shaping cosmic flow |
| 007 — Double-Slit | Void–filament bifurcation and interference-like density patterns |
| 008 — Higgs / Mass Generation | Mass-dependent drift in void expansion and filament anchoring |
| 009 — Neutrino Oscillation | Galaxy drift across curvature basins with regime transitions |
| 010 — Gravity Waves | Void "breathing modes" and large-scale curvature oscillations |
| 011 — Baryogenesis | Asymmetric void expansion and anisotropic filament formation |
| 012 / 018 — Photonics | Photon-like curvature packets moving through void/filament geometry |
| 013 — Quantum Information | Cosmic web evolution as curvature-encoded information processing |
| 014 — Topological Effects | Topologically protected filaments and void walls |
| 015 — Microresonators | Galaxy groups orbiting within curvature wells (resonant basins) |
| 016 — Casimir Self-Assembly | Filament formation from void-driven curvature imbalance |
| 017 — Time-Duration Symmetry | Phase-locked expansion rates across connected voids |
| 019 — Mass Gap | Minimum density thresholds for filament formation |
| 020 — Spin–Momentum Locking | Galaxy spin-flow alignment along filament channels |
| 021 — Chiral Phonons | Chiral galaxy streams around void boundaries |
| 022 — Local Group Anisotropic Mass Structure | Direct cosmological case: asymmetric curvature around the Local Void |

### Speculative correspondences proposed for future overlays (ED-SC-00 §7.3)

- thin films ↔ galaxy walls
- nanowires ↔ cosmic filaments
- optical cavities ↔ gravitational wells
- convection cells ↔ cosmic void flows
- quantum wells ↔ orbital basins

Each of these, per the ED-SC method, would involve identifying the channel, competing gradients, curvature structure, and stationary point in both systems, then extracting the shared architectural rule.

### Implications for the ED program (both practical and scientific)

1. **A nanoscale system instantiating the same ED geometry as a cosmological one becomes a laboratory proxy for the larger structure.** This is a *two-way bridge* between scales. If ED-SC is correct, benchtop experiments on Casimir cavities, optical resonators, or thin films are effectively probing the same architectural form that governs galaxy walls or cosmic filaments.
2. **ED-SC strengthens the empirical program.** Any successful correspondence (e.g., the Local Group ↔ Casimir overlay) is a compression of multiple phenomena into a shared architectural rule — the signature of a unifying theory (§7.1 "elegance as evidence").
3. **ED-SC predicts new experiments.** Once an architectural form is identified, search for it in other domains: if the ED channel matches, the behavior should match. This is a new kind of predictive power that traditional physics doesn't offer.
4. **ED-SC reframes how to read physical systems.** Instead of "what forces act here / what equations apply," ED-SC asks "what is the geometry of becoming / where are the gradients / what stationary points define stability." This reframing can reveal unity where fragmentation had been assumed.

### How to handle ED-SC in future sessions

- **If the user asks "does ED predict a connection between <micro phenomenon X> and <cosmological phenomenon Y>" — check Table 1 above first.** Many such connections are already mapped there.
- **If the user wants to propose a new scale-correspondence overlay** — guide them through the 7-step method. The output is a correspondence table + scale-free rule, same format as the Local Group / Casimir case.
- **ED-SC is a *program*, not a completed atlas.** Only one full overlay exists (Local Group / Casimir). The ED-SC series will grow. If the user mentions ED-SC-01, ED-SC-02, etc., those are new overlays not yet captured here.
- **ED-SC is compatible with but distinct from ED-I.** ED-I identifies what *specific classical experiments* look like through the ED lens; ED-SC identifies *architectural invariants* that recur across domains. A single phenomenon may appear in both programs under different framings (e.g., Berry phase is an ED-I-14 reinterpretation of an experiment; it is also an instance of "global ED-curvature around a multiply-connected channel" that recurs at galactic scale per Table 1 row 014).
- **ED-SC does NOT supersede the empirical program (UDM, Cluster Merger-Lag, etc.) or the PDE canon.** It supplements them with a new way of identifying architectural invariants. The empirical tests remain the means of falsification.

## 6.7 ED-SIM-3D (March 2026) — the dimensional-consistency validation

**Added in v1.2.** ED-SIM-3D (`ED-SIM-3D_Canonical_PDE_2D3D_Extension_and_Invariant_Mini-Atlas.md`, Desktop `ED Important Papers/`) extends the ED PDE solver from 2D to a fully general d=1,2,3 framework and runs five targeted invariant tests to confirm that the structural correspondences of the foundational paper are **dimension-independent properties of the PDE, not artifacts of a particular spatial dimension**. The paper validates Canon principle P7 (architectural equivalent of "dimensional consistency").

### Earlier-draft correction carried forward

**v1.1 speculated** that ED-SIM-3D was "probably source material for ED-XX's 3D Green's-function argument." **That speculation was wrong.** ED-SIM-3D is a March 2026 document covering *cross-dimensional* invariants of the canonical PDE; it does NOT contain the `T(r) ∝ (1/r)·exp(−r/ℓ_T)` Green's-function derivation that forced the April 2026 environment-sourcing revision. That derivation must live in a different (still-unread) document — likely the ED-XX paper itself or a separate "ED-Sim-01" programme document.

### The five invariant tests

Each test is run in d=1, 2, 3, comparing measured behavior against analytical predictions:

| # | Test | Channel exercised | Dimension-dependent? |
|:--|:-----|:------------------|:--------------------|
| 1 | Barenblatt PME (`∂_t δ = D_pme ∇²(δ^m)`) | Mobility | **YES** — front-radius exponent `α_R = 1/(d(m−1)+2)` |
| 2 | RC decay (uniform perturbation, `δ̇ = −DP₀δ`) | Penalty | **NO** — `λ = DP₀` exact to machine precision |
| 3 | Telegraph oscillation (uniform IC + H>0) | Participation | **NO** — `ω, γ` exact to machine precision |
| 4 | Horizon formation (high-amplitude Gaussian, mobility → 0) | Mobility (geometric) | **YES** — effective `A_c` shifts from 0.410 (d=2) to 0.450 (d=3) via Laplacian peak scaling `−dA/σ²` |
| 5 | Participation coupling (weak penalty + H>0) | Mobility × participation | **NO** (frequency match) — `v–δ` frequency match dimension-independent |

### The structural dividing line

**Dimension-independent:** properties of the **penalty and participation channels** (zero-order operators, no spatial derivatives). These produce identical behavior in 1D, 2D, 3D to machine precision.

**Dimension-dependent:** properties of the **mobility channel** (which involves the Laplacian). The Laplacian scales with `d` — specifically, the Laplacian at the peak of a d-dimensional Gaussian is `−dA/σ²` — which produces:
- Slower Barenblatt spreading in higher d (`α_R` decreases).
- Faster peak decay in higher d (horizon threshold `A_c` rises).
- Shorter horizon lifetimes in higher d.

**All dimension-dependent effects trace to a single source: the Laplacian scales with `d`.** None of these are deviations from ED theory — they are predictions of it, confirmed by simulation.

### Structures unique to higher dimensions

Higher-d simulations reveal transient structures absent in 1D:
- **Rings (2D) and shells (3D)** during the PME spreading phase when the initial condition has a central dip.
- **Anisotropic fronts** from non-radially-symmetric IC that relax to circular/spherical symmetry.
- **Hessian morphology** (blobs / filaments / sheets) classifiable via Hessian eigenvalues in 2D/3D. ED-SIM-02's invariant atlas tracks the morphological progression **blobs → filaments → sheets → uniform** over time. This progression is absent in 1D (single Hessian eigenvalue).

### Numerical specifics a future session may want

- **Solver:** implicit Euler with fixed-point (Picard) iteration, 8–12 iterations per step at tolerance 10⁻⁷–10⁻⁸. Unconditionally stable. Finite-difference stencils: (2d+1)-point Laplacian (3/5/7 points for d=1/2/3), central-difference gradient squared, Neumann BC via mirror ghost cells.
- **Participation ODE:** advanced by exact exponential integration, dimension-independent.
- **Grid scale:** 3D at N=64 is ~3×10⁶ operations/step (~0.1 s on modern CPU); N=128 is ~2.5×10⁷ ops/step (~1 s).
- **Pre-asymptotic regime:** at β=2 (m=3), 2D and 3D Barenblatt exponents approach the theoretical value from below — accessible grids (N=64–128) do not reach the self-similar limit. This is a *known* PME property, not a failure.

### ED-SIM-02 — the referenced software package

ED-SIM-3D cites "ED-SIM-02: An Architectural Lab for Entropic Dynamics. Software package (2026)" as the implementation. Key features inferred from the paper:
- Supports d=1, 2, 3, 4 (4D operators implemented but 4D invariant tests not yet run).
- Neumann, Dirichlet, and periodic boundary conditions.
- Implicit Euler finite-difference solver (primary) + ETD-RK4 spectral solver in 2D (for cross-validation — not yet run in 3D).
- Tracks Hessian morphology (blob/filament/sheet fractions) as part of the invariant atlas.

When a future session asks "how does ED simulate / what solver / what grid" — this is the reference.

### Open questions flagged by the paper

1. **4D validation** — operators implemented, five invariant tests not yet run.
2. **Spectral solver cross-validation in 3D** — would confirm solver-independence.
3. **Pre-asymptotic convergence at β=2 in d=3** — needs finer grids or Richardson extrapolation.
4. **Dimension-dependence of β** — is β itself regime- or dimension-specific?
5. **Vector/tensor-valued participation variable in higher d?** — would extend beyond axiom P5 (single scalar field).

### How to use ED-SIM-3D in future sessions

- **If the user asks about dimensional consistency / axiom P7 / the claim "same PDE governs Planck to Hubble scale"** — ED-SIM-3D is the empirical numerical validation. Cite specific rows of Appendix D (cross-dimensional scaling table).
- **If the user asks why Barenblatt spreading is slower in higher d but RC decay isn't** — the split is between channels-with-spatial-derivatives (mobility, dimension-dependent) and channels-without (penalty + participation, dimension-independent). Point to §4.6 of ED-SIM-3D.
- **If the user asks about the ED-XX 3D Green's-function argument** — **do not cite ED-SIM-3D.** That argument lives elsewhere; its source document is still unread.
- **If the user asks about the Python simulation engine** — ED-SIM-02 is the package name. Repo has `edsim/` which is likely the same package or an adjacent implementation (worth a future reconciliation pass).

---

## 6.8 ED-Arch / ED-Sim-01 (March 2026) — the architectural-invariants program

Two paired papers — ED-Arch-01 (experimental) and ED-Arch-02 (theoretical) — establish that the architectural motifs (saddles, channels, boundaries, horizons) used by the ED-SC scale-correspondence program are **mathematically necessary outcomes of the ED update rule**, and are **empirically recoverable** in controlled simulation.

### Filename / title reconciliation

**ED-Arch-01 == ED-Sim-01.** The two Desktop files have identical abstracts, methods, figures, and numerical results (saddle peak at `n=2.7, σ=0.0556`, step 457). They are the same underlying paper filed under two series labels:
- `Desktop/ED-Arch-01 Architectural Invariants of Becoming_ Experimental Probes.pdf` — internal title "Emergent Architecture in Event Density: Structural Motifs Arising from Gradient, Curvature, and Mobility Dynamics"
- `Desktop/ED Archive/ED-Simulations/ED-Sim-01 Architectural Invariants of Becoming_ Experimental Probes.pdf` — internal title "Architectural Invariants of Becoming: Experimental Probes of Scale-Free Event Density Geometry"

When a future session encounters "ED-Sim-01" OR "ED-Arch-01," assume they refer to this paper unless context demands otherwise. The simulation series continues with ED-SIM-02 (software package) and ED-SIM-3D (§6.7) — those are distinct from ED-Sim-01.

### Critical correction (carried forward from earlier drafts)

Earlier drafts of this orientation claimed "ED-Sim-01 derived the 1/r Green's function argument for ED-XX." **That claim is false.** ED-Sim-01 has nothing to do with 3D Green's functions; it is a Scenario-D parameter-sweep study of architectural invariants in the (n, σ) plane. The actual source of the ED-XX `T(r) ∝ (1/r)·exp(−r/ℓ_T)` derivation is still unlocated — likely inside the ED-XX paper itself on Desktop.

### ED-Arch-02 — the formal ontology (theory)

Defines the architectural objects via precise Hessian-based conditions on the ED field `E(x, t)`:

| Object | Mathematical criterion | Role |
|:-------|:----------------------|:-----|
| **Saddle** | Orthogonal gradient sign-flip: `∂_x E > 0, ∂_y E < 0` in one quadrant, opposite in the adjacent; `det(H) < 0` with λ_1 < 0 < λ_2 | Fundamental geometric unit; one axis of compression, one of expansion; anchor for higher-order structure |
| **Channel** | Alignment condition `d/ds(∇E/‖∇E‖) ≈ 0` along path `s`; transverse curvature `λ_⊥ > 0` (confining), longitudinal mixed (guiding) | Coherent corridor of aligned gradient flow; connects saddles into networks |
| **Boundary** | `λ_⊥ > 0` and gradient vectors converge | Compression-dominated "wall"; stabilizes pockets and long-lived structures |
| **Horizon** | `λ_⊥ < 0` and gradient vectors diverge | Expansion-dominated "open surface"; regulates noise flow; determines whether structures persist or dissolve |
| **det(H) = 0 curves** | Architectural "hinges" where one principal curvature changes sign | Separate channel interiors (mixed curvature), boundary walls (positive), horizon surfaces (negative) |

The general dynamics are decomposed as:

$$\partial_t E = M(E, \nabla E) + C(H) + \eta(x, t) - S(E)$$

where `M` is mobility-driven flow, `C` is curvature-driven reorganization, `η` is noise, `S` is suppression. Specific constitutive forms:

- **Mobility law:** `M ∝ ‖∇E‖^α`. Exponent α controls channel sharpness, boundary thickness, saddle stability, regime transitions. Higher α amplifies coherent structure.
- **Noise:** `η(x, t) ~ N(0, σ²)` with critical threshold `σ_c`. Above `σ_c`: saddles fail, channels fragment, boundaries dissolve. Noise is not a perturbation but a **sparsity field** that reshapes the ED landscape.
- **Suppression:** `S(E) = β E^γ`. Forms wells and pockets; controls balance between accumulation and dissipation.

### Four regimes (ED-Arch) — distinct from 00.3 D_crit regimes

**CRITICAL DISAMBIGUATION:** ED has two different four-/three-regime taxonomies that both use the word "regime." Do not conflate them.

| Taxonomy | Parameter axis | Regimes |
|:---------|:---------------|:--------|
| **00.3 damping regimes** (temporal) | Channel weight `D` (or discriminant Δ = D + 2ζ) | Oscillatory (D<0.1) / Hybrid (0.1≤D≤0.4) / Parabolic (D≥0.5) — sharp transition at D_crit = 0.5 |
| **ED-Arch regimes** (spatial/architectural) | Mobility exponent `α` (or `n`) + noise amplitude `σ` | Hyper-coherent / Stable-coherent / Marginal (saddle) / Non-individuating |

The ED-Arch four regimes:

| Regime | (n, σ) location in Scenario D | Mathematical criteria | Invariants status |
|:-------|:--------------|:----------------------|:------------------|
| **Hyper-coherent** | Low σ, high mobility (rapid exit, ≤100 steps, small L) | Persistent saddles with stable λ_i; strong gradient alignment; σ ≪ \|λ_i\|; α > α_c | All architectural invariants present and stable |
| **Stable-coherent** | Moderate σ, moderate mobility (100 < exit ≤ 300 steps) | Saddles with weaker curvature; aligned channels may drift; σ < σ_c | Most invariants present; stability reduced |
| **Marginal (saddle)** | Ridge of delayed exit (exit > 300 steps) | λ_1 ≈ 0 or λ_2 ≈ 0; det(H) crosses zero frequently; intermittent alignment; σ ≈ σ_c | Only partial invariants present; none stable — this is the architectural hinge of the entire parameter plane |
| **Non-individuating** | High σ, low mobility (no exit within 500 steps) | σ > σ_c; curvature fails to organize; no persistent sign-flip | No invariants present; noise-dominated diffusion |

Regime transitions are driven by noise (`σ` ↑: hyper → stable → marginal → non-individuating), by mobility (`α` ↓: pushes toward marginality), or by curvature (suppression depth shifts stable ↔ hyper-coherent).

### ED-Arch-01 — the Scenario D experiment

**Simulation setup:**
- 512×512 periodic lattice
- Discrete update rule: `p_{t+1}(i,j) = p_t(i,j) + Δt·[n·∇²p_t(i,j) − α·p_t(i,j)^γ + σ·η_t(i,j)]`
- 5-point Laplacian; unit-variance Gaussian noise; Δt = 1; clamped bounds `p_min ≤ p ≤ p_max`
- Form matches ED-SC-05.5 / ED-12.5 Analogues gradient-flow derivation
- 4×4 sweep: `n ∈ {0.5, 1, 2, 4}` × `σ ∈ {0.01, 0.02, 0.05, 0.10}`; 500 steps per cell

**Observables:**
- Phase-exit step (first iteration where the system forms a stable ED-structure, defined structurally via gradient variance + saddle-density threshold crossings).
- Final homogeneity scale `L` (autocorrelation first-zero-crossing + Fourier structure-factor peak width, averaged).
- Exit classification (phase-3 reached / no exit within 500 steps / trapped in sparse-gradient basin).

**Key results:**
- The phase-exit surface in (n, σ) space is a clean, monotonic **saddle**, with ridge peak at `n=2.7, σ=0.0556, step 457` (Hessian: κ_∥ ≈ −1.3, κ_⊥ ≈ +1.0, det(H) < 0 — confirmed ED saddle geometry, not numerical plateau).
- `L`-contours are nearly orthogonal (88° ± 4°) to the phase-exit-step gradient — the signature of an ED saddle (one axis compresses, the other expands).
- **The curvature ratio κ_∥/κ_⊥ ≈ −1.3 ± 0.2 quantitatively matches the reported ratio for the Local Group mass sheet and for Casimir cavity equilibria** — systems separated by 20+ orders of magnitude in physical scale but sharing the same ED saddle geometry.
- Four regimes cleanly delineated in the parameter plane (see table above).
- Global coherence persists even when local gradients fail — the system maintains the participation rule across sparse regions until structural mismatch becomes too large. This is the same mechanism behind tunneling, Josephson coherence, gravitational-wave phase shifts, and cosmic-web flow alignment.

### Cross-references to the ED-I interpretation series (from ED-Arch-01 §5)

The Scenario-D experimental regimes map directly to ED-I phenomena:
- Hyper-coherent ↔ superconducting channels (ED-I-023)
- Marginal (saddle) ↔ Josephson junction metastability (ED-I-023 / related)
- Mobility-controlled boundaries ↔ chiral phonon entrainment (ED-I-021), photonic Chern channels (ED-I-028)
- Non-individuating ↔ tunneling barriers (ED-I-029), gamma-ray transparency (ED-I-030), cosmic voids (ED-I-027)
- Saddle geometry also appears in: Local Group mass sheet (ED-I-022), gravitational wave scattering (ED-I-026), Calabi-Yau period emergence (ED-I-024)

### Implications flagged in the paper

From ED-Arch-01 Discussion + Conclusions:

1. **ED-gradients are experimentally accessible** — measured flow fields, stationary points, and curvature transitions match the predicted ED-channel geometry with high fidelity.
2. **Scale-correspondence is a physical principle, not an analogy** — the same saddle-channel architecture observed in the Local Group mass sheet and Casimir cavities appears in this engineered mesoscopic system. This is the first quantitative bridge to the ED-SC program.
3. **ED-channels provide a unifying description of dynamics across regimes** — flow, stability, and reconfiguration are governed by the geometry of becoming rather than by the specific forces involved.
4. **Phase boundaries in ED are architectural, not dynamical.** Saddles emerge generically whenever two orthogonal gradient families compete. Homogeneity scales are structural invariants, not emergent statistics.

### Future work (ED-Arch-01 §6.2)

Five-direction extension program:
1. **Scaling the architecture** — systematically vary channel width, suppression depth, and gradient steepness (Figure 08 shows preliminary three-panel comparison: shallow/baseline/deepened channels).
2. **Multi-channel architectures** — couple two or more channels; test ED's prediction that reconfiguration follows global, not local, constraints. Mesoscopic analogue of void–filament bifurcation.
3. **Temporal dynamics and reconfiguration** — measure reconfiguration timing; identify threshold crossings; look for the analogue of gravitational "breathing modes."
4. **Cross-scale correspondence tests** — construct dimensionless ED-invariant ratios; compare directly to astrophysical reconstructions; test stationary-point drift under asymmetric forcing against the Wempe et al. galaxy-drift reconstruction.
5. **Predictive ED engineering** — engineer channels with targeted saddle curvature; use ED-threshold tuning to create switchable quantum-like ↔ classical-like identity regimes; explore topological ED-channels.

### How to handle ED-Arch / ED-Sim-01 in future sessions

- **If the user mentions "ED-Sim-01"** — it refers to this architectural-invariants paper. Earlier Claude sessions invented a phantom "ED-Sim-01 Green's-function document" and attributed the 1/r dilution argument to it; no such separate document exists.
- **If the user asks about saddles, channels, boundaries, horizons as formal architectural objects** — cite ED-Arch-02 for the math (Hessian criteria) and ED-Arch-01 for the experimental demonstration. These supersede any informal/analogical treatment earlier in the ED series.
- **If the user asks about regimes** — always clarify which regime taxonomy: 00.3 temporal damping regimes (D_crit = 0.5) or ED-Arch spatial-architectural regimes (hyper-coherent / stable-coherent / marginal / non-individuating). They are different.
- **If the user asks about empirical support for scale-correspondence (ED-SC)** — ED-Arch-01 is now the first-order evidence. Quote κ_∥/κ_⊥ ≈ −1.3 matching Local Group mass sheet and Casimir cavity across 20+ orders of magnitude.
- **If the user asks about the ED-XX 3D Green's function argument** — continue to flag that the source document is NOT ED-Sim-01 / ED-Arch-01 / ED-Arch-02 / ED-SIM-3D, and is still unlocated. The most likely location is inside the ED-XX paper itself.

### Implications for how the four tracks relate

The ED framework's track structure is now clearer:

| Track | Goal | Primary papers | Status |
|:------|:-----|:---------------|:-------|
| **Empirical PDE** | Predict new measurements | UDM, Cluster Merger-Lag, ED-13, ED-XX | Active, multiple confirmed results |
| **Interpretive (ED-I)** | Reframe existing phenomena | ED-I-12, 13, 14, 27 | 31+ papers, structural explanations |
| **Scale-correspondence (ED-SC)** | Identify architectural invariants across scales | ED-SC-00 + this is the track that ED-Arch formalizes | Expanding overlay atlas |
| **Architectural-invariants (ED-Arch / ED-Sim-01)** | Formalize the invariants + empirically recover them | ED-Arch-01 / ED-Sim-01, ED-Arch-02 | First-order evidence in hand |

ED-Arch can be read as **the formal + experimental foundation of ED-SC**: ED-SC identifies *where* the invariants appear (Table 1, 22 correspondences); ED-Arch defines *what they are* mathematically (Hessian geometry) and *demonstrates* their inevitability in a controlled system.

---

## 6.9 ED-SC 2.0 — the canonical invariance statement

The cross-scale architectural invariance claim as originally written in ED-Arch-01 §5 and ED-Arch-02 §3 was ambiguous between two different Hessians — the parameter-space Hessian of the `(n, σ)` phase-exit-step surface, and the field-space Hessian `∇²E` of the event-density field. This ambiguity was resolved in favour of the field-space form, then refined to the **motif-conditioned median** form, which is now the canonical ED-SC invariance statement.

**Full formal statement:** [`docs/ED-SC-2.0.md`](ED-SC-2.0.md).

### Short form

> For every pair of ED-architecturally-equivalent systems with a 2D real-space event-density field `E(x, y)`, the medians of the motif-conditioned Hessian eigenvalue-ratio distributions `ℛ_motif(E)` satisfy
>
> `|med(ℛ_motif(E_A)) − med(ℛ_motif(E_B))| ≤ 0.2`
>
> with the common value `r* ≈ −1.30`. Scenario D at `(n* = 2.7, σ* = 0.0556)` serves as the reference: `med(ℛ_motif(p_ScenD)) = −1.304`.

### The motif filter (pre-registered parameters)

At a Morse saddle `x*` of the smoothed field, trace four rays of length `L_ray = 2` lattice units along the principal-axis directions of `H(x*)` with periodic wrap. Admit `x*` iff the two rays along the compression axis (negative-eigenvalue eigenvector) descend below `E_lo = p̂ − α·std(E)`, and the two rays along the expansion axis ascend above `E_hi = p̂ + α·std(E)`, with threshold parameter `α = 0.25`. Degeneracy tolerance `δ = 0.10` (filter out saddles where `|λ_min|/|λ_max| < δ`).

These parameters are **fixed across all comparison systems** by pre-registration. The only per-system tuning is the sampling-grid resolution, which must satisfy `Δx ≤ L_coh(E)/8`.

### What was dropped

- **The IQR is not claimed invariant.** ED-SC 2.0 makes no claim about the spread of `ℛ_motif`. The canonical Scenario-D distribution has IQR width 0.73, which is broader than the `±0.2` tolerance of ED-Arch-01 if that tolerance is read pointwise.
- **Raw pointwise invariance is falsified.** Median over all Morse saddles (no motif filter) is `−1.94` in Scenario D; this is not `−1.3`. Without the motif filter, the field-space Hessian has no tight cluster at `−1.3`.

### Valid comparison systems (§5 of ED-SC-2.0.md)

Only real-space 2D density fields qualify:

| System | Field |
|:-------|:------|
| Local Group projected density | `Σ(x, y)` from mass-sheet reconstruction |
| Casimir cavity | lateral interaction potential `U(x, y)` |
| Thin-film dewetting | film thickness `h(x, y)` (pre-rupture regime) |
| Stripe domains | scalar order parameter `φ(x, y)` (PFM / MFM / TEM) |
| Reaction-diffusion (gradient form) | activator concentration `u(x, y)` |

### Invalid comparison systems (previously considered)

Under ED-SC 2.0 the following are excluded as cross-scale targets:

- **k-space band-structure saddles** (graphene NN-TB M-point, tBLG van Hove, kagome, triangular lattice): `E(k_x, k_y)` is reciprocal-space, not a real-space density.
- **Lagrange-point effective potentials:** the Hessian is of `Ω(x, y)` (effective gravitational-plus-centrifugal potential), not an event-density field.
- **OSCER cross-slot strain-rate tensors:** rank-2 tensor eigenvalues, not `∇²E`.
- **Minimal-surface curvature (catenoid, gyroid):** geometric identity `H_1 + H_2 = 0`, unrelated to Hessian of a scalar density.
- **Crack-tip stress fields:** singular, not Morse saddles.

Any prior orientation text or memo that treated these as cross-scale candidates is superseded by this exclusion list.

### Reference measurement

| Parameter | Value |
|:---|:---|
| Scenario | D (Noisy Universe, Langevin mobility-weighted update) |
| Update rule | `ed_step_mobility` from `Emergence Universe/ED-SIM-Code/ED_Update_Rule.py` |
| Grid | 64 × 64, periodic |
| `α` (penalty) | 0.03 |
| `γ` (penalty exponent) | 0.5 (concave) |
| `dt` | 0.05 |
| `p_min, p_max` | 0.01, 1.0 |
| IC | uniform `[0.3, 0.7]` |
| Seed | 77 |
| `n*` (mobility exponent) | 2.7 |
| `σ*` (noise amplitude) | 0.0556 |
| Steps | 500 (`t_phys = 25`) |
| **Motif-conditioned median** | **−1.304** |

Reproduction code: `analysis/scripts/ed_arch_r2/r2_canonical.py` + `r2_motif_filter.py`.

### How to handle ED-SC 2.0 in future sessions

- **If a user asks "what is the ED-SC architectural invariant"** — cite ED-SC 2.0 §2 (motif-conditioned median form). Not ED-Arch-01 §5.
- **If a user wants to propose a new cross-scale test** — check §3 of ED-SC-2.0.md first to confirm the candidate system has a native 2D real-space scalar field. If not, the candidate is out of scope.
- **If a user cites ED-Arch-01's `−1.3` as cross-scale evidence** — clarify which Hessian the citation refers to. Under ED-SC 2.0 the value is the motif-conditioned median of the field-space Hessian. The parameter-space Hessian of the phase-exit-step surface at the same `(n*, σ*)` numerically agrees (`−1.3` vs `−1.304`), but whether this agreement is structural or coincidental is an open theoretical question.
- **If a user asks about the IQR or distribution spread** — ED-SC 2.0 does not claim spread-invariance. The IQR in Scenario D is `[−1.94, −1.21]`, width 0.73. Wider than the `±0.2` falsification tolerance on the median, which is deliberate: the invariant is the median, period.

---

## 6.10 Factor Skyline evaluation (X5D) — meta-architectural audit

**Source:** `Desktop/ED Important Papers/X5D_Evaluation_EventDensity.md`. Read 2026-04-21. This is a **meta-architectural** evaluation of ED using the Factor Skyline (X5D) framework for assessing theoretical minimality, locality, determinism, generative sufficiency, envelope tightness, and structural optimality. It does not add new physics — it evaluates ED as a *theoretical object* and reports whether ED clears each FS criterion.

### The six FS criteria

| Criterion | Meaning | ED verdict |
|:---|:---|:---|
| **Minimality** | Irreducible set of primitives; no redundancy | **PASS.** Four primitives (ρ, M, P, v) plus seven axioms (either set; see §3.1). Removing any primitive breaks the PDE uniqueness theorem; removing any axiom admits PDEs outside the ED class. |
| **Locality** | Update rule depends only on local field values and finite-order local derivatives | **PASS.** The mobility and penalty channels depend only on `(ρ, ∇ρ, ∇²ρ)` at the local point. The participation variable `v(t)` is global but couples uniformly — it is a **structural non-locality**, not a violation of axiom P1. The Canon counts this as P2 Channel Complementarity, not a failure of locality. |
| **Determinism** | Given initial conditions and boundary data, the solution is uniquely determined | **PASS.** Follows from the per-channel well-posedness theorems of ED-Math-01. No stochastic terms in the canonical equation; noise enters only in ED-Arch / Scenario-D experimental probes (§6.8). |
| **Generative sufficiency** | The framework generates physics-shaped structure without external tuning | **PASS.** Six structural analogues (§5.7) demonstrate this: RC decay, Barenblatt PME, Stefan horizons, telegraph oscillation, oscillation-modulated spreading, emergent pair interactions — all arise from the canonical PDE with no additional parameters. |
| **Envelope tightness** | The theory does not over-generate: it produces only the phenomena it claims | **PASS.** Analogue 4's negative result (horizons don't oscillate) is evidence for envelope tightness — the framework refuses to generate phenomena incompatible with its structural laws (L1 unique attractor, L7 horizon formation). |
| **Structural optimality** | Constraint/parameter accounting — more independent constraints than free parameters | **PASS.** 28 total constraints identified across the corpus (four ED-05 + seven derivation + seven Canon + nine L-laws + 1 D_crit). ~18 independent after deduplication. 8 free parameters (`D, H, ζ, τ, ρ*, ρ_max, M₀, β` — with `P_0` treated as regime-specific). **Overdetermination ratio ~18/8 = 2.25**, strongly in the over-determined regime. |

### What X5D adds to the ED program

**Four channels + five universality classes.** The X5D framework re-labels the three ED channels plus a "halo / cosmic web" channel as four constitutive channels (Mobility M, Tension T, Halo H, Participation V), and identifies five universality classes that the canonical PDE can realize:

| Class | Channels active | Physical correspondence |
|:---|:---|:---|
| **PME** | Mobility only | Porous-medium / Barenblatt spreading |
| **RC** | Penalty only | Exponential / Debye relaxation |
| **Stefan** | Mobility + Penalty | Free-boundary / transient horizon dynamics |
| **Telegraph** | All three (full ED) | Oscillation-modulated nonlinear diffusion with global feedback |
| **Void** | Degenerate / no active channel | Trivial or singular limit |

These five classes are the same five that ED-13 and the Foundational Paper v2 refer to as "structural analogues." X5D's contribution is to show they are the **complete** set of universality classes the canonical PDE supports — no additional classes emerge under any parameter choice, which is a sharper statement than the foundational paper's six-analogue demonstration.

### How X5D relates to the rest of the ED corpus

- X5D **does not add empirical predictions.** It is a theoretical-object audit.
- X5D **is complementary to ED-Math-01** (which proves uniqueness) and the **Canon 00.2** (which axiomatizes architecture): X5D provides the meta-accounting that checks whether the uniqueness + axiomatization together yield an over-determined, minimal, structurally-optimal theory. The answer is yes on all six FS criteria.
- If a future session is asked "is ED a well-formed theoretical object?" — the answer is documented in X5D, passing all six FS criteria. Cite X5D when the question is about theoretical hygiene rather than empirical content.

---

## 7. Empirical status at a glance

| Channel tested | Regime | Test | Status | Repo path |
|---|---|---|---|---|
| Mobility | Condensed matter | UDM, 10 materials | ✓ R² > 0.986 | `papers/Universal_Mobility_Law/` + [`UDM_Extension_Log`](../experiements/Universal_Mobility_Law_Evidence/UDM_Extension_Log.md) (2026-04-22: Material #11 Roosen-Runge BSA neutron-scattering fit β=2.15, R²=0.923 — cross-technique consistent with fluorescence β=2.12; 7 candidates pending extraction) |
| Penalty + moving source | Cluster mergers | Cluster Merger-Lag, 7 clusters + Finner | ✓ `ℓ = D_T/v_current` | `papers/Cluster_Merger_Lag_Evidence/` |
| Scale dependence (SL vs WL) | Cluster inner vs. outer wake | Bullet + MACS J1149 | ✓ (n=2, scoping for A2146) | `papers/ED-Finner/` (session work) |
| Activity-at-fixed-mass | Dwarf SPARC D_outer | ED-04.5 | ✓ 53% Active>Quiet | Desktop PDF |
| Activity-at-fixed-mass | SPARC BTFR residual | ED-Data-12..17, union | ✗ no signal under V-on-M control — **mis-framed per ED-XX** | `data/ED-Data-12..17/`, `papers/ED-BTFR-Activity/` |
| Mobility (lab, BSA) | **UDM FRAP** — `R(t) ~ t^(1/6)` front propagation in concentrated BSA | Creative Proteomics quote | ⏳ **CP quote received 2026-04-22: ~$1500/sample, under technician review**; decision window 2026-04-24 to 2026-05-01 | **[`FRAP-High-BSA protocol`](../experiements/FRAP-High-BSA_InProcess/protocol.md)** — captures submitted-to-CP protocol + analysis pipeline + decision tree (label corrected 2026-04-21: this is a mobility-channel test, not participation) |
| Participation (lab, reanalysis) | ED-09.5 envelope on FRAP residual at 80–800 Hz via Lomb-Scargle | Public FRAP datasets (cell-biology literature) | ⏳ self-contained; 1 week to result | **[`ED-09-5-Envelope protocol Track B`](../experiements/ED-09-5-Envelope_InProcess/protocol.md)** — no third-party dependency; fastest path to new ED empirical result |
| 3D temporal-tension PDE | Galactic field structure | ED-Sim-01 | → forced April 2026 revision | referenced in ED-XX only |
| RLC / uniform-limit coupling | Benchtop | `papers/ED-RLC-Analogue/` + notebook | ⏳ simulation done; **components ordered 2026-04-22** (AstroAI 180PCS film-capacitor kit + resistor kit + breadboard), lab not yet run | Session work |
| **ED-SC 2.0 motif-conditioned median** | **Thin-film polymer dewetting (pre-rupture h(x,y))** | **AFM scan + motif filter (α=0.25, L_ray=2)** | ⏳ pilot N=1 ℛ_all agrees sim↔image (−2.063 vs −2.149); needs real motif-resolvable AFM data | **Highest-certainty near-term test.** Route 1: 2023 *Nat Comm Phys* check; Route 2: Jacobs email; Route 3: own AFM session — **operationalized at [`AFM-Dewetting protocol`](../experiements/AFM-Dewetting-ED-SC_InProcess/protocol.md)** |
| **ED-09.5 envelope (cavity-coupled)** | **Optomechanics raw `x(t)` (Delic 2020 / Magrini 2021)** | **§15(β) envelope extraction at `ω_v ≈ 8 γ_dec`** | ⏳ Aspelmeyer email v3 drafted, pending send; Vienna program map at [`ED_Vienna_Program_Map.md`](ED_Vienna_Program_Map.md) | Tier-1 in flight — **operational protocol [`ED-09-5-Envelope protocol Track A`](../experiements/ED-09-5-Envelope_InProcess/protocol.md)** |
| **ED-09.5 envelope (FRAP-side)** | **Public FRAP recovery curves (cell-biology literature)** | **Lomb-Scargle on residual at 80–800 Hz** | ⏳ self-contained reanalysis available; no external dependencies | **[`ED-09-5-Envelope protocol Track B`](../experiements/ED-09-5-Envelope_InProcess/protocol.md)** — the fastest path to a new ED empirical result (1 week, $0) |
| **C7 Nonlinear Triad Coupling** | **5 different systems (simulation + 3 experimental routes)** | **Harmonic-mode sweep — measure `K = A₃/A₁³`, `K₂ = A₂/A₁²`, scaling `α₃`, phase-lock `Δφ`** | ✅ **Simulation companion COMPLETED 2026-04-22**: `K = 0.0148 ± 0.0005`, `K₂ = 0.279`, `α₃ = 3.0`, `Δφ = π` exact. Three experimental routes queued. | **Fifth ED empirical test.** Protocol: [`Triad-Coupling-C7_InProcess/protocol.md`](../experiements/Triad-Coupling-C7_InProcess/protocol.md). Routes: (1) **Top-1 AFM Fourier reanalysis** ($0–500, 1–6 wk, new acquisition required — existing pilot insufficient); (2) **Alt-1 Nonlinear RLC** (~$2–152, 2–3 days, plan at [`RLC_ExecutionPlan_v1.0.md`](../experiements/Triad-Coupling-C7_InProcess/RLC_ExecutionPlan_v1.0.md), uses 2026-04-22 AstroAI kit + anti-parallel 1N4148 diodes); (3) **Alt-2 Patterned FRAP** (~$2000–5000, 4–8 wk, cleanest PME mapping). Simulation: [`analysis/scripts/telegraph_pme/triad_calibration/`](../analysis/scripts/telegraph_pme/triad_calibration/). **Coverage map context:** C7 is the most load-bearing under-tested Canon axiom per [`docs/ED-Test-to-Axiom-Mapping-v1.0.md`](ED-Test-to-Axiom-Mapping-v1.0.md). |
| **Kinematic acoustic metric / P4 extremal horizon** | **Slow-light / EIT atomic medium** | **Within-apparatus differential — monotonic (`κ_M > 0`) vs extremal (`κ_E = 0`) control-field profiles; thermal-emission ratio `R_E / R_M`** | ⏳ **Protocol drafted 2026-04-22**; no collaboration contacted yet; feasibility review by EIT domain expert recommended first. PASS: `R_E / R_M < 0.1`. | **Sixth ED empirical test** (top priority of three-folder acoustic-analogue program). Protocol: [`ED-Acoustic-EIT-Extremal protocol`](../experiements/ED-Acoustic-EIT-Extremal_InProcess/protocol.md). Sibling stubs: [`ED-Acoustic-OpticalPulse`](../experiements/ED-Acoustic-OpticalPulse_InProcess/) (blocked on Belgiorno-2010 noise char.), [`ED-Acoustic-BEC-Extremal`](../experiements/ED-Acoustic-BEC-Extremal_InProcess/) (blocked on moving-background theory extension). Parent memo: [`theory/ED_Acoustic_Analogue_Experimental_Program.md`](../theory/ED_Acoustic_Analogue_Experimental_Program.md). **Honesty caveat:** `κ = 0 at smooth c_s-max` is a shared kinematic prediction with standard analogue gravity; ED-specific content is P4 mobility-collapse natively producing interior-maximum horizons. Collaborators: Lukin / Hau / Halfmann / Lvovsky / LKB-Paris. |

---

## 8. Paper inventory — locations and contents

### On user's Desktop `ED Interpretations/`

| File | Date | Content |
|---|---|---|
| 00.1 Cosmology from the ED Compositional Rule | Feb 2026 | ED cosmology from union rule; inflation, structure, thinning/expansion, horizon-dominated heat death |
| 00.2 The Architectural Canon of the Unified ED Cosmology PDE | Mar 2026 | 7 irreducible principles P1–P7 |
| 00.3 The Unified Cosmological Equation of Event Density | Mar 2026 | Unified PDE with D+H=1, SY2 penalty, D_crit=0.5, ground-state energy αγρ₀, relaxation laws |
| ED-02 Temporal Density and Galactic Curvature | Dec 2025 | Origin paper — speculative DM alternative |
| ED-04 Field-Level Account of Dark Matter | Feb 2026 | Formalization + dwarf SPARC test folded in |
| ED-10 Emergence of Spacetime, Geometry, Information | Feb 2026 | Full emergence manifesto; quantum→relational→classical→geometric continuum |
| ED-I-12 Photonics | Feb 2026 | Gradient architecture and structural control of light. Yablonovitch/Pendry/Capasso reinterpreted as channel removal/inversion/redirection/encoding/composition. Introduces chain/channel/multiplicity vocabulary. |
| ED-I-13 Quantum Information | Feb 2026 | Channel geometry and global participation. Deutsch/Deutsch-Jozsa/BB84/Teleportation/Shor as global-access, constraint-extraction, rewrite-on-measurement, identity-reassignment, symmetry-extraction. |
| ED-I-14 Topological Effects | Feb 2026 | AB/Tonomura/Berry/AC as global invariants of ED-channel curvature. Phase without force = multiply-connected channel with nontrivial curvature. |
| ED-I-27 Weak Lensing | Mar 2026 | Interpretation of Mistele+2024 as ED-channel |
| ED-XX Environment Sourcing of Temporal Tension | **Apr 2026** | **Major revision** — galaxies can't source 3D flat fields; groups/filaments/cosmic web can |
| Temporal Tension in Dwarf Galaxies: A SPARC-Based Test | Feb 2026 | ED-04.5 standalone — the 53% separation result |

### On user's Desktop `ED Important Papers/`

A second Desktop folder distinct from `ED Interpretations/`. **All `.md` contents fully read as of 2026-04-21.** The only remaining unread items are PDFs that duplicate PhilArchive / `ED Interpretations/` content already covered elsewhere (00.1, 00.2, 00.3, ED-13), and the `Protocol_UDMprediction.pdf` / `ED_UDM_MobilityLaw.pdf` which parallel `papers/Universal_Mobility_Law/` in the repo. The `.md` files on Desktop represent Allen's authored canonical copies; several of them predate or update the repo versions.

| File | Content | Read status |
|---|---|---|
| **Scale‑Correspondence in Event Density: Architectural Invariants Across Magnitudes.pdf** | ED-SC-00, the foundational scale-correspondence paper | **✓ read**. See §6.6 |
| **ED_Foundational_Paper.md** (v1) | First-generation Foundational Paper — axiomatic derivation, seven P1–P7 derivation axioms (§3.1), three-channel decomposition | **✓ read**. Absorbed into §3.1 and §5.7 |
| **ED_Foundational_Paper_v2.md** | Expanded Foundational Paper — adds six structural analogues (§5.7) with falsification tests, 3D validation (Appendix G), RLC circuit analogy as exact identity, nonlinear-mobility repulsion discovery | **✓ read**. See §5.7 |
| ED_Foundational_Paper.pdf | PDF render of one of the two versions above | Redundant with .md versions |
| **ED-Dimensional-01_Quantum_Regime.md** | Quantum-regime dimensional mapping with full ED-to-quantum dictionary, Madelung-anchored `D_phys = ℏ/2m`, exact / anchored / candidate classification, superluminal `V_0` flag | **✓ read**. See §5.8 |
| **ED-Dimensional-Master_The_Unified_Atlas.md** | Master 5-regime dimensional atlas. Universal nondimensional invariant `D_phys·T₀/L₀² = 0.3` across Quantum / Planck / Condensed-Matter / Galactic / Cosmological. 61 orders of magnitude. Flags structure-growth problem (monostable penalty cannot generate cosmic structure growth alone) as most fundamental open question | **✓ read**. See §5.8 |
| **ED-Math-01_Uniqueness_Well-Posedness_and_Architectural_Laws.md** | Formal mathematical layer. Theorem 2.1 (uniqueness of canonical PDE given seven derivation axioms). Per-channel well-posedness. Nine architectural laws L1–L9 as consequences of the Canon | **✓ read**. See §5.6 |
| **ED-SIM-3D_Canonical_PDE_2D3D_Extension_and_Invariant_Mini-Atlas.md** | March 2026 2D/3D PDE extension + 5-invariant mini-atlas. Validates axiom P7 (dimensional consistency) across d=1,2,3. Does NOT contain the 3D Green's-function argument underpinning ED-XX — that lives elsewhere | **✓ read**. See §6.7 |
| **ED-Data-01_Condensed_Matter_Mobility_Test.md** | UDM test pipeline design. Predicts `D_eff(c) = D₀(1 - c/c_max)^β` with `R² > 0.95` and `α_R` matching. Candidate materials in priority order: hard-sphere colloids (best anchoring), PEG-water, Li-graphite, sucrose, polymer gels. Anchors what became the repo's Universal Mobility Law 10-material result | **✓ read**. Complements `papers/Universal_Mobility_Law/` |
| **ED-Data-Galaxy-01_First_Halo_Edge_Test.md** | Pre-ED-XX galaxy-halo-edge test. Predicts **finite halo edge `R_edge`** with Barenblatt parabolic-cap profile `ρ ∝ √(1-(r/R_edge)²)`, distinct from NFW/Einasto tails. Data targets: SPARC, Gaia, Dragonfly, weak lensing | **✓ read**. **Pre-ED-XX framing** — after ED-XX (§6), the "no halo edge" prediction replaces the "finite R_edge" prediction (environment-sourced fields are scale-free). Historical value; do not cite as current ED prediction |
| **Appendix_G_3D_Analogues.md** | 3D validation of three of the six 2D structural analogues (Barenblatt, Horizon, Temporal Tension). All structural patterns extend to 3D; numerical parameters shift only through `d`-dependent Laplacian. Validates axiom P7 empirically | **✓ read**. See §5.7 3D validation |
| **WHAT_IS_ED.md** | One-page overview. Uses derivation-axiom P1–P7 (§3.1). Notes constitutive under-specification and invites specific `M(ρ)` / `P(ρ)` choices. Useful as a session-starter for newcomers | **✓ read**. Absorbed into §1 and §3.1 |
| **X5D_Evaluation_EventDensity.md** | Factor Skyline meta-architectural evaluation. ED passes all 6 FS criteria (Minimality, Locality, Determinism, Generative Sufficiency, Envelope Tightness, Structural Optimality). 28 constraints, ~18 independent, 8 parameters, 18→8 overdetermination ratio 2.25. Four channels (M, T, H, V). Five universality classes (PME, RC, Stefan, Telegraph, Void) | **✓ read**. See §6.10 |
| Protocol_UDMprediction.pdf | Experimental protocol for UDM prediction. Parallels `papers/Universal_Mobility_Law/` | Not read — parallel in repo |
| Cosmology from the ED Compositional Rule.pdf | Identical to Desktop/ED Interpretations/00.1 | Already covered in §4 |
| The Architectural Canon of the Unified ED Cosmology PDE.pdf | Identical to Desktop/ED Interpretations/00.2 | Already covered in §3 |
| The Unified Cosmological Equation of Event Density.pdf | Identical to Desktop/ED Interpretations/00.3 | Already covered in §4 |
| Event Density as a Physical Ontology.pdf | Same as PhilArchive PROEDA-13 (ED-13) | Already covered in §5.5 |
| ED_UDM_MobilityLaw.pdf | UDM mobility law paper. Parallels `papers/Universal_Mobility_Law/` | Not read — parallel in repo |

**As of 2026-04-21, Desktop/ED Important Papers/ is fully absorbed.** The remaining unread PDFs are either duplicates of already-covered `.md` / PhilArchive content or parallels of the repo's `papers/Universal_Mobility_Law/`. The ED-Sim-01 Green's-function derivation that underpins the ED-XX environment-sourcing revision (§6) is still unlocated; it is not in this folder. Most likely location: inside the ED-XX paper PDF itself (`ED-XX Environment Sourcing of Temporal Tension.pdf` in `Desktop/ED Interpretations/`), which has not been opened for this specific derivation yet.

### On user's Desktop `ED Archive/`

A broader archive folder. Contents are mostly images, videos, and auxiliary text files — not primary theory documents. Spot-read 2026-04-21:

| File | Content | Relevance |
|---|---|---|
| `ED Repo_Claude Review Prompts.md` | Eight audience-tuned "what is ED?" prompts (core/business-card, newcomer, scientist, skeptic, press, grad-student, "explain it like I'm 15", pocket version) | Use as-is when a future session needs an initial classification prompt from a specific audience perspective |
| `what ED Laws are.txt` | Informal gloss: "A Law in ED-Arch is a geometric truth about the ED manifold that remains invariant under changes in N, angle, radius, drift, time, resolution, and descriptive layer." Laws I–VII = local, VIII = global unification, IX = generative | Complements the formal L1–L9 of §5.6. **Note:** the "Laws I–IX" in this archive text are a distinct, older numbering from the ED-Arch series — do not conflate with ED-Math-01's L1–L9 |
| `ED in one sentence.txt` | "The saddle is the geometry; the gradients are the calculus; the boundaries are the topology; the horizons are the dynamics." | One-sentence summary useful for slide titles / abstracts |
| `ED from the outside readme maybe.txt` | Narrative framing of the ED-Arch-01 → 21 arc: ontology → laws → experiments → predictive manifold → physics-style report | Useful as a "trajectory-summary" when orienting a newcomer; no new physics content |
| `ED-Final_Synthesis_EventDensity_Physics.md` / `.pdf` | Not yet read in detail | If the user references "the final synthesis," this is the reference. Likely a pre-ED-XX integration |
| `ED-Dimensional-01-Ext_v0.4-final.tex` / `.pdf` | Extension of ED-Dimensional-01 with rate-balance across regimes. Already covered in the 2026-04-20 update entry at the top of this doc and in `theory/ED-Dimensional-01-Ext.md` | Active work-in-progress per the 2026-04-20 entry |
| `ED-Simulations/` | Subfolder containing ED-Sim-01 PDF and related simulation material | ED-Sim-01 already covered in §6.8 |
| `13 triad results/`, `14 triad results/`, `15 results/`, `16 results/`, `17 results/`, `18 notebooks a-f/` | ED-Phys-series experiment outputs (triads, participation, architectural invariants) | Data only; theory content is in the corresponding ED-Phys papers |

### On user's Desktop `ED Slide Deck/`

Presentation material (images + draft text). Not primary theory documents. Spot-inventory 2026-04-21:

- Individual slide images: one per ED-05 pre-PDE axiom (A1–A4), one per derivation-axiom P1–P7 (`Locality.PNG`, `Isotropy.PNG`, `GradientFlow.PNG`, `Dissipative.PNG`, `ScalarField.PNG`, `MinimalCoupling.PNG`, `DimensionalConsistency.PNG`), one per Canon P1–P7 (`P1_operator_structure.PNG` through `P7_nonlinear_triad.PNG`), plus channel-isolation diagrams (`Mobility_alone.PNG`, `Penalty_alone.PNG`, `Participation_alone.PNG`, `TriadCoupling.PNG`), universality-class images (`PME_porous_medium.PNG`, `RC_debye.PNG`, `RLC_Oscillator.png`), and scale-correspondence / invariants (`scale correspondence.PNG`, `Universal Invariants.png`, `UDM_universal.PNG`, `CMLag_merger.PNG`).
- `ED Presentations/` subfolder: six draft iterations (`ED_Presentation_Draft.md`, `ED_Presentation_Draft_Openings.md`, `ED_Presentation_Draft_v2.md`, `ED_Presentation_Draft_v3.md`, `ED_Presentation_Draft_v3.5.md`, `ED_Presentation_Draft_v4.md`, `ED_Presentation_Draft_v4.txt`) plus `ED_Atlas_Text_Overlays.md`.

**How to use the slide deck in future sessions:** if the user asks about a specific image (by name), the filename is descriptive enough to identify the intended axiom / principle / concept. The slide images exist **separately** from the `docs/figures/atlas/` PNGs referenced in `project_outreach_atlas.md` (user's auto-memory) — the atlas PNGs are for public lectures and follow different style conventions. Do not bake text into atlas PNGs; slide-deck images have text baked in by design.

### PhilArchive / PhilPeople (URL: `philpeople.org/profiles/allen-proxmire`)

**Full inventory rebuilt 2026-04-21 (late)** from the PhilArchive `s/allen+proxmire` search. 24 publications in attribution order. Column 1 lists the paper's informal ID in this doc's trajectory table (§2).

| ID / Label | Paper title | Content summary |
|---|---|---|
| **ED-01** | **Event Density and the Architecture of the Universe** | **Founding paper.** "The universe is made of activity before it is made of things." Four primitives + compositional rule before any physical application. Pre-dates ED-02. **Added to orientation 2026-04-21.** |
| ED-02 | Event Density and Galactic Curvature: A Speculative Alternative to Dark Matter | Dec 2025. Origin physical application — speculative DM alternative, nine qualitative predictions. ✓ read. |
| ED-03 | Extensions of Event Density: Structural Consequences Across Physics | Feb 2026. Cross-domain overview (gravitation / quantum / info / cosmology). ✓ read. |
| ED-04 | Event Density and Temporal Tension: A Field-Level Account of Dark Matter | Feb 2026. Formalization + dwarf SPARC test folded in. ✓ read. |
| ED-04.5 | Temporal Tension in Dwarf Galaxies: A SPARC-Based Test | Feb 2026. N = 46 SPARC, ⟨D_outer⟩_Active = 6.01 vs. Quiet = 3.94, 53% separation. ✓ read. |
| ED-05 | Event Density: A Mathematical Formalization | Feb 2026. Four pre-PDE axioms on bare event domain. Pre-PDE layer. ✓ read. |
| ED-06 | Horizons as Event Density Decoupling Surfaces | Feb 2026. All horizons as ED field discontinuities. BH / Rindler / cosmological unified. ✓ read. |
| ED-07 | Event Density and Relativistic Phenomena | Feb 2026. `c` as max causal-update rate; Lorentz symmetry emergent. ✓ read. |
| ED-08 | Event Density and Cosmological Structure: Temporal Tension and Expansion | Feb 2026. Expansion, redshift, acceleration, inflation as ED-gradient phenomena. ✓ read. |
| ED-09 | Event Density and Quantum Behavior: Participation, Discreteness, and Relational Becoming | Feb 2026. Superposition = coexisting channels, entanglement = shared bandwidth, measurement = structural commitment. ✓ read. |
| ED-09.5 | Event Density and the Quantum-Classical Boundary | Feb 2026. Sharp ED transition as potentially-testable novel prediction. ✓ read. |
| ED-10 | Event Density and the Emergence of Spacetime: Geometry, Information, and Temporal Asymmetry | Feb 2026. Spacetime, geometry, information, arrow-of-time as emergent. Most ambitious paper. ✓ read. |
| **ED-Phys** | **Event Density and the Architecture of Physical Law: Symmetry, Constraint, and Emergent Regularity** | **Laws, symmetries, conservation quantities as emergent architectural consequences, not fundamental postulates.** The meta-claim behind all three ED tracks. **Added 2026-04-21. See §5.9.** |
| ED-13 | Event Density as a Physical Ontology: From Primitives to Dynamics to Empirical Predictions | March 2026. Master synthesis. Four primitives + seven axioms → unique equation. Two sharp predictions (activity-dependent WL + merger-lag). ✓ read. |
| **(untitled ID)** | **Event Density: Open Note for Experiments** | **Falsifiable-test catalogue across all five regimes.** Outward-facing invitation to experimentalists. Overlaps with `outreach/ED_Falsifiable_Prediction.md`. **Added 2026-04-21.** |
| 00.1 | Cosmology from the Event Density Compositional Rule | Feb 2026. ED cosmology from union rule — inflation, structure, thinning/expansion, heat death. ✓ read. |
| 00.2 | The Architectural Canon of the Unified Event Density Cosmology PDE | March 2026. Seven irreducible principles P1–P7 of the Architectural Canon (see §3). ✓ read. |
| 00.3 | The Unified Cosmological Equation of Event Density | March 2026. Unified PDE with `D + H = 1`, SY2 penalty, `D_crit = 0.5`, ground-state energy `αγρ₀` (see §4). ✓ read. |
| (undated) | Universal Degenerate-Mobility Scaling in Crowded Soft Matter | **UDM publication.** 10-material soft-matter empirical fit, `R² > 0.986`. Authoritative version of the repo's `papers/Universal_Mobility_Law/` result. ✓ read (via repo parallel). |
| (undated) | Temporal Tension and Merger Lag in Galaxy Clusters: A Prediction from Event Density | **Cluster Merger-Lag publication.** 7 clusters + Finner aggregate, `ℓ = D_T / v_current`. Authoritative version of the repo's `papers/Cluster_Merger_Lag_Evidence/`. ✓ read (via repo parallel). |
| (Dec 2025) | Regulated Multiplicity: An Architectural Account of Consciousness and Subjectivity | Philosophy of mind. **Separate thread from the physics program — no ED physics content.** ✓ confirmed. |
| (Jan 2026) | Regulated Multiplicity: An AI Systems Architecture for Robust, Self-Correcting Models | AI architecture pattern. **Separate thread — no ED physics content.** ✓ confirmed. |
| **FS-01** | **The Factor Skyline: A 2-Dimensional View of the Number Line** | **Pure number theory, not physics.** 2D view of primes on the number line. See §12. |
| **FS-02** | **The Factor Skyline: A Unified Architecture for Multiplicative Number Theory** | **Pure number theory, not physics.** "Primes are the deterministic escape points of a geometric coverage process generated by the least prime factor." See §12. |

**Summary of additions in 2026-04-21 (late) PhilArchive sweep:**
- **ED-01** (Architecture of the Universe) — the true founding paper, pre-ED-02
- **ED-Phys** (Architecture of Physical Law) — meta-claim paper, absorbed into §5.9
- **Open Note for Experiments** — falsifiable-test catalogue
- **Two Factor Skyline papers** — non-physics thread, documented in §12 for completeness

All three ED physics additions (ED-01, ED-Phys, Open Note) have been absorbed into the body of this document. No further PhilArchive reading is required for the physics program. Future Allen publications should be added to §2 trajectory and §8 inventory as they appear.

### GitHub — `github.com/allen-proxmire/emergence-universe`

**Added 2026-04-21 (late).** Public repository for the Emergence-Universe / ED-SIM sandbox. See §11 for full treatment.

| Path | Content | Relevance |
|:---|:---|:---|
| `README.md` | Project overview — "laws are the invariants forced by architecture and constraint." Three project-level takeaways (math's unreasonable effectiveness explained, complexity does not require randomness, architecture-first ontology) | Session-start reference for the sandbox thesis |
| `ED-SIM-Code/ED_Update_Rule.py` | **Canonical Scenario-D 2D-lattice solver.** Implements `∂p/∂t = β·∇²p − α·p^γ` derived from ED-05.5 compositional rule. Mobility-weighted variant `M(ρ) = ((ρ_max − ρ)/ρ_max)^n` reproduces the saturation (black-hole) regime. Supports Langevin noise for Scenario D. | **Same file referenced by §6.9 ED-SC 2.0** as the reference Scenario-D implementation (path `C:/Users/allen/GitHub/Emergence Universe/ED-SIM-Code/` locally) |
| `ED-SIM-Code/event_update.py` | N-particle ring sandbox update rule (separate from the lattice solver) | Drives the 14 ED-Arch laws' empirical sweeps |
| `ED-SIM-Code/check_*.py` | Per-law verification scripts | Reproducibility of Laws I–XIV |
| `ED-SIM-Papers/00 ED-Arch Foundations/` | ED-Arch-00 Architectural Framework + ED-Arch-00 Micro-Event Operator | Foundational definitions of the micro-event operator |
| `ED-SIM-Papers/01-19 ED-Arch Developmental/` | ED-Arch-01 through ED-Arch-19, plus ED-Arch-12.5 (Cosmology from Compositional Rule) and ED-SC-00 (Scale-Correspondence) | Development of saddles, channels, boundaries, horizons in the sandbox |
| `ED-SIM-Papers/20-29 ED-Arch Laws/` | ED-Arch-20 through ED-Arch-35 — **the 14 laws** + manifold unification + compositionality | **Laws I–XIV** — see §11.4. Most are `.txt` notes; verbatim text can be fetched via raw GitHub URLs |
| `Reproduce_This_Paper/` | Scripts + instructions for regenerating figures / sweeps / law surfaces | Reproducibility track |
| `ED-SIM_TakeAways_Emergence_Constraint_Physical_Law.pdf` | Consolidated takeaways | Summary document |
| `Explainers_On_YT.txt` | Links to YouTube explainers | Outreach |

**Do not confuse with:** the `edsim/` directory in the Event-Density repo (this repo), which is the continuum PDE solver package for the canonical ED PDE. The two are different projects that share vocabulary. See §11.1 for disambiguation.

---

## 9. Re-acclimatization checklist for a new session

In priority order:

1. **Read this document in full.** (~20 min)
2. **Skim `theory/PDE.md` and `theory/README.md`** — repo's current canonical PDE statement. Note the discrepancies with 00.3 flagged in §1.
3. **Skim `RESULTS.md`** — repo-level summary of empirical confirmations.
4. **Skim `papers/ED-BTFR-Activity/memo.md` and `papers/ED-Finner/ED-Finner-A1.md`** — most recent session work. The BTFR memo has an addendum at the top acknowledging the ED-XX revision.
5. **Know the ED-XX update** — §6 of this doc. If the user's question touches galaxy-scale dynamics, rotation curves, dwarf galaxies, or BTFR, the environment-sourcing revision is probably relevant.
6. **Know the ED-SIM-3D result** — §6.7. If the user asks about dimensional consistency, axiom P7, the 5-invariant atlas, Barenblatt scaling, or the simulation engine itself, this is where. **Do not conflate ED-SIM-3D with the ED-Sim-01 Green's-function programme** — they are separate documents with different purposes.
7. **Check which empirical tests are open** — §7.

### Question-type → section map

| If the user asks about… | Jump to |
|---|---|
| PDE form, canonical structure, SY2 vs linear penalty, D+H=1 vs dimensional D | §3 Architectural Canon, §4 Unified PDE, §1 Discrepancies |
| Spacetime emergence, arrow of time, locality, measurement, entanglement, BH info paradox | §5 ED-10 Emergence Map |
| Pre-PDE math foundations, axioms, measure-theoretic structure | §5.5 ED-05 |
| Horizons (black hole / Rindler / cosmological), Hawking/Unruh, decoupling surfaces | §5.5 ED-06, §5 ED-10 dictionary |
| Relativity, speed of light, Lorentz invariance, geodesics, time dilation | §5.5 ED-07 |
| Cosmological expansion, redshift, acceleration, dark energy, inflation, structure formation | §5.5 ED-08, §4 00.3 canon, §6 environmental sourcing |
| Quantum behavior emergence, superposition, decoherence, quantum-classical transition | §5.5 ED-09 + ED-09.5 **(ED-09.5 has a potentially-testable sharp-transition prediction)** |
| Photonics (bandgaps, metamaterials, cloaking, metasurfaces) | §6.5 ED-I-12 |
| Quantum computing / quantum information (Deutsch, BB84, teleportation, Shor) | §6.5 ED-I-13 |
| Topological phases (Aharonov-Bohm, Berry, AC, Tonomura) | §6.5 ED-I-14 |
| Weak lensing, flat velocities to 1 Mpc, BTFR, galaxy-scale DM | §5.5 ED-13 + §6 ED-XX + `papers/Cluster_Merger_Lag_Evidence/` |
| Merger-lag, cluster offset, `ℓ = D_T / v_current`, scale dependence | `papers/Cluster_Merger_Lag_Evidence/`, `papers/ED-Finner/`, §5.5 ED-13 |
| UDM, soft-matter mobility, diffusion near saturation | `papers/Universal_Mobility_Law/`, §5.5 ED-13, + [`UDM_Extension_Log`](../experiements/Universal_Mobility_Law_Evidence/UDM_Extension_Log.md) — running log of post-publication material additions (#11 Roosen-Runge BSA added 2026-04-22) + candidates + exclusions + fitting framework |
| Consciousness, subjectivity, hard problem, AI architecture | **Regulated Multiplicity thread — separate from physics program. Not covered here.** |
| "Chain," "multiplicity," "participation rule," "identity alignment," "rewrite-on-measurement" | Definitions in §6.5 table. |
| "Pocket," "channel," "saddle," "divergence zone," "stationary point," "threshold" | ED-SC vocabulary. Definitions in §6.6 table. These are the *architectural form* primitives (distinct from the ED-I chain/multiplicity primitives). |
| "Scale-correspondence," "architectural invariant," "ED-SC," cross-scale identity | §6.6 — the Scale-Correspondence program. Includes Table 1 mapping 22 micro↔cosmological correspondences. |
| Potential connection between a quantum/optical phenomenon and a galactic/cosmological one | **Check Table 1 in §6.6 first.** ED-SC explicitly documents these. Berry phase / AB / AC → topologically protected filaments and void walls (row 014). Photonics → photon-like curvature packets through void/filament geometry (row 012/018). Quantum information → cosmic web as curvature-encoded information processing (row 013). |
| "Four primitives and seven axioms" | ED-13 composition of ED-05 (4 pre-PDE axioms) with 00.2 Canon (7 PDE principles). See §5.5 ED-13 and §3. **But first, see §3.1** — "seven axioms" may refer to the derivation axioms of ED-Math-01 OR the Canon of 00.2 (two different sets). Disambiguate before answering. |
| "P1 through P7" (any citation) | **§3.1 two-axiom-set disambiguation.** Two different P1–P7 sets exist: derivation axioms (Foundational Paper / ED-Math-01: Locality, Isotropy, Gradient-driven flow, Dissipative structure, Single scalar field, Minimal coupling, Dimensional consistency) vs. Architectural Canon (00.2: Operator Structure, Channel Complementarity, Penalty Equilibrium, Mobility Capacity Bound, Participation Feedback Loop, Damping Discriminant, Nonlinear Triad Coupling). No overlapping labels, so the surrounding text reveals which set is meant. |
| "ED is unique" / "uniqueness of the ED PDE" / Theorem 2.1 / derivation from axioms | §5.6 ED-Math-01. Theorem 2.1: the canonical ED PDE is the unique second-order scalar PDE satisfying the seven derivation axioms (§3.1). Proof by constructive elimination. |
| "Nine architectural laws" / L1–L9 / Lyapunov structure / horizon formation law / morphological hierarchy | §5.6. L1 (unique attractor) ↔ P3; L7 (horizon formation) ↔ P4; L9 (sheet–filament oscillation) ↔ P5+P6. These are theorems about Canon-compliant PDEs, not additional axioms. |
| "Six structural analogues" / structural test of ED / channel-by-channel physical-law match | §5.7 Foundational Paper v2. Six analogues: RC (0.00%), Barenblatt (1.1%), Stefan horizons (2.5%), oscillatory-horizon negative result, telegraph-modulated PME (0.03% v–δ match), emergent nonlinear-mobility repulsion. 3D validation in Appendix G: all three re-tested analogues extend without modification; only numerical parameters shift per `d`-dependent Laplacian. **First in-repo visualization + solver-independence validation of Analogue 5 (telegraph-modulated PME) locked 2026-04-21 at [`analysis/scripts/telegraph_pme/`](../analysis/scripts/telegraph_pme/). Four locked versions:** v1.0 linear-regime canonical; v1.1 nonlinear attempt; v1.2 H-sweep; **v1.3 solver-independence test** using spectral ETDRK2 + MOL-BDF in parallel — [`figure`](../analysis/scripts/telegraph_pme/figures_canonical/Analogue5_SolverIndependence_v1.3.png). **Scenario A CONFIRMED:** across 9 reliable runs spanning two independent solvers and two amplitudes at H ∈ {10, 20, 50}, measured ω/ω_linear = 1.01 ± 0.04. **The FPv2 §8.4 54% renormalization is not reproduced by any independent solver and is solver-specific, not a physical property of the ED PDE.** The linear eigenmode prediction `ω = √((DP₀ζ + HP₀)/τ − γ²)` is now verified under three independent numerical methods (explicit Euler + Neumann, spectral ETDRK2 + periodic, MOL-BDF + periodic). Recommendation: FPv2 §8.4 quantitative claim should be retracted or reframed. See `analysis/scripts/telegraph_pme/README.md` for the full index and `v1.3_solver_independence/memo.md` for the detailed analysis. **Architectural follow-through** (FPv2 §8.4 drop-in correction + publication-ready summary paragraphs) at [`v1.3_solver_independence/architectural_followthrough.md`](../analysis/scripts/telegraph_pme/v1.3_solver_independence/architectural_followthrough.md). |
| **"Does Analogue 5 predict a 54% frequency renormalization?"** / FPv2 §8.4 quantitative claim / is the 0.54 factor real? | **No — it's a code bug, diagnosed at line-level 2026-04-22.** Under three independent solvers (v1.3) the measured ω matches the linear eigenmode prediction `ω = √((DP₀ζ + HP₀)/τ − γ²)` to within 4%. **The root cause is line 162 of `edsim/phys/analogues/telegraph_pme.py`** — `F_avg = spatial_average(params.D * F_local, dx)` inserts a spurious factor of `D` into the participation ODE's forcing, shifting the off-diagonal coupling from `P₀/τ` (paper spec) to `DP₀/τ` (implemented). The resulting eigenmode `ω_coded = √(DP₀(H+ζ)/τ − γ²)` matches all three FPv2 table values (0.1662, 0.2400, 0.3842) to 4-sig-fig precision. Patch: remove `params.D *`. **One-character fix restores `ω_measured ≈ ω_linear`.** The v–δ frequency-match claim and all Analogue-5 qualitative structure survive; only the specific 54% quantitative number is retracted. See [`v1.3 solver-independence test`](../analysis/scripts/telegraph_pme/v1.3_solver_independence/) (general solver-independence evidence) and [`v1.4 bug diagnosis`](../analysis/scripts/telegraph_pme/v1.4_bug_diagnosis/) (line-level root cause). Drop-in FPv2 §8.4 correction block at [`architectural_followthrough.md`](../analysis/scripts/telegraph_pme/v1.3_solver_independence/architectural_followthrough.md) §Part 2 (updated 2026-04-22). |
| "Quantum regime" / `D_phys = ℏ/2m` / Madelung theorem / Compton length anchoring / superluminal `V_0` | §5.8 ED-Dimensional-01. `L_0 = ℏ/(mc)`, `T_0 = 0.6·ℏ/(mc²)`, `D_phys = ℏ/(2m)` (Madelung — a theorem, not an analogy). `V_0 = c/(2·D_nd) = 1.667c` is a scale conversion factor, not a signal speed (same property as the Schrödinger equation). Density-dependent mobility `M(ρ) = M_0(1-ρ̂)^β` is ED's distinguishing beyond-QM prediction. |
| "Universal nondimensional invariant" / `D_phys · T_0 / L_0² = 0.3` / cross-regime scaling / 61 orders of magnitude | §5.8. The invariant holds across Quantum / Planck / Condensed-Matter / Galactic / Cosmological regimes to machine precision. Structure-growth at cosmological scale flagged as most fundamental open question (monostable penalty cannot generate cosmic structure growth alone). |
| "Factor Skyline" / X5D / theoretical-minimality / overdetermination ratio / structural optimality | §6.10. ED passes all 6 FS criteria. 28 constraints, ~18 independent, 8 parameters, ratio 2.25 in overdetermined regime. Five universality classes (PME, RC, Stefan, Telegraph, Void). Use when the question is theoretical hygiene, not empirical content. |
| "Halo edge" / finite `R_edge` / Barenblatt parabolic-cap halo profile | Historical prediction of ED-Data-Galaxy-01 (pre-ED-XX framing). **After ED-XX (§6), ED predicts NO halo edge** — environment-sourced fields are scale-free. Do not cite ED-Data-Galaxy-01's `R_edge` as a current ED prediction. |
| "Architecture of Physical Law" / "why are laws what they are?" / symmetries as emergent / conservation quantities as architectural / Noether as emergent / gauge invariance origin | **§5.9.** Allen's *Event Density and the Architecture of Physical Law* paper. Physical laws, symmetries, and conservation quantities are emergent architectural consequences of ED gradients / participation / compositional rule — NOT fundamental postulates. This is the meta-claim behind all three ED tracks (empirical / interpretive / scale-correspondence). When a user asks "why should ED be a candidate theory of everything, not just a DM alternative?" — this is the reference. |
| "ED-01" / "founding paper" / "Architecture of the Universe" / "the universe is made of activity before it is made of things" | ED-01 (pre-ED-02, §2). The true founding paper. Establishes four primitives (events / becoming / event density / finite configurations) and the compositional rule before any physical application. On PhilArchive, not on Desktop under this name. |
| "Open Note for Experiments" / "falsifiable tests" / "ED-5-regime test catalogue" | PhilArchive Open Note (§2, §8). Outward-facing invitation to experimentalists. Overlaps with `outreach/ED_Falsifiable_Prediction.md`. Use when a user asks "what would it take to falsify ED" or "what experiments are called out across all regimes." |
| "Emergence Universe" / "ED-SIM sandbox" / `github.com/allen-proxmire/emergence-universe` / "architecture-first" / "laws are emergent invariants" / 14 laws of ED-Arch | **§11.** Pre-ED deterministic particle sandbox. Separate from `edsim/` in this repo (§11.1 disambiguation). 14 laws I–XIV including Generative Closure (exactly 10 sub-mechanism types). Contains the canonical Scenario-D implementation referenced by §6.9. |
| "14 laws" / "Laws I through XIV" / "Generative Closure" / "lambda invariant" / "10 sub-mechanism types" / "ED-Arch Law VIII / IX / XIII / XIV" | §11.4 — the sandbox laws (discrete particle universe). **Distinct from the L1–L9 of §5.6** (continuum PDE). Law IX establishes `λ(N)` as the single control parameter. Law XIII is the closure theorem. Law XIV gives the grid-dependent power-law exponent. |
| "Collapse time" / "`χ ~ λ^p`" / "power-law exponent −7/3 or −2.81" / "temporal hierarchy" | §11.4 Law XIV. Grid-dependent exponent — not a universal constant. `p = −7/3` on canonical grid (R² = 0.978), `p = −2.81` on extended grid (R² = 0.96). Temporal hierarchy `χ_folded >> χ_resonant >> χ_planar` spans 3+ orders of magnitude. |
| "Which simulation — ED-SIM-02, ED-SIM-3D, or Emergence-Universe sandbox?" | **§11.1 disambiguation.** ED-SIM-02/3D = continuum PDE solver (paper at Desktop, package = `edsim/`). Emergence-Universe sandbox = particle-based testbed at `github.com/allen-proxmire/emergence-universe`. They share vocabulary but run different code. Always ask for clarification if a user says "ED-SIM" without qualification. |
| "Factor Skyline" (as a theory of number line / primes / factorisation) | **§12.** Allen's non-physics thread — two PhilArchive papers on multiplicative number theory. Primes as deterministic escape points of a geometric coverage process. **Different from** the X5D Evaluation of ED (§6.10), which is a theory-evaluation meta-framework of the same name. |
| "Scenario D canonical code" / `ED_Update_Rule.py` / where is the Scenario-D solver | **Both:** §6.9 references it as `C:/Users/allen/GitHub/Emergence Universe/ED-SIM-Code/`. §11.3 notes this is the same file as `emergence-universe/ED-SIM-Code/ED_Update_Rule.py` on GitHub. Mobility-weighted 2D-lattice gradient-flow solver of the ED-05.5 compositional rule. |
| "Three predictive experiments" / "four predictive tests" / "five predictive tests" / operational protocols / which channel does each test exercise | **Five tests across three tracks (as of 2026-04-22):** (1) AFM dewetting [`AFM-Dewetting protocol`](../experiements/AFM-Dewetting-ED-SC_InProcess/protocol.md) — architectural invariance / cross-scale; (2) UDM-FRAP [`FRAP-High-BSA protocol`](../experiements/FRAP-High-BSA_InProcess/protocol.md) — mobility channel via R(t)~t^(1/6); (3) ED-09.5 Track A [`ED-09-5-Envelope protocol`](../experiements/ED-09-5-Envelope_InProcess/protocol.md) — participation channel via Aspelmeyer optomechanics `x(t)` envelope; (4) ED-09.5 Track B — participation channel via Lomb-Scargle on public FRAP residual at 80–800 Hz; (5) **C7 Triad Coupling [`Triad-Coupling-C7_InProcess/protocol.md`](../experiements/Triad-Coupling-C7_InProcess/protocol.md) — cubic operator nonlinearity via `K = A₃/A₁³ ≈ 0.015`**, added 2026-04-22 after Test-to-Axiom Mapping Project identified C7 as most load-bearing under-tested axiom. Each test has a session-ready protocol with pre-registered parameters and decision tree. §7 empirical-status table summarises all five. |
| **"C7" / "triad coupling" / "K = A₃/A₁³" / "third-harmonic generation" / "k=3 from k=1" / "nonlinear triad" / "`M′|∇ρ|²` signature" / "why does ED predict third harmonic"** | **§3 Canon P7 row + [`experiements/Triad-Coupling-C7_InProcess/protocol.md`](../experiements/Triad-Coupling-C7_InProcess/protocol.md).** Simulation-calibrated invariants (2026-04-22): `K = A₃/A₁³ ≈ 0.0148 ± 0.0005` (scale-free); companion `K₂ = A₂/A₁² ≈ 0.279`; scaling slope `α₃ = 3.0 ± 0.05` across 3 decades of drive amplitude; exact phase lock `φ₃ − 3φ₁ = π` (SD ~ 10⁻⁶ rad); clean regime `A₂ > A₃` by ~200×. Calibration memo: [`analysis/scripts/telegraph_pme/triad_calibration/memo.md`](../analysis/scripts/telegraph_pme/triad_calibration/memo.md). **Historical `A₃/A₁ ∈ [0.02, 0.08]` band is retired as primary criterion** — it is a saturation-regime (`A₁ ≳ 0.15·ρ_max`) measurement, not a scale-free invariant. Three experimental routes at protocol §3: Top-1 AFM Fourier reanalysis, Alt-1 nonlinear RLC ([`RLC_ExecutionPlan_v1.0.md`](../experiements/Triad-Coupling-C7_InProcess/RLC_ExecutionPlan_v1.0.md)), Alt-2 patterned FRAP. |
| **"test-to-axiom mapping" / "which axioms are covered by which tests" / "coverage matrix" / "under-tested axioms" / "gap analysis"** | **[`docs/ED-Test-to-Axiom-Mapping-v1.0.md`](ED-Test-to-Axiom-Mapping-v1.0.md).** 18×5 coverage matrix (A1–A4 pre-PDE + D1–D7 derivation + C1–C7 Canon × T1 AFM, T2 UDM-FRAP, T3a/T3b ED-09.5, T4 RLC). **Layer summary:** Pre-PDE 0 direct / 5 indirect / 15 none; Derivation 4 / 26 / 5; Canon 10 / 13 / 12. **Most load-bearing under-tested axiom: C7 Nonlinear Triad Coupling** (0 direct, 4 indirect, 1 none) — drove the 2026-04-22 C7 experimental protocol. Runner-up C3 Penalty Equilibrium (0 direct, 4 indirect). Pre-PDE layer is structurally untested (bare event domain below PDE-level tests, expected). |
| **"why is `A₂ > A₃` in clean regime" / "symmetry of `|∇ρ|²`" / "does the operator produce a second harmonic" / "odd-symmetry claim for triad"** | **Correction 2026-04-22.** `|∇ρ|²` has a DC + cos(2kx) structure that directly sources the second harmonic; the "A₂ < A₃ by odd symmetry" claim in early drafts of the C7 protocol was **inverted**. Simulation shows `K₂ = A₂/A₁² ≈ 0.279` vs `K = A₃/A₁³ ≈ 0.015`, so at A₁=0.1, A₂ ≈ 200·A₃. The odd-symmetry argument applies to the *phase lock* (`φ₃ − 3φ₁ = π`) not to the amplitude ordering. Canon P7 row in §3 updated accordingly. |
| **"ED-Phys-16 3–6% band" / "why doesn't my measurement match the 3–6% claim" / "is the 3–6% a prediction"** | The ED-Phys-16 "coupling ~0.03 and harmonic 3–6%" is a **saturation-regime measurement**, not a scale-free prediction. Per 2026-04-22 simulation calibration, `A₃/A₁` enters that band only at `A₁ ≳ 0.15·ρ_max` where the mobility bound is approached; in the clean regime (A₁ < 0.1·ρ_max) `A₃/A₁` scales as `A₁²` and is much smaller. Use `K = A₃/A₁³ ≈ 0.015` as the invariant. |
| FRAP protocol / Creative Proteomics / BSA-FITC concentrations / UDM test / R(t) exponent 0.16 vs 0.5 | **[`FRAP-High-BSA protocol`](../experiements/FRAP-High-BSA_InProcess/protocol.md)** — captures the CP-submitted protocol verbatim (§4–§8), adds ED derivation of `α_R = 1/6 ≈ 0.167` from 2D Barenblatt PME with canonical β=2 (§2), analysis pipeline (§9), decision tree (§10), and V2 review notes (§13). Sent to CP 2026-04-17; decision window 2026-04-24 to 2026-05-01. Tests **mobility** channel, not participation (label corrected in §7 table 2026-04-21). |
| ED-09.5 envelope at `ω_v = 8·γ_dec` / Aspelmeyer reanalysis / Lomb-Scargle on FRAP residual / sharp quantum-classical bifurcation / participation-channel test | **[`ED-09-5-Envelope protocol`](../experiements/ED-09-5-Envelope_InProcess/protocol.md)** — two tracks: Track A (Aspelmeyer optomechanics raw `x(t)`, blocked on email) and Track B (self-contained public FRAP reanalysis, 1 week to result). Both implement the §15(β) derivation from Observable-Sharpening memo. §2 pre-registered parameters, §5 and §9 decision trees (F0–F5 falsification criteria). Track B is the fastest path to a new ED result. |
| Sharp bleach boundary vs Gaussian blur (FRAP) | Secondary signature of ED mobility channel — compact support property of the PME. [`FRAP-High-BSA protocol`](../experiements/FRAP-High-BSA_InProcess/protocol.md) §9.2 AIC test between PME parabolic-cap profile and Fickian erf() profile. If PME wins at concentrations ≥ 250 mg/mL, independent confirmation beyond the exponent fit. |
| `ω_v = 2π·N_osc·γ_dec` / envelope frequency derivation / N_osc convention | [`ED-09-5-Observable-Sharpening.md`](ED-09-5-Observable-Sharpening.md) §15 derivation. `N_osc = 8` (full cycles, single-mode clean) per ED-Phys-17 algorithm + ED-Phys-19 derivation cross-check. `τ_v = 1/γ_dec` ansatz in good-cavity limit κ ≫ γ_dec. Operational use: [`ED-09-5-Envelope protocol`](../experiements/ED-09-5-Envelope_InProcess/protocol.md). |
| ED-SC architectural invariance / `κ∥/κ⊥ ≈ −1.3` / cross-scale invariant / motif-conditioned median | **§6.9 ED-SC 2.0.** Canonical form: `med(ℛ_motif(E)) ≈ −1.30` on real-space 2D density fields. Filter params `α = 0.25, L_ray = 2, δ = 0.10`. Reference: Scenario D gives `−1.304`. Full statement: [docs/ED-SC-2.0.md](ED-SC-2.0.md). Supersedes ED-Arch-01 §5 and ED-Arch-02 §3 as cross-scale-invariance references. |
| `H_param` vs `H_field` / parameter-space vs field-space Hessian / which Hessian is ED-SC about | §6.9. ED-SC 2.0 resolves this: the invariant is the field-space Hessian `∇²E`, motif-conditioned median. ED-Arch-01's `−1.3` is the parameter-space Hessian of `f(n,σ)`; the field-space motif-conditioned median happens to equal `−1.304`. Whether this is structural or coincidental is open. See [docs/ED-SC-Hessian-Resolution.md](ED-SC-Hessian-Resolution.md). |
| Valid ED-SC 2.0 comparison systems / which systems can be cross-scale tested | §6.9 + ED-SC-2.0.md §5. Valid: Local Group projected density, Casimir lateral potential, thin-film dewetting `h(x,y)`, stripe-domain order parameter, gradient-form RD activator. Invalid: k-space band saddles, Lagrange-point potentials, OSCER strain-rate tensors, minimal surfaces, crack-tip stress fields. |
| Reference measurement / `r* = −1.304` / Scenario D calibration / canonical Scenario D params | §6.9 Reference Measurement table. Canonical Scenario D uses `α=0.03, γ=0.5, dt=0.05, size=64, seed=77, mobility-weighted, IC=uniform[0.3,0.7]`. In ED-Arch-01 the symbol `n` is the **mobility exponent** (exponent in `M(p)`), NOT a Laplacian coefficient. Code: `analysis/scripts/ed_arch_r2/r2_canonical.py`. |
| "ED-Sim-01" / "ED-Arch-01" / "Scenario D" / architectural invariants / saddle-channel-boundary-horizon geometry / 4×4 (n,σ) sweep / saddle peak at step 457 | §6.8 — the March 2026 architectural-invariants paper (same paper, two labels). Four ED-Arch regimes. Empirical validation of scale-correspondence via κ_∥/κ_⊥ ≈ −1.3. **Does NOT contain the 1/r dilution argument.** Note: three distinct "Scenario D"s coexist in the ED program (ED-SIM v1 full-atlas, ED-Phys-35 D2D, ED-Arch-01 architectural-invariants) — disambiguate before answering. |
| "ED-Arch-02" / Hessian formalism for ED architecture / formal saddle/channel/boundary/horizon conditions | §6.8 — theoretical counterpart to ED-Arch-01. Mathematical criteria: saddle = orthogonal gradient sign-flip; boundary = `λ_⊥ > 0`; horizon = `λ_⊥ < 0`; channel = alignment condition. |
| 1/r dilution argument, 3D Green's-function derivation for ED-XX, T(r) ∝ (1/r)·exp(−r/ℓ_T) | **Source document not located.** NOT ED-SIM-3D (§6.7), NOT ED-Sim-01 / ED-Arch-01 (§6.8), NOT ED-Arch-02 (§6.8). Likely inside the ED-XX paper PDF itself. If the user references it, ask where the derivation lives or quote it from the ED-XX numerical scan table directly (§6). |
| "ED-SIM-3D," dimensional consistency, d=1/2/3 invariants, axiom P7 validation, cross-dimensional scaling table | §6.7 — the March 2026 mini-atlas. 5 invariant tests. Penalty + participation channels dimension-independent to machine precision; mobility channel dimension-dependent per `α_R = 1/(d(m−1)+2)`. |
| "ED-SIM-02," Python simulation engine, solver package, Hessian morphology (blobs/filaments/sheets) | §6.7 — referenced software package. Supports d=1,2,3,4, Neumann/Dirichlet/periodic BCs, implicit Euler + ETD-RK4 (2D only so far). Repo's `edsim/` is likely the same or adjacent package. |
| "Regime" / regimes / regime transitions | **Disambiguate first.** Two taxonomies: (a) 00.3 damping regimes (oscillatory / hybrid / parabolic, D_crit=0.5) — temporal; (b) ED-Arch regimes (hyper-coherent / stable-coherent / marginal / non-individuating) — spatial-architectural in (n, σ). See §4 vs §6.8. |
| Saddles, channels, boundaries, horizons as formal objects (not just vocabulary) | §6.8 ED-Arch-02 — Hessian-based mathematical definitions. Also §6.6 ED-SC for scale-invariant vocabulary treatment. These are the same motifs viewed from different angles. |

### What's ED saying about X? (quick reference)

- **Dark matter:** not needed. Activity-driven temporal-tension field sourced by the cosmic web (groups/filaments) produces flat rotation curves, extended weak-lensing signal, and BTFR via the participation channel.
- **Dark energy:** not needed. Accelerated expansion = steepening of ED gradients over cosmic time (ED-08, 00.1).
- **Inflation:** not needed. Gradient-penalty-dominated early regime produces exponential smoothing without a scalar field (00.1).
- **Singularities:** artifacts of the manifold approximation, not physical (ED-10 §9.4).
- **Black hole information:** no paradox. The network splits into disconnected regions at the horizon; nothing "falls into" anything (ED-06, ED-10 §8.5).
- **Measurement / wavefunction collapse:** structural commitment of a minimal channel to a single stable participation pathway. Not dynamical (ED-09, ED-10 §10.2).
- **Arrow of time:** ontological, not statistical. Commitment is irreversible by construction (ED-10 §6).

---

## 10. Canonical corrections / pointers for future repo work

If a future session is asked to update repo documentation to reflect current thinking:

- `theory/PDE.md` — update to flag the SY2 canonical form (or at minimum add a note that the linear form is a near-equilibrium simplification).
- `theory/PDE.md` — note the D-dimensional vs. D-channel-weight duality.
- `papers/Dimensional_Atlas/regimes/ED-Dimensional-04_Galactic_Regime.md` — add an annotation or footnote about the ED-XX environment-sourcing revision. The current doc is written under the galaxy-sourced hypothesis.
- `data/ED-Data-12-Galactic-Activity/README.md` through `ED-Data-17-z0MGS-Names/README.md` — already received a revised "Verdict (2026-04-17)" in this session. Post-ED-XX, those verdicts should be further annotated to note that the correct activity variable is environmental, not individual-galaxy.
- `data/ED-Data-18-BIG-SPARC/README.md` — when BIG-SPARC releases, the analysis plan should include group/filament cross-match, not just individual-galaxy SFR.
- Consider adding to the repo: a short `theory/Architectural_Canon.md` capturing P1–P7, referenced from `theory/README.md`. Currently Canon content exists only on Desktop.
- **ED-Arch-01 / ED-Arch-02 / ED-Sim-01 papers** should be updated (or a revision memo issued) to cite ED-SC 2.0 as the canonical invariance statement, replacing the ambiguous `κ∥/κ⊥ ≈ −1.3` language in their respective §5 / §3 with a clear reference to the motif-conditioned median form on the field-space Hessian. See `docs/ED-SC-2.0.md` §6 for the reinterpretation that should be adopted.
- Any future paper citing ED-Arch-01's `−1.3` as cross-scale evidence should cite **ED-SC 2.0 §2** with the motif-conditioned median as the object of the claim, not a pointwise per-saddle ratio.
- The Scenario D canonical source code lives at `C:/Users/allen/GitHub/Emergence Universe/ED-SIM-Code/` (specifically `ED_Update_Rule.py`, `Run_Simulation.py`, `Phase2D_Sweep.py`). This is a separate repo from the main Event Density repo and not on GitHub as of session date. Consider mirroring or submoduling if ED-SC 2.0 work continues to depend on it.

---

---

## 11. The Emergence-Universe / ED-SIM sandbox (github.com/allen-proxmire/emergence-universe)

**Added 2026-04-21 (late).** A separate public GitHub repository that predates — and is philosophically foundational to — the Event-Density PDE work documented in the rest of this orientation. This is the **second of two ED simulation efforts** in the program; disambiguation is critical.

### 11.1 Disambiguation: two ED simulation projects

Prior Claude sessions have conflated these. They are different.

| Simulation | Purpose | Domain | What it tests | Repo |
|:---|:---|:---|:---|:---|
| **ED-SIM-02 / ED-SIM-3D** (§6.7) | Continuum PDE solver for the canonical ED equation | 2D / 3D finite-difference lattice of the PDE `∂_t ρ = D·F[ρ] + H·v` | Dimensional consistency of the canonical PDE (axiom P7); the 5 invariant tests (Barenblatt, RC, telegraph, horizon, participation coupling) | `edsim/` in the Event-Density repo; paper at `Desktop/ED Important Papers/ED-SIM-3D_...md` |
| **Emergence Universe / ED-SIM sandbox** | Deterministic event-based minimal universe; testbed for "laws as emergent from architecture" | N-particle ring on a periodic 2D box with discrete merge rule, plus a 2D lattice cosmological-regime solver | The 14 architectural laws (Laws I–XIV) of a minimal universe; Generative Closure (exactly 10 sub-mechanism types) | `github.com/allen-proxmire/emergence-universe` (public), also `C:/Users/allen/GitHub/Emergence Universe/` locally |

**They share vocabulary ("ED-Arch," "Scenario D," "mobility exponent `n`") but run different code on different objects.** When a session encounters "ED-SIM," identify which one from context: if the question is about dimensional atlases, PDE invariants, or the `edsim/` package, it's ED-SIM-02/3D; if the question is about ring-particle collapse mechanisms, lambda invariants, 14 laws, or N-body trajectories, it's the Emergence-Universe sandbox.

**Critical connection — the Scenario-D reference code lives here.** The canonical Scenario-D implementation cited by §6.9 ED-SC 2.0 as `C:/Users/allen/GitHub/Emergence Universe/ED-SIM-Code/ED_Update_Rule.py` is **the same file** as in the Emergence-Universe public repo at `ED-SIM-Code/ED_Update_Rule.py`. So the motif-conditioned-median reference measurement `r* = −1.304` comes from the Emergence-Universe lattice solver, not from the `edsim/` package. The two simulations converge at the 2D-lattice cosmological regime: `ED_Update_Rule.py` implements `∂p/∂t = β·∇²p − α·p^γ` (with mobility-weighted and Langevin variants), derived as the gradient flow of the ED-05.5 cosmological compositional rule.

### 11.2 What the README says (verbatim kernel)

> ED-SIM provides a controlled environment to observe how physical laws are born. It is a sandbox universe for exploring how complex structure emerges from simple event-based rules.
>
> This project demonstrates that many motifs associated with physical law can emerge **without geometry, fields, or particles** — purely from event-density interactions inside a deterministic micro-universe.
>
> Physical laws may be emergent, not fundamental. (…) laws are not "written into" the universe; they are discovered as the inevitable consequences of a system's constraints.
>
> ED-SIM is not a model of our universe. It is a minimal laboratory where the architecture is known, the rules are explicit, and the emergence of law-like behavior can be observed directly.

**The central thesis** (verbatim): *"If a universe has a fixed architecture, then law-like behavior is inevitable."* This is the same meta-claim as §5.9 (Architecture of Physical Law) but demonstrated rather than argued — the sandbox is the empirical arm of that philosophical claim.

**Three project-level takeaways** (paraphrased from the README):

1. **Mathematics' unreasonable effectiveness is explained.** If laws are emergent invariants forced by architectural constraints, mathematics is simply the tool that maps those invariants. Math works because it describes the geometry of consequences.
2. **Massive complexity does not require randomness.** A purely deterministic system with minimal rules and topological boundaries naturally folds into complex scaling behaviours, resonant plateaus, and chaotic-looking boundaries — no RNG anywhere in the code.
3. **Architecture-first view of reality.** The rules are the walls; physical laws are the shape of the space trapped inside them. Understanding the real universe may require looking past the laws to understand the architecture that forces them to exist.

### 11.3 Repository structure

```
emergence-universe/
├── ED-SIM-Code/           # Python 3.10+ — no randomness in default mode
│   ├── ED_Update_Rule.py          # 2D-lattice cosmological solver (ED-05.5 gradient flow)
│   │                              # = the canonical Scenario-D solver referenced in §6.9
│   ├── ED_Lattice.py              # 2D lattice data structure
│   ├── ED_Visualization.py        # Rendering
│   ├── event_update.py            # N-particle ring sandbox update
│   ├── event_lattice.py           # Particle-sandbox data structure
│   ├── event_visualization.py     # Particle-sandbox rendering
│   ├── micro_event_operator.py    # The ED "micro-event" atomic update operator
│   ├── run_micro_event_sim.py     # Sandbox driver
│   ├── Run_Simulation.py          # 2D-lattice driver
│   ├── check_*.py                 # Per-law verification scripts (check_law_ix_consolidation.py etc.)
│   ├── generate_*.py              # Sweep generators (parameter-space grids)
│   ├── fit_alpha.py               # Temporal-scaling exponent fits
│   ├── laws/                      # Per-law output tables
│   ├── me_output/                 # Micro-event simulation outputs
│   └── Reproduce_This_Law/        # Law-by-law reproduction scripts
│
├── ED-SIM-Papers/
│   ├── 00 ED-Arch Foundations/    # ED-Arch-00 Architectural Framework + ED-Arch-00 Micro-Event Operator
│   ├── 01-19 ED-Arch Developmental/
│   │     # ED-Arch-01 Emergent Architecture … ED-Arch-19 γ-Gate and Saddle Sheet
│   │     # Includes ED-Arch-12.5 Cosmology from the ED Compositional Rule
│   │     # Includes ED-SC-00 Scale-Correspondence in Event Density
│   └── 20-29 ED-Arch Laws/        # ED-Arch-20 through ED-Arch-35 — Laws I–XIV + manifolds + compositionality
│
├── Reproduce_This_Paper/
├── ED-SIM_TakeAways_Emergence_Constraint_Physical_Law.pdf
└── README.md
```

### 11.4 The 14 architectural laws (ED-Arch Laws I–XIV)

These laws govern a **discrete particle universe** — N equally-spaced particles on a ring of radius R on a periodic-boundary-condition (PBC) unit box — not the canonical ED PDE. They test whether architectural invariants arise from a minimal deterministic rule.

**Parameters swept:** N ∈ {4, 8, 12, 20, 24, 32, 48, 64, 128}; launch angle γ; radius r; drift d. Merge threshold `merge_thr = 23.5 / 400 = 0.05875` in engine units. 45,031 total sweep+atlas files across 21 angles, 17 radii, 8 drifts, 14 N values.

**The lambda invariant.** All 14 laws are ultimately organised by a single dimensionless control parameter:

`λ(N) = s(N) / merge_thr`, where `s(N) = 2π·R / N` is the mean inter-particle spacing.

Three regimes:
- **λ >> 1** (N = 4): folded, cusp-rich, drift-fragile manifold. 9 sub-mechanism types. Rich temporal structure. Mean `χ` ≈ 22.4.
- **λ ~ 1** (N = 8): resonant plateau. OL-wandering anomaly (24% excess). 8 sub-mechanism types. Mean `χ` ≈ 2.74.
- **λ << 1** (N ≥ 48): flat, drift-rigid, instantaneous collapse. 5 sub-mechanism types. `χ` = 0.01 (measurement floor) for 99.9% of cells.

**The laws:**

| # | Law | Short statement | Status |
|:---|:---|:---|:---|
| I | Sheets, Mirrors, Ladders | The structural decomposition of the manifold — appears in every sweep | Exact |
| II | Islands, Ridges, Resonance | DECAY is a rational-resonance phenomenon, geometric not statistical | Exact |
| III | Windows, Cycles, Recurrence | PBC recurrence windows carry temporal fine structure | Exact |
| IV | Scaling Sensitivity and Structure | Scaling sensitivity is the derivative of the complexity flow in N | Exact |
| V | Commensurability Classes | Number-theoretic coordinates on the tangent layer | Exact |
| VI | N = 4 Rotational Degeneracy | N = 4 is a topological singularity where the manifold folds most sharply | Exact |
| VII | Tangent DECAY Exclusivity | DECAY is confined to N = 4; no DECAY exists at any other N | Exact |
| VIII | Manifold Unification and Complexity Flow | **The 5 descriptive manifolds (mechanism / drift / temporal / atlas / boundary) are projections of a single N-parameterised geometric object with 98.7% cross-layer agreement.** Complexity decreases monotonically with N. | Exact |
| IX | The Lambda Invariant and Asymptotic Geometry | **The entire complexity flow is governed by a single dimensionless parameter `λ(N)`.** The λ = 1 crossover at N = 8 is the sharp transition from folded to planar. | Exact |
| X | Angle Partition and Boundary-Layer Geometry | Angle determines mechanism sector; the boundary band is a thin slice at γ ≈ 0 | Exact |
| XI | The Boundary Band and Radius-Modulated Phase Geometry | PBC geometry is a boundary-layer correction, dependent on radius | Exact |
| XII | PBC Geometry and the Three-Coordinate Generative Hierarchy | **The manifold is generated by exactly three coordinates: λ (temporal regime) + angle (mechanism identity) + PBC geometry (fine structure).** PBC promoted from boundary-band correction to manifold-wide determinant. | Exact |
| XIII | **Generative Closure of the Mechanism Taxonomy** | **Exactly 10 sub-mechanism types exist, no 11th can appear.** 3 approach directions × 3 PBC modes × 3 trajectory regimes = 10 (one degenerate). Closure theorem — the taxonomy is definitively complete. | Exact — the closure theorem of the ED-Arch formalism |
| XIV | Collapse-Time Scaling and the Temporal Hierarchy | `χ ~ λ^p` power law with `p = −7/3` (canonical grid, R² = 0.978) or `p = −2.81` (extended grid, R² = 0.96). Strict hierarchy `χ_folded >> χ_resonant >> χ_planar` across three orders of magnitude. Exponent is **grid-dependent, not universal** — it encodes the radius distribution of the measurement grid. | Exact |

**Key quantitative results from Law VIII (empirical grounding):**
- Cross-layer agreement exceeds **98.7%** across 1,980 canonical sweep cells (4 Ns × 9 angles × 11 radii × 5 drifts).
- 0/65 IC cells appear outside the phase boundary.
- Complexity metrics (folds, cusps, subtypes, mean χ, metastable cells, curvature κ, torsion τ) all **decrease monotonically** from N = 4 (folded, κ ≈ 222, 9 subtypes) to N = 20 (trivial hyperplane, 5 subtypes).
- The **DECAY filament** at (N = 4, γ = 0, all radii) is the only structural exception — a 1D singularity topologically isolated from the IC domain. Destroyed by drift `d = 0.02`.
- The **N = 8 OL-wandering resonance** is a quantitative plateau (24% excess versus 0–1.4% at other N) producing a slow temporal band — visible in all five layers simultaneously.

### 11.5 How the sandbox relates to the rest of the ED program

| Sandbox element | ED-PDE counterpart |
|:---|:---|
| 14 laws governing a minimal particle universe | Nine L-laws (§5.6) governing the canonical continuum PDE |
| Generative Closure (exactly 10 mechanism types) | Five universality classes (PME, RC, Stefan, Telegraph, Void — §6.10 X5D) |
| λ (spacing-to-merge-threshold ratio) controls regime | D (channel weight) controls regime, with `D_crit = 0.5` (Canon P6) |
| Folded (λ >> 1) / resonant (λ ≈ 1) / planar (λ << 1) | Oscillatory (D < 0.1) / hybrid / parabolic (D ≥ 0.5) — §4 |
| Compositional rule → 2D lattice → `∂p/∂t = β∇²p − α·p^γ` | ED-05.5 / ED-Phys-12.5 gradient-flow derivation |
| Scenario-D noisy variant (`ED_Update_Rule.py` with `noise_scale > 0`) | The reference canonical measurement for ED-SC 2.0 (§6.9) |
| Architecture-first thesis ("laws are emergent invariants") | §5.9 Architecture of Physical Law paper |

**The sandbox is the *proof-of-concept* for the ED thesis** that laws are architectural consequences. The canonical ED PDE is the *specific instantiation* of that thesis applied to our universe. The two are mutually supporting: the sandbox demonstrates that the thesis is realisable in a minimal universe; the canonical PDE demonstrates that the thesis produces *physically-recognisable* structure in a universe with continuous fields and dimensional units.

### 11.6 How to use the Emergence-Universe repo in future sessions

- **If the user references "ED-SIM" without qualification** — always disambiguate first. "Do you mean the continuum PDE solver (edsim/) or the Emergence-Universe sandbox?" The vocabulary overlap is real and has confused prior sessions.
- **If the user asks about Laws I–XIV** — these are the sandbox laws, not the L1–L9 of §5.6. The two sets have different domains (discrete particle universe vs. continuum PDE) and different purposes.
- **If the user asks about Scenario D parameters, mobility exponent `n`, or the `(n, σ)` phase-exit surface** — this lives at the intersection: the canonical Scenario-D implementation is in the Emergence-Universe repo's `ED-SIM-Code/`, but the architectural-invariants claim (§6.8 ED-Arch / ED-Sim-01) and the motif-conditioned median (§6.9 ED-SC 2.0) are documented separately.
- **If the user asks "how do I reproduce the 14 laws"** — point to `emergence-universe/ED-SIM-Code/check_*.py` and `Reproduce_This_Law/`. Each law has a corresponding check script.
- **If the user asks where the 1/r dilution argument underpinning ED-XX lives** — this repo is NOT the answer. The Emergence-Universe sandbox does not contain a 3D Green's-function derivation. The ED-XX source is still unlocated (see §6).

---

## 12. The Factor Skyline program (non-physics, multiplicative number theory)

**Added 2026-04-21 (late).** Allen has two PhilArchive papers on a program called **The Factor Skyline**:

1. **The Factor Skyline: A 2-Dimensional View of the Number Line**
2. **The Factor Skyline: A Unified Architecture for Multiplicative Number Theory**

These are **separate from the ED physics program**. They are an application of architectural thinking to pure number theory, specifically to prime distribution and factorisation. The second paper's key claim: *"primes are not random. They are the deterministic escape points of a geometric coverage process generated by the least prime factor."*

**Note that there is *also* a document called `X5D_Evaluation_EventDensity.md` on the Desktop** (covered in §6.10) that uses "Factor Skyline" as an evaluation framework for theories like ED (assessing Minimality / Locality / Determinism / Generative Sufficiency / Envelope Tightness / Structural Optimality). The two uses are **related but distinct:**

- The PhilArchive papers apply the Factor Skyline to the number line itself (primes, factorisation, deterministic escape points).
- The X5D Evaluation document applies a variant of the same framework to **evaluate scientific theories** (ED passes all 6 FS criteria; §6.10).

Both come from the same architectural impulse — treat structure as emergent from coverage / constraint rather than as fundamental — but they live in different domains (number theory vs. theory-evaluation meta-framework).

**How to handle Factor Skyline in future sessions:**
- **If the user asks about primes, factorisation, or the number line** — these are the PhilArchive papers. Not physics; not ED. Treat as a separate intellectual thread of Allen's work.
- **If the user asks about the X5D or "Factor Skyline evaluation" of ED or another theory** — that's §6.10 in this doc; the evaluation meta-framework.
- **If the user asks whether Factor Skyline and ED are unified** — not explicitly in the current literature. The architectural-thinking-style is shared; no formal cross-citation identified.
- These two papers are **not** candidates for the ED physics session-start reading list. They belong in Allen's publication portfolio but are outside the empirical / interpretive / scale-correspondence tracks.

---

*This is a living single-file orientation. Track substantive updates in the "Recent substantive updates" block at the top of the document, not here. For point-in-time snapshots (e.g., for external paper citations), use git commit SHAs rather than embedding version stamps in the filename.*
