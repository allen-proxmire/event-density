# The Primitive-Level Arrow of Time in Event Density

**Author:** Allen Proxmire
**Collaborator:** Claude (AI collaborator)
**Date:** 27 April 2026
**Series:** Event-Density Foundational Theorems — Arc B

---

## Abstract

We close Arc B of the Event-Density (ED) program by establishing **Theorem 18 (Primitive-Level Retarded Kernel)**: the V1 vacuum response kernel established by Theorem N1 is uniquely forced at primitive level to have support restricted to the forward causal cone, so that the microscopic arrow of time arises as a structural consequence of the ED primitive ontology rather than as a thermodynamic, cosmological, or boundary-condition postulate. Taking Primitive 11 commitment-irreversibility as already-primitive, we establish the forcing argument by an explicit chain-contribution construction: V1 is a *response* kernel (Theorem N1) sourced by chain bandwidth content via the effective-vacuum factorisation of Theorem Q.8; chain bandwidth dynamics are forward-only along proper time by the joint structure of P11, P02, P04, and P13, so the chain forward-propagator $U_K(n,m)$ vanishes for $n<m$; the chain-summed kernel therefore inherits forward-cone-only support globally. Symmetric and advanced kernels demand backward chain contributions that are non-constructible at primitive level; hybrid variants are refuted by the same non-construction argument; PDE-level T-symmetry does not select among admissible Green's functions, so the primitive-level retardation cannot be undone by equation-level considerations. All six canonical falsifiers are dispatched (five dark, one conditional on the catalogue-exhaustion check). Cross-arc audits confirm strengthening rather than back-pressure: Arc N N1-E directionality is over-determined-forced via two independent routes; Arc Q.5 vacuum-polarisation analytic structure acquires a primitive-level structural foundation; Arc M F-M8 mediation refines to forward-only; Phase-3 Theorem GR1 lifts cleanly to a retarded curved-spacetime kernel via Hadamard-parametrix causal-future restriction. The primitive-level retarded kernel corresponds at continuum approximation to the standard retarded Green's function $G_R$; the symmetric Wightman correlator $W$, the Feynman propagator $G_F$, and the advanced Green's function $G_A$ remain distinct continuum objects unaffected by the primitive-level verdict. Theorem 18 advances the FORCED-theorem inventory from seventeen to eighteen and supplies the kernel-level foundation on which a follow-on thermodynamic-arrow arc (out of scope here) would build.

---

## 1. Introduction

### 1.1 Motivation: kernel-level versus thermodynamic arrow

