# #2b · The Relativistic Bridge — Assessment, and Where the Toy-Models Stop

**Foundations assessment — the hardest of the three bridges from SQ1c: does the 1+1D topological net chirality descend to a genuine *relativistic* (3+1D, Lorentz-covariant γ⁵) chiral fermion coupling to gauge fields? Sim: `evaluation/ChiralGauge/chiral_3p1d.py` (one clean check). Honest result: the arrow's *undoubling* generalizes cleanly to 3+1D (16 doublers → 1, computed) — a necessary condition met — but whether the single survivor is a *chiral* Weyl point or a *vector-like* Dirac point is the open relativistic question, and it is genuinely beyond what a toy can settle. This doc states what the bridge requires, gives the structural case both ways, incorporates AP's per-commitment reframing (the more ED-native route, which also unifies with baryogenesis), names the decisive computations, and is candid that #2b has reached the research frontier where the toy-model phase ends.**

**Crank rail.** This is the step where the honest move is to say where my tools stop. The 3+1D undoubling is a clean, real computation; the chiral-vs-vector-like survivor and the gauge/anomaly structure are *not* settleable by the toy models used so far, and I will not manufacture a verdict on them. The structural case is laid out as a case, not a result.

---

## 1. What the relativistic bridge requires

The toy results (SQ1c/SQ1d) established, in 1+1D: the arrow's retarded transport carries a net chirality that is topological (quantized ±1), robust to sparse commitment, and plausibly maximal. The bridge to the Standard Model requires three things the 1+1D toy does not supply:

1. **Dimension.** The same net chirality in 3+1D, where chirality is the Lorentz-covariant γ⁵ Weyl structure (not just 1D left/right directionality).
2. **Gauge coupling.** The chiral fermion must couple *chirally* to a gauge field (left-handed in a doublet, right-handed not) — a chiral *gauge* theory, not just a chiral fermion.
3. **Anomaly cancellation.** The chiral anomalies must cancel across species, as they do (delicately) in the SM. (SQ3, untouched.)

## 2. The one clean check: undoubling survives to 3+1D

Counting massless gap-closings over the 4D Brillouin zone:

| operator | zeros over the 4D BZ |
|---|---|
| naive hermitian (`sin p_μ`) | **16** (= 2⁴ doublers — the full N–N doubler army) |
| retarded forward-difference (the arrow) | **1** (at the origin) |

The arrow's free Wilson term lifts all 15 extra doublers in 3+1D exactly as it lifted the one in 1+1D. **So the undoubling — "no mirror army" — generalizes cleanly to 3+1D.** That is a genuine necessary condition for a chiral theory (you cannot have a single chiral fermion if you are forced to carry doublers), and it is met.

**But necessary is not sufficient.** Undoubling to a *single* fermion is also exactly what Wilson fermions do — and Wilson fermions are *vector-like* (one Dirac fermion, both chiralities). So "1 survivor" is consistent with *either* a chiral Weyl point *or* a vector-like Dirac point. The count does not distinguish them. That distinction — the actual content of the bridge — is what the toy cannot settle.

## 3. The hard part, stated honestly: chiral or vector-like survivor?

In 1+1D the net chirality was clean because there, chirality *is* directionality, and the point-gap winding *is* the chiral anomaly — they coincide. **That coincidence is special to 1+1D.** In 3+1D:

- Chirality is the γ⁵ Weyl index; the net-chirality imbalance is the 3+1D chiral anomaly (∝ the topological density `F∧F`).
- The non-hermitian topological invariant in 3D is a *different* object (a 3D point-gap invariant), classified differently from the 1D winding.
- **Whether the 3D non-hermitian invariant connects to the 4D relativistic chiral anomaly the way the 1D winding connected to the 2D anomaly is not automatic, and is genuinely open** — both in ED and in the non-hermitian-topology literature generally.

So the honest status: the 1+1D result is suggestive and the undoubling generalizes, but the *core* claim (the arrow produces a genuine relativistic chiral fermion, not a vector-like one) does **not** follow from the toy and could go either way. There is a real risk the 1+1D chirality was a low-dimensional coincidence and 3+1D defaults to vector-like (the Wilson outcome).

**Structural reasons for cautious optimism** (a case, not a proof): (a) `γ⁵ = iγ⁰γ¹γ²γ³` is built from the *timelike* `γ⁰`, and the arrow is precisely a preferred time-orientation — so there is a structural channel by which the arrow could orient the chiral structure; (b) the SQ1d result that the chirality is *topological* is encouraging, since topological quantities tend to be dimension-robust. **Structural reasons for caution:** (a) the dimension-special coincidence above; (b) the non-hermitian→unitary leap (the chirality is produced by non-unitarity; a unitary relativistic chiral fermion must survive the sparse-commitment emergent limit — favorably indicated in SQ1d but not crossed); (c) Wilson-undoubling's default *is* vector-like.

## 4. AP's reframing — the more ED-native route (and a unification)

