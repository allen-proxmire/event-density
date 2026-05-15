# Memo 2 — Multi-Scale Expansion in Periodic Rule-Type Substrates

**Arc Metamaterials, Memo 2 of 13.**
**Allen Proxmire** · May 2026

*Derive the two-scale expansion machinery for channel propagation in a periodic rule-type substrate. Introduce fast and slow variables, derive the derivative-splitting rule, and produce the order-by-order equations that feed the cell problem of Memo 3.*

---

## 1. Setup

A chain of the kind that will be used throughout this Arc — a *light-like ED-channel*, in the sense of P-MM-4 — propagates through a substrate whose rule-type identity $\tau(\mathbf{x})$ varies periodically in space with unit-cell spacing $a$ (P-MM-1 + P-MM-2). The chain's coarse-grained wavelength $\lambda$ is much larger than $a$ (P-MM-6: $\ell_P \ll a \ll \lambda \ll L$).

This Memo derives the *multi-scale (two-scale) expansion* of the chain's propagation equation in this substrate. The expansion is the foundational machinery on which Memos 3–6 (homogenization) and 7–11 (transformation optics) build. The two-scale machinery is standard asymptotic analysis; the substrate-level reading of "fast" and "slow" variation is the content this Memo adds.

### 1.1 The chain's pre-individuation amplitude

The chain's pre-individuation amplitude is a complex-valued scalar $\psi(\mathbf{x})$ in the simplest setting (or a vector / tensor for polarized propagation; the structural argument is identical). The amplitude is the substrate-level pre-image of the coarse-grained wavefunction. Its evolution is governed by a second-order differential operator whose coefficients depend on the local rule-type identity $\tau(\mathbf{x})$.

### 1.2 The generic propagation equation

A chain in vacuum satisfies a free-photon equation $(\nabla^2 + k_0^2)\psi = 0$, where $k_0 = \omega/c$ is the free-space wavenumber. In a structured substrate, the coefficients of the differential operator depend on $\tau(\mathbf{x})$. The most general second-order scalar wave equation consistent with P-MM-1 through P-MM-6 reads:

$$
\partial_i \big[A^{ij}(\mathbf{x}/a)\, \partial_j \psi(\mathbf{x})\big] + k_0^{2}\, B(\mathbf{x}/a)\, \psi(\mathbf{x}) = 0.
$$

Here:

- $A^{ij}(\mathbf{y})$ is the substrate's local rule-type *kinetic response tensor* — the substrate-level pre-image of $1/\mu_r$ for electromagnetic waves, of $1/\rho$ for acoustic waves, of the local inverse-mass tensor for matter waves, etc. The specific identification will be made in Memo 4. Here we treat $A^{ij}$ generically.
- $B(\mathbf{y})$ is the substrate's local rule-type *potential response* — the substrate-level pre-image of $\varepsilon_r$ for electromagnetic waves, of the local compressibility for acoustic waves, etc.
- Both $A^{ij}$ and $B$ depend on $\mathbf{y} = \mathbf{x}/a$ (the rescaled position), reflecting that the rule-type microstructure is periodic with unit cell of size $a$.

The dependence on $\mathbf{x}/a$ rather than directly on $\mathbf{x}$ is the substrate-level statement that the rule-type structure varies on the *microstructure scale* $a$ while $\mathbf{x}$ varies on all scales. Mathematically, $A^{ij}$ and $B$ are $\mathbf{y}$-periodic:

$$
A^{ij}(\mathbf{y} + \mathbf{e}_k) = A^{ij}(\mathbf{y}), \qquad B(\mathbf{y} + \mathbf{e}_k) = B(\mathbf{y}),
$$

for each lattice vector $\mathbf{e}_k$ (with $|\mathbf{e}_k| = 1$ in $\mathbf{y}$-units, equivalent to $|\mathbf{e}_k| = a$ in $\mathbf{x}$-units).

### 1.3 The wavelength regime

