# NS-2 — Substrate → Continuum Coarse-Graining (Scoping)

**Date:** 2026-04-30
**Status:** Active scoping. NS-2 of the Navier-Stokes roadmap. Form-derivation arc.
**Companions:** [`Navier_Stokes_Roadmap_Scoping.md`](../Navier_Stokes_Roadmap_Scoping.md), [`NS-1.05_Synthesis_B2_Verdict.md`](NS-1.05_Synthesis_B2_Verdict.md).

---

## 1. Purpose of NS-2

NS-2 is the **form-derivation arc** of the Navier-Stokes roadmap: derive the effective continuum fields — velocity, density, pressure, stress tensor — and their evolution equations from ED substrate primitives + d = 3 spatial geometry.

NS-2 inherits the following from NS-1's closure:

- **No PDE-level forcing route.** NS-1.02 closed Route 2.2 failed: T18 does not force sharp Huygens, is dimension-agnostic, and tolerates Hadamard interior-supported retardation. NS-2 cannot route any structural argument through a putative PDE-level dimensional commitment.
- **Substrate-level dimensional footing.** NS-1.04 partial-closed Route 2.4 with architectural d ≥ 3 (T20 mechanism degeneracy at d ≤ 2) and empirical-consistency d ≤ 3 (T19/T20 outputs match observed gravity at d = 3). NS-2 operates in d = 3 with this footing as a working substrate-level commitment.
- **Architectural-suggestive upper bound.** NS-1.03 partial-closed Route 2.3 with three concordant primitive-anchored mechanisms for d ≤ 3 (Polya recurrence + concentration of measure + decoupling-surface degeneration). NS-2 inherits the d ≤ 3 conclusion as a working architectural assumption.
- **Path B-strong as working dimensional assumption.** B2 closure is multi-layered (architectural d ≥ 3 + architectural-suggestive d ≤ 3 + empirical-consistency d ≤ 3). NS-2 should not produce or assume any structure that would require d > 3 viability.

The key methodological constraint: **NS-2 must not assume any continuum PDE structure a priori.** The Navier-Stokes form must emerge from substrate-level coarse-graining. If the form does not emerge cleanly, the failure point should be honestly diagnosed rather than papered over.

---

## 2. Inputs to NS-2

### 2.1 Substrate primitives carried into NS-2

| Primitive | Role in NS-2 |
|---|---|
| P02 (chain) | Timelike worldlines parameterized by proper time. Foundation for substrate-level momentum, position, and trajectory. |
| P04 (bandwidth additivity) | Bandwidth content as additive scalar at commitment events. Carries internal-energy-analog content. |
| P11 (commitment-irreversibility) | Forward-only chain dynamics; carried over from T18 / Arc B as a structural property of chain evolution. |
| P13 (proper-time intervals) | Finite intervals between commitment events. Sets time-scale of substrate dynamics; relevant for diffusion-coefficient identification. |
| Q.8 / UV-FIN (substrate cutoff ℓ_P) | UV cutoff at substrate scale. Critical for NS-3 (smoothness preservation) but enters NS-2 via the participation-count bound on coarse-graining cells. |
| ED-06 (decoupling surfaces) | Boundary structures; relevant for boundary conditions in NS form. |
| ED-07 (signal propagation, finite c) | Finite-speed propagation; constrains causal structure of substrate-level momentum transfer. |
| ED-10 (relational adjacency, spacetime emergence) | Participation neighborhoods. The locus where coarse-graining happens. |

### 2.2 Already-closed structural results carried into NS-2

