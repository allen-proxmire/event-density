# Memo 4 — Effective Constitutive Relations ($\varepsilon_{\mathrm{eff}}, \mu_{\mathrm{eff}}$)

**Arc Metamaterials, Memo 4 of 13.**
**Allen Proxmire** · May 2026

*Derive the homogenized effective wave equation from the order-$a^0$ solvability condition. Identify the effective constitutive tensors $\varepsilon_{\mathrm{eff}}^{ij}$ and $\mu_{\mathrm{eff}}^{ij}$ from substrate-level cell-problem solutions. Show how anisotropy and tensor structure emerge from rule-type microstructure.*

---

## 1. Setup and Notation

A chain (P-MM-4) propagates through a periodic rule-type substrate (P-MM-1 + P-MM-2) with unit-cell scale $a \ll \lambda \ll L$ (P-MM-6). The chain's pre-individuation amplitude $\psi(\mathbf{x})$ satisfies the scalar wave equation

$$
\partial_i\!\left[A^{ij}(\mathbf{x}/a)\, \partial_j \psi\right] + k_0^{2}\, B(\mathbf{x}/a)\, \psi = 0,
$$

where $A^{ij}(\mathbf{y})$ is the substrate's local rule-type kinetic-response tensor and $B(\mathbf{y})$ is the local potential-response scalar, both periodic on the unit cell $Y = [0,1]^d$:

$$
A^{ij}(\mathbf{y} + \mathbf{e}_k) = A^{ij}(\mathbf{y}), \qquad B(\mathbf{y} + \mathbf{e}_k) = B(\mathbf{y}).
$$

The two-scale lift is $\tilde\psi(\mathbf{X}, \mathbf{y})$ with $\mathbf{X} = \mathbf{x}$ (slow) and $\mathbf{y} = \mathbf{x}/a$ (fast). The asymptotic expansion is

$$
\tilde\psi(\mathbf{X}, \mathbf{y}) = \psi_0(\mathbf{X}, \mathbf{y}) + a\, \psi_1(\mathbf{X}, \mathbf{y}) + a^{2}\, \psi_2(\mathbf{X}, \mathbf{y}) + \ldots
$$

with each $\psi_n$ periodic in $\mathbf{y}$. The derivative-splitting rule is $\nabla_\mathbf{x} = \nabla_\mathbf{X} + a^{-1}\nabla_\mathbf{y}$.

Two prior results carried into this Memo:

**Result A** (order $a^{-2}$ analysis): $\psi_0(\mathbf{X}, \mathbf{y}) = \psi_0(\mathbf{X})$ — the leading-order amplitude is independent of the fast variable. The chain does not resolve the rule-type microstructure at probe scale $\lambda \gg a$.

**Result B** (order $a^{-1}$ analysis): the first-order correction has the form

$$
\psi_1(\mathbf{X}, \mathbf{y}) = \chi^j(\mathbf{y})\, \partial_{X^j}\psi_0(\mathbf{X}),
$$

where the *cell correctors* $\chi^j(\mathbf{y})$ for $j = 1, \ldots, d$ satisfy the *cell problem*

$$
L_\mathbf{y}[\chi^j(\mathbf{y})] = -\partial_{y^i} A^{ij}(\mathbf{y}),
$$

with the *cell operator* $L_\mathbf{y}[\phi] \equiv \partial_{y^i}\!\left[A^{ij}(\mathbf{y})\, \partial_{y^j}\phi(\mathbf{y})\right]$ acting on functions periodic on $Y$ with mean-zero normalization $\langle \chi^j \rangle = 0$.

The *averaging operator* is

$$
\langle f \rangle \;\equiv\; \frac{1}{|Y|}\int_Y f(\mathbf{y})\, d^dy.
$$

It is linear, commutes with $\partial_{X^j}$ (slow derivatives), and kills $\mathbf{y}$-divergences of periodic functions: $\langle \partial_{y^i} g^i \rangle = 0$ for any periodic $g^i(\mathbf{y})$.

This Memo's work:

1. Apply $\langle \cdot \rangle$ to the order-$a^0$ equation. Obtain the homogenized effective wave equation for $\psi_0(\mathbf{X})$.
2. Identify the effective tensor $A^{*ij}$ and effective scalar $B^*$.
3. Map the construction onto Maxwell's equations: identify $A^{ij}$ as the substrate-level pre-image of $\mu^{-1\,ij}$ (transverse-magnetic case) or $\varepsilon^{ij}$ (transverse-electric case).
4. Derive the effective permittivity and permeability tensors.
5. Show how rule-type-microstructure anisotropy produces tensor anisotropy in the effective parameters.

---

## 2. The Order-$a^0$ Solvability Condition

### 2.1 The order-$a^0$ equation

From the two-scale expansion, the order-$a^0$ equation reads

