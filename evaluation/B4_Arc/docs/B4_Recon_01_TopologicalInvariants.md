# B4 Recon 01 — Topological Invariants of the Participation Graph

**Arc:** B4 — Topological-charge hypothesis (is electric charge a discrete topological invariant on the participation graph? — the boldest falsifiable claim from the "Facts" paper, *When Contrast Becomes Fact*).
**This doc:** the scoped **reconnaissance** pass — NOT the derivation. Bounded structural probe answering the prior question: *what topological invariants does the participation graph support under the actual ED dynamics?*
**Date:** June 2026 · **Author:** Allen Proxmire
**Grounding:** `Bits/simulator/{graph,state,sigma,update}.py` (the certified Bits build) + primitives P02/P04/P05/P09/P11.
**Discipline:** reached graph-first, not charge-first — the standing crank-safety rule. No "charge" language outside the single interpretation paragraph.

---

## 1. The participation graph as a mathematical object

- **Undirected, reciprocal.** Edges stored as a *shared* dict in both directions (`_adj[u][v] is _adj[v][u]`). No intrinsic edge orientation.
- **Edge-weighted (P04 bandwidth).** Each edge carries `bw ∈ ℝ₊` (a magnitude) + a boolean `decoupled` flag (B6). Bandwidth is amplitude-like; carries no sign or phase.
- **Node state = (ρ, orientation).** `ρ` is a **monotone non-decreasing scalar** (B7 irreversibility — `commit()` is the sole ρ writer, deltas ≥ 0). `orientation` is a small vector: index 0 longitudinal (derivable), index 1.. transverse (primitive).
- **Dynamics.** A front picks the Σ-maximal admissible neighbor and commits there. **Σ is hard-invariantly orientation-blind** — reads only ρ and graph-local structure. Polarity is *transported by chain-continuity, never read by the dynamics*.

**The single most important implementation fact** (`update.py:64`):

```python
transverse = state[u].orientation[1:].copy()      # source's transverse...
state[winner].commit(..., transverse=transverse)  # ...copied verbatim to target
```

**Polarity transport in the certified build is the identity map.** P05's "connection" was instantiated as *copy-without-rotation*; the longitudinal slot is just the target id ("minimal: encode committed direction by target id"). So **P05/P09's angular (U(1)) content exists in the spec but is stubbed to trivial in the simulator** — necessarily, since the bits work required Σ orientation-blind and used orientation only as a passive passenger.

⇒ Every answer below splits into **spec-level** (what P05+P09 *declare*) vs **as-built** (what the certified sim *runs*).

## 2–3. Candidate invariants and their behavior under the dynamics

| Candidate invariant | Type | P05 transport | P04 bandwidth | P11 commitment | Additive? | As-built status |
|---|---|---|---|---|---|---|
| **ρ (commitment density)** | local scalar, monotone↑ | n/a (Σ-blind) | independent | *is* the commit | sums, but unsigned | **Ruled out** |
| **b₁ — cycle space / H₁ (Betti number E−V+C)** | integer (wiring) | preserved | preserved | preserved by pure commit; **broken by decoupling** (B6 cuts an edge → b₁ of admissible subgraph drops) | adds over disjoint union | exists, but it's the *arena* |
| **U(1) holonomy around cycles** (Wilson loop = the cited Aharonov–Bohm phase; in H¹(graph,U(1))≅U(1)^{b₁}) | **continuous** U(1) per independent cycle | **this IS the P05 invariant** (gauge-invariant under node rephasing) | independent (phase ⊥ amplitude; cf. P_K=√b·e^{iπ}) | **UNDEFINED** — spec doesn't fix commit's action on phase; trivially 0 as-built | flux adds / phase multiplies | exists at spec, **trivial (≡0) as-built** |
| **Z₂ tension sign** (aligned vs anti-aligned chains, `tension_polarity.md`) | discrete ±1 | preserved (alignment class) | sign-independent | plausibly frozen by commit | mod-2 | exists; only ± |

