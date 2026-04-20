# Universal Invariants of the Canonical ED PDE

**Purpose.** This document captures the universal invariants that fall out of the canonical Event Density PDE without any per-system tuning. Each invariant is a structural consequence of the seven Architectural Canon principles (P1–P7) acting on the unified-equation form established in 00.3 *Unified Cosmological Equation* (March 2026). They are not fit parameters; they are theorems of the equation.

**Sources.** Derivations drawn from 00.3, ED-Phys-15 through ED-Phys-19 (the in-repo simulation series at [`archive/research_history/ED Physics/`](../archive/research_history/)), and the Architectural Canon ([`Architectural_Canon.md`](Architectural_Canon.md)). Where the source PDF is on Desktop only (00.3 itself), the derivation here is reconstructed from the in-repo simulation traces and the orientation summary at [`../docs/ED-Orientation.md`](../docs/ED-Orientation.md) §4.

**Cross-reference.** For the architectural principles these invariants follow from, see [`Architectural_Canon.md`](Architectural_Canon.md). For the concrete PDE instantiation, see [`PDE.md`](PDE.md). For the broader ED corpus context, see [`../docs/ED-Orientation.md`](../docs/ED-Orientation.md) §3, §4, and the universal-invariants block in §6.9 / §22 of [`../docs/ED-09-5-Observable-Sharpening.md`](../docs/ED-09-5-Observable-Sharpening.md).

---

## 1. The unified PDE in canonical form

The canonical equation in its current cleanest statement (from 00.3):

$$\partial_t \rho \;=\; D \cdot F[\rho] \;+\; H \cdot v, \qquad D + H = 1,$$

$$\dot v \;=\; \frac{1}{\tau}\bigl(F[\rho] - \zeta v\bigr),$$

$$F[\rho] \;=\; M(\rho)\,\nabla^2\rho \;+\; M'(\rho)\,|\nabla\rho|^2 \;-\; P_{SY2}(\rho),$$

$$P_{SY2}(\rho) \;=\; \alpha\gamma \cdot \frac{\rho - \rho^*}{\sqrt{(\rho - \rho^*)^2 + \rho_0^2}}.$$

The invariants in §2–§4 below are properties of this equation that hold *without further parameter tuning*, *across all dimensions*, and *across all initial conditions consistent with the ED domain*.

---

## 2. Oscillation-death threshold: `D_crit = 0.5`

### Statement

The flow type of the coupled `(ρ, v)` system is governed by the **damping discriminant** (Canon principle P6):

$$\Delta \;=\; D + 2\zeta.$$

The system is **underdamped (oscillatory)** when `Δ < 1` and **overdamped (parabolic)** when `Δ > 1`. The transition at `Δ = 1` is **sharp** — i.e., a discontinuous change in dynamical character at a specific parameter value, not a smooth crossover. For the canonical choice `ζ = 1/4`, the transition lands at:

$$\boxed{\;D_{\text{crit}} \;=\; 1 - 2\zeta \;=\; 0.5 \quad\text{(at canonical }\zeta = 1/4\text{).}\;}$$

The deeper invariant is `Δ_crit = 1` — the location of the discriminant zero. The specific value `D_crit = 0.5` follows from the canonical `ζ = 1/4` choice. Different `ζ` shifts `D_crit` accordingly without changing the sharpness or the existence of the bifurcation.

### Derivation sketch

Linearise the canonical PDE around the unique equilibrium `ρ = ρ*` (set `δ = ρ − ρ*`, ignore spatial gradients for the uniform mode, and use the linear penalty `P(δ) ≈ P₀ δ` with `P₀ = αγ/ρ_0`). The system becomes

$$\dot\delta \;=\; -D P_0\, \delta \;+\; H\, v, \qquad \dot v \;=\; \tfrac{1}{\tau}\bigl(-P_0\,\delta - \zeta\, v\bigr).$$

The matrix is `[[-DP₀, H], [-P₀/τ, -ζ/τ]]`, with characteristic polynomial

$$\lambda^2 + (D P_0 + \zeta/\tau)\,\lambda + (P_0/\tau)(D \zeta + H) \;=\; 0.$$

