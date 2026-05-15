# The Discrete-to-Continuum Gauge Translation (DCGT) is FORCED

**Paper #8 of the Event Density Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-12
**Series:** Event Density (ED) First-Wave Forcing Papers — Paper #8 of 10
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The continuum gauge potential $A_\mu(x)$, the field strength $F_{\mu\nu}(x)$, and the covariant derivative $D_\mu$ are the standard objects of classical electrodynamics and Yang-Mills theory. They are normally postulated as continuum primitives with their transformation properties imposed as axioms. This paper shows that, **given the discrete gauge-rule-type structure of Paper #5 plus the hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ and the standard regularity assumptions of the Diffusion Coarse-Graining Theorem (DCGT, Arc D)**, the continuum gauge structure is forced as the unique hydrodynamic-window coarse-graining of the discrete substrate connection. Non-local-limit, non-connection-limit, non-tensorial, and non-covariant alternatives are excluded. The claim is conditional on the hydrodynamic-window assumption: outside that scale separation, the substrate-to-continuum bridge does not apply, and the discrete substrate content is what is fundamental. The hydrodynamic-window assumption is itself empirically robust (covers all observed gauge phenomena down to the Planck scale) but is a load-bearing input, not derived here.

---

## 1. Framing

### 1.1 What standard physics assumes about the continuum limit of gauge fields

Every textbook on quantum field theory or general relativity treats the continuum gauge field $A_\mu(x)$ as a smooth function (or differential one-form) on a four-dimensional spacetime manifold. The field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]$ is the curvature of the connection $A_\mu$; the covariant derivative $D_\mu = \partial_\mu + igA_\mu$ replaces ordinary derivatives in matter Lagrangians via minimal coupling.

The transformation properties under local gauge symmetry are imposed as axioms:
- $A_\mu \to UA_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$ for $U(x)$ a smooth local gauge transformation.
- $F_{\mu\nu} \to UF_{\mu\nu}U^{-1}$ covariantly.
- Matter fields $\psi \to U\psi$ with $D_\mu\psi$ transforming covariantly.

These transformation laws are taken as definitions; the gauge theory is *built* to respect them. Continuum gauge invariance is not derived from anything more fundamental — it is the starting structural commitment of the entire formalism.

Lattice gauge theory introduces a discrete version: gauge fields live on links of a hypercubic lattice as group elements $U_l \in G$, with field strengths defined as plaquette holonomies. The continuum limit is then *taken* as a limit of lattice spacing $a \to 0$, with the continuum $A_\mu$ identified as the leading-order expansion of $U_l = \exp(ia g A_\mu)$. Lattice gauge theory provides a regularization, but the continuum limit is a mathematical operation, not a substrate-level forcing argument. The lattice itself is postulated; the discrete-to-continuum identification is verified rather than derived.

### 1.2 The puzzle

Several partial arguments connect discrete and continuum gauge structure:

- **Lattice gauge theory** (Wilson 1974): discrete plaquette variables $U_p$ produce gauge-invariant actions; their continuum limit reproduces Yang-Mills. The lattice is a regularization choice, not a substrate.
- **Loop quantum gravity** and related programs use discrete connection variables (spin networks, holonomies) as fundamental; the continuum limit is an emergent structure. The discrete structure is postulated.
- **Fiber bundle formulations** treat connections and curvatures abstractly; the discrete-to-continuum question does not arise because the formalism is intrinsically continuum.

None of these derives the continuum gauge structure from a *pre-quantum substrate of primitive structure* via an explicit coarse-graining mechanism. The deeper question — under what conditions does substrate-level discrete gauge content yield the standard continuum $(A_\mu, F_{\mu\nu}, D_\mu)$ with the correct transformation laws, and is this discrete-to-continuum bridge unique? — remains open.

### 1.3 What this paper does

The Event Density (ED) framework supplies a pre-quantum substrate. Paper #5 establishes that the discrete gauge potential is the participation measure of a substrate-level rule-type $\tau_g$, with local gauge-quotient invariance as the rule-type's interface property. The substrate is genuinely discrete: a participation graph with channels, vertices, polarity transport, and commitment events.

The present paper extends to the continuum. Given the substrate-level discrete gauge content of Paper #5 and the substrate-to-continuum coarse-graining methodology of the ED program's Arc D, this paper forces:

1. **The continuum gauge potential** $A_\mu(x)$ as the hydrodynamic-window coarse-graining of the discrete substrate connection.
2. **The continuum field strength** $F_{\mu\nu}(x)$ as the coarse-graining of discrete holonomy around small loops.
3. **The continuum covariant derivative** $D_\mu = \partial_\mu + igA_\mu$ from the discrete vertex-anchored commitment vertex under coarse-graining.
4. **The continuum local gauge transformation law** as the substrate-level gauge-quotient invariance preserved under coarse-graining.

Alternative limits — non-local, non-connection, non-tensorial, non-covariant — are each excluded by substrate-condition violation.

**A note on naming.** In the ED program's canonical terminology, DCGT abbreviates the **Diffusion Coarse-Graining Theorem** (Arc D, closed 2026-04-30), a general substrate-to-continuum bridge covering scalar diffusion, directional viscosity, V1-kernel hyperviscosity, V5-kernel viscoelastic memory, and gauge-sector minimal coupling. The "Discrete-to-Continuum Gauge Translation" terminology of the present paper's title refers to DCGT's gauge-sector application — the specific result that gauge-rule-type participation measures coarse-grain to the standard continuum gauge structure. Both expansions refer to the same theorem and the same forcing chain; the present paper focuses on the gauge-sector content.

**Series context.** Papers #1-#4 cover the kinematic and dynamical backbone of non-relativistic quantum mechanics. Paper #5 establishes substrate-level discrete gauge structure. Paper #6 covers Hamiltonian form and mass. Paper #7 extends to relativistic spin-$\tfrac12$ with $g = 2$. The present paper closes the substrate-to-continuum gauge bridge, supplying the continuum content on which all gauge-coupled empirical predictions rest.

