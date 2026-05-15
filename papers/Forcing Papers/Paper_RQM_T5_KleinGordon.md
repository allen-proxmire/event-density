# Paper RQM-T5 — Klein–Gordon $(\square + m^2c^2/\hbar^2)\Psi = 0$ (Arc-R Stage R.1)

**Series:** Wave-3 Relativistic-QM Bridge — Theorem T5
**Status:** Wave-3 generative paper; M3 verdict at write-time. FORM-INHERITED conditional on Paper_017 + Paper_095 §2.3 (standard-form construction).
**Companions:** Paper_RQM_T4 (Dirac), Paper_RQM_T6 (minimal-coupling KG), Paper_RQM_T7 (Lorentz reps), Arc-R Stage R.1.

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 primitives are not derived.** They are postulated per Paper_087.
2. **No claim that the Klein–Gordon equation form is derived in this paper.** Per Paper_095 §2.3, writing down the Klein–Gordon equation is P (definitional standard-form construction), not D. The KG form is INHERITED from Paper_017 acoustic-metric Lorentz covariantization + standard relativistic dispersion.
3. **No claim of numerical-content derivation beyond what is explicitly INHERITED.** Specific scalar-particle masses (Higgs, pion, etc.) are INHERITED via empirical matching.
4. **No claim that ED is the only consistent substrate ontology.** Other substrate ontologies are conceivable.
5. **No claim of empirical adequacy outside the regime stated in §2.2.** KG on curved acoustic metric, KG with self-interaction $\lambda\Psi^4$, dimensional reductions are deferred / OPEN.
6. **No claim that V1 kernel produces KG-propagator structure via closed substrate-graph derivation.** The §3.4 V1 substrate-origin is asserted via Paper_013 + Paper_089 spectral inheritance, not closed at the substrate-graph level here.

---

## Abstract

Paper RQM-T5 identifies the Klein–Gordon equation $(\square + m^2c^2/\hbar^2)\Psi = 0$ as the standard-form scalar QFT carrier for scalar (spin-0) rule-types in $D = 3+1$. **The KG equation form is INHERITED**, not derived in this paper: per Paper_095 §2.3, writing down the Klein–Gordon equation is P (definitional standard-form construction). The substrate-level content of this paper is twofold: (i) identification of the mass parameter $m$ as substrate-bandwidth content (P04) at zero spatial momentum; (ii) compatibility check that V1-retardation kernel content (Paper_089) is consistent with KG-propagator structure in the low-momentum limit (Paper_013 inheritance). The structural form is FORM-INHERITED conditional on Paper_017 acoustic-metric Lorentz covariantization + Paper_095 §2.3 standard-form construction; mass parameter $m$ is VALUE-INHERITED via empirical matching. Verdict tier: **M3** with honest framing that the form is INHERITED, not D-via-I'd. The result closes Arc-R Stage R.1 and joins the Wave-3 Relativistic-QM Bridge family alongside T4 (Dirac for spinor rule-types), T6 (minimally-coupled KG), and T7 (Lorentz representations). This paper is in the substrate-ontology research-program lineage of 't Hooft, Wolfram, and the causal-set program — not in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §1 Statement of Result

**Claim.** Scalar rule-types (intrinsic-rotation $s = 0$) in $D = 3+1$ propagate according to the Klein–Gordon equation
$$(\square + m^2c^2/\hbar^2)\Psi = 0 ,$$
where $\square = \partial^\mu\partial_\mu$ is the d'Alembertian on the acoustic-metric background (Paper_017) and $m$ is the rule-type's mass parameter (INHERITED). The structural form — second-order, Lorentz-covariant, dispersion relation $E^2 = p^2c^2 + m^2c^4$ — is **FORM-INHERITED** from Paper_017 + standard relativistic dispersion (per Paper_095 §2.3, writing down the Klein–Gordon equation is P-definitional, not D). This paper's substrate-level contribution is the identification of the mass parameter as substrate-bandwidth content and the V1-retardation-inheritance compatibility check.

This paper closes Arc-R Stage R.1.

Verdict: **M3**. No new postulates.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P04 (Bandwidth)** — supplies substrate bandwidth budget entering the dispersion relation.
- **P06 (Spatial dimension $D = 3+1$)** — supplies four-gradient $\partial_\mu$ and d'Alembertian.
- **P10 (Rule-type primitive)** — scalar rule-type carrier.
- **P13 (Time homogeneity)** — supplies time-translation symmetry on which dispersion is defined.

### 2.2 Upstream Dependencies

- **I-087:** 13-primitive position paper.
- **I-017:** Substrate→continuum Lorentz covariantization (Paper_017).
- **I-089:** V1 finite-width retarded kernel (Paper_089).
- **I-073:** DCGT (Paper_073).
- **I-KG:** Standard Klein–Gordon machinery (standard physics).
- **I-Disp:** Standard relativistic dispersion relation $E^2 = p^2c^2 + m^2c^4$.

