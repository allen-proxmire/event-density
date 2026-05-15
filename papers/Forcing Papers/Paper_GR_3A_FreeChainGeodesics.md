# Paper GR-3A — Free-Chain Geodesic Worldlines (FORCED-conditional)

**Series:** Wave-3 Gravity Arc Extension — GR-3A
**Status:** Wave-3 generative paper; M3 verdict at write-time (FORCED-conditional on acoustic-metric guardrails active)
**Companions:** Paper_017 (Lorentz covariantization), Paper_014 (V1 curved acoustic background), Paper_033 (Arc ED-10), Paper_035 (acoustic-metric guardrails), Paper_089 (V1).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of free-chain geodesic-worldline motion from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates (P-FreeChain).
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim substrate derivation of the free-chain conditions themselves — P-FreeChain (no inter-chain V5 coupling, no external force, test-chain limit, eikonal regime) is declared as a paper-specific postulate; substrate-level proof is OPEN.
5. **INHERITED vs FORCED breakdown:** The geodesic-equation form is form-CONSISTENT under P-FreeChain + active acoustic-metric guardrails (Paper_035) (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3); the eikonal reduction of V1-kernel content to the substrate-action $S = -mc\int d\tau$ is OPEN. Full Einstein-equation dynamics is Phase-3 SPECULATIVE.

---

## Abstract

This paper supplies the **GR-3A** result: substrate-level **free chains** (chains satisfying P-FreeChain — no V5 inter-chain coupling, no external force, test-chain back-reaction negligible, eikonal regime) follow **geodesic worldlines** of the acoustic metric $g^{\mathrm{ac}}_{\mu\nu}$ (Paper_017). The geodesic equation is derived via eikonal / stationary-phase reduction of the substrate V1-kernel propagation to the relativistic test-particle action $S = -mc\int d\tau$, then standard variational machinery. The result is **FORCED-conditional**: forced given the acoustic-metric guardrails (C1)-(C6) of Paper_035 + P-FreeChain; outside these conditions the result is not guaranteed. Per Paper_095 form-FORCED / value-INHERITED methodology, verdict is **M3** (FORCED-conditional). Key falsifier **F1:** empirical detection of free-chain worldlines NOT following acoustic-metric geodesics in regimes where guardrails are active.

---

## §1 Statement of Result

**Claim.** **Free chains** — substrate chains with no inter-chain coupling other than acoustic-metric coupling, propagating without external force-content — follow **geodesic worldlines** of the acoustic metric $g^{\mathrm{ac}}_{\mu\nu}$ (Paper_017). Specifically, the worldline $x^\mu(\tau)$ of a free chain satisfies the geodesic equation
$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta}(x) \frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau} = 0 ,$$
where $\Gamma^\mu_{\alpha\beta}$ are the Christoffel symbols of the acoustic metric.

The structural form is **FORCED-conditional** on acoustic-metric guardrails (C1)-(C6) of Paper_035 being active. Free-chain propagation in regimes where guardrails fail does NOT necessarily follow geodesic motion.

Verdict: **M3** (FORCED-conditional, per Paper_023 Intermediate-Path-C / NS-Smoothness verdict-tier).

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P01 (Chains)** — supplies the chain content whose worldlines are considered.
- **P05 (Polarity-transport)** — supplies the substrate-level transport along edges.
- **P11 (Commitment-irreversibility)** — supplies the directional worldline structure.
- **P13 (Time homogeneity)** — supplies the temporal-translation symmetry.

### 2.2 Upstream Dependencies

- **I-017:** Substrate→continuum Lorentz covariantization — acoustic metric structure.
- **I-014:** V1 in curved acoustic background (N1/GR1).
- **I-033:** Arc ED-10 scalar-tensor covariantization.
- **I-035:** Acoustic-metric guardrails (C1)-(C6).
- **I-089:** V1 finite-width retarded kernel.
- **I-RQM-T10:** Lightlike worldlines for $\sigma = 0$ rule-types.
- **I-Geodesic:** Standard differential-geometry geodesic theory.
- **I-Variational:** Standard variational principle for geodesics.

---

## §3 Derivation

### 3.1 Free-chain definition

