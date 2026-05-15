# Paper 013 — V1 Finite-Width Retarded Vacuum Kernel (QFT-Arc Form)

**Series:** Wave-2 Generative Papers (QFT Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companion:** Paper_089 (V1 canonical reference, wedges arc). This paper supplies the QFT-arc-internal form of V1 — the propagator/Wightman-function presentation used by Papers_014–023.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the V1 kernel from primitives more fundamental than P11; V1 is a kernel rule-type supplied via P10 with retardation forced by P11.
2. It does **not** claim that the V1 functional form (Gaussian, exponential, etc.) is uniquely determined by primitives; the second-moment finiteness is the load-bearing property.
3. It does **not** override or duplicate Paper_089; this paper supplies the **QFT-arc-internal presentation** as a propagator/Wightman function, complementary to Paper_089's canonical-reference content.
4. It does **not** claim novel empirical predictions beyond standard QFT propagator structure.
5. It does **not** introduce new substrate primitives.
6. "QFT-arc form" means: V1 presented in the language of two-point functions, Källén-Lehmann spectral representation, and propagator structure consumed by Papers_014 (curved background), 017 (Lorentz covariantization), 019 (continuum YM), 020 (OS-positivity).

---

## Abstract

The V1 finite-width retarded vacuum kernel is the substrate-level two-point function entering ED-QFT propagator structure. P10 (Rule-type primitive) supplies V1 as a kernel rule-type; P11 (Commitment-irreversibility) forces retardation; the second-moment finiteness $\ell_{V1}^2 < \infty$ supplies the UV regularization scale. The QFT-arc form presents V1 as a tempered-distribution-valued two-point function with finite-width form factor; this presentation is consumed by downstream QFT-arc papers (014, 015–023) where V1 enters as the substrate-level propagator.

---

## §1 Introduction

The V1 kernel appears in two complementary presentations across the corpus:

- **Wedges-arc / canonical-reference presentation (Paper_089):** V1 as the substrate-level retarded propagation rule, with kernel $K_{V1}(x, y) = K_{V1}(x - y)$ and explicit second-moment / bandwidth properties.
- **QFT-arc presentation (this paper):** V1 as a two-point function in the substrate-level QFT-state Hilbert space, with retardation, finite-width form factor, and spectral content suitable for Wick rotation, OS-positivity audit, and propagator-level coarse-graining.

The two presentations are equivalent under appropriate coarse-graining; this paper supplies the QFT-arc-internal language.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — supplies the V1 width scale $\ell_{V1} \sim \ell_{\mathrm{ED}}$.
- **P10 (Rule-type primitive)** — supplies V1 as a kernel rule-type.
- **P11 (Commitment-irreversibility)** — forces retardation.
- **P13 (Time homogeneity)** — supplies the time-translation symmetry on which retarded structure is defined.

### 2.2 Upstream dependencies

- **I-089:** Paper_089 V1 canonical reference (finite second moment, retarded kernel form).
- **I-Hilbert:** Paper_007 — rule-type Hilbert space.
- **I-Wightman:** Standard Wightman-function machinery (standard math).
- **I-Tempered:** Standard tempered-distribution theory (standard math).
- **I-KL:** Standard Källén-Lehmann spectral representation (standard math).

### 2.3 Paper-specific postulates

- **P-V1-Spectral:** The V1 kernel admits a Källén-Lehmann spectral representation with non-negative spectral density $\rho(m^2)$ supported on $m^2 \geq 0$ and with $\int \rho(m^2)\, dm^2 < \infty$ (finite normalization).
- **P-V1-FormFactor:** The momentum-space V1 form factor $\hat{K}_{V1}(p)$ decays for $|p|\ell_{V1} \gtrsim 1$ (UV regularization).

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | V1 as kernel rule-type (Paper_089 form) | I | Paper_089. |
| 2 | Retardation from P11 | I | Paper_089 + Paper_087. |
| 3 | Finite second moment $\ell_{V1}^2$ | I | Paper_089. |
| 4 | Rule-type Hilbert space supports two-point functions | I | Paper_007. |
| 5 | Two-point function $W(x,y) = \langle 0|\phi(x)\phi(y)|0\rangle$ defined | P (definitional) | Standard-form construction. |
| 6 | $W(x,y)$ is tempered-distribution-valued | I | Standard math (I-Tempered) applied to V1 finite second moment. |
| 7 | Källén-Lehmann spectral representation | P-V1-Spectral + I-KL | Postulate + standard math. |
| 8 | Momentum-space form factor decay | P-V1-FormFactor | Postulate. |
| 9 | QFT-arc V1 propagator $G_{\mathrm{ret}}(p) = \int \frac{\rho(m^2)\, dm^2}{p^2 - m^2 + i\epsilon p^0}$ | D-via-I | Standard Källén-Lehmann (I-KL) applied to P-V1-Spectral + retardation. |
| 10 | Wick rotation to Euclidean form | I | Standard math. |
| 11 | Numerical values of $\rho(m^2)$ for specific theories | I | Empirical matching. |

---

## §3 The QFT-Arc Form

### 3.1 V1 as a two-point function

Starting from Paper_089's V1 kernel $K_{V1}(x-y)$, define the substrate-level Wightman two-point function
$$W_{V1}(x, y) = \langle 0|\phi(x)\phi(y)|0\rangle_{\mathrm{sub}} ,$$
with $\phi$ a rule-type-carrier field operator on the rule-type Hilbert space (I-Hilbert). The substrate vacuum $|0\rangle_{\mathrm{sub}}$ is the no-commitment state per P11.

By I-Tempered applied to the V1 finite second moment, $W_{V1}$ is tempered-distribution-valued.

### 3.2 Spectral representation

By P-V1-Spectral, $W_{V1}$ admits the standard Källén-Lehmann form
$$W_{V1}(x-y) = \int_0^\infty \rho(m^2)\, \Delta^{(+)}_m(x-y)\, dm^2 ,$$
where $\Delta^{(+)}_m$ is the standard positive-frequency Wightman function for mass $m$.

### 3.3 Retardation and the propagator

P11 forces $W_{V1}$ to be retarded: only $y$ with $y^0 < x^0$ contributes. The retarded propagator is
$$G_{\mathrm{ret}}(p) = \int_0^\infty \frac{\rho(m^2)\, dm^2}{p^2 - m^2 + i\epsilon p^0} .$$

By P-V1-FormFactor, the spectral density's high-mass tail is suppressed; effectively, $\rho(m^2)$ has support out to $m^2 \sim 1/\ell_{V1}^2$ as a UV cutoff.

### 3.4 Euclidean form for OS-audit

Wick rotation (I) produces the Euclidean Schwinger function
$$S_{V1}^E(x-y) = \int_0^\infty \rho(m^2)\, \Delta^E_m(x-y)\, dm^2 ,$$
consumed by Paper_020 OS-positivity audit.

---

## §4 Relation to Paper_089

| Aspect | Paper_089 (wedges, canonical) | This paper (QFT-arc) |
|---|---|---|
| Presentation | Kernel $K_{V1}(x-y)$ | Two-point function $W_{V1}(x,y)$ |
| Audience | All-arcs canonical reference | QFT-arc downstream (014, 015–023) |
| Key property | Finite second moment | Spectral density + form-factor decay |
| Audit content | Width/bandwidth | Källén-Lehmann + retardation |

The two presentations are equivalent under the standard QFT-vacuum-state identification: $W_{V1}$ on rule-type Hilbert states reduces to $K_{V1}$ on substrate edge-set under the appropriate coarse-graining (Paper_073 DCGT).

---

## §5 What This Paper Supplies and Does Not Supply

**Supplies:** QFT-arc-internal V1 presentation suitable for propagator-level coarse-graining (Papers_014–023), OS-positivity audit (Paper_020), and substrate-level QFT scaffolding.

**Does not supply:** Specific spectral density $\rho(m^2)$ for any concrete theory (INHERITED). Substrate-level derivation of $\ell_{V1}$ beyond its identification with $\ell_{\mathrm{ED}}$. Multi-point functions $n \geq 3$ (would require additional postulates).

---

## §6 Open Structural Questions

- **O-V1-1:** Substrate-level derivation of $\rho(m^2)$ from V1 kernel data.
- **O-V1-2:** Substrate derivation of P-V1-FormFactor decay shape (currently postulated as "decay for $|p|\ell_{V1} \gtrsim 1$" without specific functional form).
- **O-V1-3:** Multi-point (3-point, 4-point) substrate Wightman functions and their factorization properties.
- **O-V1-4:** Substrate-level OS-axioms verification at the V1 two-point level (partially in Paper_020).

---

## §7 Falsification Criteria

- **F1:** Demonstration that V1's two-point function does NOT admit a Källén-Lehmann representation (negative spectral density, non-tempered distribution character) — refutes P-V1-Spectral.
- **F2:** Demonstration that V1's high-momentum tail does NOT decay (UV-singular) — refutes P-V1-FormFactor.
- **F3:** Empirical detection of a substrate-level two-point function inconsistent with P11 retardation — refutes the substrate-level identification.

---

## §8 Position Statement

V1's QFT-arc form supplies the substrate-level propagator scaffolding for the QFT arc. P10 + P11 + P13 supply the primitive content; P-V1-Spectral + P-V1-FormFactor declare the load-bearing spectral properties; standard Källén-Lehmann machinery delivers the propagator form. Numerical content INHERITED via matching.

---

**End Paper 013 (FIXED).**
