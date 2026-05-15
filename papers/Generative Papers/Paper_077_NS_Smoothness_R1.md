# Paper 077 — NS-Smoothness via R1 Mechanism (Intermediate Path C)

**Series:** Wave-2 Generative Papers (Soft-Matter / NS Arc, NS-3)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_075 (NS-1 dimensional forcing), Paper_076 (NS-2 substrate→continuum), Paper_084 (vortex-stretching obstruction), Paper_089 (V1), Paper_090 (V5).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a constructive proof of NS global smoothness in 3+1; the result is at the **Intermediate Path C** verdict level — structural-positive, not constructive.
2. It does **not** claim novel empirical predictions beyond standard NS regularity work.
3. It does **not** claim that R1 mechanism alone forces smoothness; the argument composes R1 dissipation + vortex-stretching obstruction (Paper_084) under declared postulates.
4. It does **not** introduce new substrate primitives.
5. "Intermediate Path C" = the verdict level (parallel to NS-MHD and YM-arc Clay-relevance verdicts) where structural mechanisms are identified but a constructive proof is not assembled.
6. "R1 mechanism" = the substrate-level dissipation route inherited from NS-2 (Paper_076): V1 finite second moment produces a kinematic viscosity that bounds enstrophy growth at sufficient strength.

---

## Abstract

NS global smoothness is FORM-supported at the Intermediate Path C verdict level in ED. The argument composes: (i) R1 substrate dissipation (Paper_076) producing kinematic viscosity bounded below by the V1 second moment; (ii) vortex-stretching obstruction (Paper_084) preventing unbounded enstrophy growth at the substrate level; (iii) Sobolev-embedding + BKM criterion (Paper_075 PUA-5 + PUA-6) supplying the standard regularity machinery. Under P-R1-Sufficient-Strength and P-Obstruction-Sufficient, the composition forces bounded BKM integral $\int \|\omega\|_{L^\infty}\, dt < \infty$ on finite time intervals. This is a **structural-positive** verdict, not a constructive proof: the postulates are declared, and a constructive derivation of either postulate is OPEN.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)** — substrate transport carrier.
- **P04 (Bandwidth)** — additive structure for enstrophy budget.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — width scale entering viscosity.
- **P10 (Rule-type primitive)** — V1 kernel.
- **P11 (Commitment-irreversibility)** — dissipative direction.

### 2.2 Upstream dependencies

- **I-075:** NS-1 PUA axioms (Paper_075).
- **I-076:** NS-2 substrate→continuum (Paper_076).
- **I-084:** Vortex-stretching obstruction (Paper_084).
- **I-089:** V1 second moment finite (Paper_089).
- **I-030:** ED Combination Rule (Paper_030, used as cross-check for substrate dissipation scaling).
- **I-031:** BTFR slope-4 (Paper_031, cross-check on substrate kinetic-viscosity scaling).
- **I-BKM:** Standard BKM blowup-criterion machinery (standard math).
- **I-Sobolev:** Standard Sobolev embedding (standard math).
- **I-Energy:** Standard energy-method machinery (standard math).

### 2.3 Paper-specific postulates

- **P-R1-Sufficient-Strength:** The R1 substrate-derived kinematic viscosity $\nu \sim \ell_{V1}^2/\tau_{V1}$ (Paper_076) is sufficient to bound enstrophy growth at the substrate level for finite time intervals.
- **P-Obstruction-Sufficient:** The vortex-stretching obstruction (Paper_084) is structurally sufficient to prevent BKM integral divergence under R1 dissipation.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | NS-1 PUA axioms | I | Paper_075. |
| 2 | NS-2 substrate→continuum | I | Paper_076. |
| 3 | V1 finite second moment | I | Paper_089. |
| 4 | Kinematic viscosity from V1 second moment | I | Paper_076. |
| 5 | R1 sufficient strength | P-R1-Sufficient-Strength | Postulate. |
| 6 | Vortex-stretching obstruction | I | Paper_084. |
| 7 | Obstruction sufficient | P-Obstruction-Sufficient | Postulate. |
| 8 | Energy method + Sobolev embedding | I | Standard math. |
| 9 | BKM criterion | I | Standard math. |
| 10 | Composition forces $\int\|\omega\|_{L^\infty}\, dt < \infty$ | D-via-I | Composition of postulates + standard machinery. |
| 11 | Global smoothness at Intermediate Path C verdict | A→position | Composite verdict. |
| 12 | Constructive proof of NS smoothness | OPEN | Not claimed. |

---

## §3 The Composition Argument

### 3.1 R1 dissipation

By Paper_076 NS-2, the substrate-derived NS equation has kinematic viscosity $\nu \sim \ell_{V1}^2/\tau_{V1}$. By I-089, $\ell_{V1}^2 < \infty$.

By P-R1-Sufficient-Strength, $\nu$ is bounded below by a positive constant on finite time intervals, supplying the L²-energy dissipation rate needed for the energy-method argument (I-Energy).

### 3.2 Vortex-stretching obstruction

By Paper_084, the substrate-level vortex-stretching mechanism is **obstructed**: cumulative substrate commitment (P04 bandwidth-additivity + P11 commitment-irreversibility) bounds the rate at which vorticity can amplify under stretching.

By P-Obstruction-Sufficient, this obstruction is structurally sufficient to keep $\|\omega\|_{L^\infty}$ bounded on finite intervals.

### 3.3 BKM closure

Standard BKM criterion (I-BKM): if $\int_0^T \|\omega(\cdot, t)\|_{L^\infty}\, dt < \infty$, then the solution is smooth on $[0, T]$.

By §3.1 + §3.2 + standard energy / Sobolev machinery (I-Sobolev, I-Energy), the BKM integral is finite on finite intervals. NS solutions are smooth.

### 3.4 Intermediate Path C verdict

The argument is **structural-positive**, not constructive:
- P-R1-Sufficient-Strength and P-Obstruction-Sufficient are declared, not derived quantitatively.
- The composition matches the Clay-target structural form (BKM closure under viscosity + obstruction) but does not constructively prove the postulates.

This is the same verdict level as YM-arc Clay-relevance (Paper_023) and Arc ED-10 conditional-positive (Paper_033).

---

## §4 Falsification Criteria

- **F1:** Constructive demonstration of a finite-time NS blowup — refutes P-Obstruction-Sufficient and the verdict.
- **F2:** Empirical (DNS) evidence that R1 substrate viscosity is insufficient for finite-time enstrophy bound — refutes P-R1-Sufficient-Strength.
- **F3:** Substrate evidence that vortex-stretching obstruction (Paper_084) fails at substrate level — propagates upward.

---

## §5 Position Statement

NS smoothness in 3+1 is **structurally supported at Intermediate Path C** verdict level: R1 dissipation (Paper_076) + vortex-stretching obstruction (Paper_084) + standard regularity machinery jointly force BKM closure under declared postulates. **Not constructive proof**; OPEN constructive derivations remain.

---

**End Paper 077 (FIXED).**
