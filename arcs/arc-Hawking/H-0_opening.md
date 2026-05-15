# Arc Hawking — Memo 0: Opening, Scope, and Load-Bearing Decomposition

**Status:** Opening memo of Arc Hawking (Hawking spectrum from V5 cross-chain correlations). Architect-mode active. Form-FORCED / value-INHERITED methodology. No new primitives. Identification-not-derivation discipline for cross-links to closed arcs. Promoted to "next natural arc following Arc BH closure" 2026-05-01 per Investigation Priority List item 19.

**Date:** 2026-05-09

---

## 1. Structural Summary

The arc's load-bearing question, in ED's own language:

> *Of the spectrum of radiation that semiclassical gravity (Hawking 1975) predicts to emerge from a black-hole horizon, which features are FORCED by ED's substrate primitives plus Arc BH's saturated-decoupling-surface mechanism, which are CONDITIONAL on auxiliary assumptions, and which are merely inherited mathematical structure once the substrate calculation is performed?*

Standard semiclassical gravity says: a black-hole horizon emits a thermal spectrum at temperature $T_H = \kappa/(2\pi) = \hbar c^3/(8\pi G M k_B)$, where $\kappa$ is the surface gravity. Planck distribution for each mode, with greybody factors from spacetime-curvature backscattering. The derivation runs through Bogoliubov transformations between past and future modes of a quantum field on the curved spacetime, with the result that vacuum modes that look empty in one frame look thermal in the other.

This is mathematically clean and has produced one of the most striking predictions in theoretical physics. It has not been directly observed — stellar-mass black holes have temperatures of order $10^{-7}$ K, far below the cosmic microwave background, and primordial black holes light enough to be evaporating now have not been detected. Analog Hawking radiation in BEC and acoustic systems has been observed and matches the spectral form. The Hawking calculation is theoretically central but empirically unanchored at the gravitational scale.

Arc BH (closed 2026-05-01) established the substrate-level mechanism for what happens at a black-hole horizon: the horizon is a saturated decoupling surface where cross-chain bandwidth $\Gamma_{\mathrm{cross}}$ falls below hydrodynamic-window resolution. Information is blocked. Entanglement straddles. Evaporation is participation re-routing. The substrate-mechanism account is in hand.

What Arc BH did *not* do is compute the explicit V5 cross-chain correlation calculation that would produce the Hawking spectrum from substrate primitives. BH-4 noted the asymmetric participation flow at the saturated decoupling surface as the substrate mechanism for evaporation; it did not derive the spectrum the asymmetric flow produces. That calculation is the load-bearing work of Arc Hawking.

The central load-bearing question:

> **H1.** Does the V5 cross-chain correlation calculation at a saturated decoupling surface produce a thermal spectrum at temperature $T_H = \kappa/(2\pi)$, structurally recovering Hawking, or does it produce a deviation?

H1 is the gate condition. If the V5 calculation produces $T = \kappa/(2\pi)$ exactly, the framework structurally recovers Hawking, adds another sector to the closed-arc inventory, and produces a substrate-level account of why BH horizons radiate at the Hawking temperature. If the calculation produces a deviation, the deviation is a substrate-derived prediction that distinguishes ED from semiclassical gravity — a falsifiable result against analog Hawking experiments and any future direct detections. If the calculation cannot be performed in closed form, the form-FORCED / value-INHERITED structure still produces a useful structural statement.

This memo:

- States the current CANDIDATE formulation of the Hawking-spectrum prediction in ED.
- Inventories what is already FORCED-unconditional from prior closed arcs.
- Identifies the seven load-bearing-open items (H1–H7) with primitive-level loadings, FORCED/CONDITIONAL/NOT-FORCED criteria, and substrate-level falsifiers.
- Proposes the memo structure H-1 through H-7 with the same discipline used in Arc E.
- Produces the inheritance map showing how Arc Hawking depends on Arc BH, T18, V5 kernel, DCGT, and standard QFT-in-curved-spacetime as identification target.

The arc proceeds: H1 first (gate), then H2–H6 in any order once H1 closes, then H7 (synthesis). The synthesis memo is not written before the load-bearing items close.

---

## 2. Current CANDIDATE Status

### 2.1 As it appears in BH-4

