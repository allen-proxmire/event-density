# Paper 091 — Memory-Kernel Cascade Across Scales

**Series:** Wave-2 Generative Papers (Wedges Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_073 (DCGT), Paper_089 (V1), Paper_090 (V5).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of specific cascade transfer coefficients between V1 and V5 scales; coefficients are INHERITED via empirical matching.
2. It does **not** claim that all memory-kernel hierarchies are exhausted by V1/V5; higher-order kernels are addressed in Paper_092.
3. It does **not** introduce new substrate primitives.
4. "Memory-kernel cascade" = the multi-scale structure by which substrate-level kernels (V1 fast-retarded, V5 cross-chain finite-memory) produce coarse-grained effective kernels at successively larger scales under DCGT.

---

## Abstract

The substrate kernel hierarchy V1 (Paper_089) + V5 (Paper_090) generates a memory-kernel cascade across scales under DCGT (Paper_073): at scale $R \sim \ell_{V1}$, V1 dominates; at scale $\ell_{V5}$, V5 takes over; at coarse-grained scales $R_{\mathrm{cg}}$ in the hydrodynamic window, effective kernels inherit residual memory content from both. The cascade is FORM-FORCED by the substrate kernel structure + DCGT bridging; specific transfer relations are INHERITED via empirical matching. The result feeds Paper_092 (full hierarchy unification) and Paper_096 (cross-scale invariance).

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)**, **P10 (Rule-type primitive)** [V1, V5], **P11 (Commitment-irreversibility)**, **P13 (Time homogeneity)**.

### 2.2 Upstream dependencies

- **I-073:** DCGT (Paper_073).
- **I-089:** V1 finite second moment (Paper_089).
- **I-090:** V5 finite memory (Paper_090).

### 2.3 Paper-specific postulates

- **P-Kernel-Scale-Ordering:** Substrate kernel rule-types are scale-ordered: $\ell_{V1} \ll \ell_{V5}$ in physical regimes of interest, supporting a two-scale separation.
- **P-Cascade-Continuity:** Coarse-graining from V1-dominated to V5-dominated regime is continuous: no discontinuous transfer of memory-kernel content under DCGT.

---

## §2.5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | V1 finite second moment $\ell_{V1}^2$ | I | Paper_089. |
| 2 | V5 finite memory $\tau_{V5}$ | I | Paper_090. |
| 3 | DCGT hydrodynamic window | I | Paper_073. |
| 4 | Scale-ordering $\ell_{V1} \ll \ell_{V5}$ | P-Kernel-Scale-Ordering | Postulate. |
| 5 | Continuous cascade under coarse-graining | P-Cascade-Continuity | Postulate. |
| 6 | Effective kernel at scale $R$ inherits V1 + V5 content | D-via-I | Application of DCGT to V1 + V5. |
| 7 | Specific transfer coefficients | I | Empirical matching. |

---

## §3 The Cascade

### 3.1 Scale-ordered kernel content

By I-089 + I-090, V1 has width $\ell_{V1} \sim \ell_{\mathrm{ED}}$ and V5 has memory $\tau_{V5}$. By P-Kernel-Scale-Ordering, $\ell_{V1} \ll \ell_{V5}$ in standard regimes.

### 3.2 V1-dominated regime ($R \lesssim \ell_{V5}$)

At scales much smaller than the V5 memory scale, V5 contributions are integrated out; the effective kernel is dominated by V1 finite-width retarded structure.

### 3.3 V5-dominated regime ($R \gtrsim \ell_{V5}$)

At scales much larger than V5 memory but still in the hydrodynamic window ($R \ll L_{\mathrm{flow}}$), V5 cross-chain memory governs effective kernel structure.

### 3.4 Transition region

By P-Cascade-Continuity, the transition between regimes is smooth under DCGT: at $R \sim \ell_{V5}$, the effective kernel inherits residual content from both V1 (UV) and V5 (memory) at leading order.

### 3.5 Cascade structure

The cascade is FORM-FORCED by composition: substrate kernel structure (V1 + V5) + DCGT (Paper_073) + scale-ordering (P-Kernel-Scale-Ordering) jointly produce the effective kernel hierarchy at each coarse-graining scale. Specific transfer coefficients are inherited.

### 3.6 Cross-arc cascade equivalence

The memory-kernel cascade described above is structurally equivalent to the NS-Turb cascade (Paper_078) at a different scale-regime. Paper_078's P-Channel-Hierarchy partitions the P07 channel structure across the NS hydrodynamic window with energy transferred between channel-scales; this paper's P-Kernel-Scale-Ordering partitions the V1/V5 kernel hierarchy across the substrate→cosmological scale with correlation transferred between kernel-scales. Both cascades are scale-hierarchy phenomena under DCGT (Paper_073); both inherit from substrate scale separability; both produce inertial-range-like transfer with regime-specific transition exponents (Kolmogorov $k^{-5/3}$ in NS; canon-internal 0.6 in Wedges-RG, Paper_097). The two cascades occupy disjoint scale-regimes (hydrodynamic window vs substrate→cosmological window) but exhibit the same substrate-mechanism — scale-ordered transfer of substrate content under DCGT coarse-graining.

---

## §4 Falsification Criteria

- **F1:** Substrate evidence that V1 and V5 are NOT scale-separated ($\ell_{V1} \gtrsim \ell_{V5}$) — refutes P-Kernel-Scale-Ordering.
- **F2:** Discontinuity in coarse-grained kernel structure across cascade transition — refutes P-Cascade-Continuity.
- **F3:** Cascade-cross-scale measurements inconsistent with V1+V5 dual-kernel inheritance — refutes the cascade form.

---

## §5 Position Statement

The memory-kernel cascade across scales is **FORM-FORCED** in ED via V1 + V5 + DCGT under P-Kernel-Scale-Ordering + P-Cascade-Continuity. Transfer coefficients INHERITED. Feeds Paper_092 (full unification) and Paper_096 (cross-scale invariance).

---

**End Paper 091 (FIXED).**