The chain's coarse-grained wavelength $\lambda \sim 2\pi/k_0$ satisfies $\lambda \gg a$ by P-MM-6. We define the dimensionless small parameter

$$
\varepsilon = \frac{a}{\lambda} \ll 1.
$$

The multi-scale expansion is an asymptotic series in $\varepsilon$, equivalently in $a$ at fixed $\lambda$. For typical metamaterials, $\varepsilon \sim 0.05$–$0.2$ — small enough for the leading-order homogenization result to be accurate to within $O(\varepsilon^2)$ corrections.

### 1.4 What this memo derives

Two outputs:

1. The *derivative-splitting rule* $\nabla_\mathbf{x} \to \nabla_\mathbf{X} + a^{-1}\nabla_\mathbf{y}$, and the consequent expansion of the propagation equation order-by-order in $a$.

2. The *leading-order equations* at orders $a^{-2}$, $a^{-1}$, $a^0$, which feed directly into Memo 3 (the cell problem).

The substrate-level reading of the expansion — what "fast" and "slow" mean in ED terms — is articulated in §6.

---

## 2. Fast and Slow Variables

### 2.1 Definitions

Define two coordinate systems:

$$
\mathbf{X} = \mathbf{x} \qquad \text{(slow variable)},
$$

$$
\mathbf{y} = \mathbf{x}/a \qquad \text{(fast variable)}.
$$

The slow variable $\mathbf{X}$ is identical to the original spatial coordinate $\mathbf{x}$. It varies on the macroscopic scale $L$ — i.e., the slow variable changes appreciably only over distances of order $\lambda$ or $L$.

The fast variable $\mathbf{y}$ is the original position rescaled by the unit-cell size. It varies on the microstructure scale $a$ — i.e., a change in $\mathbf{x}$ by one unit cell $a$ corresponds to a change in $\mathbf{y}$ by one unit. The fast variable indexes position *within* the unit cell.

### 2.2 Two-scale ansatz

The two-scale ansatz treats $\mathbf{X}$ and $\mathbf{y}$ as *independent variables*:

$$
\psi(\mathbf{x}) \to \tilde\psi(\mathbf{X}, \mathbf{y}),
$$

with the original $\psi$ recovered by setting $\mathbf{X} = \mathbf{x}$ and $\mathbf{y} = \mathbf{x}/a$ in $\tilde\psi$:

$$
\psi(\mathbf{x}) = \tilde\psi(\mathbf{X}, \mathbf{y}) \Big|_{\mathbf{X} = \mathbf{x},\, \mathbf{y} = \mathbf{x}/a}.
$$

This is a formal trick: we lift a function of one variable to a function of two independent variables, then evaluate the lift at the "diagonal" $\mathbf{X} = \mathbf{x}, \mathbf{y} = \mathbf{x}/a$ to recover the original.

The lift is constrained by *periodicity in $\mathbf{y}$*: at each fixed $\mathbf{X}$, $\tilde\psi(\mathbf{X}, \cdot)$ is a periodic function on the unit cell $Y = [0,1]^d$ (in $d$ spatial dimensions):

$$
\tilde\psi(\mathbf{X}, \mathbf{y} + \mathbf{e}_k) = \tilde\psi(\mathbf{X}, \mathbf{y}).
$$

This periodicity matches the periodicity of the rule-type structure (P-MM-1 + P-MM-2): the substrate looks identical after a translation by one unit cell in $\mathbf{x}$ (equivalently one unit in $\mathbf{y}$), so any leading-order coarse-grained quantity should respect this symmetry locally.

### 2.3 Why two scales suffice

Three scales appear in the problem: $a$ (microstructure), $\lambda$ (chain wavelength), $L$ (macroscale). The two-scale ansatz lumps $\lambda$ and $L$ together as "slow" because both are large compared to $a$. This is valid when $a \ll \lambda$, which is the homogenization regime (P-MM-6 with $\lambda \ll L$ guaranteed by experimental design).

