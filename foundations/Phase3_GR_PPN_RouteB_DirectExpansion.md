# Phase-3 GR — Route B: Direct PPN Expansion of the ED Rule (the Framework and the O(v³) Field Equations)

**Foundations derivation — begins "Route B": a post-Newtonian expansion of the ED dynamical rule itself, *not* the conservative khronometric action. Builds the correct PPN bookkeeping for the bandwidth field and derives the first-order preferred-frame (`α₁, α₂`) structure directly from the rule. Not a corpus edit, not a new primitive. This session delivers the FRAMEWORK and the O(v³) equations, not the final numbers — and labels every undetermined quantity symbolically.**

Route A (`Phase3_GR_PPN_RouteA_Mapping.md`) reduced the open number to one coupling `c₁₄` via the *conservative* khronometric formulas, and showed those formulas cannot see ED's dissipative near-field. Route B sidesteps the conservative action entirely: it expands `ḃ = D∇²b − κρ` (plus the dissipative reserve) around a source moving through the cosmic frame and reads the preferred-frame terms off the emergent metric. The central structural fact that makes this work: **the ED rule is written in the cosmic (khronon) rest frame and is first-order in cosmic time — it is manifestly not boost-invariant. Source motion at `w` relative to that frame is exactly what sources `α₁, α₂`.**

**Crank rail (load-bearing):** derive forward from the rule; keep the metric-assembly normalization, the reserve rate, and the band-fractions **symbolic**; do **not** fabricate the standard-PPN prefactors (cite Will/TEGP) or the final `α₁, α₂`. A framework that correctly *locates* the preferred-frame terms is the deliverable; the numbers are later steps.

> **⚠ CORRECTION (2026-06-23) — §7's α₁/α₂ matching is SUPERSEDED.** §5–§7 below source `g_{0i}` from the *scalar* bandwidth current and obtain `α₁=4η(𝒮₁+𝒮₂)`, `α₂=2η𝒮₂` (conservative `α₁=−8c₁₄`, `α₂=−2c₁₄`). Both are **wrong**: `DirectedFlux` test [1] shows the scalar current is **curl-free → pure gauge → no physical `g_{0i}`**; the physical cross-term is the **vector sector** `g_{0i}=λ_J w_iU` (`w_iU` only). With the verified Will form + luminal khronometric values (`α₁=−4c₁₄`, `α₂=0`), the correct result is **`α₁=−4c₁₄𝒮(Γ)`, `α₂=0`** (the §7 `w^jU_{ij}`/α₂ term was a pure-gauge artifact). See `Phase3_GR_Alpha2_Vanishes_Alpha1_Reconciled.md §9`. The framework/order-counting of §1–§6 stands; only the §7 numeric matching is replaced.

---

## 1. Expansion strategy and PPN order counting

**Strategy.** Work in the cosmic rest frame (the preferred frame, where the khronon background is at rest). Put the matter source in bulk motion at constant velocity `w` relative to this frame (`w` = the PPN frame velocity, `|w| ~ 369 km/s` from the CMB dipole, observationally). Because the rule's `∂_t` and `∇²` are cosmic-frame operators with **no boost symmetry**, the comoving solution acquires `w`-odd and `w`-even corrections that are absent for a static source. Those corrections, carried into the emergent metric's `g_{0i}`, are the preferred-frame potentials. We expand to the order where `α₁` (∝ `w`) and `α₂` (∝ `w²` via the anisotropic potential) first appear: **`g_{0i}` at O(v³).**

**Order counting** (standard PPN bookkeeping, Will/TEGP):

| Quantity | Order | Note |
|---|---|---|
| velocities `v^i`, `w^i` | O(1) | source and frame velocities |
| Newtonian potential `U` (`∇²U = −4πGρ`) | O(2) | virial `U ~ v²` |
| rest-mass density `ρ` (source of `U`) | O(2) | |
| `∂/∂x^i` | O(0) | spatial gradient preserves PPN order |
| `∂/∂t` | O(1) | a time derivative raises order by one (`∂_t ~ −w·∇` for a comoving field) |
| bandwidth `b = 1 + b₂ + b₃ + b₄ + …` | `bₙ ~ O(vⁿ)` | `b₂ = −2U` (below) |
| lapse `N² = b` | — | `N = b^{1/2} = 1 − U + …` |
| spatial metric `g_{ij} = b^{-1}δ_{ij}` | — | isotropic ⟹ `γ = 1` (below) |
| shift / `g_{0i}` | O(3) | the preferred-frame sector |

