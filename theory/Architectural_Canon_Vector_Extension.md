# Architectural Canon — Vector / Tensor Extension Status

**Date:** 2026-04-30
**Status:** Canon-level clarification memo. **Headline: P-level architectural principles (P1–P7) are field-type agnostic; C5 ("single scalar field") in [`PDE.md`](PDE.md) is a constraint on the canonical PDE *exemplar*, not on the architectural canon. Vector and tensor field PDEs that satisfy P1–P7 component-wise (with shared or per-component constitutive functions) are architecturally ED. NS-2.08's "partial vector-extension" finding for Navier-Stokes sits cleanly within this framework: NS's viscous content is canonical ED vector-extended; the pressure-coupling, advective derivative, and incompressibility constraint are fluid-mechanical-specific structural additions that lie outside the canonical ED architecture but do not violate any P-level principle.**
**Sources:** [`Architectural_Canon.md`](Architectural_Canon.md) (P1–P7), [`PDE.md`](PDE.md) (C1–C7), [`Navier Stokes/NS-2.08_ED-PDE_Direct_Mapping.md`](Navier Stokes/NS-2.08_ED-PDE_Direct_Mapping.md), [`Navier Stokes/NS-2.07_Synthesis.md`](Navier Stokes/NS-2.07_Synthesis.md).

---

## 1. Purpose

NS-2.08's ED-PDE → Navier-Stokes mapping audit surfaced an unresolved structural ambiguity in ED's architectural canon: the canonical PDE in [`PDE.md`](PDE.md) imposes C5 ("single scalar field") as a binding constraint, while the architectural principles P1–P7 in [`Architectural_Canon.md`](Architectural_Canon.md) are stated using ρ throughout but do not explicitly forbid vector or tensor fields at the architectural level.

Three readings of this ambiguity were identified in NS-2.08 §3:

(i) **Strict.** C5 inherits at architectural level; vector extensions are not architecturally ED.
(ii) **Permissive.** P1–P7 are field-type agnostic; C5 is exemplar-specific; vector extensions architecturally ED if they satisfy P1–P7 component-wise.
(iii) **Articulation-required.** Canon is silent; vector extensions under-determined; explicit articulation required.

This memo resolves the ambiguity by ratifying reading (ii) and articulating the conditions under which vector/tensor field PDEs are "architecturally ED." It is a canon-level clarification, not a derivation; its purpose is to remove the gray area that NS-2.08 surfaced.

The motivating use case is NS itself: the chain-substrate route (NS-2.01–NS-2.07) and the ED-PDE-direct route (NS-2.08) both produce the standard Navier-Stokes form, with NS-2.08's mapping showing NS as a *partial* vector-extension of ED architecture. This memo provides the canon-level framework for that "partial" qualifier.

---

## 2. Inputs

| Input | Source |
|---|---|
| Architectural canon, principles P1–P7 | [`Architectural_Canon.md`](Architectural_Canon.md) §2 |
| Pre-PDE axioms A1–A4 (measure-theoretic layer) | [`Architectural_Canon.md`](Architectural_Canon.md) §1 |
| Compositional rule (cosmological specialization of A4) | [`Architectural_Canon.md`](Architectural_Canon.md) §1 |
| Canonical PDE constraints C1–C7 | [`PDE.md`](PDE.md) §3 |
| C5 (single scalar field) statement | [`PDE.md`](PDE.md) §3, table row C5 |
| NS-2.08 mapping memo's vector-extension construction | [`Navier Stokes/NS-2.08_ED-PDE_Direct_Mapping.md`](Navier Stokes/NS-2.08_ED-PDE_Direct_Mapping.md) §5 |
| NS-2 chain-substrate derivation result (standard NS form) | [`Navier Stokes/NS-2.07_Synthesis.md`](Navier Stokes/NS-2.07_Synthesis.md) §3 |
| NS-3 closure verdict (Intermediate Path C) | [`Navier Stokes/NS-3.04_Synthesis_Path_Verdict.md`](Navier Stokes/NS-3.04_Synthesis_Path_Verdict.md) §6 |

---

## 3. Audit of P-Level Architectural Principles

Each of P1–P7 is examined for field-type-specificity. The question for each: does the principle impose constraints that *require* the underlying field to be a scalar, or are its constraints field-type-agnostic (applicable to vector or tensor fields component-wise)?