A **free chain** is a substrate chain satisfying:
1. **No inter-chain coupling beyond acoustic metric:** the chain does not interact with other chains via V5 cross-chain content significantly. V1 within-chain propagation is the dominant dynamics.
2. **No external force content:** no gauge-field coupling (T17), no Higgs-class scalar coupling, no electromagnetic / strong / weak interactions active.
3. **Test-chain condition:** the chain's own contribution to the acoustic-metric curvature is negligible (test-particle limit).

Under these conditions, the chain's worldline is determined entirely by:
- The acoustic-metric background $g^{\mathrm{ac}}_{\mu\nu}$ (Paper_017).
- The substrate's V1 kernel propagation structure (Paper_089).
- P11 commitment-irreversibility supplying forward-causal direction.

### 3.2 Variational principle from substrate V1 propagation

For a free chain, the substrate-level participation amplitude propagates via V1 kernel. In the **eikonal limit** (semiclassical-trajectory limit), the dominant contribution to amplitude propagation comes from the substrate-edge content along which the rapid-phase $\pi_K$ accumulation is **stationary**.

By the standard eikonal / stationary-phase argument (I-Variational), the chain's worldline minimizes the **substrate-action**:
$$S = -mc \int \sqrt{-g^{\mathrm{ac}}_{\mu\nu}\, dx^\mu \, dx^\nu} = -mc \int d\tau ,$$
where $\tau$ is the proper time along the worldline (substrate-derived from the acoustic metric).

This is the standard relativistic test-particle action. The free-chain worldline minimizes this action.

### 3.3 Geodesic equation from variational principle

Standard variational machinery (I-Variational + I-Geodesic): minimizing $S = -mc\int d\tau$ yields the geodesic equation
$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau} = 0 ,$$
with Christoffel symbols computed from $g^{\mathrm{ac}}_{\mu\nu}$.

This is the **free-chain geodesic equation**: the substrate-level statement that free chains follow geodesics of the acoustic metric.

### 3.4 Why FORCED-conditional

The result is FORCED **given** the following conditions:
- Acoustic-metric guardrails active (Paper_035 (C1)-(C6)).
- Test-chain limit (chain's own back-reaction on $g^{\mathrm{ac}}$ is negligible).
- Free-chain conditions per §3.1.
- Eikonal limit / stationary-phase argument applicable.

**Without** these conditions, the result does NOT hold:
- Outside guardrails: acoustic-metric description breaks down; substrate microstructure exposed.
- Strong-coupling regimes (V5 dominant, inter-chain coupling significant): chain dynamics include explicit interaction terms.
- Strong-field regimes: test-chain back-reaction is non-negligible; full Einstein dynamics required.
- Non-eikonal regimes: quantum interference effects dominate; chain-as-classical-particle approximation fails.

This is the conditional content of the GR-3A result. Within the regime, geodesic motion is forced; outside, the substrate framework predicts deviations.

### 3.5 Connection to lightlike worldlines (Paper_RQM_T10)

For massless free chains ($\sigma = 0$ rule-types per Paper_RQM_T10), the substrate-action $S = -mc\int d\tau$ reduces to the null-curve action; the geodesic equation specializes to the **null geodesic** equation:
$$g^{\mathrm{ac}}_{\mu\nu}\, \frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda} = 0 ,$$
for an affine parameter $\lambda$.

Both massive and massless free chains follow acoustic-metric geodesics — the timelike geodesic for $m > 0$, the null geodesic for $m = 0$. The two are unified under the variational principle of §3.2.

### 3.6 Consistency with Arc ED-10

Paper_033 (Arc ED-10) supplies the scalar-tensor acoustic-metric covariantization with kinetic-term modifications proportional to $\mu(|\nabla\Phi|/a_0)$. In the deep-MOND regime, the kinetic-term modifications introduce non-trivial coupling between the scalar field $\Phi$ and the chain's worldline.

In the **Newtonian limit** (high acceleration regime $a \gg a_0$, $\mu \to 1$), Arc ED-10 reduces to standard GR kinematics and the free-chain geodesic equation of this paper applies directly.

In the **deep-MOND limit** ($a \ll a_0$, $\mu \to 0$), the scalar-field coupling modifies the effective metric. Free chains follow geodesics of the **modified effective metric**, not the bare $g^{\mathrm{ac}}$. The deep-MOND superluminality cost (Paper_034) is consistent with this modification.

### 3.7 What is NOT covered

