# Paper 022 — T17 C8 Substrate Gauge-Quotient (YM-5)

**Series:** Wave-2 Generative Papers (Yang–Mills Arc, YM-5)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_015 (T17), Paper_016 (polarity-connection match), Paper_019 (continuum YM), Paper_020 (OS-positivity), Paper_021 (mass gap), Paper_023 (YM Clay-relevance synthesis).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a solution to the Gribov problem; the substrate gauge-quotient is a definitional reframing, not a resolution of standard gauge-fixing ambiguity at constructive level.
2. It does **not** claim that the substrate gauge-quotient eliminates the need for BRST machinery in standard QFT computations; standard gauge-fixing is INHERITED.
3. It does **not** claim novel empirical predictions distinguishing the substrate gauge-quotient from standard gauge theory.
4. It does **not** introduce new substrate primitives.
5. "C8 substrate gauge-quotient" refers to clause C8 of the T17 theorem (Paper_015): the substrate-level quotient of rule-type bundle configurations by the gauge-orbit equivalence — i.e., physical states correspond to gauge orbits at the substrate level.

---

## Abstract

T17 (Paper_015) identifies gauge fields as connections on rule-type bundles. Clause C8 of T17 declares the substrate-level gauge-quotient: physical states are equivalence classes of substrate configurations under the rule-type-bundle automorphism group. This paper supplies the substrate audit of C8: the quotient is well-defined at the substrate level (every gauge orbit is a non-empty subset of substrate configurations), the quotient space carries the same Hilbert structure as the standard physical-state space, and standard gauge-fixing (BRST, Faddeev–Popov, Gribov region) appears as a coarse-graining of the substrate quotient. The "Gribov problem" — non-existence of a global gauge-fixing — is structurally reframed as a coarse-graining artifact, not a substrate-level obstacle.

---

## §1 Introduction

In standard non-Abelian gauge theory, the gauge-orbit space is topologically non-trivial; no global gauge slice exists (Gribov problem). Standard treatments use local gauge slices + BRST cohomology + ghost fields to manage the quotient.

T17 (Paper_015) embeds gauge fields as rule-type bundle connections. Clause C8 declares that the substrate-level physical-state space is the quotient by the rule-type-bundle automorphism group. This paper audits whether the substrate-level quotient is well-defined and identifies how standard gauge-fixing relates to the substrate quotient under coarse-graining.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)** — supplies substrate-level configuration content.
- **P07 (Channel structure)** — gauge-rule-type bundle.
- **P09 (U(1) polarity, extended non-Abelian via P10)** — gauge group fiber.
- **P10 (Rule-type primitive)** — rule-type bundle and automorphism group structure.

### 2.2 Upstream dependencies

- **I-T17:** T17 theorem (Paper_015) — gauge fields = rule-type bundle connections.
- **I-016:** Polarity-connection match (Paper_016).
- **I-019:** Substrate→continuum YM (Paper_019).
- **I-BRST:** Standard BRST cohomology machinery (standard math).
- **I-FP:** Standard Faddeev–Popov gauge-fixing (standard math).
- **I-Gribov:** Standard Gribov-region/horizon analysis (standard math).

### 2.3 Paper-specific postulates

- **P-Gauge-Orbit-Non-Empty:** Every gauge orbit (equivalence class of rule-type bundle configurations under bundle automorphisms) contains at least one substrate-level realization.
- **P-Quotient-Hilbert:** The quotient space inherits a Hilbert-space structure from the substrate Hilbert space (rule-type carrier states) consistent with standard physical-state Hilbert structure under coarse-graining.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | T17 supplies rule-type bundle | I | Paper_015. |
| 2 | T17 Clause C8 declares substrate gauge-quotient | P (T17 clause) | Definitional. |
| 3 | Rule-type bundle automorphism group | I | Standard fiber-bundle theory. |
| 4 | Every gauge orbit non-empty at substrate level | P-Gauge-Orbit-Non-Empty | Postulate. |
| 5 | Quotient space inherits Hilbert structure | P-Quotient-Hilbert | Postulate. |
| 6 | Substrate Hilbert space carries rule-type carrier states | I | Paper_007. |
| 7 | Quotient = substrate physical-state space | D-via-I | Application of standard fiber-bundle quotient theory to substrate. |
| 8 | Standard BRST = coarse-grained substrate quotient | D-via-I | Coarse-graining identification via DCGT (Paper_073). |
| 9 | Gribov ambiguity as coarse-graining artifact | A→position | Reframing claim, not constructive resolution. |
| 10 | Standard Faddeev–Popov machinery | I | Standard math. |
| 11 | Constructive resolution of Gribov problem | OPEN | Not claimed. |

