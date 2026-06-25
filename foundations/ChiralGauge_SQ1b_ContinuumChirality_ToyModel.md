# #2b · Continuum-Limit Chirality — Toy-Model Computation (SQ1 follow-on)

**Foundations computation — the next step after SQ1: does ED's *retarded* (arrow) transport actually *produce* the net chirality that escaping Nielsen–Ninomiya merely made *possible*? Sim: `evaluation/ChiralGauge/chiral_winding.py`. Honest scope, stated first: the full substrate-V1 → Dirac coarse-graining is OPEN (T4) and ED has no global Brillouin torus, so this does NOT compute a relativistic net chirality. It isolates the one mechanism the SQ1 hypothesis turned on, in 1D toy models, and lets it answer — including no. The result is a partial no to the optimistic reading: the arrow cleanly solves the *doubling* problem but, in the most natural reading, gives a *vector-like* (non-chiral) fermion — undoubling, not handedness. #2b stays genuinely open; the "arrow → chirality" hypothesis is not supported by this computation.**

**Crank rail — maximal, and it bit.** I went in to test whether the arrow produces chirality (SQ2's promising thread). The computation says the simplest mechanism gives the *opposite* of what was hoped (vector-like, not chiral). I report that, not a spin on it. The one chiral-candidate that survives (point-gap winding) is flagged as a distinct invariant whose relativistic descent is unproven — not as a result.

---

## 1. What was computed

Two 1D toy models of discrete fermion transport, comparing **hermitian** (time-symmetric, standard lattice) against **retarded** (one-way, the arrow — ED's V1 is strictly retarded, T18):

- **Part A — point-gap winding.** A scalar hopping `H(k) = tR e^{ik} + tL e^{-ik}` (hermitian iff `tR = tL`). Measure the non-hermitian point-gap winding number of the complex dispersion around `E = 0`.
- **Part B — doubler count.** A 1-component lattice "Dirac" dispersion; count the real-axis gap-closings ("Weyl points" / doublers). Hermitian central difference `d(k) = i·sin k` versus retarded forward difference `d(k) = e^{ik} − 1`.

## 2. Results (run output)

**Part A — point-gap winding around E = 0:**

| hopping | winding |
|---|---|
| hermitian (`tR = tL`) | **0** |
| one-way R (retarded) | **+1** |
| one-way L | **−1** |
| asymmetric (`tR=1, tL=0.3`) | **+1** |

The hermitian spectrum is real (a segment through 0) — winding 0, the doublers must pair. The one-way (arrow-like) hopping traces a circle around E = 0 — **winding ±1, nonzero.** Non-hermitian topology is real and the arrow carries it.

**Part B — lattice-Dirac doublers (real-axis gap closings):**

| difference | real-axis zeros | reading |
|---|---|---|
| central (hermitian) | `k = 0, π` (**2**) | the Nielsen–Ninomiya **doubler** |
| forward (retarded) | `k = 0` (**1**) | the π-doubler **lifted off the real axis** |

And the decomposition: **`forward = central + (cos k − 1)`**, with the extra term `= −2` at `k = π`. That extra term is exactly a **Wilson term** — the momentum-dependent mass lattice QCD *adds by hand* to kill doublers. **ED's retarded transport contains it for free.**

## 3. What this means — the two faces of the arrow, pulling opposite ways

The arrow does two things to the fermion sector, and for the *chirality* question they point in opposite directions:

**(i) It lifts the doublers (Part B) — a real, clean win, but it points *vector-like*.** The retarded/forward difference is structurally a Wilson fermion: the π-doubler is pushed off the real axis, leaving a single undoubled mode. So ED escapes the "you must have a doubler" half of Nielsen–Ninomiya *for free, via the arrow* — a genuinely nice, grounded result. **But** Wilson-style lifting is the textbook way to get an undoubled fermion *at the cost of explicit chiral-symmetry breaking* — and the generic outcome is a **vector-like (parity-conserving) fermion**, exactly as in lattice QCD. So the most natural reading of Part B is that ED's continuum fermion is *undoubled but vector-like* — i.e. **not chiral.** This is the opposite of what #2b needs.

**(ii) It carries a nonzero point-gap winding (Part A) — the only chiral candidate, and it is unbridged.** The retarded hopping has winding ±1, the non-hermitian topology that *can* host unpaired chiral modes. This is the one feature that could, in principle, give genuine handedness. **But point-gap winding is a *different* topological invariant from the relativistic Weyl/γ⁵ chirality that couples to gauge anomalies.** Whether it descends, under DCGT + Lorentz-covariantization, to a nonzero relativistic chirality index is exactly the open bridge — and nothing here establishes it.

## 4. Verdict

**The toy computation does NOT deliver net chirality, and it shifts the lean.** SQ1 left the front open with the arrow as a "promising candidate mechanism" for chirality. This computation sharpens that to a more sober, more honest reading:

- **What the arrow definitely does:** solve the *doubling* problem. ED's retarded transport is a free Wilson term; the doublers lift. ED genuinely escapes Nielsen–Ninomiya's pairing — at the level of "must there be a mirror doubler," the answer for ED is *no*. That is the rigorous content behind the discreteness reply, now demonstrated, not asserted.
- **What it does NOT do:** produce handedness. The natural (Wilson) reading is *vector-like* — undoubled but parity-conserving. The only chiral candidate (point-gap winding) is a distinct invariant with no established relativistic descent. So **net chirality is not delivered, and the simplest reading even points away from it.**
- **Net:** **#2b is reinforced as a genuine, hard open problem, not closed favorably by the arrow.** The arrow is *necessary-not-sufficient* for the matter sector to work at all (it undoubles), but it does not, by this computation, supply parity violation. The "chirality as the arrow's fourth job" hypothesis is **not supported** here — though not strictly killed: the point-gap route survives as a logical possibility whose relativistic realization is unproven.

This is consistent with the broadest honest fact about the target: a genuinely chiral *gauge* theory is unsolved even where the free-fermion doubling is beaten (lattice QCD with Wilson fermions is vector-like; chiral electroweak-on-the-lattice is open). ED lands in exactly that situation — undoubled, naturally vector-like, with chirality as the unsolved part.

## 5. Honest boundary and next

This is a 1D toy model, not ED's continuum limit, and the decisive quantities are still open:

1. **The relativistic bridge.** Does the non-hermitian point-gap winding (Part A) descend to a relativistic γ⁵ chirality index in the DCGT + Lorentz-covariant continuum limit, or does the Wilson-vector-like reading (Part B) win? This needs the actual substrate-V1 → Dirac coarse-graining (T4 §3.7, OPEN), now with a sharp fork: chiral (point-gap survives) vs vector-like (Wilson dominates). The toy model says the *default* is vector-like; overturning that to chiral requires showing the point-gap topology survives Lorentz-covariantization — currently unproven.
2. **SQ3 — the chiral gauge coupling + anomaly cancellation.** Still the hardest piece and the most plausible site of a real obstruction; untouched here.
3. **An IC-selected route.** If the dynamical mechanism gives vector-like, the SM's parity violation might instead be a *spontaneously broken* / first-arrival selection (as ED's baryogenesis arc already had to invoke for matter/antimatter) rather than a property of the transport. That is a separate, unexplored route worth flagging.

**Candor note.** Two computations into #2b, the honest trajectory is: SQ1 cleared the *impossibility* worry (N–N doesn't bind ED); this step shows the arrow cleanly handles *doubling* but, in the natural reading, gives *vector-like* fermions — so the *production* of chirality remains unsolved and, if anything, looks harder than the SQ2 hypothesis hoped. The gap is real, mapped, and open, with the relativistic bridge (point-gap → γ⁵) as the one computation that could still swing it chiral.

---

*Toy-model computation for #2b continuum chirality (`chiral_winding.py`). Part A: scalar point-gap winding — hermitian 0, one-way/retarded ±1 (non-hermitian topology nonzero, arrow carries it). Part B: lattice-Dirac doublers — central/hermitian 2 (the N–N doubler at k=0,π), forward/retarded 1 (π-doubler lifted); and forward = central + (cos k−1) = a free WILSON term (−2 at k=π). Reading: the arrow does two things pulling opposite ways for chirality — (i) lifts doublers (escapes N–N pairing, clean win) but Wilson-style => generically VECTOR-LIKE (non-chiral); (ii) carries point-gap winding ±1 (the only chiral candidate, but a distinct invariant whose relativistic γ⁵ descent is UNPROVEN). Verdict: net chirality NOT delivered; simplest (Wilson) reading is vector-like; #2b reinforced as a genuine hard open problem; "arrow → chirality" hypothesis NOT supported (not strictly killed — point-gap route survives logically). Arrow = necessary-not-sufficient: it undoubles, it doesn't (here) hand-pick handedness. Next: the relativistic bridge (point-gap → γ⁵ index via the open T4 coarse-graining; default is vector-like, overturning it needs the point-gap topology to survive Lorentz-covariantization); SQ3 anomalies; an IC-selected/spontaneous parity-breaking route. Crank-rail bit: I tested the arrow→chirality hypothesis and it came back a partial no. No primitive added, no chiral coupling constructed, no number faked.*
