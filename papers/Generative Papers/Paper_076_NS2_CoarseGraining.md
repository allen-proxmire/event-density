# Paper 076 — NS-2: Substrate→Continuum Coarse-Graining Bridge

**Series:** Wave-2 Generative Papers (Navier–Stokes Arc, NS-2)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_073 (DCGT), Paper_075 (NS-1 dimensional forcing), Paper_089 (V1 kernel), Paper_077 (NS-3 smoothness).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a solution to the Clay Navier–Stokes problem; smoothness is addressed in Paper_077 (NS-3) at Intermediate Path C level.
2. It does **not** claim derivation of numerical viscosity coefficients from substrate primitives; viscosity is INHERITED via empirical matching.
3. It does **not** claim novel empirical predictions beyond standard incompressible Navier–Stokes.
4. It does **not** claim that NS captures all substrate-level continuum-flow phenomena; turbulence, viscoelasticity, MHD, etc. are addressed in separate arc papers.
5. It does **not** introduce new substrate primitives.
6. "Substrate→continuum coarse-graining bridge" means: a structural derivation of the incompressible NS equation $\partial_t u + (u \cdot \nabla) u = -\nabla p + \nu \nabla^2 u$, $\nabla \cdot u = 0$, as the DCGT coarse-graining of substrate participation-transport dynamics in the hydrodynamic-window regime.

---

## Abstract

Navier–Stokes is FORM-FORCED in ED as the DCGT coarse-graining of substrate participation-transport dynamics in the hydrodynamic-window regime. P02 (Participation) supplies the substrate-level transport carrier; P03 (Channel + locus indexing; spatial homogeneity) supplies the locus-level translation structure that descends to the Eulerian continuum velocity field $u(x,t)$; P10 (Rule-type primitive) supplies V1 as the substrate kernel whose second-moment finiteness produces the kinematic viscosity $\nu$ under coarse-graining; P11 (Commitment-irreversibility) supplies the dissipative structure. DCGT (Paper_073) supplies the bridge. The structural form of NS is FORCED; the numerical viscosity $\nu$ is INHERITED via empirical matching. The result feeds Paper_075 (NS-1 dimensional forcing — the seven PUA axioms are inherited from this bridge) and Paper_077 (NS-3 smoothness).

---

## §1 Introduction

The Navier–Stokes equation arises as the macroscopic limit of microscopic transport dynamics. Standard derivations (Boltzmann → Chapman–Enskog → NS) start from kinetic theory and produce NS at leading order in Knudsen number.

This paper supplies the substrate-level analog: NS arises as the DCGT coarse-graining of V1-modulated participation transport in the hydrodynamic-window regime. The substrate origin grounds NS-1's seven PUA axioms (Paper_075) and feeds NS-3 smoothness analysis (Paper_077).

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)** — substrate-level transport carrier (participation flow).
- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies translation structure descending to Eulerian $u(x,t)$.
- **P04 (Bandwidth)** — supplies additivity of transport contributions.
- **P10 (Rule-type primitive)** — supplies V1 kernel rule-type whose second moment produces viscosity.
- **P11 (Commitment-irreversibility)** — supplies dissipative structure.

### 2.2 Upstream dependencies

- **I-073:** DCGT (Paper_073) — substrate→continuum bridge.
- **I-089:** V1 kernel finite second moment (Paper_089).
- **I-013:** V1 QFT-arc form (Paper_013) — propagator-level V1 content used in convolution arguments.
- **I-075:** NS-1 dimensional forcing (Paper_075) — confirms $D = 3+1$ for the resulting PDE.
- **I-Hydro:** Standard hydrodynamic-limit machinery (standard math).
- **I-Chap:** Standard Chapman–Enskog expansion (standard math).

### 2.3 Paper-specific postulates

- **P-Hydro-Window:** The hydrodynamic-window regime $\ell_{V1} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ applies, where $\ell_{V1}$ is V1 width, $R_{\mathrm{cg}}$ is coarse-graining scale, $L_{\mathrm{flow}}$ is macroscopic flow scale.
- **P-Incompressibility:** The relevant substrate participation flow is incompressible at leading order: $\nabla \cdot u = 0$. (Compressible NS would require P-Compressibility instead.)
- **P-Newtonian-Stress:** The coarse-grained stress is Newtonian (linear in strain rate) at leading order. Non-Newtonian corrections are addressed in Paper_079 (P4-NN).

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | V1 kernel finite second moment | I | Paper_089. |
| 2 | DCGT hydrodynamic-window validity | I | Paper_073. |
| 3 | Hydrodynamic-window regime $\ell_{V1} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ | P-Hydro-Window | Regime postulate. |
| 4 | Substrate participation transport carrier from P02 | P | Primitive. |
| 5 | Eulerian velocity field $u(x,t)$ from P03 coarse-graining | D-via-I | Application of P03 translation structure + DCGT. |
| 6 | Incompressibility $\nabla \cdot u = 0$ at leading order | P-Incompressibility | Postulate. |
| 7 | Convective term $(u \cdot \nabla) u$ from second-order participation-flow coarse-graining | D-via-I | Application of standard Chapman-Enskog-style expansion (I-Chap) to substrate transport. |
| 8 | Newtonian stress $\sigma_{ij} = \nu (\partial_i u_j + \partial_j u_i)$ at leading order | P-Newtonian-Stress | Postulate. |
| 9 | Kinematic viscosity $\nu$ from V1 second moment + P11 dissipation | D-via-I | Application of standard kinetic-theory machinery to V1 + P11 content. |
| 10 | Pressure $p$ from incompressibility constraint | I | Standard hydrodynamic machinery (Lagrange multiplier on $\nabla \cdot u = 0$). |
| 11 | Navier–Stokes equation $\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu \nabla^2 u$ | D-via-I | Composition of steps 5–10. |
| 12 | Numerical value of $\nu$ for specific fluids | I | Empirical matching. |
| 13 | Compressible / non-Newtonian / non-isothermal corrections | OPEN | Addressed in other arc papers. |