BH-4 (Information_And_Evaporation) establishes evaporation as participation re-routing at the saturated decoupling surface. The mechanism: at a saturated horizon, cross-bandwidth $\Gamma_{\mathrm{cross}}$ has fallen below hydrodynamic-window resolution from the inside-to-outside direction, but the substrate's participation cannot accumulate indefinitely at the surface. Asymmetric participation flow re-routes participation around the saturated surface, producing the empirical signature that standard physics calls Hawking radiation.

What BH-4 *does not* state mathematically:

- The functional form of the radiation's spectrum.
- The specific temperature parameter governing the spectrum.
- The substrate-level mechanism by which the asymmetric flow produces a *thermal* (Planck-distribution) form rather than some other spectral shape.

BH-4 is consistent with thermal Hawking radiation but does not force it. **The thermal Hawking spectrum is currently CANDIDATE in Arc Hawking's ledger** — neither FORCED nor refuted at the substrate level.

### 2.2 The CANDIDATE statement

> **CANDIDATE (Arc Hawking).** *At a saturated decoupling surface (a black-hole horizon in the substrate ontology), the V5 cross-chain correlations across the surface produce an emission spectrum that is thermal in form, with the spectral temperature equal to $T_H = \kappa/(2\pi)$ where $\kappa$ is the surface gravity of the horizon. Greybody factors from substrate-channel-coupling effects modify the spectrum at substrate-channel-specific frequencies. The total emission rate produces backreaction consistent with the BH-4 evaporation mechanism, and the spectrum's high-frequency cutoff inherits from the substrate's V5 kernel width.*

The CANDIDATE has six pieces, derived in order:

- **(C1) Spectral form.** The emission spectrum is thermal (Planck distribution) for each substrate mode.
- **(C2) Temperature value.** The thermal temperature is $T_H = \kappa/(2\pi)$, matching Hawking's semiclassical result.
- **(C3) Greybody factors.** Substrate-level analogs of the spacetime-curvature backscattering greybody factors are produced by substrate-channel-coupling effects.
- **(C4) Total emission rate.** The integrated emission rate produces backreaction on the BH mass consistent with $\dot M = -\hbar c^4 / (15360 \pi G^2 M^2)$ (Page evaporation rate).
- **(C5) High-frequency cutoff.** The spectrum's high-frequency behavior departs from the strict Planck distribution at frequencies near the V5 kernel width's inverse, with the departure form FORCED by V5's specific kernel structure.
- **(C6) Information-content structure.** The spectrum contains correlations between Hawking-radiated quanta and interior-fallen matter consistent with BH-4's entanglement-straddling, with the substrate-level account being that the V5 cross-chain correlations encode the same information that the standard Bogoliubov picture distributes between past and future modes.

H1 (the load-bearing gate question) closes (C1) and (C2). H2–H6 close (C3) through (C6). H7 synthesizes.

---

## 3. Inventory: What Is Already FORCED-Unconditional

The following items are inputs to Arc Hawking, not deliverables. They will not be re-derived; they are identified by source.

| Item | Source | What Arc Hawking Inherits |
|---|---|---|
| **Horizon as saturated decoupling surface** | BH-2 | Substrate-level identification of where the calculation happens |
| **Entanglement-straddling at horizon** | BH-4 | Substrate-level information architecture for what Hawking quanta carry |
| **Evaporation as participation re-routing** | BH-4 | Substrate-level mechanism for the existence of the radiation |
| **Area-law entropy form** | BH-5 | Substrate-counting → Shannon → von Neumann pipeline applicable to horizon entropy |
| **V1 forward-cone-only kernel** | T18 | Cross-chain correlations propagate forward only; no acausal backflow |
| **V5 finite-width memory kernel** | Substrate primitive | The cross-chain memory kernel that produces Maxwell viscoelastic memory in soft matter via DCGT, and that does the substrate work for Hawking spectrum here |
| **DCGT** | Arc D | Substrate-to-continuum bridge; coarse-graining of V5 produces continuum-level correlation functions |
| **Cross-chain bandwidth $\Gamma_{\mathrm{cross}}$** | DCGT, BH-2, Q-COMPUTE | Substrate cross-region coupling; falls below hydrodynamic resolution at saturated surfaces |
| **Sparsity $\sigma$, multiplicity $\mathcal{M}$, unresolvedness $\mathcal{U}$** | Q-COMPUTE Memo 1, BH-2 | Substrate-state quantities operating at the horizon |
| **T19 (Newton-recovery $\ell_P$)** | Arc SG | Identifies the substrate length scale; load-bears for the high-frequency cutoff |
| **Standard QFT in curved spacetime** | External mathematical physics | Identification target — the Bogoliubov transformation calculation that produces $T_H = \kappa/(2\pi)$ in semiclassical gravity. ED's substrate calculation is identified with this calculation, not derived from it. |

