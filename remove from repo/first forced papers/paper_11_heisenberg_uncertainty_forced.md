# The Heisenberg Uncertainty Relation $\Delta x\,\Delta p \geq \hbar/2$ is FORCED

**Paper #11 of the Event Density Forcing Series (Wave 2, Paper 1)**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) Forcing Papers — Paper #11 of the program
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The Heisenberg uncertainty relation $\Delta x\,\Delta p \geq \hbar/2$ is normally presented as a theorem about Fourier transforms on Hilbert space, or as an operator-algebraic identity following from $[\hat{x},\hat{p}] = i\hbar$. This paper shows that, **given the substrate primitives of Papers #1–#4 plus the four-band partition (P04 §1.5), specifically its primitive adjacency-band content with Fourier-conjugate $b_x$ / $b_p$ structure**, the uncertainty relation is recovered at the substrate level via the bandwidth-allocation inequality, with the standard Weyl-Fourier inequality emerging as its continuum form after identifying $b_x \propto |\Psi|^2$ and $b_p \propto |\tilde\psi|^2$ via the Born rule (Paper #2). The honest framing: the mathematical content of the bound is the standard Weyl-Fourier inequality on $L^2$; ED's substantive contribution is the substrate-level locus where the inequality lives (the adjacency-band Fourier-conjugate partition is the substrate-level source of the position-momentum conjugate pair). Operator-algebraic alternatives, real-valued alternatives, and non-Fourier-conjugate alternatives are excluded by substrate-condition violation. The claim is conditional on the four-band partition primitive and on the Fourier-conjugate substrate structure of the adjacency band, which are upstream content for the Primitive-Forcing Meta-Paper.

---

## 1. Framing

### 1.1 What standard quantum mechanics assumes about the uncertainty relation

In the standard presentation, the Heisenberg uncertainty relation
$$
\Delta x\,\Delta p \geq \frac{\hbar}{2}
$$
arrives either as a theorem about the Fourier transform on $L^2(\mathbb{R})$ — the standard Weyl inequality — or as an operator-algebraic identity (Robertson 1929, Schrödinger 1930) following from the canonical commutator
$$
[\hat{x}, \hat{p}] = i\hbar.
$$
The operator-algebraic derivation goes through cleanly: for any state $|\psi\rangle$ in a Hilbert space with self-adjoint $\hat{x}$ and $\hat{p}$ satisfying $[\hat{x}, \hat{p}] = i\hbar$,
$$
(\Delta x)^2\,(\Delta p)^2 \geq \left|\frac{1}{2i}\langle [\hat{x}, \hat{p}]\rangle\right|^2 = \left(\frac{\hbar}{2}\right)^2.
$$
Equality is achieved by Gaussian wavepackets.

This derivation is technically correct and pedagogically clean. But it leaves three questions unaddressed:

1. **Why this specific bound?** The commutator $[\hat{x}, \hat{p}] = i\hbar$ is a postulate of canonical quantization. The $\hbar/2$ bound is its mathematical consequence — but where does the commutator come from?
2. **Why are position and momentum the conjugate pair?** Fourier duality singles out specific pairs of variables. Why does nature use $x$-$p$ duality rather than some other pairing?
3. **What does the uncertainty relation mean physically?** In the standard presentation, the inequality is a statistical statement about ensembles of measurements. It is treated as a *mathematical* feature of state-space structure, not as a *structural* physical requirement on the substrate.

A program that wants to settle these questions structurally needs:

1. A substrate that supplies the position-momentum conjugate pair without assuming it.
2. A structural mechanism producing the bandwidth-allocation inequality from substrate primitives.
3. An identification of the bandwidth allocation with the standard position-momentum variances of the wavefunction.

### 1.2 The puzzle

The deeper puzzle is *why nature enforces this specific lower bound*. Bandwidth-allocation inequalities are common in classical wave mechanics (e.g., the time-frequency uncertainty of signal processing), but the specific value $\hbar/2$ is what makes quantum mechanics quantum mechanics. Standard derivations either take the commutator $[\hat{x}, \hat{p}] = i\hbar$ as input (operator-algebraic route) or take the Fourier-conjugate Hilbert-space structure as input (Weyl-inequality route). In both cases the *form* of the inequality is forced by mathematics, but the *specific scale* $\hbar$ is inherited.

### 1.3 What this paper does

