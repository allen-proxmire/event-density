# Arc Hawking — Memo 6: Semiclassical Equivalence and Deviation Structure

**Status:** Audit memo. Conditional on H-1 (Planck spectrum), H-2 (greybody factors), H-3 (Page rate), H-4 (V5 cutoff and motif corrections), H-5 (information correlations). No new primitives. Identification-not-derivation discipline observed: standard semiclassical Hawking is identification target throughout, never as derivation premise.

**Date:** 2026-05-09

---

## 1. The CANDIDATE Statement

Restated and consolidated from the H-arc cumulative results:

> **CANDIDATE (H6).** *At leading-order DCGT coarse-graining, ED reproduces every ingredient of standard semiclassical Hawking radiation: surface gravity $\kappa$, Bogoliubov-equivalent V5 cross-chain correlations, Regge-Wheeler effective potential, Planck distribution, Regge-Wheeler / Teukolsky greybody factors, Page evaporation rate $-\alpha_{\mathrm{Page}}/M^2$, and the Page curve $S_{\mathrm{rad}}(t)$ with $t_{\mathrm{Page}} \approx 0.54\tau_{\mathrm{BH}}$ and $S_{\mathrm{max}} = S_{\mathrm{BH,0}}/2$. At first subleading order $(\ell_P/M)^2$, ED produces FORM-FORCED deviations from V5 cutoff and motif-alphabet effects, with coefficients INHERITED from substrate-microscopic details. The framework's substrate-level V5 cutoff at $\omega_c = c/\ell_P$ resolves the trans-Planckian problem of standard semiclassical Hawking. The entanglement-straddling mechanism (BH-4) provides a substrate-level account of the pair-creation picture without requiring vacuum-pair-production primitives. ED's relationship to semiclassical Hawking is that of a regulated completion with strict-extension content at observable scales and modified-theory content at extreme scales (Planck-mass remnant scenario, conditional on H-3 higher-order analysis).*

The CANDIDATE has four pieces:

- **(C7a) Leading-order equivalence.** Every standard semiclassical Hawking ingredient is reproduced at leading-order DCGT coarse-graining.
- **(C7b) First-subleading-order deviation structure.** ED produces FORM-FORCED deviations at $(\ell_P/M)^2$ from V5 cutoff and motif-alphabet effects, with coefficients INHERITED.
- **(C7c) Trans-Planckian resolution.** ED's substrate-level V5 cutoff at $\omega_c = c/\ell_P$ provides a structural resolution of the standard semiclassical Hawking trans-Planckian problem.
- **(C7d) ED's relationship to semiclassical Hawking.** Regulated completion with strict-extension at observable scales and modified-theory at extreme scales.

H-6 examines each. The argument runs through six structural steps: (i) enumeration of semiclassical Hawking ingredients, (ii) leading-order equivalence audit, (iii) first-subleading-order deviation audit, (iv) trans-Planckian resolution, (v) pair-creation-mechanism comparison, (vi) late-time qualitative deviations.

The honest framing: H-6 does not introduce new derivation content. It synthesizes the H-arc's cumulative results into a clear statement of where ED matches semiclassical, where it diverges, and what kind of theory ED is relative to the standard semiclassical framework.

---

## 2. Substrate Inputs and the Assumption Audit

The audit uses only the following inputs, all closed earlier in the arc or inherited from prior closed arcs:

| Input | Status | Role |
|---|---|---|
| **H-1 (Planck spectrum + Hawking temperature)** | Closed (this arc) | Audited at leading and first-subleading order |
| **H-2 (greybody factors)** | Closed (this arc) | Audited at leading and first-subleading order |
| **H-3 (corrected Page rate)** | Closed (this arc) | Audited at leading and first-subleading order |
| **H-4 (V5 cutoff + motif corrections)** | Closed (this arc) | First-subleading-order content audited here |
| **H-5 (information correlations + Page curve)** | Closed (this arc) | Audited at leading and first-subleading order |
| **BH-2 through BH-7** | Closed-arc inheritance (Arc BH) | Substrate-level BH architecture providing the substrate state |
| **DCGT (substrate-to-continuum bridge)** | FORCED structural-foundation | The bridge that produces leading-order identifications throughout |
| **Standard semiclassical Hawking framework** | External mathematical physics | Identification target throughout; not derivation premise |

**No new primitives introduced.** **No new substrate quantities introduced.**

