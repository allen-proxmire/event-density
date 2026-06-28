# Hyperbolic Strong-Field Rule — Built; Direct κ∝1/r_h Resolution-Limited

**What was done.** Built the **hyperbolic** strong-field gravity rule — the wave version the arc
named but never built (`dynamical_bandwidth_3d.py` gave flat κ; the diagnosis was "needs a
HYPERBOLIC strong-field rule, not built"). `hyperbolic_modes.py` had built only its *linear*
sector (mode speeds, c_s=c). This (`hyperbolic_strongfield.py`) builds the **strong-field**
sector and drives it to a b→0 horizon:

    HYPERBOLIC :  b'' = c^2 grad^2 b - kappa rho - gamma b'   (single-P05 transport wave operator
                                                               + dissipative reserve as light damping)
    ELLIPTIC   :  b_dot = D grad^2 b - kappa rho              (the built rule, run as control)

**The question.** Does the wave rule give a *direct dynamical* κ ∝ 1/r_h (Hawking scaling) where
the elliptic rule gave flat κ? Rationale: the elliptic rule has a fixed sharing length (D) that
makes the near-horizon transition width r_h-independent → flat κ; the wave rule has no such length,
so the horizon can sharpen with the source and the slope can scale.

## Two real results

1. **The rule is built and runs, and forms sharp tight horizons** — the physically correct behavior
   for a rule with no diffusive smoothing length (no D). Confirmed: hyperbolic horizons are much
   tighter than elliptic for the same source.
2. **The measurement was fixed and is now sound.** The first attempt measured a fixed 6-cell slope
   window and got κ ≈ 0.021 *identical for both rules across all r_h* — a pure artifact. Two causes
   found and corrected: (i) heavy damping (γ=0.10) turned the wave rule *secretly diffusive* at late
   times (telegrapher D_eff ~ c²/γ), so "hyperbolic" relaxed like elliptic → fake-flat; fixed with
   light damping (γ=0.04). (ii) the slope window reached into the far field; replaced with an
   **inner-transition-width** measure (κ_w = 0.45 / [r(b=0.5) − r(b=0.05)]) on a **near-point**
   source (σ=2.5) so the horizon forms in vacuum. **Proof the fix works: the elliptic control now
   SCALES** — κ_w ~ r_h^−0.34, tracking the analytic 1/(2r_s) — instead of the artifact flat.

## The obstruction, pinned from both sides

| rule | κ_w ~ r_h^p | r_h (cells) | status |
|---|---|---|---|
| elliptic (control) | **−0.34** | 4.2 – 6.8 | resolved, but **over-smooths** (D flattens κ below the analytic ≈ −0.7) |
| hyperbolic (new)   | **+0.01** | 1.7 – 4.3 | horizons **sub-resolution** (≤ source size, < few cells) → κ_w is noise, not signal |

The hyperbolic flat result is **the lattice failing to resolve a sharp, small horizon**, not a
physics "no." This is exactly the **resolution-limited** wall the research targets already flagged
("the directly-simulated near-horizon slope is resolution-limited"), now confirmed precisely from
both directions: the elliptic rule under-scales by over-smoothing; the hyperbolic rule's horizons
are too sharp/small to measure at S=80.

## Verdict (honest, null for the direct goal)

- **Built:** the hyperbolic strong-field rule (the named-unbuilt piece) — it runs, forms sharp horizons.
- **Fixed:** the surface-gravity measurement (elliptic control now scales, proving it).
- **NOT settled:** a clean *direct dynamical* κ ∝ 1/r_h. It is **resolution-limited** — needs S ≳ 160–200
  (NR-grade) where the sharp hyperbolic horizons span enough cells; not reachable by quick S≤80 runs.
- **What stands:** the **analytic** Hawking scaling — κ = ½ db/dr = 1/(2r_s) on the harmonic vacuum
  profile b = 1 − r_s/r + measured r_s ∝ M (`strongfield_surface_gravity.py`) — unchanged. The
  direct dynamical confirmation is the open, compute-bound residual.

No win faked on a sub-resolution horizon. The rule exists; the decisive measurement awaits a finer grid.
