# NS-2.01 — Substrate Conserved Quantities + Coarse-Graining Cell

**Date:** 2026-04-30
**Status:** Foundation memo for NS-2 (substrate→continuum coarse-graining arc).
**Companions:** [`NS-2_Scoping.md`](NS-2_Scoping.md), [`NS-1.05_Synthesis_B2_Verdict.md`](NS-1.05_Synthesis_B2_Verdict.md).

---

## 1. Purpose

NS-2.01 establishes the foundational objects on which the rest of NS-2 will operate:

- The **coarse-graining cell** — what spatial region is averaged over to define continuum fields.
- The **substrate conserved quantities** — what is exactly or approximately conserved at the chain level under coarse-graining.
- The **substrate-level conservation laws** — the form they take before continuum equations are derived.

NS-2.01 is *definitional and identifying*; it does not derive dynamics. Continuum-level continuity follows in NS-2.03; momentum balance in NS-2.04; stress-tensor structure in NS-2.05.

NS-2 inherits from NS-1's closure:

- **d = 3 footing** (NS-1.04): substrate-level dimensional commitment via T19/T20 geometry; not re-litigated here.
- **No PDE-level forcing route** (NS-1.02): no appeal to T18 or any kernel-level result for dimensional commitment within NS-2.
- **Architectural-suggestive d ≤ 3** (NS-1.03): working assumption that substrate motifs (gradients, decoupling surfaces, participation neighborhoods) are viable; NS-2 must not produce structures requiring d > 3 viability.
- **Path B-strong** as working dimensional framing.

---

## 2. Coarse-Graining Cell Definition

### 2.1 Three relevant scales

Three spatial scales are involved:

| Scale | Definition | Order |
|---|---|---|
| ℓ_P | Substrate UV cutoff per Q.8 / T19 (Newton-recovery forces ℓ_ED² = ℓ_P²) | ~10⁻³⁵ m |
| λ_mfp | Mean free path of chain-bundles (molecules) at coarse-grained scale; sets kinetic-vs-hydrodynamic boundary | depends on regime; for STP gas ~10⁻⁷ m; for liquids ~10⁻¹⁰ m |
| L_field | Characteristic length scale of continuum-field gradients (∇v, ∇ρ, ∇p) | application-dependent; for NS in laboratory regime ~10⁻³ m or larger |

The coarse-graining cell radius R_cg sits between λ_mfp and L_field:

$$\ell_P \ll \lambda_{\mathrm{mfp}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{field}}.$$

Below R_cg ~ λ_mfp, kinetic-theory regime applies (NS form not yet valid; Boltzmann equation is the appropriate description). Above R_cg ~ L_field, gradient information is washed out. NS-2 operates in the intermediate window.

### 2.2 Cell shape

**Default: spherical cell of radius R_cg.** Justification:

- **Isotropy.** A spherical cell respects the substrate's d = 3 isotropy (no a-priori-preferred axis). The chain-pair participation-overlap structure (Arc N V5) is rotationally invariant; using a non-spherical cell would impose an artificial preferred orientation.
- **Single parameter.** A spherical cell is fully specified by R_cg, simplifying the dependence-on-cell-geometry analysis.
- **Compatibility with substrate-gravity machinery.** T19/T20 use 2-sphere holographic boundaries (4πr² area). NS-2's flux-through-cell-boundary integrations (NS-2.02) can use the same 2-sphere boundary structure, sharing infrastructure with T19's holographic-bound calculation. Boundary area at scale R_cg is 4πR_cg².
- **Compatibility with d = 3 geometry.** Specifically aligns with NS-1.04's d = 3 footing; would not generalize cleanly to d ≠ 3 (cosmic horizon would be S^(d-1) per NS-1.04). NS-2 does not need to generalize, so this is a feature, not a bug.

Cubic cells are computationally simpler for some lattice-style derivations but introduce artificial axes; rejected for NS-2.

### 2.3 Cell-radius constraints

R_cg must satisfy three constraints simultaneously:

**(C1) Suppress chain-level discreteness.** The cell must contain enough chain-bundles that statistical fluctuations of conserved quantities are small relative to their means. Define N_cell = n_chain · (4/3)πR_cg³ as the expected chain count in a cell of radius R_cg with chain density n_chain. The constraint:

$$N_{\mathrm{cell}} \gg 1.$$

For an ideal gas at STP (n ~ 2.5 × 10²⁵ m⁻³), R_cg ≥ ~10 nm gives N_cell ~ 10⁴, suppressing fluctuations adequately (relative fluctuation ~ 1/√N ~ 1%). For a liquid (n ~ 3 × 10²⁸ m⁻³), R_cg ≥ ~1 nm suffices. For a sparse plasma, R_cg may need to be larger.

**(C2) Hydrodynamic regime.** The cell must be larger than the chain-bundle mean free path so that NS form (rather than kinetic-Boltzmann form) applies. Knudsen number Kn = λ_mfp / R_cg ≪ 1. Standard kinetic-theory criterion:

$$R_{\mathrm{cg}} \gg \lambda_{\mathrm{mfp}}.$$

For STP gas, R_cg ≥ ~1 μm; for liquids, R_cg ≥ ~10 nm.

**(C3) Preserve local structure.** R_cg must be smaller than the smallest field-gradient length scale of interest:

$$R_{\mathrm{cg}} \ll L_{\mathrm{field}}.$$

For laboratory-scale NS flows with mm-cm length scales, R_cg ≤ ~10 μm preserves field structure.

The window (C1 ∩ C2 ∩ C3) is non-empty for typical NS regimes; for STP gas, R_cg ~ 1–10 μm satisfies all three.

### 2.4 Participation-count and chain-overlap thresholds

**Participation-count threshold.** The cell must contain enough micro-events (substrate-level events, not just chain-bundles) for participation-weighted averaging to be statistically meaningful. With N_micro = (R_cg/ℓ_P)³ ~ 10¹³⁰ for R_cg ~ 1 μm, this is trivially satisfied at any reasonable R_cg. Not a binding constraint at NS-relevant scales.

**Chain-overlap threshold.** For chain-pair correlations (Arc N V5) to coarse-grain into a meaningful stress-tensor (NS-2.05) and viscosity coefficient (NS-2.06), chains within the cell must have non-trivial pairwise participation overlap. Working criterion:

$$\langle \mathrm{chain\text{-}pair\ participation\ overlap}\rangle_{\mathrm{cell}} > 0,$$

i.e., the cell-averaged chain-pair overlap is bounded away from zero. This is automatic in dense regimes (liquids, dense gases) but may fail in extremely rarefied regimes (single-particle flow), where NS form does not apply anyway.

### 2.5 Working choice

For the rest of NS-2: spherical cell of radius R_cg, with R_cg taken as the smallest scale satisfying (C1) ∩ (C2) ∩ (C3) for the target NS regime. Specific R_cg value is INHERITED at the application level; structural derivations in NS-2 must be R_cg-independent within the (C1) ∩ (C2) ∩ (C3) window.

---

## 3. Substrate Conserved Quantities

Six candidate substrate-level quantities. Four are load-bearing for NS; two are flagged but not centrally used.

### 3.1 Chain count n_chain

**Definition.** Number of chain worldlines threading the cell at time t. For non-reactive fluids (no nuclear / chemical reactions on NS time scales), chain count is conserved.

**Primitive basis.** P02 (chain) supplies the worldline existence; P11 (commitment-irreversibility) ensures chains do not "un-commit" themselves out of existence. Chain creation/annihilation requires interactions beyond P02 + P11 (Arc M F-M8 mass-form mediation, gauge-coupled processes per T17). For ordinary NS regimes, these are absent; chain count is exactly conserved.

**Coarse-grained form.** Chain number density n(x, t) = N_chains-in-cell-at-(x,t) / V_cell.

**Status.** Approximately exactly conserved; sourceless continuity equation applies (§4.1).

### 3.2 Chain mass (and continuum mass density ρ)

**Definition.** Each chain carries inertial mass m_chain per Arc M (M.1–M.3 closure: mass-form mediation via F-M8; mass is form-FORCED at chain level, value-INHERITED at the specific-mass-value level).

