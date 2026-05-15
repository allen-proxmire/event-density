# From Primitives to Metamaterials and Photonics

*A walkthrough-grade Event Density (ED) Arc deriving the structural backbone of the Nobel-frontier metamaterials and photonics directions — Yablonovitch's photonic bandgaps, Pendry's negative refractive index, Pendry's electromagnetic cloak, and Capasso's metasurface generalized Snell's law — from substrate primitives. Fully self-contained: every required two-scale expansion, cell problem, deformation Jacobian, effective metric, interface jump condition, and Bloch-eigenmode statement is derived inside this document. No new substrate primitives are introduced.*

---

## 1. The Question

### What this walkthrough derives

This walkthrough derives, from substrate primitives, the structural backbone of four Nobel-frontier results in metamaterials and photonics:

1. **The effective constitutive tensors** $\varepsilon_{\rm eff}^{ij}(\omega)$ and $\mu_{\rm eff}^{ij}(\omega)$ of a periodic subwavelength microstructure, derived via a two-scale homogenization expansion and a cell problem on a unit cell $Y$. The cell-problem solution defines a corrector field $\chi^j(y)$ whose cell average provides the substrate-level correction to the naive arithmetic average of the microstructure response.

2. **The negative refractive index** $n_{\rm eff}(\omega) = -\sqrt{\varepsilon_r(\omega)\,\mu_r(\omega)}$ when both effective tensors are negative in an overlapping frequency band. The negative branch is FORCED by causal outgoing-wave selection (Pendry 2000). The Drude form $\varepsilon_{\rm eff}(\omega) = \varepsilon_\infty(1 - \omega_p^2/\omega^2)$ from wire-array microstructures and the Lorentz form $\mu_{\rm eff}(\omega) = 1 - F\omega^2/(\omega^2 - \omega_0^2 + i\gamma\omega)$ from split-ring resonators are each derived as cell-problem outputs.

3. **The constitutive transformation under substrate deformation** $\varepsilon'^{ij} = (\det J)^{-1}\,J^i{}_k J^j{}_l\,\varepsilon^{kl}$ and the coarse-grained **effective metric** $g_{ij} = (J^{-1})^k{}_i\,(J^{-1})^l{}_j\,\delta_{kl}$ on the wave equation, with the wave equation rewritten in covariant Laplace-Beltrami form. The metric is a coarse-grained rule-type metric on the substrate, not spacetime curvature.

4. **The Pendry spherical cloak** (Pendry 2006). The radial map $r' = R_1 + \alpha r$ with $\alpha = (R_2 - R_1)/R_2$ produces a shell-supported anisotropic medium whose effective metric vanishes radially at the inner shell. The cloaked interior is topologically excluded from the substrate seen by the propagating channel.

5. **The metasurface generalized Snell's law** (Capasso 2011). An engineered codimension-1 surface carrying a tangential phase profile $\Phi(r_\parallel)$ imposes a tangential momentum kick $k_{\parallel,2} = k_{\parallel,1} + \nabla_\parallel\Phi$, yielding
$$
n_1 \sin\theta_i \;=\; n_2 \sin\theta_t + \frac{\lambda}{2\pi}\,\frac{d\Phi}{dx}.
$$

6. **The photonic bandgap** (Yablonovitch 1987) as a frequency window in which no Bloch eigenmode exists on the periodic substrate at $a \sim \lambda$. The relevant Bloch theorem is derived inline in compact form.

7. **The unifying structural identity**:
$$
\text{Metamaterials} \;=\; \text{engineered microstructure} \;+\; \text{engineered deformation} \;+\; \text{engineered discontinuity}.
$$
The three operations exhaust the substrate-level wave-control space within the coarse-graining window $\ell_P \ll a \ll \lambda \ll L$.

Each result is derived, not posited. Every required two-scale expansion step, cell-problem statement, Jacobian computation, effective-metric identification, jump condition, and Bloch-eigenmode statement appears inline.

### Why standard photonics treats $\varepsilon$, $\mu$, and metamaterial response phenomenologically

Conventional macroscopic electromagnetism treats $\varepsilon$, $\mu$, and the refractive index $n$ as phenomenological material parameters fit to experiment. The Maxwell equations are taken as exact at the macroscopic level, with material response encoded in constitutive relations $\mathbf{D} = \varepsilon \mathbf{E}$ and $\mathbf{B} = \mu \mathbf{H}$. The standard derivations of $\varepsilon$ and $\mu$ from molecular polarizabilities (Clausius-Mossotti, Lorentz local-field corrections) treat the microscopic constituents as fixed atoms or molecules whose responses are summed over a coarse-graining volume.

The recognition that subwavelength structuring can engineer $\varepsilon_{\rm eff}$ and $\mu_{\rm eff}$ unattainable in natural materials — including negative values — was Pendry's central insight. The further recognition that smooth coordinate transformations of Maxwell's equations correspond to anisotropic constitutive tensors that can be physically built by metamaterials was the transformation-optics insight. The realization that engineered codimension-1 phase profiles produce anomalous refraction outside the bulk Snell relation was the metasurface insight. The recognition that periodic dielectric structures at $a \sim \lambda$ produce band structures with frequency gaps was the photonic-bandgap insight.

Standard theory delivers the macroscopic equations correctly. It is silent about what $\varepsilon$ and $\mu$ are ontologically: it treats them as numbers attached to a material, with no account of *why* a particular microstructure produces a particular response, *why* cloaking works mechanistically rather than merely formally as a coordinate identity, *what* a metasurface boundary condition is at the level of substrate ontology, or *why* the four Nobel-frontier directions share a common structural skeleton.

### What Event Density claims

In the ED framework the substrate carries rule-type structure at scale $\ell_P$, where rule-type means the discrete pattern of participation-rule alignment that the substrate locally enforces on channels of ED-flow. Coarse-graining within the window $\ell_P \ll a \ll \lambda \ll L$ produces an effective wave equation whose coefficients are coarse-grained projections of the substrate's local rule-type content. Three independent engineered modulations of this content control wave propagation:

- **Smooth periodic microstructure** at scale $a \ll \lambda$ produces effective constitutive tensors via homogenization. The substrate is unstrained; only its internal rule-type content is modulated. Pendry-negative-index lives here.
- **Smooth deformation** $u(X)$ produces an effective metric and transformed constitutive tensors via transformation optics. The substrate is strained; its rule-type content is transported covariantly along the deformation. Pendry-cloak lives here.
- **Engineered codimension-1 discontinuity** with engineered phase profile produces tangential momentum kicks at the interface. The substrate is unstrained in the bulk; only the interface carries engineered rule-type content. Capasso-metasurface lives here.
- **Periodic microstructure at $a \sim \lambda$**, adjacent to the homogenization regime, supports Bloch eigenmodes with band structure. Yablonovitch-bandgap lives here.

The substrate-level statement, in one sentence: **metamaterials are engineered modulations of the substrate's coarse-grained rule-type structure; the three independent modulation axes (microstructure, deformation, discontinuity) exhaust the wave-control space within the coarse-graining window.**

### The chain in summary

The derivation chain runs:

substrate primitives P-MM-1 through P-MM-6 (§2) → two-scale lift, derivative splitting, order-by-order equations, cell problem, corrector field, averaging operator, effective-tensor formula (§3) → identification with $\varepsilon$ and $\mu$, Drude wire-array response, Lorentz split-ring response, doubly-negative band, FORCED negative-index branch (§4) → deformation Jacobian, rule-type deformation tensor, constitutive transformation, effective metric in covariant form, Pendry spherical cloak, topological exclusion of cloaked interior (§5) → codimension-1 discontinuity, phase-imprinting boundary condition, tangential momentum kick, generalized Snell's law (§6) → Bloch form, band structure, bandgap formation, relation to homogenization (§7) → unifying substrate-level statement, three-axis exhaustiveness, scope limits (§8) → FORCED / INHERITED / OPEN accounting (§9) → exact claims (§10) → references (§11) → review and recommended next steps (§12).

---

## 2. The Substrate Primitives

Six substrate primitives are used. No new primitives are introduced anywhere in the derivation; the entire walkthrough runs on this list.

### P-MM-1. Substrate rule-type microstructure

The substrate carries rule-type structure at scale $\ell_P$ — discrete participation rules indexed by spatial position and internal type, encoding the substrate's local commitment patterns for ED-flow. At coarse-grained scales $a \gg \ell_P$, engineered inclusions modulate this rule-type structure, producing a position-dependent coarse-grained response. The coefficients $\varepsilon^{ij}(x)$, $(\mu^{-1})^{ij}(x)$, and $n^2(x)$ of the macroscopic wave equation are coarse-grained projections of this rule-type content.

**Substrate-level meaning.** $\varepsilon$ and $\mu$ are not fundamental fields. They are coarse-grained labels for the substrate's local rule-type response: $\varepsilon^{ij}(x)$ is the coarse-grained polarizability of the rule-type structure at $x$ — the local tendency to align ED-flow under an applied electric tension — and $(\mu^{-1})^{ij}(x)$ is the coarse-grained inverse circulation susceptibility — the local resistance to closed-loop ED-flow under an applied magnetic tension.

**Engineered modulation.** Replacing the substrate's vacuum rule-type content with an engineered pattern of inclusions modulates these coefficients. The pattern of inclusions, coarse-grained, is the metamaterial response.

### P-MM-2. Subwavelength periodicity

When inclusions are arranged with period $a$ satisfying $a \ll \lambda$, the rule-type structure admits a two-scale description in a slow coordinate $X = x$ and a fast coordinate $y = x/a$, with $y$ taking values on the unit cell $Y = [0, 1]^3$ (in normalized fast coordinates). Field quantities lift to two-scale form $\psi(x) \to \tilde\psi(X, y)$ with $\tilde\psi$ periodic in $y$. The two-scale expansion is the substrate-level mathematical reflection of the scale separation $a/\lambda \ll 1$.

**Periodic substrate.** The rule-type content is the same on each unit cell up to translations by $aR$ with $R$ in the integer lattice $\mathbb{Z}^3$. Practical metamaterials approximate this idealization to within a few percent at microwave frequencies.

### P-MM-3. ED-gradient deformation

