# Topology / Reach / Σ-law Sweep — Exploratory Foundations Note + Sweep Plan

**Exploratory behavior-space characterization. Not a substrate change, not a primitive edit, not a theory change.**
Maps the dynamical repertoire ED *already supports* by varying (1) graph topology, (2) reach/adjacency structure, and (3) Σ-law coefficients — while holding every certified invariant fixed.
**Source basis:** the Bits simulator (`Bits/simulator/{graph,sigma,update,strata}.py`); the certified Σ-rule `Σ = kc·Coh − ks·Strain − kg·Grad`; the A1 capacity results; the B4 arc (orientation-blindness + weak channel); the Emergent-Decoupling-Surfaces note.

---

## 0. Framing and the held invariants

This is a parameter-and-structure sweep *within* the certified rule family — not a rule change. Across the entire sweep the following are **held fixed** (they define the family):

- **Orientation-blindness** — `compute_sigma` reads ρ + graph structure only, never orientation (hard invariant, `sigma.py`).
- **Irreversibility (P11/B7)** — ρ is monotone non-decreasing; `commit()` is the sole writer.
- **Fixed graph** — the dynamics evolve node state on a static graph; no rule modifies edges, bandwidth, or decoupling flags (see the Emergent-Decoupling note). Topology is therefore an *input* we vary between runs, never *within* a run.
- **Determinism + total-order tie-break** — `apply_tiebreak` resolves Σ-ties by `(bw, node_id)`; runs are reproducible.
- **State-acyclicity (Gate 2)** — every recorded global state is distinct; genuine limit cycles are gated out (spatial circulation around a graph cycle is still possible as a transient).

What we vary are the three knobs the certified machinery already exposes: the graph handed to `ParticipationGraph`, its reach profile, and the `SigmaCoeffs`. Nothing below proposes a new term, a new primitive, or an edge-modifying rule.

*Implementation note (honest):* the named topology classes (RING/GRID/TREE/STAR/RANDOM/LATTICE/CSAT/SMALL-WORLD/SCALE-FREE) are **not** a pre-existing module — the repo currently has only ad-hoc per-demo builders (`build_path` = chain, `build_two_clusters`, the milestone1 center-plus-three-leaves star, `build_substrate` = two chains + decoupled bridge). The sweep plan (§5) therefore proposes a small **topology factory** built on the existing `ParticipationGraph.add_node/add_edge` API; it constructs the classes, it does not assume them.

## 1. The three sweep axes

**A. Topology axis (P02 adjacency).** Vary the adjacency structure: RING (degree-2 cycle, b₁=1), PATH/CHAIN (linear, the certified-arc default), GRID/LATTICE (degree-4, 2-D wavefronts; the B4 substrate), TREE (acyclic, b₁=0, hierarchical), STAR (one hub, articulation bottleneck), RANDOM (Erdős–Rényi, short diameter, many cycles), SMALL-WORLD (high clustering + shortcut bridges), SCALE-FREE (hub-dominated), CSAT (clustered constraint-graph). *Primitive correspondence:* P02 (participation/adjacency) — this axis *is* the participation graph. *Expected effect:* sets reachability, cycle structure, bottlenecks, and how many strata an installed cut produces.