$$
\partial_{y^i}\!\left[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_2\right]
+ \partial_{X^i}\!\left[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_1\right]
+ \partial_{y^i}\!\left[A^{ij}(\mathbf{y})\, \partial_{X^j}\psi_1\right]
+ \partial_{X^i}\!\left[A^{ij}(\mathbf{y})\, \partial_{X^j}\psi_0\right]
+ k_0^{2}\, B(\mathbf{y})\, \psi_0 = 0.
$$

This is a periodic equation in $\mathbf{y}$ for the second-order correction $\psi_2(\mathbf{X}, \mathbf{y})$. By the Fredholm alternative for the periodic self-adjoint operator $L_\mathbf{y}$, a periodic solution $\psi_2$ exists if and only if the source (the sum of all terms except the $L_\mathbf{y}[\psi_2]$ piece) has zero mean over the unit cell.

The solvability condition is the *homogenized effective equation* — the macroscopic equation governing $\psi_0(\mathbf{X})$.

### 2.2 Applying the averaging operator

Apply $\langle\cdot\rangle$ to the order-$a^0$ equation. Term by term:

**Term 1:** $\langle \partial_{y^i}[A^{ij}\partial_{y^j}\psi_2]\rangle = 0$. This is the divergence-theorem identity: any $\mathbf{y}$-divergence of a periodic function averages to zero.

**Term 2:** $\langle \partial_{X^i}[A^{ij}\partial_{y^j}\psi_1]\rangle$. The slow derivative $\partial_{X^i}$ commutes with averaging:

$$
\langle \partial_{X^i}[A^{ij}\partial_{y^j}\psi_1]\rangle = \partial_{X^i}\langle A^{ij}\partial_{y^j}\psi_1\rangle.
$$

Substitute $\psi_1 = \chi^k(\mathbf{y})\partial_{X^k}\psi_0$, so $\partial_{y^j}\psi_1 = \partial_{y^j}\chi^k(\mathbf{y}) \cdot \partial_{X^k}\psi_0$. Since $\partial_{X^k}\psi_0$ is $\mathbf{y}$-independent, it factors out of the cell average:

$$
\partial_{X^i}\langle A^{ij}\partial_{y^j}\psi_1\rangle = \partial_{X^i}\!\left[\langle A^{ij}(\mathbf{y})\,\partial_{y^j}\chi^k(\mathbf{y})\rangle\, \partial_{X^k}\psi_0(\mathbf{X})\right].
$$

**Term 3:** $\langle \partial_{y^i}[A^{ij}\partial_{X^j}\psi_1]\rangle$. A $\mathbf{y}$-divergence of a periodic quantity — even though $\partial_{X^j}\psi_1$ depends on $\mathbf{X}$, the periodicity is in $\mathbf{y}$, and the inner quantity $A^{ij}(\mathbf{y})\partial_{X^j}\psi_1$ is periodic in $\mathbf{y}$ at fixed $\mathbf{X}$ — so this term averages to zero.

**Term 4:** $\langle \partial_{X^i}[A^{ij}\partial_{X^j}\psi_0]\rangle = \partial_{X^i}\langle A^{ij}(\mathbf{y})\rangle\,\partial_{X^j}\psi_0$, since $\partial_{X^j}\psi_0$ is $\mathbf{y}$-independent.

**Term 5:** $\langle k_0^{2} B(\mathbf{y}) \psi_0 \rangle = k_0^{2}\,\langle B(\mathbf{y})\rangle\,\psi_0(\mathbf{X})$.

Summing the averaged terms:

$$
\partial_{X^i}\!\left[\langle A^{ij}\partial_{y^j}\chi^k\rangle\, \partial_{X^k}\psi_0\right]
+ \partial_{X^i}\!\left[\langle A^{ij}\rangle\, \partial_{X^j}\psi_0\right]
+ k_0^{2}\,\langle B\rangle\,\psi_0 = 0.
$$

### 2.3 Consolidating into effective form

The first two terms can be combined into a single divergence by relabeling the dummy index $k$ to $j$ in the first term:

$$
\partial_{X^i}\!\left[\big(\langle A^{ij}\rangle + \langle A^{ik}\partial_{y^k}\chi^j\rangle\big)\, \partial_{X^j}\psi_0\right] + k_0^{2}\,\langle B\rangle\,\psi_0 = 0.
$$

Define the *effective tensor*

$$
\boxed{\quad A^{*ij} \;\equiv\; \langle A^{ij}(\mathbf{y})\rangle + \langle A^{ik}(\mathbf{y})\,\partial_{y^k}\chi^j(\mathbf{y})\rangle, \quad}
$$

and the *effective potential coefficient*

$$
\boxed{\quad B^* \;\equiv\; \langle B(\mathbf{y})\rangle. \quad}
$$

Then the homogenized effective equation reads

$$
\boxed{\quad
\partial_{X^i}\!\left[A^{*ij}\, \partial_{X^j}\psi_0(\mathbf{X})\right] + k_0^{2}\, B^*\, \psi_0(\mathbf{X}) = 0.
\quad}
$$

