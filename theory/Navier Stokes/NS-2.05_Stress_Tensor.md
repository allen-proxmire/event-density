# NS-2.05 — Stress-Tensor Decomposition

**Date:** 2026-04-30
**Status:** Decomposition delivered. **Headline: ED reproduces standard NS stress-tensor structure (pressure + Newtonian viscous) at standard NS scales, with one structurally-identified ED-specific correction term whose amplitude is INHERITED (per V5's status). The V1-memory contribution coarse-grains to instantaneous viscosity at any NS scale, not memory-kernel. The form-FORCED / value-INHERITED hierarchy preserves cleanly.**
**Sources audited:** [`NS-2.01_Conserved_Quantities.md`](NS-2.01_Conserved_Quantities.md), [`NS-2.02_Participation_Fluxes.md`](NS-2.02_Participation_Fluxes.md), [`NS-2.04_Momentum_Balance.md`](NS-2.04_Momentum_Balance.md), [`arcs/arc-N/non_markov_forced.md`](../../arcs/arc-N/non_markov_forced.md) §6.5 (V5 verdict), [`theorems/T18.md`](../../theorems/T18.md) + arc-B closure (V1 retarded kernel structure).

---

## 1. Purpose

NS-2.05 decomposes the stress tensor τ_ij identified at substrate level into its physical components:

$$\tau_{ij} = p_\mathrm{eff} \, \delta_{ij} + \sigma_{ij}^\mathrm{visc} + \tau_{ij}^\mathrm{ED-specific}.$$

Three load-bearing adjudications:

- **The three pressure candidates from NS-2.01 §5.3** — kinetic (P-1), bandwidth-density gradient (P-2), cross-chain stability landscape (P-3). NS-2.05 determines which contribute to $p_\mathrm{eff}$ and how.
- **The origin of viscosity** — kinetic-theory deviatoric contribution from τ^kin, V5 deviatoric contribution from cross-chain correlations, V1-memory contribution from retarded vacuum kernel. NS-2.05 sums these and identifies the substrate-level Newtonian-viscous structure.
- **Whether ED introduces non-standard NS stress terms** — possible cross-chain memory term from V5 (form-INHERITED), possible higher-derivative regularization from ℓ_P. NS-2.05 reports what survives the standard-NS-scale continuum limit.

This is the load-bearing-hard memo of NS-2. Its outcome determines whether ED's NS form matches standard NS exactly, deviates with a structurally-identified correction, or fails to reproduce standard NS.

---

## 2. Inputs

| Input | Source |
|---|---|
| τ_ij = τ_ij^kin + τ_ij^V5 + τ_ij^V1-mem | NS-2.02 §3.1 |
| Symmetry τ_ij = τ_ji | NS-2.04 §6.1 (forced at substrate level by chain-pair Newton's-third-law analog + ED-10 rotational invariance) |
| Trace decomposition τ_ij = p_eff δ_ij + τ_ij^dev | NS-2.04 §6.3 |
| Sign convention (pressure +p δ_ij, viscous deviatoric) | NS-2.04 §6.2 |
| Material-derivative momentum equation ρ Dv_i/Dt = -∂_j τ_ij + ρf_i^ext | NS-2.04 §7 |
| **V5 status: FORCED-conditional-on-V1 in existence-of-correlations sense; amplitudes INHERITED** | [`arcs/arc-N/non_markov_forced.md`](../../arcs/arc-N/non_markov_forced.md) §6.5 |
| V1 finite-width kernel on ℓ_ED ~ ℓ_P (forced by T19 Newton-recovery) | T18 derivation chain + T19 Newton-recovery |
| Three pressure candidates P-1/P-2/P-3 | NS-2.01 §5.3 |

---

## 3. Decomposition of τ_ij^kin (kinetic contribution)

### 3.1 Kinetic-theory-analog setup

Per NS-2.02 §3.1, the kinetic-stress contribution is the cell-averaged second moment of chain velocity fluctuations:

$$\tau_{ij}^\mathrm{kin}(x, t) = \frac{1}{V_\mathrm{cell}} \sum_\mathrm{chains\ in\ cell} m_\mathrm{chain} \, \delta v_{\mathrm{chain}, i} \, \delta v_{\mathrm{chain}, j},$$

where $\delta v_{\mathrm{chain}} = v_\mathrm{chain} - v(x, t)$ is the chain's velocity fluctuation about the cell-mean.

### 3.2 Isotropic / deviatoric split

For a chain ensemble in local thermal equilibrium (LTE) — the standard kinetic-theory hydrodynamic regime, ensured by (C2) Knudsen ≪ 1 — the velocity-fluctuation distribution is approximately isotropic. The second-moment tensor splits:

$$\tau_{ij}^\mathrm{kin} = p_\mathrm{kin} \, \delta_{ij} + \sigma_{ij}^{\mathrm{visc}, \mathrm{kin}},$$

with isotropic part:

$$p_\mathrm{kin}(x, t) = \frac{1}{3} \, \tau_{ii}^\mathrm{kin} = \frac{1}{3 V_\mathrm{cell}} \sum_\mathrm{chains} m_\mathrm{chain} |\delta v_\mathrm{chain}|^2,$$

and deviatoric part $\sigma_{ij}^{\mathrm{visc}, \mathrm{kin}}$ traceless, carrying the viscous response to velocity-gradient deformation. By the standard kinetic-theory Chapman-Enskog expansion in small Knudsen number:

$$\sigma_{ij}^{\mathrm{visc}, \mathrm{kin}} = -\mu_\mathrm{kin} \left[\partial_i v_j + \partial_j v_i - \frac{2}{3} \delta_{ij} \nabla \cdot \mathbf{v}\right],$$

with $\mu_\mathrm{kin}$ the kinetic-theory shear viscosity (specific value INHERITED via chain-pair scattering cross sections; functional form is the standard Newtonian deviatoric form by symmetry + linearity in velocity gradient).

### 3.3 What is structurally identical to standard kinetic theory, what differs

**Identical.** The mechanism — second-moment of velocity fluctuations + chain-ensemble LTE + Chapman-Enskog → Newtonian deviatoric form — is the same as standard kinetic theory, with chains in place of molecules. The substitution does not change the form-derivation steps; ED's kinetic-stress contribution reproduces the standard Newtonian form exactly.

**Differs.** The substrate-level origin of the chain-pair scattering process is V5 (cross-chain participation overlap mediated by vacuum coupling), not binary molecular collisions. This affects the *value* of $\mu_\mathrm{kin}$ but not the *form* of $\sigma_{ij}^{\mathrm{visc}, \mathrm{kin}}$. Per V5's status (FORCED-conditional existence; amplitude INHERITED), $\mu_\mathrm{kin}$ is INHERITED.

**Verdict on τ^kin: form-FORCED (Newtonian deviatoric structure); value-INHERITED ($\mu_\mathrm{kin}$).**

---

## 4. Decomposition of τ_ij^V5 (cross-chain participation overlap)

### 4.1 Substrate origin per Arc N

Per [`arcs/arc-N/non_markov_forced.md`](../../arcs/arc-N/non_markov_forced.md) §6.5, V5 is the cross-chain extension of V1: same-sector chains acquire correlated $b^\mathrm{env}$ content (vacuum-mediated bandwidth correlation) via the Q.8 effective-vacuum factorisation. The verdict is unambiguous:

> "V5 differs from V1 in that V1 only forces the *kernel form* of single-chain vacuum response; V5 makes a stronger claim about cross-chain *correlation amplitude*. The correlation amplitude is INHERITED, not FORCED — it depends on multi-chain couplings to the vacuum sector. The *existence* of cross-chain correlations is FORCED-conditional-on-V1; the *amplitude* is INHERITED."

Translated to NS-2 language: τ_ij^V5 *exists* as a substrate contribution to the stress tensor, but its specific functional dependence on field variables (ρ, v, ∇v, ...) is INHERITED rather than form-derived from primitives.

### 4.2 Isotropic / deviatoric split, with honest inheritance

By symmetry and the trace decomposition (NS-2.04 §6.3):

$$\tau_{ij}^\mathrm{V5} = p_\mathrm{V5} \, \delta_{ij} + \sigma_{ij}^{\mathrm{visc}, \mathrm{V5}} + \tau_{ij}^{\mathrm{V5}, \mathrm{ED-spec}},$$

with three components:

- **Isotropic** $p_\mathrm{V5}$. Cell-averaged trace of cross-chain correlations; contributes to total pressure.
- **Deviatoric (Newtonian-form)** $\sigma_{ij}^{\mathrm{visc}, \mathrm{V5}} = -\mu_\mathrm{V5} [\partial_i v_j + \partial_j v_i - (2/3)\delta_{ij} \nabla \cdot \mathbf{v}]$ — by the same symmetry + linearity-in-gradient argument as §3.2, *if* the V5 amplitude functional form depends linearly on velocity gradients. This is the standard-NS expectation.
- **ED-specific cross-chain residual** $\tau_{ij}^{\mathrm{V5}, \mathrm{ED-spec}}$ — any non-Newtonian cross-chain correlation content not captured by the linear-gradient deviatoric form.

**Honest inheritance flag.** Because V5's amplitude is INHERITED rather than derived, the precise functional form of τ_ij^V5 is *form-partially-FORCED*: the isotropic / deviatoric split is forced by symmetry; the specific amplitude functions $p_\mathrm{V5}(\rho, ...)$ and $\mu_\mathrm{V5}(\rho, ...)$ are INHERITED. The Newtonian linear-gradient form for $\sigma^{\mathrm{visc}, \mathrm{V5}}$ is *consistent* with V5 but not uniquely *forced* by V5; it is the natural reading under the form-FORCED / value-INHERITED methodology, validated empirically by Newtonian-fluid behavior.

### 4.3 Does V5 introduce a new structural NS term?

**Likely no, modulo an INHERITED-amplitude correction.** The standard reading: V5's vacuum-mediated cross-chain correlations are the substrate-level mechanism behind kinetic-theory's binary-collision contribution to viscosity. The isotropic and deviatoric components of τ_ij^V5 add to the corresponding components of τ_ij^kin to produce a single effective Newtonian fluid form, with $\mu_\mathrm{total} = \mu_\mathrm{kin} + \mu_\mathrm{V5}$.

**Less likely but structurally possible:** V5 introduces a non-Newtonian cross-chain term $\tau_{ij}^{\mathrm{V5}, \mathrm{ED-spec}}$ with no kinetic-theory analog — for example, a stress component depending on higher-than-first velocity gradients, or a stress component depending on cross-chain participation-overlap correlation length (a substrate-specific length scale not derivable from chain ensemble alone). The amplitude of this term is INHERITED; it could be zero (recovering standard NS exactly) or non-zero (giving an ED-specific non-Newtonian deviation).

**Verdict on τ^V5: form-partially-FORCED (existence + isotropic/deviatoric split forced; specific amplitude functions INHERITED). Standard-NS-recovery is the natural reading; ED-specific deviation is possible but its amplitude is INHERITED, plausibly small/negligible at NS scales.**

---

## 5. Decomposition of τ_ij^V1-mem (retarded-kernel memory)

### 5.1 V1 finite-width and the memory time scale

V1 is the retarded vacuum kernel forced by T18 (NS-1.02 audit). Its functional form is finite-width on the substrate scale ℓ_ED, with ℓ_ED² = ℓ_P² fixed by Newton-recovery in T19 (T19 main result). The memory time scale of V1 is therefore:

$$\tau_\mathrm{V1} \sim \ell_P / c \sim 10^{-44} \, \mathrm{s}$$

(the Planck time).

Any NS-relevant time scale is many orders of magnitude longer:

- Laboratory NS: τ_NS ≥ μs ~ 10⁻⁶ s.
- Engineering / atmospheric NS: τ_NS ≥ ms.
- Galactic / astrophysical NS: τ_NS ≥ kyr.

The ratio $\tau_\mathrm{V1} / \tau_\mathrm{NS} \le 10^{-38}$ for any NS scenario.

### 5.2 Coarse-graining limit

In the substrate→continuum limit at NS scales, the V1 retardation kernel coarse-grains to:

$$K_\mathrm{V1}(t - t') \;\xrightarrow[\tau_\mathrm{V1}/\tau_\mathrm{NS} \to 0]{}\; \delta(t - t').$$

The memory-kernel contribution to the stress tensor reduces to an instantaneous response; any time-non-local structure becomes invisible at NS scales.

**Concretely:** the V1-mem contribution to τ_ij at NS scale becomes:

$$\tau_{ij}^\mathrm{V1-mem} \;\xrightarrow[\mathrm{NS}\ \mathrm{scale}]{}\; -\mu_\mathrm{V1} \left[\partial_i v_j + \partial_j v_i - \frac{2}{3} \delta_{ij} \nabla \cdot \mathbf{v}\right] + (\mathrm{isotropic\ contribution\ to}\ p_\mathrm{eff}),$$

where $\mu_\mathrm{V1}$ is the time-integrated effective viscosity from the V1 kernel's narrow finite width. The Newtonian deviatoric form is recovered.

### 5.3 Conditions under which finite-memory regime would apply

Memory-kernel structure (non-Newtonian time-non-local viscous response) survives only when:

$$\tau_\mathrm{V1} \gtrsim \tau_\mathrm{flow},$$

i.e., when the flow's characteristic time scale becomes comparable to or shorter than the V1 memory time. This requires flow time scales ≤ 10⁻⁴⁴ s, vastly outside any NS regime. **For any standard NS application, V1-mem coarse-grains to instantaneous Newtonian viscosity. No ED-specific memory-kernel deviation from standard NS at NS scales.**

Exotic regimes where the memory kernel might survive:
- Quark-gluon plasma immediately post-Big-Bang (τ_flow ~ 10⁻²³ s; still many orders larger than τ_V1).
- Direct probes at substrate scale (which would not be hydrodynamic anyway).

These are outside NS-2's scope.

**Verdict on τ^V1-mem: form-FORCED to coarse-grain to standard Newtonian deviatoric at NS scales; contributes to $\mu_\mathrm{total}$. Memory-kernel structure not present at NS scales.**

---

## 6. Pressure Identification

### 6.1 Adjudicate the three NS-2.01 §5.3 candidates

Mapping each candidate to the substrate-level contributions identified above:

**P-1 (kinetic-pressure analog).** Second moment of chain velocity fluctuations. Maps directly to $p_\mathrm{kin}$ in §3.2:

$$p_{P-1} = p_\mathrm{kin} = \frac{1}{3 V_\mathrm{cell}} \sum_\mathrm{chains} m_\mathrm{chain} |\delta v_\mathrm{chain}|^2.$$

Substrate-derivation form-FORCED. Value INHERITED via specific chain-mass and velocity-fluctuation distribution.

**P-2 (bandwidth-density gradient).** Bandwidth-content content per chain (P04) coupled to spatial extent. The bandwidth content's spatial gradient produces a force-like contribution via T19's cumulative-strain mechanism — but at NS scales, this is the *gravitational* force (already captured in $f^{\mathrm{ext}}$ per NS-2.04 §5.1), not a pressure contribution to τ_ij. **P-2 is not an additional pressure contribution at NS scales; it is the substrate origin of gravity, already accounted for in $f^{\mathrm{ext}}$.** Removing P-2 from the pressure-candidate list.

**P-3 (cross-chain stability landscape).** Cross-chain stability via vacuum-mediated participation-overlap coupling. Maps directly to τ_ij^V5's isotropic part:

$$p_{P-3} = p_\mathrm{V5}.$$

Substrate-existence form-FORCED via V5's existence verdict. Amplitude INHERITED via V5's amplitude-INHERITED status.

### 6.2 Pressure decomposition

Combining contributions to the trace of τ:

$$p_\mathrm{eff}(x, t) = p_\mathrm{kin}(x, t) + p_\mathrm{V5}(x, t) + p_\mathrm{V1-mem}(x, t).$$

Three sources:

- $p_\mathrm{kin}$ — kinetic-pressure (standard kinetic-theory form; reproduces ideal-gas + intermolecular-correction form).
- $p_\mathrm{V5}$ — cross-chain vacuum-mediated correlation contribution to pressure (form-existence forced; amplitude INHERITED).
- $p_\mathrm{V1-mem}$ — V1 retarded-kernel contribution; coarse-grains to the trace of the effective Newtonian-form contribution from §5.2 (instantaneous, isotropic part).

**Equation-of-state status.** The functional form $p_\mathrm{eff}(\rho, T, ...)$ is partially form-FORCED (kinetic part follows kinetic-theory equation of state) and partially INHERITED (V5 contribution amplitude). For an ideal monatomic chain ensemble, the kinetic part gives $p_\mathrm{kin} = nkT$ (ideal-gas form); for liquids and dense fluids, V5 corrections dominate and the form is INHERITED via empirical equation-of-state data.

This reproduces the standard physics situation: ideal-gas equation of state form-derived; real-fluid equations of state empirically fit. ED's substrate framework places this empirical fitting *inside* the form-FORCED / value-INHERITED methodology cleanly.

### 6.3 Trace verdict

$p_\mathrm{eff}$ is **kinetic + V5** (not kinetic + V5 + V1-mem as a separate third channel — V1-mem's isotropic contribution coarse-grains into the Newtonian instantaneous form alongside kinetic and V5). The decomposition is:

- form-FORCED at the existence level (substrate-level pressure is forced by trace structure of substrate-level stress tensor),
- form-FORCED for the kinetic part (standard kinetic-theory derivation),
- form-existence-FORCED + amplitude-INHERITED for the V5 part (per V5's status).

P-2 is removed from the pressure-candidate list (it is gravity, not pressure). The three-candidate framing in NS-2.01 §5.3 collapses to a two-candidate decomposition (kinetic + V5) at NS scales.

---

## 7. Final Stress-Tensor Form

$$\boxed{\tau_{ij} = p_\mathrm{eff} \, \delta_{ij} + \sigma_{ij}^\mathrm{visc} + \tau_{ij}^\mathrm{ED-specific}.}$$

with:

### 7.1 Pressure $p_\mathrm{eff}$

$$p_\mathrm{eff}(x, t) = p_\mathrm{kin}(x, t) + p_\mathrm{V5}(x, t).$$

- $p_\mathrm{kin}$: standard kinetic-theory form, ideal-gas plus intermolecular corrections. Form-FORCED.
- $p_\mathrm{V5}$: cross-chain vacuum-mediated correlation contribution. Existence form-FORCED via V5; amplitude INHERITED.

### 7.2 Viscous stress $\sigma_{ij}^\mathrm{visc}$

Standard Newtonian deviatoric form:

$$\sigma_{ij}^\mathrm{visc} = -\mu_\mathrm{total} \left[\partial_i v_j + \partial_j v_i - \frac{2}{3} \delta_{ij} \nabla \cdot \mathbf{v}\right] - \zeta \, \delta_{ij} \nabla \cdot \mathbf{v},$$

with:
- $\mu_\mathrm{total} = \mu_\mathrm{kin} + \mu_\mathrm{V5} + \mu_\mathrm{V1}$ (total shear viscosity, sum of three substrate contributions).
- $\zeta$ = bulk viscosity, contributing only when $\nabla \cdot \mathbf{v} \neq 0$ (compressible flow). Bulk viscosity origin: deviation of bandwidth-content-equilibration time scale from translational-equilibration time scale at coarse-grained level. Form-FORCED-conditional (existence depends on whether substrate produces multiple equilibration time scales); value INHERITED.

Form of $\sigma^\mathrm{visc}$ form-FORCED by symmetry + linearity-in-gradient + Newtonian-fluid empirical match. Specific values of $\mu_\mathrm{total}$ and $\zeta$ INHERITED.

### 7.3 ED-specific residual $\tau_{ij}^\mathrm{ED-specific}$

$$\tau_{ij}^\mathrm{ED-specific} \;=\; \tau_{ij}^{\mathrm{V5}, \mathrm{ED-spec}} \;+\; (\mathrm{possible}\ \ell_P\text{-derivative term}).$$

- $\tau_{ij}^{\mathrm{V5}, \mathrm{ED-spec}}$: any non-Newtonian cross-chain correlation contribution beyond the linear-gradient form. Form-existence allowed by V5's INHERITED amplitude; functional form INHERITED. **Plausibly zero at standard NS scales** (no empirical evidence of a generic non-Newtonian cross-chain correction in laboratory fluids; this would have surfaced as a discrepancy between standard NS and observed flows).
- ℓ_P-derivative term: possible higher-derivative regularization at substrate cutoff. Order-of-magnitude $\ell_P^2 \nabla^4 v$. **Negligible at NS scales** ($\ell_P^2 / L_\mathrm{flow}^2 \le 10^{-60}$ for any laboratory flow). Becomes structurally important *only* if NS-3 finds that finite-time singularities approach substrate scale, in which case the regularization protects against blow-up. Flagged for NS-3, not load-bearing for NS-2.

### 7.4 Aggregate verdict

**At standard NS scales:**

$$\tau_{ij} = p_\mathrm{eff} \, \delta_{ij} - \mu_\mathrm{total} \left[\partial_i v_j + \partial_j v_i - \frac{2}{3} \delta_{ij} \nabla \cdot \mathbf{v}\right] - \zeta \, \delta_{ij} \nabla \cdot \mathbf{v} + \tau_{ij}^\mathrm{ED-specific\ negligible}.$$

This is **standard Newtonian-fluid stress** with the ED-specific residual flagged as negligible at NS scales. ED reproduces standard NS form to high accuracy at NS scales.

The ED-specific residual is structurally identified for completeness; its empirical observability requires specialized regimes (substrate-scale probes, extreme acoustic frequencies near $\tau_\mathrm{V1}$, or non-Newtonian-fluid contexts where V5's INHERITED amplitude differs significantly from kinetic-theory expectation).

---

## 8. Implications for NS-2.06 (viscosity origin)

NS-2.06 must determine:

### 8.1 The viscosity coefficient $\mu_\mathrm{total}$

Three contributions identified in §7.2:
- $\mu_\mathrm{kin}$ — kinetic-theory contribution. Standard derivation: $\mu_\mathrm{kin} \sim n m \langle |\delta v|\rangle \lambda_\mathrm{mfp}$ in cgs-style kinetic theory. Substrate-level: chain mass + chain velocity fluctuation magnitude + chain-pair scattering mean free path. All three INHERITED.
- $\mu_\mathrm{V5}$ — cross-chain vacuum-mediated contribution. V5 amplitude INHERITED → $\mu_\mathrm{V5}$ INHERITED.
- $\mu_\mathrm{V1}$ — V1-memory-kernel time-integrated contribution. Determined by V1's specific functional form $G(\sigma/\ell_P^2)$ (form-FORCED per Theorem N1) and the integration over chain trajectories. *Possibly form-derivable* if V1's $G$-function specific form is fixed; *not form-derivable* if $G$'s specific form is INHERITED. Worth checking what Arc N N.4 specifies.

NS-2.06 should attempt a substrate-level derivation of $\mu_\mathrm{V1}$ from V1's finite-width form, even if $\mu_\mathrm{kin}$ and $\mu_\mathrm{V5}$ remain INHERITED. A partial form-derivation of $\mu_\mathrm{V1}$ would be a valuable result.

### 8.2 Whether viscosity is instantaneous or memory-kernel

§5 establishes that V1-mem coarse-grains to instantaneous at any NS scale; viscosity is therefore **instantaneous Newtonian** in the standard NS regime. NS-2.06 confirms this and reports the conditions (flow time scale vs τ_V1) under which the memory-kernel regime would activate (extreme regimes outside NS scope).

### 8.3 Whether ED-specific terms survive the continuum limit

§7.3 identifies two candidate ED-specific residuals:
- $\tau^{\mathrm{V5}, \mathrm{ED-spec}}$ — non-Newtonian cross-chain term; amplitude INHERITED; plausibly negligible at NS scales but not zero by structural argument.
- ℓ_P-derivative term — higher-derivative regularization; negligible at NS scales; structurally important for NS-3 smoothness preservation.

NS-2.06 should report what fraction of $\mu_\mathrm{total}$ comes from each substrate contribution and identify whether the V5-INHERITED part can be empirically isolated (e.g., from comparison to kinetic-theory-only predictions for dilute gases vs. dense fluids).

### 8.4 Connection to the queued diffusion-coarse-graining theorem

The Polya identification gap from NS-1.03 §3.2 enters NS-2.06 directly. A cleaner derivation of $\mu_\mathrm{kin}$ via substrate-level diffusion coarse-graining (rather than INHERITED kinetic-theory transport coefficients) would close one part of the value-INHERITED hierarchy. The diffusion-coarse-graining future-arc scoping memo's content connects to this directly; producing it before NS-2.06 lets NS-2.06 reference the scoping cleanly.

---

## 9. Recommended Next Steps

In priority order. NS-2.05 closes; load-bearing-hard work next concentrates in NS-2.06 with NS-2.07 to follow.

1. **Produce diffusion-coarse-graining future-arc scoping memo *before* NS-2.06.** File: `theory/Navier Stokes/Future_Arc_Diffusion_Coarse_Graining_Scoping.md` (or at `theory/` root). Its content connects directly to NS-2.06's $\mu_\mathrm{kin}$ derivation question (§8.4). Producing scoping first lets NS-2.06 reference the scoping cleanly when reporting which parts of $\mu_\mathrm{total}$ are amenable to substrate-level derivation vs. INHERITED. Cheap; recommended now. **Promoted from "optional" in earlier memos to "recommended before NS-2.06" given the §8.4 connection.**

2. **Draft NS-2.06 — viscosity / dissipation derivation.** File: `theory/Navier Stokes/NS-2.06_Viscosity.md`. Substantive but more bounded than NS-2.05 because the structural decomposition is now in hand. Three sub-tasks: (a) report $\mu_\mathrm{total} = \mu_\mathrm{kin} + \mu_\mathrm{V5} + \mu_\mathrm{V1}$ with each contribution's form-FORCED / value-INHERITED status; (b) attempt substrate-level derivation of $\mu_\mathrm{V1}$ from V1 finite-width kernel form (Theorem N1's $G$-function, conditional on whether $G$'s specific form is derivable from primitives); (c) confirm instantaneous-viscosity verdict at NS scales and report ED-specific term magnitudes (plausibly negligible). Estimated 1–2 sessions; cleaner than NS-2.05 because adjudication structure is established.

3. **Draft NS-2.07 — NS form synthesis + hand-off to NS-3.** File: `theory/Navier Stokes/NS-2.07_Synthesis.md`. Final NS-2 memo. Synthesizes NS-2.01 through NS-2.06 into the full NS form: continuity + momentum balance with τ decomposed + (compressible: energy equation). Reports ED's NS form: standard Newtonian-fluid form + structurally-identified ED-specific residual (plausibly negligible at NS scales). Hand-off to NS-3 explicit: substrate cutoff ℓ_P provides automatic regularization at substrate scale (Q.8 / T19); whether it survives to suppress finite-time singularities at the continuum limit is NS-3's question.

4. **Status checkpoint at NS-2.05 close.** Five of seven NS-2 memos closed (NS-2.01–NS-2.05); two remaining (NS-2.06, NS-2.07). Load-bearing-hard work largely complete; NS-2.06 / NS-2.07 are mechanical from this point. NS-3 (smoothness preservation) remains the absolute peak stall risk in the program but is post-NS-2.

### Decisions for you

- **Confirm the headline finding.** ED reproduces standard Newtonian-fluid stress at NS scales, with all three substrate contributions (τ^kin, τ^V5, τ^V1-mem) coarse-graining to the standard Newtonian deviatoric form. The form-FORCED / value-INHERITED hierarchy preserves cleanly; ED's NS form is consistent with empirical NS observations to the level allowed by INHERITED parameters. The two ED-specific residuals (V5-INHERITED non-Newtonian term + ℓ_P-derivative regularization) are flagged but plausibly negligible at NS scales.
- **Confirm P-2 reclassification.** NS-2.01 §5.3's three pressure candidates collapse to two at NS scales (P-1 kinetic, P-3 V5). P-2 (bandwidth-density gradient) was reclassified as the substrate origin of gravity rather than a pressure contribution. This is consistent with T19's substrate→Newton derivation; the bandwidth-density gradient contribution is already accounted for in $f^{\mathrm{ext}}$ via gravity, not in τ_ij.
- **Confirm proceeding with the diffusion-scoping memo as the next deliverable** before NS-2.06, given §8.4's structural connection.

---

*NS-2.05 decomposes τ_ij at NS scales into standard Newtonian-fluid stress (pressure + Newtonian viscous) plus a structurally-identified ED-specific residual that is plausibly negligible at NS scales. V5's amplitude-INHERITED status preserves form-FORCED / value-INHERITED methodology. V1-memory coarse-grains to instantaneous Newtonian viscosity at any NS scale. Three-candidate pressure framing from NS-2.01 collapses to two at NS scales (P-1 kinetic, P-3 V5; P-2 reclassified as gravity). NS-2.06 (viscosity origin) is the next memo and now bounded; NS-2.07 synthesis follows.*
