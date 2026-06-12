# ThickRegimeContinuum — Round 1 results

**Question (constructive complement to the bridge, paper §6a):** Round 6 showed conservation is
necessary-but-not-sufficient for a continuum PDE, and located the missing ingredient as **scale
separation** — which ED's natural thin/ballistic/determinate regime lacks. So: *force* the
substrate into the dense, over-damped, many-collision regime and ask whether the conserved
bandwidth field then admits a clean diffusion-class PDE. Does ED have **any** PDE-generating
regime — and if so, what does it cost?

**Script:** `thick_regime_test.py`. **Verdict:** ED has a clean diffusion-class regime at exactly
one point — full random scatter — where its defining operation has been erased. Partial ED
determinacy does not relax to diffusion; it **traps**. The price of the PDE is the whole substrate.

## Design

A single regime knob **ε** interpolates the carrier-hop rule, holding every primitive fixed
(ρ monotone per P11; bandwidth conserved exactly — carriers are unit bandwidth quanta that are
only ever *moved*; no drains, no sources):

- **ε = 0** — each carrier hops to its **max-Σ neighbour** under the certified `compute_sigma`,
  certified deterministic tie-break by `(bw, node_id)`. This is the certified determinate substrate.
- **ε = 1** — each carrier hops to a **uniformly random** neighbour: a plain conserved-tracer
  random walk, which is diffusion *by construction*.

ε is the §6a "regime, not primitive" knob: how often a carrier scatters versus follows Σ. ε>0 is
**not** the certified substrate — it is the constructed thick-regime variant whose entire purpose
is to find ED's PDE limit if one exists and to price it. The vectorised Σ is validated against the
certified `simulator.sigma.compute_sigma` at startup (max|diff| = 0.0).

Thick-regime conditions enforced: high carrier density (0.5 and 2.0 per node), tunable scattering
(ε), periodic boundaries (bounded steady arena), nearest-neighbour square lattice (isotropic at
leading order for a *scalar* conserved field — square-lattice anisotropy is fourth-order; the
measured velocity anisotropy `std(f_d)` confirms `≈0`). 96×96 lattice, T=90, mode amplitude 0.6.

Two instruments, deliberately redundant:
1. **Global mode decay** — seed the carrier density with a cosine mode `1 + 0.6 cos(kx)`, k=2π/S,
   and track the mode amplitude `a(t)`. A diffusion equation decays it as `a(t) = a₀ e^{−Dk²t}`,
   so `ln a` linear in `t` (high decay-R²) **is** the diffusion signature, and `D = −slope/k²`.
2. **Local Fickian regression** — coarse-grain `b` and the flux `J` at blocks B∈{4,8,16} and fit
   `J = −D∇b`, continuity `∂ₜb = −∇·J`, diffusion `∂ₜb = D∇²b`.

## Results

### The local Fickian regression is shot-noise-limited (as in R6) — read the mode instead

`fick_r2 ≈ 0` for **every** ε and B, *including ε=1* where the dynamics are a pure random walk and
therefore diffusion by construction. This is not physics: per-node, per-step flux is a tiny noisy
integer (≈0.5–2 carriers/node, ±1 hops) that swamps the deterministic drift `−D∇b`. This is the
same local measurement wall R3/R4/R6 hit. The **global mode-decay** instrument averages over the
whole lattice and carries signal — and it self-validates (below). We read the verdict from it.

### The mode-decay instrument self-validates at ε=1

At ε=1 the mode decay is clean exponential (decay-R² = 0.98–0.99), the MSD exponent α ≈ 1.0–1.2
(diffusive), persistence p → 0.25 (memoryless), velocity anisotropy → 0, and the recovered
coefficient **D_mode ≈ 0.23**, matching the analytic 2D nearest-neighbour random-walk value
**D = 1/(2·dim) = 0.25**. The instrument recovers the known answer where a known answer exists.

### Clean diffusion appears at exactly one place: ε = 1

