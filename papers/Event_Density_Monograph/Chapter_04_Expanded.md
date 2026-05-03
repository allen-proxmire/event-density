# Chapter 4 — Kernel-Level Arrow of Time: Theorem N1 + Theorem 18

## 4.1 Chapter Overview

Two foundational theorems together establish the substrate-level arrow of time. **Theorem N1** establishes the V1 vacuum response kernel as finite-width and chain-sourced — a substrate-level temporal smearing kernel that mediates participation events with nonzero substrate-temporal width rather than acting as an instantaneous delta. **Theorem 18** establishes that the V1 kernel is uniquely forced to have forward-cone-only support at the primitive level. The forcing comes from a specific combination of substrate primitives: P11 commitment-irreversibility, P02 chain worldline structure, P04 bandwidth update rule, P13 proper-time ordering, plus Theorem N1 itself. Under this combination, no symmetric, advanced, or hybrid kernel is constructible at the primitive level. The microscopic arrow of time is FORCED structurally rather than postulated.

The chapter develops both theorems in the architectural voice of the monograph: it does not reproduce the formal proofs (those live in the canonical sources), but it exposes the forcing chain explicitly, identifies the structural role each contributing primitive plays, and locates the chapter's content in the program's broader dependency graph. Theorem 18's significance extends beyond its formal statement. It provides the substrate-level structural foundation for upper-half-plane analyticity in standard QFT (which is postulated in conventional treatments rather than derived). It strengthens N1-E directionality via cascade-from-V1 and R1-bypass redundancy, making N1-E *over-determined-forced* rather than merely forced through one channel. It refines T17 vacuum coupling to forward-only directionality. It supplies the kernel-level arrow that Phase-3 GR1 inherits when V1 is extended to curved-spacetime backgrounds. The chapter also clarifies why the kernel-level arrow is the *only* arrow of time the framework currently derives at the substrate level: the thermodynamic, cosmological, measurement, and radiation arrows are downstream structural follow-ons that would inherit Theorem 18 as their kernel-level foundation if pursued.

## 4.2 Why the Kernel-Level Arrow Matters Structurally

### 4.2.1 The arrow of time problem in standard physics

Standard physics distributes the arrow of time across multiple incomplete accounts, each of which passes the explanatory burden to a different layer:

- **The thermodynamic arrow** says entropy increases. This is correct phenomenologically, but standard cosmology then asks why the universe began in a low-entropy state. The answer is "we don't know — it's a boundary condition we accept because it explains everything downstream." The arrow is real, but its origin has been pushed to the universe's beginning where it cannot be examined.
- **The cosmological arrow** says the universe is expanding, and forward in time is the direction in which the cosmos gets bigger. Also correct, but the expansion itself is a cosmic boundary condition rather than a derivation.
- **The measurement arrow** says wavefunction collapse is irreversible. The collapse is a postulate of standard quantum mechanics, not a structural consequence of the rest of the theory.
- **The radiation arrow** says Maxwell's equations are time-symmetric, but only the retarded Green's function is used in practice. The physicists pick the retarded solution because the advanced solution gives anti-causal absurdities. The arrow here is a solution-selection rule applied externally to a time-symmetric equation — it works, but it is a choice rather than a derivation.

Each account is correct as far as it goes. None of them locates the arrow *inside* the laws. Each either passes the buck (to a boundary condition, to a postulate, to a solution-selection rule) or hangs the arrow on something else that is itself unjustified.

### 4.2.2 ED's structural position

The Event Density framework places the arrow of time at the deepest layer the program reaches — the substrate ontology itself, in the form of P11 commitment-irreversibility (Chapter 1, Chapter 2). Every other primitive in the substrate ontology is time-symmetric in isolation; only when joined with P11 does any other substrate quantity acquire forward orientation. The framework's choice is methodologically deliberate: directionality is one structural commitment that has to live somewhere, and the substrate ontology is where it can be most cleanly stated.

P11 alone, however, is not enough. P11 says commitments are irreversible at the chain level — once a substrate event commits at a chain endpoint, the commitment cannot be reversed. This is sharp at the chain level, but it does not by itself establish that the substrate's response kernel (V1) has forward-cone-only support in the spacetime sense. The bridge from chain-time-forward to spacetime-retarded requires the entire combination P11 + P02 + P04 + P13 + N1 + substrate locality. Theorem 18 is the structural theorem that performs this bridge.

### 4.2.3 What the kernel-level arrow is, exactly

The kernel-level arrow of time, formalized in Theorem 18, is the statement that the V1 vacuum response kernel — the substrate-level kernel that mediates how participation events propagate response — has support restricted to the forward causal cone. A perturbation at substrate spacetime point $x$ produces a response only at points in the forward causal cone of $x$, never at points outside it (which would be advanced behavior) and never at all points symmetrically (which would be symmetric behavior).

