# Phase-3 GR — Round 5: The Covariance Hinge (flux ↔ Levi-Civita)

**Foundations derivation attempt. Not a rule proposal, not a corpus edit, not a new primitive. Nothing here derives the Einstein equations.**
Round 4 reduced full EFE emergence to a small set of contingent geometry-side computations and named the keystone: *is the bandwidth adjacency flux Levi-Civita-covariant with respect to `g ~ b⁻¹`?* — the one computation that, if it resolves, both closes the `G ∝ T` consistency and forces the band↔edge map (uniqueness of `F`). Round 5 performs that computation.
**Crank rail:** run forward — from the discrete continuity law + the emergent metric to the covariance statement — never backward from Einstein. A **forced** identification is a derivation; a **chosen** one is a retrofit. Tag every step **structural** vs **contingent**. Let it say no.

---

## 1. The target, stated precisely

The EFE consistency `G^μν ∝ T^μν` requires both sides to be divergence-free *in the same connection*: `∇_μ G^μν = 0` (free — contracted Bianchi, R4 §5) and `∇_μ T^μν = 0` (matter). R3 §1 supplied a candidate matter law — the bandwidth continuity law, per locus:

> `d/dt [ Σ_bands b(u) ] = − div(adjacency flux)`   …(★)

The hinge: does the `div` in (★) — a **graph** divergence built from incidence — coincide with the **Levi-Civita covariant** divergence of the emergent metric `g_ij ~ b_ij⁻¹`? R4 called this "plausible because both are built from the same `b`." Round 5 makes it precise, and the precision changes the answer in an instructive way.

## 2. The right framework: discrete exterior calculus (DEC)

On the participation graph, the natural calculus is DEC: scalars (ρ, the band budget) are **0-forms on nodes**; the gradient `(dρ)_uv = ρ_v − ρ_u` is a **primal 1-form on edges**; and a **flux** — an *amount transported across a boundary* — is a **dual `(n−1)`-form** (it lives on the dual face the edge pierces). The two divergences differ exactly by which inner product they are adjoint to:

- **graph/combinatorial divergence** `d^T` — adjoint w.r.t. the **counting measure** (every node weight 1); metric-blind.
- **Levi-Civita covariant divergence** `∇_μ` — adjoint w.r.t. the **metric volume measure** `√g`; equivalently the DEC codifferential `δ = ⋆⁻¹ d^T ⋆`, the Hodge stars carrying the `√g` factors.

So the hinge is a **measure-matching** question: does the divergence in (★) carry the metric volume element, or the bare count?

## 3. The naive identification fails — by exactly `√g`

For a contravariant **vector** current `J^μ`, the covariant divergence collapses (`Γ^μ_{μλ} = ∂_λ ln√g`):

> `∇_μ J^μ = (1/√g) ∂_μ( √g J^μ )`   …(†)

Therefore `∇_μ J^μ = 0  ⟺  ∂_μ( √g J^μ ) = 0`. The combinatorial continuity law (★) conserves a **node sum** `Σ_u b(u)` — i.e. `∂_μ(•) = 0` against the **counting** measure. These coincide **iff** the conserved discrete quantity already *is* the densitized current `√g J^μ`, not the bare `J^μ`. If `b` is a bare scalar, (★) conserves the wrong integral and **differs from the covariant law by the volume element `√g ~ b^{−n/2}`** (with `g_ij ~ b⁻¹δ_ij` isotropic in `n` dims, `det g ~ b^{−n}`).

**So the easy reading — "graph divergence = covariant divergence, automatically" — is false.** They are off by `√g`. This refutes a too-cheap covariance claim and is the round's first result: *covariance is not free*. **Contingent**, and now sharply conditional.

## 4. …but the correct *typing* of the flux makes it hold — and the typing is forced

The `√g` gap is not a defect; it is telling us how to type the bandwidth flux, and the physics supplies the type independently of GR.

The adjacency flux in (★) is, by P05 semantics, the **amount of bandwidth transported across the edge per step** — "the adjacency band exchanges with neighbours via P05 transport" (R3 §1). *Amount transported across a boundary* is, in any exterior calculus, a **flux through the dual face**: a dual `(n−1)`-form `⋆J`, which is **intrinsically `√g`-weighted** (a flux integral `∫ J·dA` already carries the area element). It is **not** a primal 1-form (that would be a *potential difference* `ρ_v−ρ_u`, which bandwidth transport is not).

Two independent corpus facts fix this typing — neither of which mentions Einstein:

- **P05 transport semantics:** transport moves *amount* across adjacency → the flux is the transported amount → a dual flux. (Typing forced by what "transport" means.)
- **P04 extensivity:** bandwidth is an **additive capacity** (four-band partition, additive; `b_ij=b_ji` shared record). An additive/extensive quantity is a **density** — its total over a region is the sum over the region's cells, i.e. `∫√g (•)`. (Density character forced by additivity.)

With the flux correctly typed as the dual (densitized) current, the combinatorial divergence `d^T(⋆J)` **is** `∂_μ(√g J^μ)`, which by (†) **is** `√g ∇_μ J^μ`. Hence:

> **The bandwidth continuity law (★) is exactly the Levi-Civita covariant conservation `∇_μ J^μ = 0`** — *provided* the flux is the transported-amount (dual) current, which P05 transport + P04 extensivity force, independently of EFE.

This is the round's positive result, and it clears the crank gate: the identification is **forced by P05+P04**, not chosen to fit Einstein. **Contingent→resolved**, non-retrofit.

## 5. Consequence: the band↔edge map is forced (R3's residual collapses)

R3 §4 left `F` only *partially* forced — the load-bearing freedom was the **band↔edge map** (per-chain four-band dynamics ↔ per-edge `b_uv`). §4 here removes that freedom in the required direction: covariance demands the conserved bandwidth be the **`√g`-density** carried as a **dual edge flux**, identified **spatially-locally** (the dual face an edge pierces — P02 adjacency *is* the spatial locality). So the per-edge `b_uv` *is* the density-valued field, and the per-chain budget maps to it as a dual flux. This is a *specific* band↔edge map, **selected by covariance + P05/P04**, not by retrofit. The residual functional family of R3 (constant, `δ`, map) loses its load-bearing member.

**One honest assumption, flagged:** "extensive ⟹ spatial density" uses the band↔edge map to be the *spatially-local* one. P02 adjacency makes this natural, but it is an identification, not a theorem from a single primitive. **Contingent** (named, plausible, not proven).

## 6. The obstruction relocates — and sharpens toward *Einstein specifically*

Resolving the hinge exposes that it was posed one tensor-rank too low. (★) conserves a **current** `J^μ` (a vector) — so what Round 5 secures is the analogue of **charge conservation** `∇_μ J^μ = 0`. But the EFE source is the **rank-2 stress tensor** `T^μν`, and its covariant divergence does **not** collapse the way (†) does:

> `∇_μ T^μν = (1/√g) ∂_μ(√g T^μν) + Γ^ν_{μλ} T^μλ`   …(‡)

The extra **`Γ^ν_{μλ}T^μλ`** term is *not* a total divergence and is *not* removed by the `√g` argument. So **vector covariance (§4) does not imply tensor covariance.** The bandwidth continuity law, even fully covariant, gives a conserved *current*, not a conserved *stress tensor*.

