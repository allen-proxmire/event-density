# Arc FSC — Memo 3: Substrate RG and Universality of Coupling Magnitudes

**Status:** First load-bearing memo of Arc FSC sub-arc FSC-3 (long-horizon). Single-question memo: does ED's coarse-grained dynamics (DCGT + Wilsonian substrate-RG + Stone-normalized memory + commitment/saturation constraints) admit RG-like flow that drives coupling magnitudes toward universal fixed points, independent of substrate-microscopic-connectivity freedom (FSC-2.1's blocker)? Architect-mode active. No new primitives. Discipline reminder (FSC-0 §9): no quoting of $1/137$ or $\alpha = 1/137.036\ldots$; numerical-match checks reserved for sub-arc closure.

**Date:** 2026-05-25

**Prior context.** FSC-1 (Memo 1) closed negatively (P09 $U(1)$-continuity blocks topological-winding quantization — *structural impossibility*). FSC-2 (Memo 1) closed negatively (V1 cross-overlap is FORCED-FORM-INHERITED-VALUE due to substrate-microscopic-connectivity underdetermination — *structural underdetermination*). FSC-3 was preserved by FSC-0 §7.1 as a long-horizon item that does *not* depend on FSC-1 or FSC-2 mechanisms: an IR-attractive fixed point of substrate-RG flow could in principle wash out the microscopic shape freedom that blocks FSC-2.

This memo opens FSC-3 and produces a preliminary structural verdict. It does *not* close the sub-arc — closure would require explicit substrate-RG flow computation in a specific operator basis, of the kind already performed for the 0.6-problem arc but applied to coupling-magnitude operators rather than to PDE-coefficient operators.

---

## 1. Restating the FSC-3 Question

### 1.1 The substrate-vs.-emergent distinction

FSC-1 and FSC-2 both addressed *substrate-level* forcing: does the 13-primitive set, applied at substrate scale $\ell_P$, force a specific dimensionless coupling value? Both answered no — for structurally different reasons. The FSC-3 question is whether the *coarse-grained, emergent-scale* dynamics can do what the substrate-scale primitives cannot:

> *Does the DCGT-mediated flow of coupling-like substrate observables, as they are integrated over scales $\ell_P \ll k^{-1} \ll L_\mathrm{flow}$, possess an IR-attractive fixed-point structure that produces a unique dimensionless coupling value $\alpha_\mathrm{ED}^{(*)}$ at all sufficiently long-wavelength emergent scales, independent of the substrate-microscopic V1 spectral shape (the FSC-2.1 inherited parameter)?*

The substrate-vs.-emergent distinction is essential. Examples from physics:

- **Critical exponents.** Universal at IR fixed points: $\nu, \eta, \alpha, \beta, \gamma, \delta$ in Ising-class systems take values independent of microscopic details (lattice type, coupling form). The microscopic theory has many parameters; the IR fixed-point theory has just the universality-class label.
- **Coupling constants in standard QFT.** *Not* universal in the critical-exponent sense. $\alpha_\mathrm{em}(\mu)$ at a given renormalization scale $\mu$ depends on UV initial data; multiple microscopic UV theories give multiple IR values. The renormalization-group is *running*, not flowing to a single fixed point that determines the value.
- **Asymptotic safety scenarios.** A subset of theories postulates that *all* couplings flow to a unique nontrivial UV fixed point with a finite number of relevant deformations, which would make IR values predictable from substrate structure plus a finite number of measurable inputs. Not yet established to work for the Standard Model.

FSC-3 asks whether ED falls into the third category. The answer determines whether the FSC-2.1 substrate-microscopic-connectivity freedom is *erased* at emergent scales (FSC-3 viable) or *propagated* to emergent scales (FSC-3 blocked).

### 1.2 What "forced at the emergent level" would mean

A FSC-3-positive outcome would have the structure:

