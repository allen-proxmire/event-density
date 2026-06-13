# Memo_ED_DCGT_VacuumEnergyMapping_Audit — Adversarial Audit of OPEN-3 Closure

**Series:** Wave-3 Audit Memo (Cosmology Arc; inflation sub-thread; Claude-B-class adversarial audit of Memo_ED_DCGT_VacuumEnergyMapping)
**Status:** Critical audit of the OPEN-3 closure claim that DCGT translates approximately-constant substrate-action density into approximately-constant vacuum-energy-like continuum stress-energy with $w \approx -1$. **Not a derivation. Auditor stance, not advocate.** Following the discipline lesson from Memo_ED_CommitPhaseInheritance_Audit + Memo_ED_SubstrateAction_Constancy_Audit.
**Date:** 2026-05-16
**Anchors:** Memo_ED_DCGT_VacuumEnergyMapping (audit target); Paper_073 (DCGT); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ functional); Paper_ED_Cos_01 §3.3–§3.5; Memo_ED_SubstrateAction_Constancy + Audit (audited OPEN-1 closure); Paper_087 (P03 + P13 substrate-translation invariance).
**Headline verdict:** **ACCEPT at "approximately vacuum-energy" level**, with three explicit qualifications. The closure is not overclaim — it operates at the same level of approximation standard cosmology slow-roll inflation uses, parallel to the OPEN-1 audit acceptance pattern. **Distinct from CommitPhaseInheritance overclaim case.** M3 substrate-graph chain Steps A–C now D-via-I closed at audited approximate level; **Paper_ED_Cos_01 row 13 closes**; verdict M2 → M3 retroactive upgrade supported.

---

## §1 What's being audited

DCGT_VacuumEnergyMapping claims OPEN-3 closure via a six-step substrate-graph chain (its §3–§5):

1. $S_{\mathrm{sub}}[\Psi]$ has Lagrangian-density structure (Paper_ED_SC_4_9)
2. P03 + P13 supply substrate-translation invariance for Noether procedure
3. Noether stress-energy substrate-side constructible: $T^{\mu\nu}_{\mathrm{sub}}$
4. For constant $\Psi$ (per OPEN-1 audited): $T^{\mu\nu}_{\mathrm{sub}} \approx -g^{\mu\nu}\rho^{\mathrm{const}}$
5. DCGT coarse-graining preserves uniform stress-energy form
6. Continuum $T^{\mu\nu}_{\mathrm{eff}} \approx -g^{\mu\nu}_{\mathrm{eff}}\rho^{\mathrm{const}}$, $w \approx -1$

The memo flags three audit issues (§6): substrate-side Noether procedure, DCGT preservation, dissipative-vs-Lagrangian translation.

This memo executes the audit adversarially.

---

## §2 Audit of discrete-Noether step (flag #1)

### Examination

**Claim:** Substrate-translation invariance (P03 spatial homogeneity + P13 time-homogeneity) supports a Noether-procedure-analog producing a substrate-side stress-energy tensor.

**Standard Noether** requires *continuous* symmetry (e.g., spacetime translation $x^\mu \to x^\mu + \epsilon^\mu$). The conserved current is $T^{\mu\nu}$.

**Substrate-graph translation is discrete** (loci are discrete points; substrate-time advances in discrete commitment events). Strict continuous-symmetry Noether does not apply directly.

**Standard lattice-field-theory analog:** discrete translation symmetry on a lattice gives discrete conservation laws (lattice Ward identities) producing a lattice stress-energy tensor that:
- Is defined via discrete differences (not derivatives)
- Satisfies discrete divergence conservation $\Delta_\mu T^{\mu\nu}_{\mathrm{lat}} = 0$
- Converges to continuum Noether $T^{\mu\nu}$ in the continuum limit

The substrate-graph analog should follow this template via DCGT supplying the continuum limit. **But this is inheritance from standard lattice-field-theory, not a substrate-graph derivation specific to ED.**

### Adversarial finding

**Audit flag #1: substrate-graph derivation of the discrete-Noether substrate-side stress-energy tensor is INHERITED from standard lattice-field-theory, not explicitly constructed in the corpus.** The inheritance is structurally clean (substrate-graph has the required discrete-translation symmetry per P03 + P13; lattice-field-theory Noether is well-established), but the explicit substrate-graph construction would tighten the closure.

For audit purposes: the inheritance is acceptable at the same level the corpus inherits other standard mathematical content (DCGT itself inherits diffusion/coarse-graining theory; Born rule inherits standard probability machinery). **Not overclaim** — it's standard inheritance of well-established mathematical machinery.

