# Arc BH — Memo 6: Wave–Black-Hole Scattering

**Status:** Fifth technical memo of Arc BH. Substrate-derivation chain converting ED-I-26's interpretive content into a DCGT + acoustic-metric + SG-4 grounded account of wave–BH scattering.

**Date:** 2026-05-01

---

## 1. Purpose

This memo:

- Derives wave–black-hole scattering from ED substrate principles using DCGT (multi-scale channel propagation) + Arc ED-10 (acoustic-metric scalar-tensor approximation) + SG-4 (curvature-like participation structure).
- Shows how a **minimal ED-channel** (gravitational wave) — low-multiplicity, low-anisotropy participation pattern — interacts with a **maximal ED-structure** (black hole) — high-multiplicity, saturated-gradient region with decoupling surface.
- Produces the BHPT (black-hole perturbation theory) phase shift as a **global invariant** of the ED-channel: a path integral of the channel action over the propagation trajectory through the saturated-gradient region.
- Identifies the substrate origin of helicity preservation (Schwarzschild-like) and helicity flip (Kerr-like), and the substrate origin of the Kerr frame-dragging twist as integrated background vorticity.

Discipline: this memo is consolidation-pattern with derivation glue. The phase shift's existence and form are derived; specific numerical values for $\delta_{\ell m}$ are inherited from the acoustic-metric BHPT match, not produced de novo.

---

## 2. Upstream Foundations

- **ED-I-26** — interpretive picture: minimal ED-channels (waves) scatter off maximal ED-structures (BHs) with global phase shifts encoding the integrated channel action; helicity preservation under axisymmetric backgrounds; Kerr twist from frame-dragging.
- **BH-2** — horizon-as-decoupling-surface under DCGT. The propagation region accessible to the scattered channel is the exterior of $\Sigma_H$.
- **BH-3** — saturated participation zone interior + the gradient saturation condition $|\nabla\rho|\ell_P^2/\rho_\mathrm{local} \gtrsim \beta_\mathrm{crit}$ near $\Sigma_H$.
- **BH-4** — information/entanglement split: the scattered channel carries committed structure (the wave); horizon blocks committed structure but not entanglement. Scattering is exterior-only at the level of committed propagation.
- **Arc D (DCGT)** — multi-scale expansion + channel propagation kernels. The minimal channel is a coarse-grained excitation of the substrate that survives DCGT to a continuum wave equation.
- **Arc SG** — SG-4 modified Poisson / field equation supplies the participation profile $\rho(\mathbf{x})$ that defines the background; SG-6 weak-field prerequisites bridge to the metric reading.
- **Arc ED-10** — acoustic-metric scalar-tensor approximation. The minimal channel's effective continuum equation is the wave equation on the acoustic metric. ED-Phys-10 guardrails preserved: this is kinematic, not full GR.

---

## 3. Minimal ED-Channel: Substrate Definition

A **minimal ED-channel** (gravitational wave, in the continuum reading) is a substrate excitation characterized by:

- **Low multiplicity** — small number of participation degrees of freedom involved per coarse-graining cell. The channel is a perturbation rather than a structure.
- **Low anisotropy** — anisotropy tensor magnitude small compared to substrate-saturation; the channel's polarization is a small perturbation of the local participation isotropy.
- **DCGT-coherent propagation** — the channel survives multi-scale expansion to a coarse-grained continuum description: a wave equation on the acoustic metric $g_{\mu\nu}^\mathrm{ac}[\rho,\nabla\rho]$.

The channel's global phase along a propagation trajectory $\gamma(\lambda)$ is:

$$
\Phi[\gamma] = \int_\gamma \mathcal{A}(\rho,\nabla\rho,\text{anisotropy})\, d\lambda
$$

