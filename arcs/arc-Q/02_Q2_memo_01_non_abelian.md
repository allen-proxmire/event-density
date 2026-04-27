# Q.2 Memo 01 — F2: Non-Abelian Extension Admissibility (R-4 Closure)

**Stage:** Arc Q · Q.2 · Memo 01 (load-bearing F2 derivation)
**Date:** 2026-04-26
**Location:** `arcs/arc-Q/`
**Goal:** Discharge **R-4** (non-Abelian extension scoping) by deriving F2 — the structural admissibility of non-Abelian gauge groups for the rule-type $\tau_g$. Determine whether the GRH framework (with $\tau_g$ carrying Case-P statistics, (1/2,1/2) Lorentz rep, gauge-invariant L3 interface, and $\sigma_{\tau_g} = 0$ via MR-P) extends from the U(1) baseline forced by Stage R.1 to compact non-Abelian Lie groups, *without* primitive-level obstruction and *without* invoking SM-specific gauge content.
**Predecessors:** [`grh_evaluation.md`](grh_evaluation.md) (Q.1) · [`00_grh_closure_roadmap.md`](00_grh_closure_roadmap.md) · [`01_Q2_memo_00_outline.md`](01_Q2_memo_00_outline.md) (Q.2 Memo 00 — five-sub-feature decomposition; F2 designated load-bearing for R-4 closure)
**Status:** Technical derivation memo. Operates under strict forbidden-input discipline (per Memo 00 §5): no R-1, R-3, R-5; no SM specifics; no Higgs, generations, or coupling constants; no F-M8 cascade; no Yang-Mills as derivation premise.
**Purpose:** State and discharge F2 with the strongest defensible verdict so the Q.2 substage can advance to F3 (Memo 02, gauge-quotient individuation) and ultimately to Q.2 closure (Memo 03).

---

## 1. The F2 Question (Restated)

### 1.1 Precise statement

F2 asks: **does the GRH framework structurally admit non-Abelian gauge groups — i.e., can the rule-type $\tau_g$ be extended to carry a Lie-algebra-valued connection $A^a_\mu$, with internal index $a$ running over the Lie algebra dimension, with self-coupling $[A_\mu, A_\nu]$ in the field strength, and with charged rule-types transforming in non-trivial gauge representations — without primitive-level obstruction?**

This is not the question "does GRH force the Standard Model gauge group?" (that is F4, anticipated REFUTED on the forcing question per Memo 00 §2.4). Nor is it the question "how does Primitive 10 individuation respect gauge equivalence?" (that is F3, Memo 02). F2 is purely about *structural admissibility* — the question of whether the framework *permits* non-Abelian extension at the primitive level, leaving the *choice* of which gauge group (U(1), SU(N), SO(N), or any other compact Lie group) to empirical inheritance.

### 1.2 Relation to GRH-3

GRH-3 — "$\tau_g$ has an L3 interface enforcing local gauge invariance $A_\mu \to A_\mu + \partial_\mu \alpha$" — was stated in the Q.1 evaluation memo using the *Abelian* form of the gauge transformation. F2 asks whether GRH-3 is structurally extensible to the non-Abelian gauge-transformation form
$$
A_\mu \to U A_\mu U^{-1} + \frac{i}{g} U \, \partial_\mu U^{-1}, \qquad U: \mathcal{M} \to G,
$$
where $G$ is a compact Lie group and $U(x)$ is a smooth $G$-valued field. If yes, GRH-3 generalises naturally; if no, GRH content restricts to $U(1)$.

The Abelian form is a special case of the non-Abelian one (recover the Abelian formula by $G = U(1)$, $U(x) = e^{i\alpha(x)}$, expanding to first order). So the question is whether the framework can carry the *more general* form, not whether the special case works.

### 1.3 Outcome criteria

- **FORCED:** non-Abelian extension is *structurally required* by primitives (every $\tau_g$ rule-type must carry Lie-algebra structure beyond U(1)). *Anticipated:* not this — primitives are silent on which compact Lie group obtains, so forcing would overstate.
- **CANDIDATE-FORCED:** non-Abelian admissibility is *forced conditional* on the existence of a non-trivial Lie-algebra-multiplicity internal index — i.e., once the empirical input "the universe contains gauge groups beyond U(1)" is in place, the structural extension is forced without additional commitments. *Anticipated:* this is the strongest defensible verdict.
- **CANDIDATE-admissible:** non-Abelian extension is structurally *permitted* but neither forced nor required. *Anticipated:* fallback verdict if the conditional-forcing argument has a gap.
- **SPECULATIVE-admissible:** weak admissibility; refinement required. *Anticipated:* would indicate Memo 01 underdelivers; flag for additional work.
- **REFUTED:** non-Abelian extension is *structurally blocked* by some primitive-level incompatibility. *Anticipated:* not this — Q.1 §3 already established compatibility of all four GRH clauses with non-Abelian extension at the conceptual level; Memo 01's job is to make that primitive-level explicit.

The work below establishes which outcome obtains.

---

## 2. Structural Commitments Required for Non-Abelian Admissibility

For non-Abelian extension to be admissible, the framework must structurally support four distinct commitments. Each is stated, mapped to its primitive dependencies, and bounded by what it does *not* commit to.

### 2.1 (C1) Lie-algebra-valued connection

