# Paper 075 — Navier–Stokes: PDE Dimensional Forcing to D=3+1 (NS-1) — FIXED

**Series:** Wave-2 Generative Papers (Navier–Stokes Arc, NS-1)
**Status:** Conditional structural derivation given the seven PDE-uniqueness axioms declared in §2.3, plus inheritance from NS-2 (Paper_076). Substrate primitives invoked only indirectly via NS-2 inheritance.

**FIXED notes (2026-05-13):**
- §3 D-rows for dimensional-forcing arguments relabeled D-via-I: the new content is **application of standard PDE machinery to the declared PUA axiom set**; the standard PDE theorems themselves (Sobolev embedding, energy method, Galilean-group covariance) are I (inherited standard math).
- Legacy cross-reference "R.2.4 / spinor bundle structure" annotated as pre-pivot designation.
- "Flexibility & Correction Block" deleted; revision triggers folded into §6.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a solution to the Clay Navier–Stokes existence/smoothness problem.
2. It does **not** claim Navier–Stokes smoothness as derived; smoothness is addressed in NS-3 at Intermediate Path C level.
3. It does **not** claim that the seven PDE-uniqueness axioms are the **minimal** axiom set; only that they are jointly sufficient at FORM level.
4. It does **not** claim that $D = 3+1$ is forced by substrate primitives alone; forcing requires the seven PUA axioms.
5. It does **not** claim that ED reproduces Galilean / Lorentz / general-covariant frame structure as derived; these are layered on separately.
6. The result is a **PDE-level** dimensional-forcing claim, not a substrate-level forcing claim.

---

## Abstract

Under the seven PDE-uniqueness axioms (PUA-1 through PUA-7, §2.3), the dimensionality of the Navier–Stokes-class PDE system is forced to $D = 3 + 1$. The forcing argument applies **standard PDE machinery** (energy method, Sobolev embedding, scaling-critical-exponent analysis, Galilean-group structure) to the declared PUA axiom set. The standard machinery is I (inherited standard math); the **application to the PUA axiom set** is the new content (D). Substrate origin of the seven axioms is inherited from NS-2 (Paper_076).

---

## §1 Introduction

A long-standing observation: the seven standard PDE-uniqueness axioms for incompressible Navier–Stokes do not, individually, fix the spatial dimension. **Jointly**, they force $D = 3 + 1$.

This paper closes the B2 dimensional-forcing question regardless of NS-existence/smoothness ambition.

ED has produced FORCED-D=3+1 results via independent mechanisms at substrate-level (R.2.4 / spinor-bundle structure — pre-pivot designation; the corresponding canonical mechanism under Paper_087 is P06 spatial-dimension primitive). The substrate-level $D = 3+1$ via P06 and the PDE-level $D = 3+1$ via PUA are independent convergence routes.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked

This is a **PDE-level** paper. Substrate primitives are invoked only indirectly via inheritance from NS-2 (Paper_076). Paper_087's P06 (Spatial dimension primitive) supplies the substrate-level $D = 3+1$ result independently; this paper's PDE-level result is a separate convergence route.

### 2.2 Inherited closed-arc results

- **I-NS2:** Substrate→continuum bridge (Paper_076 / Arc D-DCGT) producing canonical NS-class equation form.
- **I-DCGT:** Diffusion Coarse-Graining Theorem (Paper_073).
- **I-Energy-Method:** Standard $L^2$ energy-identity machinery for divergence-free flows (standard math).
- **I-Sobolev:** Standard Sobolev-embedding theorems (standard math).
- **I-BKM:** Standard BKM blowup-criterion machinery (standard math).
- **I-Galilean:** Standard Galilean-group structure theory (standard math).

### 2.3 Paper-specific postulates (the seven PUA axioms)

- **PUA-1 (Locality):** NS-class PDE is differential of finite order in space and time.
- **PUA-2 (Galilean covariance):** Solutions transform covariantly under Galilean boosts.
- **PUA-3 (Energy-method admissibility):** PDE admits $L^2$ energy identity producing Gronwall-type bound on $\|u\|_{L^2}$.
- **PUA-4 (Vorticity-equation closure):** $\omega = \nabla \times u$ satisfies autonomous PDE on divergence-free phase space.
- **PUA-5 (Sobolev-embedding compatibility):** Well-posed in $H^s$ for $s > D_s/2 + 1$.
- **PUA-6 (BKM-criterion stability):** Blowup controlled by $\int \|\omega\|_{L^\infty}\, dt$; non-vacuous.
- **PUA-7 (Finite-energy IC class):** $\|u_0\|_{L^2} < \infty$ admissible.

