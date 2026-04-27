# Arc B Scoping — Time's Arrow from Kernel Asymmetry

**Arc B Stage B.0 — Opening Scoping Memo**
**Status:** Scoping only. Defines the Arc B problem (whether ED's primitive + theorem inventory structurally forces a kernel-level forward arrow of time, given Primitive 11 commitment-irreversibility as already-primitive), enumerates four candidate sources of microscopic asymmetry (S1 commitment-irreversibility carry-through, S2 finite proper-time directionality, S3 V1 vacuum-kernel retardation, S4 N1-E bandwidth-memory directionality), three potential constraints carried over from Phase-2 / Arc N (C1 Lorentz covariance, C2 spin-statistics, C3 UV-FIN), and a five-substage roadmap (B.1 cataloguing → B.2 forced-evaluation → B.3 refuted-evaluation → B.4 cross-arc implications → B.5 synthesis). Scope restricted per opening decision: **kernel-level / microscopic arrow only**; thermodynamic and cosmological arrows out of scope as deferred follow-on work. Primitive 11 irreversibility treated as **already-primitive given**; the arc audits whether that primitive irreversibility propagates as a structurally forced retardation in the V1 vacuum-response kernel and the N1-E vacuum-induced bandwidth memory cascade. Honest framing: the verdict is genuinely open between (a) FORCED retardation as Theorem 18 and (b) ADMISSIBLE-but-not-forced kernel directionality, with intermediate verdicts also live; the V1 derivation in `non_markov_forced.md` §2 fixes the kernel as Lorentz-scalar and finite-width but does not explicitly fix retarded-vs-symmetric, so this question is genuinely open at the close of Arc N.

---

## 1. Purpose of Arc B

### 1.1 The kernel-arrow question

Arc N closed with **V1 (finite-width vacuum memory kernel) FORCED at primitive level by UV-FIN + Primitive 01 + Primitive 13 jointly**, plus four cascading FORCED-conditional items (N1-E vacuum-induced bandwidth memory, N2-E vacuum-modulated commitment memory, N3-D vacuum-mediated adjacency memory, V5 vacuum-induced cross-chain correlations). The N.2 derivation establishes the kernel's *form class* (finite-width, Lorentz-scalar, sub-power-law-2, decaying) but does not explicitly settle one structural feature on which the arrow-of-time question hinges:

**Is the V1 kernel structurally forced to be retarded (forward-acting only), or is it admissible as time-symmetric (forward + backward), or admissible as either?**

The N.2 §2 derivation works at the level of `K_vac(x − x')` as a Lorentz-scalar function of separation. Lorentz-scalarity does not fix evenness: a kernel of the form `θ(t − t') · F(σ(x, x'))` where `F` is Lorentz-scalar and `σ` is the Synge world function is itself Lorentz-scalar restricted to the forward causal structure. The arc has to ask whether the existing N.2 derivation, supplemented by Primitive 11 commitment-irreversibility taken as primitive-given, *forces* the retarded restriction or leaves both retarded and symmetric admissible.

Arc B's purpose is to evaluate this question structurally:

(Q-B) **Does Primitive 11 commitment-irreversibility, taken as primitive-given, propagate to a structurally forced retardation in the V1 vacuum-response kernel and the N1-E vacuum-induced bandwidth memory?**

If yes, the kernel-level arrow of time is FORCED at primitive level — a structural theorem rather than a postulate or boundary condition. If no, the kernel-level arrow is ADMISSIBLE-but-not-FORCED at primitive level, and downstream directionality (in decoherence, dispersion, propagator structure) inherits whatever arrow is supplied by Primitive 11 directly without kernel-level reinforcement.

### 1.2 Three Arc B targets

Arc B investigates three sub-questions:

- **(B-Carry):** Does Primitive 11 commitment-irreversibility *carry through* primitive-level arguments to fix the V1 kernel as retarded?
- **(B-Force):** Does any subset of primitives + Phase-2 theorems + Theorem N1 *force* retardation independently of Primitive 11 (e.g., via UV-FIN or causality), or does the forcing argument require Primitive 11 as a load-bearing input?
- **(B-Refute):** Are there structural constraints (C1 Lorentz covariance, C2 spin-statistics, C3 UV-FIN, or Phase-2 theorems) that *forbid* either the symmetric kernel or the retarded kernel? In particular: does forcing retardation conflict with relativistic-QFT consistency at the continuum-approximation level?

The honest expected verdict — recorded up front per the methodological discipline established in M.0, Q.0, N.0 — is *plausibly forced via Primitive 11 carry-through, but subject to a non-trivial audit of the carry-through argument and of relativistic-consistency back-pressure*. The arc may also produce an intermediate verdict where the kernel is forced retarded *as a primitive-level structure* but the continuum-approximation kernel remains admissible as either retarded or symmetric (this would parallel UV-FIN's "primitive-level forced, continuum-approximation effective" framing in Arc Q.8).

### 1.3 Why Arc B matters

Three reasons motivate Arc B as a substantive arc rather than an addendum to Arc N:

(i) **The arrow of time as a derived theorem rather than a postulate.** Standard derivations of the arrow of time in physics rely on (a) thermodynamic arguments invoking low-entropy initial conditions (Penrose, Boltzmann), (b) cosmological arguments invoking the expansion of the universe, (c) measurement-theoretic arguments invoking irreversible collapse, or (d) external boundary conditions on retarded vs. advanced Green's functions (Wheeler-Feynman, etc.). None of these is a structural theorem at the level of a microscopic kernel derived from a primitive ontology. If Arc B closes with FORCED retardation, ED supplies the cleanest derivation of the kernel-level arrow currently available — it falls out of theorems already proven (Theorem N1) plus a primitive (P11) already constitutional.

(ii) **Cross-arc implications for radiative corrections, propagators, and decoherence.** Whether the V1 kernel is retarded, advanced, or symmetric directly affects the propagator structure used in Arc Q.5 vacuum-polarisation analysis and Arc Q.7 second-quantisation. If retardation is FORCED at primitive level, the Feynman-vs-retarded distinction in continuum QFT acquires a primitive-level substrate; if not, the symmetric Feynman propagator remains the natural continuum-approximation choice without a primitive-level deeper structure. Either verdict is informative.

(iii) **Cleanest possible Theorem-18 candidate for the residual cleanup phase.** Theorem 17 closed Arc Q. Theorems 1–16 closed Phase-1 + Arc R + Arc M (form-level) + Theorem N1 + Theorem GR1. The residual M.1–M.4 cascade is unlikely to yield a substantively new structural theorem (it is mechanical closure). Arc B offers the most plausible next FORCED-theorem candidate before opening genuinely new structural territory (BH interior arc, Hawking spectrum, Why-3+1 PDE-level). If Arc B closes positive, ED's FORCED-theorem inventory advances to 18 with a clean arrow-of-time result.

---

## 2. Background

### 2.1 Primitive 11 commitment-irreversibility — the already-primitive given

Primitive 11 specifies that commitment events along a chain $\gamma_K$ are discrete, ordered, and (per the opening decision for Arc B) **non-reversible**: a committed event is a fact of the chain's past; it does not get un-committed. This is the structural analog of measurement-irreversibility in QM and provides the primitive-level seed of asymmetry from which any arrow-of-time argument in ED must propagate.

Three immediate consequences of Primitive 11 irreversibility taken as given:

(a) **Each chain $\gamma_K$ has an intrinsically directed sequence of commitment events.** The proper-time parameter $\tau_K$ supplied by Primitive 13 inherits this direction: increasing $\tau_K$ corresponds to later commitments, decreasing $\tau_K$ to earlier.

(b) **The chain's bandwidth field $b_K(\tau)$ is updated forward along $\tau_K$ at each commitment event.** The update is non-reversible: bandwidth content acquired at proper time $\tau_K^{(n)}$ is not undone at proper time $\tau_K^{(n+1)}$ unless an explicit forward update produces the reversal.

(c) **The chain's contribution to the effective vacuum at later commitment events depends on its bandwidth content at the time of the contribution.** If bandwidth content is forward-only updated, then a chain's vacuum-side contribution at proper time $\tau$ depends only on its commitment history up to $\tau$, not on its future commitments.

Consequence (c) is the bridge from chain-level Primitive 11 irreversibility to vacuum-kernel-level retardation. The arc's question is whether (c) is structurally forced (i.e., follows from Primitive 11 + V1 alone without auxiliary assumptions) or whether it requires additional inputs (e.g., specific vacuum-coupling structure, specific multi-chain coordination, specific causality assumptions).

### 2.2 Theorem N1 (V1 vacuum kernel) — what it does and does not fix

Theorem N1 (per `non_markov_forced.md` §2) establishes:

- **FIXED:** Vacuum-response kernel `K_vac(x − x')` exists.
- **FIXED:** Kernel is finite-width on the primitive event-discreteness scale $\ell_\mathrm{ED}$.
- **FIXED:** Kernel is Lorentz-scalar.
- **FIXED:** Kernel is decaying with sub-power-law-2 falloff (else UV-FIN violations in continuum approximation).
- **FIXED:** Kernel admissibility class bounded both ways (V1-δ zero-width REFUTED by C3; V1-∞ infinite-width REFUTED by C1+locality).

- **NOT FIXED EXPLICITLY:** Whether the kernel is retarded, advanced, symmetric, or admits both.
- **NOT FIXED EXPLICITLY:** Whether the support of the kernel is restricted to the forward light cone, the closed causal cone, or the full causally-connected region.

The retarded-vs-symmetric question is what Arc B must settle. The Lorentz-scalar property is necessary but not sufficient: $\theta(t - t') \cdot F(\sigma)$ is Lorentz-scalar on the forward light cone with $F$ a Lorentz-scalar function, and so is $F(\sigma)$ unrestricted. Both are Lorentz-scalar; only the second is time-reversal-symmetric.

### 2.3 Three potential carry-through routes from Primitive 11 to V1

Arc B's catalogue stage (B.1) will need to evaluate at least three plausible carry-through arguments from Primitive 11 commitment-irreversibility to V1 retardation:

(R1) **Bandwidth-update directionality.** Each chain's bandwidth field is updated forward along proper time per consequence (c) of §2.1. The chain's contribution to the effective vacuum is therefore forward-history-only. If the V1 kernel is constructed as a sum (or integral) over chain contributions, and each chain's contribution is forward-history-only, then V1 inherits forward-history-only support — i.e., retardation. *Risk:* the construction of V1 from chain contributions is not explicit in `non_markov_forced.md`; the arc may need to refine it or provide it.

(R2) **Causal-cone structure from Primitive 06 + Primitive 13.** If chain worldlines are timelike (Primitive 02 + Primitive 13) and vacuum response propagates within the causal cone (Primitive 06 + Lorentz covariance constraint C1), then the support of $K_\mathrm{vac}(x, x')$ is restricted to causally-connected $(x, x')$. Causal-cone restriction is a weaker condition than forward-light-cone restriction (it admits both forward and backward light cones), so this route alone does not force retardation; it forces *causal* structure but not *temporally-directed* structure. *Risk:* this route may give the weaker verdict that the kernel is causal-symmetric, not retarded.

(R3) **UV-FIN + commitment-irreversibility joint argument.** UV-FIN (Theorem Q.8) bounds the kernel's high-frequency behaviour. Commitment-irreversibility (Primitive 11) bounds the kernel's temporal-direction behaviour. Both bounds together may force the kernel to a unique form-class consistent with both — namely a retarded kernel with finite primitive-discreteness width. *Risk:* this argument may double-count the bound from primitive event-discreteness or may admit a symmetric finite-width kernel that satisfies UV-FIN equally well.

The catalogue stage (B.1) will enumerate these and any additional routes; the forced-evaluation stage (B.2) will evaluate which (if any) close as primitive-level forcing arguments.

### 2.4 Constraints carried over from Arc N

The same three structural constraints used in Arcs Q and N apply to Arc B:

- **C1 (Lorentz covariance):** All structural statements must be Lorentz-covariant; non-covariant claims are refuted.
- **C2 (spin-statistics preservation):** Theorems 1–7 (R.2.5 spin-statistics, R.2.4 Cl(3,1), R.2.3 anyon prohibition, R.3 Dirac, etc.) must remain consistent.
- **C3 (UV-FIN preservation):** All structural statements must be consistent with UV-FIN at primitive level.

Arc B adds one specific carry-over from Phase-2 that becomes load-bearing here:

- **CR (continuum-approximation relativistic consistency):** Whatever primitive-level structural claim Arc B makes about retardation must be consistent with the continuum-approximation level admitting both retarded and Feynman propagators as effective machinery for QFT calculations. ED at primitive level may fix retardation as a structural consequence, while continuum QFT continues to use both as continuum tools — but the primitive-level claim must not contradict standard relativistic field theory's existence as an effective theory. This parallels UV-FIN's framing: primitive-level forced, continuum-approximation effective.

CR is the constraint most likely to pull the verdict toward the intermediate "primitive-level forced, continuum-approximation effective" outcome rather than "fully forced everywhere."

---

## 3. Scope and out-of-scope items

### 3.1 In-scope

Per the opening decision: **kernel-level / microscopic arrow of time only**. Specifically:

- **V1 kernel retardation status** — retarded, advanced, symmetric, or admissible-either-way at primitive level.
- **N1-E vacuum-induced bandwidth memory directionality** — does the cascade structure inherit forward-only direction from V1 + Primitive 11?
- **N2-E vacuum-modulated commitment memory directionality** — same audit.
- **N3-D vacuum-mediated adjacency memory directionality** — same audit.
- **V5 vacuum-induced cross-chain correlation directionality** — does V5 inherit forward-only correlation structure or remain time-symmetric?

### 3.2 Out-of-scope

The following are **deferred to follow-on arcs** and explicitly not in Arc B's scope:

- **Thermodynamic arrow of time (entropy production from kernel structure).** Whether V1 + N1-E memory structure produces a primitive-level structural argument for entropy increase is a separate question, naturally a follow-on Arc B-thermo arc.
- **Cosmological arrow of time (universe expansion direction).** Phase-3 territory; outside Arc B's kernel-level scope.
- **Quantum-measurement arrow (collapse irreversibility).** Already encoded in Primitive 11 commitment-irreversibility; the kernel-level arc audits whether this propagates to V1, but does not re-examine the measurement arrow itself.
- **Radiation arrow (retarded vs. advanced electromagnetic Green's functions).** A specific instance of the kernel arrow, but in continuum approximation rather than at primitive level. Out of scope as an independent question; in scope only insofar as it inherits whatever V1 retardation status Arc B establishes.
- **CPT-theorem-level arguments.** CPT in standard QFT is a continuum-approximation-level theorem; primitive-level arguments do not invoke it. The CR constraint ensures that whatever Arc B concludes at primitive level must remain consistent with CPT at continuum level, but the arc does not derive CPT.
- **Refinement of V1 functional form (V2 exponential vs V3 power-law vs V4 multi-scale).** Arc N flagged these as INHERITED specific forms within the FORCED V1 class. Arc B addresses retardation status, not specific functional form.

### 3.3 Boundary cases

Three boundary cases require explicit clarification of treatment:

**(BC1) The empty-kernel limit.** If the V1 kernel were $K_\mathrm{vac}(x − x') \equiv 0$, retardation status is undefined. Theorem N1 forbids this (V1-δ refutation forces non-zero kernel). Boundary case is empirically empty.

**(BC2) The infinite-support limit.** If the V1 kernel has unbounded support in time, retardation status is meaningful but the kernel violates locality. Theorem N1 forbids this (V1-∞ refutation). Boundary case is empirically empty.

**(BC3) The symmetric-but-finite-support kernel.** A kernel with support on both forward and backward light cones, equal weight on each, with finite primitive-discreteness width on each. This is the *primary alternative* to retardation that Arc B must evaluate. It satisfies all explicit fixes from Theorem N1 (Lorentz-scalar, finite-width, sub-power-law-2 decaying, both-ways-bounded). The arc's main job is to determine whether Primitive 11 carry-through forbids this case.

---

## 4. Arc B methodology

### 4.1 Five-substage roadmap

Following the methodological pattern established in Arcs Q and N:

- **B.1 — Arrow-source catalogue (`arrow_catalogue.md`).** Enumerate candidate sources of microscopic asymmetry in the ED primitive + Phase-1/2 theorem + Theorem N1 inventory. For each: structural content, what would be required to force the kernel arrow, what would refute it. Three classes anticipated: (S1) Primitive 11 carry-through routes (R1, R2, R3 above plus any others uncovered); (S2) UV-FIN / Theorem N1 internal asymmetry sources; (S3) cross-arc constraint-driven asymmetry sources (e.g., spin-statistics requirements, Q.7 canonical-commutation directionality). Aim: 6–12 catalogued candidates.

- **B.2 — Forced-arrow evaluation (`arrow_forced.md`).** Apply the three-condition FORCED criterion (consistency / necessity / constraint compliance C1/C2/C3 + CR) to each catalogued candidate. Headline target: is V1 kernel retardation FORCED at primitive level? Sub-headline: are N1-E, N2-E, N3-D, V5 directionality FORCED-conditional-on-V1 retardation? Anticipated structure: 0–2 unconditionally FORCED items + 0–4 FORCED-conditional items + remainder ADMISSIBLE-NOT-FORCED.

- **B.3 — Refuted-arrow evaluation (`arrow_refuted.md`).** Identify sub-cases of catalogued candidates that violate C1/C2/C3 or CR. Specific concerns: (i) the symmetric-finite-support boundary case BC3 — is it REFUTED by Primitive 11 carry-through, or is it ADMISSIBLE-as-alternative? (ii) advanced-only kernels (kernel restricted to backward light cone) — REFUTED by Primitive 11 directly? (iii) kernels with support outside the closed causal cone — REFUTED by C1.

- **B.4 — Cross-arc implications (`arrow_implications.md`).** What does the Arc B verdict imply for: Arc M (decoherence directionality), Arc Q.5 (vacuum polarisation propagator structure), Arc Q.7 (Feynman-vs-retarded distinction), Arc N cascade items (N1-E/N2-E/N3-D/V5 directionality), Phase-3 (whether the kernel arrow couples to the cosmological arrow)? Explicit identification of any measurable signature distinguishing primitive-level retardation from continuum-approximation Feynman.

- **B.5 — Synthesis (`arc_b_synthesis.md`).** Final theorem statement (FORCED Theorem 18 candidate) or REFUTED / ADMISSIBLE verdict. Hand-off to downstream arcs.

### 4.2 Key methodological commitments

(M1) **Primitive 11 irreversibility taken as primitive-given throughout.** The arc does not re-examine whether Primitive 11 itself contains irreversibility; that is the opening-decision premise. The arc audits whether this primitive-level given propagates structurally to kernel-level retardation.

(M2) **Form-FORCED / value-INHERITED preserved.** The arc may force kernel-retardation as a *form-level* structural feature; it does not aim to fix specific kernel functional forms (V2 vs V3 vs V4) which remain INHERITED per Arc N.

(M3) **Identification-not-derivation discipline preserved (per U3).** If the arc's verdict requires identifying primitive-level retardation with continuum-level retarded-Green's-function structure, the identification proceeds via shared structural infrastructure (e.g., Lorentz-covariant causal-cone restriction); the continuum-level structure is not used as a derivation premise for the primitive-level claim.

(M4) **Acyclicity audit at every substage.** Arc B downstream (e.g., possible thermodynamic-arrow follow-on) cannot feed back into Arc B's own derivation. Arc N (which Arc B extends) cannot be re-derived using Arc B's verdict.

(M5) **Honest verdict spectrum.** The arc commits to the full spectrum of verdicts (FORCED-unconditional, FORCED-conditional-on-Primitive-11, FORCED-conditional-on-additional-input, ADMISSIBLE-not-FORCED, REFUTED-as-stated, intermediate-primitive-level-forced-continuum-approximation-effective). The substage memos do not pre-commit to a verdict before the evaluation is performed.

### 4.3 Falsifier discipline

Per the falsifier-discipline pattern established in Arc N and Arc Q substages, Arc B will track falsifiers explicitly:

- **BFal-1 (catalogue exhaustion):** Have all plausible asymmetry sources been catalogued? (B.1 falsifier; dispatched dark in B.5 by demonstrating that any asymmetry source must factor through one of the catalogued routes.)
- **BFal-2 (carry-through soundness):** Does the Primitive-11-to-V1 carry-through argument require auxiliary assumptions that import the arrow externally? (B.2 falsifier; dispatched dark by isolating the carry-through to primitive-level inputs only.)
- **BFal-3 (relativistic consistency):** Does primitive-level FORCED retardation contradict continuum-approximation relativistic-QFT consistency (CR)? (B.3 falsifier; dispatched dark by exhibiting consistent primitive-level / continuum-approximation framing analogous to UV-FIN.)
- **BFal-4 (BC3 symmetric-finite alternative):** Does the symmetric-finite-support kernel (BC3) genuinely satisfy all primitive-level constraints, making retardation ADMISSIBLE-not-FORCED? (B.3 falsifier; outcome determines whether Arc B closes positive (BFal-4 dispatched dark) or as ADMISSIBLE-not-FORCED (BFal-4 not dispatched).)
- **BFal-5 (cross-arc consistency):** Does the Arc B verdict create back-pressure on Phase-2 closures (Arc M, Arc Q.5, Arc Q.7) that requires re-opening them? (B.4 falsifier; dispatched dark by demonstrating Arc B's verdict refines but does not overturn Phase-2 closures.)
- **BFal-6 (acyclicity):** Does any substage memo use a downstream conclusion as a derivation input? (Audit at every substage; dispatched dark in B.5.)

---

## 5. Honest priors and expected verdict distribution

Per the priors-up-front discipline established in Arc Q.0 and Arc N.0, Arc B's expected verdict distribution at scoping:

- **35% FORCED-unconditional Theorem 18.** V1 retardation forced by Primitive 11 carry-through (route R1 or R3) at primitive level; cascade items N1-E, N2-E, N3-D, V5 inherit FORCED-conditional directionality. Continuum-approximation Feynman propagator preserved as effective machinery via CR. Cleanest outcome; produces the "arrow of time as a derived theorem" headline result.

- **30% FORCED-conditional-on-Primitive-11.** V1 retardation forced *given* Primitive 11 irreversibility, but not derivable from Primitives 01–10, 12, 13 + Theorems 1–17 without Primitive 11 specifically. Methodologically equivalent to Theorem 18 (since Primitive 11 is constitutional and unconditional), but conceptually distinct: the arc would have demonstrated propagation rather than independent derivation.

- **20% intermediate primitive-level-forced / continuum-approximation-effective.** V1 retardation FORCED at primitive level; continuum QFT admits both retarded and Feynman as effective machinery. This is the closest analog of Arc Q.8's UV-FIN framing. Productive outcome; clarifies the structural-vs-effective distinction at the kernel-arrow level.

- **10% ADMISSIBLE-not-FORCED.** BC3 symmetric-finite-support kernel admissible alongside retarded; Primitive 11 carry-through fails to close at primitive level (perhaps requires auxiliary structure not in the inventory). Honest outcome; clarifies the limits of Primitive-11 propagation.

- **5% REFUTED.** V1 retardation directly contradicts a Phase-2 theorem or constraint. Would force re-opening V1's classification; surprising and unlikely.

The distribution is concentrated on the upper-positive quadrant (35% + 30% = 65% in some FORCED-flavour sense), reflecting that Primitive 11 irreversibility is a strong primitive-level seed of asymmetry and that the V1 kernel structure already has a natural retarded extension. The 20% intermediate verdict is the second most likely outcome and would be a productive landing.

---

## 6. Risks and contingencies

### 6.1 Risk: Primitive 11 carry-through requires auxiliary input

**Description.** The cleanest carry-through route (R1 bandwidth-update directionality from §2.3) requires an explicit construction of V1 from chain contributions. `non_markov_forced.md` §2 derives V1 in a different framing (UV-FIN + event-discreteness + Lorentz-scalarity), without an explicit chain-contribution sum. If Arc B cannot reconstruct the chain-contribution argument from primitive-level inputs alone, the carry-through fails.

**Mitigation.** B.1 catalogue stage explicitly evaluates all three carry-through routes and any others. If R1 fails, R2 (causal-cone) and R3 (UV-FIN + irreversibility joint) remain. R2 alone gives the weaker causal-symmetric verdict, which would push the arc toward ADMISSIBLE-not-FORCED. R3 may close even if R1 does not.

**Consequence if unmitigated.** Arc B closes ADMISSIBLE-not-FORCED. Still useful — clarifies the limits of Primitive-11 propagation — but does not produce Theorem 18.

### 6.2 Risk: Lorentz-covariance back-pressure

**Description.** Standard relativistic QFT admits Lorentz-covariant time-symmetric Wightman functions (the symmetric two-point vacuum correlator). If V1's continuum-approximation limit must reproduce the Wightman function structure, then the symmetric kernel is required at continuum level, and primitive-level retardation must be reconciled with continuum-level symmetry.

**Mitigation.** This is the CR constraint. The intermediate verdict (20% in §5) explicitly accommodates this: primitive-level forced retardation can coexist with continuum-approximation symmetric Wightman functions if the symmetric kernel is the time-reversal-symmetric *combination* of forward and backward primitive-level retarded kernels (one for each direction of the time-symmetric chain pair). This requires careful construction at B.4.

**Consequence if unmitigated.** Arc B closes with primitive-level retardation tentatively forced but with unresolved continuum-approximation tension; the verdict is "FORCED-with-CR-caveat" rather than clean FORCED.

### 6.3 Risk: the symmetric-finite alternative (BC3) is genuinely admissible

**Description.** A symmetric finite-support kernel — equal weight on forward and backward light cones, finite primitive-discreteness width on each — satisfies all explicit Theorem N1 fixes. If this case is structurally admissible against all Primitive 11 carry-through arguments, retardation is ADMISSIBLE-not-FORCED.

**Mitigation.** B.3 refuted-evaluation specifically targets BC3. If Primitive 11 chain bandwidth-update directionality (consequence (c) of §2.1) genuinely propagates to kernel construction (route R1), then BC3 is REFUTED because the chain contributions to V1 are forward-history-only and cannot produce a backward-light-cone term. If R1 fails, BC3 may be ADMISSIBLE.

**Consequence if unmitigated.** Arc B closes ADMISSIBLE-not-FORCED on the kernel arrow specifically; downstream cascade directionality (N1-E etc.) still inherits Primitive-11 directionality but at the chain level rather than the kernel level.

### 6.4 Risk: scope creep into thermodynamic / cosmological arrows

**Description.** During cross-arc implications (B.4), a clean Arc B result on kernel retardation may produce immediate structural implications for entropy production or cosmological-arrow directionality, tempting an in-scope expansion that the opening decision excludes.

**Mitigation.** Strict adherence to the opening-decision scope restriction. B.4 may *flag* downstream implications as candidates for follow-on arcs but must not derive them.

**Consequence if unmitigated.** Arc B grows beyond its closure target and may not close in the planned six-memo scope.

---

## 7. Hand-off to B.1

### 7.1 B.1 deliverable

`arrow_catalogue.md` enumerates candidate sources of microscopic asymmetry in ED's inventory. For each candidate:

- **Identifier and short description.**
- **Primitive / theorem dependencies** (which primitives + theorems must hold for this candidate to operate).
- **Forcing role:** does this candidate, if FORCED, produce kernel-level retardation directly, or does it produce a precondition for retardation?
- **Anticipated FORCED status** (for B.2 evaluation): plausibly forced / plausibly admissible-not-forced / plausibly refuted.
- **Constraint sensitivities:** which of C1/C2/C3/CR are load-bearing.

B.1 should yield 6–12 catalogued candidates. The R1/R2/R3 routes from §2.3 will be among them but not exhaustive — the catalogue stage may surface additional asymmetry sources (e.g., spin-statistics-driven asymmetry, Q.7-derived canonical-commutation directionality, GR1-derived Synge-world-function ordering).

### 7.2 B.1 success criterion

B.1 closes when the catalogue is judged exhaustive: any plausible asymmetry source factors through one of the catalogued candidates. BFal-1 dispatched dark when this judgment is supported by argument.

### 7.3 Carry-forward state from B.0

The following Arc B-state items must persist forward to B.1 and beyond:

- **Primitive 11 irreversibility = primitive-given.** Not re-examined in arc.
- **Scope = kernel-level / microscopic arrow only.** Thermodynamic / cosmological / radiation / measurement arrows out of scope.
- **Constraints = C1, C2, C3, CR.** Same as Arc N + CR continuum-approximation relativistic consistency.
- **Boundary cases = BC1 empty, BC2 infinite-support, BC3 symmetric-finite.** BC3 is the primary alternative to retardation.
- **Five-substage roadmap = B.1 catalogue → B.2 forced → B.3 refuted → B.4 implications → B.5 synthesis.**

---

## 8. Cross-references

- Arc N opening: [`arc_n_scoping.md`](../arc-N/arc_n_scoping.md) (N.0 — methodological template).
- Arc N forced evaluation: [`non_markov_forced.md`](../arc-N/non_markov_forced.md) (N.2 — V1 derivation; this is the load-bearing input to Arc B).
- Arc N synthesis: [`arc_n_synthesis.md`](../arc-N/arc_n_synthesis.md) (N.5 — Theorem N1 final statement).
- Arc Q.7 second quantisation: provides Feynman-vs-retarded propagator structure context for B.4.
- Arc Q.8 vacuum and zero-point: provides UV-FIN as primitive-level / continuum-approximation framing template for B.2/B.4.
- Phase-3 GR1 (Theorem GR1): provides Synge world function structure as candidate asymmetry source (catalogue stage B.1).
- Downstream arc memos: `arrow_catalogue.md` (B.1), `arrow_forced.md` (B.2), `arrow_refuted.md` (B.3), `arrow_implications.md` (B.4), `arc_b_synthesis.md` (B.5).

---

## 9. One-line summary

**Arc B scopes a kernel-level arrow-of-time arc taking Primitive 11 commitment-irreversibility as already-primitive-given and Theorem N1 V1 finite-width vacuum kernel as load-bearing input, with the central question whether Primitive 11 irreversibility carries through structurally to force the V1 kernel as retarded (forward-acting) at primitive level — a question that Theorem N1 does not explicitly settle since its derivation fixes the kernel as Lorentz-scalar / finite-width / decaying / sub-power-law-2 but not retarded-vs-symmetric — with three candidate carry-through routes (R1 chain bandwidth-update directionality, R2 causal-cone restriction from Lorentz covariance, R3 UV-FIN + irreversibility joint argument) to be evaluated in the catalogue stage B.1; expected verdict distribution 35% FORCED-unconditional Theorem 18 / 30% FORCED-conditional-on-Primitive-11 / 20% intermediate primitive-level-forced + continuum-approximation-effective per UV-FIN template / 10% ADMISSIBLE-not-FORCED if BC3 symmetric-finite-support alternative survives Primitive 11 audit / 5% REFUTED; constraints C1 Lorentz covariance + C2 spin-statistics + C3 UV-FIN + new CR continuum-approximation relativistic consistency; scope strictly kernel-level with thermodynamic / cosmological / radiation / measurement arrows deferred to follow-on arcs; methodology preserves form-FORCED/value-INHERITED + identification-not-derivation + acyclicity disciplines from Arcs Q and N; six falsifiers BFal-1 through BFal-6 tracked across substages; B.1 deliverable is `arrow_catalogue.md` enumerating 6–12 candidate asymmetry sources with Primitive / theorem dependencies and anticipated FORCED status, success criterion catalogue exhaustion judgment with BFal-1 dispatched dark.**
