# The Chiral-Gauge / Parity Gap — Scoping and Wall-Determination (#2b)

**Foundations scoping doc — NOT a result. The frontier doc's #2b ("chiral gauge structure / Standard-Model matter sector") was flagged as the sharpest unmet challenge to ED's discreteness commitment, with wall-status *undetermined*. This doc scopes it: states the problem precisely, grounds it in what ED actually has, decomposes the wall question into tractable sub-questions, gives a provisional wall verdict, and names the concrete first move (analysis, not a lattice run). No chiral coupling is derived or faked here; this determines which wall it is and where to push.**

---

## 0. The honest framing

The question is whether a parity-*symmetric* discrete relational substrate can produce the parity-*violating* chiral gauge structure of the Standard Model. Three outcomes are possible, and the point of scoping is to find which:

- **Wall 1 (emergence / admissible-extension-away):** attainable in principle — the chirality is inherited or emerges, like the matter/antimatter asymmetry, possibly needing a substrate-graph structure ED doesn't yet have but which is *latent* in the primitives (the way GR needed the dynamical-bandwidth rule on P04).
- **Wall 2 (provably unreachable, like primes):** a theorem forbids it — a parity-symmetric discrete substrate *cannot* carry chiral gauge couplings. Nielsen–Ninomiya is the candidate.
- **Undetermined-and-foreign:** attainable only by adding a new primitive that ED's parsimony can't absorb (ED would have to *import* handedness, not derive it).

The provisional verdict below is **Wall 1**, but the first move is precisely the analysis that could overturn it to Wall 2.

---

## 1. The problem, precisely

The Standard Model is a **chiral gauge theory**. The weak interaction couples *only to left-handed* fermions (and right-handed antifermions): the left-handed fields sit in SU(2) doublets, the right-handed ones in singlets, so the two handednesses couple **differently to the gauge field**. Parity is maximally violated. Crucially, this asymmetry is **structural** — it is built into the gauge coupling itself, *before* any symmetry breaking. (The Higgs breaks electroweak symmetry and gives mass; it does not create the chirality of the coupling, which is already there.)

So the gap is not "does ED have spin-½ fermions" (it does) and not "does ED have gauge fields" (it has a gauge *sector*). The gap is: **can ED produce a gauge coupling that distinguishes left from right — a parity-violating coupling — from a substrate whose primitives are parity-symmetric?**

This is the physics behind the Nielsen–Ninomiya objection (verified 2026-06-23: N–N forbids chiral fermions on a regular lattice; the public "the universe can't be discrete" argument rests on it).

## 2. What ED actually has (grounded)

| Ingredient | Status in ED | Source |
|---|---|---|
| **Spin-½ / Cl(3,1) spinor structure** | Present. Four-component spinors, the full Clifford algebra, hence a `γ⁵` and left/right projectors *exist at the representation level* | RQM-T2 (Cl(3,1) frame uniqueness, M1); RQM-T4 (Dirac, M2) |
| **The Dirac operator** | Form FORM-FORCED as the KG factorization on Cl(3,1); but the substrate-V1 → Dirac closed proof is **OPEN**, and chirality is *imported* from standard machinery, not derived | RQM-T4 §3.7, audit row 15 |
| **Gauge sector** | A "rule-type bundle" (T17) — explicitly a *rewrite* of fiber-bundle vocabulary, not a derivation; U(1) primitive (P09); non-abelian is "by analogy" (P10); SM group not derived | T17 §2.5 |
| **Polarity (P09)** | `U(1)`-valued phase — **parity-symmetric** (a phase has no handedness) | Paper_087 P09 |
| **A fundamental orientation** | YES — the arrow (P11), and the **strictly retarded** V1 kernel (advanced V1 *refuted* by P11, T18). The participation graph edges are *directed* | Paper_089 T18; substrate def. |
| **A chirality binary (ℤ₂)** | **Does NOT exist natively.** The baryogenesis arc tried three reductions (alignment-sign, edge-parity, S¹→ℤ₂ collapse) — *all failed*. No chain-typing ℤ₂ in the corpus | `Memo_ED_BinaryChirality` §6 |