---

## §3 Derivation

### 3.1 Scalar rule-type structure

By the rule-type taxonomy (Paper_RQM_T7 + Arc-R Stage R.2), scalar rule-types carry one-component participation amplitudes $\Psi(x)$ with $s = 0$. Their substrate-level evolution is governed by V1 kernel propagation (Paper_089) on the acoustic-metric background (Paper_017).

### 3.2 Relativistic dispersion from P06 + P04

The substrate-level Lorentz covariantization (Paper_017) provides the four-gradient $\partial_\mu$ and the d'Alembertian $\square = \partial^\mu\partial_\mu$ at the substrate scale. By P06 ($D = 3+1$), the d'Alembertian has Lorentzian signature $(+,-,-,-)$.

The substrate dispersion relation for a scalar amplitude with mass parameter $m$ is the relativistic invariant:
$$E^2 = p^2 c^2 + m^2 c^4 ,$$
or equivalently
$$p^\mu p_\mu = m^2 c^2 .$$

The mass parameter $m$ characterizes the substrate-bandwidth content (P04) at zero spatial momentum: $E_{rest} = mc^2$ supplies the rest-energy bandwidth.

Standard QM-correspondence: $p_\mu \to -i\hbar \partial_\mu$. Applied to $\Psi$:
$$(-i\hbar\partial^\mu)(-i\hbar\partial_\mu)\Psi = m^2 c^2 \Psi$$
$$-\hbar^2 \square \Psi = m^2 c^2 \Psi$$
$$(\square + m^2 c^2/\hbar^2)\Psi = 0 .$$

This is the Klein–Gordon equation. The derivation rests on standard relativistic dispersion + P06 four-gradient structure + substrate Lorentz covariance.

### 3.3 Why Klein–Gordon, not Schrödinger

The non-relativistic Schrödinger equation (Paper 006 in the canonical numbering — "Unitary evolution form from V1 kernel propagation") is the **low-velocity limit** of substrate-level propagation. The relativistic generalization for scalar rule-types is Klein–Gordon, not Schrödinger.

The two are related by the substitution $E \to E_{kin} + mc^2$ in the dispersion relation and expansion in $v/c$. At leading order, KG reduces to Schrödinger with $E_{kin} = p^2/(2m)$.

The substrate-level structure is the **same** in both limits: V1 finite-width retarded propagation on the acoustic-metric background. The dispersion-relation form changes (relativistic vs non-relativistic), but the substrate kernel is unchanged.

### 3.4 Substrate-V1 origin of KG

Under V1 kernel propagation (Paper_089) at substrate level, the scalar amplitude $\Psi(x)$ propagates as
$$\Psi(x) = \int K_{V1}(x - y) \Psi(y) \, d^4y$$
in flat acoustic background. The kernel $K_{V1}$ has Fourier transform $\hat{K}_{V1}(p)$ that, at low momentum $|p|\ell_{V1} \ll 1$, takes the form (per Paper_013 QFT-arc V1 spectral content):
$$\hat{K}_{V1}(p) \propto \frac{1}{p^2 - m^2 c^2 / \hbar^2 + i\epsilon} ,$$
the standard relativistic propagator pole.

This Fourier-space form is the Klein–Gordon propagator: amplitudes satisfying $(\square + m^2c^2/\hbar^2)\Psi = 0$ are precisely the on-shell substrate excitations.

The substrate-level identification: KG is the equation of motion for free-scalar substrate excitations under V1 kernel propagation.

### 3.5 Lorentz covariance

The KG equation is manifestly Lorentz-covariant because:
- $\square$ is a Lorentz scalar.
- $m$ is a Lorentz scalar (a rule-type-specific invariant).
- $\Psi$ transforms as a scalar field under Lorentz transformations (the defining property of "scalar rule-type").

Substrate Lorentz covariantization (Paper_017) supplies the acoustic-metric background on which KG is defined. The covariance is inherited.

### 3.6 Mass parameter inheritance

The mass parameter $m$ is INHERITED via empirical matching:
- Higgs scalar: $m_H \approx 125$ GeV.
- Pion: $m_\pi \approx 135$ MeV.
- Hypothetical scalar dark-matter candidates: per-model inheritance.

The substrate framework does not derive specific $m$ values from first principles. Arc M H1-dominant supplies the **structural form** of mass (Lorentz-scalar, dimensional-anchored, statistics-class-mechanism); specific values inherited.

### 3.7 Arc-R Stage R.1 connection

Arc-R Stage R.1 (relativistic scalar equations) covers the substrate-level construction of relativistic scalar equations from rule-type structure + Lorentz covariance. This paper supplies the Klein–Gordon equation as the canonical Stage R.1 result.