**Primitive basis.** Arc M derives mass as a chain attribute. M.1 resolves the massless-slot question; M.2 establishes mass-form additivity; M.3 fixes τ_g cross-sector coupling. For NS purposes, what matters is that mass is a *chain attribute*: each chain carries a definite mass, and this mass is conserved along the chain's worldline (no continuous mass loss; chain-level mass changes occur only at commitment events tied to gauge-coupled processes, absent in NS regimes).

**Coarse-grained form.** Continuum mass density:

$$\rho(x, t) = \frac{1}{V_{\mathrm{cell}}} \sum_{\mathrm{chains\ in\ cell\ at\ }(x,t)} m_{\mathrm{chain}}.$$

**Status.** Exactly conserved in non-reactive NS regimes; sourceless continuity equation applies (§4.2). **Form-FORCED, value-INHERITED** per Arc M's status.

### 3.3 Chain momentum (and continuum momentum density ρv)

**Definition.** Each chain has 4-momentum $p_\mathrm{chain}^\mu = m_\mathrm{chain} \, u_\mathrm{chain}^\mu$ where $u^\mu$ is the chain's normalized 4-velocity (timelike per P02). For NS at non-relativistic speeds, the 3-momentum $p_{\mathrm{chain},i} = m_\mathrm{chain} v_{\mathrm{chain},i}$ is the relevant component.

**Primitive basis.** P02 (timelike worldline) gives the chain's 4-velocity; Arc M gives the mass; product gives 4-momentum. Conservation of chain momentum in the absence of inter-chain interactions is the standard "free-chain" statement, dual to P11 commitment-ordering. Chain-pair interactions transfer momentum between chains but do not destroy it (Newton's-third-law analog: at substrate level, this is the antisymmetry of chain-pair participation-overlap-mediated coupling, embedded in Arc N V5 structure).

**Coarse-grained form.** Continuum momentum density (mass-weighted average velocity):

$$\rho(x, t) v_i(x, t) = \frac{1}{V_{\mathrm{cell}}} \sum_{\mathrm{chains\ in\ cell\ at\ }(x,t)} m_{\mathrm{chain}} v_{\mathrm{chain}, i}.$$

This *defines* the velocity field v_i(x, t) given ρ(x, t).

**Status.** Exactly conserved at the level of total momentum (sum over all chains, including those outside the cell). Cell-local momentum is conserved up to flux through cell boundary plus interaction with chains outside the cell — exactly the structure that produces ∂_t (ρv) + ∇·Π = ρf in NS-2.04, with Π_ij the momentum-flux tensor whose decomposition is for NS-2.05.

### 3.4 Bandwidth content (and continuum energy density e)