**The decisive structural fact, and its irony.** ED has *an orientation* — the arrow — but not yet *a handedness*. The retarded-only V1 means every chain propagates one way along the kernel-arrow; there is no "anti-aligned" class (that is exactly why the alignment-sign chirality, R1, collapsed to a *monary*, not a binary). So the arrow gives ED a universal time-orientation, and the Cl(3,1) structure gives it the *room* for left/right projectors — but nothing currently couples the gauge sector *asymmetrically* to those projectors. The substrate is oriented in time and ambidextrous in space.

## 3. The wall question, decomposed

**SQ1 — Does Nielsen–Ninomiya actually bind ED? (the Wall-2 test; analysis-tractable, the first move.)**
N–N's premises are: a *regular, translation-invariant lattice*; *locality* on it; *hermiticity*; a conserved chiral charge. ED meets *none* cleanly:
- **Not a lattice.** The substrate is a dynamic relational participation graph, not a translation-invariant grid (P03 is homogeneity of the graph, not a fixed lattice). The doubling theorem is proved for periodic momentum-space; ED has no global Brillouin zone.
- **Not hermitian.** ED's propagation is *retarded* (T18: advanced V1 refuted) — one-way in time, the arrow. A retarded discrete Dirac operator is **not** the hermitian operator N–N assumes. *This is the sharpest ED-native angle: the very feature that defines ED (the arrow) is a premise N–N requires you not to have.*

So the **literal** theorem most likely does **not** bind ED. But "premises don't apply" is necessary, not sufficient (the chiral anomaly is real in the continuum too). SQ1's real job: write ED's discrete Dirac operator explicitly (from T4 + the V1 kernel), check each N–N premise against it, and ask whether a *more general* obstruction (graph-fermion-doubling, or an anomaly-matching argument that survives non-hermiticity) applies. **This is doable as analysis and is the first move (§5).**

