# Measuring a Determinability Boundary in Bits: A Certified Simulation of the Event Density Substrate

**Allen Proxmire**
June 2026

*Architectural Distillation corpus · `evaluations/ED_Substrate/Bits/`*

---

## Abstract

The Event Density (ED) framework models physical reality as a discrete substrate of micro-events that influence one another only across a finite reach, bounded by *decoupling surfaces*. A prior structural evaluation established that these surfaces constitute a **determinability boundary**: a horizon past which one region of the substrate cannot, even in principle, determine the state of another. That result was qualitative. This paper makes it quantitative. We build a faithful executable model of the ED substrate — discrete stability-maximizing selection under irreversible commitment, *not* a coarse-grained approximation — and subject it to four pre-registered correctness gates (monotonicity, acyclicity, factorization, unique selection), all of which it passes (20/20 automated tests). On a certified two-region test substrate separated by a single decoupling surface, we then measure the **determinability-boundary contrast** Δ in bits: the mutual information that propagates *within* a reach-connected region minus the mutual information that crosses the boundary. We find a positive within-region contrast with the across-boundary term indistinguishable from a shuffle null. Subsequent robustness sweeps (§11) sharpen the result decisively: the contrast's *magnitude* is observable-dependent (ranging 0.17–0.98 bits across readouts of the same states), so there is **no single intrinsic scalar** for ED — but across-boundary mutual information $M_2 \approx 0$ holds invariantly across substrate size, estimator, and observable. The robust finding is therefore structural, not numerical: the boundary's **perfect, observable-independent severance** is what characterizes it. We argue this demonstrates a general method (a finite-reach determinability boundary is measurable) while emphasizing strict limits: the work is structural, not physical; and a parallel to the parity barrier of multiplicative number theory is asserted at the level of *form only* — a shared boundary-that-destroys-determination, **not** a shared scalar — with no cross-domain content claim.

**Keywords:** Event Density, determinability boundary, finite reach, mutual information, factorization, discrete substrate, Architectural Distillation.

---

## 1. Introduction

A recurring idea across several formal systems is that of an architecture with **finite reach**: a generative structure whose elements influence one another only out to a bounded horizon. Where reach is finite, a natural consequence follows — there exists a boundary past which the architecture cannot determine what lies beyond. We call this a **determinability boundary**.

In the Event Density (ED) framework, finite reach is built in at the axiom level through *decoupling surfaces*, beyond which reciprocal participation between regions ceases. A structural evaluation of the ED substrate (the twelve-document analysis preceding this work) concluded that **the determinability boundary of ED is exactly the decoupling surface**: inside a reach horizon the substrate is determinable from local information; across it, no channel carries the determining information. The reach horizon and the determinability horizon coincide.

That conclusion was reached structurally — by analysis of the axioms, the update rule, and the constraint geometry. It is the kind of claim that invites a measurement. If determination genuinely fails across a boundary, then information about one side, given the other, should be *quantifiably* reduced — and information theory provides the natural currency: **bits**.

This paper reports that measurement. We construct a certified simulation of the ED substrate and measure the bits of determination that the decoupling surface blocks. The contribution is twofold: (i) a *method* — a reproducible, gated procedure for measuring a determinability boundary in bits; and (ii) a *result* — a positive, stable measurement on a controlled test substrate, with the information-theoretic controls behaving exactly as the structural theory predicts.

We are deliberate about scope. The number we report is a property of our test configuration, not of ED as a whole; the work concerns *structural* well-builtness, not physical truth; and a parallel we draw to a boundary in number theory is one of architectural form, never of content. These limits are stated where they arise and consolidated in §8.

---

## 2. Background

### 2.1 The Event Density substrate