**Definition.** Per P04 (bandwidth additivity), each chain carries bandwidth content b_chain that is additive at commitment events. Bandwidth is the substrate-native quantity that coarse-grains to internal energy at the continuum scale (per [`substrate_a0_ed_native.md`](../../arcs/arc-SG/substrate_a0_ed_native.md) §1.4–1.5: "ED-gradient fluctuation rate" and "ED-gradient bandwidth" replace standard physics' "temperature" and "energy flux").

**Primitive basis.** P04 (bandwidth additivity) establishes the additive structure; ED-06 (decoupling surfaces) + ED-07 (signal propagation) + ED-10 (relational adjacency) supply the substrate-level physics for how bandwidth flows.

**Coarse-grained form.** Continuum total-energy density:

$$e(x, t) = \frac{1}{V_{\mathrm{cell}}} \sum_{\mathrm{chains\ in\ cell\ at\ }(x,t)} \left[\frac{1}{2} m_{\mathrm{chain}} v_{\mathrm{chain}}^2 + b_{\mathrm{chain}}^{\mathrm{internal}}\right],$$

with a kinetic part (½mv²) and an internal part (b_chain^internal, the "thermal" / binding bandwidth content).

**Status.** Conserved for closed systems; subject to dissipation terms (in NS-2.06 viscous term) and external work / heating terms in open systems. Energy conservation produces a separate continuum equation (energy equation) that decouples for incompressible NS but is required for compressible NS.

### 3.5 Other substrate quantities (flagged, not load-bearing for NS-2)

- **Angular momentum.** Derives from chain momentum + position; coarse-grains to fluid angular momentum density. Not independent at the level of conservation laws. Used as diagnostic in vortex dynamics but not as a primary conserved quantity in standard NS form.
- **Charge.** Per T17 gauge structure; conserved by gauge invariance. Not load-bearing for non-charged NS; flagged for future MHD extensions.
- **Helicity.** Not a primitive; emergent flow quantity; not used in NS-2 derivation.

These are noted for completeness but not used as starting points for the NS-2 derivation chain.

### 3.6 Aggregate

Four load-bearing substrate conserved quantities, mapped to four continuum fields:

| Substrate quantity | Continuum field | Continuity equation? |
|---|---|---|
| Chain count | n(x, t) | Yes (§4.1) |
| Chain mass | ρ(x, t) | Yes (§4.2) — the NS continuity equation |
| Chain momentum | ρv(x, t) | Momentum-balance form (§4.3) — feeds NS momentum equation |
| Bandwidth content | e(x, t) | Energy-balance form (§4.4) — relevant for compressible NS |

For incompressible NS at constant density, the energy equation decouples and only continuity + momentum-balance are operative. NS-2 will derive both regimes; incompressible-NS as the simpler case, compressible-NS as the more general.

---

## 4. Conservation Laws (Primitive Level)

Substrate-level conservation laws written in continuum form after coarse-graining over the cell defined in §2. Each is derived from the substrate-level statement of the corresponding conservation, with the coarse-graining cell supplying the spatial average. Detailed flux derivations are deferred to NS-2.02; the laws here are stated in their structural form.

### 4.1 Chain-number conservation

$$\partial_t n + \nabla \cdot \mathbf{J}_n = 0,$$

where $\mathbf{J}_n(x, t)$ is the chain-number flux (chains per unit area per unit time) through the cell boundary. **Exact** in non-reactive regimes; approximate when chain creation/annihilation rates per cell volume per time are non-negligible.

### 4.2 Mass conservation

$$\partial_t \rho + \nabla \cdot (\rho \mathbf{v}) = 0.$$

**Exact** in non-reactive regimes. Identical in form to chain-number conservation when all chains in the fluid have the same mass; for multi-species fluids, the two differ by the species-weighted mass distribution but the total-mass form remains exact.

This is the NS continuity equation. NS-2.03 will re-derive it explicitly from NS-2.02's flux derivation, but the structural content is established here.

### 4.3 Momentum conservation

$$\partial_t (\rho v_i) + \partial_j \Pi_{ij} = \rho f_i^{\mathrm{ext}},$$

where $\Pi_{ij}(x, t)$ is the momentum-flux tensor (chain-momentum flux through cell boundary + intra-cell momentum-transfer mediated by chain-pair participation overlap), and $f_i^{\mathrm{ext}}$ is any external body force (e.g., gravity per T19, EM per T17). **Exact** for total momentum modulo external forces; the decomposition of $\Pi_{ij}$ into pressure + viscous + ED-specific contributions is the load-bearing question for NS-2.05 / NS-2.06.

### 4.4 Bandwidth-content (energy) conservation

$$\partial_t e + \partial_j (e v_j + Q_j) = \Pi_{ij} \partial_j v_i + \rho f_i^{\mathrm{ext}} v_i + \mathcal{D},$$

where $Q_j$ is the heat-flux-analog (bandwidth-content flux not carried by bulk transport), the right-hand side contains work-by-stresses + work-by-external-forces + bandwidth-source/sink term $\mathcal{D}$ (which is zero in closed systems). **Approximately exact in closed adiabatic regimes**; subject to small substrate-level corrections involving retarded V1 structure (T18 carries forward into bandwidth-flux retardation; see NS-2.06).

For incompressible NS, this equation decouples and is not needed for the basic NS form. For compressible NS, it is required for closure (it provides the equation determining temperature/pressure in compressible flows).

### 4.5 Status summary

| Law | Form | Exactness | Used in |
|---|---|---|---|
| Chain-number | ∂_t n + ∇·J_n = 0 | Exact (non-reactive) | NS-2.03 (continuity, equivalent to mass form) |
| Mass | ∂_t ρ + ∇·(ρv) = 0 | Exact (non-reactive) | NS-2.03 |
| Momentum | ∂_t (ρv) + ∂_j Π_ij = ρf | Exact (modulo external forces) | NS-2.04, decomposition in NS-2.05 |
| Energy | ∂_t e + ∂_j (...) = ... | Approximately exact (closed adiabatic) | Compressible NS only; for NS-2's incompressible form, not central |

---

## 5. Mapping to Continuum Fields

NS-2.01 defines the *kinematic* mapping from substrate to continuum (which substrate quantity becomes which continuum field). NS-2.01 does *not* define dynamics; that is for NS-2.03 (continuity), NS-2.04 (momentum balance), NS-2.05 (stress-tensor structure), NS-2.06 (viscosity), NS-2.07 (synthesis).

### 5.1 Density ρ(x, t) — definition

$$\rho(x, t) = \frac{1}{V_{\mathrm{cell}}} \sum_{\mathrm{chains\ in\ cell\ at\ }(x,t)} m_{\mathrm{chain}}.$$

Form-FORCED via Arc M chain mass; value-INHERITED via species-specific chain mass values. Chain-mass conservation per Arc M ensures ρ obeys the continuity equation §4.2.

### 5.2 Velocity v(x, t) — definition

$$v_i(x, t) = \frac{1}{\rho(x, t) V_{\mathrm{cell}}} \sum_{\mathrm{chains\ in\ cell\ at\ }(x,t)} m_{\mathrm{chain}} v_{\mathrm{chain}, i}.$$

Mass-weighted average of chain velocities. By construction, this is the velocity field whose product with ρ gives the continuum momentum density; momentum conservation §4.3 is therefore automatic for any v defined this way. Form-FORCED via Arc M mass + P02 chain velocity; value-INHERITED at the bulk-flow value level.

### 5.3 Pressure p(x, t) — definition deferred to NS-2.05

NS-2.01 does not pick a definition for p. Three candidates are listed for NS-2.05's adjudication:

**(P-1) Kinetic-pressure analog.** Second moment of chain velocity fluctuations relative to the cell-mean velocity:

$$p^{(P-1)}(x, t) = \frac{1}{3 V_{\mathrm{cell}}} \sum_{\mathrm{chains\ in\ cell}} m_{\mathrm{chain}} |v_{\mathrm{chain}} - v(x, t)|^2.$$

Direct kinetic-theory analog; for ideal gas this is the standard $p = (1/3) \rho \langle |\delta v|^2 \rangle = nkT$ form. Substrate-natively expressible.

**(P-2) Bandwidth-density gradient.** Derived from spatial variation of bandwidth content, parallel to T19's cumulative-strain reading. The pressure gradient $\nabla p$ would emerge as the spatial gradient of bandwidth density, with p itself defined up to a constant. This candidate is structurally adjacent to T19's mechanism for force-from-stability-landscape-gradient and may inherit substrate machinery.

**(P-3) Cross-chain stability-landscape contribution.** The pressure as the cell-averaged chain-pair stability contribution per ED-I-06's "force is what it feels like when the stability landscape changes" framing. Operates at the participation-overlap layer; structurally adjacent to Arc N V5 + T18 retarded-V1 machinery.

These are not mutually exclusive — the three may correspond to additive contributions that decompose the full pressure into ideal-gas-kinetic + bandwidth-equation-of-state + cross-chain-stability components. NS-2.05's adjudication is whether ED's substrate selects one as the "true" pressure or whether the full decomposition is structurally meaningful.

---

## 6. Preconditions for NS-2.02

NS-2.02 (participation-weighted flux derivation) will require, from NS-2.01:

1. **Coarse-graining cell geometry (§2):** spherical, radius R_cg, with (C1)∩(C2)∩(C3) constraints. Cell boundary is a 2-sphere of area 4πR_cg² aligned with T19's holographic-bound integration template.
2. **Conserved quantities (§3):** chain count, mass, momentum, bandwidth content.
3. **Conservation-law structural form (§4):** generic ∂_t (density) + ∇·(flux) = source/sink form for each.
4. **Continuum-field definitions (§5):** ρ, v explicitly defined; p deferred.

NS-2.02's deliverables (preview):

- Explicit expressions for $\mathbf{J}_n$, $\mathbf{J}_\rho = \rho \mathbf{v}$, $\Pi_{ij}$, $\mathbf{Q} + e\mathbf{v}$ in terms of substrate-level chain quantities integrated over the cell boundary.
- Identification of which flux components are *advective* (carried by bulk velocity) vs. *non-advective* (mediated by chain-pair participation overlap; the locus of viscous and pressure contributions).
- Use of the 2-sphere boundary integration to establish substrate→continuum flux scaling parallel to T19's holographic-bound usage.

---

## 7. Recommended Next Steps

In priority order.

1. **Pre-arc check: Arc M mass-derivation in usable form for NS-2.** Confirm that Arc M's M.1–M.3 closure (mass-form mediation, F-M8 framework) supplies a chain-attribute mass with the form-FORCED / value-INHERITED status NS-2.01 §3.2 assumes. Quick read of arc-M closure memos before NS-2.02 begins. Expected straightforward; flagged as a check, not anticipated to surface issues. Estimated 30 minutes.

2. **Draft NS-2.02 — participation-weighted flux derivation.** File: `theory/Navier Stokes/NS-2.02_Participation_Fluxes.md`. Three deliverables: (a) explicit flux expressions for each conserved quantity from §3, integrated over the cell's 2-sphere boundary; (b) identification of advective vs. non-advective flux components; (c) substrate→continuum flux-scaling step parallel to T19's holographic-bound integration. Should be the second-cleanest of the seven NS-2 memos (after this one); the structural template is well-established by T19.

3. **Optional, recommended in parallel: produce diffusion-coarse-graining future-arc scoping memo.** File: `theory/Navier Stokes/Future_Arc_Diffusion_Coarse_Graining_Scoping.md` (or at `theory/` root). Reasoning unchanged from NS-2 scoping §8: NS-2.06's viscosity-origin derivation may benefit from the diffusion-coarse-graining theorem's machinery; producing scoping early lets NS-2.06's drafting proceed with a clear sense of which inputs come from where. Cheap; no commitment to derivation work.

### Decisions for you

- **Confirm cell-radius parameterization is acceptable** as written: spherical, R_cg in the (C1)∩(C2)∩(C3) window, with the specific R_cg value INHERITED at application level. Alternative: pin R_cg to a substrate-specific value (e.g., R_cg = N · ℓ_P with N a structural integer); this would be a substrate-level commitment beyond what existing primitives provide and is not recommended.
- **Confirm pressure-decomposition framing** for NS-2.05 — three candidates as in §5.3, with NS-2.05 to adjudicate whether ED selects one or whether the decomposition is additive and structurally meaningful.
- **Confirm energy-equation scope** — derive in NS-2 as an optional sub-section for compressible-NS users, or restrict NS-2 to incompressible NS and treat the energy equation as out-of-scope? Recommend the former: derive in compressible form in NS-2.06 / NS-2.07 with the incompressible decoupling explicitly identified, since the compressible form is more general and the incompressible specialization is a single algebraic step.

---

*NS-2.01 establishes the substrate→continuum kinematic mapping and the substrate-level conservation laws. Spherical coarse-graining cell of radius R_cg in the (chain-discreteness-suppressed)∩(hydrodynamic-regime)∩(field-structure-preserving) window. Four load-bearing conserved quantities: chain count, mass (Arc M), momentum, bandwidth content. Mass and momentum identifications are clean; pressure identification deferred to NS-2.05 with three candidates listed. Continuity-equation form is derivable directly from §4.2; full derivation in NS-2.03. Next memo: NS-2.02 — participation-weighted flux derivation.*
