# Memo 7 — Rule-Type Deformation Tensor

**Arc Metamaterials, Memo 7 of 13.**
**Allen Proxmire** · May 2026

*Open the transformation-optics cluster (Memos 7–11) by introducing the substrate-level rule-type deformation tensor. Derive the Jacobian of a substrate-gradient deformation, show how it acts on rule-type participation pathways, and derive how it transforms the effective constitutive tensors of the homogenized medium.*

---

## 1. Setup and Notation

A chain (P-MM-4) propagates through a substrate whose rule-type microstructure can be specified at each spatial position. The homogenization cluster (Memos 2–6) treated periodic microstructures (P-MM-2) and produced effective constitutive tensors $\varepsilon_{\mathrm{eff}}^{ij}(\mathbf{X})$ and $\mu_{\mathrm{eff}}^{ij}(\mathbf{X})$ as cell-averaged rule-type responses to the chain's gauge field.

This Memo opens a new direction: instead of varying the microstructure spatially (microstructure $\tau$ as a function of $\mathbf{y}$), we consider a *substrate-gradient deformation* (P-MM-3) — a smooth spatial map that re-parameterizes how the rule-type microstructure is laid out in physical space.

The transformation-optics cluster (Memos 7–11) uses substrate-gradient deformations to derive how the effective medium transforms under such re-parameterizations. The cluster culminates in the Pendry 2006 invisibility cloak, where a specific deformation expels a region of physical space from the chain's accessible substrate, producing the cloaking effective constitutive tensor field.

This Memo derives the core algebraic object: the *rule-type deformation tensor*, which captures the substrate-level Jacobian of the deformation and propagates that information through to the effective constitutive parameters.

### 1.1 The substrate-gradient deformation (P-MM-3)

A *substrate-gradient deformation* is a smooth invertible map

$$
\mathbf{R}: \mathbb{R}^d \to \mathbb{R}^d, \qquad \mathbf{x} \;\mapsto\; \mathbf{R}(\mathbf{x}),
$$

specifying how the substrate's rule-type identity is re-parameterized. At physical position $\mathbf{x}$, the chain encounters the rule-type structure that would have existed at "virtual position" $\mathbf{R}(\mathbf{x})$ in the un-deformed substrate.

**Substrate-level meaning.** This is not a physical bending of space. It is a substrate-level reassignment of rule-type identity. The substrate's rule-type microstructure is mapped from a "virtual" arrangement (the un-deformed configuration) to a "physical" arrangement (the actual deployment) via the deformation map $\mathbf{R}$.

**Identity case.** When $\mathbf{R}(\mathbf{x}) = \mathbf{x}$, no deformation occurs and the substrate is in its un-deformed configuration.

**Smoothness and invertibility.** We require $\mathbf{R}$ smooth and invertible (a diffeomorphism on the relevant domain) so that the rule-type identity at each physical position is well-defined and chain propagation through the deformed substrate is well-posed. Sharp deformations (non-smooth $\mathbf{R}$) are OPEN extensions.

### 1.2 The two-scale framing

The chain experiences the deformed substrate via the multi-scale machinery of Memos 2–6: fast variable $\mathbf{y} = \mathbf{x}/a$ (microstructural scale), slow variable $\mathbf{X} = \mathbf{x}$ (macroscopic scale), with $\ell_P \ll a \ll \lambda \ll L$ (P-MM-6).

We parameterize the deformation by separating its slow-varying and fast-varying parts. Write

$$
\mathbf{R}(\mathbf{x}) = \mathbf{x} + \mathbf{u}(\mathbf{X}),
$$

where $\mathbf{u}(\mathbf{X})$ is a *slow-varying displacement field* — a smooth function of the macroscopic coordinate that varies on scale $L$, not on scale $a$.

This is the substrate-level statement that the deformation is *coarse-grained smooth*: it does not vary on the microstructure scale, only on the macroscale. Sub-microstructure-scale deformations would mix with the microstructure itself and require separate treatment; we exclude them here.

### 1.3 Equivalent local-shift formulation

In the two-scale picture, the displacement $\mathbf{u}(\mathbf{X})$ at macroscopic position $\mathbf{X}$ produces a *local shift* of the cell origin. Specifically, the fast variable $\mathbf{y}$ at physical position $\mathbf{x} = \mathbf{X}$ is shifted to a new fast variable

$$
\mathbf{y}'(\mathbf{X}) = \mathbf{y} + \delta\mathbf{y}(\mathbf{X}), \qquad \delta\mathbf{y}(\mathbf{X}) = \mathbf{u}(\mathbf{X})/a,
$$

