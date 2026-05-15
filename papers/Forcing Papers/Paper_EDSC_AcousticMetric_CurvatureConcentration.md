# Paper EDSC-AcousticCurvature — Acoustic-Metric Curvature Concentration on Mobility-Gradient Scale

**Series:** Wave-3 ED-SC 1.x / 4.x Extension
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_017 (Lorentz covariantization → acoustic metric), Paper_035 (acoustic-metric guardrails), Paper_096 (cross-scale invariance), Paper_ED_SC_4.1, Paper_ED_SC_4.6.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the acoustic-metric curvature concentration result from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim new derivation — analogue-gravity geometry is INHERITED (Unruh 1981, Visser 1998). The acoustic-metric curvature is **not** the GR Einstein-equation curvature; it is a kinematic-frame curvature under ED-Phys-10 guardrails.
5. The paper is a **structural-identification note**: $\mu \leftrightarrow$ V5-bandwidth. Mobility profiles and curvature values per substrate configuration INHERITED.

---

## Abstract

This paper is a structural-identification note: the acoustic-metric Ricci scalar $R_{\mathrm{ac}}$, computed by standard analogue-gravity machinery (Unruh 1981, Visser 1998) on the Visser-form acoustic metric (Paper_017), concentrates on substrate mobility-gradient scales, scaling as $R_{\mathrm{ac}} \propto |\nabla\mu|^2/\mu^2$ at leading order. ED's substrate-level contribution is the **identification** $\mu(x) \leftrightarrow$ V5 cross-chain bandwidth content (Paper_090); the acoustic-metric construction and the Ricci-on-Visser computation are INHERITED. Mobility profiles and specific curvature values per configuration INHERITED. Verdict: **M3** (identification + value-inherited) per Paper_095's three-tier verdict grammar. Key falsifier **F2**: substrate evidence that V5 mobility content does NOT enter the acoustic-metric form.

---

## §1 Statement of Result

**Reframe.** This paper is a **structural-identification note**, NOT a derivation. The acoustic-metric construction and the Ricci-on-Visser-metric computation are **INHERITED** from analogue-gravity (Unruh 1981, Visser 1998). Paper_095 §2.3 names the Ricci-of-Visser computation by name as definitional. ED's substrate contribution is the **identification** $\mu \leftrightarrow$ V5-bandwidth. Verdict **M3 (identification + value-inherited)**, not derivation-grade.

**Claim.** The acoustic-metric kinematic curvature concentrates on **mobility-gradient scales**: regions of substrate where the substrate-level mobility (V5-bandwidth content modulating cross-chain coherent propagation) varies most rapidly. Specifically:
$$R_{\mathrm{ac}}(x) \;\propto\; |\nabla\mu(x)|^2 \;+\; O(\nabla^2\mu) ,$$
where $\mu(x)$ is the substrate mobility field and $R_{\mathrm{ac}}$ is the acoustic-metric Ricci scalar.

The structural form $R_{\mathrm{ac}} \propto |\nabla\mu|^2$ at leading order is form-IDENTIFIED by the acoustic-metric form $g^{\mathrm{ac}}_{\mu\nu}[\rho_0, \mu]$ (Paper_017) + mobility-dependent kinetic-term structure. Specific mobility profiles per substrate configuration INHERITED.

Verdict: **M3**.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P02 (Participation)** — substrate density / mobility field content.
- **P03 (Channel + locus indexing)** — spatial structure for gradient calculation.
- **P10 (Rule-type primitive)** — V5 supplying mobility content.

### 2.2 Upstream Dependencies

- **I-017:** Substrate→continuum Lorentz covariantization → acoustic metric.
- **I-035:** Acoustic-metric guardrails (C1–C6).
- **I-090:** V5 cross-chain correlation kernel (mobility source).
- **I-073:** DCGT coarse-graining.
- **I-096:** Cross-scale invariance.
- **I-AcousticAnalog:** Standard acoustic-analog gravity machinery (Unruh, Visser).

---

## §3 Derivation

### 3.1 The acoustic metric and mobility field