**SQ2 — Can ED's time-orientation induce a *spatial* chirality? (the Wall-1 mechanism; the deepest, most ED-coherent question.)**
ED has a time-arrow; the SM needs a spatial handedness. These are not the same — and the link is exactly what must be shown, not assumed. But there is a genuine structural thread worth chasing:
- Chirality is defined by `γ⁵ = iγ⁰γ¹γ²γ³` — which *includes the timelike* `γ⁰`. So the left/right split is built using the time direction.
- ED has a **preferred time direction** — the foliation the arrow forces (the same one that makes ED's gravity *khronometric* and gave the khronon). 
- **Hypothesis:** the preferred foliation that ED already carries (for gravity) is the structure that picks a consistent `γ⁰`, and the question is whether coupling the gauge sector (P05 polarity-transport along *directed* edges) through that foliation-aligned Clifford structure induces a parity-asymmetric coupling. If so, the *same arrow* that buys the khronon and α₁-safety would buy chirality — a third appearance of the one idea.
- **Honest caveat:** this is *not* a CPT argument. T-violation (the arrow) and P-violation (the weak force) are distinct; CPT links them only in combination, and ED's relation to CPT is itself unestablished. So SQ2 is a promising hypothesis, not a sketch of a proof — and the baryogenesis memo's failure (the arrow gives a monary, not a binary) is the warning that the arrow *alone* is not enough: it must be split into a binary by the Clifford/foliation structure or by an IC-selected breaking.

**SQ3 — The anomaly structure (the hardest piece; likely the real obstruction-or-not).**
Even granting chiral couplings, the SM's chiral anomalies must cancel (the delicate quark/lepton cancellation per generation). Whether a relational-graph substrate reproduces that cancellation is the deepest test and almost certainly beyond first-pass scoping. Flag and defer — but note it is *here*, not at the lattice, that a genuine Wall-2-style obstruction (if any) most plausibly lives.

## 4. Provisional wall verdict

**Most likely Wall 1 (emergence / admissible-extension-away), not Wall 2 — but genuinely open.**
- **Against Wall 2:** N–N's premises (lattice, hermiticity) don't bind ED (SQ1), so there is no *known* proof of impossibility. ED also already has the rep-level chiral structure (Cl(3,1)) and a fundamental orientation (the arrow) to build from.
- **Against "already Wall-1-attained":** the current primitives demonstrably do *not* produce a chiral coupling — the baryogenesis arc proved no native chirality binary exists (three failed reductions). So this is not derivable as-is.
- **The live possibility:** chirality is *extension-away* — a substrate-graph structure (a chain-typing ℤ₂, or the foliation-aligned Clifford coupling of SQ2, or an IC-selected spontaneous handedness like baryogenesis's "first-arrival") supplies the parity asymmetry. The decisive sub-question is whether such a structure is **admissible** (latent in the primitives, like the P04 dynamical rule was for GR) or **foreign** (a new primitive — ED would be *importing* handedness, a parsimony cost and a partial concession to the discreteness critics).

## 5. The concrete first move (turnkey, analysis — no lattice run)

**Execute SQ1: the Nielsen–Ninomiya binding analysis.** Deliverable = a determination of whether any fermion-doubling / chiral-obstruction theorem binds ED's actual discrete Dirac structure. Steps:

1. **Write ED's discrete Dirac operator explicitly** from RQM-T4 + the V1 retarded kernel (Paper_089): the spinor amplitude on the participation graph, the gamma-matrix inter-component coupling (T4 §3.7), and the *retarded* propagation that replaces the hermitian lattice hopping. State it as an operator and identify its symmetry properties.
2. **Check each N–N premise against it:** translation-invariance (no — relational graph), locality (bounded V1 width — yes-ish), hermiticity (**no** — retarded/arrow), chiral-charge conservation. Mark which premises ED violates and which it meets.
3. **Test for a more general obstruction:** does a graph-theoretic or non-hermitian generalization of the doubling theorem exist that would still bind ED? (Literature: fermion doubling on random/causal lattices; non-hermitian/Lindblad chiral systems; the role of the index theorem.) If the obstruction is purely a hermitian-lattice artifact, ED escapes; if it survives non-hermiticity, ED is in real trouble.

**Three clean outcomes:**
- **(a) An obstruction binds ED** → tilts toward **Wall 2**; the discreteness commitment is in genuine jeopardy and this becomes the program's hardest honest problem (a Tong-style result against ED). Important either way.
- **(b) No obstruction binds, and SQ2's foliation-Clifford route looks viable** → **Wall 1**; open the front, and the next work is constructing the parity-asymmetric coupling (the arrow's fourth job).
- **(c) No obstruction binds, but no construction route is found** → **undetermined**; the honest resting point is "ED is not forbidden chiral gauge structure, but does not yet produce it," and the gap stays mapped-but-open.

## 6. The honest boundary

This scoping determines the *wall* and the first tractable sub-question. It does **not** produce a chiral coupling, and the full target — a parity-violating gauge sector with correct anomaly cancellation — is hard, plausibly multi-stage, and SQ3 (anomalies) is where a real obstruction, if one exists, most likely hides. The value of doing SQ1 first is that it is cheap (analysis, not a lattice run), it directly tests the discreteness commitment against its sharpest public objection, and *every* outcome is informative: a binding obstruction is a major honesty result; a non-binding one opens ED's most distinctive unexplored front, with the arrow as the natural source of the handedness.

---

*Scoping the chiral-gauge / parity gap (#2b). The problem: a parity-symmetric substrate (P09 U(1), no handedness) vs the SM's parity-violating chiral gauge coupling. Grounded state: ED has Cl(3,1) chiral *room* (γ⁵ exists, T2/T4) and a fundamental *orientation* (the arrow, retarded V1, T18) — but no native chirality ℤ₂ (baryogenesis R1/R2/R3 all failed) and a parity-symmetric gauge sector (T17 rewrite). Oriented in time, ambidextrous in space. Wall question decomposed: SQ1 does N–N bind ED? (premises — lattice, hermiticity — don't apply: ED is non-lattice and retarded/non-hermitian; the arrow is exactly what N–N forbids you to have); SQ2 can the preferred foliation (the same one that gives the khronon) + the timelike-γ⁰ Clifford structure induce a spatial handedness? (promising, ED-coherent, but NOT a CPT argument — T-violation ≠ P-violation, and the arrow alone gives a monary not a binary); SQ3 anomaly cancellation (hardest, deferred). Provisional verdict: Wall 1 (extension-away), not Wall 2 — no known impossibility proof, but current primitives don't produce it. First move (turnkey, analysis): execute SQ1 — write ED's discrete Dirac operator from T4+V1, check N–N premises, test for a non-hermitian/graph generalization; three outcomes (binds → Wall 2 jeopardy; doesn't-bind + route → open the front; doesn't-bind + no route → mapped-but-open). No primitive added, no coupling faked.*
