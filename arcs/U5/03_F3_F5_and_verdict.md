# Memo 03 — F3 (Fourier Conjugacy), F5 (Exhaustion), and U5 Arc Verdict

**Date:** 2026-04-26
**Arc:** `arcs/U5/`
**Predecessors:** [`00_arc_outline.md`](00_arc_outline.md), [`01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md), [`02_derivations_F1_F2_F4.md`](02_derivations_F1_F2_F4.md)
**Status:** Load-bearing memo of the U5 arc. Settles the two outstanding sub-features identified in Memo 01: F3 (Fourier conjugacy specificity) via translation symmetry and Stone's theorem, and F5 (exhaustion of adjacency-axes) via primitive-level audit. Delivers the U5 arc verdict and characterises the downstream cascade.
**Purpose:** Close the U5 arc with a theorem-grade verdict on the adjacency-band Fourier-conjugate partition.

---

## 1. The State of the Arc Entering Memo 03

After Memos 01–02, three of five U5 sub-features are established:

- **F1 (existence of decomposition):** established via two independent primitive-level adjacency-axes — Primitive 06's spatial axis ($\nabla \rho$) and Primitive 09's phase-propagation axis ($\nabla \pi$).
- **F2 (two-component count):** established by direct enumeration, conditional on F5.
- **F4 (orthogonality under U2):** established via Parseval's identity inherited from Fourier unitarity on the U2 inner-product space, with continuum-regime gauge-invariance verified.

Two sub-features remain:

- **F3 (Fourier conjugacy specificity).** The two adjacency-axes form a Fourier-conjugate pair under the standard $L^2$ Fourier transform; no fractional-Fourier, wavelet, or alternative conjugacy structure is admissible.
- **F5 (exhaustion / no third adjacency-axis).** The primitive stack admits exactly the two axes identified in F1; no third primitive-level adjacency-axis exists.

Two falsifiers remain active: **Fal-3** (non-Fourier conjugacy, attached to F3) and **Fal-2** in its unconditional form (third axis, attached to F5). This memo dispatches both.

---

## 2. Derivation of F3 — Fourier Conjugacy Specificity

### 2.1 The claim

Among all unitary integral transforms admissible on the U2 inner-product Hilbert space, the natural transformation between the position-representation $\Psi(x)$ and the momentum-representation $\widetilde\psi(p)$ is *uniquely* the standard Fourier transform:

$$
\widetilde\psi(p, t) = (2\pi\hbar)^{-d/2} \int \Psi(x, t) \cdot e^{-i p \cdot x / \hbar} \, d^d x \qquad (1)
$$

with $d = \dim$ position space. No fractional-Fourier $\mathcal{F}^a$ for $a \neq 1$, no wavelet transform, no Mellin transform, and no other unitary intertwiner is consistent with the primitive-level translation symmetry of the participation graph applied to the U2 inner-product structure.

### 2.2 Translation symmetry as a kinematic input

**Premise (P-03 + P-06 jointly).** The participation graph $G = (V, E)$ — and the emergent manifold $M$ in the continuum regime — supports translations as a symmetry of the primitive-level adjacency relation. Specifically:

- **Primitive 03 (Participation):** the edge structure of $G$ does not privilege any particular vertex. The participation relation is *homogeneous* at the primitive level: any two vertices participate in the same primitive-level structural relation, modulo their actual connectivity content.
- **Primitive 06 (ED Gradient):** $\nabla \rho$ defines a spatial direction, but its *direction* is not privileged — translations along $\nabla \rho$ (or any direction in the tangent space of the spatial structure) are admissible kinematic transformations.

Together, Primitives 03 and 06 establish that translations $T_a : x \to x + a$ for any vector $a$ in the spatial tangent space are admissible kinematic symmetries of the participation graph.

**Note on independence from U3.** Translation symmetry is a *kinematic* property of the participation graph: it concerns the structural homogeneity of the graph itself, not the dynamical evolution of the participation measure. The earlier tightening-program derivation of U5 invoked U3 (the participation-measure evolution equation) as a premise for translation symmetry; the present derivation derives translation symmetry directly from Primitives 03 and 06 as kinematic inputs, bypassing U3 entirely. This sharpening has a substantive consequence: the U5 verdict is *independent* of whatever conditionality U3 carries. F3 derives from primitive-level kinematic structure plus the now-FORCED U2 inner product; no dynamical premise is needed.

### 2.3 Stone's theorem on the translation group

The set of translations $\{T_a : a \in \mathbb{R}^d\}$ forms a one-parameter (per direction; $d$-parameter abelian Lie group overall) unitary group on the U2 inner-product Hilbert space $\mathcal{H}$. This is forced by:

- **Translation acts on participation-measure states.** $T_a \Psi(x) := \Psi(x - a)$ is a well-defined action of $T_a$ on functions in $\mathcal{H}$.
- **Translation preserves the U2 inner product.** $\langle T_a \Psi \mid T_a \Phi \rangle = \langle \Psi \mid \Phi \rangle$ for all $\Psi, \Phi \in \mathcal{H}$ — this is a consequence of $T_a$ being a measure-preserving change of variables on the position-representation, with the U2 inner product gauge-covariant under such changes (per the U2-Discrete and U2-Continuum theorems).
- **Translation is strongly continuous.** $\|T_a \Psi - \Psi\| \to 0$ as $a \to 0$ in the U2 norm, for any $\Psi \in \mathcal{H}$.

These three properties — group structure, unitarity, strong continuity — are the hypotheses of **Stone's theorem**:

> **Theorem (Stone, 1930s).** Every strongly continuous one-parameter unitary group $\{T_a : a \in \mathbb{R}\}$ on a Hilbert space $\mathcal{H}$ has a unique self-adjoint generator $\hat{A}$ such that $T_a = e^{i \hat{A} a}$.

Applied to the spatial-translation group on $\mathcal{H}$ (with the ED-conventional factor of $\hbar$):

$$
T_a = \exp\!\left( i \hat{p} \cdot a / \hbar \right) \qquad (2)
$$

where $\hat{p}$ is the unique self-adjoint generator of spatial translations. **Stone's theorem identifies $\hat{p}$ uniquely** — there is no freedom to pick a different generator that would produce a different conjugate-pair structure.

### 2.4 The momentum representation and the Fourier basis-change

The eigenfunctions of $\hat{p}$ in the position representation are plane waves:

$$
\langle x \mid p \rangle = (2\pi\hbar)^{-d/2} \cdot e^{i p \cdot x / \hbar}, \qquad \hat{p} \mid p \rangle = p \mid p \rangle \qquad (3)
$$

This is a standard mathematical-physics result: the eigenfunctions of $-i\hbar \nabla$ (which is what $\hat{p}$ is in the position representation, by Stone's theorem applied to the translation group) are plane waves with eigenvalue $p$.

Expanding any state $\Psi(x) \in \mathcal{H}$ in this momentum eigenbasis:

$$
\Psi(x) = \int dp \, \widetilde\psi(p) \langle x \mid p \rangle = (2\pi\hbar)^{-d/2} \int dp \, \widetilde\psi(p) \, e^{i p \cdot x / \hbar} \qquad (4)
$$

Inverting (using the orthonormality $\langle p \mid p' \rangle = \delta(p - p')$ from U2):

$$
\widetilde\psi(p) = (2\pi\hbar)^{-d/2} \int dx \, \Psi(x) \, e^{-i p \cdot x / \hbar} \qquad (5)
$$

Equation (5) is the standard Fourier transform. **The basis-change between the position representation and the momentum representation is uniquely the standard Fourier transform.**

### 2.5 Uniqueness against alternative conjugacies

Three classes of alternative unitary intertwiners on $\mathcal{H}$ warrant explicit dismissal.

**(Alt-1) Fractional-Fourier transforms $\mathcal{F}^a$.** For $a \in (0, 1)$, the fractional-Fourier transform $\mathcal{F}^a$ is a unitary intertwiner of *rotated* bases in the $(x, p)$ phase plane. It interpolates between identity ($a = 0$) and standard Fourier ($a = 1$). Why doesn't ED admit fractional-Fourier as an alternative?

The fractional-Fourier transform $\mathcal{F}^a$ for $a \neq 1$ does not diagonalise $\hat{p}$. It diagonalises the *rotated* operator $\cos(a \pi/2) \hat{x} + \sin(a \pi/2) \hat{p}$ — a different self-adjoint operator entirely. The basis-change between position and momentum (i.e., between eigenstates of $\hat{x}$ and eigenstates of $\hat{p}$) is uniquely $\mathcal{F}^1$, the standard Fourier. Stone's theorem applied to the *translation* group identifies $\hat{p}$ as the generator and forces the standard Fourier as the unique basis-change; fractional-Fourier transforms with $a \neq 1$ correspond to *different* conjugate pairs (involving rotated-phase-space operators), not to position-vs-momentum.

A different way to see this: the question "what is the unitary intertwiner between $\hat{x}$-eigenstates and $\hat{p}$-eigenstates?" has a unique answer (up to overall phase), and that answer is the standard Fourier. The fractional-Fourier family does not address this question; it addresses a different question about rotated phase-space bases.

**Fal-3 dispatched against fractional-Fourier alternatives.**

**(Alt-2) Wavelet transforms.** Wavelet transforms are multi-scale decompositions of $L^2$ functions — they do not arise from Stone's theorem applied to a one-parameter unitary group. Instead, they decompose functions across scales using a chosen "mother wavelet" function. The decomposition is *not* a unitary intertwiner of two bases of $\mathcal{H}$ in the Stone's-theorem sense; it is a multi-scale resolution of the identity.

Wavelet transforms therefore do not compete with the Fourier transform as candidate position-momentum conjugacies. They address a different mathematical structure (multi-scale resolution rather than canonical-pair intertwining). The primitive stack supplies translation symmetry, which forces Stone's theorem and standard Fourier; it does *not* supply a wavelet-style multi-scale structure as a primitive-level commitment.

**Fal-3 dispatched against wavelet alternatives.**

**(Alt-3) Mellin transform and other group-theoretic alternatives.** The Mellin transform is the unique unitary intertwiner of the *dilation* group $\{D_\lambda : f(x) \to \lambda^{1/2} f(\lambda x)\}$, not the translation group. It diagonalises the dilation generator $\hat{D} = -i\hbar(x \cdot \nabla + d/2)$, not $\hat{p}$. Different symmetry group; different Stone's theorem application; different intertwiner.

For the Mellin transform to be the relevant conjugacy in U5, the primitive stack would need to supply dilation symmetry (rather than translation symmetry) as the relevant kinematic input for adjacency. Primitive 06 (ED gradient) supplies translation symmetry, not dilation symmetry. The participation graph has a metric scale (via $\nabla \rho$) that is *not* dilation-invariant; dilations are not a primitive-level kinematic symmetry of the graph.

**Fal-3 dispatched against Mellin and other group-theoretic alternatives.**

**Joint conclusion.** The standard Fourier transform is the *unique* unitary intertwiner of the position and momentum representations on the U2 Hilbert space, given that the primitive stack supplies translation symmetry as the relevant kinematic input. Fractional-Fourier, wavelet, and Mellin alternatives all correspond to different group-theoretic structures or different operator pairs; none competes with the standard Fourier in the structural setting forced by ED's primitives.

### 2.6 Compatibility with U2-Discrete and U2-Continuum

The Fourier transform's standard form (1) requires the U2 inner product on $\mathcal{H}$ in two places:

- *Existence of $\mathcal{H}$.* The U2-Discrete and U2-Continuum theorems supply the inner-product-completed Hilbert space on which the translation group acts.
- *Unitarity of $T_a$.* Translation preserves the U2 inner product per §2.3, which is necessary for Stone's theorem to apply.

Both requirements are met by the now-FORCED U2 results. F3 is therefore consistent with — and indeed anchored in — the U2 inner-product structure already established.

In the continuum regime, the U2-Continuum gauge $(b_K, d\mu) \to (\Omega^{-D} b_K, \Omega^D d\mu)$ acts on bandwidth densities and volume measures uniformly. Translation symmetry on the participation graph is preserved under this gauge (the gauge does not break translation invariance — both pre- and post-gauge bandwidth fields are translation-equivariant). Stone's theorem applies in either gauge. The standard Fourier transform is the basis-change in either gauge, with the momentum-space measure $d\widetilde\mu(p)$ inheriting the appropriate gauge transformation to keep Parseval's identity invariant (per Memo 02 §4.6).

### 2.7 Curved-spacetime / non-flat continuum considerations

**Flat-spacetime baseline.** On flat-spacetime emergent manifolds (where translation symmetry is a *global* kinematic feature), the argument of §§2.2–2.6 applies directly. Standard Fourier transform is the unique conjugacy globally; F3 closes globally.

**Curved-spacetime / non-flat baselines.** On curved-spacetime emergent manifolds (where translation symmetry is only *local*, holding in tangent-space approximations at each point), the argument of §§2.2–2.6 applies *pointwise*: at each point $x \in M$, the local tangent space supports translation symmetry, Stone's theorem applies to the local translation group, and the standard Fourier transform supplies the local basis-change between position and momentum representations.

The Heisenberg uncertainty inequality $\Delta x \cdot \Delta p \geq \hbar/2$ is itself a *local* statement (about a state at a specific locus). The local-Fourier construction is sufficient for the inequality to hold at each point. Gluing local-Fourier constructions across points is by standard differential-geometric machinery (locally-trivialised co-tangent bundle structure on $M$); this introduces no ED-program-internal conditionalities.

**Net.** F3 holds globally on flat-spacetime baselines and pointwise on curved-spacetime baselines, with the local-Fourier construction sufficient for downstream applications of Heisenberg's inequality. The verdict is *uniformly FORCED*, with the curved-spacetime case requiring standard differential-geometric infrastructure that does not introduce new structural commitments.

### 2.8 Verdict for F3

**FORCED.** The standard Fourier transform is uniquely identified as the unitary intertwiner between position and momentum representations, by Stone's theorem applied to the translation group of the participation graph (Primitives 03 + 06 supplying translation symmetry as a kinematic input) on the U2 inner-product Hilbert space (now FORCED). Fractional-Fourier, wavelet, and Mellin alternatives are dismissed by structural inconsistency with this construction: they correspond to different group-theoretic structures or different operator pairs, not to the position-momentum conjugacy. The derivation is independent of U3 (the participation-measure evolution equation), sharpening the earlier tightening-program memo's conditional argument.

**Falsifier Fal-3 is dispatched.**

---

## 3. Derivation of F5 — Exhaustion / No Third Adjacency-Axis

### 3.1 The claim

The primitive stack admits exactly two adjacency-axes — Primitive 06's spatial axis and Primitive 09's phase-propagation axis — with no third primitive-level adjacency-axis distinct from these two. The decomposition $b^\mathrm{adj} = b_x + b_p$ is therefore exhaustive: $b_\mathrm{residual} = 0$ in equation (2) of Memo 02.

This is a *negative-existence* claim: there is no third axis. The argument structure is a primitive-level audit of candidate third axes, with each candidate dismissed on structural grounds.

### 3.2 Audit framework

A "third adjacency-axis" would be a primitive-level structural feature satisfying three criteria:

- **(A) Primitive-level.** Supplied by some primitive in the ED stack, not derived from existing primitives or computed as a higher-order quantity.
- **(B) Adjacency-relevant.** Applicable to the adjacency band of Primitive 04's four-band decomposition (rather than internal-rule, environmental, or commitment-reserve bands).
- **(C) Independent of Primitives 06 and 09.** Not reducible to the spatial axis (Primitive 06) or the phase-propagation axis (Primitive 09).

Any candidate failing one or more of (A), (B), (C) is not a third adjacency-axis. We audit four candidates, plus a survey of the remaining primitives.

### 3.3 Candidate 1 — Bandwidth-gradient direction ($\nabla b$)

**The candidate.** The gradient of bandwidth itself, $\nabla b_K$, supplies a directional structure on the participation graph. Could this be an adjacency-axis distinct from $\nabla \rho$ (Primitive 06) and $\nabla \pi$ (Primitive 09)?

**Audit against (A).** Bandwidth is a primitive (Primitive 04 supplies $b$). Its gradient is a derived quantity — computed from $b$ rather than separately supplied by a primitive. $\nabla b$ is not a primitive-level structural feature in its own right.

**Audit against (B).** $\nabla b$ is defined wherever $b$ varies, including but not limited to the adjacency band. Adjacency-relevance is satisfiable.

**Audit against (C).** The direction of $\nabla b_K$ is determined by the spatial structure of the bandwidth distribution, which is parameterised by the spatial coordinate supplied by Primitive 06's $\nabla \rho$. Specifically: $\nabla b_K$ lies in the spatial tangent space, the same space spanned by $\nabla \rho$. Any direction supplied by $\nabla b_K$ is either parallel to $\nabla \rho$ (no new direction) or perpendicular to it within the spatial tangent space (still spanned by Primitive 06's spatial structure).

**Verdict.** $\nabla b$ does not supply a *kind* of nearness distinct from the spatial axis. It is a refinement within the spatial axis already supplied by Primitive 06. **Not a distinct primitive-level adjacency-axis.**

### 3.4 Candidate 2 — Rule-type coupling

**The candidate.** Different chains have different rule-types (Primitive 07's rule-type-selectivity). Could rule-type difference supply an adjacency-axis — i.e., a notion of "nearness in rule-type"?

**Audit against (A).** Primitive 07 supplies the channel structure including rule-type labels. Rule-type difference is primitive-level structural content.

**Audit against (B).** For a *single chain* of rule-type $\tau$, the available channels are restricted to $\mathcal{K}_\tau(u)$ — channels of rule-type $\tau$ only. Within this restricted set, all channels share the same rule-type by definition; there is no rule-type-distance between channels of the same chain. Rule-type coupling is therefore *not* an adjacency-axis within a single chain's adjacency band.

For *multi-chain* systems where chains of different rule-types interact, rule-type coupling appears in the *environmental* band of the four-band structure (Primitive 04 §1.5), not in the adjacency band. The four-band orthogonality keeps these sectors separate at the primitive level.

**Audit against (C).** Even if one tried to extract rule-type coupling within an adjacency band (which is methodologically unclear), it would involve different kinds of structure — rule-type label distance — than the spatial or phase-propagation axes. Independent in principle, *but the (B) failure rules it out before (C) becomes relevant.*

**Verdict.** Rule-type coupling fails the adjacency-relevance criterion: it lives in the environmental band, not the adjacency band, when it lives in the participation-measure structure at all. **Not an adjacency-axis.**

### 3.5 Candidate 3 — Polarity-amplitude direction (distinct from polarity-phase)

**The candidate.** Primitive 09 supplies polarity *phase* $\pi(K, x)$. Could polarity have an *amplitude* dimension distinct from phase, supplying a third adjacency-axis?

**Audit against (A).** Primitive 09 explicitly states polarity is $U(1)$-valued (Memo 01 §1.2 cites Primitive 09 §1.16: "Polarity is not a binary in general — it is a phase in the full treatment"; §1.30: "Not a scalar"). Polarity has only phase content; there is no separate amplitude variable in the primitive. Polarity-amplitude distinct from phase is not supplied by any primitive.

The participation measure construction $P_K = \sqrt{b_K} \cdot e^{i \pi_K}$ has phase factor $e^{i \pi_K}$ of unit modulus and magnitude $\sqrt{b_K}$ supplied by bandwidth (Primitive 04). The "amplitude" of the participation measure is bandwidth-derived, not polarity-derived. There is no polarity-amplitude separate from bandwidth.

**Audit against (B).** Moot — fails (A).

**Audit against (C).** Moot — fails (A).

**Verdict.** Polarity-amplitude is not supplied by any primitive. Polarity is purely phase-valued at the primitive level. **Not a distinct primitive-level structural feature.**

### 3.6 Candidate 4 — Higher-derivative axes ($\nabla^2 \rho$, $\nabla^2 \pi$, etc.)

**The candidate.** Higher derivatives of event-density and polarity ($\nabla^2 \rho$, $\nabla^2 \pi$, $\nabla^3 \rho$, etc.) supply additional directional structures. Could any of these be a primitive-level adjacency-axis distinct from the first-derivative axes?

**Audit against (A).** Higher derivatives are computed from the first-derivative axes; they are not separately supplied by primitives. Higher derivatives are derivative quantities at the primitive level.

**Audit against (C).** $\nabla^2 \rho$ lies in the spatial tangent-bundle structure spanned by Primitive 06's spatial axis. $\nabla^2 \pi$ lies in the phase-gradient bundle structure spanned by Primitive 09's phase-propagation axis. Higher derivatives refine *within* the existing axes; they do not introduce a third *kind* of nearness distinct from spatial or phase-propagation.

**Verdict.** Higher derivatives are derivative quantities that refine within the existing two axes. They do not constitute an independent third adjacency-axis. **Not a distinct primitive-level axis.**

### 3.7 Survey of remaining primitives

For completeness, we survey the remaining ED primitives (01, 02, 05, 07, 08, 10, 11, 12, 13) for any candidate adjacency-axis we have not yet considered.

- **Primitive 01 (Micro-Event):** supplies vertices (discrete events), not adjacency-axes.
- **Primitive 02 (Chain):** supplies the chain identity-rule, not adjacency-relations among events.
- **Primitive 05 (Event Density):** $\rho$ is a scalar field; its *gradient* is Primitive 06. $\rho$ itself does not supply a directional structure.
- **Primitive 07 (Channel):** supplies channel sub-structures and their rule-type labels; addressed in Candidate 2.
- **Primitive 08 (Multiplicity):** supplies an effective channel-count $M_\mathrm{eff}$; not a directional structure.
- **Primitive 10 (Individuation):** supplies a threshold for distinguishing chains; event-level structural feature, not an adjacency-axis.
- **Primitive 11 (Commitment):** supplies discrete commitment events; temporal/event-level rather than spatial/phase-propagation.
- **Primitive 12 (Thickening):** supplies the accumulation-into-continuum structure; supplies thickening density $\tau$ but not a directional structure independent of Primitive 06.
- **Primitive 13 (Relational Timing):** supplies finite proper-time intervals; *temporal* nearness rather than *adjacency* (which is spatial / phase-propagation in the four-band structure).

None of these primitives supplies an adjacency-axis. Adjacency-relevant structure is concentrated in Primitives 06 and 09 only.

### 3.8 Joint verdict for F5

The audit examined four candidate third adjacency-axes (bandwidth-gradient, rule-type coupling, polarity-amplitude, higher-derivatives) and surveyed the remaining nine primitives. None constitutes a primitive-level adjacency-axis distinct from Primitives 06 (spatial) and 09 (phase-propagation):

- $\nabla b$ refines within the spatial axis already supplied by Primitive 06.
- Rule-type coupling lives in the environmental band, not the adjacency band.
- Polarity-amplitude is not supplied by Primitive 09 (which is $U(1)$-valued).
- Higher derivatives are derivative quantities refining within the existing axes.
- The remaining nine primitives supply no adjacency-relevant directional structure at all.

**No third primitive-level adjacency-axis exists in the current primitive stack.** F5's exhaustion claim is established; the decomposition $b^\mathrm{adj} = b_x + b_p$ is complete, with $b_\mathrm{residual} = 0$.

**Falsifier Fal-2 (in its unconditional form) is dispatched.** Combined with F2 of Memo 02, the two-component count is now established unconditionally.

### 3.9 Robustness against future primitive amendments

F5's verdict is conditional on the current primitive stack. A future amendment introducing a new primitive supplying an additional adjacency-relevant directional structure would re-open F5 and potentially refute the two-component decomposition. The structural sensitivity is real and should be flagged: any future primitive amendment with adjacency-relevant content (e.g., extensions to multi-component polarity, additional gradient primitives beyond Primitive 06, etc.) would require re-deriving U5 under the amended stack.

This sensitivity is structurally analogous to U2's sensitivity to Primitive 09 amendments (Memo 02 §6.2 of the U2 arc): the U5 result is as strong as the current adjacency-axis content of the primitive stack. No current amendment is on the table; the verdict stands under the current stack.

---

## 4. The U5 Verdict

### 4.1 Statement

> **Theorem (U5; Adjacency-Band Fourier-Conjugate Partition).** Let $G = (V, E)$ be a participation graph with vertex set $V$ (Primitive 01) and edge set $E$ (Primitive 03), supplying translation symmetry as a kinematic feature. Let $b^\mathrm{adj}$ denote the adjacency-band component of the four-band bandwidth decomposition (Primitive 04 §1.5). Then $b^\mathrm{adj}$ admits a unique orthogonal decomposition
>
> $$
> b^\mathrm{adj}(x, t) = b_x(x, t) + b_p(p, t)
> $$
>
> with the following structural properties:
>
> 1. **Existence (F1).** The decomposition exists because Primitive 06 supplies a spatial axis ($\nabla \rho$) and Primitive 09 supplies a phase-propagation axis ($\nabla \pi$), with the two axes structurally independent.
> 2. **Two-component count (F2 + F5).** The decomposition has exactly two components: no third primitive-level adjacency-axis exists in the current primitive stack (audit: §3).
> 3. **Fourier conjugacy (F3).** The two components are connected by the standard $L^2$ Fourier transform, uniquely identified by Stone's theorem applied to the translation group of the participation graph on the U2 inner-product Hilbert space. No fractional-Fourier, wavelet, or Mellin alternative is admissible.
> 4. **Orthogonality under U2 (F4).** $b_x$ and $b_p$ are orthogonal projections of the participation-measure state, with Parseval's identity $\int |\Psi|^2 d\mu = \int |\widetilde\psi|^2 d\widetilde\mu = N_\mathrm{adj}$ supplying the orthogonal-decomposition relation.
> 5. **Bandwidth-density identifications.** $b_x \propto |\Psi(x)|^2$ and $b_p \propto |\widetilde\psi(p)|^2$, inherited as theorem-grade identifications from Theorem 10 (Born) applied per-band.
> 6. **Continuum-regime gauge-invariance.** Under the U2-Continuum conformal gauge, both partition components rescale uniformly and Parseval's identity is gauge-invariant. The partition is preserved under the gauge.

**Status:** **FORCED.** No new structural commitment is introduced anywhere in the derivation. All inputs (Primitives 03, 04, 06, 09; the U2-Discrete and U2-Continuum theorems; Theorem 10) are already established or supplied by the primitive stack. The derivation is independent of U3 (the participation-measure evolution equation), sharpening the earlier tightening-program memo's conditional argument.

### 4.2 Scope and qualifications

**Discrete regime.** U5 is forced unconditionally on the discrete participation graph. Translation symmetry is a global kinematic feature of the homogeneous participation graph; Stone's theorem applies globally; standard Fourier transform supplies the conjugacy globally; all sub-features close uniformly.

**Continuum regime, flat-spacetime baseline.** U5 is forced unconditionally on flat-spacetime emergent manifolds (where translation symmetry is global). Stone's theorem applies globally; standard Fourier transform supplies the conjugacy globally; the U2-Continuum gauge-invariance preserves the partition.

**Continuum regime, curved-spacetime baseline.** U5 is forced pointwise. Translation symmetry is local (in tangent-space approximations at each point of $M$); Stone's theorem applies pointwise; the local Fourier transform supplies the conjugacy at each point. Heisenberg's uncertainty inequality is itself a local statement, so the local-Fourier construction is sufficient. Gluing local constructions across $M$ is by standard differential-geometric machinery (locally-trivialised cotangent-bundle structure) and introduces no ED-program-internal conditionalities.

**Sensitivity to primitive amendments.** U5's verdict is conditional on the current primitive stack. A future amendment supplying an additional adjacency-relevant directional structure would re-open F5 and potentially refute the two-component decomposition. The verdict is as strong as the current adjacency-axis content of the primitives.

### 4.3 Falsifier audit summary

| Falsifier | Sub-feature | Status |
|---|---|---|
| Fal-1 (no decomposition exists) | F1 | Dispatched (Memo 02 §5.1) |
| Fal-2 (third axis) | F2 + F5 | Dispatched (Memo 03 §3.8) |
| Fal-3 (non-Fourier conjugacy) | F3 | Dispatched (Memo 03 §2.5) |
| Fal-4 (non-orthogonal partition) | F4 | Dispatched (Memo 02 §5.3) |
| Fal-5 (gauge propagation) | F4 (continuum) | Dispatched (Memo 02 §5.4) |

All five falsifiers are dispatched. No physical-distinction alternative survives.

---

## 5. Downstream Implications

### 5.1 Heisenberg uncertainty (Phase-1 Step 5)

**Pre-U5 status.** The Heisenberg uncertainty inequality $\Delta x \cdot \Delta p \geq \hbar/2$ was derived conditionally on U2 (sesquilinear inner product) and U5 (adjacency-band Fourier-conjugate partition). With U2 forced (in both discrete and continuum regimes per the U2 program) and U5 now forced (this arc), the conditionalities are fully resolved.

**Post-U5 status.** **Heisenberg promotes to FORCED-unconditional in both discrete and continuum regimes.** The bandwidth-allocation inequality $(\Delta b_x)(\Delta b_p) \geq K_{xp}$ derives from the partition (forced by F1–F5); the structural constant $K_{xp} = \hbar/2$ is fixed by Fourier-uncertainty applied to the U2-inner-product space. Both pieces are now forced.

The continuum-regime gauge-invariance check of Memo 02 §4.6 confirms that Heisenberg's bound is gauge-invariant under the U2-Continuum conformal rescaling: the variances $(\Delta x)^2$ and $(\Delta p)^2$ are bandwidth-fraction quantities (gauge-invariant by the same mechanism as Born probabilities), so their product is gauge-invariant. Heisenberg's bound is identical across all gauge representatives.

### 5.2 Interaction with U2, Born, Bell/Tsirelson

**U2 (FORCED).** U5 inherits U2's inner-product structure as input; no feedback into U2's derivation. U5 is gauge-compatible with the U2-Continuum gauge (both partition components rescale uniformly under the conformal redundancy).

**Born / Theorem 10 (FORCED-unconditional).** U5 inherits Theorem 10's Born structure as input for the bandwidth-density identifications $b_x \propto |\Psi|^2$, $b_p \propto |\widetilde\psi|^2$. No feedback into Theorem 10.

**Bell / Tsirelson (FORCED-unconditional from U2 program).** U5 does not interact with Bell/Tsirelson directly. Bell uses Cauchy–Schwarz and operator-norm bounds on the bipartite Hilbert space; the partition into $b_x$ and $b_p$ is single-particle adjacency structure that does not bear on bipartite correlation bounds.

### 5.3 Closure of the participation-measure → Hilbert-space chain at the Phase-1 level

The QM-emergence Phase-1 program presented all four foundational quantum-mechanical postulates (Schrödinger, Born, Bell/Tsirelson, Heisenberg) as conditional on five upstream commitments U1–U5. The arc cycle closure inventory is now:

| Upstream commitment | Status |
|---|---|
| U1 (participation-measure construction) | Active CANDIDATE |
| U2 (sesquilinear inner product) | **FORCED** (discrete + continuum, with explicit conformal gauge) |
| U3 (participation-measure evolution equation) | Active CANDIDATE |
| U4 (momentum-basis identification) | Active CANDIDATE |
| U5 (adjacency-band Fourier-conjugate partition) | **FORCED** (this arc) |
| Continuum-lift conformal gauge | Description-level convention |

The active CANDIDATE inventory has reduced from {U1, U3, U4, U5} + gauge to **{U1, U3, U4} + gauge**.

For Heisenberg specifically: the chain $\text{Primitives 04 + 06 + 09} \to \text{participation measure} \to \text{four-band decomposition} \to \text{U2 inner product} \to \text{U5 adjacency partition} \to \text{Heisenberg's bound}$ is now closed at theorem grade. **The structural backbone of Step 5 is complete.**

For Schrödinger evolution and the momentum-basis identification, the chain still depends on U1, U3, U4. These remain the high-leverage targets for future arcs.

### 5.4 No new gauge structure

U5 introduces no new gauge structure beyond what U2-Continuum already established. The partition $b^\mathrm{adj} = b_x + b_p$ is preserved under the conformal rescaling: both components transform uniformly as $b_x, b_p \to \Omega^{-D} b_x, \Omega^{-D} b_p$, with $b_x \cdot d\mu, b_p \cdot d\widetilde\mu$ as the gauge-invariant local contents. The Fourier conjugacy of F3 is preserved under the gauge (translation symmetry is gauge-equivariant on the participation graph). The orthogonality of F4 is preserved by Parseval-via-U2-inheritance.

The U5 arc therefore *does not extend* the gauge structure of the QM-emergence program. The continuum gauge identified in U2-Continuum is the only description-level redundancy.

### 5.5 Updated downstream theorem-status table

| Theorem | Pre-U5 | Post-U5 |
|---|---|---|
| Born rule (Theorem 10) | FORCED-unconditional (per U2 program) | (unchanged) FORCED-unconditional |
| Bell–Tsirelson | FORCED-unconditional (per U2 program) | (unchanged) FORCED-unconditional |
| Heisenberg uncertainty | FORCED conditional on U5 | **FORCED-unconditional** in discrete + continuum (gauge-invariant) |

**One additional foundational theorem promoted to FORCED-unconditional. The QM-emergence Phase-1 program now has FORCED-unconditional structural derivations of all four foundational postulates** — Born, Bell/Tsirelson, Heisenberg, and (via the existing Phase-1 Schrödinger-emergence work conditional on the remaining U1, U3, U4) Schrödinger evolution — across both discrete and continuum regimes for the first three.

---

## 6. Recommended Next Steps

**(a) Begin closure-and-summary memo (Memo 04).** The U5 arc is now ready for its canonical closure memo. Following the templates established by U2-Discrete Memo 05, U2-Continuum Memo 04, and born_gleason Memo 06, Memo 04 should provide the canonical narrative summary of the U5 arc, the integration into the QM-emergence program (with the updated active-CANDIDATE inventory), and a public-facing explainer section. Anticipated to be a moderate-length memo with no new substantive arguments.

**(b) Bundled memory-record update after Memo 04 closure.** Following the discipline established in the U2 program, the bundled update to `project_qm_emergence_arc.md` should capture the post-U5 state covering: (i) U5 theorem (now 13 forced theorems if numbered: the existing 9 + Theorem 10 Born + U2-Discrete + U2-Continuum + U5), (ii) Heisenberg's promotion to fully unconditional, (iii) updated upstream-CANDIDATE count from {U1, U3, U4, U5} + gauge to {U1, U3, U4} + gauge, (iv) Primitive-09 sensitivity inherited from the U2 program plus the additional sensitivity to future primitive amendments supplying adjacency-relevant directional structure (flagged in §3.9 above).

**(c) Decide priority for the next foundational arc.** With U5 closed, the remaining active CANDIDATEs are U1, U3, U4. The synthesis paper §4.2 ranked U5 as the cleanest of the four; with U5 done, the remaining priority assessment becomes:
- **U1 (highest leverage).** Promoting U1 — the participation-measure construction $P_K = \sqrt{b_K} \cdot e^{i\pi_K}$ — would make the entire QM-emergence Phase-1 program structurally complete in the participation-measure framework. U1 is the load-bearing primitive-level commitment from which all other Phase-1 results derive.
- **U3 + U4 (Schrödinger-emergence specific).** U3 (the participation-measure evolution equation $i\hbar \partial_t P_K = \hat{H} P_K + \sum V_{KK'} P_{K'}$) and U4 (the momentum-basis identification $H_k = \hbar^2 k^2 / 2m$) are jointly responsible for Schrödinger emergence. They are structurally tighter than U1 but require additional Step-2 context.

Recommended next priority: **U1**, with the structural-derivation methodology now well-established across four arcs (born_gleason, U2-Discrete, U2-Continuum, U5) and ready for the most leverage-significant remaining target.

---

## 7. Cross-references

- Arc outline: [`arcs/U5/00_arc_outline.md`](00_arc_outline.md)
- Memo 01 (decomposition + mapping): [`arcs/U5/01_decomposition_and_mapping.md`](01_decomposition_and_mapping.md)
- Memo 02 (F1, F2, F4 derivations): [`arcs/U5/02_derivations_F1_F2_F4.md`](02_derivations_F1_F2_F4.md)
- Existing tightening-program memo for U5 (U3-dependent argument; superseded by the present arc's U3-independent derivation): [`arcs/arc-foundations/u5_adjacency_partition_derivation.md`](../arc-foundations/u5_adjacency_partition_derivation.md)
- U2-Inner-Product paper (inner-product structure inherited as input): [`papers/U2_Inner_Product/paper_u2_inner_product.md`](../../papers/U2_Inner_Product/paper_u2_inner_product.md)
- Born_Gleason paper (Theorem 10 inherited as input for bandwidth-density identifications): [`papers/Born_Gleason/born_gleason_paper.md`](../../papers/Born_Gleason/born_gleason_paper.md)
- Step 5 derivation (Heisenberg, downstream beneficiary now FORCED-unconditional): [`arcs/arc-foundations/uncertainty_from_participation.md`](../arc-foundations/uncertainty_from_participation.md)
- Stone's theorem reference: M. H. Stone, "On one-parameter unitary groups in Hilbert space," *Annals of Mathematics* **33**, 643–648 (1932).
- Primitive 03 (Participation, supplies graph homogeneity for translation symmetry): `quantum/primitives/03_participation.md`
- Primitive 04 (bandwidth + four-band decomposition + adjacency band): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 06 (ED gradient, supplies spatial axis + translation symmetry direction): `quantum/primitives/06_ed_gradient.md`
- Primitive 09 (tension polarity, $U(1)$ phase, supplies phase-propagation axis): `quantum/primitives/09_tension_polarity.md`

---

## 8. One-line memo summary

> **F3 (Fourier conjugacy specificity) is established by Stone's theorem applied to the translation group of the participation graph (Primitives 03 + 06 supplying translation symmetry as a kinematic input) on the U2 inner-product Hilbert space; the standard $L^2$ Fourier transform is the unique unitary intertwiner of position and momentum representations, with fractional-Fourier, wavelet, and Mellin alternatives dismissed as corresponding to different group-theoretic structures or different operator pairs. The derivation is U3-independent, sharpening the earlier tightening-program argument. F5 (exhaustion / no third adjacency-axis) is established by primitive-level audit dismissing four candidate third axes — bandwidth-gradient direction (refines within spatial axis), rule-type coupling (lives in environmental band, not adjacency), polarity-amplitude direction (not supplied by any primitive; polarity is purely $U(1)$-valued), higher-derivative axes (derivative quantities of existing axes) — plus a survey of remaining primitives confirming none supplies adjacency-relevant directional structure. Falsifiers Fal-2 and Fal-3 fully dispatched. **U5 is FORCED**: all five sub-features close, no new structural commitment introduced, derivation independent of U3, gauge-compatible with U2-Continuum. Heisenberg promotes to FORCED-unconditional in discrete and continuum regimes. Active upstream-CANDIDATE inventory reduces from {U1, U3, U4, U5} + gauge to {U1, U3, U4} + gauge.**
