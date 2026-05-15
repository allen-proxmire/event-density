# Memo 12 — Substrate-Level Metasurface Boundary Conditions

**Arc Metamaterials, Memo 12 of 13.**
**Allen Proxmire** · May 2026

*Close the third precursor of the Arc. Derive the substrate-level boundary conditions for a metasurface — an engineered interface with sub-wavelength-patterned rule-type discontinuity — and from those conditions derive the generalized Snell's law $n_1\sin\theta_i = n_2\sin\theta_t + (\lambda/2\pi)\,d\Phi/dx$ that governs Capasso-style refraction. Articulate the substrate-level meaning of phase-imprinting as engineered rule-type mismatch.*

---

## 1. Setup and Notation

A chain (P-MM-4) propagates through a substrate whose rule-type microstructure (P-MM-1) is *piecewise smooth*: smooth on each side of a codimension-1 interface, with an abrupt discontinuity at the interface itself (P-MM-5). We treat this discontinuity as a *substrate-level engineered rule-type jump* that produces the observed metasurface phenomenology.

This Memo is independent of the transformation-optics cluster (Memos 7–11). The transformation-optics machinery handles smooth substrate-gradient deformations; metasurfaces require separate treatment because the deformation is *discontinuous* at the interface. The smooth-Jacobian formalism does not apply; instead, the substrate-level interface boundary condition is derived directly.

### 1.1 Setup geometry

Choose coordinates so that the metasurface interface is the plane $z = 0$:

- For $z < 0$ ("medium 1"): substrate has rule-type microstructure with effective refractive index $n_1$.
- For $z > 0$ ("medium 2"): substrate has rule-type microstructure with effective refractive index $n_2$.
- At $z = 0$: metasurface — an engineered rule-type discontinuity with sub-wavelength-patterned phase imprint $\Phi(x, y)$ along the tangential coordinates.

