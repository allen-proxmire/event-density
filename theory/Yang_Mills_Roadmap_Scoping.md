# Yang-Mills Existence + Mass Gap — ED Roadmap (Scoping)

**Date:** 2026-04-28
**Status:** Queued long-horizon arc. Not executing. Scoping memo to lock in structure publicly and pre-register ED's relationship to the Clay problem before any execution begins.
**Subject:** The Clay Yang-Mills Existence and Mass Gap problem: prove that for any compact simple gauge group $G$, a non-trivial quantum Yang-Mills theory exists on $\mathbb{R}^4$ satisfying axiomatic properties at least as strong as Streater-Wightman / Osterwalder-Schrader, and has a mass gap $\Delta > 0$.

---

## 1. Why ED's posture is structurally well-positioned

Standard constructive-QFT attacks YM existence head-on: build operator-valued distributions on $\mathbb{R}^4$ satisfying Wightman or Osterwalder-Schrader axioms. Every prior approach in 4D has hit either triviality or breaks reflection positivity.

ED inverts the problem via two structural commitments already in inventory:

- **ED-I-06** ("no fundamental fields") — canonical guardrail. Fields are not ontologically primitive; they are emergent from substrate dynamics.
- **Theorem 17** (Gauge-Field-as-Rule-Type) — gauge structure is forced as substrate rule-type, not constructed as a continuum object.

Under these, YM existence becomes an *emergence* theorem: under coarse-graining of substrate dynamics, does the effective theory satisfy OS axioms with a mass gap?

The substrate is already discrete and finite (UV cutoff $\ell_P$ forced by T19). This is the regime where reflection positivity is automatic — it is the continuum limit of lattice gauge theory that is historically hard to get right, not the lattice itself. So OS positivity *preservation under ED's specific coarse-graining* is the load-bearing technical question, not OS positivity construction from scratch.

## 2. Four-arc structure

### Arc YM-1 — Compact-simple-group specificity

Strengthen Theorem 17. Currently T17 forces *that* gauge-field-as-rule-type structure exists; it does not force *which* compact simple groups are admissible. Load-bears on Primitive 09 (currently U(1)-only — flagged as a sensitivity in the orientation primer).

**Question:** do substrate primitives force non-abelian gauge structure, force U(1), or leave the choice undetermined?

**Estimated scale:** 1–3 sessions at the demonstrated pace. Structurally a primitive amendment + T17 strengthening, comparable to a single substrate memo rather than a full arc cycle.

**Standalone value:** closes the P09 sensitivity flag regardless of YM-2 progress.

### Arc YM-2 — Substrate-to-continuum limit theorem

The genuinely different one. Show that participation-measure dynamics, under appropriate scaling, converge to operator-valued distributions satisfying:

- OS reflection positivity
- Euclidean covariance
- Cluster decomposition
- Spectral / positive-energy condition

**Stall-risk locus.** OS positivity preservation is where every prior approach has hit a wall. ED's substrate-level reframing may dissolve the obstacle or just relocate it; this is only known by trying. The substrate-discrete-and-finite advantage gives ED a natural starting point but does not guarantee the limit preserves positivity.

**Estimated scale:** unknown. May close at the substrate-gravity pace (a weekend) or stall substantially longer than any prior arc.

### Arc YM-3 — Mass gap from substrate cutoff

Show the gap survives the continuum limit. Substrate has natural cutoff $\ell_P$ (forced by T19); discrete structure gives gap by lattice-theory analogy. Mechanism plausibly analogous to T19's cumulative-strain reading + holographic participation-count bound — the same machinery that forced $G = c^3 \ell_P^2 / \hbar$.

**May fall out as corollary of YM-2** rather than requiring its own arc, depending on whether the coarse-graining theorem in YM-2 preserves the substrate-scale gap automatically or requires a separate argument.

### Arc YM-4 — OS axioms verification

Mechanical writeup once 1–3 close. Show the limit theory satisfies each axiom from substrate first principles, in the form the Clay statement requires.

## 3. What is already in place