---

## 2. Claim

> **Forcing Theorem (DCGT, gauge sector, conditional on substrate primitives + hydrodynamic-window).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Paper #5 discrete gauge-rule-type structure, plus hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$*. Then the discrete substrate gauge content coarse-grains uniquely to the standard continuum gauge structure $(A_\mu, F_{\mu\nu}, D_\mu)$ with the standard local-gauge transformation laws.
>
> *The hydrodynamic-window assumption is load-bearing. Outside its applicability, discrete substrate content is fundamental and continuum gauge fields are not defined.*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated substrate axioms)

This paper takes the following inputs as **postulated**:

- **Hydrodynamic-window scale separation (HYD):** $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. Empirically robust at all observed scales; required for DCGT applicability. In regimes where this separation fails (Planck-scale curvature, $L_\mathrm{flow} \sim \ell_P$), the bridge does not apply and discrete substrate content is fundamental.
- **Paper #5 discrete gauge-rule-type structure:** provides the substrate-level discrete connection content.
- **DCGT regularity assumptions (Arc D):** standard smoothness and boundedness conditions on the coarse-graining kernel, inherited from Arc D's closure.

The full 13-primitive substrate axiom set is enumerated in the ED Foundations position paper. The empirical case for the postulates rests on their downstream reach across domains. This paper's contribution: given the postulates above, the discrete substrate gauge content coarse-grains uniquely to the standard continuum gauge structure $(A_\mu, F_{\mu\nu}, D_\mu)$ with the standard local-gauge transformation laws.

### 3.1 What is FORCED

- The **continuum gauge potential** $A_\mu(x)$ as a smooth (in the hydrodynamic-window sense) Lie-algebra-valued one-form on the four-dimensional event manifold.
- The **continuum field strength** $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]$ as the antisymmetric tensor produced by the small-loop holonomy coarse-graining.
- The **continuum covariant derivative** $D_\mu = \partial_\mu + igA_\mu$ as the substrate vertex-anchored commitment vertex's continuum limit.
- The **local gauge transformation law** $A_\mu \to UA_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$ for smooth $U(x)$ in the gauge group, with $F_{\mu\nu}$ transforming covariantly.
- The **hydrodynamic-window scale-separation requirement** $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ as the structural condition under which the substrate-to-continuum bridge applies.

### 3.2 What is INHERITED

- **The specific gauge group** (U(1) for electromagnetism, SU(2)×U(1) for electroweak, SU(3) for QCD). Inherited from value-layer empirical input; Paper #5 forces the *admissible class* (compact simple Lie groups + their products) but not the specific member.
- **Coupling constants** $g$, $e$, $g_s$, etc. Inherited.
- **V1 kernel-profile coefficients** entering the coarse-graining error bounds. Inherited from substrate kernel-profile data.
- **Specific labeling of basis vectors** in the gauge algebra. A representation choice.

### 3.3 What is OUT OF SCOPE

- **Full Standard Model**. Specific SU(3)×SU(2)×U(1) content, matter representations, generation count, and Higgs sector are value-layer empirical.
- **Renormalization and running couplings**. The QFT machinery operating downstream of the bare substrate-derived structure is not addressed here.
- **Quantum anomalies**. Anomalies (chiral, conformal, gravitational) arise from regularization-dependent loop content beyond the tree-level substrate forcing of this paper.
- **Gravity / curved-spacetime gauge fields**. Gauge fields on curved backgrounds belong to the ED-program's substrate-gravity sector.
- **Non-perturbative gauge dynamics** (confinement, instantons, monopoles). The forcing argument establishes the perturbative kinematic content; non-perturbative phenomena require additional substrate content.

---

## 4. Key Vocabulary

For the reader new to Event Density:

- **Substrate.** Pre-quantum primitive structural layer underlying the ED framework.
- **Participation graph.** Discrete graph-like structure underlying the substrate; chains participate at vertices.
- **Rule-type.** Substrate primitive class of channel structure (Paper #5). Gauge fields are participation measures of a rule-type $\tau_g$.
- **Discrete polarity transport.** The substrate-level operation by which polarity values at one locus are transported to a neighboring locus along an edge of the participation graph.
- **Holonomy.** The composition of polarity-transport operations around a closed loop. At the substrate level, holonomy is a discrete group element; at the continuum level, it integrates to $\exp(\oint A_\mu dx^\mu)$.
- **Hydrodynamic window.** The scale range $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ separating substrate scale $\ell_P$, coarse-graining scale $R_\mathrm{cg}$, and macroscopic flow scale $L_\mathrm{flow}$. The structural condition under which DCGT applies.
- **Coarse-graining operator $\langle\cdot\rangle_{R_\mathrm{cg}}$.** Spatial-averaging operation that converts substrate-level discrete fields to continuum fields by integrating over hydrodynamic-window cells.
- **DCGT (Diffusion Coarse-Graining Theorem).** Arc D's substrate-to-continuum bridge theorem. Covers scalar diffusion, viscosity, R1 hyperviscosity, V5 viscoelastic memory, and gauge-sector minimal coupling.
- **Gauge potential $A_\mu$.** Continuum Lie-algebra-valued one-form; the participation measure of $\tau_g$ at hydrodynamic scale.
- **Field strength $F_{\mu\nu}$.** Continuum curvature of the gauge connection; $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]$.
- **Covariant derivative $D_\mu$.** $\partial_\mu + igA_\mu$ acting on charged matter fields.

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying:

### C1. Discrete participation graph (Primitives P03 + P07)

The substrate is a discrete participation graph $G = (V, E)$ with vertex set $V$ (loci) and edge set $E$ (participation relations). Channels and discrete commitment events live on this graph.

