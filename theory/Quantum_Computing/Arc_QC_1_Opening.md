# Arc QC — Memo 1: What Quantum Computation Is in ED, and the Substrate Invariants of Its Limits

**Status:** Opening memo of Arc Q-COMPUTE. Architect-mode active. No speculation without derivational support; substrate-grounded only; form-FORCED / value-INHERITED methodology.

**Date:** 2026-05-02

---

## 1. Structural Summary

The arc's load-bearing question, in ED's own language:

> *What is the ED-substrate signature of a system performing quantum computation, and what substrate-level constraints govern its scaling?*

Standard physics frames quantum computation as a delicate engineering achievement maintained against decoherence. ED reframes: **quantum computation is the deliberate, controlled occupation of a low-multiplicity ED-regime — a regime in which a system's participation rules remain unresolved long enough for global structural manipulations to be performed before environmental ED-injection forces individuation**. The "limits of QC" are then the substrate-level constraints on holding a system in that regime as a function of the system's multiplicity load, the gradient sparsity that bounds it, and the architectural mechanism doing the holding.

This memo:

- Restates the problem in substrate language.
- Identifies the load-bearing invariants: **multiplicity** $\mathcal{M}$, **unresolvedness** $\mathcal{U}$, **gradient sparsity** $\sigma$.
- Fixes the substrate assumptions inherited from closed-arc work that the arc will treat as given.
- Proposes the first decomposition of the arc into derivable components.
- Identifies the first theorem-shaped object that must be established before any scaling law can be derived: the **Unresolved-Regime Characterization Theorem** (UR-1).

The arc proceeds: structural account first, multiplicity-cap function second, architecture classifier third, predictive content fourth. Predictive content is downstream of structural derivation, never in front of it.

---

## 2. Derivation / Argument

### 2.1 Restatement of the problem

A "quantum computer," in standard language, is a device that maintains a coherent superposition over many degrees of freedom, performs unitary operations on that superposition, and reads out a classical result. Three of those four words require translation into substrate language.

- **"Coherent superposition"** is, per ED-I-13 + ED-10 §7.4, the persistence of an *unresolved participation rule* spanning multiple endpoints. It is not a state being in two places at once; it is the absence of individuation across a participation structure that hasn't yet committed.
- **"Unitary operation"** is, per Phase-1 + ED-10 §7.4 + Theorem 18, evolution in the thin-participation regime — substrate dynamics where commitment hasn't yet occurred and the participation geometry can be reconfigured reversibly. Unitarity is the regime-property of substrate dynamics in the unresolved sector, not a postulate.
- **"Readout"** is, per P11 + ED-I-29, an ED-injection event that forces individuation: environmental ED-flow proliferates gradients into the system, the system's participation rule must individuate to one of its compatible endpoints, and the result is committed irreversibly.

So a quantum computer, in ED's reading, is **a deliberately engineered region of substrate where a participation rule is held in the unresolved low-multiplicity regime long enough for its geometry to be manipulated, before being committed via ED-injection at readout**.

This is structurally the same kind of object as a Josephson junction (ED-I-23), a bulk superconductor (ED-I-01), and the inside of a saturated participation zone (BH-3). Each is a region of low-multiplicity ED-flow held against the substrate's natural tendency to proliferate gradients and force individuation. The differences are only in *what holds the low-multiplicity regime in place* and *what is being done with it while it persists*. A bulk superconductor uses lattice symmetry to hold the regime and transports charge through it; a JJ adds an engineered sparsity-bottleneck to enforce non-individuation across a barrier; a QC uses the regime as an operating substrate on which to execute manipulations of the unresolved participation geometry.

### 2.2 The load-bearing invariants

Three substrate quantities govern the arc.

**Definition (D1) — Multiplicity** $\mathcal{M}(\mathcal{S})$.

Per ED-I-01 §2.3, multiplicity is the ED analogue of entropy: the number of viable distinct ED-gradient pathways available to a system $\mathcal{S}$. Operationally, it counts the substrate-resolvable participation channels that the system's current ED-structure can support.

