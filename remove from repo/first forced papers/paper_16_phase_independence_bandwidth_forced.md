# Phase-Independence of Bandwidth Values is FORCED

**Paper #16 of the Event Density Forcing Series (Wave 2, Paper 6)**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) Forcing Papers — Paper #16 of the program
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

That physical observables in quantum mechanics depend only on $|\psi|^2$ and are invariant under $\psi \to e^{i\theta}\psi$ — the global $U(1)$ phase redundancy — is one of QM's foundational structural facts. This paper shows that, **given the substrate primitives of Papers #1–#2 — specifically the structural distinction between bandwidth (P04, real, non-negative) and polarity (P09, $U(1)$-valued angular), and the participation-measure identity $|P_K|^2 = b_K$ from Paper #1** — phase-independence of bandwidth values is forced. The argument is structurally short: bandwidth is the substrate-level real-valued non-negative primitive, the participation measure carries it as the squared modulus, and the squared modulus is by construction $U(1)$-invariant. Bandwidth-derived observables (Born outcomes, kinetic content, uncertainty variances) inherit phase-independence. The claim is conditional on the substrate-level distinction between bandwidth and polarity as separate primitive quantities — itself a non-trivial structural commitment. **Honest reading**: this paper does not derive the global $U(1)$ gauge redundancy from "nothing"; it shows that *given* the substrate's primitive-level distinction between bandwidth (real, non-negative) and polarity ($U(1)$-angular), the redundancy is structurally inevitable. The result is closer to *making explicit* a consequence already latent in P04 + P09 + Paper #1 than to a new forcing theorem; we present it because the resulting clarity matters for downstream gauge structure.

---

## 1. Framing

### 1.1 What standard quantum mechanics assumes about phase

In standard quantum mechanics, the global phase of the wavefunction is **unobservable**. The state $\psi$ and the state $e^{i\theta}\psi$ for any constant $\theta \in U(1)$ produce identical physical predictions: the Born rule gives $|\psi|^2 = |e^{i\theta}\psi|^2$, expectation values of Hermitian operators are unchanged, and time evolution preserves the global phase relationship. The set of physical states is therefore the projective Hilbert space $\mathcal{H}/U(1)$ rather than the Hilbert space $\mathcal{H}$ itself.

The standard motivation is operational: no measurement distinguishes $\psi$ from $e^{i\theta}\psi$. Relative phases between different components of a superposition are observable (they produce interference patterns), but the global phase is not. This operational fact is usually stated as a postulate or motivated by example, not derived from a deeper structure.

A related structural fact is the **local** $U(1)$ gauge redundancy that enters electromagnetism: $\psi(x) \to e^{iq\alpha(x)/\hbar}\psi(x)$ together with $A_\mu \to A_\mu - \partial_\mu\alpha$ leaves the gauge-invariant action unchanged. This is the basis of Paper #5's gauge-field-as-rule-type result and Paper #8's DCGT gauge sector. But the global $U(1)$ phase-independence — the simpler, kinematic version — is the foundational fact on which the local gauge structure builds.

### 1.2 The puzzle

Why does nature treat the global phase as unobservable? Two related questions:

1. **Why $|\psi|^2$ and not $\psi$?** The Born rule (Papers #2, #14) gives outcome probabilities from $|\psi|^2$, which is phase-blind by construction. But this is a *consequence* of the choice; what *forces* the underlying observables to depend on the squared modulus rather than the wavefunction itself?

2. **Why $U(1)$?** Phase rotations form a circle group $U(1)$ — a specific symmetry. Standard treatments take this as given. What forces this specific symmetry, rather than $\mathbb{Z}_n$, $\mathbb{R}$, or some non-Abelian group?

A program seeking a substrate-level answer needs:

1. A substrate that supplies bandwidth and phase as primitive structural quantities.
2. A structural argument that bandwidth — the substrate-level non-negative quantity — depends only on $|P_K|^2$ and not on the phase of $P_K$.
3. A propagation argument that all physical observables inherit phase-independence from bandwidth.

### 1.3 What this paper does

The Event Density (ED) framework supplies the substrate. Paper #1 establishes the participation measure $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$ with the structural identity $|P_K|^2 = b_K$ — bandwidth equals the squared modulus of the participation measure, *by construction*. Paper #2 establishes the Born rule. Paper #11 establishes Heisenberg uncertainty via the adjacency-bandwidth partition. Paper #14 establishes the Born rule via the operational bandwidth-fraction route.

The present paper shows that **phase-independence of bandwidth values is forced** as a structural identity. The argument has three structural moves:

1. **Substrate-level definition.** Bandwidth $b_K$ is the substrate's non-negative real-valued primitive (C2 from Primitive P04). Phase $\pi_K$ is the substrate's $U(1)$-valued angular primitive (C3 from Primitive P09). These are *structurally distinct* substrate quantities — bandwidth is not phase, and phase is not bandwidth.

2. **Identity from Paper #1.** The participation measure carries bandwidth as $|P_K|^2 = b_K$ — bandwidth is the squared modulus of the complex carrier, not its argument. Under any phase transformation $P_K \to e^{i\theta_K}P_K$, the squared modulus is unchanged: $|e^{i\theta_K}P_K|^2 = |P_K|^2 = b_K$. Bandwidth is therefore *manifestly* phase-independent.

3. **Propagation to observables.** All substrate-level physical observables — Born-rule outcomes (Papers #2, #14), bandwidth-fractions, kinetic-energy content (Papers #6, #15), Heisenberg-bound variances (Paper #11) — are *bandwidth-derived* quantities. Each inherits phase-independence from the underlying bandwidth's phase-independence. The global $U(1)$ gauge redundancy of standard QM is the substrate-level statement that physical content lives in bandwidth, not in absolute phase.

This is the kinematic, foundational version of the gauge-redundancy result. Paper #5 forces the *local* $U(1)$ gauge structure and its extension to non-Abelian groups; the present paper supplies the *global* $U(1)$ phase-independence on which Paper #5 builds.

**Series context.** Paper #1 forced the participation measure with $|P_K|^2 = b_K$. Papers #2, #14 forced the Born rule from bandwidth-fractions. The present paper makes explicit the foundational structural fact that bandwidth itself is phase-independent — the substrate-level source of the global $U(1)$ gauge redundancy that Paper #5 then extends to local gauge structure.

---

## 2. Claim

> **Forcing Theorem (Phase-Independence, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Papers #1–#2 results, P04 bandwidth as real-non-negative scalar, P09 polarity as $U(1)$-angular*. Then bandwidth values are invariant under all phase transformations:
> $$
> b_K(u) = |P_K(u)|^2 = |e^{i\theta_K(u)}P_K(u)|^2.
> $$
> Bandwidth-derived observables inherit this phase-independence, forcing the global $U(1)$ gauge redundancy of the substrate-derived Hilbert-space arena.
>
> *Honest framing: this is making explicit a consequence of P04 + P09 + Paper #1, not deriving a new theorem from independent primitives.*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated within the ED Generative Primitives System)

This paper takes the following Event Density (ED) substrate primitives as **postulated within the ED Generative Primitives System**:

- **P04 (bandwidth as real-valued non-negative scalar):** distinct from the angular primitive.
- **P09 ($U(1)$-valued polarity as the unique angular primitive, structurally distinct from bandwidth):** the substrate-level structural distinction between bandwidth and polarity is what makes phase-independence non-trivially structural.
- **Papers #1–#2 results:** the participation measure identity $|P_K|^2 = b_K$ and the Born rule.

The full 13-primitive Generative Primitives System is enumerated in the ED Foundations position paper. The empirical case for the primitives rests on their downstream reach across domains. This paper's contribution — and its honest framing: the result is structurally short because the work is done by P04 + P09 + Paper #1. We present it as a standalone clarification because foregrounding the substrate-level origin of $U(1)$ gauge redundancy matters for downstream gauge structure (Paper #5). The result is that bandwidth-derived observables (Born outcomes, kinetic content, uncertainty variances) inherit phase-independence from the structural distinction between bandwidth and polarity.

### 3.1 What is FORCED

- **Phase-independence of bandwidth**: $b_K = |P_K|^2$ is invariant under $P_K \to e^{i\theta_K}P_K$.
- **Per-channel local phase redundancy**: the phase $\theta_K$ may be chosen independently for each channel and locus without affecting bandwidth content.
- **Global $U(1)$ gauge redundancy** of the substrate-derived Hilbert-space arena.
- **Inheritance by bandwidth-derived observables**: Born-rule probabilities, bandwidth-fractions, kinetic content, Heisenberg-bound variances are all phase-blind.
- **Substrate-level distinction between bandwidth (real, non-negative) and phase ($U(1)$-valued angular) primitives**: they are structurally separate quantities.

### 3.2 What is INHERITED

- **Numerical value of $\hbar$**. Inherited via Madelung anchoring.
- **Physical identification of gauge potentials**. The substrate-level $U(1)$ redundancy is forced; identification of the corresponding gauge field with the electromagnetic potential $A_\mu$ is the content of Paper #5 (and the substrate-level identification is value-layer / empirical).
- **Specific Hilbert-space basis labeling**. The choice of basis vectors $|K\rangle$ corresponding to channels is a labeling convention.

### 3.3 What is OUT OF SCOPE

- **Non-Abelian gauge structure** (Paper #5). The present paper covers the global $U(1)$ phase-independence; non-Abelian $SU(n)$ generalizations of gauge redundancy are downstream of Paper #5.
- **Local gauge invariance with covariant derivatives** (Paper #5). Local gauge transformations $\psi \to e^{iq\alpha(x)/\hbar}\psi$ together with $A_\mu \to A_\mu - \partial_\mu\alpha$ require the gauge-field rule-type of Paper #5.
- **DCGT continuum-limit gauge structure** (Paper #8). The discrete-to-continuum gauge translation operates downstream.
- **Relativistic gauge fields** and Lorentz-covariant gauge structure.
- **Quantum reference-frame physics**. Operational arguments about what is observable from different reference frames belong to a separate operational framework.

---

## 4. Key Vocabulary

- **Substrate.** Pre-quantum primitive layer of ED.
- **Channel.** Primitive structural pathway in the participation graph, indexed by $K$.
- **Participation bandwidth $b_K(u)$.** Non-negative real-valued primitive on each channel (Primitive P04).
- **Polarity $\pi_K(u)$.** $U(1)$-valued angular primitive on each channel (Primitive P09).
- **Participation measure $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$.** Complex amplitude carrier (Paper #1).
- **Phase transformation.** $P_K \to e^{i\theta_K}P_K$ for $\theta_K \in U(1)$. Global if $\theta_K$ is constant across channels and loci; local if $\theta_K$ depends on $K$ and $u$.
- **$U(1)$ gauge redundancy.** Property that physical content is invariant under phase transformations.
- **Bandwidth-derived observable.** Any physical quantity that depends on $b_K$ (or equivalently $|P_K|^2$) but not on $\pi_K$ (or $\arg P_K$) directly.
- **Physical observable.** Quantity that can be associated with a measurable outcome in a substrate-level commitment event or downstream measurement.

---

## 5. Substrate Class $\{C\}$

### C1. Participation graph + channel structure (Primitives P03 + P07)

Discrete participation graph with channels at each locus.

### C2. Bandwidth as non-negative real-valued primitive (Primitive P04)

$b_K(u) \in \mathbb{R}_{\geq 0}$ on each channel at each locus. Bandwidth is a primitive substrate quantity, *not* derived from any phase-carrying quantity. It is structurally real and non-negative.

### C3. Polarity as $U(1)$-valued angular primitive (Primitive P09)

$\pi_K(u) \in U(1)$ on each channel at each locus. Polarity is the substrate's $U(1)$-valued angular primitive, structurally distinct from bandwidth.

### C4. Inherited results from Papers #1-#15

- **Paper #1**: $P_K = \sqrt{b_K}\,e^{i\pi_K}$ with $|P_K|^2 = b_K$ as the substrate-level identity.
- **Paper #2 + #14**: Born rule $\text{Prob}(K) = |P_K|^2/\sum_{K'}|P_{K'}|^2$.
- **Paper #3**: sesquilinear inner product on the participation manifold.
- **Paper #11**: bandwidth-allocation inequality on the adjacency-band partition.
- **Paper #12**: momentum operator from spatial-translation symmetry.
- **Paper #15**: kinetic operator from adjacency-bandwidth-flow.

A reader who has not read Papers #1-#15 may take C4 as a definitional premise: the substrate carries the structures these papers establish.

### C5. No phase-dependence of bandwidth as input

The forcing argument invokes only C1-C4 plus the elementary identity $|e^{i\theta} z|^2 = |z|^2$ for $z \in \mathbb{C}$ and $\theta \in \mathbb{R}$.

No specific phase-redundancy property is assumed as input; it is produced by the forcing chain.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. Phase-dependent bandwidth.** Bandwidth defined as a function of both $|P_K|$ and $\pi_K$: $b_K = f(|P_K|, \pi_K)$ with $f$ non-trivially depending on $\pi_K$. For instance, $b_K \propto |P_K|^2 \cdot (1 + \epsilon\cos\pi_K)$ for some $\epsilon \neq 0$.

**A2. Nonlinear phase coupling.** Bandwidth contains nonlinear phase-coupling terms — e.g., $b_K = |P_K|^2 + g\,\text{Re}(P_K^2)$ for some $g \neq 0$, which would make bandwidth oscillate with twice the polarity frequency.

**A3. Real-valued participation measures.** Real-valued amplitude carrier $P_K \in \mathbb{R}$ with no phase content. Bandwidth becomes $b_K = P_K^2$ trivially (no $U(1)$ redundancy because no phase exists).

**A4. Multi-valued phase.** Phase $\pi_K$ admits multiple admissible values at each locus (branched-cover structure), with bandwidth potentially distinguishing between branches.

**A5. Discrete phase ($\mathbb{Z}_n$).** Phase is $\mathbb{Z}_n$-valued (discrete $n$-th roots of unity) rather than continuous $U(1)$. Bandwidth then has $\mathbb{Z}_n$ redundancy but not full $U(1)$ redundancy.

**A6. Phase-position coupling.** Bandwidth at locus $u$ depends on the relative phase $\pi_K(u) - \pi_K(u')$ between $u$ and an adjacent locus $u'$, not on $|P_K(u)|^2$ alone.

**A7. Non-Abelian phase structure for bandwidth.** Bandwidth lives in a non-Abelian group rather than $\mathbb{R}_{\geq 0}$, with the "phase" being non-Abelian rotation content. This blurs the bandwidth/phase distinction at the substrate level.

### 6.2 Mainstream alternatives

**B1. Phase-independence as postulate.** Global $U(1)$ invariance adopted as a foundational axiom of quantum mechanics: physical states are rays in Hilbert space, not vectors. No substrate-level derivation.

**B2. Hilbert-space $U(1)$ gauge freedom.** Phase redundancy interpreted as a mathematical gauge freedom of the Hilbert-space description, with the physical state being the equivalence class $[\psi]$ under $\psi \sim e^{i\theta}\psi$. Mathematical convention, not physical structural fact.

**B3. Classical wave-amplitude analogy.** Phase-independence motivated by analogy with classical wave amplitudes, where the magnitude $|A|$ is physically meaningful and the phase is observer-frame-dependent. Classical mechanics taken as input.

**B4. Density-matrix invariance.** Physical observables expressed via the density matrix $\rho = |\psi\rangle\langle\psi|$, which is invariant under $\psi \to e^{i\theta}\psi$. Density-matrix formalism taken as input.

**B5. Operational unobservability arguments.** Phase-independence motivated by the operational observation that no measurement distinguishes $\psi$ from $e^{i\theta}\psi$. Operational framework taken as input.

**B6. Wigner's theorem on symmetry.** The set of physical states is a projective Hilbert space, with $U(1)$ as the natural symmetry group for pure-state ambiguity. Wigner-symmetry framework taken as input.

---

## 7. Constructive Necessity

The derivation has three steps. The shortest forcing argument in the Wave 2 series.

### 7.1 Bandwidth is the squared modulus of the participation measure

By Paper #1's forcing theorem (and the substrate-level identity in C4 inherited from Paper #1):
$$
b_K(u) = |P_K(u)|^2 = P_K^*(u)\,P_K(u).
$$
Bandwidth is, by the substrate-level construction of the participation measure, the *squared modulus* of the complex amplitude carrier. It is real-valued (the modulus of a complex number is real), non-negative ($|z|^2 \geq 0$ for all $z \in \mathbb{C}$), and depends only on the magnitude of $P_K$ in the complex plane.

The structural argument behind this identity (recapped from Paper #1):
- $b_K$ is the substrate-level non-negative primitive (C2).
- $P_K$ is the complex-valued carrier forced by $U(1)$ polarity content + Frobenius classification + bandwidth additivity (Paper #1).
- The Cauchy functional equation $f(a + b) = f(a) + f(b)$ on the non-negative reals, applied to bandwidth additivity, forces the relationship $b_K = c\,|P_K|^2$ with $c = 1$ by normalization convention.

### 7.2 The squared modulus is $U(1)$-invariant

The standard arithmetic identity for complex numbers:
$$
|e^{i\theta}z|^2 = (e^{i\theta}z)^*(e^{i\theta}z) = e^{-i\theta}z^* \cdot e^{i\theta}z = z^*z = |z|^2.
$$

Applying this to the participation measure with $\theta_K(u) \in U(1)$ chosen independently for each channel and locus:
$$
|e^{i\theta_K(u)} P_K(u)|^2 = |P_K(u)|^2 = b_K(u).
$$

**Bandwidth is invariant under all phase transformations** $P_K \to e^{i\theta_K}P_K$ for any $\theta_K \in U(1)$, with $\theta_K$ allowed to depend on both channel index and locus independently.

This is a structural identity following from the algebra of the complex numbers + the bandwidth-as-squared-modulus identity of §7.1. It is *not* a postulate; it is a consequence of how bandwidth is structurally defined relative to the participation measure.

### 7.3 Phase-independence propagation to bandwidth-derived observables

All physical observables in the substrate-level framework are **bandwidth-derived**: they depend on $b_K$ (and aggregate functions of bandwidth) but not on $\pi_K$ or $\arg P_K$ directly. Specifically:

- **Born-rule outcomes** (Papers #2, #14): $\text{Prob}(K) = b_K/\sum_{K'} b_{K'} = |P_K|^2/\sum_{K'}|P_{K'}|^2$. Phase-blind by construction.
- **Bandwidth-fractions across partitions** (Paper #11's $b_x$, $b_p$; Paper #15's adjacency-bandwidth-flow): all defined in terms of bandwidth content, inherit phase-independence.
- **Inner-product values** (Paper #3): $\langle P \mid P\rangle = \sum_K \sum_u P_K^*(u)P_K(u) = \sum_K \sum_u b_K(u)$. The diagonal inner-product values are phase-independent.
- **Variance / spread of observables**: variances are bandwidth-weighted moments (Paper #11), inherit phase-independence.

**Off-diagonal inner-product values** $\langle P \mid Q\rangle$ for $P \neq Q$ contain *relative-phase* content $\pi_K^{(P)} - \pi_K^{(Q)}$, which is *not* phase-independent. This is exactly correct: relative phases between distinct states are physical (they govern interference); absolute phases of a single state are not. The $U(1)$ redundancy is on the *individual state*, not on the relative phase between two states.

This distinction is the substrate-level content of "global phase is unobservable, relative phase is observable." The substrate-level mechanism: bandwidth (a single-state observable) is phase-independent; inner-product cross-terms (two-state observables) carry relative-phase content.

### 7.4 The $U(1)$ gauge redundancy

The forced phase-independence of bandwidth + propagation to all bandwidth-derived observables means:

> Any two participation-measure states $P$ and $P'$ related by $P_K' = e^{i\theta_K}P_K$ for $\theta_K \in U(1)$ produce identical bandwidth content $b_K$ and identical bandwidth-derived physical observables.

This is the substrate-level definition of the **global $U(1)$ gauge redundancy**. The set of physically distinct states is $\mathcal{P} / U(1)$ — the projective participation manifold — rather than $\mathcal{P}$ itself.

The redundancy is *per-channel* and *per-locus*: $\theta_K(u)$ can be chosen independently for each $(K, u)$ without affecting bandwidth. This is stronger than a global constant-$\theta$ redundancy — it is a local $U(1)$-redundancy at each substrate vertex.

**Connection to Paper #5's gauge fields.** Paper #5 takes the substrate-level local $U(1)$ redundancy as input and shows that a gauge rule-type $\tau_g$ with participation measure $A_\mu$ is forced as the substrate-level carrier of the gauge structure. The present paper supplies the foundational source of that local $U(1)$ redundancy: it is the *kinematic* statement that bandwidth (the substrate's physical content) is phase-independent.

**Connection to Paper #11's adjacency-bandwidth partition.** Paper #11 used the U(1)-invariance of bandwidth to argue that the diagonal $\langle P \mid P\rangle = \sum b_K$ is $U(1)$-invariant in the variance calculations. The present paper makes that invariance explicit.

**Connection to Paper #14's operational Born rule.** Paper #14's environmental phase-randomization at commitment (Primitive P11) kills off-diagonal cross-terms; what remains is the diagonal bandwidth content, which is $U(1)$-invariant. The Born rule's phase-blindness is the operational manifestation of bandwidth's substrate-level phase-independence.

The composite result: **phase-independence of bandwidth is the substrate-level structural source of the $U(1)$ gauge redundancy of quantum mechanics**, with all bandwidth-derived observables inheriting phase-independence automatically.

---

## 8. Exclusion Arguments

### 8.1 A1 — Phase-dependent bandwidth

If bandwidth depended explicitly on $\pi_K$ — e.g., $b_K = |P_K|^2(1 + \epsilon\cos\pi_K)$ — the substrate-level identity $|P_K|^2 = b_K$ from Paper #1 would be violated. Paper #1's Cauchy-functional-equation argument forces $b_K = c|P_K|^2$ with $c$ a constant, not a phase-dependent function. C2 (bandwidth as non-negative real primitive) + C4 (Paper #1 inherited) jointly exclude phase-dependent bandwidth.

### 8.2 A2 — Nonlinear phase coupling

Terms like $b_K \propto |P_K|^2 + g\,\text{Re}(P_K^2)$ violate $U(1)$-invariance of bandwidth: under $P_K \to e^{i\theta}P_K$, $\text{Re}(P_K^2) \to \text{Re}(e^{2i\theta}P_K^2)$ depends on $\theta$. The substrate-level non-negativity of bandwidth (C2) further forbids such cross-quadratic terms because they can become negative for certain phase configurations. C2 + Paper #1 exclude nonlinear phase coupling.

### 8.3 A3 — Real-valued participation measures

Paper #1 establishes that the unique amplitude carrier consistent with substrate primitives is *complex-valued*: real-valued carriers fail to represent the $U(1)$ polarity (C3) faithfully. A real-valued $P_K$ would still have $b_K = P_K^2 \geq 0$ — trivially phase-independent because no phase exists. But this contradicts C3 (polarity is $U(1)$-valued, requiring a continuous phase carrier). Real-valued carriers are excluded at the carrier level by Paper #1's exclusion of A1.

### 8.4 A4 — Multi-valued phase

Multi-valued phase at each locus would require the substrate to distinguish between admissible branches. Bandwidth could potentially differ between branches, breaking phase-independence. However, multi-valued phases are excluded by Paper #1's exclusion of A7 (anyon-prohibition argument and well-posedness of polarity at each locus). C3 supplies single-valued polarity; multi-valued alternatives violate C3.

### 8.5 A5 — Discrete phase ($\mathbb{Z}_n$)

A discrete $\mathbb{Z}_n$-valued phase would give $\mathbb{Z}_n$ redundancy on bandwidth, not the full $U(1)$ redundancy. C3 supplies $U(1)$-valued polarity (continuous); $\mathbb{Z}_n$ is a proper subgroup, but the substrate forces the full continuous $U(1)$. Furthermore, Stone's theorem on spatial translations (Paper #12) requires a continuous $U(1)$ to support a continuous translation generator; $\mathbb{Z}_n$ does not support strongly continuous groups in the relevant sense. C3 + Paper #12 exclude discrete-phase alternatives.

### 8.6 A6 — Phase-position coupling

If bandwidth at $u$ depended on $\pi_K(u) - \pi_K(u')$ for adjacent $u'$, the substrate-level $b_K$ would not be a *local* quantity at $u$ but a *bilocal* quantity. This contradicts C2's local primitive structure: bandwidth is defined at each locus independently. Phase-position coupling is excluded by C2.

(Note: gauge-coupled covariant derivatives $D_\mu = \partial_\mu + iqA_\mu$ involve relative-phase content via the gauge field $A_\mu$. This is downstream of Paper #5 and operates on gradients of the participation measure, not on bandwidth itself. The substrate-level bandwidth $b_K(u)$ remains phase-independent and local; gauge coupling enters at the dynamical level via the gauge field.)

### 8.7 A7 — Non-Abelian phase structure for bandwidth

A non-Abelian "phase" for bandwidth would require bandwidth to live in a non-Abelian group rather than $\mathbb{R}_{\geq 0}$. This violates C2's specification of bandwidth as non-negative real-valued. Non-Abelian gauge structure (Paper #5's $SU(n)$ generalizations) lives in the *gauge-field rule-type* $\tau_g$, not in bandwidth itself. C2 forbids non-Abelian bandwidth structure.

### 8.8 B1 — Phase-independence as postulate

Adopting $U(1)$ phase-independence as a foundational axiom is *downstream* of the substrate forcing. The present paper produces it from substrate primitives; treating it as a postulate is a presentation choice.

### 8.9 B2 — Hilbert-space $U(1)$ gauge freedom

Treating phase-independence as a mathematical gauge freedom of the Hilbert-space description (with physical states as projective rays) takes the Hilbert space + gauge-freedom convention as input. Under the substrate-conditions test, the projective structure is *derived* from the substrate-level bandwidth-independence of phase, with the Hilbert space itself substrate-derived from Papers #1-#3. The projective structure is a downstream consequence, not an input.

### 8.10 B3 — Classical wave-amplitude analogy

Classical wave amplitudes have phase-frame-dependent representations, but this is a property of classical observer-frames, not a substrate-level structural fact. Under the substrate-conditions test, the substrate's bandwidth phase-independence is structural (built into $|P_K|^2 = b_K$); the classical analogy is downstream of the quantum framework, not upstream of it.

### 8.11 B4 — Density-matrix invariance

The density matrix $\rho = |\psi\rangle\langle\psi|$ is invariant under $\psi \to e^{i\theta}\psi$ by construction: $|e^{i\theta}\psi\rangle\langle e^{i\theta}\psi| = e^{i\theta}|\psi\rangle\langle\psi|e^{-i\theta} = |\psi\rangle\langle\psi|$. This is a *consequence* of the substrate-level phase-independence of bandwidth, not an independent derivation. Under the substrate-conditions test, the density-matrix formalism is one re-presentation of substrate-level bandwidth content; phase-independence is structurally upstream.

### 8.12 B5 — Operational unobservability arguments

Operational arguments motivate phase-independence by observing that no measurement distinguishes $\psi$ from $e^{i\theta}\psi$. Under the substrate-conditions test, this operational fact is a *consequence* of substrate-level commitment dynamics (Paper #2, #14): commitment outcomes depend on bandwidth (Born rule), and bandwidth is phase-independent (present paper). The operational unobservability is the empirical manifestation of substrate-level phase-independence.

### 8.13 B6 — Wigner's theorem on symmetry

Wigner's theorem on projective representations of symmetry groups is a mathematical result on Hilbert-space symmetries. Under the substrate-conditions test, the projective structure that Wigner's theorem operates on is itself substrate-derived. Wigner's theorem is downstream of the substrate forcing.

### 8.14 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 phase-dependent bandwidth | C2, Paper #1 | Cauchy equation forces $b_K = c|P_K|^2$; no phase-dependence. |
| A2 nonlinear phase coupling | C2 + $U(1)$-invariance | Cross-quadratic terms break $U(1)$-invariance and non-negativity. |
| A3 real-valued $P_K$ | C3 (Paper #1) | Real carriers fail to represent $U(1)$ polarity faithfully. |
| A4 multi-valued phase | C3 | Polarity is single-valued at each locus. |
| A5 discrete $\mathbb{Z}_n$ phase | C3 + Paper #12 | Substrate $U(1)$ is continuous; Stone's theorem requires continuity. |
| A6 phase-position coupling | C2 (locality) | Bandwidth is local at each substrate locus. |
| A7 non-Abelian bandwidth | C2 | Bandwidth is non-negative real-valued, not group-valued. |
| B1 phase-independence as postulate | not in space | Downstream of substrate forcing. |
| B2 Hilbert-space gauge freedom | not in space | Hilbert space and projective structure substrate-derived. |
| B3 classical wave analogy | not in space | Classical analogy is downstream of quantum framework. |
| B4 density-matrix invariance | not in space | Density-matrix invariance is a consequence of substrate phase-independence. |
| B5 operational unobservability | not in space | Operational consequence of substrate-level structure. |
| B6 Wigner's theorem | downstream | Operates on substrate-derived projective structure. |

**Phase-independence of bandwidth is the unique substrate-derived invariance property of $b_K$ under $U(1)$ phase transformations of $P_K$.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

Any reproducible observation of a physical observable that depends on the global phase of a quantum state (rather than on relative phases between different components of a superposition) would falsify the substrate forcing. Specific tests:

- **Tests of $|\psi|^2$ invariance under $\psi \to e^{i\theta}\psi$**: every quantum measurement that has been performed is consistent with global phase being unobservable. No counterexample has been reported.
- **Aharonov-Bohm phase**: the AB phase is a *relative* phase (between two paths) and is observable. The *global* phase remains unobservable, consistent with the substrate forcing.
- **Berry phase / geometric phases**: arise from cyclic evolution and represent the holonomy of the gauge structure (Paper #5 content). They are relative phases between initial and final states along a path, not global phases of a single state.
- **Squeezed-state experiments**: the Heisenberg-bound-saturating states have specific phase content, but the bandwidth content (variance products) is phase-independent.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C5 (participation graph, bandwidth and polarity as separate primitives, Papers #1-#15 inherited, no phase-redundancy as input) but in which bandwidth depends on the absolute phase of the participation measure. The author's claim is that no such substrate exists.

### 9.3 Downstream exposure

**Local $U(1)$ gauge structure (Paper #5).** The substrate-level local $U(1)$ phase-redundancy is the kinematic input that Paper #5 extends to local gauge fields. Without phase-independence of bandwidth, the gauge-field rule-type $\tau_g$ would not have a well-defined interface property.

**Born-rule phase-blindness (Papers #2, #14).** The Born rule's $|\psi|^2$ form inherits phase-independence from bandwidth.

**Density-matrix formalism.** $\rho = \sum_K b_K |K\rangle\langle K|$ in the post-decoherence diagonal mixture (Paper #14 §7.4) is manifestly phase-independent — the substrate-level statement of the density-matrix invariance.

**Projective Hilbert space.** The set of physical states is $\mathcal{H}/U(1)$, derived structurally from the substrate-level bandwidth invariance.

---

## Appendix A — Derivation Chain and Glossary

### A.1 The complex-number identity $|e^{i\theta}z|^2 = |z|^2$ — explicit

For $z \in \mathbb{C}$ and $\theta \in \mathbb{R}$:
$$
|e^{i\theta} z|^2 = (e^{i\theta}z)^*(e^{i\theta}z) = e^{-i\theta}z^*\cdot e^{i\theta}z = e^{-i\theta + i\theta}\,z^*z = e^0 \cdot |z|^2 = |z|^2.
$$

The cancellation of the phase factors $e^{i\theta}$ and $e^{-i\theta}$ is the structural source of $U(1)$ phase-invariance of the squared modulus. Applied to the participation measure:
$$
|e^{i\theta_K(u)} P_K(u)|^2 = |P_K(u)|^2 = b_K(u).
$$
Bandwidth values are unchanged.

### A.2 The propagation argument

Every substrate-level physical observable is a bandwidth-derived quantity. Specifically:
- $\text{Prob}(K) = b_K/\sum b_{K'}$ (Born rule, Papers #2, #14).
- $\langle P \mid P\rangle = \sum b_K$ (Paper #3 inner product, diagonal).
- $\Delta x \cdot \Delta p$ (variance products, Paper #11) computed from bandwidth-weighted moments.
- $T = b_p$-mediated kinetic content (Papers #6, #15).

Each is a function of $\{b_K\}$ alone, with no $\pi_K$-dependence beyond the absolute-phase content $|P_K|^2 = b_K$. Phase transformations $P_K \to e^{i\theta_K}P_K$ leave each unchanged.

**Off-diagonal cross-terms** $P_K^* P_{K'}$ for $K \neq K'$ do contain relative-phase content $\pi_{K'} - \pi_K$. These are observable in interference experiments. The forcing argument is specifically about *bandwidth* (single-state diagonal content), not about cross-state observables.

### A.3 Glossary

- **Bandwidth $b_K(u)$.** Non-negative real-valued substrate primitive on each channel (Primitive P04).
- **Bandwidth-derived observable.** Physical quantity depending on $b_K$ but not on $\arg P_K$ directly.
- **Channel.** Primitive structural pathway in the participation graph.
- **FORCED.** Derived from substrate primitives + standard mathematics, no additional commitments.
- **Gauge redundancy.** Property that physical content is invariant under specified transformations.
- **INHERITED.** Quantitative content (numerical $\hbar$, gauge-potential identification) used but not derived here.
- **Local $U(1)$ phase-redundancy.** Invariance under $P_K(u) \to e^{i\theta_K(u)}P_K(u)$ for independently-chosen $\theta_K(u)$ per channel and locus.
- **Participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$.** Complex amplitude carrier (Paper #1).
- **Phase $\pi_K$ / $\arg P_K$.** $U(1)$-valued angular content of the participation measure.
- **Polarity (Primitive P09).** $U(1)$-valued angular substrate primitive.
- **Projective Hilbert space.** $\mathcal{H}/U(1)$; equivalence classes of states under global phase.
- **Substrate.** Pre-quantum primitive layer of ED.
- **$U(1)$ gauge structure.** Continuous abelian symmetry group of phase transformations.

### A.4 Source-repository citations (for ED-internal readers)

- `arcs/U1/04_closure_and_summary.md` — Paper #1's participation-measure derivation with $|P_K|^2 = b_K$ identity.
- `arcs/arc-foundations/participation_measure.md` — substrate-level participation-measure construction.
- `arcs/U2/04_synthesis_and_verdict.md` — Paper #3's sesquilinear inner product (diagonal phase-invariance + off-diagonal relative-phase content).
- `arcs/arc-Q/19_synthesis_memo_02_theorem_17.md` — Paper #5's gauge structure (downstream consequence of local $U(1)$ phase-redundancy).
- `walkthroughs/from_primitives_to_gauge_fields.md` — public-facing walkthrough on the gauge-redundancy chain.

These are *not* required reading for the present paper.

---

*End of Paper #16.*
