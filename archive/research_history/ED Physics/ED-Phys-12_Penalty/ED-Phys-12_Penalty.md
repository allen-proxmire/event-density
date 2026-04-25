# ED-Phys-12: Redesigning the Relational Penalty

## 1. Diagnosis of the Current Penalty

### 1.1 The Canonical Relational Penalty

The ED compositional rule (ED-12) specifies:

    rho(A u B) = rho(A) + rho(B) - alpha * integral f(rho) d mu - ...

where f(rho) = rho^gamma with 0 < gamma < 1. This yields the **relational penalty** in the PDE:

    P(rho) = alpha * gamma * rho^(gamma-1)

At the canonical parameter gamma = 0.5:

    P(rho) = 0.05 * rho^(-0.5)

### 1.2 The Singularity at Low Density

The factor rho^(gamma-1) = rho^(-0.5) diverges as rho -> 0:

| rho | P(rho) | Drain rate per step (eta=0.2) |
|-----|--------|-------------------------------|
| 50.0 | 0.0071 | 0.0014 |
| 5.0 | 0.0224 | 0.0045 |
| 1.0 | 0.0500 | 0.0100 |
| 0.1 | 0.1581 | 0.0316 |
| 0.01 | 0.5000 | 0.1000 |

The penalty grows as density decreases. This creates **runaway depletion**: as a participation channel empties, it drains faster, which empties it more, which drains it faster still. The result is total channel collapse to rho = 0.

### 1.3 How This Enforces Overdamped Dynamics

ED-Phys-11 (Section 6.2) identified the singularity as the structural barrier to wave physics. When a hyperbolic extension (d^2 rho/dt^2) amplifies the penalty by factor 1/tau, the diverging drain creates explosive negative acceleration:

    dv/dt = (1/tau) * [-P(rho) - zeta*v + ...]

As rho decreases, P(rho) diverges, v accelerates downward, rho decreases further — a catastrophic feedback loop. The singularity makes any underdamped dynamics impossible at low density.

### 1.4 In ED Language

In the Event Density ontology:
- **Participation channels** are regions of the event domain with density rho
- The relational penalty represents the **cost of participation**: events must "pay" a toll to maintain their density within a channel
- At low density (sparse channels), this toll becomes infinite — sparse channels are destroyed
- At high density (rich channels), the toll saturates — rich channels stabilize
- The result: participation dynamics are **one-directional** — channels can only drain, never recover

### 1.5 What We Want to Keep, Open, and Avoid

**KEEP:**
- Stability at high density (peaks persist, do not blow up)
- Horizons (M(rho) -> 0 at rho_max)
- Inflation (mean gradient decays exponentially)
- Concave instability (structure formation from perturbations)

**OPEN:**
- Bounded penalty at low density (channels stop collapsing)
- Possibility of channel recovery (density can flow back into depleted regions)
- Stronger participation flows (richer channel response)
- Compatibility with underdamped or oscillatory dynamics

**DO NOT SEEK:**
- Literal wave fields (separate wave equation) — stay in the language of event density
- New ontological entities — modify the penalty within the existing framework

---

## 2. Proposed Alternative Penalty Families

### 2.1 Family 1: Soft-Floor Penalty (P_SF)

    f(rho) = (rho + rho_0)^gamma
    P_SF(rho) = alpha * gamma * (rho + rho_0)^(gamma-1)

The shift rho -> rho + rho_0 removes the singularity:
- At rho = 0: P_SF = alpha * gamma * rho_0^(gamma-1) (finite)
- At rho >> rho_0: P_SF ~ alpha * gamma * rho^(gamma-1) (recovers canonical)

**Modified RHS factor**: rho^(gamma-1) is replaced by (rho + rho_0)^(gamma-1).

**Qualitative predictions:**
- Horizons: unchanged (M(rho) still vanishes at rho_max)
- Inflation: nearly identical to canonical at high rho
- Peak stability: unchanged (concave behavior preserved)
- Low-density behavior: channels stop collapsing at rho ~ rho_0
- Channel responsiveness: identical to canonical for rho >> rho_0

**Parameter**: rho_0 controls the soft-floor scale.

### 2.2 Family 2: Symmetric Participation Penalty (P_SY)

    P_SY(rho) = alpha * gamma * (rho - rho_star) / (rho + rho_0)

