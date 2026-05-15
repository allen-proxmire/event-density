# Memo 11 — General Transformation-Optics Machinery

**Arc Metamaterials, Memo 11 of 13.**
**Allen Proxmire** · May 2026

*Generalize the transformation-optics machinery beyond the spherical cloak of Memo 9 to arbitrary substrate-gradient deformations. Derive the conditions for physical realizability, articulate the interaction with dispersion and homogenization limits, and identify the substrate-level ingredients needed for the metasurface boundary conditions of Memo 12. Close the transformation-optics cluster of the Arc.*

---

## 1. Setup and Notation

A chain (P-MM-4) propagates through a substrate whose rule-type microstructure (P-MM-1) has been re-parameterized via a substrate-gradient deformation (P-MM-3) in the coarse-graining regime $\ell_P \ll a \ll \lambda \ll L$ (P-MM-6).

The previous transformation-optics memos (Memos 7–10) treated:

- The infinitesimal/general substrate-gradient deformation $\mathbf{R}(\mathbf{x}) = \mathbf{x} + \mathbf{u}(\mathbf{X})$ with slow-varying displacement field (Memo 7).
- The mapping to an effective metric $g_{ij}(\mathbf{X}) = D_{ij}(\mathbf{X})$ where $D_{ij}$ is the rule-type deformation tensor (Memo 8).
- The specific spherical cloaking deformation $r' = R_1 + \alpha r$ with $\alpha = (R_2 - R_1)/R_2$ (Memo 9).
- The substrate-level reading of invisibility cloaking as topological exclusion (Memo 10).

This Memo generalizes to *arbitrary* substrate-gradient deformations $\mathbf{x}' = \mathbf{f}(\mathbf{x})$ with no restriction to slow-varying displacement, no restriction to spherical symmetry, and no restriction to identity-near deformations. The transformation-optics machinery applies to any smooth invertible diffeomorphism, subject to the physical-realizability conditions derived in §5 below.

---

## 2. (A) Arbitrary Coordinate Transformations

### 2.1 The general deformation map

A *general substrate-gradient deformation* is a smooth invertible map

$$
\boxed{\quad \mathbf{x}' = \mathbf{f}(\mathbf{x}): \mathbb{R}^d \to \mathbb{R}^d, \qquad x'^i = f^i(\mathbf{x}). \quad}
$$

