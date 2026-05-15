# Paper_031 — Slope-4 Baryonic Tully-Fisher Relation with Zero Intrinsic Scatter

**Series:** Event Density (ED) Generative Papers — Wave-2 rewrite of the gravity arc
**Author:** Allen Proxmire
**Status:** Publication draft (revision: §1.3 repo structure updated; §3 ECR dependency on Paper_030 + P14 made explicit)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/gravity/Paper_031_BTFR.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_031_BTFR_FIXED.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Abstract

The Event Density (ED) substrate is a 13-primitive generative system. This paper develops the **baryonic Tully-Fisher relation (BTFR)**:

$$
v_{\mathrm{flat}}^4 = G \cdot M_b \cdot a_0
$$

as a **downstream structural consequence** of four prior results in the ED gravity arc: Newton's law with $G = c^3\ell_P^2/\hbar$ (Paper_027), the transition acceleration $a_0 = cH_0/(2\pi)$ (Paper_029), the substrate-level **ED Combination Rule** $a = \sqrt{a_N \cdot a_0}$ derived in Paper_030 (conditional on P14, Bilocal Strain Coupling), and the standard circular-orbit kinematic condition $v^2 / R = a$. The BTFR slope is **exactly 4** — not 3, not 5 — because the squaring of $v^2$ in $v^4$ is structurally fixed by the circular-orbit condition combined with the multiplicative form of the ECR. The **intrinsic scatter is zero** in the deep-MOND asymptotic regime ($a_N \ll a_0$) because the radial dependence cancels exactly: $v^2 = R\sqrt{a_N a_0} = \sqrt{GM_b a_0}$ depends only on baryonic mass $M_b$ and the substrate-level transition acceleration $a_0$, not on the radial profile of $M_b(R)$. **No halo modeling is invoked. No free parameters are introduced.** Empirical BTFR measurements (McGaugh-Lelli-Schombert 2016 and subsequent surveys) are consistent with slope-4 and small residual scatter attributable to observational uncertainty. The paper makes no claim to derive $H_0$ or specific $M_b$ values, no claim that BTFR is forced from nothing, no claim that MOND is correct as a complete theory of galactic dynamics, and no claim about dark-matter particle content. The empirical case for the substrate primitives + P14 — and for the slope-4 + zero-scatter prediction — rests on cross-domain reach.

---

## 1. Introduction

### 1.1 What this paper does

The **baryonic Tully-Fisher relation (BTFR)** is one of the tightest empirical relations in galactic astrophysics: the asymptotic flat rotation velocity $v_{\mathrm{flat}}$ of a galaxy is related to its total baryonic mass $M_b$ by a power law with slope very close to 4:

$$
v_{\mathrm{flat}}^n \propto M_b, \quad n \approx 4.
$$

Observational data (McGaugh 2012; Lelli, McGaugh, Schombert 2016) give $n = 3.95 \pm 0.08$, consistent with $n = 4$ to within statistical error. The relation holds across galaxies spanning ~4 orders of magnitude in baryonic mass with remarkably small scatter.

In ED's substrate framework, BTFR slope-4 emerges as the **downstream structural consequence** of:

1. Newton's law $a_N = GM/R^2$ (Paper_027).
2. The transition acceleration $a_0 = cH_0/(2\pi)$ (Paper_029).
3. The **ED Combination Rule** $a = \sqrt{a_N \cdot a_0}$ derived in **Paper_030** (conditional on **P14, Bilocal Strain Coupling**).
4. The circular-orbit condition $v^2/R = a$ (standard kinematics).

Combining these yields:

$$
v_{\mathrm{flat}}^4 = G M_b a_0.
$$

The slope is *exactly 4* — structurally fixed by the squaring of $v^2$ in the centripetal-acceleration condition combined with the ECR's multiplicative form. The intrinsic scatter is *zero* in the deep-MOND asymptotic regime because the radial profile of $M_b(R)$ cancels exactly. No halo modeling, no free parameters.

### 1.2 Why BTFR matters in the ED generative system

The empirical BTFR is one of the strongest constraints on galactic gravitational physics. Three frameworks attempt to account for it:

- **Dark-matter cosmology:** BTFR slope-4 emerges from tuned halo profile distributions; the tightness is a coincidence of the tuning.
- **MOND-as-phenomenology:** BTFR slope-4 is built in by construction.
- **ED substrate gravity:** BTFR slope-4 emerges as the unique downstream consequence of the substrate-level cumulative-strain reading (Paper_027) + cosmic-horizon dipole projection (Paper_029) + ECR (Paper_030, conditional on P14). The slope is *derived*, not fit.

This matters for three reasons:

- **Predictive content.** ED's substrate framework makes a specific prediction (slope-4, zero intrinsic scatter) without free parameters.
- **Cross-domain coherence.** BTFR is the natural product of Papers_027 + 029 + 030. It completes the gravity arc.
- **Falsifiability.** If empirical BTFR slope deviates from 4 (beyond observational uncertainty), or if intrinsic scatter is found in the deep-MOND regime, the substrate-level mechanism is falsified.

### 1.3 How this fits into the gravity arc

The ED substrate-gravity arc consists of four papers (revised structure in this round):

- **Paper_027:** Newton's $G = c^3\ell_P^2/\hbar$ from substrate constants.
- **Paper_029:** Transition acceleration $a_0 = cH_0/(2\pi)$ from cosmic-decoupling-surface dipole projection.
- **Paper_030:** **Full structural derivation of the ED Combination Rule $a = \sqrt{a_N \cdot a_0}$**, given postulate **P14 (Bilocal Strain Coupling)** and the joint weak-gradient regime.
- **Paper_031 (this paper):** Slope-4 BTFR $v^4 = GM_b a_0$ with zero intrinsic scatter, composing Paper_027 + Paper_029 + Paper_030 + circular-orbit kinematics.

**Repo-structure note (revised in this round).** The ECR derivation lives in **Paper_030 as a dedicated paper**, not in this paper. Paper_031 *uses* the ECR result (Paper_030 §6.1) as a structural step in the BTFR derivation; it does *not* re-derive the ECR. An earlier draft of the arc structure folded the ECR derivation into Paper_031; that structure is **no longer in effect**. The current arc structure separates ECR derivation (Paper_030) from BTFR application (Paper_031) for cleaner scope and easier cross-reference.

The four papers together produce the complete ED substrate-level account of galactic gravity: Newton in the strong-acceleration regime, MOND-class transition at $a_0$, multiplicative combination in the joint regime (via P14), and flat rotation curves with slope-4 BTFR in the deep-MOND regime — all from the postulated substrate primitives + P14.

---

## 2. Primitive Inputs (postulated, not derived in this paper)

This paper takes the following Event Density (ED) substrate primitives as **postulated within the ED Generative Primitives System**:

- **P02 (Participation as primitive relation).**
- **P03 (Channel + locus indexing; spatial homogeneity).**
- **P04 (Bandwidth as non-negative additive scalar).**
- **P07 (Channel structure as ontological primitive).**
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).**
- **P11 (Commitment irreversibility).**
- **P12 (Stability landscape).** Load-bearing for the substrate-level mechanism producing the ECR's logarithmic cross-term (in Paper_030).
- **P13 (Time homogeneity).**
- **P14 (Bilocal Strain Coupling).** Postulate articulated in Paper_030 §2. **Load-bearing in this paper as an inherited dependency:** the ECR result used here (§3 below) is conditional on P14.

