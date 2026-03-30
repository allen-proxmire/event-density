# ED-Dimensional-05: Physical Units and Dimensional Mapping — The Cosmological Regime

**Allen Proxmire**
**March 2026**

---

**Canonical sources:**

| Source | Content used |
|--------|-------------|
| Critical Assessment (2026-03-27) | The challenge being addressed |
| ED-Dimensional-01 through 04 | Series template, nondimensionalization scheme, status classification |
| ED Foundational Paper | Canonical PDE, structural analogues |
| ED BAO-like Correlation Paper | Telegraph-modulated preferred scale |
| ED-I-008: Cosmological Structure | Expansion, horizon, and structure analogues |
| ED-I-012.0: Cosmology from ED Compositional Rule | Cosmological regime classification |
| `edsim/units/constants.py` | CODATA constants, $H_0$, $\rho_{\text{crit}}$ |
| `edsim/units/scales.py` | `cosmological_scales()` factory |
| Planck Collaboration (2020) | $\Lambda$CDM parameters |

**Scope.** This note addresses the cosmological regime, where the characteristic scales are the Hubble length $c/H_0$, the critical density $\rho_{\text{crit}}$, and a horizon-scale diffusivity $c^2/H_0$. It is the fifth and final note in the ED-Dimensional series, completing the mapping from the Planck scale ($10^{-35}$ m) to the Hubble scale ($10^{26}$ m) — 61 orders of magnitude in length, all governed by a single canonical PDE.

---

## 0. The Challenge

The four preceding notes anchored ED to fundamental constants (quantum, Planck), laboratory measurements (condensed matter), and astrophysical observables (galactic). Each produced a complete dimensional dictionary and a set of falsifiable predictions within its regime.

The cosmological regime is the most ambitious and the most uncertain. At Hubble scales, the ED density field must be interpreted as the large-scale mass-energy density of the universe, the time scale must match the age of the universe, and the structural predictions must be compared against the cosmic microwave background (CMB), the baryon acoustic oscillation (BAO) scale, and the large-scale structure of galaxy distributions.

The ED interpretation series has produced structural analogues of expansion (density decay), horizons (diffusion barriers), and a preferred correlation scale (telegraph-modulated diffusion). The March 2026 Critical Assessment acknowledged these as suggestive but demanded quantitative mapping. This note provides that mapping.

This note does **not** claim that ED is a cosmology. It claims that ED, when anchored to the Hubble length and critical density, produces specific timescales, length scales, and dynamical rates in SI units that can be compared against $\Lambda$CDM predictions and observational data.

---

## 1. The Nondimensionalization Scheme

The general scheme is identical to ED-Dimensional-01, Section 1. The canonical ED PDE in physical units is:

$$\partial_t \rho = D_{\text{phys}}\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr).$$

Three characteristic scales ($L_0$, $T_0$, $R_0$) and two derived scales ($V_0 = L_0/T_0$, $E_0 = R_0 \cdot L_0^d$) define the mapping:

$$\hat{x} = x/L_0, \quad \hat{t} = t/T_0, \quad \hat{\rho} = \rho/R_0, \quad \hat{v} = v/V_0.$$

---

## 2. The Cosmological Regime: Scale Anchoring

### 2.1 Density: $\rho \to$ Cosmological Mass-Energy Density

In the cosmological regime, the ED density field is identified with the total mass-energy density of the universe:

$$\rho(x,t) \;\to\; \text{cosmological density [kg m}^{-3}\text{]}.$$

The density scale is the critical density:

$$R_0 = \rho_{\text{crit}} = \frac{3H_0^2}{8\pi G} = 8.53 \times 10^{-27}\;\text{kg m}^{-3}.$$

This is the density at which the universe is spatially flat. The ED field $\hat{\rho} = \rho/\rho_{\text{crit}}$ is the cosmological density parameter: $\hat{\rho} = 1$ corresponds to $\Omega = 1$ (critical density), $\hat{\rho} < 1$ to an underdense region, $\hat{\rho} > 1$ to an overdense region.

The capacity bound $\rho_{\max} = R_0 = \rho_{\text{crit}}$ means that in the canonical ED framework, the critical density is the maximum. This is a strong structural constraint: ED predicts that cosmological density cannot exceed $\rho_{\text{crit}}$ without triggering mobility collapse. The physical meaning of this constraint is discussed in Section 6.5.

### 2.2 Length: $L_0 = c/H_0$ (Hubble Length)

$$L_0 = \frac{c}{H_0} = 1.373 \times 10^{26}\;\text{m} = 4449\;\text{Mpc} \approx 4.4\;\text{Gpc}.$$

The Hubble length is the distance at which the Hubble recession velocity equals the speed of light. It is the characteristic scale of the observable universe and the natural length unit for cosmological dynamics. In ED, one nondimensional length unit corresponds to one Hubble length.

### 2.3 Diffusivity: $D_{\text{phys}} = c^2/H_0$

