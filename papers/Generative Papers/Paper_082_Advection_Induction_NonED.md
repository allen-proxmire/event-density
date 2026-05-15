# Paper 082 — Advection-non-ED and Induction-Kinematic-non-ED Triangulation

**Series:** Wave-2 Generative Papers (Soft-Matter / NS-MHD Arc)
**Status:** Conditional structural analysis given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_016, Paper_030 (ED Combination Rule), Paper_031 (BTFR slope-4), Paper_075 (NS-1).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that advection / induction are wrong in standard NS/MHD; it claims they are **kinematic** (frame-artifact) rather than substrate-derived content.
2. It does **not** claim that the non-ED classification refutes standard NS or MHD predictions; it reframes their substrate-level status.
3. It does **not** introduce new substrate primitives.
4. "Non-ED" = at substrate level, the content is **transport-kinematic frame-artifact** (descending from the choice of coordinate frame in the coarse-graining), not substrate-derived.
5. "Triangulation" = three independent substrate-level arguments converging on the same non-ED verdict.

---

## Abstract

The advection term $(u \cdot \nabla) u$ in NS and the kinematic-induction term $\nabla \times (u \times B)$ in MHD are FORM-classified as **non-ED** (transport-kinematic frame-artifact) under triangulation by three independent arguments: (T1) **Paper_016 coarse-graining** — neither term arises from rule-type composition rules; both arise from coordinate-frame choice. (T2) **Paper_030 ED Combination Rule consistency** — substrate-gravity composition does not invoke advection-like cross-terms; analogous status. (T3) **Paper_075 PUA-2 Galilean-covariance** — both terms are Galilean covariant frame-artifacts of the convective derivative. The triangulation FORCES the non-ED classification.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)**, **P07 (Channel structure)**, **P10 (Rule-type primitive)**.

### 2.2 Upstream dependencies

- **I-016:** Non-Abelian rule-type composition (Paper_016).
- **I-030:** ED Combination Rule (Paper_030).
- **I-031:** BTFR slope-4 (Paper_031).
- **I-075:** NS-1 PUA-2 Galilean covariance (Paper_075).
- **I-076:** NS-2 substrate→continuum (Paper_076).
- **I-081:** NS-MHD closure (Paper_081).

### 2.3 Paper-specific postulates

- **P-Frame-Artifact:** Advection $(u \cdot \nabla) u$ and kinematic induction $\nabla \times (u \times B)$ are transport-kinematic frame-artifacts: they appear in the equations when transforming to a frame moving with the fluid, but the underlying substrate content carries them implicitly.

---

## §2.5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Paper_016 rule-type composition | I | Paper_016. |
| 2 | T1: advection / induction not from rule-type composition | D-via-I | Application of I-016. |
| 3 | ED Combination Rule (Paper_030) | I | Paper_030. |
| 4 | T2: no advection-like cross-term in substrate-gravity composition | D-via-I | Application of I-030. |
| 5 | PUA-2 Galilean covariance | I | Paper_075. |
| 6 | T3: advection / induction are convective-derivative frame-artifacts | D-via-I | Application of I-075. |
| 7a | P-Frame-Artifact declared | P | Postulate. |
| 7b | Non-ED verdict by triple convergence (T1 + T2 + T3) | D | Composition of D-via-I rows 2, 4, 6 gated by P-Frame-Artifact. |

---

## §3 The Triangulation

### 3.1 T1: Rule-type composition (Paper_016)

Paper_016 supplies the non-Abelian rule-type composition rules. Neither advection nor kinematic-induction terms arise from these composition rules — they are not substrate-level interaction terms but **coordinate-frame** terms.

### 3.2 T2: ED Combination Rule consistency (Paper_030)

The substrate-gravity ED Combination Rule $a = \sqrt{a_N \cdot a_0}$ does **not** involve advection-like cross-terms. By structural analogy (NOT D — A→analogy), advection in NS holds the same status: it appears in the equations of motion when coarse-graining to a moving frame, but the substrate composition rules do not contain it.

### 3.3 T3: Galilean covariance (Paper_075 PUA-2)

The convective derivative $D/Dt = \partial_t + u \cdot \nabla$ is Galilean covariant by construction. Standard analysis (I-075) shows that $(u \cdot \nabla) u$ and $\nabla \times (u \times B)$ are the standard frame-artifact terms appearing under Galilean covariance. They are **kinematic** (frame-dependent), not substrate-content.

### 3.4 Convergence

T1 + T2 + T3 converge on the **same non-ED classification**: advection and kinematic-induction are transport-kinematic frame-artifacts, not substrate-derived content. Standard NS/MHD predictions are unaffected; the substrate program's reframing is at the foundational level.

---

## §4 Falsification Criteria

- **F1:** Substrate-level rule-type composition demonstration of advection term — refutes T1.
- **F2:** ED Combination Rule extension showing advection-like cross-term substrate origin — refutes T2.
- **F3:** Galilean-covariance analysis showing advection is NOT a frame-artifact — refutes T3.
- **F4:** Any one of T1/T2/T3 surviving while the others fail — would force re-examination of the triangulation logic.

---

## §5 Position Statement

Advection and kinematic-induction are **FORCED non-ED** (transport-kinematic frame-artifact) by triple-convergence of T1 (rule-type composition) + T2 (ED Combination Rule consistency) + T3 (Galilean covariance). P-Frame-Artifact declared. Standard NS/MHD predictions unaffected.

---

**End Paper 082 (FIXED).**
