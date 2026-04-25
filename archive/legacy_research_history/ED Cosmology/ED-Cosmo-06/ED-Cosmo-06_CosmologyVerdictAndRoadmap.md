# ED-Cosmo-06: Cosmology Verdict and Roadmap

**Author:** Allen Proxmire
**Series:** ED-Cosmo-06
**Date:** March 2026
**Status:** Synthesis and provisional verdict

---

# 1. Cosmology Programme Recap

## What Was Tested

The ED cosmology programme (ED-Cosmo-01 through 05) tested a single, specific hypothesis:

> **Can the canonical ED PDE — a telegraph-type nonlinear diffusion equation with degenerate mobility, penalty relaxation, and participation coupling — reproduce the observed expansion history of the universe without a gravitational sector, without a cosmological constant, and without modifying the PDE's constitutive structure?**

The mechanism proposed was **synchronization**: the participation channel coordinates disparate local expansion rates into a coherent global signal, producing apparent acceleration ($q < 0$) from the collective dynamics of voids and filaments rather than from a repulsive force.

## The Arc

**ED-Cosmo-01 (Homogeneous Limit).** Derived the 2-ODE telegraph system for the mean density $\bar{\rho}(t)$ and participation $v(t)$. Found that the penalty channel relaxes $\bar{\rho}$ to $\rho^*$ too fast — the Hubble parameter decays to near-zero by $t_0 = 13.8$ Gyr. F1 failed for all five candidate parameter sets (83–97% mismatch with $H_0$). Diagnosed the cause: the homogeneous limit removes the mobility channel, which is the only mechanism that can resist relaxation.

**ED-Cosmo-02 (Spatial PDE).** Restored spatial structure via a 1D expanding-coordinate PDE with three ICs (void-filament, random field, single void). Found apparent acceleration ($q < 0$, F2: 3/3 PASS), correct void-filament differential (F7: 3/3), and partial synchronization (F6: 1/3). But the self-consistent scale factor used a naive Hubble-dilution term $-\mathcal{H}\rho$ that created a feedback tautology, producing contraction ($a < 1$) in stable runs and numerical blowup in the random-field IC.

**ED-Cosmo-03 (Penalty-Dilution Correction).** Identified the mathematical error: the naive dilution term double-counts the expansion. Derived the correct system from physical mass conservation — the comoving PDE has no explicit dilution; the scale factor is determined by a separate ODE driven by penalty mass flow. Proved analytically that $a(t) > 1$ and $\mathcal{H}(t) > 0$ for all $t > 0$ in the homogeneous limit. Predicted $P_0 \cdot \eta(t_0) \approx 1$ as the Hubble-matching constraint.

**ED-Cosmo-04 (Corrected Spatial PDE).** Implemented the corrected system and re-ran all three ICs. All three ran stably (including the previously unstable random-field IC). Synchronization became universal and extremely strong (F6: 3/3, variance drops to < 1% of initial). But the corrected system produced deceleration ($q > 0$, F2: 0/3) and slight contraction ($a \approx 0.95$, F5: 0/3). The apparent acceleration in ED-Cosmo-02 had been an artifact of the incorrect dilution term.

**ED-Cosmo-05 (P₀ Sweep).** Swept $P_0 \in \{1, 3, 10, 30\}$ to find a regime matching $H_0$, $q_0 < 0$, and $a > 1$ simultaneously. At low $P_0$ (1, 3): acceleration ($q < 0$) but contraction ($a < 1$) and large $H$-mismatch. At high $P_0$ (10, 30): deceleration ($q > 0$) and contraction. The comoving density overshoots $\rho^*$ and oscillates, causing the scale factor to reverse. No parameter set satisfies F1, F2, and F5 simultaneously. The $P_0 \cdot \eta$ constraint predicts $P_0 \sim 2$–$10$, but at those values $\eta(t_0)$ has already gone negative (the system has passed through $\rho^*$).

---

# 2. Positive Results

Despite the falsification of the complete cosmological model, the programme produced four robust and scientifically significant results.

## 2.1 Synchronization Is Universal (F6)

The participation channel produces synchronization of local expansion rates in every configuration tested — all three ICs, all four $P_0$ values, both the incorrect and corrected PDE formulations. The expansion-rate variance $\sigma^2_{\mathcal{H}}$ drops to less than 1% of its initial value in every stable run. This is not a marginal effect; it is a dominant feature of the coupled PDE dynamics.

**What this means:** If the ED PDE operates at cosmological scales in any capacity, it will synchronize local dynamics into coherent global behaviour. This mechanism survives independently of the scale-factor identification problem and could operate as a *correction* to standard cosmology rather than a replacement.

## 2.2 Telegraph Relaxation and Quarter-Wave Behaviour

The mean density follows the telegraph equation (damped oscillator) with a period much longer than the age of the universe ($T_{\text{osc}} \sim 90$–$270$ Gyr for the tested parameters). The observable consequence is a quarter-wave deviation from monotonic relaxation — the first slow swing of a very long oscillation. This produces a predictable, testable signature in the expansion history: a subtle departure from the smooth $\Lambda$CDM curve that is neither monotonic nor rapidly oscillatory.

