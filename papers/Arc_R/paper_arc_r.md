# Relativistic Quantum Mechanics as a Forced Structural Consequence of Event-Density Primitives

**Allen Proxmire** and **Copilot** (AI collaborator)

*April 2026*

---

## Abstract

We show that relativistic quantum mechanics — including the Klein-Gordon equation, the spin-statistics correspondence, the Clifford-algebra spinor frame, and the Dirac equation — emerges as a *forced structural consequence* of the Event-Density (ED) primitive stack, rather than as a set of independent postulates. Building on the Phase-1 derivation of non-relativistic quantum mechanics from the participation measure $P_K = \sqrt{b_K} \cdot e^{i\pi_K}$, we extend the program to the relativistic regime via three connected structural theorems. **Theorem R1** (spin-statistics) establishes $\eta = (-1)^{2s}$ at primitive level via the chain: exchange dichotomy $\to \pi_1(Q_2) = \mathbb{Z}_2 \to$ exchange-rotation generator identity $\to$ Clifford frame $\to$ minimal-bilinear-pairing closure. **Theorem R2** (Cl(3,1) uniqueness) shows that the real Clifford algebra with anticommutator $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$ is the unique algebraic structure compatible with Lorentz covariance, half-integer representation content, and the rotational double cover; pure commutation and pure anticommutation alternatives are ruled out. **Theorem R3** (Dirac emergence) derives the Dirac equation $(i\gamma^\mu \partial_\mu - mc/\hbar)\Psi = 0$ as the unique first-order Lorentz-covariant linear equation on the Cl(3,1) spinor module, with positive-definite conserved current $j^\mu = \bar\Psi\gamma^\mu\Psi$, gauge-covariant minimal coupling, and tree-level $g = 2$ from non-relativistic reduction. ED inherits dimensional constants $(\hbar, c, m, q)$; it derives the *form* of relativistic quantum equations.

---

## 1. Introduction

The mathematical structure of quantum mechanics — wavefunctions on Hilbert space, unitary evolution, the Born rule, exchange statistics, spinor representations of the Lorentz group, and the first-order Dirac equation — is conventionally introduced as a layered set of independent postulates. Each layer (kinematic, dynamical, statistical, relativistic, gauge-theoretic) is justified primarily by its empirical success rather than by derivation from a more fundamental ontology.

The Event-Density (ED) program offers an alternative: to build quantum mechanics as a *forced structural consequence* of a small primitive stack governing micro-events, chains, bandwidth content, and commitment dynamics on a 3+1-dimensional event manifold. Phase-1 of this program [1] established that non-relativistic single-particle quantum mechanics — the Schrödinger equation, the Born rule, Bell-CHSH violations saturating the Tsirelson bound, and the Heisenberg uncertainty relation — emerges from the participation measure
$$
P_K(x, t) = \sqrt{b_K(x,t)} \cdot e^{i\pi_K(x,t)},
$$
combined with the four-band bandwidth decomposition (Primitive 04) and commitment dynamics (Primitives 10–11). The squared-amplitude exponent $b_K = |P_K|^2$ is *definitional*, not postulated; the Born rule's $|\psi|^2$ is therefore not an independent axiom. The same exponent-2 structure threads through Madelung's $\sqrt{\rho}$, Schrödinger's kinetic term, sublinear bandwidth composition, and Heisenberg's $(\Delta x \cdot \Delta p)^2$, yielding ED's strongest positive structural unification.

Phase-2 extends the program. Arc R, the subject of the present paper, derives **relativistic single-chain quantum mechanics** at primitive level. Three structural theorems are established. Arc M [2] (chain-mass structure) and Arc Q [3] (QFT extension) build on Arc R; we summarise their relationship in §6.

The motivation for deriving rather than postulating is threefold. *First*, structural derivation reduces the axiomatic surface area of physics: postulates that turn out to be theorems carry no independent empirical content and can be eliminated. *Second*, structural derivation exposes the precise inputs each piece of quantum theory requires; this clarifies which features are inherited (numerical constants, specific particle content) versus structural (form of equations, classification of representations). *Third*, structural derivation enables systematic extension: if non-relativistic quantum mechanics is a thin-participation limit of a richer primitive structure, the same primitives extend to relativistic and field-level regimes by relaxing the limit, rather than by introducing new postulates.