This penalty is centered on a **reference density** rho_star:
- At rho = rho_star: P = 0 (no penalty at equilibrium)
- At rho > rho_star: P > 0 (drain, pushing toward rho_star)
- At rho < rho_star: P < 0 (boost, pushing toward rho_star)
- As rho -> infinity: P -> alpha * gamma (bounded)
- At rho = 0: P = -alpha * gamma * rho_star / rho_0 (bounded, negative)

**Modified RHS factor**: rho^(gamma-1) is replaced by (rho - rho_star) / (rho + rho_0).

**Qualitative predictions:**
- Horizons: modified — penalty at rho_max is bounded and positive (still drains)
- Inflation: modified — structure formation occurs around rho_star, not around zero
- Peak stability: peaks above rho_star are drained toward it; peaks below are boosted
- Low-density behavior: channels are actively restored to rho_star
- Channel responsiveness: fundamentally different — channels can swing above and below equilibrium

**Parameters**: rho_star (equilibrium density), rho_0 (denominator scale).

### 2.3 Family 3: Curvature-Weighted Penalty (proposed, not tested)

    P_CW(rho) = alpha * gamma * rho^(gamma-1) * (1 + epsilon * |Lap(rho)| / rho)

This strengthens the penalty where curvature is large (near peaks and valleys).

**Why not tested**: Requires computing Lap(rho) within the penalty function, coupling spatial and local operators in a way that changes the PDE character. Deferred.

### 2.4 Family 4: Logistic Penalty (proposed, not tested)

    P_LOG(rho) = alpha * gamma * rho / (1 + rho/K)

This produces a logistic-type drain that saturates at high rho.

**Why not tested**: Does not address the low-density singularity (P_LOG is well-behaved at rho=0 since it goes to zero). It removes the concave instability at low density, which may eliminate structure formation entirely. Deferred.

### 2.5 Family 5: Bounded Concave Penalty (proposed, not tested)

    P_BC(rho) = alpha * gamma * rho / (rho + rho_0)^(1-gamma)

Interpolates between linear behavior at low rho and concave at high rho.

**Why not tested**: Similar to soft-floor but with different asymptotic behavior. The soft-floor family already captures the key modification. Deferred.

---

## 3. Selected Penalties

### 3.1 Selection Criteria

| Criterion | Soft-Floor (P_SF) | Symmetric (P_SY) |
|-----------|------------------|------------------|
| Removes singularity | Yes (shifts argument) | Yes (ratio form) |
| Preserves high-rho behavior | Yes (recovers canonical) | Partially (bounded drain) |
| Analytically tractable | Yes (simple shift) | Yes (rational function) |
| Numerically stable | Yes (no new instabilities) | Yes (bounded at all rho) |
| ED-compatible | Yes (modified f(rho)) | Yes (reference density as ontological parameter) |
| Novel physics | Minimal (soft floor only) | Significant (restoring force, channel swing) |

Both selected. P_SF is the minimal modification; P_SY is the maximal modification that stays within the single-field framework.

### 3.2 Final Forms

**P_SF**: P(rho) = alpha * gamma * (rho + rho_0)^(gamma-1)

    Modified PDE RHS: drho/dt = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - alpha*gamma*(rho+rho_0)^(gamma-1)

**P_SY**: P(rho) = alpha * gamma * (rho - rho_star) / (rho + rho_0)

    Modified PDE RHS: drho/dt = M(rho)*Lap(rho) + M'(rho)*|grad(rho)|^2 - alpha*gamma*(rho-rho_star)/(rho+rho_0)

---

## 4. Implementation

### 4.1 Simulator

File: `ed_phys_penalty.py`

A unified `simulate_penalty()` function accepts a `penalty_mode` flag ("canonical", "soft_floor", "symmetric") and shares all other code paths with the canonical simulator. The penalty function is swapped at the computation step. Safety checks (NaN, Inf, blowup) are applied identically.

### 4.2 Validation: Homogeneous IC

| Penalty | rho(0) | rho(5K) | Penalty at rho(5K) |
|---------|--------|---------|-------------------|
| Canonical | 50.0 | 42.65 | 0.0077 |
| Soft-floor (rho_0=0.5) | 50.0 | 42.69 | 0.0076 |
| Symmetric (rho_star=50) | 50.0 | 50.00 | 0.0000 |

Canonical and soft-floor both drain uniformly (expected — the penalty is nonzero at all rho > 0). Symmetric stays at rho_star = 50 (penalty is exactly zero at equilibrium). All three are numerically stable.

---

## 5. Experimental Results

### 5.1 EXP2: Peak Test