### 3.1 P1 — Operator Structure

Principle statement: *the density field evolves under the nonlinear operator $F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)$.*

**Audit.** The operator's three terms each act on a single field at a time. For a vector field $v_i$ ($i = 1, 2, 3$ in d = 3 spatial), the component-wise generalization is:

$$F[v_i] = M_i(\cdot)\, \nabla^2 v_i + M'_i(\cdot)\, |\nabla v_i|^2 - P_i(v_i),$$

where the constitutive functions $M_i, P_i$ may depend on:
- the component itself (per-component),
- a shared scalar field (e.g., mass density $\rho_\mathrm{fluid}$ for fluid-mechanical applications),
- or both.

The three-term operator structure (curvature-dependent diffusion + nonlinear gradient coupling + restoring force) is preserved per component. **No P1-level scalar-specificity.**

**Verdict on P1: field-type agnostic.** Component-wise application preserves the three-term structure.

### 3.2 P2 — Channel Complementarity

Principle statement: *$\partial_t\rho = D\cdot F[\rho] + H\cdot v$, with $D + H = 1$, $D, H \in [0,1]$.*

**Audit.** The dual-channel (direct + mediated) structure applies per component:

$$\partial_t v_i = D \cdot F[v_i] + H \cdot u_i,$$

where $u_i$ is a participation variable (per-component or shared). The conservation $D + H = 1$ holds. **No P2-level scalar-specificity.**

**Verdict on P2: field-type agnostic.** Per-component dual-channel structure preserved.

### 3.3 P3 — Penalty Equilibrium

Principle statement: *$P$ has exactly one zero at $\rho = \rho^*$, with $P' > 0$. Equilibrium is unique and globally attracting.*

**Audit.** Per component, the penalty $P_i(v_i)$ has a unique equilibrium $v_i^*$ with $P_i' > 0$. The three components' equilibria may be:
- Identical (e.g., zero-flow equilibrium $v^* = 0$ for fluid at rest),
- Component-specific (different equilibria per component),
- Coupled (equilibrium of one component depends on others — non-canonical but conceivable).

For the standard fluid-mechanical case, the equilibrium is $v^* = 0$ for each component (fluid at rest), with $P_i$ functioning as a velocity-relaxation force that is structurally distinct from NS pressure-gradient (per NS-2.08 §4.2).

**No P3-level scalar-specificity.** Per-component application preserves uniqueness and global attraction.

**Verdict on P3: field-type agnostic.**

### 3.4 P4 — Mobility Capacity Bound

Principle statement: *$M(\rho_\mathrm{max}) = 0$ with $M(\rho) > 0$ for $\rho < \rho_\mathrm{max}$.*

**Audit.** Per component, $M_i$ vanishes at a maximum of its argument. For per-component arguments ($v_i = v_{i,\mathrm{max}}$), this would correspond to a maximum velocity per direction — which has physical meaning for fluids (sound speed, sonic transitions) but is unusual at NS scales. For shared-argument constitutive functions ($M$ depending on $\rho_\mathrm{fluid}$ or $|\nabla v|$), the capacity-bound applies to the shared field.

For NS, the natural reading is: $M(\rho_\mathrm{fluid})$ vanishes at $\rho_{\mathrm{fluid},\mathrm{max}}$ (incompressibility limit) or $M(|\nabla v|)$ saturates at high shear (yield-stress fluids). Both are physically meaningful and preserve P4 structure.

**No P4-level scalar-specificity.** Per-component or shared-argument structure preserves the capacity bound.

**Verdict on P4: field-type agnostic.**

### 3.5 P5 — Participation Feedback Loop

Principle statement: *$\dot v = (1/\tau)(F[\rho] - \zeta v)$, integrating the operator with exponential decay.*

**Audit.** Per component or shared participation variable. For a vector-extended ED PDE, two readings:
- **Per-component participation:** each $v_i$ has its own participation variable $u_i$ obeying $\dot u_i = (1/\tau_i)(F[v_i] - \zeta_i u_i)$.
- **Shared participation:** a single participation variable $u$ couples to all components, possibly through a shared $\bar F$ that aggregates over components.