We assume:
- The interface is flat (planar) and infinite in extent. Curved interfaces add geometric factors but the structural argument is identical.
- The two bulk media on either side are homogeneous (Memos 2–6's effective constitutive tensors are constants $n_1, n_2$).
- The metasurface thickness is sub-wavelength: $d_\text{meta} \ll \lambda$. The metasurface is effectively a 2D boundary, not a 3D layer.

### 1.2 Chain incident on the interface

A chain (light-like ED-channel, P-MM-4) is incident on the metasurface from medium 1 at angle $\theta_i$ relative to the interface normal $\hat{\mathbf{n}} = \hat{\mathbf{z}}$. The chain's pre-individuation amplitude in medium 1 is

$$
\psi_1(\mathbf{x}) = A_i\, e^{i(\mathbf{k}_1^i\cdot\mathbf{x} - \omega t)} + A_r\, e^{i(\mathbf{k}_1^r\cdot\mathbf{x} - \omega t)},
$$

with incident wave vector $\mathbf{k}_1^i$ at angle $\theta_i$, and reflected wave vector $\mathbf{k}_1^r$ at angle $\theta_r$ (initially undetermined).

In medium 2, the transmitted wave is

$$
\psi_2(\mathbf{x}) = A_t\, e^{i(\mathbf{k}_2\cdot\mathbf{x} - \omega t)},
$$

at angle $\theta_t$.

The wave vectors have magnitudes $|\mathbf{k}_1| = n_1 k_0$, $|\mathbf{k}_2| = n_2 k_0$, with $k_0 = \omega/c = 2\pi/\lambda$. The tangential components are

$$
k_{1,t}^i = n_1 k_0 \sin\theta_i, \qquad k_{1,t}^r = n_1 k_0 \sin\theta_r, \qquad k_{2,t} = n_2 k_0 \sin\theta_t.
$$

The chain's coarse-grained dynamics at the interface determine the relations among $\theta_i, \theta_r, \theta_t$ — i.e., Snell's law and the law of reflection.

### 1.3 What this Memo derives

1. The substrate-level structure of the metasurface as a rule-type discontinuity (§2).
2. The standard tangential-field continuity conditions from Maxwell's equations across the discontinuity (§3).
3. The phase-imprinting mechanism by which a sub-wavelength-patterned metasurface adds a position-dependent phase to chains crossing the interface (§4).
4. The generalized Snell's law as a tangential-momentum-conservation statement modified by the phase-imprint gradient (§5).
5. The conditions for physical realizability of the metasurface (§6).
6. The substrate-level synthesis preparing for Memo 13 (§7).

---

## 2. (A) Metasurface as a Rule-Type Discontinuity

### 2.1 The discontinuous deformation

A metasurface is a substrate-level *engineered rule-type discontinuity* (P-MM-5): an interface where the rule-type microstructure changes abruptly. We parameterize this via a discontinuous deformation:

$$
x'^i =
\begin{cases}
x^i, & z < 0, \\
x^i + \Delta^i(\mathbf{r}_\parallel), & z > 0,
\end{cases}
$$

where $\mathbf{r}_\parallel = (x, y)$ is the tangential position coordinate along the interface and $\Delta^i(\mathbf{r}_\parallel)$ is a position-dependent *tangential rule-type shift vector* that varies on the slow scale (i.e., on scales larger than $a$ but possibly smaller than $\lambda$).

This is the *discontinuous-deformation analog* of the smooth substrate-gradient deformations $\mathbf{f}(\mathbf{x})$ of Memos 7–11. The discontinuity is concentrated at $z = 0$ and is parameterized by the tangential shift $\boldsymbol\Delta(\mathbf{r}_\parallel)$.

### 2.2 Substrate-level interpretation

The substrate-level statement: the metasurface is a codimension-1 surface where the substrate's rule-type identity-labeling makes an abrupt jump. The pattern of the jump varies tangentially: at each point $(x, y)$ on the interface, the rule-type identity on the $z > 0$ side has been shifted by $\boldsymbol\Delta(x, y)$ relative to its un-deformed configuration. The shift varies with $(x, y)$ according to the metasurface's engineered pattern.

Physical realization: a metasurface is typically a 2D array of sub-wavelength resonators (split-ring resonators, V-shaped antennas, dielectric pillars) printed or etched at the interface. Each resonator is a localized rule-type structure (per Memo 1's P-MM-1 microstructure primitive) with engineered phase response. The aggregate effect is a *position-dependent phase imprint* on chains crossing the interface.

### 2.3 The phase imprint $\Phi(\mathbf{r}_\parallel)$

A chain crossing the metasurface acquires a position-dependent phase shift $\Phi(\mathbf{r}_\parallel)$. For a flat interface with sub-wavelength resonators, the phase shift at $(x, y)$ is the resonator's local phase response:

$$
\Phi(\mathbf{r}_\parallel) = \text{(engineered phase response at } \mathbf{r}_\parallel\text{)}.
$$

The phase imprint varies tangentially according to the engineered pattern of resonators. The metasurface's design specifies $\Phi(x, y)$ as a function on the interface plane.

### 2.4 Substrate-level connection

The phase imprint $\Phi(\mathbf{r}_\parallel)$ is the substrate-level manifestation of the discontinuous deformation $\boldsymbol\Delta(\mathbf{r}_\parallel)$:

$$
\Phi(\mathbf{r}_\parallel) \;=\; \mathbf{k}_\parallel \cdot \boldsymbol\Delta(\mathbf{r}_\parallel)
$$

for a wave with tangential wave vector $\mathbf{k}_\parallel$ encountering the discontinuity. The phase imprint is the wave-vector-dependent reading of the rule-type shift.

In the limit of sub-wavelength resonators (each resonator imposes a definite phase shift on the wave), the phase imprint $\Phi(\mathbf{r}_\parallel)$ becomes effectively wave-vector-independent — it is a property of the metasurface itself, engineered to produce any desired pattern. This is the Capasso 2011 regime.

### 2.5 Substrate-level summary of the metasurface

$$
\boxed{\quad
\text{Metasurface} \;=\; \text{engineered codimension-1 rule-type discontinuity with sub-wavelength-patterned phase imprint } \Phi(\mathbf{r}_\parallel) \text{ on chains crossing the interface}.
\quad}
$$

The chain's coarse-grained dynamics encounter this discontinuity as a *boundary condition* on its pre-individuation amplitude. The boundary condition determines how the incident, reflected, and transmitted wave vectors relate at the interface — the generalized Snell's law derived below.

---

## 3. (B) Jump Conditions from Maxwell's Equations

### 3.1 Standard tangential-field continuity

In standard electromagnetic theory, the boundary conditions across a 2D interface (with no free charges or currents) are:

$$
\hat{\mathbf{n}}\times(\mathbf{E}_2 - \mathbf{E}_1) = 0, \qquad \hat{\mathbf{n}}\times(\mathbf{H}_2 - \mathbf{H}_1) = 0,
$$

$$
\hat{\mathbf{n}}\cdot(\mathbf{D}_2 - \mathbf{D}_1) = 0, \qquad \hat{\mathbf{n}}\cdot(\mathbf{B}_2 - \mathbf{B}_1) = 0,
$$

with subscripts 1 and 2 denoting the fields on either side of the interface and $\hat{\mathbf{n}}$ the unit normal.

The tangential components of $\mathbf{E}$ and $\mathbf{H}$ are continuous; the normal components of $\mathbf{D}$ and $\mathbf{B}$ are continuous.

These are the *passive interface* conditions: they apply when no engineered surface charges or surface currents are present.

### 3.2 Surface polarization and surface currents from metasurfaces

A *metasurface* introduces an engineered surface polarization $\mathbf{P}_s$ and surface current $\mathbf{K}_s$ that modify the boundary conditions:

$$
\hat{\mathbf{n}}\times(\mathbf{E}_2 - \mathbf{E}_1) = -i\omega \,\hat{\mathbf{n}}\times(\hat{\mathbf{n}}\times\mathbf{M}_s),
$$

$$
\hat{\mathbf{n}}\times(\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{K}_s + i\omega\,\hat{\mathbf{n}}\times\mathbf{P}_s,
$$

where:
- $\mathbf{P}_s$ is the electric surface polarization (dipole density per unit area), induced by tangential electric field on the resonators.
- $\mathbf{M}_s$ is the magnetic surface polarization (dipole density per unit area), induced by tangential magnetic field.
- $\mathbf{K}_s$ is the surface electric current (conductivity contribution from any free charges on the resonators).

For passive dielectric metasurfaces (no free charges), $\mathbf{K}_s = 0$ and only the polarization terms remain.

### 3.3 Substrate-level meaning of surface polarization

At substrate level, the surface polarization $\mathbf{P}_s$ is the *cell-averaged rule-type-alignment shift per unit area at the interface*. The resonators at the interface each shift their local rule-type alignment in response to the chain's tangential electric field; the total alignment-shift per unit area is $\mathbf{P}_s$.

This is precisely the substrate-level mechanism that produces $\varepsilon - \varepsilon_0$ in bulk media (Memo 5 §2), now confined to a 2D interface rather than distributed through a 3D volume.

The surface polarization is the 2D analog of the bulk polarization:

$$
\mathbf{P}_s(\mathbf{r}_\parallel) = \chi_e^\text{surf}(\mathbf{r}_\parallel)\,\varepsilon_0\,\mathbf{E}_\text{local}(\mathbf{r}_\parallel),
$$

with $\chi_e^\text{surf}$ a position-dependent surface susceptibility encoding the engineered resonator response. The susceptibility's spatial pattern is what produces the position-dependent phase imprint.

### 3.4 Substrate-level meaning of surface magnetic polarization

Analogously, $\mathbf{M}_s$ is the cell-averaged rule-type circulation response per unit area at the interface. Resonant rule-type circulation pathways at the interface (e.g., split-ring resonators) produce induced magnetic dipoles in response to the chain's tangential magnetic field.

For a metasurface designed with $\chi_e^\text{surf}$ and $\chi_m^\text{surf}$ matched appropriately, the response is purely transmissive (no reflection) and produces only the phase imprint.

### 3.5 Reduction to phase-imprint form

For a thin (sub-wavelength) phase-control metasurface, the surface polarization and magnetization combine to produce a single effective property: a *position-dependent transmission phase* for chains crossing the interface.

In the *generalized sheet transition condition* (GSTC) formulation, the metasurface's transmission coefficient at position $\mathbf{r}_\parallel$ takes the form

$$
T(\mathbf{r}_\parallel) = |T(\mathbf{r}_\parallel)|\, e^{i\Phi(\mathbf{r}_\parallel)},
$$

where $|T| \leq 1$ is the transmission magnitude and $\Phi$ is the phase imprint. For an ideal lossless phase-control metasurface, $|T| = 1$ and only the phase imprint affects the chain.

The chain's pre-individuation amplitude on the transmitted side is

$$
\psi_2(\mathbf{r}_\parallel, z = 0^+) = \psi_1(\mathbf{r}_\parallel, z = 0^-)\, e^{i\Phi(\mathbf{r}_\parallel)}.
$$

This is the *phase-imprint boundary condition*. It is the substrate-level statement that the metasurface acts on the chain's amplitude by multiplying by a position-dependent phase factor.

---

## 4. (C) Phase-Imprinting Mechanism

### 4.1 Origin of the phase imprint

The phase imprint $\Phi(\mathbf{r}_\parallel)$ arises from the engineered local response of the resonators at each position on the interface. Three mechanisms produce a phase shift:

1. **Resonant electric response** of a sub-wavelength electric dipole resonator: a localized rule-type-polarizable structure (e.g., a V-shaped antenna) responds to the incident field by re-emitting with a phase shift that depends on the structure's geometry and resonance frequency.

2. **Resonant magnetic response** of a closed-loop resonator (e.g., split-ring resonator): induced rule-type circulation produces re-radiation with a phase shift dependent on the resonator's $\omega_0, F, \gamma$ parameters (Memo 6 §3).

3. **Geometric phase** (Pancharatnam-Berry): for circularly-polarized incident light, the orientation of the resonator's principal axis at $\mathbf{r}_\parallel$ produces a geometric phase shift equal to twice the rotation angle.

Each mechanism allows the metasurface designer to control the local phase imprint $\Phi(\mathbf{r}_\parallel)$ over a range of $[0, 2\pi)$ by adjusting the resonator's geometry, orientation, or composition at each position.

### 4.2 Substrate-level reading of phase imprint

At substrate level, the phase imprint at position $\mathbf{r}_\parallel$ is the result of the chain's pre-individuation amplitude being *re-aligned* by the local resonator's rule-type response. The resonator's engineered structure imposes a position-dependent rotation of the chain's amplitude phase as the chain crosses the interface.

Three substrate-level statements:

- **The resonators are localized rule-type pathways**: each resonator at $\mathbf{r}_\parallel$ supports a localized rule-type mode (electric dipole, magnetic dipole, or rotated linear polarization).
- **The chain's amplitude couples to the local mode**: at $\mathbf{r}_\parallel$, the chain's pre-individuation amplitude is partially absorbed and re-emitted by the local resonator. The re-emission's phase relative to the incident amplitude depends on the resonator's structure.
- **The aggregate effect across the interface is the phase imprint $\Phi(\mathbf{r}_\parallel)$**: averaging over the sub-wavelength resonator scale produces a smooth phase pattern that varies on the sub-wavelength scale (controlled by the metasurface designer).

### 4.3 The tangential momentum shift

A chain with tangential momentum $\mathbf{k}_{\parallel,1}$ incident on the metasurface acquires a tangential momentum kick from the spatial gradient of the phase imprint. The substrate-level mechanism:

The transmitted chain's amplitude is

$$
\psi_2(\mathbf{r}_\parallel, 0^+) = \psi_1(\mathbf{r}_\parallel, 0^-)\,e^{i\Phi(\mathbf{r}_\parallel)}.
$$

For a plane-wave incident chain $\psi_1 = A_i e^{i\mathbf{k}_{\parallel,1}\cdot\mathbf{r}_\parallel}$, the transmitted amplitude is

$$
\psi_2(\mathbf{r}_\parallel, 0^+) = A_i e^{i(\mathbf{k}_{\parallel,1}\cdot\mathbf{r}_\parallel + \Phi(\mathbf{r}_\parallel))}.
$$

The phase function at the interface is $\mathbf{k}_{\parallel,1}\cdot\mathbf{r}_\parallel + \Phi(\mathbf{r}_\parallel)$. The *effective tangential wave vector* on the transmitted side is the gradient of this phase function:

$$
\mathbf{k}_{\parallel,2} = \nabla_\parallel\!\left[\mathbf{k}_{\parallel,1}\cdot\mathbf{r}_\parallel + \Phi(\mathbf{r}_\parallel)\right] = \mathbf{k}_{\parallel,1} + \nabla_\parallel\Phi(\mathbf{r}_\parallel).
$$

So the chain acquires a *tangential momentum kick* equal to the gradient of the phase imprint:

$$
\boxed{\quad \mathbf{k}_{\parallel,2} = \mathbf{k}_{\parallel,1} + \nabla_\parallel\Phi(\mathbf{r}_\parallel). \quad}
$$

For a phase imprint varying only along one direction (say $x$): $\nabla_\parallel\Phi = (d\Phi/dx, 0)$, and the chain's tangential momentum shifts by $d\Phi/dx$ along $\hat{\mathbf{x}}$.

### 4.4 Substrate-level reading of the momentum shift

The tangential momentum kick is the substrate-level statement that the metasurface's engineered rule-type discontinuity *transfers tangential momentum* to the chain at the interface. The amount of momentum transfer per unit tangential distance is $d\Phi/dx$.

Substrate-level mechanism:
- The chain's pre-individuation amplitude has tangential phase pattern $\mathbf{k}_{\parallel,1}\cdot\mathbf{r}_\parallel$ on the incident side.
- The metasurface adds an additional position-dependent phase $\Phi(\mathbf{r}_\parallel)$.
- The transmitted amplitude has tangential phase pattern $\mathbf{k}_{\parallel,1}\cdot\mathbf{r}_\parallel + \Phi(\mathbf{r}_\parallel)$.
- The effective tangential wave vector on the transmitted side is the gradient of this combined phase pattern.

The chain's tangential phase advance per unit tangential distance has been modified by the metasurface's engineered phase gradient. This is the substrate-level origin of the generalized Snell's law.

---

## 5. (D) Derivation of Generalized Snell's Law

### 5.1 Tangential-momentum matching

The fundamental conservation law at the metasurface (modified by the engineered phase imprint) is:

$$
\mathbf{k}_{\parallel,2} = \mathbf{k}_{\parallel,1} + \nabla_\parallel\Phi(\mathbf{r}_\parallel).
$$

For a 1D phase imprint $\Phi = \Phi(x)$ (varying only in $\hat{\mathbf{x}}$), and an incident chain in the $xz$-plane (so $\mathbf{k}_{\parallel,1} = k_{1,t}\hat{\mathbf{x}}$ with $k_{1,t} = n_1 k_0\sin\theta_i$), the transmitted tangential wave vector is

$$
k_{2,t} = k_{1,t} + \frac{d\Phi}{dx}.
$$

### 5.2 Dispersion relations

The chain's wave vector in each medium satisfies the dispersion relation $|\mathbf{k}_i|^2 = (n_i k_0)^2$. The tangential and normal components are

$$
k_{i,t} = n_i k_0 \sin\theta_i, \qquad k_{i,n} = n_i k_0 \cos\theta_i.
$$

For the incident wave in medium 1:

$$
k_{1,t} = n_1 k_0 \sin\theta_i.
$$

For the transmitted wave in medium 2:

$$
k_{2,t} = n_2 k_0 \sin\theta_t.
$$

### 5.3 Generalized Snell's law

Substituting the dispersion relations into the tangential-momentum-matching condition:

$$
n_2 k_0 \sin\theta_t = n_1 k_0 \sin\theta_i + \frac{d\Phi}{dx}.
$$

Dividing through by $k_0 = 2\pi/\lambda$:

$$
\boxed{\quad
n_2 \sin\theta_t = n_1 \sin\theta_i + \frac{\lambda}{2\pi}\frac{d\Phi}{dx}.
\quad}
$$

This is the *generalized Snell's law* (Capasso 2011). It reduces to the standard Snell's law $n_1\sin\theta_i = n_2\sin\theta_t$ when $d\Phi/dx = 0$ (no phase imprint).

### 5.4 Reflection: generalized law of reflection

A parallel argument applies to the reflected wave. The reflected wave's tangential momentum also satisfies the modified matching condition:

$$
k_{1,t}^r = k_{1,t}^i + \frac{d\Phi}{dx}.
$$

With $k_{1,t}^r = n_1 k_0 \sin\theta_r$:

$$
\boxed{\quad
n_1 \sin\theta_r = n_1 \sin\theta_i + \frac{\lambda}{2\pi}\frac{d\Phi}{dx}.
\quad}
$$

Or: $\sin\theta_r - \sin\theta_i = (\lambda/(2\pi n_1))(d\Phi/dx)$. The reflected angle differs from the incident angle, in contradiction to the standard law of reflection $\theta_r = \theta_i$.

The substrate-level reading: the metasurface's engineered rule-type discontinuity transfers tangential momentum to both reflected and transmitted waves. The reflected wave is no longer at the symmetric angle.

### 5.5 Critical angle and anomalous regimes

When $d\Phi/dx$ is large enough, the right-hand side of the generalized Snell's law can exceed 1, producing $\sin\theta_t > 1$ — no real transmission angle exists. The chain is evanescent in medium 2 (total internal reflection from a phase gradient even if $n_2 > n_1$).

Conversely, for sufficiently negative $d\Phi/dx$, the transmission angle can be *negative*, producing *negative refraction* at a positive-index interface — the chain bends to the same side of the normal as the incident path. This is the metasurface analog of negative refraction.

These anomalous regimes are accessible by engineering the phase gradient $d\Phi/dx$ — a metasurface designer can produce arbitrary refraction angles (within causality and physical-realizability constraints) by choosing the appropriate phase pattern.

### 5.6 Substrate-level interpretation

The generalized Snell's law is the substrate-level statement of:

- **Metasurface as engineered rule-type discontinuity**: the interface's rule-type structure jumps in a position-dependent way, parameterized by $\Phi(\mathbf{r}_\parallel)$.
- **Phase gradient as engineered rule-type mismatch**: the spatial variation of $\Phi$ encodes a position-dependent rule-type-shift between the two sides.
- **Refraction angle as chain's response to tangential rule-type shift**: the chain's coarse-grained trajectory bends to satisfy the tangential-momentum conservation modified by the engineered phase gradient.

The substrate-level summary:

$$
\boxed{\quad
\text{Refraction at a metasurface} \;=\; \text{chain's adaptation of its tangential momentum to match the engineered rule-type discontinuity pattern}.
\quad}
$$

The chain's trajectory bends, not because of a passive optical response, but because of an *active engineered redirection* at the substrate-level rule-type interface.

---

## 6. (E) Physical Realizability

A metasurface design $\Phi(\mathbf{r}_\parallel)$ produces the generalized Snell's law via the mechanism of §4–§5. For the metasurface to be physically realizable, several conditions must hold.

### 6.1 Sub-wavelength thickness

**Requirement.** The metasurface's physical thickness $d_\text{meta}$ in the normal direction must satisfy $d_\text{meta} \ll \lambda$.

**Reason.** The boundary-condition treatment treats the metasurface as a 2D interface. If $d_\text{meta}$ is comparable to $\lambda$, the chain's amplitude variation through the metasurface must be treated as a 3D problem (a thin layer with its own internal dynamics), not as a simple jump at a 2D interface.

**Substrate-level meaning.** The rule-type discontinuity must be localized to a thin layer compared to the chain's coarse-grained probe scale. Thick metasurfaces become bulk media (treated by Memos 2–6 homogenization machinery).

### 6.2 Controlled discontinuity in rule-type microstructure

**Requirement.** The metasurface's resonator pattern produces a *deterministic* phase imprint $\Phi(\mathbf{r}_\parallel)$. The pattern must be smooth on scales larger than the inter-resonator spacing $a_\text{meta}$ but can vary on scales between $a_\text{meta}$ and $\lambda$.

**Reason.** The phase imprint is the coarse-grained response of the resonator array. If the pattern is too random or too discrete, the effective phase imprint is not a smooth function and the generalized Snell's law breaks down (additional scattering and diffraction emerge).

**Substrate-level meaning.** The metasurface's rule-type discontinuity must be *engineered* in a controlled way. Random or disordered rule-type variations at the interface produce diffuse scattering rather than refraction.

### 6.3 Bounded phase gradient

**Requirement.** $|d\Phi/dx| < (2\pi/\lambda)(n_1 + n_2)$ — equivalently, $\lambda/(2\pi)|d\Phi/dx| < n_1 + n_2$.

**Reason.** When the phase gradient exceeds this bound, the generalized Snell's law has no real-angle solution for $\theta_t$ (transmission is evanescent everywhere) and the metasurface produces no propagating transmitted wave.

**Substrate-level meaning.** The metasurface's engineered tangential momentum transfer is bounded by the wave-vector magnitudes in the two adjacent media. Phase gradients larger than this bound produce evanescent transmission rather than propagating refraction.

### 6.4 Homogenization validity at the interface

**Requirement.** The inter-resonator spacing $a_\text{meta}$ satisfies $a_\text{meta} \ll \lambda$.

**Reason.** The phase imprint $\Phi(\mathbf{r}_\parallel)$ must be a smooth function of position on scales comparable to $\lambda$. For sub-wavelength resonator spacing, the chain averages over the resonator scale and experiences a smooth phase pattern.

**Substrate-level meaning.** The metasurface engineering operates at scales below the chain's probe wavelength. The chain cannot resolve individual resonators; it experiences the cell-averaged phase pattern. This is the metasurface analog of the homogenization regime in the bulk (Memo 2–6).

### 6.5 Resonator response range and bandwidth

**Engineering requirement.** Each resonator must provide the engineered phase response over $[0, 2\pi)$ with sufficient amplitude (transmission close to unity for lossless metasurfaces).

**Bandwidth constraint.** The phase response of each resonator is frequency-dependent (resonant elements have natural resonance frequency $\omega_0$). The metasurface's design $\Phi(\mathbf{r}_\parallel)$ is achieved exactly only at the design frequency; off-resonance operation produces distorted phase patterns.

**Substrate-level meaning.** The metasurface's engineered rule-type discontinuity is *frequency-localized*. The Capasso refraction phenomenon works exactly at the design frequency; broadband metasurfaces require multiple-resonance or geometric-phase designs.

### 6.6 Substrate-level summary of realizability

$$
\boxed{\quad
\text{Metasurface realizability} \;=\; \text{controlled sub-wavelength rule-type discontinuity producing engineered position-dependent phase imprint at design frequency}.
\quad}
$$

These conditions correspond to the engineering reality of Capasso-style metasurfaces: sub-wavelength resonators (e.g., V-shaped antennas, dielectric pillars), deterministic phase patterns, bounded gradient, and operation at the design frequency.

---

## 7. (F) Preparation for Memo 13: Synthesis

The Arc's three precursor derivations are now complete:

### 7.1 Homogenization (Memos 2–6)

Substrate-level effective-medium theory for periodic rule-type microstructures. Derived:
- Multi-scale expansion in $a/\lambda$ (Memo 2).
- Cell problem and averaging operator (Memo 3).
- Effective constitutive relations $\varepsilon_{\mathrm{eff}}^{ij}, \mu_{\mathrm{eff}}^{ij}$ (Memo 4).
- Substrate-level meaning of $\varepsilon, \mu$ as coarse-grained rule-type response (Memo 5).
- Conditions for negative-index media (Pendry 2000): wire-array plasma response + split-ring-resonator magnetic response (Memo 6).

### 7.2 Transformation optics (Memos 7–11)

Substrate-level transformation of effective media under smooth substrate-gradient deformations. Derived:
- Rule-type deformation tensor $D_{ij}$ and Jacobian $J^i{}_j$ (Memo 7).
- Mapping to effective metric $g_{ij} = D_{ij}$ (Memo 8).
- Pendry 2006 spherical cloak as explicit deformation (Memo 9).
- Substrate-level reading of invisibility cloaking as topological exclusion (Memo 10).
- General transformation-optics machinery and physical realizability (Memo 11).

### 7.3 Metasurface boundary conditions (Memo 12)

Substrate-level treatment of discontinuous deformations at interfaces. Derived:
- Metasurface as engineered rule-type discontinuity with phase imprint $\Phi(\mathbf{r}_\parallel)$.
- Generalized Snell's law $n_1\sin\theta_i = n_2\sin\theta_t + (\lambda/2\pi)\,d\Phi/dx$ (Capasso 2011).
- Substrate-level interpretation: chain's tangential momentum adapts to engineered rule-type discontinuity.

### 7.4 What Memo 13 must synthesize

Memo 13 (synthesis) will:

1. **Articulate the unified substrate-level mechanism** that underlies all three closures: substrate-gradient deformations of the rule-type microstructure produce position-dependent effective response, smooth or discontinuous depending on the deformation's regularity.

2. **Map each metamaterial phenomenon** (negative refraction, cloaking, Capasso refraction) to the substrate-level mechanism that produces it. Show that all are different limits of the same underlying substrate-level theory.

3. **Identify the load-bearing substrate primitives** (P-MM-1 through P-MM-6) and how they combine to produce each phenomenon.

4. **Connect to the existing closed walkthroughs**: photonic bandgaps (Bloch theorem walkthrough) for Yablonovitch; the three precursors of this Arc for Pendry and Capasso. The combined inventory enables the public-facing `from_primitives_to_metamaterials_and_photonics.md` walkthrough.

5. **Identify open follow-ons** and the remaining work needed for a complete substrate-level account of the metamaterials and photonics frontier.

---

## 8. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **The metasurface as a codimension-1 engineered rule-type discontinuity** (§2.1, 2.5). FORCED by P-MM-5 (interface rule-type discontinuity primitive).

- **The substrate-level surface polarization $\mathbf{P}_s$ and magnetic surface polarization $\mathbf{M}_s$** as cell-averaged rule-type-alignment shift and rule-type circulation response per unit area (§3.3, 3.4). FORCED by extension of the substrate-level meanings of $\varepsilon$ and $\mu$ from bulk to 2D.

- **The phase-imprint boundary condition** $\psi_2(\mathbf{r}_\parallel, 0^+) = \psi_1(\mathbf{r}_\parallel, 0^-)e^{i\Phi(\mathbf{r}_\parallel)}$ (§3.5). FORCED by the substrate-level meaning of metasurface as engineered phase pattern.

- **The tangential momentum shift** $\mathbf{k}_{\parallel,2} = \mathbf{k}_{\parallel,1} + \nabla_\parallel\Phi$ (§4.3). FORCED by the gradient of the combined phase function at the transmitted side.

- **The generalized Snell's law** $n_1\sin\theta_i = n_2\sin\theta_t + (\lambda/2\pi)d\Phi/dx$ (§5.3). FORCED by tangential-momentum matching + dispersion relations.

- **The generalized law of reflection** $n_1\sin\theta_r = n_1\sin\theta_i + (\lambda/2\pi)d\Phi/dx$ (§5.4). FORCED by the analogous argument for the reflected wave.

- **Anomalous regimes** (no real transmission angle, negative refraction at metasurface) (§5.5). FORCED by the magnitude of $d\Phi/dx$ relative to wave vector magnitudes.

- **Physical-realizability conditions** (§6): sub-wavelength thickness, controlled discontinuity, bounded gradient, homogenization at the interface, resonator response range. FORCED at the structural level by the requirement that the metasurface's boundary condition correctly describes the chain's coarse-grained dynamics.

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Standard tangential-field continuity conditions** $\hat{\mathbf{n}}\times(\mathbf{E}_2 - \mathbf{E}_1) = 0$ etc. (§3.1). Standard EM.

- **Generalized sheet transition conditions (GSTC)** with surface polarization and surface current (§3.2). Standard EM extension; substrate-level interpretation provided.

- **Resonator response mechanisms**: electric dipole, magnetic dipole, geometric (Pancharatnam-Berry) phase (§4.1). Standard EM and quantum-optics machinery; substrate-level interpretation provided.

- **Lorentz-Drude / resonance form for resonator response**: inherited from the bulk theory of Memos 5–6 applied to 2D resonators at the interface.

- **Snell's law and law of reflection derivations from tangential-momentum conservation** (§5.2, 5.3). Standard EM.

### What remains OPEN

- **Detailed substrate-level derivation of specific resonator phase responses** (V-shaped antennas, dielectric pillars, Pancharatnam-Berry resonators). Standard physics provides the form; substrate-level derivation from rule-type-microstructure primitives is OPEN.

- **Broadband metasurfaces**: the design phase imprint $\Phi(\mathbf{r}_\parallel)$ is achieved only at the design frequency. Broadband metasurfaces use multiple resonances or geometric-phase designs; substrate-level treatment of broadband operation is OPEN.

- **Polarization-dependent metasurfaces**: different polarizations encounter different phase imprints. Substrate-level reading of polarization-multiplexed metasurfaces is OPEN.

- **Nonlinear metasurfaces** with intensity-dependent phase response. Substrate-level reading OPEN.

- **Active metasurfaces** with electronically tunable phase imprint. Substrate-level reading OPEN.

- **Coupled-mode metasurfaces** where adjacent resonators couple strongly. The simple phase-imprint treatment assumes decoupled resonators; coupled-resonator metasurfaces require extended treatment.

- **Higher-order diffraction at metasurfaces** with periodic patterns. The phase-imprint formulation gives the dominant diffraction order; higher orders require additional Fourier-series treatment.

- **3D bulk metasurfaces** ("metasurfaces" with finite thickness exhibiting bulk-like behavior). These bridge to bulk metamaterials (Memos 2–6); substrate-level treatment of the bridging regime is OPEN.

- **Time-modulated metasurfaces** with time-varying phase imprint $\Phi(\mathbf{r}_\parallel, t)$. Frequency conversion, non-reciprocal operation. OPEN.

- **Substrate-level derivation of the GSTC from first principles** (rather than inheriting from standard EM). The substrate-level meaning of surface polarization/current is articulated; a fully derived substrate-level statement starting from V1 kernel response is OPEN.

---

## 9. Review and Recommended Next Steps

### Review

Memo 12 has delivered the third and final precursor closure of the Arc:

- **(A) Metasurface as rule-type discontinuity** (§2): codimension-1 engineered rule-type jump with position-dependent shift $\boldsymbol\Delta(\mathbf{r}_\parallel)$ and phase imprint $\Phi(\mathbf{r}_\parallel)$.

- **(B) Jump conditions** (§3): standard tangential continuity modified by surface polarization $\mathbf{P}_s$ and surface current $\mathbf{K}_s$ from the engineered resonators. Substrate-level interpretation as 2D analog of bulk $\varepsilon$ and $\mu$.

- **(C) Phase-imprinting mechanism** (§4): origin of $\Phi$ from electric, magnetic, and geometric resonator responses; substrate-level reading as engineered rule-type re-alignment; tangential momentum shift $\mathbf{k}_{\parallel,2} = \mathbf{k}_{\parallel,1} + \nabla_\parallel\Phi$.

- **(D) Generalized Snell's law** (§5):

$$
n_1 \sin\theta_i = n_2 \sin\theta_t + \frac{\lambda}{2\pi}\frac{d\Phi}{dx},
$$

derived from tangential-momentum matching modified by the phase-imprint gradient. Generalized law of reflection. Anomalous regimes (negative refraction, evanescent transmission). Substrate-level interpretation: refraction is chain's adaptation to engineered rule-type discontinuity.

- **(E) Physical realizability** (§6): sub-wavelength thickness, controlled discontinuity, bounded gradient, homogenization at interface, resonator response range, bandwidth limits.

- **(F) Preparation for Memo 13** (§7): all three precursors now complete (homogenization, transformation optics, metasurface BCs). Memo 13 must synthesize them into a unified substrate-level account.

- **Explicit FORCED / FORM-FORCED-INHERITED / OPEN labeling** (§8).

### Honest scope-limit

Memo 12 introduced no new substrate primitives beyond P-MM-1 through P-MM-6 (Memo 1's inventory). The metasurface treatment is independent of the transformation-optics cluster (Memos 7–11) because the discontinuous-deformation case requires direct interface-condition derivation rather than smooth-Jacobian transformation. The standard EM boundary conditions and GSTC are inherited at form level with substrate-level interpretation provided. No cross-references to other arcs.

The three precursor closures of the Arc are now complete:
- Homogenization cluster (Memos 2–6).
- Transformation-optics cluster (Memos 7–11).
- Metasurface BC closure (Memo 12, this Memo).

### Recommended next steps

In order:

1. **Memo 13 — Synthesis.** Tie the three precursor closures together. Articulate the unified substrate-level mechanism (substrate-gradient deformation of rule-type microstructure, smooth or discontinuous). Map each metamaterial phenomenon (negative refraction, cloaking, generalized Snell refraction) to the substrate-level mechanism that produces it. Identify the load-bearing substrate primitives and the connection to the closed Bloch theorem walkthrough (for Yablonovitch photonic bandgaps). Set up the public-facing walkthrough.

2. **Public-facing walkthrough.** `from_primitives_to_metamaterials_and_photonics.md`. Compose all three precursor closures with the Bloch theorem walkthrough into a unified substrate-level account of the Yablonovitch–Pendry–Capasso cluster. This is the Nobel-relevance deliverable.

3. **Open follow-on items** identified in §8:
   - Substrate-level derivation of specific resonator phase responses (V-antennas, dielectric pillars, Pancharatnam-Berry).
   - Broadband, polarization-multiplexed, nonlinear, active, and time-modulated metasurfaces.
   - Coupled-mode metasurfaces.
   - 3D metasurfaces / bridge to bulk metamaterials.

### Anchor for future memos

The generalized Snell's law $n_1\sin\theta_i = n_2\sin\theta_t + (\lambda/2\pi)d\Phi/dx$ and the substrate-level interpretation of metasurfaces as engineered rule-type discontinuities are standardized for the remainder of the Arc. Memo 13 will integrate this with the homogenization and transformation-optics machinery into a unified substrate-level account.
