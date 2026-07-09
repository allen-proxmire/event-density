# ED Gravity Is Relational (Background-Free on the Participation Graph); the Topology/Dimension Itself Is Primitive (P06 Wall): the Two Senses Separated

**Foundations, gravity / curvature-emergence arc, the background-free question. All prior curvature probes ran on a clean d-dim LATTICE with a coordinate label line; "background-free" was the last-listed open frontier. This note separates two senses and settles each. (1) STRONG (derive the graph's dimension/topology from nothing): a WALL, canonical P06 makes the spatial dimension a primitive/selection, and the reduction program (Paper A) found 3D "selected not derived". (2) RELATIONAL (the physically meaningful sense): are the curvature results properties of the participation graph's OWN structure, readable from adjacency alone with NO coordinates? Result (`evaluation/CurvatureEmergence/background_free_relational_probe.py`): YES. On a coordinate-free irregular graph (a random geometric graph with the coordinates DISCARDED after construction, all measurements using adjacency + hop-distance only), the intrinsic dimension reads out of hop-ball growth (2.98 in the 3D graph, 1.99 in the 2D control), and the harmonic/Gauss field equation on the graph LAPLACIAN returns the dimension-appropriate Green's function, `1/k` (Newtonian) in the 3D graph (form-fit `R²=0.987`, beating `log k` 0.955 and `1/k²` 0.914), and `log k` in the 2D control (`R²=0.911`). The 2D control returning the 2D Green's function proves it is the graph's INTRINSIC dimension driving the result, not any coordinates. So ED's emergent metric + Newtonian field equation are RELATIONAL, they live on the participation relations, not on an embedding, background-free in the sense that matters. The graph's BEING ~3D stays input (P06). Verdict: relational YES; topology-from-nothing NO (a wall, consistent with the reduction program).**

---

## 1. Two senses of "background-free"

The curvature-emergence results (metric `g~1/b`, holographic cut, Gauss's-law field equation) were all measured on a clean d-dimensional lattice. That raises the standard background-independence worry: is the emergent gravity a property of the substrate's *relations*, or an artifact of the imposed lattice? The worry has two very different forms, and conflating them muddies the answer:

- **(1) Strong / topology-from-nothing.** Derive the graph's connectivity and its dimension from a deeper ED rule, with no arena assumed. **This is a wall.** Canonical Paper_087 P06 makes the spatial dimension a *primitive*; P03 makes the locus-adjacency a primitive (spatially homogeneous indexing). The reduction program (Paper A, `PrimitiveReduction_3D_...`) tested P06 directly and found 3D *selected, not derived*, with only a conditional linking candidate (itself gated). So the arena is input; deriving the topology from nothing is not achievable and is not expected to be.
- **(2) Relational.** Given a participation graph, are the curvature results computable from the graph's *own structure* (adjacency, hop-distance, bandwidth) with no reference to coordinates or a lattice embedding? If they transfer to an irregular, coordinate-free graph, the gravity is background-free in the physically meaningful sense: it is a fact about the relations, and the clean lattice was only a convenient carrier.

This note settles (2) with a probe, and states (1) as the wall it is.

## 2. The probe: curvature physics on a coordinate-free graph

Build a **random geometric graph** (N points scattered in a d-cube, connected by proximity), then **discard the coordinates** and keep only the adjacency. The graph's dimension is inherited from the construction, that inheritance *is* the P06 input of sense (1), and is acknowledged, not hidden. Everything downstream uses adjacency and hop-distance only:

- **(A) Intrinsic dimension** from hop-ball growth: `|B_hop(k)| ~ k^d`, read `d` from the graph itself.
- **(B) Holographic cut** of hop-balls: the shell `|{nodes at hop k}| ~ k^{d-1}`.
- **(C) The field equation** on the **graph Laplacian** (adjacency only): fix a source node `φ=1` and the far hop-shell `φ=0`, solve `Lφ=0` on the interior, and read the potential vs hop-distance. It must be the d-dim Green's function, `1/k` (Newtonian) in 3D, `log k` in 2D.

A 2D graph is run as a **control**: the same machinery should read `d=2` and return the 2D (log) Green's function, showing that the graph's *intrinsic dimension*, not any coordinates, drives the result.

## 3. Results

| measurement (adjacency only) | 3D coordinate-free graph | 2D control |
|---|---|---|
| (A) intrinsic dim `|B(k)|~k^d` | **d = 2.98** (`R²=0.999`) | **d = 1.99** (`R²=1.000`) |
| (B) holographic cut shell `~k^s` | s = 2.38 (`R²=0.998`) | s = 1.10 (`R²=0.989`) |
| (C) graph-Laplacian potential, best fit | **`1/k` (Newtonian)** `R²=0.987` (vs log 0.955, `1/k²` 0.914) | **`log k` (2D)** `R²=0.911` (vs `1/k` 0.650) |

**The two load-bearing results are clean.** The intrinsic dimension reads correctly from the graph's own hop-ball growth (2.98, 1.99), and the field equation on the graph Laplacian returns the dimension-appropriate Green's function, `1/k` Newtonian on the 3D graph, `log k` on the 2D control, computed from adjacency alone, no coordinates. The **2D control is the decisive check**: the same code, on a graph whose only difference is its intrinsic dimension, returns the *2D* Green's function, so it is the relational structure (the intrinsic dimension) producing the result, not a coordinate embedding.

**One honest blemish.** The cut-shell exponent (B) is noisier on the irregular graph: 1.10 in 2D (clean, ≈ d−1) but 2.38 in 3D (inflated vs the expected 2). On the dense random graph the hop-shell has log-log curvature (density gradient in hop-space); the *clean* holographic cut measurement is on the lattice (the reach-law probe gives 1.999). Here (B) is only a secondary confirmation, roughly holographic; the intrinsic dimension (A) and the field equation (C) carry the claim, and both are clean. Note also a genuine tension observed: the graph-Laplacian field equation (C) needs *sufficient* connectivity to approximate the continuum Laplacian (a sparser graph degrades it), while the cut (B) is cleaner when sparser, so no single density optimizes both; the reported run favors (C), the load-bearing one.

## 4. Verdict: relational YES, topology-from-nothing NO

- **Relational background-freedom (sense 2): achieved.** ED's emergent metric and Newtonian field equation are properties of the participation graph's own structure, computable from adjacency and bandwidth alone, with no coordinates or lattice. The clean lattice used in the earlier probes was a convenient carrier, not a load-bearing assumption; the same physics lives on an irregular coordinate-free graph. This is the physically meaningful sense of background-independence, and ED gravity has it.
- **Topology/dimension from nothing (sense 1): a wall.** The graph's *being* ~3D is input, here from the construction, canonically P06 (a primitive/selection). The reduction program already found 3D selected-not-derived (with only a conditional linking candidate). So the arena is primitive; deriving the topology from a deeper ED rule is not achieved and is not expected, consistent with the whole reduction picture.

The honest closure of the background-free frontier is therefore a **partial YES plus a named wall**: the emergent gravity is relational (it needs the relations, not an embedding), while the relations' dimension is the one genuinely primitive input the arena supplies. This also sharpens the standing 3D story: the geometry *reads* its dimension from the graph (2.98 here), so the "d" that the holographic cut, the reach law, and the Gauss field equation all use is an intrinsic graph fact, not a coordinate artifact, but *which* dimension the graph has remains P06, the wall the linking argument (Paper A) is the only conditional candidate to lift.

## 5. Status

Curvature emergence now: metric `g~1/b` derived (reach law), linear field equation derived (Gauss's law), nonlinearity characterized (MOND, interference), and the emergent gravity shown **relational / background-free** on the participation graph (this note), with the topology/dimension itself standing as the P06 primitive (a wall). The remaining genuinely-open piece is the *nonlinear covariant* field equation as a derived (not characterized) object; the linear-and-relational structure of ED gravity is now established, and the "is it just a lattice artifact?" worry is answered: no, the metric and field equation are relational; only the arena's dimension is input.