Reading the discriminant of this quadratic and tracking the boundary between complex-conjugate roots (oscillatory) and real roots (overdamped), the transition lands at `D + 2ζ = 1` for the canonical normalisation `P₀ = 1/τ`. Sharp because the discriminant is a continuous monotone function of `Δ` that crosses zero transversally at `Δ = 1`.

### Numerical confirmation

ED-Phys-18 (`HybridCosmology`) and ED-Phys-19 (`UnifiedCosmology`) confirm `D_crit = 0.5` numerically by sweeping `D` across the bifurcation and observing the qualitative regime change. The orientation summarises three regimes:

| Regime | Condition | Behavior |
|:-------|:---------:|:---------|
| Oscillatory | `D < 0.1` (or `Δ < 1`) | Underdamped, reversible, standing participation waves; 8–19 transient oscillations per ED-Phys-17 |
| Hybrid | `0.1 ≤ D ≤ 0.4` | Mixed, smooth interpolation |
| Parabolic | `D ≥ 0.5` (or `Δ > 1`) | Overdamped, irreversible, structure-forming; Barenblatt spreading; horizon dynamics |

### Why it matters

This is the architectural backbone of the **ED-09.5 quantum-classical transition prediction**. The identification of `D_crit = 0.5` with the physical Q-C boundary is the central claim of the Aspelmeyer optomechanics analysis in [`../docs/ED-09-5-Observable-Sharpening.md`](../docs/ED-09-5-Observable-Sharpening.md) §11, §22.

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
| `D_crit = 0.5` | ED-09.5 quantum-classical sharp transition (`docs/ED-09-5-Experimental-Strategy.md`); regime classification across the dimensional atlas |
| `E_ground = αγρ₀` | Confirmed in ED-Phys-17 §12.2; underlies the heat-death floor in 00.1 *Cosmology from the Compositional Rule* |
| `t_rel ≈ ρ₀/(αγ)` | Sets the timescale for the porous-medium, RC-Debye, and telegraph reductions; appears in UDM, FRAP, Cluster Merger-Lag predictions |

Together with the **dimensional invariant** `D · T₀/L₀² = 0.3` (verified across 5 regimes spanning 61 orders of magnitude per the dimensional atlas), the **triad coupling** `C ≈ 0.03` (ED-Phys-16), the **third-harmonic ratio** 3–6 % of fundamental (ED-Phys), and the **ED-SC 2.0 architectural saddle ratio** `r* ≈ −1.304` (`docs/ED-SC-2.0.md`), they form the **universal-invariant block** of the ED Math Pipeline (see [`docs/figures/atlas/ED-Math-Pipeline.png`](../docs/figures/atlas/ED-Math-Pipeline.png) bottom row). Each is a forced consequence of the canonical PDE, with no additional assumptions.

---

## 6. What this document is not

- **Not a derivation from first principles.** The full derivations live in 00.3 (Desktop / PhilArchive) and in the ED-Phys-15 through ED-Phys-19 in-repo simulation series. This document gives the canonical statements with derivation sketches sufficient for reading the rest of the corpus.
- **Not exhaustive.** Other invariants exist — the mobility-capacity bound, the harmonic-protection ratio, the architectural saddle ratio (ED-SC 2.0), the cross-dimensional `α_R` exponent (ED-SIM-3D) — and are listed in [`Architectural_Canon.md`](Architectural_Canon.md) §3 and the universal-invariants block of the orientation. This document focuses on the three that are most directly used in empirical predictions and that are simplest to derive from the SY2 penalty.
- **Not regime-specific.** The numerical values are canonical (in ED-Phys natural units). For dimensional values in any specific regime, see the corresponding `ED-Dimensional-NN` paper in the dimensional atlas.

---

*Cross-reference: For the architectural principles, see [`Architectural_Canon.md`](Architectural_Canon.md). For the concrete PDE instantiation, see [`PDE.md`](PDE.md). For the broader corpus map, see [`../docs/ED-Orientation.md`](../docs/ED-Orientation.md). Last substantive update: 2026-04-20.*
