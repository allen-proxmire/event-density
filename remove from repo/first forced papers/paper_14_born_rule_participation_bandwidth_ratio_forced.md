# The Born Rule via Participation-Bandwidth Ratio is FORCED

**Paper #14 of the Event Density Forcing Series (Wave 2, Paper 4)**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) Forcing Papers — Paper #14 of the program
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The Born rule was forced in Paper #2 via two routes (direct + Gleason-Busch). This paper supplies a standalone forcing of the **operational route**: the rule is read off as the bandwidth-fraction governing commitment-event outcomes. **Given the substrate primitives of Paper #1 plus Primitive P11 (commitment with environmental phase-randomization on a uniform $U(1)$ distribution) and bandwidth additivity (P04)**, the quadratic form is forced by the participation-measure identity $|P_K|^2 = b_K$ — bandwidth is the substrate-level non-negative additive quantity, and the participation-measure identity makes the rule quadratic by *construction*. The substantive substrate content is therefore: the rule is quadratic because $|P_K|^2 = b_K$ at the primitive level. Linear, higher-power, contextual, signed, and non-additive alternatives are excluded. The claim is conditional: the phase-randomization-on-uniform-$U(1)$ primitive (P11) is load-bearing. Why the substrate has uniform-$U(1)$ phase-randomization is upstream content for the Primitive-Forcing Meta-Paper. **Honest reading**: this paper does not derive the Born rule independently of P11; it shows that *given* P11's uniform-phase-randomization, the quadratic form is forced. The uniform-$U(1)$ assumption is itself a substantial structural commitment closely tied to the P09 polarity primitive.

---

## 1. Framing

### 1.1 Why a second derivation of the Born rule?

Paper #2 of this series established the Born rule via two routes, treating them as twin proofs converging on the same conclusion. The Gleason-Busch route operates at the **structural level**: channel-primitivity forces non-contextuality, bandwidth additivity forces σ-additivity, the participation-measure structure supplies the Hilbert-space arena, and Gleason's theorem (with Busch's POVM extension for $d = 2$) produces a unique density operator $\rho$ with $f(E) = \text{Tr}(\rho E)$.

The **operational route** of Paper #2 operates differently. It starts from the substrate's pre-commitment coherent state, applies environmental phase-randomization at commitment (a structural feature of Primitive P11), and reads off the Born rule as the bandwidth-fraction governing the resulting incoherent mixture. The argument is operational in flavor — frequencies in repeated experiments converge to the rule — whereas Gleason-Busch is axiomatic.

The present paper extracts the operational route from Paper #2 and presents it as a standalone forcing argument. The motivation is twofold:

1. **Independent verification.** Two structurally distinct derivations of the same result provide over-determined forcing. If one route had a hidden flaw, the other would still establish the conclusion.
2. **Conceptual transparency.** The operational route makes the *physical* origin of the quadratic rule more explicit: $|P_K|^2 = b_K$ is the substrate-level bandwidth, and the Born rule is just the bandwidth-fraction. The "$|\Psi|^2$" of standard QM is bandwidth-ratio under another name.

### 1.2 The puzzle

Why $|\Psi|^2$ rather than $|\Psi|$, $|\Psi|^4$, or any other power? Standard answers:
- **Gleason's theorem**: the quadratic form is the unique probability measure on projector lattices in dimension $\geq 3$.
- **Born's original argument** (1926): the squared modulus matches experiment.
- **Decision-theoretic** (Deutsch 1999, Wallace 2003): the quadratic rule follows from rationality axioms in Everettian frameworks.
- **Envariance** (Zurek 2003): environmental symmetry of entangled states forces the quadratic weight.

Each derivation operates within a specific framework with framework-specific axioms. The substrate-level question — *why does the world have a probability rule quadratic in amplitude at all?* — is answered differently in each, and not always with a clean substrate-level mechanism.

### 1.3 What this paper does

The Event Density (ED) framework supplies the substrate. Paper #1 establishes the participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ with $|P_K|^2 = b_K$ as the substrate-level identity. Paper #2 establishes the Born rule via Gleason-Busch reconstruction on the participation manifold. The present paper supplies the operational route:

1. The pre-commitment coherent state $\Psi = \sum_K P_K$ has squared modulus $|\Psi|^2$ containing diagonal (bandwidth) terms plus interference cross-terms.
2. **Environmental phase-randomization at commitment** — a substrate-level feature of Primitive P11 acting on Primitive P04's four-band structure — kills the cross-terms.
3. The post-commitment state is an **incoherent diagonal mixture** with channel-$K$ weight equal to $b_K = |P_K|^2$.
4. The natural probability measure on this mixture is the **bandwidth-fraction**: $\text{Prob}(K) = b_K/\sum_{K'} b_{K'} = |P_K|^2/\sum_{K'}|P_{K'}|^2$.
5. Operational frequencies in repeated commitment experiments converge to this fraction. This is the **Born rule**.

The quadratic form $|\Psi|^2$ is not a choice; it is the substrate-level identity $|P_K|^2 = b_K$ (Paper #1) carried through to the post-decoherence mixture. The "$|\Psi|^2$" of standard QM is the same $b_K = |P_K|^2$ relation in the thin-participation continuum limit.

**Series context.** Paper #2 forced the Born rule via twin routes (direct + Gleason-Busch). The present paper is the standalone Wave-2 forcing of the direct (operational) route. Together with Paper #2, the Born rule is over-determined-forced: two structurally distinct derivations converge on the same conclusion.

---

## 2. Claim

> **Forcing Theorem (Born via Bandwidth Ratio, conditional).** Let any substrate satisfy the conditions $\{C\}$ stated in §5 — *in particular: Paper #1 result, bandwidth additivity (P04), commitment-with-uniform-$U(1)$-phase-randomization (P11)*. Then operational frequencies of commitment outcomes converge to the bandwidth-fraction
> $$
> \text{Prob}(K \mid u) = b_K(u)/\sum_{K'} b_{K'}(u) = |P_K(u)|^2/\sum_{K'} |P_{K'}(u)|^2.
> $$
>
> *The uniform-$U(1)$ phase-randomization is load-bearing; it is what kills cross-channel coherence and produces the quadratic rule. Why the substrate has this primitive is upstream content.*

---

## 3. Scope

### 3.0 Primitive Inputs (postulated within the ED Generative Primitives System)

This paper takes the following Event Density (ED) substrate primitives as **postulated within the ED Generative Primitives System**:

- **P04 (bandwidth additivity):** required for $\sigma$-additivity of the probability rule.
- **P11 (commitment with uniform-$U(1)$ phase-randomization):** discrete substrate-level events at which interference cross-terms are killed by environmental phase-randomization, producing the post-commitment incoherent mixture.
- **Paper #1 result ($|P_K|^2 = b_K$):** the quadratic form inherits directly from the participation-measure identity.

The full 13-primitive Generative Primitives System is enumerated in the ED Foundations position paper (*The Event Density Framework: A 13-Primitive Generative System and Its Cross-Domain Reach*). The empirical case for the primitives rests on their downstream reach across domains. This paper's contribution: given the primitives above, operational frequencies of commitment outcomes converge uniquely to the bandwidth-fraction Born rule $\text{Prob}(K) = |P_K|^2/\sum_{K'}|P_{K'}|^2$. This is a complementary derivation route to Paper #2's Gleason-Busch reconstruction.

### 3.1 What is FORCED

- The **quadratic probability rule** $\text{Prob}(K) \propto |P_K|^2$.
- **Normalization** $\sum_K \text{Prob}(K) = 1$.
- **σ-additivity** over disjoint channel-subsets: $\text{Prob}(S \cup T) = \text{Prob}(S) + \text{Prob}(T)$ for disjoint $S, T$.
- **Operational frequency interpretation**: in the long-run limit of repeated commitment events at the same locus on independent identically-prepared chains, observed outcome frequencies converge to the bandwidth-fractions.
- **Phase-blindness** of the rule after commitment: relative phases $\pi_K - \pi_{K'}$ are present in the pre-commitment coherent sum but are killed by environmental phase-randomization in the post-commitment mixture.

### 3.2 What is INHERITED

- **Numerical value of $\hbar$**. Inherited via Madelung anchoring.
- **Empirical identification of $b_K$ with observed frequencies**. The substrate forcing produces $\text{Prob}(K) \propto b_K$ as a structural identity; the empirical content is that observed frequencies in laboratory experiments equal these substrate-level bandwidth fractions, requiring a substrate-to-apparatus correspondence that is empirical rather than derived here.
- **Specific commitment-trigger conditions**. The substrate-level mechanism that initiates a commitment event (environmental bandwidth growth past the individuation threshold) is itself a substrate primitive (P11); the specific environmental conditions producing commitment in any given experimental setup are empirical.

### 3.3 What is OUT OF SCOPE

- **POVM measurements and generalized effect-valued measurements**. Paper #2 §7.3 + Busch's theorem extend the Born rule to POVMs; the present paper covers the projective-measurement case (single-channel-outcome commitment events).
- **Continuous-spectrum measurements** (position, momentum). Discrete channel outcomes here; continuous extensions follow standard measure-theoretic routes.
- **Decoherence theory** as a foundational framework. The substrate-level phase-randomization mechanism of C4 is *not* decoherence theory in the standard sense — it is a primitive substrate feature, not a derived consequence of environmental coupling in a Hilbert-space framework.
- **Measurement-problem interpretation**. Whether commitment events are best understood as collapse, branching, or otherwise is a separate philosophical question; the substrate-level commitment primitive (P11) supplies the mechanism without specifying the interpretation.

---

## 4. Key Vocabulary

- **Substrate.** Pre-quantum primitive layer of the ED framework.
- **Channel.** Primitive structural pathway in the participation graph, indexed by $K$.
- **Participation bandwidth $b_K(u)$.** Non-negative real-valued primitive quantity on each channel at each locus.
- **Participation measure $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$.** Complex amplitude carrier from Paper #1, with $|P_K|^2 = b_K$.
- **Commitment event.** Discrete substrate-level event at which multi-channel participation collapses to a single channel $K^*$ (Primitive P11).
- **Four-band partition.** Substrate-level decomposition $b_K = b_K^\mathrm{int} + b_K^\mathrm{adj} + b_K^\mathrm{env} + b_K^\mathrm{com}$ (Primitive P04 §1.5).
- **Environmental phase-randomization.** Substrate-level feature of commitment: during a commitment event, the environmental band's growth induces independent random phase shifts $\delta_K$ on each channel.
- **Coherent sum / wavefunction.** $\Psi(u) = \sum_K P_K(u)$, the pre-commitment continuum object.
- **Incoherent diagonal mixture.** Post-commitment state with channel-$K$ weight $b_K$ and zero cross-channel coherence.
- **Bandwidth-fraction / Born rule.** $\text{Prob}(K) = b_K/\sum b_{K'} = |P_K|^2/\sum|P_{K'}|^2$.
- **Operational frequency.** Observed long-run frequency of outcome $K$ in repeated commitment events on identically-prepared chains.

---

## 5. Substrate Class $\{C\}$

### C1. Participation graph + channel structure (Primitives P03 + P07)

Discrete participation graph with channels at each locus, ontologically primitive.

### C2. Bandwidth with additivity (Primitive P04)

Non-negative bandwidth on each channel, additive across disjoint channels; four-band decomposition into internal, adjacency, environmental, commitment-reserve bands.

### C3. Polarity (Primitive P09)

$U(1)$-valued angular primitive on each channel.

### C4. Commitment events with environmental phase-randomization (Primitive P11)

Discrete commitment events at substrate vertices. The commitment trigger is environmental bandwidth growth past the individuation threshold (Primitive P10). During commitment, environmental coupling induces independent random phase shifts $\delta_K(u, t)$ on each channel, drawn uniformly from $[0, 2\pi)$. This is a substrate-level structural fact about commitment dynamics, *not* a derived consequence of any framework above the substrate.

### C5. Inherited results from Paper #1

The amplitude carrier is the complex-valued participation measure $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$ with $|P_K|^2 = b_K$ as the substrate-level identity. A reader who has not read Paper #1 may take this as a definitional premise.

### C6. No Born rule as input

The forcing argument invokes only C1-C5 plus standard mathematical infrastructure:
- Classical probability theory on incoherent mixtures (Kolmogorov axioms).
- The law of large numbers: empirical frequencies converge to underlying probabilities in the long-run limit.
- Standard complex-number arithmetic.

No Born rule, no Gleason theorem, no Hilbert-space measure axiom is assumed. (Paper #2 invokes Gleason's theorem as part of its Route B; the present paper does not.)

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. Linear amplitude rule.** $\text{Prob}(K) \propto |P_K|$ rather than $|P_K|^2$.

**A2. Higher-power rules.** $\text{Prob}(K) \propto |P_K|^\alpha$ with $\alpha \neq 2$. Includes quartic ($\alpha = 4$), non-integer exponents, and exponentially-suppressed rules.

**A3. Non-quadratic maps.** Probability rules that are non-power-law functions of amplitude — entropic functionals, logarithmic-amplitude rules, or other non-power-law assignments.

**A4. Nonlinear normalization.** Probability assignment using a non-linear normalization functional rather than the linear bandwidth-fraction $b_K/\sum b_{K'}$.

**A5. Contextual probability.** Probability of outcome $K$ depending on the partition $\mathcal{D}$ of $\mathcal{K}$ containing $K$: $\text{Prob}(K \mid \mathcal{D}) \neq \text{Prob}(K \mid \mathcal{D}')$ for distinct partitions both containing $K$.

**A6. Signed or negative probabilities.** Probabilities allowed to be negative; outcomes weighted by signed quantities with extraction procedure for empirical frequencies (e.g., Wigner quasi-probability).

**A7. Non-additive rules.** Probabilities of disjoint channel-subsets failing to sum: $\text{Prob}(S \cup T) \neq \text{Prob}(S) + \text{Prob}(T)$ for disjoint $S$ and $T$.

### 6.2 Mainstream alternatives

**B1. Born rule as postulate.** $\text{Prob}(K) = |\langle K | \Psi\rangle|^2$ adopted as foundational axiom of quantum mechanics with no derivation. Standard textbook treatment.

**B2. Gleason's theorem (Paper #2 Route B).** The quadratic form derived from axioms on probability measures over projectors. Distinct route from the present operational derivation.

**B3. Envariance (Zurek).** The quadratic rule derived from environmental-symmetry properties of entangled states. Environmental coupling structure taken as input.

**B4. Decision-theoretic / Deutsch-Wallace.** Quadratic rule derived from rationality axioms applied to agents in Everettian branches. Decision-theoretic substrate taken as input.

**B5. Many-worlds branch-weight rules.** Probability as branch-amplitude-squared in Everett interpretation, with branch-counting machinery taken as input.

**B6. Bohmian quantum equilibrium hypothesis.** Born rule postulated as the equilibrium distribution of hidden Bohmian particles. Pilot-wave dynamics + typicality argument taken as input.

**B7. Frequentist operational definition.** Born rule defined as the limiting frequency of repeated measurements, with the quadratic form fit to experimental data.

---

## 7. Constructive Necessity

The derivation has five steps.

### 7.1 Bandwidth-fraction definition

The substrate-level commitment-selection rule is
$$
\text{Prob}(K^* \mid u) := \frac{b_{K^*}(u)}{\sum_{K \in \mathcal{K}(u)} b_K(u)} = \frac{|P_{K^*}(u)|^2}{\sum_K |P_K(u)|^2},
$$
where the second equality uses the participation-measure identity $|P_K|^2 = b_K$ from C5.

**The quadratic form is built in by the substrate.** Paper #1 establishes $|P_K|^2 = b_K$ as the substrate-level identity (forced by U(1)-invariance + bandwidth additivity + Cauchy functional equation). Once $b_K$ is identified as the substrate-level non-negative quantity and the participation measure is the unique amplitude carrier, the bandwidth-fraction is automatically quadratic in amplitude. The Born rule's "exponent 2" is the same exponent 2 that appears in the participation-measure construction.

**Positivity** is automatic: $b_K \geq 0$ from C2.

**Normalization** is automatic: summing over $K^*$, $\sum_K \text{Prob}(K) = (\sum_K b_K)/(\sum_K b_K) = 1$.

### 7.2 Pre-commitment coherent state and interference

Before a commitment event, the chain's participation is distributed across multiple channels coherently. The coherent sum is
$$
\Psi(u, t) = \sum_K P_K(u, t) = \sum_K \sqrt{b_K(u, t)}\,e^{i\pi_K(u, t)}.
$$
Its squared modulus:
$$
|\Psi(u, t)|^2 = \sum_K |P_K|^2 + \sum_{K \neq K'} P_K^* P_{K'} = \sum_K b_K + \sum_{K \neq K'} \sqrt{b_K b_{K'}}\,e^{i(\pi_{K'} - \pi_K)}.
$$
The first term is the sum of bandwidths — real, non-negative. The second term contains **interference cross-terms** carrying relative-phase content $e^{i(\pi_{K'} - \pi_K)}$. In a pre-commitment coherent state, these cross-terms are physically meaningful: they govern interference phenomena (double-slit fringes, etc.).

If the bandwidth-fraction rule applied to $|\Psi|^2$ directly without addressing the cross-terms, the probabilities would depend on relative phases — contradicting the empirical phase-blindness of Born-rule outcomes. The next step shows how the substrate handles this.

### 7.3 Environmental phase-randomization at commitment

By C4, environmental coupling during a commitment event induces independent random phase shifts $\delta_K(u, t)$ on each channel, drawn uniformly from $[0, 2\pi)$:
$$
P_K(u, t) \to P_K(u, t)\,e^{i\delta_K(u, t)}.
$$

Each cross-term in $|\Psi|^2$ acquires a random phase factor:
$$
P_K^* P_{K'} \to \sqrt{b_K b_{K'}}\,e^{i(\pi_{K'} - \pi_K)}\,e^{i(\delta_{K'} - \delta_K)}.
$$

Averaging over the environmental ensemble (independent uniform $\delta_K$):
$$
\langle e^{i(\delta_{K'} - \delta_K)}\rangle_\mathrm{env} = \delta_{K, K'},
$$
where the right-hand side is the Kronecker delta (not the random phase). Cross-terms with $K \neq K'$ vanish on average.

The post-commitment squared modulus reduces to:
$$
\langle |\Psi(u, t)|^2\rangle_\mathrm{env} = \sum_K |P_K(u, t)|^2 = \sum_K b_K(u, t).
$$

**The substrate has converted the coherent pre-commitment state into an incoherent diagonal mixture.** All inter-channel coherence is destroyed; only the diagonal bandwidth content survives.

This is the substrate-level analog of standard QM's decoherence. In ED, it is a *primitive* mechanism (Primitive P11's commitment-trigger structure + Primitive P04's four-band decomposition), not a derived consequence of system-environment Hamiltonian coupling.

### 7.4 Post-commitment incoherent diagonal mixture

After environmental phase-randomization, the chain's state is the density-matrix-equivalent diagonal mixture
$$
\rho_\mathrm{post}(u) = \sum_K b_K(u)\,|K\rangle\langle K|,
$$
with each channel $K$ weighted by its bandwidth $b_K$. The off-diagonal terms (coherences) have been suppressed.

This is a **classical probability distribution** over channel labels: the chain is in channel $K$ with probability proportional to $b_K$, with no quantum interference between alternatives. Standard classical probability theory applies.

By Primitive P10 (individuation threshold), the chain must individuate into a single-channel outcome at commitment. The probability of selecting channel $K^*$ is the natural classical-probability measure on the diagonal mixture:
$$
\text{Prob}(K^* \mid u) = \frac{b_{K^*}(u)}{\sum_K b_K(u)}.
$$

This is the bandwidth-fraction of §7.1, now derived as the post-decoherence classical-probability measure rather than asserted as a definition.

### 7.5 Operational frequency convergence

Consider an experimental ensemble: $N$ independent identically-prepared chains at locus $u$, each subjected to a commitment event. The number of chains committing to outcome $K^*$ is $N_{K^*}$. The **operational frequency** is $f_{K^*} = N_{K^*}/N$.

By the law of large numbers applied to the post-decoherence classical mixture (§7.4),
$$
\lim_{N \to \infty} f_{K^*} = \text{Prob}(K^* \mid u) = \frac{b_{K^*}(u)}{\sum_K b_K(u)} = \frac{|P_{K^*}|^2}{\sum_K |P_K|^2}.
$$

This is the **Born rule** in its operational form: observed frequencies converge to bandwidth-fractions, which equal squared-amplitude ratios.

**Equivalence with Paper #2's Gleason-Busch route.** Paper #2 §7.2 establishes the same rule via non-contextuality + σ-additivity + the participation-manifold Hilbert space + Gleason's theorem. Paper #2 §7.1 establishes the same rule via the operational route given here. The two routes converge on the identical bandwidth-fraction expression $\text{Prob}(K) = |P_K|^2/\sum|P_{K'}|^2$, with the quadratic form forced in both by the substrate-level identity $|P_K|^2 = b_K$.

**The two routes use different premises.** Route B (Gleason-Busch) takes channel-primitivity as load-bearing for non-contextuality; the present route takes environmental phase-randomization at commitment as load-bearing for cross-term suppression. Either alone establishes the Born rule; together they over-determine it.

---

## 8. Exclusion Arguments

### 8.1 A1 — Linear amplitude rule $|P_K|$

A linear rule $\text{Prob}(K) \propto |P_K|$ contradicts the substrate-level identity $|P_K|^2 = b_K$ from C5 (Paper #1): bandwidth is the substrate-level non-negative quantity, and bandwidth is the *squared* modulus, not the unsigned modulus. Under the linear rule, $\text{Prob}(K) \propto \sqrt{b_K}$, which fails σ-additivity:
$$
\sqrt{b_{K_1} + b_{K_2}} \neq \sqrt{b_{K_1}} + \sqrt{b_{K_2}}
$$
for $b_{K_1}, b_{K_2} > 0$ (Minkowski). The Cauchy functional equation in §A.1 of Paper #2 shows that only $\alpha = 2$ preserves additivity. C2 (bandwidth additivity) forbids linear rules.

### 8.2 A2 — Higher-power rules $|P_K|^\alpha$, $\alpha \neq 2$

By the same Cauchy / Minkowski argument: the only exponent satisfying $(b_{K_1} + b_{K_2})^{\alpha/2} = b_{K_1}^{\alpha/2} + b_{K_2}^{\alpha/2}$ is $\alpha = 2$. C2 (additivity) forbids other exponents.

### 8.3 A3 — Non-quadratic maps

Entropic functionals, logarithmic-amplitude rules, and other non-power-law assignments fail σ-additivity by similar arguments: the only assignment respecting the bandwidth-additivity structure of C2 plus the participation-measure identity of C5 is the linear bandwidth-fraction, which by $|P_K|^2 = b_K$ is automatically quadratic in amplitude.

### 8.4 A4 — Nonlinear normalization

A non-linear normalization functional $\text{Prob}(K) = f(b_K, \{b_{K'}\}_{K'})$ with $f$ non-linear in $b_K$ would break the linear bandwidth-fraction structure of §7.4. Under the post-decoherence incoherent mixture (§7.4), the chain is in a classical probability distribution over channels, and the natural normalization is linear: dividing each $b_K$ by the total. Non-linear normalization would correspond to a non-classical probability assignment on the post-decoherence mixture — but the mixture is classical by construction (§7.4 eliminates all quantum coherence). C4 (environmental phase-randomization) forces the classical-probability structure.

### 8.5 A5 — Contextual probability

A partition-dependent probability $\text{Prob}(K \mid \mathcal{D})$ would require the bandwidth $b_K$ to depend on the partition. By C1 (channels are ontologically primitive — graph-substructures with intrinsic identity), each channel's bandwidth is determined by the channel itself, not by the organizational decomposition. Contextual rules violate channel-primitivity directly. This is the same channel-primitivity argument that Paper #2's Gleason-Busch route uses (Link 1) to derive non-contextuality.

### 8.6 A6 — Signed or negative probabilities

By C2, $b_K \geq 0$. The bandwidth-fraction $b_K/\sum b_{K'}$ inherits non-negativity automatically. Signed-probability rules would require either redefining bandwidth as a signed quantity (violating C2) or applying a sign-extracting procedure to bandwidth (no such procedure is supplied by the substrate). The Wigner quasi-probability distribution, which is famously signed, is a distribution on phase space whose marginals are probabilities; it is not a channel-selection probability and not in the present paper's scope.

### 8.7 A7 — Non-additive rules

Non-additive rules violate C2 (bandwidth additivity) directly: by definition, $b_{K_1 \cup K_2} = b_{K_1} + b_{K_2}$ for disjoint $K_1, K_2$, and the bandwidth-fraction inherits this additivity at the probability-rule level.

### 8.8 B1 — Born rule as postulate

Adopting the Born rule as a foundational axiom is *downstream* of the substrate forcing. The present paper produces the rule from substrate primitives; treating it as a postulate is a presentation choice.

### 8.9 B2 — Gleason's theorem (Paper #2 Route B)

Gleason's theorem produces the same rule via a structurally distinct route (non-contextuality + σ-additivity + Hilbert space → unique density operator). The two routes are *complementary*, not competing. Paper #2 covers both; the present paper extracts and stands the operational route as a standalone derivation. Both forcings converge on the same equation.

### 8.10 B3 — Envariance (Zurek)

Zurek's envariance derivation derives the quadratic rule from environmental-symmetry properties of entangled states. Under the substrate-conditions test, Zurek's environmental-coupling structure is a *specific implementation* of the substrate-level Primitive P11 + four-band P04 mechanism. The substrate-level mechanism is upstream of Zurek's framework; Zurek's argument is one possible Hilbert-space realization of substrate-level commitment with phase-randomization.

### 8.11 B4 — Decision-theoretic / Deutsch-Wallace

Decision-theoretic derivations operate on a different substrate — agent rationality + Everettian branches. The substrate is decision-theoretic, not physical. The present paper's forcing is on the *physical* substrate; the two are not directly comparable at the substrate level. Under the present forcing, agents reasoning coherently about substrate-level commitment outcomes will adopt degrees of belief consistent with the bandwidth-fraction — but the order of explanation is reversed from Deutsch-Wallace: the substrate forces the rule, and rational agents adopt it because the substrate forces it, not because their rationality alone requires it.

### 8.12 B5 — Many-worlds branch-weight rules

Many-worlds branch-weight rules operate within the Everett interpretation, with branch-counting machinery as input. Under the substrate-conditions test, Everettian branches are downstream of the substrate-level coherent-sum + commitment structure. The substrate forces the bandwidth-fraction directly; whether the resulting outcomes are reinterpreted as Everettian branches is a separate question about interpretation.

### 8.13 B6 — Bohmian quantum equilibrium hypothesis

Bohmian theory postulates the Born rule as the equilibrium distribution of hidden particles guided by the pilot wave. Under the substrate-conditions test, Bohmian theory is downstream of the substrate forcing: the substrate produces the bandwidth-fraction; whether this is reinterpreted as an equilibrium distribution of hidden particles is a separate ontological question. Bohmian theory takes a position on a different debate (hidden variables) and is not in the alternative-encodings space for the present forcing.

### 8.14 B7 — Frequentist operational definition

Defining the Born rule as the limiting frequency of repeated measurements is *part* of the present operational derivation (§7.5), not an alternative to it. The substrate forcing provides the structural mechanism (commitment + phase-randomization → incoherent mixture → bandwidth-fraction) and shows that the operational frequency *converges* to the substrate-derived value. A pure-frequentist definition without a substrate-level mechanism is incomplete; the present paper supplies the mechanism.

### 8.15 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 linear $\|P\|$ | C2 (additivity) | $\sqrt{b}$ rule violates Minkowski additivity. |
| A2 $\alpha \neq 2$ | C2 | Cauchy functional equation forces $\alpha = 2$. |
| A3 non-quadratic maps | C2 + C5 | Bandwidth-additivity + $|P|^2 = b$ identity force linear bandwidth-fraction. |
| A4 nonlinear normalization | C4 | Post-decoherence mixture is classical; classical-probability normalization is linear. |
| A5 contextual probability | C1 | Channel-primitivity forces partition-independence. |
| A6 signed probabilities | C2 | Bandwidth non-negative; no sign-carrying primitive. |
| A7 non-additive rules | C2 | Bandwidth additivity propagates to rule. |
| B1 Born as postulate | not in space | Downstream of substrate forcing. |
| B2 Gleason's theorem | complementary | Twin derivation; converges on same rule. |
| B3 envariance | downstream | Specific Hilbert-space realization of substrate-level mechanism. |
| B4 decision-theoretic | different substrate | Agent-rationality substrate; not directly comparable. |
| B5 many-worlds branches | downstream | Branches reinterpret substrate outcomes; same rule. |
| B6 Bohmian equilibrium | downstream | Hidden-variable interpretation of substrate-derived rule. |
| B7 frequentist definition | incomplete | Frequencies converge to substrate-derived rule; substrate supplies mechanism. |

**The Born rule via bandwidth-fraction is the unique substrate-derived operational probability rule.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier is identical to the empirical falsifier of standard QM:

**Any observed deviation from $|\Psi|^2$ in any properly controlled measurement falsifies the substrate forcing along with standard QM.**

Specific constraints:
- **Multi-slit interference experiments** test the σ-additivity at high precision (Sinha et al. 2010 constrained third-order interference to $\sim 10^{-3}$).
- **Atomic spectroscopy** tests Born to many-digit precision across the periodic table.
- **Trapped-ion / superconducting-qubit projective measurements** test Born in the engineered-quantum-system context.
- **Tests of alternative-exponent rules**: no observed deviation from $\alpha = 2$ in any experiment.

The substrate forcing predicts exactly $|\Psi|^2$ with no sub-Born corrections. Any reproducible deviation would refute both the substrate forcing and standard QM.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C6 (participation graph, bandwidth additivity, polarity, commitment with environmental phase-randomization, Paper #1 inherited, no Born rule as input) but supporting a non-bandwidth-fraction operational probability rule that survives the exclusion arguments of §8.

The author's claim is that no such substrate exists. Each alternative is dispatched by a specific substrate-condition violation. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

The Born rule is the bridge between substrate-level participation content and observable frequencies. Every quantitative quantum prediction depends on it.

**Bell-Tsirelson and Heisenberg uncertainty (Papers #3 and #11)** both build on the squared-modulus rule. The substrate-derived $|P_K|^2 = b_K$ identity is the structural source.

**Quantum-computing fidelity measurements** test the Born-rule structure in engineered systems. Substrate-derived agreement to current precision.

**Stern-Gerlach / projective spin measurements** test the bandwidth-fraction in two-channel systems. Born saturation observed in every test.

---

## Appendix A — Derivation Chain and Glossary

### A.1 The environmental-phase-randomization calculation — explicit

The coherent sum at locus $u$:
$$
\Psi(u) = \sum_K P_K(u) = \sum_K \sqrt{b_K}\,e^{i\pi_K}.
$$
Squared modulus:
$$
|\Psi|^2 = \sum_K b_K + \sum_{K \neq K'}\sqrt{b_K b_{K'}}\,e^{i(\pi_{K'} - \pi_K)}.
$$

Apply environmental phase-randomization (C4): each channel acquires an independent random phase $\delta_K \sim \mathrm{Uniform}[0, 2\pi)$:
$$
P_K \to P_K\,e^{i\delta_K} \implies P_K^* P_{K'} \to \sqrt{b_K b_{K'}}\,e^{i(\pi_{K'} - \pi_K)}\,e^{i(\delta_{K'} - \delta_K)}.
$$

Average over the environmental ensemble:
$$
\langle e^{i(\delta_{K'} - \delta_K)}\rangle = \int_0^{2\pi}\int_0^{2\pi}\frac{d\delta_K\,d\delta_{K'}}{(2\pi)^2}\,e^{i(\delta_{K'} - \delta_K)} = \delta_{K, K'}.
$$

For $K \neq K'$, the integral evaluates to zero by independent uniform averaging of each phase factor:
$$
\int_0^{2\pi}\frac{d\delta_K}{2\pi}\,e^{-i\delta_K} = 0.
$$

Therefore:
$$
\langle |\Psi|^2\rangle_\mathrm{env} = \sum_K b_K + \sum_{K \neq K'}\sqrt{b_K b_{K'}}\,e^{i(\pi_{K'} - \pi_K)}\cdot 0 = \sum_K b_K.
$$

Cross-terms vanish. Only diagonal terms (bandwidths) survive.

### A.2 Bandwidth-fraction as classical-probability measure on the diagonal mixture

The post-decoherence density:
$$
\rho_\mathrm{post}(u) = \sum_K b_K(u)\,|K\rangle\langle K|.
$$

Probability of single-channel outcome $K^*$ under classical-probability measure on the mixture:
$$
\text{Prob}(K^* \mid u) = \frac{\text{tr}(\rho_\mathrm{post}\,|K^*\rangle\langle K^*|)}{\text{tr}(\rho_\mathrm{post})} = \frac{b_{K^*}(u)}{\sum_K b_K(u)} = \frac{|P_{K^*}|^2}{\sum_K |P_K|^2}.
$$

The Born rule.

### A.3 Glossary

- **Bandwidth $b_K(u)$.** Primitive non-negative substrate quantity on each channel.
- **Born rule.** $\text{Prob}(K \mid u) = |P_K(u)|^2/\sum_{K'}|P_{K'}(u)|^2$.
- **Coherent sum / wavefunction.** $\Psi(u) = \sum_K P_K(u)$.
- **Commitment event.** Discrete substrate-level event (Primitive P11) collapsing multi-channel participation to single channel.
- **Environmental phase-randomization.** Substrate-level feature (C4): independent random phase shifts on each channel during commitment.
- **FORCED.** Derived from substrate primitives + standard mathematics, no additional commitments.
- **Four-band partition.** Primitive P04 §1.5 decomposition into internal / adjacency / environmental / commitment-reserve bands.
- **INHERITED.** Quantitative content ($\hbar$, empirical $b_K$-identification) used but not derived here.
- **Incoherent diagonal mixture.** Post-decoherence state with channel-$K$ weight $b_K$ and zero off-diagonal coherence.
- **Operational frequency.** Observed long-run frequency in repeated commitment experiments.
- **Participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$.** Complex amplitude carrier (Paper #1).
- **Substrate.** Pre-quantum primitive layer of ED.

### A.4 Source-repository citations (for ED-internal readers)

- `arcs/arc-foundations/born_rule_from_participation.md` — QM Step 3 derivation memo (the operational route).
- `arcs/born_gleason/05_synthesis_theorem10.md` — Paper #2's Gleason-Busch route (twin derivation).
- `walkthroughs/from_primitives_to_born_rule.md` — public-facing walkthrough.

These are *not* required reading for the present paper.

---

*End of Paper #14.*
