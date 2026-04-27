# REFUTED Evaluation: Closing All Alternatives to Retarded V1

**Arc B Stage B.3 — REFUTED Evaluation Memo**
**Status:** Evaluation memo. **Headline verdict: every non-retarded V1 candidate is REFUTED at primitive level.** Specifically: the symmetric kernel BC3 is REFUTED-by-non-construction (no chain-contribution sum produces it); the advanced kernel is REFUTED-by-contradiction-with-P11 (backward chain dynamics structurally forbidden); all hybrid variants (H1 forward-dominant + backward-nonzero, H2 angular-restricted backward, H3 weighted-symmetric, H4 symmetric-core + directional-envelope) are REFUTED by the same chain-contribution argument; PDE-level T-symmetry does not rescue any non-retarded candidate (PDE is form-substrate, not direction-source). Cross-arc consistency confirmed: Arc N, Arc Q (T17), Arc M (F-M8 cascade), UV-FIN, and Lorentz covariance are all preserved by FORCED retarded V1; the retarded-Green's-function ↔ continuum-approximation correspondence operates correctly; the symmetric Wightman correlator is a distinct object and is unaffected by the V1 verdict. **Falsifier dispatch: BFal-1 dispatched (conditional on P05/P08/P12 neutrality), BFal-2/3/4 dispatched dark, BFal-5 pending B.4, BFal-6 dispatched dark. Theorem 18 is structurally locked subject to B.4 cross-arc audit and B.5 final synthesis.** A note on falsifier numbering: the canonical Arc B falsifier set was established in B.0 §4.3 (BFal-1 catalogue exhaustion / BFal-2 carry-through soundness / BFal-3 relativistic consistency / BFal-4 BC3 alternative / BFal-5 cross-arc consistency / BFal-6 acyclicity). The B.3 prompt described the falsifiers in terms of the *content tests dispatched at B.3* (symmetric viability, advanced viability, hybrid viability, PDE-cancellation, etc.); these are sub-cases within the canonical numbering. §7 addresses both numberings with explicit mapping to avoid drift.

---

## 1. Recap of B.1.2 FORCED result

The forcing chain established in B.2 §3.4 (chain-contribution construction):