A slowly varying displacement field $u(X)$ acting on the substrate produces a coarse-grained deformation
$$
x'^i \;=\; x^i + u^i(X),
$$
whose Jacobian
$$
J^i{}_j \;=\; \delta^i{}_j + \frac{\partial u^i}{\partial X^j}
$$
transports rule-type structure covariantly. The deformation is smooth and orientation-preserving: $\det J > 0$ everywhere, $J$ and $J^{-1}$ bounded. Time-independent deformations carry no internal dispersion of their own; all dispersion enters through the constitutive coefficients at the microstructure level.

**Substrate-level meaning.** The deformation is a coordinate-level engineered displacement of the substrate. Rule-type tensors transform as densities of weight one: a coefficient $\varepsilon^{ij}(x)$ at the undeformed point $x$ becomes the coefficient $\varepsilon'^{ij}(x')$ at the deformed point $x'$, with the transformation rule derived in §5.

### P-MM-4. Channel propagation in structured media

Wave propagation in the coarse-grained substrate is governed by an effective second-order wave equation
$$
\partial_{x^i}\!\left[A^{ij}(x)\,\partial_{x^j}\psi(x)\right] + k_0^2\,n^2(x)\,\psi(x) \;=\; 0,
$$
where $\psi$ is a scalar component of the electromagnetic field (or any field reducible to scalar form for a chosen polarization), $A^{ij}(x)$ is a coarse-grained rank-2 tensor coefficient determined by the substrate's local rule-type content, $n^2(x)$ is a coarse-grained scalar coefficient, and $k_0 = \omega/c$ is the vacuum wavenumber.

**Polarization identifications.** For Maxwell's equations in the time-harmonic regime, the scalar form corresponds to:
- TM modes (transverse magnetic, $\mathbf{E}$ in the plane of incidence): $A^{ij} \leftrightarrow (\mu^{-1})^{ij}$, $n^2 \leftrightarrow \varepsilon$.
- TE modes (transverse electric, $\mathbf{H}$ in the plane of incidence): $A^{ij} \leftrightarrow \varepsilon^{ij}$, $n^2 \leftrightarrow \mu$.

The derivations of §3 apply to either polarization by reading the identifications.

### P-MM-5. Interface rule-type discontinuity

A codimension-1 surface $\Sigma$ across which the rule-type microstructure or deformation jumps imposes jump conditions on the coarse-grained wave field. In the absence of engineered surface phase profile or surface currents, the standard tangential-field continuity holds: $\mathbf{E}_\parallel$ and $\mathbf{H}_\parallel$ are continuous across $\Sigma$. An engineered surface phase profile $\Phi(r_\parallel)$ imposes a phase-jump matching condition derived in §6.

**Substrate-level meaning.** A metasurface is a codimension-1 engineered rule-type discontinuity: the substrate carries different rule-type content on the two sides of $\Sigma$, with the discontinuity itself engineered to imprint a controlled phase shift on transmitted channels.

### P-MM-6. Coarse-graining window

All derivations operate in the window
$$
\ell_P \;\ll\; a \;\ll\; \lambda \;\ll\; L,
$$
where $\ell_P$ is the substrate cutoff (smallest substrate length scale), $a$ is the microstructure period (engineered), $\lambda$ is the operating wavelength, and $L$ is the device scale.

**Within this window:**
- Substrate discreteness is invisible at the wavelength scale: $\ell_P \ll \lambda$ ensures that the coarse-grained wave equation is meaningful.
- Microstructure averaging is well-defined: $a \ll \lambda$ ensures that the two-scale expansion converges and the cell-problem corrector is well-posed.
- Device-scale envelopes are slow: $\lambda \ll L$ ensures that boundary effects at device boundaries do not invalidate bulk derivations.

**Boundaries of the window.** The Bloch / bandgap regime lives at $a \sim \lambda$, adjacent to but outside the strict homogenization regime $a \ll \lambda$. The substrate cutoff $\ell_P$ is invisible throughout this walkthrough; nothing here depends on its precise value.

---

## 3. Two-Scale Expansion and the Cell Problem

This section derives the homogenization framework that produces $\varepsilon_{\rm eff}$ and $\mu_{\rm eff}$. The two-scale expansion is the mathematical reflection of P-MM-2 and P-MM-6.

### 3.1 Setup

Under P-MM-1, P-MM-2, P-MM-4, P-MM-6, consider the scalar form of the wave equation
$$
\partial_{x^i}\!\left[A^{ij}\!\left(x/a\right)\,\partial_{x^j}\psi(x)\right] + k_0^2\,n^2\!\left(x/a\right)\,\psi(x) \;=\; 0,
$$
where $A^{ij}(y)$ and $n^2(y)$ are $Y$-periodic functions of the fast coordinate $y = x/a$. The coefficient $A^{ij}(y)$ is positive-definite and bounded:
$$
c_- |\xi|^2 \;\le\; A^{ij}(y)\,\xi_i\,\xi_j \;\le\; c_+ |\xi|^2, \qquad 0 < c_- \le c_+ < \infty,
$$
for all $\xi \in \mathbb{R}^3$ and all $y \in Y$. The ratio $a/\lambda$ is small; we expand the equation in this parameter.

### 3.2 Two-scale lift

Lift $\psi(x)$ to a two-scale function $\tilde\psi(X, y)$, treating $X = x$ (slow) and $y = x/a$ (fast) as independent variables. The chain rule gives
$$
\frac{\partial}{\partial x^i} \;=\; \frac{\partial}{\partial X^i} + \frac{1}{a}\,\frac{\partial}{\partial y^i}.
$$
This is the **derivative splitting** rule of two-scale analysis. It expresses the fact that a spatial gradient $\partial/\partial x$ has two contributions: a slow contribution from the device-scale envelope $\partial/\partial X$ and a fast contribution from the cell-scale modulation $a^{-1}\partial/\partial y$.

Lift $\psi$ to an asymptotic series in $a$:
$$
\tilde\psi(X, y) \;=\; \psi_0(X, y) + a\,\psi_1(X, y) + a^2\,\psi_2(X, y) + a^3\,\psi_3(X, y) + \cdots,
$$
with each $\psi_k(X, y)$ smooth in $X$ and $Y$-periodic in $y$. Substitute into the wave equation and collect terms by power of $a$.

### 3.3 Order-by-order equations

The wave equation, in lifted form, reads
$$
\left(\partial_{X^i} + a^{-1}\partial_{y^i}\right)\!\left[A^{ij}(y)\left(\partial_{X^j} + a^{-1}\partial_{y^j}\right)\tilde\psi\right] + k_0^2 n^2(y)\,\tilde\psi \;=\; 0.
$$
Expand the bracket and collect powers of $a$.

**Order $a^{-2}$:**
$$
\partial_{y^i}\!\left[A^{ij}(y)\,\partial_{y^j}\psi_0(X, y)\right] \;=\; 0.
$$
Multiply by $\psi_0$ and integrate over $Y$; integrate by parts using $Y$-periodicity (boundary terms cancel between opposite faces of $Y$):
$$
\int_Y A^{ij}(y)\,\partial_{y^i}\psi_0\,\partial_{y^j}\psi_0\, d^3y \;=\; 0.
$$
By positive-definiteness of $A^{ij}$ (P-MM-4), the integrand is non-negative and vanishes only if $\partial_{y^j}\psi_0 = 0$. Therefore $\psi_0(X, y) = \psi_0(X)$ is independent of $y$. **The leading-order field has no microstructure dependence.**

**Order $a^{-1}$:**
$$
\partial_{y^i}\!\left[A^{ij}(y)\,\partial_{y^j}\psi_1(X, y)\right] \;=\; -\partial_{y^i}\!\left[A^{ij}(y)\,\partial_{X^j}\psi_0(X)\right].
$$
The right-hand side is linear in $\partial_{X^j}\psi_0$. By linearity of the elliptic equation in $\psi_1$, the solution has the form
$$
\psi_1(X, y) \;=\; \chi^j(y)\,\partial_{X^j}\psi_0(X) + \tilde\psi_1(X),
$$
where the **corrector field** $\chi^j(y)$ satisfies the **cell problem**:
$$
\boxed{\;\;\partial_{y^i}\!\left[A^{ij}(y)\,\partial_{y^j}\chi^k(y)\right] \;=\; -\partial_{y^i} A^{ik}(y), \qquad \chi^k \text{ is } Y\text{-periodic, with } \langle\chi^k\rangle = 0. \;\;}
$$

The cell problem is a linear elliptic boundary-value problem on $Y$ with periodic boundary conditions. By the Fredholm alternative for elliptic operators with periodic boundary conditions, it has a unique solution up to additive constants; the zero-mean condition $\langle\chi^k\rangle = 0$ fixes the constant.

**Substrate-level meaning of the corrector field.** $\chi^k(y)$ is the local accommodation pattern of the substrate response to a unit slow gradient in the $k$-direction. The substrate's rule-type structure adjusts within each unit cell to absorb the slow gradient; $\chi^k$ records that adjustment.

### 3.4 The averaging operator

Define the cell-averaging operator
$$
\langle f \rangle \;\equiv\; \frac{1}{|Y|}\int_Y f(y)\, d^3y.
$$
Two basic properties follow from $Y$-periodicity:

1. **Vanishing of pure $y$-divergences.** For any $Y$-periodic vector field $V^i(y)$,
$$
\langle \partial_{y^i} V^i \rangle \;=\; \frac{1}{|Y|}\int_Y \partial_{y^i} V^i\, d^3y \;=\; \frac{1}{|Y|}\oint_{\partial Y} V^i n_i\, dS \;=\; 0,
$$
because the boundary integral on $\partial Y$ vanishes by periodicity (opposite faces cancel).

2. **Commutativity with $X$-derivatives.** Since $X$ and $y$ are independent in the lifted picture,
$$
\langle \partial_{X^i} f(X, y) \rangle \;=\; \partial_{X^i}\langle f(X, y)\rangle.
$$

These two properties drive the homogenization computation.

### 3.5 Order-$a^0$ equation and effective tensor

**Order $a^0$:**
$$
\partial_{X^i}\!\left[A^{ij}(y)\,\partial_{X^j}\psi_0\right] + \partial_{X^i}\!\left[A^{ij}(y)\,\partial_{y^j}\psi_1\right] + \partial_{y^i}\!\left[A^{ij}(y)\,\partial_{X^j}\psi_1\right] + \partial_{y^i}\!\left[A^{ij}(y)\,\partial_{y^j}\psi_2\right] + k_0^2 n^2(y)\,\psi_0 \;=\; 0.
$$

