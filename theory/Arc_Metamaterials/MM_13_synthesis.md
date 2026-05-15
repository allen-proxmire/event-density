# Memo 13 — Synthesis of the Three Precursor Closures

**Arc Metamaterials: Substrate-Level Effective Media, Transformation Optics, and Metasurface Boundary Conditions**

This memo concludes the precursor Arc by synthesizing the three closures (homogenization, transformation optics, metasurface boundary conditions) into a single substrate-level account of metamaterials and photonics. The memo is fully self-contained: all notation, primitives, and derivations needed to read this synthesis are restated inline. No new substrate primitives are introduced.

---

## 0. Notation and substrate primitives used in this memo

We work in three spatial dimensions with Cartesian coordinates $x = (x^1, x^2, x^3)$, time $t$, and a scalar or vector wave field $\psi(x, t)$. Where needed we specialize to electromagnetism with electric field $E^i$, magnetic field $H^i$, displacement $D^i = \varepsilon^{ij} E^j$, and induction $B^i = \mu^{ij} H^j$. The vacuum speed of light is $c$; the vacuum impedance is $Z_0 = \sqrt{\mu_0/\varepsilon_0}$; the wavenumber in vacuum is $k_0 = \omega/c$; the wavelength is $\lambda = 2\pi/k_0$. The substrate cutoff is the Planck length $\ell_P$.

Three length scales are relevant throughout:

- $\ell_P$ — substrate microscale (rule-type discreteness).
- $a$ — microstructure period (engineered).
- $\lambda$ — operating wavelength.
- $L$ — device scale.

The substrate primitives used (defined in Memo 1, restated here for self-containment):

- **P-MM-1 (Substrate rule-type microstructure):** the substrate carries rule-type structure at scale $\ell_P$; engineered inclusions at scales $a \gg \ell_P$ modulate this rule-type structure at coarse-grained scales.
- **P-MM-2 (Subwavelength periodicity):** when inclusions are arranged with period $a$ satisfying $a \ll \lambda$, the rule-type structure admits a two-scale description in slow coordinate $X = x$ and fast coordinate $y = x/a$ with $y$ on the unit cell $Y$.
- **P-MM-3 (ED-gradient deformation):** a slowly varying displacement field $u(X)$ acting on the substrate produces a coarse-grained deformation $x \mapsto x + u(X)$ whose Jacobian $J^i{}_j = \delta^i{}_j + \partial u^i / \partial X^j$ transports rule-type structure covariantly.
- **P-MM-4 (Channel propagation in structured media):** wave propagation in the coarse-grained substrate is governed by an effective second-order wave equation whose coefficients are determined by averaging over the microstructure.
- **P-MM-5 (Interface rule-type discontinuity):** a codimension-1 surface across which microstructure or deformation jumps imposes jump conditions on the coarse-grained wave field; engineered surface phase profiles $\Phi(r_\parallel)$ produce tangential momentum shifts.
- **P-MM-6 (Coarse-graining window):** all derivations operate in the window $\ell_P \ll a \ll \lambda \ll L$, where substrate discreteness is invisible, microstructure averaging is meaningful, and device-scale envelopes are slow.

These six primitives are the entire substrate vocabulary of the Arc.

---

## 1. Recap of the three closures (compact form)

We restate the load-bearing result of each closure in compact, self-contained form. The full derivations are in Memos 2–12.

### 1.1 Homogenization (Memos 2–6) — effective constitutive tensors

Under P-MM-1, P-MM-2, P-MM-4, P-MM-6, with microstructure period $a$ and $\lambda/a \to \infty$, the wave equation

$$
\partial_{x^i}\!\left[A^{ij}(x/a)\, \partial_{x^j} \psi \right] + k_0^2 n^2(x/a)\, \psi = 0
$$

with $Y$-periodic coefficient $A^{ij}(y)$ admits the two-scale lift $\psi(x) = \psi_0(X) + a\,\psi_1(X, y) + a^2 \psi_2(X, y) + \cdots$ with $y = x/a$. The leading term $\psi_0$ is independent of $y$. The order-$a^{-1}$ equation yields the cell problem