- **Full Einstein equation dynamics** (substrate derivation of $G_{\mu\nu} = 8\pi G T_{\mu\nu}$): OPEN, Phase-3 SPECULATIVE.
- **Back-reaction of test chain on $g^{\mathrm{ac}}$:** Test-chain limit assumed.
- **Quantum corrections to geodesic motion:** Eikonal limit assumed; corrections from V1 finite-width (Paper_014 N1/GR1) introduce $O(\ell_P^2 R)$ corrections.

These OPEN items are part of the gravity arc's long-horizon program. This paper supplies the **kinematic** free-chain-as-geodesic result conditional on the active guardrails.

### 3.8 Numerical content

- Specific worldlines per substrate configuration: INHERITED via standard GR matching.
- Acoustic-metric values $g^{\mathrm{ac}}_{\mu\nu}$ per substrate configuration: INHERITED via Paper_017 + empirical input.
- Free-chain geodesic equation form: FORCED-conditional.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P01, P05, P11, P13 primitives | P | Primitives. |
| 2 | Acoustic-metric Lorentz covariantization | I | Paper_017. |
| 3 | V1 in curved acoustic background | I | Paper_014. |
| 4 | Acoustic-metric guardrails (C1)-(C6) | I | Paper_035 (postulates). |
| 5 | Free-chain definition (no V5 coupling, no external force, test-chain) | P | **P-FreeChain:** no V5 coupling; V1-only within-chain kernel; test-chain (negligible back-reaction); eikonal/geodesic regime. Declared as paper-specific postulate; substrate-derivation OPEN. |
| 6 | Eikonal / stationary-phase limit | A→regime | Regime selection. |
| 7 | Substrate-action $S = -mc\int d\tau$ via eikonal/V1 reduction | OPEN | Reduction of V1-kernel content to substrate-action $S = -mc\int d\tau$ via eikonal limit — substrate-level OPEN; currently asserted via analogy with standard eikonal/WKB. |
| 8 | Minimization yields geodesic equation | I | Standard variational (I-Variational). |
| 9 | Geodesic equation $\ddot x^\mu + \Gamma^\mu_{\alpha\beta}\dot x^\alpha\dot x^\beta = 0$ | P | Geodesic equation written down per Paper_095 §2.3 (standard-form construction = definitional). |
| 10 | Null geodesic specialization for $m = 0$ | I | Paper_RQM_T10. |
| 11 | Consistency with Arc ED-10 in Newtonian limit | I | Paper_033. |
| 12 | Deviations in deep-MOND regime | I | Paper_033 + Paper_034. |
| 13 | Full Einstein dynamics | OPEN | Phase-3 SPECULATIVE. |
| 14 | FORCED-conditional verdict (M3) | A→position | Per Paper_095 + intermediate-path-C verdict-tier. |

---

## §5 Falsification Criteria

- **F1:** Empirical detection of free-chain (test-particle) worldlines NOT following acoustic-metric geodesics in regimes where guardrails are active. Would refute the FORCED-conditional result.
- **F2:** Acoustic-metric guardrails (Paper_035) shown to fail under any admissible substrate variation in a regime where geodesic motion is expected. Would refute the conditional anchor.
- **F3:** Substrate evidence that the eikonal / stationary-phase limit produces a non-geodesic equation of motion. Would refute step 7.
- **F4:** Variational principle for free-chain action shown to produce a non-geodesic equation. Would refute step 8.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the **GR-3A (Free-Chain Geodesic Worldlines)** result for the gravity arc, addressing the previously-flagged corpus gap. The result is FORCED-conditional: structurally forced within the regime where acoustic-metric guardrails are active.

**Relationship to other papers:**
- **Paper_017:** acoustic-metric source.
- **Paper_014:** V1 in curved background (companion).
- **Paper_033:** Arc ED-10 scalar-tensor extension (deep-MOND regime).
- **Paper_035:** guardrails supplying the conditional anchor.
- **Paper_RQM_T10:** null-geodesic specialization for $\sigma = 0$.

**Numerical content INHERITED.** Specific worldlines, $g^{\mathrm{ac}}$ values. **Form FORCED-conditional.** Free-chain geodesic equation within acoustic-metric guardrail regime.

**Future work.** Phase-3 substrate-level Einstein-equation emergence (Phase-3 SPECULATIVE); back-reaction analysis beyond test-chain limit; quantum corrections to geodesic motion (V1 finite-width effects on chain trajectories).

Verdict: **M3** (FORCED-conditional).

---

**End Paper GR-3A.**