- $\mathcal{M} \to 1$: only one viable participation pathway. Hyper-coherent regime. Bulk superconductor; engineered qubit at full coherence.
- $\mathcal{M} \to \infty$: arbitrarily many pathways. Classical thermal regime.

$\mathcal{M}$ is defined per region per substrate timescale. A composite system has a *system multiplicity* that depends both on the multiplicity of its components and on the substrate connectivity between them.

**Definition (D2) — Unresolvedness** $\mathcal{U}(\mathcal{S},t) \in [0,1]$.

The integrity of a participation rule that spans multiple endpoints of $\mathcal{S}$ at substrate time $t$. $\mathcal{U} \to 1$ when the rule remains globally coherent across all designated endpoints (no individuation has occurred). $\mathcal{U} \to 0$ when the rule has fully individuated (full classicality reached).

$\mathcal{U}$ is closely related to but distinct from $\mathcal{M}$:
- $\mathcal{M}$ is the *available* count of pathways at a substrate region.
- $\mathcal{U}$ is the *dynamical state* of a specific participation rule as it traverses or spans those pathways.

A system can have low $\mathcal{M}$ (one viable pathway) and $\mathcal{U} = 1$ (the rule is coherently occupying that pathway). It can also have low $\mathcal{M}$ and $\mathcal{U} = 0$ (the rule has individuated to one of the available pathway endpoints). Both quantities are required.

**Definition (D3) — Gradient sparsity** $\sigma(\mathbf{x})$.

Inherited from BH-2: $\sigma = |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$. The substrate-scale steepness of participation density. Load-bearing for whether substrate channels carrying participation rules between regions remain bandwidth-supported. ED-I-23 + ED-I-29 establish that engineered low-$\mathcal{M}$ regions are deliberately constructed sparsity bottlenecks: the bulk SC electrodes have collapsed-gradient $\mathcal{M} \approx 1$, and the JJ barrier imposes a sparsity gap that prevents the two electrodes from individuating against each other.

### 2.3 Substrate assumptions inherited from closed-arc work (treated as fixed)

The arc treats the following as substrate-level facts, derived in prior closed arcs:

1. **Phase-1 closure.** Quantum mechanical evolution in the thin-participation regime is structurally unitary; the four QM postulates are derived (T1–T16). $\hbar$ enters as a substrate constant from the Born-Gleason and bandwidth-conservation results.
2. **Theorem 18 / V1 retardation.** The V1 vacuum kernel is finite-width and forward-cone-only. Substrate dynamics carry a kernel-level arrow of time; cross-endpoint correlations propagate forward only.
3. **Arc D / DCGT.** Substrate-to-continuum bridge for canonical-ED dynamical content via hydrodynamic-window scale separation $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$. Cross-bandwidth between substrate regions takes the form $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$.
4. **ED-I-01.** Multiplicity is the ED analogue of entropy. Symmetry = low-$\mathcal{M}$ structure. Decoherence = re-entry into high-$\mathcal{M}$. Critical-threshold structure: $\mathcal{M}$ is held low by structural mechanism (lattice symmetry, engineered barrier, global geometry, or redundancy) until ED-injection overwhelms the mechanism.
5. **ED-I-23.** Engineered low-$\mathcal{M}$ regions (Josephson-class) are sparsity bottlenecks. Coherence is enforced by structural simplification, not maintained by isolation. Macroscopic quantum coherence is the persistence of low-$\mathcal{M}$ geometry.
6. **ED-I-29.** Tunneling = global reconfiguration of a participation rule across sparse-$\sigma$ regions; low-$\mathcal{M}$ systems can reconfigure, high-$\mathcal{M}$ cannot. Macroscopic systems do not tunnel because their identity is too developed.
7. **ED-I-13.** Quantum information operations are channel-geometry manipulations of unresolved participation rules. Five landmark QI operations (Deutsch, Deutsch-Jozsa, BB84, teleportation, Shor) are reframed as global, multiplicity-mediated, rewrite-on-measurement, identity-reassignment, and symmetry-extraction operations on ED-channel geometry.
8. **ED-I-14.** Topological phases are global invariants of ED-channel geometry — phase without force from multiply-connected channels with nontrivial global curvature.
9. **ED-I-18.** Multi-timescale systems are high-multiplicity ED-objects whose redundancy expands the viable-pathway count. Topological protection is rigidity of ED-gradients.
10. **ED-I-12.** Photonics is the engineering of ED-gradients; channels are removed, inverted, redirected, encoded, and composed by structural manipulation of the gradient landscape.

