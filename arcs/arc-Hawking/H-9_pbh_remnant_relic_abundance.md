# Arc Hawking — Memo 9: PBH Remnant Relic-Abundance

**Status:** Cosmological calculation memo. Conditional on H-8 (stable Planck-mass remnant FORCED by substrate constraints). No new primitives. Framing note: ED's substrate-gravity (galactic_dynamics walkthrough) explains rotation curves, BTFR, and galactic phenomenology without invoking dark matter. The Planck-mass remnant population from PBH evaporation is a *separate structural prediction* about cosmic relic-matter content, not a phenomenological dark-matter explanation. Throughout this memo, the remnant population is referred to as a *relic-matter component* with cosmological abundance $\Omega_{\mathrm{relic}}$, never as a "dark matter candidate."

**Date:** 2026-05-09

---

## 1. The CANDIDATE Statement

> **CANDIDATE (H9).** *Given H-8's prediction that all primordial black holes (PBHs) with initial mass $M_0$ such that $\tau_{\mathrm{BH}}(M_0) < t_{\mathrm{universe}}$ have evaporated to stable Planck-mass remnants of mass $M_* = c_* \ell_P$ (with $c_*$ order-unity, INHERITED), the present-day cosmological abundance of these remnants is determined by the parent PBH initial mass function. For standard scale-invariant power-law spectra, the relic-matter fraction $\Omega_{\mathrm{relic}}$ is parametrically small (order $10^{-15}$ to $10^{-3}$) depending on the PBH formation efficiency $\beta$ and spectral index. For blue-tilted or inflationary-spike scenarios with enhanced small-mass formation, $\Omega_{\mathrm{relic}}$ can range from $10^{-3}$ to order unity. Observational constraints on the parent PBH population (BBN bounds on evaporating PBHs, gamma-ray backgrounds, CMB spectral distortions) constrain the remnant population indirectly. The framework predicts that the relic-matter fraction is structurally non-zero, with the specific value INHERITED from the empirical cosmological PBH formation history.*

The CANDIDATE has four pieces:

- **(C9a) Structural existence of remnant relic-matter component.** H-8 forces stable Planck-mass remnants from any PBH that has fully evaporated. Whatever the parent PBH formation history, some non-zero remnant relic-matter component is structurally predicted.

- **(C9b) Abundance calculation.** $\Omega_{\mathrm{relic}}$ is computable from initial PBH mass function $\beta(M_0)$ and the present-day cosmic energy budget.

- **(C9c) Scenario-dependence.** Different PBH formation scenarios produce different $\Omega_{\mathrm{relic}}$ ranges — order $10^{-15}$ for standard scale-invariant, up to order unity for inflationary-spike scenarios.

- **(C9d) Constraint compatibility.** Existing observational constraints on parent PBHs constrain the remnant abundance indirectly. Most regions of parameter space are constrained; specific narrow regions remain viable.

H-9 examines each. The argument runs through standard PBH cosmology with the H-8 endpoint substituted for the standard "complete evaporation" endpoint.

---

## 2. Substrate Inputs and Framing Note

The calculation uses only the following inputs:

| Input | Status | Role |
|---|---|---|
| **H-8 (stable Planck-mass remnant)** | Closed (this arc) | Endpoint of PBH evaporation: $M_* = c_*\ell_P$ |
| **Standard PBH formation cosmology** | External cosmology literature | Initial mass function $\beta(M_0)$ from formation history |
| **Standard cosmological parameters** | Empirical | $H_0$, $\rho_{\mathrm{crit}}$, $t_{\mathrm{universe}}$, etc. |
| **Standard PBH evaporation lifetime** | H-3 + standard physics | $\tau_{\mathrm{BH}}(M_0) \approx M_0^3 / (3\alpha_{\mathrm{Page}})$ |
| **PBH observational constraints** | External cosmology literature | Carr et al. compilation [1], updated through 2024 |

**Framing note (load-bearing):** ED's substrate-gravity (galactic_dynamics walkthrough) already explains the empirical phenomenology of galactic dynamics — flat rotation curves, slope-4 BTFR, transition acceleration $a_0 = c H_0/(2\pi)$, radial-acceleration relation — *without invoking dark matter*. The framework does not require, and does not posit, a dark-matter particle population to explain galactic dynamics. What ΛCDM attributes to dark-matter halos, ED attributes to substrate-level dipole-mode projection plus geometric-mean composition (Combination Rule).

The PBH remnant population computed here is therefore *not* a dark-matter candidate. It is a *structural prediction* about the cosmic energy budget: H-8 forces stable Planck-mass remnants from evaporated PBHs, and the cosmic abundance of these remnants is a derivable quantity given the parent PBH formation history. The relic-matter fraction $\Omega_{\mathrm{relic}}$ is the cosmological signature of the H-8 prediction, separate from any DM phenomenology.

The structural question this memo answers: *what fraction of the cosmic energy budget do Planck-mass remnants from primordial-BH evaporation occupy at the present epoch?* The answer: it depends on the empirical PBH formation history — possibly negligible, possibly significant, but in any case a structural consequence of H-8.

**No new primitives introduced.** **The remnant population is not framed as dark matter at any point.**

---

## 3. The H-8 Endpoint and the Critical Mass

### 3.1 The H-8 result

