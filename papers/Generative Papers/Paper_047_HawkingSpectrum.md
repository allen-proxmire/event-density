# Paper_047 — The Hawking Spectrum at $T_H = \kappa/(2\pi)$ via V5 KMS

**Series:** Event Density (ED) Generative Papers — Wave-2 BH/Hawking arc
**Author:** Allen Proxmire
**Status:** Publication draft (delivers the spectrum derivation promised in Paper_039 §4 + §7.2)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/black-hole/Paper_047_HawkingSpectrum.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_047_HawkingSpectrum.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (Paper_087).
2. **The surface gravity $\kappa$ is not derived in this paper.** $\kappa$ is **inherited** from the GR / BH-geometric setup as the coarse-grained identification at the substrate decoupling surface (Paper_039 §3.2). Independent substrate-level derivation of $\kappa$ awaits the Arc ED-10 curvature-emergence program.
3. **The Euclidean conical-defect structure (§3) is inherited via DCGT, not substrate-derived.** §3's content (Euclidean continuation, conical-defect smoothness, imaginary-time periodicity $\beta_H = 2\pi/\kappa$) is the standard semiclassical Euclidean BH structure, applied to substrate-graph content via DCGT (Paper_073). The substrate-level novelty is in §6 (the cutoff corrections), not §3.
4. **The BH mass $M$ and spacetime geometry are not derived.** Inherited from BH physics; substrate framework operates conditional on $\kappa(M, J, Q, \ldots)$.
5. **No claim that the standard semiclassical Hawking derivation is wrong.** ED's substrate-level mechanism reproduces standard Hawking at leading order ($\omega \ll \omega_c$), with **specific predicted non-thermal corrections** at higher order (under P-V5-Even).
6. **No claim that V5 supplies the only substrate-level mechanism for Hawking radiation.** Alternative substrate-level mechanisms (V1-only, or future-cascade-kernel-based) are conceivable but not load-bearing in the current substrate framework.
7. **No claim of unitarity proof.** Paper_039 §7 argues the information paradox is structurally not generated; this paper does not re-derive that argument. Hawking spectrum derivation operates conditional on the substrate-level structure Paper_039 establishes.
8. **No claim that $\omega_c = c/\ell_P$ is derived.** $\omega_c$ is **chosen to match the substrate scale**: $\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ via $\ell_{\mathrm{ED}} = \ell_P$ (Paper_027 §5.3). This is empirical-scale matching, not substrate-derivation.
9. **The $(\omega/\omega_c)^2$ leading-correction form is conditional on the P-V5-Even postulate (§2).** For parity-asymmetric V5 envelopes, the leading correction would be $\mathcal{O}(\omega/\omega_c)$ — linear rather than quadratic. P-V5-Even is a substrate-level structural commitment, not a derivation; alternative parity choices would predict different empirical signatures.
10. **No claim that the coefficient $c_1$ is exactly derivable.** $c_1$ is order-unity (e.g., $c_1 = 1/2$ for Gaussian V5 envelope under P-V5-Even), inherited from V5 envelope shape, which is value-layer (Paper_090 §3.3).
11. **Information-bearing claim is a soft structural availability, not a derivation.** §6.3 establishes that the substrate framework leaves room for $(\omega/\omega_c)^2$ deviations to carry information; the explicit substrate-to-spectrum encoding map awaits Paper_050.

---

## Abstract

This paper delivers the **Hawking spectrum derivation** promised in Paper_039 §4 + §7.2. Given the 13 postulated primitives (Paper_087) + V1 inheritance (Paper_089) + V5 dependence (Paper_090) + Paper_039's substrate-level decoupling-surface mechanism, the substrate-level Hawking spectrum follows from **V5 imaginary-time periodicity** + the **substrate-level KMS condition** at the near-horizon Euclidean geometry. The derivation has four load-bearing components: (1) V5 acquires imaginary-time periodicity $\beta_H = 2\pi/\kappa$ from the Euclidean conical-defect smoothness at the decoupling surface; (2) periodicity implies the **KMS condition** for V5 cross-chain correlators; (3) KMS implies thermal Planck distribution at temperature $T_H = 1/\beta_H = \kappa/(2\pi)$; (4) V5's substrate-level cutoff $\omega_c = c/\ell_P$ produces **specific predicted non-thermal corrections** of order $(\omega/\omega_c)^2$ (under the P-V5-Even postulate, §2), with sign-definite and mass-dependent structure. The corrections leave **structural room** for information-bearing content, with the explicit encoding map awaiting Paper_050 (Page-curve substrate mechanism). The headline result:

$$
n_H^{\mathrm{ED}}(\omega) = n_H^{\mathrm{Planck}}(\omega)\,\left[1 - c_1(\omega/\omega_c)^2 + \mathcal{O}((\omega/\omega_c)^4)\right]
$$

with $c_1$ an order-unity coefficient inherited from V5 envelope shape. The $(\omega/\omega_c)^2$ leading-correction form is **conditional on the P-V5-Even postulate (§2)** — V5 envelope parity-symmetric in $\omega$; parity-asymmetric envelopes would give a linear leading correction $\mathcal{O}(\omega/\omega_c)$ instead. The paper makes no claim that $\kappa$ is derived (inherited from BH geometry), no claim that $\omega_c$ is derived (chosen to match $\ell_P$), no claim that the Euclidean conical-defect content of §3 is substrate-derived (inherited via DCGT from standard semiclassical Euclidean BH geometry), no claim of unitarity proof in this paper, and no claim that $c_1$ is exactly derivable.

---

## 1. Introduction

### 1.1 What this paper does

This paper supplies the **substrate-level Hawking-spectrum derivation** in four steps:

1. V5 imaginary-time periodicity at the substrate decoupling surface (§3).
2. KMS condition from periodicity (§4).
3. Thermal Planck distribution at $T_H = \kappa/(2\pi)$ (§5).
4. Non-thermal $(\omega/\omega_c)^2$ corrections from V5 finite cutoff (§6).

The derivation operates conditional on Paper_039's substrate-level decoupling-surface mechanism (which establishes the substrate-graph structure at the BH horizon). This paper does not re-derive the decoupling surface; it builds the Hawking spectrum on top of it.

### 1.2 Why this matters

Paper_039 promised the spectrum derivation in two places:

- §4: "the full derivation — including the matching to the leading-order semiclassical Hawking spectrum — is the subject of Paper_047."
- §7.2: the non-thermal correction $n_H^{\mathrm{ED}} = n_H^{\mathrm{Planck}}\,[1 - c_1(\omega/\omega_c)^2 + \ldots]$ was stated as a headline result; the explicit derivation lives in this paper.

Without Paper_047, Paper_039's headline non-thermal-correction prediction (§7.2) lacks dedicated derivation. This paper supplies it.

### 1.3 How this fits into the BH/Hawking arc

- **Paper_039:** Horizon as decoupling surface; trans-Planckian resolution; Planck-mass remnant.
- **Paper_047 (this paper):** Hawking spectrum via V5 KMS.
- **Paper_050 (in queue):** Page-curve substrate mechanism.
- **Paper_052 (in queue):** BH info-paradox publication-grade synthesis.

This is the second BH-arc paper; together with Paper_039 it establishes the substrate-level Hawking mechanism.

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated** (Paper_087):

- **P02, P04, P05, P07, P09, P10, P11, P12** — as load-bearing in Paper_039.

**V1 inheritance (Paper_089):** finite-width retarded structure.

**V5 dependence (Paper_090):** cross-chain correlation kernel; finite memory at near-horizon $\tau_{V5}^{\mathrm{BH}} \sim \ell_P/c$.

**Postulate specific to this paper (added per round-2 QC Rereading Test):**

- **P-V5-Even (V5 envelope parity-symmetric in frequency):** *The V5 envelope $F_{V5}(\omega/\omega_c)$ is parity-symmetric (even) under $\omega \to -\omega$ around the substrate-saturated regime.* This postulate is required to exclude odd-power leading corrections in the $(\omega/\omega_c)$ expansion (§6.2), giving the $(\omega/\omega_c)^2$ leading non-thermal correction. For non-even envelopes (e.g., pure exponential $e^{-\omega/\omega_c}$, which is not parity-symmetric), the leading correction is $\mathcal{O}(\omega/\omega_c)$ instead — a different empirical signature. P-V5-Even is the substrate-level structural commitment that selects the parity-even case (Gaussian-like, $1 - (\omega/\omega_c)^2 + \ldots$); it is **not** derivable from Paper_090's V5 admissible class alone and is labeled here for transparency.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_089:** V1 canonical reference.
- **Paper_090:** V5 cross-chain kernel.
- **Paper_039:** Horizon decoupling — supplies substrate-graph structure at BH horizon, including the surface gravity $\kappa$ as the coarse-grained P12-gradient identification at the decoupling surface.
- **Paper_073:** DCGT — used to bridge substrate-level KMS to semiclassical Hawking continuum spectrum.