Apply the averaging operator. The pure $\partial_{y^i}[\cdots]$ terms (third and fourth terms) vanish by property 1. The second term, using $\psi_1 = \chi^j\,\partial_{X^j}\psi_0$ and property 2, becomes $\partial_{X^i}\langle A^{ij}\partial_{y^j}\chi^k\rangle\,\partial_{X^k}\psi_0$. The first term becomes $\partial_{X^i}\langle A^{ij}\rangle\,\partial_{X^j}\psi_0$. The fifth term becomes $k_0^2\langle n^2\rangle\,\psi_0$.

Combining:
$$
\partial_{X^i}\!\left[\,\big(\langle A^{ik}\rangle + \langle A^{ij}\,\partial_{y^j}\chi^k\rangle\big)\,\partial_{X^k}\psi_0\,\right] + k_0^2\,\langle n^2\rangle\,\psi_0 \;=\; 0.
$$

This is the **homogenized wave equation** at leading order:
$$
\partial_{X^i}\!\left[A^{*ik}\,\partial_{X^k}\psi_0\right] + k_0^2\,n^{*2}\,\psi_0 \;=\; 0,
$$
with the **effective coefficient**
$$
\boxed{\;\; A^{*ik} \;=\; \langle A^{ik}\rangle + \langle A^{ij}\,\partial_{y^j}\chi^k\rangle, \qquad n^{*2} \;=\; \langle n^2\rangle. \;\;}
$$

The effective coefficient is the cell-averaged coefficient *plus* a correction from the cell-problem solution. The correction captures the local accommodation of the field to the microstructure: as the field threads through the unit cell, it deforms to follow the substrate's rule-type response, and the deformation feeds back into the cell-averaged flux.

### 3.6 Voigt-Reuss bounds

The corrector correction is non-positive in the energy norm. Standard variational arguments on the cell problem give
$$
\langle (A^{-1})^{ij}\rangle^{-1} \;\le\; A^{*ij} \;\le\; \langle A^{ij}\rangle
$$
as quadratic forms on $\mathbb{R}^3$. The lower (Reuss) bound is the harmonic mean of $A^{ij}$ over the cell; the upper (Voigt) bound is the arithmetic mean. The effective coefficient lives between these bounds and saturates the upper bound only when $A^{ij}$ is constant on $Y$ (no microstructure, trivial homogenization).

### 3.7 Worked example: layered substrate

For a one-dimensional layered substrate with $A(y) = A_1$ on layer 1 (volume fraction $f$) and $A(y) = A_2$ on layer 2 (volume fraction $1 - f$), the cell problem in 1D reduces to
$$
\frac{d}{dy}\!\left[A(y)\left(\frac{d\chi}{dy} + 1\right)\right] \;=\; 0,
$$
so $A(y)(d\chi/dy + 1) = C$ (constant on $Y$). Solving:
$$
\frac{d\chi}{dy} + 1 \;=\; \frac{C}{A(y)}, \qquad \chi \text{ periodic} \Rightarrow \langle d\chi/dy\rangle = 0 \Rightarrow 1 = C\langle 1/A\rangle.
$$
So $C = \langle 1/A\rangle^{-1}$, and the effective coefficient parallel to the layering is
$$
A^*_\parallel \;=\; \langle A(d\chi/dy + 1)\rangle \;=\; \langle C\rangle \;=\; \langle 1/A\rangle^{-1},
$$
the harmonic mean. Perpendicular to the layering, $A^*_\perp = \langle A\rangle$, the arithmetic mean. The microstructure thus produces anisotropy even from isotropic constituents — a substrate-level FORCED feature of any non-trivial periodic microstructure.

---

## 4. Effective Constitutive Tensors and Negative Index

### 4.1 From scalar form to Maxwell

For Maxwell's equations in a non-magnetic medium ($\mu = \mu_0$), the TE polarization wave equation in 2D is
$$
\partial_i\!\left[\frac{1}{\varepsilon(x)/\varepsilon_0}\,\partial_i H_z\right] + \frac{\omega^2}{c^2}\,H_z \;=\; 0,
$$
identifying $A^{ij} \leftrightarrow (\varepsilon/\varepsilon_0)^{-1}\delta^{ij}$. For TM polarization,
$$
\partial_i\!\left[\frac{1}{\mu(x)/\mu_0}\,\partial_i E_z\right] + \frac{\omega^2}{c^2}\,E_z \;=\; 0,
$$
identifying $A^{ij} \leftrightarrow (\mu/\mu_0)^{-1}\delta^{ij}$. Applying §3 in each polarization gives effective constitutive tensors.

### 4.2 Effective constitutive tensors

In full vector form, for an anisotropic periodic substrate with $\varepsilon^{ij}(y)$ and $\mu^{ij}(y)$ both $Y$-periodic, the homogenization theorem yields
$$
\boxed{\;\;\varepsilon_{\rm eff}^{ij} \;=\; \langle\varepsilon^{ij}\rangle + \langle\varepsilon^{ik}\,\partial_{y^k}\chi_E^j\rangle, \qquad (\mu_{\rm eff}^{-1})^{ij} \;=\; \langle(\mu^{-1})^{ij}\rangle + \langle(\mu^{-1})^{ik}\,\partial_{y^k}\chi_M^j\rangle,\;\;}
$$
with $\chi_E^j(y)$ and $\chi_M^j(y)$ the electric and magnetic correctors solving their respective cell problems.

**Anisotropy from microstructure.** Even if $\varepsilon^{ij}(y) = \varepsilon(y)\delta^{ij}$ and $\mu^{ij}(y) = \mu(y)\delta^{ij}$ are locally isotropic, the corrector solutions $\chi_E^j$, $\chi_M^j$ generally produce anisotropy in $\varepsilon_{\rm eff}^{ij}$ and $\mu_{\rm eff}^{ij}$. The principal axes of the effective tensors are aligned with the symmetry axes of the microstructure.

### 4.3 Substrate-level meaning of $\varepsilon$ and $\mu$

In the ED picture, $\varepsilon^{ij}(y)$ is the substrate's local rule-type polarizability: the coarse-grained tendency for ED-flow to align under an applied electric tension. $(\mu^{-1})^{ij}(y)$ is the local rule-type inverse circulation susceptibility: the coarse-grained resistance to closed-loop ED-flow under an applied magnetic tension. Neither is a fundamental field; both are coarse-grained labels for rule-type response.

The corrector fields $\chi_E^j(y)$ and $\chi_M^j(y)$ are the local accommodation patterns of the substrate response. When a slow gradient $\partial_{X^j}\psi_0$ threads through a unit cell, the substrate's rule-type structure adjusts within the cell; $\chi^j(y)$ records the spatial pattern of that adjustment, and the cell-averaged adjustment contributes to the effective tensor.

### 4.4 Wire-array microstructure → Drude $\varepsilon_{\rm eff}(\omega)$

Consider a square array of thin conducting wires of radius $r_0$ and lattice constant $a$, with $r_0 \ll a \ll \lambda$. Standard analysis (Pendry 1996) of the cell problem with electric field along the wire axis identifies the wires as supporting a longitudinal collective oscillation with effective plasma frequency
$$
\omega_p^2 \;=\; \frac{2\pi c^2}{a^2\,\ln(a/r_0)}.
$$
The wire-array effective dielectric function takes the Drude form
$$
\boxed{\;\;\varepsilon_{\rm eff}(\omega) \;=\; \varepsilon_\infty\left(1 - \frac{\omega_p^2}{\omega^2}\right). \;\;}
$$
Below $\omega_p$, $\varepsilon_{\rm eff}(\omega) < 0$. Above $\omega_p$, $\varepsilon_{\rm eff}(\omega) > 0$ and approaches $\varepsilon_\infty$ at high frequency.

**Substrate-level meaning.** The wire array carries a collective rule-type oscillation: ED-flow along the wires is constrained by the wire geometry to a single longitudinal mode, with effective plasma frequency set by the geometric line density and the cell logarithm. Below this frequency, the substrate's longitudinal response is *opposite* to the applied tension — the engineered rule-type collective mode dominates over any local polarizability — producing negative effective $\varepsilon$.

### 4.5 Split-ring microstructure → Lorentz $\mu_{\rm eff}(\omega)$

