# Paper RQM-T9 — Primitive-Level UV Finiteness

**Series:** Wave-3 Relativistic-QM Bridge — Theorem T9
**Status:** Wave-3 generative paper; M3 verdict at write-time
**Companions:** Paper_089 (V1), Paper_090 (V5), Paper_040 (Trans-Planckian via V5 cutoff), Paper_013 (V1 QFT-arc form), Paper_RQM_T5 (KG), Paper_RQM_T4 (Dirac).

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived.** They are postulated per Paper_087.
2. **No claim that substrate UV-finiteness is forced from nothing.** The result is conditional on P04 + P08 + Paper_013 + Paper_040 + Paper_089 + Paper_090 + standard QFT machinery.
3. **No claim of numerical-content derivation beyond what is explicitly INHERITED.** The cutoff scale $\omega_c = c/\ell_P$ is INHERITED via Planck-scale matching.
4. **No claim that the §3.5 power-counting derivation is closed at substrate level.** §3.5 invokes Paper_040 V5-cutoff and standard QFT power-counting machinery (inherited); the substrate-level derivation chain is OPEN.
5. **No claim that ED is the only consistent substrate ontology.** Other substrate ontologies are conceivable.
6. **No claim of empirical adequacy for asymptotic freedom / triviality.** Substrate-level audit of these is currently open.
7. **No claim that the substrate-cutoff reframing of renormalization is itself a derivation.** §3.4 + audit rows 9 + 10 are framework-positioning claims, not derivations.

---

## Abstract

Paper RQM-T9 establishes substrate-level UV finiteness in ED-QFT as a form-IDENTIFIED structural consequence of P04 (bandwidth-additive primitive) + P08 (substrate scale $\ell_{\mathrm{ED}}$), composed with V1 (Paper_089) + V5 (Paper_090) finite-bandwidth kernel content and Paper_040 V5-UV-cutoff. The substrate-level mechanism: each substrate cell carries finite bandwidth budget; the maximum momentum scale is $|k| \sim 1/\ell_P$ via P08; V1 form-factor decay + V5 cutoff $\omega_c = c/\ell_P$ supply intrinsic UV regulators. All standard-QFT UV divergences are coarse-graining artifacts of $\ell_P \to 0$. The structural form is form-IDENTIFIED; the cutoff value $\omega_c = c/\ell_P$ is VALUE-INHERITED. The reframing of renormalization as substrate-cutoff-absorption is a framework-positioning claim, not a derivation. §3.5 substrate-graph → power-counting derivation is OPEN. Verdict tier: **M3** per Paper_095. The result joins the Wave-3 Relativistic-QM Bridge family as foundational for the QFT-arc: T4, T5, T6 substrate-level loop integrals all inherit UV finiteness from this paper. This paper is in the substrate-ontology research-program lineage of 't Hooft, Wolfram, and the causal-set program — not in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §1 Statement of Result

**Claim.** Substrate-level QFT in ED is **UV-finite at the primitive level**: there are no ultraviolet divergences in substrate-level loop integrals, because the substrate's bandwidth primitive (P04) + substrate scale (P08) impose a natural cutoff at $\omega_c \sim c/\ell_P$ (P-V5-UV-Cutoff, Paper_040). All standard-QFT UV divergences are coarse-graining artifacts of taking $\ell_P \to 0$ — i.e., of removing the substrate UV regulator after the fact. At substrate level, no regularization is needed.

form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) by P04 + P08 + V1/V5 finite-bandwidth structure. The substrate cutoff value $\omega_c = c/\ell_P$ is INHERITED via Planck-scale matching.

Verdict: **M3**. No new postulates.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P04 (Bandwidth)** — non-negative additive scalar; supplies finite per-cell budget that caps mode content.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — Planck-length anchor; supplies UV cutoff scale.
- **P10 (Rule-type primitive)** — V1 and V5 kernels as substrate primitives.

### 2.2 Upstream Dependencies

- **I-013:** V1 QFT-arc form, Källén-Lehmann spectral representation with finite spectral density.
- **I-040:** Trans-Planckian resolution via V5 cutoff $\omega_c = c/\ell_P$.
- **I-089:** V1 finite-width retarded kernel with finite second moment.
- **I-090:** V5 cross-chain correlation kernel with finite bandwidth.
- **I-Cutoff:** Standard QFT UV-cutoff machinery (lattice, Pauli-Villars, dimensional regularization).

---

## §3 Derivation

### 3.1 Standard QFT UV divergences

In standard QFT, loop integrals such as
$$\int \frac{d^4k}{(2\pi)^4} \frac{1}{k^2 + m^2}$$
diverge as $k \to \infty$ (UV divergence). Regularization schemes (Pauli-Villars, dimensional, lattice) introduce a cutoff $\Lambda$ to render integrals finite; renormalization absorbs the cutoff-dependence into redefined coupling constants.

The standard view: the cutoff $\Lambda$ is a **regularization tool**, eventually taken to $\Lambda \to \infty$. Divergences are interpreted as artifacts of treating the field theory at all scales.

