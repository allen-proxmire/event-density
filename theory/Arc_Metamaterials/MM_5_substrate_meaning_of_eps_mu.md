# Memo 5 — Substrate-Level Meaning of $\varepsilon$ and $\mu$

**Arc Metamaterials, Memo 5 of 13.**
**Allen Proxmire** · May 2026

*Articulate the substrate-level meaning of the effective constitutive parameters derived in Memo 4. Establish that $\varepsilon$ is a coarse-grained rule-type polarizability and $\mu$ is a coarse-grained rule-type circulation response. Interpret the corrector decomposition. Explain why $\varepsilon$ and $\mu$ are not fundamental fields. Identify the substrate-level conditions under which they can become negative — preparing the ground for Memo 6.*

---

## 1. Setup and Notation

A chain of the kind permitted by P-MM-4 — a channel propagating in a structured medium — has pre-individuation amplitude $\psi(\mathbf{x})$ governed by a scalar wave equation derived from Maxwell's equations under one polarization choice:

$$
\partial_i\!\left[A^{ij}(\mathbf{x}/a)\, \partial_j \psi\right] + k_0^{2}\, B(\mathbf{x}/a)\, \psi = 0,
$$

where the rule-type kinetic-response tensor $A^{ij}(\mathbf{y})$ identifies with the inverse permeability $\mu^{-1\,ij}(\mathbf{y})$ in the transverse-magnetic (TM) polarization, or with the permittivity $\varepsilon^{ij}(\mathbf{y})$ in the analogous formulation for the displacement field, and the potential-response scalar $B(\mathbf{y})$ identifies with the conjugate constitutive coefficient.

The substrate's rule-type microstructure varies periodically on the unit cell $Y = [0, 1]^d$ with cell size $a$ (P-MM-1 + P-MM-2). The chain's coarse-grained wavelength $\lambda$ satisfies $a \ll \lambda \ll L$ (P-MM-6).

From Memos 2–4, the multi-scale expansion produced:

- Two-scale lift $\tilde\psi(\mathbf{X}, \mathbf{y}) = \psi_0(\mathbf{X}) + a\chi^j(\mathbf{y})\partial_{X^j}\psi_0 + \ldots$, with leading-order amplitude $\psi_0(\mathbf{X})$ independent of $\mathbf{y}$.
- Cell correctors $\chi^j(\mathbf{y})$ satisfying $L_\mathbf{y}[\chi^j] = -\partial_{y^i}A^{ij}(\mathbf{y})$ with periodic BCs on $Y$ and mean-zero normalization.
- Averaging operator $\langle f \rangle = (1/|Y|)\int_Y f(\mathbf{y})\, d^dy$.
- Effective tensors

$$
\varepsilon_{\mathrm{eff}}^{ij} = \langle\varepsilon^{ij}(\mathbf{y})\rangle + \langle\varepsilon^{ik}(\mathbf{y})\,\partial_{y^k}\chi^j(\mathbf{y})\rangle,
$$

$$
\mu_{\mathrm{eff}}^{-1\,ij} = \langle\mu^{-1\,ij}(\mathbf{y})\rangle + \langle\mu^{-1\,ik}(\mathbf{y})\,\partial_{y^k}\chi^j_M(\mathbf{y})\rangle,
$$

with $\chi^j$ the electric cell corrector and $\chi^j_M$ the magnetic cell corrector.

This Memo articulates the *substrate-level meaning* of these constructions. The mathematics is established; this Memo is interpretive, but its content is rigorous: each substrate-level reading is derived from the substrate primitives P-MM-1 through P-MM-6 inline.

---

## 2. The Substrate-Level Meaning of Permittivity $\varepsilon$

### 2.1 The standard physical definition

In standard electromagnetism, the local permittivity $\varepsilon(\mathbf{x})$ relates the displacement field $\mathbf{D}$ to the electric field $\mathbf{E}$ via the constitutive relation

$$
\mathbf{D}(\mathbf{x}) = \varepsilon(\mathbf{x})\,\mathbf{E}(\mathbf{x}).
$$

Equivalently, the polarization density $\mathbf{P} = \mathbf{D} - \varepsilon_0\mathbf{E}$ is the induced electric dipole moment per unit volume, and

$$
\mathbf{P}(\mathbf{x}) = \big(\varepsilon(\mathbf{x}) - \varepsilon_0\big)\,\mathbf{E}(\mathbf{x}) \equiv \chi_e(\mathbf{x})\,\varepsilon_0\,\mathbf{E}(\mathbf{x}),
$$

with $\chi_e = \varepsilon_r - 1$ the electric susceptibility.

At substrate level, $\varepsilon_0$ is the vacuum value of the rule-type kinetic-response, $\varepsilon(\mathbf{x})$ is its locally-modulated value in a structured substrate, and $\mathbf{P}$ measures the *additional* response above vacuum that the substrate's microstructure produces.

### 2.2 The substrate-level identification

