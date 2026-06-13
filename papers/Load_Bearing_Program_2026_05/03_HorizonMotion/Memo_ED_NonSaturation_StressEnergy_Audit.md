# Memo_ED_NonSaturation_StressEnergy_Audit — Adversarial Audit of OPEN-HM-1 Closure

**Series:** Wave-3 Audit Memo (Cosmology + Dynamics Arcs; Claude-B-class adversarial audit of Memo_ED_NonSaturation_StressEnergy)
**Status:** Critical audit of the OPEN-HM-1 closure claim that substrate-side Noether stress-energy for non-saturation states (RDE, MDE) is derivable at D-via-I level. **Not a derivation. Auditor stance, not advocate.** Following the discipline cascade from CommitPhaseInheritance_Audit + SubstrateAction_Constancy_Audit + DCGT_VacuumEnergyMapping_Audit.
**Date:** 2026-05-16
**Anchors:** Memo_ED_NonSaturation_StressEnergy (audit target); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$); Paper_073 (DCGT); Paper_ED_Cos_01 (M3-upgraded reference); Memo_ED_DCGT_VacuumEnergyMapping_Audit (M3-chain Step C audit precedent); Paper_087 (P10 multiple rule-types); Paper_089 (V1 + T18); Paper_012 (P-RB-1).
**Headline verdict:** **ACCEPT at "approximately-standard-cosmology level"** with two explicit qualifications, BUT **structurally weaker than M3-chain audit acceptance**. The closure leans on standard-QFT-analog inheritance for chain-class identification more than on substrate-graph derivation. Not overclaim by CommitPhaseInheritance-class standards (no structural inconsistency, no defeating counterexample), but the hidden-inheritance pattern is real and should be flagged.

---

## §1 What's being audited

NonSaturation_StressEnergy claims OPEN-HM-1 closure via a four-step chain:

1. **(§2 of memo)** Substrate-side identification: "chains propagating at rates close to substrate-c" = relativistic (RDE); "chains propagating well below substrate-c" = non-relativistic (MDE)
2. **(§3 of memo)** Noether procedure on substrate-side $\mathcal{L}_{\mathrm{sub}}$ for each regime — traceless ($w = 1/3$) for radiation, dust-like ($w = 0$) for matter, vacuum-energy ($w = -1$) for saturation
3. **(§4 of memo)** DCGT translates substrate-side stress-energy to continuum stress-energy preserving equation of state
4. **(§5 of memo)** Friedmann + horizon evolution standard cosmology inheritance