The full Arc-R sequence:
- **R.1:** Klein–Gordon (this paper).
- **R.2:** Spinor taxonomy (T1+T2+T3).
- **R.3:** Dirac equation (T4).
- **R.4:** Vector/tensor equations (future).

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P06 $D = 3+1$ | P | Primitive. |
| 2 | P04 bandwidth | P | Primitive. |
| 3 | P10 scalar rule-type | P | Primitive. |
| 4 | Substrate Lorentz covariantization → acoustic metric | I | Paper_017. |
| 5 | Four-gradient $\partial_\mu$, d'Alembertian $\square$ | I | Standard math + I-017. |
| 6 | Relativistic dispersion $E^2 = p^2c^2 + m^2c^4$ | I | Standard physics (I-Disp). |
| 7 | QM-correspondence $p_\mu \to -i\hbar\partial_\mu$ | I | Standard QM. |
| 8 | KG equation $(\square + m^2c^2/\hbar^2)\Psi = 0$ | P | Standard-form construction per Paper_095 §2.3 (writing down the Klein–Gordon equation is P, not D). |
| 9 | KG as low-momentum V1-kernel propagator pole | P | Standard-form construction per Paper_095 §2.3 (the propagator-pole form is inherited / definitional, not substrate-derived here). |
| 10 | Lorentz covariance of KG | I | Standard math (each constituent is Lorentz-covariant). |
| 11 | Mass parameter $m$ | I | Empirical matching. |
| 12 | Specific scalar-particle masses | I | Empirical. |
| 13 | Schrödinger as low-velocity limit | I | Standard QM. |
| 14 | KG as Arc-R Stage R.1 canonical result | A→position | Framing-claim verdict row (per Paper_095 §3.3): position-statement classification of the result within the Arc-R program, not derivation. |

---

## §5 Falsification Criteria

- **F1: Empirical detection of scalar particle NOT obeying KG dispersion** in regimes where standard QFT predicts KG. Would refute the substrate-KG identification.

- **F2: Substrate evidence that V1 kernel's low-momentum Fourier behavior is NOT the KG propagator pole.** Would refute §3.4 substrate-V1 connection.

- **F3: Substrate-level evidence that scalar rule-type evolution is governed by a higher-order PDE in the relativistic limit.** Would refute step 8.

- **F4: Substrate Lorentz covariantization (Paper_017) shown to fail in scalar sector.** Propagates from upstream.

---

## §6 Position Statement

Paper RQM-T5 establishes the Klein–Gordon equation as **M3** with the honest framing that the KG equation form is **INHERITED** from Paper_017 acoustic-metric Lorentz covariantization + standard relativistic dispersion + Paper_095 §2.3 (standard-form construction is P-definitional, not D). The substrate-level contribution of this paper is **not** the derivation of the KG form, but: (i) substrate-level identification of mass parameter $m$ as the rest-frame substrate-bandwidth content (P04); (ii) V1-retardation-inheritance compatibility check confirming that V1 kernel low-momentum Fourier structure (Paper_013 + Paper_089) is consistent with KG-propagator pole. Specific scalar-particle masses are VALUE-INHERITED via empirical matching. No new postulates.

This paper does NOT derive the KG equation form from substrate primitives — the form is INHERITED. It does NOT close the substrate-graph V1 → KG-propagator derivation at the closed-proof level (compatibility-check level only). It does NOT extend to curved-acoustic-metric KG, self-interaction $\lambda\Psi^4$, or dimensional reductions (deferred).

The result joins the Wave-3 Relativistic-QM Bridge family as Arc-R Stage R.1, complementary to T4 (first-order Dirac for spinor rule-types), extended by T6 (minimally-coupled KG), and classified via T7 (Lorentz reps).

This paper is in the Wave-3 Relativistic-QM Bridge series of the Event Density program — a substrate-ontology research program in the lineage of 't Hooft's cellular-automaton interpretation, Wolfram's Ruliad, and the causal-set program (Sorkin et al.); NOT in the operational-reconstruction lineage of Hardy / CDP / Coecke-Kissinger.

---

## §7 Rewrite Note

This paper closes Arc-R Stage R.1 with the substrate-level KG derivation. Form FORM-INHERITED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3); mass values INHERITED.

**Relationship to other RQM-bridge papers:**
- **T4 Dirac:** Dirac operator factorizes KG; spinor rule-types satisfy Dirac, which implies KG.
- **T6 minimal-coupling KG:** extends KG to interaction with gauge fields.
- **T7 Lorentz reps:** classifies scalar rule-type Lorentz representation; this paper gives its equation.

**Numerical content INHERITED.** Mass parameters per scalar particle. **Form INHERITED.** KG structural form for scalar rule-types in $D = 3+1$ (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3).

**Future work.** KG extensions: KG on curved acoustic metric (companion to GR1 / Paper_014); KG with self-interaction $\lambda\Psi^4$ (substrate-derivation OPEN); KG in dimensional reductions (effective 2D scalar fields).

Verdict: **M3**.

---

**End Paper RQM-T5.**
