# The V1 Retarded-Support Vacuum Kernel (Theorem T18) is FORCED

**Paper #19 of the Event Density Forcing Series (Wave 2, Paper 9)**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-13
**Series:** Event Density (ED) Forcing Papers — Paper #19 of the program
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The vacuum response kernel established in Paper #18 (Theorem N1) is forced to have finite width — but the question of *temporal support* remains: does the kernel respond only to past perturbations (retarded support, $\tau \geq 0$), only to future perturbations (advanced support), or symmetrically to both (time-symmetric)? Standard quantum field theory treats vacuum response as fundamentally time-symmetric, with retarded / advanced support emerging only through choice of boundary conditions (initial-value formulations select retarded; final-value formulations select advanced; both are mathematically admissible). This paper shows that, given the substrate conditions $\{C\}$ and Paper #18's V1 finite-width result, **the V1 kernel must have strictly retarded temporal support**, forced by Primitive P11 (commitment-irreversibility) carrying through to chain bandwidth dynamics. The argument has three convergent threads: (i) the advanced kernel is consistency-refuted because P11 forbids backward-only chain contributions; (ii) the symmetric kernel is non-constructible from the chain ensemble — no backward-going chain contributions exist in the substrate inventory to produce the symmetric kernel's negative-time support; (iii) the retarded kernel is uniquely constructible from the substrate's forward-only chain contribution sum, established explicitly via the chain-contribution construction. This is **Theorem T18**: the V1 vacuum-response kernel is retarded, the substrate-level structural source of the kernel-level arrow of time. The Wightman correlator and Feynman propagator remain unaffected as distinct continuum objects via the CR continuum-approximation framing.

---

## 1. Framing

### 1.1 What "retarded support" means for a memory kernel

