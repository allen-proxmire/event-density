# Memo_ED_SubstrateAction_Constancy_Audit — Adversarial Audit of OPEN-1 Closure

**Series:** Wave-3 Audit Memo (Cosmology Arc; inflation sub-thread; Claude-B-class adversarial audit of Memo_ED_SubstrateAction_Constancy)
**Status:** Critical audit of the OPEN-1 closure claim that substrate-action density is spatially and temporally constant across the saturation region. **Not a derivation. Auditor stance, not advocate.** Audit conducted following the discipline lesson from Memo_ED_CommitPhaseInheritance_Audit (apparently-clean substrate-graph closures sometimes hide assumptions that adversarial reading exposes).
**Date:** 2026-05-16
**Anchors:** Memo_ED_SubstrateAction_Constancy (audit target); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ functional); Paper_ED_Cos_01 §3.3–§3.4 (saturation regime); Paper_073 (DCGT); Paper_ED_CCC §3.6 + §3.7; Memo_ED_CommitPhaseInheritance_Audit (audit discipline template).
**Headline verdict:** **ACCEPT at "approximately constant" level**, with explicit qualifications. The closure is not overclaim — it operates at the same level of approximation standard cosmology slow-roll inflation uses. **Distinct from CommitPhaseInheritance overclaim case.** Recommend updating SubstrateAction_Constancy memo to make the "approximately constant" framing explicit.

---

## §1 What's being audited

Memo_ED_SubstrateAction_Constancy claims OPEN-1 closure via three sub-arguments:

- **§3 (spatial constancy):** post-SCBU homogeneity + SC-4.x + uniform V1/V5 + uniform Hessian signature → $s(\ell_1) = s(\ell_2)$ across saturation region
- **§4 (temporal constancy):** saturation = capacity at every locus; boundary advance preserves saturation density; total content scales with $V(t)$ keeping density at saturation level
- **§5 (DCGT applicability):** uniform-saturation has zero spatial gradients + small temporal gradients → DCGT hydrodynamic-window applies

The memo flags itself for audit (§7), citing the CommitPhaseInheritance precedent where apparently-clean substrate-graph closure was audited as overclaim.

This memo executes that audit adversarially.

---

## §2 Audit of §3 spatial-constancy argument

### Examination

**Claim:** "At any two loci $\ell_1, \ell_2$ in saturation, substrate-action density is equal."

**Required substrate-graph content:**
- Equal $\Psi$ content density
- Equal V1+V5 kernel coupling
- Equal Hessian eigenvalue signature

**Supplied by SC-4.x + post-SCBU homogeneity?**

SC-4.x scale-collapse + Paper_ED_CCC §3.6 supply **spatial homogeneity** — same substrate structure at every locus. This guarantees:
- Same channel structure available at every locus (uniform channel STRUCTURE)
- Same kernel parameters (uniform kernel PARAMETERS)

It does NOT automatically guarantee:
- Same channel POPULATIONS at every locus
- Same per-locus Hessian eigenvalue SPECTRUM (only qualitative pattern)

**Hidden assumption check #1 — channel populations.** Spatial homogeneity gives uniform channel STRUCTURE but not uniform channel POPULATION. Different loci could have different populations of each available channel, giving different $S_{\mathrm{sub}}$ contributions.

In the saturation regime, however, **every channel saturates at its substrate-c-bounded admission demand at every locus** (per §1 saturation condition + uniform capacity per locus by spatial homogeneity). So channel populations ARE uniform across loci under spatial homogeneity + saturation. ✓

This is a substrate-graph reasoning step the SubstrateAction_Constancy memo glossed over. The audit verifies it holds — but it should be made explicit.

**Hidden assumption check #2 — Hessian eigenvalue spectrum.** The Hessian at a saddle is a tensor with eigenvalues. "All loci in saturation have the same Hessian SIGNATURE" (qualitative pattern: unbalanced toward expansion-dominant) ≠ "all loci have the same Hessian EIGENVALUE SPECTRUM" (exact eigenvalues).