### C2. Substrate length scale $\ell_P$

The graph has a characteristic edge length $\ell_P$ — the substrate length scale, identified with the Planck length under the substrate-gravity arc's Newton-recovery argument. The substrate is *not* infinitely fine; it has primitive discreteness at scale $\ell_P$.

### C3. Polarity (Primitive P09)

$U(1)$-valued angular primitive on each channel, lifted to Lie-algebra-valued for non-Abelian gauge rule-types (Paper #5 §7.3).

### C4. Vertex-anchored commitment events (Primitive P11)

Discrete commitment events at substrate vertices. Each event involves a specific locus + a specific channel + a phase update under the gauge-rule-type's transport rule.

### C5. Gauge rule-type $\tau_g$ from Paper #5

The substrate supplies a gauge rule-type $\tau_g$ whose participation measure carries the gauge content. By Paper #5, $\tau_g$ has:
- A non-Abelian-capable Lie-algebra-valued participation measure (compact simple Lie group with Killing-form / Jacobi closure).
- Vertex-anchored minimal-coupling structure (single bilinear vertex per matter-gauge pair).
- Discrete field strength as the commutator of transported phases around small substrate plaquettes.
- Local gauge-quotient invariance: structurally-identical configurations are not distinguished by the substrate.

### C6. Hydrodynamic-window scale separation

The forcing argument applies in the scale regime
$$
\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow},
$$
where $\ell_P$ is the substrate scale (C2), $R_\mathrm{cg}$ is the coarse-graining cell radius, and $L_\mathrm{flow}$ is the macroscopic gradient scale of the continuum gauge field. The lower bound suppresses substrate-discreteness fluctuations (statistical-regularity condition); the upper bound preserves field gradients (gradient-expansion-truncation validity).

This is a *scope condition*, not a structural assumption: the forcing applies within the hydrodynamic window, with explicit error bounds at $\mathcal{O}((\ell_P / L_\mathrm{flow})^2)$ on the truncated higher-order expansion.

### C7. Inherited results from Papers #1-#7

The participation measure, Born rule, sesquilinear inner product, Schrödinger dynamics, gauge-rule-type structure, Hamiltonian/mass framework, and relativistic spinor structure are all available as inputs from prior papers. A reader who has not read Papers #1-#7 may take these as definitional premises.

### C8. No continuum gauge structure as input

The forcing argument invokes only C1-C7 plus the following standard mathematical infrastructure:

- Multi-scale expansion / homogenization theory.
- Standard differential-geometric machinery for connections and curvatures on principal bundles (used only to identify the resulting continuum objects; not assumed as input).
- The Baker-Campbell-Hausdorff formula for composition of small-parameter Lie group elements.
- Standard Taylor expansion in the small parameter $\ell_P / L_\mathrm{flow}$.

No continuum gauge potential, field strength, covariant derivative, or local gauge transformation law is assumed; all are produced by the coarse-graining chain.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. No continuum limit / discrete-only gauge theory.** The substrate's discrete gauge structure does not admit a smooth continuum limit. Gauge fields remain inherently discrete at all scales.

**A2. Non-local continuum limits.** The continuum gauge field $A_\mu(x)$ is defined as an integral over an extended substrate region rather than a local cell-averaged quantity — for instance, a Fourier-modes-only definition without a real-space cell average.

**A3. Non-connection continuum limits.** The continuum gauge field exists but does not satisfy the parallel-transport composition law required of a connection — for instance, a field strength defined independently of any gauge potential, with no underlying connection.

**A4. Non-tensorial continuum objects.** The continuum gauge field has indices that do not transform as a tensor under coordinate changes: scalar gauge field, pseudo-vector gauge field, or other non-standard transformation properties.

**A5. Non-covariant continuum limits.** The continuum field strength is defined via $\partial_\mu A_\nu - \partial_\nu A_\mu$ but lacks the non-Abelian $[A_\mu, A_\nu]$ term, breaking gauge covariance for non-Abelian groups.

**A6. Non-minimal continuum coupling.** The continuum covariant derivative is not $\partial_\mu + igA_\mu$ but contains extra non-minimal terms (Pauli-class moments, anomalous magnetic moments at the bare level, contact interactions).

**A7. Different hydrodynamic-window scaling.** The substrate-to-continuum limit is taken in a different scaling regime than $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ — e.g., direct $\ell_P \to 0$ without intermediate cell-averaging, or $R_\mathrm{cg} \sim L_\mathrm{flow}$ without scale separation.

### 6.2 Mainstream alternatives

**B1. Continuum gauge fields as postulate.** The continuum gauge structure $(A_\mu, F_{\mu\nu}, D_\mu)$ is adopted as fundamental in standard QFT, with no underlying substrate. Maxwell and Yang-Mills equations are basic axioms.

**B2. Lattice gauge theory.** Discrete plaquette variables $U_p \in G$ on a hypercubic lattice with lattice spacing $a$; continuum limit $a \to 0$ taken as a regularization. Wilson's loop variables and the continuum identification are verified but not derived from a substrate.

**B3. Fiber-bundle gauge theory.** Connections and curvatures defined abstractly on principal $G$-bundles over spacetime; the continuum-vs-discrete question does not arise within the formalism. The bundle structure is mathematical input.

**B4. Loop quantum gravity-style discrete connections.** Spin networks and holonomy variables as fundamental; continuum spacetime emergent. The discrete structure is postulated; the emergence mechanism is a separate research problem.

**B5. Non-commutative geometry continuum limits.** Gauge fields on non-commutative manifolds with deformation-quantization continuum limits. Specific commutator-deformation structure is mathematical input.

**B6. String-theoretic gauge fields.** Gauge fields arising as low-energy effective descriptions of string excitations. The string-theoretic substrate is itself a postulate; the continuum limit is taken within the string formalism.

