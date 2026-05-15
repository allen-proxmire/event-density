# Arc Hawking — Memo 1: Spectral Form and Temperature from V5 Cross-Chain Correlations

**Status:** Gate memo for Arc Hawking. Verdict determines downstream Arc Hawking memos. No new primitives. Identification-not-derivation discipline observed: standard Hawking-via-Bogoliubov calculation is identification target downstream, not derivation premise.

**Date:** 2026-05-09

---

## 1. The CANDIDATE Statement

Restated from H-0 §2.2 (pieces C1 and C2):

> **CANDIDATE (H1).** *At a saturated decoupling surface (a black-hole horizon in the substrate ontology), the V5 cross-chain correlations across the surface produce an emission spectrum that is thermal in form (Planck distribution per substrate mode), with the spectral temperature equal to $T_H = \kappa/(2\pi)$ where $\kappa$ is the surface gravity of the horizon.*

The CANDIDATE has two pieces:

- **(C1) Spectral form claim.** The V5 cross-chain correlation calculation produces a spectrum that is Planckian (thermal) in form for each substrate mode.
- **(C2) Temperature value claim.** The spectral temperature is $T = \kappa/(2\pi)$, matching Hawking's semiclassical result.

H-1 examines each. The argument runs through six structural steps: (i) the V5 cross-chain correlation function across a saturated surface, (ii) the substrate-level surface gravity $\kappa_{\mathrm{ED}}$, (iii) the substrate analog of the Rindler frame at the saturated surface, (iv) the substrate-Unruh argument for thermal correlations, (v) the identification of $\kappa_{\mathrm{ED}}$ with the standard surface gravity $\kappa$ via DCGT, (vi) the redshift-equivalence argument that produces Hawking from substrate-Unruh.

The honest framing: the substrate calculation is structurally analogous to the Hawking-as-Unruh derivation in standard general relativity. The framework's contribution is the substrate-level account of why this calculation produces the right temperature, not a new derivation route. The Unruh-analog approach has been used elsewhere in the framework (notably in T19 Newton-recovery) and is acknowledged in the Investigation Priority List as a known imported scaffolding that future work could replace with an ED-native derivation.

---

## 2. Substrate Inputs and the Assumption Audit

The derivation uses only the following inputs (each FORCED-unconditional, primitive, or canonical guardrail at the time of writing):

| Input | Status | Role |
|---|---|---|
| **V5 finite-width memory kernel** | Substrate primitive | The cross-chain memory kernel that does the substrate work for the spectrum |
| **V1 forward-cone-only kernel (T18)** | FORCED-unconditional | Cross-chain correlations propagate causally; no acausal vacuum-state contributions |
| **BH-2 (horizon as saturated decoupling surface)** | Closed-arc inheritance | Identifies *where* the calculation happens; supplies the substrate state at the surface |
| **BH-4 (asymmetric participation flow)** | Closed-arc inheritance | Identifies *what* drives the emission; supplies the substrate mechanism |
| **DCGT (substrate-to-continuum bridge)** | FORCED structural-foundation | Identifies $\kappa_{\mathrm{ED}}$ with continuum $\kappa$ at leading-order coarse-graining |
| **Cross-chain bandwidth $\Gamma_{\mathrm{cross}} \sim \exp[-\alpha \int \sigma\, d\ell]$** | DCGT-derived | Sets the substrate-rate of correlation suppression near the saturated surface |
| **Sparsity $\sigma$, multiplicity $\mathcal{M}$, unresolvedness $\mathcal{U}$** | Q-COMPUTE Memo 1, BH-2 | Substrate-state quantities at the surface |
| **T19 (Newton-recovery $\ell_P$)** | Closed-arc inheritance | Identifies the substrate length scale |
| **Substrate locality** | Substrate primitive | Restricts cross-chain correlations to substrate-locality-permitted pathways |
| **P11 (commitment irreversibility)** | Substrate primitive | Provides the substrate-time arrow consistent with the asymmetric participation flow |
| **Standard Unruh effect / KMS condition** | External mathematical physics | Identification target; the substrate calculation is identified with the standard Unruh-thermality argument, not derived from it |

**No new primitives introduced.** **No use of standard Hawking-via-Bogoliubov as a derivation premise** — only as identification target downstream.

---

## 3. The V5 Cross-Chain Correlation Function at a Saturated Decoupling Surface

The first structural step is to set up the substrate-level correlation function whose spectral content is the load-bearing object of the calculation.

### 3.1 Geometry of the saturated decoupling surface

