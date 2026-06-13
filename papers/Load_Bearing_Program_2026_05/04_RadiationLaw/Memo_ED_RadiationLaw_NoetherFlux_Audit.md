# Memo_ED_RadiationLaw_NoetherFlux_Audit — Adversarial Audit of OPEN-RL-1 Closure

**Series:** Wave-3 Audit Memo (Cosmology + Dynamics Arcs; Claude-B-class adversarial audit of Memo_ED_RadiationLaw_NoetherFlux)
**Status:** Critical audit of the OPEN-RL-1 closure claim that substrate-side Noether stress-energy flux for time-varying $\Psi$ content, combined with DCGT coarse-graining, yields EM Larmor and GW quadrupole continuum formulas at D-via-I level. **Not a derivation. Auditor stance, not advocate.** Following the discipline cascade from CommitPhaseInheritance_Audit + three M3-chain audits.
**Date:** 2026-05-16
**Anchors:** Memo_ED_RadiationLaw_NoetherFlux (audit target); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$); Paper_073 (DCGT); Paper_ED_GW_00 (row 12 closure target); Paper_ED_Dyn_03 (placeholder; would close via this audit); Paper_089 (V1 finite-width retarded); Memo_ED_NonSaturation_StressEnergy_Audit (parallel pattern); other M3-chain audit memos (precedents).
**Headline verdict:** **ACCEPT at "approximately-standard-physics level"** with two explicit qualifications — the same pattern as NonSaturation_StressEnergy audit ACCEPTED. Closure not overclaim; analog-inheritance qualifications are honest and parallel established M3-template precedents.

---

## §1 What's being audited

NoetherFlux claims OPEN-RL-1 closure via a five-step chain:

1. Source-class identification (accelerated chain / time-varying multipole) — inherited by standard EM/GR analog
2. Substrate-side Noether stress-energy for time-varying $\Psi$ → non-trivial flux components $T^{0i}_{\mathrm{sub}}$
3. DCGT translation to continuum stress-energy flux $T^{0i}_{\mathrm{eff}}$
4. Standard Maxwell / linearized Einstein retarded-Green's-function machinery
5. EM Larmor $P = q^2 a^2/(6\pi\epsilon_0 c^3)$ + GW quadrupole $P = G\dddot Q^2/(5c^5)$ formulas

The memo flags two audit issues (§7 audit flags). This memo extends to **five audit flags** examined adversarially.

---

## §2 Audit flag #1 — Source-class identification

### Examination

**Claim:** "Accelerated chain" = chain whose V1-propagation-direction changes between commitment events; "time-varying multipole" = spatial $\Psi$-distribution with time-varying spatial moments.

**Required substrate-graph content:**
- Substrate-graph criterion for "chain V1-propagation direction"
- Substrate-graph criterion for "direction change between commitment events" (i.e., acceleration)
- Substrate-graph multipole expansion of $\Psi$ content

**Supplied by corpus?**

Paper_089 + Paper_093 T18 supply chain-arrow direction (V1 retarded support direction at commitment locus). Per Paper_012 P-RB-1 + Paper_089, V1 has substrate-c bound. Chain-arrow direction changes are substrate-graph well-defined.

But: the specific identification *"V1-propagation-direction change = acceleration analogous to standard EM accelerated charge"* is **INHERITED by standard EM analog**, not derived substrate-graph. The substrate has the supporting content; the specific analog mapping is the load-bearing step.

Similarly for "time-varying multipole": Paper_ED_SC_4_9 supplies saddle-Hessian structure; spatial moments of $\Psi$ distribution are substrate-graph well-defined; but the specific identification *"time-varying second-moment = mass-quadrupole analogous to standard GR"* is inherited by standard GR analog.

### Adversarial finding

**Same kind of inheritance assumption as load-bearing #3 audit flag A** (chain-class identification by standard-QFT analog). Substrate has supporting content; specific analog mapping is inherited.

**Status:** ACCEPT with qualification that source-class identification is INHERITED by standard EM/GR analog. Explicit substrate-graph construction would tighten the closure.