### 3.2 Substrate cutoff: P04 + P08

The ED substrate is intrinsically regulated by two primitive constraints:

**P04 bandwidth:** Each substrate cell carries finite bandwidth budget. At the substrate level, the **mode content** of any region is bounded: the substrate cannot support arbitrarily-high-frequency modes within a finite spatial region.

**P08 substrate scale $\ell_{\mathrm{ED}}$:** The Planck-length anchor sets the minimum-distance scale at substrate level. Substrate structure does not exist below $\ell_P$ (per Paper_042 substrate-interior cutoff). The maximum momentum scale is therefore $|k| \sim 1/\ell_P$.

Combined: substrate-level loop integrals are bounded by
$$\int^{|k| \lesssim 1/\ell_P} \frac{d^4k}{(2\pi)^4} \frac{1}{k^2 + m^2} < \infty .$$

The integral is **automatically UV-finite** because the integration domain is bounded by the substrate cutoff.

### 3.3 V1 + V5 kernel finite-bandwidth structure

The substrate-level V1 kernel (Paper_089) has finite second moment $\ell_{V1}^2 < \infty$. Its momentum-space form factor $\hat{K}_{V1}(p)$ decays for $|p|\ell_{V1} \gtrsim 1$ (Paper_013 QFT-arc form, P-V1-FormFactor). This decay supplies an intrinsic UV regulator at the V1-kernel level.

The V5 kernel (Paper_090) has finite bandwidth $\ell_{V5}$ and finite UV cutoff $\omega_c = c/\ell_P$ (Paper_040 P-V5-UV-Cutoff). Cross-chain correlations above $\omega_c$ are not substrate-supported.

Together, V1 + V5 finite-bandwidth structure ensures that **all substrate-level loop integrals have natural UV cutoffs** built in. The cutoffs are not introduced ad hoc; they are inherent properties of the substrate kernel rule-types.

### 3.4 Why standard QFT looks UV-divergent

Standard QFT extracts effective continuum dynamics from the substrate via DCGT coarse-graining (Paper_073). The coarse-graining takes $\ell_P \to 0$ implicitly: it treats the continuum as resolving structure at all scales.

In this limit, the substrate's intrinsic UV cutoff $\omega_c = c/\ell_P$ is removed. Loop integrals then diverge as $\Lambda = \omega_c \to \infty$. The standard-QFT "UV divergence" is the **coarse-graining artifact** of removing the substrate regulator.

Renormalization, in this framing, is the procedure that reconstructs continuum predictions while accounting for the absorbed cutoff. The "infinity" of bare quantities is the divergence of $\omega_c$ in the coarse-graining limit, not a true infinity at substrate level.

### 3.5 Substrate-level computation: example

Consider the substrate-level analog of the standard one-loop vacuum bubble:
$$I_{\mathrm{sub}} = \int \frac{d^4k}{(2\pi)^4} \frac{|\hat{K}_{V1}(k)|^2}{k^2 + m^2} ,$$
where $\hat{K}_{V1}(k)$ is the V1 form factor with $\hat{K}_{V1}(k) \to 0$ for $|k|\ell_{V1} \gg 1$.

The form factor enforces the UV regulator: the integrand decays rapidly at large $|k|$. $I_{\mathrm{sub}}$ is **finite** without any external cutoff — purely from the substrate kernel structure.

This is the substrate-level meaning of UV finiteness: every loop integral, when written with the substrate's actual kernel content rather than the bare propagator, is finite.

### 3.6 Connection to trans-Planckian resolution (Paper_040)

Paper_040 establishes the V5 cutoff $\omega_c = c/\ell_P$ as the substrate-level mode-content limit. This is the same cutoff that resolves the trans-Planckian problem in Hawking radiation (Paper_040 §3).

T9 (this paper) generalizes that result: **all substrate-level QFT computations** inherit the V5 UV cutoff, not only Hawking-radiation calculations. The trans-Planckian problem and the standard QFT UV divergences are both manifestations of taking $\omega_c \to \infty$ in the coarse-graining limit.

### 3.7 Numerical content

The cutoff scale $\omega_c = c/\ell_P \approx 10^{43}$ Hz is INHERITED from the Planck-length value. The substrate framework supplies the **form** of the cutoff (it exists, it is intrinsic to V5, it equals $c/\ell_P$); the numerical value comes via $\ell_P$ matching.

