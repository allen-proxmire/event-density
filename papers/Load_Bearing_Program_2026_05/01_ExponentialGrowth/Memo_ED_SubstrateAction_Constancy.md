# Memo_ED_SubstrateAction_Constancy — Construction Memo (OPEN-1 Attempt)

**Series:** Wave-3 Construction Memo (Cosmology Arc; inflation sub-thread; OPEN-1 from Memo_ED_DCGT_StateDependent §4)
**Status:** Substrate-graph attempt to derive whether the substrate-action density $S_{\mathrm{sub}}[\Psi]/V$ remains approximately constant across the unbalanced-saddle region during the saturation regime. Closure would supply Step B of the M3 substrate-graph chain (Memo_ED_DCGT_StateDependent §3). **Not a derivation. No new primitives.** Outcome: **substantive positive — substrate-action density is derivable as approximately constant across the saturation region from existing corpus content** (SC-4.x spatial homogeneity + Paper_ED_Cos_01 dynamic-equilibrium saturation condition + Paper_073 DCGT hydrodynamic-window applicability to uniform states). Closure is at **D-via-I** composition level, subject to audit per the discipline lessons from CommitPhaseInheritance.
**Date:** 2026-05-16
**Anchors:** Paper_ED_SC_4_9 (substrate-action $S_{\mathrm{sub}}$ functional + Hessian classification); Paper_073 (DCGT, hydrodynamic-window A→regime); Paper_ED_Cos_01 (Inflation §3.3–§3.4 saturation regime); Memo_ED_DCGT_StateDependent (M3 substrate-graph chain; OPEN-1); Paper_ED_CCC §3.6 + §3.7 (post-SCBU homogeneity + ignition); Paper_089 (V1); Paper_090 (V5).

---

## §1 Saturation-regime conditions

Per Paper_ED_Cos_01 §3.3–§3.4, the saturation regime within the post-SCBU ignition phase is structurally characterized by:

- $\Gamma_{\mathrm{diff}} > \Gamma_{\mathrm{prod}}$ — substrate diffusion outpaces substrate production.
- Substrate event-density near maximum — at the substrate-c-bounded admission demand.
- Expansion-dominant Hessian axes (Paper_ED_SC_4_9) sustained by diffusion-driven redistribution.
- Compression-dominant Hessian axes depleted faster than commitment can replenish.
- Substrate is globally homogeneous at cosmic scale per Paper_ED_CCC §3.6 + SC-4.x scale-collapse.

The regime is a **transient sub-regime** within the post-SCBU ignition phase — it begins when the substrate enters the diffusion-dominated condition and ends when $\Gamma_{\mathrm{prod}}$ recovers (Paper_ED_Cos_01 §3.5). During the regime, the substrate is in dynamic equilibrium maintained by the diffusion-production imbalance.

---

## §2 Substrate-action $S_{\mathrm{sub}}$ in Paper_ED_SC_4_9

Per Paper_ED_SC_4_9 §3.1, the substrate-action $S_{\mathrm{sub}}[\Psi]$ is a functional of the substrate participation field $\Psi$, with V1 + V5 kernel content supplying the quadratic form. Critical points $\delta S_{\mathrm{sub}}/\delta\Psi = 0$ are substrate-level saddles; the Hessian $\mathcal{H} = \delta^2 S_{\mathrm{sub}}/\delta\Psi\delta\Psi'$ classifies saddles by eigenvalue signature.

**Substrate-action density** $s(\ell) := S_{\mathrm{sub}}[\Psi]/V$ at locus $\ell$ depends on:

- **Local $\Psi$ content** — the chain-population substrate-graph state at $\ell$
- **V1 + V5 kernel coupling structure** at $\ell$
- **Local Hessian eigenvalue signature** (compression-dominant + expansion-dominant axis partition)

In a substrate where these inputs are uniform across loci, $s(\ell)$ is spatially uniform.

---

