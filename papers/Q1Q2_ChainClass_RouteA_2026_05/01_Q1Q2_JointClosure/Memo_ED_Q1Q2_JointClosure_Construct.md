# Memo_ED_Q1Q2_JointClosure_Construct — Construction Memo (Q1A + Q2A Attempts)

**Series:** Wave-3 Construction Memo (Cosmology + Dynamics Arcs; Q1/Q2 Joint-Closure Project; Path-Q1A + Path-Q2A from Memo_ED_Q1Q2_JointClosure_Scoping §7)
**Status:** Substrate-graph attempt at Route Q1A (kernel-symmetry uniqueness of substrate-side Noether stress-energy) and Route Q2A (coarse-graining invariance uniqueness of the DCGT mapping). **Not a derivation. No new primitives.** Outcome: **substantive positive-partial — Q1A eliminates A.2–A.6 leaving A.1 (bare Noether) as unique candidate under stated assumptions; Q2A eliminates B.2–B.5 at leading order in $\varepsilon = \ell_{\mathrm{ED}}/R_{\mathrm{cg}}$ leaving B.1 (standard hydrodynamic mapping) as unique candidate.** Three residual OPEN items remain: (i) confirmation that $\Psi$ is substrate-scalar at SC-4.9 level (load-bearing for Q1A); (ii) subleading-order scheme-dependence in Q2A (O($\varepsilon$) corrections; not load-bearing for leading-order continuum phenomenology); (iii) trace-anomaly inheritance B.6 (outside DCGT scope; standard continuum-QFT inheritance). Q2B + Q2C remain pending for full Q2 closure (conservation-pinned flux structure and metric-compatibility).
**Date:** 2026-05-16
**Anchors:** Memo_ED_Q1Q2_JointClosure_Scoping (parent project; Q1A + Q2A scope); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ + Hessian); Paper_073 (DCGT + hydrodynamic-window axioms); Paper_087 (13 primitives — P02, P03, P04, P09, P10, P11, P12, P13); Paper_015 / T17 (gauge-bundle structure); Paper_098_5 / T1 ($D = 3+1$ spin-statistics); Paper_109 (Lorentz reps); Paper_089 (V1 Lorentz-covariance §3); Paper_090 (V5 cross-chain); Paper_012 (P-RB-1 substrate-c); Paper_093 (T18 kernel-arrow); Paper_ED_GW_00 §3.2 (no fundamental substrate metric). **Standard kinetic-theory inheritance:** Bensoussan-Lions-Papanicolaou (1978) two-scale homogenization theorem.

> ⚠️ **Correction (2026-07-06):** This document cites Θ_ED as "Paper_087 P12 (ED-threshold)" (see the B.5 non-metricity discussion below). That attribution is incorrect — canonical `Paper_087` P12 is a stability-landscape functional (Σ_C), unrelated to an event-density threshold. Θ_ED's actual (uncritically-inherited) origin is `Paper_ED_CCC_ConformalCyclicCosmology.md` §3.2/§3.7 (ED Generative repo), itself now flagged with the same correction. This does not change this document's tier verdicts — it only corrects the primitive citation. See `docs/Scoping_ThetaED_FirstPrinciples_2026-07-06.md`.

---

## §1 Setup

### §1.1 Substrate Lagrangian content

Per Paper_ED_SC_4_9, the substrate action is

$$
S_{\mathrm{sub}}[\Psi] = \int \mathcal{L}_{\mathrm{sub}}\big[\Psi, \nabla_{V_1}\Psi, \nabla_{V_5}\Psi\big] \, d\mu_{\mathrm{sub}}
$$

with $\Psi$ the substrate-action density and $\nabla_K$ the kernel-derivative for $K \in \{V_1, V_5\}$. **$\Psi$ is substrate-scalar** at SC-4.9 level: per Paper_087 P02 (participation) and Paper_ED_SC_4_9 §2, $\Psi$ is a single scalar density on the substrate graph; substrate-side rule-type / gauge-bundle / spin / chirality content lives in *separate* substrate-graph structures (Paper_015 T17 rule-type bundles; Paper_098_5/T1 $D=3+1$ spin classes; Paper_109 Lorentz reps) that enter the continuum-side theory through DCGT translation, not through $\Psi$'s Lorentz-tensor structure.

