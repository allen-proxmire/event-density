# ED-Dimensional-03: Physical Units and Dimensional Mapping — The Condensed-Matter Regime

**Allen Proxmire**
**March 2026**

---

**Canonical sources:**

| Source | Content used |
|--------|-------------|
| Critical Assessment (2026-03-27) | The challenge being addressed |
| ED-Dimensional-01 (Quantum Regime) | Nondimensionalization scheme, status classification, series template |
| ED-Dimensional-02 (Planck Regime) | Planck anchoring for cross-regime comparison |
| ED Foundational Paper | Canonical PDE, Appendix A parameters, Appendix D PME derivation |
| `edsim/units/constants.py` | CODATA 2018 physical constants |
| `edsim/units/scales.py` | `Scales` dataclass, `compute_scales()`, `condensed_matter_scales()` |
| `docs/units.md` | Nondimensionalization scheme |
| CRC Handbook of Chemistry and Physics | Thermal diffusivities and densities of materials |

**Scope.** This note addresses the condensed-matter regime, where all three characteristic scales are set by experimentally measured material properties rather than by fundamental constants or dimensional analysis. It is the third in the ED-Dimensional series and the first regime in which the anchoring is directly falsifiable against laboratory data.

---

## 0. The Challenge

ED-Dimensional-01 (quantum) anchored $D_{\text{phys}}$ to $\hbar/(2m)$ via a mathematical theorem. ED-Dimensional-02 (Planck) anchored all scales via dimensional uniqueness from $\hbar$, $G$, $c$. Both regimes are remote from direct experimental measurement.

The condensed-matter regime changes this. Here, the characteristic scales — length, density, diffusivity — are laboratory-measurable quantities with known values for specific materials. This makes the regime the most directly falsifiable in the ED-Dimensional series: every predicted timescale, relaxation rate, and spreading exponent can be compared against experimental data.

The cost is that the anchoring is no longer unique. The choice of $L_0$, $R_0$, and $D_{\text{phys}}$ depends on the material and the experimental context. The mapping is a family of dictionaries parameterised by material properties, not a single universal table.

This note does **not** claim that ED describes any specific condensed-matter system. It claims that ED, when anchored to the thermal diffusivity and mass density of a specific material, produces quantitative predictions in SI units that can be tested against transport measurements, relaxation experiments, and pattern-formation studies.

---

## 1. The Nondimensionalization Scheme

The general scheme is identical to ED-Dimensional-01, Section 1. The canonical ED PDE in physical (SI) units is:

$$\partial_t \rho = D_{\text{phys}}\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr).$$

Three characteristic scales ($L_0$, $T_0$, $R_0$) and two derived scales ($V_0 = L_0/T_0$, $E_0 = R_0 \cdot L_0^d$) define the mapping:

$$\hat{x} = x/L_0, \quad \hat{t} = t/T_0, \quad \hat{\rho} = \rho/R_0, \quad \hat{v} = v/V_0.$$

After substitution, the nondimensional PDE has $\hat{D} = D_{\text{nd}}$ by construction of $T_0$.

---

## 2. The Condensed-Matter Regime: Scale Anchoring

### 2.1 Density: $\rho \to$ Mass Density

In the condensed-matter regime, the ED density field is identified with mass density (or concentration, or number density, depending on the application):

$$\rho(x,t) \;\to\; \text{mass density [kg m}^{-3}\text{]}.$$

The density scale $R_0$ is set by the material:

$$R_0 = \rho_{\text{material}} \quad [\text{kg m}^{-3}].$$

For a liquid or solid, $R_0$ is the bulk density at the relevant temperature and pressure. The ED field $\hat{\rho} \in [0,1]$ then represents the fraction of the local density relative to the material's bulk value. The capacity bound $\rho_{\max} = R_0$ is the close-packing or bulk density — the physical maximum.

### 2.2 Length: $L_0 =$ Experimental Length Scale

The length scale is set by the experiment:

$$L_0 = \text{domain size, film thickness, grain size, etc.}$$

There is no canonical choice. Common values include:

| Application | Typical $L_0$ |
|-------------|---------------|
| Thin films, coatings | $10^{-7}$ m (100 nm) |
| Microfluidics, colloids | $10^{-6}$ m (1 $\mu$m) |
| Grain-scale metallurgy | $10^{-5}$ to $10^{-4}$ m |
| Macroscopic heat transfer | $10^{-3}$ to $10^{-1}$ m |

