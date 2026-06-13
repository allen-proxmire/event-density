# Memo_ED_Q1Q2_JointClosure_Scoping — Scoping Memo for Joint Q1/Q2 Closure Project

**Series:** Wave-3 Scoping Memo (Cosmology + Dynamics Arcs; successor to the Load-Bearing Program 2026-05-16)
**Status:** Substrate-graph scoping of whether the qualitative-mechanism load-bearing gaps Q1 (uniqueness of substrate-side Noether stress-energy for non-uniform and time-varying $\Psi$) and Q2 (uniqueness of the DCGT mapping from substrate stress-energy to standard continuum $T^{\mu\nu}$) admit joint closure. Closure would upgrade **Paper_ED_Cos_01 + Paper_ED_Dyn_02 + Paper_ED_Dyn_03 from M2 → M3 simultaneously** and would **fully close Paper_ED_GW_00 audit row 12 (form aspect)**. **Not a derivation. No new primitives proposed. Negative results acceptable.**
**Date:** 2026-05-16
**Anchors:** Paper_087 (13 primitives); Paper_073 (DCGT); Paper_ED_SC_4_9 (substrate-action $S_{\mathrm{sub}}$ + saddle Hessian classification); Paper_089 (V1 retarded kernel + T18); Paper_090 (V5 cross-chain); Paper_012 (P-RB-1 substrate-c); Paper_015 / T17 (gauge fields); Paper_098_5 / T1 (spin-statistics); Paper_109 (Lorentz reps); Paper_ED_Cos_01 (M2; Q1/Q2 inheritance); Paper_ED_Dyn_02 (M2; Q1/Q2 explicit OPEN rows); Paper_ED_Dyn_03 (M2; Q1/Q2 explicit OPEN rows). **Substrate-research support:** Memo_ED_DCGT_VacuumEnergyMapping + Audit (saturation-case Q1/Q2-free chain); Memo_ED_NonSaturation_StressEnergy + Audit (Q1/Q2 identified for non-saturation); Memo_ED_RadiationLaw_NoetherFlux + Audit (Q1/Q2 identified for time-varying sources); Memo_ED_LoadBearingProgram_Overview (program-level context).

---

## §1 Restated load-bearing gaps

### §1.1 Q1 — Noether stress-energy uniqueness

**Claim to close:** given the substrate Lagrangian $\mathcal{L}_{\mathrm{sub}}[\Psi, \nabla_{V_1}\Psi, \nabla_{V_5}\Psi]$ (Paper_ED_SC_4_9), the substrate-side Noether construction

$$
T^{\mu\nu}_{\mathrm{sub}} = \sum_{K \in \{V_1, V_5\}} \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K \Psi)} \nabla^\nu_K \Psi - g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}
$$

is the **unique consistent stress-energy tensor** for non-uniform and time-varying $\Psi$ states, modulo trivial improvement terms.

**Standard-physics precedent (NOT a counterexample but a warning):** in standard QFT the Noether stress-energy is famously non-unique — Belinfante-Rosenfeld improvement, Hilbert (metric-variation) tensor, and conformal-improvement variants all yield admissible $T^{\mu\nu}$ candidates that differ by total-divergence terms. The relevant standard fact is that *for spin-0 scalars Noether = Belinfante = Hilbert modulo conservation-preserving redefinitions*, while *for gauge fields the bare Noether tensor is non-symmetric and requires Belinfante symmetrization*. **Q1 must establish which standard ambiguity class applies to substrate-side $\Psi$ and what fixes the residual freedom uniquely.**

**Why Q1 is load-bearing:** the regime-specific predictions (traceless $T^\mu_\mu = 0$ for radiation, $w = 1/3$; dust-like $T^{ii} = 0$ for matter, $w = 0$; vacuum-energy $w = -1$ for saturation; Poynting / quadrupole flux forms for radiation sources) all depend on which member of the improvement-class is the "substrate-physical" one. Standard-QFT-analog inheritance assumes the standard physics choice; substrate-graph closure requires deriving the choice from substrate primitives.

### §1.2 Q2 — DCGT mapping uniqueness

