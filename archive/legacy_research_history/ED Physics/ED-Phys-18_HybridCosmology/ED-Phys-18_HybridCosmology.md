# ED-Phys-18: Hybrid Cosmology (Oscillator + Parabolic)

## 1. Motivation and Context

ED-Phys-17 established that the P_SY2 oscillator produces universal relaxation: every density configuration — peaks, basins, voids, horizons — decays to uniform rho_star through damped oscillations. ED-Phys-13 showed that parabolic (first-order) dynamics produce monotonic, irreversible structure evolution. These are two fundamentally different cosmological regimes.

This module asks: **what happens when both layers operate simultaneously?** In the ED ontology, density evolves through participation channels that may include both diffusive (parabolic) and inertial (oscillatory) components. A hybrid universe combines both.

**Key questions:**
1. Does the parabolic channel suppress oscillations, or does the oscillatory channel suppress monotonic decay?
2. Is there a critical mixing ratio where behavior transitions between regimes?
3. Do hybrid dynamics produce new motifs absent in either pure regime?
4. How do horizons behave under mixed dynamics?
5. Does the ED framework admit a unified cosmological architecture with tunable layers?

**Canonical sources:** ED-5, ED-12, ED-12.5.

---

## 2. Hybrid Update Rule

### 2.1 Definition

The hybrid update rule combines parabolic and oscillatory dynamics through mixing weights:

```
drho/dt = D * RHS  +  H * v
dv/dt   = (1/tau) * (RHS - zeta * v)
```

where:
- RHS = M(rho) * Lap(rho) + M'(rho) * |grad rho|^2 - P_SY2(rho)
- D = parabolic weight (direct density response to RHS)
- H = oscillatory weight (density responds through velocity channel)
- D + H = 1 (normalization constraint)

### 2.2 Limiting Cases

- **D = 1, H = 0 (pure parabolic):** drho/dt = RHS. The velocity v decouples — density responds instantaneously to forces. Monotonic, irreversible, no oscillations.

- **D = 0, H = 1 (pure oscillatory):** drho/dt = v, dv/dt = (1/tau)(RHS - zeta*v). Density responds through inertial channel only. Produces damped oscillations.

- **0 < D < 1, 0 < H < 1 (hybrid):** Both channels active. The parabolic channel provides direct, immediate response while the oscillatory channel adds inertial memory.

### 2.3 Three Hybrid Regimes

| Regime | D | H | Character |
|--------|---|---|-----------|
| Oscillator-dominated | 0.2 | 0.8 | Mostly inertial, weak direct response |
| Balanced hybrid | 0.5 | 0.5 | Equal parabolic and oscillatory weight |
| Parabolic-dominated | 0.8 | 0.2 | Mostly direct response, weak inertia |

### 2.4 Predictions

1. **Oscillator-dominated (D=0.2, H=0.8):** Should retain oscillations but with faster damping than pure oscillatory, because the D=0.2 parabolic channel adds direct dissipation.

2. **Balanced hybrid (D=0.5, H=0.5):** Should show transitional behavior — oscillations may be critically damped.

3. **Parabolic-dominated (D=0.8, H=0.2):** Should behave like slightly modified parabolic dynamics — monotonic decay with minor oscillatory perturbations.

---

## 3. Experimental Setup

### 3.1 Parameters

All experiments use canonical parameters from ED-Phys-15:

| Parameter | Value |
|-----------|-------|
| alpha | 0.1 |
| gamma | 0.5 |
| M_0 | 1.0 |
| rho_max | 100 |
| n_mob | 2 |
| dx | 1.0 |
| tau | 100 |
| zeta | 0.5 |
| rho_star | 50 |
| rho_0 | 0.5 |
| CFL | 0.4 |

1D grid: N = 512. 2D grid: 128 x 128.

### 3.2 Diagnostics

Same as ED-Phys-17: peak/basin/horizon tracking, energy diagnostics, positivity monitoring. Additionally:
- **Half-life:** Steps for rho_std to drop to half its initial value (measures relaxation speed).
- **Horizon lifetime:** Consecutive tracking samples with horizon sites > 0.

---

## 4. Results: Single-Peak Hybrid Dynamics (Experiment 1)

### 4.1 Peak Relaxation Across Regimes

Single Gaussian peak: height = 30 above rho_star, sigma = 15, on flat background. 50K steps.

