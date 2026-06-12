# Phase-3 GR — Round 9: The Field Equation, and the Burden-of-Proof Inversion

**Foundations derivation attempt — the arc's capstone. Not a rule proposal, not a corpus edit, not a new primitive. This does NOT claim to derive the Einstein field equations; it shows what would force them and reduces the open problem to a single, sharp residual.**
Rounds 1–8 built the metric, forced covariance, identified matter conservation with geodesic motion, and decided the weak-field fork (Einstein, with the factor of 2 and redshift derived). Round 9 attacks the last keystone: the field equation `G^μν = κT^μν`. The result is not a brute-force tensor computation but a **uniqueness argument** — and an inversion of the burden of proof.
**Crank rail:** this is the round most able to over-claim ("ED derives Einstein!"). It will not. Lovelock's theorem gives a *conditional*, and the one unmet condition is named and load-bearing.

---

## 1. What the field equation *is*, in ED

In ED the metric is built from bandwidth (`g ~ b⁻¹`, `N² ~ b`), and the source from event density and its flux (`T^μν = ρu^μu^ν`, R6). So "the field equation" is the **(steady-state) law relating the bandwidth configuration to the matter it carries** — concretely, a relation between *second derivatives of `b`* (curvature) and *`ρ`/`T`* (source). This is precisely the steady-state of the admissible **dynamical-bandwidth rule** (R2): `ḃ = F(ρ, ∇ρ, b)`. The field equation and the bandwidth dynamics are the same object.

Its **Newtonian limit is already in hand** (R1: ED reproduces Poisson). With `g_00 = −N² ~ −b ≡ −(1+2Φ)`, Poisson `∇²Φ = 4πGρ` reads, in bandwidth variables,

> `∇² b ~ ρ`   (the bandwidth Laplacian sourced by event density).

This is **second-order in `b`** (hence in the metric) and linear in the source — a fact we will need.

## 2. The weak-field metric is now fully derived

Combining the pieces, the weak-field metric is no longer imposed:

- `∇²b ~ ρ` (R1) gives the **profile**: in vacuum `∇²b = 0 ⟹ b = 1 − r_s/r` (the `1/r` Schwarzschild profile, `r_s ∝ M`).
- `N² ~ b` and `g_00 g_rr ~ −1` (R8) give the **relation** between the components.

Together: `g_00 = −(1 − r_s/r)`, `g_rr = (1 − r_s/r)⁻¹` — the **weak-field Schwarzschild metric, derived**. So ED reproduces *all three* classical tests (light bending with the factor of 2, redshift, and — via timelike geodesics in this metric — perihelion precession) at the weak-field level, with the profile now coming from the Newtonian bandwidth law rather than being assumed. **What remains is the full, nonlinear, all-components field equation.**

## 3. The Lovelock argument — the field equation is *forced*, conditionally

Rather than computing `G^μν` from `b` by hand, use the uniqueness theorem that makes Einstein inevitable. **Lovelock's theorem (4D):** the *only* symmetric rank-2 tensor that is (i) built solely from the metric and its derivatives, (ii) of second differential order, linear in the second derivatives, (iii) identically divergence-free, is

> `a·G^μν + b·g^μν` — the Einstein tensor plus a cosmological term.

So *any* metric theory meeting (i)–(iii) in 4D has the field equation `G^μν + Λg^μν = κT^μν`. Check ED against the conditions:

| Lovelock condition | ED status |
|---|---|
| 4D spacetime | ✓ (assembled metric, R4/R8) |
| symmetric rank-2 source, **divergence-free** | ✓ `T^μν=ρu^μu^ν`, `∇·T=0` (R5/R6) — and `∇·G=0` free (R4) |
| **second-order, linear in 2nd derivatives** | ✓ at Newtonian order (`∇²b~ρ`); the rule `F(ρ,∇ρ,b)` introduces no higher metric derivatives |
| built **solely from the metric** (no extra field) | **the open condition — §4** |

Three of the four conditions are met by results already banked. **If the fourth holds, the field equation is *forced* to be Einstein (with Λ) — no further computation required.** This is the legitimate way to reach `G=κT`: not by deriving the tensor, but by showing ED satisfies the hypotheses that make it the *only* possibility.

## 4. The residual: a degrees-of-freedom count

The one open Lovelock condition — "built solely from the metric, no extra field" — is the whole remaining question, and it is sharp:

- **If ED's gravity is *purely metric*** (the bandwidth `b_ij` carries exactly the metric's degrees of freedom and no more), Lovelock forces **Einstein**.
- **If `b` carries an *extra scalar* degree of freedom** beyond the metric, the theory is **scalar-tensor** (Brans–Dicke-like): Einstein plus a scalar, *not* pure GR.

There is evidence on **both** sides, which is why it is genuinely open:

- *Toward purely-metric (Einstein):* bandwidth is **per-edge — directional** (R6), so `b_ij` is a genuine rank-2 tensor with the full tensor structure, in principle carrying the metric's two propagating (gravitational-wave) polarizations — not a single scalar. A single-scalar `b` would be Nordström-like; the per-edge structure escapes that.
- *Toward an extra scalar (scalar-tensor):* the lapse and spatial metric are *both* tied to `b` (`N²~b`, `g~b⁻¹`), which looks like a constraint linking components — and if the *trace/magnitude* of `b` propagates independently of its tensor part, that propagating scalar is exactly the extra degree of freedom that makes it scalar-tensor.

So the entire EFE-emergence question now reduces to a **mode count**: *do the propagating degrees of freedom of the per-edge bandwidth field `b_ij` match the metric's (→ Einstein) or exceed them by a scalar (→ scalar-tensor)?* That is a well-posed, possibly-decidable question about the bandwidth field's linearized dynamics — not a vague "derive Einstein."