A vacuum response kernel $K_\mathrm{vac}(x, x')$ describes how a perturbation to the substrate at spacetime point $x'$ produces a response at point $x$. The temporal support of the kernel — the set of $(x, x')$ pairs for which $K_\mathrm{vac}(x, x') \neq 0$ — characterizes the *temporal direction* of the response.

Three structural support classes:

1. **Retarded support**: $K_\mathrm{vac}(x, x') \neq 0$ only for $t > t'$ (future-of-$x'$). The kernel responds only to past perturbations. The standard "retarded Green's function" of classical electrodynamics has this support.

2. **Advanced support**: $K_\mathrm{vac}(x, x') \neq 0$ only for $t < t'$ (past-of-$x'$). The kernel responds only to future perturbations. The advanced Green's function of mathematical physics has this support.

3. **Symmetric (time-symmetric) support**: $K_\mathrm{vac}(x, x') \neq 0$ for both $t > t'$ and $t < t'$. The Wightman two-point function and the Feynman propagator (with appropriate $i\epsilon$ prescription) have this support: they are not strictly retarded or advanced but combine both directions in a specific causal-structured way.

A finite-width kernel from Paper #18 — V1-class — does not by itself fix the temporal support: the V1-class admits retarded, advanced, and symmetric finite-width realizations. Paper #18 forces the kernel to be finite-width but is silent on which support class the V1 kernel realizes.

### 1.2 The puzzle

Standard QFT treats vacuum response as fundamentally time-symmetric. The Wightman two-point function is symmetric under time reflection on its real-time arguments (and the imaginary-time Wick-rotated correlator is manifestly symmetric). The Feynman propagator is symmetric in spacelike-separated configurations and has both retarded and advanced pieces in timelike-separated configurations. The retarded and advanced Green's functions are derived from the Feynman propagator by choosing specific boundary conditions on the field equations.

Under this standard view, the *retardation* observed in physical contexts (radiation reaction, decoherence dynamics, dissipation) arises from initial-value boundary conditions applied to a fundamentally time-symmetric vacuum response. No structural fact of the vacuum *itself* picks retarded over advanced; nature appears to use retarded boundary conditions, but this is an external commitment rather than a structural property of the vacuum.

The deeper question: *why does the vacuum exhibit an intrinsic arrow of time, rather than acquiring one from external boundary conditions?* Several substrate-level frameworks attempt to address this — Wheeler-Feynman absorber theory uses retarded + advanced contributions that conspire to produce effective retardation; thermodynamic arrows are interpreted as low-entropy initial conditions; some cosmological arguments tie the arrow to expansion. None of these derives a kernel-level structural arrow at the substrate level.

A program seeking a substrate-level answer needs:

1. A substrate primitive supplying a direction-of-time at the primitive level.
2. A propagation argument showing this primitive arrow carries through to the kernel-level support structure.
3. An exclusion argument refuting symmetric and advanced kernels as inconsistent with or non-constructible from substrate-level structural content.

### 1.3 What this paper does

The Event Density (ED) framework supplies **Primitive 11 (P11 commitment-irreversibility)** as a direction-bearing substrate primitive: commitment events on a chain are non-reversible and ordered along the chain's proper time in the forward sense. This is the only direction-bearing primitive in the ED inventory; all other primitives are direction-neutral or direction-inheriting from P11.

The present paper forces, given P11 and the V1 finite-width result of Paper #18:

1. **Retarded V1 is consistent** with all substrate primitives and Phase-1/2 theorems. The kernel $K^\mathrm{ret}_\mathrm{vac}(x, x') = \theta(t - t')\,G(\sigma(x, x')/\ell_\mathrm{ED}^2)$ respects Lorentz covariance under $L^\uparrow_+$ (the proper orthochronous Lorentz group, which P11 picks out as the largest covariance group preserved by the primitive substrate), the (3,1) signature, Theorem N1 form-class fixes, and the gauge / Bell / inner-product structures of Papers #1-#17.

2. **Advanced V1 is consistency-refuted**. The kernel $K^\mathrm{adv}_\mathrm{vac}(x, x') = \theta(t' - t)\,G(\sigma/\ell_\mathrm{ED}^2)$ would require backward-only chain contributions, contradicting P11 directly. **REFUTED**.

3. **Symmetric V1 is non-constructible**. The kernel $K^\mathrm{sym}_\mathrm{vac}(x, x') = G(\sigma/\ell_\mathrm{ED}^2)$ would require some backward-going chain contributions to produce the negative-time support. No such backward-going contributions exist in the substrate inventory (P11 forbids them). The symmetric form has no source mechanism in the substrate. **NON-CONSTRUCTIBLE**.

4. **Retarded V1 is uniquely constructible**. The chain-contribution construction (made explicit in §7.4) shows that V1 emerges from a forward-only sum of chain contributions, producing the retarded form uniquely. The kernel-level arrow of time is therefore the substrate-level reflection of P11's commitment-irreversibility carried through the chain ensemble.

The result is **Theorem T18**: V1 retardation FORCED. The kernel-level arrow of time is structurally derived from substrate primitives, not from external boundary conditions.

**Series context.** Paper #18 forced the V1 finite-width class without specifying temporal support. The present paper forces the retarded support, establishing the kernel-level arrow of time. Paper #20 will force the V5 cross-chain correlation kernel (which inherits forward-only structure from V1's retardation). Paper #21 forces the full memory-kernel cascade (N1-E, N2-E, N3-D) inheriting retarded support from V1. Paper #22 derives the Lindblad limit. The V1 retardation result is the substrate-level structural foundation for all downstream kernel-arrow content.

---

## 2. Claim

> **Forcing Theorem (V1 Retarded Support; Theorem T18).** Let any substrate satisfy the conditions $\{C\}$ stated in §5. Then the V1 vacuum response kernel $K_\mathrm{vac}(x, x')$ in flat spacetime is FORCED to have **strictly retarded temporal support**:
> $$
> K_\mathrm{vac}(x, x') = \theta(t - t')\,G(\sigma(x, x')/\ell_\mathrm{ED}^2),
> $$
> with $G$ a Lorentz-scalar function of the Synge world function $\sigma$ on the proper orthochronous Lorentz group $L^\uparrow_+$, $\theta(t - t')$ enforcing forward-light-cone-only support, and the V1 finite-width structure of Paper #18 (Theorem N1) preserved. The kernel-level arrow of time is FORCED. Symmetric V1 (BC3, time-symmetric kernel) is non-constructible from the chain ensemble; advanced V1 is consistency-refuted by P11. The CR continuum-approximation framing preserves the Wightman correlator, Feynman propagator, and advanced Green's function as distinct continuum objects.

---

## 3. Scope

### 3.0 Primitive Inputs (postulated within the ED Generative Primitives System)

This paper takes the following Event Density (ED) substrate primitives as **postulated within the ED Generative Primitives System**:

- **P11 (commitment irreversibility):** the substrate's primitive commitment-irreversibility content. Direct structural source of V1 retarded support.
- **V1 existence as a substrate vacuum-kernel rule-type:** the substrate carries a primitive vacuum response kernel.
- **P07 (channel structure):** supplies the substrate-level categorical domain on which the V1 kernel operates.
- **V1 finite-width structure (Theorem N1, Paper #18):** inherited as upstream result.
- **Lorentz covariance under $L^\uparrow_+$ (proper orthochronous Lorentz group, time-orientation-preserving):** inherited from the substrate's relativistic-scope symmetry content.

The full 13-primitive Generative Primitives System is enumerated in the ED Foundations position paper. The empirical case for the primitives rests on their downstream reach across domains. This paper's contribution: given the primitives above, V1's vacuum response kernel is the unique solution carrying *strictly retarded temporal support* ($K_\mathrm{vac}(x, x') \propto \theta(t - t')$, non-zero only on the forward light cone of $x'$) — Theorem T18. The kernel-level arrow of time is the structural reflection of commitment irreversibility. Symmetric V1 is non-constructible from the chain ensemble; advanced V1 is consistency-refuted by P11.

### 3.1 What is FORCED

- **Retarded temporal support**: $K_\mathrm{vac}(x, x') \propto \theta(t - t')$; non-zero only on the forward light cone of $x'$.
- **Kernel-level arrow of time**: the V1 vacuum kernel itself carries time-orientation, not inherited from external boundary conditions but from substrate-level P11.
- **Compatibility with Primitive 13 (irreversible commitment)**: the retarded structure is the kernel-level reflection of chain commitment-irreversibility.
- **Compatibility with finite width (Paper #18)**: retardation refines the V1 finite-width class but does not contradict it.
- **Compatibility with Lorentz covariance under $L^\uparrow_+$**: the proper orthochronous Lorentz group preserves time-orientation; retarded V1 is $L^\uparrow_+$-covariant.
- **Non-constructibility of symmetric V1 from the chain ensemble**: no backward-going chain contributions exist in the substrate inventory.

### 3.2 What is INHERITED

- **Envelope parameters** of the kernel function $G(\sigma/\ell_\mathrm{ED}^2)$: peak amplitude, decay rate, spectral structure. Inherited from substrate microscopic details (V2 exponential, V3 power-law-above-critical, V4 multi-scale realizations admissible per Paper #18).
- **Numerical value of $\ell_\mathrm{ED}$**: identified with $\ell_P$ via Newton-recovery (Paper #9).
- **Specific decay profile**: the choice of V2/V3/V4 functional form is INHERITED.
- **Strength of the cascade-inherited retardation**: N1-E, N2-E, N3-D, V5 all inherit forward-only structure, with specific amplitudes INHERITED.

### 3.3 What is OUT OF SCOPE

- **Full kernel cascade (Paper #21)**: the downstream FORCED-conditional-on-V1 items (N1-E bandwidth memory, N2-E commitment memory, N3-D adjacency memory) inherit retarded structure from V1, but their full derivation lives in Paper #21.
- **Cross-chain kernels (Paper #20)**: V5 cross-chain correlation kernel inherits forward-only structure from V1 but is the subject of Paper #20.
- **Lindblad limit (Paper #22)**: the Markovian limit of V1 retarded → Lindblad-form open-system dynamics is the content of Paper #22.
- **Curved-spacetime extension**: Theorem T9 / GR1 (Synge world function in curved spacetime) extends V1 to curved backgrounds and is downstream of the present paper (substrate-gravity arc).
- **Wightman two-point function vs. V1**: the substrate-level V1 retarded kernel coexists with the continuum-level Wightman correlator (which is symmetric); the CR continuum-approximation framing addresses this in §7.5 but full QFT continuum-content is downstream.

---

## 4. Key Vocabulary

- **Retarded support**: kernel non-zero only for $t > t'$; forward-light-cone-only.
- **Advanced support**: kernel non-zero only for $t < t'$; backward-light-cone-only.
- **Symmetric (time-symmetric) support**: kernel non-zero for both $t > t'$ and $t < t'$, with appropriate causal-structured prescription.
- **Memory kernel**: substrate-level structural object describing how the vacuum responds to past perturbations.
- **Primitive 11 (P11) — commitment-irreversibility**: substrate primitive specifying that commitment events on a chain are non-reversible. The unique direction-bearing primitive in the ED substrate.
- **Primitive 13 (P13) — proper-time**: substrate primitive specifying that commitment events have finite proper-time intervals; supplies the proper-time parameterization along chain worldlines.
- **Commitment arrow**: the substrate-level forward direction along a chain's proper time, supplied by P11+P13 jointly.
- **Chain worldline $\gamma_K$**: the substrate-level trajectory of a chain through the event manifold, parameterized by proper time $\tau_K$.
- **V1 kernel**: the finite-width vacuum response kernel forced by Paper #18 (Theorem N1).
- **Theorem T18**: the present paper's main result — V1 kernel retardation forced.
- **CR continuum-approximation framing**: the structural framework distinguishing the substrate-level V1 retarded kernel from the continuum-level Wightman correlator; both coexist as distinct objects at different levels of the ED-to-QFT hierarchy.
- **Proper orthochronous Lorentz group $L^\uparrow_+$**: the connected component of the Lorentz group preserving both spatial parity and time orientation; the relevant covariance group for retarded-support kernels.
- **Non-constructibility**: a stronger refutation than violation — a structure is *non-constructible* if no substrate mechanism can produce it, independent of whether it would violate any specific constraint if produced.

---

## 5. Substrate Class $\{C\}$

### C1. Primitive 11 (commitment-irreversibility)

The substrate supplies commitment events on chains as **non-reversible**: once a commitment event occurs on chain $\gamma_K$ at proper-time $\tau_K^{(n)}$, the substrate's content at that locus is set, and cannot be un-set. The forward direction along $\gamma_K$ is established by the ordering of commitment events.

This is the substrate's *unique* direction-bearing primitive. All other primitives are direction-neutral (e.g., P03 spatial homogeneity, P04 bandwidth) or direction-inheriting from P11 (e.g., P13 proper-time, which acquires direction from P11's commitment ordering).

### C2. Primitive 13 (proper-time)

The substrate supplies proper-time $\tau_K$ along each chain worldline $\gamma_K$, with finite proper-time intervals between commitment events. The proper-time parameterization is *oriented* in the forward direction by P11.

### C3. Bandwidth additivity (Primitive P04)

Substrate-level bandwidth on each chain is updated forward-only along the chain's proper time: bandwidth at $\tau_K^{(n)}$ is determined by chain history $\{\tau_K^{(m)} : m \leq n\}$ but not by future content $\{\tau_K^{(m)} : m > n\}$. This is the bandwidth-side carry-through of P11 commitment-irreversibility.

### C4. V1 finite-width kernel (Paper #18 / Theorem N1)

The vacuum response kernel $K_\mathrm{vac}(x, x')$ in flat spacetime lies in the V1 admissible class: finite-width, Lorentz-covariant under $L^\uparrow_+$, UV-FIN-compatible, with substrate-level smoothing at $\ell_\mathrm{ED}$.

### C5. V1 as response kernel (sourced by chain bandwidth content)

The V1 kernel is **a response kernel**, distinct from the unperturbed vacuum two-point function: it describes the linear response of the effective vacuum to chain perturbations. The kernel is *sourced by chain bandwidth content* — chain perturbations propagate to the vacuum response via the kernel.

This sourcing structure is implicit in Arc Q.8 effective-vacuum factorisation: the effective vacuum at any spacetime point is determined by the bandwidth content of all chains in its support. The present paper makes the response-kernel framing explicit (§7.4).

### C6. Inherited results from Papers #1-#18

- **Paper #1**: participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$.
- **Paper #4**: time-translation symmetry from P13 + Schrödinger evolution.
- **Paper #5**: gauge-field structure with vacuum sector (T17 C5).
- **Paper #7**: Lorentz-covariant relativistic structure.
- **Paper #18 (T8/N1)**: V1 finite-width vacuum memory kernel class.

A reader who has not read Papers #1-#18 may take C6 as a definitional premise.

### C7. No kernel-arrow as input

The forcing argument invokes only C1-C6 plus standard mathematical infrastructure (Lorentz-covariance constraints on tempered distributions, theta-function support analysis, chain-contribution algebra). No prior temporal-support property of V1 is assumed.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. Symmetric V1 (BC3, time-symmetric kernel).** $K^\mathrm{sym}_\mathrm{vac}(x, x') = G(\sigma(x, x')/\ell_\mathrm{ED}^2)$ without theta-function. The kernel responds equally to past and future perturbations.

**A2. Advanced V1 (backward-only).** $K^\mathrm{adv}_\mathrm{vac}(x, x') = \theta(t' - t)\,G(\sigma/\ell_\mathrm{ED}^2)$. The kernel responds only to future perturbations.

**A3. Mixed retarded-advanced (Wheeler-Feynman-like).** $K_\mathrm{vac}(x, x') = \tfrac{1}{2}[\theta(t-t') + \theta(t'-t)]\,G(\sigma/\ell_\mathrm{ED}^2)$. Equal weight to retarded and advanced supports.

**A4. Time-reversal-violating kernels with neither pure retarded nor symmetric structure.** Arbitrary functional dependence on $(t - t')$ that breaks time-reversal symmetry but does not have pure $\theta(t - t')$ structure.

**A5. Non-causal (spacelike-supporting) kernels.** Kernels with support outside the forward light cone of $x'$ — i.e., for spacelike-separated $(x, x')$ pairs even at $t > t'$. (The retarded form supports only the forward light cone; pure causal but not strictly $\theta(t - t')$ support is an alternative class.)

**A6. Macroscopic-arrow-derived retardation.** Retardation imposed as a thermodynamic / macroscopic boundary condition rather than a substrate-level kernel property.

**A7. Anti-retarded kernels (acausal in the strict sense).** Kernels with support on spacelike-separated configurations specifically, with no causal-cone restriction.

### 6.2 Mainstream alternatives

**B1. Time-symmetric QFT propagators.** Standard QFT's Wightman two-point function is symmetric on its real-time arguments (up to a sign for fermionic statistics). The Feynman propagator combines retarded and advanced contributions via the $i\epsilon$ prescription. No structural asymmetry between retarded and advanced exists at the level of fundamental fields.

**B2. Markovian approximations.** Zero-memory (δ-function) kernels are formally symmetric. Markovian master equations have retarded structure only via the choice of forward-time evolution operator.

**B3. Stochastic vacuum models.** White-noise or Ornstein-Uhlenbeck vacuum models are time-symmetric in their correlation functions; retardation enters only via initial-condition specification.

**B4. Thermodynamic arrows of time.** The arrow of time is interpreted as arising from low-entropy initial conditions of the universe (Boltzmann brain arguments, the past hypothesis). The vacuum response itself is time-symmetric; retardation is observed because the universe started in a low-entropy state.

**B5. Wheeler-Feynman absorber theory.** Time-symmetric formulation of electrodynamics with equal retarded and advanced contributions that combine via the universe's absorber structure to produce effective retardation. Retardation is an emergent property of the absorber, not a fundamental kernel property.

**B6. Cosmological / expansion-based arrows.** The arrow of time is interpreted as arising from the universe's expansion, providing a natural forward direction. The vacuum response is time-symmetric in a static spacetime; expansion supplies the directionality.

**B7. Boundary-condition-based retardation.** Retardation is a choice of boundary conditions on a time-symmetric vacuum response. Initial-value formulations select retarded; the underlying vacuum has no intrinsic arrow.

---

## 7. Constructive Necessity

The argument establishes V1 retardation in five steps. The key structural move (§7.4) is the chain-contribution construction making explicit V1's response-kernel character.

### 7.1 The three V1-support candidates

We evaluate three structurally distinct candidates for V1 temporal support:

**Retarded V1.** $K^\mathrm{ret}_\mathrm{vac}(x, x') = \theta(t - t')\,G(\sigma(x, x')/\ell_\mathrm{ED}^2)$. Forward-cone-only support.

**Symmetric V1 (BC3).** $K^\mathrm{sym}_\mathrm{vac}(x, x') = G(\sigma(x, x')/\ell_\mathrm{ED}^2)$. Both forward and backward causal-cone support.

**Advanced V1.** $K^\mathrm{adv}_\mathrm{vac}(x, x') = \theta(t' - t)\,G(\sigma(x, x')/\ell_\mathrm{ED}^2)$. Backward-cone-only support.

All three are V1-class (finite-width, Lorentz-scalar on $\sigma$, UV-FIN-compatible) and respect the explicit fixes of Theorem N1. The forcing argument must discriminate.

### 7.2 Advanced V1 — consistency refutation

The advanced kernel $K^\mathrm{adv}_\mathrm{vac}(x, x') = \theta(t' - t)\,G(\sigma/\ell_\mathrm{ED}^2)$ has support only for $t < t'$: it would describe vacuum response at $x$ to *future* perturbations at $x'$.

Under the chain-contribution construction (§7.4), V1 is sourced by chain bandwidth content. Advanced V1 would require *backward-going chain contributions* — chain dynamics propagating from later commitment events to earlier ones, with bandwidth content at $\tau_K^{(m)}$ depending on future content $\{\tau_K^{(n)} : n > m\}$.

This directly contradicts P11 commitment-irreversibility (C1) + the bandwidth-update rule of C3: chain bandwidth dynamics are *forward-only* along proper time. No backward-going chain contributions exist in the substrate inventory.

**Advanced V1 is REFUTED at the consistency stage.** It violates P11 carry-through to chain-level bandwidth dynamics. The substrate cannot produce a kernel with advanced-only support because the underlying chain contributions are forward-only.

### 7.3 Symmetric V1 (BC3) — non-constructibility

The symmetric kernel $K^\mathrm{sym}_\mathrm{vac}(x, x') = G(\sigma/\ell_\mathrm{ED}^2)$ without theta-factor has support on both forward and backward causal cones. To produce this support from the chain-contribution sum, the substrate would require some structure that contributes to the $t < t'$ region — i.e., some mechanism that produces vacuum response at $x$ to perturbations at $x'$ with $t > t'$ (i.e., at $x'$ in the *future* of $x$).

But the chain-contribution sum is *exclusively forward-going*: each chain contribution propagates forward in the chain's proper time, and the chain's commitment-event content at any $\tau_K^{(n)}$ is determined by past content only (C3). There is no substrate mechanism that can produce the backward-direction support of the symmetric kernel.

This is **non-constructibility**, distinct from refutation:

- **Refutation** (Advanced V1): the structure violates an explicit substrate condition (P11). Even if the structure could be assembled in principle, it would be inconsistent with the substrate.
- **Non-constructibility** (Symmetric V1): the structure does not violate an explicit constraint — Symmetric V1 satisfies Lorentz covariance, finite-width, UV-FIN, and all other N1 form-class fixes. But the substrate has no mechanism to construct it: no backward-going chain contributions exist in the chain-contribution inventory.

The symmetric kernel is **non-constructible** from the chain ensemble. It is a logically coherent structural object, but the ED substrate provides no construction recipe.

**Why non-constructibility matters**: a structurally coherent object that the substrate cannot construct is *de facto* excluded. The substrate's structural content sets the admissibility class; objects outside the constructibility envelope are not realized.

### 7.4 The chain-contribution construction (load-bearing step)

The load-bearing step of the forcing argument is the explicit chain-contribution construction making clear that V1 is a *response kernel* sourced by chain bandwidth content with forward-only construction.

**Setup**. V1 is defined as the linear response of the effective vacuum at $x$ to a chain perturbation at $x'$. By construction, V1 is a **response kernel** — distinct from the unperturbed vacuum two-point function $W(x, x') = \langle 0 | \hat{\phi}(x) \hat{\phi}(x') | 0 \rangle$, which is a different object measuring intrinsic vacuum correlations.

A response kernel is sourced by perturbations. The source for V1 is **chain bandwidth content**: chain perturbations $\delta P_\mathrm{chain}(x')$ are bandwidth-coupled to the effective vacuum at the chain's commitment events, and the kernel $K_\mathrm{vac}$ propagates the perturbation across the substrate.

This sourcing structure is implicit in Arc Q.8 effective-vacuum factorisation: the effective vacuum at any spacetime point is determined by the bandwidth content of all chains in its support. The present argument makes this explicit.

**The chain-contribution sum**. Let $\{\gamma_K\}_{K=1}^N$ index the chains in the support of $V_\mathrm{vac}(x)$. Each chain $\gamma_K$ is a worldline parameterised by its proper time $\tau_K$; commitment events along $\gamma_K$ occur at indices $n = 1, 2, \ldots$ with proper-time values $\tau_K^{(n)}$.

A chain perturbation $\delta b_K(\tau_K^{(m)})$ at commitment index $m$ on chain $K$ produces a perturbation in the chain's bandwidth content at later commitment events $n \geq m$ via the chain's *forward* bandwidth-update rule:
$$
\delta b_K(\tau_K^{(n)}) = \sum_{m \leq n} U_K(n, m)\,\delta b_K^\mathrm{source}(\tau_K^{(m)}),
$$
where $U_K(n, m)$ is the chain's forward propagator. **By P11 irreversibility (C1) + the bandwidth-update rule (C3), $U_K(n, m) = 0$ for $n < m$**: the propagator vanishes for backward propagation. This is the substrate-level fact: chain bandwidth dynamics are forward-only.

The chain's contribution to the effective vacuum at spacetime point $x$ is given by the bandwidth content at the commitment event nearest $x$ (or, more generally, by the integrated bandwidth-coupling at all commitment events whose vacuum-coupling support reaches $x$). Schematically:
$$
\delta V_\mathrm{vac}^{(K)}(x) = \sum_n \mathcal{F}_K(x; \tau_K^{(n)})\,\delta b_K(\tau_K^{(n)}),
$$
where $\mathcal{F}_K(x; \tau_K^{(n)})$ is the substrate-level coupling function from chain commitment event $\tau_K^{(n)}$ to vacuum point $x$.

**Constructing V1**. Summing over all chains and all commitment events:
$$
\delta V_\mathrm{vac}(x) = \sum_K \sum_n \mathcal{F}_K(x; \tau_K^{(n)})\,\delta b_K(\tau_K^{(n)}) = \int d^4x'\,K_\mathrm{vac}(x, x')\,\delta P_\mathrm{chain}(x'),
$$
where the V1 kernel $K_\mathrm{vac}(x, x')$ is the substrate-level structural function emerging from the chain-contribution sum.

**Why the sum produces retarded support**. Each chain perturbation $\delta b_K^\mathrm{source}(\tau_K^{(m)})$ enters the sum at $\tau_K^{(m)}$ and propagates forward in proper time via $U_K(n, m)$ with $n \geq m$. The bandwidth content at chain commitment event $\tau_K^{(n)}$ depends only on past chain history. When mapped to spacetime coordinates $x = (t, \mathbf{x})$, the commitment-event proper-time $\tau_K^{(n)}$ corresponds to a specific time $t_n$ on chain $\gamma_K$'s worldline. The vacuum coupling $\mathcal{F}_K(x; \tau_K^{(n)})$ reaches spacetime point $x$ only if $x$ is in the *future* light cone of the chain's commitment event at $\tau_K^{(n)}$ — i.e., $t > t_n$.

Therefore the chain perturbation $\delta b_K^\mathrm{source}(\tau_K^{(m)})$ contributes to $\delta V_\mathrm{vac}(x)$ only for $t > t_m$ (the time of the chain's source commitment event). In terms of the V1 kernel: the perturbation at $x'$ (with chain commitment at $t' = t_m$) contributes to $\delta V_\mathrm{vac}(x)$ only for $t > t'$. **The kernel has retarded support**: $K_\mathrm{vac}(x, x') \neq 0$ only for $t > t'$.

This is the chain-contribution construction's load-bearing result: **V1 emerges from a forward-only chain contribution sum, producing the retarded form $K^\mathrm{ret}_\mathrm{vac}(x, x') = \theta(t - t')\,G(\sigma/\ell_\mathrm{ED}^2)$ uniquely**.

### 7.5 The CR continuum-approximation framing

A potential objection: standard QFT's Wightman correlator $W(x, x') = \langle 0 | \hat\phi(x)\hat\phi(x') | 0\rangle$ is time-symmetric on its real-time arguments. The Feynman propagator $G_F(x, x')$ combines retarded and advanced contributions. If V1 is forced to be retarded, are these continuum objects also retarded? Are they inconsistent with substrate-level retardation?

**Resolution via CR continuum-approximation framing.** The substrate-level V1 retarded kernel and the continuum-level Wightman / Feynman / advanced Green's functions are **distinct objects at different levels of the ED-to-QFT hierarchy**:

- **V1 (substrate level)**: response kernel sourced by chain bandwidth content. Forward-only structure forced by P11. The substrate-level structural object.
- **Wightman correlator (continuum level)**: intrinsic vacuum two-point function, not sourced by perturbations. Measures unperturbed vacuum correlations. Time-symmetric in its real-time arguments.
- **Feynman propagator (continuum level)**: time-ordered vacuum correlator with $i\epsilon$ prescription. Combines retarded and advanced contributions in spacetime-dependent ways.
- **Retarded Green's function $G_R$ (continuum level)**: causal response function with $\theta(t - t')$ support. The continuum-level analog of V1.
- **Advanced Green's function $G_A$ (continuum level)**: anti-causal response function with $\theta(t' - t)$ support. A distinct continuum object that has no substrate-level analog.

The CR continuum-approximation framing: under DCGT-style coarse-graining (Paper #8), the substrate-level V1 retarded kernel produces the continuum-level retarded Green's function $G_R$. The Wightman correlator, Feynman propagator, and advanced Green's function are *different continuum objects* with different physical content:

- $G_R$ is a *response* function — directly inherited from V1.
- $W$ is a *correlation* function — measures unperturbed vacuum structure, distinct from response.
- $G_F$ is a *time-ordered* function — used in perturbative scattering calculations.
- $G_A$ is the anti-causal response — has no substrate-level analog but exists as a continuum mathematical object.

The substrate-level retardation of V1 does *not* force the continuum-level Wightman or Feynman propagators to be retarded. These are distinct continuum-level objects that coexist with V1 retarded at different levels of the hierarchy.

This framing parallels the substrate-level UV-FIN (Paper #18) vs. continuum-level regularized two-point functions: the substrate is UV-finite, but continuum-level objects may have UV-divergent forms that are regularized via various continuum techniques. The substrate-level structural property and the continuum-level mathematical object are different.

**The composite result**: V1 retarded support is the substrate-level structural fact. Continuum-level objects with different temporal-support structures coexist consistently at the continuum level via the CR continuum-approximation framing.

---

## 8. Exclusion Arguments

### 8.1 A1 — Symmetric V1 (BC3)

Excluded by non-constructibility (§7.3). Symmetric V1 would require backward-going chain contributions to produce the negative-time support; no such contributions exist in the chain ensemble. The substrate has no construction recipe for the symmetric kernel.

While the symmetric kernel does not violate any explicit substrate constraint (C1 Lorentz covariance, C3 UV-FIN, C4 V1 finite-width are all satisfied formally), it cannot be assembled from substrate-level structural content. **Non-constructible**.

### 8.2 A2 — Advanced V1

Excluded by consistency refutation (§7.2). Advanced V1 would require backward-only chain contributions, contradicting P11 commitment-irreversibility (C1). The bandwidth-update rule (C3) explicitly forbids future-to-past propagation. **REFUTED**.

### 8.3 A3 — Mixed retarded-advanced (Wheeler-Feynman-like)

A mixed kernel $K_\mathrm{vac}(x, x') = \tfrac{1}{2}[\theta(t-t') + \theta(t'-t)]\,G$ would require *partial* backward-going chain contributions to produce the advanced piece. By the same argument as A2, the backward piece is REFUTED by P11.

Wheeler-Feynman absorber theory addresses this in the continuum limit via the universe's absorber structure: the advanced piece is supposedly "absorbed" and effectively cancels, producing pure retardation. At the substrate level, no analog of the universe's absorber exists; the advanced piece cannot be constructed and there is nothing to absorb. **REFUTED**.

### 8.4 A4 — Time-reversal-violating but non-pure-theta kernels

Arbitrary functional dependence on $(t - t')$ that breaks time-reversal symmetry without pure $\theta(t - t')$ structure — e.g., $K_\mathrm{vac}(x, x') \propto e^{-\alpha(t-t')} G(\sigma/\ell_\mathrm{ED}^2)$ for some $\alpha > 0$ without the theta-function — would have *some* support at $t < t'$ (though exponentially suppressed). This still requires backward-going chain contributions, REFUTED by P11.

Conversely, a kernel with pure $\theta(t-t')$ structure plus exponential decay $\theta(t-t')\,e^{-\alpha(t-t')}\,G$ is a *retarded V1 with V2 (exponential) decay*, fully consistent with §7.4.

### 8.5 A5 — Non-causal (spacelike-supporting) kernels

Retarded V1 has support on $t > t'$ but is *not* restricted to the forward light cone in the strict sense — spacelike-separated configurations with $t > t'$ are supported. The kernel $K^\mathrm{ret}_\mathrm{vac}(x, x') = \theta(t - t')\,G(\sigma/\ell_\mathrm{ED}^2)$ has support on the entire $t > t'$ half-space of spacetime, modulo the decay structure of $G(\sigma/\ell_\mathrm{ED}^2)$.

For matter-field-mediated communication, locality / causality requires support on the forward light cone only (not on spacelike-separated configurations). At the substrate level, V1 *can* have spacelike support because chain bandwidth coupling reaches across spacelike-separated regions instantaneously at the substrate level (constrained by primitive-discreteness ℓ_ED but not by light-cone causality at the primitive level).

This is consistent with the substrate-level structural content (P11 forces forward-only-in-time, not strict-causal); the continuum-level causal structure emerges at the DCGT-coarse-graining level.

**A5 is structurally compatible with retarded V1** at the substrate level; it is not an alternative excluded by the substrate. The light-cone restriction is a continuum-level approximation, not a substrate-level commitment.

### 8.6 A6 — Macroscopic-arrow-derived retardation

Retardation imposed externally — e.g., as a thermodynamic / cosmological boundary condition on a time-symmetric vacuum — would be downstream of the substrate. Under the substrate-conditions test, the substrate *forces* retardation at the kernel level (§7.4); the substrate does not need an external boundary condition. The macroscopic-arrow framework provides one possible *explanation* of why the substrate-level retardation manifests at macroscopic scales, but it cannot replace the substrate-level forcing.

### 8.7 A7 — Anti-retarded (acausal) kernels

Anti-retarded kernels with support only on spacelike-separated configurations would describe vacuum response across spacelike intervals — possibly with no temporal-direction restriction. At the substrate level, P11 still forbids backward-going contributions; only the forward-future-in-substrate-proper-time portion of spacelike configurations could be supported. **REFUTED** by P11 if the kernel has backward-time components; partially admissible only as the spacelike sub-case of retarded V1 (A5).

### 8.8 B1 — Time-symmetric QFT propagators

Time-symmetric Wightman correlators and Feynman propagators are *continuum-level objects*, not substrate-level V1 kernels. Under the CR continuum-approximation framing (§7.5), these coexist with substrate-level V1 retarded as distinct objects. The Wightman correlator is a *correlation* function (not a response function); the Feynman propagator is a *time-ordered* function used for perturbative scattering.

The substrate-level V1 retarded corresponds at the continuum level to the retarded Green's function $G_R$, not the Wightman correlator $W$ or the Feynman propagator $G_F$. These continuum objects have different physical content and different temporal-support properties.

### 8.9 B2 — Markovian approximations

Markovian (δ-function) kernels are excluded by Paper #18 (Theorem N1): δ-width is refuted by UV-FIN. The retardation question is downstream of finite-width forcing; the substrate-level vacuum kernel is finite-width *and* retarded.

### 8.10 B3 — Stochastic vacuum models

Stochastic vacuum models with time-symmetric correlation functions can be reformulated as V1 retarded with appropriate boundary conditions on the stochastic process. The forcing of retardation at the substrate level corresponds to the choice of forward-time evolution in the stochastic-process formulation. Under the substrate-conditions test, the stochastic models are downstream operational formulations; the substrate-level retardation is upstream.

### 8.11 B4 — Thermodynamic arrows of time

The thermodynamic arrow framework attributes the arrow of time to low-entropy initial conditions of the universe rather than to fundamental physics. Under the substrate-conditions test, this is *consistent* with the substrate-level retardation but not in competition: the substrate-level P11 commitment-irreversibility is the kernel-level arrow, and this carries through to macroscopic statistical-mechanical arrows under coarse-graining.

The thermodynamic framework is *downstream* of the substrate-level retardation. Both can be true; the substrate-level fact is upstream.

### 8.12 B5 — Wheeler-Feynman absorber theory

Wheeler-Feynman uses time-symmetric retarded + advanced contributions that combine via the universe's absorber structure to produce effective retardation. Under the substrate-conditions test, the advanced contribution is REFUTED by P11 (§7.2): the substrate cannot construct the advanced piece. Wheeler-Feynman's premise — that retarded and advanced contributions both exist at the fundamental level — is incompatible with the substrate-level forcing.

### 8.13 B6 — Cosmological / expansion-based arrows

The cosmological-expansion-based arrow framework attributes the arrow of time to the expansion of the universe, providing a natural forward direction. Under the substrate-conditions test, the substrate-level P11 is more upstream than cosmological expansion: P11 acts at every commitment event on every chain, not only at the cosmological scale. The cosmological arrow may *correlate* with the substrate-level arrow but is not the source of it.

### 8.14 B7 — Boundary-condition-based retardation

Retardation as a boundary-condition choice on time-symmetric vacuum response is *not* an alternative to substrate-level retardation; it is a continuum-level *consequence* of the substrate-level retardation. The continuum field equations are time-symmetric, but the response kernel that propagates substrate-level chain content is retarded by substrate forcing. Initial-value formulations select the retarded Green's function because that is the kernel actually present at the substrate level.

### 8.15 Summary of exclusions

| Alternative | Status | Reason |
|---|---|---|
| A1 Symmetric V1 (BC3) | NON-CONSTRUCTIBLE | No backward-going chain contributions exist in substrate. |
| A2 Advanced V1 | REFUTED | Violates P11 commitment-irreversibility directly. |
| A3 Mixed retarded-advanced | REFUTED | Advanced piece refuted by P11; substrate has no absorber analog. |
| A4 Time-reversal-violating non-theta | REFUTED | Any backward-time support requires backward chain contributions. |
| A5 Non-causal spacelike-supporting | compatible | Spacelike forward-time support admissible at substrate; light-cone causality is continuum-emergent. |
| A6 Macroscopic-arrow-derived | downstream | External boundary condition unnecessary; substrate forces retardation directly. |
| A7 Anti-retarded acausal | REFUTED | Backward-time component violates P11. |
| B1 time-symmetric QFT propagators | not in space | Continuum-level objects, distinct from V1; CR framing preserves both. |
| B2 Markovian approximations | excluded by Paper #18 | δ-width refuted by UV-FIN. |
| B3 stochastic vacuum models | downstream | Stochastic-process formulations downstream of substrate retardation. |
| B4 thermodynamic arrows | downstream | Macroscopic consequence of substrate-level P11 carry-through. |
| B5 Wheeler-Feynman absorber | REFUTED | Advanced contribution non-constructible at substrate. |
| B6 cosmological arrows | downstream | Substrate-level P11 more upstream than cosmological expansion. |
| B7 boundary-condition retardation | downstream | Substrate-level retardation is the upstream fact; boundary conditions reflect it. |

**Retarded V1 (Theorem T18) is the unique substrate-derived temporal-support structure for the vacuum response kernel.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier is sharp:

**Any reproducible observation of advanced vacuum response** at the substrate level (i.e., vacuum content responding to future perturbations, not handled by continuum-level Wightman/Feynman structures) would falsify the substrate-level forcing.

Specific contexts:

- **Casimir-effect dynamical measurements**: time-resolved measurements of Casimir-force response should show retarded kernel structure with finite memory. Observed dynamics are consistent with retarded response; no advanced contributions detected.
- **Vacuum-polarization time-resolved measurements**: in QED vacuum-polarization experiments (e.g., precision electron magnetic-moment measurements interpreted dynamically), the response is consistent with retarded kernels.
- **Radiation reaction**: the Abraham-Lorentz force on accelerating charges shows retarded behavior; advanced contributions would produce pre-acceleration (acceleration before the force is applied), which is not observed empirically.
- **Decoherence dynamics**: open-quantum-system experiments show retarded decoherence — environments couple to systems forward in time, never backward. The Born-Markov approximation and its non-Markovian generalizations are consistent with retarded substrate-level structure.

If any of these were experimentally violated — if reproducible advanced vacuum response or pre-acceleration were observed — the substrate-level forcing would be refuted along with standard observed temporal causality.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C7 (P11 commitment-irreversibility, P13 proper-time, bandwidth additivity, V1 finite-width from Paper #18, V1 as response kernel sourced by chain bandwidth content, Papers #1-#18 inherited, no kernel-arrow as input) but in which the V1 kernel admits non-retarded support — symmetric, advanced, or mixed — that survives the exclusion arguments of §8.

The author's claim is that no such substrate exists. Each alternative is dispatched by a specific substrate-condition violation or non-constructibility argument. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

V1 retardation is the kernel-level arrow of time at the substrate level. Downstream consequences:

**Paper #20 (V5 cross-chain correlation kernel).** V5 inherits forward-only structure from V1 retardation; cross-chain correlations propagate forward in time.

**Paper #21 (memory-kernel cascade).** N1-E (vacuum-induced bandwidth memory), N2-E (vacuum-modulated commitment memory), N3-D (vacuum-mediated adjacency memory) all inherit retarded support from V1.

**Paper #22 (Lindblad limit).** Lindblad-form open-system dynamics is the Markovian limit of retarded V1 (in the small-memory-time approximation). The substrate-level Lindblad-form follows from V1 retardation.

**Paper #10 (Black holes + Hawking via V5-KMS).** The substrate-level KMS condition on V5 imaginary-time correlations (Paper #10 §7.5) uses V1-class retarded structure. Without V1 retardation, the KMS-based Hawking-temperature derivation would lack its structural foundation.

**Macroscopic thermodynamic arrows.** Carry-through from substrate-level P11 + V1 retardation to macroscopic statistical-mechanical arrows of time via DCGT coarse-graining (Paper #8). The H-theorem and the second law of thermodynamics emerge at the macroscopic level from the substrate-level kernel-arrow.

**Causal-structure preservation in DCGT continuum limit.** Light-cone causality at the continuum level is the DCGT-coarse-grained signature of V1 retardation at the substrate level.

The V1 retardation result is structurally upstream of essentially all temporal-direction phenomena in physics.

---

## Appendix A — Derivation Chain and Glossary

### A.1 The chain-contribution sum producing retarded V1

The substrate-level chain contribution sum:
$$
\delta V_\mathrm{vac}(x) = \sum_K \sum_n \mathcal{F}_K(x; \tau_K^{(n)})\,\delta b_K(\tau_K^{(n)}),
$$
where:
- $K$ indexes chains.
- $n$ indexes commitment events on chain $K$.
- $\tau_K^{(n)}$ is the proper-time of the $n$-th commitment event on chain $K$.
- $\delta b_K(\tau_K^{(n)})$ is the bandwidth perturbation at that commitment event.
- $\mathcal{F}_K(x; \tau_K^{(n)})$ is the coupling function from the chain's commitment event to vacuum point $x$.

The bandwidth perturbation propagates forward in proper time:
$$
\delta b_K(\tau_K^{(n)}) = \sum_{m \leq n} U_K(n, m)\,\delta b_K^\mathrm{source}(\tau_K^{(m)}),
$$
with $U_K(n, m) = 0$ for $n < m$ (forward-only propagation by P11 + C3).

The coupling function $\mathcal{F}_K(x; \tau_K^{(n)})$ has support only for $t > t_n$ (where $t_n$ is the spacetime time of the chain's $n$-th commitment event), because the vacuum response at $x$ can only be reached by the substrate's structural mechanism after the chain commitment occurs.

Combining: $\delta V_\mathrm{vac}(x) = \int d^4x'\,K_\mathrm{vac}(x, x')\,\delta P_\mathrm{chain}(x')$ with $K_\mathrm{vac}(x, x') \neq 0$ only for $t > t'$. The retarded form $K^\mathrm{ret}_\mathrm{vac}(x, x') = \theta(t - t')\,G(\sigma/\ell_\mathrm{ED}^2)$ is uniquely produced.

### A.2 Non-constructibility of the symmetric kernel

The symmetric kernel would require the chain-contribution sum to include backward-going contributions, with $U_K(n, m) \neq 0$ for $n < m$ — chain bandwidth at $\tau_K^{(n)}$ depending on future content $\tau_K^{(m)}$ for $m > n$.

This contradicts the substrate-level bandwidth-update rule (C3) derived from P11: bandwidth at $\tau_K^{(n)}$ is determined by past content only. The substrate has no mechanism to construct $U_K(n, m) \neq 0$ for $n < m$.

Therefore the symmetric kernel cannot be assembled from chain contributions, regardless of whether it would violate any other explicit constraint. The substrate's structural inventory does not contain the construction recipe. **Non-constructibility**.

### A.3 The advanced kernel's direct refutation

The advanced kernel requires the chain-contribution sum to consist *entirely* of backward-going contributions, with $U_K(n, m) = 0$ for $n \geq m$ but non-zero for $n < m$. This is the direct inversion of the bandwidth-update rule and directly contradicts P11 commitment-irreversibility. The advanced kernel is **REFUTED at the consistency stage**, prior to any constructibility analysis.

### A.4 Glossary

- **Advanced support**: $K_\mathrm{vac}(x, x') \propto \theta(t' - t)$; backward-light-cone-only.
- **Bandwidth-update rule**: substrate-level rule (P11 + C3) specifying that chain bandwidth at $\tau_K^{(n)}$ is determined by past content only.
- **Chain-contribution sum**: substrate-level construction of V1 as a sum of chain perturbation contributions.
- **Commitment-event index $n$**: ordering index of commitment events on a chain $\gamma_K$ along its proper time.
- **CR continuum-approximation framing**: structural framework distinguishing substrate-level V1 retarded from continuum-level Wightman / Feynman / advanced Green's functions.
- **FORCED**: derived from substrate primitives + standard mathematics with no additional commitments.
- **INHERITED**: quantitative content (envelope parameters, decay profile, $\ell_P$ value) used but not derived in this paper.
- **Kernel-level arrow of time**: substrate-level forward-time direction encoded in the V1 kernel's retarded support.
- **Non-constructibility**: stronger refutation than violation — a structure has no construction recipe in the substrate inventory.
- **P11 (commitment-irreversibility)**: substrate primitive specifying non-reversibility of commitment events. The unique direction-bearing primitive.
- **P13 (proper-time)**: substrate primitive specifying finite proper-time intervals between commitment events.
- **Proper orthochronous Lorentz group $L^\uparrow_+$**: connected component of the Lorentz group preserving spatial parity and time orientation.
- **Response kernel**: substrate-level kernel describing linear response to perturbations, distinct from intrinsic correlation function.
- **Retarded support**: $K_\mathrm{vac}(x, x') \propto \theta(t - t')$; forward-light-cone-only.
- **Substrate**: pre-quantum primitive layer of ED.
- **Symmetric support**: kernel non-zero on both forward and backward causal cones.
- **Theorem T18**: V1 kernel retardation FORCED; the main result of this paper.
- **V1 kernel**: finite-width vacuum response kernel forced by Paper #18 (Theorem N1).

### A.5 Source-repository citations (for ED-internal readers)

- `arcs/arc-B/arrow_forced.md` — Stage B.2 FORCED evaluation memo establishing V1 retardation as FORCED via P11 carry-through + chain-contribution construction.
- `arcs/arc-B/arrow_refuted.md` — Stage B.3 REFUTED evaluation memo establishing advanced V1 as consistency-refuted and symmetric V1 as non-constructible.
- `arcs/arc-B/arc_b_synthesis.md` — Arc B synthesis with Theorem T18 as the headline result.
- `arcs/arc-B/arrow_catalogue.md` — full catalogue of arrow-of-time candidates.
- `arcs/arc-B/arrow_implications.md` — cross-arc implications (Stage B.5) of V1 retardation.
- `theorems/T18.md` — theorem-level index entry: T18 FORCED-unconditional.
- `papers/Time_Arrow_Theorem_18/paper_time_arrow_theorem_18.md` — predecessor publication.

These are *not* required reading for the present paper.

---

*End of Paper #19.*