For finer resolution — when $\lambda \sim L$ or when the macroscale itself supports non-trivial structure — a three-scale expansion would be needed. We do not pursue this here; the two-scale expansion is sufficient for the metamaterials targeted in this Arc.

---

## 3. The Derivative-Splitting Rule

### 3.1 Chain rule on the lift

For any function $f(\mathbf{x})$, the lift $\tilde f(\mathbf{X}, \mathbf{y})$ with $\mathbf{X} = \mathbf{x}, \mathbf{y} = \mathbf{x}/a$ has partial derivatives related to the original by the chain rule:

$$
\frac{\partial f(\mathbf{x})}{\partial x^i} = \frac{\partial \tilde f(\mathbf{X}, \mathbf{y})}{\partial X^i}\bigg|_{\mathbf{X} = \mathbf{x}} \cdot \frac{\partial X^j}{\partial x^i}\delta^i_j + \frac{\partial \tilde f(\mathbf{X}, \mathbf{y})}{\partial y^i}\bigg|_{\mathbf{y} = \mathbf{x}/a} \cdot \frac{\partial y^j}{\partial x^i}\delta^i_j.
$$

With $\partial X^j/\partial x^i = \delta^j_i$ (since $\mathbf{X} = \mathbf{x}$) and $\partial y^j/\partial x^i = (1/a)\delta^j_i$ (since $\mathbf{y} = \mathbf{x}/a$):

$$
\boxed{\quad \frac{\partial f}{\partial x^i} = \frac{\partial \tilde f}{\partial X^i} + \frac{1}{a}\frac{\partial \tilde f}{\partial y^i}.\quad }
$$

Equivalently, in operator form:

$$
\nabla_\mathbf{x} = \nabla_\mathbf{X} + \frac{1}{a}\nabla_\mathbf{y}.
$$

This is the *derivative-splitting rule*. It states that a single derivative on $\mathbf{x}$ becomes a sum of two pieces under the two-scale lift: a slow-derivative piece (acting on $\mathbf{X}$ only) and a fast-derivative piece (acting on $\mathbf{y}$ only, scaled by $1/a$).

### 3.2 Second derivatives

Iterating the rule:

$$
\frac{\partial^2 f}{\partial x^i \partial x^j} = \left(\frac{\partial}{\partial X^i} + \frac{1}{a}\frac{\partial}{\partial y^i}\right)\left(\frac{\partial}{\partial X^j} + \frac{1}{a}\frac{\partial}{\partial y^j}\right)\tilde f.
$$

Expanding:

$$
\frac{\partial^2 f}{\partial x^i \partial x^j} = \frac{\partial^2 \tilde f}{\partial X^i \partial X^j} + \frac{1}{a}\left(\frac{\partial^2 \tilde f}{\partial X^i \partial y^j} + \frac{\partial^2 \tilde f}{\partial y^i \partial X^j}\right) + \frac{1}{a^{2}}\frac{\partial^2 \tilde f}{\partial y^i \partial y^j}.
$$

The leading-order term is $a^{-2}\partial_{y^i}\partial_{y^j}\tilde f$ — the fast-fast derivative, which dominates when $a$ is small.

### 3.3 General differential operators

For any second-order linear differential operator with $\mathbf{x}/a$-dependent coefficients, the splitting rule produces a sum of operators organized by powers of $1/a$:

$$
\hat L = \hat L_{-2} \cdot a^{-2} + \hat L_{-1} \cdot a^{-1} + \hat L_0 \cdot a^{0} + \ldots,
$$

where each $\hat L_n$ involves a specific combination of fast and slow derivatives. We will compute the $\hat L_n$ for our specific propagation equation in §5.

---

## 4. Asymptotic Expansion of the Amplitude

### 4.1 The expansion ansatz

Expand the chain's pre-individuation amplitude as a series in powers of $a$:

$$
\boxed{\quad \tilde\psi(\mathbf{X}, \mathbf{y}) = \psi_0(\mathbf{X}, \mathbf{y}) + a\, \psi_1(\mathbf{X}, \mathbf{y}) + a^{2}\, \psi_2(\mathbf{X}, \mathbf{y}) + \ldots. \quad}
$$

Each $\psi_n(\mathbf{X}, \mathbf{y})$ is:

- A function of both slow and fast variables.
- Periodic in $\mathbf{y}$ on the unit cell $Y$: $\psi_n(\mathbf{X}, \mathbf{y} + \mathbf{e}_k) = \psi_n(\mathbf{X}, \mathbf{y})$.

The leading-order term $\psi_0$ is the dominant contribution; corrections at orders $a, a^2, \ldots$ are higher-order in the small parameter $\varepsilon = a/\lambda$.

### 4.2 Substrate-level interpretation of the expansion

$\psi_0(\mathbf{X}, \mathbf{y})$ is the chain's pre-individuation amplitude in the *homogenized limit*. We will see in Memo 3 that $\psi_0$ is independent of $\mathbf{y}$ — i.e., it depends only on $\mathbf{X}$. This means: at leading order in $a$, the chain's amplitude does not vary within a unit cell. The chain experiences the substrate as a smooth effective medium.

$\psi_1(\mathbf{X}, \mathbf{y})$ encodes the first-order correction: the *unit-cell oscillation* of the amplitude. At this order, the chain begins to resolve the periodic microstructure. The correction is small ($O(a)$) but determines, via the cell problem of Memo 3, the *effective constitutive parameters* of the homogenized medium.

$\psi_2(\mathbf{X}, \mathbf{y})$ and higher provide $O(a^2)$ corrections to the effective equation. These are the substrate-level FORM-FORCED-INHERITED first-subleading corrections.

---

## 5. Order-by-Order Expansion of the Propagation Equation

### 5.1 Substituting the expansion

Substitute the two-scale ansatz and the asymptotic expansion into the propagation equation. With $\partial_i \to \partial_{X^i} + a^{-1}\partial_{y^i}$, the wave operator becomes (defining $A^{ij} = A^{ij}(\mathbf{y})$ and $B = B(\mathbf{y})$ for brevity):

$$
\left(\partial_{X^i} + \frac{1}{a}\partial_{y^i}\right)\!\left[A^{ij}(\mathbf{y})\left(\partial_{X^j} + \frac{1}{a}\partial_{y^j}\right)\tilde\psi(\mathbf{X}, \mathbf{y})\right] + k_0^{2}\, B(\mathbf{y})\, \tilde\psi(\mathbf{X}, \mathbf{y}) = 0.
$$

Note that the spatial dependence of $A^{ij}, B$ is on $\mathbf{y}$ alone (the fast variable), so slow derivatives act on these coefficients as the zero operator: $\partial_{X^j} A^{ij}(\mathbf{y}) = 0$.

Expanding the product:

$$
\frac{1}{a^{2}}\partial_{y^i}\big[A^{ij}(\mathbf{y})\,\partial_{y^j}\tilde\psi\big]
\;+\; \frac{1}{a}\Big\{\partial_{X^i}\big[A^{ij}(\mathbf{y})\,\partial_{y^j}\tilde\psi\big] + \partial_{y^i}\big[A^{ij}(\mathbf{y})\,\partial_{X^j}\tilde\psi\big]\Big\}
$$
$$
\;+\; \partial_{X^i}\big[A^{ij}(\mathbf{y})\,\partial_{X^j}\tilde\psi\big]
\;+\; k_0^{2}\, B(\mathbf{y})\, \tilde\psi = 0.
$$

### 5.2 Inserting the amplitude expansion

Now insert $\tilde\psi = \psi_0 + a\psi_1 + a^2\psi_2 + \ldots$. Each term in the wave operator produces a series in $a$. Collecting powers of $a$:

**Order $a^{-2}$:**

$$
\partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_0(\mathbf{X}, \mathbf{y})\big] = 0.
$$

**Order $a^{-1}$:**

$$
\partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_1\big] + \partial_{X^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_0\big] + \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{X^j}\psi_0\big] = 0.
$$

**Order $a^{0}$:**

$$
\partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_2\big] + \partial_{X^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_1\big] + \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{X^j}\psi_1\big] + \partial_{X^i}\big[A^{ij}(\mathbf{y})\, \partial_{X^j}\psi_0\big] + k_0^{2}\, B(\mathbf{y})\, \psi_0 = 0.
$$

Higher orders ($a^1, a^2, \ldots$) follow the same pattern and produce successive corrections.

### 5.3 The three load-bearing equations

The first three orders are the load-bearing equations for the homogenization derivation:

$$
\boxed{
\begin{aligned}
\text{Order } a^{-2}:\quad & \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_0\big] = 0, \\[4pt]
\text{Order } a^{-1}:\quad & \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_1\big] = -\partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{X^j}\psi_0\big] - \partial_{X^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_0\big], \\[4pt]
\text{Order } a^{0}:\quad & \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\psi_2\big] = -\partial_{y^i}\big[A^{ij}\, \partial_{X^j}\psi_1\big] - \partial_{X^i}\big[A^{ij}\, \partial_{y^j}\psi_1\big] - \partial_{X^i}\big[A^{ij}\, \partial_{X^j}\psi_0\big] - k_0^{2} B\, \psi_0.
\end{aligned}
}
$$

Each equation is interpreted as a periodic differential equation on the unit cell $Y$ (in $\mathbf{y}$) parameterized by the slow variable $\mathbf{X}$.

### 5.4 The structure of solvability

Each order-$n$ equation has the structure $L_y[\psi_n] = (\text{source involving } \psi_{n-1}, \psi_{n-2}, \ldots)$, where $L_y$ is the *cell operator* acting on $\mathbf{y}$:

$$
L_y[\phi] \equiv \partial_{y^i}\big[A^{ij}(\mathbf{y})\, \partial_{y^j}\phi\big].
$$

The cell operator $L_y$ is a periodic second-order operator on the unit cell. By the structure of periodic differential equations, $L_y[\phi] = f$ has a solution for $\phi$ periodic in $\mathbf{y}$ if and only if the source $f$ satisfies a *solvability condition* (the source must have zero average over the unit cell). This solvability condition will turn out to be the *homogenized effective wave equation* for $\psi_0(\mathbf{X})$. Memo 3 derives the cell problem in detail; Memo 4 derives the effective equation.

---

## 6. The Substrate-Level Meaning of Fast vs Slow

The two-scale expansion is formally an asymptotic manipulation. Its substrate-level interpretation is the substantive content of this Memo.

### 6.1 "Fast" variation is rule-type-microstructure variation

The fast variable $\mathbf{y}$ indexes position within the unit cell. Variation in $\mathbf{y}$ corresponds to variation across the substrate's *rule-type microstructure* (P-MM-1): from one type of substrate-rule region to another within the unit cell.

In a periodic dielectric photonic crystal, varying $\mathbf{y}$ at fixed $\mathbf{X}$ means moving from a dielectric-rod region to a vacuum region, within the same unit cell. The rule-type structure changes abruptly as we move; the chain's amplitude $\psi$ also varies — but at substrate-level, the variation reflects the chain's *local adaptation* to the rule-type structure it encounters as it threads through the cell.

The substrate-level statement: fast variation in $\mathbf{y}$ is the chain's identity-alignment responding to the rule-type microstructure within each unit cell. The chain doesn't "see" the unit cell as a single homogeneous medium; locally it sees the distinct rule-type structures. Its amplitude oscillates within the cell to accommodate the abrupt rule-type changes.

### 6.2 "Slow" variation is macroscopic chain propagation