Throughout this note, the default is $L_0 = 10^{-6}$ m (1 $\mu$m) unless stated otherwise. This is the natural scale for colloidal dynamics, thin-film diffusion, and microscale transport — the regime where ED's nonlinear mobility is most likely to have observable consequences.

### 2.3 Diffusivity: $D_{\text{phys}} =$ Thermal Diffusivity

The physical diffusivity is the thermal diffusivity of the material:

$$D_{\text{phys}} = \frac{\kappa}{\rho\,c_p} \quad [\text{m}^2\text{ s}^{-1}],$$

where $\kappa$ is the thermal conductivity, $\rho$ is the mass density, and $c_p$ is the specific heat capacity. For mass diffusion (e.g., solute transport), $D_{\text{phys}}$ is the mass diffusivity. For charge transport, $D_{\text{phys}}$ is the charge diffusivity.

Unlike the quantum and Planck regimes, where $D_{\text{phys}}$ is fixed by fundamental constants, the condensed-matter diffusivity is a measured material property. This is the key difference: the anchoring is empirical, not theoretical.

**Representative values:**

| Material | $D_{\text{phys}}$ (m$^2$/s) | $\rho$ (kg/m$^3$) | Source |
|----------|------------------------------|---------------------|--------|
| Water (25$^\circ$C) | $1.43 \times 10^{-7}$ | 997 | Thermal diffusivity |
| Silicon (300 K) | $8.80 \times 10^{-5}$ | 2329 | Thermal diffusivity |
| Copper (300 K) | $1.17 \times 10^{-4}$ | 8960 | Thermal diffusivity |

### 2.4 Time Scale

$$T_0 = \frac{L_0^2\,D_{\text{nd}}}{D_{\text{phys}}}.$$

For $L_0 = 1\;\mu$m and $D_{\text{nd}} = 0.3$:

| Material | $D_{\text{phys}}$ | $T_0$ | Physical meaning |
|----------|---------------------|-------|------------------|
| Water | $1.43 \times 10^{-7}$ m$^2$/s | $2.098 \times 10^{-6}$ s ($\sim 2\;\mu$s) | Thermal equilibration over 1 $\mu$m |
| Silicon | $8.80 \times 10^{-5}$ m$^2$/s | $3.409 \times 10^{-9}$ s ($\sim 3.4$ ns) | Phonon transport across 1 $\mu$m |
| Copper | $1.17 \times 10^{-4}$ m$^2$/s | $2.564 \times 10^{-9}$ s ($\sim 2.6$ ns) | Electron-mediated heat transport across 1 $\mu$m |

These are experimentally accessible timescales. Ultrafast laser pump-probe experiments routinely resolve nanosecond and sub-nanosecond dynamics. Microfluidic experiments operate on microsecond to millisecond timescales. The ED time scale $T_0$ falls squarely within the range of laboratory measurement.

### 2.5 Velocity Scale

$$V_0 = \frac{L_0}{T_0} = \frac{D_{\text{phys}}}{L_0 \cdot D_{\text{nd}}}.$$

| Material | $V_0$ (m/s) | Comparison |
|----------|------------|------------|
| Water | 0.477 | Well below sound speed in water ($\sim 1500$ m/s) |
| Silicon | 293 | Comparable to phonon group velocities |
| Copper | 390 | Comparable to electron drift velocities at high fields |

Unlike the quantum and Planck regimes, the condensed-matter velocity scale is subluminal and physically meaningful. For water, $V_0$ is a gentle flow speed. For silicon and copper, $V_0$ is on the order of relevant transport velocities. No superluminal caveat is needed.

### 2.6 Energy Scale

$$E_0 = R_0 \cdot L_0^d.$$

For $d = 3$ and $L_0 = 1\;\mu$m:

| Material | $E_0$ (kg) | Physical meaning |
|----------|-----------|------------------|
| Water | $9.970 \times 10^{-16}$ | Mass of water in a 1 $\mu$m$^3$ cube |
| Silicon | $2.329 \times 10^{-15}$ | Mass of silicon in a 1 $\mu$m$^3$ cube |
| Copper | $8.960 \times 10^{-15}$ | Mass of copper in a 1 $\mu$m$^3$ cube |

