# Quantum Darwinism as a Fourth Face of the V5 Budget (Scoping)

**Series:** ED — V5 Characterization (companion to `V5_UnifiedBudget_Consolidation.md` / `Paper_V5UnifiedBudget`)
**Status:** Scoping note (candidate, not a result). AP's idea 2026-07-14: "a per-locus cap on redundant *classical* encoding is Quantum-Darwinism-adjacent, and it might have an observable edge — it would fall out for free."
**Verdict:** a real candidate fourth face; the "free" part holds; the observable edge is potentially *more measurable than weapon #4 itself*, and distinctive. Needs a QD-in-ED construction to promote to a result (then an EDG-repo paper per `workflow_report_addenda`).

---

## The idea

The V5 unified-budget paper showed one bounded envelope `W_max` underlies monogamy (065), the Page curve (050), and the Class-C error-correction plateau (058), in ratios `1:1:0.88`. **Quantum Darwinism (QD)** — the redundant imprinting of a system's pointer-basis (classical) information into many environment fragments, the mechanism behind classical objectivity — is *the same structure in a fourth arena*: a **per-locus cap on redundant classical encoding**. If QD redundancy is a fourth projection of `W_max`, it (i) falls out of the existing consolidation for free, and (ii) is measurable in a way the Class-C plateau is not.

## ED-native check (does it hold?)

ED already has the two ingredients: **einselection is primitive** (the arrow selects the pointer/channel basis — QM keystone), and **V5 caps cross-chain correlation** at `W_max`. A "classical record in an environment fragment" is, in ED, an **environment chain whose V5 cross-chain correlation carries the system's committed channel** (P11 record). The number of environment fragments that can *each* hold an independent full record is then capped by the finite budget:
$$
R_\delta \;\lesssim\; R_{\max}\;\sim\; W_{\max}/w_{\rm record},
$$
`w_record` = the V5 correlation cost of one full classical record. So QD redundancy is a **fourth projection of `W_max`** — same parent, its own O(1) factor — and R2 extends automatically (fixed ratio to plateau / monogamy / Page). *This is the "free" part, and it holds.*

## The observable edge (why it may beat weapon #4)

**The distinctive prediction:** in standard physics, *classical* information broadcasts freely (only entanglement is monogamous, 065), so QD redundancy `R_δ` grows with environment size with no fundamental ceiling. In ED, **all** cross-chain correlation — classical records included — is V5-mediated and budget-limited, so **`R_δ` saturates at a substrate ceiling `R_max` independent of environment size.** This is the *same mechanism as the Class-C plateau* (redundant encoding hitting the finite `W_max`), transposed to environmental objectivity.

- **Test:** measure `R_δ` (redundancy = the mutual-information plateau *length*, not its height `H_S`) vs environment size. ED predicts a **saturation** (curvature change to flat) at `R_max`; standard QD predicts continued growth until the environment is merely exhausted. Same signature as the Class-C error-vs-distance plateau, in a **QD experiment** (photonic / cavity-QED / trapped-ion objectivity setups) — far more accessible than high-code-distance QEC.
- **Payoff for #4:** a QD redundancy measurement *anchors* `W_max`, which by R2 propagates to the Class-C plateau height (`1:1:0.88:R_max-factor`). So QD gives weapon #4 the empirical handle it lacks — and is a distinctive weapon in its own right.

## Honest caveats / tier

- **Candidate, not derived.** Needs the QD-in-ED construction: pointer basis = einselected channel (have it); fragment = environment chain V5-correlated to the system (plausible); `w_record` and the redundancy plateau geometry (unbuilt). Until built, `R_δ` as a clean `W_max` projection is a hypothesis.
- **Load-bearing distinctive premise:** "classical redundancy is budget-capped" rests on ED's claim that *all* correlation is V5-mediated (not free classical broadcasting). That is the deep, distinctive ED commitment — and the thing the observable test would actually probe. State it as such.
- **Distinguishability risk:** the saturation must be shown *independent of environment size* to separate the ED substrate cap from ordinary environment-limited finiteness. The test design is the make-or-break.

## Experimental literature check (2026-07-14, DONE)

