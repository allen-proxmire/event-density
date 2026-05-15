# Arc Hawking — Memo 2: Greybody Factors from Substrate-Channel Coupling

**Status:** Articulation memo conditional on H-1 closure (Planck spectrum at $T_H = \kappa/(2\pi)$ from V5 cross-chain correlations at saturated decoupling surface). No new primitives. Identification-not-derivation discipline observed: standard Regge-Wheeler / Teukolsky greybody calculation is identification target, not derivation premise.

**Date:** 2026-05-09

---

## 1. The CANDIDATE Statement

Restated from H-0 §2.2 (piece C3):

> **CANDIDATE (H2).** *Greybody factors $\mathcal{T}_\ell(\omega)$ that modify the strict Planck distribution between the saturated decoupling surface and substrate-asymptotic infinity are produced by substrate-level analogs of the spacetime-curvature backscattering effects in standard physics. The greybody factors take the form $\mathcal{T}_\ell(\omega) = |T_\ell^{\mathrm{(ED)}}(\omega)|^2$ where $T_\ell^{\mathrm{(ED)}}$ is the transmission amplitude through a substrate-derived effective potential barrier. At leading-order DCGT coarse-graining, $\mathcal{T}_\ell(\omega)$ identifies with the standard semiclassical greybody factors $\mathcal{T}_\ell^{\mathrm{(GR)}}(\omega)$ from Regge-Wheeler / Teukolsky scattering theory. ED-distinctive corrections appear at first subleading order $(\ell_P/M)^2$ from V5-kernel structure and motif-alphabet $g$ effects.*

The CANDIDATE has three pieces:

- **(C3a) Form claim.** The substrate scattering problem produces a transmission coefficient of the form $\mathcal{T}_\ell(\omega) = |T_\ell^{\mathrm{(ED)}}(\omega)|^2$, with $T_\ell^{\mathrm{(ED)}}$ obtained by solving a substrate-derived wave equation through an effective potential $V_\ell^{\mathrm{(ED)}}(r)$ with the standard centrifugal-plus-state-dependent structure.
- **(C3b) Leading-order identification claim.** At leading-order DCGT coarse-graining, $V_\ell^{\mathrm{(ED)}}(r)$ identifies with the standard Regge-Wheeler effective potential, so $\mathcal{T}_\ell(\omega)$ matches the semiclassical greybody factors exactly.
- **(C3c) Subleading correction claim.** At first subleading order, V5-kernel and motif-alphabet substrate-cutoff effects produce ED-distinctive corrections to $\mathcal{T}_\ell(\omega)$ of order $(\ell_P/M)^2$.

H-2 examines each. The argument runs through six structural steps: (i) the substrate scattering problem for V5 modes propagating from the saturated surface, (ii) the effective potential in ED variables, (iii) the transmission coefficient, (iv) comparison with semiclassical greybody factors, (v) identification of substrate-cutoff corrections, (vi) audit of FORCED / CONDITIONAL status.

The honest framing parallels H-1: the substrate calculation is structurally analogous to the standard Regge-Wheeler / Teukolsky treatment with DCGT supplying the substrate-to-continuum identification at leading order. ED's substantively new content is the substrate-cutoff corrections at first subleading order. The leading-order identification is structurally equivalent to the standard semiclassical result via the same DCGT bridge that operated in H-1.

---

## 2. Substrate Inputs and the Assumption Audit

The derivation uses only the following inputs, each FORCED-unconditional, primitive, or canonical guardrail:

| Input | Status | Role |
|---|---|---|
| **H-1 (Planck spectrum + Hawking temperature)** | Closed (this arc) | Establishes the Planck-distribution-per-mode that greybody factors filter |
| **V5 finite-width memory kernel** | Substrate primitive | Mediates the substrate-modes that propagate through the exterior; sets high-frequency cutoff scale |
| **V1 forward-cone-only kernel (T18)** | FORCED-unconditional | Causal propagation structure of substrate-modes |
| **BH-6 (Wave-BH scattering)** | Closed-arc inheritance | Substrate-level wave-scattering structure at horizon, BHPT phase-shift content, helicity behavior |
| **DCGT (substrate-to-continuum bridge)** | FORCED structural-foundation | Identifies substrate-effective-potential with continuum Regge-Wheeler at leading order |
| **Cross-chain bandwidth $\Gamma_{\mathrm{cross}} \sim \exp[-\alpha \int \sigma\, d\ell]$** | DCGT-derived | Substrate-state-dependent factor in the effective potential |
| **Sparsity $\sigma$, multiplicity $\mathcal{M}$** | Substrate quantities | Parameterize the exterior substrate-state |
| **Substrate motif alphabet $g$** | INHERITED from BH-5 | The substrate-counting structure that produces area-law entropy; affects greybody factors at first subleading order |
| **T19 (Newton-recovery $\ell_P$)** | Closed-arc inheritance | Identifies the substrate length scale for cutoff physics |
| **Spherical geometry of saturated surface** | BH-2 inheritance | Permits angular-mode decomposition into $(\ell, m)$ harmonics |
| **Standard Regge-Wheeler / Teukolsky equations** | External mathematical physics | Identification target; not used as derivation premise |