These ten anchors are *taken as given*. The arc neither rederives them nor relaxes them.

### 2.4 First decomposition

**Decomposition I — The arc splits into four sequential blocks.**

- **Block A (this memo + UR-1).** What QC *is* in substrate language. Establish $\mathcal{U}$, $\mathcal{M}$, $\sigma$ as load-bearing invariants. Derive the Unresolved-Regime Characterization Theorem (UR-1) — the substrate conditions necessary and sufficient for a system to be in the unresolved regime. Without UR-1, no scaling law has structural ground.
- **Block B.** Failure modes — the substrate-level mechanisms that drive $\mathcal{U} \to 0$ on an engineered system. (F1) premature individuation from environmental ED-injection; (F2) cross-endpoint decoupling from $\Gamma_\mathrm{cross}$ collapse; (F3) commitment-pressure cascade from accumulated P11 events. Each failure mode is given a substrate-level rate or scaling.
- **Block C.** Architectural classification — the substrate-allowed mechanisms for *holding* $\mathcal{U} \approx 1$ against the failure modes in Block B. The provisional three-class hypothesis (engineered-low-multiplicity / global-geometric / high-multiplicity-redundancy) must be either derived as substrate-exhaustive or replaced. Open question OQ-2 lives here.
- **Block D.** The multiplicity-cap function $M$. The substrate-determined relationship between system multiplicity load, gradient sparsity, architectural-class protection mechanism, and the integrity of $\mathcal{U}$. Cross-anchor consistency (matter-wave Q-C boundary, Hafezi multi-timescale, SC-qubit fault-tolerance curves, topological-qubit progress) is the falsifiability condition. Predictive content is delivered here, not earlier.

The arc proceeds A → B → C → D. We do not write Block C memos until Block A's UR-1 closes and Block B's failure modes are quantified. We do not write Block D until Block C's architectural exhaustiveness is settled. Otherwise we risk deriving consequences from undecided premises.

**Decomposition II — Class × failure mode produces a 3 × 3 matrix.**

For any architectural class $K \in \{A, B, C\}$ and any failure mode $F \in \{F1, F2, F3\}$, there is a class-specific substrate scaling $M_{K,F}$. The full multiplicity-cap function is the envelope over the 3 × 3 matrix. This decomposition is provisional pending Block C's exhaustiveness audit.

### 2.5 The first theorem-shaped object: UR-1

> **UR-1 (Unresolved-Regime Characterization Theorem; statement of target, not yet proved).** A substrate region $\mathcal{S}$ is in the unresolved regime — i.e., admits $\mathcal{U}(\mathcal{S},t) \approx 1$ for some specified set of participation-rule endpoints — if and only if:
>
> (i) *Multiplicity is bounded.* $\mathcal{M}(\mathcal{S}) \leq \mathcal{M}_\mathrm{crit}$ for some substrate-determined threshold $\mathcal{M}_\mathrm{crit}$;
>
> (ii) *Cross-endpoint cross-bandwidth is sustained.* $\Gamma_\mathrm{cross}(\mathbf{x}) \geq \Gamma_\mathrm{min}$ for all $\mathbf{x}$ on the engineered participation pathways between designated endpoints;
>
> (iii) *Commitment-injection is below the individuation rate.* The rate of ED-injection from environment plus accumulated P11 commitments inside $\mathcal{S}$ is below the substrate-determined individuation threshold.
>
> Failure of any of (i)–(iii) drives $\mathcal{U} \to 0$ at a rate determined by which condition fails and by how much.

