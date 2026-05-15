# ED Dependency Graph — Substrate Primitives × Forcing Papers

**Date:** 2026-05-13
**Status:** Consolidates §3.0 Primitive Inputs from all Forcing Papers #1–#19 + Meta-Paper M0.
**Purpose:** Identify which substrate primitives are load-bearing for which forcing theorems, which primitives are high-centrality (need forcing first), which are low-centrality (can wait), and which downstream papers must be updated after each primitive closes.

---

## Section 1. Primitive Inventory

### 1.1 Numbered substrate primitives (P-series)

| ID | Primitive | One-line definition |
|---|---|---|
| **P01** | Event-density layer existence | The substrate exists as a pre-quantum primitive layer. |
| **P02** | Participation as primitive relation | Chains participate in channels as a primitive relation. |
| **P03** | Channel + locus indexing | Discrete channel index $\mathcal{K}$; (discrete or continuous) locus index. Also: spatial homogeneity as primitive symmetry. |
| **P04 core** | Bandwidth as non-negative additive scalar | $b_K \in \mathbb{R}_{\geq 0}$ on each channel; additive under disjoint channel decomposition. |
| **P04 §1.5** | Four-band partition | Bandwidth decomposes into 4 orthogonal bands: internal, adjacency, environmental, commitment-reserve. |
| **P05** | Polarity-transport along edges | Substrate-level connection structure between adjacent loci. |
| **P06** | Spatial dimension $D = 3$ | The substrate's spatial axis is $\mathbb{R}^3$. |
| **P07** | Channel structure | Channels are ontologically primitive; identity intrinsic to the participation graph. |
| **P08** | Substrate scale $\ell_P$ | Characteristic edge length of the participation graph. |
| **P09** | $U(1)$-valued polarity | Polarity $\pi_K \in U(1) \cong S^1$; the *unique* angular primitive in the substrate. |
| **P10** | Rule-type structure | The substrate supports multiple structural rule-types $\tau_\bullet$ with their own participation measures. |
| **P11** | Commitment with environmental phase-randomization | Discrete substrate-level events at which multi-channel participation collapses to a single channel; phase-randomization on uniform $U(1)$; irreversible. |
| **P12** | Stability landscape primitive | Substrate-level functional $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$ governing chain dynamics. |
| **P13** | Time homogeneity | The substrate's primitive time-translation symmetry. |

### 1.2 Kernel rule-types and auxiliary structural commitments (non-numbered)

| ID | Structural commitment | One-line definition |
|---|---|---|
| **V1** | V1 retarded vacuum kernel | Substrate-level vacuum-fluctuation kernel; retarded support forced by P11; finite-width (Theorem N1). |
| **V5** | V5 cross-chain correlation kernel | Substrate-level cross-chain temporal-correlation kernel; UV cutoff at $c/\ell_P$. |
| **HOL** | Holographic participation-count bound | $N = 4\pi R^2/\ell_\mathrm{ED}^2$ on closed 2-surfaces. |
| **DEC** | Cosmic decoupling surface + dipole-mode projection | Substrate boundary at $R_H = c/H_0$; dipole projection onto chain adjacency. |
| **HYD** | Hydrodynamic-window scale separation | $\ell_P \ll R_\mathrm{cg} \ll L_\mathrm{flow}$ for substrate-to-continuum bridge (DCGT). |
| **THN** | Thin-participation regime | $M_\mathrm{eff} \to \infty$, $b_\mathrm{env} \to 0$, $\Gamma_\mathrm{commit} \to 0$ for continuum Schrödinger. |
| **GAL** | Galilean symmetry at non-rel scope | Galilean group acting on the participation manifold. |
| **POI** | Poincaré symmetry at relativistic scope | Poincaré group acting at the relativistic scope. |
| **IND** | Individuation-exclusion on $Q_2$ | Two indistinguishable fermionic chains cannot coincide. |

### 1.3 Background mathematical infrastructure (not substrate; not load-bearing in dependency-graph sense)

Frobenius classification (real division algebras), Stone's theorem, Cauchy functional equation, Weyl-Fourier inequality on $L^2$, Gleason 1957 + Busch 2003, classification of compact Lie groups, Shannon-Khinchin entropy axioms, Coecke-Kissinger categorical-QM framework, Landau-Khalfin operator-norm algebra, standard measure-theoretic analysis. These are background; ED does not rederive them.

---

## Section 2. Master Dependency Table