---

## 3. Enumeration of Standard Semiclassical Hawking Ingredients

The standard semiclassical framework for Hawking radiation has seven structurally identifiable ingredients:

1. **Surface gravity $\kappa$.** The geometric quantity at the BH horizon controlling the radiation temperature. For Schwarzschild: $\kappa = 1/(4M)$ (geometrized units). Set by the spacetime metric.

2. **Bogoliubov coefficients.** The transformation between past- and future-frame mode operators that diagonalizes the QFT vacuum on the BH spacetime. Produces the thermal mixing of modes that observers at infinity perceive as Hawking radiation.

3. **Regge-Wheeler effective potential.** The radial-mode effective potential governing wave propagation through the curved spacetime exterior. For massless scalar on Schwarzschild: $V_\ell(r) = (1 - 2M/r)[\ell(\ell+1)/r^2 + 2M/r^3]$.

4. **Planck distribution.** The thermal occupation number per mode: $N(\omega) = 1/(e^{\omega/T_H} - 1)$, with $T_H = \kappa/(2\pi)$.

5. **Greybody factors.** The angular-channel transmission coefficients $\mathcal{T}_\ell(\omega) = |T_\ell(\omega)|^2$ obtained by solving the wave equation with the Regge-Wheeler potential. Modify the Planck distribution at observed infinity.

6. **Page evaporation rate.** Integrated emission rate produces $\dot M = -\alpha_{\mathrm{Page}}/M^2$ (massless scalar approximation; species-summed coefficient depends on emitted-particle taxonomy).

7. **Page curve.** The entanglement-entropy evolution $S_{\mathrm{rad}}(t)$ with linear rise to $S_{\mathrm{BH,0}}/2$ at $t_{\mathrm{Page}} \approx 0.54\tau_{\mathrm{BH}}$, followed by power-law fall to 0 at $\tau_{\mathrm{BH}}$.

These seven ingredients constitute the standard semiclassical Hawking framework. Each is a derived result within standard QFT-in-curved-spacetime, with the spacetime metric (Einstein equations) providing the underlying geometric structure.

---

## 4. Leading-Order Equivalence Table

For each semiclassical ingredient, the leading-order ED identification:

| Semiclassical Ingredient | ED Substrate-Level Counterpart | Leading-Order Identification | Source |
|---|---|---|---|
| Surface gravity $\kappa$ | $\kappa_{\mathrm{ED}} = \alpha\,(\nabla\sigma)\|_{\mathrm{surf}}$ | $\kappa_{\mathrm{ED}} \to \kappa$ via DCGT | H-1 §7.1 |
| Bogoliubov coefficients | V5 cross-chain correlations across saturated surface | V5 substrate-Unruh argument structurally identifies with Bogoliubov calculation | H-1 §4–§6 |
| Regge-Wheeler potential | $V_\ell^{(\mathrm{ED})}(r) = f_\sigma(r)[\ell(\ell+1)/r^2 + (1/r)(df_\sigma/dr)]$ | $f_\sigma(r) \to 1 - 2M/r$ via DCGT, recovering $V_\ell^{(\mathrm{GR})}$ | H-2 §4 |
| Planck distribution | KMS condition from V5 imaginary-time periodicity | Substrate KMS yields $1/(e^{\beta\omega} - 1)$ at $\beta = 2\pi/\kappa_{\mathrm{ED}}$ | H-1 §5–§6 |
| Greybody factors $\mathcal{T}_\ell(\omega)$ | $\mathcal{T}_\ell^{(\mathrm{ED})}(\omega) = |T_\ell^{(\mathrm{ED})}|^2$ from substrate scattering | Identifies with semiclassical $\mathcal{T}_\ell^{(\mathrm{GR})}(\omega)$ at leading order | H-2 §5–§6 |
| Page evaporation rate $\dot M = -\alpha_{\mathrm{Page}}/M^2$ | Integrated substrate emission rate via H-1 + H-2 | DCGT identification reproduces $\alpha_{\mathrm{Page}}$ exactly | H-3 §4 |
| Page curve | Bipartite-entanglement evolution via BH-4 + Arc E + BH-5 | Reproduces $t_{\mathrm{Page}} \approx 0.54\tau_{\mathrm{BH}}$, $S_{\mathrm{max}} = S_{\mathrm{BH,0}}/2$ | H-5 §4 |