---

## 7. Constructive Necessity

The argument establishes the substrate-to-continuum gauge bridge in five steps. The chain is a specialization of the broader DCGT (Arc D) to the gauge sector.

### 7.1 The hydrodynamic-window coarse-graining operator

Define the **spatial coarse-graining operator** on a substrate-level field $f$ as
$$
\langle f \rangle_{R_\mathrm{cg}}(x) := \frac{1}{|\Omega(x, R_\mathrm{cg})|}\int_{\Omega(x, R_\mathrm{cg})} f(x + \delta)\,d^4\delta,
$$
where $\Omega(x, R_\mathrm{cg})$ is a four-dimensional spacetime cell of characteristic size $R_\mathrm{cg}$ centered at $x$ on the emergent continuum manifold, and the integral is over the discrete substrate vertices within the cell, suitably interpolated as a continuum integral in the limit $R_\mathrm{cg} \gg \ell_P$.

**Hydrodynamic-window admissibility (C6):** $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. The lower bound ensures the cell contains $(R_\mathrm{cg}/\ell_P)^4 \gg 1$ substrate vertices, sufficient for statistical regularity. The upper bound ensures the cell is small compared to the macroscopic field gradient scale, so that gradient expansion truncation is valid.

The coarse-graining operator commutes with spatial and temporal derivatives at leading order:
$$
\partial_\mu \langle f \rangle_{R_\mathrm{cg}} = \langle \partial_\mu f \rangle_{R_\mathrm{cg}} + \mathcal{O}(\ell_P/L_\mathrm{flow}).
$$

This is the structural object that converts substrate-level discrete fields to continuum fields.

### 7.2 Continuum gauge potential from discrete polarity transport

By Paper #5 §7.3, the discrete substrate supplies, for each edge $\langle u, u' \rangle$ of the participation graph, a polarity-transport operator
$$
U_{u \to u'} = \exp(ig A^{(\mathrm{disc})}(u, u') \cdot \ell_P) \in G,
$$
where $A^{(\mathrm{disc})}(u, u')$ is the discrete Lie-algebra-valued connection on the edge and $\ell_P$ is the substrate edge length. For an infinitesimal continuum displacement $dx^\mu$, the discrete-to-continuum identification at hydrodynamic scale is
$$
U_{x \to x + dx} = \exp(ig A_\mu(x) dx^\mu) + \mathcal{O}((\ell_P/L_\mathrm{flow})^2),
$$
with
$$
A_\mu(x) = \langle A^{(\mathrm{disc})}_\mu \rangle_{R_\mathrm{cg}}(x).
$$

This is the **continuum gauge potential**: the hydrodynamic-window coarse-graining of the discrete substrate connection. $A_\mu(x)$ is a Lie-algebra-valued one-form on the four-dimensional emergent continuum manifold, with Lorentz-covariant transformation properties inherited from the substrate's underlying spacetime structure.

The coarse-graining produces a smooth continuum field from discrete substrate data; smoothness at scale $L_\mathrm{flow}$ is guaranteed by the upper bound $R_\mathrm{cg} \ll L_\mathrm{flow}$, which preserves field gradients up to error $\mathcal{O}(\ell_P/L_\mathrm{flow})$.

### 7.3 Continuum field strength from discrete holonomy

Consider a small substrate plaquette spanned by edges $\langle u, u + \ell_P\hat\mu \rangle$ and $\langle u, u + \ell_P\hat\nu \rangle$ at a vertex $u$. The discrete holonomy around this plaquette is
$$
W_{\mu\nu}^{(\mathrm{disc})}(u) = U_{u + \ell_P\hat\mu \to u + \ell_P\hat\mu + \ell_P\hat\nu}\,U_{u \to u + \ell_P\hat\mu}\,U_{u + \ell_P\hat\nu \to u}^{-1}\,U_{u + \ell_P\hat\mu + \ell_P\hat\nu \to u + \ell_P\hat\nu}^{-1}.
$$
Expanding each transport operator using $U_l = \exp(ig A_l \ell_P)$ and the Baker-Campbell-Hausdorff formula, retaining terms to second order in $\ell_P$:
$$
W_{\mu\nu}^{(\mathrm{disc})}(u) = \exp\left(ig\ell_P^2 F_{\mu\nu}(u) + \mathcal{O}(\ell_P^3)\right),
$$
with
$$
F_{\mu\nu}(u) = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu].
$$
(The $[A_\mu, A_\nu]$ commutator term arises from the BCH expansion when $A_\mu$ and $A_\nu$ do not commute, i.e., for non-Abelian gauge groups.)

Coarse-graining at hydrodynamic scale:
$$
F_{\mu\nu}(x) = \frac{1}{ig\ell_P^2}\,\langle \log W_{\mu\nu}^{(\mathrm{disc})}\rangle_{R_\mathrm{cg}}(x) + \mathcal{O}(\ell_P/L_\mathrm{flow}).
$$

This is the **continuum field strength**: the small-loop holonomy of the discrete substrate connection, coarse-grained to the hydrodynamic window. The form is exactly the standard Yang-Mills field strength:
$$
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu].
$$

Gauge covariance: under a substrate-level local gauge transformation $A^{(\mathrm{disc})}_\mu \to U A^{(\mathrm{disc})}_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$ at the substrate scale (smoothly varying at scale $L_\mathrm{flow}$), $W_{\mu\nu}^{(\mathrm{disc})}$ transforms covariantly: $W_{\mu\nu}^{(\mathrm{disc})}(u) \to U(u) W_{\mu\nu}^{(\mathrm{disc})}(u) U(u)^{-1}$. Coarse-graining preserves this: $F_{\mu\nu}(x) \to U(x) F_{\mu\nu}(x) U(x)^{-1}$ — the standard covariant transformation.

