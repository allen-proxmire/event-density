# Phase-3 GR — Round 6: The Stress Tensor and the Einstein/Nordström Fork

**Foundations derivation attempt. Not a rule proposal, not a corpus edit, not a new primitive. Nothing here derives the Einstein equations.**
Round 5 secured the *vector* hinge — the bandwidth current is Levi-Civita-covariant, forced by P05+P04 — and relocated the obstruction to the **rank-2** source: build `T^μν` from the bandwidth/participation geometry and test whether `∇_μ T^μν = 0`, including the irreducible `Γ^ν_{μλ}T^μλ` term. Round 6 builds the tensor and runs that test.
**Crank rail:** forward only. A **forced** result is a derivation; a **chosen** one is a retrofit. Tag **structural** vs **contingent**. The most valuable possible outcome here is a sharp *falsifier* — find it if it is there.

---

## 1. Building `T^μν` — the natural matter content

ED's matter is the event density `ρ` carried by the bandwidth current `J^μ = ρ u^μ` (R5: `J^μ` is the transported-amount dual flux; write `u^μ` for its unit direction, `ρ` for its magnitude). The minimal rank-2 object built from this is **pressureless dust**:

> `T^μν = ρ u^μ u^ν`   …(D)

This is not an arbitrary choice — it is the *leading* (lowest-derivative) covariant tensor the R5 current admits, and it matches the corpus picture of matter as **worldlines** (the chain/worldline propagator; the CoarseGrain ballistic fronts). Two honest extensions are noted, not yet used:

- **Perfect fluid** `T^μν = (ρ+p)u^μu^ν + p g^μν` if the Σ **strain** term supplies an isotropic pressure `p` (strain penalises density, the hallmark of pressure). Dust is the `p→0` limit.
- **Scalar-field** `T^μν = ∂^μρ ∂^νρ − ½ g^μν(∂ρ)²` if the `∇ρ` (participation-gradient) energy dominates over advected energy. This is the "field" reading of "ρ + participation geometry."

We proceed with dust (D) as the leading model and flag where the alternatives would change the conclusion.

## 2. The `Γ·T` term is not a cancellation — it is the geodesic condition

Take the covariant divergence of (D), splitting via the current:

> `∇_μ(ρ u^μ u^ν) = (∇_μ J^μ) u^ν + ρ u^μ ∇_μ u^ν`

The first term **vanishes by Round 5** (`∇_μ J^μ = 0`, forced). The second is `ρ a^ν`, where `a^ν ≡ u^μ∇_μ u^ν` is the **4-acceleration** of the flux worldlines. Therefore:

> `∇_μ T^μν = ρ a^ν`   …(◆)

So the irreducible `Γ·T` term of R5 §6 **neither cancels automatically nor obstructs structurally** — it reassembles into the acceleration. The verdict is exact and clean:

> **`∇_μ T^μν = 0` ⟺ `a^ν = 0` ⟺ the bandwidth-flux worldlines are *geodesics* of `g ~ b⁻¹`.**

This is the standard GR fact (dust conservation *is* the geodesic equation), now reached forward from ED's own current. It converts the rank-2 covariance question into a **dynamical** one: *does ED's matter free-fall along the metric its own bandwidth builds?* **Structural status:** no primitive forbids it; whether it holds is a contingent dynamical computation.

## 3. Does ED supply the geodesic identity? Evidence for, proof absent

There is real corpus evidence that the answer is *yes*:

- **CoarseGrain trilogy:** the certified substrate is a **chain/worldline propagator** whose fronts **free-stream ballistically** (`|v|≈1`) on smooth landscapes and bend where the landscape (hence `b`) varies — "the substrate makes trajectories first; fields are what their density makes." Ballistic free-flight that bends with the bandwidth gradient *is* geodesic motion in `g ~ b⁻¹`.
- **Round 1:** ED already exhibits "geodesic-like motion" in the Newtonian limit (it reproduces Poisson).

But evidence is not proof. **It is not established that the substrate worldlines coincide with the metric geodesics of `g ~ b⁻¹`** — the front advances by max-Σ selection (a ρ-coherence extremum), and whether the max-Σ path equals the `g~b⁻¹` geodesic is an unperformed computation (the natural form of "least proper time / longest coherence"). So `∇_μ T^μν = 0` is **conditional on the geodesic identity** — plausible, evidenced by ballistic worldlines, **not proven**. **Contingent — Round 7.** This is also exactly where signature assembly (R4 Q2) becomes a **hard prerequisite**: `a^ν` and `Γ^ν_{μλ}` mix the time and space sectors, so the acceleration cannot even be *written* without the assembled Lorentzian metric.

