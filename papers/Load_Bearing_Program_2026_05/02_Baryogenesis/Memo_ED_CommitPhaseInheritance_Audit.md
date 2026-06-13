# Memo_ED_CommitPhaseInheritance_Audit — Critical Audit of Path-A

**Series:** Wave-3 Audit Memo (Cosmology Arc; baryogenesis sub-thread)
**Status:** Claude-B-class critical audit of Path-A from Memo_ED_CommitPhaseInheritance — the proposal to treat $\pi_{\mathrm{commit}} = \pi_K$ as D-via-I under strict post-SCBU homogeneity and upgrade Paper_ED_Baryogenesis from M2 to M3. **Not a derivation. Auditor stance, not advocate.**
**Date:** 2026-05-16
**Anchors:** Memo_ED_CommitPhaseInheritance; Memo_ED_KernelArrowAsymmetry; Memo_ED_BinaryChirality; Memo_ED_ChainArrowChirality; Paper_ED_Baryogenesis_Open; Paper_087 (P09 definition); Paper_ED_CCC §3.6 + §3.7.
**Headline verdict:** **Push back. Path-A is NOT cleanly D-via-I.** The §4 argument has at least one hidden assumption (conflation of spatial-homogeneity with channel-structure-uniqueness) and one substantive structural concern (the strict reading appears to predict zero antimatter, not the observed small-but-nonzero asymmetry). Recommend retaining the M2 framing with P-CommitPhaseInheritance declared as a *second* paper-specific postulate (Path-B), or holding the question OPEN at the current M2.

---

## §1 What Path-A claims

The CommitPhaseInheritance memo §4 argues an eight-step substrate-graph chain:

1. P09 supplies $U(1)$ phase
2. Paper_093 T18 identifies kernel-arrow with V1 retarded-support
3. Paper_089 T18 forces V1 retarded by P11
4. P11 forward ↔ V1 retarded ↔ kernel-arrow (substrate-side directional identification)
5. P11 commitment creates new chain content in the substrate's forward direction
6. New chain's chain-arrow direction = forward direction = kernel-arrow direction at locus
7. **P09 phase of chain-arrow at creation = P09 phase of kernel-arrow → $\pi_C(e_{\mathrm{new}}) = \pi_K(\ell)$**
8. Therefore $\chi_C(e_{\mathrm{new}}) = 0$

Path-A treats steps 1–8 as D-via-I composition closure under "strict post-SCBU homogeneity" — asymmetric admission cost OPEN row closes; baryogenesis upgrades M2 → M3.

---

## §2 Step-by-step audit

**Steps 1, 2, 3, 4:** Direct inheritances from Paper_087, Paper_089 T18, Paper_093 T18, Paper_ED_CCC. ✓ Clean.

**Step 5:** Direct from P11 commitment-irreversibility definition. ✓ Clean.

**Step 6:** Per (4), substrate-side "forward" direction at the commitment locus is the kernel-arrow direction. The new chain's chain-arrow (its successor-edge direction) is, *by P11 definition*, forward. So the chain-arrow direction = kernel-arrow direction at locus. ✓ Clean *as a statement about edge directions*.

**Step 7:** Claims that the **P09 phase representation** of the chain-arrow equals the **P09 phase representation** of the kernel-arrow at the same locus, because they "share the same substrate-graph direction."

**This step does not hold cleanly.** The chain-arrow and kernel-arrow being parallel (same edge direction at substrate-graph level) does not imply their P09 phase representations are equal. P09 phase is attached to *channels*, not to directions per se. Multiple channels at a single locus can propagate in the same direction with *different* P09 phase content.

Memo_ED_ChainArrowChirality §3.3 explicitly defines $\chi_C := \pi_C - \pi_K \pmod{2\pi}$ as a phase difference that *can be nonzero* — i.e., $\pi_C$ and $\pi_K$ are independently-valued P09 phases of two directed substrate-graph objects at the same locus. The chirality definition itself **presupposes** that the two phases can differ. Step 7 contradicts that presupposition without supplying substrate-graph justification.

**Step 8:** Follows from (7) if (7) holds. ✓ Conditionally clean.

**Net audit of §4 argument:** load-bearing failure at step 7. The argument's "strict homogeneity → unique phase reference → $\pi_{\mathrm{commit}} = \pi_K$" chain requires a hidden assumption identified in §3 below.

---

## §3 Hidden assumptions and weak links

### Weak link 1 (load-bearing): conflation of two homogeneity notions