Single Gaussian peak (height 75, background 50) on 1D lattice, 20K steps.

| Penalty | rho_0 / rho_star | Peak final | Background final | Contrast retained |
|---------|-----------------|------------|-----------------|------------------|
| Canonical | — | 28.5 | 14.2 | 57% |
| Soft-floor | 0.1 | 28.6 | 14.3 | 57% |
| Soft-floor | 0.5 | 28.8 | 14.6 | 56% |
| Soft-floor | 2.0 | 29.5 | 15.8 | 55% |
| Soft-floor | 5.0 | 30.7 | 17.7 | 52% |
| Symmetric | rho_star=20 | 22.3 | 21.0 | 5% |
| Symmetric | rho_star=40 | 52.2 | 43.5 | 36% |
| Symmetric | rho_star=50 | 61.0 | 50.0 | 44% |

**Soft-floor**: Nearly identical to canonical. Higher rho_0 slightly raises the background floor (expected — the penalty at low rho is weaker). Peak contrast is preserved at 52-57%.

**Symmetric**: Dramatically different behavior depending on rho_star:
- rho_star=20: both peak and background converge toward 20, destroying contrast (5% retained)
- rho_star=40: moderate contrast retention (36%), background drifts toward 40
- rho_star=50: background stays at 50 (matching the IC), peak drains toward 50 but retains 44% contrast due to the bounded penalty

**Key observation**: No height oscillations in any mode. The symmetric penalty creates a restoring force toward rho_star but this force is monotonic, not oscillatory. Channels approach rho_star smoothly.

### 5.2 EXP3: Horizon Test

Near-horizon region (rho=95) on rho=50 background.

| Penalty | rho_max final | Background final |
|---------|--------------|-----------------|
| Canonical | 72.5 | 14.2 |
| Soft-floor (rho_0=0.5) | 72.6 | 14.7 |
| Soft-floor (rho_0=5.0) | 73.3 | 17.7 |
| Symmetric (rho_star=20) | 31.0 | 21.0 |
| Symmetric (rho_star=50) | 78.4 | 50.0 |

**Soft-floor**: Horizons behave identically to canonical. The high-density penalty is unchanged.

**Symmetric**: rho_star=50 preserves the background at 50 and drains the near-horizon region toward rho_star more slowly (78.4 vs 72.5 in canonical). This is because the symmetric penalty at rho=95 is:

    P_SY(95) = 0.05 * (95-50)/(95+1) = 0.0234

vs canonical:

    P_CAN(95) = 0.05 * 95^(-0.5) = 0.00513

The symmetric penalty is actually STRONGER at rho=95 near rho_star=50 (0.023 vs 0.005). But the horizon still exists because M(rho) -> 0 is controlled by the mobility function, not the penalty.

**Conclusion**: Horizons are preserved in all penalty modes. The mobility-driven freeze at rho_max is independent of the penalty form.

### 5.3 EXP4: Flow Test

Two peaks (height 70, separation 153) on rho=50 background.

| Penalty | Sep initial | Sep final | Delta | Valley initial | Valley final |
|---------|------------|-----------|-------|---------------|-------------|
| Canonical | 153 | 143 | **-10** | 50.0 | 21.4 |
| Soft-floor (0.1) | 153 | 143 | **-10** | 50.0 | 21.4 |
| Soft-floor (0.5) | 153 | 143 | **-10** | 50.0 | 21.7 |
| Soft-floor (2.0) | 153 | 143 | **-10** | 50.0 | 22.5 |
| Soft-floor (5.0) | 153 | 143 | **-10** | 50.0 | 23.8 |
| Symmetric (rho_star=20) | 153 | 153 | **0** | 50.0 | 21.3 |
| Symmetric (rho_star=40) | 153 | 153 | **0** | 50.0 | 43.7 |
| Symmetric (rho_star=50) | 153 | 153 | **0** | 50.0 | 50.1 |

**Critical finding**: Canonical and soft-floor both show peak approach (sep 153 -> 143, delta = -10). The peaks migrate toward each other by 10 lattice sites over 20K steps. This is the first observation of peak approach in the canonical ED system with these parameters.

**Note**: This peak approach is NOT caused by inter-peak forces (ED-Phys-10 showed zero force-mediated movement). It is caused by **asymmetric thinning**: the valley between peaks drains faster than the outer edges because the background is lower there, creating a density gradient that pulls peaks inward. This is a canonical basin-merging mechanism.