> The substrate-RG flow on the dimensionless coupling-like observable $g(k)$ — derived from V1-cross-overlap at scale $k^{-1}$ via DCGT-mediated coarse-graining — has an IR-attractive fixed point $g^{(*)}$ such that for all initial conditions $g(\Lambda_\mathrm{UV} = 1/\ell_P) = g_0$ in some basin of attraction, $g(k) \to g^{(*)}$ as $k \to 0$. The fixed-point value $g^{(*)}$ is determined entirely by the substrate-RG flow operator, which is FORCED by P01–P13, and is independent of $g_0$ (and therefore independent of V1 spectral shape).

This would be a substantive program-level result: it would *unblock* FSC-2.1 at the emergent scale even though the substrate-level blockage stands. The structural analog is asymptotic freedom in QCD, where the IR coupling at low energies is determined by the structure of the RG flow (specifically, the position of $\Lambda_\mathrm{QCD}$ relative to the asymptotic-freedom scale), with universal IR behavior despite UV initial-condition freedom.

A FSC-3-negative outcome would have one of two structures:

- **No fixed-point structure.** The substrate-RG flow on $g(k)$ has no IR-attractive fixed point. The IR value of $g$ depends on the UV initial condition (V1 spectral shape) without erasure.
- **Multiple basins / unstable fixed points.** The substrate-RG flow has fixed-point structure, but the basins of attraction are sensitive to UV initial conditions, so the FSC-2.1 freedom does not wash out.

A FSC-3-ambiguous outcome (most likely for an opening memo) would be: structural argument insufficient to settle; explicit flow-equation computation required.

---

## 2. ED Structures That Could Support an RG-Like Flow

The closed-arc inventory provides four structural inputs for a substrate-RG analysis. None of them is new; all are inherited.

### 2.1 DCGT (Diffusion Coarse-Graining Theorem)

Arc D / Paper #73 establishes the substrate-to-continuum bridge under the hydrodynamic window
$$\ell_P \;\ll\; R_\mathrm{cg} \;\ll\; L_\mathrm{flow}.$$
Coarse-graining at scale $R_\mathrm{cg}$ produces effective continuum equations from substrate microscopic dynamics. The Krieger-Dougherty viscosity, the Maxwell viscoelastic ansatz, the V1 → R1 transition, and the T17 minimal-coupling Lorentz structure all emerge from DCGT.

DCGT *is* the substrate-RG block-averaging step in continuum dress: it removes degrees of freedom below scale $R_\mathrm{cg}$ and produces effective constitutive content at scale $R_\mathrm{cg}$. The substrate-RG flow is the family of effective theories obtained by varying $R_\mathrm{cg}$ across the hydrodynamic window.

### 2.2 Wilsonian RG on canonical ED PDE (closed Arc RG, three-regime)

The arc-RG closure (`arcs/arc-RG/ED_RG_Flow_Analysis.md`, seventh pass, 2026-04-22) computed explicit Wilsonian RG flow on the canonical ED PDE
$$\partial_t \delta = D\,F[\delta] + Hv, \qquad \tau\dot v = F[\delta] - \zeta v, \qquad D + H = 1,$$
with operator basis $\{O_0, O_2, O_{3,0}, O_{1,2}, O_{2,2}, O_4, O_v, O_{v,t}, O_{\delta v}\}$ and Z₂ symmetry $(\delta, v) \to (-\delta, -v)$. The arc produced:

- **A three-regime structure**: substrate regime $k \sim 1/\ell_P$, intermediate regime, continuum hydrodynamic regime $k \ll 1/L_\mathrm{flow}$.
- **Specific dimensionless invariants** appearing across regimes (including the "0.6" universal ratio that fixed the second-pass discrepancy in canonical-ED PDE coefficients).
- **Operator-scaling-dimension assignments** and identification of which operators are RG-relevant vs.-irrelevant at the canonical fixed point.

**This is the closed-arc evidence that ED's substrate-RG can produce universal dimensionless quantities.** The 0.6 ratio is a substrate-RG universal: it does not depend on substrate-microscopic shape parameters; it emerges from the structure of the flow itself.

The FSC-3 question is whether the same machinery, extended to *coupling-magnitude* operators (rather than PDE-coefficient operators), produces analogous universals.

### 2.3 Stone-normalized memory bandwidth