**Empirical / value-layer inputs:**

- **Surface gravity $\kappa$:** inherited from BH geometry (Schwarzschild: $\kappa = c^4/(4GM)$; Kerr: depends on $M, J$). **Not derived in this paper.**
- **BH mass $M$, angular momentum $J$, charge $Q$:** astrophysical parameters; inherited.
- **Substrate scale $\ell_{\mathrm{ED}} = \ell_P$:** empirically identified via Paper_027 §5.3.
- **V5 envelope shape:** value-layer; determines $c_1$ in non-thermal correction.

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| V1 retarded kernel structure | D | Paper_089 |
| V5 cross-chain correlation | D | Paper_090 |
| Substrate decoupling surface at BH horizon | D | Paper_039 §3 |
| Surface gravity $\kappa$ | I | Paper_039 §3.2 coarse-grained from GR; this paper inherits |
| Euclidean continuation of substrate-graph structure | **I-via-DCGT** | **§3.1 inherited from standard semiclassical Euclidean BH geometry via DCGT (Paper_073); the substrate-level novelty is in §6, not §3.** |
| Conical-defect smoothness condition | **I-via-DCGT** | §3.2 standard Euclidean BH structure; substrate framework reinterprets the periodicity locus (V5 correlators) but inherits the geometric condition. |
| Imaginary-time periodicity $\beta_H = 2\pi/\kappa$ | **I-via-DCGT** | §3.3 from inherited conical-defect smoothness + inherited $\kappa$. |
| KMS condition on V5 correlators | D | §4 from imaginary-time periodicity (substrate-level reinterpretation: periodicity now lives in V5 correlators, not in matter fields) |
| Thermal Planck distribution at $T_H = \kappa/(2\pi)$ | D | §5 from KMS condition |
| V5 substrate cutoff $\omega_c = c/\ell_P$ | I / regime | $\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ chosen to match substrate scale; Paper_090 §5.2 |
| V5 envelope parity-symmetric in $\omega$ | **P (P-V5-Even)** | **§2 postulate.** Excludes odd-power leading corrections; required for the $(\omega/\omega_c)^2$ leading-form prediction. |
| Non-thermal correction form $(\omega/\omega_c)^2$ leading | D | §6.2 from P-V5-Even + V5 envelope Taylor expansion (even powers only) |
| Sign-definite negative leading correction | D | §6.3 from V5 envelope decay shape (positive decay rate at large $\omega$ → negative correction to occupation number) |
| Mass-dependent scaling of correction magnitude | D | §6.3 from $\omega_H/\omega_c \sim M_P/M$ |
| Information-bearing structure of corrections | **A→P** | **§6.3 leaves substrate-level room for information-bearing content; explicit substrate-to-spectrum encoding map awaits Paper_050.** Soft claim, not derived. |
| Coefficient $c_1$ order-unity | I | V5 envelope shape value-layer (Paper_090 §3.3) |
| DCGT bridge to semiclassical continuum | D | Paper_073 |

All load-bearing steps are P, D, I, or labeled regime/soft. *Round-2 Rereading Test applied: §3 rows previously labeled D (Euclidean conical-defect content) relabeled as I-via-DCGT because they inherit from standard semiclassical Euclidean BH geometry via DCGT, not from substrate-level derivation. Even-envelope postulate (P-V5-Even) made explicit. Information-bearing claim (§6.3) softened to A→P pending Paper_050.*

---

## 3. V5 Imaginary-Time Periodicity at the Substrate Decoupling Surface

### 3.1 Euclidean continuation of substrate-graph structure

At the substrate decoupling surface (Paper_039 §3), V5 cross-chain correlations operate in the near-horizon region. To analyze thermal-like substrate behavior, we perform the **Euclidean continuation** $t \to -i\tau_E$ on the substrate-graph structure.

In standard semiclassical Hawking analysis, the Euclidean continuation of Schwarzschild spacetime near the horizon takes the form $ds^2_E = \kappa^2 r^2\,d\tau_E^2 + dr^2 + (\mathrm{angular})$ (after Rindler-like coordinates centered at the horizon). The Euclidean geometry near $r = 0$ has a **conical structure** with deficit angle determined by $\beta = 2\pi/\kappa$.