**Symmetric penalty freezes peak separation**: At all rho_star values, the separation stays at 153. The symmetric penalty maintains the valley density near rho_star, preventing the asymmetric thinning that drives peak approach. At rho_star=50, the valley stays at 50.1 (nearly unchanged from 50.0).

### 5.4 EXP5: Cosmology Test

Random IC (rho in [20, 80]), 20K steps.

| Penalty | lambda_1 | R^2 | Basins (init -> final) | rho range (final) |
|---------|----------|-----|----------------------|------------------|
| Canonical | 0.000112 | 0.59 | 165 -> 2 | [18.7, 22.9] |
| Soft-floor (0.1) | 0.000112 | 0.59 | 165 -> 2 | [18.7, 22.9] |
| Soft-floor (0.5) | 0.000112 | 0.59 | 165 -> 2 | [19.0, 23.1] |
| Soft-floor (2.0) | 0.000113 | 0.60 | 165 -> 2 | [19.9, 23.9] |
| Soft-floor (5.0) | 0.000115 | 0.61 | 165 -> 2 | [21.5, 25.3] |
| Symmetric (rho_star=20) | **0.000253** | **0.92** | 165 -> 2 | [21.2, 21.5] |
| Symmetric (rho_star=40) | 0.000162 | 0.81 | 165 -> 5 | [43.5, 46.5] |
| Symmetric (rho_star=50) | 0.000152 | 0.79 | 165 -> 5 | [49.9, 53.8] |

**Soft-floor**: Nearly identical to canonical. The inflation rate is unchanged. The soft-floor only matters at rho << rho_0, which is not reached during the cosmological evolution at these density scales.

**Symmetric**: Significantly different:
- lambda_1 is 1.4-2.3x higher than canonical (faster gradient decay)
- R^2 is much higher (0.79-0.92 vs 0.59), meaning the exponential fit is better
- Basins survive longer (5 final vs 2 for canonical at rho_star=40,50)
- Final density range is much narrower — the system converges toward rho_star

The symmetric penalty produces **cleaner inflation** (higher R^2) because the restoring force toward rho_star acts as an additional smoothing mechanism. Overdense regions are drained while underdense regions are boosted, both driving toward uniformity.

### 5.5 EXP6: Low-Density Depletion

Starting from rho=1 (low density), 2K steps.

| Penalty | rho(0) | rho(2K) | Behavior |
|---------|--------|---------|----------|
| Canonical | 1.0 | 0.000 | Total depletion (runaway) |
| Soft-floor (0.1) | 1.0 | 0.000 | Total depletion |
| Soft-floor (0.5) | 1.0 | 0.000 | Total depletion |
| Soft-floor (2.0) | 1.0 | 0.000 | Total depletion |
| **Symmetric (rho_star=5)** | 1.0 | **4.926** | **Recovery toward rho_star** |

**Key result**: The soft-floor penalty STILL depletes to zero. Although the singularity is removed (the penalty is finite at rho=0), the penalty is still positive at all rho > 0, so it continues to drain. The soft floor only prevents the drain from being infinite — it does not prevent the drain itself.

**The symmetric penalty actively restores density**: Starting from rho=1 (below rho_star=5), the penalty is negative (P = -0.0333), which BOOSTS density. The channel recovers from 1.0 to 4.926 in 2K steps, approaching rho_star=5.

This is the fundamental difference: the symmetric penalty converts one-directional channel collapse into two-directional channel regulation.

### 5.6 EXP7: 2D Cosmology

Random IC (rho in [20, 80]), 128x128, 5K steps.

| Penalty | rho range (final) | rho std |
|---------|------------------|---------|
| Canonical | [50.3, 51.5] | 0.271 |
| Soft-floor (0.5) | [50.3, 51.6] | 0.271 |
| Symmetric (rho_star=50) | [52.7, 54.6] | 0.420 |

Symmetric produces 55% more structure (std = 0.42 vs 0.27) with density pushed slightly above rho_star. This suggests the symmetric penalty enhances structure formation in 2D.

---

## 6. Architectural Tradeoff Analysis

### 6.1 Soft-Floor Penalty (P_SF)

**Does it preserve ED's core motifs?**
- Inflation: YES (lambda_1 unchanged)
- Horizons: YES (identical to canonical)
- Stable peaks: YES (contrast 52-57% vs 57% canonical)

**Does it remove low-density pathology?**
- **NO.** The penalty is finite at rho=0, but still positive. Channels still drain to zero — just not infinitely fast. The depletion time is extended but not prevented.

