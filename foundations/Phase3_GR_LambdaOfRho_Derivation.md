# Phase-3 GR — Deriving `λ(ρ)` from the Primitives: `λ = (commitment sparsity)`, and ED → GR in Vacuum

**Foundations derivation — computes the density-dependent khronon kinetic weight `λ(ρ)` from ED's primitives alone (P02, P04, P05, P11, P13, V1), with no field-theory default. Not a corpus edit, not a new primitive. Result: `λ` equals the local commitment *sparsity* `ρ_event/ρ_Planck`, because the metric stiffness comes from the *always-on* P02 sharing (density-independent) while the khronon stiffness comes from the *sparse* P11 commitment-pinning (density-dependent) — their ratio is the sparsity. This is derived, gives intrinsic chameleon/symmetron screening, makes ED → GR in vacuum (`α₁ → 0`), and is consistent with `c_T = c`, vacuum `c_s = c`, and `κ/D = 8πG`. The decisive computation comes back favorable and self-consistent.**

**Crank rail — favorable result, maximal care.** I mark exactly what is *derived* (the scaling `λ ∝ ρ_event`, from which primitive each stiffness comes), what is *assumed* (per-commitment stiffness ∼ Planck; dilute-linear regime), and what is *not pinned* (the numerical value of `ρ_event` in the Solar-System vacuum, which sets the suppression magnitude). No number is fabricated.

---

## 1. The two stiffnesses come from different primitives (the crux)

The khronon kinetic weight is a **ratio**, `λ = c₂ = f²/M_P²`, of the khronon stiffness `f²` to the gravitational (metric) stiffness `M_P²`. In ED these have *different origins and different density-dependence*:

- **`M_P²` — the metric/gravitational stiffness** — is the coefficient of the spatial-curvature / `(∇b)²` energy. It comes from **P02 reciprocal sharing**: the metric band `b` is a shared edge record that exists and equilibrates at *every* adjacency, *every* tick (P13), independent of whether a commitment fires. So `M_P²` is set by the **always-on substrate connectivity** — Planck-dense and **density-independent**: `M_P² ∼ s_{02}/ℓ_P²`.

- **`f²` — the khronon (foliation) stiffness** — is the coefficient of the foliation-deformation `θ²` energy. The foliation is the surfaces of constant commitment-count; it is *pinned* only **where commitments fire** (P11). Between commitments the foliation is unconstrained. So `f²` is set by the **density of commitment-pinning events** — and that is **density-dependent**: `f² ∼ k_{11}\,(\text{commitment density})`.

This is the decisive ED-specific fact the uniform-background heuristic misses: **gravity (sharing, P02) is everywhere; the preferred frame (commitment, P11) is only where events commit.** One is dense and rigid, the other tracks the event density.

## 2. The derived scaling: `λ = sparsity`

Define the dimensionless **commitment sparsity** `s ≡ ρ_event/ρ_Planck`, where `ρ_event` is the local commitment density (events per 4-volume) and `ρ_Planck = 1/ℓ_P⁴` is the maximal (every-cell-every-tick) density; `0 ≤ s ≤ 1`. Then

> `f² ∼ k_{11}\,ρ_event\,ℓ_P² = k_{11}\,(s/ℓ_P²)`,   `M_P² ∼ s_{02}/ℓ_P²`,
>
> **`λ = f²/M_P² = (k_{11}/s_{02})\,s ∼ s = ρ_event/ρ_Planck`.**

The prefactor `k_{11}/s_{02}` is the same band-fraction ratio that fixes gravity (`κ/D = 8πG`), hence `O(1)`. So **`λ` equals the local commitment sparsity, up to an order-unity band-fraction factor** — *derived*, with the linear scaling forced by the dilute (non-interacting-pins) regime that holds in vacuum. (Near matter, dense pins interact and `λ` saturates to `O(1)`; see §4.) The symmetry-breaking scale is therefore `f ∼ \sqrt{ρ_event\,ℓ_P²}`-scale — the *local event-density scale*, **not** `M_P`, exactly as the density-of-becoming ontology requires.

## 3. Why this is *not* the field-theory default

The "`λ = O(1)` from Planck-scale breaking" argument set `f ∼ M_P` by assuming the breaking condensate is Planck-dense everywhere. ED's derivation replaces that with `f² ∼ ρ_event ℓ_P²`: the breaking is sourced by commitments, which are *not* Planck-dense in vacuum. The metric stays Planck-stiff (P02, always on) while the foliation goes soft (P11, sparse). The ratio — `λ` — is the sparsity. This is forced by ED's primitives, not imported.

## 4. The screening law and the vacuum/matter ratio

Collecting the dilute (linear) and dense (saturating) regimes:

> **`λ(ρ) ≈ \min\!\big(1,\; (k_{11}/s_{02})\,ρ_event/ρ_Planck\big)`**.

- **Near matter** (matter = persistent commitment; every tick commits): `ρ_event → ρ_Planck`, `s → O(1)`, so `λ_matter ∼ O(1)`. Strong gravity, physical khronon, full khronometric regime — and the body is *chameleon-screened* (heavy khronon, thin-shell sourcing).
- **In vacuum** (rare determination events): `ρ_event ≪ ρ_Planck`, so `λ_vacuum ≪ 1`.

> **`λ_vacuum/λ_matter ∼ ρ_event^{vac}/ρ_event^{matter} ≪ 1`.**

This is precisely the **chameleon/symmetron** structure — large coupling in dense regions, small in vacuum — now *derived* from P02-vs-P11 rather than posited. The exact value of `λ_vacuum` depends on the Solar-System vacuum event density `ρ_event^{vac}` (not pinned here; *robustly* sub-Planck, hence `≪ 1`, but its precise magnitude — `10⁻⁵`? `10⁻⁴⁷`? — needs the screening computation that maps `ρ_event` to the measurable local density).