In ED's substrate framework, the substrate-graph adjacency near the decoupling surface inherits this Euclidean conical structure as the coarse-grained DCGT-continuum limit of the substrate-graph metric (Paper_039 §3.2). At substrate-graph scales, the structure is discrete; at coarse-grained scales, it matches the standard Euclidean BH geometry.

### 3.2 Conical-defect smoothness condition

For substrate-graph kernels to extend smoothly across the conical structure in the Euclidean continuation, the imaginary-time direction must be **periodic** with period matching the conical structure. This is the substrate-level analog of the standard semiclassical condition that the Euclidean BH geometry is regular at the horizon (no conical defect).

**The smoothness condition:** for V5 cross-chain correlators to be regular at the Euclidean horizon (no singularity in V5 envelope at the conical-defect point), the imaginary-time direction must be identified with period:

$$
\beta_H = \frac{2\pi}{\kappa}.
$$

**Dimensional check:** $\kappa$ has units $[1/\mathrm{time}]$ (acceleration / velocity = $1/\mathrm{time}$ — surface gravity is acceleration, divided by $c$ in natural units, gives $1/\mathrm{time}$); $\beta_H$ has units $[\mathrm{time}]$. $2\pi$ dimensionless. ✓

### 3.3 Imaginary-time periodicity of V5

Combining §3.1 and §3.2, V5 cross-chain correlators near the decoupling surface satisfy:

$$
K_{V5}(u_A, t_A; u_B, t_B)\Big|_{\mathrm{Euclidean}} = K_{V5}(u_A, t_A + i\beta_H; u_B, t_B)\Big|_{\mathrm{Euclidean}}
$$

with periodicity $\beta_H = 2\pi/\kappa$.

This is the substrate-level imaginary-time periodicity. **It is derived from the conical-defect smoothness condition + inherited $\kappa$**, not assumed.

---

## 4. KMS Condition from Periodicity

### 4.1 The KMS condition

The **Kubo–Martin–Schwinger (KMS) condition** for a quantum-mechanical thermal state at temperature $T = 1/\beta$ is:

$$
\langle\phi(t_A)\phi(t_B)\rangle_{T} = \langle\phi(t_A + i\beta)\phi(t_B)\rangle_{T}
$$

for two-point correlators $\langle\phi(t_A)\phi(t_B)\rangle$ evaluated in the thermal density matrix $\rho = e^{-\beta H}/Z$.

KMS is the defining property of thermal equilibrium in quantum statistical mechanics (Kubo 1957, Martin–Schwinger 1959).

### 4.2 V5 correlators satisfy KMS at $\beta = \beta_H$

From §3.3, V5 cross-chain correlators in the near-horizon Euclidean substrate-graph structure are periodic in imaginary time with period $\beta_H = 2\pi/\kappa$:

$$
\langle\phi(u_A, t_A)\phi(u_B, t_B)\rangle_{V5}^{\mathrm{Eucl}} = \langle\phi(u_A, t_A + i\beta_H)\phi(u_B, t_B)\rangle_{V5}^{\mathrm{Eucl}}.
$$

**This is the KMS condition** for V5 correlators at substrate level, with $\beta = \beta_H$. The substrate-level structure of V5 near the decoupling surface is **automatically thermal** at temperature

$$
T_H = \frac{1}{\beta_H} = \frac{\kappa}{2\pi}.
$$

**Dimensional check:** $T_H$ has units of $[1/\mathrm{time}]$ (in natural units with $\hbar = k_B = 1$); restoring units: $T_H = \hbar\kappa/(2\pi k_B)$ has units of temperature. ✓

### 4.3 Substrate-level KMS vs. field-theoretic KMS

In standard semiclassical Hawking analysis, KMS is established for *matter-field* correlators on a fixed BH background — the matter field's two-point function in the Hartle–Hawking state is KMS-thermal at $T_H$.

In ED's substrate framework, KMS is established for **V5 substrate-level cross-chain correlators** — the substrate kernel rule-type is itself thermal at the substrate level. The two are connected via DCGT (Paper_073 §6.4): V5 substrate KMS coarse-grains to standard matter-field KMS in the continuum limit.

The substrate-level KMS is structurally deeper: it operates at the level of substrate primitives (V5 cross-chain kernel) rather than at the level of derived field-theoretic content.

---

## 5. Leading-Order Hawking Spectrum

### 5.1 Thermal Planck spectrum from KMS