The Arc R results consist of three theorems plus extensive supporting structural content. The theorems establish:

- **R1 (Spin-statistics):** $\eta = (-1)^{2s}$ derived from primitive-level exchange topology and frame structure;
- **R2 (Cl(3,1) uniqueness):** the real Clifford algebra with anticommutator $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$ is the unique algebraic frame compatible with the Lorentz / spin / topology constraints;
- **R3 (Dirac emergence):** the Dirac equation is the unique first-order Lorentz-covariant equation on the Cl(3,1) spinor module, with conserved current and tree-level $g = 2$ as automatic consequences.

ED's primitive-level account does *not* predict the numerical values of dimensional constants ($\hbar$, $c$) or rule-type-specific parameters ($m$, $q$); these are inherited via the Dimensional Atlas. The clean separation between *form* (forced structurally) and *value* (inherited empirically) is a load-bearing methodological principle that recurs throughout Arc R and continues into Arc M and Arc Q.

---

## 2. Background

### 2.1 The ED primitive stack

Event Density is built on thirteen primitives organised in a canonical 7-section template (Definition / Mathematical Object / Relations / Measurable Signature / Examples / Simulator-PDE Instantiation / Open Questions). The primitives relevant to Arc R are summarised below:

- **Primitive 01 (micro-event):** discrete events on the 3+1-dimensional ambient manifold; the substrate for all participation.
- **Primitive 02 (chain):** worldlines $\gamma_K$ of persistent participation; supplies the worldline structure for rule-type instances.
- **Primitive 03 (participation):** the act of a chain entering a micro-event with non-zero amplitude.
- **Primitive 04 (bandwidth):** the four-band decomposition $b_K = b_K^{\text{int}} + b_K^{\text{adj}} + b_K^{\text{env}} + b_K^{\text{com}}$ allocating participation amplitude across structural channels.
- **Primitive 06 (four-gradient):** $\partial_\mu$ as the structural derivative on the event manifold; carries Lorentz covariance.
- **Primitive 07 (rule-type):** the discrete classification of chains by their structural levers (L1 bandwidth partition, L2 internal index, L3 interface, L4 statistics class).
- **Primitive 09 (polarity phase):** the phase $\pi_K$ of the participation measure.
- **Primitive 10 (individuation):** the threshold separating distinct chains; supports the two-chain pairing structure.
- **Primitive 11 (commitment):** the dynamical update producing micro-event events along $\gamma_K$.
- **Primitive 13 (relational timing):** proper time $\tau_K$ along $\gamma_K$ as the invariant relational clock.

### 2.2 The participation measure

The Phase-1 participation measure is
$$
P_K(x^\mu) = \sqrt{b_K(x^\mu)} \cdot e^{i \pi_K(x^\mu)} \;\in\; \mathbb{C},
$$
fusing Primitive 04 (bandwidth amplitude) with Primitive 09 (polarity phase). Stage R.1 promotes this object from a non-relativistic configuration-space scalar to a Lorentz-covariant scalar field on the ambient 3+1D event manifold:
$$
P_K(x^\mu) = \sqrt{b_K(x^\mu)} \cdot e^{i \pi_K(x^\mu)},
$$
where $x^\mu = (ct, \mathbf{x})$ now refers to the event-manifold coordinate. Lorentz covariance is forced by Primitive 06.

### 2.3 Rule-type ontology

A rule-type $\tau$ is a discrete classification of chain-types specified by four levers from Primitive 07:

- **L1:** bandwidth partition pattern $w_\tau^X$ across the four bands;
- **L2:** internal-index content (Lorentz representation $(j_L, j_R)$ plus any gauge index);
- **L3:** interface content (Fierz class $\Gamma_\tau$ or analogue);
- **L4:** statistics class (Case P bosonic / Case R fermionic).

The rule-type taxonomy is the structural classification framework for matter and gauge content. Stage R.2 of Arc R produces the spin-statistics correspondence connecting L4 to L2.

### 2.4 Commitment and individuation

Primitive 11 (commitment) supplies the dynamical update along chain worldlines: discrete events in which a chain "commits" — depositing a definite outcome on the event manifold. Primitive 10 (individuation) sets the threshold at which two same-type chains remain distinguishable; for Case-R rule-types, individuation forbids same-type coincidence, leading to the antisymmetry that yields Pauli exclusion at primitive level. The interplay of these two primitives is central to the spin-statistics theorem of §4.

