# Paper Metamaterials — Photonic Bandgap, Negative-Index, Cloaking from Substrate via Two-Scale Expansion

**Series:** Wave-3 Condensed-Matter / Photonics Extension
**Status:** Wave-3 generative paper; **M2 (Intermediate Path C)** verdict (substrate identification + standard-machinery composition; no D rows in audit; specific metamaterial designs INHERITED)
**Companions:** Paper_017 (acoustic metric), Paper_073 (DCGT), Paper_011 (Bloch theorem), Paper_EDSC_AcousticMetric_CurvatureConcentration, Paper_089 (V1), Paper_090 (V5).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the metamaterial-phenomenon classes (photonic bandgap / negative-index / cloaking) from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates + INHERITED two-scale homogenization machinery.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim derivation of the two-scale homogenization machinery — that is INHERITED from Bensoussan-Lions-Papanicolaou (1978). ED's contribution is supplying V1/V5 kernel content into the standard homogenization framework, plus Paper_017 acoustic-metric identification for cloaking.
5. **INHERITED vs FORCED breakdown:** ED supplies V1/V5 kernel content into standard homogenization. Verdict **M2** reflects identification + composition (no D rows in audit); specific metamaterial designs INHERITED via engineering.

---

## Abstract

This paper supplies the substrate-level account of three metamaterial-phenomenon classes — photonic bandgap, negative refractive index, and electromagnetic cloaking — via two-scale expansion of the substrate framework. The two-scale homogenization machinery is **INHERITED** from Bensoussan-Lions-Papanicolaou (1978); ED's contribution is identification + composition: feeding V1 (Paper_089) and V5 (Paper_090) kernel content into standard homogenization, Bloch theorem (Paper_011) for bandgap, and acoustic-metric (Paper_017) for transformation-optics cloaking. The audit contains no D rows; per Paper_095 form-FORCED / value-INHERITED methodology, verdict is **M2 (Intermediate Path C)**. Specific metamaterial designs (split-ring resonators, photonic-crystal lattices, transformation-optics cloaks) are INHERITED via standard engineering. Key falsifier **F1:** substrate evidence that V1 + V5 do NOT produce effective-medium tensors consistent with metamaterial designs.

---

## §1 Statement of Result

**ED is compatible with the two-scale expansion framework.** Two-scale homogenization machinery is INHERITED from Bensoussan-Lions-Papanicolaou (1978); ED's contribution is supplying V1/V5 kernel content into standard homogenization, which is identification+composition (M2), not forcing.

**Claim.** Three classes of metamaterial phenomena — (i) **photonic bandgap** in periodic photonic structures, (ii) **negative refractive index** in resonant metamaterials, (iii) **electromagnetic cloaking** via transformation-optics — are described in ED via a **two-scale expansion** of the substrate framework, with V1/V5 kernel content supplied into the inherited homogenization machinery:

- **Microscale:** Substrate participation field with periodic / resonant / coordinate-deformed microstructure.
- **Macroscale:** Coarse-grained effective-medium description via DCGT (Paper_073).

The two-scale expansion forces:
- Photonic bandgap structure from periodic substrate microstructure + Bloch theorem (Paper_011).
- Negative-index from V1 / V5 effective-medium tensor structure (resonant frequency regime).
- Cloaking from substrate-level coordinate deformation translating to coordinate-transformed acoustic metric.

The structural identification is via inherited two-scale homogenization (Bensoussan-Lions-Papanicolaou 1978) with substrate V1/V5 inputs. Specific metamaterial-design parameters INHERITED.

Verdict: **M2 (Intermediate Path C)**.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P03 (Channel + locus indexing; spatial homogeneity)** — supplies the substrate locus structure on which microscale periodicity / deformation acts.
- **P05 (Polarity-transport)** — supplies substrate-level transport that metamaterials manipulate.
- **P09 ($U(1)$-valued polarity)** — photonic polarity content.
- **P10 (Rule-type primitive)** — V1, V5 kernels supplying substrate dispersion.

### 2.2 Upstream Dependencies

- **I-011:** Bloch theorem from substrate translation symmetry.
- **I-017:** Substrate→continuum Lorentz covariantization (acoustic metric).
- **I-073:** DCGT coarse-graining.
- **I-089:** V1 finite-width retarded kernel.
- **I-090:** V5 cross-chain correlation kernel.
- **I-EDSC-AcousticCurvature:** Acoustic-metric curvature on mobility-gradient scale.
- **I-Homog:** Standard homogenization theory.
- **I-TO:** Standard transformation-optics machinery (Pendry, Leonhardt).
- **I-Effective:** Standard effective-medium theory.

