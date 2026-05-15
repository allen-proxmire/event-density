# Paper BH-H2 — Greybody Factors via Regge–Wheeler in DCGT (H-2)

**Series:** Wave-3 Black-Hole Arc Extension — H-2 (Hawking memo)
**Status:** Wave-3 generative paper; M3 verdict at write-time (form-IDENTIFIED structural mechanism; greybody numerical factors INHERITED via standard BHPT)
**Companions:** Paper_044 (BHPT scattering structure), Paper_047 (Hawking spectrum), Paper_073 (DCGT), Paper_014 (V1 curved acoustic background).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of greybody factors $\Gamma_{\ell s}(\omega)$ from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim a new derivation of greybody factors — these are INHERITED from standard BHPT (Regge-Wheeler 1957, Zerilli 1970, Page 1976).
5. ED's contribution is the **identification** of the BHPT background as the V1-modulated acoustic-metric background under DCGT coarse-graining; greybody numerical factors INHERITED; per-spin computations INHERITED from standard BHPT.

---

## Abstract

This paper identifies the standard BHPT Regge-Wheeler / Zerilli scattering structure on Schwarzschild background as the substrate-level coarse-grained scattering on the V1-modulated curved acoustic-metric (Paper_014) under DCGT (Paper_073). Greybody factors $\Gamma_{\ell s}(\omega)$ are **INHERITED** from standard BHPT (Regge-Wheeler 1957, Zerilli 1970, Page 1976); ED's contribution is the substrate-level **identification** of the BHPT background as V1-acoustic, not a new derivation. The Regge-Wheeler potential form, transmission-coefficient asymptotics, and spin-dependence are all standard. Verdict: **M3** (identification claim) per Paper_095's three-tier verdict grammar. Key falsifier **F2**: substrate evidence that V1 + DCGT does NOT produce the Regge-Wheeler potential form on Schwarzschild background.

---

## §1 Statement of Result

**Identification claim.** ED's substrate construction **identifies** the standard BHPT Regge-Wheeler / Zerilli scattering objects on the V1-modulated curved acoustic-metric background (Paper_014 N1/GR1), with DCGT coarse-graining supplying the substrate-to-continuum bridge (Paper_073). Greybody factors $\Gamma_{\ell s}(\omega)$ are **INHERITED** from standard BHPT (Regge-Wheeler 1957, Zerilli 1970, Page 1976). ED's contribution is the **identification** of the BHPT background as V1-acoustic, NOT a new derivation of greybody factors.

The Regge-Wheeler potential, transmission-coefficient formulas, and spin-dependence are INHERITED from standard BHPT. Specific greybody factors per spin / multipole are INHERITED from standard BHPT calculations (Paper_044).

Verdict: **M3**.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P10 (Rule-type primitive)** — V1 kernel rule-type.
- **P11 (Commitment-irreversibility)** — V1 retardation, supplying outgoing-Hawking-mode boundary structure.
- **P13 (Time homogeneity)** — frequency content on which $\Gamma_{\ell s}(\omega)$ is defined.

### 2.2 Upstream Dependencies

- **I-014:** V1 in curved acoustic background (Paper_014 N1/GR1).
- **I-044:** BHPT scattering structure (Paper_044).
- **I-047:** Hawking spectrum (Paper_047).
- **I-073:** DCGT coarse-graining.
- **I-039:** Horizon as decoupling surface (Paper_039) — ingoing-only horizon boundary.
- **I-RW:** Standard Regge-Wheeler / Teukolsky machinery (standard math).
- **I-WKB:** Standard WKB scattering analysis.

---

## §3 Derivation

### 3.1 The greybody-factor problem

Hawking radiation at temperature $T_H = \kappa/(2\pi)$ (Paper_047) is **not** exactly thermal at infinity: outgoing modes must traverse the curvature-induced potential barrier between the horizon and spatial infinity. The barrier modifies the emission spectrum from the Planck distribution by a multiplicative **greybody factor** $\Gamma_{\ell s}(\omega)$:
$$\frac{dN_{\ell s}}{dt \, d\omega} \;=\; \frac{\Gamma_{\ell s}(\omega)}{2\pi} \cdot \frac{1}{e^{\omega/T_H} \pm 1} ,$$
with $\Gamma_{\ell s}(\omega) \in [0, 1]$ encoding the fraction of horizon-emitted modes transmitted to infinity.