This $\Psi$-scalar property is **assumed** in this memo and is itself a substrate-graph claim that load-bears the Q1A closure (see §4 residual OPEN-i).

### §1.2 Substrate-side Noether tensor (A.1)

Under substrate-translation invariance (P03 + P13), the bare substrate-side Noether stress-energy is

$$
T^{\mu\nu}_{\mathrm{sub},\mathrm{Noether}} = \sum_{K \in \{V_1, V_5\}} \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K \Psi)}\, \nabla^\nu_K \Psi - g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}.
$$

Conservation $\nabla_\mu T^{\mu\nu}_{\mathrm{sub},\mathrm{Noether}} = 0$ follows from translation invariance by standard Noether-theorem construction. **A.1 is the canonical candidate.**

### §1.3 DCGT coarse-graining operator

Per Paper_073, DCGT acts as

$$
T^{\mu\nu}_{\mathrm{eff}}(x) = \int W_{R_{\mathrm{cg}}}(x - y) \, T^{\mu\nu}_{\mathrm{sub}}(y) \, dy
$$

with window function $W_{R_{\mathrm{cg}}}$ of characteristic scale $R_{\mathrm{cg}}$ satisfying $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ (hydrodynamic-window axiom), normalized $\int W = 1$, and translation-covariant. **B.1 is the canonical mapping.**

---

## §2 Route Q1A — Kernel-symmetry uniqueness

Goal: prove A.1 is the unique candidate under V1/V5 kernel symmetry + locality + conservation + gauge-bundle compatibility constraints.

### §2.1 Improvement freedom in standard QFT

Noether stress-energy admits improvement $T^{\mu\nu} \to T^{\mu\nu} + \partial_\lambda \Sigma^{\lambda\mu\nu}$ where $\Sigma^{\lambda\mu\nu} = -\Sigma^{\mu\lambda\nu}$ (antisymmetric in first two indices, ensuring conservation is preserved). The improvement freedom is parametrized by the choice of $\Sigma^{\lambda\mu\nu}$. The standard ambiguity classes:

- **Belinfante-Rosenfeld:** $\Sigma$ constructed from the spin tensor (vanishes for scalar fields)
- **Hilbert:** $T^{\mu\nu} = (2/\sqrt{-g})\, \delta S/\delta g_{\mu\nu}$; requires variation w.r.t. a fundamental metric
- **Conformal:** for massless scalar in 4D, $\Sigma \sim (\partial_\lambda - g_{\lambda\mu}\partial^\mu)\Psi^2/6$; requires conformal coupling structure

### §2.2 Candidate-by-candidate elimination

Following the scoping memo §2.1 catalog:

**A.2 Belinfante-Rosenfeld improvement** — eliminated. The Belinfante improvement is constructed from the spin tensor $S^{\lambda\mu\nu}$. For substrate-scalar $\Psi$ (§1.1), $S^{\lambda\mu\nu} = 0$ identically; the Belinfante improvement is trivial; A.2 collapses to A.1. The substrate-side spin/gauge content (via Paper_015 T17 rule-type bundles + Paper_098_5/T1 spin-statistics) lives in *separate* substrate-graph structures that enter at continuum via DCGT, not in $\Psi$'s Lorentz-tensor structure at substrate level.

**A.3 Hilbert (metric-variation) tensor** — eliminated. The Hilbert construction requires variation of $S_{\mathrm{sub}}$ with respect to a *background metric* on the substrate graph. **Substrate has no fundamental metric** (Paper_ED_GW_00 §3.2); the only metric structure available is the continuum-side metric emerging from DCGT. The Hilbert construction therefore applies only post-DCGT (where it coincides with the standard Hilbert tensor in continuum GR), not at substrate-side. A.3 is structurally unavailable as a substrate-side candidate.

**A.4 Conformal-coupling improvement** — eliminated. The conformal improvement requires (a) $\Psi$ to be conformally weighted and (b) a substrate-effective scalar curvature for $\Psi$ to couple to. Paper_087's P02 + P04 supply bandwidth and participation content but no substrate-graph conformal weight; SC-4.9 supplies the Hessian structure but no substrate-side scalar curvature. **A.4 is structurally unavailable absent a substrate-graph derivation of conformal weight content**, which Paper_087 does not provide. (If a future substrate-research closure derives substrate-graph conformal weight content from primitives, A.4 would need to be re-examined; for the current corpus it is eliminated.)

