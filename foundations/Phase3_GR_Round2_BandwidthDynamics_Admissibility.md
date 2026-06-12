# Phase-3 GR — Round 2: Admissibility of a Dynamical-Bandwidth Rule

**Foundations admissibility test. Not a rule proposal, not a corpus edit, not a new primitive.**
Tests whether ED can admit a *dynamical bandwidth law* `ḃ_uv = F(ρ_u, ρ_v, ∇ρ, b_uv, …)` — the state→structure coupling implicated as the shared missing piece in **A2** (emergent decoupling), **B4 Step 4** (active charge), and **Phase-3 GR Round 1** (full EFE).
**Discipline (the crank rail):** the rule must be *forced/admissibility-constrained*, never reverse-engineered to yield EFE. Run forward (derive the admissible class from the primitives + conservation), not backward from Einstein.

---

## 1. Target

A dynamical bandwidth rule updates edge bandwidths `b_uv` over time as a function of node state, subject to: it must preserve P02 adjacency and P05 transport semantics, introduce no new primitive, and violate neither P11 irreversibility nor P13 time-homogeneity. The certified simulator holds `b` static (a single scalar read by the tie-break); the question is whether *that staticness is a primitive commitment or merely a simplification.*

## 2. The decisive finding — the coupling is already declared

It is a simplification, not a commitment. **P04 + P11 already specify a ρ↔b coupling that the certified simulator omits:**

- **P04 §1.5** — the four-band partition includes a **commitment-reserve band** "consumed by P11 commitment events."
- **`commitment.md`** — a commitment "**draws from commitment-reserve bandwidth and converts channel-distributed bandwidth into single-channel concentrated bandwidth**" — bandwidth is *redistributed* (drawn from reserve, concentrated into the selected channel), not invented or destroyed.
- **`commitment.md`** — `Γ_commit ~ b_int / (commitment-reserve budget)`: the commitment *rate* depends on the reserve level — a built-in feedback.

So a dynamical bandwidth law is not a foreign extension; it is the **formalization of the commitment-reserve dynamics the primitives already declare**. The certified Bits simulator drops it (collapsing `b` to a static tie-break scalar) precisely because the determinability-boundary measurement did not need it. Round 2's question therefore narrows: *does restoring the already-declared band dynamics violate any invariant or theorem?* The answer below is **no, under a monotone/conservative form**.

## 3. Admissibility constraints — checked

| Constraint | Verdict | Reason |
|---|---|---|
| **P04 semantics** (b ≥ 0, additive, four-band) | **Pass** | the rule *is* P04's own commitment-reserve band dynamics; total `b` conserved (redistributed), `b ≥ 0` preserved |
| **P11 irreversibility / ρ monotone** | **Pass** | the rule is *commitment-driven*; ρ stays written only by `commit()` and monotone; the band redistribution is the irreversible consumption P11 already implies |
| **Orientation-blind Σ** | **Pass** | `F` reads ρ/∇ρ/b, never orientation; and `b` enters the **tie-break/admissibility**, never `compute_sigma` — so Σ stays blind even as `b` evolves |
| **Determinism + tie-break totality** | **Pass** | deterministic `F`; node-id remains the final tie-break key, so ties stay resolvable |
| **P02 — no edge create/destroy** | **Pass** | `b_uv → 0` is *capacity collapse*, not adjacency removal; the P02 edge persists at zero P04 capacity (a zero-capacity channel is no channel — pure P04 semantics) |
| **No fundamental metric / continuous field** | **Pass** | operates on discrete edge weights; the metric `g ~ b⁻¹` stays *emergent* from the discrete `b`, honoring the Facts paper's "no fundamental metric" |

Every certified constraint passes for a rule that (i) is commitment-driven, (ii) conserves/redistributes total bandwidth, (iii) reads no orientation, (iv) collapses capacity rather than deleting adjacency.

## 4. The three GR-required properties

- **A. Geometry responds to matter (ρ → b).** ✅ Commitment events (ρ-dynamics) redistribute `b`; since `g ~ b⁻¹`, the emergent metric responds to matter. Direct.
- **B. Local and relational.** ✅ `F` depends on local node states `ρ_u, ρ_v` and the edge `b_uv` (graph-local) — ED-style locality, consistent with A1's no-nonlocal-influence finding.
- **C. Bianchi-like conservation identity.** ⚠️ **Candidate present, unproven.** Commitment *redistributes* bandwidth (conserves the total budget while moving it between bands/channels). That **bandwidth-budget conservation** (`Σ_bands b = const` per locus, with commitment as the transfer operator) is the natural seed of a contracted-Bianchi identity for the `g ~ b⁻¹` metric. Whether it *is* the contracted-Bianchi (`∇_μ G^μν = 0 ↔ ∇_μ T^μν = 0`) is the Round-3 keystone.

## 5. Candidate forms of F

| Form of `F` | Verdict | Note |
|---|---|---|
| local ρ only — `ḃ_uv = −g(ρ_u+ρ_v)` (drain with commitment density) | **Admissible** | the cleanest reading of commitment-reserve drawdown; monotone in commitment count |
| ∇ρ-driven (P06) — `ḃ_uv = −g(\|ρ_v−ρ_u\|)` | **Conditionally admissible** | P06 is certified, but `\|ρ_v−ρ_u\|` is exactly Σ's Grad term — risk of double-counting/feedback with the selection rule; needs separation |
| second-order `b` (bandwidth curvature) | **Conditionally admissible** | needed for a *curvature-dynamics* analogue; admissible only if it stays local and posits no fundamental metric |
| **monotone / conservative** (drain reserve, redistribute, total conserved) | **Admissible** | matches P11 irreversibility (consumption is one-way) and the redistribution semantics; gives *frozen* emergent cuts |
| **non-monotonic / replenishing** (b can spontaneously increase) | **Inadmissible** | no primitive supplies replenishment; conflicts with the irreversibility of commitment consumption |