**State of the art.** Three platform families have observed QD; all measure the mutual-information-vs-fragment-size "plateau" (objectivity signature), none measure redundancy vs *total environment size* (our signature):
- **Photonic simulator** (Chen et al. 2019, arXiv:1808.07388): 6 photons; observed classical-info redundancy + quantum-correlation suppression in fragments.
- **NV-center diamond** (Unden et al. 2019, "QD spotted in diamond spins"): ~4 nuclear-spin fragments; one ¹³C read gives most of the NV spin info, extra spins add little. First "natural environment" demo. Scaling flagged as the hard problem.
- **Superconducting circuits** (2025, Sci. Adv. / arXiv:2504.00781): **current SOTA** — 2 system + 10 environment qubits; MI plateau at `H_S ≈ 1` for fragments m=2..8, discord ≈ 0 in the plateau. Explicitly does *not* explore scaling beyond N=10.

**Feasibility of our test:** ~~redundancy-vs-environment-size is an unmeasured, open niche... ED predicts departure from linearity at `R_max`~~ **[SUPERSEDED 2026-07-14 — this framing predates the live/committed repair and is wrong under it.]** Under the repaired accounting (committed records exit the budget), a slow/sequential redundancy-vs-N protocol shows **no flattening, and ED predicts none**: each record commits and frees its budget, so `R_δ` grows linearly regardless of `W_max`. The redundancy-vs-N scan is therefore *not* a confirmation channel — it flipped to a **falsification channel** (observed saturation of accumulated redundancy would falsify the accounting theorem; F-QD-3 in the paper). The live observable is **sustained coherent branching width** (GHZ/cat width, QEC code distance): live content that cannot commit-and-free. QD-simulator states (Ciampini/Chen/2504.00781) do probe live width, but at N ≤ 10 — far below the 120-qubit GHZ floor, so cat states and code distance, not QD redundancy scans, are the strong probes.

**The critical catch — Riedel–Zurek natural redundancy (arXiv:1001.3419).** For a 1 μm dust grain in sunlight, position is imprinted **~10⁸ times in 1 μs**, and `R_δ = (t/τ_D)/ln[(2δ ln2)⁻¹]` grows *linearly in time without bound*. Everyday objectivity therefore involves accumulated classical redundancy of astronomical size. Consequence for ED:
- If ED caps **total accumulated classical** redundancy, `R_max` must be ≳ 10⁸·(seconds of illumination) to survive daylight — astronomically large, hence **lab-unreachable**, and the naive saturation test dies.
- The defensible ED version is almost certainly a cap on **live (uncommitted) V5 correlation** only: all three existing faces (monogamy, Class-C QEC coherence, horizon entanglement) are *live* correlations, and P11-committed classical records plausibly leave the budget (cf. Paper_050's info-preserved-by-recording: records persist, entanglement budget transfers). Then the QD face is a cap on the **record-formation bandwidth** — how many fragments can be *in the process of* imprinting simultaneously — i.e. a redundancy-generation *rate* limit `dR/dt ≲ W_max/(w_record·τ_commit)`, not a total ceiling. Accumulated committed copies grow freely (consistent with sunlight AND with the Class-C plateau, whose QEC redundancy must stay live/coherent — that's why *it* saturates at reachable scale while classical records don't).

**Net:** the literature check *saved the arc from a wrong prediction* (total-redundancy saturation would be in tension with everyday objectivity or unreachable) and sharpened the target: the construction step must decide live-vs-committed budget accounting, and the observable becomes a rate/bandwidth saturation (drive record formation faster, watch the formation rate cap) or the live-window redundancy. Harder than the naive test, still potentially distinctive: standard physics has no fundamental record-formation bandwidth.

## Construction RUN (2026-07-14) — promoted to corpus paper

Done: `ED Generative/physics-papers/substrate-evaluation/Paper_QuantumDarwinism_RecordBandwidth.md`. Key results: accounting theorem (committed records exit the budget; grounded in Paper_090 §6's committed/uncommitted split + P11 + A1); unbounded objectivity derived (Riedel–Zurek-safe); live cap `N_live ≤ W_max/w̄` + formation bandwidth (D, form); P-QD-LiveWeight declared (058-consistency-forced) → GHZ-width ceiling commensurate with the Class-C plateau (the weapon; F-QD-1 sharp falsifier). Existing floors: 120-qubit certified GHZ (arXiv:2510.09520), d=7 codes → `W_max/w_min ≳ 10²`. GHZ topology caveat (hub vs path) handled in §4.3/§5. Logged as addendum A5.