**Claim to close:** given the DCGT coarse-graining axioms (Paper_073: hydrodynamic-window scale-separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$; energy-momentum conservation preservation; translation invariance; A→regime applicability), the substrate-side $T^{\mu\nu}_{\mathrm{sub}}$ maps to a **unique consistent continuum object** $T^{\mu\nu}_{\mathrm{eff}}$ that satisfies standard continuum-side conservation $\nabla_\mu T^{\mu\nu}_{\mathrm{eff}} = 0$ and standard hydrodynamic flux structure.

**Standard-physics precedent (warning):** coarse-graining maps are scheme-dependent in general. Different window kernels (Gaussian, Heaviside, Wilsonian sharp-momentum) produce different continuum-side objects that agree only at leading order in the scale-separation parameter. The substrate-side stress-energy could in principle map to continuum-side objects with **torsion, non-metricity, or anomalous trace** that all formally preserve energy-momentum conservation but differ in their geometric content.

**Why Q2 is load-bearing:** the continuum-side prediction (standard Einstein-gravity $T^{\mu\nu}_{\mathrm{eff}}$ feeding standard Friedmann; standard Maxwell stress-energy feeding standard Larmor; standard linearized-GR quadrupole flux feeding standard quadrupole formula) depends on DCGT producing the **standard metric-compatible torsion-free** continuum object. Standard-physics-analog inheritance assumes this; substrate-graph closure requires deriving it from DCGT axioms.

### §1.3 Joint nature

Q1 and Q2 are **logically independent but corpus-linked**: Q1 fixes the substrate-side input; Q2 fixes the substrate-to-continuum map. Both gaps must close for the form-IDENTIFIED → form-IDENTIFIED-substrate-graph upgrade. A Q1-only closure that leaves Q2 OPEN still permits non-standard continuum outcomes; a Q2-only closure that leaves Q1 OPEN still permits non-standard substrate-side inputs.

**Joint closure target:** the *composition* substrate-side Noether → DCGT → continuum $T^{\mu\nu}$ produces the standard-physics result *uniquely*, given Paper_ED_SC_4_9 + V1 + V5 + DCGT axioms.

---

## §2 Alternative candidates that must be ruled out

### §2.1 Alternative substrate-side stress-energy candidates (for Q1)

| Candidate | Standard precedent | Why it might survive substrate-graph | Why it must be ruled out for closure |
|---|---|---|---|
| **A.1 Bare Noether** | Standard QFT scalar | If $\Psi$ behaves as a substrate scalar | Asymmetric for V1/V5 kernel-mediated coupling to substrate-graph direction structure (Paper_093 T18); fails standard symmetry |
| **A.2 Belinfante-Rosenfeld improvement** | Standard QFT spin/gauge | If V1 / V5 kernel carries substrate-side analog of spin/gauge structure (per Paper_015 T17 + Paper_109) | Need substrate-graph identification of the spin/gauge piece; otherwise improvement structure is ambiguous |
| **A.3 Hilbert (metric-variation) tensor** | Standard GR | If substrate admits metric-variation principle | Substrate has no fundamental metric (Paper_ED_GW_00 §3.2); Hilbert construction requires continuum metric and so applies only post-DCGT |
| **A.4 Conformal-coupling improvement** | Massless scalar in 4D | If $\Psi$ is conformally coupled to substrate-effective curvature | Requires substrate-graph notion of conformal weight; not supplied by Paper_087 |
| **A.5 Non-local kernel-weighted stress-energy** | None in standard physics | If V1's finite width $\ell_{V_1}$ is loadbearing for the form | Standard hydrodynamic-window assumes locality at $R_{\mathrm{cg}}$; non-local candidate must reduce to local under coarse-graining |
| **A.6 Asymmetric (Cartan / torsion-bearing) stress-energy** | Einstein-Cartan theory | If substrate-graph direction structure (P09 polarity + P13 translation arrow) introduces intrinsic torsion | Substrate post-DCGT is torsion-free standard-GR-compatible (Paper_073 hydrodynamic-window); torsion candidate must be ruled out at DCGT level |

The closure must show that among A.1–A.6 (and any others), exactly one survives substrate-graph + DCGT consistency.

### §2.2 Alternative DCGT mapping candidates (for Q2)