| Result | Role in NS-2 |
|---|---|
| Arc M (mass-form mediation) | Identifies inertial mass as a chain property; supplies the m in (ρ = chain mass density) and in momentum p = ρv. |
| Arc N + T18 (V1 retarded vacuum kernel) | Cross-chain participation overlap structure; load-bearing for stress-tensor derivation (NS-2.05) and viscosity origin (NS-2.06). |
| Arc Q + T17 (gauge structure) | Not directly load-bearing for NS-2 unless NS-2 needs to handle EM-coupled fluids; flagged as potentially relevant for future MHD extensions, not for the core NS-2 derivation. |
| T19 (substrate → Newton, holographic bound, ℓ_P forced) | **Methodological template.** T19's substrate→continuum coarse-graining is the model for NS-2's substrate→continuum step. |
| T20 + Combination Rule + T21 (a₀, deep-regime, BTFR) | Not directly load-bearing for NS-2; relevant only if NS extends to gravitating fluids in deep-regime. Flagged for future hydrodynamic-with-gravity extensions. |

### 2.3 Geometry inputs (d = 3 spatial)

| Input | Origin |
|---|---|
| Cosmic horizon as $S^2$ at radius c/H₀ | NS-1.04 dimensional footing |
| Holographic 2-sphere boundary scaling 4πr² | T19 / NS-1.04 |
| Spherical-harmonic decomposition on $S^2$ | T20 / NS-1.04 |
| 3D vector calculus (∇, ∇·, ∇×, ∇²) | Standard d = 3 |

### 2.4 What NS-2 must not assume

- **No NS form a priori.** NS-2 cannot assume ∂_t v + (v·∇)v = −∇p + ν∇²v as a starting point. It must derive it.
- **No specific equation of state a priori.** NS-2 cannot assume p = p(ρ) or any specific functional form for pressure.
- **No specific viscosity coefficient a priori.** ν must emerge structurally from chain-substrate properties.
- **No incompressibility a priori.** ∇·v = 0 (if relevant) must emerge from substrate-level conservation, or NS-2 must derive a compressible-NS form first and identify the incompressible limit.
- **No Reynolds-stress closure ansatz.** If turbulent closure is needed in any sub-step, ED must produce its own closure structurally.
- **No higher-derivative regularization a priori.** ℓ_P-scale regularization (if it appears in the continuum limit) must be derived, not inserted.

---

## 3. Target Outputs of NS-2

### 3.1 Continuum fields

The four continuum fields NS-2 must derive from substrate primitives:

| Field | Substrate-level identification (working) |
|---|---|
| Velocity v(x, t) | Chain center-of-mass velocity, averaged over participation neighborhood at (x, t) above ℓ_P. |
| Density ρ(x, t) | Chain mass density (per Arc M), counted in participation neighborhood at (x, t). |
| Pressure p(x, t) | Substrate-level analog of momentum-flux contribution beyond bulk velocity transport. Specific structural content **to be derived**, not assumed. |
| Stress tensor T_ij(x, t) | Coarse-grained chain-momentum-flux tensor including pressure, viscous, and (potentially) ED-specific contributions. |

The "working" identifications for v and ρ are the natural ones; they should be confirmed at NS-2.01 / NS-2.02. The identifications for p and T_ij are **target outputs**, not inputs — they are what NS-2.04 / NS-2.05 must produce.

### 3.2 Target evolution equations

NS-2 closes when the following equations emerge from substrate-level coarse-graining:

**Continuity equation (NS-2.03 target):**
$$\partial_t \rho + \nabla \cdot (\rho v) = 0.$$

**Momentum balance (NS-2.04–NS-2.06 target):**
$$\partial_t v + (v \cdot \nabla) v = -\frac{1}{\rho} \nabla p + \nu \nabla^2 v + f_\mathrm{ED} + f_\mathrm{ext},$$

where:
- the pressure-gradient term emerges from the equilibrium part of the stress tensor,
- the ν∇²v viscous term emerges from cross-chain momentum transfer (Arc N V5 / participation-overlap structure),
- $f_\mathrm{ED}$ is any ED-specific term that emerges (history-dependent, retardation-induced, or substrate-cutoff-induced) — *NS-2 must report whether such terms appear and what their character is*,
- $f_\mathrm{ext}$ is external forcing if applicable.

**Equation of state (implicit in NS-2.05–NS-2.06):** NS-2 must derive the relation between p and (ρ, v, additional substrate-level quantities) that closes the system. NS-2 cannot assume the standard barotropic p = p(ρ) form a priori.

