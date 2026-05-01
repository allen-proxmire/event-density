# NS-2.04 — Continuum Momentum-Balance Equation

**Date:** 2026-04-30
**Status:** Momentum balance derived in conservation form and material-derivative form. τ_ij carried forward as undecomposed placeholder; decomposition is NS-2.05's job. Mechanical from NS-2.01 + NS-2.02 + NS-2.03 inputs.
**Companions:** [`NS-2.01_Conserved_Quantities.md`](NS-2.01_Conserved_Quantities.md), [`NS-2.02_Participation_Fluxes.md`](NS-2.02_Participation_Fluxes.md), [`NS-2.03_Continuity.md`](NS-2.03_Continuity.md).

---

## 1. Purpose

NS-2.04 derives the continuum momentum-balance equation in two equivalent forms:

**Conservation form:**

$$\boxed{\partial_t (\rho v_i) + \partial_j \Pi_{ij} = \rho f_i^{\mathrm{ext}}, \qquad \Pi_{ij} = \rho v_i v_j + \tau_{ij}.}$$

**Material-derivative form (using NS-2.03 continuity):**

$$\boxed{\rho \, \frac{Dv_i}{Dt} = -\partial_j \tau_{ij} + \rho f_i^{\mathrm{ext}}, \qquad \frac{D}{Dt} = \partial_t + v_j \partial_j.}$$

τ_ij is carried forward as an undecomposed placeholder per NS-2.02 §3.1 / §6.2. The decomposition into pressure + viscous + ED-specific contributions is NS-2.05's job.

NS-2.04 also records the substrate-level constraints τ_ij must satisfy (symmetry, sign convention, trace placeholder) so that NS-2.05's decomposition operates within those constraints rather than imposing assumptions a priori.

---

## 2. Inputs from NS-2.01, NS-2.02, NS-2.03

| Input | Source | Role |
|---|---|---|
| Spherical coarse-graining cell, R_cg in (C1)∩(C2)∩(C3) window | NS-2.01 §2 | Spatial averaging volume, 2-sphere boundary |
| Substrate momentum conservation: ∂_t (ρv_i) + ∂_j Π_ij = ρf_i^ext | NS-2.01 §3.3, §4.3 | Generic conservation form |
| Momentum flux Π_ij = ρv_iv_j + τ_ij | NS-2.02 §5.3 / §6.2 | Substrate→continuum flux form |
| τ_ij = τ_ij^kin + τ_ij^V5 + τ_ij^V1-mem | NS-2.02 §3.1 | Three substrate-level contributions; not decomposed here |
| Continuity: ∂_t ρ + ∇·(ρv) = 0 | NS-2.03 §5 | Used in chain-rule manipulation |
| ρ(x,t), v(x,t) definitions | NS-2.01 §5 | Continuum field identifications |

---

## 3. Substrate Momentum Conservation → Cell-Averaged Form

### 3.1 Substrate-level statement

Total chain momentum in any spatial region Ω changes via three mechanisms: chains crossing the boundary ∂Ω carrying momentum (advective flux), chain-pair participation-overlap-mediated momentum exchange across ∂Ω (non-advective flux), and external forces acting on chains within Ω. At chain level (P02 + Arc M):

$$\frac{d}{dt} \left[\sum_{\mathrm{chains\ in\ }\Omega} m_\mathrm{chain} v_{\mathrm{chain}, i}\right] \;=\; -\Phi_i^{\partial\Omega} + F_i^{\mathrm{ext}}(\Omega),$$

where $\Phi_i^{\partial\Omega}$ is the i-component momentum flux outward through ∂Ω (advective + non-advective; per NS-2.02) and $F_i^{\mathrm{ext}}(\Omega)$ is the total external force on chains within Ω.

### 3.2 Cell-averaged form

Apply to the spherical coarse-graining cell at position x with radius R_cg. The cell momentum content is $\rho(x, t) v_i(x, t) V_\mathrm{cell}$ by NS-2.01 §5.2. Substituting:

$$V_\mathrm{cell} \, \partial_t (\rho v_i) \;=\; -\oint_{S^2(R_\mathrm{cg})} \Pi_{ij} \hat{n}_j \, dA + V_\mathrm{cell} \, \rho f_i^{\mathrm{ext}}.$$

