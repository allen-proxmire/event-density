# ED-Data-Galaxy-04: Full ED PDE With Penalty — The Steady-State Problem

**Allen Proxmire**
**March 2026**

---

## 0. Purpose

ED-Data-Galaxy-03 showed that the pure-PME Barenblatt profile has the right core shape but the wrong edge shape for dwarf galaxy halos. The Burkert profile — with a flat core and a gradual $r^{-3}$ tail — fits better. The natural next step was to solve the full ED PDE with penalty ($P_0 > 0$), which should produce a density floor instead of a sharp edge.

This note attempts that solution and discovers a fundamental structural constraint.

---

## 1. The Steady-State Equation

The spherically symmetric steady-state ED PDE is:

$$\frac{1}{r^2}\frac{d}{dr}\!\left[r^2 M(\rho)\frac{d\rho}{dr}\right] = P_0(\rho - \rho^*),$$

with $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ and boundary conditions $d\rho/dr|_{r=0} = 0$ (symmetry), $\rho \to \rho^*$ as $r \to \infty$.

The expectation was that this ODE would produce a cored profile with a gradual tail — replacing the sharp Barenblatt edge with a smooth approach to $\rho^*$.

---

## 2. The Structural Discovery: No Nontrivial Steady State

### 2.1 Law L1 Applies

The ED PDE has a unique globally attracting equilibrium: $\rho = \rho^*$ everywhere, $v = 0$ (Law L1, proven in ED-Math-01). This means:

**The only steady-state solution of the ED PDE with $P_0 > 0$ is the spatially uniform field $\rho(x) = \rho^*$.**

There is no nontrivial steady-state halo profile. The ODE in Section 1 has $\rho(r) = \rho^*$ as its only solution satisfying the boundary conditions.

### 2.2 Why This Follows From the Architecture

The penalty $P(\rho) = P_0(\rho - \rho^*)$ is a monostable restoring force. It drives every point toward $\rho^*$. The mobility $\nabla\cdot[M(\rho)\nabla\rho]$ spreads density gradients. Together, they guarantee that any initial structure will eventually flatten to $\rho^*$. There is no mechanism in the canonical ED PDE that can sustain a density peak against the penalty — no bistability, no conserved dynamics, no external source.

This is the same unique-attractor property that makes ED's horizons transient (Analogue 4 in the foundational paper): the monostable penalty guarantees that all structure is temporary.

### 2.3 What This Means for Galaxy Halos

If the ED PDE governs galactic density dynamics, then galaxy halos are not steady states. They are **long-lived transients** — structures that formed from initial conditions and are slowly decaying toward $\rho^*$. The halo profile at any given time is a snapshot of this decay, not an equilibrium.

This is not unique to ED. In standard astrophysics, galaxy halos are also not in true equilibrium — they grow by accretion, are perturbed by mergers, and evolve over Hubble times. The difference is that in $\Lambda$CDM, the NFW profile is a quasi-equilibrium maintained by ongoing accretion; in ED, the profile is a transient maintained by slow penalty decay.

---

## 3. Transient Profiles: What ED Actually Predicts

Since the steady state is trivial ($\rho = \rho^*$), the relevant ED prediction is the profile at a specific time — the "age" of the halo. This requires solving the time-dependent PDE:

$$\partial_t\rho = D\bigl[\nabla\cdot(M(\rho)\nabla\rho) - P_0(\rho - \rho^*)\bigr].$$

### 3.1 Numerical Solutions

The spherically symmetric PDE was evolved from a Gaussian initial condition with $\beta = 2$, $D = 0.3$, and varying $P_0$:

| $P_0$ | $T$ (nd units) | $\rho(0)/\rho_{\text{init}}(0)$ | Profile shape | Core radius |
|:-------|:---------------|:-------------------------------|:-------------|:-----------|
| 0.001 | 500 | 0.705 | Nearly flat (spread everywhere) | $> 20$ kpc |
| 0.003 | 500 | 0.546 | Nearly flat | $> 20$ kpc |
| 0.010 | 500 | 0.268 | Nearly flat | $> 20$ kpc |

At all tested penalty values, the profile at $T = 500$ is nearly uniform — the degenerate mobility has spread the initial bump across the entire domain, and the penalty has partially relaxed it toward $\rho^*$. No halo-like structure (concentrated core with declining envelope) survives.