The KMS condition at temperature $T_H = \kappa/(2\pi)$ (§4.2) implies that V5 correlators in the near-horizon Euclidean substrate-graph structure have the thermal-Planck form:

$$
\langle\phi(\omega)\phi(\omega')\rangle_{V5}^{\mathrm{thermal}} \propto \frac{1}{e^{\hbar\omega/k_B T_H} - 1}\,\delta(\omega - \omega') + (\text{vacuum part}).
$$

This is the **Bose–Einstein distribution at temperature $T_H$**:

$$
n_H^{\mathrm{Planck}}(\omega) = \frac{1}{e^{\hbar\omega/k_B T_H} - 1}.
$$

**Dimensional check:** $\hbar\omega$ has units of energy; $k_B T_H$ has units of energy; ratio is dimensionless; $n_H^{\mathrm{Planck}}$ is dimensionless (occupation number). ✓

### 5.2 Identification with semiclassical Hawking

The semiclassical Hawking result (Hawking 1974, 1975) gives the thermal radiation flux at temperature $T_H = \kappa/(2\pi)$ via matter-field-mode tracing through the BH spacetime.

ED's substrate-level KMS derivation yields **the same leading-order spectrum** via DCGT coarse-graining (Paper_073 §6.4): substrate-level V5 KMS coarse-grains to standard matter-field KMS in the continuum, with the same temperature.

**At leading order** ($\omega \ll \omega_c = c/\ell_P$), ED reproduces standard semiclassical Hawking. The substrate-level mechanism supplies a structural derivation of the temperature via V5 imaginary-time periodicity, but does not change the leading-order spectrum.

### 5.3 Why this matters

Standard semiclassical Hawking requires extrapolation of matter-field modes to $\omega \to \infty$ — the trans-Planckian problem (Paper_039 §5). ED's substrate-level KMS derivation:

- Does not require trans-Planckian extrapolation (V5 has finite memory at $\tau_{V5}^{\mathrm{BH}} \sim \ell_P/c$).
- Produces structurally-truncated spectrum at $\omega \to \omega_c$.
- Predicts specific deviations from purely thermal behavior at higher orders (§6).

These three features are the substrate-level structural improvements over standard semiclassical Hawking. The leading-order spectrum coincides; the higher-order content distinguishes.

---

## 6. Non-Thermal Corrections from V5 Cutoff

### 6.1 The V5 substrate cutoff

By Paper_090 §5.2, V5's near-horizon memory time is **chosen to match the substrate scale**: $\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ (conditional on $\ell_{\mathrm{ED}} = \ell_P$, Paper_027 §5.3). The corresponding cutoff frequency is:

$$
\omega_c = 1/\tau_{V5}^{\mathrm{BH}} = c/\ell_P.
$$

V5 envelope $F_{V5}$ decays exponentially for $\omega > \omega_c$; substrate-level V5 correlators cannot support modes above $\omega_c$.

### 6.2 Non-thermal correction form — given P-V5-Even

The substrate-level Hawking spectrum, derived from V5 KMS with finite cutoff, has the form:

$$
n_H^{\mathrm{ED}}(\omega) = n_H^{\mathrm{Planck}}(\omega) \cdot f_{V5}(\omega/\omega_c)
$$

where $f_{V5}(x)$ is the **V5 cutoff-correction factor** inherited from V5 envelope shape.

**The leading-order form of $f_{V5}$ depends on V5 envelope parity:**

- **Under P-V5-Even (§2 postulate):** the V5 envelope is parity-symmetric ($F_{V5}(\omega) = F_{V5}(-\omega)$ around the substrate-saturated regime). The Taylor expansion in $\omega/\omega_c$ contains only **even powers**, giving:
  $$
  f_{V5}(x) = 1 - c_1\,x^2 + \mathcal{O}(x^4)
  $$
  with $c_1 > 0$ (sign-definite, §6.3). Example: Gaussian $F_{V5}(\omega) \sim e^{-\omega^2/\omega_c^2}$ gives $c_1 = 1/2$.

- **Without P-V5-Even (parity-asymmetric envelopes, e.g., pure exponential $F_{V5}(\omega) \sim e^{-\omega/\omega_c}$):** the Taylor expansion contains a non-zero **linear term**, giving:
  $$
  f_{V5}(x) = 1 - c_0\,x + \mathcal{O}(x^2)
  $$
  with $c_0 \approx 1$ for the exponential case. This is a **different empirical signature** (linear leading correction rather than quadratic).