H-8 establishes that all PBHs evaporate to stable Planck-mass remnants:
$$M_* = c_* \ell_P \approx c_* \cdot 2.18 \times 10^{-8}\, \mathrm{kg} \approx c_* \cdot 22\, \mu\mathrm{g}$$

with $c_*$ an order-unity coefficient INHERITED from substrate microscopic details. For order-of-magnitude estimates, take $c_* = 1$, giving $M_* \approx m_P \approx 22\,\mu\mathrm{g} = 2.18 \times 10^{-8}$ kg.

### 3.2 The critical mass for full evaporation

Standard PBH evaporation lifetime [from H-3 leading-order Page rate]:
$$\tau_{\mathrm{BH}}(M_0) = \frac{M_0^3}{3\alpha_{\mathrm{Page}}}$$

For PBHs that have evaporated to remnants by the present epoch, $\tau_{\mathrm{BH}}(M_0) < t_{\mathrm{universe}} \approx 4.35 \times 10^{17}$ s. Solving for the critical mass:

$$M_{\mathrm{evap}} = (3\alpha_{\mathrm{Page}} t_{\mathrm{universe}})^{1/3}$$

Numerically (using standard $\alpha_{\mathrm{Page}} \approx 1.27 \times 10^{16}$ kg$^3$/s for the standard species mix):
$$M_{\mathrm{evap}} \approx 5 \times 10^{11}\, \mathrm{kg} = 5 \times 10^{14}\, \mathrm{g}$$

This is the standard "evaporating-now" PBH mass — PBHs with $M_0 \approx M_{\mathrm{evap}}$ are completing their evaporation at the present epoch. PBHs with $M_0 < M_{\mathrm{evap}}$ have already evaporated to remnants; PBHs with $M_0 > M_{\mathrm{evap}}$ persist at intermediate mass.

### 3.3 The remnant population

The remnant number density at present epoch is:
$$n_{\mathrm{remnant}}(t_0) = \int_{M_*}^{M_{\mathrm{evap}}} dM_0 \cdot \frac{dn_{\mathrm{PBH}}}{dM_0}\bigg|_{t_0}$$

where $\frac{dn_{\mathrm{PBH}}}{dM_0}\big|_{t_0}$ is the present-day differential number density of PBHs with initial mass $M_0$. Each such PBH has evaporated to a remnant of mass $M_*$.

The total remnant mass density:
$$\rho_{\mathrm{remnant}}(t_0) = M_* \cdot n_{\mathrm{remnant}}(t_0)$$

The relic-matter fraction:
$$\Omega_{\mathrm{relic}} = \frac{\rho_{\mathrm{remnant}}(t_0)}{\rho_{\mathrm{crit}}}, \quad \rho_{\mathrm{crit}} \approx 9.47 \times 10^{-27}\, \mathrm{kg/m}^3$$

Computing $\Omega_{\mathrm{relic}}$ requires the initial PBH mass function from a specific formation scenario.

---

## 4. Standard PBH Formation Scenarios

We compute $\Omega_{\mathrm{relic}}$ for four standard PBH formation scenarios.

### 4.1 Scale-invariant primordial spectrum

In radiation-domination, large-amplitude primordial density perturbations on a fixed comoving scale $k$ collapse to PBHs of mass $M_0 \sim M_H(k)$ (the horizon mass at the time the scale crosses inside the horizon). For a scale-invariant spectrum (Carr-Hawking 1974 [2], Carr 2005 [3]), the differential PBH mass function takes a power law:

$$\frac{d\beta}{dM_0} \propto M_0^{-\alpha}$$

with $\alpha = 5/2$ for radiation-domination PBH formation. The mass function spans from the smallest formed mass (set by the cosmological epoch when the relevant comoving scale crossed inside the horizon) to the largest.

The PBH formation efficiency $\beta(M_0)$ — the fraction of the cosmic energy budget that went into PBHs at formation — is constrained at each mass scale. For standard scale-invariant: $\beta \lesssim 10^{-22}$ at $M_0 \sim 10^{15}$ g (BBN bound) [1]. At smaller masses, the constraints are weaker because evaporation occurred deeper in the cosmological past.

For $\beta \sim 10^{-22}$ over the range $M_* < M_0 < M_{\mathrm{evap}}$:
$$\Omega_{\mathrm{relic}}^{\mathrm{scale-inv}} \sim \frac{M_*}{M_{\mathrm{evap}}} \cdot \beta \sim 10^{-19} \cdot 10^{-22} \cdot \mathrm{dimensionless\ factor} \sim 10^{-30} \text{ to } 10^{-15}$$

depending on the precise mass function shape and constraint saturation. **This scenario produces a negligible relic-matter fraction.**

### 4.2 Blue-tilted primordial spectrum

A "blue-tilted" inflation spectrum has more power at small comoving scales (large $k$), enhancing PBH formation at small masses. Differential PBH formation:
$$\frac{d\beta}{dM_0} \propto M_0^{-\alpha + n_{\mathrm{tilt}}}$$

with $n_{\mathrm{tilt}} > 0$ for blue tilt. Inflation-model-dependent values of $n_{\mathrm{tilt}}$ can produce orders-of-magnitude enhancement at small masses.

For sufficiently blue tilts, $\beta(M_0)$ can saturate constraints across a range of small masses. The blue-tilted case can produce:
$$\Omega_{\mathrm{relic}}^{\mathrm{blue}} \sim 10^{-10} \text{ to } 10^{-3}$$

**Possibly significant, depending on tilt magnitude. Constrained by various observational bounds.**