Both are admissible at the P-level. NS standardly uses *external* forcing (gravity, etc.) rather than a participation-variable-class integrated feedback; NS forcing is therefore not *literally* a P5 instance, but the *role* (supplying global / non-local content) is parallel.

**No P5-level scalar-specificity.** Per-component or shared participation preserves the feedback structure.

**Verdict on P5: field-type agnostic.**

### 3.6 P6 — Damping Discriminant

Principle statement: *$(D - \zeta)^2 < 4(1 - D)$ ⟺ underdamped. Sharp transition at equality, $D_\mathrm{crit}(\zeta) \approx 0.896$ at canon-default $\zeta = 1/4$.*

**Audit.** The discriminant condition is dimensionless and depends on the dimensionless channel weight D and damping ζ. It applies per component (each component's dynamics is over- or underdamped according to its own (D, ζ) parameters) or globally (shared parameters across components → shared regime).

**No P6-level scalar-specificity.** Per-component or shared parameters preserve the discriminant structure.

**Verdict on P6: field-type agnostic.**

### 3.7 P7 — Nonlinear Triad Coupling

Principle statement: *the nonlinear term $M'(\rho)|\nabla\rho|^2$ generates higher-harmonic content with invariant amplitude ratio under multiplicative perturbations.*

**Audit.** Per component, the nonlinear $M'_i(\cdot)|\nabla v_i|^2$ term generates harmonic content per component. For shared-argument constitutive functions, the nonlinear term may couple components (e.g., $M'(\rho_\mathrm{fluid})|\nabla v_i|^2$ couples $v_i$'s harmonic content to $\rho_\mathrm{fluid}$'s field structure).

Coupling between components via the nonlinear term is a structural feature of vector extensions that does not arise in scalar instances; it is admissible at the P7 level (P7 specifies the existence and amplitude-ratio structure of harmonic generation, not the absence of inter-component coupling).

**No P7-level scalar-specificity.** Per-component nonlinear coupling preserves harmonic generation.

**Verdict on P7: field-type agnostic.**

### 3.8 Aggregate P-level audit

| Principle | Field-type-specific? | Generalization to vector/tensor |
|---|---|---|
| P1 (operator structure) | No | Component-wise three-term operator |
| P2 (channel complementarity) | No | Per-component dual-channel |
| P3 (penalty equilibrium) | No | Per-component or shared equilibrium |
| P4 (mobility capacity bound) | No | Per-component or shared-argument capacity |
| P5 (participation feedback) | No | Per-component or shared participation |
| P6 (damping discriminant) | No | Per-component or shared regime |
| P7 (nonlinear triad coupling) | No | Per-component, possibly inter-coupled |

**Net:** all seven P-level principles are **field-type agnostic**. Vector and tensor field PDEs satisfying P1–P7 component-wise (with appropriate constitutive structure) are architecturally consistent with the ED canon.

This ratifies reading (ii) of NS-2.08 §3.

---

## 4. Audit of C-Level Canonical PDE Constraints

### 4.1 C5 status

[`PDE.md`](PDE.md) §3 states C5 as: *"The state variable is one bounded scalar ρ ∈ [0, ρ_max] (no vector or tensor fields, no spinors)."*

This is a constraint on the *canonical PDE exemplar* — the specific instantiation written in PDE.md §1. C5 binds at the *concrete-PDE level*: any PDE that violates C5 is not the canonical PDE. But the architectural canon (P1–P7) is a meta-level statement defining a *class* of PDEs, and C5 is not among the architectural principles.

The relationship between layers, per [`Architectural_Canon.md`](Architectural_Canon.md) §0 / §8: PDE.md is "the concrete instantiation of the Canon using specific functional forms," and Architectural_Canon.md is "the architectural layer that explains why PDE.md has the structure it has." C5 is part of the concrete instantiation, not part of the architectural layer.

### 4.2 Why C5 does not forbid vector extensions at the architectural level

Three observations:

(a) **The architectural canon (P1–P7) does not include a "scalar-only" principle.** Per §3 above, the seven architectural principles are field-type agnostic in their content. No P-level commitment is violated by a vector or tensor extension.

(b) **C1–C7 are the canonical PDE's defining constraints, not the architectural canon's.** Architectural_Canon.md §5 lists what can vary (functional forms, parameter values, domain geometry, time rescaling) while preserving architectural ED-ness. The list does not explicitly mention field type, but the *content* of the seven principles' invariance is preserved under field-type generalization (per §3 above).