The Stone-theorem $\hbar$-normalization (Papers #4, #13) and the V5 memory-kernel cascade (Arc Hawking H-4, Arc D V5 derivations) provide additional structural anchors at the substrate-RG level. Specifically:

- The $\int V_1\, d^4x = c\ell_P \mathcal{N}_*$ Stone-normalization (FSC-2 §2.3) is a *substrate-RG invariant*: it must hold at every coarse-graining scale, not just at substrate scale.
- The V5 kernel timescale $\tau_{V5}$ is sector-dependent at the substrate level (Maxwell $\sim 10^{-3}$ s, Hawking $\sim 10^{-44}$ s, entanglement-window varying) but obeys a *substrate-RG invariant scaling relation* — the same V5 primitive doing structurally identical jobs at 40 orders of magnitude is *itself* evidence of a substrate-RG fixed-point structure for V5-kernel emergence.

V5's cross-scale unification is, in substrate-RG language, the *strongest extant evidence* that some ED quantities are universal across the hydrodynamic-window-and-beyond scales. The question for FSC-3 is whether this universality extends to coupling-magnitude observables.

### 2.4 Saturation and horizon constraints

Two additional substrate-RG anchors:

- **Decoupling-surface saturation (Arc BH, BH-2).** At horizons, cross-chain bandwidth $\Gamma_\mathrm{cross}$ saturates at substrate-level thresholds. This produces sharp endpoints in the substrate-RG flow that act as boundary conditions on certain coupling-like ratios.
- **Multiplicity-cap function $M$ (Arc Q-COMPUTE).** The Q-COMPUTE arc established that $M_A, M_B, M_C$ projections are FORCED-exhaustive at the architectural level; the substrate-RG flow on $M$-type observables has structural endpoints at the architectural-class transitions. This is suggestive (though not directly applicable) of fixed-point structure for participation-strength-like observables.

These are inheritance items, not load-bearing inputs to this memo. They are listed for cross-arc coherence.

---

## 3. Degrees of Freedom That Vary Under Coarse-Graining

For the substrate-RG question to have a definite answer, we must identify which substrate-microscopic degrees of freedom enter the flow.

### 3.1 V1 spectral shape

The FSC-2.1 load-bearing freedom: $V_1$'s dimensionless spectral profile (Gaussian-class vs. Lorentzian-class vs. Bessel-class) at substrate scale $\ell_P$, parametrized by shape parameters $\{s_i\}$ that depend on substrate-microscopic adjacency / connectivity. Under coarse-graining, the effective $V_1^{(k)}$ at scale $k^{-1} > \ell_P$ has a renormalized spectral shape $\{s_i^{(k)}\}$ that flows from the substrate-scale value as $k \to 0$.

**Key question for FSC-3:** does $\{s_i^{(k)}\}$ flow to a $k$-independent fixed point $\{s_i^{(*)}\}$ as $k \to 0$, independent of the initial $\{s_i\}$?

If yes (universal IR shape), then the FSC-2.1 freedom washes out at emergent scales and $I(0)^{(k)} \to I(0)^{(*)}$ is a universal substrate-derived value. If no, the FSC-2.1 freedom propagates.

The standard QFT analog suggests "no" generically: kernel shapes are sensitive to UV details and do not generically flow to fixed-point shapes. The asymptotic-safety analog suggests "yes" in special structurally-constrained theories.

### 3.2 Local connectivity

The substrate-microscopic adjacency structure (cubic / BCC / random-graph / foam, FSC-2 §2.4) varies in the substrate-microscopic dataspace. Under coarse-graining, the effective adjacency structure at scale $R_\mathrm{cg}$ is *averaged out* in continuum DCGT — the continuum hydrodynamic equations do not depend on lattice type (this is the standard hydrodynamic-emergence universality and is essentially the content of Arc D / DCGT).

So local connectivity *does* wash out under DCGT coarse-graining at continuum hydrodynamic scales. This is the *positive* part of substrate-RG universality in ED: lattice type does not survive coarse-graining; effective theories do not distinguish cubic from BCC.

However, this universality is about *continuum form* of the equations, not about *coefficient values*. The continuum Krieger-Dougherty viscosity has universal form but its coefficient INHERITS substrate-microscopic details. The FSC-3 question is whether coefficient values also flow to fixed-point universal values, which is a stronger claim than DCGT establishes.

### 3.3 Participation-strength distributions

Participation strength $b_K(u)$ at substrate scale has some distribution across (channels, loci). Under coarse-graining, this distribution evolves. Candidate fixed points:

- **Maximum-entropy fixed point.** $b_K$ distributed uniformly across channels at each locus, subject to total-bandwidth constraint. This would be the analog of the "infinite-temperature" fixed point in lattice models — typically IR-attractive in many cases.
- **Stability-landscape extremum.** $b_K$ concentrated on substrate-channel configurations that extremize the $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$ landscape (P12).
- **Q-COMPUTE Class-A wall.** Multiplicity saturation acting as a fixed-point endpoint for participation-density observables.

Each of these is a candidate attractor, but none has been computed as an IR-attractive fixed point of an explicit substrate-RG flow equation.

### 3.4 Memory-bandwidth allocation

The four-band partition of bandwidth (P04 §1.5: internal / adjacency / environmental / commitment-reserve) is a substrate-level structural decomposition. Under coarse-graining, the *partition* survives (it is a P04 substrate primitive); the *allocation ratios* between bands may flow.

If allocation ratios flow to fixed points, they would be substrate-RG-universal dimensionless quantities. Their relationship (if any) to QED-sector coupling magnitudes would require a T17 + DCGT bridge analysis. This is structurally distinct from the V1-shape-flow question of §3.1.

---

## 4. Does Coarse-Graining Suppress Microscopic Shape-Dependence?

### 4.1 What washes out (positive evidence)

The following microscopic features *do* wash out under DCGT coarse-graining, by closed-arc evidence:

- **Lattice type.** Cubic vs. BCC vs. random-graph all produce the same continuum Krieger-Dougherty viscosity *form* (Arc D); only the *coefficient* differs.
- **Sub-substrate-scale features.** Anything at scales $\ll \ell_P$ is integrated out structurally; only $\ell_P$-scale and longer-scale features survive at hydrodynamic-window scales.
- **Discrete-event temporal microstructure.** P13 event-discreteness at substrate timestep washes out into continuous time at hydrodynamic-window scales.
- **Phase-randomization microevents.** P11 commitment-microstructure washes out into continuum decoherence rates at hydrodynamic-window scales.

This is the standard DCGT result and is substantively confirmed by Arc D + Arc RG closures.

### 4.2 What does NOT wash out (negative evidence)

- **Continuum coefficient values.** Krieger-Dougherty's coefficient, the Maxwell viscoelastic ratio, the canonical-ED PDE coefficients $D, H, \tau, \zeta, M_0, P_0$ — all of these are continuum-emergent but their *values* INHERIT from substrate microscopic data. They are *not* substrate-RG universals; they vary with substrate microscopic choice.
- **Coupling constants in the QED-emergent sector.** By the Yang-Mills arc inheritance pattern (YM-3 coupling values INHERITED), substrate-emergent gauge couplings inherit from substrate-microscopic data analogously.

The 0.6 ratio (Arc RG closure) is an exception: it is a substrate-RG universal that appears across regimes. But the 0.6 ratio is a *ratio* of PDE coefficients, not an *absolute* coupling magnitude. It washes out the overall scale dependence but does not pin individual coefficient values.

This is the structurally relevant precedent: **ED substrate-RG produces universal *ratios* (like 0.6) but not universal *absolute magnitudes*.** The structural pattern aligns with the standard-QFT pattern: critical-exponent-like quantities and dimensionless coefficient-ratios can be universal, while absolute coupling values typically are not.

### 4.3 Attractor analysis for participation strength

Without explicit substrate-RG flow-equation computation, structural argument suggests:

- Maximum-entropy fixed point is *generically* IR-attractive in symmetric block-averaging schemes.
- Stability-landscape extremum is *generically* IR-attractive if landscape is convex; otherwise multiple basins exist.
- Q-COMPUTE Class-A wall acts as a saturation endpoint, not an interior fixed point.

These are *structural plausibility* statements, not derivations. An explicit flow computation in a chosen operator basis would be needed to confirm them. The arc-RG closure provides the methodology template but did not perform this computation for participation-strength observables.

### 4.4 Honest assessment

The closed-arc evidence supports a *limited universality* picture for ED substrate-RG:

- Continuum-equation *forms* are universal (DCGT-confirmed).
- Some *ratios* of continuum coefficients are universal (0.6 example).
- *Absolute* coefficient values, including coupling magnitudes, are *not* universal.

This pattern is consistent with FSC-2.1's blocker propagating to the emergent scale: substrate-microscopic-connectivity freedom does not wash out at the level of absolute coupling magnitudes, even though it washes out at the level of continuum-equation form.

---

## 5. Possible Fixed-Point Structures

### 5.1 Fixed-point ratios of reversible to irreversible participation

A candidate substrate-RG universal: the ratio
$$R_\mathrm{rev/irrev} \;=\; \frac{\text{reversible participation flow}}{\text{irreversible participation flow}}$$
at the hydrodynamic-window scale. This ratio may have an IR-attractive fixed point determined by the substrate-RG flow on (reversible-channel mixing × commitment-rate density), with the value forced by P11 (commitment irreversibility) composed with V1 (reversible kernel structure).

**Structural plausibility.** Moderate. The closed Q-COMPUTE arc identified that reversible-vs.-irreversible architecture is a load-bearing distinction (Class A / B / C are partly distinguished by reversible-vs.-irreversible content). Whether a fixed-point ratio emerges from substrate-RG flow on this distinction is computable in principle but not yet computed.

**Cross-arc parallel.** Analogous to the "0.6 ratio" universal of Arc RG, but for a different operator pair. Same methodology applies.

### 5.2 Fixed-point spectral shapes

The most structurally interesting candidate: does the V1 spectral shape itself flow to a $k$-independent fixed-point shape under substrate-RG coarse-graining?

**Heuristic argument for plausibility.** The V1 cross-overlap integral $I(0)$ is the substrate analog of a one-loop QFT diagram (FSC-2 §3.4). In standard QFT, the one-loop running of dimensionless couplings is governed by the *anomalous dimensions* of the relevant operators — these are universal at IR fixed points (when such fixed points exist). If V1 shape parameters $\{s_i^{(k)}\}$ have IR-attractive fixed points under substrate-RG, the corresponding $I(0)^{(*)}$ would be a substrate-derived universal.

**Heuristic argument for skepticism.** Kernel shapes are typically *not* RG-attractive in standard analyses — they are sensitive to UV detail and do not flow to fixed-point shapes generically. The exceptions are theories with strong constraint structure (asymptotic safety, conformal field theories, etc.) which have additional symmetry or structural input. ED's substrate has structural input (P01–P13) but it is not clear this input is enough to pin V1-shape fixed points specifically.

**Verdict:** unsettled by structural argument; explicit flow computation required.

### 5.3 Fixed-point dimensionless groups (program-wide)

The closed-arc inventory provides candidate substrate-RG universals that have already been verified:

- The "0.6 ratio" (Arc RG closure).
- V5 cross-scale invariance (Maxwell / Hawking / entanglement, ~40 orders of magnitude).
- $\xi_\mathrm{canonical} = 1.7575$ lu canonical operating point (Arc ED-SC 3.x closure).
- BTFR slope-4 (substrate-gravity).
- Form-FORCED/value-INHERITED methodology (universal across closed arcs).

Each of these is a substrate-RG-universal dimensionless quantity. **The set is non-empty.** ED demonstrably *can* produce universal dimensionless quantities at the emergent scale.

The FSC-3 question is whether the set extends to include $\alpha$-like coupling magnitudes. The structural argument here is: most of the existing universals are *ratios* or *invariants* of substrate-emergent dynamics, not *absolute coupling values*. The pattern suggests that absolute coupling magnitudes are not in the same structural class.

But "the pattern suggests" is not the same as "structural impossibility." Unlike FSC-1's blockage (P09-continuity blocks quantization period), there is no closed-arc structural argument that *forbids* an absolute coupling magnitude from being substrate-RG-universal. The question is genuinely open.

---

## 6. Preliminary Verdict

### 6.1 Categorization

**FSC-3 preliminary verdict: (b) SPECULATIVE-COHERENT, structurally underdetermined by single-memo analysis.**

Specifically:

- *(a) Viable, structurally established.* NO. No closed-arc evidence forces a coupling-magnitude fixed point.
- *(b) Speculative-coherent.* **YES (preliminary).** Substrate-RG machinery exists and has produced universal ratios (0.6 example) and universal cross-scale invariants (V5 example). Whether the same machinery extends to absolute coupling magnitudes is structurally undetermined by present argument.
- *(c) Blocked-without-new-primitives.* NO. Unlike FSC-1 and FSC-2, no structural primitive forbids a coupling-magnitude fixed point. The blockage status would require an explicit flow computation that demonstrates IR-non-attractive behavior of coupling-like observables.
- *(d) Pure numerology.* N/A — FSC-3 is structurally serious as a question, not numerology.

### 6.2 What would close FSC-3 positively

A FSC-3-positive closure would require:

- **Explicit flow-equation computation** in a chosen operator basis that includes coupling-magnitude-like operators (extending Arc RG's PDE-coefficient operator basis to include V1-cross-overlap-type operators).
- **Identification of an IR-attractive fixed point** for the coupling-magnitude operator.
- **Verification of universality basin** showing that the fixed point's basin of attraction includes generic substrate-microscopic initial conditions (cubic, BCC, random-graph, etc., all flow to the same IR coupling value).
- **Bridge via T17 + DCGT** to identify the substrate-RG IR fixed-point value with the QED-emergent $\alpha$.

Estimated computational scope: 6–10 memos in the Arc RG / Arc D methodology style. Significant, but bounded.

### 6.3 What would close FSC-3 negatively

A FSC-3-negative closure would require:

- Explicit flow-equation computation in the chosen basis.
- Demonstration of *non-attractive* behavior (no IR fixed point, or multiple basins sensitive to initial conditions, or marginal behavior without dynamical pinning of value).
- A structural argument identifying *why* coupling-magnitude operators lack the universality structure (operator-dimension argument, symmetry argument, or pathology in the flow).

The result would sharpen position-paper §7.2 further: not only is the substrate-microscopic-connectivity freedom load-bearing at substrate scale (FSC-2.1), but it also propagates to emergent scales through the substrate-RG flow without fixed-point washout.

### 6.4 The most likely outcome

Honest assessment based on standard-QFT-analog patterns + ED closed-arc evidence (universal ratios but not universal absolute magnitudes):

> *The most likely outcome of a fully-computed FSC-3 is **partial universality**: substrate-RG IR-attractive fixed points exist for certain dimensionless ratios (like the 0.6 example) but not for absolute coupling magnitudes. The substrate-microscopic-connectivity freedom of FSC-2.1 likely propagates to emergent scales, modulated but not erased.*

If this outcome obtains, position-paper §7.2 is structurally upgraded a third time: from "FORCED-INHERITED at substrate" (after FSC-1 + FSC-2) to "FORCED-INHERITED at substrate-and-emergent scales, with partial universality at the level of coupling-ratios but not coupling-absolute-magnitudes." This would be the strongest form of the disclaimer and would align ED's coupling-magnitude content fully with the standard-QFT pattern: ratios may be universal, magnitudes are not.

A FSC-3-positive outcome (asymptotic-safety-analog with unique IR fixed point pinning all coupling magnitudes) would be a genuinely novel structural result, comparable in scope to the substrate-gravity-arc closure (Newton + $a_0$ + ECR substrate-derivation). It is not impossible, but it is not the structurally-expected outcome based on ED's existing closed-arc pattern.

---

## 7. Implications for Arc FSC and Beyond

### 7.1 Arc FSC status after FSC-3 Memo 1

The three sub-arcs are now characterized:

| Sub-arc | Status | Verdict | Closure type |
|---|---|---|---|
| FSC-1 (topological winding) | Closed negatively | Structural impossibility | P09 $U(1)$-continuity blocks |
| FSC-2 (V1 cross-overlap) | Closed negatively | Structural underdetermination | V1 spectral shape INHERITED |
| FSC-3 (substrate-RG fixed point) | **Open, preliminary verdict (b)** | Speculative-coherent | Closure requires explicit flow computation |

Arc FSC's primary sub-arcs (FSC-1, FSC-2) are closed. The arc's *honest closure* awaits FSC-3 resolution — if FSC-3 closes positively, position-paper §7.2 would need substantial revision; if FSC-3 closes negatively, §7.2 is doubly load-bearing.

### 7.2 Two-tier recommendation

**Tier 1: hold §7.2 disclaimer as currently stated.** The FSC-1 + FSC-2 closures + the FSC-3 preliminary "speculative-coherent" verdict together support the position-paper §7.2 disclaimer as load-bearing at present, with the explicit caveat that FSC-3 remains computationally open. The disclaimer should *not* be sharpened to "FORCED-INHERITED at substrate-and-emergent scales" until FSC-3 is explicitly closed.

**Tier 2: queue FSC-3 explicit flow computation as a long-horizon item** on the Investigation Priority List. Estimated 6–10 memos in Arc RG methodology style. Not a high-priority item; the negative outcome is structurally expected, and the positive outcome would be surprising. Either outcome is informative.

### 7.3 Decoupling from §7.2 disclaimer question

A subtlety from FSC-0 §7.1: FSC-3 was originally flagged as "decoupled from §7.2-disclaimer question" because its result would be an emergent-universality finding, not a substrate-microscopic-forcing finding. This memo's analysis confirms the decoupling:

- A FSC-3-positive closure would *not* undo FSC-1 (P09-continuity blockage at substrate level still holds).
- A FSC-3-positive closure would *partially* unblock FSC-2 (substrate-microscopic-connectivity freedom would be washed out by IR flow at the emergent scale).
- A FSC-3-negative closure would *strengthen* §7.2 to a doubled-up FORCED-INHERITED statement covering substrate AND emergent scales.

The §7.2 disclaimer holds either way; FSC-3 only changes its precise structural content.

### 7.4 Cross-arc consequences

- **Arc RG (closed).** Provides the methodology template for explicit FSC-3 flow computation. The operator-basis extension to include coupling-magnitude-like operators is the natural follow-on direction. Worth a coordinated re-opening if FSC-3 is pursued.
- **Yang-Mills arc.** YM-3's coupling-value INHERITED status is consistent with the most-likely FSC-3 outcome (partial universality, magnitudes inherited). A FSC-3-positive surprise would also reopen YM-3.
- **0.6 problem closure.** Provides the strongest positive precedent for substrate-RG universality of dimensionless quantities. The structural difference between "0.6 ratio" (closed positive) and "$\alpha$ value" (FSC-3 candidate) is ratio-vs.-absolute-magnitude, which is the load-bearing distinction.
- **V5 cross-scale unification.** The most striking emergent-universality finding in the closed-arc inventory. Suggests *some* substrate-derived dimensionless quantities are universal across scales. Does not directly establish that absolute coupling magnitudes are.
- **Q-COMPUTE arc.** Class-A wall at 140–250 kDa is a substrate-fixed *threshold*, not a coupling-magnitude. The structural distinction is the same one operating in FSC-3.

### 7.5 Honest scope caveats

This memo:

- Provides a *preliminary* verdict, not a closure. Settling FSC-3 requires explicit flow computation.
- Assumes the Arc RG methodology generalizes to coupling-magnitude operators. This is plausible but not verified.
- Does not address non-Abelian extensions or coupling-*ratio* universality (which may have stronger structural content than coupling-magnitude universality and is separately worth investigation).
- Does not address asymptotic-safety scenarios specifically (which would require analyzing UV fixed points of the substrate-RG flow, complementing the IR-fixed-point analysis emphasized here).

---

## 8. Summary

| Question (FSC-3 Memo 1 scope) | Answer |
|---|---|
| Does ED have substrate-RG structure? | Yes (Arc RG closed; DCGT-mediated flow demonstrated). |
| Has ED substrate-RG produced universal dimensionless quantities? | Yes (0.6 ratio; V5 cross-scale invariance). |
| Are these universal-ratios or universal-absolute-magnitudes? | Universal-*ratios* (and cross-scale invariants of substrate kernels). Not universal-absolute-magnitudes for coupling-like observables. |
| Does Arc RG methodology extend to coupling-magnitude operators? | Plausibly yes; not yet computed. |
| Is the FSC-3 mechanism viable (IR-attractive fixed point for coupling magnitude)? | Speculative-coherent. Not blocked by any closed-arc finding; not established by any closed-arc finding. |
| Verdict category (FSC-3 prompt §6)? | **(b) speculative-coherent**, structurally underdetermined by single-memo analysis. |
| Most likely outcome of full FSC-3 computation? | Partial universality: ratio fixed points exist, absolute-magnitude fixed points do not. |
| What would close FSC-3 positively? | Explicit flow computation showing IR-attractive fixed point for coupling-magnitude operator with universal basin. Estimated 6–10 memos. |
| Implication for position-paper §7.2? | Hold as currently stated. FSC-3 modifies precise structural content but does not undo FSC-1 + FSC-2 closures. |

---

## 9. References and Inheritance

| Inherited Item | Source | Use in FSC-3 Memo 1 |
|---|---|---|
| DCGT | Paper #73 / Arc D | Substrate-to-continuum bridge providing coarse-graining mechanism (§2.1) |
| Arc RG closure | `arcs/arc-RG/ED_RG_Flow_Analysis.md` | Wilsonian flow methodology + 0.6 ratio as universal-precedent (§2.2, §4.2, §5.3) |
| Stone-theorem normalization | Papers #4, #13 | Substrate-RG invariant amplitude constraint (§2.3) |
| V5 cross-scale unification | Arc Hawking H-4, Arc D, position paper §6.1 | Strongest emergent-universality precedent in closed-arc inventory (§2.3, §5.3) |
| Arc BH / BH-2 | `theory/Black_Holes/BH-2*` | Decoupling-surface saturation as substrate-RG boundary condition (§2.4) |
| Arc Q-COMPUTE / Class A wall | `theory/Quantum_Computing/` | Multiplicity-cap as fixed-point endpoint analog (§2.4, §3.3) |
| Yang-Mills arc / YM-3 coupling INHERITED | Arc YM | Standard inheritance-pattern for coupling magnitudes (§6.4) |
| ED-SC 3.x canonical operating point | Arc EDSC closure | Universal dimensionless quantity precedent (§5.3) |
| BTFR slope-4 universality | Arc SG | Universal dimensionless quantity precedent (§5.3) |
| FSC-0 opener | `FSC-0_opening.md` | Sub-arc structure; L1–L4 criteria |
| FSC-1 Memo 1 (polarity-transport topology) | `FSC-1_polarity_transport_topology.md` | Companion negative result (structural impossibility) |
| FSC-2 Memo 1 (V1 cross-overlap) | `FSC-2_v1_cross_overlap.md` | Companion negative result (structural underdetermination); FSC-3 is the candidate unblocker |

---

**End of FSC-3 Memo 1.**

*Preliminary verdict: (b) SPECULATIVE-COHERENT. ED substrate-RG demonstrably produces universal dimensionless ratios (0.6 example) and universal cross-scale invariants (V5 example), but no closed-arc evidence establishes IR-attractive fixed points for absolute coupling magnitudes. Closure requires explicit flow computation in extended Arc-RG operator basis, estimated 6–10 memos. Most likely outcome: partial universality — ratio fixed points exist, absolute-magnitude fixed points do not — which would further sharpen position-paper §7.2 disclaimer to substrate-AND-emergent-scale FORCED-INHERITED. Tier-1 recommendation: hold §7.2 as currently stated; queue FSC-3 explicit computation as long-horizon investigation item. Arc FSC's primary sub-arc closure (FSC-1 + FSC-2) is unaffected by FSC-3 status.*