---

## 3. The ED-to-Condensed-Matter Dictionary

Every canonical ED parameter is mapped to its condensed-matter physical quantity. Numerical values are given for **silicon** at $L_0 = 1\;\mu$m, $d = 3$, $D_{\text{nd}} = 0.3$.

| ED Parameter | Canonical value | Physical quantity | Formula (SI) | Value (Si) | Unit | Status |
|:-------------|:----------------|:------------------|:-------------|:-----------|:-----|:-------|
| $\rho$ | field in $[0,1]$ | Mass density | $\rho_{\text{phys}} = \hat{\rho} \cdot R_0$ | $\hat{\rho} \cdot 2329$ | kg m$^{-3}$ | **Measured** |
| $D$ | 0.3 | Thermal diffusivity | $D_{\text{phys}} = \kappa/(\rho c_p)$ | $8.80 \times 10^{-5}$ | m$^2$ s$^{-1}$ | **Measured** |
| $M(\rho)$ | $M_0(1 - \hat{\rho})^\beta$ | Density-dependent mobility | $M_{\text{phys}} = M_0(1 - \hat{\rho})^\beta \cdot D_{\text{phys}}/D_{\text{nd}}$ | (state-dependent) | m$^2$ s$^{-1}$ | **ED-specific** |
| $P(\rho)$ | $P_0(\hat{\rho} - \hat{\rho}^*)$ | Restoring force (thermal equilibration) | $P_{\text{phys}} = P_0(\hat{\rho} - \hat{\rho}^*) \cdot R_0/T_0$ | (state-dependent) | kg m$^{-3}$ s$^{-1}$ | **Anchored** |
| $v(t)$ | scalar | Global mode amplitude | $v_{\text{phys}} = \hat{v} \cdot V_0$ | $\hat{v} \cdot 293$ | m s$^{-1}$ | **Candidate** |
| $H$ | 0–50 | Global coupling strength | $H_{\text{phys}} = H_{\text{nd}} \cdot V_0$ | $H_{\text{nd}} \cdot 293$ | m s$^{-1}$ | **Candidate** |
| $\tau$ | 1.0 | Relaxation timescale | $\tau_{\text{phys}} = \tau_{\text{nd}} \cdot T_0$ | $3.409 \times 10^{-9}$ | s | **Candidate** |
| $\zeta$ | 0.1 | Damping rate | $\zeta_{\text{phys}} = \zeta_{\text{nd}} / T_0$ | $2.933 \times 10^{7}$ | s$^{-1}$ | **Candidate** |
| $\rho^*$ | 0.5 | Equilibrium density | $\rho^*_{\text{phys}} = 0.5 \cdot R_0$ | 1164.5 | kg m$^{-3}$ | **Anchored** |
| $\rho_{\max}$ | 1.0 | Bulk / close-packing density | $\rho_{\max,\text{phys}} = R_0$ | 2329 | kg m$^{-3}$ | **Measured** |
| $M_0$ | 1.0 | Mobility prefactor | $M_{0,\text{phys}} = D_{\text{phys}}/D_{\text{nd}}$ | $2.933 \times 10^{-4}$ | m$^2$ s$^{-1}$ | **Anchored** |
| $\beta$ | 2.0 | Mobility exponent (PME $m = 3$) | dimensionless | 2.0 | — | **Structural** |
| $P_0$ | 0.01–1.0 | Penalty slope | $P_{0,\text{phys}} = P_0 / T_0$ | $P_0 \cdot 2.933 \times 10^{8}$ | s$^{-1}$ | **Anchored** |

**Status key** (extended from ED-Dimensional-01):

- **Measured**: determined by laboratory measurement of the specific material. This is the strongest anchoring available in the condensed-matter regime.
- **Anchored**: uniquely determined once the measured scales ($L_0$, $R_0$, $D_{\text{phys}}$) are fixed.
- **ED-specific**: a prediction of the ED framework with no standard counterpart in classical transport theory.
- **Candidate**: physically motivated but not uniquely determined.
- **Structural**: a dimensionless constitutive parameter, unchanged by nondimensionalization.

---

## 4. The PDE in SI Units

Restoring all dimensional factors, the ED PDE in the condensed-matter regime reads:

$$\partial_t \rho = D_{\text{therm}}\bigl[M(\rho/R_0)\,\nabla^2\rho + M'(\rho/R_0)\,|\nabla\rho|^2/R_0 - P_0(\rho - \rho^*)/T_0\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr),$$

where $D_{\text{therm}} = \kappa/(\rho c_p)$ is the thermal diffusivity of the material, $M(\hat{\rho}) = (1 - \hat{\rho})^\beta$, and all spatial derivatives are in physical coordinates.

The key observation: no fundamental constants appear. The dimensional PDE is written entirely in terms of measurable material properties ($D_{\text{therm}}$, $R_0$, $L_0$) and the ED constitutive structure ($M$, $P$, $v$). This is the regime where ED is closest to being an empirically testable transport equation.

**Standard diffusion limit.** When $M(\rho) \equiv 1$ (constant mobility, $\beta = 0$) and $H = 0$, the PDE reduces to:

$$\partial_t \rho = D_{\text{therm}}\bigl[\nabla^2\rho - P_0(\rho - \rho^*)/T_0\bigr],$$

which is the standard reaction-diffusion equation: Fickian diffusion with a linear source term. The ED framework recovers classical heat/mass transfer as a special case.

---

## 5. Conversion Factor Table

Compact reference for converting ED-SIM-02 simulation output to SI units ($L_0 = 1\;\mu$m, $d = 3$, $D_{\text{nd}} = 0.3$):

### 5.1 Water (25$^\circ$C)

| Quantity | ND $\to$ SI | Numerical factor |
|:---------|:-----------|:-----------------|
| Length $x$ | $x_{\text{SI}} = \hat{x} \cdot L_0$ | $L_0 = 1.000 \times 10^{-6}$ m |
| Time $t$ | $t_{\text{SI}} = \hat{t} \cdot T_0$ | $T_0 = 2.098 \times 10^{-6}$ s |
| Density $\rho$ | $\rho_{\text{SI}} = \hat{\rho} \cdot R_0$ | $R_0 = 997$ kg m$^{-3}$ |
| Velocity $v$ | $v_{\text{SI}} = \hat{v} \cdot V_0$ | $V_0 = 4.767 \times 10^{-1}$ m s$^{-1}$ |
| Diffusivity $D$ | $D_{\text{SI}} = D_{\text{nd}} \cdot L_0^2/T_0$ | $D_0 = 4.767 \times 10^{-7}$ m$^2$ s$^{-1}$ |

### 5.2 Silicon (300 K)

| Quantity | ND $\to$ SI | Numerical factor |
|:---------|:-----------|:-----------------|
| Length $x$ | $x_{\text{SI}} = \hat{x} \cdot L_0$ | $L_0 = 1.000 \times 10^{-6}$ m |
| Time $t$ | $t_{\text{SI}} = \hat{t} \cdot T_0$ | $T_0 = 3.409 \times 10^{-9}$ s |
| Density $\rho$ | $\rho_{\text{SI}} = \hat{\rho} \cdot R_0$ | $R_0 = 2329$ kg m$^{-3}$ |
| Velocity $v$ | $v_{\text{SI}} = \hat{v} \cdot V_0$ | $V_0 = 2.933 \times 10^{2}$ m s$^{-1}$ |
| Diffusivity $D$ | $D_{\text{SI}} = D_{\text{nd}} \cdot L_0^2/T_0$ | $D_0 = 2.933 \times 10^{-4}$ m$^2$ s$^{-1}$ |

### 5.3 Copper (300 K)

| Quantity | ND $\to$ SI | Numerical factor |
|:---------|:-----------|:-----------------|
| Length $x$ | $x_{\text{SI}} = \hat{x} \cdot L_0$ | $L_0 = 1.000 \times 10^{-6}$ m |
| Time $t$ | $t_{\text{SI}} = \hat{t} \cdot T_0$ | $T_0 = 2.564 \times 10^{-9}$ s |
| Density $\rho$ | $\rho_{\text{SI}} = \hat{\rho} \cdot R_0$ | $R_0 = 8960$ kg m$^{-3}$ |
| Velocity $v$ | $v_{\text{SI}} = \hat{v} \cdot V_0$ | $V_0 = 3.900 \times 10^{2}$ m s$^{-1}$ |
| Diffusivity $D$ | $D_{\text{SI}} = D_{\text{nd}} \cdot L_0^2/T_0$ | $D_0 = 3.900 \times 10^{-4}$ m$^2$ s$^{-1}$ |

**Code example** (using the existing `edsim.units` API):

```python
from edsim.core.parameters import EDParameters
from edsim.units import condensed_matter_scales

params = EDParameters(d=3, L=(1.0, 1.0, 1.0), N=(64, 64, 64))

# Silicon at 1 micron
sc = condensed_matter_scales(params, L0=1e-6, R0=2329.0)
print(f"L0 = {sc.L0:.4e} m")
print(f"T0 = {sc.T0:.4e} s")
print(f"V0 = {sc.V0:.4e} m/s")
```

**Note on the current code.** The `condensed_matter_scales()` factory does not accept `D_phys` as a parameter. It uses the default convention `T0 = L0^2/D_nd`, which gives $T_0 = 3.33 \times 10^{-6}$ s for $L_0 = 1\;\mu$m — independent of the material. For physically anchored simulations, `D_phys` should be passed to `compute_scales()` directly. The numerical values in this note use the physically anchored convention $T_0 = L_0^2 D_{\text{nd}} / D_{\text{phys}}$.

---

## 6. What Is Exact, What Is Candidate

### 6.1 Structural Identities (Regime-Independent)

The four structural identities from ED-Dimensional-01 hold in any regime, including condensed matter:

1. **PME reduction.** The mobility channel with $P_0 = 0$, $H = 0$ reduces exactly to the porous-medium equation with $m = \beta + 1$. For $\beta = 2$: $m = 3$, and the Barenblatt front-radius exponent in $d = 3$ is $\alpha_R = 1/(d(m-1)+2) = 1/8 = 0.125$. This is a testable prediction: a density perturbation in a material with density-dependent mobility should spread with front radius $R(t) \propto t^{1/8}$.

2. **RC decay.** The penalty channel in isolation produces exponential decay with time constant $\tau_{\text{RC}} = T_0/(D_{\text{nd}} P_0)$. For silicon at $L_0 = 1\;\mu$m and $P_0 = 1.0$: $\tau_{\text{RC}} = 1.136 \times 10^{-8}$ s ($\sim 11$ ns). This is a measurable relaxation time.

3. **Telegraph oscillation.** For $H = 5$, canonical parameters, silicon: $T_{\text{osc}} = 9.589 \times 10^{-9}$ s ($\sim 10$ ns). This is within the range of ultrafast pump-probe experiments.

4. **Compact support.** The PME solution has finite propagation speed. A thermal perturbation in a material with density-dependent diffusivity should have a sharp front — not the Gaussian tails predicted by Fourier's law with constant diffusivity.

### 6.2 Measured Correspondences

In the condensed-matter regime, three parameters are determined by direct laboratory measurement:

- **$D_{\text{phys}}$**: thermal diffusivity, measured by laser flash analysis, transient hot-wire methods, or modulated DSC. Typical uncertainties: 2–5%.
- **$R_0$**: mass density, measured by pycnometry, Archimedes' method, or X-ray diffraction. Typical uncertainties: 0.1%.
- **$L_0$**: domain size, set by the experiment (film thickness, channel width, grain size). Uncertainty depends on fabrication tolerance.

These are the strongest possible anchoring: direct measurement, not theoretical inference.

### 6.3 Anchored Correspondences

Once $L_0$, $R_0$, and $D_{\text{phys}}$ are measured, the following are uniquely determined:

- $T_0 = L_0^2 D_{\text{nd}} / D_{\text{phys}}$
- $V_0 = L_0/T_0 = D_{\text{phys}}/(L_0 D_{\text{nd}})$
- $E_0 = R_0 \cdot L_0^d$
- $M_{0,\text{phys}} = D_{\text{phys}}/D_{\text{nd}}$
- $P_{0,\text{phys}} = P_0/T_0$

### 6.4 Candidate Correspondences

The participation channel parameters have no established condensed-matter counterpart:

- **$v(t)$ as a collective thermal mode.** Possible interpretations include a spatially averaged temperature fluctuation, a phonon bath mode, or a global order parameter. None is uniquely determined.
- **$\tau$ as a thermal relaxation time.** For silicon: $\tau_{\text{phys}} = 3.41 \times 10^{-9}$ s. This is comparable to phonon-phonon scattering times at room temperature ($\sim 1$–$10$ ns), suggesting a possible physical identification — but not a unique one.
- **$H$ as a phonon-bath coupling.** The participation coupling could represent the feedback between the local density field and a global thermal reservoir. The identification is plausible but not established.

### 6.5 The Mobility: From Prediction to Measurement

The density-dependent mobility $M(\rho) = M_0(1 - \hat{\rho})^\beta$ is the defining structural feature of ED. In the condensed-matter regime, it predicts:

**Density-dependent thermal diffusivity.** Standard Fourier heat conduction assumes constant thermal diffusivity. ED predicts that diffusivity decreases as the local density approaches the bulk value and vanishes at close-packing. This is not exotic: concentration-dependent diffusion is well documented in metallurgy, polymer science, and colloidal suspensions. The specific functional form $M \propto (1 - \hat{\rho})^\beta$ with $\beta = 2$ is the ED constitutive choice.

**Comparison with known physics:**

| Feature | Fourier / Fick (standard) | ED prediction |
|---------|---------------------------|---------------|
| Diffusivity | Constant | Density-dependent: $D_{\text{eff}} \propto (1 - \rho/\rho_{\max})^\beta$ |
| Front shape | Gaussian tails (infinite propagation) | Compact support (sharp front) |
| Spreading exponent | $\alpha_R = 1/2$ (all $d$) | $\alpha_R = 1/(d(m-1)+2) = 1/8$ ($d = 3$, $m = 3$) |
| Capacity bound | None | $\rho_{\max}$ (mobility vanishes) |

The condensed-matter regime is where this prediction is most directly testable: diffusivity measurements as a function of concentration or density are routine in materials science.

---

## 7. Falsifiable Predictions

### 7.1 Predictions That Follow From the Mapping

1. **Diffusion timescale.** For silicon at $L_0 = 1\;\mu$m: $T_0 = 3.41$ ns. A thermal perturbation of spatial extent $\sim 1\;\mu$m should equilibrate on a timescale of order $T_0$. This is directly measurable by laser flash or pump-probe experiments.

2. **Density-dependent diffusivity.** ED predicts that thermal or mass diffusivity decreases as $\rho \to \rho_{\max}$ and vanishes at close-packing. For a colloidal suspension approaching the glass transition, the effective diffusivity should decrease as $(1 - \phi/\phi_{\max})^\beta$ where $\phi$ is the volume fraction. This is experimentally testable by dynamic light scattering (DLS) or fluorescence recovery after photobleaching (FRAP).

3. **PME spreading exponent.** A density perturbation spreading in a medium with density-dependent diffusivity should follow $R(t) \propto t^{1/8}$ (for $d = 3$, $\beta = 2$), rather than the Gaussian $R(t) \propto t^{1/2}$. The front should be sharp, not diffuse. This can be tested by tracking the spreading of a dye pulse in a concentrated colloidal suspension.

4. **Compact support.** The PME solution has finite propagation speed. Beyond the front, no transport has occurred. This contrasts with Fourier's law, where the temperature field has Gaussian tails extending to infinity. In practice, Gaussian tails decay exponentially and may be undetectable — but the *qualitative shape* of the front (sharp vs. diffuse) is measurable.

5. **Penalty relaxation rate.** For silicon, $P_0 = 1.0$: $\tau_{\text{RC}} = 11.4$ ns. For water: $\tau_{\text{RC}} = 7.0\;\mu$s. These are the timescales for density perturbations to relax back to equilibrium. Measurable by transient absorption or thermal-lens spectroscopy.

6. **Telegraph oscillation period.** For silicon at $H = 5$: $T_{\text{osc}} = 9.6$ ns. If the participation channel has a physical counterpart (phonon bath mode, collective excitation), this oscillation should be observable in ultrafast spectroscopy.

### 7.2 What Would Falsify the Mapping

- If thermal diffusivity in a well-characterised material is density-independent across all accessible densities, the mobility channel ($\beta > 0$) is falsified as a description of thermal transport in that material.
- If PME spreading ($\alpha_R = 1/8$) is not observed in any system with concentration-dependent diffusivity, the specific ED constitutive form ($m = \beta + 1 = 3$) is falsified.
- If the penalty relaxation time does not match any measured thermal or concentration-relaxation timescale, the penalty mapping is unsupported.

### 7.3 What Would Not Falsify the Mapping

- The participation channel parameters are candidates. The absence of observable telegraph oscillation in a specific material weakens but does not falsify the structural core.
- The specific value $\beta = 2$ is a constitutive choice. If density-dependent diffusivity follows a different power law (e.g., $\beta = 1$ or $\beta = 3$), the mapping framework holds with a different PME exponent.
- Failure in one material does not falsify the framework in other materials. The condensed-matter mapping is material-specific.

---

## 8. Open Questions

1. **Which materials?** The mapping is material-specific. Which condensed-matter systems are most likely to exhibit ED-like behaviour (density-dependent diffusivity with compact-support fronts)? Leading candidates: concentrated colloidal suspensions, polymer melts near the glass transition, granular flows, and dense fermionic systems.

2. **Mobility exponent $\beta$.** The canonical value $\beta = 2$ gives $m = 3$. Is this the correct constitutive choice for a specific material, or should $\beta$ be fitted to experimental data? If the latter, the mapping becomes a one-parameter fit — still far more constrained than a general nonlinear diffusion model, but no longer purely constitutive.

3. **Physical origin of $\rho^*$.** The equilibrium density $\rho^* = 0.5\,R_0$ has a clearer physical meaning in condensed matter than in the quantum or Planck regimes: it could represent the equilibrium concentration of a solution, the average density of a two-phase mixture, or the set point of a thermostatic process. But $\rho^*/R_0 = 0.5$ is a canonical choice; the physical value may differ.

4. **Participation channel identification.** In the quantum regime, $v(t)$ had no clear analogue. In condensed matter, stronger candidates exist: a phonon bath mode, a spatially averaged order parameter, a global thermal feedback. Identifying $v(t)$ with a specific measurable quantity is the most important open problem for this regime.

5. **Horizon formation in experiments.** ED horizons form when $\rho \to \rho_{\max}$. In condensed matter, this corresponds to close-packing or jamming. Colloidal glasses and granular packings exhibit jamming transitions where mobility drops to zero above a critical volume fraction. Whether the ED horizon dynamics (sharp threshold, monotone retreat, transient lifetime) match experimental jamming dynamics is testable.

6. **Code update.** The `condensed_matter_scales()` factory should accept `D_phys` as an optional parameter and pass it to `compute_scales()`, so that material-specific physical anchoring is built into the API.

7. **Temperature dependence.** Both $D_{\text{phys}}$ and $R_0$ depend on temperature. The current mapping is isothermal. Extending to temperature-dependent material properties would require coupling the ED PDE to a thermal equation — a significant extension beyond the current single-field framework.

---

## 9. Other Regimes (Preview)

| Regime | $L_0$ | $R_0$ | $D_{\text{phys}}$ | Anchoring | Note |
|--------|--------|--------|---------------------|-----------|------|
| Quantum | $\hbar/(mc)$ | $L_0^{-d}$ | $\hbar/(2m)$ | Madelung theorem | ED-Dimensional-01 |
| Planck | $\ell_{\text{Pl}}$ | $\rho_{\text{Pl}}$ | $\sqrt{\hbar G/c}$ | Dimensional uniqueness | ED-Dimensional-02 |
| **Condensed matter** (this note) | Experimental ($\sim\mu$m) | Material density | Thermal diffusivity | Laboratory measurement | ED-Dimensional-03 |
| Galactic | 1 kpc | $\rho_{\text{crit}}$ | User-chosen | Astrophysical scales | ED-Dimensional-04 |
| Cosmological | $c/H_0$ | $\rho_{\text{crit}}$ | User-chosen | Hubble scales | ED-Dimensional-05 |

The condensed-matter regime is the third note because it is the first to rely entirely on empirical anchoring — no fundamental-constant theorem, no dimensional uniqueness. This makes it the most directly testable regime and the closest to experimental falsification.

---

## Appendix A: Derivation of $T_0$ for Three Materials

Starting from the general formula $T_0 = L_0^2 D_{\text{nd}}/D_{\text{phys}}$ with $L_0 = 10^{-6}$ m and $D_{\text{nd}} = 0.3$:

**Water:**

$$T_0 = \frac{(10^{-6})^2 \times 0.3}{1.43 \times 10^{-7}} = \frac{3.0 \times 10^{-13}}{1.43 \times 10^{-7}} = 2.098 \times 10^{-6}\;\text{s}.$$

$$V_0 = \frac{10^{-6}}{2.098 \times 10^{-6}} = 0.477\;\text{m/s}.$$

**Silicon:**

$$T_0 = \frac{3.0 \times 10^{-13}}{8.80 \times 10^{-5}} = 3.409 \times 10^{-9}\;\text{s}.$$

$$V_0 = \frac{10^{-6}}{3.409 \times 10^{-9}} = 293.3\;\text{m/s}.$$

**Copper:**

$$T_0 = \frac{3.0 \times 10^{-13}}{1.17 \times 10^{-4}} = 2.564 \times 10^{-9}\;\text{s}.$$

$$V_0 = \frac{10^{-6}}{2.564 \times 10^{-9}} = 390.0\;\text{m/s}.$$

**Verification** ($D_{\text{phys}} \cdot T_0 / L_0^2 = D_{\text{nd}}$):

- Water: $1.43 \times 10^{-7} \times 2.098 \times 10^{-6} / 10^{-12} = 0.300$. Confirmed.
- Silicon: $8.80 \times 10^{-5} \times 3.409 \times 10^{-9} / 10^{-12} = 0.300$. Confirmed.
- Copper: $1.17 \times 10^{-4} \times 2.564 \times 10^{-9} / 10^{-12} = 0.300$. Confirmed.

---

## Appendix B: Comparison Across All Three Regimes ($d = 3$)

| Scale | Quantum (electron) | Planck | Condensed matter (Si) | Ratio: Pl/QM | Ratio: CM/QM |
|:------|:-------------------|:-------|:----------------------|:-------------|:-------------|
| $L_0$ | $3.86 \times 10^{-13}$ m | $1.62 \times 10^{-35}$ m | $1.00 \times 10^{-6}$ m | $4.2 \times 10^{-23}$ | $2.6 \times 10^{6}$ |
| $T_0$ | $7.73 \times 10^{-22}$ s | $1.62 \times 10^{-44}$ s | $3.41 \times 10^{-9}$ s | $2.1 \times 10^{-23}$ | $4.4 \times 10^{12}$ |
| $R_0$ | $1.74 \times 10^{37}$ m$^{-3}$ | $5.16 \times 10^{96}$ kg m$^{-3}$ | $2.33 \times 10^{3}$ kg m$^{-3}$ | — | — |
| $V_0$ | $5.00 \times 10^{8}$ m/s | $9.99 \times 10^{8}$ m/s | $2.93 \times 10^{2}$ m/s | 2.0 | $5.9 \times 10^{-7}$ |
| $D_{\text{phys}}$ | $5.79 \times 10^{-5}$ m$^2$/s | $4.85 \times 10^{-27}$ m$^2$/s | $8.80 \times 10^{-5}$ m$^2$/s | $8.4 \times 10^{-23}$ | 1.5 |

The condensed-matter regime occupies the middle ground in length and time, has subluminal velocity scales, and has diffusivities comparable to the quantum regime. The density scales are not directly comparable because the quantum regime uses probability density (m$^{-d}$) while the condensed-matter and Planck regimes use mass density (kg m$^{-3}$).

---

## References

1. Proxmire, A. "ED-Dimensional-01: Physical Units and Dimensional Mapping — The Quantum Regime." (2026).
2. Proxmire, A. "ED-Dimensional-02: Physical Units and Dimensional Mapping — The Planck Regime." (2026).
3. Proxmire, A. "Event Density as an Ontological Framework: Constitutive Channels, Structural Laws, and Six Empirical Analogues." (2026).
4. Proxmire, A. ED-SIM-02: An Architectural Lab for Entropic Dynamics. Software package (2026).
5. Vazquez, J. L. *The Porous Medium Equation.* Oxford University Press (2007).
6. Carslaw, H. S. and Jaeger, J. C. *Conduction of Heat in Solids.* 2nd ed. Oxford University Press (1959).
7. Haynes, W. M. (ed.) *CRC Handbook of Chemistry and Physics.* 97th ed. CRC Press (2016).