These eleven anchors are *taken as given*. The arc neither rederives them nor relaxes them.

---

## 4. Load-Bearing Open Questions: H1 Through H7

For each item: (a) the question, (b) which primitives load-bear, (c) FORCED / CONDITIONAL / NOT-FORCED criteria, (d) substrate-level falsifier.

### H1 — Spectral form and temperature

(a) **Question.** Does the V5 cross-chain correlation calculation at a saturated decoupling surface produce a thermal (Planck-distribution) spectrum at temperature $T_H = \kappa/(2\pi)$?

(b) **Loads on:** V5 kernel structure, BH-2 saturated surface, BH-4 asymmetric participation flow, T18 forward-cone-only correlations, DCGT substrate-to-continuum bridge.

(c) **Criteria.**
- **FORCED:** the V5 cross-chain correlation calculation produces a thermal spectrum at exactly $T_H = \kappa/(2\pi)$ without auxiliary assumptions, structurally recovering Hawking.
- **CONDITIONAL:** the calculation produces a thermal spectrum only after an auxiliary assumption (e.g., a specific functional form for V5 not derivable from primitives, or an approximation step that introduces a small parameter not naturally available).
- **NOT FORCED:** the calculation produces a non-thermal spectrum, contradicting Hawking but providing an empirically distinguishable substrate-level prediction.

(d) **Falsifier.** A substrate calculation satisfying all of V5 + BH-2 + BH-4 + T18 + DCGT but producing a non-thermal spectrum or a temperature deviating from $\kappa/(2\pi)$ would refute FORCED status. Empirical falsifier: analog Hawking radiation experiments (BEC, acoustic, photonic) producing a spectrum that matches ED's prediction in the regime where ED predicts deviation from semiclassical Hawking.

### H2 — Greybody factors

(a) **Question.** Are the greybody factors that modify the strict Planck distribution at frequencies where spacetime-curvature backscattering is significant produced by substrate-channel-coupling effects, and what is the substrate-level form of those factors?

(b) **Loads on:** H1 closure; substrate-channel-coupling structure; T17 (gauge-field-as-rule-type) for charged-particle Hawking emission; V5 kernel.

(c) **Criteria.**
- **FORCED:** substrate-channel-coupling effects produce the standard greybody factor structure $\Gamma_l(\omega)$ as a multiplicative modifier of the Planck distribution.
- **CONDITIONAL:** form FORCED but specific coefficients INHERITED.
- **NOT FORCED:** substrate produces no greybody-factor analog, contradicting standard physics.

(d) **Falsifier.** A substrate calculation that fails to produce frequency-dependent modification of the Planck distribution.

### H3 — Total emission rate and Page evaporation

(a) **Question.** Does the integrated substrate-level emission rate produce backreaction on the BH mass consistent with the standard Page evaporation rate $\dot M = -\hbar c^4/(15360 \pi G^2 M^2)$?

(b) **Loads on:** H1 + H2; BH mass-area relationship from BH-5; substrate-level energy-momentum balance.

(c) **Criteria.**
- **FORCED:** integration over the substrate-level spectrum produces the Page rate exactly.
- **COEFFICIENT-INHERITED:** functional dependence on $M$ FORCED but specific numerical coefficient inherited.
- **NOT FORCED:** rate departs from Page rate at order-unity factors.

(d) **Falsifier.** Empirical: black-hole evaporation rate measurements (none currently exist for gravitational BHs; analog systems may provide constraints).

### H4 — High-frequency cutoff from V5 kernel width

(a) **Question.** Does the spectrum's high-frequency behavior depart from the strict Planck distribution at frequencies near the V5 kernel-width inverse, and what is the form of the departure?

(b) **Loads on:** V5 kernel-width parameters; T19 ($\ell_P$ as substrate length); H1 closure.

(c) **Criteria.**
- **FORM-FORCED:** specific functional form of high-frequency cutoff produced by the V5 kernel structure.
- **FORM-FORCED + value-INHERITED:** form FORCED, kernel-width parameters INHERITED.
- **NOT FORCED:** no high-frequency cutoff produced — substrate calculation gives strict Planck distribution at all frequencies.