**Status: Every semiclassical ingredient is reproduced exactly at leading-order DCGT coarse-graining via the substrate-to-continuum bridge.** The framework reproduces standard semiclassical Hawking in its entirety at the leading-order level.

This is the strongest structural-recovery result of the H-arc. ED is *identical* to semiclassical Hawking at observable BH scales (where $(\ell_P/M)^2$ is negligibly small).

---

## 5. First-Subleading-Order Deviations Table

For each semiclassical ingredient, the first-subleading-order ED deviation:

| Semiclassical Ingredient | ED Deviation at $(\ell_P/M)^2$ | Form Status | Coefficient Status |
|---|---|---|---|
| Surface gravity $\kappa$ | $\kappa_{\mathrm{ED}} = \kappa \cdot [1 + c_g(\ell_P/M)^2 \log g + O((\ell_P/M)^4)]$ | FORM-FORCED via H-4 §6 | $c_g$ INHERITED from BH-5 motif structure |
| Hawking temperature $T_H = \kappa/(2\pi)$ | Inherits $\kappa$ correction: $T_H^{(\mathrm{ED})} = T_H \cdot [1 + c_g(\ell_P/M)^2 \log g + ...]$ | FORM-FORCED | INHERITED |
| Planck distribution | Modulated by V5 form-factor: $N_{ED}(\omega) = N_H(\omega) / (1 + (\omega\tau_{V5})^2)$ | FORM-FORCED via H-4 §3 | $\tau_{V5} = \ell_P/c$ FORCED via T19 |
| High-frequency tail of spectrum | Cut off at $\omega \sim \omega_c = c/\ell_P = $ Planck frequency | FORM-FORCED | Cutoff scale FORCED via T19 |
| Greybody factors $\mathcal{T}_\ell(\omega)$ | $\mathcal{T}_\ell^{(\mathrm{ED})}(\omega) = \mathcal{T}_\ell^{(\mathrm{GR})}(\omega) \cdot [1 + \delta_{V5}^{\mathrm{(grey)}}(\omega) + \delta_g^{\mathrm{(grey)}}(\omega) + O((\ell_P/M)^4)]$ | FORM-FORCED via H-2 §7 | INHERITED |
| Page evaporation rate | $\dot M_{ED} = -\alpha_{\mathrm{Page}}/M^2 \cdot [1 - K(\ell_P/M)^2 + O((\ell_P/M)^4)]$ | FORM-FORCED via H-3 §7 | $K$ INHERITED |
| Page time $t_{\mathrm{Page}}$ | $t_{\mathrm{Page}}^{(\mathrm{ED})} = 0.54\tau_{\mathrm{BH}} \cdot [1 + c_t (\ell_P/M_0)^2 + O((\ell_P/M_0)^4)]$ | FORM-FORCED via H-5 §5–§6 | $c_t$ INHERITED |
| Maximum radiation entropy $S_{\mathrm{max}}$ | $S_{\mathrm{max}}^{(\mathrm{ED})} = (S_{\mathrm{BH,0}}/2) \cdot [1 + c_S (\ell_P/M_0)^2 + ...]$ | FORM-FORCED via H-5 §6 | $c_S$ INHERITED |
| Late-time evaporation profile | Possible Planck-mass remnant at $M_* \sim \ell_P$ | FORM-FORCED at structural level | CONDITIONAL on H-3 higher-order resummation |
| Late-time information-recovery completeness | Three scenarios (full / modified-turnover / remnant) | Structurally enumerated | CONDITIONAL on remnant scenario |

**Status: Every semiclassical ingredient receives a FORM-FORCED first-subleading-order correction with COEFFICIENTS INHERITED from substrate-microscopic details.** The corrections are all $\sim(\ell_P/M)^2$ at the BH scale, with the V5 cutoff additionally producing frequency-dependent corrections at $\omega \sim \omega_c$.

The corrections are invisible at stellar-mass BH scales and become order-unity in the late-stage evaporation of Planck-mass-approaching BHs.

---

## 6. The V5 Trans-Planckian Resolution

Standard semiclassical Hawking has a structural problem in its derivation called the *trans-Planckian problem*: modes observed at moderate frequencies at infinity arose from arbitrarily-blueshifted Planck-scale (and beyond) modes near the horizon. The standard derivation assumes ordinary QFT applies all the way to the Planck scale, which is structurally questionable — at and beyond the Planck scale, quantum-gravity effects should modify QFT.