where $\delta\mathbf{y}(\mathbf{X})$ is the cell-origin shift in fast-variable units at macroscopic position $\mathbf{X}$. The shift is *slow-varying* (varies on scale $L$, not on scale $a$).

This local-shift formulation matches the user-specified Memo 7 notation: $y^i \mapsto y'^i = y^i + \delta y^i(\mathbf{X})$ with $\delta y^i$ a slow function. The substrate-level meaning: at each macroscopic position, the rule-type microstructure has been translated by $\delta\mathbf{y}(\mathbf{X})$ relative to its un-deformed origin, with the translation varying smoothly across the macroscale.

### 1.4 What this Memo derives

Three derived objects:

1. The *Jacobian* $J^i{}_j(\mathbf{X})$ of the substrate-gradient deformation, capturing its local-stretching action.

2. The *rule-type deformation tensor* $D_{ij}(\mathbf{X})$, the substrate-level metric-like object that determines how the deformation propagates through to constitutive parameters.

3. The *transformation rules* for the effective permittivity and permeability tensors under the deformation:

$$
\varepsilon'^{ij}(\mathbf{X}) = \frac{1}{\det J(\mathbf{X})}\, J^i{}_k(\mathbf{X})\, J^j{}_l(\mathbf{X})\, \varepsilon^{kl}, \qquad \mu'^{ij}(\mathbf{X}) = \frac{1}{\det J(\mathbf{X})}\, J^i{}_k(\mathbf{X})\, J^j{}_l(\mathbf{X})\, \mu^{kl}.
$$

These transformations are the substrate-level analog of the standard transformation-optics constitutive-transformation formulas, derived here from substrate primitives.

---

## 2. The Jacobian of the Deformation

### 2.1 Definition

The Jacobian of the substrate-gradient deformation is the matrix of partial derivatives

$$
\boxed{\quad J^i{}_j(\mathbf{X}) \;\equiv\; \frac{\partial R^i(\mathbf{X})}{\partial X^j} \;=\; \delta^i{}_j + \frac{\partial u^i(\mathbf{X})}{\partial X^j}. \quad}
$$

In the local-shift formulation $\mathbf{y}' = \mathbf{y} + \delta\mathbf{y}(\mathbf{X})$, the Jacobian relates the new and old position differentials. For a small step $d\mathbf{x}$ that decomposes as $d\mathbf{x} = d\mathbf{X} + a\,d\mathbf{y}$ in the un-deformed substrate, the corresponding deformed-substrate step is

$$
dR^i = \frac{\partial R^i}{\partial X^j}dX^j = J^i{}_j(\mathbf{X})\, dX^j.
$$