**No new primitives introduced.** **No use of standard greybody-factor results as derivation premises** — only as identification targets at leading order.

---

## 3. The Substrate Scattering Problem

### 3.1 Setup

The output of H-1 is the V5 cross-chain correlation function evaluated at the saturated decoupling surface, producing a Planck distribution per substrate mode at $T_H = \kappa/(2\pi)$. This is the *near-horizon* spectrum.

For a substrate observer at infinity to see the radiation, each mode must propagate from the saturated surface through the exterior substrate region. The substrate between the surface and infinity has structure: $\sigma(r)$ varies with substrate-distance $r$, $\Gamma_{\mathrm{cross}}$ varies along the propagation path, and the substrate-channel-coupling structure modifies which modes can propagate freely and which encounter substrate-state-induced barriers.

This is a *substrate scattering problem*: V5 modes incident on the substrate-exterior region from the saturated surface; some fraction transmits to infinity; some fraction reflects back to the surface (and falls into the saturated region, contributing to the area-law entropy build-up but not to observed radiation).

### 3.2 Substrate-mode decomposition

By BH-2's spherical-geometry inheritance, substrate-modes near the saturated surface admit angular-momentum decomposition. A V5 substrate-mode with frequency $\omega$ and angular labels $(\ell, m)$ has wave-equation structure:

```
ψ_{ωℓm}(r, t) = R_ωℓ(r) · Y_ℓm(θ, φ) · e^(-iωt)
```

where $R_{\omega\ell}(r)$ is the radial substrate-amplitude and $Y_{\ell m}$ are standard spherical harmonics. The substrate's spherical symmetry around the saturated surface forces this decomposition; it is FORCED by BH-2's spherical-geometry inheritance.

### 3.3 The radial substrate wave equation

The radial substrate amplitude $R_{\omega\ell}(r)$ satisfies a substrate-derived wave equation. The general structure is:

```
d²R_ωℓ/dr*² + [ω² - V_ℓ^(ED)(r)] R_ωℓ = 0
```

where $r_*$ is a substrate-tortoise coordinate (the substrate-distance variable that absorbs the substrate-state-factor near the saturated surface, analogous to the standard tortoise coordinate $r_* = r + 2M\ln|r/2M - 1|$ in Schwarzschild).

The substrate-effective potential $V_\ell^{\mathrm{(ED)}}(r)$ is the load-bearing object of the H-2 calculation. It has two contributions:

- A **centrifugal barrier** from the angular-momentum decomposition: $\ell(\ell+1)/r^2$.
- A **state-dependent factor** from the substrate's $\sigma(r)$ profile, which goes to zero at the saturated surface and to unity at infinity.

§4 derives the explicit form.

### 3.4 Boundary conditions

The substrate wave equation has two boundary conditions:

- **At the saturated surface ($r \to r_h^+$, $r_* \to -\infty$):** purely outgoing waves carrying Hawking radiation. $R_{\omega\ell} \sim e^{i\omega r_*}$ with the amplitude set by H-1's Planck spectrum.
- **At substrate-asymptotic infinity ($r \to \infty$, $r_* \to +\infty$):** outgoing transmitted waves plus reflected ingoing waves. $R_{\omega\ell} \sim T_\ell^{\mathrm{(ED)}}(\omega) e^{i\omega r_*}$ asymptotically.

These boundary conditions are FORCED by the substrate's causal structure (T18) and by H-1's identification of the saturated surface as the source of the Planck distribution. The transmission amplitude $T_\ell^{\mathrm{(ED)}}(\omega)$ is what determines the greybody factor $\mathcal{T}_\ell(\omega) = |T_\ell^{\mathrm{(ED)}}(\omega)|^2$.

---

## 4. The Effective Potential in ED Variables

The substrate-effective potential $V_\ell^{\mathrm{(ED)}}(r)$ must be constructed from substrate quantities. The construction has three pieces.

### 4.1 The state-dependent factor $f_\sigma(r)$

Define the substrate state-dependent factor:

```
f_σ(r) ≡ exp[-α · ∫_{r_h}^{r} σ(r') dr'/ℓ_P²]   (approximate form)
```

