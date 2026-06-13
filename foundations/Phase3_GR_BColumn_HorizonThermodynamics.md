# Phase-3 GR — B-Column: Horizon Thermodynamics on the Emergent Horizon (`S ∝ A` yes, `T ∝ κ` not yet)

**Foundations measurement — the B-column payoff: with the keystone rule built (#1/#8) and a horizon forming dynamically, do the ED-10/Information thermodynamic scalings appear on it? Not a corpus edit, not a new primitive. Nothing here derives `S = A/4` or the Hawking temperature — coefficients are value-inherited; the *scalings* are measured.**
The ED-10/Information arc established the horizon thermodynamics *structurally, EFE-free* — `S ∝ A` from A1 severance, `T ∝ κ` — with the verdict "numbers wait on the Phase-3 keystone." The keystone now exists and forms a frozen `b → 0` horizon (the first build). This note measures whether that **dynamically-emergent** horizon carries the scalings.
**Crank rail:** measure the scalings; do not tune the model to produce them. An area-law that came back *volume*-scaling, or a temperature that scaled correctly only after fiddling, must be reported as such. Sim: `evaluation/DynamicalBandwidth/dynamical_bandwidth.py` (`horizon_thermo`).

---

## 1. What is measured

On the emergent horizon (the frozen `b → 0` cut), across source strengths giving horizons of radius `r_h ≈ 13–19`:

- **Entropy `S` = the severed-information count.** By A1, the capacity *across* the frozen cut is exactly zero (exact severance), so the hidden degrees of freedom are the **severed adjacency channels** — the edges crossing the `b → 0` surface. Holographic `S ∝ A` *iff* that count scales with the horizon **perimeter** (area, `~ r_h`), not the **enclosed region** (volume, `~ r_h²`).
- **Surface gravity `κ` = `∂_r N` at the horizon** (`N ~ √b`), the proxy for the Hawking temperature `T ∝ κ`. Schwarzschild scaling is `κ ∝ 1/r_h` (smaller horizon hotter — the `T ∝ 1/M` relation).

## 2. Result

| source | `r_h` | `A` (surface edges) | `V` (enclosed) | `A/r_h` | `V/r_h²` | `κ` | `κ·r_h` |
|---|---|---|---|---|---|---|---|
| 2.0 | 13.2 | 76 | 548 | 5.75 | 3.14 | 0.053 | 0.70 |
| 3.0 | 14.9 | 88 | 708 | 5.90 | 3.18 | 0.054 | 0.80 |
| 4.0 | 16.0 | 92 | 812 | 5.77 | 3.19 | 0.054 | 0.86 |
| 6.0 | 17.5 | 100 | 960 | 5.71 | 3.13 | 0.054 | 0.94 |
| 9.0 | 18.8 | 108 | 1124 | 5.74 | 3.17 | 0.054 | 1.02 |

Log-log scaling exponents vs `r_h`:

- **`A`(surface) `~ r_h^{0.96}`** — *area-law*. (`A/r_h` is flat at ≈ 5.8.)
- **`V`(enclosed) `~ r_h^{2.01}`** — the bulk, for contrast (2D disk).
- **`κ` `~ r_h^{0.07}`** — *flat*, **not** `r_h^{−1}`.

## 3. `S ∝ A` — confirmed (holographic, on a dynamical horizon)

The severed-information count tracks the horizon **perimeter** (`r_h^{0.96}`), not the enclosed bulk (`r_h^{2.01}`). The contrast is clean and decisive: **the entropy is a surface quantity, not an extensive one.**

> **The dynamically-emergent horizon carries area-law (holographic) entropy: `S ∝ A`, not `S ∝ V`.** This realizes the ED-10/Information structural claim — *previously argued EFE-free for a posited horizon* — now **on a horizon that the keystone rule formed by its own dynamics.**

Honest reading of *what* this confirms: A1 severance is intrinsically a **surface** phenomenon (capacity-zero *across* a cut → the hidden DOF are the boundary channels), so `S ∝ A` is *half-structural*. What the measurement adds is the non-trivial half: the emergent `b → 0` region is a **clean compact surface** (not fractal or volume-severing — the `r_h^{0.96}` vs `r_h^{2.01}` split proves it), so the severed count genuinely scales as the area. Had the emergent horizon been ragged or volume-filling, `S` would have scaled as `r_h²` and this would have come back *no*. It came back holographic.

## 4. `T ∝ κ ∝ 1/r_h` — not reproduced by the minimal model (located)

The surface gravity is **flat** (`κ ~ r_h^{0.07}`), not the Schwarzschild `κ ∝ 1/r_h`. This is an honest negative, and the cause is locatable:

> In the **minimal elliptic** rule (`ḃ = D∇²b − κρ`), the horizon's transition width — over which `b` climbs from `0` to its ambient value — is set by the **fixed sharing length `D`**, *independent of `r_h`*. So `∂_r√b` at the surface is roughly constant, giving `κ ≈ const`. The Schwarzschild `κ ∝ 1/r_h` requires the transition width to tie to `r_h`, which the minimal elliptic relaxation does not supply.

So the Hawking *scaling* is **not** a property of the minimal model — and tuning `D` to force it would be a retrofit (forbidden). It needs one of: (i) the **full (non-minimal) rule** where the transition structure ties to the horizon scale; (ii) **3D** (the static build's dimensional caveat — the `1/r` profile and its strong-field completion live in 3D, where the surface-gravity structure differs from the 2D log); or (iii) the **hyperbolic strong-field** metric rather than the elliptic relaxation. The entropy result is dimension- and model-robust (it is a counting statement); the temperature scaling is model-specific and the minimal model does not carry it.

## 5. Structural vs contingent

| Item | Verdict |
|---|---|
| emergent horizon = frozen `b→0` cut | **built** (first build) |
| `S` = severed adjacency channels (A1: capacity-zero across the cut) | **structural** (A1) |
| `S ∝ A` (perimeter, `r_h^{0.96}`) not `S ∝ V` (`r_h^{2.01}`) | **measured — holographic, confirmed** |
| emergent horizon is a clean compact surface (not fractal/volume) | **measured** (the surface/bulk split) |
| `T ∝ κ ∝ 1/r_h` (Hawking scaling) | **not reproduced** by the minimal model — `κ ≈ const` |
| cause: fixed sharing length `D` sets a `r_h`-independent transition width | **located** |
| coefficients (`1/4` in `S=A/4`; exact Hawking `T`) | **value-inherited** (G/`ℓ_P`); not computed |
| any structural block | **none** — the temperature is a model limitation, not a block |

## 6. Verdict

**The dynamically-emergent horizon carries area-law (holographic) entropy `S ∝ A` — confirmed; the Hawking temperature scaling `T ∝ 1/r_h` is not reproduced by the minimal model, and the reason is located.** The frozen `b → 0` cut severs adjacency channels on its boundary (A1: exact capacity-zero across the cut), and the count of those channels scales as the horizon **perimeter** (`r_h^{0.96}`), not the enclosed bulk (`r_h^{2.01}`) — a clean, decisive surface-vs-volume contrast that realizes the ED-10/Information `S ∝ A` claim on a horizon the keystone rule *formed dynamically*, not on a posited one. The surface gravity, by contrast, came back **flat** (`κ ~ r_h^{0.07}`, not `1/r_h`): in the minimal elliptic rule the horizon transition width is set by the fixed sharing length `D`, not by `r_h`, so the model does not carry the Hawking scaling — a located limitation (full rule / 3D / hyperbolic strong-field), **not** a structural block, and explicitly **not** retrofitted away.

**The honesty lines.** (i) `S ∝ A` is *half-structural* (A1 severance is a surface cut) and *half-measured* (the emergent horizon is a clean surface — the part that could have failed and did not). (ii) The **coefficients** are value-inherited (`G`, `ℓ_P`) — this measures *scalings*, not `S = A/4` or the Hawking `T` value. (iii) The temperature scaling is a genuine **negative** for the minimal model, reported as such; the entropy result is the robust one because it is a counting statement, dimension- and model-insensitive. **Of the two B-column horizon numbers, the area-law is delivered on the emergent horizon; the Hawking scaling awaits the full/3D rule.**

## 7. Next

1. **The Hawking scaling in 3D / the full rule.** Re-measure `κ` where the transition structure ties to `r_h` (3D `1 − r_s/r`, or the hyperbolic strong-field metric) — does `κ ∝ 1/r_h` emerge?
2. **The entropy coefficient.** `S ∝ A` is measured; the `1/4` is value-inherited via `G = c³ℓ_P²/ℏ` (Paper_027). Confirm the A1-severance count, normalized by the substrate's `ℓ_P`, reproduces `A/4ℓ_P²` in form (the holographic coefficient as a value-inherited statement).
3. **Feed the ED-10/Information arc.** Update its "numbers wait on the keystone" flag: the area-law is now realized on a dynamical horizon; the temperature scaling is located to the full/3D rule.

---

*B-column horizon thermodynamics on the dynamically-emergent horizon. The frozen `b→0` cut carries area-law (holographic) entropy: the severed adjacency-channel count (A1: exact capacity-zero across the cut) scales as the horizon perimeter (`r_h^{0.96}`), not the enclosed bulk (`r_h^{2.01}`) — a clean surface-vs-volume split realizing the ED-10/Information `S∝A` claim on a horizon the keystone formed dynamically, not a posited one. The Hawking temperature scaling `T∝κ∝1/r_h` is NOT reproduced by the minimal elliptic model (`κ≈const`, `r_h^{0.07}`), because the horizon transition width is set by the fixed sharing length `D`, not `r_h` — a located model limitation (needs the full/3D/hyperbolic strong-field rule), not a structural block, and not retrofitted. Coefficients (1/4, exact T) value-inherited; scalings measured. No corpus edits, no new primitives; one B-column number delivered on the emergent horizon, one located.*
