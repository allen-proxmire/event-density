# ED Testing-Mode Synthesis — 2026-04-17

**Frame.** Full three-track architecture loaded, ED-XX environmental sourcing internalized, ED-Arch formal ontology incorporated, FRAP treated as active external pipeline. Not running tests — producing the testing map.

---

## 1. Structural summary of ED as it now stands

### PDE canon (current)

Two parameterizations of the same architecture:
- **Dimensional (repo PDE.md):** `∂_t ρ = D_phys·[M(ρ)∇²ρ + M'(ρ)|∇ρ|² − P(ρ)] + H_phys·v`, `τv̇ = F̄(ρ) − ζv`. `M(ρ) = M₀(ρ_max−ρ)^β`, `D_phys = 2.1×10²⁷ m²/s` anchored from Mistele weak-lensing extent.
- **Dimensionless (00.3 Canon):** `∂_t ρ = D·F[ρ] + H·v`, `D + H = 1`, `D, H ∈ [0,1]`.

**Canonical penalty:** `P_SY2(ρ) = αγ·(ρ−ρ*)/√((ρ−ρ*)² + ρ₀²)` — saturating. The linear form in repo PDE.md is a near-equilibrium simplification; horizon/heat-death behavior requires SY2.

**Canon (P1–P7):** operator structure / channel complementarity / penalty equilibrium / mobility capacity bound / participation feedback loop / damping discriminant / nonlinear triad coupling. Counterfactually minimal and irreducible.

**Pre-PDE layer (ED-05):** four measure-theoretic axioms (non-negativity, null baseline, monotonicity, subadditivity) on a bare event domain.

**Uniqueness (ED-13):** four primitives + seven axioms → unique scalar dynamical equation. Three channels ↔ porous-medium + Debye + telegraph reductions exactly.

### Universal invariants (00.3)

| Invariant | Value | Source |
|---|---|---|
| Equilibrium density | `ρ*` — unique zero of P_SY2, globally attracting ∀ D∈[0,1] | 00.3 |
| Ground state energy | `E_ground = αγρ₀` — dimension/regime/IC-independent | 00.3 |
| Relaxation timescale | `t_rel ≈ ρ₀/(αγ)` — varies <13% across hybrid param space | 00.3 |
| Oscillation-death threshold | `D_crit = 0.5` — sharp | 00.3, ED-Phys-18 |
| Triad coupling coefficient | `C ≈ 0.03` | ED-Phys-16 |
| Harmonic ratio | 3–6% of fundamental | ED-Phys |
| Quality factor | `Q ≈ 3.5` (oscillatory sector) | 00.3 |
| Transient oscillation count | `N_osc ≈ 9` (8–19 observed) | ED-Phys-17 |
| Dimensional nondimensional invariant | `D_phys · T₀/L₀² = 0.3` exact across 5 regimes | Dimensional Atlas |
| Architectural saddle ratio | `κ_∥/κ_⊥ ≈ −1.3 ± 0.2` — matches Local Group sheet + Casimir | ED-Arch-01 |

### ED-XX environmental sourcing (April 2026)

- Temporal-tension source must have σ ≥ 1–3 Mpc (groups/filaments/cosmic web) for flat T(r) over 10–1000 kpc.
- Galaxies set **amplitude** (baryonic identity); environment sets **spatial extent**.
- Merger-lag at cluster scale unaffected (clusters ARE the extended source).
- Source document for 1/r derivation still unlocated (orientation §6 is reconstruction).

### Interpretive layer (ED-I / ED-10)

- **ED-10 coarse-graining dictionary:** space = participation adjacency, time = commitment order, curvature = ED gradient structure, horizons = decoupling surfaces, etc.
- **ED-I operational vocabulary:** chain, multiplicity, identity alignment, rewrite-on-measurement, global ED-curvature, parameter-space channel.
- **ED-I-12/13/14/27:** photonics, quantum information, topological effects, weak lensing — interpretive reframings, *not* new empirical predictions.

### Scale-correspondence + architectural layer (ED-SC + ED-Arch)

- **ED-SC-00 + Table 1 (22 micro↔cosmological correspondences):** architectural invariance across 20+ orders of magnitude. Pocket / channel / saddle / divergence zone / stationary point / threshold vocabulary.
- **ED-Arch-02:** formal Hessian criteria (saddle = orthogonal gradient sign-flip, det(H)<0; boundary = λ_⊥>0; horizon = λ_⊥<0; channel = alignment `d/ds(∇E/‖∇E‖)≈0`).
- **ED-Arch-01 / ED-Sim-01:** empirical validation via 512×512 Scenario-D sweep; saddle peak at (n=2.7, σ=0.0556); κ_∥/κ_⊥ ≈ −1.3 matches Local Group and Casimir.