The memo §4 reasoning treats "strict post-SCBU homogeneity" as implying "only one P09 phase reference available at each substrate locus." But Paper_ED_CCC §3.6 + SC-4.x scale-collapse establish **spatial homogeneity** — same substrate structure at every locus — *not* **channel-structure uniqueness** at each locus.

Spatial homogeneity says: at locus $\ell_1$ and locus $\ell_2$, the substrate has the same channel structure. It does NOT say: at any single locus, there is only one channel.

A homogeneous substrate can have a rich channel structure at each locus — multiple channels per direction, each with different P09 phase content. The standard-physics analog: even a spatially-homogeneous vacuum has multiple field sectors (electron, positron, photon, ...) at each spacetime point.

**Strict homogeneity does not eliminate multi-channel-per-direction structure.** Step 7 of the §4 argument requires the *latter* (channel-uniqueness), not the former (spatial homogeneity). The corpus supplies the former, not the latter.

This is the load-bearing weak link. Without channel-uniqueness, step 7 is not D-via-I derivable from existing primitives.

### Weak link 2 (substantive): the strict reading predicts zero antimatter

If the §4 argument *did* close cleanly — i.e., if at substrate-graph level only $\pi_K$ phase content is available for new-chain creation — then the substrate would create **only** $\chi_C = 0$ chains. There would be no substrate-graph mechanism for creating $\chi_C = \pi$ chains at all, in any regime.

This contradicts observation: antimatter exists (created in pair-production, observed in cosmic rays, manufactured at CERN). The framework needs to permit anti-aligned chains in *some* regime, even if asymmetrically.

The memo §1 toy-model statement *requires* that anti-aligned chains can be created with substrate slack ("Post-saturation, substrate slack returns → phase-inverted commitments resume → symmetric pair-production restores"). But under the strict-homogeneity reading that supplies step 7, there is no substrate-side phase reference *other than* $\pi_K$ — so phase-inverted commitments cannot occur in any regime, slack or no slack.

**The strict reading that supplies the closure also kills the framework's empirical match.** This is structurally substantive — not just a regime-restriction caveat.

If the framework allows phase-inverted commitments in some regimes (post-saturation), then alternative substrate-side phase references must exist, which contradicts the channel-uniqueness assumption in step 7.

### Weak link 3: V5 cross-boundary memory phase content

Paper_ED_CCC §3.4 identifies the twistor mass-conservation integral with V5 cross-boundary memory. The substrate-graph content carried across SCBU includes mass-energy from pre-boundary aeon. Whether V5 cross-boundary content carries P09 phase information is OPEN, flagged in CommitPhaseInheritance §5.

If V5 cross-boundary carries phase, then it supplies a substrate-side phase reference *additional* to $\pi_K$ at post-boundary loci. This contradicts the channel-uniqueness assumption. The OPEN flag in §5 is honest but the weak link is more than incidental — it potentially undermines step 7 entirely.

### Weak link 4: "new-chain creation" vs "ongoing-chain commitment" proportion

The memo §3 argues that in the saturation regime, chains are being newly-created en masse (Source B inheritance) rather than ongoing-chain commitments (Source A). This is asserted from Paper_ED_CCC §3.7 ignition-regime non-stationarity but not constructively derived. If a substantial fraction of saturation-regime commitments are ongoing-chain commitments (P05 transport from upstream), the §4 argument applies only to the new-chain subset. Asymmetric admission might still emerge but for different reasons than §4's mechanism.

This is a smaller concern than Weak Link 1–3 but worth flagging.

---

## §4 Auditor verdict

**As Claude-B-class auditor, I do not accept the M2 → M3 upgrade on the basis of Path-A.** Reasons:

1. **Step 7 of the §4 argument has a hidden assumption** (channel-uniqueness at locus) that is not supplied by spatial homogeneity. The argument is structurally promising but not D-via-I derivable from existing primitives as stated.

2. **The strict reading that supplies the closure is inconsistent with the framework's empirical match.** If step 7 holds, antimatter cannot exist in any regime — contradicting observation. If step 7 doesn't hold strictly, the closure doesn't follow.

3. **The OPEN items in CommitPhaseInheritance §5** (strict-vs-approximate homogeneity in ignition regime; V5 cross-boundary phase content) are flagged but they are not incidental — they directly affect whether step 7 closes.

The §4 argument supplies a **structurally promising mechanism candidate** that does not close at substrate-graph D-via-I level under audit. It does close at the level of "strongly natural identification worth declaring as paper-specific postulate" (Outcome 2 from CommitPhaseInheritance §6). Path-B is the honest path; Path-A is overclaim.