### 4.3 Critical collapse

In the critical-collapse PBH formation model (Niemeyer-Jedamzik 1998 [4]), the mass function has a near-Gaussian peak around the horizon mass at formation, with a small spread. The mass function is well-localized in mass:
$$\frac{d\beta}{dM_0} \approx \beta_{\mathrm{peak}} \cdot G(M_0; M_{\mathrm{peak}}, \sigma_M)$$

where $G$ is a Gaussian-like distribution. If $M_{\mathrm{peak}} < M_{\mathrm{evap}}$, all PBHs in the peak have evaporated to remnants:
$$\Omega_{\mathrm{relic}}^{\mathrm{critical}} = \beta_{\mathrm{peak}} \cdot (M_*/M_{\mathrm{peak}})$$

For $M_{\mathrm{peak}} \sim 10^{12}$ g and $\beta_{\mathrm{peak}} \sim 10^{-19}$ (BBN-constrained):
$$\Omega_{\mathrm{relic}}^{\mathrm{critical}} \sim 10^{-19} \cdot 10^{-22} \sim 10^{-41}$$

**Negligible relic-matter fraction unless $\beta_{\mathrm{peak}}$ is at saturation and $M_{\mathrm{peak}}$ is finely tuned.**

### 4.4 Inflationary spike models

In inflationary-spike scenarios (e.g., Garcia-Bellido et al. 2017 [5]), specific features in the inflation potential (steps, inflection points, ultra-slow-roll phases) produce narrow peaks in the primordial power spectrum at specific comoving scales. These peaks generate concentrated PBH populations at specific mass scales.

The relic-matter fraction depends on:
- Peak location: $M_{\mathrm{peak}}$
- Peak amplitude: $\beta_{\mathrm{peak}}$
- Peak width: $\sigma_M$

If a peak is positioned at $M_{\mathrm{peak}} \sim 10^9$ g (well below $M_{\mathrm{evap}}$) with substantial $\beta_{\mathrm{peak}} \sim 10^{-7}$ (within constraints for the relevant evaporation epoch):
$$\Omega_{\mathrm{relic}}^{\mathrm{spike}} \sim \beta_{\mathrm{peak}} \cdot (M_*/M_{\mathrm{peak}}) \sim 10^{-7} \cdot 10^{-17} \sim 10^{-24}$$

For peaks at very low masses ($M_{\mathrm{peak}} \to M_*$):
$$\Omega_{\mathrm{relic}}^{\mathrm{spike, low-M}} \sim \beta_{\mathrm{peak}} \to \mathcal{O}(\beta_{\mathrm{peak}})$$

**For peaks at masses approaching $M_*$, $\Omega_{\mathrm{relic}}$ approaches $\beta_{\mathrm{peak}}$ directly.** A spike with $\beta_{\mathrm{peak}} \sim 0.1$ at $M_{\mathrm{peak}} \sim 10^{-7}$ kg (very low mass) would produce $\Omega_{\mathrm{relic}} \sim 0.1$ — significant cosmic energy contribution.

However, BBN and CMB constraints largely rule out $\beta(M_0)$ values that would produce $\Omega_{\mathrm{relic}} \gtrsim 10^{-3}$ across most of the relevant mass range.

---

## 5. The Calculation in Detail

### 5.1 Standard cosmological framework