## §3 Spatial constancy via SC-4.x + post-SCBU homogeneity

Per Paper_ED_CCC §3.6 + Papers SC-4.x, the post-SCBU substrate has:

- Global homogeneity — no local content distinguishes substrate loci.
- Cross-scale invariance — no scale-dependent local structure.
- Curvature-moment collapse — no local curvature content.

**Consequence:** at any two loci $\ell_1, \ell_2$ in the post-SCBU substrate, the substrate-graph state is structurally identical (up to global $U(1)$ choices that don't affect the substrate-action density's magnitude). Therefore:

- $\Psi$ content density at $\ell_1$ = $\Psi$ content density at $\ell_2$
- V1 + V5 kernel coupling at $\ell_1$ = V1 + V5 kernel coupling at $\ell_2$ (kernels are substrate-parameter-determined, not state-dependent per Paper_089 + Paper_090 + Path-β negative on state-dependent V1)
- Local Hessian eigenvalue signature is the same at $\ell_1$ and $\ell_2$ (in the saturation regime, all loci have the same "unbalanced toward expansion-dominant" Hessian content)

→ **Substrate-action density $s(\ell)$ is spatially uniform across the saturation region.** $s(\ell_1) = s(\ell_2)$ for all $\ell_1, \ell_2$ in the unbalanced region.

This is a direct D-via-I composition from existing primitives (P03 spatial homogeneity in post-SCBU regime per ED_MEMORY anchor + SC-4.x scale-collapse + Paper_ED_CCC §3.6).

**Status: spatial constancy IDENTIFIED at D-via-I.**

---

## §4 Temporal constancy via diffusion–production dynamic equilibrium

The saturation regime is a transient sub-regime, not an asymptotic equilibrium. The substrate-action density evolves over the regime's duration. Is it approximately constant?

**Three dynamical mechanisms during saturation:**

(a) **Production** adds new $\Psi$ content at rate $\Gamma_{\mathrm{prod}}$ per substrate-graph locus per substrate-time. Net effect: total $\Psi$ content grows at rate $\Gamma_{\mathrm{prod}} \cdot V$ where $V$ is region volume.

(b) **Diffusion** redistributes existing $\Psi$ content at rate $\Gamma_{\mathrm{diff}}$. Net effect on density: maintains uniform spatial distribution (per §3); does not change total $\Psi$ content.

(c) **Region boundary advance** at substrate-c via V1 retarded propagation (per Paper_ED_Cos_01 §3.4). Net effect: $V$ grows at boundary advance rate. Volume scales as $V(t) \propto t^3$ in default-flat geometry (per Memo_ED_V1BoundaryExpansion §2).