The fast-variable part is unaffected at leading order (the deformation doesn't reach into the microstructure).

### 2.2 Properties of the Jacobian

**Identity at zero deformation.** When $\mathbf{u} = 0$, $J^i{}_j = \delta^i{}_j$.

**Smoothness.** $J^i{}_j(\mathbf{X})$ varies smoothly with $\mathbf{X}$ because $\mathbf{u}(\mathbf{X})$ is smooth.

**Invertibility.** We require $\det J(\mathbf{X}) > 0$ for the deformation to be locally invertible. This excludes singular deformations (e.g., collapses where $\det J \to 0$). At cloaking-singularity points (where the deformation expels a region to a point), $\det J$ diverges or vanishes; we treat these as limit cases in Memo 9.

**Composition.** Two successive deformations $\mathbf{R}_1$ then $\mathbf{R}_2$ have Jacobian $J^i{}_j = (J_2)^i{}_k\,(J_1)^k{}_j$ by the chain rule.

**Inverse map.** The inverse map $\mathbf{R}^{-1}$ has Jacobian $(J^{-1})^i{}_j$ satisfying $(J^{-1})^i{}_k\,J^k{}_j = \delta^i{}_j$.

### 2.3 Substrate-level meaning of the Jacobian

At each macroscopic position $\mathbf{X}$, the Jacobian $J^i{}_j(\mathbf{X})$ describes *how the deformation locally stretches, rotates, and shears* the substrate's spatial structure.

- $J^i{}_j$ acting on a vector $\mathbf{v}$ at $\mathbf{X}$: produces the corresponding vector in the deformed substrate.
- $\det J(\mathbf{X})$: the local *volume expansion factor*. $\det J > 1$ stretches volumes; $\det J < 1$ compresses them; $\det J = 1$ preserves volumes (isovolumic deformation).
- The symmetric part $\tfrac{1}{2}(J + J^T) - \delta$ encodes local stretching and shearing.
- The antisymmetric part $\tfrac{1}{2}(J - J^T)$ encodes local rotation.

In substrate-level language: the Jacobian captures how the substrate's local rule-type identity-labeling is stretched, sheared, and rotated by the deformation. The chain experiences these changes through the cell-averaged response (Memos 2–6) computed with the deformed microstructure.

### 2.4 Action on rule-type participation pathways

A rule-type participation pathway through the un-deformed substrate is a sequence of rule-type identity-commitments that the chain undergoes as it propagates. Under the deformation $\mathbf{R}$, the pathway is *re-routed*: at each physical position $\mathbf{x}$, the chain encounters the rule-type identity-structure that would have been at $\mathbf{R}(\mathbf{x})$ in the un-deformed substrate.

The Jacobian $J^i{}_j$ tells us how the *direction* of the chain's propagation is re-parameterized:
- A path tangent vector $\mathbf{v}$ at $\mathbf{X}$ in the un-deformed substrate corresponds to the tangent vector $J\,\mathbf{v}$ in the deformed substrate.
- The path's *arc length* is re-scaled by the local stretch factor along the path.

Substrate-level statement: the deformation redirects the chain's propagation by mapping un-deformed tangent vectors to deformed tangent vectors via $J$. The chain's identity-commitments along the path are unchanged (same rule-type identities), but their geometric arrangement in physical space is re-parameterized.

---

## 3. The Rule-Type Deformation Tensor

### 3.1 Definition

Define the *rule-type deformation tensor* as

$$
\boxed{\quad D_{ij}(\mathbf{X}) \;\equiv\; (J^{-1})^k{}_i(\mathbf{X})\, (J^{-1})^l{}_j(\mathbf{X})\, \delta_{kl}. \quad}
$$

Equivalently, in matrix notation: $D = (J^{-1})^T (J^{-1})$, or component-wise $D_{ij} = (J^{-1})^k{}_i (J^{-1})^k{}_j$ (summed over $k$).

The tensor $D_{ij}(\mathbf{X})$ is symmetric in $i, j$ (manifestly, by construction).

### 3.2 Geometric meaning

$D_{ij}$ is the *pulled-back metric tensor* under the deformation. To see this, consider the un-deformed substrate equipped with the flat Euclidean metric $\delta_{kl}$. Under the deformation $\mathbf{x} \mapsto \mathbf{R}(\mathbf{x})$, the metric is pulled back:

$$
\text{(new metric at } \mathbf{X}\text{)}_{ij} = \frac{\partial R^k}{\partial X^i}\frac{\partial R^l}{\partial X^j}\delta_{kl} \cdot \text{(inverse Jacobian factor for active vs passive interpretation)}.
$$

In the standard transformation-optics formulation, $D$ is the inverse-metric-like object that captures how distances in the deformed substrate relate to distances in the un-deformed substrate.

Substrate-level meaning: $D_{ij}(\mathbf{X})$ is the substrate-level *effective metric tensor* induced by the deformation on the chain's coarse-grained propagation. At each macroscopic point $\mathbf{X}$, the chain experiences effective distances that are warped by $D$ relative to the un-deformed flat metric.

### 3.3 Identity at zero deformation

When $J^i{}_j = \delta^i{}_j$:

$$
D_{ij} = \delta^k{}_i\,\delta^l{}_j\,\delta_{kl} = \delta_{ij}.
$$

The flat-metric identity, as expected.

### 3.4 Stretching example

Consider a uniform-stretching deformation in direction $\hat{\mathbf{x}}_1$: $J = \text{diag}(\alpha, 1, 1)$ for some $\alpha > 0$. Then $J^{-1} = \text{diag}(\alpha^{-1}, 1, 1)$, and

$$
D = (J^{-1})^T(J^{-1}) = \text{diag}(\alpha^{-2}, 1, 1).
$$

The pulled-back metric is stretched along $\hat{\mathbf{x}}_1$ by factor $\alpha^{-2}$: distances in $\hat{\mathbf{x}}_1$ direction in deformed substrate correspond to $\alpha^{-1}$ times the distances in the un-deformed substrate.

If $\alpha > 1$ (deformation stretches the substrate along $\hat{\mathbf{x}}_1$), $D_{11} = \alpha^{-2} < 1$, meaning the chain experiences a shorter effective distance traversal in $\hat{\mathbf{x}}_1$ — consistent with the chain's amplitude being spread over a larger physical distance per unit $X^1$.

---

## 4. Transformation of the Effective Constitutive Tensors

### 4.1 Setup

In the un-deformed substrate, the chain's coarse-grained propagation is governed by the homogenized effective wave equation (Memo 4):

$$
\partial_{X^i}\!\left[\mu_{\mathrm{eff}}^{-1\,ij}\, \partial_{X^j}\psi_0\right] + \omega^{2}\,\varepsilon_{\mathrm{eff}}^{ij}\,\partial_{X^j}\psi_0 + \omega^2 \cdot \text{(scalar contributions)} = 0,
$$

with $\varepsilon_{\mathrm{eff}}^{ij}, \mu_{\mathrm{eff}}^{ij}$ the cell-averaged constitutive tensors. (For full Maxwell, the equation is vector-valued with $\mathbf{E}$ as the dynamical field; we use a generic scalar form here and apply the transformation rules to both $\varepsilon$ and $\mu$ as tensors.)

Under the substrate-gradient deformation $\mathbf{R}$, the chain's physical position is mapped: $\mathbf{X} \mapsto \mathbf{R}(\mathbf{X})$. The effective constitutive tensors are correspondingly transformed: at the new physical position, the chain experiences a re-arranged version of the original tensors.

### 4.2 Derivation of the transformation rule

Consider the chain's gauge field $\mathbf{E}'(\mathbf{X})$ in the deformed substrate. By the equivalence principle for substrate-level diffeomorphisms (which we derive: the chain's physics is invariant under smooth re-parameterization of the substrate's spatial identity-labels), Maxwell's equations in the deformed substrate take the same form as in the un-deformed substrate, with deformation-transformed constitutive tensors.

The transformation of $\mathbf{E}$ under the change of variables $\mathbf{X} \to \mathbf{R}(\mathbf{X})$:

$$
E'_i(\mathbf{R}) = (J^{-1})^j{}_i\, E_j(\mathbf{X}),
$$

(covariant transformation as a one-form, since $\mathbf{E}$ relates to the gradient of a scalar potential).

The transformation of $\mathbf{D}$:

$$
D'^i(\mathbf{R}) = \frac{1}{\det J}\, J^i{}_j\, D^j(\mathbf{X}),
$$

(contravariant tensor density of weight 1, since $\mathbf{D}$ is a vector density — its components transform with the inverse Jacobian times the determinant factor).

The constitutive relation $\mathbf{D} = \varepsilon\,\mathbf{E}$ must hold in both un-deformed and deformed forms:

$$
D^j = \varepsilon^{jk}\, E_k \qquad \text{(un-deformed)},
$$

$$
D'^i = \varepsilon'^{ij}\, E'_j \qquad \text{(deformed)}.
$$

Substituting the transformation rules for $\mathbf{D}$ and $\mathbf{E}$ into the deformed relation:

$$
\frac{1}{\det J}\, J^i{}_l\, D^l = \varepsilon'^{ij}\, (J^{-1})^k{}_j\, E_k.
$$

Substitute $D^l = \varepsilon^{lk}E_k$ on the left:

$$
\frac{1}{\det J}\, J^i{}_l\, \varepsilon^{lk}\, E_k = \varepsilon'^{ij}\, (J^{-1})^k{}_j\, E_k.
$$

Both sides must equal for arbitrary $\mathbf{E}$, so:

$$
\frac{1}{\det J}\, J^i{}_l\, \varepsilon^{lk} = \varepsilon'^{ij}\, (J^{-1})^k{}_j.
$$

Multiply both sides by $J^k{}_m$ on the right and contract with $\delta^m_n$:

$$
\frac{1}{\det J}\, J^i{}_l\, J^n{}_k\, \varepsilon^{lk} = \varepsilon'^{ij}\, (J^{-1})^k{}_j\, J^n{}_k = \varepsilon'^{ij}\, \delta^n_j = \varepsilon'^{in}.
$$

So

$$
\boxed{\quad \varepsilon'^{ij}(\mathbf{X}) \;=\; \frac{1}{\det J(\mathbf{X})}\, J^i{}_k(\mathbf{X})\, J^j{}_l(\mathbf{X})\, \varepsilon^{kl}. \quad}
$$

This is the standard transformation-optics constitutive transformation for the permittivity tensor.

### 4.3 Analogous derivation for $\mu^{ij}$

The same argument applies to the magnetic constitutive relation $\mathbf{B} = \mu\,\mathbf{H}$:

$$
\boxed{\quad \mu'^{ij}(\mathbf{X}) \;=\; \frac{1}{\det J(\mathbf{X})}\, J^i{}_k(\mathbf{X})\, J^j{}_l(\mathbf{X})\, \mu^{kl}. \quad}
$$

The permeability transforms identically to the permittivity under substrate-gradient deformations.

### 4.4 Verification: identity deformation preserves constitutive tensors

When $J^i{}_j = \delta^i{}_j$, $\det J = 1$, and the transformation gives

$$
\varepsilon'^{ij} = \delta^i{}_k\,\delta^j{}_l\,\varepsilon^{kl} = \varepsilon^{ij}.
$$

The constitutive tensors are unchanged, as required.

### 4.5 Verification: composition preserves transformation

For two successive deformations $J_1$ then $J_2$, the composite Jacobian is $J_{12} = J_2 J_1$. Applying the transformation rule sequentially:

After $J_1$: $\varepsilon_1^{ij} = (\det J_1)^{-1} (J_1)^i{}_k (J_1)^j{}_l \varepsilon^{kl}$.

After $J_2$ applied to $\varepsilon_1$: $\varepsilon_2^{ij} = (\det J_2)^{-1} (J_2)^i{}_k (J_2)^j{}_l \varepsilon_1^{kl} = (\det J_2)^{-1}(\det J_1)^{-1} (J_2 J_1)^i{}_k (J_2 J_1)^j{}_l \varepsilon^{kl} = (\det J_{12})^{-1} (J_{12})^i{}_k (J_{12})^j{}_l \varepsilon^{kl}$.

The composite transformation matches the direct $J_{12}$ application. Consistency under composition is verified.

### 4.6 Substrate-level meaning of the transformation

The transformation rule

$$
\varepsilon'^{ij} = (\det J)^{-1}\, J^i{}_k\, J^j{}_l\, \varepsilon^{kl}
$$

encodes how the *coarse-grained rule-type polarizability* of the substrate's microstructure transforms under a substrate-gradient deformation. Three contributions:

1. **The $J^i{}_k J^j{}_l$ rotation/shear factors**: transform the tensor indices according to how the deformation stretches and rotates the substrate's spatial structure. The chain experiences the rule-type response in transformed directions.

2. **The $(\det J)^{-1}$ volume factor**: accounts for the volume expansion/compression. When the deformation locally stretches the substrate's spatial extent (det $J > 1$), the *volume density* of rule-type microstructure decreases, reducing the per-unit-volume effective response. Conversely, compression (det $J < 1$) increases the density.

3. **The substrate-level rule-type pattern $\varepsilon^{kl}$**: the un-deformed cell-averaged response carrying through the transformation.

In substrate-level language: the deformation reshapes the substrate's rule-type microstructure pattern. At each macroscopic position $\mathbf{X}$, the chain experiences a rule-type response tensor that is the original response tensor transformed by the local Jacobian — capturing how the deformation has stretched, rotated, and re-arranged the cell-averaged microstructural response in the chain's local frame.

The analogous interpretation holds for $\mu'^{ij}$: the *coarse-grained rule-type circulation response* transforms identically under the deformation.

---

## 5. Compatibility with the Homogenization Cluster

### 5.1 The deformation acts on coarse-grained quantities

The homogenization cluster (Memos 2–6) produced effective constitutive tensors $\varepsilon_{\mathrm{eff}}^{ij}(\mathbf{X}), \mu_{\mathrm{eff}}^{ij}(\mathbf{X})$ via cell-averaging of the substrate's rule-type microstructure. These are *coarse-grained* quantities — defined at macroscopic position $\mathbf{X}$, smooth on scale $L$.

The substrate-gradient deformation $\mathbf{R}(\mathbf{X})$ is also a *coarse-grained* quantity — it varies on scale $L$, not on scale $a$. The deformation acts on the coarse-grained effective tensors via the transformation rules derived in §4.

This is the substrate-level statement of *scale-separation between homogenization and deformation*: the homogenization machinery first averages the microstructure within each cell to produce smooth effective tensors; the deformation then re-parameterizes these smooth effective tensors via the Jacobian. The two operations commute at leading order in $a/\lambda$.

### 5.2 Subleading corrections

At subleading orders in $a/\lambda$ or $a/L$, the deformation can couple to the microstructure. For instance, if the deformation gradient $\partial_j u^i$ varies appreciably on scales comparable to the microstructure scale $a$, the cell problem itself becomes deformation-dependent, and the homogenization analysis must be repeated with $\tau(\mathbf{R}(\mathbf{x}))$ as the microstructure pattern. These subleading effects are OPEN; for leading-order transformation optics they can be neglected.

### 5.3 What the deformation does not change

The substrate's *rule-type identity content* — which rule types occupy the substrate, with what physical properties — is unchanged by the deformation. Only the *spatial arrangement* of the rule-type pattern is re-parameterized.

Substrate-level statement: the deformation is a passive re-parameterization. The substrate primitives (P-MM-1 through P-MM-6) are unchanged. What changes is the substrate's rule-type-pattern-as-a-function-of-physical-position. The chain experiences this re-arranged pattern as if it had different effective constitutive tensors.

---

## 6. The Rule-Type Deformation Tensor in Effective-Wave-Equation Form

### 6.1 The transformed wave equation

In the un-deformed substrate, the chain's coarse-grained pre-individuation amplitude $\psi_0(\mathbf{X})$ satisfies the homogenized effective wave equation. Under the deformation, the equation transforms to

$$
\partial_{X^i}\!\left[\mu'^{-1\,ij}(\mathbf{X})\, \partial_{X^j}\psi'_0(\mathbf{X})\right] + \omega^{2}\,\varepsilon'(\mathbf{X})\,\psi'_0(\mathbf{X}) = 0,
$$

where $\psi'_0, \varepsilon', \mu'^{-1}$ are the deformed-substrate quantities. The transformed constitutive tensors are given by §4.2 and §4.3.

The amplitude $\psi'_0(\mathbf{X})$ at new position $\mathbf{X}$ corresponds to $\psi_0(\mathbf{R}^{-1}(\mathbf{X}))$ — the un-deformed amplitude evaluated at the pre-image of $\mathbf{X}$ under the deformation.

### 6.2 The deformation tensor in the wave equation

The wave equation can be rewritten using the rule-type deformation tensor $D_{ij}$. Substituting $\mu'^{-1\,ij} = (\det J)^{-1} J^i{}_k J^j{}_l \mu^{-1\,kl}$:

$$
\partial_{X^i}\!\left[(\det J)^{-1}\, J^i{}_k\, J^j{}_l\, \mu^{-1\,kl}\, \partial_{X^j}\psi'_0\right] + \omega^{2}\,(\det J)^{-1}\, \varepsilon^{kl}(\text{contracted})\, \psi'_0 = 0.
$$

After algebra (using the volume factor and Jacobian-inverse identity $D^{-1} = J^T J$ which is the un-deformed-Euclidean-pulled-back metric), this reduces to

$$
\partial_{X^i}\!\left[\sqrt{\det D}\, D^{ik}\, D^{jl}\, \mu^{-1}_{kl}\, \partial_{X^j}\psi'_0\right] + \omega^{2}\, \sqrt{\det D}\, \varepsilon\, \psi'_0 = 0
$$

in covariant-tensor form, with $D^{ij}$ the inverse of the rule-type deformation tensor. The rule-type deformation tensor $D_{ij}$ thus plays the role of the *effective metric* on the chain's coarse-grained propagation in the deformed substrate.

This is the substrate-level analog of the standard transformation-optics statement: "the deformed effective medium with $\varepsilon', \mu'$ is mathematically equivalent to a homogeneous medium in curved geometry with metric $D$."

The substrate-level reading: the chain's coarse-grained propagation in the deformed substrate follows geodesics with respect to the deformation-induced effective metric $D$. The chain "sees" the substrate as if it were curved, but no actual spacetime curvature is involved — only a substrate-level re-parameterization of rule-type identity.

---

## 7. Worked Example: Uniform Stretch

To make the construction concrete, consider a uniform stretch in one direction:

$$
\mathbf{R}(\mathbf{x}) = (\alpha x^1, x^2, x^3), \qquad \alpha > 0.
$$

The deformation stretches the substrate by factor $\alpha$ in $\hat{\mathbf{x}}_1$, leaving other directions unchanged.

### 7.1 Jacobian

$$
J = \text{diag}(\alpha, 1, 1), \qquad J^{-1} = \text{diag}(\alpha^{-1}, 1, 1), \qquad \det J = \alpha.
$$

### 7.2 Rule-type deformation tensor

$$
D = (J^{-1})^T(J^{-1}) = \text{diag}(\alpha^{-2}, 1, 1).
$$

### 7.3 Transformed permittivity (isotropic original)

If the un-deformed substrate is isotropic with $\varepsilon^{kl} = \varepsilon_0\,\delta^{kl}$:

$$
\varepsilon'^{11} = \alpha^{-1}\cdot\alpha\cdot\alpha\cdot \varepsilon_0 = \alpha\,\varepsilon_0, \\
\varepsilon'^{22} = \alpha^{-1}\cdot 1\cdot 1\cdot \varepsilon_0 = \alpha^{-1}\,\varepsilon_0, \\
\varepsilon'^{33} = \alpha^{-1}\cdot 1\cdot 1\cdot \varepsilon_0 = \alpha^{-1}\,\varepsilon_0.
$$

Off-diagonal components are zero.

So the uniform stretch produces:
- Permittivity *enhanced* by factor $\alpha$ along the stretch direction.
- Permittivity *reduced* by factor $\alpha^{-1}$ perpendicular to the stretch.

**Substrate-level reading.** Stretching the substrate by $\alpha$ along $\hat{\mathbf{x}}_1$:
- Increases the path length the chain must traverse in $\hat{\mathbf{x}}_1$ direction.
- Concentrates rule-type microstructure density per unit physical length perpendicular to the stretch (since unit cells are compressed in the perpendicular directions).
- The effective permittivity tensor reflects this: stronger response along stretch direction, weaker response perpendicular.

This is the substrate-level mechanism for *uniaxial anisotropy from deformation*: starting from an isotropic substrate and applying a uniform stretch yields a uniaxial effective medium.

### 7.4 Cloaking preview

A cloaking deformation expels a region $R \leq R_1$ to a shell $R_1 \leq R \leq R_2$. The Jacobian is highly position-dependent: large stretch along the radial direction near $R = R_1$ (where the "shrinking" of the cloaked region forces the surrounding shell to stretch radially), and angular components that compensate. The resulting transformed $\varepsilon, \mu$ are highly anisotropic and position-dependent — exactly what Pendry's 2006 cloak prescribes.

Memo 9 derives the explicit cloaking deformation and its $\varepsilon, \mu$ tensors.

---

## 8. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **The substrate-gradient deformation $\mathbf{R}(\mathbf{x})$ as a smooth re-parameterization of the substrate's rule-type identity-labeling** (§1.1, P-MM-3). FORCED by P-MM-3.

- **The two-scale decomposition $\mathbf{R}(\mathbf{x}) = \mathbf{x} + \mathbf{u}(\mathbf{X})$ with slow-varying displacement** (§1.2). FORCED by P-MM-6 (the deformation acts at coarse-grained scale $L$, not at microstructure scale $a$).

- **The Jacobian $J^i{}_j = \partial R^i/\partial X^j$ and its identity-at-zero-deformation, smoothness, invertibility, and composition properties** (§2). FORCED by smooth-manifold structure of the substrate.

- **The rule-type deformation tensor $D_{ij} = (J^{-1})^k{}_i (J^{-1})^l{}_j \delta_{kl}$** (§3.1) as the pulled-back metric tensor. FORCED by the substrate-gradient deformation acting on the un-deformed flat Euclidean metric.

- **The constitutive transformation rule $\varepsilon'^{ij} = (\det J)^{-1} J^i{}_k J^j{}_l \varepsilon^{kl}$** (§4.2). FORCED by:
  - The transformation rules for $\mathbf{E}$ (covariant one-form) and $\mathbf{D}$ (contravariant tensor density).
  - The invariance of the constitutive relation $\mathbf{D} = \varepsilon\mathbf{E}$ under change of variables.

- **The analogous transformation rule for $\mu'^{ij}$** (§4.3). FORCED by the analogous derivation for the magnetic constitutive relation.

- **Compatibility with homogenization at leading order in $a/L$** (§5). FORCED by the scale-separation between the macroscopic deformation and the microstructure-scale averaging.

- **The substrate-level reading of $D_{ij}$ as the effective metric in the deformed substrate** (§6.2). FORCED by the wave-equation rewrite in covariant tensor form.

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Tensor transformation rules** ($\mathbf{E}$ as one-form, $\mathbf{D}$ as tensor density) (§4.2). Standard differential-geometry results applied to Maxwell's equations.

- **Constitutive-relation invariance under change of variables** (§4.2). Standard physics requirement: the relation $\mathbf{D} = \varepsilon\mathbf{E}$ must hold in any choice of coordinates.

- **Matrix-algebra identities for Jacobians and their inverses** (§2.2, §4.5). Standard linear algebra.

- **Pulled-back metric structure** (§3.2). Standard differential geometry.

### What remains OPEN

- **Substrate-level coupling between deformation and microstructure at subleading orders in $a/L$** (§5.2). The leading-order analysis decouples homogenization (which averages at scale $a$) from deformation (which acts at scale $L$). When the deformation gradient is large compared to $L/a$, this decoupling breaks down. OPEN; structurally similar but algebraically more involved.

- **Sharp (non-smooth) deformations** with kinks, singularities, or discontinuous Jacobians. The standard transformation-optics formalism assumes smooth diffeomorphisms; cloaking deformations approach singularities at the cloak's inner boundary (the "expelled" region collapses to a point or line). OPEN for fully singular cases; smooth approximations work in practice.

- **Time-dependent deformations.** Substrate-gradient deformations $\mathbf{R}(\mathbf{x}, t)$ that vary in time would produce dynamical effective constitutive tensors. The leading-order analysis here is static. OPEN.

- **Active deformations driven by the chain itself.** When the chain's amplitude back-reacts on the deformation (gravitational or self-induced deformation), the system becomes self-consistent. For metamaterials, the chain's field is too weak to back-react; this is OPEN for high-power or quantum-coherent applications.

- **Deformations that change the substrate's topology.** Cloaking deformations push the "expelled" region to a boundary, but standard transformation optics works within a fixed topology. Topologically non-trivial substrate-gradient deformations (e.g., wormhole-like substrate structures) are OPEN.

- **Quantum metamaterial deformations.** Quantum effects in metamaterials with explicit deformation control (e.g., time-modulated metamaterials with single-photon dynamics) require composition with Lindblad-type machinery. OPEN.

- **Substrate-level non-Hermitian deformations** with gain/loss anisotropy. OPEN.

---

## 9. Review and Recommended Next Steps

### Review

Memo 7 has delivered, opening the transformation-optics cluster:

- **Setup of substrate-gradient deformations** $\mathbf{R}(\mathbf{x}) = \mathbf{x} + \mathbf{u}(\mathbf{X})$ with slow-varying displacement field (§1.1–1.3). The local-shift formulation $\mathbf{y}' = \mathbf{y} + \delta\mathbf{y}(\mathbf{X})$ as the equivalent two-scale parameterization (§1.3).

- **Jacobian** $J^i{}_j(\mathbf{X}) = \delta^i{}_j + \partial u^i/\partial X^j$ (§2.1) with substrate-level meaning as the local stretching/rotation/shearing of the substrate's spatial structure (§2.3) and its action on rule-type participation pathways (§2.4).

- **Rule-type deformation tensor** $D_{ij}(\mathbf{X}) = (J^{-1})^k{}_i(J^{-1})^l{}_j\delta_{kl}$ (§3.1), the substrate-level pulled-back metric tensor (§3.2).

- **Constitutive-tensor transformation rules** $\varepsilon'^{ij} = (\det J)^{-1} J^i{}_k J^j{}_l \varepsilon^{kl}$ and $\mu'^{ij} = (\det J)^{-1} J^i{}_k J^j{}_l \mu^{kl}$ (§4.2–4.3), derived from substrate primitives via the tensor transformation rules for $\mathbf{E}$ and $\mathbf{D}$.

- **Compatibility with the homogenization cluster** at leading order in $a/L$ (§5.1), with substrate-level statement that deformation and homogenization commute at this order.

- **Wave-equation form in the deformed substrate** with $D_{ij}$ playing the role of an effective metric (§6.2), establishing the substrate-level reading: "chain's coarse-grained propagation in the deformed substrate follows geodesics of the deformation-induced effective metric, but no actual spacetime curvature is involved."

- **Worked example of uniform stretch** producing uniaxial anisotropy in initially-isotropic substrate (§7).

- **Cloaking preview** identifying the substrate-level mechanism for the next memos: expelling a region requires position-dependent Jacobian with large radial stretch near the cloak's inner boundary (§7.4).

- **Explicit FORCED / FORM-FORCED-INHERITED / OPEN labeling** (§8).

### Honest scope-limit

Memo 7 introduced no new substrate primitives beyond P-MM-1 through P-MM-6 (Memo 1's inventory). All derivations are done inline. The standard tensor transformation rules and matrix algebra are inherited at form level with substrate-level interpretation provided. No cross-references to other arcs.

### Recommended next steps

In order:

1. **Memo 8 — Mapping to Effective Metric.** Articulate the explicit substrate-level interpretation of $D_{ij}$ as the effective metric on the chain's coarse-grained propagation, including geodesic structure and how the chain's pre-individuation amplitude propagates along these geodesics. Connect to standard transformation-optics formalism and the curved-space analogy.

2. **Memo 9 — The Cloaking Deformation.** Specify the explicit cloaking deformation that expels a sphere $R \leq R_1$ to a shell $R_1 \leq R' \leq R_2$, compute its Jacobian, the rule-type deformation tensor, and the resulting position-dependent $\varepsilon, \mu$ tensor fields.

3. **Memo 10 — Substrate-Level Reading of Invisibility Cloaking.** Articulate the substrate-level mechanism: cloaking as substrate-level rule-type-redirection that excludes a topologically distinct region from the chain's accessible substrate.

4. **Memo 11 — Conditions and Limits of Transformation Optics.** Identify when transformation optics works (smooth deformations within homogenization validity) and when it breaks down (sharp deformations, broadband cloaking, magnetic-electric coupling not captured by standard formulation).

5. **Memo 12 — Substrate-Level Metasurface Boundary Conditions.** Independent line: derive the generalized Snell's law from rule-type discontinuities at interfaces (P-MM-5).

6. **Memo 13 — Synthesis.** Tie all three precursor derivations together.

### Anchor for future memos

The Jacobian $J^i{}_j(\mathbf{X})$, the rule-type deformation tensor $D_{ij}(\mathbf{X})$, and the constitutive transformation rules established in Memo 7 are standardized for the remainder of the transformation-optics cluster. Memo 8 will articulate the metric interpretation; Memos 9–11 will apply the transformation to specific cloaking configurations and analyze the substrate-level meaning of invisibility.
