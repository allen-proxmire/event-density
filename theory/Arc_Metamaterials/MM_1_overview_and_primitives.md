# Arc Metamaterials — Memo 1: Overview, Roadmap, and Primitives

**Allen Proxmire** · May 2026

*A precursor Arc closing the three derivations required for a full Event Density (ED) walkthrough of Yablonovitch–Pendry–Capasso metamaterials and photonics: substrate-level effective-medium / homogenization theorem, substrate-level transformation optics, and substrate-level metasurface boundary conditions.*

---

## 1. Arc Overview

The Yablonovitch–Pendry–Capasso photonics cluster is one of this year's strongest Nobel-physics contender topic areas. The cluster contains four landmark experimental and theoretical results:

1. **Yablonovitch (1987)** — photonic bandgaps in periodic dielectric structures: frequency ranges in which no electromagnetic mode propagates.
2. **Pendry (2000)** — negative refraction in engineered substructures with simultaneous $\varepsilon < 0$ and $\mu < 0$, producing reversed Snell's law and "perfect lens" sub-wavelength imaging.
3. **Pendry (2006)** — transformation-optics invisibility cloaks: spatial coordinate transformations applied to Maxwell's equations produce effective $\varepsilon(\mathbf{r}), \mu(\mathbf{r})$ tensor fields that route electromagnetic waves around a hidden region.
4. **Capasso (2011, 2016)** — metasurfaces with subwavelength-patterned phase imprints: abrupt rule-type discontinuities at interfaces produce generalized Snell's law and arbitrary wavefront engineering.

The ED framework has, by closed-arc inventory:

- Bloch theorem walkthrough — substrate-level derivation of band structure in periodic rule-type substrates, including band gaps as rule-type incompatibility. This already covers Yablonovitch.
- T17 (gauge-fields-as-rule-type-connection), Klein-Gordon §6 minimal coupling, Aharonov-Bohm walkthrough, DCGT substrate-to-continuum bridge.

What is missing for full FORCED-level walkthrough coverage of Pendry and Capasso:

1. **Substrate-level effective-medium / homogenization theorem.** Derive from substrate primitives how subwavelength rule-type microstructure coarse-grains to macroscopic effective constitutive relations $\mathbf{D} = \varepsilon(\mathbf{r}) \mathbf{E}$ and $\mathbf{B} = \mu(\mathbf{r}) \mathbf{H}$ — including the condition for $\varepsilon_\text{eff} < 0$ and $\mu_\text{eff} < 0$ that produces negative refractive index.

2. **Substrate-level transformation optics.** Derive how substrate-gradient deformations correspond to continuum coordinate transformations on the effective metric of Maxwell's equations, producing the cloaking $\varepsilon, \mu$ tensor field from a substrate-level deformation specification.

3. **Substrate-level metasurface boundary conditions.** Derive the generalized Snell's law $n_1 \sin\theta_i = n_2 \sin\theta_t + (\lambda/2\pi)\, d\Phi/dx$ from substrate primitives plus a sub-wavelength-patterned interface rule-type discontinuity.

This Arc closes all three. The output is three substrate-derived results, each placed on Event Density primitives via DCGT-style multi-scale expansion, with explicit FORCED / INHERITED / OPEN labeling at every step.

### Arc claim

Each of the three precursor derivations is FORCED at the substrate level by composition of: substrate rule-type microstructure (P-MM-1), subwavelength periodicity (P-MM-2), ED-gradient deformation (P-MM-3), channel propagation in structured media (P-MM-4), interface rule-type discontinuity (P-MM-5), and the coarse-graining-window hierarchy $\ell_P \ll a \ll \lambda \ll L$ (P-MM-6). No new substrate primitives are introduced beyond those already in the closed ED-program inventory. The derivations layer cleanly on T17 + Bloch + DCGT machinery.

The substrate-level mechanism, in one sentence: **metamaterials are not "tricking light" but re-sculpting the substrate's rule-type structure that defines what coherent light-like channels can propagate through.**

---

## 2. The Three Closures: What Each Memo Cluster Does

### 2.1 Memos 2–6: Substrate-Level Effective-Medium / Homogenization