**Density evolution:**
$$
s(t) = \frac{\text{total } \Psi \text{ content}}{V(t)} = \frac{\Psi_0 + \Gamma_{\mathrm{prod}} \cdot \int V(t')\,dt'}{V(t)}
$$

For density to be approximately constant in time, we need $\dot s \approx 0$, i.e., total $\Psi$ content scaling proportional to $V(t)$ as both grow.

**Saturation condition implications:** at saturation, substrate is at capacity — each locus carries the maximum $\Psi$ content per substrate-graph locus permitted by V1 + V5 + P04 bandwidth × P07 channel multiplicity. New loci added at the boundary (via V1 advance) immediately enter the saturation state because the substrate is uniform. **Density at new boundary loci = density at interior loci = saturation density.**

This is the structural content of "saturation" — the substrate is at maximum density at every locus, and boundary advance adds new loci at the same maximum density. Density is therefore **temporally approximately constant** during the saturation regime, at the saturation level.

The "approximately" reflects that the regime is transient: at the regime's start, density rises rapidly to the saturation level; at the regime's end, density falls as $\Gamma_{\mathrm{prod}}$ recovers. **During the bulk of the regime, density is approximately constant at the saturation level.**

This matches the structural analogy with standard cosmology de Sitter inflation: $\rho_{\mathrm{vac}}$ is approximately constant during slow-roll inflation; rises rapidly at inflation's start, falls at inflation's end. For exponential growth via Friedmann equations, "approximately constant" is sufficient.

**Status: temporal constancy IDENTIFIED at D-via-I composition** from Paper_ED_Cos_01 §3.3 saturation condition + boundary advance content + saturation = capacity structural property.

---

## §5 DCGT applicability to uniform-saturation states (partial OPEN-2 closure)

Memo_ED_DCGT_StateDependent flagged OPEN-2: whether DCGT applies (or admits clean extension) to the saturation regime, given DCGT's hydrodynamic-window restriction (Paper_073 + ED_MEMORY anchor: "DCGT breaks down outside the hydrodynamic-window — strong-gradient regimes, near-substrate-scale physics, near-singularity regimes").

**Examination:** the saturation regime in a globally-homogeneous post-SCBU substrate has:

- **Spatial gradients = 0** (per §3 spatial uniformity)
- **Temporal gradients small** at coarse-graining scale (per §4 temporal dynamic equilibrium; saturation evolution is slow compared to substrate-c)
- **Substrate at maximum density**, not near substrate-scale singularity

The "strong-gradient / near-singularity" conditions Paper_073 excludes do NOT apply to the saturation regime. **Uniform saturation has no strong gradients; DCGT's hydrodynamic-window applies.**

The high event-density per se is not a problem for DCGT — DCGT is bounded above by substrate-c (rate bound), not by event-density (state bound). High event-density with uniform distribution and small temporal gradients is well within DCGT's regime of applicability.

**Status: OPEN-2 closes partially.** DCGT applies to uniform-saturation states without requiring substrate-graph extension. The strong-gradient / near-singularity exclusions in Paper_073 do not fire in the saturation regime.

(Note: OPEN-2 fully closes here for the *uniform* saturation regime. If non-uniform saturation regimes exist — substrate with gradients in $\Gamma_{\mathrm{diff}}/\Gamma_{\mathrm{prod}}$ ratio across loci — DCGT applicability would need separate examination. For the post-SCBU homogeneous-ignition phase, uniform saturation is what the corpus content supplies.)

---

## §6 IDENTIFIED vs OPEN

### IDENTIFIED:

- **Spatial constancy of substrate-action density** across the saturation region — derived at D-via-I from SC-4.x scale-collapse + Paper_ED_CCC §3.6 post-SCBU homogeneity + P03 spatial homogeneity. §3.
- **Temporal constancy of substrate-action density** during the saturation regime — derived at D-via-I from Paper_ED_Cos_01 §3.3 saturation condition + saturation = capacity structural property + boundary advance preserving saturation density. §4.
- **DCGT applicability to uniform saturation states** — closes OPEN-2 partially. Uniform saturation has zero spatial gradients, small temporal gradients; outside Paper_073's strong-gradient / near-singularity exclusions. §5.
- **Substrate-action density is approximately constant** across the unbalanced region during saturation, at the saturation-level density. Both spatially and temporally constant within the regime's duration.

### OPEN (audit pending):

- **Hidden-assumption audit.** Per the discipline lesson from CommitPhaseInheritance (where §4's apparently-clean chain was audited as overclaim by hidden conflation of spatial-homogeneity with channel-uniqueness), this memo's §3–§4 chain should be audited for similar hidden assumptions. **Candidate weak links:**
  - Does "all loci have the same Hessian eigenvalue signature in the saturation regime" require channel-uniqueness at locus (which Audit Weak Link 1 identified as NOT supplied by spatial homogeneity)? If yes, similar audit problem.
  - Does "saturation = capacity at every locus" require structurally uniform capacity, which may depend on more than spatial homogeneity alone?
- **Quantitative substrate-action density value** at saturation — what is the saturation-level density? Not derived; would be needed for OPEN-4 (quantitative $H$ derivation).
- **OPEN-3 (DCGT translation to continuum stress-energy) remains.** This memo closes OPEN-1 and partially OPEN-2; OPEN-3 (substrate-action density → vacuum-energy-like continuum content) is a separate translation question.

### Status update for M3 closure:

Of the four load-bearing OPEN items from Memo_ED_DCGT_StateDependent §4:

| OPEN | Status after this memo |
|---|---|
| OPEN-1 (substrate-action density constancy) | **D-via-I (this memo §3 + §4), audit pending** |
| OPEN-2 (DCGT applicability to saturation) | **Partially closed (this memo §5), uniform-saturation regime within DCGT window** |
| OPEN-3 (DCGT translation to vacuum-energy stress-energy) | Still OPEN |
| OPEN-4 (quantitative $H$ derivation) | Still OPEN |

**If OPEN-1 and OPEN-2 hold up under audit**, the M3 substrate-graph chain advances to Steps A–C resolved, with Steps D–E (Friedmann recovery + exponential growth) standard standard-cosmology inheritance. Only OPEN-3 (the substrate-action-density → vacuum-energy translation) remains as the load-bearing substrate-graph derivation for M3 closure.

---

## §7 Recommended next steps

The substrate-research-frontier on load-bearing #1 has advanced substantively. Two honest next steps:

**Path-α.2 (audit this memo's §3–§4 chain).** Following the discipline lesson from CommitPhaseInheritance, the apparently-clean substrate-action constancy derivation should be audited for hidden assumptions. Specific audit questions:
- Does "all loci have the same Hessian signature" require channel-uniqueness?
- Does "saturation = capacity at every locus" require additional substrate-graph content?
- Are there counterexamples — substrate states where post-SCBU homogeneity holds but substrate-action density is non-uniform?

A focused audit memo (analogous to Memo_ED_CommitPhaseInheritance_Audit) would settle whether this memo's closure holds.

**Path-α.3 (attempt OPEN-3 directly).** Focused construction memo examining whether DCGT translates constant substrate-action density to vacuum-energy-like continuum stress-energy. This is a structural translation question — does Paper_ED_SC_4_9's S_sub functional play the role of a Lagrangian density whose constant value gives vacuum-energy continuum content?

In standard field theory, constant Lagrangian density $\mathcal{L}$ corresponds to constant vacuum-energy contribution $-\mathcal{L}$ to the stress-energy tensor. If $S_{\mathrm{sub}}$ is the substrate-side Lagrangian-density analog, constant $S_{\mathrm{sub}}$ density translates to constant vacuum-energy-like continuum density under DCGT. **Plausibility: high.** This may be a relatively quick closure attempt.

**My recommended next step:** **Path-α.2 audit first** — discipline lesson from CommitPhaseInheritance suggests apparently-clean substrate-graph closures should be audited before being committed to as D-via-I. The substrate-research-frontier work is high-value but the audit is cheap insurance against overclaim.

If audit holds: proceed to Path-α.3 (OPEN-3 attempt). If audit identifies hidden assumptions: revise this memo and reconsider the M3 closure prospects.

**Comparison with parallel cases:**

| Case | Apparently-closed at D-via-I? | Audit result |
|---|---|---|
| CommitPhaseInheritance (baryogenesis) | Yes (Memo_ED_CommitPhaseInheritance §4) | **Audited as overclaim — Weak Links 1, 2, 3 identified hidden assumptions** |
| **This memo (substrate-action constancy)** | Yes (§3 + §4) | **Audit pending** |

The CommitPhaseInheritance precedent argues strongly for running the audit before claiming closure. The corpus's discipline (per ED_MEMORY) is that load-bearing closures should be audit-tested by Claude-B-class adversarial reading. This memo's §3–§4 chain is load-bearing for M3, which would propagate to row 13 closure for Paper_ED_Cos_01.

---

**End Memo_ED_SubstrateAction_Constancy.**