This is the *macroscopic* wave equation: a constant-coefficient equation for the leading-order amplitude $\psi_0(\mathbf{X})$, with the substrate's microstructure entering only through the cell-averaged effective constitutive parameters $A^{*ij}$ and $B^*$.

### 2.4 Structural symmetry of $A^{*ij}$

The effective tensor admits the equivalent symmetric form (derived in Memo 3, repeated for completeness)

$$
A^{*ij} = \big\langle A^{kl}(\mathbf{y})\,(\delta_i^k + \partial_{y^k}\chi^i)\,(\delta_j^l + \partial_{y^l}\chi^j)\big\rangle.
$$

This makes the symmetry $A^{*ij} = A^{*ji}$ manifest when $A^{ij} = A^{ji}$ (which holds for non-bianisotropic substrates). It also exhibits $A^{*ij}$ as a positive-semidefinite quadratic form, with the corrector $\chi^j$ acting as a "shape function" that distorts the cell-averaging in response to the macroscopic gradient direction.

### 2.5 Substrate-level reading of the effective equation

The macroscopic equation has the structure of a constant-coefficient wave equation in a homogeneous medium with effective parameters $A^{*ij}, B^*$. From the chain's vantage at probe scale $\lambda \gg a$, the substrate appears as a smooth medium with these effective coefficients. The actual rule-type microstructure — visible only at scale $a$ — has been integrated out through the cell-averaging and corrector machinery.

The effective constitutive parameters are substrate-level *coarse-grained rule-type response coefficients*. They are not material properties in any deeper sense — they are summary descriptors of how the substrate's rule-type microstructure responds to coarse-grained gradients on average.

---

## 3. Electromagnetic Identification

### 3.1 Maxwell's equations in a structured medium

In a medium with position-dependent rule-type response, Maxwell's equations (in the absence of free charges and currents) read

$$
\nabla\times \mathbf{E} = -\partial_t \mathbf{B}, \qquad \nabla\times \mathbf{H} = \partial_t \mathbf{D},
$$

with constitutive relations

$$
\mathbf{D} = \varepsilon(\mathbf{x})\, \mathbf{E}, \qquad \mathbf{B} = \mu(\mathbf{x})\, \mathbf{H},
$$

where $\varepsilon^{ij}(\mathbf{x})$ and $\mu^{ij}(\mathbf{x})$ are the local permittivity and permeability tensors. In a structured substrate (P-MM-1), these depend on $\mathbf{x}/a$ and are periodic on the unit cell.

For harmonic time dependence $\mathbf{E}, \mathbf{H} \propto e^{-i\omega t}$, eliminate $\mathbf{B} = \mu \mathbf{H}$ from $\nabla\times\mathbf{E} = i\omega \mu \mathbf{H}$ and substitute into $\nabla\times\mathbf{H} = -i\omega\varepsilon \mathbf{E}$:

$$
\nabla\times\!\left(\mu^{-1}(\mathbf{x})\,\nabla\times\mathbf{E}\right) = \omega^{2}\,\varepsilon(\mathbf{x})\,\mathbf{E}.
$$

This is the standard vector wave equation in a structured medium, with both $\mu^{-1}$ and $\varepsilon$ position-dependent.

### 3.2 Scalar reduction: TM and TE modes

For two-dimensional substrates (microstructure varying in the $xy$-plane, translation symmetry in $z$), Maxwell's equations decouple into two polarizations:

**Transverse-magnetic (TM) polarization.** $\mathbf{E} = E_z(\mathbf{x})\hat{\mathbf{z}}$. The wave equation reduces to

$$
\partial_i\!\left[\mu^{-1\,ij}(\mathbf{x}/a)\, \partial_j E_z\right] + \omega^{2}\, \varepsilon_{zz}(\mathbf{x}/a)\, E_z = 0,
$$

where $i, j$ run over $\{x, y\}$.

Identifying the substrate's coarse-grained kinetic-response tensor with the inverse magnetic permeability and the potential coefficient with the $z$-$z$ component of permittivity:

$$
\boxed{\quad A^{ij}(\mathbf{y}) \;\longleftrightarrow\; \mu^{-1\,ij}(\mathbf{y}), \qquad B(\mathbf{y}) \;\longleftrightarrow\; \varepsilon_{zz}(\mathbf{y}), \qquad k_0^{2} \;\longleftrightarrow\; \omega^{2}. \quad}
$$

The general homogenization machinery of Memos 2–3 then applies directly. The TM mode's effective propagation in the homogenized medium is governed by

$$
\partial_{X^i}\!\left[\mu^{-1\,ij}_\text{eff}\, \partial_{X^j} E_z\right] + \omega^{2}\,\varepsilon^\text{eff}_{zz}\, E_z = 0,
$$

with

$$
\mu^{-1\,ij}_\text{eff} = \langle \mu^{-1\,ij}\rangle + \langle \mu^{-1\,ik}\,\partial_{y^k}\chi^j\rangle, \qquad \varepsilon^\text{eff}_{zz} = \langle \varepsilon_{zz}\rangle.
$$

