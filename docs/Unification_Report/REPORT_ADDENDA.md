# Unification Report — Addenda & Updates (post-v1.0)

The flagship report (`ED Generative/ED_UnifiedFramework_Report.md`, released `unification-report-v1.0` @ `d4e8647`) is **frozen**. New findings, sharpenings, and corrections that arise after the release accumulate **here** rather than editing the report in place. This list is the raw material for a future consolidated update / v2.

Format per entry: what changed, tier, where it lives, and which report box/weapon it touches.

---

## A1 — The V5 budget is one envelope, not three postulates (Class-C plateau sharpening)

**Date:** 2026-07-14. **Touches:** §14 weapon #4 (Class-C error-correction plateau); cross-arc to §6 (Page curve) and the entanglement box (monogamy).
**Corpus paper (cite this from the report):** `ED Generative/physics-papers/substrate-evaluation/Paper_V5UnifiedBudget.md`. Working derivation: `event-density/theory/V5_Characterization/V5_UnifiedBudget_Consolidation.md`.

The three separately-postulated finite V5 budgets — monogamy's `W_V5` (Paper_065), the Class-C plateau's `B_cross,max` (Paper_058), the Page curve's `B_ent,max` (Paper_050) — are **projections of one bounded V5 envelope** `W_max = ∫F_V5` (finiteness form-forced by Paper_090 §4.1–4.2 + P04). Paper_050 already calls its budget "related but distinct" from 058's = same parent, different projection factor. Collapses three inherited postulates into **one inherited scale + O(1) projections** (the KM-II "one Λ, two descriptions" move).

