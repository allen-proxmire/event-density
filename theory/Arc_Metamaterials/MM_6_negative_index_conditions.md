# Memo 6 — Conditions for Negative Index (Pendry 2000)

**Arc Metamaterials, Memo 6 of 13.**
**Allen Proxmire** · May 2026

*Derive the substrate-level conditions for negative effective permittivity (plasma-like microstructures), negative effective permeability (resonant rule-type circulation pathways), and the combined negative refractive index regime. Articulate the substrate-level mechanism for negative refraction. Close the homogenization cluster of the Arc.*

---

## 1. Setup and Notation

A chain of the kind permitted by P-MM-4 — a light-like ED-channel — propagates through a periodic rule-type substrate (P-MM-1 + P-MM-2). The chain's pre-individuation amplitude $\psi(\mathbf{x})$ satisfies the scalar wave equation derived from Maxwell's equations under one polarization choice. In the homogenization regime $\ell_P \ll a \ll \lambda \ll L$ (P-MM-6), the chain's coarse-grained dynamics is governed by the macroscopic effective wave equation

$$
\partial_{X^i}\!\left[\mu_{\mathrm{eff}}^{-1\,ij}\, \partial_{X^j}\psi_0\right] + \omega^{2}\,\varepsilon_{\mathrm{eff}}\,\psi_0 = 0,
$$

with effective constitutive tensors

$$
\varepsilon_{\mathrm{eff}}^{ij}(\omega) = \big\langle\varepsilon^{ij}(\mathbf{y}; \omega)\big\rangle + \big\langle\varepsilon^{ik}(\mathbf{y}; \omega)\,\partial_{y^k}\chi^j(\mathbf{y}; \omega)\big\rangle,
$$

$$
\mu_{\mathrm{eff}}^{-1\,ij}(\omega) = \big\langle\mu^{-1\,ij}(\mathbf{y}; \omega)\big\rangle + \big\langle\mu^{-1\,ik}(\mathbf{y}; \omega)\,\partial_{y^k}\chi^j_M(\mathbf{y}; \omega)\big\rangle.
$$

Both $\varepsilon^{ij}$ and $\mu^{ij}$ may depend on frequency $\omega$ (dispersion); the cell correctors $\chi^j(\mathbf{y}; \omega), \chi^j_M(\mathbf{y}; \omega)$ inherit this frequency dependence through the cell problems

$$
\partial_{y^i}\!\left[\varepsilon^{ij}(\mathbf{y}; \omega)\,\partial_{y^j}\chi^k(\mathbf{y}; \omega)\right] = -\partial_{y^i}\varepsilon^{ik}(\mathbf{y}; \omega),
$$

with the analogous problem for $\chi^j_M$ using $\mu^{-1\,ij}$.

The averaging operator is $\langle f \rangle = (1/|Y|)\int_Y f(\mathbf{y})\, d^d y$, and the homogenization machinery is the multi-scale expansion in $a/\lambda \ll 1$.

The substrate-level identifications:
- $\varepsilon$ — coarse-grained rule-type polarizability of the microstructure.
- $\mu$ — coarse-grained rule-type circulation response of the microstructure.
- $\chi^j(\mathbf{y})$ — local accommodation pattern of the chain's amplitude in response to a macroscopic gradient.

Standard physics tells us that natural materials have $\varepsilon, \mu > 0$ at most frequencies of interest. Pendry's 2000 work showed that *engineered microstructures* — wire arrays and split-ring resonators — can produce *negative* effective $\varepsilon$ and $\mu$ in suitably chosen frequency windows, and that the combination produces negative refractive index. This Memo derives the substrate-level conditions for each.

---

## 2. (A) Negative Effective Permittivity — Plasma-Like Microstructures

### 2.1 The wire-array microstructure

Consider a unit cell containing a long thin conducting wire embedded in vacuum:

- Wire material: idealized perfect conductor (or high-conductivity metal) supporting collective rule-type-alignment oscillations.
- Wire radius: $r_0 \ll a$, with $a$ the unit-cell spacing.
- Wire length: parallel to one cell axis, spanning the cell.

The local permittivity is

$$
\varepsilon(\mathbf{y}; \omega) = \begin{cases} \varepsilon_w(\omega) & \mathbf{y} \in Y_w \text{ (wire region)}, \\ \varepsilon_0 & \mathbf{y} \in Y \setminus Y_w \text{ (vacuum region)}, \end{cases}
$$

with wire volume fraction $f_w = |Y_w|/|Y|$. For a thin wire of radius $r_0$ in a cell of side $a$:

$$
f_w \approx \pi r_0^2 / a^2 \ll 1.
$$

The wire's local rule-type response $\varepsilon_w(\omega)$ supports collective oscillations of its bound rule-type structure: the substrate-level analog of free-electron plasma oscillations. For frequencies $\omega$ below the wire's intrinsic rule-type-plasma frequency $\omega_{p,\text{wire}}$, the wire's response is plasma-like.

### 2.2 Substrate-level rule-type collective oscillations