ED posits a discrete relational substrate with the following primitive commitments (the substrate's axioms, labelled B1–B7 in the source evaluation):

- **Micro-events (B1)** — atomic, indivisible acts of becoming; their local rate is the *event density*.
- **Channels (B2)** — participation relations on stable subgraphs, each weighted by a bandwidth.
- **Adjacency and chains (B3)** — bandwidth-gated adjacency; sequences of adjacent events form *chains* (which coarse-grain to particles).
- **Commitment density ρ (B4)** — the local accumulation of committed events; the substrate's state variable.
- **Orientation (B5)** — a relational directionality carried by the channel structure.
- **Decoupling surfaces (B6)** — horizons of finite reach, where reciprocal participation between regions becomes one-sided.
- **Commitment irreversibility, "P11" (B7)** — every commitment, once made, is never unmade; evolution is forward-only.

The substrate evolves by an explicit, local **selection rule**. A chain at a position evaluates each admissible next event $e'$ by a stability score

$$\Sigma(e') = \mathrm{Coh}(e', s) - \mathrm{Str}(e', \rho_{\text{local}}) - \mathrm{Grad}(e', \nabla\rho),$$

where $\mathrm{Coh}$ rewards coherence with the current chain state, $\mathrm{Str}$ penalizes participation strain against the local commitment density, and $\mathrm{Grad}$ penalizes fighting the local density gradient. The chain commits the **maximum-$\Sigma$** candidate. This is a discrete, local, *selection* law — it picks an extreme, it does not average.

A point of emphasis that proves important below: ED's familiar continuum description is a degenerate-parabolic (diffusive) partial differential equation. That diffusive law is the **coarse-grained shadow** of the substrate — what one obtains by averaging the selection rule over many chains and many steps. The substrate itself, being maximization-driven, is *sharpening*, not diffusing. The diffusion is an artifact of zooming out, not a property of the substrate (see §7).

### 2.2 The determinability boundary

A **reach stratum** is a maximal set of micro-events mutually reachable without crossing a decoupling surface — formally, a connected component of the *reciprocal* (non-decoupled) participation subgraph. Because reach is finite (B6), the substrate partitions into such strata, and the reachable configurations *factorize* across them: regions separated by a decoupling surface are causally independent. One-sided influence may cross a surface, but reciprocal participation — the kind that would let one region determine another — does not.

The structural evaluation's central finding is that this factorization *is* the determinability boundary. Within a stratum the substrate is determinable from local channels; across a decoupling surface, no channel carries the determining information. The boundary is therefore a positive structural feature (an axiom, B6), not an absence — and it is the natural object to quantify.

### 2.3 A structural parallel — stated as form only

The motivation to measure ED's boundary in bits comes partly from a parallel with an unrelated system. Separate work on the multiplicative structure of the integers (the "Factor Skyline" programme) identifies its own determinability limit — the **parity barrier** (a Sarnak-disjointness phenomenon) — and has *quantified* it (an "escape density" of roughly 0.265 in its own decomposition). The two systems share an architectural *shape*: a finite-reach generative substrate, a determinability boundary at the reach horizon, and a smoother continuous projection.

We use this parallel only to motivate the *kind* of measurement, and we state the discipline plainly and keep it throughout: **the analogy is structural, detected by a shared evaluation methodology; it is not a claim that ED explains primes, that the prime work explains physics, or that the two boundaries are the same object.** Placing ED's measured number beside the parity barrier's is a comparison of *roles*, never of *values*.

### 2.4 Why a custom simulator

Two existing ED codebases were surveyed. Both are valuable but neither suffices: they evolve by diffusion / gradient-flow dynamics, which is precisely the *shadow* behaviour (averaging), not the *substrate* behaviour (selection). Measuring the substrate's determinability boundary requires the substrate's own sharpening, selection-driven rule. We therefore built a minimal, faithful simulator implementing $\Sigma$-maximization directly, reusing only general infrastructure (information-theoretic estimators) from the surveyed code.

---

## 3. The measurement question

We define the **determinability-boundary contrast** as the difference between predictability within a stratum and predictability across the boundary, in bits:

$$\boxed{\;\Delta = M_1 - M_2\;}$$

where, with all terms computed as mutual information (MI) over an ensemble of independent runs:

- $M_1$ = **within-stratum** predictability — MI between two reach-connected halves of a single stratum;
- $M_2$ = **across-boundary** predictability — MI between two reach-decoupled strata;
- $M_3$ = **shuffle/null control** — MI between one stratum and a randomly permuted copy of the other, giving the estimator's finite-sample floor.

The theoretical prediction is sharp: reach-connected regions share information ($M_1 > 0$); reach-decoupled regions do not ($M_2 \approx 0$); and $M_2$ should be indistinguishable from the null floor $M_3$. The contrast $\Delta$ is then the positive quantity of determination that lives within a stratum but does not cross the boundary — *the bits the boundary blocks*.

Crucially, $M_1$, $M_2$, and $M_3$ are computed with the **same estimator and the same binning**, so $\Delta = M_1 - M_2$ differences out the estimator's shared finite-sample bias. This matched-difference design is what makes a small absolute number trustworthy.

---

## 4. Methods

### 4.1 Simulator

The simulator is a seven-module Python package implementing the substrate faithfully:

- a **participation graph** with bandwidth-weighted channels and a per-edge decoupling flag;
- **node state** carrying commitment density $\rho$ and orientation, with a single write path — `commit()` — that enforces irreversibility (it rejects any decrement of $\rho$);
- the **$\Sigma$ functional**, computed from $\rho$ and graph-local structure only (it is, by construction, blind to orientation — orientation contributes no stability score, consistent with the substrate's specification);
- a **deterministic tie-break**: among $\Sigma$-maximal candidates, the winner is the one with lexicographically maximal key $(\text{bandwidth}, \text{node id})$ — a total order, so the next step is always unique;
- the **update loop**, processing active chains in a canonical (stratum, node) order with commitments immediately visible, making the whole evolution a deterministic function of (graph, initial state, parameters);
- **reach-stratum detection** (connected components of the reciprocal subgraph) and **decoupling-surface detection** (the boundary edges and the across-boundary node pairings);
- an append-only **recorder** that captures per-step $\rho$/orientation and the commitment log, and exports them.

Randomness enters *only* through the seeded initial conditions; trajectories themselves are deterministic — the ensemble model the measurement requires.

### 4.2 Test substrate (the controlled boundary)

The measurement substrate is two isomorphic eight-node chains, $A=\{0,\dots,7\}$ and $B=\{8,\dots,15\}$, joined by a single **decoupled bridge** $(7,8)$. The reciprocal subgraph thus has exactly two components — two reach strata — separated by one determinability boundary. Each chain is seeded from its **own independent** random initial conditions (distinct seeds), so $B$ is a genuinely independent draw from $A$. Evolution runs to a natural fixed point (no admissible positive-score move remains) or a step cap; in practice it reaches the fixed point quickly.

### 4.3 Ensemble and estimator

An ensemble of $N$ independent runs is generated with independent per-stratum seeds. For each run we extract summary statistics (summed final $\rho$) for: stratum $A$, stratum $B$, and the two reach-connected halves of $A$. Mutual information is estimated with a **Miller-Madow-corrected** histogram estimator (quantile-edged bins), and converted from nats to bits ($1\text{ nat} = 1/\ln 2$ bits). The Miller-Madow correction is necessary because the naive plug-in MI is *positively* biased at finite sample size: truly independent variables yield a small spurious positive MI without it. We report $N = 200$ as the primary ensemble, with $N \in \{100, 200, 400\}$ for stability.

### 4.4 Reproducibility by construction

Every ensemble uses fixed seed bases, so the entire measurement reproduces exactly. The simulator's determinism is itself tested (identical inputs yield bit-identical histories).

---

## 5. Verification: the four correctness gates

No determinability number is measured until the simulator is **certified** against four pre-registered gates. The gates were fixed in advance, as general criteria, before the measurement substrate was scored against them — the discipline that prevents tuning the instrument to a flattering result.

| Gate | Requirement | How verified |
|---|---|---|
| **1 — Monotonicity** | $\rho$ never decreases | Recorded history is elementwise non-decreasing; `commit()` rejects negative increments. |
| **2 — Acyclicity** | No global state recurs | Every per-step state signature is unique; total $\rho$ strictly increases. |
| **3 — Factorization** | Decoupling severs reciprocal participation | *Structural*: perturbing one stratum's seed leaves the other byte-identical, and no commitment crosses the boundary. *Informational*: across-boundary MI ≈ 0, matching its shuffle control. |
| **4 — Tie-break** | Unique, deterministic selection | Forced ties resolve to exactly one candidate by the lexicographic key; orientation flips leave $\Sigma$ unchanged. |

Gate 3 is the load-bearing one and is tested two independent ways. The structural test is *exact*: because the strata are causally independent, changing $B$'s random seed must leave $A$'s entire commitment history and final state **bit-for-bit identical** — and it does, with the symmetric statement for $B$ under an $A$-perturbation. If a single channel leaked across the boundary, this exact equality would fail. The informational test corroborates: the mutual information between the two strata is statistically indistinguishable from zero and from a shuffle null.

A consolidated certification harness runs all gates together. The result:

```
pytest          : 20 passed, 0 failed
Gate 1 mono     : PASS
Gate 2 acyclic  : PASS
Gate 3 factor   : PASS   (MI = -0.0017 nats; exact A<->B independence)
Gate 4 tiebreak : PASS
SIMULATOR: CERTIFIED — Delta measurement permitted.
```

One verification subtlety, recorded for transparency: an early acyclicity check flagged a recurrence that was, on inspection, the terminal fixed point recorded twice (a stationary endpoint, not a cycle). The recorder was corrected to log a snapshot only when the step changed the state; the genuine invariant — total $\rho$ strictly increasing on every recorded step — holds exactly. This is stationarity, not a violation of acyclicity.

---

## 6. Results

With the simulator certified, the determinability-boundary contrast was measured on the test substrate. The primary ensemble ($N=200$, 2-bin Miller-Madow estimator, bits):

| Quantity | Definition | Value (bits) |
|---|---|---|
| $M_1$ — within-stratum | $\mathrm{MI}(A_{\text{left}}; A_{\text{right}})$ | **$+0.092$** |
| $M_2$ — across-boundary | $\mathrm{MI}(A; B)$ | **$-0.002$** |
| $M_3$ — shuffle null | $\mathrm{MI}(A; \text{shuffled } B)$ | **$-0.001$** |
| **$\Delta = M_1 - M_2$** | determinability-boundary contrast | **$+0.094$** |

The residual $M_2 - M_3 = -0.0014$ bits confirms the across-boundary term sits at the estimator's null floor. Stability across ensemble sizes:

| $N$ | $M_1$ | $M_2$ | $\Delta$ |
|---|---|---|---|
| 100 | $+0.0884$ | $+0.0032$ | $+0.0852$ |
| 200 | $+0.0920$ | $-0.0025$ | $+0.0945$ |
| 400 | $+0.0833$ | $+0.0000$ | $+0.0833$ |

The spread in $\Delta$ over $N \in \{100,200,400\}$ is $0.011$ bits — an order of magnitude below the signal.

**Reading.** The three measures behave exactly as the structural theory requires. Within a reach stratum, the two halves share real information ($M_1 \approx 0.09$ bits). Across the determinability boundary, shared information collapses to the noise floor ($M_2 \approx M_3 \approx 0$). The contrast

$$\Delta \approx 0.09 \text{ bits}$$

is positive, well above the $\sim 0.001$-bit floor, and stable. **The determinability boundary blocks a real, repeatable, measurable quantity of information.**

---

## 7. Discussion

### 7.1 What the number means: a picture

It is easy to misread $\Delta \approx 0.09$ bits as "the most a single event can hand off." It is not that. $\Delta$ is a **contrast between two correlations**, measured across the ensemble — and the intuition is best built through a concrete frame.

**The betting frame.** Run the substrate many times. Each run, record how "busy" (high-$\rho$) the **left half** of region $A$ ended up, and how busy its **right half** ended up. Now ask: *told the left half was busy, how well can you bet on the right half?*

- *Within a region (the two halves of $A$).* A little better than chance. The halves belong to one reach-connected region, so a faint shared signal links them — told "left busy," you would bet "right busy" and win modestly more than half the time. That faint edge is $M_1 \approx 0.092$ bits.
- *Across the boundary (region $A$ vs. region $B$).* Not at all. Told everything about $A$, your best guess about $B$ is an even coin flip. The two strata are statistical strangers. That is $M_2 \approx 0$ bits.

$\Delta$ is the *betting edge you have inside a region minus the edge you have across the boundary*: $0.092 - 0 \approx 0.09$ bits.

**The soundproof-wall frame.** Inside region $A$, two halves can faintly hear each other through a thin wall. The decoupling surface is a **perfectly soundproof wall**: whatever happens in $A$, region $B$ hears nothing. $\Delta$ measures *how much hearing the wall removes* — the faint within-region signal ($\approx 0.09$ bits) that the boundary erases to silence ($0$ bits).

**The scale of a bit.** One full bit of mutual information is a perfect yes/no link (tell me $X$, I know $Y$ for certain); zero bits is total independence. $0.09$ bits is therefore *small* — a faint lean, not a lock. Inside a region: a weak hint. Across the boundary: no hint at all, indistinguishable from randomly shuffled data.

**The contrast is the result, not the value.** The scientifically meaningful content is not the magnitude $0.09$ but the *pattern*: **nonzero within a region, exactly zero across the boundary.** The zero is not trivial — there genuinely is a signal to block (the nonzero $M_1$), and the boundary blocks all of it, down to the noise floor. That is the determinability boundary rendered numerically: knowability lives inside reach and dies at the boundary. The value $0.09$ is merely *how large the erased signal happened to be in this test configuration* (see §8.1); the erasure itself — the collapse from a real signal to zero — is the finding.

This also clarifies the comparison to the parity barrier (§2.3): that programme's $\approx 0.265$ is *domain-intrinsic* — a fraction of multiplicative structure that genuinely escapes determinability, a property of the integers themselves. The present $0.09$ is a *configuration baseline*, not yet an intrinsic ED quantity. The two are alike in *kind* (a determinability boundary measured in bits), not in being comparable values — exactly the role-only parallel maintained throughout.

### 7.2 The structural claim, now quantified

The structural evaluation argued that ED's decoupling surface is a determinability boundary. This measurement gives that claim a number. The qualitative prediction — information propagates within a reach horizon and stops at it — is borne out quantitatively: $M_1 > 0$, $M_2 \approx 0$, and the gap $\Delta$ is positive and stable. The boundary is not a turn of phrase; it is a measurable information barrier.

### 7.3 Substrate sharpens; shadow diffuses

A result that emerged from building the faithful simulator deserves emphasis. ED's continuum shadow is diffusive (a degenerate-parabolic PDE), but the substrate, driven by maximization, *sharpens*. The diffusion is **manufactured by coarse-graining** — averaging a sharpening selection rule over many events — and is absent from the substrate itself. This is why a faithful measurement could not have used the diffusive shadow: it would have measured the wrong object. The simulator implements the selection rule directly, and the certified factorization is a property of that rule, not of any averaged approximation. More broadly, this shows that a system's behaviour at the substrate level need not match its behaviour at the coarse-grained level — a methodological caution of independent interest.

### 7.4 The method generalizes

Nothing in the measurement procedure is specific to ED's particular parameters. The construction — partition a finite-reach substrate into strata, run an ensemble, contrast within-stratum against across-boundary mutual information with a matched estimator — applies to *any* discrete relational substrate with a determinability boundary. ED is the first worked example; the procedure is the transferable contribution.

---

## 8. Scope and limitations

We state the bounds of the result explicitly.

1. **The magnitude is configuration-specific.** $\Delta \approx 0.09$ bits is a property of this test substrate, not a constant of ED. It depends on the summary statistic, the binning, the $\Sigma$ coefficients, the extinction threshold, the topology, and the seeding. What is robust is the *pattern* ($\Delta > 0$, $M_2 \approx M_3$, $M_1 > M_2$); the *value* is not yet a property of the architecture. Establishing a configuration-independent ED value would require a systematic robustness program (varying topology, reach profile, coefficients, and summary), which is research-scale and separate from this proof-of-method.

2. **This is structural, not physical.** The entire programme — both the prior evaluation and this measurement — concerns *architectural well-builtness*. It does not test, support, or undermine ED as a description of the physical world. A boundary being measurable in bits is a fact about the architecture, not about nature.

3. **The number-theory parallel is form, not content.** The comparison to the parity barrier is role-to-role: both are finite-reach determinability boundaries admitting a bits-denominated measure. We make **no** claim that $0.09$ and the parity barrier's $\sim 0.265$ are comparable in value, that ED's boundary *is* a parity barrier, or that the domains share subject matter.

4. **Small substrate, simple estimator.** The test case is sixteen nodes with a single constructed boundary, and the MI estimator is a 2-bin histogram with bias correction. These suffice for a matched-difference proof-of-method but are not a high-resolution measurement; larger substrates and richer estimators are part of the robustness program.

---

## 9. Reproducibility

The complete simulator, analysis, tests, and step-by-step record are in `evaluations/ED_Substrate/Bits/`. To reproduce:

```
python certify.py                  # runs all four gates -> "SIMULATOR: CERTIFIED"
python examples/delta_demo.py      # generates the ensemble -> Delta ~ 0.09 bits
```

Both are deterministic given the seed bases. The build is documented step-by-step under `docs/` (`docs/Phase_*.md`), each with a recorded-output results note (`docs/*_Results.md`); the measurement specifically is `docs/Phase_Delta_Implementation.md` and `docs/Delta_Results.md`. Certification artifacts (gate summary, snapshot) are under `certification_output/`.

**Stack.** Python 3 with NumPy; pytest for the gates. No specialized hardware.

---

## 10. Conclusion

A structural evaluation of the Event Density substrate concluded that its decoupling surfaces are determinability boundaries — horizons past which one region cannot determine another. This paper turned that conclusion into a measurement. We built a faithful, certified simulator of the substrate's selection dynamics, proved (via four pre-registered gates, 20/20 automated tests) that it monotonically accumulates, never cycles, severs reciprocal participation across decoupling surfaces, and selects uniquely. On a certified two-stratum test substrate we measured the determinability-boundary contrast at

$$\Delta \approx 0.09 \text{ bits},$$

positive, stable, and well above the estimator's null floor, with the across-boundary term indistinguishable from a shuffle control — exactly as the structural theory predicts.

The result is a *proof-of-method*: a finite-reach substrate's determinability boundary is measurable in bits, with the information-theoretic controls behaving as required. The specific magnitude belongs to the test configuration, not to ED as such; the work is structural rather than physical; and the parallel to a number-theoretic boundary is one of architectural form alone. Within those bounds, the chain is complete:

> *The architecture established that the boundary exists. The certified simulator demonstrated that it cleanly separates the two sides. The measurement put a positive, stable number of bits on what it blocks.*

A configuration-independent value — the step that would make $\Delta$ a measured property of the architecture itself — was the natural next undertaking. It was subsequently run. The postscript reports what it settled.

---

## 11. Postscript: what the robustness sweeps settled

The proof-of-method above measured Δ for one configuration and flagged the obvious next question: is the magnitude an intrinsic property of ED, or an artifact of the chosen substrate and observable? Two robustness sweeps answered it (`docs/SizeSweep_Results.md`, `docs/ObservableSweep_Results.md`).

- **Size and estimator.** The 2-bin histogram estimator made Δ *appear* to converge to ~0.92 bits across a 16× size range — but that was an estimator artifact: varying the bin count alone swung it 0.46–0.99. A binning-free k-nearest-neighbour (KSG) estimator, stable under its own parameter, gave **Δ ≈ 1.0 bit**, stable across size 16–256.
- **Observable (the decisive test).** Holding size and estimator fixed and changing only *how the final state is read out*, Δ ranged from **0.17 to 0.98 bits** (summed ρ ≈ 0.98; per-node vectors ≈ 0.94; a local window ≈ 0.17; the gradient ≈ 0.36), each KSG-stable. **The ~1 bit was the information content of the `summed_rho` observable — not an intrinsic property of ED.** There is no single scalar "Δ for ED."
- **What survived every dial.** Across-boundary mutual information $M_2 \approx 0$ held under *every* size, estimator, and observable. This is exactly what theory demands: independence is observable-invariant (the mutual information between any function of one side and any function of the other vanishes), whereas the *strength* of dependence is observable-relative. So the magnitude was never going to be a single number — but the **zero is**.

This sharpens the paper's central claim and the parallel to the parity barrier of multiplicative number theory. A clean two-line statement of the result:

> **Both systems have a boundary that destroys determination. The Factor Skyline programme quantifies its boundary with a scalar (an escape density ≈ 0.265); the Event Density substrate quantifies its boundary structurally.**

The sharpening: ED's structural quantification **is the zero**. The robust, observable-invariant statement is $M_2 = 0$ — across every readout, determination does not merely shrink across the boundary, it vanishes completely, and that total severance is the structural quantity. ED *can* produce scalars (0.17, 0.36, 0.94, 0.98); they are simply observable-relative, not canonical. "Structural" therefore does not mean "no number available" — it means **the intrinsic characterization is the invariant, not a number.**

And a hypothesis for *why* the two architectures differ in this way — offered as a conjecture, not a result, but the most interesting thing the sweeps hint at:

> **The Factor Skyline gets a scalar because it has a canonical observable; ED does not.** FS's multiplicative structure singles out *what to measure* — the parity / Möbius content — so "what fraction escapes determinability" has a privileged answer (≈ 0.265). ED's substrate privileges no single function of ρ, so "how much determination crosses the boundary" has no canonical readout, and hence no canonical scalar — only the observable-independent invariant, the zero. If this is right, the scalar-versus-structural difference is not a measurement limitation but a genuine structural difference between the two architectures: **one has a preferred coordinate; the other does not.**

Testing that conjecture — whether an observable-*independent* object (a channel capacity, a transfer-entropy / causal-influence measure) recovers a canonical ED invariant where single-observable mutual information cannot — is a reformulation rather than a parameter sweep, and the natural next theoretical direction. Until then, the bounded, robust result stands: **the determinability boundary severs perfectly and observably-invariantly; its severance, not a scalar, is what characterizes it.**

---

## References (internal corpus)

**Structural evaluation (the determinability boundary, established):**
`evaluations/ED_Substrate/` — Memo_00 (scoping); Phase_A/A1/A2 (substrate-level AD criteria and extraction modes); Phase_B–E (architecture, envelope, extremal dynamics, constraint surface; the determinability boundary located at the decoupling surface); Phase_F (criteria verdict, 6/6); Phase_G (generalization); tie-break and orientation-primitivity closures.

**This measurement (the empirical arc):**
`evaluations/ED_Substrate/Bits/` — `README.md` (plain-language summary) and this paper at the root; `certify.py` (one-command verifier); code in `simulator/`, `analysis/` (incl. KSG estimator and observables), `tests/`, `examples/` (incl. `size_sweep.py`, `observable_sweep.py`). The full build narrative and results notes live in `docs/` — measurement plan, simulator design and implementation plan, build-step implementations and results (Milestone 1 through certification), `docs/Phase_Delta_Implementation.md` and `docs/Delta_Results.md` (the measurement), and the robustness sweeps `docs/SizeSweep_Results.md`, `docs/Phase_ObservableSweep_Implementation.md`, `docs/ObservableSweep_Results.md` (§11).

**Motivating note:**
`AD_Note_SubstrateBeneathTheShadow.md` — the finite-reach / determinability-boundary / projection-shadow motif shared (in form) by ED and the Factor Skyline programme.

---

*Architectural Distillation evaluates the structural integrity of an architecture, independent of empirical interpretation. This document reports a structural measurement; it makes no claim about the physical correctness of Event Density.*