The standard physics-level statement: a periodic dielectric medium with unit cell size $a \ll \lambda$ supports propagation of electromagnetic waves with wavelength $\lambda$ as if the medium were a homogeneous bulk with effective constitutive parameters $\varepsilon_\text{eff}$ and $\mu_\text{eff}$ determined by averaging the local $\varepsilon(\mathbf{r}), \mu(\mathbf{r})$ over the unit cell.

The substrate-level statement (forced by Memos 2–6): a periodic rule-type substrate with unit cell size $a \ll \lambda$, where $\lambda$ is the chain's coarse-grained wavelength, coarse-grains via DCGT-style multi-scale expansion to a continuum theory in which the chain's effective propagation rate is the volume-averaged response of the rule-type structure to the imposed gauge field. The averaging operator, cell-problem, and effective constitutive relations are derived inline.

**Coverage of Pendry 2000.** Negative refraction requires simultaneously $\varepsilon_\text{eff} < 0$ and $\mu_\text{eff} < 0$. These are obtained when the substrate's rule-type microstructure includes (i) a wire-array pattern producing plasma-like response in the electric channel below a plasma cutoff frequency, and (ii) a split-ring-resonator pattern producing resonant magnetic response above a magnetic resonance frequency. The two together, in a frequency window between the cutoffs, produce $n_\text{eff} = -\sqrt{|\varepsilon_\text{eff} \mu_\text{eff}|} < 0$. Memos 2–6 derive these conditions from substrate primitives.

### 2.2 Memos 7–11: Substrate-Level Transformation Optics

The standard physics-level statement: Maxwell's equations are form-invariant under coordinate transformations, provided $\varepsilon$ and $\mu$ are reinterpreted as the appropriate tensor density. A coordinate transformation $\mathbf{x}' = \mathbf{f}(\mathbf{x})$ that "expels" a region (mapping a point or disk to a sphere) produces an effective medium with $\varepsilon, \mu$ tensor fields that route waves around the expelled region — a Pendry cloak.

The substrate-level statement (forced by Memos 7–11): a substrate-gradient deformation specified by a smooth rule-type-coordinate map $\mathbf{R}(\mathbf{x}): \mathbf{x} \to \mathbf{R}$ produces, under DCGT coarse-graining, an effective constitutive-tensor field that is the pullback of the original Maxwell structure under the deformation. The cloak's "expulsion" is the substrate-level statement that the rule-type structure has a topologically distinct region (the cloaked interior) excluded from the chain's accessible substrate. Memos 7–11 derive the rule-type deformation tensor, its mapping to the effective metric, and the explicit cloaking transformation.

**Coverage of Pendry 2006.** The cloaking $\varepsilon, \mu$ tensor field is the coarse-grained image of a specific substrate-gradient deformation that expels a spherical region from the chain's accessible rule-type substrate. The cloak is FORCED by the substrate-level deformation; its form is calculable from the deformation specification.

### 2.3 Memo 12: Substrate-Level Metasurface Boundary Conditions

The standard physics-level statement: at a sub-wavelength-patterned interface with position-dependent phase shift $\Phi(\mathbf{x})$, the generalized Snell's law is

$$
n_1 \sin\theta_i - n_2 \sin\theta_t = \frac{\lambda_0}{2\pi}\frac{d\Phi}{dx},
$$

where $\lambda_0$ is the free-space wavelength.

The substrate-level statement (forced by Memo 12): a rule-type discontinuity at an interface, where the chain's identity-alignment basis changes abruptly with a position-dependent phase imprint $\Phi(\mathbf{x})$, generates a transverse-momentum kick equal to the gradient of the phase imprint. The kick is FORCED by the substrate-level continuity condition on the chain's pre-individuation amplitude at the interface. The generalized Snell's law follows.

**Coverage of Capasso 2011, 2016.** Capasso's metasurfaces patternedly imprint phase $\Phi(\mathbf{x})$ across an interface via subwavelength resonators. The substrate-level reading: each subwavelength element is a localized rule-type discontinuity, and the spatial pattern of phase imprints is the spatial pattern of substrate-level rule-type rotations at the interface.

### 2.4 Memo 13: Synthesis