The cosmological diffusivity is constructed from the two available scales — $c$ and $H_0$ — as their unique combination with dimensions of m$^2$ s$^{-1}$:

$$D_{\text{phys}} = \frac{c^2}{H_0} = c \cdot L_0 = 4.115 \times 10^{34}\;\text{m}^2\text{ s}^{-1}.$$

This follows the same dimensional logic as the galactic regime ($D = v \cdot L_0$) with $v = c$ — the maximum causal speed at the horizon scale. The physical justification:

1. **Dimensional uniqueness.** From $c$ and $H_0$ alone, $c^2/H_0$ is the only combination with dimensions of diffusivity, just as $\sqrt{\hbar G/c}$ was the unique Planck diffusivity.

2. **Consistency with the galactic regime.** At galactic scales, $D_{\text{phys}} = v_{\text{circ}} \cdot L_0$. At cosmological scales, the characteristic velocity is $c$ (the recession velocity at the Hubble radius), giving $D_{\text{phys}} = c \cdot L_0 = c^2/H_0$.

3. **Horizon-scale transport.** $D_{\text{phys}} = c^2/H_0$ is the diffusivity at which a perturbation spreads across the Hubble volume in one Hubble time. This is the maximum rate of causal transport at the largest scale.

### 2.4 Time Scale

$$T_0 = \frac{L_0^2\,D_{\text{nd}}}{D_{\text{phys}}} = \frac{(c/H_0)^2 \cdot D_{\text{nd}}}{c^2/H_0} = \frac{D_{\text{nd}}}{H_0} = D_{\text{nd}} \cdot t_H.$$

This is the same clean result as the Planck and galactic regimes:

$$\boxed{T_0 = D_{\text{nd}} \cdot t_H = \frac{D_{\text{nd}}}{H_0}.}$$

For $D_{\text{nd}} = 0.3$ and $H_0 = 67.4$ km/s/Mpc:

$$T_0 = 0.3 \times 14.51\;\text{Gyr} = 4.35\;\text{Gyr}.$$

This is a remarkable result. The ED time scale in the cosmological regime is approximately one-third the age of the universe. One nondimensional time unit corresponds to 4.35 billion years — comparable to the elapsed time since the formation of the solar system.

### 2.5 Velocity Scale

$$V_0 = \frac{L_0}{T_0} = \frac{c/H_0}{D_{\text{nd}}/H_0} = \frac{c}{D_{\text{nd}}}.$$

For $D_{\text{nd}} = 0.3$: $V_0 = c/0.3 = 3.333\,c$.

The superluminal $V_0$ is a mathematical consequence of the parabolic PDE, identical to the Planck regime. At cosmological scales, superluminal transport is not unusual — the Hubble flow itself carries distant galaxies away faster than light. However, the ED PDE does not describe metric expansion; it describes density diffusion. The caveat from ED-Dimensional-01 applies: the characteristic velocity is a nondimensionalization factor, not a signal speed.

### 2.6 Energy/Mass Scale

$$E_0 = R_0 \cdot L_0^3 = \rho_{\text{crit}} \cdot \left(\frac{c}{H_0}\right)^3 = 2.206 \times 10^{52}\;\text{kg} = 1.109 \times 10^{22}\;M_\odot.$$

This is the total mass within one Hubble volume at critical density — approximately $10^{22}$ solar masses, consistent with estimates of the mass of the observable universe.

### 2.7 Summary of Cosmological-Regime Scales

| Scale | Formula | Value | Unit | Cosmological meaning |
|:------|:--------|:------|:-----|:---------------------|
| $L_0$ | $c/H_0$ | $1.373 \times 10^{26}$ | m | Hubble length (4.4 Gpc) |
| $T_0$ | $D_{\text{nd}}/H_0$ | $1.374 \times 10^{17}$ | s | 4.35 Gyr (0.3 Hubble times) |
| $R_0$ | $3H_0^2/(8\pi G)$ | $8.53 \times 10^{-27}$ | kg m$^{-3}$ | Critical density |
| $V_0$ | $c/D_{\text{nd}}$ | $9.993 \times 10^{8}$ | m s$^{-1}$ | $3.333\,c$ |
| $D_{\text{phys}}$ | $c^2/H_0$ | $4.115 \times 10^{34}$ | m$^2$ s$^{-1}$ | Horizon-scale diffusivity |
| $E_0\;(d{=}3)$ | $\rho_{\text{crit}}(c/H_0)^3$ | $2.206 \times 10^{52}$ | kg | $1.1 \times 10^{22}\;M_\odot$ |

---

## 3. The ED-to-Cosmological Dictionary

Every canonical ED parameter is mapped to its cosmological-regime physical quantity ($d = 3$, $D_{\text{nd}} = 0.3$, $H_0 = 67.4$ km/s/Mpc).