| Candidate | Standard precedent | Why it might survive substrate-graph | Why it must be ruled out for closure |
|---|---|---|---|
| **B.1 Standard hydrodynamic coarse-graining** | BBGKY → Chapman-Enskog → Navier-Stokes; standard continuum-mechanics inheritance | DCGT's natural regime per Paper_073 | This is the target — must be uniquely selected |
| **B.2 Wilsonian RG-like multi-scale coarse-graining** | Standard QFT renormalization | If substrate admits scale-hierarchy beyond hydrodynamic window | Beyond DCGT axioms; not load-bearing for hydrodynamic-window claims |
| **B.3 Window-kernel-dependent coarse-graining** | Standard kinetic theory scheme dependence | Different windows (Gaussian, sharp, Heaviside) give different continuum objects | Must reduce to scheme-independent leading order under hydrodynamic-window scale-separation |
| **B.4 Torsion-introducing coarse-graining** | Einstein-Cartan; teleparallel gravity | If V1/V5 substrate-direction content survives coarse-graining as continuum torsion | Must be ruled out by DCGT axioms (metric-compatibility) or by showing substrate-direction content averages away |
| **B.5 Non-metricity-introducing coarse-graining** | Weyl-class geometries | If substrate-action density admits scale-rescaling that survives coarse-graining | Must be ruled out by DCGT energy-momentum conservation preservation |
| **B.6 Anomalous-trace coarse-graining** | Trace-anomaly in standard QFT (Polyakov; standard conformal anomaly) | If substrate-side scaling structure carries anomaly content | Must be either ruled out or absorbed into the standard QFT trace-anomaly inheritance |

The closure must show that among B.1–B.6, exactly B.1 (standard hydrodynamic) survives DCGT axioms + hydrodynamic-window constraints, modulo standard QFT trace-anomaly absorption.

---

## §3 Minimal substrate-graph assumptions required

For joint closure, the following substrate-graph inputs are load-bearing:

### §3.1 For Q1

- **Substrate-side $\mathcal{L}_{\mathrm{sub}}[\Psi, \nabla_{V_1}\Psi, \nabla_{V_5}\Psi]$ structure** (Paper_ED_SC_4_9). IDENTIFIED.
- **V1 + V5 kernel symmetry properties** (Paper_089 §3 Lorentz-covariance; Paper_090 cross-chain content). IDENTIFIED at structural level; the *specific symmetry-improvement consequences* for Noether stress-energy are OPEN.
- **Substrate-graph spin/gauge content via Paper_015 T17 + Paper_098_5/T1**. IDENTIFIED; T17 supplies gauge-bundle structure; T1 supplies $D = 3+1$ spin-statistics; substrate-graph derivation of Belinfante-improvement piece from this content is OPEN.
- **Substrate-graph locality radius** (V1 finite width $\ell_{V_1}$; V5 finite memory $\tau_{V_5}$). IDENTIFIED; whether this locality is sufficient for standard-QFT-class Noether uniqueness is OPEN.
- **SC-4.9 Hessian structure** as a constraint on the form of admissible $\mathcal{L}_{\mathrm{sub}}$ derivative content. IDENTIFIED structurally; the *uniqueness consequence* for Noether form is OPEN.

### §3.2 For Q2

- **DCGT axioms** (Paper_073). IDENTIFIED.
- **Hydrodynamic-window scale-separation** $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$. IDENTIFIED; the *uniqueness consequence* (scheme-independence at leading order) is OPEN.
- **Energy-momentum conservation preservation** under coarse-graining (BBGKY-class). IDENTIFIED structurally; the *consequence for ruling out torsion / non-metricity candidates* is OPEN.
- **Substrate translation invariance** (P03 + P13). IDENTIFIED; supplies Noether at substrate side and is preserved under DCGT in principle; whether it suffices to fix the continuum-side metric-compatibility is OPEN.
- **Substrate-side absence of fundamental metric** (Paper_ED_GW_00 §3.2). IDENTIFIED; consequence is that any continuum metric structure emerges from DCGT, not substrate; closure must show standard Lorentzian metric emerges uniquely.

### §3.3 What this paper does NOT assume

- No new primitive beyond Paper_087's 13 primitives.
- No paper-specific postulate beyond the structural content already in Paper_073 + Paper_ED_SC_4_9 + Paper_089 + Paper_090.
- No standard-physics-analog inheritance for Q1 or Q2 themselves (the inheritance is what closure must replace).

---

## §4 Route map for closure strategies

Five candidate routes; the first two attack Q1, the last three attack Q2. Routes are not mutually exclusive — a closure may compose Q1A + Q2A, Q1B + Q2B, etc.