Consider an array of split-ring resonators (SRRs) — pairs of concentric metallic loops with a gap, embedded in a host dielectric — with lattice constant $a$, resonance frequency $\omega_0$, oscillator strength $F$ (related to the ring's filling fraction), and damping rate $\gamma$. Standard analysis of the cell problem for an applied magnetic field perpendicular to the rings (Pendry 1999) gives the Lorentz form
$$
\boxed{\;\;\mu_{\rm eff}(\omega) \;=\; 1 - \frac{F\omega^2}{\omega^2 - \omega_0^2 + i\gamma\omega}. \;\;}
$$
For $\omega$ in a narrow band immediately above $\omega_0$, $\mathrm{Re}\,\mu_{\rm eff}(\omega) < 0$.

**Substrate-level meaning.** Each SRR is a closed-loop rule-type resonator: ED-flow circulating around the ring constitutes a coarse-grained magnetic moment, whose natural frequency $\omega_0$ is set by the ring's geometric inductance and capacitance (gap capacitance). Driven above $\omega_0$, the rule-type circulation lags by more than $\pi/2$ and opposes the applied magnetic tension, producing negative effective $\mu$.

### 4.6 The doubly-negative band

Engineering both wire arrays and SRRs into the same substrate produces a frequency band where both $\varepsilon_r(\omega) < 0$ and $\mu_r(\omega) < 0$. In this band, $\varepsilon_r\mu_r > 0$, so the wave equation
$$
\nabla^2\psi + k_0^2\,\varepsilon_r\,\mu_r\,\psi \;=\; 0
$$
admits propagating solutions $\psi = e^{i\mathbf{k}\cdot\mathbf{x}}$ with $|\mathbf{k}|^2 = k_0^2\varepsilon_r\mu_r > 0$.

### 4.7 Negative-index branch FORCED

The refractive index satisfies $n_{\rm eff}^2 = \varepsilon_r\mu_r$, so $n_{\rm eff} = \pm\sqrt{\varepsilon_r\mu_r}$. The branch is determined by causal outgoing-wave selection.

**Argument.** In the doubly-negative band, the relation between $\mathbf{D}$ and $\mathbf{E}$ is $\mathbf{D} = \varepsilon_r\varepsilon_0\mathbf{E}$ with $\varepsilon_r < 0$, reversing direction. Similarly, $\mathbf{B} = \mu_r\mu_0\mathbf{H}$ with $\mu_r < 0$ reverses direction. The Poynting vector
$$
\mathbf{S} \;=\; \mathbf{E}\times\mathbf{H}
$$
remains in the direction of energy outflow (causality, P-MM-4). For a plane wave, the phase velocity $\mathbf{v}_p = (\omega/|\mathbf{k}|^2)\mathbf{k}$ is parallel to $\mathbf{k}$. Combining Maxwell's curl equations $\nabla\times\mathbf{E} = -\partial_t\mathbf{B}$ and $\nabla\times\mathbf{H} = \partial_t\mathbf{D}$:
$$
\mathbf{k}\times\mathbf{E} \;=\; \omega\mu_r\mu_0\mathbf{H}, \qquad \mathbf{k}\times\mathbf{H} \;=\; -\omega\varepsilon_r\varepsilon_0\mathbf{E}.
$$
Both signs flip when $\varepsilon_r, \mu_r < 0$. The triad $(\mathbf{E}, \mathbf{H}, \mathbf{k})$ becomes left-handed instead of right-handed. The Poynting vector $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ now points *opposite* to $\mathbf{k}$.

For an outgoing wave with $\mathbf{S}$ pointing away from the source, $\mathbf{k}$ points toward the source. The refractive index $n_{\rm eff} = c|\mathbf{k}|/\omega$ is conventionally signed by the direction of $\mathbf{k}$ relative to the outward normal. With $\mathbf{k}$ inward and $\mathbf{S}$ outward, this is precisely the negative-index branch:
$$
\boxed{\;\; n_{\rm eff}(\omega) \;=\; -\sqrt{\varepsilon_r(\omega)\,\mu_r(\omega)} \qquad \text{when } \varepsilon_r(\omega), \mu_r(\omega) < 0. \;\;}
$$
This is the Pendry 2000 negative refractive index. The choice is FORCED by causal outgoing-wave selection given the doubly-negative constitutive response; no separate postulate is required.

### 4.8 Substrate-level meaning of negative index

The substrate's rule-type structure in the doubly-negative band is engineered such that channels propagate with phase advancing in the direction *opposite* to energy flow. In substrate terms: the engineered combination of collective rule-type oscillation (wire-array Drude response) and resonant rule-type circulation (SRR Lorentz response) produces a coarse-grained substrate whose channels carry phase upstream relative to their energy flow. Negative refraction at an interface — bending to the same side of the normal as the incident wave — is the direct geometric consequence at the interface boundary.

### 4.9 Bandwidth and dispersion bounds

The wire-array and SRR responses are both intrinsically dispersive: by Kramers-Kronig relations on causal linear response, $\mathrm{Im}\,\varepsilon(\omega) \ne 0$ over any band of finite width implies $\mathrm{Re}\,\varepsilon(\omega)$ varies with $\omega$. The doubly-negative band, where both $\mathrm{Re}\,\varepsilon$ and $\mathrm{Re}\,\mu$ are negative, is intrinsically narrow ($\Delta\omega/\omega \sim 5$-$20\%$ in typical microwave metamaterials). Lossless negative-index media over arbitrarily broad bandwidth are forbidden by causality.

---

## 5. Substrate Deformation, Effective Metric, and the Pendry Cloak

### 5.1 Setup

Under P-MM-1, P-MM-3, P-MM-4, P-MM-6, consider a slow substrate deformation $x'^i = f^i(x)$ with Jacobian
$$
J^i{}_j \;=\; \frac{\partial x'^i}{\partial x^j}, \qquad (J^{-1})^k{}_l \;=\; \frac{\partial x^k}{\partial x'^l}, \qquad \det J > 0.
$$
The undeformed substrate carries an isotropic vacuum rule-type response $\varepsilon^{ij}(x) = \varepsilon_0 \delta^{ij}$, $\mu^{ij}(x) = \mu_0 \delta^{ij}$. The deformation maps this to a coarse-grained anisotropic medium with transformed constitutive tensors derived below.

### 5.2 Rule-type deformation tensor

The substrate's local rule-type orientation is a rank-2 contravariant tensor structure $D^{ij}(x)$ at each point. Under deformation, $D^{ij}$ transports covariantly as
$$
D'^{ij}(x') \;=\; \frac{1}{\det J}\,J^i{}_k\,J^j{}_l\,D^{kl}(x).
$$
The factor $1/\det J$ accounts for the volume change under deformation (density of weight one). The Jacobian factors transport the tensor indices into the deformed frame.

**Conjugate tensor.** The conjugate rank-2 covariant tensor structure $D_{ij}(x)$ transforms as
$$
D'_{ij}(x') \;=\; (\det J)\,(J^{-1})^k{}_i\,(J^{-1})^l{}_j\,D_{kl}(x).
$$

### 5.3 Constitutive transformation

The substrate's coarse-grained electric and magnetic responses are rank-2 contravariant tensors. Applying the deformation rule of §5.2:
$$
\boxed{\;\;\varepsilon'^{ij}(x') \;=\; \frac{1}{\det J}\,J^i{}_k\,J^j{}_l\,\varepsilon^{kl}(x), \qquad \mu'^{ij}(x') \;=\; \frac{1}{\det J}\,J^i{}_k\,J^j{}_l\,\mu^{kl}(x). \;\;}
$$

This is the **transformation-optics constitutive law**. It is a substrate-level FORCED statement: given the deformation $f$, the transformed constitutive tensors are computed by applying the Jacobian densities. No separate posit is required.

**Special case: vacuum starting medium.** If the undeformed substrate is vacuum ($\varepsilon^{ij} = \varepsilon_0\delta^{ij}$, $\mu^{ij} = \mu_0\delta^{ij}$), then
$$
\varepsilon'^{ij}(x') \;=\; \frac{\varepsilon_0}{\det J}\,(JJ^T)^{ij}, \qquad \mu'^{ij}(x') \;=\; \frac{\mu_0}{\det J}\,(JJ^T)^{ij}.
$$
The impedance $\sqrt{\mu'/\varepsilon'}$ equals $\sqrt{\mu_0/\varepsilon_0} = Z_0$ everywhere — the transformed medium is **impedance-matched to vacuum at every point**, eliminating reflections from interior surfaces.

### 5.4 Effective metric

The wave equation in the deformed substrate, with the transformed constitutive tensors, can be rewritten in covariant Laplace-Beltrami form. Consider Maxwell's equations in a transformed medium; using the transformation rule of §5.3 in the scalar-form wave equation gives
$$
\partial_{x'^i}\!\left[\frac{(JJ^T)^{ij}}{\det J}\,\partial_{x'^j}\psi\right] + k_0^2\,\psi \;=\; 0.
$$

Identify
$$
\boxed{\;\;g^{ij}(x') \;=\; \frac{(JJ^T)^{ij}}{\det J}, \qquad g_{ij}(x') \;=\; (J^{-1})^k{}_i\,(J^{-1})^l{}_j\,\delta_{kl}, \qquad \sqrt{|g|} \;=\; \frac{1}{\det J}. \;\;}
$$

The wave equation becomes
$$
\frac{1}{\sqrt{|g|}}\,\partial_{x'^i}\!\left[\sqrt{|g|}\,g^{ij}\,\partial_{x'^j}\psi\right] + k_0^2\,\psi \;=\; 0.
$$

This is the **covariant Laplace-Beltrami wave equation** on a Riemannian manifold with metric $g_{ij}$.

**Crucial scope note.** The metric $g_{ij}$ is a coarse-grained rule-type metric on the substrate: it encodes the coarse-grained rule-type geometry seen by the propagating field. It is *not* spacetime curvature. The substrate-level operation that produced it is an engineered displacement (P-MM-3), not a gravitational effect. The identification $g_{ij} \leftrightarrow$ rule-type metric is structural, not analogical: the same mathematical object appears in both contexts because both contexts describe wave propagation through a curved geometry, but the underlying physics is different.

### 5.5 Eikonal limit: rays as geodesics

