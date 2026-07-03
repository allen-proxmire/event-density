# A3 — Topology / Σ-Law / Reach-Grading Sweep: Results

**Bits-measurement angle #3 (`project_bits_measurement_state.md`), run 2026-07-01. The prior robustness sweeps (size, MI estimator, observable) all varied one dial on a fixed chain-plus-hard-bridge substrate. This sweep varies the substrate's shape and rule instead: topology, Σ-coefficient balance, and whether the reach boundary is graded or hard. Same certified simulator, same M1/M2/M3/Delta pipeline (`analysis/delta.py`), no new rules.**

## Result summary

| Axis | Configurations | Severance (M2 ≈ shuffle floor) held? |
|---|---|---|
| Topology | chain, tree, grid | **3/3 yes** |
| Σ-law | balanced, coherence-dominated, strain-dominated, gradient-dominated | **4/4 yes** |
| Reach grading | bridge bandwidth 0.5 → 0.001 (never marked decoupled) | **0/6** (all show real cross-boundary information) |
| Reach grading | hard-decoupled reference | **1/1 yes** |

## 1. Topology — robust, with one caveat

Severance holds cleanly across chain and tree topologies: both show strong within-stratum signal (M1 = 0.82 for chain, 0.39 for tree) and near-zero across-boundary information (M2 ≈ M3, the shuffle-floor). This is a genuine, discriminating confirmation — there was real information to sever, and it was severed.

The grid case also reads "severance holds," but it's a weaker test than it looks: grid's own within-stratum signal (M1 ≈ -0.005) is also near zero. There wasn't much correlation there to begin with, so "M2 near zero too" doesn't discriminate the same way. Read the grid result as "no measurable structure detected, boundary or no boundary," not as a strong positive confirmation. Worth a follow-up with a grid construction that produces a stronger internal signal (e.g. a denser lattice, or measuring diagonal rather than column-split halves) before leaning on it.

## 2. Σ-law — robust, with the same caveat pattern

Severance holds across all four coefficient regimes tested. Balanced and strain-dominated regimes show strong M1 signal (0.82 each) with clean severance. Coherence-dominated shows a real but smaller signal (M1 = 0.25), also cleanly severed. Gradient-dominated shows almost no signal at all (M1 = 0.0015) — same caveat as the grid case: not much there to sever, so the "holds" reading is weak evidence at that extreme.

**Net for both axes:** wherever the substrate actually built up real within-stratum correlation (chain, tree, balanced/strain/coherence Σ), the boundary severed it completely. Wherever correlation was already weak to begin with (grid, gradient-dominated Σ), severance is true but nearly untested. The finding is robust; two of the seven "confirming" configurations just weren't strong tests.

## 3. Reach grading — the real discovery

This axis was built to ask whether severance is a hard threshold or something that appears continuously as bridge bandwidth is reduced. It instead surfaced a fact about the simulator itself: **bandwidth is not read anywhere in the certified update rule.** `compute_sigma` and candidate selection (`admissible_neighbors`) only ever consult the binary `decoupled` flag on an edge; the bandwidth number is stored but has no dynamical role in the currently certified Σ-rule.

The evidence: all six graded-bandwidth configurations (0.5, 0.25, 0.10, 0.05, 0.01, 0.001), spanning three orders of magnitude, produced **byte-for-byte identical measurements** (M1 = 0.042, M2 = 0.247, M3 = 0.0015 every time). Only the hard-decoupled reference case differs (M2 drops to the shuffle floor). That flat, unchanging result across such a wide sweep is itself the signature of a parameter that isn't wired into the dynamics, not evidence about physics.

**Honest reframe of the question this answers:** in the currently certified rule, reach is not graded, it is a strict on/off switch. Severance appears if and only if an edge carries the `decoupled` flag; it does not depend on how "thin" a non-decoupled channel is made. This is a real, useful finding about the current simulator's scope, not a bug to silently patch — extending the rule so bandwidth genuinely modulates candidate admissibility or Σ (a graded reach mechanism) would be a distinct, follow-on piece of work, not a fix to this sweep.

## 4. Overall verdict

**The core finding — perfect, architecture-independent severance at a decoupling surface — survives every topology and every Σ-coefficient regime tested where there was meaningful signal to sever.** The one place severance visibly fails is exactly where it should: a bridge that was never actually marked as a decoupling surface, regardless of how weak its nominal bandwidth is. That's not a counterexample to the finding; it's a confirmation that `decoupled` is the substrate's real, sole boundary mechanism as currently built, and a clean, honest discovery that "reach" in this simulator doesn't yet have a graded form to test.

## 5. What this resolves and what it opens

**Resolves:** angle #3 (topology/reach/Σ-law exploration) as scoped in the bits-measurement memo — the dynamical repertoire has been characterized across three topologies and four Σ regimes, and severance is architecture-independent within that repertoire.

**Opens:** whether wiring bandwidth into the Σ-rule or candidate selection (making reach genuinely graded) would produce a continuous transition to severance, or whether it would stay a hard threshold even then — a natural, well-scoped follow-on, distinct from this sweep.