(c) **The compositional rule (cosmological specialization of A4) is not field-type-specific in its underlying structure.** It operates on density assignment $p(\cdot)$ over configurations of micro-events. The three correction terms (relational penalty, gradient penalty, boundary) are operations on density-class quantities; the canonical PDE exemplar specializes this to a single scalar field, but the underlying compositional architecture admits richer field structures.

**Verdict:** C5 is a constraint on the *canonical PDE exemplar* in PDE.md, not on the architectural canon. Vector and tensor field PDEs satisfying P1–P7 are architecturally ED even though they violate C5.

### 4.3 When would a new C-level extension be needed?

A new canonical PDE exemplar — say, a "vector ED PDE" or "tensor ED PDE" — would be appropriate if:

- A vector / tensor field PDE that satisfies P1–P7 has empirical or theoretical importance comparable to the scalar exemplar (e.g., NS for vector fields; some specific tensor PDE for elasticity or relativistic field dynamics).
- The vector / tensor exemplar admits a uniqueness theorem analogous to PDE.md §3's Theorem D.19 (the seven C-level constraints select PDE.md's specific form uniquely).
- Articulation of constitutive function families and parameter spaces is structurally non-trivial enough to warrant its own document.

For NS specifically: NS-2.08's analysis shows that NS is *partially* ED-architectural — viscous content maps cleanly; pressure / advection / incompressibility are fluid-mechanical-specific additions. **A "vector ED PDE" extension that includes NS as its paradigm case would also need to articulate the fluid-mechanical additions (pressure-Lagrange-multiplier, advective derivative, incompressibility constraint) as either canonical extensions or as fluid-specific structural additions outside the architecture.** Drafting such a C-level extension is a substantial articulation task; flagged as candidate future work, not pursued here.

---

## 5. Vector-Extension Conditions

Formal statement of conditions under which a vector PDE is architecturally ED.

### 5.1 Per-component P1–P7 obedience

A vector PDE on field $v_i$ ($i = 1, \ldots, n$) is **architecturally ED** if each component evolves under a P1–P7-compliant system:

$$\partial_t v_i = D_i \cdot F_i[v_i] + H_i \cdot u_i, \qquad D_i + H_i = 1,$$

with:
- $F_i[v_i] = M_i(\cdot)\, \nabla^2 v_i + M_i'(\cdot)\, |\nabla v_i|^2 - P_i(v_i)$ (P1).
- Each $P_i$ has a unique zero $v_i^*$ with $P_i' > 0$ (P3).
- Each $M_i$ vanishes at its argument's maximum (P4).
- Per-component or shared participation feedback obeying P5.
- (D, ζ) parameter regime determined by P6.
- P7 harmonic-generation structure preserved per component.

The constitutive functions $M_i, P_i$ may be:
- Per-component (independent per direction).
- Shared (single $M, P$ depending on a shared field like $\rho_\mathrm{fluid}$ or $|v|$).
- Mixed (some shared, some per-component).

### 5.2 Coupling-term structure

Inter-component coupling (when present) must respect the compositional rule's three-correction-term structure or be flagged as a fluid-mechanical-specific addition outside the architecture:

- **Compositional-rule-class couplings:** relational ($\alpha \int v_i^\gamma$ over overlap regions), gradient ($\beta \int |\nabla v_i|^2$), boundary ($\gamma \int h(|\nabla v_i|)$). These preserve the canonical architectural content.
- **Fluid-mechanical additions:** pressure-as-Lagrange-multiplier, advective convective derivative, incompressibility constraint. These are *not* derivable from P1–P7 + compositional rule. A vector PDE that includes them is partially ED-architectural (its compositional-rule-class content) plus fluid-mechanical-specific structure.

### 5.3 Participation channel — global or per-component

For vector extensions, participation can be:

- **Global participation:** single participation variable $u(t)$ coupling to all components via a shared $\bar F$ that aggregates (e.g., $\bar F = \sum_i F_i[v_i]$ or some aggregate).
- **Per-component participation:** each $v_i$ has its own $u_i(t)$ with independent dynamics.

Both are P-level admissible. The choice depends on physical context.

