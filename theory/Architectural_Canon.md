# The Architectural Canon of Event Density

**Purpose.** This document is the repo-level statement of the **seven irreducible structural principles** that define ED as a class of PDEs, together with the **four pre-PDE axioms** that define ED as a mathematical object beneath the dynamics. It supersedes nothing in [`PDE.md`](PDE.md); it provides the *architectural* layer that PDE.md instantiates.

**Sources.** The seven principles are from the Architectural Canon paper (ED-Arch series, 00.2, March 2026). The four pre-PDE axioms are from ED-05 *Event Density: A Mathematical Formalization* (February 2026). The synthesis statement "four primitives and seven axioms → unique scalar dynamical equation" is from ED-13 *Event Density as a Physical Ontology* (March 2026).

**Cross-reference.** See [`../docs/ED-Orientation.md`](../docs/ED-Orientation.md) §3, §4, §5.5 for the full context, including how the Canon sits inside the broader paper series.

---

## 1. The pre-PDE layer: four measure-theoretic axioms (ED-05)

Before any dynamics are attached, ED is a mathematical object on a **bare event domain**. It assigns a non-negative density value to every finite configuration of micro-events. The four axioms governing this assignment:

| # | Axiom | Statement |
|---|---|---|
| **A1** | Non-negativity | `ED(A) ≥ 0` for every finite configuration `A`. |
| **A2** | Null baseline | `ED(∅) = 0`. |
| **A3** | Monotonicity | If `A ⊆ B`, then `ED(A) ≤ ED(B)`. |
| **A4** | Subadditivity | `ED(A ∪ B) ≤ ED(A) + ED(B)`. Captures the non-linear relational character of becoming. |

No time, geometry, causality, or probability is presupposed. These axioms are situated relative to measure theory, probability, point processes, causal sets, and statistical mechanics, and morphisms between ED systems identify when two systems share underlying structure (categorical perspective).

This is the layer *beneath* the PDE. It establishes what ED *is* before it establishes how ED *evolves*.

### The Compositional Rule (cosmological specialization of A4)

When the subadditivity axiom A4 is generalized to include correction terms at arbitrary scale, it produces the **ED Compositional Rule** (from 00.1 *Cosmology from the ED Compositional Rule*, February 2026):

$$
p(A \cup B) = p(A) + p(B) - \alpha \int_{A \cap B} p^\gamma\,d\mu - \beta \int_{A \cup B} |\nabla p|^2\,d\mu - \gamma \int_{\partial(A \cup B)} h(|\nabla p|)\,dS
$$

Three correction terms:

1. **Relational penalty** `α·∫ p^γ` over the overlap `A ∩ B` — suppresses overlap of high-ED regions (competition).
2. **Gradient penalty** `β·∫ |∇p|²` over the union — drives smoothing (diffusion at this layer).
3. **Boundary term** `γ·∫ h(|∇p|)` over the boundary `∂(A∪B)` — produces horizon / holographic behavior.

This rule is the ontological mechanism behind cosmic behavior: in the early universe, the gradient penalty dominates (inflation-like exponential smoothing); at intermediate times, relational concavity amplifies residual gradients into structures (galaxies, stars, clusters); at late times, ED flows outward (thinning-as-expansion); in the far future, the boundary term dominates (horizon-dominated heat-death). No metric is invoked — the entire cosmological history is a direct consequence of the compositional rule.

In PDE form, this same architectural content appears as the operator `F[ρ] = M(ρ)∇²ρ + M'(ρ)|∇ρ|² − P(ρ)` (principle P1 below) acting on the density field. The compositional rule is the configuration-space statement; the PDE is its continuum-limit dynamics.

---

## 2. The PDE layer: seven canonical principles (00.2 Architectural Canon)

Any PDE satisfying all seven principles below is architecturally ED, regardless of specific functional forms. These principles are **individually necessary and jointly sufficient** (counterfactual analysis in the Canon paper removes each principle and shows an essential architectural layer breaks).

### P1 — Operator Structure

The density field evolves under a nonlinear operator of the form

$$F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$$

— curvature-dependent diffusion, nonlinear gradient coupling, and a density-dependent restoring force.

Without P1: no spatial dynamics, no diffusion, no harmonic generation, no spectral structure. The architecture collapses to uncoupled ODEs.

### P2 — Channel Complementarity

Density evolves through two complementary channels:

$$\partial_t\rho = D\cdot F[\rho] + H\cdot v, \qquad D + H = 1, \qquad D, H \in [0,1]$$

The **direct channel** `D·F[ρ]` applies the operator immediately; the **mediated channel** `H·v` applies it through memory. The conservation constraint `D + H = 1` ensures all dynamics lie on a one-simplex in parameter space.

**Important:** In P2, `D` is a **dimensionless channel weight**, distinct from `D_phys` the dimensional diffusivity in [`PDE.md`](PDE.md). See §1 of `ED-Orientation.md` for the reconciliation.