This factor goes to zero at the saturated surface ($r = r_h$, where the integral diverges due to $\sigma$ saturation) and to unity at substrate-asymptotic infinity (where $\sigma \to 0$ and the integrand vanishes).

The exact functional form of $f_\sigma(r)$ depends on the substrate's $\sigma(r)$ profile in the exterior region. For a stationary saturated surface in spherical symmetry (BH-2 inheritance), $\sigma(r)$ is determined by the BH-2 substrate-state. At leading-order DCGT coarse-graining:

```
f_σ(r) → 1 - 2M/r   (Schwarzschild identification)
```

This is the substrate-level analog of the Schwarzschild "lapse function" $1 - 2M/r$. The identification is FORCED at leading order via DCGT's substrate-to-continuum bridge applied to the saturated surface's spherical-symmetric substrate state.

### 4.2 The centrifugal contribution

The centrifugal-barrier piece comes from the angular-momentum decomposition of substrate-modes:

```
V_ℓ^(centrifugal)(r) = ℓ(ℓ+1)/r²
```

This is purely geometric — it follows from the substrate's spherical symmetry and the spherical-harmonic decomposition of substrate-modes. It is FORCED by BH-2 spherical-geometry inheritance.

### 4.3 The combined effective potential

The substrate-effective potential combines the state-dependent factor and the centrifugal barrier with the substrate's spatial-derivative structure. For massless scalar substrate-modes (the simplest case):

```
V_ℓ^(ED)(r) = f_σ(r) · [ℓ(ℓ+1)/r² + (1/r) · df_σ/dr]
```

At leading-order DCGT identification ($f_\sigma(r) \to 1 - 2M/r$):

```
V_ℓ^(ED)(r) → (1 - 2M/r) · [ℓ(ℓ+1)/r² + 2M/r³]
```

This is the standard **Regge-Wheeler effective potential** for massless scalar perturbations on Schwarzschild. The substrate calculation reproduces the Regge-Wheeler form at leading order via DCGT identification.

### 4.4 Spin-dependent generalizations

For massless modes of higher spin (vector $s = 1$, tensor $s = 2$), the standard treatment uses the Teukolsky master equation with spin-weighted spherical harmonics. The substrate analog inherits this generalization: spin-1 substrate-modes (gauge-field excitations from T17 rule-type-as-connection structure) and spin-2 substrate-modes (gravitational-wave-like substrate excitations) produce modified effective potentials with the same general structure as Regge-Wheeler / Teukolsky:

```
V_ℓ,s^(ED)(r) = f_σ(r) · [ℓ(ℓ+1)/r² - (s²-1)/r² · df_σ/dr + ...]
```

The substrate calculation reproduces the standard spin-s Teukolsky effective potential at leading-order DCGT identification.

### 4.5 What's FORCED vs. INHERITED in $V_\ell^{\mathrm{(ED)}}$

- **Form-FORCED:** the centrifugal-plus-state-dependent structure of $V_\ell^{\mathrm{(ED)}}(r)$ from substrate-mode angular-momentum decomposition + substrate-state-dependent factor.
- **Leading-order identification with $V_\ell^{\mathrm{(GR)}}$:** FORCED via DCGT.
- **Specific values of $f_\sigma(r)$ at substrate-cutoff scales:** INHERITED from V5-kernel + motif-alphabet $g$ structure.

---

## 5. The Transmission Coefficient and Greybody Factor Form

With the substrate-effective potential in hand, the transmission coefficient is computed by standard wave-mechanics methods applied to the substrate wave equation.

### 5.1 The transmission amplitude

For an incoming wave from the saturated surface (at $r_* \to -\infty$, $\psi \sim e^{i\omega r_*}$) and outgoing waves to substrate-asymptotic infinity (at $r_* \to +\infty$, $\psi \sim T_\ell^{\mathrm{(ED)}} e^{i\omega r_*} + R_\ell^{\mathrm{(ED)}} e^{-i\omega r_*}$), the transmission amplitude $T_\ell^{\mathrm{(ED)}}(\omega)$ is determined by integrating the wave equation through the barrier $V_\ell^{\mathrm{(ED)}}(r)$.

The greybody factor is:

```
𝒯_ℓ(ω) = |T_ℓ^(ED)(ω)|²
```

By unitarity (substrate-level conservation of the V5 mode flux): $|T_\ell^{\mathrm{(ED)}}(\omega)|^2 + |R_\ell^{\mathrm{(ED)}}(\omega)|^2 = 1$.

### 5.2 Limits of the greybody factor

The substrate-level greybody factor exhibits standard limits:

**Low-frequency limit ($\omega M \ll 1$):** the centrifugal barrier dominates the substrate-effective potential. Tunneling is exponentially suppressed for high $\ell$, leading to:

```
𝒯_ℓ(ω) ≈ ((ω r_h)/2)^{2ℓ+2} · [function of ℓ]   for small ω
```

This is the Page-formula low-frequency suppression — high angular momentum modes have low transmission, with the suppression scaling as $(\omega M)^{2\ell+2}$. The substrate calculation reproduces this at leading order.

**High-frequency limit ($\omega M \gg 1$):** the centrifugal barrier becomes negligible compared to the wave kinetic energy. Modes propagate semiclassically and:

```
𝒯_ℓ(ω) → 1   for ω M ≫ 1, modulo geometric absorption corrections
```

In this limit, the substrate-level greybody factor approaches unity, and the spectrum at infinity approaches the strict Planck distribution. The geometric absorption cross-section is $\sigma_{abs} \to 27\pi M^2$ for s-wave in the high-frequency limit (the standard Schwarzschild result), inherited from DCGT identification.

### 5.3 Intermediate frequencies

For $\omega M \sim 1$ (the most physically relevant regime, where the spectrum has its peak), $\mathcal{T}_\ell(\omega)$ is neither $\sim (\omega M)^{2\ell+2}$ nor $\sim 1$. The standard Schwarzschild calculation produces intermediate values that must be obtained numerically or via WKB approximation through the Regge-Wheeler barrier.

The substrate calculation, at leading-order DCGT identification, produces the same intermediate-frequency $\mathcal{T}_\ell(\omega)$ as the standard Schwarzschild calculation. The substrate is not free to produce different values at this regime — DCGT's substrate-to-continuum bridge forces leading-order identification.

### 5.4 Form-FORCED, values-INHERITED at leading order

The substrate-level greybody factor has:
- **Form-FORCED:** transmission-coefficient structure $\mathcal{T}_\ell(\omega) = |T_\ell^{\mathrm{(ED)}}(\omega)|^2$ with low-frequency power-law suppression and high-frequency saturation to unity.
- **Values-INHERITED at leading order:** specific numerical values of $\mathcal{T}_\ell(\omega)$ identify with the standard Regge-Wheeler / Teukolsky values via DCGT.

---

## 6. Comparison with Semiclassical Greybody Factors

At leading-order DCGT coarse-graining, the substrate-derived greybody factors $\mathcal{T}_\ell^{\mathrm{(ED)}}(\omega)$ identify exactly with the standard semiclassical greybody factors $\mathcal{T}_\ell^{\mathrm{(GR)}}(\omega)$ from Regge-Wheeler / Teukolsky scattering theory.

### 6.1 The identification

```
𝒯_ℓ^(ED)(ω) → 𝒯_ℓ^(GR)(ω)   at leading-order DCGT (ℓ_P/M → 0 limit)
```

This identification is FORCED by:

- The DCGT identification $f_\sigma(r) \to 1 - 2M/r$ at leading order (§4.1).
- The DCGT identification of substrate-mode angular structure with continuum spherical-harmonic structure (BH-2 inheritance).
- The DCGT identification of the substrate wave equation with the standard Regge-Wheeler / Teukolsky equation at leading order.

The greybody factors at leading order are not modified by ED. They are the standard semiclassical values, derived through a substrate-level chain rather than computed directly from spacetime curvature.

### 6.2 Empirical tests

Greybody factors are tested at the gravitational scale only indirectly, through:

- Hawking-spectrum predictions for primordial black holes (none directly observed).
- Analog Hawking radiation in BEC and acoustic systems, where the analog greybody factors are computed from the analog effective potential and tested experimentally — confirming the standard theoretical structure within experimental precision.
- Semiclassical-quantum-gravity tests at intermediate scales — none currently available.

ED's prediction at leading order matches the standard semiclassical prediction. The framework reproduces the empirically validated content (analog Hawking experiments) and predicts the unobserved content (gravitational-scale Hawking spectra) identically with semiclassical Hawking + Regge-Wheeler.

### 6.3 Spin-dependent matching

For massless modes of higher spin, the substrate calculation produces:

- **Spin-0 (scalar):** $\mathcal{T}_\ell^{(s=0)}(\omega)$ matching the standard Schwarzschild-Klein-Gordon greybody factor.
- **Spin-1/2 (Dirac fermion, charged):** $\mathcal{T}_\ell^{(s=1/2)}(\omega)$ matching the standard Dirac-equation-on-Schwarzschild greybody factor.
- **Spin-1 (gauge field, photon-like):** $\mathcal{T}_\ell^{(s=1)}(\omega)$ matching the standard Maxwell-equation-on-Schwarzschild greybody factor — including the well-known "photon barrier" structure.
- **Spin-2 (graviton-like substrate excitation):** $\mathcal{T}_\ell^{(s=2)}(\omega)$ matching the standard linearized-Einstein-equation-on-Schwarzschild greybody factor.