---

## §3 The Derivation

### 3.1 Substrate transport setup

P02 supplies participation as the substrate-level transport carrier. P03 supplies channel/locus indexing with spatial homogeneity, on which a continuum velocity field $u(x, t)$ is defined at coarse-graining scale $R_{\mathrm{cg}}$.

By P-Hydro-Window, $R_{\mathrm{cg}}$ is large enough that V1 microstructure is averaged out, and small enough that continuum derivatives are well-defined.

### 3.2 Coarse-grained transport equation

DCGT (I-073) coarse-grains the substrate participation-transport equation to a continuum density-velocity equation. At leading order under P-Hydro-Window:
$$\partial_t \rho + \nabla \cdot (\rho u) = 0 ,$$
where $\rho$ is the coarse-grained participation density.

By P-Incompressibility, $\rho$ is constant at leading order, yielding $\nabla \cdot u = 0$.

### 3.3 Momentum equation

Coarse-graining the substrate momentum-transport equation under DCGT produces, at leading order:
$$\rho \left( \partial_t u + (u \cdot \nabla) u \right) = \nabla \cdot \sigma ,$$
with $\sigma$ the coarse-grained stress tensor.

The convective term $(u \cdot \nabla) u$ arises from second-order participation-flow coarse-graining via standard Chapman–Enskog-style expansion (I-Chap).

### 3.4 Newtonian viscosity from V1

P-Newtonian-Stress declares $\sigma_{ij} = -p\delta_{ij} + \nu (\partial_i u_j + \partial_j u_i)$ at leading order. The kinematic viscosity $\nu$ arises from the V1 second moment under DCGT:
$$\nu \sim \ell_{V1}^2 / \tau_{V1} ,$$
with $\tau_{V1}$ a substrate timescale set by P11 dissipation rate. The **scaling** is FORCED; the **numerical prefactor** is INHERITED.

### 3.5 Putting it together

Combining §3.2–§3.4:
$$\partial_t u + (u \cdot \nabla) u = -\nabla p + \nu \nabla^2 u , \quad \nabla \cdot u = 0 .$$

This is the incompressible Navier–Stokes equation. The FORM is FORCED by DCGT coarse-graining of V1-modulated participation transport under the declared postulates. The viscosity coefficient is INHERITED.

---

## §4 Feeding NS-1 (Paper_075)

The seven PUA axioms of Paper_075 (NS-1 dimensional forcing) are sketched in §5 of Paper_075 with substrate origins. This paper supplies the explicit substrate-level audit for each:

| PUA | Substrate origin (this paper) |
|---|---|
| PUA-1 (Locality) | V1 finite width → finite-order derivatives under coarse-graining (§3.3). |
| PUA-2 (Galilean covariance) | Acoustic-metric kinematic frame (Paper_017) at low-velocity limit. |
| PUA-3 (Energy method) | V1 second-moment finite → bounded $L^2$ dissipation (§3.4). |
| PUA-4 (Vorticity closure) | R1 mechanism (Paper_077) — autonomous vorticity equation on divergence-free phase space. |
| PUA-5 (Sobolev) | DCGT hydrodynamic-window (P-Hydro-Window) sets function-space scale. |
| PUA-6 (BKM) | V1 width $\ell_{V1}$ sets blowup-control scale. |
| PUA-7 (Finite energy) | Substrate-level chain count finite (P01 + P02). |

The substrate origins are **claims of inheritance**, not derivations in Paper_075. This paper (NS-2) is where the actual coarse-graining audit lives.

---

## §5 Open Structural Questions

- **O-NS2-1:** Quantitative derivation of $\nu$ from V1 kernel data (currently scaling only).
- **O-NS2-2:** Compressible-NS extension (would require P-Compressibility replacing P-Incompressibility).
- **O-NS2-3:** Non-Newtonian extension (Paper_079 P4-NN).
- **O-NS2-4:** Non-isothermal / thermal-coupled NS.
- **O-NS2-5:** Substrate-level derivation of pressure $p$ beyond Lagrange-multiplier (currently inherited).
- **O-NS2-6:** Connection to NS-3 smoothness (Paper_077) at the coarse-graining level.

---

## §6 Falsification Criteria

- **F1:** Demonstration that DCGT coarse-graining of V1-modulated participation transport does NOT produce NS form at leading order — refutes the substrate origin.
- **F2:** Demonstration that the convective term $(u \cdot \nabla) u$ does NOT arise from second-order substrate coarse-graining — refutes §3.3.
- **F3:** Demonstration that V1 second moment does NOT scale-set the kinematic viscosity — refutes §3.4.
- **F4:** Empirical detection of fluid flow inconsistent with NS in the P-Hydro-Window regime — propagates upward (and would also refute standard fluid mechanics).

---

## §7 Position Statement

Navier–Stokes is **FORM-FORCED** in ED as the DCGT coarse-graining of V1-modulated substrate participation-transport dynamics in the hydrodynamic-window regime, under P-Hydro-Window + P-Incompressibility + P-Newtonian-Stress. Viscosity $\nu$ is **scaled** from V1 second moment; numerical value INHERITED.

This supplies the substrate inheritance line for Paper_075's seven PUA axioms and feeds Paper_077 (NS-3 smoothness via R1 mechanism).

---

**End Paper 076 (FIXED).**