For $s(\ell_1) = s(\ell_2)$ strictly, we need eigenvalue spectra equal. Under spatial homogeneity + saturation, this holds **only in the strict-uniformity limit** (idealization). In the realistic ignition regime (Paper_ED_Cos_01 §3.4 non-stationary), small fluctuations in Hessian eigenvalues across loci exist.

**Audit finding A:** Spatial constancy holds **strictly only under strict uniformity** (idealization); **approximately under approximate homogeneity** (realistic ignition regime).

### Adversarial counterexample search

Are there substrate states where spatial homogeneity holds but $s(\ell)$ is non-uniform?

- **Multi-channel substrate with heterogeneous population:** spatial homogeneity gives uniform channel structure but doesn't force uniform population. Counterexample defeated by saturation condition (all channels saturate uniformly).
- **V5 cross-boundary content variations:** Memo_ED_V5PhaseContent established V5 cross-boundary carries pre-aeon phase content. If pre-aeon substrate was non-uniform, V5 delivery could be locus-variable. Under post-SCBU homogeneity (which establishes substrate-uniformity), V5 cross-boundary delivery is also uniform → counterexample defeated.
- **Substrate-graph noise / primordial fluctuations:** ignition regime has small substrate-graph fluctuations (these seed structure formation per Paper_ED_Cos_01 §3.6). These are non-uniform substrate states under approximate (not strict) homogeneity. Counterexample stands at the approximate level.

**Audit finding B:** Spatial constancy is structurally clean at the strict-homogeneity level. At the realistic-non-strict level, small fluctuations exist (consistent with observed CMB anisotropies). These are the same kind of approximations standard cosmology slow-roll inflation uses.

---

## §3 Audit of §4 temporal-constancy argument

### Examination

**Claim:** "Boundary advance adds new loci at the same maximum density; density stays at saturation level throughout the regime."

**Hidden assumption check #1 — capacity uniformity.** "Saturation = capacity at every locus" requires substrate capacity to be uniform across loci. Per Paper_087 + Paper_089 + spatial homogeneity, V1 finite-width × P04 bandwidth × P07 channel multiplicity is uniform → capacity is uniform. ✓ Clean.

**Hidden assumption check #2 — instantaneous boundary-locus saturation.** "New loci added by boundary advance immediately enter saturation" requires the balanced → unbalanced transition at the boundary to be instantaneous (or fast compared to bulk dynamics).

This is **NOT true at substrate-graph level.** The transition takes finite time. The boundary region has a transition zone of finite width — at least $\ell_{V_1}$ — where density varies from balanced (low) to saturated (max).

**Audit finding C:** The boundary transition zone has density gradient. This is a substantive concern for strict constancy. **Mitigating factor:** for $a \gg \ell_{V_1}$, transition zone occupies a small fraction of total region; bulk is at saturation density. Bulk-temporal-constancy holds asymptotically (as in standard slow-roll inflation after a few e-folds).

For $a \sim \ell_{V_1}$ (early ignition), boundary effects dominate; constancy does NOT hold. This is a regime restriction — bulk-of-regime constancy, not start-of-regime constancy.

**Hidden assumption check #3 — temporal regime stationarity.** The saturation regime is **transient**, not stationary. Per Paper_ED_Cos_01 §3.5, the regime begins when $\Gamma_{\mathrm{diff}}$ exceeds $\Gamma_{\mathrm{prod}}$ and ends when $\Gamma_{\mathrm{prod}}$ recovers. During the regime, the ratio $\Gamma_{\mathrm{diff}}/\Gamma_{\mathrm{prod}}$ evolves.

"Density stays at saturation level" requires the saturation level itself to be approximately constant during the regime. The saturation level depends on substrate parameters (V1 + V5 + P04 + P07) which are constant — but it also depends on the ratio $\Gamma_{\mathrm{diff}}/\Gamma_{\mathrm{prod}}$ being "in saturation."