(F-i) **V1 is a response kernel** — the linear response of the effective vacuum at $x$ to a chain perturbation at $x'$. Distinct from the unperturbed Wightman correlator $W(x, x') = \langle 0 | \hat{\phi}(x) \hat{\phi}(x') | 0 \rangle$. Established by Theorem N1 (existence + form-class) + Arc Q.8 effective-vacuum factorisation (sourcing structure).

(F-ii) **Response kernels require sourced contributions.** A response kernel acts on perturbations propagated through the substrate. The source for V1 is chain bandwidth content via the bandwidth-coupling channel of Q.8 effective-vacuum factorisation. There is no non-chain-sourced contribution to V1 *as a response kernel* (non-chain-sourced contributions live in the unperturbed correlator $W$, which is a distinct object).

(F-iii) **Chain bandwidth dynamics are forward-only along proper time.** P11 commitment-irreversibility supplies the temporal direction; P02 + P13 supply the worldline parameterisation; P04 supplies the bandwidth update rule. Jointly: the chain forward-propagator $U_K(n, m) = 0$ for $n < m$. Bandwidth at $\tau_K^{(n)}$ depends on chain history $\{\tau_K^{(m)} : m \leq n\}$ but never on future $\{\tau_K^{(m)} : m > n\}$.

(F-iv) **Forward-only chain dynamics → forward-cone-only V1 support.** The chain-contribution sum (B.2 §3.4.3) admits non-zero contributions to $K_\mathrm{vac}(x, x')$ only when $(x - x')$ lies in the forward causal cone (along every chain's universal P11 time orientation, which is shared across the chain ensemble).

(F-v) **Symmetric and advanced kernels require backward chain dynamics.** Any non-zero kernel support outside the forward causal cone — backward cone for advanced, both cones for symmetric — requires backward chain propagator $U_K(n, m) \neq 0$ for $n < m$.

(F-vi) **Backward chain dynamics violate P11.** P11 commitment-irreversibility is constitutional and direction-bearing primitively. There is no admissible backward chain dynamics in the inventory.

**Conclusion (provisional, B.2):** V1 retardation is FORCED. **Conclusion (after B.3, this memo):** all non-retarded alternatives are REFUTED, locking the FORCED-uniqueness verdict.

---

## 2. REFUTED evaluation of the symmetric kernel (BC3)

### 2.1 Definition of the symmetric candidate

**BC3 (symmetric-finite-support kernel):** $K_\mathrm{vac}^\mathrm{sym}(x, x') = G(\sigma(x, x') / \ell_\mathrm{ED}^2)$, with $G$ a Lorentz-scalar function of Synge's world function $\sigma$, finite-width on $\ell_\mathrm{ED}$, decaying with sub-power-law-2 falloff. Equal-weight support on both forward and backward causal cones — equivalently, time-reversal-invariant kernel.

BC3 satisfies all *explicit* Theorem N1 form-class fixes (per `non_markov_forced.md` §2): Lorentz-scalar, finite-width, decaying, both-ways-bounded. It satisfies all four constraints C1+C2+C3+CR in isolation (B.2 §4.5). The question is whether it admits a primitive-level construction.

### 2.2 Required backward chain contributions

For the symmetric kernel, the chain-contribution sum (B.2 §3.4.2) must produce non-zero terms with $\tau_K^{(n)} < \tau_K^{(m)}$ — i.e., terms in which a perturbation at chain index $m$ propagates to chain index $n$ with $n$ *earlier* than $m$ along the chain's proper-time parameter.

Concretely, the BC3 kernel structure demands:
$$
K_\mathrm{vac}^\mathrm{sym}(x, x') \supset \sum_K \sum_{n < m} \mathcal{F}_K(x; \tau_K^{(n)}) \cdot U_K^\mathrm{back}(n, m) \cdot \mathcal{F}_K^\dagger(x'; \tau_K^{(m)})
$$
with $U_K^\mathrm{back}(n, m) \neq 0$ for $n < m$ (the backward chain propagator).

### 2.3 Backward contributions violate P11 irreversibility

P11 commitment-irreversibility (taken as primitive-given per opening decision §2.1) specifies: a committed event at proper time $\tau_K^{(m)}$ is a fact of the chain's past relative to $\tau_K^{(n)}$ for any $n > m$, and is *not* a fact of the chain's past relative to $\tau_K^{(n)}$ for $n < m$ — in the latter case, the event hasn't happened yet relative to the chain at index $n$.

Backward propagation $U_K^\mathrm{back}(n, m) \neq 0$ for $n < m$ would require: a perturbation at $\tau_K^{(m)}$ (a future event from the perspective of $\tau_K^{(n)}$) producing a change in the chain state at $\tau_K^{(n)}$ (an earlier event). This is precisely *un-commitment*: it amounts to retroactive modification of past chain content based on future events. P11 explicitly forbids this.

**Backward chain contributions structurally violate P11.**

### 2.4 Backward contributions violate chain-propagator structure

Independently of P11's high-level prohibition: the chain forward-propagator $U_K(n, m)$ is defined as the bandwidth-update operator that maps chain state at $\tau_K^{(m)}$ to chain state at $\tau_K^{(n)}$ for $n \geq m$. The propagator is constructed step-by-step via the chain's discrete bandwidth-update rule (P04 + commitment events at successive proper-time intervals supplied by P13).

The discrete update rule operates by accumulating forward — it is a sequence-construction object, not a relation that admits inversion. Asking for $U_K^\mathrm{back}(n, m)$ for $n < m$ amounts to asking for the *inverse* of the forward propagator, which (a) is not generically defined for the discrete bandwidth-update structure (the update rule may not be invertible at the level of chain bandwidth content under P04), and (b) even if formally defined as an operator inverse, would still represent backward-in-proper-time propagation, conflicting with P11.

The chain-propagator structure itself does not admit backward propagation as a primitive-level object. BC3 cannot be constructed from chain dynamics by any operator-inversion or alternative chain-side construction.

### 2.5 Could BC3 be sourced non-chain-side?

V1 is the response kernel — by definition, it acts on chain perturbations and propagates them through the substrate. Non-chain-sourced contributions to V1 would not be "response" contributions; they would be intrinsic vacuum content (Wightman-type correlators).

The unperturbed vacuum correlator $W(x, x')$ is a *different object* from V1 — it is the two-point function of the field operators in the vacuum state, and is symmetric (or has the standard $W(x, x') = W^*(x', x)$ structure). $W$ exists at continuum approximation and at primitive level, but it is not V1. **The CR continuum-approximation framing (B.2 §4.4) explicitly preserves the distinction**: V1 (response kernel, retarded) and $W$ (correlator, symmetric) coexist as distinct objects.

Therefore BC3 cannot be sourced from outside the chain ensemble *as a response kernel*. Any symmetric content lives in $W$, not in V1.

### 2.6 BC3 verdict

**BC3 is REFUTED-by-non-construction.** Symmetric V1 has no primitive-level construction admitting it: chain-side contributions are forward-only by P11 + chain-propagator structure; non-chain sources do not exist for response kernels.

This is a *constructive* refutation rather than a constraint-violation refutation: BC3 satisfies all four explicit constraints (C1+C2+C3+CR) but cannot be sourced. The refutation is structural — there is no path from primitives to BC3.

---

## 3. REFUTED evaluation of the advanced kernel

### 3.1 Definition

**Advanced V1:** $K_\mathrm{vac}^\mathrm{adv}(x, x') = \theta(t' - t) \cdot G(\sigma(x, x') / \ell_\mathrm{ED}^2)$ — backward-light-cone-only support. The kernel is non-zero only when $(x' - x)$ lies in the forward causal cone, equivalently when $x$ lies in the backward causal cone of $x'$.

### 3.2 Required chain contributions for advanced kernel

For advanced V1 to arise from chain contributions, *all* chain-contribution terms must have $\tau_K^{(n)} < \tau_K^{(m)}$ — i.e., every chain contribution must propagate backward in proper time. There would be no forward contributions; the chain forward-propagator $U_K(n, m)$ would have to vanish for $n \geq m$ and be non-zero only for $n < m$.

This is the *reverse* of the chain-propagator structure that B.2 §3.4 establishes. It would require the inverse temporal direction throughout the chain ensemble.

### 3.3 Direct violation of P11

P11 commitment-irreversibility specifies forward-only commitment-event ordering across the chain ensemble. Advanced V1 demands backward-only chain contributions, which would require the chain's commitment-event structure itself to run in reverse. This is *not* a partial violation of P11 in some sub-case — it is a *global inversion* of P11's direction-bearing content.

P11 as a primitive does not admit such inversion; it specifies one direction (forward). The advanced kernel is structurally inconsistent with P11.

### 3.4 Direct violation of P13 proper-time ordering

P13 supplies proper-time intervals along $\gamma_K$. Under P11, these intervals are ordered increasingly with chain index: $\tau_K^{(m+1)} > \tau_K^{(m)}$. Advanced V1's chain contributions would require $\tau_K^{(n)} < \tau_K^{(m)}$ for all contributing pairs — i.e., every contribution propagates from later to earlier proper time.

This requires P13's proper-time intervals to be traversed in reverse order. P13 alone is direction-neutral, but the joint P11+P13 structure orients them forward. Advanced V1's traversal in reverse is incompatible with this joint orientation.

### 3.5 Conflict with the participation rule (P07)

P07 (rule-type / Lever L1) specifies bandwidth partition patterns $w_\tau^X$ that operate on chain bandwidth content. Under P11 + P04, chain bandwidth content is accumulated forward; the partition rule operates on this *forward* history.

Advanced V1 would require the partition to operate on *future* bandwidth — content that has not yet been accumulated. This is structurally vacuous: there is no future bandwidth content to partition, because chain bandwidth at $\tau_K^{(n)}$ depends only on $\{\tau_K^{(m)} : m \leq n\}$ per P11 carry-through.

The rule-type structure of P07 has no future-content to operate on. Advanced V1 is structurally inconsistent with P07 application.

### 3.6 Conflict with N1-E bandwidth inheritance

N1-E (vacuum-induced bandwidth memory) is FORCED-conditional-on-V1 per `non_markov_forced.md` §3.5. If V1 were advanced, N1-E would inherit backward-only kernel structure: bandwidth at $\tau$ would depend on *future* bandwidth content, not past.

This contradicts P11 directly: bandwidth at $\tau_K^{(n)}$ is defined to depend only on $\{\tau_K^{(m)} : m \leq n\}$. An advanced N1-E forces bandwidth at $\tau_K^{(n)}$ to depend on $\{\tau_K^{(m)} : m > n\}$. Direct P11 contradiction.

The cascade structure refutes advanced V1 from a different angle than the chain-contribution argument: even if (counter to §3.3) advanced V1 could somehow be constructed at the kernel level, its cascade to N1-E would still violate P11 on the bandwidth-update side. **Advanced V1 is over-determined-refuted.**

### 3.7 Advanced V1 verdict

**Advanced V1 is REFUTED-by-contradiction.** The refutation is multiple-fronted:
- C1 consistency: refuted at B.2 §2.3 (P11 carry-through conflict).
- §3.3: direct global P11 inversion.
- §3.4: P13 ordering reversal incompatibility.
- §3.5: P07 rule-type application has no future-content to operate on.
- §3.6: N1-E cascade refutation independent of kernel-level argument.

This is the cleanest refutation in the arc — every primitive-level structural feature points the same direction.

---

## 4. Hybrid and weighted-symmetric variants

### 4.1 Hybrid taxonomy

We audit four classes of mixed forward/backward kernels:

- **(H1)** Forward-dominant + backward-nonzero: $K = \theta(t-t') \cdot G + \epsilon \cdot \theta(t'-t) \cdot G$ for small $\epsilon > 0$.
- **(H2)** Angular-restricted backward: backward support only in some spatial directions; forward support in all directions.
- **(H3)** Weighted symmetric: $K = w_\mathrm{fwd}(x, x') \cdot \theta(t-t') \cdot G + w_\mathrm{back}(x, x') \cdot \theta(t'-t) \cdot G$ with $w_\mathrm{back} \neq 0$ somewhere.
- **(H4)** Time-symmetric core + directional envelope: $K = G_\mathrm{sym}(\sigma) \cdot E(t-t')$ with $G_\mathrm{sym}$ symmetric and $E$ a direction-modulating envelope.

The audit checks whether any hybrid form admits a primitive-level construction.

### 4.2 (H1) Forward-dominant + backward-nonzero — REFUTED

Any non-zero backward component in V1, regardless of magnitude, requires non-zero backward chain contributions $U_K^\mathrm{back}(n, m) \neq 0$ for some $n < m$. This is the same backward-propagator content that BC3 demanded (§2.2–2.4) and is forbidden by P11 + chain-propagator structure for the same reasons.

The amplitude $\epsilon$ is irrelevant: the construction does not become admissible at small $\epsilon$ because the *type* of contribution required is forbidden, not its magnitude. **(H1) REFUTED-by-non-construction** for any $\epsilon > 0$.

### 4.3 (H2) Angular-restricted backward — REFUTED

Restricting backward support to a subset of spatial directions does not change the temporal structure: any backward-cone support, in any spatial cone of directions, requires chain contributions with $\tau_K^{(n)} < \tau_K^{(m)}$. The chain-propagator structure does not admit angular-selective backward propagation — the propagator $U_K(n, m)$ is a function of chain indices, not of spatial direction.

Even if one *could* construct an angular filter at the kernel level, it would have to act on a non-existent backward chain contribution. **(H2) REFUTED.**

### 4.4 (H3) Weighted symmetric — REFUTED

Identical to (H1) generalised to position-dependent weights $w_\mathrm{back}(x, x')$. The refutation argument is unchanged: any non-zero $w_\mathrm{back}$ at any $(x, x')$ requires backward chain contributions in that region, which P11 forbids. **(H3) REFUTED.**

### 4.5 (H4) Symmetric core + directional envelope — REFUTED

The decomposition $K = G_\mathrm{sym}(\sigma) \cdot E(t-t')$ separates a symmetric core from a directional envelope. The envelope $E(t-t')$ may pick a direction (e.g., $E = \theta(t-t')$), but the symmetric core $G_\mathrm{sym}$ has support on both light cones in isolation.

Two readings:
- **Reading (H4a):** The full kernel $K = G_\mathrm{sym} \cdot E$ has only forward support if $E = \theta(t-t')$. Then the kernel is *equivalent* to the retarded form $\theta(t-t') \cdot G_\mathrm{sym}$, which is just retarded V1 with $G_\mathrm{sym}$ as the Lorentz-scalar form factor. **Not a distinct candidate** — it is a re-parameterisation of the retarded kernel.
- **Reading (H4b):** The symmetric core $G_\mathrm{sym}$ is the *primary* structural object and the envelope $E$ is a multiplicative restriction. Then primitive-level construction must produce the full $G_\mathrm{sym}$ with both-cone support before the envelope acts. The chain-contribution sum produces only forward-cone support, so $G_\mathrm{sym}$ itself is not chain-sourced. The envelope cannot generate the missing backward-cone content; it can only restrict pre-existing content. **Refuted by the same non-construction argument as BC3.**

Under either reading, (H4) is not a viable alternative. **(H4) REFUTED** (or trivially equal to retarded V1, in the (H4a) reading).

### 4.6 Hybrid summary

All four hybrid classes reduce to the same chain-contribution argument as BC3: any non-zero backward-cone support requires non-existent backward chain contributions, which P11 + chain-propagator structure forbid. **No hybrid kernel admits a primitive-level construction.**

---

## 5. PDE-level neutrality check

### 5.1 PDE T-symmetry

The canonical ED PDE structure at form level (KG-class second-order, Cl(3,1) signature, Dirac T-symmetric per R.3) is **time-reversal-symmetric at the equation level**. This was established at the catalogue stage (B.1 §5) and re-confirmed at B.2 §3.5: PDE structure does not source a temporal direction.

The question for B.3: could PDE T-symmetry *override* the kernel directionality established by primitive-level chain dynamics — i.e., could the PDE re-introduce backward-cone content in V1 that the chain-contribution argument excluded?

### 5.2 PDE does not override kernel directionality

The PDE is the *equation* of the relevant field theory; the kernel V1 is a specific *Green's function* of that equation. Equations admit multiple Green's functions: the same KG equation has retarded $G_R$, advanced $G_A$, Feynman $G_F$, and symmetric $G_\mathrm{sym}$ as distinct admissible solutions — all of which satisfy the PDE.

T-symmetry of the equation **does not force T-symmetry of the selected Green's function**. The Green's function is determined by *boundary conditions* / *kernel-construction prescriptions*, which lie outside the PDE proper.

In ED, V1 is the response kernel selected by primitive-level chain dynamics (B.2 §3.4). The PDE provides the equation V1 satisfies; the primitive-level structure provides the boundary conditions / construction prescription that selects V1 as retarded among the equation's admissible Green's functions.

**The PDE does not, and cannot, override the kernel directionality.** The selection happens at the construction level, not the equation level.

### 5.3 PDE cannot rescue symmetric or advanced kernels

If primitive-level construction selects retarded V1, the PDE does not permit the alternative kernels (BC3, advanced, hybrid) to enter via some PDE-level back-pressure. The PDE is satisfied by all admissible Green's functions; V1 is *one specific choice*, fixed by the chain-contribution structure.

There is no PDE-level mechanism by which the symmetric or advanced or hybrid kernels could be re-introduced. **PDE-level T-symmetry does not generate any rescue path for the REFUTED candidates.**

### 5.4 PDE-level neutrality verdict

**Confirmed.** PDE-level structure is a direction-neutral substrate that propagates whatever direction is supplied at the kernel-construction level. The §2 / §3 / §4 refutations are not undone by PDE-level considerations.

---

## 6. Cross-arc consistency

### 6.1 Arc N (N1, N1-E)

**Theorem N1 (V1 finite-width vacuum kernel) — preserved.** N1's explicit fixes (Lorentz-scalar, finite-width, decaying, both-ways-bounded by V1-δ and V1-∞ refutations) are independent of retardation. Retarded V1 is a *refinement* of N1's form-class: it adds the support specification (forward causal cone) without modifying the pre-existing form-class fixes. **Theorem N1 is unchanged; FORCED retarded V1 is consistent with N1.**

**N1-E (vacuum-induced bandwidth memory) — refined.** N1-E was established as FORCED-conditional-on-V1 per `non_markov_forced.md` §3.5. Under retarded V1, N1-E is forward-only memory. This is the structurally honest reading of the "memory" terminology: bandwidth at $\tau$ depends on past bandwidth, never future. **Refinement of N1-E directionality, not an overturn.**

The cascade items N2-E (vacuum-modulated commitment memory), N3-D (vacuum-mediated adjacency memory), V5 (vacuum-induced cross-chain correlations) inherit the same forward-only refinement consistently. **Arc N is fully consistent with FORCED retarded V1.**

### 6.2 Arc Q (Theorem 17)

**Theorem 17 (gauge fields as forced rule-type structure) — preserved.** T17's nine clauses C1–C9 (carrier, group, vertex, worldline, vacuum kernel, three vacuum classes, vacuum strict-non-commit + B[v;τ_g] additive, unified gauge-quotient, acyclic derivability) operate within rule-type sectors $\tau_g$. Vacuum-coupling in clauses C5–C7 inherits V1 kernel structure; under retarded V1, the rule-type vacuum coupling is forward-only.

This **refines** T17's vacuum-coupling clauses without modifying the gauge-quotient or minimal-coupling content of T17. The forced existence of A_μ as the participation measure of $\tau_g$ is independent of V1 directionality; T17's structural content is preserved. **Theorem 17 is fully consistent with FORCED retarded V1.**

### 6.3 Arc M (F-M8 cascade)

The Arc M cascade items (M.1 massless-slot resolution, M.2 mass-form additivity, M.3 cross-sector coupling, M.4 verdict refresh) are unblocked by Theorem 17. Among these, **F-M8** (τ_g-mediated mass-form contribution channel through V1 vacuum kernel) is the most directly affected by Arc B's verdict.

Under retarded V1, F-M8's mass-form contribution is mediated by *forward-only* vacuum coupling: a chain's mass-form content at proper time $\tau$ receives contributions from prior chain history via the V1 kernel, never from future history. This is a refinement of F-M8's mediation directionality — the form-FORCED status of F-M8's contribution channel is unchanged; the *direction of mediation* is now forward-only.

**Arc M F-M8 cascade is consistent with FORCED retarded V1.** The cascade's structural conclusions are preserved; the directionality is refined.

### 6.4 UV-FIN (Theorem Q.8)

UV-FIN (FORCED at primitive level via Primitive 01 + Primitive 13 + Primitive 04 jointly per Q.8 closure) bounds the kernel's UV behaviour. The retarded restriction $\theta(t - t')$ is a multiplicative theta-function applied to the form-factor $G(\sigma)$; the high-frequency / UV behaviour of the kernel is determined by $G(\sigma)$, not by $\theta(t-t')$.

**UV-FIN is preserved exactly as before.** The retarded structure does not modify the UV bound; the form-factor's sub-power-law-2 decay continues to bound the kernel's UV content per Q.8 §5.2. **No UV-FIN conflict.**

### 6.5 Lorentz covariance

Under the proper orthochronous Lorentz group $L_+^\uparrow$, the retarded kernel transforms covariantly: $\theta(t-t')$ is invariant under $L_+^\uparrow$ (which preserves time orientation), and $G(\sigma)$ is invariant under the full Lorentz group. **Lorentz covariance under $L_+^\uparrow$ is preserved.**

Discrete time-reversal T is not a primitive-level symmetry — P11 explicitly breaks it. Demanding full Lorentz including T as a constraint would conflict with P11 itself. The relevant covariance group at primitive level is $L_+^\uparrow$, not full Lorentz. **No Lorentz-covariance conflict.**

### 6.6 Retarded V1 ↔ retarded Green's function correspondence

At continuum approximation, ED's V1 maps to the standard retarded Green's function $G_R(x, y)$ of the underlying wave equation. The standard QFT relation
$$
G_R(x, y) = i \theta(t_x - t_y) [W(x, y) - W(y, x)]
$$
expresses $G_R$ in terms of the symmetric Wightman correlator $W$. **This correspondence is consistent with FORCED retarded V1 at primitive level.** ED's primitive-level claim is a statement about V1; the continuum-approximation identification is with $G_R$.

### 6.7 Symmetric Wightman correlator $W$ unaffected

The Wightman correlator $W(x, y) = \langle 0 | \hat{\phi}(x) \hat{\phi}(y) | 0 \rangle$ is a *distinct* object from V1. $W$ measures intrinsic vacuum correlations; V1 measures vacuum response to chain perturbations. They are different physical quantities related by the standard identity above.

**Arc B's verdict on V1 does not constrain $W$.** $W$ remains symmetric as standard QFT prescribes. The CR continuum-approximation framing operates exactly: primitive-level retarded V1, continuum-level symmetric $W$, retarded $G_R$, Feynman $G_F$ — all coexist as distinct structural / continuum-approximation objects. **No conflict between primitive-level retardation and continuum-approximation Wightman / Feynman propagators.**

### 6.8 Cross-arc consistency verdict

**All cross-arc audits pass.** Arc N, Arc Q (T17), Arc M (F-M8), UV-FIN, Lorentz covariance, and the retarded ↔ continuum correspondence are all consistent with FORCED retarded V1. No Phase-2 / N-arc / Phase-3 closure is back-pressured.

The detailed Phase-3 GR1 carry-over audit is deferred to B.4, but no obstruction is anticipated: GR1 extends V1 to curved spacetime via Synge's world function, and the retarded restriction transfers to the Hadamard-parametrix-restricted-to-causal-future structure naturally.

---

## 7. Falsifier status update

The B.0 §4.3 canonical falsifier set (BFal-1 through BFal-6) is the authoritative numbering. The B.3 prompt described falsifiers in terms of *content tests dispatched at this stage*; those tests are sub-cases within the canonical numbering. Below: each canonical falsifier is updated post-B.3, with the user's content-test descriptions mapped explicitly.

### 7.1 BFal-1 — catalogue exhaustion

**B.0 description:** Have all plausible asymmetry sources been catalogued?
**B.3 status: dispatched conditional on P05/P08/P12 neutrality.** B.1 §7.5 dispatched BFal-1 conditionally pending verification of P05, P08, P12 constitutional content. B.3 confirms that the forcing argument (B.2 §3.4) and the refutation arguments (this memo §2–4) route through P11 + P02 + P04 + P13 only — not through P05, P08, or P12. **The forcing and refutation verdicts are robust to P05/P08/P12 verification.** Catalogue exhaustion as a complete-survey claim still requires verification, but the V1 retardation FORCED + alternatives REFUTED verdicts are not contingent on it.

User-prompt mapping: addressed under canonical BFal-1.

### 7.2 BFal-2 — carry-through soundness

**B.0 description:** Does the Primitive-11-to-V1 carry-through argument require auxiliary inputs?
**B.3 status: dispatched dark.** The chain-contribution construction (B.2 §3.4) routes through ED-internal structures only (P11 + P02 + P04 + P13 + Q.8 effective-vacuum factorisation); no external assumption imports the arrow. **Confirmed.**

User-prompt mapping (the user's "BFal-2: symmetric kernel viability"): the symmetric kernel has been formally REFUTED in §2. This is a *content dispatch* corresponding to the "BC3 alternative" canonical falsifier (BFal-4 below). It is also confirmation of carry-through soundness in the sense that the carry-through argument is sufficient to refute the leading alternative.

### 7.3 BFal-3 — relativistic consistency

**B.0 description:** Does primitive-level FORCED retardation contradict continuum-approximation relativistic-QFT consistency?
**B.3 status: dispatched dark.** §6.7 confirms: primitive-level retarded V1 ↔ continuum-approximation $G_R$, with symmetric Wightman correlator $W$ unaffected as a distinct object. CR framing operative; no contradiction. **Confirmed.**

User-prompt mapping (the user's "BFal-3: advanced kernel viability"): the advanced kernel has been formally REFUTED in §3. Again a content dispatch corresponding to the BC3-alternative canonical falsifier (the advanced kernel is a refuted alternative variant). Mapped under canonical BFal-4 below.

### 7.4 BFal-4 — BC3 / non-retarded alternative

**B.0 description:** Does the symmetric-finite-support kernel (BC3) genuinely satisfy all primitive-level constraints?
**B.3 status: dispatched dark (final).** §2 establishes BC3 is REFUTED-by-non-construction; §3 establishes advanced V1 is REFUTED-by-contradiction; §4 establishes all hybrid variants are REFUTED by the same chain-contribution argument. **All non-retarded V1 candidates are formally refuted at primitive level.**

User-prompt mapping (the user's "BFal-4: hybrid variants"): hybrids H1–H4 formally REFUTED in §4. **Mapped to canonical BFal-4.**

### 7.5 BFal-5 — cross-arc consistency

**B.0 description:** Does Arc B's verdict create back-pressure on Phase-2 / N-arc / Phase-3 closures?
**B.3 status: provisionally dispatched dark; full audit pending B.4.** §6 dispatches all Phase-2 / N-arc audits (Arc N, Arc Q T17, Arc M F-M8, UV-FIN, Lorentz). Phase-3 GR1 cross-arc audit is the explicit deliverable of B.4 cross-arc implications. **Provisional pass; final dispatch at B.4.**

User-prompt mapping (the user's "BFal-5: propagation to observables"): the observable-signature mapping (which measurable quantity distinguishes primitive-level retardation from continuum-approximation Feynman) is the central deliverable of B.4. **Pending B.4.**

### 7.6 BFal-6 — acyclicity

**B.0 description:** Does any substage memo use a downstream conclusion as a derivation input?
**B.3 status: dispatched dark.** §1–§6 of this memo use only B.0 + B.1 + B.2 inputs and ED primitives + Phase-1/2 theorems + Theorem N1 as derivation premises. No B.4 / B.5 / downstream content is invoked. **Acyclicity preserved.**

User-prompt mapping (the user's "BFal-6: PDE-level cancellation"): the PDE-level neutrality dispatch in §5 confirms PDE T-symmetry does not rescue any non-retarded candidate. This is a *cancellation-pathway* check, mapped under canonical BFal-4 (the BC3 alternative as expanded). PDE-level cancellation is REFUTED. **Mapped under BFal-4 + BFal-6.**

### 7.7 Falsifier summary

| Canonical | B.3 status | User-prompt content-test mapping |
|---|---|---|
| BFal-1 catalogue exhaustion | Dispatched conditional on P05/P08/P12 | "BFal-1" (same) |
| BFal-2 carry-through soundness | Dispatched dark | (also addressed: symmetric refutation in §2) |
| BFal-3 relativistic consistency | Dispatched dark | (also addressed: advanced refutation in §3) |
| BFal-4 BC3 / non-retarded alternatives | **Dispatched dark (final)** | "BFal-2 symmetric" + "BFal-3 advanced" + "BFal-4 hybrids" + "BFal-6 PDE cancellation" all map here |
| BFal-5 cross-arc consistency | Provisional dispatch; pending B.4 | "BFal-5 propagation to observables" — pending |
| BFal-6 acyclicity | Dispatched dark | (acyclicity preserved throughout) |

**Five of six canonical falsifiers dispatched dark or conditional after B.3; BFal-5 the only remaining open item, pending B.4 cross-arc audit.**

---

## 8. Provisional arc verdict

### 8.1 Refutation summary

After B.3, the structural status of every candidate kernel form:

| Candidate | Status | Refutation route |
|---|---|---|
| Retarded V1 | **FORCED** (B.2 §5.1) | — |
| Symmetric V1 (BC3) | **REFUTED-by-non-construction** | §2.6 |
| Advanced V1 | **REFUTED-by-contradiction** | §3.7 (multi-front) |
| (H1) Forward + ε backward | **REFUTED-by-non-construction** | §4.2 |
| (H2) Angular-restricted backward | **REFUTED-by-non-construction** | §4.3 |
| (H3) Weighted symmetric | **REFUTED-by-non-construction** | §4.4 |
| (H4a) Symmetric core × forward envelope | (Equivalent to retarded V1; not distinct) | §4.5 |
| (H4b) Symmetric core × symmetry-preserving envelope | **REFUTED-by-non-construction** | §4.5 |
| PDE-level cancellation | **REFUTED** (cannot rescue alternatives) | §5 |

**Every non-retarded candidate is refuted.** The refutation routes are structurally distinct (non-construction for symmetric/hybrid, multi-front contradiction for advanced) but converge on the same conclusion.

### 8.2 Retarded kernel uniqueness

The retarded kernel is the **uniquely admissible V1 candidate at primitive level**. This is the strict converse of the FORCED verdict from B.2: not only is retardation forced, but no alternative candidate is admissible.

Uniqueness is established by:
- (B.2) constructive forcing of retarded V1 from chain dynamics.
- (B.3) refutation of every alternative candidate by either non-construction (symmetric, hybrids) or contradiction (advanced).
- Full coverage of the candidate space (BC3 + advanced + four hybrid classes + PDE-cancellation pathway).

### 8.3 Theorem 18 structurally locked in (pending B.4 / B.5)

**Theorem 18 (V1 kernel retardation FORCED) is structurally locked at primitive level subject to:**
- B.4 confirming Phase-3 GR1 cross-arc consistency (anticipated but not yet executed).
- B.4 producing the CR continuum-approximation framing table (UV-FIN-style primitive-vs-continuum mapping).
- B.4 identifying any observable-signature implications (BFal-5 dispatch).
- B.5 final synthesis with explicit theorem statement and unconditional falsifier dispatch.

The arc-level verdict at the close of B.3:

**The microscopic arrow of time is FORCED at the kernel level. V1 is uniquely retarded. All alternatives are REFUTED. Theorem 18 is structurally established subject to B.4 cross-arc audit and B.5 synthesis.**

---

## 9. Recommended next steps

### 9.1 B.4 cross-arc implications (immediate next memo)

Open `arrow_implications.md`. Specific deliverables:

(i) **Phase-3 GR1 carry-over audit.** Confirm that retarded V1 lifts to retarded $K_\mathrm{vac}^\mathrm{curved}$ in curved spacetime via Synge's world function with appropriate causal-future restriction. Anticipated: clean lift; the Hadamard-parametrix structure naturally accommodates the $\theta$-restriction.

(ii) **CR continuum-approximation framing table.** Produce the explicit mapping table for primitive-level kernel structure ↔ continuum-approximation Green's function structure, paralleling the Q.8 UV-FIN primitive-vs-continuum table. Columns: primitive-level (V1 retarded), continuum-level objects ($G_R$, $G_A$, $G_F$, $W$), correspondence, where each appears in the inventory.

(iii) **Observable-signature mapping (BFal-5 dispatch).** Identify any measurable signature distinguishing primitive-level retardation from purely continuum-level retardation. Anticipated: dispersion-relation modification at very-high-frequency / event-discreteness scale, or modification of vacuum-polarisation analytic structure. Cross-link to UV-FIN signature program if relevant.

(iv) **N-arc cascade refinement detail.** Document how N1-E, N2-E, N3-D, V5 directionality refinements propagate to specific Phase-2 closures (Arc M F-M8, Arc Q.5 vacuum polarisation, Arc Q.6 mixing CP, Arc Q.8 Λ structural channels).

(v) **Arc B-thermo follow-on hooks (out-of-scope but flagged).** Briefly identify the hooks for a follow-on thermodynamic-arrow arc — specifically, how forward-only V1 + N1-E memory structure could supply a primitive-level entropy-production source. This is *flagging only*, not derivation; the thermodynamic arrow remains out of scope per Arc B opening decision.

### 9.2 P05 / P08 / P12 verification (parallel; pre-B.5)

**Recommendation:** verify P05 / P08 / P12 constitutional content against the `ED-primitives` repo before B.5 closes. The forcing and refutation arguments are robust to their direction-neutrality assumption, but the BFal-1 catalogue-exhaustion claim becomes unconditional only after verification. This task can be performed in parallel with B.4 and does not block B.4 progress.

### 9.3 Theorem numbering coordination with Arc M cascade

The current FORCED-theorem inventory ends at Theorem 17 (Arc Q closure via T17). Arc M residual cascade (M.1–M.4) is mechanical-residual cleanup but may produce a Theorem 18 if M.4's verdict refresh materially refines. **Coordinate with Arc M timing**: if M.4 closes before Arc B does, Arc B's theorem becomes Theorem 19; if Arc B closes first, M.4's potential theorem (if any) becomes Theorem 19. **Provisional:** Arc B candidate is Theorem 18 (or 19, pending Arc-M cascade). Final numbering at B.5.

### 9.4 Synthesis-paper revision pre-flag

The synthesis paper at `papers/QM_Emergence_Structural_Completion/` (per project memory) is in line for §§3.3–3.5 + §4 revision after Phase-1 closure. With Theorem 18 (Arc B) added to the inventory, the revision should be coordinated: §3 inventory tables grow; §4 reduction-count discussion now reads "zero upstream commitments + one description-level continuum gauge + one primitive-level kernel-arrow theorem" (or similar framing). **This is project-management coordination, not Arc B work**; flagged here so it is not lost.

### 9.5 Public-facing artifact preparation

Theorem 18 is the cleanest arrow-of-time derivation in the literature (per B.0 §1.3). Once B.5 closes, recommend:
- A desktop public explainer in the same Science-Friday-voice as `ED_Theorem17_Gauge_Fields_Explainer.md`. Title candidate: *"Why Time Has a Direction — and What 'Forward' Actually Means at the Smallest Scale."*
- A publication-grade SVG showing the forcing chain (P11 → chain dynamics → V1 → retardation → arrow of time), parallel to `ED_Theorem17_Derivation_Architecture.svg`.
- A public SVG showing the postulate-to-forced inversion ("Time's arrow is usually a mystery / a postulate / a thermodynamic accident — Event Density makes it a structural theorem").

These artifacts can be drafted after B.5 closes; flagged here to preserve context.

---

Ready for B.4 — Cross-Arc Implications.