By BH-2, a saturated decoupling surface is a substrate region where cross-chain bandwidth across it has fallen below the hydrodynamic-window resolution. Per BH-2 closure, the surface is characterized by:

- A specific substrate location where $\sigma(\mathbf{x})$ takes its substrate-saturation value $\sigma_{\mathrm{sat}}$.
- An exponential suppression of $\Gamma_{\mathrm{cross}}$ across the surface, with the path-integral $\int \sigma\, d\ell$ rising sharply as the path crosses the surface.
- A stationary substrate-time structure: the surface persists in substrate-time without dissolving (this corresponds to the standard "stationary horizon" assumption in semiclassical Hawking).

Set up local coordinates near the surface. Let $r$ denote a substrate-distance coordinate normal to the surface, with $r = 0$ at the surface, $r > 0$ in the exterior region (where chains can propagate), and $r < 0$ in the interior region (which is excluded from the chain's accessible substrate).

Near $r = 0$, expand the gradient sparsity:

```
σ(r) ≈ σ_sat + r · (∇σ)|_surf + O(r²)
```

The surface gradient $(\nabla \sigma)|_{\mathrm{surf}}$ is the load-bearing quantity for what follows. Define:

```
κ_ED ≡ α · (∇σ)|_surf
```

with units of inverse-length-squared corrected to inverse-length via the substrate's $\alpha$ prefactor and $\ell_P$. The numerical value of $\alpha$ is INHERITED from V1-kernel + DCGT closed-form details.

**$\kappa_{\mathrm{ED}}$ is the substrate-level surface gravity.** It measures the rate at which $\sigma$ rises at the saturated surface, scaled by the substrate's path-suppression coefficient.

### 3.2 The V5 correlation function

Define the V5 cross-chain correlation function across the saturated surface:

```
G_V5(t_1, x_1; t_2, x_2) ≡ ⟨V_5(t_1, x_1) V_5†(t_2, x_2)⟩_substrate
```

evaluated on the substrate's saturated-surface state. The expectation value is taken in the substrate's V5 vacuum (the substrate analog of the Boulware or Unruh vacuum, depending on which substrate-state is appropriate).

For two points $\mathbf{x}_1$ and $\mathbf{x}_2$ on the surface or near it, with both in the exterior region $r > 0$, the correlation function is governed by:

- The V5 kernel's intrinsic structure (forward-cone-only by inheritance from T18, finite-width by V5 primitive properties).
- The substrate-state's response to the saturated-surface geometry.
- Substrate locality: the correlation is supported on substrate-locality-permitted pathways between $\mathbf{x}_1$ and $\mathbf{x}_2$.

### 3.3 Substrate-time invariance assumption

For a stationary saturated surface, the substrate-state is invariant under translations in a "Killing-like" substrate-time direction. Formally:

```
G_V5(t_1 + s, x_1; t_2 + s, x_2) = G_V5(t_1, x_1; t_2, x_2)   for all s
```

This is the standard stationary-horizon assumption translated to the substrate level. It allows the correlation function to be Fourier-decomposed in $\Delta t = t_1 - t_2$ rather than depending on $t_1$ and $t_2$ separately.

**Status of substrate-time invariance:** CONDITIONAL. Stationary horizons satisfy this trivially; dynamical horizons (forming horizons during gravitational collapse, evaporating horizons in the late stages of BH lifetime) do not. The substrate-Hawking calculation as developed here applies to stationary horizons; extensions to dynamical horizons are downstream content.

### 3.4 The frequency-domain correlation function

Define the frequency-domain spectral function:

```
G̃_V5(ω, x_1, x_2) ≡ ∫ dΔt · e^(iωΔt) · G_V5(Δt, x_1, x_2)
```

The Hawking-spectrum question becomes: what is the structure of $\tilde G_{V5}(\omega)$ for $\omega > 0$ (positive-frequency modes that escape to infinity)? If $\tilde G_{V5}(\omega) \propto 1/(e^{\beta\omega} - 1)$ for some $\beta$, the substrate produces a Planck-distributed thermal spectrum. The temperature is then $T = 1/\beta$.

This is the load-bearing computation of H-1.

---

## 4. Substrate-Level Surface Gravity and the Rindler-Like Substrate Frame

### 4.1 The substrate's accelerated frame near the surface

Near a saturated decoupling surface, the substrate-state has an asymmetric structure that can be coordinatized in a way analogous to the Rindler frame in standard physics. The construction is parallel to the standard Schwarzschild-near-horizon-becomes-Rindler argument.

Introduce a new substrate-distance coordinate $\rho$ via:

```
r = ρ² / (2/κ_ED)   ⟺   ρ = √(2r/κ_ED)
```

In the $(\rho, t)$ coordinates near the surface, the substrate's local geometry has the structure of an accelerating frame. Substrate observers at fixed $\rho$ experience proper substrate-acceleration:

```
a(ρ) = κ_ED / (κ_ED · ρ) = 1/ρ
```

The substrate-state is invariant under translations along the surface but has a specific accelerating-frame structure perpendicular to it.

### 4.2 The substrate analog of the Unruh effect

The substrate's V5 vacuum state, viewed from a substrate observer at fixed $\rho$ (who is therefore accelerated in the asymptotic substrate frame), appears thermal. This is the substrate analog of the Unruh effect.

The substrate Unruh argument runs as follows:

(i) The substrate's V5 vacuum state is defined relative to substrate observers at rest in the asymptotic frame (those for whom the substrate's vacuum is "empty").