(d) **Falsifier.** This is structurally informative independent of empirical access. ED predicts a specific high-frequency cutoff that semiclassical Hawking does not — the cutoff is a substrate-level prediction that distinguishes ED from QFT-in-curved-spacetime if it can be measured (e.g., via primordial black holes evaporating in their final stages, or via analog systems).

### H5 — Information-content structure and Hawking-quanta correlations

(a) **Question.** Does the substrate spectrum contain correlations between Hawking-radiated quanta and interior-fallen matter consistent with BH-4's entanglement-straddling, and how do these correlations evolve as the BH evaporates?

(b) **Loads on:** BH-4 entanglement-straddling; H1 closure; the cross-domain echo with Arc E (entanglement) bandwidth-budget mechanism.

(c) **Criteria.**
- **FORCED:** correlations FORCED with structural form matching the standard information-paradox-resolution candidates (Page curve, information-recovery at half-evaporation).
- **CONDITIONAL:** correlations form FORCED but specific dynamics CONDITIONAL on auxiliary substrate-bandwidth-budget evolution.
- **NOT FORCED:** correlations either absent or in the wrong functional form.

(d) **Falsifier.** Standard information-paradox arguments — if the substrate produces a thermal spectrum that is *exactly* uncorrelated with interior-fallen matter, the information paradox is in ED unsolved. If it produces correlations matching the Page-curve structure, ED has a substrate-level account of the resolution. The structural-positive verdict here would be a notable cross-domain unification (Arc E entanglement bandwidth-budget + Arc Hawking spectrum).

### H6 — Substrate vs. semiclassical equivalence of derivation

(a) **Question.** What is the relationship between the V5 cross-chain correlation calculation and the standard Bogoliubov-transformation derivation of Hawking radiation? Are they identifications (substrate provides the substrate-mechanism that the Bogoliubov calculation mathematically expresses) or genuine departures (substrate produces a different spectrum)?

(b) **Loads on:** H1 + H2 + H4 closure; comparison with QFT-in-curved-spacetime mathematics.

(c) **Criteria.**
- **IDENTIFICATION:** substrate calculation is mathematically equivalent to the Bogoliubov calculation in the leading-order substrate-to-continuum coarse-graining, with the substrate calculation providing the substrate-physical justification for the formal QFT manipulations.
- **DEPARTURE:** substrate calculation produces predictions distinguishable from semiclassical Hawking at substrate-cutoff scales.
- **MIXED:** leading-order identification with first-subleading-order departure (analogous to how DCGT gives standard physics at leading order plus substrate-cutoff corrections at $(\ell_P/R_{cg})^2$).

(d) **Falsifier.** Identification can be checked by direct computation; departure can be checked by substrate-level prediction extraction. The mixed verdict is the most likely outcome based on the framework's other arcs (NS, YM, Q-COMPUTE all produce mixed verdicts of this kind).

### H7 — Cross-domain synthesis

(a) **Question.** Do the closures of H1–H6 produce cross-domain echoes with closed arcs — specifically, with Arc D (V5 → Maxwell viscoelastic memory at substrate-to-continuum), Arc BH (entanglement-straddling), Arc E (entanglement bandwidth-budget), and the framework's broader bandwidth-budget mechanism?

(b) **Loads on:** all of H1–H6; Arc D; Arc BH; Arc E; Q-COMPUTE.

(c) **Criteria.**
- **STRUCTURAL ECHO ESTABLISHED** if explicit identities (or close structural correspondences) hold between the V5-mediated Hawking calculation here and the V5-mediated Maxwell memory calculation in soft matter. Same kernel; two different physical applications.
- **STRUCTURAL ECHO ABSENT** is a valid honest outcome.

(d) **Falsifier.** N/A — synthesis content is non-falsifiable by design; what is falsifiable lives in H1–H6.

---

## 5. Memo Structure

| Memo | Title | Status / Disposition |
|---|---|---|
| **H-0** | This opening memo | **Drafted** (this file) |
| **H-1** | Spectral form and temperature from V5 cross-chain correlations | Gate; must close before H-2 onward |
| **H-2** | Greybody factors from substrate-channel-coupling effects | Articulation memo, conditional on H-1 |
| **H-3** | Total emission rate and Page evaporation backreaction | Substantive derivation, depends on H-1 + H-2 |
| **H-4** | High-frequency cutoff from V5 kernel width | Substantive derivation; structural prediction |
| **H-5** | Information-content structure and Hawking-quanta correlations | Substantive derivation, depends on H-1 + BH-4 + Arc E inheritance |
| **H-6** | Substrate vs. semiclassical equivalence of derivation | Identification memo, depends on H-1 + H-2 + H-4 |
| **H-7** | Synthesis: cross-domain echoes with Arc D / Arc BH / Arc E | Synthesis memo, written last |

