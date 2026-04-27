# Arrow-of-Time Source Catalogue

**Arc B Stage B.1 — Catalogue Memo**
**Status:** Catalogue only. Enumerates the structurally admissible candidate sources of microscopic temporal asymmetry across the ED primitive set (01–13), the FORCED-theorem inventory (Theorems 1–17), and the Arc N kernel-level results (Theorem N1, N1-E cascade). For each candidate: structural content, role in any kernel-arrow argument, what would force an arrow through that candidate, what would refute one. Headline catalogue: **11 primitive-level candidates (P01–P13 audit), 4 kernel-level candidates (V1 sub-features), 4 memory-level candidates (N1-E sub-features), 3 PDE-level candidates (KG-class structure / Dirac-class structure / spinor-bundle direction), plus a cross-interaction map**. Catalogue verdict: **multiple candidate sources exist; one candidate (P11 irreversibility) is already-primitive-given by the opening decision; one candidate (V1 retardation) is the load-bearing target of B.2; no candidate is already-refuted at the catalogue stage**. BFal-1 (catalogue exhaustion) hooks listed at §7. **The constitutional content of P05, P08, P12 is not reproduced in any in-tree memo I have access to; these primitives are catalogued functionally with explicit verification-required flags. The user should sanity-check against the `ED-primitives` repo before B.2 closes.**

---

## 1. Catalogue overview

### 1.1 Purpose

The catalogue enumerates *every* structurally admissible candidate source of microscopic temporal asymmetry that could carry through to an Arc B verdict. The B.0 scoping memo identified three plausible carry-through routes (R1 chain bandwidth-update directionality, R2 causal-cone restriction, R3 UV-FIN + irreversibility joint argument). B.1 widens that survey: any source of asymmetry that could *contribute* to a kernel-level arrow — whether it acts directly on the V1 kernel, indirectly through the N1-E cascade, or upstream through primitive-level structure — is logged here. The B.2 forced-evaluation stage will then evaluate which candidates close as primitive-level forcing arguments under the FORCED criterion (consistency / necessity / constraint compliance).

The discipline is exhaustion-then-evaluation: B.1 errs toward inclusion, even where a candidate is plausibly admissible-not-forced or plausibly refuted. B.2 narrows. The cost of a thin catalogue is missing a forcing route that closes; the cost of a thick catalogue is one extra evaluation pass per candidate. The asymmetry favours inclusion.

### 1.2 Evaluation criteria for catalogue entries

Each entry is recorded with five fields:

- **(C-1) Structural content.** What the candidate *is* in the ED inventory: which primitive, theorem, or derived structure carries the asymmetry-relevant content.
- **(C-2) Direction-bearing status.** Whether the candidate is *directly direction-bearing* (intrinsically picks forward), *direction-inheriting* (forward only via dependence on a direction-bearing item), *direction-neutral* (carries no temporal direction), or *direction-ambiguous* (admits direction or symmetry depending on interpretation).
- **(C-3) Forcing role.** What would have to be true for this candidate to *force* the V1 kernel as retarded — direct structural argument, cascade through N1-E, or upstream constraint.
- **(C-4) Refutation profile.** What would refute this candidate as a forcing source — auxiliary-input requirement, constraint violation, or admissibility of a symmetric alternative.
- **(C-5) V1 / N1-E interaction.** How the candidate interacts with V1 kernel structure (per Theorem N1) and the N1-E vacuum-induced bandwidth memory cascade (per `non_markov_forced.md` §3.5).

### 1.3 Notation

Primitives referred to by short codes: **P01–P13**. Theorems: **T1–T17, TN1, TGR1**. Constraints: **C1 Lorentz covariance, C2 spin-statistics, C3 UV-FIN, CR continuum-approximation relativistic consistency** (per B.0 §2.4). The V1 kernel is referenced by symbol $K_\mathrm{vac}$ throughout; the N1-E vacuum-induced bandwidth memory by $K_{N1\text{-}E}$ when distinguished.

---

## 2. Primitive-level candidates

The audit traverses primitives 01–13 in order. Coverage matches what is enumerated in [`arc_n_scoping.md`](../arc-N/arc_n_scoping.md) §2.1 (P01, P02, P03, P04, P06, P07, P09, P10, P11, P13); P05, P08, P12 are not enumerated there and their constitutional content lives in the `ED-primitives` repo. I include each at its expected functional role with an explicit **verification flag** so that the B.2 evaluation does not propagate any fabricated content.

### 2.1 P01 — Event discreteness

**(C-1)** Discrete events on the event manifold; primitive-level event-resolution scale $\ell_\mathrm{ED}$ below which the substrate is not continuum-like.
**(C-2)** **Direction-neutral.** Event-discreteness fixes a *resolution* but not a *direction*; a discrete-event manifold can be traversed forward or backward without contradiction at the level of P01 alone.
**(C-3)** P01 contributes to V1's *finite-width* property (per `non_markov_forced.md` §2.2) but supplies no direction-bearing content.
**(C-4)** Refuted as a forcing source for retardation by direct inspection: a symmetric finite-width kernel respects P01 equally well as a retarded one.
**(C-5)** P01 is load-bearing for V1's existence (Theorem N1) but neutral for V1's retardation question. Auxiliary input only.