## 4. The decisive fork: Einstein or Nordström?

Geodesic motion is necessary but **not sufficient** for Einstein — *both* Einstein gravity and Nordström scalar gravity put matter on geodesics. What separates them is the **field equation** (full tensor `G^μν ∝ T^μν` vs trace/scalar `R ∝ T`), and that is decided by whether the **emergent metric carries genuine tensor (anisotropic) structure** or is merely **conformal** (`g_μν = Ω²η_μν`). Nordström gravity is conformally flat, and its fatal, experimentally-refuted signature is **no light bending** (conformally flat metrics leave null geodesics undeflected).

Here ED has a real structural advantage, and a real risk:

- **The advantage (leans Einstein).** Bandwidth `b_uv` is **per-edge — directional**. So `g_ij ~ b_ij⁻¹` is a genuinely **anisotropic** rank-2 metric, *not* a single conformal factor `b(x)⁻¹δ_ij`. Per-edge directionality is exactly the tensor freedom that escapes the conformal-flat Nordström trap and makes Einstein **possible**. The off-diagonal/shift `g_0i` (frame-dragging) likewise needs directed flux (R4 §2) — present only in the genuinely tensorial sector.
- **The risk (a real falsifier).** If, under coarse-graining, the directional bandwidth **isotropises** to an effective scalar `b(x)` near a source, then `g_ij → b(x)⁻¹δ_ij` is **conformally flat** → ED collapses to **Nordström** → **no light bending** → *experimentally dead.* And there is a yellow flag for this: the CoarseGrain equilibrium was measured **isotropic** (`f_d≈0.25`, aniso≈0). That result was for the **vacuum** sector (homogeneous, sourceless) — where isotropy is *correct* (Minkowski is isotropic too) — so it does **not** establish conformal collapse. But it makes the sourced-sector anisotropy a **live, decidable risk**, not a foregone win.

> **The Einstein/Nordström fork is therefore sharp, located, and — for the first time in this arc — *simulable*:** put an ED source down (a high-ρ region), measure whether the emergent metric `g_ij ~ b_ij⁻¹` develops **genuine anisotropy** (radial ≠ tangential bandwidth, the curvature signature) or only a **conformal** rescaling, and compute the resulting **null-geodesic deflection**. Anisotropic + light-bending → Einstein-class; conformal + no-bending → Nordström → ruled out. This is a concrete, falsifiable test the certified-style simulator can run.

## 5. ED ↔ GR structure map (updated through Round 6)

| GR object | ED structure | status |
|---|---|---|
| matter current `J^μ` | adjacency flux (dual, P05) | covariant ✓ (R5) |
| `∇_μ J^μ = 0` | bandwidth continuity (★) | forced ✓ (R5) |
| stress tensor `T^μν` | **dust `ρu^μu^ν`** (leading; fluid/scalar alts) | **built ✓ (R6)** |
| `∇_μ T^μν = 0` | `= ρ a^ν` (◆) | **⟺ geodesic motion (R6)** |
| geodesic identity | substrate worldlines = `g~b⁻¹` geodesics? | evidenced (ballistic), **unproven — R7** |
| Lorentzian signature | space `b` + cone `c` + arrow T18 | **prerequisite** for `a^ν` — **open (R4 Q2)** |
| field equation `G ∝ T` vs `R ∝ T` | metric **anisotropic** (per-edge `b`) vs conformal | **the fork — simulable (R7)** |
| Einstein `G^μν` | curvature of `g~b⁻¹` | `∇·G=0` free (R4); `=T?` open |

## 6. Structural vs contingent

| Item | Verdict |
|---|---|
| `T^μν` exists (dust from R5 current) | **built** (leading; fluid/scalar extensions open) |
| `Γ·T` term cancels/obstructs? | **neither — it is the acceleration** `ρa^ν` (◆) |
| `∇_μ T^μν = 0` | `⟺` geodesic motion — **contingent, evidenced** (R7) |
| geodesic identity (max-Σ path = geodesic) | **contingent — open** (R7) |
| Lorentzian signature for `a^ν` | **contingent — prerequisite** (R4 Q2) |
| metric anisotropy (Einstein-capable) | **available** via per-edge `b`; survival under CG **open** |
| conformal collapse → Nordström | **the falsifier** — vacuum-isotropy a flag, sourced sector untested |
| any structural block | **none found** |