---

## §3 Derivation

### 3.1 Two-scale expansion at substrate level

A **two-scale expansion** treats the substrate field $\Psi(x)$ as a function of two coordinates: a **macroscopic** coordinate $x$ (slowly varying) and a **microscopic** coordinate $y = x/\epsilon$ (rapidly varying, dimensionless), with $\epsilon$ the ratio of microstructure-scale to macrostructure-scale.

The substrate-level Maxwell-class equations (V1 + V5 modulated, coarse-grained per Paper_073) become, under two-scale expansion:
$$\Psi(x) \;=\; \Psi_0(x, y) + \epsilon \Psi_1(x, y) + \epsilon^2 \Psi_2(x, y) + O(\epsilon^3) ,$$
with each $\Psi_n$ a function of both scales. Microscale equations determine the periodic / resonant / deformed microstructure; macroscale equations describe the effective-medium response.

This is standard homogenization theory (I-Homog) applied at substrate level. The substrate framework provides the **substrate-level kernel content** (V1 + V5) that enters the homogenization machinery.

### 3.2 Photonic bandgap from periodic substrate microstructure

**Setup:** Substrate microstructure is periodic with period $a$ in some direction. By Paper_011 (Bloch theorem), photonic excitations on this periodic substrate form Bloch bands.

**Bandgap mechanism:** For appropriate periodic dielectric structures, certain frequency ranges are **forbidden** — Bloch states do not exist at these frequencies. The forbidden ranges are **photonic bandgaps**.

Substrate-level origin: V1 kernel propagation modulated by periodic substrate-mobility content (V5-modulated $\mu(x)$ with period $a$) produces an effective dispersion relation $\omega(k)$ with gaps at specific Bloch-wavevector values. The bandgap structure is form-IDENTIFIED by Bloch theorem + periodic substrate kernel content.

**Inherited content:** Specific bandgap widths, central frequencies, and band-edge dispersion per metamaterial design.

### 3.3 Negative refractive index from resonant V1/V5 effective-medium

**Setup:** Substrate microstructure includes resonant elements (e.g., split-ring resonators, dielectric resonators) that produce strong frequency-dependent permittivity $\epsilon(\omega)$ and permeability $\mu(\omega)$.

**Negative-index mechanism:** When both $\epsilon(\omega) < 0$ and $\mu(\omega) < 0$ in some frequency range, the refractive index $n = \sqrt{\epsilon\mu}$ is negative (with the appropriate branch choice). Wave propagation in such media exhibits anomalous behavior: phase velocity opposite group velocity, reverse Snell's law, etc.

Substrate-level origin: V1 + V5 effective-medium tensors derived from substrate microstructure via two-scale homogenization. The substrate-level dispersion structure produces the frequency-dependent $\epsilon, \mu$; resonance at specific frequencies (from microstructure resonant geometry) produces sign changes; combined-sign-flip regime yields negative index.

The form-IDENTIFIED structural content: existence of frequency ranges with $\mathrm{Re}[n] < 0$ when both effective tensors are negative. Specific resonance frequencies and bandwidths INHERITED.

### 3.4 Cloaking from substrate-level coordinate deformation

**Setup:** Standard transformation-optics theory (I-TO; Pendry 2006, Leonhardt 2006): an electromagnetic cloak is constructed by designing a medium whose effective dielectric tensors $\epsilon^{ij}, \mu^{ij}$ correspond to a coordinate transformation $x \to x'(x)$ that maps a finite region (the cloaked object) to a point.

Substrate-level account: by Paper_017 (substrate→continuum Lorentz covariantization), the acoustic metric encodes the kinematic frame for photonic propagation. A coordinate transformation $x \to x'(x)$ at substrate level corresponds to a transformed acoustic metric $g^{\mathrm{ac}}_{\mu\nu}(x')$. Photonic propagation in the cloaked region follows the transformed acoustic-metric geodesics; the cloak design is the substrate-level coordinate transformation translated into engineered $\epsilon, \mu$ tensors.

The form-IDENTIFIED content: coordinate-deformation cloaking is structurally implementable in any substrate framework supporting an acoustic metric. Specific cloak designs (annular cylindrical cloaks, carpet cloaks, etc.) are inherited.