**Transverse-electric (TE) polarization.** $\mathbf{H} = H_z(\mathbf{x})\hat{\mathbf{z}}$. By a parallel derivation (eliminating $\mathbf{E}$ instead of $\mathbf{B}$ from Maxwell's equations), the wave equation reduces to

$$
\partial_i\!\left[\varepsilon^{-1\,ij}(\mathbf{x}/a)\, \partial_j H_z\right] + \omega^{2}\, \mu_{zz}(\mathbf{x}/a)\, H_z = 0,
$$

with identification

$$
\boxed{\quad A^{ij}(\mathbf{y}) \;\longleftrightarrow\; \varepsilon^{-1\,ij}(\mathbf{y}), \qquad B(\mathbf{y}) \;\longleftrightarrow\; \mu_{zz}(\mathbf{y}). \quad}
$$

The TE-mode effective equation is

$$
\partial_{X^i}\!\left[\varepsilon^{-1\,ij}_\text{eff}\, \partial_{X^j} H_z\right] + \omega^{2}\,\mu^\text{eff}_{zz}\, H_z = 0,
$$

with

$$
\varepsilon^{-1\,ij}_\text{eff} = \langle \varepsilon^{-1\,ij}\rangle + \langle \varepsilon^{-1\,ik}\,\partial_{y^k}\chi_E^j\rangle, \qquad \mu^\text{eff}_{zz} = \langle \mu_{zz}\rangle,
$$

where $\chi_E^j$ is the cell corrector for the TE problem (solving $L_y^E[\chi_E^j] = -\partial_{y^i}\varepsilon^{-1\,ij}$ with cell operator $L_y^E[\phi] = \partial_{y^i}[\varepsilon^{-1\,ij}\partial_{y^j}\phi]$).

### 3.3 The two correctors

The TM and TE polarizations involve two *different* cell correctors:

- $\chi^j$ ("magnetic corrector"): solves $\partial_{y^i}[\mu^{-1\,ij}\partial_{y^j}\chi^k] = -\partial_{y^i}\mu^{-1\,ik}$.
- $\chi_E^j$ ("electric corrector"): solves $\partial_{y^i}[\varepsilon^{-1\,ij}\partial_{y^j}\chi_E^k] = -\partial_{y^i}\varepsilon^{-1\,ik}$.

Each corrector is determined by *its own* cell problem with the corresponding constitutive coefficient. In general, $\chi^j \neq \chi_E^j$.

### 3.4 Full vector Maxwell case

For three-dimensional substrates without translation symmetry, Maxwell's equations do not decouple into scalar polarizations. The full vector wave equation must be homogenized. The structural argument parallels the scalar case but involves vector-valued correctors:

$$
\boldsymbol\chi^k_\text{vec}(\mathbf{y}): \nabla_\mathbf{y}\times\!\left[\mu^{-1}(\mathbf{y})\, (\hat{\mathbf{e}}_k + \nabla_\mathbf{y}\times\boldsymbol\chi^k_\text{vec})\right] = 0,
$$

and the effective constitutive tensors take the form

$$
\boxed{\quad
\begin{aligned}
\mu^{-1\,ij}_\text{eff} &= \big\langle (\delta_l^i + (\nabla_\mathbf{y}\times\boldsymbol\chi^i_\text{vec})_l)\, \mu^{-1\,lm}\, (\delta_m^j + (\nabla_\mathbf{y}\times\boldsymbol\chi^j_\text{vec})_m)\big\rangle, \\[4pt]
\varepsilon_{\mathrm{eff}}^{ij} &= \big\langle (\delta_l^i + \partial_{y^l}\xi^i)\, \varepsilon^{lm}\, (\delta_m^j + \partial_{y^m}\xi^j)\big\rangle,
\end{aligned}
\quad}
$$

where $\xi^j$ is the (scalar) electric corrector for the $\mathbf{D}$-field homogenization.

The structural form is identical to the scalar case: cell-averaged coefficient + corrector-mediated correction. The full vector version is more elaborate to write out but does not introduce new substrate-level content.

For clarity, the remainder of this Memo focuses on the scalar (TM/TE) case, with the understanding that the vector generalization is structurally identical.

### 3.5 The user-specified identifications

The Arc specification calls for two parallel identifications:

- $A^{ij}(\mathbf{y}) \longleftrightarrow \varepsilon^{ij}(\mathbf{y})$ for the *electric response*.
- $A^{ij}(\mathbf{y}) \longleftrightarrow \mu^{-1\,ij}(\mathbf{y})$ for the *magnetic response*.

Each is a FORM-FORCED-INHERITED identification: the substrate's coarse-grained rule-type response, when the chain is an electromagnetic mode, decomposes into electric and magnetic response components, each of which has a separate cell problem.

The effective permittivity tensor is then

$$
\boxed{\quad
\varepsilon_{\mathrm{eff}}^{ij} \;=\; \langle \varepsilon^{ij}(\mathbf{y})\rangle + \langle \varepsilon^{ik}(\mathbf{y})\,\partial_{y^k}\chi^j(\mathbf{y})\rangle,
\quad}
$$

where $\chi^j$ is the cell corrector for the *electric* cell problem $\partial_{y^i}[\varepsilon^{ij}\partial_{y^j}\chi^k] = -\partial_{y^i}\varepsilon^{ik}$. The effective inverse-permeability tensor is

$$
\boxed{\quad
\mu_{\mathrm{eff}}^{-1\,ij} \;=\; \langle \mu^{-1\,ij}(\mathbf{y})\rangle + \langle \mu^{-1\,ik}(\mathbf{y})\,\partial_{y^k}\chi^j_M(\mathbf{y})\rangle,
\quad}
$$

where $\chi^j_M$ is the *magnetic* cell corrector solving $\partial_{y^i}[\mu^{-1\,ij}\partial_{y^j}\chi^k_M] = -\partial_{y^i}\mu^{-1\,ik}$.

These two effective tensors are independently derived from independent cell problems on the same unit cell, applied to two different microstructural fields. They become the macroscopic constitutive parameters of the homogenized medium.

---

## 4. Anisotropy from Microstructure

### 4.1 Tensor structure of the effective constitutive parameters

The effective tensors $\varepsilon_{\mathrm{eff}}^{ij}$ and $\mu_{\mathrm{eff}}^{-1\,ij}$ are generically *anisotropic* even if the local $\varepsilon^{ij}, \mu^{-1\,ij}$ are isotropic ($\propto \delta^{ij}$). The anisotropy arises from the *geometry* of the unit cell.

To see this, consider an isotropic two-phase substrate: $\varepsilon(\mathbf{y}) = \varepsilon_1$ in region $Y_1$ and $\varepsilon(\mathbf{y}) = \varepsilon_2$ in region $Y_2$ (both isotropic scalars). The local tensor $\varepsilon^{ij}(\mathbf{y}) = \varepsilon(\mathbf{y})\,\delta^{ij}$ is isotropic at every $\mathbf{y}$. But the cell-problem solution $\chi^j(\mathbf{y})$ depends on the *geometric arrangement* of $Y_1$ and $Y_2$ within the unit cell, and this geometry imprints directional structure on the effective tensor.

### 4.2 Cubic symmetry → isotropic effective tensor

If the unit cell has cubic symmetry (the full point group $O_h$ acts on $Y$), then the effective tensor must be invariant under all cubic symmetries. The only rank-2 tensor invariant under cubic symmetry is $\propto \delta^{ij}$:

$$
\text{Cubic unit cell} \;\Longrightarrow\; \varepsilon_{\mathrm{eff}}^{ij} = \varepsilon_{\mathrm{eff}}\,\delta^{ij}.
$$

The effective medium is isotropic.

### 4.3 Lower symmetries → anisotropic effective tensor

Sub-cubic unit cells produce anisotropic effective tensors. The most common case is a *layered (uniaxial)* unit cell, where one direction (say $\mathbf{e}_3$) is distinguished by the layer normal. The point group reduces to $D_{\infty h}$, and the effective tensor takes the uniaxial form

$$
\varepsilon_{\mathrm{eff}}^{ij} = \varepsilon_\parallel\,\delta^{ij}_\parallel + \varepsilon_\perp\,\delta^{ij}_\perp,
$$

where $\delta^{ij}_\parallel$ projects onto the layer direction and $\delta^{ij}_\perp$ projects onto the plane perpendicular to the layers.

### 4.4 Layered substrate: closed-form effective tensors

Consider a 1D layered substrate (translation invariance in $x, y$; layers stacked along $z$). The unit cell is $Y = [0, 1]$ in the $z$-direction, with layer $Y_1 = [0, f]$ (permittivity $\varepsilon_1$) and $Y_2 = [f, 1]$ (permittivity $\varepsilon_2$).

For propagation in the $z$-direction ($\partial_{X^z}$ gradient), the cell problem is the 1D problem worked out in Memo 3. The effective permittivity in the layer direction ($z$) is the *harmonic mean*:

$$
\varepsilon_\parallel = \varepsilon^\text{eff}_{zz} = \left[\frac{f}{\varepsilon_1} + \frac{1-f}{\varepsilon_2}\right]^{-1}.
$$

For propagation in the in-plane direction ($x$ or $y$), the corrector $\chi^x(\mathbf{y})$ vanishes (since $\varepsilon$ does not vary in $x$ or $y$). The effective permittivity in-plane is the *arithmetic mean*:

$$
\varepsilon_\perp = \varepsilon^\text{eff}_{xx} = \varepsilon^\text{eff}_{yy} = f\,\varepsilon_1 + (1-f)\,\varepsilon_2.
$$

The effective tensor is uniaxial with components

$$
\varepsilon_{\mathrm{eff}}^{ij} = \begin{pmatrix} \varepsilon_\perp & 0 & 0 \\ 0 & \varepsilon_\perp & 0 \\ 0 & 0 & \varepsilon_\parallel \end{pmatrix},
$$

with $\varepsilon_\parallel = \langle\varepsilon^{-1}\rangle^{-1}$ and $\varepsilon_\perp = \langle\varepsilon\rangle$. The harmonic mean is always less than or equal to the arithmetic mean, so $\varepsilon_\parallel \leq \varepsilon_\perp$, with equality only when $\varepsilon_1 = \varepsilon_2$.

### 4.5 Why anisotropy is FORCED at substrate level

The substrate's rule-type microstructure (P-MM-1) has a specific geometry within each unit cell. The chain probes this microstructure differently depending on the macroscopic gradient direction:

- Gradient *along layers*: the chain experiences the volume-averaged response (arithmetic mean).
- Gradient *across layers*: the chain experiences the harmonic-mean response, limited by the smaller-$\varepsilon$ layer.

The substrate-level mechanism: in the across-layer direction, the chain's pre-individuation amplitude must be continuous as it crosses each layer interface. Continuity across layers with different $\varepsilon$ values forces the amplitude to develop a specific spatial pattern (encoded by $\chi^z(\mathbf{y})$) that limits the effective response. In the along-layer direction, no such constraint applies; the chain experiences the layers in parallel, and the response is the unconstrained arithmetic average.

The anisotropy is therefore a substrate-level *direction-dependent rule-type response*, not a postulated material property. It is FORCED by the geometry of the rule-type microstructure within the unit cell.

---

## 5. Substrate-Level Interpretation

### 5.1 The effective permittivity tensor

$\varepsilon_{\mathrm{eff}}^{ij}$ is the substrate-level *coarse-grained electric rule-type response*. The chain's pre-individuation amplitude, at probe scale $\lambda \gg a$, couples to the substrate's electric field with a rule-type-coupling coefficient that is the cell-averaged $\varepsilon$ corrected by the cell-problem solution.

Decomposition:
- $\langle\varepsilon^{ij}\rangle$: the *bare arithmetic average* of the local electric response. This is what the chain would experience if the unit cell were a homogeneous mixture.
- $\langle\varepsilon^{ik}\partial_{y^k}\chi^j\rangle$: the *microstructure correction*. The chain's amplitude oscillates within each unit cell (pattern $\chi^j$) to accommodate the local rule-type variation; this oscillation reduces the effective response below the arithmetic mean.

Together they produce the macroscopic permittivity that the chain experiences at probe scale.

### 5.2 The effective permeability tensor

Analogous decomposition for $\mu_{\mathrm{eff}}^{-1\,ij}$. The substrate-level *coarse-grained magnetic rule-type response* is the cell-averaged $\mu^{-1}$ corrected by the magnetic cell-problem solution.

### 5.3 The chain's experienced medium

From the chain's vantage at probe scale $\lambda \gg a$:
- The substrate appears as a homogeneous medium with constant constitutive tensors $\varepsilon_{\mathrm{eff}}^{ij}$ and $\mu_{\mathrm{eff}}^{-1\,ij}$.
- The substrate's actual rule-type microstructure is invisible — the chain cannot resolve it.
- The chain's propagation is governed by the macroscopic wave equation derived in §2.3.

The microstructure influences the chain only through its *cell-averaged* response. All the rule-type variation within each unit cell is integrated over and absorbed into the two effective tensors.

### 5.4 What this enables

Once the substrate's rule-type microstructure is specified (P-MM-1 + P-MM-2), the cell problems can in principle be solved (analytically for simple geometries, numerically for general ones), and the effective $\varepsilon_{\mathrm{eff}}, \mu_{\mathrm{eff}}$ tensors are determined. The chain's macroscopic propagation is then fully predicted.

Conversely, by *engineering* the rule-type microstructure within the unit cell, one can produce desired effective constitutive tensors. This is the substrate-level basis of metamaterial engineering: choose a microstructure that yields the target $\varepsilon_{\mathrm{eff}}, \mu_{\mathrm{eff}}$ via the cell-problem machinery.

The specific case of negative effective constitutive parameters — and the conditions for $\varepsilon_{\mathrm{eff}} < 0, \mu_{\mathrm{eff}} < 0$ producing negative refraction — is the subject of Memo 6.

---

## 6. Mapping Back to the Original Substrate Equation

To verify consistency, the macroscopic effective equation should reduce to the original (free-space) wave equation in the trivial limit. With $\varepsilon^{ij}(\mathbf{y}) = \varepsilon_0\delta^{ij}$ and $\mu^{-1\,ij}(\mathbf{y}) = \mu_0^{-1}\delta^{ij}$ both constant:

- Cell problem $\partial_{y^i}[\mu^{-1}\delta^{ij}\partial_{y^j}\chi^k] = -\partial_{y^i}\mu^{-1}\delta^{ik} = 0$. The source vanishes; the cell-problem solution is $\chi^k = 0$.
- Effective tensors $\varepsilon_{\mathrm{eff}}^{ij} = \langle\varepsilon\rangle\delta^{ij} = \varepsilon_0\delta^{ij}$ and $\mu_{\mathrm{eff}}^{-1\,ij} = \mu_0^{-1}\delta^{ij}$.
- Macroscopic equation: $\nabla^2\psi_0 + \omega^2\varepsilon_0\mu_0\psi_0 = 0$, recovering the standard free-space wave equation with $c^2 = 1/\varepsilon_0\mu_0$ (in SI units).

This consistency check confirms that the homogenization machinery correctly recovers vacuum propagation in the trivial-microstructure limit.

---

## 7. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **Homogenized macroscopic wave equation** $\partial_{X^i}[A^{*ij}\partial_{X^j}\psi_0] + k_0^2 B^*\psi_0 = 0$ (§2.3). FORCED by the order-$a^0$ solvability condition + averaging operator properties + cell-problem decomposition $\psi_1 = \chi^j\partial_{X^j}\psi_0$.

- **Effective tensor structure** $A^{*ij} = \langle A^{ij}\rangle + \langle A^{ik}\partial_{y^k}\chi^j\rangle$ (§2.3). FORCED by the order-$a^0$ averaging.

- **Effective potential coefficient** $B^* = \langle B\rangle$ (§2.3). FORCED.

- **Symmetric/positive-definite form of $A^{*ij}$** (§2.4). FORCED by self-adjointness of $L_\mathbf{y}$ + positivity of $A^{ij}$.

- **Anisotropy from sub-cubic unit-cell symmetry** (§4). FORCED by group-theoretic invariance: rank-2 tensors invariant under a sub-cubic point group are not proportional to $\delta^{ij}$.

- **Layered-substrate closed forms** $\varepsilon_\parallel = \langle\varepsilon^{-1}\rangle^{-1}$ (harmonic mean) and $\varepsilon_\perp = \langle\varepsilon\rangle$ (arithmetic mean) (§4.4). FORCED.

- **Consistency with vacuum propagation in the trivial-microstructure limit** (§6). FORCED.

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Maxwell's equations** in a structured medium (§3.1). Standard EM; the substrate-level pre-image is inherited from coarse-graining of T17 gauge-field structure (treated as a given here).
- **Scalar reduction to TM and TE polarizations** (§3.2). Standard EM in 2D; re-derived inline.
- **Identification $A^{ij} \leftrightarrow \mu^{-1\,ij}$ (TM)** and **$A^{ij} \leftrightarrow \varepsilon^{ij}$ (TE / electric formulation)** (§3.2–3.5). FORM-FORCED-INHERITED from Maxwell's equations + standard scalar-reduction algebra.
- **Vector wave equation in 3D with vector correctors** (§3.4). Structurally identical to scalar case; the vector calculus is standard.
- **Group-theoretic constraint of cubic symmetry → isotropic tensor** (§4.2). Standard tensor representation theory.

### What remains OPEN

- **Closed-form effective tensors for 2D and 3D periodic microstructures.** The 1D layered case (§4.4) admits closed-form harmonic and arithmetic means; 2D and 3D require numerical solution of the cell problem in most cases. OPEN at closed-form level; FORM-FORCED at structural level.

- **Bianisotropic substrates** (microstructures with magnetoelectric coupling $\varepsilon, \mu$ → 4-tensor structure). Requires extension of the cell problem to include cross-coupling terms; structurally similar but algebraically more elaborate. OPEN.

- **Dispersion of the effective tensors** ($\varepsilon_{\mathrm{eff}}(\omega), \mu_{\mathrm{eff}}(\omega)$). When the local $\varepsilon, \mu$ depend on frequency (resonant microstructures), the effective tensors inherit this dependence. The leading-order homogenization here treats $\varepsilon, \mu$ as constant at fixed $\omega$; frequency-dependent extensions are derived by repeating the cell problem at each $\omega$. The structural form is FORM-FORCED at each $\omega$; the global $\omega$-dependence of $\varepsilon_{\mathrm{eff}}, \mu_{\mathrm{eff}}$ is OPEN for general microstructures.

- **Strong-contrast microstructures** (where $\varepsilon_1/\varepsilon_2$ or $\mu_1/\mu_2$ is very large or very small). The standard homogenization expansion may need modification (high-contrast homogenization). OPEN.

- **Random (non-periodic) microstructures.** Replaces unit-cell averaging with ensemble-averaging (stochastic homogenization). OPEN; structurally parallel to periodic case.

- **Non-local effective constitutive relations.** When $\lambda \sim a$ (Bragg regime), the local effective tensor description breaks down. Non-local kernels $\varepsilon_{\mathrm{eff}}^{ij}(\mathbf{X}, \mathbf{X}')$ are needed. OPEN; outside the homogenization regime.

- **Quantum metamaterials.** When individual-photon effects matter (e.g., single-photon transport in metamaterials), the classical effective-medium description is insufficient. Substrate-level account requires composition with Lindblad-type open-system machinery. OPEN.

---

## 8. Review and Recommended Next Steps

### Review

Memo 4 has delivered:

- **Order-$a^0$ solvability condition** (§2.2) applied to the order-$a^0$ wave equation, producing the homogenized macroscopic equation $\partial_{X^i}[A^{*ij}\partial_{X^j}\psi_0] + k_0^2 B^*\psi_0 = 0$ (§2.3).
- **Effective tensor** $A^{*ij} = \langle A^{ij}\rangle + \langle A^{ik}\partial_{y^k}\chi^j\rangle$ and **effective scalar** $B^* = \langle B\rangle$ (§2.3).
- **Electromagnetic identifications** $A^{ij} \leftrightarrow \mu^{-1\,ij}$ (TM) and $A^{ij} \leftrightarrow \varepsilon^{ij}$ (TE) (§3).
- **Effective permittivity tensor** $\varepsilon_{\mathrm{eff}}^{ij} = \langle\varepsilon^{ij}\rangle + \langle\varepsilon^{ik}\partial_{y^k}\chi^j\rangle$ (§3.5).
- **Effective inverse-permeability tensor** $\mu_{\mathrm{eff}}^{-1\,ij} = \langle\mu^{-1\,ij}\rangle + \langle\mu^{-1\,ik}\partial_{y^k}\chi^j_M\rangle$ with the magnetic corrector $\chi^j_M$ (§3.5).
- **Vector Maxwell case** with vector correctors $\boldsymbol\chi^k_\text{vec}$, structurally identical to scalar (§3.4).
- **Anisotropy from microstructure** — cubic symmetry → isotropic tensor; sub-cubic symmetry → anisotropic tensor (§4).
- **Layered-substrate closed forms** $\varepsilon_\parallel = \langle\varepsilon^{-1}\rangle^{-1}$ (harmonic mean) and $\varepsilon_\perp = \langle\varepsilon\rangle$ (arithmetic mean) (§4.4).
- **Substrate-level interpretation**: $\varepsilon_{\mathrm{eff}}, \mu_{\mathrm{eff}}$ as coarse-grained rule-type response coefficients (§5).
- **Trivial-limit consistency check** recovering free-space wave equation (§6).
- **Explicit FORCED / FORM-FORCED-INHERITED / OPEN labeling** (§7).

### Honest scope-limit

This Memo introduced no new substrate primitives beyond P-MM-1 through P-MM-6 (Memo 1's inventory). All derivations are done inline. No cross-references to other arcs.

### Recommended next steps

In order:

1. **Memo 5 — Substrate-Level Meaning of $\varepsilon$ and $\mu$.** Articulate the substrate-level reading of the effective constitutive parameters in terms of rule-type response. Connect $\varepsilon$ to the substrate's electric-polarization response (rule-type-coupling to the gauge field's electric component) and $\mu$ to the substrate's magnetic-polarization response. Show how T17-derived gauge-field structure, when applied to a structured substrate, produces the effective constitutive tensors as substrate-level rule-type responses.

2. **Memo 6 — Conditions for Negative Index (Pendry 2000).** With effective constitutive tensors in hand, derive the wire-array and split-ring-resonator microstructures and their effective $\varepsilon_{\mathrm{eff}} < 0$ and $\mu_{\mathrm{eff}} < 0$ responses. The wire array produces plasma-like electric response with negative $\varepsilon$ below a plasma frequency; the split-ring resonator produces resonant magnetic response with negative $\mu$ above a magnetic resonance. The two together in a frequency window produce negative refractive index $n_{\mathrm{eff}} = -\sqrt{|\varepsilon_{\mathrm{eff}}\mu_{\mathrm{eff}}|}$.

3. **Memos 7–11 — Transformation Optics.** Build on the homogenization machinery + the substrate-gradient-deformation primitive (P-MM-3) to derive how coordinate transformations on the effective medium correspond to substrate-level rule-type deformations. Cloaking emerges as a specific deformation that expels a region from the chain's accessible substrate.

4. **Memo 12 — Metasurface Boundary Conditions.** Independent line: derive the generalized Snell's law from substrate-level continuity conditions at rule-type discontinuities.

5. **Memo 13 — Synthesis.** Tie all three precursors together.

### Anchor for future memos

The effective constitutive tensors $\varepsilon_{\mathrm{eff}}^{ij}$ and $\mu_{\mathrm{eff}}^{-1\,ij}$, with the explicit decomposition into bare-average + corrector-correction, are now standardized for the remainder of the Arc. Memo 5 will articulate their substrate-level meaning; Memo 6 will derive the negative-index regime; Memos 7–11 will deform the effective medium under substrate-gradient transformations to produce cloaking.