### 7.4 Continuum covariant derivative from the discrete commitment vertex

Paper #5 §7.5 establishes that the substrate-level matter-gauge interaction is a **vertex-anchored commitment vertex** — a single bilinear coupling per matter-gauge rule-type pair, occurring at a specific substrate locus. For a charged matter chain at locus $u$, the discrete commitment-vertex contribution to the chain's evolution is
$$
\Psi(u + \ell_P\hat\mu) = U_{u \to u + \ell_P\hat\mu}\,\Psi(u) = e^{ig A^{(\mathrm{disc})}_\mu \ell_P}\,\Psi(u).
$$

In the infinitesimal-step limit $\ell_P \to 0$ at the hydrodynamic scale, this is
$$
\Psi(x + dx) = \Psi(x) + ig A_\mu(x)\,\Psi(x)\,dx^\mu + \partial_\mu \Psi(x)\,dx^\mu + \mathcal{O}(\ell_P/L_\mathrm{flow}).
$$
The matter field's continuum derivative along the gauge-coupled path is therefore
$$
\frac{D\Psi}{dx^\mu} = \partial_\mu\Psi + ig A_\mu \Psi = D_\mu \Psi,
$$
with
$$
D_\mu = \partial_\mu + ig A_\mu(x).
$$

This is the **continuum covariant derivative**: the hydrodynamic-window coarse-graining of the substrate vertex-anchored commitment vertex.