**A.5 Non-local kernel-weighted stress-energy** — eliminated under hydrodynamic-window scale-separation. A non-local candidate $T^{\mu\nu}_{\mathrm{non-local}}(x) = \int K_{\ell_{V_1}}(x-y) \cdot [\text{local Noether at } y] \, dy$ collapses to local A.1 evaluated at $x$ at leading order in $\ell_{V_1}/R_{\mathrm{cg}}$ (hydrodynamic-window scale-separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}}$ from Paper_073). The non-local kernel-weighting is therefore equivalent to A.1 at the coarse-graining scale; A.5 is not an independent candidate.

**A.6 Asymmetric / torsion-bearing stress-energy** — eliminated by V1 + V5 Lorentz-covariance. An asymmetric $T^{\mu\nu} \neq T^{\nu\mu}$ would require substrate-graph asymmetry in the Lorentz-tensor structure of $T^{\mu\nu}_{\mathrm{sub}}$. V1 has Lorentz-covariant retarded-kernel structure (Paper_089 §3); V5 has Lorentz-covariant cross-chain coupling (Paper_090). Substrate-side directional content (P09 polarity + P13 translation arrow) enters the *per-chain* chain-arrow direction (Paper_093 T18), which is a substrate-graph object *attached to individual chains*, not a Lorentz-tensor asymmetry in the *bulk substrate stress-energy*. Bulk substrate stress-energy is therefore Lorentz-symmetric; A.6 is structurally unavailable absent substrate-side Lorentz-tensor asymmetry, which the corpus does not supply.

### §2.3 Result: A.1 uniquely surviving

Under the assumptions:
- $\Psi$ is substrate-scalar at SC-4.9 level (§1.1; load-bearing for the argument)
- Substrate has no fundamental metric (Paper_ED_GW_00 §3.2)
- Substrate has no conformal weight content (Paper_087 + Paper_ED_SC_4_9)
- Hydrodynamic-window scale-separation holds (Paper_073)
- V1 + V5 carry Lorentz-covariant kernel structure (Paper_089 §3 + Paper_090)

**A.1 (bare Noether) is the unique surviving candidate.** Conservation holds by construction from P03 + P13 translation invariance. **Q1A closes** at the level of stated assumptions, modulo residual OPEN-i below.

---

## §3 Route Q2A — Coarse-graining invariance uniqueness

Goal: prove B.1 is the unique candidate under DCGT axioms + hydrodynamic-window scale-separation + conservation preservation.

### §3.1 Standard kinetic-theory uniqueness at leading order

The Bensoussan-Lions-Papanicolaou (1978) two-scale homogenization theorem (Paper_095 §2.3 "Always-I" entry) establishes that for scale-separation $\varepsilon = \ell_{\mathrm{micro}}/R_{\mathrm{cg}} \to 0$, the leading-order homogenized continuum stress-energy is **scheme-independent**: different window kernels (Gaussian, Heaviside, sharp-momentum, smooth-bump) produce identical continuum $T^{\mu\nu}_{\mathrm{eff}}$ at $O(\varepsilon^0)$, with differences appearing only at $O(\varepsilon)$ subleading order.

DCGT axiomatically operates in this regime ($\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}}$, Paper_073). Standard homogenization inheritance applies.

### §3.2 Candidate-by-candidate elimination

Following the scoping memo §2.2 catalog:

**B.2 Wilsonian RG-like multi-scale coarse-graining** — eliminated by DCGT axiom specification. DCGT is **single-scale** at $R_{\mathrm{cg}}$ within the hydrodynamic window (Paper_073); Wilsonian RG flow across multiple scales is not the DCGT operation. B.2 lies outside the DCGT axiom set and is therefore not a candidate for "DCGT mapping" — it is a different (Wilsonian) operation. Eliminated as a DCGT mapping.

