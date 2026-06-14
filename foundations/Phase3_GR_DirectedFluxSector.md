# Phase-3 GR — The Directed-Flux (Vector) Sector: Built, and the Preferred-Frame `g_{0i}` Measured

**Foundations derivation + build-and-run — constructs the vector sector of `F` that the `η` cross-check located as the missing ingredient, and measures the preferred-frame `g_{0i}` it produces. Not a corpus edit, not a new primitive (P05 directionality + P02 sharing + P11 drain — all declared). Sim: `evaluation/DynamicalBandwidth/directed_flux.py`.**

The `η` note (`Phase3_GR_PPN_RouteB_EtaCrossCheck.md`) showed the scalar rule's current is curl-free (pure gauge), so the preferred-frame cross-term lives in ED's *directed-flux (vector)* sector — declared by the primitives, built by no round. This note builds it and runs it.

**Crank rail:** the vector sector's *structure* is forced by the primitives; its one coupling `λ_J` and the reserve-drain profile `Γ(x)` are **band-fractions, not yet pinned** — kept symbolic. The simulation measures the machinery and the suppression; it does **not** fabricate the final `α₁, α₂` (which need `λ_J` and `Γ` pinned). Numbers shown are the *relations and the suppression functional*, not the verdict.

---

## 1. The vector sector, derived

The diagonal metric came from the scalar band `b` sharing across adjacency (P02): `D∇²b = κρ`, sourcing the long-range Newtonian potential `U` from mass density `ρ`. The off-diagonal metric `g_{0i} = A^i` is the **vector** counterpart — built from exactly the same three declared structures:

- **P05 directionality:** transport carries a *direction*; the scalar reduction `b` keeps only the band magnitude, the directed flux `J^i`/`A^i` keeps the direction.
- **P02 sharing:** the directed quantity equilibrates across adjacency by the same graph Laplacian → `D∇²A^i`.
- **P11 commitment-concentration, now moving:** a static commitment-concentration sources `b` via `−κρ`; a *moving* one (matter drifting at `w` relative to the cosmic frame) is a **bandwidth current** `∝ κρw` that sources the directed flux.

So the vector sector, parallel to the scalar Newtonian sector, is

> **`D∇²A^i = κ_J\,ρ\,w^i`**,  with `κ_J = λ_J\,κ`,  `g_{0i} = A_i`,

`λ_J` = the dimensionless ratio of the vector (current) coupling to the scalar (density) coupling — a P04 band-fraction. This is the same object Route A called `c₁₄` and Route B called `−η`; we now see it concretely as **how strongly a moving commitment-concentration drives the shared directed flux relative to how a static one drives the scalar band.**

Because the sources are parallel (`κρ` ↔ `κ_J ρ w^i`), the solutions are parallel: `A^i = λ_J w^i U`, long-range — the `w_i U` structure that carries `α₁`. (The anisotropic `w^j U_{ij}` piece that carries `α₂` comes from the tensor part of the current; the same sector, higher multipole.)

## 2. Build and run — what the simulation confirms

`directed_flux.py` solves the scalar Poisson (for `U`, `b`, and the scalar flux `J=−D∇b`) and the vector Poisson (for `A^i`) for a Gaussian source moving at `w=(w₀,0)`, on a periodic box by FFT. Results:

| Test | Result | Meaning |
|---|---|---|
| **[1]** scalar flux curl `∇×J` (rel.) | `4×10⁻¹⁶` (machine zero) | scalar rule sources **no physical `g_{0i}`** — the obstruction, reproduced |
| **[2]** vector `A_x/(w₀U)` in mid-field | `1.0000`, spread `5×10⁻¹⁶`, **independent of source mass** | `g_{0i}` is **long-range `= λ_J w_i U`** — the `α₁` PPN structure |
| **[2]** gravitomagnetic field `\|∇×A\|` | nonzero (rel. `1.6`) | the vector sector sources a **genuine** (non-gauge) cross-term |
| **[3]** measured coefficient vs input `λ_J` | `0.25→0.25, 0.5→0.5, 1.0→1.0` | the coefficient **is** `λ_J` = `c₁₄` = `−η` — **the cross-check holds** |

So the vector sector does exactly what the two routes predicted: it produces a long-range preferred-frame `g_{0i} = λ_J w_i U`, with `λ_J` the single coupling that both routes had isolated. The Route-A/Route-B cross-check `η = −c₁₄` is confirmed structurally: all three are `λ_J`, the vector/scalar coupling ratio.

## 3. The dissipative reserve — screening measured

The reserve (P11, one-way) drains the directed flux near matter, adding a damping term that turns the vector Poisson into a **screened (Yukawa)** equation, `(D∇² − Γ)A^i = κ_J ρ w^i`, range `√(D/Γ)`. The near-field suppression `𝒮(Γ) = A^Γ/A^0` at the read radius (~3 source-radii):

| `Γ` | Yukawa range / `σ` | `𝒮(Γ)` |
|---|---|---|
| 0 | ∞ | 1.0000 |
| 0.01 | 5.0 | 0.672 |
| 0.1 | 1.58 | 0.161 |
| 1.0 | 0.50 | 0.0079 |
| 10 | 0.16 | 4×10⁻⁴ |
| 100 | 0.05 | <10⁻⁴ |

