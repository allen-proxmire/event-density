# Paper 092 — Kernel Hierarchy Unification

**Series:** Wave-2 Generative Papers (Wedges Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_073 (DCGT), Paper_089 (V1), Paper_090 (V5), Paper_091 (kernel cascade).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that the kernel hierarchy is exhaustively V1 + V5; it claims a **unified scaffold** that V1, V5, and any future higher-order kernels fit into.
2. It does **not** claim novel empirical predictions beyond the constituent kernel papers.
3. It does **not** introduce new substrate primitives.
4. "Kernel hierarchy unification" = a single substrate-level framework that classifies all kernel rule-types by their characteristic scale, retardation order, and cross-chain rank.

---

## Abstract

Substrate kernel rule-types (Paper_089 V1, Paper_090 V5, plus any future higher-order $V_n$) are unified in ED under a single hierarchy parameterized by three indices: (i) **characteristic scale** $\ell_n$ (V1: $\ell_{\mathrm{ED}}$; V5: $\ell_{V5}$); (ii) **retardation order** $r_n$ (V1: first-order retarded; V5: extended memory); (iii) **cross-chain rank** $k_n$ (V1: within-chain; V5: pairwise cross-chain; higher kernels: $k$-chain). Under P-Hierarchy-Indexing and P-Hierarchy-Closure, every substrate kernel rule-type is classified by $(\ell_n, r_n, k_n)$. The unification is FORM-FORCED; specific kernel content INHERITED from Papers_089/090.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale)**, **P10 (Rule-type primitive)**, **P11 (Commitment-irreversibility)**, **P13 (Time homogeneity)**.

### 2.2 Upstream dependencies

- **I-073:** DCGT.
- **I-089:** V1 (Paper_089).
- **I-090:** V5 (Paper_090).
- **I-091:** Kernel cascade across scales (Paper_091).

### 2.3 Paper-specific postulates

- **P-Hierarchy-Indexing:** Every substrate kernel rule-type admits a classification by three indices: characteristic scale $\ell_n$, retardation order $r_n$, cross-chain rank $k_n$.
- **P-Hierarchy-Closure:** The kernel hierarchy is closed under DCGT coarse-graining: coarse-graining produces kernels within the same $(\ell_n, r_n, k_n)$ indexing.

---

## §2.5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | V1 substrate kernel | I | Paper_089. |
| 2 | V5 substrate kernel | I | Paper_090. |
| 3 | Three-index classification | P-Hierarchy-Indexing | Postulate. |
| 4 | Hierarchy closure under DCGT | P-Hierarchy-Closure | Postulate. |
| 5 | V1 at $(\ell_{\mathrm{ED}}, 1, 1)$ | D | Classification. |
| 6 | V5 at $(\ell_{V5}, \infty, 2)$ | D | Classification. |
| 7 | Higher-order $V_n$ kernels | OPEN | Not claimed exhaustive. |

---

## §3 The Hierarchy

### 3.1 Three indices

By P-Hierarchy-Indexing: each kernel has $\ell_n$ (characteristic scale), $r_n$ (retardation order — finite vs extended memory), $k_n$ (cross-chain rank — within-chain, pairwise, $k$-chain).

### 3.2 V1 placement

V1 (Paper_089) has $\ell_1 = \ell_{\mathrm{ED}}$, $r_1 = 1$ (first-order retarded), $k_1 = 1$ (within-chain). Classification: $(\ell_{\mathrm{ED}}, 1, 1)$.

### 3.3 V5 placement

V5 (Paper_090) has $\ell_5 = \ell_{V5}$, $r_5 = \infty$ (extended memory), $k_5 = 2$ (pairwise cross-chain). Classification: $(\ell_{V5}, \infty, 2)$.

### 3.4 Closure under DCGT

By P-Hierarchy-Closure, coarse-graining produces kernels within the same indexing scheme — no new index types appear. This is the closure content of the unification.

### 3.5 Higher-order kernels

Beyond V1 and V5, the hierarchy permits $V_n$ with various $(\ell_n, r_n, k_n)$. Whether such higher-order kernels are realized at substrate level is an OPEN question (not claimed exhausted by V1 + V5).

---

## §4 Falsification Criteria

- **F1:** Substrate evidence of a kernel rule-type not classifiable by $(\ell_n, r_n, k_n)$ — refutes P-Hierarchy-Indexing.
- **F2:** DCGT coarse-graining producing a kernel outside the indexing — refutes P-Hierarchy-Closure.
- **F3:** V1 or V5 classification mismatching the indices in §3.2–§3.3 — refutes the specific assignment.

---

## §5 Position Statement

Substrate kernel hierarchy is **FORM-FORCED-unified** under $(\ell_n, r_n, k_n)$ indexing per P-Hierarchy-Indexing + P-Hierarchy-Closure. V1 and V5 are placed. Higher-order kernels OPEN.

---

**End Paper 092 (FIXED).**