**Legend:**
- ✅ = load-bearing primitive input (forcing theorem fails without it)
- ➡ = upstream-paper input (built directly on prior result)
- · = not directly invoked

| Paper | P03 | P04 core | P04 §1.5 | P06 | P07 | P09 | P10 | P11 | P12 | P13 | V1 | V5 | HOL | DEC | HYD | THN | GAL | POI | IND | Upstream papers |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **#1** Participation measure | ✅ | ✅ | · | · | ✅ | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | · | — |
| **#2** Born rule | · | ✅ | · | · | · | ✅ | · | ✅ | · | · | · | · | · | · | · | · | · | · | · | ➡ #1 |
| **#3** Inner product + Tsirelson | · | ✅ | ✅ | · | · | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | · | ➡ #1, #2 |
| **#4** Schrödinger (Stone) | · | · | · | · | · | · | · | · | · | ✅ | · | · | · | · | · | · | · | · | · | ➡ #1, #2, #3 |
| **#5** Gauge fields (T17) | · | · | · | · | · | ✅ | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | ➡ #1–#4 |
| **#6** Hamiltonian + mass | · | ✅ | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | · | ✅ | · | · | ➡ #1–#4 |
| **#7** Dirac + g=2 | · | · | · | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | · | ✅ | ✅ | ➡ #1–#6 |
| **#8** DCGT gauge translation | · | · | · | · | · | · | · | · | · | · | · | · | · | · | ✅ | · | · | · | · | ➡ #5 |
| **#9** Newton G + a₀ + BTFR | · | · | · | · | · | · | · | · | ✅ | · | · | · | ✅ | ✅ | · | · | · | · | · | ➡ #1–#8 |
| **#10** BH + Hawking | · | · | · | · | · | · | · | · | · | · | ✅ | ✅ | · | · | ✅ | · | · | · | · | ➡ #1–#9 |
| **#11** Heisenberg | · | · | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | ➡ #1–#4 |
| **#12** Momentum operator | ✅ | · | · | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | ➡ #1–#3 |
| **#13** Schrödinger thin-limit | · | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | · | ✅ | · | · | · | ➡ #1–#4 |
| **#14** Born via bandwidth-ratio | · | ✅ | · | · | · | · | · | ✅ | · | · | · | · | · | · | · | · | · | · | · | ➡ #1 |
| **#15** Adjacency kinetic structure | · | · | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | · | ✅ | · | · | ➡ #1–#6, #11 |
| **#16** Phase-independence | · | ✅ | · | · | · | ✅ | · | · | · | · | · | · | · | · | · | · | · | · | · | ➡ #1, #2 |
| **#17** Four postulates unified | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | ✅ | · | ✅ | · | · | · | · | · | · | · | · | · | ➡ #1–#16 |
| **#18** V1 finite-width (N1) | · | · | · | · | · | · | · | · | · | · | ✅ | · | · | · | · | · | · | · | · | ➡ #1–#4 |
| **#19** V1 retarded (T18) | · | · | · | · | · | · | · | ✅ | · | · | ✅ | · | · | · | · | · | · | · | · | ➡ #18 |

### 2.1 Centrality counts (number of forcing papers using each load-bearing primitive)