**Discipline.**

- **No new primitives.** Arc Hawking will not introduce any substrate-level CANDIDATE that is not already on the active inventory (currently {} as of 2026-05-08 closure tally, after Arc E closure).
- **Form-FORCED / value-INHERITED separation** explicit in every memo's verdict section.
- **Identification-not-derivation discipline** for the QFT-in-curved-spacetime cross-link: standard Hawking calculation is identified as the structural target downstream of H-1, never used as a derivation premise inside H-1.
- **Acyclicity discipline** as in Arc E: each memo opens with a circularity audit confirming it does not depend on any later-numbered memo's content.

---

## 6. Inheritance Map

```
                    QFT in curved spacetime (identification target only)
                                       ▲
                                       │ [identification, not derivation]
                                       │
         BH-2 ───────────────► Arc Hawking ◄──────────── BH-4
       (saturated                  │   │             (entanglement-
        decoupling                 │   │              straddling +
        surface)                   │   │              participation
                                   │   │              re-routing)
                                   │   ▼
              V5 kernel ──────────►H-1 (gate: spectrum form + temperature)
                                   │
                                   ├────────────────► H-2 (greybody)
                                   │
                                   ├────────────────► H-3 (Page rate)
                                   │
              T19 (ℓ_P) ──────────►H-4 (V5 cutoff)
                                   │
              Arc E (entanglement)─►H-5 (information)
                                   │
                                   └────────────────► H-6 (semiclassical
                                                            equivalence)
                                                            │
                                                            ▼
              Arc D (DCGT, V5→Maxwell) ────────────► H-7 (synthesis)
              BH-4 (entanglement-straddling) ──────►
              Arc E (E-4 bandwidth-budget) ────────►
              Q-COMPUTE Γ_cross ────────────────────►
```

**Arc Hawking is downstream of:** BH-2 (saturated horizon), BH-4 (entanglement-straddling + participation re-routing), BH-5 (area-law entropy form), V5 kernel, T18 (forward-cone V1 — establishes causal structure for cross-chain correlations), DCGT (substrate-to-continuum bridge), T19 (substrate length $\ell_P$), Arc E (entanglement structure), Q-COMPUTE ($\Gamma_{\mathrm{cross}}$).

**Arc Hawking is upstream of:** future arcs that would extend Hawking-spectrum results to charged BHs (Reissner-Nordström analogs), rotating BHs (Kerr — couples with O1 superradiance amplitude), and primordial-BH cosmology.

**Cross-domain echo target (E-7-style):** V5 kernel produces Maxwell viscoelastic memory in soft matter (Arc D, DCGT consequence) AND Hawking spectrum at BH horizons (this arc). Same kernel, two physical applications. If H-7 establishes this structural echo, it is a notable unification of soft-matter rheology and BH thermodynamics through shared V5 kernel infrastructure.

---

## 7. Verdict-Class Projection

Anticipated verdict structure when Arc Hawking closes (based on inheritance map and analogous arc patterns):

- **H1: FORM-FORCED, VALUE-DEPENDS-ON-CALCULATION.** The thermal spectral form is expected to be FORCED by V5 cross-chain correlation structure plus saturated-horizon substrate state. The specific temperature value ($T_H = \kappa/(2\pi)$ vs. some deviation) depends on the explicit calculation. The most likely outcome is identification — substrate produces $T = \kappa/(2\pi)$ exactly via the Bogoliubov-equivalent calculation — based on the framework's general pattern of structurally recovering standard physics in regimes where standard physics has been validated.
- **H2: FORM-FORCED, COEFFICIENT-INHERITED.** Greybody-factor form FORCED by substrate-channel-coupling structure; specific coefficients INHERITED from substrate-mode statistics.
- **H3: FORM-FORCED, COEFFICIENT-INHERITED.** Page evaporation rate functional form $\dot M \propto 1/M^2$ FORCED; specific numerical coefficient (15360 π) INHERITED.
- **H4: FORM-FORCED.** High-frequency V5 cutoff — this is *new* substrate content beyond standard Hawking. The form should be FORCED by V5's kernel structure; the substrate calculation should produce a specific functional form for the cutoff.
- **H5: FORM-FORCED.** Hawking-quanta correlations consistent with BH-4 entanglement-straddling FORCED. Specific evolution dynamics potentially CONDITIONAL.
- **H6: MIXED.** Leading-order identification with semiclassical Hawking, plus first-subleading-order departures at substrate-cutoff scales. Parallel to NS-Smoothness / Yang-Mills / Arc ED-10 pattern.
- **H7: SYNTHESIS** — non-falsifiable; structural-positive expected.

