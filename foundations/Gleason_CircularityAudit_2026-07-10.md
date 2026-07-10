# P-Channel-Orthogonality — Circularity Audit of the 2026-07-08 Reconstruction

**Foundations — QM-kinematics / #8b (Gate 1). Opened 2026-07-10.** Crank-rail ON. This note does NOT re-derive orthogonality (the corpus already did, 2026-07-08, `Gleason_Soler_LatticeVerification.md`). It audits the one thing that decides whether that reconstruction is real: the **circularity flag** the 2026-07-08 docs left hanging on Move 1 and on the Solèr angle condition. Verdict up front: **the flag clears; the reconstruction is non-circular; the genuine residual is Solèr lattice rigor, not orthogonality.**

Sources read: `Paper_004_GleasonUniqueness.md` (the two postulates + Conjecture 1), `Gleason_Rehabilitation_Attempt.md` (three failed routes), `Gleason_Complementarity_Reframe_Scoping.md` (the operational reframe + non-Boolean gate), `Gleason_Soler_LatticeVerification.md` (the axiom map + Move 1 + einselection), and `evaluation/ChiralGauge/move1_operational_orthogonality.py` (theorem (B) verified: best confusion-free detection = `1 − c²`, standard unambiguous-discrimination).

---

## 1. The state being audited

The 2026-07-08 reconstruction discharges P-Channel-Orthogonality via **Move 1**:

- **(A) Operational fact, metric-free:** a pure channel-`K` preparation commits to `K` with frequency 1 (P11); a pure channel-`L` preparation has `b_K = 0`, so commits to `K` with frequency 0 (P07 + Born, Paper_003). So distinct ED channels are **perfectly distinguishable** (`p(K|K)=1, p(K|L)=0`), pure frequency data, no inner product.
- **(B) Theorem, within the representation:** for candidate states with tunable overlap `c = ⟨K|L⟩`, the best confusion-free detection of `K` (max `⟨K|E|K⟩` over POVMs with `⟨L|E|L⟩=0`) is `1 − c²`, equal to 1 iff `c = 0`. So **perfect distinguishability ⟺ orthogonality.**
- **Conclusion:** `⟨K|L⟩ = 0` is forced by the commitment frequencies, **given that the inner-product representation exists** (the Piron–Solèr embedding).

**The two circularity flags the 2026-07-08 docs raised on this:**
- **Flag 1 (Move 1):** theorem (B) uses POVMs/vectors, i.e. it is proven *inside* the representation. Does deriving orthogonality "within the representation" beg the question?
- **Flag 2 (angle condition):** Solèr needs an infinite *orthonormal* sequence of *equal norm*. "Orthonormal" seems to presuppose the orthogonality being derived, and "equal norm" is a metric statement presupposing the inner product.

---

## 2. The resolution: two different notions of orthogonality

Both flags conflate **two distinct objects** that the reconstruction keeps separate:

- **Lattice-orthogonality** (`K ⟂ L`): the abstract orthocomplementation relation `a ≤ b'` in the proposition lattice. ED grounds it in **P11 exclusivity**: a pure-`K` state never resolves to `L`, so `K ≤ L'` in the commitment lattice. This is **metric-free** — it is a fact about which commitments exclude which, not about any inner product.
- **Metric-orthogonality** (`⟨K|L⟩ = 0`): the *value* the reconstructed inner product assigns to a pair of channel-atoms. This is the **output**.

The entire content of Piron–Solèr is a **representation theorem**: an orthocomplemented lattice satisfying the axioms is represented by a Hermitian space in which the abstract lattice-`⟂` *becomes* metric-`⟂`. So lattice-`⟂` is the **input** (grounded in P11, metric-free) and metric-`⟂` is the **output** (forced by the theorem). They are not the same object; the theorem is precisely what connects them. Once this distinction is drawn, both flags clear.

### Flag 2 clears — the angle condition is fed metric-free
Solèr's angle condition (infinite orthogonal sequence, equal norm) has three inputs, each grounded without a metric:
- **infinite** ← P03 spatial homogeneity (infinitely many translation-equivalent channels);
- **orthogonal** ← P11 exclusivity, in the **lattice** sense (`K ≤ L'`), not the metric sense;
- **equal norm** ← P03 homogeneity gives translation-equivalent channels *equal bandwidth*, hence equal Born-normalized weight (each single-channel pure state has total commitment probability 1). This is **equal commitment frequency**, an operational fact, not the metric norm.