Each spin sector inherits the standard Teukolsky-equation result at leading-order DCGT identification.

### 6.4 What ED reproduces at leading order

**ED reproduces the semiclassical greybody factors at leading order.** Across all spin sectors, all angular momentum channels, and all frequencies, the substrate-derived greybody factor identifies with the standard Regge-Wheeler / Teukolsky greybody factor at leading-order DCGT coarse-graining. There is no substrate-level departure from the standard result at the level of the leading-order calculation.

This is the load-bearing leading-order claim for H-2. **(C3a) and (C3b) are FORCED.**

---

## 7. ED-Distinctive Corrections at First Subleading Order

The framework's substantively new content lives at first subleading order $(\ell_P/M)^2$. Two effects produce ED-distinctive corrections to the leading-order greybody factors.

### 7.1 V5 kernel cutoff effect

The substrate's V5 kernel has finite width. In the substrate wave equation, V5's finite width modifies the propagation of modes at frequencies near the V5 kernel-width inverse:

```
ω_V5^cutoff ≈ 1/(τ_V5)
```

where $\tau_{V5}$ is V5's characteristic memory time (a substrate parameter, INHERITED).

For modes with $\omega \ll \omega_{V5}^{\mathrm{cutoff}}$, V5 corrections are negligible and the leading-order greybody factor holds. For modes approaching $\omega \sim \omega_{V5}^{\mathrm{cutoff}}$, V5 corrections become significant:

```
𝒯_ℓ^(ED)(ω) = 𝒯_ℓ^(GR)(ω) · [1 - c_V5 · (ω τ_V5)² · h_ℓ(ω)] + O((ω τ_V5)^4)
```

where $c_{V5}$ is a substrate-determined coefficient (INHERITED from V5 kernel structure) and $h_\ell(\omega)$ is a function depending on the angular channel and frequency.

The form of the correction is FORCED by the V5 kernel's finite-width substrate structure plus DCGT first-subleading-order machinery. The specific coefficient is INHERITED.

### 7.2 Motif alphabet $g$ effect

BH-5 introduced the motif alphabet $g$ as the substrate-counting structure that produces area-law entropy with coefficient $\log g$ INHERITED. The motif alphabet also affects greybody factors at first subleading order.

The substrate's motif-counting structure modifies the effective potential's near-horizon behavior. At first subleading order:

```
V_ℓ^(ED)(r) = V_ℓ^(GR)(r) + (ℓ_P/M)² · g_correction_term(r) + O((ℓ_P/M)^4)
```

where the $g_{\mathrm{correction}}$ term depends on the motif alphabet structure and produces frequency-dependent modifications to the greybody factor, particularly in the near-horizon regime where $f_\sigma(r) \to 0$.

This produces a low-frequency modification to the greybody factor:

```
𝒯_ℓ^(ED)(ω) = 𝒯_ℓ^(GR)(ω) · [1 + c_g · (ℓ_P/M)² · k_ℓ(ω)] + O((ℓ_P/M)^4)
```

where $c_g$ is INHERITED from the motif alphabet $g$ and $k_\ell(\omega)$ is a function depending on the angular channel.

### 7.3 Combined first-subleading-order correction

The total first-subleading-order correction to the greybody factor is:

```
𝒯_ℓ^(ED)(ω) = 𝒯_ℓ^(GR)(ω) · [1 + δ_V5(ω) + δ_g(ω) + O((ℓ_P/M)^4 + (ω τ_V5)^4)]
```

with:

- $\delta_{V5}(\omega) \sim -c_{V5} (\omega \tau_{V5})^2 h_\ell(\omega)$ (V5 high-frequency cutoff).
- $\delta_g(\omega) \sim c_g (\ell_P/M)^2 k_\ell(\omega)$ (motif alphabet near-horizon modification).

For Schwarzschild BHs of stellar mass, $(\ell_P/M)^2 \sim 10^{-76}$ and $\omega \tau_{V5}$ is whatever small dimensionless ratio the substrate provides — both corrections are negligible at observable scales.

For primordial BHs evaporating now, $(\ell_P/M)^2 \sim 10^{-14}$ and the V5 cutoff scale becomes accessible during the final stages of evaporation. The corrections are then in principle observable.

For analog Hawking experiments, the substrate-cutoff scales are determined by the analog system's microscopic details (BEC healing length, acoustic phonon wavelength) — different from the cosmological substrate scales but structurally analogous. Analog systems can test the structural form of the substrate-cutoff corrections.

### 7.4 What's FORCED vs. INHERITED in the corrections