where $\mathcal{A}$ is the channel's substrate action density — the integrand that, after DCGT, reduces in the asymptotic region to the standard kinetic + dispersion terms of a wave on the acoustic metric. In the bulk of the propagation region, $\mathcal{A}$ inherits curvature-like contributions from the SG-4 participation profile.

Two structural points:

1. $\Phi[\gamma]$ is a path-functional, not a local quantity. It captures the *cumulative* effect of the channel's traversal through the participation-density profile.
2. The minimality of the channel (low multiplicity, low anisotropy) is what makes $\Phi$ a single scalar phase rather than a richer multi-component object. A high-multiplicity excitation would acquire a multi-component phase tensor; the wave channel is structurally simple enough that $\Phi$ collapses to a scalar (per polarization).

---

## 4. Maximal ED-Structure: Black Hole Background

A **maximal ED-structure** (black hole) is, in substrate terms:

- **High multiplicity** — large number of committed participation channels per coarse-graining cell in the central region.
- **Saturated-gradient** — interior obeys BH-3's saturation condition; exterior near $\Sigma_H$ has $|\nabla\rho|\ell_P^2/\rho_\mathrm{local}$ approaching the decoupling threshold from below.
- **Decoupling-surface bounded** — $\Sigma_H$ separates exterior (scattering region) from interior (saturated zone). Scattered channels propagate in the exterior.
- **Curvature-like participation structure** — given by SG-4: $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G\rho_m$ in the relevant weak-field regime; the participation profile $\rho(\mathbf{x})$ that follows produces, via Arc ED-10, an acoustic metric whose curvature is strong near $\Sigma_H$ and weak asymptotically.

In the BH-relevant regime the channel propagates through a region where (for $\mathbf{x}$ approaching $\Sigma_H$):

$$
|\nabla\rho|\,\ell_P^2/\rho_\mathrm{local} \gg 1
$$

and the acoustic metric is strongly curved. Asymptotically far from $\Sigma_H$, the gradient is small and the acoustic metric is nearly flat — the channel's action density $\mathcal{A}$ reduces to the free-wave form, and $\Phi$ accumulates only the asymptotic contribution.

The interesting structure — phase shifts, helicity behavior, twist — arises from the strong-curvature region where $\mathcal{A}$ deviates from its asymptotic form along the channel's trajectory.

---

## 5. Substrate Mechanism of Scattering

The mechanism:

1. The minimal channel's propagation kernel — the DCGT-emergent wave equation on the acoustic metric — is **distorted** by the maximal structure's saturated gradients. Strong $|\nabla\rho|$ contributes to the acoustic-metric curvature, which appears in $\mathcal{A}$ as a curvature-coupling term beyond the flat-space free-wave action.

2. The channel's global phase accumulates a shift relative to its asymptotic free-wave value:

$$
\delta_{\ell m} = \int_\mathrm{path} \Delta\mathcal{A}\, d\lambda
$$

where $\Delta\mathcal{A} = \mathcal{A}_\mathrm{full} - \mathcal{A}_\mathrm{asymptotic}$ is the curvature-induced excess action density along the trajectory.

3. The shift is **global** because the channel is minimal: the low-multiplicity, low-anisotropy structure means the shift collapses to a single scalar per partial-wave mode $(\ell,m)$, rather than a richer object. The mode decomposition $(\ell,m)$ is inherited from the asymptotic axisymmetric structure of the BH background, not derived de novo.

4. The shift is **inevitable** for any non-trivial channel trajectory through the strong-curvature region: the gradient saturation near $\Sigma_H$ (BH-3) guarantees $\Delta\mathcal{A} \neq 0$ along any trajectory that approaches the surface. There are no trajectories that thread the strong-curvature region without acquiring a phase shift.

5. The S-matrix structure $S = e^{iN}$ from ED-I-26 is recovered: $N$ is the integrated channel action, $\delta_{\ell m}$ are its partial-wave components, and unitarity of $S$ on a per-channel basis follows from the reality of $\mathcal{A}$ in the exterior region (no committed structure leaks into the interior — BH-4 — so no probability is lost from the scattering channel; entanglement-amplitude correlations with the interior persist but do not enter the exterior unitarity bookkeeping).

