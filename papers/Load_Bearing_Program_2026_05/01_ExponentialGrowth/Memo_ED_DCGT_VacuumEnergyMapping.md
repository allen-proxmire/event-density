# Memo_ED_DCGT_VacuumEnergyMapping — Construction Memo (OPEN-3 Attempt)

**Series:** Wave-3 Construction Memo (Cosmology Arc; inflation sub-thread; OPEN-3 from Memo_ED_DCGT_StateDependent §4)
**Status:** Substrate-graph attempt to derive whether DCGT translates an approximately-constant substrate-action density $S_{\mathrm{sub}}/V$ (per audited OPEN-1 closure) into an approximately-constant vacuum-energy-like continuum stress-energy tensor $T^{\mu\nu}_{\mathrm{eff}}$ with equation-of-state $w \approx -1$. **Not a derivation. No new primitives.** Outcome: **substantive positive — the translation closes at D-via-I from existing primitives + standard field-theoretic Noether procedure inheritance**, subject to three audit flags. Combined with OPEN-1 closure, this advances M3 substrate-graph chain Steps A–C to D-via-I.
**Date:** 2026-05-16
**Anchors:** Paper_073 (DCGT, hydrodynamic-window); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ functional); Paper_ED_Cos_01 (Inflation §3.3–§3.5); Memo_ED_SubstrateAction_Constancy + Audit (OPEN-1 D-via-I closure at approximately-constant level); Memo_ED_DCGT_StateDependent (M3 chain; OPEN-3); Paper_087 (P03 spatial homogeneity, P13 time-homogeneity for Noether invariance).

---

## §1 DCGT translation rules

Per Paper_073 + ED_MEMORY anchor, DCGT bridges substrate-graph dynamics to continuum-level equations within the hydrodynamic-window scale-separation $\ell_{ED} \ll R_{cg} \ll L_{flow}$. Key features:

- Supplies the **form** of continuum equations (diffusion-form, propagator-form, constitutive-law-form).
- Coefficients (diffusion constant, viscosity, etc.) are INHERITED from value-layer empirical content.
- Operates by coarse-graining substrate-graph content over scales $R_{cg}$ much larger than substrate scale $\ell_{ED}$ but much smaller than flow scale $L_{flow}$.

DCGT does not explicitly specify the substrate-to-continuum translation for the stress-energy tensor. Standard hydrodynamics-from-microscopics derivations (e.g., Bogoliubov–Born–Green–Kirkwood–Yvon hierarchy, Chapman–Enskog expansion) preserve energy-momentum conservation under coarse-graining, with continuum stress-energy emerging from microscopic stress-energy averaging. The analogous substrate-side derivation is the load-bearing translation question.

---

## §2 Substrate-action as Lagrangian-density analog

Per Paper_ED_SC_4_9, the substrate-action $S_{\mathrm{sub}}[\Psi]$ is a functional of the substrate participation field $\Psi$ with V1 + V5 kernel content supplying the quadratic form. Structurally:

$$
S_{\mathrm{sub}}[\Psi] = \int s(\ell, t) \, d\mu(\ell, t) = \int \mathcal{L}_{\mathrm{sub}}(\Psi(\ell, t), \, \nabla_{V_1} \Psi, \, \nabla_{V_5} \Psi) \, d\mu
$$

where the substrate-side "Lagrangian density" $\mathcal{L}_{\mathrm{sub}}$ depends on local $\Psi$ content plus kernel-coupled $\Psi$ at neighboring loci (V1 + V5 finite-width couplings act analogously to spatial derivatives in field-theoretic Lagrangians).

**Substrate-action density** $s(\ell, t) := \mathcal{L}_{\mathrm{sub}}$ at substrate-graph locus $\ell$ at substrate-time $t$. Per audited OPEN-1 closure (Memo_ED_SubstrateAction_Constancy_Audit), $s(\ell, t)$ is **approximately constant across the saturation region** (spatially uniform per SC-4.x homogeneity; temporally constant in the regime bulk per dynamic equilibrium).

