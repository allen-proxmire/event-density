# Arc E — Memo 6: Entanglement-Entropy Form — Form-FORCED, Coefficient-INHERITED

**Status:** Second substantive-derivation memo of Arc E. Conditional on E-1 (tensor product), E-2 (generic non-factorizability), E-3 (Schmidt FORM-FORCED), E-4 (monogamy FORM-FORCED with bandwidth-saturation reading available). Independent of E-5 (no-signaling). No new primitives. Identification-not-derivation discipline observed: standard Shannon–Khinchin theorem is identification target for the substrate-derived counting result.

**Date:** 2026-05-08

---

## 1. The CANDIDATE Statement

> **CANDIDATE (E6).** *Given E-1 (tensor product), E-3 (Schmidt decomposition), T10 (Born rule), ED-I-01 (multiplicity-as-entropy-analogue), P04 (bandwidth additivity for independent contributions), P11 (commitment irreversibility), and DCGT (substrate-to-continuum bridge), the entanglement entropy of a bipartite pure state $|\Psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$ is FORCED to take the Shannon–von Neumann form*
> $$S(\rho_A) = -k \sum_i \lambda_i \log \lambda_i = -k \,\mathrm{Tr}(\rho_A \log \rho_A),$$
> *where $\{\lambda_i\}$ are the Schmidt eigenvalues (E-3) and $k > 0$ is a multiplicative constant. The functional form is FORCED at the substrate level via Shannon–Khinchin uniqueness applied to ED's substrate counting; the constant $k$ is INHERITED from substrate units (logarithm base for information-theoretic units, $k_B$ for thermodynamic units).*

The CANDIDATE has three pieces, derived in order:

- **(H1) Probability-distribution claim.** The Schmidt eigenvalues $\{\lambda_i\}$ from E-3 form a probability distribution via T10 normalization, on which any substrate-derived entanglement-entropy functional $S$ must be defined.
- **(H2) Axiomatic uniqueness claim.** ED's substrate primitives (P04, P11, ED-I-01, DCGT) impose continuity, expansibility, additivity-for-independent-contributions, and strong-additivity / branching constraints on any entropy functional. These constraints are exactly Shannon–Khinchin's axioms, which uniquely select Shannon's $-\sum p_i \log p_i$ up to a multiplicative constant.
- **(H3) Coefficient-INHERITED claim.** The constant $k$ is not substrate-FORCED; it is INHERITED from the unit conventions chosen for the entropy (information-theoretic: $k = 1/\ln 2$ bits, $k = 1$ nats; thermodynamic: $k = k_B$).

E-6 is a substantive-derivation memo: (H1) is structural inheritance, (H2) is the load-bearing substrate-level axiomatic argument, (H3) is value-inheritance identification. The structural parallel to BH-5 (area-law form FORCED, coefficient INHERITED) is explicit.

---

## 2. Substrate Inputs (Inheritance)

| Input | Status | Role |
|---|---|---|
| **E-1** (tensor product FORM-FORCED) | Closed (this arc) | $\rho_A = \mathrm{Tr}_B(|\Psi\rangle\langle\Psi|)$ well-defined |
| **E-3** (Schmidt FORM-FORCED, values-INHERITED) | Closed (this arc) | Schmidt eigenvalues $\{\lambda_i\}$ are spectrum of $\rho_A$ |
| **E-4** (monogamy FORM-FORCED) | Closed (this arc) | Bandwidth-saturation reading: $S(\rho_A)$ measures fraction of A's bandwidth engaged with B |
| **T10** (Born rule) | FORCED-unconditional | $\sum_i \lambda_i = 1$, $\lambda_i \geq 0$ — probability distribution |
| **ED-I-01** (multiplicity-as-entropy-analogue) | Interpretation | Substrate entropy counts substrate-resolvable participation channels |
| **P04** (bandwidth additivity for independent contributions) | Primitive | Independent substrate contributions add — substrate-level additivity |
| **P11** (commitment irreversibility) | Primitive | Commitment events are irreversible — supports decomposition of compound measurements |
| **Q-COMPUTE Memo 1 invariants** ($\mathcal{M}, \mathcal{U}, \sigma$) | Closed-arc inheritance | $\mathcal{M}$ is substrate-multiplicity = ED's entropy-analogue |
| **DCGT** (substrate-to-continuum) | Closed-arc inheritance | Continuity and form-stability under coarse-graining |
| **BH-5** (area-law form-FORCED, coefficient-INHERITED) | Closed-arc inheritance | Identification target for the form-FORCED-coefficient-INHERITED pattern |
| **Standard Shannon–Khinchin axioms / theorem** | Free (mathematical) | Identification target: substrate-derived axioms map onto SK; uniqueness of Shannon entropy is mathematical |