What is **derived** here:
- The form of the phase-shift as $\int \Delta\mathcal{A}\,d\lambda$.
- The fact that it is a global scalar invariant per partial-wave mode.
- The fact that it is inevitable (gradient saturation forces $\Delta\mathcal{A} \neq 0$).
- Unitarity of the scattering S-matrix on the exterior side.

What is **inherited**:
- The specific numerical values of $\delta_{\ell m}$ as functions of mode and frequency. These match the BHPT values to the extent that the acoustic-metric scalar-tensor reading reproduces the GR Schwarzschild/Kerr metric in the relevant regime — and Arc ED-10 establishes that as a conditional-positive verdict (acoustic-metric is kinematic, not full GR; matching depends on the SG-4 weak-field prerequisites). Numerical match for specific BH spectra is therefore conditional on the same prerequisites that Arc ED-10 / Arc SG flag as the limiting conditions.

---

## 6. Helicity Preservation and Flip

The channel's polarization is encoded in its anisotropy tensor. Polarization transport along the trajectory is governed by how the anisotropy basis evolves under the background participation profile.

**Helicity preservation (Schwarzschild-like):**

For axisymmetric, non-rotating backgrounds, the principal directions of the participation profile are aligned along the radial-tangential axes uniformly along the trajectory's symmetry plane. The channel's anisotropy tensor, parallel-transported along the trajectory, returns to itself up to an overall scalar phase.

Therefore:

- **Helicity is preserved** — the channel's circular-polarization eigenstates are eigenstates of the parallel transport.
- The phase shift acts identically on both helicity states: $\delta_{\ell m}^{(+)} = \delta_{\ell m}^{(-)}$.
- This recovers the standard Schwarzschild BHPT result that scattering is helicity-diagonal.

**Helicity flip channels (Kerr-like):**

For backgrounds with frame-dragging — i.e., a non-zero substrate-level vorticity $\boldsymbol{\omega}_\mathrm{FD}$ in the participation flow — the principal directions of the participation profile **rotate** along the trajectory. The channel's anisotropy tensor, parallel-transported through this rotating basis, picks up a **twist** relative to a non-rotating reference frame.

The accumulated twist is:

$$
\Delta\phi_\mathrm{twist} = \int \omega_\mathrm{FD}\, d\lambda
$$

