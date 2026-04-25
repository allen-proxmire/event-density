# Klein-Gordon Minimal Coupling + Conserved Four-Current

**Date:** 2026-04-24
**Location:** `quantum/foundations/kg_minimal_coupling_and_current.md`
**Status:** Phase-2 Arc-R Stage R.1 follow-up memo. Extends the free-particle Klein-Gordon derivation of `klein_gordon_emergence.md` to include minimal electromagnetic coupling and derives the associated conserved four-current. Scalar case (bosonic chains) throughout; spinor (Dirac) content is not addressed in this memo.
**Purpose:** Complete Stage R.1 of the relativistic arc at the level of a charged scalar particle in an external electromagnetic field. Stays strictly within scalar minimal coupling + current; rule-type taxonomy (prerequisite for Dirac) is flagged in §8 but not undertaken.

---

## 1. Starting material

### 1.1 The free-particle Klein-Gordon equation

From `klein_gordon_emergence.md` §4, the coherent-sum wavefunction $\Psi(x^\mu)$ for a scalar chain satisfies
\begin{equation}
  \left(\Box + \frac{m^2 c^2}{\hbar^2}\right) \Psi(x^\mu) = 0,
  \label{eq:KG_free}
\end{equation}
with $\Box = \partial_\mu \partial^\mu$ the d'Alembertian, $m$ the particle's inherited mass, and $\hbar$ inherited via the Dimensional Atlas.

### 1.2 What this memo adds

- The minimal-coupling replacement $p_\mu \to p_\mu - q A_\mu$ promoting (eq:KG_free) to the interacting Klein-Gordon equation for a charged scalar particle in an external electromagnetic field.
- The gauge-covariant derivative $D_\mu = \partial_\mu + (i q / \hbar) A_\mu$.
- The conserved four-current for the minimally-coupled equation.
- The explicit non-relativistic limit giving the Schrödinger equation with electromagnetic coupling.

### 1.3 What this memo does not do

- No spinor / Dirac content. All operations are scalar throughout.
- No derivation of the rule-type taxonomy (Primitive 07 §7.4) — deferred to Arc R Stage R.2.
- No derivation of the specific value of the electromagnetic charge $q$ or the electromagnetic potential $A_\mu$; both are inherited.

---

## 2. Minimal coupling

### 2.1 The prescription

In classical electrodynamics, the canonical momentum of a charged particle in an external electromagnetic field differs from the kinetic momentum:
\begin{equation}
  p_\mu^{\mathrm{canonical}} = p_\mu^{\mathrm{kinetic}} + q A_\mu.
\end{equation}

Rearranging, the kinetic four-momentum in terms of the canonical four-momentum and the electromagnetic four-potential $A_\mu = (\varphi/c, -\mathbf{A})$ is
\begin{equation}
  \pi_\mu \equiv p_\mu - q A_\mu.
  \label{eq:kinetic_momentum}
\end{equation}

The minimal-coupling prescription in quantum mechanics is the substitution
\begin{equation}
  p_\mu \to \pi_\mu = p_\mu - q A_\mu
\end{equation}
in the mass-shell condition (or in the Lagrangian / Hamiltonian formalism of the free theory).

### 2.2 Operator form

In wave-mechanical form, the canonical four-momentum is represented by the differential operator $\hat{p}_\mu = -i \hbar \partial_\mu$. The minimal-coupling prescription becomes
\begin{equation}
  -i \hbar \partial_\mu \to -i \hbar \partial_\mu - q A_\mu = -i \hbar \left(\partial_\mu + \frac{i q}{\hbar} A_\mu\right).
\end{equation}

Defining the **gauge-covariant derivative**
\begin{equation}
  D_\mu \equiv \partial_\mu + \frac{i q}{\hbar} A_\mu,
  \label{eq:covariant_derivative}
\end{equation}
the minimal-coupling prescription takes the form
\begin{equation}
  \partial_\mu \to D_\mu.
\end{equation}

### 2.3 Primitive-level justification