(ii) An accelerated substrate observer (at fixed $\rho$ near the saturated surface) traces a non-trivial trajectory through the substrate's vacuum state. The accelerated observer's substrate-time evolution corresponds to a substrate-state restricted to a Rindler-wedge-like region rather than the full substrate.

(iii) The reduction of the substrate's vacuum state to the Rindler-wedge-like region produces a substrate-mixed-state that is thermal at temperature:

```
T_Unruh = a / (2π) = 1 / (2πρ)
```

This is the substrate-level Unruh effect: an accelerated observer in the substrate sees thermal radiation at temperature proportional to the proper acceleration.

### 4.3 What the Unruh-analog argument depends on

The substrate-Unruh argument depends structurally on:

- The V5 vacuum state having a specific structure that, under substrate analytic continuation, exhibits the Euclidean periodicity required for thermal correlations. This is the substrate analog of the Wightman vacuum being a positive-frequency state in standard QFT.
- The substrate-time invariance of §3.3 (stationary surface).
- The substrate's "Killing-like" direction near the surface having the same algebraic structure as a Rindler boost.

**Status of substrate-Unruh argument:** identification with the standard Unruh effect, via the substrate-to-continuum coarse-graining of DCGT. The substrate's V5 vacuum at leading-order coarse-graining identifies with the standard Minkowski vacuum that the Unruh effect operates on. The acceleration $a$ identifies with the substrate-level proper acceleration.

This identification is FORCED at leading order via DCGT. Substrate-cutoff corrections at $(\ell_P/\rho)^2$ would produce departures from the strict Unruh result; these are first-subleading-order effects analogous to the substrate-cutoff corrections in NS (the R1 hyperviscous term) and Yang-Mills (the mass-gap mechanism). For the leading-order Hawking calculation, substrate-cutoff corrections are negligible.

---

## 5. The Imaginary-Time Periodicity (the Load-Bearing Step)

The substrate's V5 vacuum state, restricted to the Rindler-wedge-like region near the saturated surface, exhibits imaginary-time periodicity that is the substrate analog of the Euclidean trick in standard physics.

### 5.1 The Euclidean continuation in substrate-time

Consider the V5 correlation function $G_{V5}(\Delta t)$ for two points on the saturated surface separated by substrate-time $\Delta t$. Under analytic continuation $\Delta t \to -i\Delta\tau$, the correlation function becomes:

```
G_V5^E(Δτ) ≡ G_V5(-iΔτ)
```

For substrate-states with the appropriate analytic structure (positive-frequency vacuum states, by the substrate analog of the standard QFT positivity-of-spectrum condition), the Euclidean correlation function is well-defined for $\Delta\tau$ in some strip in the complex plane.

### 5.2 The periodicity argument

Near the saturated surface, the substrate's local structure (in $(\rho, t)$ coordinates) has a Lorentzian-to-Euclidean continuation with the property that the substrate-time direction becomes an angular coordinate. Specifically:

In Lorentzian substrate-time: $ds^2_{\mathrm{sub}} \approx -\rho^2 \kappa_{\mathrm{ED}}^2\, dt^2 + d\rho^2 + (\text{transverse})$

Under $t \to -i\tau$: $ds^2_{\mathrm{sub}} \to \rho^2 \kappa_{\mathrm{ED}}^2\, d\tau^2 + d\rho^2 + (\text{transverse})$

This is the substrate analog of flat 2D Euclidean space in polar coordinates, with $\rho$ as the radial coordinate and $\kappa_{\mathrm{ED}}\tau$ as the angular coordinate. To avoid a substrate-level conical singularity at $\rho = 0$ (the saturated surface itself), the angular coordinate $\kappa_{\mathrm{ED}}\tau$ must have period $2\pi$:

```
κ_ED · τ ∈ [0, 2π)   ⟺   τ ∈ [0, 2π/κ_ED)
```

Substrate-time, analytically continued to $\tau$, has period $\beta = 2\pi/\kappa_{\mathrm{ED}}$.

### 5.3 What "no substrate-level conical singularity" means

In standard physics, the no-conical-singularity argument is geometric: the Euclidean continuation of the metric must be smooth at the bifurcation point of the Killing horizon, which constrains the periodicity of the imaginary time.

The substrate-level statement is: the substrate's V5 vacuum state must be self-consistent at the saturated surface. A conical singularity in the analytically continued substrate would correspond to a discontinuity in the V5 correlations as the imaginary substrate-time circle is traversed. Such a discontinuity would mean the substrate's vacuum state is not a single coherent substrate object but rather two separate substrate states glued together inconsistently. The substrate's locality (P02) and continuity-under-DCGT-coarse-graining forbid such discontinuities at the substrate-vacuum level.

The periodicity $\beta = 2\pi/\kappa_{\mathrm{ED}}$ is therefore FORCED by substrate-vacuum self-consistency at the saturated surface, in parallel with the standard no-conical-singularity argument in QFT-in-curved-spacetime.

### 5.4 KMS condition equivalent

A correlation function periodic in imaginary time with period $\beta$ satisfies the KMS condition:

```
G_V5(-iβ + Δt, x_1, x_2) = G_V5(Δt, x_2, x_1)
```

The KMS condition is mathematically equivalent to thermal correlations at temperature $T = 1/\beta$. This is a theorem of standard mathematical physics (Kubo, Martin, Schwinger 1957–1959), inherited as identification target.

The substrate's V5 correlation function across the saturated surface, satisfying the imaginary-time periodicity argued in §5.3, therefore satisfies the KMS condition at temperature:

```
T = 1/β = κ_ED / (2π)
```

This is the substrate-level temperature of the V5 cross-chain correlations across the saturated decoupling surface.

### 5.5 Status of the periodicity argument

The imaginary-time periodicity at $\beta = 2\pi/\kappa_{\mathrm{ED}}$ is FORCED at the substrate level by:

- V5 vacuum self-consistency at the saturated surface (substrate-level no-conical-singularity).
- Substrate locality and DCGT continuity preventing discontinuities at the substrate-vacuum level.
- The substrate-time invariance of stationary saturated surfaces.

The argument is structurally parallel to the standard Euclidean-trick derivation of Hawking temperature, with the substrate's V5 vacuum playing the role of the Wightman vacuum in standard QFT.

The load-bearing step is the no-substrate-conical-singularity argument. This argument is FORCED at the substrate level for stationary saturated surfaces but requires the substrate's continuity-under-DCGT to extend to imaginary substrate-time. This is a non-trivial extension that the framework's primitives support but that has not been independently verified outside the substrate-Hawking context.

**Status: FORCED-CONDITIONAL.** Forced given the substrate's imaginary-time analytic structure being well-behaved (which is part of the substrate's continuity-under-DCGT inheritance). Conditional on the substrate's analytic-continuation behavior matching the standard QFT analytic-continuation behavior — an assumption that DCGT supports at leading order but that has not been independently checked.

---

## 6. From Imaginary-Time Periodicity to Planck Distribution

### 6.1 Spectral form from KMS

The KMS condition at temperature $T = 1/\beta$ implies that the spectral function $\tilde G_{V5}(\omega)$ has the Bose-Einstein structure:

```
G̃_V5(ω) ∝ 1 / (e^(βω) - 1)   for ω > 0
```

(For fermionic substrate-modes, the corresponding structure would be Fermi-Dirac: $\tilde G(\omega) \propto 1/(e^{\beta\omega} + 1)$. The V5 kernel mediates bosonic substrate excitations under standard substrate-mode classification.)

This is the Planck distribution: per substrate mode, the occupation number is $n(\omega) = 1/(e^{\beta\omega} - 1)$, identical in functional form to the standard photon-mode occupation in a thermal cavity at temperature $T$.

### 6.2 What this delivers

(C1) — the spectral form claim — is now FORCED. The V5 cross-chain correlation function across a saturated decoupling surface, under the substrate-Unruh / imaginary-time-periodicity argument, produces a Planck distribution per mode at temperature $T = \kappa_{\mathrm{ED}}/(2\pi)$.

The spectral form is FORCED by:

- The KMS condition equivalent (mathematical theorem applied to imaginary-time-periodic correlation functions).
- The imaginary-time periodicity at $\beta = 2\pi/\kappa_{\mathrm{ED}}$ from §5.
- The substrate's V5 kernel structure providing the substrate-level bosonic vacuum that the calculation operates on.

