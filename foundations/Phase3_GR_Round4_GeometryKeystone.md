# Phase-3 GR — Round 4: Geometry Keystone (genuineness, signature, covariance, compatibility)

**Foundations geometry-side analysis. Not a rule proposal, not a corpus edit, not a new primitive. Nothing here derives the Einstein equations.**
Round 3 relocated the obstruction from "is there a conservation law" to the geometry side. Round 4 tests whether ED's emergent geometry (`g_ij ~ b_ij⁻¹` from P04 + the V1 retarded kernel from GR1/T18) is *genuine enough* to support `∇·G = 0`.
**Crank rail:** classify each condition as **structural** (a primitive forbids it) vs **contingent** (a computation/assumption remains). Do not mistake "no structural block" for "EFE emerges."

---

## 1. Metric genuineness — the spatial sector

A thick-regime Riemannian metric needs: symmetry, positive-definiteness, locality, smoothability.

- **Symmetry — guaranteed.** The certified graph is reciprocal (P02; `b_ij = b_ji`, shared edge record), so `g ~ b⁻¹` is symmetric. Structural ✓.
- **Locality — guaranteed.** `g` is built from local adjacency/bandwidth; consistent with A1's no-nonlocal-influence. ✓.
- **Smoothability — thick-regime only.** At the discrete scale there is no smooth metric (only edge weights); `g` is smooth in the DCGT coarse-grained limit. Standard ED methodology; contingent on the thick regime.
- **Positive-definiteness — conditional, and instructively so.** `b ≥ 0` (P04) does **not** by itself make the bandwidth *kernel* positive-definite (a graph kernel can carry zero modes). Genuineness requires **bandwidth regularity** (the kernel invertible, no zero modes) — an assumption beyond `b ≥ 0`. Crucially, the failure mode is physically correct: where `b → 0` (a decoupling cut, A2), the kernel degenerates and `g → ∞` — **the metric degenerates exactly at emergent horizons.** So `g` is a genuine positive-definite metric **in the bulk** (`b > 0`) and degenerates in a controlled way at `b → 0`, which is precisely GR horizon behavior — not a defect (see §6).

**Spatial-sector verdict: conditionally viable** — symmetry/locality structural, smoothness thick-regime, positive-definiteness in the bulk under bandwidth regularity, with correct horizon degeneration at `b → 0`.

## 2. Signature assembly — the time sector

`g ~ b⁻¹` from non-negative bandwidth is Riemannian (positive-definite) — the *spatial* metric. The Lorentzian structure must come from elsewhere. The honest assembly, from corpus ingredients:

- **the cone / lapse** = the **finite-width bandwidth-limit speed `c`** (T8/N1 finite-width kernel; P03 §5.4 "bandwidth-limit speed"). Finite propagation speed *is* what gives an acoustic/analogue metric its light-cone.
- **the time-orientation** = the **retarded arrow** (T18/GR1, inherited from P11): which half of the cone is future.
- **space** = `g_ij ~ b_ij⁻¹`.

Assembled, at leading order: `ds² = −c² dt² + g_ij dx^i dx^j`. Two honest qualifications:

- **Orientation-blindness does NOT block this.** The causal/temporal structure is *kernel-level* (T8/N1, T18), not Σ-level. So B4's ceiling is irrelevant here — the time-direction never needs Σ to read orientation.
- **A reconstruction, not a corpus derivation, and missing the cross-terms.** GR1/T9 currently *takes* the acoustic Lorentzian `σ` (Synge function) as a **background input**; this section *argues* the signature can be built from finite-width `c` + arrow, but the corpus has not derived it that way. And the diagonal `−c²dt² + g_ij dx^i dx^j` is the **static** metric: the cross-terms `g_0i` (lapse/**shift**, frame-dragging, gravitomagnetism) require a **directed bandwidth flux**, absent in the static reciprocal baseline and present only dynamically.

**Time-sector verdict: conditionally viable** — the static Lorentzian metric assembles from corpus pieces (space from `b`, cone from finite-width `c`, arrow from T18); cross-terms need directed flux; and the assembly is a reconstruction the corpus has not yet performed.

## 3. Transport-covariance — and a bundle correction

The round asks whether **P05** transport is covariant w.r.t. the connection that defines curvature. Working it through forces a correction: **P05 is the wrong connection.** P05 transports *polarity / U(1) phase* — it is the **U(1) gauge connection** (the B4 holonomy bundle). The connection that governs `∇·T` and curvature is the **Levi-Civita connection on the tangent bundle**. These are connections on **different bundles**; they are not the same object, and the relevant covariance is **not** a P05 property.

The matter current in `∇_μ T^μν = 0` is the **bandwidth adjacency flux** (a tangent-bundle current `J^μ`). The genuine question is whether *that flux* is Levi-Civita-covariant w.r.t. `g ~ b⁻¹`. Since both the flux and the metric are built from the same bandwidth structure, self-consistent covariance is **plausible** — but it is an **unproven tangent-bundle computation**, and it does **not** reduce to a statement about P05. This is the true uniqueness hinge for `F`: if the adjacency flux is Levi-Civita-covariant, the band↔edge map is forced; if not, `F` stays underdetermined.

**Covariance verdict: conditionally viable / OPEN** — the hinge, correctly identified as a tangent-bundle (flux ↔ Levi-Civita) computation, distinct from P05.

## 4. Metric compatibility (`∇g = 0`)

Compatibility is **automatic for the *defined* connection**: any genuine metric `g` has a unique torsion-free metric-compatible (Levi-Civita) connection. So `∇g = 0` is never the obstruction. The real content is whether ED's **physical** transport/flux connection *coincides* with that Levi-Civita connection — which is exactly the §3 covariance question. If ED's emergent flux-connection had torsion or were non-metric, it would differ from Levi-Civita and break the `G ∝ T` consistency.

**Compatibility verdict: admissible** (automatic for the defined connection); the physical coincidence is the §3 open computation.

## 5. Does `∇·G = 0` follow?

**Yes — automatically, given §1 (genuine metric) + §4 (its Levi-Civita connection).** `∇_μ G^μν = 0` is the contracted second Bianchi identity, a theorem of Riemannian geometry; it is *not* something ED must separately derive. The catch is the connection: this `∇·G = 0` uses Levi-Civita, so the EFE consistency `G ∝ T` (both divergence-free in the *same* connection) still requires the §3 covariance (`∇·T` in Levi-Civita). So: **`∇·G = 0` is free once the metric is genuine; the whole consistency rests on §3.**

## 6. Structural vs contingent — and a unification

| Gap | Structural or contingent? |
|---|---|
| positive-definiteness needs bandwidth regularity | **contingent** (regularity assumption; generically holds in the bulk) |
| metric degenerates at `b → 0` | **not a gap — correct horizon behavior** (see below) |
| smoothability (thick regime) | **contingent** (DCGT; standard) |
| signature assembly (lapse `c`, arrow T18) | **contingent** (pieces exist; derivation not yet done) |
| cross-terms `g_0i` (shift/frame-dragging) | **contingent** (need directed flux; dynamical) |
| transport-covariance (flux ↔ Levi-Civita) | **contingent** (the open computation; not structurally blocked) |
| P05 ≠ Levi-Civita | **clarification, not a block** (different bundles) |

**No structural block is found.** Every open item is contingent — a regularity assumption, an unperformed computation, or a thick-regime correction — not a primitive forbidding the structure.

**The unification (a real payoff):** `g` degenerating at `b → 0` means **A2's emergent decoupling cuts are exactly metric horizons** (where `g` degenerates) — tying A2 (emergent boundaries), the bandwidth-collapse rule (Round 2), and the corpus horizon papers (V5-saturated surfaces, 039/047.5) into one object: *a decoupling surface, an emergent horizon, and a metric degeneration are the same `b → 0` locus.* The bandwidth-collapse rule that forms A2's cuts is the same rule that would form the EFE's horizons.

## 7. Verdict

**ED's emergent geometry is "genuine enough" *in principle* — conditionally viable, with no structural block.** `∇·G = 0` follows automatically once the metric is genuine, and the metric is genuine in the bulk under bandwidth regularity. The residual obstructions are **all contingent**: bandwidth regularity, the **transport-covariance computation** (the hinge, and a tangent-bundle question distinct from P05), the **signature-assembly derivation** (pieces present, not yet assembled; cross-terms need directed flux), and **thick-regime DCGT corrections** (a potential falsifier against exact GR). This is a substantially sharper "genuinely open" than the corpus's starting point: the gap is a small set of geometry-side computations and regularity conditions, **not** a structural impossibility — and it stays honest, because none of those computations is performed here.

Combined Rounds 1–4: full EFE emergence is **partially admissible**; the missing extension is admissible and largely forced (commitment-reserve dynamics); matter conservation is in hand (`∇·T` analogue); the geometric identity `∇·G = 0` is free given a genuine metric; and the entire remaining problem reduces to **transport-covariance + signature assembly + thick-regime regularity** — contingent, not structural. Einstein is *not* derived; the open problem is *located*.

## 8. Round-5 questions

1. **The covariance computation (the hinge).** Is the bandwidth adjacency flux Levi-Civita-covariant w.r.t. `g ~ b⁻¹`? If yes, `F` is forced and `∇·T = 0` matches `∇·G = 0`.
2. **Signature derivation.** Derive the Lorentzian metric explicitly from (space `b`) + (lapse from T8/N1 `c`) + (arrow T18) — does GR1's `σ` *emerge* rather than being assumed?
3. **Cross-terms.** Does directed bandwidth flux produce the shift `g_0i` (frame-dragging / gravitomagnetism)?
4. **Bandwidth regularity.** What conditions on `b` guarantee kernel invertibility (bulk positive-definiteness), and do generic ED states meet them?
5. **Thick-regime corrections.** The DCGT correction to `∇·G = 0` — magnitude, and whether it predicts a measurable departure from exact GR (a falsifier).
6. **Horizon identity.** Confirm `b → 0` emergent cuts (A2) are exactly metric horizons, unifying A2, the bandwidth-collapse rule (Round 2), and the V5 horizon papers (039/047.5).

---

*Round-4 geometry-side analysis only. Verdict: emergent geometry is conditionally viable / "genuine enough" in principle — `∇·G = 0` is automatic given a genuine metric, the metric is bulk-genuine under regularity, and all residual obstructions are contingent (transport-covariance, signature assembly, thick-regime), not structural; the P05-vs-Levi-Civita distinction is a clarification, not a block; A2's cuts unify with metric horizons. No corpus edits, no new primitives, no speculative physics. Einstein is not derived — the open problem is located.*