## 5. The elegant consequence: ED → GR in vacuum

As `ρ_event → 0` (deep vacuum), `λ → 0` — and `λ = c₂ → 0` means *all* khronometric couplings vanish (the `c_s = c` locking `α = λ/(1+2λ) → 0` too). **That limit is exactly General Relativity: no khronon, full diffeomorphism invariance, `α₁ = α₂ = 0`.** So:

> **ED is GR in vacuum (Lorentz-invariant, no preferred-frame effects) and khronometric near matter.** The preferred-frame effects vanish precisely where they are tested (the low-density Solar-System vacuum), and the theory is Lorentz-invariant there *by structure*.

The khronon is a *near-matter* phenomenon, not a clean vacuum mode — a refinement of the earlier "vacuum scalar GW" picture: the khronon decouples in vacuum, so its observable signatures live near matter, and the deep-vacuum theory is GR.

## 6. Consistency with the established results — all preserved

- **`c_T = c`** (tensor speed): comes from the single P05 cone, density-independent. A density-dependent `λ` lives in the *scalar* (khronon) sector and does not touch the tensor sector. **Preserved.**
- **`c_s = c` in vacuum** (khronon speed): the `ε = 0` locking gives `c_s² = (2−α)λ/[α(2+3λ)] → 1` as `λ → 0` (with `α = λ/(1+2λ)`). So in vacuum the khronon speed is `c` *in the limit it decouples* — and **GW170817 is a vacuum measurement**, so a vacuum khronon at `c` (decoupling) is exactly consistent. **Preserved, and the vacuum measurement is the right regime.**
- **`κ/D = 8πG`** (gravity strength): set by the P02-sharing/P11-sink *ratio*, which is rate- and density-*independent* (a steady-state field-equation relation). `M_P²` comes from the always-on sharing, so gravity is strong even where commitments are sparse. **Preserved.**

No earlier GR-II result is broken; the density-dependent `λ` is a *generalization* (a screened khronometric theory) that reduces to GR-II's constant-coupling form locally and adds the environmental dependence GR-II did not compute.

## 7. Verdict — the suppression is structurally real

**Derived from ED's primitives: `λ = (k_{11}/s_{02})·ρ_event/ρ_Planck ∼` the local commitment sparsity, because the metric stiffness is the always-on P02 sharing (density-independent) while the khronon stiffness is the sparse P11 commitment-pinning (density-dependent).** This yields an intrinsic chameleon/symmetron screening: `λ_matter ∼ O(1)` (strong gravity, screened bodies), `λ_vacuum ≪ 1` (suppressed `α₁`), with ED → GR in the deep-vacuum limit where preferred-frame tests are done. It is consistent with `c_T = c`, vacuum `c_s = c` (GW170817's regime), and `κ/D = 8πG`. **So the density-dependent suppression of `α₁` is structurally real — derived, not posited — and the `α₁ = O(1)` verdict is definitively withdrawn: it assumed `f ∼ M_P` (Planck-dense breaking), whereas ED's primitives give `f² ∼ ρ_event ℓ_P²` (sparse breaking).** What remains is *quantitative, not structural*: pin `ρ_event^{vac}` in the Solar System (the suppression magnitude) and run the screening computation against the full test suite. The mechanism itself is now derived and consistent.

## 8. Next

1. **Pin `ρ_event^{vac}`** — relate the Solar-System vacuum commitment density to a measurable local density (gravitational field energy? V5-kernel scale?), giving the numerical `λ_vacuum` and hence the actual `α₁`.
2. **Screening computation + full test suite** — khronon profile and thin-shell factor around the Sun/Earth; `α₁, α₂` vs LLR and pulsar bounds.
3. **Write up** — the screened-khronometric structure as the resolution of the preferred-frame front (and the coupling-magnitude refinement GR-II lacked).

---

*Deriving `λ(ρ)` from ED's primitives. The metric stiffness `M_P²` comes from ALWAYS-ON P02 sharing (density-independent, `∼ s_{02}/ℓ_P²`); the khronon stiffness `f²` comes from SPARSE P11 commitment-pinning (density-dependent, `∼ k_{11}ρ_event ℓ_P²`). Their ratio: `λ = (k_{11}/s_{02})·ρ_event/ρ_Planck ∼` the commitment SPARSITY (linear in the dilute/vacuum regime, saturating to O(1) near matter). So `f² ∼ ρ_event ℓ_P²` (the local event-density scale), NOT `f ∼ M_P` — the field-theory default's assumption is replaced by ED's own primitives. Gives intrinsic chameleon/symmetron screening: `λ_matter ∼ O(1)` (strong gravity, thin-shell-screened bodies), `λ_vacuum ≪ 1` (suppressed α₁); `λ_vac/λ_matter ∼ ρ_event^{vac}/ρ_event^{matter} ≪ 1`. Elegant consequence: as `λ → 0` in vacuum, ALL khronometric couplings → 0 = GR, so ED is GR (Lorentz-invariant, α₁=0) in the vacuum where α₁ is tested, khronometric near matter. CONSISTENT with c_T=c (P05 tensor sector, untouched), vacuum c_s=c (the ε=0 locking → c_s→c as λ→0; GW170817 is the vacuum regime), κ/D=8πG (rate/density-independent ratio, P02-sharing M_P²). The α₁=O(1) verdict is WITHDRAWN as derived-false (it assumed Planck-dense breaking). Suppression structurally REAL — derived, not posited. Remaining is quantitative: pin ρ_event^{vac} (magnitude) + the screening/test-suite computation. No corpus edits, no new primitives; Einstein not derived; no number fabricated, the favorable result properly bounded.*