---

## §3 Audit flag #2 — Non-uniform Noether for time-varying $\Psi$

### Examination

**Claim:** Substrate-side Noether procedure on $\mathcal{L}_{\mathrm{sub}}$ for time-varying $\Psi$ gives non-trivial flux components $T^{0i}_{\mathrm{sub}}$ with form matching standard Poynting (EM) and quadrupole-flux (GW) structures.

**Required substrate-graph content:**
- Substrate-side Noether procedure for non-uniform time-dependent $\Psi$
- Specific flux form (Poynting-class for EM-coupled chain; quadrupole-flux for GW-relevant sources)

**Supplied?**

The M3-chain audit (DCGT_VacuumEnergyMapping) accepted Noether for uniform $\Psi$ (derivative terms vanish → vacuum-energy form). The NonSaturation_StressEnergy audit accepted Noether for non-uniform stationary $\Psi$ (traceless or dust-like forms by standard QFT analog).

This memo extends to time-varying $\Psi$ — Noether produces non-trivial $T^{0i}_{\mathrm{sub}}$ flux components. Standard QFT inheritance gives the flux structure for time-varying fields (well-established in standard radiation theory).

**Substrate-side specific form:** depends on V1 + V5 kernel structure. Per Paper_089 §3, V1 has Lorentz-covariant structure — necessary for the Noether procedure to give standard Lorentz-covariant stress-energy. Whether it's sufficient for the specific Poynting / quadrupole-flux forms requires substrate-graph verification.

### Adversarial finding

**Same kind of inheritance assumption as load-bearing #3 audit flag B** (specific stress-energy forms inherited by standard-QFT analog). The Noether procedure structure is well-established; the specific form depends on substrate-side Lagrangian which is plausible but not constructed explicitly.

**Status:** ACCEPT with qualification that the specific stress-energy flux forms (Poynting, quadrupole-flux) are INHERITED by standard-QFT analog applied to substrate-side $\mathcal{L}_{\mathrm{sub}}$. Same level as load-bearing #3 audit acceptance.

---

## §4 Audit flag #3 — DCGT preserves flux structure for time-varying sources

### Examination

**Claim:** DCGT coarse-graining of substrate-side time-varying flux preserves the flux structure required for radiation laws.

**Standard hydrodynamics-from-microscopics:** BBGKY hierarchy + Chapman-Enskog preserve energy-momentum conservation; continuum stress-energy emerges from substrate-side stress-energy averaging.

**For time-varying flux:** DCGT must preserve time-derivative structure at the coarse-graining scale. Standard hydrodynamics derivations handle smooth time-evolution at scales $\tau \gg \tau_{\mathrm{micro}}$. For substrate-side $\tau_{\mathrm{micro}} \sim \tau_{V_1} \sim \ell_{V_1}/c$, DCGT applies for radiation frequencies $\omega \ll 1/\tau_{V_1} \sim c/\ell_{V_1}$.

### Adversarial finding

**For standard radiation frequencies** (radio to gamma): $\omega \ll c/\ell_{V_1}$, well within hydrodynamic-window. DCGT preserves flux structure cleanly. ✓

