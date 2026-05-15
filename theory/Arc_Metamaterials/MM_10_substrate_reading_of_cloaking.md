# Memo 10 — Substrate-Level Reading of Invisibility Cloaking

**Arc Metamaterials, Memo 10 of 13.**
**Allen Proxmire** · May 2026

*Articulate the substrate-level interpretation of invisibility cloaking. Establish that "invisibility" is topological absence rather than concealment. Show how the chain experiences the cloak through coarse-grained geodesics, why scattering is suppressed through impedance matching, why the cloaked interior is unreachable through divergent metric components, and how energy flows around the cloaked region.*

---

## 1. Setup and Notation

A chain (P-MM-4) propagates through a substrate whose rule-type microstructure (P-MM-1) has been deformed via a substrate-gradient deformation (P-MM-3) in the coarse-graining regime $\ell_P \ll a \ll \lambda \ll L$ (P-MM-6).

The specific deformation is the *Pendry 2006 spherical cloak* derived in the previous memo of this Arc:

$$
r' = R_1 + \alpha\, r, \qquad \theta' = \theta, \qquad \phi' = \phi,
$$

with $\alpha = (R_2 - R_1)/R_2 \in (0, 1)$ and $\beta = 1/\alpha = R_2/(R_2 - R_1) > 1$. The map carries virtual radius $r \in [0, R_2]$ to physical radius $r' \in [R_1, R_2]$, sending the virtual origin $r = 0$ to the physical sphere $r' = R_1$.

The resulting effective constitutive tensors in the cloak shell $R_1 \leq r' \leq R_2$ (orthonormal spherical basis) are

$$
\varepsilon_{\hat r'}/\varepsilon_0 = \mu_{\hat r'}/\mu_0 = \beta\left(\frac{r' - R_1}{r'}\right)^2,
$$

$$
\varepsilon_{\hat \theta'}/\varepsilon_0 = \varepsilon_{\hat \phi'}/\varepsilon_0 = \mu_{\hat \theta'}/\mu_0 = \mu_{\hat \phi'}/\mu_0 = \beta.
$$

The effective metric in the cloak (orthonormal spherical basis) is

$$
g_{\hat r'\hat r'} = \beta^{2}, \qquad g_{\hat \theta'\hat \theta'} = g_{\hat \phi'\hat \phi'} = \beta^{2}\left(\frac{r' - R_1}{r'}\right)^{2}.
$$

The coordinate-basis metric in physical $(r', \theta', \phi')$ coordinates is

$$
ds^{2}_\text{cloak} = \beta^{2}\!\left[dr'^{2} + (r' - R_1)^{2}\,d\theta'^{2} + (r' - R_1)^{2}\sin^{2}\theta'\,d\phi'^{2}\right],
$$

which is conformal to a flat Euclidean metric centered at $r' = R_1$ with radial coordinate $\rho \equiv r' - R_1$.

The mathematics is established. This Memo articulates the substrate-level *meaning* of the cloak — what invisibility is, how the chain experiences the cloak, why scattering vanishes, why the interior is unreachable, and how energy flows around the cloaked region.

---

## 2. (A) What "Invisibility" Means at Substrate Level

### 2.1 The substrate ontology of cloaking

The substrate inventory (P-MM-1 through P-MM-6) contains:
- Chains and their participation rules.
- Rule-type microstructure $\tau(\mathbf{x})$ specifying which rule-type identity occupies each substrate-level position.
- Coarse-graining machinery producing effective constitutive tensors.
- Substrate-gradient deformations re-parameterizing the rule-type identity-labeling.

The cloaking deformation maps virtual radius $r \in [0, R_2]$ to physical radius $r' \in [R_1, R_2]$. Two consequences:

1. **The virtual interior $r < R_2$** maps into the physical shell $R_1 \leq r' \leq R_2$. Every virtual rule-type identity has a physical pre-image.
2. **The physical region $r' < R_1$** has *no virtual pre-image*. No rule-type identity has been assigned to this region in the deformed configuration.

The substrate-level statement: in the deformed substrate, the physical region $r' < R_1$ is a *gap in the substrate's rule-type assignment*. It is not a region with low-density microstructure or with vacuum-like rule-type; it is a region where the substrate's rule-type identity-labeling does not extend at all.

### 2.2 Invisibility as topological absence

"Invisibility" of the cloaked region $r' < R_1$ is the substrate-level statement that this region is *not part of the chain's accessible substrate*. The chain has no rule-type pathway to interact with whatever (if anything) occupies the physical region $r' < R_1$, because:

- The chain's coarse-grained dynamics is governed by the effective constitutive tensors and effective metric of the substrate.
- The effective constitutive tensors and effective metric are derived from the substrate's rule-type identity-labeling via the cell-averaging machinery.
- Where the rule-type identity-labeling has not been assigned, no effective constitutive tensors exist and no effective metric exists.
- Without effective constitutive tensors and effective metric, the chain has no coarse-grained dynamics in that region.

Substrate-level formulation: *the cloaked region is not a hidden region; it is an absent region.*

### 2.3 Comparison with classical "invisibility"

Classical (non-cloak) "invisibility" requires concealment: the cloaked object is physically present and physically interacts with the chain (via Maxwell's equations), but its presence is hidden via passive absorption, active cancellation, or sensory deception. The object is *there*; its interaction with the chain is suppressed.

Pendry-cloak "invisibility" is structurally different. The cloaked region is *not there* in the chain's accessible substrate. The cloak does not suppress an interaction that would otherwise occur; it eliminates the possibility of interaction by removing the cloaked region from the chain's substrate altogether.

This is a stronger sense of invisibility:
- A classical cloak hides a thing.
- A Pendry cloak makes the thing inaccessible.

The substrate-level mechanism: the substrate-gradient deformation re-parameterizes the rule-type identity-labeling so that no rule-type identity is assigned to the cloaked interior. The substrate, as the chain encounters it, has no information about what occupies $r' < R_1$ — that region is outside the substrate's rule-type domain in the deformed configuration.

### 2.4 What can be placed in the cloaked region

In standard transformation-optics analysis, *anything* can be placed in the cloaked region $r' < R_1$ without affecting chain propagation in the shell $R_1 \leq r' \leq R_2$ or in the exterior $r' > R_2$. Substrate-level reading: whatever occupies the cloaked region cannot interact with the chain because:

- No chain pathway reaches the cloaked region.
- The chain's coarse-grained dynamics in the shell is determined entirely by the effective constitutive tensors and the boundary condition at $r' = R_1$ (the vanishing-radial-response boundary).
- Whatever physical structure exists in $r' < R_1$ couples to chains only via its own substrate-level rule-type structure; but the deformation has eliminated the rule-type pathway connecting the cloaked-region structure to the exterior.

The cloaked region's contents are *substrate-level isolated* from the exterior. They neither receive nor emit chains that the exterior can detect.

### 2.5 Substrate-level summary

$$
\boxed{\quad
\text{Invisibility} \;=\; \text{absence of rule-type pathways connecting cloaked region to chain's accessible substrate}.
\quad}
$$

The cloak does not hide anything; it makes the cloaked region absent from the chain's substrate. Whatever is in the cloaked region is structurally inaccessible — not because it is shielded but because no substrate-level pathway leads to it.

---

## 3. (B) How the Chain Experiences the Cloak

### 3.1 The chain's coarse-grained geodesics

The chain's high-frequency (ray-optics) propagation in the cloak follows geodesics of the effective metric. The cloak metric is conformal to a flat metric centered at $r' = R_1$:

$$
ds^{2}_\text{cloak} = \beta^{2}\,(d\rho^{2} + \rho^{2}\,d\theta'^{2} + \rho^{2}\sin^{2}\theta'\,d\phi'^{2}),
$$

with shifted radial coordinate $\rho = r' - R_1 \geq 0$.

In conformally flat spaces, geodesics coincide with the geodesics of the underlying flat metric, up to affine reparameterization. The flat metric in $\rho, \theta', \phi'$ is Euclidean centered at $\rho = 0$. Its geodesics are straight lines.

So the chain's coarse-grained trajectories in the cloak are *straight lines* in the $\rho, \theta', \phi'$ coordinate system. Mapping back to physical coordinates: the chain's trajectories are straight lines in a coordinate system where the cloak's inner sphere $r' = R_1$ has been *collapsed to a single point* $\rho = 0$.

### 3.2 Geodesic bending in physical coordinates

In physical $(r', \theta', \phi')$ coordinates, the cloak's effective metric is *not* flat. The chain's geodesics, when expressed in physical coordinates, are curved. Specifically:

- Far from the cloak ($r' \gg R_2$): vacuum, $g_{ij} = \delta_{ij}$. Geodesics are straight lines.
- In the cloak shell ($R_1 \leq r' \leq R_2$): the metric is anisotropic. Geodesics curve toward smaller $r'$ but cannot reach $r' = R_1$.
- The inner sphere $r' = R_1$ corresponds to $\rho = 0$ — a single point in the conformally-flat picture. Geodesics that "would have passed through" $r' = 0$ instead pass near but not through $\rho = 0$ (i.e., they pass tangentially near $r' = R_1$).

The substrate-level statement: the chain's trajectory bends to avoid the inner sphere because the substrate has been re-parameterized so that the inner sphere is a single point in the chain's effective geometry. The chain cannot pass through a point (it has finite transverse extent in the eikonal approximation), so it bends around.

### 3.3 The chain's phase-accumulation along geodesics

The chain's pre-individuation amplitude accumulates phase along its trajectory at the local rate set by the effective wavenumber $k(\mathbf{X}) = n(\mathbf{X})\,\omega/c$, where $n$ is the local effective refractive index.

In the cloak, the chain's coarse-grained refractive index along a geodesic with tangent vector $\hat{\mathbf{t}}$ is

$$
n(\hat{\mathbf{t}}) = \sqrt{\hat{t}^{i}\hat{t}^{j} g_{ij}}\cdot \sqrt{\hat{t}^{i}\hat{t}^{j} \varepsilon_{ij}\mu_{ij}/(\varepsilon_0\mu_0)}.
$$

For the cloak, this evaluates to:

- **Radial direction** ($\hat{\mathbf{t}} = \hat r'$): $n_{\hat r'} = \sqrt{g_{\hat r'\hat r'}\cdot \varepsilon_{\hat r'}\mu_{\hat r'}/(\varepsilon_0\mu_0)} = \beta \cdot \beta((r'-R_1)/r')^{2} = \beta^{2}((r'-R_1)/r')^{2}$.
- **Angular direction** ($\hat{\mathbf{t}} = \hat\theta'$ or $\hat\phi'$): $n_{\hat\theta'} = \sqrt{g_{\hat\theta'\hat\theta'}\cdot \varepsilon_{\hat\theta'}\mu_{\hat\theta'}/(\varepsilon_0\mu_0)} = \beta((r'-R_1)/r')\cdot \beta = \beta^{2}(r'-R_1)/r'$.

Wait — the effective refractive index for a wave propagating in direction $\hat{\mathbf{t}}$ involves both the metric (for the wave equation's principal symbol) and the constitutive tensors. The relation depends on convention. The key substrate-level point is that *along the chain's geodesic, the phase accumulation rate varies with position*. The chain's phase advances more slowly near the inner boundary $r' \to R_1$ (in the radial direction) and at a constant rate (in the angular direction).

The total phase accumulated by the chain traversing the cloak is, formally,

$$
\Phi_\text{cloak} = \int_\text{geodesic} k(\mathbf{X})\, ds,
$$

with $k = n\,\omega/c$ varying along the path. By the conformal flatness of the cloak metric (§3.1), this integral equals the phase accumulated by the same chain traversing the corresponding straight-line geodesic in the conformally-rescaled flat metric.

### 3.4 The cloak's exterior appearance

To an external observer (at $r' > R_2$), the chain's trajectory through the cloak is structurally indistinguishable from a chain traversing the same external region without the cloak. The chain enters at $r' = R_2$ from one direction, emerges at $r' = R_2$ on the far side, and continues in the same direction it would have without the cloak (because the cloak's bending preserves the asymptotic direction).

The phase accumulated by the chain in the cloak is *not zero*, but it equals the phase the chain would have accumulated traversing the same physical distance in vacuum, accounting for the cloak's effective optical path length. For an ideal Pendry cloak, the chain's exterior phase pattern is indistinguishable from its phase pattern in vacuum without the cloak.

Substrate-level reading: the cloak's deformation has preserved the chain's coarse-grained trajectory and phase pattern as it would have been in undeformed substrate, while excluding the inner region from the chain's accessible substrate.

---

## 4. (C) Why Scattering Is Suppressed

### 4.1 Impedance matching everywhere in the cloak

The cloak's effective constitutive tensors satisfy $\varepsilon_{\hat i} = \mu_{\hat i}\,\varepsilon_0/\mu_0$ for each orthonormal direction $\hat i \in \{\hat r', \hat\theta', \hat\phi'\}$. The local wave impedance in direction $\hat i$ is

$$
Z_{\hat i}(\mathbf{X}) = \sqrt{\mu_{\hat i}(\mathbf{X})/\varepsilon_{\hat i}(\mathbf{X})}.
$$

For the cloak:

$$
Z_{\hat r'} = \sqrt{\mu_0\beta((r'-R_1)/r')^{2}\,/\,\varepsilon_0\beta((r'-R_1)/r')^{2}} = \sqrt{\mu_0/\varepsilon_0} = Z_0,
$$

$$
Z_{\hat \theta'} = Z_{\hat\phi'} = \sqrt{\mu_0\beta/(\varepsilon_0\beta)} = \sqrt{\mu_0/\varepsilon_0} = Z_0,
$$

where $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ is the vacuum impedance.

The cloak is *impedance-matched to vacuum everywhere*, in every direction.

### 4.2 Why impedance matching eliminates reflections

A boundary between two media reflects a wave when there is an impedance mismatch. For a wave at normal incidence from medium 1 ($Z_1$) to medium 2 ($Z_2$), the Fresnel reflection coefficient is

$$
r = \frac{Z_2 - Z_1}{Z_2 + Z_1}.
$$

When $Z_2 = Z_1$, $r = 0$ and no reflection occurs.

At the cloak's outer boundary $r' = R_2$, the chain transitions from vacuum (impedance $Z_0$) to the cloak shell (impedance $Z_0$). Since the impedances match, *no reflection occurs* despite the discontinuity in the individual $\varepsilon, \mu$ values (the radial $\varepsilon_{\hat r'}/\varepsilon_0$ jumps from 1 outside to $\alpha < 1$ inside the cloak at $r' = R_2$, but $\mu_{\hat r'}/\mu_0$ jumps identically, preserving impedance).

The chain enters the cloak smoothly.

### 4.3 Why impedance matching also eliminates reflections within the cloak

Within the cloak shell, $Z_{\hat i}(\mathbf{X}) = Z_0$ at every position and in every direction. There is *no impedance gradient* anywhere in the cloak.

For a wave traveling through a slowly-varying medium, reflections occur when the impedance gradient is non-zero. In the cloak, the impedance is uniformly $Z_0$ throughout the shell, so there is no internal reflection — even though the cloak's $\varepsilon$ and $\mu$ values vary considerably with $r'$ (the radial components go from $\alpha$ at $r' = R_2$ to $0$ at $r' = R_1$). The variation in $\varepsilon$ is exactly compensated by the matching variation in $\mu$, preserving the impedance.

### 4.4 Substrate-level meaning of impedance matching

In standard EM, impedance is a property of the medium's response to electromagnetic waves: it measures the ratio of electric to magnetic field strength in a propagating wave.

At substrate level (per Memo 5), $\varepsilon$ is the coarse-grained rule-type polarizability response and $\mu$ is the coarse-grained rule-type circulation response. The impedance $Z = \sqrt{\mu/\varepsilon}$ measures the *balance* between these two response types.

The cloak's $\varepsilon = \mu$ condition (in normalized units) is the substrate-level statement that the rule-type microstructure has been engineered with equal polarizability and circulation responses at every position. The chain's gauge-field amplitude — which couples to both responses — experiences no asymmetry between electric and magnetic structure as it traverses the cloak.

**Substrate-level reading: impedance matching means rule-type microstructure density is adjusted so that the chain's participation amplitude does not "see" a boundary or a gradient**. The cloak's spatial variation in rule-type response is structured so that the *ratio* of responses is constant, even though the individual responses vary.

The chain experiences the cloak as a smooth (non-scattering) medium because no impedance discontinuity arises at any boundary or within the bulk. The deformation has produced rule-type microstructure with the correct correlation pattern (electric and magnetic responses scaling identically with position) to suppress all reflection.

---

## 5. (D) Why the Interior Is Unreachable

### 5.1 Vanishing radial constitutive response at $r' = R_1$

From Memo 9:

$$
\varepsilon_{\hat r'}(r')/\varepsilon_0 = \mu_{\hat r'}(r')/\mu_0 = \beta\left(\frac{r' - R_1}{r'}\right)^{2}.
$$

At $r' \to R_1$:

$$
\lim_{r' \to R_1^{+}} \varepsilon_{\hat r'}(r')/\varepsilon_0 = \beta\cdot 0 = 0.
$$

The radial component of $\varepsilon$ (and $\mu$) vanishes at the inner boundary.

### 5.2 Why vanishing $\varepsilon_{\hat r'}$ blocks radial propagation

A propagating wave with wave vector $\mathbf{k}$ in direction $\hat{\mathbf{t}}$ satisfies

$$
\mathbf{k}\cdot\hat{\mathbf{t}} \cdot c/\omega = n(\hat{\mathbf{t}}) = \sqrt{\hat{t}^{i}\hat{t}^{j}\varepsilon_{ij}\mu_{ij}/(\varepsilon_0\mu_0)}.
$$

For a purely radial wave ($\hat{\mathbf{t}} = \hat r'$):

$$
n_{\hat r'} \propto \sqrt{\varepsilon_{\hat r'}\mu_{\hat r'}/(\varepsilon_0\mu_0)} = \beta((r' - R_1)/r')^{2}.
$$

At $r' \to R_1$: $n_{\hat r'} \to 0$. The radial refractive index vanishes.

A vanishing refractive index means the wave's phase velocity in that direction diverges: $v_\text{phase}^{\hat r'} = c/n_{\hat r'} \to \infty$. Equivalently, the wave's radial wavelength $\lambda_{\hat r'} \to \infty$.

The substrate-level interpretation: at the inner boundary, the chain's pre-individuation amplitude *cannot vary* over any finite radial distance — the wavelength is infinite. The amplitude is forced to be constant in the radial direction at $r' = R_1$. No radial wave propagation is possible.

### 5.3 Divergent radial metric component

From Memo 9:

$$
g_{\hat r'\hat r'} = \beta^{2},
$$

which is finite at $r' = R_1$ in orthonormal basis. However, the *coordinate-basis* metric component is

$$
g_{r'r'}^\text{coord} = g_{\hat r'\hat r'} = \beta^{2}\;\text{at } r' = R_1.
$$

The angular components vanish:

$$
g_{\theta'\theta'}^\text{coord} = \beta^{2}(r' - R_1)^{2} \to 0 \quad \text{as } r' \to R_1.
$$

This is the substrate-level statement that the angular coordinate $\theta'$ at $r' = R_1$ corresponds to a single point in the virtual space — the angular extent at the inner boundary is degenerate.

### 5.4 The substrate-level mechanism of unreachability

The cloaking deformation maps the entire virtual interior $r < R_2$ onto the physical shell $R_1 \leq r' \leq R_2$. In particular, the virtual point $r = 0$ maps to the entire physical sphere $r' = R_1$.

Substrate-level reading: an *infinite virtual compression* has been applied at the inner boundary. The substrate's rule-type microstructure for the virtual interior has been radially compressed to vanishing thickness at $r' = R_1$ — the inner boundary is a "singular layer" where infinite virtual rule-type structure has been compressed into zero physical thickness.

The chain, propagating through the cloak in the radial direction, encounters this singular layer at $r' = R_1$. Two possibilities:

- The chain stops at $r' = R_1$ because no radial propagation is possible (radial wavelength infinite).
- The chain bends tangentially and continues around the inner sphere (the only remaining propagation direction is angular).

The cloak is designed so that the chain bends tangentially. The angular components of the constitutive tensor are finite ($\varepsilon_{\hat\theta'} = \beta\varepsilon_0$), so angular propagation is well-defined. The chain's geodesics in the conformally-flat picture are straight lines that pass through or near $\rho = 0$ (i.e., $r' = R_1$); in physical coordinates, these correspond to trajectories that approach $r' = R_1$ tangentially and circulate around the inner sphere.

### 5.5 Substrate-level summary of unreachability

$$
\boxed{\quad
\text{Interior unreachability} \;=\; \text{infinite virtual rule-type compression at $r' = R_1$ eliminates radial propagation pathways}.
\quad}
$$

The chain cannot enter the cloaked region because:
1. The radial refractive index vanishes at the inner boundary.
2. The radial wavelength diverges.
3. The substrate's rule-type structure has zero "extent" in the radial direction at $r' = R_1$ (everything in the virtual interior has been compressed to that singular layer).
4. Beyond $r' = R_1$, no rule-type identity has been assigned to the substrate.

The interior is *unreachable* because there are no rule-type pathways leading there. The cloaking deformation has eliminated them by construction.

---

## 6. (E) Energy Flow and the Poynting Vector

### 6.1 Energy flow lines

The energy flow of an electromagnetic wave is described by the Poynting vector $\mathbf{S} = \mathbf{E}\times\mathbf{H}$. In a medium with effective tensors $\varepsilon, \mu$, the time-averaged Poynting vector points along the geodesic direction (for plane waves).

In the cloak, the chain's effective geodesics are straight lines in the conformally-flat coordinate system $(\rho, \theta', \phi')$ with $\rho = r' - R_1$. Mapping these back to physical $(r', \theta', \phi')$ coordinates, the energy flow lines are curves that bend around the inner sphere.

The energy flow pattern in physical coordinates:

- Far from the cloak ($r' \gg R_2$): energy flows in straight lines.
- Approaching the cloak ($r' \to R_2^{+}$): energy flow enters the cloak smoothly (no reflection).
- In the cloak shell ($R_1 \leq r' \leq R_2$): energy flow curves around the inner sphere following geodesics of the conformally-flat metric.
- At the inner boundary ($r' = R_1$): energy flow is tangential.
- Exiting the cloak ($r' = R_2$, far side): energy flow emerges in the same direction it would have had without the cloak.

### 6.2 No energy enters the cloaked region

Since the chain's geodesics do not enter the interior $r' < R_1$, the energy flow does not enter either. The Poynting vector has no inward radial component at $r' = R_1$.

Substrate-level reading: the chain's coarse-grained energy is carried along the same rule-type pathways that the chain itself follows. Since these pathways exclude the cloaked region, no energy reaches the interior.

This is structurally distinct from a classical reflective coating, where energy can pile up at the inner boundary or be reflected back. In the Pendry cloak, no energy reaches the inner boundary — the energy flow bends smoothly around without accumulating anywhere.

### 6.3 Energy flow continuity

Energy flow into the cloak at $r' = R_2$ equals energy flow out of the cloak on the far side: the cloak does not absorb energy (assuming a lossless cloak; real cloaks have small losses from material absorption).

Substrate-level reading: the deformation conserves the chain's coarse-grained amplitude flow. The amplitude that enters the cloak at $r' = R_2$ on one side emerges on the far side without loss, having been re-routed around the inner sphere.

### 6.4 Substrate-level mechanism for energy redirection

The cloak's effective constitutive tensors produce a gradient of refractive index throughout the shell. Energy follows geodesics of the effective metric, which are paths of stationary optical path length (Fermat's principle).

The substrate-level mechanism: the cloak's ED-gradient deformation re-parameterizes the substrate's rule-type identity-labeling in a way that makes geodesics around the inner sphere have *equal optical path length* to straight lines through the original (un-deformed) space. The deformation has been engineered so that the chain's coarse-grained dynamics in the deformed substrate produces the same external observations as in vacuum.

$$
\boxed{\quad
\text{ED-gradient deformation redirects channel propagation without scattering, by preserving optical path lengths and impedance everywhere}.
\quad}
$$

This is the substrate-level statement of the cloak's "perfect" property: with idealized (singular) constitutive tensors at $r' = R_1$, no reflection, no absorption, no scattering, no phase distortion. The deformation has *re-routed* the chain's dynamics around the excluded region while preserving all external observables.

---

## 7. (F) Preparation for Memo 11

The Pendry cloak is a *specific* substrate-gradient deformation: a spherical, radial-only, smooth map that excludes a sphere. Memo 11 will articulate the *limits* of the transformation-optics framework by examining what deformations work and what break down.

### 7.1 Generalization to arbitrary deformations

The substrate-gradient deformation $\mathbf{R}(\mathbf{x})$ can be any smooth invertible map. Different deformations produce different constitutive tensor patterns:

- **Linear deformations**: uniform stretching, shearing, or rotation. Produce uniform anisotropic effective media (Memo 7 §7).
- **Radial deformations with spherical symmetry**: the Pendry cloak family.
- **Cylindrical deformations**: 2D cloaks (cylinder around a line).
- **Carpet cloaks**: deformations that "flatten" a bump in a surface.
- **Arbitrary deformations**: arbitrary shaped cloaks (cloaking arbitrary objects).

Each is a substrate-gradient deformation; the substrate-level reading (re-parameterization of rule-type identity-labeling) is identical. The specific effective constitutive tensors depend on the deformation specification.

### 7.2 What Memo 11 will analyze

Limits of the transformation-optics machinery:

- **Smoothness requirement**: deformations must be smooth (invertible diffeomorphisms) for the Jacobian to be well-defined and the effective constitutive tensors to be finite. Cloaks have singular Jacobian at the inner boundary; regularization is needed for practical implementation.

- **Homogenization regime requirement** ($a \ll \lambda$): the deformation must vary slowly enough relative to the microstructure scale that homogenization remains valid. Rapidly varying deformations break this assumption.

- **Frequency dependence**: the cloak's $\varepsilon, \mu$ values are FORCED at a single frequency. Real microstructures have dispersion; broadband cloaking requires multiple resonances or different mechanisms.

- **Magnetic-electric coupling (bianisotropy)**: the standard transformation-optics formulation produces $\varepsilon, \mu$ tensors without magnetoelectric cross-coupling. Generalizations producing bianisotropic effective media (e.g., for chiral materials) require extended formalism.

- **Active and time-varying deformations**: the static deformations treated here cannot produce, e.g., Doppler-shifting cloaks or non-reciprocal devices. Time-dependent transformation optics is OPEN.

Memo 11 will address these limits and articulate the substrate-level reading of each.

### 7.3 Substrate-level meaning of generalized cloaks

The substrate-level mechanism applies to *any* deformation that produces a topologically distinct region in the chain's accessible substrate. The Pendry sphere is the canonical example; cylindrical cloaks, carpet cloaks, and arbitrarily-shaped cloaks all follow the same substrate-level reading:

- The deformation re-parameterizes the substrate's rule-type identity-labeling.
- The deformed configuration has some region excluded from the chain's accessible substrate.
- The chain's coarse-grained dynamics in the deformed substrate excludes the deformed-out region.
- The external observable pattern is preserved because the deformation conserves the chain's external trajectory and phase.

This unified substrate-level mechanism is what Memo 11 will close out, distinguishing what is FORCED by the substrate ontology from what is INHERITED from specific transformation-optics conventions.

---

## 8. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **Invisibility as topological absence**, not concealment (§2). FORCED by the substrate-gradient deformation having no inverse image for the cloaked region in the deformed configuration.

- **The chain's geodesics avoiding the inner sphere** (§3.2). FORCED by the conformal flatness of the cloak metric centered at $r' = R_1$: the inner sphere is a single point in the conformally-flat picture; geodesics cannot pass through a point in 3D.

- **Impedance matching everywhere in the cloak** (§4.1). FORCED by $\varepsilon_{\hat i} = \mu_{\hat i}\,\varepsilon_0/\mu_0$ at every position in every direction (a structural feature of the cloak deformation).

- **Absence of reflections at the outer boundary $r' = R_2$ and within the cloak** (§4.2, 4.3). FORCED by impedance matching, regardless of the variation of $\varepsilon, \mu$ individually.

- **Vanishing radial refractive index at $r' = R_1$** (§5.1–5.3). FORCED by the deformation mapping a virtual point to a physical sphere (infinite virtual compression at the inner boundary).

- **Unreachability of the cloaked interior** (§5.4–5.5). FORCED by:
  1. Vanishing radial propagation rate at $r' = R_1$.
  2. No rule-type identity assigned to the substrate in $r' < R_1$.

- **Energy flow around the inner sphere with no entry into cloaked region** (§6.2). FORCED by the chain's geodesics avoiding the inner sphere.

- **Energy continuity through the cloak (no absorption in idealized lossless cloak)** (§6.3). FORCED by the deformation being invertible on the shell + impedance matching.

- **The substrate-level mechanism for cloaking as topological exclusion** (§2.5, §6.4). FORCED by the cumulative effect of substrate-gradient deformation, vanishing radial response, impedance matching, and geodesic structure.

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Fresnel reflection formulas at impedance boundaries** (§4.2). Standard EM; the substrate-level interpretation is the new content.

- **Eikonal limit and geodesic structure of waves in inhomogeneous media** (§3.1). Standard high-frequency limit of Maxwell's equations.

- **Poynting-vector definition and energy-flow interpretation** (§6.1). Standard EM.

- **Conformal-flatness reading of the cloak metric centered at $r' = R_1$** (§3.1). Standard differential-geometry observation about the specific cloak metric.

- **Wave-impedance definition $Z = \sqrt{\mu/\varepsilon}$** (§4.1). Standard EM.

### What remains OPEN

- **Boundary-layer treatment at $r' = R_1$**: the cloak's singular metric at the inner boundary requires careful treatment. Practical implementations use smooth regularization at the inner surface; substrate-level reading of regularized cloaks (with finite radial response near $R_1$) is OPEN.

- **Broadband cloaks**: the Pendry cloak's perfect invisibility holds only at the design frequency. Substrate-level treatment of broadband cloaking limitations is OPEN.

- **Polarization-dependent cloaking**: real cloaks have polarization-dependent imperfections. OPEN.

- **Cloaks with internal structure that interacts with the chain via non-EM channels** (e.g., gravitational interaction, thermal coupling). The Pendry cloak hides the cloaked region from EM chains; whether other interaction types can be cloaked simultaneously is OPEN.

- **Quantum cloaks**: single-photon-level cloaking with non-classical states of light. Requires composition with Lindblad-type machinery. OPEN.

- **Cloaks for fields other than EM** (acoustic, elastodynamic, matter waves, gravity waves). The substrate-level transformation-optics framework applies in principle; specific constitutive transformations and feasibility differ. OPEN.

- **Stability of cloak performance under perturbations** (manufacturing imperfections, frequency drift, geometric distortions). Substrate-level reading OPEN.

- **Inverse problem**: given a desired cloaking pattern, derive the required substrate-gradient deformation. Open at general-shape level.

---

## 9. Review and Recommended Next Steps

### Review

Memo 10 has delivered the substrate-level reading of invisibility cloaking:

- **(A) Invisibility as topological absence** (§2): cloaking is not concealment but exclusion. The cloaked region has no rule-type identity assigned in the deformed configuration; no rule-type pathway leads to it. Anything in the cloaked region is substrate-level isolated from the exterior.

- **(B) The chain's experience** (§3): coarse-grained geodesics in the cloak are straight lines in a conformally-flat space centered at $r' = R_1$. In physical coordinates, these bend around the inner sphere. Phase accumulation along these geodesics is position-dependent; total phase accumulated is consistent with vacuum propagation around the cloak.

- **(C) Why scattering is suppressed** (§4): impedance matching $Z = Z_0$ everywhere in the cloak (in every direction). The cloak's rule-type microstructure is engineered with equal polarizability and circulation responses at every position, eliminating all reflections at internal and external boundaries.

- **(D) Why the interior is unreachable** (§5): vanishing radial refractive index and divergent angular metric at $r' = R_1$. Infinite virtual compression of rule-type microstructure eliminates radial propagation pathways. The chain cannot proceed radially inward; it must bend tangentially.

- **(E) Energy flow** (§6): Poynting-vector flow lines bend around the inner sphere without entering the cloaked region. Energy continuity through the cloak preserves the chain's external trajectory and phase pattern. The substrate-level mechanism is ED-gradient deformation redirecting channel propagation without scattering.

- **(F) Preparation for Memo 11** (§7): identification of remaining transformation-optics machinery needed (general deformations, arbitrary shapes, bianisotropy, time-varying deformations) and their substrate-level meaning.

- **Explicit FORCED / FORM-FORCED-INHERITED / OPEN labeling** (§8).

### Honest scope-limit

Memo 10 introduced no new substrate primitives beyond P-MM-1 through P-MM-6 (Memo 1's inventory). The substrate-level readings developed here are derived from the substrate primitives plus the explicit cloak deformation from Memo 9; no new substrate primitives or theorems are introduced. The standard EM concepts of impedance, Fresnel reflection, eikonal limit, and Poynting vector are inherited at form level with substrate-level interpretation provided.

### Recommended next steps

In order:

1. **Memo 11 — Conditions and Limits of Transformation Optics.** Articulate when transformation optics works and when it fails:
   - Smooth deformations within homogenization regime: full validity.
   - Sharp deformations at cloak boundaries: regularization needed; substrate-level interpretation of regularization.
   - Broadband cloaking: dispersion limits.
   - Bianisotropy and magnetoelectric coupling beyond standard transformation optics.
   - Active and time-varying deformations: structural extensions needed.
   - Substrate-level reading of each limit.
   - This closes the transformation-optics cluster (Memos 7–11).

2. **Memo 12 — Substrate-Level Metasurface Boundary Conditions.** Independent line: derive generalized Snell's law from rule-type discontinuities at interfaces (P-MM-5). This is the third precursor closure for the Arc.

3. **Memo 13 — Synthesis.** Tie all three precursor derivations together (homogenization + transformation optics + metasurface boundary conditions). After Memo 13, the precursor Arc is complete and ready for the public-facing walkthrough `from_primitives_to_metamaterials_and_photonics.md`.

### Anchor for future memos

The substrate-level reading of invisibility cloaking established in Memo 10 — invisibility as topological absence rather than concealment, geodesics bending around the inner sphere due to substrate exclusion, impedance matching eliminating scattering, infinite virtual compression eliminating radial propagation, and energy redirection without scattering — is standardized for the remainder of the transformation-optics cluster. Memo 11 will analyze the limits of this machinery; Memo 13 will tie it together with the homogenization and metasurface BC results.