The arrow of time is one of the persistent foundational asymmetries in physics. Its standard accounts fall into four broad categories: thermodynamic (entropy increase under low-entropy initial conditions), cosmological (alignment with the expansion of the universe), measurement-theoretic (irreversibility of quantum measurement), and electrodynamical (the Wheeler-Feynman selection of retarded over advanced Green's functions via causal boundary conditions). Each account secures a particular asymmetry by a particular mechanism, and each mechanism is treated as an external input to the relevant theory rather than as a derived structural consequence.

A *kernel-level* arrow is structurally distinct from these accounts. It is the asymmetry of the linear-response kernel that mediates vacuum response to perturbations of the substrate. In standard quantum field theory the kernel-level arrow is built into the iε prescription and the choice of retarded Green's function for causal response; it is correct and operationally indispensable, but it is also postulated rather than derived. The question this paper addresses is whether the kernel-level arrow can instead be *forced* — derived from primitive structural inputs — within a framework whose primitives include a candidate seed of asymmetry.

### 1.2 Why ED's primitives make the kernel-level arrow the correct target

Event Density commits at primitive level to discrete commitment events along chain worldlines, ordered by proper time. The ED Primitive 11 (commitment) carries the further commitment that committed events are non-reversible along the chain — a primitive-level analog of measurement-irreversibility in standard quantum mechanics. This irreversibility is direction-bearing in a way that no other ED primitive is: it picks a forward orientation for chain dynamics intrinsically, not by appeal to thermodynamic ensembles, cosmic expansion, or external boundary-condition selection.

The kernel-level arrow is the natural target because the V1 vacuum response kernel established by Theorem N1 is the structural site at which chain-level irreversibility could either propagate or fail to propagate. Theorem N1 fixes V1 as Lorentz-scalar, finite-width on the primitive event-discreteness scale $\ell_\mathrm{ED}$, sub-power-law-2 decaying, and bounded both ways by the V1-δ and V1-∞ refutations. It does not, however, explicitly fix retarded versus symmetric support: a Lorentz-scalar kernel can take both retarded form $\theta(t-t')\,G(\sigma)$ and symmetric form $G(\sigma)$ without violating any of N1's explicit fixes. This paper closes that previously-unfixed sub-feature.

### 1.3 Relationship to standard QFT causal structure

The result we establish is not a deviation from standard QFT causal structure but a primitive-level structural foundation for it. At continuum approximation, the primitive-level retarded V1 corresponds to the standard retarded Green's function $G_R$, which is itself related to the symmetric Wightman correlator $W$ by $G_R(x,y) = i\theta(t_x - t_y)\,[W(x,y) - W(y,x)]$. The Wightman correlator, the Feynman propagator $G_F$, and the advanced Green's function $G_A$ remain distinct continuum objects with their standard physical roles. Arc B's verdict applies specifically to the response kernel V1; it neither eliminates nor constrains the other Green's functions and correlators of the continuum theory.

The structural significance of the result is therefore foundational rather than phenomenological. ED matches standard QFT causal structure at all currently accessible scales; the primitive-level retardation supplies the structural origin of that causal structure rather than predicting empirically discriminating deviations. Discriminating signatures, when they appear, live at scales near $\ell_\mathrm{ED}$ — the same regime in which UV-finiteness becomes a directly probable property — and remain experimentally inaccessible at present.

### 1.4 Arc B in the ED program

Within the broader ED program, Arc B occupies the time-orientation position. The seventeen-theorem inventory at Arc B's opening comprised: form-level results in the relativistic and QM-emergence sectors (Theorems 1–7 and 10–16), the memory-kernel layer (Theorem 8 / Theorem N1), the gravitational-kernel layer (Theorem 9 / Theorem GR1), and the gauge sector (Theorem 17). Arc B adds the kernel-arrow / time-orientation structural layer, completing the picture of which structural features are forced at primitive level versus inherited as continuum-approximation effective machinery.

---

## 2. Background and Preliminaries

### 2.1 The ED primitive set (P01–P13)

The ED program operates on a primitive set comprising thirteen items. The subset directly load-bearing for Arc B's argument is:

- **P01 (event-discreteness):** discrete events on the event manifold, with primitive event-resolution scale $\ell_\mathrm{ED}$.
- **P02 (chain):** continuous worldline structures $\gamma_K$ with persistent identity, parameterised by proper time.
- **P03 (participation):** instantaneous, pointwise.
- **P04 (bandwidth):** four-band decomposition $b = (b^\mathrm{env}, b^\mathrm{ind}, b^\mathrm{int}, b^\mathrm{rel})$ with an update rule along $\gamma_K$.
- **P06 (four-gradient):** Lorentz-covariant differential structure on the event manifold.
- **P07 (rule-type, Lever L1):** structural rule-types $\tau_g$ specifying bandwidth partition patterns.
- **P09 (U(1) polarity phase):** polarity-valued field at each event.
- **P10 (individuation):** threshold-crossing event-class.
- **P11 (commitment):** discrete commitment events along $\gamma_K$. Commitment-irreversibility is taken as already-primitive throughout this paper.
- **P13 (relational timing):** finite proper-time intervals between commitment events along $\gamma_K$.

The remaining primitives P05, P08, P12 are direction-neutral under their standard functional readings; the forcing argument of this paper does not invoke them and is robust to their precise constitutional content.

### 2.2 Rule-type structure and the participation rule

The participation rule encoded by Primitive 07 specifies bandwidth partition patterns $w_\tau^X$ associated with structural rule-types $\tau$. Theorem 17 elevates rule-types as the carriers of gauge-field structure, so that the gauge field $A_\mu$ is identified as the participation measure of a structural rule-type $\tau_g$. The participation rule is direction-neutral in its definitional content; the application of $w_\tau^X$ to chain bandwidth content inherits whatever directionality the chain bandwidth dynamics carry.

### 2.3 Proper-time ordering

Primitive 13 supplies finite proper-time intervals along $\gamma_K$. Proper time alone is direction-neutral: increasing $\tau_K$ versus decreasing $\tau_K$ is a parameterisation choice. Joint with P11 commitment-irreversibility, however, $\tau_K$ acquires an oriented sequence: commitment-event indices $n = 1, 2, \ldots$ correspond to proper-time values $\tau_K^{(1)} < \tau_K^{(2)} < \ldots$, and the joint structure picks a forward orientation along the worldline.

### 2.4 Commitment irreversibility

Primitive 11 specifies that commitment events are discrete, ordered, and non-reversible. A committed event at proper time $\tau_K^{(m)}$ is a fact of the chain's past relative to any subsequent index $\tau_K^{(n)}$ with $n > m$, and is *not* a fact of the chain's past relative to any earlier index $\tau_K^{(n)}$ with $n < m$. This is the primitive-level seed of asymmetry: in conjunction with P02 and P13 it orients the worldline; in conjunction with P04 it fixes the bandwidth update rule as forward-only.

Three immediate consequences:

1. Each chain $\gamma_K$ has an intrinsically directed sequence of commitment events.
2. The chain's bandwidth field $b_K(\tau_K)$ is updated forward at each commitment event; bandwidth content acquired at $\tau_K^{(n)}$ is not retroactively undone at $\tau_K^{(n+1)}$.
3. The chain's contribution to the effective vacuum at any subsequent commitment event depends on its bandwidth content at the time of that contribution, not on its future commitments.

The third consequence is the structural bridge from chain-level irreversibility to vacuum-kernel-level retardation that this paper exploits.

### 2.5 Theorem N1 and the N1-E cascade

Theorem N1 (V1 finite-width vacuum memory kernel FORCED) was established by Arc N. Its content, fixed by the joint argument from primitive event-discreteness (P01), finite proper-time intervals (P13), and the UV-finiteness theorem of Arc Q.8 (Theorem 7), specifies that the vacuum-response kernel $K_\mathrm{vac}(x,x')$:

(i) exists; (ii) is Lorentz-scalar in the separation; (iii) is finite-width on $\ell_\mathrm{ED}$; (iv) is decaying with sub-power-law-2 falloff; (v) is bounded both ways by the V1-δ refutation (zero-width forbidden by C3) and the V1-∞ refutation (infinite-width forbidden by C1 and locality).

What N1 does *not* explicitly fix is the support specification: whether $K_\mathrm{vac}$ is retarded, advanced, symmetric, or admits both retarded and advanced support. A Lorentz-scalar kernel admits both $\theta(t-t')\,G(\sigma)$ (retarded) and $G(\sigma)$ unrestricted (symmetric); both satisfy N1's explicit fixes.

The N1-E cascade item (vacuum-induced bandwidth memory) was established as FORCED-conditional-on-V1: bandwidth-coupling to the vacuum is structurally inherent to the effective-vacuum framework, and the bandwidth-memory kernel inherits its kernel structure from V1. Whether the inherited kernel is retarded, symmetric, or advanced depends on V1.

### 2.6 Q.8 effective-vacuum factorisation

Theorem Q.8 establishes the multi-rule-type effective vacuum factorisation: the effective vacuum at any spacetime point is determined by the bandwidth content of the chain ensemble in its support, with cross-sector independence between distinct rule-types $\tau_g$. The factorisation supplies the chain-sourcing structure on which Arc B's forcing argument depends: the source of effective-vacuum response at any spacetime point is chain bandwidth content, with no non-chain-sourced contribution to the response kernel.

This is the load-bearing input for the chain-contribution construction in §6.

### 2.7 Response kernels versus Wightman correlators

Throughout this paper we maintain a strict distinction between two distinct two-point objects:

- **Response kernel $K_\mathrm{vac}(x,x')$.** The linear response of the effective vacuum at $x$ to a chain perturbation at $x'$. This is the object Theorem N1 establishes; it is what we refer to as "V1." Its physical role is causal mediation of perturbations.
- **Wightman correlator $W(x,y) = \langle 0 | \hat{\phi}(x)\hat{\phi}(y) | 0 \rangle$.** The intrinsic vacuum two-point function. This object measures unperturbed vacuum correlations and has the standard QFT property $W(x,y) = W^*(y,x)$.

The two objects are related at continuum approximation by the standard QFT identity
$$
G_R(x,y) = i\,\theta(t_x - t_y)\,[W(x,y) - W(y,x)],
$$
which expresses the retarded Green's function as a $\theta$-restricted combination of Wightman correlators. The retarded $G_R$ is the continuum-approximation correspondent of the primitive-level V1; the symmetric $W$ is a distinct object.

Failure to maintain this distinction is the most common conceptual error in arrow-of-time arguments at the kernel level. Arc B's verdict applies specifically to V1 (response kernel); $W$ is unaffected.

---

## 3. Problem Statement

### 3.1 The kernel-level arrow question

Given the ED primitive set (P01–P13), Primitive 11 commitment-irreversibility taken as primitive, Theorem N1 establishing the V1 vacuum response kernel's form class, and the Q.8 effective-vacuum factorisation supplying the chain-sourcing structure, *is the V1 kernel structurally forced to be retarded (forward-cone-only support), or is it admissible as symmetric or otherwise?*

A FORCED verdict requires the joint application of three conditions, by analogy to the criteria used in Arcs M, Q, and N:

- **Consistency (C1).** The candidate is consistent with primitives 01–13 plus all prior FORCED theorems.
- **Necessity (C2).** The candidate is required by primitive-level argument (uniquely sourced; or theorem closure breaks without it; or no admissible alternative survives).
- **Constraint compliance (C3).** The candidate satisfies all explicit constraints — Lorentz covariance, spin-statistics preservation, UV-finiteness, and continuum-approximation relativistic consistency (denoted CR).

A candidate that satisfies (C1) and (C3) but not (C2) lands as ADMISSIBLE-NOT-FORCED.

### 3.2 Primitive-level versus continuum-approximation objects

The arc operates at two layers, and clarity about which layer is in play is necessary throughout:

- **Primitive-level objects.** V1 (response kernel), chain forward-propagator $U_K(n,m)$, vacuum-coupling form-factors $\mathcal{F}_K$, the bandwidth update rule. These are the fundamental ED objects on which the primitive-level claim operates.
- **Continuum-approximation objects.** $G_R$ (retarded Green's function), $G_A$ (advanced), $G_F$ (Feynman), $W$ (Wightman correlator). These are continuum effective-theory objects derived from the underlying field theory; they correspond to primitive-level structures at long wavelengths.

The verdict of this paper is a primitive-level claim about V1, with a single explicit correspondence at continuum approximation (V1 retarded ↔ $G_R$). The other continuum objects are not constrained by the verdict.

### 3.3 Admissible inputs

The forcing argument of §6 invokes only:

- ED primitives P02, P04, P11, P13 directly (with P01 and P06 contributing to V1's existence via Theorem N1, not to the retardation question).
- Theorem N1 (V1 form-class fixes).
- Theorem Q.8 (effective-vacuum factorisation supplying chain-sourcing).

P05, P08, and P12 are not invoked; their constitutional content does not bear on the argument. Theorems 1–7, 10–16, and 17 are consistency-relevant but not derivation-relevant; the argument does not invoke them as premises.

This input restriction is methodologically important: it ensures that the forcing argument is mono-rooted in P11 commitment-irreversibility, with the chain-contribution construction as the unique structural path to the V1 retardation conclusion.

---

## 4. Catalogue of Candidate Arrow Sources

The catalogue stage of Arc B audited every plausible source of microscopic temporal asymmetry across the primitive set, the kernel structure, the memory-cascade structure, and the canonical PDE structure. We summarise the audit here.

### 4.1 Primitive-level candidates

Of the thirteen ED primitives, exactly one is direction-bearing primitively: **P11 commitment-irreversibility**. The remaining twelve fall into two classes:

- **Direction-neutral (P01, P03, P06, P09; P05, P08, P12 under standard functional readings):** carry no temporal direction; auxiliary infrastructure for the kernel-arrow argument.
- **Direction-inheriting (P02, P04, P07, P10, P13):** carry no temporal direction in isolation but inherit forward orientation through joint structure with P11.

The mono-rooted-in-P11 character of the primitive-level direction-bearing content is structurally important. It concentrates the forcing argument on a single primitive's carry-through soundness, and renders the verdict robust to verification flags on direction-neutral primitives (P05, P08, P12) since none of them is load-bearing.

### 4.2 Kernel-level candidates

Theorem N1 fixes V1's form class but leaves three kernel-level sub-features open at the catalogue stage: (i) the support-structure question — retarded, advanced, symmetric, or admissible-either-way; (ii) the boundary case BC3 of a symmetric finite-support kernel; (iii) the Synge-world-function ordering inherited from Theorem GR1 in curved spacetime. Of these, (i) is the load-bearing question of the arc; (ii) is the primary alternative that B.3 must close; (iii) is the cross-arc consistency check that B.4 audits.

### 4.3 Memory-level candidates (N1-E)

The N1-E vacuum-induced bandwidth memory cascade admits two readings of its directionality:

- **Cascade-from-V1.** N1-E inherits whatever directionality V1 has, via the vacuum-coupling channel. Structurally honest reading.
- **Direct-from-P11 (R1-bypass).** N1-E directionality arises directly from chain bandwidth-update dynamics (P11 + P04) without dependence on V1 directionality. Independent route.

Both routes are admissible structurally; both produce forward-only N1-E directionality if their respective premises hold. The redundancy is structurally important: even if the V1-cascade route failed, R1-bypass would independently force forward-only N1-E directionality.

### 4.4 PDE-level candidates

The canonical ED PDE structure at form level — Klein-Gordon-class second-order equations from the free-scalar QFT layer, Cl(3,1) signature from R.2.4, Dirac T-symmetric operator structure from R.3 — is direction-neutral. A second-order linear PDE is invariant under $t \to -t$ at the equation level; the Cl(3,1) signature distinguishes timelike from spacelike but not forward-timelike from backward-timelike; Dirac is T-symmetric under appropriate antiunitary T-transformation.

The kernel-arrow argument therefore *cannot route through the PDE*. PDE structure propagates whatever direction is supplied at the kernel-construction level but does not source direction independently.

### 4.5 Catalogue summary

| Source | Direction status | Load-bearing for V1 retardation |
|---|---|---|
| P01 event-discreteness | Neutral | No (auxiliary for V1 width) |
| P02 chain | Direction-inheriting | Yes (carry-through conduit) |
| P03 participation | Neutral | No |
| P04 bandwidth | Direction-inheriting | Yes (chain-update conduit) |
| P05, P08, P12 | Assumed neutral | No |
| P06 four-gradient | Neutral | No (Lorentz substrate) |
| P07 rule-type | Direction-inheriting (weak) | Indirect (T17 vacuum-coupling) |
| P09 U(1) phase | Neutral | No |
| P10 individuation | Direction-inheriting | Indirect (V5 cross-chain) |
| **P11 commitment** | **Direction-bearing primitively** | **Yes — load-bearing seed** |
| P13 proper-time | Direction-inheriting | Conduit (with P11) |
| V1 support structure | Direction-ambiguous | Self — load-bearing question |
| BC3 symmetric-finite | Symmetric | Primary alternative |
| N1-E cascade | Direction-inheriting | Inherits from V1 |
| N1-E R1-bypass | Direction-inheriting (independent) | Direct from P11 |
| KG / Dirac / Cl(3,1) PDE | Neutral | No (substrate only) |
| Synge $\sigma$ (Theorem GR1) | Symmetric metric | Cross-arc consistency check |

The catalogue is closed under interactions: every direction-bearing or direction-inheriting item routes through P11; no convergent secondary source exists.

---

## 5. The Forcing Chain

The forcing argument proceeds in five steps, plus a closure step that handles the symmetric and advanced alternatives at the kernel-construction level (the formal refutation of those alternatives is presented separately in §7).

### 5.1 V1 as a response kernel

V1 is the *response kernel*: the linear response of the effective vacuum at $x$ to a chain perturbation $\delta P_\mathrm{chain}(x')$ at $x'$. As established in Arc N (`non_markov_forced.md` §2), V1 is the kernel that propagates such perturbations through the substrate.

V1 is structurally distinct from the unperturbed Wightman correlator $W$. Where $W$ measures intrinsic vacuum correlations, V1 measures vacuum *response* to perturbations. This distinction is foundational for the forcing argument: the support structure of a response kernel depends on the dynamics of the sources that produce the response, whereas the support structure of an unperturbed correlator depends on the field theory's vacuum-state symmetries.

### 5.2 Response kernels require sourced contributions

A response kernel acts on perturbations propagated through the substrate. Its construction must therefore exhibit a sourcing structure: the perturbation enters through some specific channel and propagates from there.

By the Q.8 effective-vacuum factorisation, the source for V1 is chain bandwidth content. The effective vacuum at any spacetime point is determined by the bandwidth content of the chains in its support; perturbations of the substrate therefore enter through chain bandwidth, and V1 propagates such perturbations to the vacuum response at any other spacetime point.

There is no non-chain-sourced contribution to V1 as a response kernel. Non-chain-sourced contributions (intrinsic vacuum correlations) live in $W$, not V1. We will return to this point in §7.5 when we close the BC3 boundary case.

### 5.3 Forward-only chain dynamics

We now establish the temporal directionality of chain bandwidth dynamics.

Let $\{\gamma_K\}_{K=1}^N$ index the chains in the support of the effective vacuum at a given spacetime region. Each chain $\gamma_K$ is parameterised by proper time $\tau_K$ (P02 and P13). Commitment events along $\gamma_K$ occur at indices $n = 1, 2, \ldots$ with proper-time values $\tau_K^{(n)}$. By Primitive 11 commitment-irreversibility (taken as primitive throughout), these proper-time values are ordered increasingly with index: $\tau_K^{(n+1)} > \tau_K^{(n)}$.

A chain perturbation $\delta b_K^\mathrm{source}(\tau_K^{(m)})$ at commitment index $m$ on chain $K$ produces a perturbation in the chain's bandwidth content at later commitment events $n \geq m$ via the chain's *forward* bandwidth-update rule:
$$
\delta b_K(\tau_K^{(n)}) \;=\; \sum_{m \leq n} U_K(n, m) \cdot \delta b_K^\mathrm{source}(\tau_K^{(m)}),
$$
where $U_K(n, m)$ is the chain's forward bandwidth-propagator. The structural commitment of P11, jointly applied with P04 (bandwidth update rule) and P13 (proper-time ordering), yields:
$$
U_K(n, m) \;=\; 0 \quad \text{for} \quad n < m.
$$
That is, the chain forward-propagator vanishes on backward propagation. Bandwidth content at $\tau_K^{(n)}$ depends on chain history $\{\tau_K^{(m)} : m \leq n\}$ but never on future $\{\tau_K^{(m)} : m > n\}$.

### 5.4 Composition: V1 has forward-cone-only support

Combining the chain-update rule of §5.3 with the chain-vacuum-coupling rule of Q.8, the kernel relating a perturbation at $x'$ to a vacuum response at $x$ takes the form
$$
K_\mathrm{vac}(x, x') \;=\; \sum_{K} \sum_{n \geq m} \mathcal{F}_K(x; \tau_K^{(n)}) \cdot U_K(n, m) \cdot \mathcal{F}_K^\dagger(x'; \tau_K^{(m)}),
$$
where $\mathcal{F}_K(x; \tau)$ is the vacuum-coupling form-factor connecting the chain commitment at $\gamma_K(\tau)$ to the spacetime location $x$. The constraint $n \geq m$ is enforced by $U_K(n, m) = 0$ for $n < m$.

For a chain $\gamma_K$ with timelike worldline (P02 plus chain-causality), proper-time ordering $\tau_K^{(n)} \geq \tau_K^{(m)}$ maps to $(x_n^K - x_m^K)$ being in the forward causal cone of $\gamma_K$, where $x_n^K = \gamma_K(\tau_K^{(n)})$. Crucially, *all chains share the same time orientation*: P11 is universal across the chain ensemble, so every chain in the inventory has its own proper-time ordering aligned with the global forward direction. There is no "anti-chain" running backward in time, because P11 forbids un-commitment for any chain.

The chain-summed kernel therefore has globally forward-cone-only support:
$$
K_\mathrm{vac}(x, x') \neq 0 \;\Longrightarrow\; (x - x') \text{ lies in the forward causal cone}.
$$

### 5.5 V1 is RETARDED

Steps 5.1 through 5.4 establish that V1 has forward-cone-only support. This is the defining property of a retarded kernel:
$$
K_\mathrm{vac}^\mathrm{ret}(x, x') \;=\; \theta(t - t') \cdot G(\sigma(x, x') / \ell_\mathrm{ED}^2),
$$
where $G$ is the Lorentz-scalar function of the Synge world function $\sigma$ established by Theorem N1, and $\theta(t-t')$ is the time-orientation restriction supplied by the chain-contribution construction. The form factor $G$ retains all four explicit Theorem-N1 fixes (Lorentz-scalar, finite-width on $\ell_\mathrm{ED}$, sub-power-law-2 decaying, both-ways-bounded); the $\theta$-factor is the support-restriction refinement that B.2 establishes.

### 5.6 FORCED verdict

The chain-contribution construction is unique: V1 admits no construction other than the chain-contribution sum, because V1 is by definition the response kernel sourced by the chain ensemble (no non-chain-sourced contribution exists for the response part of the vacuum two-point structure). The construction admits only forward-cone support (by §5.3 and §5.4). Therefore V1 is uniquely retarded.

This satisfies the FORCED criterion's necessity condition (C2) by uniqueness: no admissible alternative construction exists. Consistency (C1) is satisfied by direct verification — retarded V1 is consistent with N1's explicit fixes, with Cl(3,1) signature (signature is metric, retardation is time-orientation), and with all Phase-2 theorems. Constraint compliance (C3) is satisfied: Lorentz covariance under the proper orthochronous Lorentz group $L_+^\uparrow$, spin-statistics preservation (vanishes at spacelike separations), UV-finiteness (multiplicative $\theta$-factor does not affect high-frequency behaviour), and continuum-approximation relativistic consistency (CR) via the response-kernel-vs-correlator distinction discussed in §8.6.

**V1 retardation is FORCED at primitive level.**

---

## 6. Refutation of Alternatives

The forcing argument of §5 establishes that V1 is uniquely retarded by uniqueness of construction. We now treat the candidate alternatives explicitly.

### 6.1 Symmetric V1 (BC3)

The symmetric kernel $K_\mathrm{vac}^\mathrm{sym}(x, x') = G(\sigma(x, x') / \ell_\mathrm{ED}^2)$ — Lorentz-scalar, finite-width, both-causal-cone support, time-reversal-invariant — satisfies all four explicit Theorem-N1 fixes and all four constraints C1, C2, C3, CR in isolation. It is the primary alternative to retardation.

For a symmetric kernel to arise from chain contributions, the kernel sum (§5.4) must produce non-zero terms with $\tau_K^{(n)} < \tau_K^{(m)}$ — that is, terms in which a perturbation at chain index $m$ propagates to chain index $n$ with $n$ earlier than $m$ along the chain's proper-time parameter. By §5.3, $U_K(n, m) = 0$ for $n < m$. There is no such term in the chain-contribution sum.

A symmetric kernel cannot be sourced by chain contributions. It would require a non-chain-sourced contribution to V1 — an intrinsic vacuum-correlation contribution. Such contributions exist at continuum approximation (the Wightman correlator $W$) but are *not* the response kernel V1; they are a different object. The response-kernel-vs-correlator distinction maintained throughout this paper is what closes this point.

The chain-propagator structure itself is independently incompatible with backward propagation. The chain forward-propagator $U_K(n, m)$ is a discrete sequence-construction object built by accumulating bandwidth updates step-by-step along proper time. It is not a relation that admits inversion at the level of chain bandwidth content under Primitive 04, and even if formally defined as an operator inverse, it would represent backward-in-proper-time propagation in conflict with P11.

**Symmetric V1 is REFUTED-by-non-construction.** The kernel form is constraint-compliant in isolation, but no primitive-level construction admitting it exists.

### 6.2 Advanced V1

The advanced kernel $K_\mathrm{vac}^\mathrm{adv}(x, x') = \theta(t' - t) \cdot G(\sigma)$ — backward-causal-cone-only support — fails on multiple structural grounds.

**Direct violation of P11.** Advanced V1 demands that *all* chain contributions come from future events: for every term in the chain-contribution sum, $\tau_K^{(n)} < \tau_K^{(m)}$. This requires the chain's commitment-event structure to run in reverse globally — backward-only chain dynamics across the ensemble. P11 commitment-irreversibility forbids this directly; it is not a partial violation in some sub-case but a global inversion of P11's direction-bearing content.

**Violation of P13 ordering.** Under P11+P13 jointly, proper-time intervals are ordered increasingly with chain index. Advanced V1 requires the inverse traversal: every contribution propagates from later to earlier proper time. P13 alone admits this, but P13 jointly with P11 does not.

**P07 application is structurally vacuous.** The participation rule of Primitive 07 specifies bandwidth partition patterns operating on chain bandwidth content. Under P11 plus P04, chain bandwidth content is accumulated forward; the partition rule operates on this forward history. Advanced V1 would demand the partition operate on future bandwidth — content that has not been accumulated, because forward chain dynamics have not yet reached it.

**N1-E cascade conflict.** Advanced V1 would force N1-E (vacuum-induced bandwidth memory) to depend on future bandwidth content: bandwidth at $\tau$ would be determined by $\{\tau_K^{(m)} : m > n\}$, contradicting P11 directly at the bandwidth-update level.

**Advanced V1 is REFUTED-by-multi-front-contradiction.** This is the cleanest refutation in the arc; every primitive-level structural feature points the same direction.

### 6.3 Hybrid variants

Four classes of hybrid kernels admit consideration:

- **(H1)** Forward-dominant plus small backward content: $K = \theta(t-t')\,G + \epsilon\,\theta(t'-t)\,G$ for $\epsilon > 0$.
- **(H2)** Angular-restricted backward support: backward content only in some spatial directions.
- **(H3)** Weighted symmetric: position-dependent weights $w_\mathrm{fwd}(x,x')$ and $w_\mathrm{back}(x,x')$ on forward and backward components.
- **(H4)** Symmetric core multiplied by directional envelope: $K = G_\mathrm{sym}(\sigma) \cdot E(t-t')$.

In each case, any non-zero backward-cone content requires non-zero $U_K(n, m)$ for some $n < m$. The amplitude $\epsilon$ of (H1) is irrelevant: the *type* of contribution required is forbidden, not its size. The angular restriction of (H2) is irrelevant: chain propagators have no spatial-angular selectivity for inversion. The position-dependent weights of (H3) are irrelevant for the same reason as (H1). The decomposition of (H4) admits two readings: (H4a) symmetric core multiplied by a forward-restricting envelope $\theta(t-t')$, which collapses to retarded V1 with $G_\mathrm{sym}$ as the form factor and is therefore not a distinct candidate; (H4b) symmetric core with a symmetry-preserving envelope, which requires the symmetric core to be primitive-level constructible, refuted by the same non-construction argument as BC3.

**All hybrid variants are REFUTED.** Either by reduction to retarded V1 (H4a) or by non-construction (H1, H2, H3, H4b).

### 6.4 PDE-level cancellation

The canonical PDE structure (§4.4) is direction-neutral. Standard relativistic field theory permits multiple Green's functions of the same wave equation: retarded, advanced, Feynman, symmetric. The PDE itself does not select among them; selection occurs at the level of *boundary conditions* or *kernel-construction prescriptions* outside the PDE proper.

In ED, V1 is the response kernel selected by primitive-level chain dynamics. The PDE provides the equation V1 satisfies; the primitive-level structure provides the construction prescription that selects V1 as retarded among the equation's admissible Green's functions. T-symmetry of the equation does not generate any rescue path for the refuted alternatives; it permits multiple Green's functions but does not pick among them.

**PDE-level cancellation is REFUTED.** The PDE cannot override kernel-construction selection.

### 6.5 Refutation summary

| Candidate | Status | Refutation route |
|---|---|---|
| Retarded V1 | FORCED | Established uniquely by §5 |
| Symmetric V1 (BC3) | REFUTED-by-non-construction | Backward chain contributions structurally forbidden |
| Advanced V1 | REFUTED-by-contradiction | P11 inversion + P13 reversal + P07 vacuous + N1-E conflict |
| (H1) Forward + ε backward | REFUTED-by-non-construction | Magnitude irrelevant; type forbidden |
| (H2) Angular-restricted backward | REFUTED-by-non-construction | Chain propagator has no angular selectivity |
| (H3) Weighted symmetric | REFUTED-by-non-construction | Generalisation of (H1) |
| (H4a) Symmetric core × forward envelope | Equivalent to retarded V1 (not distinct) | Reparameterisation, not alternative |
| (H4b) Symmetric core × symmetry-preserving envelope | REFUTED-by-non-construction | Core non-constructible |
| PDE-level T-symmetry cancellation | REFUTED | Cannot override kernel-construction selection |

**Every non-retarded V1 candidate is closed.** The retarded kernel is uniquely admissible at primitive level.

---

## 7. Cross-Arc Implications

We audit consistency of FORCED retarded V1 with each closed arc and with the continuum-approximation framing.

### 7.1 Arc N

Theorem N1's explicit form-class fixes (Lorentz-scalar, finite-width, sub-power-law-2 decaying, both-ways-bounded by V1-δ and V1-∞ refutations) are properties of the form factor $G(\sigma)$. Retardation is a *support* refinement, orthogonal to the form-class fixes. The retarded V1 takes the form $\theta(t-t') \cdot G(\sigma)$ with $G$ retaining all N1 fixes intact; the $\theta$-factor is the additional sub-feature that B.2 establishes.

The N1-E cascade item is over-determined-forced under retarded V1: the cascade-from-V1 route inherits forward-only kernel structure automatically, and the R1-bypass route forces forward-only N1-E directionality directly through P11+P04 chain bandwidth-update dynamics independently of any V1-cascade dependence. The N2-E (vacuum-modulated commitment memory), N3-D (vacuum-mediated adjacency memory), and V5 (vacuum-induced cross-chain correlations) cascade items inherit the same forward-only refinement consistently.

UV-finiteness is preserved exactly by retarded V1: the multiplicative $\theta$-factor does not affect high-frequency behaviour, and Theorem 7's bound is determined by the form factor $G(\sigma)$.

**Arc N is strengthened.** N1-E is the most direct beneficiary: directionality is now FORCED through two independent paths.

### 7.2 Arc Q

Theorem 17's nine clauses (carrier, group, vertex, worldline, vacuum kernel, three vacuum classes, vacuum strict-non-commit + B-term additivity, unified four-channel quotient, acyclic derivability) operate within rule-type sectors $\tau_g$. Vacuum-coupling clauses (C5–C7) inherit V1 kernel structure; under retarded V1, the rule-type vacuum coupling is forward-only within each sector. The gauge-quotient and minimal-coupling clauses are independent of directionality and remain unchanged.

Theorem Q.5 (vacuum polarisation) establishes loop-form-level admissibility, tree-level $g=2$ preservation, and Fierz $\sigma^{\mu\nu}$ as the only contributor to anomalous magnetic moment. The vacuum-polarisation tensor's analytic structure in continuum QFT (Källén-Lehmann spectral representation, upper-half-plane analyticity, dispersion relations) is the continuum-level reflection of causal structure. Under retarded V1, the analytic structure is supplied at primitive level: the causal-only response is the structural origin of the upper-half-plane analyticity that standard QFT postulates as a causality assumption. Theorem Q.5's closure is therefore strengthened: ED supplies a primitive-level structural foundation for an analytic property that standard QFT treats as an axiomatic input.

Theorem Q.7 (canonical anti-commutation) operates on the operator algebra of the multi-chain field at *spacelike* separations, which lies outside both the forward and backward causal cones. Retarded V1 vanishes at spacelike points, as does symmetric and advanced V1. Q.7 is therefore independent of V1 directionality and consistent automatically.

Theorem Q.8 (effective-vacuum factorisation) supplies the chain-sourcing structure on which the forcing argument of §5 depends. The compatibility is mutual: Q.8 enables Arc B's chain-sourcing structure, and Arc B refines Q.8's vacuum-response kernel as retarded.

**Arc Q is strengthened.** Q.5 in particular gains a primitive-level foundation for structures standard QFT treats as axiomatic inputs.

### 7.3 Arc M

The F-M8 cascade item (τ_g-mediated mass-form contribution channel through the V1 vacuum kernel), promoted to FORCED-unconditional by Theorem 17, refines under retarded V1 to forward-only mediation: a chain's effective mass-form content at proper time $\tau$ receives V1-mediated contributions from prior chain history (chain bandwidth content at $\tau' < \tau$), never from future history. The form-FORCED status of F-M8's contribution channel is preserved; the directionality is refined.

The remaining Arc M cascade items M.1 (massless-slot resolution), M.2 (mass-form additivity), and M.3 (τ_g cross-sector coupling) are unaffected by V1 directionality at their content level: M.1 operates through gauge-quotient and rule-type structure; M.2 operates on form-level additivity; M.3 cross-sector coupling refines to forward-only mediation under retarded V1 but its structural content is preserved.

The M.4 verdict refresh inherits forward-only mediation across the F-M8 channel and refined cross-sector coupling without modification to Arc M's H1-dominant verdict structure.

**Arc M is strengthened.** No backward-propagating mass-form contributions are admissible across any M.x sub-item.

### 7.4 Arc R

Theorem R.2.4 (Cl(3,1) frame uniqueness) fixes Lorentz signature; signature is a metric property, retardation is a time-orientation property. The (3,1) signature distinguishes timelike from spacelike but not forward-timelike from backward-timelike. Retarded V1 lives entirely on the timelike-or-null forward causal cone, fully respecting (3,1) structure.

Theorem R.2.5 (spin-statistics $\eta = (-1)^{2s}$) operates at spacelike separations and is independent of V1 directionality.

Theorem R.3 (Dirac equation emergence) is T-symmetric at the equation level under appropriate antiunitary T-transformation. T-symmetry of the equation does not constrain the kernel directionality; the Dirac equation admits retarded, advanced, Feynman, and symmetric Green's functions as solutions, with primitive-level chain dynamics selecting the retarded one.

The Synge world function $\sigma(x, x')$ is symmetric in its arguments: $\sigma(x, x') = \sigma(x', x)$. This is a metric property of the geodesic structure connecting $x$ and $x'$. Retarded V1's $\theta$-factor is a time-orientation restriction superimposed on the symmetric $\sigma$ structure; the two operate at different layers and do not conflict.

**Arc R is preserved.** All items consistent as direction-neutral substrate or direction-aligned with retarded V1.

### 7.5 Phase-3 lift via Synge $\sigma$ and causal-future restriction

Theorem GR1 (V1 with Synge world function in curved spacetime) extends the V1 vacuum response kernel to curved spacetime via the Hadamard-parametrix construction, yielding $K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}^\mathrm{prim}(\sigma(x, x') / \ell_\mathrm{ED}^2)$. Under FORCED retarded V1 in flat spacetime, the curved-spacetime extension takes the form
$$
K_\mathrm{vac}^\mathrm{curved,\,ret}(x, x') \;=\; \theta_\Sigma(x, x') \cdot G(\sigma(x, x') / \ell_\mathrm{ED}^2),
$$
where $\theta_\Sigma$ is the causal-future restriction defined relative to a Cauchy surface foliation in globally hyperbolic spacetimes. The Hadamard parametrix admits retarded, advanced, and Feynman variants, with the primitive-level chain-contribution argument selecting the retarded variant in curved spacetime exactly as it does in flat spacetime. P11 carry-through preserves the time orientation along curved geodesics: chain worldlines are timelike geodesics in the eikonal limit (GR-3A), and proper-time ordering remains forward-only along each geodesic.

The cascade items inherit forward-only structure consistently in curved spacetime: GR-3A geodesic worldlines preserve P11 time orientation; GR-2D V5 cross-chain correlations propagate forward-only along the cosmological substrate; GR-4D Λ-integral structural channel directionality refines to causal-future support.

**Phase-3 lifts cleanly.** Theorem 18 is preserved under curved-spacetime extension; cosmological-arrow follow-on inherits the foundation.

### 7.6 Continuum-approximation framing — the CR table

The mapping table relating primitive-level kernel objects to continuum-approximation objects:

| Primitive-level | Continuum-approximation | Physical role |
|---|---|---|
| **V1 retarded (response kernel)** | $G_R(x, y)$ retarded Green's function | Causal vacuum response to chain perturbations |
| (No primitive-level analog — distinct object) | $W(x, y)$ Wightman correlator | Unperturbed vacuum two-point function |
| (No primitive-level analog) | $G_F(x, y)$ Feynman propagator | Time-ordered amplitude in perturbative QFT |
| (No primitive-level analog) | $G_A(x, y)$ advanced Green's function | Algebraic tool in scattering theory |

V1 retarded ↔ $G_R$ is the natural correspondence; the standard QFT relation
$$
G_R(x, y) = i\,\theta(t_x - t_y)\,[W(x, y) - W(y, x)]
$$
expresses $G_R$ as a $\theta$-restricted combination of Wightman correlators, exhibiting the same forward-cone-only restriction at continuum level that the chain-contribution argument establishes at primitive level.

The remaining continuum objects retain their standard roles. $W$ measures intrinsic vacuum correlations and is symmetric; $G_F$ is the time-ordered propagator emerging in continuum perturbative-QFT amplitude calculations; $G_A$ is an algebraic tool useful in scattering-theory derivations. None of these is constrained by Arc B's verdict; the verdict applies specifically to V1 (the response kernel).

This framing parallels the UV-FIN primitive-vs-continuum mapping of Arc Q.8 exactly: ED forces a structural property at primitive level that continuum QFT either postulates (the iε prescription, the Kramers-Kronig causality structure) or treats as effective-theory machinery for distinct physical roles. Both layers are internally consistent.

---

## 8. Observable Signatures

The empirical content of Theorem 18 is structural-foundational rather than discriminating-from-standard-physics. ED matches standard QFT and QM causal structure at all currently accessible scales; the primitive-level retardation supplies the structural foundation for that causal structure rather than predicting deviations from it. Discriminating signatures, if any, live at scales near the primitive event-discreteness $\ell_\mathrm{ED}$ — the same regime in which UV-finiteness becomes a directly probable property — and remain experimentally inaccessible at present.

### 8.1 Strict causality of vacuum response near $\ell_\mathrm{ED}$

At scales near $\ell_\mathrm{ED}$, the vacuum response is structurally retarded — strict causality, no anti-causal pre-response, no symmetric tails. At continuum approximation, this matches standard QFT's $G_R$ structure exactly. The discrimination is foundational: ED makes causal structure a primitive-level structural property, whereas standard QFT treats it as a causality postulate or boundary-condition selection. At directly probed scales below $\ell_\mathrm{ED}^{-1}$, the ED prediction matches standard QFT.

### 8.2 Dispersion-relation Kramers-Kronig structure at near-$\ell_\mathrm{ED}$ scales

Combining Theorem 7 (UV-finiteness) with Theorem 18 (retardation), dispersion-relation modifications at near-$\ell_\mathrm{ED}$ scales are constrained to be Kramers-Kronig-causal-only. Any observation of vacuum-response dispersion modifications at extreme-high-frequency or cosmological scales — UHECR timing, GRB photon timing, gravitational-wave dispersion via LIGO/Virgo/KAGRA bounds — must respect Kramers-Kronig causality structurally. Empirically observed acausal dispersion would refute the joint structural verdict; observed consistency confirms the structural prediction.

### 8.3 Cosmological-correlation persistence with strict forward-only structure

The V5 cross-chain correlations at cosmological scales (LSS-correlation persistence empirical-signature route from Phase-3) inherit forward-only structure from FORCED retarded V1. Large-scale-structure correlation functions across cosmological distances should exhibit strict-forward-only causal structure — no detectable backward-correlation tails. This is consistent with standard cosmological causality but provides a primitive-level structural foundation for it.

### 8.4 Primitive-level structural account of measurement-collapse arrow

The quantum-measurement arrow (collapse irreversibility) is encoded at primitive level by P11 commitment-irreversibility. Theorem 18 strengthens this: the measurement arrow propagates to kernel-level retardation as a structural consequence, providing a unified primitive-level account of P11 commitment-irreversibility (chain-level), V1 retardation (kernel-level), and $G_R$ continuum correspondence (continuum-level) under a single structural origin.

### 8.5 Asymmetry in N1-E bandwidth inheritance

Forward-only N1-E bandwidth memory implies that bandwidth-mediated decoherence and similar mass-form effects are strictly forward-only in proper time. This matches the standard structure for quantum-decoherence and collapse models in continuum effective theory; ED supplies a primitive-level structural foundation for it. Decoherence-rate signatures in matter-wave interferometry exhibit no backward-time decoherence tails — a structural prediction matching standard expectation supplied at primitive level.

### 8.6 Why ED matches standard QFT at accessible scales

The CR continuum-approximation framing of §7.6 is the structural reason ED matches standard QFT at all accessible scales. The primitive-level retarded V1 corresponds to the continuum retarded Green's function $G_R$; the symmetric Wightman correlator $W$, the Feynman propagator $G_F$, and the advanced Green's function $G_A$ remain distinct continuum objects with their standard physical roles. The framework lands on standard physics in the appropriate continuum limit rather than predicting empirically refuted deviations. **This is a strength of the result, not a weakness:** it confirms the structural soundness of ED's continuum approximation against an empirically well-established target.

---

## 9. Falsifier Inventory

The Arc B canonical falsifier set comprises six items, established at the scoping stage:

- **BFal-1.** Catalogue exhaustion: have all plausible asymmetry sources been catalogued?
- **BFal-2.** Carry-through soundness: does the P11→V1 carry-through argument require auxiliary inputs?
- **BFal-3.** Relativistic consistency: does primitive-level FORCED retardation contradict continuum-approximation relativistic-QFT consistency?
- **BFal-4.** BC3 / non-retarded alternatives: do the symmetric, advanced, or hybrid kernels admit primitive-level constructions?
- **BFal-5.** Cross-arc consistency: does Arc B's verdict create back-pressure on Phase-2 / N-arc / Phase-3 closures?
- **BFal-6.** Acyclicity: does any substage memo use a downstream conclusion as a derivation input?

The dispatch state at the close of the arc:

| Falsifier | Status | Resolution |
|---|---|---|
| BFal-1 catalogue exhaustion | Dispatched conditional | Conditional on P05/P08/P12 verification. Robust for Theorem 18 itself: the forcing argument routes solely through P11+P02+P04+P13 plus Theorem N1 and Q.8, not through P05/P08/P12. |
| BFal-2 carry-through soundness | Dispatched dark | The P11→V1 carry-through routes through ED-internal structures only; no external assumption imports the arrow. |
| BFal-3 relativistic consistency | Dispatched dark | CR continuum-approximation framing operative. Primitive-level retarded V1 coexists with continuum-approximation $G_R/G_A/G_F/W$ via the response-kernel-vs-correlator distinction. |
| BFal-4 non-retarded alternatives | Dispatched dark | Every non-retarded V1 candidate REFUTED in §6. Symmetric, advanced, hybrid (H1–H4), and PDE-cancellation pathways all closed. |
| BFal-5 cross-arc consistency | Dispatched dark | All cross-arc audits in §7 pass. Arc N strengthened, Arc Q strengthened, Arc M strengthened, Arc R preserved, Phase-3 lifts cleanly. |
| BFal-6 acyclicity | Dispatched dark | All derivation steps use only primitive-level and prior-FORCED-theorem inputs; no downstream content invoked. |

Five of six falsifiers are dispatched dark; BFal-1 remains conditional pending verification of the constitutional content of P05, P08, and P12. The conditional dispatch does not gate Theorem 18: the theorem is robust to the verification outcome since the forcing argument does not invoke any of the verification-flagged primitives.

---

## 10. Theorem 18 — Final Statement

> **Theorem 18 (Primitive-Level Retardation of the V1 Vacuum Response Kernel).**
>
> *Let the Event Density primitive set comprise the items P01 through P13, with Primitive 11 commitment-irreversibility taken as primitively encoded. Let Theorem N1 establish the V1 vacuum response kernel as Lorentz-scalar, finite-width on $\ell_\mathrm{ED}$, decaying with sub-power-law-2 falloff, and bounded both ways by the V1-δ and V1-∞ refutations. Let Theorem Q.8 establish the multi-rule-type effective-vacuum factorisation and the consequent chain-sourcing structure of V1.*
>
> *Then the V1 vacuum response kernel $K_\mathrm{vac}(x, x')$ has, uniquely at primitive level, support restricted to the forward causal cone:*
> $$
> K_\mathrm{vac}(x, x') \neq 0 \;\Longrightarrow\; (x - x') \text{ lies in the forward causal cone}.
> $$
>
> *No symmetric, advanced, or hybrid kernel admits a primitive-level construction: any non-zero backward-cone support would require backward chain contributions $U_K(n, m) \neq 0$ for $n < m$, forbidden by the joint structure of P11 commitment-irreversibility, P02 chain worldline, P04 bandwidth update rule, and P13 proper-time ordering.*
>
> *The microscopic arrow of time is therefore structurally FORCED at the kernel level. The kernel form (retardation) is FORCED; the specific functional form $G(\sigma)$ within the V1 finite-width form-class and the continuum-approximation propagator-boundary-condition specifics are INHERITED.*
>
> *At continuum approximation, the primitive-level retarded V1 corresponds to the standard retarded Green's function $G_R(x, y)$ via the relation*
> $$
> G_R(x, y) = i\,\theta(t_x - t_y)\,[W(x, y) - W(y, x)],
> $$
> *which expresses $G_R$ as a $\theta$-restricted combination of Wightman correlators. The Wightman correlator $W$, the Feynman propagator $G_F$, and the advanced Green's function $G_A$ remain distinct continuum objects unaffected by the primitive-level verdict.*

The theorem advances the FORCED-theorem inventory of the ED program from seventeen to eighteen and supplies the kernel-level / time-orientation structural layer of the framework. The numbering is provisional pending coordination with the residual Arc M cascade (M.1–M.4); this is bookkeeping only and does not affect the structural content of the result.

---

## 11. Discussion

### 11.1 Interpretation of the primitive-level arrow

Theorem 18 establishes the microscopic arrow of time as a structural consequence of the ED primitive ontology rather than as a postulate or boundary-condition choice. The arrow is mono-rooted in Primitive 11 commitment-irreversibility: a single primitive carries the direction-bearing content, and the carry-through to kernel-level retardation proceeds through the chain-contribution construction without any auxiliary direction-bearing input.

The interpretation is that the arrow of time at the kernel level is *what irreversibility looks like* once primitive-level commitment events propagate to vacuum-response structure. The primitive ontology commits to discrete, ordered, non-reversible commitment events along chain worldlines; the response kernel is sourced by these events through chain bandwidth coupling; the kernel inherits the forward orientation that the chain ensemble shares universally. The primitive seed and the kernel-level consequence are the same direction-bearing content viewed at different structural layers.

### 11.2 Relationship to thermodynamic and cosmological arrows

The thermodynamic arrow (entropy increase under low-entropy initial conditions) and the cosmological arrow (alignment with cosmic expansion) are explicitly out of scope for Arc B. Their relationship to the kernel-level arrow is the subject of follow-on work and is not derived in this paper.

A natural conjecture is that thermodynamic and cosmological arrows inherit from the kernel-level arrow through specific structural channels: forward-only V1 plus N1-E bandwidth memory could supply a primitive-level structural argument for entropy production; forward-only V5 cosmological correlations plus Theorem GR1 in expanding spacetime could couple the kernel arrow to cosmological structure formation. These are speculative bridges, not derivations; their structural content remains to be evaluated. The kernel-level arrow is the structural prerequisite — the foundation on which any such bridge would build — but Arc B does not undertake the bridges themselves.

### 11.3 Why the result is foundational rather than phenomenological

Theorem 18 does not predict empirically discriminating deviations from standard QFT or QM causal structure. It supplies the structural foundation for the causal structure that standard physics already exhibits. This is the foundational character of the result: ED articulates a primitive-level account of *why* the kernel-level arrow exists, not a phenomenological prediction of *new* arrow-related effects.

The structural significance is methodological. Standard physics has a multiplicity of arrow accounts — thermodynamic, cosmological, measurement-theoretic, electrodynamical — each securing a particular asymmetry by a particular mechanism. Each mechanism is treated as an external input. Theorem 18 supplies a single primitive-level structural origin for the kernel-level arrow; whether downstream arrows (thermodynamic, cosmological) similarly inherit from this structural origin is the subject of separate arcs.

The result also establishes a structural foundation for analytic-causality properties that standard QFT postulates. The upper-half-plane analyticity of vacuum-polarisation tensors, the Kramers-Kronig dispersion relations, the iε prescription for Feynman propagators — all of these standardly rest on causality assumptions or boundary-condition selections at the field-theory level. Theorem 18 supplies a primitive-level structural origin for each, in the form of the response-kernel retardation that the chain-contribution argument forces.

---

## 12. Conclusion

Arc B closes with the establishment of Theorem 18 (Primitive-Level Retardation of the V1 Vacuum Response Kernel). The microscopic arrow of time is FORCED at the kernel level as a structural consequence of the ED primitive ontology: the V1 response kernel is retarded by uniqueness of construction from forward-only chain bandwidth dynamics, with no admissible symmetric, advanced, or hybrid alternative.

The structural significance is threefold. First, the result advances the FORCED-theorem inventory of the ED program from seventeen to eighteen, completing the kernel-arrow / time-orientation layer alongside the previously-closed memory-kernel layer (Theorem N1), gravitational-kernel layer (Theorem GR1), and gauge sector (Theorem 17). Second, the cross-arc audit confirms strengthening rather than back-pressure: Arc N's N1-E directionality is over-determined-forced through two independent paths; Arc Q.5's vacuum-polarisation analytic structure acquires a primitive-level structural foundation; Arc M's F-M8 mediation refines to forward-only; Phase-3's Theorem GR1 lifts cleanly to a retarded curved-spacetime kernel via Hadamard-parametrix causal-future restriction. Third, the continuum-approximation correspondence — V1 retarded ↔ $G_R$, with $W$, $G_F$, and $G_A$ unaffected as distinct continuum objects — preserves the standard QFT structure at all currently accessible scales while supplying its primitive-level structural foundation.

Three follow-on directions are suggested by Theorem 18. First, the thermodynamic-arrow arc, explicitly out of scope here, would investigate whether forward-only V1 plus N1-E memory supplies a primitive-level structural argument for entropy production. Second, the residual Arc M cascade (M.1 through M.4) is mechanically staged to close in the wake of Theorem 17's promotion of F-M8 to FORCED-unconditional and Theorem 18's refinement of F-M8 mediation to forward-only. Third, the Phase-3 GR-4A question — whether Einstein-equation emergence is forced or remains SPECULATIVE — is unaffected by Theorem 18 in either direction but is the next major structural frontier of the program.

The kernel-level arrow of time, in the framework of Event Density, is not a postulate, not a thermodynamic accident, and not a boundary-condition choice. It is the kernel-level reflection of a primitive-level structural commitment to commitment-event irreversibility, propagated to the response kernel through the chain-contribution structure that Theorem N1 and Theorem Q.8 jointly supply. Forward is forced.

---

## Acknowledgments

This paper is a closure deliverable of the Event Density structural-foundations program. The arc-and-memo derivation discipline that produced Theorem 18 was developed across the prior Arc R, Arc M, Arc Q, Arc N, and Phase-3 closures, and the methodological framing of "form FORCED, value INHERITED" originates in the Arc M and Arc Q closures. The chain-contribution construction at the heart of the forcing argument depends critically on the effective-vacuum factorisation established in Theorem Q.8 and the V1 form-class fixes established in Theorem N1; this paper would not be possible without those prior results.

---

## References

Internal references to the ED program structure. The program operates as a single living framework; all references below are to internal arcs, theorems, primitives, and memos. No external references are required for this paper.

- **ED primitive set P01–P13.** Constitutional content in the `ED-primitives` repository (separate from the main `event-density` derivation repository).
- **Theorem N1 (V1 finite-width vacuum memory kernel FORCED).** Arc N closure. Primary memo: `arcs/arc-N/non_markov_forced.md`. Synthesis: `arcs/arc-N/arc_n_synthesis.md`. Publication paper: `papers/Arc_N/arc_n_paper.{md,tex,pdf}`.
- **Theorem Q.5, Q.7, Q.8 and Theorem 17.** Arc Q closures. Primary memos in `arcs/arc-Q/`. Synthesis: `arcs/arc-Q/19_synthesis_memo_02_theorem_17.md`. Publication paper: `papers/Gauge_Fields_Theorem_17/paper_gauge_fields_theorem_17.{md,tex,pdf}`.
- **Theorem GR1 (V1 with Synge world function FORCED).** Phase-3 closure. Memos in `arcs/Phase-3/`. Synthesis: `arcs/Phase-3/phase3_synthesis.md`.
- **Phase-1 QM-emergence theorems (Theorems 10–16).** Born/Gleason, U2-Discrete, U2-Continuum, U5, U1, U4, U3 closure cycle. Memos across `arcs/born_gleason/`, `arcs/U2/`, `arcs/U2_continuum/`, `arcs/U5/`, `arcs/U1/`, `arcs/U4/`, `arcs/U3/`. Publication papers in the structural-foundations series at `papers/`.
- **Arc R form-level theorems (Theorems 1–4).** Spin-statistics, Cl(3,1) frame uniqueness, anyon prohibition, Dirac equation emergence. Memos in `arcs/arc-R/` (or equivalent path under `quantum/foundations/`). Publication paper: `papers/Arc_R/paper_arc_r.{md,tex,pdf}`.
- **Arc M form-level closure.** Memos in `arcs/arc-M/` (or equivalent). Publication paper: `papers/Arc_M/paper_arc_m.{md,tex,pdf}`.
- **Arc B memo set (this paper's source memos).** `arcs/arc-B/arc_b_scoping.md`, `arcs/arc-B/arrow_catalogue.md`, `arcs/arc-B/arrow_forced.md`, `arcs/arc-B/arrow_refuted.md`, `arcs/arc-B/arrow_implications.md`, `arcs/arc-B/arc_b_synthesis.md`.
- **ED Orientation document.** `docs/ED-Orientation.md`. Living single-file orientation reference; current at the time of writing through the 2026-04-27 Arc B closure entry.

---

**End of Paper — ready for repository inclusion.**