---

## 2. Cross-track integration

### How the three tracks constrain each other

- **Empirical ↔ Interpretive:** ED-I reframings sit on top of the same PDE the empirical track tests. A failing UDM fit or a failing Cluster Merger-Lag prediction would break the PDE, hence break every ED-I reinterpretation simultaneously. The interpretive track is *not* insulated from empirical falsification — it shares the substrate.
- **Empirical ↔ Scale-correspondence:** ED-SC's cross-scale identity claim (e.g., Local Group sheet ↔ Casimir cavity) is now independently empirically accessible via ED-Arch-01. A saddle ratio κ_∥/κ_⊥ *not* clustering near −1.3 across more domains would falsify the scale-correspondence unification.
- **Interpretive ↔ Scale-correspondence:** ED-I identifies what specific experiments look like through ED; ED-SC identifies architectural invariants that recur across experiments. A Berry-phase AB interpretation (ED-I-14) and a "topologically protected filament / void wall" correspondence (ED-SC Table 1 row 014) must describe the same global ED-curvature in different guises — if they diverge, one account is wrong.

### Overdetermined vs. underdetermined

**Overdetermined (strong architecture, little room to wiggle):**
- P1–P7 Canon + ED-05 axioms → unique PDE (ED-13 claim). No free structural choices.
- `D_nd = 0.3` across five regimes (Dimensional Atlas) — no fit parameters, must hold exactly.
- `D_crit = 0.5` — analytic, sharp, not tunable.
- `E_ground = αγρ₀` and `t_rel ≈ ρ₀/(αγ)` — dimension/IC-independent.
- κ_∥/κ_⊥ architectural saddle ratio — one measurement, three orders-of-magnitude-apart predictions.