This is not the same as the thermodynamic arrow (entropy increase), the cosmological arrow (cosmic expansion direction), the measurement arrow (wavefunction collapse), or the radiation arrow (retarded Green's function selection). It is the *substrate-level* arrow at the layer of vacuum response. Standard physics has this at the level of a postulate (the iε prescription, upper-half-plane analyticity, retarded Green's function selection) or as a solution-selection rule applied externally. ED *derives* it.

## 4.3 Theorem N1: The V1 Finite-Width Vacuum Kernel

### 4.3.1 What N1 establishes

Theorem N1 establishes the V1 vacuum response kernel as a finite-width chain-sourced response kernel at the substrate level. The content has three components:

1. **Existence.** V1 exists as a substrate-level vacuum response kernel. It mediates participation events — a perturbation at one chain endpoint produces response at other endpoints through the V1 kernel.
2. **Finite width.** V1 has nonzero temporal width at the substrate scale. It is not an instantaneous delta function. The width is INHERITED — Theorem N1 establishes that the width is finite and substrate-determined, but the specific functional shape of the kernel is not closed-form derived from any other primitive.
3. **Chain-sourced.** V1 is sourced by chain-level participation events. The kernel is not a free-standing vacuum object that exists independently of the chain ensemble; it is constructed from the contributions of chain dynamics. This is the structural content that Theorem 18 will use to propagate P11-irreversibility through the kernel.

### 4.3.2 Why finite-width matters structurally

The finite-width commitment is what makes Theorem N1 a substantive theorem rather than a trivial restatement of the V1 finite-kernel primitive (Chapter 1). In standard QFT, vacuum response kernels are typically treated as continuum objects with effective-theory structure; their finite-width content is implicit in the regularization scale. ED commits to finite-width at the substrate-ontological level, and Theorem N1 formalizes this commitment as a substrate-level theorem.

The finite-width content is load-bearing for several downstream results in the program:

- **Theorem 18 retardation (Section 4.4).** The forward-cone-only support derived in Theorem 18 requires V1's finite width as a structural input. A delta-function kernel would not admit the chain-summed structure that Theorem 18 uses.
- **R1 substrate-cutoff regularization in Navier–Stokes (Chapter 8).** V1's finite width produces, at first subleading order in the DCGT multi-scale expansion, the hyperviscous correction term $-\kappa\mu_\mathrm{V1}\ell_P^2 \nabla^4\mathbf{v}$. This is the R1 mechanism. Without finite-width V1, the substrate-cutoff regularization that supplies the Clay-NS-relevant Intermediate Path C verdict would not exist.
- **Yang–Mills mass-gap mechanism (Chapter 9).** V1's second-moment expansion under DCGT non-Abelian generalization produces the substrate-level mass-gap. The second-moment is well-defined precisely because V1 has finite width.
- **Black-hole area-law motif alphabet (Chapter 13).** V1's per-patch substrate temporal width sets the per-patch motif alphabet $g$ that enters the BH area-law entropy expression $S = (A/\ell_P^2)\log g$.

### 4.3.3 What N1 does *not* establish

Theorem N1 does not establish the specific functional shape of V1. The width is finite and substrate-determined, but the closed-form shape (Boltzmann-like, rational, sigmoid, or some V1-kernel-specific form) is INHERITED. This INHERITED status propagates downstream: every theorem that uses V1's specific shape (R1 cutoff coefficient, YM mass-gap value, BH motif alphabet $g$) inherits the same INHERITED status for its specific numerical content, while the structural form remains FORCED.

Theorem N1 also does not establish forward-cone-only support. Theorem N1 establishes V1's existence, finite width, and chain-sourced character. The forward-cone-only support is the content of Theorem 18, which uses N1 as one input and combines it with primitives P02, P04, P11, P13 plus substrate locality to force retardation.

### 4.3.4 N1-E directionality

N1-E refers to the directionality content of the V1 kernel as established in Theorem N1: that V1 is chain-sourced and that chain dynamics carry an intrinsic ordering through P13 proper-time ordering. N1-E by itself is forward-only along chain proper time. The cross-arc strengthening of N1-E by Theorem 18 elevates this to forward-cone-only support in the spacetime sense, via the combination with P11, P02, P04, and substrate locality.

The strengthening is *over-determined-forced*: N1-E directionality is reachable through two independent paths (cascade-from-V1 and R1-bypass redundancy), so it is forced even in regimes where one of the paths fails. Section 4.6 develops this over-determined-forced status as a structural strengthening of the kernel-level arrow.

## 4.4 Theorem 18: V1 Kernel Retardation

### 4.4.1 The theorem statement

Theorem 18 states: *given the ED primitive set, P11 commitment-irreversibility (taken as primitive), the chain worldline structure (P02), the bandwidth update rule (P04), the proper-time ordering (P13), Theorem N1 (V1 finite-width vacuum kernel), and the effective-vacuum factorisation (Q.8), the V1 vacuum response kernel is uniquely forced at primitive level to have support restricted to the forward causal cone; no symmetric, advanced, or hybrid kernel is constructible at primitive level; the microscopic arrow of time is structurally FORCED at the kernel level; form FORCED (retardation), value INHERITED (specific kernel functional form $G(\sigma)$, continuum-approximation propagator-boundary-condition specifics).*