| Regime | D | H | Oscillations | Merges | E_initial | E_final | Clips |
|--------|---|---|-------------|--------|-----------|---------|-------|
| Pure oscillatory | 0.0 | 1.0 | 8 | 24 | 0.1439 | 0.0250 | 0 |
| Osc-dominated | 0.2 | 0.8 | 2 | 6 | 0.1438 | 0.0250 | 0 |
| Balanced | 0.5 | 0.5 | 0 | 1 | 0.1438 | 0.0250 | 0 |
| Par-dominated | 0.8 | 0.2 | 0 | 1 | 0.1438 | 0.0250 | 0 |
| Pure parabolic | 1.0 | 0.0 | 0 | 1 | 0.1438 | 0.0250 | 0 |

**Key findings:**

1. **Sharp oscillation threshold:** Oscillations persist only when H > 0.5. At D = 0.5 (balanced), oscillations are already fully suppressed. The parabolic channel is a powerful oscillation damper.

2. **Identical final energy:** All regimes reach E_final = 0.0250 (the ground state alpha*gamma*rho_0). The destination is universal; only the path differs.

3. **Oscillation count drops steeply:** Pure oscillatory = 8 oscillations. Adding just D = 0.2 drops it to 2. Adding D = 0.5 eliminates oscillations entirely. The parabolic channel overwhelms the oscillatory channel.

4. **Zero clips in all regimes.** The hybrid update is positivity-safe across all mixing ratios.

---

## 5. Results: Multi-Peak Hybrid Cosmology (Experiment 2)

### 5.1 Multi-Peak Systems Across Regimes

2, 5, and 10 peaks on flat backgrounds, 80K steps.

| Config | Regime | Peaks (init->final) | Oscillations | Merges |
|--------|--------|-------------------|-------------|--------|
| 2 peaks | osc_dom (0.2/0.8) | 2->0 | 3 | 8 |
| 2 peaks | balanced (0.5/0.5) | 2->0 | 0 | 2 |
| 2 peaks | par_dom (0.8/0.2) | 2->0 | 0 | 2 |
| 5 peaks | osc_dom | 4->0 | 2 | 9 |
| 5 peaks | balanced | 4->0 | 0 | 4 |
| 5 peaks | par_dom | 4->0 | 0 | 4 |
| 10 peaks | osc_dom | 5->0 | 2 | 14 |
| 10 peaks | balanced | 5->0 | 0 | 6 |
| 10 peaks | par_dom | 5->0 | 0 | 6 |

**Key findings:**

1. **Parabolic suppression of oscillatory merging:** In the oscillator-dominated regime, 10 peaks produce 14 merging events (peaks oscillate through the detection threshold). In balanced and parabolic-dominated regimes, the same 10 peaks produce only 6 merges (monotonic disappearance).

2. **Balanced and parabolic-dominated are indistinguishable:** Both produce identical merge counts and zero oscillations. The oscillatory channel at H <= 0.5 is effectively invisible in multi-peak dynamics.

3. **No new merging motifs:** The hybrid does not create qualitatively new dynamics. It interpolates between oscillatory (rich transients) and parabolic (monotonic decay).

---

## 6. Results: Hybrid Horizon Behavior (Experiment 3)

### 6.1 Near-Horizon Peak Across Regimes

Gaussian peak reaching rho = 95 (near mobility ceiling rho_max = 100). 50K steps.

| Regime | D | H | Peak (init->final) | Hor Max Sites | Hor Lifetime | Oscillations |
|--------|---|---|-------------------|---------------|-------------|-------------|
| Pure osc | 0.0 | 1.0 | 95->50 | 15 | 8 | 9 |
| Osc-dom | 0.2 | 0.8 | 95->50 | 15 | 8 | 1 |
| Balanced | 0.5 | 0.5 | 95->50 | 15 | 7 | 0 |
| Par-dom | 0.8 | 0.2 | 95->50 | 15 | 6 | 0 |
| Pure par | 1.0 | 0.0 | 95->50 | 15 | 5 | 0 |

**Key findings:**

1. **Horizon size is regime-independent:** All regimes produce exactly 15 horizon sites. The initial condition determines the horizon extent, not the dynamics.

2. **Horizon lifetime increases with H:** Pure parabolic = 5 tracking samples, pure oscillatory = 8 tracking samples. The oscillatory channel sustains horizons 60% longer because the velocity inertia resists immediate dissolution.

