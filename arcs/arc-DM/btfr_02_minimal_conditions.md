# BTFR.02 — Minimal Mathematical Conditions for BTFR

**Date:** 2026-04-27
**Arc:** Dark Matter — BTFR sub-arc, second memo
**Status:** Structural derivation complete. Two-condition theorem and viability checklist established.
**Predecessor:** BTFR.01 (structural definition of the empirical BTFR; structural test for any candidate theory).
**Successor:** BTFR.03 (apply viability checklist to ED).

---

## 1. Setup

Consider any theory in which a scalar field φ is sourced by a baryonic distribution ρ_b through a *linear* PDE

> L φ = −σ · s(ρ_b)

with linear differential operator L, source functional s(ρ_b), and coupling constant σ. Linearity gives

> φ(x) = σ · ∫ G(x, x′) · s(ρ_b(x′)) d³x′

where G(x, x′) is the Green's function of L. The kinematic prediction is read off via

> v_circ²(R) = α · R · ∂_R φ(R, z = 0)

where α absorbs theory-specific dimensional constants. This form is universal across any framework in which kinematic forcing is the gradient of a scalar field (Newton, MOND deep regime, ED Reading B).

The BTFR test asks: does v_circ become asymptotically constant ("flat") at large R, and does that constant satisfy v_flat⁴ ∝ M_b independent of galaxy size, surface brightness, or morphology?

---

## 2. Asymptotic monopole

For an axisymmetric source confined within radius R_b, multipole-expand at field points R ≫ R_b:

> φ(R, z = 0) = σ · [G_mono(R) · M_eff + higher multipoles]

where

> M_eff ≡ ∫ s(ρ_b(x′)) d³x′

is the **effective monopole charge** of the source. Higher multipoles fall off faster than the monopole; for the BTFR test only the monopole matters.

Write the asymptotic monopole Green's function as

> G_mono(R) ~ −C · g(R)   (R → ∞)

where g(R) is the asymptotic kernel form and C is a dimensional constant.

Asymptotically:

> v_circ²(R → ∞) ∝ M_eff · R · g′(R).

---

## 3. The flat-curve condition (C1)

For v_circ² to approach a non-zero constant as R → ∞,

> R · g′(R) → k    (constant ≠ 0)

This integrates to

> g(R) = k · ln R + const.

**The only Green's-function asymptotic that produces a strictly flat rotation curve from a localized source is logarithmic.** Any power-law tail R^{−n} (n > 0) gives v_circ² → 0; any exponential tail e^{−R/L} drives v_circ² to zero faster than any polynomial.

This is equivalent to requiring the operator L to be effectively two-dimensional in the asymptotic regime: 2D Newtonian Poisson natively has a log Green's function; 3D-isotropic operators do not.

---

## 4. The BTFR-coupling condition (C2)

If C1 holds,

> v_flat² = (α · σ · C · k) · M_eff.

Squaring:

> v_flat⁴ = (α · σ · C · k)² · M_eff².

For BTFR (v_flat⁴ ∝ M_b),

> M_eff² ∝ M_b   ⟺   σ · M_eff ∝ M_b^{1/2}.

The product (coupling × effective charge) must scale as the **square root** of the baryonic mass.

Two structurally distinct routes satisfy C2:

- **Route A — sublinear coupling.** s = ρ_b (so M_eff = M_b), but the coupling carries an M_b^{−1/2} weight, requiring the theory to contain a fundamental acceleration scale a₀ against which the sublinearity is measured. MOND in the deep regime is the canonical example.
- **Route B — sublinear source functional.** σ is mass-independent, but s(ρ_b) integrates to M_eff ∝ √M_b. This requires explicit nonlinearity in the source construction or a kinematic functional whose disc-geometry integration yields the √M_b scaling.

C1 (kernel-level) and C2 (source-level) are independent. **Both must hold.**

---

## 5. Classification of Green's-function asymptotics

| Kernel asymptotic g(R) | R · g′(R) | v_circ²(R) | Flat? |
|---|---|---|---|
| 1/R (3D Newton) | −1/R | ~1/R | falls |
| 1/R^n, n > 0 | −n/R^n | ~1/R^n | falls |
| e^{−R/L}/R (Yukawa) | exponential | ~e^{−R/L} | falls (exponential) |
| ln R (2D Newton) | 1 | constant | **flat** |
| R^n, n > 0 | nR^n | grows | unphysical |
| (1/R)(1 + R/L_∞) (linear-confining) | 1/L_∞ | constant | **flat** |
| Anisotropic Yukawa, D_z ≪ D_R | log over a window in R | ≈ constant (windowed) | **flat (windowed)** |
| Fractional Laplacian (−Δ)^s, dim d | R^{−(d−2s)} | R^{−(d−2s)+1} | flat iff d − 2s = 1 |

