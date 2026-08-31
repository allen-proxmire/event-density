# Scoping Note — Spectral Dimension of the ED Substrate: a Measured Negative, and the Arena It Would Need

**Series:** Event Density (ED) Generative Papers — substrate-evaluation / curvature-emergence. **Scoping / fishing note.** Records a checked-and-parked question, one measured trap in the existing probes, and one positioning correction. Files a negative rather than a result.

**Status:** MEASURED (the integer-reach coupling floor; the method validation) + DECLARED-OPEN (the actual question, which no built arena can currently answer). Does **not** claim a spectral dimension for ED, does not claim a dimensional flow, and does not claim ED is or is not like any other quantum-gravity program in the ultraviolet beyond the one sourced contrast in §5.

**Author:** Allen Proxmire · **Date:** 2026-08-31

---

## 1. The question, and why it was worth an afternoon

The **spectral dimension** of a space is what dimension a spreading process *reports* after running for a while: let something diffuse and watch how often it returns to where it started. It need not equal the number of coordinate directions, and in several independent quantum-gravity programs it does not. Causal dynamical triangulations, asymptotic safety, Hořava gravity and non-commutative geometry all find the same thing — spacetime behaves as ~4-dimensional at large scales and flows toward **~2 at short scales**. It is one of the very few numbers on which otherwise-unrelated approaches converge.

Two features made this look worth pointing at ED. First, `Paper_GR-II` already identifies ED's gravity as **khronometric, the Hořava infrared class**, so ED has a named relative in that set. Second, spectral dimension is a *connectivity* statistic: it is defined on a bare graph with no lengths on its edges, which is exactly what ED's participation graph is. Where most quantities require ED to inherit a scale, this one would not — a rare chance for the substrate to produce a number rather than take one.

A search of the corpus found **no prior treatment**: "spectral dimension" appears nowhere.

## 2. What the substrate offers that is the right *kind* of ingredient

A running dimension needs something about the effective connectivity to change with scale. ED has candidate structure here, and it should be recorded honestly as *suggestive*, not as a mechanism:

- **`Paper_097`** carries a three-regime RG flow: a **V1-dominated UV**, a transition regime, and a **V5-dominated IR**.
- **`Paper_092`** indexes each kernel by (scale, retardation order, **cross-chain rank**), placing **V1 at rank 1 (within a single chain)** and **V5 at rank 2 (pairwise, between chains)**.

Read naively that is the right shape: within-chain coupling is chain-like and low-dimensional, cross-chain coupling knits chains into a network and is higher-dimensional, so the dominant connectivity would look *lower*-dimensional at short range and *higher* at long range — the direction the 4→2 result runs.

**This is explicitly not an argument.** Cross-chain *rank* counts how many chains a kernel couples; spatial *dimension* counts directions. They are different quantities, and the fact that both involve "1 versus 2" is a word-level coincidence until something connects them. The corpus's standing retrofit rule (`Paper_ChargeAsTopology_B4`) forbids treating a numerical resemblance as structure. What §2 earns is a reason to run a measurement, nothing more.

## 3. The measurement, and the trap it surfaced

Run on the existing curvature-emergence arena, reusing `isotropy_3d_probe.build_graph_bfs`'s construction unchanged (bandwidth enters only through connectivity, `reach ~ b^p`). Script: `evaluation/CurvatureEmergence/spectral_dimension_probe.py`. Method: lazy random walk on the symmetrised graph, return probability by Rademacher trace estimation, `d_s = -2 dlog P/dlog t`. No dynamics needed — pure connectivity, which sidesteps the fact that ED's layer-1 transport is ballistic rather than diffusive.

**The method validates.** On a nearest-neighbour graph, where the answer must be 3, it returns **d_s = 3.10** over the mid-range window. The measurement itself works.

**The first control failed, and the failure is the finding.** At the arena's own settings the control (uniform bandwidth, no mass — which must read 3, flat) instead humped to **4.8** and sagged to 2.8. Diagnosis: at `R0 = 2` each locus has ~31 neighbours, so the walk spends the whole usable window still inside one neighbourhood-ball, and the far end is eaten by the box wall. There is no clean stretch between.

