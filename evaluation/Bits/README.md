# The Bit-Measurement Project — Plain-Language Summary

*Final summary of the determinability-boundary measurement for the Event Density substrate.*

**Status:** Complete (proof-of-method). Simulator certified; the boundary measured at **Δ ≈ 0.09 bits**.
**Author:** Allen Proxmire · June 2026

---

## In one paragraph

Event Density (ED) describes reality as a web of tiny events that influence each other only over a finite reach. Earlier work argued — on paper — that this finite reach creates a **boundary**: past a certain point, one region of the substrate simply cannot determine what happens in another. We called that the *determinability boundary*. This project asked a sharper question: **can we actually measure how much "knowability" is lost across that boundary, and put a number on it in bits?** To do that we built a small, faithful computer simulation of the ED substrate, proved (with automated tests) that it behaves exactly as the theory says it should, and then ran the measurement. The answer: yes — the boundary blocks a real, positive, repeatable amount of information. On our test setup that came out to about **0.09 bits**.

---

## What we set out to do

The ED framework had a *structural* claim: there's a horizon in the substrate (a "decoupling surface") past which one region can't determine another. That claim was solid on paper. But a claim like "information is lost across this boundary" is the kind of thing you can, in principle, **measure** — count the lost bits, the way information theory counts anything. This project was about turning the words into a number, honestly.

There was a parallel motivating it: a separate piece of mathematics (the "Factor Skyline" / prime-number work) has its *own* such boundary — the parity barrier — and that one has been quantified (~0.265 in its units). We wanted to show ED's boundary can be quantified *in the same way* — same kind of measurement, not the same number, and **with no claim that the two fields are secretly the same**.

---

## What we built

We built the measurement from the ground up, in deliberate stages, and we never let ourselves measure the number until the tool was proven correct.

1. **A simulator of the ED substrate.** A small program (seven modules) that creates a network of events and evolves it by ED's own rule — each step, every active "chain" picks the single best next move by a local score (coherence minus strain), and once something is committed it can never be undone. Crucially, it uses ED's *actual* selection rule, **not** a smoothed-out approximation — that distinction turned out to matter (see below).

2. **Four "correctness gates."** Before trusting any measurement, we demanded the simulator prove four things, as automated tests:
   - **Monotonicity** — commitments only ever accumulate, never reverse.
   - **Acyclicity** — the system never loops back to an earlier state; it always moves forward.
   - **Factorization** — *this is the key one* — two regions separated by a decoupling boundary truly cannot affect each other.
   - **Tie-break** — when two moves score equally, the rule still picks one, deterministically.

3. **A test case (the "MWE").** Two small clusters of events joined by a single **decoupled bridge** — i.e., a built-in determinability boundary — with each cluster started from its own independent random conditions.

4. **The measurement itself.** Run the test case hundreds of times with different random starts, then compare how predictable things are *inside* a cluster versus *across* the boundary.

All of it is automated. A single command (`certify.py`) runs every check and either stamps the simulator **CERTIFIED** or refuses.

---

## What we found

**The simulator is certified.** All four gates pass together — 20 out of 20 automated tests, every time. In particular, the factorization gate passed two independent ways:
- **Exactly:** if you change the random seed of one cluster, the other cluster's history comes out *bit-for-bit identical*. They genuinely cannot touch each other across the boundary.
- **Statistically:** the shared information between the two clusters is essentially zero — indistinguishable from pure noise.

**The boundary is measurable, and it blocks real information.** The measurement compares three quantities (all in bits):

| Quantity | What it measures | Result |
|---|---|---|
| **Within a cluster** | how much one half tells you about the other half | **+0.092 bits** |
| **Across the boundary** | how much one cluster tells you about the other | **≈ 0** (−0.002) |
| **Pure-noise baseline** | the measurement's own background level | **≈ 0** (−0.001) |

The headline number is the gap between the first two:

> **Δ ≈ 0.09 bits** — the amount of "knowability" that exists *inside* a region but does **not** cross the determinability boundary.

It's positive, it's well above the noise floor, and it stayed steady (0.085–0.095) when we changed how many runs we averaged over. The controls behaved exactly as the theory predicts: information flows *within* a region and stops *at* the boundary.

---

## Wait — what does "0.09 bits" actually feel like?

It's natural to read "0.09 bits" as *"the most one event can hand off."* It isn't that. The number is a **comparison of two correlations**, and the easiest way to feel it is a betting game.

Run the toy universe many times. Each run, jot down how *busy* the **left half** of region A got, and how *busy* its **right half** got. Then ask: **if I tell you the left half was busy, how well can you bet on the right half?**

