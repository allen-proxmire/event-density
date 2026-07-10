# ED — The Road to Unification (the finish-line view)

*The strategic "where to go" map. It pairs with `ED_Research_Targets.md`, which is the authoritative per-target status log; this doc organizes those same targets against **what unifying physics actually requires**, so research energy lands on the load-bearing gates and not on the inherited-by-design or walled items. Built 2026-07-10. When an arc closes, update `ED_Research_Targets.md` first, then reflect any strategic shift here.*

---

## The one thing to see first

ED has delivered the **form** of nearly all of physics: QM kinematics, gravity plus the dark sector, the continuum (Maxwell as the coherent field), black-hole thermodynamics, entanglement, the cosmology boundary. The open frontier is **not** spread across a hundred loose ends. It is three things:

- **Two structural gates** (the "is ED actually *forced* where it currently *inherits*?" questions): **#8b** and **#2b**.
- **One goal-weapon** (the move that makes ED undeniable, a different axis from closing the theory): the **prediction inventory**.

Everything else is either already done (form), **inherited by the theory's own logic** (the constants), or **proven unreachable** (primality). That is the entire map. The value of this document is that it makes those categories *visibly different*, so a session never pours structural-research effort into a target that ED's own results say is inherited, or into a proven wall.

---

## The finish line: what "unify physics" requires

A checklist any candidate unified theory must satisfy, with ED's current standing and the *kind* of target each is.