Minimal coupling — the absence of non-minimal terms in $D_\mu$ — is preserved from the substrate (Paper #5 §7.5): the substrate supplies a single vertex per matter-gauge pair, and coarse-graining over the hydrodynamic window does not introduce additional terms within the truncated multi-scale expansion. Non-minimal terms would arise only at sub-leading order $\mathcal{O}(\ell_P^2/L_\mathrm{flow}^2)$ in the expansion — beyond the hydrodynamic-window scope.

### 7.5 Local gauge symmetry from the substrate gauge-quotient

The substrate gauge-quotient invariance (Paper #5 §7.6) states that structurally-identical gauge configurations are not distinguished by the substrate. At the discrete level, this means
$$
A^{(\mathrm{disc})}_\mu(u) \sim U(u)\,A^{(\mathrm{disc})}_\mu(u)\,U(u)^{-1} - (i/g)(\partial_\mu U(u))\,U(u)^{-1}
$$
for any substrate-level local gauge transformation $U(u) \in G$ varying with the substrate vertex $u$.

Under coarse-graining, smooth-at-scale-$L_\mathrm{flow}$ local gauge transformations $U(x)$ commute with the cell-averaging operator at leading order:
$$
\langle U(u)\,A^{(\mathrm{disc})}(u)\,U(u)^{-1}\rangle_{R_\mathrm{cg}} = U(x)\,\langle A^{(\mathrm{disc})}\rangle_{R_\mathrm{cg}}(x)\,U(x)^{-1} + \mathcal{O}(\ell_P/L_\mathrm{flow}).
$$

The substrate-level gauge-quotient therefore lifts directly to a **continuum local gauge symmetry**:
$$
A_\mu(x) \to U(x)\,A_\mu(x)\,U(x)^{-1} - \frac{i}{g}(\partial_\mu U(x))\,U(x)^{-1},
$$
$$
F_{\mu\nu}(x) \to U(x)\,F_{\mu\nu}(x)\,U(x)^{-1},
$$
$$
\Psi(x) \to U(x)\,\Psi(x), \qquad D_\mu\Psi(x) \to U(x)\,D_\mu\Psi(x).
$$

The continuum gauge transformation law is forced by the substrate's gauge-quotient invariance plus coarse-graining; no separate axiom is imposed.

The composite result of §§7.1-7.5: the standard continuum gauge structure $(A_\mu, F_{\mu\nu}, D_\mu)$ with the standard local gauge transformation laws is the unique hydrodynamic-window coarse-graining of the substrate-level discrete gauge content. Form FORCED; specific gauge group and coupling constants INHERITED.

---

## 8. Exclusion Arguments

### 8.1 A1 — No continuum limit / discrete-only gauge theory

The hydrodynamic-window scale separation (C6) is a structural condition: in the regime $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$, the substrate's discrete content cell-averages to a smooth continuum field with error $\mathcal{O}(\ell_P/L_\mathrm{flow})$. A claim that no continuum limit exists would have to deny C6 — denying that any scale-separation regime obtains. Empirically, gauge fields exhibit smooth behavior at scales $\gg \ell_P$ (laboratory-scale experiments on electromagnetic and Yang-Mills phenomena), confirming the existence of the hydrodynamic window. C6 holds; continuum limits exist.

### 8.2 A2 — Non-local continuum limits

A non-local definition of $A_\mu(x)$ as an integral over extended substrate regions (rather than a cell-averaged local quantity) violates the locality requirement of vertex-anchored commitment events (C4). The substrate-level commitment vertex is local (Paper #5 §7.5); coarse-graining preserves locality at leading order ($\partial_\mu$ commutes with $\langle\cdot\rangle_{R_\mathrm{cg}}$ up to $\mathcal{O}(\ell_P/L_\mathrm{flow})$). Non-local continuum limits would require non-local substrate-level structure, which the participation graph (C1) does not supply.

### 8.3 A3 — Non-connection continuum limits

A continuum field strength defined without an underlying connection violates the substrate-level polarity-transport structure (C5). The discrete substrate connection is the polarity-transport rule (Paper #5 §7.3); the field strength is the holonomy of this connection (§7.3 above). A continuum field strength existing independently of a connection has no substrate origin: there is no substrate-level discrete object that coarse-grains to a connection-less field strength.

Furthermore, the parallel-transport composition law $U_{\gamma_1 \circ \gamma_2} = U_{\gamma_1} U_{\gamma_2}$ is a substrate-level structural fact (Paper #5 §7.2). Coarse-graining preserves the composition law in the limit; a non-connection continuum object would violate this composition. C5 forbids it.

### 8.4 A4 — Non-tensorial continuum objects

The Lorentz-vector index structure of the discrete substrate connection $A^{(\mathrm{disc})}_\mu(u)$ is preserved by coarse-graining: $\langle A^{(\mathrm{disc})}_\mu\rangle_{R_\mathrm{cg}}$ inherits the Lorentz-vector transformation properties from the substrate-level four-vector structure of the participation graph (the substrate's emergent four-dimensional event manifold has Lorentz symmetry, established in Paper #7's relativistic-extension scope). Non-tensorial continuum objects would have to arise from non-tensorial substrate objects, which the participation-graph structure does not supply.

### 8.5 A5 — Non-covariant continuum limits

The non-Abelian commutator term $[A_\mu, A_\nu]$ in the continuum field strength is forced by the Baker-Campbell-Hausdorff expansion of small-loop holonomy (§7.3 above). When $A_\mu$ and $A_\nu$ do not commute (non-Abelian gauge group), the BCH expansion produces the commutator term as a *necessary* consequence of multiplying group elements; it cannot be omitted without breaking the group structure.

Equivalently: gauge covariance under non-Abelian transformations requires the field strength to transform as $F_{\mu\nu} \to U F_{\mu\nu} U^{-1}$. The bare derivative $\partial_\mu A_\nu - \partial_\nu A_\mu$ alone does not transform covariantly under non-Abelian $U(x)$; the commutator term is required to make the total expression covariant. C5 (substrate gauge-quotient invariance under non-Abelian local transformations) lifts to require the commutator term in the continuum.

### 8.6 A6 — Non-minimal continuum coupling

Non-minimal terms (Pauli moments $\sigma^{\mu\nu}F_{\mu\nu}$, contact interactions) at the bare continuum level would require additional substrate-level vertices unsupported by C4's single-vertex commitment primitive. Paper #5 §7.5 establishes that the substrate supplies one matter-gauge vertex per rule-type pair; coarse-graining preserves this single-vertex structure at leading order. Non-minimal couplings can arise as effective field-theory terms at sub-hydrodynamic scales (integrated-out heavy sectors), but they are not substrate-level forced structure.

### 8.7 A7 — Different hydrodynamic-window scaling

Direct $\ell_P \to 0$ without intermediate cell-averaging produces an ill-defined limit: substrate-discreteness fluctuations dominate at scales $R_\mathrm{cg} \sim \ell_P$, and the limit fails to converge. The scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ is structurally necessary for the multi-scale expansion to truncate at leading order with controllable errors.

Direct $R_\mathrm{cg} \sim L_\mathrm{flow}$ without scale separation produces a different ill-defined limit: gradient expansion fails because the cell-averaged field varies appreciably across the cell. Gauge-field smoothness at hydrodynamic scale requires preserving the upper bound.

C6's scale-separation requirement is forced by the structure of the multi-scale expansion itself.

### 8.8 B1 — Continuum gauge fields as postulate

Continuum gauge fields adopted as fundamental in standard QFT are *downstream* of the substrate forcing chain. Paper #5 establishes substrate-level discrete gauge content; the present paper coarse-grains it to continuum content matching the standard Maxwell/Yang-Mills formalism. Postulating the continuum structure rather than deriving it from substrate is a presentation choice; the substrate-conditions test forces the structure regardless.

### 8.9 B2 — Lattice gauge theory

Lattice gauge theory operates at a *chosen* lattice spacing $a$ as a regularization, with the continuum limit taken via $a \to 0$. The lattice is a tool, not a substrate. Under the substrate-conditions test, lattice gauge theory is a regularization of the same continuum content the substrate forces — specifically, lattice gauge theory at scale $a \sim R_\mathrm{cg}$ approximates the hydrodynamic-window coarse-graining of the substrate, with $\ell_P$ implicit in the lattice's structural primitives.

Lattice and substrate are not competing; the substrate provides the *physical* basis for what lattice gauge theory implements as a *mathematical* regularization. Both arrive at the same continuum content.

### 8.10 B3 — Fiber-bundle gauge theory

Fiber-bundle formulations are the *mathematical language* of continuum gauge theory. The connection 1-form, the curvature 2-form, the principal bundle structure — all are abstract objects on which gauge theory is built. Under the substrate-conditions test, fiber-bundle theory is the appropriate language for the *forced result*: the substrate produces a continuum gauge field that *is* a connection on an emergent principal bundle. The bundle structure is itself coarse-grained from substrate-level discrete gauge data.

The substrate is *upstream* of the fiber-bundle formalism; the fiber-bundle theory is the right mathematical apparatus for handling the forced continuum structure but is not an alternative to it.

### 8.11 B4 — Loop quantum gravity / spin network connections

Loop quantum gravity uses discrete connection variables (holonomies, spin networks) as fundamental kinematic objects. Continuum spacetime is emergent. Under the substrate-conditions test, LQG-style discrete connections are *parallel* to ED's substrate-level discrete gauge content: both treat the discrete level as fundamental and aim to recover continuum content. The specific kinematic structures differ (spin networks vs. ED's participation graph + rule-types), and the emergence mechanisms differ (LQG's semiclassical limit + spin-foam dynamics vs. ED's hydrodynamic-window coarse-graining). Whether the two programs are compatible at the continuum level is an open structural question; they are not in direct competition for the present paper's forcing claim.

### 8.12 B5 — Non-commutative geometry continuum limits

Non-commutative gauge theory uses deformation-quantization of continuum manifolds rather than discrete substrates. Under the substrate-conditions test, NCG is operating in a different framework: the deformation parameter $\theta$ is a continuum-level structure, not a substrate-derived quantity. ED's substrate-level discrete structure is fundamentally different from non-commutative deformation; the two are not directly comparable as substrate-to-continuum forcings.

### 8.13 B6 — String-theoretic gauge fields

String theory derives gauge fields as low-energy effective descriptions of string excitations on specific background geometries. The string-theoretic substrate is itself a postulate (the worldsheet conformal field theory, string tension, target-space geometry). Under the substrate-conditions test, string-theoretic gauge fields are downstream of a different choice of pre-quantum substrate; ED's substrate is participation-graph + rule-type-class, whereas string theory's substrate is worldsheet CFT. The two are competitor frameworks at the substrate level; the present paper's forcing chain applies to the ED substrate.

### 8.14 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 no continuum limit | C6 | Hydrodynamic window exists empirically; substrate cell-averages to continuum. |
| A2 non-local limit | C4 | Vertex-anchored commitment is local; locality preserved by coarse-graining. |
| A3 non-connection limit | C5 | Discrete connection's parallel-transport composition lifts to continuum. |
| A4 non-tensorial objects | substrate Lorentz structure | Coarse-graining inherits substrate four-vector index transformation. |
| A5 non-covariant (missing $[A_\mu, A_\nu]$) | C5 BCH expansion | Non-Abelian small-loop holonomy forces commutator term. |
| A6 non-minimal coupling | C4 | Single-vertex commitment preserved under coarse-graining. |
| A7 different scaling | C6 | Multi-scale expansion requires $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. |
| B1 continuum as postulate | not in space | Downstream of substrate; same content, different presentation. |
| B2 lattice gauge theory | regularization | Approximates substrate at $a \sim R_\mathrm{cg}$; same continuum content. |
| B3 fiber-bundle theory | mathematical language | Right language for the forced result; not an alternative substrate. |
| B4 loop quantum gravity | parallel | Different substrate (spin networks vs. participation graph); open compatibility. |
| B5 non-commutative geometry | scope-different | Deformation-quantization of continuum, not substrate-derivation. |
| B6 string gauge fields | competitor framework | Different choice of pre-quantum substrate; ED forces continuum gauge from its substrate. |

**The continuum gauge structure $(A_\mu, F_{\mu\nu}, D_\mu)$ with standard transformation laws is the unique hydrodynamic-window coarse-graining of the substrate-level discrete gauge content.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier is identical to the empirical falsifier of standard continuum gauge theory:

- **Tests of continuum gauge invariance**: precision tests of QED and the Standard Model are consistent with continuum gauge symmetry to the limits of experimental precision. Any reproducible observation of gauge-invariance violation at the kinematic level (not attributable to anomalies or symmetry-breaking) would refute the substrate-level forcing.
- **Aharonov-Bohm and topological-phase experiments**: directly test the continuum-limit holonomy $\exp(\oint A_\mu dx^\mu)$ as the predicted continuum coarse-graining of substrate-level discrete holonomy. Agreement to experimental precision confirms §7.3.
- **Yang-Mills precision tests**: the non-Abelian structure of the electroweak sector and QCD is tested in collider experiments. The $[A_\mu, A_\nu]$ commutator term in $F_{\mu\nu}$ — forced by §7.3's BCH expansion — is directly tested by tri-boson and quartic-boson vertices.
- **Minimal-coupling tests**: precision QED measurements of the electron magnetic moment (Paper #7) confirm minimal coupling at the bare-coupling level, with deviations attributed to QED radiative corrections rather than to substrate-level non-minimal structure.

If any of these were violated empirically — if continuum gauge invariance, the standard $F_{\mu\nu}$ structure, or minimal coupling failed at the bare level — the substrate-level forcing of this paper would be refuted along with standard gauge theory.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C8 (discrete participation graph with substrate scale $\ell_P$, polarity, vertex-anchored commitment, gauge rule-type from Paper #5, hydrodynamic-window admissibility, Papers #1-#7 inherited, no continuum gauge structure as input) but supporting a non-local, non-connection-based, non-tensorial, or non-covariant continuum limit that survives the exclusion arguments of §8.

The author's claim is that no such substrate exists. Each alternative is dispatched by a specific substrate-condition violation. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

Three immediate exposures:

**Electromagnetism.** Maxwell's equations follow from the variational principle applied to the gauge-invariant action $\mathcal{L} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} + J^\mu A_\mu$ on the substrate-derived continuum gauge potential. Every laboratory test of electromagnetism — from Coulomb's law to laser interferometry to synchrotron radiation — tests the continuum content produced by the substrate-to-continuum coarse-graining of this paper.

**Yang-Mills (electroweak + QCD).** The non-Abelian gauge sectors of the Standard Model are described by the same continuum structure forced here, with specific gauge groups inherited from value-layer data. Every collider experiment testing electroweak interactions or QCD scattering tests the continuum forcing.

**Berry phase and topological-phase experiments.** Holonomy around closed loops in parameter space — the geometric Berry phase — is the substrate-level signature of the continuum connection. Aharonov-Bohm experiments, molecular Berry-phase measurements, and topological-phase experiments in condensed matter directly test §7.3's coarse-graining of discrete substrate holonomy.

The substrate-level continuum-gauge forcing of this paper supports every quantitative gauge-coupled prediction in physics.

---

## Appendix A — Derivation Chain and Glossary

### A.1 Small-loop holonomy and the field strength — explicit BCH calculation

Consider a substrate plaquette at vertex $u$, spanned by infinitesimal substrate displacements $\ell_P\hat\mu$ and $\ell_P\hat\nu$. Define the four edge transports:
$$
U_1 = \exp(ig A_\mu(u)\ell_P), \quad U_2 = \exp(ig A_\nu(u + \ell_P\hat\mu)\ell_P),
$$
$$
U_3 = \exp(-ig A_\mu(u + \ell_P\hat\nu)\ell_P), \quad U_4 = \exp(-ig A_\nu(u)\ell_P).
$$
The plaquette holonomy is $W = U_4 U_3 U_2 U_1$. Expanding each factor to second order in $\ell_P$, using
$$
A_\nu(u + \ell_P\hat\mu) = A_\nu(u) + \ell_P\partial_\mu A_\nu(u) + \mathcal{O}(\ell_P^2),
$$
and applying the Baker-Campbell-Hausdorff formula $e^X e^Y = e^{X + Y + \tfrac12[X, Y] + \cdots}$ for small $X, Y$:
$$
W = \exp\left[ig\ell_P^2(\partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]) + \mathcal{O}(\ell_P^3)\right].
$$

Reading off the coefficient of $\ell_P^2$ in the exponent:
$$
F_{\mu\nu}(u) = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu].
$$

This is the standard Yang-Mills field strength. The commutator term is forced by the non-commutativity of group elements in the non-Abelian case; for U(1), the commutator vanishes and $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ reduces to the Abelian (Maxwell) form.

Coarse-graining at hydrodynamic scale: $F_{\mu\nu}(x) = \langle F_{\mu\nu}^{(\mathrm{disc})}\rangle_{R_\mathrm{cg}}(x)$, with error $\mathcal{O}(\ell_P/L_\mathrm{flow})$ on the truncated higher-order multi-scale expansion.

### A.2 Multi-scale expansion of the coarse-graining operator

For a smooth-at-scale-$L_\mathrm{flow}$ continuum field $f(x)$, the cell-averaging operator admits the expansion
$$
\langle f \rangle_{R_\mathrm{cg}}(x) = f(x) + \frac{R_\mathrm{cg}^2}{6}\nabla^2 f(x) + \mathcal{O}(R_\mathrm{cg}^4/L_\mathrm{flow}^4),
$$
where the $\nabla^2$ correction arises from the second moment of the cell-volume distribution (assuming isotropic cells; analogous expansions hold for anisotropic averaging). The leading-order identity $\langle f \rangle = f$ in the hydrodynamic-window scope produces the basic substrate-to-continuum correspondence; the $\nabla^2$ correction supplies the V1-kernel-induced hyperviscous + diffusion terms in the broader DCGT (Arc D, scalar/directional sectors).

For the gauge sector, the leading-order identity gives $A_\mu(x) = \langle A^{(\mathrm{disc})}_\mu\rangle_{R_\mathrm{cg}}(x)$ + error; the $\nabla^2$ correction contributes sub-leading corrections to the field strength that are below the hydrodynamic-window scope.

### A.3 Glossary

- **Bandwidth $b_K(u)$.** Primitive non-negative real-valued substrate quantity on each channel.
- **Channel.** Primitive structural pathway in the participation graph.
- **Coarse-graining operator $\langle\cdot\rangle_{R_\mathrm{cg}}$.** Spatial cell-averaging at scale $R_\mathrm{cg}$.
- **Connection.** Lie-algebra-valued one-form encoding parallel transport on the participation manifold; the gauge potential.
- **Covariant derivative $D_\mu$.** $\partial_\mu + ig A_\mu$; the gauge-invariant derivative.
- **Curvature $F_{\mu\nu}$.** $\partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]$; the field strength.
- **DCGT (Diffusion Coarse-Graining Theorem).** Arc D's substrate-to-continuum bridge theorem. The present paper covers DCGT's gauge sector.
- **Discrete polarity transport.** Substrate-level transport of polarity along a participation-graph edge: $U_{u \to u'} = \exp(ig A^{(\mathrm{disc})}\ell_P)$.
- **FORCED.** Derived from substrate primitives + standard mathematics with no additional commitments.
- **Gauge potential $A_\mu$.** Continuum Lie-algebra-valued one-form.
- **Gauge rule-type $\tau_g$.** Substrate primitive class of channel structure whose participation measure is the gauge potential (Paper #5).
- **Hydrodynamic window.** Scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$.
- **Holonomy.** Phase / group element acquired by parallel transport around a closed loop.
- **INHERITED.** Specific gauge group, coupling constants, kernel coefficients — not derived in this paper.
- **Minimal coupling.** Single bilinear matter-gauge vertex via $\partial \to D$; preserved from Paper #5.
- **Participation graph.** Discrete graph-like structure underlying the substrate.
- **Rule-type.** Substrate primitive class of channel structure (Paper #5).
- **Substrate.** Pre-quantum primitive structural layer.
- **Substrate length scale $\ell_P$.** Characteristic edge length of the participation graph.
- **Vertex-anchored commitment.** Substrate-level commitment event at a specific locus; the location of the matter-gauge interaction.

### A.4 Source-repository citations (for ED-internal readers)

- `theory/Arc_D/Arc_D_5_Minimal_Coupling_Coarse_Graining.md` — Arc D Memo 5: substrate-to-continuum gauge minimal coupling (Lorentz force derivation, T17 coarse-graining).
- `theory/Arc_D/Arc_D_6_Synthesis_And_Theorem.md` — Arc D synthesis memo with the canonical DCGT theorem statement and proof sketch.
- `theory/Arc_D/Arc_D_1_Opening.md` through `Arc_D_4_Kernel_Coarse_Graining.md` — the four substrate-derivation memos covering scalar diffusion, directional viscosity, V1/V5 kernel coarse-graining; companions to the gauge sector.
- `walkthroughs/from_primitives_to_dcgt.md` — public-facing walkthrough.
- `papers/Navier Stokes_Synthesis_Paper/NS_Synthesis_Appendix_D_DCGT_Integration.md` — Appendix D of the NS Synthesis Paper integrating DCGT.
- `theorems/T17.md` — Theorem 17 (gauge-fields-as-rule-type), the substrate-level antecedent of this paper.

These are *not* required reading for the present paper.

---

*End of Paper #8.*