The slow variable $\mathbf{X}$ indexes the chain's propagation across many unit cells. Variation in $\mathbf{X}$ corresponds to the chain's *coarse-grained motion through the substrate at scales much larger than the unit cell*.

The substrate-level statement: slow variation in $\mathbf{X}$ is the chain's *effective* (coarse-grained) trajectory through the structured medium. From a vantage of $\lambda \gg a$, the chain appears to move smoothly through a continuous effective medium; the granular rule-type microstructure is invisible at this scale, because it has been integrated over.

### 6.3 Why the leading-order amplitude is $\mathbf{y}$-independent

We will derive in Memo 3 that $\psi_0(\mathbf{X}, \mathbf{y})$ is independent of $\mathbf{y}$. The substrate-level reading: at leading order, the chain's amplitude does not see the unit-cell variation. The chain probes only the average rule-type response.

This is consistent with P-MM-6: when $\lambda \gg a$, the chain's *probe scale* is much larger than the rule-type microstructure scale. The chain's coarse-grained amplitude must therefore be approximately uniform over each unit cell, varying only on scales $\sim \lambda$.

### 6.4 Why corrections at $O(a)$ are unit-cell oscillations

The first-order correction $\psi_1(\mathbf{X}, \mathbf{y})$ generically depends on $\mathbf{y}$. This is the substrate-level statement that, at $O(a)$, the chain begins to resolve the unit-cell rule-type variation. The amplitude acquires a small oscillation pattern within each cell.

The cell-problem solution (derived in Memo 3) characterizes this oscillation pattern. The pattern determines, through the order-$a^0$ solvability condition (derived in Memo 4), the *effective constitutive parameters* — i.e., the volume-averaged rule-type response that the chain experiences at the slow scale.

### 6.5 Why the expansion converges in the homogenization regime

The asymptotic expansion is in powers of $a$ at fixed $\lambda$, equivalently in powers of $\varepsilon = a/\lambda$. The expansion converges when $\varepsilon \ll 1$. P-MM-6 guarantees $\varepsilon \ll 1$ in the homogenization regime.

Outside the homogenization regime (when $\lambda \sim a$), the expansion fails. This is the Bragg regime, where the chain wavelength matches the unit-cell spacing and photonic bandgaps appear. The substrate-level meaning: when $\lambda \sim a$, the chain's coarse-grained probe scale equals the rule-type microstructure scale, and the chain *does* resolve the unit cell — destroying the separability of fast and slow variation. In this regime, Bloch-theorem machinery (separate from this Arc) governs the propagation.

The transition between homogenization regime ($\lambda \gg a$) and Bragg regime ($\lambda \sim a$) is structurally sharp: the multi-scale expansion converges below the Bragg condition and breaks down above it.

---

## 7. The Free-Space Limit

A consistency check: when the rule-type microstructure is trivial (vacuum everywhere), $A^{ij}(\mathbf{y}) = \delta^{ij}$ and $B(\mathbf{y}) = 1$, both independent of $\mathbf{y}$. The cell operator becomes $L_y = \nabla_y^2$, the Laplacian on the unit cell.

The order-$a^{-2}$ equation reduces to $\nabla_y^2 \psi_0 = 0$, whose periodic solutions on the unit cell are the constants. So $\psi_0$ is $\mathbf{y}$-independent: $\psi_0 = \psi_0(\mathbf{X})$ only.

The order-$a^{-1}$ equation becomes $\nabla_y^2 \psi_1 = 0$ (since $\psi_0$ is $\mathbf{y}$-independent and $A^{ij}$ is constant), so $\psi_1$ is also constant in $\mathbf{y}$; we can choose $\psi_1 = 0$ without loss of generality.

The order-$a^0$ equation reduces to $\nabla_X^2 \psi_0 + k_0^{2}\psi_0 = 0$, the free-space wave equation.

This confirms that the expansion recovers free-space propagation in the trivial limit, as required.

---