Three classes produce asymptotically flat curves: logarithmic (true 2D), linear-confining, and anisotropic-Yukawa-in-the-plane (3D theory behaving as 2D over a finite radial window).

---

## 6. PDE class viability table

| PDE class | Operator | 3D monopole G_∞ | v_circ scaling | BTFR viability |
|---|---|---|---|---|
| Newtonian Poisson | −Δ | 1/R | R^{−1/2} | **No** (curves fall) |
| Screened Poisson (Yukawa) | −Δ + 1/L² | e^{−R/L}/R | exponential cutoff | **No** (curves fall) |
| Biharmonic | Δ² | R (in 3D) | grows | **No** (unphysical) |
| Fractional Laplacian (−Δ)^s, 3D | s ∈ (0,1) | R^{−(3−2s)} | flat iff s = 1 (Poisson) | **No** (in 3D) |
| 2D Newtonian Poisson | −Δ_2D | ln R | constant | **C1 yes; needs C2** |
| Anisotropic 3D Poisson, D_z ≪ D_R | −D_R Δ_R − D_z ∂_z² | log in plane (windowed) | constant (windowed) | **C1 yes (windowed); needs C2** |
| MOND-equivalent (nonlinear) | ∇·[μ(\|∇φ\|/a₀)∇φ] | log far-field | constant | **C1+C2 by construction** |
| Linear-confining Poisson | −Δ + R/L_∞² | 1/R + R/L_∞ | constant from linear piece | **C1 yes; needs C2** |
| Fractional Laplacian (−Δ)^{1/2} in 2D | s = 1/2, d = 2 | log | constant | **C1 yes; needs C2** |

**Pattern.** Only operators whose effective dimensionality is 2 (genuinely 2D, anisotropic 3D, or 2D-fractional) produce flat curves from a linear PDE. 3D-isotropic operators with localized sources cannot produce flat curves regardless of source choice. This is a structural impossibility theorem for the entire 3D-isotropic-linear class.

---

## 7. Two-condition theorem

> **Theorem (BTFR viability for linear-PDE theories).**
> A linear-PDE source-Green's-function theory predicts BTFR (v_flat⁴ ∝ M_b, R-independent) if and only if both of the following hold:
>
> **(C1) Logarithmic far-field.** The monopole Green's function satisfies R · g′(R) → constant ≠ 0 as R → ∞ (over the radial regime where v_flat is measured). Equivalently, the operator must be effectively 2D in the asymptotic limit.
>
> **(C2) Sublinear effective coupling.** The product σ · M_eff scales as M_b^{1/2}. This is achieved either via a sublinear coupling weighted by a fundamental acceleration scale a₀ (Route A), or via a source functional whose disc-integral is intrinsically ∝ √ρ_b (Route B).
>
> C1 and C2 are independent; both are necessary; together they are sufficient.

---

## 8. Two structural corollaries

**Corollary 1.** Any 3D-isotropic linear PDE with a localized source produces curves that fall faster than R^{−1/2} at large R. **3D isotropy + linearity + locality = no BTFR.**

**Corollary 2.** To escape Corollary 1 within a linear-PDE framework, the theory must contain both:

- (a) **Effectively 2D operator structure** (anisotropy or 2D embedding) producing a logarithmic in-plane far-field.
- (b) **A √M_b-yielding source-coupling combination** (Route A: embedded a₀, or Route B: sublinear functional).

A theory missing (a) produces falling curves regardless of source choice. A theory with (a) but missing (b) produces flat curves with the wrong M_b scaling.

---

## 9. BTFR viability checklist

For Step 3 application:

1. **Logarithmic tail.** Does the theory's monopole Green's function asymptote to a logarithm (or equivalent windowed log) at the relevant radial scales? If no → C1 fails → **no BTFR**.

2. **Amplitude ∝ M_b^{1/2}.** Does the product σ · M_eff scale as M_b^{1/2}? Equivalently, does the theory contain either a fundamental acceleration scale (Route A) or a sublinear source functional (Route B)? If no → C2 fails → **no BTFR**.

3. **R-independence.** Is the asymptotic v_flat independent of R_d, surface brightness, and other galaxy parameters that vary in the sample? If no → BTFR scatter cannot match the empirical 0.1 dex.

4. **Constant from theory parameters.** Does the BTFR proportionality constant emerge from the theory's fundamental constants (with no per-galaxy tunables) and match the empirical A ≈ 47 M_⊙^{−1} (km/s)⁴ to within order-of-magnitude? If no → the theory at best fits BTFR with auxiliary calibration; it does not derive it.

A theory that passes (1)–(4) **derives BTFR structurally**. Failing any one is a structural defeater.

Status: complete.