**V1 inheritance (Papers #18, #19 / Paper_093):** finite-width retarded kernel structure inherited as in Papers_027, 029, 030.

**Upstream paper dependencies:**

- **Paper_027 (Newton's $G$):** establishes $a_N = GM/R^2$ with $G = c^3\ell_P^2/\hbar$.
- **Paper_029 (transition acceleration $a_0$):** establishes $a_0 = cH_0/(2\pi)$.
- **Paper_030 (ECR derivation, conditional on P14):** establishes $a = \sqrt{a_N \cdot a_0}$ in the joint weak-gradient regime. **Direct upstream input.**
- **Standard kinematics:** the circular-orbit condition $v^2/R = a$.

**Empirical inputs:** $c$, $\hbar$, $H_0$, $\ell_P$, per-galaxy $M_b$.

**No primitive forcing is invoked.**

---

## 3. Newton + $a_0$ + ED Combination Rule

### 3.1 Summary of Paper_027 and Paper_029

From Paper_027:

$$
a_N = \frac{GM}{R^2}, \qquad G = \frac{c^3 \ell_P^2}{\hbar}.
$$

From Paper_029:

$$
a_0 = \frac{cH_0}{2\pi} \approx 1.08 \times 10^{-10}\,\mathrm{m/s^2}.
$$

These are the two upstream acceleration scales.

### 3.2 The ECR taken from Paper_030

**The ECR used in this paper is taken from Paper_030 and is conditional on the bilocal-strain-coupling postulate (P14) introduced there.** This paper does not re-derive the ECR; the derivation lives in Paper_030 §§4–6.

The result of Paper_030, used here as a structural step:

$$
\boxed{a = \sqrt{a_N \cdot a_0} \qquad \text{(ECR, from Paper\_030, given P14 + joint weak-gradient regime)}}
$$

**Conditional structure.** The ECR is a downstream structural consequence of:

- The substrate primitives P02 + P03 + P04 + P07 + P08 + P11 + P12 + P13.
- P14 (Bilocal Strain Coupling) — articulated in Paper_030 §2.
- V1 inheritance (Papers #18, #19 / Paper_093).
- The joint weak-gradient regime assumption.
- The upstream results: $G$ from Paper_027 and $a_0$ from Paper_029.

This paper inherits the ECR as a substrate-derived structural result with the conditional dependency on P14 made explicit. If P14 is structurally challenged (see Paper_030 §8.4 honest accounting of P14's postulational status), the ECR — and consequently the BTFR slope-4 + zero-scatter result of this paper — is structurally challenged accordingly. The empirical case is therefore joint: BTFR slope-4 tests the substrate framework + Paper_030's ECR + P14 simultaneously.

### 3.3 The three regimes (summary)

| Regime | Acceleration | Empirical |
|---|---|---|
| Newtonian ($a_N \gg a_0$) | $a \approx a_N = GM/R^2$ | Solar system, inner galactic regions |
| Joint weak-gradient ($a_N \sim a_0$) | $a \approx \sqrt{a_N \cdot a_0}$ (P14 active) | Galactic outer regions, transition zone |
| Deep-MOND ($a_N \ll a_0$) | $a \approx \sqrt{a_N \cdot a_0}$ (P14 active) | Far outer galactic regions, dwarf galaxies |

The ECR is valid throughout the joint and deep-MOND regimes (where P14 applies). In the Newtonian regime, $a_N$ dominates and the ECR reduces to $a \approx a_N$ via the regime-restriction structure of P14 (Paper_030 §2). The asymptotic flat-rotation-curve behavior occurs in the deep-MOND regime, which is where BTFR slope-4 is most precisely defined and tested.

---

## 4. Circular-Orbit Condition

### 4.1 Newtonian kinematics

For a test object in a circular orbit at radius $R$:

$$
\frac{v^2}{R} = a
$$

where $v$ is orbital velocity and $a$ is total radial acceleration. Standard kinematics; not substrate-level content.

### 4.2 Substituting the ECR

In the deep-MOND regime where ECR applies (Paper_030 §6.1), $a \approx \sqrt{a_N \cdot a_0}$. Substituting:

$$
\frac{v^2}{R} = \sqrt{a_N \cdot a_0} = \sqrt{\frac{GM_b}{R^2} \cdot a_0} = \frac{\sqrt{GM_b a_0}}{R}.
$$

Multiplying both sides by $R$:

$$
v^2 = \sqrt{G M_b a_0}.
$$

Squaring:

$$
\boxed{v^4 = G \cdot M_b \cdot a_0.}
$$

This is the slope-4 baryonic Tully-Fisher relation.

### 4.3 What "flat rotation curve" means in this framework

A "flat rotation curve" is the empirical observation that, in galaxies at large radii:

$$
v(R) \approx v_{\mathrm{flat}} \quad \text{for } R \gtrsim R_{\mathrm{transition}}.
$$

Given the ECR (from Paper_030, conditional on P14), the circular-orbit kinematics produces constant rotation velocity at large radii, with $v_{\mathrm{flat}}$ uniquely determined by $M_b$ and $a_0$.

---

## 5. Why the Slope is Exactly 4

### 5.1 Structural derivation of the exponent

From §4.2:

$$
v^4 = G M_b a_0 \implies v \propto M_b^{1/4} \implies v^n \propto M_b \text{ requires } n = 4.
$$

The slope is *exactly* 4, structurally, because:

- The circular-orbit condition is *quadratic* in velocity: $v^2 = aR$.
- The ECR introduces $\sqrt{a_N \cdot a_0}$ — a *one-half-power* of $a_N$.
- Newton's law gives $a_N \propto M_b/R^2$ — a *first-power* of $M_b$.
- Composing: $v^2 = R \cdot \sqrt{(GM_b/R^2) \cdot a_0} = \sqrt{GM_b a_0}$, so $v^4 \propto M_b^1$.

The slope-4 emerges from the joint action of centripetal kinematics + ECR square-root + Newton's law's radial cancelation.

### 5.2 Why no other exponent is structurally allowed

Alternative combination rules give different slopes:

- **Additive** ($a = a_N + a_0$): in deep-MOND, $v^2 = a_0 R$; no $M_b$ dependence; slope undefined.
- **Maximum** ($a = \max$): same.
- **Quadratic** ($a^2 = a_N^2 + a_0^2$): in deep-MOND, $a \approx a_0$; same.
- **Cube-root** ($a^3 = a_N a_0^2$): slope-6.
- **Multiplicative geometric mean** (ECR, $a = \sqrt{a_N a_0}$): slope-4. ✓

Only the ECR — which Paper_030 derives from P14 — produces slope-4. The empirical slope-4 BTFR therefore tests P14 + Paper_030's ECR derivation jointly.

### 5.3 Slope-4 is dimensional / structural, not empirical-fit

Slope-4 is *not* a parameter ED tunes. It is a structural consequence of the dimensional structure of Newton's law, the ECR square-root, and circular kinematics — composed without free parameters.

---

## 6. Zero Intrinsic Scatter

### 6.1 The radial cancelation

From §4.2:

$$
v^2 = R \cdot \sqrt{a_N \cdot a_0} = R \cdot \sqrt{\frac{GM_b}{R^2} \cdot a_0} = \sqrt{GM_b a_0}.
$$

**The radius $R$ cancels exactly.** $v_{\mathrm{flat}}$ depends only on total baryonic mass $M_b$ and the substrate-level transition acceleration $a_0$. It does not depend on the radial distribution of $M_b(R)$, the radius at which the rotation curve is measured (in the asymptotic deep-MOND regime), or detailed potential structure at intermediate radii.

### 6.2 Why this produces zero intrinsic scatter

Empirical BTFR scatter has two sources:

- **Intrinsic scatter:** physical variation in $v_{\mathrm{flat}}$-$M_b$ beyond measurement.
- **Observational scatter:** measurement uncertainty.

In ED's substrate framework, the radial cancelation implies asymptotic $v_{\mathrm{flat}}$ is uniquely determined by $M_b$, independently of any galaxy-specific structural property. **Intrinsic scatter is zero**; all observed scatter must be observational.

This is sharp: as observational uncertainties shrink, residual scatter should approach zero in the deep-MOND asymptotic regime.

### 6.3 Current empirical state

McGaugh-Lelli-Schombert SPARC (2016): 175 galaxies, slope $3.95 \pm 0.08$, scatter ~0.1 dex. The question is whether the 0.1-dex scatter is observational (consistent with ED) or intrinsic (inconsistent). Current analyses suggest largely observational; tighter measurements could resolve.

### 6.4 The deep-MOND asymptotic qualifier

ED predicts zero intrinsic scatter **in the deep-MOND asymptotic regime** ($a_N \ll a_0$). In the joint weak-gradient regime ($a_N \sim a_0$), the ECR transitions between Newtonian and deep-MOND behavior, and some residual scatter is expected — domain-of-applicability statement, not falsification.

---

## 7. Cross-Domain Context

### 7.1 The gravity arc, completed

This paper completes the ED substrate-gravity arc:

- **Paper_027:** Newton's $G$.
- **Paper_029:** $a_0 = cH_0/(2\pi)$.
- **Paper_030:** ECR derivation given P14.
- **Paper_031 (this paper):** Slope-4 BTFR with zero intrinsic scatter.

All four papers together produce the substrate-level account of galactic gravity, with no halo modeling and no free parameters beyond $c$, $\hbar$, $H_0$, $\ell_P$, per-galaxy $M_b$.

### 7.2 Interaction with V5 and cross-domain invariants

The substrate-gravity arc uses V1 (single-chain vacuum kernel) as the dominant kernel. V5 (Paper #20 / Paper_090) operates in different contexts (soft-matter, BH, entanglement). The kernel hierarchy supplies the structural machinery for cross-locus interaction phenomena across ED.

### 7.3 Cross-checks across the gravity arc

BTFR slope-4 depends on:

- Paper_027's $G$ identification.
- Paper_029's $a_0$ identification.
- Paper_030's ECR derivation + P14.
- Standard circular-orbit kinematics.

Empirical BTFR data — slope-4 + small scatter — simultaneously tests all of these. Cross-domain coherence: BTFR is the load-bearing testable consequence of the gravity arc.

---

## 8. What This Paper Does NOT Claim

### 8.1 No derivation of $H_0$

$H_0$ enters via $a_0 = cH_0/(2\pi)$ (Paper_029). Empirical cosmological content.

### 8.2 No derivation of $M_b$ values

$M_b$ is astrophysical measurement, value-layer empirical.

### 8.3 No claim that BTFR is forced from nothing

Conditional on postulated primitives + V1 inheritance + P14 (via Paper_030) + Paper_027 + Paper_029 results.

### 8.4 No claim that MOND is correct as a complete theory

ED supplies a substrate mechanism for the empirical phenomenology MOND describes.

### 8.5 No claim about dark-matter distributions

ED's framework operates without halo modeling. Does not refute dark matter as particle content.

### 8.6 No claim of MOND-interpolation-function derivation

ED produces the deep-MOND asymptotic relation + ECR transition (Paper_030); not the full Milgrom $\mu(x)$.

### 8.7 No claim of universal validity across all galaxy classes

Prediction restricted to the deep-MOND asymptotic regime.

### 8.8 No claim of cosmological-evolution prediction

If $H_0$ varies with cosmic time, $a_0$ varies; BTFR coefficient varies. ED does not derive $H_0$ evolution.

### 8.9 No claim that the ECR derivation is contained in this paper

The ECR derivation is in **Paper_030**, not this paper. This paper uses the ECR result. The ECR's structural status (conditional on P14 — see Paper_030 §8.4) flows into this paper as inherited.

---

## 9. Falsification Criteria

### 9.1 Deep-MOND intrinsic scatter is non-zero

If tighter measurements reduce observational uncertainty but leave residual intrinsic scatter, the radial-cancelation prediction is falsified.

### 9.2 Slope deviates from 4

If empirical slope is significantly distinct from 4 beyond observational uncertainty, the substrate-level mechanism is falsified.

### 9.3 $a_0$ does not match $cH_0/(2\pi)$

If empirical $a_0 \neq cH_0/(2\pi)$ at resolved precision, Paper_029's mechanism is falsified, BTFR coefficient fails.

### 9.4 Multiplicative-combination-rule failure

If transition-regime rotation curves require non-multiplicative combination, the ECR (Paper_030, P14) is falsified, BTFR slope-4 with it.

### 9.5 Halo modeling required to reproduce BTFR

If empirical BTFR cannot be reproduced without halo modeling at high precision, the substrate framework's halo-free claim is falsified.

### 9.6 Outer-galactic rotation curves do not follow ECR

Systematic deviations from $v(R) \approx (GM_b(<R) a_0)^{1/4}$ falsify the substrate framework's BTFR prediction.

### 9.7 P14 falsified independently

If P14 (Paper_030's bilocal-strain-coupling postulate) is independently falsified (e.g., via cross-domain inconsistency or laboratory substrate-probing), Paper_030's ECR derivation fails, BTFR slope-4 follows.

---

## 10. Position Statement

The baryonic Tully-Fisher relation with slope **exactly 4** and **zero intrinsic scatter** in the deep-MOND asymptotic regime is **not** a phenomenological coincidence, an empirical fit, or a tuned halo result. In the ED Generative Primitives System, BTFR is a downstream structural identification:

$$
v_{\mathrm{flat}}^4 = G \cdot M_b \cdot a_0
$$

where:

- $G = c^3 \ell_P^2 / \hbar$ (Paper_027).
- $a_0 = cH_0/(2\pi)$ (Paper_029).
- The slope-4 form is structurally fixed by circular-orbit kinematics + ECR (Paper_030, conditional on P14) + Newton's law's radial cancelation.
- Zero intrinsic scatter follows from radial cancelation: $v^2 = R\sqrt{a_N a_0} = \sqrt{GM_b a_0}$ depends only on $M_b$.

**No halo modeling. No free parameters.** Empirically: slope $\approx 3.95 \pm 0.08$, scatter ~0.1 dex.

What this paper claims:

- Given the postulated primitives + V1 inheritance + Paper_027 + Paper_029 + **Paper_030 (ECR, conditional on P14)** + standard kinematics, slope-4 BTFR with zero intrinsic scatter is the unique downstream structural prediction.
- The substrate-level multiplicative geometric mean (ECR from Paper_030) is the unique combination rule producing slope-4.
- Radial cancelation in the deep-MOND regime is the structural mechanism for zero intrinsic scatter.
- The substrate framework supplies a mechanism for the empirically observed BTFR that neither MOND-as-phenomenology nor dark-matter-as-particle provides.

What this paper does *not* claim:

- $H_0$ and cosmology not derived.
- $M_b$ values are value-layer.
- BTFR not forced from nothing; conditional on the substrate ontology + P14.
- MOND not endorsed as complete theory.
- Dark matter not refuted as particle content.
- Full MOND interpolation function not derived.
- The ECR derivation is not contained in this paper; it lives in Paper_030.

**Series context.** Paper_031 of the gravity arc. The arc is complete with this paper:

- **Paper_027:** Newton's $G$.
- **Paper_029:** $a_0$.
- **Paper_030:** ECR (given P14).
- **Paper_031 (this paper):** BTFR slope-4 + zero scatter.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** `paper_ED_Framework_13_Primitive_Generative_System.md`.
- **Primitive load-bearing audit:** `PRIMITIVE_LOAD_BEARING_AUDIT.md` — P12 audit; P14 audit pending in Paper_030.
- **Paper_027 (Newton's $G$):** establishes $G = c^3\ell_P^2/\hbar$.
- **Paper_029 (transition acceleration $a_0$):** establishes $a_0 = cH_0/(2\pi)$.
- **Paper_030 (ECR, conditional on P14):** establishes $a = \sqrt{a_N \cdot a_0}$. **Direct upstream input.**
- **Paper #18, #19 / Paper_093 (V1 kernel):** finite-width retarded inheritance.
- **Paper #20 / Paper_090 (V5):** cross-domain context §7.2.

### Glossary

- **Baryonic Tully-Fisher Relation (BTFR).** $v_{\mathrm{flat}}^4 = GM_b a_0$. Asymptotic flat-rotation-velocity-baryonic-mass relation.
- **Slope-4.** Exponent $n = 4$ in $v^n \propto M_b$. Empirically $n \approx 3.95 \pm 0.08$.
- **Zero intrinsic scatter.** Substrate-level prediction that all empirical BTFR scatter is observational.
- **ED Combination Rule (ECR).** $a = \sqrt{a_N \cdot a_0}$. Derived in **Paper_030** conditional on P14 + joint weak-gradient regime. Used here as a structural step.
- **P14 (Bilocal Strain Coupling).** Postulate articulated in Paper_030 §2. Load-bearing upstream dependency of this paper's BTFR result.
- **Joint weak-gradient regime.** $a_N \sim a_0$. Where P14 applies and ECR holds.
- **Deep-MOND regime.** $a_N \ll a_0$. ECR dominates; flat rotation curves; BTFR slope-4 applies.
- **Circular-orbit condition.** $v^2/R = a$. Standard kinematics.
- **Radial cancelation.** Structural mechanism by which $R$-dependence cancels in $v^2 = R\sqrt{a_N a_0} = \sqrt{GM_b a_0}$, giving zero intrinsic scatter.
- **Asymptotic flat rotation curve.** $v(R) \approx v_{\mathrm{flat}}$ for $R \gtrsim R_{\mathrm{transition}}$.

---

**End of Paper_031.**

*Wave-2 Generative Paper — Gravity Arc Foundation. Round-2 revision: §1.3 updated to reflect the four-paper arc structure (Papers_027 + 029 + 030 + 031) with the ECR derivation living in Paper_030, not folded into this paper; §3.2 added explicit sentence noting the ECR is taken from Paper_030 and is conditional on P14 (Bilocal Strain Coupling) introduced there. BTFR derivation and zero-scatter argument unchanged.*