### §4.1 Route Q1A — Noether-uniqueness via kernel-symmetry constraints

**Mechanism:** V1's substrate-side kernel has specific symmetry properties (Lorentz-covariance per Paper_089 §3; substrate-c-bound per Paper_012; forward-causal per Paper_093 T18). V5's cross-chain kernel has finite-memory structure (Paper_090) with substrate-side directional weighting. **Claim:** these kernel symmetries uniquely fix the Belinfante-improvement piece of substrate-side Noether — i.e., the bare Noether stress-energy + the unique kernel-symmetry-compatible improvement is the substrate-physical $T^{\mu\nu}_{\mathrm{sub}}$.

**Plausibility:** MEDIUM. V1's Lorentz-covariance is a substantive structural input; whether it is sharp enough to fix the entire improvement freedom (Belinfante + conformal + higher-order) is the load-bearing question. If yes, Q1A closes; if no, residual freedom persists and Q1A leaves a smaller-but-real gap.

**Load-bearing.**

### §4.2 Route Q1B — Noether-uniqueness via SC-4.9 Hessian structure

**Mechanism:** Per Paper_ED_SC_4_9, the substrate-action saddle Hessian classifies each substrate locus into compression-dominant and expansion-dominant axes. **Claim:** the Hessian's eigenvalue-signature partition imposes a substrate-graph constraint on the admissible form of $\mathcal{L}_{\mathrm{sub}}$ at each locus — and a corresponding constraint on the form of Noether stress-energy derived from it. The Hessian-eigenvalue-signature partition uniquely fixes which improvement-class member is substrate-physical (e.g., the symmetric improvement that respects the compression/expansion partition).

**Plausibility:** MEDIUM-LOW. The Hessian classification is a strong substrate-graph input but it's not obvious that it has anything to say about Noether improvement freedom. The route may turn out to be a vocabulary-level connection rather than a load-bearing closure.

**Possibly load-bearing.**

### §4.3 Route Q2A — DCGT-uniqueness via coarse-graining invariance

**Mechanism:** Standard kinetic theory establishes that the leading-order coarse-grained stress-energy is scheme-independent: Gaussian, sharp-momentum, Heaviside windows all give the same continuum $T^{\mu\nu}_{\mathrm{eff}}$ at leading order in $\ell_{\mathrm{ED}} / R_{\mathrm{cg}}$. **Claim:** DCGT's hydrodynamic-window scale-separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ is exactly the parameter regime where this scheme-independence holds, and so DCGT's output is unique modulo scheme-dependent subleading corrections. Rules out B.3 (window-kernel-dependent) at leading order.

**Plausibility:** HIGH. This is standard kinetic-theory inheritance applied to DCGT's regime; the substrate-graph addition is identifying that DCGT *is* in this regime by axiom. Likely closes.

**Load-bearing.**

### §4.4 Route Q2B — DCGT-uniqueness via hydrodynamic-window conservation laws

**Mechanism:** Energy-momentum conservation under coarse-graining is a DCGT axiom (BBGKY-class inheritance). Standard kinetic theory shows that conservation-preserving coarse-grainings of substrate-side stress-energy produce continuum stress-energy with the standard hydrodynamic flux structure (Euler + Navier-Stokes-class equations) at leading order. **Claim:** the conservation requirement rules out B.4 (torsion-introducing) and B.5 (non-metricity-introducing) candidates, because both violate the standard form of continuum-side $\nabla_\mu T^{\mu\nu}_{\mathrm{eff}} = 0$.

**Plausibility:** MEDIUM-HIGH. Conservation does pin a lot; whether it pins the *full* metric-compatibility (Q2C territory) or only a weaker structural condition is the load-bearing question. May close in conjunction with Q2C.

**Load-bearing.**

### §4.5 Route Q2C — DCGT-uniqueness via metric-compatibility constraints

**Mechanism:** Substrate has no fundamental metric (Paper_ED_GW_00 §3.2); the continuum-side metric emerges from DCGT. **Claim:** DCGT's translation-invariance + Lorentz-covariance preservation forces the emergent continuum metric to be standard Lorentzian and metric-compatible (no torsion, no non-metricity). Combined with Q2B (conservation), this rules out the full B.4 + B.5 alternative class.