Declared, not derived in this paper.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Seven PUA axioms | P | Paper-specific postulates. |
| 2 | NS-class PDE form inherited | I | Paper_076. |
| 3 | Hydrodynamic-window validity | I | Paper_073. |
| 4 | Spatial $D_s \geq 2$ from PUA-4 (vorticity non-trivial) | D-via-I | New content: applying PUA-4 to dimension question. The vorticity-curl-vanishing-in-$D_s=1$ argument is elementary linear algebra (I). |
| 5 | Spatial $D_s \leq 3$ from PUA-3 + PUA-5 | D-via-I | New content: applying axioms jointly. Standard energy-method + Sobolev-embedding scaling-critical exponent argument is I (I-Energy-Method + I-Sobolev). |
| 6 | Spatial $D_s = 3$ from PUA-5 + PUA-6 critical matching | D-via-I | New content: joint-axiom application. BKM-criterion machinery is I (I-BKM). |
| 7 | Temporal $D_t \geq 1$ from PUA-7 | D-via-I | Elementary IC-problem argument (I). |
| 8 | Temporal $D_t \leq 1$ from PUA-2 | D-via-I | New content: application to dimension question. Standard Galilean-group structure is I (I-Galilean). |
| 9 | Composite: $D = 3 + 1$ forced under PUA-1...PUA-7 | D | Composition of steps 4–8; composition is the new content. |
| 10 | Substrate origin of PUA axioms | I | Sketched in §5; inherited from Paper_076. |

The strengthened D-row rereading: each dimensional-forcing argument applies standard PDE machinery (I) to the declared PUA axiom set. The "D-via-I" label is the honest framing — application is new content, machinery is inherited.

---

## §3 The Spatial Dimensional Forcing

### 3.1 Lower bound $D_s \geq 2$ (from PUA-4) — D-via-I

PUA-4 requires $\omega = \nabla \times u$ to satisfy autonomous PDE on divergence-free phase space. In $D_s = 1$, curl vanishes identically (elementary linear algebra, I); vorticity equation collapses to $0 = 0$; autonomy violated.

**Application of elementary linear algebra (I) to PUA-4 yields $D_s \geq 2$ (D).**

### 3.2 Upper bound $D_s \leq 3$ (from PUA-3 + PUA-5) — D-via-I

PUA-3 produces $L^2$ energy identity (using standard energy-method machinery I-Energy-Method):
$$\frac{d}{dt}\|u\|_{L^2}^2 + 2\nu \|\nabla u\|_{L^2}^2 = 0 .$$

PUA-5 requires well-posedness in $H^s$ with $s > D_s/2 + 1$. Standard Sobolev embedding (I-Sobolev) controls $u \cdot \nabla u$:
$$\|u \cdot \nabla u\|_{L^2} \leq C \|u\|_{H^s} \|\nabla u\|_{L^2} .$$

Critical Sobolev exponent for NS scaling: $s_c = D_s/2 - 1 < 1$ iff $D_s < 4$. Energy-method closure fails for $D_s \geq 4$.

**Application of I-Energy-Method + I-Sobolev (standard machinery) to PUA-3 + PUA-5 yields $D_s \leq 3$ (D).**

### 3.3 Exact forcing $D_s = 3$ (from PUA-5 + PUA-6 critical matching) — D-via-I

Both $D_s = 2$ and $D_s = 3$ admissible under §3.1–§3.2. PUA-6 (BKM-criterion non-vacuous) discriminates:

- $D_s = 2$: energy method subcritical; BKM criterion vacuous (blowup never occurs). PUA-6's content collapses.
- $D_s = 3$: energy method critical; BKM non-vacuous; vorticity-stretching active.

PUA-6 requires non-vacuous criterion. Standard BKM machinery (I-BKM) applied to PUA-6 forces $D_s = 3$.