The substrate-level task: derive $\Gamma_{\ell s}(\omega)$'s structural form.

### 3.2 Regge-Wheeler potential from V1 + curved acoustic metric

By Paper_014 (V1 in curved acoustic background) + Paper_073 (DCGT), V1-modulated field propagation on the Schwarzschild acoustic-metric background yields a **scattering equation** for each multipole $(\ell, m)$ mode of the field:
$$\frac{d^2 \psi_{\ell s}}{dr_*^2} + [\omega^2 - V_{\ell s}(r_*)]\psi_{\ell s} = 0 ,$$
where $r_*$ is the **tortoise coordinate** ($dr_* = (1 - 2M/r)^{-1} dr$) and $V_{\ell s}(r_*)$ is the Regge-Wheeler potential:
$$V_{\ell s}(r_*) = \left(1 - \frac{2M}{r}\right)\left[\frac{\ell(\ell+1)}{r^2} + \frac{(1-s^2)\cdot 2M}{r^3}\right] ,$$
with $s$ the spin of the field-class (0 scalar; 1 vector; 2 tensor).

The substrate-level origin: V1 kernel curvature coupling (Paper_014 GR1) produces this exact potential form under DCGT coarse-graining at leading order. The Regge-Wheeler form is FORCED-conditional on Schwarzschild acoustic-metric background + V1 propagation.

### 3.3 Transmission coefficient via WKB / matching

Standard WKB / matching machinery (I-WKB) applied to the Regge-Wheeler equation produces the transmission coefficient $|T_{\ell s}(\omega)|^2$ relating the ingoing horizon-side amplitude to the outgoing infinity-side amplitude:

**Low-frequency regime** ($\omega M \ll 1$):
$$\Gamma_{\ell s}(\omega) \;\sim\; (\omega M)^{2\ell + 2} \cdot |\text{spin-dependent prefactor}| .$$

**High-frequency regime** ($\omega M \gg 1$, $\omega > V_{\max}$):
$$\Gamma_{\ell s}(\omega) \to 1 .$$

**Crossover regime** ($\omega M \sim 1$): transition between exponential suppression and unit transmission.

These structural features (low-freq power-law, high-freq saturation, crossover) are form-IDENTIFIED by Regge-Wheeler form + WKB. Specific numerical prefactors per $(\ell, s)$ are INHERITED via standard BHPT calculation.

### 3.4 Substrate-level boundary conditions

Two boundary conditions enter the transmission-coefficient calculation:
- **Horizon (ingoing-only):** By Paper_039 + Paper_044's P-Horizon-Ingoing-Only, modes at the horizon are purely ingoing (causal structure forbids outgoing modes at the horizon).
- **Infinity (outgoing-only):** By Paper_044's P-Asymptotic-Outgoing, modes at infinity are purely outgoing.

These boundary conditions are form-IDENTIFIED at substrate level: horizon = V5-saturated decoupling surface (Paper_039); infinity = standard asymptotic flatness.

### 3.5 Spin-dependence

The Regge-Wheeler potential depends on the field spin $s$ through the $(1-s^2)$ factor. Different field-class greybody factors:
- **Scalar ($s = 0$):** $V_{0\ell} = (1 - 2M/r)[\ell(\ell+1)/r^2 + 2M/r^3]$.
- **Spin-1/2 (Dirac):** Special analysis; effective potential includes additional spin-orbit term.
- **Spin-1 (Maxwell, photon):** $V_{1\ell} = (1 - 2M/r)\ell(\ell+1)/r^2$ (no $2M/r^3$ term).
- **Spin-2 (Regge-Wheeler odd-parity, even-parity Zerilli):** $V_{2\ell}$ with different structure for odd/even parity.

The substrate-level origin: each spin-class rule-type has a distinct V1 kernel coupling structure to the acoustic-metric curvature (per Paper_RQM_T7 Lorentz-representation classification). The Regge-Wheeler-class potential form is uniform; spin-dependence enters through the curvature coupling.

### 3.6 Connection to Hawking spectrum