The arc's **load-bearing risk** is concentrated at H1. Every other memo's verdict is contingent on H1, but H1's verdict is contingent on whether the V5 cross-chain correlation calculation produces a thermal spectrum at $T = \kappa/(2\pi)$. If H1 produces only CONDITIONAL or NOT-FORCED, the entire Arc Hawking's verdict structure shifts substantially.

---

## 8. What Arc Hawking Is Not

- **Not** a derivation of the Einstein equations. Hawking's calculation runs on QFT-in-curved-spacetime; ED's substrate calculation runs on V5 cross-chain correlations at a saturated decoupling surface. The substrate calculation does not require the Einstein equation to be derived. (GR-4A — Einstein-equation emergence — remains SPECULATIVE-not-REFUTED in the priority list.)
- **Not** a resolution of the firewall paradox. Standard physics literature on BH information has produced multiple proposed paradoxes (firewall, ER=EPR, soft-hair). ED's approach is to derive the substrate-level mechanism and let the paradox-content fall out where it does. If the substrate produces a Page-curve-consistent spectrum, the standard information paradox doesn't arise as an in-framework problem. If the substrate produces a thermal spectrum without correlations, the framework has its own version of the information question.
- **Not** a treatment of rotating BHs (Kerr). Schwarzschild-class horizons are the focus. Rotating-BH extensions are downstream content (couples with O1 superradiance amplitude and O3 Kerr interior audit).
- **Not** a treatment of charged BHs (Reissner-Nordström). Same caveat — charged extensions involve T17 gauge-field structure at the horizon and are downstream.
- **Not** an empirical-prediction arc in the strong sense. Hawking radiation has not been directly observed at the gravitational scale. ED's structural prediction sits next to the standard semiclassical prediction; the empirical verification awaits primordial-BH evaporation data, analog-Hawking experiments, or whatever future observational windows produce.
- **Not** a treatment of the BH interior. BH-3 closed the saturated-zone interior structure for Schwarzschild-class BHs. Arc Hawking treats only the horizon and exterior.

The deliverable is the FORCED / CONDITIONAL / INHERITED classification of the Hawking spectrum's mathematical content at the substrate level, with H1 as the gate.

---

## 9. Recommended Next Steps

1. **H-1 (next memo): Derive spectral form and temperature from V5 cross-chain correlations at a saturated decoupling surface.** Construct the substrate-level calculation:

   (a) Identify the V5 cross-chain correlation function across the saturated horizon. The substrate state is: $\Gamma_{\mathrm{cross}}$ falls below hydrodynamic-window resolution from interior to exterior, but participation cannot accumulate at the surface, so cross-chain correlations re-route around the surface.

   (b) Compute the substrate-level emission spectrum from the asymmetric flow. The standard QFT-in-curved-spacetime calculation produces $T = \kappa/(2\pi)$ via Bogoliubov transformation. The ED calculation should reproduce the same result if the substrate-to-continuum identification is correct.

   (c) Honest verdict whether the construction is FORCED, CONDITIONAL (and on what), or NOT FORCED.

   File: `arcs/arc-Hawking/H-1_spectral_form_and_temperature.md`. Estimated 2–3 sessions.

2. **(Defer until H-1 closes) Open OQ-Hawking-V5kernel:** what is the explicit functional form of V5 used in the calculation? V5 has been treated as a finite-width memory kernel in the framework's other applications (DCGT → Maxwell viscoelastic memory in soft matter), but the specific functional form has not been pinned down. The Hawking calculation may force closer specification of V5 — or may proceed at the form-FORCED level without it.

3. **(Defer until H-1 closes) Stage H-4 (V5 cutoff) as the first-subleading-order memo.** The high-frequency cutoff is the most ED-distinctive piece of content in the arc — the place where ED predicts deviation from semiclassical Hawking. H-4 is the natural follow-on memo after H-1.

---

**Pause for further instruction.**