**Status:** ACCEPT with qualification that explicit substrate-graph discrete-Noether construction would tighten the closure.

---

## §3 Audit of DCGT preservation of uniform stress-energy (flag #2)

### Examination

**Claim:** DCGT coarse-graining of uniform substrate-side stress-energy preserves the vacuum-energy form $T^{\mu\nu} = -g^{\mu\nu}\rho$ at continuum side.

**For genuinely uniform content:** coarse-graining is averaging; averaging uniform content gives uniform averaged content; uniform vacuum-energy form is preserved. **Trivially true.** ✓

**For approximately-uniform content (realistic ignition regime per OPEN-1 audit):** small fluctuations exist; coarse-graining averages over these. The averaged stress-energy may have small deviations from strict vacuum-energy form.

In standard hydrodynamics-from-microscopics (BBGKY hierarchy, Chapman–Enskog expansion), coarse-graining preserves energy-momentum conservation but can introduce dissipative corrections to the stress-energy tensor. For uniform background + small fluctuations:
- Zeroth-order (uniform): preserves vacuum-energy form
- First-order (fluctuations): introduces small deviations, typically dissipative

### Adversarial finding

**Audit flag #2: for uniform-saturation states, DCGT preservation of vacuum-energy form is trivially true; for non-uniform states (realistic ignition regime), small deviations from vacuum-energy form exist via standard coarse-graining corrections.** These deviations are exactly the same order as the OPEN-1 audited "approximately-constant" qualifications.

