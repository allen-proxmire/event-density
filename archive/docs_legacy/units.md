# Physical Units and Dimensional Mapping

ED-SIM-02 solves the canonical ED PDE in nondimensional form.  The
`edsim.units` package provides an optional layer that maps nondimensional
quantities to physical (SI) units.  The solver is never modified; all
conversions happen at the interface.

## The Nondimensionalization Scheme

The canonical ED PDE in physical units is

$$\partial_t \rho = D_{\text{phys}}\bigl[M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)\bigr] + H_{\text{phys}}\,v,$$

where $\rho$ has dimensions of density $[\text{kg}\,\text{m}^{-3}]$,
$x$ has dimensions of length $[\text{m}]$, and $t$ has dimensions of
time $[\text{s}]$.

We define three **characteristic scales**:

| Scale | Symbol | Definition | Unit |
|-------|--------|------------|------|
| Length | $L_0$ | Domain size or physical length scale | m |
| Time | $T_0$ | Diffusion time $L_0^2 / D_{\text{phys}}$ | s |
| Density | $R_0$ | Capacity bound $\rho_{\max}$ or background | kg m$^{-3}$ |

The nondimensional variables are:

$$\hat{x} = x / L_0, \quad \hat{t} = t / T_0, \quad \hat{\rho} = \rho / R_0.$$

After substitution, the PDE becomes

$$\partial_{\hat t}\hat\rho = \hat D\bigl[\hat M(\hat\rho)\hat\nabla^2\hat\rho + \hat M'(\hat\rho)|\hat\nabla\hat\rho|^2 - \hat P(\hat\rho)\bigr] + \hat H\,\hat v,$$

where $\hat D = D_{\text{phys}} T_0 / L_0^2 = 1$ (by construction of $T_0$),
and all hatted quantities are dimensionless.

Two **derived scales** follow:

| Scale | Symbol | Definition | Unit |
|-------|--------|------------|------|
| Velocity | $V_0 = L_0 / T_0$ | Characteristic speed | m s$^{-1}$ |
| Energy density | $E_0 = R_0 \cdot L_0^d$ | Mass scale | kg |

## How to Compute Characteristic Scales

```python
from edsim.core.parameters import EDParameters
from edsim.units import compute_scales

params = EDParameters(d=2, L=(1.0, 1.0), N=(64, 64))

# Generic: provide L0 and R0
scales = compute_scales(params, L0=1e-6, R0=1e3, regime="micron")
print(f"T0 = {scales.T0:.4e} s")
print(f"V0 = {scales.V0:.4e} m/s")
```

Pre-built factories are available for common regimes:

```python
from edsim.units import planck_scales, quantum_scales, galactic_scales

sc_planck   = planck_scales(params)      # L0 ~ 1.6e-35 m
sc_quantum  = quantum_scales(params)     # L0 ~ Compton wavelength
sc_galactic = galactic_scales(params)    # L0 ~ 1 kpc
```

## ED Parameters and Physical Constants

Each ED parameter maps to one or more physical analogues.  The mapping
is *structural*, not ontological: the ED framework does not commit to
a single physical interpretation.

| ED Parameter | Physical analogue(s) | Physical unit |
|-------------|---------------------|---------------|
| $\rho$ | density, probability, curvature potential | kg m$^{-3}$ or m$^{-d}$ |
| $v$ | bulk velocity, global mode amplitude | m s$^{-1}$ |
| $D$ | diffusivity, viscosity, $\hbar / 2m$ | m$^2$ s$^{-1}$ |
| $M(\rho)$ | mobility, conductivity (PME: $u^m$) | m$^2$ s$^{-1}$ |
| $P(\rho)$ | pressure, drift, chemical potential | kg m$^{-3}$ s$^{-1}$ |
| $H$ | forcing amplitude, feedback gain | m s$^{-1}$ |
| $\tau$ | relaxation time, damping time | s |
| $\rho^*$ | background density, mean density | kg m$^{-3}$ |
| $\rho_{\max}$ | close-packing, Pauli limit, horizon | kg m$^{-3}$ |

The full dictionary with all analogues can be printed:

```python
from edsim.units import print_dictionary
print_dictionary(params, scales)
```

## Running in Physical Units

### Option 1: Convert output after running

Run the solver in nondimensional mode, then convert:

```python
from edsim.experiments.scenarios import get_scenario
from edsim.experiments.atlas import run_atlas
from edsim.units import compute_scales, convert_time_series

scenario = get_scenario("A_2d_cosine")
params, ts = run_atlas(scenario)

scales = compute_scales(params, L0=1e-6, R0=1e3)
pts = convert_time_series(ts, scales)

print(f"Final time:  {pts.times_s[-1]:.4e} s")
print(f"Final mass:  {pts.mass_kg[-1]:.4e} kg")
print(f"Corr length: {pts.correlation_length_m[-1]:.4e} m")
```

### Option 2: Specify physical parameters directly

```python
from edsim.units import PhysicalParameters, run_physical_simulation

pp = PhysicalParameters(
    d=2,
    L_phys=(1e-6, 1e-6),      # 1 micron x 1 micron domain
    N=(64, 64),
    D_phys=1e-12,              # diffusivity [m^2/s]
    rho_star_phys=500.0,       # equilibrium density [kg/m^3]
    rho_max_phys=1000.0,       # capacity bound [kg/m^3]
    dt_phys=1e-15,             # 1 femtosecond
    T_phys=1e-9,               # 1 nanosecond
)

pts = run_physical_simulation(pp, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})
print(f"Energy: {pts.energy_J[0]:.4e} -> {pts.energy_J[-1]:.4e} J")
```

## Example Regimes

### Micron-scale (condensed matter)

- Domain: 1 micron.  Timescale: nanoseconds.  Density: water ($10^3$ kg/m$^3$).
- Appropriate for: diffusion in thin films, colloid dynamics, soft matter.

```python
scales = condensed_matter_scales(params, L0=1e-6, R0=1e3)
# L0 = 1e-6 m, T0 ~ 3.3e-3 s (if D=0.3, D_phys ~ 3e-10 m^2/s)
```

### Galactic scale

- Domain: 1 kpc.  Timescale: Gyr.  Density: critical ($8.5 \times 10^{-27}$ kg/m$^3$).
- Appropriate for: dark-matter halo evolution, galactic density profiles.

```python
scales = galactic_scales(params)
# L0 = 3.09e19 m, T0 ~ 3.18e38 s, R0 = 8.53e-27 kg/m^3
```

### Quantum scale

- Domain: Compton wavelength.  Density: probability density.
- Appropriate for: Schrodinger-like analogues, quantum measurement problems.

```python
scales = quantum_scales(params, mass=m_e)
# L0 = 3.86e-13 m (reduced Compton of electron)
```

## Design Principles

1. **The solver never sees physical units.**  All conversion is at the
   boundary: input conversion (PhysicalParameters -> EDParameters) and
   output conversion (TimeSeries -> PhysicalTimeSeries).

2. **Dimensionless invariants are passed through.**  Spectral entropy,
   morphology fractions, dissipation ratios, and Euler characteristic
   are inherently dimensionless and require no conversion.

3. **The mapping is agnostic.**  The dictionary lists multiple physical
   analogues for each ED parameter.  The user chooses the interpretation
   appropriate to their domain.

4. **Scales are explicit.**  Every conversion uses a Scales object that
   records L0, T0, R0, V0, E0 and the regime label.  There are no
   hidden unit assumptions.