The "equal-norm presupposes the inner product" worry conflated the operational equal-Born-weight (input) with the metric self-value (output). Cleared.

### Flag 1 clears — Move 1 is a consistency bridge, not a bootstrap
Theorem (B) is correctly proven inside the representation, because its *job* is not to build the representation but to **connect** the metric-free operational fact (A) to the forced metric: given the representation, operational perfect-distinguishability forces the metric overlap `c = 0`. This is non-circular **provided the representation's existence does not itself presuppose metric-`⟂`** — and it does not. The representation is produced by Piron–Solèr from inputs that are all metric-free:

```
[P11 exclusivity  → lattice-⟂ channel-atoms]        (metric-free)
[P_K=√b·e^{iπ}, P11 → non-Boolean complementarity]  (metric-free; the 2026-07-08 gate, Parts 1–3)
[P11 first-kind + irreversibility → covering law]    (metric-free)
[P03 homogeneity  → infinite equal-weight atoms]     (metric-free)
        │
        ▼  Piron–Solèr representation theorem
[forced Hermitian inner product; field ℂ via P09 / V5-063]
        │
        ▼  Move 1 (B)
[operational distinguishability  =  metric ⟨K|L⟩=0]
```

This is the standard structure of every quantum reconstruction (Piron, Solèr, Hardy, CDP): metric-free operational/lattice input → forced metric output → the operational facts map onto the metric facts. **Non-circular.** The three historical routes (P04 additivity, P07 distinctness, P11 phase-randomization) failed because they hunted metric-`⟂` as a *kinematic fact inside an assumed metric*; orthogonality is instead the metric *representation* of the P11-grounded lattice exclusivity.

---

## 3. The residual, correctly re-scoped (and one honest soft spot)

Orthogonality is discharged and non-circular. What remains load-bearing is **not** orthogonality but the **rigor that ED's commitment lattice actually satisfies the Piron–Solèr hypotheses**:

1. **The covering law's exchange property** (the projective-geometry step of Piron's representation). Operationally grounded (P11 = first-kind orthogonal atomic projection, irreversibility enforcing repeatability); the lattice-theoretic exchange-property rigor is owed.
2. **The full orthomodular identity — the honest soft spot.** The 2026-07-08 work established ED's lattice is **non-Boolean** (metric-free, from complementarity) and that the *full* orthomodular identity "rides with the representation." But Piron's theorem takes orthomodularity as a **hypothesis**. So the real open question is sharp: can ED establish the full orthomodular identity **metric-free** (from the primitives / operational structure), or only non-distributivity? If only the latter, the hypothesis of the representation theorem is not yet metric-free-established. This is the tightest remaining screw, and it should not be waved through.
3. **Infinite-dimensional subtleties + the `*`-ring rigor** underneath Solèr's field trichotomy.

Plus the **prediction frontier**: the reconstruction's two distinctive claims — *primitive einselection* (the arrow selects the channel pointer basis) and *emergent multi-context* (Gleason/KS structure is emergent, not fundamental) — need an observability analysis. That is where a falsifier would live.

---

## 4. Honest tier + net

**Tier: an audit that upgrades the reconstruction's honesty, not a new theorem.** Two flagged circularities clear once lattice-`⟂` (input, from P11) is distinguished from metric-`⟂` (output, forced), and operational equal-Born-weight from the metric norm. Orthogonality (`⟨K|L⟩ = 0`) is derived at **reconstruction tier** and is **non-circular**. This realizes Paper_004's Conjecture 1 (P07 distinguishability → orthogonality) with an explicit, non-circular mechanism.

**Do NOT claim** the Hilbert space is derived. The Piron–Solèr hypotheses for ED's lattice are grounded to roughly 6–7 of 8, with the exchange-property geometry, the **metric-free establishment of the full orthomodular identity** (the soft spot, §3.2), and the infinite-dim/`*`-ring rigor as the genuine remaining program.

**Net for Gate 1 / #8b:** the blocking postulate that stalled three prior attempts is discharged and audited-non-circular. The keystone's residual is **Solèr lattice rigor + the einselection-prediction observability**, not orthogonality. The research-targets #8b entry and the day-old `ED_Road_To_Unification.md` Gate 1 framing were stale (2026-07-02 wording, predating the 2026-07-08 reconstruction); both are corrected to point here.