**Status:** ACCEPT at approximately-vacuum-energy level. Strict-uniform vacuum-energy preservation holds; realistic-regime small deviations match standard cosmology slow-roll inflation phenomenology (small deviations from $w = -1$ are the source of observable primordial fluctuation spectrum's small red tilt).

---

## §4 Audit of diffusion-form continuum vs vacuum-energy $w \approx -1$ (flag #3)

### Examination

**Tension:** DCGT produces continuum equations of *diffusion-form* (potentially dissipative). Standard Lagrangian field theory gives *non-dissipative* dynamics with conserved Noether stress-energy. Vacuum-energy form $T^{\mu\nu} = -g^{\mu\nu}\rho$ is non-dissipative.

**Are these compatible?**

Standard physics resolution: microscopic dynamics is Lagrangian (non-dissipative); coarse-graining introduces dissipation as an emergent feature at continuum scale; continuum stress-energy is the *coarse-grained* substrate-side stress-energy, not constructed from continuum-side Lagrangian. The continuum-side equations of motion are dissipative; the continuum-side stress-energy can be near-conserved with small dissipative corrections.

**For uniform-saturation states:** no gradients → no diffusion currents → no dissipation. Continuum-side stress-energy from coarse-grained substrate-side stress-energy is approximately vacuum-energy form without dissipative corrections.

**For non-uniform states:** gradients drive diffusion currents → dissipation → continuum-side stress-energy has small deviations from vacuum-energy form. Equation of state deviates slightly from $w = -1$.

### Adversarial finding

**Audit flag #3: the dissipative-vs-Lagrangian tension is structurally real but vanishes for uniform-saturation states (no gradients → no dissipation).** For non-uniform realistic ignition, small deviations from $w = -1$ exist via standard coarse-graining dissipative corrections.

**Cross-reference with standard cosmology:** standard slow-roll inflation also has $w$ slightly different from $-1$ (specifically: $w = -1 + (2/3)\epsilon$ where $\epsilon$ is the slow-roll parameter). This deviation is what produces the observable spectral tilt. The substrate-side analog has the same structure.

**Status:** ACCEPT at $w \approx -1$ level. Strict $w = -1$ for uniform; small deviations for non-uniform consistent with standard slow-roll phenomenology.

---

## §5 Hidden-assumption search (parallel to CommitPhaseInheritance)

CommitPhaseInheritance overclaim had three weak links:
1. Channel-uniqueness conflated with spatial homogeneity (hidden assumption not supplied by corpus)
2. Strict reading predicts zero antimatter (structural inconsistency)
3. V5 cross-boundary supplies alternative phase reference (independent counterexample)

**Does DCGT_VacuumEnergyMapping have analogous problems?**

### Hidden-assumption check

| Required content | Supplied by corpus? |
|---|---|
| Substrate-translation invariance | P03 + P13 ✓ |
| Lagrangian structure of $S_{\mathrm{sub}}$ | Paper_ED_SC_4_9 ✓ |
| Discrete-Noether stress-energy | Standard lattice-field-theory inheritance ✓ (with audit flag #1 qualification) |
| DCGT preservation of uniform content | Trivially true for uniform; standard hydrodynamics for non-uniform ✓ |
| Vacuum-energy form from constant Lagrangian | Standard QFT inheritance ✓ |
| $g^{\mu\nu}_{\mathrm{eff}}$ continuum metric | Supplied by DCGT coarse-graining (with substrate-graph derivation details not explicit but inheritable) |

**No hidden assumption analogous to CommitPhaseInheritance's channel-uniqueness identified.** All required content is supplied by corpus + standard mathematical inheritance.

### Structural-inconsistency check

**Does strict reading predict an empirically false consequence?**

Strict reading: uniform-saturation substrate gives strict vacuum-energy continuum stress-energy with $w = -1$ → de Sitter exponential growth.

This MATCHES standard cosmology inflation phenomenology. **No empirical inconsistency.** Standard cosmology slow-roll inflation operates at the same approximation level (approximately $w = -1$).

No structural inconsistency parallel to CommitPhaseInheritance's "zero antimatter."

### Independent counterexample search

**Counterexample candidate 1: Substrate states with constant $\Psi$ but non-uniform Hessian eigenvalue spectrum.** Under strict reading (homogeneity → uniform substrate), this is excluded. Under approximate reading (with fluctuations), small Hessian variations contribute to small stress-energy deviations from vacuum-energy form. These are the source of primordial fluctuations — consistent with observation, not a defeating counterexample.

**Counterexample candidate 2: DCGT regimes where coarse-graining produces non-Lagrangian effective dynamics that doesn't admit clean stress-energy.** Per Paper_073, DCGT applies in hydrodynamic window. Outside that window, stress-energy translation may break down. For uniform-saturation states within DCGT window (per OPEN-1 audit §5), the translation holds.

**Counterexample candidate 3: Substrate-side dissipation from V1 finite-width that doesn't cleanly translate.** V1 retarded propagation is non-dissipative at substrate-graph level (V1 transports content forward; doesn't produce entropy locally). Coarse-grained dissipation arises from V1's coarse-graining at scales $R_{cg} \gtrsim \ell_{V_1}$, not from V1 itself. For uniform-saturation, V1 coarse-graining is trivial; no dissipation introduced.

**No counterexample defeats the approximately-vacuum-energy reading.**

---

## §6 Verdict

**ACCEPT the OPEN-3 closure at "approximately vacuum-energy" level**, with three explicit qualifications:

- **Strict $w = -1$ for uniform-saturation;** small deviations for non-uniform realistic ignition consistent with standard slow-roll inflation phenomenology (substrate-side source of primordial fluctuation spectrum's spectral tilt).
- **Discrete-Noether substrate-graph derivation INHERITED from standard lattice-field-theory** rather than explicitly constructed; explicit substrate-graph construction would tighten the closure but is not required for current closure level.
- **DCGT applies within hydrodynamic window** per Paper_073 + ED_MEMORY; uniform-saturation states are within this window per OPEN-1 audit §5.

These qualifications match the **same level of approximation standard cosmology slow-roll inflation uses.** The closure is acceptable at this level.

### Distinct from CommitPhaseInheritance overclaim case

CommitPhaseInheritance audit REJECTED closure because:
- Required assumption (channel-uniqueness) was NOT supplied by corpus
- Strict reading was structurally INCONSISTENT with framework (predicted zero antimatter)
- Independent counterexample existed (V5 cross-boundary alternative phase reference)

This memo's audit ACCEPTS closure because:
- All required content IS supplied by corpus + standard inheritance
- Strict reading is structurally CONSISTENT with framework + empirical observation
- No counterexample defeats approximate reading

**Pattern:** the constancy + vacuum-energy closures (OPEN-1 + OPEN-3) follow standard QFT / standard cosmology templates applied to substrate-side analogs. They use standard mathematical inheritance, not specialized substrate-graph derivations that need to close from existing primitives alone. **The audit-acceptance reflects standard-physics-inheritance robustness, not substrate-graph-derivation novelty.**

### What the closure does NOT establish

- Strict (exactly $w = -1$) vacuum-energy continuum content. Only approximately.
- Constancy / vacuum-energy form during regime start/end transitions. Only bulk-of-regime.
- Quantitative substrate-graph derivation of $\rho_{\mathrm{eff}}^{\mathrm{const}}$ value. OPEN-4 territory.
- Quantitative substrate-graph derivation of $H$ value. OPEN-4 territory.

These limitations should be explicitly flagged in the updated DCGT_VacuumEnergyMapping memo.

---

## §7 Status update for M3 substrate-graph chain

| Step | Substance | Status |
|---|---|---|
| A | Saturation regime structure | INHERITED (Paper_ED_Cos_01 §3.3) |
| B | Substrate-action density constancy | **D-via-I (OPEN-1, audit ACCEPTED at approximate level)** |
| C | DCGT translation to vacuum-energy continuum | **D-via-I (OPEN-3, this audit ACCEPTED at approximate level)** |
| D | Friedmann recovery → constant $H$ | INHERITED (standard cosmology) |
| E | $a(t) \propto e^{Ht}$ | INHERITED (standard cosmology de Sitter) |

**M3 substrate-graph chain Steps A–E now established at audited approximate level.** Steps A, D, E are standard inheritance; Steps B, C are D-via-I closures with audit-accepted approximate-level qualifications.

**Paper_ED_Cos_01 row 13 closes at D-via-I substrate-graph derivation, at the same approximation level standard cosmology slow-roll inflation operates at.**

### Implications for Paper_ED_Cos_01

1. **Row 13 OPEN → D-via-I closed** at approximate level (referencing OPEN-1 + OPEN-3 audited closures).
2. **Verdict M2 → M3 retroactive upgrade** is supported by the closure. Inflation paper becomes form-IDENTIFIED + value-INHERITED at M3 level.
3. **Row 16 (qualitative spectral character) becomes partially closable** — primordial fluctuations are the small deviations from uniform-saturation that this audit identified. Substrate-side reading: deviations from $w = -1$ via standard coarse-graining are the substrate-side source of primordial fluctuation spectrum.
4. **OPEN-4 (quantitative $H$) and row 17 (quantitative $n_s$, $r$, $N$) remain.** These are quantitative consolidations, not load-bearing for qualitative M3 closure.

---

## §8 Recommended updates + next steps

### Updates to DCGT_VacuumEnergyMapping memo

1. **Explicit "approximately vacuum-energy" framing** throughout — replace "vacuum-energy" with "approximately vacuum-energy" where appropriate.
2. **Add qualification subsection** noting:
   - Strict $w = -1$ for uniform-saturation; small deviations for non-uniform realistic regime
   - Discrete-Noether inheritance from standard lattice-field-theory
   - DCGT hydrodynamic-window applicability
   - Cross-reference to standard slow-roll inflation as analogous-level closure
3. **Connect to Paper_ED_Cos_01 row 16** — primordial fluctuations as substrate-side source of small deviations from $w = -1$.

### Next steps for load-bearing #1

**Path-α.4 (OPEN-4 quantitative consolidation):** focused construction memo deriving substrate-graph $\rho_{\mathrm{eff}}^{\mathrm{const}}$ value and $G_{\mathrm{eff}}$ from substrate parameters. Would supply quantitative substrate-graph $H$ derivation. Quantitative; not load-bearing for qualitative M3 closure.

**Path-α.5 (update Paper_ED_Cos_01):** propose retroactive upgrade M2 → M3 in inflation paper. Reflect audited OPEN-1 + OPEN-3 closures + M3 substrate-graph chain establishment. Update audit table row 13 from OPEN → D-via-I; verdict tier across 5 anchor points.

**Recommended:** Path-α.5 first (paper update reflecting closure), then Path-α.4 (quantitative consolidation).

### Cross-arc impact

The M3 substrate-graph chain closure is the **first substantive substrate-graph closure of a load-bearing OPEN derivation in the corpus** that produces a verdict upgrade (M2 → M3 for inflation paper).

**Compared to the chirality cascade outcome:**
- Chirality cascade: all closure attempts REJECTED at audit; arc stays M2 with one postulate; substrate is chirality-symmetric (negative substrate-research finding)
- **Exponential-growth attack: closure attempts ACCEPTED at audit; inflation arc upgrades M2 → M3; substrate supports exponential-growth via DCGT vacuum-energy translation (positive substrate-research finding)**

This asymmetry between the two load-bearing items is substantively informative: **ED's substrate ontology supports exponential-growth dynamics via standard QFT/cosmology inheritance through DCGT, but does NOT support chirality-discrimination via existing primitives.** The substrate is "leaner" in some directions (chirality) and "deeper" in others (cosmological dynamics).

Worth flagging in any future corpus-discipline overview as a substantive characterization of ED's substrate-ontology reach.

---

**End Memo_ED_DCGT_VacuumEnergyMapping_Audit.**