**This paper commits to P-V5-Even** as a substrate-level postulate (§2). The leading correction is therefore $(\omega/\omega_c)^2$, not $(\omega/\omega_c)$. The choice of even envelope is motivated by Gaussian-like smoothness of the V5 substrate-saturated regime, but it is a **postulational commitment**, not a derivation — alternative substrate ontologies with non-even envelopes would predict a different (linear) leading correction.

**Headline result (under P-V5-Even):**

$$
\boxed{n_H^{\mathrm{ED}}(\omega) = n_H^{\mathrm{Planck}}(\omega)\,\left[1 - c_1\,(\omega/\omega_c)^2 + \mathcal{O}((\omega/\omega_c)^4)\right]}
$$

with $c_1$ order-unity, value-layer (inherited from V5 envelope shape).

**Dimensional check:** $\omega$ has $[1/\mathrm{time}]$; $\omega_c$ has $[1/\mathrm{time}]$; $\omega/\omega_c$ dimensionless; $n_H$ dimensionless. ✓

**Empirical falsification handle.** The choice between $(\omega/\omega_c)^2$ (P-V5-Even) and $(\omega/\omega_c)$ (non-even envelope) is empirically distinguishable in analog-Hawking experiments: linear vs. quadratic scaling of the deviation from purely thermal is a sharp test. See §11 for falsifier sentences.

### 6.3 Sign-definite, mass-dependent, information-bearing

Three structural features distinguish ED's correction from "tiny correction smoothed away":

**Sign-definite (negative).** The leading correction term is $-c_1\,(\omega/\omega_c)^2$ with $c_1 > 0$. The correction **suppresses emission relative to thermal** at all $\omega < \omega_c$. This is set by V5 envelope decay (positive decay rate at large $\omega$).

**Mass-dependent.** The dominant Hawking-emission frequency scales as $\omega_H \sim \kappa \sim 1/M$ (for Schwarzschild). The ratio $\omega_H/\omega_c$ scales as $\omega_H/\omega_c \sim M_P/M$. For astrophysical BHs ($M \gg M_P$), $(\omega_H/\omega_c)^2 \sim (M_P/M)^2$ is extremely small — corrections invisible. For evaporating BHs approaching $M_\star = M_P$ (Paper_039 §6), $(\omega_H/\omega_c)^2 \sim 1$ — corrections $\mathcal{O}(1)$, spectrum qualitatively non-thermal.

**Information-bearing (soft claim, pending Paper_050).** Pure thermality carries no information about BH formation state. The substrate framework **leaves room for** the $(\omega/\omega_c)^2$ deviations to carry V5-cross-chain-correlation content with substrate-level BH-formation history. This is the substrate-level *channel* through which BH-formation information could be carried out by the radiation (Paper_039 §7.2 + Paper_050 in queue).

**Honesty caveat:** the explicit map from substrate-level BH-formation state to specific spectrum features is **not derived in this paper**. "Information-bearing" is a substrate-level *room-for*, not a derivation. The explicit encoding map awaits Paper_050 (Page-curve substrate mechanism). Without that map, "information-bearing" is a structural-availability claim, not an operational identification. Substrate-level unitarity is established structurally in Paper_039 §7; this paper supplies the substrate-level *vehicle* (non-thermal corrections) through which information *can be* carried, not the explicit encoding.

### 6.4 Empirical content

- **Astrophysical BHs:** corrections at level $(\hbar\omega/M_P c^2)^2 \sim (T_H/T_P)^2$ — extremely small but structurally non-zero. Direct astrophysical detection beyond current sensitivity.
- **Analog Hawking experiments** (BEC, fluid, optical analogs): analog system's natural high-frequency cutoff much closer to dominant analog-Hawking frequency. Non-thermal corrections should be observable as deviation from purely thermal prediction. **Near-term empirical test.**
- **Late-stage BH evaporation:** at $M \to M_\star = M_P$, corrections become $\mathcal{O}(1)$; spectrum qualitatively non-thermal. Direct observation in PBH-evaporation cosmological signatures (if any) or hypothetical near-Planck-mass BH evaporation.

### 6.5 Coefficient $c_1$ value-layer status

$c_1$ depends on V5 envelope shape (Paper_090 §3.3):