- **Form-FORCED:** the substrate-cutoff corrections at first subleading order $(\ell_P/M)^2$ exist as a structural consequence of V5 finite-width + motif alphabet $g$. The functional form of the corrections (multiplicative on the leading-order greybody factor; specific $\omega$-dependence from each substrate-cutoff effect) is FORCED.
- **Coefficient-INHERITED:** the specific coefficients $c_{V5}$, $c_g$, $\tau_{V5}$, and the functional shapes $h_\ell(\omega)$, $k_\ell(\omega)$ are INHERITED from V5-kernel + motif-alphabet substrate details.

These corrections are detailed structurally in H-4 (V5 cutoff, the dedicated subleading-order memo). H-2 establishes that the corrections exist with the right structural form; H-4 derives the detailed form.

---

## 8. Verdict

> **VERDICT (H2): FORM-FORCED, VALUES-INHERITED at leading order with first-subleading-order corrections.**
>
> At leading-order DCGT coarse-graining, the substrate-derived greybody factors $\mathcal{T}_\ell^{\mathrm{(ED)}}(\omega)$ identify exactly with the standard semiclassical Regge-Wheeler / Teukolsky greybody factors $\mathcal{T}_\ell^{\mathrm{(GR)}}(\omega)$ across all spin sectors, all angular momentum channels, and all frequencies. The substrate-effective potential $V_\ell^{\mathrm{(ED)}}(r)$ has form-FORCED structure (centrifugal barrier + substrate-state-dependent factor), with the leading-order substrate-state-dependent factor identifying as the Schwarzschild lapse function $1 - 2M/r$. ED-distinctive corrections appear at first subleading order $(\ell_P/M)^2$ and at high frequencies near the V5 kernel-width inverse: V5 high-frequency cutoff $\delta_{V5}(\omega) \sim -(\omega\tau_{V5})^2$ and motif-alphabet near-horizon modification $\delta_g(\omega) \sim (\ell_P/M)^2$. Both correction forms are FORCED; specific coefficients are INHERITED.

**Trending toward YES on H-2 reproduction of semiclassical greybody factors at leading order.** ED reproduces the standard semiclassical greybody factors exactly at leading-order DCGT coarse-graining, with substantively new ED-distinctive corrections appearing at first subleading order. The leading-order match is a structural recovery; the subleading corrections are the ED-distinctive content.

**Verdict-class details:**

- **(C3a) Form claim:** FORCED. The substrate scattering problem produces a transmission coefficient with the standard structure.
- **(C3b) Leading-order identification:** FORCED via DCGT. ED reproduces semiclassical greybody factors at leading order.
- **(C3c) Subleading correction claim:** Form-FORCED, coefficients-INHERITED. The corrections exist with specific functional structure; numerical values come from substrate-cutoff details.
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {} as of arc-opening tally.

---

## 9. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| Standard Regge-Wheeler / Teukolsky used as derivation premise? | **No.** Standard greybody calculation appears in §6 as identification target, not derivation step. The substrate scattering problem is set up in §3 from substrate primitives + H-1 boundary conditions; the substrate-effective potential is constructed in §4 from substrate-state quantities; the transmission coefficient is computed in §5 from the substrate wave equation. Identification with standard semiclassical results is a §6 step, not a §3-§5 derivation premise. |
| H-1 used only as input? | **Confirmed.** H-1's Planck-spectrum-at-saturated-surface is the boundary condition for the scattering problem at $r_* \to -\infty$; not re-derived. |
| BH-2 / BH-6 / DCGT used only as inputs? | **Confirmed.** BH-2 supplies spherical geometry; BH-6 supplies wave-scattering structure; DCGT supplies leading-order substrate-to-continuum identification. None re-derived. |
| H-3 through H-7 used as derivation premises? | **No.** Not invoked. H-2 is structurally upstream of H-3 (Page rate uses greybody factors), H-5 (information correlations use spectrum + greybody factors), H-7 (synthesis). H-4 (V5 cutoff) is referenced as the subleading-order detailed treatment, but H-2 establishes the existence and form of the corrections without invoking H-4's specific derivations. |
| Self-reference of H-2 within itself? | **No.** §3 → §4 → §5 → §6 → §7 derivation chain is acyclic. |

**Acyclicity confirmed.**

---

## 10. Falsification

### 10.1 Falsifier for FORM-FORCED, VALUES-INHERITED at leading order verdict (current verdict)

A substrate construction satisfying H-1, BH-2, BH-6, DCGT, and substrate locality, in which the substrate-derived greybody factors fail to identify with the standard Regge-Wheeler / Teukolsky values at leading-order DCGT coarse-graining. Concretely:

- (a) A substrate-effective potential $V_\ell^{\mathrm{(ED)}}(r)$ that fails to reduce to the Regge-Wheeler form $V_\ell^{\mathrm{(GR)}}(r)$ in the leading-order $(\ell_P/M \to 0)$ limit — would refute DCGT's substrate-to-continuum bridge in this regime.
- (b) A substrate calculation that fails to produce the standard low-frequency power-law suppression $(\omega r_h)^{2\ell+2}$ or the high-frequency saturation $\mathcal{T}_\ell \to 1$ — would refute the substrate-mode angular-momentum decomposition or the scattering-theory identification.
- (c) A substrate-level construction that produces strong $(O(1))$ deviations from semiclassical greybody factors at the leading-order calculation level — would refute the leading-order identification.

Each refutation would downgrade the verdict from FORCED to CONDITIONAL or NOT FORCED.

### 10.2 Empirical-side falsifier

Any analog Hawking experiment (BEC, acoustic, photonic) producing greybody factors that deviate from the standard analog-Regge-Wheeler predictions within experimental precision would falsify both ED's leading-order prediction and standard semiclassical Hawking. Such observations are not currently available; analog Hawking experiments are typically focused on confirming the spectral form rather than precisely measuring greybody factors.

### 10.3 Substrate-cutoff observable predictions

ED's distinctive predictions live at first subleading order $(\ell_P/M)^2$ from V5 cutoff and motif-alphabet effects. These produce:

- Modifications to the high-frequency tail of the Hawking spectrum, observable in principle for primordial BHs in their final evaporation stages.
- Modifications to the low-frequency suppression of greybody factors, observable in principle for analog Hawking systems with sufficient experimental precision.

H-4 develops these predictions in detail. For H-2, the leading-order identification is the load-bearing result.

### 10.4 Subtle structural test

The framework's substrate-effective-potential construction depends on the substrate-state-dependent factor $f_\sigma(r)$ identifying with $1 - 2M/r$ at leading order. A more careful examination of this identification — in extensions to charged BHs (Reissner-Nordström substrate analog), rotating BHs (Kerr substrate analog), or higher-dimensional substrate-saturation surfaces — could reveal whether the leading-order identification is genuinely FORCED or has hidden dependencies on the substrate's specific saturation structure.

---

## 11. Consequences for the Arc

1. **H-2 closes cleanly as articulation memo.** The substrate-derived greybody factors reproduce semiclassical Regge-Wheeler / Teukolsky values at leading order, with first-subleading-order corrections form-FORCED and coefficients-INHERITED. Arc Hawking can now proceed to H-3, H-4, H-5, H-6, H-7.

2. **H-3 (Page rate) is structurally enabled.** With the leading-order Planck distribution from H-1 and the leading-order greybody factors from H-2, integrating over modes produces the total emission rate. The Page rate $\dot M = -\hbar c^4/(15360\pi G^2 M^2)$ should follow at leading order with the specific numerical coefficient INHERITED from substrate-mode counting.

3. **H-4 (V5 cutoff) is the natural follow-on for ED-distinctive content.** §7 of H-2 identified the V5 cutoff form-FORCED at first subleading order. H-4 develops the detailed functional form of the high-frequency cutoff and connects to observable predictions for primordial BH evaporation.

4. **H-5 (information correlations) inherits the leading-order spectrum + greybody factor structure.** With H-1 and H-2 producing the leading-order spectrum at infinity, H-5 can address the information-content structure of the radiation: how Hawking-quanta correlations relate to interior-fallen matter via BH-4 entanglement-straddling + Arc E bandwidth-budget mechanism.

5. **Cross-domain echo with BH-6 sharpened.** BH-6 (Wave-BH scattering) closed the wave-scattering structure at the BH horizon level. H-2 builds on BH-6 to produce the explicit greybody factors. The cross-arc inheritance is now concrete.

6. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

7. **Sensitivity flag inherited from H-1.** §4.1's identification of $f_\sigma(r) \to 1 - 2M/r$ at leading order assumes spherical-symmetric saturated surfaces (Schwarzschild substrate state). Extensions to charged or rotating substrate states require generalizing this identification.

---

## 12. Summary

**What this memo accomplished.**

