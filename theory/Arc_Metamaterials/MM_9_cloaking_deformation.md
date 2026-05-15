# Memo 9 — The Cloaking Deformation

**Arc Metamaterials, Memo 9 of 13.**
**Allen Proxmire** · May 2026

*Derive the explicit Pendry 2006 cloaking deformation from substrate primitives. Compute the Jacobian, the rule-type deformation tensor, the effective metric, and the constitutive tensors of the cloak. Establish the substrate-level mechanism by which the cloak topologically excludes a region from the chain's accessible substrate.*

---

## 1. Setup and Notation

A chain (P-MM-4) propagates through a substrate whose rule-type microstructure (P-MM-1, P-MM-2) has been deformed via a substrate-gradient deformation (P-MM-3) in the coarse-graining regime $\ell_P \ll a \ll \lambda \ll L$ (P-MM-6).

The substrate-gradient deformation is a smooth invertible map $\mathbf{R}: \mathbb{R}^3 \to \mathbb{R}^3$ that re-parameterizes the substrate's rule-type identity-labeling. The Jacobian of the deformation is

$$
J^i{}_j(\mathbf{X}) \equiv \frac{\partial R^i}{\partial X^j},
$$

and the rule-type deformation tensor is

$$
D_{ij}(\mathbf{X}) \equiv (J^{-1})^k{}_i\,(J^{-1})^l{}_j\,\delta_{kl}.
$$

For an initially-isotropic substrate ($\varepsilon^{kl} = \varepsilon_0\delta^{kl}$, $\mu^{kl} = \mu_0\delta^{kl}$), the constitutive tensors transform under the deformation via

$$
\varepsilon'^{ij}(\mathbf{X}) = \frac{1}{\det J}\,J^i{}_k\,J^j{}_l\,\varepsilon^{kl}, \qquad \mu'^{ij}(\mathbf{X}) = \frac{1}{\det J}\,J^i{}_k\,J^j{}_l\,\mu^{kl},
$$

producing position-dependent effective constitutive tensors in the deformed substrate.

This Memo specifies the explicit *cloaking deformation* — the Pendry 2006 transformation that maps a virtual point to a physical sphere, producing an invisibility cloak. We compute its Jacobian, effective metric, and constitutive tensors, and articulate the substrate-level meaning of cloaking.

The target results (Pendry 2006, orthonormal-basis components in physical coordinates):

$$
\varepsilon_{\hat r'} = \mu_{\hat r'} = \frac{R_2}{R_2 - R_1}\left(\frac{r' - R_1}{r'}\right)^2,
$$

$$
\varepsilon_{\hat \theta'} = \mu_{\hat \theta'} = \varepsilon_{\hat \phi'} = \mu_{\hat \phi'} = \frac{R_2}{R_2 - R_1}.
$$

These will be derived from the substrate-level deformation specification.

---

## 2. (A) The Cloaking Map

### 2.1 Definition of the deformation

The Pendry 2006 spherical cloak is defined by a radial map between *virtual* coordinates $(r, \theta, \phi)$ — the un-deformed substrate's coordinate system — and *physical* coordinates $(r', \theta', \phi')$ — the deformed-substrate coordinate system in which the chain experiences the cloak.

The map is