Apply the divergence theorem to the boundary flux:

$$\oint_{S^2(R_\mathrm{cg})} \Pi_{ij} \hat{n}_j \, dA \;=\; \int_\mathrm{cell} \partial_j \Pi_{ij} \, dV \;\approx\; V_\mathrm{cell} \, \partial_j \Pi_{ij} \big|_{x, t}$$

in the small-cell limit. Cancelling V_cell on both sides:

$$\partial_t (\rho v_i) + \partial_j \Pi_{ij} \;=\; \rho f_i^{\mathrm{ext}}.$$

Substituting $\Pi_{ij} = \rho v_i v_j + \tau_{ij}$:

$$\partial_t (\rho v_i) + \partial_j (\rho v_i v_j + \tau_{ij}) \;=\; \rho f_i^{\mathrm{ext}}.$$

This is the **conservation form** of the momentum-balance equation. NS-2.05 will decompose τ_ij; until then, it is a placeholder identified at substrate level.

---

## 4. Chain-Rule Manipulation

Convert the conservation form to the material-derivative form using continuity (NS-2.03 §5).

### 4.1 Expand the time derivative

$$\partial_t (\rho v_i) = v_i \, \partial_t \rho + \rho \, \partial_t v_i.$$

### 4.2 Expand the advective divergence

$$\partial_j (\rho v_i v_j) = v_i \, \partial_j (\rho v_j) + \rho v_j \, \partial_j v_i.$$

### 4.3 Combine and apply continuity

Adding the two:

$$\partial_t (\rho v_i) + \partial_j (\rho v_i v_j) \;=\; v_i \big[\partial_t \rho + \partial_j (\rho v_j)\big] + \rho \big[\partial_t v_i + v_j \partial_j v_i\big].$$

The first bracket vanishes by continuity (NS-2.03 §5):

$$\partial_t \rho + \partial_j (\rho v_j) = 0.$$

The second bracket is the material derivative of v_i:

$$\partial_t v_i + v_j \partial_j v_i = \frac{D v_i}{Dt}.$$

Therefore:

$$\partial_t (\rho v_i) + \partial_j (\rho v_i v_j) \;=\; \rho \, \frac{D v_i}{Dt}.$$

### 4.4 Material-derivative momentum equation

Substituting back into the conservation form:

$$\rho \, \frac{D v_i}{Dt} + \partial_j \tau_{ij} = \rho f_i^{\mathrm{ext}},$$

i.e.,

$$\boxed{\rho \, \frac{D v_i}{Dt} = -\partial_j \tau_{ij} + \rho f_i^{\mathrm{ext}}.}$$

This is the **material-derivative form** of the momentum-balance equation. It is the form in which the standard NS equation is usually written (with τ_ij further decomposed as -p δ_ij + viscous-stress contributions). Decomposition is NS-2.05.

---

## 5. External Forces f_i^ext

The external-force term carries any force acting on chains beyond the chain-pair participation-overlap structure already contained in τ_ij. For NS regimes:

### 5.1 Gravity

Per T19's substrate→Newton derivation, gravity acts on chains via the cumulative-strain reading on the stability landscape Σ. At continuum level, the chain population in a cell experiences gravitational acceleration $g_i$ determined by the surrounding mass distribution:

$$f_i^{\mathrm{grav}} = g_i, \qquad \mathbf{g} = -\nabla \phi_\mathrm{grav},$$

with $\phi_\mathrm{grav}$ the Newtonian gravitational potential satisfying $\nabla^2 \phi_\mathrm{grav} = 4\pi G \rho_\mathrm{total}$ (per T19; G derived as $c^3 \ell_P^2 / \hbar$).

For laboratory-scale NS in Earth's gravity, $g_i \approx -g \delta_{i3}$ with g ≈ 9.8 m/s²; the gravitational contribution is approximately uniform over typical NS domains. For self-gravitating astrophysical NS (stellar interiors, accretion flows), $\mathbf{g}$ is computed from ρ via T19's mechanism.

In the deep-acceleration regime (a < a₀, T20 territory), the ED Combination Rule modifies gravity to the multiplicative form $a^2 = a_N \cdot a_0$ (T21 BTFR slope-4). This regime is irrelevant for typical laboratory and engineering NS but appears in galactic-scale hydrodynamics; flagged for future astrophysical-NS extensions.