### 6.1 The trans-Planckian problem in standard semiclassical

Near the horizon at $r = r_h(1 + \epsilon)$ for small $\epsilon$, modes are blueshifted by factor $\sim 1/\sqrt{\epsilon}$. For a Hawking quantum observed at infinity with frequency $\omega \sim T_H$, the proper-frame frequency near the horizon is:

```
ω_proper(r) ~ ω · (1 - 2M/r)^(-1/2)
```

For $\epsilon \to 0$ (mode tracing back to horizon), $\omega_{\mathrm{proper}} \to \infty$. The mode's "origin" in the standard derivation traces back to arbitrarily-high-frequency near-horizon physics, where standard QFT is not necessarily reliable.

This is structurally questionable. The standard answer is "QFT must apply at all scales for the Hawking calculation to be justified" — empirically supported but theoretically uncomfortable.

### 6.2 ED's substrate-level resolution

ED's V5 finite-memory kernel has characteristic time $\tau_{V5} = \ell_P/c$ (H-4 §3.4). The kernel cannot mediate coherent cross-chain correlations at frequencies $\omega \gg c/\ell_P = \omega_c$ (the Planck frequency). At and beyond $\omega_c$, V5 coherence breaks down.

For the Hawking calculation, this means: substrate modes near the horizon at proper frequencies $\omega_{\mathrm{proper}} \gtrsim \omega_c$ do not maintain V5-coherent structure. The substrate does not support arbitrarily-blueshifted modes near the horizon. The trans-Planckian problem is *resolved at the substrate level* by V5's finite memory.

### 6.3 What this delivers

The substrate provides a *natural UV cutoff* at the Planck scale. Modes that would be problematic in standard semiclassical (arbitrarily blueshifted near the horizon) are not part of the substrate's supportable mode structure. Hawking radiation in ED is *genuinely produced* by substrate modes within the V5-coherent regime; modes beyond the cutoff scale do not contribute.

This is structurally distinct from standard semiclassical's posit that "QFT applies at all scales." ED is structurally honest: substrate modes have a UV cutoff at the Planck scale, and the Hawking calculation is performed within the substrate-supported mode structure.

The substrate-level UV cutoff:
- **Resolves** the trans-Planckian problem at the structural level (no ad-hoc cutoffs needed; the substrate provides the cutoff intrinsically).
- **Predicts** observable consequences (the H-4 §5 high-frequency cutoff in the spectrum + the H-3 §7 late-stage evaporation modifications).
- **Distinguishes** ED from semiclassical in late-stage primordial-BH evaporation (where the cutoff scale becomes accessible).

**Status: V5 trans-Planckian resolution is FORCED-via-T19 (the natural substrate timescale at the gravitational scale is $\tau_{V5} = \ell_P/c$).**

This is one of the framework's most theoretically significant contributions to the Hawking-radiation literature. The trans-Planckian problem has been recognized as a structural concern in semiclassical Hawking since the 1990s; ED provides a substrate-level resolution rather than a phenomenological regulator.

---

## 7. Entanglement-Straddling vs. Pair-Creation

The standard semiclassical picture interprets Hawking radiation as *vacuum pair creation near the horizon*: virtual particle-antiparticle pairs continuously form in the QFT vacuum, normally annihilating, but near the horizon one member can be captured (falling into the BH) while the other escapes (becoming a Hawking quantum). The "negative-energy" infalling member reduces the BH mass, accounting for evaporation.

ED's substrate-level mechanism (BH-4 entanglement-straddling) is structurally distinct.

### 7.1 The pair-creation picture (standard semiclassical)

In the standard picture, the QFT vacuum near the horizon is in a particular vacuum state (Boulware, Hartle-Hawking, or Unruh, depending on the boundary conditions). Vacuum modes near the horizon couple to negative-energy modes inside via the geometry's mode-mixing. The Bogoliubov calculation yields the thermal mixing.

This picture invokes:
- A specific QFT vacuum state.
- Vacuum pair-production as a continuous process.
- Particle-antiparticle annihilation as a default behavior, suppressed near the horizon.
- The "negative-energy mode falling in" as the mass-loss mechanism.

The picture is computationally productive but structurally heavy. It requires QFT machinery and vacuum-state choices that are not always uniquely specified.

### 7.2 The entanglement-straddling picture (ED)