The theorem's structure has three parts:
1. **Inputs.** A specified subset of the substrate primitives, plus Theorem N1, plus the effective-vacuum factorisation (Q.8) that connects V1 to the chain-contribution sum.
2. **Forcing chain.** A constructive argument showing that the inputs jointly force V1 to have forward-cone-only support.
3. **Refutation sweep.** A demonstration that none of the alternative kernels (symmetric, advanced, hybrid variants) is constructible from the same inputs. This is what makes the theorem *forcing* rather than merely *consistent* — alternatives are not just refuted, they are non-constructible.

### 4.4.2 The forcing chain in one breath

The forcing chain, stated as a single architectural claim:

V1 is a response kernel (Theorem N1 + Q.8) — therefore response kernels need chain-sourced contributions — therefore chain bandwidth dynamics are forward-only along proper time (P11 + P02 + P04 + P13; chain forward-propagator $U_K(n,m) = 0$ for $n < m$) — therefore chain-summed kernel has forward-cone-only support (universal P11 time orientation across the chain ensemble plus substrate locality bridging chain-time-forward to spacetime-retarded) — therefore V1 retarded.

Each step in the chain is structurally non-optional given the inputs. The chain is the program's primary derivation of the kernel-level arrow.

### 4.4.3 The refutation sweep

Theorem 18's refutation sweep dispatches the alternative kernel candidates by *non-construction* rather than by external constraint:

- **Symmetric V1 (BC3).** A symmetric vacuum response kernel would require the chain-summed kernel to have backward-cone support as well as forward-cone. But there are no chain contributions with backward-cone support, because every chain's forward-propagator vanishes for backward chain-proper-time arguments (P11 + P02 + P04 + P13). The chain-summed kernel therefore cannot acquire symmetric content; it has no source. **REFUTED-by-non-construction.**
- **Advanced V1.** An advanced kernel would require everything to run backward — P11 inverted, P13 reversed, P07 vacuous, N1-E cascade conflict. Multiple substrate primitives would have to fail simultaneously. **REFUTED-by-multi-front-contradiction.**
- **Hybrid variants.** Several hybrid candidates were considered: H1 (forward + ε backward), H2 (angular-restricted backward), H3 (weighted symmetric), H4 (symmetric core × envelope). Each requires backward-cone support in some weighting, and each runs into the same non-construction argument as the symmetric kernel. **All REFUTED by the same non-construction structure.**
- **PDE T-symmetry cancellation.** A standard objection is that the underlying continuum PDE (the wave equation, the Schrödinger equation) is time-symmetric, so a symmetric kernel might emerge from the symmetric PDE despite primitive-level asymmetry. This objection is **REFUTED**: the PDE is direction-neutral, but it does not override the kernel-construction selection at the primitive level. The PDE describes solutions; the kernel is a specific construction from the chain ensemble, and the chain ensemble is not direction-neutral.

The refutation sweep's structural significance is that the alternative kernels are not merely inconsistent with observation; they are *non-constructible* from the substrate primitives. There is no weighted average, no perturbative correction, no boundary-condition adjustment that produces them. The forward-cone-only kernel is the only kernel a chain ensemble can produce.

### 4.4.4 The structural status of the result

Theorem 18 belongs to the program's *forced theorems* — results whose conclusions are not chosen but are uniquely produced by the substrate inputs. The forced-theorem inventory at Theorem 18's closure stands at eighteen: T1 through T16 from Phase-1 closure of QM, T17 (gauge-field-as-rule-type), and Theorem 18 itself.

The form-FORCED content of Theorem 18 is the retardation: V1 has forward-cone-only support. The value-INHERITED content includes the specific functional form $G(\sigma)$ of the V1 kernel and the continuum-approximation propagator-boundary-condition specifics that downstream QFT machinery uses. The form is structurally fixed; the values are calibrated empirically or inherit from substrate constants whose closed-form derivation is downstream open work.

## 4.5 Distinguishing Response Kernel from Correlator: The CR Framing

### 4.5.1 The Wightman correlator is a different object

A natural objection to Theorem 18 is that standard QFT contains a manifestly time-symmetric vacuum correlator — the Wightman correlator $W(x,y) = \langle 0 | \hat{\phi}(x) \hat{\phi}(y) | 0 \rangle$. If Theorem 18 forces V1 to be retarded, how can the symmetric Wightman correlator coexist with the framework?

The objection rests on a conflation. The Wightman correlator and the response kernel are *different objects*:

- **The Wightman correlator** measures intrinsic vacuum fluctuations — what the vacuum looks like to itself, in equilibrium, with no perturbation applied.
- **The response kernel** measures something different: how the vacuum *responds* to a perturbation that arrives from somewhere.

Symmetric correlations (in Wightman) and asymmetric responses (in V1) can coexist in the same theory; they are answers to different physical questions. Theorem 18's argument is about the response kernel; the Wightman correlator is unaffected.