**B.3 Window-kernel-dependent coarse-graining (Gaussian vs Heaviside vs sharp)** — eliminated at leading order. By the Bensoussan-Lions-Papanicolaou homogenization theorem applied to DCGT's hydrodynamic-window regime, the leading-order continuum stress-energy is window-kernel-independent. Different choices of $W_{R_{\mathrm{cg}}}$ differ only at $O(\varepsilon)$ subleading order. B.3 is therefore eliminated at the leading order relevant for standard continuum-physics inheritance. Subleading scheme-dependence remains; see residual OPEN-ii below.

**B.4 Torsion-introducing coarse-graining** — eliminated by directional-averaging at leading order. Substrate-side directional content lives in *per-chain* chain-arrow directions (Paper_093 T18); the bulk substrate at coarse-graining scale $R_{\mathrm{cg}} \gg \ell_{V_1}$ samples many chains with distributed chain-arrow directions. For isotropic chain distributions, directional content averages to zero at leading order; the surviving continuum structure is the local stress-energy tensor (Lorentz-symmetric), not a torsion bias. For anisotropic chain distributions (e.g., radiation propagation), the directional content is captured by the *flux components* $T^{0i}_{\mathrm{eff}}$ (which are part of standard stress-energy), not by continuum torsion. Continuum torsion would require a *systematic* anti-symmetric structure surviving averaging, which the substrate-graph chain-arrow distribution does not supply. B.4 eliminated at leading order.

**B.5 Non-metricity-introducing coarse-graining** — eliminated by substrate's lack of scale freedom. Weyl-class non-metricity arises from a substrate-side scaling freedom that survives coarse-graining as a continuum scale-rescaling structure. **Substrate-action density per substrate-graph unit is a fixed quantity** (Paper_ED_SC_4_9 + Paper_087 P02 + P12 ED-threshold); no scale-rescaling freedom is supplied by substrate primitives. The continuum scale structure is set by DCGT's window scale $R_{\mathrm{cg}}$, which is an external coarse-graining parameter, not a substrate-side dynamical scale. B.5 is structurally unavailable.

**B.6 Anomalous-trace coarse-graining** — outside DCGT scope. Standard continuum-QFT trace anomalies (Polyakov anomaly; conformal-anomaly-from-regularization) arise from continuum-side renormalization, not from substrate-to-continuum coarse-graining itself. The discrete substrate (Paper_087 + Paper_089 V1 finite-width) supplies natural UV regularization that *replaces* the standard continuum-QFT regulator-induced anomaly; any residual trace anomaly enters the continuum theory through standard continuum-QFT inheritance (post-DCGT), not through DCGT's coarse-graining map itself. B.6 is therefore outside the scope of *DCGT mapping uniqueness* and is absorbed into standard continuum-QFT inheritance as a separate concern (residual OPEN-iii below).

### §3.3 Result: B.1 uniquely surviving (at leading order)

Under the assumptions:
- DCGT axioms hold (Paper_073)
- Hydrodynamic-window scale-separation $\varepsilon = \ell_{\mathrm{ED}}/R_{\mathrm{cg}} \ll 1$
- Substrate has no fundamental scale freedom (no non-metricity source)
- Substrate-graph chain-arrow distribution is averageable at $R_{\mathrm{cg}}$ scale (no systematic torsion source)
- Standard Bensoussan-Lions-Papanicolaou homogenization inheritance applies

**B.1 (standard hydrodynamic mapping) is the unique surviving candidate at $O(\varepsilon^0)$ leading order.** **Q2A closes at leading order**, modulo residual OPEN-ii (subleading scheme-dependence) and OPEN-iii (B.6 trace-anomaly outside DCGT scope).

---

## §4 Residual OPEN items

After Q1A + Q2A construction, three OPEN items remain:

### OPEN-i (load-bearing for Q1A): substrate-scalar $\Psi$ at SC-4.9 level

Q1A's elimination of A.2 (Belinfante) and A.6 (asymmetric) rests on $\Psi$ being substrate-scalar at SC-4.9 level. This is supplied by Paper_087 P02 + Paper_ED_SC_4_9 §2, but is itself a substrate-graph claim about how Paper_087 + SC-4.9 content composes. Specifically: if subsequent substrate-research reveals that $\Psi$ has tensor / spinor / gauge-bundle *internal structure* at substrate-graph level that the current Paper_087 + SC-4.9 reading does not capture, A.2 revives non-trivially and Q1A re-opens.