3. **The oscillatory channel stabilizes horizons.** This is a new finding: while all structures eventually relax, the inertial channel extends horizon persistence. In the pure oscillatory case, the horizon oscillates (9 height oscillations), meaning density repeatedly approaches and retreats from the ceiling.

---

## 7. Results: Hybrid Inflation and Thinning (Experiment 4)

### 7.1 Peak at Wave Crest, Trough, and Node

Peak (h=20, sigma=15) on standing wave background (A=10, mode n=2), tested at three phases.

| Placement | Regime | Initial Height | Final Height | Oscillations |
|-----------|--------|---------------|--------------|-------------|
| Crest | osc_dom | 80.0 | 50.0 | 2 |
| Crest | balanced | 80.0 | 50.0 | 0 |
| Crest | par_dom | 80.0 | 50.0 | 0 |
| Trough | osc_dom | 60.0 | 50.0 | 3 |
| Trough | balanced | 60.0 | 50.0 | 0 |
| Trough | par_dom | 60.0 | 50.0 | 0 |
| Node | osc_dom | 70.3 | 50.0 | 1 |
| Node | balanced | 70.3 | 50.0 | 0 |
| Node | par_dom | 70.3 | 50.0 | 0 |

**Key findings:**

1. **Trough placement retains more oscillations:** In the osc-dominated regime, the trough peak shows 3 oscillations vs 2 for the crest. The trough (rho = 60, closer to rho_star) has a weaker restoring force from P_SY2, allowing oscillations to persist.

2. **Balanced and parabolic-dominated show no phase dependence:** All placements produce zero oscillations. The parabolic channel eliminates the phase-dependent dynamics entirely.

3. **No hybrid inflation or thinning motifs:** The parabolic channel does not produce sustained inflation or thinning in the hybrid regime — all configurations relax to rho_star. The oscillatory modulation of parabolic thinning is observed only in the osc-dominated regime, and even there it is weak (1-3 oscillations).

---

## 8. Results: 2D Hybrid Cosmology (Experiment 5)

### 8.1 2D Fields Across Regimes

128 x 128 grid, 20K steps.

| Configuration | Regime | Initial Std | Final Std | Drift | Clips |
|--------------|--------|-----------|-----------|-------|-------|
| Random field | osc_dom | 6.439 | ~0 | ~0 | 0 |
| Random field | balanced | 6.353 | ~0 | ~0 | 0 |
| Random field | par_dom | 6.268 | ~0 | ~0 | 0 |
| Directional + peak | osc_dom | 6.250 | ~0 | ~0 | 0 |
| Directional + peak | balanced | 6.247 | ~0 | ~0 | 0 |
| Directional + peak | par_dom | 6.244 | ~0 | ~0 | 0 |
| Radial peak | osc_dom | 4.701 | ~0 | ~0 | 0 |
| Radial peak | balanced | 4.701 | ~0 | ~0 | 0 |
| Radial peak | par_dom | 4.700 | ~0 | ~0 | 0 |

**Key findings:**

1. **All 2D hybrid regimes are stable.** Zero clips, zero drift, complete relaxation to rho_star across all mixing ratios and initial conditions.

2. **2D results are regime-insensitive.** At 20K steps, all regimes have fully relaxed. The relaxation rate differences visible in 1D (Section 10) are too small to matter at this timescale.

3. **The hybrid update preserves the P_SY2 guarantee:** rho_star is the global attractor in 2D regardless of the D/H ratio.

---

## 9. Results: Hybrid Phase Diagram (Experiment 6)

### 9.1 Structure Sweep

5-peak IC swept across D = 0.0 to 1.0 in steps of 0.1. 50K steps.

| D | H | Oscillations | Merges | Half-life (steps) |
|---|---|-------------|--------|-------------------|
| 0.0 | 1.0 | 15 | 64 | 1416 |
| 0.1 | 0.9 | 7 | 20 | 1404 |
| 0.2 | 0.8 | 2 | 16 | 1380 |
| 0.3 | 0.7 | 2 | 7 | 1368 |
| 0.4 | 0.6 | 1 | 5 | 1344 |
| 0.5 | 0.5 | 0 | 4 | 1332 |
| 0.6 | 0.4 | 0 | 4 | 1308 |
| 0.7 | 0.3 | 0 | 4 | 1296 |
| 0.8 | 0.2 | 0 | 4 | 1272 |
| 0.9 | 0.1 | 0 | 4 | 1260 |
| 1.0 | 0.0 | 0 | 4 | 1236 |