ED's BH-4 mechanism establishes that information crosses the horizon via V5 cross-chain correlations re-routed around the saturated decoupling surface. The substrate-level structure:

- The saturated decoupling surface is a substrate locus where $\Gamma_{\mathrm{cross}}$ falls below hydrodynamic-window resolution.
- V5 cross-chain correlations established before horizon crossing are preserved across the surface despite the cross-bandwidth suppression.
- The "outgoing Hawking quantum" is one endpoint of a V5 cross-chain correlation; the "infalling partner" is the other endpoint.
- The "pair" is a substrate entanglement-pair, not a vacuum pair-production event.

The substrate-level mechanism does not require:
- A specific QFT vacuum state choice.
- Vacuum pair-production as a continuous process.
- A particle-antiparticle annihilation default.
- Negative-energy modes (energies remain positive in substrate language; the mass-loss is bandwidth re-routing, not negative-energy absorption).

### 7.3 Are the two pictures equivalent?

At leading-order DCGT coarse-graining, both pictures predict the same observable spectrum, the same temperature, the same greybody factors, the same Page curve. They are *empirically equivalent* at observable BH scales.

Structurally, the two pictures give different accounts of "what is happening near the horizon":

- Standard semiclassical: continuous vacuum pair production with one member captured, one escaping.
- ED: substrate entanglement structure existing pre-horizon-formation, re-routed by the saturated surface, with cross-correlated endpoints appearing as "in" and "out" modes.

The ED picture is structurally more economical (no vacuum-pair-production primitives needed; entanglement structure is already a substrate feature). The standard picture is computationally productive (the QFT machinery is well-developed). Both are correct as accounts of the same observable phenomenon at leading order.

### 7.4 Status

**The pair-creation vs. entanglement-straddling distinction is one of substrate ontology, not of empirical prediction.** At leading order, the two pictures are observationally indistinguishable. At first subleading order, the substrate-level account (ED) produces specific predictions (V5 cutoff, motif corrections, possible remnant) that the standard pair-creation picture does not naturally produce; the standard picture, supplemented with phenomenological substrate-cutoff regulators, can in principle reproduce ED's first-subleading content.

ED's contribution: provides the substrate-level structural account that the standard semiclassical picture has historically lacked, eliminating the need for vacuum-state choices and pair-production primitives.

---

## 8. Late-Time Qualitative Deviations

The H-arc identifies one qualitative deviation from standard semiclassical Hawking: the late-time evaporation profile in the limit $M \to M_P$.

### 8.1 Standard semiclassical late-time

Standard semiclassical Hawking with $\dot M = -\alpha_{\mathrm{Page}}/M^2$ predicts $M(t) = (M_0^3 - 3\alpha_{\mathrm{Page}} t)^{1/3}$ with full evaporation at $t = \tau_{\mathrm{BH}} = M_0^3/(3\alpha_{\mathrm{Page}})$. As $M \to 0$, the Hawking temperature $T_H \to \infty$ and emission rate diverges. The BH "explodes" in a final burst.

The Page curve correspondingly returns to zero at $\tau_{\mathrm{BH}}$, indicating full information recovery through correlations between Hawking quanta.

### 8.2 ED late-time scenarios

H-3 §7 and H-5 §7 identified three possible scenarios:

**Scenario A (Full Recovery, no remnant):** Higher-order corrections to $\dot M$ vanish at $M \sim M_*$, allowing full evaporation. Page curve returns to zero. Information fully recovered.

**Scenario B (Modified Turnover, no remnant):** Higher-order corrections slow but do not halt evaporation. BH evaporates fully on a timescale longer than $\tau_{\mathrm{BH}}^{(\mathrm{leading})}$. Page curve returns to zero on the longer timescale. Information fully recovered.

**Scenario C (Remnant Storage, stable Planck-mass remnant):** Higher-order corrections produce a stable endpoint at $M_* \sim M_P$. Evaporation stops. $S_{\mathrm{remnant}} \sim O(\log g)$ bits stored. Page curve does not return to zero — asymptotes at $S_{\mathrm{BH,0}} - S_{\mathrm{remnant}}$.

### 8.3 Qualitative-deviation status

**Scenario A:** Quantitatively distinct from standard semiclassical (corrections at $(\ell_P/M)^2$) but qualitatively identical (both predict full evaporation and full information recovery).

**Scenario B:** Quantitatively distinct (longer evaporation timescale) but qualitatively identical (both predict full evaporation and full information recovery, just on different timescales).

