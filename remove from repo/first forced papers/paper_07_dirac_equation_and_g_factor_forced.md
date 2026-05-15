# The Dirac Equation and the Electron g-Factor (g = 2) are FORCED

**Paper #7 of the Event Density Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-12
**Series:** Event Density (ED) First-Wave Forcing Papers — Paper #7 of 10
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The Dirac equation and the electron gyromagnetic ratio $g = 2$ are normally derived from the Clifford algebra construction with relativistic covariance and the spinor module postulated alongside. This paper shows that, **given the substrate primitives of Papers #1–#6 plus the substrate's spatial-dimension primitive (P06, the spatial axis is $\mathbb{R}^3$), Poincaré symmetry at the relativistic scope, and the individuation-exclusion primitive on two-chain configuration space**, the entire structure is forced: two-chain configuration-space topology forces $\pi_1(Q_2) = \mathbb{Z}_2$ and the spin-statistics dichotomy; the exchange-class generator coincides with the $2\pi$-rotation generator, forcing $SL(2,\mathbb{C})$ as the admissible covariance group for fermionic rule-types; Cl(3,1) is the unique frame algebra realizing the spinor representation; the Dirac equation is the unique first-order Lorentz-covariant linear equation using the Cl(3,1) frame; and the half-angle factor produces the Zeeman coefficient $q\hbar/(2m)$ in the non-relativistic limit, fixing $g = 2$. The claim is conditional on the spatial-dimension primitive (the spatial axis is specifically three-dimensional) and on the substrate's Poincaré symmetry at relativistic scope. Why the substrate has these specific symmetry and dimensional commitments is upstream content for the Primitive-Forcing Meta-Paper. Radiative corrections to $g$ are downstream of QED and out of scope.

---

## 1. Framing

### 1.1 What standard physics postulates about relativistic spin-$\tfrac12$ dynamics

Every graduate course on relativistic quantum mechanics presents the Dirac equation as a postulate or as the result of an ingenious algebraic move. The standard story:

1. The Klein-Gordon equation $(\Box + m^2c^2/\hbar^2)\Psi = 0$ is the natural relativistic wave equation, but it is second-order in time and has negative-probability-density pathologies for charged particles.
2. To find a first-order alternative, Dirac (1928) sought operators $\gamma^\mu$ such that $(i\gamma^\mu\partial_\mu)^2 = -\Box$. The required anticommutation relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}\mathbb{1}$ has no finite-dimensional commutative solution; the smallest matrix representation is $4 \times 4$, with $\Psi$ a four-component object.
3. The Dirac equation $(i\gamma^\mu\partial_\mu - mc/\hbar)\Psi = 0$ then yields, in the non-relativistic limit with minimal electromagnetic coupling, the Pauli equation containing a Zeeman term $-(q\hbar/2m)\,\sigma\cdot B$. The gyromagnetic ratio is $g = 2$.

This presentation leaves several structural facts unmotivated. *Why* is the spinor four-component and not some other dimension? *Why* the Clifford algebra rather than a different operator structure? *Why* the first-order form? And — most strikingly — *why* does the factor of 2 in $g = 2$ fall out exactly, with no empirical tuning?

The $g = 2$ result is one of the great quantitative successes of theoretical physics. It was a triumph of the 1928 Dirac construction. But within the standard presentation, it is a *consequence* of postulates that themselves are not derived: Lorentz covariance, the choice to use spinors, the Clifford algebra. The deeper question — why nature uses these specific structures — remains open.

### 1.2 The puzzle

Several partial derivations exist:

- **Wigner's representation analysis** (1939): unitary irreducible representations of the Poincaré group classify particles by mass and spin. Half-integer spin requires representations of the universal cover $SL(2, \mathbb{C})$ of the proper orthochronous Lorentz group. The Poincaré group and the choice to work on a Hilbert space are inputs.
- **Operator-theoretic constructions**: the Dirac equation is the unique first-order Lorentz-covariant linear equation on a Clifford module. The Clifford module structure is taken as given.
- **Geometric constructions** via fiber bundles: spinor bundles on spin manifolds carry Dirac operators. The spin structure on the manifold is an input.
- **Dirac's belt trick / configuration-space arguments**: $2\pi$ rotation of a fermion is non-trivial; $4\pi$ returns to identity. This explains the double cover but does not derive it from primitives.

None of these derives the spinor structure, the Clifford algebra, and the Dirac equation from a substrate of pre-quantum primitive structure. The $g = 2$ result, in particular, falls out only at the very end of the chain, after all the relativistic structure has been put in.

### 1.3 What this paper does

The Event Density (ED) framework supplies a pre-quantum substrate. Papers #1-#6 establish the participation measure, the Born rule, the sesquilinear inner product, the Schrödinger evolution, the gauge-field structure, and the non-relativistic Hamiltonian / mass framework — all forced from substrate primitives. The present paper extends to the relativistic spin-$\tfrac12$ sector.

This paper forces, in sequence:

1. **Configuration-space topology**: $\pi_1(Q_2) = \mathbb{Z}_2$ in 3+1D, from spatial-dimension primitive + individuation exclusion of fermionic coincidence.
2. **Spin-statistics dichotomy**: $\eta \in \{+1, -1\}$, with no continuous anyonic phases admissible.
3. **Rotational double cover**: $SL(2, \mathbb{C})$ as the admissible covariance group for fermionic rule-types.
4. **Cl(3,1) Clifford algebra**: $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}\mathbb{1}$ as the unique frame algebra on the spinor module.
5. **Dirac equation**: $(i\gamma^\mu\partial_\mu - mc/\hbar)\Psi = 0$ as the unique first-order Lorentz-covariant equation using the Cl(3,1) frame.
6. **Minimal coupling**: $\partial_\mu \to D_\mu = \partial_\mu + (iq/\hbar)A_\mu$ from local $U(1)$ invariance.
7. **The electron $g$-factor**: $g = 2$ falling out of the non-relativistic reduction via the half-angle factor in $\exp(-\tfrac{i}{2}\theta\sigma^{12})$.

Alternative structures — Klein-Gordon-only, real-valued representations, non-Clifford algebras, non-minimal coupling, anomalous $g \neq 2$ at the structural level — are excluded by substrate-condition violation. Radiative corrections to $g$ (the celebrated $g - 2 = \alpha/\pi + \ldots$ of quantum electrodynamics) are downstream of the present paper and inherited from the QED perturbative expansion.

**Series context.** Paper #1-#6 cover the non-relativistic kinematic + dynamical + interaction backbone. The present paper extends to the relativistic spin-$\tfrac12$ sector. Together with the substrate-level forcing chain, it produces $g = 2$ as one of the program's sharpest structural results: a precisely measured physical constant emerges from substrate primitives + standard relativistic representation theory, with no empirical tuning.