**B. Reach axis (degree / diameter / clustering).** Within or across topology classes, vary mean degree, diameter, clustering coefficient, and local-vs-global connectivity (e.g. Watts–Strogatz rewiring probability). *Primitive correspondence:* P02 (adjacency density) + P04/P05 (which neighbors carry bandwidth/transport). *Expected effect:* degree sets candidates-per-front (selectivity of Σ); diameter sets global propagation time; clustering localizes domains; bottlenecks/hubs gate fronts (the structural analogue of a soft barrier — cf. the Emergent note's ρ-wall, but here from the wiring, not the dynamics).

**C. Σ-law axis (the certified terms).** Vary `SigmaCoeffs`: **kc** (Coherence, `Coh = −(ρ_v − ρ*)²`), **ks** (Strain, `= ρ_v`), **kg** (Grad, `= |ρ_v − ρ_u|`), **rho_star** (ρ*), **increment**, **extinction_threshold**; optional toggles such as `kg = 0` (disable gradient penalty) or `kc ≫ ks, kg` (coherence-dominant). *Primitive correspondence:* the extremal-dynamics (P12 stability landscape) acting on ρ (P11 commitment increments). *Expected effect (per term):* high **kc** → fronts seek ρ* → uniform coherent domains; high **ks** → fronts avoid dense nodes → spreading, anti-saturation; high **kg** → fronts follow ρ level-sets → smooth, contour-following, can trap; high **extinction_threshold** → fronts die sooner → fragmentation; larger **increment** → ρ grows faster → hits the strain penalty sooner.

## 2. Behavioral taxonomy (expected regimes)

- **Propagation regimes:** *ballistic* (steady end-to-end sweep; low kg, low ks), *diffusive* (high-degree/random branching), *contour-trapped* (high kg locks the front onto ρ level-sets), *extinguishing* (high threshold or strain kills fronts early).
- **Collapse vs spread:** Coherence (kc) *collapses* the field toward ρ* domains; Strain (ks) *spreads* it by repelling dense targets. The kc/ks ratio is the primary collapse–spread dial.
- **Stable domains:** kc builds uniform-ρ* domains; clustering topology (SMALL-WORLD, CSAT) localizes them into multiple coexisting domains.
- **Oscillatory / cycling:** true limit cycles are gated out (acyclicity, Gate 2); in cyclic topologies (RING, RANDOM) the front can *circulate* spatially once (transient), and — under an extended U(1) layer — carry the B4 winding; with orientation-blindness held, circulation is ρ-driven only.
- **Fragmentation vs coherence:** high extinction_threshold + sparse/low-degree topology → fronts die at bottlenecks → fragmented committed patches; low threshold + dense topology → coherent full coverage.
- **Topology sensitivity:** articulation points (STAR hub, TREE root, SCALE-FREE hubs) gate propagation; long diameter slows it; cycles enable circulation; the strata count under an installed cut tracks the reciprocal-subgraph component structure.

## 3. Cross-axis interactions

- **Topology modulates Strain/Grad.** kg (gradient penalty) traps more strongly in *low-degree* topologies: a chain front must cross a ρ-gradient head-on (no level-set neighbor to escape to), whereas a GRID front has many iso-ρ neighbors, so the same kg is far less confining. So the *effective* strength of the Grad term is topology-dependent — degree provides escape routes.
- **Reach modulates determinability boundaries.** Where an installed cut sits relative to the reach profile changes Δ: a cut across a high-bandwidth hub severs a richly-correlated stratum (large within-MI), while a cut across a low-degree bridge severs weakly-coupled regions (small within-MI). Reach thus tunes the *contrast* of the boundary even though (per the Emergent note) it cannot *form* one.
- **Σ-law reshapes the effective geometry.** High kg makes the front move along ρ level-sets — an effective foliation/metric on the graph (resonant with the P06 reading that the bandwidth-weighted ρ-gradient is the emergent metric). Tuning kc/ks/kg therefore changes the *effective geometry the front experiences on a fixed graph* — the cleanest demonstration that "geometry" here is dynamical, not wired in.

## 4. Expected-behavior table (topology × Σ-regime)

| Topology ↓ \ Σ-regime → | Coherence-dom (kc↑) | Strain-dom (ks↑) | Grad-dom (kg↑) | High extinction |
|---|---|---|---|---|
| **CHAIN/PATH** | single ρ* domain, ballistic | steady end-to-end spread | strongly contour-trapped (1-D, no escape) | early death → short committed segment |
| **RING** | uniform domain around loop | spread + transient circulation | trapped; circulation along level-set | fragments into arcs |
| **GRID/LATTICE** | broad coherent 2-D domain | wavefront spread | mild trap (many iso-ρ neighbors); smooth fronts | patchy 2-D fragments |
| **TREE** | coherent per-branch domains | spread down branches | branch-local trapping | leaves die first → pruned tree of commits |
| **STAR** | hub-centered domain | hub bottleneck throttles spread | hub tie-break dominates (degenerate Σ) | leaves extinguish, hub persists |
| **RANDOM / SMALL-WORLD** | fast global coherence | rapid diffusive spread | weak trap (high degree) | scattered fragments, shortcut-seeded |
| **SCALE-FREE** | hub-funneled domains | hubs saturate then repel (ks) | hub-dominated, periphery trapped | periphery dies, hub-core survives |

*(Cells are expected/hypothesized regimes to be confirmed by the sweep, not measured results.)*

## 5. Proposed sweep plan (structured outline)

```
# topology_factory.py  — built ONLY on ParticipationGraph.add_node/add_edge
def make(topology, n, **p) -> (graph, seed_nodes):
    RING    : nodes 0..n-1, edges (i, i+1 mod n)
    CHAIN   : edges (i, i+1)
    GRID    : sqrt(n) x sqrt(n), 4-neighbour
    TREE    : balanced b-ary tree (p['branch'])
    STAR    : hub 0 to leaves 1..n-1
    RANDOM  : Erdos-Renyi G(n, p['p_edge'])
    SMALLWORLD: Watts-Strogatz (p['k'], p['beta'])
    SCALEFREE : Barabasi-Albert (p['m'])
    CSAT    : clustered constraint graph (p['clusters'], p['intra'], p['inter'])
    # bandwidth: default 1.0; optional p['bw_profile'] (uniform / degree-weighted / random)
    # NO decoupled flags unless a cut is explicitly installed for the Delta measurement

SIGMA_GRID = product over:
    kc in {0.5, 1, 2}, ks in {0.5, 1, 2}, kg in {0, 1, 2},
    rho_star in {0.3, 0.5}, extinction_threshold in {None, -2.0, -0.5}

for topo in TOPOLOGIES:
  for reach in REACH_PROFILES[topo]:          # degree / diameter / clustering variants
    g, seeds = make(topo, n, **reach)
    for coeffs in SIGMA_GRID:
      for seed in SEEDS:                       # random init ensemble for Delta
        sv = init_state(g, seed)               # rho ~ U(0,0.5), orientation random
        strata = assign_stratum_ids(sv, g)
        traj = run_to_fixed_point(sv, g, coeffs, strata, recorder=on)
        record METRICS(traj, g, sv)            # see Section 6
# Hold fixed: orientation-blind Sigma, monotone rho, static graph, deterministic tie-break.
# Optional Delta sub-sweep: install ONE reciprocal cut per topology, measure within vs across MI.
```

Run order is cheap → expensive: small n (≤64) full grid first to locate regime boundaries, then targeted larger-n confirmation on the interesting cells. Deterministic per (topo, reach, coeffs, seed) ⇒ fully reproducible.

## 6. Measurable outputs

- **Front speed** — commits per step until fixed point (ballistic vs diffusive vs trapped).
- **Collapse time** — steps to fixed point (extinction vs full coverage).
- **Coverage fraction** — committed nodes / total (fragmentation vs coherence).
- **Domain count** — number of connected committed regions; and number of distinct ρ-level domains (coherence structure).
- **Coherence metric** — variance of ρ about ρ* (how tightly Coherence pulled the field).
- **Penetration depth / fragmentation index** — how far fronts reach past bottlenecks; patch-size distribution.
- **Δ across installed cuts** — within-stratum − across-boundary MI (the A1/Bits observable), as a function of topology and reach.
- **Circulation** — for cyclic topologies, net front winding around a cycle (transient; the ρ-only analogue of B4's winding).
- **Tie-break load** — fraction of commits decided by tie-break vs strict Σ-max (how degenerate the Σ landscape is — high in symmetric topologies/STAR hubs).

## 7. What the sweep can and cannot show

It can **characterize** how the certified dynamics behave across the structure×coefficient space — the regime map, the cross-axis interactions, the effective-geometry reshaping. It **cannot** (and is not designed to) produce emergent boundaries, modify the graph, or change any invariant — those are held fixed by construction. The value is a behavior-space atlas of the certified rule family: which topologies + tunings give ballistic vs trapped vs fragmented dynamics, how Δ depends on where a cut sits, and how Σ-weights reshape the effective geometry on a fixed graph.

---

*Exploratory note + plan only. No corpus edits, no new primitives, no rule changes. Suitable for `evaluation/TopologySweep/`; runs against the certified Bits simulator via a topology factory on the existing `ParticipationGraph` API.*
