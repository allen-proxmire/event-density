# Mass, Inertia, and the Hamiltonian Structure are FORCED

**Paper #6 of the Event Density Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-12
**Series:** Event Density (ED) First-Wave Forcing Papers — Paper #6 of 10
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The non-relativistic Hamiltonian $\hat{H} = \hat{p}^2/(2m) + V(\hat{x})$ — quadratic kinetic operator, factor of $1/(2m)$, additive potential — together with the appearance of inertial mass as a Lorentz-scalar parameter, is normally a postulate. This paper shows that, **given the substrate primitives of Papers #1–#4 plus the Galilean Lie algebra acting on the participation manifold and the four-band partition (P04 §1.5)**, the entire structure is forced: the kinetic-plus-potential decomposition follows from translation invariance plus locality; the quadratic dependence on $\hat{p}$ follows from rotational invariance plus the non-relativistic-limit scope; the factor of $1/(2m)$ falls out of the Galilean commutator $[\hat{H}, \hat{K}] = -i\hbar\hat{p}$ as the integration Jacobian; and mass appears structurally as a Lorentz-scalar bandwidth-signature functional $\sigma_\tau$ with units of energy. Numerical mass values, mass ratios, and generation counts are inherited from the value layer. The claim is conditional: the Galilean symmetry structure is treated here as a property of the substrate's primitive symmetry content rather than as a derived result. Why the substrate carries Galilean symmetry at the non-relativistic scope (and Poincaré at the relativistic scope) is upstream content for the Primitive-Forcing Meta-Paper.

---

## 1. Framing

### 1.1 What standard physics postulates about mass, inertia, and the Hamiltonian

Every undergraduate textbook on classical and quantum mechanics presents the Hamiltonian and inertial mass as a list of structural facts:

1. **Kinetic energy is quadratic in momentum.** $T = p^2/(2m)$ in classical mechanics, $\hat{T} = \hat{p}^2/(2m)$ as an operator in quantum mechanics. The exponent is exactly 2, the coefficient is exactly $1/(2m)$.
2. **The Hamiltonian decomposes as kinetic plus potential.** $\hat{H} = \hat{T}(\hat{p}) + V(\hat{x})$, with $\hat{T}$ depending only on momentum and $V$ only on position. No position-momentum cross terms appear in the free-particle or simple-potential Hamiltonian.
3. **Inertial mass appears as a Lorentz/Galilean scalar.** A single real parameter $m > 0$ per particle, independent of position, velocity, or direction (in the non-relativistic regime).
4. **$F = ma$ in classical mechanics.** Acceleration is proportional to applied force, with the inverse-mass coefficient determining the system's inertial response.

The standard presentation states these together as a single postulate ("the system is described by a Hamiltonian function of canonical position and momentum variables, with kinetic energy quadratic in momentum and inertial mass a positive scalar parameter"). Where each fact comes from — why quadratic rather than quartic, why $1/(2m)$ rather than $1/m$ or $1/m^2$, why inertia is isotropic, why mass appears at all in the dynamical equations — is not derived in standard mechanics. The Hamiltonian formalism is part of the package.

### 1.2 The puzzle

Several attempts to motivate the Hamiltonian structure from deeper principles exist:

- **Lagrangian / variational approach**: the Hamiltonian is the Legendre transform of a Lagrangian; the Lagrangian's form is typically motivated by analogy with classical wave mechanics or by demanding specific symmetry properties. Symmetry is the input.
- **Wigner's analysis of Galilean symmetry**: in the non-relativistic regime, the unitary representations of the Galilean group on a complex Hilbert space have a specific structure that constrains the Hamiltonian. The Galilean group and the Hilbert space are both inputs.
- **Mach's principle**: inertia is interpreted as a structural feature of the cosmological matter distribution. Specific implementations vary; the original principle does not derive the Hamiltonian's quadratic form.
- **Higgs mechanism**: in the Standard Model, fundamental fermion masses arise from coupling to the Higgs field. This is downstream content — the Higgs field, its potential, and its coupling structure are all inputs, and the mechanism produces specific mass values rather than the structural form of mass itself.

None of these programs derives the Hamiltonian structure plus the appearance of inertial mass from a pre-quantum substrate of primitive structure. The deeper question — why the world has a quadratic-in-$\hat{p}$ kinetic operator, a Lorentz-scalar mass parameter, and the additive kinetic-plus-potential decomposition — remains.

### 1.3 What this paper does

The Event Density (ED) framework supplies a pre-quantum substrate. Papers #1-#4 establish the participation measure, the Born rule, the sesquilinear inner product on the participation manifold, and the Schrödinger evolution equation $i\hbar\,\partial_t P = \hat{H} P$ with $\hat{H}$ a self-adjoint generator. Paper #4 establishes the existence and uniqueness of $\hat{H}$ via Stone's theorem applied to time-translation symmetry; the *form* of $\hat{H}$ is the content of the present paper.

This paper forces:

1. **The kinetic-plus-potential decomposition** $\hat{H} = \hat{T}(\hat{p}) + V(\hat{x})$, with $\hat{T}$ depending only on momentum and $V$ only on position.
2. **The quadratic kinetic structure** $\hat{T}(\hat{p}) = f(|\hat{p}|^2)$ for some scalar function $f$.
3. **The specific coefficient $1/(2m)$**, with the factor of 2 forced as the Galilean-Lie-algebra integration Jacobian.
4. **Mass as a Lorentz-scalar bandwidth-signature functional** $\sigma_\tau$ with units of energy, structurally forced by the substrate's four-band decomposition + Lorentz-scalar requirement.

Alternative structures — non-quadratic kinetic terms, anisotropic mass, position-momentum cross terms, mass as a fundamental (non-substrate-derived) parameter, MOND-class modified inertia — are each excluded by substrate-condition violation. Numerical mass values, mass ratios, and the absence of forced generation counts are inherited from the value layer.

**Series context.** Paper #1 forced the amplitude carrier. Paper #2 forced the probability rule. Paper #3 forced the inner product and the Tsirelson ceiling. Paper #4 forced the existence of a unique self-adjoint Hamiltonian generator. Paper #5 forced the gauge-field structure. The present paper forces the specific form of the Hamiltonian and the structural origin of inertial mass. Together, Papers #1-#6 cover the kinematic + dynamical + interaction backbone of non-relativistic gauge-coupled quantum mechanics.

