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

## The finer run (S=144, resolved) — the decisive result: the premise was a measurement artifact

Ran the NR-grade config to completion (S=144, strong sources, both horizons now resolved):

| rule | κ_w ~ r_h^p | r_h (cells) | κ_w vs 1/(2r_s) |
|---|---|---|---|
| **elliptic (control)** | **−0.50** | 6.1 – 8.6 | tracks closely (0.094→0.079 vs 0.096→0.074) |
| **hyperbolic (new)** | **−0.33** | 3.0 – 7.0 | tracks (0.102→0.076 vs 0.138→0.080); ~−0.57 over its larger horizons |

**The decisive answer is NO, and it dissolves the original premise.** The target item assumed the
elliptic rule gives *flat* κ and a *hyperbolic* rule is needed to recover κ∝1/r_h. With a sound
measurement that assumption is false:

1. **The elliptic "flat" was a measurement artifact.** Properly measured (inner-transition-width
   κ_w, near-point source), the elliptic rule already **scales** — κ_w ~ r_h^−0.50, and κ_w tracks
   the analytic 1/(2r_s) in value. The old "flat r_h^0.09" (`dynamical_bandwidth_3d.py`) was the
   fixed-window artifact, not the rule.
2. **The hyperbolic rule does not beat it** — −0.33 over the full range (dragged shallow by its
   smaller, less-resolved horizons), ~−0.57 over its larger horizons, i.e. *comparable to, not
   better than,* the elliptic −0.50. The wave rule adds nothing to the Hawking-scaling story.
3. **Neither reaches the clean −1**, because at accessible horizon sizes (3–9 cells, finite source)
   r_h ≠ r_s — the surface-gravity *value* is captured (κ_w ≈ 1/(2r_s) for both rules) but the clean
   −1 *power law* vs r_h is a finite-resolution / finite-source limit, not a rule-type effect.

## Net conclusion

- The **hyperbolic strong-field rule is built** (real, runs, forms sharp horizons) — but it is **NOT
  needed** for the Hawking scaling. The gravity sector does not require it for κ∝1/r_h.
- The target's **"fully-direct κ∝1/r_h sim" residual is resolved at the level of the *premise*:** the
  elliptic "flat κ" was a measurement artifact; with a sound measurement the elliptic rule already
  gives partial inverse scaling tracking κ ≈ 1/(2r_s). The **analytic** κ = 1/(2r_s) on the harmonic
  profile + measured r_s∝M **stands and is corroborated in value**; the clean −1 *power law* is
  finite-resolution-limited, not rule-limited.
- Honest could-say-no: the hypothesis ("hyperbolic rule carries the scaling the elliptic can't") is
  **refuted**. More informative than a win — it removes a supposed gap (no special rule needed) and
  pins the residual to resolution, not physics.
