# Universal Invariants of the Canonical ED PDE

**Purpose.** This document captures the universal invariants that fall out of the canonical Event Density PDE without any per-system tuning. Each invariant is a structural consequence of the seven Architectural Canon principles (P1–P7) acting on the unified-equation form established in 00.3 *Unified Cosmological Equation* (March 2026). They are not fit parameters; they are theorems of the equation.

**Sources.** Derivations drawn from 00.3, ED-Phys-15 through ED-Phys-19 (the in-repo simulation series at [`archive/research_history/ED Physics/`](../archive/research_history/)), and the Architectural Canon ([`Architectural_Canon.md`](Architectural_Canon.md)). Where the source PDF is on Desktop only (00.3 itself), the derivation here is reconstructed from the in-repo simulation traces and the orientation summary at [`../docs/ED-Orientation.md`](../docs/ED-Orientation.md) §4.

**Cross-reference.** For the architectural principles these invariants follow from, see [`Architectural_Canon.md`](Architectural_Canon.md). For the concrete PDE instantiation, see [`PDE.md`](PDE.md). For the broader ED corpus context, see [`../docs/ED-Orientation.md`](../docs/ED-Orientation.md) §3, §4, and the universal-invariants block in §6.9 / §22 of [`../docs/ED-09-5-Observable-Sharpening.md`](../docs/ED-09-5-Observable-Sharpening.md).

**r\* status (2026-04-23).** The ED-SC 2.0 motif-conditioned saddle-ratio median is **not** a derivation-based invariant of the canonical PDE. Its status was closed 2026-04-23 as a filter-conditioned statistic of the GRF linearisation of the R2 simulator, with pooled value r\* ≈ −1.88 ± 0.4. See [`ED_SC_2_0_r_star_Final_Verdict.md`](ED_SC_2_0_r_star_Final_Verdict.md) for the full closure and [`../analysis/ED_SC_2_0_Sample_Size_Audit.md`](../analysis/ED_SC_2_0_Sample_Size_Audit.md) for the audit trail. Readers arriving here via the orientation doc's universal-invariant block should not resurrect the scalar form.

---

## 1. The unified PDE in canonical form

The canonical equation in its current cleanest statement (from 00.3):

$$\partial_t \rho \;=\; D \cdot F[\rho] \;+\; H \cdot v, \qquad D + H = 1,$$

$$\dot v \;=\; \frac{1}{\tau}\bigl(F[\rho] - \zeta v\bigr),$$

$$F[\rho] \;=\; M(\rho)\,\nabla^2\rho \;+\; M'(\rho)\,|\nabla\rho|^2 \;-\; P_{SY2}(\rho),$$

$$P_{SY2}(\rho) \;=\; \alpha\gamma \cdot \frac{\rho - \rho^*}{\sqrt{(\rho - \rho^*)^2 + \rho_0^2}}.$$

The invariants in §2–§4 below are properties of this equation that hold *without further parameter tuning*, *across all dimensions*, and *across all initial conditions consistent with the ED domain*.

---

## 2. Oscillation-death threshold: `D_crit(ζ) ≈ 0.896` at canon-default `ζ = 1/4`

> **Update 2026-04-22.** Earlier drafts gave `D_crit = 0.5` via the additive heuristic `Δ = D + 2ζ, critical at Δ = 1`. That heuristic is retired as a quantitative claim (it is off by ~80%). The correct linearised threshold is given by the exact discriminant below. Derivation and discrepancy analysis in [`D_crit_Resolution_Memo.md`](D_crit_Resolution_Memo.md).

### Statement (revised)

The flow type of the coupled `(ρ, v)` system is governed by the **damping discriminant** of the linearised 2×2 system around equilibrium. At reference mode `ε_k·τ = 1`:

$$
(D - \zeta)^2 \;<\; 4\,(1 - D) \quad \Longleftrightarrow \quad \text{underdamped (oscillatory)}
$$

The transition at equality is **sharp** — a transversal crossing of the discriminant through zero, giving a discontinuous change in dynamical character. The critical threshold is

$$
\boxed{\;D_{\rm crit}(\zeta) \;=\; -(2-\zeta) + 2\sqrt{2-\zeta} \;=\; \sqrt{2-\zeta}\bigl(2 - \sqrt{2-\zeta}\bigr).\;}
$$

At canon-default `ζ = 1/4`: **`D_crit ≈ 0.8958`** (the "0.9" figure flagged in the 2026-04-20 ED-Dimensional-01-Ext Appendix A). At `ζ = 0`: `D_crit = 2√2 − 2 ≈ 0.828`. At `ζ → 1`: `D_crit → 1`.

The deeper invariant is the **existence** and **sharpness** of the bifurcation, not its numerical location. Both survive the correction; the numerical value changes from 0.5 to ≈ 0.896.

### Derivation (corrected)

Linearise the canonical PDE around `ρ*` with `δ = ρ − ρ*`. Using `P(δ) ≈ P₀ δ` (linear penalty) and `M(ρ*) = M₀`, the mobility-channel contribution is `M₀∇²δ`. Fourier mode at wavenumber `k` gives the effective rate `ε_k = M₀ k² + P₀`. The coupled (ρ, v) ODE becomes

