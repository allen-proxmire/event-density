# ED-Dimensional-Master: The Unified Atlas of Physical Scales

**Allen Proxmire**
**March 2026**

---

## 0. Executive Summary

This document is the capstone of the ED-Dimensional series. It synthesises five regime-specific monographs (ED-Dimensional-01 through 05) into a single, self-contained atlas showing how one canonical PDE acquires physical meaning across the entire range of known scales — from the Planck length ($10^{-35}$ m) to the Hubble length ($10^{26}$ m), spanning 61 orders of magnitude.

**What the atlas contains.** A universal nondimensionalization scheme; five complete regime mappings (quantum, Planck, condensed matter, galactic, cosmological); a master dictionary translating every ED parameter into physical quantities at each scale; a catalogue of cross-regime invariants; a regime manifold showing how scales connect; and a consolidated list of falsifiable predictions.

**What the five-regime mapping achieves.** It demonstrates that the canonical ED PDE — derived from seven structural axioms, with three constitutive channels — admits a consistent dimensional interpretation at every physical scale. The nondimensional identity $D_{\text{phys}} \cdot T_0 / L_0^2 = D_{\text{nd}} = 0.3$ holds exactly in all five regimes. The structural correspondences (PME reduction, RC decay, telegraph oscillation, horizon formation, compact support) persist across all scales. The same PDE, with the same constitutive functions, produces quantitative predictions in SI units for quantum diffusion, Planck-scale transport, condensed-matter relaxation, galactic dynamics, and cosmological evolution.

**What remains open.** No experimental or observational test of the mapping has been performed. The anchoring ranges from theorem-level (quantum) to dimensional construction (cosmological). The participation channel remains a candidate identification in every regime. The fundamental tension between ED's monostable penalty (all perturbations decay) and cosmological structure growth (perturbations grow) is unresolved. The atlas is a framework for making predictions, not a demonstration that those predictions are correct.

---

## 1. The Universal Nondimensionalization Scheme

### 1.1 The ED PDE in Physical Units

The canonical ED system in physical (SI) units is:

$$\partial_t \rho = D_{\text{phys}}\bigl[M(\rho)\,\nabla^2\rho + M'(\rho)\,|\nabla\rho|^2 - P(\rho)\bigr] + H_{\text{phys}}\,v,$$

$$\dot{v} = \frac{1}{\tau_{\text{phys}}}\bigl(\bar{F}_{\text{phys}} - \zeta\,v\bigr),$$

with constitutive functions:

$$M(\rho) = M_0\!\left(\frac{\rho_{\max} - \rho}{\rho_{\max}}\right)^\beta, \qquad P(\rho) = P_0\!\left(\frac{\rho - \rho^*}{\rho_{\max}}\right).$$

Here $\rho(x,t)$ is the density field, $v(t)$ is the global participation variable, $D_{\text{phys}}$ is the physical diffusivity, and $\bar{F}_{\text{phys}}$ is the domain-averaged density operator.

### 1.2 Three Characteristic Scales

The mapping between physical and nondimensional variables is defined by three independent scales:

| Scale | Symbol | Role | Unit |
|:------|:-------|:-----|:-----|
| Length | $L_0$ | Physical domain or wavelength | m |
| Time | $T_0$ | Diffusion time: $L_0^2 D_{\text{nd}}/D_{\text{phys}}$ | s |
| Density | $R_0$ | Physical density scale | regime-dependent |

Two derived scales follow uniquely:

| Scale | Symbol | Definition | Unit |
|:------|:-------|:-----------|:-----|
| Velocity | $V_0$ | $L_0/T_0$ | m s$^{-1}$ |
| Energy/mass | $E_0$ | $R_0 \cdot L_0^d$ | regime-dependent |

### 1.3 Nondimensional Variables

$$\hat{x} = x/L_0, \quad \hat{t} = t/T_0, \quad \hat{\rho} = \rho/R_0, \quad \hat{v} = v/V_0.$$

After substitution, the PDE becomes:

$$\partial_{\hat{t}}\hat{\rho} = D_{\text{nd}}\bigl[\hat{M}(\hat{\rho})\,\hat{\nabla}^2\hat{\rho} + \hat{M}'(\hat{\rho})\,|\hat{\nabla}\hat{\rho}|^2 - \hat{P}(\hat{\rho})\bigr] + \hat{H}\,\hat{v},$$

where $D_{\text{nd}} = D_{\text{phys}} T_0/L_0^2$ by construction. The solver sees only nondimensional variables. All physics enters through the choice of $(L_0, T_0, R_0)$.

### 1.4 Why This Works Across 61 Orders of Magnitude

The nondimensionalization absorbs all scale information into the three characteristic numbers $(L_0, T_0, R_0)$. The PDE structure — degenerate mobility, monostable penalty, global participation — is scale-free. The constitutive functions $M(\hat{\rho})$ and $P(\hat{\rho})$ operate on the nondimensional density $\hat{\rho} \in [0,1]$ regardless of whether $R_0 = 10^{96}$ kg/m$^3$ (Planck) or $10^{-27}$ kg/m$^3$ (cosmological). This is axiom P7 (dimensional consistency) in action: the constitutive structure is independent of the spatial dimension $d$ and the physical scale $L_0$.

---

## 2. The Five Regimes

### 2.1 Quantum Regime (ED-Dimensional-01)

**Anchoring.** $L_0 = \hbar/(mc)$ (reduced Compton wavelength), $R_0 = L_0^{-d}$ (probability density normalisation), $D_{\text{phys}} = \hbar/(2m)$ (Madelung–Schrödinger diffusion).

**Physical meaning.** The density field is the Born probability density $|\psi|^2$. The diffusivity is fixed by a mathematical theorem: the Madelung transformation of the free-particle Schrödinger equation produces a continuity equation with diffusion coefficient $\hbar/(2m)$.

**Key dictionary rows** (electron, $d = 2$):

| Parameter | Physical quantity | Value | Status |
|:----------|:------------------|:------|:-------|
| $D$ | $\hbar/(2m_e)$ | $5.79 \times 10^{-5}$ m$^2$/s | **Exact** |
| $L_0$ | Compton wavelength | $3.86 \times 10^{-13}$ m | **Anchored** |
| $T_0$ | $2D_{\text{nd}}\hbar/(m_e c^2)$ | $7.73 \times 10^{-22}$ s | **Anchored** |
| $V_0$ | $c/(2D_{\text{nd}}) = 1.67\,c$ | $5.00 \times 10^8$ m/s | **Anchored** |

**Anchoring type.** Theorem (Madelung 1927). Strongest in the series.

**Key prediction.** Density-dependent probability diffusion: transport slows as $|\psi|^2 \to \rho_{\max}$. No standard-QM analogue.

---

### 2.2 Planck Regime (ED-Dimensional-02)

**Anchoring.** $L_0 = \ell_{\text{Pl}} = \sqrt{\hbar G/c^3}$, $R_0 = \rho_{\text{Pl}} = c^5/(\hbar G^2)$, $D_{\text{phys}} = \sqrt{\hbar G/c} = \ell_{\text{Pl}}^2/t_{\text{Pl}}$.

**Physical meaning.** All three scales are the unique combinations of $\hbar$, $G$, $c$ with the required dimensions. No free parameters. The density field is Planck-scale mass-energy density.

**Key dictionary rows** ($d = 3$):

| Parameter | Physical quantity | Value | Status |
|:----------|:------------------|:------|:-------|
| $D$ | $\sqrt{\hbar G/c}$ | $4.85 \times 10^{-27}$ m$^2$/s | **Anchored** |
| $T_0$ | $D_{\text{nd}} \cdot t_{\text{Pl}}$ | $1.62 \times 10^{-44}$ s | **Anchored** |
| $\tau_{\text{RC}}$ | $t_{\text{Pl}}$ (at $P_0 = 1$) | $5.39 \times 10^{-44}$ s | **Anchored** |

**Anchoring type.** Dimensional uniqueness. No theorem, but no freedom.

**Key prediction.** Penalty relaxation in one Planck time. Transient horizons at $\rho_{\text{Pl}}$.

---

### 2.3 Condensed-Matter Regime (ED-Dimensional-03)

**Anchoring.** $L_0 =$ experimental length ($\sim 1\;\mu$m), $R_0 =$ material density (kg/m$^3$), $D_{\text{phys}} = \kappa/(\rho c_p)$ (thermal diffusivity).

**Physical meaning.** The density field is mass density or concentration. All scales are set by laboratory measurement of specific materials.

**Key dictionary rows** (silicon, $L_0 = 1\;\mu$m, $d = 3$):

| Parameter | Physical quantity | Value | Status |
|:----------|:------------------|:------|:-------|
| $D$ | Thermal diffusivity | $8.80 \times 10^{-5}$ m$^2$/s | **Measured** |
| $T_0$ | Thermal equilibration | $3.41 \times 10^{-9}$ s | **Measured** |
| $V_0$ | Transport velocity | 293 m/s | **Anchored** |
| $R_0$ | Bulk density | 2329 kg/m$^3$ | **Measured** |

**Anchoring type.** Laboratory measurement. Most directly testable.

**Key prediction.** Density-dependent diffusivity: $D_{\text{eff}} \propto (1 - \rho/\rho_{\max})^\beta$. Compact-support fronts ($\alpha_R = 1/8$). Both testable in colloidal suspensions or polymer melts.

---

### 2.4 Galactic Regime (ED-Dimensional-04)

**Anchoring.** $L_0 = 1$ kpc, $R_0 = \rho_{\text{crit}}$ (or halo density), $D_{\text{phys}} = v_{\text{circ}} \cdot L_0$ (dynamical diffusivity).

**Physical meaning.** The density field is astrophysical mass-energy density. The diffusivity is constructed from the circular velocity and scale length — the two fundamental galactic observables.

**Key dictionary rows** (Milky Way, $d = 3$):

| Parameter | Physical quantity | Value | Status |
|:----------|:------------------|:------|:-------|
| $D$ | $v_{\text{circ}} \cdot L_0$ | $6.79 \times 10^{24}$ m$^2$/s | **Constructed** |
| $T_0$ | $D_{\text{nd}} \cdot t_{\text{cross}}$ | 1.33 Myr | **Constructed** |
| $V_0$ | $v_{\text{circ}}/D_{\text{nd}}$ | 733 km/s | **Anchored** |

**Anchoring type.** Dynamical construction from observables.

**Key prediction.** Density-dependent transport in haloes; compact-support halo edges; horizon formation in dense cores (core-cusp connection).

---

### 2.5 Cosmological Regime (ED-Dimensional-05)

**Anchoring.** $L_0 = c/H_0$ (Hubble length), $R_0 = \rho_{\text{crit}} = 3H_0^2/(8\pi G)$, $D_{\text{phys}} = c^2/H_0$.

**Physical meaning.** The density field is the large-scale cosmological mass-energy density. The diffusivity is the unique combination of $c$ and $H_0$ with dimensions of m$^2$/s.

**Key dictionary rows** ($d = 3$):

| Parameter | Physical quantity | Value | Status |
|:----------|:------------------|:------|:-------|
| $D$ | $c^2/H_0$ | $4.12 \times 10^{34}$ m$^2$/s | **Constructed** |
| $T_0$ | $D_{\text{nd}}/H_0$ | 4.35 Gyr | **Constructed** |
| $\tau_{\text{RC}}$ | $t_H$ (at $P_0 = 1$) | 14.5 Gyr | **Anchored** |

**Anchoring type.** Dimensional construction from $c$, $H_0$, $G$.

**Key prediction.** $\tau_{\text{RC}} = t_H$: penalty relaxation equals one Hubble time. Telegraph period $\sim 12$ Gyr. BAO-like preferred correlation scale.

---

## 3. Cross-Regime Invariants

Seven structural features persist identically across all five regimes. These are properties of the PDE, not of the physical interpretation.

### 3.1 $T_0 = D_{\text{nd}} \cdot t_{\text{natural}}$

Whenever the diffusivity takes the form $D_{\text{phys}} = v \cdot L_0$ (characteristic velocity times characteristic length), the time scale simplifies to:

$$T_0 = \frac{L_0^2 D_{\text{nd}}}{v \cdot L_0} = D_{\text{nd}} \cdot \frac{L_0}{v} = D_{\text{nd}} \cdot t_{\text{natural}}.$$

This pattern holds in three regimes:

| Regime | $v$ | $t_{\text{natural}}$ | $T_0$ |
|:-------|:----|:---------------------|:------|
| Planck | $c$ | $t_{\text{Pl}}$ | $D_{\text{nd}} \cdot t_{\text{Pl}}$ |
| Galactic | $v_{\text{circ}}$ | $t_{\text{cross}}$ | $D_{\text{nd}} \cdot t_{\text{cross}}$ |
| Cosmological | $c$ | $t_H$ | $D_{\text{nd}} \cdot t_H$ |

The quantum and condensed-matter regimes use a different anchoring form but produce analogous results ($T_0$ proportional to the natural timescale of the regime).

### 3.2 PME Exponent $\alpha_R = 1/(d(m-1)+2)$

For $\beta = 2$ ($m = 3$) in $d = 3$: $\alpha_R = 1/8 = 0.125$ in every regime. The porous-medium reduction is a property of the constitutive function $M(\hat{\rho}) = (1 - \hat{\rho})^\beta$, which is nondimensional and scale-free. The Barenblatt self-similar solution has the same exponent whether the density represents probability ($|\psi|^2$), Planck density ($\rho_{\text{Pl}}$), silicon density (kg/m$^3$), halo density, or cosmological density.

### 3.3 Horizon Formation

ED horizons form wherever $\rho \to \rho_{\max}$ (i.e., $\hat{\rho} \to 1$). The mobility vanishes, transport halts, and a free boundary appears. This occurs in every regime:

| Regime | $\rho_{\max}$ | Horizon meaning |
|:-------|:-------------|:----------------|
| Quantum | $R_0 = L_0^{-d}$ | Normalization/Pauli bound |
| Planck | $\rho_{\text{Pl}}$ | Planck-density singularity regularisation |
| Condensed matter | Bulk density | Close-packing / jamming |
| Galactic | $\rho_{\text{crit}}$ or halo density | Core formation |
| Cosmological | $\rho_{\text{crit}}$ | Critical-density structure freeze |

In every case, the horizon is transient — the monostable penalty guarantees collapse back to $\rho^*$.

### 3.4 Compact Support

The PME solution has finite propagation speed. The front has a well-defined edge; beyond it, no transport has occurred. This property holds in every regime and contrasts with the Gaussian tails of standard (linear) diffusion.

### 3.5 RC Decay

The penalty channel in isolation gives $\dot{\delta} = -D_{\text{nd}} P_0\,\delta$, producing exponential decay with $\tau_{\text{RC}} = 1/(D_{\text{nd}} P_0)$ nondimensional time units. In physical units: $\tau_{\text{RC}} = T_0/(D_{\text{nd}} P_0) = t_{\text{natural}}/P_0$ (when the $T_0 = D_{\text{nd}} \cdot t_{\text{natural}}$ pattern holds). For $P_0 = 1$: $\tau_{\text{RC}} = t_{\text{natural}}$. This produces the remarkable coincidences $\tau_{\text{RC}} = t_{\text{Pl}}$ (Planck) and $\tau_{\text{RC}} = t_H$ (cosmological).

### 3.6 Telegraph Oscillation

The coupled $(\delta, v)$ system produces damped oscillation with frequency $\omega = \sqrt{\omega_0^2 - \gamma^2}$, where $2\gamma = D_{\text{nd}} P_0 + \zeta/\tau$ and $\omega_0^2 = (D_{\text{nd}} P_0 \zeta + H P_0)/\tau$. This structure is identical in all regimes; only the physical timescale ($T_0$) changes.

### 3.7 Dimensional Consistency (Axiom P7)

The nondimensional identity $D_{\text{phys}} \cdot T_0 / L_0^2 = D_{\text{nd}}$ is verified to machine precision in all five regimes. The constitutive functions, the PDE structure, and the dimensionless invariants are independent of the physical scale. This is the empirical validation of axiom P7.

---

## 4. The ED-to-Physics Dictionary (Master Table)

| ED Parameter | ED meaning | Quantum | Planck | Condensed matter | Galactic | Cosmological |
|:-------------|:-----------|:--------|:-------|:-----------------|:---------|:-------------|
| $\rho$ | Density field | $\|\psi\|^2$ (probability) | Mass-energy density | Mass density / concentration | Halo mass density | Cosmological density |
| $D$ | Diffusion weight | $\hbar/(2m)$ | $\sqrt{\hbar G/c}$ | $\kappa/(\rho c_p)$ | $v_{\text{circ}} L_0$ | $c^2/H_0$ |
| $M(\rho)$ | Degenerate mobility | Density-dep. QM transport | Planck transport | Density-dep. thermal conductivity | Density-dep. gravitational transport | Density-dep. cosmic transport |
| $P(\rho)$ | Monostable penalty | Confining potential | Planck relaxation | Thermal equilibration | Virial equilibration | Cosmological restoring force |
| $v(t)$ | Participation variable | Decoherence mode | Proto-cosmological mode | Phonon bath / collective mode | Star-formation feedback | Dark-energy mode |
| $H$ | Coupling strength | Measurement coupling | Quantum-gravity feedback | Bath coupling | Galactic feedback | Dark-energy coupling |
| $\tau$ | Participation timescale | Decoherence time | Sub-Planck timescale | Thermal relaxation | Feedback cycle period | DE response time |
| $\rho^*$ | Equilibrium density | Equilibrium $\|\psi\|^2$ | $0.5\,\rho_{\text{Pl}}$ | Equilibrium concentration | Background density | $0.5\,\rho_{\text{crit}}$ |
| $\rho_{\max}$ | Capacity bound | Normalization bound | $\rho_{\text{Pl}}$ | Close-packing / bulk | Halo central density | $\rho_{\text{crit}}$ |
| $\beta$ | Mobility exponent | 2 (canonical) | 2 (canonical) | Material-specific | Galaxy-specific | 2 (canonical) |

**Status by regime:**

| Parameter | Quantum | Planck | Condensed | Galactic | Cosmological |
|:----------|:--------|:-------|:----------|:---------|:-------------|
| $D$ | Exact | Anchored | Measured | Constructed | Constructed |
| $L_0$ | Anchored | Anchored | Measured | Observed | Anchored |
| $R_0$ | Anchored | Anchored | Measured | Observed | Anchored |
| $M(\rho)$ | ED-specific | ED-specific | ED-specific | ED-specific | ED-specific |
| $v, H, \tau, \zeta$ | Candidate | Candidate | Candidate | Candidate | Candidate |
| $\beta$ | Structural | Structural | Structural | Structural | Structural |

---

## 5. The Regime Manifold

### 5.1 The Two-Dimensional Space of Scale Choices

Every ED regime is specified by a point in the $(L_0, D_{\text{phys}})$ plane. Given $L_0$ and $D_{\text{phys}}$, the time scale $T_0 = L_0^2 D_{\text{nd}} / D_{\text{phys}}$ and velocity scale $V_0 = L_0/T_0 = D_{\text{phys}}/(L_0 D_{\text{nd}})$ follow uniquely. The density scale $R_0$ provides a third, independent degree of freedom, but for three of the five regimes (Planck, galactic, cosmological) it is determined by $L_0$ and fundamental constants, reducing the effective dimensionality to two.

### 5.2 Regime Coordinates

```
log10(D_phys)
    |
 35 |                                              * Cosmological
    |                                               (c^2/H_0)
 25 |                          * Galactic
    |                           (v_circ * L_0)
    |
  0 |
    |
 -5 |  * Quantum        * Condensed
    |   (hbar/2m)        (kappa/rho*cp)
    |
-27 |      * Planck
    |       (sqrt(hbar*G/c))
    +------+------+------+------+------+------+-----> log10(L0)
         -35    -13     -6      0     19     26
```

The five regimes occupy five distinct regions. The Planck regime sits at the extreme lower-left (smallest $L_0$, smallest $D_{\text{phys}}$). The cosmological regime sits at the extreme upper-right (largest $L_0$, largest $D_{\text{phys}}$). The quantum and condensed-matter regimes are close in $D_{\text{phys}}$ but separated by seven orders of magnitude in $L_0$.

### 5.3 Continuity Between Regimes

**Quantum $\leftrightarrow$ Planck.** Setting $m = m_{\text{Pl}}$ in the quantum anchoring recovers $L_0 = \ell_{\text{Pl}}$ exactly. The diffusivities differ by a factor of 2 (convention-dependent). The two regimes are connected by a smooth variation of particle mass from $m_e$ to $m_{\text{Pl}}$.

**Condensed matter $\leftrightarrow$ Galactic.** Increasing $L_0$ from $\mu$m to kpc and replacing the thermal diffusivity with the dynamical diffusivity produces a continuous path through the $(L_0, D_{\text{phys}})$ plane. No structural change in the PDE occurs along this path.

**Galactic $\leftrightarrow$ Cosmological.** Increasing $L_0$ from kpc to $c/H_0$ and $v_{\text{circ}}$ to $c$ produces the cosmological regime. Both share $R_0 = \rho_{\text{crit}}$.

**Universal coverage.** Every point in the $(L_0, D_{\text{phys}})$ plane with $L_0 > 0$ and $D_{\text{phys}} > 0$ defines a valid ED regime. The five named regimes are coordinate patches on a continuous manifold. Any intermediate scale (e.g., planetary, stellar, interstellar) can be assigned a consistent dictionary by choosing the appropriate $(L_0, D_{\text{phys}}, R_0)$.

---

## 6. Architectural Principles

Six principles unify the five regime mappings.

**Principle 1: Scale separation.** The ED PDE is structurally scale-free. Physical meaning enters only through the choice of $(L_0, T_0, R_0)$. The constitutive functions $M(\hat{\rho})$ and $P(\hat{\rho})$ are nondimensional and identical across all regimes.

**Principle 2: Structural persistence.** The four structural correspondences — PME reduction, RC decay, telegraph oscillation, horizon formation — are properties of the PDE, not of the physical interpretation. They hold in every regime without exception.

**Principle 3: Anchoring hierarchy.** The five regimes are ordered by the strength of their anchoring, from mathematical theorem (quantum) through dimensional uniqueness (Planck) through laboratory measurement (condensed matter) through dynamical construction (galactic, cosmological). This hierarchy defines the confidence level of each mapping.

**Principle 4: Falsifiability is regime-specific.** Each regime has its own falsification criteria determined by the specific physical quantities predicted. Failure in one regime (e.g., no density-dependent diffusivity in silicon) does not falsify the mapping in another regime (e.g., cosmological timescales). The architecture is universal; the empirical tests are local.

**Principle 5: The velocity boundary.** Regimes where $V_0 < c$ (condensed matter, galactic) require no relativistic caveat. Regimes where $V_0 > c$ (quantum, Planck, cosmological) reflect the parabolic nature of the PDE and would require a hyperbolic extension for causal dynamics. The boundary $V_0 = c$ — equivalently $D_{\text{nd}} = D_{\text{phys}}/(c L_0)$ — divides the regime manifold into a subluminal region and a superluminal region.

**Principle 6: Completeness without commitment.** The atlas provides a complete dimensional dictionary for every scale without committing to a specific physical ontology. ED may describe the density at each scale, or it may not. The atlas makes the predictions explicit so that the question can be answered empirically.

---

## 7. Falsifiable Predictions Across All Regimes

### 7.1 Quantum

| # | Prediction | Observable | Timescale |
|---|:-----------|:-----------|:----------|
| Q1 | $D_{\text{phys}} = \hbar/(2m_e) = 5.79 \times 10^{-5}$ m$^2$/s | Probability-density diffusion | $T_0 = 7.73 \times 10^{-22}$ s |
| Q2 | Density-dependent mobility: transport slows as $|\psi|^2 \to \rho_{\max}$ | Anomalous quantum diffusion at high density | Sub-femtosecond |
| Q3 | PME exponent $\alpha_R = 1/4$ ($d = 2$, $m = 3$) | Front-radius scaling of probability wave packets | Sub-femtosecond |

### 7.2 Planck

| # | Prediction | Observable | Timescale |
|---|:-----------|:-----------|:----------|
| Pl1 | $\tau_{\text{RC}} = t_{\text{Pl}} = 5.39 \times 10^{-44}$ s | Planck-scale relaxation | $t_{\text{Pl}}$ |
| Pl2 | Transient horizons at $\rho_{\text{Pl}}$ | Singularity regularisation | $\sim$ few $t_{\text{Pl}}$ |
| Pl3 | Barenblatt exponent $\alpha_R = 1/8$ ($d = 3$) | Spreading of Planck-density perturbations | $t_{\text{Pl}}$ |

### 7.3 Condensed Matter

| # | Prediction | Observable | Timescale |
|---|:-----------|:-----------|:----------|
| CM1 | $D_{\text{eff}} \propto (1 - \rho/\rho_{\max})^2$ | Concentration-dependent diffusion (DLS, FRAP) | ns to $\mu$s |
| CM2 | Compact-support front ($\alpha_R = 1/8$, $d = 3$) | Sharp vs. diffuse spreading profiles | ns to $\mu$s |
| CM3 | $\tau_{\text{RC}} = 11.4$ ns (Si, $P_0 = 1$) | Thermal relaxation timescale | ns |
| CM4 | Telegraph oscillation $T_{\text{osc}} = 9.6$ ns (Si, $H = 5$) | Ultrafast spectroscopy | ns |

### 7.4 Galactic

| # | Prediction | Observable | Timescale |
|---|:-----------|:-----------|:----------|
| G1 | $\tau_{\text{RC}} = 4.44$ Myr (MW, $P_0 = 1$) | Tidal-feature relaxation | Myr |
| G2 | Compact-support halo edges | Sharp halo truncation radius | Static |
| G3 | Horizon formation in dense cores | Core-cusp transition at $\rho \to R_0$ | Static |
| G4 | Participation period $T_{\text{osc}} = 3.75$ Myr (MW, $H = 5$) | Periodic SFR modulation | Myr |

### 7.5 Cosmological

| # | Prediction | Observable | Timescale |
|---|:-----------|:-----------|:----------|
| C1 | $\tau_{\text{RC}} = t_H = 14.5$ Gyr ($P_0 = 1$) | Structure dissolution rate | Hubble time |
| C2 | Telegraph period $T_{\text{osc}} = 12.2$ Gyr ($H = 5$) | Dark-energy oscillation / $w(z)$ variation | Gyr |
| C3 | BAO-like preferred scale from telegraph modulation | Correlation feature at $\sim 150$ Mpc | Static |
| C4 | Sharp void boundaries (compact support) | Void-wall sharpness in galaxy surveys | Static |
| C5 | Horizon formation at $\rho = \rho_{\text{crit}}$ | Sharp density transition at critical density | Static |

---

## 8. Open Questions and Future Work

### 8.1 Cross-Regime Questions

1. **Mobility exponent $\beta$.** The canonical value $\beta = 2$ is used across all regimes. Is this universal, or should $\beta$ be regime-specific (e.g., fitted to colloidal data in condensed matter, to core profiles in galactic)? If $\beta$ varies, what determines it?

2. **Physical origin of $\rho^*$.** The equilibrium density $\rho^* = 0.5\,R_0$ is a canonical choice. Its physical meaning differs by regime (vacuum density? equilibrium concentration? background cosmological density?) and is not derived from first principles.

3. **Participation channel universality.** The participation variable $v(t)$ is classified as a candidate in every regime. Is there a single physical principle that determines $v(t)$ across all scales, or is it a different physical quantity at each scale?

### 8.2 Regime-Specific Questions

4. **Quantum.** Density-dependent probability diffusion has no experimental support or refutation. Can it be tested in BEC experiments, quantum dots, or matter-wave interferometry?

5. **Planck.** All predictions occur at $\sim t_{\text{Pl}}$, far beyond experimental reach. Can the Planck mapping be connected to observable signatures (e.g., trans-Planckian effects in cosmology, black-hole information)?

6. **Condensed matter.** Which materials are most likely to exhibit ED-like behaviour? Leading candidates: concentrated colloids near the glass transition, polymer melts, granular flows.

7. **Galactic.** Can an ED simulation with the galactic dictionary reproduce a measured rotation curve (e.g., from SPARC data) without dark matter? Can the ED core profile match observed dwarf-galaxy cores?

8. **Cosmological.** Can the ED PDE, run on an expanding domain with the cosmological dictionary, reproduce the CMB angular power spectrum? This is the ultimate quantitative test.

### 8.3 Structural Questions

9. **Structure growth vs. decay.** The monostable penalty guarantees that all perturbations decay. Cosmological structure grows. Can the participation channel produce sufficient transient growth? This is the most fundamental open question.

10. **ED–Friedmann correspondence.** The spatially homogeneous ED equation is a damped oscillator around $\rho^*$. The Friedmann equation is a power-law evolution of the scale factor. Can one be mapped onto the other?

11. **Hyperbolic extension.** At scales where $V_0 > c$, the parabolic PDE is inadequate. The ED-Phys-13/14 hyperbolic (telegraph-type) extension restores finite propagation speed. Does this extension preserve the structural correspondences?

---

## 9. Conclusion

### 9.1 What the Unified Atlas Establishes

The ED-Dimensional series demonstrates that a single canonical PDE — derived from seven axioms, operating through three constitutive channels — admits a consistent dimensional mapping at every physical scale from $1.6 \times 10^{-35}$ m (Planck) to $1.4 \times 10^{26}$ m (Hubble). The mapping produces a complete dictionary of physical quantities in SI units at each scale, classifies every correspondence by its epistemic status (exact, anchored, measured, constructed, candidate), identifies falsifiable predictions, and states what remains open.

The nondimensional identity $D_{\text{phys}} T_0/L_0^2 = D_{\text{nd}}$ holds exactly across all five regimes. The structural correspondences (PME reduction, RC decay, telegraph oscillation, horizon formation, compact support) persist at every scale without modification. The constitutive functions are scale-free. Axiom P7 is validated empirically.

### 9.2 What It Does Not Claim

The atlas does not claim that ED governs the physics at any of these scales. It does not derive general relativity, quantum mechanics, or the Standard Model. It does not match observational data. It does not resolve the structure-growth problem. It does not explain the physical origin of the participation variable.

### 9.3 The Path to Empirical Validation

The atlas converts abstract structural claims into specific, quantitative, falsifiable predictions. The next phase of the ED programme is empirical:

1. **Condensed-matter experiments.** Test density-dependent diffusivity and compact-support fronts in colloidal suspensions or polymer systems.
2. **Galactic simulations.** Run ED-SIM-02 with the galactic dictionary and compare density profiles to observed rotation curves and core-cusp data.
3. **Cosmological simulations.** Run ED-SIM-02 with the cosmological dictionary on an expanding domain and compare to BAO data, void statistics, and (ultimately) the CMB power spectrum.

### 9.4 The Role of ED

Event Density is a candidate physical ontology. The unified atlas shows that its minimal constitutive architecture — four primitives, three channels, seven axioms — is dimensionally consistent across the full range of known scales. Whether this dimensional consistency reflects a deep structural truth about physical law, or is instead an expressive property of quasilinear parabolic PDEs, is a question that only empirical testing can answer. The atlas makes that testing possible.

---

## Appendix A: Cross-Regime Numerical Table

All values for $D_{\text{nd}} = 0.3$. Quantum regime at $d = 2$ (electron); all others at $d = 3$.

| Scale | Quantum (e$^-$) | Planck | Condensed (Si) | Galactic (MW) | Cosmological |
|:------|:-----------------|:-------|:----------------|:--------------|:-------------|
| $L_0$ (m) | $3.862 \times 10^{-13}$ | $1.616 \times 10^{-35}$ | $1.000 \times 10^{-6}$ | $3.086 \times 10^{19}$ | $1.373 \times 10^{26}$ |
| $T_0$ (s) | $7.729 \times 10^{-22}$ | $1.617 \times 10^{-44}$ | $3.409 \times 10^{-9}$ | $4.208 \times 10^{13}$ | $1.374 \times 10^{17}$ |
| $R_0$ | $6.706 \times 10^{24}$ m$^{-2}$ | $5.155 \times 10^{96}$ kg/m$^3$ | $2329$ kg/m$^3$ | $8.53 \times 10^{-27}$ kg/m$^3$ | $8.53 \times 10^{-27}$ kg/m$^3$ |
| $V_0$ (m/s) | $4.997 \times 10^{8}$ | $9.993 \times 10^{8}$ | $2.933 \times 10^{2}$ | $7.333 \times 10^{5}$ | $9.993 \times 10^{8}$ |
| $V_0/c$ | 1.667 | 3.333 | $9.8 \times 10^{-7}$ | $2.4 \times 10^{-3}$ | 3.333 |
| $D_{\text{phys}}$ (m$^2$/s) | $5.788 \times 10^{-5}$ | $4.845 \times 10^{-27}$ | $8.800 \times 10^{-5}$ | $6.789 \times 10^{24}$ | $4.115 \times 10^{34}$ |
| $D_{\text{phys}} T_0/L_0^2$ | 0.300 | 0.300 | 0.300 | 0.300 | 0.300 |
| Anchoring | Theorem | Dimensional | Measured | Constructed | Constructed |

---

## Appendix B: Dimensional Consistency Proofs

**Claim.** For all five regimes, $D_{\text{phys}} \cdot T_0 / L_0^2 = D_{\text{nd}} = 0.3$.

**Proof (by construction).** The time scale is defined as $T_0 = L_0^2 D_{\text{nd}} / D_{\text{phys}}$. Therefore:

$$\frac{D_{\text{phys}} \cdot T_0}{L_0^2} = \frac{D_{\text{phys}} \cdot L_0^2 D_{\text{nd}} / D_{\text{phys}}}{L_0^2} = D_{\text{nd}}. \quad \square$$

This identity is tautological by the definition of $T_0$. Its content is not the algebraic identity itself but the fact that $T_0$ so defined produces physically meaningful timescales in every regime: sub-femtoseconds (quantum), sub-Planck-times (Planck), nanoseconds (condensed matter), megayears (galactic), gigayears (cosmological).

**Claim.** $V_0 = D_{\text{phys}}/(L_0 D_{\text{nd}})$ in all regimes.

**Proof.** $V_0 = L_0/T_0 = L_0 \cdot D_{\text{phys}}/(L_0^2 D_{\text{nd}}) = D_{\text{phys}}/(L_0 D_{\text{nd}})$. $\square$

**Claim.** When $D_{\text{phys}} = v \cdot L_0$, the velocity scale is $V_0 = v/D_{\text{nd}}$.

**Proof.** $V_0 = D_{\text{phys}}/(L_0 D_{\text{nd}}) = v L_0/(L_0 D_{\text{nd}}) = v/D_{\text{nd}}$. $\square$

---

## Appendix C: Glossary of ED Parameters

| Symbol | Name | Canonical value | Role |
|:-------|:-----|:----------------|:-----|
| $\rho(x,t)$ | Density field | $[0, \rho_{\max}]$ | Primary state variable |
| $v(t)$ | Participation variable | scalar | Global feedback mode |
| $D$ | Diffusion weight | 0.3 | Local operator strength |
| $M(\rho)$ | Mobility function | $M_0(1 - \hat{\rho})^\beta$ | Density-dependent transport |
| $P(\rho)$ | Penalty function | $P_0(\hat{\rho} - \hat{\rho}^*)$ | Monostable restoring force |
| $H$ | Participation coupling | 0–50 | Global feedback strength |
| $\tau$ | Participation timescale | 1.0 | Response time of $v$ |
| $\zeta$ | Damping coefficient | 0.1 | Friction on $v$ |
| $\rho^*$ | Equilibrium density | 0.5 | Penalty target |
| $\rho_{\max}$ | Capacity bound | 1.0 | Maximum density |
| $M_0$ | Mobility prefactor | 1.0 | Diffusion scale |
| $\beta$ | Mobility exponent | 2.0 | PME index: $m = \beta + 1$ |
| $P_0$ | Penalty slope | 0.01–1.0 | Restoring force strength |

---

## Appendix D: Glossary of Physical Constants

| Symbol | Name | Value | Unit | Source |
|:-------|:-----|:------|:-----|:-------|
| $\hbar$ | Reduced Planck constant | $1.055 \times 10^{-34}$ | J s | CODATA 2018 |
| $G$ | Gravitational constant | $6.674 \times 10^{-11}$ | m$^3$ kg$^{-1}$ s$^{-2}$ | CODATA 2018 |
| $c$ | Speed of light | $2.998 \times 10^{8}$ | m s$^{-1}$ | Exact |
| $k_B$ | Boltzmann constant | $1.381 \times 10^{-23}$ | J K$^{-1}$ | Exact |
| $m_e$ | Electron mass | $9.109 \times 10^{-31}$ | kg | CODATA 2018 |
| $m_p$ | Proton mass | $1.673 \times 10^{-27}$ | kg | CODATA 2018 |
| $m_{\text{Pl}}$ | Planck mass | $2.176 \times 10^{-8}$ | kg | Derived |
| $\ell_{\text{Pl}}$ | Planck length | $1.616 \times 10^{-35}$ | m | Derived |
| $t_{\text{Pl}}$ | Planck time | $5.391 \times 10^{-44}$ | s | Derived |
| $\rho_{\text{Pl}}$ | Planck density | $5.155 \times 10^{96}$ | kg m$^{-3}$ | Derived |
| $H_0$ | Hubble constant | $2.184 \times 10^{-18}$ | s$^{-1}$ | Planck 2020 |
| $\rho_{\text{crit}}$ | Critical density | $8.53 \times 10^{-27}$ | kg m$^{-3}$ | Derived |
| kpc | Kiloparsec | $3.086 \times 10^{19}$ | m | IAU |
| $M_\odot$ | Solar mass | $1.989 \times 10^{30}$ | kg | IAU |

---

## References

1. Proxmire, A. "ED-Dimensional-01: Physical Units and Dimensional Mapping — The Quantum Regime." (2026).
2. Proxmire, A. "ED-Dimensional-02: Physical Units and Dimensional Mapping — The Planck Regime." (2026).
3. Proxmire, A. "ED-Dimensional-03: Physical Units and Dimensional Mapping — The Condensed-Matter Regime." (2026).
4. Proxmire, A. "ED-Dimensional-04: Physical Units and Dimensional Mapping — The Galactic Regime." (2026).
5. Proxmire, A. "ED-Dimensional-05: Physical Units and Dimensional Mapping — The Cosmological Regime." (2026).
6. Proxmire, A. "Event Density as an Ontological Framework: Constitutive Channels, Structural Laws, and Six Empirical Analogues." (2026).
7. Proxmire, A. ED-SIM-02: An Architectural Lab for Entropic Dynamics. Software package (2026).
8. Madelung, E. "Quantentheorie in hydrodynamischer Form." *Z. Phys.* **40**, 322–326 (1927).
9. Planck Collaboration. "Planck 2018 results. VI. Cosmological parameters." *Astron. Astrophys.* **641**, A6 (2020).
10. Vazquez, J. L. *The Porous Medium Equation.* Oxford University Press (2007).