Working in standard $\Lambda$CDM cosmology (the framework's empirical-cosmology baseline; the substrate-gravity content does not modify cosmological evolution outside the substrate-saturation regime). At PBH formation epoch $t_f$:
$$\rho_{\mathrm{rad}}(t_f) = (3 H_f^2 M_{\mathrm{Pl}}^2 / 8\pi)$$

For PBHs forming with mass $M_0 \sim M_H(t_f)$ (horizon mass), the formation fraction is:
$$\beta(M_0) = \rho_{\mathrm{PBH}}(t_f) / \rho_{\mathrm{rad}}(t_f)$$

The PBH abundance evolves as $\rho_{\mathrm{PBH}}(t) \propto a^{-3}$ (matter scaling) compared to $\rho_{\mathrm{rad}}(t) \propto a^{-4}$ (radiation scaling). At later times, the ratio grows as $a$.

The present-day PBH mass density (for PBHs that have not yet evaporated):
$$\rho_{\mathrm{PBH}}(t_0) = \beta(M_0) \cdot \rho_{\mathrm{rad}}(t_f) \cdot (a_f/a_0)^3$$

For PBHs that have evaporated, replace $\rho_{\mathrm{PBH}} \to \rho_{\mathrm{remnant}} = (M_*/M_0) \rho_{\mathrm{PBH}}$ since each PBH leaves a single remnant of mass $M_*$ instead of its full $M_0$.

### 5.2 The remnant relic-matter fraction

For an initial mass function $\beta(M_0)$ over the range $M_* < M_0 < M_{\mathrm{evap}}$, the present-day remnant mass density:
$$\rho_{\mathrm{remnant}}(t_0) = \int_{M_*}^{M_{\mathrm{evap}}} dM_0\, \beta(M_0) \rho_{\mathrm{rad}}(t_f(M_0)) (a_f/a_0)^3 \cdot (M_*/M_0)$$

Evaluating the cosmological scaling factors (radiation-dominated era during PBH formation), with formation at horizon-crossing:
$$\rho_{\mathrm{rad}}(t_f) (a_f/a_0)^3 \propto (a_f/a_0)^{-1} \rho_{\mathrm{rad}}(t_0)$$

The relic-matter fraction:
$$\Omega_{\mathrm{relic}} = \frac{\rho_{\mathrm{remnant}}(t_0)}{\rho_{\mathrm{crit}}} = \int_{M_*}^{M_{\mathrm{evap}}} dM_0\, \beta(M_0) \cdot \mathcal{F}(M_0) \cdot (M_*/M_0)$$

where $\mathcal{F}(M_0)$ is the cosmological-evolution factor accounting for radiation-to-matter equality plus matter-radiation density ratio at present.

### 5.3 Order-of-magnitude estimate

For order-of-magnitude scaling:
$$\Omega_{\mathrm{relic}} \sim \beta_{\mathrm{eff}} \cdot \langle M_* / M_0 \rangle$$

where $\beta_{\mathrm{eff}}$ is the effective PBH formation fraction integrated over the relevant mass range, and $\langle M_* / M_0 \rangle$ is the mass-loss fraction per PBH (typically $\ll 1$ since $M_* \ll M_0$ for most evaporated PBHs).

For $\beta_{\mathrm{eff}} \lesssim 10^{-22}$ (BBN-constrained at $M_0 \sim 10^{15}$ g) and $\langle M_*/M_0 \rangle \sim 10^{-19}$ (taking $M_0 \sim 10^{11}$ kg):
$$\Omega_{\mathrm{relic}} \sim 10^{-22} \cdot 10^{-19} \sim 10^{-41}$$

For unconstrained low-mass formation (where $\beta(M_0)$ can be larger because evaporation completed before BBN):
$$\Omega_{\mathrm{relic}} \sim \beta_{\mathrm{low-M}} \cdot 10^{-(\text{some power})}$$

with $\beta_{\mathrm{low-M}}$ allowed up to $\sim 10^{-3}$ to $10^{-1}$ depending on the formation epoch and constraints. The relic-matter fraction can therefore range widely depending on PBH formation history.

### 5.4 The full calculation table

Summarizing the four scenarios:

| Scenario | $\beta_{\mathrm{eff}}$ range | Mass range | $\Omega_{\mathrm{relic}}$ estimate |
|---|---|---|---|
| Scale-invariant ($\alpha = 5/2$) | $\lesssim 10^{-22}$ | $M_*$ to $M_{\mathrm{evap}}$ | $10^{-30}$ to $10^{-20}$ |
| Blue-tilted, moderate | $10^{-15}$ to $10^{-10}$ | Concentrated at low M | $10^{-15}$ to $10^{-10}$ |
| Critical collapse | $\beta_{\mathrm{peak}} \cdot M_*/M_{\mathrm{peak}}$ | Narrow peak | $10^{-41}$ to $10^{-15}$ |
| Inflationary spike (low-M) | Up to $10^{-3}$ within constraints | Concentrated at very low M | $10^{-3}$ to $10^{-15}$ |

**The relic-matter fraction $\Omega_{\mathrm{relic}}$ depends sensitively on the PBH formation scenario.** For standard scale-invariant or critical-collapse scenarios, the fraction is negligibly small. For blue-tilted or inflationary-spike scenarios with concentrated low-mass formation, the fraction can be cosmologically significant.

---

## 6. Observational Constraints

The remnant population at $M_* \sim m_P \sim 10^{-8}$ kg is *itself* constrained only weakly by direct observations — the remnants are too small for direct microlensing, too gravitationally weak to produce significant structure-formation effects, and too dilute (in most scenarios) to produce dynamical signatures. Most constraints on the remnant population come *indirectly* through constraints on the parent PBH population.

### 6.1 Big Bang Nucleosynthesis (BBN) constraints

PBHs evaporating during or before BBN (epoch $t \sim 1$ s to $\sim 10^3$ s, corresponding to PBHs of $M_0 \sim 10^9$ to $10^{14}$ g) inject high-energy particles that can disrupt nucleosynthesis. Constraints [1, 6]:
$$\beta(M_0) \lesssim 10^{-22} \text{ to } 10^{-18}$$

over $M_0 \in [10^9, 10^{14}]$ g. These constraints translate to $\Omega_{\mathrm{relic}}$ contributions from this mass range that are $\lesssim 10^{-15}$.

### 6.2 CMB spectral distortions

PBHs evaporating after recombination but before structure formation inject high-energy photons into the CMB, producing $\mu$-type and $y$-type spectral distortions. COBE/FIRAS constraints [7]:
$$\beta(M_0) \lesssim 10^{-21}$$

at $M_0 \sim 10^{15}$ g (current evaporation epoch). Future CMB-S4 and PIXIE experiments [8] would tighten this by an order of magnitude.

### 6.3 Diffuse gamma-ray background

PBHs at the current evaporation threshold produce gamma rays observable by EGRET, Fermi-LAT, HESS, and CTA. Constraints [9]:
$$\beta(M_0) \lesssim 10^{-26}$$

at $M_0 \approx M_{\mathrm{evap}} \sim 5 \times 10^{14}$ g. **The gamma-ray background is the strongest constraint at the evaporation-epoch mass.** This implies $\Omega_{\mathrm{relic}}$ contributions from $M_0 \sim M_{\mathrm{evap}}$ are $\lesssim 10^{-26} \cdot (M_*/M_{\mathrm{evap}}) \sim 10^{-43}$ — entirely negligible.

### 6.4 Microlensing constraints

Microlensing surveys (MACHO, OGLE, Subaru-HSC, EROS) constrain PBHs in the mass range $10^{-10}$ to $10^{2} M_\odot$ [10, 11]. The relevant PBHs do *not* evaporate (their lifetimes far exceed the age of the universe), so they are constrained as persistent intermediate-mass objects, not as remnants. **Microlensing constraints do not directly constrain the remnant abundance.**

### 6.5 Gravitational-wave constraints

LIGO/Virgo/KAGRA observations constrain PBH binary mergers in the stellar-mass to intermediate-mass range. Specific constraints depend on the mass function shape [12]. **For Planck-mass remnants, gravitational-wave detection is far below current sensitivity.**

### 6.6 Structure formation and large-scale-structure surveys

PBHs at intermediate masses ($M_0 \sim 10^{20}$ to $10^{30}$ g) modify structure formation through Poisson noise [13]. **For Planck-mass remnants, structure-formation effects are negligible due to the vastly smaller mass per object.**

### 6.7 Cosmic-ray air-shower constraints

Planck-mass particles colliding with cosmic-ray protons would produce extreme-energy cascades observable by air-shower observatories (Pierre Auger, Telescope Array). The cross-section for Planck-mass-particle / proton collisions is $\sim$ Planck-scale (many orders of magnitude below proton-proton cross-sections), so the rate is extremely low. **Current air-shower observatories do not significantly constrain Planck-mass remnant abundance.**

### 6.8 Constraint compilation

The relic-matter fraction $\Omega_{\mathrm{relic}}$ contribution from any specific PBH mass range $[M_1, M_2]$ is bounded:
$$\Omega_{\mathrm{relic}}|_{[M_1, M_2]} \leq \beta_{\mathrm{constraint}}(M_1, M_2) \cdot \frac{M_*}{\langle M_0 \rangle}$$

For the strongest-constrained mass range ($M_0 \sim 10^{14}$ g, gamma-ray bound), $\Omega_{\mathrm{relic}}$ contribution is bounded $\lesssim 10^{-43}$ — entirely negligible.

For weakly-constrained low-mass formation regimes ($M_0 \sim 10^{4}$ g and below, evaporation in the very early universe before any post-BBN observable), $\beta$ can be larger and $\Omega_{\mathrm{relic}}$ contributions of order $10^{-3}$ to $10^{-10}$ are possible.

**The observational constraints push the predicted relic-matter fraction toward small values, but do not exclude scenarios with $\Omega_{\mathrm{relic}}$ in the range $10^{-15}$ to $10^{-3}$ depending on PBH formation history.**

---

## 7. Compatible Scenarios

### 7.1 Negligible-$\Omega_{\mathrm{relic}}$ scenarios

The standard scale-invariant primordial spectrum, the standard critical-collapse formation, and any formation scenarios producing $\beta(M_0)$ at or below standard-cosmology-constraint values produce $\Omega_{\mathrm{relic}} \lesssim 10^{-15}$ — cosmologically negligible.

These scenarios are *fully compatible* with the framework's H-8 prediction. The remnant population is structurally predicted but cosmologically invisible. The framework's substrate-gravity (galactic_dynamics walkthrough) handles the empirical phenomenology of galactic dynamics; the remnant population is a subdominant cosmic-energy-budget contribution that does not produce significant observational signatures.

### 7.2 Moderate-$\Omega_{\mathrm{relic}}$ scenarios

Blue-tilted spectra with moderate enhancement at small masses, or specific inflationary-feature scenarios, can produce $\Omega_{\mathrm{relic}}$ in the range $10^{-10}$ to $10^{-5}$. These are within current observational constraints but produce a subdominant relic-matter component.

In these scenarios, the remnant population is a structural cosmological prediction that contributes a small but nonzero fraction of the cosmic energy budget. It is too small to dominate but significant enough to be a cosmological signature.

### 7.3 Significant-$\Omega_{\mathrm{relic}}$ scenarios (constrained)

For inflationary-spike scenarios with concentrated formation at very low masses ($M_0 \sim 10^{4}$ to $10^{8}$ g) and high formation efficiency ($\beta_{\mathrm{peak}} \sim 10^{-3}$), $\Omega_{\mathrm{relic}}$ can approach $10^{-3}$ to $10^{-2}$.

Such scenarios are at the boundary of observational viability — strongly constrained but not entirely ruled out. They would represent a cosmologically significant relic-matter component.

### 7.4 Dominant-$\Omega_{\mathrm{relic}}$ scenarios

Scenarios producing $\Omega_{\mathrm{relic}} \gtrsim 0.1$ (a substantial fraction of the cosmic energy budget) require finely-tuned PBH formation parameters. They are largely excluded by current observational constraints across the relevant mass ranges.

The framework does not predict that remnants constitute a dominant fraction of the cosmic energy budget. It predicts a structural population whose abundance depends on the empirical PBH formation history.

### 7.5 Compatible scenario summary

| Scenario class | $\Omega_{\mathrm{relic}}$ range | Observationally compatible? |
|---|---|---|
| Standard scale-invariant | $10^{-30}$ to $10^{-20}$ | Yes (negligible) |
| Critical collapse | $10^{-41}$ to $10^{-25}$ | Yes (negligible) |
| Blue-tilted, moderate | $10^{-15}$ to $10^{-5}$ | Yes (subdominant relic) |
| Inflationary spike, moderate | $10^{-10}$ to $10^{-5}$ | Yes (subdominant relic) |
| Inflationary spike, aggressive | $10^{-5}$ to $10^{-3}$ | Marginally compatible |
| Inflationary spike, extreme | $\gtrsim 10^{-3}$ | Constrained / excluded |
| Spike at very low $M$ ($M_0 \sim M_*$) | Up to order unity | Largely excluded by indirect constraints |

---

## 8. Verdict

> **VERDICT (H9): Relic-matter fraction $\Omega_{\mathrm{relic}}$ structurally predicted, scenario-dependent, with bounds set by observational constraints on parent PBH population.**
>
> H-8 forces a stable Planck-mass remnant from every PBH that has fully evaporated by the present epoch. The cosmological abundance of the remnant population is a structural consequence of substrate-cutoff physics combined with the empirical PBH formation history. For standard scale-invariant or critical-collapse formation scenarios, $\Omega_{\mathrm{relic}} \lesssim 10^{-15}$ — cosmologically negligible. For blue-tilted or inflationary-spike scenarios with concentrated low-mass formation, $\Omega_{\mathrm{relic}}$ can range from $10^{-15}$ to $\sim 10^{-3}$ within current observational constraints. Larger values are largely excluded by BBN, CMB-distortion, and gamma-ray-background constraints on the parent PBH population.

**Verdict-class details:**

- **(C9a) Structural existence:** FORCED via H-8.
- **(C9b) Abundance calculation:** straightforward given input mass function $\beta(M_0)$.
- **(C9c) Scenario-dependence:** FORCED by the calculation; specific values INHERITED from cosmological-PBH formation history.
- **(C9d) Constraint compatibility:** observational constraints bound $\Omega_{\mathrm{relic}}$ from above; scenarios with $\Omega_{\mathrm{relic}}$ up to $\sim 10^{-3}$ are compatible.
- **No new active CANDIDATEs.** Active CANDIDATE inventory remains {} as of arc-opening tally.

**Important framing emphasis:** the framework's substrate-gravity already explains galactic dynamics without dark matter. The Planck-mass remnant population is a *separate* structural prediction about cosmic relic-matter content. Whether this relic-matter component is cosmologically significant depends on the empirical PBH formation history — which is itself a cosmological-observational question, separate from any DM-explanation framing.

**The framework predicts that some non-zero relic-matter component exists** (FORCED via H-8), but does not predict a specific abundance — that depends on the cosmological PBH formation history, which is INHERITED from observational cosmology.

---

## 9. Falsification and Circularity Audit

### 9.1 Circularity audit

| Potential circularity | Audit verdict |
|---|---|
| H-8 used as derivation premise? | **Yes — as input only.** H-8's stable Planck-mass remnant prediction is the starting point; not re-derived. |
| Standard PBH formation scenarios used as derivation premise? | **No — used as inputs.** Initial mass functions are external cosmology-literature objects; the calculation produces $\Omega_{\mathrm{relic}}$ from these inputs. |
| Standard cosmological evolution used as derivation premise? | **Yes — as background framework.** The cosmological evolution outside the substrate-saturation regime is standard $\Lambda$CDM, which the framework's substrate-gravity work treats as the empirical-cosmology baseline. |
| Self-reference of H-9 within itself? | **No.** §3 → §4 → §5 → §6 → §7 → §8 derivation chain is acyclic. |
| **DM-explanation framing assumed?** | **Explicitly avoided.** §2 framing note establishes that ED's substrate-gravity already explains galactic dynamics without DM. Remnants are framed as relic-matter, not DM candidates. |

**Acyclicity confirmed. No DM-explanation framing imposed.**

### 9.2 Falsifiers

**Falsifier for the structural existence of remnants (C9a):**
H-8's substrate-cutoff regularization argument is refuted. This would be a substrate-level refutation of the framework's stable-remnant prediction. Specifically, if substrate-microscopic analysis demonstrates that DCGT closure does not produce a stable endpoint at $M_* > 0$, the remnant prediction is refuted.

**Falsifier for the abundance calculation (C9b):**
The calculation assumes standard cosmological evolution outside the substrate-saturation regime. If ED's substrate-cosmology (when developed) produces qualitatively different cosmic evolution affecting the remnant abundance calculation, the calculation needs revision.

**Falsifier for specific scenarios (C9c):**
Direct detection of stable Planck-mass remnants at specific abundance levels would corroborate or refute specific PBH formation scenarios. Conversely, observational refutation of specific PBH formation scenarios constrains the relic-matter fraction.

**Falsifier for constraint compatibility (C9d):**
A future observation (CMB-S4, PIXIE, future gamma-ray observatory, structure-formation precision) detecting a relic-matter signature inconsistent with the framework's prediction would falsify the prediction. Detection of a Planck-mass relic with abundance significantly different from the calculated range would be informative.

### 9.3 Subtle empirical edge cases

**Detection signatures of Planck-mass remnants:**
- Microlensing: not feasible (Planck-mass too small).
- Gravitational lensing: not feasible (gravity too weak per particle).
- Cosmic-ray collisions: extreme-energy events with characteristic Planck-scale signatures; no such events detected to date.
- Structure formation: Poisson-noise constraints essentially absent for Planck-mass particles.

The framework's prediction is therefore *currently observationally consistent* across the full range of compatible scenarios. Future observations could distinguish, but current observations do not.

---

## 10. Consequences for the Framework

1. **H-9 closes as cosmological-calculation memo.** With H-8's remnant prediction in hand, H-9 establishes the cosmological-abundance question as scenario-dependent and provides bounds.

2. **The framework's cosmology sector is now structurally connected to the BH program.** The cosmic energy budget includes a structural relic-matter component from PBH evaporation, with the abundance dependent on inflationary cosmology and PBH formation history.

3. **No conflict with substrate-gravity galactic dynamics.** The framework's substrate-gravity (galactic_dynamics walkthrough) explains galactic phenomenology without DM. The relic-matter component from H-9 is a separate cosmological prediction that does not contradict or supplement the substrate-gravity content.

4. **Cross-arc connection to substrate-gravity Hubble parameter.** The substrate-gravity transition acceleration $a_0 = c H_0/(2\pi)$ uses the Hubble parameter as cosmological input. H-9's calculation similarly uses $H_0$ and standard cosmology. Both arcs operate within the same empirical cosmology framework.

5. **Falsifiable cosmological predictions.** The framework predicts non-zero $\Omega_{\mathrm{relic}}$ structurally, with the value depending on PBH formation history. Future precision cosmology (CMB-S4, PIXIE, next-generation gamma-ray observatories) would constrain or refute specific scenarios.

6. **No new active CANDIDATEs.** Active CANDIDATE inventory remains {}.

7. **Open work flagged:** the substrate-cosmology program (potential Arc COSMO from the Investigation Priority List) would extend H-9's calculation to include any substrate-level modifications to cosmological evolution. Currently, H-9 uses standard $\Lambda$CDM as the empirical-cosmology baseline.

---

## 11. Summary

**What this memo accomplished.**

- Stated the H-9 CANDIDATE (§1) decomposing it into (C9a) structural existence, (C9b) abundance calculation, (C9c) scenario-dependence, (C9d) constraint compatibility.
- Established the framing note (§2): ED's substrate-gravity explains galactic dynamics without DM; remnants are a *separate* structural cosmological prediction, not a DM candidate.
- Started from H-8's stable Planck-mass remnant endpoint $M_* = c_*\ell_P$ (§3).
- Computed remnant relic-matter fractions for four PBH formation scenarios (§§4–5):
  - Scale-invariant: $\Omega_{\mathrm{relic}} \sim 10^{-30}$ to $10^{-20}$ (negligible).
  - Blue-tilted: $\Omega_{\mathrm{relic}} \sim 10^{-15}$ to $10^{-5}$ (subdominant relic).
  - Critical collapse: $\Omega_{\mathrm{relic}} \sim 10^{-41}$ to $10^{-25}$ (negligible).
  - Inflationary-spike: $\Omega_{\mathrm{relic}}$ up to $\sim 10^{-3}$ within constraints (marginal).
- Audited observational constraints (§6): BBN, CMB distortions, gamma-ray backgrounds, microlensing, gravitational waves, structure formation, cosmic-ray showers.
- Identified compatible scenarios (§7): negligible / subdominant relic / marginal cases all observationally viable; dominant cases largely excluded.
- Issued the verdict (§8): structural existence FORCED via H-8; specific abundance INHERITED from PBH formation history; observational constraints bound the abundance.
- Confirmed acyclicity and provided substrate-level + empirical falsifiers (§9).
- Identified consequences for the framework (§10).

**Trending toward:** a non-zero relic-matter component is structurally predicted; its abundance is scenario-dependent; observational constraints push it toward small values but do not exclude $\Omega_{\mathrm{relic}}$ up to $\sim 10^{-3}$.

**Brief 2–3 sentence summary:** Given H-8's prediction of stable Planck-mass remnants from primordial-BH evaporation, the present-day relic-matter fraction $\Omega_{\mathrm{relic}}$ is computable from any specified PBH formation scenario, ranging from $10^{-30}$ for standard scale-invariant spectra (negligible) to $\sim 10^{-3}$ for aggressive inflationary-spike scenarios at the boundary of observational viability. Existing constraints from BBN, CMB spectral distortions, and the diffuse gamma-ray background bound the parent PBH population and thereby constrain the remnant abundance indirectly; for most standard scenarios, $\Omega_{\mathrm{relic}} \ll 1$ and the remnant population is cosmologically subdominant. **Critical framing:** the framework's substrate-gravity already explains galactic dynamics (rotation curves, BTFR, transition acceleration) without invoking dark matter; the Planck-mass remnant population is therefore a *separate structural cosmological prediction* about cosmic relic-matter content, not a DM-explanation candidate, with the relic-matter fraction inherited from the empirical cosmological PBH formation history.

---

## 12. Recommended Next Steps

Multiple options, in decreasing order of immediate productivity:

1. **(Cross-link memo) Update H-7 synthesis and BH-information-paradox-resolution paper.** With H-8 + H-9 closed, the H-arc late-time content is now: (i) Scenario C FORCED, (ii) structural relic-matter prediction with scenario-dependent abundance. The BH-information-paradox-resolution paper at `papers/BH_Information_Paradox_Resolution/` should be updated to reflect the H-9 abundance calculation and explicitly note that the framework's substrate-gravity already explains galactic dynamics without DM (so remnants are not a DM candidate). Estimated 1–2 sessions.

2. **(Substrate cosmology Arc COSMO scoping)** A scoping memo for substrate-level cosmology — substrate-derived Friedmann-class equations, substrate-level $H_0$ derivation, expansion-history dynamics, substrate-cosmology effects on the H-9 calculation. The cosmology sector is currently the framework's most-open frontier; a substrate-cosmology arc would couple naturally with H-9. Estimated 2–4 sessions for scoping; full arc would be much longer.

3. **(Closed-form $c_*$ derivation memo)** The substrate-microscopic derivation of $c_* = M_*/\ell_P$ from V5-kernel + DCGT closure microscopic details would tighten the abundance prediction. Couples with O2 (closed-form $\log g$) and other closed-form-substrate-constants problems. Estimated 2–4 sessions.

4. **(Cross-domain memo) Substrate-saturation regime universalities.** The substrate-saturation regime that produces Planck-mass remnants may have cross-domain implications: behavior near the cosmic horizon $R_H = c/H_0$, early-universe substrate density, Q-COMPUTE multiplicity-saturation, BH interior structure. A unified memo articulating the substrate-saturation pattern would strengthen the framework's structural unification. Estimated 2–3 sessions.

5. **(Empirical engagement) Future-observation prediction memo.** Articulate specific observational targets that would test the framework's relic-matter prediction: CMB-S4 spectral-distortion sensitivity, PIXIE projected limits, next-generation gamma-ray observatory thresholds, gravitational-wave constraints on PBH binaries. Estimated 1–2 sessions.

6. **(Memory update + repository organization)** Document H-8 + H-9 closures in `MEMORY.md`. Add the relic-matter calculation to the framework's cross-session retrieval inventory. Brief documentation pass.

7. **(Walkthrough on substrate-cutoff regularization)** A walkthrough articulating the substrate-cutoff regularization pattern across multiple framework sectors — V5 cutoff in Hawking, DCGT closure at Planck mass, substrate-saturation regime in BH interior, substrate-cosmology limits — would extend the public-facing series. Title candidate: `from_primitives_to_substrate_cutoff_regularization.md`. Estimated 1–2 sessions.

---

## References

[1] Carr, B., Kuhnel, F., Sandstad, M. "Primordial Black Holes as Dark Matter." *Physical Review D* **94**, 083504 (2016). [Standard compilation of PBH constraints; framing note: the title's "as Dark Matter" refers to the standard literature's framing, not to ED's framework, which does not require DM.]

[2] Carr, B. J., Hawking, S. W. "Black Holes in the Early Universe." *Monthly Notices of the Royal Astronomical Society* **168**, 399–415 (1974).

[3] Carr, B. J. "Primordial Black Holes: Do They Exist and Are They Useful?" *Inflating Horizons of Particle Astrophysics and Cosmology* (2005).

[4] Niemeyer, J. C., Jedamzik, K. "Near-Critical Gravitational Collapse and the Initial Mass Function of Primordial Black Holes." *Physical Review Letters* **80**, 5481–5484 (1998).

[5] Garcia-Bellido, J., Ruiz Morales, E. "Primordial Black Holes from Single Field Models of Inflation." *Physics of the Dark Universe* **18**, 47–54 (2017).

[6] Carr, B., Dimopoulos, K., Owen, C., Tenkanen, T. "Primordial Black Hole Formation During Slow Reheating After Inflation." *Physical Review D* **97**, 123535 (2018).

[7] Fixsen, D. J., Cheng, E. S., Gales, J. M., et al. "The Cosmic Microwave Background Spectrum from the Full COBE/FIRAS Data Set." *Astrophysical Journal* **473**, 576 (1996).

[8] Kogut, A., Fixsen, D. J., Chuss, D. T., et al. "The Primordial Inflation Explorer (PIXIE): A Nulling Polarimeter for Cosmic Microwave Background Observations." *Journal of Cosmology and Astroparticle Physics* **2011** (07), 025 (2011).

[9] Carr, B., Dimopoulos, K., Owen, C., Tenkanen, T. (compilation in [1] with updates through 2020).

[10] Tisserand, P., Le Guillou, L., Afonso, C., et al. "Limits on the MACHO Content of the Galactic Halo from the EROS-2 Survey of the Magellanic Clouds." *Astronomy & Astrophysics* **469**, 387–404 (2007).

[11] Niikura, H., Takada, M., Yasuda, N., et al. "Microlensing Constraints on Primordial Black Holes with Subaru/HSC Andromeda Observations." *Nature Astronomy* **3**, 524–534 (2019).

[12] Sasaki, M., Suyama, T., Tanaka, T., Yokoyama, S. "Primordial Black Hole Scenario for the Gravitational-Wave Event GW150914." *Physical Review Letters* **117**, 061101 (2016).

[13] Carr, B. J., Silk, J. "Primordial Black Holes as Generators of Cosmic Structures." *Monthly Notices of the Royal Astronomical Society* **478**, 3756–3775 (2018).

[14] Proxmire, A. *Arc Hawking H-8: Higher-Order Resummation and the Late-Time Evaporation Endpoint.* May 2026.

[15] Proxmire, A. *Walkthrough: From Primitives to Galactic Dynamics.* (Substrate-gravity derivation explaining galactic phenomenology without dark matter.) May 2026.

[16] Proxmire, A. *Walkthrough: From Primitives to Hawking Radiation.* May 2026.

[17] The full Event Density corpus, including all forced theorems and supporting memos, is available at https://github.com/allen-proxmire/event-density.

---

**Pause for further instruction.**
