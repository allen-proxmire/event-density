# Paper 034 — Deep-MOND Asymptotic and Superluminality Structural Cost

**Series:** Wave-2 Generative Papers (Gravity Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_027 (Newton's $G$), Paper_029 ($a_0$), Paper_030 (ED Combination Rule), Paper_031 (BTFR slope-4), Paper_033 (Arc ED-10 scalar-tensor covariantization), Paper_036 (flat-background MOND-like field equation).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that deep-MOND superluminality is observable in any realistic galactic scenario; the structural cost is at the theory level, not empirical.
2. It does **not** claim that the deep-MOND $\mu(x) \to x$ asymptotic is uniquely fixed by substrate primitives; alternative asymptotic functional forms are admissible under different declared postulates.
3. It does **not** claim derivation of $a_0$ numerical value here; that is in Paper_029.
4. It does **not** claim that substrate gravity replaces GR; substrate gravity is a flat-background field-equation theory under acoustic-metric guardrails (Paper_035, ED-Phys-10).
5. It does **not** introduce new substrate primitives.
6. "Deep-MOND asymptotic" means: $|\nabla\Phi| \ll a_0$ regime where the interpolation $\mu(x) = x/(1+x)$ (or similar) reduces to $\mu(x) \to x$, producing $a = \sqrt{a_N a_0}$.
7. "Superluminality structural cost" means: in the deep-MOND limit, scalar-mode propagation in the acoustic metric admits superluminal characteristics under any admissible substrate-consistent $\mu$-function; this is a structural feature, not a bug fixable by changing $\mu$.

---

## Abstract

The deep-MOND asymptotic $a = \sqrt{a_N a_0}$ in the $|\nabla\Phi| \ll a_0$ regime is FORM-FORCED in ED by P12 (stability landscape) + ED Combination Rule (Paper_030) + transition acceleration $a_0$ (Paper_029). The associated **superluminality structural cost** — scalar-mode characteristics exceeding the substrate $c$ in the deep-MOND asymptotic — is **structurally FORCED** under any admissible substrate-consistent $\mu$-function: avoidance routes either violate the BTFR slope-4 (Paper_031) or violate the no-new-primitives constraint of the program. This is the load-bearing structural cost identified by Arc ED-10 (Paper_033). The numerical scale is INHERITED.

---

## §1 Introduction

The MOND-like interpolation function $\mu(x)$ in $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G \rho_m$ (Paper_036) has two limits:

- **Newtonian limit:** $|\nabla\Phi| \gg a_0 \Rightarrow \mu(x) \to 1$, recovering Newton's law.
- **Deep-MOND limit:** $|\nabla\Phi| \ll a_0 \Rightarrow \mu(x) \to x$, giving $a = \sqrt{a_N a_0}$.

The deep-MOND limit is empirically tested at galactic rotation-curve outskirts; ED inherits it via Paper_030 + Paper_031. This paper supplies the substrate audit of the deep-MOND asymptotic, and identifies the superluminality structural cost as a load-bearing feature.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — supplies the Planck length used in $a_0 = c H_0 / (2\pi)$ (Paper_029).
- **P11 (Commitment-irreversibility)** — supplies the directional structure of substrate-gravity dissipation.
- **P12 (Stability landscape)** — supplies the cumulative-strain stability content (Paper_026).
- **P13 (Time homogeneity)** — supplies $H_0$ as a substrate-level cosmological time-rate.

### 2.2 Upstream dependencies

- **I-027:** Newton's law $G = c^3 \ell_P^2 / \hbar$ (Paper_027).
- **I-029:** Transition acceleration $a_0 = c H_0 / (2\pi)$ (Paper_029).
- **I-030:** ED Combination Rule $a = \sqrt{a_N a_0}$ (Paper_030).
- **I-031:** BTFR slope-4 $v^4 = G M a_0$ (Paper_031).
- **I-033:** Arc ED-10 scalar-tensor acoustic-metric covariantization (Paper_033).
- **I-Acoustic:** ED-Phys-10 acoustic-metric guardrails.
- **I-MOND-Math:** Standard MOND interpolation-function mathematics (standard math).

### 2.3 Paper-specific postulates

- **P-MOND-Interpolation:** The $\mu$-function $\mu : [0,\infty) \to [0,1]$ is smooth, monotonically increasing, with $\mu(0) = 0$, $\mu(\infty) = 1$, and $\mu(x) \to x$ as $x \to 0$ (deep-MOND asymptotic).
- **P-No-New-Primitive:** No new substrate primitive is introduced to avoid the superluminality structural cost. (Programmatic commitment.)

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | $a_0 = c H_0/(2\pi)$ | I | Paper_029. |
| 2 | ED Combination Rule $a = \sqrt{a_N a_0}$ | I | Paper_030. |
| 3 | BTFR slope-4 $v^4 = G M a_0$ | I | Paper_031. |
| 4 | $\mu$-function asymptotic $\mu(x) \to x$ for $x \to 0$ | P-MOND-Interpolation | Postulate. |
| 5 | $\mu$-function asymptotic $\mu(x) \to 1$ for $x \to \infty$ | P-MOND-Interpolation | Postulate. |
| 6 | Deep-MOND regime $|\nabla\Phi| \ll a_0$ | A→regime | Regime selection. |
| 7 | Deep-MOND scalar-mode characteristics computed from Arc ED-10 action | I | Paper_033 + standard variational analysis. |
| 8 | Characteristics exceed substrate $c$ in deep-MOND limit | D-via-I | Application of I-033 + I-MOND-Math + P-MOND-Interpolation. |
| 9 | No-new-primitive constraint | P-No-New-Primitive | Programmatic. |
| 10 | Avoidance routes violate either I-031 (slope-4) or P-No-New-Primitive | D | Composition of constraints. |
| 11 | Superluminality structural cost is FORCED | A→position | Composite verdict. |
| 12 | Empirical-test admissibility (causal observability) | OPEN | Not claimed as load-bearing on this paper. |

---

## §3 The Deep-MOND Asymptotic

### 3.1 The $\mu$-function in deep-MOND limit

Under P-MOND-Interpolation, the deep-MOND limit gives $\mu(|\nabla\Phi|/a_0) \to |\nabla\Phi|/a_0$. Substituting into the flat-background field equation (Paper_036):
$$\nabla\cdot\left[\frac{|\nabla\Phi|}{a_0}\nabla\Phi\right] = 4\pi G \rho_m .$$
For a point source $M$, spherical symmetry, and large radius, this yields acceleration $a \sim \sqrt{G M a_0} / r$, equivalent to $a = \sqrt{a_N a_0}$ (ED Combination Rule, Paper_030).

The deep-MOND asymptotic is therefore FORM-FORCED by P-MOND-Interpolation + Paper_036 + spherical geometry.

### 3.2 The structural cost: superluminality

By I-033 (Arc ED-10 acoustic-metric covariantization), the scalar mode $\Phi$ propagates in the acoustic-metric background with characteristics determined by the kinetic-term coefficient. In the deep-MOND regime, the kinetic coefficient scales as $\mu' \sim 1/a_0$ (P-MOND-Interpolation $\mu(x) \to x$ derivative).

Standard variational analysis (I-MOND-Math) shows that the scalar-mode characteristic speed in this regime exceeds the substrate $c$ — superluminal propagation of $\Phi$-perturbations relative to substrate $c$.

This is **D-via-I** under P-MOND-Interpolation + I-033.

### 3.3 Why the cost cannot be removed

To avoid superluminality, one would need either:
- (a) A $\mu$-function with different deep-MOND asymptotic — but then the ED Combination Rule (Paper_030) and BTFR slope-4 (Paper_031) fail.
- (b) A new substrate primitive providing additional kinetic-term structure — but this violates P-No-New-Primitive.

By exhaustion: the superluminality structural cost is **FORCED** under the program's self-consistency constraints (A→position).

### 3.4 Why this is "structural cost" not "refutation"

The superluminality is a feature of the **scalar perturbation mode** $\Phi$, not of matter or radiation. Standard ED-Phys-10 guardrails (Paper_035) confine the acoustic-metric framework to regimes where the scalar-mode causality structure does not compete with operational matter signals. Whether deep-MOND superluminality is **operationally observable** is an OPEN empirical question.

---

## §4 Falsification Criteria

- **F1:** Empirical detection that deep-MOND $\mu(x) \to x$ asymptotic produces causality-violating matter-signal propagation — would shift the structural cost from theory-level to refutation-level.
- **F2:** Demonstration of a substrate-consistent $\mu$-function preserving BTFR slope-4 (Paper_031) and avoiding the superluminality cost without new primitives — refutes the "FORCED" verdict.
- **F3:** Empirical refutation of BTFR slope-4 in the deep-MOND-limit galaxy population — propagates from Paper_031 to here.
- **F4:** Empirical detection of deep-MOND-asymptotic systems with $a \ne \sqrt{a_N a_0}$ — refutes Paper_030 / Paper_031 inheritance.

---

## §5 Position Statement

The deep-MOND asymptotic $a = \sqrt{a_N a_0}$ is **FORM-FORCED** under P-MOND-Interpolation + Paper_030 + Paper_031. The associated **superluminality structural cost** is **structurally FORCED** by the substrate program's self-consistency under P-No-New-Primitive: avoidance routes violate either BTFR slope-4 or the no-new-primitives constraint. This is the load-bearing structural cost identified by Arc ED-10 (Paper_033). Empirical observability of the cost is OPEN.

---

**End Paper 034 (FIXED).**