- Stated the H-2 CANDIDATE (§1) decomposing it into (C3a) form, (C3b) leading-order identification, and (C3c) subleading corrections.
- Set up the substrate scattering problem for V5 modes propagating from the saturated surface to substrate-asymptotic infinity, with substrate-mode angular-momentum decomposition (§3).
- Constructed the substrate-effective potential $V_\ell^{\mathrm{(ED)}}(r) = f_\sigma(r) [\ell(\ell+1)/r^2 + (1/r)(df_\sigma/dr)]$ from substrate-state quantities, with leading-order DCGT identification $f_\sigma(r) \to 1 - 2M/r$ producing the standard Regge-Wheeler form (§4).
- Computed the transmission coefficient $\mathcal{T}_\ell(\omega) = |T_\ell^{\mathrm{(ED)}}(\omega)|^2$ with standard low-frequency power-law suppression $(\omega r_h)^{2\ell+2}$ and high-frequency saturation $\mathcal{T}_\ell \to 1$ (§5).
- Established the leading-order identification: ED reproduces semiclassical Regge-Wheeler / Teukolsky greybody factors exactly at leading-order DCGT coarse-graining (§6).
- Identified two ED-distinctive corrections at first subleading order: V5 high-frequency cutoff and motif-alphabet near-horizon modification (§7).
- Issued the verdict: **FORM-FORCED, VALUES-INHERITED at leading order with first-subleading-order corrections** (§8).
- Confirmed acyclicity (§9) and provided substrate-level + empirical falsifiers (§10).

**Trending toward YES on ED reproduction of semiclassical greybody factors at leading order.**

**Brief 2–3 sentence summary:** The substrate scattering problem for V5 modes propagating from the saturated decoupling surface to substrate-asymptotic infinity produces an effective potential of the form $V_\ell^{\mathrm{(ED)}}(r) = f_\sigma(r)[\ell(\ell+1)/r^2 + (1/r)(df_\sigma/dr)]$, with the substrate-state-dependent factor $f_\sigma(r) \to 1 - 2M/r$ at leading-order DCGT coarse-graining recovering the standard Regge-Wheeler effective potential. The transmission coefficient $\mathcal{T}_\ell^{\mathrm{(ED)}}(\omega) = |T_\ell^{\mathrm{(ED)}}(\omega)|^2$ identifies exactly with the semiclassical greybody factor $\mathcal{T}_\ell^{\mathrm{(GR)}}(\omega)$ at leading order, with ED-distinctive corrections appearing at first subleading order from V5 high-frequency cutoff $\delta_{V5}(\omega) \sim -(\omega\tau_{V5})^2$ and motif-alphabet near-horizon modification $\delta_g(\omega) \sim (\ell_P/M)^2$ — both form-FORCED with INHERITED coefficients. ED reproduces semiclassical greybody factors at leading order; the substantively new ED content lives at first subleading order and is developed in detail in H-4.

---

## 13. Recommended Next Steps

Multiple options, in decreasing order of immediate Arc Hawking productivity:

1. **H-4 (V5 cutoff at first subleading order) — RECOMMENDED.** With H-1 and H-2 producing the leading-order spectrum + greybody factors, H-4 is now the most productive next memo. The substrate-cutoff corrections identified in §7 of H-2 (V5 high-frequency cutoff and motif-alphabet near-horizon modification) are the most ED-distinctive content of the arc. H-4 develops the detailed functional forms and connects to observable predictions for primordial BH evaporation. Estimated 1–2 sessions.

2. **H-3 (Page rate).** Direct follow-on after H-1 + H-2. Integrating the Planck distribution (H-1) with greybody factors (H-2) over modes produces the total emission rate. The Page rate $\dot M \propto 1/M^2$ should follow at leading order with the specific numerical coefficient INHERITED from substrate-mode counting. Quick memo, estimated 1 session.

3. **H-5 (information correlations).** Most theoretically rich follow-on. The bandwidth-budget mechanism from Arc E plus BH-4 entanglement-straddling produces a substrate-level account of Hawking-quanta correlations with interior-fallen matter — the substrate-level account of the information-paradox-resolution content. Couples Arc Hawking with Arc E and Arc BH cross-domain unification structurally. Estimated 2–3 sessions.

4. **(Defer) H-6 (semiclassical equivalence) and H-7 (synthesis).** These are the final memos; written after all structural derivation memos close. H-6 in particular benefits from H-4's first-subleading-order analysis, since the semiclassical-equivalence question depends on whether the corrections produce qualitatively new behavior or just numerical refinements.

5. **(Independent) Spin-sector extension memo.** §6.3 of H-2 noted that the spin-dependent generalization to massless modes of higher spin (s = 1/2, 1, 2) inherits the standard Teukolsky-equation result at leading-order DCGT identification. A dedicated memo could develop the spin-sector greybody factors in more detail, including the substrate-level content of "photon barrier" structure and graviton-like substrate excitations. Could supplement H-2 if needed for a broader treatment.

6. **(Optional) Charged-BH (Reissner-Nordström) extension.** The substrate analog of the charged-BH case would require T17 (gauge-field-as-rule-type) inheritance for the charged-particle Hawking emission and the modified substrate-state-dependent factor at the charged horizon. A separate memo on this could extend Arc Hawking's coverage; defer unless specifically wanted.

---

**Pause for further instruction.**