### 2.2 P02 — Chain (worldline)

**(C-1)** Worldlines $\gamma_K$ are continuous structures with persistent identity. Each chain admits a parameterisation by proper time $\tau_K$ (P13).
**(C-2)** **Direction-inheriting.** A worldline is geometrically a 1D submanifold; a *directed* worldline requires a temporal orientation, supplied by P11 commitment-event ordering and (per the opening decision) P11-irreversibility.
**(C-3)** P02 supplies the substrate on which Primitive-11 ordering acts. If P11 is the seed of asymmetry, P02 is the conduit through which chain-level directionality reaches kernel-level structure (route R1 of B.0 §2.3).
**(C-4)** Without P11 carry-through, P02 alone admits forward and backward parameterisations symmetrically. Worldlines are not intrinsically directed.
**(C-5)** Critical for route R1 (chain-contribution construction of V1). If V1 can be constructed as a sum/integral over chain contributions, and P11+P02 together force forward-only chain dynamics, then V1 inherits forward-only support.

### 2.3 P03 — Participation

**(C-1)** Instantaneous; participation density at each event is a single-point quantity with no temporal extent.
**(C-2)** **Direction-neutral.** A pointwise quantity has no direction.
**(C-3)** No direct forcing role. Indirect role only: participation density at chain commitment events is what couples chains to the effective vacuum, so P03 contributes to *which chains contribute to V1* but not to the direction of those contributions.
**(C-4)** N/A — not a candidate forcing source on its own.
**(C-5)** Auxiliary infrastructure only.

### 2.4 P04 — Bandwidth (four-band decomposition)

**(C-1)** Four-band decomposition $b = (b^\mathrm{env}, b^\mathrm{ind}, b^\mathrm{int}, b^\mathrm{rel})$ specifies amplitudes at each event; admits dynamical evolution along $\gamma_K$.
**(C-2)** **Direction-inheriting.** Bandwidth amplitudes are scalars at each event; their *update rule along $\gamma_K$* inherits direction from P11+P13. Per `arc_n_scoping.md` §2.1 P04 is a candidate site for non-Markovian structure but not itself direction-bearing.
**(C-3)** P04 is load-bearing for the N1-E vacuum-induced bandwidth memory cascade. If the bandwidth update rule is forced forward-only by P11 (consequence (c) of B.0 §2.1), then $b^\mathrm{env}$ at later events depends only on the chain's bandwidth history up to that event. This is the bandwidth-level analog of route R1.
**(C-4)** Without P11 carry-through, P04's update rule admits forward or backward integration symmetrically.
**(C-5)** Direct relevance to N1-E: if the bandwidth-update rule is forward-only, $K_{N1\text{-}E}$ inherits forward-only structure; if symmetric, $K_{N1\text{-}E}$ admits both directions.

### 2.5 P05 — *(content verification required)*

**(C-1)** **Verification flag.** P05's constitutional content is not reproduced in `arc_n_scoping.md` §2.1 (the most explicit primitive-by-primitive audit available in-tree). Functionally, P05 most naturally fills the role of a density / sourcing primitive (i.e., the primitive that names the framework — *event density*). Under that functional reading, P05 specifies the density field $\rho_\mathrm{event}$ as a primitive-level quantity.
**(C-2)** Under the functional reading: **direction-neutral.** A density field at each event is a scalar with no temporal direction; integrating it forward or backward is symmetric.
**(C-3)** Under the functional reading: no direct forcing role. P05's contribution to V1 is via specifying *which density field couples to the vacuum-response kernel*, not the direction of coupling.
**(C-4)** Under the functional reading: refuted as a forcing source by direct inspection (density is even-indexed in time).
**(C-5)** Under the functional reading: auxiliary; supplies the source field for V1 but not the direction.

**Recommendation for B.2:** verify P05's actual constitutional content against `ED-primitives` repo before evaluating. If P05 is *not* a density/sourcing primitive but instead carries (e.g.) explicit ordering or sourcing-direction content, this entry must be re-evaluated. The catalogue records the candidate at its most plausible functional reading and flags the verification dependency.

### 2.6 P06 — Four-gradient (Lorentz covariance)