## 5. The coefficient κ

Lovelock fixes the *form*; the coefficient `κ` is fixed by matching the Newtonian limit `∇²Φ = 4πGρ ⟹ κ = 8πG`. Newton's `G` is the bandwidth→metric conversion constant — a **global relational constant**, value-inherited (Facts paper), not derived. So `κ = 8πG` with `G` inherited, exactly as ED treats all constants. The cosmological `Λ` is the V1-backreaction term (R1). Neither value is chased; both are inherited, as the program's stance requires.

## 6. Structural vs contingent

| Item | Verdict |
|---|---|
| weak-field Schwarzschild metric | **derived** (`∇²b~ρ` profile + R8 relation) |
| three classical tests (bending/redshift/precession) | **derived** at weak field |
| field-equation **form** `G+Λg=κT` | **forced by Lovelock** — *if* §4 (purely metric) holds |
| 4D, div-free source, 2nd-order | **met** (R5/R6, R1) |
| **purely-metric (no extra scalar)** | **the open residual** — a mode count (R10) |
| coefficient `κ=8πG`, `Λ` | **fixed up to value-inherited constants** |
| `α=1` (reserve independence, R8) | still assumed; folds into the mode structure |
| strong-field / explicit nonlinear solutions | **not checked** (Lovelock gives the form, not the solutions) |
| any structural block | **none found across the whole arc** |

## 7. ED ↔ GR structure map (final, through Round 9)

| GR object | ED structure | status |
|---|---|---|
| metric `g_μν` | `g~b⁻¹`, `N²~b` | weak-field Schwarzschild **derived** |
| `∇·G=0`, `∇·T=0` | Bianchi free; bandwidth-current conserved | **both ✓** (R4/R5/R6) |
| geodesics | front = Fermat null geodesics | **✓** (R7) |
| weak-field tests | bending ×2, redshift, precession | **derived** (R7/R8/R9) |
| field equation `G+Λg=κT` | bandwidth field law `∇²b~ρ` + Lovelock | **forced iff purely metric (R9)** |
| Einstein vs scalar-tensor | mode count of `b_ij` | **the one residual (R10)** |

## 8. Verdict — the burden of proof is inverted

**The arc has turned the question around.** It began (R1) as *"can ED support EFE emergence?"* — an open, locate-the-obstruction problem. It ends (R9) as *"is there anything preventing ED from being Einstein?"* — and the only candidate is a single extra scalar degree of freedom. Concretely: ED has a genuine 4D metric, a covariantly-conserved rank-2 source, a second-order field law (Newtonian-confirmed), and the weak-field Schwarzschild metric with all three classical tests derived. By **Lovelock's theorem**, those facts *force* the field equation to be `G^μν + Λg^μν = κT^μν` — **unless** the bandwidth field smuggles in a propagating scalar, in which case ED is scalar-tensor (Einstein + a scalar). So the entire "big E" reduces to one sharp, well-posed **mode count**: do the propagating degrees of freedom of the per-edge bandwidth `b_ij` match the metric (Einstein) or exceed it by a scalar (scalar-tensor)?

This is the strongest honest statement the arc can make, and it deliberately stops short of "ED derives Einstein." It does **not**: Lovelock is conditional, the deciding condition is unproven, strong-field solutions are unchecked, and the `α=1` reserve reading still underpins the lapse. But the residual is no longer a wilderness — it is **one decidable question**, and the prior is now that Einstein is *forced* unless a specific extra structure (a propagating bandwidth scalar) is found. **No structural block appeared anywhere in Rounds 1–9. The big E is reduced to a degrees-of-freedom count — and the burden has shifted from "show ED can be Einstein" to "show what, if anything, stops it."**

## 9. Round-10 questions (the residual, and beyond)

1. **The mode count (the last question).** Linearize the per-edge bandwidth dynamics `ḃ_ij = F` about a background; count the propagating degrees of freedom. Two transverse-traceless tensor modes only → **Einstein** (Lovelock closes). An extra propagating scalar (the trace/magnitude of `b`) → **scalar-tensor**, and characterize it (Brans–Dicke `ω`?).
2. **`α = 1` from the band law.** Confirm the commitment-reserve does not co-scale with `b_int`, closing R8's assumption.
3. **Strong field.** Beyond Lovelock's structural result, check explicit strong-field behavior: does `b → 0` give the Schwarzschild horizon (R4 §6 unification: `b→0` = metric degeneration = A2 cut = V5 horizon)?
4. **Gravitational waves.** If purely metric, ED should carry exactly two GW polarizations — a concrete, simulable signature of the Einstein branch.

---

*Round-9 capstone. Verdict: the weak-field Schwarzschild metric is **derived** (`∇²b~ρ` profile + R8 relation; three classical tests follow), and by **Lovelock's theorem** the full field-equation *form* `G^μν+Λg^μν=κT^μν` is **forced** — given that ED meets the 4D / divergence-free-source / second-order conditions (it does, R1/R5/R6) and is **purely metric**, the one open condition. The residual is therefore a single, well-posed **degrees-of-freedom count**: do the per-edge bandwidth modes match the metric (Einstein) or carry an extra scalar (scalar-tensor)? `κ=8πG` and `Λ` are fixed up to value-inherited constants. No corpus edits, no new primitives, no structural block in Rounds 1–9. **This does not derive the Einstein equations** — it inverts the burden of proof: Einstein is now forced unless a propagating bandwidth scalar exists, reducing the whole "big E" to one decidable question.*
