# Arc: Conservation Leaks — Noether symmetries as emergent & scale-dependent

**Status:** SCOPING — **core mechanism VERIFIED against the primitive definitions (2026-08-07)**; full NoetherFlux dynamics-arc read still pending before drafting the paper. Opened 2026-08-07.
**Origin:** AP intuition — *"if time is different everywhere, symmetry doesn't quite make sense, and conservation eventually stops"* — cross-checked against the corpus and found to touch a real, unfilled gap.
**Discipline note:** this is a frame + open questions. Tiers are stated up front so nothing gets over-banked. The base physics (energy not globally conserved in a dynamic spacetime) is **standard GR**, not an ED discovery; ED's possible contribution is grounding/unification (Tier 1) and, speculatively, a departure (Tier 2, held).

---

## 1. The gap (from reading `physics-papers/substrate-evaluation/Paper_HowTheoryCoarseGrainReality.md`)

The ledger paper ("emergent symmetry is forgotten information") builds every emergent symmetry from **order-erasure**: averaging is permutation-blind, so it forgets which commitment came first, and that is where reversibility, unitarity, no-preferred-frame, diffeo-invariance, continuity, and Markov memorylessness come from.

**Its §14 recipe table contains no conservation law.** Energy, momentum — the Noether charges — are absent. This is not an oversight: conservation laws come from a **different discard**. Reversibility comes from forgetting *order*; conservation comes from assuming a *uniform (translation-invariant) backdrop*. The ledger built the first mechanism and never built the second.

The ledger's own §2.2 scope note anticipates this without doing it: *"a blur that keeps fluxes or currents… inherits a direction."* Energy flux in a changing spacetime is exactly such a current — the carrier of the leak.

## 2. The thesis (the new ledger row)

- **Conservation law = the artifact of assuming an exactly uniform backdrop.** Energy ← time-translation invariance; momentum ← space-translation invariance (Noether).
- **The leak:** the substrate's backdrop is only *locally* uniform. Where uniformity fails — dynamic spacetime: cosmic expansion, gravitational collapse, a passing wave — the conserved quantity **leaks**, and the leak is **scale-dependent**: its size is set by how much the backdrop changes across the patch/interval measured over. Gradient, not cliff.
- **Unification payoff:** reversibility (order-erasure) and conservation (uniformity-assumption) become **two discard mechanisms in one ledger**. §15's "a discarded column never fully vanishes; it leaks" now covers conservation too.

## 3. The ED-native mechanism (the load-bearing claim — TO VERIFY, §6)

Candidate resolution, grounded in two existing primitives — **not yet confirmed against the corpus**:

- **P13 (time homogeneity)** = the *law* is the same tick to tick → **local** time-translation symmetry → **local** energy conservation, exact.
- **P11 (commitment-irreversibility, the arrow)** = the *record/state* always grows; the substrate is never globally stationary (cosmic commitment; the horizon / SCBU surface grows). → there is **no global** time-translation symmetry.
- **Together:** local conservation is exact (P13); global conservation leaks (P11). AP's "local vs scale" intuition, grounded in P11 + P13. The leak **is the arrow resurfacing in the energy books** — precisely the §15 pattern (ED's falsifiable content = the discarded column leaking back).

## 4. Corpus-consistency (F4 reconciliation — checked)

`physics-papers/qm-kinematics/Paper_006_5_Schrodinger_Stone.md` codes **F4: "Substrate-level non-conservation of energy *from time-translation symmetry* — would refute the Noether identification of Ĥ as energy."**

- F4 is scoped to non-conservation **where the symmetry holds**. The leak occurs **where the symmetry is absent** (dynamic backdrop) → Noether yields no conserved charge → non-conservation is *expected*, not a refuter. **F4 does not bite.** ✓
- Caveat: this holds *only if* P13 is a **local** symmetry (law-homogeneity), not an exact global one. If the corpus asserts P13 as exact-and-global, substrate energy is globally conserved and the story changes (leak becomes emergent-only). This is the #1 verification item (§6).

## 5. What this fills (corpus silences)

- **"Who pays for the redshifted CMB energy?"** The corpus reproduces the expanding-universe equations (Friedmann via substrate Noether stress-energy → DCGT) but never raises this as a conservation question. Answer on this frame: the backdrop's non-uniformity (the arrow / cosmic non-stationarity) does. The emergent energy leaks because the backdrop grows.
- **A disconnect inside the corpus:** the ledger paper (emergent symmetry) and the NoetherFlux dynamics arc (`Paper_ED_GW_00`, `Paper_ED_Dyn_02`, etc., which *use* Noether machinery to reproduce GR) never cite each other. This arc is the bridge.

## 6. Open questions — VERIFY before promoting to a paper