### 3.3 What NS-2 must identify, not just derive

- **Which coefficients are structural vs emergent.** ν, the bulk viscosity (if any), the equation-of-state coefficients — each must be classified as either fixed by substrate constants (structural) or as INHERITED at the form-derivation level (emergent, value-set-by-empirical-input). Form-FORCED / value-INHERITED is the canonical methodology; NS-2 follows it.
- **Whether ED-specific terms beyond standard NS appear.** If retarded V1 structure (T18) generates a memory-kernel correction to viscous transport, that term should be reported even if it is small. The deliverable is honest characterization of ED's NS, not a forced match to standard NS.
- **The continuum-limit regime.** At what scales does the substrate→NS coarse-graining hold? Above ℓ_P trivially; what is the upper-scale limit? Cosmic-horizon scale, or smaller? This affects what NS-3 inherits.

---

## 4. Methodological Template (T19-style)

NS-2 follows the methodological pattern of T19's substrate→Newton derivation, adapted for hydrodynamic content. T19's pattern:

1. Identify substrate-level conserved quantity (chain count / bandwidth content per region).
2. Identify the substrate-level "field" the conserved quantity sources (cumulative-strain reading on Σ).
3. Identify the boundary-scaling (holographic 2-sphere bound).
4. Combine to derive the continuum form (a = GM/r²).

NS-2's analogous pattern, in seven steps mapped to the seven memos:

1. **Identify substrate-level conserved quantities** (NS-2.01). Chain count, chain mass (Arc M), chain bandwidth content (P04), chain momentum (P02 + Arc M). Chain energy is implicit in bandwidth + kinetic content. Establish which conservation laws hold at substrate level under coarse-graining.

2. **Identify participation-weighted fluxes** (NS-2.02). For each conserved quantity, define the substrate-level flux through a participation-neighborhood boundary. Use ED-10's relational adjacency to define "boundary of a coarse-graining cell" without imposing a-priori-geometric bias. The flux is integrated over the cell boundary (analog of T19's holographic surface integration).

3. **Coarse-grained continuity equation** (NS-2.03). Mass conservation under coarse-graining yields ∂_t ρ + ∇·(ρv) = 0 directly, provided chain count is conserved at substrate level (subject to substrate-level chain creation/annihilation rates being negligible at coarse-grained scales — this assumption is to be checked, not assumed). Form-derivation step; should follow cleanly from NS-2.01–NS-2.02.

4. **Momentum-balance structure** (NS-2.04). Coarse-grained chain momentum gives ∂_t (ρv) + ∇·T = ρf_ext, where T is the chain-momentum-flux tensor. The NS form requires identifying T's decomposition. This memo writes down the bare momentum balance; the decomposition is for NS-2.05.

5. **Stress-tensor structure** (NS-2.05). Decompose T into:
   - bulk momentum transport ρv⊗v (dynamic),
   - pressure-like equilibrium part (isotropic, scalar p),
   - viscous (deviatoric, gradient-of-velocity-dependent),
   - ED-specific (if any — retarded-V1-induced memory terms, substrate-cutoff regularization, etc.).
   Each component must be identified from substrate-level chain-pair correlation structures. **This is one of the load-bearing-hard memos; stall risk concentrated here.**

6. **Viscosity / dissipation derivation** (NS-2.06). Origin of ν from cross-chain participation overlap (Arc N V5 / vacuum-kernel-mediated correlations). The viscous term ν∇²v should emerge from coarse-graining the chain-pair correlation structure that V5 articulates. *This is the other load-bearing-hard memo; the participation-overlap structure here connects directly to the diffusion-coarse-graining identification gap from NS-1.03 §3.2.*

7. **NS form synthesis** (NS-2.07). Combine NS-2.03 + NS-2.04 + NS-2.05 + NS-2.06 into the full NS form. Identify ED-specific deviations from standard NS (if any). Classify each coefficient as form-FORCED / value-INHERITED. Hand off to NS-3 (smoothness preservation).

