# Gate 2 (#2b, chiral-gauge / T4 spinor gate) — Current-State Audit + Chirality-Wall Corridor Check

**Foundations — matter sector / #2b. Opened 2026-07-10.** Crank-rail ON. This note does NOT reinvent the #2b sprint (SQ1a–j, Gauge_01–11, T4_01–04, FirstArrival, ParityWall). It reads the *current* state (which has hardened past what `docs/ED_Research_Targets.md` #2b and MEMORY record), and audits the two open corridors the wall paper itself flags. Verdict up front: **the gauge structure is derived; two questions (uniqueness {1,2,3}; weak chirality) are walls; one flagged corridor collapses, the other = the standing gate. The optimistic June "arrow → net chirality, promising" framing is superseded and must be written back.**

Sources: `T4_01/02/03/04`, `Gauge_01–11`, `ChiralGauge_SQ1h/i/j`, `FirstArrival_HandednessImprint` (with its 2026-07-08 P-half retraction), `Paper_ParityWall_ChiralityVerdict` (the hardened published verdict), `Paper_MS-I/II` (the two matter-sector papers). Verified via two grounded cluster-reads 2026-07-10.

---

## 1. The current three-part state (hardened 2026-07-08)

**(A) Gauge + spinor STRUCTURE — substantially DERIVED (structural tier).** A real, coherent sector, well past T17's "rewrite by analogy":
- `SU(N)` from channel multiplicity (Gauge_01, derived-conditional on the ℂ-amplitude; indistinguishability alone gives only `S_N`).
- P05-transport = a `U(N)` lattice gauge connection (Gauge_02); gauging is **generically non-abelian** (Gauge_10: `F≠0` in 2000/2000 trials; abelian = measure-zero). The `SU(N)` mixer is **P05 re-routing, not V5** (Gauge_10 correction — retires the "V5 = SU(N) mixer" analogy).
- Yang–Mills action `−¼Tr(F²)` from the coherence-deficit on the plaquette holonomy (Gauge_06, numerically verified); mass gap ⟺ non-commuting channels (Gauge_07, mechanism tier, continuum survival unproven).
- Single hypercharge `U(1)_Y` = the **one global P09 phase** against the one arrow-flow (Gauge_11) → `∏SU(N_i)×U(1)_P09 = SU(3)×SU(2)×U(1)_Y`. Values inherited; EWSB Higgs-gated.
- Spin-½ double cover from channel tethering (T4_03, account tier).