**(C-1)** Four-gradient operator $\partial_\mu$; Lorentz-covariant differential structure on the event manifold.
**(C-2)** **Direction-neutral by construction.** The four-gradient is symmetric under Lorentz transformations including time-reversal in the proper Lorentz group $L_+^\uparrow$ component; full Lorentz including discrete operations admits time-reversal.
**(C-3)** P06 *constrains* the form of any kernel-level construction (must be Lorentz-covariant per C1) but supplies no direction. Crucially, Lorentz-covariance does not preclude retardation: $\theta(t-t') \cdot G(\sigma)$ with $G$ Lorentz-scalar is Lorentz-covariant on the forward causal cone.
**(C-4)** P06 alone does not refute retardation but does not force it either. The causal-cone-vs-forward-cone distinction is not settled by P06.
**(C-5)** P06 is load-bearing for V1's Lorentz-scalar property (per `non_markov_forced.md` §2.2) but neutral for the retardation question.

### 2.7 P07 — Rule-type (Lever L1)

**(C-1)** Rule-types $\tau_g$ specify bandwidth partition patterns $w_\tau^X$ per Arc M; Theorem 17 elevates rule-types as the carriers of gauge-field structure.
**(C-2)** **Direction-inheriting** (via L1 Lever specification). A rule-type's bandwidth partition $w_\tau^X$ is in principle constant in time; it can be made history-dependent (per `arc_n_scoping.md` §2.1 P07), but this is not direction-forcing — history-dependence on either past or future bandwidth would be admissible structurally.
**(C-3)** P07 contributes to V1 via its specification of *which interface content couples to the vacuum*. Theorem 17 makes the gauge-field A_μ a participation measure of $\tau_g$, so vacuum-coupling structure inherits rule-type content. Direction-bearing only if the interface-coupling rule is forward-only.
**(C-4)** Without forward-only interface-coupling, P07 admits time-symmetric vacuum coupling.
**(C-5)** Indirect relevance to V1 via the gauge-field-as-rule-type identification (Theorem 17). N1-E inherits rule-type-mediated bandwidth memory, but the directionality of that memory comes from P11 carry-through, not from P07 itself.

### 2.8 P08 — *(content verification required)*

**(C-1)** **Verification flag.** P08 is not enumerated in `arc_n_scoping.md` §2.1. No reliable inference about its content is available from the in-tree memos accessed for this catalogue.
**(C-2)** Cannot be classified without verification.
**(C-3)** Cannot be evaluated without verification.
**(C-4)** Cannot be evaluated without verification.
**(C-5)** Cannot be evaluated without verification.

**Recommendation for B.2:** P08 must be added to the audit when its content is verified. The catalogue records the entry as a placeholder so B.2 does not implicitly assume P08 is direction-neutral. If P08 turns out to carry direction-bearing content, this entry is upgraded; if direction-neutral, it is closed.

### 2.9 P09 — U(1) polarity phase

**(C-1)** U(1)-valued polarity phase at each event; load-bearing for Theorems 11 (U2-Discrete) and 14 (U1) per the orientation §6.x sensitivity flags.
**(C-2)** **Direction-neutral.** A U(1) phase has no temporal direction; it is a circle-valued field.
**(C-3)** No direct forcing role.
**(C-4)** N/A.
**(C-5)** Auxiliary infrastructure only.

### 2.10 P10 — Individuation

**(C-1)** Threshold-crossing event-class; structurally instantaneous.
**(C-2)** **Direction-inheriting.** Individuation events are point-events with no intrinsic direction; their *ordering* derives from P11+P13. The threshold-crossing event itself is direction-neutral, but the *sequence* of crossings inherits P11 ordering.
**(C-3)** P10 is load-bearing for the multi-chain adjacency structure that supports V5 cross-chain correlations (per Arc Q.2 R-2 closure). If P11 carry-through forces forward-only chain dynamics, multi-chain individuation correlations inherit forward-only structure.
**(C-4)** Without P11 carry-through, individuation events admit symmetric ordering.
**(C-5)** Critical for V5 cross-chain correlation directionality (a downstream Arc B sub-question). Indirect for V1 itself.

### 2.11 P11 — Commitment events (irreversibility)

**(C-1)** Discrete commitment events along $\gamma_K$; **per the Arc B opening decision, P11 includes commitment-irreversibility as an already-primitive given.** Commitment events are non-reversible; a committed event is a fact of the chain's past.
**(C-2)** **Direction-bearing — primitively.** This is the seed of all kernel-level asymmetry candidates that route through chain-level structure. Commitment-irreversibility is the primitive-level analog of measurement-irreversibility in QM.
**(C-3)** P11 is the *only* directly direction-bearing primitive in the inventory under the opening decision. Every primitive-level forcing argument for kernel retardation must route through P11. The three carry-through routes from B.0 §2.3 (R1 bandwidth-update, R2 causal-cone, R3 UV-FIN + irreversibility joint) are P11-rooted.
**(C-4)** P11 cannot be refuted (it is constitutional). Refutation of *kernel-level retardation* requires showing that P11 carry-through fails — i.e., that the chain-level forward-only structure does not propagate to kernel-level forward-only support.
**(C-5)** Direct relevance: V1 retardation is conjectured to follow from P11 carry-through. N1-E directionality cascades from V1.

**This is the load-bearing primitive for the entire arc.** B.2 will evaluate whether P11 carry-through closes structurally.

### 2.12 P12 — *(content verification required)*

**(C-1)** **Verification flag.** P12 is not enumerated in `arc_n_scoping.md` §2.1. No reliable inference available.
**(C-2)** Cannot be classified without verification.
**(C-3)** Cannot be evaluated without verification.
**(C-4)** Cannot be evaluated without verification.
**(C-5)** Cannot be evaluated without verification.

**Recommendation for B.2:** same as P08.

### 2.13 P13 — Relational timing (proper-time intervals)

**(C-1)** Finite proper-time intervals between commitment events along $\gamma_K$; supplies the parameterisation $\tau_K$.
**(C-2)** **Direction-inheriting.** Proper-time *intervals* are ordered as a sequence (P11 supplies the ordering); proper-time *direction* is not specified by P13 alone — increasing $\tau_K$ vs. decreasing $\tau_K$ is a parameterisation choice without P11.
**(C-3)** P13 + P11 jointly direct the chain. P13 alone is direction-neutral; P11 alone supplies discrete ordering without continuous parameterisation. The joint structure is what enables route R1 (forward-only bandwidth update along $\tau_K$).
**(C-4)** Without P11 carry-through, P13 admits both forward and backward parameterisations symmetrically.
**(C-5)** Load-bearing for V1's existence (per `non_markov_forced.md` §2.2 as one of the three primitives forcing finite kernel width); neutral for V1's retardation question except as conduit for P11.

### 2.14 Primitive-level summary

| Primitive | Direction status | Load-bearing for V1 retardation? |
|---|---|---|
| P01 event-discreteness | Neutral | No (auxiliary for V1 width only) |
| P02 chain | Direction-inheriting | Yes (R1 conduit) |
| P03 participation | Neutral | No |
| P04 bandwidth | Direction-inheriting | Yes (R1 + N1-E inheritance) |
| P05 *(verify)* | (functionally neutral) | No (under functional reading) |
| P06 four-gradient | Neutral | No (auxiliary for Lorentz-scalar) |
| P07 rule-type | Direction-inheriting (weak) | Indirect (T17 vacuum-coupling) |
| P08 *(verify)* | Unknown | Unknown |
| P09 U(1) phase | Neutral | No |
| P10 individuation | Direction-inheriting | Indirect (V5 cross-chain) |
| **P11 commitment** | **Direction-bearing (primitively)** | **YES — load-bearing** |
| P12 *(verify)* | Unknown | Unknown |
| P13 proper-time | Direction-inheriting | Conduit (with P11) |

**Net primitive-level reading:** exactly one direction-bearing primitive (P11) seeds the asymmetry. Several primitives (P02, P04, P10, P13) inherit direction from P11 and serve as conduits for carry-through to kernel and memory levels. P05/P08/P12 are catalogue placeholders pending verification but, under their most plausible functional readings, do not change this picture. The kernel-arrow argument is therefore mono-rooted in P11; this is structurally important because it concentrates the entire forcing chain on a single primitive's carry-through soundness, which is what B.2 must audit.

---

## 3. Kernel-level candidates

### 3.1 V1-(a) Lorentz-scalar finite-width structure (the N.2-fixed properties)

**(C-1)** Per `non_markov_forced.md` §2: V1 kernel exists, is finite-width on $\ell_\mathrm{ED}$, Lorentz-scalar, sub-power-law-2 decaying. These are the *fixed* properties from Theorem N1.
**(C-2)** **Direction-ambiguous.** Lorentz-scalar admits both retarded $\theta(t-t') F(\sigma)$ and symmetric $F(\sigma)$ realisations. Finite-width admits both. Sub-power-law-2 decay admits both.
**(C-3)** Forces an arrow only if combined with an asymmetry source (P11 carry-through).
**(C-4)** Refutes an arrow only if the sub-features force symmetry — which they do not (Lorentz-scalar does not preclude retardation).
**(C-5)** This is the *substrate* on which the retardation question is asked.

### 3.2 V1-(b) Support structure (forward / backward / both light cones)

**(C-1)** The kernel's spacetime support: forward causal cone only (retarded), backward causal cone only (advanced), both (symmetric / time-reversal-invariant), or full causally-connected region.
**(C-2)** **Direction-ambiguous at N.2 level.** The N.2 derivation does not explicitly fix support. C1 Lorentz covariance restricts support to causally-connected $(x, x')$ but does not pick forward over backward.
**(C-3)** **The load-bearing question of the arc.** If P11 carry-through forces forward-cone-only support, V1 is retarded and the kernel-level arrow is FORCED.
**(C-4)** If P11 carry-through fails to fix support and a symmetric or both-cone realisation is structurally admissible, the kernel-level arrow is ADMISSIBLE-not-FORCED.
**(C-5)** This is V1's direct retardation question. N1-E inherits whatever V1 settles.

### 3.3 V1-(c) Causal-cone restriction (the BC3 boundary case)

**(C-1)** A specific candidate: V1 has support on both forward and backward light cones with equal weight, finite primitive-discreteness width on each. Per B.0 §3.3, this is **BC3**, the primary alternative to retardation.
**(C-2)** **Direction-symmetric.** Equal weight on forward and backward cones is time-reversal-invariant.
**(C-3)** N/A — BC3 is the *alternative* to retardation, not a forcing source.
**(C-4)** BC3 is REFUTED if P11 chain bandwidth-update directionality (R1) propagates to V1 construction such that backward-cone support is structurally forbidden. BC3 is ADMISSIBLE if R1 fails to close.
**(C-5)** Whether BC3 survives the audit determines whether V1 retardation is FORCED. This is the central evaluation question of B.2/B.3.

### 3.4 V1-(d) Synge world function ordering (Theorem GR1 carry-over)

**(C-1)** Theorem GR1 (Phase-3) extends V1 to curved spacetime via Synge's world function $\sigma(x, x')$: $K_\mathrm{vac}^\mathrm{curved}(x, x') = K_\mathrm{vac}^\mathrm{prim}(\sigma(x, x') / \ell_\mathrm{ED}^2)$.
**(C-2)** **Direction-ambiguous.** Synge's world function $\sigma(x, x')$ is symmetric in its arguments: $\sigma(x, x') = \sigma(x', x)$. Argument-symmetry of $\sigma$ does not force kernel-symmetry, but the most natural extension preserves $\sigma$-symmetry as a kernel-symmetry property.
**(C-3)** Forces retardation only if the Synge-world-function-based extension is augmented with explicit causal-cone restriction (e.g., $\theta(\Sigma_t \succ \Sigma_{t'})$ for Cauchy surfaces).
**(C-4)** Refutes a flat-space retardation argument only if Phase-3 GR-extension forces full kernel-symmetry; this is unlikely since Phase-3 inherits whatever Arc B settles for the flat-space case.
**(C-5)** Cross-arc relevance to Phase-3. If Arc B closes with FORCED retardation, Phase-3 GR1 extension must preserve retardation in curved spacetime — a substantive consistency check for B.4.

---

## 4. Memory-level candidates (N1-E and cascade)

### 4.1 N1-E-(a) The "memory" reading: past-only by linguistic convention

**(C-1)** N1-E is named *vacuum-induced bandwidth memory*. In dynamical-systems terminology, "memory" means past-only influence: the present state depends on past states but not future.
**(C-2)** **Direction-bearing if the linguistic reading is structurally enforced; direction-ambiguous if it is mere terminology.**
**(C-3)** If the dynamical-systems reading is structurally enforced (i.e., N1-E literally means $K_{N1\text{-}E}$ is a retarded kernel), then directionality is built in by definition.
**(C-4)** Refuted as a *forcing source* if "memory" in N1-E is mere convention imported from dynamical-systems language without structural force. The N.2 derivation (`non_markov_forced.md` §3.5) cascades N1-E from V1; it does not derive N1-E with direction independent of V1.
**(C-5)** This is the central question of §4: does N1-E impose direction on V1, or inherit direction from V1?

### 4.2 N1-E-(b) Cascade-from-V1 reading

**(C-1)** Per `non_markov_forced.md` §3.5, N1-E is FORCED-conditional-on-V1: bandwidth-coupling to the vacuum is structurally inherent to the effective-vacuum framework (Arc Q.8), and the bandwidth-memory kernel inherits its kernel structure from V1.
**(C-2)** **Direction-inheriting from V1.** N1-E carries whatever directionality V1 has.
**(C-3)** If V1 is retarded (per the load-bearing B.2 evaluation), N1-E inherits forward-only kernel support. If V1 is symmetric, N1-E is symmetric.
**(C-4)** N1-E does not refute V1 retardation; it inherits the verdict.
**(C-5)** **This is the structurally honest reading of N1-E.** The "memory" terminology in N1's catalogue label is descriptive, not derivational. Direction is inherited from V1, not imposed.

### 4.3 N1-E-(c) Bandwidth-update-rule reading (P11 carry-through bypass)

**(C-1)** An alternative reading: N1-E direction comes directly from P11+P02+P04 chain bandwidth-update rules (route R1), bypassing V1. The chain's $b^\mathrm{env}$ band is updated forward along $\gamma_K$; the bandwidth-memory kernel reflects forward-only chain history regardless of V1's kernel symmetry.
**(C-2)** **Direction-bearing via P11 carry-through, independent of V1 directionality.**
**(C-3)** Forces N1-E directionality even if V1 is admissibility-symmetric. Could close the cascade arrow at the N1-E level even if V1 itself remains admissibility-ambiguous.
**(C-4)** Refuted if the bandwidth-update rule is itself symmetric (R1 fails). Refuted if N1-E construction structurally requires V1 directionality (i.e., is genuinely cascade-only).
**(C-5)** This is the *alternative* path to a structural arrow if V1 retardation does not close. It would yield a *bandwidth-level* arrow without a kernel-level arrow — a partial-positive verdict for the arc.

### 4.4 N1-E-(d) Cross-cascade consistency (N2-E and N3-D inheritance)

**(C-1)** N2-E (vacuum-modulated commitment memory) and N3-D (vacuum-mediated adjacency memory) cascade from V1 in the same pattern as N1-E. If V1 directionality settles, all three cascade items inherit. If V1 is direction-ambiguous, all three are inherited-ambiguous.
**(C-2)** **Direction-inheriting (downstream).**
**(C-3)** No independent forcing role; cross-checks consistency of the cascade.
**(C-4)** Inconsistency between cascade items would refute the mono-rooted-in-V1 reading. None expected at catalogue level.
**(C-5)** Audit target for B.4 (cross-arc implications). If V1 settles retarded, all cascade items must consistently inherit forward-only structure.

---

## 5. PDE-level candidates

### 5.1 PDE-(a) KG-class second-order structure (free-scalar QFT layer)

**(C-1)** ED's free-scalar QFT layer admits a Klein-Gordon-class equation: second-order in proper time, Lorentz-scalar, no first-order time derivative. The orientation §10 confirms ED admits free-scalar QFT and Dirac at form-level.
**(C-2)** **Direction-symmetric at PDE level.** A second-order linear PDE of KG type is invariant under $t \to -t$ at the level of the equation. Both retarded and advanced and Feynman propagators are admissible Green's functions of a KG-class equation.
**(C-3)** **The PDE itself does not force a kernel arrow.** This is the standard relativistic-QFT consistency point: the equation is time-symmetric; direction enters through propagator boundary conditions, not through the equation.
**(C-4)** Refutes the proposition that PDE-level structure alone picks a direction. Forces the kernel-arrow argument to route through *non-PDE* sources (P11, V1 construction) rather than through the equation.
**(C-5)** PDE structure *propagates* whatever direction is supplied by initial conditions / kernel choice. It does not source direction.

### 5.2 PDE-(b) Dirac-class first-order structure (R.3 layer)

**(C-1)** Theorem R.3 establishes Dirac-equation emergence at form level. Dirac-class equations are *first-order* in time — they have an explicit $\partial_t$ rather than $\partial_t^2$.
**(C-2)** **Direction-ambiguous.** First-order time derivative does not by itself pick forward; the Dirac equation is also time-reversal-invariant under appropriate antiunitary T-transformation. However, Dirac admits forward-only initial-value-problem structure more naturally than KG (forward propagator is first-order-distinguished from advanced).
**(C-3)** Dirac-class structure could be invoked as a *natural* substrate for retardation — but only if augmented by P11 carry-through. The first-order structure does not force direction; it merely *accommodates* it more cleanly than KG.
**(C-4)** Refuted as a *standalone* forcing source: T-symmetry of Dirac is structurally clean and well-established.
**(C-5)** PDE-level structure does not source the arrow. Dirac is auxiliary, not direction-bearing.

### 5.3 PDE-(c) Cl(3,1) spinor-bundle direction (R.2.4 layer)

**(C-1)** Theorem R.2.4 (Cl(3,1) frame uniqueness). The (3,1) signature distinguishes one timelike direction from three spacelike directions, but the timelike-vs-spacelike distinction is a signature property, not a temporal-direction property. Both forward-timelike and backward-timelike are admissible in Cl(3,1).
**(C-2)** **Direction-neutral.** Signature picks timelike/spacelike, not forward/backward.
**(C-3)** No direct forcing role. The (3,1) signature is necessary for the substrate on which retardation could be imposed but does not impose retardation.
**(C-4)** Refuted as a forcing source: signature is even-handed in time-reversal.
**(C-5)** Auxiliary infrastructure only.

### 5.4 PDE-level summary

The canonical ED PDE structure at form level is **time-symmetric** (KG-class second-order, Cl(3,1) signature, Dirac T-symmetric). PDE-level structure *propagates* whatever direction is supplied externally (initial conditions, kernel choice) but does not *source* a direction. **The kernel-arrow argument cannot route through the PDE.** It must route through P11 carry-through (primitive-level) and V1 construction (kernel-level), with PDE structure as the substrate that carries the result without modification.

This is a structurally clean result for the arc: the PDE-level analysis does not produce a forcing source, but it also does not produce a *refuting* source. The arc is free to argue P11→V1 retardation without PDE-level back-pressure, provided the continuum-approximation Feynman propagator remains admissible as effective machinery (the CR constraint).

---

## 6. Cross-interaction map

### 6.1 The flow from primitive to kernel arrow

The catalogue identifies a **single forcing chain** with a **single direction-bearing seed**:

```
P11 commitment-irreversibility (seed, direction-bearing primitively)
        |
        |  carries forward via P02 (chain) + P13 (proper time)
        v
chain-level forward-only bandwidth update (P04 update rule)
        |
        |  Route R1: chain contributions sum into V1 kernel
        |  Route R2: causal-cone restriction (Lorentz covariance C1)
        |  Route R3: UV-FIN + irreversibility joint (Theorem N1)
        v
V1 kernel retardation (LOAD-BEARING question for B.2)
        |
        |  cascade per `non_markov_forced.md` §3.5
        v
N1-E forward-only bandwidth memory
N2-E forward-only commitment memory
N3-D forward-only adjacency memory
V5  forward-only cross-chain correlations
        |
        |  PDE-level (KG / Dirac / Cl(3,1)) propagates without modification
        v
continuum-approximation observable signatures (B.4 cross-arc deliverable)
```

### 6.2 The interaction matrix

| Source | Affects V1? | Affects N1-E? | Affects PDE structure? | Direction-bearing? |
|---|---|---|---|---|
| **P11 irreversibility** | Yes (seed) | Yes (via R1 bypass) | No (PDE is symmetric) | **Yes (primitive)** |
| P02 chain | Yes (R1 conduit) | Yes (R1 conduit) | No | Inherited from P11 |
| P04 bandwidth | Yes (R1 conduit) | Yes (direct) | No | Inherited from P11 |
| P13 proper-time | Yes (parameterisation) | Yes (parameterisation) | No | Inherited from P11 |
| P10 individuation | Indirect (via V5) | No | No | Inherited from P11 |
| P07 rule-type | Indirect (T17 coupling) | Indirect | No | Weakly inherited |
| **V1 kernel retardation** | **Self** | Cascade-imposed | No | **Question of B.2** |
| N1-E "memory" reading | Imposes if structural | Self | No | Linguistic (likely cascade) |
| N1-E bandwidth-update reading | No (independent) | Self | No | Direct from P11 (R1) |
| KG-class PDE structure | Substrate only | Substrate only | Self (symmetric) | No |
| Dirac-class PDE structure | Substrate only | Substrate only | Self (T-symmetric) | No |
| Cl(3,1) signature | Substrate only | Substrate only | Self (signature) | No |
| Synge $\sigma$ (GR1) | Cross-arc check | Cross-arc check | Phase-3 only | Inherited from V1 |

### 6.3 Two structural observations

**Observation 1 — Mono-rooted forcing chain.** Every direction-bearing item in the catalogue routes through P11. The arrow argument has *one seed*, not several converging sources. This is structurally clean (single-point-of-failure analysis is tractable) but also concentrates risk: if P11 carry-through fails, no alternative direction-bearing source exists to close the arc.

**Observation 2 — Two routes to N1-E direction, one route to V1 direction.** N1-E directionality has two paths: cascade-from-V1 (the structurally honest reading per §4.2) and direct-from-P11-via-bandwidth-update-rule (§4.3). V1 directionality has one path only: P11 carry-through to V1 construction. **This means N1-E directionality is more robust than V1 directionality**: even if V1 retardation fails to close at B.2, N1-E directionality may close via the bandwidth-update bypass. Arc B could yield a partial-positive verdict (N1-E forced, V1 ambiguous) as one of the live outcomes.

---

## 7. Catalogue verdict (not the arc verdict)

### 7.1 Multiplicity of candidate sources

**Multiple candidate sources exist** at the primitive (P02, P04, P10, P13 as conduits; P11 as seed), kernel (V1-(b) support structure), memory (N1-E (a)/(b)/(c) readings), and cross-arc (Synge $\sigma$, Theorem 17 rule-type vacuum-coupling) levels. The catalogue is non-trivial in size (11 primitive-level + 4 kernel-level + 4 memory-level + 3 PDE-level = 22 entries plus the cross-interaction map) but structurally concentrated: only one primitive (P11) seeds direction; everything else inherits or carries.

### 7.2 Items already-forced at catalogue level

**One item is already-primitive-given:** P11 commitment-irreversibility (per Arc B opening decision §2.1). This is *primitive-given*, not *theorem-forced*; B.2 inherits it as input.

**No kernel-level or memory-level item is already-forced at the catalogue stage.** V1 retardation, N1-E directionality, and cascade items remain open for B.2 evaluation.

### 7.3 Items already-refuted at catalogue level

**No catalogue item is already-refuted.** Several items are evaluated as *not-direction-bearing* (P01, P03, P06, P09, KG/Dirac/Cl(3,1) PDE structure) but this is a *structural property* rather than a refutation — they do not source the arrow but also do not refute it.

The single boundary case BC3 (symmetric-finite-support kernel) is **not refuted at catalogue level**; its admissibility-or-refutation is the central B.3 question.

### 7.4 Items requiring deeper evaluation

The following catalogue items are flagged as load-bearing for B.2 forced-evaluation:

- **V1-(b) Support structure** (§3.2) — *the* load-bearing question of the arc.
- **V1-(c) BC3 boundary case** (§3.3) — central for B.3 refuted-evaluation.
- **N1-E-(b) Cascade-from-V1 reading** (§4.2) — structurally honest reading; primary cascade route.
- **N1-E-(c) Bandwidth-update-rule reading** (§4.3) — alternative-path candidate for partial-positive verdict.
- **Three carry-through routes (R1/R2/R3)** from B.0 §2.3 — must be evaluated each on its own merits at B.2.
- **Synge $\sigma$ ordering** (§3.4) — cross-arc consistency check for B.4.
- **CR continuum-approximation relativistic consistency** — must be confirmed at B.2/B.4 (Wightman-symmetric continuum coexistence with primitive-level retardation).

The following catalogue items are flagged as **verification-required** before B.2 closes:

- **P05 constitutional content** — catalogued under the functional density/sourcing reading; verify against `ED-primitives` repo.
- **P08 constitutional content** — placeholder; constitutional content unknown at catalogue stage.
- **P12 constitutional content** — placeholder; constitutional content unknown at catalogue stage.

If P05/P08/P12 turn out to carry direction-bearing content, the catalogue mono-rooted-in-P11 finding upgrades to multi-rooted, and the arc structure changes.

### 7.5 BFal-1 (catalogue exhaustion) hooks

Per B.0 §4.3, BFal-1 is the catalogue-exhaustion falsifier: have all plausible asymmetry sources been catalogued? B.1 closes BFal-1 conditionally. The argument for catalogue exhaustion:

(i) Every primitive in the inventory has been audited (P01–P13 at §2; verification flags on P05/P08/P12).
(ii) Every Phase-1/2 theorem layer has been audited at level: PDE-class structure (§5.1–5.3 via R.2.4, R.3, free-scalar layer), kernel structure (§3 via Theorem N1), memory structure (§4 via N1-E cascade).
(iii) The cross-interaction map (§6) confirms the catalogue is closed under interactions: every direction-bearing or direction-inheriting item routes through P11.
(iv) Theorem 17 (gauge-field-as-rule-type) is included via P07 rule-type catalogue entry (§2.7) and carries no direction-bearing content beyond what P07 supplies.
(v) Theorem GR1 Synge $\sigma$ is included as cross-arc consistency check (§3.4).

**BFal-1 is dispatched conditionally on the verification flags closing.** If P05/P08/P12 verification surfaces direction-bearing content, BFal-1 is reopened and the catalogue revised.

---

## 8. Recommended next steps

### 8.1 B.2 forced-evaluation (immediate next memo)

Open `arrow_forced.md`. Evaluate the three carry-through routes (R1/R2/R3) on the FORCED criterion (consistency / necessity / constraint compliance). Headline target: does V1-(b) support structure (§3.2) close as forward-cone-only? Sub-headline targets: do N1-E (§4) and the cascade items inherit consistently?

Expected B.2 outcome shape (per B.0 §5 priors): one of {Theorem 18 FORCED-unconditional via R1 closure, FORCED-conditional-on-P11 via R3, intermediate primitive-level-forced + continuum-approximation-effective per UV-FIN template, ADMISSIBLE-not-FORCED if BC3 survives}.

### 8.2 Verification of P05/P08/P12 constitutional content

**Before B.2 closes**, verify P05, P08, P12 against the `ED-primitives` repo. If any carries direction-bearing content not catalogued in §2, reopen §2 and revise the cross-interaction map (§6). If all three are direction-neutral / direction-inheriting under their actual constitutional content, no catalogue revision needed.

### 8.3 Pre-evaluation refinement of route R1

Route R1 (chain bandwidth-update directionality → V1 construction) is the most plausible direct forcing route. The N.2 §2 derivation does not explicitly construct V1 from chain contributions; it derives V1 via UV-FIN + event-discreteness + Lorentz-scalarity. **B.2 must explicitly construct the chain-contribution sum / integral that produces V1 from the bandwidth-coupling channel** (likely via the effective-vacuum factorisation of Arc Q.8). If this construction admits forward-only chain contributions and no others, R1 closes; if it admits backward-cone contributions, R1 fails.

This is the single most consequential structural step in the arc. Recommend that B.2 begin with this construction.

### 8.4 BC3 audit dispatch order

BC3 (symmetric-finite-support) is the primary alternative to retardation. B.2 evaluates whether retardation is FORCED; B.3 evaluates whether BC3 is REFUTED. The two dispatches are coupled: if R1 closes, BC3 is REFUTED at B.3 by direct contradiction with R1 (forward-only chain contributions structurally forbid backward-cone support). If R1 fails, B.3 must independently evaluate whether BC3 satisfies all primitive-level constraints — and if it does, the arc closes ADMISSIBLE-not-FORCED.

### 8.5 CR continuum-approximation framing draft

B.4 cross-arc implications must explicitly draft the framing for primitive-level retardation coexisting with continuum-approximation Feynman propagators (CR constraint). Recommend that this framing follow the UV-FIN primitive-level / continuum-approximation pattern from Arc Q.8 — primitive-level FORCED structural property, continuum-approximation effective machinery, no contradiction at either level. Begin sketching this framing during B.2 to ensure the FORCED verdict (if reached) is internally consistent at the continuum level.

---

Ready for B.2 — FORCED evaluation.