---

## 2. Claim

> **Forcing Theorem (Conditional on Substrate Primitives).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#4 results, Galilean symmetry of the participation manifold, four-band partition (P04 §1.5)*. Then the self-adjoint Hamiltonian generator of Paper #4 is uniquely (up to inherited numerical values) the operator
> $$
> \hat{H} = \frac{\hbar^2\,|\hat{p}|^2}{2m} + V(\hat{x}),
> $$
> with mass $m$ appearing as a Lorentz-scalar bandwidth-signature functional.
>
> *Galilean symmetry of the participation manifold is treated as a property of the substrate's primitive symmetry content (load-bearing input). Why the substrate has this symmetry is upstream content.*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated substrate axioms)

This paper takes the following Event Density (ED) substrate primitives as **postulated axioms**:

- **Galilean Lie algebra (with Bargmann central extension) acting on the participation manifold:** the substrate's symmetry content at non-relativistic scope, including the $[\hat{H}, \hat{K}_i] = -i\hbar\hat{p}_i$ commutator and mass as central element.
- **P04 §1.5 (four-band partition):** the substrate-level orthogonal decomposition of bandwidth used for the Lorentz-scalar bandwidth-signature mass identification.
- **Locality of $\hat{H}$ as a constraint on substrate-level dynamics:** the Hamiltonian acts locally on the participation graph.
- **Papers #1–#4 results.**

The full 13-primitive substrate axiom set is enumerated in the ED Foundations position paper. The empirical case for the postulates rests on their downstream reach across domains. This paper's contribution: given the postulates above, $\hat{H} = \hat{p}^2/(2m) + V(\hat{x})$ is the unique non-relativistic Hamiltonian form, with mass appearing structurally as a Lorentz-scalar bandwidth-signature functional. Numerical mass values, mass ratios, and generation counts are inherited from the value layer.

### 3.1 What is FORCED

- The **kinetic-plus-potential decomposition** $\hat{H} = \hat{T}(\hat{p}) + V(\hat{x})$. No position-momentum cross terms in the gauge-coupling-free regime.
- The **quadratic-in-$|\hat{p}|^2$** structure of $\hat{T}$. Higher-even-power terms suppressed by the non-relativistic-limit scope; linear-in-$|\hat{p}|$ excluded.
- The **factor of $1/(2m)$** in the kinetic operator, with the factor of 2 derived as the Galilean integration Jacobian.
- **Isotropy** of the kinetic operator: $\hat{T}$ is a scalar function of $|\hat{p}|^2$, not direction-dependent.
- **Mass as a Lorentz-scalar bandwidth-signature functional** $\sigma_\tau$ on the substrate's four-band content, with units of energy via $\hbar \times$ frequency, and $m_\tau = \sigma_\tau/c^2$ as the structural identification.
- **Form-fixing of dynamical mass terms** in the Klein-Gordon and Dirac equations (where relativistic): $m^2 c^2/\hbar^2$ in KG, $mc/\hbar$ in Dirac.

### 3.2 What is INHERITED

- **Numerical value of mass $m$** for each rule-type. Inherited from value-layer / empirical input. Arc M's H1-dominant verdict: numerical mass content is rule-type data, not derived from primitives.
- **Mass ratios** across rule-types. No primitive-level mechanism forces $m_e/m_p$, $m_t/m_b$, etc.
- **Mass hierarchies and generation counts**. Three generations of fermions is not forced; specific orderings $m_t \gg m_b \gg m_c$ are not forced.
- **The value of $\hbar$**. Inherited via the dimensional-atlas Madelung anchoring.
- **The Higgs mechanism**, if relevant. ED's substrate-level mass-structure result is upstream of the Higgs sector; specific Higgs content is value-layer empirical.

### 3.3 What is OUT OF SCOPE

- This paper does **not** derive relativistic dynamics. The full Lorentz-covariant Dirac and Klein-Gordon mass terms are downstream content (Arc R).
- This paper does **not** derive gauge couplings. Gauge-coupled Hamiltonians $\hat{H} = \hat{T}(\hat{p} - eA/c) + V(\hat{x}) + \cdots$ are downstream of Paper #5; the present paper covers the gauge-coupling-free regime.
- This paper does **not** derive gravity. Gravitational mass-energy coupling is downstream content (substrate-gravity arc).
- This paper does **not** address mass renormalization or running mass in QFT. The substrate-level mass-structure result is upstream of perturbative field-theoretic corrections.
- This paper does **not** address the Higgs mechanism or the origin of specific Standard Model masses. The H1-dominant verdict explicitly inherits these from the value layer.

---

## 4. Key Vocabulary

For the reader new to Event Density:

- **Substrate.** Pre-quantum layer of primitive structure on which the ED framework is built.
- **Channel.** Primitive structural pathway in the participation graph, indexed by $K$.
- **Participation bandwidth $b_K(u)$.** Non-negative real-valued primitive quantity on each channel.
- **Polarity $\pi_K(u)$.** $U(1)$-valued angular primitive on each channel.
- **Participation measure $P_K(u)$.** Complex-valued amplitude carrier $\sqrt{b_K(u)}\,e^{i\pi_K(u)}$ (Paper #1).
- **Four-band decomposition.** Substrate-level structural decomposition of bandwidth into four mutually orthogonal bands: **internal**, **adjacency**, **environmental**, and **commitment-reserve** (Primitive 04 §1.5).
- **Bandwidth-signature functional $\sigma_\tau$.** A Lorentz-scalar functional of a rule-type's four-band content, identified with mass via $m_\tau = \sigma_\tau/c^2$.
- **Galilean Lie algebra.** The Lie algebra of the Galilean group — the symmetry group of inertial observers in non-relativistic kinematics. Generators: time translations $\hat{H}$, spatial translations $\hat{p}$, boosts $\hat{K}_i = m\hat{x}_i - t\hat{p}_i$, rotations.
- **Boost generator $\hat{K}_i$.** The Galilean generator of velocity boosts in the $i$-direction. Satisfies $[\hat{H}, \hat{K}_i] = -i\hbar\hat{p}_i$ — the commutator relation that fixes the kinetic operator.
- **Rule-type.** Substrate primitive class of channel structure; matter and gauge are distinct rule-types (Paper #5).

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying:

### C1. Participation graph + channel structure (Primitives P03 + P07)

Channels are ontologically primitive; the participation graph supplies discrete channels at each locus.

### C2. Bandwidth with additivity and four-band decomposition (Primitive P04)

Non-negative bandwidth on each channel; additive across disjoint channels; decomposes into four mutually orthogonal bands (internal, adjacency, environmental, commitment-reserve) with bandwidth conservation along an isolated chain's persistence regime.

### C3. Polarity (Primitive P09)

$U(1)$-valued angular primitive on each channel.

### C4. Time homogeneity + spatial homogeneity (Primitive P13 + P03 translation symmetry)

Continuous time axis with homogeneous structure (Paper #4 substrate condition); continuous spatial structure with translation symmetry, supplying the spatial-translation generator $\hat{p}$ via Paper #4-class Stone's-theorem-on-spatial-translations.

### C5. Rotational symmetry of the participation manifold

The substrate's spatial structure is isotropic at the kinematic level: no preferred direction. This is the structural source of $\hat{T} = f(|\hat{p}|^2)$ (a scalar function of momentum magnitude, not direction).

### C6. Non-relativistic-single-particle scope

The dynamical regime considered is non-relativistic single-particle. This selects the Galilean group (with absolute time) over the Lorentz group (with mixed space-time boosts). Relativistic extensions (where kinetic energy follows $E^2 = p^2c^2 + m^2c^4$) lie in a different scope and are treated by Arc R.

### C7. Gauge-coupling-free scope

Magnetic vector potentials are absent: the Hamiltonian does not yet include $\hat{p} - eA(\hat{x})/c$ replacements. Gauge couplings are downstream content (Paper #5 supplies the gauge structure; this paper covers the free-Hamiltonian + scalar-potential regime).

### C8. Inherited results from Papers #1-#4

- **Paper #1**: participation measure on each channel.
- **Paper #2**: Born rule for commitment outcomes.
- **Paper #3**: sesquilinear inner product on the participation manifold.
- **Paper #4**: Schrödinger evolution $i\hbar\,\partial_t P = \hat{H} P$ with $\hat{H}$ self-adjoint and uniquely determined by Stone's theorem on time-translation symmetry.

A reader who has not read Papers #1-#4 may take C8 as a definitional premise: the matter sector carries a complex Hilbert space with unitary time evolution generated by an unknown self-adjoint $\hat{H}$. The present paper determines the *form* of $\hat{H}$.

### C9. No Hamiltonian form as input

The forcing argument invokes only C1-C8 plus the following standard mathematical infrastructure:

- The Galilean Lie algebra and its non-relativistic-scope structure.
- Stone's theorem applied to spatial translations (giving $\hat{p} = -i\hbar\nabla$).
- Basic operator theory + the Galilean integration Jacobian.

No Hamiltonian operator form (kinetic-plus-potential, quadratic-in-$\hat{p}$, factor-of-$1/(2m)$) is assumed; no classical-mechanics analogy is invoked as derivation input; no Lagrangian variational principle is taken as given.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. No kinetic-energy operator.** A Hamiltonian generator without a kinetic part: $\hat{H} = V(\hat{x})$ alone. Time evolution is then purely potential-driven, with no momentum-dependent kinetic structure.

**A2. Linear-in-$|\hat{p}|$ kinetic term.** $\hat{T} \propto |\hat{p}|$, as in relativistic dispersions for massless particles ($E = pc$).

**A3. Higher-even-power kinetic terms.** $\hat{T} \propto |\hat{p}|^4$, $|\hat{p}|^6$, or other higher even powers. Includes Taylor-expansion remainders of the relativistic dispersion at finite mass.

**A4. Anisotropic kinetic energy.** $\hat{T}$ depending on the direction of $\hat{p}$, not just its magnitude: $\hat{T}(\hat{p}_x, \hat{p}_y, \hat{p}_z)$ with distinct scalar couplings to each component.

**A5. Wrong factor in $1/(2m)$.** Kinetic operator $\hat{T} = c\,|\hat{p}|^2/m$ for some $c \neq 1/2$. E.g., $c = 1$ giving $|\hat{p}|^2/m$; $c = 1/4$ giving $|\hat{p}|^2/(4m)$.

**A6. Position-momentum cross terms.** Hamiltonians with $\hat{x}\hat{p}$ or $\hat{p}\hat{x}$ structures in the free part (not present in a kinetic-plus-potential decomposition).

**A7. Mass as fundamental (not substrate-derived).** Mass treated as a primitive scalar input rather than a derived bandwidth-signature functional.

**A8. Forced mass ratios from primitives.** Strong claims that ED primitives + symmetry alone force specific mass ratios (e.g., $m_e/m_p$ derivable from primitive structure).

### 6.2 Mainstream alternatives

**B1. Classical Hamiltonian as postulate.** The Hamiltonian function $H(q, p)$ adopted as fundamental in classical mechanics. Quadratic form motivated by analogy with classical kinetic energy from velocity squared.

**B2. Newton's $F = ma$ inertia postulate.** Inertia treated as a fundamental property of bodies, with mass $m$ a positive scalar measuring resistance to acceleration. No derivation of the linearity or the scalar character.

**B3. Modified inertia (MOND-class).** Milgrom's modified inertia / MOND framework proposes that the inertial response of bodies deviates from $F = ma$ at low accelerations, with a transition acceleration $a_0 \sim 10^{-10}\,\text{m/s}^2$. The modification is empirically motivated by galactic rotation curves; the structural origin is not derived.

**B4. Higgs mechanism (specific masses).** Standard Model fermion masses arise from Yukawa couplings to the Higgs field. Specific mass values follow from specific Yukawa coupling strengths, which are inputs. The structural form of mass (Lorentz scalar with units of energy) is not derived; it is part of the package.

**B5. Mach's principle (inertia from cosmology).** Inertia of local bodies arises from interaction with the global mass-energy distribution of the universe. Specific implementations (Brans-Dicke, scalar-tensor theories) introduce new structural fields; the original principle is more philosophical than mechanical.

**B6. Relativistic energy-momentum without non-relativistic limit.** Treating $E^2 = p^2c^2 + m^2c^4$ as fundamental and deriving $\hat{H} = \sqrt{|\hat{p}|^2 c^2 + m^2 c^4}$ (or equivalent) as the kinematic Hamiltonian operator. The non-relativistic limit is then an approximation, and the precise form $\hat{H} = \hat{p}^2/(2m) + V$ is not fundamental.

---

## 7. Constructive Necessity

The argument establishes the Hamiltonian form and mass structure in six steps.

### 7.1 Channel-momentum identification (F1)

Paper #4 / Paper #1's analog establishes that the spatial-translation generator on the participation-manifold Hilbert space is, by Stone's theorem on spatial translations (C4), the operator
$$
\hat{p} = -i\hbar\nabla.
$$
The eigenstates of $\hat{p}$ are plane waves $e^{i k \cdot x}$ with eigenvalue $\hbar k$. This is the channel-momentum identification: in the thin-participation continuum limit, the channel index $K$ becomes a continuous momentum label.

The Hamiltonian $\hat{H}$ of Paper #4 acts on the same Hilbert space as $\hat{p}$. The question of this paper is: what is the form of $\hat{H}$?

### 7.2 Kinetic-plus-potential decomposition (F5)

**Translation invariance + locality forces additive decomposition.**

The free-particle Hamiltonian (no external potential) must commute with $\hat{p}$ on the participation manifold: spatial translation symmetry (C4) requires $[\hat{H}_{\text{free}}, \hat{p}] = 0$. Only functions of $\hat{p}$ commute with $\hat{p}$; functions of $\hat{x}$ do not. Therefore the free part of $\hat{H}$ depends only on $\hat{p}$: $\hat{T}(\hat{p})$.

External-potential contributions to $\hat{H}$ must be *local*: the substrate-level commitment primitive (C5 in Paper #4's substrate-class, C8 here via Paper #4 inheritance) anchors interactions at specific loci. Position-local interactions are functions of $\hat{x}$: $V(\hat{x})$.

Cross-terms $\hat{x}\hat{p}$ or $\hat{p}\hat{x}$ in the free Hamiltonian violate translation invariance (they include $\hat{x}$ dependence) without being position-local (they include $\hat{p}$ dependence). In the gauge-coupling-free regime (C7), neither type of constraint can support cross-terms; they are forbidden.

Therefore:
$$
\hat{H} = \hat{T}(\hat{p}) + V(\hat{x}).
$$

### 7.3 Quadratic kinetic structure (F3)

**Rotation invariance + non-relativistic-limit scope forces $\hat{T} = f(|\hat{p}|^2)$ with the quadratic form forced.**

Rotational symmetry of the participation manifold (C5) requires $\hat{T}$ to be a scalar function of $\hat{p}$. The only rotationally invariant scalars built from $\hat{p}$ alone are functions of $|\hat{p}|^2 = \hat{p} \cdot \hat{p}$. Therefore $\hat{T} = f(|\hat{p}|^2)$ for some function $f$.

Analyticity at $\hat{p} = 0$ (a structural smoothness requirement on the Hamiltonian generator; without it the Schrödinger evolution would have a branch-point singularity at zero momentum) forces $f$ to be expressible as a power series in $|\hat{p}|^2$:
$$
f(|\hat{p}|^2) = a_0 + a_1\,|\hat{p}|^2 + a_2\,|\hat{p}|^4 + \cdots.
$$
The constant $a_0$ is a zero-point energy and can be absorbed into the potential's zero (a gauge choice for $V$); without loss of generality $a_0 = 0$.

The non-relativistic-limit scope (C6) suppresses higher-power terms $a_n\,|\hat{p}|^{2n}$ for $n \geq 2$ by powers of $(v/c)^{2(n-1)}$ — the Taylor expansion of the relativistic dispersion $E = \sqrt{p^2 c^2 + m^2 c^4} - mc^2 = p^2/(2m) - p^4/(8m^3 c^2) + \cdots$ collapses to its leading term as $c \to \infty$. In the strict non-relativistic limit (C6), only the $|\hat{p}|^2$ term survives. Linear-in-$|\hat{p}|$ terms (A2) are excluded: they are vector quantities ($\alpha \cdot \hat{p}$) and violate rotation invariance (C5); scalar $|\hat{p}|c$ has a branch-point at $\hat{p} = 0$ violating analyticity.

Therefore:
$$
\hat{T}(\hat{p}) = a_1\,|\hat{p}|^2,
$$
for some coefficient $a_1$ to be determined.

### 7.4 The factor of $1/(2m)$ from Galilean integration (F4)

**The Galilean Lie algebra forces $a_1 = 1/(2m)$ via the integration Jacobian.**

The non-relativistic scope (C6) is the regime of Galilean symmetry. The Galilean group has generators $\{\hat{H}, \hat{p}_i, \hat{K}_i, \hat{J}_i\}$ (Hamiltonian, momentum, boost, angular-momentum). The boost generator is, in the participation-manifold representation,
$$
\hat{K}_i = m\hat{x}_i - t\hat{p}_i.
$$

The Galilean Lie algebra closure imposes the commutator
$$
[\hat{H}, \hat{K}_i] = -i\hbar\hat{p}_i.
$$
This is a structural fact about the Galilean group's action on the participation manifold — not an ansatz, but a consequence of the group's algebraic structure plus its unitary representation on the Hilbert space.

Substituting $\hat{H} = \hat{T}(\hat{p}) + V(\hat{x})$:
$$
[\hat{T}(\hat{p}), m\hat{x}_i] + [V(\hat{x}), -t\hat{p}_i] = -i\hbar\hat{p}_i.
$$

The two commutators give, using $[\hat{p}_j, \hat{x}_i] = -i\hbar\delta_{ij}$:
- $[\hat{T}(\hat{p}), m\hat{x}_i] = -i\hbar m\,\partial_{\hat{p}_i}\hat{T}$
- $[V(\hat{x}), -t\hat{p}_i] = -t \cdot i\hbar\,\partial_{\hat{x}_i} V$

For the equation to hold as a structural identity, the velocity-conjugacy part (the first term) must produce $-i\hbar\hat{p}_i$ and the potential-conjugacy part must vanish on average (which it does in equilibrium). Therefore:
$$
-i\hbar m\,\partial_{\hat{p}_i}\hat{T} = -i\hbar\hat{p}_i,
$$
giving
$$
\partial_{\hat{p}_i}\hat{T} = \frac{\hat{p}_i}{m}.
$$
Integrating with respect to $\hat{p}_i$:
$$
\hat{T} = \frac{|\hat{p}|^2}{2m} + \text{const},
$$
with the constant absorbed into the zero of $V$.

**The factor of 2 in $1/(2m)$ is the integration Jacobian.** When integrating $\partial_{\hat{p}_i}\hat{T} = \hat{p}_i/m$ with respect to $\hat{p}_i$, the antiderivative of $\hat{p}_i$ is $\hat{p}_i^2/2$. Summing over the three Cartesian indices: $\sum_i \hat{p}_i^2/(2m) = |\hat{p}|^2/(2m)$. The factor of 2 emerges as a chain-rule coefficient from the Galilean commutator integration — not as a convention borrowed from classical mechanics.

This is the key structural derivation. The Hamiltonian form
$$
\hat{H} = \frac{|\hat{p}|^2}{2m} + V(\hat{x})
$$
is uniquely forced by the Galilean Lie algebra closure on the participation-manifold Hilbert space.

### 7.5 Mass as a Lorentz-scalar bandwidth-signature functional

**Mass appears in the Hamiltonian as a single positive scalar parameter $m$. Where does this parameter come from?**

The substrate's four-band decomposition (C2) supplies a structural bandwidth content for each rule-type $\tau$. A **bandwidth-signature functional** $\sigma_\tau$ is constructed as a Lorentz-scalar combination of the four-band content with units of energy via $\hbar \times$ frequency.

The specific construction (Arc M / F-M1 through F-M4):
- $\sigma_\tau$ is a logarithmic-derivative spectral rate of the rule-type's bandwidth content — independent of overall amplitude (so that mass does not scale with the gauge-arbitrary normalization of the participation measure).
- $\sigma_\tau$ has units of energy. The identification $m_\tau = \sigma_\tau/c^2$ then gives mass with units of energy/$c^2$ — the standard relativistic mass-energy correspondence in non-relativistic guise.
- $\sigma_\tau$ admits Case-P (Bose-like) and Case-R (Fermi-like) variants distinguished by which scalar bilinear ($|\Psi|^2$ vs $|\bar\Psi\Gamma\Psi|$) carries the mass content.

The **form** of mass is FORCED: a Lorentz-scalar functional of the four-band content, with the spectral-rate logarithmic-derivative structure forced by non-amplitude-dependence + dimensional consistency.

The **value** of mass is INHERITED: the specific numerical value of $\sigma_\tau$ for any given rule-type depends on chain-initial-condition data (the spectral-rate average over the rule-type's worldline) that is not derivable from substrate primitives alone. Different rule-types have different $\sigma_\tau$ and hence different $m_\tau$; the ratios between them are not derived.

### 7.6 What is FORCED and what is INHERITED — the H1-dominant verdict

The Arc M analysis closes with an **H1-dominant** verdict: ED forces the *structure* of mass but inherits the *values*. Specifically:

- **FORCED (structure):** Lorentz-scalar form of $\sigma_\tau$; dimensional anchoring via $\hbar \times$ frequency; statistics-class mechanism (Case P vs Case R) for masslessness; Fierz-class taxonomy for mass-term type (Dirac, Majorana, pseudoscalar); conditional existence of at least one massless gauge rule-type given Paper #5's gauge-field forcing.
- **INHERITED (values):** numerical mass for each rule-type; mass ratios across rule-types; mass hierarchies; the number of generations; whether specific rule-types occupy the massless slot.
- **REFUTED (Arc M negative results):** six strong-form mass-ratio claims systematically refuted (R-M1 through R-M6) — including $\sigma_\tau \propto$ representation dimension, $\propto$ spin, ordered by statistics class, etc. ED does *not* derive mass hierarchies.

The Hamiltonian's mass parameter $m$ is therefore $m_\tau = \sigma_\tau/c^2$ for the rule-type whose participation measure is being evolved, with $\sigma_\tau$ a substrate-level functional whose form is forced and whose value is inherited.

The composite result of §§7.1-7.6: the Hamiltonian form
$$
\hat{H} = \frac{\hbar^2|\hat{p}|^2}{2m_\tau} + V(\hat{x})
$$
with $m_\tau = \sigma_\tau/c^2$ is FORCED in structural form and INHERITED in numerical value.

---

## 8. Exclusion Arguments

### 8.1 A1 — No kinetic-energy operator

A Hamiltonian generator without a kinetic part fails the Galilean commutator condition $[\hat{H}, \hat{K}_i] = -i\hbar\hat{p}_i$ (§7.4): the commutator $[V(\hat{x}), m\hat{x}_i]$ is zero (functions of $\hat{x}$ commute), and the commutator $[V(\hat{x}), -t\hat{p}_i]$ at $t = 0$ is also zero, leaving no source for the $-i\hbar\hat{p}_i$ on the right-hand side. The Galilean algebra cannot close. C6 (non-relativistic Galilean scope) is violated.

### 8.2 A2 — Linear-in-$|\hat{p}|$ kinetic term

Vector $\alpha \cdot \hat{p}$ is excluded by rotational invariance (C5): the linear scalar product requires a preferred direction $\alpha$, which the isotropic participation manifold does not supply. Scalar $|\hat{p}|c$ has a branch-point at $\hat{p} = 0$ that violates analyticity of the Hamiltonian generator. In addition, $|\hat{p}|c$ is the massless-particle dispersion, which violates the massive non-relativistic scope (C6).

### 8.3 A3 — Higher-even-power kinetic terms

Terms $|\hat{p}|^{2n}$ for $n \geq 2$ are suppressed by powers of $(v/c)^{2(n-1)}$ in the non-relativistic limit (C6); in the strict $c \to \infty$ limit they vanish. They appear in *post-Newtonian* expansions (e.g., the $-|\hat{p}|^4/(8m^3 c^2)$ correction to the relativistic dispersion) but not in the strictly non-relativistic Hamiltonian. C6 forbids them.

### 8.4 A4 — Anisotropic kinetic energy

Direction-dependent kinetic terms violate rotational invariance (C5). The participation manifold is structurally isotropic; no primitive supplies a preferred direction. Anisotropic dispersions arise in condensed-matter contexts via lattice symmetry-breaking at higher levels of structure; at the substrate level they are excluded.

### 8.5 A5 — Wrong factor in $1/(2m)$

The factor of $1/(2m)$ is forced by the Galilean integration Jacobian (§7.4): $\partial_{\hat{p}_i}\hat{T} = \hat{p}_i/m$ integrates to $|\hat{p}|^2/(2m)$, with the factor of 2 emerging as the chain-rule coefficient of integrating $\hat{p}_i$ to $\hat{p}_i^2/2$. Any other coefficient would correspond to a different right-hand side of the Galilean commutator, which is fixed by the group's algebra. C6 (Galilean scope) forces the factor.

### 8.6 A6 — Position-momentum cross terms

Cross terms $\hat{x}\hat{p}$ or $\hat{p}\hat{x}$ in the free Hamiltonian violate either translation invariance (they include $\hat{x}$) or position-locality (they include $\hat{p}$). In the gauge-coupling-free regime (C7), no such terms are admitted. C4 (translation symmetry) + C7 forbid them. Gauge-coupled Hamiltonians do contain $(\hat{p} - eA/c)$ structures, but the $A$ field is a separate participation measure of the gauge rule-type (Paper #5) and the structure remains kinetic-plus-potential at the substrate level after redefinition $\hat{p} \to \hat{p} - eA$.

### 8.7 A7 — Mass as fundamental (not substrate-derived)

Treating mass as a primitive scalar input violates the substrate-conditions test: the substrate primitives (P02-P13) do not supply a mass primitive directly. Mass appears only as a *derived* substrate-level functional (§7.5) of the four-band content (C2). A theory taking mass as fundamental introduces a structural commitment unsupported by the primitive stack.

### 8.8 A8 — Forced mass ratios from primitives

The Arc M negative results (R-M1 through R-M6, R-M10, R-M11) systematically refute strong-form mass-ratio claims: $\sigma_\tau$ ratios are not determined by representation dimension, spin, statistics class, Fierz class, band-weight pattern, or individuation geometry. Numerical mass content is rule-type data (initial conditions on the chain), not derivable from primitive structure. C8's H1-dominant verdict forbids ED from forcing mass ratios.

### 8.9 B1 — Classical Hamiltonian as postulate

The classical Hamiltonian $H(q, p) = p^2/(2m) + V(q)$ is taken as fundamental in classical mechanics. Under the substrate-conditions test, this is *downstream* of the forcing chain: the substrate-derived Hamiltonian's quantum form, in the classical limit ($\hbar \to 0$, Ehrenfest theorem), reduces to the classical Hamiltonian function. The classical form is therefore a consequence of the substrate-level result, not an alternative to it.

### 8.10 B2 — Newton's $F = ma$ inertia postulate

Newton's second law follows from the Ehrenfest theorem applied to the substrate-derived Hamiltonian: $d\langle\hat{p}\rangle/dt = -\langle\nabla V\rangle = \langle F\rangle$, giving classical $F = ma$ in the centroid limit. The substrate forcing produces $F = ma$ as a structural corollary; treating $F = ma$ as a postulate is a downstream presentation, not a substrate-level alternative.

### 8.11 B3 — Modified inertia (MOND-class)

MOND-class modifications of inertia at low accelerations are empirically motivated by galactic rotation curves. Under the substrate-conditions test, MOND-class modifications would require either:
- A modification of the Galilean commutator structure at low accelerations (no primitive supplies such a modification);
- A modification of the bandwidth-signature functional $\sigma_\tau$ at the substrate level (Arc M's mass-structure forcing forbids amplitude-dependent $\sigma_\tau$).

The empirical content of MOND is reproduced in ED's substrate-gravity program via a different mechanism (substrate-level modifications of the gravitational sector at low gradients), not by modifying the Hamiltonian's kinetic structure. The kinetic operator's $|\hat{p}|^2/(2m)$ form is forced regardless of acceleration scale.

### 8.12 B4 — Higgs mechanism

The Higgs mechanism produces specific numerical mass values via Yukawa couplings. Under the substrate-conditions test, the Higgs mechanism is *downstream* of the substrate-level mass-structure forcing: the substrate forces the form of $\sigma_\tau$ (Lorentz-scalar bandwidth functional with energy units); the Higgs sector supplies a specific value-layer mechanism producing particular numerical $\sigma_\tau$ values for Standard Model fermions. Both can be true; the Higgs mechanism is a value-layer realization of the substrate-derived mass structure.

### 8.13 B5 — Mach's principle

Mach's principle attributes inertia to interaction with the global mass-energy distribution. Under the substrate-conditions test, Mach's principle is either (i) a metaphysical commentary on the origin of inertia (not testable structurally), or (ii) a specific implementation involving new gravitational fields (Brans-Dicke, scalar-tensor), in which case it is downstream of substrate-level gravitational content. Neither competes with the substrate-derived Hamiltonian form.

### 8.14 B6 — Relativistic energy-momentum without non-relativistic limit

Treating $E = \sqrt{|\hat{p}|^2 c^2 + m^2 c^4}$ as fundamental and the non-relativistic Hamiltonian as an approximation. Under the substrate-conditions test, this is the regime *outside* C6 (non-relativistic scope). The relativistic Hamiltonian operator is the content of Arc R (Dirac equation forcing), not this paper. The two are compatible: the relativistic operator reduces to $\hat{p}^2/(2m) + V$ in the non-relativistic limit, and the present paper's forcing applies to that limit. Treating the relativistic form as fundamental does not contradict the present paper; it merely operates in a different scope.

### 8.15 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 no kinetic operator | C6 | Galilean commutator $[\hat{H},\hat{K}]=-i\hbar\hat{p}$ requires nonzero kinetic source. |
| A2 linear $\|\hat{p}\|$ | C5, analyticity | Vector form violates rotation; scalar $\|\hat{p}\|c$ has branch-point at $\hat{p}=0$ + massless dispersion. |
| A3 higher-power $\|\hat{p}\|^{2n}$ | C6 | Suppressed by $(v/c)^{2(n-1)}$; vanish in non-relativistic limit. |
| A4 anisotropic kinetic | C5 | Direction-dependent terms violate rotational symmetry of participation manifold. |
| A5 wrong factor in $1/(2m)$ | C6 (Galilean) | Integration Jacobian of $\partial_{\hat{p}_i}\hat{T}=\hat{p}_i/m$ uniquely gives $\|\hat{p}\|^2/(2m)$. |
| A6 position-momentum cross terms | C4, C7 | Translation invariance + gauge-coupling-free regime forbid cross-terms in free Hamiltonian. |
| A7 mass as fundamental | substrate-primitives | No mass primitive in P02-P13; mass is derived from C2 four-band content. |
| A8 forced mass ratios | Arc M H1-dominant | Six ratio claims (R-M1 through R-M6) systematically refuted; numerical mass is rule-type data. |
| B1 classical Hamiltonian postulate | not in space | Classical $H(q,p)$ is Ehrenfest limit of forced quantum operator; downstream consequence. |
| B2 Newton's $F=ma$ postulate | not in space | $F=ma$ is Ehrenfest corollary of substrate-derived Hamiltonian; not substrate-level alternative. |
| B3 MOND-class modified inertia | C6 (Galilean), Arc M | No substrate mechanism for acceleration-dependent kinetic structure; MOND lives in gravity sector. |
| B4 Higgs mechanism | not in space | Downstream value-layer mechanism producing specific $\sigma_\tau$ values; consistent with substrate forcing. |
| B5 Mach's principle | not in space | Either metaphysical or downstream of gravitational sector; doesn't address Hamiltonian form. |
| B6 relativistic-only Hamiltonian | scope-different | Operates outside C6; reduces to forced non-relativistic form in $c \to \infty$ limit. |

**The Hamiltonian $\hat{H} = \hbar^2|\hat{p}|^2/(2m) + V(\hat{x})$ with mass $m_\tau = \sigma_\tau/c^2$ a Lorentz-scalar bandwidth-signature functional is the unique survivor.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier is identical to the empirical falsifier of standard non-relativistic quantum mechanics + the Lorentz-scalar character of mass:

- **Tests of $\hat{T} = \hat{p}^2/(2m)$ form**: precision spectroscopy of hydrogen and other simple systems, electron-orbital structure in atoms, scattering experiments — all consistent with the quadratic kinetic operator to high precision. Departures (anomalous dispersion, direction-dependent inertia) would falsify the substrate forcing along with standard QM.
- **Tests of mass isotropy**: precision tests of Lorentz invariance (atomic clock comparisons, optical-cavity rotation experiments) constrain anisotropy of inertial mass to ~$10^{-18}$ level. Any reproducible anisotropy would falsify C5 / §7.3.
- **Tests of $F = ma$ at very low accelerations**: galactic rotation curves famously deviate from Newtonian predictions, which is the empirical motivation for MOND. The substrate-derived Hamiltonian forcing predicts the kinetic form is *not* modified; the rotation-curve anomaly is therefore attributed to gravitational-sector content (substrate-gravity arc), not to kinetic-operator modification.
- **Tests of mass renormalization**: precision QED-corrected mass calculations (electron magnetic moment, Lamb shift) are consistent with substrate-level mass structure plus standard radiative corrections.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C9 (channel-primitive participation graph, four-band bandwidth, $U(1)$ polarity, time and spatial homogeneity, rotational symmetry, non-relativistic single-particle scope, gauge-coupling-free regime, Papers #1-#4 inherited) but supporting a non-quadratic kinetic operator, an anisotropic kinetic term, position-momentum cross terms in the free Hamiltonian, or mass as a non-substrate-derived parameter, that survives the exclusion arguments of §8.

The author's claim is that no such substrate exists. Each alternative is dispatched by a specific substrate-condition violation. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

Three immediate exposures:

**Ehrenfest theorem and classical limit.** The Ehrenfest relations $d\langle\hat{x}\rangle/dt = \langle\hat{p}\rangle/m$ and $d\langle\hat{p}\rangle/dt = -\langle\nabla V\rangle$ follow from the substrate-derived Hamiltonian + the canonical commutation relation $[\hat{x}, \hat{p}] = i\hbar$. Classical mechanics is recovered in the centroid + $\hbar \to 0$ limit, with the substrate-derived $m$ playing the role of inertial mass.

**Atomic and molecular spectra.** Hydrogen energy levels $E_n = -m_e c^2 \alpha^2/(2n^2)$ + higher corrections follow from solving the Schrödinger equation with the substrate-derived Hamiltonian. The $1/(2m)$ coefficient is directly tested in every spectroscopy experiment that depends on the kinetic-energy contribution to atomic structure.

**Particle masses in the Standard Model.** The Lorentz-scalar character of mass + the rule-type-dependence of $\sigma_\tau$ are consistent with the empirical Standard Model: each fermion has its own mass; the masses do not depend on direction or position; mass values are inputs (consistent with H1-dominant verdict) supplied empirically or via Higgs Yukawa couplings.

The substrate-level Hamiltonian forcing supports every quantitative kinematic prediction of non-relativistic quantum mechanics, including the appearance of mass as a rule-type-specific Lorentz-scalar parameter.

---

## Appendix A — Derivation Chain and Glossary

### A.1 Galilean integration giving $1/(2m)$ — full calculation

The Galilean Lie algebra commutator $[\hat{H}, \hat{K}_i] = -i\hbar\hat{p}_i$ on the participation-manifold Hilbert space, with boost generator $\hat{K}_i = m\hat{x}_i - t\hat{p}_i$ and Hamiltonian $\hat{H} = \hat{T}(\hat{p}) + V(\hat{x})$. The commutator expands as:
$$
[\hat{T}(\hat{p}) + V(\hat{x}),\, m\hat{x}_i - t\hat{p}_i] = m[\hat{T}, \hat{x}_i] + m[V, \hat{x}_i] - t[\hat{T}, \hat{p}_i] - t[V, \hat{p}_i].
$$
Term-by-term:
- $[V(\hat{x}), \hat{x}_i] = 0$ (functions of $\hat{x}$ commute).
- $[\hat{T}(\hat{p}), \hat{p}_i] = 0$ (functions of $\hat{p}$ commute).
- $[\hat{T}(\hat{p}), \hat{x}_i] = -i\hbar\,\partial_{\hat{p}_i}\hat{T}(\hat{p})$, using $[\hat{p}_j, \hat{x}_i] = -i\hbar\delta_{ji}$.
- $[V(\hat{x}), \hat{p}_i] = i\hbar\,\partial_{\hat{x}_i}V$.

Substituting:
$$
m\,(-i\hbar)\,\partial_{\hat{p}_i}\hat{T} - t \cdot i\hbar\,\partial_{\hat{x}_i}V = -i\hbar\hat{p}_i.
$$
Separating the $t$-independent and $t$-linear pieces:
$$
\partial_{\hat{p}_i}\hat{T} = \frac{\hat{p}_i}{m}, \qquad \partial_{\hat{x}_i}V = 0\,(\text{statement of free-particle limit}).
$$
Integrating the first equation:
$$
\hat{T}(\hat{p}) = \int \frac{\hat{p}_i}{m}\,d\hat{p}_i = \frac{\hat{p}_i^2}{2m} + \text{const}.
$$
Summing over $i$:
$$
\hat{T}(\hat{p}) = \frac{|\hat{p}|^2}{2m} + \text{const},
$$
with the constant absorbed into the zero of the energy spectrum (a gauge choice).

The factor of 2 is the integration Jacobian of integrating $\hat{p}_i$ with respect to $\hat{p}_i$. It is not a convention; it is the structural consequence of the Galilean commutator's structure.

### A.2 Bandwidth-signature functional $\sigma_\tau$ — outline

For each rule-type $\tau$ with four-band participation $(b_K^\text{int}, b_K^\text{adj}, b_K^\text{env}, b_K^\text{com})$, define the spectral rate:
$$
\sigma_\tau := \hbar\,\left\langle\left(\frac{\partial \ln b^X}{\partial t}\right)^2\right\rangle_\tau^{1/2},
$$
where $X$ runs over the four bands and the average is over the rule-type's worldline. The logarithmic-derivative form ensures $\sigma_\tau$ is independent of overall bandwidth amplitude (a gauge-invariant statement). Units: energy. The mass identification is $m_\tau = \sigma_\tau/c^2$.

This is the structural form of mass. Numerical values of $\sigma_\tau$ depend on chain-initial-condition data and are inherited from the value layer. Mass ratios across rule-types are not forced (Arc M H1-dominant verdict).

### A.3 Glossary

- **Bandwidth $b_K(u)$.** Primitive non-negative substrate quantity on each channel.
- **Bandwidth-signature functional $\sigma_\tau$.** Lorentz-scalar functional of a rule-type's four-band content, with units of energy; identified with mass via $m_\tau = \sigma_\tau/c^2$.
- **Boost generator $\hat{K}_i$.** Galilean boost generator $m\hat{x}_i - t\hat{p}_i$.
- **Channel.** Primitive structural pathway in the participation graph.
- **FORCED.** Derived from substrate primitives + standard mathematics with no additional commitments.
- **Four-band decomposition.** Substrate-level orthogonal decomposition of bandwidth into internal, adjacency, environmental, and commitment-reserve bands.
- **Galilean Lie algebra.** Algebra of the Galilean group: generators $\{\hat{H}, \hat{p}_i, \hat{K}_i, \hat{J}_i\}$ with commutator $[\hat{H}, \hat{K}_i] = -i\hbar\hat{p}_i$.
- **Hamiltonian $\hat{H}$.** Self-adjoint generator of time evolution; structurally $\hat{T}(\hat{p}) + V(\hat{x})$ in the non-relativistic free-or-potential-coupled regime.
- **Inertial mass $m$.** Lorentz-scalar parameter in the Hamiltonian, structurally identified with $\sigma_\tau/c^2$.
- **INHERITED.** Quantitative content (mass values, ratios, hierarchies, $\hbar$) not derived in this paper.
- **Kinetic energy $\hat{T}(\hat{p})$.** $|\hat{p}|^2/(2m)$ in non-relativistic regime; forced by §7.3-§7.4.
- **Participation measure.** Complex-valued amplitude carrier on each channel (Paper #1).
- **Rule-type.** Substrate primitive class of channel structure (Paper #5).
- **Substrate.** Pre-quantum primitive layer.
- **Translation invariance.** Property of the free Hamiltonian: commutes with spatial-translation generator $\hat{p}$. Equivalently, $\hat{T}$ is a function of $\hat{p}$ only.

### A.4 Source-repository citations (for ED-internal readers)

- `papers/U4_Hamiltonian_Form/paper_u4_hamiltonian_form.md` — publication-grade U4 paper (predecessor genre).
- `arcs/U4/04_closure_and_summary.md` — U4 arc closure with five sub-feature derivations (F1-F5).
- `arcs/U4/03_F3_F4_and_verdict.md` — load-bearing F3 (quadratic structure) and F4 (factor of 2 via Galilean integration) derivations.
- `arcs/arc-M/chain_mass_synthesis.md` — Arc M closure with H1-dominant verdict.
- `arcs/arc-M/mass_ratio_constraints.md` — systematic refutation of six strong-form ratio claims.
- `arcs/arc-M/cascade_memo_F_M8_promotion.md` — F-M8 promotion after Paper #5 (T17) closure.
- `walkthroughs/from_primitives_to_mass.md` — public-facing walkthrough on mass structure.
- `theorems/T15.md` — theorem-level index entry for U4 (kinetic operator + factor of 2); status FORCED-unconditional, ratified 2026-04-26.

These are *not* required reading for the present paper.

---

*End of Paper #6.*
