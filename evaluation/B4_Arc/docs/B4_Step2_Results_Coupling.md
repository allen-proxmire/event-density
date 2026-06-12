# B4 Step 2 — Coupling Test: Can the Winding Act on the Dynamics?

**Arc:** B4 — topological-charge hypothesis. **This doc:** the load-bearing fork — can the integer winding (Step 1's latent invariant) *couple* to the ED dynamics without Σ reading orientation? If yes, ED can host an *active* topological charge; if not, the ontology forbids one as-built.
**Code:** `B4_Arc/coupling_test.py` (numpy; N=6 cycle, 400k draws). **Date:** June 2026.
**Discipline:** no hand-installed quantization or sign conventions; coupling functions are the corpus's own polar-measure overlap, not retrofits. Σ held orientation-blind throughout.

---

## The only structurally-available channels

Σ reads **ρ + graph only** (hard invariant, `sigma.py`). From `update.py`, the only phase-reachable dynamical quantities are:

- **bandwidth b_e (P04)** — enters the **tie-break** (`apply_tiebreak`) and, at b→0, **effective decoupling** (`admissible_neighbors`). *Never* enters `compute_sigma`.
- **transport amplitude (P05)** — the connection itself.

The ED-sanctioned phase↔amplitude pairing is the corpus polar participation measure **P_K = √b_K · e^{iπ_K}**, so the natural P04 coupling is an edge **coherence bandwidth** b_e = |⟨P_u,P_v⟩|² = **cos²(Δφ_e/2)** — maximal at aligned phase, zero at anti-aligned. Standard amplitude overlap; nothing installed.

## The mechanism — a topological bound becomes a w-indexed ladder

A winding-w single-valued field on an N-cycle obeys **Σ|wrap(Δφ_e)| ≥ |Σ wrap(Δφ_e)| = 2π|w|**. So |w| forces a *minimum total phase variation*, which **caps the achievable coherent bandwidth**. The minimum-variation (ground-state) config per sector is uniform, Δφ = 2πw/N, giving the discrete ladder b_e = cos²(πw/N):

| w | ground-state b_e = cos²(πw/N) | total \|Δφ\|/2π | bound 2π\|w\|/2π |
|---|---|---|---|
| 0 | **1.0000** | 0.0000 | 0.0000 |
| 1 | **0.7500** | 1.0000 | 1.0000 |
| 2 | **0.2500** | 2.0000 | 2.0000 |
| 3 | **0.0000** | 3.0000 | 3.0000 |

Random configs binned by sector confirm the monotone trend (mean b_e: w=0 → 0.527, |w|=1 → 0.475, |w|=2 → 0.285). **The integer winding indexes a discrete ladder of achievable coherent bandwidth** — a genuinely w-dependent dynamical quantity, and Σ never reads orientation.

## Candidate taxonomy (the deliverable)

| Candidate | Channel | Outcome | Note |
|---|---|---|---|
| baseline (no coupling) | — | **INERT** | Step 1 |
| **A. phase→bandwidth (P04 coherence)** | tie-break (weak) / b→0 decoupling (strong) | **DISCRETE (w-indexed ladder), Σ-blind** | the live channel |
| B. holonomy→transport (P05, AB-like) | connection amplitude | **WEAK / CONTINUOUS** | couples to the *continuous* holonomy (~49,769 distinct/50k) — sees the wrong invariant |
| C. phase→ρ | ρ (which Σ reads) | **FORBIDDEN** | back-door orientation read — violates the hard invariant |

Winding is **conserved under coupling A** (the coupling touches bandwidth, not the committed phases — those stay frozen by P11).

## The honest reading — coupling exists, but it is weak/conditional

**Coupling is not forbidden.** Candidate A produces a real, integer-indexed effect (the cos²(πw/N) ladder) while keeping Σ blind. So ED does **not** categorically forbid an active topological invariant — the fork resolves to *yes, weakly*. But three honest qualifications bound it hard:

1. **The channel is feeble generically.** Bandwidth enters only the **tie-break**, which acts only on exact Σ-ties — non-generic in continuous-ρ dynamics (though common in the symmetric/degenerate substrates where clean winding actually lives). So the winding's influence is order-1 only in symmetric configurations; otherwise it is a tie-breaker's whisper.
2. **The strong version needs an added ingredient.** A genuinely strong effect requires b→0 to **induce decoupling** (P04→B6), changing the admissible graph (and its b₁ — cf. recon). That threshold is ED-*plausible* (zero bandwidth = no channel) but it is a **modeling choice, not forced** by the primitives. Flag it as such.
3. **The natural strong coupling sees the wrong invariant.** Holonomy→transport (the AB-like channel that *would* be strong) couples to the **continuous** holonomy, not the integer winding. The integer only enters through the weak amplitude/tie-break route.

## Interpretation — does ED admit an *active* topological charge?

ED admits a topological invariant with **all four** charge-hallmarks reachable — quantized (ℤ), conserved, irreversibility-protected (Step 1), and now **coupled** (Step 2, via the P04 coherence ladder with Σ blind) — so an *active* topological charge is structurally **possible**, not forbidden. But its activation is **weak and indirect**: the winding indexes a discrete ladder of coherent-bandwidth *cost*, feeding the dynamics only through the amplitude/tie-break (or an optional bandwidth→decoupling) channel — never through Σ. What it conspicuously does **not** do is the defining act of electric charge: **source a long-range (Coulombic) field via Gauss's law**. That requires a surrounding surface — 2-D for 3-D space — which a 1-D cycle (b₁=1) structurally cannot provide; it needs the full spatial substrate (P06), not the minimal model. So the minimal substrate establishes the charge-like *skeleton* (discreteness + protection + weak coupling) but is the wrong dimensionality to establish *sourcing*.

## Classification & recommendation

**Outcome:** Candidate A → **DISCRETE (integer-dependent), Σ-blind** — coupling exists. B → weak/continuous. C → forbidden.

**Recommendation: REFRAME, then PARK at a clean result.** B4 has, across three honest steps, cashed out the Facts-paper's boldest claim **partially and defensibly**:

> *ED's U(1) polarity (P09) + irreversible commitment (P11) yield a quantized, conserved, irreversibility-protected topological invariant (a winding number) that can couple to the dynamics through bandwidth (P04) with Σ left orientation-blind — a charge-like structure — without supplying Coulombic sourcing or the Standard-Model charge spectrum.*

That is a real ontology result and the right register for Book 2 (charge-as-topology has the correct discreteness/protection/weak-coupling skeleton in ED). The **full** claim — "this *is* electric charge," with 1/r sourcing and Gauss's law — is **not** supported by the minimal model and requires a separate, much larger lift on the **spatial substrate (P06) + a Gauss/sourcing mechanism**, with real risk it does not cash out (a 1-D cycle cannot source a flux). Pursue that only as a deliberate, scoped project — not as a casual next step.

---

## Where B4 stands (arc summary)

| Step | Question | Verdict |
|---|---|---|
| Recon | What invariants does the graph admit? | U(1) holonomy (continuous); ρ ruled out; b₁ is the arena; Z₂ sign too coarse |
| Step 1 | Does commitment quantize it? | Operative invariant becomes the integer **winding** — quantized (ℤ), conserved, irreversibility-protected; **inert** |
| Step 2 | Can the winding act on the dynamics? | **Yes, weakly** — w-indexed coherence-bandwidth ladder via P04, Σ blind; not Coulombic sourcing |
| Step 3 (future) | Does it source a field (Gauss's law)? | **Not in the minimal model** — needs the spatial substrate P06; big lift, uncertain |

**Net:** charge-as-topology is *viable as a charge-like structure* in ED and *unproven as electric charge*. Honest, crank-safe, and reached graph-first throughout.