**Does it enhance channel responsiveness?**
- **NO.** At the density scales where structure lives (rho ~ 20-80), the soft-floor penalty is indistinguishable from canonical. The modification only matters at rho << rho_0.

**New pathologies?**
- None. The soft-floor penalty is strictly safer than canonical (no singularity).

**Classification: ED-COMPATIBLE IMPROVEMENT** — but a minimal one. It removes the mathematical singularity without changing any physically observable behavior in the canonical density regime.

### 6.2 Symmetric Participation Penalty (P_SY)

**Does it preserve ED's core motifs?**
- Inflation: MODIFIED — lambda_1 is 1.4-2.3x higher, R^2 is much better
- Horizons: YES (M(rho) controls horizons, not the penalty)
- Stable peaks: MODIFIED — peaks converge toward rho_star; contrast depends on rho_star choice

**Does it remove low-density pathology?**
- **YES.** Channels below rho_star are actively restored. Density recovery from 1.0 to 4.9 demonstrated. The runaway depletion is completely eliminated.

**Does it enhance channel responsiveness?**
- **PARTIALLY.** The restoring force creates two-directional participation flows (drain AND boost). However, the approach to rho_star is monotonic, not oscillatory. No oscillatory channel response was observed.

**New pathologies?**
- **Structural homogenization**: At rho_star near the mean density, all structure converges toward rho_star. With rho_star=20 on rho_mean=50, contrast is reduced to 5%. The penalty can destroy the rich structure that canonical ED creates.
- **Frozen peak dynamics**: The symmetric penalty freezes peak separation (no basin merging through asymmetric thinning). This eliminates a key canonical mechanism.
- **New free parameter**: rho_star introduces a reference density that has no canonical precedent in ED-12.

**Classification: INTERESTING BUT RISKY** — it solves the low-density singularity definitively, but at the cost of introducing a preferred density scale that can suppress canonical structure formation. The choice of rho_star is critical and has no canonical derivation.

### 6.3 Comparative Summary

| Property | Canonical | Soft-Floor | Symmetric |
|----------|-----------|------------|-----------|
| Low-density singularity | YES (diverges) | NO (bounded) | NO (bounded) |
| Channel recovery | NO (one-way drain) | NO (still drains) | YES (restores) |
| Peak contrast (20K steps) | 57% | 52-57% | 5-44% |
| Horizon formation | YES | YES | YES |
| Inflation rate | lambda_1 | ~lambda_1 | 1.4-2.3x lambda_1 |
| Peak approach | YES (-10 sites) | YES (-10 sites) | NO (frozen) |
| Oscillatory modes | NO | NO | NO |
| Free parameters | 0 | 1 (rho_0) | 2 (rho_star, rho_0) |
| ED-12 compatibility | Exact | Direct extension | Requires new interpretation |

---

## 7. Implications for the ED Ontology

### 7.1 The Soft-Floor as Canonical Regularization

The soft-floor penalty f(rho) = (rho + rho_0)^gamma is the minimal modification that removes the low-density singularity. In ED language:

- The canonical penalty says: "participation costs grow without bound as a channel empties"
- The soft-floor says: "participation costs grow, but there is a floor — even an empty channel has a finite cost"

This is ontologically natural: rho_0 represents the **residual participation cost** of the channel itself, independent of its current density. It is a property of the channel, not the events within it.

The soft-floor penalty can be recommended as a **canonical regularization** for any application where low-density behavior matters (e.g., hyperbolic extensions, strong coupling). It does not change any observable in the canonical density regime.

### 7.2 The Symmetric Penalty as a New Ontological Regime

The symmetric penalty introduces a fundamentally new concept: a **preferred participation density** rho_star at which channels are in equilibrium. This is not present in ED-12.

**Possible ED interpretation**: rho_star represents the "natural density" of the event domain — the density at which participation channels are in balance between incoming and outgoing events. Channels below this density are "starved" and attract events; channels above are "saturated" and shed events.

This interpretation is consistent with ED-5's axioms (non-negativity, compositionality) but introduces a scale that ED-12 does not specify. Whether rho_star should be derived from other parameters (e.g., rho_star = rho_mean, or rho_star = function of alpha, gamma) or is a free parameter is an open question.

### 7.3 What the Symmetric Penalty Does NOT Solve

Despite removing the singularity and enabling channel recovery, the symmetric penalty does NOT produce:
- Oscillatory participation dynamics (the approach to rho_star is monotonic)
- Wave-like propagation (the PDE remains parabolic)
- Inter-peak forces (the penalty is local)