Specific renormalization-group calculations and effective field theory matching are inherited from standard QFT. The substrate framework's contribution is the conceptual reframing: **divergences are coarse-graining artifacts, not fundamental infinities**.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P04 bandwidth-additive | P | Primitive. |
| 2 | P08 substrate scale $\ell_{\mathrm{ED}}$ | P | Primitive. |
| 3 | P10 rule-type (supplies V1, V5) | P | Primitive. |
| 4 | V1 finite second moment $\ell_{V1}^2$ | I | Paper_089. |
| 5 | V1 form factor decay $\hat{K}_{V1}(p)$ at high $|p|$ | I | Paper_013 (P-V1-FormFactor). |
| 6 | V5 UV cutoff $\omega_c = c/\ell_P$ | I | Paper_040 (P-V5-UV-Cutoff). |
| 7 | Substrate cutoff scale exists at $|k| \sim 1/\ell_P$ | D-via-I | P04 + P08 + I-040. |
| 8 | Substrate-level reframing of UV finiteness as inherent substrate-cutoff content | A→position | Framing-claim verdict row (per Paper_095 §3.3): framework-positioning reframing, not derivation; cutoff scale inherited from Paper_040. |
| 9 | Standard QFT divergences = coarse-graining artifacts of $\omega_c \to \infty$ | A→position | Framing-claim verdict row (per Paper_095 §3.3): framework-positioning / reframing claim (not a derivation step). |
| 10 | Renormalization as substrate-cutoff-absorption procedure | A→position | Framing-claim verdict row (per Paper_095 §3.3): framework-positioning / reframing claim. |
| 11 | Trans-Planckian problem (Paper_040) is the same phenomenon | I | Paper_040. |
| 12 | Numerical cutoff $\omega_c = c/\ell_P \approx 10^{43}$ Hz | I | Empirical Planck-scale matching. |
| 13 | Substrate-graph → continuum power-counting explicit derivation | OPEN | §3.5 invokes Paper_040 V5-cutoff and standard QFT power-counting machinery (inherited) but the substrate-level derivation chain is not closed in this paper. |

---

## §5 Falsification Criteria

- **F1: This falsifier is structural rather than empirical** — refutation would require substrate-level inconsistency proof rather than experimental measurement: substrate-level evidence that V1 second moment is divergent under any admissible substrate variation. Empirical companion: discovery that QFT predictions diverge at $\omega \sim c/\ell_P$ rather than being naturally cut off would constitute empirical pressure.

- **F2: Substrate evidence that V5 admits modes above $\omega_c = c/\ell_P$.** Would refute step 6 (and Paper_040 falsifier propagates).

- **F3: Empirical detection of substrate-level QFT loop integral divergence in a regime where standard renormalization is not applied.** Would refute the substrate-finite claim.

- **F4: This falsifier is structural rather than empirical** — refutation would require substrate-level inconsistency proof: substrate-level computation showing the V1 form factor does NOT decay at high $|p|$ would refute step 5 (and Paper_013 falsifier propagates).

---

## §6 Position Statement

Paper RQM-T9 establishes substrate-level UV finiteness as **M3** (form-IDENTIFIED structural finiteness + VALUE-INHERITED cutoff scale) under P04 + P08 + V1/V5 finite-bandwidth structure with no new postulates. The substrate-level UV-cutoff is form-IDENTIFIED; the value $\omega_c = c/\ell_P$ is INHERITED via Planck-scale matching. The reframing of standard-QFT UV divergences as coarse-graining artifacts is a framework-positioning claim, not a derivation. The §3.5 substrate-graph → power-counting derivation is OPEN. The result joins the Wave-3 Relativistic-QM Bridge family as the QFT-finiteness foundation: T4, T5, T6 substrate-level loop integrals inherit UV finiteness from this paper.

This paper does NOT derive $\ell_P$'s numerical value, does NOT close the substrate-graph → power-counting derivation (OPEN), and does NOT extend to substrate-level audit of asymptotic freedom / triviality (deferred).

This paper is in the Wave-3 Relativistic-QM Bridge series of the Event Density program — a substrate-ontology research program in the lineage of 't Hooft's cellular-automaton interpretation, Wolfram's Ruliad, and the causal-set program (Sorkin et al.); NOT in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §7 Rewrite Note

This paper supplies the substrate-level **UV finiteness** claim that is foundational for the entire QFT-arc of the ED corpus. Form form-IDENTIFIED; numerical $\omega_c$ INHERITED.

**Relationship to other RQM-bridge papers:**
- **T5 KG + T4 Dirac:** field equations whose substrate-level loop integrals are UV-finite per this paper.
- **T6 minimal coupling:** interaction terms; substrate-level interaction-loop integrals also UV-finite.
- **T7 Lorentz reps:** rule-type-specific UV structure preserved across reps.

**Cross-corpus impact:** The conceptual reframing — "divergences are coarse-graining artifacts" — is one of the ED program's substantive contributions to QFT foundations. Standard renormalization-group machinery remains operationally correct; the substrate framework supplies the **origin** of the cutoff scale that standard QFT introduces ad hoc.

**Numerical content INHERITED.** $\omega_c = c/\ell_P$ via $\ell_P$ matching. **Form IDENTIFIED** (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3)**.** Substrate-level UV finiteness as structural consequence of P04 + P08 + V1/V5 finite-bandwidth.

**Future work.** Quantitative comparison of substrate-level QFT predictions vs standard-renormalized predictions for specific observables; substrate-level audit of asymptotic freedom and triviality (currently open).

Verdict: **M3**.

---

**End Paper RQM-T9.**
