# Update Plan — After M-2 (P04 core + P04 §1.5) Closes

**Date:** 2026-05-13
**Trigger:** M-2 paper accepted as closed (forcing argument for P04 bandwidth additivity + four-band partition complete).
**Scope:** Surgical §3.0 edits to Papers #1, #2, #3, #6, #11, #13, #14, #15, #16, #17. No proof edits. Genre discipline preserved.

---

## 1. Overview

Meta-Paper M-2 establishes that the substrate's bandwidth content is forced to (a) be a non-negative real-valued additive scalar (P04 core, Shannon-Khinchin axiom 4 + operational adequacy) and (b) decompose into exactly four mutually orthogonal bands organized as two conjugate pairs (P04 §1.5, Routes A + C + D). With M-2 closed, every downstream Forcing Paper whose Phase-1 §3.0 listed P04 (core or §1.5) as a load-bearing input must update its §3.0 to reflect that P04 is now forced upstream by M-2 rather than postulated.

This plan specifies the exact surgical edits for the 10 affected papers. Each edit is contained within a single bullet point in §3.0; no proofs, equations, derivations, or other §§3.1–3.3 / §§4–10 content is touched. The update converts "P04 is load-bearing input; why bandwidth has this character is upstream content" to "P04 is now forced upstream by M-2; treated here as derived structural result of M-2."

---

## 2. List of Affected Papers

Per Dependency Graph §2 + §5:

**Papers depending on P04 core (bandwidth additivity):** #1, #2, #3, #6, #13, #14, #16, #17 (8 papers).
**Papers depending on P04 §1.5 (four-band partition):** #3, #6, #11, #15, #17 (5 papers).
**Union of affected papers:** **#1, #2, #3, #6, #11, #13, #14, #15, #16, #17** (10 papers).

**Justification.** Each of these papers has a §3.0 Primitive Inputs entry (added during Phase-1) that explicitly names P04 core or P04 §1.5 (or both) as load-bearing input. The M-2 closure changes the upstream status of these primitives.

**NOT affected** (no P04 entry in §3.0): #4 (Schrödinger via Stone — invokes only P13), #5 (Gauge T17 — invokes P10), #7 (Dirac — invokes P06, POI, IND), #8 (DCGT — invokes HYD), #9 (Substrate gravity — invokes P12, HOL, DEC), #10 (BH/Hawking — invokes V1, V5, HYD), #12 (Momentum — invokes P03, P06).

**NOT touched per spec:** Papers #18, #19 (Wave-2 papers, outside scope).

---

## 3. Per-Paper §3.0 Replacement Blocks

### Paper #1 — Participation Measure

**Closed primitive:** P04 core (bandwidth as non-negative additive scalar).

**Update type:** Replacement of single bullet point.

**Old text (from Phase-1):**

> **P04 (bandwidth as non-negative additive scalar).** The substrate supplies a real-valued non-negative quantity $b_K \geq 0$ on each channel, additive under channel decomposition. *Why bandwidth and not some other non-additive carrier of "amount of participation"* is upstream content treated in the Primitive-Forcing Meta-Paper.

**New text (post-M-2):**

> **P04 (bandwidth as non-negative additive scalar) — now forced upstream by M-2 (2026).** The substrate supplies a real-valued non-negative quantity $b_K \geq 0$ on each channel, additive under channel decomposition. Forced by Meta-Paper M-2 under joint Routes B (operational adequacy: Born-rule $\sigma$-additivity requires it) and D (Shannon-Khinchin axiom 4: entropy additivity over independent events). Treated here as derived structural result, not as a primitive postulate.

**Notes on formatting.** Single-bullet replacement; preserve markdown indentation and surrounding bullets (P09 — already closed by M-1; P03+P07 — still load-bearing pending M-4 + M-6).

---

### Paper #2 — Born Rule

**Closed primitive:** P04 (bandwidth additivity).

**Update type:** Replacement of "Bandwidth additivity" bullet.

**Old text (from Phase-1):**

> **Bandwidth additivity (P04).** Needed for $\sigma$-additivity of the probability rule. Upstream content.

**New text (post-M-2):**