## 8. What This Memo Has Established

The two-scale machinery is in place:

- Two-scale ansatz $\tilde\psi(\mathbf{X}, \mathbf{y})$ with periodicity in $\mathbf{y}$.
- Asymptotic expansion $\tilde\psi = \psi_0 + a\psi_1 + a^2\psi_2 + \ldots$
- Derivative-splitting rule $\nabla_\mathbf{x} = \nabla_\mathbf{X} + a^{-1}\nabla_\mathbf{y}$.
- Order-by-order equations at orders $a^{-2}, a^{-1}, a^0$, each a periodic equation on the unit cell.
- Substrate-level interpretation: fast variation = within-unit-cell rule-type microstructure response; slow variation = coarse-grained chain propagation across many cells.

The machinery is the foundation for Memos 3 through 11.

---

## 9. What's Forced, What's Inherited, What's Open

### What is FORCED by the substrate ontology

- **Existence of a two-scale structure** in the chain's amplitude when the substrate is periodic with $\lambda \gg a$. FORCED by P-MM-1 + P-MM-2 + P-MM-6.
- **The derivative-splitting rule** $\nabla_\mathbf{x} = \nabla_\mathbf{X} + a^{-1}\nabla_\mathbf{y}$. FORCED by the chain rule applied to the two-scale lift $\mathbf{X} = \mathbf{x}, \mathbf{y} = \mathbf{x}/a$.
- **The order-by-order equations** of §5.3. FORCED by substitution of the asymptotic expansion into the propagation equation and collection of powers of $a$.
- **$\mathbf{y}$-periodicity of each $\psi_n$**. FORCED by the substrate's periodicity (P-MM-2): any coarse-grained amplitude must respect the local rule-type symmetry.
- **Convergence of the expansion in the homogenization regime $\lambda \gg a$**. FORCED by the asymptotic-series structure with small parameter $\varepsilon = a/\lambda$.
- **Substrate-level interpretation of fast/slow variation** (§6). FORCED by the substrate's primitive structure: rule-type microstructure varies on scale $a$, chain propagation is coarse-grained on scale $\lambda$.

### What is FORM-FORCED-INHERITED (and re-derived inside this memo)

- **Chain rule for partial derivatives.** Standard calculus, used in §3.1.
- **Asymptotic-series formalism** (collecting powers of a small parameter). Standard. Used in §5.
- **The scalar wave-equation form** $\partial_i [A^{ij}\partial_j \psi] + k_0^2 B \psi = 0$. The exact form of the substrate's coarse-grained propagation equation is inherited from coarse-graining of T17 + Klein-Gordon §6 minimal coupling; here we treat it as a given. Memo 4 will identify $A^{ij}$ and $B$ with specific physical quantities.
- **Periodic boundary conditions on the unit cell.** Standard from solid-state physics; the substrate-level justification is P-MM-2.

### What remains OPEN

- **Tight bounds on the rate of convergence of the expansion.** The expansion is formally asymptotic; rigorous bounds on the error at finite $a$ for a specific class of substrate microstructures are OPEN. FORM-FORCED expected at $O(a^2/\lambda^2)$ but explicit coefficients deferred.
- **Three-scale expansion** when $\lambda \sim L$ or when the macroscale itself carries non-trivial structure (e.g., curved waveguides at the macroscale). OPEN; would generalize the two-scale machinery here.
- **Non-Hermitian and dissipative substrate microstructures.** When the substrate's rule-type structure has gain or loss (non-Hermitian $A^{ij}, B$), the cell problem changes structure. OPEN.
- **Random (non-periodic) substrate microstructures.** When the substrate is statistically homogeneous but not periodic, the multi-scale expansion is replaced by ensemble-averaging machinery (stochastic homogenization). OPEN; structurally parallel but requires probability-measure tools.
- **Vector and tensor amplitudes**. We treated $\psi$ as a scalar for simplicity. Vector (electromagnetic) and tensor (gravitational) amplitudes follow the same structural argument with index complications. The structural conclusions are unchanged; the formula complexity grows. Memo 4 takes this up explicitly for the EM case.
- **Strong-contrast microstructures.** When $A^{ij}$ varies by orders of magnitude within the unit cell (e.g., metal-vacuum composites near the percolation threshold), the leading-order expansion may need modification (high-contrast homogenization). OPEN.