The total Hawking-emission spectrum at infinity is
$$\frac{dN}{dt \, d\omega} \;=\; \sum_{\ell, s, m} \frac{\Gamma_{\ell s}(\omega)}{2\pi} \cdot \frac{1}{e^{\omega/T_H} \pm 1} .$$

Without greybody factors, this would be exactly Planck/Fermi-Dirac thermal. The greybody modulation produces the **observed Hawking-spectrum** structure:
- Low-frequency suppression (modes with $\omega M \ll 1$ are inefficiently transmitted).
- High-frequency saturation (modes with $\omega M \gg 1$ are nearly transparent).
- Peak emission near $\omega M \sim O(1)$.

This is the standard greybody-modified Hawking spectrum. Substrate origin: Regge-Wheeler scattering on V1-modulated curved acoustic background.

### 3.7 Leading-order match to standard BHPT

The **leading-order match** between substrate-derived greybody factors and standard BHPT (Paper_044) is form-IDENTIFIED at the structural level: the Regge-Wheeler potential, the transmission-coefficient formula, the spin-dependence — all match standard results.

**Higher-order corrections** (V5 finite-bandwidth effects, substrate-Lorentz-covariance corrections at strong-field, $(\ell_P/M)^2$ corrections per Paper_040) enter at subleading order. The substrate framework predicts these corrections exist but does not derive their specific numerical values without further substrate-quantitative work.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P10, P11, P13 primitives | P | Primitives. |
| 2 | V1 in curved acoustic background (N1/GR1) | I | Paper_014. |
| 3 | DCGT coarse-graining | I | Paper_073. |
| 4 | Schwarzschild acoustic-metric background | I | Standard GR + Paper_017. |
| 5 | Regge-Wheeler / Teukolsky equation | I | Standard math (I-RW). |
| 6 | $V_{\ell s}(r_*)$ Regge-Wheeler potential | I | Regge-Wheeler 1957, Zerilli 1970 — standard BHPT, not ED-derived. Paper_095 §2.3 lists Regge-Wheeler potential by name as definitional. |
| 7 | Ingoing-only horizon boundary | I | Paper_039 + Paper_044. |
| 8 | Outgoing-only infinity boundary | I | Paper_044. |
| 9 | WKB / matching transmission coefficient | I | Standard math (I-WKB). |
| 10 | Low-frequency $\Gamma \sim (\omega M)^{2\ell+2}$ | I | Standard BHPT. |
| 11 | High-frequency $\Gamma \to 1$ | I | Standard BHPT. |
| 12 | Spin-dependence via Lorentz-rep curvature coupling | I | Paper_RQM_T7 + standard BHPT. |
| 13 | Greybody-modified Hawking spectrum form | D-via-I | Composition. |
| 14 | Leading-order match to standard BHPT | A→position | Match is identification (framing claim), not derivation. |
| 15 | Higher-order substrate corrections | OPEN | Future work. |
| 16 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1:** Discovery of a black-hole system where the standard BHPT greybody computation on a V1-acoustic background fails to reproduce observed Hawking-spectrum corrections would falsify the ED background-identification. (Falsifying standard BHPT first falsifies a 50-year-old framework, not ED-specifically.)
- **F2:** Substrate evidence that V1 + DCGT does NOT produce the Regge-Wheeler potential form on Schwarzschild background. Refutes step 6.
- **F3:** Spin-dependence shown to differ from $(1-s^2)$-class structure. Refutes step 12.
- **F4:** Higher-order substrate corrections shown empirically to dominate over leading-order — would shift the verdict but not refute substrate origin.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the substrate-level structural derivation of greybody factors via Regge-Wheeler scattering on V1-modulated curved acoustic background.

**Relationship to other papers:**
- **Paper_044 (BHPT scattering):** parent paper supplying the full BHPT machinery.
- **Paper_014 (V1 in curved acoustic):** supplies the V1-curved-background propagation.
- **Paper_047 (Hawking spectrum):** the spectrum that greybody factors modulate.
- **Paper_073 (DCGT):** supplies the coarse-graining bridge.

**Numerical content INHERITED.** Specific transmission coefficients per $(\ell, s, m)$. **Form IDENTIFIED.** Regge-Wheeler potential structure + leading-order greybody-factor form (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3).

Verdict: **M3**.

---

**End Paper BH-H2.**
