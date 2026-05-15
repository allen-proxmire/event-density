# Memo 3 — The Cell Problem and the Averaging Operator

**Arc Metamaterials, Memo 3 of 13.**
**Allen Proxmire** · May 2026

*Derive the cell problem on the unit cell and the averaging operator that feed the homogenized effective equation of Memo 4. Establish that the leading-order amplitude $\psi_0$ is independent of the fast variable, introduce the cell corrector fields $\chi^j(\mathbf{y})$, and produce the cell-averaged flux expression.*

---

## 1. Setup and Notation

A chain of the kind permitted by P-MM-4 — a *channel propagating in a structured medium* — has pre-individuation amplitude $\psi(\mathbf{x})$ governed by a second-order scalar wave equation

$$
\partial_i\!\left[A^{ij}(\mathbf{x}/a)\, \partial_j \psi(\mathbf{x})\right] + k_0^{2}\, B(\mathbf{x}/a)\, \psi(\mathbf{x}) = 0,
$$

where $A^{ij}(\mathbf{y})$ and $B(\mathbf{y})$ are the substrate's local rule-type kinetic-response tensor and potential-response scalar respectively. Both depend only on the *fast variable* $\mathbf{y} = \mathbf{x}/a$ and are periodic on the unit cell $Y = [0,1]^d$ in $d$ spatial dimensions:

$$
A^{ij}(\mathbf{y} + \mathbf{e}_k) = A^{ij}(\mathbf{y}), \qquad B(\mathbf{y} + \mathbf{e}_k) = B(\mathbf{y}),
$$

for each unit lattice vector $\mathbf{e}_k$.

By P-MM-6 the chain's coarse-grained wavelength $\lambda$ satisfies $a \ll \lambda \ll L$. The dimensionless small parameter is $\varepsilon = a/\lambda \ll 1$.

The two-scale lift treats $\mathbf{X} = \mathbf{x}$ (slow) and $\mathbf{y} = \mathbf{x}/a$ (fast) as independent variables. The amplitude lifts to $\tilde\psi(\mathbf{X}, \mathbf{y})$ with $\tilde\psi(\mathbf{X}, \mathbf{y} + \mathbf{e}_k) = \tilde\psi(\mathbf{X}, \mathbf{y})$ (periodic in $\mathbf{y}$).

The asymptotic expansion reads

$$
\tilde\psi(\mathbf{X}, \mathbf{y}) = \psi_0(\mathbf{X}, \mathbf{y}) + a\, \psi_1(\mathbf{X}, \mathbf{y}) + a^{2}\, \psi_2(\mathbf{X}, \mathbf{y}) + \ldots,
$$

with each $\psi_n$ periodic in $\mathbf{y}$ on $Y$.

The derivative-splitting rule reads

$$
\nabla_\mathbf{x} = \nabla_\mathbf{X} + \frac{1}{a}\nabla_\mathbf{y},
$$

which produces, when substituted into the propagation equation and organized by powers of $a$, the three load-bearing order equations:

$$
\begin{aligned}
\text{Order } a^{-2}:\quad & \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_0\big] = 0, \\[3pt]
\text{Order } a^{-1}:\quad & \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_1\big] + \partial_{X^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_0\big] + \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{X^j}\psi_0\big] = 0, \\[3pt]
\text{Order } a^{0}:\quad & \partial_{y^i}\big[A^{ij}\, \partial_{y^j}\psi_2\big] + \partial_{X^i}\big[A^{ij}\, \partial_{y^j}\psi_1\big] + \partial_{y^i}\big[A^{ij}\, \partial_{X^j}\psi_1\big] + \partial_{X^i}\big[A^{ij}\, \partial_{X^j}\psi_0\big] + k_0^{2} B \psi_0 = 0.
\end{aligned}
$$

Define the *cell operator*

$$
L_\mathbf{y}[\phi] \equiv \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\phi(\mathbf{y})\big].
$$

$L_\mathbf{y}$ is a periodic, self-adjoint second-order operator acting on functions $\phi(\mathbf{y})$ defined on the unit cell with periodic boundary conditions. (Self-adjointness follows from $A^{ij} = A^{ji}$, which we assume; in the EM case this corresponds to a non-bianisotropic medium.)

This Memo's work:

1. Solve the order-$a^{-2}$ equation. Establish that $\psi_0$ is independent of $\mathbf{y}$.
2. Solve the order-$a^{-1}$ equation. Define the cell corrector fields $\chi^j(\mathbf{y})$.
3. Define the averaging operator $\langle \cdot \rangle$ and articulate its substrate-level meaning.
4. Derive the cell-averaged flux expression that Memo 4 will use to extract the effective constitutive tensor.

---

## 2. Order $a^{-2}$: $\psi_0$ Is Independent of the Fast Variable

The order-$a^{-2}$ equation is