Chasing that produced the note's one hard result. The probes set reach as `max(1, round(R0 * b^p))`, and because that **rounds to a whole number** while `b` never exceeds 1, small `R0` cannot resolve any variation in `b` at all:

| reach setting `R0` | fraction of edges the mass changes |
|---|---|
| 1.0 | **0.00%** |
| 2.0 | 2.70% |
| 4.0 | 4.25% |

**At nearest-neighbour reach the bandwidth field is completely inert** — the construction is a plain lattice, and any result obtained there is a fact about the background rather than about `b`. This bounds the arena from both sides: reach must be large enough for `b` to couple at all, but every increment enlarges the neighbourhood and degrades any measurement that needs short scales. **Tier: Measured.** Recorded as a new scope item in `Paper_MetricFromTheGraph_ForcedTo3D` (preamble item 7); the P1–P4 results there are unaffected, since all were run at coupling reach.

Two further readings, both negative and both worth keeping:

- **The mass makes no difference to `d_s`.** Three depths (`b_min` = 1.0 / 0.2 / 0.05) give local `d_s` at `t = 15` of 3.089 / 3.098 / 3.104 — identical to three digits. On reflection this is expected rather than disappointing: curvature is a *local* geometry effect and spectral dimension is a *global* counting statistic. The arena was built for the first question.
- **Even at `R0 = 4` the mass perturbs only 4.25% of edges**, so the arena is a lightly-perturbed regular lattice, not a qualitatively different graph.

## 4. Why the question is parked rather than answered

The measurement can be made; it just cannot be made *informative here*. The hypothesis of §2 is about **V1 versus V5 dominance**, and:

- the curvature-emergence arenas have a **single connectivity rule, no chains, and no V5**;
- the certified Bits simulator likewise has **no V5 and no chains** — consistent with the standing corpus statement that the A1 channel-capacity result runs on a **V5-free** substrate.

**No built arena carries both kernels.** So the parked condition is specific and testable-for-readiness:

> **Blocked until an arena exists carrying chains with V1 within-chain links *and* V5 cross-chain links at a longer range.** With that, the question is: does `d_s` measured on short walks (before the walk feels V5) differ from `d_s` on long walks (after it does)?

Building such an arena is a real construction, not a probe tweak, and it carries the standing hazard that a purpose-built arena tests one's model of ED rather than ED — the failure mode recorded in `CLAUDE.md` for 2026-07-09. That hazard is the reason this is parked rather than queued.

## 5. One positioning correction, banked separately

Pointing at Hořava surfaced a gap worth closing on its own account. `Paper_GR-II` correctly places ED in the **Hořava infrared class**, and says nothing either way about the ultraviolet. But Hořava's UV reputation — power-counting renormalizability, and the very dimensional flow to 2 that motivated this note — rests on **anisotropic Lifshitz scaling** (`t → b^z t`, `z = 3`), which deliberately breaks Lorentz scaling at short distance. ED does the opposite: its V1 kernel is **Lorentz-covariant** (`z = 1`, `Paper_089`/`Paper_017`), and it regulates the UV by a physical grain cutoff instead (`Paper_111`), so there are no divergences to renormalize.

**ED and Hořava agree in the infrared and use opposite ultraviolet strategies.** No UV result of Hořava's transfers. Banked as `Paper_GR-II` preamble item 10, so a reader cannot slide from "Hořava infrared class" to "inherits Hořava's UV wins."

## 6. Bottom line

A checked negative with two by-products. The question — does ED's effective dimension run with scale — is **well-posed, unexplored, and unanswerable on any arena that currently exists**, and the blocking condition is named precisely (§4). The measurement method is **validated** (3.10 where 3 is required). The one hard finding is a **trap in the existing probes**: integer-rounded reach silently decouples bandwidth from connectivity below `R0 = 2`, which nothing in the code or the papers said. And one positioning fence is now in place (§5).

Filed as a negative on purpose. Without it, a future session meeting "ED is the Hořava infrared class" alongside "everyone else finds `d_s → 2`" will walk this path again and spend the same afternoon.

**Do-not-retry unless:** a two-kernel (V1 + V5) arena exists. Retrying on the curvature-emergence or Bits arenas will reproduce §3 exactly.