---

## 10. Review and Recommended Next Steps

### Review

Memo 2 has delivered the multi-scale expansion machinery for channel propagation in a periodic rule-type substrate:

- Setup: a chain in a substrate with rule-type microstructure varying periodically on scale $a$ (P-MM-1, P-MM-2). Wavelength regime $\lambda \gg a$ (P-MM-6).
- Two-scale lift $\psi(\mathbf{x}) \to \tilde\psi(\mathbf{X}, \mathbf{y})$ with $\mathbf{X} = \mathbf{x}$ (slow) and $\mathbf{y} = \mathbf{x}/a$ (fast), and periodicity in $\mathbf{y}$.
- Derivative-splitting rule $\nabla_\mathbf{x} = \nabla_\mathbf{X} + a^{-1}\nabla_\mathbf{y}$ (§3).
- Asymptotic expansion $\tilde\psi = \psi_0 + a\psi_1 + a^2\psi_2 + \ldots$ (§4).
- Order-by-order equations at orders $a^{-2}, a^{-1}, a^0$ (§5.3) — the load-bearing equations for Memos 3 and 4.
- Substrate-level interpretation of fast/slow variation (§6).
- Free-space consistency check (§7).
- Explicit FORCED / INHERITED / OPEN labeling (§9).

The machinery is now in place for the cell problem (Memo 3).

### Honest scope-limit

This memo introduced no new substrate primitives beyond P-MM-1 through P-MM-6 (Memo 1's inventory). All steps are derived inline. No cross-references to other arcs.

### Recommended next steps

In order:

1. **Memo 3 — The Cell Problem and Averaging Operator.** Solve the order-$a^{-2}$ equation to establish $\psi_0$'s structure (it is $\mathbf{y}$-independent). Solve the order-$a^{-1}$ equation to derive the cell problem for $\psi_1$: $\psi_1(\mathbf{X}, \mathbf{y}) = \chi^j(\mathbf{y}) \partial_{X^j}\psi_0(\mathbf{X})$, where $\chi^j$ is the cell-problem solution. Define the unit-cell averaging operator $\langle \cdot \rangle = (1/|Y|)\int_Y d^dy\, (\cdot)$ and articulate the solvability condition that produces the effective equation.

2. **Memo 4 — Effective Constitutive Relations.** Apply the solvability condition at order $a^0$ to derive the homogenized effective equation for $\psi_0(\mathbf{X})$. Identify the effective constitutive parameters $\varepsilon_\text{eff}^{ij}$ and $\mu_\text{eff}^{ij}$ in terms of cell-problem solutions and the substrate's microstructure $A^{ij}, B$.

3. **Memo 5 — Substrate-Level Meaning of $\varepsilon$ and $\mu$.** Articulate what these effective constitutive parameters mean at substrate level.

4. **Memo 6 — Conditions for Negative Index (Pendry 2000).** Wire-array and split-ring-resonator microstructures and their effective response.

After Memo 6, the homogenization cluster (Memos 2–6) is closed, and Memos 7–11 build on it for transformation optics.

### Anchor for future memos

Throughout the remainder of the Arc, the two-scale expansion and derivative-splitting rule of Memo 2 will be invoked. The notation $\psi_0(\mathbf{X}), \psi_1(\mathbf{X}, \mathbf{y}), \chi^j(\mathbf{y})$, the cell operator $L_y$, the averaging operator $\langle \cdot \rangle$ (to be defined in Memo 3) — all are standardized by this Memo's machinery and will not be re-derived in later memos.