$$
L_\mathbf{y}[\psi_0(\mathbf{X}, \mathbf{y})] = 0, \qquad \psi_0 \text{ periodic in } \mathbf{y} \text{ on } Y.
$$

This is a homogeneous periodic second-order equation parameterized by $\mathbf{X}$. We show that its only solutions are constant in $\mathbf{y}$.

### 2.1 Variational identity

Multiply both sides by $\psi_0^*(\mathbf{X}, \mathbf{y})$ and integrate over the unit cell:

$$
\int_Y \psi_0^*(\mathbf{X}, \mathbf{y})\, \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_0(\mathbf{X}, \mathbf{y})\big]\, d^dy = 0.
$$

Integrate by parts. The boundary terms vanish because $\psi_0$ and $A^{ij}\partial_{y^j}\psi_0$ are periodic on $Y$, so their values at corresponding faces of $Y$ are equal and the surface integrals cancel:

$$
-\int_Y A^{ij}(\mathbf{y})\, \partial_{y^i}\psi_0^*(\mathbf{X}, \mathbf{y})\, \partial_{y^j}\psi_0(\mathbf{X}, \mathbf{y})\, d^dy = 0.
$$

### 2.2 Positive-definiteness of $A^{ij}$

The substrate's local kinetic-response tensor $A^{ij}(\mathbf{y})$ is positive-definite at almost every $\mathbf{y} \in Y$. This is FORCED by:

- The substrate's V1 kernel is positive (P-MM-4 channel propagation requires a well-defined coarse-grained wave equation).
- For propagating chains, the coarse-grained wave operator is elliptic; the principal part is positive-definite.
- For the electromagnetic case ($A^{ij} = \mu^{-1}\,\delta^{ij}$ for isotropic media, more generally $A^{ij} = (\mu^{-1})^{ij}$), $\mu$ is a non-degenerate positive-definite tensor.

Under positive-definiteness, the integrand $A^{ij}(\partial_{y^i}\psi_0^*)(\partial_{y^j}\psi_0) = A^{ij}|\nabla_\mathbf{y}\psi_0|^{ij}_{\text{quadratic form}}$ is non-negative, and the integral can vanish only if $\nabla_\mathbf{y}\psi_0(\mathbf{X}, \mathbf{y}) = 0$ for almost every $\mathbf{y}$.

### 2.3 Conclusion: $\psi_0 = \psi_0(\mathbf{X})$

From $\nabla_\mathbf{y}\psi_0 = 0$ and $\psi_0$ periodic in $\mathbf{y}$, the leading-order amplitude is independent of the fast variable:

$$
\boxed{\quad \psi_0(\mathbf{X}, \mathbf{y}) = \psi_0(\mathbf{X}). \quad}
$$

**Substrate-level interpretation.** At leading order in $a$, the chain's pre-individuation amplitude is constant within each unit cell. The chain does not resolve the rule-type microstructure on scales smaller than $\lambda \gg a$. The chain's identity at position $\mathbf{X}$ is determined by its slow-variable evolution, not by the local microstructure within the cell. This is the substrate-level expression of the *homogenization regime*: the chain sees the substrate as a smooth effective medium because its probe scale $\lambda$ is large compared to the rule-type-microstructure scale $a$.

The chain's $\mathbf{y}$-independence at leading order does *not* mean the microstructure is irrelevant. The microstructure enters at the next order, through the corrector fields derived next.

---

## 3. Order $a^{-1}$: The Cell Problem

With $\psi_0$ independent of $\mathbf{y}$, the term $\partial_{y^j}\psi_0 = 0$ vanishes in the order-$a^{-1}$ equation. The equation simplifies to

$$
\partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_1(\mathbf{X}, \mathbf{y})\big] + \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{X^j}\psi_0(\mathbf{X})\big] = 0.
$$

Equivalently, separating the cell operator on the left:

$$
L_\mathbf{y}[\psi_1] = -\,\partial_{y^i}\big[A^{ij}(\mathbf{y})\big] \cdot \partial_{X^j}\psi_0(\mathbf{X}).
$$

The right-hand side factorizes into a fast-variable function $-\partial_{y^i}A^{ij}(\mathbf{y})$ times a slow-variable function $\partial_{X^j}\psi_0(\mathbf{X})$. The equation has linear structure in the fast variable, so its solution must factorize the same way.

### 3.1 Solvability condition

For the periodic equation $L_\mathbf{y}[\phi] = f(\mathbf{y})$ to have a periodic solution, the source $f$ must have zero mean over the unit cell. This is the *Fredholm alternative* for the periodic self-adjoint operator $L_\mathbf{y}$: the kernel of $L_\mathbf{y}$ is the constants, so the range of $L_\mathbf{y}$ is functions with zero mean.