This pattern directly mirrors the standard Boltzmann-equation-style hydrodynamic derivation in kinetic theory, but with chain primitives in place of molecules and participation-overlap structure in place of binary collision integrals. The structural fidelity to T19 is at the level of "substrate quantity → boundary-flux integration → continuum form"; the specific machinery (participation-neighborhood coarse-graining; chain-pair correlation expansion) is hydrodynamic-specific.

---

## 5. Architectural Questions NS-2 Must Answer

These are the questions whose answers determine whether NS-2 closes affirmatively, partial-closes, or fails. They should be addressed across the seven memos and consolidated in NS-2.07.

### 5.1 Velocity and pressure correspondences

- What substrate structure is the natural "velocity field" v(x, t)? Working: chain center-of-mass velocity averaged over a participation neighborhood. Confirm in NS-2.01.
- What substrate structure is the natural "pressure" p(x, t)? Working candidates:
  - ⟨ρ δv δv⟩ / 3 (kinetic-pressure analog, second moment of chain velocity fluctuations).
  - Bandwidth-content-density gradient contribution (if bandwidth couples to spatial extent).
  - Chain participation-overlap contribution (cross-chain stability landscape gradient).
- The choice between these candidates is structurally consequential. NS-2.05 must adjudicate.

### 5.2 Chain-level momentum transfer coarse-graining

- How does P02 + Arc M chain momentum transfer at substrate level coarse-grain to bulk-fluid momentum transfer? The natural picture: chain-pair participation-overlap mediates momentum exchange; coarse-graining yields a stress tensor. Specific structure depends on chain-pair correlation structure (Arc N).
- Does momentum transfer remain local under coarse-graining (giving local NS form), or does retarded V1 structure (T18) introduce non-local memory terms (giving NS form + memory kernel)?

### 5.3 Origin of viscosity in ED

- ν emerges from cross-chain participation-mediated momentum transfer. The substrate-level expression for ν depends on:
  - chain density,
  - chain-pair participation overlap as a function of separation (Polya-class scaling at coarse-grained scales — connects to NS-1.03 §3.2),
  - retardation kernel structure (T18).
- The dimensional analysis (already at hand): ν has units of m²/s. Substrate constants give ν ~ ℓ_P² · (substrate frequency) or ν ~ c · ℓ_P (kinetic-theory analog). Specific prefactor is for NS-2.06 to derive.
- **Risk flag:** if the diffusion-coarse-graining theorem (queued from NS-1.05 §6) is required to derive ν cleanly, NS-2.06 may stall pending that follow-on. NS-2.06 should attempt the derivation and report explicitly whether it can close without the diffusion theorem or whether it can only deliver a conditional result.

### 5.4 Stress-tensor uniqueness

- Does ED produce a *unique* stress-tensor form, or are multiple forms admissible? Standard fluid mechanics has the Stokes hypothesis (bulk viscosity = -2/3 shear viscosity for Newtonian fluids); ED may produce its own constraint or leave bulk viscosity free.
- If multiple admissible forms, NS-2.05 must report what fixes the choice (empirical match or additional substrate articulation).

### 5.5 ED-specific correction terms

- Does retarded V1 structure (T18) generate a memory-kernel term in viscous transport at coarse-grained scales? The natural form would be:
  $$\sigma_{ij}^\mathrm{visc}(t) = \int_{-\infty}^{t} K(t - t') \nabla_{(i} v_{j)}(t') \, dt',$$
  where K is a retardation kernel inheriting from V1. Whether K coarse-grains to a delta function (recovering instantaneous Newtonian viscosity) or retains finite memory at coarse-grained scales is a structural question.
- Does the ℓ_P substrate cutoff produce a higher-derivative regularization at the form level? Candidate: a term like $\ell_P^2 \nabla^4 v$ in the momentum equation, suppressing dynamics below ℓ_P. This is structurally important for NS-3 (it would automatically prevent finite-time singularities at substrate scale).