In the chain's substrate-level perspective: at physical position $\mathbf{x}'$, the chain encounters the rule-type identity that would have been at *virtual position* $\mathbf{x} = \mathbf{f}^{-1}(\mathbf{x}')$ in the un-deformed substrate.

**No assumptions** on:
- Symmetry of the deformation.
- Magnitude of the displacement.
- Smoothness beyond $C^1$ (one continuous derivative — required for the Jacobian to be defined).
- Form of the displacement field (the deformation is not restricted to $\mathbf{f}(\mathbf{x}) = \mathbf{x} + \mathbf{u}(\mathbf{x})$ with small $\mathbf{u}$).

The deformation can be:
- A small displacement (linear elasticity-like limit).
- A large deformation (spherical cloak, carpet cloak, beam-bending transformations).
- A topological deformation (mapping a region to a thin shell, as in cloaks).
- A discontinuous deformation (jumps at interfaces — required for metasurfaces, Memo 12).

The constraint at this stage is *only* smoothness and invertibility on each connected piece of the deformation domain.

### 2.2 The Jacobian of the general deformation

The Jacobian matrix is

$$
\boxed{\quad J^i{}_j(\mathbf{x}) \equiv \frac{\partial f^i(\mathbf{x})}{\partial x^j}, \quad}
$$

a $d \times d$ position-dependent matrix. Components $J^i{}_j$ may have arbitrary magnitude and need not be small.

**Properties of $J$ (when $\mathbf{f}$ is smooth and invertible):**

- $J^i{}_j(\mathbf{x})$ is smooth in $\mathbf{x}$.
- $\det J(\mathbf{x}) \neq 0$ everywhere on the deformation domain (invertibility condition; non-zero determinant for local invertibility by the inverse function theorem).
- The inverse Jacobian $(J^{-1})^i{}_j = \partial f^{-1\,i}/\partial x'^j$ is well-defined and smooth on the image domain.

### 2.3 The rule-type deformation tensor

Define the *rule-type deformation tensor* in the general setting (matching Memos 7–8's definition):

$$
\boxed{\quad D_{ij}(\mathbf{x}') \equiv (J^{-1})^k{}_i(\mathbf{x}')\,(J^{-1})^l{}_j(\mathbf{x}')\,\delta_{kl}. \quad}
$$

The argument $\mathbf{x}'$ on the right side indicates that $J^{-1}$ is evaluated at the physical position $\mathbf{x}'$, where $\mathbf{x}'= \mathbf{f}(\mathbf{x})$ specifies the deformed coordinate.

**Properties of $D_{ij}$:**

- Symmetric in $i, j$.
- Position-dependent (varies with $\mathbf{x}'$).
- Positive-definite when $J$ is invertible with $\det J > 0$ (orientation-preserving deformation).
- Reduces to $\delta_{ij}$ when $\mathbf{f}(\mathbf{x}) = \mathbf{x}$ (no deformation).

### 2.4 Composition of deformations

For two successive deformations $\mathbf{f}_1$ then $\mathbf{f}_2$, the composite is $\mathbf{f}_{12} = \mathbf{f}_2 \circ \mathbf{f}_1$ with Jacobian

$$
J_{12}^{i}{}_j(\mathbf{x}) = J_2^{i}{}_k(\mathbf{f}_1(\mathbf{x}))\,J_1^{k}{}_j(\mathbf{x}).
$$

The composite deformation tensor is

$$
D_{ij}^{12}(\mathbf{x}') = (J_{12}^{-1})^k{}_i (J_{12}^{-1})^l{}_j \delta_{kl},
$$

which is *not* in general $D_{ij}^1 + D_{ij}^2$ — deformations compose multiplicatively at the Jacobian level, not additively at the tensor level.

### 2.5 Substrate-level meaning

The general deformation map $\mathbf{f}(\mathbf{x})$ specifies the substrate's coarse-grained rule-type identity-labeling everywhere in space. At each physical position $\mathbf{x}'$, the chain encounters whatever rule-type structure was at $\mathbf{f}^{-1}(\mathbf{x}')$ in the un-deformed substrate.

Three categories of generic deformations:

- **Identity-preserving deformations** ($\det J > 0$, smooth $J$): standard transformation-optics regime. Effective constitutive tensors are well-defined and finite.
- **Region-collapsing deformations** ($\det J \to 0$ at some surface): a region in physical space corresponds to a lower-dimensional set in virtual space. The cloaking deformation is in this category: the virtual point $r = 0$ maps to the entire physical sphere $r' = R_1$, with $\det J$ singular at $r' = R_1$.
- **Region-expanding deformations** ($\det J \to \infty$ at some surface): a region in physical space corresponds to a higher-dimensional set in virtual space. Less common in practical metamaterials but theoretically possible.

All three categories produce well-defined coarse-grained effective constitutive tensors away from the singular surfaces. At the singular surfaces, regularization is needed (Memo 9 §6, generalized in §5 below).

---

## 3. (B) General Effective Metric

### 3.1 The effective metric in coordinate basis

For the general deformation, the effective metric on the chain's coarse-grained propagation is

$$
\boxed{\quad g_{ij}(\mathbf{x}') = D_{ij}(\mathbf{x}'). \quad}
$$

The inverse metric is

$$
g^{ij}(\mathbf{x}') = \frac{1}{\det J(\mathbf{x}')}\, J^i{}_k(\mathbf{x}')\, J^j{}_l(\mathbf{x}')\, \delta^{kl}.
$$

Note: the Jacobian here is evaluated at the physical position $\mathbf{x}'$, so $J(\mathbf{x}') \equiv J(\mathbf{f}^{-1}(\mathbf{x}'))$ — the Jacobian at the virtual pre-image of $\mathbf{x}'$.

The verification of inverse relationship is exactly as in Memo 8 §3.4: $g^{ij}\,g_{jk} = (1/\det J)\,\delta^i_k$ (off by a determinant factor), corresponding to the non-canonical normalization used throughout this Arc.

### 3.2 The volume element

The metric determinant is $\det g_{ij} = \det D_{ij} = 1/(\det J)^2$, so

$$
\boxed{\quad \sqrt{|g(\mathbf{x}')|} = \frac{1}{|\det J(\mathbf{x}')|}. \quad}
$$

For orientation-preserving deformations ($\det J > 0$): $\sqrt{|g|} = 1/\det J$.

The volume-element factor is the *inverse Jacobian determinant*. Regions where the deformation locally stretches volumes ($\det J > 1$) have smaller effective volume per coordinate unit; regions where the deformation locally compresses volumes ($\det J < 1$) have larger effective volume per coordinate unit.

### 3.3 The covariant Laplace-Beltrami wave equation

The chain's coarse-grained pre-individuation amplitude $\psi_0(\mathbf{x}')$ in the generally-deformed substrate satisfies

$$
\boxed{\quad \frac{1}{\sqrt{|g(\mathbf{x}')|}}\,\partial_{x'^i}\!\left[\sqrt{|g(\mathbf{x}')|}\,g^{ij}(\mathbf{x}')\,\partial_{x'^j}\psi_0(\mathbf{x}')\right] + k_0^{2}\,n^{2}(\mathbf{x}')\,\psi_0(\mathbf{x}') = 0, \quad}
$$

where:
- $g^{ij}(\mathbf{x}')$ and $\sqrt{|g(\mathbf{x}')|}$ are as defined above.
- $n^{2}(\mathbf{x}')$ is the local effective refractive index squared, derived from the deformed constitutive tensors (see §4).
- $k_0 = \omega/c$ is the vacuum wavenumber.

The Laplace-Beltrami operator $\Delta_g = (1/\sqrt{|g|})\partial_i[\sqrt{|g|}g^{ij}\partial_j]$ is coordinate-invariant. Under further changes of variable, the wave equation transforms covariantly.

### 3.4 Geodesic structure

In the high-frequency (eikonal / ray-optics) limit, the chain's coarse-grained trajectory follows geodesics of the effective metric $g_{ij}$. The geodesic equation is

$$
\frac{d^2 x'^i}{d\tau^2} + \Gamma^i_{jk}(\mathbf{x}')\,\frac{dx'^j}{d\tau}\frac{dx'^k}{d\tau} = 0,
$$

where $\tau$ is an affine parameter and $\Gamma^i_{jk}$ are the Christoffel symbols of $g_{ij}$.

For the general deformation, $g_{ij} = D_{ij}$, and the Christoffel symbols are

$$
\Gamma^i_{jk} = \frac{1}{2}g^{il}\big(\partial_j g_{kl} + \partial_k g_{jl} - \partial_l g_{jk}\big).
$$

These determine the chain's coarse-grained path through the deformed substrate.

### 3.5 Substrate-level meaning of the general metric

The effective metric $g_{ij}(\mathbf{x}')$ is the substrate-level *induced geometric structure on the chain's coarse-grained propagation* in the deformed substrate (Memo 8 §4):

- It is *not* spacetime curvature.
- The substrate's V1 kernel propagation rate $c$ is unchanged.
- The chain's local rate of becoming is unchanged.
- The substrate remains structurally flat at sub-microstructural scales.

The effective metric is a coarse-grained spatial-propagation descriptor that captures how the deformation has re-arranged the rule-type microstructure. The chain experiences this descriptor as if propagating through a Riemannian space, but no fundamental geometric structure is involved — only the substrate's rule-type identity-labeling has been re-parameterized.

---

## 4. (C) General Constitutive-Tensor Transformation

### 4.1 The transformation rules

Under the general deformation $\mathbf{f}: \mathbf{x} \mapsto \mathbf{x}'$, the substrate's effective constitutive tensors transform as (Memo 7 §4.2):

$$
\boxed{\quad
\varepsilon'^{ij}(\mathbf{x}') = \frac{1}{\det J(\mathbf{x}')}\, J^i{}_k(\mathbf{x}')\, J^j{}_l(\mathbf{x}')\, \varepsilon^{kl},
\quad}
$$

$$
\boxed{\quad
\mu'^{ij}(\mathbf{x}') = \frac{1}{\det J(\mathbf{x}')}\, J^i{}_k(\mathbf{x}')\, J^j{}_l(\mathbf{x}')\, \mu^{kl}.
\quad}
$$

These are the standard transformation-optics constitutive-transformation rules in their general form. They apply to *any* smooth invertible deformation, subject to the realizability conditions of §5.

### 4.2 Anisotropy from general deformations

Even when the un-deformed substrate is *isotropic* ($\varepsilon^{kl} = \varepsilon_0\delta^{kl}$ and $\mu^{kl} = \mu_0\delta^{kl}$), the deformed tensors are generically anisotropic:

$$
\varepsilon'^{ij}(\mathbf{x}') = \frac{\varepsilon_0}{\det J}\,(JJ^T)^{ij}(\mathbf{x}'),
$$

where $(JJ^T)^{ij} = J^i{}_k J^j{}_l \delta^{kl}$. The tensor $JJ^T$ is symmetric positive-definite (since $J$ is invertible), but generally not proportional to $\delta^{ij}$.

The deformed effective tensor's *anisotropy structure* is determined by the eigenvalue structure of $JJ^T$:

- **Eigenvalues of $JJ^T$**: principal stretches squared. $\lambda_k^2 = $ (stretch factor in direction $\hat{\mathbf{e}}_k$)$^2$.
- **Eigenvectors of $JJ^T$**: principal stretch directions.

If all eigenvalues are equal, $JJ^T = \lambda^2\delta$ and the deformed tensor is isotropic with $\varepsilon' = \varepsilon_0\lambda^2/\det J$. If eigenvalues differ, the deformed tensor is uniaxial (two equal eigenvalues) or biaxial (three distinct eigenvalues).

### 4.3 Inhomogeneity from position-dependent Jacobian

When the Jacobian $J^i{}_j(\mathbf{x}')$ varies with position, the deformed constitutive tensors are *inhomogeneous*: their values depend on $\mathbf{x}'$.

This is the general feature of transformation-optics deformations: spatially-varying deformations produce spatially-varying effective media. The cloaking deformation (Memo 9) is the canonical example.

### 4.4 Bianisotropy from generalized deformations

The standard transformation-optics formulation derived above produces *purely electric and purely magnetic* tensor responses, with no electric-magnetic cross-coupling. This is the *non-bianisotropic* regime.

For *bianisotropic* materials — those with magnetoelectric coupling (e.g., chiral media, moving media, gyrotropic materials) — the deformation rules generalize. The full bianisotropic constitutive relation is

$$
\begin{pmatrix} \mathbf{D} \\ \mathbf{B} \end{pmatrix} = \begin{pmatrix} \varepsilon^{ij} & \xi^{ij} \\ \zeta^{ij} & \mu^{ij} \end{pmatrix} \begin{pmatrix} \mathbf{E} \\ \mathbf{H} \end{pmatrix},
$$

where $\xi^{ij}, \zeta^{ij}$ are magnetoelectric coupling tensors. Under general substrate-gradient deformations, all four tensors $\varepsilon, \mu, \xi, \zeta$ transform via the same Jacobian-based rule:

$$
T'^{ij}(\mathbf{x}') = \frac{1}{\det J}\,J^i{}_k\,J^j{}_l\,T^{kl}, \qquad T \in \{\varepsilon, \mu, \xi, \zeta\}.
$$

If the un-deformed substrate is non-bianisotropic ($\xi = \zeta = 0$), the deformed substrate is also non-bianisotropic. Bianisotropy can only arise from deformation of an already-bianisotropic substrate or from extensions of the transformation-optics machinery (e.g., moving-frame transformations).

### 4.5 Substrate-level meaning

The general constitutive-transformation rules encode how the substrate's coarse-grained rule-type response is re-parameterized under deformation:

- **$J^i{}_k J^j{}_l$ factors**: direction-by-direction stretching and rotation of the rule-type response tensor.
- **$(\det J)^{-1}$ factor**: volume-density compensation. When the deformation locally compresses volumes, the rule-type microstructure density per unit volume is increased; the corresponding response is enhanced.

In substrate-level language: the deformation reshapes the substrate's rule-type response pattern in physical space. The chain experiences the reshaped response as if it were a different effective medium, even though the substrate's underlying rule-type identity content is unchanged.

---

## 5. (D) Conditions for Physical Realizability

A general transformation $\mathbf{x}' = \mathbf{f}(\mathbf{x})$ produces effective constitutive tensors $\varepsilon'^{ij}(\mathbf{x}'), \mu'^{ij}(\mathbf{x}')$ via the rules of §4. For these to correspond to a *physically realizable* metamaterial, the deformation must satisfy several conditions.

### 5.1 Smoothness of $f$

**Requirement.** $f^i(\mathbf{x})$ has at least one continuous derivative ($C^1$) on each connected piece of its domain.

**Reason.** The Jacobian $J^i{}_j = \partial f^i/\partial x^j$ must be well-defined for the constitutive-transformation rules to apply.

**Substrate-level meaning.** The substrate's rule-type identity-labeling must vary smoothly across physical space, at least on scales coarser than the microstructure scale $a$. Discontinuous deformations are treated separately (Memo 12 metasurface boundary conditions).

### 5.2 Boundedness of $J$ and $J^{-1}$

**Requirement.** $J^i{}_j(\mathbf{x})$ and $(J^{-1})^i{}_j(\mathbf{x})$ are bounded almost everywhere on their respective domains.

**Reason.** If $|J|$ diverges, the deformed $\varepsilon'^{ij}$ becomes infinite (via the $(JJ^T)^{ij}$ factor). If $|J^{-1}|$ diverges, the deformed $\varepsilon'^{ij}$ vanishes (via the $1/\det J$ factor, which is $\det J^{-1}$). Both extremes correspond to singular effective media.

In practice, bounded $J$ and $J^{-1}$ together imply $\det J$ is bounded away from $0$ and $\infty$ — the deformation is locally bounded-aspect.

**Substrate-level meaning.** The substrate's rule-type microstructure cannot be infinitely compressed or infinitely diluted at any physical position. Boundedness ensures the effective constitutive tensors are finite and well-defined.

**Exception.** At intentionally engineered boundaries (cloaks, where $\det J \to \infty$ at the inner cloak surface to map a point to a sphere), the deformation is *singular* but the singularity is structurally engineered. Regularization (smooth-cloak approximations with finite-thickness boundary layers) restores boundedness. The Pendry cloak's idealized boundary is the singular limit of a sequence of regularized cloaks.

### 5.3 Positivity of $\det J$

**Requirement.** $\det J(\mathbf{x}) > 0$ everywhere on the deformation domain.

**Reason.** Negative determinant corresponds to orientation-reversal — the deformation flips the substrate's left-handed/right-handed convention. This produces unphysical constitutive tensors (negative diagonal eigenvalues at every position) and is generally not realizable.

**Substrate-level meaning.** The deformation must preserve the substrate's local orientation. Region-reversing deformations are forbidden.

### 5.4 Homogenization regime ($a \ll \lambda$)

**Requirement.** The deformation is smooth on scales comparable to the chain's wavelength $\lambda$: $|\partial J/\partial \mathbf{x}'| \cdot \lambda \ll |J|$.

Equivalently: the deformation's characteristic length scale $L_J = J/|\partial J|$ satisfies $L_J \gg \lambda$.

**Reason.** The homogenization machinery (Memos 2–6) assumes the chain's probe scale $\lambda$ is large compared to the microstructure scale $a$. If the deformation varies on scales comparable to $a$ or $\lambda$, the homogenization assumption breaks down and the effective constitutive tensors no longer correctly describe the chain's coarse-grained dynamics.

**Substrate-level meaning.** The deformation is a *macroscopic* re-parameterization. It does not reach into the microstructure scale itself. Microstructure-scale deformations would entangle with the cell problem and produce more complex effective dynamics.

### 5.5 Absence of singularities except at engineered boundaries

**Requirement.** The deformation has well-defined Jacobian everywhere on the deformation domain *except* possibly at intentionally engineered boundary surfaces.

**Reason.** Generic singularities (e.g., $\det J \to 0$ on a surface other than a cloak's inner boundary) produce singular effective tensors that are difficult or impossible to realize in practice.

**Substrate-level meaning.** Singularities in the deformation correspond to substrate regions where the rule-type identity-labeling becomes degenerate. Engineered singularities at cloak boundaries are acceptable because the substrate-level mechanism (topological exclusion, Memo 10) is well-understood. Generic singularities elsewhere correspond to substrate features that the engineering does not control.

### 5.6 Engineering realizability beyond mathematical requirements

In addition to the mathematical requirements above, *engineering* realizability imposes further constraints:

- **Constitutive-tensor values must be achievable** by available microstructure: typical metamaterials achieve $\varepsilon^{ij}, \mu^{ij}$ in the range $[10^{-2}, 10^{2}]$ in either sign. Extreme values (very large, very small, or strongly negative) require engineered resonant microstructures with narrow operational bandwidths.
- **Spatial resolution must match microstructure scale**: the effective tensor's variation in space must occur on scales accessible to the chosen microstructure spacing $a$.
- **Manufacturing tolerances**: real cloaks suffer from manufacturing imperfections that distort the ideal effective tensors. Substrate-level reading: the cloak's rule-type microstructure has tolerances that propagate to imperfect topological exclusion.

These engineering constraints are not derived from substrate primitives but inherited from the practical limits of metamaterial fabrication.

---

## 6. (E) Dispersion and Bandwidth Limits

### 6.1 Frequency dependence of effective constitutive tensors

The homogenization machinery (Memo 6) produces frequency-dependent effective constitutive tensors when the substrate's microstructure contains resonant elements:

- **Drude dispersion** (wire-array microstructures, Memo 6 §2): $\varepsilon(\omega) = \varepsilon_\infty(1 - \omega_p^2/\omega^2)$.
- **Lorentz dispersion** (split-ring-resonator microstructures, Memo 6 §3): $\mu(\omega) = 1 - F\omega^2/(\omega^2 - \omega_0^2 + i\gamma\omega)$.

When such microstructures are subjected to a transformation-optics deformation, the dispersion propagates through to the deformed effective tensors:

$$
\varepsilon'^{ij}(\mathbf{x}'; \omega) = \frac{1}{\det J(\mathbf{x}')}\,J^i{}_k(\mathbf{x}')\,J^j{}_l(\mathbf{x}')\,\varepsilon^{kl}(\omega).
$$

At each frequency $\omega$, the transformation rules apply with the un-deformed dispersive $\varepsilon^{kl}(\omega)$. The deformed tensors are frequency-dependent in the same way as the un-deformed ones.

### 6.2 Bandwidth limitations on cloaking

The Pendry cloak (Memo 9) requires specific frequency-independent values of $\varepsilon', \mu'$ at every position in the shell. In practice, the underlying microstructure has dispersion, so the cloak achieves its target effective tensors only over a *narrow frequency window* around the resonance frequencies.

The substrate-level reading: a cloak engineered for frequency $\omega_0$ achieves topological exclusion of the cloaked region for chains with $\omega \approx \omega_0$. For chains with $\omega$ far from $\omega_0$, the underlying microstructure does not provide the required dispersive response, and the deformation's effective constitutive tensors differ from the cloak design. The chain at off-resonance frequencies *can partially see* the cloaked region — the topological exclusion is incomplete.

### 6.3 Why broadband cloaking is hard

For broadband cloaking, one would need:
- A microstructure that provides the cloak's $\varepsilon', \mu'$ at every position over a wide range of frequencies.
- This requires *non-dispersive* effective tensors over the operational bandwidth.

Non-dispersive negative $\varepsilon$ or $\mu$ is impossible for passive media (by Kramers-Kronig dispersion relations + causality). Active media (with gain) could in principle achieve broadband negative response, but introduce stability and noise complications.

**Substrate-level reading.** The cloak's idealized topological exclusion at any single frequency $\omega_0$ does not extend to all frequencies because the rule-type microstructure's resonant response is frequency-dependent. The chain's coarse-grained interaction with the cloak depends on its frequency; the cloak engineered at $\omega_0$ provides topological exclusion only for chains with $\omega \approx \omega_0$.

### 6.4 Bandwidth limitations on negative-index media

The same argument applies to negative-index media: the simultaneous negative $\varepsilon, \mu$ regime (Memo 6 §4) exists in a narrow frequency window where both the plasma-like and resonant-magnetic responses are active. Outside this window, one or both responses revert to positive values, and negative refraction disappears.

The substrate-level reading: negative refraction in real materials is a *frequency-localized phenomenon*, valid only where the rule-type microstructure provides simultaneous resonant electric and magnetic responses with appropriate phase relationships.

### 6.5 Interaction with homogenization limits

The homogenization regime requires $\lambda \gg a$ (microstructure scale). If $\lambda \to a$ (chain wavelength comparable to unit cell), the homogenization machinery breaks down:

- Bragg scattering becomes dominant.
- The chain resolves individual unit cells.
- Effective constitutive tensors are replaced by full band-structure analysis.

The substrate-level reading: at the Bragg regime, the chain "sees" the microstructure directly. The transformation-optics machinery — which operates entirely at the homogenized level — does not apply. Cloaks and other transformation-optics devices fail at frequencies where $\lambda$ approaches $a$.

### 6.6 Substrate-level summary of dispersion and bandwidth

$$
\boxed{\quad
\text{Transformation optics works at frequencies where: (i) the microstructure provides the required } \varepsilon', \mu', \text{ (ii) homogenization is valid (}\lambda \gg a\text{), and (iii) no dispersive resonance destabilizes the engineered response.}
\quad}
$$

Outside these conditions, the transformation-optics machinery breaks down. The substrate-level mechanism (re-parameterization of rule-type identity-labeling) is general, but the *coarse-grained effective description* (effective $\varepsilon, \mu$ tensors and the chain's response to them) has limited frequency validity.

---

## 7. (F) Time-Dependent Transformations

### 7.1 The general time-dependent deformation

For static metamaterials, the deformation $\mathbf{f}(\mathbf{x})$ is time-independent. For dynamic metamaterials, the deformation can be time-dependent:

$$
\mathbf{x}' = \mathbf{f}(\mathbf{x}, t).
$$

The time dependence introduces:
- A time-dependent Jacobian $J^i{}_j(\mathbf{x}, t)$.
- A time-dependent rule-type deformation tensor $D_{ij}(\mathbf{x}', t)$.
- Time-dependent effective constitutive tensors $\varepsilon'^{ij}(\mathbf{x}', t), \mu'^{ij}(\mathbf{x}', t)$.

The transformed wave equation includes time-derivative terms from the time-dependent metric and constitutive tensors.

### 7.2 Spacetime-modulated metamaterials

A *spacetime-modulated metamaterial* has $\varepsilon'^{ij}, \mu'^{ij}$ that vary both in space and in time. Such media can produce effects analogous to:

- **Non-reciprocal propagation**: time-modulated index gradients break time-reversal symmetry, enabling one-way propagation.
- **Frequency conversion**: time-periodic modulation up- or down-converts incident chain frequencies.
- **Effective rotation**: time-rotating constitutive tensors mimic gyrotropic response.

The substrate-level reading: time-dependent deformations re-parameterize the substrate's rule-type identity-labeling dynamically. The chain experiences the deformation's evolution as time-varying effective constitutive tensors.

### 7.3 Constraints on time-varying cloaks

Time-varying cloaks face additional constraints beyond static cloaks:

- **Causality**: the deformation's time dependence must respect causality. The effective tensors at time $t$ cannot depend on the future deformation specification.
- **Energy conservation under modulation**: time-modulated tensors can absorb or emit energy from the modulation source. This complicates the cloak's energy-flow analysis.
- **Adiabaticity**: when the deformation varies slowly compared to the chain's propagation time, the chain experiences a quasi-static cloak. Rapid modulation breaks adiabaticity and produces additional scattering.

### 7.4 Substrate-level meaning of time-dependent deformations

A time-dependent substrate-gradient deformation re-parameterizes the substrate's rule-type identity-labeling as a function of *time*. The substrate's rule-type assignments evolve dynamically; the chain experiences this evolution as a time-varying effective medium.

The substrate-level mechanism: at each time $t$, the substrate's rule-type microstructure occupies a configuration specified by $\mathbf{f}(\mathbf{x}, t)$. The chain's coarse-grained dynamics integrates the time-varying configuration over its propagation time. For slow modulation, the chain experiences an adiabatic sequence of effective media; for fast modulation, the chain experiences strong time-dependent scattering.

### 7.5 Open extensions

Time-dependent transformation optics is an active research area with substrate-level reading still under development. The OPEN extensions include:

- **Causal time-modulated cloaks**: cloaks that can be "turned on" or "turned off" without violating causality.
- **Optical isolators based on time modulation**: one-way propagation from time-asymmetric deformations.
- **Time-reversal mirrors**: spacetime configurations that reverse the chain's coarse-grained trajectory.
- **Substrate-level reading of Floquet-mode physics in time-periodic metamaterials**.

These are flagged OPEN for future work; the present Memo establishes the structural form but does not pursue detailed derivations.

---

## 8. (G) Prepare for Memo 12: Discontinuous Transformations

Memo 12 will treat *metasurfaces* — substrate regions where the rule-type identity-labeling has an *abrupt jump* at a codimension-1 interface (P-MM-5).

### 8.1 Why metasurfaces require separate treatment

The smooth-deformation machinery of Memos 7–11 assumes $\mathbf{f}(\mathbf{x})$ is smooth ($C^1$). Metasurfaces violate this: at the metasurface, $\mathbf{f}$ is discontinuous in the transverse direction (different rule-type pattern on opposite sides of the interface). The Jacobian is undefined at the interface; the constitutive tensors are not well-defined there.

The metasurface's effect on chain propagation cannot be captured by the smooth-deformation effective constitutive tensors alone. Instead, the metasurface introduces a *boundary condition* on the chain's pre-individuation amplitude at the interface.

### 8.2 The substrate-level setup for Memo 12

Memo 12 treats:

- An interface separating medium 1 ($r < 0$) from medium 2 ($r > 0$, with $r$ the normal coordinate).
- A position-dependent phase imprint $\Phi(\mathbf{r}_\parallel)$ that varies along the interface in the transverse direction $\mathbf{r}_\parallel$.
- The phase imprint represents a sub-wavelength-patterned metasurface that adds a position-dependent phase shift to chains crossing the interface.

The chain's pre-individuation amplitude must satisfy:

- **Continuity in the transverse direction**: $\psi_2(\mathbf{r}_\parallel, 0^+) = \psi_1(\mathbf{r}_\parallel, 0^-)\,e^{i\Phi(\mathbf{r}_\parallel)}$.
- **Tangential-wavevector continuity modified by phase gradient**: the standard Snell's law generalizes to include the gradient of $\Phi$.

The resulting *generalized Snell's law* is

$$
n_1\sin\theta_i - n_2\sin\theta_t = \frac{\lambda_0}{2\pi}\,\frac{d\Phi}{dx_\parallel},
$$

with $\lambda_0$ the free-space wavelength.

### 8.3 What Memo 12 will derive

- The substrate-level mechanism for phase imprint: how a sub-wavelength-patterned metasurface produces a position-dependent rule-type discontinuity.
- The substrate-level continuity condition on the chain's pre-individuation amplitude at the interface.
- The generalized Snell's law from substrate primitives.
- The substrate-level reading of Capasso-style metasurface phase engineering.

This is the third precursor closure of the Arc, after the homogenization cluster (Memos 2–6) and the transformation-optics cluster (Memos 7–11).

### 8.4 Substrate-level meaning of the transition

The transformation-optics machinery (Memos 7–11) treats *smooth* substrate-gradient deformations. The metasurface (Memo 12) treats *discontinuous* substrate-gradient deformations at codimension-1 interfaces. Together, the two cover the full range of substrate-level deformation phenomena:

- **Smooth deformations**: produce position-dependent effective constitutive tensors (Memos 7–11).
- **Discontinuous deformations at interfaces**: produce jump boundary conditions on the chain's amplitude (Memo 12).

The substrate-level mechanism is the same in both cases: the substrate-gradient deformation re-parameterizes the rule-type identity-labeling. The mathematical machinery differs because smooth deformations admit a local Jacobian while discontinuous ones do not.

---

## 9. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **The general deformation map $\mathbf{f}(\mathbf{x})$ and its Jacobian $J^i{}_j = \partial f^i/\partial x^j$** (§2.1, 2.2). FORCED by P-MM-3 (substrate-gradient deformation primitive) generalized beyond identity-near deformations.

- **The general rule-type deformation tensor $D_{ij} = (J^{-1})^k{}_i (J^{-1})^l{}_j \delta_{kl}$** (§2.3). FORCED by extension of Memo 7's construction.

- **The general effective metric $g_{ij}(\mathbf{x}') = D_{ij}(\mathbf{x}')$ and volume element $\sqrt{|g|} = 1/\det J$** (§3). FORCED by the construction of the Laplace-Beltrami wave equation for the deformed substrate.

- **The general constitutive-tensor transformation rules** (§4.1). FORCED by the tensor transformation properties of $\mathbf{E}, \mathbf{D}$ + invariance of the constitutive relations under change of variables.

- **Anisotropy and inhomogeneity arising from general deformations** (§4.2, 4.3). FORCED by the position-dependent and not-isotropic Jacobian.

- **Bianisotropy transformation rules** (§4.4). FORCED by extension of the tensor transformation rules to magnetoelectric coupling tensors.

- **The realizability conditions** smoothness, boundedness, positive determinant, homogenization regime, absence of unintentional singularities (§5). FORCED at the structural level by the requirements that the constitutive tensors be well-defined and finite.

- **Frequency dependence of deformed tensors when the un-deformed substrate is dispersive** (§6.1). FORCED by the transformation rules applied at each frequency.

- **Bandwidth limitations on cloaks and negative-index media** (§6.2–6.4). FORCED by the dispersive nature of the underlying microstructure responses.

- **Breakdown of transformation optics outside the homogenization regime** (§6.5). FORCED by the homogenization machinery's validity boundary.

- **The structural form of time-dependent deformations and their substrate-level meaning** (§7). FORCED by extension of static transformation optics to time-dependent re-parameterization.

- **The need for separate treatment of discontinuous deformations at interfaces** (§8). FORCED by the breakdown of the smooth-Jacobian machinery at metasurfaces.

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Tensor transformation rules** ($\mathbf{E}$ as covariant one-form, $\mathbf{D}$ as contravariant tensor density). Standard differential geometry.

- **Laplace-Beltrami operator and its covariance** (§3.3). Standard.

- **Composition rule for diffeomorphisms** (§2.4). Standard differential geometry.

- **Christoffel symbols and the geodesic equation** (§3.4). Standard Riemannian geometry.

- **Kramers-Kronig relations** (§6.3, implicitly). Standard causality + linearity in EM.

- **Bianisotropic constitutive structure** (§4.4). Standard EM extension.

### What remains OPEN

- **Substrate-level treatment of singular deformations at engineered boundaries**. The Pendry cloak's idealized boundary is the singular limit of regularized cloaks. A full substrate-level derivation of the regularization, including how the chain's amplitude behaves in the finite-thickness boundary layer, is OPEN.

- **Detailed substrate-level account of dispersion in time-dependent transformations**. The interaction between time-varying deformation and frequency-dependent material response is structurally clear but algebraically complex. Detailed examples (frequency-conversion metamaterials, parametric amplifiers) are OPEN.

- **Substrate-level reading of non-reciprocal propagation in time-modulated media**. Time-asymmetric deformations break Lorentz reciprocity; substrate-level mechanism for one-way propagation is OPEN.

- **Bianisotropic transformation optics extensions**: when the un-deformed substrate is itself bianisotropic, the transformation rules involve additional cross-coupling terms. Detailed substrate-level treatment is OPEN.

- **Quantum transformation optics**: single-photon and few-photon dynamics in transformation-optics media. Composition with Lindblad-type machinery required. OPEN.

- **Substrate-level reading of "perfect lens" sub-wavelength imaging**: Pendry 2000's perfect lens uses negative-index slab geometry; substrate-level reading of evanescent-wave amplification is OPEN.

- **Topological deformations and topological metamaterials**: substrate-gradient deformations that change the topology of the chain's accessible substrate (e.g., wormhole-like deformations, multiply-connected substrate regions). Substrate-level reading OPEN.

- **Approximation theory for sub-optimal cloaks**: when the cloak's $\varepsilon, \mu$ deviate from the ideal Pendry formulas, the cloak's invisibility is degraded. Substrate-level reading of the degradation pattern is OPEN.

---

## 10. Review and Recommended Next Steps

### Review

Memo 11 has delivered the general transformation-optics machinery, closing the transformation-optics cluster (Memos 7–11):

- **(A) Arbitrary coordinate transformations** $\mathbf{x}' = \mathbf{f}(\mathbf{x})$ with Jacobian $J^i{}_j = \partial f^i/\partial x^j$, no smallness or symmetry restrictions (§2).

- **(B) General effective metric** $g_{ij}(\mathbf{x}') = D_{ij}(\mathbf{x}')$ with inverse $g^{ij} = (1/\det J)(JJ^T)^{ij}$, volume element $\sqrt{|g|} = 1/\det J$, and Laplace-Beltrami wave equation (§3).

- **(C) General constitutive-tensor transformation rules** $\varepsilon'^{ij}, \mu'^{ij}$ via $(1/\det J)J^i{}_k J^j{}_l$ contraction, with anisotropy and inhomogeneity arising from generic deformations (§4).

- **(D) Conditions for physical realizability**: smoothness, boundedness, positive determinant, homogenization regime, absence of unintentional singularities (§5).

- **(E) Dispersion and bandwidth limits**: how transformation-optics interacts with Drude and Lorentz responses, why broadband cloaks are hard, breakdown outside homogenization regime (§6).

- **(F) Time-dependent transformations**: structural form, spacetime-modulated metamaterials, constraints on time-varying cloaks (§7).

- **(G) Preparation for Memo 12**: discontinuous deformations require separate treatment via interface boundary conditions (§8).

- **Explicit FORCED / FORM-FORCED-INHERITED / OPEN labeling** (§9).

### Honest scope-limit

Memo 11 introduced no new substrate primitives beyond P-MM-1 through P-MM-6 (Memo 1's inventory). The general transformation-optics formulas are derived inline by extending Memo 7–10 to arbitrary deformations. Standard tensor calculus, Riemannian geometry, and EM theory are inherited at form level with substrate-level interpretation provided. No cross-references to other arcs.

The transformation-optics cluster (Memos 7–11) is now closed. Together with the homogenization cluster (Memos 2–6), the substrate-level machinery for *smooth* substrate-gradient deformations is fully established.

### Recommended next steps

In order:

1. **Memo 12 — Substrate-Level Metasurface Boundary Conditions.** Independent line: derive the generalized Snell's law from rule-type discontinuities at interfaces (P-MM-5). This is the third precursor closure of the Arc. Structure:
   - Substrate-level setup of the metasurface as a codimension-1 interface with rule-type discontinuity.
   - Phase-imprinting mechanism: sub-wavelength-patterned interface with $\Phi(\mathbf{r}_\parallel)$.
   - Continuity condition on the chain's pre-individuation amplitude at the interface.
   - Derivation of generalized Snell's law $n_1\sin\theta_i - n_2\sin\theta_t = (\lambda_0/2\pi)\,d\Phi/dx_\parallel$.
   - Substrate-level reading of Capasso-style metasurfaces.

2. **Memo 13 — Synthesis.** Tie all three precursor derivations together (homogenization + transformation optics + metasurface boundary conditions). Summarize the substrate-level mechanism for each metamaterials phenomenon (negative refraction, cloaking, generalized refraction), identify the substrate-level unifying principle, and articulate how the closed Arc enables a complete substrate-level walkthrough of the Yablonovitch–Pendry–Capasso cluster.

3. **Public-facing walkthrough**: `from_primitives_to_metamaterials_and_photonics.md`. Compose all three precursor closures with the Bloch theorem walkthrough (for Yablonovitch photonic bandgaps) into a unified substrate-level account of metamaterials and photonics.

### Anchor for future memos

The general transformation-optics machinery established in Memo 11 — arbitrary deformations, general effective metric and constitutive tensors, physical realizability conditions, dispersion-bandwidth interactions, and time-dependent extensions — is standardized for the remainder of the Arc. Memo 12 will treat the qualitatively different case of discontinuous deformations at metasurfaces. Memo 13 will tie the entire Arc together.