### 9.2 Horizon Sweep

Near-horizon peak (rho=95) swept across D = 0.0 to 1.0.

| D | H | Hor Max | Hor Lifetime | Oscillations |
|---|---|---------|-------------|-------------|
| 0.0 | 1.0 | 15 | 8 | 9 |
| 0.1 | 0.9 | 15 | 8 | 2 |
| 0.2 | 0.8 | 15 | 8 | 1 |
| 0.3 | 0.7 | 15 | 8 | 1 |
| 0.4 | 0.6 | 15 | 7 | 0 |
| 0.5 | 0.5 | 15 | 7 | 0 |
| 0.6 | 0.4 | 15 | 7 | 0 |
| 0.7 | 0.3 | 15 | 6 | 0 |
| 0.8 | 0.2 | 15 | 6 | 0 |
| 0.9 | 0.1 | 15 | 6 | 0 |
| 1.0 | 0.0 | 15 | 5 | 0 |

### 9.3 Phase Diagram Classification

The data reveals three distinct regimes with two critical thresholds:

**Regime 1: Oscillatory (D < 0.1)**
- Many oscillations (7-15)
- Many merging events (20-64)
- Rich transient structure
- Longest horizon lifetimes (8 samples)

**Regime 2: Transitional (0.1 <= D <= 0.4)**
- Few oscillations (1-2)
- Reduced merges (5-16)
- Damped oscillatory character
- Intermediate horizon lifetimes (7-8 samples)

**Regime 3: Parabolic (D >= 0.5)**
- Zero oscillations
- Minimal merges (4, exactly one per initial peak)
- Monotonic decay
- Shortest horizon lifetimes (5-7 samples)

**Critical thresholds:**
- **Oscillation death:** D_crit ~ 0.5. Oscillations vanish at D >= 0.5.
- **Merging saturation:** D_crit ~ 0.5. Merging events saturate at 4 (= number of detected peaks) for D >= 0.5.
- **Horizon transition:** Gradual. Lifetime decreases linearly from 8 to 5 as D increases from 0 to 1.

### 9.4 Relaxation Rate

The half-life decreases linearly with D:
- D = 0.0: half-life = 1416 steps
- D = 1.0: half-life = 1236 steps
- Ratio: 1236/1416 = 0.87

The parabolic channel accelerates relaxation by ~13% compared to pure oscillatory dynamics. This is a modest effect — the relaxation rate is dominated by the underlying P_SY2 restoring force, not the dynamical channel.

### 9.5 No Bifurcations or Chaos

The phase sweep reveals:
- **No blowups** at any D/H ratio
- **No positivity clips** at any ratio
- **No chaotic regime**: oscillation count decreases monotonically with D
- **No hysteresis**: the transition at D ~ 0.5 is smooth, not discontinuous
- **No new motifs**: the hybrid interpolates between the two pure regimes without producing qualitatively new behavior

---

## 10. Synthesis

### 10.1 The Parabolic Channel Dominates

The most striking finding is the asymmetry between channels: **the parabolic channel overwhelms the oscillatory channel.** Adding just D = 0.2 parabolic weight reduces oscillations from 8 to 2 (75% reduction). At D = 0.5, oscillations are completely suppressed.

This asymmetry arises because the parabolic channel provides direct, instantaneous density response to forces. The oscillatory channel introduces inertial delay through the velocity field. When both are present, the instantaneous response outpaces the inertial response, and the density reaches equilibrium before the velocity channel can generate significant oscillation.

### 10.2 Universal Relaxation Is Robust

All hybrid regimes — from pure oscillatory to pure parabolic — produce the same final state: uniform rho_star. Zero positivity clips across all experiments, all dimensions, all mixing ratios. The P_SY2 restoring force is the fundamental driver; the dynamical channel (parabolic, oscillatory, or hybrid) only affects the transient path.

### 10.3 Horizons Are Dynamically Enriched

The one area where the hybrid produces graded behavior is horizon dynamics. The oscillatory channel extends horizon lifetimes by 60% (5 vs 8 tracking samples). This is because:
- Near the ceiling, M(rho) -> 0, suppressing the parabolic response (which relies on M*Lap)
- The oscillatory velocity field v has inertia independent of M
- The penalty P_SY2 acts directly, but its effect on rho is delayed by the inertial channel

