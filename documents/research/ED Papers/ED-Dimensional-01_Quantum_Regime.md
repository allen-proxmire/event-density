# ED-Dimensional-01: Physical Units and Dimensional Mapping — The Quantum Regime

**Allen Proxmire**
**March 2026**

---

**Canonical sources:**

| Source | Content used |
|--------|-------------|
| Critical Assessment (2026-03-27) | The challenge being addressed |
| ED Foundational Paper | Canonical PDE, Appendix A parameters, Appendix D PME derivation |
| `edsim/units/constants.py` | CODATA 2018 physical constants |
| `edsim/units/scales.py` | `Scales` dataclass, `compute_scales()`, `quantum_scales()` |
| `edsim/units/mapping.py` | Conversion functions |
| `docs/units.md` | Nondimensionalization scheme |
| Madelung (1927), Nelson (1966) | Schrödinger–diffusion correspondence |

**Scope.** This note addresses the quantum regime only, where $D_{\text{phys}} = \hbar/2m$ is determined by a mathematical theorem (the Madelung transformation). Other regimes — Planck, condensed matter, galactic, cosmological — require separate scale anchoring and will be treated in ED-Dimensional-02 through 05.

---

## 0. The Challenge

The March 2026 Critical Assessment identified the most significant gap in the ED programme:

> *"The canonical PDE operates with dimensionless parameters. Nowhere in the reviewed materials is there a clear, falsifiable mapping from these parameters to physical constants ($\hbar$, $G$, $c$, $k_B$). Without this mapping, the framework cannot make quantitative predictions in physical units. This is not a minor gap — it is the difference between a mathematical model and a physical theory."*

This note responds directly to that challenge. It presents a complete, explicit mapping from every ED parameter to a physical quantity in the quantum regime, anchored to three fundamental constants: $\hbar$, $m$ (particle mass), and $c$. It classifies each mapping as **exact** (mathematical identity), **anchored** (uniquely determined by the scale choice), or **candidate** (interpretive). It identifies falsifiable predictions that follow from the mapping and states what remains open.

This note does **not** claim that ED is quantum mechanics. It claims that ED admits a structurally consistent mapping to quantum-mechanical quantities in one specific regime, and that this mapping produces falsifiable predictions.

---

## 1. The Nondimensionalization Scheme

### 1.1 The Physical-Units PDE

The canonical ED PDE in physical (SI) units is:

$$\partial_t \rho = D_{\text{phys}}\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr),$$

where $\rho$ has dimensions of density, $x$ has dimensions of length, and $t$ has dimensions of time.

### 1.2 Three Characteristic Scales

| Scale | Symbol | Role | Unit |
|-------|--------|------|------|
| Length | $L_0$ | Physical domain/wavelength scale | m |
| Time | $T_0$ | Diffusion time: $L_0^2 D_{\text{nd}} / D_{\text{phys}}$ | s |
| Density | $R_0$ | Physical density scale | regime-dependent |

Two derived scales follow:

| Scale | Symbol | Definition | Unit |
|-------|--------|------------|------|
| Velocity | $V_0$ | $L_0 / T_0$ | m s$^{-1}$ |
| Energy/mass | $E_0$ | $R_0 \cdot L_0^d$ | regime-dependent |

### 1.3 Nondimensional Variables

$$\hat{x} = x/L_0, \quad \hat{t} = t/T_0, \quad \hat{\rho} = \rho/R_0, \quad \hat{v} = v/V_0.$$

After substitution, the PDE becomes:

$$\partial_{\hat{t}}\hat{\rho} = \hat{D}\bigl[\hat{M}(\hat{\rho})\,\hat{\nabla}^2\hat{\rho} + \hat{M}'(\hat{\rho})\,|\hat{\nabla}\hat{\rho}|^2 - \hat{P}(\hat{\rho})\bigr] + \hat{H}\,\hat{v},$$

where $\hat{D} = D_{\text{phys}} T_0 / L_0^2 = D_{\text{nd}}$ by construction of $T_0$.

The solver operates entirely in nondimensional variables. All physical conversions happen at the boundary.

---

## 2. The Quantum Regime: Scale Anchoring

### 2.1 Density: $\rho \to |\psi|^2$

In the quantum regime, the ED density field is identified with the Born probability density:

$$\rho(x,t) \;\to\; |\psi(x,t)|^2.$$

The dimensions are $[\rho] = \text{m}^{-d}$ (probability per unit $d$-volume), not kg m$^{-3}$. The density scale is:

$$R_0 = L_0^{-d},$$

so that the integral of $\hat{\rho}$ over one $L_0^d$ volume equals 1. This matches the implementation in `edsim/units/scales.py` line 164.

### 2.2 Length: $L_0 = \hbar/(mc)$

The natural length scale for a quantum particle of mass $m$ is the reduced Compton wavelength:

$$L_0 = \frac{\hbar}{mc}.$$

This is the scale below which pair creation becomes relevant and the single-particle density picture breaks down. It is the smallest length at which a single-particle probability density is physically meaningful.

### 2.3 Diffusivity: $D_{\text{phys}} = \hbar/(2m)$

The Madelung transformation (1927) rewrites the Schrödinger equation as a pair of fluid equations. The continuity equation for $|\psi|^2$ takes the form of a diffusion equation with:

$$D_{\text{phys}} = \frac{\hbar}{2m}.$$

This is not an analogy. It is a mathematical theorem: the free-particle Schrödinger equation, written in terms of the probability density and phase, contains a diffusive term with exactly this coefficient. The ED mobility channel, when $M(\rho) \equiv 1$ (constant mobility), reproduces this diffusion.

### 2.4 Time Scale

The time scale $T_0$ is determined by $L_0$, $D_{\text{phys}}$, and the nondimensional diffusion weight $D_{\text{nd}}$:

$$T_0 = \frac{L_0^2\,D_{\text{nd}}}{D_{\text{phys}}} = \frac{[\hbar/(mc)]^2 \cdot D_{\text{nd}}}{\hbar/(2m)} = \frac{2\,D_{\text{nd}}\,\hbar}{mc^2}.$$

For the canonical $D_{\text{nd}} = 0.3$:

$$T_0 = \frac{0.6\,\hbar}{mc^2}.$$

This is 0.6 times the Compton time $\hbar/(mc^2)$ — a natural quantum timescale.

### 2.5 Velocity Scale and the Superluminal Caveat

$$V_0 = \frac{L_0}{T_0} = \frac{c}{2\,D_{\text{nd}}}.$$

For $D_{\text{nd}} = 0.3$: $V_0 = c/0.6 \approx 5.00 \times 10^8$ m/s, which exceeds $c$ by a factor of 1.667.

This is **not** a physical velocity. It is a mathematical consequence of the nondimensionalization of a parabolic PDE. The ED equation, like the Schrödinger equation itself, is parabolic and has infinite propagation speed. Neither respects a causal light cone. A relativistic extension (hyperbolic ED, cf. ED-Phys-13/14) would be required for causal propagation. The superluminal $V_0$ is a regime-boundary marker, not a physical prediction.

### 2.6 Numerical Values

**Electron** ($m = 9.109 \times 10^{-31}$ kg):

| Scale | Formula | $d = 1$ | $d = 2$ | $d = 3$ | Unit |
|-------|---------|---------|---------|---------|------|
| $L_0$ | $\hbar/(m_e c)$ | $3.862 \times 10^{-13}$ | $3.862 \times 10^{-13}$ | $3.862 \times 10^{-13}$ | m |
| $T_0$ | $2 D_{\text{nd}} \hbar/(m_e c^2)$ | $7.729 \times 10^{-22}$ | $7.729 \times 10^{-22}$ | $7.729 \times 10^{-22}$ | s |
| $R_0$ | $L_0^{-d}$ | $2.590 \times 10^{12}$ | $6.706 \times 10^{24}$ | $1.737 \times 10^{37}$ | m$^{-d}$ |
| $V_0$ | $c/(2 D_{\text{nd}})$ | $4.997 \times 10^{8}$ | $4.997 \times 10^{8}$ | $4.997 \times 10^{8}$ | m s$^{-1}$ |
| $D_{\text{phys}}$ | $\hbar/(2 m_e)$ | $5.788 \times 10^{-5}$ | $5.788 \times 10^{-5}$ | $5.788 \times 10^{-5}$ | m$^2$ s$^{-1}$ |
| $E_0$ | $R_0 \cdot L_0^d$ | 1.000 | 1.000 | 1.000 | (dimensionless) |

**Proton** ($m = 1.673 \times 10^{-27}$ kg):

| Scale | $d = 2$ value | Unit |
|-------|--------------|------|
| $L_0$ | $2.103 \times 10^{-16}$ | m |
| $T_0$ | $4.209 \times 10^{-25}$ | s |
| $R_0$ | $2.261 \times 10^{31}$ | m$^{-2}$ |
| $D_{\text{phys}}$ | $3.153 \times 10^{-8}$ | m$^2$ s$^{-1}$ |

Note: $V_0 = c/(2 D_{\text{nd}})$ is mass-independent. The Planck mass ($m_{\text{Pl}} = 2.176 \times 10^{-8}$ kg) recovers $L_0 = l_{\text{Pl}}$ and $T_0 \approx 3.23 \times 10^{-44}$ s — the Planck regime emerges as a special case.

---

## 3. The ED-to-Quantum Dictionary

This is the central deliverable. Every canonical ED parameter is mapped to a physical quantity with its formula, numerical value, and classification status.

| ED Parameter | Canonical value | Physical quantity | Formula (SI) | Value (electron, $d{=}2$) | Unit | Status |
|:-------------|:----------------|:------------------|:-------------|:--------------------------|:-----|:-------|
| $\rho$ | field in $[0,1]$ | Probability density $|\psi|^2$ | $\rho_{\text{phys}} = \hat{\rho} \cdot R_0$ | $\hat{\rho} \cdot 6.706 \times 10^{24}$ | m$^{-2}$ | **Anchored** |
| $D$ | 0.3 | Quantum diffusivity | $D_{\text{phys}} = \hbar/(2m)$ | $5.788 \times 10^{-5}$ | m$^2$ s$^{-1}$ | **Exact** |
| $M(\rho)$ | $M_0(\rho_{\max} - \rho)^\beta$ | Density-dependent mobility | $M_{\text{phys}} = M_0(1 - \hat{\rho})^\beta \cdot D_{\text{phys}}/D_{\text{nd}}$ | (state-dependent) | m$^2$ s$^{-1}$ | **ED-specific** |
| $P(\rho)$ | $P_0(\rho - \rho^*)$ | Restoring force (confining potential analogue) | $P_{\text{phys}} = P_0(\hat{\rho} - \hat{\rho}^*) \cdot R_0/T_0$ | (state-dependent) | m$^{-2}$ s$^{-1}$ | **Anchored** |
| $v(t)$ | scalar | Mean-field mode amplitude | $v_{\text{phys}} = \hat{v} \cdot V_0$ | $\hat{v} \cdot 4.997 \times 10^{8}$ | m s$^{-1}$ | **Candidate** |
| $H$ | 0–50 | Global coupling strength | $H_{\text{phys}} = H_{\text{nd}} \cdot V_0$ | $H_{\text{nd}} \cdot 4.997 \times 10^{8}$ | m s$^{-1}$ | **Candidate** |
| $\tau$ | 1.0 | Relaxation / decoherence timescale | $\tau_{\text{phys}} = \tau_{\text{nd}} \cdot T_0$ | $7.729 \times 10^{-22}$ | s | **Candidate** |
| $\zeta$ | 0.1 | Environmental damping | $\zeta_{\text{phys}} = \zeta_{\text{nd}} / T_0$ | $1.294 \times 10^{20}$ | s$^{-1}$ | **Candidate** |
| $\rho^*$ | 0.5 | Equilibrium probability density | $\rho^*_{\text{phys}} = \hat{\rho}^* \cdot R_0$ | $3.353 \times 10^{24}$ | m$^{-2}$ | **Anchored** |
| $\rho_{\max}$ | 1.0 | Normalization / Pauli bound | $\rho_{\max,\text{phys}} = R_0$ | $6.706 \times 10^{24}$ | m$^{-2}$ | **Anchored** |
| $M_0$ | 1.0 | Mobility prefactor | $M_{0,\text{phys}} = M_0 \cdot D_{\text{phys}}/D_{\text{nd}}$ | $1.930 \times 10^{-4}$ | m$^2$ s$^{-1}$ | **Anchored** |
| $\beta$ | 2.0 | Mobility exponent (PME index $m = \beta + 1 = 3$) | dimensionless | 2.0 | — | **Structural** |
| $P_0$ | 0.01–1.0 | Penalty slope | $P_{0,\text{phys}} = P_0 / T_0$ | $P_0 \cdot 1.294 \times 10^{21}$ | s$^{-1}$ | **Anchored** |

**Status key:**

- **Exact**: mathematical identity that holds regardless of interpretation (Madelung theorem, PME reduction, telegraph reduction).
- **Anchored**: uniquely determined once the three characteristic scales ($L_0$, $T_0$, $R_0$) are fixed.
- **ED-specific**: a prediction of the ED framework with no standard QM analogue (see Section 6).
- **Candidate**: physically motivated but not uniquely determined; alternative interpretations exist.
- **Structural**: a dimensionless constitutive parameter of the PDE, unchanged by nondimensionalization.

---

## 4. The PDE in SI Units

Restoring all dimensional factors, the ED PDE in the quantum regime reads:

$$\partial_t \rho = \frac{\hbar}{2m}\bigl[M(\rho/R_0)\,\nabla^2\rho + M'(\rho/R_0)\,|\nabla\rho|^2/R_0 - P_0(\rho - \rho^*)/T_0\bigr] + H_{\text{phys}}\,v,$$

where $M(\hat{\rho}) = (\rho_{\max}/R_0 - \hat{\rho})^\beta = (1 - \hat{\rho})^\beta$ and all spatial derivatives are in physical coordinates.

The participation equation in physical units:

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr),$$

where $\tau_{\text{phys}} = \tau_{\text{nd}} \cdot T_0 = 2\,\tau_{\text{nd}} D_{\text{nd}}\,\hbar/(mc^2)$.

The key observation: $\hbar$ and $m$ appear explicitly in the dimensional PDE. The quantum identity of the framework is carried by the diffusion coefficient $\hbar/(2m)$ and the length scale $\hbar/(mc)$.

---

## 5. Conversion Factor Table

Compact reference for converting ED-SIM-02 simulation output to SI units in the quantum regime (electron, $d = 2$, $D_{\text{nd}} = 0.3$):

| Quantity | ND $\to$ SI | SI $\to$ ND | Numerical factor |
|:---------|:-----------|:-----------|:-----------------|
| Length $x$ | $x_{\text{SI}} = \hat{x} \cdot L_0$ | $\hat{x} = x_{\text{SI}} / L_0$ | $L_0 = 3.862 \times 10^{-13}$ m |
| Time $t$ | $t_{\text{SI}} = \hat{t} \cdot T_0$ | $\hat{t} = t_{\text{SI}} / T_0$ | $T_0 = 7.729 \times 10^{-22}$ s |
| Density $\rho$ | $\rho_{\text{SI}} = \hat{\rho} \cdot R_0$ | $\hat{\rho} = \rho_{\text{SI}} / R_0$ | $R_0 = 6.706 \times 10^{24}$ m$^{-2}$ |
| Velocity $v$ | $v_{\text{SI}} = \hat{v} \cdot V_0$ | $\hat{v} = v_{\text{SI}} / V_0$ | $V_0 = 4.997 \times 10^{8}$ m s$^{-1}$ |
| Diffusivity $D$ | $D_{\text{SI}} = D_{\text{nd}} \cdot L_0^2/T_0$ | $D_{\text{nd}} = D_{\text{SI}} \cdot T_0/L_0^2$ | $D_0 = 1.930 \times 10^{-4}$ m$^2$ s$^{-1}$ |
| Correlation length $\xi$ | $\xi_{\text{SI}} = \hat{\xi} \cdot L_0$ | $\hat{\xi} = \xi_{\text{SI}} / L_0$ | $L_0 = 3.862 \times 10^{-13}$ m |

**Code example** (using the existing `edsim.units` API):

```python
from edsim.core.parameters import EDParameters
from edsim.units import quantum_scales
from edsim.units.constants import m_e

params = EDParameters(d=2, L=(1.0, 1.0), N=(64, 64))
sc = quantum_scales(params, mass=m_e)
print(f"L0 = {sc.L0:.4e} m")
print(f"T0 = {sc.T0:.4e} s")
print(f"R0 = {sc.R0:.4e} m^-2")
print(f"V0 = {sc.V0:.4e} m/s")
```

**Note on the current code.** The `quantum_scales()` factory in `scales.py` does not pass `D_phys = hbar/(2m)` to `compute_scales()`. It uses the default convention `T0 = L0^2 / D_nd`, which differs from the physically anchored `T0 = L0^2 D_nd / D_phys` by a factor of $D_{\text{nd}}^2 / D_{\text{phys}}$. For exact physical anchoring, `quantum_scales()` should be updated to pass `D_phys = hbar/(2*mass)`. The numerical values in this note use the physically anchored convention.

---

## 6. What Is Exact, What Is Candidate

### 6.1 Exact Correspondences

These are mathematical identities. They hold regardless of physical interpretation.

1. **$D = \hbar/(2m)$ as diffusion coefficient.** The Madelung transformation of the free-particle Schrödinger equation produces a continuity equation for $|\psi|^2$ with diffusive coefficient $\hbar/(2m)$. This is a theorem (Madelung 1927, Nelson 1966), not an analogy.

2. **$M(\rho)$ as porous-medium mobility.** The ED PDE with $P_0 = 0$, $H = 0$, under the substitution $\delta = \rho_{\max} - \rho$, reduces exactly to the porous-medium equation $\partial_t \delta = D_{\text{pme}}\nabla^2(\delta^m)$ with $m = \beta + 1$ and $D_{\text{pme}} = D M_0/(\beta + 1)$. This is the structural identity established in the foundational paper, Appendix D.

3. **$P(\rho)$ as RC decay.** The penalty channel in isolation ($M = 0$, $H = 0$) produces $\dot{\delta} = -D P_0 \delta$, which is exactly the RC-circuit discharge equation with time constant $\tau_{\text{RC}} = 1/(D P_0)$.

4. **Participation as telegraph oscillation.** The coupled $(\delta, v)$ linearised system is exactly the telegraph equation with $2\gamma = D P_0 + \zeta/\tau$ and $\omega_0^2 = (D P_0 \zeta + H P_0)/\tau$.

### 6.2 Anchored Correspondences

These are uniquely determined once the three characteristic scales are fixed:

- $\rho_{\max} \to R_0 = L_0^{-d}$ (normalization bound)
- $\rho^* \to \rho^*_{\text{nd}} \cdot R_0$ (equilibrium probability density)
- $T_0$, $V_0$, $E_0$ follow from $L_0$ and $D_{\text{phys}}$
- $M_0$, $P_0$ in physical units follow from their nondimensional values and $T_0$

### 6.3 Candidate Correspondences

These are physically motivated but not uniquely determined:

- **$v(t)$ as decoherence mode amplitude.** Plausible but not the only interpretation. Could also represent measurement back-action or environmental coupling.
- **$\tau$ as decoherence timescale.** In physical units: $\tau_{\text{phys}} = 7.73 \times 10^{-22}$ s for canonical parameters and the electron. This is in the sub-femtosecond range — comparable to electronic relaxation times in condensed matter, but the identification is not unique.
- **$H$ as measurement coupling.** Could also be environmental interaction strength, mean-field coupling, or collective feedback.
- **$\zeta$ as environmental damping.** The physical value $\zeta_{\text{phys}} \sim 10^{20}$ s$^{-1}$ is extremely large, suggesting the canonical $\zeta_{\text{nd}} = 0.1$ may not be the appropriate value for the quantum regime. This is an open question.

### 6.4 The Mobility: ED's Strongest Prediction or Weakest Link

The density-dependent mobility $M(\rho) = M_0(1 - \hat{\rho})^\beta$ is the most distinctive feature of the ED PDE. In the quantum regime, it predicts that probability-density diffusion **slows as the density approaches the normalization bound** and **vanishes at the bound**. Standard quantum mechanics has no such feature: the Schrödinger equation has constant (density-independent) diffusion.

This is either:

- **ED's most interesting prediction**: a beyond-QM effect where high probability density suppresses transport, analogous to Pauli blocking or nonlinear Schrödinger dynamics. If observed, it would distinguish ED from standard QM.
- **ED's weakest link**: if no density-dependent slowing is ever observed in quantum systems, the mobility structure ($\beta > 0$) is falsified in this regime.

The honest assessment: no experimental evidence currently supports or refutes this prediction. It is the most testable distinguishing feature of the quantum mapping.

---

## 7. Falsifiable Predictions

### 7.1 Predictions That Follow From the Mapping

1. **Diffusion timescale.** For a free electron, the ED diffusion coefficient is $D_{\text{phys}} = \hbar/(2m_e) = 5.79 \times 10^{-5}$ m$^2$/s. The characteristic time for probability-density evolution on the Compton length scale is $T_0 = 7.73 \times 10^{-22}$ s. Any ED simulation in the quantum regime must produce dynamics on this timescale.

2. **Density-dependent mobility.** ED predicts that probability-density transport slows as $\rho \to \rho_{\max}$. In standard QM, the probability current is independent of local density (except through the quantum potential). This is a distinguishing prediction: ED says the probability-density PDE is a porous-medium equation ($m = 3$ for $\beta = 2$), not a heat equation ($m = 1$).

3. **Penalty relaxation time.** The RC time constant in the quantum regime is $\tau_{\text{RC}} = T_0/(D_{\text{nd}} P_0) = 2.58 \times 10^{-21}$ s for canonical parameters. This predicts a specific timescale for the decay of probability-density perturbations toward equilibrium.

4. **Telegraph oscillation period.** For $H = 5$: $T_{\text{osc}} = 2\pi/\omega \cdot T_0 = 2.17 \times 10^{-21}$ s. This predicts a specific oscillation frequency for the participation variable — a global mode of the probability-density field.

### 7.2 What Would Falsify the Mapping

- If the quantum diffusion coefficient is measured to differ from $\hbar/(2m)$, the Madelung anchoring fails. (This would also falsify the Madelung transformation itself, which is a theorem — so this falsification condition is effectively a consistency check.)
- If probability-density evolution in high-density regimes shows no density-dependent slowing, the mobility channel ($\beta > 0$) is falsified in this regime.
- If the penalty relaxation time does not correspond to any observed quantum timescale (decoherence, relaxation, thermalization), the penalty mapping is unsupported.

### 7.3 What Would Not Falsify the Mapping

- The participation channel parameters ($v$, $H$, $\tau$, $\zeta$) are classified as candidates. Failure to match a specific observable weakens but does not falsify the structural core.
- The value $\beta = 2$ is a constitutive choice. Different values of $\beta$ may be appropriate for different quantum systems. Falsification of $\beta = 2$ does not falsify the mapping framework — only the specific constitutive choice.

---

## 8. Open Questions

1. **Code update.** The `quantum_scales()` factory should be updated to pass `D_phys = hbar/(2*mass)` to `compute_scales()` for exact physical anchoring. Currently, $T_0$ is computed from the nondimensional convention alone.

2. **Physical origin of $\rho^*$.** In standard QM, there is no preferred probability density. In ED, $\rho^* = 0.5 \cdot R_0$ is the equilibrium. What physical mechanism determines this resting point in the quantum regime? Possible candidates: vacuum fluctuation density, cosmological background, thermodynamic equilibrium. This is unresolved.

3. **Physical interpretation of $v(t)$.** The participation variable has no direct standard-QM analogue. It represents global, non-local coupling. Possible physical candidates: mean-field decoherence parameter, measurement back-action amplitude, environmental interaction mode. None is uniquely determined by the current mapping.

4. **Density-dependent mobility from first principles.** The mobility $M(\rho) = M_0(1 - \hat{\rho})^\beta$ is the ED constitutive choice. Is there a derivation of density-dependent probability diffusion from quantum first principles? Possible connections include nonlinear Schrödinger equations, quantum pressure in Bose-Einstein condensates, and Pauli exclusion effects in fermionic systems.

5. **Multi-particle extension.** The mapping presented here is for a single-particle probability density. Extension to $N$-body systems, entanglement, and quantum information requires mapping the ED field to multi-particle density matrices or Wigner functions. This is future work.

6. **Experimental comparison.** No quantitative comparison with experimental data (matter-wave diffraction, quantum dot spectra, decoherence timescales) has been performed. This is the essential next step for validating or falsifying the mapping.

---

## 9. Other Regimes (Preview)

The quantum regime is the first of five planned dimensional mappings. The others differ in their anchoring choices:

| Regime | $L_0$ | $R_0$ | $D_{\text{phys}}$ | Anchoring | Note |
|--------|--------|--------|---------------------|-----------|------|
| **Quantum** (this note) | $\hbar/(mc)$ | $L_0^{-d}$ | $\hbar/(2m)$ | Madelung theorem | ED-Dimensional-01 |
| Planck | $\ell_{\text{Pl}} = \sqrt{\hbar G/c^3}$ | $\rho_{\text{Pl}} = c^5/(\hbar G^2)$ | $\sqrt{\hbar G/c}$ | Planck units | ED-Dimensional-02 |
| Condensed matter | User-chosen ($\sim\mu$m) | User-chosen ($\sim$kg/m$^3$) | Thermal diffusivity | Experimental fit | ED-Dimensional-03 |
| Galactic | 1 kpc | $\rho_{\text{crit}}$ | User-chosen | Astrophysical scales | ED-Dimensional-04 |
| Cosmological | $c/H_0$ | $\rho_{\text{crit}}$ | User-chosen | Hubble scales | ED-Dimensional-05 |

The quantum regime was chosen first because it has the strongest anchoring: $D_{\text{phys}} = \hbar/(2m)$ is determined by a mathematical theorem, not by physical analogy or experimental fit. Every other regime requires at least one parameter to be set by convention or measurement.

---

## Appendix A: Derivation of $T_0$

Starting from the three anchoring choices:

$$L_0 = \frac{\hbar}{mc}, \quad R_0 = L_0^{-d}, \quad D_{\text{phys}} = \frac{\hbar}{2m}.$$

The time scale is:

$$T_0 = \frac{L_0^2\,D_{\text{nd}}}{D_{\text{phys}}} = \frac{\left(\frac{\hbar}{mc}\right)^2 D_{\text{nd}}}{\frac{\hbar}{2m}} = \frac{\hbar^2}{m^2 c^2} \cdot \frac{2m}{\hbar} \cdot D_{\text{nd}} = \frac{2\,D_{\text{nd}}\,\hbar}{mc^2}.$$

The velocity scale is:

$$V_0 = \frac{L_0}{T_0} = \frac{\hbar/(mc)}{2 D_{\text{nd}} \hbar/(mc^2)} = \frac{c}{2\,D_{\text{nd}}}.$$

For $D_{\text{nd}} = 0.3$: $V_0 = c/0.6 = 1.667\,c$.

This superluminal characteristic velocity reflects the parabolic nature of the PDE. The Schrödinger equation has the same property: it is parabolic with infinite propagation speed. Neither ED nor Schrödinger respects a causal light cone without relativistic extension. The characteristic velocity $V_0$ is a scale conversion factor, not a signal speed.

---

## Appendix B: Numerical Values for Common Particles ($d = 2$)

| Particle | Mass (kg) | $L_0$ (m) | $T_0$ (s) | $R_0$ (m$^{-2}$) | $D_{\text{phys}}$ (m$^2$/s) |
|:---------|:----------|:----------|:----------|:-----------------|:---------------------------|
| Electron | $9.109 \times 10^{-31}$ | $3.862 \times 10^{-13}$ | $7.729 \times 10^{-22}$ | $6.706 \times 10^{24}$ | $5.788 \times 10^{-5}$ |
| Proton | $1.673 \times 10^{-27}$ | $2.103 \times 10^{-16}$ | $4.209 \times 10^{-25}$ | $2.261 \times 10^{31}$ | $3.153 \times 10^{-8}$ |
| Planck mass | $2.176 \times 10^{-8}$ | $1.616 \times 10^{-35}$ | $3.235 \times 10^{-44}$ | $3.828 \times 10^{69}$ | $2.423 \times 10^{-27}$ |

Note: The Planck-mass row recovers the Planck scales ($L_0 = \ell_{\text{Pl}}$, $T_0 \approx 0.6\,t_{\text{Pl}}$). The quantum regime and Planck regime are connected by a single parameter: the particle mass.

---

## References

1. Madelung, E. "Quantentheorie in hydrodynamischer Form." *Z. Phys.* **40**, 322–326 (1927).
2. Nelson, E. "Derivation of the Schrödinger equation from Newtonian mechanics." *Phys. Rev.* **150**, 1079–1085 (1966).
3. Proxmire, A. "Event Density as an Ontological Framework: Constitutive Channels, Structural Laws, and Six Empirical Analogues." (2026).
4. Proxmire, A. ED-SIM-02: An Architectural Lab for Entropic Dynamics. Software package (2026).
5. Vazquez, J. L. *The Porous Medium Equation.* Oxford University Press (2007).