**Application of I-BKM to PUA-5 + PUA-6 yields $D_s = 3$ (D).**

---

## §4 The Temporal Dimensional Forcing

### 4.1 Lower bound $D_t \geq 1$ (from PUA-7) — D-via-I

$D_t = 0$ means no time variable; PDE collapses to constraint equation; IC class empty. **Elementary argument (I) applied to PUA-7 yields $D_t \geq 1$ (D).**

### 4.2 Upper bound $D_t \leq 1$ (from PUA-2) — D-via-I

Standard Galilean-group structure (I-Galilean): $\mathrm{Gal}(D_s, D_t = 1)$ has $D_s$ boost generators. With $D_t = 2$, natural generalization has $2 D_s$ generators; equation-of-motion convective-derivative form invariance breaks.

**Application of I-Galilean to PUA-2 yields $D_t = 1$ (D).**

### 4.3 Exact value

Combining: $D_t = 1$.

---

## §5 Substrate Origin of PUA-1...PUA-7 (Inheritance Sketch)

Substrate origin inherited from Paper_076 (NS-2). Sketch:

| PUA | Substrate origin |
|---|---|
| PUA-1 (Locality) | V1 kernel finite width (Paper_089) |
| PUA-2 (Galilean covariance) | Acoustic-metric kinematic frame (Paper_017) at low-velocity regime |
| PUA-3 (Energy method) | V1 second-moment finite (Paper_089) |
| PUA-4 (Vorticity closure) | R1 mechanism (Paper_076) |
| PUA-5 (Sobolev) | DCGT hydrodynamic window (Paper_073) |
| PUA-6 (BKM) | V1 finite width sets blowup-control scale (Paper_089) |
| PUA-7 (Finite energy) | Substrate-level chain count finite (P01 Chains, P02 Participation per Paper_087) |

Each line is a **claim of origin**, not a derivation in this paper.

---

## §6 Open Structural Questions

- **O-NS1-1:** Minimality of the seven PUA axiom set.
- **O-NS1-2:** Substrate derivation of PUA-2 Galilean covariance at quantitative level.
- **O-NS1-3:** Extension to compressible NS (additional thermodynamic PDE).
- **O-NS1-4:** Extension to MHD.

**Revision triggers:**
- If subset of PUA suffices, audit table strengthens.
- If PUA-2 is derived quantitatively, §4.2 strengthens.
- If compressible-NS extension shifts forcing, §3–4 require revision.

---

## §7 Falsification Criteria

- **F1:** PDE class satisfying PUA-1...PUA-7 in $D_s \neq 3$ — falsifies forcing claim.
- **F2:** Non-trivial NS-class theory in $D_t = 2$ with all PUA preserved.
- **F3:** PUA-5 + PUA-6 jointly admit $D_s = 2$ as non-vacuous.
- **F4:** NS-2's substrate→continuum bridge does not produce the seven PUA.

---

## §8 Position Statement

Under the seven PUA axioms PUA-1...PUA-7, NS-class PDE dimensionality is **FORCED** to $D = 3 + 1$. The seven axioms are **declared paper-specific postulates**; their substrate origin is inherited from Paper_076. The forcing arguments apply **standard PDE machinery** (I) to the declared axiom set; the application is the new content (D).

This closes the B2 dimensional-forcing question independently of NS-existence and NS-smoothness ambitions. It does **not** address the Clay NS problem.

PDE-level companion to ED's substrate-level $D = 3+1$ via P06. Multi-route convergence on $D = 3+1$ is itself a structural finding.

---

## Appendix — Why D=3 Specifically (Comparison Across Mechanisms)

| Mechanism | Source | Forcing level |
|---|---|---|
| P06 Spatial dimension primitive | Paper_087 canonical enumeration | Substrate-level (posited as primitive). |
| Spinor-bundle Cl(3,1) | R.2.4 (pre-pivot designation) | Substrate-level (legacy framing). |
| Acoustic-metric signature | Paper_017 / ED-Phys-10 | Coarse-grained kinematic. |
| PDE-uniqueness axioms (this paper) | PUA-1...PUA-7 | PDE-level. |

The four mechanisms agree on $D = 3+1$. None reduces to another; multi-route convergence is a structural finding.

---

**End Paper 075 (FIXED).**