This means: **horizons persist longer when the oscillatory channel is stronger.** This is a genuine dynamical prediction of the hybrid cosmology.

### 10.4 No New Motifs

The hybrid does not produce qualitatively new structure formation motifs. It interpolates between:
- Oscillatory: rich transients, many merges, ringing relaxation
- Parabolic: monotonic decay, minimal merges, smooth relaxation

No parameter regime produces sustained structures, standing patterns, or self-organized criticality. The P_SY2 restoring force ensures universal relaxation regardless of the dynamical channel.

### 10.5 Relaxation Rate Scaling

The half-life varies only 13% across the full D range (1236-1416 steps). This confirms that relaxation is rate-limited by P_SY2, not by the dynamical channel. The P_SY2 restoring force alpha*gamma/rho_0 = 0.1 sets the fundamental timescale; D and H modulate only the transient character.

---

## 11. Phase Diagram Summary

```
D = 0.0  [OSCILLATORY]    15 osc, 64 merges, hor_life=8
  |
D = 0.1  [TRANSITIONAL]    7 osc, 20 merges, hor_life=8
  |
D = 0.2                     2 osc, 16 merges, hor_life=8
  |
D = 0.3                     2 osc,  7 merges, hor_life=8
  |
D = 0.4                     1 osc,  5 merges, hor_life=7
  |       ---- oscillation death threshold ----
D = 0.5  [PARABOLIC]        0 osc,  4 merges, hor_life=7
  |
D = 0.6                     0 osc,  4 merges, hor_life=7
  |
D = 0.7                     0 osc,  4 merges, hor_life=6
  |
D = 0.8                     0 osc,  4 merges, hor_life=6
  |
D = 0.9                     0 osc,  4 merges, hor_life=6
  |
D = 1.0  [PURE PARABOLIC]   0 osc,  4 merges, hor_life=5
```

Three key numbers:
- **D_crit = 0.5:** oscillation death
- **Relaxation rate:** varies only 13% across full range
- **Horizon lifetime:** varies 60% (5 to 8 samples) across full range

---

## 12. Implications for Event Density Ontology

### 12.1 The Two Cosmological Sectors Coexist But Do Not Compete Equally

The parabolic and oscillatory channels can operate simultaneously, but the parabolic channel dominates. At equal weight (D = H = 0.5), the system is already fully parabolic in character. This suggests that in an ED universe with both diffusive and inertial participation channels, the diffusive channel would control macroscopic structure formation while the inertial channel would be relevant only where diffusion is suppressed (near horizons).

### 12.2 Horizons as the Oscillatory Refuge

Near the mobility ceiling (rho -> rho_max), M -> 0 and the parabolic channel weakens. The oscillatory channel — which acts through velocity inertia independent of mobility — becomes relatively more important. This creates a natural partition:
- **Bulk dynamics:** parabolic-dominated (diffusion is fast)
- **Near-horizon dynamics:** oscillatory-enhanced (diffusion is suppressed)

This is a genuine architectural feature: the ED framework naturally produces dynamically distinct bulk and boundary regimes without introducing separate physics.

### 12.3 No New Motifs — The P_SY2 Guarantee

The hybrid cosmology confirms that P_SY2 is the fundamental force in ED cosmology. Regardless of the dynamical channel (parabolic, oscillatory, or any mixture), the unique minimum of the potential V(rho) = alpha*gamma*sqrt((rho - rho_star)^2 + rho_0^2) ensures universal relaxation.

For new motifs to emerge, the system would need:
1. **Multiple competing potentials** (not just a single P_SY2)
2. **Spatial dependence in rho_star** (creating heterogeneous equilibria)
3. **Nonlinear coupling between channels** (not just linear mixing D*RHS + H*v)

### 12.4 Unified Cosmological Architecture

The hybrid update rule provides a clean, tunable framework:
- A single parameter D (with H = 1 - D) interpolates between fully reversible (oscillatory) and fully irreversible (parabolic) dynamics
- The transition at D_crit = 0.5 is smooth, not a bifurcation
- Both channels respect positivity, energy bounds, and the P_SY2 attractor

This means the ED framework supports a unified cosmological architecture where the "stiffness" of the universe (how inertially it responds to forces) is a free parameter. The qualitative physics (universal relaxation, transient structure, horizons) is robust across the full parameter range.

---

## 13. Quantitative Summary