---

## §3 The Substrate Quotient

### 3.1 The bundle automorphism group

Rule-type bundle automorphisms form a group $\mathcal{G}_{\mathrm{sub}}$ acting on substrate configurations. Two configurations are **gauge-equivalent** if related by a $\mathcal{G}_{\mathrm{sub}}$ element. Physical content (per T17 C8) is the equivalence class.

### 3.2 Non-emptiness and Hilbert structure

P-Gauge-Orbit-Non-Empty: every equivalence class is non-empty at substrate level. (This is non-trivial: it asserts the substrate admits enough configurations to populate every gauge orbit.)

P-Quotient-Hilbert: the quotient space $\mathcal{C}_{\mathrm{sub}} / \mathcal{G}_{\mathrm{sub}}$ inherits a Hilbert structure from the rule-type carrier Hilbert space (Paper_007).

Together, these supply a well-defined substrate-level physical-state space.

### 3.3 Coarse-graining to standard gauge theory

Under DCGT (Paper_073) + Paper_019's continuum YM construction, the substrate quotient coarse-grains to standard gauge theory's physical-state space. Standard gauge-fixing machinery (BRST, Faddeev–Popov) is a **coarse-graining tool** for computing inner products and matrix elements on the quotient — not a constructive operation at the substrate level.

### 3.4 The Gribov problem reframed

The standard Gribov problem — no global gauge slice exists — arises from attempting a smooth global section of the bundle of gauge orbits at the **coarse-grained** continuum level. At the substrate level, the quotient is well-defined (P-Gauge-Orbit-Non-Empty + P-Quotient-Hilbert); the Gribov ambiguity is a coarse-graining artifact, **not a substrate-level obstacle**.

This is an **A→position** claim: the reframing does not constructively resolve the Gribov problem at the constructive-QFT level. It supplies the substrate-level audit showing that the obstacle is coarse-graining-specific.

---

## §4 Distinguishing Definitional vs Derived

- **Definitional (P):** T17 Clause C8 itself; P-Gauge-Orbit-Non-Empty; P-Quotient-Hilbert.
- **Inherited (I):** Standard fiber-bundle quotient theory, BRST, Faddeev–Popov, Gribov-region analysis.
- **Derived (D-via-I):** Substrate quotient = substrate physical-state space; BRST = coarse-grained substrate quotient.
- **Position (A→position):** Gribov reframing.

The honest framing: ED does **not** newly resolve the Gribov problem at the constructive level; it supplies a substrate audit showing the obstacle is coarse-graining-specific.

---

## §5 Open Structural Questions

- **O-YM5-1:** Constructive derivation of P-Gauge-Orbit-Non-Empty from substrate combinatorics (would strengthen step 4 to D).
- **O-YM5-2:** Constructive resolution of Gribov problem at continuum level via substrate-derived quotient measure.
- **O-YM5-3:** Substrate audit of BRST cohomology = standard physical states.
- **O-YM5-4:** Substrate audit of large gauge transformations + theta-vacua.

---

## §6 Falsification Criteria

- **F1:** Demonstration of a gauge orbit that is provably empty at substrate level — refutes P-Gauge-Orbit-Non-Empty.
- **F2:** Demonstration that the substrate quotient does NOT inherit a Hilbert structure consistent with standard physical-state space — refutes P-Quotient-Hilbert.
- **F3:** Demonstration that BRST cohomology does NOT match the substrate quotient under DCGT — refutes the coarse-graining identification.

---

## §7 Position Statement

T17 Clause C8 (substrate gauge-quotient) is **definitionally** well-defined at substrate level under P-Gauge-Orbit-Non-Empty + P-Quotient-Hilbert. Standard gauge-fixing (BRST, FP, Gribov region) is identified as a coarse-graining tool for computing observables on the substrate quotient. The Gribov ambiguity is **reframed** (A→position) as a coarse-graining artifact, **not constructively resolved**.

This closes the YM-5 gap in the YM arc and feeds Paper_023's Clay-relevance synthesis.

---

**End Paper 022 (FIXED).**
