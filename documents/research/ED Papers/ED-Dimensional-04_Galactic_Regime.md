# ED-Dimensional-04: Physical Units and Dimensional Mapping — The Galactic Regime

**Allen Proxmire**
**March 2026**

---

**Canonical sources:**

| Source | Content used |
|--------|-------------|
| Critical Assessment (2026-03-27) | The challenge being addressed |
| ED-Dimensional-01 through 03 | Series template, nondimensionalization scheme, status classification |
| ED Foundational Paper | Canonical PDE, Appendix A parameters |
| ED-I-002: Galactic Curvature | Temporal tension and halo formation |
| ED-I-027: Weak Lensing | Flat rotation curves and BTFR scaling |
| `edsim/units/constants.py` | Astrophysical constants |
| `edsim/units/scales.py` | `galactic_scales()` factory |

**Scope.** This note addresses the galactic regime, where the characteristic scales are set by astrophysical observables: kiloparsec lengths, cosmological or halo densities, and dynamical velocities. It is the fourth in the ED-Dimensional series and the first regime in which the density field $\rho$ is interpreted as mass-energy density on astrophysical scales, rather than probability density (quantum) or laboratory density (condensed matter).

---

## 0. The Challenge

ED-Dimensional-01 (quantum) and 02 (Planck) anchored scales to fundamental constants. ED-Dimensional-03 (condensed matter) anchored scales to laboratory-measured material properties. All three regimes produce quantitative predictions within their respective domains, but none addresses the domain where ED's interpretive papers have made the strongest qualitative claims: **galactic dynamics**.

The ED interpretation series (ED-I-002, ED-I-022, ED-I-027) proposes that ED's density field and temporal-tension mechanism can account for flat rotation curves, the baryonic Tully-Fisher relation (BTFR), and extended halo profiles without invoking dark matter. The March 2026 Critical Assessment acknowledged these as suggestive but demanded a quantitative mapping: specific parameter values, specific predictions in physical units, specific falsification criteria.

This note responds by constructing a complete dimensional dictionary for the galactic regime. It does **not** claim that ED replaces dark matter. It claims that ED, when anchored to galactic-scale observables, produces a specific set of quantitative predictions that can be tested against rotation curves, velocity dispersions, and density profiles.

---

## 1. The Nondimensionalization Scheme

The general scheme is identical to ED-Dimensional-01, Section 1. The canonical ED PDE in physical (SI) units is:

$$\partial_t \rho = D_{\text{phys}}\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr).$$

Three characteristic scales ($L_0$, $T_0$, $R_0$) and two derived scales ($V_0 = L_0/T_0$, $E_0 = R_0 \cdot L_0^d$) define the mapping:

$$\hat{x} = x/L_0, \quad \hat{t} = t/T_0, \quad \hat{\rho} = \rho/R_0, \quad \hat{v} = v/V_0.$$

After substitution, the nondimensional PDE has $\hat{D} = D_{\text{nd}}$ by construction of $T_0$.

---

## 2. The Galactic Regime: Scale Anchoring

### 2.1 Density: $\rho \to$ Mass-Energy Density

In the galactic regime, the ED density field is identified with the total (baryonic + dark) mass-energy density:

$$\rho(x,t) \;\to\; \text{mass density [kg m}^{-3}\text{]}.$$

The density scale $R_0$ is set by the astrophysical context:

| Application | $R_0$ (kg m$^{-3}$) | Physical meaning |
|-------------|---------------------|------------------|
| Cosmological normalisation | $8.53 \times 10^{-27}$ | Critical density $\rho_{\text{crit}} = 3H_0^2/(8\pi G)$ |
| Dark-matter halo (typical) | $\sim 10^{-24}$ to $10^{-22}$ | Central density of an NFW profile |
| Galactic disk (midplane) | $\sim 10^{-21}$ | Local stellar + gas density |

The default in this note is $R_0 = \rho_{\text{crit}} = 8.53 \times 10^{-27}$ kg m$^{-3}$ for the Milky Way (matching the `galactic_scales()` factory), and $R_0 = 10^{-24}$ kg m$^{-3}$ (typical halo density) for dwarf spheroidals. The choice of $R_0$ determines the physical interpretation of $\rho_{\max}$: the Planck-regime maximum ($\rho_{\text{Pl}}$) has no role here. Instead, $\rho_{\max} = R_0$ represents the maximum local density the system can sustain, which in the galactic context is the close-packing limit for gravitationally supported structures.

### 2.2 Length: $L_0 = 1$ kpc

$$L_0 = 1\;\text{kpc} = 3.086 \times 10^{19}\;\text{m}.$$