| Quantity | Value |
|----------|-------|
| Oscillation death threshold | D_crit = 0.5 |
| Pure oscillatory oscillations | 15 (5-peak IC) |
| D=0.2 oscillations | 2 (87% reduction) |
| D=0.5 oscillations | 0 (complete suppression) |
| Relaxation half-life range | 1236-1416 steps (13% variation) |
| Horizon lifetime range | 5-8 samples (60% variation) |
| Final energy (all regimes) | 0.0250 (= alpha*gamma*rho_0) |
| Positivity clips (all runs) | 0 |
| 2D mean drift (all regimes) | < 1e-7 |
| Phase diagram regimes | 3 (oscillatory, transitional, parabolic) |
| Bifurcations | 0 |
| New motifs | 0 |

---

## 14. Conclusions

1. **The parabolic channel dominates the oscillatory channel.** Adding D = 0.2 parabolic weight reduces oscillations by 87%. At D = 0.5, oscillations are fully suppressed.

2. **All hybrid regimes relax to the same ground state** (uniform rho_star, E = alpha*gamma*rho_0). The mixing ratio affects only transient dynamics.

3. **Horizon lifetime is the primary observable that varies with D/H.** Oscillatory-dominated regimes sustain horizons 60% longer than parabolic-dominated regimes.

4. **The oscillation death threshold is D_crit = 0.5.** Below this, the system is oscillatory; above, parabolic. The transition is smooth.

5. **Relaxation rate varies only 13%** across the full D range. The P_SY2 restoring force, not the dynamical channel, controls the timescale.

6. **No new motifs emerge from hybrid dynamics.** The hybrid interpolates between pure regimes without producing qualitatively new behavior.

7. **The ED framework supports a unified, tunable cosmological architecture.** A single mixing parameter D continuously interpolates between reversible and irreversible dynamics while preserving stability, positivity, and the universal attractor.

8. **Zero positivity clips** across all experiments (1D and 2D), all regimes, all initial conditions. The hybrid update is unconditionally safe.

---

## Appendix A: Code Reference

All experiments run from `ed_phys_hybrid.py` in this directory. Results stored in `results/hybrid_results.json` and `results/2d_*.npy`.

### Hybrid Update Implementation

```python
# Hybrid update core
dv = (1.0 / osc.tau) * (rhs - osc.zeta * v)
v_new = v + eta * dv
drho = D * rhs + H * v_new
rho_new = rho + eta * drho
```

When D=1, H=0: drho = rhs (parabolic).
When D=0, H=1: drho = v_new (oscillatory).

### Regime Definitions

```python
REGIMES = {
    "osc_dom":  HybridParams(D=0.2, H=0.8),
    "balanced": HybridParams(D=0.5, H=0.5),
    "par_dom":  HybridParams(D=0.8, H=0.2),
    "pure_osc": HybridParams(D=0.0, H=1.0),
    "pure_par": HybridParams(D=1.0, H=0.0),
}
```

---

## Appendix B: Phase Diagram Data

### Structure Sweep (5-peak IC, 50K steps)

| D | Oscillations | Merges | Half-life |
|---|-------------|--------|-----------|
| 0.0 | 15 | 64 | 1416 |
| 0.1 | 7 | 20 | 1404 |
| 0.2 | 2 | 16 | 1380 |
| 0.3 | 2 | 7 | 1368 |
| 0.4 | 1 | 5 | 1344 |
| 0.5 | 0 | 4 | 1332 |
| 0.6 | 0 | 4 | 1308 |
| 0.7 | 0 | 4 | 1296 |
| 0.8 | 0 | 4 | 1272 |
| 0.9 | 0 | 4 | 1260 |
| 1.0 | 0 | 4 | 1236 |

### Horizon Sweep (near-horizon peak, 50K steps)

| D | Hor Max Sites | Hor Lifetime | Oscillations |
|---|--------------|-------------|-------------|
| 0.0 | 15 | 8 | 9 |
| 0.1 | 15 | 8 | 2 |
| 0.2 | 15 | 8 | 1 |
| 0.3 | 15 | 8 | 1 |
| 0.4 | 15 | 7 | 0 |
| 0.5 | 15 | 7 | 0 |
| 0.6 | 15 | 7 | 0 |
| 0.7 | 15 | 6 | 0 |
| 0.8 | 15 | 6 | 0 |
| 0.9 | 15 | 6 | 0 |
| 1.0 | 15 | 5 | 0 |