No auxiliary assumption is required beyond what was already FORCED in §5.

### 6.3 Spectrum at infinity

The Planck distribution at $T = \kappa_{\mathrm{ED}}/(2\pi)$ describes the V5 correlations evaluated *at the saturated surface*. The radiation observed at substrate-asymptotic infinity is the gravitationally-redshifted version. In the substrate ontology:

- Substrate observers at fixed $\rho$ near the surface see a thermal spectrum at $T_{\mathrm{local}} = a/(2\pi) = 1/(2\pi\rho)$.
- Substrate observers at substrate-asymptotic infinity see the redshifted spectrum.
- The redshift factor is $\sqrt{1 - 2M/r}$ in standard Schwarzschild coordinates, which approaches $\rho \kappa_{\mathrm{ED}}$ near the surface.

Combining: $T_{\mathrm{infinity}} = T_{\mathrm{local}} \cdot \rho \kappa_{\mathrm{ED}} = \kappa_{\mathrm{ED}}/(2\pi)$.

The redshift cancels the local proper-acceleration factor, leaving the asymptotic temperature equal to $\kappa_{\mathrm{ED}}/(2\pi)$. This is the substrate analog of the standard Hawking-Unruh equivalence.

---

## 7. Identification with Standard Hawking Temperature

The substrate calculation produces $T = \kappa_{\mathrm{ED}}/(2\pi)$. To recover the standard Hawking result $T_H = \kappa/(2\pi)$, the substrate-level surface gravity $\kappa_{\mathrm{ED}}$ must identify with the standard surface gravity $\kappa$.

### 7.1 The DCGT identification

DCGT establishes the substrate-to-continuum bridge for substrate-state quantities. At leading-order coarse-graining, substrate-state quantities identify with their continuum-level counterparts:

- Substrate gradient sparsity $\sigma$ identifies with continuum-level gradient density.
- Substrate-level V1 kernel parameters identify with continuum-level vacuum coupling.
- Substrate-level surface gravity $\kappa_{\mathrm{ED}}$ identifies with continuum-level surface gravity $\kappa$ at the horizon.

The identification $\kappa_{\mathrm{ED}} = \kappa$ at leading order is FORCED by DCGT's substrate-to-continuum bridge applied to the saturated decoupling surface.

### 7.2 The standard surface gravity $\kappa$

The standard surface gravity $\kappa$ at a Schwarzschild black-hole horizon is:

```
κ = c⁴ / (4GM) = 1 / (4M)   in geometrized units
```

For other classes of black holes:
- Reissner-Nordström (charged): $\kappa = (M^2 - Q^2)^{1/2} / (2M(M + (M^2 - Q^2)^{1/2}))$
- Kerr (rotating): $\kappa = \sqrt{M^2 - a^2} / (2M(M + \sqrt{M^2 - a^2}))$ for the outer horizon

The substrate-level $\kappa_{\mathrm{ED}}$ identifies with each of these in the appropriate substrate state.

### 7.3 The recovered Hawking temperature

Combining the substrate calculation $T = \kappa_{\mathrm{ED}}/(2\pi)$ with the DCGT identification $\kappa_{\mathrm{ED}} = \kappa$:

```
T_H = κ / (2π)
```

For Schwarzschild: $T_H = 1/(8\pi M)$ in geometrized units, or $T_H = \hbar c^3/(8\pi G M k_B)$ in SI units.

This is the standard Hawking temperature. **(C2) is FORCED via identification with standard semiclassical Hawking through DCGT.**

### 7.4 Substrate-cutoff corrections (preview of H-4)

The leading-order identification $\kappa_{\mathrm{ED}} = \kappa$ holds at order $(\ell_P/R_{cg})^0$. At first subleading order $(\ell_P/R_{cg})^2$, substrate-cutoff corrections to both $\kappa_{\mathrm{ED}}$ and the spectral form produce departures from the strict Hawking result. These are the substrate-level predictions distinguishing ED from semiclassical Hawking.

For Schwarzschild horizons of stellar mass (M ~ M_sun ~ $10^{38}\, \ell_P$), the ratio $\ell_P/M$ is of order $10^{-38}$, so substrate-cutoff corrections are negligible at observable scales. For primordial black holes evaporating now, $\ell_P/M$ is of order $10^{-7}$ near the end of evaporation, so substrate-cutoff corrections become observable in principle.

H-4 develops the high-frequency cutoff in detail. For H-1, the leading-order Hawking-temperature recovery is the load-bearing result; the cutoff is downstream content.