**Underdetermined (room to adjust without breaking architecture):**
- Specific `M(ρ)` shape (any function with M(ρ_max)=0).
- Specific `P(ρ)` shape (any monotone with P(ρ*)=0; SY2 vs linear is near-equilibrium indistinguishable).
- Parameter values `D, ζ, τ, ρ_max, ρ*` — the constants are regime-anchored, not derived.
- Precise value of mobility exponent β (might be regime-specific per ED-SIM-3D open question).
- Whether ED-Arch regimes map exactly onto 00.3 damping regimes (they almost certainly don't — parameter axes are different).

### Falsifiable vs. interpretive predictions

**Falsifiable (could die tomorrow with new data):**
1. `ℓ = D_T/v_current` across all clusters — any cluster with high v, low D_T showing a large offset kills this.
2. UDM `D(c) = D₀(1 − c/c_max)^β` — any soft-matter system outside the 10-material fit range deviating substantially.
3. Activity-dependent weak-lensing velocities `V_∞ ∝ √S_env` at fixed baryonic mass (post-ED-XX framing).
4. ED-09.5 **sharp** quantum-classical transition — macroscopic quantum experiments verifying only smooth decoherence kill this.
5. Architectural saddle ratio κ_∥/κ_⊥ ≈ −1.3 — a second benchtop ED-channel instantiation showing a different ratio kills ED-SC's strong version.
6. FRAP participation-channel signature (pending).
7. Finner-A1 scale dependence across A2146 + new clusters.
8. `D_nd = 0.3` in any sixth regime.

**Interpretive (cannot be falsified by new data alone):**
- ED-10 dictionary (space = adjacency, time = commitment order, etc.).
- ED-I reinterpretations of photonics, quantum info, topology — they reframe, not predict.
- ED-06 horizon-as-decoupling-surface reading of Hawking/Unruh (consistent with thermal behavior; doesn't predict a different temperature).
- ED-07 derivation of c as max-update-rate (compatible with all SR).
- ED-SC scale-correspondence *as an ontology* — falsifiable only indirectly via the architectural ratio predictions.

---

## 3. Complete test map

### Tests already completed

| Test | Result | Channel | Status |
|:-----|:-------|:--------|:-------|
| UDM soft-matter (10 materials) | R² > 0.986 | Mobility | ✓ confirmed |
| Cluster Merger-Lag (7 clusters + Finner aggregate 58 subclusters) | `ℓ = D_T/v` consistent | Penalty + moving source | ✓ confirmed |
| Dwarf SPARC D_outer (ED-04.5, n=46) | 53% Active>Quiet | Activity proxy (environmental) | ✓ stands under ED-XX |
| SPARC BTFR residual (ED-Data-12..17) | No signal under V-on-M control | Galaxy-level sSFR | ✗ mis-framed per ED-XX; correct variable is environmental |
| PDE dimensional invariant `D_nd` | 0.3 exact in 5 regimes | Cross-regime | ✓ structural, not empirical |
| ED-SIM-3D invariants (d=1,2,3) | Penalty + participation dimension-independent; mobility per `α_R = 1/(d(m−1)+2)` | All three channels | ✓ axiom P7 validated |
| ED-Arch-01 / ED-Sim-01 Scenario D sweep | Saddle at (n=2.7, σ=0.0556); κ_∥/κ_⊥ ≈ −1.3 matches Local Group + Casimir | Architectural (cross-scale) | ✓ first ED-SC bridge |

### Tests currently running / external pipelines

- **FRAP participation-channel experiment** — out for quote with Creative Proteomics Core. **Active external pipeline.** Tests the participation channel's `τv̇ + ζv = F̄(ρ)` signature in a controlled benchtop system. Participation-channel data is the one channel with no strong empirical confirmation yet at the lab scale. The RLC analogue memo has the theoretical prediction; FRAP gives the physical realization.

### Tests ready to run immediately (no new data/theory)

1. **Finner-A1 scale-dependence** — n=2 confirmed (Bullet + MACS J1149); scoping A2146. Scripts in `analysis/scripts/` already drafted (`finner_a1_analysis.py`, `seven_cluster_validation.py`). Just needs cluster-selection sign-off.
2. **RLC analogue benchtop** — simulation done; lab realization is a straightforward circuit build. Memo in `papers/ED-RLC-Analogue/`.
3. **GAMA lens catalog / GGL pipeline** — pipeline scripts drafted (`gama_lens_catalog.py`, `ggl_pipeline.py`, `ggl_4bin.py`, `ggl_12bin.py`). Needs a sign-off on activity-binning strategy under ED-XX (environmental, not individual).
4. **Architectural saddle ratio in a second mesoscopic system** — ED-Arch-01's Scenario D is one realization. ED predicts κ_∥/κ_⊥ ≈ −1.3 in other competing-gradient systems (thin-film instabilities, optical cavity arrays). Any existing benchtop data with measured curvature ratios would be a zero-cost cross-check.

### Tests requiring new data

1. **BIG-SPARC with group/filament cross-match** — BIG-SPARC release is the target for the correctly-framed activity test. Needs 2MRS / SDSS / GAMA group catalog cross-match.
2. **Additional cluster mergers for Finner-A1 scale-dependence beyond n=3** — A2146 is queued; n>3 needs new imaging/lensing reductions.
3. **KiDS-1000 weak-lensing activity-dependence** (`data/KiDS-1000/` is untracked in repo, suggests work-in-progress).
4. **Macroscopic quantum coherence experiments for ED-09.5** — cavity QED with increasing atom number, optomechanical systems near Q-C boundary, large-mass superposition. No current pipeline — would require a collaboration.

### Tests requiring new theory

1. **Source document for ED-XX 1/r derivation** — needs to be located or re-derived. Currently taken on authority from ED-XX's numerical scan table.
2. **Explicit derivation of architectural saddle ratio κ_∥/κ_⊥ from P1–P7** — ED-Arch-02 shows saddles arise; it doesn't derive the specific ≈ −1.3 ratio from the Canon. Closing this would turn ED-SC into a quantitative predictive theory.
3. **Bridge between ED-Arch regimes and 00.3 D_crit regimes** — currently two separate taxonomies. If there's a deep connection, it's unstated.
4. **Connection between merger-lag wake machinery (Cluster Merger-Lag) and Berry-phase / AB global ED-curvature (ED-I-14)** — I flagged this in the v1.1 pass; ED-SC-00 documents it as a research direction but no formal paper yet.

### Tests requiring new simulation

1. **4D invariant mini-atlas** — ED-SIM-02 has 4D operators; 5 invariant tests not yet run.
2. **Spectral ETD-RK4 in 3D** — cross-validate implicit-Euler results against spectral solver in 3D.
3. **Pre-asymptotic convergence of Barenblatt exponents at β=2, d=3** — needs finer grids or Richardson extrapolation.
4. **Multi-channel ED-Arch architectures** — two-or-more coupled channels to test global-vs-local reconfiguration prediction. Mesoscopic analogue of void-filament bifurcation.
5. **ED-Sim-01 Scenario-D temporal dynamics** — reconfiguration timing, threshold crossings, "breathing-mode" analogues.

### Tests requiring new observational pipelines

1. **Environmental-activity weak-lensing stacking** by group/filament richness — the post-ED-XX definitive test of activity-dependent V_∞.
2. **Wempe et al. galaxy-drift reconstruction comparison** — ED-Arch-01 flags this as a cross-scale saddle test.
3. **Cluster wakes at the penalty mobility ceiling** — P_SY2 vs linear form is distinguishable at high ρ; would require a specific cluster environment or simulation-to-observation pipeline.

---

## 4. Prioritized next tests

### Highest discriminative power

1. **BIG-SPARC environmental activity test.** Under ED-XX this is THE galaxy-scale falsifier. A null result here would hurt ED more than the individual-galaxy sSFR null did. Waiting on BIG-SPARC data release.
2. **ED-09.5 sharp Q-C transition.** Predicts a signature *nobody else predicts.* The single most distinctive falsifiable claim in the ED corpus. Requires a collaboration but the payoff is existential.
3. **Second ED-Arch saddle ratio in a different substrate.** ED-SC's "scale-free is identity not analogy" claim lives or dies on whether κ_∥/κ_⊥ ≈ −1.3 recurs beyond the Scenario D + Local Group + Casimir triad.

### Low-cost, high-yield

1. **Finner-A1 A2146 and next n=3 cluster.** Scripts drafted, data exists, just needs to run. Closes the cluster-scale scale-dependence loop.
2. **RLC benchtop.** Cheap circuit; unambiguous participation-channel test.
3. **Literature sweep for existing competing-gradient systems with published curvature ratios.** Zero-cost cross-check on ED-SC.
4. **4D ED-SIM mini-atlas run.** Sim infrastructure exists; just a compute spend.

### Tests that close architectural loops

1. **FRAP (active)** + **RLC (ready)** — together give mobility + participation channel benchtop coverage; penalty is already covered by Cluster Merger-Lag. Closing all three at lab scale would be a major structural win.
2. **ED-Arch multi-channel coupling** — would empirically test the global-constraint prediction and bridge ED-Arch (mesoscopic) to ED-SC Table 1 (cosmological).
3. **Derivation of κ_∥/κ_⊥ from Canon P1–P7** — would convert an empirical coincidence into a structural prediction, closing the Canon ↔ ED-Arch ↔ ED-SC loop.

### Tests bottlenecked by missing repo updates

1. **`papers/Dimensional_Atlas/regimes/ED-Dimensional-04_Galactic_Regime.md`** — written under galaxy-sourced framing. Any rotation-curve analysis that cites this page propagates a pre-ED-XX assumption. Blocks: any new galaxy-scale test memo.
2. **Data READMEs ED-Data-12..17** — verdicts still not annotated with environmental-vs-galaxy framing per ED-XX. Blocks: clean write-up of the BIG-SPARC plan.
3. **`papers/ED-BTFR-Activity/memo.md`** — addendum acknowledges ED-XX but main body still pre-ED-XX. Blocks: cleanly citing the BTFR result as an ED-XX case study rather than a null.
4. **`theory/PDE.md`** — SY2 noted but linear form still boxed as canonical. Blocks: any horizon/heat-death argument that depends on penalty saturation.

---

## 5. Pressure map

### Where ED is strongest

- **Mobility channel (UDM).** Ten chemically distinct systems, R² > 0.986. Single law, no per-system fit. This is the strongest empirical leg.
- **Penalty + moving source (Cluster Merger-Lag).** Seven clusters + Finner aggregate. `ℓ = D_T/v_current` is a sharp prediction that survives.
- **Architectural uniqueness.** P1–P7 + ED-05 axioms + ED-13 uniqueness → one equation. No structural freedom to hide behind.
- **Cross-scale κ_∥/κ_⊥ ≈ −1.3 match.** Three independent systems (Scenario D, Local Group, Casimir) spanning 20+ orders of magnitude share the same ratio. First quantitative ED-SC bridge.
- **Dimensional atlas D_nd = 0.3.** Exact across 5 regimes — hard to explain as coincidence.

### Where ED is weakest

- **Participation channel at the lab scale.** No direct confirmation yet. FRAP (pending) and RLC (ready) are the first attempts. Until one of these lands, the participation channel's "telegraph/RLC" reduction is a structural claim with no lab-scale verification.
- **Activity-dependent V_∞ at galaxy scale.** BTFR null result (when framed by individual sSFR) is the single public "X" in the empirical table. ED-XX reframes this, but the reframed version hasn't been tested yet. Time-to-falsification is bounded by BIG-SPARC release.
- **Source of the ED-XX 1/r derivation** is unlocated. The architecture rests on a result nobody can currently cite a derivation for.
- **ED-09.5 sharp transition** is the most distinctive prediction but has no assigned test program.

### Where ED is overconstrained

- The combination of (i) Canon P1–P7, (ii) ED-05 axioms, (iii) ED-13 uniqueness claim means there is **no room for a "free parameter fix"** — any empirical failure cannot be rescued by shape-changing `M(ρ)` or `P(ρ)` without breaking the uniqueness theorem.
- `D_nd = 0.3` must hold in any new regime added to the Atlas. Adding a sixth regime where it doesn't hold kills the Atlas.
- κ_∥/κ_⊥ ≈ −1.3 across Scenario D + Local Group + Casimir means any new benchtop realization showing a substantially different ratio would fracture the scale-correspondence claim.

### Where ED is underconstrained

- Specific numerical values of `ζ, τ, ρ_max, ρ*` are regime-anchored but not derived from higher principles.
- The mobility exponent β is treated as a constitutive choice; whether it's regime-specific or universal is an open question flagged by ED-SIM-3D.
- The relationship between the two regime taxonomies (00.3 damping vs ED-Arch spatial) is unspecified.
- The participation channel's identification across regimes is a candidate, not a confirmed fact (per repo theory/README §Status).

### Where the architecture is most sensitive to new data

- **FRAP result.** Only channel with no lab-scale confirmation. High sensitivity.
- **A2146 Finner-A1 cluster.** Confirming n=3 vs. breaking `ℓ = D_T/v_current` is an existential test for the penalty channel.
- **Any second ED-Arch benchtop.** The κ_∥/κ_⊥ ratio is a single-point prediction.
- **First macroscopic-quantum ED-09.5 test.** The sharp transition is falsifiable in a way no other ED prediction matches.

---

## 6. Recommended next-action plan for this session

### Run

- **Nothing yet.** Testing map first, runs second. Follow user's explicit instruction.

### Prepare

1. **Finner-A1 A2146 run-plan memo** — scripts are drafted; what's missing is a one-page pre-registration of selection criteria, expected signal, and kill criterion. Low-cost.
2. **RLC benchtop BOM + measurement protocol** — turn the `papers/ED-RLC-Analogue/` memo into an actionable lab sheet.
3. **BIG-SPARC environmental-activity analysis plan** — under ED-XX. Define the group/filament cross-match strategy, the activity-binning strategy, and the pre-registered signal prediction before BIG-SPARC arrives.
4. **FRAP pre-registration** — while the external pipeline is out for quote, pre-register the participation-channel signature expected from the RLC-analogue prediction. Locks in the falsification criterion before data arrives.
5. **ED-Arch cross-substrate literature sweep memo** — survey published competing-gradient systems with measured Hessian curvature ratios. Identifies zero-cost cross-checks for κ_∥/κ_⊥.

### Clean up in the repo

Prioritized by blast radius × effort:

1. **`data/ED-Data-12..17/` README verdicts** — add the ED-XX environmental-activity annotation. Unblocks the BIG-SPARC memo.
2. **`papers/ED-BTFR-Activity/memo.md`** — elevate the ED-XX addendum into the main body, reframing the result as an ED-XX case study. Unblocks citation.
3. **`theory/PDE.md`** — make SY2 the boxed canonical form; move linear to a footnote. Unblocks horizon / heat-death arguments.
4. **`papers/Dimensional_Atlas/regimes/ED-Dimensional-04_Galactic_Regime.md`** — ED-XX footnote. Unblocks galactic-regime citations.
5. **`theory/Architectural_Canon.md`** — add D_crit = 0.5, E_ground, t_rel explicitly (currently unstated).

### Defer

- **ED-09.5 sharp Q-C transition test design.** High value but needs collaboration. Not a this-session task.
- **4D ED-SIM invariant atlas.** Compute-bound, not structural. Run when compute is free.
- **Locating the 1/r derivation source document.** Worth one Desktop search pass; if not found, write it down as an open question and move on.
- **Reconciling ED-SIM-02 software package with repo `edsim/`.** Housekeeping; not blocking any test.
- **Derivation of κ_∥/κ_⊥ from Canon.** Would be valuable but is a theoretical research task, not a testing task.

---

**Bottom line.** ED has three lab-scale channel tests available (mobility ✓, penalty at cluster scale ✓, participation pending/ready), two galaxy-scale tests in flight (Finner-A1 scale dependence, BIG-SPARC activity), one architectural saddle confirmation in hand (ED-Arch-01), and one existential falsification path (ED-09.5) not yet resourced. The pressure is highest on BIG-SPARC (time-bounded by external release) and on FRAP (lab result lands when it lands). The cheapest near-term win is the RLC benchtop + Finner-A1 A2146. The biggest architectural reward is closing the participation-channel loop.
