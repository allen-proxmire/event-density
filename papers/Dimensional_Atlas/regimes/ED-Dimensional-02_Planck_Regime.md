# ED-Dimensional-02: Physical Units and Dimensional Mapping — The Planck Regime

**Allen Proxmire**
**March 2026**

---

**Canonical sources:**

| Source | Content used |
|--------|-------------|
| Critical Assessment (2026-03-27) | The challenge being addressed |
| ED-Dimensional-01 (Quantum Regime) | Nondimensionalization scheme, status classification, series template |
| ED Foundational Paper | Canonical PDE, Appendix A parameters, Appendix D PME derivation |
| `edsim/units/constants.py` | CODATA 2018 physical constants and Planck scales |
| `edsim/units/scales.py` | `Scales` dataclass, `compute_scales()`, `planck_scales()` |
| `archive/docs_legacy/units.md` | Nondimensionalization scheme |

**Scope.** This note addresses the Planck regime, where all three characteristic scales are built from the three constants $\hbar$, $G$, and $c$ — no particle mass, no temperature, no external scale. It is the second in the ED-Dimensional series (following ED-Dimensional-01: Quantum Regime) and the only regime in which the anchoring is fully determined by dimensional analysis alone.

---

## 0. The Challenge

The March 2026 Critical Assessment required a falsifiable mapping from ED parameters to physical constants. ED-Dimensional-01 addressed this for the quantum regime by anchoring $D_{\text{phys}} = \hbar/(2m)$ via the Madelung theorem — a mapping that depends on a particle mass $m$.

The Planck regime eliminates that free parameter. At the Planck scale, there is no external mass: the only available constants are $\hbar$, $G$, and $c$. Dimensional analysis fixes every scale uniquely. This makes the Planck regime the cleanest dimensional mapping in the ED programme — and simultaneously the most remote from experiment.

This note does **not** claim that ED describes Planck-scale physics. It claims that ED admits a unique, parameter-free mapping to Planck units, and that this mapping produces specific numerical predictions for every ED quantity in SI units. Whether those predictions are physically meaningful is an open question that depends on whether ED's constitutive structure (degenerate mobility, monostable penalty, global participation) is relevant at the Planck scale.

---

## 1. The Nondimensionalization Scheme

The general scheme is identical to ED-Dimensional-01, Section 1. The canonical ED PDE in physical (SI) units is:

$$\partial_t \rho = D_{\text{phys}}\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr).$$

Three characteristic scales ($L_0$, $T_0$, $R_0$) and two derived scales ($V_0 = L_0/T_0$, $E_0 = R_0 \cdot L_0^d$) define the mapping between nondimensional simulation variables and SI quantities:

$$\hat{x} = x/L_0, \quad \hat{t} = t/T_0, \quad \hat{\rho} = \rho/R_0, \quad \hat{v} = v/V_0.$$

After substitution, the nondimensional PDE has $\hat{D} = D_{\text{nd}}$ by construction of $T_0$.

---

## 2. The Planck Regime: Scale Anchoring

### 2.1 The Planck Scales

The Planck scales are the unique combinations of $\hbar$, $G$, and $c$ with dimensions of length, time, and mass density:

$$\ell_{\text{Pl}} = \sqrt{\frac{\hbar G}{c^3}} = 1.616 \times 10^{-35}\;\text{m},$$

$$t_{\text{Pl}} = \sqrt{\frac{\hbar G}{c^5}} = 5.391 \times 10^{-44}\;\text{s},$$

$$\rho_{\text{Pl}} = \frac{c^5}{\hbar G^2} = 5.155 \times 10^{96}\;\text{kg m}^{-3}.$$

These are not postulated. They are the only scales that can be formed from $\hbar$, $G$, and $c$ with the appropriate dimensions. No other combination exists.

### 2.2 Length: $L_0 = \ell_{\text{Pl}}$

$$L_0 = \sqrt{\frac{\hbar G}{c^3}} = 1.616 \times 10^{-35}\;\text{m}.$$

This is the scale at which quantum gravitational effects are expected to become significant. Below $\ell_{\text{Pl}}$, the semiclassical spacetime picture is expected to break down. If ED's density field is to have a geometric or proto-gravitational interpretation, the Planck length is the natural resolution limit.

### 2.3 Density: $R_0 = \rho_{\text{Pl}}$

$$R_0 = \frac{c^5}{\hbar G^2} = 5.155 \times 10^{96}\;\text{kg m}^{-3}.$$

