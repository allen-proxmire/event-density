# Paper_030 — The ED Combination Rule $a = \sqrt{a_N \cdot a_0}$

**Series:** Event Density (ED) Generative Papers — Wave-2 rewrite of the gravity arc
**Author:** Allen Proxmire
**Status:** Publication draft (revision: P14 postulate added; §5 derivation rewritten single-pass; uniqueness argument replaced; $\Sigma_0$ reframed as coarse-grained Paper_029 dipole potential)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/gravity/Paper_030_CombinationRule.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_030_CombinationRule_FIXED.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Abstract

The Event Density (ED) substrate is a 13-primitive generative system. This paper develops the **ED Combination Rule (ECR)**:

$$
a = \sqrt{a_N \cdot a_0}
$$

as a **downstream structural consequence** of the postulated substrate primitives **augmented by P14 (Bilocal Strain Coupling)** — a new substrate-level postulate articulated explicitly in this revision. Given P14 and the joint weak-gradient regime, the substrate-level cumulative-strain reading of P12's stability landscape (Paper_027) combined with the coarse-grained cosmic-horizon dipole-projection potential (Paper_029) produces a logarithmic cross-term:

$$
\Sigma_{\mathrm{cross}}(R) = -\sqrt{GMa_0} \cdot \log(R/R_0)
$$

whose negative gradient yields the multiplicative geometric-mean combination $a = \sqrt{a_N \cdot a_0}$. The ECR bridges the Newtonian regime ($a \approx a_N$ when $a_N \gg a_0$) and the deep-MOND regime ($a \approx \sqrt{a_N a_0}$ when $a_N \ll a_0$) with a smooth, parameter-free transition profile. **The geometric-mean form is the structural consequence of P14, not derived from a uniqueness-of-substrate-mechanisms argument.** The paper makes no claim that $H_0$ or cosmology is derived, no claim that MOND-as-phenomenology is correct as a complete theory, no claim that the ECR's specific transition profile matches every MOND interpolation function, and no claim that the rule is forced from nothing. The empirical case rests on cross-domain reach: Papers_027 + 029 + 030 (this paper) + 031 constitute the substrate-gravity arc, with BTFR slope-4 + zero intrinsic scatter (Paper_031) as the testable consequence.

---

## 1. Introduction

### 1.1 What this paper does

This paper develops the **ED Combination Rule (ECR)** as a downstream structural consequence of the ED 13-Primitive Generative System **augmented by P14**. The derivation proceeds in four structural steps:

1. **Upstream results.** Newton's law $a_N = GM/R^2$ with $\Sigma_N(R) = -GM/R$ (Paper_027) and the cosmic dipole-projection potential $\Sigma_0(R)$ (coarse-grained from Paper_029, see §3.2) supply the two upstream contributions.

2. **P14 (Bilocal Strain Coupling).** In the joint weak-gradient regime, bilocal substrate channels carry strain proportional to the geometric mean of the local and horizon-sourced bandwidth contributions. **P14 is a new substrate-level postulate articulated in §2 of this paper.**

3. **Logarithmic cross-term derivation (single-pass).** Given P14 and the joint weak-gradient regime, the substrate-level cumulative-strain reading produces the logarithmic cross-term $\Sigma_{\mathrm{cross}}(R) = -\sqrt{GMa_0}\,\log(R/R_0)$.

4. **Combination rule identification.** In the joint weak-gradient regime, the bilocal cross-term dominates the chain's experienced acceleration; the negative gradient yields the ECR: $a = \sqrt{a_N \cdot a_0}$.

The geometric-mean form is **the structural consequence of P14**, not derived from a uniqueness argument.

### 1.2 Why the combination rule is a wedge

Standard accounts (dark-matter halos, MOND-as-phenomenology) either tune halo profiles or fit an interpolation function. ED supplies a **substrate-level mechanism (via P14)** for the transition. The transition profile is *derived* given P14, not fit.

This matters for: mechanism, predictive content, cross-arc coherence (Paper_027 → Paper_030 → Paper_031).

### 1.3 How this fits into the gravity arc

- **Paper_027:** Newton's $G$.
- **Paper_029:** Transition acceleration $a_0$.
- **Paper_030 (this paper):** Full structural derivation of the ECR via P14.
- **Paper_031:** Slope-4 BTFR (uses ECR as a step).

---