The Event Density (ED) framework supplies a substrate: a participation graph with a primitive **four-band decomposition** of bandwidth (Primitive 04 §1.5). The four bands — internal, adjacency, environmental, commitment-reserve — are mutually orthogonal substrate-level structural channels (used in Paper #3 §7.1.4 to derive inner-product orthogonality from substrate orthogonality).

This paper shows that the **adjacency band** of the four-band partition is the substrate-level carrier of position-momentum structure, and that its orthogonal decomposition into a position-adjacency component $b_x$ and a momentum-adjacency component $b_p$ produces the Heisenberg uncertainty relation through the substrate-level bandwidth-allocation inequality. Specifically:

1. The substrate adjacency band $b^\mathrm{adj}$ admits a Fourier-conjugate partition $b^\mathrm{adj} = b_x + b_p$.
2. The bandwidth-allocation inequality $(\Delta b_x)(\Delta b_p) \geq K_{xp}$ is forced by orthogonal-partition structure plus substrate-level bandwidth additivity.
3. Identifying $b_x(x) \propto |\Psi(x)|^2$ and $b_p(p) \propto |\tilde\psi(p)|^2$ via the Born rule (Paper #2) within each partition, the bandwidth spreads $\Delta b_x$ and $\Delta b_p$ equal the standard position and momentum variances $\Delta x$ and $\Delta p$.
4. The Fourier-uncertainty theorem, in the thin-participation limit where $\Psi$ satisfies Schrödinger (Paper #4) with $\hat{p} = -i\hbar\nabla$, forces $K_{xp} = \hbar/2$.

The Heisenberg relation $\Delta x\,\Delta p \geq \hbar/2$ is therefore a substrate-level structural consequence of the four-band partition, not a Hilbert-space mathematical theorem applied to an assumed conjugate-variable structure.

**Series context.** Papers #1-#4 forced the participation measure, Born rule, sesquilinear inner product, and Schrödinger evolution. Papers #5-#10 extended through gauge fields, mass, the Dirac equation with $g = 2$, the substrate-to-continuum bridge, substrate gravity, and the black-hole / Hawking sector. The present paper opens Wave 2 by closing the fourth foundational QM postulate — the Heisenberg uncertainty inequality — from substrate primitives. Together, Papers #1-#3 + this paper cover all four foundational QM postulates (Born, Bell-Tsirelson, Heisenberg, Schrödinger) as substrate-forced consequences.

---

## 2. Claim

> **Forcing Theorem (Heisenberg from Four-Band Partition, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#4 results plus four-band partition with adjacency-band Fourier-conjugate $b_x/b_p$ structure (P04 §1.5)*. Then the bandwidth-allocation inequality on the Fourier-conjugate adjacency-band partition, identified with $|\Psi|^2$ and $|\tilde\psi|^2$ via the Born rule, produces
> $$
> \Delta x\,\Delta p \geq \hbar/2.
> $$
>
> *The substantive contribution is the substrate-level origin of the conjugate-variable pair (the adjacency-band partition). The $\hbar/2$ value follows from the standard Weyl-Fourier inequality once $b_x \propto |\Psi|^2$ and $b_p \propto |\tilde\psi|^2$ are identified via Born — i.e., the inequality's mathematical content is standard $L^2$ Fourier analysis, with ED supplying the substrate-level locus.*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated substrate axioms)

This paper takes the following inputs as **postulated**:

- **P04 §1.5 (four-band partition) with adjacency-band Fourier-conjugate structure:** the substrate-level conjugate-variable pair $(b_x, b_p)$ within the adjacency band is the primitive carrier of position-momentum content.
- **Standard $L^2$ Weyl-Fourier inequality (Weyl 1928):** mathematical infrastructure; ED does not rederive it.
- **Papers #1–#4 results:** including Born-rule identification of $b_x \propto |\Psi|^2$ and $b_p \propto |\tilde\psi|^2$.

The full 13-primitive substrate axiom set is enumerated in the ED Foundations position paper. The empirical case for the postulates rests on their downstream reach across domains. This paper's contribution — and its honest framing: this paper does *not* derive a new uncertainty inequality. It derives the *substrate-level origin* of the standard inequality's conjugate-variable pair. The $\hbar/2$ value follows from standard $L^2$ Fourier analysis combined with the Born-rule identification. The novel content is *where the inequality lives at the substrate level* (the adjacency-band Fourier-conjugate partition), not the inequality itself.

### 3.1 What is FORCED

- The **bandwidth-allocation inequality** $(\Delta b_x)(\Delta b_p) \geq K_{xp}$ between Fourier-conjugate components of the adjacency band.
- The **Fourier-conjugate structure** of $b_x$ and $b_p$ as orthogonal substrate-level partitions.
- The **variance-form** $\Delta x\,\Delta p \geq \hbar/2$ inequality after identification with standard QM variances.
- The **specific bound** $\hbar/2$ (form), with $\hbar$ a dimensional anchor (value inherited).
- **Equality conditions**: Gaussian wavepackets saturate the bound — substrate-level minimum-uncertainty states.

### 3.2 What is INHERITED

- The **numerical value of $\hbar$**. Inherited via the dimensional-atlas Madelung anchoring (the same anchor used in Papers #4 and #6).
- The **identification** $b_x(x) \propto |\Psi(x)|^2$ within the position-adjacency partition. Follows from the Born rule (Paper #2) applied within the partition; the proportionality constant is a normalization convention.
- The **specific Cartesian basis** for $x$ and $p$. A labeling choice; the inequality holds in any rotated basis with appropriate substitution.

### 3.3 What is OUT OF SCOPE

- **Robertson-Schrödinger generalizations** to arbitrary self-adjoint operator pairs $(\hat{A}, \hat{B})$. The present paper covers the specific $x$-$p$ inequality forced by the adjacency-band partition; generalizations to other operator pairs require additional substrate structure.
- **Entropic uncertainty relations** (Maassen-Uffink, Berta et al.). Information-theoretic refinements of the standard inequality. Downstream of the present substrate forcing.
- **Relativistic uncertainty relations**. Time-energy uncertainty and relativistic generalizations involve additional structure not addressed here.
- **Measurement-disturbance uncertainty** (Ozawa, Branciard). Operational uncertainty about measurement back-action, distinct from the state-preparation uncertainty derived here.

---

## 4. Key Vocabulary

For the reader new to Event Density:

- **Substrate.** Pre-quantum primitive layer of the ED framework.
- **Channel.** Primitive structural pathway in the participation graph, indexed by $K$.
- **Participation bandwidth $b_K(u)$.** Non-negative real-valued primitive on each channel (Primitive 04).
- **Four-band partition.** Substrate-level decomposition of bandwidth into four mutually orthogonal structural bands: **internal** (sustains the chain's own rule), **adjacency** (couples to immediate participation-adjacent structure), **environmental** (couples to broader bath), and **commitment-reserve** (available for commitment events). Primitive 04 §1.5.
- **Adjacency band $b^\mathrm{adj}$.** The four-band component responsible for positional / kinematic coupling — how a chain relates to its local participation-adjacent neighborhood.
- **Position-adjacency $b_x$.** Component of $b^\mathrm{adj}$ allocated to spatial localization.
- **Momentum-adjacency $b_p$.** Component of $b^\mathrm{adj}$ allocated to phase-coherent propagation (Fourier-conjugate to $b_x$).
- **Participation manifold.** Complex Hilbert space carrying the participation measures (Paper #3).
- **Bandwidth-allocation inequality.** Substrate-level inequality on the allocation of bandwidth across orthogonal conjugate partitions.

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying:

### C1. Participation graph + channel structure (Primitives P03 + P07)

Discrete participation graph with channels at each locus.

### C2. Four-band bandwidth partition (Primitive P04 §1.5)

Non-negative bandwidth on each channel decomposes into four mutually orthogonal bands:
$$
b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com},
$$
with conservation $\sum_K b_K = b_\mathrm{total}$ along an isolated chain's persistence regime.

The four bands are *mutually orthogonal* in the participation-manifold inner product established in Paper #3: cross-band inner products vanish because the band labels correspond to disjoint structural channels at the substrate level.

### C3. Adjacency band as carrier of position-momentum structure

The adjacency band $b^\mathrm{adj}$ is, by Primitive 04 §1.5, "the participation the chain shares with its immediate participation-adjacent neighborhood." It is structurally the kinematic-coupling band: it governs how the chain relates to its local surroundings in position-like ways.

Two natural orthogonal sub-components of $b^\mathrm{adj}$:
- **Spatial proximity**: nearness to the chain's current spatial position (position-adjacency, $b_x$).
- **Phase-coherent propagation**: nearness in the phase-propagation sense (momentum-adjacency, $b_p$).

These are the two structural modes of "relating to a neighborhood" — classical-locality and Fourier-dual-locality. C3 commits the substrate to admitting both as orthogonal partitions of $b^\mathrm{adj}$.

### C4. Inherited results from Papers #1-#4

- **Paper #1**: participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$.
- **Paper #2**: Born rule $\text{Prob}(K) \propto |P_K|^2$.
- **Paper #3**: sesquilinear inner product + orthogonal-partition structure.
- **Paper #4**: Schrödinger evolution with $\hat{p} = -i\hbar\nabla$ as the spatial-translation generator.

### C5. No uncertainty relation as input

The forcing argument invokes only C1-C4 plus the following standard mathematical infrastructure:

- The Fourier-uncertainty theorem (Weyl inequality) for $L^2(\mathbb{R})$ functions and their Fourier transforms.
- The Cauchy-Schwarz inequality on inner-product spaces.
- The variance identity $(\Delta f)^2 = \langle f^2\rangle - \langle f\rangle^2$.

No canonical commutator $[\hat{x}, \hat{p}] = i\hbar$ is assumed; no Robertson-Schrödinger operator-algebraic identity is taken as input. Both are *produced* by the forcing chain (Paper #4 + the present paper) rather than assumed.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. No four-band partition.** The substrate has only a single undifferentiated bandwidth at each channel, with no internal / adjacency / environmental / commitment-reserve structure. Position-momentum conjugacy then has no substrate-level carrier.

**A2. Non-Fourier-conjugate adjacency partition.** The adjacency band partitions into two orthogonal components, but they are not Fourier-conjugate — e.g., they correspond to two independent spatial directions, or to spin-up / spin-down, or to some other orthogonal pairing.

**A3. Three or more conjugate partitions of $b^\mathrm{adj}$.** The adjacency band partitions into three or more Fourier-conjugate components rather than the two $(b_x, b_p)$. Each pair of components then has its own uncertainty relation.

**A4. Non-variance bandwidth-spread measure.** The bandwidth "spread" is defined via a non-variance functional — e.g., the support width, the entropy of the distribution, or some other localization measure incompatible with the variance identity.

**A5. Anisotropic conjugate pairs.** The position-momentum conjugacy depends on direction in space — $x$-$p_x$, $y$-$p_y$, $z$-$p_z$ are independent pairs with different $\hbar_x$, $\hbar_y$, $\hbar_z$ constants.

**A6. Different commutator structure.** A modified position-momentum commutator $[\hat{x}, \hat{p}] = i f(\hat{x}, \hat{p})$ with $f$ a non-constant function, producing a state-dependent uncertainty bound.

**A7. No bandwidth-allocation inequality.** The two adjacency partitions are independently allocatable: $b_x$ and $b_p$ can both be concentrated simultaneously, with no inequality constraint.

### 6.2 Mainstream alternatives

**B1. Heisenberg as Hilbert-space Fourier theorem.** The uncertainty relation derived as a mathematical theorem on $L^2(\mathbb{R})$, with no substrate underpinning. The Fourier-conjugate pair is taken as given.

**B2. Operator-algebraic derivation (Robertson-Schrödinger).** Heisenberg follows from the canonical commutator $[\hat{x}, \hat{p}] = i\hbar$ via the Cauchy-Schwarz inequality on Hilbert space. The commutator is the structural commitment.

**B3. Operational uncertainty (measurement-disturbance).** Heisenberg interpreted as a statement about measurement back-action: precise position measurement disturbs momentum. Ozawa's reformulation and Branciard's bounds. Distinct from state-preparation uncertainty.

**B4. Entropic uncertainty relations.** Information-theoretic refinements (Maassen-Uffink 1988; Berta et al. 2010) replacing variances with entropies. Downstream of the standard variance form.

**B5. Semiclassical / coherent-state derivations.** Uncertainty as a property of coherent-state minimum-uncertainty wavepackets in semiclassical / WKB-class arguments. Coherent states taken as input.

**B6. Decoherence-as-source models.** Uncertainty interpreted as arising from interaction with the environment producing classical-like uncertainty in the system. Decoherence dynamics taken as substrate-level mechanism.

---

## 7. Constructive Necessity

The argument establishes the Heisenberg inequality in five steps.

### 7.1 Adjacency band as position-momentum carrier

The four-band partition of substrate bandwidth (C2) supplies four mutually orthogonal bands. Of these, three are structurally inappropriate as carriers of position-momentum content:

- The **internal band** sustains the chain's rule-content (mass, statistics, internal symmetries). Not a positional / kinematic quantity.
- The **environmental band** couples to the broader bath; phase-randomized at commitment (Paper #2 §7.1, Step 4). Carries decoherence-relevant content, not kinematic locality.
- The **commitment-reserve band** depletes during commitment events. Not directly positional.

The **adjacency band** $b^\mathrm{adj}$ is the unique remaining four-band component that governs kinematic relationships to the chain's neighborhood. By C3, this is the substrate-level carrier of position-momentum content.

### 7.2 Orthogonal partition into $b_x$ and $b_p$

The adjacency band admits two structurally distinct modes of "neighborhood-coupling":

- **Spatial proximity** ($b_x$): the chain participates with adjacent spatial regions. Localization in $x$ corresponds to concentration of $b_x$ at the chain's position; spread corresponds to broad spatial extent.
- **Phase-coherent propagation** ($b_p$): the chain participates via phase-coherent channels propagating across space. Localization in $p$ corresponds to concentration of $b_p$ at a specific momentum; spread corresponds to a range of propagation modes.

These two modes are **Fourier-conjugate** at the substrate level. The structural argument:

1. Spatial proximity is characterized by the spatial coordinate $x$ — a coordinate on the participation manifold.
2. Phase-coherent propagation is characterized by the wavenumber $k = p/\hbar$ — the Fourier-conjugate variable to $x$ on the participation manifold.
3. By Paper #4 §7.2 (Stone's theorem on spatial translations, extended to the position-momentum case), $\hat{p} = -i\hbar\nabla$ is the unique self-adjoint translation generator on the participation manifold. Position and momentum are therefore canonically Fourier-conjugate.

The two sub-components of the adjacency band are orthogonal in the participation-manifold inner product (C2 four-band orthogonality applied at the sub-component level): cross-coupling between $b_x$ and $b_p$ vanishes because spatial-proximity content and phase-coherent-propagation content are structurally disjoint.

Therefore:
$$
b^\mathrm{adj} = b_x + b_p, \qquad \langle b_x, b_p\rangle = 0.
$$

### 7.3 Bandwidth-allocation inequality

For orthogonal partitions of bandwidth drawing from a common bandwidth budget, the spreads (measured as variances) satisfy a **bandwidth-allocation inequality**:
$$
(\Delta b_x)(\Delta b_p) \geq K_{xp},
$$
where $K_{xp}$ is a structural constant determined by the partition topology.

**Why an inequality exists.** Concentrating bandwidth in $b_x$ (sharp spatial localization) requires sourcing the bandwidth from somewhere; with orthogonal partitions sharing a common adjacency-band budget, the natural source is $b_p$. The Fourier-conjugate structure means that maximal concentration in $b_x$ corresponds to maximal spread in $b_p$, and vice versa.

The inequality form is forced by the same Cauchy-Schwarz argument that underlies Robertson's uncertainty inequality, applied here at the substrate-bandwidth level rather than the Hilbert-space-operator level. The Cauchy-Schwarz application uses C4's inner-product structure on the participation manifold.

### 7.4 Identification with $|\Psi|^2$ and $|\tilde\psi|^2$ via the Born rule

In the thin-participation limit where the coherent sum $\Psi(x, t) = \sum_K P_K(x, t)$ satisfies the Schrödinger equation (Paper #4), the position-probability density is $|\Psi(x)|^2$ by the Born rule (Paper #2). The substrate-level position-adjacency bandwidth $b_x$ is identified with this density:
$$
b_x(x) \propto |\Psi(x)|^2.
$$
The proportionality constant is absorbed into overall normalization.

Similarly, the momentum-probability density is $|\tilde\psi(p)|^2$, where $\tilde\psi(p)$ is the Fourier transform of $\Psi(x)$:
$$
\tilde\psi(p, t) = \frac{1}{\sqrt{2\pi\hbar}}\int \Psi(x, t)\,e^{-ipx/\hbar}\,dx.
$$
The momentum-adjacency bandwidth $b_p$ identifies with:
$$
b_p(p) \propto |\tilde\psi(p)|^2.
$$

These identifications are forced by the Born rule applied within each adjacency-partition. Under the identifications, the substrate-level bandwidth spreads equal the standard QM position-momentum variances:
$$
(\Delta b_x)^2 = \langle x^2\rangle_{|\Psi|^2} - \langle x\rangle_{|\Psi|^2}^2 = (\Delta x)^2,
$$
$$
(\Delta b_p)^2 = \langle p^2\rangle_{|\tilde\psi|^2} - \langle p\rangle_{|\tilde\psi|^2}^2 = (\Delta p)^2.
$$

### 7.5 The Fourier-uncertainty theorem forces $K_{xp} = \hbar/2$

Substituting §7.4 into §7.3's allocation inequality:
$$
\Delta x\,\Delta p \geq K_{xp}.
$$

The **Fourier-uncertainty theorem** (Weyl inequality) is a mathematical identity for $L^2(\mathbb{R})$ functions: for any $\Psi \in L^2(\mathbb{R})$ with Fourier transform $\tilde\psi$ defined as above,
$$
\Delta x\,\Delta p \geq \frac{\hbar}{2},
$$
with equality achieved by Gaussian wavepackets $\Psi(x) \propto e^{-x^2/(4\sigma^2)}$.

Comparing:
$$
K_{xp} = \frac{\hbar}{2}.
$$

The factor of $\hbar/2$ traces to the standard Fourier-transform normalization convention $\tilde\psi(p) = (2\pi\hbar)^{-1/2}\int \Psi(x)\,e^{-ipx/\hbar}\,dx$, with $\hbar$ entering as the dimensional conversion between $x$-space and $p$-space. Paper #4 establishes that this $\hbar$ is the same $\hbar$ as in the Schrödinger equation; the dimensional-atlas Madelung anchoring fixes its numerical value.

**The Heisenberg uncertainty relation $\Delta x\,\Delta p \geq \hbar/2$ is therefore forced at the substrate level** by the chain:
substrate four-band partition (C2) → adjacency band as kinematic carrier (§7.1) → Fourier-conjugate $b_x + b_p$ decomposition (§7.2) → bandwidth-allocation inequality (§7.3) → Born-rule identification (§7.4) → Fourier-uncertainty theorem (§7.5).

No canonical commutator is assumed; no Robertson-Schrödinger derivation is invoked as primary; the inequality arises from substrate-level structural facts plus standard Fourier analysis.

---

## 8. Exclusion Arguments

### 8.1 A1 — No four-band partition

Primitive 04 §1.5 supplies the four-band partition as a substrate-level structural fact (C2). A substrate with only a single undifferentiated bandwidth provides no structural carrier for the position-momentum conjugate pair, and the orthogonal-partition mechanism producing the uncertainty inequality cannot start. C2 is violated.

### 8.2 A2 — Non-Fourier-conjugate adjacency partition

The Fourier-conjugate structure of $(b_x, b_p)$ is forced by Paper #4 §7.2: spatial translation symmetry on the participation manifold has a unique self-adjoint generator $\hat{p} = -i\hbar\nabla$. The variables $x$ and $p = \hbar k$ are canonically Fourier-conjugate. An alternative partition into non-Fourier-conjugate components (e.g., $(b_y, b_z)$ for two spatial directions) would not correspond to a position-momentum pair and would not produce the Heisenberg-form inequality. C4 (Paper #4 momentum-operator result) forces Fourier-conjugacy.

### 8.3 A3 — Three or more conjugate partitions

A partition of $b^\mathrm{adj}$ into three or more Fourier-conjugate components would require three or more canonical-conjugate pairs sharing a single bandwidth budget. The Fourier transform on $\mathbb{R}^d$ supplies $d$ position-momentum pairs $(x_i, p_i)$, but each pair has its *own* bandwidth budget (the adjacency band along that spatial direction), not a shared one. A three-or-more-conjugate partition of a single budget would require non-standard Fourier structure not supplied by the participation manifold's translation symmetry.

In $\mathbb{R}^3$, the correct structure is three independent adjacency-band partitions, one per spatial direction, each producing its own uncertainty inequality $\Delta x_i\,\Delta p_i \geq \hbar/2$. Cross-direction uncertainties ($\Delta x_i\,\Delta p_j$ for $i \neq j$) are not constrained by the substrate-level argument — consistent with standard QM, where $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$.

### 8.4 A4 — Non-variance bandwidth-spread measure

Alternative spread measures (support width, distributional entropy, $L^p$ norms for $p \neq 2$) would change the inequality form but not necessarily its existence. The variance identity is forced by the substrate's $L^2$ structure (Paper #3's sesquilinear inner product on the participation manifold): the variance is the natural quadratic functional on inner-product spaces, and the Cauchy-Schwarz inequality that underlies the Robertson-Schrödinger form is a variance-based statement. Non-variance measures produce different inequalities (e.g., entropic uncertainty relations, B4) downstream of the variance form, not as competing substrate-level structures.

### 8.5 A5 — Anisotropic conjugate pairs

Direction-dependent $\hbar$ would correspond to a substrate that breaks rotational symmetry of the participation manifold. By the substrate's primitive structure (Primitives P03 + P09 + P13 supply rotationally-symmetric content), all three spatial directions carry the same Fourier-conjugacy structure with the same $\hbar$. Anisotropic $\hbar_x \neq \hbar_y \neq \hbar_z$ would require a primitive supplying directional anisotropy, which the substrate does not provide.

### 8.6 A6 — Different commutator structure

A state-dependent commutator $[\hat{x}, \hat{p}] = i f(\hat{x}, \hat{p})$ would violate Stone's theorem applied to spatial translations (Paper #4 §7.2). Stone's theorem produces a unique constant-coefficient generator $\hat{p} = -i\hbar\nabla$; state-dependent generators would require violating the unitary-translation-group structure, which is itself forced by the substrate's homogeneity (C4 inheritance from Paper #4). C4 forbids state-dependent commutators.

### 8.7 A7 — No bandwidth-allocation inequality

Independent allocation of $b_x$ and $b_p$ (both concentratable simultaneously) would violate the orthogonal-partition Cauchy-Schwarz argument of §7.3. Orthogonal partitions sharing a common bandwidth budget (the adjacency band $b^\mathrm{adj}$) necessarily satisfy the allocation inequality; the only way to evade it would be to have *independent* bandwidth budgets for $b_x$ and $b_p$. But §7.2 establishes that they share the *same* adjacency band, not separate budgets. C2's four-band structure (one adjacency band, not two) forces the shared-budget property.

### 8.8 B1 — Heisenberg as Hilbert-space Fourier theorem

The Weyl-inequality formulation of Heisenberg takes the $L^2(\mathbb{R})$ Hilbert space as input. Under the substrate-conditions test, the Hilbert-space arena is itself substrate-derived (Paper #3 supplies the sesquilinear inner product; the completion is the Hilbert space). The Weyl inequality applies *to* the substrate-derived Hilbert space; it is a downstream consequence rather than a primary derivation. The present paper's substrate forcing produces both the Hilbert space (via Papers #1, #3) and the uncertainty inequality (via the four-band partition argument here), with the Weyl inequality as the mathematical-infrastructure step in §7.5.

### 8.9 B2 — Operator-algebraic derivation (Robertson-Schrödinger)

The operator-algebraic derivation takes the canonical commutator $[\hat{x}, \hat{p}] = i\hbar$ as input. Under the substrate-conditions test, the commutator is substrate-derived: Paper #4 §7.2 produces $\hat{p} = -i\hbar\nabla$ via Stone's theorem on spatial translations; combined with the position operator $\hat{x}$ as multiplication-by-$x$ on the participation manifold, the commutator is the standard $[\hat{x}, \hat{p}] = i\hbar$ identity from operator theory. The Robertson-Schrödinger inequality is therefore downstream of the substrate forcing chain; the present paper's four-band-partition argument produces the same result without taking the commutator as input.

### 8.10 B3 — Operational uncertainty (measurement-disturbance)

Ozawa's reformulation and Branciard's bounds address measurement back-action — a distinct phenomenon from state-preparation uncertainty. Both are observed in laboratory experiments; both have their own derivations. The present paper covers state-preparation uncertainty (the $\Delta x$, $\Delta p$ in the standard form refer to state-level variances, not measurement-disturbance quantities). Operational uncertainty is downstream content involving additional measurement-process structure not covered here.

### 8.11 B4 — Entropic uncertainty relations

Entropic uncertainty relations (Maassen-Uffink, Berta et al.) refine the variance-form Heisenberg inequality by replacing variances with entropies. These are downstream of the variance form: the variance is the second moment, and entropies provide tighter bounds in certain regimes. The present paper covers the variance form; entropic refinements operate on the same substrate-derived Hilbert-space arena.

### 8.12 B5 — Semiclassical / coherent-state derivations

Semiclassical / WKB derivations take coherent states as inputs and derive uncertainty as a minimum-uncertainty property. Under the substrate-conditions test, coherent states are downstream of the substrate forcing: they are specific minimum-uncertainty wavepackets in the Hilbert space the substrate produces. The substrate forcing predicts coherent states will saturate the inequality (§7.5: Gaussian wavepackets are the equality case); coherent-state-based derivations are not alternatives but consequences.

### 8.13 B6 — Decoherence-as-source models

Decoherence-driven uncertainty interprets the inequality as arising from environmental coupling rather than as a state-preparation property. Under the substrate-conditions test, environmental decoherence is a *separate* substrate-level mechanism (Paper #2's commitment-event phase-randomization, C4-level), distinct from the state-preparation uncertainty of the present paper. Decoherence broadens distributions over time but does not generate the underlying inequality; the Heisenberg bound holds for pure states with no environmental coupling, contradicting decoherence-as-source models.

### 8.14 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 no four-band partition | C2 | Primitive P04 §1.5 forces four-band structure. |
| A2 non-Fourier-conjugate partition | C4 (Paper #4) | Stone's theorem forces $\hat{p} = -i\hbar\nabla$; $x$-$p$ are canonically Fourier-conjugate. |
| A3 three+ conjugate partitions | C2 + Fourier structure | Each spatial direction has its own adjacency band; cross-direction pairs unconstrained. |
| A4 non-variance spreads | C4 (Paper #3 IP) | Variance forced by inner-product $L^2$ structure; entropic forms downstream. |
| A5 anisotropic conjugate pairs | rotational symmetry of substrate | No primitive supplies directional anisotropy. |
| A6 state-dependent commutator | C4 (Paper #4 Stone) | Stone's theorem forces constant-coefficient generator. |
| A7 no allocation inequality | C2 (shared budget) | Orthogonal partitions share adjacency-band budget; Cauchy-Schwarz forces inequality. |
| B1 Weyl-theorem-as-primary | not in space | Hilbert space itself is substrate-derived; Weyl inequality is downstream. |
| B2 Robertson-Schrödinger | not in space | Commutator is substrate-derived (Paper #4); operator algebra downstream. |
| B3 operational (measurement-disturbance) | scope-different | Distinct phenomenon; covers measurement back-action, not state-preparation. |
| B4 entropic uncertainty | downstream | Refinements of variance form; same substrate-derived Hilbert space. |
| B5 semiclassical / coherent-state | downstream | Coherent states are minimum-uncertainty consequences, not alternative substrate. |
| B6 decoherence-as-source | C4 (Paper #2) | Decoherence is a separate substrate mechanism; pure-state inequality contradicts decoherence-source model. |

**The Heisenberg uncertainty relation $\Delta x\,\Delta p \geq \hbar/2$ is the unique substrate-derived inequality on the Fourier-conjugate partition of the adjacency band.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier is sharp:

**Any observed violation of $\Delta x\,\Delta p \geq \hbar/2$ for a quantum state's position-momentum variances falsifies the substrate forcing along with standard quantum mechanics.**

Specific tests:

- **Single-atom diffraction**: precision measurements of position and momentum spreads in atom-interferometer experiments. All observed data is consistent with the Heisenberg bound at the precision available.
- **Bose-Einstein condensate position-momentum cross-correlation**: BEC dynamics test the bound on macroscopic-coherence states; observed data consistent.
- **Squeezed-state experiments**: quantum optics produces states with $\Delta x < $ vacuum-state-uncertainty at the cost of $\Delta p > $ vacuum-state-uncertainty, with the product $\Delta x\,\Delta p$ saturating the bound at $\hbar/2$ for minimum-uncertainty squeezed states. Observed saturation at the bound.

None of these tests has produced a reproducible violation. The substrate forcing predicts the bound exactly; any reproducible violation would refute both the substrate forcing and standard QM.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C5 (participation graph with four-band partition, adjacency band as kinematic carrier, Papers #1-#4 inherited, no uncertainty relation as input) but supporting a non-Heisenberg uncertainty inequality — e.g., $\Delta x\,\Delta p \geq \hbar/4$, or a state-dependent bound, or no bound at all — that survives the exclusion arguments of §8.

The author's claim is that no such substrate exists. Each alternative is dispatched by a specific substrate-condition violation. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

Three immediate exposures:

**Atomic and molecular physics.** The Heisenberg inequality underlies the zero-point energy of harmonic oscillators (a consequence of $\Delta x\,\Delta p \geq \hbar/2$ in oscillator ground states), the size of atoms (the balance between kinetic energy and Coulomb attraction set by the uncertainty bound), and the structure of the periodic table. All quantitative predictions of atomic physics depend on the substrate-derived bound.

**Quantum metrology and squeezed-state technology.** Squeezed states saturating the Heisenberg bound enable precision measurements below the standard quantum limit (gravitational-wave detectors with squeezed-light input, atomic clocks with spin-squeezed atomic ensembles). The substrate forcing supports this entire technology.

**Quantum information theory.** Channel capacity bounds and entropic uncertainty relations build on the substrate-derived variance form. The present paper's substrate forcing supports the foundational structure of quantum information theory.

The empirical exposure of the present paper is the entirety of quantitative quantum-mechanical phenomenology that depends on the position-momentum uncertainty bound — which is essentially all of it.

---

## Appendix A — Derivation Chain and Glossary

### A.1 The Fourier-uncertainty theorem — standard mathematical content

For any $\Psi \in L^2(\mathbb{R})$ with $\int |\Psi|^2 dx = 1$ and Fourier transform $\tilde\psi$ defined by
$$
\tilde\psi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int \Psi(x)\,e^{-ipx/\hbar}\,dx,
$$
the variances $(\Delta x)^2 = \langle x^2\rangle - \langle x\rangle^2$ and $(\Delta p)^2 = \langle p^2\rangle - \langle p\rangle^2$ satisfy
$$
\Delta x\,\Delta p \geq \frac{\hbar}{2}.
$$

**Proof sketch (Weyl's argument).** Without loss of generality, $\langle x\rangle = \langle p\rangle = 0$. Define $\hat{x}\Psi = x\Psi(x)$ and $\hat{p}\Psi = -i\hbar\partial_x\Psi$. The commutator $[\hat{x}, \hat{p}] = i\hbar$ holds by direct calculation. Apply the Cauchy-Schwarz inequality to $\hat{x}\Psi$ and $\hat{p}\Psi$:
$$
\|\hat{x}\Psi\|^2\,\|\hat{p}\Psi\|^2 \geq |\langle \hat{x}\Psi, \hat{p}\Psi\rangle|^2.
$$
The right-hand side equals $|\langle \Psi, \hat{x}\hat{p}\Psi\rangle|^2 \geq (\text{Im}\langle\Psi, \hat{x}\hat{p}\Psi\rangle)^2 = (\frac{1}{2}\langle\Psi, [\hat{x}, \hat{p}]\Psi\rangle)^2 = (\hbar/2)^2$. Taking square roots:
$$
\Delta x\,\Delta p \geq \frac{\hbar}{2}.
$$
Equality holds for Gaussian wavepackets $\Psi(x) \propto e^{-x^2/(4\sigma^2)}$, which satisfy $(\hat{x} - ic\hat{p})\Psi = 0$ for an appropriate $c$.

### A.2 The bandwidth-allocation inequality — substrate derivation

The substrate-level form is derived by applying the Cauchy-Schwarz argument at the bandwidth level. Define the *bandwidth-weighted* expectation values for the position-adjacency partition:
$$
\langle f(x)\rangle_{b_x} = \frac{\int f(x)\,b_x(x)\,dx}{\int b_x(x)\,dx},
$$
and analogously for $b_p$. Bandwidth variances:
$$
(\Delta b_x)^2 = \langle x^2\rangle_{b_x} - \langle x\rangle_{b_x}^2, \qquad (\Delta b_p)^2 = \langle p^2\rangle_{b_p} - \langle p\rangle_{b_p}^2.
$$

Under the identifications $b_x(x) \propto |\Psi(x)|^2$ and $b_p(p) \propto |\tilde\psi(p)|^2$ (Born rule applied within each adjacency partition), these bandwidth variances equal the standard QM variances. The orthogonal-partition Cauchy-Schwarz argument on the participation-manifold inner product then forces
$$
(\Delta b_x)(\Delta b_p) \geq K_{xp},
$$
and the Fourier-uncertainty theorem of A.1 forces $K_{xp} = \hbar/2$ in the thin-participation limit.

### A.3 Glossary

- **Adjacency band $b^\mathrm{adj}$.** Substrate-level (Primitive P04 §1.5) bandwidth component coupling chains to immediate participation-adjacent neighborhoods.
- **Bandwidth-allocation inequality.** $(\Delta b_x)(\Delta b_p) \geq K_{xp}$; substrate-level constraint on bandwidth-variance products across orthogonal conjugate partitions.
- **Bandwidth variance $(\Delta b)^2$.** Second central moment of a bandwidth distribution: $\langle x^2\rangle_b - \langle x\rangle_b^2$.
- **Born rule.** $\text{Prob}(K) \propto |P_K|^2$ (Paper #2).
- **Cauchy-Schwarz inequality.** $|\langle a, b\rangle|^2 \leq \langle a, a\rangle\,\langle b, b\rangle$ on inner-product spaces.
- **FORCED.** Derived from substrate primitives + standard mathematics with no additional commitments.
- **Four-band partition.** Primitive P04 §1.5: $b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com}$, mutually orthogonal.
- **Fourier-conjugate pair.** Two variables $x$ and $p = \hbar k$ related by the Fourier transform on $L^2(\mathbb{R})$.
- **Heisenberg uncertainty relation.** $\Delta x\,\Delta p \geq \hbar/2$.
- **INHERITED.** Quantitative content (value of $\hbar$, proportionality constants in identifications) used but not derived in this paper.
- **Momentum operator $\hat{p}$.** $-i\hbar\nabla$; spatial-translation generator (Paper #4 §7.2).
- **Momentum-adjacency $b_p$.** Component of $b^\mathrm{adj}$ allocated to phase-coherent propagation; Fourier-conjugate to $b_x$.
- **Participation manifold.** Complex Hilbert space carrying participation measures (Paper #3).
- **Position-adjacency $b_x$.** Component of $b^\mathrm{adj}$ allocated to spatial localization.
- **Substrate.** Pre-quantum primitive layer of ED.
- **Variance.** $(\Delta f)^2 = \langle f^2\rangle - \langle f\rangle^2$ for a probability density or bandwidth distribution.

### A.4 Source-repository citations (for ED-internal readers)

- `arcs/arc-foundations/uncertainty_from_participation.md` — Step 5 derivation memo for the Heisenberg uncertainty from the four-band partition.
- `arcs/U5/04_closure_and_summary.md` — U5 arc closure with Stone's theorem on spatial translations → $\hat{p} = -i\hbar\nabla$ (the conjugate-variable structure inherited here).
- `quantum/primitives/04_participation_bandwidth.md` §1.5 — Primitive 04 four-band partition.
- `walkthroughs/from_primitives_to_heisenberg_uncertainty.md` — public-facing walkthrough.

These are *not* required reading for the present paper.

---

*End of Paper #11.*
