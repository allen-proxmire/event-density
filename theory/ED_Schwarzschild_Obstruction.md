---
title: "ED Acoustic Metric vs Schwarzschild — Coordinate-Equivalence Obstruction"
status: Working memo (scoping study)
date: 2026-04-22
scope: Can any ED background ρ₀(x) reproduce Schwarzschild via coordinate transformation of the effective acoustic metric?
---

# ED Acoustic Metric vs Schwarzschild: Coordinate-Equivalence Scoping

## 0. Question and one-line verdict

**Question.** Given the ED acoustic metric
`g^eff_μν = diag(−M(ρ₀(x)), 1, 1, 1)`
derived in `ED_Effective_Acoustic_Metric.md`, does there exist a choice of
background `ρ₀(x)` (including spherically-symmetric `ρ₀(r)`) and a
diffeomorphism `x → y` such that `g^eff` becomes Schwarzschild
`ds² = −f(r)dt² + f(r)⁻¹dr² + r²dΩ²`, `f = 1 − 2GM/r`?

**Verdict.** **No.** Three coordinate-invariant obstructions rule this out:

- **(A)** ED acoustic metric has a **flat Euclidean spatial 3-section**
  (intrinsic `³R_ij = 0`); Schwarzschild's spatial section is intrinsically
  curved.
- **(B)** The only ED profile making the full Ricci tensor vanish is
  `N(r) = const` (Minkowski). No non-trivial Ricci-flat ED acoustic
  background exists.
- **(C)** The ED Kretschmann scalar `K = 4(N″² + 2N′²/r²)/N²` cannot be made
  functionally equal to `K_Schw = 48(GM)²/r⁶` while simultaneously enforcing
  Ricci-flatness.

This sharpens `ED_Acoustic_Metric_Curvature.md` §9C from "not
Schwarzschild-like in these coordinates" to "not Schwarzschild in any
coordinates."

---

## 1. Invariant criteria for Schwarzschild

A metric is locally Schwarzschild iff it satisfies:

1. **4D Lorentzian.**
2. **Static and spherically symmetric.**
3. **Ricci-flat:** `R_μν = 0` (vacuum Einstein).
4. **Non-trivial Riemann:** Kretschmann `K = R_{abcd}R^{abcd} = 48(GM)²/r⁶`.
5. **Asymptotically flat** with ADM mass `M`.
6. **Horizon at `r = 2GM`** with surface gravity `κ = 1/(4GM)`.

Any coordinate transformation preserves (1)–(6). So if ED can match these as
invariants, a coordinate transformation might find Schwarzschild form. If it
fails even one invariant, no coordinate change helps.

---

## 2. Setup: ED acoustic metric with spherical profile

Take `ρ₀` spherically symmetric: `ρ₀ = ρ₀(r)`, `r = √(x²+y²+z²)`. Let
`N(r) ≡ √M(ρ₀(r))` so `c_s(r) = N(r)`. In spherical spatial coordinates:

```
ds² = −N(r)² dt² + dr² + r²(dθ² + sin²θ dφ²)
```

Metric components:

```
g_tt = −N²(r),   g_rr = 1,   g_θθ = r²,   g_φφ = r² sin²θ
```

ED inherits the Euclidean background's spherical coordinate warping
(`r²dΩ²`), but `g_rr = 1` — **the spatial 3-section is flat Euclidean, only
expressed in spherical coordinates.**

---

## 3. Direct coordinate-match attempt

Try `r → R(r)` and match to Schwarzschild `(T,R,θ,φ)` form:

| Component | Schwarzschild | ED transformed |
|---|---|---|
| `g_TT` | `−f(R) = −(1 − 2GM/R)` | `−N²(r(R))` |
| `g_RR` | `f(R)⁻¹ = (1 − 2GM/R)⁻¹` | `(dr/dR)²` |
| `g_θθ` | `R²` | `r(R)²` |

Three simultaneous equations for one unknown `r(R)`:

- (i) `N²(r(R)) = 1 − 2GM/R`
- (ii) `(dr/dR)² = (1 − 2GM/R)⁻¹`
- (iii) `r(R) = R`

**(iii) forces `dr/dR = 1`. (ii) demands `dr/dR = (1 − 2GM/R)⁻¹/² ≠ 1`.
Contradiction.**