### 3.2 Why the Profiles Are Flat

The degenerate mobility $M(\rho) = (\rho_{\max} - \rho)^\beta$ is largest where $\rho$ is smallest — meaning low-density regions have the highest transport rate. In spherical geometry, this causes rapid spreading of material from the core into the large-volume outer regions. The $r^2$ volume factor in spherical geometry amplifies this: even a small outward flux fills a much larger volume than the core. The result is that the initial Gaussian spreads to fill the domain on a timescale much shorter than the penalty relaxation time.

### 3.3 What Would Produce a Halo-Like Profile

For the ED PDE to produce a concentrated, long-lived halo-like profile, one of the following would be needed:

1. **Continuous mass infall.** An external source term $+S(r, t)$ that feeds mass into the core, balancing the outward spreading and penalty relaxation. In astrophysical terms: ongoing accretion.

2. **A bistable or conserved penalty.** Replacing the monostable $P(\rho) = P_0(\rho - \rho^*)$ with a double-well potential (like Allen-Cahn) would create stable, spatially inhomogeneous equilibria. But this violates ED's axiom P4 (dissipative structure with unique equilibrium).

3. **An inverted mobility.** If $M(\rho)$ increased with $\rho$ instead of decreasing, dense regions would spread faster, which is the wrong direction. But if the mobility had a minimum at intermediate $\rho$, it could trap density in a core. This would require a non-monotonic mobility — outside the canonical ED constitutive choice.

4. **The participation channel as a source.** With $H > 0$ and $v(t) > 0$, the participation term $+Hv$ adds uniform density everywhere, which could (transiently) maintain a density excess. But $v(t) \to 0$ by Law L1, so this is also temporary.

None of these options is available within the canonical ED PDE as defined by axioms P1–P7. The conclusion is structural.

---

## 4. Comparison to Dwarf Galaxy Data

### 4.1 Can a Transient Profile Match?

The question becomes: is there a time $T$ and a set of parameters $(D, P_0, \beta, \rho_{\max})$ such that the ED transient profile at time $T$ resembles a Burkert-like halo?

For this to work:
- The mobility spreading timescale must be long enough that the core persists for $\sim 10$ Gyr ($\sim 10^4$ nondimensional units in the galactic regime).
- The penalty must be weak enough that the central density remains well above $\rho^*$.

Requirement: $P_0 \ll 1/T_{\text{age}}$ in nondimensional units, where $T_{\text{age}} \sim 10^4$. This gives $P_0 \ll 10^{-4}$ — essentially the pure-PME limit. At such weak penalty, the profile is Barenblatt-like with a sharp edge — the same result as Galaxy-02 and Galaxy-03.

**This is a catch-22:** strong penalty erases the halo; weak penalty produces a sharp edge. There is no intermediate regime where the penalty produces a gradual tail while preserving a core.

### 4.2 Quantitative Assessment

| Regime | $P_0$ | Profile at $T \sim 10^4$ | Matches dwarf data? |
|:-------|:------|:------------------------|:--------------------|
| Pure PME | $\sim 0$ | Barenblatt cap (sharp edge) | Core yes, tail no |
| Weak penalty | $10^{-4}$ | Barenblatt + slight floor | Core yes, tail insufficient |
| Moderate penalty | $10^{-2}$ | Flattened (no core) | No |
| Strong penalty | $10^{-1}$ | Uniform ($\rho \approx \rho^*$) | No |

---

## 5. Interpretation: What This Means for ED at Galactic Scales

### 5.1 The Structural Limitation

The canonical ED PDE cannot produce a self-sustaining, quasi-static halo profile. This is not a numerical failure — it is a structural consequence of the monostable penalty (Law L1). Every structure is transient and decays to $\rho^*$.

This is the galactic manifestation of the same architectural limit identified in the foundational paper (Analogue 4): ED horizons are transient; ED structure is temporary. At condensed-matter scales, this is not a problem (diffusion experiments are inherently transient). At galactic scales, it is a significant limitation: observed galaxy halos have persisted for $\sim 10$ Gyr and show no signs of dissolving.