| ε | persist | aniso | MSD α | decay-R² | D_mode | reading |
|---|---|---|---|---|---|---|
| 0.00 | 0.25–0.35 | ≈0 | 0.79–0.93 | 0.86–0.95 | 1.6–3.3 | sub-diffusive; D≠0.25; no Fickian closure |
| 0.25 | 0.24–0.31 | ≈0.01 | 0.23–0.60 | **0.001–0.74** | erratic | mode decay non-exponential — **trapping** |
| 0.50 | 0.25–0.28 | ≈0.01 | 0.26–0.33 | **0.01–0.72** | erratic | trapping; no clean PDE |
| 0.75 | 0.26 | ≈0.01 | 0.10–1.10 | 0.85–0.89 | 1.1–4.7 | transitional, still not D=0.25 |
| 1.00 | **0.25** | **≈0** | **1.0–1.2** | **0.98–0.99** | **≈0.23** | **clean diffusion, D≈0.25** ✓ |

(Values span the two densities frac = 0.5 / 2.0.)

The story is monotone in the wrong direction for ED. As ε falls from 1 toward 0 — i.e. as the
certified Σ-selection is given *more* say — the dynamics move **away** from diffusion, not toward
it. The intermediate regime (ε = 0.25–0.5) is the worst: the mode decay is non-exponential
(decay-R² collapses toward 0) and the MSD exponent drops to α ≈ 0.1–0.33, deep **sub-diffusion**.
Mechanistically this is Σ doing exactly what it is built to do: it funnels carriers toward the
coherence optimum ρ ≈ ρ\* and the monotone ρ-footprint (P11) freezes them there. Σ-selection is a
*trapping* operator, not a *relaxing* one. A diffusion PDE needs relaxation; ED supplies commitment.

A second-order nuance: at ε=0 with high density (frac 2.0) the MSD exponent creeps back up to
α ≈ 0.93 and decay-R² ≈ 0.95 — but with D_mode ≈ 3.3, nowhere near 0.25, and no Fickian closure.
This is *density-induced effective scattering* (the carriers' own ρ-deposits roughen the Σ
landscape until selection is effectively randomised), not a genuine diffusion limit of the
selection rule — it is ε→effective-noise by a different route, and it still does not produce a
clean, coefficient-correct PDE.

## Verdict

**ED has a PDE-generating thick regime only in the limit ε → 1, where Σ-selection has been
completely replaced by random scattering.** At that point the object is a textbook conserved
random walk (diffusion, D = 0.25) wearing ED's data structures — it is no longer the ED substrate
in any operative sense. For **any** ε < 1, with the certified Σ-rule still steering even partially,
the conserved field does **not** relax to a diffusion-class PDE: it is sub-diffusive / trapping,
its mode decay is non-exponential, and nothing closes.

This is the constructive confirmation of the bridge (paper §6a). Round 6 said conservation is not
enough and named scale separation as the missing piece. Round 1 here *forces* every thick-regime
ingredient — density, scattering, isotropy, bounded steady arena, conservation — and finds that the
one remaining obstruction is **structural, not parametric**: ED's determinate selection operator is
the opposite of a collision operator. You cannot tune the substrate into a fluid; you can only
delete the substrate and put a random walk in its place. **The price of the PDE is the whole ED
character.** ED makes facts (determinate commitment); fluids relax (random scattering); they are
not two regimes of one rule — they are different rules, and only the second integrates to a PDE.

Failure mode, stated plainly per the brief: **structural — the selection rule is a trapping
operator, so no amount of density/scattering short of fully overriding it (ε=1) yields the local
equilibrium a diffusion PDE requires.** Residual anisotropy is not the cause (aniso ≈ 0);
insufficient scale separation at ε<1 is a *symptom* of the trapping, not an independent knob.

## Crank-safety / honesty notes

- No primitive changed; ρ monotone (P11); bandwidth conserved exactly (carriers only moved).
- ε > 0 is explicitly **not** the certified substrate; it is the §6a constructed variant.
- The local Fickian regression is reported as **shot-noise-limited and unreliable**, not as evidence;
  the verdict rests on the mode-decay instrument, which is validated against the analytic D = 0.25.
- The result is a clean *negative for ED-as-PDE-generator* and a clean *positive for the
  complementarity thesis*. Reported as the data fell, including the ε=0 high-density nuance.