The substrate's rule-type microstructure (P-MM-1) consists of localized participation-rule structures — bound atomic dipoles, dielectric inclusions, metallic wires, resonant elements — distributed within each unit cell. When the chain (a light-like channel; P-MM-4) propagates through this microstructure, the substrate's gauge field couples to these localized rule-type structures via standard rule-type-coupling (the same machinery that produces minimal-coupling in T17 gauge-field theory, applied here at substrate level).

The substrate-level statement: the local rule-type response of the microstructure to the chain's electric component shifts each localized participation-rule structure's *alignment* slightly, producing a substrate-level *induced rule-type polarization*. The cell-averaged induced polarization, per unit applied electric field, is the substrate-level definition of $\varepsilon$.

Formally: define the substrate-level polarization density as the cell-averaged rule-type-alignment shift induced per unit volume:

$$
P^i(\mathbf{X}) \equiv \big\langle \delta r_\text{align}^i(\mathbf{X}, \mathbf{y})\big\rangle,
$$

where $\delta r_\text{align}^i$ is the local rule-type-alignment displacement at position $\mathbf{y}$ within the cell at slow position $\mathbf{X}$, in direction $i$. (The "alignment displacement" is the substrate-level pre-image of the dipole-moment-density vector; see §2.3 for explicit construction.)

For linear response, $P^i$ is linear in the applied field component:

$$
P^i(\mathbf{X}) = \varepsilon_0\,\chi_e^{ij}(\mathbf{X})\,E_j(\mathbf{X}).
$$

The substrate-level susceptibility $\chi_e^{ij}(\mathbf{X})$ is the *coarse-grained rule-type polarizability* of the microstructure at slow position $\mathbf{X}$. The full permittivity is $\varepsilon^{ij}_\text{eff}(\mathbf{X}) = \varepsilon_0(\delta^{ij} + \chi_e^{ij}(\mathbf{X}))$.

### 2.3 Where the cell-averaged response comes from

The cell-averaged polarization decomposes as

$$
P^i(\mathbf{X}) = \big\langle \chi^{ij}_e(\mathbf{y})\big\rangle\varepsilon_0 E_j(\mathbf{X}) + \big\langle \chi_e^{ik}(\mathbf{y})\,\partial_{y^k}\chi^j(\mathbf{y})\big\rangle\varepsilon_0 E_j(\mathbf{X}),
$$

matching the structure of $\varepsilon_{\mathrm{eff}}^{ij}$ from Memo 4. The two terms have distinct substrate-level interpretations:

**First term** — *bare cell average*: $\langle \chi_e^{ij}(\mathbf{y})\rangle$ is the volume-fraction-weighted average of the local rule-type polarizability across the unit cell. If the cell contains fraction $f$ of high-polarizability rule-type structure ($\chi_e^{(1)}$) and fraction $1-f$ of vacuum ($\chi_e^{(2)} = 0$), this term gives $f\chi_e^{(1)}$.

**Second term** — *microstructure correction*: $\langle\chi_e^{ik}\partial_{y^k}\chi^j\rangle$ is the contribution from the chain's amplitude rearrangement within the cell. When the chain's amplitude redistributes (via the corrector $\chi^j$) to minimize its energetic interaction with the rule-type structure, the cell-averaged response is *reduced* below the bare average. The redistribution concentrates the chain's amplitude in low-polarizability regions and removes it from high-polarizability regions.

In substrate-level language: the chain "routes around" high-response rule-type structures within the cell. The corrector $\chi^j$ encodes this routing pattern. The microstructure correction term captures the reduction in effective response that the routing produces.

### 2.4 Substrate-level summary