**No new primitives.** **No use of E-5 (no-signaling) or E-7 (synthesis).**

---

## 3. Derivation of (H1): Schmidt Eigenvalues as Probability Distribution

By E-3 §3, the reduced density operator $\rho_A = \mathrm{Tr}_B(|\Psi\rangle\langle\Psi|)$ has spectral decomposition

$$\rho_A = \sum_{i=1}^{r} \lambda_i \, |i\rangle_A\langle i|_A, \qquad \lambda_i > 0, \qquad \sum_i \lambda_i = 1,$$

where $r$ is the Schmidt rank. By T10, $\lambda_i$ is the Born-rule probability of outcome $|i\rangle_A$ in a measurement on subsystem $A$ in the Schmidt basis.

**Operationally:** when measurement injects ED into A and forces individuation (ED-I-02 §6), $\lambda_i$ is the probability that the individuation lands on channel $i$. The substrate reads $\{\lambda_i\}$ as the *amplitude-weight distribution of the substrate-shared participation channels between A and B* (E-3 §5.1).

Any substrate-derived entanglement-entropy functional $S$ on a bipartite pure state must be a function of this probability distribution: $S(\rho_A) = S(\{\lambda_i\})$. The eigenbasis $\{|i\rangle_A\}$ is irrelevant to $S$ because $S$ is a function of the spectrum of $\rho_A$, not of any particular basis (this is a consequence of E-3's spectral-theorem construction; basis-changes within degenerate eigenspaces leave $\{\lambda_i\}$ invariant).

**(H1) is FORCED** as inheritance from E-3 + T10.

---

## 4. Derivation of (H2): Substrate-Level Shannon–Khinchin Axioms

The load-bearing substrate-level argument: derive each Shannon–Khinchin axiom from ED primitives.

### 4.1 Axiom S1 (Continuity)

> **S1.** $S(\{\lambda_i\})$ is a continuous function of the probabilities $\{\lambda_i\}$.

**Substrate justification.** DCGT (Diffusion Coarse-Graining Theorem) supplies the substrate-to-continuum bridge. Continuity of $S$ in $\{\lambda_i\}$ is required because:

- Substrate participation rules and shared-channel weights vary continuously under substrate-evolution (the $\lambda_i$ are eigenvalues of $\rho_A$, which depends continuously on $|\Psi\rangle$ per E-1's complex-Hilbert-space structure inherited from U2);
- Any substrate-derived macroscopic functional (counting, multiplicity, entropy-analogue) must be continuous in the substrate state, otherwise small substrate fluctuations would produce discontinuous macroscopic jumps — contradicting DCGT's continuity-preservation under coarse-graining.

If $S$ were discontinuous in $\{\lambda_i\}$, infinitesimal substrate perturbations could produce finite jumps in the macroscopic entropy — physically meaningless and DCGT-incompatible.

**S1 is FORCED** by DCGT + U2.

### 4.2 Axiom S2 (Maximality at uniform distribution)

> **S2.** For fixed $r$ (number of nonzero outcomes), $S(\{\lambda_i\})$ is maximized when $\lambda_1 = \lambda_2 = \cdots = \lambda_r = 1/r$.

**Substrate justification.** ED-I-01's multiplicity-as-entropy-analogue: substrate entropy is *the count of viable substrate-resolvable participation pathways*. For a fixed number of nonzero pathways $r$, the configuration with maximum substrate entropy is the one where *no pathway is preferred over any other* — equivalently, where each pathway carries weight $1/r$.

If one pathway were weighted higher than the others, the substrate would have a preferred channel — fewer effectively-distinct pathways — lower multiplicity — lower entropy. The uniform distribution is the only configuration with no preferred substrate channel.

This is ED-I-01's substrate analogue of the standard "maximum entropy ↔ maximum disorder" reading from thermodynamics.

E-4's bandwidth-saturation reading also confirms: maximum bandwidth saturation between A and B (maximally-entangled state) corresponds exactly to the uniform-$\lambda_i$ Schmidt distribution (E-4 §4.3).

**S2 is FORCED** by ED-I-01 + E-4 bandwidth-saturation.

### 4.3 Axiom S3 (Expansibility)

> **S3.** $S(\lambda_1, \lambda_2, \ldots, \lambda_r, 0) = S(\lambda_1, \lambda_2, \ldots, \lambda_r)$. Adding a zero-probability outcome does not change the entropy.

**Substrate justification.** A zero-Schmidt-coefficient term in the decomposition corresponds to an *unused substrate channel* — a participation pathway available in principle but not carrying any amplitude weight. Per ED-I-01 + Q-COMPUTE Memo 1 §2.2 (D1), substrate multiplicity counts *resolvable* pathways with nonzero contribution; unused channels contribute zero multiplicity.

If $S$ depended on the count of zero-weight channels, the entropy would be ambiguous: any state could be embedded in arbitrarily large Hilbert spaces by appending zero-weight Schmidt terms, and the entropy would depend on the embedding rather than the substrate state. This contradicts E-3's substrate reading of Schmidt rank as the *intrinsic* count of shared substrate channels.

**S3 is FORCED** by ED-I-01 + E-3 substrate reading.

### 4.4 Axiom S4 (Additivity for independent distributions)

> **S4.** For independent (i.e., (IP)-class) bipartite states with reduced distributions $\{p_i\}$ on $A_1$ and $\{q_j\}$ on $A_2$, the joint distribution is $\{p_i q_j\}$, and the entropy adds: $S(\{p_i q_j\}) = S(\{p_i\}) + S(\{q_j\})$.

**Substrate justification.** This is *exactly* P04 (bandwidth additivity for independent contributions) lifted from bandwidth to entropy via ED-I-01's multiplicity-as-entropy-analogue:

- **P04 substrate side:** Independent substrate channels' bandwidths add: $\Gamma_{12} = \Gamma_1 + \Gamma_2$.
- **ED-I-01 substrate side:** Substrate multiplicities of independent subsystems multiply: $\mathcal{M}(A_1 \otimes A_2)_{\mathrm{IP}} = \mathcal{M}(A_1) \cdot \mathcal{M}(A_2)$.
- **Entropy as $\log$ multiplicity:** $S(A_1 \otimes A_2)_{\mathrm{IP}} = \log[\mathcal{M}(A_1) \cdot \mathcal{M}(A_2)] = \log \mathcal{M}(A_1) + \log \mathcal{M}(A_2) = S(A_1) + S(A_2)$.

The substrate-level fact is multiplicativity of multiplicities for independent subsystems (ED-I-01); the entropy-as-log-multiplicity reading converts that multiplicativity to additivity. This is the same logarithmic relationship that makes Boltzmann's $S = k_B \log W$ work.

**S4 is FORCED** by P04 + ED-I-01.

### 4.5 Axiom S5 (Strong additivity / branching / recursivity)

> **S5.** $S(p_1, p_2, \ldots, p_n) = S(p_1 + p_2, p_3, \ldots, p_n) + (p_1 + p_2) S\left(\frac{p_1}{p_1 + p_2}, \frac{p_2}{p_1 + p_2}\right)$.

**Substrate justification.** This is the *decomposition* axiom: a measurement that distinguishes channels 1 and 2 from $\{3, \ldots, n\}$, followed conditionally on outcome $\{1, 2\}$ by a measurement that distinguishes 1 from 2, has total entropy equal to the entropy of the coarse measurement plus the conditional entropy of the fine measurement.

Substrate translation:

- **Coarse measurement (commitment to $\{1,2\}$ vs. $\{3,\ldots,n\}$):** P11 commitment irreversibility makes the coarse outcome a definite substrate fact. The substrate has *committed* to one branch, and the probability of each branch is given by Born + the coarse partition.
- **Fine measurement (conditional on coarse):** Given the substrate has committed to $\{1, 2\}$, the residual unresolvedness $\mathcal{U}$ (Q-COMPUTE Memo 1) over $\{1, 2\}$ has its own substrate entropy $S(p_1/(p_1+p_2), p_2/(p_1+p_2))$, weighted by the prior probability $p_1 + p_2$ that the substrate committed to that branch in the first place.
- **Total entropy:** the substrate's total un-resolved structure decomposes additively into coarse + (probability-weighted) conditional, because P11 makes the coarse commitment a definite fact that conditional measurements then operate on.

If S5 were violated, the decomposition of a measurement into coarse + fine stages would produce a different total entropy than a single measurement — contradicting P11 (which makes the staged decomposition substrate-equivalent to the single-stage measurement) and ED-I-01 (which counts pathway-multiplicity additively over commitment-event stages).

**S5 is FORCED** by P11 + ED-I-01 + Q-COMPUTE $\mathcal{U}$ structure.

### 4.6 Shannon–Khinchin uniqueness theorem

The Shannon–Khinchin theorem (Khinchin 1953; Faddeev 1956; Aczél et al.) establishes: any functional $S(\{\lambda_i\})$ satisfying S1 (continuity) + S2 (maximality at uniform) + S3 (expansibility) + S4 (additivity for independents) + S5 (strong additivity / branching) is uniquely of the form

$$S(\{\lambda_i\}) = -k \sum_i \lambda_i \log \lambda_i, \qquad k > 0.$$

The constant $k$ is unconstrained by S1–S5 alone — multiplying $S$ by any positive constant preserves all five axioms. Standard variants of Shannon–Khinchin (different axiom sets, e.g., Faddeev's reduced set) reach the same conclusion.

Substrate reading: §§4.1–4.5 derived S1–S5 from ED primitives. The mathematical theorem then identifies the substrate-derived axioms with the unique Shannon entropy form.

**(H2) is FORCED.**

---

## 5. Derivation of (H3): Coefficient $k$ INHERITED

### 5.1 What sets $k$?

The Shannon–Khinchin theorem leaves $k$ unconstrained. The choice of $k$ is fixed by the unit conventions adopted for the entropy:

- **Information-theoretic units (bits):** $k = 1/\ln 2$. Then $S$ is dimensionless, measured in bits, with maximum entropy of a uniform binary distribution equal to 1 bit.
- **Information-theoretic units (nats):** $k = 1$. Then $S$ is dimensionless, measured in nats.
- **Thermodynamic units:** $k = k_B$ (Boltzmann constant). Then $S$ has units of $J/K$ and identifies with the standard thermodynamic entropy via Boltzmann's $S = k_B \log W$.

None of these choices is substrate-FORCED. The substrate counts pathway multiplicities; the conversion from "pathway count" to "bits", "nats", or "Joules per Kelvin" is a unit convention.

### 5.2 ED's value-inheritance ledger

The framework already has analogous value-inheritance examples:

- **U4:** kinetic-energy form $\hat{p}^2/(2m)$ FORCED; mass $m$ INHERITED per Arc M.
- **BH-5:** area-law form $S \propto A$ FORCED; Bekenstein-Hawking coefficient $1/4$ INHERITED.
- **T19:** Newton's $G = c^3 \ell_P^2/\hbar$ FORCED; values $c, \ell_P, \hbar$ INHERITED.

E-6 inherits the same pattern: the Shannon-form $-\sum \lambda_i \log \lambda_i$ is FORCED; the multiplicative $k$ is INHERITED from unit conventions (information theory) or from substrate constants ($k_B$, expressed via $\hbar$, $c$, and substrate-density-of-states for thermodynamic identification).

For the von Neumann entanglement entropy in physical systems, the convention $k = 1$ (nats) or $k = 1/\ln 2$ (bits) is standard; for thermodynamic identification, $k = k_B$.

**(H3) is INHERITED.**

### 5.3 Cross-link to BH-5

BH-5 derived black-hole entropy as $S_{BH} \propto A/\ell_P^2$, with the coefficient (Bekenstein-Hawking $1/4$, or any equivalent normalization) INHERITED from V1-kernel structure + $\ell_P$-substrate-cutoff. The Bekenstein-Hawking coefficient is the BH-side instance of E-6's inherited coefficient: both originate as "log of motif count" or "log of substrate-channel multiplicity," and both have the substrate counting *form*-FORCED while the *coefficient* is set by substrate constants whose specific values come from outside the form-derivation.

E-6 + BH-5 are therefore the *same* form-FORCED-coefficient-INHERITED pattern applied to two different substrate-counting contexts (entanglement-channel multiplicity vs. horizon-motif multiplicity). This identification is part of E-7's synthesis content.

---

## 6. Audit of Non-Shannon Alternatives

Test alternative entropy functionals against the substrate-derived axioms S1–S5.

### 6.1 Tsallis entropy

Tsallis entropy: $S_q(\{\lambda_i\}) = \frac{1}{q-1}\left(1 - \sum_i \lambda_i^q\right)$ for $q \neq 1$.

- **S1 (continuity):** Satisfied for $q > 0$.
- **S2 (maximality at uniform):** Satisfied.
- **S3 (expansibility):** Satisfied.
- **S4 (additivity for independents):** **Violated.** Tsallis is *not* additive: $S_q(P \otimes Q) = S_q(P) + S_q(Q) + (1-q) S_q(P) S_q(Q)$ — contains a non-vanishing cross-term unless $q = 1$ (which is Shannon).
- **S5 (strong additivity):** **Violated.**

The S4 violation is the load-bearing one: Tsallis violates P04 + ED-I-01's multiplicative-multiplicity-for-independents at the substrate level. Substrate reading: Tsallis would require the multiplicity of two independent subsystems to *not* be the product of individual multiplicities — contradicting the substrate fact that independent participation contributions multiply (ED-I-01).

**Tsallis is substrate-refuted by P04 + ED-I-01.**

### 6.2 Rényi entropy

Rényi entropy: $S_\alpha(\{\lambda_i\}) = \frac{1}{1-\alpha} \log \sum_i \lambda_i^\alpha$ for $\alpha \neq 1$.

- **S1 (continuity):** Satisfied for $\alpha > 0$.
- **S2 (maximality at uniform):** Satisfied.
- **S3 (expansibility):** Satisfied.
- **S4 (additivity for independents):** Satisfied — Rényi *is* additive for product distributions.
- **S5 (strong additivity / branching):** **Violated.** Rényi entropy does not satisfy the Shannon-Khinchin recursivity axiom for $\alpha \neq 1$. Specifically, the conditional-decomposition $S(p_1, p_2, p_3) = S(p_1+p_2, p_3) + (p_1+p_2) S(p_1/(p_1+p_2), p_2/(p_1+p_2))$ holds for Shannon but not for Rényi.

The S5 violation is substrate-load-bearing: Rényi would require staged measurements (coarse + conditional fine) to produce a different total entropy than a single combined measurement — contradicting P11's substrate-equivalence of staged decompositions.

**Rényi is substrate-refuted by P11.**

### 6.3 Hartley entropy

Hartley entropy: $S_0(\{\lambda_i\}) = \log r$ where $r = |\{i : \lambda_i > 0\}|$.

- **S1 (continuity):** **Violated.** Discontinuous at boundary (a $\lambda_i$ transitioning from $0^+$ to $0$ produces a step).
- **S3 (expansibility):** Satisfied.
- **S4, S5:** Satisfied for support-size-only counting.

Hartley counts *which* channels are active, not how they are weighted. The substrate distinction is: ED-I-01 reads multiplicity as *amplitude-weighted* pathway count (Q-COMPUTE Memo 1's $\mathcal{M}$ + $\mathcal{U}$ structure), not just support-size. Hartley discards the amplitude information.

**Hartley is substrate-refuted by S1-violation under DCGT + E-3 amplitude-weighted reading.**

### 6.4 Min-entropy and max-entropy

Min-entropy: $S_\infty = -\log \max_i \lambda_i$. Max-entropy / Hartley: $S_0$ above.

Both are limit cases of Rényi at $\alpha \to \infty$ and $\alpha \to 0$ respectively. Both fail S5 (and S1 for $S_0$). Substrate-refuted by the same arguments as Rényi + Hartley.

### 6.5 Generalized entropies satisfying all five axioms?

The Shannon–Khinchin uniqueness theorem says: any functional satisfying S1–S5 *is* Shannon (up to multiplicative constant). So no "generalized entropy" satisfying all five axioms can be non-Shannon — this is a mathematical theorem, not a substrate result. The substrate's job is to derive S1–S5; once that is done (§4), Shannon is the unique entropy.

### 6.6 Audit summary

| Entropy candidate | S1 | S2 | S3 | S4 | S5 | Verdict |
|---|---|---|---|---|---|---|
| **Shannon** $-\sum \lambda_i \log \lambda_i$ | ✓ | ✓ | ✓ | ✓ | ✓ | **Selected by substrate** |
| Tsallis $S_q$, $q \neq 1$ | ✓ | ✓ | ✓ | ✗ | ✗ | Refuted by P04 + ED-I-01 |
| Rényi $S_\alpha$, $\alpha \neq 1$ | ✓ | ✓ | ✓ | ✓ | ✗ | Refuted by P11 |
| Hartley $S_0$ | ✗ | (✓) | ✓ | (✓) | (✓) | Refuted by DCGT + amplitude-weighting |
| Min-entropy $S_\infty$ | ✓ | ✗ | ✓ | (✓) | ✗ | Refuted by P11 + ED-I-01 |

**Shannon is the unique substrate-FORCED entropy form.**

---

## 7. DCGT Stability Under Coarse-Graining

The Shannon-form is stable under DCGT coarse-graining in the sense that:

- Substrate-level multiplicity counting at the discrete-substrate scale produces $S = \log \mathcal{M}$;
- Coarse-graining via DCGT to the continuum scale produces $S = -\sum \lambda_i \log \lambda_i$ where $\{\lambda_i\}$ is the continuum probability distribution;
- The two are continuous limits of one another: $\log \mathcal{M} \to -\sum \lambda_i \log \lambda_i$ as the substrate counting transitions from discrete-uniform-over-channels to continuum-weighted-distribution.

DCGT's continuity-preservation under coarse-graining therefore *forces* the Shannon-form at every scale: any counting that satisfies the substrate-level axioms at the discrete scale must satisfy them after coarse-graining as well (DCGT preserves S1–S5 by linearity-and-continuity preservation), and Shannon is the unique solution at every scale.

This stability is what BH-5's area-law derivation also exploits: substrate motif-counting at the horizon transitions to area-law continuum entropy via DCGT, with Shannon form preserved.

**DCGT closure is FORCED by §4 + DCGT-continuity-preservation.**

---

## 8. Verdict

> **VERDICT (E6): FORM-FORCED, COEFFICIENT-INHERITED.**
>
> The von Neumann entanglement-entropy form $S(\rho_A) = -k \sum_i \lambda_i \log \lambda_i$ is FORCED at the substrate level. (H1) Schmidt eigenvalues form a probability distribution via T10 (inheritance). (H2) ED's primitives derive each Shannon–Khinchin axiom: S1 from DCGT + U2; S2 from ED-I-01 + E-4 bandwidth-saturation; S3 from ED-I-01 + E-3; S4 from P04 + ED-I-01 (multiplicativity-of-independent-multiplicities lifted to entropy-as-log via standard Boltzmann mapping); S5 from P11 + ED-I-01 + Q-COMPUTE $\mathcal{U}$ structure. Shannon–Khinchin's uniqueness theorem then identifies Shannon as the substrate-FORCED form. (H3) The constant $k$ is INHERITED from unit conventions (information theory: $k = 1/\ln 2$ bits, $k = 1$ nats; thermodynamic: $k = k_B$). Audit of non-Shannon alternatives (Tsallis, Rényi, Hartley, min-entropy) refutes each on substrate-primitive grounds. DCGT preserves the form under coarse-graining. Structural parallel to BH-5 explicit.

**Verdict-class details:**

- **Form-FORCED:** the functional structure $-\sum_i \lambda_i \log \lambda_i$ as a function of the Schmidt-eigenvalue distribution.
- **Coefficient-INHERITED:** the multiplicative $k$ depends on unit convention or substrate-thermodynamic-constant choice; not substrate-FORCED.
- **No CONDITIONAL caveat survived the audit.** Each Shannon-Khinchin axiom is FORCED by named primitives without auxiliary assumption.
- **No NOT-FORCED option survived.** Every non-Shannon entropy candidate was refuted by at least one substrate primitive.
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.
- **Strong cross-link to BH-5.** Same form-FORCED-coefficient-INHERITED pattern; same substrate-counting-Shannon pipeline; identification with E-7 synthesis content.

---

## 9. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| E-4 (monogamy) used as derivation premise? | **E-4's bandwidth-saturation reading** is invoked in §4.2 (S2 axiom) only as a *cross-check* confirming ED-I-01's substrate reading, not as the derivation premise itself. The §4.2 derivation of S2 from ED-I-01 alone is sufficient; E-4 sharpens the physical reading. Removing E-4 from §4.2 would not change the verdict. |
| E-5 (no-signaling) used as derivation premise? | **No.** Not invoked. |
| E-7 (synthesis) used as derivation premise? | **No.** Not invoked. |
| Self-reference of E-6 within itself? | **No.** §3 → §4 → §5 → §6 → §7 derivation chain is acyclic. |
| E-1, E-2, E-3 used only as inputs? | **Confirmed.** E-1 supplies tensor product; E-2 supplies (IP) reading for S4; E-3 supplies Schmidt eigenvalues as the probability distribution argument of $S$. None re-derived. |
| Shannon's theorem used as input not as conclusion? | **Confirmed.** Shannon-Khinchin is a *mathematical theorem* (not an ED claim) that *identifies* the substrate-derived axiom set with the Shannon entropy form. Identification, not derivation. |
| BH-5 used as input not as conclusion? | **Confirmed.** BH-5's form-FORCED-coefficient-INHERITED pattern is identification target for E-6's structural parallel; not invoked as derivation step. |

**Acyclicity confirmed.**

---

## 10. Falsification

### 10.1 Falsifier for FORM-FORCED, COEFFICIENT-INHERITED verdict (current verdict)

A substrate counting rule satisfying P04, P11, ED-I-01, DCGT, T10, E-1, E-3, but producing a non-Shannon entropy form (i.e., a form not of the family $-k \sum \lambda_i \log \lambda_i$).

By Shannon–Khinchin uniqueness, this would require the substrate counting to violate at least one of S1–S5. By §4, each Sk follows from named primitives; refutation would require either:

- (a) Refuting one of P04, P11, ED-I-01, DCGT — i.e., refuting one of ED's primitives or interpretations; or
- (b) Showing that the §4 derivation of one of Sk from named primitives is logically flawed (e.g., a missing step or a hidden auxiliary assumption).

(a) is high-stakes structural refutation; (b) is logical-argument refutation. Neither has been identified by the audit.

### 10.2 Falsifier for CONDITIONAL verdict (rejected)

An auxiliary assumption beyond P04, P11, ED-I-01, DCGT, T10, E-1, E-3 that is required for the §4 axiom-derivations. The audit identifies none. The only auxiliary the candidate could have hidden is unit-convention selection for $k$ — and that is exactly what (H3) classifies as INHERITED, not auxiliary.

### 10.3 Falsifier for NOT-FORCED verdict (rejected)

A substrate construction satisfying all primitives but producing two distinct entropy forms (or no entropy form), with no substrate principle selecting between them. §4 derives a unique axiom set; Shannon-Khinchin uniqueness then forces a unique form. No room for ambiguity at the form level.

### 10.4 Empirical-side falsifier

An empirical demonstration of bipartite quantum entanglement entropy that follows a non-Shannon distribution — i.e., experimental data inconsistent with $S = -\sum \lambda_i \log \lambda_i$ for the experimentally-determined Schmidt eigenvalues. Standard quantum-state-tomography across many platforms confirms the von Neumann form to high precision; experimental falsification of this result would refute the entire framework of quantum information theory simultaneously, not just E-6.

### 10.5 Substrate-physics edge case

For systems with constraints that violate one of P04/P11/ED-I-01 in an isolated context, deviations from Shannon could in principle appear. Examples: long-range-correlated systems where independence (P04 prerequisite) fails, or systems with non-Markovian memory effects (P11 modulated). Per ED-I-02's substrate reading, such systems are *not* genuine independent-preparation configurations — they are partially-shared (SP)-class — and the §4 derivation is correctly inapplicable to them as a *substrate* fact. The Shannon form holds for the bipartite-pure-state entanglement entropy as defined; non-Shannon deviations in correlated systems are correctly read as *substrate non-independence* (which Tsallis attempts to capture phenomenologically), not as failures of the entropy form for genuinely-independent subsystems.

---

## 11. Consequences for the Arc

1. **E-6 closes as substantive-derivation memo.** The von Neumann entanglement-entropy form is FORCED at the substrate level via Shannon–Khinchin axioms derived from ED primitives. The constant $k$ is INHERITED. Standard form-FORCED-coefficient-INHERITED pattern, parallel to BH-5.

2. **Cross-domain unification with BH-5: substrate-counting → Shannon entropy pipeline.** Both BH-5 (area-law via horizon-motif counting) and E-6 (entanglement entropy via shared-channel counting) instantiate the same substrate-counting → log-multiplicity → Shannon-entropy pipeline. The two are different *substrate-counting contexts* (horizon motifs vs. shared participation channels) feeding into the *same* entropy form. This is part of E-7's synthesis content.

3. **Cross-domain unification with Q-COMPUTE: $\mathcal{M}$ as substrate-multiplicity.** Q-COMPUTE Memo 1's $\mathcal{M}$ is the *same* substrate quantity as ED-I-01's multiplicity-as-entropy-analogue. E-6's identification of $S = \log \mathcal{M}$ at the substrate scale + Shannon form at the continuum scale unifies Q-COMPUTE's multiplicity machinery with E-6's entanglement entropy — both are projections of one substrate counting structure.

4. **E-4 + E-6 jointly ground the bandwidth-saturation reading.** $S(\rho_A)$ measures bandwidth-engagement fraction (E-4 §11.5 + E-6 §4.2): low-rank Schmidt + concentrated $\lambda_i$ → low entropy → low bandwidth saturation; uniform-rank Schmidt → maximum entropy → maximum bandwidth saturation. The bandwidth-saturation reading is now formally derived rather than heuristic.

5. **E-7 synthesis is now structurally enabled.** With E-1 through E-6 all closed, E-7 can integrate:
   - Cross-domain echoes (BH-4 entanglement-straddling, Q-COMPUTE Class C plateau, BH-5 area-law)
   - Substrate-level over-determination patterns (E-5 three-lock, E-4 + Q-COMPUTE bandwidth budget, E-6 + BH-5 substrate-counting)
   - ER=EPR-class structural readings (entanglement and BH horizons share substrate-level mechanism via decoupling-surface bandwidth straddling + V1 cross-chain correlations + substrate-counting Shannon entropy).
   - Quantum vs. post-quantum characterization (Bell–Tsirelson 2√2 + no-signaling jointly).

6. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

7. **No new sensitivity flags beyond inherited ones.** E-6 inherits load-bearings on P04, P11, ED-I-01, DCGT — same as Q-COMPUTE and BH-5. No new load-bearings introduced.

---

## 12. Summary

**What this memo accomplished.**

- Stated the E-6 CANDIDATE (§1), decomposed it into (H1) probability-distribution claim, (H2) axiomatic uniqueness claim, (H3) coefficient-inheritance claim.
- Derived (H1) via E-3 + T10: Schmidt eigenvalues form a normalized probability distribution (§3).
- Derived (H2) via substrate-level Shannon–Khinchin axiom derivation (§4):
  - S1 (continuity) ← DCGT + U2;
  - S2 (maximality at uniform) ← ED-I-01 + E-4 bandwidth-saturation;
  - S3 (expansibility) ← ED-I-01 + E-3;
  - S4 (additivity for independents) ← P04 + ED-I-01;
  - S5 (strong additivity / branching) ← P11 + ED-I-01 + Q-COMPUTE $\mathcal{U}$.
- Identified Shannon–Khinchin uniqueness as the mathematical theorem connecting the substrate-derived axioms to the Shannon entropy form (§4.6).
- Articulated (H3) coefficient-inheritance: $k$ is fixed by unit conventions (info-theoretic) or substrate-thermodynamic constants ($k_B$, INHERITED from substrate via the same path as $\hbar$, $c$); structural parallel to BH-5 explicit (§5).
- Audited four non-Shannon entropy candidates (Tsallis, Rényi, Hartley, min-entropy) and refuted each on substrate-primitive grounds (§6).
- Confirmed DCGT preserves the form under coarse-graining at every scale (§7).
- Issued the verdict: **FORM-FORCED, COEFFICIENT-INHERITED** (§8).
- Confirmed acyclicity (§9) and provided substrate-level + empirical falsifiers (§10).
- Identified cross-domain unifications with BH-5 (substrate-counting → Shannon pipeline) and Q-COMPUTE ($\mathcal{M}$ as shared substrate quantity) for E-7 synthesis (§11).

**What this memo did not do.**

- Did not derive the *value* of $k$ in physical units. $k = k_B$ for thermodynamic identification is INHERITED from substrate constants via the same path as $\hbar$ (Madelung anchor) — flagged as out of scope here.
- Did not derive mixed-state entropy or quantum mutual information. Mixed-state structure was deferred at E-3; quantum-mutual-information, conditional entropy, and other compound quantities are downstream content. The pure-state bipartite entanglement entropy is the focus of E-6.
- Did not derive thermodynamic entropy at finite temperature. The substrate-counting-Shannon pipeline applies; explicit thermodynamic-derivation of $S = k_B \log W$ at finite-$T$ is downstream of a temperature-substrate memo (not currently in flight).
- Did not derive Rényi or Tsallis as effective entropies in substrate-non-independent contexts. Per §10.5, these are correctly read as substrate-non-independence indicators, but the explicit derivation of *which* generalized entropy applies *when* is downstream content if Arc E develops a non-independence-correction memo.

**Recommended next steps.**

1. **E-7 (next memo): Synthesis.** With E-1 through E-6 all closed, the synthesis memo can integrate the cross-domain echoes:
   - BH-5 (area-law) ↔ E-6 (entanglement-entropy) — same substrate-counting → Shannon pipeline.
   - BH-4 (entanglement-straddling) ↔ E-4 (monogamy) — same bandwidth-budget mechanism at different scales.
   - Q-COMPUTE Class C (correlation-budget plateau) ↔ E-4 (monogamy) — bipartite-projection of multipartite bandwidth ceiling.
   - Phase-1 Bell–Tsirelson 2√2 ↔ E-5 (no-signaling) — quantum-correlation characterization (vs. post-quantum PR-box).
   - ER=EPR-class structural reading (entanglement and BH horizon share substrate decoupling-surface mechanism).
   - Over-determination as recurrent ED structural feature (E-4 four-way, E-5 three-lock, E-6 axiomatic over-determination via multiple SK axioms each independently substrate-forced).
   
   Estimated 1–2 sessions.

2. **(Optional, low priority) O-E-Bandwidth-Map open item from E-4** — specific functional form $F: \Gamma \to E(\rho_{AB})$ — now sharpened by E-6: bandwidth-saturation fraction → entanglement-entropy bits via $-\sum (\Gamma_i/\Gamma_\mathrm{max}) \log(\Gamma_i/\Gamma_\mathrm{max})$ relationship. Could be closed in a focused 1–2 session memo if needed; otherwise defer.

3. **(Documentation) Phase-1 / Q-COMPUTE / BH-5 inheritance ledger update.** With E-1 through E-6 closed, the bipartite-entanglement portion of ED's inheritance footprint is fully substrate-justified. Documentation update across Phase-1, Q-COMPUTE, and BH-5 to reflect tightened ledger. Not blocking; cleanup pass when convenient.

---

**Pause for further instruction.**