UR-1 is the gate condition for the arc. Until UR-1 is derived from substrate primitives — with the thresholds in (i), (ii), (iii) expressed in terms of the substrate quantities $\mathcal{M}$, $\sigma$, $\Gamma_\mathrm{cross}$, V1-kernel-mediated correlations, and P11 commitment density — no failure-mode rate, no architectural-class scaling, and no multiplicity-cap function can be honestly stated.

UR-1 is theorem-shaped because:

- It states necessary-and-sufficient substrate conditions for a substrate-level regime, in terms of substrate-level quantities.
- It admits a derivation chain: (i) from ED-I-01 + ED-I-23 (multiplicity-as-entropy + low-$\mathcal{M}$ engineering); (ii) from BH-2 + Arc D (decoupling-surface mechanism); (iii) from ED-10 §7.4 + Theorem 18 + P11 + ED-I-29 (thin-participation regime + commitment-irreversibility + tunneling-as-reconfiguration).
- It is falsifiable: a substrate region satisfying (i)–(iii) but not maintaining $\mathcal{U} \approx 1$, or maintaining $\mathcal{U} \approx 1$ while violating one of (i)–(iii), would refute the theorem.

The honest-framing question is whether UR-1's three conditions are *independent* (each separately necessary) or *coupled* (one implies the others under substrate constraints). That is part of OQ-3.

### 2.6 Working invariants / definitions list

| Symbol | Meaning | Status | Source |
|---|---|---|---|
| $\mathcal{M}(\mathcal{S})$ | Multiplicity (ED-entropy analogue) | DEFINED | ED-I-01 §2.3 |
| $\mathcal{U}(\mathcal{S},t) \in [0,1]$ | Participation-rule unresolvedness | DEFINED | this memo §2.2 |
| $\sigma(\mathbf{x}) = \|\nabla\rho\|\ell_P^2/\rho_\mathrm{local}$ | Gradient sparsity | INHERITED | BH-2 |
| $\Gamma_\mathrm{cross} \sim \exp[-\alpha\sigma]$ | Cross-bandwidth between regions | INHERITED | DCGT, BH-2 |
| (F1) | Premature individuation | DERIVED | this memo §2.4, prior turn |
| (F2) | Cross-endpoint decoupling | DERIVED | this memo §2.4, prior turn |
| (F3) | Commitment-pressure cascade | DERIVED | this memo §2.4, prior turn |
| UR-1 | Unresolved-Regime Characterization | TARGETED | this memo §2.5 |
| $M_{K,F}$ | Class-K, failure-F scaling | NAMED | this memo §2.4 |
| $M(\cdot)$ | Multiplicity-cap function | NAMED, undefined | arc-level deliverable |

### 2.7 Open questions / blockers / dependencies

- **OQ-1 (load-bearing).** Functional form of $\mathcal{U}$ from substrate primitives. Required for UR-1 condition (iii) and for any quantitative failure-mode rate.
- **OQ-2.** Exhaustiveness of the three-class architectural decomposition. Are A, B, C the only substrate-allowed mechanisms for holding $\mathcal{U} \approx 1$ against failure modes (F1)–(F3)?
- **OQ-3.** Whether UR-1's conditions (i), (ii), (iii) are independent or coupled.
- **OQ-4.** Whether the multiplicity-cap function $M$ is one substrate object with class-projections, or three structurally distinct functions sharing boundary conditions.
- **OQ-5.** Whether the matter-wave Q-C boundary (Anchor 1) and the QC ceiling (Anchors 2–4) are projections of *the same* function or merely *related* functions sharing substrate machinery.
- **OQ-6 (new this memo).** Relationship between $\mathcal{M}$ and $\mathcal{U}$. Does low $\mathcal{M}$ structurally entail $\mathcal{U} \approx 1$ in the absence of injection, or are they independent dimensions of substrate state?

**No external blockers.** All substrate machinery required is in closed-arc inventory. **No external dependencies.**