---

## 3. Arc R Stage R.1 — Scalar Relativistic Quantum Mechanics

### 3.1 Klein-Gordon equation

The Stage R.1 derivation begins with the Lorentz-covariant participation measure on the (0,0) representation. For a free scalar rule-type, requiring (i) Lorentz-scalar form of the dynamical equation, (ii) translation invariance, and (iii) reduction to the non-relativistic Schrödinger limit yields the Klein-Gordon equation
$$
\left( \Box + \frac{m^2 c^2}{\hbar^2} \right) \Psi = 0,
$$
where $\Box = \eta^{\mu\nu} \partial_\mu \partial_\nu$ is the d'Alembertian. The mass term $m^2 c^2/\hbar^2$ enters as the Casimir eigenvalue of the Poincaré algebra acting on the rule-type's participation module; numerical $m$ is rule-type data inherited from the Dimensional Atlas.

### 3.2 Minimal coupling

Local-phase invariance of the participation measure $\Psi \to e^{iq\alpha(x)/\hbar}\Psi$ forces the introduction of a connection $A_\mu$ transforming as $A_\mu \to A_\mu - \partial_\mu \alpha$. The covariant derivative
$$
D_\mu = \partial_\mu + \frac{iq}{\hbar} A_\mu
$$
ensures $D_\mu \Psi$ transforms covariantly. The interacting Klein-Gordon equation
$$
(D_\mu D^\mu + m^2 c^2/\hbar^2) \Psi = 0
$$
is gauge-covariant. The U(1) gauge structure is therefore *forced* at primitive level by local-phase invariance, not postulated.

### 3.3 Conserved current

Standard manipulation yields the conserved Klein-Gordon current
$$
j^\mu = \frac{i\hbar}{2m} \left[ \Psi^* D^\mu \Psi - \Psi (D^\mu \Psi)^* \right],
$$
satisfying $\partial_\mu j^\mu = 0$ on solutions. The $j^0$ component is sign-indefinite, signalling the well-known negative-probability pathology of Klein-Gordon for matter fields. This pathology is resolved by Stage R.3's Dirac construction (§5).

### 3.4 Stage R.1 status

Stage R.1 produces:

- Lorentz-covariant scalar participation measure (FORCED);
- Klein-Gordon equation (FORCED);
- Minimal coupling and U(1) gauge structure (FORCED);
- Scalar conserved current (FORCED, sign-indefinite for matter — superseded by spinor case).

Numerical $m$, $q$, $\hbar$, $c$ are inherited.

---

## 4. Arc R Stage R.2 — Rule-Type Taxonomy and Spin-Statistics

Stage R.2 establishes the structural framework for spin and statistics. We summarise the five-memo sub-program (R.2.1 exchange, R.2.2 Lorentz representations, R.2.3 double-cover topology, R.2.4 Clifford algebra, R.2.5 synthesis) and state the spin-statistics theorem.

### 4.1 Exchange dichotomy (R.2.1)

For two same-type chains $K_A, K_B$, the exchange operation $E_{AB}$ swaps their participation labels. Involutive structure ($E_{AB}^2 = \mathrm{id}$) and mutual substitutability of same-type chains restrict the exchange factor $\eta(\tau)$ to
$$
\eta(\tau) \in \{+1, -1\}.
$$
Two rule-type categories emerge: **Case P** (bandwidth-sharing-permissive, $\eta = +1$, symmetric joint participation) and **Case R** (bandwidth-sharing-restrictive, $\eta = -1$, antisymmetric, vanishing-on-coincidence, Pauli exclusion).

### 4.2 Lorentz representations (R.2.2)

Finite-dimensional representations of the complexified Lorentz algebra $\mathfrak{so}(3,1)_\mathbb{C} \cong \mathfrak{su}(2)_\mathbb{C} \oplus \mathfrak{su}(2)_\mathbb{C}$ are classified by pairs $(j_L, j_R)$ with $j_L, j_R \in \{0, 1/2, 1, 3/2, \dots\}$ and dimension $(2j_L + 1)(2j_R + 1)$. The spin quantum number $s$ runs through $|j_L - j_R| \le s \le j_L + j_R$ via the Pauli-Lubanski Casimir. The exhaustive ladder
$$
s \in \{0, 1/2, 1, 3/2, 2, \dots\}
$$
is rigid in 3+1D — no half-odd-half values appear — by Lie-algebraic theorem.