Allowing time rescaling `t → aT + h(r)` doesn't help: the Schwarzschild
radial coordinate is already the *areal* radius (`g_θθ = R²`), so (iii) is
forced — any diffeomorphism relabeling `r` must preserve the transverse
area or introduce off-diagonal terms that break staticity.

Any valid coordinate change would preserve the curvature invariants of
§4–§6 below. Those invariants already disagree, so a more clever
diffeomorphism cannot save the match.

---

## 4. Invariant obstruction A: Ricci tensor

For `ds² = −N(r)² dt² + dr² + r²dΩ²`, the Ricci components are:

```
R_tt = N(N″ + 2N′/r)
R_rr = −N″/N
R_θθ = −rN′/N
R_φφ = sin²θ · R_θθ
```

**Ricci-flatness requires all four to vanish:**

- `R_rr = 0` ⇒ `N″ = 0`
- `R_θθ = 0` ⇒ `N′ = 0`

Hence `N = const`, i.e. **flat Minkowski** (trivially).

> **No non-trivial ED acoustic background is Ricci-flat.**

Schwarzschild is Ricci-flat *and* non-Minkowski. The two are mutually
exclusive in ED's acoustic class.

This is a true coordinate invariant: `R_μν R^{μν} ≥ 0` with equality iff
`R_μν = 0`, and both hold as scalars under any diffeomorphism.

---

## 5. Invariant obstruction B: intrinsic 3-curvature

The constant-`t` hypersurface of the ED acoustic metric has induced metric

```
ds²_{(3)} = dr² + r²(dθ² + sin²θ dφ²)
```

This is **flat Euclidean** `R³`. Intrinsic Riemann, Ricci, scalar curvature
all vanish.

Schwarzschild's `t = const` slice has

```
ds²_{(3)}^Schw = f(r)⁻¹ dr² + r²dΩ²
```

Intrinsic Ricci scalar `³R = 2·2GM/(r³(r − 2GM))` ≠ 0 (except at infinity).

> **Diffeomorphisms preserve intrinsic 3-curvature. Flat `R³` cannot
> become Schwarzschild's curved 3-section under any coordinate change.**

(The isotropic-coordinate form of Schwarzschild has a *conformally* flat
3-section, not a flat one — conformal flatness is strictly weaker. Every
3-manifold is conformally flat; intrinsic curvature still lives in the
conformal factor.)

---

## 6. Invariant obstruction C: Kretschmann scalar

The only nonzero Riemann components (up to symmetries) for the ED
spherically-symmetric acoustic metric are:

```
R_{trtr} = N N″
R_{tθtθ} = r N N′
R_{tφtφ} = r sin²θ · N N′
```

All purely spatial Riemann components vanish (spatial section is flat).

Kretschmann:

```
K_ED = (4/N²)·[N″² + 2 N′²/r²]
```

Schwarzschild:

```
K_Schw = 48 (GM)² / r⁶
```

To match `K_ED = K_Schw` across all `r` we'd need a specific `N(r)`
satisfying

```
N″² + 2N′²/r² = 12(GM)² N² / r⁶
```

This non-linear ODE admits solutions, but the same `N(r)` must *also*
satisfy Ricci-flatness (`N′ = N″ = 0`) per §4 — which forces `N = const`,
giving `K_ED = 0 ≠ K_Schw`.

> **No `N(r)` satisfies the three invariants simultaneously.**

---

## 7. What ED *can* achieve in this class

These are the interesting fallbacks, useful to state precisely:

### 7A. Ricci-scalar-flat: `N(r) = 1 − A/r`

Setting `(r²N′)′ = 0` gives `N = B − A/r`. Asymptotic flatness picks `B = 1`:

```
N(r) = 1 − A/r,   g_tt = −(1 − A/r)²,   g_rr = 1
```

- **Ricci scalar `R = 0`** ✓
- **Ricci tensor `R_μν ≠ 0`** ✗
- Kretschmann `K_ED = 4(N″² + 2N′²/r²)/N² = 4·(4A²/r⁶ + 2A²/r⁴) / (1 − A/r)²`
  is finite, not Schwarzschild-form.