The key consequence of "`∂_t` is O(1)": the rule's time-derivative term `ḃ`, which vanishes for a static source, becomes the **convective term `−w·∇b`** for a comoving source — and `w·∇b₂` is O(3), exactly the order of `g_{0i}`. The preferred-frame terms are sourced by the one term in the rule that the static derivation discarded.

## 2. Metric assembly: `g_{0i}` is the bandwidth current

ED fixes the diagonal metric (GR-I): `g_{00} = −N² = −b`, `g_{ij} = b^{-1}δ_{ij}`. The off-diagonal `g_{0i}` — absent in the static solution — must come from the directed bandwidth flux (the "cross-terms require the directed-flux dynamics" deferred in the metric-assembly note). Write the emergent metric in ADM form,

> `ds² = −N²dt² + g_{ij}(dx^i + N^i dt)(dx^j + N^j dt)`,  so  `g_{0i} = g_{ij}N^j = b^{-1}N_i ≈ N_i` (at O(3), `b ≈ 1`).

The shift `N^i` is the local drift velocity of the bandwidth field — the analogue-gravity "flow." In analogue/acoustic metrics `g_{0i} = −v_i^{flow}`; for ED the flow is the bandwidth current `J_b^i` per unit field. We therefore identify

> `g_{0i} = η · J_b^i + O(v⁵)`,   `η` = the metric-assembly normalization *(symbolic — fixed by the explicit directed-flux derivation; this is Route B's analogue of Route A's `c₁₄`, and the two must agree, §7)*.

`J_b^i` is the conserved bandwidth current of P04: from `∂_t b + ∇·J_b = S` with sink `S = −κρ` (+ reserve), Fick's law for P02 adjacency-sharing gives the diffusive part `J_b^{diff} = −D∇b`, and a moving depletion carries a convective part. Both are computed below.

## 3. The boost-non-invariant rule → convection–diffusion

The ED metric-band rule in the cosmic frame is

> `∂_t b = D∇²b − κρ`   *(+ dissipative reserve, §6)*,  `κ/D = 8πG` (pinned).

First-order in cosmic time ⟹ **no boost invariance**: this is the structural origin of preferred-frame effects. For a source in bulk motion `ρ(x,t) = ρ₀(x − wt)`, seek the comoving solution `b(x,t) = B(ξ)`, `ξ = x − wt`. Then `∂_t b = −w·∇B`, and the rule becomes the **convection–diffusion equation**:

> `D∇²B + w·∇B = κρ₀`.   (★)

The convective term `w·∇B` is the entire preferred-frame source. It is O(1) higher than the diffusive term (the `∂_t`-counting), so it enters one PPN order above Newtonian — precisely at the `g_{0i}` order.

## 4. O(2): the static sector (recovers `γ = 1`)

Write `B = 1 + β`, `β = β₂ + β₃ + …`. At O(2), drop `w·∇β` (higher order):

`D∇²β₂ = κρ₀ ⟹ ∇²β₂ = (κ/D)ρ₀ = 8πG ρ₀ ⟹` **`β₂ = −2U`**,  `∇²U = −4πGρ₀`.

Then `g_{00} = −b = −1 + 2U + O(v⁴)` and `g_{ij} = b^{-1}δ_{ij} = (1 + 2U)δ_{ij} + O(v⁴)`, so comparing to the PPN forms `g_{00} = −1 + 2U`, `g_{ij} = (1 + 2γU)δ_{ij}` gives **`γ = 1`** — the same `b` setting both, i.e. the Schwarzschild relation of GR-I, re-derived inside the PPN bookkeeping. (Consistency check passed; the factor-of-two light bending follows from `γ = 1` as usual.)

## 5. O(3): the preferred-frame sector — where `α₁` and `α₂` are born

Two O(3) structures feed `g_{0i} = η J_b^i`.

**(a) The convective current → `w_i U` → `α₁`.** The conserved current carrying the co-moving depletion is `J_b^{conv} = w(b − 1) = wβ`. At O(3):

> `J_b^{conv,(3)} = w β₂ = −2U\,w`   ⟹   `g_{0i} ⊃ η · (−2U w_i) = −2η\,w_i U`.

This is the `w_i U` potential — the structure whose PPN coefficient is fixed by `α₁`. It is **nonzero in the purely conservative (`D∇²`) theory**, with magnitude set by `η`.