$$
\partial_{y^i}\!\left[A^{ij}(y)\big(\partial_{y^j}\chi^k(y) + \delta^k_j\big)\right] = 0, \qquad \chi^k \text{ is } Y\text{-periodic},
$$

and the cell-averaging operator

$$
\langle f \rangle \;\equiv\; \frac{1}{|Y|}\int_Y f(y)\, d^3 y
$$

produces the effective coefficient

$$
A^{*ik} \;=\; \langle A^{ik} \rangle + \langle A^{ij}\, \partial_{y^j}\chi^k \rangle .
$$

Specializing to electromagnetism (with $A \leftrightarrow \mu^{-1}$ for TM modes and $A \leftrightarrow \varepsilon$ for TE modes), one obtains the effective constitutive tensors

$$
\varepsilon_{\rm eff}^{ij} \;=\; \langle \varepsilon^{ij} \rangle + \langle \varepsilon^{ik}\, \partial_{y^k}\chi^j \rangle, \qquad
(\mu_{\rm eff}^{-1})^{ij} \;=\; \langle (\mu^{-1})^{ij} \rangle + \langle (\mu^{-1})^{ik}\, \partial_{y^k} \tilde\chi^j \rangle .
$$

With engineered wire-array inclusions one obtains the Drude form $\varepsilon_{\rm eff}(\omega) = \varepsilon_\infty(1 - \omega_p^2/\omega^2)$ with $\omega_p^2 = 2\pi c^2 / [a^2 \ln(a/r_0)]$; with split-ring resonator inclusions one obtains the Lorentz form $\mu_{\rm eff}(\omega) = 1 - F\omega^2/(\omega^2 - \omega_0^2 + i\gamma\omega)$. When both responses are negative in overlapping frequency bands, the branch choice $n_{\rm eff} = -\sqrt{\varepsilon_r \mu_r}$ is FORCED by causal energy outflow.

**Closure 1 statement.** Subwavelength engineered microstructure $\Rightarrow$ controlled $\varepsilon_{\rm eff}(\omega), \mu_{\rm eff}(\omega)$, including negative branches.

### 1.2 Transformation optics (Memos 7–11) — effective metric

Under P-MM-1, P-MM-3, P-MM-4, P-MM-6, a slowly varying deformation $x'^i = f^i(x)$ with Jacobian $J^i{}_j = \partial x'^i / \partial x^j$ acting on a substrate carrying isotropic vacuum rule-type structure produces a coarse-grained anisotropic medium whose constitutive tensors are

$$
\varepsilon'^{ij} \;=\; \frac{1}{\det J}\, J^i{}_k J^j{}_l\, \varepsilon^{kl}, \qquad
\mu'^{ij} \;=\; \frac{1}{\det J}\, J^i{}_k J^j{}_l\, \mu^{kl}.
$$

The wave equation in the deformed substrate is equivalent to the covariant Laplace–Beltrami form

$$
\frac{1}{\sqrt{|g|}}\, \partial_i\!\left[\sqrt{|g|}\, g^{ij}\, \partial_j \psi\right] + k_0^2\, \psi = 0
$$

with effective metric

$$
g_{ij} \;=\; D_{ij} \;=\; (J^{-1})^k{}_i\, (J^{-1})^l{}_j\, \delta_{kl}, \qquad g^{ij} = \frac{(J J^T)^{ij}}{\det J}, \qquad \sqrt{|g|} = \frac{1}{\det J} .
$$

This is a coarse-grained rule-type geometry, **not** spacetime curvature; it lives on the substrate as an engineered modulation of rule-type structure.

The Pendry 2006 spherical cloak is the deformation $r' = R_1 + \alpha r$ with $\alpha = (R_2 - R_1)/R_2$, mapping the open ball $r < R_2$ onto the shell $R_1 < r' < R_2$. The induced constitutive tensors are