- Horizon at `r = A` where `g_tt → 0`; acoustically extremal (§7C of
  `ED_Acoustic_Metric_Curvature.md`).

This is the **closest** ED gets to Einstein vacuum — only the trace
matches. Geometrically it is *not* Schwarzschild: it has `g_tt = −(1 −
A/r)²` rather than `−(1 − 2GM/r)`, and `g_rr = 1` rather than
`(1 − 2GM/r)⁻¹`.

### 7B. Rindler: `M(x) ∝ x²`

In 1D profile `M(x) = A(x − x₀)²`, the (t,x) block is Rindler, a coordinate
chart of flat 4D Minkowski. Zero curvature. Not Schwarzschild.

### 7C. The (t,r) block alone

If we discard the transverse 2-sphere and look only at the (t,r) block,
any 2D Lorentzian metric is conformally flat, so any ED `M(r)` can be
mapped to Schwarzschild's (t,r) block by a 2D diffeomorphism plus
conformal rescaling. **But the failure of §5 and §6 is *entirely* about
the transverse geometry — throwing it away begs the question.**

---

## 8. Why this fails structurally, not just technically

The three obstructions aren't accidents of the specific derivation in
`ED_Effective_Acoustic_Metric.md` — they follow from the *kinematic*
character of ED's emergent metric:

1. **ED has no tensor DOFs.** The acoustic metric is built from a single
   scalar `c_s²(x) = M(ρ₀(x))`. Schwarzschild's geometry carries six
   independent metric functions (two after symmetry reduction). You
   cannot fit two independent `f(r)` and `f(r)⁻¹` into one scalar profile
   without introducing extra structure.

2. **Background spatial topology is Euclidean.** ED fluctuations live on
   `R³`. The acoustic metric inherits this flat spatial substrate. All
   known ways to generate curved spatial sections in analog gravity
   require either (i) non-trivial flow `v₀ ≠ 0` (Painlevé-Gullstrand
   form), (ii) anisotropic mobility tensor `M^{ij}(ρ)` instead of
   scalar `M(ρ)`, or (iii) a different kinematic construction entirely.
   None of these are in canonical ED.

3. **No dynamical equation for `g^eff`.** Schwarzschild is a *solution of
   Einstein's equation* `R_μν = 0`, sourced by the choice of ADM mass.
   ED's `g^eff` is *constructed* from a chosen `ρ₀`; there's no
   equation-of-motion that selects Schwarzschild as the
   spherically-symmetric vacuum.

4. **Mobility capacity bound `M ≥ 0`.** Architectural Canon P4 requires
   `M(ρ)` non-negative with collapse at `ρ*`. Schwarzschild has
   `g_tt = −(1 − 2GM/r)` that *changes sign* inside `r < 2GM` — this is
   the interior region where `t` becomes spacelike. In ED, `M < 0` is
   forbidden, so the *interior* of a Schwarzschild black hole has no
   ED correspondent.

---

## 9. Invariant comparison table

| Property | Schwarzschild | ED acoustic metric (`ρ₀(r)`) |
|---|---|---|
| Dimension | 4D | 4D ✓ |
| Lorentzian signature | (−,+,+,+) | (−,+,+,+) ✓ |
| Static | Yes | Yes (for `v₀ = 0`) ✓ |
| Spherical symmetry | Yes | Yes ✓ |
| Spatial 3-section | Curved (`³R ≠ 0`) | **Flat Euclidean** ✗ |
| Ricci tensor | `R_μν = 0` | `R_μν ≠ 0` unless `N = const` ✗ |
| Ricci scalar | `R = 0` | Can be `0` (for `N = 1 − A/r`) |
| Kretschmann | `48(GM)²/r⁶` | `4(N″² + 2N′²/r²)/N²` |
| Horizon structure | Bifurcate, `κ = 1/(4GM)` | Boundary/capacity, generically extremal |
| Interior (`M < 0`) | Well-defined | **Forbidden by P4 capacity** ✗ |

---

## 10. Verdict and implication for ED-10

**No ED background `ρ₀(x)` can produce a Schwarzschild-equivalent metric
via coordinate transformation of the canonical acoustic metric
`g^eff_μν = diag(−M, 1, 1, 1)`.**