where $\omega_\mathrm{FD}$ is the local frame-dragging angular velocity (the substrate-vorticity component along the trajectory's principal axis).

Consequences:

- The two circular-polarization eigenstates are no longer eigenstates of parallel transport; they couple via the twist.
- **Helicity flip channels open**: amplitudes for $|+\rangle \to |-\rangle$ become non-zero, scaling with $\Delta\phi_\mathrm{twist}$.
- This recovers the standard Kerr BHPT result that scattering is helicity-mixing, with mixing strength tied to spin parameter via $\omega_\mathrm{FD}$.

The mechanism is anisotropy-basis transport in a background with substrate-level vorticity. Helicity behavior is not put in by hand; it emerges from how the channel's polarization tensor evolves through the participation-flow profile.

---

## 7. Kerr Scattering: Global Twist

The Kerr phase shift relative to Schwarzschild has a substrate origin:

1. **Frame-dragging is a global rotation of the participation anisotropy basis.** A spinning maximal structure carries a non-zero substrate-level vorticity in its participation flow — a structural reading of the rotating-spacetime background.

2. **The channel acquires a twist proportional to integrated vorticity.** As the channel traverses the strong-curvature region, the rotation of the local anisotropy basis accumulates into the channel's transported polarization frame:

$$
\Delta\phi_\mathrm{twist} = \int \omega_\mathrm{FD}\, d\lambda.
$$

3. **The twist produces the Kerr scattering asymmetry.** Because the twist depends on the alignment of the channel's trajectory with the spin axis, scattering is no longer isotropic in the trajectory's azimuthal direction. Channels with trajectories prograde to the spin acquire a different twist than retrograde channels. This is the substrate origin of the prograde/retrograde asymmetry in Kerr scattering.

4. **Superradiance compatibility.** Superradiance — energy extraction from a Kerr BH by certain scattering channels — corresponds in this picture to channels whose interaction with the rotating participation flow nets a positive energy transfer from background to channel. The mechanism is consistent with BH-4: no committed structure is extracted from the interior; the energy transfer is mediated by the exterior participation flow's vorticity acting on the channel. A full superradiance derivation is not produced here; the structural compatibility is noted.

What is **derived**: Kerr twist as integrated frame-dragging vorticity along the trajectory; prograde/retrograde asymmetry from trajectory-dependent integration.
What is **inherited**: specific superradiance amplitudes, numerical values of the spin-dependent corrections to $\delta_{\ell m}$.

---

## 8. Structural Verdict

The structural conclusions of this arc are:

- **BHPT phase shift = global invariant of minimal ED-channel.** $\delta_{\ell m} = \int_\mathrm{path}\Delta\mathcal{A}\,d\lambda$, scalar per partial-wave mode, derived from substrate channel-action machinery.
- **Scattering is a global reorientation of the channel inside a saturated-gradient region.** Not a local interaction event; a cumulative path-integrated effect through the strong-curvature exterior of $\Sigma_H$.
- **Helicity behavior arises from anisotropy-basis transport.** Preservation under axisymmetric backgrounds; flip under backgrounds with substrate-level vorticity.
- **Kerr twist = integrated background vorticity.** Prograde/retrograde asymmetry derived from trajectory-dependence of the integral; superradiance structurally compatible (full derivation deferred).
- **Verdict: conditional-positive.** The form of every result is derived from substrate machinery. Numerical match to specific BHPT spectra is conditional on the same Arc ED-10 / Arc SG prerequisites that govern the acoustic-metric-as-kinematic reading. Same structural pattern as NS-Smoothness Intermediate Path C, Yang-Mills Clay-relevance, and the Arc ED-10 covariant scalar-tensor result.

---

## 9. Deliverables

This memo produces:

- A **substrate-derivation chain** for wave–BH scattering, routing ED-I-26's interpretive content through DCGT + Arc ED-10 + SG-4.
- A **derivation of the BHPT phase shift form** as $\delta_{\ell m} = \int_\mathrm{path}\Delta\mathcal{A}\,d\lambda$, with $\Delta\mathcal{A}$ the curvature-induced excess action density.
- A **substrate explanation of helicity preservation/flip**: anisotropy-basis parallel transport through axisymmetric (no flip) vs frame-dragging (flip) backgrounds.
- A **substrate explanation of Kerr twist** as integrated frame-dragging vorticity, with prograde/retrograde asymmetry derived and superradiance flagged structurally compatible.

Numerical-match deliverables are inherited (conditional on Arc ED-10 + Arc SG prerequisites), not de novo derived.

---

## 10. Recommended Next Step

Proceed to **Arc_BH_7_Synthesis.md** — Arc BH synthesis + Clay-relevance-style verdict. Closes the seven-memo arc by consolidating: BH-1 opening + BH-2 horizon-DCGT + BH-3 singularity/strong-curvature audit + BH-4 information/evaporation + BH-5 area-law entropy (form derived, $1/4$ INHERITED) + BH-6 wave-BH scattering. Issues the arc-level structural verdict on ED's account of black-hole architecture, identifies what is derived vs inherited vs deferred, and slots Arc BH into the program-level theorem inventory + publication-grade paper queue.

File path: `theory/Black_Holes/Arc_BH_7_Synthesis.md`. Estimated 1 session.
