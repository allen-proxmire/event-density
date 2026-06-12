# B4 Step 1 — U(1) Holonomy / Commitment-Quantization: Results

**Arc:** B4 — topological-charge hypothesis. **This doc:** the first real step after recon — build the minimal U(1)-on-a-cycle substrate and test whether commitment (P11) quantizes the holonomy.
**Code:** `B4_Arc/holonomy_test.py` (numpy only; N=6 cycle, b₁=1, 200k draws). **Date:** June 2026.
**Discipline:** quantization was NOT hand-installed. No snapping to Zₙ. We set up two distinct loop invariants and let P09 (U(1)-valued) + P11 (single-valued irreversible fact) decide which one the committed substrate carries.

---

## Setup

Smallest ED-consistent substrate with a nontrivial loop: one cycle (b₁=1), a genuine P05 phase θ_e per directed edge, no decoupling (B6 off). Two candidate loop invariants:

- **(A) Connection holonomy** `H = (Σ θ_e) mod 2π ∈ U(1)` — the bare P05 connection, *before* commitment.
- **(B) Committed-field winding** `w = (1/2π) Σ wrap(φ_{v+1}−φ_v) ∈ ℤ` — what P11 produces: each node locked to **one single-valued** phase `φ_v ∈ S¹` (P09: polarity is U(1)-valued; P11: a definite irreversible fact). Integrality is forced by π₁(U(1))=ℤ — *we never round; we read it off.*

## Results (`holonomy_test.py`, verbatim)

| Test | Result | Reading |
|---|---|---|
| (A) connection holonomy H | 196,920 distinct values / 200k; KS dev 0.0023 | **CONTINUOUS** — the bare connection does **not** quantize |
| (B) committed-field winding w | max\|w−round(w)\| = **4.4e-16**; dist 0:0.55, ±1:0.22, ±2:0.008 | **EXACTLY INTEGER** — quantized to ℤ |
| (3a) uncommitted drift | **4438** winding-slips / 20k steps | free phases → winding not protected |
| (3b) committed (P11) | **0** slips / 20k steps | irreversibility freezes the facts → winding conserved |
| (4) coupling | Σ orientation-blind (hard invariant) | winding **dynamically inert** |

## What is genuinely shown vs. what is structural

**Genuinely shown (empirical):**
1. The bare U(1) connection holonomy is **continuous** (uniform on the circle to KS 0.002). The recon's continuous-holonomy claim is confirmed numerically.
2. The committed substrate carries a **different** invariant — the winding of the single-valued committed phase field — and it is integer to machine precision. The continuous holonomy is **not rounded**; rather, single-valued commitment makes the *integer winding* the operative loop invariant.
3. The winding is **conserved**, changing only via a phase-slip (a node-difference crossing ±π). With phases free, slips happen (4438/20k); under P11 the facts are frozen and slips are **impossible** — so the protection mechanism *is* commitment's irreversibility.

**Honest about what's near-tautological:** that a single-valued S¹ field on a loop has integer winding is a *mathematical* fact (π₁=ℤ), not a discovery. The non-trivial content is the **mapping onto ED primitives**: P09 (U(1)) + P11 (single-valued, irreversible) are *exactly* the conditions that (i) make winding the operative invariant and (ii) topologically protect it. ED instantiates the standard topological-protection structure — modest, correct, not oversold. Test (4) is asserted from the orientation-blindness invariant in `sigma.py`, not independently re-derived; (3b) confirms the *logic* (frozen ⟹ no slip), it is not an emergent surprise.

## The decisive finding — three hallmarks present, the fourth blocked

A topological charge needs four structural hallmarks. This test shows ED-as-built supplies **three**:

| Hallmark | Status | Source |
|---|---|---|
| **Quantized** (discrete spectrum) | ✅ winding ∈ ℤ | π₁(U(1))=ℤ, activated by single-valued P11/P09 |
| **Conserved** (invariant under evolution) | ✅ | telescoping loop sum |
| **Protected** (can't change continuously) | ✅ | P11 irreversibility blocks the phase-slip |
| **Coupled** (sources / acts on dynamics) | ❌ **absent** | **Σ is orientation-blind (hard invariant)** |

So the recon's hinge ("does commitment quantize the holonomy?") gets a precise answer: **commitment doesn't round the continuous holonomy — single-valued irreversible commitment makes the operative invariant the integer winding, which is automatically quantized, conserved, and protected.** Three of four charge-hallmarks fall out *for free* from U(1)+irreversibility. The center of gravity of B4 therefore **moves**: the quantization question is essentially answered (yes); the real obstacle is **coupling**.

## Interpretation — for "charge as topology"

The committed ED substrate carries a quantized, conserved, irreversibility-protected integer winding around its cycles — the structural signature of a topological charge, with quantization and protection emerging *without retrofit* from the substrate's own U(1) polarity (P09) and irreversible commitment (P11). What it does **not** yet have is the defining *action* of a charge: the winding neither sources its connection nor affects the dynamics, because Σ is **orientation-blind** by a hard invariant the bits-program results depend on. ED thus possesses a *latent* topological charge — present, quantized, protected, but causally disconnected. The honest cap from recon holds: this gives quantization + protection, **not** a scale or the ±⅓ spectrum.

## The structural tension this exposes (the real B4 frontier)

Coupling cannot go through Σ without breaking **orientation-blindness** — a load-bearing invariant (the stratified-orientation result, the whole determinability measurement rest on it). So B4's next question is sharp and consequential:

> **Can the winding couple to the dynamics through a non-Σ channel — e.g. modulating bandwidth (P04) or the connection itself (P05) — leaving Σ orientation-blind?**

This is *not* obviously a dead end: the corpus's own polar participation measure **P_K = √b_K · e^{iπ_K}** already pairs amplitude (P04) with phase (P09). If phase couples to amplitude/transport while Σ stays blind, a dynamically-active charge is conceivable without touching the invariant. If it *cannot*, then ED cannot host an active charge without revising a load-bearing invariant — itself a major, honest structural result and a Book-2 fence-post.

## Classification & recommendation

**Outcome:** (b) **collapses to a discrete subgroup** — with the refinement that the discrete invariant is the **winding (ℤ)**, it is **irreversibility-protected**, and it is currently **dynamically inert**.

**Recommendation: PROCEED.** B4 is viable and just produced a real result: quantization + conservation + protection emerge non-circularly. The next step is **not** more quantization work — it is the **coupling test**: can the winding act through P04/P05 without Σ reading orientation? That single question now carries the whole hypothesis, and it sits right on a genuine tension with a load-bearing invariant — exactly where a load-bearing test of the ontology should sit.

---

## Next step (B4 Step 2)

Coupling test: introduce a phase→amplitude (P09→P04) or phase→transport (P09→P05) coupling on the cyclic substrate, hold Σ orientation-blind, and check whether the winding (a) measurably affects the ρ-dynamics / observable statistics and (b) is itself still conserved. Decision: active-charge channel exists (B4 strongly viable) vs. coupling forces an orientation-blindness violation (ED cannot host an active charge as-built — clean structural negative).