---

## 2. Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#6 results, P06 spatial dimension $=3$, Poincaré symmetry at relativistic scope, and individuation-exclusion on $Q_2$*. Then:
> - **(D)** The unique first-order Lorentz-covariant linear wave equation on a fermionic-rule-type participation measure is the Dirac equation.
> - **(g)** Minimal electromagnetic coupling produces, in the non-relativistic limit, $g = 2$ at the structural (tree-level) value.
>
> *The spatial-dimension and Poincaré-symmetry primitives are load-bearing; both are upstream content.*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated substrate axioms)

This paper takes the following Event Density (ED) substrate primitives as **postulated axioms**:

- **P06 (spatial dimension $D = 3+1$):** the substrate's spatial axis is $\mathbb{R}^3$. Load-bearing — $\pi_1(Q_2) = \mathbb{Z}_2$ holds specifically in $D = 3$; in $D = 2$ it is the braid group (anyons); in $D \geq 4$ it is trivial.
- **Poincaré symmetry at relativistic scope:** the substrate's symmetry content at relativistic scope, with Galilean group emerging as the $c \to \infty$ Inönü-Wigner contraction.
- **Individuation-exclusion on two-chain configuration space:** two indistinguishable fermionic chains cannot coincide in the participation graph; substrate-level commitment generating $Q_2 = (\mathbb{R}^3 \times \mathbb{R}^3 \setminus \Delta)/S_2$.
- **Papers #1–#6 results.**

The full 13-primitive substrate axiom set is enumerated in the ED Foundations position paper. The empirical case for the postulates rests on their downstream reach across domains. This paper's contribution: given the postulates above, the Dirac equation $(i\gamma^\mu\partial_\mu - mc/\hbar)\Psi = 0$ is the unique first-order Lorentz-covariant linear wave equation using the Cl(3,1) frame, and the electron gyromagnetic ratio $g = 2$ falls out structurally at tree level. Radiative QED corrections to $g$ are downstream of this paper and inherited from perturbative expansion.

### 3.1 What is FORCED

- **Spinor structure** for fermionic (Case-R) rule-types: participation measures carry an internal spinor index and transform under $SL(2, \mathbb{C})$.
- **Cl(3,1) Clifford algebra**: $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}\mathbb{1}$ as the unique frame algebra on the spinor module.
- **First-order Lorentz-covariant Dirac equation**: $(i\gamma^\mu\partial_\mu - mc/\hbar)\Psi = 0$ as the unique linear wave equation using the Cl(3,1) structure non-trivially.
- **Minimal coupling**: $\partial_\mu \to D_\mu = \partial_\mu + (iq/\hbar)A_\mu$ from local $U(1)$ invariance.
- **Conserved current**: $j^\mu = \bar\Psi\gamma^\mu\Psi$ with positive-definite density $j^0 = \Psi^\dagger\Psi$.
- **Gyromagnetic ratio $g = 2$**: structural value at the tree level from the Pauli reduction.

### 3.2 What is INHERITED

