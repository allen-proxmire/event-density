# Event Density

**One PDE, derived from four primitives and seven structural constraints, whose three constitutive channels predict the dynamics of concentrated soft matter, merging galaxy clusters, and physics across 61 orders of magnitude — with no fitting between domains.**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Allen-Proxmire/Event-Density/blob/main/ED_FrontDoor/ED_minimal_demo.ipynb)

---

## The PDE on one page

The Event Density (ED) framework is a single canonical PDE coupled to a global participation variable:

```
   ∂_t ρ = D · [ M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ) ] + H · v
   v̇   = (1/τ) · ( F̄(ρ) − ζ · v )
```

with constitutive functions

```
   M(ρ) = M₀ · (ρ_max − ρ)^β        (mobility — degenerate at capacity)
   P(ρ) = P₀ · (ρ − ρ*)              (penalty — monostable equilibrium)
   v(t)                              (participation — global feedback)
```

### Four primitives

| Primitive | Symbol | Role |
|-----------|--------|------|
| Density | ρ(x,t) | Bounded scalar field; the state variable |
| Mobility | M(ρ) | Degenerate diffusion that vanishes at capacity |
| Penalty | P(ρ) | Monostable restoring force toward equilibrium |
| Participation | v(t) | Global feedback variable (non-local oscillation) |

### Seven structural constraints

Locality, isotropy, gradient-driven flow, dissipative structure, single scalar field, minimal coupling, dimensional consistency.

These seven constraints uniquely select the canonical PDE above. The derivation is not a postulate; the constraints eliminate all alternatives.

### Three channels

Each constitutive channel, when isolated, reduces *exactly* to a known physical equation:

```
                    ┌─────────────────────────────────────┐
                    │      One canonical ED PDE           │
                    └──────────────┬──────────────────────┘
                                   │
            ┌──────────────────────┼──────────────────────┐
            ▼                      ▼                      ▼
   ┌────────────────┐    ┌────────────────┐    ┌────────────────────┐
   │   Mobility     │    │    Penalty     │    │   Participation    │
   │   M(ρ) ∇²ρ     │    │  −P₀(ρ − ρ*)   │    │   τv̇ + ζv = F̄    │
   ├────────────────┤    ├────────────────┤    ├────────────────────┤
   │  Porous-medium │    │  Exponential   │    │  Damped telegraph  │
   │  diffusion     │    │  (RC / Debye)  │    │  / RLC oscillation │
   │  (Barenblatt)  │    │                │    │                    │
   ├────────────────┤    ├────────────────┤    ├────────────────────┤
   │   1.1% error   │    │   0.00% error  │    │    0.00% error     │
   └────────────────┘    └────────────────┘    └────────────────────┘
```

Full derivation: [`papers/foundational/`](papers/foundational/), the Foundational Paper.

---

## Three flagship results

| Result | Domain | Channel | Prediction | Observed |
|--------|--------|---------|------------|----------|
| **[UDM](papers/UDM/)** | Concentrated soft matter | Mobility | `D(c) = D₀(1 − c/c_max)^β` | R² > 0.986 across 10 materials; β = 1.72 ± 0.37 |
| **[Galaxy-15](papers/galaxy-15/)** | Cluster mergers | Penalty / dynamical wake | `ℓ = D_T / v_current` | 7 clusters + Finner+25 median 79 ± 14 kpc, all consistent |
| **[PDE Atlas](papers/ED-Dimensional-Master_The_Unified_Atlas.md)** | All physics, 5 regimes | All channels | One PDE across 61 orders of magnitude | 9 architectural laws verified in dimensions 1–4 |

The same PDE, the same parameter set, no inter-domain fitting. Full unification narrative: **[RESULTS.md](RESULTS.md)**.

---

## Try it in 3 minutes

**Colab (zero setup):** click the badge above.

**Local:**

```bash
git clone https://github.com/Allen-Proxmire/Event-Density.git
cd Event-Density
pip install -r requirements.txt
jupyter notebook ED_FrontDoor/ED_minimal_demo.ipynb
```

Full quickstart, reproduction notebooks, and troubleshooting: **[GETTING_STARTED.md](GETTING_STARTED.md)**.

---

## Repository map

```
event-density/
├── README.md                ← you are here
├── RESULTS.md               ← three flagship results, the unification claim
├── GETTING_STARTED.md       ← install + reproduction quickstart
│
├── papers/                  ← canonical papers (one folder per paper)
│   ├── foundational/        ← Foundational Paper (axioms, derivation, analogues)
│   ├── UDM/                 ← Universal Degenerate Mobility (soft matter)
│   ├── galaxy-15/           ← Merger-Lag First Evidence (cluster lensing)
│   └── ED-Dimensional-Master_The_Unified_Atlas.md
│
├── edsim/                   ← simulation engine (Python package, CLI, 112 tests)
│   └── (core / experiments / phys / invariants / tests / units)
│
├── data/                    ← empirical datasets (SPARC, GSWLC, z0MGS, …)
├── analysis/                ← reusable scripts and reproduction notebooks
│   └── notebooks/           ← 01_minimal_demo, 02_three_channels, 03_galaxy15_lag, 04_udm_mobility
├── outputs/                 ← solver outputs (gitignored, regenerable)
│
├── ED_FrontDoor/            ← outreach materials, 1-pagers, demo notebook
├── docs/                    ← architecture, how-to-run, API, changelog, archive
│
├── CONTRIBUTING.md
├── LICENSE                  ← MIT
├── pyproject.toml
└── requirements.txt
```

---

## What ED claims, and what it doesn't

**Claims.** Architectural sufficiency: one PDE, derived from minimal primitives, generates the dynamical structure of multiple known regimes without fitting. The structural correspondences (mobility ⇔ porous-medium, penalty ⇔ exponential decay, participation ⇔ telegraph) hold for *all* parameter values, not just tuned ones. Tested empirically in concentrated soft matter (10 materials) and cluster mergers (7 systems + 1 aggregate sample of 58 subclusters). Falsifiable predictions are documented in [`ED_FrontDoor/ED_Falsifiable_Prediction.md`](ED_FrontDoor/ED_Falsifiable_Prediction.md).

**Does not claim.** ED does not derive general relativity, quantum mechanics, or the Standard Model. It does not contain gauge fields, fermions, or superposition. Its horizons are transient. Its cosmology is provisionally falsified as a standalone model. These limits are not concealed; they are tested and documented.

---

## Contact and contribution

**Allen Proxmire** — creator of the Event Density framework.

- Repository: [github.com/Allen-Proxmire/Event-Density](https://github.com/Allen-Proxmire/Event-Density)
- To propose experiments, test predictions, or collaborate: open an issue.
- Contributing guidelines: [CONTRIBUTING.md](CONTRIBUTING.md).

License: **MIT**.