| # | Requirement | ED status now | Kind | Gating item |
|---|---|---|---|---|
| 1 | **QM foundations** (Hilbert space + Born rule from the substrate) | Form closed **except** the inner-product keystone (channel orthogonality) | **Structural gate** | #8b |
| 2 | **Gauge structure + chirality** (why `SU(3)×SU(2)×U(1)`, parity violation) | Structurally in place, reduced to the T4 spinor gate; not yet a derivation | **Structural gate** | #2b |
| 3 | **Matter spectrum** (generations, Yukawa masses, mixing, Higgs / EWSB) | Mostly open; mass sector open; folds into #2b + the value layer | Mixed | #2b, value |
| 4 | **Gravity** (GR + dark matter + dark energy + the quantum side) | **CLOSED** as khronometric (GR-I..IV) + khronon MOND/DE (KM-I/II) | Done (form) | — |
| 5 | **Cosmology + baryogenesis + Λ** | SCBU M3-closed; baryogenesis lock folds into #2b; Λ-magnitude = `Θ_ED` substrate constant (inherited) | Mostly done / value | #2b, #10 |
| 6 | **The constants** (α, mass ratios, mixing angles, the Λ *value*) | **Inherited-in-principle by ED's own result** (no intrinsic scalar; A1 + Facts + FSC) | Value frontier (settled-as-inherited) | #9 |
| 7 | **Classical / continuum limit** (Maxwell, Navier-Stokes, Yang-Mills, thermo) | Coherent field = the textbook object; the layers program (#3c); named debts owed | Done (form), with debts | #3b debts |

**The strategic read:** requirements 4, 5, 7 are essentially delivered at the form level. Requirement 6 is not a to-do list, it is *answered* (see the value frontier below). So the live structural work is exactly requirements 1 and 2, which are the two gates.

---

## The three kinds of target (why the map is small)

**1. Structural gates.** The "is ED forced, or is it inheriting?" questions. Few, and high-leverage: closing one re-promotes a whole cluster of results from inherited/conditional to forced. This is where research energy goes. Two are live: **#8b** and **#2b**.

**2. The value frontier (the constants).** ED's own result settles this, and it is easy to mistake for open research. By A1 (no intrinsic scalar exists in the substrate) plus the Facts ontology plus the FSC arc (closed 2026-05-25), the fundamental constants are **inherited-in-principle**: they are boundary conditions the theory carries, not quantities it derives. So this is mostly a **non-front**: *think, don't chase*. The exceptions that genuinely moved are specific and named: `Θ_ED` (Λ-smallness, promoted to a substrate constant 2026-07-06, #10), `G = c³ℓ_P²/ℏ` (derived given `ℓ_P`), `a₀ = cH₀/2π` (form derived, value inherited). Do not open a general "derive the constants" program; ED already predicts they are inherited.

**3. Proven walls.** Never spend effort here. **Primality** (the Möbius/parity sign) is ED's one *proven* no: a finite-memory substrate provably cannot reach it (Sarnak's barrier is the external ruler). The load-bearing discipline (from `Paper_FormAndFlesh_TwoWalls`): the walls are heterogeneous and do not transfer. A proven no about primality says nothing about gravity or Maxwell, and a win on Maxwell says nothing about primality.

---

## The gate map (the actual roadmap)

### Gate 1 — #8b `P-Channel-Orthogonality` (the QM-foundations keystone)

- **What it is.** The single open postulate sitting under three downgraded theorems at once: **T10** (Born rule), **T11** (discrete inner-product / Bell-Tsirelson), **T12** (continuum inner-product). Distinct channels being orthogonal, `⟨K|L⟩ = 0`. Close it and all three re-promote; the QM foundations become forced rather than inherited.
- **Status.** The sibling half, `P-Gleason-Compatibility`, is partially derived (bookkeeping sense, via P02+P04). Orthogonality is the remaining half. Three derivation routes have failed (P04 additivity, P07 distinctness, P11 phase-randomization); a candidate regime-bound (`c₁₂`) was tried and withdrawn. The sharpened question is not "prove `⟨K|L⟩=0` inside an already-free vector space" (true there by construction) but "is the free/orthogonal representation physically correct at all."
- **Why first.** Nearest, most self-contained, bounded. A clean structural question, not a program.
- **Detail:** `ED_Research_Targets.md` #8b · `foundations/Gleason_Rehabilitation_Attempt.md` · `ED Generative/theorems/T11.md` + `T12.md`.

### Gate 2 — #2b chiral gauge / the Standard-Model matter sector

- **What it is.** Producing parity-violating chiral gauge couplings and the SM matter content from a parity-symmetric substrate. The sharpest challenge to the discreteness commitment.
- **Where it now sits.** After a long sprint (SQ1a-j, the gauge program Gauge_01-08, the first-arrival keystone), #2b is **not walled** (Nielsen-Ninomiya does not bind ED: no Brillouin torus, non-hermitian arrow) and is **reduced to the T4 spinor gate** (`Paper_106` §3.7) plus the channel-topology→gauge program. Real positive support: the arrow carries a net chirality that is topological, sparsity-robust, and plausibly maximal; parity violation can only live in the non-abelian (V5 / cross-channel) sector; `SU(N)` comes from channel multiplicity; and the whole thing plausibly unifies with baryogenesis as one first-arrival handed-commitment lock.
- **Open hard core.** The relativistic `γ⁵` bridge (discrete net chirality → Lorentz-covariant Weyl coupling), why internal `d=3` (the braiding / linking thread), anomaly cancellation (SQ3), and why the weak force specifically is chiral (the η-thread).
- **Why it is the big front.** The entire SM matter sector (requirement 3: generations, masses, mixing, EWSB) sits behind it. This is a genuine derivation via T4, not a tidy-up.
- **Detail:** `ED_Research_Targets.md` #2b · the `T4_*`, `Gauge_*`, `ChiralGauge_SQ1*`, `FirstArrival_*` foundations memos · `ED Generative/physics-papers/relativistic-qm/Paper_106_DiracEquation.md`.

### The goal-weapon (a different axis) — the prediction inventory

The north star is not *closing the theory*, it is a **confirmed, novel, falsifiable prediction** that ends arguments. That is orthogonal to the two gates and, for the program's *goal* (being undeniable, being seen), it is the highest-leverage build. The weapon is `ED Generative/physics-papers/predictions/Paper_101` (the Falsification Register + Prediction Inventory); growing it is the move. Live seeds already in the corpus: the Class-A multiplicity wall (140-250 kDa), `α₂=0`-exact (preferred frame), the merger-lag, the gauge-handedness ↔ cosmic-matter-sign correlation (falls out of #2b), the offset-velocity cluster knee.

---

## Where to point energy (the sequence)

1. **Gate 1 — P-Channel-Orthogonality.** Do now. Bounded; closes T10/T11/T12 in one stroke.
2. **Gate 2 — T4 / #2b.** The major research front. A real substrate→Dirac derivation, with the whole SM matter sector behind it.
3. **Prediction inventory (Paper_101).** Parallel track, the undeniability weapon; distinct from the gates, feeds the program's goal directly.
4. **Value frontier.** Background only. ED's own logic says the constants are inherited. Do not chase; think.
5. **Walls.** Never. Primality is proven unreachable; do not re-litigate.

---

## What this map does *not* change

- `ED_Research_Targets.md` remains the authoritative per-target log (status, dates, the full audit trail). This document is the strategic overlay, not a replacement, and defers to it on any detail.
- The closed column stays closed. ED has delivered form broadly (the "one-line read" in the targets doc lists it). This overlay is about the open front, and the point is that the front is **small and sharp**: two gates, one weapon.
- **One-line read:** *Physics-unification for ED = close two structural gates (#8b, then #2b), build the prediction inventory to make it undeniable, and leave the constants (inherited) and primality (walled) alone.*