### 4.5.2 The continuum-approximation framing

The framework formalizes this distinction as the *CR (continuum-approximation) framing*:

- **Primitive level.** V1 is the substrate-level response kernel, forced by Theorem 18 to have forward-cone-only support.
- **Continuum approximation.** Standard QFT objects (the Feynman propagator $G_F$, the retarded Green's function $G_R$, the advanced Green's function $G_A$, the Wightman correlator $W$) are continuum-level effective machinery, each playing distinct physical roles.
- **Correspondence.** The natural correspondence is primitive-level retarded V1 ↔ continuum-approximation $G_R$. The other continuum objects ($G_F$, $G_A$, $W$) remain admissible at the continuum level as effective machinery for distinct physical roles (time-ordered amplitudes for $G_F$; certain scattering-theory uses for $G_A$; intrinsic vacuum fluctuations for $W$).

Both layers are internally consistent. The primitive level commits to forward-cone-only V1; the continuum level retains the standard menu of effective propagators for the calculations they were always useful for. The CR framing parallels the program's UV-finiteness framing exactly: ED forces a structural property at the primitive level that continuum QFT either postulates or treats as effective-theory machinery.

### 4.5.3 What the CR framing solves

The CR framing solves a potential interpretive tension. Without it, a reader might worry that Theorem 18 is in conflict with the well-established time-symmetric vacuum correlations of standard QFT. With it, the reader understands that Theorem 18 is a primitive-level structural derivation of the *retarded response* content, and that the continuum-level menu of propagators (including the symmetric Wightman correlator) remains intact at the continuum level. The two layers are separately consistent and meet through the standard relationships among continuum propagators.

## 4.6 The Over-Determined-Forced Status of N1-E Directionality

### 4.6.1 Two independent paths

N1-E directionality — the directional structure of the V1 kernel as established in Theorem N1 — is forced through two independent paths in the substrate dependency graph:

- **Cascade-from-V1.** N1-E inherits its forward-only chain-time character from P11 + P02 + P04 + P13 propagated through the chain-summed kernel construction (Theorem 18's primary forcing chain).
- **R1-bypass redundancy.** Even in regimes where the chain-summed-kernel argument is weakened (e.g., extreme coarse-graining, marginal scale separation), N1-E's directional content is reachable through the R1 substrate-cutoff content and its first-subleading-order propagation in DCGT (Chapter 3).

The two paths are independent in the sense that they use different intermediate substrate machinery to reach the same conclusion. Either path alone suffices to force N1-E forward-only directionality; the existence of two paths makes the directionality *over-determined-forced*.

### 4.6.2 Why over-determination is structurally significant

Over-determined-forced status means: the directionality cannot be removed without breaking multiple independent substrate machinery simultaneously. A single missing primitive or a single failed bridge would not eliminate the directionality, because the redundant path remains. This is the structural counterpart of redundancy in error-correcting code: the substrate's directional content is robust against single-channel failure.

The structural significance is that the kernel-level arrow of time is not merely a consequence of one fragile derivation chain. It is over-determined by the substrate's primitive structure, propagated through multiple independent constructions. The framework's commitment to a substrate-level arrow of time is therefore not contingent on any single derivation surviving; it is a substrate-level structural feature reachable through redundant paths.

### 4.6.3 Implications for downstream results

The over-determined-forced status of N1-E feeds into several downstream chapters:

- **Phase-3 GR1 (curved-spacetime extension).** When V1 is extended to curved spacetime via Hadamard-parametrix causal-future restriction with Synge world function, the V1 retarded support is preserved. The over-determined-forced status of N1-E is what makes this preservation robust: even in curved-spacetime regimes where some substrate machinery is more delicate, the directionality survives.
- **T17 vacuum coupling refinement.** T17's clauses C5–C7 are refined to forward-only directionality within sectors, inheriting the kernel-level arrow.
- **Q.5 vacuum-polarisation analytic structure.** Standard QFT's upper-half-plane analyticity for vacuum-polarisation diagrams is *postulated* in conventional treatments; Theorem 18 supplies the substrate-level structural foundation for it. The over-determined-forced status means this foundation is robust.

## 4.7 The Forcing Chain in Detail

### 4.7.1 Step 1: V1 is a response kernel sourced by chains

The first step of the forcing chain establishes that V1 is a response kernel constructed from chain-level contributions. Theorem N1 supplies V1's existence, finite width, and chain-sourced character. The effective-vacuum factorisation (Q.8) supplies the explicit construction of V1 from chain-contribution sums.

The structural content: V1 is not a free-standing vacuum object that exists independently of the chain ensemble. It is the chain-summed kernel produced by aggregating contributions from chain dynamics across the substrate. Whatever V1 does, it does because the chains do it.

### 4.7.2 Step 2: chain forward-propagator vanishes for backward arguments

The second step establishes the chain-level forward-only structure. Each chain has a forward-propagator $U_K(n,m)$ between two chain commitments at chain-proper-time positions $n$ and $m$. The forward-propagator satisfies $U_K(n,m) = 0$ for $n < m$.

The forward-only character has multiple substrate sources:
- **P11 commitment-irreversibility.** Once a chain commits at proper-time position $m$, the commitment cannot affect earlier chain-proper-time positions. There is no commitment-erasing or commitment-undoing dynamics.
- **P02 chain worldline structure.** Chains are coherent worldlines with persistent identity. A chain at chain-proper-time $m$ is structurally connected to its earlier and later chain-proper-time positions through the chain identity.
- **P04 bandwidth update rule.** The chain's bandwidth update at each proper-time step is forward-only — it updates the current chain state from its previous state, not the other way around.
- **P13 proper-time ordering.** Each chain carries an intrinsic proper-time order; this ordering is what makes "earlier" and "later" meaningful at the chain level.

Together, these primitives force $U_K(n,m) = 0$ for $n < m$. There is no chain contribution that propagates a chain commitment backward in chain proper time.

### 4.7.3 Step 3: chain-summed kernel has forward-cone-only support

The third step bridges chain-time-forward to spacetime-retarded. The chain-summed kernel V1 aggregates contributions from all chains in the substrate. Each chain's contribution is forward-only along its own proper time; substrate locality (the commitment that chains couple to neighbors via adjacency, not at arbitrary distance) bridges this chain-time forward-only character to spacetime forward-cone-only support.

Without substrate locality, a chain's forward-time commitments could in principle reach arbitrary spacetime points in the universe's forward time slab, and the chain-summed kernel would be a forward-time-slab object rather than a forward-light-cone object. With substrate locality, the chain's contributions are restricted to the chain's own causal neighborhood, and the chain-summed kernel acquires forward-light-cone-only support.

Universal P11 time orientation across the chain ensemble provides the consistency: every chain in the substrate shares the same forward direction (because every chain is governed by P11), so there are no anti-chains running backward, no chains contributing backward-cone support. The chain-summed kernel therefore has a unique, universal property: response at one spacetime point can only be sourced by perturbations in its causal past.

### 4.7.4 Step 4: alternative kernels are non-constructible

The final step is the refutation sweep: alternative kernels (symmetric, advanced, hybrid) are not just inconsistent with observation; they are *non-constructible* from the substrate inputs. There is no recipe to build them from chain contributions, because the chain contributions do not have the backward-cone content that the alternatives would require.

The non-constructibility is what makes Theorem 18 a forcing theorem rather than merely a consistency theorem. Theorems that simply rule out alternatives by external constraint are weaker; theorems that show alternatives have no construction recipe are stronger. Theorem 18 is in the stronger class.

## 4.8 What Is and Is Not Solved

### 4.8.1 The kernel-level arrow is solved

The kernel-level arrow of time — the directionality of the vacuum response kernel V1 — is FORCED at the substrate level by Theorem 18. This is the cleanest derivation of an arrow of time available within the framework, falling out of theorems already proven (Theorem N1, T17, T18) plus P11 taken as an already-primitive substrate commitment. The kernel-level arrow is therefore solved at the substrate level.

### 4.8.2 The other arrows are out of scope

Four other arrows of time studied in standard physics are explicitly *out of scope* for Theorem 18:

- **The thermodynamic arrow.** Why does entropy increase? The framework's substrate-level analogue — multiplicity (Chapter 2) — provides the substrate-level vocabulary in which the thermodynamic arrow could potentially be derived, but the derivation has not been performed at substrate level. The kernel-level arrow supplies a structural foundation for any future substrate-level thermodynamic-arrow derivation, since multiplicity dynamics under environmental forcing inherit the kernel-level forward-only character.
- **The cosmological arrow.** Why is the universe expanding? The framework treats this as substrate-level open work (Arc COSMO, flagged in Chapter 15). The cosmic horizon enters through T20 (Chapter 11) and Arc ED-10 (Chapter 12), but the cosmological arrow itself — the directionality of cosmic expansion — has not been derived from the substrate.
- **The measurement arrow.** Why is wavefunction collapse irreversible? The Phase-1 closure (Chapter 5) reframes this as the coarse-grained signature of substrate-level commitment events through P11. In this sense the measurement arrow inherits Theorem 18's substrate-level foundation directly: P11's irreversibility, propagated through the kernel-level arrow, supplies the structural origin of measurement irreversibility.
- **The radiation arrow.** Why do we use the retarded Green's function? Theorem 18 supplies the structural answer: the substrate-level kernel V1 is uniquely forced to be retarded, and the continuum-approximation $G_R$ inherits this character. This is the framework's substrate-level resolution of the radiation arrow's standard-physics solution-selection rule.

The kernel-level arrow is therefore the *structural prerequisite* for the other arrows. Each downstream arrow either inherits Theorem 18 as its kernel-level foundation (measurement, radiation) or remains substrate-level open work (thermodynamic, cosmological) that would build on Theorem 18's content if pursued.

### 4.8.3 The structural significance of the kernel-level placement

Standard physics has the radiation arrow at the level of solution selection, the measurement arrow at the level of postulate, the thermodynamic arrow at the level of boundary condition, and the cosmological arrow at the level of empirical observation. None of these is at the level of the laws themselves.

ED places the kernel-level arrow at the level of substrate ontology — at the layer where the framework's laws originate. This is structurally distinct from any of the standard placements. The kernel-level arrow is not a postulate (it is derived from P11 + chain primitives + N1), not a boundary condition (it is a property of the kernel itself, not a constraint imposed on initial data), not a solution-selection rule (it is the unique constructible kernel, not a chosen solution among many), and not an empirical observation (it is a substrate-level structural consequence).

This placement is what the framework's choice to put P11 in the substrate ontology buys. Without P11 at the substrate level, the arrow would have to be placed somewhere else — and it would inherit the same structural weaknesses as the standard placements.

## 4.9 Theorem 18's Cross-Arc Strengthening

### 4.9.1 Strengthening Phase-3 GR1

Phase-3 GR1 is the program's substrate-level theorem on V1's curved-spacetime extension. It establishes that V1 lifts cleanly from flat to curved-background spacetime via Hadamard-parametrix causal-future restriction with the Synge world function. Theorem 18's forward-cone-only support is preserved under this lift; GR-3A geodesic worldlines preserve P11 time orientation along curved geodesics; GR-2D V5 cosmological correlations inherit forward-only structure; GR-4D Λ-integral content is refined to causal-future support.

The strengthening: Theorem 18 supplies the kernel-level arrow at the flat-spacetime level, and Phase-3 GR1 propagates the same arrow to curved-spacetime backgrounds without re-deriving the directionality. Theorem 18 is the structural foundation; GR1 is the curved-spacetime extension that inherits the foundation.

### 4.9.2 Strengthening T17 vacuum coupling

T17 (Chapter 6) establishes gauge fields as participation measures of structural rule-types. Theorem 18 refines T17's vacuum-coupling clauses C5–C7 to forward-only directionality within sectors. The substrate-level kernel-arrow content propagates into T17's vacuum-mediated coupling structure, ensuring that the gauge-field content is not merely time-neutral at the substrate level but inherits the kernel-level arrow.

The strengthening: T17 alone does not force directionality on its vacuum-coupling content; T17 + Theorem 18 jointly do. The cross-arc strengthening makes T17's vacuum coupling a forced-directional structure rather than a postulate-directional structure.

### 4.9.3 Strengthening Q.5 vacuum-polarisation analytic structure

Standard QFT's vacuum-polarisation analytic structure — the upper-half-plane analyticity property of vacuum-polarisation diagrams used in dispersion relations and Kramers-Kronig analyses — is postulated in conventional treatments. Theorem 18 supplies the substrate-level structural foundation: causal-only response (the kernel-level arrow) is the substrate origin of upper-half-plane analyticity at the continuum level. The standard-QFT property inherits a substrate-level structural derivation.

This is one of Theorem 18's most consequential downstream applications. Standard QFT has been using upper-half-plane analyticity as a postulate for decades; ED supplies the structural foundation. The framework does not change any standard-QFT calculation, but it changes the *story underneath* — the analyticity is no longer a postulate floating above the laws, it is the continuum-level reflection of the substrate-level kernel arrow.

### 4.9.4 Strengthening Arc M F-M8 mass-form mediation

Arc M's F-M8 mass-form mediation, which addresses the substrate-level structure of mass content, is refined to forward-only via the V1 vacuum kernel. Theorem 18 supplies the kernel-arrow content that constrains how mass-form mediation propagates through V1.

### 4.9.5 Preservation of direction-neutral substrate

Several substrate-level structures remain direction-neutral or direction-aligned with retarded V1, and Theorem 18 preserves their status:

- **Arc R Cl(3,1) signature.** The substrate-level signature on the spinor bundle remains direction-neutral.
- **R.2.5 spin-statistics.** The substrate-level spin-statistics theorem is preserved.
- **R.3 Dirac equation.** The Dirac equation's substrate-level derivation remains direction-aligned with retarded V1.
- **ED-Phys-10 acoustic-metric guardrails.** The acoustic-metric kinematic-summary content of Chapter 12 inherits Theorem 18's directionality but does not require additional refinement.

## 4.10 Form-FORCED vs Value-INHERITED at the Kernel-Level Arrow

### 4.10.1 What is form-FORCED at this layer

- **V1's existence as a substrate-level vacuum response kernel** (Theorem N1).
- **V1's finite-width character at the substrate scale** (Theorem N1).
- **V1's chain-sourced construction** (Theorem N1 + Q.8 effective-vacuum factorisation).
- **V1's forward-cone-only support** (Theorem 18).
- **The non-constructibility of symmetric, advanced, and hybrid kernel alternatives** (Theorem 18 refutation sweep).
- **The over-determined-forced status of N1-E directionality** (cascade-from-V1 + R1-bypass redundancy).
- **The CR framing distinguishing primitive-level retarded V1 from continuum-level Wightman correlator** (an interpretive/structural framing, but the framing's content — that the two are different objects — is FORCED by the structure of the substrate-to-continuum bridge).

### 4.10.2 What is value-INHERITED at this layer

- **The specific functional shape $G(\sigma)$ of the V1 kernel.** Finite-width is FORCED; closed-form shape is INHERITED.
- **Continuum-approximation propagator-boundary-condition specifics** (the iε prescription's specific small parameter, the contour-deformation conventions in standard QFT). These are continuum-level conventions that inherit consistency with substrate-level V1 retardation but are not closed-form derived from substrate primitives.
- **Specific numerical thresholds** for testing kernel-arrow-discriminating signatures (the energy or length scales at which substrate-level deviations from standard-QFT causal structure could in principle become observable). These would be calibrated against any future near-substrate-scale experiments.

### 4.10.3 What this means for empirical posture

Theorem 18's empirical content is structural-foundational rather than discriminating-from-standard-physics. ED matches standard QFT/QM causal structure at all currently accessible scales. Primitive-level retardation supplies the structural foundation for that causal structure, rather than predicting deviations from it. Discriminating signatures live at near-$\ell_P$ scales (UV-FIN territory; not yet directly probed), where substrate-level structure would in principle manifest.

Specific signature candidates flagged in the canonical sources include: strict causality of vacuum-mediated response near $\ell_P$; Kramers-Kronig-causal-only dispersion structure at near-$\ell_P$ scales (cross-link with UHECR / GRB / GW dispersion / LSS-correlation routes); V5-mediated cosmological-correlation persistence with strict forward-only structure; absence of backward-influence terms in cross-chain correlations; primitive-level account of measurement-collapse arrow consistent with P11; asymmetry in N1-E bandwidth inheritance (decoherence-rate signatures in matter-wave interferometry).

## 4.11 Dependencies

### 4.11.1 Upstream

- **Chapter 1 (substrate primitives).** Especially P11 commitment-irreversibility (the only direction-bearing primitive); P02 chain worldline structure; P04 bandwidth update rule; P13 proper-time ordering; finite-kernel commitment (V1); substrate locality.
- **Chapter 2 (load-bearing invariants).** V1 as load-bearing invariant; gradient sparsity $\sigma$ as the substrate-scale measure entering the cross-bandwidth structure that is mediated by V1 in some downstream applications.
- **Chapter 3 (DCGT as continuum-approximation bridge).** The CR framing that distinguishes primitive-level retarded V1 from continuum-level effective propagators relies on DCGT's substrate-to-continuum bridge to make the two-layer correspondence precise.

### 4.11.2 Downstream

- **Chapter 5 (Phase-1 closure).** The measurement rule emerges from P11 commitment-irreversibility; Theorem 18 supplies the kernel-level structural foundation for the directional content of measurement.
- **Chapter 6 (Form-level QFT).** T17 vacuum coupling is refined to forward-only directionality. Q.5 vacuum-polarisation analytic structure inherits Theorem 18's structural foundation.
- **Chapter 7 (Quantum computing).** UR-1 condition (iii) commitment-injection-bounded inherits P11's irreversibility through Theorem 18's kernel-level arrow. The Poisson-class commitment-event accumulation that defines the third UR-1 condition is the QC-platform-specific reading of the kernel-level arrow.
- **Chapter 8 (Navier–Stokes).** R1 substrate-cutoff regularization arises from V1's finite width; Theorem 18 supplies the directional content of how V1 couples to the dynamics.
- **Chapter 9 (MHD and Yang–Mills).** YM mass-gap mechanism arises from V1's second-moment expansion; the mass-gap inherits V1's directional character.
- **Chapter 10 (Soft-matter mobility).** V5 cross-chain memory under DCGT produces Maxwell viscoelasticity; the directional character of memory is supplied by Theorem 18-class arguments applied to V5.
- **Chapter 11 (Substrate gravity).** Theorem 18's kernel-level arrow lifts to curved-spacetime backgrounds via Phase-3 GR1; substrate-gravity content inherits the directionality.
- **Chapter 12 (Curvature emergence).** Acoustic-metric kinematic content respects ED-Phys-10 guardrails and is consistent with Theorem 18's kernel-arrow structure.
- **Chapter 13 (Black-hole architecture).** BH-4 information-non-paradox uses P11 commitment-irreversibility directly; Theorem 18 supplies the kernel-level structural foundation for the substrate-level information architecture (committed structure cannot un-commit, so it cannot cross a horizon and re-emerge).
- **Chapter 14 (Cross-platform unifications).** The form-FORCED methodology, including the kernel-level arrow as a substrate signature, is a cross-domain consistency check.

## 4.12 Canonical Sources

- `papers/Time_Arrow_Theorem_18/`
- Theorem N1 paper (in V1 vacuum kernel inventory)
- `arcs/arc-B/` (Arc B closure memos: arc_b_scoping, arrow_catalogue, arrow_forced, arrow_refuted, arrow_implications, arc_b_synthesis)

The Time_Arrow_Theorem_18 paper presents Theorem 18 in publication-grade form with the formal forcing chain and the refutation sweep. The Theorem N1 paper presents the V1 finite-width vacuum kernel theorem. The Arc B closure memos in `arcs/arc-B/` contain the six-substage Arc B trajectory (B.0 scoping → B.1 catalogue → B.2 forced-evaluation → B.3 refuted-evaluation → B.4 cross-arc implications → B.5 synthesis) that produced the closure of Theorem 18.

The Monograph Shell's Appendix A theorem provenance map lists Theorem N1 and Theorem 18 with their explicit dependency chains. The Notation Glossary in Appendix B lists V1, V5, P11, P02, P04, P13, and the chain forward-propagator $U_K(n,m)$ used in this chapter.

## 4.13 Optional Figures

**Figure 4.1 — The four standard accounts of the arrow of time and ED's substrate-level placement.** A horizontal arrangement: four boxes labeled "thermodynamic arrow" (boundary condition), "cosmological arrow" (boundary condition), "measurement arrow" (postulate), "radiation arrow" (solution-selection rule), each annotated with where standard physics places the arrow. A fifth box labeled "kernel-level arrow" sits below the four, annotated with "ED substrate ontology — P11 + Theorem N1 + Theorem 18." Arrows from the fifth box upward indicate that the kernel-level arrow can serve as a structural foundation for the four standard accounts. The figure makes visible the structural placement difference between standard physics (arrow distributed across multiple non-fundamental layers) and ED (arrow placed at the substrate layer).

**Figure 4.2 — The Theorem 18 forcing chain.** A vertical flow diagram with five stages: (1) Substrate inputs — P11, P02, P04, P13, Theorem N1, Q.8 effective-vacuum factorisation, substrate locality; (2) Chain forward-propagator $U_K(n,m) = 0$ for $n < m$; (3) Chain-summed kernel construction; (4) Universal P11 time orientation across chain ensemble; (5) V1 forward-cone-only support. Each stage is connected to the next with a labeled arrow indicating the structural step. Side-arrows out of each stage label which alternative kernels are ruled out at that stage (symmetric V1 fails at stage 3; advanced V1 fails at stage 1; hybrid variants fail at stage 3 with the symmetric V1).

**Figure 4.3 — The CR framing.** A two-column figure. Left column ("Primitive level"): substrate ontology, V1 forward-cone-only kernel, Theorem 18. Right column ("Continuum approximation"): standard QFT propagators ($G_R$, $G_F$, $G_A$, Wightman correlator $W$), each with its physical role labeled. A horizontal arrow between the columns labeled "DCGT" indicates the substrate-to-continuum bridge. A specific correspondence arrow labeled "primitive-level retarded V1 ↔ continuum $G_R$" highlights the natural correspondence; the other continuum propagators retain their distinct continuum-level roles. The figure makes visible that the primitive-level result and the continuum-level menu are separately consistent.

**Figure 4.4 — The over-determined-forced status of N1-E directionality.** A diagram with N1-E directionality in a central box, with two independent arrows leading into it from above: the "cascade-from-V1" path on the left, the "R1-bypass redundancy" path on the right. A label on each arrow identifies the substrate machinery that path uses. A note below the central box reads "either path alone suffices; existence of two paths makes directionality robust." The figure makes visible the redundancy structure that makes the kernel-level arrow over-determined.

**Figure 4.5 — Theorem 18's downstream cross-arc strengthening map.** A radial diagram with Theorem 18 at the center and six radial arrows to: (1) Phase-1 measurement rule (Chapter 5); (2) T17 vacuum coupling refinement (Chapter 6); (3) Q.5 upper-half-plane analyticity foundation (Chapter 6); (4) Arc M F-M8 mass-form mediation; (5) Phase-3 GR1 curved-spacetime extension (Chapter 11 background); (6) UR-1 condition (iii) commitment-injection (Chapter 7). Each arrow is labeled with the specific content Theorem 18 supplies to the downstream result.

**Figure 4.6 — The empirical posture of Theorem 18.** A horizontal axis showing length/energy scale, from sub-Planck on the right to macroscopic on the left. A shaded region on the left marks "currently accessible scales," where ED matches standard QFT/QM causal structure exactly. A shaded region on the right marks "near-$\ell_P$ scales," where substrate-level structure could in principle become observable. Arrows in the right region point to specific signature candidates: strict causality of vacuum response near $\ell_P$; Kramers-Kronig-causal-only dispersion structure; V5-mediated cosmological-correlation persistence; absence of backward-influence terms in cross-chain correlations; asymmetry in N1-E bandwidth inheritance (decoherence-rate signatures). The figure makes visible that Theorem 18's empirical content is structural-foundational rather than discriminating at currently-accessible scales.