The kiloparsec is the natural unit for galactic structure: disk scale heights ($\sim 0.3$ kpc), bulge radii ($\sim 1$–$3$ kpc), and halo scale radii ($\sim 10$–$20$ kpc) are all expressed as small multiples of kpc. The ED simulation domain in nondimensional units maps directly to kiloparsec-scale physical domains.

For dwarf spheroidals (Fornax, Sculptor), $L_0 = 0.7$ kpc is more appropriate. For galaxy clusters, $L_0 = 1$ Mpc.

### 2.3 Diffusivity: $D_{\text{phys}} = v_{\text{circ}} \cdot L_0$

Unlike the quantum and Planck regimes, there is no fundamental-constant formula for $D_{\text{phys}}$ at galactic scales. The diffusivity must be constructed from observable quantities.

The natural choice is the **dynamical diffusivity**:

$$D_{\text{phys}} = v_{\text{circ}} \cdot L_0,$$

where $v_{\text{circ}}$ is the circular velocity of the galaxy at the scale radius. This has dimensions of m$^2$ s$^{-1}$ and encodes the characteristic rate of gravitational transport across one scale length. The physical justification:

1. **Dimensional consistency.** The only observable velocity scale at galactic radii is $v_{\text{circ}}$. The only observable length is $L_0$. Their product is the unique diffusivity constructible from galactic observables without introducing new parameters.

2. **Dynamical time.** This anchoring gives $T_0 = D_{\text{nd}} \cdot L_0/v_{\text{circ}} = D_{\text{nd}} \cdot t_{\text{cross}}$, where $t_{\text{cross}} = L_0/v_{\text{circ}}$ is the crossing time. The ED time scale is a fraction of the dynamical time — the natural timescale for gravitational redistribution.

3. **Virial scaling.** For a virialised system, $v_{\text{circ}}^2 \sim GM/R$, so $D_{\text{phys}} = v_{\text{circ}} L_0 \sim \sqrt{GML_0}$. The diffusivity encodes both the gravitational potential and the system size.

**Representative values:**

| System | $v_{\text{circ}}$ (km/s) | $L_0$ (kpc) | $D_{\text{phys}}$ (m$^2$/s) |
|--------|--------------------------|-------------|------------------------------|
| Milky Way | 220 | 1.0 | $6.79 \times 10^{24}$ |
| Dwarf spheroidal (Fornax) | 15 | 0.7 | $3.24 \times 10^{23}$ |
| Galaxy cluster (Coma) | 1000 | 1000 | $3.09 \times 10^{28}$ |

### 2.4 Time Scale

$$T_0 = \frac{L_0^2\,D_{\text{nd}}}{D_{\text{phys}}} = \frac{L_0^2\,D_{\text{nd}}}{v_{\text{circ}}\,L_0} = \frac{D_{\text{nd}}\,L_0}{v_{\text{circ}}} = D_{\text{nd}} \cdot t_{\text{cross}}.$$

This is a clean result:

$$\boxed{T_0 = D_{\text{nd}} \cdot t_{\text{cross}},}$$

directly analogous to the Planck regime where $T_0 = D_{\text{nd}} \cdot t_{\text{Pl}}$.

| System | $t_{\text{cross}}$ | $T_0$ ($D_{\text{nd}} = 0.3$) | Physical meaning |
|--------|---------------------|-------------------------------|------------------|
| Milky Way | 4.44 Myr | **1.33 Myr** | Fraction of dynamical time |
| Dwarf spheroidal | 45.6 Myr | **13.7 Myr** | Slow dynamical regime |
| Galaxy cluster | 978 Myr | **293 Myr** | Cluster relaxation fraction |

### 2.5 Velocity Scale

$$V_0 = \frac{L_0}{T_0} = \frac{v_{\text{circ}}}{D_{\text{nd}}}.$$

| System | $v_{\text{circ}}$ (km/s) | $V_0$ (km/s) | $V_0/c$ |
|--------|--------------------------|--------------|---------|
| Milky Way | 220 | 733 | $2.4 \times 10^{-3}$ |
| Dwarf spheroidal | 15 | 50 | $1.7 \times 10^{-4}$ |
| Galaxy cluster | 1000 | 3333 | $1.1 \times 10^{-2}$ |

All velocity scales are deeply subluminal. No superluminal caveat is needed. This is the only regime besides condensed matter where $V_0 \ll c$.

### 2.6 Energy/Mass Scale

$$E_0 = R_0 \cdot L_0^3.$$