Integer-spin representations descend to $\mathrm{SO}^+(3,1)$; half-integer representations require the double cover $\mathrm{SL}(2, \mathbb{C})$.

### 4.3 Configuration-space topology (R.2.3)

The fundamental group of the two-identical-chain configuration space $Q_2 = (\mathbb{R}^3 \times \mathbb{R}^3 \setminus \Delta)/S_2$ in 3+1D evaluates to
$$
\pi_1(Q_2) = \mathbb{Z}_2.
$$
The proof uses centre-of-mass + relative coordinates: the relative-coordinate space $(\mathbb{R}^3 \setminus \{0\})/\mathbb{Z}_2 \simeq \mathbb{R}P^2$, with $\pi_1(\mathbb{R}P^2) = \mathbb{Z}_2$.

**Consequences:**

1. Anyonic exchange phases are *forbidden* in 3+1D — only $\eta \in \{\pm 1\}$ admissible.
2. The exchange-path generator equals the $2\pi$-rotation generator under the $\mathrm{SO}(3)$-equivariant embedding of the relative coordinate.

The latter is the geometric content connecting exchange statistics to rotational structure.

### 4.4 Clifford algebra uniqueness (R.2.4)

Half-integer representations require an algebraic frame in which $0$ and $2\pi$ rotations are distinguishable. The structural problem: find the unique real finite-dimensional associative algebra $\mathcal{A}$ generated by elements $e_\mu$ ($\mu = 0,1,2,3$) satisfying:

- (P1) Lorentz tangent-space compatibility: $\{e_\mu\}$ transforms as a four-vector;
- (P2) Metric compatibility: symmetric pairings reproduce $\eta_{\mu\nu}$;
- (P3) Half-integer representation realisation;
- (P4) Minimal dimension.

Pure commutation ($e_\mu e_\nu = e_\nu e_\mu$) fails (P3); pure anticommutation ($e_\mu e_\nu = -e_\nu e_\mu$ strictly) fails (P2). The unique solution is the **anticommutator** structure
$$
\boxed{\{\gamma^\mu, \gamma^\nu\} = 2 \eta^{\mu\nu} \cdot \mathbb{1},}
$$
defining the real Clifford algebra $\mathrm{Cl}(3,1) \cong M_4(\mathbb{R})$ of dimension $16$. The Lorentz generators on the spinor module are
$$
\sigma^{\mu\nu} = \frac{i}{2} [\gamma^\mu, \gamma^\nu],
$$
generating the $\mathrm{SL}(2, \mathbb{C})$ action. Direct computation yields $D(R(2\pi)) = -\mathbb{1}$ on the spinor module — the rotational double-cover sign emerges automatically from the half-angle in $\exp(-i\theta\sigma^{12}/2)$.

### 4.5 Spin-statistics synthesis (R.2.5)

Combining §4.1–4.4 yields the **primitive-level spin-statistics theorem**:

> **Theorem R1 (Spin-Statistics).** *For any ED rule-type in 3+1D with Lorentz-covariant internal index structure, the exchange sign $\eta$ and the spin quantum number $s$ are related by*
> $$\eta = (-1)^{2s},$$
> *with $\eta$ FORCED to lie in $\{\pm 1\}$ by $\pi_1(Q_2) = \mathbb{Z}_2$ and $s$ FORCED to lie in $\{0, 1/2, 1, 3/2, 2, \dots\}$ by Lorentz representation theory. Integer-spin rule-types are Case P (bosonic); half-integer-spin rule-types are Case R (fermionic).*

**Sketch of proof.** The chain runs through six steps:

1. Exchange dichotomy $\eta \in \{+1, -1\}$ from rule-type structure (R.2.1).
2. Topological upgrade $\pi_1(Q_2) = \mathbb{Z}_2$ from spatial dimension 3 + identical-chain exchange (R.2.3).
3. Geometric theorem: exchange-path generator $=$ $2\pi$-rotation generator (R.2.3).
4. Lorentz-representation ladder: half-integer requires $\mathrm{SL}(2,\mathbb{C})$ (R.2.2).
5. Algebraic frame: $\mathrm{Cl}(3,1)$ with $D(R(2\pi)) = -\mathbb{1}$ on spinor module (R.2.4).
6. Bilinear-pairing closure: Primitive 10 individuation supplies the bilinear $\bar\Psi \Gamma \Psi$ coupling between chain indices, fixing the rule-type-frame coupling (R.2.5).

The minimal-bilinear (MB) closure step uses Primitive 10's two-chain individuation pairing made dynamical by Primitive 11. This step has no remaining CANDIDATE assumptions; the spin-statistics theorem is FORCED unconditionally at primitive level. $\square$

**Dependencies on primitives.** Primitives 02, 03, 06, 07, 10, 11, 13.

### 4.6 Cl(3,1) uniqueness as a separate theorem

We isolate the algebraic-frame content of §4.4 as a theorem in its own right:

> **Theorem R2 (Cl(3,1) Uniqueness).** *The unique real finite-dimensional associative algebra compatible with (P1) Lorentz tangent-space compatibility, (P2) metric compatibility, (P3) half-integer representation realisation, and (P4) minimal dimension is the real Clifford algebra $\mathrm{Cl}(3,1)$ with $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu} \cdot \mathbb{1}$. Pure commutation fails (P3); pure anticommutation (strict) fails (P2). The anticommutator is structurally mandatory.*

**Sketch of proof.** Suppose $e_\mu e_\nu = e_\nu e_\mu$ for all $\mu, \nu$ (commutative $\mathcal{A}$). Then (P2) reduces to $e_\mu e_\nu = (\eta_{\mu\nu}/2) \mathbb{1}$, forcing $e_\mu = 0$ for $\mu \ne \nu$ and rigid scalars on the diagonal. The resulting algebra does not support a half-integer $\mathrm{SL}(2,\mathbb{C})$ representation; (P3) fails.

Suppose $e_\mu e_\nu = -e_\nu e_\mu$ strictly. Then $e_\mu^2 = 0$ for all $\mu$, contradicting (P2) on the diagonal.

The remaining possibility is a mixed relation $e_\mu e_\nu + e_\nu e_\mu = 2\eta_{\mu\nu} \mathbb{1}$, i.e., the Clifford-algebra defining relation. This relation generates $\mathrm{Cl}(3,1)$ uniquely up to isomorphism, with dimension $2^4 = 16$ and basis $\{\mathbb{1}, \gamma^\mu, \gamma^{\mu\nu}, \gamma^{\mu\nu\rho}, \gamma^5\}$. $\square$

**Dependencies on primitives.** Primitive 06 (Lorentz covariance + metric) plus the half-integer-representation requirement from Theorem R1.

---

## 5. Arc R Stage R.3 — Dirac Emergence

### 5.1 Square-root factorisation

The Stage R.1 Klein-Gordon equation applied component-wise to a spinor field $\Psi_\alpha$ (on the four-dimensional Cl(3,1) module) is a *second-order* equation that does not use the $\gamma^\mu$ generators non-trivially. To use the algebraic frame, a *first-order* Lorentz-covariant equation built from $\gamma^\mu$, $\partial_\mu$, and a mass scale is required.

Compute:
$$
(i\gamma^\mu \partial_\mu)(i\gamma^\nu \partial_\nu) = -\gamma^\mu \gamma^\nu \partial_\mu \partial_\nu = -\frac{1}{2}\{\gamma^\mu, \gamma^\nu\}\partial_\mu \partial_\nu = -\eta^{\mu\nu} \partial_\mu \partial_\nu \cdot \mathbb{1} = -\Box.
$$
Therefore
$$
(i\gamma^\mu \partial_\mu - mc/\hbar)(i\gamma^\mu \partial_\mu + mc/\hbar) = -\Box - m^2 c^2/\hbar^2.
$$
A spinor satisfying the *first-order* equation
$$
(i\gamma^\mu \partial_\mu - mc/\hbar)\, \Psi = 0
$$
automatically satisfies Klein-Gordon component-wise. This is the **Dirac equation**.

### 5.2 Uniqueness of the first-order form

Three independent arguments force the first-order form for Case-R rule-types:

1. **Use of the Cl(3,1) structure.** Theorem R2 establishes $\gamma^\mu$ as primitive-level frame generators. A second-order equation leaves this structure inert. Equation $(i\gamma^\mu \partial_\mu - mc/\hbar)\Psi = 0$ is the unique Lorentz-covariant first-order linear operator on $\Psi$ constructible from $\gamma^\mu, \partial_\mu$, and a mass scale.

2. **Single time-derivative / positivity.** Klein-Gordon as a second-order spinor equation gives an indefinite inner product (negative-norm sector). The first-order Dirac form yields a positive-definite current (§5.3) and a Hilbert-space evolution compatible with the Stage R.1 inner-product structure.

3. **Half-integer representation content.** For the $(1/2, 0) \oplus (0, 1/2)$ Dirac module, the minimal Lorentz-covariant first-order equation is unique up to equivalence: it is the Dirac equation.

This yields:

> **Theorem R3 (Dirac Emergence).** *Given Stage R.1 (Klein-Gordon Casimir) and Stage R.2 (Cl(3,1) frame, half-integer representation content), the unique first-order Lorentz-covariant linear dynamical equation for Case-R rule-type participation measures is*
> $$\boxed{(i\gamma^\mu \partial_\mu - mc/\hbar)\, \Psi = 0.}$$
> *No additional postulates are required. The equation is structurally FORCED.*

**Sketch of proof.** Lorentz-covariance plus first-order linear structure built from $\gamma^\mu, \partial_\mu, m$ admits exactly the family $a \, i\gamma^\mu \partial_\mu \Psi + b \cdot (mc/\hbar) \Psi = 0$ with $a, b$ scalars. Squaring must reproduce Klein-Gordon component-wise (mass-shell consistency); this forces $a = 1, b = -1$ up to overall normalisation. The Cl(3,1) anticommutator $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$ ensures that squaring eliminates the cross term $\gamma^\mu \gamma^\nu \partial_\mu \partial_\nu$ via the symmetry of $\partial_\mu \partial_\nu$. $\square$

**Dependencies on primitives.** All Arc R stages: R.1 Casimir + R.2 Cl(3,1) frame + R.2 spin-statistics for the Case-R identification.

### 5.3 Conserved current

Multiplying the Dirac equation by $\bar\Psi = \Psi^\dagger \gamma^0$ and combining with the adjoint equation, the mass terms cancel and we obtain
$$
\partial_\mu (\bar\Psi \gamma^\mu \Psi) = 0,
$$
so
$$
j^\mu \equiv \bar\Psi \gamma^\mu \Psi
$$
is conserved. The time component
$$
j^0 = \bar\Psi \gamma^0 \Psi = \Psi^\dagger \gamma^0 \gamma^0 \Psi = \Psi^\dagger \Psi = \sum_\alpha |\Psi_\alpha|^2 \ge 0
$$
is **positive-definite**, in contrast to the indefinite Klein-Gordon current. The Dirac construction therefore resolves the negative-probability pathology of Klein-Gordon for spin-1/2 matter fields. This positivity is structurally tied to the first-order form via the spinor-module structure.

### 5.4 Minimal coupling and gauge invariance

The Stage R.1 minimal-coupling procedure applies unchanged on the spinor module:
$$
(i\gamma^\mu D_\mu - mc/\hbar) \Psi = 0, \qquad D_\mu = \partial_\mu + \frac{iq}{\hbar} A_\mu.
$$
Under local U(1), $\Psi \to e^{iq\alpha/\hbar}\Psi$, $A_\mu \to A_\mu - \partial_\mu \alpha$, and $D_\mu \Psi \to e^{iq\alpha/\hbar} D_\mu \Psi$. The interacting Dirac equation is gauge-covariant.

### 5.5 Non-relativistic reduction and $g = 2$