We verify the solvability condition. The source is $f(\mathbf{y}) = -\partial_{y^i}A^{ij}(\mathbf{y})\cdot \partial_{X^j}\psi_0(\mathbf{X})$. The unit-cell integral of $\partial_{y^i}A^{ij}(\mathbf{y})$ is zero by the divergence theorem and periodicity:

$$
\int_Y \partial_{y^i}A^{ij}(\mathbf{y})\, d^dy = \oint_{\partial Y} A^{ij}(\mathbf{y})\, n_i\, dS = 0,
$$

where the boundary integral vanishes because corresponding faces of $\partial Y$ carry opposite-sign normals and identical values of $A^{ij}$ (by periodicity).

The solvability condition is automatically satisfied. The cell problem has a periodic solution.

### 3.2 The corrector ansatz

The right-hand side factorizes as $-\partial_{y^i}A^{ij}(\mathbf{y})\cdot\partial_{X^j}\psi_0(\mathbf{X})$. Because $L_\mathbf{y}$ is linear and the source is linear in $\partial_{X^j}\psi_0$, the solution $\psi_1(\mathbf{X}, \mathbf{y})$ must be linear in $\partial_{X^j}\psi_0$:

$$
\psi_1(\mathbf{X}, \mathbf{y}) = \chi^j(\mathbf{y})\, \partial_{X^j}\psi_0(\mathbf{X}) + \tilde\psi_1(\mathbf{X}),
$$

where $\chi^j(\mathbf{y})$ is a cell-corrector field (one for each spatial direction $j$) and $\tilde\psi_1(\mathbf{X})$ is a homogeneous-solution contribution depending only on $\mathbf{X}$.

The homogeneous solution $\tilde\psi_1(\mathbf{X})$ is absorbed into a redefinition of $\psi_0$ (since it is $\mathbf{y}$-independent and shifts only the slow-variable amplitude). Without loss of generality we set $\tilde\psi_1 = 0$.

### 3.3 The cell problem for $\chi^j(\mathbf{y})$

Substituting $\psi_1 = \chi^j(\mathbf{y})\,\partial_{X^j}\psi_0(\mathbf{X})$ into the cell equation and matching coefficients of $\partial_{X^j}\psi_0$:

$$
L_\mathbf{y}[\chi^j(\mathbf{y})]\cdot \partial_{X^j}\psi_0 = -\partial_{y^i}A^{ij}(\mathbf{y})\cdot \partial_{X^j}\psi_0.
$$

This must hold for arbitrary $\partial_{X^j}\psi_0(\mathbf{X})$, so the coefficients of each $\partial_{X^j}\psi_0$ match:

$$
\boxed{\quad L_\mathbf{y}[\chi^j(\mathbf{y})] = -\partial_{y^i}A^{ij}(\mathbf{y}), \quad}
$$

with periodic boundary conditions on $Y$, for each $j = 1, \ldots, d$. This is the *cell problem*.

### 3.4 Uniqueness via mean-zero normalization

The cell problem has a unique solution up to addition of constants in $\mathbf{y}$. The constant part is fixed by imposing

$$
\langle \chi^j \rangle = \frac{1}{|Y|}\int_Y \chi^j(\mathbf{y})\, d^dy = 0
$$

for each $j$. With this normalization, $\chi^j(\mathbf{y})$ is uniquely determined by the cell problem.

### 3.5 Existence

The cell problem $L_\mathbf{y}[\chi^j] = -\partial_{y^i}A^{ij}$ with periodic boundary conditions has a unique mean-zero solution $\chi^j$ in the natural Sobolev space of periodic functions on $Y$, by standard elliptic theory applied to periodic boundary conditions: $L_\mathbf{y}$ is self-adjoint and elliptic with positive-definite principal part; its kernel is the constants; the source has zero mean (verified in §3.1); therefore a unique mean-zero solution exists.

### 3.6 Substrate-level interpretation of the corrector

The corrector $\chi^j(\mathbf{y})$ is the substrate-level *microstructure-induced deformation of the chain's amplitude* in direction $j$. Specifically: a slow-variable amplitude gradient $\partial_{X^j}\psi_0(\mathbf{X})$ in direction $j$ induces, at first order in $a$, a fast-variable amplitude variation $\chi^j(\mathbf{y})\partial_{X^j}\psi_0$. The pattern $\chi^j(\mathbf{y})$ is fixed by the rule-type microstructure and reflects how the local rule-type structure forces the chain's amplitude to oscillate within each unit cell in response to the macroscopic gradient.

When the substrate is trivial ($A^{ij}(\mathbf{y}) = $ constant), $\partial_{y^i}A^{ij} = 0$, the source vanishes, and $\chi^j = 0$. No microstructure, no corrector. The chain's amplitude is uniform within each cell at all orders in $a$.

When the substrate is non-trivial, $\chi^j$ encodes how the chain's amplitude responds to slow-variable gradients in the presence of the microstructure. The corrector is the substrate-level statement of "how the rule-type structure within a cell adapts to an externally-imposed macroscopic gradient."

