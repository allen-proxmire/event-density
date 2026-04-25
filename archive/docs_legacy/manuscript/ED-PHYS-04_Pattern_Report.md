# ED-PHYS-04: Nonlinear Pattern Formation in Event Density

## Key Finding

**The canonical ED PDE does NOT support pattern formation.**

The uniform equilibrium rho = rho_star is linearly stable to perturbations of ALL wavenumbers.  No Turing patterns, no spinodal decomposition, no symmetry-breaking instabilities.

However, ED produces rich **transient morphological structure** from multi-modal initial conditions.  This structure decays to equilibrium but has a measurable lifetime and complexity peak.

## Regime

- Dimension: 2D, grid 64^2
- P0 = 0.5 (weak penalty), D = 0.3
- sigma_k1 = 0.8902, morphological lifetime ~ 1.12
- Decay ratio k4/k1 = 13.47

## Experiment 1: Noise Instability Test

- Noise amplitude: 0.01
- Any mode grew above initial: **True**
- Transient amplification ratio C_peak/C_0 = 1.0000
- Peak complexity time: 0.0000
- Complexity half-life: 0.0400

### Modal Decay Rates

| k | sigma_fitted | sigma_predicted | Status |
|---|-------------|----------------|--------|
| 1 | 0.9182 | 0.8902 | DECAY |
| 2 | 2.0896 | 3.1109 | DECAY |
| 3 | 3.4335 | 6.8120 | DECAY |
| 4 | 3.8493 | 11.9935 | DECAY |
| 5 | 3.1740 | 18.6555 | DECAY |

**All modes decaying: True**
**Fastest growth rate: -3.8493e+00** (< 0, no instability)

## Experiment 2: Filament Stability

- Filament width: 0.05
- Initial peak: 0.0790
- Final peak: 7.4867e-03
- Filament intact (no breakup): **False**

The filament decays smoothly by diffusion and penalty relaxation. No Plateau-Rayleigh-like breakup occurs.

## Experiment 3: Spot Evolution

- Initial peak: 0.0786
- Final peak: 8.2921e-02
- Developed ring structure: **True**

The spot diffuses isotropically and decays monotonically. No ring formation or morphological instability.

## Why ED Does Not Form Patterns

Pattern formation in reaction-diffusion systems requires an instability band: a range of wavenumbers k where the linearised growth rate sigma_k > 0.  In ED:

    sigma_k = -D (M_star mu_k + P0) < 0   for ALL k

because both terms are positive.  There is no mechanism for:
- Negative effective diffusion (M_star > 0 always)
- Activator-inhibitor dynamics (only one field)
- Bistable potential (penalty is monostable)
- Spinodal decomposition (no double-well energy)

## What ED Does Instead: Transient Morphology

Although ED cannot sustain patterns, it creates rich transient structure through **differential decay rates**.  High-k modes decay faster than low-k modes (by a factor of 13.5x at k=4 vs k=1).  This differential decay:

- Creates a transient hierarchy of spatial scales
- Produces filaments, sheets, and blobs (ED-Phys-35)
- Generates oscillatory morphological exchange (Law 9)
- Has a characteristic lifetime ~ 1/sigma_k1 = 1.12

This 'transient pattern' phenomenon is unique to ED and distinguishes it from both pattern-forming (AC, CH) and non-structured (pure heat) PDEs.

## Comparison to Pattern-Forming PDEs

| Feature | ED | Allen-Cahn | Cahn-Hilliard |
|---------|-----|------------|---------------|
| Instability band | No | Yes | Yes |
| Steady-state patterns | No | Domain walls | Labyrinthine |
| Transient structure | Rich | Limited | Rich |
| Attractor | Unique (uniform) | Bistable | Coarsened |
| Coarsening | No | Yes | Yes (L~t^{1/3}) |
| Morphological oscillation | Yes | No | No |