1. **Is P13 exact-global or local?** Is the substrate globally non-stationary (graph growth, horizon/SCBU)? Read `physics-papers/foundations/Paper_087_13Primitives.md`, `primitives/P11_commitment.md`, `physics-papers/gravity/Paper_028_CosmicDecoupling.md`, SCBU papers. **Load-bearing for §3–§4.**
2. **Does the law-homogeneity (P13) vs state-arrow (P11) split hold in the corpus,** or is it my construction? (memory: "arrow = P11+P13+V1 (T18)" — P13 and P11 are distinct and both feed the arrow; verify the split I'm drawing.)
3. **Read the NoetherFlux dynamics machinery in full** (`Paper_ED_GW_00`, `Paper_ED_Dyn_02`, `Paper_ED_Cos_05`): confirm covariant conservation ∇_μT^μν = 0 is the **local** law (consistent with a global leak), and that global energy is genuinely never discussed.
4. **Is any leak reachable/testable (Tier 2),** or is it all cosmological = exactly GR? (Almost certainly the latter — confirm.)
5. **Does a substrate-level TOTAL exist that stays globally conserved even as the emergent GR energy leaks?** (The Tier-2 hook — hold as a question, do not answer prematurely.)

## 6.5 VERIFICATION RESULTS (2026-08-07) — the mechanism holds, stronger flavor

Read `Paper_087_13Primitives.md` (P11, P13 definitions) + `Paper_006_5` (F4).

- **Q1 — is P13 local or global? RESOLVED.** P13 is defined as a symmetry of the **law**, not the state: *"the substrate-level laws at time t are identical to those at time t'… ∂_t is a substrate-level symmetry."* A time-symmetric law gives a **local conserved current** (Noether), not a globally conserved charge — a global charge needs a stationary *state* (a timelike Killing symmetry), which P13 does not assert. This is exactly the GR structure (covariant law, no global energy in dynamic solutions). → **local conservation exact; global conservation not guaranteed.**
- **Q2 — does the P11(state-arrow)/P13(law-symmetry) split exist in the corpus? RESOLVED, YES, verbatim.** P13's own definition: *"ensures P11's commitment-direction is the **only** temporal-asymmetry primitive."* P11: *"The collapse is irreversible; no substrate-level operation maps post-commitment to pre-commitment state"* — the state is non-stationary by construction. The split is **not my construction**; it is explicit in `Paper_087`. The conservation-leak mechanism is therefore **latent in the existing primitives** — it just was never connected to the conservation ledger.
- **Q3 — NoetherFlux machinery local-only? CONFIRMED at the math level** (`GW_00`, `Cos_05` read; `Dyn_02` via survey). The substrate Noether stress-energy `T^{μν}_sub` (from P03+P13 translation-invariance + the S_sub functional) is used as a **local flux**, DCGT-coarse-grained to reproduce the standard radiation/Friedmann laws; **no global energy is ever defined.** Two positive corroborations:
  - **`GW_00`:** GW energy = "local ED-gradient load"; GR's stress-energy **pseudotensor is explicitly *Replaced*** (row 10, D-via-I). The pseudotensor is GR's failed attempt at *global* gravitational energy — ED discards it for a local quantity. ED affirmatively leans local, not global.
  - **`Cos_05` (bonus — the end-state branch):** dark energy = late-universe **saturation regime**, "expansion-driven dilution drives the substrate toward **uniform-Ψ**" → de Sitter. So the backdrop's non-uniformity (the leak source) **dilutes away** toward the end; the leak is largest in the dynamic/structured epoch and **shuts off** at the uniform de Sitter end — where symmetry (and conservation) is *restored*. This grounds AP's CCC "ultimate uniformity restores symmetry" branch in a corpus result, and gives the leak a **time/scale profile**: big early, vanishing late.

**Verdict:** the mechanism holds, and it is the **stronger** branch (AP's note Q1): local conservation exact from P13, global leak from the arrow P11, **substrate-native** (not emergent-only). The two halves are already in the corpus; the arc's contribution is to **connect them to the conservation ledger** and name the leak.

**Honesty brake (unchanged):** this still **reproduces standard GR** (global energy non-conservation in dynamic spacetimes is textbook GR). "Stronger Tier-1" means the *grounding* is substrate-native, not that the claim became novel. No new prediction. Q5 (a substrate-level total conserved even as the emergent energy leaks) remains the only Tier-2 hook, still HELD.

## 7. Tiers (do not over-bank)

- **Tier 1 — grounding + unification (the deliverable).** Same tier as the ledger itself, which openly says *"a reading, not a theorem, no new results."* Add the conservation row + the P11/P13 mechanism, unify reversibility and conservation, fill the silences. **Reproduces standard GR** global energy non-conservation. Modest, solid, publishable as an EDG companion to the ledger.
- **Tier 2 — novel scale-dependent departure from GR (HELD, not chased).** Would need ED's backdrop to differ from GR's; the corpus is presently committed *against* it (F4). A research **question**, not a result. Chasing it as a claim would be the crank move.

## 8. Next steps

- Verify Q1–Q3 (read the primitive + cosmology + dynamics papers).
- If the P11/P13 mechanism holds → draft the Tier-1 grounding note in full (here in this arc).
- Log the thread in `event-density/docs/ED_Research_Targets.md`.
- Final cold-reader paper → EDG (`ED Generative/physics-papers/`), sibling to `Paper_HowTheoryCoarseGrainReality.md`.