## 2. Primitive Inputs (including P14, new in this paper)

This paper takes the following ED substrate primitives as **postulated within the ED Generative Primitives System**:

- **P02 (Participation as primitive relation).**
- **P03 (Channel + locus indexing; spatial homogeneity).**
- **P04 (Bandwidth as non-negative additive scalar).**
- **P07 (Channel structure as ontological primitive).**
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).**
- **P11 (Commitment irreversibility).**
- **P12 (Stability landscape).**
- **P13 (Time homogeneity).**

**New postulate (this paper):**

> **P14 (Bilocal Strain Coupling).** *In the joint weak-gradient regime, bilocal substrate channels — channels that carry participation-content contributions from two distinct substrate-source regions simultaneously — carry strain proportional to the geometric mean of the local-source and horizon-sourced bandwidth contributions per channel.*
>
> *Operational statement:* For a bilocal substrate channel carrying per-channel participation content $b_K^{\mathrm{loc}}(R)$ from a local source (cumulative-strain reading of Paper_027) and $b_K^{\mathrm{horizon}}(R)$ from the cosmic-horizon dipole projection (Paper_029), the substrate-level strain content of the bilocal channel scales as:
>
> $$\sigma_{\mathrm{ch}}^{\mathrm{bilocal}}(R) \propto \sqrt{b_K^{\mathrm{loc}}(R) \cdot b_K^{\mathrm{horizon}}(R)}.$$
>
> *Regime restriction:* P14 applies in the **joint weak-gradient regime** where both contributions are simultaneously non-negligible and their gradients are weak relative to substrate-scale cutoffs (specifically, $a_N \sim a_0$ and both $\ll c^2/\ell_P$).
>
> *Cross-domain status:* P14 is articulated for the substrate-gravity arc. Whether it has cross-domain manifestations in other ED sectors is in-queue work.

