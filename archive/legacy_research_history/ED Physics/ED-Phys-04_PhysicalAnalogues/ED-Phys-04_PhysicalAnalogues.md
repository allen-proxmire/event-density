# ED-Phys-04: Physical Analogues — Mapping ED Variables to Physics

## Canonical Lineage

| Source | Role in This Document |
|--------|----------------------|
| ED-5 | Ontological grounding: becoming, events, density as primitive |
| ED-12 | Compositional rule: three penalty terms, coarse-grained variables, epoch dynamics |
| ED-12.5 | Nonlinear diffusion form, mobility function, Friedmann analogue, horizon/Rindler conditions |
| ED-Phys-01 | PDE: d(rho)/dt = M(rho)*Lap(rho) + M'(rho)*\|grad(rho)\|^2 - alpha*gamma_exp*rho^(gamma_exp-1) |
| ED-Phys-03 | Simulation data: measured lambda_1, lambda_2, scale factor growth, basin dynamics, structure stabilization |

---

## 1. The Mapping Problem

ED begins with a single primitive — **becoming** — and constructs everything from it. The density field rho(x,t) is not a priori energy, matter, curvature, or any standard physical quantity. It is the **intensity of becoming** at a location.

The task of this document is to identify which standard physical quantities ED variables correspond to, evaluate each mapping's strength, and flag degeneracies where multiple interpretations are consistent with the mathematics.

### Mapping Criteria

Each candidate mapping is evaluated on five dimensions:

1. **Ontological consistency** (ED-5): Does the mapping respect the primitive status of becoming?
2. **PDE consistency** (ED-Phys-01): Is the mapping compatible with the dynamical equation?
3. **Cosmological consistency** (ED-12, ED-12.5): Does the mapping reproduce known cosmological behavior?
4. **Simulation consistency** (ED-Phys-03): Does the mapping match measured diagnostics?
5. **Uniqueness**: Is this the only viable mapping, or are there alternatives?

### Mapping Types

| Type | Definition |
|------|-----------|
| **Local** | Defined at each lattice site independently: rho(x), Lap(rho)(x) |
| **Relational** | Defined between neighboring sites: grad(rho), gradient direction |
| **Global** | Defined over the entire lattice: Sum(rho), mean(rho), basin count |

---

## 2. Analogue 1: rho(x,t) — The Density Field

### 2.1 Candidate Mappings

#### (A) Energy density (rho_phys ~ rho_ED)

**Justification:** In standard cosmology, energy density rho drives the Friedmann equation H^2 = (8*pi*G/3)*rho. ED-12.5 provides a Friedmann analogue: d(rho_mean)/dt = -Gamma(rho_mean). If rho_ED maps to rho_phys, the thinning d(rho_mean)/dt < 0 corresponds directly to the dilution of energy density during cosmic expansion.

**PDE consistency:** The thinning relation d(rho_mean)/dt = -lambda_2 * G^2 (confirmed with lambda_2 = 9.95 in 1D, 3.83 in 2D) mirrors the Friedmann continuity equation d(rho)/dt + 3H*(rho + p) = 0, with G^2 playing the role of 3H*(rho + p).

**Strengths:**
- Direct correspondence with Friedmann dynamics
- Thinning rate matches quadratic gradient dependence
- Non-negative (axiom A1) matches non-negative energy density

**Weaknesses:**
- In standard physics, energy density has units and couples to geometry via Einstein's equations; ED has no geometry a priori
- rho_ED measures "intensity of becoming" — energy is only one aspect of becoming

**Mapping type:** Local, one-to-one at each site.

#### (B) Scalar field amplitude (rho_ED ~ phi)

**Justification:** The PDE d(rho)/dt = M(rho)*Lap(rho) + ... resembles a nonlinear scalar field equation. During inflation, the gradient penalty produces exponential smoothing reminiscent of slow-roll dynamics.

**PDE consistency:** The mobility M(rho) introduces density-dependent diffusion, which is more general than a standard Klein-Gordon field. However, in the high-rho, small-gradient limit, the PDE reduces to a diffusion equation — not a wave equation — so rho behaves like a diffusing condensate, not an oscillating field.

**Strengths:**
- Inflation dynamics from gradient smoothing
- No need for a separate inflaton potential — the compositional rule provides it

**Weaknesses:**
- rho is always positive (axiom A1); standard scalar fields can be negative
- The PDE is purely dissipative (no wave-like solutions without additional terms)
- No direct mechanism for rho oscillations (reheating analogue would require modification)