This is the genuine, sharpened obstruction, and it is the gate to **Einstein** specifically: a theory whose gravity is sourced by a scalar/current (only §4) is a *Nordström-type* scalar gravity, **not** GR. Reaching the Einstein equation requires (a) **constructing `T^μν`** from the bandwidth + participation geometry (R4 §2's "ρ + participation geometry" stress analogue, as yet unbuilt), and (b) showing **(‡) vanishes** — i.e. the `Γ·T` term is accounted for in the same Levi-Civita connection. Neither is performed here. **Contingent, not structural** — no primitive forbids a rank-2 source; it is an unperformed construction.

## 7. ED ↔ GR structure map (updated through Round 5)

| GR object | ED structure | status |
|---|---|---|
| spatial metric `g_ij` | `b_ij⁻¹` (P04) | bulk-genuine under regularity (R4 §1) |
| Lorentzian signature | space `b` + cone `c` (T8/N1) + arrow (T18) | assembly **open** (R4 Q2) |
| connection ∇ | Levi-Civita of `g~b⁻¹` (**not** P05 = U(1)) | defined; physical coincidence = this round |
| matter current `J^μ` | adjacency flux = **dual** transported-amount (P05) | **covariant ✓ (§4)** |
| `∇_μ J^μ = 0` | bandwidth continuity (★) | **holds, forced (§4–5)** |
| band↔edge map | density/dual-flux identification | **forced by covariance (§5)** |
| Einstein tensor `G^μν` | curvature of `g~b⁻¹` | `∇·G=0` free (R4 §5) |
| stress tensor `T^μν` | rank-2 from ρ + participation geometry | **NOT built — open (R6)** |
| `∇_μ T^μν = 0` | rank-2 covariance incl. `Γ·T` (‡) | **open — the relocated hinge (R6)** |

## 8. Structural vs contingent

| Item | Verdict |
|---|---|
| graph-div ≠ covariant-div (off by `√g`) | **resolved** — fixed by correct (dual) typing |
| flux typing (dual/density) | **forced** by P05 transport + P04 extensivity (non-retrofit) |
| vector covariance `∇_μ J^μ=0` | **holds** (contingent→resolved) |
| band↔edge map | **forced** by covariance (R3 residual collapses) |
| extensive ⟹ *spatial* density | **contingent** (P02-natural; assumed, not proven) |
| rank-2 `T^μν` construction | **contingent — open** (unbuilt) |
| rank-2 covariance (`Γ·T` term, ‡) | **contingent — open** (the relocated obstruction) |
| any structural block | **none found** |

## 9. Verdict

**The covariance hinge resolves — at the rank it was posed — in ED's favour, and the resolution is forced, not retrofitted.** The bandwidth adjacency flux *is* Levi-Civita-covariant with respect to `g ~ b⁻¹`, once it is correctly typed as the transported-amount (dual, density-weighted) current — a typing forced by P05 transport semantics and P04 extensivity, with no reference to Einstein. This (i) makes the bandwidth continuity law the genuine covariant conservation `∇_μ J^μ = 0`, (ii) **forces the band↔edge map**, collapsing R3's load-bearing residual freedom in `F`, and (iii) refutes the naive "graph-divergence = covariant-divergence" reading (they differ by exactly `√g`), replacing it with a correct, derived one.

**But resolving it shows the hinge was one tensor-rank too low.** What is secured is a *current* (charge-type) conservation; the EFE source is a *rank-2* stress tensor, whose covariant divergence carries an irreducible `Γ^ν_{μλ}T^μλ` term (‡) that the vector argument does not touch. So Round 5 **advances partial admissibility** — the flux-covariance sub-problem is closed and `F`'s uniqueness is improved — while **relocating** the obstruction precisely: from *"is the flux covariant?"* (now: **yes, forced**) to *"can a rank-2 `T^μν` be built from the bandwidth/participation geometry and shown covariantly conserved (‡)?"* — which is the gate to **Einstein specifically** (a current-only source is Nordström scalar gravity, not GR). No structural block appears; the residual is an unperformed rank-2 construction. **Einstein is not derived; the open problem is now located one level deeper, and one degree of freedom less free.**

## 10. Round-6 questions

1. **Build `T^μν`.** Construct the rank-2 stress tensor from ρ + participation geometry (R4 §2). What are its components — does directed bandwidth flux supply the off-diagonal momentum density (the same flux that supplies the metric shift `g_0i`)?
2. **The `Γ·T` term (‡).** Does `∇_μ T^μν = 0` hold for that `T` in the Levi-Civita connection of `g~b⁻¹` — i.e. is the `Γ^ν_{μλ}T^μλ` term cancelled by the densitized part, or does it obstruct?
3. **Nordström fork.** If only the current conserves and the rank-2 term obstructs, does ED's emergent gravity land on **scalar (Nordström) gravity** rather than GR? Characterize that fork explicitly — it is a sharp, falsifiable divergence from Einstein.
4. **Signature coupling.** Does the rank-2 covariance computation *require* the Lorentzian assembly (R4 Q2) first, since `Γ` mixes time and space sectors? (Likely yes — signature assembly may be a prerequisite, not a parallel task.)
5. **Spatial-locality assumption (§5).** Can the "extensive ⟹ spatial density" identification be derived from P02 + P04 rather than assumed?

---

*Round-5 derivation attempt only. Verdict: the flux ↔ Levi-Civita covariance hinge **resolves, forced (non-retrofit)** — the bandwidth current is covariant once typed as the transported-amount dual flux (P05+P04), making (★) the genuine `∇_μ J^μ = 0`, forcing the band↔edge map, and refuting the naive graph-divergence reading (off by `√g`). The obstruction **relocates** to the rank-2 stress tensor: `∇_μ T^μν = 0` carries an irreducible `Γ·T` term the vector argument does not reach, and the EFE source `T^μν` is as yet unbuilt — the gate to Einstein specifically (vs Nordström scalar gravity). No corpus edits, no new primitives, no speculative physics. Nothing here derives the Einstein equations; the open problem is located one level deeper, with one fewer free parameter.*