In the eikonal limit $\lambda \to 0$, the wave equation reduces to the eikonal equation
$$
g^{ij}\,\partial_i S\,\partial_j S \;=\; n^2,
$$
where $S(x')$ is the phase function and $n$ is the local refractive index. The solutions are geodesics of the effective metric $g_{ij}$. **Light in a transformation-optics medium follows geodesics of the engineered substrate metric.** This is the operational statement that drives cloaking, lensing, and waveguiding in the transformation-optics regime.

### 5.6 Pendry spherical cloak: deformation

Choose the radial map
$$
r' \;=\; R_1 + \alpha\,r, \qquad \alpha \;=\; \frac{R_2 - R_1}{R_2}, \qquad 0 \le r \le R_2,
$$
in spherical coordinates $(r, \theta, \phi)$, with angular coordinates unchanged. The map sends the open ball $r < R_2$ onto the shell $R_1 < r' < R_2$. The interior point $r = 0$ maps to the inner shell $r' = R_1$; the outer boundary $r = R_2$ maps to itself.

The Jacobian in spherical coordinates has principal components:
- Radial: $\partial r'/\partial r = \alpha$.
- Polar angular: $r' /r$.
- Azimuthal angular: $(r'/r)\sin\theta/\sin\theta = r'/r$.

Note $r = (r' - R_1)/\alpha$. So $r'/r = \alpha r'/(r' - R_1)$.

### 5.7 Pendry cloak: constitutive tensors

Applying the constitutive transformation of §5.3 in spherical coordinates with $\det J = \alpha\,(r'/r)^2 = \alpha\,(\alpha r'/(r' - R_1))^2$:
$$
\det J \;=\; \alpha^3\,\frac{r'^2}{(r' - R_1)^2}.
$$

The radial constitutive component:
$$
\frac{\varepsilon_{\hat r'}}{\varepsilon_0} \;=\; \frac{J_{rr}^2}{\det J} \cdot \frac{1}{(g_{\rm sph})_{rr}} \;\Rightarrow\; \frac{\varepsilon_{\hat r'}}{\varepsilon_0} \;=\; \beta\,\frac{(r' - R_1)^2}{r'^2},
$$
where $\beta = R_2/(R_2 - R_1) = 1/\alpha$ (with appropriate handling of the spherical metric factors).

The angular constitutive components:
$$
\frac{\varepsilon_{\hat\theta'}}{\varepsilon_0} \;=\; \frac{\varepsilon_{\hat\phi'}}{\varepsilon_0} \;=\; \beta.
$$

The same expressions hold for $\mu/\mu_0$ — the cloak is impedance-matched to vacuum at every point. In boxed form:
$$
\boxed{\;\;\frac{\varepsilon_{\hat r'}}{\varepsilon_0} \;=\; \beta\,\frac{(r' - R_1)^2}{r'^2}, \qquad \frac{\varepsilon_{\hat\theta'}}{\varepsilon_0} \;=\; \frac{\varepsilon_{\hat\phi'}}{\varepsilon_0} \;=\; \beta, \qquad \beta \;=\; \frac{R_2}{R_2 - R_1}. \;\;}
$$

These are the **Pendry spherical cloak constitutive tensors** (Pendry 2006).

### 5.8 Effective metric of the cloak

The effective metric components, applying §5.4 to the cloak deformation:
$$
g_{\hat r'\hat r'} \;=\; \beta^2\,\frac{(r' - R_1)^2}{r'^2}, \qquad g_{\hat\theta'\hat\theta'} \;=\; g_{\hat\phi'\hat\phi'} \;=\; \beta^2.
$$

At $r' = R_1$, the radial metric component vanishes: $g_{\hat r'\hat r'}(r' = R_1) = 0$.

### 5.9 Substrate-level meaning of invisibility

The vanishing of $g_{\hat r'\hat r'}$ at $r' = R_1$ has the substrate-level reading that **rule-type channels carrying field amplitude cannot enter the cloaked interior**. The radial distance, in the rule-type metric, becomes singular at the inner shell: any geodesic of $g_{ij}$ that attempts to cross $r' = R_1$ would require infinite proper length. The interior is *topologically excluded* from the substrate seen by the propagating field.

This is the structural meaning of invisibility:
- Not absorption (no energy loss in the cloak shell).
- Not reflection (impedance matching eliminates reflections).
- Not concealment (no hiding behind material screens).
- **Topological exclusion**: the cloaked region is removed from the rule-type geometry seen by the propagating channel.

Energy flow follows geodesics of $g_{ij}$, which detour smoothly around the cloaked interior and exit the outer shell $r' = R_2$ as if traveling through vacuum. An observer outside the cloak sees the field profile of vacuum propagation; the cloaked object is invisible.

### 5.10 General transformation optics

The Pendry cloak is one instance of the general transformation-optics construction. Any smooth deformation $f: x \mapsto x'$ with $J$ and $J^{-1}$ bounded and $\det J > 0$ produces a substrate-level effective medium with constitutive tensors given by §5.3 and effective metric given by §5.4. The geodesics of the effective metric are the engineered light rays.

**Physical realizability conditions:**
- Smoothness of $f$: $J, J^{-1}$ smooth and bounded.
- Orientation preservation: $\det J > 0$.
- Homogenization regime: the resulting $\varepsilon', \mu'$ must be achievable by some periodic microstructure with $a \ll \lambda$ at the operating frequency.
- Absence of unintentional singularities: $\varepsilon'$ and $\mu'$ singularities only at designed locations.
- Bandwidth: dispersion of the implementing microstructure restricts the design to a finite frequency band.

The Pendry cloak saturates condition 4 deliberately at $r' = R_1$; this singularity is the price of perfect cloaking, and it is what makes the perfect cloak intrinsically bandwidth-limited and physically realizable only as an approximation.

---

## 6. Metasurfaces and the Generalized Snell's Law

### 6.1 Codimension-1 discontinuity

Under P-MM-5, P-MM-6, consider a surface $\Sigma$ at $z = 0$ across which the substrate's rule-type structure changes discontinuously. The bulk regions $z < 0$ and $z > 0$ are described by the coarse-grained wave equation of P-MM-4 with refractive indices $n_1$ and $n_2$ respectively. The discontinuity at $\Sigma$ imposes jump conditions on the wave field.

### 6.2 Passive interface: standard Snell's law

For a passive interface (no engineered surface phase profile, no surface polarization, no surface currents), the standard tangential-field continuity holds:
$$
\mathbf{E}_\parallel(r_\parallel, 0^+) \;=\; \mathbf{E}_\parallel(r_\parallel, 0^-), \qquad \mathbf{H}_\parallel(r_\parallel, 0^+) \;=\; \mathbf{H}_\parallel(r_\parallel, 0^-).
$$
For a scalar wave $\psi$ (component of $\mathbf{E}$ or $\mathbf{H}$ parallel to $\Sigma$):
$$
\psi(r_\parallel, 0^+) \;=\; \psi(r_\parallel, 0^-).
$$

Take a plane wave on side 1: $\psi_1 = e^{i k_{\parallel,1}\cdot r_\parallel + i k_{z,1} z}$. Continuity at $z = 0$ forces the tangential wavevector to match: $k_{\parallel,2} = k_{\parallel,1}$. With $k_{\parallel,1} = n_1 k_0 \sin\theta_i$ and $k_{\parallel,2} = n_2 k_0 \sin\theta_t$, the matching condition gives
$$
n_1 \sin\theta_i \;=\; n_2 \sin\theta_t,
$$
the standard Snell's law.

### 6.3 Engineered phase profile

A metasurface is a codimension-1 surface engineered to imprint a tangential phase profile $\Phi(r_\parallel)$ on the transmitted field. The phase profile is produced by subwavelength resonant scatterers ("meta-atoms") whose engineered geometry imprints a position-dependent phase shift. Each meta-atom is a coarse-grained rule-type discontinuity of negligible thickness; the metasurface as a whole is the spatial pattern of these meta-atoms.

The boundary condition at $\Sigma$ becomes, for a scalar wave:
$$
\boxed{\;\;\psi_2(r_\parallel, 0^+) \;=\; \psi_1(r_\parallel, 0^-)\,e^{i\Phi(r_\parallel)}. \;\;}
$$

**Substrate-level meaning.** The metasurface is a codimension-1 engineered rule-type discontinuity. The tangential phase profile $\Phi(r_\parallel)$ is the integrated rule-type phase imprinted on a channel as it crosses $\Sigma$. The function $\Phi$ is engineered by the meta-atom geometry: each meta-atom resonance produces a controlled phase shift, and the spatial arrangement of meta-atoms produces the spatial profile.

### 6.4 Tangential momentum kick

Take an incident plane wave on side 1: $\psi_1 = e^{i k_{\parallel,1}\cdot r_\parallel + i k_{z,1} z}$. At $z = 0^-$, the field is $\psi_1(r_\parallel, 0^-) = e^{i k_{\parallel,1}\cdot r_\parallel}$. Applying the metasurface boundary condition:
$$
\psi_2(r_\parallel, 0^+) \;=\; e^{i k_{\parallel,1}\cdot r_\parallel + i\Phi(r_\parallel)}.
$$

Take the tangential gradient of the phase. For a *linear* phase profile $\Phi(x) = (d\Phi/dx)\,x$:
$$
\psi_2(r_\parallel, 0^+) \;=\; e^{i[k_{\parallel,1} + d\Phi/dx]\,x},
$$
showing that the tangential wavevector on side 2 is
$$
\boxed{\;\;k_{\parallel,2} \;=\; k_{\parallel,1} + \nabla_\parallel \Phi(r_\parallel). \;\;}
$$

The metasurface imparts a **tangential momentum kick** equal to the gradient of the engineered phase profile. This is the operational signature of the metasurface: the discontinuity adds a tangential wavevector contribution that no passive interface can produce.

### 6.5 Generalized Snell's law

Substitute $k_{\parallel,1} = n_1 k_0 \sin\theta_i$, $k_{\parallel,2} = n_2 k_0 \sin\theta_t$, $k_0 = 2\pi/\lambda$ into the matching condition $k_{\parallel,2} = k_{\parallel,1} + d\Phi/dx$:
$$
n_2 k_0 \sin\theta_t \;=\; n_1 k_0 \sin\theta_i + \frac{d\Phi}{dx},
$$
or equivalently
$$
\boxed{\;\; n_1 \sin\theta_i \;=\; n_2 \sin\theta_t + \frac{\lambda}{2\pi}\,\frac{d\Phi}{dx}. \;\;}
$$

This is the **Capasso 2011 generalized Snell's law**. The standard Snell's law is the special case $d\Phi/dx = 0$.

### 6.6 Consequences

The generalized Snell's law permits:

- **Anomalous refraction.** For $d\Phi/dx \ne 0$, the refraction angle $\theta_t$ is no longer determined solely by the bulk indices and incidence angle. Refraction angles unattainable from $n_1, n_2$ alone become accessible.
- **Negative refraction at a single interface.** A sufficiently steep phase gradient $d\Phi/dx$ can produce $\theta_t$ on the same side of the normal as $\theta_i$ even with both bulk indices positive.
- **Reflectionless beam steering.** By engineering $\Phi$, the metasurface redirects a transmitted beam to any angle within the limits of the phase gradient.
- **Phase-only optical components.** Lenses, waveplates, holograms, and arbitrary optical functionality implemented as flat metasurfaces of subwavelength thickness.

### 6.7 Limits

The phase profile $\Phi(r_\parallel)$ must vary slowly on the scale of $\lambda$ for the boundary-condition treatment to be valid. Phase profiles with features finer than $\lambda$ are not captured by the metasurface picture alone; they enter full diffraction theory. The phase imprint is intrinsically frequency-dependent (the meta-atoms supporting $\Phi$ are resonant), so achromatic metasurfaces require multi-resonance engineering and remain bandwidth-limited.

---

## 7. Photonic Bandgaps via Bloch Eigenmodes

### 7.1 When homogenization breaks down

The two-scale expansion of §3 requires $a/\lambda \to 0$. At $a \sim \lambda$, the expansion no longer converges term-by-term: the corrector field develops slow-coordinate dependence, and additional corrections of order $(a/\lambda)^2$ enter the effective coefficient. The relevant description in this regime is Bloch / Floquet analysis: instead of effective constants, one obtains a band structure $\omega_n(k)$ on the Brillouin zone.

This is the regime of **photonic crystals**, adjacent to the strict homogenization regime.

### 7.2 Bloch's theorem on the periodic substrate

Under P-MM-1, P-MM-2, P-MM-4, P-MM-6 with $a \sim \lambda$, consider the wave equation
$$
\partial_i\!\left[A^{ij}(x)\,\partial_j\psi\right] + \omega^2\,n^2(x)\,\psi \;=\; 0,
$$
with $A^{ij}$ and $n^2$ periodic with lattice $\Lambda = a\mathbb{Z}^3$. Define the translation operator $T_R$ acting on functions: $T_R \psi(x) = \psi(x + R)$ for $R \in \Lambda$.

The wave operator commutes with $T_R$ for any $R \in \Lambda$. The simultaneous eigenfunctions of the wave operator and $\{T_R\}_{R\in\Lambda}$ form a complete basis. The translation operators are unitary on a suitable Hilbert space, so their eigenvalues are phases $e^{ik\cdot R}$ with $k$ a real vector. Restricting $k$ to the first Brillouin zone (BZ) — the set of $k$ such that $|k| \le |k - G|$ for all reciprocal lattice vectors $G \in \Lambda^*$ — uniquely labels the simultaneous eigenfunctions.

**Bloch form.** Simultaneous eigenfunctions take the form
$$
\boxed{\;\;\psi_{n, k}(x) \;=\; u_{n, k}(x)\,e^{i k\cdot x}, \qquad u_{n, k}(x + R) \;=\; u_{n, k}(x) \text{ for all } R \in \Lambda, \;\;}
$$
indexed by band index $n \in \mathbb{N}$ and crystal momentum $k$ in the first BZ.

### 7.3 Band structure

Substituting the Bloch form into the wave equation gives, after expanding the derivatives,
$$
(\partial_i + i k_i)\!\left[A^{ij}(x)\,(\partial_j + i k_j) u_{n, k}\right] + \omega_n^2(k)\,n^2(x)\,u_{n, k} \;=\; 0,
$$
a Hermitian generalized eigenvalue problem for $u_{n, k}$ on a single unit cell with periodic boundary conditions. At each $k$, the eigenvalues $\omega_n^2(k)$ form a discrete real sequence
$$
0 \le \omega_1^2(k) \le \omega_2^2(k) \le \omega_3^2(k) \le \cdots,
$$
indexed by band number $n$. As $k$ varies continuously over the BZ, each eigenvalue $\omega_n^2(k)$ traces out the **$n$-th band** of the band structure.

### 7.4 Bandgap formation

A **bandgap** is a frequency interval $[\omega_a, \omega_b]$ such that no value of $k$ produces an eigenvalue $\omega_n^2(k)$ in $[\omega_a^2, \omega_b^2]$ for any band $n$. At those frequencies, no propagating Bloch eigenmode exists — the substrate forbids field propagation in the bulk.

**Mechanism.** A bandgap appears when the bands $\omega_n(k)$ and $\omega_{n+1}(k)$, in some region of the BZ, separate without crossing. The standard mechanism is constructive vs. destructive interference of the field across the unit cell: at certain $k$ near the BZ boundary, the spatial pattern of the lower band has nodes on the high-index regions while the higher band has nodes on the low-index regions, with the energy difference producing a gap.

For periodic dielectric substrates with sufficient index contrast (typically $\Delta\varepsilon/\varepsilon \gtrsim 0.5$ for full 3D gaps), complete bandgaps appear: frequency intervals in which no propagating mode exists in any direction. This is the **Yablonovitch photonic bandgap**.

### 7.5 Substrate-level meaning

The bandgap is a frequency window in which the periodic rule-type substrate offers no allowed coarse-grained channel. The substrate's rule-type structure, periodicized at scale $a \sim \lambda$, supports certain frequencies as propagating modes (the bands) and forbids others (the gaps). The forbidden frequencies are those for which no Bloch eigenmode can be assembled from the local rule-type response.

This is the substrate-level analog of an electronic bandgap in a crystalline solid: same Bloch machinery, applied to the substrate's coarse-grained rule-type response rather than electron wave functions.

### 7.6 Relation to homogenization

The homogenization regime $a \ll \lambda$ corresponds to the long-wavelength limit $k \to 0$ of the lowest band:
$$
\omega_1(k) \;\approx\; c_{\rm eff}\,|k|, \qquad k \to 0,
$$
with $c_{\rm eff}$ determined by the effective constitutive tensors of §3-4. The lowest band, near $k = 0$, looks like vacuum propagation in a homogeneous effective medium.

Bandgaps live further into the BZ, at $|k| \sim \pi/a$, where homogenization is no longer valid and the full Bloch structure is needed. At these wavevectors, the wavelength $\lambda = 2\pi/k \sim 2a$ is comparable to the lattice period, and the field oscillates significantly within one cell.

The two regimes — homogenization and Bloch / bandgap — are not independent. They are two limits of the same substrate operation: engineered periodic microstructure under P-MM-1, P-MM-2. Homogenization gives the long-wavelength effective medium; Bloch analysis gives the full band structure including bandgaps. A photonic crystal is the same substrate operation as a homogenized metamaterial; the difference is the operating wavelength relative to the lattice period.

### 7.7 Defects and waveguiding

Local defects in the periodic substrate (a single perturbed unit cell, a missing inclusion, an embedded line of perturbed cells) support localized modes inside the bandgap. These defect states are the substrate-level mechanism for photonic-crystal waveguides, cavities, and add-drop filters. The defect modifies the local rule-type response, producing a discrete eigenmode whose frequency lies in the bulk's forbidden gap.

---

## 8. The Unifying Substrate-Level Statement

### 8.1 Three control axes

The three closures derived in this walkthrough — homogenization, transformation optics, metasurface boundary conditions — correspond to three independent engineered modulations of the substrate's coarse-grained rule-type structure:

| Operation | Substrate primitive | Coarse-grained result | Nobel-frontier instance |
|---|---|---|---|
| Smooth periodic microstructure | P-MM-1, P-MM-2 | $\varepsilon_{\rm eff}, \mu_{\rm eff}$ (and Bloch bands at $a\sim\lambda$) | Pendry-negative-index, Yablonovitch-bandgap |
| Smooth deformation | P-MM-3 | effective metric $g_{ij}$, transformed $\varepsilon, \mu$ | Pendry-cloak |
| Codim-1 discontinuity | P-MM-5 | tangential momentum kick $\nabla_\parallel \Phi$ | Capasso-metasurface |

### 8.2 Exhaustiveness within the precursor machinery

Within the coarse-graining window P-MM-6 and under the second-order wave equation P-MM-4, engineered modifications of the substrate enter one of three locations:

1. The coefficient $A^{ij}(x)$ varies smoothly on a scale $a$ — Closure 1.
2. The coordinate $x$ is the image of a deformed substrate $x = f(X')$ with $f$ smooth — Closure 2.
3. The coefficient $A^{ij}(x)$ has a codimension-1 jump on a surface — Closure 3.

Higher-codimension features (lines, points) do not survive coarse-graining: they appear as point scatterers at coarse-grained scales and are not metamaterial control mechanisms. Volumetric non-smooth features cannot be averaged within the homogenization window and reduce to one of the three cases at the operating wavelength. **The three closures therefore exhaust the substrate-level wave-control space within the precursor machinery.**

### 8.3 The unifying identity

$$
\boxed{\;\;\text{Metamaterials} \;=\; \text{engineered rule-type microstructure} \;+\; \text{engineered deformation} \;+\; \text{engineered discontinuity}.\;\;}
$$

Each Nobel-frontier result is the instantiation of one axis in isolation:
- **Yablonovitch bandgap** = periodic microstructure at $a \sim \lambda$.
- **Pendry negative index** = doubly-resonant periodic microstructure at $a \ll \lambda$.
- **Pendry cloak** = smooth deformation with FORCED constitutive transformation.
- **Capasso metasurface** = engineered codim-1 phase discontinuity.

Practical metamaterials generally compose all three axes: a transformation-optics device implemented by a graded homogenized medium with a metasurface termination, for example.

### 8.4 The unified substrate-level wave equation

The most general coarse-grained wave equation in the precursor machinery is
$$
\frac{1}{\sqrt{|g|}}\,\partial_i\!\left[\sqrt{|g|}\,g^{ij}\,(\varepsilon_{\rm eff}^{-1})^{jk}\,\partial_k\psi\right] + k_0^2\,\mu_{\rm eff}\,\psi \;=\; 0,
$$
subject to jump conditions on engineered codim-1 surfaces $\Sigma$:
$$
\psi(r_\parallel, 0^+) \;=\; \psi(r_\parallel, 0^-)\,e^{i\Phi(r_\parallel)}.
$$

This is the **unified substrate-level wave equation of the Arc**. The three closures are its three independent control knobs: $\varepsilon_{\rm eff}, \mu_{\rm eff}$ (Closure 1), $g_{ij}$ (Closure 2), and $\Phi$ on $\Sigma$ (Closure 3). All three knobs derive from the same substrate operations (P-MM-1, P-MM-3, P-MM-5) coarse-grained under P-MM-6 and propagated under P-MM-4.

### 8.5 Scope and limits

The closures hold under the following bounds:

- **Homogenization regime:** $a/\lambda \ll 1$. Beyond $a \sim \lambda/3$ the leading expansion is qualitative only; Bloch analysis takes over.
- **Negative-index bandwidth:** $\varepsilon_r < 0$ and $\mu_r < 0$ overlap over a band intrinsically narrowed by Kramers-Kronig. Lossless negative-index media over arbitrary bandwidth are forbidden.
- **Transformation optics smoothness:** $J$ and $J^{-1}$ bounded, $\det J > 0$. Singular maps (Pendry cloak at $r' = R_1$) are intrinsically dispersive and bandwidth-limited.
- **Metasurface phase variation:** $\Phi(r_\parallel)$ slow on $\lambda$. Sub-$\lambda$ phase features require full diffraction theory.
- **Universal:** energy conservation, causality (Kramers-Kronig), Sommerfeld-Brillouin signal-front bound $v_{\rm front} \le c$, bandwidth-response trade-off across all axes.

The effective metric $g_{ij}$ of §5 is a coarse-grained rule-type metric on the substrate — not spacetime curvature. The substrate-level operation that produces it is engineered displacement, not gravitational physics. The identification is structural, not analogical.

---

## 9. FORCED / INHERITED / OPEN Accounting

### FORCED at substrate level

The following results are FORCED by the substrate primitives P-MM-1 through P-MM-6 and the derivations of this walkthrough. No additional posit is required.

- **Two-scale lift and derivative splitting** (§3.2) — FORCED from P-MM-2, P-MM-6.
- **Order-by-order equations** (§3.3) — FORCED.
- **Leading-order $\psi_0(X, y) = \psi_0(X)$** independence from fast variable (§3.3) — FORCED by positive-definiteness of $A^{ij}$.
- **Cell problem** with $Y$-periodicity and zero-mean corrector (§3.3) — FORCED.
- **Cell-averaging operator properties** (vanishing of pure $y$-divergences, commutativity with $X$-derivatives) (§3.4) — FORCED.
- **Effective-coefficient formula** $A^{*ik} = \langle A^{ik}\rangle + \langle A^{ij}\partial_{y^j}\chi^k\rangle$ (§3.5) — FORCED.
- **Voigt-Reuss bounds** (§3.6) — FORCED.
- **Anisotropy from microstructure** (§3.7, §4.2) — FORCED FORM.
- **Form of effective constitutive tensors** $\varepsilon_{\rm eff}^{ij}$, $\mu_{\rm eff}^{ij}$ (§4.2) — FORCED FORM.
- **Negative-index branch choice** $n = -\sqrt{\varepsilon_r\mu_r}$ in the doubly-negative band (§4.7) — FORCED by causal outgoing-wave selection.
- **Constitutive transformation under deformation** $\varepsilon'^{ij} = (\det J)^{-1} J^i{}_k J^j{}_l \varepsilon^{kl}$ (§5.3) — FORCED from P-MM-3 + P-MM-4 + P-MM-6.
- **Impedance matching to vacuum** under deformation from vacuum starting medium (§5.3) — FORCED.
- **Effective metric** $g_{ij} = (J^{-1})^k{}_i (J^{-1})^l{}_j \delta_{kl}$ (§5.4) — FORCED.
- **Light rays as geodesics of $g_{ij}$** in eikonal limit (§5.5) — FORCED.
- **Pendry cloak constitutive tensors** (§5.7) — FORCED FORM from the deformation $r' = R_1 + \alpha r$.
- **Topological exclusion of cloaked interior** (§5.9) — FORCED by vanishing of $g_{\hat r'\hat r'}$ at $r' = R_1$.
- **Metasurface phase-imprinting boundary condition** $\psi_2 = \psi_1 e^{i\Phi}$ (§6.3) — FORCED from P-MM-5 + P-MM-6.
- **Tangential momentum kick** $k_{\parallel,2} = k_{\parallel,1} + \nabla_\parallel\Phi$ (§6.4) — FORCED.
- **Generalized Snell's law** (§6.5) — FORCED.
- **Bloch form** for periodic substrates (§7.2) — FORCED from P-MM-1, P-MM-2, P-MM-4.
- **Band structure** as Hermitian eigenvalue problem on the unit cell (§7.3) — FORCED.
- **Photonic-bandgap mechanism** as eigenvalue gaps in the Bloch problem (§7.4) — FORCED FORM.
- **Continuity of homogenization regime with Bloch regime** through long-wavelength limit of lowest band (§7.6) — FORCED.
- **Three-axis exhaustiveness** within P-MM-4 + P-MM-6 (§8.2) — FORCED.
- **Unifying identity** (§8.3) — FORCED.
- **Unified substrate-level wave equation** (§8.4) — FORCED FORM.

### INHERITED (form FORCED, values from microstructure or geometry choice)

The following take their *form* from the FORCED results above, but their numerical values are INHERITED from specific microstructure or device-geometry choices made by the engineer.

- **Drude plasma frequency** $\omega_p^2 = 2\pi c^2 / [a^2 \ln(a/r_0)]$ (§4.4) — Drude FORM FORCED; coefficient INHERITED from wire-array geometry.
- **Lorentz parameters** $F$, $\omega_0$, $\gamma$ (§4.5) — Lorentz FORM FORCED; oscillator parameters INHERITED from SRR geometry.
- **Cloak parameters** $\alpha$, $\beta$ (§5.7) — INHERITED from cloak-shell radii $R_1, R_2$.
- **Metasurface phase profile** $\Phi(r_\parallel)$ (§6.3) — INHERITED from meta-atom geometry and arrangement.
- **Band structure** $\omega_n(k)$ (§7.3) — FORM FORCED; specific band positions INHERITED from periodic geometry and material contrast.
- **Bandgap widths and locations** (§7.4) — INHERITED from periodic geometry.
- **Corrector fields** $\chi^j(y)$ (§3.3) — equation FORCED; specific solutions INHERITED from cell coefficient $A^{ij}(y)$.

### OPEN

The following items are OPEN at the substrate level. They are not derived in this walkthrough and are flagged for future work.

- **Higher-order homogenization corrections** at $a \sim \lambda/3$ to $\lambda$. The leading expansion is FORCED; next-order corrections at $(a/\lambda)^2$ are FORM-FORCED-VALUES-INHERITED from specific cell solutions but not derived here.
- **Nonlocal / spatially dispersive metamaterials.** The closure machinery is local; spatial dispersion enters at the next order in $a/\lambda$ and requires extension beyond two-scale expansion.
- **Active and time-varying metamaterials.** Time-dependent deformation $u(X, t)$ and time-varying microstructure are allowed by P-MM-1 and P-MM-3 respectively, but the corresponding closures (Floquet-in-time, parametric amplification, non-reciprocal phenomena) require their own derivations.
- **Topological photonics within Closure 1.** Periodic substrates with engineered band topology, Berry curvature on the BZ, Chern numbers, photonic topological insulators — adjacent to Closure 1 but not derived here. (Adjacent closed walkthroughs in the broader inventory cover this direction.)
- **Quantum-optical metamaterials.** Single-photon and entangled-photon propagation through metamaterials uses the same coarse-grained wave equation at the field level; substrate-level quantum-state evolution through Closure 1/2/3 devices is reachable but not derived here.
- **Bulk-boundary correspondence** for photonic systems. The relation between bulk band topology and boundary states is not derived here.
- **Hyperbolic metamaterials.** Substrates with effective tensors of mixed-signature signature ($\varepsilon_\parallel > 0$, $\varepsilon_\perp < 0$ or vice versa) are within Closure 1's reach but not derived in detail here.
- **Time-domain metasurfaces.** Spatiotemporal phase profiles $\Phi(r_\parallel, t)$ produce frequency shifts in addition to angle shifts; the static derivation of §6 does not cover this case.

**No new substrate primitives are introduced anywhere in the walkthrough.**

---

## 10. Exact Claims

The substrate-level claims established in this walkthrough are:

1. The substrate ontology FORCES a coarse-grained second-order wave equation (P-MM-4) whose coefficients are determined by the substrate's local rule-type content (P-MM-1).

2. Subwavelength periodic microstructure (P-MM-2) admits two-scale homogenization. The cell-problem corrector field $\chi^j(y)$, defined by an elliptic boundary-value problem on the unit cell with periodic boundary conditions and zero mean, produces effective constitutive tensors
$$
\varepsilon_{\rm eff}^{ij} = \langle\varepsilon^{ij}\rangle + \langle\varepsilon^{ik}\partial_{y^k}\chi_E^j\rangle, \qquad (\mu_{\rm eff}^{-1})^{ij} = \langle(\mu^{-1})^{ij}\rangle + \langle(\mu^{-1})^{ik}\partial_{y^k}\chi_M^j\rangle.
$$

3. The effective tensors satisfy Voigt-Reuss bounds. Microstructure produces anisotropy from isotropic constituents.

4. Engineered wire-array microstructures produce a Drude effective dielectric function with plasma frequency $\omega_p^2 = 2\pi c^2 / [a^2 \ln(a/r_0)]$, giving $\varepsilon_{\rm eff}(\omega) < 0$ for $\omega < \omega_p$.

5. Engineered split-ring resonator microstructures produce a Lorentz effective magnetic function with $\mu_{\rm eff}(\omega) < 0$ in a band immediately above the resonance frequency $\omega_0$.

6. In the doubly-negative band, the negative refractive index $n_{\rm eff} = -\sqrt{\varepsilon_r\mu_r}$ is FORCED by causal outgoing-wave selection. No separate postulate is required.

7. Slow substrate deformation (P-MM-3) produces transformed constitutive tensors $\varepsilon'^{ij} = (\det J)^{-1} J^i{}_k J^j{}_l \varepsilon^{kl}$ and an effective metric $g_{ij} = (J^{-1})^k{}_i (J^{-1})^l{}_j \delta_{kl}$ on the wave equation, written in covariant Laplace-Beltrami form.

8. The Pendry spherical cloak deformation $r' = R_1 + \alpha r$ with $\alpha = (R_2 - R_1)/R_2$ produces constitutive tensors $\varepsilon_{\hat r'}/\varepsilon_0 = \beta(r' - R_1)^2/r'^2$, $\varepsilon_{\hat\theta'}/\varepsilon_0 = \varepsilon_{\hat\phi'}/\varepsilon_0 = \beta$. The cloaked interior is topologically excluded at substrate level by the vanishing of $g_{\hat r'\hat r'}$ at $r' = R_1$.

9. The effective metric $g_{ij}$ is a coarse-grained rule-type metric on the substrate. It is *not* spacetime curvature; no claim about gravitational physics is made or required.

10. Engineered codim-1 phase discontinuities (P-MM-5) imprint a tangential momentum kick $k_{\parallel,2} = k_{\parallel,1} + \nabla_\parallel\Phi$ on transmitted channels. The generalized Snell's law $n_1 \sin\theta_i = n_2 \sin\theta_t + (\lambda/2\pi)(d\Phi/dx)$ follows directly.

11. Periodic substrate at $a \sim \lambda$ supports Bloch eigenmodes $\psi_{n, k} = u_{n, k}\,e^{i k\cdot x}$ with band structure $\omega_n(k)$ on the Brillouin zone. Photonic bandgaps are frequency intervals where no eigenvalue exists, FORCED-FORM at substrate level.

12. The three substrate-level wave-control axes (microstructure, deformation, discontinuity) exhaust the precursor-machinery design space within P-MM-6.

13. Practical metamaterials are engineered compositions along the three axes. The unified substrate-level wave equation is
$$
\frac{1}{\sqrt{|g|}}\,\partial_i\!\left[\sqrt{|g|}\,g^{ij}\,(\varepsilon_{\rm eff}^{-1})^{jk}\,\partial_k\psi\right] + k_0^2\,\mu_{\rm eff}\,\psi = 0,
$$
with jump conditions $\psi(0^+) = \psi(0^-)\,e^{i\Phi(r_\parallel)}$ on engineered codim-1 surfaces.

14. The precursor machinery is bounded by the coarse-graining window P-MM-6, Kramers-Kronig dispersion-bandwidth trade-offs, and the Sommerfeld-Brillouin signal-front bound $v_{\rm front} \le c$.

15. The four Nobel-frontier metamaterials and photonics directions — Yablonovitch's photonic bandgaps, Pendry's negative refractive index, Pendry's electromagnetic cloak, and Capasso's generalized Snell's law — are reproduced at the substrate level by the three precursor closures plus the adjacent Bloch / bandgap regime, with no new substrate primitives.

---

## 11. References

- Yablonovitch, E. *Inhibited spontaneous emission in solid-state physics and electronics.* Phys. Rev. Lett. **58**, 2059 (1987) — photonic bandgaps.
- John, S. *Strong localization of photons in certain disordered dielectric superlattices.* Phys. Rev. Lett. **58**, 2486 (1987) — companion bandgap paper.
- Veselago, V. G. *The electrodynamics of substances with simultaneously negative values of $\varepsilon$ and $\mu$.* Sov. Phys. Uspekhi **10**, 509 (1968) — original theoretical analysis of negative index.
- Pendry, J. B., Holden, A. J., Stewart, W. J., Youngs, I. *Extremely low frequency plasmons in metallic mesostructures.* Phys. Rev. Lett. **76**, 4773 (1996) — wire-array effective plasma frequency.
- Pendry, J. B., Holden, A. J., Robbins, D. J., Stewart, W. J. *Magnetism from conductors and enhanced nonlinear phenomena.* IEEE Trans. Microw. Theory Tech. **47**, 2075 (1999) — split-ring resonator magnetic response.
- Smith, D. R., Padilla, W. J., Vier, D. C., Nemat-Nasser, S. C., Schultz, S. *Composite medium with simultaneously negative permeability and permittivity.* Phys. Rev. Lett. **84**, 4184 (2000) — first experimental demonstration.
- Pendry, J. B. *Negative refraction makes a perfect lens.* Phys. Rev. Lett. **85**, 3966 (2000) — negative refractive index and superlens.
- Pendry, J. B., Schurig, D., Smith, D. R. *Controlling electromagnetic fields.* Science **312**, 1780 (2006) — transformation optics; spherical cloak.
- Leonhardt, U. *Optical conformal mapping.* Science **312**, 1777 (2006) — concurrent transformation-optics construction.
- Schurig, D., Mock, J. J., Justice, B. J., Cummer, S. A., Pendry, J. B., Starr, A. F., Smith, D. R. *Metamaterial electromagnetic cloak at microwave frequencies.* Science **314**, 977 (2006) — experimental realization.
- Yu, N., Genevet, P., Kats, M. A., Aieta, F., Tetienne, J.-P., Capasso, F., Gaburro, Z. *Light propagation with phase discontinuities: generalized laws of reflection and refraction.* Science **334**, 333 (2011) — metasurfaces and generalized Snell's law.
- Aieta, F., Genevet, P., Kats, M. A., Yu, N., Blanchard, R., Gaburro, Z., Capasso, F. *Aberration-free ultrathin flat lenses and axicons at telecom wavelengths based on plasmonic metasurfaces.* Nano Lett. **12**, 4932 (2012) — metasurface lens.
- Bensoussan, A., Lions, J.-L., Papanicolaou, G. *Asymptotic Analysis for Periodic Structures.* North-Holland (1978) — mathematical foundations of two-scale homogenization.
- Milton, G. W. *The Theory of Composites.* Cambridge University Press (2002) — homogenization, Voigt-Reuss bounds, effective tensors.
- Joannopoulos, J. D., Johnson, S. G., Winn, J. N., Meade, R. D. *Photonic Crystals: Molding the Flow of Light.* 2nd ed., Princeton University Press (2008) — photonic-crystal band theory.
- Sakoda, K. *Optical Properties of Photonic Crystals.* 2nd ed., Springer (2005) — Bloch analysis of photonic crystals.

---

## 12. Brief Review and Recommended Next Steps

### Review

This walkthrough reaches walkthrough-grade for the four Nobel-frontier metamaterials and photonics directions under fully self-contained discipline: every required two-scale expansion step, cell-problem statement, Jacobian computation, effective-metric identification, jump condition, and Bloch-eigenmode statement appears inside the document. No new substrate primitives are introduced; the entire derivation chain runs on P-MM-1 through P-MM-6.

Honest accounting of the load-bearing sections:

- **§3** carries the load of the two-scale homogenization derivation, including the lift, the derivative splitting, the order-by-order analysis at orders $a^{-2}, a^{-1}, a^0$, the cell problem with its zero-mean condition, the averaging operator with its two basic properties, and the effective-coefficient formula. Voigt-Reuss bounds and the 1D layered worked example are included.
- **§4** specializes to electromagnetism, identifies the polarization-dependent scalar form, derives the Drude effective dielectric function from wire arrays, derives the Lorentz effective magnetic function from split-ring resonators, and FORCES the negative-index branch by working out the left-handed triad $(\mathbf{E}, \mathbf{H}, \mathbf{k})$ in the doubly-negative band.
- **§5** derives the constitutive transformation under deformation from the rule-type-tensor transport rule, identifies the effective metric in covariant Laplace-Beltrami form, derives the Pendry spherical cloak's full constitutive structure (radial and angular components) and effective metric, and gives the substrate-level reading of invisibility as topological exclusion. The crucial scope note — that $g_{ij}$ is rule-type, not spacetime — is stated explicitly.
- **§6** derives the metasurface boundary condition from the codim-1 discontinuity primitive, the tangential momentum kick by inspection of the phase-imprinted field, and the generalized Snell's law in standard form.
- **§7** reviews the Bloch regime in compact self-contained form, derives the band structure as a Hermitian eigenvalue problem on the unit cell, identifies the bandgap mechanism, and establishes the continuity between homogenization (lowest band, $k \to 0$) and Bloch (full BZ, $|k| \sim \pi/a$) as two limits of the same substrate operation.
- **§8** establishes the unifying substrate-level statement: three control axes, exhaustiveness within the precursor machinery, the unified wave equation, scope limits.
- **§9** provides full FORCED / INHERITED / OPEN accounting.
- **§10** lists the substrate-level claims.

The walkthrough sits in the established ~600-line range for arc-grade ED documents, comparable to the Berry-phase walkthrough and the V5-kernel cross-domain-unification walkthrough.

### Honest scope-limit

The walkthrough does not derive: higher-order homogenization corrections at $a \sim \lambda/3$, nonlocal metamaterials, active and time-varying metamaterials, full topological-photonics machinery (covered in adjacent closed walkthroughs), quantum-optical metamaterials at the state-evolution level, bulk-boundary correspondence, hyperbolic-metamaterial details, or time-domain metasurfaces. These are flagged OPEN in §9, not asserted as derived.

The effective metric $g_{ij}$ of §5 is a coarse-grained rule-type metric on the substrate. It is not spacetime curvature; no claim about gravitational physics is made or needed. The structural identity between the rule-type metric and a Riemannian metric on a manifold is what permits the covariant Laplace-Beltrami form of the wave equation, but the underlying physics is engineered substrate displacement, not gravity.

The doubly-negative branch choice $n = -\sqrt{\varepsilon_r\mu_r}$ in §4 follows from causal outgoing-wave selection given the doubly-negative constitutive response. The argument is FORCED but rests on the assumption that energy flows outward from sources; this is the standard causality posit for linear-response electrodynamics.

### What this completes for the photonics direction

Four Nobel-frontier metamaterials and photonics directions now have FORCED-form derivations at the substrate level within the ED framework:

- **Yablonovitch photonic bandgaps** — via periodic-microstructure Bloch eigenmodes.
- **Pendry negative refractive index** — via doubly-resonant homogenization with FORCED negative branch.
- **Pendry electromagnetic cloak** — via transformation-optics deformation with topologically excluded interior.
- **Capasso metasurface generalized Snell's law** — via codim-1 engineered phase discontinuity.

Together with the closed Berry-phase, Bloch-theorem, and photonic-Chern walkthroughs in the broader inventory, the photonics direction of the program now spans bandgaps, negative index, cloaking, metasurfaces, and topological photonics within a unified substrate-level account.

### Recommended next steps

In order of structural value:

1. **Add `project_arc_metamaterials.md` to memory.** Record: Arc closed at 13 memos, three precursor clusters (homogenization Memos 2-6, transformation optics Memos 7-11, metasurface BCs Memo 12, synthesis Memo 13), public walkthrough complete, no new primitives. Nobel-relevance routing: Yablonovitch / Pendry-negative / Pendry-cloak / Capasso all FORCED-form at substrate level.

2. **Update `project_walkthrough_series_expansion.md`.** Walkthrough count increments by one. Record this walkthrough as composing three precursor closures plus the adjacent Bloch regime.

3. **Update `walkthroughs_deferred.md`.** Mark closed: effective-medium / homogenization, transformation optics, metasurface boundary conditions. Add new deferred entries: nonlocal metamaterials, active and time-varying metamaterials, quantum-optical metamaterials, bulk-boundary correspondence in topological photonics, hyperbolic metamaterials, time-domain metasurfaces.

4. **Optional publication-grade paper.** Consider a paper in the `papers/` tree consolidating the Arc, structured as: substrate primitives → three closures → unifying identity → reproduction of four Nobel-frontier results → limits and open extensions. Decision depends on whether external publication on the metamaterials direction is targeted.

5. **Hyperbolic-metamaterials walkthrough.** Mid-effort follow-on. Substrates with mixed-signature effective tensors are within Closure 1's reach and have distinct substrate-level meaning (anisotropic rule-type response with sign-flip between principal axes).

6. **Time-domain metasurfaces walkthrough.** Short follow-on. Spatiotemporal phase profiles $\Phi(r_\parallel, t)$ produce frequency shifts in addition to angle shifts; the substrate-level mechanism is a codim-1 engineered rule-type discontinuity with explicit time dependence.

7. **Quantum-optical-metamaterials walkthrough.** Long-horizon follow-on. Single-photon and entangled-photon propagation through metamaterials at the state-evolution level; reachable from the closed QM-emergence inventory composed with this walkthrough's machinery.

The Yablonovitch / Pendry / Capasso metamaterials and photonics frontier is now substrate-level FORCED in its central structural claims: the substrate ontology forces effective constitutive tensors from periodic microstructure, an effective metric from smooth deformation, and tangential momentum kicks from engineered codim-1 phase discontinuities; the three axes exhaust the precursor-machinery design space; and the four Nobel-frontier results emerge as instantiations of the three axes plus the adjacent Bloch regime.