$$
\frac{\varepsilon_{\hat r'}}{\varepsilon_0} \;=\; \beta\, \frac{(r' - R_1)^2}{r'^2}, \qquad \frac{\varepsilon_{\hat\theta'}}{\varepsilon_0} = \frac{\varepsilon_{\hat\phi'}}{\varepsilon_0} = \beta,
$$

with $\beta = R_2/(R_2 - R_1)$ and the same expressions for $\mu$. The vanishing of $\varepsilon_{\hat r'}$ at $r' = R_1$ topologically excludes the interior: substrate channels routed by the deformation cannot enter the cloaked region.

**Closure 2 statement.** Smooth engineered substrate deformation $\Rightarrow$ controlled effective metric $g_{ij}$ and constitutive tensors, including invisibility by topological exclusion.

### 1.3 Metasurface boundary conditions (Memo 12) — phase-gradient discontinuity

Under P-MM-1, P-MM-5, P-MM-6, a codimension-1 surface at $z = 0$ across which the rule-type microstructure jumps discontinuously, engineered to imprint a tangential phase profile $\Phi(r_\parallel)$, imposes the matching condition

$$
\psi_{2}(r_\parallel, 0^+) \;=\; \psi_{1}(r_\parallel, 0^-)\, e^{i \Phi(r_\parallel)} .
$$

The tangential gradient yields

$$
k_{\parallel,2} \;=\; k_{\parallel,1} + \nabla_\parallel \Phi(r_\parallel),
$$

which, for an interface between media of refractive indices $n_1$ and $n_2$ with linear phase gradient $\Phi(x) = (d\Phi/dx)\, x$, gives the generalized Snell's law

$$
n_1 \sin\theta_i \;=\; n_2 \sin\theta_t + \frac{\lambda}{2\pi}\, \frac{d\Phi}{dx} .
$$

The standard Snell's law is the special case $d\Phi/dx = 0$.

**Closure 3 statement.** Engineered codimension-1 rule-type discontinuity with phase profile $\Phi(r_\parallel)$ $\Rightarrow$ controlled refraction angles independent of the bulk indices alone.

---

## 2. (A) How the three clusters fit together

The three closures address three logically distinct ways to modulate the substrate rule-type structure that supports wave propagation:

1. **Smooth periodic microstructure** (Closure 1) — vary rule-type response on scale $a \ll \lambda$, average to obtain $\varepsilon_{\rm eff}, \mu_{\rm eff}$. The substrate is unstrained; only its internal rule-type content is modulated.
2. **Smooth aperiodic deformation** (Closure 2) — apply a slow displacement field $u(X)$ to the substrate itself, producing an effective metric $g_{ij}$ and transformed constitutive tensors. The substrate is strained; its rule-type content is transported covariantly.
3. **Codimension-1 discontinuity** (Closure 3) — confine the modulation to an interface, imprinting a phase profile $\Phi(r_\parallel)$ that produces tangential momentum kicks. The substrate is unstrained in the bulk; only the interface carries engineered rule-type content.

These three options are exhaustive for substrate-level wave control within the precursor machinery. The argument is as follows. P-MM-4 confines us to second-order wave equations of the form $\partial_i [A^{ij}(x) \partial_j \psi] + k_0^2 n^2(x) \psi = 0$. Any engineered modification of the substrate that can be coarse-grained within the window P-MM-6 must enter one of three locations:

- The coefficient $A^{ij}(x)$ varies smoothly on a scale $a \ll \lambda$ — Closure 1.
- The coordinate $x$ itself is the image of a deformed substrate $x = f(X')$ with $f$ smooth — Closure 2.
- The coefficient $A^{ij}(x)$ has a codimension-1 jump on a surface — Closure 3.

Higher-codimension features (lines, points) do not survive coarse-graining: under P-MM-6 they appear as point scatterers at the device scale and are not metamaterial control mechanisms. Volumetric non-smooth features cannot be averaged within the homogenization window and reduce to one of the three cases at the operating wavelength. The three closures therefore cover the substrate-level control space.

Compositions are allowed: a metasurface (Closure 3) can be backed by a homogenized substrate (Closure 1); a transformation-optics device (Closure 2) can be implemented as a graded homogenized medium (Closure 1 with slowly varying cell). Such compositions are the generic case in practice.

---

## 3. (B) Unifying substrate-level structure

Each closure factors into three substrate-level operations:

- **Engineered rule-type microstructure** (P-MM-1): non-trivial internal content of the substrate.
- **Engineered deformation** (P-MM-3): coordinate-level displacement of the substrate.
- **Engineered discontinuity** (P-MM-5): codimension-1 jumps in the rule-type content or deformation.

The unifying statement is

$$
\boxed{\;\;\text{Metamaterials} \;=\; \text{engineered rule-type microstructure} \;+\; \text{engineered deformation} \;+\; \text{engineered discontinuity}.\;\;}
$$

Each closure is the implementation of one of these three terms in isolation:

| Closure | Microstructure | Deformation | Discontinuity |
|---|---|---|---|
| Homogenization | engineered, periodic | trivial | trivial |
| Transformation optics | trivial vacuum | engineered, smooth | trivial |
| Metasurface BCs | trivial bulk | trivial bulk | engineered codim-1 |

The wave equation in the coarse-grained substrate, in fully general form, reads

$$
\frac{1}{\sqrt{|g|}}\, \partial_i\!\left[\sqrt{|g|}\, g^{ij}\, \varepsilon_{\rm eff}^{-1, jk}\, \partial_k \psi\right] + k_0^2\, \mu_{\rm eff}\, \psi = 0,
$$

subject to jump conditions on engineered codim-1 surfaces $\Sigma$:

$$
[\psi]_\Sigma \;=\; \psi(r_\parallel, 0^+) - \psi(r_\parallel, 0^-)\, e^{i\Phi(r_\parallel)} = 0 \quad (\text{phase-imprinting case}).
$$

This is the unified substrate-level wave equation of the Arc. The three closures are its three independent control knobs: $\varepsilon_{\rm eff}, \mu_{\rm eff}$ (Closure 1), $g_{ij}$ (Closure 2), and $\Phi$ on $\Sigma$ (Closure 3).

All three control knobs derive from the same substrate operations (P-MM-1, P-MM-3, P-MM-5) coarse-grained under P-MM-6 and propagated under P-MM-4. The unification is structural, not analogical.

---

## 4. (C) Reproduction of the four Nobel-frontier photonics results

We map each Nobel-frontier result to the closure that produces it.

### 4.1 Yablonovitch — photonic bandgaps

A spatially periodic substrate microstructure with period $a$ comparable to (not much smaller than) the wavelength supports Bloch eigenmodes $\psi_{n, k}(x) = u_{n,k}(x)\, e^{i k \cdot x}$ with $u_{n,k}$ periodic, indexed by band index $n$ and crystal momentum $k$ in the first Brillouin zone. The dispersion relation $\omega_n(k)$ can develop gaps where no propagating modes exist. This is the Bloch theorem applied to electromagnetism. It lies adjacent to, but not inside, the homogenization regime $\lambda \gg a$ of Closure 1: photonic crystals operate at $\lambda \sim a$ where homogenization breaks down and band structure becomes the relevant description.

Within the precursor machinery, photonic bandgaps are the natural extension of Closure 1 to the $\lambda \sim a$ regime. They use the same substrate operation (P-MM-1, P-MM-2) but the analysis is Floquet–Bloch rather than two-scale homogenization. The Bloch theorem is closed in the walkthrough series outside this Arc; we cite its existence here without re-deriving.

**Yablonovitch result reproduction:** photonic bandgaps follow from periodic P-MM-1 with $a \sim \lambda$ via Bloch analysis. (Outside this Arc's precursor closures; adjacent regime.)

### 4.2 Pendry — negative index

From §1.1 above, engineered wire-array microstructure yields Drude $\varepsilon_{\rm eff}(\omega) < 0$ below an engineered plasma frequency; engineered split-ring resonator microstructure yields Lorentz $\mu_{\rm eff}(\omega) < 0$ in a band above the resonance. When both responses are negative in an overlapping band, causal outgoing-wave selection FORCES the branch

$$
n_{\rm eff}(\omega) \;=\; -\sqrt{\varepsilon_r(\omega)\, \mu_r(\omega)} .
$$

This is Closure 1 (homogenization) operating in the doubly-resonant regime.

**Pendry negative-index result reproduction:** FORCED by Closure 1.

### 4.3 Pendry — cloaking

From §1.2 above, the deformation $r' = R_1 + \alpha r$ produces a shell-supported anisotropic medium whose effective metric has $g_{\hat r' \hat r'} = \beta^2 (r' - R_1)^2/r'^2$ vanishing at the inner surface. Substrate channels routed by P-MM-3 cannot cross the inner surface; the interior is topologically excluded. Impedance matching $\mu_i / \varepsilon_i = \mu_0/\varepsilon_0$ for each principal direction eliminates reflections at the outer surface.

**Pendry cloaking result reproduction:** FORCED by Closure 2.

### 4.4 Capasso — metasurfaces

From §1.3 above, an engineered codim-1 discontinuity carrying linear phase profile $\Phi(x) = (d\Phi/dx) x$ produces the generalized Snell's law

$$
n_1 \sin\theta_i = n_2 \sin\theta_t + \frac{\lambda}{2\pi}\, \frac{d\Phi}{dx},
$$

which permits anomalous refraction (including refraction angles unattainable from the bulk indices alone) and beam steering.

**Capasso metasurface result reproduction:** FORCED by Closure 3.

### 4.5 Summary of Nobel-frontier reproduction

| Result | Closure | Mechanism |
|---|---|---|
| Yablonovitch (photonic bandgaps) | adjacent to 1 | Bloch theorem on periodic P-MM-1 |
| Pendry (negative index) | 1 | doubly-resonant homogenization, $n = -\sqrt{\varepsilon_r \mu_r}$ |
| Pendry (cloaking) | 2 | transformation optics, topological exclusion |
| Capasso (metasurfaces) | 3 | phase-gradient codim-1 discontinuity, generalized Snell |

The four Nobel-frontier photonics directions are reproduced by the three precursor closures plus the externally-closed Bloch theorem.

---

## 5. (D) Substrate-level map of metamaterials

The space of metamaterial functionalities is organized by the type of substrate operation invoked:

- **Smooth microstructure** ($\nabla A^{ij}(y)$ smooth on $Y$, $a \ll \lambda$) → homogenized medium with $\varepsilon_{\rm eff}, \mu_{\rm eff}$.
- **Smooth deformation** ($u(X)$ smooth, $|\nabla u| < 1$) → transformation-optics device with effective metric $g_{ij}$.
- **Discontinuous deformation / microstructure** (codim-1 surface with $\Phi(r_\parallel)$) → metasurface with phase-gradient control.
- **Periodic microstructure at $a \sim \lambda$** → photonic crystal with band structure (adjacent to Closure 1).
- **Resonant microstructure** (e.g., split-ring at $\omega_0$) → Lorentz/Drude response, negative-index regime.
- **Combined microstructure + deformation** → graded-index transformation-optics device implemented by spatially varying homogenized cells.
- **Combined microstructure + discontinuity** → frequency-selective metasurface, multi-band Capasso devices.
- **Combined deformation + discontinuity** → graded transformation-optics device with metasurface termination.
- **All three combined** → arbitrary optical functionality within the precursor window P-MM-6.

The substrate-level map is therefore a three-axis classification (microstructure, deformation, discontinuity) with combinations spanning the practical metamaterial design space.

---

## 6. (E) Limits of the precursor machinery

The precursor machinery is bounded by the regime in which P-MM-6 holds and the closures' derivations remain controlled.

### 6.1 Homogenization limits ($\lambda \gg a$)

Two-scale expansion requires $a/\lambda \ll 1$. As $a \to \lambda$, the corrector field $\chi^j(y)$ acquires non-negligible $X$-dependence and additional cell-averaged corrections enter at order $(a/\lambda)^2$. The homogenization picture breaks down; Bloch analysis takes over. For practical metamaterials operating at microwave frequencies with $a \sim \lambda/10$, the leading homogenization picture is quantitative to a few percent; near $a \sim \lambda/3$ it is qualitative only.

### 6.2 Dispersion limits (Drude/Lorentz)

Negative-index operation requires both $\varepsilon_r < 0$ and $\mu_r < 0$. The Drude form $\varepsilon_r(\omega) = 1 - \omega_p^2/\omega^2$ requires $\omega < \omega_p$; the Lorentz form $\mu_r(\omega) = 1 - F\omega^2/(\omega^2 - \omega_0^2 + i\gamma\omega)$ admits $\mu_r < 0$ only in a narrow band above $\omega_0$. The overlap band is intrinsically narrow ($\Delta\omega/\omega \sim 10\%$ typical). Losses $\gamma$ become significant near resonance and degrade $|n|$ rapidly. Causality (Kramers–Kronig) FORCES dispersion wherever $\mathrm{Im}\,\varepsilon, \mathrm{Im}\,\mu \neq 0$; lossless negative-index media over arbitrarily broad bandwidth are forbidden.

### 6.3 Transformation-optics smoothness limits

The deformation $f(x)$ must have $\det J > 0$ everywhere, $J$ and $J^{-1}$ bounded, and (for physical realizability) the induced $\varepsilon, \mu$ tensors must be physically achievable by some homogenized medium. The Pendry spherical cloak achieves $\det J \to \infty$ at $r' = R_1$, producing a singular response; perfect cloaking over all frequencies is forbidden by causality (the cloak is intrinsically dispersive, bandwidth-limited, and group-velocity-bounded). Practical cloaks operate over narrow bands and include the homogenization error of their constituent metamaterial.

### 6.4 Metasurface phase-gradient limits

The generalized Snell's law requires $\Phi(r_\parallel)$ to vary slowly on the scale of $\lambda$ for the boundary-condition treatment to be valid; phase profiles with features finer than $\lambda$ are not captured by Closure 3 alone and must be analyzed with full diffraction theory. The phase imprint is intrinsically frequency-dependent (the meta-atoms supporting $\Phi$ are resonant), so achromatic metasurfaces require multi-resonance engineering and remain bandwidth-limited.

### 6.5 Energy, causality, and bandwidth

All three closures inherit:

- **Energy conservation** in the lossless limit: $\nabla\cdot\mathbf{S} + \partial_t u = 0$ with $\mathbf{S}$ the Poynting vector and $u$ the field energy density.
- **Causality** (Kramers–Kronig): $\varepsilon(\omega), \mu(\omega)$ analytic in the upper half-plane $\Rightarrow$ dispersion is mandatory whenever absorption occurs.
- **Bandwidth–response trade-off**: large $|\varepsilon|, |\mu|, |n|$ or singular $g_{ij}$ requires concentration of spectral weight, which by Kramers–Kronig narrows the bandwidth.
- **No superluminal information transport**: group velocity may exceed $c$ in regions of anomalous dispersion, but signal front velocity (Sommerfeld–Brillouin) is bounded by $c$.

These are absolute constraints from substrate-level causality and from P-MM-6.

---

## 7. (F) Forward-looking synthesis

### 7.1 What the final public-facing walkthrough must contain

The public walkthrough `from_primitives_to_metamaterials_and_photonics.md` should be a self-contained, primitives-to-results derivation chain of approximately 10–11 sections. It must:

1. Open with the six primitives P-MM-1 through P-MM-6, restated from Memo 1.
2. State the three closures as compact theorems with their derivation chains traceable to the Arc memos.
3. Walk through the four Nobel-frontier results (Yablonovitch, Pendry-negative, Pendry-cloak, Capasso) as instantiations of the closures.
4. Provide the unifying statement: metamaterials = engineered microstructure + engineered deformation + engineered discontinuity.
5. Include the substrate-level map (§5 of this memo) as the design-space classification.
6. State the precursor-machinery limits honestly (§6 of this memo).
7. Label each result FORCED / FORM-FORCED-VALUES-INHERITED / OPEN.
8. End with a short outlook section on what the substrate-level account does and does not buy beyond conventional metamaterials theory.

The walkthrough must be standalone (no cross-references), in the established walkthrough style, and approximately 500–700 lines.

### 7.2 How the three precursor closures integrate into a single narrative

The narrative is: the substrate carries rule-type structure at scale $\ell_P$; coarse-graining within the window $\ell_P \ll a \ll \lambda \ll L$ produces a wave equation with effective coefficients; the three independent ways to engineer those coefficients are smooth microstructure, smooth deformation, and codim-1 discontinuity; each of these has been historically discovered as a distinct subfield (homogenization-based metamaterials, transformation optics, metasurfaces) but in the substrate picture they are three projections of a single structural identity. The four Nobel-frontier photonics results are the canonical demonstrations of each projection plus the periodic-microstructure regime adjacent to Closure 1.

### 7.3 What remains open at the substrate level

The precursor machinery, as closed in Memos 1–12, is structurally complete for the four Nobel-frontier photonics directions. The following items are OPEN but not load-bearing for the public walkthrough:

- **Quantitative substrate derivation of corrector-field response at $a \sim \lambda/3$.** The leading two-scale expansion is FORCED; the next-order corrections are FORM-FORCED-COEFFICIENT-INHERITED from cell-problem solutions on specific geometries.
- **Substrate-level account of nonlocal (spatially dispersive) metamaterials.** The closure machinery as stated is local; spatial dispersion enters at the next order in $a/\lambda$ and requires a generalization beyond the leading two-scale expansion.
- **Substrate-level account of active and time-varying metamaterials.** Time-dependent deformation $u(X, t)$ and time-varying microstructure are allowed within P-MM-3 and P-MM-1 respectively, but the corresponding closures (Floquet-in-time, parametric amplification, non-reciprocal phenomena) require their own dedicated derivations and are not within the present Arc's scope.
- **Substrate-level account of topological photonics.** Edge states, Chern numbers, and photonic topological insulators are adjacent to Closure 1 (periodic microstructure with engineered band topology) and to closed walkthroughs outside this Arc (Bloch, photonic Chern channels). They are reachable but not derived in the present precursor Arc.
- **Quantum-optical metamaterials.** Single-photon and entangled-photon propagation through metamaterials uses the same coarse-grained wave equation at the field level; substrate-level quantum-state evolution through Closure 1/2/3 devices is reachable from the closed QM-emergence inventory but not derived here.

None of these OPEN items blocks the public walkthrough.

---

## 8. Status labels for the Arc

- **Two-scale homogenization framework (Memos 2–3):** FORCED from P-MM-1, P-MM-2, P-MM-4, P-MM-6.
- **Effective constitutive tensors $\varepsilon_{\rm eff}, \mu_{\rm eff}$ (Memo 4):** FORM-FORCED; values INHERITED from specific microstructure geometries via the cell problem.
- **Substrate meaning of $\varepsilon, \mu$ as coarse-grained rule-type response (Memo 5):** FORCED.
- **Negative-index conditions and branch choice $n = -\sqrt{\varepsilon_r \mu_r}$ (Memo 6):** FORCED in the doubly-negative band by causal outgoing-wave selection; specific $\omega_p, \omega_0$ values INHERITED from inclusion geometry.
- **Rule-type deformation tensor $D_{ij}$ and constitutive transformation (Memo 7):** FORCED from P-MM-3 + P-MM-4 + P-MM-6.
- **Mapping to effective metric $g_{ij}$ (Memo 8):** FORCED; identification $g_{ij} = D_{ij}$ is structural, not analogical.
- **Pendry spherical cloak (Memos 9–10):** FORCED form for the deformation $r' = R_1 + \alpha r$; values $\alpha, \beta$ INHERITED from cloak-shell geometry choice.
- **General transformation optics (Memo 11):** FORCED form for arbitrary smooth $f(x)$; realizability constraints FORCED.
- **Metasurface phase-imprinting BC and generalized Snell's law (Memo 12):** FORCED form from P-MM-5 + P-MM-6; phase profile $\Phi(r_\parallel)$ INHERITED from meta-atom geometry.
- **Unified substrate-level wave equation with three control knobs (this memo, §3):** FORCED.
- **Exhaustiveness of the three closures within the precursor machinery (this memo, §2):** FORCED under P-MM-4 + P-MM-6.
- **Reproduction of the four Nobel-frontier photonics results (this memo, §4):** Yablonovitch reproduction is INHERITED from externally-closed Bloch theorem; Pendry-negative, Pendry-cloak, Capasso reproductions are FORCED by Closures 1, 2, 3 respectively.

**Open items (not load-bearing):** higher-order homogenization corrections, nonlocal/spatially dispersive metamaterials, active and time-varying metamaterials, topological photonics within Closure 1, quantum-optical metamaterials.

**No new substrate primitives introduced anywhere in the Arc.**

---

## 9. Review

The Arc set out to close the substrate-level derivation gap for a future public walkthrough on metamaterials and photonics covering the Yablonovitch / Pendry / Capasso Nobel-frontier directions. It identified three precursor closures needed:

1. Homogenization — to ground negative-index Pendry 2000.
2. Transformation optics — to ground cloaking Pendry 2006.
3. Metasurface boundary conditions — to ground generalized Snell's law Capasso 2011.

Memos 2–6 closed homogenization; Memos 7–11 closed transformation optics; Memo 12 closed metasurface boundary conditions. This memo (Memo 13) synthesizes the three closures into a single substrate-level account.

The synthesis establishes that the three closures exhaust the substrate-level wave-control space within the precursor machinery; that all three derive from the same substrate operations (engineered microstructure, engineered deformation, engineered discontinuity) within P-MM-6; that the four Nobel-frontier results map cleanly onto the three closures (plus the adjacent Bloch regime for Yablonovitch); and that the precursor machinery is structurally complete for the planned public walkthrough.

No new substrate primitives were introduced. All derivations stayed within P-MM-1 through P-MM-6. The Arc is closed.

---

## 10. Recommended Next Steps

These recommendations are listed for completeness; the user is not obligated to follow them.

1. **Produce the public walkthrough** `from_primitives_to_metamaterials_and_photonics.md` per §7.1 above, composing the three precursor closures with the externally-closed Bloch theorem walkthrough.
2. **Update the memory ledger** to add a `project_arc_metamaterials.md` entry recording that the Arc closed with 13 memos, three precursor clusters, no new primitives, and Nobel-relevance routing for Yablonovitch / Pendry / Capasso.
3. **Update `project_walkthrough_series_expansion.md`** to record the metamaterials/photonics walkthrough once produced, including its derivation chain (Memos 2–6 → negative index; Memos 7–11 → cloaking; Memo 12 → generalized Snell; Bloch walkthrough → bandgaps).
4. **Spawn (or queue) the OPEN follow-on arcs** if/when relevant: nonlocal metamaterials (next-order homogenization), active/time-varying metamaterials (Floquet-in-time), topological photonics within Closure 1, quantum-optical metamaterials.
5. **Cross-link the closed Arc** to the existing photonic Chern channels and Bloch theorem walkthroughs in the program inventory, so that the metamaterials/photonics walkthrough can compose cleanly with adjacent closed work.
6. **Consider a publication-grade paper** in the `papers/` tree consolidating the Arc, structured as: substrate primitives → three closures → unifying statement → reproduction of four Nobel-frontier results → limits and open extensions. This is optional and depends on whether the program is targeting external publication on the metamaterials side.

End of Memo 13. End of Arc Metamaterials precursor closure.