$$
\boxed{\quad
\varepsilon_{\mathrm{eff}}^{ij}(\mathbf{X}) = \text{coarse-grained rule-type polarizability response of the substrate microstructure to the gauge field's electric component, computed as cell-averaged response with microstructure-induced routing correction.}
\quad}
$$

Where the chain experiences this:
- **At probe scale $\lambda \gg a$**: the chain sees only the effective $\varepsilon_{\mathrm{eff}}^{ij}$, not the underlying microstructure.
- **At substrate scale $a$**: the microstructure varies; the chain's amplitude varies with it (through $\psi_1 = \chi^j\partial_{X^j}\psi_0$).
- **At fundamental scale $\ell_P$**: substrate-level rule-type structure; not resolved at metamaterial probe scales.

---

## 3. The Substrate-Level Meaning of Permeability $\mu$

### 3.1 The standard physical definition

In standard electromagnetism, the local permeability $\mu(\mathbf{x})$ relates the magnetic field $\mathbf{H}$ to the magnetic induction $\mathbf{B}$ via

$$
\mathbf{B}(\mathbf{x}) = \mu(\mathbf{x})\,\mathbf{H}(\mathbf{x}).
$$

The magnetization $\mathbf{M} = \mathbf{B}/\mu_0 - \mathbf{H}$ is the induced magnetic dipole moment per unit volume:

$$
\mathbf{M}(\mathbf{x}) = \big(\mu(\mathbf{x})/\mu_0 - 1\big)\mathbf{H}(\mathbf{x}) \equiv \chi_m(\mathbf{x})\,\mathbf{H}(\mathbf{x}),
$$

with $\chi_m = \mu_r - 1$ the magnetic susceptibility.

Magnetic dipole moments arise from circulating currents — at the atomic level, electron orbital and spin currents; in engineered metamaterials, induced currents in split-ring resonators or wire loops.

### 3.2 The substrate-level identification

In ED, the gauge field's magnetic component is the curl of the gauge connection $\mathbf{A}$:

$$
\mathbf{B} = \nabla \times \mathbf{A}.
$$

At substrate level, the gauge connection is the rule-type connection on the participation-rule bundle (this is T17's substrate-level identification, treated here as a given). The curl of the rule-type connection measures the substrate-level *rule-type curvature* — the holonomy accumulated by a chain as its identity is parallel-transported around a closed loop.

Magnetic response arises when the substrate's microstructure contains *closed-loop rule-type circulation pathways*: spatial regions where the chain's pre-individuation amplitude can circulate, producing induced rule-type holonomy that opposes the applied rule-type curvature (Lenz's law analog).

The substrate-level statement: the local rule-type circulation response of the microstructure to the chain's magnetic component induces a substrate-level *induced rule-type magnetization*. The cell-averaged induced magnetization, per unit applied magnetic field, is the substrate-level definition of $\mu$.

Formally: define the substrate-level magnetization density as the cell-averaged rule-type circulation per unit volume:

$$
M^i(\mathbf{X}) \equiv \big\langle (\nabla_\mathbf{y} \times \mathbf{j}_\text{rule-circ})^i (\mathbf{X}, \mathbf{y})\big\rangle,
$$

where $\mathbf{j}_\text{rule-circ}$ is the local rule-type circulation current density (analog of the magnetization current in standard EM). The cell-averaged magnetization, in linear response, is

$$
M^i(\mathbf{X}) = \chi_m^{ij}(\mathbf{X})\,H_j(\mathbf{X}),
$$

with $\chi_m^{ij}$ the substrate-level *rule-type circulation susceptibility*. The full permeability is $\mu^{ij}_\text{eff}(\mathbf{X}) = \mu_0(\delta^{ij} + \chi_m^{ij}(\mathbf{X}))$, and the inverse permeability used in TM-mode homogenization is the inverse of this tensor.

### 3.3 Where the cell-averaged response comes from

For the inverse-permeability formulation that appeared naturally in Memo 4's TM-mode analysis:

$$
\mu_{\mathrm{eff}}^{-1\,ij}(\mathbf{X}) = \big\langle\mu^{-1\,ij}(\mathbf{y})\big\rangle + \big\langle\mu^{-1\,ik}(\mathbf{y})\,\partial_{y^k}\chi^j_M(\mathbf{y})\big\rangle.
$$

Two terms:

**First term** — *bare cell-averaged inverse permeability*: average of the local inverse rule-type circulation response across the unit cell.

**Second term** — *magnetic microstructure correction*: contribution from the chain's amplitude redistribution within the cell that affects the rule-type circulation pattern. The magnetic corrector $\chi^j_M$ encodes how the chain's amplitude rearranges to minimize its energetic coupling to the local rule-type circulation structures.

### 3.4 The role of T17 rule-type connection

T17 establishes the gauge field as the rule-type connection on the participation-rule bundle. In the substrate, the chain's identity is parallel-transported by this connection; rule-type holonomy around closed loops produces the substrate-level pre-image of the magnetic flux through the loop.

A substrate with *non-trivial microstructure for circulation pathways* — for instance, a split-ring resonator pattern that supports localized rule-type circulation modes — can exhibit large effective $\mu$ even when the underlying substrate is non-magnetic at the rule-type level. The effective magnetic response is *not* a fundamental property of the substrate at the V1 / T17 level; it is a *coarse-grained statistical response* of the microstructure's circulation pathways.

This is the substrate-level reason that metamaterials can exhibit strong magnetic response at optical frequencies despite the underlying non-magnetic constituent materials: the magnetic response is *geometric* (from the microstructure's support for rule-type circulation) rather than *intrinsic* (from the constituent rule-type alignment).

### 3.5 Substrate-level summary

$$
\boxed{\quad
\mu_{\mathrm{eff}}^{ij}(\mathbf{X}) = \text{coarse-grained rule-type circulation response of the substrate microstructure to the gauge field's magnetic component, where rule-type circulation pathways are the closed loops along which the T17 rule-type connection accumulates holonomy.}
\quad}
$$

---

## 4. The Substrate-Level Meaning of the Corrector Fields

### 4.1 Microstructure-induced deformation of channel propagation

The cell corrector field $\chi^j(\mathbf{y})$ is the substrate-level *pattern by which the chain's pre-individuation amplitude redistributes within each unit cell in response to a unit macroscopic gradient* in direction $j$.

At each $\mathbf{y}$ within the unit cell, the corrector value $\chi^j(\mathbf{y})$ tells us how much the chain's amplitude differs from the cell-average leading-order $\psi_0(\mathbf{X})$:

$$
\psi(\mathbf{x}) \approx \psi_0(\mathbf{X}) + a\,\chi^j(\mathbf{y})\,\partial_{X^j}\psi_0(\mathbf{X}) + O(a^2).
$$

The correction $a\chi^j\partial_{X^j}\psi_0$ is *small* (suppressed by $a/\lambda$) and *periodic in $\mathbf{y}$*. It encodes the chain's local adaptation to the rule-type microstructure.

### 4.2 Why the corrector is non-zero

The cell problem $L_\mathbf{y}[\chi^j] = -\partial_{y^i}A^{ij}(\mathbf{y})$ has zero source when $A^{ij}$ is constant in $\mathbf{y}$ (trivial microstructure). The source $-\partial_{y^i}A^{ij}$ is non-zero exactly when $A^{ij}$ varies across the unit cell — that is, when the substrate has non-trivial rule-type microstructure.

The substrate-level interpretation: the corrector is *forced into existence* by the spatial variation of the rule-type response within the cell. As the chain's macroscopic gradient $\partial_{X^j}\psi_0$ traverses regions of different rule-type response, the chain's amplitude must adapt locally; the adaptation pattern is $\chi^j(\mathbf{y})$.

### 4.3 Sign of the corrector correction

The corrector contribution to $\varepsilon_{\mathrm{eff}}$ has a specific sign structure derivable from the cell problem. Multiplying the cell problem by $\chi^j$ and integrating over $Y$:

$$
\int_Y \chi^j\, L_\mathbf{y}[\chi^j]\, d^dy = -\int_Y \chi^j\,\partial_{y^i}A^{ij}\, d^dy.
$$

Integrating both sides by parts (boundary terms vanish by periodicity):

$$
-\int_Y A^{ik}\,\partial_{y^i}\chi^j\,\partial_{y^k}\chi^j\, d^dy = \int_Y A^{ij}\,\partial_{y^i}\chi^j\, d^dy.
$$

The left side is $-\langle A^{ik}(\partial_{y^i}\chi^j)(\partial_{y^k}\chi^j)\rangle |Y| \leq 0$ (since $A$ is positive-definite). The right side is $\langle A^{ij}\partial_{y^i}\chi^j\rangle |Y|$. Therefore

$$
\langle A^{ij}\,\partial_{y^i}\chi^j\rangle \leq 0.
$$

Relabeling indices ($i \leftrightarrow k$) and recognizing this as the corrector-correction term in $A^{*ij}$:

$$
\langle A^{ik}\,\partial_{y^k}\chi^j\rangle \leq 0 \quad \text{(diagonal components)}.
$$

The corrector correction is *non-positive* on diagonal components — meaning it always *reduces* the effective response below the arithmetic mean. This is the substrate-level statement that microstructural rearrangement of the chain's amplitude is always energetically favorable (reduces effective coupling to the microstructure).

### 4.4 Substrate-level interpretation summary

$$
\boxed{\quad
\chi^j(\mathbf{y}) = \text{substrate-level local accommodation pattern of the chain's amplitude in response to a macroscopic gradient, forced by spatial variation of the rule-type microstructure within the unit cell.}
\quad}
$$

The corrector encodes the chain's "routing strategy" — how the chain redistributes its amplitude within each cell to minimize energetic interaction with the rule-type microstructure. The routing strategy is forced by the cell problem; once the microstructure is specified, the corrector is uniquely determined (up to mean-zero normalization).

---

## 5. $\varepsilon$ and $\mu$ Are Not Fundamental Fields

### 5.1 What is fundamental at substrate level

The ED program's substrate-level inventory contains:
- Chains (P-MM-4): channels along which participation rules propagate.
- Bandwidth: the graded measure of participation.
- Polarity: U(1)-valued phase relation between chain's update rule and local ED-flow.
- Rule-type structure: the substrate's local rule-type identity assignment.
- V1 finite-width kernel: the substrate's vacuum-response kernel.
- The substrate's rule-type connection (T17 gauge structure).

The permittivity $\varepsilon$ and permeability $\mu$ are *not* in this inventory. They do not exist as primitive substrate fields. They are *coarse-grained statistical descriptors* of how the substrate's rule-type microstructure responds to applied gauge fields, computed via the homogenization machinery of Memos 2–4.

### 5.2 What this means in practice

At every scale below $\lambda$, the substrate is described by:
- Chain dynamics (substrate-level rule-type evolution).
- Rule-type microstructure $\tau(\mathbf{x})$ specifying which rule-type structure occupies each substrate-level region.

At scales above $\lambda$, the chain experiences the substrate as if it had constitutive parameters $\varepsilon_{\mathrm{eff}}(\mathbf{X}), \mu_{\mathrm{eff}}(\mathbf{X})$. These are summary statistics — they capture exactly enough of the underlying microstructure for the chain's coarse-grained dynamics, but they erase the substructural detail.

The substrate-level statement: $\varepsilon$ and $\mu$ are not properties of "matter"; they are properties of how rule-type microstructure summarizes itself when probed at large coarse-grained scales. Different microstructures with the same cell-averaged response produce identical $\varepsilon, \mu$ — the substrate-level details are invisible to the chain at probe scale $\lambda$.

### 5.3 Why this matters for metamaterials

This substrate-level reading is precisely what makes metamaterials possible. By *engineering* the rule-type microstructure within each unit cell, one can produce target $\varepsilon_{\mathrm{eff}}, \mu_{\mathrm{eff}}$ values that may not exist in any natural material. The microstructure is the substrate-level engineering knob; the effective parameters are the macroscopic output.

In particular:
- **Negative $\varepsilon$**: requires a microstructure whose cell-averaged rule-type polarizability is *negative* at the operating frequency. Natural materials cannot do this in general; engineered plasma-like (wire-array) microstructures can.
- **Negative $\mu$**: requires a microstructure whose cell-averaged rule-type circulation response is *negative*. Natural non-magnetic materials cannot do this; engineered resonator (split-ring) microstructures can.

The substrate-level basis: at substrate level, neither $\varepsilon < 0$ nor $\mu < 0$ violates anything fundamental, because $\varepsilon$ and $\mu$ are not fundamental. They are coarse-grained statistical descriptors; their sign and magnitude depend entirely on the microstructure being engineered.

---

## 6. Anisotropy, Dispersion, and Tensor Structure

### 6.1 Anisotropy from sub-cubic microstructure

When the unit-cell rule-type microstructure lacks full cubic symmetry, the effective tensors $\varepsilon_{\mathrm{eff}}^{ij}, \mu_{\mathrm{eff}}^{ij}$ are anisotropic. The substrate-level reading: the chain's routing strategy through the cell is direction-dependent. For a macroscopic gradient in one direction, the cell-averaged response differs from the response to a gradient in another direction.

Layered substrate (uniaxial example, see Memo 4 §4.4):
- Gradient *along layers*: $\varepsilon^\text{eff}_\perp = \langle\varepsilon\rangle$ (arithmetic mean).
- Gradient *across layers*: $\varepsilon^\text{eff}_\parallel = \langle\varepsilon^{-1}\rangle^{-1}$ (harmonic mean).

Substrate-level reading: the chain's amplitude in the across-layer direction must maintain *continuity* across each interface between layers of different rule-type response. The continuity condition forces the chain's amplitude to develop a specific pattern that is dominated by the weakest-coupling layer — yielding the harmonic mean.

### 6.2 Dispersion from resonant microstructure

When the local $\varepsilon^{ij}(\mathbf{y}; \omega)$ or $\mu^{ij}(\mathbf{y}; \omega)$ depends on frequency $\omega$ (resonant microstructure), the cell-averaged effective parameters inherit this frequency dependence.

Resonant rule-type structures within the cell — bound atomic dipoles with natural frequencies, ring resonators with magnetic resonance frequencies, etc. — respond strongly to the chain's gauge field near their resonance, and weakly far from it. The substrate-level mechanism: the rule-type structure's identity-alignment response is large near its natural mode and small elsewhere, producing strong $\omega$-dependence in the cell-averaged response.

The homogenization machinery applies at each frequency $\omega$ separately: solve the cell problem at $\omega$, average to get $\varepsilon_{\mathrm{eff}}(\omega)$, repeat for the next $\omega$. The result is a frequency-dependent effective medium.

### 6.3 Tensor structure from rule-type tensor character

The rule-type response is intrinsically tensorial: at each substrate point, the response depends on the *direction* of the applied field. For rule-type microstructures with anisotropic local response (e.g., uniaxial crystals, oriented molecular structures), $\varepsilon^{ij}(\mathbf{y})$ is itself a position-dependent tensor.

The substrate-level reading: the rule-type structure can favor one direction over others — for instance, a polar molecule's alignment preferentially shifts in one direction in response to an applied field. The local tensor character of $\varepsilon^{ij}$ encodes this preferential direction at substrate level.

When homogenized via the cell problem, the effective tensor $\varepsilon_{\mathrm{eff}}^{ij}$ inherits the local tensor character plus additional anisotropy from the microstructure's spatial geometry.

---

## 7. Substrate-Level Mechanisms for Three Key Phenomena

### 7.1 Local field enhancement

Standard physics: in subwavelength microstructures, the local electric field can be much larger than the macroscopic applied field (factor 10–1000), concentrated at sharp features, resonant elements, or interfaces.

Substrate-level reading: the corrector $\chi^j(\mathbf{y})$ can have large gradients $|\partial_{y^k}\chi^j|$ at sharp microstructure features. The local field $E^j(\mathbf{x}) = \partial_{X^j}\psi_0(\mathbf{X}) + a^{-1}\partial_{y^j}[\chi^k(\mathbf{y})\partial_{X^k}\psi_0]$ contains a $1/a$ enhancement factor from the fast-derivative term.

The substrate-level mechanism: at sharp features, the chain's amplitude redistributes rapidly to accommodate the local rule-type structure. The rapid redistribution produces large local field values. The cell-averaged macroscopic response is moderated by the corrector contribution, but the *local* field at specific positions can be far larger than the cell average.

The substrate-level enhancement factor is $|a^{-1}\partial_{y^j}\chi^k|$, the corrector gradient. For sharp rule-type discontinuities (interface between regions of very different response), this gradient can be order $1/a$, producing a $1/a$-scaled enhancement of the local field.

### 7.2 Microstructure-induced phase delay

Standard physics: a chain traversing a homogenized medium accumulates phase $k_{\mathrm{eff}} L$ along path length $L$, with $k_{\mathrm{eff}} = \omega \sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}$.

Substrate-level reading: the chain's pre-individuation amplitude accumulates phase at rate $\omega_{\mathrm{becoming}} = \omega\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}$ per unit time, where $\omega_{\mathrm{becoming}}$ is the chain's local rate of phase accumulation in the coarse-grained effective medium. The rate is modulated by the cell-averaged rule-type response: dense microstructure (high $\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}$) slows the chain's coarse-grained becoming.

The substrate-level mechanism: through the cell problem, the chain's amplitude redistributes to interact preferentially with high-response regions of the microstructure; each interaction accumulates phase. The cell-averaged phase accumulation per unit propagation is the substrate-level pre-image of the effective wavenumber $k_{\mathrm{eff}}$.

Equivalently: the chain's effective propagation speed is reduced below the substrate's fundamental $c$ by the factor $\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}}/\sqrt{\varepsilon_0\mu_0}$. The substrate $c$ itself is unchanged; only the chain's *dressed* (cell-averaged) propagation speed is modified.

### 7.3 Microstructure-induced circulation

Standard physics: in a magnetic metamaterial, induced currents (or rule-type circulation patterns) flow within each unit cell in response to the applied magnetic field. The cell-averaged circulation produces the effective magnetization.

Substrate-level reading: rule-type closed-loop pathways within the cell support local rule-type circulation. T17 establishes that the gauge connection's holonomy around closed loops is gauge-invariant; the rule-type curvature (magnetic field) drives this holonomy.

When the unit cell contains a ring-like structure (e.g., split-ring resonator), the chain's amplitude can circulate within the ring in response to the applied rule-type curvature. The induced circulation produces a counter-curvature (Lenz-law analog) that determines the cell-averaged magnetic response.

The substrate-level mechanism: rule-type closed-loop pathways are *geometric features* of the microstructure that support local circulation modes. The cell-averaged response is the sum of all such local circulation modes, weighted by the applied magnetic field. Engineered split-ring resonators (Pendry 1999) provide controlled circulation pathways with tunable resonance frequency, allowing engineered $\mu_{\mathrm{eff}}$.

---

## 8. Conditions for Negative $\varepsilon_{\mathrm{eff}}$ and $\mu_{\mathrm{eff}}$

This section prepares the ground for Memo 6, which derives the specific microstructures producing negative-index metamaterials. Here we identify the *substrate-level conditions* under which the effective constitutive parameters can become negative.

### 8.1 Negative $\varepsilon_{\mathrm{eff}}$

The bare-average $\langle\varepsilon^{ij}\rangle$ is positive at static and high frequencies for ordinary dielectric microstructures (with $\varepsilon \geq \varepsilon_0 > 0$). However, near resonances or for plasma-like microstructures, the local $\varepsilon(\mathbf{y}; \omega)$ can become *negative*.

**Plasma-like response (wire-array microstructures).** A conducting wire embedded in vacuum supports collective rule-type oscillations (plasma modes) at a plasma frequency $\omega_p$. For frequencies $\omega < \omega_p$, the rule-type polarizability response is *negative* — the rule-type alignment opposes the applied field rather than following it. Standard Lorentz-Drude analysis gives the local response

$$
\varepsilon_\text{wire}(\omega) = \varepsilon_0\!\left(1 - \frac{\omega_p^2}{\omega^2 + i\gamma\omega}\right),
$$

with damping $\gamma$. For $\omega < \omega_p$ and small $\gamma$, $\text{Re}[\varepsilon_\text{wire}] < 0$.

Cell-averaged response for a wire array embedded in vacuum: $\varepsilon_{\mathrm{eff}}(\omega) \approx f\varepsilon_\text{wire}(\omega) + (1-f)\varepsilon_0$, with $f$ the wire volume fraction. For $\omega < \omega_p\sqrt{f}$ (effective plasma frequency of the array), $\varepsilon_{\mathrm{eff}}(\omega) < 0$.

The substrate-level condition for $\varepsilon_{\mathrm{eff}} < 0$: a sufficient fraction of the unit cell must support rule-type polarizability response that is negative at the operating frequency. Plasma-like (wire-array) microstructures satisfy this below the array's effective plasma frequency.

### 8.2 Negative $\mu_{\mathrm{eff}}$

The bare-average $\langle\mu^{ij}\rangle$ is positive for non-magnetic constituent materials. However, *resonant* microstructures (e.g., split-ring resonators) can produce *negative* cell-averaged response in narrow frequency windows.

**Resonant magnetic response (split-ring resonators).** A split-ring resonator (a circular conducting ring with a gap) supports a localized LC-resonance: the ring inductance plus gap capacitance produces a magnetic dipole resonance at frequency $\omega_0$. For frequencies $\omega$ slightly above $\omega_0$, the induced rule-type circulation *opposes* the applied magnetic field strongly enough to produce negative cell-averaged response.

Standard analysis yields the local resonant susceptibility

$$
\chi_m(\omega) = \frac{F\omega^2}{\omega_0^2 - \omega^2 - i\gamma\omega},
$$

with $F$ the filling-factor-weighted resonance strength. For frequencies just above $\omega_0$, $\chi_m(\omega) < -1$ and $\mu_{\mathrm{eff}}(\omega) = \mu_0(1 + \chi_m) < 0$.

The substrate-level condition for $\mu_{\mathrm{eff}} < 0$: the unit cell must contain rule-type circulation pathways (closed-loop structures supporting localized rule-type modes) with a resonance frequency $\omega_0$ near the operating frequency. Slightly above the resonance, the induced circulation overshoots and produces negative effective response.

### 8.3 Combined negative-index regime

When both $\varepsilon_{\mathrm{eff}}(\omega) < 0$ and $\mu_{\mathrm{eff}}(\omega) < 0$ simultaneously, the effective refractive index satisfies

$$
n_{\mathrm{eff}}^2 = \varepsilon_{\mathrm{eff}}\,\mu_{\mathrm{eff}} > 0,
$$

so $n_{\mathrm{eff}}$ is real, but the sign of $n_{\mathrm{eff}}$ is determined by the causality / Maxwell-wave analysis: for a passive medium with both $\varepsilon < 0$ and $\mu < 0$, the correct branch is $n_{\mathrm{eff}} = -\sqrt{\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}/(\varepsilon_0\mu_0)} < 0$.

The substrate-level reading: the chain's coarse-grained propagation in such a medium exhibits *reversed phase velocity relative to energy flow*, equivalent to negative refraction at interfaces with positive-index media. The microstructure has produced an effective rule-type response opposite to the natural one.

The conditions for negative refractive index:
1. Microstructure with negative $\varepsilon_{\mathrm{eff}}$ at $\omega$ (e.g., wire array below plasma frequency).
2. Microstructure with negative $\mu_{\mathrm{eff}}$ at $\omega$ (e.g., split-ring resonator above magnetic resonance).
3. Both effects active simultaneously at the operating $\omega$ — a narrow frequency window.

Memo 6 derives both microstructures explicitly from substrate primitives.

---

## 9. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **$\varepsilon_{\mathrm{eff}}$ as coarse-grained rule-type polarizability** (§2). FORCED by the cell-averaged response of the rule-type microstructure to the gauge field's electric component, computed via the cell problem.

- **$\mu_{\mathrm{eff}}$ as coarse-grained rule-type circulation response** (§3). FORCED by T17's identification of the gauge connection with the rule-type connection + cell-averaged response of rule-type closed-loop pathways in the microstructure.

- **Corrector fields as substrate-level local accommodation patterns** (§4). FORCED by the cell problem: spatial variation of the microstructure forces the chain's amplitude to redistribute within the cell.

- **Non-positive sign of the corrector correction** (§4.3). FORCED by the variational principle for $L_\mathbf{y}$ (microstructural rearrangement always reduces effective response below arithmetic mean).

- **$\varepsilon$ and $\mu$ are not fundamental fields** (§5). FORCED by the substrate ontology: only chains, bandwidth, polarity, rule-type structure, V1 kernel, and rule-type connection are primitive. $\varepsilon$ and $\mu$ are derived statistical descriptors of microstructure response.

- **Substrate-level mechanisms for field enhancement, phase delay, and circulation** (§7). FORCED by the corrector structure and the cell-averaged response decomposition.

- **Substrate-level conditions for negative $\varepsilon$ and negative $\mu$** (§8). FORCED at structural level: plasma-like microstructures for negative $\varepsilon$, resonant circulation pathways for negative $\mu$. The specific Lorentz-Drude and resonant-susceptibility forms are inherited from standard analysis (see §9 below).

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Standard constitutive relations $\mathbf{D} = \varepsilon\mathbf{E}, \mathbf{B} = \mu\mathbf{H}$** (§2.1, 3.1). Standard EM definitions; the substrate-level interpretation is the new content of this Memo.

- **Lorentz-Drude form for plasma-like response** (§8.1). Standard atomic-physics derivation; here it is invoked at the level of *form* (specific functional dependence on $\omega$) without re-deriving from first principles. The substrate-level reading: rule-type collective oscillations of conducting microstructures produce this response form.

- **Resonant susceptibility for split-ring resonators** (§8.2). Standard LC-circuit analysis applied to the ring; the substrate-level reading is rule-type circulation modes of the closed-loop pathway.

- **Branch choice for $n_{\mathrm{eff}}$ in the negative-index regime** (§8.3). Standard causality / Maxwell-wave analysis; the substrate-level reading is the chain's pre-individuation amplitude exhibiting reversed phase velocity relative to energy flow.

### What remains OPEN

- **Detailed substrate-level derivation of the Lorentz-Drude form** from rule-type primitives (V1 kernel + bound rule-type structures + collective coupling). Standard atomic physics provides the form; a substrate-level derivation from substrate-V1-kernel response to bound rule-type structures is OPEN.

- **Substrate-level derivation of the split-ring resonator response**. The LC-circuit analysis is standard; the substrate-level mechanism is intuitive but a fully-derived substrate-level treatment of how a closed-loop rule-type pathway supports a localized circulation mode is OPEN.

- **Quantum corrections to the effective constitutive parameters** at high field strength or near material resonances. The classical homogenization machinery treats $\varepsilon, \mu$ as linear response; nonlinear and quantum corrections are FORM-FORCED but coefficient-INHERITED at standard nonlinear-optics level. Substrate-level OPEN.

- **Substrate-level account of the role of T17 in producing the magnetic response.** Memo 5 invokes T17's identification of gauge connection with rule-type connection; the explicit substrate-level derivation of how this produces effective $\mu$ for circulation-supporting microstructures is at the level of structural reading rather than full derivation. OPEN at full-derivation level.

- **Hyperbolic and indefinite metamaterials.** When $\varepsilon$ or $\mu$ has mixed signs in different directions (positive in one axis, negative in another), the effective medium is hyperbolic. Substrate-level reading is direct; the experimental phenomenology is OPEN.

- **Active and gain-loss-balanced metamaterials.** Non-Hermitian rule-type microstructure with gain or loss. OPEN.

---

## 10. Review and Recommended Next Steps

### Review

Memo 5 has delivered:

- **Substrate-level meaning of $\varepsilon$** as a coarse-grained rule-type polarizability response (§2).
- **Substrate-level meaning of $\mu$** as a coarse-grained rule-type circulation response, tied to T17's identification of the gauge connection with the rule-type connection (§3).
- **Substrate-level interpretation of the corrector fields** $\chi^j(\mathbf{y})$ as local accommodation patterns of the chain's amplitude in response to macroscopic gradients (§4), with proof that the corrector correction always reduces effective response below the arithmetic mean.
- **Interpretation of the effective-tensor decomposition**: bare-average term (volume-fraction-weighted) + microstructure correction (chain's routing through the cell) (§2.3, 3.3).
- **Establishment that $\varepsilon$ and $\mu$ are not fundamental fields in ED** but coarse-grained statistical descriptors emerging from P-MM-1 through P-MM-4 (§5).
- **Substrate-level mechanisms for anisotropy, dispersion, tensor structure** (§6) — all traceable to microstructure features and resonant rule-type modes.
- **Substrate-level mechanisms for local field enhancement, phase delay, circulation** (§7) — explained via corrector gradients, cell-averaged phase rate, and rule-type closed-loop pathways.
- **Substrate-level conditions for negative $\varepsilon_{\mathrm{eff}}$ and $\mu_{\mathrm{eff}}$** (§8) — plasma-like microstructures for negative $\varepsilon$; resonant circulation pathways for negative $\mu$; combined negative-index regime requires both simultaneously at the operating frequency.
- **Explicit FORCED / FORM-FORCED-INHERITED / OPEN labeling** (§9).

### Honest scope-limit

Memo 5 is interpretive rather than primarily derivational. The substrate-level meanings of $\varepsilon$ and $\mu$ are derived from the substrate primitives plus the homogenization machinery of Memos 2–4; the standard Lorentz-Drude and resonant-susceptibility forms are FORM-FORCED-INHERITED with substrate-level mechanism layered on top. No new substrate primitives are introduced.

### Recommended next steps

1. **Memo 6 — Conditions for Negative Index (Pendry 2000).** Derive the wire-array (negative $\varepsilon$) and split-ring-resonator (negative $\mu$) microstructures from substrate primitives. Compute the effective $\varepsilon_{\mathrm{eff}}(\omega), \mu_{\mathrm{eff}}(\omega)$ for each, identify the frequency window in which both are negative, and derive the resulting negative refractive index. Articulate the substrate-level mechanism for negative refraction at interfaces. This closes the homogenization cluster (Memos 2–6).

2. **Memos 7–11 — Transformation Optics.** Build on the homogenization machinery + substrate-gradient deformation (P-MM-3) to derive cloaking and other transformation-optics effects from substrate primitives.

3. **Memo 12 — Metasurface Boundary Conditions.** Derive the generalized Snell's law from substrate-level rule-type discontinuities at interfaces (P-MM-5).

4. **Memo 13 — Synthesis.** Tie the three precursor derivations together.

### Anchor for future memos

The substrate-level meanings established in Memo 5 — $\varepsilon$ as coarse-grained rule-type polarizability, $\mu$ as coarse-grained rule-type circulation response, corrector fields as local accommodation patterns, and the substrate-level non-fundamentality of $\varepsilon, \mu$ — are standardized for the remainder of the Arc. Memo 6 will compute specific values; Memos 7–11 will deform the effective tensors under substrate-gradient transformations. Throughout, the substrate-level interpretation of $\varepsilon, \mu$ provided by Memo 5 anchors the physical content.