**Closure path:** explicit substrate-graph audit of $\Psi$'s scalar nature under Paper_087 + Paper_ED_SC_4_9 + Paper_098_5/T1 + Paper_109 composition. Likely closes positively (substrate-action density is structurally a single scalar) but worth verifying.

### OPEN-ii (not load-bearing for leading-order continuum phenomenology): subleading scheme-dependence in Q2A

B.3 elimination holds at $O(\varepsilon^0)$ leading order; subleading $O(\varepsilon)$ corrections are scheme-dependent. For standard continuum-physics inheritance (Friedmann, Larmor, quadrupole formulas at standard cosmological / radiation frequencies), $\varepsilon \sim \ell_{\mathrm{ED}}/R_{\mathrm{cg}} \sim \ell_P/L_{\mathrm{macro}}$ is extraordinarily small; subleading corrections are negligible for all observational purposes.

**Status:** flagged but not load-bearing for the M2 → M3 upgrade. If any specific load-bearing prediction at the corpus level relies on subleading-order DCGT structure, OPEN-ii would re-enter as load-bearing. Currently no such reliance is identified.

### OPEN-iii (outside DCGT scope): trace-anomaly B.6 inheritance

Standard continuum-QFT trace anomalies enter via continuum-side renormalization, not DCGT. The substrate-side discrete UV regulator (Paper_089 V1 finite-width) replaces the standard continuum regulator but the continuum-side trace structure may still inherit standard QFT anomaly content through continuum-side standard inheritance. This is not a DCGT-mapping uniqueness issue; it is a standard continuum-QFT inheritance question.

**Status:** absorbed into standard continuum-QFT inheritance (treated as I in audit-table accounting). Not load-bearing for Q2A's DCGT mapping uniqueness claim.

---

## §5 Elimination summary

### §5.1 Q1A elimination table

| Candidate | Status after Q1A | Eliminating constraint |
|---|---|---|
| A.1 Bare Noether | **SURVIVING** | Conservation holds by P03 + P13 translation invariance |
| A.2 Belinfante-Rosenfeld | ELIMINATED | Substrate-scalar $\Psi$ → spin tensor vanishes → improvement trivial (§2.2; load-bearing on OPEN-i) |
| A.3 Hilbert | ELIMINATED | No fundamental substrate metric (Paper_ED_GW_00 §3.2) |
| A.4 Conformal-coupling | ELIMINATED | No substrate-graph conformal weight content (Paper_087 + SC-4.9) |
| A.5 Non-local kernel-weighted | ELIMINATED | Collapses to A.1 at coarse-graining scale via hydrodynamic-window scale-separation |
| A.6 Asymmetric / torsion-bearing | ELIMINATED | V1 + V5 Lorentz-covariance (Paper_089 §3 + Paper_090); substrate directional content per-chain, not bulk |

### §5.2 Q2A elimination table

| Candidate | Status after Q2A | Eliminating constraint |
|---|---|---|
| B.1 Standard hydrodynamic | **SURVIVING** (at leading order) | DCGT axioms + Bensoussan-Lions-Papanicolaou homogenization inheritance |
| B.2 Wilsonian RG-like | ELIMINATED | Outside DCGT axiom set (single-scale vs multi-scale) |
| B.3 Window-kernel-dependent | ELIMINATED at $O(\varepsilon^0)$ | Bensoussan-Lions-Papanicolaou homogenization (subleading $O(\varepsilon)$ remains; OPEN-ii) |
| B.4 Torsion-introducing | ELIMINATED at leading order | Directional content per-chain not bulk; averages out at $R_{\mathrm{cg}} \gg \ell_{V_1}$ |
| B.5 Non-metricity-introducing | ELIMINATED | No substrate-side scale freedom (Paper_ED_SC_4_9 + P02 + P12) |
| B.6 Anomalous-trace | OUTSIDE DCGT SCOPE | Continuum-QFT trace anomaly enters via continuum-side renormalization, not DCGT mapping; OPEN-iii |

---

## §6 What remains to complete Q1 and Q2

### §6.1 For Q1 full closure

