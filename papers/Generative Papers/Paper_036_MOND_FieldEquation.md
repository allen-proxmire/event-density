# Paper 036 — Flat-Background Field Equation $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G \rho_m$

**Series:** Wave-2 Generative Papers (Gravity Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_026 (cumulative-strain P12), Paper_027 (Newton's $G$), Paper_028 (cosmic decoupling surface), Paper_029 ($a_0$), Paper_030 (ED Combination Rule), Paper_031 (BTFR slope-4), Paper_034 (deep-MOND).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a derivation of the specific functional form of $\mu$; the asymptotic behavior is FORCED, the interpolating form is INHERITED.
2. It does **not** claim that the field equation is the full theory of substrate gravity; it is the **flat-background** equation. Curved-background extension is Paper_033 / Arc ED-10.
3. It does **not** claim novel empirical predictions beyond standard MOND-class field theories.
4. It does **not** introduce new substrate primitives.
5. "Flat-background field equation" means: the substrate-gravity equation on a flat acoustic-metric background, suitable for galactic-scale predictions in the weak-field regime.

---

## Abstract

The flat-background substrate-gravity field equation $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G \rho_m$ is FORM-FORCED in ED by composing: (i) P12 stability landscape (Paper_026) supplying the cumulative-strain origin of the gravitational potential $\Phi$; (ii) P-Codim-1 (substrate-derived codimension-1 source structure, inherited from Paper_025); (iii) Newton's law $G$ (Paper_027); (iv) transition acceleration $a_0$ (Paper_029); (v) cosmic decoupling surface (Paper_028). The structural form of the equation — divergence of a $\mu$-modulated gradient with non-linear $|\nabla\Phi|/a_0$ dependence — is FORCED; the specific functional form of $\mu$ is INHERITED via empirical matching against galaxy rotation curves.

---

## §1 Introduction

The substrate-gravity arc derives Newton's law (T19, Paper_027), transition acceleration $a_0$ (T20, Paper_029), ED Combination Rule (Paper_030), and BTFR slope-4 (T21, Paper_031) at the substrate level. These results imply a MOND-class field equation interpolating between Newtonian and deep-MOND regimes; this paper supplies the substrate audit of the field equation itself.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)** — supplies the substrate-level matter-content carrier (sources $\rho_m$).
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — supplies the Planck scale entering $G$ (Paper_027).
- **P11 (Commitment-irreversibility)** — supplies the dissipative directional structure of substrate gravity.
- **P12 (Stability landscape)** — supplies the cumulative-strain content giving rise to $\Phi$ (Paper_026).
- **P13 (Time homogeneity)** — supplies $H_0$ entering $a_0$ (Paper_029).

### 2.2 Upstream dependencies

- **I-026:** Cumulative-strain reading of P12 (Paper_026).
- **I-027:** Newton's $G = c^3 \ell_P^2/\hbar$ (Paper_027).
- **I-028:** Cosmic decoupling surface $R_H = c/H_0$ (Paper_028).
- **I-029:** Transition acceleration $a_0 = c H_0/(2\pi)$ (Paper_029).
- **I-030:** ED Combination Rule (Paper_030).
- **I-031:** BTFR slope-4 (Paper_031).
- **I-Var:** Standard variational-principle / Euler-Lagrange machinery (standard math).

### 2.3 Paper-specific postulates

- **P-Codim-1:** The substrate-level matter source has codimension-1 footprint at the coarse-graining scale, justifying the standard density-source $4\pi G \rho_m$. (Inherited from Paper_025 holographic bound.)
- **P-MOND-Field-Form:** The substrate-gravity field equation takes the form $\nabla\cdot[\mu(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G \rho_m$ on the flat acoustic-metric background, with $\mu$ satisfying P-MOND-Interpolation (Paper_034).
- **P-Weak-Field:** The flat-background regime applies when $|\nabla\Phi|/c^2 \ll 1$ (weak-field) and the acoustic metric is approximately flat (guardrails (C1)-(C6) of Paper_035 active).

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | $G$ from P08 + substrate primitives | I | Paper_027. |
| 2 | $a_0$ from P13 + cosmological scale | I | Paper_029. |
| 3 | Cumulative-strain $\Phi$ from P12 | I | Paper_026. |
| 4 | Codimension-1 matter-source footprint | P-Codim-1 | Postulate (inherited from Paper_025). |
| 5 | Newtonian limit: $\mu(x) \to 1$ for $x \gg 1$ | I | Paper_027 + Paper_034. |
| 6 | Deep-MOND limit: $\mu(x) \to x$ for $x \ll 1$ | I | Paper_030 + Paper_031. |
| 7 | $\mu$-function smoothness, monotonicity | P-MOND-Field-Form | Postulate. |
| 8 | Field-equation structural form $\nabla\cdot[\mu \nabla\Phi] = 4\pi G \rho_m$ | P-MOND-Field-Form | Standard-form construction. |
| 9 | Equation follows from variational principle (Lagrangian $\mathcal{L} = -F(|\nabla\Phi|^2/a_0^2)/8\pi G + \rho_m \Phi$) | I | Standard variational machinery. |
| 10 | Newtonian regime recovers $\nabla^2\Phi = 4\pi G \rho_m$ | D-via-I | Standard MOND-limit calculation. |
| 11 | Deep-MOND regime recovers $a = \sqrt{a_N a_0}$ | I | Paper_030. |
| 12 | Specific functional form of $\mu$ (e.g., $\mu(x) = x/\sqrt{1+x^2}$) | I | Empirical matching to galaxy rotation curves. |

The audit honestly labels the field-equation form as P (standard-form construction): the substrate program does not derive the equation from a deeper structural principle; it constructs the equation to match the two asymptotic limits (Newtonian + deep-MOND) inherited from upstream substrate-gravity results.

---

## §3 The Field Equation

### 3.1 Construction strategy

The substrate-gravity arc supplies two asymptotic limits:
- **Newtonian** (Paper_027 + standard $\mu \to 1$): $\nabla^2\Phi = 4\pi G \rho_m$.
- **Deep-MOND** (Paper_030 / Paper_031, $\mu \to x$): $\nabla\cdot[(|\nabla\Phi|/a_0)\nabla\Phi] = 4\pi G \rho_m$.

A single equation interpolating both is the MOND-class form:
$$\nabla\cdot\left[\mu(|\nabla\Phi|/a_0) \nabla\Phi\right] = 4\pi G \rho_m .$$

This is a **standard-form construction (P)** matching the two asymptotic limits. It is not derived from a deeper substrate principle; it is the simplest substrate-consistent interpolation under P-MOND-Field-Form.

### 3.2 Variational origin

The equation follows from the variational principle applied to the Lagrangian
$$\mathcal{L} = -\frac{1}{8\pi G} a_0^2 F\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right) + \rho_m \Phi ,$$
where $F'(y^2) = \mu(y)/2$ (Bekenstein–Milgrom AQUAL form, inherited from standard MOND literature).

The variational structure is **I (standard math)** applied to the postulated Lagrangian.

### 3.3 Two limits recovered

- $|\nabla\Phi| \gg a_0$ ($\mu \to 1$): Newtonian.
- $|\nabla\Phi| \ll a_0$ ($\mu \to x$): Deep-MOND $a = \sqrt{a_N a_0}$.

Both limits are inherited from upstream substrate-gravity results.

---

## §4 Distinguishing Structural $\mu$-Form vs Empirical $\mu$-Choice

- **Structural (P + I):** The asymptotic behavior $\mu(0) = 0$, $\mu(\infty) = 1$, $\mu(x) \to x$ for $x \to 0$, $\mu(x) \to 1$ for $x \to \infty$. Forced by Newtonian limit (Paper_027) + deep-MOND limit (Paper_030 / Paper_031).
- **Empirical (I):** Specific interpolating form (e.g., $\mu(x) = x/\sqrt{1+x^2}$, $\mu(x) = x/(1+x)$, etc.). Selected by empirical fit to galaxy rotation curves.

The substrate program **does not derive** the specific $\mu$-function; it constrains the asymptotic behavior.

---

## §5 Falsification Criteria

- **F1:** Empirical detection that the field-equation form fails between the two asymptotic regimes — refutes P-MOND-Field-Form.
- **F2:** Empirical detection that the deep-MOND or Newtonian regime asymptotic fails — propagates from upstream papers.
- **F3:** Substrate evidence that the variational structure cannot be derived from substrate primitives — refutes the variational origin.
- **F4:** Detection of substrate-gravity phenomenology in the strong-field regime ($|\nabla\Phi|/c^2 \sim 1$) outside P-Weak-Field — would require Arc ED-10 (Paper_033) instead of this paper.

---

## §6 Position Statement

The flat-background substrate-gravity field equation is **FORM-FORCED** in its asymptotic behavior by upstream substrate-gravity results (Papers_027–031), declared as P-MOND-Field-Form for its interpolating structure, and follows by standard variational machinery (I) from the AQUAL-form Lagrangian. The specific $\mu$ functional form is **INHERITED** via empirical matching, **not derived**.

This is the flat-background equation. Curved-background extension is Paper_033 / Arc ED-10.

---

**End Paper 036 (FIXED).**