---

## 8. Verdict

> **VERDICT (H1): FORCED at leading order, with explicit conditional on the substrate-Unruh identification.**
>
> The V5 cross-chain correlations across a saturated decoupling surface produce a Planck-distributed thermal spectrum at temperature $T_H = \kappa/(2\pi)$ via:
> - (C1) FORCED: the V5 vacuum's imaginary-time periodicity at $\beta = 2\pi/\kappa_{\mathrm{ED}}$ from substrate-vacuum self-consistency at the saturated surface (no-substrate-conical-singularity argument), combined with the KMS-condition equivalent of imaginary-time-periodic correlation functions.
> - (C2) FORCED-via-DCGT-identification: the substrate-level surface gravity $\kappa_{\mathrm{ED}}$ identifies with the standard surface gravity $\kappa$ at leading-order coarse-graining via DCGT's substrate-to-continuum bridge.
>
> The argument is structurally parallel to the Hawking-as-Unruh derivation in standard general relativity, with the substrate's V5 vacuum playing the role of the Wightman vacuum in standard QFT, and DCGT providing the identification that makes the substrate calculation match the semiclassical result at leading order.

**Trending toward YES.** The framework structurally recovers Hawking via the substrate-Unruh argument applied at the saturated decoupling surface. The temperature $T_H = \kappa/(2\pi)$ is reproduced exactly at leading order. Substrate-cutoff corrections at $(\ell_P/M)^2$ produce departures developed in H-4.

**Verdict-class details:**

- **Form-FORCED:** Planck distribution per mode, periodicity $\beta = 2\pi/\kappa_{\mathrm{ED}}$, redshift cancellation between local-acceleration temperature and asymptotic temperature.
- **Value-FORCED-via-identification:** $T = \kappa/(2\pi)$ via DCGT identification of $\kappa_{\mathrm{ED}}$ with $\kappa$.
- **CONDITIONAL caveat:** the substrate-Unruh identification depends on the substrate's V5-vacuum analytic-continuation structure matching the standard QFT analytic structure. This is supported by DCGT continuity at leading order but has not been independently verified outside the substrate-Hawking context.
- **No NOT-FORCED option survived.** The substrate calculation produces the correct spectral form and temperature at leading order without any substrate-level deviation that could refute Hawking.
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {} as of arc-opening tally.

---

## 9. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| Standard Hawking-via-Bogoliubov used as derivation premise? | **No.** Standard Hawking calculation appears in §1, §6.3 (redshift equivalence), §7 (identification target) but never as a derivation step. The substrate-Unruh argument and the imaginary-time periodicity argument are derived from substrate primitives in §3–§5, then identified with the standard Hawking result in §7. Identification, not derivation. |
| Standard Unruh effect used as derivation premise? | **No.** The Unruh-effect mathematical machinery (KMS condition, imaginary-time periodicity, thermal correlation functions) is used in §5–§6 as identification target — the substrate calculation matches the structure of the Unruh derivation when the substrate-Unruh identification is made. The substrate-level argument for $\beta = 2\pi/\kappa_{\mathrm{ED}}$ is the no-substrate-conical-singularity argument from V5-vacuum self-consistency, not the standard Wightman-vacuum argument. |
| Self-reference of H-1 within itself? | **No.** §3 → §4 → §5 → §6 → §7 derivation chain is acyclic. |
| BH-2 / BH-4 / DCGT used only as inputs? | **Confirmed.** BH-2 supplies the saturated-surface state; BH-4 supplies the asymmetric-flow mechanism; DCGT supplies the identification bridge. None re-derived. |
| H-2 through H-7 used as derivation premises? | **No.** None invoked. H-1 is structurally upstream of all other Arc Hawking memos. |

**Acyclicity confirmed.**

---

## 10. Falsification

### 10.1 Falsifier for FORCED-at-leading-order verdict (current verdict)

A substrate construction satisfying all of V5, BH-2, BH-4, T18, DCGT, and substrate locality, in which the V5 cross-chain correlation function across a saturated decoupling surface fails to produce a Planck-distributed spectrum at $T = \kappa/(2\pi)$. Concretely:

- (a) V5 correlations that fail to satisfy imaginary-time periodicity at $\beta = 2\pi/\kappa_{\mathrm{ED}}$ — would refute the no-substrate-conical-singularity argument or expose a hidden non-stationary substrate structure.
- (b) A substrate-level identification of $\kappa_{\mathrm{ED}}$ with continuum $\kappa$ that fails at leading-order coarse-graining — would refute DCGT's substrate-to-continuum bridge in this regime.
- (c) A substrate-level non-thermal spectrum produced by the V5 correlations at the saturated surface — would refute one of (a) or (b) above.