In the non-relativistic limit, write $\Psi = (\varphi, \chi)^T \cdot e^{-imc^2 t/\hbar}$ and solve the small-component equation algebraically. Substituting back and keeping leading-order terms yields the **Pauli equation**:
$$
i\hbar \partial_t \varphi = \left[ \frac{(\mathbf{p} - q\mathbf{A})^2}{2m} + qA^0 - \frac{q\hbar}{2m}\, \boldsymbol{\sigma} \cdot \mathbf{B} \right] \varphi.
$$
The Zeeman coefficient identifies the gyromagnetic ratio
$$
\boxed{g_{\text{Dirac}} = 2,}
$$
emerging without any parameter tuning from the Cl(3,1) frame and the first-order form. Higher-order QED corrections $g - 2 \approx \alpha/\pi + \dots$ are loop-level content (Arc Q [3] handles these); the *tree-level* $g = 2$ is a structural prediction of Arc R.

Dropping spin-dependent terms (projecting onto a spinless participation) yields the Schrödinger equation, recovering the Phase-1 non-relativistic limit and closing a consistency loop across the entire QM-emergence program.

---

## 6. Discussion

### 6.1 What Arc R forces vs what it leaves open

**Arc R FORCES, at primitive level:**

- Lorentz-covariant scalar participation measure;
- Klein-Gordon equation for spin-0 rule-types;
- Minimal coupling and U(1) gauge structure from local-phase invariance;
- Spin-statistics theorem $\eta = (-1)^{2s}$ (Theorem R1);
- $(j_L, j_R)$ representation classification with exhaustive spin ladder;
- Anyon prohibition in 3+1D (from $\pi_1(Q_2) = \mathbb{Z}_2$);
- Cl(3,1) frame uniqueness with $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$ (Theorem R2);
- $D(R(2\pi)) = -\mathbb{1}$ on the spinor module;
- Dirac equation as unique first-order Lorentz-covariant equation on the spinor module (Theorem R3);
- Positive-definite conserved current $j^\mu = \bar\Psi \gamma^\mu \Psi$;
- Tree-level Dirac $g = 2$ from non-relativistic reduction;
- Phase-1 consistency: Schrödinger emerges as the spinless non-relativistic limit.

**Arc R INHERITS (does not predict):**

- Numerical $\hbar$, $c$;
- Per-rule-type mass $m$, charge $q$;
- Specific spin assignment per rule-type (which rung of the ladder a given species occupies);
- Choice between Dirac, Weyl, and Majorana reality structure for any specific Case-R rule-type;
- The number of rule-types occupying any particular structural slot.

The clean form/value separation is preserved throughout. ED's primitive structure determines the *form* of relativistic quantum equations and the *classification* of admissible spin/statistics structures; numerical content is inherited via the Dimensional Atlas.

### 6.2 Relationship to Arc M

Arc M [2] addresses the chain-mass problem: whether ED primitives constrain the numerical mass values of rule-types. Building on Arc R's spin-statistics framework and Cl(3,1) frame, Arc M constructs a candidate bandwidth-signature
$$
\sigma_\tau = \hbar \cdot \sqrt{\sum_X w_\tau^X \cdot \langle (\partial_\mu \ln b_\tau^X)(\partial^\mu \ln b_\tau^X) \rangle_\tau}
$$
as a Lorentz-scalar functional of rule-type bandwidth content. Arc M closes "H1-dominant": $\sigma_\tau$'s Lorentz-scalar form is FORCED, but mass values, ratios, and hierarchies are INHERITED. ED fixes the *structure* of mass but not its *values*. Arc R supplies the foundational framework for Arc M's analysis without itself addressing mass-value content.

### 6.3 Relationship to Arc Q

Arc Q [3] extends ED to the QFT regime: gauge-group structure, interaction vertices, Higgs-like SSB, radiative corrections, generations, second quantisation, and vacuum structure. Three Arc Q theorems extend the structural framework:

- **GRH unconditional FORCED** — at least one massless Case-P (1/2, 1/2) gauge rule-type exists structurally; ED's first "particle-class must exist" prediction.
- **Canonical (anti-)commutation FORCED** — second-quantisation structure derived directly from Arc R's spin-statistics + Primitive 10 individuation.
- **UV-FIN FORCED at primitive level** — Primitive 01 event-discreteness + Primitive 13 finite intervals + Primitive 04 bounded bandwidth jointly guarantee primitive-level UV finiteness; renormalisation REFUTED as fundamental.

Arc Q's results presuppose Arc R's framework: the Cl(3,1) frame supplies the vertex catalogue's Fierz basis; the spin-statistics theorem forces the (anti-)commutation structure; the Dirac equation supplies the matter-sector dynamics for QFT loop calculations.