**Scenario C:** **Qualitatively distinct** from standard semiclassical (predicts a stable remnant; standard predicts full evaporation). Information not fully recovered at the radiation level. Cosmologically significant (primordial-BH-remnant DM scenario).

The framework's late-time prediction is **conditional on which scenario realizes**. The leading-correction analysis cannot determine this; it requires substrate-microscopic analysis or empirical evidence.

### 8.4 What this means structurally

ED is **quantitatively distinct from standard semiclassical** at first-subleading-order across the entire spectrum and Page-curve evolution. ED is **qualitatively distinct only in Scenario C**, where the stable remnant produces structurally new content not present in standard semiclassical.

The framework's most cosmologically significant prediction (remnant DM) requires Scenario C; this prediction is *conditional* on higher-order analysis. If higher-order analysis settles Scenario A or B, ED is a regulated completion + small-deviation strict-extension. If it settles Scenario C, ED is a regulated completion + qualitative-deviation modified-theory.

---

## 9. Verdict: ED's Relationship to Semiclassical Hawking

> **VERDICT (H6): Regulated Completion (with strict-extension content at observable scales and possible modified-theory content at extreme scales).**
>
> ED reproduces every standard semiclassical Hawking ingredient exactly at leading-order DCGT coarse-graining (§4 table). ED produces FORM-FORCED first-subleading-order corrections at $(\ell_P/M)^2$ from V5 cutoff and motif-alphabet effects (§5 table). ED's substrate-level V5 cutoff at $\omega_c = c/\ell_P$ provides a natural UV cutoff resolving the trans-Planckian problem of standard semiclassical Hawking (§6). ED's entanglement-straddling mechanism (BH-4) provides a substrate-level account that is empirically equivalent to the standard pair-creation picture at leading order, structurally distinct, and structurally more economical (§7). Late-time qualitative deviations from standard semiclassical depend on Scenario C realization (§8) — conditional on higher-order resummation of $(\ell_P/M)^2$ corrections.

### 9.1 Structural classification of ED relative to semiclassical Hawking

**Strict extension** (semiclassical is a special limit of ED): ED reproduces semiclassical exactly at leading order; corrections at higher orders do not contradict semiclassical. **Yes, in the leading-order sense.** At observable BH scales, ED is empirically equivalent to semiclassical.

**Regulated completion** (ED provides UV-completion resolving structural problems of semiclassical): ED's V5 cutoff resolves the trans-Planckian problem at the substrate level. **Yes, in the structural sense.** ED is a substrate-level UV-completion of semiclassical Hawking that does not require ad-hoc regulators.

**Modified theory** (ED produces qualitatively distinct predictions): At observable scales (stellar-mass BHs), no. At extreme scales (Planck-mass BHs in late-stage evaporation), Scenario-C-conditional. **Conditionally yes** at extreme scales if higher-order analysis settles Scenario C.

The honest summary: **ED is a regulated completion of semiclassical Hawking that includes all of semiclassical at leading order plus FORM-FORCED first-subleading corrections + a substrate-level UV cutoff + a conditional remnant-DM scenario at extreme scales.**

### 9.2 Verdict-class details

- **(C7a) Leading-order equivalence:** FORCED via DCGT, applies to every semiclassical ingredient.
- **(C7b) First-subleading deviations:** FORM-FORCED, COEFFICIENTS-INHERITED.
- **(C7c) Trans-Planckian resolution:** FORCED via T19 + V5 substrate primitive.
- **(C7d) ED's relationship:** regulated completion at structural level; strict extension at observable scales; modified theory at extreme scales conditional on Scenario C.
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {} as of arc-opening tally.

---

## 10. Circularity Audit

| Potential circularity | Audit verdict |
|---|---|
| H-1 through H-5 used as derivation premises? | **Yes — as inputs only.** Each closed earlier in the arc; H-6 audits/synthesizes their cumulative results. Inheritance, not circularity. |
| Standard semiclassical Hawking used as derivation premise? | **No.** Standard semiclassical appears throughout as identification target via DCGT (leading-order matching) and as comparison baseline (first-subleading-order deviations, late-time scenarios). Never as derivation premise. |
| Self-reference of H-6 within itself? | **No.** §3 → §4 → §5 → §6 → §7 → §8 derivation chain is acyclic. |
| H-7 used as derivation premise? | **No.** Not invoked. H-6 is structurally upstream of H-7 (synthesis). |