$$
\dot\delta \;=\; -D\epsilon_k\,\delta + H\,v, \qquad \dot v \;=\; \tfrac{1}{\tau}\bigl(-\epsilon_k\,\delta - \zeta\, v\bigr).
$$

Characteristic polynomial:

$$
\lambda^2 + (D\epsilon_k + \zeta/\tau)\,\lambda + \frac{\epsilon_k(D\zeta + H)}{\tau} \;=\; 0.
$$

With `ε_k = τ = 1` and `H = 1 − D`, the underdamping condition `T² < 4S` collapses to

$$
(D + \zeta)^2 < 4(1 - D + D\zeta) \;\;\Longleftrightarrow\;\; (D - \zeta)^2 < 4(1-D),
$$

and equality at `D_crit(ζ)` as above. The earlier heuristic `Δ = D + 2ζ = 1` drops the coupled cross-term and over-weights `ζ` by ~2×; full derivation and error analysis in the resolution memo.

### Numerical confirmation

ED-Phys-18 (`HybridCosmology`) and ED-Phys-19 (`UnifiedCosmology`) swept `D` across the bifurcation and observed the qualitative regime change. Their published boundary at `D ≈ 0.5` used the retired heuristic as a classification marker; the underlying eigenvalues are correctly computed in code and therefore the actual numerical results do not change, only the interpretive label shifts from "boundary at 0.5" to "boundary at ≈ 0.896."

The three-regime taxonomy survives:

| Regime | Condition (corrected) | Behavior |
|:-------|:---------------------|:---------|
| Oscillatory | `D ≪ D_crit(ζ)` | Underdamped, reversible, standing participation waves; 8–19 transient oscillations per ED-Phys-17 |
| Hybrid | `D → D_crit(ζ)` from below | Mixed, smooth interpolation |
| Parabolic | `D ≥ D_crit(ζ) ≈ 0.896` | Overdamped, irreversible, structure-forming; Barenblatt spreading; horizon dynamics |

### Why it matters

This is the architectural backbone of the **ED-09.5 quantum-classical transition prediction**. The claim is that `D_crit` is a physical Q-C boundary — a claim about the **existence of a sharp transition**, not its numerical value. The correction shifts the boundary from 0.5 to ≈ 0.896 but leaves the Q-C claim qualitatively intact. Any Aspelmeyer optomechanics analysis or other experimental-design memo that depends on the sharp-transition existence ([`../docs/ED-09-5-Observable-Sharpening.md`](../docs/ED-09-5-Observable-Sharpening.md) §11, §22) inherits the corrected threshold without structural disruption.

**Helper available in code** — `edsim.math.damping.d_crit(zeta)` and `edsim.math.damping.D_CRIT_CANONICAL` for programmatic access.

---

## 3. Ground-state energy: `E_ground = αγρ₀`

### Statement

The canonical SY2 penalty derives from a **scalar potential**

$$V_{SY2}(\rho) \;=\; \alpha\gamma \cdot \sqrt{(\rho - \rho^*)^2 + \rho_0^2}.$$

(Verify: `dV/dρ = αγ · (ρ − ρ*)/√(…) = P_SY2(ρ)`, ✓.) At the unique minimum `ρ = ρ*`, the potential takes the value:

$$\boxed{\;E_{\text{ground}} \;=\; V_{SY2}(\rho^*) \;=\; \alpha\gamma\,\rho_0.\;}$$

### Properties

- **Dimension-independent.** The minimum value of `V_SY2` does not depend on the spatial dimension `d`.
- **Regime-independent.** Independent of the channel weights `D`, `H`, the participation parameters `τ`, `ζ`, the mobility prefactor `M_0`, the exponent `β`, or the capacity bound `ρ_max`.
- **Initial-condition-independent.** Any IC consistent with the ED domain (`0 ≤ ρ ≤ ρ_max`) relaxes to the unique minimum at `ρ*`, where `V` takes the same value `αγρ₀`.

### Why it matters

`E_ground` is the **floor of the ED energy budget**. Any ED system at equilibrium carries this irreducible energy per unit configuration; it is the analogue of zero-point energy in quantum systems but is structurally derivable rather than postulated.

For ED-Phys-17 canonical parameters (`α=0.1, γ=0.5, ρ_0=0.5`), `E_ground = 0.025`, matching the simulation's reported asymptotic energy in ED-Phys-17 §12.2 to machine precision.

---

## 4. Universal relaxation timescale: `t_rel ≈ ρ₀/(αγ)`

### Statement

For small perturbations around equilibrium, the SY2 penalty linearises to

$$P_{SY2}(\rho) \;\approx\; \frac{\alpha\gamma}{\rho_0}\,(\rho - \rho^*) \quad \text{for } |\rho - \rho^*| \ll \rho_0.$$

The linearised stiffness is `K_eff = αγ/ρ_0`. The associated relaxation timescale (the natural decay time for perturbations to the equilibrium) is:

$$\boxed{\;t_{\text{rel}} \;\approx\; \frac{1}{K_{\text{eff}}} \;=\; \frac{\rho_0}{\alpha\gamma}.\;}$$

For ED-Phys-17 canonical parameters, `t_rel ≈ 0.5/(0.1·0.5) = 10`, which sets the natural unit of relaxation in those simulations.

### Spread across the hybrid regime

00.3 reports that `t_rel` varies by only **~13 %** across the entire hybrid parameter space (`0.1 ≤ D ≤ 0.4`). This is a non-trivial property: the relaxation timescale is set by the penalty's linearised stiffness, which is independent of `D` and `H`; the small residual variation comes from the participation-channel coupling modifying the effective decay rate at second order.

### Why it matters

`t_rel` is the **universal clock** of any ED system. It appears in the porous-medium reduction (mobility channel), in the Debye / RC reduction (penalty channel), and as one of the two timescales in the telegraph / RLC reduction (participation channel) — see [`PDE.md`](PDE.md) §4 for these channel reductions.

In dimensional regimes:
- **Quantum regime:** `t_rel ~ ρ₀/(αγ) · T_0 ~ 0.6·ℏ/(mc²)` per [ED-Dimensional-01](../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md).
- **Galactic regime:** `t_rel ~ ρ₀/(αγ) · T_0 ~ Myr` per [ED-Dimensional-04](../papers/Dimensional_Atlas/regimes/ED-Dimensional-04_Galactic_Regime.md).
- **Optomechanics regime:** `t_rel ~ 1/γ_dec` under the candidate-(b) cavity-field identification per [ED-09-5-Observable-Sharpening](../docs/ED-09-5-Observable-Sharpening.md) §15, §22.

---

## 5. Where these invariants enter empirical claims

Each invariant anchors a different class of ED prediction:

| Invariant | Anchors |
|:----------|:--------|
| `D_crit(ζ) ≈ 0.896` at `ζ = 1/4` | ED-09.5 quantum-classical sharp transition (`docs/ED-09-5-Experimental-Strategy.md`); regime classification across the dimensional atlas. Corrected 2026-04-22 from retired heuristic 0.5; see `D_crit_Resolution_Memo.md` |
| `E_ground = αγρ₀` | Confirmed in ED-Phys-17 §12.2; underlies the heat-death floor in 00.1 *Cosmology from the Compositional Rule* |
| `t_rel ≈ ρ₀/(αγ)` | Sets the timescale for the porous-medium, RC-Debye, and telegraph reductions; appears in UDM, FRAP, Cluster Merger-Lag predictions |

Together with the **dimensional invariant** `D · T₀/L₀² = 0.3` (verified across 5 regimes spanning 61 orders of magnitude per the dimensional atlas), they form the **derivation-based universal-invariant block** of the ED Math Pipeline (see [`docs/figures/atlas/ED-Math-Pipeline.png`](../docs/figures/atlas/ED-Math-Pipeline.png) bottom row). Each is a forced consequence of the canonical PDE, with no additional assumptions.

**Not in this block (removed 2026-04-23):** the ED-SC 2.0 motif-conditioned saddle-ratio median (formerly `r* ≈ −1.304`) and the two ED-Phys-16-provenance figures `C ≈ 0.03` (triad coupling) and third-harmonic ratio 3–6 %. The first was retired from scalar-invariant status following the falsifier audit; the structural replacement is *"a motif-conditioned saddle-ratio distribution exists on the filtered Gaussian-random-field saddle population of the canonical PDE and is filter-dependent"* — see [`ED_SC_2_0_r_star_Final_Verdict.md`](ED_SC_2_0_r_star_Final_Verdict.md). The latter two remain provisional pending provenance re-check against the C7 deterministic-canonical-operator results (`analysis/scripts/telegraph_pme/triad_calibration/memo.md`).

---

## 6. What this document is not

- **Not a derivation from first principles.** The full derivations live in 00.3 (Desktop / PhilArchive) and in the ED-Phys-15 through ED-Phys-19 in-repo simulation series. This document gives the canonical statements with derivation sketches sufficient for reading the rest of the corpus.
- **Not exhaustive.** Other invariants exist — the mobility-capacity bound, the harmonic-protection ratio, the architectural saddle ratio (ED-SC 2.0), the cross-dimensional `α_R` exponent (ED-SIM-3D) — and are listed in [`Architectural_Canon.md`](Architectural_Canon.md) §3 and the universal-invariants block of the orientation. This document focuses on the three that are most directly used in empirical predictions and that are simplest to derive from the SY2 penalty.
- **Not regime-specific.** The numerical values are canonical (in ED-Phys natural units). For dimensional values in any specific regime, see the corresponding `ED-Dimensional-NN` paper in the dimensional atlas.

---

*Cross-reference: For the architectural principles, see [`Architectural_Canon.md`](Architectural_Canon.md). For the concrete PDE instantiation, see [`PDE.md`](PDE.md). For the broader corpus map, see [`../docs/ED-Orientation.md`](../docs/ED-Orientation.md). Last substantive update: 2026-04-20.*