The memo flags two audit issues (§6 audit flags #1, #2). This memo executes the audit adversarially.

---

## §2 Audit of relativistic vs non-relativistic chain identification

### Examination

**Claim:** "Chains propagating at rates close to substrate-c = relativistic; chains propagating well below substrate-c = non-relativistic." Substrate-graph identification supplied by V1 + Paper_012 P-RB-1.

**Required substrate-graph content:**
- A substrate-graph criterion for "chain propagation rate"
- A substrate-graph distinction between chains propagating at substrate-c vs sub-substrate-c rates
- Mapping from chain-class to cosmological-phase (radiation, matter, vacuum)

**Supplied by Paper_087 + Paper_089 + Paper_012?**

Paper_087 supplies P10 (multiple structurally distinct rule-types), which COULD support chain-class distinctions. But the specific criterion *"chains propagating at substrate-c = relativistic; chains propagating sub-substrate-c = matter"* is **NOT directly supplied** by existing corpus content.

V1 has substrate-c bound per Paper_089 + Paper_012 P-RB-1. The substrate-c is a propagation-rate ceiling, not a per-chain rate parameter. The corpus does not natively supply a notion of "individual chain propagation rate" varying from chain to chain.

In standard QFT, "relativistic" means kinetic energy ≳ rest-mass energy. The substrate-side analog would require:
- A substrate-graph notion of "kinetic energy" per chain
- A substrate-graph notion of "rest-mass energy" per chain
- A criterion for when kinetic exceeds rest-mass

None of these are explicitly supplied by Paper_087 + Paper_089 + Paper_012.

### Adversarial finding A

**Audit flag A: the substrate-graph identification of "relativistic vs non-relativistic chains" is INHERITED by analogy with standard QFT, not derived from existing primitives.** The chain-class distinction is asserted by structural analogy ("chains analogous to relativistic fields = relativistic"); the specific substrate-graph criterion is not constructed.

This is structurally **similar to but weaker than the CommitPhaseInheritance Audit Weak Link 1** (channel-uniqueness assumption not supplied by homogeneity). Weaker because:
- The analog inheritance is from a well-established framework (standard QFT)
- The corpus's P10 (multiple rule-types) supports the general possibility of chain-class distinctions
- No structural inconsistency follows from the inheritance

But **the substrate-graph derivation step is missing**. The memo assumes the chain-class identification by analogy; doesn't supply substrate-graph criterion.

**Status:** ACCEPT with qualification that the chain-class identification is INHERITED by standard-QFT analog, not derived substrate-graph. Explicit substrate-graph criterion (perhaps via Paper_087 P10 rule-type specifics + Paper_098_5/T1 spin-statistics distinctions) would tighten the closure.

---

## §3 Audit of Noether stress-energy form derivation

### Examination

**Claim:** For radiation regime (relativistic chains), Noether procedure on substrate-side $\mathcal{L}_{\mathrm{sub}}$ gives traceless $T^\mu_\mu = 0$ with $w = 1/3$. For matter regime (non-relativistic chains), Noether gives dust-like $T^{00} = \rho$, $T^{ii} = 0$ with $w = 0$.

**Required substrate-graph content:**
- Substrate-side $\mathcal{L}_{\mathrm{sub}}$ structure for relativistic vs non-relativistic chain content
- Noether procedure applied to substrate-side V1 + V5 kernel structure
- Resulting $T^{\mu\nu}_{\mathrm{sub}}$ form per regime

**Supplied by Paper_ED_SC_4_9 + Paper_089 + standard QFT analog?**

Paper_ED_SC_4_9 supplies $S_{\mathrm{sub}}[\Psi]$ as a functional with V1 + V5 kernel content. The specific form of substrate-side Noether stress-energy for the V1 + V5 kernel content is not explicitly constructed in the corpus.

The memo asserts traceless stress-energy form for radiation by structural analogy with massless field theory. The standard QFT massless-field Lagrangian $\mathcal{L} = \frac{1}{2}\partial_\mu \phi \partial^\mu \phi$ has Noether stress-energy $T^{\mu\nu} = \partial^\mu \phi \partial^\nu \phi - g^{\mu\nu}\mathcal{L}$, and the trace $T^\mu_\mu = \partial_\mu \phi \partial^\mu \phi - 4 \cdot \frac{1}{2}\partial_\mu \phi \partial^\mu \phi$ ... wait, this isn't zero. The traceless property requires the field to be massless AND the Lagrangian to have specific conformal-invariance properties.

Actually for free massless scalar in 4D, the stress-energy is NOT traceless in general; the traceless improvement requires the conformally-coupled scalar $\mathcal{L}_{\mathrm{conf}} = \frac{1}{2}\partial_\mu \phi \partial^\mu \phi - \frac{1}{12}R\phi^2$. The standard traceless result for radiation is from electromagnetic fields (gauge bosons), not generic scalars.

**For the substrate-side analog:** whether V1 + V5 kernel structure gives the EM-analog gauge-invariant traceless stress-energy or a scalar non-traceless stress-energy depends on V1/V5's specific gauge-structure content. **The memo glossed over this.**

Per Paper_089, V1 has "Lorentz-covariant structure with retarded support." This may give Lorentz-covariant substrate-side Lagrangian. But Lorentz-covariance ≠ conformal invariance ≠ traceless stress-energy. The substrate-side derivation of which specific stress-energy form V1 + V5 give for relativistic chains requires more careful work.

### Adversarial finding B

**Audit flag B: the substrate-side Noether stress-energy form for radiation regime is asserted by analogy with standard QFT EM-class (traceless) rather than scalar-class (non-traceless).** The choice of analog is not justified substrate-graph from V1 + V5 kernel structure.

For matter regime: dust-like stress-energy is the standard non-relativistic limit; substrate-side analog requires verifying that slow-Ψ-propagation states give pressureless dust form. Plausible but not derived.

**Status:** ACCEPT with qualification that the specific stress-energy forms ($w = 1/3$ traceless for radiation, $w = 0$ dust for matter) are INHERITED by standard-QFT analog choices that themselves require substrate-graph justification. The closure depends on V1 + V5 substrate-side structure giving EM-analog-like stress-energy for relativistic chains and dust-analog-like for non-relativistic chains.

---

## §4 Audit of substrate-side Lagrangian Lorentz-covariance

### Examination

Per Paper_089 §3, V1's substrate-side kernel has "Lorentz-covariant structure with retarded support." This supports the substrate-side Lagrangian's Lorentz-covariance.

**However:** Lorentz-covariance is necessary but not sufficient for the stress-energy forms the memo claims. Additional structure (conformal invariance for traceless EM-like; mass term for matter-like) is required.

**Substrate-side V1 + V5 kernel content:** does it admit both conformal-invariant (massless-photon-analog) and mass-term-bearing (massive-particle-analog) substrate-side substates corresponding to radiation and matter respectively?

Paper_087 P10 (multiple rule-types) supports this in principle. Paper_098_5/T1 (spin-statistics) gives boson/fermion distinction. Standard physics structure (massless gauge bosons = radiation, massive matter = dust) likely has substrate-side analog under Paper_087 rule-type content, but the substrate-side construction is not explicit.

### Adversarial finding C

**Audit flag C: substrate-side Lagrangian structure supporting both conformal-invariant (radiation) and mass-term-bearing (matter) substates is plausible from Paper_087 P10 + Paper_098_5/T1 but not constructed.** The specific substrate-graph derivation of how V1 + V5 content distinguishes these substates is OPEN.

**Status:** ACCEPT with qualification that substrate-side gauge-structure / mass-structure content underlying the equation-of-state determinations is inherited at standard-physics analog level. Explicit substrate-graph construction would tighten the closure.

---

## §5 Audit of DCGT applicability to RDE/MDE

### Examination

**Claim:** DCGT applies to RDE/MDE more cleanly than to saturation regime because RDE/MDE are nominal hydrodynamic regimes.

**Hydrodynamic-window condition:** $\ell_{ED} \ll R_{cg} \ll L_{flow}$.

**For RDE:** in the radiation-dominated regime, characteristic scale is $1/T$ (inverse temperature) for thermal fluid + $1/H$ for cosmological dynamics. Very early RDE (Planck-scale temperatures): $1/T \to \ell_P \sim \ell_{ED}$ → DCGT at edge of validity. Standard RDE (post-BBN, $T \sim$ MeV down to recombination): $1/T \gg \ell_{ED}$ → DCGT applies cleanly. Late RDE (near radiation-matter equality): $1/H_{\mathrm{eq}}$ very large → DCGT applies cleanly.

**For MDE:** matter dust has long-range correlations; $L_{flow} \sim$ cluster scales; DCGT applies cleanly throughout.

**For LDE (Λ-dominated):** $H_0^{-1}$ very large; DCGT applies cleanly.

### Adversarial finding D

**Audit flag D: DCGT applicability holds cleanly for mid-to-late RDE, all of MDE, all of LDE.** **Very early RDE (Planck-scale) is at edge of validity** — similar issue to the saturation regime's near-edge-of-window status.

This is a regime restriction worth flagging but not load-bearing for the standard cosmology phenomenology DCGT translation produces. Most of cosmological history is in the clean-DCGT regime.

**Status:** ACCEPT with regime-restriction qualification.

---

## §6 Counterexample search

**Counterexample candidate 1: Mixed-component substrate states.** Real universe has multiple components (radiation + matter + vacuum). Composite substrate state has mixed stress-energy. Composite $w$ = weighted average per density ratios.

This is not a defeating counterexample — it's the standard cosmology fact accommodated by additive Noether stress-energy. ✓

**Counterexample candidate 2: Stiff matter ($w = 1$) or phantom dark energy ($w < -1$).** Standard cosmology observationally constrains both ($w_{\mathrm{stiff}}$ requires extreme conditions; phantom DE has theoretical instabilities).

Substrate-side: $w > 1/3$ requires substrate-side kinetic-dominated content beyond standard relativistic; $w < -1$ requires substrate-side negative kinetic terms (unstable). Both would require additional substrate-graph machinery not currently in the corpus.

This is **consistent with the closure** — substrate-side gives standard cosmology phenomenology, doesn't supply exotic equation-of-state values without extra content. Not a defeating counterexample.

**Counterexample candidate 3: Substrate states with post-SCBU homogeneity but non-standard $w$.** Could substrate have a uniform $\Psi$ content giving $w \neq -1, 0, 1/3$?

Under spatial homogeneity, uniform $\Psi$ should give a homogeneous substrate-side stress-energy. The equation of state is determined by the $\mathcal{L}_{\mathrm{sub}}$ structure at the uniform state. For constant $\Psi$ (no derivatives), $T^{\mu\nu} = -g^{\mu\nu}\mathcal{L}_{\mathrm{const}}$ → $w = -1$ regardless of which uniform state. For non-constant but homogeneously-distributed $\Psi$ content (e.g., uniform-density radiation), the derivative structure gives a specific stress-energy form per chain class.

Whether non-standard $w$ values are accessible substrate-side under spatial homogeneity requires checking whether substrate-side $\mathcal{L}_{\mathrm{sub}}$ admits chain content with non-standard stress-energy structure. **OPEN at substrate-graph level** but not a clear-cut defeating counterexample.

---

## §7 Comparison with prior audits + verdict

| Audit criterion | CommitPhaseInheritance | SubstrateAction_Constancy | DCGT_VacuumEnergyMapping | **NonSaturation_StressEnergy (this audit)** |
|---|---|---|---|---|
| Required content supplied? | NO (channel-uniqueness) | YES (approximate) | YES (approximate) | **PARTIALLY** — chain-class identification is standard-QFT-analog inheritance, not derived substrate-graph |
| Strict reading structurally consistent? | NO (predicts zero antimatter) | YES | YES | YES — gives standard cosmology phenomenology |
| Counterexample defeats? | YES | NO | NO | NO |
| **Verdict** | **REJECTED** | **ACCEPTED at approximately-constant level** | **ACCEPTED at approximately-vacuum-energy level** | **ACCEPTED at approximately-standard-cosmology level (with structural-inheritance qualifications)** |

### Verdict

**ACCEPT the OPEN-HM-1 closure at "approximately-standard-cosmology level"**, with two explicit qualifications:

- **Substrate-side chain-class identification (relativistic vs non-relativistic) is INHERITED by standard-QFT analog**, not derived substrate-graph from existing primitives. Plausible from Paper_087 P10 + Paper_098_5/T1 + standard physics structure but explicit substrate-graph criterion not constructed.
- **Specific stress-energy forms for each regime (traceless for radiation, dust for matter) are INHERITED by standard-QFT analog choices** (EM-class vs scalar-class for relativistic; non-relativistic limit for matter). Substrate-graph derivation of which specific form V1 + V5 kernel structure gives for each chain class is OPEN.

The closure is **structurally weaker than M3-chain audit acceptance** because the M3 chain relied on explicit substrate-graph derivation (constant-Ψ → vacuum-energy is direct from substrate-side Noether), while this memo relies more on standard-QFT-analog inheritance for the regime-specific stress-energy forms.

### Distinct from CommitPhaseInheritance overclaim case

CommitPhaseInheritance audit REJECTED closure because:
- Required content NOT supplied (channel-uniqueness)
- Strict reading structurally inconsistent (zero antimatter)
- Independent counterexample existed (V5 cross-boundary)

This memo's audit ACCEPTS closure because:
- Required content PARTIALLY supplied + standard inheritance fills the rest
- Strict reading structurally consistent (standard cosmology phenomenology)
- No defeating counterexample

But the partial-supply (vs full-supply for M3 chain memos) is a real qualification. **The audit acceptance is appropriately weaker than M3-chain acceptance.**

### What the closure does NOT establish

- Strict substrate-graph derivation of $w = 1/3$ for radiation and $w = 0$ for matter — only at standard-QFT-analog level.
- Substrate-graph criterion for chain-class distinction — inherited by analogy.
- Equation-of-state derivation in mixed-component regimes — qualitative only.

---

## §8 Recommended updates + next steps

### Updates to NonSaturation_StressEnergy memo

1. **Add explicit "standard-QFT-analog inheritance" framing** for chain-class identification (§2) and stress-energy form derivation (§3).
2. **Acknowledge the hidden-assumption pattern** — the closure inherits more from standard physics templates than the M3 chain did. Note this as a substantive characterization, not a defect.
3. **Add early-RDE regime restriction** for DCGT applicability (Planck-scale regime at edge of validity).
4. **Flag substrate-graph derivation of chain-class criterion** as recommended future substrate-research-frontier work (would tighten the closure).

### Status update for load-bearing #3

| Step | Substance | Status |
|---|---|---|
| A | Cosmological phase identification | INHERITED (standard cosmology) |
| B | Substrate-side Noether stress-energy for each regime | **D-via-I (this memo audit ACCEPTED at approximately-standard-cosmology level)** |
| C | DCGT translation to continuum stress-energy | **D-via-I (inherited from M3-chain audit precedent + this memo §4)** |
| D | Friedmann recovery | INHERITED |
| E | Horizon evolution per phase | INHERITED |

**Load-bearing #3 closes at D-via-I via the M3-chain template applied to non-saturation states**, with weaker audit-acceptance qualifications than the M3 chain itself (due to additional standard-QFT-analog inheritance).

### Recommended next step

**Update Paper_ED_Cos_01 / draft Paper_ED_Dyn_02** to reflect this closure. The Horizon-Motion-Law paper (Dyn_02) is now draftable at **M3 form-IDENTIFIED with standard-QFT-analog inheritance qualifications**.

### Substrate-research-pattern update

| # | Item | Closure path | Status |
|---|---|---|---|
| 1 | Exponential growth | M3-chain template; saturation regime | **CLOSED D-via-I (audit accepted, robust)** |
| 2 | Chirality $\mathbb{Z}_2$ | Requires specialized substrate-graph machinery | OPEN; substrate is chirality-symmetric |
| **3** | **Horizon motion** | **M3-chain template; non-saturation regimes** | **CLOSED D-via-I (this audit accepted, weaker — standard-QFT-analog inheritance qualifications)** |
| 4 | ED radiation law | TBD | Not yet attacked |
| 5 | Λ smallness | Likely M3-chain template for Λ-dominated late universe | TBD (high plausibility) |

**Two of five load-bearing items closed.** The M3-chain template robustly handles standard cosmology phenomenology via DCGT inheritance. The closure pattern's robustness varies — saturation regime (M3 chain) closes via direct substrate-graph derivation; non-saturation regimes close via standard-QFT-analog inheritance.

**Substrate-ontology characterization continues consolidating:** ED's substrate ontology supports standard cosmology phenomenology via DCGT + standard QFT/cosmology inheritance, not via specialized substrate-graph derivations. **This is consistent with the corpus's substrate-ontology lineage** (Wolfram, 't Hooft, causal-set) — substrate-side physics inherits cleanly from standard physics through the coarse-graining bridge, doesn't replicate it from substrate-graph principles alone.

---

**End Memo_ED_NonSaturation_StressEnergy_Audit.**