The structural mirror to field-theoretic $S = \int \mathcal{L}\, d^4x$ is direct: $S_{\mathrm{sub}}$ plays the role of action functional, $\mathcal{L}_{\mathrm{sub}}$ the role of Lagrangian density, $\Psi$ the role of field.

---

## §3 Substrate-side stress-energy via Noether procedure

Standard field-theoretic Noether procedure: for a Lagrangian density $\mathcal{L}(\phi, \partial_\mu \phi)$ invariant under spacetime translations, the conserved Noether stress-energy tensor is:

$$
T^{\mu\nu} = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} \partial^\nu \phi - g^{\mu\nu} \mathcal{L}
$$

**Substrate-side analog:** for substrate-side $\mathcal{L}_{\mathrm{sub}}(\Psi, \nabla_{V_1}\Psi, \nabla_{V_5}\Psi)$ invariant under substrate-graph translation (P03 spatial homogeneity + P13 time-homogeneity), the conserved substrate-side stress-energy tensor is:

$$
T^{\mu\nu}_{\mathrm{sub}} = \sum_{K \in \{V_1, V_5\}} \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K \Psi)} \nabla^\nu_K \Psi - g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}
$$

(with kernel-couplings replacing standard spatial derivatives; substrate-side metric $g^{\mu\nu}_{\mathrm{sub}}$ supplied by DCGT continuum bridge for the coarse-graining frame).

**Constant-$\mathcal{L}_{\mathrm{sub}}$ case:** if $\Psi$ is constant in space and time across the saturation region (per OPEN-1 closure approximate-constancy), all derivative terms $\nabla_K \Psi$ vanish (or are at-most O(fluctuations)). The Noether stress-energy reduces to:

$$
T^{\mu\nu}_{\mathrm{sub}} \approx -g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}} = -g^{\mu\nu} \rho_{\mathrm{sub}}^{\mathrm{const}}
$$

where $\rho_{\mathrm{sub}}^{\mathrm{const}} = \mathcal{L}_{\mathrm{sub}}^{\mathrm{const}}$ is the constant substrate-action density.

**This is exactly the vacuum-energy form** at substrate-graph level: $T^{\mu\nu} = -g^{\mu\nu} \rho$ with equation of state $p = -\rho$ ($w = -1$).

---

## §4 DCGT coarse-graining preserves vacuum-energy form

For uniform substrate states (approximately-constant $\Psi$ across the saturation region), DCGT coarse-graining of substrate-side content $X(\ell, t)$ produces continuum-side $X_{\mathrm{eff}}(x, t) = \langle X \rangle_{R_{cg}}$, the average over scales $R_{cg}$.

Applied to substrate-side stress-energy:

$$
T^{\mu\nu}_{\mathrm{eff}}(x, t) = \langle T^{\mu\nu}_{\mathrm{sub}} \rangle_{R_{cg}}
$$

For uniform $T^{\mu\nu}_{\mathrm{sub}} = -g^{\mu\nu} \rho_{\mathrm{sub}}^{\mathrm{const}}$, averaging over uniform content preserves the form:

$$
T^{\mu\nu}_{\mathrm{eff}}(x, t) \approx -g^{\mu\nu}_{\mathrm{eff}} \rho_{\mathrm{eff}}^{\mathrm{const}}
$$

with $\rho_{\mathrm{eff}}^{\mathrm{const}} = \rho_{\mathrm{sub}}^{\mathrm{const}}$ (substrate-side constant value, possibly modified by DCGT-specific coarse-graining factors but preserving the constant character).

**Continuum-side stress-energy is approximately-constant vacuum-energy-like, with equation of state $w \approx -1$.**

---

## §5 Equation of state $w \approx -1$

The continuum stress-energy $T^{\mu\nu}_{\mathrm{eff}} = -g^{\mu\nu} \rho_{\mathrm{eff}}^{\mathrm{const}}$ in standard cosmology-fluid form decomposes as:

- Energy density $\rho = T^{00}_{\mathrm{eff}} = \rho_{\mathrm{eff}}^{\mathrm{const}}$
- Pressure $p = -T^{ii}_{\mathrm{eff}}/3 = -\rho_{\mathrm{eff}}^{\mathrm{const}}$
- Equation of state $w = p/\rho = -1$

**Vacuum-energy / cosmological-constant form.** Friedmann equations with constant $\rho$, $w = -1$ give:

$$
H^2 = \frac{8\pi G_{\mathrm{eff}}}{3} \rho_{\mathrm{eff}}^{\mathrm{const}} = \mathrm{constant}
$$

$\dot a / a = H = $ constant → $a(t) = a_0 e^{Ht}$ → **exponential scale-growth.**

This is Steps D + E of the M3 substrate-graph chain (standard cosmology inheritance from Friedmann equations applied to vacuum-energy stress-energy).

**Combined M3 closure (subject to OPEN-3 audit):** Steps A–C of the M3 chain (saturation regime → constant substrate-action density → DCGT translation to vacuum-energy continuum content) closes at D-via-I from existing primitives + Noether + DCGT coarse-graining + audited OPEN-1. Steps D + E are standard cosmology inheritance.

**Exponential growth $\dot a \propto a$ in ED inflation closes at D-via-I — pending audit.**

---

## §6 IDENTIFIED vs OPEN (with audit flags)

### IDENTIFIED:

- **Substrate-action $S_{\mathrm{sub}}[\Psi]$ has Lagrangian-density structure.** $\mathcal{L}_{\mathrm{sub}}(\Psi, \nabla_{V_1}\Psi, \nabla_{V_5}\Psi)$ mirrors standard field-theoretic Lagrangian density, with V1 + V5 kernel couplings replacing standard spatial derivatives.
- **P03 spatial homogeneity + P13 time-homogeneity supply substrate-translation invariance** required for Noether procedure.
- **Noether stress-energy substrate-side** $T^{\mu\nu}_{\mathrm{sub}}$ is constructible from $\mathcal{L}_{\mathrm{sub}}$ + standard Noether procedure.
- **For constant $\Psi$ (saturation regime per OPEN-1):** $T^{\mu\nu}_{\mathrm{sub}} \approx -g^{\mu\nu} \rho_{\mathrm{sub}}^{\mathrm{const}}$ — vacuum-energy form at substrate-graph level.
- **DCGT coarse-graining of uniform stress-energy preserves vacuum-energy form** — continuum-side $T^{\mu\nu}_{\mathrm{eff}} \approx -g^{\mu\nu}_{\mathrm{eff}} \rho_{\mathrm{eff}}^{\mathrm{const}}$ with $w \approx -1$.
- **Friedmann recovery from vacuum-energy continuum stress-energy** gives $a(t) = a_0 e^{Ht}$ with constant $H$ — standard cosmology de Sitter.

### Audit flags (load-bearing for OPEN-3 acceptance):

- **Audit flag #1 — Substrate-side Noether procedure.** Standard Noether requires the action to be invariant under continuous symmetry. Substrate-graph translation is a *discrete* symmetry (loci are discrete points). Whether the discrete-symmetry analog of Noether produces a well-defined stress-energy tensor is a substrate-graph derivation step not constructed here. Likely closes via standard lattice-field-theory Noether procedures (well-established in standard physics), but worth verifying.
- **Audit flag #2 — DCGT preserves stress-energy under coarse-graining.** Standard hydrodynamics-from-microscopics (BBGKY, Chapman–Enskog) preserves energy-momentum conservation under coarse-graining. The substrate-side analog should follow but requires substrate-graph derivation. For uniform states, the derivation is essentially trivial (averaging uniform content gives uniform averaged content); for non-uniform states it's non-trivial.
- **Audit flag #3 — DCGT dissipative-vs-Lagrangian translation.** DCGT produces continuum equations of diffusion-form (potentially dissipative). Standard Lagrangian field theory gives non-dissipative dynamics. The transition from substrate-side Lagrangian dynamics to continuum-side diffusion dynamics involves entropy production / projection / coarse-graining that doesn't preserve Lagrangian structure. **Does this affect the stress-energy translation?** For uniform-saturation states (no entropy production from coarse-graining of uniform content), the dissipative effects are minimal; stress-energy translation is approximately Lagrangian-conservative. For non-uniform states, dissipative corrections could modify the effective equation of state away from $w = -1$.