**Plausibility:** MEDIUM. The substrate-graph derivation of standard Lorentzian metric emergence is a substantive claim that may itself require additional substrate-research; if it holds, Q2C completes Q2B closure. If the substrate-side direction content (P09 polarity + P13 translation arrow) survives coarse-graining as continuum torsion, Q2C fails and substrate-derived continuum geometry is non-standard.

**Load-bearing; potentially fragile.**

---

## §5 Load-bearing vs vocabulary-level routes

| Route | Load-bearing? | Notes |
|---|---|---|
| **Q1A** (kernel-symmetry) | **YES — load-bearing for Q1 closure** | Direct attack on Noether improvement freedom via substrate-side kernel structure |
| **Q1B** (Hessian structure) | Possibly vocabulary-level; need explicit construction to determine | Hessian connection to Noether improvement is not standard; may yield substantive constraint or may be reframing only |
| **Q2A** (coarse-graining invariance) | **YES — load-bearing for Q2 closure** | Standard kinetic-theory result applied to DCGT regime; high closure plausibility |
| **Q2B** (conservation laws) | **YES — load-bearing for Q2 closure** | Pins hydrodynamic flux structure; needs Q2C for full metric-compatibility |
| **Q2C** (metric-compatibility) | **YES — load-bearing for Q2 closure** | Completes Q2B; potentially fragile if substrate-direction content survives coarse-graining |

**Net assessment:**

- **Q1A + Q2A + Q2B + Q2C is the cleanest candidate joint-closure path.** Q1A attacks the substrate side via kernel symmetry; Q2A + Q2B + Q2C attack the continuum side via coarse-graining invariance + conservation + metric-compatibility.
- **Q1B is a substantively interesting but uncertain auxiliary route** — worth investigating if Q1A leaves residual freedom; may serve as a tightening route.
- **Joint closure plausibility: MEDIUM** — higher than Route A (substrate-research-frontier cosmological-parameter derivation) but lower than the standard M3-template closures of loads #1/#3/#4 (which inherited from standard physics).
- **The substrate-graph content of all five routes uses corpus material already in place** (no new primitives proposed), which makes the work *construction* rather than *discovery*.

---

## §6 IDENTIFIED vs OPEN

### IDENTIFIED

- The substrate-side $\mathcal{L}_{\mathrm{sub}}$ structure (Paper_ED_SC_4_9).
- V1 + V5 kernel structural properties (Paper_089 §3 Lorentz-covariance; Paper_090 finite-memory; Paper_093 T18).
- DCGT axioms (Paper_073).
- Substrate has no fundamental metric (Paper_ED_GW_00 §3.2).
- Substrate-side spin/gauge supporting content (Paper_015 T17; Paper_098_5/T1; Paper_109).
- The alternative-candidate catalogs (§2.1 A.1–A.6; §2.2 B.1–B.6).
- The five candidate routes (§4 Q1A, Q1B, Q2A, Q2B, Q2C).
- The minimal substrate-graph assumptions required for closure (§3).

### OPEN (load-bearing for joint Q1/Q2 closure)

- **Q1 sub-OPEN-1:** uniqueness consequence of V1 + V5 kernel symmetries for substrate-side Noether improvement freedom (Q1A target).
- **Q1 sub-OPEN-2:** whether SC-4.9 Hessian structure imposes a substantive constraint on Noether improvement form, or is vocabulary-level only (Q1B target).
- **Q1 sub-OPEN-3:** substrate-graph derivation of Belinfante-improvement piece from Paper_015 T17 + Paper_098_5/T1 substrate-side spin/gauge content.
- **Q2 sub-OPEN-1:** scheme-independence proof for DCGT at hydrodynamic-window leading order (Q2A target).
- **Q2 sub-OPEN-2:** energy-momentum-conservation pinning of standard continuum flux structure (Q2B target).
- **Q2 sub-OPEN-3:** standard Lorentzian metric-compatibility emergence under DCGT, ruling out torsion / non-metricity candidates (Q2C target).
- **Joint composition uniqueness:** does substrate-side Q1-result + Q2-result composition produce standard continuum $T^{\mu\nu}$ uniquely, or could residual freedom survive in the composition even with both gaps separately closed?

### OPEN (substantive, not load-bearing for Q1/Q2 closure)