| System | $R_0$ (kg m$^{-3}$) | $E_0$ (kg) | $E_0$ ($M_\odot$) | Physical meaning |
|--------|---------------------|-----------|-------------------|------------------|
| Milky Way | $8.53 \times 10^{-27}$ | $2.51 \times 10^{32}$ | 126 | Mass in one kpc$^3$ at critical density |
| Dwarf sph. | $1.0 \times 10^{-24}$ | $1.01 \times 10^{34}$ | 5070 | Mass in one (0.7 kpc)$^3$ at halo density |
| Galaxy cluster | $5.0 \times 10^{-25}$ | $1.47 \times 10^{43}$ | $7.4 \times 10^{12}$ | Cluster-mass scale |

### 2.7 Summary of Galactic-Regime Scales

| Scale | Formula | MW value | Dwarf sph. value | Unit |
|:------|:--------|:---------|:------------------|:-----|
| $L_0$ | Observed | $3.086 \times 10^{19}$ | $2.160 \times 10^{19}$ | m |
| $T_0$ | $D_{\text{nd}} \cdot L_0/v_{\text{circ}}$ | $4.208 \times 10^{13}$ | $4.320 \times 10^{14}$ | s |
| $R_0$ | Observed/chosen | $8.53 \times 10^{-27}$ | $1.0 \times 10^{-24}$ | kg m$^{-3}$ |
| $V_0$ | $v_{\text{circ}}/D_{\text{nd}}$ | $7.333 \times 10^{5}$ | $5.000 \times 10^{4}$ | m s$^{-1}$ |
| $D_{\text{phys}}$ | $v_{\text{circ}} \cdot L_0$ | $6.789 \times 10^{24}$ | $3.240 \times 10^{23}$ | m$^2$ s$^{-1}$ |
| $E_0\;(d{=}3)$ | $R_0 \cdot L_0^3$ | $2.506 \times 10^{32}$ | $1.008 \times 10^{34}$ | kg |

---

## 3. The ED-to-Galactic Dictionary

Every canonical ED parameter is mapped to its galactic-regime physical quantity. Numerical values are given for the **Milky Way** ($L_0 = 1$ kpc, $R_0 = \rho_{\text{crit}}$, $v_{\text{circ}} = 220$ km/s, $d = 3$, $D_{\text{nd}} = 0.3$).

| ED Parameter | Canonical value | Physical quantity | Formula (SI) | Value (MW) | Unit | Status |
|:-------------|:----------------|:------------------|:-------------|:-----------|:-----|:-------|
| $\rho$ | field in $[0,1]$ | Mass-energy density | $\rho_{\text{phys}} = \hat{\rho} \cdot R_0$ | $\hat{\rho} \cdot 8.53 \times 10^{-27}$ | kg m$^{-3}$ | **Observed** |
| $D$ | 0.3 | Dynamical diffusivity | $D_{\text{phys}} = v_{\text{circ}} \cdot L_0$ | $6.789 \times 10^{24}$ | m$^2$ s$^{-1}$ | **Constructed** |
| $M(\rho)$ | $M_0(1 - \hat{\rho})^\beta$ | Density-dependent transport | $M_{\text{phys}} = M_0(1 - \hat{\rho})^\beta \cdot D_{\text{phys}}/D_{\text{nd}}$ | (state-dependent) | m$^2$ s$^{-1}$ | **ED-specific** |
| $P(\rho)$ | $P_0(\hat{\rho} - \hat{\rho}^*)$ | Restoring force (virial equilibration) | $P_{\text{phys}} = P_0(\hat{\rho} - \hat{\rho}^*) \cdot R_0/T_0$ | (state-dependent) | kg m$^{-3}$ s$^{-1}$ | **Anchored** |
| $v(t)$ | scalar | Global participation mode | $v_{\text{phys}} = \hat{v} \cdot V_0$ | $\hat{v} \cdot 733$ km/s | m s$^{-1}$ | **Candidate** |
| $H$ | 0–50 | Feedback coupling strength | $H_{\text{phys}} = H_{\text{nd}} \cdot V_0$ | $H_{\text{nd}} \cdot 733$ km/s | m s$^{-1}$ | **Candidate** |
| $\tau$ | 1.0 | Participation timescale | $\tau_{\text{phys}} = \tau_{\text{nd}} \cdot T_0$ | 1.33 Myr | s | **Candidate** |
| $\zeta$ | 0.1 | Damping rate | $\zeta_{\text{phys}} = \zeta_{\text{nd}} / T_0$ | $2.377 \times 10^{-15}$ | s$^{-1}$ | **Candidate** |
| $\rho^*$ | 0.5 | Equilibrium density | $\rho^*_{\text{phys}} = 0.5 \cdot R_0$ | $4.27 \times 10^{-27}$ | kg m$^{-3}$ | **Anchored** |
| $\rho_{\max}$ | 1.0 | Capacity bound | $\rho_{\max,\text{phys}} = R_0$ | $8.53 \times 10^{-27}$ | kg m$^{-3}$ | **Anchored** |
| $M_0$ | 1.0 | Mobility prefactor | $M_{0,\text{phys}} = D_{\text{phys}}/D_{\text{nd}}$ | $2.263 \times 10^{25}$ | m$^2$ s$^{-1}$ | **Anchored** |
| $\beta$ | 2.0 | Mobility exponent (PME $m = 3$) | dimensionless | 2.0 | — | **Structural** |
| $P_0$ | 0.01–1.0 | Penalty slope | $P_{0,\text{phys}} = P_0 / T_0$ | $P_0 \cdot 2.377 \times 10^{-14}$ | s$^{-1}$ | **Anchored** |