Each refutation would downgrade the verdict from FORCED to CONDITIONAL or NOT FORCED.

### 10.2 Empirical-side falsifier

Any empirical observation of black-hole radiation that deviates from Hawking's predicted thermal spectrum at temperature $T_H = \kappa/(2\pi)$ within experimental precision would falsify both ED's leading-order prediction and standard semiclassical Hawking. Such observations are not currently available at the gravitational scale (no direct detection of Hawking radiation from astrophysical BHs); analog Hawking radiation in BEC and acoustic systems matches the spectral form within experimental uncertainty.

### 10.3 Substrate-cutoff observable predictions (preview of H-4)

ED predicts substrate-cutoff corrections at first subleading order $(\ell_P/M)^2$. These produce:
- A high-frequency cutoff in the Hawking spectrum at $\omega \sim \ell_P/M^2$ (or similar dimensional combination).
- Modifications to the Page evaporation rate at order $(\ell_P/M)^2$.

These are the framework's *new* predictions that distinguish ED from strict semiclassical Hawking. They are observable in principle for primordial BHs evaporating now, where the cutoff scale becomes accessible.

H-4 develops these predictions in detail. For H-1, the leading-order Hawking-temperature recovery is the load-bearing result.

### 10.4 Subtle structural test

The framework's substrate-Unruh argument depends on the substrate's V5 vacuum exhibiting the correct analytic-continuation structure. A more careful examination of the V5 vacuum's analytic properties — possibly in a future memo H-1.5 or in extensions to non-stationary horizons — could reveal whether the substrate-Unruh identification is genuinely FORCED or has hidden dependencies on the standard QFT analytic structure.

---

## 11. Consequences for the Arc

1. **H-1 closes as the gate memo.** Arc Hawking can now proceed to H-2 (greybody factors), H-3 (Page rate), H-4 (V5 cutoff), H-5 (information correlations), H-6 (semiclassical equivalence), and H-7 (synthesis).

2. **The substrate-Unruh argument is now a working substrate-level tool.** The same argument that produces $T_H = \kappa/(2\pi)$ at a saturated decoupling surface produces $T_U = a/(2\pi)$ for a uniformly accelerated substrate observer. The substrate-Unruh argument is a separate substrate-level result that may warrant its own walkthrough in the future.

3. **H-2 (greybody factors) is structurally enabled.** The Planck distribution per mode is now in hand; greybody factors are multiplicative modifications that depend on substrate-channel-coupling effects. H-2 develops the substrate-level mechanism for these factors.

4. **H-3 (Page rate) is structurally enabled.** Integrating the Planck distribution over modes produces a total emission rate. The Page evaporation rate $\dot M = -\hbar c^4/(15360 \pi G^2 M^2)$ should follow at leading order, with the specific numerical coefficient INHERITED from substrate-mode counting.

5. **H-4 (V5 cutoff) is the most distinctive ED prediction.** With H-1 producing leading-order Hawking, H-4's first-subleading-order cutoff is where ED departs from strict semiclassical Hawking. The cutoff scale is at $\omega \sim 1/(\ell_P \kappa)$ or similar substrate-cutoff combination, suppressed by $(\ell_P/M)^2$ at leading order.

6. **H-5 (information correlations) couples cleanly with E-arc inheritance.** The bandwidth-budget mechanism that produces E-4 monogamy is the same substrate machinery operating at the saturated surface. Information-content correlations between Hawking-radiated quanta and interior-fallen matter inherit the entanglement-straddling structure from BH-4 plus the bandwidth-budget structure from E-4.

7. **Cross-domain echo with Arc D becomes concrete.** V5 produces Maxwell viscoelastic memory in soft matter (DCGT consequence) AND Hawking thermal spectrum at BH horizons (this memo). Same kernel, two physical applications. H-7 develops this echo explicitly.

8. **One sensitivity flag.** The §3.3 substrate-time invariance assumption (stationary saturated surfaces) is load-bearing. Extensions to dynamical horizons (forming, evaporating) require relaxing this assumption and may produce non-stationary corrections to the spectrum.

9. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {} as of arc-opening tally.

---

## 12. Summary

**What this memo accomplished.**