By Paper_017 (substrate→continuum Lorentz covariantization), the acoustic metric takes the standard analog-gravity form
$$g^{\mathrm{ac}}_{\mu\nu}[\rho_0, \mu] \;=\; \frac{\rho_0}{\mu}\begin{pmatrix} -(c_s^2 - v^2) & -v_j \\ -v_i & \delta_{ij} \end{pmatrix} ,$$
where $\rho_0$ is the substrate participation density, $\mu$ is the substrate mobility, $c_s$ is the local substrate sound speed, and $v$ is the local substrate flow velocity. (Visser-form acoustic metric, I-AcousticAnalog.)

The mobility $\mu(x)$ is supplied by V5 cross-chain content (Paper_090): regions of high V5 bandwidth permit high mobility; regions of low V5 bandwidth (e.g., near horizons, Paper_039) suppress mobility.

### 3.2 Curvature from acoustic-metric form

Standard differential-geometry calculation: the Ricci scalar of the acoustic metric depends on derivatives of $\rho_0$, $\mu$, $v$. For static configurations (no flow, $v = 0$) and uniform participation density ($\rho_0 = $ const), the curvature is dominated by the mobility field:
$$R_{\mathrm{ac}}(x) \;=\; -\frac{1}{\mu^2}|\nabla\mu|^2 \;+\; \frac{1}{\mu}\nabla^2\mu \;+\; O(\nabla^3) .$$

At leading order in mobility gradients, $R_{\mathrm{ac}} \propto |\nabla\mu|^2 / \mu^2$. The curvature **concentrates** where the mobility gradient is largest.

### 3.3 Why mobility-gradient scale concentrates curvature

Physical interpretation: the acoustic metric encodes the effective spacetime experienced by substrate-coarse-grained excitations. Regions of varying mobility (e.g., near substrate features where V5 bandwidth changes rapidly) appear as curved spacetime to these excitations.

The mathematical mechanism: the kinetic-term coefficient in the substrate effective Lagrangian is $1/\mu$. When $\mu$ varies, this coefficient varies, producing effective non-uniformity of the kinematic frame. Curvature is the standard differential-geometric measure of such non-uniformity.

The substrate-level statement: substrate mobility gradients are the **source** of acoustic-metric curvature. Regions of uniform mobility appear flat; regions of varying mobility appear curved.

### 3.4 Connection to ED-SC 1.x

The ED-SC 1.x program (per memory `project_ed_sc_3_arc.md` predecessor) developed canonical scale-correspondence content. This paper supplies the **structural mechanism** by which substrate-level mobility gradients produce coarse-grained spacetime curvature.

Specifically: the canonical operating point $\xi_{\mathrm{canonical}} = 1.7575$ lu (Paper_096) corresponds to a specific mobility-gradient configuration; the substrate kernel-content at this operating point produces a characteristic acoustic-metric curvature pattern.

### 3.5 Connection to ED-SC 4.x SCBU framework

Under Paper_ED_SC_4.1 and Paper_ED_SC_4.6, the substrate-cosmology boundary $R_H = c/H_0$ is the substrate-level surface where V5 bandwidth (mobility) saturates. The acoustic-metric curvature at the SCBU boundary is the cosmological-scale curvature; intermediate-scale curvatures (at galactic, planetary, atomic scales) inherit from the mobility-gradient profile across the corresponding substrate region.

