# Arc FSC — Memo 1: Topology of U(1) Polarity Transport in ED

**Status:** First load-bearing memo of Arc FSC sub-arc FSC-1. Single-question memo: does composition of P09 ($U(1)$-valued polarity), P05 (polarity-transport along edges), and P11 (commitment with uniform-$U(1)$ phase-randomization, irreversible) force quantized winding around closed substrate loops? Architect-mode active. No new primitives. No external gauge-theory imports beyond identification-not-derivation references.

**Date:** 2026-05-25

**Discipline reminder (FSC-0 §9).** This memo may not quote $1/137$, $\alpha = 1/137.036\ldots$, or any numerical value of the fine-structure constant. Numerical-match checks are reserved for sub-arc closure. Negative-but-informative outcomes (sharper structural-blockage statements) are first-class deliverables.

---

## 1. Restating the Question in ED Terms

### 1.1 What "winding" means without a metric, a gauge field, or a fiber bundle

In standard differential geometry, the winding number of a $U(1)$ holonomy around a closed loop is the integer
$$W(\gamma) = \frac{1}{2\pi i} \oint_\gamma A \in \mathbb{Z}$$
when the holonomy is forced to be trivial — i.e., when the wavefunction (a section of a $U(1)$ bundle) must be single-valued upon return. This integer is well-defined because (i) there is a smooth manifold over which the bundle is defined, (ii) the section is a continuous map into the bundle, (iii) the bundle has a topological classification.

ED's substrate is none of these things. There is no smooth manifold (P03 + P13 give a discrete loci/timestep structure; P08 sets the substrate scale $\ell_P$ at which discreteness lives). There is no fiber bundle (no smooth base manifold to put a bundle over). There is no a-priori gauge field — gauge structure emerges from P05 + P09 + P10 via T17 (Paper #5), it is not an input to the substrate.

What ED has is:

- A **participation graph** (P03's locus index set + P02's chain-channel participation relation), with vertices being (channel × locus) pairs and edges being substrate-level adjacencies along which P05's polarity-transport can act.
- A **$U(1)$-valued polarity field** $\pi_K(u) \in U(1) \cong S^1$ on the vertex set (P09).
- A **transport rule** assigning to each directed edge $e: (K, u) \to (K, u')$ a transport element $T_e \in U(1)$ such that under transport, an in-transit chain's carried polarity rotates by $T_e$ (P05's content in T17's reading).
- **Discrete commitment events** at specific (chain, locus, substrate-timestep) triples (P11).

The ED-native definition of "winding" must be built from these objects alone:

> **Definition (ED loop holonomy).** Let $\gamma = (e_1, e_2, \ldots, e_n)$ be a closed walk in the participation graph: a sequence of directed edges with $\mathrm{target}(e_i) = \mathrm{source}(e_{i+1})$ and $\mathrm{target}(e_n) = \mathrm{source}(e_1)$. The **substrate holonomy** of $\gamma$ for an in-transit chain that does not commit at any vertex along $\gamma$ is
> $$H(\gamma) = T_{e_n} \cdot T_{e_{n-1}} \cdots T_{e_2} \cdot T_{e_1} \in U(1).$$

Substrate holonomy is automatically a $U(1)$ element. The question of "quantized winding" becomes: *is $H(\gamma)$ structurally forced by P09 + P05 + P11 to lie in a discrete cyclic subgroup of $U(1)$* — that is, in $\{e^{2\pi i k/N} : k = 0, 1, \ldots, N-1\}$ for some substrate-fixed integer $N$ — *for all closed walks $\gamma$*?

### 1.2 Why the question is non-trivial in ED

Three structural facts make the answer non-obvious:

- **F-i.** Each edge transport element $T_e$ is a priori an arbitrary $U(1)$ element. P05 does not specify a discretization rule.
- **F-ii.** $\pi_K(u)$ is a single-valued function on the vertex set by P09 (each (channel, locus) has a definite polarity value). This already differs from the standard-physics setting where the wavefunction is a *section* (not a function) and single-valuedness imposes the constraint that generates quantization. In ED, single-valuedness is automatic for the polarity field — it carries no information.
- **F-iii.** P11 commitment events are discrete (an integer count of commitments along a loop is well-defined). But commitment also *randomizes* polarity, raising the question of whether commitment quantizes or decoheres the holonomy.

The honest path is to examine each of (F-i), (F-ii), (F-iii) and determine which (if any) forces quantization.

---

## 2. Minimal ED Objects That Carry a U(1) Phase Around a Loop

There are exactly three substrate-level loci where a $U(1)$ phase exists in ED:

### 2.1 The polarity field $\pi_K(u)$

This is a function $\pi_K: \mathcal{K} \times \mathcal{U} \to U(1)$ on (channels × loci). By F-ii, it is single-valued by definition. Around a closed walk, the polarity field returns to its starting value trivially: $\pi_K(u_0) = \pi_K(u_0)$. The polarity field itself has no loop-holonomy structure — it carries values, not phases.

The polarity field is the *target* of transport, not the carrier of transport. It plays the role of a "matter field" in lattice gauge theory (lattice-Higgs analog), not the role of a connection.

### 2.2 In-transit chain polarity

When a chain $\chi$ traverses an edge $e: u \to u'$ without committing, the chain's carried polarity $\pi_\chi$ evolves: $\pi_\chi^\mathrm{after} = T_e \cdot \pi_\chi^\mathrm{before}$. This is the substrate analog of "parallel transport of a charged particle's phase along a path."

This is the *only* substrate-level locus where $U(1)$ holonomy meaningfully accumulates around a closed loop. The ED-native definition of §1.1 is precisely the closed-walk product of edge transports applied to chain polarity.

### 2.3 Commitment-event randomization

P11 specifies: at a commitment event, the post-commitment polarity is drawn uniformly from $U(1)$, independent of pre-commitment polarity. The commitment event itself is not a $U(1)$ phase; it is a *substitution* of phase by a uniform random variable.

Commitment events are discrete (countable along a chain trajectory) but the substitution rule is continuous (uniform on $U(1)$). They are at best a *de-correlation* mechanism, not a $U(1)$-phase carrier.

### 2.4 What is NOT present

Several objects standard physics would use to construct quantization arguments are explicitly *absent* from ED's substrate:

- **Wavefunctions as bundle sections.** The participation measure $P_K = \sqrt{b_K}\, e^{i\pi_K}$ is a *function* on (channels × loci × time), not a section of a $U(1)$ bundle. P09 makes $\pi_K(u)$ a function valued in $U(1)$, with $U(1)$ playing the role of a *target space*, not a *fiber*.
- **Magnetic monopoles or topological defects in P05's transport.** P05 specifies that edges have transport elements; it does not specify singular vertices where transport is undefined. The participation graph is regular — every vertex is identical structurally (P03 spatial homogeneity).
- **Cohomology classes on a smooth base.** The substrate has no smooth base; chain cohomology on the discrete participation graph exists but is the integral homology of a 1-complex, which is free abelian on edge cycles. There is no torsion structure that would quantize anything.

The absence of these objects is *not* a deficiency of ED's exposition — it is structural. ED's substrate is a discrete graph with $U(1)$-valued vertex labels and $U(1)$-valued edge labels, plus a discrete event-set for commitments. That is the full inventory.

---

## 3. Is P05 Polarity-Transport Path-Dependent?

### 3.1 Two readings of P05

A reading question must be resolved before proceeding: does P05 specify transport that is *path-independent* (trivializable globally, i.e., $T_e$ can be gauged away by a vertex-relabeling) or *path-dependent* (non-trivial holonomy possible)?

- **Reading-A (trivial connection).** $T_e$ is a comparison rule: it says "the polarity at $u'$, expressed in $u$'s reference, equals $T_e \cdot \pi_K(u')$." Under this reading, polarity values are absolute (P09), and the transport rule simply restates the values. All holonomies are identity. This reading makes P05 informationally vacuous — it adds no structure beyond P09.
- **Reading-B (genuine connection).** $T_e$ is the substrate's *physical* rule for evolving chain-carried phase along an edge. Different paths between the same endpoints can yield different evolved phases. The holonomy around closed walks is generally non-trivial.

### 3.2 T17 forces Reading-B

T17 (gauge-field-as-rule-type, Paper #5 / Paper #15) reads P05 as the substrate-level *gauge connection* whose continuum coarse-graining (via DCGT) produces the gauge potential $A_\mu$. Specifically, T17 identifies:

- P05's edge transport elements $T_e$ ↔ the lattice-link variables $U_\mu(x)$ of lattice gauge theory ↔ the continuum $e^{i \int A_\mu \, dx^\mu}$ along an edge.
- The substrate's elementary closed walks (4-vertex plaquettes in the participation graph at substrate scale $\ell_P$) ↔ the lattice plaquette variables $U_{\mu\nu}(x)$ ↔ the continuum field strength $F_{\mu\nu}$ via the lattice-curvature identification.

If P05 were Reading-A (trivial connection), then all plaquette curvatures would be identity, all lattice field strengths would vanish, and T17's coarse-graining would produce $F_{\mu\nu} \equiv 0$ — no gauge dynamics, contradicting the substrate-emergent existence of gauge fields. Since T17 is a closed-arc result with substantive content (it produces the Yang-Mills structural derivation of the YM arc and the Lorentz-covariant minimal-coupling content of Paper #6 / Paper #7), Reading-A is structurally excluded.

**Conclusion: P05 is a genuine connection (Reading-B). Polarity-transport is path-dependent in general.**

### 3.3 Consequence: substrate holonomy is generically in $U(1)$, continuous

Under Reading-B, the substrate holonomy $H(\gamma)$ of §1.1 is a non-trivial $U(1)$ element for generic loops. The transport elements $T_e$ are a priori arbitrary in $U(1)$; their product around a closed walk is a generic $U(1)$ element; no constraint forces the product into a discrete subgroup.

This is *consistent with* the closed-arc Aharonov-Bohm walkthrough (`walkthroughs/from_primitives_to_aharonov_bohm.md`) and Berry-phase walkthrough (`walkthroughs/from_primitives_to_berry_phase.md`), both of which produce *continuous* substrate-level phase accumulation matching the standard continuous results. Neither walkthrough requires or produces phase quantization at the substrate level; both reproduce continuous geometric phases.

The path-dependence of P05 is the structural source of substrate holonomy. It is also the structural source of (continuous) emergent gauge physics. The same primitive that makes holonomy *exist* also makes it *continuous*.

---

## 4. Does P11 Introduce a Topological Obstruction or Quantization Condition?

This is the load-bearing question of the memo. We examine three candidate mechanisms by which P11 could quantize substrate holonomy.

### 4.1 Mechanism 4.1: P11 as discrete-event counter

P11 commitment events are countable: along any chain trajectory, the number of commitments $n_\gamma$ is a well-defined non-negative integer. Could $n_\gamma$ itself, or some functional of it, quantize the holonomy?

The structure of a commitment event (P11):

1. Pre-commitment: chain has multi-channel participation with polarities $\{\pi_K\}_K$ across channels.
2. Commitment fires: chain collapses to a single channel $K_*$.
3. Post-commitment: chain's polarity in $K_*$ is drawn uniformly from $U(1)$, independently of $\{\pi_K\}_K$.

**Critical observation.** The post-commitment polarity is *independent* of the pre-commitment polarities. There is no functional relation $\pi_\chi^\mathrm{after} = f(\pi_\chi^\mathrm{before}, n_\gamma)$ with $f$ depending on commitment count — the post-commitment value is uniform random regardless of $n_\gamma$.

Therefore the count $n_\gamma$ does not enter the holonomy as a structural constraint. It enters only as a *decoherence event count* — the number of statistically independent uniform-random phase substitutions that occurred along the walk.

**Verdict.** Mechanism 4.1 does not yield quantization. The discrete count $n_\gamma$ is real, but it does not pin the substrate holonomy to discrete values.

### 4.2 Mechanism 4.2: P11 as single-valuedness enforcer

In standard QM, the Dirac quantization argument runs: *the wavefunction is a section of a $U(1)$ bundle; under transport around a closed loop, the section's phase changes by the holonomy; consistency requires the holonomy to equal $1$ (single-valuedness), which forces $e \cdot g / \hbar \in 2\pi\mathbb{Z}$ for a monopole charge $g$.*

Could P11 play the analog role in ED? The argument would be: a chain that commits, traverses a loop, and re-commits at the same locus must produce the *same* uniform-random distribution before and after — and this distributional consistency forces the holonomy to lie in a discrete subgroup.

Examination of this candidate argument:

- Before the loop traversal: chain commits at $u_0$, post-commitment polarity $\pi^{(1)} \sim \mathrm{Uniform}(U(1))$.
- Chain traverses closed walk $\gamma$ back to $u_0$: chain's carried polarity is now $H(\gamma) \cdot \pi^{(1)}$.
- Chain re-commits at $u_0$: post-commitment polarity $\pi^{(2)} \sim \mathrm{Uniform}(U(1))$, independent of $H(\gamma) \cdot \pi^{(1)}$.

The pre-commitment polarity at the second commitment is $H(\gamma) \cdot \pi^{(1)}$, a $U(1)$ rotation of a uniform random variable. *But the uniform distribution on $U(1)$ is invariant under $U(1)$ rotation.* So $H(\gamma) \cdot \pi^{(1)}$ is distributed identically to $\pi^{(1)}$, *regardless of the value of $H(\gamma)$*. The distributional consistency is automatic for any $H(\gamma) \in U(1)$.

**Verdict.** Mechanism 4.2 fails because uniform $U(1)$ distributions are $U(1)$-rotation-invariant. The single-valuedness analog in ED is *automatically satisfied* by every holonomy, not just by holonomies in a discrete subgroup. P11's uniform-randomization choice (which is forced by maximum-entropy / no-preferred-phase considerations) specifically erases the constraint that would generate quantization.

This is a sharp structural finding: **the very feature of P11 that makes it a uniform randomization — invariance under arbitrary $U(1)$ shifts — is the feature that prevents it from quantizing holonomy.** A P11 variant with a non-uniform post-commitment distribution would generate a quantization condition. The uniform variant does not.

### 4.3 Mechanism 4.3: P11 as topological-obstruction source

A commitment event severs the chain's pre-commitment phase from its post-commitment phase. Could this severance act as a topological *obstruction* — a defect in the participation graph's $U(1)$ bundle, analogous to a Dirac string?

Examination:

- In standard physics, a Dirac string is a 1-dimensional defect on a 3-dimensional base manifold such that the holonomy around any loop linking the string is a fixed non-trivial element (the monopole charge).
- The ED substrate has no 3-dimensional manifold and no 1-dimensional defect locus. Commitment events are *point-events* in (chain × locus × substrate-timestep), not 1-dimensional loci that can be "linked" by 2-dimensional loops.
- A loop in the participation graph cannot "link" a commitment event in any homological sense — commitment events are not subobjects of the participation graph; they are events that happen *to chains traversing the graph*, attached to chain trajectories rather than to graph vertices or edges intrinsically.

The structural mismatch: commitment events live in chain-trajectory space, not in participation-graph space. The would-be topological linking relation (loop links defect) does not have a substrate-level realization.

**Verdict.** Mechanism 4.3 fails for structural-dimensional reasons. P11 events are not topological-obstruction loci of the substrate participation graph.

### 4.4 Mechanism 4.4: Plaquette quantization from substrate scale

A subtler candidate: at substrate scale $\ell_P$, the participation graph has elementary closed walks (plaquettes) of integer length 4 (or 3 or 6 depending on graph structure). If each elementary plaquette's holonomy were forced into a discrete subgroup by some substrate-consistency argument, larger loops would inherit the quantization by composition.

This requires identifying a substrate-level argument that forces *every* plaquette holonomy $H_\square \in U(1)$ to lie in $\{e^{2\pi i k/N}\}$ for some substrate-fixed $N$. Candidate arguments:

- (a) **Stability landscape extremum at plaquette level.** $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$ (P12) extremized over plaquette configurations could prefer discrete $H_\square$ values. *Examination:* the $\Sigma$ landscape's continuous-$U(1)$ symmetry under simultaneous polarity rotations means its extrema in $H_\square$ form continuous orbits, not discrete points. No quantization.
- (b) **Substrate finite-state-per-locus.** If the substrate has only finitely many distinct polarity states per locus (a hidden $\mathbb{Z}_N$ structure underlying the $U(1)$ continuous label), plaquettes would inherit $\mathbb{Z}_N$ quantization. *Examination:* this requires modifying P09 from "$\pi_K(u) \in U(1) \cong S^1$" to "$\pi_K(u) \in \mathbb{Z}_N$ with $U(1)$ as a continuum-limit emergence." This is a new primitive (P09'), explicitly outside Arc FSC's no-new-primitives discipline.
- (c) **Cohomology constraint from boundary-of-boundary.** The product of plaquette holonomies around a closed 2-surface in the participation 2-complex equals the identity by the "boundary of boundary is zero" identity (Bianchi-analog at the substrate level). *Examination:* this is true but does not quantize *individual* plaquette holonomies. It is a global cohomological consistency that admits continuous solutions.

**Verdict.** Mechanism 4.4 fails. The candidate routes either require new primitives (b) or yield no quantization (a, c).

---

## 5. Closed-Loop Transport Verdict

Combining §3 (path-dependent continuous transport via P05) with §4 (P11 fails to quantize at all three examined mechanisms):

**Closed-loop substrate holonomy is (b) continuous in $U(1)$.**

Explicit statement of the substrate-level structural finding:

> **Finding (FSC-1.1).** For any closed walk $\gamma$ in the substrate participation graph, the substrate holonomy $H(\gamma)$ is a generically continuous element of $U(1)$. The composition of P09 ($U(1)$-valued polarity), P05 (polarity-transport along edges, identified as a genuine connection by T17), and P11 (commitment with uniform-$U(1)$ phase-randomization, irreversible) does not force $H(\gamma)$ into any discrete cyclic subgroup $\mathbb{Z}_N \subset U(1)$. The holonomy admits all continuous $U(1)$ values without substrate-level structural constraint.

This is the *gate-failure* outcome for Arc FSC's polarity-transport route. The candidate mechanism (4.4 in FSC-0) — *topological invariant of polarity-transport holonomy as the substrate origin of an $\alpha$-like integer* — is structurally blocked at the substrate level.

---

## 6. If Quantization Is Impossible, Which Primitive Blocks It?

The blockage is *over-determined* by three primitives, with one dominant and two reinforcing:

### 6.1 Dominant blocking primitive: P09

**P09 specifies $\pi_K(u) \in U(1) \cong S^1$.** $U(1)$ is the continuous circle group, not a discrete cyclic group. This continuity propagates through the entire holonomy construction:

- Edge transport elements $T_e \in U(1)$ inherit continuity from P09's polarity values.
- Plaquette holonomies inherit continuity from edge transports.
- Loop holonomies inherit continuity from edge transports (or, equivalently, from plaquette holonomies via §4.4(c)).

To force quantization, P09 would have to be replaced or amended:

- **P09' (Z_N-valued polarity).** $\pi_K(u) \in \mathbb{Z}_N$ for a substrate-fixed integer $N$. This is a *new primitive*, distinct from P09. It conflicts with the closed-arc derivation of continuous Aharonov-Bohm phase and continuous Berry phase (both of which produce continuous substrate-level results matching experiment).
- **P09'' (U(1) with substrate-level discretization scale).** $\pi_K(u) \in U(1)$ at the level of P09's statement, but with a substrate-emergent discreteness at substrate scale $\ell_P$ that re-emerges as continuous $U(1)$ only in the DCGT coarse-graining limit. This would be a deep substrate modification with its own structural consequences (continuous-AB and continuous-Berry would need re-derivation as coarse-graining-emergent rather than substrate-level).

Neither amendment is supported by closed-arc evidence. P09 as currently stated is the dominant blocking primitive.

### 6.2 Reinforcing blocker: P11's uniform randomization

The *uniform* in "P11 commitment with uniform-$U(1)$ phase-randomization" is itself the reinforcing block. A non-uniform post-commitment distribution would not be $U(1)$-rotation-invariant, and the §4.2 distributional-consistency argument would yield a quantization condition.

P11's uniform-randomization choice is *itself* structurally motivated by maximum-entropy considerations (no preferred phase emerges from a substrate with no preferred-phase content). The choice is internally consistent with the substrate's symmetry-content but produces the side-effect that distributional consistency under loop transport is automatic and unconstraining.

### 6.3 Reinforcing blocker: substrate-graph dimensional structure

§4.3's finding — commitment events live in chain-trajectory space, not in graph-topology space, so the loop-linking relation has no substrate realization — is a structural feature of how P11 events attach to the substrate. Commitment events are *events* (P11) at chain × locus × substrate-timestep triples, not *defects* in the participation graph.

This is a reinforcing block: even if P11 events were to carry a topological charge (which they do not), the absence of a linking-relation between graph loops and chain-trajectory events would prevent that charge from quantizing graph-loop holonomy.

### 6.4 Structural diagnosis

The blockage is not an artifact of incomplete exposition or unrealized composition. It is forced by:

- P09's specification that polarity takes values in the continuous group $U(1)$, not in any discrete subgroup.
- P11's uniform-randomization, which is itself motivated by substrate symmetry considerations and which produces $U(1)$-rotation-invariant distributions that do not constrain holonomy.
- The category of P11 events (chain-attached, not graph-attached), which prevents a linking-class quantization mechanism.

Three independent structural features each independently block quantization. The blockage is over-determined.

---

## 7. Honest Caveats

Three caveats should accompany the verdict:

### 7.1 Substrate-level vs. coarse-grained quantization

The verdict applies at the substrate level. Flux quantization in superconductors is a familiar example of a *coarse-grained* quantization: the underlying microscopic theory (electrons + electromagnetic field) does not quantize flux, but the macroscopic wavefunction (the order parameter) does, because its single-valuedness across the superconducting region forces $\oint A \in 2\pi\mathbb{Z} \cdot \hbar/(2e)$.

ED's substrate-level holonomy is continuous. Whether *coarse-grained* (DCGT-emergent) quantization can occur at higher scales — when the participation measure $P_K = \sqrt{b_K}\, e^{i\pi_K}$ acquires a global-coherence regime analogous to a superconducting order parameter — is **not addressed by this memo and is not blocked by the substrate-level finding**. This is a follow-on question, not a closure-altering caveat.

### 7.2 The verdict is about *quantization*, not about *existence*

The substrate-level holonomy $H(\gamma)$ exists (it is well-defined and continuous in $U(1)$). What is blocked is its *discrete-cyclic-subgroup* quantization. Continuous holonomy is exactly what the AB and Berry-phase walkthroughs produce and what experimental observation matches. The blockage of quantization is *not* a problem for those closed arcs — it is consistent with them.

### 7.3 No analogous claim is made about non-Abelian rule-types

T17 establishes that the substrate's gauge structure admits non-Abelian rule-types (compact simple Lie groups with Killing-form / Jacobi closure). The current memo addresses only the $U(1)$ polarity primitive P09; whether non-Abelian rule-type holonomy admits a different quantization story is **outside this memo's scope**. (Brief observation: standard non-Abelian gauge theory's center-symmetry quantization $\mathbb{Z}_N \subset SU(N)$ might admit a substrate-level analog, but the question is not the FSC question — $\alpha$ is the $U(1)$-sector coupling, not a non-Abelian coupling.)

---

## 8. Implications for Arc FSC

### 8.1 Sub-arc FSC-1 verdict

FSC-1's load-bearing question (FSC-0 §7.1, Mechanism 4.4) is closed negatively:

> **FSC-1 verdict.** Composition of P09 + P05 + P11 does not force quantized holonomy around closed substrate loops. The topological-winding route to an $\alpha$-like substrate-derived integer is structurally blocked. The dominant blocker is P09's $U(1)$-continuity; reinforced by P11's $U(1)$-rotation-invariant uniform-randomization and by the chain-attached (not graph-attached) category of commitment events.

FSC-1 produced a *negative-but-informative* outcome in the sense of FSC-0 §9. The arc is not closed by this single memo (additional sub-questions in FSC-0 §7.1 examined holonomy more broadly — e.g., monopole-analog forcing, Berry-phase + commitment composition — but each reduces to the same P09-continuity blockage demonstrated here). A follow-on FSC-1 closure memo would consolidate these structural variants, but the substrate-level verdict is already settled by Finding FSC-1.1.

### 8.2 Promotion of FSC-2 to next active sub-arc

With FSC-1 blocked, the remaining viable structural sub-route is **FSC-2: V1-kernel cross-overlap computation** (FSC-0 §7.1). FSC-2's load-bearing question — does $\int V_1(x) V_1(x+\delta)\, d^4x$ under N1's forced V1 form + T18's retarded support yield a forced dimensionless value? — does not depend on holonomy quantization and is not blocked by Finding FSC-1.1.

FSC-2 is promoted to next active sub-arc of Arc FSC.

### 8.3 Sharpening of position-paper §7.2

The position paper's §7.2 disclaimer ("ED does not derive the specific values of fundamental coupling constants; coupling magnitudes are inherited") can be sharpened in light of Finding FSC-1.1. The sharpened statement:

> *ED does not derive coupling-constant magnitudes via topological winding of $U(1)$ polarity transport. P09's specification of polarity values in the continuous group $U(1)$, combined with P11's $U(1)$-rotation-invariant uniform-randomization at commitment events, structurally forbids substrate-level holonomy quantization. The substrate's continuous-holonomy result is consistent with the continuous Aharonov-Bohm and Berry phases observed experimentally. Quantization of an EM coupling constant by this route would require either modifying P09 to a discrete polarity group (a new primitive, distinct from the 13-primitive set) or producing the quantization at a coarse-grained scale via DCGT-emergent global-coherence structure (not addressed at the substrate level).*

This is a structural upgrade from "we do not derive" (silence on mechanism) to "this specific route is blocked, and here is the load-bearing structural reason." The §7.2 disclaimer remains in force; its content is now more informative.

### 8.4 Cross-arc consequences

- **Yang-Mills arc.** YM-3's mass-gap mechanism inherits coupling values; Finding FSC-1.1 indicates the inheritance is structural rather than provisional for the $U(1)$ sector. The non-Abelian center-symmetry analog (§7.3 caveat) remains an open question for YM-specific coupling magnitudes.
- **Q-COMPUTE arc.** The closed-form $\mathcal{M}_\mathrm{crit}$ open item (O-QC-1) is structurally distinct from $\alpha$-derivation — $\mathcal{M}_\mathrm{crit}$ is a multiplicity-counting threshold (P12 + Q-COMPUTE machinery), not a holonomy or coupling-strength ratio. The cross-check posed in FSC-0 §7.2 is partially answered: they are *not* the same substrate-constants problem, at least via the polarity-transport route.
- **0.6 problem / RG three-regime arc.** FSC-3's substrate-RG fixed-point question is unaffected by Finding FSC-1.1. RG fixed points (if they exist at the substrate scale) do not require holonomy quantization.
- **Berry phase + Aharonov-Bohm walkthroughs.** Finding FSC-1.1 is *consistent* with these closed walkthroughs and does not require their revision. The continuous-phase results both walkthroughs produce are exactly the substrate-level expectation under continuous $U(1)$ holonomy.

---

## 9. Summary

| Question | Answer | Mechanism |
|---|---|---|
| Does ED have a substrate-level $U(1)$ phase that can accumulate around loops? | Yes (in-transit chain polarity, transported by P05 across edges). | T17 reading of P05 as genuine connection; Reading-B forced by closed-arc YM and gauge content. |
| Is P05 polarity-transport path-dependent? | Yes (generically). | T17 + substrate-emergent gauge dynamics require non-trivial plaquette holonomies. |
| Does P11 introduce a topological obstruction? | No (commitment events are chain-attached, not graph-attached; no linking relation). | §4.3 structural-dimensional mismatch. |
| Does P11 introduce a quantization condition? | No (uniform-$U(1)$ randomization is $U(1)$-rotation-invariant; distributional consistency holds for all $H(\gamma) \in U(1)$). | §4.2 distributional-invariance argument. |
| Is closed-loop substrate holonomy quantized? | **No — continuous in $U(1)$.** | §5 Finding FSC-1.1. |
| What primitive blocks quantization? | **P09 (dominant), reinforced by P11's uniform-randomization and the chain-attached category of P11 events.** | §6 over-determined structural blockage. |
| Can ED's existing $U(1)$ polarity support topological quantization of participation strength? | **No, not without modifying P09 or producing quantization at a coarse-grained scale via emergent global-coherence structure.** | §7.1 caveat scopes coarse-grained possibility as future question. |

---

## 10. References and Inheritance

| Inherited Item | Source | Use in FSC-1 |
|---|---|---|
| P05, P09, P10, P11 | Position paper §1 | Primary structural inputs |
| T17 gauge-field-as-rule-type | Paper #5 / Arc M closure | Forces Reading-B of P05 as genuine connection (§3.2) |
| Aharonov-Bohm substrate walkthrough | `walkthroughs/from_primitives_to_aharonov_bohm.md` | Consistency check (continuous phase) |
| Berry-phase substrate walkthrough | `walkthroughs/from_primitives_to_berry_phase.md` | Consistency check (continuous phase) |
| Yang-Mills arc | Arc YM (closed 2026-04-30) | Establishes that substrate gauge dynamics has non-trivial plaquette curvatures (§3.2) |
| Position paper §7.2 disclaimer | Position paper | Load-bearing target; sharpened in §8.3 |
| FSC-0 opener | `FSC-0_opening.md` | Sub-arc structure; Mechanism 4.4 → FSC-1 |

---

**End of FSC-1 Memo 1.**

*Finding FSC-1.1: substrate holonomy is continuous in $U(1)$; quantization is structurally blocked by P09 (dominant) with P11 uniform-randomization and chain-attached P11 event category as reinforcing blockers. Sub-arc FSC-1 verdict: topological-winding route to $\alpha$-like substrate integer is closed negatively. Sub-arc FSC-2 (V1-kernel cross-overlap) promoted to next active. Position-paper §7.2 disclaimer sharpened: not just "inherited" but "structurally blocked by P09-continuity for the polarity-transport route specifically."*