### P3 — Penalty Equilibrium

The penalty function `P(ρ)` has exactly one zero at `ρ = ρ*`, with `P' > 0`. This equilibrium is unique and globally attracting.

The canonical form of `P` in the current synthesis (00.3, March 2026) is **not** the linear `P₀(ρ − ρ*)` used in [`PDE.md`](PDE.md), but the smoothed / saturating form:

$$P_{SY2}(\rho) = \alpha\gamma \cdot \frac{\rho - \rho^*}{\sqrt{(\rho - \rho^*)^2 + \rho_0^2}}$$

Both forms satisfy P3 near equilibrium, but `P_SY2` persists at the mobility ceiling while the linear form does not. The horizon and heat-death arguments in 00.1 Cosmology depend on `P_SY2`'s saturation behavior.

### P4 — Mobility Capacity Bound

The mobility satisfies `M(ρ_max) = 0` with `M(ρ) > 0` for `ρ < ρ_max`. Density is bounded above, and diffusive transport collapses at the bound.

This is the architectural source of horizons: a horizon forms where `M → 0`, creating a kinetic barrier that separates one region's participation from another's (see ED-06 "Horizons as Decoupling Surfaces" in `ED-Orientation.md` §5.5).

### P5 — Participation Feedback Loop

The participation variable evolves as

$$\dot v = \frac{1}{\tau}(F[\rho] - \zeta v)$$

— integrating the operator with exponential decay and feeding back into density evolution via P2.

Without P5: no memory, no oscillation, no spiral, no temporal causality, no information storage. The architecture reduces to single-variable diffusion.

### P6 — Damping Discriminant

Flow type is determined by the discriminant

$$(D - \zeta)^2 \;<\; 4(1 - D) \quad \Longleftrightarrow \quad \text{underdamped}$$

**Sharp transition at equality:** `D_crit(ζ) = √(2−ζ)·(2 − √(2−ζ))`, which evaluates to **≈ 0.896** at canon-default `ζ = 1/4`. This supersedes the retired additive heuristic `Δ = D + 2ζ = 1 → D_crit = 0.5`, which is off by ~80% (see [`D_crit_Resolution_Memo.md`](D_crit_Resolution_Memo.md), 2026-04-22). The sharpness and structural existence of the bifurcation are unchanged; only the numerical location shifts.

The boundary partitions the architecture into two topologically distinct dynamical regimes and is the mathematical origin of the three-regime phase structure (parabolic / oscillatory / hybrid).

### P7 — Nonlinear Triad Coupling

The nonlinear term `M'(ρ)|∇ρ|²` generates higher-harmonic content, especially k=3 from k=1, with an invariant amplitude ratio under multiplicative perturbations. Coupling strength is weak (~0.03); harmonic generation is 3–6% of fundamental. No mode locking, no chaos, no bifurcations.

This is the spectral fingerprint of ED: any PDE architecturally ED generates the same harmonic-ratio invariant from its nonlinear term.

---

## 3. Universal invariants (00.3)

The unified PDE `∂t ρ = D·F[ρ] + H·v` admits several universal invariants that do not depend on dimension, mixing ratio, functional-form details, or initial condition:

- **Unique equilibrium** `ρ*` — global attractor across all `D ∈ [0,1]`.
- **Ground state energy** `E_ground = αγρ₀` — dimension-, regime-, and IC-independent.
- **Relaxation timescale** `t_rel ≈ ρ₀/(αγ)` — varies only ~13% across the full hybrid parameter space.
- **Oscillation-death threshold** `D_crit(ζ) ≈ 0.896` at canon-default `ζ = 1/4` — sharp (corrected 2026-04-22; see `D_crit_Resolution_Memo.md`).
- **Triad coupling coefficient** `C ≈ 0.03` — measured in ED-Phys-16.
- **Harmonic-generation ratio** ~3–6% of fundamental.
- **Quality factor** `Q ≈ 3.5` in the oscillatory sector.
- **Transient oscillation count** `N_osc ≈ 9` before decay in the oscillatory sector (8–19 observed in ED-Phys-17).

These are architectural, not empirical — they are consequences of P1–P7, not fit parameters.

---

## 4. Three regimes

The discriminant P6 partitions the parameter space into three qualitatively distinct dynamical sectors:

| Regime | Condition | Behavior |
|---|---|---|
| **Oscillatory** | `D < 0.1` (or `Δ < 1`) | Underdamped, reversible, standing participation waves. |
| **Transitional / Hybrid** | `0.1 ≤ D ≤ 0.4` | Mixed behavior; smooth interpolation between sectors. |
| **Parabolic** | `D ≥ 0.5` (or `Δ > 1`) | Overdamped, irreversible, structure-forming. Peak merging, basin formation, horizon dynamics. |