**Audit finding D:** During the bulk of the regime, temporal constancy holds. At regime start/end transitions, it does not. Approximate constancy, not strict.

---

## §4 Audit of §5 DCGT-applicability argument

### Examination

**Claim:** Uniform saturation has zero spatial gradients + small temporal gradients → DCGT hydrodynamic-window applies.

**Hidden assumption check #1 — gradient elimination.** Spatial gradients are zero only at the bulk of the region. At the boundary transition zone, gradients are non-zero (per Audit finding C). DCGT may not apply cleanly at the boundary transition.

**Mitigating factor:** for coarse-graining scale $R_{cg} > \ell_{V_1}$ (transition zone width), DCGT smooths over the boundary; bulk + transition together coarse-grain to approximately uniform continuum content. DCGT applies in this regime.

For $R_{cg} < \ell_{V_1}$, DCGT resolves boundary gradients; may not apply cleanly. But the relevant inflation scales have $R_{cg} \gg \ell_{V_1}$, so this case is irrelevant.

**Audit finding E:** DCGT applicability holds for the bulk under standard hydrodynamic-window scale-separation. Boundary transition is sub-coarse-graining-scale and effectively smoothed over.

**Hidden assumption check #2 — temporal gradients.** Saturation regime is transient; temporal gradients exist (density evolves over regime duration). These are small at the coarse-graining time-scale during the bulk; large at regime start/end.

For inflation's ~60 e-folds bulk, temporal gradients are small. For regime transitions, they're large. Same as standard slow-roll inflation.

**Audit finding F:** DCGT applicability for temporal evolution holds in the bulk of the saturation regime.

---

## §5 Comparison with CommitPhaseInheritance audit

The CommitPhaseInheritance overclaim was identified via three weak links:
1. Channel-uniqueness conflation with spatial homogeneity
2. Strict reading predicted zero antimatter (audit-killing)
3. V5 cross-boundary supplies alternative phase reference

**Does SubstrateAction_Constancy face analogous problems?**

| Weak link pattern | CommitPhaseInheritance | SubstrateAction_Constancy |
|---|---|---|
| Hidden assumption beyond spatial homogeneity? | YES — required channel-uniqueness, not supplied by homogeneity | **Partially:** Hessian eigenvalue-spectrum uniformity beyond signature uniformity, supplied by saturation condition + strict homogeneity (or approximately under approximate homogeneity) |
| Strict reading structurally inconsistent with framework? | YES — predicts zero antimatter, contradicts observation | **NO** — approximate constancy is sufficient for M3 closure (matches standard cosmology slow-roll discipline) |
| Independent substrate-graph counterexample exists? | YES — V5 cross-boundary supplies alternative phase reference | **NO** — no substrate-graph counterexample defeats approximate constancy under spatial homogeneity + saturation |

**Net comparison:** the constancy claim is structurally **more robust than CommitPhaseInheritance** at the relevant level (approximate). The framework's approximation level matches standard cosmology's slow-roll discipline; the audit does not identify a structural inconsistency or counterexample that defeats the closure at this level.

---

## §6 Verdict

**ACCEPT the OPEN-1 closure at "approximately constant" level**, with explicit qualifications:

- **Spatial constancy holds approximately**, under approximate post-SCBU homogeneity. Strict constancy is the idealization; small fluctuations exist in the realistic ignition regime (consistent with observed CMB anisotropies = primordial fluctuations).
- **Temporal constancy holds in the bulk of the regime**, not at start/end transitions or in the small-region (early ignition, $a \sim \ell_{V_1}$) limit.
- **DCGT applies under standard hydrodynamic-window scale-separation** ($R_{cg} \gg \ell_{V_1}$). Boundary transition zone is sub-coarse-graining-scale; smoothed over by DCGT coarse-graining.