- **Inside region A:** a little better than a coin flip. The two halves are part of the same connected region, so a faint signal links them — told "left busy," you'd guess "right busy" and win modestly more than half your bets. That faint edge is the **0.09 bits**.
- **Across the boundary (region A vs. region B):** no edge at all. Told *everything* about A, your best guess about B is a dead-even coin flip. The two sides are total strangers — **0 bits**.

So picture the decoupling boundary as a **perfectly soundproof wall**. Inside a region, two halves hear each other faintly through a thin wall. Across the soundproof wall, region B hears *nothing* of region A, ever. **Δ measures how much hearing the wall removes** — the faint signal inside (0.09 bits) that the boundary erases to silence (0 bits).

**And here's the key — the meaning is in the contrast, not the value.** A "bit" is a yes/no's worth of knowing; 0.09 bits is *small* — a faint lean, not a lock. The point was never that 0.09 is big. The point is: **inside a region the number is real and nonzero; across the boundary it drops to exactly zero.** That zero isn't trivial — there *was* a signal to block, and the boundary blocks all of it. That collapse — real signal inside, nothing across — *is* the determinability boundary, made into a number. The 0.09 is just how big the erased signal happened to be in our little 16-event test.

(This is also why the prime-number "0.26" feels more solid than our "0.09": *theirs* is baked into the integers themselves — a true property of that architecture — while *ours* is a number for our specific toy. They're alike in **kind** — a boundary measured in bits — not in being comparable numbers.)

---

## A surprising thing we learned along the way

ED's smoothed-out, "zoomed-out" version is a **diffusion** equation — things spread and blur. But the underlying substrate does the **opposite**: because each step picks the single best move (a sharp choice, not an average), the substrate actually *sharpens*. The blurriness only appears when you average over many events. In plain terms: **the fuzziness people associate with ED is a side-effect of zooming out, not a property of the thing itself.** Our simulator reproduces the sharp substrate directly — which is exactly why it was the right tool for measuring the boundary.

---

## What the number means — and what it does *not* mean

**It means:** ED's determinability boundary is real in a measurable, quantitative sense, not just a structural turn of phrase. You can count the bits it blocks, and the count is positive and stable. The method works.

**It does *not* mean** (and we were careful about this throughout):
- **0.09 bits is not a fundamental constant of ED.** It's the number *for our small test setup*. Change the size, the wiring, or the tuning knobs and the number moves. What's robust is the *pattern* (information stops at the boundary), not the exact value.
- **This says nothing about whether ED is correct physics.** The whole project measures *structural* behavior — how the architecture is built — not whether it describes the real universe.
- **No claim that ED and the prime-number work are related.** The parallel is purely about *form*: both have a finite-reach boundary you can measure in bits. ED does not explain primes; the prime work does not explain physics. Putting our 0.09 next to their 0.265 is a comparison of *roles*, never of values.

---

## Why we did it so carefully

The whole evaluation rests on not fooling ourselves. The rules and tests were all fixed **before** the number was measured, so the simulator couldn't be quietly tuned to give a flattering answer. When something looked wrong, we diagnosed it instead of patching over it (one "failure" turned out to be the system correctly sitting still at its endpoint, not a real bug). And every limitation above is written into the permanent record, not just mentioned in passing. A measured number is only worth as much as the discipline behind it.

---

## Where everything lives

Everything is in this folder (`evaluations/ED_Substrate/Bits/`) and committed to the repository. The layout:

```
Bits/
  README.md                                 <- this plain-language summary
  ED_Determinability_Boundary_Measurement.md / .pdf   <- the publish-grade paper
  certify.py                                <- run to re-verify the whole thing
  simulator/   the seven-module ED substrate simulator
  analysis/    information-theory tools (entropy, KSG MI, observables, the Δ calc)
  tests/       the 20 automated correctness checks
  examples/    runnable demos: the test case, the measurement driver, the sweeps
  docs/        the full build narrative + results notes (see below)
```

- **`docs/`** — the step-by-step record: `Phase_*.md` (how each piece was built) and `*_Results.md` (what each run produced), from `Phase_SimulatorDesign.md` through `Phase_Delta_Implementation.md` / `Delta_Results.md` (the measurement) and the robustness sweeps (`SizeSweep_Results.md`, `ObservableSweep_Results.md`).

To reproduce the whole result: run `python certify.py` (certifies the simulator), then `python examples/delta_demo.py` (produces the Δ number).

---

## What's left (optional, and bigger)

The natural next step is to find out whether Δ settles to a number that's a genuine property *of ED itself* rather than of our particular test setup — which means systematically varying the size, wiring, and tuning and watching where Δ lands. That's a real research effort, separate from this one. This project's job was narrower and is done: **show that the determinability boundary can be measured in bits, with the controls behaving as the theory requires.** It can, and they do.

---

*The architecture said the boundary exists. The simulator showed it cleanly separates the two sides. The measurement put a positive, stable number of bits on what it blocks. That's the whole story.*