## 7. Verdict

**The rank-2 source is built, and its covariant conservation reduces — exactly and forward — to geodesic motion.** Modelling ED matter as the dust `T^μν = ρu^μu^ν` carried by the R5 current, the divergence collapses to `∇_μ T^μν = ρ a^ν` (◆): the irreducible `Γ·T` term that blocked R5 is neither a cancellation nor an obstruction but the **4-acceleration**, so `∇_μ T^μν = 0` **iff the bandwidth-flux worldlines are geodesics of `g ~ b⁻¹`.** ED supplies strong *evidence* for that identity (the CoarseGrain ballistic worldlines; R1's geodesic-like Newtonian limit) but **not a proof** that the max-Σ path equals the metric geodesic — and writing the acceleration at all now **requires** the Lorentzian signature assembly (R4 Q2), which is hereby a hard prerequisite, not a parallel task.

**Most importantly, Round 6 sharpens the endgame into a single falsifiable fork.** Geodesic motion alone does not give Einstein — Nordström scalar gravity also puts matter on geodesics. The separator is whether the emergent metric is **genuinely anisotropic** (→ Einstein, light-bending) or **conformally flat** (→ Nordström, no light-bending, experimentally dead). ED's **per-edge, directional** bandwidth makes the metric genuinely tensorial and so **Einstein-capable in principle** — but if coarse-graining **isotropises** the bandwidth near a source, ED collapses to Nordström and is **ruled out**. The CoarseGrain vacuum-isotropy result is a genuine yellow flag here (though vacuum-only). **No structural block remains; the entire Einstein question now reduces to one decidable, *simulable* test:** does an ED source produce anisotropic curvature and bend light (Einstein), or only a conformal rescaling and no deflection (Nordström)? Einstein is not derived — but for the first time the arc has a concrete experiment that could *confirm or kill* ED-gravity-as-GR.

## 8. Round-7 questions

1. **The geodesic identity (closes `∇·T=0`).** Prove or refute: do ED's coarse-grained worldlines (max-Σ front paths) coincide with the geodesics of `g ~ b⁻¹`? This is the missing step for rank-2 conservation.
2. **The light-bending test (the fork — simulable).** Put a high-ρ source in the certified-style simulator; measure whether `g_ij ~ b_ij⁻¹` develops radial≠tangential (anisotropic) structure or only conformal rescaling; compute null-geodesic deflection. **Anisotropic+bending = Einstein-class; conformal+no-bending = Nordström = ruled out.**
3. **Conformal-collapse risk.** Does coarse-graining isotropise the sourced-sector bandwidth (Nordström) or preserve directional structure (Einstein)? Connect directly to the CoarseGrain isotropy result, now in the *sourced* (not vacuum) regime.
4. **Signature assembly (now a prerequisite).** Assemble the Lorentzian metric (space `b` + cone `c` from T8/N1 + arrow T18) explicitly, so `a^ν` and `Γ^ν_{μλ}` can be written.
5. **The field equation.** Beyond the fork: derive the curvature↔source relation and check whether it is the full-tensor `G^μν = κT^μν` (Einstein) or a trace relation `R = κT` (Nordström).

---

*Round-6 derivation attempt only. Verdict: the rank-2 stress tensor is **built** (dust `ρu^μu^ν` from the R5 current, leading model), and `∇_μ T^μν` reduces **exactly** to `ρ a^ν` — the `Γ·T` term **is** the 4-acceleration, so conservation `⟺` geodesic motion of the bandwidth worldlines (evidenced by the CoarseGrain ballistic fronts, **not** proven; signature assembly now a prerequisite). The Einstein question sharpens to a single **falsifiable, simulable** fork: per-edge directional bandwidth makes the metric genuinely anisotropic and **Einstein-capable**, but conformal collapse under coarse-graining would drop ED to **Nordström** (no light-bending, ruled out). No corpus edits, no new primitives, no speculative physics. Nothing here derives the Einstein equations — but the arc now has a concrete test that could confirm or kill ED-gravity-as-GR.*