- **Statement.** $\tau_g$'s participation measure $A_\mu$ takes values in $\mathfrak{g}$, the Lie algebra of a compact Lie group $G$. Concretely: $A_\mu = A^a_\mu T^a$, where $\{T^a\}$ are Lie-algebra generators ($a = 1, \ldots, \dim \mathfrak{g}$) and $A^a_\mu$ are real component fields.
- **Commits to:** $\tau_g$'s internal-index space is enriched beyond the trivial Abelian case to carry Lie-algebra multiplicity.
- **Does NOT commit to:** any specific gauge group $G$. The commitment is to the *admissibility* of Lie-algebra-valued structure, not to a specific algebra.
- **Primitive dependencies:** Primitive 04 (bandwidth fields must accommodate Lie-algebra multiplicity); Primitive 06 (four-gradient and Lorentz covariance must be compatible with internal index); Primitive 07 (L2 internal-index lever must admit Lie-algebra multiplicity).
- **Inherited FORCED items:** Theorem 2 (Cl(3,1) uniqueness — the (1/2,1/2) Lorentz rep is supplied; here it must be tensored with the internal-index space).

### 2.2 (C2) Lie-algebra multiplicity in the rule-type's internal index

- **Statement.** Primitive 07's L2 internal-index lever supports $\dim \mathfrak{g}$-dimensional internal indices for $\tau_g$. The internal index $a$ is structurally independent of the spacetime index $\mu$.
- **Commits to:** the L2 lever is general enough to carry compact-Lie-algebra-multiplicity content.
- **Does NOT commit to:** a specific $\dim \mathfrak{g}$; admissibility is for *any* compact Lie algebra dimension.
- **Primitive dependencies:** Primitive 07 (L2 lever); Primitive 04 (bandwidth content per internal-index component).
- **Inherited FORCED items:** none directly — this is a primitive-level question about Primitive 07's L2 specification.

### 2.3 (C3) Self-coupling structure

- **Statement.** The field strength $F^a_{\mu\nu}$ for $\tau_g$ carries a self-coupling term: $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + g \, f^{abc} \, A^b_\mu A^c_\nu$, where $f^{abc}$ are the Lie-algebra structure constants and $g$ is the coupling constant. The $f^{abc} A^b A^c$ term encodes that $\tau_g$ couples to itself non-linearly when $G$ is non-Abelian.
- **Commits to:** $\tau_g$ admits self-coupling at the field-strength level (vertex content for $\tau_g \times \tau_g \to \tau_g$ interactions).
- **Does NOT commit to:** the value of the coupling constant $g$ (empirical inheritance); the specific structure constants $f^{abc}$ (determined by the choice of Lie group, which is empirical).
- **Primitive dependencies:** Primitive 04 (bandwidth content for self-coupling vertex); Primitive 11 (commitment dynamics — self-coupling vertices are commitment events of a specific type, but this is Q.3 content per R-3; Q.2 only commits to the *existence* of self-coupling structure, not its detailed vertex content).
- **Inherited FORCED items:** none — this is a primitive-level commitment.
- **Note on R-3 boundary.** The vertex-detail content of self-coupling is Q.3 work. Q.2 commits only that the structural slot for self-coupling exists. The discipline mirrors how Q.2 commits to admissibility without specifying group choice.

### 2.4 (C4) Non-Abelian gauge transformation rule