The obstruction is coordinate-invariant and operates at three
independent levels (flat 3-section, Ricci-tensor mismatch, Kretschmann
form). This is not a near-miss; it is a structural incompatibility.

### 10A. What this closes

- Casual claims that ED-10 reproduces black-hole geometry
  "automatically" as a large-scale summary of gradients.
- Any program that derives Hawking radiation, BH thermodynamics, or
  event-horizon area law from ED's canonical reversible-sector metric
  without further ingredients.

### 10B. What this leaves open (for a possible future program)

If one *wanted* ED to reach Schwarzschild-type geometries, the minimal
additions are:

- (i) **Anisotropic mobility tensor** `M^{ij}(ρ)` replacing the scalar
  `M(ρ)` — would give spatial-metric anisotropy enough to break flat-
  section degeneracy.
- (ii) **Background flow** `v₀(x) ≠ 0` — standard analog-gravity
  Painlevé-Gullstrand route, but requires justifying steady-state flow
  in ED.
- (iii) **Dynamical equation for `g^eff`** — e.g. promoting `M(ρ)` to
  respond to a Newtonian-type `∇²Φ = source`. This would effectively
  import Einstein's equations from outside ED.

All three are additions to — not derivations from — ED canon. They
should be explicitly scoped as extensions, not presented as implicit
consequences of P1–P7.

### 10C. Recommended orientation-doc update

Update ED-10 language to reflect this closed question. Suggested line:

> *ED-10 (revised scope, 2026-04-22):* ED's canonical reversible-sector
> fluctuations live on an effective acoustic metric `g^eff = diag(−M,
> 1, 1, 1)` whose spatial section is flat Euclidean and whose Ricci
> tensor vanishes only in the trivial Minkowski limit. Einstein's
> equations are **not** an implicit consequence of ED gradients at
> large scale; the acoustic metric is (ii)-grade kinematic geometry,
> not dynamical spacetime. Reproducing Schwarzschild-type backgrounds
> would require structural extensions beyond canonical ED (anisotropic
> mobility, background flow, or a dynamical metric equation).

---

## Appendix A. Ricci and Riemann for `ds² = −N²dt² + dr² + r²dΩ²`

**Christoffels (non-zero):**

```
Γ^t_{tr} = N′/N,     Γ^r_{tt} = N N′
Γ^r_{θθ} = −r,       Γ^r_{φφ} = −r sin²θ
Γ^θ_{rθ} = Γ^φ_{rφ} = 1/r
Γ^θ_{φφ} = −sinθ cosθ,  Γ^φ_{θφ} = cotθ
```

**Riemann (non-zero up to symmetries):**

```
R^t_{rtr} = −N″/N       ⇒ R_{trtr} = N N″
R^t_{θtθ} = −r N′/N     ⇒ R_{tθtθ} = r N N′
R^t_{φtφ} = −r sin²θ N′/N  ⇒ R_{tφtφ} = r sin²θ N N′
```

All purely-spatial Riemann components vanish (flat 3-section).

**Ricci (contractions):**

```
R_tt = N (N″ + 2 N′/r)
R_rr = −N″/N
R_θθ = −r N′/N,   R_φφ = sin²θ · R_θθ
```

**Ricci scalar:**

```
R = −(2/N)·(1/r²)·(r² N′)′ = −2[N″ + 2N′/r]/N
```

**Kretschmann:**

```
K = R_{abcd} R^{abcd} = 4(N″²/N²) + 8(N′²/(r²N²)) = (4/N²)·[N″² + 2N′²/r²]
```

Solving `R = 0`:
`(r²N′)′ = 0 ⇒ N = B − A/r`.

Solving `R_μν = 0`:
`R_rr = 0 ⇒ N″ = 0; R_θθ = 0 ⇒ N′ = 0 ⇒ N = const` (Minkowski only).

---

**Status.** Working memo. Coordinate-invariant proof that ED acoustic
metric cannot reach Schwarzschild. Closes a specific ED-10 framing; does
not change ED's other sectors. Next natural question: whether admitting
anisotropic `M^{ij}(ρ)` or non-zero `v₀` could reopen the route — both
are extensions of canonical ED and should be scoped separately.
