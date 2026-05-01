# NS-2.02 — Participation-Weighted Flux Derivation

**Date:** 2026-04-30
**Status:** T19-analog substrate→continuum step. Derives fluxes of all four conserved quantities across the coarse-graining cell boundary; produces flux expressions that feed NS-2.03 (continuity) and NS-2.04 (momentum balance) directly. Does not decompose the stress tensor τ — that is NS-2.05's job.
**Companions:** [`NS-2.01_Conserved_Quantities.md`](NS-2.01_Conserved_Quantities.md), [`NS-2_Scoping.md`](NS-2_Scoping.md).

---

## 1. Purpose

NS-2.02 derives the substrate-level fluxes of the four conserved quantities established in NS-2.01:

- chain count n,
- mass ρ,
- momentum ρv,
- bandwidth-content / energy e,

across the boundary of the coarse-graining cell, and converts them to continuum flux forms in the substrate→continuum scaling limit. This is the methodological analog of T19's holographic-bound integration: substrate-level chain-by-chain accounting → continuum-level field flux via 2-sphere boundary integration.

The output of NS-2.02 is a set of explicit continuum flux expressions:

- $\mathbf{J}_\rho = \rho \mathbf{v}$ (mass flux)
- $\Pi_{ij} = \rho v_i v_j + \tau_{ij}$ (momentum-flux tensor; τ structure deferred to NS-2.05)
- $\mathbf{J}_e = e \mathbf{v} + \mathbf{Q} + \mathbf{v} \cdot \tau$ (energy flux)

with the stress tensor τ identified as the locus of all non-advective momentum transport, to be decomposed downstream.

---

## 2. Inputs from NS-2.01

Required inputs, all established in NS-2.01:

| Input | Role |
|---|---|
| Spherical coarse-graining cell, radius R_cg | Cell geometry; boundary is a 2-sphere of area 4πR_cg² |
| (C1)∩(C2)∩(C3) constraints on R_cg | Defines the scaling-limit window |
| Participation-neighborhood as cell content | Set of chains with non-trivial participation overlap within radius R_cg |
| Conserved-quantity inventory: n, ρ, ρv, e | The four quantities whose fluxes are derived here |
| Substrate-level conservation laws | Generic ∂_t(density) + ∇·(flux) = source/sink form |
| ρ(x, t) = (1/V) Σ m_chain | Mass-density definition |
| v_i(x, t) = (1/(ρV)) Σ m_chain v_chain,i | Mass-weighted average velocity |

Pressure p is *not* an input here — it is a derived component of τ in NS-2.05. NS-2.02 produces the bare momentum-flux tensor; the pressure-vs-viscous decomposition follows downstream.

---

## 3. Participation-Weighted Transport Rules

For each conserved quantity, two distinct transport channels exist at substrate level:

- **Advective transport** — quantity is carried bodily by chain motion. Chains crossing the cell boundary at velocity $v_\mathrm{chain}$ carry whatever they hold (mass, momentum, bandwidth content) across with them. Direct from P02 timelike-worldline structure.
- **Non-advective transport** — quantity is exchanged between chains via participation overlap (V5 cross-chain correlations from Arc N) without requiring chain bodies to physically cross the boundary. Bandwidth content updates per P04 mediate this channel; the V1 retarded vacuum kernel (T18) supplies the propagation structure.

Both channels are operative at substrate level. Both must be integrated across the cell boundary to produce the continuum flux. The relative magnitude of advective vs. non-advective contributions varies by quantity:

- Chain count: advective only (chain bodies must physically cross the boundary; participation overlap doesn't transfer chain identity).
- Mass: advective only (mass is rigidly attached to chains per Arc M; no non-advective channel).
- Momentum: *both*. Advective gives ρv⊗v; non-advective gives the entire stress tensor τ.
- Bandwidth content: *both*. Advective gives e v; non-advective gives the heat flux Q.

### 3.1 Transport rules per quantity

**Chain count.** Chain crosses the cell boundary surface element dA per unit time at rate $n \, v_\mathrm{chain} \cdot \hat{n} \, dA$, where $\hat{n}$ is the outward unit normal. Cell-averaged transport rule:

$$\mathbf{J}_n = n \mathbf{v}_\mathrm{chain-avg} = n \mathbf{v}.$$

(Mass-weighted v ≈ chain-average v when chains have equal mass; for multi-species fluids the two diverge by the species distribution but the chain-count flux remains advective in form.)

**Mass.** Each chain carries mass m_chain rigidly. Per chain crossing the boundary:

$$dM/dt = m_\mathrm{chain} \, v_\mathrm{chain} \cdot \hat{n} \, dA.$$

Cell-averaged:

$$\mathbf{J}_\rho = \frac{1}{V_\mathrm{cell}} \sum_\mathrm{chains} m_\mathrm{chain} \mathbf{v}_\mathrm{chain} = \rho \mathbf{v}.$$

By construction (NS-2.01 §5.2), this is the mass-weighted average product, which equals ρv exactly.

**Momentum.** Each chain carries momentum $m_\mathrm{chain} v_{\mathrm{chain}, i}$, transported advectively at velocity $v_{\mathrm{chain}, j}$. Advective contribution to the i-component flux through normal direction j:

$$\Pi_{ij}^\mathrm{adv} = \frac{1}{V_\mathrm{cell}} \sum_\mathrm{chains} m_\mathrm{chain} v_{\mathrm{chain}, i} v_{\mathrm{chain}, j}.$$

Decompose chain velocities as $v_{\mathrm{chain}, i} = v_i(x, t) + \delta v_{\mathrm{chain}, i}$ where $v_i$ is the cell-mean velocity and $\delta v_\mathrm{chain}$ is the chain's residual velocity fluctuation. The advective stress decomposes:

$$\Pi_{ij}^\mathrm{adv} = \rho v_i v_j + \frac{1}{V_\mathrm{cell}} \sum_\mathrm{chains} m_\mathrm{chain} \delta v_{\mathrm{chain}, i} \delta v_{\mathrm{chain}, j}.$$

The first term is the bulk-flow advection. The second term is the **kinetic-stress contribution** $\tau_{ij}^\mathrm{kin}$ — a substrate-level analog of the kinetic-theory pressure tensor. This is candidate **(P-1)** from NS-2.01 §5.3 emerging naturally as part of the momentum-flux decomposition.

Non-advective momentum transport: chains within the cell exchange momentum with chains outside the cell via cross-chain participation overlap (V5) and via the V1 retarded vacuum kernel (T18). The rate of momentum exchange across the boundary involves an integration of the cross-chain interaction kernel over chain-pair separations near the boundary. Schematically:

$$\Pi_{ij}^\mathrm{non-adv} = \tau_{ij}^\mathrm{V5} + \tau_{ij}^\mathrm{V1-mem},$$

where $\tau_{ij}^\mathrm{V5}$ is the cross-chain participation-overlap contribution (Arc N V5-mediated) and $\tau_{ij}^\mathrm{V1-mem}$ is any retardation-induced memory-kernel contribution that survives the substrate→continuum limit (load-bearing-uncertain; deferred to NS-2.06's audit).

**Total momentum flux:**

$$\Pi_{ij} = \rho v_i v_j + \tau_{ij}, \qquad \tau_{ij} = \tau_{ij}^\mathrm{kin} + \tau_{ij}^\mathrm{V5} + \tau_{ij}^\mathrm{V1-mem}.$$

NS-2.02 establishes this structural form. The decomposition of τ into pressure + viscous + ED-specific is NS-2.05's job.

**Bandwidth content / energy.** Each chain carries kinetic energy $\frac{1}{2} m_\mathrm{chain} v_\mathrm{chain}^2$ and internal bandwidth $b_\mathrm{chain}^\mathrm{int}$. Advective contribution:

$$\mathbf{J}_e^\mathrm{adv} = \frac{1}{V_\mathrm{cell}} \sum_\mathrm{chains} \left[\frac{1}{2} m_\mathrm{chain} v_\mathrm{chain}^2 + b_\mathrm{chain}^\mathrm{int}\right] \mathbf{v}_\mathrm{chain}.$$

Decomposing $v_\mathrm{chain} = v + \delta v$ (mean-plus-fluctuation), this splits into:

$$\mathbf{J}_e^\mathrm{adv} = e \mathbf{v} + \mathbf{v} \cdot \tau^\mathrm{kin} + \mathbf{Q}_\mathrm{kin},$$

where $\mathbf{Q}_\mathrm{kin}$ is the third-moment chain-velocity-fluctuation contribution (analog of kinetic-theory heat flux from $\langle \delta v_i \delta v_j \delta v_k \rangle$; standard kinetic-theory result).

Non-advective contribution: bandwidth content flows between chains via P04 update events without chain motion. This is the substrate-level analog of conduction. Schematically:

$$\mathbf{Q}^\mathrm{non-adv} = \mathbf{Q}_\mathrm{V1-mediated},$$

where the V1 retarded kernel mediates bandwidth-content propagation across the cell boundary. This contribution is finite-c-bounded by ED-07 and includes the substrate-level analog of thermal conduction.

**Total energy flux:**

$$\mathbf{J}_e = e \mathbf{v} + \mathbf{v} \cdot \tau + \mathbf{Q}, \qquad \mathbf{Q} = \mathbf{Q}_\mathrm{kin} + \mathbf{Q}_\mathrm{V1-mediated}.$$

The $\mathbf{v} \cdot \tau$ term combines the kinetic-stress work with the non-advective stress contribution; this is the standard form for the energy flux in compressible NS, with τ now identified at substrate level as before.

---

## 4. Flux Integrals over the 2-Sphere Boundary

For each conserved quantity Q with substrate-level transport rule $T_Q$, the total flux across the cell boundary is:

$$\Phi_Q(x, t) = \oint_{S^2(R_\mathrm{cg})} T_Q \cdot \hat{n} \, dA,$$

with the integration over the 2-sphere of radius R_cg surrounding the cell centre. The structural pattern parallels T19's holographic-bound integration over a 2-sphere.

### 4.1 Mass flux integral

$$\Phi_\rho = \oint_{S^2(R_\mathrm{cg})} \rho \mathbf{v} \cdot \hat{n} \, dA \;=\; V_\mathrm{cell} \, \nabla \cdot (\rho \mathbf{v})$$

(by Gauss's theorem in the small-cell limit, where the divergence is evaluated at the cell center). The 4πR_cg² area cancels with the cell volume V_cell = (4/3)πR_cg³ to yield ∇·(ρv) per unit volume. This is the standard divergence-from-flux step; the substrate-level chain-by-chain accounting reproduces it cleanly.

### 4.2 Momentum flux integral

$$\Phi_{\rho v_i} = \oint_{S^2(R_\mathrm{cg})} (\rho v_i v_j + \tau_{ij}) \hat{n}_j \, dA \;=\; V_\mathrm{cell} \, \partial_j (\rho v_i v_j + \tau_{ij}).$$

Same divergence-from-flux step. The advective ρv⊗v term and the stress-tensor τ_ij both contribute through the boundary surface; both produce divergence forms in the small-cell limit.

### 4.3 Energy flux integral

$$\Phi_e = \oint_{S^2(R_\mathrm{cg})} (e \mathbf{v} + \mathbf{v} \cdot \tau + \mathbf{Q}) \cdot \hat{n} \, dA \;=\; V_\mathrm{cell} \, \nabla \cdot (e \mathbf{v} + \mathbf{v} \cdot \tau + \mathbf{Q}).$$

Three contributions each become divergence terms in the cell-averaged energy equation.

### 4.4 What survives the R_cg → continuum limit

Track each term as R_cg shrinks within the (C1)∩(C2)∩(C3) window:

| Term | Behavior under R_cg variation |
|---|---|
| Bulk-advection $\rho v$, $\rho v_i v_j$, $e v$ | **R_cg-independent** when R_cg satisfies (C1). Statistical fluctuations scale as $1/\sqrt{N_\mathrm{cell}} \to 0$. |
| Kinetic-stress $\tau_{ij}^\mathrm{kin}$ | **R_cg-independent** within the window. The second-moment of velocity fluctuations is a local property of the chain-pair velocity distribution at scale R_cg. |
| V5-stress $\tau_{ij}^\mathrm{V5}$ | **R_cg-independent** in the window where chain-pair correlation length is much smaller than R_cg. (Assumption: chain-pair participation-overlap correlation length ≪ R_cg; verified for hydrodynamic regimes by C2.) |
| V1-memory stress $\tau_{ij}^\mathrm{V1-mem}$ | **R_cg-dependent at finite memory time.** Survives the limit if the memory kernel coarse-grains to a delta function (instantaneous Newtonian viscosity); becomes a non-local time-integral if the memory time exceeds the cell relaxation time. NS-2.06 audit. |
| Heat flux $\mathbf{Q}$ | **R_cg-independent** within the window for both kinetic-theory and V1-mediated contributions, by analogous reasoning. |
| Discrete chain-fluctuation terms | **Vanish** as $1/\sqrt{N_\mathrm{cell}} \to 0$ within the (C1) window. |

The R_cg-dependent surviving term — the V1-memory stress — is the locus where retarded-V1 structure (T18) may produce ED-specific corrections to standard NS. NS-2.06 will adjudicate whether this term coarse-grains to an instantaneous viscous form or to a non-local memory term.

---

## 5. Substrate → Continuum Scaling

The scaling-limit step takes substrate-level chain-by-chain accounting → continuum-level smooth fields, performed within the (C1)∩(C2)∩(C3) window from NS-2.01 §2.

### 5.1 Sum-over-chains → integral

For any chain-attribute quantity $A_\mathrm{chain}$, the cell-average converges in the (C1) regime:

$$\frac{1}{V_\mathrm{cell}} \sum_\mathrm{chains\ in\ cell} A_\mathrm{chain} \;\longrightarrow\; \int A(x', t) \, dV',$$

with the integral over a delta-function-like distribution at the cell center in the small-cell limit. This is the standard ensemble-average → continuum-field transition; in ED's case, the "ensemble" is the set of chains in the cell.

### 5.2 Cell-averaged products → continuum field products

For products of chain-attribute quantities, the cell-average separates into a product of cell-means plus a covariance term:

$$\frac{1}{V_\mathrm{cell}} \sum_\mathrm{chains} A_\mathrm{chain} B_\mathrm{chain} \;\longrightarrow\; \rho_{AB}(x, t) \cdot \langle AB \rangle(x, t),$$

with $\langle AB \rangle = \langle A \rangle \langle B \rangle + \mathrm{Cov}(A, B)$. The covariance term is the locus of all stress-tensor / heat-flux contributions; the cell-mean product is the locus of advective transport.

This is the structural origin of the kinetic-stress decomposition $\Pi^\mathrm{adv} = \rho v \otimes v + \tau^\mathrm{kin}$: the bulk-flow product comes from the means; the τ^kin comes from the covariance.

### 5.3 Continuum flux forms

Combining §3 transport rules + §4 boundary integrations + §5.1–5.2 scaling:

**Mass flux (continuum):**

$$\boxed{\mathbf{J}_\rho = \rho \mathbf{v}.}$$

Pure advection. No non-advective contribution.

**Momentum flux (continuum):**

$$\boxed{\Pi_{ij} = \rho v_i v_j + \tau_{ij},}$$

with τ_ij the stress tensor whose decomposition is for NS-2.05. At this point τ_ij is identified as the sum of (kinetic-stress) + (V5-stress) + (V1-memory-stress, possibly), but not yet decomposed into pressure + viscous form.

**Energy flux (continuum):**

$$\boxed{\mathbf{J}_e = e \mathbf{v} + \mathbf{v} \cdot \tau + \mathbf{Q},}$$

with Q the heat flux containing kinetic + V1-mediated bandwidth-conduction contributions.

These are the canonical NS forms for the flux content. The NS form is not yet derived — it will follow in NS-2.04 once the momentum equation is written explicitly using Π_ij. The structural content of NS-2.02 is establishing that ED's substrate produces these flux forms, with the non-advective contributions explicitly identified as substrate-level chain-fluctuation + cross-chain-participation-overlap + V1-retardation contributions, *not* as imported assumptions from continuum fluid mechanics.

### 5.4 Where ED differs structurally from standard kinetic-theory derivation

A standard kinetic-theory derivation (Boltzmann equation → Chapman-Enskog → NS) produces the same flux forms but via binary-collision integrals on the molecular distribution function. ED's substrate→NS path produces these forms via:

- **Chain-pair participation-overlap (V5)** in place of binary collisions — this is the structural substitute. V5 is generally retarded and finite-range at substrate level.
- **V1 retarded vacuum kernel (T18)** as a possible memory-kernel modification — *no analog in standard kinetic theory*. This is potentially an ED-specific deviation from standard NS.
- **Substrate UV cutoff ℓ_P (Q.8)** as the natural regularization — *no analog in standard kinetic theory*. Provides automatic short-scale regularization that may produce a higher-derivative term in the continuum momentum equation.

These three differences are the candidate sites where ED's NS form may deviate from standard NS. NS-2.05 / NS-2.06 / NS-2.07 will report whether the deviations survive the continuum limit at NS scales or coarse-grain to zero.

---

## 6. Output Forms for NS-2.03 and NS-2.04

NS-2.03 and NS-2.04 will use the following flux expressions exactly as written below.

### 6.1 For NS-2.03 (continuity equation)

$$\partial_t \rho + \nabla \cdot (\rho \mathbf{v}) = 0.$$

This follows directly from §3 (mass transport rule = advection only), §4.1 (mass flux integral → divergence form), §5.3 (continuum mass flux is ρv). NS-2.03's task is to write this as an equation, audit any source/sink terms (chain creation/annihilation, negligible for NS regimes), and confirm exactness in the non-reactive limit.

### 6.2 For NS-2.04 (momentum balance)

$$\partial_t (\rho v_i) + \partial_j (\rho v_i v_j + \tau_{ij}) = \rho f_i^{\mathrm{ext}}.$$

Equivalent by chain rule and continuity to:

$$\rho (\partial_t v_i + v_j \partial_j v_i) = -\partial_j \tau_{ij} + \rho f_i^{\mathrm{ext}}.$$

This is the **bare momentum balance equation**. The NS form emerges only after τ_ij is decomposed; until NS-2.05 produces that decomposition, the equation stands in the bare form above. NS-2.04's task is to write this equation explicitly, verify the chain-rule equivalence, and identify f^ext for the non-isolated case (gravity per T19, etc.).

**τ_ij is left undecomposed at this stage.** Its content per NS-2.02 is:

$$\tau_{ij} = \tau_{ij}^\mathrm{kin} + \tau_{ij}^\mathrm{V5} + \tau_{ij}^\mathrm{V1-mem},$$

with each component identified as substrate-level in origin. NS-2.05 adjudicates the decomposition into pressure + viscous + ED-specific.

### 6.3 For NS-2.07 (energy equation, compressible only)

$$\partial_t e + \partial_j (e v_j + v_i \tau_{ij} + Q_j) = \rho v_i f_i^{\mathrm{ext}}.$$

Used in compressible-NS closure; not load-bearing for the basic incompressible NS form. NS-2.07 will derive this equation explicitly when synthesizing the full NS form for the compressible case.

---

## 7. Recommended Next Steps

In priority order. With NS-2.02's flux forms in hand, NS-2.03 (continuity) follows mechanically and NS-2.04 (momentum balance) is largely transcription.

1. **Draft NS-2.03 — coarse-grained continuity equation.** File: `theory/Navier Stokes/NS-2.03_Continuity.md`. Short memo. Three sub-tasks: (a) write ∂_t ρ + ∇·(ρv) = 0 explicitly with cell-averaging derivation traced from NS-2.01 + NS-2.02; (b) audit source/sink terms (chain creation/annihilation negligible for NS regimes; confirm); (c) note the form is identical to chain-number conservation when fluid is single-species. **Expected the cleanest of all seven NS-2 memos.** Estimated 1–2 sessions at demonstrated pace.

2. **Draft NS-2.04 — momentum-balance equation.** File: `theory/Navier Stokes/NS-2.04_Momentum_Balance.md`. Slightly more involved than NS-2.03 because the τ_ij content from §6.2 must be carried forward as a placeholder for NS-2.05. Three sub-tasks: (a) write ∂_t (ρv_i) + ∂_j Π_ij = ρf_i^ext with NS-2.02's Π_ij; (b) verify chain-rule equivalence to ρ(∂_t v + v·∇v) = -∇·τ + ρf form; (c) identify f^ext (gravity, EM if applicable, plus any substrate-level contributions); (d) state explicitly that τ-decomposition is NS-2.05's task and audit what NS-2.04 inherits regarding τ's symmetry, sign conventions, and trace structure (any constraints from substrate level that NS-2.05 must respect). Estimated 1–2 sessions.

3. **Draft diffusion-coarse-graining future-arc scoping memo in parallel with NS-2.03 / NS-2.04.** File: `theory/Navier Stokes/Future_Arc_Diffusion_Coarse_Graining_Scoping.md`. Reasoning unchanged from NS-2 scoping § 8: NS-2.06 (viscosity origin) may need this theorem's machinery, and the connection to V5-stress + V1-memory-stress identified in §3.1 above suggests the diffusion theorem's coarse-graining work will share infrastructure with NS-2.06's stress-tensor derivation. Producing scoping early lets the two arcs share inputs cleanly. Cheap; recommended now, not later.

4. **Pre-NS-2.05 check: locate and read Arc N V5 memos** before NS-2.05 begins. NS-2.02 §3 identifies τ_ij^V5 as the cross-chain participation-overlap contribution, with structural origin in Arc N's V5 framework. NS-2.05's stress-tensor decomposition will need explicit V5 content. Quick read of arc-N memos covering V5 (likely [`arcs/arc-N/`](../../arcs/arc-N/) — file pattern to be confirmed) before NS-2.05 drafting begins. Estimated 30–60 minutes; a check, not anticipated to surface issues.

### Decisions for you

- **Confirm that τ-decomposition is NS-2.05-only**, not partial in NS-2.04. Recommended: yes — NS-2.04 should carry τ_ij as a placeholder per NS-2.02's structural identification, with no decomposition until NS-2.05. Keeps the load-bearing-hard work concentrated in one memo where it can be audited carefully.
- **Confirm the V1-memory term flag.** Per §4.4 and §5.4, $\tau_{ij}^\mathrm{V1-mem}$ may produce an ED-specific deviation from standard NS (memory-kernel viscous term) or may coarse-grain to instantaneous Newtonian viscosity. NS-2.06 audit. Worth flagging now that this is the most likely site of an ED-specific NS deviation, so any external-facing materials about NS-2 progress can frame the question correctly.

---

*NS-2.02 produces the substrate→continuum flux forms: $\mathbf{J}_\rho = \rho \mathbf{v}$, $\Pi_{ij} = \rho v_i v_j + \tau_{ij}$, $\mathbf{J}_e = e \mathbf{v} + \mathbf{v} \cdot \tau + \mathbf{Q}$. Stress tensor τ identified as $\tau^\mathrm{kin} + \tau^\mathrm{V5} + \tau^\mathrm{V1-mem}$ at substrate level; decomposition into pressure + viscous + ED-specific deferred to NS-2.05. Three candidate sites of ED-specific deviation from standard NS identified: V5 chain-pair structure, V1 retarded-memory kernel, ℓ_P substrate cutoff. Continuity (NS-2.03) and momentum balance (NS-2.04) follow mechanically from these flux forms; both should be fast.*