**Acyclicity confirmed.**

---

## 11. Falsification

### 11.1 Falsifier for Regulated Completion verdict

A substrate construction or empirical observation that:

- (a) Demonstrates leading-order *non-equivalence* between ED and standard semiclassical Hawking — would refute the §4 leading-order equivalence table and DCGT's substrate-to-continuum bridge.
- (b) Demonstrates that the first-subleading-order corrections do not scale as $(\ell_P/M)^2$ — would refute V5 + motif scaling structure inherited from H-4.
- (c) Demonstrates that the trans-Planckian problem is *not* resolved by V5 substrate-cutoff at $\omega_c = c/\ell_P$ — would refute the §6 trans-Planckian resolution.

Each refutation would downgrade the verdict.

### 11.2 Empirical-side falsifier — analog Hawking experiments

Precision analog Hawking measurements simultaneously testing:

- Spectral form (matches Planck distribution at leading order — confirmation of §4).
- Greybody factors (match Regge-Wheeler at leading order — confirmation of §4).
- High-frequency cutoff at $\omega \sim 1/\tau_{\mathrm{analog}}$ (V5-form modulation — confirmation of §5).

If all three match the framework's prediction: confirmation of the regulated-completion verdict.
If any deviates from the framework's prediction: refutation of one or more of H-1, H-2, H-4 inheritance.

### 11.3 Empirical-side falsifier — primordial BH late-stage observation

PBH detection with sufficient temporal and spectral resolution to track late-stage evaporation:

- If the evaporation profile matches Scenario A or B (full evaporation in finite time): confirms regulated completion + strict extension at observable-scale + dimension and refutes Scenario C.
- If the evaporation profile shows a stable remnant: confirms Scenario C + modified-theory content at extreme scales.

No PBH evaporations have been detected to date.

### 11.4 Empirical-side falsifier — DM remnant searches

If continued absence of Planck-mass DM detection at improving experimental sensitivity continues to constrain the remnant scenario, this would refute Scenario C and force the regulated-completion verdict to either Scenario A or Scenario B.

---

## 12. Consequences for the Arc

1. **H-6 closes as audit memo.** Synthesizes H-1 through H-5 into a clear statement of ED's relationship to semiclassical Hawking. Arc Hawking can now proceed to H-7 (final synthesis).

2. **Regulated-completion verdict is the framework's principal claim.** ED is not a *replacement* for semiclassical Hawking; it is a *substrate-level completion*. This has implications for how the framework presents itself relative to the standard literature: ED is upstream-providing, regulating, and extending — not contradicting.

3. **Leading-order match is comprehensive and clean.** Every semiclassical ingredient is reproduced exactly. The framework has no leading-order disagreement with the empirically validated standard semiclassical Hawking results.

4. **First-subleading deviations are well-classified.** The §5 table provides a clean catalog of where ED differs from semiclassical at the $(\ell_P/M)^2$ level. Each deviation has FORM-FORCED structural form and INHERITED specific values.

5. **Trans-Planckian resolution is structurally clean.** ED's V5 substrate-cutoff at $\omega_c = c/\ell_P$ naturally resolves a structural problem that has been recognized in semiclassical Hawking since the 1990s. This is one of the framework's most theoretically significant contributions.

6. **Pair-creation vs. entanglement-straddling distinction is ontological.** Both pictures are empirically equivalent at leading order; ED's entanglement-straddling mechanism is structurally more economical. This is a structural improvement, not an empirical deviation.

7. **Late-time qualitative-deviation prediction is conditional.** Scenario C (Planck-mass remnant) would constitute a modified-theory deviation but requires higher-order analysis to settle. The most cosmologically significant prediction sits structurally available but empirically pending.

8. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

---

## 13. Summary

**What this memo accomplished.**