After Memos 2–12, the gap for a full metamaterials walkthrough is closed. Memo 13 articulates the three closures together and points at the natural follow-on: the canonical `from_primitives_to_metamaterials_and_photonics.md` walkthrough that composes all three precursors plus the Bloch-theorem walkthrough (for Yablonovitch's bandgaps) into a single substrate-derived treatment of the Yablonovitch–Pendry–Capasso cluster.

---

## 3. Recommended Sequence

The recommended order of work, designed to maximize structural dependence and minimize re-derivation:

1. **Memos 2–6 first (homogenization).** This is the foundational machinery: averaging operators, cell problems, multi-scale expansion of substrate-level rule-type structures. Once this is in hand, transformation optics builds on the same averaging operator + the additional concept of substrate-gradient deformation.

2. **Memos 7–11 next (transformation optics).** Composes Memos 2–6's averaging operator with a substrate-deformation specification. Cloaking is the canonical application.

3. **Memo 12 (metasurface BCs).** Independent of Memos 2–11 in principle, but conceptually fits after them. Could in principle be done first as a self-contained piece, but the framing benefits from having the bulk effective-medium and transformation-optics machinery already in place.

4. **Memo 13 (synthesis).** After all twelve are done.

5. **`from_primitives_to_metamaterials_and_photonics.md` walkthrough.** Composes everything into a public-facing derivation document.

### Estimated effort

- Memos 2–6: 5 memos, ~300–500 lines each. Substantial derivation work.
- Memos 7–11: 5 memos, ~300–500 lines each. Substantial derivation work.
- Memo 12: 1 memo, ~400–600 lines.
- Memo 13: 1 memo, ~200–300 lines (synthesis).
- Walkthrough: 1 walkthrough, ~700 lines (composition).

Total: ~5000–6500 lines of derivation across the Arc, plus a public walkthrough at the end.

### What's load-bearing in each cluster

- **Memos 2–6 load-bearing piece**: the substrate-level averaging operator. Specifically, the integration over the unit cell with the correct measure — counting-measure on substrate sites, smoothed by the V1 finite-width kernel.
- **Memos 7–11 load-bearing piece**: the rule-type deformation tensor. The substrate-level analog of the diffeomorphism Jacobian, defined as the pushforward of the substrate's rule-type connection under the deformation map.
- **Memo 12 load-bearing piece**: the substrate-level continuity condition on the chain's pre-individuation amplitude at a rule-type discontinuity. Gives momentum-conservation modified by phase-gradient.

---

## 4. The Six Primitives

The Arc requires six substrate primitives. None are new to the broader ED program; each composes from already-closed primitive inventory but is named explicitly here for the Arc's clarity.

### P-MM-1. Substrate rule-type microstructure

A *substrate rule-type microstructure* is a spatial pattern of distinct participation-rule types occupying neighboring substrate regions. At substrate-level position $\mathbf{x}$, the local rule-type label $\tau(\mathbf{x}) \in \mathcal{T}$ specifies which rule-type structure the substrate carries there. The label set $\mathcal{T}$ is finite (discrete substrate types) or continuous (smooth tensor fields), depending on the microstructure being modeled.

**Examples in target experimental systems:**
- *Photonic crystal*: $\tau(\mathbf{x})$ alternates between dielectric ($\varepsilon_1$) and vacuum ($\varepsilon_2$) regions on a lattice.
- *Negative-index metamaterial*: $\tau(\mathbf{x})$ encodes both wire-array (plasma-like electric response) and split-ring-resonator (resonant magnetic response) patterns.
- *Cloaking material*: $\tau(\mathbf{x})$ is the smoothly-varying tensor field that satisfies the cloaking constitutive relations.
- *Metasurface*: $\tau(\mathbf{x})$ is a sub-wavelength-patterned interface label, abrupt in the transverse direction at the interface.

**Substrate-level meaning.** Microstructure is not a physical "material" overlaid on a flat substrate; it is a pattern *of* substrate rule-type identity. At each $\mathbf{x}$, $\tau(\mathbf{x})$ tells us which substrate-level rule structure the chains must follow as they propagate through that region.

**Algebraic structure.** Each rule-type $\tau \in \mathcal{T}$ has its own:
- alignment set $\mathcal{R}_\tau$,
- inner-product structure $\langle \cdot | \cdot \rangle_\tau$,
- evolution operator $H_\tau$ (coarse-grained Hamiltonian).

These vary smoothly or discontinuously with $\mathbf{x}$ according to the microstructure specification.

### P-MM-2. Subwavelength periodicity

The microstructure is *periodic* with unit-cell spacing $\mathbf{a}$: $\tau(\mathbf{x} + \mathbf{a}) = \tau(\mathbf{x})$. The periodicity may be in one, two, or three spatial dimensions.

**Subwavelength condition.** The chain's coarse-grained wavelength $\lambda$ satisfies $\lambda \gg a$. Equivalently, the chain probes the medium on scales much larger than the unit cell.

**Substrate-level meaning.** A subwavelength-periodic microstructure looks, to a chain whose probe scale is $\lambda \gg a$, like a smooth effective medium. The chain cannot resolve the individual unit cells; it experiences only the cell-averaged response.

**Why subwavelength.** When $\lambda \sim a$ (probe at the unit-cell scale), Bragg scattering dominates and the chain sees the medium as a periodic structure, producing photonic bandgaps (already covered by Bloch theorem walkthrough). When $\lambda \gg a$, the chain sees an effective continuum medium (this is the regime homogenization covers).

### P-MM-3. ED-gradient deformation

An *ED-gradient deformation* is a smooth spatial map $\mathbf{R}(\mathbf{x}): \mathbb{R}^3 \to \mathbb{R}^3$ specifying how the substrate's rule-type identity is reparameterized. At substrate-level position $\mathbf{x}$, the chain encounters the rule-type structure that would have been at position $\mathbf{R}(\mathbf{x})$ in the un-deformed substrate.

**Identity deformation.** When $\mathbf{R}(\mathbf{x}) = \mathbf{x}$, no deformation occurs and the substrate is unchanged.

**Cloaking deformation.** A deformation that smoothly expels a region $R < R_1$ to a shell $R_1 < R' < R_2$ produces, at coarse-grained level, the cloaking constitutive-tensor field.

**Substrate-level meaning.** A deformation is not a physical bending of space; it is a substrate-level reassignment of rule-type identity to positions. The chain at $\mathbf{x}$ aligns with whatever rule-type structure $\mathbf{R}(\mathbf{x})$ would have pointed to in the un-deformed substrate.

**Algebraic structure.** The deformation has a Jacobian $\Lambda^i_j(\mathbf{x}) = \partial R^i / \partial x^j$, which we will derive in Memo 8 as the rule-type deformation tensor. The pullback of the substrate's constitutive structure under $\mathbf{R}$ produces the effective-medium constitutive-tensor field.

### P-MM-4. Channel propagation in structured media

A *channel* is the participation pathway through which a chain propagates. A *channel in a structured medium* propagates through a substrate region whose rule-type structure varies via the microstructure $\tau(\mathbf{x})$ or deformation $\mathbf{R}(\mathbf{x})$.

**Coarse-grained wave equation.** The chain's pre-individuation amplitude $\psi(\mathbf{x}, t)$ satisfies a wave equation whose coefficients (effective $\varepsilon, \mu$ or their substrate-level pre-images) depend on position. For a photon-like chain in vacuum at position $\mathbf{x}$:

$$
\nabla \times (\mu^{-1}(\mathbf{x}) \nabla \times \mathbf{E}) - \omega^2 \varepsilon(\mathbf{x}) \mathbf{E} = 0,
$$

with the effective constitutive parameters derived in Memos 2–6 as functions of the microstructure $\tau$ or deformation $\mathbf{R}$.

**Substrate-level meaning.** The chain propagates through varying rule-type identity; its eigenchannel structure adapts to the local rule-type as it traverses the substrate. The substrate-level mechanism is the same as in vacuum propagation (T17 + Klein-Gordon §6 + Bloch eigenchannels), but with the rule-type structure varying in space.

### P-MM-5. Interface rule-type discontinuity

An *interface rule-type discontinuity* is an abrupt change in the substrate's rule-type structure at a (codimension-1) interface. At positions $\mathbf{x}$ with normal coordinate $n$:

- For $n < 0$: substrate carries rule-type $\tau_1(\mathbf{x})$ (e.g., vacuum, with refractive index $n_1$).
- For $n > 0$: substrate carries rule-type $\tau_2(\mathbf{x})$ (e.g., dielectric, with refractive index $n_2$).
- For $n = 0$: the chain's pre-individuation amplitude must satisfy a continuity condition that accounts for any phase imprint $\Phi(\mathbf{x}_\parallel)$ engineered into the interface.

**Phase imprint.** A *metasurface* is an interface with a sub-wavelength-patterned phase imprint $\Phi(\mathbf{x}_\parallel)$. The chain crossing the interface acquires a phase that depends on the transverse position at the crossing. The phase imprint is a substrate-level engineered feature, encoded in the rule-type structure of the sub-wavelength resonators making up the metasurface.

**Substrate-level meaning.** A metasurface is not a passive interface; it is a substrate region where the rule-type identity is engineered to rotate the chain's pre-individuation amplitude by a position-dependent angle as the chain crosses. The continuity condition + phase imprint together force the chain's transverse momentum to acquire a kick $\propto d\Phi/dx_\parallel$.

### P-MM-6. Coarse-graining window $\ell_P \ll a \ll \lambda \ll L$

The Arc operates in a four-scale hierarchy:

- $\ell_P$: substrate-level discreteness scale (Planck-scale microstructure of the V1 kernel).
- $a$: microstructure unit-cell scale (typically nm to μm, depending on the target frequency).
- $\lambda$: chain probe wavelength (typically optical to microwave).
- $L$: macroscopic scale of the experimental setup (typically mm to m).

**Hierarchy.** Each scale separation must satisfy at least a factor of $\sim 10$ for the multi-scale expansion to converge cleanly. Typical metamaterials operate with $a \sim \lambda/10$ and $L \sim 10^3 \lambda$, well within the regime.

**Substrate-level meaning.** The coarse-graining window guarantees that:
- Substrate-level discreteness ($\ell_P$) is below the unit-cell scale ($a$), so the unit cell is a well-defined averaging domain.
- The unit cell is below the chain's probe wavelength ($\lambda$), so the chain sees an averaged effective medium.
- The chain's wavelength is below the experimental scale ($L$), so the effective-medium picture is locally accurate across the experimental geometry.

**Multi-scale expansion.** Each derivation in the Arc uses an asymptotic expansion in small ratios $a/\lambda$ and $\lambda/L$. The leading-order term gives the effective-medium / transformation-optics / metasurface-BC result. Subleading terms are FORM-FORCED-INHERITED corrections at $O(a/\lambda)^2$ or $O(\lambda/L)^2$.

**No new substrate primitives are introduced beyond P-MM-1 through P-MM-6.**

---

## 5. Memo Roadmap

### Memo 2 — Multi-Scale Expansion in Periodic Rule-Type Substrates

Set up the asymptotic expansion machinery. Introduce fast variable $\mathbf{y} = \mathbf{x}/a$ (varies on the unit cell) and slow variable $\mathbf{X} = \mathbf{x}/L$ (varies on the macroscale). Expand the chain's pre-individuation amplitude as $\psi = \psi_0(\mathbf{X}, \mathbf{y}) + (a/\lambda)\psi_1(\mathbf{X}, \mathbf{y}) + \ldots$, with each $\psi_n$ periodic in $\mathbf{y}$. Plug into the wave equation, collect orders in $a/\lambda$, derive the cell problem.

### Memo 3 — The Cell Problem and Averaging Operator

Define the unit-cell averaging operator $\langle \cdot \rangle = (1/|Y|)\int_Y d^3 y\, (\cdot)$. Derive the leading-order cell problem: at fixed $\mathbf{X}$, $\psi_0(\mathbf{X}, \mathbf{y})$ satisfies a periodic eigenvalue problem on the unit cell $Y$. This problem's solution determines the local effective constitutive parameters.

### Memo 4 — Effective Constitutive Relations

Derive $\varepsilon_\text{eff}^{ij}(\mathbf{X})$ and $\mu_\text{eff}^{ij}(\mathbf{X})$ as integrals over the unit cell weighted by the cell-problem solution. Show that the effective parameters are tensor-valued in general (anisotropic if the unit cell lacks isotropic symmetry).

### Memo 5 — Substrate-Level Meaning of $\varepsilon$ and $\mu$

Reinterpret the effective constitutive parameters in substrate-level language. $\varepsilon$ is the cell-averaged rule-type polarizability response to the imposed gauge field; $\mu$ is the cell-averaged rule-type magnetic-response coefficient. Both emerge from coarse-graining of the substrate's microstructure.

### Memo 6 — Conditions for Negative Index (Pendry 2000)

Derive the substrate-level conditions for $\varepsilon_\text{eff} < 0$ and $\mu_\text{eff} < 0$ simultaneously. Wire arrays produce plasma-like electric response with negative $\varepsilon$ below a plasma frequency; split-ring resonators produce resonant magnetic response with negative $\mu$ in a narrow frequency window above a magnetic resonance. The intersection of these two windows is the negative-index regime. Memo 6 derives both microscopic mechanisms from substrate primitives.

### Memo 7 — Rule-Type Deformation Tensor

Define the rule-type deformation tensor as the Jacobian $\Lambda^i_j = \partial R^i / \partial x^j$ of the substrate-gradient deformation. Derive its transformation properties under deformation composition. Show that the substrate's V1 kernel transforms covariantly under deformation.

### Memo 8 — Mapping to Effective Metric

Show that under deformation $\mathbf{R}(\mathbf{x})$, the effective Maxwell structure transforms as $\varepsilon^{ij} \to (\det \Lambda)^{-1} \Lambda^i_k \Lambda^j_l \varepsilon^{kl}$, with the analogous transformation for $\mu^{ij}$. This is the standard transformation-optics formula, derived inline from substrate primitives.

### Memo 9 — The Cloaking Deformation

Specify the cloaking deformation explicitly: a smooth radial map that expels a sphere $R < R_1$ from the chain's accessible substrate by stretching the shell $R_1 \leq R \leq R_2$ to cover $0 \leq R' \leq R_2$. Compute the explicit $\varepsilon, \mu$ tensor fields.

### Memo 10 — Substrate-Level Reading of Invisibility Cloaking

Articulate the substrate-level mechanism: a cloaking deformation creates a topologically distinct region (the cloaked interior) that is excluded from the chain's accessible substrate. The chain's pre-individuation amplitude smoothly avoids the interior because no rule-type structure exists there. The effective $\varepsilon, \mu$ tensor fields are the coarse-grained image of this substrate-level exclusion.

### Memo 11 — Conditions and Limits of Transformation Optics

Enumerate when transformation optics works (smooth deformations within homogenization validity) and when it breaks down (sharp deformations, sub-wavelength deformations, broadband cloaking, magnetic-electric coupling not captured by the standard formulation). Substrate-level reading of each limit.

### Memo 12 — Substrate-Level Metasurface Boundary Conditions

Derive the generalized Snell's law $n_1 \sin\theta_i - n_2 \sin\theta_t = (\lambda_0/2\pi)\, d\Phi/dx$ from substrate primitives. Set up: chain crosses the interface; pre-individuation amplitude must be continuous up to the phase imprint $\Phi(\mathbf{x}_\parallel)$. The tangential-momentum continuity condition is modified by $\partial \Phi/\partial x_\parallel$. Derive the resulting refraction angle. Substrate-level reading.

### Memo 13 — Synthesis

After Memos 2–12, all three precursors are closed. Memo 13 summarizes the closure, articulates how the three results compose with the Bloch theorem walkthrough into a complete substrate-level account of the Yablonovitch–Pendry–Capasso cluster, and points to the next-step deliverable: the public-facing `from_primitives_to_metamaterials_and_photonics.md` walkthrough.

---

## 6. What Is FORCED, What Is Inherited, What Is Open at Arc Level

### FORCED by the substrate ontology (when Memos 2–12 are complete)

- Effective constitutive relations $\varepsilon_\text{eff}(\mathbf{r}), \mu_\text{eff}(\mathbf{r})$ as cell-averaged response of the substrate rule-type microstructure (Memos 2–5).
- Negative-index regime conditions from substrate-level wire-array + split-ring-resonator microstructures (Memo 6).
- Transformation-optics constitutive-tensor transformation under substrate-gradient deformation (Memos 7–8).
- Cloaking $\varepsilon, \mu$ tensor field as coarse-grained image of substrate exclusion deformation (Memos 9–10).
- Generalized Snell's law from substrate-level continuity + phase imprint (Memo 12).

### FORM-FORCED-INHERITED (and re-derived inside the Arc)

- Multi-scale expansion machinery (Memo 2): standard asymptotic analysis re-derived inline.
- Cell problem and averaging-operator definition (Memo 3): standard homogenization theory re-derived inline.
- Maxwell's equations in tensor form: standard EM re-derived as needed.
- Lorentz-Drude oscillator model for wire-array and resonator responses (Memo 6): standard.

### OPEN

- **Tight magnitude bounds on subleading corrections** at $O(a/\lambda)^2$ and $O(\lambda/L)^2$: FORM-FORCED expected; explicit coefficients deferred.
- **Broadband cloaking and dispersion-free transformation optics**: standard physics treats this as fundamentally limited; substrate-level account of why limits exist is OPEN.
- **Non-Hermitian and gain-loss-balanced metamaterials**: requires extension to non-Hermitian substrate-level rule-type structure; substrate-level treatment OPEN.
- **Coupling between effective $\varepsilon$ and $\mu$ at high frequencies**: bianisotropic coupling needs separate substrate-level treatment; OPEN.
- **Quantum metamaterials**: metamaterials operating in the regime where individual photon statistics matter; needs composition with Lindblad walkthrough; OPEN.

---

## 7. Review and Recommended Next Steps

### Review

Memo 1 sets the foundation for the Arc:

- The three closures are identified: homogenization, transformation optics, metasurface BCs.
- The six primitives are defined: substrate rule-type microstructure, subwavelength periodicity, ED-gradient deformation, channel propagation in structured media, interface rule-type discontinuity, coarse-graining-window hierarchy.
- The memo roadmap is laid out: 5 memos for homogenization, 5 for transformation optics, 1 for metasurface BCs, 1 for synthesis.
- FORCED / INHERITED / OPEN labeling at Arc level is set up.

No new substrate primitives are introduced beyond the six listed. All six compose from primitives already in the closed ED-program inventory (chains, bandwidth, polarity, T17 rule-type connection, DCGT coarse-graining).

### Recommended next steps

In order of structural value:

1. **Begin Memo 2 (Multi-Scale Expansion in Periodic Rule-Type Substrates).** The foundational machinery. Once Memo 2 is in hand, Memos 3–6 build on it sequentially.

2. **Memo 3 (Cell Problem and Averaging Operator).** Defines the averaging operator that's used throughout the rest of the homogenization cluster.

3. **Memo 4 (Effective Constitutive Relations).** First substantive derivation.

4. **Memo 5 (Substrate-Level Meaning of $\varepsilon, \mu$).** Substrate-level reading.

5. **Memo 6 (Conditions for Negative Index).** Closes the homogenization cluster with the Pendry 2000 result.

6. **Memos 7–11 (Transformation Optics).** Composes Memos 2–6's machinery with substrate-gradient deformations.

7. **Memo 12 (Metasurface BCs).** Independent of Memos 2–11; can be done first if preferred.

8. **Memo 13 (Synthesis).** After all twelve close.

9. **Public-facing walkthrough.** `from_primitives_to_metamaterials_and_photonics.md` composing all three closures + Bloch theorem walkthrough.

The walkthrough is the Nobel-relevance deliverable. The Arc closes the precursors needed for the walkthrough to be FORCED-level rigorous.

### What this Arc does not cover

- Yablonovitch's photonic bandgaps — already FORCED via the Bloch theorem walkthrough.
- Topological photonics (Haldane-territory Chern insulators) — already FORCED via Photonic Chern walkthrough.
- Synthetic-dimension and Floquet topological photonics — separate cluster, partially covered by Bloch walkthrough.
- Non-Hermitian and PT-symmetric photonics — OPEN, separate arc.

After this Arc closes, three of the four Nobel-relevance photonics areas (Yablonovitch, Pendry, Capasso) will have substrate-level FORCED derivations in the closed inventory. The fourth (topological-photonics / Haldane-territory) is already closed. The Nobel-relevance routing table for photonics is then complete.