**Limitations:** Cloaking is approximate; frequency-dispersion of the resonant elements + causality (Kramers-Kronig) constraints prevent perfect broadband cloaking. These limitations are inherited from standard transformation-optics analysis.

### 3.5 SCBU-boundary connection for cloaking

Cloaking via transformation-optics constructs a substrate-level "region of vanishing observable presence" — the cloaked region appears to have zero substrate-coupling to external photonic probes. This is structurally analogous to the SCBU boundary (Paper_ED_SC_4.1): a region where substrate cross-chain coupling vanishes.

The analogy is **structural-positive** (A→analogy), not derivational: cloaking achieves locally what the SCBU boundary achieves globally (decoupling of an interior region from exterior probes). The substrate framework supplies a unified vocabulary for both phenomena.

### 3.6 Combined metamaterial sector

Combining §3.2–§3.5, the substrate framework supplies a unified two-scale-expansion account of:
- **Photonic bandgap:** periodic substrate microstructure + Bloch theorem.
- **Negative index:** resonant V1 / V5 effective-medium tensors.
- **Cloaking:** substrate-level coordinate deformation + transformation-optics.

All three are form-IDENTIFIED at the structural level via two-scale expansion of substrate kernel content. Specific metamaterial designs INHERITED.

### 3.7 Numerical content

**form-IDENTIFIED:**
- Two-scale expansion structure.
- Bandgap existence from periodic substrate microstructure.
- Negative-index existence in dual-negative-tensor regimes.
- Cloaking implementability via coordinate-deformation.

**INHERITED:**
- Specific bandgap frequencies, widths, central values.
- Specific resonance frequencies and bandwidths.
- Specific cloak designs.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P03, P05, P09, P10 primitives | P | Primitives. |
| 2 | Substrate Maxwell-class equations from V1 + V5 + DCGT | I | Standard substrate-EM machinery. |
| 3 | Two-scale expansion machinery | I | Standard math (I-Homog). |
| 4 | Bloch theorem on periodic substrate | I | Paper_011. |
| 5 | Photonic bandgap from periodic microstructure | D-via-I | Standard photonic-crystal theory + substrate. |
| 6 | Effective-medium $\epsilon(\omega), \mu(\omega)$ from V1 + V5 | I | Standard effective-medium theory. |
| 7 | Negative-index in dual-negative regime | D-via-I | Standard math + substrate. |
| 8 | Acoustic metric encodes photonic kinematic frame | I | Paper_017. |
| 9 | Coordinate-deformation transformation-optics | I | Standard math (I-TO). |
| 10 | Cloaking via substrate-level coordinate deformation | D-via-I | Composition. |
| 11 | Cloaking limitations (frequency dispersion, Kramers-Kronig) | I | Standard analysis. |
| 12 | Cloaking ↔ SCBU boundary structural analogy | A→analogy | Not a derivation. |
| 13 | Specific metamaterial designs | I | Empirical / engineering. |
| 14 | Verdict M2 (Intermediate Path C) | A→position | Per Paper_095. No D rows present; audit content matches M2 (substrate identification + standard-machinery composition), not M3. |

---

## §5 Falsification Criteria

- **F1:** Substrate evidence that V1 + V5 do NOT produce effective-medium tensors consistent with metamaterial designs. Refutes step 6.
- **F2:** Photonic bandgap detected in non-periodic substrate microstructure (where Bloch theorem doesn't apply). Refutes step 5.
- **F3:** Negative-index detected in regimes with single-negative or no-negative tensor signature. Refutes step 7.
- **F4:** Substrate-level cloaking shown to fail at coordinate-deformation level (not just engineering-limitation). Refutes step 10.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the substrate-level derivation of three metamaterial-phenomenon classes via two-scale expansion.

**Relationship to other papers:**
- **Paper_011 (Bloch theorem):** photonic bandgap origin.
- **Paper_017 (acoustic metric):** cloaking coordinate-deformation source.
- **Paper_073 (DCGT):** two-scale expansion machinery.
- **Paper_089, 090 (V1, V5):** effective-medium tensor sources.
- **Paper_EDSC_AcousticCurvature:** mobility-gradient curvature companion.

**Numerical content INHERITED.** Specific metamaterial designs. **Form via inherited two-scale homogenization** with substrate V1/V5 inputs: bandgap / negative-index / cloaking structural mechanisms.

Verdict: **M2 (Intermediate Path C)**.

---

**End Paper Metamaterials.**