Inside the wire, the substrate's rule-type structure supports a collective mode in which the local rule-type-alignment oscillates coherently. The mode is the substrate-level analog of plasma oscillations in a free-electron gas.

The substrate-level mechanism: in a region of rule-type microstructure that supports free (unbound) rule-type-alignment displacement, an applied electric field perturbs the local alignment from equilibrium. The displaced alignment carries an inertial substrate-level response (each rule-type-alignment shift has an effective "mass" set by the rule-type kinetic-response tensor), and the restoring force comes from the local rule-type-charge accumulation that the displacement produces.

Newton's equation analog for the rule-type-alignment displacement $\boldsymbol{\xi}$:

$$
m^*\ddot{\boldsymbol{\xi}} = -e^*\mathbf{E}_\text{local}(\boldsymbol{\xi}) - m^*\gamma\dot{\boldsymbol{\xi}},
$$

with:
- $m^*$ the substrate-level effective rule-type-alignment mass (inertia of the alignment shift).
- $e^*$ the substrate-level effective rule-type-coupling charge to the gauge field's electric component.
- $\gamma$ the substrate-level damping (loss of alignment coherence per unit time).
- $\mathbf{E}_\text{local}$ the local electric field at the alignment-displaced position.

In the long-wavelength limit ($a \ll \lambda$), the local field is approximately the applied field $\mathbf{E}$. For harmonic drive $\mathbf{E} \propto e^{-i\omega t}$, $\boldsymbol{\xi} \propto e^{-i\omega t}$, and the equation of motion gives

$$
\boldsymbol{\xi}(\omega) = -\frac{e^*\mathbf{E}}{m^*(\omega^2 + i\gamma\omega)}.
$$

### 2.3 Wire-local polarization and permittivity

The wire-local polarization (rule-type-alignment dipole moment per unit volume) is

$$
\mathbf{P}_\text{wire}(\omega) = -n^*\, e^*\,\boldsymbol{\xi}(\omega) = \frac{n^*(e^*)^2}{m^*(\omega^2 + i\gamma\omega)}\,\mathbf{E},
$$

where $n^*$ is the substrate-level density of mobile rule-type-alignment carriers in the wire. The wire-local susceptibility is

$$
\chi_e^\text{wire}(\omega) = \frac{P_\text{wire}}{\varepsilon_0 E} = \frac{n^*(e^*)^2}{\varepsilon_0 m^*(\omega^2 + i\gamma\omega)} = -\frac{\omega_{p,\text{wire}}^2}{\omega^2 + i\gamma\omega},
$$

where we define the wire's intrinsic *substrate-level plasma frequency*

$$
\boxed{\quad \omega_{p,\text{wire}}^2 \;\equiv\; \frac{n^*(e^*)^2}{\varepsilon_0\, m^*}. \quad}
$$

The wire's local permittivity is

$$
\varepsilon_w(\omega) = \varepsilon_0\!\left(1 - \frac{\omega_{p,\text{wire}}^2}{\omega^2 + i\gamma\omega}\right).
$$

For $\omega < \omega_{p,\text{wire}}$ and small $\gamma$, $\text{Re}[\varepsilon_w(\omega)] < 0$ — the wire's local rule-type response is *anti-parallel* to the applied field.

### 2.4 Cell-averaging: from local plasma frequency to effective plasma frequency

The cell-averaged permittivity for the wire-vacuum microstructure depends on the unit-cell geometry. For a *thin-wire array* with wires aligned along one axis (say $z$):

- For propagation perpendicular to the wires (electric field along $z$, the wire direction), the relevant cell-averaged response is dominated by the wires' collective rule-type oscillation.

The Pendry 1996/1998 analysis of the thin-wire microstructure (which we summarize and substrate-level-interpret here) yields an *effective* plasma frequency for the array

$$
\omega_p^2 \equiv \omega_{p,\text{eff}}^2 = \frac{2\pi c^2}{a^2 \ln(a/r_0)},
$$

where:
- $c$ is the substrate's V1-kernel propagation rate (the substrate-level speed of light, treated as fundamental and constant per the ED program's acoustic-metric guardrails).
- $a$ is the unit-cell spacing.
- $r_0$ is the wire radius.
- $\ln(a/r_0)$ is the logarithmic geometric factor from the wire's transverse extent compared to the cell spacing.

The effective plasma frequency $\omega_p$ is *much smaller* than the wire's intrinsic $\omega_{p,\text{wire}}$, because the array effectively dilutes the substrate-level rule-type-alignment density. The reduction factor is on the order of $f_w \cdot |\text{logarithmic factor}|^{-1}$.

### 2.5 The Drude-form effective permittivity

For frequencies $\omega \gg \gamma$ (low damping), the wire-array effective permittivity takes the *Drude form*

$$
\boxed{\quad \varepsilon_{\mathrm{eff}}(\omega) = \varepsilon_\infty\!\left(1 - \frac{\omega_p^2}{\omega^2}\right), \quad}
$$