### 5.4 Aggregate

A vector PDE is **fully architecturally ED** if it satisfies §5.1 (per-component P1–P7) and §5.2 (compositional-rule-class couplings only) and §5.3 (admissible participation structure).

A vector PDE is **partially architecturally ED** if it satisfies §5.1 and §5.3 but adds fluid-mechanical-specific structure beyond compositional-rule-class couplings (per §5.2's fluid-mechanical-additions list).

The distinction matters: fully ED-architectural vector PDEs can be considered direct vector exemplars of the canon; partially ED-architectural ones (like NS) are recognized as having canonical content plus domain-specific additions.

---

## 6. NS as a Case Study

Per NS-2.08:

| NS structural feature | ED-architectural status |
|---|---|
| Viscous term $\mu \nabla^2 v_i$ | Canonical ED architecture vector-extended (mobility/gradient channel applied component-wise per §5.1) |
| Pressure gradient $-\nabla p$ (incompressible NS, Lagrange multiplier) | Fluid-mechanical addition; not native to ED PDE channels |
| Pressure gradient $-\nabla p$ (compressible NS, equation-of-state) | Constitutive relation; partially compositional-rule-relational-penalty-class but with fluid-specific equation-of-state structure |
| Advective convective derivative $(v \cdot \nabla) v$ | Fluid-mechanical addition; kinematic coupling between velocity components, not derivable from ED PDE channels |
| Incompressibility constraint $\nabla \cdot v = 0$ | Holonomic constraint; not derivable from ED architecture |
| External forcing $f^\mathrm{ext}$ (gravity from T19, EM from T17, etc.) | Participation-channel-class supplemented by ED-internal forcing structures (T17, T19) |
| Boundary conditions | Compositional-rule boundary term content (analogous in role) |

**Aggregate:** NS is *partially* architecturally ED — its viscous and forcing content is canonical ED architecture vector-extended; its pressure / advection / incompressibility content is fluid-mechanical-specific addition.

This is structurally valuable: NS sits within the canonical ED equation family for its viscous content (alongside porous-medium soft matter, RLC oscillation, cluster-merger lensing) while being fluid-mechanical-specific in its complete structure.

---

## 7. Architectural Verdict

### 7.1 Summary

**Vector and tensor field PDEs are permitted at the P-level architectural canon.** P1–P7 are field-type agnostic; their content generalizes to vector and tensor fields component-wise without violation.

**C5 in [`PDE.md`](PDE.md) §3 is a constraint on the canonical PDE exemplar**, not on the architectural canon. Vector / tensor PDEs that satisfy P1–P7 are architecturally ED even though they violate C5.

**NS is a partial vector-extension of ED architecture.** Its viscous content is canonical ED vector-extended; its pressure / advection / incompressibility content is fluid-mechanical-specific structural additions outside the canonical architecture but not in violation of any P-level principle.

**A C-level vector-PDE extension could be added** as a separate canonical exemplar in future work, with NS as its paradigm case. This would require articulating the fluid-mechanical-specific additions (pressure-Lagrange-multiplier, advective derivative, incompressibility) as either canonical extensions or as case-specific structural additions.

### 7.2 Three-tier classification

The verdict supports a three-tier classification of PDEs relative to the ED canon:

| Tier | Status | Examples |
|---|---|---|
| **Canonical** (PDE.md exemplar) | Satisfies C1–C7 (all C-level) and P1–P7 (architectural) | Porous-medium soft matter, cluster-merger penalty PDE, RLC participation oscillator |
| **Fully ED-architectural** | Satisfies P1–P7 with appropriate generalization (vector / tensor) but does not satisfy C5 (or another C-level constraint specific to PDE.md exemplar) | Hypothetical vector / tensor PDEs satisfying §5.1 + §5.2 + §5.3 |
| **Partially ED-architectural** | Satisfies P1–P7 component-wise but includes additional structural content (fluid-mechanical, etc.) not derivable from the ED architecture | **Navier-Stokes** (per NS-2.08); potentially Euler equation, magnetohydrodynamics, etc. |

This classification clarifies what "architecturally ED" means at different levels of strictness and provides language for placing future vector / tensor / mixed PDEs within the ED canon.

### 7.3 What this enables

The vector-extension verdict enables three kinds of program-level work:

- **Two-route concordance for NS** (NS-2 chain-substrate + NS-2.08 ED-PDE-direct) is now canon-supported. Both routes deliver the same NS form; the ED-PDE-direct route's vector-extension is architecturally legitimate.
- **Future canonical-extension memos** for specific vector / tensor PDEs of program interest. NS itself is a candidate paradigm case, with the fluid-mechanical-specific additions explicitly catalogued.
- **Programmatic clarity on what "ED-class equation" means** at architectural vs. canonical-PDE-exemplar level. The three-tier classification supports clearer external-facing material (papers, public explainers) about which physical equations sit where in the ED ecosystem.

---

## 8. Recommended Next Steps

In priority order. This memo is canon-level cleanup; the recommendations are program-level follow-on tasks.

1. **Update [`PDE.md`](PDE.md) §3 with clarifying note on C5.** Editorial pass; minimal change. Add a sentence clarifying that C5 is a constraint on the canonical PDE exemplar in PDE.md, not on the architectural canon (P1–P7), and pointing to this memo for the vector-extension framework. Recommended insertion: in PDE.md §3 below the C5 row, add a footnote-class sentence: *"C5 binds at the concrete-PDE level. The architectural canon (P1–P7 in [`Architectural_Canon.md`](Architectural_Canon.md)) is field-type agnostic; vector and tensor extensions of the ED architecture are addressed in [`Architectural_Canon_Vector_Extension.md`](Architectural_Canon_Vector_Extension.md)."* No content change to the canon; informational addition.

2. **Update [`Architectural_Canon.md`](Architectural_Canon.md) §5 with cross-reference to this memo.** Editorial pass. The existing list of "what can vary while preserving architectural ED-ness" should include or reference field-type generalization. Recommend: in §5's "What can vary" list, add a line about field-type extensions (per §3 of this memo) with a cross-reference to this document. Again, informational addition; no canon content change.

3. **Integrate NS-2.08 + this memo into the NS-2 synthesis paper as two-route concordance** (per NS-3.04 §9 recommendation). The synthesis paper's structure would now include:
   - Section 1: NS form derivation (chain-substrate route per NS-2.01–NS-2.07).
   - Section 2: NS form derivation (ED-PDE-direct route per NS-2.08).
   - Section 3: Two-route concordance + ED-PDE architecture vector-extension framework (this memo).
   - Section 4: NS-3 Path C verdict (Intermediate).
   This structure shows NS as both empirically-matched-to-standard-NS (chain-substrate route) and architecturally-ED-with-fluid-mechanical-additions (ED-PDE-direct route + vector-extension framework). Stronger synthesis paper than NS-2.07 alone proposed.

4. **Defer drafting a C-level vector-PDE extension** until program priorities surface a clear use case beyond NS. NS is a partial vector-extension that doesn't unambiguously call for a new canonical exemplar (its fluid-mechanical-specific additions aren't naturally absorbed into a "vector ED PDE" canonical form). Other candidate paradigm cases (MHD, relativistic fluids, elasticity tensor PDEs) might benefit from a C-level vector / tensor extension; flagged for `theory/Candidate_Architectural_Extensions.md` (referenced in NS-2.08 §8) as possible future work.

### Decisions for you

- **Confirm reading (ii) ratification.** The architectural canon (P1–P7) is field-type agnostic; C5 is exemplar-specific. Vector / tensor extensions architecturally ED if P1–P7 satisfied component-wise.
- **Confirm three-tier classification** (canonical / fully ED-architectural / partially ED-architectural) as program-level clarification language.
- **Confirm editorial passes** to PDE.md §3 and Architectural_Canon.md §5 with cross-references to this memo. Minimal changes; informational additions.
- **Confirm two-route concordance integration** in the NS-2 synthesis paper.

---

*Architectural Canon Vector / Tensor Extension memo. P1–P7 audited and verified field-type agnostic; C5 confirmed as canonical-PDE-exemplar-specific, not architectural; vector and tensor PDEs satisfying P1–P7 component-wise are architecturally ED. Three-tier classification (canonical / fully ED-architectural / partially ED-architectural) provides program-level clarity. NS placed as partially ED-architectural per NS-2.08. C-level vector-PDE extension deferred pending broader use case.*