At the primitive level, the electromagnetic potential $A_\mu$ represents an external structural influence on the chain, extending the Phase-1 notion of an external potential $V(x)$ to a Lorentz-covariant four-potential. The coupling constant $q$ is the chain's electromagnetic charge — inherited at the species level along with the mass.

The minimal-coupling prescription is FORCED by the requirement of local U(1) gauge invariance: if the phase of $\Psi$ can be redefined locally via $\Psi \to e^{i q \alpha(x)/\hbar} \Psi$, the evolution equation must be invariant under simultaneous redefinition $A_\mu \to A_\mu + \partial_\mu \alpha$. This gauge symmetry forces the $\partial_\mu$ in the evolution equation to be replaced by $D_\mu$ (see §4 for the gauge covariance argument).

**Status of minimal coupling: FORCED** conditional on the local U(1) gauge invariance as a structural commitment. The gauge invariance itself is a primitive-level structural feature at the participation-phase level; its primitive-level derivation is flagged briefly in §8 but not undertaken here.

---

## 3. The interacting Klein-Gordon equation

### 3.1 Substitution into the mass-shell condition

The free-particle mass-shell condition $p_\mu p^\mu = m^2 c^2$ (from `klein_gordon_emergence.md` §3.4) becomes, under minimal coupling,
\begin{equation}
  \pi_\mu \pi^\mu = m^2 c^2 \quad \Longleftrightarrow \quad (p_\mu - q A_\mu)(p^\mu - q A^\mu) = m^2 c^2.
\end{equation}

In operator form, this translates to the interacting Klein-Gordon equation:
\begin{equation}
  \boxed{\left(D_\mu D^\mu + \frac{m^2 c^2}{\hbar^2}\right) \Psi(x^\nu) = 0.}
  \label{eq:KG_interacting}
\end{equation}

### 3.2 Explicit expansion

Writing out the covariant derivative,
\begin{equation}
  D_\mu D^\mu = \left(\partial_\mu + \frac{i q}{\hbar} A_\mu\right)\left(\partial^\mu + \frac{i q}{\hbar} A^\mu\right),
\end{equation}
which expands as
\begin{equation}
  D_\mu D^\mu = \Box + \frac{i q}{\hbar}\left(A_\mu \partial^\mu + \partial_\mu A^\mu\right) \cdot (\,\cdot\,) - \frac{q^2}{\hbar^2} A_\mu A^\mu,
\end{equation}
where the notation $\partial_\mu A^\mu \cdot (\,\cdot\,)$ indicates that the derivative acts on everything to its right (including the wavefunction). Explicitly,
\begin{equation}
  D_\mu D^\mu \Psi = \Box \Psi + \frac{i q}{\hbar}\left[A_\mu \partial^\mu \Psi + \partial_\mu (A^\mu \Psi)\right] - \frac{q^2}{\hbar^2} A_\mu A^\mu \Psi.
\end{equation}

In Lorenz gauge ($\partial_\mu A^\mu = 0$), the simplified form is
\begin{equation}
  D_\mu D^\mu \Psi = \Box \Psi + \frac{2 i q}{\hbar} A_\mu \partial^\mu \Psi - \frac{q^2}{\hbar^2} A_\mu A^\mu \Psi.
\end{equation}

The interacting Klein-Gordon equation reduces to the free-particle equation (eq:KG_free) when $A_\mu = 0$, and inherits the d'Alembertian + mass-term structure otherwise.

### 3.3 Status

**The interacting Klein-Gordon equation (eq:KG_interacting) is FORCED** by the combination of:
- The free-particle Klein-Gordon form (from `klein_gordon_emergence.md`, FORCED).
- The minimal-coupling prescription (FORCED by local U(1) gauge invariance).
- The gauge-covariant derivative (eq:covariant_derivative), which is the unique first-order gauge-covariant derivative consistent with the gauge-transformation rules.

---

## 4. Gauge covariance

### 4.1 Local U(1) gauge transformation

A local U(1) gauge transformation parameterized by a scalar function $\alpha(x^\mu)$ acts on the wavefunction and the electromagnetic potential as
\begin{align}
  \Psi(x^\mu) &\to \Psi'(x^\mu) = e^{i q \alpha(x^\nu)/\hbar} \Psi(x^\mu), \\
  A_\mu(x^\nu) &\to A'_\mu(x^\nu) = A_\mu(x^\nu) + \partial_\mu \alpha(x^\nu).
  \label{eq:gauge_transf}