In Paper_GR_Lambda_V1 (this batch's earlier paper), the cosmological constant $\Lambda$ is derived as a V1 cosmological-scale integral. The curvature-mobility relation derived here provides the substrate-level **mechanism** by which substrate mobility gradients translate to spacetime curvature, including the integrated cosmological-constant contribution.

### 3.6 Quantitative structure

For a static, slowly-varying mobility field $\mu(r)$ in a region near a substrate feature (e.g., near a horizon or massive object), the acoustic-metric Ricci scalar is approximately
$$R_{\mathrm{ac}}(r) \;\approx\; \frac{|\nabla\mu(r)|^2}{\mu(r)^2} + \text{(subleading)} .$$

The **mobility-gradient scale** is the characteristic length over which $\mu$ varies significantly:
$$L_{\mathrm{mob}}(r) \;\equiv\; \frac{\mu(r)}{|\nabla\mu(r)|} .$$

The curvature scales as $R_{\mathrm{ac}} \sim 1/L_{\mathrm{mob}}^2$. Small mobility-gradient scales (sharp mobility variations) produce large curvature; large mobility-gradient scales (smooth mobility variation) produce small curvature.

This is the **curvature concentration on mobility-gradient scale** result: acoustic-metric curvature is concentrated where the substrate mobility gradient is sharpest.

### 3.7 Numerical content

- Specific mobility profiles $\mu(x)$ per substrate configuration: INHERITED.
- Specific curvature values $R_{\mathrm{ac}}$ per substrate configuration: INHERITED.
- Structural relation $R_{\mathrm{ac}} \propto |\nabla\mu|^2$ at leading order: form-IDENTIFIED.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P03, P10 primitives | P | Primitives. |
| 2 | Acoustic-metric form $g^{\mathrm{ac}}[\rho_0, \mu]$ | I | Paper_017 + I-AcousticAnalog. |
| 3 | Mobility $\mu(x)$ from V5 content | I | Paper_090. |
| 4 | Acoustic-metric guardrails active | I | Paper_035. |
| 5 | Ricci-scalar computation from $g^{\mathrm{ac}}$ | I | Standard Visser/Unruh analogue-gravity computation (Unruh 1981, Visser 1998); not ED-derived. Paper_095 §2.3 names Ricci-of-Visser as definitional. |
| 6 | Leading-order $R_{\mathrm{ac}} \propto |\nabla\mu|^2/\mu^2$ | I | Standard Visser/Unruh analogue-gravity computation; not ED-derived. |
| 7 | Mobility-gradient scale $L_{\mathrm{mob}} = \mu/|\nabla\mu|$ | I | Standard analogue-gravity definitional scale. |
| 8 | $R_{\mathrm{ac}} \sim 1/L_{\mathrm{mob}}^2$ | I | Standard analogue-gravity (Visser 1998). |
| 9 | Curvature concentration on mobility-gradient scale | I | Standard analogue-gravity consequence. |
| 9b | $\mu \leftrightarrow$ V5-bandwidth identification | A→position | Substrate identification; framing claim. |
| 10 | Connection to canonical operating point | I | Paper_096. |
| 11 | Connection to SCBU boundary | I | Papers_ED_SC_4.1, 4.6. |
| 12 | Specific mobility profiles per configuration | I | Empirical. |
| 13 | Verdict M3 | A→position | Per Paper_095. |

---

## §5 Falsification Criteria

- **F1:** Discovery of a physical system where the V5-bandwidth $\leftrightarrow \mu$ identification fails to reproduce observed curvature-concentration in the analogue-gravity regime would falsify the substrate identification. (Falsifying Ricci-on-Visser is definitional, not falsifiable; not claimed.)
- **F2:** Substrate evidence that V5 mobility content does NOT enter the acoustic-metric form. Refutes step 3.
- **F3:** Acoustic-metric guardrails (Paper_035) shown to fail in regimes claimed for this paper. Propagates.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the substrate-level structural mechanism by which acoustic-metric curvature concentrates on substrate mobility-gradient scales.

**Relationship to other papers:**
- **Paper_017:** acoustic-metric source.
- **Paper_090:** V5 supplying mobility content.
- **Paper_035:** guardrails.
- **Paper_ED_SC_4.1, 4.6:** SCBU framework placing this in the cross-scale picture.
- **Paper_GR_Lambda_V1:** uses curvature-mobility relation for cosmological-constant derivation.

**Numerical content INHERITED.** Mobility profiles, specific curvatures. **Form IDENTIFIED.** $R_{\mathrm{ac}} \propto |\nabla\mu|^2$ leading-order structural form (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3).

Verdict: **M3**.

---

**End Paper EDSC-AcousticCurvature.**