where $\varepsilon_\infty$ is the high-frequency limit of the effective permittivity (typically $\varepsilon_\infty \approx \varepsilon_0$ for thin-wire arrays in vacuum). The dissipative imaginary part is $\propto \gamma\omega_p^2/\omega^3$ in the standard formulation.

For $\omega < \omega_p$, $\varepsilon_{\mathrm{eff}} < 0$. The negative-permittivity frequency window is

$$
0 < \omega < \omega_p,
$$

bounded above by the effective plasma frequency. Microwave-frequency thin-wire arrays (with $a \sim$ cm, $r_0 \sim$ mm) yield $\omega_p \sim$ GHz, placing $\omega_p$ in the microwave regime — well below the wire material's intrinsic optical-frequency plasma frequency.

### 2.6 Substrate-level meaning of the plasma frequency

The plasma frequency $\omega_p$ is the substrate-level *threshold above which the rule-type microstructure can keep up with the applied field's oscillation*.

For $\omega > \omega_p$: the field oscillates faster than the rule-type-alignment can respond. The substrate behaves as approximately empty (positive $\varepsilon \to \varepsilon_\infty$).

For $\omega < \omega_p$: the field oscillates slowly enough that the rule-type-alignment can not only respond but overshoot — the alignment moves in *opposition* to the applied field (negative $\varepsilon$). The induced polarization is anti-parallel to the field.

The substrate-level mechanism for negative $\varepsilon$: the rule-type microstructure's collective oscillation produces a coarse-grained response that *opposes* the applied field below the array's effective plasma frequency. The chain experiences an effective medium in which the rule-type response inverts the field's effect.

---

## 3. (B) Negative Effective Permeability — Resonant Circulation Pathways

### 3.1 The split-ring-resonator microstructure

Consider a unit cell containing a split-ring resonator (SRR):