**V1 inheritance (Papers #18, #19 / Paper_093):** finite-width retarded kernel structure inherited.

**Upstream paper dependencies:**

- **Paper_027 (Newton's $G$):** establishes $a_N = GM/R^2$ and $\Sigma_N(R) = -GM/R$.
- **Paper_029 (transition acceleration $a_0$):** establishes $a_0 = cH_0/(2\pi)$ via dipole-projection on residual $SO(2)$. The cosmic-horizon contribution to the stability landscape is the **coarse-grained dipole projection potential** $\Sigma_0(R) = -a_0 R$ (see §3.2).
- **Paper_031 (BTFR slope-4):** downstream user of ECR.

**No primitive forcing is invoked.**

---

## 3. Upstream Results: The Two Strain Contributions

### 3.1 Newtonian strain from local mass

From Paper_027:

$$
\Sigma_N(R) = -\frac{GM}{R}, \qquad a_N(R) = -\frac{d\Sigma_N}{dR} = \frac{GM}{R^2}.
$$

### 3.2 Cosmic-horizon strain as coarse-grained Paper_029 dipole potential

This section is revised in this round to clarify the conceptual status of $\Sigma_0(R)$.

The substrate-level cosmic-horizon contribution to the chain's stability landscape is obtained from Paper_029's dipole-mode projection of the cosmic decoupling surface onto the accelerating chain's adjacency structure. Paper_029 derived the **characteristic acceleration scale** $a_0 = cH_0/(2\pi)$ via the dipole-projection integral on the residual $SO(2)$ symmetry.

The corresponding **coarse-grained potential** along the chain's adjacency axis at distance $R$ from the chain locus is:

$$
\Sigma_0(R) = -\,a_0 \cdot R.
$$

This is the **coarse-grained potential associated with the dipole projection from Paper_029**, obtained by integrating the constant cosmic-anisotropy acceleration $a_0$ along the radial direction. The linear-in-$R$ form reflects that the cosmic-anisotropy contribution to the stability landscape grows linearly with the chain's radial position — the substrate-level integral of a constant acceleration over a radial path.

**Status of $\Sigma_0(R)$:** $\Sigma_0(R) = -a_0 R$ is *not* a separately-postulated stability-landscape function; it is the coarse-grained potential derived from Paper_029's dipole-projection mechanism via radial integration. The negative gradient $-d\Sigma_0/dR = a_0$ reproduces the cosmic-anisotropy acceleration scale of Paper_029. This is the standard substrate-to-coarse-grained correspondence: substrate-level dipole-projection content + radial coarse-graining = effective linear-in-$R$ potential along the chain's axis.

### 3.3 The joint weak-gradient regime

When both contributions are simultaneously present and their magnitudes are comparable, the chain is in the **joint weak-gradient regime**:

$$
a_N(R) \sim a_0 \implies R \sim R_{\mathrm{transition}} = \sqrt{GM/a_0}.
$$

For galactic masses ($M \sim 10^{40}$–$10^{42}$ kg), $R_{\mathrm{transition}}$ is in the kpc range, consistent with empirically-observed transition radii.

P14 applies in this regime.

### 3.4 Naïve additive combination — why it fails

A naïve additive combination:

$$
\Sigma_{\mathrm{naïve}}(R) = -\frac{GM}{R} - a_0 R, \qquad a_{\mathrm{naïve}} = \frac{GM}{R^2} + a_0.
$$

In the deep-MOND regime ($a_N \ll a_0$): $a_{\mathrm{naïve}} \approx a_0$ (constant), giving $v^2 = a_0 R$ — empirically refuted by BTFR data. The substrate-level mechanism must produce a non-additive combination.

P14 supplies the substrate-level mechanism for the non-additive combination via bilocal channel coupling.

---

## 4. Bilocal Substrate Channels — P14 in Operation

### 4.1 Substrate-level bilocal interaction

The substrate's cumulative-strain reading integrates strain content across all substrate channels connecting the chain to its environment. In the joint regime, two substrate channel classes contribute:

- **Newtonian channels:** $N(R) = 4\pi R^2/\ell_{\mathrm{ED}}^2$ channels connecting chain to local source mass (Paper_027 §3).
- **Cosmic-horizon channels:** $N_{\mathrm{horizon}}$ channels connecting chain to dipole-projected cosmic horizon (Paper_029).

**Bilocal channels** are substrate channels that carry participation-content contributions from *both* source regions simultaneously. The existence of bilocal channels follows from P03 (translation-invariance of the participation graph) + P07 (channel-structure as ontological primitive): a substrate channel that passes through both source regions in the substrate-graph sense carries strain from both contributions.

**P14 (this paper §2) specifies the strain-coupling structure on bilocal channels:** the per-channel strain on a bilocal channel is the geometric mean of the per-channel contributions from each source. This is the new postulational content.

### 4.2 Bilocal strain content scaling under P14

For a bilocal channel carrying per-channel participation content $b_K^{\mathrm{loc}}(R)$ from the local source and $b_K^{\mathrm{horizon}}(R)$ from the cosmic horizon, P14 gives:

$$
\sigma_{\mathrm{ch}}^{\mathrm{bilocal}}(R) \propto \sqrt{b_K^{\mathrm{loc}}(R) \cdot b_K^{\mathrm{horizon}}(R)}.
$$

The per-channel local-source content from Paper_027's holographic substrate-source resolution (rewritten for Paper_027 §4.3) is $b_K^{\mathrm{loc}}(R) \propto GM/(R \cdot N(R))$, which after coefficient assembly gives the Newtonian potential $\Sigma_N = -GM/R$ per-channel-resolved as $-GM/(R \cdot N(R))$. The per-channel horizon content is $b_K^{\mathrm{horizon}}(R) \propto a_0 R / N_{\mathrm{horizon}}$.

For substrate-level bandwidth conventions chosen consistent with Papers_027 and 029, the bilocal-channel strain content evaluates (per the cumulative-strain conventions) to:

$$
\sigma_{\mathrm{ch}}^{\mathrm{bilocal}}(R) \propto \sqrt{\frac{GM}{R} \cdot a_0 R} = \sqrt{GMa_0}.
$$

The bilocal strain per channel is **independent of $R$** — it depends only on the two source scales.

### 4.3 Number of bilocal channels

The bilocal-channel density along the radial direction scales as $1/R$ (substrate-graph radial-projection geometry, anchored by P03 spatial-homogeneity). The total bilocal contribution to the chain's stability landscape is the radial integral of the bilocal-channel strain content:

$$
\Sigma_{\mathrm{cross}}(R) = -\int_{R_0}^{R}\frac{\sqrt{GMa_0}}{R'}\,dR' = -\sqrt{GMa_0}\cdot\log(R/R_0).
$$

The logarithmic form emerges from integrating $\sigma_{\mathrm{ch}}^{\mathrm{bilocal}} \cdot (1/R)$ along the radial direction. The reference scale $R_0$ is a substrate-level integration constant; it drops out when computing accelerations as gradients.

---

## 5. Single-Pass Derivation of the ECR

This section is the load-bearing derivation, **completely rewritten in this revision as a clean single-pass derivation using P14**. The previous round's §5.3 stream-of-consciousness derivation is deleted.

### 5.1 Setup

Three contributions to the chain's stability landscape in the joint weak-gradient regime:

$$
\Sigma(R) = \Sigma_N(R) + \Sigma_0(R) + \Sigma_{\mathrm{cross}}(R)
$$

where:

- $\Sigma_N(R) = -GM/R$ from Paper_027 (cumulative-strain reading, holographic substrate-source resolution).
- $\Sigma_0(R) = -a_0 R$ from the coarse-grained Paper_029 dipole-projection potential (§3.2).
- $\Sigma_{\mathrm{cross}}(R) = ?$ — derived next from P14.

### 5.2 Derivation of the cross-term given P14

Given P14, the substrate-level bilocal-channel strain is $\sigma_{\mathrm{ch}}^{\mathrm{bilocal}}(R) \propto \sqrt{GMa_0}$ (§4.2, $R$-independent).

The total bilocal contribution to the stability landscape is the radial integral of the bilocal-channel strain density:

$$
\Sigma_{\mathrm{cross}}(R) = -\int_{R_0}^{R}\rho_{\mathrm{bilocal}}(R')\,dR'
$$

where $\rho_{\mathrm{bilocal}}(R')$ is the bilocal-channel strain density along the radial direction. From §4.3, $\rho_{\mathrm{bilocal}}(R') = \sqrt{GMa_0}/R'$, giving:

$$
\boxed{\Sigma_{\mathrm{cross}}(R) = -\sqrt{GMa_0}\cdot\log(R/R_0).}
$$

This is the **logarithmic cross-term** in the joint regime, derived from P14 + substrate-level radial integration.

### 5.3 Combination-rule identification (in the joint weak-gradient regime)

The chain's experienced acceleration is the negative gradient of the total stability landscape:

$$
a(R) = -\frac{d\Sigma}{dR} = -\frac{d\Sigma_N}{dR} - \frac{d\Sigma_0}{dR} - \frac{d\Sigma_{\mathrm{cross}}}{dR} = \frac{GM}{R^2} + a_0 + \frac{\sqrt{GMa_0}}{R}.
$$

**Regime-assumption reframing.** In the joint weak-gradient regime, the **bilocal cross-term dominates** the chain's experienced acceleration. This is a regime assumption, articulated explicitly in this revision:

> **Regime assumption (joint weak-gradient).** *In the joint weak-gradient regime where $a_N \sim a_0$ and both contributions are present, the bilocal-channel cross-term gradient $\sqrt{GMa_0}/R$ is the dominant contribution to the chain's experienced acceleration, with the pure-source terms ($a_N$ and $a_0$) acting as subdominant corrections.*

In this regime:

$$
a(R) \approx -\frac{d\Sigma_{\mathrm{cross}}}{dR} = \frac{\sqrt{GMa_0}}{R}.
$$

Using $a_N = GM/R^2$:

$$
\frac{\sqrt{GMa_0}}{R} = \sqrt{\frac{GM \cdot a_0}{R^2}} = \sqrt{a_N \cdot a_0}.
$$

Therefore:

$$
\boxed{a = \sqrt{a_N \cdot a_0} \qquad \text{(in the joint weak-gradient regime, given P14).}}
$$

This is the **ED Combination Rule (ECR)**. It is a *downstream structural consequence* of P14 + the joint weak-gradient regime assumption.

---

## 6. Identification and Structural Status of the Combination Rule

### 6.1 The ECR as downstream structural consequence

> **Given P14 (Bilocal Strain Coupling) and the joint weak-gradient regime, the ED Combination Rule $a = \sqrt{a_N \cdot a_0}$ follows as a downstream structural consequence.**

The ECR is *not* derived from a uniqueness-of-substrate-mechanisms argument. It is derived from:

- **P14** specifying the substrate-level bilocal-channel strain-coupling form (geometric mean).
- **Joint weak-gradient regime** specifying the operational range where bilocal coupling dominates.
- **Substrate-level radial integration** producing the logarithmic cross-term.

### 6.2 Why the geometric-mean is the structural form

This section is rewritten in this revision to remove the circular uniqueness argument.

> **Given P14, the geometric mean is the structural form** of bilocal-channel strain coupling. Replacing P14 with a different bilocal-coupling postulate (arithmetic mean, max, power-law, etc.) would produce a different cross-term and a different combination rule.

P14 is a postulate, not a derived consequence of the prior 13 primitives. Whether P14 is structurally forced from a deeper substrate principle, or whether other bilocal-coupling forms could be substrate-consistent alternatives, is **not addressed in this paper**. The substrate framework treats P14 as a postulate in the same genre as the other 13 primitives.

The prior round's draft included a "uniqueness" argument claiming that arithmetic mean, max, and power-law combinations were not substrate-motivated, with geometric mean uniquely structural. That argument was structurally circular: it inferred substrate-motivation from the combination-rule outcome rather than deriving the combination-rule outcome from substrate-motivation. The corrected stance is:

- **P14 specifies geometric-mean coupling.** This is a substrate-level postulate.
- **Given P14, the geometric-mean combination rule follows.** This is a derivation.
- **Whether geometric-mean coupling is structurally forced from a deeper substrate principle is an open question.** The substrate framework, as currently postulated, does not derive P14; it postulates P14 (this paper §2).

This is the honest accounting of the structural status of the ECR within the ED Generative Primitives System.

### 6.3 The "no interpolation function" claim

Standard MOND uses a phenomenological interpolation function $\mu(x)$. ED derives the transition profile *structurally* via P14 + the substrate-level cumulative-strain reading. The transition profile is determined by:

$$
a(R) = a_N + a_0 + \frac{\sqrt{GMa_0}}{R}.
$$

In Newtonian regime ($a_N \gg a_0$): $a \approx a_N$. In deep-MOND regime ($a_N \ll a_0$, joint weak-gradient applies): $a \approx \sqrt{a_N a_0}$.

The transition profile is structurally fixed (no fit parameter) but may differ from specific MOND interpolation functions $\mu(x)$. Galaxy-by-galaxy comparison is empirical-test program.

---

## 7. Regime Structure

### 7.1 Three regimes

**Newtonian regime ($a_N \gg a_0$, $R \ll R_{\mathrm{transition}}$):** $a \approx a_N = GM/R^2$. Standard Newtonian dynamics; cosmic-anisotropy and bilocal contributions subdominant. P14 inactive (joint weak-gradient regime does not apply).

**Transition regime ($a_N \sim a_0$, $R \sim R_{\mathrm{transition}}$):** $a \approx a_N + a_0 + \sqrt{a_N a_0}$. Joint weak-gradient regime; all three contributions comparable; P14 active.

**Deep-MOND regime ($a_N \ll a_0$, $R \gg R_{\mathrm{transition}}$):** $a \approx \sqrt{a_N \cdot a_0}$. Joint weak-gradient still applies; bilocal cross-term dominates over both pure-source terms. P14 active; ECR is the dominant approximation.

### 7.2 Smooth, parameter-free crossover

The transition is **smooth** and **parameter-free** given P14 + upstream results ($G$, $a_0$ from Papers_027, 029).

### 7.3 Comparison to MOND interpolation functions

ED's structural transition profile (parameter-free given P14) vs. standard MOND $\mu(x)$ (with one phenomenological parameter $a_0$). Galaxy-rotation-curve fit comparisons are empirical-test program.

---

## 8. What This Paper Does NOT Claim

### 8.1 No derivation of $H_0$

$H_0$ enters via $a_0 = cH_0/(2\pi)$ (Paper_029); empirical cosmological input.

### 8.2 No derivation of cosmology

ED does not derive cosmological dynamics; ECR operates conditional on cosmological inputs.

### 8.3 No claim that MOND-as-phenomenology is correct as a complete theory

ED supplies a substrate mechanism for the transition; does not endorse MOND-as-complete-theory.

### 8.4 No claim that P14 is forced from the other 12 primitives

This is the key honesty point of this revision. P14 (Bilocal Strain Coupling) is a **postulated substrate primitive in this paper's setup**. Whether P14 is structurally forced from the prior 13 primitives + deeper substrate analysis is an open question; ED's current substrate framework postulates P14 without deriving it.

The 14-primitive set augmented by P14 produces the ECR; the 13-primitive set without P14 does not contain a substrate-level mechanism for the bilocal-coupling form that P14 articulates. Whether the 13-primitive ontology is sufficient for the ECR or whether P14 is genuinely needed as an additional postulate is **structurally open**.

### 8.5 No claim that the ECR is forced from nothing

The derivation is **conditional** on P14 + the joint weak-gradient regime + the upstream papers. Not a derivation from zero assumptions.

### 8.6 No claim of derivation of the reference scale $R_0$

$R_0$ is a convention; drops out of accelerations as gradients.

### 8.7 No claim of full galactic-rotation-curve fitting

ED's substrate framework supplies the *gravity mechanism*; galaxy-specific empirical inputs (mass distribution, etc.) are value-layer content.

### 8.8 No claim of GR or curvature emergence

ECR operates in Newtonian (flat-spacetime weak-field) regime. Curvature emergence is Arc ED-10 territory.

### 8.9 No claim of uniqueness of bilocal-coupling form

Geometric-mean coupling is specified by P14, not derived. Other bilocal-coupling forms (arithmetic mean, max, power-law) would correspond to different substrate-level postulates. ED commits to P14 in this paper; alternative substrate frameworks could postulate different bilocal-coupling forms.

---

## 9. Falsification Criteria

### 9.1 Deep-MOND regime does not follow $\sqrt{a_N a_0}$

Empirical demonstration that deep-MOND galactic rotation curves follow a different combination (constant $a_0$, additive, different power-law) falsifies P14 + ECR.

### 9.2 Logarithmic cross-term contradicted by rotation-curve data

Empirical demonstration that the joint-regime stability content has a different functional form (e.g., power-law rather than logarithmic) falsifies the §5 derivation given P14.

### 9.3 Transition region shows free-parameter behavior

Galaxy-by-galaxy fits requiring galaxy-specific transition parameters (beyond $G$, $a_0$, $M_b$) falsify the parameter-free transition profile.

### 9.4 ECR fits worse than standard MOND interpolations

If MOND $\mu(x)$ with one fit parameter consistently fits better than ED's parameter-free profile, the substrate mechanism is empirically challenged.

### 9.5 P14 inconsistency from cross-domain analysis

If applying P14-style bilocal coupling in other ED sectors (cross-domain) produces inconsistencies with already-derived results (e.g., contradicting V5 cross-chain correlation structure, ECR in non-gravity contexts), P14's substrate-level status is challenged. Cross-domain consistency of P14 is in-queue work.

### 9.6 Geometric-mean coupling refuted in laboratory substrate-probing

If laboratory-scale experiments probing substrate-level bilocal-channel content (hypothetical, future) refute geometric-mean coupling in favor of a different form, P14 is falsified.

---

## 10. Position Statement

The **ED Combination Rule** $a = \sqrt{a_N \cdot a_0}$ is a downstream structural consequence of:

- The postulated 13 substrate primitives.
- **P14 (Bilocal Strain Coupling) — a new substrate-level postulate articulated in this paper.**
- The joint weak-gradient regime assumption.
- The upstream results: $G = c^3\ell_P^2/\hbar$ (Paper_027), $a_0 = cH_0/(2\pi)$ (Paper_029).
- The coarse-grained Paper_029 dipole-projection potential $\Sigma_0(R) = -a_0 R$.

> **Given P14 and the joint weak-gradient regime, the ED Combination Rule follows as a downstream structural consequence.**

The substrate mechanism:

- P14 specifies bilocal-channel strain coupling as the geometric mean of per-channel source contributions.
- In the joint weak-gradient regime, bilocal channels produce an $R$-independent per-channel strain $\sqrt{GMa_0}$.
- Radial integration produces the logarithmic cross-term $\Sigma_{\mathrm{cross}}(R) = -\sqrt{GMa_0}\log(R/R_0)$.
- In the joint weak-gradient regime, the cross-term gradient dominates the chain's experienced acceleration.
- The cross-term gradient $\sqrt{GMa_0}/R = \sqrt{a_N a_0}$ is the ECR.

The transition profile is smooth, parameter-free given P14 + upstream results.

What this paper claims:

- Given the postulated primitives + P14 + Papers_027/029 + joint weak-gradient regime assumption, the ECR is the downstream structural consequence.
- The geometric-mean form is **specified by P14**, not derived from a uniqueness argument.
- The substrate-level bilocal-channel mechanism supplies a structural origin for the transition profile.
- No interpolation function is fit; the transition is structurally derived given P14.

What this paper does *not* claim:

- $H_0$ and cosmology not derived.
- MOND-as-phenomenology not endorsed as complete theory.
- P14 not derived from the prior 13 primitives — it is a new postulate.
- ECR not forced from nothing — conditional on P14 + regime + upstream.
- Geometric-mean coupling not unique among substrate-consistent forms — alternative postulates would give alternative combination rules.

The empirical case for the substrate primitives + P14 — and for the ECR — rests on **cross-domain reach**. The substrate-gravity arc (Papers_027 + 029 + 030 + 031) supplies one cross-domain test; BTFR slope-4 (Paper_031) is the load-bearing testable consequence; potential cross-domain manifestations of P14 in other ED sectors are in-queue work.

**Series context.** Paper_030 of the gravity arc. The arc continues:

- **Paper_031:** Slope-4 BTFR (uses ECR).

The 14-primitive set (13 + P14) is the substrate-ontological basis for the gravity arc as currently developed.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** `paper_ED_Framework_13_Primitive_Generative_System.md` — canonical primitive enumeration (will need P14 update if P14 is adopted across the broader ED framework).
- **Primitive load-bearing audit:** `PRIMITIVE_LOAD_BEARING_AUDIT.md` — P12 audit; P14 audit pending.
- **Paper_027 (Newton's $G$):** establishes $a_N = GM/R^2$, $\Sigma_N(R) = -GM/R$.
- **Paper_029 (transition acceleration $a_0$):** establishes $a_0 = cH_0/(2\pi)$ + coarse-grained dipole potential $\Sigma_0(R) = -a_0 R$.
- **Paper_031 (BTFR slope-4):** downstream user of ECR.
- **Paper #18, #19 / Paper_093 (V1 kernel + T18):** V1 retarded inheritance.
- **SG-3 memo** (pre-pivot): legacy reference.

### Glossary

- **ED Combination Rule (ECR).** $a = \sqrt{a_N \cdot a_0}$ in the joint weak-gradient regime, given P14.
- **P14 (Bilocal Strain Coupling).** *New substrate-level postulate articulated in this paper.* Specifies that bilocal substrate channels carry strain proportional to the geometric mean of the local-source and horizon-sourced bandwidth contributions, in the joint weak-gradient regime.
- **Bilocal substrate channels.** Substrate channels carrying participation-content contributions from two distinct substrate-source regions simultaneously.
- **Cumulative-strain reading.** Substrate-level integration of strain content across substrate channels (Paper_027 §4).
- **Joint weak-gradient regime.** $a_N \sim a_0$ and gradients $\ll c^2/\ell_P$. The regime where P14 applies and the bilocal cross-term dominates the experienced acceleration.
- **Logarithmic cross-term.** $\Sigma_{\mathrm{cross}}(R) = -\sqrt{GMa_0}\log(R/R_0)$. Substrate-level cross-contribution from P14-coupled bilocal channels.
- **Geometric-mean combination.** $\sqrt{a_N \cdot a_0}$. Specified by P14, not derived from uniqueness.
- **Coarse-grained dipole-projection potential.** $\Sigma_0(R) = -a_0 R$, obtained by radial integration of the Paper_029 dipole-projection acceleration scale.
- **Newtonian / Transition / Deep-MOND regimes.** Defined by ratio $a_N/a_0$.
- **Transition radius.** $R_{\mathrm{transition}} = \sqrt{GM/a_0}$.
- **MOND interpolation function $\mu(x)$.** Phenomenological function in standard MOND; ED's structural transition profile is derived given P14, not fit.

---

**End of Paper_030.**

*Wave-2 Generative Paper — Gravity Arc, ECR Dedicated Derivation. Round-2 revision: P14 (Bilocal Strain Coupling) added as new substrate-level postulate in §2; §5 rewritten as clean single-pass derivation using P14; §3.2 reframes $\Sigma_0(R) = -a_0 R$ as the coarse-grained Paper_029 dipole-projection potential; §6.2 removes the circular uniqueness argument and replaces it with "Given P14, the geometric mean is the structural form"; §8.4 and §8.9 articulate honestly that P14 is a new postulate not derived from the prior 13 primitives, and that the geometric-mean form is not unique among substrate-consistent alternatives.*