### OPEN:

- **All three audit flags require adversarial audit** (Claude-B-class memo) before committing to OPEN-3 closure. Following the discipline lesson from CommitPhaseInheritance, the apparently-clean closure should be audit-tested.
- **OPEN-4 (quantitative $H$ derivation)** remains. Requires substrate-graph derivation of $\rho_{\mathrm{eff}}^{\mathrm{const}}$ in terms of substrate parameters + $G_{\mathrm{eff}}$ from DCGT.

---

## §7 Status update for M3 chain

| Step | OPEN | Status |
|---|---|---|
| A | Saturation regime structure (Paper_ED_Cos_01 §3.3) | INHERITED |
| B | Substrate-action density constancy in saturation | **D-via-I (OPEN-1, audited)** |
| C | DCGT translates constant substrate-action to vacuum-energy continuum stress-energy | **D-via-I (this memo, OPEN-3, audit pending)** |
| D | Friedmann recovery → constant $H$ | Standard cosmology inheritance |
| E | $a(t) = a_0 e^{Ht}$ | Standard cosmology inheritance |

**If OPEN-3 holds up under audit, the M3 substrate-graph chain Steps A–C are fully D-via-I closed.** Steps D + E are standard cosmology inheritance via Friedmann + de Sitter standard machinery. **Paper_ED_Cos_01 row 13 closes substrate-graph-derivably; verdict M2 → M3 retroactively.**

### Remaining OPEN items for full M3:

- **OPEN-2 (DCGT applicability):** partially closed by OPEN-1 audit memo §5 for uniform-saturation states. Full closure requires checking non-uniform saturation regimes (sub-regime variations during regime start/end transitions), which are bulk-of-regime corrections not load-bearing for M3 framing.
- **OPEN-4 (quantitative $H$):** substrate-graph derivation of $\rho_{\mathrm{eff}}^{\mathrm{const}}$ value + $G_{\mathrm{eff}}$ from substrate parameters. Quantitative consolidation; not load-bearing for qualitative M3 closure.

### Recommended next step

**Adversarial audit of this memo's §3–§4 chain.** Same discipline as CommitPhaseInheritance + SubstrateAction_Constancy audits. Three load-bearing audit flags identified in §6.

If audit accepts: M3 substrate-graph chain Steps A–C fully closed; proceed to OPEN-4 quantitative consolidation + Paper_ED_Cos_01 update to retroactively upgrade row 13 to D-via-I and propose verdict M2 → M3.

If audit identifies hidden assumptions: revise this memo; reconsider M3 closure prospects.

**Comparison with parallel cases:**

| Memo | Apparently-closed at D-via-I? | Audit outcome |
|---|---|---|
| CommitPhaseInheritance | Yes | **REJECTED** — Weak Links 1, 2, 3 identified hidden assumptions |
| SubstrateAction_Constancy | Yes | **ACCEPTED at approximately-constant level** — distinct from CommitPhaseInheritance |
| **DCGT_VacuumEnergyMapping (this memo)** | Yes | **Audit pending** |

The SubstrateAction_Constancy audit accepted closure because the required assumptions ARE supplied by the corpus (approximately) AND no structural inconsistency existed. This memo's audit should test the same criteria.

**Pattern note:** the load-bearing #1 attack is advancing substrate-graph closures where load-bearing #2 (chirality) hit walls. The substrate-research-frontier asymmetry between these arcs may itself be substantively informative — ED's substrate may support exponential-growth dynamics (via DCGT vacuum-energy translation) but not chirality-discrimination (which requires ontology extension).

---

**End Memo_ED_DCGT_VacuumEnergyMapping.**