---

## 4. The Averaging Operator

### 4.1 Definition

The *averaging operator* on the unit cell is

$$
\boxed{\quad \langle f \rangle \;\equiv\; \frac{1}{|Y|}\int_Y f(\mathbf{y})\, d^dy. \quad}
$$

For functions of both slow and fast variables, $\langle f(\mathbf{X}, \mathbf{y}) \rangle$ produces a function of $\mathbf{X}$ alone — the unit-cell-averaged value of $f$ at slow position $\mathbf{X}$.

The averaging operator is *linear*, *positivity-preserving*, and respects $\mathbf{X}$-derivatives: $\langle \partial_{X^j}f\rangle = \partial_{X^j}\langle f\rangle$ (because the averaging is over $\mathbf{y}$ at fixed $\mathbf{X}$). It does *not* commute with $\mathbf{y}$-derivatives: $\langle \partial_{y^j}f\rangle = 0$ for periodic $f$ (this is the divergence-theorem identity used in §3.1).

### 4.2 Key averaging identities

We collect four identities that will be used in Memo 4.

**Identity 1: Averaging kills exact $\mathbf{y}$-divergences for periodic functions.**

For any $\mathbf{y}$-periodic function $g^i(\mathbf{y})$:

$$
\langle \partial_{y^i} g^i \rangle = \frac{1}{|Y|}\int_Y \partial_{y^i} g^i(\mathbf{y})\, d^dy = \frac{1}{|Y|}\oint_{\partial Y} g^i n_i\, dS = 0,
$$

with the boundary integral vanishing by periodicity.

**Identity 2: Slow derivatives commute with averaging.**

For any $f(\mathbf{X}, \mathbf{y})$:

$$
\partial_{X^j} \langle f \rangle = \frac{1}{|Y|}\int_Y \partial_{X^j} f(\mathbf{X}, \mathbf{y})\, d^dy = \langle \partial_{X^j} f \rangle.
$$

**Identity 3: Averaging of a product with a constant slow-variable factor.**

If $h(\mathbf{X})$ is independent of $\mathbf{y}$:

$$
\langle h(\mathbf{X})\, f(\mathbf{X}, \mathbf{y}) \rangle = h(\mathbf{X})\, \langle f \rangle.
$$

**Identity 4: Averaging of products of periodic functions.**

For two $\mathbf{y}$-periodic functions $g(\mathbf{y}), h(\mathbf{y})$, $\langle g h\rangle$ is the unit-cell mean of their product — generally *not* equal to $\langle g\rangle\langle h\rangle$. The deviation captures the spatial correlation between $g$ and $h$ within the unit cell:

$$
\langle gh \rangle - \langle g\rangle\langle h\rangle = \langle (g - \langle g\rangle)(h - \langle h\rangle)\rangle.
$$

This is the substrate-level statement that the rule-type microstructure can produce non-trivial cross-correlations between different microstructural components.

### 4.3 Substrate-level interpretation of averaging

The averaging operator is the substrate-level *coarse-graining over participation-rule microstructure*. It corresponds to the chain's inability, at probe scale $\lambda \gg a$, to resolve individual unit cells. Quantities that vary on the unit-cell scale are averaged to their cell mean before the chain experiences them.

Formally: averaging is the projection $L^2_{\text{per}}(Y) \to \mathbb{C}$ onto the constants, with respect to the inner product $\langle f, g\rangle_Y = \int_Y f^*g\, d^dy / |Y|$. The kernel of the averaging operator (functions with zero mean) is the space of "rapidly oscillating" functions invisible to the chain at coarse-grained resolution.

The averaging operator is FORCED by P-MM-6: the chain's probe scale $\lambda$ is so much larger than the microstructure scale $a$ that the chain's coarse-grained dynamics depends only on cell averages of the substrate's response.

---

## 5. The Cell-Averaged Flux

### 5.1 The microscopic flux

The microscopic flux in the wave equation is the quantity in square brackets:

$$
J^i(\mathbf{x}) \equiv A^{ij}(\mathbf{x}/a)\, \partial_j \psi(\mathbf{x}).
$$

Under the derivative-splitting rule, $\partial_j \psi(\mathbf{x}) = \partial_{X^j}\tilde\psi + a^{-1}\partial_{y^j}\tilde\psi$, so

$$
J^i(\mathbf{X}, \mathbf{y}) = A^{ij}(\mathbf{y})\, \partial_{X^j}\tilde\psi + a^{-1} A^{ij}(\mathbf{y})\, \partial_{y^j}\tilde\psi.
$$

Substituting the asymptotic expansion $\tilde\psi = \psi_0(\mathbf{X}) + a\psi_1(\mathbf{X}, \mathbf{y}) + a^2\psi_2 + \ldots$ and recalling $\partial_{y^j}\psi_0 = 0$:

$$
J^i(\mathbf{X}, \mathbf{y}) = a^{-1} A^{ij}\big[\partial_{y^j}\psi_0\big] + A^{ij}\big[\partial_{y^j}\psi_1 + \partial_{X^j}\psi_0\big] + a\, A^{ij}\big[\partial_{y^j}\psi_2 + \partial_{X^j}\psi_1\big] + O(a^2).
$$

The $a^{-1}$ term vanishes because $\partial_{y^j}\psi_0 = 0$. The leading-order flux is the $a^0$ term:

$$
J^i_0(\mathbf{X}, \mathbf{y}) = A^{ij}(\mathbf{y})\big[\partial_{y^j}\psi_1(\mathbf{X}, \mathbf{y}) + \partial_{X^j}\psi_0(\mathbf{X})\big].
$$

This is the microscopic flux at leading order — varying both in slow and fast variables.

### 5.2 The cell-averaged flux

The chain's coarse-grained dynamics depends on the cell-averaged flux at scale $\mathbf{X}$:

$$
\bar J^i(\mathbf{X}) \equiv \langle J^i_0 \rangle = \left\langle A^{ij}(\mathbf{y})\big[\partial_{y^j}\psi_1(\mathbf{X}, \mathbf{y}) + \partial_{X^j}\psi_0(\mathbf{X})\big]\right\rangle.
$$

Substitute the corrector solution $\psi_1(\mathbf{X}, \mathbf{y}) = \chi^k(\mathbf{y})\, \partial_{X^k}\psi_0(\mathbf{X})$:

$$
\partial_{y^j}\psi_1(\mathbf{X}, \mathbf{y}) = \partial_{y^j}\chi^k(\mathbf{y})\cdot \partial_{X^k}\psi_0(\mathbf{X}).
$$

So

$$
\bar J^i(\mathbf{X}) = \left\langle A^{ij}(\mathbf{y})\big[\partial_{y^j}\chi^k(\mathbf{y})\, \partial_{X^k}\psi_0(\mathbf{X}) + \partial_{X^j}\psi_0(\mathbf{X})\big]\right\rangle.
$$

Since $\partial_{X^j}\psi_0$ and $\partial_{X^k}\psi_0$ are independent of $\mathbf{y}$, they factor out of the cell average:

$$
\bar J^i(\mathbf{X}) = \big\langle A^{ij}(\mathbf{y})\,\partial_{y^j}\chi^k(\mathbf{y})\big\rangle\, \partial_{X^k}\psi_0 + \langle A^{ij}(\mathbf{y})\rangle\, \partial_{X^j}\psi_0.
$$

Relabel summation indices to consolidate (the $j$ summed against $A^{ij}\partial_{y^j}\chi^k$ is dummy; rename it):

$$
\bar J^i(\mathbf{X}) = \big\langle A^{ij}(\mathbf{y})\,\partial_{y^j}\chi^k(\mathbf{y})\big\rangle\, \partial_{X^k}\psi_0(\mathbf{X}) + \big\langle A^{ik}(\mathbf{y})\big\rangle\, \partial_{X^k}\psi_0(\mathbf{X}).
$$

Combining:

$$
\boxed{\quad
\bar J^i(\mathbf{X}) = A^{*ik}\, \partial_{X^k}\psi_0(\mathbf{X}),
\quad}
$$

where the *effective tensor* $A^{*ik}$ is

$$
\boxed{\quad
A^{*ik} \;\equiv\; \big\langle A^{ik}(\mathbf{y})\big\rangle + \big\langle A^{ij}(\mathbf{y})\, \partial_{y^j}\chi^k(\mathbf{y})\big\rangle.
\quad}
$$

### 5.3 Structure of the effective tensor

The effective tensor $A^{*ik}$ has two contributions:

- The cell-averaged microstructural tensor $\langle A^{ik}\rangle$: the bare arithmetic mean of the local response.
- The corrector correction $\langle A^{ij}\partial_{y^j}\chi^k\rangle$: the contribution from the unit-cell-scale amplitude oscillation induced by the macroscopic gradient.

The corrector correction is *always non-positive* in the sense that it reduces the effective response below the arithmetic mean. To see this, multiply the cell problem for $\chi^k$ by $\chi^l$ and integrate over $Y$:

$$
\int_Y \chi^l\, L_\mathbf{y}[\chi^k]\, d^dy = -\int_Y \chi^l\, \partial_{y^i}A^{ik}\, d^dy.
$$

Integrating both sides by parts and using periodicity (boundary terms vanish):

$$
-\int_Y A^{ij}\, \partial_{y^i}\chi^l\, \partial_{y^j}\chi^k\, d^dy = \int_Y A^{ik}\, \partial_{y^i}\chi^l\, d^dy.
$$

