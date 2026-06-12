# Phase TieBreak — Tie-Breaking Rule Specification

**Evaluation:** Architectural Distillation of the Event Density *substrate* (discrete relational layer)
**Phase:** TieBreak (architectural closure)
**Status:** Fills the open slot from Phase B §3; closes the Phase F Determinism CONDITIONAL
**Date filed:** June 2026
**Author:** Allen Proxmire
**Related:** `Phase_B_ArchitecturalSpecification.md` §3 (open slot); `Phase_E_ConstraintSurface.md` §7 (stratified orientation); `Phase_F_CriteriaEvaluation.md` §5 (Determinism CONDITIONAL)

---

## 1. Purpose

This document fills the single open architectural slot in the ED substrate specification: the **tie-breaking rule** flagged at Phase B §3 and responsible for the lone CONDITIONAL in Phase F (Determinism, Component 4 — unique local maximizer).

The evolution rule commits the maximum-Σ candidate; where two or more candidates share the maximal Σ, the rule as specified does not determine which commits, so unique determination holds *generically* but not *universally*. The goal here is to specify a **deterministic tie-break** such that Σ-maximization always yields a unique next step — closing the gap and upgrading Determinism from CONDITIONAL to PASS.

This is an architectural specification, not a new axiom: it fills a slot the architecture left open, using only structure the axioms already supply.

---

## 2. Requirements for a Valid Tie-Break

A valid tie-break **must be:**

- **Deterministic** — no randomness; the same tied set always yields the same selection.
- **Local** — uses graph-local information only, drawn from the bounded candidate neighborhood.
- **Finite-reach compatible** — reads no information past a decoupling surface.
- **Irreversibility compatible (P11)** — selects only among forward candidates; never uncommits.
- **Stratified-orientation compatible (Phase E §7)** — does not disturb the derivation of orientation as a within-stratum invariant; in particular, requires no cross-stratum orientation comparison.

A valid tie-break **must not:**

- introduce new non-local structure;
- contradict any established invariant (I1–I5);
- alter Σ or any of its components (Coh, Str, Grad). The tie-break acts strictly *downstream* of Σ-maximization, on the already-computed Σ-maximal set.

---

## 3. Candidate Tie-Break Mechanisms

The two mechanisms named in Phases D and F.

**Mechanism 1 — Orientation-ordering.** Break ties using the orientation channel (B5): prefer the candidate whose orientation is most consistent with the current chain's carried orientation.

- *Advantages:* uses existing structure (B5); reinforces orientation consistency, aligning with the stratified invariant.
- *Compatibility with B1–B7:* compatible within a stratum, where orientation is defined and comparable.
- *Compatibility with the stratified verdict:* **partial risk.** Phase E derived orientation conservation in part from Σ-orientation-neutrality (orientation bears no score, so reversal is never selected *for*). Making orientation a selection criterion entangles the tie-break with the very invariant it must preserve. The entanglement happens to *reinforce* consistency rather than break it — but it makes the rule non-orthogonal to I1, which is undesirable for a clean closure.
- *Always defined?* **No.** Two tied candidates may carry the *same* orientation, leaving orientation-ordering unable to separate them. Orientation does not guarantee a total order on the tied set.

**Mechanism 2 — Channel-bandwidth-ordering.** Break ties by channel bandwidth (B2): prefer the candidate reached along the higher-bandwidth channel.

- *Advantages:* bandwidth is a scalar local quantity attached to every channel by B2; defined for *every* candidate (each candidate is reached along some channel with some bandwidth); graph-local; reads only local edge weights.
- *Compatibility with B1–B7:* fully compatible. Bandwidth is native to B2; reading it adds nothing.
- *Compatibility with the stratified verdict:* **clean — orthogonal.** Bandwidth is independent of the orientation channel (Phase E §3 places them in distinct structural roles), so a bandwidth tie-break **cannot disturb** the orientation invariant's derivation. This orthogonality is the decisive advantage.
- *Always defined?* **Almost.** Bandwidth separates all candidates except those reached along equal-bandwidth channels — a measure-zero residual that requires one further key for guaranteed totality (§5).

**Assessment.** Bandwidth-ordering dominates on the two requirements that matter most: it is **orthogonal to the orientation invariant** (orientation-ordering is not) and it is **defined for every candidate** (orientation-ordering is not). Its only shortfall — non-totality under exactly-equal bandwidth — is closeable with a canonical final key drawn from existing structure, without invoking orientation at all.

---

## 4. Selection of the Canonical Tie-Break

Selecting the mechanism that is always defined within a reach stratum, requires no cross-stratum comparison, preserves the stratified-orientation invariant, and adds no axiom:

**Channel-bandwidth-ordering is chosen as the primary tie-break**, with a canonical local key as the totality guarantee. Orientation-ordering is *deliberately not used*, precisely to keep the tie-break **orthogonal to the stratified-orientation invariant** — a feature, not an omission.