This is the Planck density — the mass-energy concentration at which a region of size $\ell_{\text{Pl}}$ contains one Planck mass. In ED, $\rho_{\max} = R_0 = \rho_{\text{Pl}}$: the capacity bound is the Planck density. This is the most extreme density the framework permits. The mobility vanishes at $\rho = \rho_{\text{Pl}}$, creating an ED horizon.

**Physical interpretation.** If $\rho$ represents energy density (or mass density), then $\rho_{\text{Pl}}$ is the density at which classical general relativity predicts a singularity and quantum gravity is expected to regularise it. ED regularises it differently: the degenerate mobility $M(\rho) \to 0$ halts transport before the density can diverge. The ED horizon is a structural analogue of the Planck-density cutoff expected from quantum gravity.

### 2.4 Diffusivity: $D_{\text{phys}} = \ell_{\text{Pl}}^2 / t_{\text{Pl}}$

The Planck diffusivity is the unique combination of $\hbar$, $G$, and $c$ with dimensions of m$^2$ s$^{-1}$:

$$D_{\text{phys}} = \frac{\ell_{\text{Pl}}^2}{t_{\text{Pl}}} = \sqrt{\frac{\hbar G}{c}} = 4.845 \times 10^{-27}\;\text{m}^2\text{ s}^{-1}.$$

This can be verified directly: $\ell_{\text{Pl}}^2 / t_{\text{Pl}} = (\hbar G / c^3) / \sqrt{\hbar G / c^5} = \sqrt{\hbar G / c}$.

An equivalent expression is $D_{\text{phys}} = \ell_{\text{Pl}} \cdot c$, which has a suggestive interpretation: the Planck diffusivity is the product of the smallest meaningful length and the largest meaningful speed. This is the maximum possible diffusivity consistent with both quantum mechanics ($\hbar$) and general relativity ($G$, $c$).

**Connection to ED-Dimensional-01.** In the quantum regime, $D_{\text{phys}} = \hbar/(2m)$. Setting $m = m_{\text{Pl}} = \sqrt{\hbar c / G}$ yields $D_{\text{phys}} = \hbar/(2\sqrt{\hbar c/G}) = \sqrt{\hbar G/c}/2$. This differs from the Planck-regime value $\sqrt{\hbar G/c}$ by a factor of 2, which arises because the quantum-regime $T_0$ is defined via $D_{\text{phys}} = \hbar/(2m)$ while the Planck-regime $T_0$ uses $D_{\text{phys}} = \ell_{\text{Pl}}^2/t_{\text{Pl}}$ directly. The two regimes converge at $m = m_{\text{Pl}}$ to within a factor of 2 — a convention-dependent numerical constant, not a structural discrepancy.

### 2.5 Time Scale

$$T_0 = \frac{L_0^2\,D_{\text{nd}}}{D_{\text{phys}}} = \frac{\ell_{\text{Pl}}^2 \cdot D_{\text{nd}}}{\ell_{\text{Pl}}^2 / t_{\text{Pl}}} = D_{\text{nd}} \cdot t_{\text{Pl}}.$$

This is the cleanest result in the entire ED-Dimensional series:

$$\boxed{T_0 = D_{\text{nd}} \cdot t_{\text{Pl}}.}$$

The ED time scale in the Planck regime is simply the Planck time multiplied by the nondimensional diffusion weight. For $D_{\text{nd}} = 0.3$:

$$T_0 = 0.3 \times 5.391 \times 10^{-44}\;\text{s} = 1.617 \times 10^{-44}\;\text{s}.$$

### 2.6 Velocity Scale

$$V_0 = \frac{L_0}{T_0} = \frac{\ell_{\text{Pl}}}{D_{\text{nd}} \cdot t_{\text{Pl}}} = \frac{c}{D_{\text{nd}}}.$$

For $D_{\text{nd}} = 0.3$: $V_0 = c/0.3 = 3.333\,c$.

The same superluminal caveat applies as in ED-Dimensional-01, Section 2.5. The characteristic velocity $V_0$ is a nondimensionalization scale factor, not a signal speed. The parabolic ED PDE does not respect a causal light cone. At the Planck scale, this is a particularly significant caveat: any physically meaningful Planck-scale dynamics would need to be embedded in a causal (hyperbolic) framework.

### 2.7 Energy Scale

$$E_0 = R_0 \cdot L_0^d.$$

For $d = 3$:

$$E_0 = \rho_{\text{Pl}} \cdot \ell_{\text{Pl}}^3 = \frac{c^5}{\hbar G^2} \cdot \left(\frac{\hbar G}{c^3}\right)^{3/2} = \sqrt{\frac{\hbar c}{G}} \cdot c = m_{\text{Pl}} c^2... $$