> **Bandwidth additivity (P04) — now forced upstream by M-2 (2026).** Needed for $\sigma$-additivity of the probability rule. Forced upstream by M-2 under Routes B + D (Shannon-Khinchin axiom 4 + Born-rule operational adequacy). The $\sigma$-additivity required for Gleason-Busch and for the operational route now inherits from M-2 rather than from a displaced postulate.

**Notes on formatting.** Single-bullet replacement; preserve the P11 bullet (which was partly updated by M-1 closure to note uniform-$U(1)$ inheritance from M-1; full P11 update belongs to M-3).

---

### Paper #3 — Inner Product + Tsirelson

**Closed primitives:** P04 core (bandwidth additivity) + P04 §1.5 (four-band orthogonality).

**Update type:** Replacement of two bullet points.

**Old text (from Phase-1):**

> **Four-band orthogonality (P04 §1.5).** The substrate's bandwidth decomposes into four mutually orthogonal bands (internal, adjacency, environmental, commitment-reserve). This orthogonality is a primitive-level structural commitment; it is the substrate-level source of inner-product orthogonality on the participation manifold. *Why four bands and not three or five, and why orthogonal at the primitive level, is upstream content.*
> - **Bandwidth additivity (P04).** Provides the $\ell^2$ summation structure that supports the sesquilinear pairing.

**New text (post-M-2):**

> **Four-band orthogonality (P04 §1.5) — now forced upstream by M-2 (2026).** The substrate's bandwidth decomposes into four mutually orthogonal bands (internal, adjacency, environmental, commitment-reserve). This orthogonality is forced by M-2 under joint Routes A (symmetry-minimality: $\mathbb{Z}_2 \times \mathbb{Z}_2$ "is/does" × "kinematic/dissipative" duality) + C (compositional closure) + D (information-theoretic minimum decomposition). The inner-product orthogonality structure on the participation manifold inherits from this upstream forcing.
> - **Bandwidth additivity (P04) — now forced upstream by M-2 (2026).** Provides the $\ell^2$ summation structure that supports the sesquilinear pairing. Forced under Routes B + D per M-2.

**Notes on formatting.** Both bullets replaced; preserve the "Papers #1–#2 results" bullet and the closing paragraph on Landau-Khalfin machinery.

---

### Paper #6 — Hamiltonian + Mass

**Closed primitive:** P04 §1.5 (four-band partition for bandwidth-signature mass).

**Update type:** Replacement of one bullet point.

**Old text (from Phase-1):**

> **Four-band partition (P04 §1.5).** Enters for the bandwidth-signature mass identification.

**New text (post-M-2):**

> **Four-band partition (P04 §1.5) — now forced upstream by M-2 (2026).** Enters for the bandwidth-signature mass identification. Forced by M-2 under joint Routes A + C + D. The Lorentz-scalar bandwidth-signature functional $\sigma_\tau$ that this paper identifies with mass operates on substrate-derived four-band content rather than postulated four-band content.

**Notes on formatting.** Single-bullet replacement; preserve "Papers #1–#4 results," "Galilean Lie algebra acting on the participation manifold," and "Locality of $\hat{H}$" bullets (Galilean closes in M-4; locality remains).

---

### Paper #11 — Heisenberg Uncertainty

**Closed primitive:** P04 §1.5 (four-band partition with adjacency-band Fourier-conjugate structure).

**Update type:** Replacement of one bullet point.

**Old text (from Phase-1):**

> **Four-band partition with adjacency-band Fourier-conjugate structure (P04 §1.5).** Load-bearing — the substrate-level conjugate-variable pair $(b_x, b_p)$ is the primitive carrier of the position-momentum content.

**New text (post-M-2):**

> **Four-band partition with adjacency-band Fourier-conjugate structure (P04 §1.5) — now forced upstream by M-2 (2026).** The substrate-level conjugate-variable pair $(b_x, b_p)$ is the primitive carrier of the position-momentum content. The four-band structure itself (and the adjacency-band identification as the kinematic carrier) is now forced by M-2 under Routes A + C + D. The Fourier-conjugate sub-partition $(b_x, b_p)$ within the adjacency band is a downstream operational distinction not directly forced by M-2 — it follows from the adjacency band's interaction with spatial-translation symmetry (P03, scoped for M-4). The substrate-level locus of the conjugate-variable pair is now M-2-derived rather than postulated.