**Mapping type:** Local.

#### (C) Curvature potential (rho_ED ~ Phi_grav)

**Justification:** In Newtonian gravity, the gravitational potential Phi satisfies Lap(Phi) = 4*pi*G*rho. In the ED PDE, the diffusion term M(rho)*Lap(rho) plays a smoothing role analogous to gravitational potential relaxation. High rho corresponds to deep potential wells.

**Weaknesses:**
- The sign is inverted: in gravity, overdensities create negative potential wells; in ED, overdensities have positive rho
- Curvature potential is typically signed; rho is non-negative
- Better suited as an analogy for the *source* of curvature, not curvature itself

**Mapping type:** Local.

### 2.2 Assessment

| Mapping | Ontological | PDE | Cosmological | Simulation | Uniqueness |
|---------|------------|-----|-------------|-----------|-----------|
| Energy density | Strong | Strong | Strong | Strong | Primary candidate |
| Scalar field | Moderate | Moderate | Strong (inflation) | Moderate | Alternative for inflation epoch |
| Curvature potential | Weak | Weak (sign issue) | Weak | Weak | Disfavored |

**Recommendation:** rho <-> energy density is the **primary mapping**, with the caveat that ED's rho is more fundamental than energy — it is the ontological substrate from which energy (as a conserved quantity) would need to be derived, not assumed.

---

## 3. Analogue 2: |grad(rho)| — Gradient Magnitude

### 3.1 Candidate Mappings

#### (A) Curvature magnitude (|grad(rho)| ~ |R| or |K|)

**Justification (ED-12):** Gradients in rho represent differences in the intensity of becoming between neighboring regions. In GR, spacetime curvature quantifies the inhomogeneity of the gravitational field. ED-12 explicitly identifies the gradient penalty with the smoothing of spacetime during inflation.

**PDE consistency:** The gradient penalty g(u) = u^2 in the compositional rule penalizes spatial inhomogeneity quadratically — this is structurally identical to the Ricci scalar R being quadratic in first derivatives of the metric.

**Simulation evidence (ED-Phys-03):**
- Exponential gradient decay (G(t) = G(0)*exp(-lambda_1*t)) corresponds to the exponential flattening of spacetime curvature during inflation
- The measured lambda_1 = 0.271 (1D), 0.726 (2D) sets the inflation rate

**Strengths:**
- Direct structural parallel with curvature
- Inflation correspondence is quantitatively confirmed
- Gradient-free state (G=0) corresponds to flat spacetime

**Weaknesses:**
- Curvature in GR is a tensor; |grad(rho)| is a scalar — this is a magnitude-only mapping
- No directional information (missing the tensor character of Riemann curvature)

#### (B) Force magnitude (|grad(rho)| ~ |F|)

**Justification:** In many physical systems, forces are proportional to field gradients: F = -grad(Phi). If rho is an energy-like potential, |grad(rho)| is the force driving becoming from high-density to low-density regions.

**PDE consistency:** The mobility-weighted flux J = M(rho)*grad(rho) is exactly the "force" driving the diffusion. The flux vanishes when either the gradient vanishes (no force) or the mobility vanishes (horizon/saturation).

**Strengths:**
- Natural interpretation of the diffusion flux
- Force vanishes at horizons (M -> 0), consistent with causal decoupling

**Weaknesses:**
- In ED, there are no pre-existing objects for forces to act *on* — forces emerge relationally, not as applied to particles

#### (C) Information gradient

**Justification (ED-5):** Becoming has structure; regions with different rho are informationally distinct. |grad(rho)| measures how quickly the character of becoming changes across space — an information-theoretic gradient.

**Strengths:**
- Ontologically clean: information about becoming is a natural ED concept
- No need to import dynamical concepts (force, curvature) from standard physics

**Weaknesses:**
- Less directly testable; information is not a standard observable in cosmology

### 3.2 Assessment

| Mapping | Ontological | PDE | Cosmological | Simulation | Uniqueness |
|---------|------------|-----|-------------|-----------|-----------|
| Curvature magnitude | Moderate | Strong | Strong | Strong | Primary candidate |
| Force magnitude | Moderate | Strong (flux) | Moderate | Moderate | Co-primary |
| Information gradient | Strong | Moderate | Weak | Weak | Conceptually clean but less testable |