Two forced relations fall out, independent of the inherited scale:
- **R1 — universal-in-complexity onset (a band in the proxy).** The plateau onset is at fixed correlation-content `B_cross,max` for every architecture; it is a *band* in code distance (`R_C^sat = B_cross,max/α`, `α` architecture-specific), a *point* in the substrate variable. Same figure as the Class-A mass band (sharp in `M_eff`, band in kDa). *(AP's "it's internal complexity, not mass" reframe, made precise.)*
- **R2 — fixed O(1) ratios across arenas.** `B_ent,max/B_cross,max = f_ent·g_∂/ρ_loc`, `W_V5/B_cross,max = 1/ρ_loc` — the inherited scale cancels, so the plateau height, the monogamy bound, and the Page time are one scale through three fixed windows.

**Tier:** parent form-forced; three-as-projections structural; R1 derived-conditional; R2 ratios forced (values O(1)-inherited-shape); absolute `Γ_plateau` inherited (do NOT chase — V5 substrate constant, 5 envelope passes failed).
**Falsifiers:** F-R2 (two arenas' budgets don't reconcile to one `W_max` → single-envelope false); F-R1 (two Class-C architectures plateau at different content).
**Buys #4:** from "floor at unknown height" → "floor whose height ratio to monogamy + Page curve is fixed, onset a fixed point in complexity."

## A2 — R2 partially pinned: the entanglement projection = the area-law tiling (≈ 0.88 bits/cell)

**Date:** 2026-07-14. **Touches:** A1's R2; §6 (Page curve / area law); §14 #4.
**Source:** `Paper_HorizonTilingThreeCounts` + `evaluation/AreaLaw_Arc/edge_density_coefficient.py`; `Paper_039` §3.5 (V5 entanglement straddles).

The straddling-edge count — entanglement-carrying V5 edges crossing a boundary at `ℓ_V5 ~ ℓ_P` — is **measured ≈ 0.88 per Planck cell**, converging with the frozen-state (0.78) and holographic (1) counts on ~1 bit/Planck-cell. That number **is** R2's entanglement/boundary projection factor `f_ent·g_∂`, now pinned (measured) and tied to Bekenstein–Hawking `S = A/4`. So the **Page-curve/monogamy side of R2 is anchored to the area law.**

## A3 — R2 fully closed: `ρ_loc = 1`, so `W_V5 : B_cross,max : B_ent,max = 1 : 1 : 0.88`

**Date:** 2026-07-14. **Touches:** A1/A2; §14 #4, §6, entanglement box. **Paper:** `Paper_V5UnifiedBudget` §5.

The remaining factor `ρ_loc` is a **structural identity, not a bulk measurement**: `W_V5` (065, per-chain `∫K_V5` over partners) and `B_cross,max` (058, per-locus cross-chain content) are the *same* `∫K_V5 = W_max` — one budget spent two ways (entanglement partners vs redundant-encoding channels), identical at the P08 substrate grain. So **`ρ_loc = 1`: the monogamy bound *equals* the plateau budget.** With A2's entanglement factor `≈ 0.88`, **R2 is fully pinned: `W_V5 : B_cross,max : B_ent,max = 1 : 1 : 0.88`** (absolute `W_max` inherited; the common `ℓ_V5` DCGT-renormalization cancels in ratios).

**Net of A1–A3:** the Class-C plateau height is no longer a free inherited number — it equals the monogamy bound and is `1/0.88×` the Page-curve budget. Weapon #4 interlocks with entanglement (monogamy) and black-hole (Page/area-law) through one V5 kernel. Absolute scale still inherited (don't chase); the ratios + R1's complexity-universal onset are the failable content.

## A4 — Candidate fourth face: Quantum Darwinism redundancy (a *measurable* proxy for #4)

**Date:** 2026-07-14. **Touches:** A1–A3; §14 #4; the einselection/QM keystone. **Status:** candidate (scoping) — **superseded by A5; its content (lit check, Riedel–Zurek constraint, observable) is absorbed into A5's corpus paper** `ED Generative/physics-papers/substrate-evaluation/Paper_QuantumDarwinism_RecordBandwidth.md`. Scoping note: `event-density/theory/V5_Characterization/V5_QuantumDarwinism_FourthFace_Scoping.md`.

AP's idea: a per-locus cap on redundant *classical* encoding is Quantum-Darwinism territory, and it might carry an observable edge, falling out for free. Assessment: **it holds as a candidate fourth projection of `W_max`.** QD redundancy `R_δ` (number of environment fragments each carrying a full classical record of the einselected pointer state) is capped by the same finite budget, `R_δ ≲ W_max/w_record`. The corpus has einselection (QM keystone) + the V5 budget but **no QD treatment** — this is new.

**Observable edge (why it may beat #4):** standard physics lets *classical* info broadcast freely (only entanglement is monogamous), so `R_δ` grows with environment size unboundedly. ED budget-limits *all* cross-chain correlation, so `R_δ` **saturates** at a substrate ceiling `R_max` independent of environment size — the same plateau mechanism as Class-C, but in a **QD experiment** (photonic / cavity-QED objectivity setups), far more accessible than high-code-distance QEC. A QD redundancy measurement would *anchor* `W_max` and, via R2, hand #4 its number.

**Caveats:** needs the QD-in-ED construction (`w_record`, redundancy-plateau geometry) to promote from hypothesis to result; the distinctive premise is "classical redundancy is budget-capped" (ED's all-correlation-is-V5 claim); the test must show saturation *independent of environment size* to separate the substrate cap from ordinary environment-limited finiteness. If it survives → EDG-repo paper + prediction-inventory near-term weapon.

**Literature check (2026-07-14):** Riedel–Zurek (arXiv:1001.3419) natural redundancy (dust grain in sunlight ≈ 10⁸ imprints/μs, unbounded linear growth) rules out a lab-reachable cap on *total accumulated* classical redundancy. *(An earlier "redundancy-vs-N = open niche" framing here was stale after the repair: under the live/committed accounting a slow redundancy-vs-N protocol shows no flattening and ED predicts none — that scan is a falsification channel (F-QD-3), not a confirmation channel. The live observable moved to sustained coherent width; see A5.)* Defensible ED version = cap on **live (uncommitted)** V5 correlation only (all three existing faces are live; P11-committed records leave the budget per Paper_050's recording mechanism) → the QD face becomes a **record-formation bandwidth** limit, not a total ceiling. Construction step must fix the live-vs-committed accounting; observable shifts to rate/live-window saturation. Details in the scoping note.

## A5 — QD construction RUN: committed records are free, live redundancy is budgeted; GHZ-width ceiling commensurate with the Class-C plateau

**Date:** 2026-07-14. **Touches:** A1–A4; §14 #4; QM keystone (einselection). **Corpus paper (cite this):** `ED Generative/physics-papers/substrate-evaluation/Paper_QuantumDarwinism_RecordBandwidth.md`.

The live-vs-committed accounting is **already in the corpus**: Paper_090 §6 splits horizon correlation into "committed structure (P11) interior-confined" vs "uncommitted-entanglement amplitude straddling." With P11 no-erasure + A1 (correlations persist at zero channel capacity), the **accounting theorem** (D-structural) follows: a committed record consumes no V5 budget. Consequences:
- **Unbounded objectivity, derived:** accumulated classical redundancy grows without bound because the classical IS the committed — ED derives Riedel–Zurek-scale everyday redundancy from P11, rather than being threatened by it.
- **Live cap (D, form):** simultaneous uncommitted directly-correlated fragments `N_live ≤ W_max/w̄` per locus; record-formation bandwidth `dR/dt ≲ N_live/τ_commit`. Topology caveat stated (hub yes, path-circuit no).
- **P-QD-LiveWeight (declared, consistency-forced):** uncommitted branch-basis correlation consumes pairwise V5 weight — the same accounting 058's Class-C budget already uses (QEC redundancy = live branch-type correlation) and, with ρ_loc = 1 (A3), the same `W_max`. Denying it while keeping the plateau is not an available position.
- **The weapon:** GHZ-type branching-width ceiling `N_max ~ W_max/w_min`, **commensurate with the Class-C plateau** (one budget, one content category; R2 extends to `1:1:0.88:r_QD`). Standard physics has neither ceiling. **Existing floors (content-rule-converted, corrected post-B/A7):** 120-qubit certified-GME GHZ at F=0.56 (IBM 2025, arXiv:2510.09520) → guaranteed ≈1 bit/locus, ≈28 under benign-junk = `W_max/w_min ≳ 10⁰–10¹`, rising with every larger/higher-fidelity certified broadcast-type state. (d=7 codes floor weakly — topological per-locus load is O(1); see A6.)
- **Sharp falsifier F-QD-1:** a confirmed plateau in one arena at content `X` + certified widths ≫ X-equivalent in the other kills the single-accounting claim.

**Tier:** accounting theorem D-structural; live cap D (form); width ceiling + commensurability D *conditional on P-QD-LiveWeight* (declared, 058-consistency-motivated); absolutes inherited.

## A6 — The Proxy Conversion Doctrine (one rule set replaces five local patches)

**Date:** 2026-07-14. **Touches:** §14 (all prediction bands), Class-A wall, Class-C plateau, A1–A5. **Corpus paper (cite this):** `ED Generative/physics-papers/substrate-evaluation/Paper_ProxyConversionDoctrine.md`.

Pattern caught adversarially (three same-shaped patches in one week: 058's α resurfacing, w_record in QD scoping, the certified-width content rule): the corpus kept inventing local proxy-to-content conversions (α, αβ, Q, f_ent·g_∂, w_min...) with no general rule. The doctrine paper states it once: **(D1)** predictions sharp in substrate content, banded in any proxy (generalizes R1 + the Class-A mass band); **(D2)** conversions are per-architecture structural constants, never universal, never silently transported; **(D3)** where budgets bind, content = per-locus LIVE V5 weight (committed/live split first); **(D4)** empirical floor/ceiling claims must PRE-REGISTER their content rule — qubit-counting is not a content rule. §3 pre-registers the live-width rule + works it on GHZ (per-locus ~N−1, certification-discounted), graph states (per-locus O(1) — the 414-qubit certification floors ~nothing), topological codes (per-locus O(1) in d by design).

**Resolves the "self-tightening lock" objection** (every bigger cat state seemingly pushing weapon #4's plateau out of near-term reach): with the honest certified floor at 10⁰–10¹ bits/locus, the certified frontier (~120 qubits now, ~10³ in 2–5 yr) probes the broadcast-side wall *directly* — the near-term face survives on the broadcast leg. **The code-distance leg is weaker than first stated (post-B):** if topological per-locus load is O(1) in d, the plateau in code distance does not occur via this mechanism for topological codes at all — the leg transfers entirely to broadcast/repetition-type redundancy (and 058 §4.3 itself classes surface codes as hybrid B+C, not pure C; syndrome measurements are P11 commitments = budget-free, strengthening the branch). Rescue branch = 058's α_topological non-small. **New open item (deliberate):** encoding-dependence of 058's α = the highest-value review question for the Class-C arc.

## A7 — Claude B corpus review of the three-paper package: architecture survives; five fixes applied

**Date:** 2026-07-14. **Touches:** A1–A6 papers.

Full adversarial corpus review (against 090/065/058/053/056/050/A1/keystone/ED-09.5).

## A8 — α_topological SETTLED = 0: the plateau relocates to broadcast-type redundancy; weapon #4 restructured

**Date:** 2026-07-14. **Touches:** §14 weapon #4 (prediction 4.10), A5/A6. **Corpus paper (cite this):** `ED Generative/physics-papers/q-compute/Paper_058b_PlateauDomain_AlphaTopological.md`. Predictions List 4.10 re-scoped with dated banner.

Settled from the corpus's own commitments (read 058 in full): P-Corr-Budget is per-locus (058 §2 + glossary); V5 is a pairwise finite-reach kernel (090 §3.2), so all live correlation is a pairwise web whose per-locus load = incident degree × weight; topological encoding keeps that web local *by definition* (bounded degree, ~0 distant pairwise correlation, syndrome records P11-committed = budget-free). So per-locus `B_cross ~ z·w_pair`, **constant in code distance — the 058 §3.3 saturation never triggers for topological codes: α_topological = 0.** P-Redundancy-Mapping's linear regime = the broadcast/hub regime. This is a domain-sharpening 058 pre-hedged (Preamble 8, §4.3 hybrid classification, falsifier 6.4), not a correction.

**Weapon #4 restructured (net of A1–A8):**
- **Topological branch = prediction of absence:** no substrate plateau in surface-code distance via this mechanism — converts the brewing tension with Willow's clean Λ≈2 suppression into a *match*.
- **Active pair (both public data streams today):** (a) **repetition-code floor persistence** — Google's d≤29 repetition codes deviated from exponential suppression above d≈15, apparent ~10⁻¹⁰/cycle floor from rare correlated bursts (Nature 638 / arXiv:2408.13687): the plateau *shape in exactly the encoding type the mechanism binds*; WATCH item, not confirmation (mundane cosmic-ray/TLS attribution live; discriminator = floor survives shielding/mitigation + cross-platform-consistent converted content); (b) **cat-width ceiling** (A5), same budget at fixed ratio. One number family: repetition floors : cat widths : monogamy : Page, through `1:1:0.88:r_QD`.
- **R1 finalized:** topological architectures drop out of the band; R1 ranges over broadcast-type platforms.
- **Falsifiers re-scoped:** continued topological-distance suppression no longer bears on P-Corr-Budget; the kill shots are post-mitigation broadcast suppression to zero, or inconsistent post-mitigation floor content across platforms.

Loop closed: doctrine §3.4 marked settled; QD paper + UnifiedBudget R1 caveat synced; Predictions 4.10 + §6 updated; PAPERS_INDEX + q-compute README rows added. **Survived attack, stated plainly:** the one-budget architecture; ρ_loc=1 vs QD per-locus loading (consistent — QD §4.1 is literally 065's partition); committed-records-free vs 050 (no friction); F-QD-3 discipline (no committed-saturation test anywhere); einselection usage; novelty (no prior QD treatment in corpus); 056/0.88/ρ_loc catalog rows. **Fixed on B's findings:** (1) doctrine's Q row was misattributed (Q lives in the ED-09.5 envelope arc as the canonical-PDE quality factor, NOT Paper_085/mobility — two report-§14 items had been fused); (2) "P-QD-LiveWeight consistency-FORCED by 058" downgraded to *consistent-with* (058 accounts per channel, silent on content character; near-circular via the encoding fork); (3) floor arithmetic done honestly: F=0.56 N=120 GHZ guarantees ≈1 bit/locus (adversarial junk), ≈28 (benign junk) → 10⁰–10¹ not 10¹–10²; (4) committed/uncommitted bifurcation retiered from "I (corpus)" to **D-structural (generalization)** — 090 §6.4's clause is horizon-local; the generalization is the paper's own (and unique corpus-consistent) construction; (5) topological failure branch strengthened from "demotes" to "does not occur via this mechanism" + 058's hybrid classification noted. Minor: 065 citation un-rewritten ("live" flagged as this paper's restriction); A1 demoted from "sharp form" to direct support (V5-free substrate); α row re-sourced; w_pair added to catalog; R1 caveat added to UnifiedBudget §4.