---

## 3. Consequences for the Arc

1. **UR-1 is the gate condition.** No memo writing Block B failure-mode rates, Block C class scalings, or Block D's $M$ function will be drafted before UR-1 closes. If UR-1 has structural pieces that don't close, the arc's deliverables are conditional on whatever piece is INHERITED.

2. **The three-class decomposition is hypothesized, not premised.** Block C's first task is the exhaustiveness audit. A Class D — substrate-allowed mechanism not in {A, B, C} — would refute the provisional decomposition and force its replacement. We will not bake the three-class structure into Block A or Block B.

3. **The matter-wave Q-C boundary is the program's existing empirical anchor.** Whatever $M$ ends up looking like, it must reproduce 140–250 kDa as the molecular-mass projection. This is a hard consistency check, not a tunable fit. If $M$ does not reproduce it, $M$ is wrong.

4. **The relationship between $\mathcal{M}$ and $\mathcal{U}$ matters at Block A.** If $\mathcal{U}$ is not independent of $\mathcal{M}$ — if low $\mathcal{M}$ structurally entails $\mathcal{U} \approx 1$ in the unresolved regime — then UR-1 simplifies and Block A is one definition shorter. If they are independent, UR-1 carries condition (iii) separately. OQ-6 is therefore load-bearing for UR-1's final form.

5. **Verdict-class projection.** Form-FORCED on UR-1, the failure-mode taxonomy, and the multiplicity-cap function's general shape. Value-INHERITED on the specific numerical thresholds ($\mathcal{M}_\mathrm{crit}$, $\Gamma_\mathrm{min}$, individuation-rate scale, the matter-wave Q-C boundary's exact value, and class-specific ceilings). The arc will not promise more than substrate machinery delivers.

6. **What this arc is not.** Not an engineering survey of QC platforms. Not a critique of any company's roadmap. Not an investment thesis. Not a Hawking-style spectrum derivation (that's Arc B4 / next-natural-arc-after-BH; it sits separately on the priority list). The deliverable is the substrate-level structural account of QC and its limits, plus whatever falsifiable predictive content the substrate machinery actually forces.

---

## 4. Recommended Next Step

**Memo 2 — Derive UR-1 (Unresolved-Regime Characterization Theorem) from substrate primitives.** Equivalently: derive the functional form of $\mathcal{U}(\mathcal{S},t)$ from $\mathcal{M}$, $\sigma$, $\Gamma_\mathrm{cross}$, V1-kernel-mediated correlations, and P11 commitment density.

File: `theory/Quantum_Computing/Arc_QC_2_UR1_Unresolved_Regime_Characterization.md`.

Scope:

- Construct $\mathcal{U}$ from substrate primitives. Identify which substrate quantities are load-bearing and which are subleading.
- State the boundary conditions: $\mathcal{U} \to 1$ in the thin-participation pre-commitment regime (Phase-1 + ED-10 §7.4); $\mathcal{U} \to 0$ in the thick-classical regime (BH-3-style saturated participation); smooth interpolation between, with the interpolation shape forced by substrate mechanics.
- Derive UR-1's three conditions from the substrate definitions; identify whether they are independent or coupled (closes OQ-3).
- Test UR-1 against three known regimes — bulk superconductor (ED-I-01), Josephson junction (ED-I-23), free atomic-scale matter wave — to confirm the substrate-conditions characterization picks them out correctly.
- Honest verdict on whether closed-form UR-1 is in hand or whether some piece is INHERITED.

Closes OQ-1 and OQ-3. Partially closes OQ-6 (will know whether $\mathcal{M}$ and $\mathcal{U}$ are independent dimensions). Sets up Block B (failure-mode quantification) directly.

Estimated 1–2 sessions.

If UR-1 closes cleanly, Memo 3 quantifies (F1)–(F3) failure-mode rates from UR-1's conditions. If UR-1 has structural pieces that don't close, Memo 3 is whatever the math exposes — we follow the substrate, not the plan.