### 5.6 Closure assumptions

- What assumptions are required for NS-2 to close (pressure equation of state; form of cross-chain correlation function; coarse-graining-cell-size-independence)? Each assumption should be stated explicitly; assumptions that depend on observed phenomenology are empirical-consistency-conditional and should be flagged accordingly.

---

## 6. Dependencies and Risks

### 6.1 NS-1 dependencies

- **d = 3 footing** (NS-1.04 / NS-1.05): assumed throughout. NS-2 does not re-litigate dimensionality.
- **Substrate primitive d-agnosticism** (NS-1.04 §2.4): confirmed for the primitive set. NS-2 inherits this.
- **Architectural-suggestive d ≤ 3** (NS-1.03): inherits as working assumption; NS-2 should not produce structures that require d > 3 viability.
- **No PDE-level dimensional commitment** (NS-1.02): NS-2 may not appeal to T18 or any other kernel-level result for dimensional commitment.

### 6.2 New primitive-level articulation needed

| Articulation | Status | Required for memo |
|---|---|---|
| Coarse-grained chain center-of-mass velocity, formal definition | Implicit in P02 + ED-10; should be made explicit as a derived quantity | NS-2.01 |
| Participation-neighborhood as coarse-graining cell, formal definition | Implicit in ED-10 + Q.8; should be formalized | NS-2.01, NS-2.02 |
| Chain-pair correlation function under coarse-graining | Adjacent to Arc N V5 work; may need explicit formulation for NS-2 | NS-2.05, NS-2.06 |
| Cross-chain participation-overlap as a function of separation | Adjacent to Polya identification gap (NS-1.03 §3.2) | NS-2.06 |

The first two are formalization-of-implicit-content tasks (small to moderate). The third and fourth are the load-bearing items; they connect to the queued diffusion-coarse-graining future arc.

### 6.3 Stall-risk loci within NS-2

- **NS-2.05 (stress-tensor structure).** Stress-tensor uniqueness, pressure identification, and ED-specific term identification all converge here. Probable site of multiple structural decisions where ED's substrate may admit multiple admissible forms; closing requires either an additional structural argument or empirical-match input.
- **NS-2.06 (viscosity origin).** If clean viscosity derivation requires the diffusion-coarse-graining theorem (queued from NS-1.05), NS-2.06 may produce only a conditional result pending that theorem. Honest reporting of this dependency is essential.

NS-3 (smoothness preservation) remains the absolute peak stall-risk locus in the program. NS-2's stall risk is moderate by comparison — most NS-2 memos are direct adaptations of T19-style coarse-graining, with NS-2.05 / NS-2.06 the exceptions.

### 6.4 What is *not* a risk for NS-2