\end{align}

### 4.2 Transformation of the covariant derivative

Compute the transformation of $D_\mu \Psi$:
\begin{align}
  D'_\mu \Psi' &= \left(\partial_\mu + \frac{i q}{\hbar} A'_\mu\right) \left(e^{i q \alpha/\hbar} \Psi\right) \\
  &= e^{i q \alpha/\hbar} \left[\partial_\mu \Psi + \frac{i q}{\hbar}(\partial_\mu \alpha) \Psi + \frac{i q}{\hbar}(A_\mu + \partial_\mu \alpha) \Psi\right] \\
  &= e^{i q \alpha/\hbar} \left[\partial_\mu \Psi + \frac{i q}{\hbar} A_\mu \Psi + \frac{i q}{\hbar}(\partial_\mu \alpha) \Psi - \frac{i q}{\hbar}(\partial_\mu \alpha) \Psi\right].
\end{align}

The $\partial_\mu \alpha$ terms cancel, leaving
\begin{equation}
  D'_\mu \Psi' = e^{i q \alpha/\hbar} D_\mu \Psi.
  \label{eq:Dmu_covariant}
\end{equation}

**The covariant derivative transforms with the same phase factor as the wavefunction.** This is the defining property of $D_\mu$.

### 4.3 Invariance of the Klein-Gordon equation

Applying the above argument twice, $D_\nu D^\nu \Psi$ transforms as
\begin{equation}
  (D'_\nu D'^\nu) \Psi' = e^{i q \alpha/\hbar} D_\nu D^\nu \Psi.
\end{equation}

The interacting Klein-Gordon equation (eq:KG_interacting) picks up an overall phase $e^{i q \alpha/\hbar}$ under gauge transformation. Since the equation states that this quantity equals zero, the equation is **gauge-invariant**.

**Status: FORCED** by the construction of $D_\mu$ with the specific phase structure in (eq:covariant_derivative). The choice of minimal coupling is the unique first-order gauge-covariant extension of the free Klein-Gordon equation.

---

## 5. The conserved four-current

### 5.1 Definition

The four-current for the minimally-coupled Klein-Gordon equation is defined by
\begin{equation}
  \boxed{j^\mu(x^\nu) = \frac{i \hbar}{2 m}\left[\Psi^* D^\mu \Psi - \Psi \left(D^\mu \Psi\right)^*\right].}
  \label{eq:current_def}
\end{equation}

Several forms are equivalent under integration by parts and Leibniz rule; the form above is manifestly Hermitian in the sense that $j^\mu$ is real (note the factor $i$ and the $\Psi^* \cdots - \Psi \cdots$ antisymmetrization).

### 5.2 Reality of $j^\mu$

The bracketed quantity $\Psi^* D^\mu \Psi - \Psi (D^\mu \Psi)^*$ is pure imaginary (it is the difference of a complex number and its conjugate). Multiplying by $i$ gives a real quantity, and the prefactor $\hbar / (2m)$ is real. Therefore $j^\mu$ is a real four-vector, as required for a physical conserved current.

### 5.3 Gauge invariance of $j^\mu$

Under gauge transformation (eq:gauge_transf), the wavefunction picks up the phase $e^{i q \alpha/\hbar}$, and the covariant derivative transforms with the same phase (eq:Dmu_covariant). Therefore the bilinear $\Psi^* D^\mu \Psi$ transforms as
\begin{equation}
  \Psi^* D^\mu \Psi \to (e^{-i q \alpha/\hbar} \Psi^*)(e^{i q \alpha/\hbar} D^\mu \Psi) = \Psi^* D^\mu \Psi.
\end{equation}

The bilinear is invariant; consequently the four-current (eq:current_def) is gauge-invariant.

**Status: FORCED** by the gauge-covariant transformation rules.

### 5.4 Derivation of the continuity equation

**Claim:** $\partial_\mu j^\mu = 0$ for any $\Psi$ satisfying the interacting Klein-Gordon equation (eq:KG_interacting).

**Proof.** Take the four-divergence of (eq:current_def):
\begin{equation}
  \partial_\mu j^\mu = \frac{i \hbar}{2 m}\left[\partial_\mu\left(\Psi^* D^\mu \Psi\right) - \partial_\mu\left(\Psi (D^\mu \Psi)^*\right)\right].
\end{equation}

Observe that the bilinears $\Psi^* D^\mu \Psi$ and $\Psi (D^\mu \Psi)^*$ are gauge-invariant scalars (net charge zero). For such scalars, the four-divergence $\partial_\mu$ equals the gauge-covariant four-divergence $D_\mu$:
\begin{equation}
  \partial_\mu\left(\Psi^* D^\mu \Psi\right) = D_\mu\left(\Psi^* D^\mu \Psi\right) = (D_\mu \Psi)^* D^\mu \Psi + \Psi^* D_\mu D^\mu \Psi.
\end{equation}

Using the interacting Klein-Gordon equation $D_\mu D^\mu \Psi = -(m^2 c^2/\hbar^2) \Psi$:
\begin{equation}
  \partial_\mu\left(\Psi^* D^\mu \Psi\right) = (D_\mu \Psi)^* D^\mu \Psi - \frac{m^2 c^2}{\hbar^2} |\Psi|^2.
\end{equation}

Similarly, for the conjugate bilinear:
\begin{align}
  \partial_\mu\left(\Psi (D^\mu \Psi)^*\right) &= D_\mu\left(\Psi (D^\mu \Psi)^*\right) \\
  &= (D_\mu \Psi) (D^\mu \Psi)^* + \Psi \left(D_\mu D^\mu \Psi\right)^* \\
  &= (D_\mu \Psi) (D^\mu \Psi)^* - \frac{m^2 c^2}{\hbar^2} |\Psi|^2.
\end{align}

Subtracting the two expressions:
\begin{align}
  \partial_\mu(\Psi^* D^\mu \Psi) - \partial_\mu(\Psi (D^\mu \Psi)^*) &= (D_\mu \Psi)^* D^\mu \Psi - (D_\mu \Psi) (D^\mu \Psi)^* \\
  &= 0,
\end{align}
where the last equality follows because the two quantities $(D_\mu \Psi)^* D^\mu \Psi$ and $(D_\mu \Psi) (D^\mu \Psi)^*$ are complex conjugates of each other, and they are both real (being sesquilinear expressions with index contraction against a real metric). Their difference vanishes.

**Therefore:**
\begin{equation}
  \boxed{\partial_\mu j^\mu = 0.}
  \label{eq:continuity}
\end{equation}

**Status: FORCED** as a mathematical consequence of (eq:KG_interacting). The continuity equation follows algebraically from the interacting Klein-Gordon equation and the definition of the four-current.

### 5.5 Physical interpretation

The four-current has components $j^\mu = (c \rho_{\mathrm{em}}, \mathbf{j}_{\mathrm{em}})$ where $\rho_{\mathrm{em}}$ is the charge density and $\mathbf{j}_{\mathrm{em}}$ is the charge-current density. The continuity equation (eq:continuity) in components reads
\begin{equation}
  \partial_t \rho_{\mathrm{em}} + \nabla \cdot \mathbf{j}_{\mathrm{em}} = 0,
\end{equation}
expressing the local conservation of electric charge.

**Caveat — Klein-Gordon pathology.** The zeroth component $j^0$ of the Klein-Gordon current is NOT positive-definite: $j^0$ can take negative values in regions where the phase structure of $\Psi$ is appropriate, a feature that distinguishes Klein-Gordon from the Schrödinger case (where $|\psi|^2$ is the positive-definite probability density). For a single-particle theory, this non-positive-definiteness is an interpretive obstacle and is one of the standard arguments motivating the QFT extension (Arc Q). For the purposes of this memo, the four-current is treated as a charge-current density rather than a probability density, and the non-positive-definiteness is not an issue at the charge-conservation level.

---

## 6. Non-relativistic limit

### 6.1 Rest-energy factorization with potential

As in the free case (`klein_gordon_emergence.md` §5), factor out the rest-energy phase:
\begin{equation}
  \Psi(\mathbf{x}, t) = e^{-i m c^2 t / \hbar} \psi(\mathbf{x}, t).
  \label{eq:NR_factorization_EM}
\end{equation}

In the presence of an external electromagnetic potential $A_\mu = (\varphi/c, -\mathbf{A})$, additional phase structure is absorbed into the scalar potential $\varphi$ via the minimal-coupling redefinition. The remaining $\psi$ carries the non-relativistic dynamics.

### 6.2 Expansion of the minimally-coupled equation

The covariant derivatives in components:
\begin{align}
  D_0 &= \partial_0 + \frac{i q}{\hbar} A_0 = \frac{1}{c} \partial_t + \frac{i q \varphi}{\hbar c}, \\
  D_i &= \partial_i + \frac{i q}{\hbar} A_i \quad \text{for spatial indices.}
\end{align}

With the gauge convention $\mathbf{A}$ as the spatial three-vector and $\varphi$ as the scalar potential (standard convention), spatial components of $D_\mu$ give
\begin{equation}
  \mathbf{D} = \nabla - \frac{i q}{\hbar} \mathbf{A}, \qquad -i \hbar \mathbf{D} = -i \hbar \nabla - q \mathbf{A}.
\end{equation}

Substituting into $D_\mu D^\mu \Psi = D^0 D_0 \Psi - \mathbf{D} \cdot \mathbf{D} \Psi$ and applying the rest-energy factorization, the analysis follows that of `klein_gordon_emergence.md` §5 with the potential-shifted energy.

### 6.3 Resulting Schrödinger equation

The standard result, after dropping the relativistic-correction term $(1/c^2) \partial_t^2 \psi$ and simplifying, is
\begin{equation}
  \boxed{i \hbar \partial_t \psi = \left[\frac{1}{2m}(-i \hbar \nabla - q \mathbf{A})^2 + q \varphi\right] \psi.}
  \label{eq:SchrodingerEM}
\end{equation}

This is the **Schrödinger equation with electromagnetic coupling** — the non-relativistic wave equation for a charged particle in an external electromagnetic field.

### 6.4 Structural identification

The left-hand side of (eq:SchrodingerEM) is the standard Schrödinger time-evolution. The right-hand side contains the kinetic energy of the charged particle (squared kinetic momentum divided by $2m$) plus the scalar-potential energy $q \varphi$.

**This matches the Phase-1 Schrödinger result** (from `schrodinger_emergence.md` §4, with the potential $V(\mathbf{x})$ now specified as the scalar electromagnetic potential $q \varphi$) augmented by the magnetic-coupling term $-q \mathbf{A}$ in the kinetic momentum.

**Status: FORCED** by the non-relativistic limit of the interacting Klein-Gordon equation. The derivation is mathematically identical to §5 of `klein_gordon_emergence.md` with $\partial_\mu \to D_\mu$ substitutions throughout.

---

## 7. Status classification

### 7.1 Forced content

| Feature | Source |
|---|---|
| Local U(1) gauge invariance as structural commitment | Primitive-level content of participation phase |
| Minimal-coupling prescription $p_\mu \to p_\mu - q A_\mu$ | Unique first-order gauge-covariant extension |
| Gauge-covariant derivative $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$ | Unique form preserving gauge covariance |
| Interacting Klein-Gordon equation $(D_\mu D^\mu + m^2 c^2/\hbar^2) \Psi = 0$ | Minimal coupling applied to free KG |
| Covariant transformation $D'_\mu \Psi' = e^{iq\alpha/\hbar} D_\mu \Psi$ | Direct computation (§4.2) |
| Gauge invariance of the equation | Direct consequence of (§4.2) |
| Four-current $j^\mu$ definition (eq:current_def) | Canonical form for U(1)-conserved current |
| Reality of $j^\mu$ | Direct (§5.2) |
| Gauge invariance of $j^\mu$ | Direct (§5.3) |
| Continuity equation $\partial_\mu j^\mu = 0$ | Direct algebraic consequence of interacting KG (§5.4) |
| Non-relativistic limit to Schrödinger-EM (eq:SchrodingerEM) | Direct rest-energy factorization (§6) |

### 7.2 Inherited content

| Item | Inheritance source |
|---|---|
| Speed of light $c$ | Dimensional Atlas (relativistic regime) |
| Reduced Planck constant $\hbar$ | Dimensional Atlas Madelung anchoring |
| Scalar-particle mass $m$ | Species-level anchoring (chain-mass derivation open, Arc M) |
| Electromagnetic charge $q$ | Species-level anchoring (coupled with chain-mass) |
| Electromagnetic four-potential $A_\mu(x^\nu)$ | External-field specification; apparatus-level |

### 7.3 Not addressed in this memo

- **Dynamical origin of the electromagnetic field.** $A_\mu$ is treated as an external field in this memo; its primitive-level emergence (via Maxwell's equations in the ED framework) is a separate derivation.
- **Quantization of the electromagnetic field.** Photon creation/annihilation, the quantum electrodynamic vertex, Feynman rules — all require the QFT extension (Arc Q).
- **Spinor / Dirac case.** Minimal coupling generalizes straightforwardly to Dirac once the spinor participation measure is available; that requires the rule-type taxonomy (Primitive 07 §7.4, Arc R Stage R.2).

---

## 8. Forward note on rule-type taxonomy and Dirac

### 8.1 What is established

With this memo, the scalar-particle content of Phase-2 Arc-R Stage R.1 is complete. For bosonic (scalar) chains in an external electromagnetic field:
- The wave equation is interacting Klein-Gordon.
- The conserved four-current is the gauge-invariant bilinear $j^\mu$.
- The non-relativistic limit is the Schrödinger equation with electromagnetic coupling.

All three results are FORCED modulo inherited constants.

### 8.2 What blocks Dirac

The Dirac equation for fermionic (spinor) chains requires the spinor participation measure $P_{K,\alpha}(x^\mu) \in \mathbb{C}^4$ and the Clifford algebra $\gamma^\mu$ satisfying $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$. Both require a primitive-level derivation of the rule-type taxonomy (Primitive 07 §7.4): what structurally distinguishes a fermionic chain from a bosonic chain, and what forces the four-component spinor index structure and the Clifford anti-commutation relations?

### 8.3 What the rule-type taxonomy would provide

A primitive-level derivation of the rule-type taxonomy would:
- Classify chain rule-types into bosonic and fermionic (and possibly other) categories.
- Specify the internal index structure for each category: scalar for bosons, spinor for fermions.
- Derive the spin-statistics connection (bosons commute on exchange, fermions anticommute).
- Provide the primitive-level origin of the Clifford algebra for fermionic rule-types.
- Unlock the Dirac emergence derivation (Arc R Stage R.3).

The same derivation is prerequisite for Arc M (chain-mass). Both arcs share this bottleneck.

### 8.4 Stage status

**Stage R.1 (Klein-Gordon for scalar chains):**
- Free-particle Klein-Gordon emergence: complete (`klein_gordon_emergence.md`).
- Minimal coupling + conserved current: complete (this memo).
- Stage R.1 synthesis: next deliverable (short memo consolidating free + interacting scalar case).

**Stage R.2 (rule-type taxonomy):**
- Scoping memo (not yet begun).
- Full derivation (multi-memo; shared with Arc M).

**Stage R.3 (Dirac emergence):**
- Contingent on Stage R.2.
- Multiple memos after taxonomy closure.

---

## 9. Summary

The minimally-coupled Klein-Gordon equation $(D_\mu D^\mu + m^2 c^2/\hbar^2) \Psi = 0$ with $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$ is derived as the gauge-covariant extension of the free Klein-Gordon equation under local U(1) gauge invariance. The associated conserved four-current $j^\mu = (i\hbar/2m)(\Psi^* D^\mu \Psi - \Psi (D^\mu \Psi)^*)$ satisfies the continuity equation $\partial_\mu j^\mu = 0$ as an algebraic consequence of the interacting wave equation. The non-relativistic limit reduces exactly to the Schrödinger equation with electromagnetic coupling, $i\hbar \partial_t \psi = [(1/2m)(-i\hbar \nabla - q\mathbf{A})^2 + q\varphi]\psi$, consistent with the Phase-1 Schrödinger framework.

All structural content is FORCED by the combination of Phase-1 primitive-level results, Arc-R Lorentz-covariance constraints, and local U(1) gauge invariance. The numerical values of the charge $q$, the mass $m$, the speed of light $c$, and $\hbar$ are inherited at the species / empirical-anchoring level. The external electromagnetic field $A_\mu$ is specified by the apparatus context.

Stage R.1 of Arc R (scalar relativistic wave-equation content) is complete at the free-particle-plus-electromagnetic-coupling level. Stage R.2 (rule-type taxonomy) and Stage R.3 (Dirac) remain open; the taxonomy sub-program is shared with Arc M and is the critical prerequisite for both the spinor extension of the relativistic arc and the chain-mass derivation.

---

## 10. Cross-references

### Arc-R Stage R.1 memos
- Relativistic scoping: [`quantum/foundations/relativistic_participation_measure.md`](relativistic_participation_measure.md)
- Free-particle Klein-Gordon: [`quantum/foundations/klein_gordon_emergence.md`](klein_gordon_emergence.md)
- This memo (minimal coupling + conserved current): `kg_minimal_coupling_and_current.md`

### Phase-1 anchoring
- Phase-1 Schrödinger (non-relativistic limit target): [`quantum/foundations/schrodinger_emergence.md`](schrodinger_emergence.md)
- Phase-1 QM-emergence closure: [`quantum/foundations/qm_emergence_closure.md`](qm_emergence_closure.md)
- ℏ-origin memo: [`quantum/foundations/hbar_origin.md`](hbar_origin.md)

### Phase-2 roadmap
- Phase-2 extensions roadmap: [`quantum/foundations/phase2_extensions_roadmap.md`](phase2_extensions_roadmap.md) §2.1
- Rule-type taxonomy and Dirac (deferred to Stages R.2 and R.3)

### Classical references
- Weyl, H. (1929). Elektron und Gravitation I. *Zeitschrift für Physik* **56**, 330–352.
- Dirac, P. A. M. (1928). The Quantum Theory of the Electron. *Proc. Roy. Soc. A* **117**, 610–624.
- Pauli, W. (1940). The Connection Between Spin and Statistics. *Phys. Rev.* **58**, 716–722.
- Weinberg, S. (1995). *The Quantum Theory of Fields*, Vol. 1. Cambridge University Press.

---

## 11. One-line summary

> **Minimal electromagnetic coupling is implemented by the gauge-covariant derivative $D_\mu = \partial_\mu + (iq/\hbar) A_\mu$, promoting the free Klein-Gordon equation to $(D_\mu D^\mu + m^2 c^2/\hbar^2)\Psi = 0$ — FORCED by local U(1) gauge invariance as the unique first-order gauge-covariant extension. The associated conserved four-current $j^\mu = (i\hbar/2m)(\Psi^* D^\mu \Psi - \Psi (D^\mu \Psi)^*)$ is real, gauge-invariant, and satisfies $\partial_\mu j^\mu = 0$ as a direct algebraic consequence of the interacting wave equation — FORCED. Non-relativistic limit via rest-energy factorization $\Psi = e^{-imc^2 t/\hbar}\psi$ yields the Schrödinger equation with electromagnetic coupling $i\hbar \partial_t \psi = [(1/2m)(-i\hbar\nabla - q\mathbf{A})^2 + q\varphi]\psi$, consistent with Phase-1 Schrödinger. Inherited: $q$, $m$, $\hbar$, $c$, $A_\mu$. Stage R.1 of Arc R (scalar relativistic) complete at the free-plus-electromagnetic-coupling level; Stage R.2 (rule-type taxonomy) and Stage R.3 (Dirac) remain open. The taxonomy sub-program is the critical prerequisite for both fermionic content and chain-mass derivation (Arc M), shared across two Phase-2 arcs.**