Let us compute directly: $E_0 = 5.155 \times 10^{96} \times (1.616 \times 10^{-35})^3 = 2.176 \times 10^{-8}$ J.

This equals $m_{\text{Pl}} \cdot c^2$... no. $m_{\text{Pl}} c^2 = 2.176 \times 10^{-8} \times (2.998 \times 10^8)^2 = 1.956 \times 10^9$ J $= E_{\text{Pl}}$. So $E_0 = m_{\text{Pl}}$ in kg, or equivalently $E_0 = \rho_{\text{Pl}} \cdot \ell_{\text{Pl}}^3 = m_{\text{Pl}}$: the total mass in one Planck volume at Planck density is one Planck mass. The energy scale $E_0$ in Joules requires an additional factor of $c^2$:

$$E_0 = m_{\text{Pl}} = 2.176 \times 10^{-8}\;\text{kg} \quad (\text{mass scale}).$$

$$E_0 \cdot c^2 = E_{\text{Pl}} = 1.956 \times 10^{9}\;\text{J} \quad (\text{energy scale}).$$

### 2.8 Summary of Planck-Regime Scales

| Scale | Formula | Value | Unit | Relation to Planck unit |
|:------|:--------|:------|:-----|:-----------------------|
| $L_0$ | $\sqrt{\hbar G/c^3}$ | $1.616 \times 10^{-35}$ | m | $= \ell_{\text{Pl}}$ |
| $T_0$ | $D_{\text{nd}} \cdot t_{\text{Pl}}$ | $1.617 \times 10^{-44}$ | s | $= 0.3\,t_{\text{Pl}}$ |
| $R_0$ | $c^5/(\hbar G^2)$ | $5.155 \times 10^{96}$ | kg m$^{-3}$ | $= \rho_{\text{Pl}}$ |
| $V_0$ | $c/D_{\text{nd}}$ | $9.993 \times 10^{8}$ | m s$^{-1}$ | $= 3.333\,c$ |
| $D_{\text{phys}}$ | $\sqrt{\hbar G/c}$ | $4.845 \times 10^{-27}$ | m$^2$ s$^{-1}$ | $= \ell_{\text{Pl}}^2/t_{\text{Pl}}$ |
| $E_0\;(d{=}3)$ | $\rho_{\text{Pl}} \cdot \ell_{\text{Pl}}^3$ | $2.176 \times 10^{-8}$ | kg | $= m_{\text{Pl}}$ |

---

## 3. The ED-to-Planck Dictionary

Every canonical ED parameter is mapped to its Planck-regime physical quantity.

| ED Parameter | Canonical value | Physical quantity | Formula (SI) | Value ($d{=}3$) | Unit | Status |
|:-------------|:----------------|:------------------|:-------------|:-----------------|:-----|:-------|
| $\rho$ | field in $[0,1]$ | Mass-energy density | $\rho_{\text{phys}} = \hat{\rho} \cdot \rho_{\text{Pl}}$ | $\hat{\rho} \cdot 5.155 \times 10^{96}$ | kg m$^{-3}$ | **Anchored** |
| $D$ | 0.3 | Planck diffusivity | $D_{\text{phys}} = \sqrt{\hbar G/c}$ | $4.845 \times 10^{-27}$ | m$^2$ s$^{-1}$ | **Anchored** |
| $M(\rho)$ | $M_0(\rho_{\max} - \rho)^\beta$ | Density-dependent mobility | $M_{\text{phys}} = M_0(1 - \hat{\rho})^\beta \cdot D_{\text{phys}}/D_{\text{nd}}$ | (state-dependent) | m$^2$ s$^{-1}$ | **ED-specific** |
| $P(\rho)$ | $P_0(\rho - \rho^*)$ | Restoring force toward equilibrium | $P_{\text{phys}} = P_0(\hat{\rho} - \hat{\rho}^*) \cdot R_0/T_0$ | (state-dependent) | kg m$^{-3}$ s$^{-1}$ | **Anchored** |
| $v(t)$ | scalar | Global mode amplitude | $v_{\text{phys}} = \hat{v} \cdot V_0$ | $\hat{v} \cdot 9.993 \times 10^{8}$ | m s$^{-1}$ | **Candidate** |
| $H$ | 0–50 | Global coupling strength | $H_{\text{phys}} = H_{\text{nd}} \cdot V_0$ | $H_{\text{nd}} \cdot 9.993 \times 10^{8}$ | m s$^{-1}$ | **Candidate** |
| $\tau$ | 1.0 | Participation timescale | $\tau_{\text{phys}} = \tau_{\text{nd}} \cdot T_0$ | $1.617 \times 10^{-44}$ | s | **Candidate** |
| $\zeta$ | 0.1 | Damping rate | $\zeta_{\text{phys}} = \zeta_{\text{nd}} / T_0$ | $6.183 \times 10^{42}$ | s$^{-1}$ | **Candidate** |
| $\rho^*$ | 0.5 | Equilibrium density | $\rho^*_{\text{phys}} = 0.5 \cdot \rho_{\text{Pl}}$ | $2.577 \times 10^{96}$ | kg m$^{-3}$ | **Anchored** |
| $\rho_{\max}$ | 1.0 | Planck density (capacity bound) | $\rho_{\max,\text{phys}} = \rho_{\text{Pl}}$ | $5.155 \times 10^{96}$ | kg m$^{-3}$ | **Anchored** |
| $M_0$ | 1.0 | Mobility prefactor | $M_{0,\text{phys}} = D_{\text{phys}}/D_{\text{nd}}$ | $1.615 \times 10^{-26}$ | m$^2$ s$^{-1}$ | **Anchored** |
| $\beta$ | 2.0 | Mobility exponent (PME index $m = 3$) | dimensionless | 2.0 | — | **Structural** |
| $P_0$ | 0.01–1.0 | Penalty slope | $P_{0,\text{phys}} = P_0 / T_0$ | $P_0 \cdot 6.183 \times 10^{43}$ | s$^{-1}$ | **Anchored** |