**Reading the table**
- **ρ is cleanly ruled out.** Unsigned, strictly increasing, purely local — no sign, no winding, no conservation. The naive "ρ = charge" idea is dead on arrival.
- **b₁ is real but it's the stage, not an actor.** A discrete integer, but it counts *independent loops in the wiring*, not *sources*; no sign, doesn't move with the dynamics — except that **forming a decoupling surface changes it** (the determinability boundary alters the graph's topology — a genuine hook). It can't itself *be* a charge.
- **The U(1) holonomy is the right kind of object — and the corpus already uses it** (the Aharonov–Bohm phase P09 cites *is* this holonomy). But it is **continuous** (a U(1) element per cycle) and in the certified build **identically trivial** (transport stubbed to identity). The slot where commitment acts on the phase is **undefined**.
- **The Z₂ sign is a genuine discrete invariant** but only ± — supplies a particle/antiparticle sign, not a quantized magnitude.

## 4. The decisive finding

Nothing in the as-built substrate is a discrete integer topological invariant. But the **U(1) holonomy on H¹ is a nontrivial invariant of the right family at the spec level** — continuous, and trivial-as-built only because P05 was instantiated as identity transport. So the live question is not *"is there a topological invariant?"* (yes: U(1) holonomy) but:

> **Does commitment (P11) quantize the continuous U(1) cycle-holonomy onto a discrete subgroup?**

This is the hinge, and it's structurally forced, not retrofitted: **P11 is the only primitive that injects discreteness** (irreversible lock-in), and quantization is fundamentally a discreteness phenomenon. If charge-as-topology cashes out in ED at all, it must route through commitment-induced quantization of the holonomy — which would, as a bonus, explain *why* the invariant is discrete (because commitment is). A real, falsifiable, crank-safe ontological claim.

## Interpretation — what this means for "charge as topology"

The participation graph **does** carry the natural gauge-topological object electric charge would need — a U(1) holonomy around its independent cycles (the same Aharonov–Bohm phase the corpus already invokes), in H¹(graph, U(1)) ≅ U(1)^{b₁}. But as it stands that object is a **continuous flux, not a discrete charge**, and the certified simulator zeroes it out by transporting polarity trivially. For "charge is a discrete topological invariant" to be true in ED, the continuous holonomy must be **quantized to a discrete subgroup, and the only candidate quantizer is commitment (P11)**. Honest ceiling: success would yield *charge quantization* (integer/rational multiples of a unit) as a topological consequence of discrete commitment — it would **not**, by itself, reproduce the Standard Model's specific ±⅓ spectrum (that needs structure ED doesn't obviously supply; chasing it is the crank trap). B4's defensible target is *quantization-from-commitment*, not the charge spectrum.

## Recommendation: PROCEED — WITH MODIFIED FRAMING

(Outcome class 3 from the arc brief: invariant exists but is continuous/trivial under the current instantiation → modified framing required.)

1. **The B4 claim becomes:** *Commitment quantizes the U(1) cycle-holonomy of the participation graph onto a discrete subgroup, yielding a conserved, additive, integer-valued invariant.* **Falsifier:** if commitment leaves the holonomy continuous (or destroys it), charge-as-discrete-topology fails in ED — a clean negative and a Book-2 fence-post.
2. **The certified Bits simulator is the wrong tool** — it stubs P05 to identity, and its chains are near-acyclic (b₁≈0 — no loops to carry holonomy). The real B4 Step 1 is a small **purpose-built substrate that implements P05 as a genuine non-trivial U(1) transport** (a phase per directed edge) **on a graph with cycles**, then checks whether commitment quantizes the loop holonomy.
3. **Cap the ambition at quantization, not the spectrum.** State the fence up front so the work can't drift into ±⅓-retrofitting.

**Net:** B4 is **viable**; the invariant is **real but continuous**; the whole hypothesis now rests on one crisp, structurally-motivated, falsifiable question — *does P11 quantize the holonomy?* It stayed crank-safe by reaching the U(1) object from the graph, not from the word "charge."

---

## Next step (real B4, not recon)

Build `B4_Arc/` Step-1 minimal substrate: a small cyclic participation graph with a non-trivial per-edge U(1) phase (P05 transport), evolve under the real Σ-rule + commitment (P11), and measure the loop holonomy before/after commitment. Decision: holonomy stays continuous (B4 fails — clean negative) vs. locks to a discrete subgroup (B4 viable — proceed to multi-step derivation). NOT yet started.