| Envelope shape | $c_1$ |
|---|---|
| Exponential $e^{-\omega/\omega_c}$ | $\approx 1$ |
| Gaussian $e^{-\omega^2/\omega_c^2}$ | $1/2$ |
| Step function $\Theta(\omega_c - \omega)$ | divergent at $\omega = \omega_c$ (not physical) |

The specific value of $c_1$ is **value-layer empirical**: it requires independent determination of V5 envelope shape (e.g., via cross-domain V5 applications in soft-matter Maxwell relaxation, where empirical relaxation kernels constrain V5 envelope independently).

The substrate framework's structural prediction is the **form** ($(\omega/\omega_c)^2$ scaling, negative sign at leading order, mass-dependence); the **coefficient** is downstream of V5 envelope determination.

---

## 7. The Wedge — Empirical Distinction from Standard Semiclassical Hawking

The substrate-level Hawking spectrum is **distinguishable from purely thermal semiclassical Hawking** via:

1. **Sign-definite negative corrections at $(\omega/\omega_c)^2$.** Standard semiclassical Hawking is exactly thermal; ED predicts specific deviations.
2. **Mass-dependent scaling of the correction magnitude.** Standard semiclassical Hawking has no analogous correction; ED predicts that the deviation grows as $M$ decreases.
3. **Information-bearing non-thermal content.** Standard semiclassical Hawking is information-less; ED's non-thermal corrections carry substrate-level information about BH formation state.

**Empirical strategy:**

- Analog Hawking experiments (closest near-term test): measure the analog spectrum's deviation from purely thermal at the analog system's $(\omega/\omega_c^{\mathrm{analog}})^2$ scale.
- Late-stage BH evaporation (long-term test): direct astrophysical observation if PBH evaporation produces detectable signatures.

This is the wedge content of Paper_047: a **specific, falsifiable, sign-definite, mass-dependent non-thermal correction** that no standard semiclassical or modified-gravity account predicts.

---

## 8. Falsification Criteria

### 8.1 Analog Hawking with exact thermal spectrum at $(\omega/\omega_c)^2$

**Falsifier sentence:** *Analog Hawking experiments (BEC, fluid, optical) detecting Hawking-like radiation with no detectable deviation from purely thermal at the analog system's $(\omega/\omega_c^{\mathrm{analog}})^2$ scale, after accounting for analog-system noise, would falsify §6's headline non-thermal-correction prediction.*

### 8.2 Wrong sign or scaling of non-thermal corrections (sharp P-V5-Even test)

**Falsifier sentence (sign):** *Empirical observation of non-thermal Hawking-spectrum corrections with positive sign (enhancement rather than suppression) would falsify V5 envelope decay shape.*

**Falsifier sentence (parity / scaling):** *Empirical observation of a **linear** $(\omega/\omega_c)^1$ leading correction (rather than quadratic $(\omega/\omega_c)^2$) would falsify the **P-V5-Even postulate (§2)** and force adoption of a parity-asymmetric V5 envelope. This is a sharp empirical test of P-V5-Even directly: the leading-correction power-law is the falsification handle.*

**Falsifier sentence (higher-order):** *Empirical scaling other than $(\omega/\omega_c)^2$ or $(\omega/\omega_c)^1$ (e.g., $(\omega/\omega_c)^{1.5}$, or no power-law scaling at all) would falsify the V5 envelope-Taylor-expansion mechanism entirely, requiring a different substrate-level mechanism for the non-thermal corrections.*

### 8.3 No imaginary-time periodicity at substrate level

**Falsifier sentence:** *Substrate-level analysis showing V5 cross-chain correlators do not acquire imaginary-time periodicity in the near-horizon Euclidean substrate-graph structure would falsify §3.3 and the KMS / Hawking-temperature derivation.*

### 8.4 Hawking temperature differs from $\kappa/(2\pi)$

**Falsifier sentence:** *Astrophysical observation of BH thermal radiation at temperature substantially differing from $\kappa/(2\pi)$ — beyond the predicted $(\omega/\omega_c)^2$ corrections — would falsify the substrate-level KMS mechanism.*

### 8.5 V5 cutoff frequency differs from $c/\ell_P$

**Falsifier sentence:** *Empirical demonstration that the trans-Planckian cutoff for the Hawking spectrum is at a frequency $\omega_c \neq c/\ell_P$ — i.e., inconsistent with $\tau_{V5}^{\mathrm{BH}} = \ell_P/c$ matching — would falsify the substrate-scale matching of Paper_090 §5.2 (which Paper_047 inherits).*