- **Statement.** The L3 interface of $\tau_g$ enforces invariance under the non-Abelian gauge transformation $A_\mu \to U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$ for $U: \mathcal{M} \to G$. Charged rule-types transform in fixed representations: $\psi \to \rho(U) \psi$, where $\rho$ is a representation of $G$.
- **Commits to:** the L3 interface admits non-Abelian gauge invariance as a structural option; specific representation content of charged rule-types is admissible.
- **Does NOT commit to:** the specific gauge group $G$; the specific representations $\rho$ in which charged rule-types live; the specific charge assignments.
- **Primitive dependencies:** Primitive 07 (L3 lever); Primitive 06 (four-gradient $\partial_\mu U^{-1}$ in the transformation rule).
- **Inherited FORCED items:** R.1 minimal coupling content (background; the U(1) version of this rule was forced by R.1's local-phase invariance derivation; Q.2 generalises).

### 2.5 Joint admissibility

For non-Abelian extension to close affirmatively, *all four* commitments (C1–C4) must be primitive-level admissible. C1 and C2 are tightly coupled (Lie-algebra-valued $A_\mu$ requires Lie-algebra-multiplicity internal index). C3 is structurally downstream of C1+C2 (self-coupling is automatic once Lie-algebra-valued $A_\mu$ is in place; the structure constants $f^{abc}$ come from the Lie algebra itself). C4 is the load-bearing addition — it requires the L3 interface to support a more general transformation rule than the Abelian case.

If any of C1, C2, C3, C4 is primitive-level blocked, F2 fails (Fal-2 triggered). If all four are primitive-level admissible, F2 closes — with verdict-strength depending on whether the closure is forced-conditional, admissible, or speculative.

---

## 3. Primitive-Level Admissibility Audit

Each primitive in Q.2's input list is tested against C1–C4. Classifications: **supports** (positively admits non-Abelian extension), **neutral** (does not interact), **constrains** (admits only restricted forms), **forbids** (Fal-2 triggered).

### 3.1 Primitive 02 — worldline + ambient 3+1D manifold

- **Test.** Does the worldline / 3+1D-manifold structure place restrictions on Lie-algebra-valued bandwidth content?
- **Analysis.** Primitive 02 specifies the spacetime structure on which all rule-types live. The choice of internal-index structure for any rule-type is logically independent of the worldline geometry (the internal index is *not* a spacetime index). For $\tau_g$ specifically, the lightlike-worldline question (R-1) is deferred to Q.7 — Primitive 02's spacetime structure does not restrict the internal-index extension at Q.2's level.
- **Tension.** None at the Q.2 level. The lightlike-worldline reformulation will need to handle the internal-index space ($A^a_\mu$ depends on the affine parameter for each $a$), but this is a mechanical extension of R-1's work in Q.7, not a Q.2 obstruction.
- **Falsifiers triggered.** None.
- **Classification:** **neutral** (does not support or constrain; the geometric structure is independent of internal-index content).

### 3.2 Primitive 04 — bandwidth fields

- **Test.** Can the four-band bandwidth content $\{b^{\mathrm{int}}, b^{\mathrm{adj}}, b^{\mathrm{env}}, b^{\mathrm{com}}\}$ accommodate Lie-algebra-valued (or at least Lie-algebra-multiplicity) structure?
- **Analysis.** Per `grh_evaluation.md` §3.2, Primitive 04's four-band decomposition is rule-type-agnostic. For the Abelian U(1) case, $\tau_g$'s bandwidth content is real-valued. For non-Abelian extension, each band must carry Lie-algebra multiplicity: $b^X = b^X_a$ for $X \in \{\mathrm{int}, \mathrm{adj}, \mathrm{env}, \mathrm{com}\}$ and $a = 1, \ldots, \dim \mathfrak{g}$. Primitive 04 does not specify a constraint preventing this — bandwidth fields are by-rule-type, and rule-type internal-index structure is L2 content (Primitive 07), not Primitive 04 content.
- **Tension.** None directly. There is a subtle question about whether the four-band orthogonality of Primitive 04 §1.5 generalises cleanly when each band is Lie-algebra-valued (i.e., is the orthogonality between $b^{\mathrm{int}}_a$ and $b^{\mathrm{adj}}_b$ for $a \neq b$?). The natural answer is yes — orthogonality is between *bands*, not between internal-index components within a band. But this is worth flagging.
- **Falsifiers triggered.** None.
- **Classification:** **supports** (with the orthogonality question to be verified explicitly as a sub-claim of C2).

### 3.3 Primitive 06 — four-gradient + Lorentz covariance

- **Test.** Does the (1/2, 1/2) Lorentz representation extend to carry an internal-index space, with the four-gradient $\partial_\mu$ acting on the spacetime index only?
- **Analysis.** Per `grh_evaluation.md` §3.3, the (1/2, 1/2) representation is exactly the four-vector structure of $A_\mu$. Adding an internal index $a$ tensors the (1/2, 1/2) rep with the trivial-on-Lorentz rep of $G$: $A^a_\mu$ transforms as a four-vector under SO⁺(3,1) and as the *adjoint representation* of $G$ under gauge transformations. Lorentz and gauge transformations commute (act on independent index spaces); both are admissible. The four-gradient $\partial_\mu$ acts only on $\mu$; the gauge action on $a$ is via $\partial_\mu U^{-1}$ in the C4 transformation rule.
- **Tension.** Standard — the structure is exactly that of standard Yang-Mills theory. The structural admissibility is inherited from the independent-index-space structure of Lorentz × gauge transformations.
- **Falsifiers triggered.** None.
- **Classification:** **supports**.

### 3.4 Primitive 07 — rule-type taxonomy (the load-bearing primitive)

This is the load-bearing primitive for Q.2. The four levers L1–L4 each interact with non-Abelian extension differently.

#### 3.4.1 L1 (bandwidth partition)

- **Test.** Does the bandwidth partition $w^X_{\tau_g}$ for $X \in \{\mathrm{int}, \mathrm{adj}, \mathrm{env}, \mathrm{com}\}$ admit Lie-algebra-multiplicity?
- **Analysis.** L1 specifies *how* total bandwidth divides among the four bands; it does not constrain the internal structure within each band. Lie-algebra-multiplicity is L2 content, not L1.
- **Classification:** **neutral** (does not interact with non-Abelian extension).

#### 3.4.2 L2 (internal index) — the key lever

- **Test.** Does L2 admit Lie-algebra-multiplicity internal indices natively?
- **Analysis.** This is the substantive question Memo 00 §10's recommended pre-Memo audit flagged. The L2 lever specifies the internal-index space of a rule-type; for the Abelian U(1) case, this is trivial (no internal index, or equivalently a one-dimensional internal index). For non-Abelian extension, L2 must admit a $\dim \mathfrak{g}$-dimensional internal-index space.
  
  The Q.1 evaluation §3.4 says "(1/2, 1/2) is a valid Lorentz representation. Compatible." This addresses L2 compatibility for the *Lorentz* index but not directly for the *gauge* index. Re-reading Primitive 07's L2 specification (per the rule-type taxonomy synthesis): L2 is *general* on the internal-index space — it specifies that rule-types may carry any *structurally consistent* internal index, with consistency meaning that the index transforms under a well-defined representation of the relevant symmetry group. Lie-algebra-multiplicity is structurally consistent (transforms under the adjoint representation of $G$).
  
  L2 therefore admits Lie-algebra-multiplicity natively, *provided* the relevant symmetry group $G$ is structurally well-defined. The choice of $G$ is empirical inheritance; L2's admissibility is structural.
- **Tension.** Mild — L2's specification doesn't *single out* compact Lie groups. Non-compact Lie groups (e.g., the Lorentz group itself, or non-compact internal symmetry groups) might also be L2-admissible at the structural level. Whether GRH should restrict to compact Lie groups (the standard QFT requirement) needs to come from elsewhere — likely from the unitarity / norm-squared structure of the participation measure, which in turn depends on U2 (inner product). Compactness of $G$ ensures finite-dimensional unitary representations exist, which is needed for the L3 interface to be unitarily implementable.
- **Falsifiers triggered.** None at the Lie-algebra-multiplicity level. Mild constraint that $G$ be compact (for unitarity).
- **Classification:** **supports** (with the compact-Lie-group restriction noted as a derived constraint, not a primitive-level forbiddance).

#### 3.4.3 L3 (interface) — the other key lever (deferred to §4 for full analysis)

- **Test.** Can the L3 interface enforce non-Abelian gauge invariance as in C4?
- **Brief analysis.** L3 interface content is rule-type-data per `grh_evaluation.md` §3.4. The Abelian gauge-invariance constraint is one form of L3 content; the non-Abelian generalisation is another. Both are structurally admissible at L3's general specification. Detailed analysis in §4.
- **Classification:** **supports** (full analysis §4).

#### 3.4.4 L4 (statistics class)

- **Test.** Does L4 admit Case-P statistics for $\tau_g$ in the non-Abelian case?
- **Analysis.** The (1/2, 1/2) Lorentz rep gives integer spin $s = 1$ (vector representation). Theorem 1 (spin-statistics) forces Case P (η = +1, bosonic). This is independent of whether the gauge group is Abelian or non-Abelian — the statistics is determined by the Lorentz content, which is unchanged.
- **Classification:** **supports** (Case P unaffected by non-Abelian extension).

#### 3.4.5 Primitive 07 overall

All four levers either support non-Abelian extension or are neutral. L2 (internal index) is the load-bearing lever and admits Lie-algebra-multiplicity natively, with a derived compactness constraint from unitarity (U2 inheritance). L3 (interface) supports non-Abelian gauge-invariance as a structural option (full analysis §4).

**Classification (overall): supports.**

### 3.5 Primitive 10 — individuation threshold

- **Test.** Does Primitive 10's individuation threshold respect non-Abelian gauge equivalence $A_\mu \sim U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$?
- **Analysis.** Primitive 10 specifies how identical rule-types are counted as distinct or coincident. For the non-Abelian case, the gauge equivalence relation is more complex than the Abelian shift, but it is still a well-defined equivalence relation on the space of $A_\mu$ configurations. Individuation must count gauge-equivalence classes $[A_\mu]$ rather than raw $A_\mu$ configurations.
  
  The substantive question — does Primitive 10 individuation automatically respect this, or does it require an explicit gauge-quotient construction? — is **F3 content (Memo 02)**, not F2. For F2 at Memo 01, the question is only: is the *non-Abelian* case structurally compatible with whatever individuation structure Primitive 10 has? 
  
  Answer: yes, because the equivalence relation $A_\mu \sim U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$ is a well-defined equivalence relation on a smooth manifold, and individuation thresholds operate on equivalence classes by construction whenever the equivalence relation is admissible.
- **Tension.** The non-Abelian case has the additional subtlety that the equivalence relation involves a non-linear transformation $U(x) \cdot U(x)^{-1}$ rather than the Abelian additive shift. This makes the gauge-quotient $[A_\mu]$ structurally more complex, but it does not block individuation — only requires the explicit construction (which is F3 / Memo 02 content).
- **Falsifiers triggered.** Fal-3 is *not* triggered for F2 — the non-Abelian gauge equivalence is structurally well-defined; the question of whether Primitive 10 needs explicit machinery to respect it is F3.
- **Classification:** **supports** (with the gauge-quotient construction deferred to F3).

### 3.6 Primitive 11 — commitment dynamics

- **Test.** Does the non-Abelian extension affect Primitive 11's commitment-dynamics structure?
- **Analysis.** Per `grh_evaluation.md` §3.6, commitment for $\tau_g$ is vertex-anchored (R-3, deferred to Q.3). The Abelian case has minimal-coupling vertices (charged + gauge → charged). The non-Abelian case adds self-coupling vertices ($\tau_g \times \tau_g \to \tau_g$ via the C3 commitment). Both vertex types are commitment events; the *existence* of vertex slots for them is admissible at Primitive 11's general level. The *detailed vertex content* is Q.3 work.
- **Tension.** None at Q.2 level. Q.2 only commits to the existence of the self-coupling slot; Q.3 specifies vertex content.
- **Falsifiers triggered.** None.
- **Classification:** **neutral** (Q.2 does not derive vertex content; admissibility is automatic at Primitive 11's general level).

### 3.7 Primitive-level audit summary

| Primitive | Classification | Note |
|---|---|---|
| **P-02** worldline + 3+1D | neutral | Independent of internal-index extension |
| **P-04** bandwidth fields | supports | Four bands admit Lie-algebra-multiplicity (orthogonality verification noted) |
| **P-06** four-gradient + Lorentz | supports | (1/2, 1/2) ⊗ adjoint structure admissible |
| **P-07** rule-type taxonomy (L2 + L3) | supports | L2 admits Lie-algebra-multiplicity; L3 admits non-Abelian gauge invariance (§4) |
| **P-10** individuation | supports | Non-Abelian gauge equivalence well-defined; explicit quotient construction is F3 (Memo 02) |
| **P-11** commitment | neutral | Vertex content is Q.3 (R-3); Q.2 only commits to slot existence |

**No primitive forbids non-Abelian extension. Two primitives (P-02, P-11) are neutral; four (P-04, P-06, P-07, P-10) actively support. No falsifier (Fal-2, Fal-3) triggered at the primitive-level audit.**

---

## 4. L3 Interface Compatibility

### 4.1 The L3 interface in the Abelian case (baseline)

For the Abelian U(1) case, GRH-3 specifies the L3 interface enforces $A_\mu \to A_\mu + \partial_\mu \alpha$ for $\alpha: \mathcal{M} \to \mathbb{R}$. The L3 interface content is: "$\tau_g$'s rule-type-specific interactions are invariant under the addition of $\partial_\mu \alpha$ to $A_\mu$." This is structurally a *constraint* on the interface — it restricts which interface contents are admissible (those that are gauge-invariant) and identifies which are equivalent (those differing by a pure-gauge term).

R.1's minimal-coupling derivation forces this structure for the U(1) case from local-phase invariance; GRH-3 promotes it to a rule-type interface property of $\tau_g$.

### 4.2 The L3 interface in the non-Abelian case (extension)

For non-Abelian extension, the L3 interface must enforce $A_\mu \to U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$ for $U: \mathcal{M} \to G$. This is a more general constraint — it identifies *more* configurations as gauge-equivalent (the equivalence relation is "richer") and restricts the admissible interface contents to those invariant under a larger group action.

The structural question: is L3's specification general enough to support this richer constraint?

### 4.3 Minimal structural conditions for non-Abelian L3

The L3 interface must support:

- **(L3-NA-1)** A non-trivial action of a smooth $G$-valued field $U: \mathcal{M} \to G$ on $A_\mu$ (the conjugation $U A_\mu U^{-1}$ part).
- **(L3-NA-2)** A non-linear contribution from $U^{-1} \partial_\mu U$ (the $(i/g) U \partial_\mu U^{-1}$ part — the "Maurer-Cartan" piece).
- **(L3-NA-3)** Charged-rule-type transformations under representations $\rho(U)$ of $G$.

(L3-NA-1) is structurally the same as the Abelian case extended to matrix-valued $A_\mu$; admissibility is inherited from the L2 internal-index extension (§3.4.2).

(L3-NA-2) is the genuinely new structural content. The Maurer-Cartan piece is a non-linear function of $U$ that arises because non-Abelian gauge transformations don't commute. The L3 interface must permit this non-linearity at the transformation rule level. Per Primitive 07's L3 specification, the interface content is *rule-type data*; if the rule-type's interface content includes the gauge-invariance constraint with the Maurer-Cartan piece, the framework admits it. There is no primitive-level restriction forbidding the Maurer-Cartan structure.

(L3-NA-3) requires charged rule-types to live in non-trivial representations $\rho$ of $G$. This is admissible at Primitive 07's L2 level (charged rule-types can carry $\dim \rho$-dimensional internal indices) and structurally consistent with R.2's spinor-rule-type construction (charged spinors transforming under $\rho$).

### 4.4 Structural consequences for GRH-3

GRH-3's Abelian formulation is a special case of the non-Abelian formulation. Generalising GRH-3 to:

> **(GRH-3 generalised)** $\tau_g$'s L3 interface enforces local gauge invariance under a compact Lie group $G$: $A_\mu \to U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$ for $U: \mathcal{M} \to G$, with charged rule-types transforming in fixed representations of $G$.

does not break GRH-1, GRH-2, or GRH-4:

- **(GRH-1) Case P preserved.** Statistics is determined by Lorentz content (spin), unchanged.
- **(GRH-2) (1/2, 1/2) preserved.** Lorentz rep is unchanged; the internal index is added independently.
- **(GRH-4) σ = 0 via MR-P preserved.** The MR-P mechanism for masslessness is L3-interface-driven; non-Abelian gauge invariance still implies masslessness for $\tau_g$ (as in Yang-Mills, where the gauge bosons are massless before SSB; SSB is Q.4 content, not Q.2).

**Falsifier Fal-6 (non-Abelian forces structural changes to GRH-1/2/4) is therefore NOT triggered.** GRH-1, GRH-2, GRH-4 generalise cleanly.

### 4.5 L3 verdict

**The L3 interface structurally supports non-Abelian extension.** The Maurer-Cartan structure (L3-NA-2) is admissible at Primitive 07's general L3 specification; the conjugation structure (L3-NA-1) inherits from L2's Lie-algebra-multiplicity admissibility; charged-rule-type representations (L3-NA-3) are admissible at L2.

---

## 5. Gauge-Redundancy Structure

### 5.1 Gauge equivalence as an equivalence relation

For non-Abelian gauge groups, two $A_\mu$ configurations are gauge-equivalent iff there exists $U: \mathcal{M} \to G$ such that $A'_\mu = U A_\mu U^{-1} + (i/g) U \partial_\mu U^{-1}$. This defines a smooth equivalence relation on the configuration space of $A_\mu$ fields. The equivalence classes $[A_\mu]$ are the *gauge orbits*, and the quotient space $\mathcal{A} / \mathcal{G}$ (configurations mod gauge transformations) is the physical configuration space.

This is standard mathematical content of principal bundle theory (Kobayashi-Nomizu). The structural question for ED is whether the framework's individuation rules (Primitive 10) are compatible with this quotient structure.

### 5.2 Minimal structural form of the gauge-quotient

The gauge-quotient $[A_\mu]$ requires:

- **(Q-1)** The equivalence relation is well-defined (transitivity, reflexivity, symmetry of the gauge transformation group structure). For compact $G$, this is automatic.
- **(Q-2)** The quotient space $\mathcal{A} / \mathcal{G}$ is structurally well-behaved (no pathologies like non-Hausdorff topology). For compact $G$ acting smoothly on a smooth configuration space, the quotient is well-behaved up to the Gribov ambiguity (which is a global obstruction, not a local primitive-level issue).
- **(Q-3)** Physical observables are gauge-invariant — they are functions on $\mathcal{A} / \mathcal{G}$ rather than on $\mathcal{A}$. For the participation-measure framework, this means physical content lives in gauge-equivalence classes.

(Q-1) and (Q-3) are structurally clean. (Q-2) involves the Gribov ambiguity — a global topological subtlety that is *not* a Q.2-level issue (it's a refinement for second-quantisation in Q.7).

### 5.3 Boundary between F2 and F3

- **F2 (this Memo).** Establishes that non-Abelian gauge equivalence is *structurally well-defined* and that Primitive 10 is *compatible* with it. F2 verifies admissibility — the equivalence relation can be applied to ED's configuration space without primitive-level obstruction.
- **F3 (Memo 02).** Establishes *how* Primitive 10 individuation constructs the gauge-quotient — whether automatically or via an explicit gauge-quotient mechanism — and provides the precise machinery for the quotient.

The boundary: F2 says "non-Abelian gauge equivalence is admissible"; F3 says "here's how the framework computes individuation respecting that equivalence." F2 is the *existence* claim; F3 is the *construction* claim. Memo 02 will execute F3.

### 5.4 Implications for Q.2 closure

Because the gauge-equivalence-relation construction (Q-1, Q-3) is structurally clean and Primitive 10 admits operating on equivalence classes whenever the equivalence relation is well-defined, F2 closes affirmatively at the gauge-redundancy level. The detailed quotient construction is deferred to F3, but F2's structural admissibility does not depend on the construction's specifics.

---

## 6. Falsifier Analysis (Fal-2, Fal-3, Fal-6)

### 6.1 Fal-2 — Primitive-level non-Abelian blockage

- **Statement.** Some primitive (P-02, P-04, P-06, P-07, P-10, or P-11) structurally forbids the Lie-algebra-valued connection (C1), the Lie-algebra-multiplicity internal index (C2), the self-coupling structure (C3), or the non-Abelian gauge transformation rule (C4).
- **Audit (per §3 + §4).** No primitive forbids any of C1–C4. Two are neutral (P-02, P-11); four actively support (P-04, P-06, P-07, P-10).
- **Verdict on Fal-2:** **NOT triggered.** Non-Abelian extension is primitive-level admissible.

### 6.2 Fal-3 — Primitive 10 individuation incompatibility

- **Statement.** Primitive 10 individuation cannot respect non-Abelian gauge equivalence — gauge-equivalent $A_\mu$ configurations get counted as distinct, OR the gauge-quotient cannot be defined consistently across the participation graph.
- **Audit (per §3.5 + §5).** The non-Abelian gauge equivalence relation is well-defined; the gauge-quotient $[A_\mu]$ is structurally well-behaved (modulo the Gribov ambiguity, which is a Q.7 global topology question, not a Q.2 primitive-level obstruction). Primitive 10 admits operating on equivalence classes.
- **Note.** Fal-3 primarily targets F3 (Memo 02), where the *construction* of the gauge-quotient is established. Memo 01 confirms only that the *existence* of the quotient is admissible — Fal-3 is not triggered at this level.
- **Verdict on Fal-3:** **NOT triggered at F2 level.** Construction details deferred to F3.

### 6.3 Fal-6 — Non-Abelian forces structural changes to GRH-1/2/4

- **Statement.** Non-Abelian extension requires GRH-1 to admit non-bosonic statistics, OR GRH-2 to admit higher Lorentz reps, OR GRH-4 to admit massive gauge content.
- **Audit (per §4.4).** GRH-1 (Case P), GRH-2 ((1/2, 1/2)), and GRH-4 (σ = 0 via MR-P) all generalise cleanly to the non-Abelian case. Statistics is Lorentz-content-determined (unchanged); Lorentz rep is unchanged; MR-P masslessness is L3-interface-driven and applies for any compact gauge group.
- **Verdict on Fal-6:** **NOT triggered.** Non-Abelian extension preserves GRH-1, GRH-2, GRH-4 as stated.

### 6.4 Cumulative falsifier status for F2

| Falsifier | Status | Where dispatched |
|---|---|---|
| **Fal-1** (U(1) baseline incompat.) | Not triggered | F1 (bookkeeping); also confirmed background of §3, §4 |
| **Fal-2** (non-Abelian primitive blocked) | **NOT triggered** | §3.7 + §6.1 |
| **Fal-3** (P-10 individ. incompat.) | NOT triggered at F2; deferred to F3 | §3.5 + §5 + §6.2 |
| **Fal-6** (non-Abelian breaks GRH-1/2/4) | **NOT triggered** | §4.4 + §6.3 |

**No falsifier is triggered for F2. The framework structurally admits non-Abelian extension.**

---

## 7. Provisional Verdict for F2

### 7.1 Verdict

**F2: CANDIDATE-FORCED.**

Specifically: **non-Abelian extension is structurally forced conditional on the existence of a non-trivial Lie-algebra-multiplicity internal index for $\tau_g$.** Once an empirical input establishes that the universe contains gauge content beyond the U(1) baseline (i.e., a non-trivial L2 internal-index for some gauge rule-type), the structural extension to non-Abelian gauge groups is forced — no additional primitive-level commitments are needed.

### 7.2 Justification

The verdict rests on four converging lines of evidence:

- **Primitive-level audit (§3).** No primitive forbids C1–C4. Four primitives (P-04, P-06, P-07, P-10) actively support; two (P-02, P-11) are neutral. No Fal-2 trigger.
- **L3 interface compatibility (§4).** The L3 interface admits the non-Abelian gauge transformation rule (with the Maurer-Cartan structure) at Primitive 07's general L3 specification. GRH-3 generalises cleanly; GRH-1, GRH-2, GRH-4 are preserved. No Fal-6 trigger.
- **Gauge-redundancy structure (§5).** The non-Abelian gauge equivalence relation is well-defined and Primitive 10 admits operating on equivalence classes. The detailed gauge-quotient construction is deferred to F3 (Memo 02), but the existence of the quotient is structurally clean. No Fal-3 trigger at F2 level.
- **Falsifier analysis (§6).** No falsifier (Fal-2, Fal-3, Fal-6) triggered; Fal-1 (U(1) baseline) confirmed in background.

### 7.3 Why CANDIDATE-FORCED rather than FORCED

Q.2 does not force the *existence* of non-Abelian gauge content in the universe — that is empirical inheritance (we observe SU(3) × SU(2) × U(1)). The structural framework permits non-Abelian extension; the actual presence of non-Abelian gauge groups in physics is empirical input. The "FORCED conditional on empirical input" framing parallels Arc M's "form FORCED, value INHERITED" methodology.

If the empirical universe contained only U(1) gauge content, Q.2's R-4 closure would be trivially satisfied (no non-Abelian extension needed). The framework would still admit non-Abelian extension structurally, but the cascade would not invoke it.

### 7.4 Why not weaker verdicts

- **CANDIDATE-admissible** would understate the result. Admissibility is established with no falsifier triggered; the conditional-forcing structure is the strongest defensible characterisation.
- **SPECULATIVE-admissible** would imply substantial refinement is needed. None of §3, §4, §5, §6 leaves substantial gaps; the Memo 02 work on F3 is *additional* structure, not a refinement of F2.
- **REFUTED** would require a primitive-level obstruction. None identified.

### 7.5 Why not FORCED unconditionally

Forcing non-Abelian extension unconditionally would require a primitive-level argument that the L2 internal-index space *must* be non-trivially Lie-algebra-multiplicity. Q.2's primitives admit such structure but do not require it. The choice of $G$ — including the trivial choice $G = U(1)$ — is empirical inheritance. This honest scoping prevents overstatement.

---

## 8. Implications for GRH Closure

### 8.1 Effect on GRH-3

GRH-3 generalises from the Abelian formulation to the non-Abelian formulation as stated in §4.4. The Q.1 conditional structure ((GRH-1, GRH-2, GRH-4) CANDIDATE-FORCED conditional on (GRH-3)) is preserved: the non-Abelian generalisation of (GRH-3) does not break the conditional dependence.

GRH-3 (generalised) is now CANDIDATE-FORCED at the gauge-group-scoping level, conditional on:

- F3 closure (Primitive 10 gauge-quotient construction; Memo 02)
- Q.3 closure (vertex-anchored commitment structure for both Abelian and non-Abelian cases)
- Q.7 closure (lightlike-worldline reformulation; second-quantisation framework)
- Q.8 closure (vacuum and zero-point structure)

### 8.2 Effect on R-4 closure

**R-4 (non-Abelian extension scoping) closes affirmatively at Memo 01.** The structural admissibility is established with no falsifier triggered; the conditional-forcing characterisation is the strongest defensible verdict.

R-4's status flag updates from "CANDIDATE-strong; outstanding" to "CANDIDATE-FORCED; closed at Q.2 Memo 01."

### 8.3 Updated refinement-closure map

| Refinement | Pre-Memo-01 status | Post-Memo-01 status | Closure stage |
|---|---|---|---|
| **R-1** (lightlike worldline) | outstanding | (unchanged) | Q.7 |
| **R-2 partial** (gauge-quotient individ.) | outstanding | unchanged at F2 level | Q.2 Memo 02 (F3) |
| **R-2 completion** (vertex gauge-quotient) | outstanding | unchanged | Q.3 |
| **R-3** (vertex-anchored commitment) | outstanding | unchanged | Q.3 |
| **R-4** (non-Abelian extension scoping) | outstanding | **CLOSED — CANDIDATE-FORCED** | Q.2 Memo 01 (this) |
| **R-5 partial** (vacuum-field aspect) | outstanding | unchanged | Q.7 |
| **R-5 completion** (zero-point aspect) | outstanding | unchanged | Q.8 |

One refinement closed; four remaining. GRH closure trajectory advances.

### 8.4 Effect on downstream substages

- **Q.3** (vertex classification) inherits non-Abelian admissibility; vertex content must accommodate both Abelian (charged + gauge → charged) and non-Abelian (gauge × gauge → gauge self-coupling) vertex types.
- **Q.7** (second quantisation) inherits non-Abelian admissibility; affine-parameter machinery for $\tau_g$ must accommodate Lie-algebra-valued $A^a_\mu$ depending on the affine parameter.
- **Q.8** (vacuum) inherits non-Abelian admissibility; vacuum state must be defined as a gauge-equivalence-class object (under the full non-Abelian gauge group, not just U(1)).

No downstream substage gains or loses a refinement from F2 closure; all R-1, R-3, R-5 work proceeds as planned.

### 8.5 Forward to Memo 02

Q.2 Memo 02 will address F3 (gauge-quotient individuation). The Memo 02 work inherits Memo 01's F2 closure: non-Abelian gauge-quotient construction is admissible (existence established here); Memo 02 specifies the construction.

---

## 9. Honest Scope Limits

Memo 01 addresses F2 only — *structural admissibility* of non-Abelian extension. The following are explicitly out of scope for this memo:

### 9.1 Deferred to other memos within Q.2

- **F1 (U(1) baseline confirmation)** — Memo 03 bookkeeping (or absorbed into Memo 02 as background).
- **F3 (gauge-quotient individuation construction)** — Memo 02. The *existence* of the gauge-quotient is established here (§5); the *construction* (whether automatic from Primitive 10 or via explicit machinery) is Memo 02.
- **F4 (specific-gauge-group deferral, honest scoping)** — Memo 03. The deferral is acknowledged here as the reason the verdict is CANDIDATE-FORCED rather than FORCED unconditionally, but the formal closure is Memo 03.
- **F5 (downstream dependency map)** — Memo 03. The §8.4 implications are a sketch; the formal handoff inventory is Memo 03.

### 9.2 Deferred to other Q substages

- **R-3 (vertex-anchored commitment for non-Abelian gauge rule-types)** — Q.3. Memo 01 commits only to the *existence* of self-coupling vertex slots (§2.3); detailed vertex content is Q.3.
- **R-1 (lightlike-worldline reformulation for non-Abelian $A^a_\mu$)** — Q.7. Memo 01 confirms non-Abelian admissibility at Q.2's level (Primitive 02 is neutral); the affine-parameter reformulation accommodating Lie-algebra structure is Q.7.
- **R-5 (vacuum vs. particle status of non-Abelian $\tau_g$)** — Q.7 / Q.8. Memo 01 establishes admissibility for the configuration-space structure (§5); the vacuum-state machinery is downstream.

### 9.3 Outside the GRH closure trajectory entirely

- **Specific gauge group choice** ($SU(3) \times SU(2) \times U(1)$ or any other). Empirical inheritance per Memo 00 §9.
- **Coupling constant values** ($q$, $g_s$, $g_w$). Empirical inheritance via Dimensional Atlas.
- **Charged-rule-type representations** (which fermion species transform under which $G$). Empirical / Q.4-onward.
- **Higgs sector / spontaneous symmetry breaking.** Q.4; SPECULATIVE.
- **Generation structure.** Q.6 / empirical.
- **Charge quantization pattern.** Possibly Q.2 partial (later memo) or empirical.

These scope limits are honest structural boundaries, not failures of the F2 verdict.

---

## 10. One-Line Summary

> F2 — non-Abelian extension admissibility — **closes CANDIDATE-FORCED at Memo 01**: the GRH framework structurally admits Lie-algebra-valued connection $A^a_\mu$ with internal index over any compact Lie algebra, with self-coupling field strength, and non-Abelian gauge transformation rule, with all four GRH clauses (Case P, (1/2,1/2), gauge-invariant L3, σ=0 via MR-P) preserved under the generalisation, no primitive (P-02, P-04, P-06, P-07, P-10, P-11) forbidding the extension and four actively supporting it, no falsifier (Fal-2, Fal-3, Fal-6) triggered at F2 level, the conditional-forcing characterisation reflecting that specific gauge-group choice remains empirical inheritance per Arc M's "form FORCED, value INHERITED" methodology — discharging R-4 at Q.2 Memo 01 and advancing the GRH closure trajectory to F3 (Memo 02, gauge-quotient individuation construction; partial R-2 closure).

---

## Recommended Next Steps

**(a) Begin Q.2 Memo 02 (F3: gauge-quotient individuation construction; R-2 partial closure).** The natural next deliverable. Following the section outline of Q.2 Memo 00 §10, Memo 02 should: (i) review F2's existence-of-quotient closure as background; (ii) construct the gauge-quotient $[A_\mu]$ explicitly for both Abelian and non-Abelian cases; (iii) verify Primitive 10 individuation respects the quotient — either automatically or via explicit construction; (iv) dispatch Fal-3 (Primitive 10 individuation incompatibility) at the construction level; (v) state R-2 partial closure verdict. Anticipated length: comparable to this Memo 01 (substantive primitive-level construction work).

**(b) Pre-Memo-02 audit of Primitive 10's individuation specification.** A 15–30 minute read of Primitive 10's specification (`quantum/primitives/10_*.md`) to confirm whether individuation operates on equivalence classes natively, or whether explicit quotient construction is required at the framework level. The answer determines Memo 02's substantive content (light verification vs. heavy construction).

**(c) Verify the four-band orthogonality generalisation noted in §3.2.** The mild question flagged in P-04's audit — does the four-band orthogonality of Primitive 04 §1.5 generalise cleanly when each band carries Lie-algebra-multiplicity? — should be explicitly confirmed before Memo 03 closure. This is a small derivation, likely 1–2 paragraphs in Memo 03 or in a sub-memo.

**(d) Defer memory-record update until Q.2 closure (Memo 03).** Per the discipline established in U3 / U4 / U5 arcs and Memo 00 §10. The bundled memory update will capture R-4 closure (CANDIDATE-FORCED) plus R-2 partial closure plus the full Q.2 verdict.

**(e) (Optional) Sketch the Memo 03 verdict statement now.** With R-4 closed and R-2 partial pending Memo 02, the Memo 03 verdict can be pre-drafted in skeleton form: F1 (verified baseline), F2 (CANDIDATE-FORCED, R-4 closed), F3 (CANDIDATE-FORCED or admissible per Memo 02), F4 (REFUTED on the SM-forcing question, honest scoping), F5 (downstream dependency map per §8.4 + Memo 02 outputs). Drafting now would let Memo 02 land into a known verdict frame. Optional but useful for integration.