**For near-substrate-scale frequencies** ($\omega \to c/\ell_{V_1}$): DCGT at edge of validity (similar to saturation regime in load #1 or early-RDE in load #3). Regime restriction; not load-bearing for standard radiation phenomenology.

**Status:** ACCEPT with regime-restriction qualification (DCGT applies for radiation at standard physical frequencies; edge-of-validity at near-Planck-scale frequencies).

---

## §5 Audit flag #4 — V1 retarded consistency with continuum retarded Green's functions

### Examination

**Claim:** V1's finite-width retarded propagation reproduces standard continuum retarded Green's function $G^{\mathrm{ret}} = \delta(t - t' - |x - x'|/c)/(4\pi|x-x'|)$ under DCGT coarse-graining.

**Structural consistency check:** V1 has finite width $\ell_{V_1}$; standard $G^{\mathrm{ret}}$ has delta-function support on the light-cone.

**Substrate-graph derivation:** for coarse-graining scale $R_{cg} \gg \ell_{V_1}$, V1's finite-width support is effectively delta-function-like at the coarse-graining scale → consistent with standard $G^{\mathrm{ret}}$ at continuum level.

### Adversarial finding

**For $R_{cg} \gg \ell_{V_1}$** (cosmological + astrophysical scales): V1 → standard retarded Green's function cleanly. ✓

**For $R_{cg} \sim \ell_{V_1}$** (near-substrate-scale): V1's finite width is resolved at coarse-graining scale; continuum retarded Green's function approximation breaks down. Same regime restriction as flag #3.

**Status:** ACCEPT with regime-restriction qualification. V1 retarded propagation is consistent with continuum retarded Green's functions at the DCGT-hydrodynamic-window scale.

---

## §6 Counterexample search

**Candidate 1: Time-varying $\Psi$ with zero radiation.** Standard physics: stationary fields don't radiate. Substrate-side: time-varying $\Psi$ → non-zero Noether flux. Both agree on the basic existence statement. Not a defeating counterexample.

**Candidate 2: Non-standard radiation patterns (e.g., monopole radiation).** Standard EM: monopole radiation forbidden by charge conservation. Standard GR: monopole + dipole gravitational radiation forbidden by mass-momentum conservation. Substrate-side: should respect these via substrate-side analog of charge/mass conservation.

Per Paper_015 T17, substrate-side gauge content has continuity equation (Paper_010 / Paper_015 inheritance). Per Paper_087 P02 + P04, substrate-side bandwidth content is additive + conserved. **Substrate-side charge/mass conservation is supplied by corpus content.** Standard radiation pattern selection rules (no monopole / dipole gravitational) inherit cleanly.

Not a defeating counterexample.

**Candidate 3: Non-standard polarization modes.** Paper_ED_GW_00 explicitly establishes two transverse GW polarizations only (no scalar / vector / longitudinal) per saddle-Hessian eigenvalue partition + Paper_109 + Paper_116. **Substrate-side GW radiation has standard $h_+, h_\times$ polarizations.** For EM: standard transverse polarizations via Paper_015 T17 + Paper_109. ✓

Not a defeating counterexample.

**Candidate 4: Substrate-side radiation with additional fundamental-scale modes (Planck-scale photon analog).** ED's discrete substrate (Paper_087 + Paper_089 finite-width V1) doesn't have an infinite tower of QFT modes. The substrate's "radiation field" is bounded by substrate-graph content at substrate scale.

But: at standard radiation frequencies, the substrate-graph cutoff is irrelevant (DCGT smooths over substrate-scale content). At Planck-scale frequencies, substrate cutoff matters but DCGT is at edge of validity anyway.

Not a defeating counterexample at standard physical frequencies.

**Counterexample search yields no defeating cases.** Standard radiation phenomenology is respected by substrate-side approach across all examined candidates.

---

## §7 Comparison with prior audits + verdict

| Audit | Required content supplied? | Strict reading consistent? | Counterexample defeats? | Verdict |
|---|---|---|---|---|
| CommitPhaseInheritance | NO (channel-uniqueness) | NO (zero antimatter) | YES (V5 cross-boundary) | REJECTED |
| SubstrateAction_Constancy | YES (approximate) | YES | NO | ACCEPTED (approximately-constant) |
| DCGT_VacuumEnergyMapping | YES (approximate) | YES | NO | ACCEPTED (approximately-vacuum-energy) |
| NonSaturation_StressEnergy | PARTIALLY (standard-QFT-analog) | YES | NO | ACCEPTED (approximately-standard-cosmology) |
| **NoetherFlux (this audit)** | **PARTIALLY (standard-EM/GR-analog)** | **YES** | **NO** | **ACCEPTED (approximately-standard-physics)** |

### Verdict

**ACCEPT the OPEN-RL-1 closure at "approximately-standard-physics level"** with three explicit qualifications:

- **Source-class identification (accelerated chain / time-varying multipole) is INHERITED by standard EM/GR analog**, not derived substrate-graph from existing primitives. Plausible from Paper_015 T17 + Paper_ED_SC_4_9 + standard physics structure; explicit substrate-graph criterion not constructed. (Same pattern as load #3 audit flag A.)
- **Specific stress-energy flux forms (Poynting for EM; quadrupole-flux for GW) are INHERITED by standard-QFT analog choices applied to substrate-side $\mathcal{L}_{\mathrm{sub}}$.** Substrate-graph derivation of the specific forms via V1 + V5 kernel structure is plausible but not explicit. (Same pattern as load #3 audit flag B.)
- **DCGT applies for radiation at standard physical frequencies** (radio to gamma); edge-of-validity at near-Planck-scale frequencies (regime restriction matching load #1 / #3 boundary cases).

These qualifications match the **same level of approximation as load-bearing #3 audit acceptance**. The closure is acceptable at this level.

### Distinct from CommitPhaseInheritance overclaim case

CommitPhaseInheritance was REJECTED because:
- Required content NOT supplied (channel-uniqueness)
- Strict reading structurally INCONSISTENT (zero antimatter)
- Independent counterexample existed (V5 cross-boundary)

This memo's audit ACCEPTS because:
- Required content PARTIALLY supplied + standard EM/GR inheritance fills the rest (same as load #3)
- Strict reading structurally consistent (standard radiation phenomenology)
- No counterexample defeats

The closure is **at the same approximate-level as load-bearing #3 audit**, with standard-physics-analog inheritance qualifications honestly named.

### What the closure does NOT establish

- Strict substrate-graph derivation of Larmor coefficient $1/(6\pi\epsilon_0)$ or quadrupole coefficient $1/5$ from substrate parameters alone. Only at standard-physics-analog level.
- Substrate-graph criterion for source-class distinction. Inherited by analog.
- Radiation at near-Planck-scale frequencies (beyond DCGT hydrodynamic-window).
- Radiation reaction / self-force effects (standard physics inheritance, not load-bearing here).

---

## §8 Recommended updates + load-bearing program closure

### Updates to NoetherFlux memo

1. **Add explicit "standard-EM/GR-analog inheritance" framing** for source-class identification (§2) and stress-energy flux form derivation (§3).
2. **Acknowledge the hidden-inheritance pattern** — closure inherits from standard EM/GR templates more than from substrate-graph derivation. Same pattern as load #3 audit acceptance.
3. **Add DCGT regime restriction note** for near-Planck-scale frequencies.

### Status update for load-bearing #4

| Step | Substance | Status |
|---|---|---|
| A | Source-class identification | **D-via-I (this audit ACCEPTED at approximately-standard-physics level)** |
| B | Substrate-side Noether for time-varying $\Psi$ | **D-via-I (this audit ACCEPTED)** |
| C | DCGT translation to continuum flux | **D-via-I (this audit ACCEPTED; DCGT sweet spot)** |
| D | Maxwell / linearized Einstein retarded-Green's machinery | INHERITED (standard physics) |
| E | Larmor / quadrupole formulas | INHERITED (standard radiation theory) |

**Load-bearing #4 closes at D-via-I via M3-template extended to time-varying sources.** Paper_ED_GW_00 row 12 closes retroactively.

### Load-bearing program final status

| # | Item | Status |
|---|---|---|
| 1 | Exponential growth | **CLOSED D-via-I (audit ACCEPTED, robust)** |
| 2 | Chirality $\mathbb{Z}_2$ | **OPEN; substrate is chirality-symmetric (negative finding)** |
| 3 | Horizon motion | **CLOSED D-via-I (audit ACCEPTED, weaker — analog-inheritance qualifications)** |
| **4** | **ED radiation law** | **CLOSED D-via-I (audit ACCEPTED, this memo — analog-inheritance qualifications)** |
| 5 | Λ smallness | **Conditionally closed pending Route A + Friedmann inheritance** |

### Substrate-research program characterization (final form)

**Three load-bearing items closed via M3-template:** loads #1, #3, #4 — all via substrate-side Noether → DCGT translation → standard physics inheritance pattern. Pattern is robust across substrate-side state types (uniform, non-uniform stationary, time-varying).

**One load-bearing item negative:** load #2 (chirality $\mathbb{Z}_2$) — substrate is chirality-symmetric; specialized substrate-graph machinery required beyond existing primitives; closure not achievable from corpus.

**One load-bearing item conditionally closed:** load #5 (Λ smallness) reduces to Route A closure + Friedmann inheritance. Route A is the highest-leverage open derivation in the corpus per ED_MEMORY anchor 7.

**Final substrate-research-frontier characterization:** ED's substrate ontology supports standard cosmology + radiation phenomenology via M3-template + DCGT + standard QFT/EM/GR inheritance applied to substrate-side analogs. ED's substrate does NOT supply specialized substrate-graph derivations beyond standard physics inheritance (chirality $\mathbb{Z}_2$) or quantitative-magnitude items independent of Route A (Λ smallness reduces to Route A).

**Route A** ($\ell_{V_5}(H_0)$ substrate-side derivation) remains the **single highest-leverage open derivation** with cross-arc impact: ED-SC 4.x arc-wide upgrade + load #5 closure + possibly more.

### Cross-arc consequences if NoetherFlux audit accepted

- **Paper_ED_GW_00 audit row 12** closes retroactively. GW paper has no substantive load-bearing OPEN remaining.
- **Paper_ED_Dyn_03** (Radiation Law) becomes draftable at M3 form-IDENTIFIED. Captures EM Larmor + GW quadrupole substrate-side derivation.
- **Paper_ED_Dyn_05** (Inspiral dynamics) unlocked (depends on Dyn_01 + Dyn_03).
- **Paper_ED_GW_01** (BH ringdown spectroscopy) gains substantive radiation-amplitude content.

**Substantial Dynamics-Arc advance.**

### Recommended next steps

**Path-Update-Dyn_03:** draft Paper_ED_Dyn_03 (Radiation Law paper) at M3 form-IDENTIFIED, referencing the audited NoetherFlux substrate-graph chain. Mirror Paper_ED_Cos_01's M3 upgrade pattern: scoping memo + construction memo + audit memo → paper update.

**Path-Update-GW_00:** update Paper_ED_GW_00 audit table to reflect row 12 closure via NoetherFlux + this audit. Verdict potentially upgrades or strengthens.

**Path-Consolidate-Program:** consolidate the substrate-research-frontier findings into a program-overview memo. The substrate-research closure of the load-bearing program is substantively complete (modulo Route A and the negative finding on chirality).

**My recommendation:** **Path-Update-Dyn_03 + Path-Update-GW_00 in parallel** — both papers benefit from this audit's closure. Then **Path-Consolidate-Program** to capture the substrate-research findings for the corpus.

### Substrate-ontology characterization

The four audit memos in the cascade (load #1 + #3 + #4) collectively establish a robust substrate-ontology characterization:

**ED's substrate ontology supports standard cosmology + radiation phenomenology via DCGT + standard QFT/EM/GR inheritance** applied to substrate-side analogs, across all examined substrate-side state types (uniform, non-uniform stationary, time-varying).

**Limits of substrate reach:** (i) specialized substrate-graph derivations beyond standard physics inheritance (load #2 chirality); (ii) quantitative-magnitude items independent of Route A (load #5).

**This characterization is substantively informative about the substrate-ontology lineage's reach.** Consistent with corpus's substrate-ontology lineage (Wolfram, 't Hooft, causal-set) — substrate-side physics inherits cleanly from standard physics through coarse-graining bridge; doesn't replicate standard physics from substrate-graph principles alone.

The load-bearing program's substantive substrate-research closure (3 closed + 1 negative + 1 conditional on Route A) is a meaningful corpus contribution. **Route A remains the central substrate-research-frontier item.**

---

**End Memo_ED_RadiationLaw_NoetherFlux_Audit.**