**Status key** (same as ED-Dimensional-01):

- **Anchored**: uniquely determined by the three Planck scales. No free parameters remain.
- **ED-specific**: a prediction of the ED framework with no standard analogue in quantum gravity.
- **Candidate**: physically motivated but not uniquely determined; the participation channel has no established Planck-scale counterpart.
- **Structural**: a dimensionless constitutive parameter, unchanged by nondimensionalization.

**Note on "Exact" status.** Unlike the quantum regime, where $D = \hbar/(2m)$ is fixed by the Madelung theorem, the Planck regime has no analogous mathematical theorem fixing $D_{\text{phys}}$. The identification $D_{\text{phys}} = \sqrt{\hbar G/c}$ follows from dimensional analysis — it is the unique combination of $\hbar$, $G$, $c$ with dimensions of diffusivity. This is a stronger constraint than convention but weaker than a theorem. Accordingly, $D_{\text{phys}}$ is classified as **anchored** rather than exact.

---

## 4. The PDE in SI Units

Restoring all dimensional factors, the ED PDE in the Planck regime reads:

$$\partial_t \rho = \sqrt{\frac{\hbar G}{c}}\,\bigl[M(\rho/\rho_{\text{Pl}})\,\nabla^2\rho + M'(\rho/\rho_{\text{Pl}})\,|\nabla\rho|^2/\rho_{\text{Pl}} - P_0(\rho - \rho^*)/T_0\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr),$$

where $M(\hat{\rho}) = (1 - \hat{\rho})^\beta$, all spatial derivatives are in physical coordinates, and:

$$\tau_{\text{phys}} = \tau_{\text{nd}} \cdot D_{\text{nd}} \cdot t_{\text{Pl}}.$$

The key observation: all three constants $\hbar$, $G$, and $c$ appear explicitly in the dimensional PDE. The Planck identity of the framework is carried entirely by the diffusion coefficient $\sqrt{\hbar G/c}$, the density scale $c^5/(\hbar G^2)$, and the length scale $\sqrt{\hbar G/c^3}$. No particle mass, temperature, or external scale enters.

---

## 5. Conversion Factor Table

Compact reference for converting ED-SIM-02 simulation output to SI units in the Planck regime ($d = 3$, $D_{\text{nd}} = 0.3$):

| Quantity | ND $\to$ SI | SI $\to$ ND | Numerical factor |
|:---------|:-----------|:-----------|:-----------------|
| Length $x$ | $x_{\text{SI}} = \hat{x} \cdot \ell_{\text{Pl}}$ | $\hat{x} = x_{\text{SI}} / \ell_{\text{Pl}}$ | $\ell_{\text{Pl}} = 1.616 \times 10^{-35}$ m |
| Time $t$ | $t_{\text{SI}} = \hat{t} \cdot D_{\text{nd}} \cdot t_{\text{Pl}}$ | $\hat{t} = t_{\text{SI}} / (D_{\text{nd}} \cdot t_{\text{Pl}})$ | $T_0 = 1.617 \times 10^{-44}$ s |
| Density $\rho$ | $\rho_{\text{SI}} = \hat{\rho} \cdot \rho_{\text{Pl}}$ | $\hat{\rho} = \rho_{\text{SI}} / \rho_{\text{Pl}}$ | $\rho_{\text{Pl}} = 5.155 \times 10^{96}$ kg m$^{-3}$ |
| Velocity $v$ | $v_{\text{SI}} = \hat{v} \cdot c/D_{\text{nd}}$ | $\hat{v} = v_{\text{SI}} \cdot D_{\text{nd}}/c$ | $V_0 = 9.993 \times 10^{8}$ m s$^{-1}$ |
| Diffusivity $D$ | $D_{\text{SI}} = D_{\text{nd}} \cdot \ell_{\text{Pl}}^2/T_0$ | $D_{\text{nd}} = D_{\text{SI}} \cdot T_0/\ell_{\text{Pl}}^2$ | $D_0 = 1.615 \times 10^{-26}$ m$^2$ s$^{-1}$ |
| Mass (d=3) | $m_{\text{SI}} = \hat{m} \cdot m_{\text{Pl}}$ | $\hat{m} = m_{\text{SI}} / m_{\text{Pl}}$ | $m_{\text{Pl}} = 2.176 \times 10^{-8}$ kg |

**Code example** (using the existing `edsim.units` API):

```python
from edsim.core.parameters import EDParameters
from edsim.units import planck_scales

params = EDParameters(d=3, L=(1.0, 1.0, 1.0), N=(32, 32, 32))
sc = planck_scales(params)
print(f"L0 = {sc.L0:.4e} m  (Planck length)")
print(f"T0 = {sc.T0:.4e} s")
print(f"R0 = {sc.R0:.4e} kg/m^3  (Planck density)")
print(f"V0 = {sc.V0:.4e} m/s")
```

**Note on the current code.** The `planck_scales()` factory in `scales.py` sets `L0 = l_Pl` and `R0 = rho_Pl` but does not pass `D_phys = sqrt(hbar*G/c)` to `compute_scales()`. As with the quantum regime, the physically anchored convention gives $T_0 = D_{\text{nd}} \cdot t_{\text{Pl}}$, while the default code convention gives $T_0 = \ell_{\text{Pl}}^2/D_{\text{nd}}$. The numerical values in this note use the physically anchored convention.

---

## 6. What Is Exact, What Is Candidate

### 6.1 Dimensional Correspondences

In the Planck regime, no mathematical theorem (like the Madelung identity) fixes $D_{\text{phys}}$. Instead, the anchoring is determined by **dimensional uniqueness**: $\sqrt{\hbar G/c}$ is the only combination of $\hbar$, $G$, $c$ with dimensions of diffusivity. This is a constraint from dimensional analysis, not from a dynamical equation. Accordingly, the strongest classification available is "anchored" (uniquely determined by the scale choice), not "exact" (mathematical identity).

The four structural identities from ED-Dimensional-01, Section 6.1 still hold in any regime:

1. **PME reduction.** $M(\rho)$ with $P_0 = 0$, $H = 0$ reduces to the porous-medium equation with $m = \beta + 1$. This is a property of the PDE, independent of the physical regime.

2. **RC decay.** The penalty channel in isolation produces exponential decay with $\tau_{\text{RC}} = 1/(D_{\text{nd}} P_0)$ in nondimensional time. In the Planck regime: $\tau_{\text{RC,phys}} = t_{\text{Pl}}/(P_0)$ for canonical $D_{\text{nd}} = 0.3$. For $P_0 = 1.0$: $\tau_{\text{RC}} = t_{\text{Pl}} = 5.391 \times 10^{-44}$ s. **The penalty relaxation time equals one Planck time.**

3. **Telegraph oscillation.** The coupled $(\delta, v)$ system produces telegraph dynamics. For $H = 5$, canonical parameters: $T_{\text{osc}} = 0.84\,t_{\text{Pl}}$. Oscillation periods are sub-Planck-time — a prediction that may be unphysical (see Section 8).

4. **Horizon formation.** Mobility vanishes at $\rho = \rho_{\text{Pl}}$. ED horizons form when the density approaches the Planck density — structurally analogous to the expectation from quantum gravity that new physics regularises singularities at $\rho_{\text{Pl}}$.

### 6.2 Anchored Correspondences

All Planck-regime scales are uniquely fixed by dimensional analysis:

- $L_0 = \ell_{\text{Pl}}$: no free parameter.
- $R_0 = \rho_{\text{Pl}}$: no free parameter.
- $D_{\text{phys}} = \sqrt{\hbar G/c}$: no free parameter.
- $T_0 = D_{\text{nd}} \cdot t_{\text{Pl}}$: determined by $D_{\text{nd}}$ alone.
- $V_0 = c/D_{\text{nd}}$: determined by $D_{\text{nd}}$ alone.
- All physical-unit parameter values follow without additional choices.

### 6.3 Candidate Correspondences

The participation channel parameters ($v$, $H$, $\tau$, $\zeta$) have no established Planck-scale counterparts:

- **$v(t)$ as a proto-cosmological mode.** At the Planck scale, a global variable driven by the domain-averaged density operator could represent a pre-inflationary field, a cosmological condensate, or a quantum-gravitational collective mode. None of these identifications is established.
- **$\tau_{\text{phys}} \sim 10^{-44}$ s.** Sub-Planck-time dynamics. The physical meaning of a relaxation timescale shorter than $t_{\text{Pl}}$ is unclear. This may indicate that the canonical $\tau_{\text{nd}} = 1.0$ is not appropriate for the Planck regime.
- **$\zeta_{\text{phys}} \sim 10^{42}$ s$^{-1}$.** Extremely large damping rate. Same caveat as $\tau$.

### 6.4 The Mobility at the Planck Scale

In the Planck regime, the ED mobility $M(\rho) = M_0(1 - \hat{\rho})^\beta$ predicts that diffusion halts as the energy density approaches $\rho_{\text{Pl}}$. This is the ED analogue of the widespread expectation in quantum gravity that the Planck density represents a physical cutoff — a maximum density beyond which the classical description breaks down.

The structural correspondence is notable:

| Feature | Quantum gravity expectation | ED prediction |
|---------|---------------------------|---------------|
| Maximum density | $\rho_{\text{Pl}}$ (singularity resolution) | $\rho_{\max} = \rho_{\text{Pl}}$ (mobility vanishes) |
| Mechanism | Unknown (loop quantum gravity, strings, ...) | Degenerate mobility $M \to 0$ |
| Boundary type | Conjectured (bounce, minimum area, ...) | Transient horizon (monotone retreat) |
| Permanence | Possibly permanent | Strictly temporary (monostable penalty) |

The last row is the most important. ED horizons are transient — the monostable penalty guarantees collapse back to equilibrium. If Planck-scale density saturation is permanent (as in some loop quantum gravity models), the ED architecture is structurally incompatible. If it is temporary (as in cosmological bounce scenarios), the structural analogy holds.

---

## 7. Falsifiable Predictions

### 7.1 Predictions That Follow From the Mapping

1. **Planck diffusivity.** $D_{\text{phys}} = \sqrt{\hbar G/c} = 4.845 \times 10^{-27}$ m$^2$/s. Any ED simulation in the Planck regime must produce dynamics with this diffusion coefficient. The diffusion time across one Planck length is $T_0/D_{\text{nd}} = t_{\text{Pl}}$.

2. **Density saturation at $\rho_{\text{Pl}}$.** ED predicts that transport halts as $\rho \to \rho_{\text{Pl}}$. The front-propagation speed vanishes. This is the ED version of Planck-density regularisation.

3. **Penalty relaxation in one Planck time.** For canonical $D_{\text{nd}} = 0.3$ and $P_0 = 1.0$: $\tau_{\text{RC}} = t_{\text{Pl}}$. Density perturbations above $\rho^*$ decay exponentially with time constant $t_{\text{Pl}}$.

4. **Horizon lifetime.** An ED horizon (where $M < M_{\text{crit}}$) forming at Planck density has lifetime $\tau_H \sim \text{few} \times t_{\text{Pl}}$. The horizon is transient. If Planck-scale horizons in nature are permanent, this prediction is falsified.

5. **Barenblatt spreading exponent.** The PME reduction gives $\alpha_R = 1/(d(m-1)+2) = 1/8$ for $d = 3$, $\beta = 2$. A Planck-density perturbation spreads with front radius $R(t) \propto t^{1/8}$ in Planck units.

### 7.2 What Would Falsify the Mapping

- If a well-established quantum-gravity framework predicts a Planck diffusivity different from $\sqrt{\hbar G/c}$, the dimensional anchoring is contradicted.
- If Planck-scale density saturation is permanent (non-decaying), the monostable penalty is falsified in this regime.
- If the Planck regime requires non-scalar degrees of freedom (tensors, spinors, gauge fields), the single-scalar-field axiom (P5) is falsified.

### 7.3 What Would Not Falsify the Mapping

- The participation channel parameters are candidates. They are not required to match specific quantum-gravity observables.
- The canonical nondimensional parameter values ($D_{\text{nd}} = 0.3$, $\beta = 2$, etc.) are constitutive choices. Different values may be appropriate at the Planck scale.
- The parabolic (non-causal) character of the PDE is a known limitation, not a falsification. A hyperbolic extension would be needed for causal Planck-scale dynamics.

---

## 8. Open Questions

1. **Physical status of Planck diffusivity.** Is $D_{\text{phys}} = \sqrt{\hbar G/c}$ a meaningful physical quantity, or merely a dimensional combination? In the quantum regime, $D = \hbar/(2m)$ is fixed by the Madelung theorem. No analogous theorem exists for the Planck regime. The anchoring is dimensional, not dynamical.

2. **Sub-Planck-time dynamics.** For canonical parameters, the participation timescale $\tau_{\text{phys}} = 1.617 \times 10^{-44}$ s and the telegraph period $T_{\text{osc}} = 4.55 \times 10^{-44}$ s are comparable to or shorter than $t_{\text{Pl}}$. If the Planck time is a fundamental resolution limit, these predictions may be unphysical. This suggests that the canonical nondimensional parameters may not be appropriate for the Planck regime — specifically, $\tau_{\text{nd}}$ and $\zeta_{\text{nd}}$ may need to be rescaled.

3. **Equilibrium density $\rho^*$.** In the Planck regime, $\rho^* = 0.5\,\rho_{\text{Pl}} = 2.58 \times 10^{96}$ kg m$^{-3}$. What physical mechanism sets the equilibrium density at half the Planck density? Possible candidates: vacuum energy density (far too low), cosmological equilibrium (scale mismatch), or a purely structural convention. This is unresolved.

4. **Causality.** The parabolic ED PDE has infinite propagation speed, which is incompatible with the causal structure expected at the Planck scale. The ED-Phys-13/14 hyperbolic extension (telegraph-type modification) would restore finite propagation speed. Whether this extension preserves the structural correspondences established in the foundational paper is an open question.

5. **Tensor structure.** Planck-scale physics is expected to involve tensor fields (the metric in general relativity, spin connections in loop quantum gravity). ED's axiom P5 restricts the framework to a single scalar field. This is the most fundamental architectural limitation for the Planck regime.

6. **Connection to quantum regime.** Setting $m = m_{\text{Pl}}$ in the quantum-regime mapping (ED-Dimensional-01) recovers the Planck length and approximately recovers the Planck time, but the diffusivities differ by a factor of 2. A unified treatment that smoothly interpolates between the quantum and Planck regimes requires resolving this convention-dependent discrepancy.

7. **Code update.** The `planck_scales()` factory should be updated to pass `D_phys = sqrt(hbar*G/c)` to `compute_scales()` for exact physical anchoring.

---

## 9. Other Regimes (Preview)

| Regime | $L_0$ | $R_0$ | $D_{\text{phys}}$ | Anchoring | Note |
|--------|--------|--------|---------------------|-----------|------|
| Quantum | $\hbar/(mc)$ | $L_0^{-d}$ | $\hbar/(2m)$ | Madelung theorem | ED-Dimensional-01 |
| **Planck** (this note) | $\ell_{\text{Pl}}$ | $\rho_{\text{Pl}}$ | $\sqrt{\hbar G/c}$ | Dimensional uniqueness | ED-Dimensional-02 |
| Condensed matter | User-chosen ($\sim\mu$m) | User-chosen ($\sim$kg/m$^3$) | Thermal diffusivity | Experimental fit | ED-Dimensional-03 |
| Galactic | 1 kpc | $\rho_{\text{crit}}$ | User-chosen | Astrophysical scales | ED-Dimensional-04 |
| Cosmological | $c/H_0$ | $\rho_{\text{crit}}$ | User-chosen | Hubble scales | ED-Dimensional-05 |

The Planck regime is the second note in the series because it has the second-strongest anchoring: all three scales are uniquely determined by dimensional analysis from $\hbar$, $G$, $c$, with no free parameters. The quantum regime (ED-Dimensional-01) is first because its diffusivity is fixed by a theorem, not just by dimensional analysis. The remaining three regimes each introduce at least one experimentally or conventionally chosen parameter.

---

## Appendix A: Derivation of Planck-Regime Scales

Starting from the three constants $\hbar$, $G$, $c$:

**Length.** The unique combination with dimensions of length:

$$L_0 = \ell_{\text{Pl}} = \sqrt{\frac{\hbar G}{c^3}}.$$

**Density.** The unique combination with dimensions of kg m$^{-3}$:

$$R_0 = \rho_{\text{Pl}} = \frac{c^5}{\hbar G^2}.$$

**Diffusivity.** The unique combination with dimensions of m$^2$ s$^{-1}$:

$$D_{\text{phys}} = \sqrt{\frac{\hbar G}{c}} = \frac{\ell_{\text{Pl}}^2}{t_{\text{Pl}}} = \ell_{\text{Pl}} \cdot c.$$

**Time scale.** From $T_0 = L_0^2 D_{\text{nd}} / D_{\text{phys}}$:

$$T_0 = \frac{\ell_{\text{Pl}}^2 \cdot D_{\text{nd}}}{\ell_{\text{Pl}}^2 / t_{\text{Pl}}} = D_{\text{nd}} \cdot t_{\text{Pl}} = D_{\text{nd}} \sqrt{\frac{\hbar G}{c^5}}.$$

**Velocity scale.** From $V_0 = L_0/T_0$:

$$V_0 = \frac{\ell_{\text{Pl}}}{D_{\text{nd}} \cdot t_{\text{Pl}}} = \frac{c}{D_{\text{nd}}}.$$

**Verification.** $D_{\text{nd}} = D_{\text{phys}} \cdot T_0 / L_0^2 = \sqrt{\hbar G/c} \cdot D_{\text{nd}} t_{\text{Pl}} / (\hbar G/c^3) = D_{\text{nd}} \cdot (t_{\text{Pl}} c^3) / (\sqrt{\hbar G/c} \cdot ... )$. More directly: $D_{\text{phys}} \cdot T_0 / L_0^2 = (\ell_{\text{Pl}}^2/t_{\text{Pl}}) \cdot (D_{\text{nd}} \cdot t_{\text{Pl}}) / \ell_{\text{Pl}}^2 = D_{\text{nd}}$. Confirmed.

---

## Appendix B: Comparison of Quantum and Planck Regimes at $m = m_{\text{Pl}}$

| Scale | Quantum regime ($m = m_{\text{Pl}}$) | Planck regime | Ratio |
|:------|:-------------------------------------|:--------------|:------|
| $L_0$ | $\hbar/(m_{\text{Pl}} c) = \ell_{\text{Pl}}$ | $\ell_{\text{Pl}}$ | 1 |
| $R_0$ ($d = 3$) | $\ell_{\text{Pl}}^{-3}$ | $\rho_{\text{Pl}}$ | $\rho_{\text{Pl}} \cdot \ell_{\text{Pl}}^3 = m_{\text{Pl}}$ |
| $D_{\text{phys}}$ | $\hbar/(2m_{\text{Pl}}) = \sqrt{\hbar G/c}/2$ | $\sqrt{\hbar G/c}$ | 2 |
| $T_0$ | $2 D_{\text{nd}} \hbar/(m_{\text{Pl}} c^2) = 2 D_{\text{nd}} \cdot t_{\text{Pl}}$ | $D_{\text{nd}} \cdot t_{\text{Pl}}$ | 2 |
| $V_0$ | $c/(2 D_{\text{nd}})$ | $c/D_{\text{nd}}$ | 2 |

The two regimes share $L_0 = \ell_{\text{Pl}}$ at $m = m_{\text{Pl}}$. The factor-of-2 differences in $D_{\text{phys}}$, $T_0$, and $V_0$ arise from the Madelung convention $D = \hbar/(2m)$ versus the Planck convention $D = \ell_{\text{Pl}}^2/t_{\text{Pl}}$. The density scales differ because the quantum regime normalises to probability ($R_0 = L_0^{-d}$) while the Planck regime normalises to mass density ($R_0 = \rho_{\text{Pl}}$). These are convention-dependent differences, not structural inconsistencies.

---

## References

1. Proxmire, A. "ED-Dimensional-01: Physical Units and Dimensional Mapping — The Quantum Regime." (2026).
2. Proxmire, A. "Event Density as an Ontological Framework: Constitutive Channels, Structural Laws, and Six Empirical Analogues." (2026).
3. Proxmire, A. ED-SIM-02: An Architectural Lab for Entropic Dynamics. Software package (2026).
4. Planck, M. "Über irreversible Strahlungsvorgänge." *Sitzungsberichte der Preußischen Akademie der Wissenschaften*, 440–480 (1899).
5. Misner, C. W., Thorne, K. S., and Wheeler, J. A. *Gravitation.* W. H. Freeman (1973).
6. Vazquez, J. L. *The Porous Medium Equation.* Oxford University Press (2007).