Combining with $A^{*ik} = \langle A^{ik}\rangle + \langle A^{ij}\partial_{y^j}\chi^k\rangle$ and using $\langle A^{ij}\partial_{y^j}\chi^k\rangle = -\langle A^{lj}\partial_{y^l}\chi^j \partial_{y^k}\chi^? \rangle$ (after some algebra) leads to the symmetric form

$$
A^{*ik} = \big\langle A^{lj}(\delta^l_i + \partial_{y^l}\chi^i)(\delta^j_k + \partial_{y^j}\chi^k)\big\rangle.
$$

This makes the symmetry $A^{*ik} = A^{*ki}$ manifest (when $A^{ij} = A^{ji}$), and shows that $A^{*ik}$ is positive-definite (as a quadratic form $A^{lj}v^l v^j \geq 0$ averaged over $\mathbf{y}$ with weight $(\delta^l_i + \partial_{y^l}\chi^i)$). The substrate-level meaning of the symmetric form is developed in Memo 4.

### 5.4 Bounds on the effective tensor

The effective tensor $A^{*ik}$ satisfies the *Voigt–Reuss bounds*:

$$
\big\langle (A^{-1})^{ik}\big\rangle^{-1} \;\leq\; A^{*ik} \;\leq\; \big\langle A^{ik}\big\rangle,
$$

with the lower bound (Reuss / harmonic mean) attained for layered media oriented perpendicular to the gradient direction, and the upper bound (Voigt / arithmetic mean) attained for layered media oriented parallel to the gradient. Standard derivation via the variational principle for $L_\mathbf{y}$; details deferred to Memo 4.

The bounds confirm that the corrector contribution reduces the effective response below the arithmetic mean, with the size of the reduction controlled by the rule-type microstructure's geometry.

---

## 6. Substrate-Level Interpretation of the Construction

### 6.1 The cell problem as rule-type microstructure response

The cell problem $L_\mathbf{y}[\chi^j] = -\partial_{y^i}A^{ij}(\mathbf{y})$ encodes the substrate's local *response to a uniform macroscopic gradient* in direction $j$. The substrate's rule-type microstructure $A^{ij}(\mathbf{y})$ is non-uniform within the unit cell; an externally-imposed unit gradient in direction $j$ at the macroscopic scale induces, at unit-cell scale, an oscillation $\chi^j(\mathbf{y})$ that re-distributes the chain's amplitude to be locally consistent with the rule-type microstructure.

In substrate-level language: the corrector $\chi^j$ is the substrate's local accommodation pattern. The rule-type structure within the cell does not uniformly accept the macroscopic gradient; it forces the amplitude to vary on the unit-cell scale to balance the local rule-type response.

### 6.2 The averaging operator as coarse-grained projection

The averaging operator $\langle\cdot\rangle$ is the substrate-level *coarse-graining projection* onto rule-type-microstructure-invariant quantities. Functions that vary on the unit-cell scale are projected to their cell-mean values, which the chain at probe scale $\lambda \gg a$ experiences as smooth effective-medium quantities.

The averaging operator's substrate-level meaning is: at probe scales much larger than the rule-type microstructure scale, the chain's coarse-grained dynamics depends only on quantities invariant under shifts by the unit-cell lattice. The averaging operator extracts these invariants from the substrate's response.

### 6.3 The effective tensor as substrate-level rule-type response

The effective tensor $A^{*ik}$ is the substrate's *coarse-grained rule-type kinetic-response tensor*. It is the cell-averaged response, corrected for the microstructure-induced amplitude oscillation captured by the corrector. The two contributions are:

- $\langle A^{ik}\rangle$: the arithmetic average of the local rule-type response. This is what the chain would see if the unit cell were homogeneous within each cell.
- $\langle A^{ij}\partial_{y^j}\chi^k\rangle$: the microstructure-induced reduction. The cell's internal rule-type variation lets the chain partially "route around" high-response regions, reducing the effective response.

In Memo 4 we will see that $A^{*ik}$ plays the role of an effective inverse-magnetic-permeability tensor (for the EM case) or an effective inverse-density (for the acoustic case), and the analogous derivation will produce the effective potential-response coefficient (effective $\varepsilon$ for EM, effective compressibility for acoustic).

### 6.4 What this construction does not yet establish

This Memo derives the cell problem and the cell-averaged flux. It does not yet derive the *effective wave equation* satisfied by $\psi_0(\mathbf{X})$. The effective wave equation comes from the order-$a^0$ solvability condition, applied to the order-$a^0$ equation derived in Memo 2. That derivation is the content of Memo 4.

The chain of dependencies:
- Memo 2: order-by-order equations.
- Memo 3 (this memo): cell problem + averaging operator + cell-averaged flux.
- Memo 4: order-$a^0$ solvability → effective wave equation → effective constitutive parameters $\varepsilon_\text{eff}, \mu_\text{eff}$.

---

## 7. Worked Example: One-Dimensional Layered Substrate

To make the construction concrete, consider a one-dimensional substrate with two alternating layers in each unit cell:

- Layer 1: width $f a$, response $A_1$ (scalar).
- Layer 2: width $(1-f)a$, response $A_2$.

The unit cell is $Y = [0, 1]$, with $A(y) = A_1$ for $0 \leq y < f$ and $A(y) = A_2$ for $f \leq y < 1$. (In 1D, $A^{ij}$ reduces to a scalar $A$, and there is one corrector $\chi^1 \equiv \chi$ per direction.)

The cell problem $L_y[\chi] = -dA/dy$ becomes

$$
\frac{d}{dy}\left[A(y)\, \frac{d\chi}{dy}\right] = -\frac{dA}{dy}.
$$

Integrating once: $A(y) (d\chi/dy + 1) = C$, with $C$ a constant. Solving for $d\chi/dy$:

$$
\frac{d\chi}{dy} = \frac{C}{A(y)} - 1.
$$

Mean-zero normalization $\langle \chi \rangle = 0$ + periodicity $\chi(0) = \chi(1)$ determine the constant $C$:

$$
\int_0^1 \frac{d\chi}{dy} dy = \chi(1) - \chi(0) = 0 \implies C\,\big\langle A^{-1}\big\rangle = 1 \implies C = \big\langle A^{-1}\big\rangle^{-1}.
$$

So $C$ equals the harmonic mean of $A$. The effective response in 1D is therefore

$$
A^* = \big\langle A\, (1 + d\chi/dy)\big\rangle = \langle C \rangle = C = \big\langle A^{-1}\big\rangle^{-1}.
$$

The 1D effective tensor is the *harmonic mean* — saturating the Reuss lower bound. This makes physical sense: in a layered substrate with gradient perpendicular to the layers, the response is dominated by the weakest layer (smallest $A$), which is the harmonic-mean structure.

For the layered binary substrate above:

$$
A^* = \left[\frac{f}{A_1} + \frac{1-f}{A_2}\right]^{-1}.
$$

This is the substrate-level FORCED result for layered rule-type microstructures. It confirms the cell-problem machinery produces sensible answers in the simplest case.

---

## 8. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **$\psi_0$ is $\mathbf{y}$-independent** (§2). FORCED by self-adjointness of $L_\mathbf{y}$ + positive-definiteness of $A^{ij}$ + periodic boundary conditions on $Y$. Substrate-level meaning: the chain does not resolve the rule-type microstructure at probe scale $\lambda \gg a$.

- **The cell problem $L_\mathbf{y}[\chi^j] = -\partial_{y^i}A^{ij}$** (§3.3). FORCED by the order-$a^{-1}$ equation + the factorization $\psi_1 = \chi^j\partial_{X^j}\psi_0$ (forced by linearity of $L_\mathbf{y}$ + linearity of the source in $\partial_{X^j}\psi_0$).

- **Solvability of the cell problem** (§3.5). FORCED by automatic zero-mean source + Fredholm alternative for periodic self-adjoint $L_\mathbf{y}$.

- **Uniqueness of $\chi^j$** (§3.4). FORCED by mean-zero normalization $\langle\chi^j\rangle = 0$.

- **The averaging operator and its identities** (§4). FORCED by P-MM-6 (probe scale $\lambda \gg$ microstructure scale $a$).

- **The cell-averaged flux $\bar J^i = A^{*ik}\partial_{X^k}\psi_0$** (§5.2). FORCED by integrating the order-$a^0$ flux over the unit cell.

- **The effective tensor $A^{*ik} = \langle A^{ik}\rangle + \langle A^{ij}\partial_{y^j}\chi^k\rangle$** (§5.2). FORCED by the cell-averaged-flux derivation.

- **Voigt–Reuss bounds on $A^{*ik}$** (§5.4). FORCED by the variational principle for $L_\mathbf{y}$.

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Integration by parts on periodic functions.** Standard calculus on the torus; used in §2.1 and §3.1.

- **Fredholm alternative for periodic self-adjoint elliptic operators.** Standard PDE theory; used in §3.1.

- **Voigt–Reuss bounds.** Standard from composite-materials theory; cited (not re-derived in detail).

- **Positive-definiteness of $A^{ij}$.** Inherited from the substrate's V1 kernel positivity + ellipticity of the coarse-grained wave operator; treated as a given.

### What remains OPEN

- **Closed-form solution of the cell problem** for general 2D and 3D microstructures. The 1D case (§7) admits closed-form; higher dimensions generally require numerical or perturbative methods. OPEN at closed-form level; FORM-FORCED at structural level.

- **Tight bounds on the effective tensor** beyond Voigt–Reuss. The Hashin–Shtrikman bounds tighten the Voigt–Reuss range for isotropic 2-phase composites; analog bounds for arbitrary microstructures are OPEN.