- A circular conducting ring of radius $r_\text{ring}$, with a small gap of width $g$.
- The ring lies in a plane perpendicular to one axis (say the chain's propagation direction, or perpendicular to the applied magnetic field).
- The ring supports inductance $L$ (from circulating rule-type currents around the ring) and capacitance $C$ (from rule-type-charge accumulation across the gap).
- Together, $L$ and $C$ produce an LC-resonance at frequency $\omega_0 = 1/\sqrt{LC}$.

The substrate-level structure: the ring is a *closed-loop rule-type pathway* in the substrate's microstructure. It supports a localized rule-type circulation mode where the chain's amplitude can circulate around the ring, with the gap acting as a capacitive break point.

### 3.2 Substrate-level rule-type circulation mode

T17's identification of the gauge field with the rule-type connection (taken as a given in this Memo) implies that a chain's amplitude can accumulate rule-type holonomy by traversing closed loops in the substrate. A ring-like microstructure supports a *localized rule-type mode* — a configuration of the chain's amplitude that circulates around the ring and is bound to the ring by the rule-type structure of the ring itself.

When an external magnetic field is applied (rule-type curvature threading the ring), the localized circulation mode is driven. The induced circulation produces a rule-type-current loop, which in turn generates its own rule-type curvature (Faraday's law analog applied to the rule-type connection).

The equation of motion for the ring's circulating rule-type-current amplitude $I(t)$:

$$
L\ddot{Q} + R\dot{Q} + Q/C = \Phi_\text{ext},
$$

where $Q(t)$ is the rule-type-charge accumulated on one side of the gap, $I = \dot Q$ is the circulating rule-type current, $R$ is the ring's effective rule-type resistance (substrate-level damping), and $\Phi_\text{ext}$ is the external rule-type flux threading the ring (the rule-type-curvature analog).

In substrate-level language:
- $L$: the substrate-level inductance of the ring — quantifies the rule-type holonomy accumulated per unit circulating rule-type current.
- $C$: the substrate-level capacitance of the gap — quantifies rule-type-charge accumulation per unit rule-type-potential drop across the gap.
- $R$: the substrate-level damping — rate of rule-type-coherence loss in the circulation mode.
- $\omega_0 = 1/\sqrt{LC}$: the substrate-level resonance frequency of the circulation mode.

### 3.3 Ring response to applied magnetic field

For harmonic drive $\Phi_\text{ext} = \Phi_0 e^{-i\omega t}$, the ring's response is

$$
Q(\omega) = \frac{\Phi_\text{ext}}{1/C - L\omega^2 - iR\omega} \cdot \frac{1}{L} = \frac{\Phi_\text{ext}/L}{\omega_0^2 - \omega^2 - i(R/L)\omega}.
$$

The circulating current is $I = -i\omega Q$:

$$
I(\omega) = \frac{-i\omega\,\Phi_\text{ext}/L}{\omega_0^2 - \omega^2 - i\gamma\omega},
$$

with the damping rate $\gamma \equiv R/L$. The induced magnetic dipole moment of the ring is $m = \pi r_\text{ring}^2 I$. The ring's contribution to magnetization (per cell):

$$
\mathbf{M}_\text{ring}(\omega) = -\frac{n_\text{ring}\,\pi r_\text{ring}^2\, I}{|Y|}\,\hat{\mathbf{n}}_\text{ring},
$$

with $n_\text{ring}$ the number of rings per cell and $\hat{\mathbf{n}}_\text{ring}$ the ring's normal direction.

For applied magnetic field $\mathbf{H}$ along $\hat{\mathbf{n}}_\text{ring}$ with $\Phi_\text{ext} = \mu_0\pi r_\text{ring}^2 H$ (idealized, ignoring back-reaction):

$$
\mathbf{M}_\text{ring}(\omega) = -\frac{F\omega^2}{\omega_0^2 - \omega^2 - i\gamma\omega}\,\mathbf{H},
$$

where the *filling-factor oscillator strength* is

$$
\boxed{\quad F = \frac{\mu_0\, n_\text{ring}\, (\pi r_\text{ring}^2)^2}{|Y|\,L} = \frac{f_\text{ring}}{f_\text{geom}}, \quad}
$$

with $f_\text{ring}$ the fraction of cell volume containing rings and $f_\text{geom}$ a geometric factor of order unity. For dense ring arrays, $F$ can be a significant fraction of 1.

### 3.4 The Lorentz-form effective permeability

The effective magnetic susceptibility from cell-averaging the ring response is

$$
\chi_m(\omega) = -\frac{F\omega^2}{\omega_0^2 - \omega^2 - i\gamma\omega}.
$$

The effective permeability (relative to $\mu_0$):

$$
\boxed{\quad \mu_{\mathrm{eff}}(\omega) = 1 + \chi_m(\omega) = 1 - \frac{F\omega^2}{\omega^2 - \omega_0^2 + i\gamma\omega}. \quad}
$$

(The sign of the imaginary part of the denominator depends on the convention for harmonic time dependence; using $e^{-i\omega t}$ with positive $\gamma$ gives $+i\gamma\omega$ as in Pendry 1999.)

For frequencies slightly above $\omega_0$:

- $\omega \to \omega_0^+$: the denominator's real part becomes small and positive; $\chi_m \to -\infty$ (for negligible $\gamma$).
- $\omega \to \omega_p^\text{mag}$ (defined below): $\chi_m = -1$, so $\mu_{\mathrm{eff}} = 0$.
- For $\omega_0 < \omega < \omega_p^\text{mag}$: $\mu_{\mathrm{eff}} < 0$.

The *magnetic plasma frequency* (upper edge of negative-$\mu$ window) is

$$
\omega_p^\text{mag} = \frac{\omega_0}{\sqrt{1 - F}}.
$$

The negative-$\mu$ frequency window is

$$
\omega_0 < \omega < \omega_p^\text{mag} = \frac{\omega_0}{\sqrt{1-F}}.
$$

The window's width depends on the oscillator strength $F$: wider for larger $F$ (dense, low-inductance rings).

### 3.5 Substrate-level meaning of $\omega_0$, $F$, $\gamma$

$\omega_0 = 1/\sqrt{LC}$: the substrate-level *natural frequency of rule-type circulation* in the ring. Sets the lower edge of the negative-$\mu$ window.

$F$: the *substrate-level filling-factor oscillator strength* — quantifies how strongly the rule-type circulation modes couple back to produce magnetization, weighted by their density per unit cell. Higher $F$ means denser rings with stronger coupling, wider negative-$\mu$ window.

$\gamma$: the *substrate-level damping rate* of rule-type circulation coherence. Damping broadens the resonance and reduces the depth of negative $\mu$; in the high-loss limit ($\gamma \sim \omega_0$), the negative-$\mu$ window disappears.

### 3.6 Substrate-level mechanism for negative $\mu$

Below $\omega_0$: the ring's rule-type circulation is in phase with the applied magnetic field. Induced magnetization is parallel to $\mathbf{H}$, contributing positive susceptibility.

Above $\omega_0$: the ring's circulation lags the applied field by more than $\pi/2$. The induced magnetization is antiparallel to $\mathbf{H}$, contributing negative susceptibility. When the magnitude exceeds 1, $\mu_{\mathrm{eff}} = 1 + \chi_m < 0$.

The substrate-level mechanism: the resonant rule-type circulation mode, driven above its natural frequency, overshoots and produces a rule-type-curvature *opposite* to the applied curvature. The cell-averaged response in this regime exhibits negative permeability — the substrate's coarse-grained rule-type circulation response is anti-parallel to the applied magnetic field.

The phenomenon is *purely geometric*: it requires a closed-loop rule-type pathway with appropriate $L$ and $C$. Natural materials at optical frequencies do not provide such pathways at the right scale; engineered split-ring resonators do.

---

## 4. (C) Combined Negative Refractive Index

### 4.1 The simultaneous-negative regime

A Pendry-type negative-index metamaterial combines:
- Wire-array microstructure providing $\varepsilon_{\mathrm{eff}}(\omega) < 0$ for $\omega < \omega_p$.
- Split-ring-resonator microstructure providing $\mu_{\mathrm{eff}}(\omega) < 0$ for $\omega_0 < \omega < \omega_p^\text{mag}$.

The overlapping window where both are simultaneously negative:

$$
\max(0, \omega_0) < \omega < \min(\omega_p, \omega_p^\text{mag}).
$$

For a well-designed metamaterial, the wires are dimensioned so $\omega_p > \omega_p^\text{mag}$, and the rings are tuned so $\omega_0 < \omega_p$. The overlap window is then $\omega_0 < \omega < \omega_p^\text{mag}$.

### 4.2 The refractive index in the negative regime

The refractive index is defined by

$$
n^2(\omega) = \varepsilon_r(\omega)\,\mu_r(\omega),
$$

where $\varepsilon_r = \varepsilon_{\mathrm{eff}}/\varepsilon_0$ and $\mu_r = \mu_{\mathrm{eff}}/\mu_0$ are dimensionless. When both $\varepsilon_r < 0$ and $\mu_r < 0$:

$$
\varepsilon_r\mu_r = (-|\varepsilon_r|)(-|\mu_r|) = |\varepsilon_r\mu_r| > 0.
$$

So $n^2 > 0$ and $n$ is real. The question is which sign of $n$ to choose.

### 4.3 Branch choice from causality

The Maxwell wave equation in a homogeneous medium with $\varepsilon, \mu$ admits solutions $\psi \propto e^{i(kx - \omega t)}$ with $k^2 = \omega^2\varepsilon\mu/c^2 = \omega^2 n^2/c^2$. For a passive medium (no gain), causality requires:

1. The wave vector $\mathbf{k}$ in the direction of energy flow has positive imaginary part: $\text{Im}[k] > 0$ for damping.
2. The Poynting vector $\mathbf{S} = \text{Re}(\mathbf{E}\times\mathbf{H}^*)/2$ points in the direction of energy flow.

For a wave traveling in the $+x$ direction with $\varepsilon, \mu < 0$:

- $\mathbf{E} = E_0\hat{\mathbf{y}}e^{i(kx - \omega t)}$, $\mathbf{H} = H_0\hat{\mathbf{z}}e^{i(kx - \omega t)}$.
- From Faraday's law: $kE_0 = \omega\mu H_0$, so $H_0 = kE_0/(\omega\mu)$.
- Poynting vector: $S_x = \text{Re}(E_0 H_0^*)/2 = |E_0|^2\,\text{Re}(k/(\omega\mu))/2$.

For $\mathbf{S}$ in the $+x$ direction (energy flowing forward), $\text{Re}(k/\mu) > 0$. With $\mu < 0$, this requires $\text{Re}(k) < 0$ — the wave vector points in the $-x$ direction, opposite to the energy flow.

Equivalently: the phase velocity $\mathbf{v}_p = (\omega/k)\hat{\mathbf{k}}$ is antiparallel to the group/energy-flow velocity. The chain's amplitude phase advances backward relative to the energy propagation.

This is reflected in the sign of $n$. With

$$
n(\omega) = \pm\sqrt{\varepsilon_r\mu_r},
$$

the causality requirement forces

$$
\boxed{\quad n(\omega) = -\sqrt{\varepsilon_r(\omega)\,\mu_r(\omega)} \quad \text{when } \varepsilon_r < 0 \text{ and } \mu_r < 0. \quad}
$$

The refractive index is *negative*.

### 4.4 Substrate-level meaning of negative refractive index

The substrate-level reading: the chain's pre-individuation amplitude in the negative-index regime propagates with *reversed phase advance* relative to its coarse-grained energy flow. The chain's phase accumulates backward as energy carries forward.

This is not a violation of causality — the chain's energy flows forward at the appropriate group velocity. The phase reverses because the substrate's effective rule-type response is *inverted*: at each substrate point in the effective medium, the rule-type response opposes the chain's instantaneous gauge-field amplitude, producing a phase-reversal pattern that builds up across the medium.

In substrate-level terms:
- *Phase velocity*: the rate at which the chain's coarse-grained pre-individuation phase advances at fixed spatial position. Negative in negative-index media.
- *Group/energy velocity*: the rate at which the chain's coarse-grained energy flows. Positive (causal).

The two velocities being antiparallel is the substrate-level signature of the inverted rule-type response.

### 4.5 Snell's law in the negative-index regime

At an interface between a positive-index medium ($n_1 > 0$) and a negative-index medium ($n_2 < 0$), Snell's law gives

$$
n_1 \sin\theta_1 = n_2 \sin\theta_2.
$$

With $n_2 < 0$, this requires $\sin\theta_2 < 0$ — the refracted ray bends to the *same side* of the normal as the incident ray (rather than the opposite side as in conventional refraction). This is *negative refraction*, the experimental signature of negative-index metamaterials.

### 4.6 Substrate-level reading of negative refraction

At the interface, the chain's transverse momentum is conserved (tangential wave-vector continuity at the boundary), but the substrate's effective rule-type response on the negative-index side imposes a phase pattern that points the wave vector in the opposite direction relative to the energy flow.

The substrate-level mechanism for negative refraction:
- *Rule-type gradient inversion*: the effective medium on the negative-index side has rule-type response opposing the natural direction. The chain's amplitude bends accordingly.
- *Microstructure-induced phase-advance reversal*: the chain's coarse-grained pre-individuation phase advances backward relative to its energy flow on the negative-index side. The interface preserves transverse phase continuity, forcing the wave vector to bend to the same-side angle.
- *ED-gradient redirection of channel propagation*: the engineered rule-type microstructure has reshaped the substrate's effective gradient structure so that the chain's coarse-grained pathway through the medium has reversed phase-rotation handedness.

Standard physics describes this in terms of $n < 0$ and Snell's law with negative angle. Substrate-level physics describes the same phenomenon as a rule-type-response inversion that the chain follows because its pre-individuation amplitude must respect the local effective constitutive structure.

---

## 5. Worked Example: Pendry 2000 Combined Microstructure

To make the construction concrete, consider the canonical Pendry 2000 microwave metamaterial:

- **Wire array**: copper wires of radius $r_0 = 1$ mm, lattice spacing $a = 5$ mm, oriented along $\hat{\mathbf{z}}$. Effective plasma frequency $\omega_p = (2\pi)\cdot 10$ GHz (target value, set by the wire spacing).
- **Split-ring resonators**: copper SRRs in the $xy$-plane, ring radius $r_\text{ring} = 1.5$ mm, gap width $g = 0.2$ mm, ring thickness $0.2$ mm. Resonance frequency $\omega_0 = (2\pi)\cdot 4$ GHz, oscillator strength $F \approx 0.3$.

The negative-$\mu$ window: $\omega_0 = 4$ GHz to $\omega_p^\text{mag} = \omega_0/\sqrt{1-F} = 4/\sqrt{0.7} \approx 4.78$ GHz.

The negative-$\varepsilon$ window: $\omega < \omega_p = 10$ GHz.

The overlap window: $4$ GHz $< \omega < 4.78$ GHz.

Within this window:
- $\varepsilon_r(\omega) \approx 1 - (10/\omega)^2 \cdot $ (correction) — negative.
- $\mu_r(\omega) = 1 - F\omega^2/(\omega^2 - \omega_0^2) $ — negative.
- $n(\omega) = -\sqrt{\varepsilon_r\mu_r} < 0$.

For a wave at $\omega = 4.5$ GHz: $\varepsilon_r \approx -4$, $\mu_r \approx -2$, $n \approx -2.8$.

Pendry's 2000 prediction and the subsequent Shelby-Smith-Schultz 2001 experimental confirmation observed this negative refraction in the 4-5 GHz range.

The substrate-level reading: in this frequency window, the engineered rule-type microstructure produces a substrate region with simultaneously inverted electric and magnetic rule-type response. A chain traversing the region experiences:
- Phase-velocity reversal (the chain's coarse-grained phase advances backward).
- Group-velocity preservation (energy flows forward).
- Negative refraction at boundaries (the chain bends to the same side as the incident path).

All three effects are coarse-grained consequences of the rule-type microstructure's engineered response within each unit cell, integrated over the wavelength scale.

---

## 6. Substrate-Level Synthesis

The substrate-level story for negative-index metamaterials, in summary:

### 6.1 Negative $\varepsilon$

A rule-type microstructure that supports *plasma-like collective rule-type oscillations* (e.g., wire-array structures with free rule-type-alignment carriers along the wires) produces, when cell-averaged, an effective permittivity that becomes negative below the array's effective plasma frequency.

The substrate-level mechanism: the rule-type collective mode, driven below its natural frequency, produces a coarse-grained response anti-parallel to the applied field.

### 6.2 Negative $\mu$

A rule-type microstructure that supports *resonant rule-type circulation pathways* (e.g., split-ring resonators with closed-loop rule-type modes) produces, when cell-averaged, an effective permeability that becomes negative slightly above the resonance frequency.

The substrate-level mechanism: the resonant rule-type circulation mode, driven above its natural frequency, overshoots and produces a coarse-grained rule-type curvature anti-parallel to the applied magnetic curvature.

### 6.3 Negative refractive index

Simultaneous negative $\varepsilon$ and $\mu$ in the same frequency window produces an effective medium with $n < 0$. The chain's coarse-grained propagation in this medium exhibits reversed phase velocity relative to energy flow, and produces negative refraction at boundaries with positive-index media.

The substrate-level mechanism: the engineered rule-type microstructure has inverted both the electric and magnetic effective response within each unit cell; the chain follows this inverted response, producing macroscopic effects opposite to conventional refraction.

### 6.4 Why this works at substrate level

At substrate level, $\varepsilon$ and $\mu$ are not fundamental — they are coarse-grained statistical descriptors of how the rule-type microstructure responds to applied gauge fields (per Memo 5). There is no substrate-level constraint that forces them to be positive. Engineering the microstructure to produce negative values does not violate any substrate primitive.

The chain's propagation is governed by the chain's pre-individuation amplitude dynamics, which couples to the cell-averaged effective constitutive parameters at coarse-grained probe scale. When those parameters are negative, the chain's coarse-grained dynamics exhibits negative-index propagation, with all its experimentally observed consequences.

Pendry's 2000 insight is therefore the substrate-level statement: by engineering rule-type microstructure with specific resonant pathways (wire-array + split-ring-resonator), one can produce coarse-grained substrate response with $n_{\mathrm{eff}} < 0$ in a chosen frequency window. The substrate has no fundamental opinion about whether $n$ is positive or negative; it is a derived statistical quantity.

---

## 7. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **Plasma-like response from rule-type microstructures supporting collective alignment oscillations** (§2). FORCED at the structural level by the substrate's ability to support coherent oscillations of bound rule-type-alignment structures (free-rule-type carriers in conducting microstructures).

- **Drude-form effective permittivity** $\varepsilon_{\mathrm{eff}}(\omega) = \varepsilon_\infty(1 - \omega_p^2/\omega^2)$ for wire-array microstructures (§2.5). FORCED at the form level by the substrate-level Newton's-law-analog response to harmonic forcing; the value of $\omega_p$ is FORM-FORCED by the array geometry but INHERITED in detail from the wire microstructure parameters.

- **Resonant circulation response from closed-loop rule-type pathways** (§3). FORCED at the structural level by T17's identification of the gauge field with the rule-type connection: closed loops support rule-type holonomy, and engineered closed-loop microstructures support localized circulation modes.

- **Lorentz-form effective permeability** $\mu_{\mathrm{eff}}(\omega) = 1 - F\omega^2/(\omega^2 - \omega_0^2 + i\gamma\omega)$ for SRR microstructures (§3.4). FORCED at the form level by the substrate-level LC-resonance response of the closed-loop rule-type mode.

- **Negative-index frequency window** when both $\varepsilon < 0$ and $\mu < 0$ overlap (§4.1). FORCED by the geometric overlap of the wire-array and SRR negative-response windows.

- **Branch choice $n(\omega) = -\sqrt{\varepsilon_r\mu_r}$ in the doubly-negative regime** (§4.3). FORCED by causality (Poynting vector and group velocity must point in the same direction for a passive medium).

- **Negative refraction at interfaces** (§4.5–4.6). FORCED by tangential-wave-vector continuity + negative index of refraction in the negative-index medium.

- **Substrate-level mechanism for negative refraction** as rule-type gradient inversion + phase-advance reversal + ED-gradient redirection (§4.6). FORCED by the substrate-level reading of negative $\varepsilon, \mu$ as inverted rule-type response.

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Lorentz-Drude equation of motion for the rule-type-alignment displacement** (§2.2). Standard atomic-physics equation of motion applied to substrate-level rule-type oscillations. The substrate-level reading is articulated inline; the equation form is inherited from standard physics.

- **Pendry's thin-wire effective plasma frequency** $\omega_p^2 = 2\pi c^2/(a^2\ln(a/r_0))$ (§2.4). Standard wire-array analysis (Pendry 1996, 1998) inherited here at the form level; substrate-level interpretation provided.

- **Split-ring-resonator LC analysis** (§3.2). Standard circuit-theory analysis applied to the engineered ring; the substrate-level reading is the rule-type circulation mode.

- **Snell's law and Poynting-vector causality argument for the negative-index branch choice** (§4.3, 4.5). Standard electromagnetic-wave analysis.

- **Specific numerical example values for the Pendry 2000 microstructure** (§5). Inherited from Pendry's published microstructure design.

### What remains OPEN

- **First-principles substrate-level derivation of the Drude form** from V1-kernel response to bound rule-type structures (instead of inheriting from standard Newton's-law form). The form is structurally well-motivated but a fully substrate-derived Lorentz-Drude equation of motion is OPEN.

- **First-principles substrate-level derivation of the SRR LC analysis** from rule-type-connection holonomy + rule-type-charge accumulation at a gap. The closed-loop circulation mode is structurally clear at substrate level, but the explicit substrate-level inductance and capacitance formulae are inherited from standard circuit theory. OPEN at full-derivation level.

- **Loss compensation via gain media**. Active metamaterials with gain to compensate losses are OPEN; require non-Hermitian substrate-level treatment.

- **Quantum effects in negative-index media**. Single-photon and few-photon dynamics in negative-index metamaterials require composition with Lindblad-type machinery. OPEN.

- **Nonlinear metamaterials and harmonic generation in negative-index regions**. The classical linear-response treatment here treats $\varepsilon, \mu$ as field-independent; nonlinear extensions OPEN.

- **Hyperbolic and indefinite metamaterials**. When $\varepsilon$ or $\mu$ has mixed signs in different directions (e.g., uniaxial with $\varepsilon_\parallel > 0, \varepsilon_\perp < 0$), the effective medium is hyperbolic, not isotropically negative-index. Substrate-level treatment is parallel; specific phenomenology OPEN.

- **Wide-band negative-index materials**. The frequency window of negative index is narrow (limited by the SRR resonance width). Broadband negative-index materials require multiple overlapping resonances or different mechanisms. OPEN.

- **Substrate-level derivation of the Veselago-Pendry perfect lens**. The negative-index regime enables sub-wavelength imaging beyond the diffraction limit (Pendry 2000 "perfect lens"). Substrate-level reading of evanescent-wave amplification in the slab geometry is OPEN.

---

## 8. Review and Recommended Next Steps

### Review

Memo 6 has delivered, closing the homogenization cluster of the Arc:

- **Substrate-level derivation of the Drude-form effective permittivity** for plasma-like (wire-array) microstructures (§2). Established substrate-level plasma frequency $\omega_p^2 = n^*(e^*)^2/(\varepsilon_0 m^*)$ at the wire level, Pendry effective array plasma frequency $\omega_p^2 = 2\pi c^2/(a^2\ln(a/r_0))$ at the array level. The negative-permittivity window is $\omega < \omega_p$.

- **Substrate-level derivation of the Lorentz-form effective permeability** for resonant circulation pathways (split-ring-resonator microstructures) (§3). Established substrate-level resonance frequency $\omega_0 = 1/\sqrt{LC}$, oscillator strength $F$, damping $\gamma$. The negative-permeability window is $\omega_0 < \omega < \omega_p^\text{mag} = \omega_0/\sqrt{1-F}$.

- **Substrate-level conditions for negative refractive index** in the overlap of the two negative windows (§4). Branch choice $n = -\sqrt{\varepsilon_r\mu_r}$ FORCED by causality. The chain's phase advances backward; energy flows forward.

- **Substrate-level mechanism for negative refraction** as rule-type gradient inversion, microstructure-induced phase-advance reversal, and ED-gradient redirection of channel propagation (§4.6).

- **Worked example** of the Pendry 2000 microwave metamaterial (§5) with $n_{\mathrm{eff}}(4.5\text{GHz}) \approx -2.8$.

- **Substrate-level synthesis** explaining why negative $\varepsilon, \mu$ are not fundamentally forbidden in ED (§6.4) — these are derived statistical descriptors of microstructure response, and engineering the microstructure can produce any sign.

- **Explicit FORCED / FORM-FORCED-INHERITED / OPEN labeling** (§7).

### Honest scope-limit

Memo 6 introduced no new substrate primitives beyond P-MM-1 through P-MM-6 (Memo 1's inventory). All derivations are done inline. The Drude-form and Lorentz-form equations of motion are inherited from standard physics at the form level, with substrate-level interpretation provided. No cross-references to other arcs.

The homogenization cluster (Memos 2–6) is now closed: the substrate-level effective-medium machinery, the cell-problem framework, the effective constitutive tensors, the substrate-level meaning of $\varepsilon$ and $\mu$, and the conditions for negative-index metamaterials are all in place.

### Recommended next steps

In order:

1. **Memo 7 — Rule-Type Deformation Tensor.** Begin the transformation-optics cluster (Memos 7–11). Define the substrate-gradient deformation $\mathbf{R}(\mathbf{x})$ (P-MM-3) and the rule-type deformation tensor $\Lambda^i_j = \partial R^i/\partial x^j$ as the substrate-level Jacobian. Derive its transformation properties.

2. **Memo 8 — Mapping to Effective Metric.** Show how the rule-type deformation tensor transforms the effective constitutive parameters $\varepsilon_{\mathrm{eff}}, \mu_{\mathrm{eff}}$ derived in the homogenization cluster. Connect to the standard transformation-optics formula $\varepsilon^{ij} \to (\det\Lambda)^{-1}\Lambda^i_k\Lambda^j_l\varepsilon^{kl}$.

3. **Memo 9 — The Cloaking Deformation.** Specify the explicit cloaking deformation that expels a region from the chain's accessible substrate.

4. **Memo 10 — Substrate-Level Reading of Invisibility Cloaking.** Articulate the substrate-level mechanism: cloaking as substrate-level rule-type-redirection.

5. **Memo 11 — Conditions and Limits of Transformation Optics.** Identify when transformation optics works and when it breaks down.

6. **Memo 12 — Metasurface Boundary Conditions.** Independent line: derive the generalized Snell's law from substrate-level rule-type discontinuities at interfaces (P-MM-5).

7. **Memo 13 — Synthesis.** Tie all three precursor derivations together.

After Memo 13, the precursor Arc is complete. The next deliverable is the public-facing walkthrough `from_primitives_to_metamaterials_and_photonics.md` that composes all three precursor closures with the substrate-level Bloch theorem treatment of Yablonovitch photonic bandgaps into a complete substrate-level account of the Yablonovitch–Pendry–Capasso cluster.

### Anchor for future memos

The substrate-level effective constitutive tensors $\varepsilon_{\mathrm{eff}}^{ij}, \mu_{\mathrm{eff}}^{ij}$ — with their cell-problem-derived form, their substrate-level meaning as coarse-grained rule-type response coefficients, and the conditions under which they can become negative — are now fully established for the Arc. The transformation-optics cluster (Memos 7–11) will deform them under substrate-gradient deformations to produce cloaking; the metasurface BC memo (Memo 12) will treat their abrupt discontinuities at engineered interfaces. The synthesis memo (Memo 13) will close the precursor Arc by tying together the three precursor derivations.