### 5.2 What ED Gets Right Despite This Limitation

1. **Flat cores.** The ED mobility structure (degenerate at $\rho_{\max}$) naturally produces flat-cored profiles at early times. This is correct for dwarf galaxies and contrasts with NFW cusps.

2. **Core scale radius.** The ED $R_{\text{edge}}$ is within a factor of 1.3–1.7 of the Burkert core radius for all four tested dwarfs. The mobility-driven scale radius is physically meaningful even though the full profile shape is wrong.

3. **Sub-Fickian transport.** The ED prediction that density transport is slower than Fickian ($\alpha_R < 0.5$) is qualitatively consistent with the slow evolution of galactic structure.

### 5.3 What Would Be Needed

For ED to describe galaxy halos as long-lived structures, one of the following extensions would be needed:

1. **Continuous source term.** Add $+S(r,t)$ representing accretion. This is astrophysically motivated but breaks the closed-system axiom.

2. **Modified penalty.** Replace the monostable $P(\rho) = P_0(\rho - \rho^*)$ with a form that has a spatially varying equilibrium $\rho^*(r)$. This is equivalent to embedding the ED PDE in a gravitational potential.

3. **Coupling to gravity.** The most natural extension: couple the ED density field to the Poisson equation $\nabla^2\Phi = 4\pi G\rho$, making $\rho^*$ (or the penalty) dependent on the gravitational potential. This would allow self-gravitating equilibria and is the subject of future work (ED-Phys geometry series).

---

## 6. Honest Assessment

| Criterion | Result |
|:----------|:-------|
| Does ED-with-penalty produce a nontrivial steady-state halo? | **No** (Law L1: unique attractor) |
| Does ED-with-penalty produce a transient halo at intermediate times? | Partially (core forms, but spreads too quickly in spherical geometry) |
| Does any parameter regime produce a Burkert-like profile? | **No** (catch-22: strong penalty erases core; weak penalty gives sharp edge) |
| Is the structural limitation fixable within canonical ED? | **No** (requires source term, modified penalty, or gravitational coupling) |
| Does ED still predict correct core scales? | **Yes** (R_edge ≈ r_c within factor 1.3–1.7) |

---

## 7. Next Steps

### 7.1 Accept the Limitation

The canonical ED PDE — four primitives, three channels, seven axioms — cannot produce self-sustaining galaxy halos. This is a genuine architectural limit. Document it honestly and move on to extensions.

### 7.2 Explore Extensions

1. **ED + Poisson.** Couple the ED PDE to the gravitational Poisson equation. The gravitational potential acts as an effective spatially varying $\rho^*(r)$ that can sustain a density peak against penalty relaxation. This is the most physically motivated extension.

2. **ED + accretion source.** Add a mass-infall term $+S(r,t)$ calibrated to cosmological accretion rates. This preserves the ED PDE structure while adding astrophysical realism.

3. **Modified mobility.** Test whether a non-power-law mobility $M(\rho)$ (e.g., with a minimum at intermediate density) can produce self-sustaining profiles. This requires revisiting axiom P3.

### 7.3 Refocus on Strengths

The ED framework's strengths at galactic scales are:

- **Core formation mechanism.** The degenerate mobility naturally produces cored profiles without baryonic feedback. This is a structural prediction that matches observations and contrasts with NFW cusps.
- **Core scale radius.** The ED core radius is quantitatively comparable to observed Burkert core radii.
- **Connection to condensed matter.** The same mobility law ($\beta \approx 2$) fits colloidal, molecular, and protein systems. The universality of the functional form extends to galactic core scales.

### 7.4 Pipeline Status

| Note | Title | Status | Key Result |
|:-----|:------|:-------|:-----------|
| Galaxy-01 | Halo Edge Design | Complete | Pipeline defined |
| Galaxy-02 | NGC 3198 | Complete | Pure-PME rejected |
| Galaxy-03 | Dwarf Mini-Sweep | Complete | Core scale correct; edge shape wrong |
| **Galaxy-04** | **Full ED with Penalty** | **Complete** | **No nontrivial steady state (Law L1); catch-22 for halos; gravitational coupling needed** |
| Galaxy-05 | ED + Poisson coupling | Planned | Self-gravitating ED halos |