### 5.2 Electromagnetic forces (charged fluids only)

Per T17 gauge-fields-as-rule-type structure, charged chains experience EM forces. Continuum form (Lorentz force density):

$$f_i^{\mathrm{EM}} = \frac{1}{\rho} \left[\rho_q E_i + (\mathbf{j} \times \mathbf{B})_i\right],$$

with $\rho_q$ the charge density and $\mathbf{j}$ the current density of charged chains. Operative for plasmas and MHD; not load-bearing for neutral-fluid NS.

### 5.3 Other forces — none operative at NS scales

- **Strong/weak nuclear forces.** Confined to ~10⁻¹⁵ m scales; vastly below NS resolution.
- **Inertial pseudoforces.** If the NS coordinate frame is non-inertial, Coriolis and centrifugal contributions appear; these are coordinate-induced rather than substrate-level forces and are added to f^ext at the application level.
- **Substrate-cutoff effects from ℓ_P.** Per Q.8 / T19, the substrate cutoff is below NS scales by tens of orders of magnitude; ℓ_P-scale forces do not appear in f^ext at NS scales. (However, ℓ_P may produce a higher-derivative regularization term in τ_ij itself; that question is for NS-2.05 / NS-2.06, not for f^ext.)

### 5.4 Aggregate

For NS regimes:

$$f_i^{\mathrm{ext}} = g_i + \frac{1}{\rho} \left[\rho_q E_i + (\mathbf{j} \times \mathbf{B})_i\right] + (\mathrm{coordinate\text{-}induced\ pseudoforces}).$$

For neutral fluids without EM coupling (the standard NS case), $f_i^{\mathrm{ext}} = g_i$.

---

## 6. τ_ij Placeholder Constraints

NS-2.04 records the substrate-level constraints τ_ij must satisfy. NS-2.05's decomposition must respect these.

### 6.1 Symmetry: τ_ij = τ_ji

**Forced at substrate level by chain-pair Newton's-third-law analog.** When chain A exchanges momentum with chain B via V5 participation overlap or V1-mediated coupling, the momentum gained by A equals the momentum lost by B (sign-flipped). Aggregating over all chain pairs in the cell, the off-diagonal contributions to τ_ij are antisymmetric under chain-pair index swap, which after summing produces a *symmetric* tensor in the spatial indices i, j.