- The dimensional question (closed in NS-1).
- Singularity formation at substrate scale (forbidden by ℓ_P cutoff per Q.8).
- The Clay smoothness problem (NS-3 territory).
- Stress-tensor existence in the abstract (NS-2.04 establishes momentum-balance form; NS-2.05 fills in T's structure; existence is given by momentum conservation at coarse-grained scale).

---

## 7. Deliverables for NS-2

| Memo | Title (working) | Load |
|---|---|---|
| NS-2.01 | Substrate Conserved Quantities + Coarse-Graining Cell Articulation | Foundation; defines what is being conserved. |
| NS-2.02 | Participation-Weighted Flux Derivation | Substrate-level flux through coarse-graining cell boundaries. |
| NS-2.03 | Coarse-Grained Continuity Equation | ∂_t ρ + ∇·(ρv) = 0 from substrate. |
| NS-2.04 | Momentum-Balance Equation | ∂_t (ρv) + ∇·T = ρf form from substrate. |
| NS-2.05 | Stress-Tensor Structure | Decomposition of T; pressure identification; ED-specific term audit. **Load-bearing-hard.** |
| NS-2.06 | Viscosity / Dissipation Derivation | Origin of ν from cross-chain correlations; possible memory-kernel term audit. **Load-bearing-hard; possibly conditional on diffusion theorem.** |
| NS-2.07 | NS Form Synthesis + Hand-off to NS-3 | Combine all above; classify coefficients form-FORCED / value-INHERITED; report ED-specific deviations from standard NS. |

Total estimated scope: seven memos. By analogy to the substrate-gravity arc (which produced ten arc-SG memos plus the ED Combination Rule memo plus T19/T20/T21), this is a comparable single-arc derivation effort. At demonstrated cycle pace, days-to-weeks per memo with NS-2.05 / NS-2.06 the slowest.

---

## 8. Recommended Next Steps

In priority order.

1. **Pre-arc check: confirm Arc M's mass derivation is in usable form for NS-2.** Specifically, confirm the inertial-mass identification at chain level (per Arc M, M.1–M.3 closure) is compatible with the "ρ = chain mass density" identification NS-2.01 will use. A quick read of the Arc M closure memos before NS-2.01 begins. If Arc M's mass is form-FORCED-value-INHERITED, NS-2 inherits the same status for ρ; this is the expected case but should be confirmed.

2. **Optional but recommended: produce the diffusion-coarse-graining future-arc scoping memo** before NS-2.06 is reached. File: `theory/Navier Stokes/Future_Arc_Diffusion_Coarse_Graining_Scoping.md` (or at `theory/` root). Reasoning: NS-2.06's viscosity-origin derivation may benefit substantially from the diffusion-coarse-graining theorem's machinery, even before the theorem is closed. Producing the scoping memo in parallel with early NS-2 memos lets the two arcs share infrastructure rather than NS-2.06 stalling pending an unscoped follow-on. Cheap; highly recommended.

3. **Draft NS-2.01 — substrate conserved quantities + coarse-graining cell articulation.** File: `theory/Navier Stokes/NS-2.01_Conserved_Quantities.md`. Three deliverables: (a) explicit definition of the participation-neighborhood-based coarse-graining cell at scale ℓ_cell > ℓ_P; (b) identification of conserved substrate quantities under coarse-graining (chain count, chain mass, chain momentum, chain bandwidth-content / energy); (c) derivation of substrate-level conservation laws for each (∂_t (substrate density) + (substrate flux) divergence = source/sink, where source/sink is to be evaluated). NS-2.01 should be the cleanest of the seven memos; it is the natural opening move.

4. **Draft NS-2.02 — participation-weighted flux derivation** following NS-2.01. File: `theory/Navier Stokes/NS-2.02_Participation_Fluxes.md`. Coarse-grain the substrate fluxes from NS-2.01 to continuum-level fluxes, using ED-10's relational adjacency to define cell-boundary integration without imposing a-priori-geometric bias. This is the substrate→continuum step that mirrors T19's holographic-bound integration. Once NS-2.02 closes, NS-2.03 (continuity) follows mechanically.

### Decisions for you

- **Confirm NS-2 scope** — seven memos as listed in §7, with NS-2.05 / NS-2.06 as the load-bearing-hard items? Alternative: split NS-2.05 into two memos (5a stress-tensor decomposition; 5b ED-specific term audit) if the audit work proves substantial.
- **Sequence the diffusion-scoping memo** — produce before NS-2.01 opens, in parallel with NS-2.01–NS-2.04 (the earlier memos), or only when NS-2.06 is reached? Recommend producing in parallel.
- **Confirm Path B-strong dimensional framing** is to be used throughout NS-2's writeups (matching NS-1.05's headline framing). Not strictly load-bearing for NS-2's structural content, but consequential for any externally-facing material that emerges from NS-2.

---

*NS-2 scoped. Form-derivation arc; methodologically T19-analog. Seven memos; NS-2.05 / NS-2.06 are the load-bearing-hard items. Diffusion-coarse-graining scoping memo recommended in parallel with early NS-2 work to share infrastructure. NS-2.01 (substrate conserved quantities + coarse-graining cell articulation) is the natural first memo. NS-2 stall risk moderate; NS-3 remains the absolute peak stall locus.*