$$
\boxed{\quad r' = R_1 + \frac{R_2 - R_1}{R_2}\, r, \qquad \theta' = \theta, \qquad \phi' = \phi. \quad}
$$

The parameters:
- $R_1$ — inner radius of the cloak. The cloaked (excluded) region is $r' < R_1$.
- $R_2$ — outer radius of the cloak. For $r' > R_2$ the substrate matches vacuum.
- $R_2 > R_1 > 0$.

**Range of variables:**
- Virtual $r \in [0, R_2]$ maps to physical $r' \in [R_1, R_2]$.
- Virtual $r = 0$ (a point) maps to physical $r' = R_1$ (a sphere of finite radius).
- Virtual $r = R_2$ (a sphere) maps to physical $r' = R_2$ (the same sphere).

**Inverse map:**

$$
r = \frac{R_2}{R_2 - R_1}\,(r' - R_1), \qquad \theta = \theta', \qquad \phi = \phi'.
$$

The inverse is well-defined for $r' \in [R_1, R_2]$. For $r' < R_1$ the inverse does not exist — the cloaked interior has no virtual pre-image.

### 2.2 Notation for compactness

For brevity, define

$$
\alpha \equiv \frac{R_2 - R_1}{R_2}, \qquad \beta \equiv \frac{R_2}{R_2 - R_1} = \frac{1}{\alpha}.
$$

With this notation, the cloaking map is $r' = R_1 + \alpha r$ (virtual-to-physical) and $r = \beta(r' - R_1)$ (physical-to-virtual). Note $0 < \alpha < 1$ and $\beta > 1$.

### 2.3 Substrate-level meaning of the map

The cloaking deformation re-parameterizes the substrate's rule-type identity-labeling so that:

- **The virtual interior $r < R_2$** of the substrate is "stretched outward" into a *shell* in physical space.
- **The virtual point $r = 0$** is mapped to the *inner cloak surface* $r' = R_1$ in physical space.
- **The cloaked interior $r' < R_1$** in physical space is *not part of* the chain's accessible substrate — it has no virtual pre-image.

The substrate-level statement: the cloaking deformation creates a topologically excluded region in the chain's accessible substrate. No substrate-level rule-type identity has been assigned to the physical region $r' < R_1$ in the deformed configuration; the chain has no rule-type pathway leading there.

---

## 3. (A) The Jacobian of the Cloaking Map

### 3.1 Jacobian in spherical coordinates

In spherical coordinates, the Jacobian matrix of the map $(r, \theta, \phi) \mapsto (r', \theta', \phi')$ is diagonal:

$$
J^i{}_j = \frac{\partial x'^i}{\partial x^j} = \begin{pmatrix} \partial r'/\partial r & \partial r'/\partial \theta & \partial r'/\partial \phi \\ \partial \theta'/\partial r & \partial \theta'/\partial \theta & \partial \theta'/\partial \phi \\ \partial \phi'/\partial r & \partial \phi'/\partial \theta & \partial \phi'/\partial \phi \end{pmatrix} = \begin{pmatrix} \alpha & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.
$$

So in spherical coordinate basis (not orthonormal), the Jacobian is constant — *independent of position*. The deformation is a uniform radial stretching.

**Determinant in spherical coordinates:** $\det J|_\text{spherical} = \alpha$.

### 3.2 Orthonormal-basis "Jacobian"

In the orthonormal basis $\hat{\mathbf{e}}_{\hat r'}, \hat{\mathbf{e}}_{\hat \theta'}, \hat{\mathbf{e}}_{\hat \phi'}$ at physical point $(r', \theta', \phi')$, the orthonormal vectors are related to the orthonormal vectors in the virtual basis by an orthonormal-basis "Jacobian" $\hat\Lambda$ that includes the conversion factors $r' \to r'$ for arc-length along $\hat \theta'$ and $\hat \phi'$ directions.

Specifically, the orthonormal arc-length elements are:

$$
ds_{\hat r'} = dr', \qquad ds_{\hat \theta'} = r'\,d\theta', \qquad ds_{\hat \phi'} = r'\sin\theta'\,d\phi'.
$$

The corresponding orthonormal-basis Jacobian relating physical arc-lengths to virtual arc-lengths:

$$
\hat\Lambda = \begin{pmatrix} \partial s_{\hat r'}/\partial s_{\hat r} & 0 & 0 \\ 0 & \partial s_{\hat \theta'}/\partial s_{\hat \theta} & 0 \\ 0 & 0 & \partial s_{\hat \phi'}/\partial s_{\hat \phi} \end{pmatrix}.
$$

Compute each component:

**Radial:** $\partial s_{\hat r'}/\partial s_{\hat r} = \partial r'/\partial r = \alpha$.

**Polar angle:** $\partial s_{\hat \theta'}/\partial s_{\hat \theta} = \partial(r'\theta')/\partial(r\theta) = r'/r$ (since $\theta' = \theta$, fixed angle interval).

**Azimuthal:** $\partial s_{\hat \phi'}/\partial s_{\hat \phi} = r'\sin\theta'/(r\sin\theta) = r'/r$ (since $\theta' = \theta$).

So

$$
\hat\Lambda = \begin{pmatrix} \alpha & 0 & 0 \\ 0 & r'/r & 0 \\ 0 & 0 & r'/r \end{pmatrix}.
$$

With $r = \beta(r'-R_1)$:

$$
r'/r = \frac{r'}{\beta(r'-R_1)} = \frac{\alpha r'}{r'-R_1}.
$$

So

$$
\hat\Lambda = \begin{pmatrix} \alpha & 0 & 0 \\ 0 & \alpha r'/(r'-R_1) & 0 \\ 0 & 0 & \alpha r'/(r'-R_1) \end{pmatrix}.
$$

### 3.3 Determinant of the orthonormal-basis Jacobian

$$
\det \hat\Lambda = \alpha \cdot \left(\frac{\alpha r'}{r'-R_1}\right)^2 = \frac{\alpha^3 r'^2}{(r'-R_1)^2}.
$$

### 3.4 Inverse orthonormal Jacobian

$$
\hat\Lambda^{-1} = \begin{pmatrix} 1/\alpha & 0 & 0 \\ 0 & (r'-R_1)/(\alpha r') & 0 \\ 0 & 0 & (r'-R_1)/(\alpha r') \end{pmatrix}.
$$

### 3.5 Behavior at the boundaries

**At $r' = R_1$:** $(r'-R_1)/r' \to 0$, so the angular components of $\hat\Lambda^{-1}$ go to zero. Equivalently, the angular components of $\hat\Lambda$ diverge: $\alpha r'/(r'-R_1) \to \infty$. This is the substrate-level statement that the deformation maps a single virtual point ($r = 0$) to an entire physical sphere ($r' = R_1$) — an infinite stretching in angular directions at the inner boundary.

**At $r' = R_2$:** $(r'-R_1)/r' = (R_2-R_1)/R_2 = \alpha$, so the angular components are $\alpha \cdot R_2/(R_2-R_1) \cdot (R_2-R_1)/R_2 = 1$. Wait — let me recompute: $\alpha r'/(r'-R_1) = \alpha R_2 /(R_2 - R_1) = \alpha \beta = 1$. So at the outer boundary, the orthonormal Jacobian components are $\alpha$ (radial) and $1$ (angular).

The outer boundary's Jacobian does not equal identity — there is a *radial* mismatch by factor $\alpha$ at $r' = R_2$. This produces the well-known property that the Pendry cloak's individual $\varepsilon, \mu$ values do not match vacuum at $r' = R_2$, even though the wave impedance does (cloak is impedance-matched but not vacuum-matched in individual constitutive components).

---

## 4. (B) The Effective Metric

### 4.1 Rule-type deformation tensor in orthonormal spherical basis

The rule-type deformation tensor is

$$
D_{ij}(\mathbf{X}) = (\hat\Lambda^{-1})^k{}_i\,(\hat\Lambda^{-1})^l{}_j\,\delta_{kl}.
$$

With $\hat\Lambda^{-1}$ diagonal as computed:

$$
D_{\hat r' \hat r'} = (1/\alpha)^2 = 1/\alpha^2 = \beta^2,
$$

$$
D_{\hat \theta'\hat \theta'} = D_{\hat \phi'\hat \phi'} = \left(\frac{r'-R_1}{\alpha r'}\right)^2 = \beta^2\left(\frac{r'-R_1}{r'}\right)^2 \cdot \frac{1}{\beta^2} = \left(\frac{r'-R_1}{\alpha r'}\right)^2.
$$

Simplifying: with $1/\alpha = \beta$:

$$
D_{\hat \theta'\hat \theta'} = \beta^2 \left(\frac{r'-R_1}{r'}\right)^2.
$$

Wait, let me redo this carefully. $\hat\Lambda^{-1}_{\hat\theta'} = (r'-R_1)/(\alpha r')$, so $D_{\hat\theta'\hat\theta'} = \left[(r'-R_1)/(\alpha r')\right]^2 = (r'-R_1)^2/(\alpha^2 r'^2) = \beta^2(r'-R_1)^2/r'^2$.

So the rule-type deformation tensor components in orthonormal spherical basis are:

$$
\boxed{\quad D_{\hat r' \hat r'} = \beta^2, \qquad D_{\hat \theta' \hat \theta'} = D_{\hat \phi' \hat \phi'} = \beta^2\left(\frac{r'-R_1}{r'}\right)^2. \quad}
$$

These are the effective-metric components (per Memo 8's identification $g_{ij} = D_{ij}$).

### 4.2 Effective metric in orthonormal basis

$$
\boxed{\quad g_{\hat r' \hat r'} = \beta^2, \qquad g_{\hat \theta' \hat \theta'} = g_{\hat \phi' \hat \phi'} = \beta^2\left(\frac{r'-R_1}{r'}\right)^2. \quad}
$$

**Inverse metric components** (diagonal, so each $g^{\hat i \hat i} = 1/g_{\hat i \hat i}$):

$$
g^{\hat r' \hat r'} = 1/\beta^2 = \alpha^2, \qquad g^{\hat \theta' \hat \theta'} = g^{\hat \phi' \hat \phi'} = \alpha^2\left(\frac{r'}{r'-R_1}\right)^2.
$$

### 4.3 Volume element

$$
\det g = g_{\hat r'\hat r'}\cdot g_{\hat \theta'\hat \theta'}\cdot g_{\hat \phi'\hat \phi'} = \beta^2 \cdot \beta^4 \left(\frac{r'-R_1}{r'}\right)^4 = \beta^6 \left(\frac{r'-R_1}{r'}\right)^4.
$$

$$
\sqrt{|g|} = \beta^3 \left(\frac{r'-R_1}{r'}\right)^2.
$$

Cross-check with $\sqrt{|g|} = 1/\det J|_\text{orthonormal} = 1/(\alpha^3 r'^2/(r'-R_1)^2) = (r'-R_1)^2/(\alpha^3 r'^2) = \beta^3(r'-R_1)^2/r'^2 = \beta^3(r'-R_1)^2/r'^2$.

Matches.

### 4.4 Behavior of the metric at the boundaries

**At $r' = R_1$:** $D_{\hat\theta'\hat\theta'} \to 0$, $D_{\hat\phi'\hat\phi'} \to 0$. The angular components of the metric vanish. The volume element $\sqrt{|g|} \to 0$. The metric is *degenerate* at the inner boundary.

The substrate-level statement: at $r' = R_1$, the chain's effective angular distances shrink to zero. The inner boundary is a single virtual point ($r = 0$); the entire sphere $r' = R_1$ in physical space corresponds to this one virtual point, so the chain experiences zero angular extent there.

**At $r' = R_2$:** $D_{\hat\theta'\hat\theta'} = \beta^2((R_2-R_1)/R_2)^2 = \beta^2 \alpha^2 = 1$. The angular components match vacuum. $D_{\hat r'\hat r'} = \beta^2$ does not match (radial mismatch).

---

## 5. (C) The Transformed Constitutive Tensors

### 5.1 Transformation formula in orthonormal basis

For an initially-isotropic substrate with $\varepsilon^{\hat i \hat j}_\text{virt} = \varepsilon_0 \delta^{\hat i \hat j}$ and $\mu^{\hat i \hat j}_\text{virt} = \mu_0 \delta^{\hat i \hat j}$, the transformation formula in orthonormal basis becomes (for diagonal components in a diagonal Jacobian setting):

$$
\varepsilon'^{\hat i \hat i}_\text{phys} = \frac{(\hat\Lambda^{\hat i \hat i})^2}{\det \hat\Lambda}\,\varepsilon_0 \qquad \text{(no sum)},
$$

and analogously for $\mu$.

### 5.2 Radial component

$$
\varepsilon'_{\hat r' \hat r'} = \frac{(\hat\Lambda^{\hat r' \hat r'})^2}{\det \hat\Lambda}\,\varepsilon_0 = \frac{\alpha^2}{\alpha^3 r'^2/(r'-R_1)^2}\,\varepsilon_0 = \frac{(r'-R_1)^2}{\alpha r'^2}\,\varepsilon_0 = \beta \cdot \left(\frac{r'-R_1}{r'}\right)^2 \varepsilon_0.
$$

Equivalently, in *relative* form (normalized to vacuum $\varepsilon_0$):

$$
\boxed{\quad \varepsilon_{\hat r'}/\varepsilon_0 = \mu_{\hat r'}/\mu_0 = \frac{R_2}{R_2 - R_1}\left(\frac{r' - R_1}{r'}\right)^2. \quad}
$$

This is the Pendry 2006 radial component, derived from the substrate-level deformation specification.

### 5.3 Angular components

$$
\varepsilon'_{\hat \theta' \hat \theta'} = \frac{(\hat\Lambda^{\hat \theta'\hat\theta'})^2}{\det \hat\Lambda}\,\varepsilon_0 = \frac{(\alpha r'/(r'-R_1))^2}{\alpha^3 r'^2/(r'-R_1)^2}\,\varepsilon_0 = \frac{\alpha^2 r'^2/(r'-R_1)^2}{\alpha^3 r'^2/(r'-R_1)^2}\,\varepsilon_0 = \frac{1}{\alpha}\,\varepsilon_0 = \beta\,\varepsilon_0.
$$

In relative form:

$$
\boxed{\quad \varepsilon_{\hat \theta'}/\varepsilon_0 = \mu_{\hat \theta'}/\mu_0 = \varepsilon_{\hat \phi'}/\varepsilon_0 = \mu_{\hat \phi'}/\mu_0 = \frac{R_2}{R_2 - R_1}. \quad}
$$

The angular components are constant throughout the cloak shell. This is the Pendry 2006 angular result.

### 5.4 Summary of the cloak constitutive tensors

In orthonormal spherical basis at physical point $(r', \theta', \phi')$ in the cloak shell $R_1 \leq r' \leq R_2$:

$$
\varepsilon_{\hat r'}/\varepsilon_0 = \mu_{\hat r'}/\mu_0 = \frac{R_2}{R_2 - R_1}\left(\frac{r' - R_1}{r'}\right)^2 \quad \text{(radial component, varies with } r'\text{)},
$$

$$
\varepsilon_{\hat \theta'}/\varepsilon_0 = \mu_{\hat \theta'}/\mu_0 = \varepsilon_{\hat \phi'}/\varepsilon_0 = \mu_{\hat \phi'}/\mu_0 = \frac{R_2}{R_2 - R_1} \quad \text{(angular components, constant)}.
$$

Off-diagonal components are zero: the cloak is *diagonal anisotropic* in orthonormal spherical basis.

### 5.5 Refractive-index structure

The local effective refractive index components are $n_i = \sqrt{\varepsilon_{\hat i}\mu_{\hat i}/(\varepsilon_0\mu_0)}$. For the cloak:

$$
n_{\hat r'} = \frac{R_2}{R_2 - R_1}\left(\frac{r' - R_1}{r'}\right)^2, \qquad n_{\hat \theta'} = n_{\hat \phi'} = \frac{R_2}{R_2 - R_1}.
$$

At $r' = R_1$: $n_{\hat r'} = 0$, while $n_{\hat \theta'} = n_{\hat \phi'} = R_2/(R_2-R_1) > 1$. The chain experiences *zero refractive index in the radial direction* at the inner boundary — the radial propagation rate is "infinite" (or, equivalently, the radial component of the wave equation degenerates).

This is the key feature: rays approaching $r' = R_1$ are forced to bend into the angular directions (because $n_{\hat r'} \to 0$ but $n_{\hat \theta'}, n_{\hat \phi'} > 0$). The chain cannot propagate radially at the inner boundary; it propagates tangentially around the inner sphere.

### 5.6 Impedance matching at $r' = R_2$

The wave impedance in the cloak is $Z = \sqrt{\mu/\varepsilon}$. With $\varepsilon_{\hat i} = \mu_{\hat i}$ everywhere (per the formulas above), the cloak has impedance $Z = \sqrt{\mu_0/\varepsilon_0}$ — exactly the vacuum impedance — everywhere in the shell.

At $r' = R_2$, the cloak's wave impedance matches vacuum's wave impedance. Therefore, no reflection occurs at the outer boundary, despite the individual $\varepsilon$ and $\mu$ values not equaling 1 there.

The substrate-level statement: the cloak's rule-type microstructure is engineered to maintain $\varepsilon = \mu$ everywhere, producing a "magnetically and electrically matched" effective medium that admits chains from vacuum without reflection.

---

## 6. (D) Substrate-Level Interpretation of Cloaking

### 6.1 Topological exclusion of the interior

The cloaking deformation $\mathbf{R}(\mathbf{x})$ maps the *entire virtual interior $r < R_2$* (including $r = 0$) onto the *physical shell $R_1 \leq r' \leq R_2$*. The physical region $r' < R_1$ has *no virtual pre-image*.

The substrate-level statement: in the deformed substrate, no rule-type identity has been assigned to the physical interior $r' < R_1$. The chain's accessible substrate excludes this region. There are no rule-type pathways leading into the cloaked interior because no rule-type structure exists there in the deformed configuration.

This is *not* a barrier the chain bumps against. It is the complete absence of substrate-level rule-type structure in the cloaked region. The chain literally cannot propagate into the interior because no propagation medium has been deployed there.

### 6.2 Radial compression of rule-type microstructure

The radial component of the Jacobian is $\partial r'/\partial r = \alpha = (R_2-R_1)/R_2 < 1$. The deformation *compresses* the virtual radial interval $[0, R_2]$ (length $R_2$) onto the physical shell $[R_1, R_2]$ (length $R_2 - R_1$). The compression factor is $\alpha < 1$.

Substrate-level reading: the virtual rule-type microstructure that filled the entire virtual sphere has been *radially compressed* into the physical shell. The shell carries more rule-type microstructure per unit radial distance than virtual space did.

The effective radial constitutive response is correspondingly enhanced. Specifically, $\varepsilon_{\hat r'}/\varepsilon_0 = \beta(r'-R_1)^2/r'^2$:

- At $r' \to R_2$: $\varepsilon_{\hat r'}/\varepsilon_0 \to \beta\alpha^2 = \alpha < 1$, less than vacuum (this is the radial mismatch noted in §3.5).
- At $r' \to R_1$: $\varepsilon_{\hat r'}/\varepsilon_0 \to 0$, vanishing radial response.

The vanishing radial response at $r' \to R_1$ is the substrate-level statement that *the compressed rule-type microstructure becomes singular at the inner boundary*: an infinite amount of virtual rule-type structure (the entire virtual interior) has been compressed onto the single inner shell, producing a divergence-like response that prevents any radial chain propagation at that boundary.

### 6.3 Angular stretching of rule-type microstructure

The angular components of the orthonormal Jacobian are $\hat\Lambda^{\hat\theta'\hat\theta'} = \alpha r'/(r'-R_1)$. At $r' \to R_1$, this diverges: the angular arc-length in physical space is much larger than in virtual space. The deformation *stretches* angular distances near the inner boundary.

Substrate-level reading: the virtual point $r = 0$ has been *angularly stretched* into the entire inner sphere $r' = R_1$. A single virtual rule-type identity (at the origin) has been replicated angularly to cover an entire sphere in physical space.

The effective angular constitutive response is correspondingly enhanced: $\varepsilon_{\hat\theta'}/\varepsilon_0 = \beta > 1$. The angular response is constant throughout the shell (not position-dependent), reflecting that the angular stretching has the same rate everywhere in the cloak.

### 6.4 The chain's experience traversing the cloak

A chain approaching the cloak from outside ($r' > R_2$, vacuum) and heading toward the cloaked region $r' < R_1$ experiences:

1. **Entry at $r' = R_2$**: smooth transition (impedance-matched). The chain enters the shell without reflection.

2. **Propagation in the shell** ($R_1 < r' < R_2$): the chain's coarse-grained trajectory bends. The position-dependent radial constitutive component $\varepsilon_{\hat r'}/\varepsilon_0 \to 0$ as $r' \to R_1$ causes the wave-vector's radial component to vanish; the wave bends into the angular direction.

3. **Approach to the inner boundary** ($r' \to R_1$): the chain's trajectory becomes tangential to the inner sphere. The chain cannot proceed radially inward because the radial constitutive response vanishes.

4. **Tangential propagation around the inner sphere**: the chain circulates around the inner sphere (geodesics of the effective metric).

5. **Continuation around the cloak**: the chain's tangential propagation eventually carries it around the cloak and out the far side.

6. **Exit at $r' = R_2$**: smooth transition back to vacuum (impedance-matched). The chain emerges on the far side of the cloak as if no obstacle had been present.

The chain *never enters* the cloaked interior $r' < R_1$. From the chain's vantage, the cloaked region is invisible — it does not interact with the chain because the chain has no rule-type pathway to it.

### 6.5 Why this is "invisibility"

From outside the cloak, an observer sees the chain emerging from the cloak shell as if it had traveled through empty space. The chain's trajectory has been bent around the cloak; its arrival time and direction are exactly what they would have been if no cloak (and no cloaked region) had been present.

The substrate-level reading: the cloak does not "hide" anything in the conventional sense. The cloaked interior is not concealed behind a barrier; it is excluded from the chain's accessible substrate entirely. Anything placed inside the cloaked region (any structure with $r' < R_1$ that would normally interact with chains) has no rule-type contact with the chain — they exist in disjoint accessible-substrate regions.

The cloak is an *engineered topological exclusion*: by deforming the substrate's rule-type identity-labeling, the cloak creates a region of physical space that is structurally invisible to the chain because the chain has no rule-type pathway to interact with it.

---

## 7. Geodesic Structure of the Cloak

### 7.1 Ray-optics limit

In the high-frequency limit ($\omega \gg c/R_2$), the chain's propagation is described by the eikonal equation and ray trajectories follow geodesics of the effective metric. The geodesic equation in spherical coordinates with the cloak metric

$$
g_{\hat r'\hat r'} = \beta^2, \qquad g_{\hat\theta'\hat\theta'} = g_{\hat\phi'\hat\phi'} = \beta^2(r'-R_1)^2/r'^2,
$$

is derived from the geodesic Lagrangian

$$
\mathcal{L} = \frac{1}{2}g_{ij}\,\dot x^i\dot x^j = \frac{\beta^2}{2}\!\left[\dot r'^2 + (r'-R_1)^2/r'^2 \cdot r'^2(\dot\theta'^2 + \sin^2\theta'\,\dot\phi'^2)\right].
$$

Wait, let me be careful with the orthonormal basis vs. coordinate basis distinction. The coordinate-basis metric (which is what enters the geodesic equation) has

$$
g_{r'r'}^\text{coord} = g_{\hat r' \hat r'} = \beta^2, \qquad g_{\theta'\theta'}^\text{coord} = r'^2\cdot g_{\hat\theta'\hat\theta'}/r'^2 = (r'-R_1)^2 \beta^2/r'^2 \cdot r'^2 / r'^2 \cdot r'^2 = \beta^2(r'-R_1)^2.
$$

Actually: $g_{\hat\theta'\hat\theta'}$ orthonormal = $g_{\theta'\theta'}^\text{coord} \cdot (1/r')^2 \cdot (1/r')^{-2}$... Let me redo more carefully.

For an orthonormal frame $\hat e_{\hat r'} = \partial_{r'}$, $\hat e_{\hat\theta'} = (1/r')\partial_{\theta'}$, $\hat e_{\hat\phi'} = (1/(r'\sin\theta'))\partial_{\phi'}$:

Coordinate metric component $g_{\theta'\theta'} = g(\partial_{\theta'}, \partial_{\theta'}) = g(r'\hat e_{\hat\theta'}, r'\hat e_{\hat\theta'}) = r'^2 g(\hat e_{\hat\theta'}, \hat e_{\hat\theta'}) = r'^2 \cdot g_{\hat\theta'\hat\theta'}$.

So $g_{\theta'\theta'}^\text{coord} = r'^2 \cdot \beta^2(r'-R_1)^2/r'^2 = \beta^2(r'-R_1)^2$.

Similarly $g_{\phi'\phi'}^\text{coord} = r'^2\sin^2\theta' \cdot \beta^2(r'-R_1)^2/r'^2 = \beta^2(r'-R_1)^2\sin^2\theta'$.

And $g_{r'r'}^\text{coord} = \beta^2$.

The coordinate-basis cloak metric is therefore

$$
ds^2_\text{cloak,coord} = \beta^2[dr'^2 + (r'-R_1)^2\,d\theta'^2 + (r'-R_1)^2\sin^2\theta'\,d\phi'^2].
$$

This is conformal to a flat metric centered at $r' = R_1$ with radial coordinate $\rho \equiv r' - R_1$:

$$
ds^2_\text{cloak,coord} = \beta^2[d\rho^2 + \rho^2 d\theta'^2 + \rho^2\sin^2\theta' d\phi'^2] = \beta^2 ds^2_\text{flat}(\rho, \theta', \phi').
$$

So the effective metric in the cloak is *flat geometry centered at the inner boundary*, scaled by $\beta^2$.

### 7.2 The chain's geodesics

In flat geometry (after the conformal rescaling), the chain's geodesics are *straight lines* in the $(\rho, \theta', \phi')$ space. The conformal factor $\beta^2$ does not affect geodesic shapes (only the affine parameterization), so the chain follows straight lines in the $(\rho, \theta', \phi')$ system.

Map these straight lines back to physical $(r', \theta', \phi')$: with $\rho = r' - R_1$, the chain's geodesics in physical space are straight lines in the *shifted-radial* coordinate system.

The substrate-level reading: in the cloak, the chain propagates *as if it were in vacuum but with the inner boundary $r' = R_1$ playing the role of the origin*. The chain traverses the cloak as if traversing flat space; the "obstacle" at $r' < R_1$ has been smoothly mapped to a single point that the geodesics simply avoid (you cannot pass through a point in 3D).

### 7.3 Why the chain's trajectory bends around the cloak

In the cloak's effective flat metric centered at $r' = R_1$, a chain entering at $r' = R_2$ heading toward $r' = 0$ would, in the flat-coordinate picture, head toward $\rho = -R_1$ — a non-existent point. Equivalently, the chain's trajectory in the cloak's flat space cannot reach the origin $\rho = 0$ (which corresponds to $r' = R_1$).

In the physical coordinate system, this manifests as: the chain enters the shell at $r' = R_2$, propagates inward, but its trajectory smoothly bends around the inner sphere $r' = R_1$ without ever reaching it. The chain emerges on the far side at $r' = R_2$ with its straight-line propagation having traversed the entire cloak shell.

### 7.4 Substrate-level summary

The chain's geodesic structure in the cloak is *equivalent* to free-space propagation in a flat geometry where:
- The cloaked interior $r' < R_1$ has been "removed" (mapped to a single point).
- The cloak shell $R_1 \leq r' \leq R_2$ has been "stretched" to accommodate the removal.
- Chains traverse straight lines in this re-mapped flat geometry.

The substrate-level mechanism: the deformation has restructured the chain's accessible substrate so that what was previously a point at the cloak's center is now an entire inner sphere, and what was previously the interior is now excluded. Chains that would have passed through the center now bend around the inner sphere because there is no substrate there.

---

## 8. (E) Preparation for Memo 10: ED-Gradient Reading

Memo 10 will articulate the substrate-level reading of invisibility cloaking in full. This Memo prepares two key concepts.

### 8.1 ED-gradient interpretation of the deformation

The substrate-gradient deformation $\mathbf{R}(\mathbf{x}) = \mathbf{x} + \mathbf{u}(\mathbf{X})$ (Memo 7) re-parameterizes the substrate's rule-type identity-labeling. The cloaking deformation has displacement field

$$
\mathbf{u}(r', \theta, \phi) = (\beta(r' - R_1) - r')\,\hat r' = -(r' - R_1)/\alpha \cdot (1 - \beta)\hat r' = \ldots
$$

More directly: the virtual radius at physical $r'$ is $r = \beta(r' - R_1)$, so the displacement is $u^{\hat r'} = r' - r = r' - \beta(r' - R_1)$. Compute:

$$
u^{\hat r'}(r') = r' - \beta(r' - R_1) = r'(1 - \beta) + \beta R_1 = -\frac{R_1}{\alpha}(1 - r'/R_2) \cdot \alpha = -R_1(1 - r'/R_2).
$$

Wait, let me redo: $1 - \beta = 1 - 1/\alpha = (\alpha - 1)/\alpha = -(1-\alpha)/\alpha = -R_1/(R_2-R_1)$... actually $\alpha = (R_2-R_1)/R_2$ so $1 - \alpha = R_1/R_2$ and $(1-\alpha)/\alpha = R_1/(R_2-R_1)$. So $1 - \beta = -R_1/(R_2-R_1)$.

$u^{\hat r'}(r') = r'(1-\beta) + \beta R_1 = -r' R_1/(R_2-R_1) + R_1 R_2/(R_2-R_1) = R_1(R_2 - r')/(R_2-R_1) = R_1 \cdot \beta \cdot \alpha (1 - r'/R_2) \cdot 1/\alpha = R_1(1 - r'/R_2)/\alpha$.

Hmm let me try differently. We want to express the displacement $u$ such that $r = r' - u$ (or $r' = r + u$, depending on convention). With $r' = R_1 + \alpha r$ and $r = \beta(r' - R_1)$:

$r' - r = r' - \beta(r' - R_1) = r'(1 - \beta) + \beta R_1$

At $r' = R_2$: $r' - r = R_2(1 - \beta) + \beta R_1 = R_2 - \beta R_2 + \beta R_1 = R_2 - \beta(R_2 - R_1) = R_2 - 1 = R_2 - R_2 = 0$. Good, identity at outer boundary.

At $r' = R_1$: $r' - r = R_1(1 - \beta) + \beta R_1 = R_1$. So displacement is $R_1$ at inner boundary: the virtual origin ($r = 0$) is at the same physical location as $r' = R_1$, so the displacement is $r' - r = R_1 - 0 = R_1$.

So the displacement field of the cloaking deformation is:

$$
u^{\hat r'}(r') = r' - r(r') = r' - \beta(r' - R_1) = R_1\!\left(1 - \frac{r' - R_1}{R_2 - R_1}\cdot\frac{R_2}{R_2}\right)\cdot\ldots
$$

Let me just simplify: $u^{\hat r'}(r') = r'(1-\beta) + \beta R_1$. Substituting $\beta = R_2/(R_2-R_1)$:

$u^{\hat r'}(r') = r' - r'\cdot R_2/(R_2-R_1) + R_1 R_2/(R_2-R_1) = r' - R_2(r' - R_1)/(R_2 - R_1)$.

Or: $u^{\hat r'}(r') = R_1\cdot(R_2 - r')/(R_2 - R_1)$ (after algebra).

Check: at $r' = R_2$: $u = 0$. At $r' = R_1$: $u = R_1\cdot(R_2 - R_1)/(R_2 - R_1) = R_1$. ✓

So the displacement field is

$$
\boxed{\quad u^{\hat r'}(r') = R_1\,\frac{R_2 - r'}{R_2 - R_1}. \quad}
$$

This is the substrate-level *ED-gradient deformation* (P-MM-3) specifying the cloak: a radial inward displacement that equals $R_1$ at the inner boundary $r' = R_1$ and zero at the outer boundary $r' = R_2$.

### 8.2 ED-gradient meaning of cloaking

The substrate-level reading: the cloaking deformation is an ED-gradient (P-MM-3) that *radially compresses* the substrate's rule-type identity-labeling toward the inner boundary. At each radius $r'$ in the cloak shell, the substrate's rule-type identity is what would have existed at the smaller virtual radius $r = \beta(r' - R_1)$ in the un-deformed substrate.

The displacement increases linearly from zero at $r' = R_2$ (no shift) to $R_1$ at $r' = R_1$ (the maximum shift, equal to the cloak's inner radius). The gradient $\partial u^{\hat r'}/\partial r' = -R_1/(R_2-R_1)$ is constant — the deformation is *uniform* in the sense that the rate of rule-type-shift is the same at every radius in the shell.

The chain experiences this uniform deformation as the position-dependent effective constitutive tensors derived in §5. The radial-versus-angular asymmetry of those tensors reflects the directional asymmetry of the deformation: radially inward there is rule-type compression; angularly there is rule-type stretching (because the virtual point at $r = 0$ has been "spread out" into a sphere).

### 8.3 What Memo 10 will articulate

The substrate-level reading of invisibility cloaking:
- The cloaked interior is *not concealed* but *absent* from the chain's accessible substrate.
- The chain's coarse-grained geodesics avoid the inner boundary because no substrate exists beyond it.
- Cloaking is engineered *topological exclusion* via substrate-gradient deformation, not a passive concealment.
- The chain's experience emerging on the far side of the cloak is indistinguishable from free-space propagation, because the deformation has preserved the chain's coarse-grained trajectory while excluding the interior region.

---

## 9. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **The cloaking map $r' = R_1 + \alpha r$** (§2.1) as the canonical substrate-gradient deformation that maps a virtual point to a physical sphere. FORCED by P-MM-3 (substrate-gradient deformation primitive).

- **The diagonal Jacobian in spherical coordinates** $J = \text{diag}(\alpha, 1, 1)$ (§3.1). FORCED by the radial map preserving angular coordinates.

- **The orthonormal-basis Jacobian** $\hat\Lambda = \text{diag}(\alpha, r'/r, r'/r)$ (§3.2). FORCED by the conversion to physical arc-length elements.

- **The effective-metric components** $g_{\hat r'\hat r'} = \beta^2$, $g_{\hat\theta'\hat\theta'} = g_{\hat\phi'\hat\phi'} = \beta^2((r'-R_1)/r')^2$ (§4.1, §4.2). FORCED by the rule-type deformation tensor formula applied to the cloaking Jacobian.

- **The Pendry cloak constitutive tensors** $\varepsilon_{\hat r'}/\varepsilon_0 = \beta((r'-R_1)/r')^2$ and $\varepsilon_{\hat\theta'} = \varepsilon_{\hat\phi'} = \beta \varepsilon_0$ (§5.4). FORCED by the transformation-optics formula $\varepsilon'^{\hat i\hat i} = (\hat\Lambda^{\hat i\hat i})^2/\det\hat\Lambda \cdot \varepsilon_0$ applied to the orthonormal cloak Jacobian.

- **Identical formulas for $\mu$** since the transformation rule is identical (§5.4). FORCED.

- **Vanishing radial response at $r' = R_1$** (§5.5). FORCED by the deformation mapping a point to a sphere (infinite angular stretching at the inner boundary).

- **Constant angular response throughout the shell** (§5.4, §5.5). FORCED by the radial-only nature of the deformation.

- **Impedance matching at $r' = R_2$** (§5.6). FORCED by $\varepsilon = \mu$ everywhere in the cloak.

- **Topological exclusion of the cloaked interior** (§6.1). FORCED by the deformation having no inverse image for $r' < R_1$.

- **Tangential geodesic propagation at the inner boundary** (§7.2, §7.3). FORCED by the effective metric being conformal to flat space centered at $r' = R_1$.

- **Substrate-level interpretation of cloaking as topological-exclusion deformation** (§6, §8). FORCED.

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Spherical-coordinate calculus and orthonormal-basis conversions** (§3, §4). Standard.

- **Conformal-equivalence reading of the cloak metric to flat space centered at $r' = R_1$** (§7.1). Standard differential-geometry observation.

- **Ray-optics / eikonal-equation limit** (§7.1). Standard high-frequency limit of Maxwell's equations.

- **Impedance-matching theory at electromagnetic interfaces** (§5.6). Standard EM.

### What remains OPEN

- **Sharp deformation at the inner boundary**: the cloaking map has divergent Jacobian components as $r' \to R_1$. Regularizations (smooth cloaks, finite-thickness boundary layers) are needed for practical implementation. OPEN at full-substrate-level treatment of the boundary-layer behavior.

- **Broadband cloaking**: the Pendry cloak's $\varepsilon, \mu$ values are FORCED by the deformation but typically only achievable over a narrow frequency window in real metamaterials (because the underlying microstructure has dispersion). Substrate-level treatment of broadband cloaking limitations is OPEN.

- **Polarization effects**: the cloak's $\varepsilon = \mu$ matching is an idealization. Real cloaks have polarization-dependent imperfections. OPEN.

- **Cylindrical and 2D cloaks**: the spherical cloak treated here is the prototype; cylindrical (Pendry 2006) and 2D (Schurig 2006) cloaks follow the same structural argument with adjusted geometry. The substrate-level reading is identical; explicit derivations parallel this Memo's.

- **Non-Euclidean cloaks**: Leonhardt 2006 invisibility based on conformal mapping (Riemann sheets) uses different deformation structure. OPEN.

- **Active and time-varying cloaks**: cloaks that respond dynamically to incoming waves. OPEN.

- **Quantum cloaks**: single-photon-level effects in cloaks. OPEN.

- **Cloaks for fields other than EM** (acoustic, elastodynamic, matter waves). The substrate-level transformation-optics framework applies; specific constitutive transformations differ. OPEN.

---

## 10. Review and Recommended Next Steps

### Review

Memo 9 has delivered:

- **The cloaking map** $r' = R_1 + \alpha r$ with $\alpha = (R_2 - R_1)/R_2$, mapping virtual point $r = 0$ to physical sphere $r' = R_1$ (§2).

- **The Jacobian** in spherical coordinates ($J = \text{diag}(\alpha, 1, 1)$) and orthonormal spherical basis ($\hat\Lambda = \text{diag}(\alpha, r'/r, r'/r)$) (§3).

- **The effective metric components** $g_{\hat r'\hat r'} = \beta^2$, $g_{\hat\theta'\hat\theta'} = g_{\hat\phi'\hat\phi'} = \beta^2((r'-R_1)/r')^2$ in orthonormal basis (§4), with explicit volume element $\sqrt{|g|} = \beta^3(r'-R_1)^2/r'^2$.

- **The Pendry cloak constitutive tensors** $\varepsilon_{\hat r'}/\varepsilon_0 = \mu_{\hat r'}/\mu_0 = \beta((r'-R_1)/r')^2$ and $\varepsilon_{\hat\theta'}/\varepsilon_0 = \mu_{\hat\theta'}/\mu_0 = \varepsilon_{\hat\phi'}/\varepsilon_0 = \mu_{\hat\phi'}/\mu_0 = \beta$ (§5), exactly matching the Pendry 2006 formulas, derived from the substrate-level deformation specification.

- **Vanishing radial constitutive response at $r' = R_1$ and impedance matching at $r' = R_2$** (§5.5, §5.6).

- **Substrate-level interpretation** of cloaking as topological exclusion: the cloaked interior is absent from the chain's accessible substrate (§6.1). Radial compression and angular stretching of rule-type microstructure (§6.2–6.3).

- **The chain's experience** traversing the cloak: smooth entry at $r' = R_2$, bending around the inner sphere, smooth exit on the far side, never entering the cloaked interior (§6.4).

- **Substrate-level meaning of invisibility**: not concealment but exclusion; the cloaked region has no rule-type structure assigned to it in the deformed configuration (§6.5).

- **Geodesic structure** of the cloak: conformal to flat space centered at $r' = R_1$; chain's coarse-grained trajectories are straight lines that bend around the inner sphere because no substrate exists there (§7).

- **ED-gradient interpretation** of the cloaking deformation: radial inward displacement $u^{\hat r'}(r') = R_1(R_2 - r')/(R_2 - R_1)$ with constant gradient $-R_1/(R_2-R_1)$ (§8.1).

- **Preparation for Memo 10**: the substrate-level reading of invisibility cloaking will be articulated in full (§8.2, §8.3).

- **Explicit FORCED / FORM-FORCED-INHERITED / OPEN labeling** (§9).

### Honest scope-limit

Memo 9 introduced no new substrate primitives beyond P-MM-1 through P-MM-6 (Memo 1's inventory). The deformation map $r' = R_1 + \alpha r$ is treated as the canonical Pendry cloak; its derivation from substrate primitives is via P-MM-3 (substrate-gradient deformation). The transformation-optics machinery from Memos 7–8 is applied; the standard Pendry 2006 constitutive-tensor formulas are derived inline. No cross-references to other arcs.

The cloak's singular behavior at the inner boundary $r' \to R_1$ is treated at the level of structural form (vanishing radial response is FORCED); regularization for practical implementation is OPEN.

### Recommended next steps

In order:

1. **Memo 10 — Substrate-Level Reading of Invisibility Cloaking.** Articulate the full substrate-level interpretation:
   - Cloaking as substrate-level topological exclusion via ED-gradient deformation.
   - The chain's experience as free-space propagation in a flat metric with the cloaked interior removed.
   - Invisibility as the *absence of rule-type pathways* to the cloaked region.
   - Comparison with classical and standard transformation-optics readings of cloaking.

2. **Memo 11 — Conditions and Limits of Transformation Optics.** Identify when transformation optics works and when it fails:
   - Smooth deformations within homogenization regime: full validity.
   - Sharp deformations at cloak boundaries: regularization needed.
   - Broadband cloaking: dispersion limits.
   - Magnetic-electric coupling beyond standard transformation-optics: bianisotropy.
   - Substrate-level reading of each limit.

3. **Memo 12 — Substrate-Level Metasurface Boundary Conditions.** Independent line: derive the generalized Snell's law from rule-type discontinuities at interfaces (P-MM-5).

4. **Memo 13 — Synthesis.** Tie all three precursor derivations together. After Memo 13, the precursor Arc is complete and ready for the public-facing walkthrough.

### Anchor for future memos

The explicit Pendry cloak constitutive tensors derived in this Memo — $\varepsilon_{\hat r'}/\varepsilon_0 = \mu_{\hat r'}/\mu_0 = \beta((r'-R_1)/r')^2$ and $\varepsilon_{\hat\theta'} = \mu_{\hat\theta'} = \beta\varepsilon_0$ — are standardized as the substrate-level cloak result. Memo 10 will articulate the substrate-level meaning of these formulas as topological exclusion of the cloaked region. Memo 11 will analyze the limits of the transformation-optics machinery, particularly the inner-boundary singularity treated here at structural level.