Equivalently: angular momentum conservation at substrate level (a consequence of ED-10's rotational invariance of relational adjacency — no preferred spatial direction in the participation-overlap kernel) requires the stress tensor to be symmetric. An asymmetric τ_ij would correspond to an internal torque, which the substrate's rotational symmetry forbids.

**Status: forced at substrate level.** NS-2.05's decomposition must produce symmetric τ_ij in each component (kinetic, V5, V1-mem).

### 6.2 Sign convention

Π_ij is the *outward* momentum flux through a surface with normal in the j direction. By construction of the cell-boundary integration in NS-2.02 §4, positive Π_ij means i-momentum flowing in the +j direction.

τ_ij ≡ Π_ij - ρ v_i v_j is the non-advective part. For an isotropic compressive contribution (pressure) to act as a *push outward* on a fluid element, the pressure contribution to τ must be **+p δ_ij** with p > 0 for compression. Equivalently, the force per unit area on a surface element with outward normal $\hat{n}_j$ is **−τ_ij n_j** (the surroundings push *into* the element along the inward direction). This is the standard physics convention; NS-2.05 will use it.

**Status: convention fixed.** Pressure contribution to τ is +p δ_ij; viscous deviatoric contribution is conventionally written as -σ^visc with σ^visc the viscous stress.

### 6.3 Trace structure (placeholder, adjudicated in NS-2.05)

The trace $\mathrm{Tr}(\tau) = \tau_{ii}$ contains the *isotropic* part of the stress tensor — the pressure-like content. Generically:

$$\tau_{ii}/3 = p_\mathrm{eff}(x, t),$$

where $p_\mathrm{eff}$ is the effective pressure. The decomposition

$$\tau_{ij} = p_\mathrm{eff} \, \delta_{ij} + \tau_{ij}^\mathrm{dev}, \qquad \tau_{ii}^\mathrm{dev} = 0,$$

separates the isotropic and deviatoric parts. The deviatoric part contains the viscous stress + any ED-specific deviatoric contributions.

Whether $p_\mathrm{eff}$ corresponds cleanly to one of the three pressure candidates from NS-2.01 §5.3 (kinetic-pressure analog, bandwidth-density gradient, cross-chain stability landscape) or to a sum of them is the question NS-2.05 must answer.

**Status: placeholder.** NS-2.04 records the decomposition structure without fixing $p_\mathrm{eff}$.

### 6.4 Three substrate contributions, individually constrained

Per NS-2.02 §3.1: $\tau_{ij} = \tau_{ij}^\mathrm{kin} + \tau_{ij}^\mathrm{V5} + \tau_{ij}^\mathrm{V1-mem}$.

Each contribution must individually satisfy:

- Symmetry (per §6.1).
- Sign convention (per §6.2).
- A well-defined trace whose physical interpretation NS-2.05 will determine.

The three contributions may carry pressure-like, viscous, and ED-specific content in different proportions. NS-2.05's load-bearing-hard work is identifying which contribution carries which physical content.

---

## 7. Final Momentum-Balance Equation

**Conservation form:**

$$\partial_t (\rho v_i) + \partial_j (\rho v_i v_j + \tau_{ij}) = \rho f_i^{\mathrm{ext}}.$$

**Material-derivative form:**

$$\rho \, \frac{D v_i}{Dt} = -\partial_j \tau_{ij} + \rho f_i^{\mathrm{ext}}.$$

Both forms are equivalent given continuity (NS-2.03). The material-derivative form is the preferred form for downstream NS form derivation; the conservation form is preferred for numerical implementations and for boundary-condition / flux-conservation analyses.

### 7.1 Status in form-FORCED / value-INHERITED framework

- **Form FORCED.** The momentum-balance form ∂_t (ρv) + ∇·Π = ρf is forced by substrate-level momentum conservation (P02 chain momentum + Arc M chain-attribute mass + Newton's-third-law-analog at chain-pair level). No alternative form admits primitive-level construction.
- **τ_ij decomposition** is form-FORCED at the kinetic + V5 + V1-mem level (per NS-2.02). Whether it further decomposes cleanly into pressure + viscous + ED-specific is NS-2.05's question; pressure-decomposition status is currently *form-undecided*.
- **Value INHERITED.** Specific values of v(x, t), τ_ij(x, t), f^ext(x, t) at any point depend on initial conditions and applied boundary/forcing; not determined by form derivation.

### 7.2 What NS-2.04 has *not* delivered

Honest catalogue:

- **No decomposition of τ_ij.** Pressure, viscosity, ED-specific terms not separated. Awaits NS-2.05.
- **No equation of state.** The relation between ρ and any pressure-like content of τ is not derived. NS-2.05 / NS-2.06 / NS-2.07 territory.
- **No Reynolds stress / turbulent closure.** The chain-velocity-fluctuation second moment τ^kin is identified at substrate level but its functional form (in terms of mean fields) is not derived. NS-2.05.
- **No ν.** The viscosity coefficient is not derived. NS-2.06.

NS-2.04's role is to establish the equation's structural form; substantive content awaits the next memos.

---

## 8. Preconditions for NS-2.05

NS-2.05 (stress-tensor decomposition) will require:

1. **The bare momentum-balance equation** in conservation and material-derivative forms (this memo §7).
2. **τ_ij = τ_ij^kin + τ_ij^V5 + τ_ij^V1-mem** substrate-level identification (NS-2.02 §3.1).
3. **τ_ij placeholder constraints** (this memo §6): symmetry, sign convention, trace structure.
4. **Three pressure candidates** from NS-2.01 §5.3: kinetic-pressure analog (P-1), bandwidth-density gradient (P-2), cross-chain stability landscape (P-3). NS-2.05 adjudicates which contribute to which τ component.
5. **Arc N V5 memos** for explicit cross-chain participation-overlap structure. Required to derive τ_ij^V5 explicitly. **Not yet read; pre-NS-2.05 check.**
6. **T18 retarded-V1 structure** for τ_ij^V1-mem analysis. Already in hand from arc-B work read during NS-1.02 audit.

NS-2.05's deliverables (preview):

- Decomposition $\tau_{ij} = p \, \delta_{ij} + \tau_{ij}^\mathrm{visc} + \tau_{ij}^\mathrm{ED-specific}$ with each component's substrate origin identified.
- Pressure equation of state (form, with values INHERITED).
- Viscous stress functional form (Newtonian, non-Newtonian, or memory-kernel — to be reported).
- ED-specific term audit (memory-kernel from V1 retardation; substrate-cutoff from ℓ_P; both flagged in NS-2.02 §5.4).

---

## 9. Recommended Next Steps

In priority order. NS-2.04 closes mechanically; NS-2.05 is now the load-bearing-hard memo.

1. **Pre-NS-2.05 check: locate and read Arc N V5 memos** before NS-2.05 drafting begins. Glob over `arcs/arc-N/` for V5 content; also check whether V5 lives in `non_markov_forced.md` (cited in [`arrow_forced.md`](../../arcs/arc-B/arrow_forced.md) §3.5 as the source for N1-E cascade, suggesting V5 is in arc-N closure memos). Estimated 30–60 minutes; produces the explicit cross-chain participation-overlap structure NS-2.05 needs to derive τ_ij^V5. **Run this before NS-2.05 starts; if V5 content is sparse or distributed across multiple memos, NS-2.05 may need a sub-section consolidating it.**

2. **Draft NS-2.05 — stress-tensor decomposition.** File: `theory/Navier Stokes/NS-2.05_Stress_Tensor.md`. Load-bearing-hard memo. Three sub-tasks: (a) decompose τ_ij^kin into pressure + viscous + (no ED-specific) using kinetic-theory analog machinery; (b) decompose τ_ij^V5 into pressure + viscous + (possible ED-specific cross-chain term) using Arc N V5 content; (c) audit τ_ij^V1-mem for memory-kernel structure — does it coarse-grain to instantaneous viscosity (recovering standard NS) or retain finite memory time (ED-specific)? Adjudicate the three pressure candidates from NS-2.01 §5.3. Estimated 2–4 sessions; the longest single memo in NS-2.

3. **Optional, parallel: produce diffusion-coarse-graining future-arc scoping memo.** File: `theory/Navier Stokes/Future_Arc_Diffusion_Coarse_Graining_Scoping.md`. Reasoning unchanged from prior memos: NS-2.06 (viscosity origin) likely needs this theorem's machinery; NS-2.05's V5 work may surface inputs the diffusion theorem could use. Producing scoping early lets infrastructure share. Cheap, recommended now.

4. **Status checkpoint at NS-2.04 close.** Four memos closed (NS-2.01 through NS-2.04); three remaining (NS-2.05, NS-2.06, NS-2.07). The two load-bearing-hard memos are next; NS-2 stall risk concentrated there. Reasonable to pause for status-summary if external-facing material is desired before NS-2.05.

### Decisions for you

- **Confirm Arc N V5 location pre-NS-2.05.** Recommended one-minute Glob over `arcs/arc-N/` to pin V5 memo location before NS-2.05 begins. If V5 is well-localized in one memo, NS-2.05 incorporates it directly; if distributed, NS-2.05 needs a small consolidation step.
- **Confirm proceeding to NS-2.05 directly**, or pause for status-summary/external-facing material at the four-memos-closed mark.

---

*NS-2.04 derives ∂_t (ρv_i) + ∂_j (ρv_iv_j + τ_ij) = ρf_i^ext mechanically from substrate momentum conservation + NS-2.02's flux form. Material-derivative equivalent ρ(Dv_i/Dt) = -∂_j τ_ij + ρf_i^ext via continuity. τ_ij carried as undecomposed placeholder with three substrate-level contributions (kinetic, V5, V1-mem) and three constraints (symmetry forced, sign convention fixed, trace structure decomposable into isotropic pressure + deviatoric). External force f^ext = gravity (T19) + EM (T17, charged fluids) + coordinate-induced pseudoforces; no substrate-level forces beyond these at NS scales. NS-2.05 (stress-tensor decomposition) is the next memo and the longest in NS-2; NS-2.06 (viscosity origin) will follow.*