The admissible core: **a commitment-driven, monotone/conservative, orientation-blind, local rule** that redistributes the commitment-reserve band — i.e., exactly the dynamics P04+P11 already declare.

## 6. Cross-arc consistency (with an honest refinement of Round 1)

- **A2 — emergent decoupling.** ✅ **Served, strongly.** Commitment-driven drain can push an edge's `b_uv → 0`; bandwidth-gated admissibility then excludes it → an **emergent** decoupling surface, and (drain being one-way) a *frozen* one. This also delivers A1's exactly-zero capacity across the formed cut. The rule unifies A2 (emergence) with A1 (the exact-zero signature) and the Emergent-Decoupling note's named insertion point.
- **Phase-3 GR — matter→geometry.** ✅ **Served, conditionally.** `g ~ b⁻¹` responds to commitments, with budget-conservation as the Bianchi-candidate. The full nonlinear EFE closure is gated on Property C (Round 3).
- **B4 — active charge.** ⚠️ **Refinement of Round 1.** This rule is *commitment/ρ-driven*; B4's charge is *orientation/winding-driven*. The winding reaches `b` only through the **coherence-bandwidth channel** (`b ~ cos²(Δφ/2)`), which B4 Step 2 already showed is the *weak* tie-break channel, with Σ blind by design. So the shared extension is more precisely **one *family* of bandwidth dynamics with two drivers**: the *commitment-driven* member is strong and serves A2 + GR; the *orientation-driven* member is admissible but weak and does not, by itself, give B4 a determined active charge. Round 1's "one missing piece, not three" thus stands as *"one admissible family,"* but B4's member is weak and orientation-blindness remains its separate ceiling.
- **A1 — determinability structure.** ✅ **Preserved.** `F` is local (no nonlocal influence); emergent `b→0` cuts reproduce A1's exact-zero capacity. The rule lets boundaries *form* (A2) without disturbing A1's signature or locality.

## 7. Verdict

**CONDITIONALLY ADMISSIBLE — and the conditions are sharp, not vague.** A commitment-driven, monotone/conservative, orientation-blind, local bandwidth rule violates *no* certified primitive, invariant, or theorem; it is the **formalization of the commitment-reserve dynamics P04+P11 already declare**, which the certified simulator merely omits. Non-monotonic/replenishing forms are **inadmissible** (no replenishment primitive; conflicts with commitment irreversibility). The remaining conditions are: **(C1)** pin down consume-vs-redistribute precisely (the corpus leans *redistribute*, which yields the conservation needed); **(C2)** establish bandwidth-budget conservation as the contracted-Bianchi identity for `g ~ b⁻¹` (Round 3 keystone); **(C3)** show the specific `F` is *forced* by the commitment-rate law `Γ_commit ~ b_int/reserve`, not freely chosen. Meeting C1–C3 would convert "conditionally admissible" to "admissible and forced" — and would be the same step that turns A2 from possible to realized and supplies Phase-3 GR's missing closure.

## 8. Round-3 questions

1. **Bianchi (the keystone).** Is bandwidth-budget conservation (`Σ_bands b = const`, commitment as transfer) the contracted-Bianchi identity for `g ~ b⁻¹`? If yes, the source coupling conserves `T_μν` automatically — EFE-closure-enabling. If no, full EFE is blocked even with dynamical `b`.
2. **Forcing / uniqueness.** Does `Γ_commit ~ b_int/reserve` *force* a unique `F`, or admit an inequivalent family? (The crank-safety gate: a forced `F` is a derivation; a chosen one is a retrofit.)
3. **Stability.** With `Γ_commit ~ b_int/reserve`, does drain self-limit (commitment slows as the relevant band is exhausted → geometry settles) or run away (all `b→0` → universal decoupling)? Determine the sign of the feedback.
4. **Correspondence.** Does the rule recover Poisson/Newton in the linear limit and a nonlinear `curvature = source` beyond it?
5. **Band accounting.** Which band feeds `g ~ b⁻¹` (total vs adjacency vs internal)? The metric's response to commitment depends on this, currently unpinned.
6. **B4's second driver.** Is there an orientation-blind-safe way for the winding to drive `b` strongly (beyond the weak coherence/tie-break channel), or is active charge permanently capped by orientation-blindness?

---

*Round-2 admissibility test only. Verdict: a dynamical-bandwidth rule is **conditionally admissible** — in its commitment-driven, monotone/conservative, orientation-blind form it is the formalization of P04+P11's already-declared commitment-reserve dynamics, violating no certified invariant; the conditions are the Bianchi identity (C2) and the forcing of F (C3), both Round-3. The same rule realizes A2's emergent boundaries and supplies Phase-3 GR's missing matter→geometry closure; B4's active charge needs a distinct, weaker orientation-driven member and stays separately gated by orientation-blindness. No corpus edits, no new primitives, no rule changes.*