| Primitive | Paper count | Centrality tier | Forcing status |
|---|---|---|---|
| **P04 core** (bandwidth additivity) | 8 (#1, #2, #3, #6, #13, #14, #16, #17) | **HIGH** | ✅ **FORCED (M-2, 2026)** |
| **P09** ($U(1)$ polarity) | 6 (#1, #2, #3, #5, #16, #17) | **HIGH** | ✅ **FORCED (M-1, 2026)** |
| **P04 §1.5** (four-band partition) | 5 (#3, #6, #11, #15, #17) | **HIGH** | ✅ **FORCED (M-2, 2026)** |
| **P11** (commitment + phase-randomization) | 4 (#2, #14, #17, #19) | MED | ⚠️ **PARTIALLY FORCED (M-3, 2026)** — commitment-existence residue |
| **P03** (spatial-channel indexing) | 3 (#1, #12, #17) | MED | ✅ **FORCED (M-4, 2026)** |
| **P07** (channel structure as ontological primitive) | 3 (#1, #2, #17 — implicitly more) | MED | ✅ **FORCED (M-Omnibus, 2026)** |
| **V1** (retarded vacuum kernel) | 3 (#10, #18, #19) | MED | ⚠️ **PARTIALLY FORCED (M-Omnibus, 2026)** — existence forced; detailed form residue |
| **P13** (time homogeneity) | 2 (#4, #17) | LOW | ✅ **FORCED (M-4, 2026)** |
| **P06** ($D = 3$) | 3 (#7, #12, #17) | LOW | 🔴 **HONEST RESIDUE** |
| **GAL** (Galilean symmetry) | 2 (#6, #15) | LOW | ✅ **FORCED (M-4, 2026)** |
| **POI** (Poincaré symmetry) | 1 (#7) | LOW | ⚠️ **PARTIALLY FORCED (M-4, 2026)** — cosmological-curvature residue |
| **V5** (cross-chain correlation kernel) | 1 (#10) + Arc-D/Arc-E echoes | LOW | ⚠️ **PARTIALLY FORCED (M-Omnibus, 2026)** — existence forced; detailed form residue |
| **HYD** (hydrodynamic window) | 2 (#8, #10) | LOW | 🔴 **RESIDUE declared (M-Omnibus, 2026)** — empirically-robust assumption |
| **P10** (rule-type primitive) | 1 (#5) | LOW | 🔴 **RESIDUE declared (M-Omnibus, 2026)** — structural-normative capacity |
| **HOL** (holographic counting) | 1 (#9) | LOW | 🔴 **RESIDUE declared (M-Omnibus, 2026)** — mixed forceable + empirical |
| **DEC** (decoupling-surface + dipole) | 1 (#9) | LOW | 🔴 **RESIDUE declared (M-Omnibus, 2026)** — mixed forceable + empirical |
| **P12** (stability landscape) | 1 (#9) | LOW | 🔴 **RESIDUE declared (M-Omnibus, 2026)** — operational construct |
| **IND** (individuation-exclusion) | 1 (#7) | LOW | 🔴 **RESIDUE declared (M-Omnibus, 2026)** — likely forceable, cluster-efficiency |
| **THN** (thin-participation regime) | 1 (#13) | LOW | 🔴 **RESIDUE declared (M-Omnibus, 2026)** — operational limit, not primitive |

**Total load-bearing items audited: 19.** Of these, 3 are HIGH centrality (P04 core, P09, P04 §1.5), 4 are MED, 12 are LOW.

**Post-Omnibus forcing count (2026-05-13, M-series TERMINAL):**
- **Fully FORCED:** P09 (M-1), P04 core (M-2), P04 §1.5 (M-2), P03 (M-4), P13 (M-4), GAL (M-4), P07 (M-Omnibus) — **7 primitives**.
- **Partially FORCED with named residue:** P11 (M-3, commitment-existence residue), POI (M-4, cosmological-curvature residue), V1 (M-Omnibus, form residue), V5 (M-Omnibus, form residue) — **4 primitives**.
- **Honest residue declared:** P06, P10, P12, HYD, HOL, DEC, IND, THN — **8 primitives**.

**All 19 load-bearing items are now closed with definite structural status.** No item remains pending; no item remains "load-bearing input without resolution." The M-series is **terminal**.

---

## Section 3. Forcing-Paper Dependency Graph (DAG)

Text-based directed acyclic graph. Arrows point upstream → downstream. Primitives at the root, papers in the middle, downstream consequences at the bottom.

```
                ┌─────────────────────────── PRIMITIVES (root layer) ───────────────────────────┐
                │                                                                                │
            ┌───┴───┐    ┌──────┐   ┌──────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐
            │P04 core│   │P04   │   │ P09  │   │P03 │   │P07 │   │P11 │   │P13 │   │P06 │
            │bandwidth│  │§1.5  │   │U(1)  │   │loc │   │chan│   │comm│   │time│   │D=3 │
            │additivit│  │4-band│   │polar │   │idx │   │   │   │+rand│   │hom │   │    │
            └─┬───────┘  └─┬────┘   └──┬───┘   └─┬──┘   └─┬──┘   └─┬──┘   └─┬──┘   └─┬──┘
              │            │           │         │        │         │        │       │
              │            │           │         │        │         │        │       │
              ▼            ▼           ▼         ▼        ▼         ▼        ▼       ▼
        ┌────────────────────────────────────────────────────────────────────────────────┐
        │                                                                                │
        │   PAPER #1  ──────────────┐  (participation measure: needs P04+P09+P03+P07)    │
        │       │                   │                                                    │
        │       ▼                   ▼                                                    │
        │   PAPER #2 (Born)    PAPER #16 (phase-independence)                            │
        │       │  needs +P11  needs P09 + P04                                           │
        │       │                                                                        │
        │       ▼                                                                        │
        │   PAPER #3 (inner product + Tsirelson: needs +P04 §1.5)                        │
        │       │                                                                        │
        │       ▼                                                                        │
        │   PAPER #4 (Schrödinger Stone: needs +P13)                                     │
        │       │                                                                        │
        │       ├──────────────┐─────────────┐──────────────┐                            │
        │       ▼              ▼             ▼              ▼                            │
        │   PAPER #5 (gauge)  PAPER #6     PAPER #11     PAPER #13                       │
        │   needs +P10        (H+mass)    (Heisenberg)  (thin-limit)                     │
        │   ┌───┴────┐        needs +GAL  needs +P04    needs +THN                       │
        │   │        │        +P04 §1.5    §1.5                                          │
        │   ▼        ▼              │                                                    │
        │ PAPER #8 PAPER #7         ▼                                                    │
        │ (DCGT)   (Dirac)      PAPER #15                                                │
        │ +HYD     +P06+POI    (adj kinetic)                                             │
        │          +IND        +GAL + P04 §1.5                                           │
        │   │        │                                                                   │
        │   ▼        ▼                                                                   │
        │ PAPER #9 (gravity)   needs +P12 + HOL + DEC                                    │
        │     │                                                                          │
        │     ▼                                                                          │
        │ PAPER #10 (BH + Hawking)   needs +V1 + V5 + HYD                                │
        │                                                                                │
        │   PAPER #12 (momentum)   needs P03+P06                                         │
        │                                                                                │
        │   PAPER #14 (Born via bandwidth-ratio)   needs +P11 (parallel to #2 direct)    │
        │                                                                                │
        │   PAPER #17 (Four-postulates synthesis)   needs ALL OF #1–#16                  │
        │                                                                                │
        │   PAPER #18 (V1 finite-width)   needs Papers #1–#4 + V1                        │
        │       │                                                                        │
        │       ▼                                                                        │
        │   PAPER #19 (V1 retarded)   needs +P11 + V1                                    │
        │                                                                                │
        └────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Direct primitive-to-paper edges (high-centrality primitives)

```
P04 core ──→ #1, #2, #3, #6, #13, #14, #16, #17
P09 (U(1)) ──→ #1, #2, #3, #5, #16, #17
P04 §1.5 ──→ #3, #6, #11, #15, #17
P11 ──→ #2, #14, #17, #19
P03 ──→ #1, #12, #17
P13 ──→ #4, #17
P06 ──→ #7, #12, #17
```

### 3.2 Paper-to-paper edges (upstream consequences)

```
#1 → #2 → #3 → #4 → #5 → #6 → #7
              ↓     ↓     ↓
              #11   #8    
              ↓     ↓
              #13   #9 → #10
              ↓
              #15

#1 → #16
#1 → #14
#1–#4 → #18 → #19
#1–#16 → #17 (synthesis)
```

---

## Section 4. Centrality Analysis and Forcing Priority

### 4.1 Centrality tiers

**HIGH-CENTRALITY (close these first; downstream impact maximal):**

1. **P04 core (bandwidth additivity)** — 8 papers depend on it. Forcing route: Shannon-Khinchin axiom 4 + operational adequacy (Born $\sigma$-additivity requires it).
2. **P09 ($U(1)$ polarity)** — 6 papers depend on it. Forcing route: Frobenius classification (compactness rules out $\mathbb{R}$; continuity rules out $\mathbb{Z}_n$) + Coecke-Kissinger Frobenius algebra classification. **This is the primitive the displaced-postulate critique specifically targeted.**
3. **P04 §1.5 (four-band partition)** — 5 papers depend on it. Forcing route: information-theoretic minimum decomposition (fewer bands conflate operational categories; more bands split artificially) + compositional closure.

**MED-CENTRALITY:**

4. **P11 (commitment with uniform-$U(1)$ phase-randomization)** — 4 papers. Forcing route: operational adequacy (Born rule recovery) + Haar measure on $U(1)$ for max-entropy. Inherits load-bearing on P09's $U(1)$ structure.
5. **P03 (spatial-channel indexing / spatial homogeneity)** — 3 papers. Forcing route: symmetry-minimality (Stone's theorem requirement).
6. **P07 (channel structure)** — 3 papers. Forcing route: compositional closure (categorical morphism composition).
7. **V1 (retarded vacuum kernel)** — 3 papers. Partial forcing already in Paper #19 (retardation via P11). Existence-as-rule-type forcing: operational adequacy + compositional closure.

**LOW-CENTRALITY (close later; minor downstream impact):**

8. **P13 (time homogeneity)** — 2 papers. Likely *residue*: "minimum operational adequacy for Stone's theorem on time-translations."
9. **P06 ($D = 3$)** — 3 papers. Likely *residue*: "empirically necessary; deeper structural forcing (anthropic, holographic, dynamical) open."
10. **GAL (Galilean) / POI (Poincaré)** — 3 papers combined. Likely *joint forcing* with P13: symmetry-minimality at non-rel + rel scopes.
11. **V5, HYD, P10, HOL, DEC, P12, IND, THN** — 1 paper each. Each closed individually with route-appropriate arguments; some likely residue.

### 4.2 Forcing priority order (recommended sequence)

**Tier 1 — Most impactful first closures:**

- **M-1: P09 ($U(1)$ polarity).** Direct response to displaced-postulate critique. Clearest forcing routes (Routes A symmetry-minimality + E category-theoretic necessity). Expected outcome: **forceable** with Frobenius + Coecke-Kissinger arguments.
- **M-2: P04 core (bandwidth additivity).** Clean operational + information-theoretic forcing. Expected outcome: **forceable** with Shannon-Khinchin + $\sigma$-additivity.

**Tier 2 — Substantial closures:**

- **M-3: P04 §1.5 (four-band partition).** Information-theoretic minimum decomposition + compositional closure. Expected outcome: **likely forceable**; small residue risk on "why exactly four and not three subsumed into compositional structure."
- **M-4: P11 (commitment + phase-randomization).** Inherits load from P09 closure. Expected outcome: **mixed** — commitment-existence likely residue; uniform-$U(1)$ phase-randomization forceable given P09 closure + Haar-maximum-entropy.

**Tier 3 — Symmetry and channel-structure closures:**

- **M-5: P03 + P13 + GAL + POI (joint symmetry forcing).** Joint paper or sequence: symmetry primitives at non-rel + rel scopes. Expected outcome: **mixed** — strong route via symmetry-minimality; residue on "why Galilean and not Carrollian at non-rel scope."
- **M-6: P07 (channel structure as ontological primitive).** Category-theoretic necessity. Expected outcome: **likely forceable**; small residue risk.

**Tier 4 — Kernel and scale-separation closures:**

- **M-7: V1 existence as rule-type** (V1 retardation already in Paper #19). Operational adequacy. **likely forceable**.
- **M-8: V5 existence as rule-type.** Operational adequacy + cross-scale unification. **likely forceable**.
- **M-9: HYD (hydrodynamic window).** Empirical robustness; possibly **residue** as "necessary assumption for substrate-to-continuum bridge applicability."

**Tier 5 — Residue / late closures:**

- **M-10: P06 ($D = 3+1$).** Likely **residue** under "empirically necessary; deeper structural forcing open in physics generally."
- **M-11: P10 (rule-type primitive).** Likely **residue**: "necessary for substrate to support multiple rule-types (matter + gauge + V1 + V5)."
- **M-12: P12 (stability landscape) + HOL + DEC + IND + THN.** Mostly **residue** with route-appropriate arguments per primitive. Some may collapse to joint papers.

### 4.3 Expected outcome summary

Of ~16 load-bearing primitives:
- **~6–8 likely forceable** under one or more of Routes A–E (P04 core, P09, P04 §1.5, P11 partial, P03, P07, V1 existence, V5 existence).
- **~4–6 mixed** (P11 commitment-existence, joint symmetry primitives, four-band exact count).
- **~4–6 likely residue** (P06 $D=3$, P10 rule-type, HYD, P12, HOL, DEC).

**Honest forecast.** ED will exit the primitive-forcing arc with a mix of fully-forced primitives + honest-residue commitments. The residue commitments will be explicitly named ("minimum operational adequacy," "necessary for compositional closure," "empirically necessary") — substantially stronger than the current displaced-postulate framing, even where full upstream-forcing fails.

---

## Section 5. Downstream Update Map (Which Papers to Update After Each Primitive Closes)

When primitive **$P$** closes (in paper M-k), the following downstream papers must update their §3.0 Primitive Inputs to replace "load-bearing input" with "now forced upstream by M-k":

| Primitive closes | Update §3.0 in papers... |
|---|---|
| **P09 ($U(1)$ polarity)** | #1, #2, #3, #5, #16, #17 |
| **P04 core** | #1, #2, #3, #6, #13, #14, #16, #17 |
| **P04 §1.5** | #3, #6, #11, #15, #17 |
| **P11** | #2, #14, #17, #19 |
| **P03** | #1, #12, #17 |
| **P07** | #1, #2, #17 |
| **V1** | #10, #18, #19 |
| **P13** | #4, #17 |
| **P06** | #7, #12, #17 |
| **GAL / POI** | #6, #7, #15, #17 |
| **V5** | #10 |
| **HYD** | #8, #10 |
| **P10** | #5 |
| **HOL / DEC / P12** | #9 |
| **IND** | #7 |
| **THN** | #13 |

**Note on the cumulative load:** Closing P09 + P04 + P04 §1.5 (Tiers 1+2) cumulatively touches Papers #1, #2, #3, #6, #11, #13, #14, #15, #16, #17 — i.e., 10 of 19 papers. These three closures handle the bulk of the displaced-postulate critique.

---

## Section 6. Circularity Audit

**Concern.** Forcing P09 (Meta-Paper M-1) must not invoke any Forcing Paper #1–#19 result, since P09 is upstream of all of them. Specifically, M-1 cannot:

- Invoke the participation measure (Paper #1) as input — Paper #1 is *downstream* of P09.
- Invoke the Born rule (Paper #2) — also downstream.
- Invoke the Hilbert-space arena (Paper #3) — downstream.

**Permitted inputs for M-1:**

- The meta-substrate framework $\{C^*\}$ established in Meta-Paper §5.
- Background mathematics: Frobenius classification, compact Lie group theory, Coecke-Kissinger categorical-QM framework, real analysis.
- The structural-normative goal (Route B): "the substrate must support recovery of empirically observed physics."

**Methodological discipline.** Each primitive-forcing paper must explicitly check that its forcing argument does not invoke any *downstream* result. The dependency graph here serves as the circularity-audit reference: a primitive's forcing argument may invoke only:
- Background mathematics.
- The meta-substrate framework.
- Already-closed primitive-forcing papers (M-k with $k < $ current paper).

**Closure ordering preservation.** Tier-1 closures (M-1 = P09, M-2 = P04 core) are mutually independent under the forcing routes proposed (P09 via Frobenius + Coecke-Kissinger; P04 via Shannon-Khinchin). Closing in either order is acceptable. Tier-2 onward presumes Tier-1 is closed.

---

## Section 7. Summary

The ED program has **~16 load-bearing substrate primitives**, identified across Forcing Papers #1–#19 via the Phase-1 §3.0 audit. Of these:

- **3 are HIGH-centrality** (P04 core, P09, P04 §1.5) — closing them updates ~10 of 19 papers.
- **4 are MED-centrality** (P11, P03, P07, V1).
- **9 are LOW-centrality** — many likely residue.

The recommended forcing priority is **P09 first (M-1)**, since:
- Highest impact on the displaced-postulate critique (reviewer-targeted).
- Clearest forcing routes (Routes A + E).
- Lowest residue risk.
- Updates 6 downstream papers (#1, #2, #3, #5, #16, #17).

Followed by P04 core (M-2), P04 §1.5 (M-3), P11 (M-4), and the joint symmetry primitives (M-5).

The residue-class primitives (P06, P10, P12, HOL, DEC, HYD, etc.) close later with honest residue-category framings rather than forcing-from-nothing claims.

The full primitive-forcing arc is expected to require **8–12 papers** depending on whether some primitives are jointly forced. Total program length comparable to the Forcing Series Wave 1 (Papers #1–#10).

---

## Section 8. Post-Consolidation Graph (2026-05-13)

After M-1 through M-4 closures + UPDATE_PLAN applications across Papers #1–#17:

### 8.1 Updated DAG visualization

```
                ┌─────────────────────────── PRIMITIVES (root layer) ───────────────────────────┐
                │                                                                                │
            ┌───┴───┐    ┌──────┐   ┌──────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐   ┌────┐
            │P04 core│   │P04   │   │ P09  │   │P03 │   │P07 │   │P11 │   │P13 │   │P06 │
            │FORCED  │   │§1.5  │   │FORCED│   │FRCD│   │PEND│   │PART│   │FRCD│   │RES │
            │ M-2 ✅ │   │FRCD✅│   │ M-1✅│   │M-4✅│   │M-6 │   │ M-3│   │M-4✅│   │  🔴│
            └─┬───────┘  └─┬────┘   └──┬───┘   └─┬──┘   └─┬──┘   └─┬──┘   └─┬──┘   └─┬──┘
              │            │           │         │        │         │        │       │
              │            │           │         │        │         │        │       │
              ▼            ▼           ▼         ▼        ▼         ▼        ▼       ▼
        ┌────────────────────────────────────────────────────────────────────────────────┐
        │                                                                                │
        │   Forcing Papers #1–#19 (§3.0 entries cumulatively updated 2026-05-13)         │
        │                                                                                │
        │   Papers fully closed (all §3.0 forced or named residue):                      │
        │     #3 ✓  #4 ✓  #11 ✓  #16 ✓                                                   │
        │                                                                                │
        │   Papers mostly closed (1–2 pending or residue items):                         │
        │     #1 (P07 pending)  #2 (commitment-existence residue)                        │
        │     #5 (P10 pending)  #6 (closed)  #12 (P06 residue)                           │
        │     #14 (commitment-existence residue)  #15 (closed)                           │
        │     #17 (cumulative tracker reflects all)                                      │
        │                                                                                │
        │   Papers with substantial pending content:                                     │
        │     #7 (P06 residue; IND pending)                                              │
        │     #8 (HYD likely residue)                                                    │
        │     #9 (HOL, DEC, P12 mixed/residue)                                           │
        │     #10 (V1, V5 pending M-7, M-8)                                              │
        │     #13 (THN likely residue)                                                   │
        │                                                                                │
        └────────────────────────────────────────────────────────────────────────────────┘
```

**Legend:** ✅ FORCED · ⚠️ Partially forced · 🔴 Honest residue · ⏳ Pending future M-paper

### 8.2 §3.0 status across all 17 in-scope papers

| Paper | §3.0 closure status | Notes |
|---|---|---|
| #1 | ~90% closed | P09 ✅ M-1, P04 ✅ M-2, P03 ✅ M-4; P07 pending M-6 |
| #2 | ~85% closed | P04 ✅ M-2, P11 partial M-3; commitment-existence residue |
| #3 | ~100% closed | P09 ✅ M-1, P04 + P04 §1.5 ✅ M-2 |
| #4 | ~100% closed | P13 ✅ M-4 |
| #5 | ~50% closed | P09 ✅ M-1; P10 pending |
| #6 | ~100% closed | P04 §1.5 ✅ M-2, GAL ✅ M-4 |
| #7 | ~60% closed | POI ✅ M-4 (residue named); P06 residue; IND pending |
| #8 | ~10% closed | HYD likely residue (not yet declared) |
| #9 | ~10% closed | P12, HOL, DEC mixed |
| #10 | ~10% closed | V1, V5 pending; HYD residue |
| #11 | ~100% closed | P04 §1.5 ✅ M-2 |
| #12 | ~70% closed | P03 ✅ M-4; P06 residue |
| #13 | ~50% closed | P04 core ✅ M-2 (indirect); THN residue |
| #14 | ~85% closed | P04 ✅ M-2, P11 partial M-3; commitment-existence residue |
| #15 | ~100% closed | P04 §1.5 ✅ M-2, GAL ✅ M-4 |
| #16 | ~100% closed | P09 ✅ M-1, P04 ✅ M-2 |
| #17 | ~85% closed | Cumulative tracker reflects all 4 M-closures |

**Aggregate:** approximately 75–80% of the §3.0 load-bearing-input lines across all 17 in-scope papers are now upstream-forced (or named residue). Remaining ~20–25% awaits M-5 through M-12 or honest residue declarations.

### 8.3 Update map for next M-papers

[**Superseded by M-Omnibus closure 2026-05-13.** All originally planned M-5 through M-12 updates were executed in a single closure paper. The update map below is retained for historical reference.]

When M-5 (P07) closes, update Papers #1, #2, #17 §3.0 entries.
When M-6 (V1 existence) closes, update Papers #10, #18, #19 §3.0 entries.
When M-7 (V5 existence) closes, update Paper #10 + Arc-D/Arc-E memos.
When M-8 (residue omnibus or per-primitive) closes, update Papers #7, #8, #9, #13 §3.0 entries.

---

## Section 9. Post-Omnibus Graph Snapshot (2026-05-13, M-Series TERMINAL)

### 9.1 Updated DAG visualization — final state

```
                ┌─────────────── PRIMITIVES (root layer, all closed) ────────────────┐
                │                                                                    │
   ┌─────────┐ ┌──────┐ ┌──────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐
   │P04 core │ │P04   │ │ P09  │ │P03 │ │P07 │ │P11 │ │P13 │ │P06 │ │GAL │ │POI │
   │FORCED ✅│ │§1.5 ✅│ │FRCD ✅│ │FRCD│ │FRCD│ │PART│ │FRCD│ │RES │ │FRCD│ │PART│
   │  M-2    │ │ M-2  │ │  M-1 │ │M-4✅│ │M-Ω✅│ │M-3 │ │M-4✅│ │M-Ω🔴│ │M-4✅│ │M-4 │
   └─┬───────┘ └─┬────┘ └──┬───┘ └─┬──┘ └─┬──┘ └─┬──┘ └─┬──┘ └─┬──┘ └─┬──┘ └─┬──┘
     │           │         │       │      │      │      │      │      │      │
     ▼           ▼         ▼       ▼      ▼      ▼      ▼      ▼      ▼      ▼

   ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
   │ V1  │ │ V5  │ │ P10 │ │ P12 │ │ HYD │ │ HOL │ │ DEC │ │ IND │ │ THN │
   │PART │ │PART │ │RES  │ │RES  │ │RES  │ │RES  │ │RES  │ │RES  │ │RES  │
   │M-Ω⚠️ │ │M-Ω⚠️ │ │M-Ω🔴│ │M-Ω🔴│ │M-Ω🔴│ │M-Ω🔴│ │M-Ω🔴│ │M-Ω🔴│ │M-Ω🔴│
   └──┬──┘ └──┬──┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘
      │       │
      ▼       ▼
        ┌────────────────────────────────────────────────────────┐
        │                                                        │
        │       All 19 load-bearing items CLOSED                 │
        │       with definite structural status.                 │
        │                                                        │
        │       M-series TERMINAL (M-Omnibus 2026-05-13).        │
        │                                                        │
        │       Forcing Papers #1–#19 §3.0 entries fully         │
        │       reflect upstream-forced or named-residue status. │
        │                                                        │
        └────────────────────────────────────────────────────────┘
```

**Legend:** ✅ Fully FORCED · ⚠️ Partially FORCED with named residue · 🔴 Honest RESIDUE declared

### 9.2 §3.0 status across all in-scope papers (final state)

| Paper | §3.0 closure | Notes |
|---|---|---|
| #1 | 100% closed | P04 ✅, P09 ✅, P03 ✅, P07 ✅ — all forced |
| #2 | ~90% closed | P04 ✅, P11 partial (commitment-existence residue), Paper #1 inheritance ✅ |
| #3 | 100% closed | P09 ✅, P04 + §1.5 ✅ |
| #4 | 100% closed | P13 ✅ |
| #5 | ~95% closed | P09 ✅; P10 residue declared |
| #6 | 100% closed | P04 §1.5 ✅, GAL ✅ |
| #7 | ~85% closed | POI partial (cosmo residue); P06 residue; IND residue |
| #8 | ~90% closed | HYD residue declared |
| #9 | ~90% closed | P12, HOL, DEC residue declared |
| #10 | ~85% closed | V1 partial, V5 partial; HYD residue |
| #11 | 100% closed | P04 §1.5 ✅ |
| #12 | ~95% closed | P03 ✅; P06 residue |
| #13 | ~95% closed | P04 ✅ (indirect); THN residue declared |
| #14 | ~90% closed | P04 ✅, P11 partial |
| #15 | 100% closed | P04 §1.5 ✅, GAL ✅ |
| #16 | 100% closed | P09 ✅, P04 ✅ |
| #17 | ~95% closed | Cumulative tracker reflects all 5 M-closures including Omnibus |
| #18 | ~95% closed | V1 existence ✅, P11 ✅, P07 ✅ (§3.0 added in Omnibus update) |
| #19 | ~95% closed | P11 ✅, V1 ✅, P07 ✅ (§3.0 added in Omnibus update) |

**Aggregate:** approximately **93–95%** of all §3.0 load-bearing-input lines across the 19 in-scope papers are now either upstream-forced or explicitly named residue. The displaced-postulate critique is substantively eliminated across the entire Forcing Series.

### 9.3 M-series chain (terminal)

```
{C*} ─→ M-1 ─→ M-2 ─→ M-3 ─→ M-4 ─→ M-Omnibus ━━ TERMINAL ━━
        │       │       │       │           │
        ▼       ▼       ▼       ▼           ▼
       P09    P04     P11    P03+P13      P07
              core+  irrev. +GAL+POI    V1+V5
              §1.5   +φ-rand           existence
                                       +residue
                                       cluster
```

The M-series is now closed. No further M-papers are planned. References to "M-5 through M-12" in earlier program documents are superseded by the M-Omnibus closure.