The Bulk vs. Near-Horizon architectural insight from 00.3: **in the bulk, mobility is high, diffusion dominates, parabolic behavior. Near the ceiling (`ρ → ρ_max`), mobility collapses, inertia dominates, oscillatory behavior.** The same PDE produces both limits; they are two layers of one architecture, not two different theories.

---

## 5. Canonical equivalence class

A PDE is **architecturally ED** if and only if it satisfies all seven principles P1–P7 (and implicitly the four ED-05 pre-PDE axioms on the underlying domain). Two PDEs with different functional forms `M`, `P`, or parameter values but satisfying the same Canon are architecturally **identical**:

- the same eight motifs (saddle / spiral / horizon / manifold / boundary / memory loop / dissipator / nonlinear triad)
- the same nine laws (unique attraction, finite capacity, harmonic protection, etc.)
- the same geometric objects (attractor point, stable manifold, spiral sheet, horizon surface, boundary surface, modal decay funnel, triad locus, monotonic cone)
- the same universal invariants (§3 above)

This is the architectural meaning of *equivalence*: **different equations, same architecture**. What can vary without breaking the Canon:

- Specific shape of `M(ρ)` (as long as `M(ρ_max) = 0`)
- Specific form of `P(ρ)` (as long as `P(ρ*) = 0` with `P' > 0`)
- Parameter values `D ∈ [0,1]`, `ζ ≥ 0`, `τ > 0`, `ρ_max > ρ*`
- Domain geometry (1D, 2D, 3D; periodic / reflective / open)
- Time rescaling and multiplicative factors on the operator

What cannot vary:
- The three-term operator structure (P1)
- The `D + H = 1` dual channel (P2)
- The unique monotone equilibrium (P3)
- The mobility capacity bound (P4)
- The participation feedback loop (P5)
- The damping discriminant threshold (P6)
- The triad coupling (P7)

---

## 6. Connection to the ontology: what is ED, in one sentence

From the emergence-map (ED-10) and the dictionary in `ED-Orientation.md` §5:

> Space = stable participation adjacency. Time = commitment order. Distance = participation resistance. Curvature = ED gradient structure. Horizons = decoupling surfaces. Geometry = coarse-grained participation. Einstein's equations = large-scale summary of ED gradients. Schrödinger evolution = thin-regime participation dynamics.

These equivalences are how the architectural machinery above connects to physical phenomena. They are not axioms of the Canon — they are consequences of its coarse-grained behavior in regimes where participation is thick, dense, and stable.

---

## 7. Four primitives + seven axioms (ED-13 synthesis)

ED-13 *Event Density as a Physical Ontology* (March 2026) summarizes the entire foundational structure in one phrase:

> From four primitives and seven axioms, the framework yields a unique scalar dynamical equation whose three channels correspond exactly to familiar physical laws: nonlinear diffusion, exponential relaxation, and telegraph-type oscillation.

Reading this carefully:

- **Four primitives** — the four ED-05 pre-PDE axioms (non-negativity, null baseline, monotonicity, subadditivity), OR equivalently the four ontological primitives (micro-events, ED gradients, participation, commitment). Either reading is internally consistent.
- **Seven axioms** — the seven Canon principles P1–P7 above.
- **Unique scalar dynamical equation** — the coupled `ρ̇ / v̇` system of 00.3.
- **Three channels correspond exactly to** — the mobility channel reduces to the porous-medium equation (nonlinear diffusion), the penalty channel reduces to Debye / RC exponential relaxation, and the participation channel reduces to the telegraph / RLC damped oscillator. See [`PDE.md`](PDE.md) §4 for the specific reductions.

This is why the ED framework claims **architectural uniqueness**: given the primitives and axioms, the PDE is not one choice among many; it is the only evolution equation consistent with the structural commitments.

---

## 8. What this document is not

- **Not a derivation** of the Canon from first principles (that is in the Architectural Canon paper — 00.2 — on the user's Desktop and on PhilArchive).
- **Not an empirical statement** — P1–P7 are structural axioms, not empirical findings. Empirical tests of ED live in `/papers/Universal_Mobility_Law/`, `/papers/Cluster_Merger_Lag_Evidence/`, and the ED-04.5 / ED-13 dwarf and weak-lensing claims summarized in `ED-Orientation.md` §7.
- **Not a replacement** for [`PDE.md`](PDE.md). PDE.md is the concrete instantiation of the Canon using specific functional forms (`M(ρ) = M₀(ρ_max − ρ)^β`, `P(ρ) = P₀(ρ − ρ*)` in the linear near-equilibrium simplification). This document is the architectural layer that explains *why* PDE.md has the structure it has.

---

*Cross-reference: For a complete paper-by-paper map of the ED series and how this Canon fits in, see `../docs/ED-Orientation.md`. For the canonical PDE instantiation, see [`PDE.md`](PDE.md).*