- **Q1A is substantially complete** (A.1 unique under stated assumptions). Residual OPEN-i (substrate-scalar $\Psi$ verification) is load-bearing; closure path is explicit audit of $\Psi$'s scalar nature.
- **Q1B (Route via SC-4.9 Hessian structure)** is not pursued in this memo. Q1A closing makes Q1B's necessity unclear — if A.1 is unique by kernel-symmetry constraints alone, Q1B is either vocabulary-level (the Hessian is the reason kernel-symmetry constraints apply the way they do) or a tightening route that constrains $\mathcal{L}_{\mathrm{sub}}$'s admissible form per regime (different scope; see §6.3 below).

### §6.2 For Q2 full closure

- **Q2A is complete at leading order** (B.1 unique up to scheme-dependent $O(\varepsilon)$ subleading corrections; OPEN-ii + OPEN-iii flagged as outside leading-order load-bearing scope).
- **Q2B (conservation-pinned flux structure)** remains to attempt — partially redundant with Q2A's elimination of B.4 + B.5 via conservation/scale-freedom arguments, but a standalone construction memo would tighten the closure by explicitly showing that energy-momentum conservation under coarse-graining selects the standard Euler / Navier-Stokes hydrodynamic flux structure uniquely.
- **Q2C (metric-compatibility)** remains to attempt — Q2A's elimination of B.4 (torsion) is at leading order via averaging; Q2C would tighten this by showing that DCGT's translation-invariance + Lorentz-covariance preservation forces continuum metric-compatibility structurally, ruling out residual torsion / non-metricity at all orders.

### §6.3 Scope clarification: regime-specific $\mathcal{L}_{\mathrm{sub}}$ content

The original Dyn_02 / Dyn_03 audit qualifications named two concerns that this memo addresses partially:

- **Regime-form correspondence** (RDE → traceless; MDE → dust-like; LDE → vacuum-energy; EM accelerated chain → Poynting; GW time-varying multipole → quadrupole-flux): once **A.1 is unique** for any given $\mathcal{L}_{\mathrm{sub}}$ (Q1A) and **B.1 is unique** for any given substrate stress-energy (Q2A), the regime-specific continuum $T^{\mu\nu}_{\mathrm{eff}}$ is fixed by the choice of $\mathcal{L}_{\mathrm{sub}}$. This memo therefore closes the *construction-uniqueness* aspect of the regime-form correspondence.
- **Regime-class identification** (which substrate states correspond to RDE / MDE / LDE / EM accelerated / GW time-varying source classes): this is *the choice of $\mathcal{L}_{\mathrm{sub}}$ from substrate-graph content*, not the Noether construction from a given $\mathcal{L}_{\mathrm{sub}}$. **Regime-class identification is a separate question, not addressed here.** It corresponds to a different OPEN gap (chain-class criterion) that lives beyond the joint Q1/Q2 closure project as scoped.

**Implication:** the joint Q1/Q2 closure as scoped here is *necessary but possibly not sufficient* for the full Cos_01 + Dyn_02 + Dyn_03 M2 → M3 upgrade. If chain-class identification (regime-form correspondence at the $\mathcal{L}_{\mathrm{sub}}$-choice level) remains OPEN as a separate qualitative-mechanism gap, the M3 upgrade is conditional on closing that gap as well. The scoping-memo Q1/Q2 framing addresses construction uniqueness; the audit-flagged Q1/Q2 framing additionally requires chain-class identification.

This scope mismatch is itself a substantive finding and should be reflected in subsequent paper updates.

---

## §7 Status update + recommended next steps

### Joint Q1/Q2 closure status after this memo