**Status key** (extended from ED-Dimensional-03):

- **Observed**: determined by astrophysical measurement ($v_{\text{circ}}$, $\rho_{\text{crit}}$, $L_0$).
- **Constructed**: built from observables by dimensional analysis ($D_{\text{phys}} = v_{\text{circ}} \cdot L_0$). Not measured directly; justified by dynamical scaling.
- **Anchored**: uniquely determined once the observed/constructed scales are fixed.
- **ED-specific**: a prediction of the ED framework with no standard astrophysical counterpart.
- **Candidate**: physically motivated but not uniquely determined.
- **Structural**: dimensionless, unchanged by nondimensionalization.

---

## 4. The PDE in SI Units

Restoring all dimensional factors, the ED PDE in the galactic regime reads:

$$\partial_t \rho = (v_{\text{circ}} \cdot L_0)\bigl[M(\rho/R_0)\,\nabla^2\rho + M'(\rho/R_0)\,|\nabla\rho|^2/R_0 - P_0(\rho - \rho^*)/T_0\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr),$$

where $M(\hat{\rho}) = (1 - \hat{\rho})^\beta$, all spatial derivatives are in physical coordinates, and $T_0 = D_{\text{nd}} \cdot L_0/v_{\text{circ}}$.

The key observation: no fundamental constants appear. The dimensional PDE is written entirely in terms of astrophysical observables ($v_{\text{circ}}$, $L_0$, $R_0$) and the ED constitutive structure. Gravity enters implicitly through $v_{\text{circ}}$, which encodes the gravitational potential via $v_{\text{circ}}^2 \sim GM/R$.

**Newtonian limit.** When $M(\rho) \equiv 1$ (constant mobility), $H = 0$, and $P_0 = 0$, the PDE reduces to:

$$\partial_t \rho = D_{\text{phys}}\,\nabla^2 \rho,$$

which is the standard diffusion equation for mass redistribution on galactic timescales. The nonlinear mobility and penalty are ED's structural additions to this baseline.

---

## 5. Conversion Factor Table

### 5.1 Milky Way ($L_0 = 1$ kpc, $R_0 = \rho_{\text{crit}}$, $v_{\text{circ}} = 220$ km/s)

| Quantity | ND $\to$ SI | Numerical factor |
|:---------|:-----------|:-----------------|
| Length $x$ | $x_{\text{SI}} = \hat{x} \cdot L_0$ | $L_0 = 3.086 \times 10^{19}$ m $=$ 1 kpc |
| Time $t$ | $t_{\text{SI}} = \hat{t} \cdot T_0$ | $T_0 = 4.208 \times 10^{13}$ s $= 1.33$ Myr |
| Density $\rho$ | $\rho_{\text{SI}} = \hat{\rho} \cdot R_0$ | $R_0 = 8.53 \times 10^{-27}$ kg m$^{-3}$ |
| Velocity $v$ | $v_{\text{SI}} = \hat{v} \cdot V_0$ | $V_0 = 7.333 \times 10^{5}$ m s$^{-1}$ $= 733$ km/s |
| Diffusivity $D$ | $D_{\text{SI}} = D_{\text{nd}} \cdot L_0^2/T_0$ | $D_0 = 2.263 \times 10^{25}$ m$^2$ s$^{-1}$ |
| Mass $(d{=}3)$ | $m_{\text{SI}} = \hat{m} \cdot E_0$ | $E_0 = 2.506 \times 10^{32}$ kg $= 126\;M_\odot$ |

### 5.2 Dwarf Spheroidal ($L_0 = 0.7$ kpc, $R_0 = 10^{-24}$ kg/m$^3$, $v_{\text{circ}} = 15$ km/s)

| Quantity | ND $\to$ SI | Numerical factor |
|:---------|:-----------|:-----------------|
| Length $x$ | $x_{\text{SI}} = \hat{x} \cdot L_0$ | $L_0 = 2.160 \times 10^{19}$ m $= 0.7$ kpc |
| Time $t$ | $t_{\text{SI}} = \hat{t} \cdot T_0$ | $T_0 = 4.320 \times 10^{14}$ s $= 13.7$ Myr |
| Density $\rho$ | $\rho_{\text{SI}} = \hat{\rho} \cdot R_0$ | $R_0 = 1.0 \times 10^{-24}$ kg m$^{-3}$ |
| Velocity $v$ | $v_{\text{SI}} = \hat{v} \cdot V_0$ | $V_0 = 5.000 \times 10^{4}$ m s$^{-1}$ $= 50$ km/s |
| Mass $(d{=}3)$ | $m_{\text{SI}} = \hat{m} \cdot E_0$ | $E_0 = 1.008 \times 10^{34}$ kg $= 5070\;M_\odot$ |

**Code example** (using the existing `edsim.units` API):

```python
from edsim.core.parameters import EDParameters
from edsim.units import galactic_scales

params = EDParameters(d=3, L=(1.0, 1.0, 1.0), N=(64, 64, 64))
sc = galactic_scales(params)
print(f"L0 = {sc.L0:.4e} m  ({sc.L0/3.0857e19:.1f} kpc)")
print(f"T0 = {sc.T0:.4e} s")
print(f"R0 = {sc.R0:.4e} kg/m^3")
```

**Note on the current code.** The `galactic_scales()` factory does not accept $v_{\text{circ}}$ or `D_phys` as parameters. It uses the default convention $T_0 = L_0^2/D_{\text{nd}}$, which gives a time scale independent of the galaxy's dynamics. For physically anchored galactic simulations, `compute_scales(params, L0=kpc, R0=rho_crit, D_phys=v_circ*kpc)` should be called directly.

---

## 6. What Is Exact, What Is Candidate

### 6.1 Structural Identities (Regime-Independent)

The four structural identities hold in the galactic regime:

1. **PME reduction.** The mobility channel with $P_0 = 0$, $H = 0$ reduces to the porous-medium equation with $m = \beta + 1 = 3$. The Barenblatt exponent in $d = 3$: $\alpha_R = 1/8 = 0.125$. A density perturbation in the halo should spread with front radius $R(t) \propto t^{1/8}$, not the Gaussian $R(t) \propto t^{1/2}$ of standard diffusion.

2. **RC decay.** The penalty channel in isolation gives $\tau_{\text{RC}} = T_0/(D_{\text{nd}} P_0)$. For the Milky Way with $P_0 = 1.0$: $\tau_{\text{RC}} = 4.44$ Myr. This is the timescale for density perturbations to relax toward equilibrium — comparable to galactic dynamical times.

3. **Telegraph oscillation.** For $H = 5$: $T_{\text{osc}} = 2.81 \cdot T_0 = 3.75$ Myr (Milky Way). The participation variable oscillates on a multi-megayear timescale — slow enough to modulate galactic structure.

4. **Compact support.** The PME front has finite propagation speed. A density perturbation in the halo does not spread to infinity instantaneously (as Gaussian diffusion would predict) but advances at a finite, calculable rate.

### 6.2 Observed/Constructed Correspondences

- **$v_{\text{circ}}$**: directly measured from rotation curves (HI 21-cm line, stellar kinematics, or weak lensing). Typical uncertainties: 5–10%.
- **$L_0$**: set by the astrophysical context (scale radius from surface brightness fitting). Typical uncertainties: 10–20%.
- **$R_0$**: either $\rho_{\text{crit}}$ (known to $\sim 2\%$ from Planck CMB data) or a halo density (uncertain by factors of 2–10 depending on the profile model).
- **$D_{\text{phys}} = v_{\text{circ}} \cdot L_0$**: constructed. Not directly measured; justified by dimensional analysis and dynamical scaling. This is the weakest anchoring in the galactic dictionary.

### 6.3 Anchored Correspondences

Once $L_0$, $R_0$, and $D_{\text{phys}}$ are fixed, all remaining parameters are determined:

- $T_0 = D_{\text{nd}} \cdot L_0/v_{\text{circ}}$ (a fraction of the crossing time)
- $V_0 = v_{\text{circ}}/D_{\text{nd}}$ (a multiple of the circular velocity)
- $\rho^* = 0.5 \cdot R_0$ (equilibrium density)
- All physical-unit parameter values follow

### 6.4 Candidate Correspondences

The participation channel has suggestive but unconfirmed galactic interpretations:

- **$v(t)$ as a galactic collective mode.** ED-I-002 interprets the participation variable as a "temporal tension" field driven by the aggregate dynamical activity (star formation, supernovae, AGN feedback) of the galaxy. This is physically motivated — galaxies do exhibit global feedback cycles — but the identification is not unique.
- **$\tau_{\text{phys}} \sim 1$ Myr (MW).** This is comparable to the timescale of supernova remnant evolution and OB association lifetimes. If the participation channel represents feedback from star-forming activity, the timescale is in the right range.
- **$H$ as feedback coupling.** The coupling between the global participation mode and the local density field could represent how large-scale galactic processes (bar instabilities, spiral arm passage, AGN winds) influence local density evolution.

### 6.5 The Mobility at Galactic Scales

The density-dependent mobility $M(\rho) = M_0(1 - \hat{\rho})^\beta$ predicts that mass transport slows as the local density approaches the capacity bound $R_0$. In the galactic context, this has a striking interpretation:

**Density-dependent gravitational transport.** Standard gravitational dynamics (Poisson equation + collisionless Boltzmann) has no density-dependent diffusivity. The diffusion of stars and dark matter through phase space is density-independent in the collisionless limit. ED predicts a departure: as the local density approaches $\rho_{\max}$, transport halts.

This is the galactic analogue of the mobility prediction in all other regimes. It predicts:

- **Horizon formation** in galactic cores where $\rho \to R_0$: a region where mass transport is suppressed, potentially corresponding to the cores of cuspy NFW profiles or the observed "core" profiles of dwarf galaxies.
- **Density-dependent halo profiles.** The PME self-similar solution produces profiles qualitatively different from both NFW ($\rho \propto r^{-1}$) and isothermal ($\rho \propto r^{-2}$) haloes. The ED profile has compact support and a well-defined edge — a prediction that can be compared against observed halo truncation radii.

---

## 7. Falsifiable Predictions

### 7.1 Predictions That Follow From the Mapping

1. **Dynamical timescale.** For the Milky Way: $T_0 = 1.33$ Myr. Density perturbations of kpc spatial extent should evolve on this timescale. This is consistent with known galactic dynamical times but provides a specific numerical value.

2. **PME spreading exponent.** A density perturbation in the halo should spread as $R(t) \propto t^{1/8}$ ($d = 3$, $m = 3$), not $t^{1/2}$. The front should be sharp, not Gaussian. This is testable against N-body simulations of halo relaxation after a perturbation (e.g., satellite accretion).

3. **Penalty relaxation time.** For the MW with $P_0 = 1$: $\tau_{\text{RC}} = 4.44$ Myr. A galactic density perturbation (e.g., from a minor merger) should relax exponentially with this time constant. Observable via the age-dating of tidal features.

4. **Horizon formation in dense cores.** Where $\rho \to R_0$, mobility vanishes. For the MW at $R_0 = \rho_{\text{crit}}$, this occurs at unrealistically low densities. For a dwarf spheroidal at $R_0 = 10^{-24}$ kg m$^{-3}$, horizons form when the central density approaches this value — plausibly in the inner $\sim 100$ pc. ED predicts a sharp transition in transport properties at this radius: a testable prediction against observed core-cusp profiles.

5. **Compact support of density profiles.** Standard dark-matter haloes extend to the virial radius with gradually declining density. ED predicts a sharp edge (compact support of the PME solution). The existence or absence of a well-defined halo boundary at a specific radius is a falsifiable prediction.

6. **Participation-modulated dynamics.** For the MW at $H = 5$: $T_{\text{osc}} = 3.75$ Myr. If the participation channel is physical, the galaxy should exhibit quasi-periodic global fluctuations on this timescale. Possible observational signatures: periodic modulation of the star formation rate (detected in some studies at $\sim 5$–$10$ Myr periods) or oscillatory features in the gaseous halo.

### 7.2 What Would Falsify the Mapping

- If halo density profiles show no evidence of compact support or sharp edges, the PME prediction is weakened. (Note: this tests the mobility constitutive choice, not the mapping framework.)
- If no density-dependent transport is observed in N-body simulations or galactic dynamics, the mobility channel ($\beta > 0$) is unsupported at galactic scales.
- If the relaxation timescale of tidal features is inconsistent with $\tau_{\text{RC}}$, the penalty anchoring is falsified.
- If the dynamical diffusivity $D_{\text{phys}} = v_{\text{circ}} \cdot L_0$ produces timescales grossly inconsistent with observed galactic evolution, the constructed anchoring fails.

### 7.3 What Would Not Falsify the Mapping

- The participation channel is a candidate. Absence of observable telegraph oscillation does not falsify the structural core.
- The choice $R_0 = \rho_{\text{crit}}$ is conventional. If a different $R_0$ (e.g., a halo-specific NFW central density) produces better predictions, the framework holds with a different density normalisation.
- The value $\beta = 2$ is a constitutive choice. Different mobility exponents may be appropriate for different galaxies.

---

## 8. Open Questions

1. **Is $D_{\text{phys}} = v_{\text{circ}} \cdot L_0$ the right diffusivity?** This is a dimensional construction, not a derivation. Alternative choices include the ISM turbulent diffusivity ($\sim 10^{21}$ m$^2$/s — three orders of magnitude smaller), the cosmic-ray diffusivity ($\sim 3 \times 10^{24}$ m$^2$/s — comparable to $v_{\text{circ}} L_0$), or a gravitational Brownian-motion diffusivity. The choice of $D_{\text{phys}}$ is the most uncertain element of the galactic mapping.

2. **Dark matter interpretation.** The ED interpretation papers (ED-I-002, ED-I-027) propose that flat rotation curves arise from temporal tension rather than dark matter. This note does not adjudicate that claim. It provides the dimensional framework within which such claims could, in principle, be made quantitatively. The critical test: can an ED simulation with the galactic dictionary reproduce a measured rotation curve (e.g., from SPARC data) without dark matter? This has not been attempted.

3. **NFW vs. ED density profiles.** The PME self-similar solution has compact support and a specific radial profile. How does this compare quantitatively to NFW, isothermal, Burkert, or cored profiles? The comparison requires running ED-SIM-02 at galactic scales and extracting the radial density profile. This is future work.

4. **Mobility exponent and the core-cusp problem.** The cusp-core controversy in dwarf galaxy haloes concerns whether central density profiles are cuspy ($\rho \propto r^{-1}$, NFW) or cored ($\rho \sim$ const, observed). ED's degenerate mobility naturally produces cores: near $\rho_{\max}$, transport halts and the density cannot steepen further. Whether the ED core size matches observed core radii depends on $\beta$ and $R_0$. This is a quantitative test.

5. **Scale dependence of $R_0$.** Using $R_0 = \rho_{\text{crit}}$ for the MW gives $\rho_{\max} = 8.53 \times 10^{-27}$ kg m$^{-3}$ — far below the central density of any real galaxy. This means $\hat{\rho} \gg 1$ in galactic cores, which violates the assumption $\hat{\rho} \in [0,1]$. In practice, $R_0$ should be chosen to match the physical maximum density of the system (e.g., the central density of the halo). The `galactic_scales()` default of $R_0 = \rho_{\text{crit}}$ is appropriate for large-scale cosmological simulations but not for individual galaxies. A galaxy-specific $R_0$ is needed.

6. **Participation channel and star-formation feedback.** The strongest physical candidate for $v(t)$ at galactic scales is the global star-formation feedback cycle. Star formation heats and disrupts the ISM, reducing local density; the reduced density lowers the star-formation rate; the gas cools and re-collapses. This cycle has a natural period of $\sim 5$–$50$ Myr, comparable to $T_{\text{osc}}$ for the MW. Whether the ED participation equation ($\dot{v} = (\bar{F} - \zeta v)/\tau$) quantitatively reproduces observed feedback cycles is an open question.

7. **Code update.** The `galactic_scales()` factory should accept $v_{\text{circ}}$ and optionally a galaxy-specific $R_0$ to enable physically anchored galactic simulations.

---

## 9. Other Regimes (Preview)

| Regime | $L_0$ | $R_0$ | $D_{\text{phys}}$ | Anchoring | Note |
|--------|--------|--------|---------------------|-----------|------|
| Quantum | $\hbar/(mc)$ | $L_0^{-d}$ | $\hbar/(2m)$ | Madelung theorem | ED-Dimensional-01 |
| Planck | $\ell_{\text{Pl}}$ | $\rho_{\text{Pl}}$ | $\sqrt{\hbar G/c}$ | Dimensional uniqueness | ED-Dimensional-02 |
| Condensed matter | Experimental | Material density | Thermal diffusivity | Laboratory measurement | ED-Dimensional-03 |
| **Galactic** (this note) | 1 kpc | $\rho_{\text{crit}}$ or halo | $v_{\text{circ}} \cdot L_0$ | Dynamical scaling | ED-Dimensional-04 |
| Cosmological | $c/H_0$ | $\rho_{\text{crit}}$ | $c^2/H_0$ (or similar) | Hubble scales | ED-Dimensional-05 |

The galactic regime is the fourth note because it is the first to invoke a constructed (not measured or derived) diffusivity. The anchoring $D_{\text{phys}} = v_{\text{circ}} \cdot L_0$ is dimensionally natural but not independently measured, making this regime intermediate in rigor between the condensed-matter regime (fully empirical) and the cosmological regime (fully conventional).

---

## Appendix A: Derivation of $T_0$ and $V_0$

Starting from $D_{\text{phys}} = v_{\text{circ}} \cdot L_0$ and $T_0 = L_0^2 D_{\text{nd}} / D_{\text{phys}}$:

$$T_0 = \frac{L_0^2 \cdot D_{\text{nd}}}{v_{\text{circ}} \cdot L_0} = \frac{D_{\text{nd}} \cdot L_0}{v_{\text{circ}}} = D_{\text{nd}} \cdot t_{\text{cross}}.$$

$$V_0 = \frac{L_0}{T_0} = \frac{L_0}{D_{\text{nd}} \cdot L_0 / v_{\text{circ}}} = \frac{v_{\text{circ}}}{D_{\text{nd}}}.$$

**Verification** ($D_{\text{phys}} \cdot T_0 / L_0^2 = D_{\text{nd}}$):

$$\frac{v_{\text{circ}} L_0 \cdot D_{\text{nd}} L_0 / v_{\text{circ}}}{L_0^2} = D_{\text{nd}}. \quad \checkmark$$

---

## Appendix B: Comparison Across All Four Regimes ($d = 3$)

| Scale | Quantum (e$^-$) | Planck | Condensed (Si) | Galactic (MW) |
|:------|:-----------------|:-------|:----------------|:--------------|
| $L_0$ (m) | $3.86 \times 10^{-13}$ | $1.62 \times 10^{-35}$ | $1.00 \times 10^{-6}$ | $3.09 \times 10^{19}$ |
| $T_0$ (s) | $7.73 \times 10^{-22}$ | $1.62 \times 10^{-44}$ | $3.41 \times 10^{-9}$ | $4.21 \times 10^{13}$ |
| $D_{\text{phys}}$ (m$^2$/s) | $5.79 \times 10^{-5}$ | $4.85 \times 10^{-27}$ | $8.80 \times 10^{-5}$ | $6.79 \times 10^{24}$ |
| $V_0$ (m/s) | $5.00 \times 10^{8}$ | $9.99 \times 10^{8}$ | $2.93 \times 10^{2}$ | $7.33 \times 10^{5}$ |
| $V_0/c$ | 1.667 | 3.333 | $9.8 \times 10^{-7}$ | $2.4 \times 10^{-3}$ |
| $D_{\text{phys}}$ anchoring | Theorem | Dimensional | Measured | Constructed |

The four regimes span 54 orders of magnitude in length ($10^{-35}$ to $10^{19}$ m) and 57 orders of magnitude in time ($10^{-44}$ to $10^{13}$ s). The ED nondimensionalization maps all of them onto the same canonical PDE with $\hat{D} = D_{\text{nd}} = 0.3$. The velocity scale is superluminal at quantum and Planck scales, subluminal at condensed-matter and galactic scales — a natural boundary separating regimes where the parabolic PDE is adequate from those requiring a hyperbolic extension.

---

## References

1. Proxmire, A. "ED-Dimensional-01 through 03." ED-Dimensional series (2026).
2. Proxmire, A. "Event Density as an Ontological Framework." Foundational Paper (2026).
3. Proxmire, A. "ED-I-002: Event Density and Galactic Curvature." (2025).
4. Proxmire, A. "ED-I-027: Temporal Tension in Galaxy-Scale Weak Lensing." (2026).
5. Navarro, J. F., Frenk, C. S., and White, S. D. M. "The Structure of Cold Dark Matter Halos." *Astrophys. J.* **462**, 563–575 (1996).
6. McGaugh, S. S., Lelli, F., and Schombert, J. M. "Radial Acceleration Relation in Rotationally Supported Galaxies." *Phys. Rev. Lett.* **117**, 201101 (2016).
7. Lelli, F., McGaugh, S. S., and Schombert, J. M. "SPARC: Mass Models for 175 Disk Galaxies." *Astron. J.* **152**, 157 (2016).
8. Vazquez, J. L. *The Porous Medium Equation.* Oxford University Press (2007).