- Substrate-graph derivation of numerical coefficients (Dyn_03 row 14) — *independent of Q1 + Q2*; not addressed here.
- Substrate-graph derivation of $H_0$ via Route A — *independent of Q1 + Q2*; not addressed here.
- Saddle-Hessian-dynamics alternative routes to horizon-motion / radiation (Dyn_02 row 12; Dyn_03 row 13) — substrate-research-frontier alternatives; not load-bearing for the joint closure here.

### Negative-finding possibilities (acceptable outcomes)

A substantively informative negative finding would be:

- **N1:** Q1A fails — V1 + V5 kernel symmetries are insufficient to pin Noether improvement freedom substrate-graph. Substrate ontology does not supply the uniqueness; the closure would require an additional substrate primitive or paper-specific postulate.
- **N2:** Q2C fails — substrate-side direction content (P09 + P13) survives DCGT coarse-graining as continuum torsion. Substrate-derived continuum geometry is non-standard (Einstein-Cartan-class rather than standard GR), which would be a substantive substrate-ontology characterization separate from standard physics inheritance.
- **N3:** joint composition fails — even with Q1 and Q2 separately closed, the substrate-side stress-energy → DCGT → continuum stress-energy composition admits residual freedom not pinned by the individual closures.

Any of N1–N3 would honestly cap Cos_01 + Dyn_02 + Dyn_03 at M2 permanently and constitute a corpus-level finding about the substrate ontology's reach. Per the Load-Bearing Program pattern, negative findings (load #2 chirality-symmetric) are first-class results.

---

## §7 Recommended next steps

**Path-Q1A (focused construction memo):** attack Route Q1A directly. Substrate-side derivation of V1 + V5 kernel-symmetry consequences for Noether improvement freedom; explicit construction of the unique kernel-symmetry-compatible improvement (or demonstration that residual freedom persists). **Most-tractable starting point** — has the highest closure plausibility for the Q1 side.

**Path-Q2A (focused construction memo, parallel to Q1A):** attack Route Q2A directly. Substrate-side derivation of DCGT scheme-independence at hydrodynamic-window leading order. Likely closes (standard kinetic theory + DCGT axiom composition); supplies one of three Q2 closure pieces.

**Path-Q1B (auxiliary):** attempt only if Q1A leaves residual freedom. SC-4.9 Hessian-structure connection to Noether improvement form; substantive-or-vocabulary determination.

**Path-Q2B + Q2C (sequential construction):** after Q2A, attack Q2B (conservation laws pin hydrodynamic flux) and Q2C (metric-compatibility rules out torsion / non-metricity). Q2C is potentially fragile and may produce a negative finding (N2 above).

**Path-Joint-Audit (after construction):** Claude-B-class adversarial audit of the composed Q1 + Q2 closure once construction memos exist. Counterexample search; alternative-mapping defeat-attempts; verification that joint closure is sharper than each individual closure.

**My recommendation:** **Path-Q1A + Path-Q2A in parallel.** Both attack the highest-closure-plausibility routes for their respective gaps; both use existing corpus material without new substrate-research-frontier work. If both close, Q1B + Q2B + Q2C follow naturally as tightening / completion work. If Q1A fails (N1) or Q2C fails (N2), the negative findings are themselves corpus contributions — substrate-ontology reach is honestly mapped.

**Closure plausibility for full joint Q1 + Q2:** MEDIUM. Higher than Route A; lower than the M3-template-based load-bearing closures already achieved. The work is *construction* using existing corpus content — closer to vocabulary-elevation than to substrate-research-discovery.

**Cross-program note:** if joint Q1 + Q2 closes, **Cos_01 + Dyn_02 + Dyn_03 upgrade M2 → M3 simultaneously, GW_00 row 12 closes fully on the form aspect, and Paper_ED_Cos_05 becomes draftable at M3 conditional on Route A only.** This is a three-paper-upgrade single-project win, larger immediate corpus impact than Route A's six-projection ED-SC 4.x M3 → M2 downgrade.

**Compared with Route A:** Q1/Q2 joint closure targets the *qualitative-mechanism* gap that the Load-Bearing Program identified; Route A targets the *quantitative-magnitude* gap. They are complementary and non-competing. Q1/Q2 first is the lower-risk, higher-near-term-payoff path; Route A first leaves the verdict ceilings still pinned at M2.

---

**End Memo_ED_Q1Q2_JointClosure_Scoping.**