| Sub-gap | Status |
|---|---|
| Q1A (kernel-symmetry uniqueness of Noether) | **Substantially closed under stated assumptions** (5 of 5 alternative candidates eliminated; A.1 unique surviving) |
| Q1A residual OPEN-i (substrate-scalar $\Psi$ verification) | **OPEN; load-bearing for Q1A; closure path explicit** |
| Q2A (coarse-graining invariance uniqueness at leading order) | **Closed at $O(\varepsilon^0)$** (4 of 5 in-scope candidates eliminated; B.1 unique surviving; B.6 outside scope) |
| Q2A residual OPEN-ii (subleading scheme-dependence) | **OPEN but not load-bearing** for leading-order continuum phenomenology |
| Q2A residual OPEN-iii (B.6 trace-anomaly) | **Outside DCGT scope**; absorbed into standard continuum-QFT inheritance |
| Q2B (conservation-pinned flux structure) | Not attempted in this memo; partially redundant with Q2A; standalone closure would tighten |
| Q2C (metric-compatibility) | Not attempted in this memo; tightening route for full all-orders torsion / non-metricity exclusion |
| Q1B (Hessian-structure auxiliary) | Not attempted; Q1A closing makes Q1B's necessity unclear (vocabulary-level vs separate regime-form scope) |
| **Chain-class identification scope-mismatch finding (§6.3)** | **NEW substantive finding; load-bearing for Cos_01 + Dyn_02 + Dyn_03 M3 upgrade** |

### Recommended next steps

**Path-Q1A-Audit:** adversarial audit of this memo's Q1A construction. Verify OPEN-i ($\Psi$ substrate-scalar nature) closes cleanly via Paper_087 + Paper_ED_SC_4_9 + Paper_098_5/T1 composition; check for missed candidate-class members beyond A.1–A.6; counterexample search for kernel-symmetry-respecting non-Noether candidates.

**Path-Q2A-Audit:** adversarial audit of this memo's Q2A construction. Verify Bensoussan-Lions-Papanicolaou inheritance is correctly applied to DCGT's specific window structure; check that B.4 (torsion) averaging argument holds for non-stationary anisotropic chain distributions (radiation case); verify B.5 (non-metricity) lacks substrate-side scale freedom under all primitive content.

**Path-Q2B-Q2C-Construction:** standalone construction memo attempting Q2B (conservation-pinned flux) and Q2C (metric-compatibility all-orders). Would tighten the Q2A closure and rule out residual torsion / non-metricity beyond leading order.

**Path-ChainClass-Scoping (NEW per §6.3):** scoping memo for the regime-form correspondence at the *$\mathcal{L}_{\mathrm{sub}}$-choice* level — i.e., which substrate-graph content selects which $\mathcal{L}_{\mathrm{sub}}$ structure for each regime (RDE/MDE/LDE) and source class (EM accelerated / GW time-varying multipole). This is a load-bearing companion gap that the joint Q1/Q2 closure as construction-uniqueness does not fully address. Recommended priority: HIGH — without it, the Cos_01 + Dyn_02 + Dyn_03 M3 upgrade remains conditional.

**My recommendation:** **Path-Q1A-Audit + Path-Q2A-Audit in parallel**, followed by **Path-ChainClass-Scoping** to address the §6.3 scope-mismatch finding. If audits accept and chain-class scoping identifies tractable closure routes, the M3 upgrade pathway is clear. If chain-class scoping reveals it requires substrate-research-frontier work (analogous to Route A in difficulty), the M2 → M3 upgrade is honestly contingent on a longer-horizon program.

### Cross-program impact

**Best-case outcome (Q1A + Q2A audits accept + ChainClass scoping finds tractable closure):**
- Cos_01 + Dyn_02 + Dyn_03 upgrade M2 → M3 simultaneously
- GW_00 row 12 closes fully on form aspect (coefficient OPEN still)
- Cos_05 draftable at M3 conditional on Route A only

**Mid-case outcome (Q1A + Q2A audits accept; ChainClass scoping reveals substrate-research-frontier work):**
- Construction-uniqueness gap closed; chain-class identification gap re-opens as the new load-bearing OPEN for M3 upgrade
- The M2 → M3 upgrade is honestly contingent on the new gap closing
- Substrate-ontology characterization sharpens: substrate ontology supports construction uniqueness via existing primitives, but chain-class identification requires separate substrate-research-frontier work

**Worst-case outcome (Q1A or Q2A audits identify defeating counterexample):**
- Construction-uniqueness gap remains open; substrate-ontology characterization sharpens further (substrate primitives don't supply construction uniqueness; standard-physics-analog inheritance is genuinely load-bearing)
- M2 verdict permanent for the affected papers; honest corpus contribution

All three outcomes are corpus-informative. **No outcome wastes the construction effort.**

---

**End Memo_ED_Q1Q2_JointClosure_Construct.**
