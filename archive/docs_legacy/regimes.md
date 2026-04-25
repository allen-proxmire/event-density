# Physical Regime Classification

The `edsim.regimes` package classifies ED simulations into physical
regimes based on characteristic scales, computes physical observables,
and produces cross-regime comparison atlases.

## The Regime Manifold

The ED PDE is solved in nondimensional form.  A **regime** is a region
of the physical scale space $(L_0, R_0, T_0)$ in which the
nondimensional dynamics admit a specific physical interpretation.

Five canonical regimes are defined:

| Regime | $L_0$ range | $R_0$ range | Physical analogues |
|--------|-------------|-------------|-------------------|
| Quantum-like | $10^{-36}$ -- $10^{-9}$ m | $10^{10}$ -- $10^{100}$ kg/m$^3$ | Probability density, pilot wave, Planck foam |
| Mesoscopic | $10^{-9}$ -- $10^{-4}$ m | $10^{-3}$ -- $10^{6}$ kg/m$^3$ | Colloids, nanoparticles, cell biology |
| Condensed-matter | $10^{-6}$ -- $10$ m | $10^{-1}$ -- $10^{5}$ kg/m$^3$ | Porous media, thin films, solidification |
| Gravitational | $10^{15}$ -- $10^{23}$ m | $10^{-30}$ -- $10^{-20}$ kg/m$^3$ | Dark-matter halos, galaxy clusters |
| Cosmological | $10^{23}$ -- $10^{30}$ m | $10^{-30}$ -- $10^{-24}$ kg/m$^3$ | Cosmic web, large-scale structure |

These five regimes span approximately 60 orders of magnitude in length
and 130 orders of magnitude in density.

## How Classification Works

Given a `Scales` object with $(L_0, R_0)$:

1. **Containment check.**  Each regime defines an $(L_0, R_0)$ box.
   If the scales fall within exactly one box, that regime is assigned.

2. **Tightest bracket.**  If multiple regimes overlap, the one with
   the narrowest $L_0$ range (in log space) wins.

3. **Nearest neighbour.**  If no regime contains the scales, the
   regime whose $(L_0, R_0)$ midpoint is closest in log space is
   assigned.

```python
from edsim.units import condensed_matter_scales
from edsim.regimes import classify_scales

scales = condensed_matter_scales(params)
regime = classify_scales(scales)
print(regime.label)  # "Condensed-matter-like"
```

## Interpreting L0, R0, T0

| Scale | Meaning |
|-------|---------|
| $L_0$ | Physical size of the simulation domain.  Determines which objects the simulation describes (atoms, films, galaxies, ...). |
| $R_0$ | Physical density scale.  Determines what $\rho = 1$ means (water density, critical density, Planck density, ...). |
| $T_0 = L_0^2 / D_{\text{phys}}$ | Diffusion timescale.  Determines how fast the dynamics unfold in physical time. |
| $V_0 = L_0 / T_0$ | Characteristic velocity.  Determines the speed scale of participation coupling. |
| $E_0 = R_0 \cdot L_0^d$ | Mass/energy scale.  Determines the physical significance of Lyapunov energy changes. |

## Dimensionless Groups

The classifier computes key dimensionless ratios that locate the
simulation within the manifold:

| Group | Meaning |
|-------|---------|
| $L_0 / l_{\text{Pl}}$ | Domain size in Planck lengths |
| $L_0 / a_0$ | Domain size in Bohr radii |
| $L_0 / \text{kpc}$ | Domain size in kiloparsecs |
| $R_0 / \rho_{\text{crit}}$ | Density parameter $\Omega$ |
| $V_0 / c$ | Velocity in units of light speed |
| $T_0 \cdot H_0$ | Time in Hubble units |

```python
from edsim.regimes import compute_dimensionless_groups
groups = compute_dimensionless_groups(scales, params)
print(f"L0/kpc = {groups['L0/kpc']:.2e}")
```

## Physical Observables

The `observables` module extracts SI-valued quantities from a
`PhysicalTimeSeries`:

```python
from edsim.regimes import compute_observables

obs = compute_observables(pts, regime_name="Condensed-matter")
print(f"Mass: {obs.total_mass_kg:.4e} kg")
print(f"Energy ratio: {obs.energy_ratio:.4f}")
print(f"Correlation length: {obs.correlation_length_final_m:.4e} m")
```

Available observables include total mass, energy ratio, correlation
length growth, dissipation channel fractions, spectral entropy
evolution, morphology fractions, and Euler characteristic conservation.

## Running the Regime Atlas

The atlas runs one simulation and interprets it at multiple scales:

```python
from edsim.regimes import quick_regime_atlas

atlas = quick_regime_atlas("A_2d_cosine")

# Four figures are generated:
atlas.figures["regime_scatter"]       # L0 vs R0 scatter
atlas.figures["energy_overlay"]       # normalised energy decay
atlas.figures["invariant_comparison"] # bar chart of invariants
atlas.figures["dimensionless_groups"] # group profiles

# Summary table
print(atlas.summary_table())
```

For more control:

```python
from edsim.regimes import run_regime_atlas
from edsim.units import quantum_scales, galactic_scales

scenario = get_scenario("A_2d_cosine")
scales_list = [quantum_scales(params), galactic_scales(params)]
atlas = run_regime_atlas(scenario=scenario, scales_list=scales_list)
```

## Examples

### Example 1: Quantum regime

```python
from edsim.units import quantum_scales, m_e
scales = quantum_scales(params, mass=m_e)
# L0 = 3.86e-13 m (reduced Compton wavelength)
# R0 = 6.71e+24 m^-2 (probability density in 2D)
# Interpretation: electron density in a 2D confining potential
```

### Example 2: Galactic regime

```python
from edsim.units import galactic_scales
scales = galactic_scales(params)
# L0 = 3.09e+19 m (1 kpc)
# R0 = 8.53e-27 kg/m^3 (critical density)
# Interpretation: dark-matter halo density profile
```

### Example 3: Condensed-matter regime

```python
from edsim.units import condensed_matter_scales
scales = condensed_matter_scales(params, L0=1e-6, R0=1e3)
# L0 = 1e-6 m (1 micron)
# R0 = 1e3 kg/m^3 (water density)
# Interpretation: thin-film spreading on a substrate
```

## How ED Invariants Map to Physical Observables

| ED Invariant | Physical observable | Regime-dependence |
|-------------|--------------------|--------------------|
| Lyapunov energy $E[\rho]$ | Free energy [J] | Dimensional ($E_0 = R_0 L_0^d$) |
| ED-complexity $C[\rho]$ | Gradient energy [J/m$^2$] | Dimensional ($R_0^2 L_0^{d-2}$) |
| Mass $M[\rho]$ | Total mass [kg] | Dimensional ($R_0 L_0^d$) |
| Correlation length $\xi$ | Physical correlation [m] | Dimensional ($L_0$) |
| $R_{\text{grad}}$ | Gradient dissipation fraction | **Dimensionless** |
| Spectral entropy $H$ | Modal disorder | **Dimensionless** |
| Morphology fractions | Structure classification | **Dimensionless** |
| Euler characteristic $\chi$ | Topology | **Dimensionless** |

The dimensionless invariants are **regime-independent**: they take the
same values regardless of which physical scales are applied.  This is
the quantitative expression of the ED architectural universality.
