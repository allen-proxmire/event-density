# Arc FSC — Memo 0: Opening, Scope, and Load-Bearing Decomposition

**Status:** Opening memo of Arc FSC (Fine-Structure Constant — can the ED substrate produce a dimensionless electromagnetic coupling analogous to $\alpha \approx 1/137$?). Architect-mode active. Form-FORCED / value-INHERITED methodology. No new primitives unless explicitly flagged. Honest-accounting discipline: §7.2 of the position paper currently disclaims coupling-constant derivation; this arc tests whether that disclaimer is *structurally forced* or merely *not-yet-attempted*.

**Date:** 2026-05-25

**Genre note.** This is an **exploratory arc opener**, not a closure document. Unlike Arc Hawking (where Arc BH had already established the substrate mechanism and only the spectrum calculation was open), Arc FSC opens against an explicit position-paper disclaimer (§7.2: "ED does not derive the specific values of fundamental coupling constants"). The opener's job is to determine whether the disclaimer is load-bearing or revisable.

---

## 1. Problem Statement

### 1.1 The question, precisely

> *Does the ED substrate's participation-scattering architecture force a dimensionless cross-chain coupling constant — a substrate-level invariant of the form $\alpha_\mathrm{ED} = f(\text{primitive ratios})$ — that (i) is structurally forced by the 13 primitives, (ii) plays the role of cross-chain interaction strength in the substrate ontology, (iii) maps onto $\alpha$ in the emergent electromagnetic sector via the T17 / DCGT bridge, and (iv) is neither numerology nor parameter fit?*

The four conditions are stated in priority order. (i) is the gate; without structural forcing the result is decoration. (ii) is the substrate-side interpretive anchor — the result must mean something in ED's own language before it can mean something about $\alpha$. (iii) is the bridge requirement — without a T17-grade map from substrate quantity to QED quantity, the result is at best a substrate-internal invariant that happens to be dimensionless. (iv) is the discipline guardrail.

### 1.2 What counts as a legitimate ED-based derivation

A result qualifies as a legitimate substrate-level derivation of an $\alpha$-like constant if and only if **all** of the following hold:

- **L1 (Primitive-anchored).** Every quantity appearing in $\alpha_\mathrm{ED}$ is either a canonical primitive (P01–P13), an explicitly closed-arc result, or a substrate quantity defined by closed-arc machinery (DCGT coarse-graining variables, V1/V5 kernel parameters, T17 rule-type structures, $\Sigma$-landscape extrema).
- **L2 (Form-FORCED).** The functional form $\alpha_\mathrm{ED} = f(\cdot)$ follows from substrate-level argument with no auxiliary numerical input — the *structure* of the combination is forced, even if its *value* is INHERITED from underlying substrate parameters.
- **L3 (Bridge-coherent).** The mapping $\alpha_\mathrm{ED} \leftrightarrow \alpha_\mathrm{QED}$ runs through T17 (gauge-field-as-rule-type, Paper #5) + DCGT (discrete-to-continuum gauge translation, Paper #8) — the same machinery used in the Yang-Mills arc and the substrate-gravity arcs.
- **L4 (Falsifiable).** The result generates at least one falsifier — a substrate-level prediction whose violation by experiment refutes the derivation.

A result is **numerology** if it fails L1 (uses quantities not anchored in primitives), L2 (the form is fitted to recover $\approx 1/137$ rather than forced), L3 (no T17/DCGT bridge), or L4 (no falsifier).

The historical reference class is unforgiving: Eddington's $\alpha^{-1} = 137$ from group-theoretic counting, Wyler's geometric ratios, Beck-Bethe-Riemann hypotheses, and a long literature of post-hoc dimensional combinations all fail L2 (forms chosen after the answer was known). The arc is held to the standard of T19 ($G = c^3\ell_P^2/\hbar$ derived from substrate cumulative-strain reading + holographic counting before the numerical match was computed) and T20 ($a_0 = cH_0/(2\pi)$ derived from dipole-mode azimuthal periodicity before the numerical match was computed). If Arc FSC cannot meet this standard, it should report a structural blockage, not a coincidence.

### 1.3 What the position paper currently says

Position paper §7.2 (`papers/Generative Papers/paper_ED_Framework_13_Primitive_Generative_System.md`):

> *ED does not derive the specific values of fundamental coupling constants ($\alpha$, $\alpha_s$, $g_w$, etc.). The structural existence of $U(1) \times SU(2) \times SU(3)$ admissible-class gauge groups is supported by T17; specific group choice and coupling magnitudes are inherited.*

This disclaimer is the load-bearing target of the arc. The arc tests whether the disclaimer is **structurally forced** (no path exists from the 13 primitives to a substrate-level $\alpha$) or **revisable** (a path exists, was not previously explored, and either yields a derivation or a sharper structural blockage statement than "inherited").

---

## 2. ED Primitives and Dimensionless Groups

### 2.1 Substrate quantities with dimensions

Two enumerations are useful. The **canonical-primitive list** (P01–P13, position-paper §1) is the ontological commitment. The **PDE-level list** ($\rho, v, D, \zeta, \gamma, \alpha_R, \tau, \varepsilon_k$, from canonical-ED PDE notation) is the dynamical-content vocabulary used in NS / Arc D / Arc SG / Arc ED-10. The two are bridged by DCGT (Paper #8): PDE quantities are coarse-grained images of substrate quantities at the hydrodynamic window $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$.

| Symbol | Provenance | Dimension | Source |
|---|---|---|---|
| $c$ | substrate signal speed | $[L T^{-1}]$ | V1 kernel propagation rate (P-RB-1, T18) |
| $\hbar$ | substrate action quantum | $[M L^2 T^{-1}]$ | $\sigma_\tau$ functional + Stone-theorem normalization (Paper #4, Paper #6) |
| $\ell_P = \ell_\mathrm{ED}$ | substrate edge scale | $[L]$ | P08 (Newton-recovery anchor, T19) |
| $G$ | derived gravitational coupling | $[M^{-1} L^3 T^{-2}]$ | $c^3\ell_P^2/\hbar$ (T19); not independent |
| $H_0$ | empirical input | $[T^{-1}]$ | not derived; appears in $a_0$ via T20 |
| $a_0$ | transition acceleration | $[L T^{-2}]$ | $cH_0/(2\pi)$ (T20); not independent of $H_0$ |
| $b_K(u)$ | bandwidth scalar | dimensionless (per channel, per locus) | P04 §1.5 |
| $\pi_K(u)$ | $U(1)$ polarity | dimensionless ($S^1$-valued) | P09 |
| $\Gamma_\mathrm{cross}$ | cross-chain bandwidth | $[T^{-1}]$ | derived (Q-COMPUTE arc, BH-2) |
| $\tau_{V1}$ | V1 kernel width | $[T]$ | $\ell_P/c$ at substrate scale (H-4, T18) |
| $\tau_{V5}$ | V5 cross-chain kernel timescale | $[T]$ | sector-dependent (Maxwell $10^{-3}$ s; Hawking $\ell_P/c$; entanglement window) |
| $\sigma_\tau$ | mass/bandwidth-signature functional | $[M]$ after Born identification | Paper #6 |
| $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$ | stability landscape | dimensionless after normalization | P12 |
| $D_E, D_T$ | participation diffusivities | $[L^2 T^{-1}]$ | DCGT coarse-graining |
| $\zeta$ | coherence/relaxation parameter | $[T]$ or $[T^{-1}]$ (sector-dependent) | DCGT coarse-graining |
| $\rho$ | participation density (PDE-level) | $[L^{-3}]$ after coarse-graining | DCGT |

**Key absence.** There is no substrate primitive corresponding to electric charge $e$, no primitive corresponding to vacuum permittivity $\varepsilon_0$, and no primitive identifying which substrate quantity plays the role of "the quantum of action transferred per emission event in the QED sense." This absence is the structural locus of the FSC question.

### 2.2 The dimensionless combinations the substrate already supports

ED's substrate generates dimensionless ratios from three sources:

**(D-a) Universal substrate ratios.** $c, \hbar, \ell_P$ alone form no nontrivial dimensionless combination — the Planck units exhaust their algebraic content. Adding $H_0$ gives one dimensionless cosmological ratio:
$$\frac{H_0 \ell_P}{c} = \frac{\ell_P}{R_H} \approx 10^{-61}.$$
This is the substrate's only "free" dimensionless number formed from universal scales. It is not $\sim 1/137$ in any obvious way.

**(D-b) Sector-specific kernel ratios.** V5 kernel timescales differ by sector. The ratio $\tau_{V5}^\mathrm{(soft)} / \tau_{V5}^\mathrm{(Hawking)} \sim 10^{41}$ is the cross-scale invariant emphasized in §6.1 of the position paper. Within a sector, $\tau_{V5}/\tau_{V1}$ is a dimensionless characterizer of the kernel hierarchy. None of these are obviously coupling-constant-like.

**(D-c) Participation-flow ratios.** Within a single participation event, the ratio of cross-chain bandwidth transferred to total bandwidth — $\Gamma_\mathrm{cross} \cdot \tau / b_\mathrm{tot}$ for some timescale $\tau$ — is dimensionless. **This is the structural locus where an $\alpha$-like ratio could conceivably live.** It is the substrate-side analogue of "fraction of an interaction's amplitude that crosses between chains per unit substrate time per unit available bandwidth." Whether such a ratio is *forced to take a specific value* by substrate consistency is the load-bearing question of the arc (§3, §4).

**(D-d) Phase-quantization ratios.** P09's $U(1)$ polarity is $S^1$-valued; the substrate has no primitive integer winding number. If a topological invariant of the polarity field emerges from substrate consistency (e.g., a forced winding-number constraint from P11's commitment irreversibility composed with P05's polarity-transport), it would be an integer — which when combined with a kernel-ratio prefactor could produce a dimensionless quantity. **No such forced quantization is currently established.** This is candidate territory (§4.4).

### 2.3 Which combinations could plausibly encode coupling strength

Sorted by structural plausibility (highest first), the candidate substrate-level loci for an $\alpha$-like constant are:

- **C-α.1** Cross-chain bandwidth-fraction at the smallest participation event: $\alpha_\mathrm{ED} \stackrel{?}{=} \Gamma_\mathrm{cross} \cdot \tau_{V1} / b_\mathrm{unit}$ at the substrate's minimum participation transfer. *Plausibility:* high, because this is the substrate-side analog of "coupling per event." *Obstacle:* the value of $\Gamma_\mathrm{cross}$ at the substrate scale is INHERITED, not forced, by any closed arc to date.
- **C-α.2** V1-kernel-overlap integral for cross-channel coupling: $\alpha_\mathrm{ED} \stackrel{?}{=} \int V_1(s) V_1'(s) ds / \mathrm{normalization}$. *Plausibility:* moderate; depends on whether the V1 kernel cross-coupling structure is forced or free.
- **C-α.3** Topological invariant of P09 polarity transport under P11 commitment: integer winding × kernel prefactor. *Plausibility:* moderate; requires establishing the forced winding constraint.
- **C-α.4** $\Sigma$-landscape extremum count: combinatorial substrate invariant from P12 stability landscape, normalized by participation count. *Plausibility:* low — extends Q-COMPUTE multiplicity-counting machinery into a regime not previously explored.
- **C-α.5** RG fixed-point structure at the substrate scale: the 0.6 problem (RG three-regime arc) hinted at substrate-fixed dimensionless quantities; whether $\alpha^{-1} \approx 137$ could be a substrate-RG fixed point is a long-horizon open question. *Plausibility:* low but not zero; couples this arc to `project_ed_rg_three_regime.md`.

C-α.1 is the leading candidate and the focus of §3.

---

## 3. Participation-Scattering Architecture

### 3.1 The substrate's "interaction event"

In QED, an interaction event is the emission or absorption of a photon by a charged particle, with amplitude $\propto e$, probability $\propto e^2 \propto \alpha$. The structural role of $\alpha$ is *the dimensionless probability per natural unit of interaction opportunity that an interaction event occurs*.

In ED, the substrate analog of an interaction event is **cross-chain participation transfer**: two chains share a substrate locus (or adjacent loci), and a finite fraction of one chain's bandwidth in a given channel is transferred to the other chain's participation in that channel. The substrate machinery for this is:

- **P02 (participation as primitive relation)** — chains participate in channels.
- **P05 (polarity-transport along edges)** — substrate-level connection structure for transporting $U(1)$ polarity between adjacent loci.
- **P07 (channel structure as ontological primitive)** — channels are distinguishable carriers; cross-channel transfer is meaningful.
- **P10 (rule-type primitive)** — the substrate supports multiple structurally distinct rule-types; matter-rule-type and gauge-rule-type chains coexist (T17).
- **V1 kernel (Theorem N1 + T18)** — finite-width retarded propagation; sets the spacetime support of "cross-chain influence."
- **V5 kernel (Arc D, Arc Hawking, Arc E)** — cross-chain correlation kernel; sets the timescale of "cross-chain memory."

### 3.2 Where a dimensionless ratio naturally appears

At a single substrate cross-chain participation transfer event, the substrate must specify *what fraction of the available cross-bandwidth flows from chain A to chain B per substrate time-step*. Schematically:
$$\boxed{\;\alpha_\mathrm{ED}^\mathrm{(candidate)} \;\stackrel{?}{=}\; \frac{\Delta b_\mathrm{transfer}}{b_\mathrm{available} \cdot N_\mathrm{steps}}\;}$$
where the right-hand side is evaluated at the substrate's smallest participation-transfer event (a single edge of the participation graph during a single substrate timestep $\tau_{V1} = \ell_P/c$).

The numerator is the substrate's quantum of cross-chain bandwidth transfer. The denominator is the substrate's natural normalization (total available bandwidth × number of substrate timesteps over which the V1 kernel has support). The ratio is dimensionless by construction.

**This is the structural locus where, *if* an $\alpha$-like constant exists in ED, it should live.** §4 develops candidate mechanisms for fixing the ratio's value.

### 3.3 Is the ratio quantized?

Quantization of $\Delta b_\mathrm{transfer}$ would require:

- **Q1.** A substrate-level minimum bandwidth transfer (a "quantum" of cross-chain participation).
- **Q2.** A substrate-level normalization that picks out a unique total bandwidth scale.
- **Q3.** A substrate-level forcing that fixes the ratio Q1/Q2 to a specific value rather than leaving it free.

None of Q1, Q2, Q3 is currently established by any closed arc.

- P04 makes bandwidth a *non-negative additive scalar*, not a quantized scalar; the band-partition (internal / adjacency / environmental / commitment-reserve) is a structural decomposition, not a quantization of total content.
- Q-COMPUTE's $\mathcal{M}_\mathrm{crit}$ (140–250 kDa wall) is a substrate-fixed *threshold*, not a coupling-strength ratio. Its derivation (Arc Q-COMPUTE) does not transfer to the FSC question.
- The Born rule (Paper #2/#14) fixes the *probability law* given participation amplitudes, not the *amplitude magnitude* per cross-chain event.

The honest reading is that **the substrate as currently axiomatized does not force a specific value for the cross-chain participation-transfer fraction**. The fraction is *defined* — it has a structural locus where it would live — but it is not *fixed*.

---

## 4. Candidate Mechanisms for an α-like Constant

Each mechanism is stated with its structural locus, what would need to be established to make it work, and the honest verdict on whether closed-arc machinery supports it.

### 4.1 Participation-strength quantization

**Mechanism.** Argue that the substrate's smallest cross-chain participation transfer is forced to be an integer multiple of a substrate quantum $\Delta b_\mathrm{min}$, with $\Delta b_\mathrm{min}$ determined by substrate consistency (e.g., V1-kernel normalization, P11 commitment-event minimum, P04 four-band-partition saturation).

**What would close it.** A theorem of the form: *"Given P02 + P04 + P05 + P11, the cross-chain participation-transfer per V1-kernel-width is forced to be $\Delta b_\mathrm{min} = f(\text{primitive ratios})$ with no continuous freedom."*

**Verdict.** No such theorem exists. P04's additivity does not force a minimum quantum; P11's irreversibility forces *commitment* to be discrete (a chain commits to a single channel) but does not force *bandwidth* to be quantized. Status: **OPEN, no extant route**.

### 4.2 Cross-chain coupling ratios

**Mechanism.** The coupling between two chains via a shared channel is determined by V1-kernel overlap. The ratio of effective coupling to a natural reference (self-coupling, single-chain V1 norm, V5 cross-correlation amplitude) could be a substrate invariant.

**What would close it.** A substrate-level computation of $\int V_1(x-y) V_1(y-z) d^4y / \|V_1\|^2$ or an analog, with the ratio forced by V1 kernel structure (which is itself derived in N1 and T18) to take a specific dimensionless value.

**Verdict.** Currently the V1 kernel's *form* is FORCED (Gaussian-like retarded support per N1) but its *normalization* is INHERITED (set by substrate scale $\ell_P$ + signal speed $c$ to produce $\hbar$ correctly via Stone-theorem normalization). The overlap integral is dimensionless and computable in principle. Status: **SPECULATIVE-COHERENT, computable**. This is the most concrete candidate for follow-on work.

### 4.3 Memory × speed denominators

**Mechanism.** A combination of the form $X / (\hbar c)$ — generically, "interaction strength per natural quantum of action × speed" — is the QED-template denominator. If a substrate quantity $X$ with dimensions of $[\hbar c]$ emerges from cross-chain machinery, the ratio is automatic.

**What would close it.** Identification of a substrate-derived quantity $X$ (with dimensions $[M L^3 T^{-2}]$ in SI, or equivalently $[\text{energy} \cdot \text{length}]$) whose structural role is "the substrate's quantum of cross-chain interaction amplitude squared, per unit charge squared."

**Verdict.** The honest reading is that this is the route most likely to lapse into numerology if pursued without discipline — it is the dimensional-analysis recipe Eddington / Wyler / Beck-style derivations used. A legitimate ED route requires $X$ to be substrate-derived and identified *before* the numerical match is computed. Status: **NUMEROLOGY RISK** unless tied to 4.2 or 4.4.

### 4.4 Reversible-channel phase factors

**Mechanism.** Compose P09 ($U(1)$ polarity) + P05 (polarity-transport) + P11 (commitment with uniform-$U(1)$ phase-randomization) to produce a topological invariant — a forced winding number, holonomy quantization, or Berry-phase-like substrate invariant — that fixes a coupling ratio.

**What would close it.** A theorem of the form: *"The polarity-transport holonomy around a closed substrate loop, conditioned on at least one P11 commitment event along the loop, is forced to be an integer multiple of $2\pi/N$ for a substrate-fixed integer $N$."* If $N$ is forced and computable, $1/N$ is an $\alpha$-like candidate.

**Verdict.** This is the most ED-native of the candidates. The Berry-phase walkthrough (`walkthroughs/from_primitives_to_berry_phase.md`) and the Aharonov-Bohm walkthrough (`from_primitives_to_aharonov_bohm.md`) establish substrate-level phase-holonomy machinery. They do *not* force a specific quantization integer. Whether they *could* — via composition with P11 commitment events that force topological compatibility conditions — is genuinely open. Status: **SPECULATIVE-COHERENT, ED-native, highest interpretive priority**.

### 4.5 ED-specific invariants

Other ED-specific substrate invariants that could play the coupling role:

- **$\Sigma$-landscape saddle counts.** P12's stability landscape has a saddle structure (Arc-EDSC saddle-classification paper). The combinatorial ratio of saddle types could be a substrate invariant.
- **DCGT coarse-graining anomalies.** The discrete-to-continuum bridge has potential structural anomalies at finite coarse-graining; the anomaly coefficient could be a dimensionless substrate constant.
- **V5 cross-chain "no-go" thresholds.** Cross-chain bandwidth $\Gamma_\mathrm{cross}$ has structural collapse thresholds (BH-2, Q-COMPUTE Class A). The ratio of threshold values across sectors could be invariant.

Each of these is at the boundary of "substrate-derived" and "numerological." None is currently load-bearing.

---

## 5. Structural Obstacles

The honest accounting of what ED lacks:

### 5.1 No explicit charge primitive

ED has no P-numbered primitive corresponding to electric charge. The closest substrate analog is "participation strength in a specific rule-type's channel set" (via T17 + P10), but participation strength is a *bandwidth allocation*, not a quantized topological label. Standard QED has integer charge quantization (Dirac's monopole argument, gauge-invariant of $U(1)$); ED has no analog.

**What would unblock.** Either (a) demonstrate that participation-strength quantization is forced by composition of existing primitives (Mechanism 4.1) — currently no route, or (b) introduce a new primitive: **P14 (charge quantization)** as an additional postulate. Option (b) would be a primitive-set expansion and explicitly violates the "no new primitives" discipline maintained across closed arcs.

### 5.2 No gauge symmetry as substrate primitive

T17 (gauge-field-as-rule-type) establishes gauge structure as *emergent* from P10's rule-type capacity + P09's $U(1)$ polarity + P05's polarity-transport. It does *not* establish gauge symmetry as a substrate-level forced principle. Standard QED uses gauge invariance to constrain coupling structure; ED's substrate-derived gauge structure does not provide the same constraint at the substrate scale.

**Implication.** The Ward-Takahashi-style identities that constrain $\alpha$'s renormalization-group behavior in QED do *not* automatically propagate to substrate-level constraints on $\alpha_\mathrm{ED}$.

### 5.3 The reversible sector and U(1)-like phase

P09's $U(1)$ polarity is $S^1$-valued and *does* support phase structure. The Berry-phase walkthrough and the Aharonov-Bohm walkthrough both establish substrate-level $U(1)$ phase-accumulation. So **the substrate does support a $U(1)$-like phase** — this is not an obstacle.

The obstacle is that phase accumulation along a substrate edge or around a substrate loop produces an *operator-valued* result (a unitary), not a *quantized integer*. Integer quantization requires a topological compatibility condition that the substrate does not currently force.

### 5.4 Participation strength without new axioms

Three composition routes have been examined for forcing participation-strength quantization without new axioms:

- **R-i.** P04 + P11 (bandwidth + commitment). Forces *commitment* discreteness, not bandwidth discreteness.
- **R-ii.** P09 + P05 + P11 (polarity + transport + commitment). Forces phase-randomization on commitment, not amplitude quantization.
- **R-iii.** P12 + Q-COMPUTE multiplicity machinery. Forces system-multiplicity ceilings (Class A wall), not per-event coupling magnitude.

None of the three routes forces participation-strength quantization without an additional axiom.

**This is the load-bearing structural obstacle for Arc FSC.** The four-band partition of bandwidth (P04 §1.5) is a *partition*, not a *quantization*. Quantization in ED appears at the *commitment* level (P11 — chain collapses to a single channel) and at the *multiplicity* level (Q-COMPUTE $\mathcal{M}_\mathrm{crit}$) but not at the *amplitude* level.

---

## 6. Assessment

### 6.1 Verdict on structural viability

**Verdict: (c) blocked-without-new-primitives, with one speculative-coherent sub-route (Mechanism 4.4) and one computable sub-route (Mechanism 4.2) preserved as follow-on items.**

The four-condition test of §1.1:

- **(i) Structurally forced by ED primitives.** *Fails currently.* No closed-arc machinery forces a specific dimensionless cross-chain coupling value. The structural locus exists (§3.2); the forcing does not.
- **(ii) Plays the role of cross-chain interaction strength.** *Locus identified (§3.2), value not fixed.* The substrate-side interpretation is coherent — participation transfer fraction per V1-kernel-width is the natural ED analog of "coupling per event" — but no closed arc fixes its value.
- **(iii) Maps to $\alpha$ in the emergent EM sector.** *Bridge available but unloaded.* T17 + DCGT provides the substrate-to-QED gauge-structure bridge, but the bridge transports *forms* (gauge equations, kernel structure), not *coupling magnitudes*. The Yang-Mills arc (which ran the same bridge) explicitly INHERITED couplings rather than deriving them.
- **(iv) Not numerology.** *Conditional.* If a route closes via Mechanism 4.4 (topological winding from P09 + P05 + P11) or Mechanism 4.2 (V1-kernel overlap integral computed before value-matching), the result would satisfy L1–L4. If a route closes via Mechanism 4.3 (memory × speed denominator) without independent substrate-level identification of the numerator, the result fails L2 and is numerology.

### 6.2 Verdict relative to position-paper §7.2

The position paper's "coupling magnitudes are inherited" disclaimer is **structurally consistent with the current arc's findings** but is **not yet proven to be load-bearing**. Two sub-routes remain unexamined in detail:

- The V1-kernel cross-overlap computation (Mechanism 4.2) is computable from existing closed-arc machinery (N1 V1 kernel form, T18 retardation, DCGT). It has not been performed. Whether it yields a forced dimensionless value or a free parameter is an open question whose answer is bounded.
- The polarity-transport + commitment-event topological winding (Mechanism 4.4) is the most ED-native candidate. It composes existing primitives without adding new ones. Whether the composition forces a specific integer is an open structural question.

If either route closes positively, §7.2 of the position paper would need revision. If both routes close negatively (or if Mechanism 4.4's composition is shown not to force a quantization integer), §7.2 would be *structurally upgraded* from "we do not derive coupling values" to "coupling values are FORCED-INHERITED — the form ED takes makes them not derivable from the 13 primitives without an additional axiom."

The second outcome (structural upgrade to FORCED-INHERITED) is itself a positive arc result, analogous to the Arc Q-COMPUTE finding that the three architectural classes are FORCED-exhaustive even though specific platform $\mathcal{M}_\mathrm{crit}$ values are INHERITED.

### 6.3 What this arc has accomplished as an opener

- Mapped the substrate-level structural locus where an $\alpha$-like quantity would live (§3.2).
- Enumerated five candidate mechanisms with explicit verdicts (§4).
- Identified the load-bearing structural obstacle: P04's bandwidth is partitioned, not quantized (§5.4).
- Reduced the open question from "can ED derive $\alpha$" to two specific computable / structurally-investigable sub-questions (Mechanism 4.2 + Mechanism 4.4).

---

## 7. Next Steps

### 7.1 Sub-arc recommendations, in priority order

**FSC-1 (highest priority): Polarity-Transport Holonomy + Commitment-Forced Quantization.**

Examine whether composition of P09 ($U(1)$ polarity) + P05 (polarity-transport) + P11 (commitment-event with uniform-$U(1)$ phase-randomization) forces a topological compatibility condition that quantizes polarity-transport holonomy around closed substrate loops.

Sub-questions:
- Does a closed substrate loop with at least one P11 commitment event along it support a forced relation between pre-commitment and post-commitment holonomy?
- Is there a substrate-level Dirac-monopole analog: do P05-transport-defects force integer winding when composed with P11?
- Does the Aharonov-Bohm walkthrough's substrate-level account contain unexploited forcing structure for the phase-quantization integer?
- Does the Berry-phase walkthrough's substrate-level account combine with P12 stability-landscape extremum-counting to force a substrate-level integer?

Estimated scope: 4–6 memos. Outcome class: substrate-derived integer (positive) or sharper structural blockage statement (negative-but-informative).

**FSC-2 (second priority): V1-Kernel Cross-Overlap Computation.**

Compute the substrate-level V1-kernel cross-coupling integral $\int V_1(x) V_1(x+\delta) d^4x$ (and analogs for two-channel V1 cross-coupling) under N1's FORCED V1 kernel form, with substrate-level normalization from Stone-theorem $\hbar$-identification. Determine whether the integral yields a forced dimensionless value or a free parameter.

Sub-questions:
- Is the V1 cross-coupling integral dimensionless?
- Does N1's V1 form + T18's retarded support fix the integral value, or does it leave a normalization free?
- If a normalization is free, what would need to fix it (and is that fixing a substrate-derivable result or an additional axiom)?

Estimated scope: 3–4 memos. Outcome class: forced value (positive) or identified free parameter (negative-but-informative).

**FSC-3 (long-horizon): Substrate-RG Fixed Point Structure.**

Couple this arc to `project_ed_rg_three_regime.md` (RG three-regime / 0.6 problem) and examine whether the substrate's RG flow has fixed-point structure that pins coupling values at the substrate scale. This is a long-horizon item; the 0.6 problem's closure left this question untouched.

Estimated scope: 6–10 memos. Outcome class: SPECULATIVE; unknown a priori whether substrate-RG has the structure needed.

### 7.2 Cross-arc connections to monitor

- **T17 (gauge-field-as-rule-type, Paper #5).** Any FSC-1 result will need to bridge through T17 to reach QED.
- **DCGT (Paper #8).** Coupling-magnitude inheritance vs. coupling-form forcing is a DCGT question; the discrete-to-continuum bridge may be where the magnitude information is lost.
- **Q-COMPUTE Mechanism unification.** $\mathcal{M}_\mathrm{crit}$ machinery + $\Gamma_\mathrm{cross}$ thresholds may share machinery with cross-chain coupling magnitude. Worth checking whether the closed-form $\mathcal{M}_\mathrm{crit}$ open item (O-QC-1) and a hypothetical closed-form $\alpha_\mathrm{ED}$ are the *same* substrate-constants problem.
- **Yang-Mills arc.** YM-3 (mass gap from non-Abelian quartic stabilization) inherited coupling values; if FSC-1 yields a substrate-derived $\alpha$, the YM coupling-inheritance question reopens.
- **Berry-phase + Aharonov-Bohm walkthroughs.** Already-closed substrate-level phase-holonomy machinery; first place to look for FSC-1 forcing structure.

### 7.3 Explicit non-goals

- **Not pursued:** Direct numerical fitting of $\alpha^{-1} = 137.036\ldots$ to any substrate-derived combination. Even if a substrate quantity happens to be numerically close, that match is not a derivation.
- **Not pursued:** Group-theoretic counting arguments à la Eddington. Substrate-derived combinatorial structures (e.g., $\Sigma$-saddle counts) are admissible only if their *form* is forced before any value-match is examined.
- **Not pursued:** New primitives (P14 charge quantization, P14 substrate-coupling-fixing axiom, etc.) without explicit acknowledgment that primitive-set expansion violates closed-arc discipline. If a sub-arc determines that a new primitive is required, this is a substantive program-level finding requiring explicit framing — not a quiet axiom-addition.

---

## 8. Inheritance Map

| Inherited Item | Source | What Arc FSC Uses It For |
|---|---|---|
| P02, P04, P05, P07, P09, P10, P11, P12, P13 | Position paper §1 | Substrate-level coupling-locus identification (§3) |
| T17 gauge-field-as-rule-type | Paper #5 / Arc M closure | Bridge target for any FSC-derived substrate coupling → QED $\alpha$ |
| DCGT discrete-to-continuum | Paper #8 / Arc D | Continuum-emergence machinery; potential coupling-magnitude information loss locus |
| V1 kernel finite-width form | Theorem N1 / Paper #18 | FSC-2 cross-overlap computation input |
| V1 retarded support | Theorem T18 / Paper #19 | FSC-2 cross-overlap computation input |
| Berry-phase substrate-level account | `walkthroughs/from_primitives_to_berry_phase.md` | FSC-1 holonomy-machinery input |
| Aharonov-Bohm substrate-level account | `walkthroughs/from_primitives_to_aharonov_bohm.md` | FSC-1 holonomy-machinery input |
| Q-COMPUTE $\mathcal{M}_\mathrm{crit}$ machinery | Arc Q-COMPUTE / Paper #61 | Cross-check for shared substrate-constants problem (§7.2) |
| $\Sigma$-landscape saddle structure | Arc-EDSC saddle papers | FSC mechanism 4.5 candidate input |
| Position paper §7.2 disclaimer | Position paper | Load-bearing target of the arc (§1.3) |

---

## 9. Arc Discipline Statement

Arc FSC is held to the standard of T19 and T20: substrate-level derivation of *form* before any numerical match is examined, and explicit identification of *inherited* vs. *forced* content in every sub-arc.

Specifically:

- No memo in FSC-1, FSC-2, or FSC-3 may quote $1/137$, $137.036$, $\alpha = 1/137.0359990\ldots$, or any other numerical value of $\alpha$ in its derivation sections. Numerical match is checked *only* in the closure-verdict section of each sub-arc.
- No memo may introduce a new primitive (P14, P15, …) without an explicit primitive-introduction section flagged at the top of the memo and a program-level review.
- No memo may use post-hoc dimensional combinations of $c, \hbar, \ell_P, H_0, e, m_e, \ldots$ to recover $\alpha$. All substrate quantities used in derivations must be primitive-anchored per §1.2 L1.
- Negative-but-informative results (sharper statements of structural blockage) are first-class deliverables and should be written up with the same rigor as positive results. Arc closure does not require a positive answer; it requires a verdict.

---

**End of Arc FSC opening memo.**

*Arc FSC's gate condition is FSC-1's verdict. If FSC-1 yields a substrate-derived integer-quantization mechanism (positive), Arc FSC opens to full investigation. If FSC-1 yields a sharper structural blockage statement (negative-but-informative), Arc FSC closes after FSC-2 confirms (or refutes) the V1-kernel-overlap route. If both FSC-1 and FSC-2 close negatively, Arc FSC produces a structural upgrade to position-paper §7.2: from "coupling magnitudes are inherited" to "coupling magnitudes are FORCED-INHERITED — the 13-primitive set as currently axiomatized cannot derive $\alpha$ without an additional axiom, and this is itself a substrate-level structural finding."*