**Verdict tier impact:** baryogenesis paper remains M2. Two options for handling the new memo content:

**Option B-1 (preferred):** Declare **P-CommitPhaseInheritance** as a *second* paper-specific postulate in Paper_ED_Baryogenesis_Open. *"In the post-SCBU saturation regime, P11 commitment events at substrate locus $\ell$ create new chain content with P09 phase $\pi_{\mathrm{commit}}(\ell) = \pi_K(\ell)$. Substrate-graph derivation OPEN; declared as paper-specific postulate per Paper_095 §2.3."* This closes the asymmetric-admission OPEN row at D-via-I via the production-side mechanism, **at the cost of a second declared postulate.** Verdict remains M2 with two postulates.

**Option B-2 (alternative):** Hold the question OPEN at current M2. Keep P-BinaryAdmission as the only declared postulate; leave asymmetric admission OPEN; cite Memo_ED_CommitPhaseInheritance as a candidate substrate-graph mechanism under investigation but not yet closed. This keeps the framework cleaner (single postulate) but loses the closure of asymmetric admission.

**Trade-off:** B-1 trades one OPEN row for one declared postulate. B-2 keeps the substrate-research frontier honest at the OPEN level. **Neither is strictly worse than the other** — the choice depends on whether the user prefers more closure (B-1) or fewer declared postulates (B-2).

**My recommendation as auditor:** B-2 (hold OPEN), with explicit citation of the CommitPhaseInheritance candidate mechanism as a substrate-research frontier item. Reasons: (i) the framework currently has one postulate; adding a second moves it from "clean M2" to "loaded M2"; (ii) the CommitPhaseInheritance candidate may yet close substrate-graph-derivably via further work on Weak Links 1–3; (iii) the corpus's discipline of honest OPEN-flagging is more important than the closure of one specific audit row.

---

## §5 What Path-A would need to actually close

To make Path-A genuinely D-via-I rather than postulate, the following sub-derivations would need substrate-graph closure:

- **(a) Substrate-graph proof that the post-SCBU ignition regime substrate has channel-uniqueness at each locus** (only one channel per kernel-arrow direction, with phase $\pi_K$). This is stronger than spatial homogeneity and not supplied by SC-4.x scale-collapse.
- **(b) Substrate-graph mechanism for anti-aligned chain creation in post-saturation regimes** that does not violate channel-uniqueness in (a). These two requirements appear in structural tension; (a) makes (b) impossible. The framework needs either a regime-dependent channel structure (channel-uniqueness in saturation, channel-multiplicity post-saturation) or a different mechanism entirely.
- **(c) Substrate-graph determination of whether V5 cross-boundary memory carries P09 phase content.** If yes, supplies additional phase references competing with $\pi_K$.

Closing (a) + (b) + (c) substrate-graph-derivably would supply Path-A. Currently none close. Until they do, Path-A is overclaim and Path-B is the honest framing.

---

## §6 Recommended next exploration

If continuing the baryogenesis arc:

1. **Examine Weak Link 1 substrate-graph rigor.** Is "channel-uniqueness at each locus" derivable from any corpus content (perhaps via Paper_ED_SC_4_9 saddle Hessian structure + Paper_072 individuation)? Or is it strictly an additional assumption beyond spatial homogeneity? This is the central audit question.

2. **Examine Weak Link 2 resolution.** Can the framework supply a substrate-graph mechanism for anti-aligned chain creation in post-saturation regimes without violating channel-uniqueness in saturation? If yes, supplies (b) above. If no, the framework as currently structured cannot match the small-but-nonzero antimatter observation regardless of Path-A vs Path-B.

3. **Examine Weak Link 3.** Spot-check Paper_090 (V5 cross-chain) and Paper_ED_CCC §3.4 to determine whether V5 cross-boundary content has P09 phase structure. If yes, additional substrate-side phase references exist; channel-uniqueness fails; alternative substrate-graph mechanism for asymmetric admission needed.

**Until at least Weak Link 1 closes substrate-graph-derivably, I would not accept M2 → M3 upgrade for baryogenesis.** The current M2 framing with one postulate (P-BinaryAdmission) and asymmetric admission OPEN is the honest substrate-research state. Adding a second postulate (P-CommitPhaseInheritance) or upgrading to M3 on Path-A would, under audit, represent the kind of "FORCED-without-D-row" overclaim that the corpus's discipline is designed to prevent.

---

**End Memo_ED_CommitPhaseInheritance_Audit.**