- Stated the H-1 CANDIDATE (§1) decomposing it into (C1) spectral form and (C2) temperature value.
- Set up the V5 cross-chain correlation function across a saturated decoupling surface, with substrate coordinates $(\rho, t)$ near the surface and substrate-level surface gravity $\kappa_{\mathrm{ED}} = \alpha (\nabla \sigma)|_{\mathrm{surf}}$ (§3, §4).
- Derived the substrate-Unruh effect: substrate observers accelerated near the saturated surface see a substrate-thermal spectrum at $T = a/(2\pi)$ (§4).
- Established the imaginary-time periodicity at $\beta = 2\pi/\kappa_{\mathrm{ED}}$ from the no-substrate-conical-singularity argument (V5-vacuum self-consistency at the saturated surface), combined with the KMS-condition equivalent (§5).
- Produced the Planck-distributed spectrum from the KMS condition (§6).
- Identified $\kappa_{\mathrm{ED}} = \kappa$ at leading-order DCGT coarse-graining, recovering the standard Hawking temperature $T_H = \kappa/(2\pi)$ (§7).
- Issued the verdict: **FORCED at leading order**, trending toward YES on the structural-recovery question (§8).
- Confirmed acyclicity (§9) and provided substrate-level + empirical falsifiers (§10).

**Trending toward YES on H1 structural recovery of Hawking.** The framework structurally recovers the Hawking spectrum and temperature via the substrate-Unruh argument at the saturated decoupling surface. The argument is structurally parallel to the standard Hawking-as-Unruh derivation, with DCGT providing the identification that makes the substrate calculation match the semiclassical result at leading order. Substrate-cutoff corrections at first subleading order produce ED-distinctive predictions developed in H-4.

**Brief 2–3 sentence summary:** The V5 cross-chain correlations across a saturated decoupling surface satisfy imaginary-time periodicity at $\beta = 2\pi/\kappa_{\mathrm{ED}}$ via a substrate-level no-conical-singularity argument, which produces a Planck-distributed thermal spectrum at temperature $T = \kappa_{\mathrm{ED}}/(2\pi)$ via the KMS-condition equivalent. Identifying $\kappa_{\mathrm{ED}}$ with the standard surface gravity $\kappa$ via DCGT's substrate-to-continuum coarse-graining yields the Hawking temperature $T_H = \kappa/(2\pi)$ at leading order, structurally recovering the semiclassical Hawking result through the substrate-Unruh equivalence. The argument is FORCED at leading order with substrate-cutoff corrections at first subleading order distinguishing ED from strict semiclassical Hawking — the latter developed in H-4.

---

## 13. Recommended Next Steps

Multiple options, in decreasing order of immediate Arc Hawking productivity:

1. **H-4 (V5 cutoff at first subleading order) — RECOMMENDED.** The most ED-distinctive piece of content in the arc. With H-1 producing leading-order Hawking, H-4's substrate-cutoff corrections at $(\ell_P/M)^2$ produce specific predictions distinguishing ED from strict semiclassical Hawking. The cutoff scale is observable in principle for primordial BHs evaporating now, and would constitute a falsifiable substrate-level prediction. Estimated 1–2 sessions.

2. **H-2 (greybody factors).** Structurally cleanest follow-on after H-1. With the Planck distribution per mode in hand, greybody factors are the multiplicative modifications from substrate-channel-coupling effects. H-2 develops the substrate-level mechanism producing the standard greybody-factor structure $\Gamma_l(\omega)$. Estimated 1–2 sessions.

3. **H-5 (information correlations with cross-domain E-arc echo).** Most theoretically rich follow-on. The bandwidth-budget mechanism from Arc E plus BH-4 entanglement-straddling produces a substrate-level account of Hawking-quanta correlations with interior-fallen matter — i.e., a substrate-level account of the information-paradox-resolution content. Couples Arc Hawking with Arc E and Arc BH cross-domain unification structurally. Estimated 2–3 sessions.

4. **H-3 (Page rate).** Direct follow-on after H-1 + H-2. Integrating the Planck distribution (with greybody factors from H-2) produces the total emission rate, which should reproduce the standard Page rate $\dot M \propto 1/M^2$ at leading order. Estimated 1 session.

5. **(Defer) H-6 (semiclassical equivalence) and H-7 (synthesis).** These are the final memos; written after all structural derivation memos close.

6. **(Independent) Standalone walkthrough on the substrate-Unruh argument.** The substrate-Unruh effect is a separable substrate-level result that is now structurally available. A walkthrough in the `walkthroughs/` series — `from_primitives_to_substrate_unruh.md` — could derive the substrate-Unruh effect standalone and serve as a structural prerequisite for both Arc Hawking H-1 and any future arc on cosmological horizons / de Sitter thermality. Estimated 1–2 sessions for the walkthrough; would supplement the existing series.

---

**Pause for further instruction.**