## 2.3 Structural Consistency

The Compton/Hubble anchoring ($H = D_{\text{nd}}$, giving $c_{\text{ED}} = c$) works exactly as derived. The Lyapunov stability criterion ($H/P_0 < 100$) is satisfied at every tested parameter point. The nine architectural laws from ED-Phys-06 apply throughout the cosmological parameter range. The ED architecture is internally consistent at Hubble scales — it simply does not, by itself, produce the correct expansion history.

## 2.4 The Void-Filament Differential

In the uncorrected system (ED-Cosmo-02), voids expand faster than filaments — the physically correct behaviour. This reverses in the corrected system (ED-Cosmo-04/05), which is informative: the differential depends on the expansion-density coupling, not just the mobility channel. A correct gravitational coupling may restore the void-filament ordering.

---

# 3. Negative Results and Structural Failures

## 3.1 F1+F5: The Scale Factor Cannot Sustain Expansion

The central failure: the ED-derived scale factor $a(t) = \bar{\rho}_{\text{com}}(0)/\bar{\rho}_{\text{com}}(t)$ does not produce sustained expansion ($a > 1$ growing monotonically to the present). The comoving density relaxes to $\rho^*$ on a timescale shorter than the age of the universe, then oscillates around it. The scale factor peaks when $\bar{\rho}$ first crosses $\rho^*$ and then *reverses*.

This is not a parameter-tuning problem. It is structural: the penalty channel drives $\bar{\rho} \to \rho^*$ at rate $\gamma \sim DP_0$, and for any $P_0$ large enough to produce significant expansion ($P_0 \gtrsim 1$), the relaxation completes before $t_0$.

## 3.2 No Simultaneous F1+F2+F5 Solution

The P₀ sweep (ED-Cosmo-05) tested $P_0 \in \{0.1, 1, 3, 10, 30\}$ across three ICs. The results form a clear dichotomy:

- **Low $P_0$** ($\leq 3$): $q < 0$ (acceleration) but $a < 1$ (contraction) and $H$-mismatch $> 100\%$.
- **High $P_0$** ($\geq 10$): $q > 0$ (deceleration) and $a < 1$ (contraction).

There is no intermediate regime where all three conditions are met. The parameter space has been searched and the gap is structural, not numerical.

## 3.3 F7 Reversal in the Corrected System

The void-filament differential ($H_{\text{void}} > H_{\text{fil}}$) holds in the incorrect formulation (ED-Cosmo-02) but reverses in the corrected system (ED-Cosmo-04/05). This means the dilution term was artificially creating the correct differential — without it, the mobility channel alone does not produce the expected density-dependent expansion ordering.

## 3.4 Root Cause

The fundamental issue: **the ED PDE has no gravitational sector.** In standard cosmology, the expansion of space is governed by the Friedmann equations, which couple the matter density to the metric through Einstein's field equations. The scale factor $a(t)$ is a property of *spacetime geometry*, not of the matter field.

In ED cosmology, $a(t)$ was identified with a function of the mean comoving density — a property of the matter field. This collapses the matter-geometry distinction, making the expansion a direct consequence of the density dynamics. But the density dynamics (penalty relaxation + telegraph oscillation) do not produce the same behaviour as the Friedmann equations. The penalty channel is a *relaxation* mechanism, not a *gravitational* mechanism. It drives the system toward a fixed point, not toward accelerated expansion.

---

# 4. Provisional Verdict

## The Statement

> **Pure ED telegraph cosmology — the canonical ED PDE with the cosmological anchoring $D = c^2/H_0$, $L_0 = c/H_0$, and scale factor identified from mean density — is provisionally falsified as a standalone cosmological model. No parameter set within the architecturally permitted range produces simultaneous Hubble-rate matching ($H(t_0) \approx H_0$), acceleration ($q(t_0) < 0$), and expansion ($a(t_0) > 1$).**

## What This Means

This is a **model-level** verdict, not an architectural death sentence. The falsification applies to a specific model: the ED PDE *without gravitational coupling*, with the scale factor *identified from the mean comoving density*. It does not falsify:

- The ED PDE itself (which is validated by 112 tests, 9/9 reproducibility phases, and six structural analogues).
- The participation-field interpretation (ED-Phys-05, confirmed by the Compton anchoring and telegraph dynamics).
- The universality results (ED-Phys-06, β-sweep confirmed for β ∈ [0.5, 3.0]).
- The condensed-matter predictions (β = 2.00 ± 0.29 across three materials).
- The galactic-scale results (cored halos, BTFR, activity dependence, merger lag).
- The synchronization mechanism (universal, robust, and potentially observable).

The verdict is: **ED cosmology needs a gravitational sector.** The PDE alone — penalty, mobility, and participation — cannot replace the Friedmann equations. It may be able to *modify* them, but it cannot *replace* them.

## What Survives

Three results from the cosmology programme have permanent scientific value:

1. **Synchronization is real and robust.** Any future model that couples ED to gravity will inherit this mechanism.
2. **The telegraph quarter-wave** provides a testable prediction for dynamical dark energy models.
3. **The $H/P_0$ stability criterion** constrains the cosmological parameter space from below.

---

# 5. Roadmap Options

## 5.1 Option A: ED-Poisson Cosmology

**Concept:** Couple the ED PDE to the Poisson equation for the gravitational potential $\Phi$, exactly as done in the galactic regime (ED-Data-Galaxy series). The Friedmann equations emerge as the spatially-averaged limit of the ED-Poisson system, with ED providing the matter dynamics and gravity providing the expansion dynamics.

**Why this might work:** The galactic-regime ED-Poisson coupling already produces cored halos, the BTFR, and the correct rotation curves. The cosmological extension would let gravity — not the penalty channel — drive the expansion, while ED provides the structure formation and synchronization.

**Concrete modules:**

- **ED-Cosmo-07:** Derive the ED-Poisson cosmological equations in 1D. Show that the Friedmann equations emerge from spatial averaging.
- **ED-Cosmo-08:** Implement and simulate the 1D ED-Poisson cosmological PDE with structured ICs.
- **ED-Cosmo-09:** Compare ED-Poisson expansion history with $\Lambda$CDM and observational $H(z)$ data.

## 5.2 Option B: Alternative Scale-Factor Identification

**Concept:** Instead of identifying $a(t)$ with $\bar{\rho}(0)/\bar{\rho}(t)$ (mean density), identify it with a participation-based or horizon-based quantity:

- $a(t) \propto \xi(t)$ (correlation length — expansion = coarsening)
- $a(t) \propto 1/v_{\text{rms}}(t)$ (inverse participation amplitude — expansion = synchronization)
- $a(t)$ from the horizon radius of the telegraph propagation front

**Why this might work:** The mean density identification failed because the penalty channel relaxes $\bar{\rho}$ too fast. A participation-based identification ties the expansion to a slower dynamical quantity — the coherence of the global flow rather than its amplitude.

**Concrete modules:**

- **ED-Cosmo-07alt:** Derive alternative scale-factor definitions and their consistency conditions.
- **ED-Cosmo-08alt:** Simulate and compare: which definition produces $a(t) > 1$ monotonically while preserving $q < 0$?

## 5.3 Option C: Hybrid ED-ΛCDM

**Concept:** Accept ΛCDM as the background cosmology and use ED as a correction. The Friedmann equations govern $a(t)$; the ED PDE governs structure formation, with the participation channel providing synchronization-based corrections to the growth rate $f\sigma_8(z)$ and the void-filament differential.

**Why this might work:** ED's strongest cosmological results — synchronization, telegraph oscillation, density-dependent mobility — are all *perturbative* effects. They modify the expansion history at the 1–10% level, not the 100% level. A hybrid model captures these corrections without requiring ED to reproduce the full Friedmann dynamics.

**Concrete modules:**

- **ED-Cosmo-07hyb:** Write the ED PDE on an ΛCDM background: $a(t)$ prescribed from Planck parameters, ED evolves the density perturbations.
- **ED-Cosmo-08hyb:** Compare ED structure growth with N-body simulations and galaxy survey data ($f\sigma_8$, void statistics).
- **ED-Cosmo-09hyb:** Derive the synchronization correction to $q(z)$ and compare with DESI/Rubin precision data.

---

# 6. Pivot to Condensed Matter

## Status of the Cosmology Arc

The ED cosmology programme is **parked at ED-Cosmo-06.** The five simulation modules (01–05) have been executed, the structural limitations identified, and the roadmap laid out. No further cosmology simulations will be run until one of the three roadmap options (ED-Poisson, alternative $a(t)$, or hybrid) is specified at the theoretical level.

## Next Active Programme

The next active research direction is **condensed-matter universality** — expanding the empirical foundation from three materials to a larger set:

- **ED-Data-12+:** New materials (polymer solutions, ionic liquids, active colloids, protein mixtures at additional concentrations).
- **Front-propagation experiments:** Direct measurement of $\alpha_R$ in gradient-diffusion setups where $\beta$ is independently known.
- **Density-dependent slowing:** FRAP experiments at high volume fraction testing the $(\rho_{\max} - \rho)^\beta$ prediction near saturation.

The condensed-matter programme is where ED has its strongest empirical contact and where additional data has the highest scientific leverage.

## When Cosmology Returns

The cosmology arc will be revisited when:

1. A theoretical specification for one of the three roadmap options is complete (paper-level derivation, not simulation).
2. The condensed-matter universality claim is strengthened to $\geq 5$ materials.
3. The galactic-regime predictions (activity dependence, merger lag) have been tested against survey data.

Until then, the cosmology verdict stands: **pure ED telegraph cosmology is provisionally falsified; the synchronization mechanism is preserved for future use in a gravitationally-coupled model.**

---

*ED-Cosmo-06 · Event Density Research Programme · March 2026*