**(b) The diffusive O(3) response → `w^j U_{ij}` → `α₂`.** The convective term back-reacts on the scalar through (★) at O(3):

`D∇²β₃ + w·∇β₂ = 0 ⟹ D∇²β₃ = −w·∇β₂ = 2\,w·∇U`,  i.e.  `∇²β₃ = (2/D)\,w^j ∂_j U`.

The diffusive current carries this as `J_b^{diff,(3)} = −D∇β₃`, so

> `g_{0i} ⊃ η · (−D ∂_i β₃) = −2η\, w^j\, ∂_i∂_j Ψ`,   `∇²Ψ = U`,

where `∂_i∂_j Ψ` is the symmetric anisotropic superpotential `U_{ij}` (Will's `χ_{,ij}`-type tensor, `∇²Ψ = U`). This `w^j U_{ij}` potential is the **anisotropic** structure whose PPN coefficient is fixed by `α₂`. It too is **nonzero conservatively**.

So the rule produces, at O(3),

> **`g_{0i} = −2η\,( w_i U + w^j U_{ij} ) + (standard matter-current terms `V_i, W_i`) + O(v⁵)`.**

Both preferred-frame potentials appear, both ∝ `η`. This reproduces, from the rule directly, Route A's conclusion that a *conservative* reading gives nonzero `α₁, α₂` — and it identifies the single conservative normalization `η` as their common origin.

## 6. The dissipative reserve — ED's non-conservative correction (kept explicit)

The conservative result of §5 is not ED's final answer, because near matter the khronon sector is dissipative (the `ε = 0` derivation: the commitment-reserve is one-way, overdamping the scalar). In the band rule this is a **relaxation/damping term** tied to the reserve drain `Γ(x)` (large where commitment is active, i.e. near matter):

> `∂_t b = D∇²b − κρ − Γ(x)\,(b − b_eq)`   ⟹ comoving:  `D∇²B + w·∇B − Γ(B − b_eq) = κρ₀`.   (★★)

`Γ(x)` is the reserve-overdamping rate *(symbolic — set by the P11 drain profile; `Γ → 0` in vacuum, `Γ` large near matter)*. Its effect on the O(3) sector: the damping competes with the convective transport. Schematically the O(3) equation becomes `D∇²β₃ − Γβ₃ = −w·∇β₂`, whose Green's function is **Yukawa-screened** (range `√(D/Γ)`) rather than long-range. The physical consequence:

> **Near matter (`Γ` large), the preferred-frame current is screened: the `w^j U_{ij}` response is suppressed by a factor `~ D∇²/(D∇² − Γ)` relative to the conservative value, and the convective `w_i U` term is damped where the field cannot follow the moving hole.** The overdamped khronon cannot build the coherent frame-dependent near-field that `α₁, α₂` measure — exactly the ED-specific suppression Route A's conservative formulas could not represent, now appearing explicitly as the `Γ` term in (★★).

This is the load-bearing non-conservative content: `α₁, α₂` are the conservative `η`-terms of §5 **times a dissipative suppression functional of `Γ`** that the standard khronometric PPN map omits.

## 7. Map to standard PPN, and the Route-A cross-check

Will's PPN metric writes the preferred-frame part of `g_{0i}` as (schematically, exact prefactors per TEGP — *to verify against source, not fabricated here*):

> `g_{0i}^{PF} = −\tfrac{1}{2}(α₁ − 2α₂)\,w_i U − α₂\, w^j U_{ij} + …`

Matching to §5–§6:

- coefficient of `w_i U`:  `−2η · 𝒮₁(Γ) = −\tfrac12(α₁ − 2α₂)` ⟹ **`(α₁ − 2α₂) = 4η\,𝒮₁(Γ)`**;
- coefficient of `w^j U_{ij}`:  `−2η · 𝒮₂(Γ) = −α₂` ⟹ **`α₂ = 2η\,𝒮₂(Γ)`**,

where `𝒮₁, 𝒮₂` are the dissipative suppression functionals (`𝒮 = 1` conservative, `𝒮 → 0` as `Γ → ∞`). Hence `α₁ = 4η(𝒮₁ + 𝒮₂)` and `α₂ = 2η𝒮₂` — **both ∝ `η`, both suppressed by `Γ`.**

**Cross-check with Route A.** Route A gave `α₁ = −4c₁₄` (conservative, `β = 0`). Route B gives `α₁ = 4η(𝒮₁+𝒮₂)` with `𝒮 → 1` conservatively. Consistency requires the metric-assembly normalization to match the khronometric acceleration coupling: **`η ↔ −c₁₄`** (up to the `𝒮₁+𝒮₂` bookkeeping). The two routes therefore pin the *same* single unknown from two directions — a genuine consistency target, not an independent new free parameter. The conservative agreement is the check; the `𝒮(Γ)` factor is the new physics Route B adds.

## 8. What this session establishes

1. **Correct PPN bookkeeping for ED** (§1): the orders of `b, N, g_{μν}`, and the fact that the discarded static term `ḃ` *is* the preferred-frame source.
2. **The expanded field equations to O(v³)** (§4–§6): O(2) static Poisson (recovers `γ = 1`); O(3) convection–diffusion with the convective `w_i U` and diffusive `w^j U_{ij}` structures; and the dissipative (★★) with the screening `Γ`.
3. **Which terms feed `α₁, α₂`** (§5, §7): `α₁` from the convective bandwidth current `wβ₂`; `α₂` from the diffusive anisotropic response `−D∇β₃`; both ∝ the metric-assembly normalization `η`, both multiplied by dissipative suppression `𝒮(Γ)`.
4. **The boost-non-invariance is the engine** (§3): preferred-frame effects are sourced precisely by the rule's first-order-in-cosmic-time structure — the arrow, once more.

## 9. Remaining quantities to compute (later steps)

- **`η` — the metric-assembly normalization** (`g_{0i} = η J_b^i`). Requires the explicit directed-flux derivation of the cross-terms (the deferred §6 of the metric-assembly note). *Must equal `−c₁₄` of Route A — the cross-check.*
- **`𝒮₁(Γ), 𝒮₂(Γ)` — the dissipative suppression functionals.** Solve (★★) at O(3) with the actual `Γ(x)` profile from the P11 reserve drain; extract the screened Green's-function factors. This is the ED-specific content that decides safety.
- **`Γ(x)` — the reserve overdamping profile** in band-fractions (P04/P11). Symbolic here.
- **The standard-PPN prefactors** in §7: verify Will/TEGP `g_{0i}^{PF}` coefficients against the source before reading numbers.
- **Numerical sanity check (only after the above give a ballpark):** a two-body ED simulation drifting at `w` through the cosmic frame, measuring the gravitational anisotropy directly — an `F`-native measurement of `α₁, α₂` that bypasses both the conservative-action assumption *and* the `η`-normalization, closing the loop.

## 10. Verdict (this session)

**Route B is set up correctly and the O(v³) preferred-frame field equations are in hand.** The expansion confirms, from the rule directly: (i) preferred-frame effects are sourced by the rule's boost-non-invariant `ḃ → w·∇b` term; (ii) the conservative theory yields nonzero `α₁, α₂`, both proportional to a single metric-assembly normalization `η` that must equal Route A's `−c₁₄`; (iii) the dissipative reserve enters as an explicit screening term `Γ` that suppresses both parameters near matter — the non-conservative physics the khronometric formulas cannot represent. **The number is not computed and not faked.** What remains is definite: compute `η` (= the Route-A cross-check), the suppression functionals `𝒮(Γ)`, and the reserve profile `Γ`, then evaluate and compare to `|α₁| ≲ 10⁻⁴`, `|α₂| ≲ 10⁻⁷`. The framework now makes each of those a well-posed calculation rather than an open-ended one.

---

*Route B begun: a direct PPN expansion of `ḃ = D∇²b − κρ` (+ dissipative reserve), not the conservative khronometric action. Order counting set (`g_{0i}` at O(v³)); the rule's boost-non-invariance (first-order in cosmic time) identified as the preferred-frame engine; a moving source gives the convection–diffusion equation `D∇²B + w·∇B = κρ₀`, whose O(2) recovers `γ=1` and whose O(3) yields `g_{0i} = −2η(w_iU + w^jU_{ij})` — the convective current feeding `α₁`, the diffusive anisotropic response feeding `α₂`, both ∝ the metric-assembly normalization `η` (= Route A's `−c₁₄`, the cross-check). The dissipative reserve enters as an explicit screening term `Γ` (Yukawa range `√(D/Γ)`) that suppresses both near matter — ED's non-conservative escape, made explicit. Remaining: compute `η`, the suppression functionals `𝒮(Γ)`, and `Γ`; verify the TEGP prefactors; then a moving-binary sim. No corpus edits, no new primitives; Einstein not derived; the numbers deliberately not faked.*