These qualifications are **the same level of approximation standard cosmology slow-roll inflation uses.** The closure is acceptable at this level.

### Distinct from CommitPhaseInheritance overclaim case

The CommitPhaseInheritance audit rejected its closure because the **required assumption** (channel-uniqueness) was **not supplied by the corpus** AND the **strict reading** (which would supply the closure) was **structurally inconsistent** with the framework (predicted zero antimatter).

This memo's required assumptions ARE supplied by the corpus (at the approximate level), AND the approximate reading IS structurally consistent with both the framework and the standard cosmology comparison case. **Not overclaim.**

### What the closure does NOT establish

- Strict (exactly uniform) substrate-action density. Only approximate.
- Constancy at regime start/end transitions. Only bulk-of-regime.
- Constancy at sub-coarse-graining-scale resolution. Only at coarse-graining scale.
- Quantitative substrate-action density value. Not derived; would be OPEN-4 territory.

These limitations should be explicitly flagged in the updated SubstrateAction_Constancy memo.

---

## §7 Recommended updates + next steps

### Updates to SubstrateAction_Constancy memo

1. **Explicit "approximately constant" framing** throughout — replace claims of "constant" with "approximately constant," with explicit qualifications.
2. **Add qualification subsection** noting:
   - Strict uniformity is idealization; realistic ignition has small fluctuations
   - Bulk-of-regime, not start/end transitions
   - Hessian eigenvalue spectrum uniformity beyond signature uniformity is supplied by saturation condition + homogeneity at the strict level
3. **Add comparison to standard cosmology slow-roll** — note that "approximately constant vacuum energy" is exactly the level standard inflation operates at; the substrate-side framework operates at the same level of approximation.
4. **Note that primordial fluctuations are the substrate-side small-deviations from strict constancy** — connects to Paper_ED_Cos_01 row 16 (qualitative spectral character) and row 17 (quantitative $n_s$, $r$, $N$).

### Next-step paths

**Path-α.3 (proceed to OPEN-3):** focused construction memo examining whether DCGT translates approximately-constant substrate-action density to approximately-constant vacuum-energy-like continuum stress-energy. This is a structural translation question, plausibly clean given $S_{\mathrm{sub}}$'s Lagrangian-density-analog structure. Likely tractable closure attempt.

**Path-α.4 (proceed to OPEN-4):** focused construction memo deriving quantitative substrate-side $H$ value from the saturation-level substrate-action density. Would close row 13 substantively and supply inflation-fluctuation-spectrum content (rows 16, 17 closure).

**Recommended:** Path-α.3 first. OPEN-3 closure plus this memo's accepted OPEN-1 + OPEN-2 partial closure would advance M3 substrate-graph chain Steps A–C fully + bring Step D (Friedmann recovery) into reach. After Path-α.3, Path-α.4 quantitative consolidation. Then update Paper_ED_Cos_01 to retroactively upgrade row 13 to D-via-I and propose verdict M2 → M3.

**Status of load-bearing #1 after this audit:**

| Memo | Result |
|---|---|
| ExponentialGrowth_Scoping | Four candidates identified |
| V1BoundaryExpansion (Path-β) | Negative; V1-structural mechanisms fail |
| DCGT_StateDependent (Path-α) | M3 identified as cleanest route; 4 OPEN items |
| SubstrateAction_Constancy (Path-α.1) | OPEN-1 D-via-I closure attempted |
| **SubstrateAction_Constancy_Audit (this memo)** | **OPEN-1 closure ACCEPTED at approximately-constant level. Not overclaim. Distinct from CommitPhaseInheritance case.** |

**Net advance:** OPEN-1 closed (with approximate-constancy qualification); OPEN-2 partially closed; OPEN-3 and OPEN-4 remain for M3 full closure. **Load-bearing #1 is substantively advancing.**

---

**End Memo_ED_SubstrateAction_Constancy_Audit.**