- Stated the H-6 CANDIDATE (§1) decomposing it into (C7a) leading-order equivalence, (C7b) first-subleading deviations, (C7c) trans-Planckian resolution, (C7d) ED's relationship to semiclassical.
- Enumerated the seven semiclassical Hawking ingredients (§3).
- Constructed the leading-order equivalence table (§4): every semiclassical ingredient reproduced exactly via DCGT.
- Constructed the first-subleading-order deviations table (§5): every semiclassical ingredient receives a FORM-FORCED $(\ell_P/M)^2$ correction with COEFFICIENTS INHERITED.
- Articulated ED's substrate-level resolution of the trans-Planckian problem via V5 cutoff at $\omega_c = c/\ell_P$ (§6).
- Compared ED's entanglement-straddling mechanism with the standard pair-creation picture: empirically equivalent at leading order, structurally distinct, structurally more economical (§7).
- Articulated the three late-time scenarios and the qualitative-deviation status of Scenario C (§8).
- Issued the verdict: **Regulated completion of semiclassical Hawking, with strict-extension content at observable scales and possible modified-theory content at extreme scales** (§9).
- Confirmed acyclicity (§10) and provided substrate-level + empirical falsifiers (§11).

**Trending toward YES on the regulated-completion verdict.**

**Brief 2–3 sentence summary:** ED reproduces every standard semiclassical Hawking ingredient exactly at leading-order DCGT coarse-graining (Bogoliubov ↔ V5, Regge-Wheeler ↔ $V_\ell^{(\mathrm{ED})}$, Planck factor ↔ KMS-from-V5, greybody factors ↔ substrate-scattering, Page rate ↔ integrated emission, Page curve ↔ bipartite-entanglement evolution), with FORM-FORCED first-subleading-order corrections at $(\ell_P/M)^2$ from V5 cutoff and motif-alphabet effects. The substrate-level V5 cutoff at $\omega_c = c/\ell_P$ provides a natural UV resolution of the standard semiclassical trans-Planckian problem, and the entanglement-straddling mechanism (BH-4) gives a structurally more economical account than the standard vacuum-pair-creation picture. ED's structural relationship to semiclassical Hawking is **regulated completion** — strict extension at observable scales, modified theory at extreme scales (conditional on Scenario C remnant) — rather than replacement; the framework includes all of semiclassical at leading order while resolving structural problems and adding substrate-derived first-subleading-order content.

---

## 14. Recommended Next Steps

Multiple options, in decreasing order of immediate Arc Hawking productivity:

1. **H-7 (synthesis) — RECOMMENDED.** Final memo of Arc Hawking. Integrates H-1 through H-6 into the cross-domain unification framework. V5 kernel doing soft-matter Maxwell viscoelasticity (Arc D), Hawking high-frequency cutoff (H-4), Hawking entanglement-bandwidth modulation (H-5), and Hawking late-stage regulation (H-3 + H-5 + H-6). Bandwidth-budget mechanism unifying BH-4 + Arc E + Q-COMPUTE + H-5. Completes Arc Hawking with a structural statement of cross-domain echoes. Estimated 1–2 sessions.

2. **(Independent) Higher-order resummation memo.** Resolves Scenario A/B/C late-time question. The most cosmologically significant deferred work in the arc. Required to settle the conditional remnant-DM prediction. Estimated 2–4 sessions.

3. **(Independent) Substrate-information-paradox-resolution paper.** §7 of H-5 + §6 of this memo (trans-Planckian resolution) + §7 of this memo (entanglement-straddling vs. pair-creation) jointly articulate the framework's substrate-mechanism resolution of the BH information paradox. A standalone publication-grade paper comparing ED's resolution to firewall, ER=EPR, soft-hair, and other proposals. Estimated 4–6 sessions.

4. **(Independent) Trans-Planckian resolution short paper.** §6 of this memo articulates the framework's V5-substrate-cutoff resolution of the trans-Planckian problem. A short standalone paper on this single point — historically significant in the Hawking literature — could position the framework for engagement with theoretical cosmology / quantum-gravity audiences. Estimated 2 sessions.

5. **(Independent) Walkthrough on Hawking Spectrum from Substrate.** With H-1 through H-6 closed, a public-facing walkthrough in the `walkthroughs/` series could derive Hawking radiation from substrate primitives at the level matched to the existing series (Born, Schrödinger, Bell-Tsirelson, etc.). Title candidate: `from_primitives_to_hawking_radiation.md`. Estimated 1–2 sessions.

6. **(Independent) Cross-arc analysis: V5 kernel doing three jobs.** H-7 will synthesize this; an independent extended analysis could become a separate cross-domain-mechanism-overview paper. The V5 kernel's role in soft-matter Maxwell viscoelasticity + Hawking spectrum + BH information transfer is a striking cross-domain unification. Estimated 2–3 sessions.

---

**Pause for further instruction.**