**Notes on formatting.** Single-bullet replacement; preserve "Papers #1–#4 results" and "Standard $L^2$ Weyl-Fourier inequality" bullets, plus the closing "Honest reading" paragraph.

---

### Paper #13 — Schrödinger Thin-Participation Limit

**Closed primitive:** P04 core (bandwidth additivity, implicit in per-channel evolution + bandwidth conservation).

**Update type:** Replacement note (P04 is invoked indirectly through Papers #1–#4 results and through bandwidth conservation in the per-channel rule).

**Old text (from Phase-1):**

> **Per-channel evolution rule.** Substrate-level dynamical equation; treated as a primitive-derived structural commitment.

**New text (post-M-2):**

> **Per-channel evolution rule.** Substrate-level dynamical equation; treated as a primitive-derived structural commitment. **Note (post-M-2 2026):** the bandwidth-conservation property used in this rule's derivation inherits from M-2's P04 core forcing (Shannon-Khinchin axiom 4); the per-channel rule itself remains downstream structural content of substrate dynamics under bandwidth conservation.

**Notes on formatting.** Append explicit note to the existing per-channel bullet. Other bullets (Papers #1–#4, thin-participation regime) unchanged.

---

### Paper #14 — Born Rule via Bandwidth Ratio

**Closed primitive:** P04 (bandwidth additivity).

**Update type:** Replacement of one bullet point.

**Old text (from Phase-1):**

> **Bandwidth additivity (P04).** Needed for $\sigma$-additivity.

**New text (post-M-2):**

> **Bandwidth additivity (P04) — now forced upstream by M-2 (2026).** Needed for $\sigma$-additivity. Forced upstream by M-2 under Routes B + D. The operational route's $\sigma$-additivity (used to extend the bandwidth-fraction rule across disjoint channel subsets) now inherits from M-2 rather than from a substrate postulate.

**Notes on formatting.** Single-bullet replacement; preserve "Paper #1 result" and "Commitment with uniform-$U(1)$-phase-randomization (P11)" bullets. P11 remains pending M-3 closure (treated separately in UPDATE_PLAN_after_M3.md).

---

### Paper #15 — Adjacency Kinetic Structure

**Closed primitive:** P04 §1.5 (adjacency-band Fourier-conjugate structure).

**Update type:** Replacement of one bullet point.

**Old text (from Phase-1):**

> **Adjacency-band Fourier-conjugate structure (P04 §1.5 + Paper #11).** Load-bearing — supplies the conjugate-variable pair.

**New text (post-M-2):**

> **Adjacency-band Fourier-conjugate structure (P04 §1.5 + Paper #11) — now forced upstream by M-2 (2026).** The four-band partition itself, including the adjacency band as kinematic carrier, is forced upstream by M-2 under Routes A + C + D. The Fourier-conjugate sub-partition $(b_x, b_p)$ within the adjacency band remains downstream operational content of Paper #11. The substrate-level kinematic-content locus is now M-2-derived rather than postulated.

**Notes on formatting.** Single-bullet replacement; preserve "Papers #1–#6 results" and "Galilean covariance + rotational isotropy" bullets (Galilean closes in M-4).

---

### Paper #16 — Phase-Independence of Bandwidth

**Closed primitive:** P04 (bandwidth as real-valued non-negative primitive).

**Update type:** Replacement of one bullet point.

**Old text (from Phase-1):**

> **P04 (bandwidth as real-valued non-negative primitive).** Load-bearing — phase-independence follows because bandwidth is *not* the angular primitive.

**New text (post-M-2):**

> **P04 (bandwidth as real-valued non-negative primitive) — now forced upstream by M-2 (2026).** Phase-independence follows because bandwidth is *not* the angular primitive. The bandwidth primitive is forced upstream by M-2 under Routes B (operational adequacy) + D (Shannon-Khinchin axiom 4). The structural distinction between bandwidth (P04, M-2-forced) and polarity (P09, M-1-forced) is now both upstream content — the present paper's "phase-independence is forced" result becomes fully derived under M-1 + M-2 closures.

**Notes on formatting.** Single-bullet replacement; preserve "Papers #1–#2 results" and "P09" bullets, plus the "Honest reading" paragraph (which can optionally be augmented to note that both bandwidth and polarity are now M-series-forced).

---

### Paper #17 — Four Postulates Unified

**Closed primitives:** P04 core + P04 §1.5 (parts of the full primitive set).

**Update type:** Replacement of two bullet points (P04 core + P04 §1.5 in the primitive list and the standalone four-band partition bullet).

**Old text (from Phase-1):**

> **The full substrate primitive set $\{P03, P04, P06, P07, P09, P11, P13\}$.** Each is doing load-bearing work in at least one of the four postulates.
> - **Four-band partition (P04 §1.5).** Load-bearing for inner-product orthogonality, kinetic structure, and adjacency-band uncertainty content.
> - **Participation-measure structure ($|P_K|^2 = b_K$ from Paper #1).** Load-bearing for the quadratic form of the Born rule, the global $U(1)$ gauge redundancy, and the Heisenberg $\hbar/2$ bound.

**New text (post-M-2):**

> **The full substrate primitive set $\{P03, P04, P06, P07, P09, P11, P13\}$.** Each is doing load-bearing work in at least one of the four postulates. **As of 2026 with M-1 + M-2 closures, P09 ($U(1)$ polarity) is forced upstream by M-1, and P04 (bandwidth additivity + four-band partition) is forced upstream by M-2.** Remaining primitives (P03, P06, P07, P11, P13) pending M-3 through M-12.
> - **Four-band partition (P04 §1.5) — now forced upstream by M-2 (2026).** Load-bearing for inner-product orthogonality, kinetic structure, and adjacency-band uncertainty content. Forced under joint Routes A + C + D per M-2.
> - **Participation-measure structure ($|P_K|^2 = b_K$ from Paper #1).** Load-bearing for the quadratic form of the Born rule, the global $U(1)$ gauge redundancy, and the Heisenberg $\hbar/2$ bound. (Paper #1 itself now operates on M-1 + M-2 forced primitives per the Phase-1 + M-1 + M-2 update cascade.)

**Updated §3.3 Honest Reading paragraph:**

> ED's substantive synthesis claim is that the four QM postulates, normally presented as logically independent, are *facets of one substrate object* — once the substrate primitives are in place. **As of 2026 with M-1 + M-2 closures, two of the load-bearing primitives (P09 and P04) are upstream-forced; the displaced-postulate critique no longer applies to them.** The synthesis is increasingly transparent. Remaining primitives are pending M-3 through M-12. ED is best characterized as a **substrate ontology + reconstruction program**.

**Notes on formatting.** Two bullets replaced + opening sentence augmented to track cumulative M-series closures. The third bullet (participation-measure structure) is parenthetically updated to note Paper #1's cascade-updated status.

---

## 4. Circularity Audit

**Rule (per DEPENDENCY_GRAPH_ED.md §6).** Each Forcing Paper §3.0 may cite M-2's forcing result for P04. M-2's machinery is NOT used in Forcing Paper §§4–10 derivations. The citation in §3.0 is purely a status-pointer; the proof is unchanged.

**Check.** M-2's forcing argument uses only $\{C^*\}$ + M-1 + standard background mathematics (Shannon-Khinchin, $\mathbb{Z}_2 \times \mathbb{Z}_2$ symmetry, compositional closure). It does NOT invoke any Paper #1–#17 result. Therefore citing M-2 in any Paper #N's §3.0 (for $N \in \{1, 2, 3, 6, 11, 13, 14, 15, 16, 17\}$) introduces no circularity: M-2 is a strictly upstream paper.

**Cumulative check after M-1 + M-2 + M-3 + M-4:** Each M-k paper invokes only M-1 through M-(k-1) plus background math + $\{C^*\}$. The DAG is consistent.

---

## 5. Cumulative-Update Table

After this M-2 update plan is applied (combined with M-1 closure from UPDATE_PLAN_after_M1.md):

| Paper | P09 (M-1) | P04 core (M-2) | P04 §1.5 (M-2) | Net §3.0 status |
|---|---|---|---|---|
| #1 | ✅ forced | ✅ forced | (not invoked) | P09 + P04 closed; P03+P07 pending |
| #2 | ✅ forced (via P11 partial) | ✅ forced | (not invoked) | P04 closed; P11 partial; P09 closed |
| #3 | ✅ forced | ✅ forced | ✅ forced | All P04 + P09 closed |
| #6 | (not invoked directly) | (not invoked) | ✅ forced | P04 §1.5 closed; GAL pending |
| #11 | (not invoked) | (not invoked) | ✅ forced | P04 §1.5 closed |
| #13 | (not invoked) | ✅ forced (indirect) | (not invoked) | P04 core (indirect) noted; thin-regime + per-channel rule pending |
| #14 | ✅ forced (via P11 partial) | ✅ forced | (not invoked) | P04 closed; P11 partial; P09 closed |
| #15 | (not invoked) | (not invoked) | ✅ forced | P04 §1.5 closed; GAL pending |
| #16 | ✅ forced | ✅ forced | (not invoked) | P09 + P04 closed (this paper now fully derived from M-series + Paper #1) |
| #17 | ✅ forced | ✅ forced | ✅ forced | Cumulative tracker note added; P03/P06/P07/P11/P13 pending |

**Net post-M-1 + M-2 coverage:** Papers #1, #2, #3, #14, #16 have ~2 of their load-bearing primitives closed (typically P09 + P04). Papers #6, #11, #13, #15 have ~1 of their load-bearing primitives closed (P04 §1.5 or P04 core). Paper #17's tracker note reflects cumulative status.

---

## 6. Execution Checklist

After M-2 paper is written and accepted:

- [ ] Open Paper #1, navigate to §3.0, replace P04 bullet per spec.
- [ ] Open Paper #2, navigate to §3.0, replace Bandwidth-additivity bullet.
- [ ] Open Paper #3, navigate to §3.0, replace both Four-band-orthogonality and Bandwidth-additivity bullets.
- [ ] Open Paper #6, navigate to §3.0, replace Four-band-partition bullet.
- [ ] Open Paper #11, navigate to §3.0, replace Adjacency-Fourier-conjugate bullet.
- [ ] Open Paper #13, navigate to §3.0, append post-M-2 note to Per-channel-evolution-rule bullet.
- [ ] Open Paper #14, navigate to §3.0, replace Bandwidth-additivity bullet.
- [ ] Open Paper #15, navigate to §3.0, replace Adjacency-Fourier-conjugate bullet.
- [ ] Open Paper #16, navigate to §3.0, replace P04 bullet.
- [ ] Open Paper #17, navigate to §3.0 + §3.3, replace primitive-set opening sentence, Four-band-partition bullet, and Participation-measure-structure parenthetical; update §3.3 Honest Reading paragraph.
- [ ] Update Meta-Paper M0 §5.1: change P04 tag from "likely forceable" to "FORCED in M-2 (2026)."
- [ ] Update Meta-Paper M0 §6.2: change P04 core scope from "scoped under Routes B + D" to "FORCED in M-2 (2026)."
- [ ] Update Meta-Paper M0 §6.3: change P04 §1.5 scope similarly.
- [ ] Update Dependency Graph §5: change P04 row from "load-bearing input" → "now upstream-forced."
- [ ] Update MEMORY.md: add or update project_primitive_forcing_arc.md entry to note M-2 closure.
- [ ] Identify next M-paper: M-3 (P11). NPP scaffold already exists.

**No proofs, equations, or §§4–10 content touched in any paper.**

---

## 7. Post-M-2 Status

After this plan is applied:

- **P04 core + P04 §1.5 closed:** Routes A + C + D + B (joint).
- **10 downstream papers updated** with surgical §3.0 edits.
- **Displaced-postulate critique elimination:** combined with M-1, now applies to ~10–13 of 17 papers (depending on how counts overlap).
- **Cumulative coverage:** Papers fully primitive-forced (every §3.0 entry now M-series-forced): #16 essentially complete; #1, #2, #3, #14 mostly complete (pending P11, P03+P07); others partial.

**Next priority:** M-3 (P11 commitment irreversibility). UPDATE_PLAN_after_M3.md covers the corresponding §3.0 updates.

---

**End of plan.**