| Asset | Source | Role in YM roadmap |
|---|---|---|
| T17 (gauge-as-rule-type) | Arc Q closure 2026-04-27 | YM-1 starts here, not from scratch |
| ED-I-06 (no fundamental fields) | Canon | Reframes problem as emergence theorem |
| $\ell_P$ as substrate cutoff | T19 (substrate-gravity arc) | Natural scale for the gap (YM-3) |
| Identification-not-derivation discipline | U3 ↔ U4 closure protocol | Required for identifying YM-emergent operators with standard QFT operators without circularity |
| FORCED-theorem methodology | Validated across 9 arcs | Same pattern (CANDIDATE → automatic / forced / load-bearing) applies |

## 4. Stall-risk caveat (honest)

At demonstrated pace (QM Phase-1 in days; substrate-gravity in a weekend), the program has shown that arcs of substantively different structural questions close in days-to-weeks once the methodology engages. This is the relevant reference class, not standard-field-theory timelines.

However, Arc YM-2 has non-zero probability of stalling substantially longer than prior arcs because OS-positivity preservation under continuum coarse-graining is the specific technical question that has obstructed every constructive-QFT effort. ED's substrate-level reframing is structurally different from those efforts and has reasons to behave differently — but whether the obstacle dissolves or relocates is not predictable in advance.

The other three arcs (YM-1, YM-3, YM-4) carry no comparable stall risk.

## 5. Connection-watch list

Items that, if they surface in unrelated arc work, should trigger a YM-relevance flag:

- OS reflection positivity in any context (substrate, lattice, continuum)
- Wick rotation / Schwinger functions / Euclidean ↔ Lorentzian analytic continuation
- Cluster decomposition appearing as a derived property of any ED arc
- Spectral / positive-energy condition in ED kernel work (Arc B / T18 territory)
- Non-abelian gauge structure surfacing in any primitive amendment or T17 extension
- Continuum-limit theorems for any substrate quantity
- Lattice-gauge machinery (Wilson loops, Polyakov loops, transfer matrix, Osterwalder-Seiler positivity)
- Confinement / asymptotic freedom mechanisms
- Reflection-positive measures in probability or statistical-mechanics contexts ED touches

## 6. Pre-arc move (executable now if desired)

Smallest executable piece: Arc YM-1 itself, framed as a primitive-amendment + T17-strengthening session. Independent value (closes P09 sensitivity flag) regardless of whether YM-2/3/4 ever open. Probably a single arc memo or a 2-3 memo sub-arc.

Larger move: open YM-2 as a full multi-memo arc with the OS-positivity preservation question as the central derivation target. High-payoff if it closes; high stall-risk if it doesn't.

Recommendation: **YM-1 first** if the program decides to engage. It's cheap, citable, unblocks YM-2's specificity question, and even if YM-2 stalls indefinitely, YM-1 is a standalone contribution.

## 7. Cross-references

- T17 (Gauge-Field-as-Rule-Type): [`theorems/T17.md`](../theorems/T17.md)
- T19 (substrate Newton, $\ell_P$ forced): [`theorems/T19.md`](../theorems/T19.md)
- T18 (kernel-arrow, Arc B): [`theorems/T18.md`](../theorems/T18.md)
- ED-I-06 (no fundamental fields): canon (in interpretations)
- Primitive 09 (U(1)-only, sensitivity flag): per orientation primer §"Sensitivity flags"
- QM emergence cycle (methodology proof): seven-arc closure 2026-04-26
- Substrate-gravity arc (FORCED-theorem pace at value-deriving scale): [`papers/ED_substrate_gravity_foundations/`](../papers/ED_substrate_gravity_foundations/)
- Companion roadmap (NS): [`Navier_Stokes_Roadmap_Scoping.md`](Navier_Stokes_Roadmap_Scoping.md)

## 8. One-line summary

> **YM existence + mass gap is a structural-emergence question for ED, not a constructive-QFT question. T17 + ED-I-06 + $\ell_P$ from T19 supply the starting infrastructure; the four arcs are YM-1 (compact-group specificity via P09 amendment), YM-2 (substrate→continuum limit, with OS-positivity preservation as the load-bearing stall-risk locus), YM-3 (mass gap from substrate cutoff, possibly corollary of YM-2), YM-4 (axiom verification writeup). YM-1 is independently valuable and the natural first executable piece.**