**Recommendation:** |grad(rho)| maps to **curvature magnitude** in the cosmological context and **force/flux** in the dynamical context. These are two aspects of the same mathematical quantity.

---

## 4. Analogue 3: Lap(rho) — Laplacian / Local Curvature Sign

### 4.1 Candidate Mappings

#### (A) Local curvature sign (proto-gravity)

**Justification:** In the PDE, the term M(rho)*Lap(rho) is the primary driver of dynamics:
- Lap(rho) > 0 at local minima: rho is lower than neighbors, so density flows *in* (convergence, gravitational attraction analogue)
- Lap(rho) < 0 at local maxima: rho is higher than neighbors, so density flows *out* (divergence, pressure analogue)
- Lap(rho) = 0 at inflection points: no net curvature drive

**PDE consistency:** The Laplacian appears directly in the PDE as the diffusion driver. Its sign determines whether a site gains or loses density — this is functionally identical to the role of curvature in gravitational dynamics.

**Simulation evidence:** In EXP2, the Gaussian bump has Lap(rho) < 0 at the peak (outward pressure) balanced by the relational penalty (inward instability), producing stability. This is the ED version of hydrostatic equilibrium.

**Strengths:**
- Direct appearance in the PDE
- Sign determines convergent vs divergent behavior — exactly what gravity does
- Hydrostatic equilibrium naturally emerges

**Weaknesses:**
- Lap(rho) in the ED PDE drives diffusion, not geodesic deviation — the mechanism is different even if the effect is analogous
- In GR, curvature affects all forms of energy-momentum; here it only affects rho itself

### 4.2 Assessment

| Mapping | Ontological | PDE | Cosmological | Simulation | Uniqueness |
|---------|------------|-----|-------------|-----------|-----------|
| Local curvature sign | Moderate | Strong | Strong | Strong | Strong — unique role in PDE |

**Recommendation:** Lap(rho) <-> **signed local curvature** with Lap > 0 as convergence (attraction) and Lap < 0 as divergence (repulsion). This is a robust mapping.

---

## 5. Analogue 4: Basins (Local Minima) — Proto-Particles / Matter Concentrations

### 5.1 Candidate Mapping

**Justification (ED-12):** Local minima in rho(x) are sites where Lap(rho) > 0 and density flows inward from all directions. These are the ED version of gravitational potential wells — regions that attract becoming from their surroundings.

**Simulation evidence (ED-Phys-03):**
- EXP1: 170 initial basins merge to 74 — consistent with gravitational clustering
- EXP3: 3,228 basins merge to 1,557 in 2D — approximately 50% loss
- Merging rate is 24.5 / time unit (1D), 1,071 / time unit (2D)

**Physical interpretation:** Basins are **proto-matter concentrations**. They are:
- Self-attracting (Lap > 0 draws density inward)
- Persistent (stabilized by the concave relational penalty once they form)
- Capable of merging (two basins can combine into one, analogous to gravitational merger)