### 8.6 Late-stage evaporation purely thermal at $M \to M_P$

**Falsifier sentence:** *Empirical evidence that late-stage BH evaporation near $M = M_P$ produces purely thermal spectrum (no $\mathcal{O}(1)$ non-thermal deviations as predicted by §6.3 mass-dependence) would falsify the substrate-level $(\omega/\omega_c)^2$ correction structure.*

---

## 9. Position Statement

The **Hawking spectrum at $T_H = \kappa/(2\pi)$** is a downstream structural identification in the ED Generative Primitives System. Given the postulated primitives + V1/V5 + Paper_039's substrate decoupling-surface mechanism + Paper_073 DCGT, the spectrum follows from:

- V5 imaginary-time periodicity $\beta_H = 2\pi/\kappa$ at the Euclidean near-horizon substrate-graph structure (§3).
- KMS condition on V5 cross-chain correlators (§4).
- Thermal Planck distribution at $T_H = 1/\beta_H = \kappa/(2\pi)$ (§5).

**Headline non-thermal correction** (§6, delivering Paper_039 §7.2's promise):

$$
n_H^{\mathrm{ED}}(\omega) = n_H^{\mathrm{Planck}}(\omega)\,[1 - c_1\,(\omega/\omega_c)^2 + \mathcal{O}((\omega/\omega_c)^4)]
$$

with:

- $\omega_c = c/\ell_P$ (V5 substrate cutoff, chosen to match substrate scale).
- $c_1$ order-unity, value-layer (V5 envelope shape).
- Sign-definite negative, mass-dependent, information-bearing.

What this paper claims:

- Given the postulated primitives + V5 + Paper_039 + Paper_073, $T_H = \kappa/(2\pi)$ is the unique substrate-level identification of the Hawking temperature.
- The leading-order spectrum coincides with standard semiclassical Hawking.
- The $(\omega/\omega_c)^2$ non-thermal correction is a specific, falsifiable, sign-definite prediction that distinguishes ED from standard semiclassical accounts.
- Analog Hawking experiments are the near-term empirical wedge.

What this paper does *not* claim:

- The substrate primitives are not derived (Paper_087).
- $\kappa$ is not derived — inherited from BH geometry.
- $\omega_c$ is not derived — chosen to match substrate scale ($\ell_{\mathrm{ED}} = \ell_P$).
- $c_1$ is not exactly derivable — value-layer V5 envelope shape.
- Unitarity proof not delivered in this paper (Paper_039 + Paper_052 in queue).
- BH mass/geometry not derived.

The empirical case is cross-domain reach + the analog-Hawking-experiment near-term test.

**Series context.** Paper_047 of the BH/Hawking arc. The arc continues:

- **Paper_050 (in queue):** Page-curve substrate mechanism.
- **Paper_052 (in queue):** BH info-paradox publication-grade synthesis.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper_089 (V1):** kernel inheritance.
- **Paper_090 (V5):** cross-chain kernel; cutoff $\omega_c$ matching.
- **Paper_039 (Horizon Decoupling):** substrate decoupling surface; $\kappa$ inheritance.
- **Paper_073 (DCGT):** continuum-limit bridge.

### Glossary

- **Hawking temperature $T_H = \kappa/(2\pi)$.** Substrate-level identification via V5 KMS.
- **Surface gravity $\kappa$.** Inherited from BH geometry; not derived in this paper.
- **Imaginary-time periodicity $\beta_H$.** $\beta_H = 2\pi/\kappa$ from Euclidean conical-defect smoothness.
- **KMS condition.** Kubo–Martin–Schwinger thermal-state condition on V5 correlators.
- **V5 substrate cutoff $\omega_c = c/\ell_P$.** Chosen to match substrate scale.
- **Non-thermal correction.** $(\omega/\omega_c)^2$ leading-order deviation from purely thermal; sign-definite, mass-dependent, information-bearing.
- **Coefficient $c_1$.** Order-unity, value-layer V5 envelope shape.
- **Conical-defect smoothness.** Substrate-graph regularity condition at Euclidean horizon.

---

**End of Paper_047.**

*Wave-2 Generative Paper — BH/Hawking Arc. Substrate-level Hawking-spectrum derivation via V5 KMS, delivering Paper_039 §4 + §7.2 promised content. Headline result: $n_H^{\mathrm{ED}} = n_H^{\mathrm{Planck}}[1 - c_1(\omega/\omega_c)^2 + \ldots]$.*
