# Born / Gleason Arc — Examination Outline

**Date opened:** 2026-04-26
**Location:** `arcs/born_gleason/`
**Goal:** Determine whether ED's primitive structure FORCES the non-contextuality assumption that Gleason's theorem requires. If yes, promote Born rule to a fully theorem-grade result (candidate Theorem #10) by chaining ED-primitives → Gleason non-contextuality → Born rule.
**Predecessor work:** `arcs/arc-foundations/born_rule_from_participation.md` (Step 3 of QM-emergence program). Step 3 derived Born conditional on environmental phase-independence; this arc replaces that conditional with a Gleason-style structural argument grounded in primitives.

---

## 1. The question, sharply

**Gleason's theorem (1957):** any probability measure μ on the closed subspaces of a Hilbert space ℋ of dimension d ≥ 3 that satisfies non-contextuality (μ(P) depends only on P, not on which orthogonal resolution P appears in) is necessarily of the form μ(P) = Tr(ρP) for some density operator ρ. The Born rule is the special case ρ = |ψ⟩⟨ψ|.

**The load-bearing assumption:** non-contextuality. Drop it and Gleason fails (Kochen-Specker exhibits non-contextual hidden-variable obstructions but Gleason itself just needs the assumption to derive Born).

**ED's question:** does the primitive-level structure of channels (Primitive 07), bandwidth (Primitive 04), and commitment (Primitive 11) force μ(P) to be non-contextual — i.e., independent of the surrounding resolution — by construction?

**If yes:** Born is FORCED at theorem grade. The "phase-independence" CANDIDATE in Step 3 is replaced by a Gleason-grade structural derivation.
**If no:** the failure mode itself is informative — it identifies which primitive would need strengthening to close the gap.

---

## 2. Why ED plausibly forces non-contextuality (the working intuition)

Channels (Primitive 07) are **primitive ontological objects**, not basis-dependent labels. A channel K exists as a structural feature of the chain, independent of which other channels happen to be in the resolution against which K is being measured.

Bandwidth `b_K = |P_K|²` (Primitive 04) is **assigned to K itself**, not to an ordered tuple (K, K', K'', ...). The bandwidth in K does not change if the surrounding channels in the resolution change.

Commitment events (Primitive 11) **select one channel from those available**, weighted by bandwidth. The selection is a property of the chosen channel's bandwidth fraction, not of the partition structure of the alternatives.

If these three primitive-level features hold, then the probability of outcome K* is structurally a function of K* alone (via b_K*) and the total bandwidth at the commitment locus — never of which other channels happen to be present in the resolution. **That is exactly Gleason's non-contextuality assumption, derived from primitives.**

This is the working intuition. The arc's job is to make it rigorous or find the loophole.

---

## 3. Examination plan — six memos

### Memo 1: `01_gleason_assumptions_inventory.md`
Lay out Gleason's theorem precisely. Enumerate every assumption: (a) Hilbert space of dimension d ≥ 3, (b) non-contextuality, (c) σ-additivity, (d) μ(0) = 0 and μ(I) = 1, (e) μ(P) ∈ [0,1]. For each assumption, identify which ED primitive(s) would need to underwrite it. Status: pure literature work, no ED derivation yet.

### Memo 2: `02_channel_noncontextuality_argument.md`
The core derivation memo. Argue rigorously that Primitive 07 (channel as primitive) + Primitive 04 (bandwidth as channel-local quantity) + Primitive 11 (commitment selects on channel-local bandwidth) jointly force non-contextuality. Identify any hidden assumptions. Flag any gap where a primitive *almost* gives non-contextuality but doesn't quite — those gaps are the falsification points.

### Memo 3: `03_dimension_and_sigma_additivity.md`
Check the other Gleason assumptions against ED. (a) Does ED's channel structure give Hilbert spaces of dimension ≥ 3 for any non-trivial chain? (Probably yes via multi-channel coherent sums; verify.) (b) Does the bandwidth-fraction probability rule satisfy σ-additivity? (Probably yes via additivity of bandwidth across orthogonal channel partitions; verify.)

### Memo 4: `04_d2_edge_case.md`
Gleason fails for d = 2 (qubits). For two-channel systems, the Born rule is not forced by Gleason and requires a separate argument (e.g., Busch's POVM extension, or Hardy's continuity-from-d≥3-via-tensor-product). Determine which extension ED's structure naturally supports. Note: most ED applications have many channels, so d ≥ 3 is the generic case; d = 2 is edge.

### Memo 5: `05_synthesis_theorem_10_candidate.md`
If Memos 2–4 close: assemble the chain Primitives 04+07+11 → Gleason non-contextuality → Gleason theorem → Born rule. State this as candidate Theorem #10. Cross-reference Step 3 (`born_rule_from_participation.md`) to show what was previously CANDIDATE is now FORCED. If Memos 2–4 don't close: state the residual gap precisely as a sub-CANDIDATE for future work.

### Memo 6: `06_arc_closure.md`
Three-line verdict. Update QM-emergence synthesis (`papers/QM_Emergence_Structural_Completion/`) with the new theorem (or with the sharpened gap). Update memory record `project_qm_emergence_arc.md` with the result. Cross-reference into the running theorem inventory.

---

## 4. First-session scope

Memos 1 and 2. That is the load-bearing pair: the Gleason assumptions inventory establishes what we need to derive, and the channel-non-contextuality argument is the actual derivation. If Memo 2 fails to close, Memos 3–6 are moot until the gap is repaired. If Memo 2 closes, Memos 3–6 are largely consolidation.

**Predicted outcome (to be tested, not assumed):** Memo 2 closes cleanly because ED's channel ontology is genuinely primitive — non-contextuality is more natural in ED than in standard QM, where it has to be postulated separately. The risk is in subtle definitional drift between "channel as primitive" and "Hilbert-space projector," which Memo 1 should pin down.

---

## 5. Falsification conditions for the arc

The arc is **closed positive** if Memos 1–5 produce a chain Primitives → Gleason non-contextuality → Born with no residual CANDIDATEs along the way (other than upstream U1, the participation-measure definition itself).

The arc is **closed negative** if Memo 2 fails — i.e., if ED's primitive structure does not force non-contextuality and a contextual probability assignment is consistent with the primitives. In that case the arc produces a precise statement of which primitive would need amendment to reach non-contextuality, and the Step 3 CANDIDATE remains.

The arc is **inconclusive** if Memo 2's argument is plausible but not rigorous — non-contextuality is *suggested* by primitives but a watertight derivation remains out of reach. In that case the arc produces a sub-CANDIDATE for future structural work.

---

## 6. Cross-references

- Step 3 derivation (predecessor): `arcs/arc-foundations/born_rule_from_participation.md`
- QM-emergence synthesis: `papers/QM_Emergence_Structural_Completion/QM_Emergence_Structural_Completion.md`
- Gleason 1957: A. M. Gleason, "Measures on the closed subspaces of a Hilbert space," J. Math. Mech. 6, 885.
- Busch 2003 (POVM extension covering d=2): P. Busch, "Quantum states and generalized observables: a simple proof of Gleason's theorem," Phys. Rev. Lett. 91, 120403.
- Primitive 04 (bandwidth): `quantum/primitives/04_participation_bandwidth.md`
- Primitive 07 (channel): `quantum/primitives/07_channel.md`
- Primitive 11 (commitment): `quantum/primitives/11_commitment.md`

---

## 7. One-line arc summary

> **Test whether ED's primitive structure (channels + bandwidth + commitment) forces the non-contextuality assumption Gleason needs. If yes, the Born rule promotes from CANDIDATE-with-phase-independence (Step 3) to fully FORCED Theorem #10 via the chain Primitives → Gleason non-contextuality → Born.**