**Important distinction:** ED basins are minima (low-rho regions), not maxima. In the energy-density mapping, a low-rho basin corresponds to a *void* or *potential well*, not a matter clump. The **peaks** (high-rho maxima, like EXP2's Gaussian bump) are the matter concentrations; basins are the voids between them.

**Revised interpretation:**
- **Peaks** (local maxima of rho) = proto-matter concentrations (stabilized by concave saturation)
- **Basins** (local minima of rho) = proto-voids (low-becoming regions between structures)
- **Basin count** tracks the number of distinct voids, which inversely tracks structure count

### 5.2 Assessment

| Mapping | Ontological | PDE | Cosmological | Simulation | Uniqueness |
|---------|------------|-----|-------------|-----------|-----------|
| Peaks as proto-matter | Strong | Strong | Strong | Strong (EXP2) | Primary |
| Basins as proto-voids | Strong | Strong | Moderate | Strong (EXP1/3) | Primary (inverse of above) |

**Recommendation:** rho-peaks <-> **matter concentrations**; rho-basins <-> **cosmic voids**. The basin count is an inverse proxy for structure count.

---

## 6. Analogue 5: Sign-Changing Curvature Boundaries — Proto-Forces / Interaction Surfaces

### 6.1 Candidate Mapping

**Definition:** Boundaries where Lap(rho) changes sign — the zero-crossings of the Laplacian. These are the inflection surfaces of the density field.

**Justification:** At a sign-changing boundary:
- On the convergent side (Lap > 0): density flows inward (attractive)
- On the divergent side (Lap < 0): density flows outward (repulsive)
- The boundary itself is the interface where the direction of density flow reverses

**Physical analogue:** These surfaces are the ED version of **force balance surfaces** — the locations where gravitational attraction and pressure repulsion balance. In standard astrophysics, these correspond to:
- The virial radius of a galaxy cluster
- The surface of a star (hydrostatic equilibrium boundary)
- The boundary between a gravitationally bound system and the expanding universe

**PDE consistency:** At Lap(rho) = 0, the diffusion drive vanishes — evolution at these surfaces is controlled entirely by the relational penalty and nonlinear gradient correction. These are the *least dynamically active* surfaces in the bulk.

**Mapping type:** Relational (defined by the spatial derivative structure between neighboring sites).

### 6.2 Assessment

| Mapping | Ontological | PDE | Cosmological | Simulation | Uniqueness |
|---------|------------|-----|-------------|-----------|-----------|
| Force balance surfaces | Moderate | Strong | Strong | Not directly measured yet | Primary |

**Recommendation:** Lap(rho) = 0 surfaces <-> **interaction / force-balance boundaries**. This mapping should be directly measurable in ED-Phys-06 by tracking zero-crossings of the discrete Laplacian.

---

## 7. Analogue 6: Horizon Candidates — Causal Decoupling Surfaces

### 7.1 Candidate Mapping

**Justification (ED-12.5):** ED-12.5 defines horizons as surfaces where M(rho) -> 0. At these surfaces:
- Diffusion halts: no density can flow across the horizon
- The region becomes causally decoupled from its exterior
- The boundary penalty h(|grad(rho)|) dominates, producing area-law scaling

**Mathematical definition:**
```
Horizon at site i  iff  rho_i / rho_max > threshold (e.g., 0.9)
Equivalently: M(rho_i) < 0.01 * M_0
```

**Physical analogue:** Event horizons in GR — one-way causal boundaries:
- Black hole horizons: nothing escapes
- Cosmological (de Sitter) horizons: regions beyond the horizon are causally disconnected
- Rindler horizons: acceleration-dependent causal boundaries

**ED-12.5 specifics:**
- Black hole horizon: M(rho) -> 0 at rho -> rho_max, with evaporation rate dM/dt ~ -1/M^2 and lifetime ~ M^3
- de Sitter horizon: constant flux J = M(rho_dS) * |grad(rho)|_dS = constant
- Rindler horizon: linear gradient rho = kx produces d(rho)/dt = M(rho)*k (Unruh temperature analogue)

**Simulation status (ED-Phys-03):** No horizon candidates observed in EXP1–3 because initial rho (= 50) is far below rho_max (= 100). Horizon studies require rho_mean close to rho_max or localized extreme overdensities.

### 7.2 Assessment

| Mapping | Ontological | PDE | Cosmological | Simulation | Uniqueness |
|---------|------------|-----|-------------|-----------|-----------|
| Causal horizons | Strong | Strong | Strong (ED-12.5) | Not yet observed | Unique — M(rho)=0 is a clean definition |

**Recommendation:** M(rho) = 0 surfaces <-> **causal horizons**. This is one of the most robust mappings in the entire framework because it has a sharp mathematical criterion and clear physical consequences.

---

## 8. Analogue 7: Thinning (d(Sum(rho))/dt < 0) — Cosmic Expansion

### 8.1 Candidate Mapping

**Justification (ED-12):** The thinning relation d(rho_mean)/dt = -lambda_2 * G^2 is the ED analogue of the Friedmann continuity equation. As total becoming decreases, the "universe" becomes sparser — the scale factor a(t) = 1/G(t) grows.

**Simulation evidence (ED-Phys-03):**
- EXP1: total rho decreases by 0.055%, lambda_2 = 9.95
- EXP3: total rho decreases by 0.022%, lambda_2 = 3.83
- Scale factor triples in both experiments
- Thinning is driven by gradients: no gradients = no thinning

**Physical analogue:** Cosmic expansion — the dilution of energy density as space expands:
- Standard: d(rho)/dt + 3H*(rho + p) = 0
- ED: d(rho_mean)/dt = -lambda_2 * G^2

**Key difference:** In standard cosmology, expansion is a property of the metric (space itself stretches). In ED, thinning is a property of the density field (becoming spreads out). There is no separate "space" that expands — the thinning of rho *is* the expansion.

**Late-time behavior (ED-12):** As G -> 0, thinning halts: d(rho_mean)/dt -> 0. This is the ED analogue of dark energy — a residual stiffness preventing complete relaxation. rho_mean asymptotes to rho_min > 0 rather than reaching zero.

### 8.2 Assessment

| Mapping | Ontological | PDE | Cosmological | Simulation | Uniqueness |
|---------|------------|-----|-------------|-----------|-----------|
| Cosmic expansion | Strong | Strong | Strong | Strong | Primary — no competing interpretation |

**Recommendation:** Thinning <-> **cosmic expansion / Hubble flow**. This is a robust, well-confirmed mapping.

---

## 9. Analogue 8: Inflation Rate lambda_1 — Early-Universe Exponential Expansion

### 9.1 Candidate Mapping

**Justification (ED-12):** The measured exponential decay G(t) = G(0)*exp(-lambda_1*t) during the inflation epoch produces a(t) = 1/G(t) ~ exp(lambda_1*t), directly analogous to de Sitter expansion a(t) ~ exp(H*t).

**Quantitative correspondence:**
- ED inflation rate lambda_1 maps to Hubble parameter H during inflation
- ED e-folding time tau = 1/lambda_1 maps to Hubble time 1/H
- The number of e-folds N = lambda_1 * T_inflation sets the "flatness" of the post-inflation universe

**Simulation evidence (ED-Phys-03):**

| Quantity | EXP1 (1D) | EXP3 (2D) | Physical Analogue |
|---------|----------|----------|-------------------|
| lambda_1 | 0.271 | 0.726 | Hubble parameter H during inflation |
| tau = 1/lambda_1 | 3.69 | 1.38 | Hubble time |
| N_e-folds (in run) | ~1.1 | ~1.2 | Number of e-folds |
| R^2 of exponential fit | 0.981 | 0.993 | Quality of de Sitter approximation |

**Important:** lambda_1 is **not** a free parameter — it is an emergent quantity determined by M_0, rho_mean, the lattice coordination number, and the gradient field structure. This is consistent with the ED philosophy: the inflation rate emerges from the compositional rule, not from a separate inflaton field.

**Dependence on dimensionality:** lambda_1(2D) / lambda_1(1D) = 2.68, exceeding the naive coordination ratio of 2.0. This suggests lambda_1 scales superlinearly with dimension, possibly as D^(1+epsilon) with epsilon > 0 due to nonlinear cross-terms.

### 9.2 Assessment

| Mapping | Ontological | PDE | Cosmological | Simulation | Uniqueness |
|---------|------------|-----|-------------|-----------|-----------|
| Inflation Hubble rate | Strong | Strong | Strong | Strong (R^2 > 0.98) | Unique |

**Recommendation:** lambda_1 <-> **inflationary Hubble parameter**. Clean, quantitatively confirmed.

---

## 10. The Complete ED-to-Physics Mapping Table

| # | ED Variable | Physical Analogue | Mapping Type | Justification | Confidence | Constraints | Open Questions |
|---|------------|-------------------|-------------|--------------|-----------|------------|---------------|
| 1 | rho(x,t) | Energy density | Local | Friedmann analogue, thinning dynamics, non-negativity | **High** | No geometry coupling; rho is ontologically prior to energy | How does mass-energy equivalence emerge? |
| 2 | \|grad(rho)\| | Curvature magnitude / force | Relational | Gradient penalty = curvature cost; inflation = curvature smoothing | **High** | Scalar, not tensor; no directional information | Can tensor curvature emerge from higher-order gradient structure? |
| 3 | Lap(rho) | Signed local curvature | Local | Lap > 0 = convergence = attraction; Lap < 0 = divergence = repulsion | **High** | Drives diffusion, not geodesic deviation | Can a metric be reconstructed from Lap(rho)? |
| 4a | rho-peaks | Matter concentrations | Local | Concave saturation stabilizes overdensities (EXP2) | **High** | Requires alpha > 0 and 0 < gamma_exp < 1 | What sets the mass scale of proto-structures? |
| 4b | rho-basins | Cosmic voids | Local | Low-rho regions between peaks | **Moderate** | Basin count is inverse proxy for structure count | Are void properties consistent with observed voids? |
| 5 | Lap(rho) = 0 surfaces | Force-balance boundaries | Relational | Convergence-divergence transition; virial/hydrostatic balance | **Moderate** | Not yet measured in simulation | Do these surfaces have observable physical signatures? |
| 6 | M(rho) = 0 surfaces | Causal horizons | Local | ED-12.5: horizons where mobility vanishes; area-law from h(u) saturation | **High** | Not yet observed in simulation (needs rho ~ rho_max) | Do horizon thermodynamics emerge (temperature, entropy)? |
| 7 | d(Sum(rho))/dt < 0 | Cosmic expansion | Global | Friedmann analogue d(rho)/dt = -lambda_2*G^2 | **High** | Expansion is thinning, not metric stretching | Can Hubble law (v = Hd) be derived from thinning? |
| 8 | lambda_1 | Inflationary Hubble rate | Global | G(t) = G(0)*exp(-lambda_1*t); a(t) ~ exp(lambda_1*t) | **High** | Emergent, not tuned; depends on M_0 and dimension | What determines the number of e-folds? |

---

## 11. Degeneracies and Alternative Interpretations

### 11.1 The rho Degeneracy

The primary degeneracy in the framework is the interpretation of rho itself. Three mappings are mathematically consistent:

1. **Energy density** — strongest cosmological correspondence
2. **Scalar field amplitude** — strongest inflation correspondence
3. **Curvature potential** — weakest overall but cannot be fully excluded

These are not mutually exclusive: rho could be a more fundamental quantity from which energy, field amplitude, and curvature all emerge in different limits. ED-5's position is that rho measures becoming, and becoming is ontologically prior to all three.

**Resolution strategy:** Rather than choosing one mapping, track which interpretation works best in each epoch:
- Inflation: scalar field analogy is natural (gradient smoothing ~ slow roll)
- Structure formation: energy density analogy is natural (gravitational instability)
- Late time: curvature potential analogy may become relevant (when boundary terms dominate)

### 11.2 The Peak/Basin Ambiguity

Are **peaks** (high-rho) or **basins** (low-rho) the better proto-matter analogue?

In the energy-density mapping:
- Peaks = matter concentrations (high energy density)
- Basins = voids (low energy density)

But in the curvature-potential mapping:
- Basins = gravitational potential wells (matter concentrations)
- Peaks = potential hills (voids)

The energy-density mapping is preferred because EXP2 shows that peaks are stabilized by the concave penalty — they persist like gravitationally bound structures. This breaks the degeneracy in favor of peaks = matter.

### 11.3 The Missing Tensor

|grad(rho)| maps to curvature magnitude, but curvature in GR is a rank-4 tensor (Riemann), not a scalar. The ED framework on a lattice naturally produces only scalar and vector quantities. Whether tensor structure can emerge from the lattice topology (e.g., from the full gradient vector field and its covariant derivatives) is an open question for ED-Phys-07.

---

## 12. Robust vs. Speculative Mappings

### Robust (confirmed by simulation + theory)

| Mapping | Evidence |
|---------|---------|
| rho <-> energy density | Friedmann analogue holds; thinning confirmed |
| \|grad(rho)\| <-> curvature magnitude | Inflation dynamics confirmed (R^2 > 0.98) |
| Lap(rho) <-> signed curvature | Directly present in PDE; hydrostatic balance observed |
| Thinning <-> expansion | lambda_2 measured; G^2 dependence confirmed |
| lambda_1 <-> inflation rate | Clean exponential confirmed in 1D and 2D |
| rho-peaks <-> matter (with saturation) | EXP2: bump persists 50K steps |

### Moderate (theoretically motivated, partially confirmed)

| Mapping | Status |
|---------|--------|
| rho-basins <-> voids | Consistent but indirect (basin count tracks inversely) |
| Lap(rho) = 0 <-> force-balance surfaces | PDE-consistent; not yet measured |

### Speculative (theoretically possible, not yet tested)

| Mapping | What's Needed |
|---------|--------------|
| M(rho) = 0 <-> horizons | Runs with rho near rho_max |
| h(u) saturation <-> area-law entropy | Boundary penalty experiments |
| rho-oscillations <-> reheating | Modified PDE with wave-like terms |
| Gradient direction <-> spatial geometry | Tensor reconstruction from vector field |

---

## 13. Derived Quantities: Mapping Compositions

Beyond the direct mappings, several physically important quantities emerge as compositions:

### 13.1 Hubble Parameter Proxy

```
H(t) = d(ln a)/dt = lambda_1   (during inflation)
H(t) = -G'(t) / G(t)           (general)
```

where G(t) = mean(|grad(rho)|) and a(t) = 1/G(t).

### 13.2 Equation of State Proxy

From thinning + scale factor, an effective equation of state w can be inferred:

```
d(rho)/dt = -3H*(1+w)*rho   (standard Friedmann)
d(rho_mean)/dt = -lambda_2 * G^2  (ED)
```

Setting these equal and using H = lambda_1 during inflation:

```
w_eff = (lambda_2 * G^2) / (3 * lambda_1 * rho_mean) - 1
```

For EXP1 at step 0: w_eff = (9.95 * 0.055^2) / (3 * 0.271 * 50.0) - 1 = 0.000741 - 1 = **-0.999**

This is remarkably close to w = -1 (de Sitter / cosmological constant), which is exactly what is expected during an inflation-like epoch.

### 13.3 Pressure Analogue

From the equation of state:
```
p_eff = w_eff * rho_mean
```

During inflation: p_eff ~ -rho_mean (negative pressure driving exponential expansion).

### 13.4 Gravitational Potential Proxy

```
Phi(x) proportional to -rho(x) + rho_mean
```

Overdensities (rho > rho_mean) correspond to negative potential wells (attractive). Underdensities (rho < rho_mean) correspond to potential hills.

### 13.5 ED Flux (Current Density)

```
J(x) = M(rho(x)) * grad(rho(x))
```

The density flux — the rate at which becoming flows from high-rho to low-rho regions. Vanishes at horizons (M = 0) and in homogeneous regions (grad = 0). Physical analogue: energy flux, or equivalently, momentum density.

---

## 14. References to ED-Phys-03 Diagnostics

Each mapping can be cross-checked against the simulation data:

| Mapping | Relevant ED-Phys-03 Diagnostic | What to Check |
|---------|-------------------------------|--------------|
| rho <-> energy density | rho_mean time series | Does thinning follow Friedmann? (Yes: lambda_2 confirmed) |
| \|grad\| <-> curvature | grad_mean time series | Does exponential decay hold? (Yes: R^2 > 0.98) |
| Lap <-> signed curvature | (not directly recorded) | Needs new diagnostic: track mean(Lap), sign distribution |
| Peaks <-> matter | rho_max time series, EXP2 | Does peak persist? (Yes: 0.02% change in 50K steps) |
| Basins <-> voids | n_basins time series | Does count decrease via merging? (Yes: ~50% loss) |
| Thinning <-> expansion | thinning_rate, rho_total | Proportional to G^2? (Yes) |
| lambda_1 <-> H_inflation | Fit to log(grad_mean) vs t | Clean exponential? (Yes) |

---

## 15. Open Questions for ED-Phys-05 and ED-Phys-06

### For Parameter Sweeps (ED-Phys-05)

1. **Critical alpha/M_0 ratio:** At what ratio does structure formation overcome diffusion? This determines when proto-matter can form from perturbations (not just persist from initial conditions).

2. **gamma_exp sensitivity:** How does the equation of state w_eff depend on gamma_exp? Is there a gamma_exp value that reproduces w = -1/3 (radiation-matter transition)?

3. **Dimension dependence of lambda_1:** Confirm whether lambda_1 scales as D^(1+epsilon). Run 1D and 2D with identical parameters and compare.

4. **rho_max and horizon onset:** At what rho_mean / rho_max ratio do horizon candidates first appear? What is the horizon "phase diagram"?

### For Emergent Phenomena (ED-Phys-06)

5. **Lap(rho) = 0 surface dynamics:** Track zero-crossings of the discrete Laplacian as a new diagnostic. Do they behave like virial boundaries?

6. **Peak coalescence:** When two high-rho peaks merge, does the resulting peak have properties consistent with gravitational merger (mass conservation, gravitational wave analogue in the gradient field)?

7. **Void statistics:** Does the size distribution of basins follow known void statistics (e.g., void probability function)?

8. **Flux topology:** Track the ED flux field J = M(rho)*grad(rho). Do flow lines form structures (filaments, sheets, nodes) consistent with cosmic web topology?

9. **Emergent temperature:** Can a temperature-like quantity be defined from the fluctuation spectrum of rho around its mean? If so, does it follow Unruh-like scaling with |grad(rho)|?