**(B) Gauge-group UNIQUENESS {1,2,3} — OPEN WALL.** Why exactly `SU(1)×SU(2)×SU(3)`? Both mechanisms are down: the spatial-dimension bound is a category error (Gauge_04: color is rotation-invariant, `ℝ³→SO(3)` dim 3 ≠ `ℂ³→SU(3)` dim 8), and the channel-stability route is refuted (Gauge_09: the symmetric `SU(N)` multiplet is stable for *all* N; coherence-binding *grows* with N — the intuition was backwards). Gauge_08 reduces it to one clean number: **uniqueness {1,2,3} ⟺ internal channel-amplitude dimension `d=3`.** No built route. The one live (unbuilt) lead: the **3D-special linking/braiding** structure (the ChainsAsLinks arc's K6-minor result), *if* channel structure is braiding-based, could fix internal-`d=3` from spatial-3 without the Gauge_04 category error. Speculative.

**(C) Weak CHIRALITY / parity violation — WALL, inherited not derived.** T4_04 (2026-07-08) triple-confirmed the emergent fermion is **vector-like by default**, from three independent angles:
- *transport/screw:* the SQ1g discriminator `advance(L) − advance(R)` reduces to a single geometric quantity — the **screw pitch `n_z`** (frame-rotation about the arrow). Canonical `U(N)` transport does not force a screw; in 3+1D the arrow is a *time* axis and picks out no spatial rotation axis → `n_z = 0` → vector.
- *wiring/topology:* canonical P07 (Paper_087) is a **combinatorial** distinguishability statement — no geometry, no topology, hence no handedness. The "channel topology" that would carry a helix is an unbuilt Phase-2/3 elaboration.
- *selection/first-arrival:* the first commitment can imprint C (matter/antimatter, via the parity-**even** P09 circle `S¹`) but **not P** — there is no parity-**odd** order parameter (no handed spatial 3-frame; the arrow is a time axis, P09 is internal, B5 is a headless director). This **retires the FirstArrival keystone's "one event imprints both C and P" P-half** (its correction banner is applied); the C-half (baryogenesis) stands.

The June optimism ("arrow → net chirality, topological, plausibly maximal") was **1+1D dimension-special** (there the single spatial axis *is* the arrow, collapsing the screw distinction); in 3+1D it does not survive. Published as `Paper_ParityWall_ChiralityVerdict` (current, hardened). **Matter/antimatter (C) is ED-native; weak parity violation (P) is inherited.**

---

## 2. Corridor audit — are the wall paper's two open corridors live?

`Paper_ParityWall` is honest that its "P is a wall" verdict is not airtight: it flags two open corridors (§2 scope, §5 anomaly). Both are exactly where the earlier (never-built, structural-synthesis) SQ1i "V5 = chiral gauge coupling" hope would live. I audit each.

### Corridor 2 (the P09 anomaly) — COLLAPSES (self-defeating)
The caveat: "internal-U(1) → parity-inert → C-not-P" assumes the P09 `U(1)` is not *anomalously* parity-odd in 3+1D; if it were, the selection route could give P.

**This corridor cannot source parity violation, because every mechanism that would make P09 parity-odd needs a prior parity-odd input the parity-symmetric substrate does not supply:**
- A **chiral (ABJ) anomaly** that makes `∂·j₅ ∝ F∧F` parity-odd requires **chiral fermions** in the P09 coupling. But the fermion is vector-like (§1C). A vector `U(1)` has equal L and R content; the triangle's parity-odd part cancels. So the anomaly cannot appear unless chirality is *already* present — it is downstream of chirality, not a source of it. Circular.
- A **`θ F∧F` (topological) term** is parity-odd, but its coefficient `θ` is itself a parity-odd input; on a parity-symmetric substrate `θ = 0` by symmetry unless something *else* breaks parity — relocating, not solving, the wall.

So corridor 2 requires the handedness it is supposed to produce. **It is not an independent route; remove it.** (This is a genuine tightening of ParityWall §5 the paper did not make.)

### Corridor 1 (the irreducible-generator emergent spinor) — REAL, but = the standing gate
The caveat: T4_04's vector verdict used the **reducible** minimal transport `U = e^{iφ}·V` (scalar P09 phase × `SU(2)` frame), in which `φ` **cancels** from the discriminator. An "irreducible" construction, where the phase-advance is locked to the spin-frame ab initio, "is not shown to reduce to the same `n_z` discriminator."

**Sharpening what this corridor actually is.** At the **Weyl 2-spinor** level the caveat has no teeth: every `U(2) = e^{iφ}·SU(2)`, so T4_04's scan is fully general and `advance(L)−advance(R) = f(n_z)` is the complete 2-spinor answer (chirality ⟺ screw, screw unforced). The corridor's teeth are only at the **full 4-spinor** level (`γ⁵` acts across two Weyl blocks) and/or where the P09 phase is **generated by the same object** as the frame transport (so `n_z` cannot be scanned free of `φ`). Building that is exactly the open **§3.7 gate**: construct the full emergent 4-spinor from substrate d.o.f. (the channel-topology→gauge program, P07 §7.4), which every T4 doc names as "a major program with no guarantee the result is handed." **Corridor 1 is not a shortcut around the wall; it IS the standing gate.**

**Net of the audit:** the chirality wall is honest and, after removing corridor 2, rests on the single open gate (corridor 1 = the full channel-topology→gauge construction). The wall stands unless that major program is built *and* comes out handed — which the primitive-level evidence (no handed structure anywhere in P05/P07/first-arrival) rates as unlikely, but not impossible. Correct honest label: **weak chirality is inherited by current evidence, open only through the one unbuilt gate.** Not a *proven* wall (unlike primality); a well-founded, four-times-confirmed, one-corridor-open wall.

---

## 3. Honest tier + net for the roadmap

**Gate 2 is mostly resolved, not a live derivation front.** Structure derived (a strong, banked result); two questions are walls (uniqueness {1,2,3}; weak chirality), each with one unbuilt corridor (internal-`d=3` via 3D-linking; the full 4-spinor gate). This is the *form-forced / value-inherited* pattern again: ED derives the **shape** of the Standard-Model gauge+spinor sector and inherits the two things that pick out *our* SM (which groups; which handedness).

**Strategic consequence (for `ED_Road_To_Unification.md`).** Both "structural gates" have now been worked: Gate 1 (P-Channel) reconstructed; Gate 2 (#2b) resolved to derived-structure + two walls. The program's open frontier is even smaller and more wall-shaped than the 2-day-old roadmap said — which *strengthens* its core thesis (form delivered broadly; the rest inherited or walled). The live research is no longer "close the gates" (largely done) but: (i) the one unbuilt gate behind chirality *if* one wants to test handedness, (ii) the internal-`d=3` lead for uniqueness, and (iii) the prediction inventory (the undeniability weapon).

**Documentation debt found (close-the-loop):** #2b (research map) and MEMORY still carry the June "arrow → net chirality, promising" framing; the roadmap calls #2b "the live hard front"; and the **current headline matter-sector paper `Paper_MS-II` overclaims the retired P-imprint** ("first commitment imprints both C and P; V5 is where parity lives"), as does the superseded `Paper_MS-I`. These are corrected / flagged alongside this note.