**The rule, stated explicitly:**

> *When two or more candidates tie on Σ, select the candidate whose local key — channel bandwidth, then canonical local participation index — is lexicographically maximal.*

The final key (canonical local participation index) is derived from the distinctness of micro-events guaranteed by B1 (atomic, distinct events): the tied candidates are finitely many and distinguishable by their existing relational data, so a canonical local ordering exists without new structure.

---

## 5. Formal Specification of the Rule

**Ordering relation.** For each candidate next-state e′ in the local candidate neighborhood 𝒩, define the local key

> **κ(e′) = ( bw(e′), σ(e′) )**

where **bw(e′)** is the bandwidth (B2 edge weight) of the channel along which e′ is reached, and **σ(e′)** is a canonical local index induced from the distinct relational data of e′ (well-defined by B1 atomicity — distinct micro-events carry distinct local identities). Order keys **lexicographically, descending**: compare bw first; on equal bw, compare σ.

**Selection.** Among the Σ-maximal set 𝒮 = { e′ ∈ 𝒩 : Σ(e′) = max } (computed first, by the unchanged rule), commit the unique e′ ∈ 𝒮 with lexicographically maximal κ(e′).

**Local computation.** Both keys are read from the bounded candidate neighborhood: bw from the local channel weights (B2), σ from the local event identities (B1). No quantity outside 𝒩 is consulted. Σ itself is unchanged; the tie-break is a strictly downstream filter on 𝒮.

**Behavior at decoupling surfaces.** 𝒩 is bounded by finite reach (B6); no candidate lies across a decoupling surface (F2/N3), so no key is ever read across one. The tie-break is computed entirely within the chain's reach stratum and requires **no cross-stratum comparison** — consistent with the stratified-orientation result, which it does not touch.

**Totality.** 𝒩 is finite (bounded neighborhood, finite reach) and its members are distinct (B1). The lexicographic order on (bw, σ) is therefore a **total order on 𝒮**, so a unique lexicographic maximum exists for every tied set. The rule is **guaranteed total within each reach stratum.**

---

## 6. Determinism Upgrade

Re-evaluating **Determinism Component 4 — unique local maximizer** (Phase F §5):

- The evolution rule first computes the Σ-maximal set 𝒮 (unchanged).
- The tie-break rule (§5) selects the unique lexicographic-maximal element of 𝒮 via a total order.
- Therefore every update commits **exactly one** candidate. Uniqueness holds for all updates, not merely generically.

**Component 4: now PASS.** Components 1–3 (forward determinism, stable dependence, reach-bounded determination) were already PASS in Phase F. With Component 4 closed, **Determinism satisfies all four components.**

**The ED substrate's Determinism criterion is upgraded from CONDITIONAL to PASS.**

The upgrade introduces no new axiom (keys use only B1 + B2 structure), alters no component of Σ, contradicts no invariant (the rule is orthogonal to I1 and silent on I2–I5), and respects finite reach and irreversibility. All §2 requirements are met.

---

## 7. AD Score Update

With Determinism upgraded:

> **AD Score: 6 PASS / 0 CONDITIONAL / 0 FAIL.**

This closes the only architectural gap identified in Phase F. All six substrate-level AD criteria (minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality) now PASS for the ED substrate.

*Note on interpretation.* The score change reflects a *specification completion*, not a re-judgment: Phase F correctly returned CONDITIONAL on the architecture *as then specified* (with the slot open). This document fills the slot using only existing structure; the upgrade is the honest consequence of completing the specification, not a relaxation of the criterion. The "teeth" demonstrated in Phase F stand — the criterion did flag a real gap; the gap is now closed by the minimal addition required.

---

## 8. Next Actions

To propagate this closure through the corpus:

- **Update `Phase_F_CriteriaEvaluation.md`** — record Determinism as PASS (with a reference to this document), and update the six-criteria table and AD score to 6/6. Recommended form: leave the original CONDITIONAL analysis intact (it is correct for the as-then-specified architecture) and append an upgrade note pointing here, preserving the evaluation history.
- **Update `atlas/entries/ED_Substrate_AD_Entry.md`** — change the header verdict and §6 score to 6 PASS / 0 CONDITIONAL / 0 FAIL; move the tie-break item from §11 Open Items (architectural) to resolved; note the canonical rule.

**No other architectural changes are required.** The tie-break is the only open architectural slot; with it filled, the substrate specification is complete. The two remaining open items from Phase G — orientation primitivity (architectural) and the determinability-boundary measurement in bits (empirical) — are unaffected by this closure and remain as separately scoped work.

---

*End of TieBreak specification. This document fills the open tie-break slot using only B1/B2 structure, upgrades Determinism from CONDITIONAL to PASS, and brings the ED substrate to a 6/6 AD score. Propagation to Phase F and the atlas entry is recommended; no other architectural change is required.*