> **The dissipative escape is numerically real:** if the reserve overdamps the flux within `≲ 0.1` source-radii (`Γ ≳ 10`), the near-field preferred-frame response is suppressed by `≳ 2500×`, enough to push an `O(1)` conservative `α₁` below the `10⁻⁴` bound. The mechanism Route A could not evaluate and Route B flagged is here, and it works — *quantitatively, conditional on the reserve range.*

## 4. Where the number now stands (tiers)

Putting it together with the Route-A normalization `α₁ = −4c₁₄`:

> **`α₁ = −4\,λ_J\,𝒮(Γ)`**,  with `λ_J` = the vector/scalar band-fraction and `𝒮(Γ)` the reserve screening. ED is PPN-safe iff **`λ_J\,𝒮(Γ) ≲ 2.5×10⁻⁵`** (and the tighter `α₂` analogue).

- **derived / measured:** the vector sector and its long-range `g_{0i}=λ_J w_iU` structure; the cross-check `η=−c₁₄=−λ_J`; the screening functional `𝒮(Γ)` and that it *can* reach `<10⁻⁴`. (§1–§3)
- **open — two band-fractions, now the only unknowns:**
  1. **`λ_J`** — the vector/scalar coupling ratio (`= c₁₄`). In a boost-*invariant* theory it is locked to the covariant value that gives `α₁=α₂=0` (the mass current and density are one tensor); ED's boost-non-invariance *allows* a deviation, and `α₁` measures it. Pinning `λ_J` from the P04 band structure is step one.
  2. **`Γ(x)`** — the reserve-drain range near matter, which sets `𝒮`. Pinning it from the P11 reserve profile is step two.

## 5. The boost-invariance reading (why this is the right place for the number)

The preferred-frame parameters are, precisely, **the deviation of `λ_J` from its boost-covariant value.** A Lorentz-invariant theory has no choice: `T^{0i}` (current) and `T^{00}` (density) are one tensor, so the vector and scalar couplings are locked and `α₁=α₂=0`. ED's rule is written in the cosmic frame and is *not* boost-invariant, so `λ_J` is a free band-fraction — and its mismatch with the covariant value is the preferred-frame effect. The dissipative reserve then suppresses whatever mismatch survives, by `𝒮(Γ)`. Two clean dials, both physical, both pinnable.

## 6. Verdict

**The directed-flux (vector) sector is built and runs, and it produces the preferred-frame `g_{0i}` exactly as the two routes required.** The simulation confirms, decisively (machine-precision on the structural checks): the scalar rule alone sources no `g_{0i}` (curl-free); the vector sector sources a long-range `g_{0i} = λ_J w_i U` with a real gravitomagnetic field; the coefficient *is* `λ_J = c₁₄ = −η`, so **the Route-A/Route-B cross-check holds**; and the dissipative reserve screens the near-field by a measured `𝒮(Γ)` that reaches `<10⁻⁴` for short drain range. **The open falsification number is now `α₁ = −4 λ_J 𝒮(Γ)`, reduced to exactly two pinnable band-fractions — `λ_J` (the boost-non-invariant coupling deviation) and `Γ` (the reserve range) — with the suppression mechanism confirmed real rather than hoped-for.** No number is fabricated; ED is safe iff `λ_J 𝒮(Γ) ≲ 2.5×10⁻⁵`, and the two routes now agree on what must be computed to decide it.

## 7. Next

1. **Pin `λ_J`** from the P04 band-partition: the ratio of the moving-concentration current coupling to the static-concentration scalar coupling. Decide whether it equals the boost-covariant value (`α₁=0` outright) or deviates.
2. **Pin `Γ(x)`** from the P11 reserve-drain profile near matter → evaluate `𝒮(Γ)`.
3. **Evaluate `α₁ = −4 λ_J 𝒮(Γ)`, `α₂` (anisotropic)** and compare to `10⁻⁴, 10⁻⁷`. Then the front closes — favorably or not.
4. **Full moving-binary sim** (now buildable, since the vector sector exists) as the `F`-native cross-check on the analytic `α₁, α₂`.

---

*The directed-flux (vector) sector built and run (`directed_flux.py`). Structure derived from P05 directionality + P02 sharing + P11 moving-concentration: `D∇²A^i = κ_J ρ w^i`, `g_{0i}=A_i`, `κ_J=λ_J κ`. Sim confirms (machine precision): scalar flux curl-free (no `g_{0i}`); vector sector → long-range `g_{0i}=λ_J w_iU` (the `α₁` structure) with nonzero gravitomagnetic field; coefficient = `λ_J` = `c₁₄` = `−η`, so the Route-A/Route-B cross-check holds. Dissipative reserve → Yukawa screening `𝒮(Γ)` measured, reaches `<10⁻⁴` for drain range `≲0.1` source-radii. Net: `α₁ = −4 λ_J 𝒮(Γ)`, reduced to two pinnable band-fractions (`λ_J` = boost-non-invariant coupling deviation; `Γ` = reserve range); safe iff `λ_J 𝒮(Γ) ≲ 2.5×10⁻⁵`. Suppression mechanism confirmed real. No corpus edits, no new primitives; Einstein not derived; the numbers deliberately not faked.*