| ED Parameter | Canonical value | Physical quantity | Formula (SI) | Value | Unit | Status |
|:-------------|:----------------|:------------------|:-------------|:------|:-----|:-------|
| $\rho$ | field in $[0,1]$ | Cosmological density | $\rho_{\text{phys}} = \hat{\rho} \cdot \rho_{\text{crit}}$ | $\hat{\rho} \cdot 8.53 \times 10^{-27}$ | kg m$^{-3}$ | **Anchored** |
| $D$ | 0.3 | Horizon-scale diffusivity | $D_{\text{phys}} = c^2/H_0$ | $4.115 \times 10^{34}$ | m$^2$ s$^{-1}$ | **Constructed** |
| $M(\rho)$ | $M_0(1 - \hat{\rho})^\beta$ | Density-dependent cosmic transport | $M_{\text{phys}} = M_0(1 - \hat{\rho})^\beta \cdot D_{\text{phys}}/D_{\text{nd}}$ | (state-dependent) | m$^2$ s$^{-1}$ | **ED-specific** |
| $P(\rho)$ | $P_0(\hat{\rho} - \hat{\rho}^*)$ | Cosmological restoring force | $P_{\text{phys}} = P_0(\hat{\rho} - \hat{\rho}^*) \cdot R_0/T_0$ | (state-dependent) | kg m$^{-3}$ s$^{-1}$ | **Anchored** |
| $v(t)$ | scalar | Global cosmological mode | $v_{\text{phys}} = \hat{v} \cdot V_0$ | $\hat{v} \cdot 3.333\,c$ | m s$^{-1}$ | **Candidate** |
| $H$ | 0–50 | Cosmological feedback coupling | $H_{\text{phys}} = H_{\text{nd}} \cdot V_0$ | $H_{\text{nd}} \cdot 9.993 \times 10^{8}$ | m s$^{-1}$ | **Candidate** |
| $\tau$ | 1.0 | Participation timescale | $\tau_{\text{phys}} = T_0$ | 4.35 Gyr | s | **Candidate** |
| $\zeta$ | 0.1 | Cosmological damping rate | $\zeta_{\text{phys}} = \zeta_{\text{nd}}/T_0$ | $7.280 \times 10^{-19}$ | s$^{-1}$ | **Candidate** |
| $\rho^*$ | 0.5 | Equilibrium density | $\rho^*_{\text{phys}} = 0.5 \cdot \rho_{\text{crit}}$ | $4.27 \times 10^{-27}$ | kg m$^{-3}$ | **Anchored** |
| $\rho_{\max}$ | 1.0 | Critical density (capacity) | $\rho_{\max,\text{phys}} = \rho_{\text{crit}}$ | $8.53 \times 10^{-27}$ | kg m$^{-3}$ | **Anchored** |
| $M_0$ | 1.0 | Mobility prefactor | $M_{0,\text{phys}} = D_{\text{phys}}/D_{\text{nd}}$ | $1.372 \times 10^{35}$ | m$^2$ s$^{-1}$ | **Anchored** |
| $\beta$ | 2.0 | Mobility exponent (PME $m = 3$) | dimensionless | 2.0 | — | **Structural** |
| $P_0$ | 0.01–1.0 | Penalty slope | $P_{0,\text{phys}} = P_0/T_0$ | $P_0 \cdot 7.28 \times 10^{-18}$ | s$^{-1}$ | **Anchored** |

**Status key** (consistent with the full series):

- **Anchored**: uniquely determined by the cosmological observables ($H_0$, $c$, $G$).
- **Constructed**: built from observables by dimensional analysis ($D_{\text{phys}} = c^2/H_0$).
- **ED-specific**: a prediction of the ED framework with no standard $\Lambda$CDM counterpart.
- **Candidate**: physically motivated but not uniquely determined.
- **Structural**: dimensionless, unchanged by nondimensionalization.

---

## 4. The PDE in SI Units

Restoring all dimensional factors, the ED PDE in the cosmological regime reads:

$$\partial_t \rho = \frac{c^2}{H_0}\bigl[M(\rho/\rho_{\text{crit}})\,\nabla^2\rho + M'(\rho/\rho_{\text{crit}})\,|\nabla\rho|^2/\rho_{\text{crit}} - P_0(\rho - \rho^*)/T_0\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr),$$

where $T_0 = D_{\text{nd}}/H_0$, $M(\hat{\rho}) = (1 - \hat{\rho})^\beta$, and all spatial derivatives are in physical (comoving) coordinates.

The key observation: only $c$, $H_0$, and $G$ (via $\rho_{\text{crit}}$) appear. The cosmological PDE is written entirely in terms of the same three constants that define the Friedmann equations, but arranged in a different mathematical structure — a quasilinear parabolic PDE rather than an ODE for the scale factor.

---

## 5. Conversion Factor Table

Compact reference for converting ED-SIM-02 simulation output to SI units ($d = 3$, $D_{\text{nd}} = 0.3$, $\Lambda$CDM parameters):

| Quantity | ND $\to$ SI | Numerical factor | Cosmological unit |
|:---------|:-----------|:-----------------|:------------------|
| Length $x$ | $x_{\text{SI}} = \hat{x} \cdot L_0$ | $L_0 = 1.373 \times 10^{26}$ m | 4449 Mpc |
| Time $t$ | $t_{\text{SI}} = \hat{t} \cdot T_0$ | $T_0 = 1.374 \times 10^{17}$ s | 4.35 Gyr |
| Density $\rho$ | $\rho_{\text{SI}} = \hat{\rho} \cdot R_0$ | $R_0 = 8.53 \times 10^{-27}$ kg m$^{-3}$ | $\rho_{\text{crit}}$ |
| Velocity $v$ | $v_{\text{SI}} = \hat{v} \cdot V_0$ | $V_0 = 9.993 \times 10^{8}$ m s$^{-1}$ | $3.333\,c$ |
| Diffusivity $D$ | $D_{\text{SI}} = D_{\text{nd}} \cdot L_0^2/T_0$ | $D_0 = 1.372 \times 10^{35}$ m$^2$ s$^{-1}$ | $c^2/(D_{\text{nd}} H_0)$ |
| Mass $(d{=}3)$ | $m_{\text{SI}} = \hat{m} \cdot E_0$ | $E_0 = 2.206 \times 10^{52}$ kg | $1.1 \times 10^{22}\;M_\odot$ |

**Notable conversions:**

| Nondimensional quantity | Physical value | Significance |
|:------------------------|:---------------|:-------------|
| $\hat{t} = 1$ | 4.35 Gyr | One ED time unit = age of solar system |
| $\hat{t} = 3.17$ | 13.8 Gyr | Age of the universe |
| $\hat{x} = 0.034$ | 150 Mpc | BAO scale |
| $\hat{x} = 3.2$ | 14.3 Gpc | Comoving radius of observable universe |

**Code example** (using the existing `edsim.units` API):

```python
from edsim.core.parameters import EDParameters
from edsim.units.scales import compute_scales
from edsim.units import constants as C

params = EDParameters(d=3, L=(1.0, 1.0, 1.0), N=(64, 64, 64))
L_H = C.c / C.H_0
D_phys = C.c**2 / C.H_0

sc = compute_scales(params, L0=L_H, R0=C.rho_crit, D_phys=D_phys,
                    regime="cosmological")
print(f"L0 = {sc.L0:.4e} m  (Hubble length)")
print(f"T0 = {sc.T0:.4e} s  ({sc.T0 / 3.1557e16:.2f} Gyr)")
print(f"R0 = {sc.R0:.4e} kg/m^3  (rho_crit)")
```

---

## 6. What Is Exact, What Is Candidate

### 6.1 Structural Identities (Regime-Independent)

The four structural identities hold at cosmological scales:

1. **PME reduction.** The mobility channel with $P_0 = 0$, $H = 0$ reduces to the porous-medium equation with $m = 3$. The Barenblatt exponent: $\alpha_R = 1/8$ ($d = 3$). A cosmic density perturbation should spread as $R(t) \propto t^{1/8}$ with compact support — qualitatively different from the Gaussian profiles assumed in standard cosmological perturbation theory.

2. **RC decay.** The penalty channel gives $\tau_{\text{RC}} = T_0/(D_{\text{nd}} P_0) = t_H/P_0$. For $P_0 = 1.0$:

$$\boxed{\tau_{\text{RC}} = t_H = 14.51\;\text{Gyr}.}$$

**The ED penalty relaxation time equals one Hubble time.** This is the single most striking numerical coincidence in the entire ED-Dimensional series. The time for a cosmological density perturbation to decay by a factor of $e$ is exactly the age of the universe (within the $\Lambda$CDM determination of $H_0$). This is not designed in: it follows from $\tau_{\text{RC}} = 1/(D_{\text{nd}} P_0) \cdot T_0 = (D_{\text{nd}} t_H)/(D_{\text{nd}} P_0) = t_H/P_0$, and $P_0 = 1$ is the canonical value.

3. **Telegraph oscillation.** For $H = 5$: $T_{\text{osc}} = 2.81 \cdot T_0 = 12.2$ Gyr. The participation variable oscillates with a period comparable to the age of the universe. This is the timescale of the BAO-like preferred scale identified in the ED BAO paper.

4. **Compact support.** Cosmic density perturbations in the PME regime have a finite extent — a sharp boundary beyond which no transport has occurred. In standard cosmology, perturbations are assumed to have Gaussian profiles extending to infinity. The compact-support prediction is structurally distinct.

### 6.2 Constructed Correspondences

- **$D_{\text{phys}} = c^2/H_0$**: the unique diffusivity from $c$ and $H_0$. This is the strongest possible construction — dimensional uniqueness from observable constants — but it is not derived from a dynamical equation.
- **$L_0 = c/H_0$**: the Hubble length, directly observable (from Type Ia supernovae, BAO, CMB).
- **$R_0 = \rho_{\text{crit}}$**: derived from $H_0$ and $G$ via the Friedmann equation. Known to $\sim 2\%$.

### 6.3 Candidate Correspondences

The participation channel has the strongest physical motivation at cosmological scales:

- **$v(t)$ as a dark-energy mode.** The most natural cosmological interpretation of a global variable that drives uniform density change is dark energy or a cosmological-constant equivalent. The participation variable adds a spatially uniform term $+Hv$ to the PDE — structurally analogous to $\Lambda$ adding a uniform acceleration to the Friedmann equation. This is the most physically motivated candidate identification in any regime.
- **$\tau_{\text{phys}} = 4.35$ Gyr.** If $v(t)$ represents a dark-energy mode, $\tau$ is the response time of dark energy to changes in the average density. The value 4.35 Gyr is comparable to the transition epoch ($z \sim 0.7$) at which dark energy began dominating over matter — a suggestive but unconfirmed correspondence.
- **$H_{\text{nd}}$ as the dark-energy coupling.** The strength of the participation feedback determines how strongly the global mode influences local density evolution. In $\Lambda$CDM, this role is played by $\Omega_\Lambda$.

### 6.4 The $\tau_{\text{RC}} = t_H$ Coincidence

The result $\tau_{\text{RC}} = t_H$ for $P_0 = 1$ deserves careful discussion.

**What it means.** The ED penalty channel, at canonical parameters, predicts that cosmological density perturbations decay with a time constant equal to the Hubble time. This is numerically consistent with the observed fact that the universe has had approximately one Hubble time to evolve from its initial density perturbations to the present large-scale structure.

**What it does not mean.** This is not a derivation of the age of the universe. The Hubble time enters as an input ($L_0 = c/H_0$), not as an output. The nontrivial content is that the penalty relaxation time — determined by $D_{\text{nd}}$ and $P_0$ — happens to equal $t_H$ when $P_0 = 1$ and $D_{\text{nd}} = 0.3$. If $P_0 \neq 1$, the coincidence breaks.

**Honest assessment.** This is either a meaningful structural resonance (the ED architecture naturally produces cosmological-timescale relaxation) or a numerical coincidence (the canonical parameters were not chosen with cosmology in mind, but the algebra works out). Distinguishing between these possibilities requires independent evidence.

### 6.5 The Mobility at Cosmological Scales

The density-dependent mobility $M(\rho) = M_0(1 - \hat{\rho})^\beta$ with $\rho_{\max} = \rho_{\text{crit}}$ predicts:

**Density-dependent cosmic transport.** As the local density approaches the critical density, large-scale transport slows and eventually halts. Regions at $\rho \approx \rho_{\text{crit}}$ become ED horizons — zones where density redistribution is suppressed.

This has a striking cosmological interpretation:

| Feature | $\Lambda$CDM | ED prediction |
|---------|-------------|---------------|
| Overdense regions | Gravitational collapse, virialisation | Mobility decreases, transport slows |
| Critical density | Flat spatial geometry | Mobility vanishes (horizon) |
| Voids | Underdense, expanding faster | High mobility, rapid transport |
| Structure growth | Gravitational instability | Nonlinear mobility creates sharp boundaries |

The ED picture inverts the standard narrative: instead of gravity pulling overdense regions together, ED's mobility suppression *freezes* overdense regions by halting transport. The result — sharp boundaries between dense and underdense regions — is qualitatively consistent with the observed cosmic web (filaments, walls, voids), but the mechanism is different.

**Critical caveat.** In standard cosmology, density perturbations grow (gravitational instability). In ED, all perturbations decay (monostable penalty). This is the fundamental structural difference. ED cannot produce growing structure from the penalty channel alone. The participation channel ($+Hv$) can temporarily enhance density, but the monostable attractor guarantees eventual decay. Whether the transient enhancement is sufficient to match observed structure formation timescales is an open question.

---

## 7. Falsifiable Predictions

### 7.1 Predictions That Follow From the Mapping

1. **Cosmological timescale.** $T_0 = 4.35$ Gyr. One nondimensional ED time unit corresponds to the elapsed time since the formation of the solar system. The age of the universe is $\hat{t}_{\text{age}} = 13.8/4.35 = 3.17$ nondimensional units.

2. **Penalty relaxation = Hubble time.** For $P_0 = 1$: $\tau_{\text{RC}} = t_H = 14.5$ Gyr. Cosmological density perturbations should decay with an $e$-folding time equal to the Hubble time. This is testable: the observed rate of structure dissolution (void expansion, cluster dispersal) should be consistent with $\tau_{\text{RC}} \sim t_H$.

3. **Telegraph oscillation period.** For $H = 5$: $T_{\text{osc}} = 12.2$ Gyr. If the participation channel is physical, the universe should exhibit a quasi-periodic global fluctuation with period comparable to its age. Possible observational signatures: oscillatory features in the cosmic star-formation rate history, or periodic modulation of the dark-energy equation of state.

4. **PME spreading exponent.** Density perturbations spreading under the mobility channel should follow $R(t) \propto t^{1/8}$, not the Gaussian $t^{1/2}$. The perturbation front should be sharp. This is testable against the observed sharpness of void boundaries in galaxy surveys (SDSS, DESI).

5. **BAO-like preferred scale.** The ED BAO paper showed that telegraph-modulated diffusion produces a preferred correlation scale. In physical units, this scale is set by the ratio of the diffusion length to the telegraph frequency: $r_{\text{BAO}} \sim 2 D_{\text{eff}} / \omega$. The observed BAO scale ($\sim 150$ Mpc $= 0.034\,L_0$ in nondimensional units) provides a quantitative target.

6. **Horizon formation at critical density.** ED predicts mobility collapse at $\rho = \rho_{\text{crit}}$. Regions at or above critical density should exhibit suppressed transport — structurally analogous to the formation of gravitationally bound structures. The prediction is that the transition from mobile (void) to frozen (cluster) should be sharp, not gradual.

### 7.2 What Would Falsify the Mapping

- If the penalty relaxation time is grossly inconsistent with the Hubble time (i.e., if the observed rate of structure evolution is much faster or slower than $t_H$), the penalty anchoring is falsified.
- If cosmic density perturbations grow rather than decay, the monostable penalty is structurally incompatible with cosmological structure formation. (This is the most serious potential falsification — see Section 8.)
- If the BAO-like scale produced by ED simulations does not match the observed 150 Mpc, the telegraph-modulation mechanism is quantitatively falsified.
- If void boundaries are diffuse rather than sharp, the compact-support (PME) prediction is weakened.

### 7.3 What Would Not Falsify the Mapping

- The participation channel is a candidate. Absence of observable dark-energy oscillation does not falsify the structural core.
- The canonical $D_{\text{nd}} = 0.3$ and $P_0 = 1.0$ are constitutive choices. Different values may be appropriate for cosmology.
- The parabolic character of the PDE (infinite propagation speed) is a known limitation shared with all diffusion-based cosmological models.

---

## 8. Open Questions

1. **Structure growth vs. structure decay.** The most fundamental tension between ED and standard cosmology: gravitational instability produces growing perturbations; the ED monostable penalty produces decaying perturbations. Can the participation channel ($+Hv$) produce sufficient transient growth to account for the observed cosmic web? This is the central open question for cosmological ED. If the answer is no, the ED PDE in its current form cannot describe cosmological structure formation.

2. **Metric expansion vs. density decay.** ED interprets cosmic expansion as density decay toward $\rho^*$, not as metric expansion of space. These are structurally different: metric expansion stretches wavelengths (redshift), separates test particles (Hubble flow), and dilutes radiation ($\rho_{\text{rad}} \propto a^{-4}$). Does ED density decay produce equivalent observational signatures? This has not been demonstrated.

3. **Dark energy as participation.** The identification $v(t) \leftrightarrow$ dark energy is the most physically motivated candidate in any regime. If correct, it predicts that the dark-energy equation of state $w(z)$ should show oscillatory behaviour with period $\sim T_{\text{osc}} \sim 12$ Gyr. Current constraints on $w(z)$ from Type Ia supernovae and BAO are consistent with $w = -1$ (no oscillation), but the uncertainties are large at high redshift. Future surveys (DESI, Euclid, Rubin) will tighten these constraints.

4. **The $\rho_{\max} = \rho_{\text{crit}}$ constraint.** In the canonical mapping, $\rho_{\max} = \rho_{\text{crit}}$, meaning the critical density is the maximum permissible density. But the central densities of galaxies, clusters, and stars vastly exceed $\rho_{\text{crit}}$. This implies either: (a) the cosmological ED describes only the large-scale average density field, not individual collapsed objects, or (b) a different $R_0$ (much higher) should be used for sub-Hubble scales. The former interpretation is standard in cosmological perturbation theory; the latter connects to the galactic regime (ED-Dimensional-04).

5. **CMB power spectrum.** The strongest quantitative test of any cosmological model is the CMB angular power spectrum. Can an ED simulation, run from appropriate initial conditions with the cosmological dictionary, reproduce the observed CMB peaks? This has not been attempted. It would require: (a) an expanding-domain formulation of the ED PDE, (b) a prescription for initial conditions (analogue of inflation-generated perturbations), and (c) a photon-decoupling analogue. This is major future work.

6. **Friedmann correspondence.** The Friedmann equations describe the evolution of a spatially homogeneous density. For ED, the spatially homogeneous limit ($\nabla\rho = 0$) gives $\dot{\rho} = -D P_0 (\rho - \rho^*) + Hv$. This is a damped oscillation around $\rho^*$, not the Friedmann deceleration/acceleration. Whether the ED homogeneous solution can be mapped onto the Friedmann scale factor $a(t)$ is an open algebraic question.

7. **Code updates.** The `cosmological_scales()` factory in `scales.py` should accept `D_phys = c**2/H_0` to enable physically anchored cosmological simulations.

---

## 9. Cross-Regime Summary: The Complete ED-Dimensional Series

### 9.1 The Five Regimes

| # | Regime | $L_0$ | $R_0$ | $D_{\text{phys}}$ | $T_0$ | Anchoring type |
|---|--------|--------|--------|---------------------|--------|---------------|
| 01 | Quantum | $\hbar/(mc)$ | $L_0^{-d}$ | $\hbar/(2m)$ | $2D_{\text{nd}}\hbar/(mc^2)$ | Theorem |
| 02 | Planck | $\ell_{\text{Pl}}$ | $\rho_{\text{Pl}}$ | $\sqrt{\hbar G/c}$ | $D_{\text{nd}} \cdot t_{\text{Pl}}$ | Dimensional uniqueness |
| 03 | Condensed matter | Experimental | Material density | $\kappa/(\rho c_p)$ | $L_0^2 D_{\text{nd}}/D_{\text{phys}}$ | Laboratory measurement |
| 04 | Galactic | 1 kpc | $\rho_{\text{crit}}$ or halo | $v_{\text{circ}} \cdot L_0$ | $D_{\text{nd}} \cdot t_{\text{cross}}$ | Dynamical construction |
| 05 | Cosmological | $c/H_0$ | $\rho_{\text{crit}}$ | $c^2/H_0$ | $D_{\text{nd}} \cdot t_H$ | Dimensional construction |

### 9.2 Scales Across 61 Orders of Magnitude

| Scale | Quantum (e$^-$) | Planck | Condensed (Si) | Galactic (MW) | Cosmological |
|:------|:-----------------|:-------|:----------------|:--------------|:-------------|
| $L_0$ (m) | $3.86 \times 10^{-13}$ | $1.62 \times 10^{-35}$ | $1.00 \times 10^{-6}$ | $3.09 \times 10^{19}$ | $1.37 \times 10^{26}$ |
| $T_0$ (s) | $7.73 \times 10^{-22}$ | $1.62 \times 10^{-44}$ | $3.41 \times 10^{-9}$ | $4.21 \times 10^{13}$ | $1.37 \times 10^{17}$ |
| $D_{\text{phys}}$ (m$^2$/s) | $5.79 \times 10^{-5}$ | $4.85 \times 10^{-27}$ | $8.80 \times 10^{-5}$ | $6.79 \times 10^{24}$ | $4.12 \times 10^{34}$ |
| $V_0/c$ | 1.667 | 3.333 | $9.8 \times 10^{-7}$ | $2.4 \times 10^{-3}$ | 3.333 |
| $V_0$ subluminal? | No | No | **Yes** | **Yes** | No |

### 9.3 Anchoring Hierarchy

The five regimes are ordered by the strength of their anchoring:

1. **Quantum** (strongest): $D_{\text{phys}} = \hbar/(2m)$ is fixed by a mathematical theorem (Madelung). No freedom.
2. **Planck**: all scales fixed by dimensional uniqueness from $\hbar$, $G$, $c$. No freedom, but no dynamical theorem.
3. **Condensed matter**: all scales fixed by laboratory measurement. No freedom, but material-specific.
4. **Galactic**: $D_{\text{phys}} = v_{\text{circ}} \cdot L_0$ constructed from observables. One dimensional argument.
5. **Cosmological** (weakest, but most constrained by scope): $D_{\text{phys}} = c^2/H_0$ constructed from $c$ and $H_0$. Dimensional uniqueness, but no independent measurement of cosmological diffusivity.

### 9.4 The Recurring Pattern: $T_0 = D_{\text{nd}} \cdot t_{\text{natural}}$

Across three regimes, the same clean result appears:

| Regime | Natural time | $T_0$ |
|--------|-------------|-------|
| Planck | $t_{\text{Pl}}$ | $D_{\text{nd}} \cdot t_{\text{Pl}}$ |
| Galactic | $t_{\text{cross}} = L_0/v_{\text{circ}}$ | $D_{\text{nd}} \cdot t_{\text{cross}}$ |
| Cosmological | $t_H = 1/H_0$ | $D_{\text{nd}} \cdot t_H$ |

In each case, the ED time scale is the natural dynamical timescale of the regime multiplied by $D_{\text{nd}}$. This is a structural consequence of the anchoring $D_{\text{phys}} = v \cdot L_0$ (where $v$ is the characteristic velocity of the regime), and it holds whenever this form is used.

### 9.5 What the Series Has Established

The ED-Dimensional series demonstrates that the canonical ED PDE admits a consistent dimensional mapping at every physical scale from $10^{-35}$ m (Planck) to $10^{26}$ m (Hubble). At each scale:

- Every ED parameter maps to a specific physical quantity in SI units.
- The mapping is classified as exact, anchored, constructed, or candidate.
- Falsifiable predictions are identified.
- Open questions are stated.

The series does **not** demonstrate that ED governs the physics at any of these scales. It demonstrates that the dimensional framework is consistent, the predictions are specific, and the programme is falsifiable. Whether the predictions match observations is the work of the next phase of the ED programme.

---

## Appendix A: Derivation of Cosmological-Regime Scales

Starting from $L_0 = c/H_0$, $R_0 = \rho_{\text{crit}} = 3H_0^2/(8\pi G)$, and $D_{\text{phys}} = c^2/H_0$:

**Time scale:**

$$T_0 = \frac{L_0^2 D_{\text{nd}}}{D_{\text{phys}}} = \frac{(c/H_0)^2 \cdot D_{\text{nd}}}{c^2/H_0} = \frac{c^2 D_{\text{nd}}}{H_0^2} \cdot \frac{H_0}{c^2} = \frac{D_{\text{nd}}}{H_0} = D_{\text{nd}} \cdot t_H.$$

**Velocity scale:**

$$V_0 = \frac{L_0}{T_0} = \frac{c/H_0}{D_{\text{nd}}/H_0} = \frac{c}{D_{\text{nd}}}.$$

**Verification:**

$$\frac{D_{\text{phys}} \cdot T_0}{L_0^2} = \frac{(c^2/H_0)(D_{\text{nd}}/H_0)}{(c/H_0)^2} = \frac{c^2 D_{\text{nd}}}{H_0^2} \cdot \frac{H_0^2}{c^2} = D_{\text{nd}}. \quad \checkmark$$

**Mass scale ($d = 3$):**

$$E_0 = \rho_{\text{crit}} \cdot L_0^3 = \frac{3H_0^2}{8\pi G} \cdot \frac{c^3}{H_0^3} = \frac{3c^3}{8\pi G H_0} = \frac{3}{8\pi} \cdot \frac{c^3}{GH_0}.$$

Numerically: $E_0 = 2.206 \times 10^{52}$ kg. This is the total mass within the Hubble sphere at critical density — the mass of the observable universe.

---

## Appendix B: $\Lambda$CDM Parameters and ED Correspondences

| $\Lambda$CDM parameter | Value (Planck 2020) | ED nondimensional analogue | ED interpretation |
|:-----------------------|:--------------------|:--------------------------|:-----------------|
| $H_0$ | 67.4 km/s/Mpc | Sets $L_0$, $T_0$, $D_{\text{phys}}$ | Determines all scales |
| $\Omega_m$ | 0.315 | $\hat{\rho}_m \approx 0.315$ | Matter density fraction |
| $\Omega_\Lambda$ | 0.685 | Candidate: $H_{\text{nd}} \hat{v}$ | Participation-driven density |
| $\Omega_b$ | 0.049 | Sub-component of $\hat{\rho}$ | Baryonic fraction |
| $\sigma_8$ | 0.811 | Amplitude of $\hat{\rho}$ fluctuations at $\hat{x} = 8/L_0$ | Structure normalisation |
| $n_s$ | 0.965 | Spectral index of initial $\hat{\rho}$ perturbations | Initial-condition parameter |
| $\tau_{\text{reion}}$ | 0.054 | No direct analogue | — |
| Age of universe | 13.8 Gyr | $\hat{t} = 3.17$ | 3.17 nondimensional time units |

The $\Lambda$CDM model has 6 free parameters. The ED cosmological mapping has 3 inputs ($H_0$, $c$, $G$) plus the canonical nondimensional parameters ($D_{\text{nd}}$, $P_0$, $\beta$, $H_{\text{nd}}$, $\tau_{\text{nd}}$, $\zeta_{\text{nd}}$). The two frameworks have comparable parametric freedom but different mathematical structures.

---

## References

1. Proxmire, A. "ED-Dimensional-01 through 04." ED-Dimensional series (2026).
2. Proxmire, A. "Event Density as an Ontological Framework." Foundational Paper (2026).
3. Proxmire, A. "Event Density as an Ontology: A BAO-like Correlation Feature from a Minimal PDE." (2026).
4. Proxmire, A. "ED-I-008: Event Density and Cosmological Structure." (2025).
5. Proxmire, A. "ED-I-012.0: Cosmology from the ED Compositional Rule." (2026).
6. Planck Collaboration. "Planck 2018 results. VI. Cosmological parameters." *Astron. Astrophys.* **641**, A6 (2020).
7. Eisenstein, D. J. et al. "Detection of the Baryon Acoustic Peak." *Astrophys. J.* **633**, 560–574 (2005).
8. Perlmutter, S. et al. "Measurements of $\Omega$ and $\Lambda$ from 42 High-Redshift Supernovae." *Astrophys. J.* **517**, 565–586 (1999).
9. Vazquez, J. L. *The Porous Medium Equation.* Oxford University Press (2007).