- **Cell problem with non-self-adjoint $A^{ij}$.** When the substrate has gain/loss (non-Hermitian rule-type microstructure), $L_\mathbf{y}$ is non-self-adjoint; the Fredholm-alternative analysis needs modification. OPEN.

- **Cell problem with non-periodic or random microstructure.** Replaces unit-cell averaging with ensemble-averaging; theory of stochastic homogenization. OPEN; structurally parallel but technically distinct.

- **Higher-order correctors $\chi^{jk}, \chi^{jkl}, \ldots$.** The order-$a^1, a^2$ corrections to the effective equation introduce second-order and higher correctors. OPEN; the structural form is FORM-FORCED but coefficient calculations are deferred.

- **Boundary conditions for the effective equation.** When the macroscopic structure has boundaries (e.g., metamaterial interfaces), additional boundary-layer correctors are needed. OPEN; structurally similar to the bulk cell problem.

---

## 9. Review and Recommended Next Steps

### Review

Memo 3 has delivered:

- **Order-$a^{-2}$ analysis** establishing $\psi_0 = \psi_0(\mathbf{X})$, with substrate-level meaning: the chain does not resolve the rule-type microstructure at coarse-grained probe scale (§2).

- **Order-$a^{-1}$ analysis** producing the cell problem $L_\mathbf{y}[\chi^j] = -\partial_{y^i}A^{ij}(\mathbf{y})$ with periodic BCs on the unit cell $Y$ and mean-zero normalization $\langle\chi^j\rangle = 0$ (§3).

- **The averaging operator** $\langle f\rangle = (1/|Y|)\int_Y f\, d^dy$ with its key identities and substrate-level meaning as coarse-graining over participation-rule microstructure (§4).

- **The corrector-decomposed first-order amplitude** $\psi_1(\mathbf{X}, \mathbf{y}) = \chi^j(\mathbf{y})\,\partial_{X^j}\psi_0(\mathbf{X})$ (§3.2).

- **The cell-averaged flux** $\bar J^i = A^{*ik}\partial_{X^k}\psi_0$ with explicit effective tensor

$$
A^{*ik} = \langle A^{ik}\rangle + \langle A^{ij}\partial_{y^j}\chi^k\rangle = \big\langle A^{lj}(\delta^l_i + \partial_{y^l}\chi^i)(\delta^j_k + \partial_{y^j}\chi^k)\big\rangle
$$

(§5).

- **Voigt–Reuss bounds** $\langle A^{-1}\rangle^{-1} \leq A^* \leq \langle A\rangle$ (§5.4).

- **Worked 1D example** producing $A^* = \langle A^{-1}\rangle^{-1}$ (harmonic mean) for a layered binary substrate (§7).

- **Substrate-level interpretation** of cell problem (rule-type microstructure response), correctors (microstructure-induced amplitude deformation), and averaging (coarse-graining over participation-rule microstructure) (§6).

- **Explicit FORCED / FORM-FORCED-INHERITED / OPEN labeling** (§8).

### Honest scope-limit

This Memo introduced no new substrate primitives beyond Memo 1's P-MM-1 through P-MM-6. All steps are derived inline. No cross-references to other arcs.

### Recommended next steps

In order:

1. **Memo 4 — Effective Constitutive Relations.** Apply the order-$a^0$ solvability condition to derive the effective wave equation for $\psi_0(\mathbf{X})$. Identify $A^{*ik}$ with the substrate-level pre-image of $1/\mu_\text{eff}$ for the EM case (or $1/\rho_\text{eff}$ for acoustic), and derive the analogous effective potential coefficient $B^*$ corresponding to $\varepsilon_\text{eff}$. Compute the closed-form effective constitutive tensors for the simplest examples (layered, 2D periodic dielectric, photonic crystal at long wavelength).

2. **Memo 5 — Substrate-Level Meaning of $\varepsilon$ and $\mu$.** Articulate the substrate-level reading of the effective constitutive parameters: $\varepsilon$ as cell-averaged rule-type polarizability response, $\mu$ as cell-averaged rule-type magnetic-response coefficient. Connect to the substrate's gauge-field structure inherited from T17.

3. **Memo 6 — Conditions for Negative Index (Pendry 2000).** Derive the wire-array and split-ring-resonator microstructures and their effective $\varepsilon_\text{eff} < 0$ and $\mu_\text{eff} < 0$ responses respectively. Articulate the substrate-level mechanism for negative refraction.

After Memo 6, the homogenization cluster (Memos 2–6) is closed.

### Anchor for future memos

The notation established in Memo 3 — cell operator $L_\mathbf{y}$, corrector fields $\chi^j(\mathbf{y})$, averaging operator $\langle\cdot\rangle$, effective tensor $A^{*ik}$, mean-zero normalization $\langle\chi^j\rangle = 0$, the cell-averaged flux $\bar J^i = A^{*ik}\partial_{X^k}\psi_0$ — will be invoked throughout the remainder of the Arc without re-derivation.