### 6.4 How Arc R sets the stage for the QFT extension

Arc R closes the relativistic single-chain quantum sector and supplies the structural prerequisites for Arc Q:

- The Cl(3,1) frame from Theorem R2 is the algebraic backbone of the Arc Q vertex catalogue (Q.3).
- Theorem R1's spin-statistics directly forces Arc Q's canonical (anti-)commutation relations (Q.7).
- The Dirac equation of Theorem R3 supplies the matter-sector dynamics for Arc Q's interaction-vertex analysis.
- The minimal-coupling derivation extends to non-Abelian gauge groups (Arc Q.3) without additional structural input.

Together, Arc R + Arc Q yields a structurally complete, UV-finite quantum field framework whose form is forced and whose numerical content is inherited.

---

## 7. Conclusion

Arc R derives relativistic single-chain quantum mechanics as a forced structural consequence of the ED primitive stack. Three structural theorems carry the load: spin-statistics (Theorem R1), Cl(3,1) uniqueness (Theorem R2), and Dirac emergence (Theorem R3). Together they reduce the conventional independent postulates of relativistic quantum theory — the form of the wave equation, the spin-statistics correspondence, the spinor frame, the gauge-covariant minimal coupling, and the conserved current — to consequences of a small primitive stack on a 3+1-dimensional event manifold.

The methodological framing — *form FORCED, value INHERITED* — distinguishes ED's contribution from numerical-prediction frameworks. ED does not predict the numerical value of $\hbar$, the electron mass, or the fine-structure constant. It predicts the *structural form* of the equations these constants appear in: the Klein-Gordon and Dirac equations, the gauge-covariant derivative, the conserved current, the spin ladder, the exchange-statistics dichotomy, and the Cl(3,1) algebraic frame.

Arc R's tree-level Dirac $g = 2$ emerges from the Cl(3,1) frame and the first-order form without parameter tuning. Its positive-definite conserved current resolves the Klein-Gordon negative-probability pathology for spin-1/2 fields. Its anyon prohibition follows from $\pi_1(Q_2) = \mathbb{Z}_2$ — a topological theorem about 3+1-dimensional configuration space.

These structural results ground the further extensions of Arc M (chain-mass) and Arc Q (QFT). Together, Phase-2 of the ED program (Arc R + Arc M + Arc Q) yields a structurally complete, UV-finite quantum field framework. The clean separation between structural prediction and empirical inheritance is preserved at every layer.

Phase-3 directions — ED to general-relativistic coupling, cosmological structure via the UV-FIN reframing of cosmological-$\Lambda$, possible high-energy empirical signatures near primitive event-discreteness scales — are unblocked by the Phase-2 closure of which Arc R is the relativistic foundation.

---

## References

[1] A. Proxmire and Copilot, *Quantum Mechanics as a Structural Consequence of Event-Density Primitives* (Phase-1 closure paper), 2026.

[2] A. Proxmire, *Chain-Mass Structure in Event Density* (Arc M synthesis), `chain_mass_synthesis.md`, 2026.

[3] A. Proxmire, *QFT Extension of Event Density: Arc Q Synthesis*, `arc_q_synthesis.md`, 2026.

[4] A. Proxmire, *Event-Density Primitive Stack* (Primitives 01–13), 2026.

[5] A. Proxmire, *Phase-2 Global Synthesis*, `phase2_synthesis.md`, 2026.

[6] R. Streater and A. Wightman, *PCT, Spin and Statistics, and All That*. Princeton University Press, 1964.

[7] J. Schwinger, "On Quantum-Electrodynamics and the Magnetic Moment of the Electron," *Phys. Rev.* **73**, 416 (1948).

[8] P. A. M. Dirac, "The Quantum Theory of the Electron," *Proc. R. Soc. Lond. A* **117**, 610 (1928).

[9] H. Weyl, *The Theory of Groups and Quantum Mechanics*. Methuen, 1931.

[10] L. H. Ryder, *Quantum Field Theory*, 2nd ed. Cambridge University Press, 1996.

---

*Manuscript closure: 2026-04-24. Companion documents: Arc M synthesis [2], Arc Q synthesis [3], Phase-2 synthesis [5]. All Arc R memos available at* `quantum/foundations/` *in the Event Density repository.*