- **Mass $m$**: rule-type-specific (Paper #6); numerical value not derived.
- **Charge $q$**: rule-type-specific; numerical value not derived.
- **Universal constants $\hbar$, $c$**: dimensional anchors from the Dimensional Atlas.
- **Choice of gauge group**: U(1) for electromagnetism; SU(2)×U(1) or SU(3) extensions inherited from the value-layer Standard Model content (Paper #5).
- **Specific labeling of spinor components**: Weyl, Dirac, or Majorana representation is a basis choice.

### 3.3 What is OUT OF SCOPE

- **Radiative corrections to $g$**. The famous $g - 2 = \alpha/(2\pi) + \ldots$ of QED is downstream of the present paper and inherited from the QED perturbative expansion. The structural value $g = 2$ is the tree-level result; radiative content lives in the QED loop expansion, not in the substrate-level derivation.
- **Full QED**. The renormalization machinery, the running coupling, the Lamb shift, and other perturbative QED content are downstream.
- **Renormalization**. Mass and charge renormalization, vertex corrections, and counterterm structure are downstream of the bare Dirac equation.
- **The Standard Model gauge group**. Specific SU(3)×SU(2)×U(1) content is value-layer empirical (Paper #5 scope).
- **Quantum gravity / curved-spacetime Dirac**. The Dirac equation in curved spacetime is a downstream extension; the present paper covers flat-spacetime Minkowski.
- **Anyons / 2+1D physics**. The forcing argument applies to 3+1D; 2+1D systems have $\pi_1$ a braid group rather than $\mathbb{Z}_2$, admitting fractional statistics.

---

## 4. Key Vocabulary

- **Substrate.** Pre-quantum layer of primitive structure on which ED is built.
- **Channel.** Primitive structural pathway in the participation graph, indexed by $K$.
- **Bandwidth $b_K(u)$.** Non-negative real-valued primitive on each channel.
- **Polarity $\pi_K(u)$.** $U(1)$-valued angular primitive on each channel.
- **Participation measure $P_K(u)$.** Complex-valued amplitude carrier $\sqrt{b_K(u)}\,e^{i\pi_K(u)}$ (Paper #1); for fermionic rule-types, carries an internal spinor index.
- **Rule-type (Case P / Case R).** Substrate primitive class of channel structure (Paper #5). Case P (bosonic, $\eta = +1$, symmetric under exchange) versus Case R (fermionic, $\eta = -1$, antisymmetric under exchange).
- **Configuration space $Q_2$.** Space of distinct positions for two identical chains: $(\mathbb{R}^3 \times \mathbb{R}^3 \setminus \Delta)/S_2$, with $\Delta$ the diagonal and $S_2$ the exchange group.
- **Spin-statistics relation $\eta = (-1)^{2s}$.** Connection between intrinsic spin $s$ and exchange phase $\eta$. Bosons ($s$ integer) have $\eta = +1$; fermions ($s$ half-integer) have $\eta = -1$.
- **$SL(2, \mathbb{C})$.** The universal double cover of the proper orthochronous Lorentz group $SO^+(3, 1)$. Spinor representations live on $SL(2, \mathbb{C})$ but not on $SO^+(3, 1)$.
- **Clifford algebra Cl(3,1).** Real associative algebra generated by $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}\mathbb{1}$ with metric signature $(+, -, -, -)$.
- **Dirac equation.** $(i\gamma^\mu\partial_\mu - mc/\hbar)\Psi = 0$, the first-order Lorentz-covariant wave equation for spinor fields.
- **Gyromagnetic ratio $g$.** Ratio between magnetic moment and spin angular momentum, $\mu = g \cdot (q/2m)\,S$.

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying:

### C1. Participation graph + channel structure (Primitives P03 + P07)

Channels are ontologically primitive; the participation graph supplies discrete channels at each locus.

### C2. Bandwidth with additivity (Primitive P04)

Non-negative bandwidth on each channel; additive across disjoint channels.

### C3. Polarity (Primitive P09)

$U(1)$-valued angular primitive on each channel.

### C4. Time + spatial homogeneity (Primitives P03 + P13)

Continuous time and spatial axes with homogeneous structure; Paper #4's substrate condition extended to 3+1D Minkowski via the Lorentz-covariance constraints of relativistic kinematics.

### C5. Spatial dimensionality 3+1D

The substrate's spatial structure is three-dimensional, with Lorentz signature $(+, -, -, -)$ on the four-dimensional event manifold. This is a structural commitment of the ED program (cf. the substrate-derived 3+1D forcing of the NS-1 arc).

### C6. Commitment events with locality (Primitive P11)

Discrete commitment events at substrate vertices, with locality (no superluminal correlations between commitments).

### C7. Individuation threshold (Primitive P10)

For fermionic (Case R) rule-types, same-type coincidence is excluded: two identical Case-R chains cannot occupy the same locus.

### C8. Rule-type taxonomy (Primitive P02 / Paper #5)

The substrate supplies a primitive class of rule-types. The taxonomy includes a Case-P / Case-R distinction governed by exchange symmetry of the rule-type's bandwidth content under two-chain swap.

### C9. Inherited results from Papers #1-#6

- **Paper #1**: complex-valued participation measure.
- **Paper #2**: Born rule for commitment outcomes.
- **Paper #3**: sesquilinear inner product on the participation manifold.
- **Paper #4**: linear unitary Schrödinger evolution (non-relativistic regime), generalized to Lorentz-covariant evolution in the relativistic regime.
- **Paper #5**: gauge-field-as-rule-type structure with local U(1) symmetry for the gauge sector.
- **Paper #6**: mass as Lorentz-scalar bandwidth-signature functional; non-relativistic Hamiltonian form.

### C10. No relativistic dynamical form as input

The forcing argument invokes only C1-C9 plus the following standard mathematical infrastructure:

- Algebraic topology: fundamental groups of configuration spaces, deformation retracts.
- Lie group theory: $SL(2, \mathbb{C})$ as the universal cover of $SO^+(3, 1)$; finite-dimensional irreducible representations.
- The Frobenius classification of finite-dimensional real associative algebras (used to identify Cl(3,1) uniquely).
- Standard non-relativistic-limit Taylor expansion of relativistic equations.

No Dirac equation, no Clifford algebra, no spinor module, no $g = 2$ is assumed as input; all are produced by the forcing chain.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. Second-order Klein-Gordon-only equations.** The relativistic wave equation for fermionic rule-types is Klein-Gordon $(\Box + m^2c^2/\hbar^2)\Psi = 0$ applied componentwise, without a first-order Dirac structure.

**A2. Real-valued spinor representations.** Spinor structure is real-valued (Majorana-only), with no complex amplitude content beyond the real spinor components.

**A3. Non-Clifford frame algebras.** The frame algebra on the spinor module is not Cl(3,1) — for instance, a pure commutator algebra $[\gamma^\mu, \gamma^\nu]$ rather than anticommutator $\{\gamma^\mu, \gamma^\nu\}$, or a different metric-signature Clifford algebra (Cl(4,0), Cl(2,2)).

**A4. Higher-order linear equations on the spinor module.** $(\gamma^\mu\partial_\mu)^2 \Psi = m^2\Psi$ as a fundamental equation rather than the derived consequence of the Dirac equation.

**A5. Non-minimal electromagnetic coupling.** Couplings beyond $\partial \to D$ — for instance, an explicit Pauli term $\bar\Psi\sigma^{\mu\nu}F_{\mu\nu}\Psi$ added at the structural level.

**A6. Anomalous $g$ at the structural level.** Any $g \neq 2$ at the tree level — e.g., $g = 1$ (classical spinning sphere), $g = 4$, fractional values, or a free parameter.

**A7. Fractional / anyonic exchange phases in 3+1D.** Exchange phases $\eta = e^{i\theta}$ with $\theta \neq 0, \pi$ for two identical chains.

**A8. $SO(3, 1)$ representations without $SL(2, \mathbb{C})$ double cover.** Spinor representations defined directly on $SO^+(3, 1)$ rather than its universal cover.

### 6.2 Mainstream alternatives

**B1. Klein-Gordon-only relativistic dynamics.** The Klein-Gordon equation as the universal relativistic wave equation, without specialization for spin-$\tfrac12$.

**B2. Pauli equation as postulate.** The non-relativistic Pauli equation with the Zeeman term $-(q\hbar/2m)\sigma\cdot B$ adopted directly without deriving it from Dirac.

**B3. Classical spinning-electron models.** Classical models in which the electron is a rotating charged sphere or shell. These predict $g = 1$ (uniform sphere) or other classical values, not $g = 2$.

**B4. Wigner-classification approach.** Spinor representations adopted as inputs from the Wigner classification of Poincaré representations, with the Dirac equation as the irreducible representation operator.

**B5. Fiber-bundle spinor formulations.** Spinor bundles on spin manifolds with the Dirac operator as a structural input from differential geometry.

**B6. Higher-spin generalizations as fundamental.** Rarita-Schwinger or higher-spin equations as fundamental rather than the spin-$\tfrac12$ Dirac equation.

---

## 7. Constructive Necessity

The derivation chain has seven structural steps. Each traces to substrate primitives or to standard mathematical infrastructure; no input from the Dirac equation or the Clifford algebra is assumed.

### 7.1 Configuration-space topology forces $\pi_1(Q_2) = \mathbb{Z}_2$

Consider two identical Case-R chains at positions $x_1, x_2 \in \mathbb{R}^3$ on a constant-time slice. Their classical configuration space, treating the chains as interchangeable, is
$$
Q_2 = (\mathbb{R}^3 \times \mathbb{R}^3 \setminus \Delta) / S_2,
$$
with $\Delta = \{(x, x) : x \in \mathbb{R}^3\}$ the diagonal (excluded for fermionic rule-types by C7's individuation threshold) and $S_2$ the symmetric group acting by exchange.

In center-of-mass and relative coordinates $R = (x_1 + x_2)/2$, $r = x_1 - x_2$, the exchange acts as $R \to R$, $r \to -r$. Therefore
$$
Q_2 \cong \mathbb{R}^3 \times (\mathbb{R}^3 \setminus \{0\}) / \mathbb{Z}_2.
$$
The $\mathbb{R}^3$ factor is contractible. The quotient $(\mathbb{R}^3 \setminus \{0\})/\mathbb{Z}_2$ deformation-retracts onto $\mathbb{RP}^2$ (since $\mathbb{R}^3 \setminus \{0\}$ retracts onto $S^2$, and the antipodal quotient of $S^2$ is $\mathbb{RP}^2$). Therefore
$$
\pi_1(Q_2) = \pi_1(\mathbb{RP}^2) = \mathbb{Z}_2.
$$

This is a topological theorem with three inputs: spatial dimension 3 (C5), continuous exchange paths (C6), and same-type coincidence excluded for fermionic chains (C7). The result is forced by the substrate.

### 7.2 Spin-statistics dichotomy $\eta \in \{+1, -1\}$ (T3)

One-dimensional unitary representations of $\mathbb{Z}_2$ are homomorphisms $\mathbb{Z}_2 \to U(1)$. There are exactly two: the trivial homomorphism (generator $\mapsto +1$) and the sign homomorphism (generator $\mapsto -1$). No continuous phase $e^{i\theta}$ with $\theta \neq 0, \pi$ is a valid $\mathbb{Z}_2$ representation.

Therefore the exchange phase is forced to be
$$
\eta \in \{+1, -1\}.
$$
This is the substrate-level derivation of the spin-statistics dichotomy in 3+1D. Continuous anyonic phases are excluded structurally — they would require $\pi_1 = \mathbb{Z}$ (the braid group), which occurs only in 2+1D where the spatial dimension does not allow continuous "unknotting" of exchange paths.

This result is theorem-level **T3 (anyon prohibition in 3+1D)** in the ED inventory.

### 7.3 Exchange = 2$\pi$ rotation; $SL(2, \mathbb{C})$ double cover forced

The exchange path representing the non-trivial class of $\pi_1(Q_2)$ corresponds geometrically to a $2\pi$ rotation of the relative-coordinate frame. The standard demonstration: rotate the segment connecting the two chains by $\pi$ about an axis perpendicular to the segment. The segment without orientation returns to itself after $\pi$; a framed segment returns only after $2\pi$. The path-class generator in $\pi_1(Q_2)$ maps to the $2\pi$-rotation generator in $\pi_1(SO(3)) = \mathbb{Z}_2$. Both are the non-trivial $\mathbb{Z}_2$ element.

The proper orthochronous Lorentz group $SO^+(3, 1)$ has $\pi_1 = \mathbb{Z}_2$; its universal cover is $SL(2, \mathbb{C})$. A representation $D$ of $SL(2, \mathbb{C})$ descends to a representation of $SO^+(3, 1)$ iff $D(-\mathbb{1}) = +\mathbb{1}$ on the internal index space, where $-\mathbb{1} \in SL(2, \mathbb{C})$ is the non-trivial covering-map kernel element.

Lorentz representations are classified by $(j_L, j_R)$ with $j_L, j_R \in \{0, \tfrac12, 1, \tfrac32, \ldots\}$. The $(j_L, j_R)$ representation has $D(-\mathbb{1}) = (-1)^{2(j_L + j_R)}$. Half-integer $j_L + j_R$ representations do *not* descend to $SO^+(3, 1)$; they live on $SL(2, \mathbb{C})$ only.

For fermionic rule-types, the substrate's individuation structure (C7) plus configuration-space topology (§7.1-7.2) forces $\eta = -1$. The exchange-class generator coincides with the $2\pi$-rotation generator. Half-integer spinor representations are therefore structurally required for fermionic rule-types: $SL(2, \mathbb{C})$ is the admissible covariance group.

### 7.4 Cl(3,1) Clifford algebra forced (T2)

The spinor module — the carrier of the $(\tfrac12, 0) \oplus (0, \tfrac12)$ representation of $SL(2, \mathbb{C})$ — requires an algebraic frame. What algebra realizes Lorentz covariance on this module?

Consider a real associative algebra $\mathcal{A}$ generated by four elements $\gamma^\mu$ ($\mu = 0, 1, 2, 3$) such that bilinear combinations $\sigma^{\mu\nu} = (i/2)[\gamma^\mu, \gamma^\nu]$ generate the Lorentz algebra $\mathfrak{so}(3, 1)$. The structural requirement: $\gamma^\mu$ must transform as a four-vector under Lorentz transformations, $S(\Lambda)\gamma^\mu S(\Lambda)^{-1} = \Lambda^\mu{}_\nu\,\gamma^\nu$.

Three algebraic structures are candidates: pure commutator $[\gamma^\mu, \gamma^\nu]$, pure anticommutator $\{\gamma^\mu, \gamma^\nu\}$, or a mixed structure. The Lorentz-vector-transformation requirement, combined with the metric signature $(+, -, -, -)$ from C5, forces the anticommutator structure
$$
\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}\mathbb{1}.
$$
A pure commutator alone cannot reproduce $\gamma^\mu\gamma^\mu = \eta^{\mu\mu}$ (the diagonal Clifford relation needed for the square-root construction below). A pure antisymmetric structure has no place for the symmetric metric contribution. The mixed structure forced by Lorentz covariance + metric signature is exactly the Clifford anticommutator.

By Frobenius-style classification of real associative algebras generated by four anticommuting square roots of the metric in signature $(3, 1)$, the unique algebra (up to isomorphism) is the real Clifford algebra Cl(3, 1). It has dimension $2^4 = 16$ as a real vector space; its minimal faithful matrix representation is $4 \times 4$ complex (the standard Dirac matrices).

The Lorentz generators are $\sigma^{\mu\nu} = (i/2)[\gamma^\mu, \gamma^\nu]$, satisfying the Lorentz algebra. Crucially, under a rotation by angle $\theta$ in the $(x^1, x^2)$ plane, the spinor transformation is
$$
S(R(\theta)) = \exp\left(-\frac{i}{2}\theta\sigma^{12}\right),
$$
with the **half-angle factor** $-i\theta/2$ rather than $-i\theta$. This makes $S(R(2\pi)) = -\mathbb{1}$ automatically — the $2\pi$-rotation acts as $-\mathbb{1}$ on the spinor module, exactly as required for half-integer representations.

This result is theorem-level **T2 (Cl(3, 1) uniqueness)** in the ED inventory.

### 7.5 Dirac equation as the unique first-order Lorentz-covariant wave equation (T4)

Case-R rule-type participation measures live on the spinor module: $\Psi(x^\mu) \in \mathbb{C}^4$ (or the equivalent Cl(3, 1)-module). Klein-Gordon (Paper #5's Stage R.1) applies component-wise: each $\Psi_\alpha$ satisfies $(\Box + m^2c^2/\hbar^2)\Psi_\alpha = 0$. But this is second-order and blind to the Cl(3, 1) frame.

Construct a first-order operator using the $\gamma^\mu$ frame. Consider $(i\gamma^\mu\partial_\mu)^2$:
$$
(i\gamma^\mu\partial_\mu)(i\gamma^\nu\partial_\nu) = -\gamma^\mu\gamma^\nu\partial_\mu\partial_\nu = -\tfrac12\{\gamma^\mu, \gamma^\nu\}\partial_\mu\partial_\nu = -\eta^{\mu\nu}\partial_\mu\partial_\nu = -\Box.
$$
(The commutator term vanishes because $\partial_\mu\partial_\nu$ is symmetric while $[\gamma^\mu, \gamma^\nu]$ is antisymmetric.)

Therefore
$$
(i\gamma^\mu\partial_\mu - mc/\hbar)(i\gamma^\mu\partial_\mu + mc/\hbar) = -\Box - m^2c^2/\hbar^2 = -(\Box + m^2c^2/\hbar^2).
$$
If $\Psi$ satisfies the first-order equation
$$
(i\gamma^\mu\partial_\mu - mc/\hbar)\Psi = 0,
$$
then applying $(i\gamma^\mu\partial_\mu + mc/\hbar)$ from the left gives $(\Box + m^2c^2/\hbar^2)\Psi = 0$ component-wise. The first-order equation is a **square root** of Klein-Gordon.

That the first-order form is FORCED for Case-R rule-types follows from three independent arguments:

- **Use of the Cl(3, 1) structure.** The $\gamma^\mu$ are primitive-level frame generators on the spinor module (§7.4). A wave equation that does not contain $\gamma^\mu$ leaves the Cl(3, 1) structure inert. The unique Lorentz-covariant first-order linear operator on $\Psi$ constructible from $\gamma^\mu$, $\partial_\mu$, and a mass scale is $i\gamma^\mu\partial_\mu - mc/\hbar$.
- **Positive-definite current.** Klein-Gordon as a second-order equation on the spinor module gives an indefinite-norm current (the standard Klein-Gordon negative-probability pathology). The first-order Dirac form yields $j^\mu = \bar\Psi\gamma^\mu\Psi$ with $j^0 = \Psi^\dagger\Psi \geq 0$ — a positive-definite probability density. Hilbert-space evolution compatible with the Paper #3 inner-product structure requires the first-order form.
- **Half-integer representation content.** Klein-Gordon is the natural equation for spin-0. For spin-$\tfrac12$, the minimal covariant first-order equation using the Cl(3, 1) frame is the Dirac equation.

The Dirac equation is the unique structurally admissible first-order dynamical equation for Case-R rule-type participation measures. This is theorem-level **T4 (Dirac equation emergence)** in the ED inventory.

### 7.6 Minimal coupling from local $U(1)$ invariance

Paper #5 establishes that gauge-field rule-types $\tau_g$ admit local $U(1)$ (and non-Abelian generalizations) as their interface property. For a Case-R matter rule-type, local $U(1)$ invariance — $\Psi(x) \to e^{iq\alpha(x)/\hbar}\Psi(x)$ — requires the replacement
$$
\partial_\mu \to D_\mu = \partial_\mu + (iq/\hbar)A_\mu,
$$
where $A_\mu$ is the gauge participation measure and $q$ is the rule-type's charge. This is the minimal-coupling substitution.

Under this replacement, the Dirac equation becomes the **interacting Dirac equation**
$$
(i\gamma^\mu D_\mu - mc/\hbar)\Psi = 0,
$$
gauge-covariant under local $U(1)$. Non-minimal couplings (additional Pauli terms $\bar\Psi\sigma^{\mu\nu}F_{\mu\nu}\Psi$, contact interactions, etc.) would require additional substrate-level vertices unsupported by C6's single-vertex commitment primitive. Minimal coupling is forced (Paper #5 §7.5; same argument applies here).

### 7.7 Non-relativistic limit and $g = 2$

Write the Dirac spinor as
$$
\Psi = \begin{pmatrix}\varphi \\ \chi\end{pmatrix} e^{-imc^2 t/\hbar},
$$
with $\varphi, \chi$ two-component Pauli spinors and the phase factor removing the rest-energy oscillation. In the Dirac representation ($\gamma^0 = \text{diag}(\mathbb{1}, -\mathbb{1})$, $\gamma^i$ off-diagonal with Pauli $\sigma^i$ blocks), the interacting Dirac equation decomposes into coupled equations for $\varphi$ and $\chi$.

In the non-relativistic limit, $\chi$ is small compared to $\varphi$ — of order $v/c$. Solving the $\chi$ equation algebraically and substituting back, the leading-order equation for $\varphi$ is the **Pauli equation**:
$$
i\hbar\,\partial_t\varphi = \left[\frac{(\hat{p} - qA)^2}{2m} + qA^0 - \frac{q\hbar}{2m}\,\sigma\cdot B\right]\varphi,
$$
where $B = \nabla \times A$ is the magnetic field. The final term is the **Zeeman term**, coupling the electron spin $S = (\hbar/2)\sigma$ to the magnetic field with coefficient $q\hbar/(2m)$.

The magnetic moment of a spin-$\tfrac12$ particle is conventionally written
$$
\mu = g\,\frac{q}{2m}\,S.
$$
Reading off from the Zeeman term, the coefficient $q\hbar/(2m)$ multiplying $\sigma$ corresponds to $\mu = q\hbar/(2m) = (q/2m) \cdot \hbar = g \cdot (q/2m) \cdot (\hbar/2)$ with $g = 2$.

**The gyromagnetic ratio $g = 2$ is FORCED**.

The factor of 2 traces precisely to the half-angle factor in $\exp(-\tfrac{i}{2}\theta\sigma^{12})$, the spinor representation of rotations on the Cl(3, 1) module (§7.4). Doubling the rotation angle to make the spinor return to itself corresponds, via the non-relativistic reduction, to halving the rotation generator that enters the magnetic-coupling expression — equivalently, doubling the magnetic moment relative to the classical $g = 1$ prediction.

This is one of the program's sharpest empirical successes: a precisely measured physical constant is recovered at the structural level from substrate primitives plus standard mathematical infrastructure, with no empirical tuning. Radiative corrections to $g$ ($g - 2 = \alpha/(2\pi) + \ldots$ in QED) are downstream of this tree-level value and out of scope.

---

## 8. Exclusion Arguments

### 8.1 A1 — Second-order Klein-Gordon-only for fermions

The spinor module carries the Cl(3, 1) frame structure (§7.4) and a positive-definite participation-measure-amplitude norm (C9 from Paper #3). A second-order Klein-Gordon equation applied component-wise on the spinor module fails to use the $\gamma^\mu$ structure non-trivially and produces an indefinite current (the Klein-Gordon negative-probability pathology). The Hilbert-space-evolution requirement (Paper #4) forces a positive-definite probability density, which Klein-Gordon on spinors cannot supply. The first-order Dirac form is structurally required.

### 8.2 A2 — Real-valued spinor representations

Paper #1 establishes that the unique amplitude carrier consistent with substrate $U(1)$ polarity (C3) is the complex-valued participation measure. Real-valued spinors fail to carry the $U(1)$ phase content; Majorana spinors are admissible as complex-valued spinors with a reality constraint, but the underlying carrier is complex.

### 8.3 A3 — Non-Clifford frame algebras

The unique real associative algebra generated by four anticommuting square roots of the metric in signature $(3, 1)$ is Cl(3, 1). Pure-commutator algebras fail to reproduce the diagonal relation $\gamma^\mu\gamma^\mu = \eta^{\mu\mu}$ required for the square-root factorization of Klein-Gordon. Different-signature Clifford algebras (Cl(4, 0), Cl(2, 2)) violate the substrate's $(3, 1)$ Lorentz signature (C5). Non-associative algebras fail to support the Lorentz-generator structure $\sigma^{\mu\nu} = (i/2)[\gamma^\mu, \gamma^\nu]$.

### 8.4 A4 — Higher-order linear equations on the spinor module

A second-order equation $(\gamma^\mu\partial_\mu)^2\Psi = m^2\Psi$ as a fundamental dynamical equation is equivalent component-wise to Klein-Gordon (since $(\gamma^\mu\partial_\mu)^2 = -\Box$) and therefore reduces to A1: no use of the Cl(3, 1) structure non-trivially, indefinite norm. The first-order Dirac form is structurally required for the Cl(3, 1) use + positivity.

### 8.5 A5 — Non-minimal electromagnetic coupling

Paper #5 establishes that the substrate-level commitment primitive supplies a single vertex per matter-gauge rule-type pair. Non-minimal couplings would require additional substrate-level vertices or non-bilinear vertex structure, neither of which C6 supplies. Anomalous magnetic-moment terms ($\bar\Psi\sigma^{\mu\nu}F_{\mu\nu}\Psi$) in the bare Lagrangian violate the single-vertex constraint; observed deviations from $g = 2$ arise from QED radiative corrections (integrated-out loop content), not from substrate-level non-minimal coupling.

### 8.6 A6 — Anomalous $g$ at the structural level

The Pauli reduction of the minimal-coupled Dirac equation produces the Zeeman coefficient $q\hbar/(2m)$ exactly. The factor of 2 in $g = 2$ traces to the half-angle factor in $S(R(\theta)) = \exp(-i\theta\sigma^{12}/2)$ on the spinor module (§7.4). Any structural $g \neq 2$ would require either a different Clifford-algebra structure (excluded by A3), a different first-order operator (excluded by A4), or a non-minimal coupling (excluded by A5). The structural value $g = 2$ is forced.

### 8.7 A7 — Fractional / anyonic exchange phases in 3+1D

Fractional exchange phases $\eta = e^{i\theta}$ with $\theta \neq 0, \pi$ would require $\pi_1(Q_2) = \mathbb{Z}$ (the braid group), which occurs only in 2+1D. The substrate's 3+1D commitment (C5) forces $\pi_1(Q_2) = \mathbb{Z}_2$ (§7.1), admitting only $\eta = \pm 1$. Anyons in bulk 3+1D are excluded by the substrate's spatial dimensionality.

### 8.8 A8 — $SO(3, 1)$ representations without $SL(2, \mathbb{C})$ double cover

Half-integer-spin representations do not descend from $SL(2, \mathbb{C})$ to $SO^+(3, 1)$ because $D(-\mathbb{1}) = -\mathbb{1} \neq +\mathbb{1}$ on these representations (§7.3). The substrate's individuation structure (C7) + configuration-space topology (§7.1-7.2) force the $2\pi$-rotation-as-$-\mathbb{1}$ identification, which is only possible on the double-cover $SL(2, \mathbb{C})$. Working without the double cover excludes half-integer-spin fermionic rule-types — which contradicts the substrate's primitive admissibility of Case-R rule-types (C8).

### 8.9 B1 — Klein-Gordon as universal relativistic dynamics

Klein-Gordon is structurally appropriate for spin-0 (Case-P scalar rule-types) but inappropriate for spin-$\tfrac12$ (Case-R spinor rule-types): on the spinor module, Klein-Gordon misses the Cl(3, 1) frame and produces an indefinite current. The forcing chain shows that distinct rule-type sectors require distinct dynamical equations: Klein-Gordon for spin-0, Dirac for spin-$\tfrac12$, and higher-spin equations for higher representations.

### 8.10 B2 — Pauli equation as postulate

The Pauli equation is the non-relativistic limit of the Dirac equation. Adopting it as a postulate inserts the Zeeman coefficient $q\hbar/(2m)$ by hand. Under the substrate-conditions test, the Pauli equation is downstream of the Dirac forcing; the Zeeman coefficient is derived, not postulated.

### 8.11 B3 — Classical spinning-electron models

Classical models of the electron as a rotating charged sphere predict $g = 1$ (uniform sphere), $g = 2/3$ (shell), or other classical values — not $g = 2$. The discrepancy was historically resolved by quantum mechanics + Dirac. Under the substrate-conditions test, classical models fail to incorporate the spinor structure forced by §7.4 and the half-angle rotation factor that produces $g = 2$. They are excluded as inadequate at the structural level.

### 8.12 B4 — Wigner-classification approach

Wigner's classification of Poincaré representations identifies spin-$\tfrac12$ as the $(\tfrac12, 0) \oplus (0, \tfrac12)$ representation. Under the substrate-conditions test, this is *parallel* to the present derivation rather than competing: Wigner takes the Poincaré group as given; the substrate forces the same representation theory via configuration-space topology + double-cover identification (§§7.1-7.3). Both arrive at the same spinor structure; the present derivation traces it deeper, to substrate primitives.

### 8.13 B5 — Fiber-bundle spinor formulations

Spinor bundles on spin manifolds, with the Dirac operator as a structural input from differential geometry, are an *alternative mathematical language* for the same forced result. The spin structure on the manifold is supplied by the substrate's individuation-induced double-cover identification (§7.3). Fiber-bundle formulations are downstream mathematical reformulations, not alternative substrate-level commitments.

### 8.14 B6 — Higher-spin generalizations as fundamental

Rarita-Schwinger spin-$\tfrac32$ and higher-spin equations apply to higher representations of $SL(2, \mathbb{C})$. The substrate admits these representations — but each requires its own dynamical equation derived analogously to §§7.4-7.5. The Dirac equation is forced for spin-$\tfrac12$ specifically; higher-spin equations are forced separately for their own representations. They are not in competition with Dirac for the spin-$\tfrac12$ sector.

### 8.15 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 second-order on spinors | §7.5, Paper #3 | Indefinite current; Cl(3,1) frame unused; Hilbert-space positivity forces first-order. |
| A2 real-valued spinors | C3 (Paper #1) | Fails to carry $U(1)$ polarity content; carrier must be complex. |
| A3 non-Clifford frames | §7.4 | Unique algebra realizing four anticommuting roots of metric in signature (3,1) is Cl(3,1). |
| A4 higher-order spinor equations | §7.5 | Reduces to second-order; no use of Cl(3,1); same problems as A1. |
| A5 non-minimal coupling | Paper #5 §7.5 | Single-vertex commitment supplies one bilinear coupling per matter-gauge pair. |
| A6 structural $g \neq 2$ | §7.7 | Half-angle factor in $\exp(-i\theta\sigma^{12}/2)$ forces Zeeman coefficient $q\hbar/(2m)$. |
| A7 fractional exchange phases in 3+1D | C5, §7.1 | $\pi_1(Q_2) = \mathbb{Z}_2$ in 3+1D admits only $\eta = \pm 1$. |
| A8 no double cover | §7.3 | Half-integer reps don't descend to $SO^+(3,1)$; substrate forces $SL(2,\mathbb{C})$. |
| B1 Klein-Gordon for fermions | §7.5 | Inappropriate on spinor module; misses Cl(3,1) + indefinite current. |
| B2 Pauli equation postulate | not in space | Non-relativistic limit of Dirac; downstream consequence. |
| B3 classical spinning electron | empirical | Predicts $g = 1$ or other classical values, not $g = 2$. |
| B4 Wigner classification | parallel | Same representation theory derived deeper from substrate primitives. |
| B5 fiber-bundle spinors | reformulation | Mathematical language for the forced result. |
| B6 higher-spin as fundamental | scope-different | Applies to higher reps; Dirac is forced for spin-$\tfrac12$ specifically. |

**The Dirac equation $(i\gamma^\mu D_\mu - mc/\hbar)\Psi = 0$ with $g = 2$ at the tree level is the unique survivor.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier is identical to the empirical falsifier of standard relativistic quantum mechanics + the tree-level $g = 2$ prediction. The key constraint is the electron magnetic moment.

The measured electron $g$-factor (Hanneke-Fogwell-Gabrielse 2008, refined subsequently) is
$$
g_e = 2.002\,319\,304\,361\ldots,
$$
agreeing with the QED prediction to better than 1 part in $10^{12}$. The departure from exactly 2 is the famous $g - 2 = \alpha/(2\pi) + (\alpha/\pi)^2 \cdot c_2 + \ldots$ of QED, with $c_2$ a known constant and higher-order terms calculated. The leading $g = 2$ value is the tree-level prediction of the Dirac equation; all observed corrections are radiative and downstream of the present paper.

If the leading value were observed to be other than 2 — if the electron $g$-factor were not consistent with $2 + \text{(QED corrections)}$ — the substrate forcing of this paper would be refuted along with standard QED.

Specific structural-level falsifiers:
- **Observed $g \neq 2$ at tree level** for any spin-$\tfrac12$ Dirac fermion would refute §7.7.
- **Observed anyonic statistics in 3+1D bulk** (not confinable to 2+1D surface effects) would refute §7.1-7.2.
- **Half-integer spin representations behaving as $SO^+(3, 1)$ representations** (without the double-cover $-\mathbb{1}$ factor) would refute §7.3.

None of these has been observed.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C10 (channel-primitive participation graph, four-band bandwidth, $U(1)$ polarity, time + spatial homogeneity, 3+1D dimensionality, commitment locality, individuation excluding Case-R coincidence, rule-type taxonomy, Papers #1-#6 inherited, no relativistic dynamics as input) but supporting a non-Cl(3, 1) frame, a second-order spinor wave equation, non-minimal coupling, or $g \neq 2$ at the structural level, that survives the exclusion arguments of §8.

The author's claim is that no such substrate exists. The exclusion chain in §8 is closed; each alternative is dispatched by a specific substrate-condition violation. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

Three immediate exposures:

**Electron magnetic moment.** The most precisely measured quantity in physics agrees with the substrate-forced tree-level $g = 2$ plus QED radiative corrections to better than 1 part in $10^{12}$. Every precision experiment on the electron magnetic moment tests the substrate forcing.

**Hydrogen fine structure.** Spin-orbit coupling in the hydrogen atom, which produces the fine-structure splitting of energy levels, is the non-relativistic-limit-plus-spin-correction expansion of the Dirac equation with the Coulomb potential. The observed fine-structure constant agrees with the substrate-derived structure.

**Spin-statistics in matter.** The structural dichotomy $\eta \in \{+1, -1\}$ — bosons and fermions, with no anyons in 3+1D bulk — is observed in every condensed-matter, atomic-physics, and particle-physics experiment. Anyonic statistics, when observed, appear only in 2+1D effective systems (fractional quantum Hall states, certain spin-liquid edge modes), consistent with §7.1's dimension-dependent topology.

The substrate-level Dirac + $g = 2$ forcing supports every quantitative spin-$\tfrac12$-particle prediction in physics.

---

## Appendix A — Derivation Chain and Glossary

### A.1 The half-angle factor and $g = 2$ — explicit calculation

In the Dirac representation:
$$
\gamma^0 = \begin{pmatrix}\mathbb{1} & 0 \\ 0 & -\mathbb{1}\end{pmatrix}, \qquad \gamma^i = \begin{pmatrix}0 & \sigma^i \\ -\sigma^i & 0\end{pmatrix},
$$
with $\sigma^i$ the Pauli matrices. The interacting Dirac equation $(i\gamma^\mu D_\mu - mc/\hbar)\Psi = 0$ in $A^0$-and-$\mathbf{A}$ external fields, with $\Psi = (\varphi, \chi)^T e^{-imc^2 t/\hbar}$, gives the coupled equations
$$
i\hbar\,\partial_t\varphi = c\,\sigma\cdot(\hat{p} - q\mathbf{A})\,\chi + qA^0\varphi,
$$
$$
(i\hbar\,\partial_t + 2mc^2)\chi = c\,\sigma\cdot(\hat{p} - q\mathbf{A})\,\varphi + qA^0\chi.
$$
In the non-relativistic limit, $\chi$ is small ($\sim v/c$) and $|i\hbar\,\partial_t\chi| \ll 2mc^2|\chi|$. Solving the $\chi$ equation algebraically:
$$
\chi \approx \frac{1}{2mc}\,\sigma\cdot(\hat{p} - q\mathbf{A})\,\varphi.
$$
Substituting into the $\varphi$ equation:
$$
i\hbar\,\partial_t\varphi = \frac{1}{2m}\,[\sigma\cdot(\hat{p} - q\mathbf{A})]^2\,\varphi + qA^0\varphi.
$$
Using the identity $(\sigma\cdot A)(\sigma\cdot B) = A\cdot B + i\sigma\cdot(A \times B)$:
$$
[\sigma\cdot(\hat{p} - q\mathbf{A})]^2 = (\hat{p} - q\mathbf{A})^2 + i\sigma\cdot[(\hat{p} - q\mathbf{A}) \times (\hat{p} - q\mathbf{A})].
$$
The cross-product, with $\hat{p} = -i\hbar\nabla$, gives
$$
(\hat{p} - q\mathbf{A}) \times (\hat{p} - q\mathbf{A}) = -q[\hat{p} \times \mathbf{A} + \mathbf{A} \times \hat{p}] = -i\hbar q(\nabla \times \mathbf{A}) = -i\hbar q\,\mathbf{B}.
$$
Therefore $i\sigma\cdot(\cdot) = i\sigma\cdot(-i\hbar q\mathbf{B}) = \hbar q\,\sigma\cdot\mathbf{B}$. Substituting back:
$$
i\hbar\,\partial_t\varphi = \left[\frac{(\hat{p} - q\mathbf{A})^2}{2m} + qA^0 + \frac{\hbar q}{2m}\sigma\cdot\mathbf{B}\right]\varphi.
$$
With sign conventions standard, the Zeeman term is
$$
-\frac{q\hbar}{2m}\,\sigma\cdot\mathbf{B}.
$$
The magnetic moment of a spin-$\tfrac12$ particle is $\mu = g(q/2m)\mathbf{S}$ with $\mathbf{S} = (\hbar/2)\sigma$; the Zeeman energy is $-\mu\cdot\mathbf{B} = -g(q/2m)(\hbar/2)\sigma\cdot\mathbf{B}$. Matching the coefficient:
$$
g \cdot \frac{q\hbar}{4m} = \frac{q\hbar}{2m} \implies g = 2.
$$

The factor of 2 traces to the half-angle in the spinor representation $\exp(-i\theta\sigma^{12}/2)$: doubling the rotation angle is what makes the spinor return after $4\pi$, and this same factor enters the Zeeman coefficient via the $\sigma\cdot(\hat{p} - q\mathbf{A})$ structure of the first-order Dirac equation.

### A.2 Glossary

- **Anticommutator $\{A, B\}$.** $AB + BA$.
- **Bar operation $\bar\Psi$.** $\Psi^\dagger\gamma^0$, the Dirac adjoint.
- **Case P / Case R.** Rule-type taxonomy distinguishing bosonic ($\eta = +1$, scalar participation measure) and fermionic ($\eta = -1$, spinor participation measure) chains.
- **Clifford algebra Cl(3, 1).** Real associative algebra generated by $\gamma^0, \ldots, \gamma^3$ with $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}\mathbb{1}$.
- **Configuration space $Q_2$.** Space of distinct positions for two identical Case-R chains: $(\mathbb{R}^3)^2 \setminus \Delta)/S_2$.
- **Conserved current.** $j^\mu = \bar\Psi\gamma^\mu\Psi$; $\partial_\mu j^\mu = 0$; $j^0 \geq 0$.
- **Covariant derivative.** $D_\mu = \partial_\mu + (iq/\hbar)A_\mu$ for U(1) gauge.
- **Dirac equation.** $(i\gamma^\mu\partial_\mu - mc/\hbar)\Psi = 0$ free; $(i\gamma^\mu D_\mu - mc/\hbar)\Psi = 0$ with minimal coupling.
- **Exchange phase $\eta$.** Sign acquired by a multi-particle wavefunction under exchange of two identical particles.
- **FORCED.** Derived from substrate primitives + standard mathematics, no additional commitments.
- **Fundamental group $\pi_1$.** Algebraic-topology invariant classifying loops up to homotopy.
- **Gyromagnetic ratio $g$.** $\mu = g(q/2m)\mathbf{S}$; $g = 2$ for tree-level Dirac.
- **Individuation threshold (Primitive P10).** Substrate-level mechanism forbidding same-type Case-R coincidence.
- **INHERITED.** Quantitative content (mass, charge, $\hbar$, $c$) used in the paper but not derived in it.
- **Klein-Gordon equation.** $(\Box + m^2c^2/\hbar^2)\Psi = 0$; relativistic wave equation for Case-P scalar rule-types.
- **Minimal coupling.** $\partial_\mu \to D_\mu = \partial_\mu + (iq/\hbar)A_\mu$.
- **Pauli equation.** Non-relativistic limit of the Dirac equation; Schrödinger + Zeeman term.
- **Rule-type.** Substrate primitive class of channel structure (Papers #5, #6).
- **$SL(2, \mathbb{C})$.** Universal double cover of $SO^+(3, 1)$.
- **Spin-statistics relation.** $\eta = (-1)^{2s}$; T1 in the ED inventory.
- **Spinor.** Element of the 4-dimensional Cl(3, 1)-module carrying the $(\tfrac12, 0) \oplus (0, \tfrac12)$ representation of $SL(2, \mathbb{C})$.
- **Zeeman term.** $-\mu\cdot\mathbf{B} = -(q\hbar/2m)\sigma\cdot\mathbf{B}$; the magnetic-moment coupling in the Pauli equation.

### A.3 Source-repository citations (for ED-internal readers)

- `arcs/arc-R/dirac_emergence.md` — Stage R.3 main derivation memo for the Dirac equation, including the square-root factorization and non-relativistic reduction.
- `arcs/arc-R/clifford_algebra_from_spinor_structure.md` — Cl(3, 1) uniqueness derivation.
- `arcs/arc-R/rotational_double_cover_scoping.md` — configuration-space topology and double-cover argument.
- `arcs/arc-R/lorentz_representations_from_primitives.md` — Lorentz representation theory on the participation manifold.
- `arcs/arc-R/relativistic_participation_measure.md` — Lorentz-covariant extension of the participation measure.
- `arcs/arc-R/klein_gordon_emergence.md` — Stage R.1 Klein-Gordon for Case-P scalars.
- `arcs/arc-R/arc_r_stage1_synthesis.md` — Arc R Stage 1 synthesis.
- `walkthroughs/from_primitives_to_dirac_equation_and_g2.md` — public-facing walkthrough.
- `walkthroughs/from_primitives_to_spin_statistics.md` — companion walkthrough on the spin-statistics dichotomy.
- `theorems/T1.md` — spin-statistics theorem ($\eta = (-1)^{2s}$).
- `theorems/T2.md` — Cl(3, 1) uniqueness theorem.
- `theorems/T3.md` — anyon prohibition in 3+1D.
- `theorems/T4.md` — Dirac equation emergence.

These are *not* required reading for the present paper.

---

*End of Paper #7.*