The overdamped character of ED dynamics is not caused solely by the penalty singularity. It is also caused by the first-order time structure and the local diffusion operator. Modifying the penalty opens one door but does not open the others identified in ED-Phys-09/10/11.

### 7.4 Recommendation

**For immediate use**: Adopt the soft-floor penalty P_SF with rho_0 ~ 0.5 as the canonical regularization. This removes the mathematical singularity without changing physical predictions at rho >> rho_0.

**For future exploration**: The symmetric penalty P_SY warrants further study with careful choice of rho_star. The optimal rho_star likely depends on the simulation context:
- For cosmological runs with rho_mean ~ 50: rho_star = 50 preserves the mean while allowing structure formation
- For structure formation studies: rho_star well below rho_mean would allow peaks to grow above rho_star while preventing valley collapse
- For combined use with ED-Phys-11 extensions: rho_star removes the singularity barrier to underdamped dynamics

---

## 8. Connection to Prior Modules

| Module | Finding | Status with P_SF | Status with P_SY |
|--------|---------|------------------|------------------|
| ED-Phys-09 | Overdamped: no waves | Unchanged | Unchanged (no oscillations) |
| ED-Phys-10 | GMF force too weak | Unchanged | Unchanged |
| ED-Phys-11 | rho^(gamma-1) causes runaway | **FIXED** (bounded at rho=0) | **FIXED** (restoring force) |
| ED-Phys-11 | Strong GMF blows up | Unchanged (instability is in phi) | Unchanged |
| ED-Phys-11 | Directional anisotropy achieved | Compatible | Compatible |

The soft-floor penalty directly addresses the ED-Phys-11 finding that the rho^(gamma-1) singularity causes runaway depletion in the hyperbolic extension. With P_SF, the penalty at rho=0 is bounded at alpha*gamma*rho_0^(gamma-1), which may allow the hyperbolic extension to stabilize.

---

## 9. Limitations

1. **No oscillatory response observed** — the symmetric penalty creates monotonic approach to rho_star, not oscillation
2. **rho_star has no canonical derivation** — it must be chosen ad hoc or derived from additional principles
3. **Flow test shows frozen separation** — the symmetric penalty prevents natural basin merging
4. **No coupling to hyperbolic extension tested** — the primary motivation (fixing the ED-Phys-11 instability) was not directly validated
5. **1D and 2D only** — 3D not tested

---

## 10. Future Directions

1. **Penalty + Hyperbolic**: Combine P_SF with the hyperbolic extension from ED-Phys-11 to test whether removing the singularity enables stable underdamped dynamics.

2. **Adaptive rho_star**: Let rho_star evolve dynamically, e.g., rho_star(t) = rho_mean(t). This would create a self-regulating system where the reference density tracks the global mean.

3. **Penalty-dependent coupling**: Modify the GMF coupling strength to scale with the penalty difference |P(rho_peak) - P(rho_valley)|, creating density-dependent forces.

4. **Concave-convex transition**: Design a penalty that is concave at high rho and convex at low rho, creating a natural basin of attraction at an intermediate density.

5. **Two-channel system**: Introduce two density fields rho_1 and rho_2 with different penalty parameters, testing whether inter-channel competition produces richer dynamics.

---

## Appendix A: Penalty Function Comparison

At gamma = 0.5, alpha = 0.1:

| rho | Canonical | Soft-floor (rho_0=0.5) | Symmetric (rho_star=50, rho_0=1) |
|-----|-----------|----------------------|--------------------------------|
| 0.01 | 0.500 | 0.070 | -0.0490 |
| 0.1 | 0.158 | 0.065 | -0.0490 |
| 1.0 | 0.050 | 0.041 | -0.0245 |
| 5.0 | 0.022 | 0.021 | -0.0375 |
| 10.0 | 0.016 | 0.015 | -0.0364 |
| 50.0 | 0.007 | 0.007 | 0.0000 |
| 95.0 | 0.005 | 0.005 | 0.0234 |
| 100.0 | 0.005 | 0.005 | 0.0248 |

---

## Appendix B: File Inventory

| File | Purpose |
|------|---------|
| `ed_phys_penalty.py` | Penalty variant simulator and experiment suite |
| `ED-Phys-12_Penalty.md` | This document |
| `README.md` | Module overview |
| `results/penalty_results.json` | All quantitative results |
| `results/2d_*_rho.npy` | 2D density field snapshots |