AP's framing sharpens the whole approach: **handedness is a property *of* a commitment** — each committed fact is a handed act — so net chirality is intrinsically a *count* of handed commitments, not a property to be extracted from continuum transport. This is the ontological reason the SQ1d result was topological (a count is quantized), and it suggests a *different* and possibly cleaner route to the relativistic bridge:

> Don't (only) ask whether the coarse-grained transport gives a chiral Dirac operator. Ask: **what handedness does a single commitment carry, and do they align?** The continuum chiral fermion would then be the coarse-grained description of *handed commitment events*, with the net chirality = the aligned count.

This route has two attractions. First, it is faithful to the ontology (chirality lives where the physics lives — in commitment). Second, **it unifies with the baryogenesis arc**: ED's baryogenesis already needs a "first-arrival" lock-in that picks one global chirality (the matter/antimatter selection). If the weak force's parity violation and the matter/antimatter asymmetry are *both* the alignment of handed commitments, they are **one phenomenon, not two** — a single handed-commitment lock-in giving both. That is a genuine, motivated unification hypothesis worth pursuing, and it sidesteps the "does the transport coarse-grain chirally" worry by locating the handedness in the commitment events directly.

## 5. The decisive computations (named, not done)

The bridge will be settled — for or against — by one of:

1. **The open T4 substrate-V1 → Dirac coarse-graining, with net chirality as the explicit target.** Push the derivation T4 §3.7 left open, and read off whether the continuum survivor is chiral (γ⁵ imbalance) or vector-like. This is *the* computation; it is research-grade and needs the real coarse-graining, not a toy.
2. **A 3+1D non-hermitian index / chiral-anomaly computation** — does the arrow's 3D point-gap topology yield a nonzero 4D chiral anomaly? Connects ED to a live question in non-hermitian topology.
3. **The per-commitment-handedness + first-arrival-alignment construction** (AP's route) — build the chirality from handed commitment events and their lock-in, unifying with baryogenesis. The most ED-native, and the one that reuses existing machinery (the baryogenesis chirality memos).

## 6. Verdict — the research frontier

**#2b has reached the point where the toy-model phase ends and genuine research begins.** The honest state after five steps:
- **SQ1:** Nielsen–Ninomiya does not bind ED (no Brillouin torus, non-hermitian arrow). — *settled.*
- **SQ1c:** the arrow carries a net chirality (correcting SQ1b's vector-like misread). — *toy-settled.*
- **SQ1d:** that chirality is topological, survives sparse commitment, is plausibly maximal. — *toy-settled.*
- **SQ1e (here):** the undoubling survives to 3+1D (16→1), but whether the survivor is chiral or vector-like — the relativistic core — is **open and not toy-settleable.**

The structural case is coherent and promising: the arrow is a candidate source of *maximal* chirality, with a clean undoubling in 3+1D and a favorable sparsity story. But crossing to a genuine relativistic chiral *gauge* theory with anomaly cancellation needs the real substrate→Dirac derivation (and likely the per-commitment/baryogenesis-unified route), and there is a real risk the 3+1D survivor defaults vector-like. **That is the honest edge: a promising, internally-coherent case at the structural/1+1D level, with the relativistic realization as the genuine open problem — exactly where #2b should be left until the open T4 coarse-graining (or the per-commitment construction) is done.** Toy-models took it as far as they honestly can.

---

*Relativistic bridge for #2b (`chiral_3p1d.py`). Clean check: the arrow's undoubling survives to 3+1D (16 doublers → 1, computed) — necessary, met. NOT sufficient: 1 survivor is consistent with BOTH a chiral Weyl point and a vector-like Dirac point (Wilson's default is vector-like); the count can't distinguish them. The 1+1D point-gap-winding = chiral-anomaly coincidence is dimension-special; 3+1D needs the 4D chiral anomaly, and whether the 3D non-hermitian invariant connects to it is genuinely open. Structural case both ways: optimism (γ⁵ built from timelike γ⁰ = the arrow's orientation; topological → dimension-robust); caution (dimension-special coincidence; non-hermitian→unitary leap; Wilson default vector-like). AP's reframing — handedness is per-commitment (a count, hence topological) — gives the more ED-native route: build chirality from handed commitment EVENTS and their first-arrival alignment, UNIFYING with baryogenesis (parity violation + matter/antimatter asymmetry possibly ONE handed-commitment lock-in). Decisive computations (named, not done): the open T4 substrate→Dirac chain with chirality target; a 3+1D non-hermitian index/anomaly; the per-commitment+first-arrival construction. Verdict: #2b reached the research frontier — coherent/promising at the 1+1D/structural level, undoubling confirmed in 3+1D, but the chiral-vs-vector-like relativistic core is open and needs the real derivation, not toys. Crank-rail: undoubling computed/solid; chiral survivor explicitly NOT claimed; the frontier named honestly. No relativistic coupling built, no anomaly computed, no number faked.*
