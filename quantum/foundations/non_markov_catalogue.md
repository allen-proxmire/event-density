# Catalogue of Admissible Non-Markovian Structures

**Arc N Stage N.1 — Catalogue Memo**
**Status:** Catalogue only. Enumerates every non-Markovian structure consistent with ED Primitives 01–13 across four sectors: N1 bandwidth-memory (5 items), N2 commitment-memory (5 items), N3 adjacency-memory (5 items), V vacuum-response (5 items). Each item characterised by primitive dependencies and potential constraint-violation flags (C1 Lorentz, C2 spin-statistics, C3 UV-FIN). **No FORCED / REFUTED evaluation in this memo** — those are Stage N.2 and N.3 deliverables. The catalogue's purpose is to ensure no admissible structure is missed before evaluation begins.

---

## 1. Framing

### 1.1 Recap of Arc N scope

The Arc N opening memo [1] established:

- ED is **Markov-compatible but not Markov-forcing.** No primitive in 01–13 explicitly forbids history-dependence in bandwidth content, commitment dynamics, or multi-chain adjacency relations.
- Non-Markovianity may arise in three sectors: **N1 bandwidth-memory** (history-dependent $b_K^X$ evolution), **N2 commitment-memory** (history-dependent individuation thresholds and commitment rates), **N3 adjacency-memory** (history-dependent multi-chain correlations).
- A fourth sector, **vacuum-response (V)**, draws on Arc Q.8's effective-vacuum framework as a natural site for finite-width memory kernels.

Three potential constraints frame what *might* be ruled out at Stage N.3:

- **C1 (Lorentz covariance):** memory kernels must be Lorentz-scalar combinations.
- **C2 (Spin-statistics):** non-Markovian extensions must preserve $\eta = (-1)^{2s}$.
- **C3 (UV-FIN):** memory kernels must preserve primitive-level UV finiteness from Arc Q [2] Theorem Q3.

### 1.2 Scope of this memo

Stage N.1 catalogues. Stage N.2 evaluates FORCED candidates. Stage N.3 evaluates REFUTED candidates. The catalogue is intentionally inclusive — it lists structures that *may* later be REFUTED at Stage N.3, alongside structures that survive constraint-checking. Premature filtering would risk omitting forms that pass constraints under refined analysis.

### 1.3 Notation

Throughout this memo:

- $b_K^X(x^\mu)$ denotes the band-X bandwidth amplitude at event $x^\mu$ for chain $K$.
- $\tau_K$ denotes proper time along $\gamma_K$.
- $K(\Delta\tau)$ denotes a generic memory kernel as a function of proper-time difference.
- $\tau_\mathrm{mem}^X$ denotes a characteristic memory timescale per band.
- "Markovian limit" corresponds to $K(\Delta\tau) \to \delta(\Delta\tau)$.

---

## 2. N1 — Bandwidth-Memory Structures

Bandwidth-memory: the four-band amplitudes $b_K^X(x^\mu)$ at event $x^\mu$ depend on a history-weighted integral over prior events along $\gamma_K$, rather than only on the participation amplitude at $x^\mu$.

### 2.1 N1-A — Finite-width memory kernels in $b^\mathrm{env}$

**Description.** The environment-coupled bandwidth $b_K^\mathrm{env}$ at event $x^\mu$ is a finite-width history-weighted integral over participation along $\gamma_K$:
$$
b_K^\mathrm{env}(x^\mu) = \int_{-\infty}^{\tau_K(x^\mu)} K_\mathrm{env}(\tau_K(x^\mu) - \tau') \cdot p_K(\tau') \, d\tau',
$$
with $K_\mathrm{env}$ a bounded kernel of finite width $\tau_\mathrm{mem}^\mathrm{env}$. This is the most natural non-Markovian extension: environments respond to perturbations on finite timescales, naturally producing memory in the environment-coupled band.

**Primitive dependencies.** Primitive 04 (four-band decomposition supplies $b^\mathrm{env}$); Primitive 11 (commitment events as the participation source); Primitive 13 (proper-time parameter for the integral).

**Potential constraint violations.** None obvious at this stage. C1 satisfied if $K_\mathrm{env}$ is a function of proper-time difference (Lorentz scalar). C3 satisfied if $K_\mathrm{env}$ is bounded at $\Delta\tau \to 0$.

**Notes.** Most plausibly active in dissipative / environment-coupled rule-types. The Markovian limit is the standard Lindblad-style assumption.

### 2.2 N1-B — History-weighted spectral-rate terms

**Description.** Arc M's σ_τ master formula uses the proper-time average $\langle (\partial_\mu \ln b_\tau^X)(\partial^\mu \ln b_\tau^X) \rangle_\tau$. In the non-Markovian extension, the average becomes a memory-weighted integral:
$$
\langle (\partial \ln b)^2 \rangle_\tau^\mathrm{NM} = \int W(\Delta\tau) \cdot (\partial \ln b)^2(\tau - \Delta\tau) \, d\Delta\tau,
$$
with $W(\Delta\tau)$ a weighting function. The σ_τ formula gains memory content via $W$.

**Primitive dependencies.** Primitive 04; Primitive 06 (four-gradient for $\partial_\mu \ln b$); Primitive 11 (event accumulation); Primitive 13 (proper-time parameter).

**Potential constraint violations.** C1 if $W$ is not a Lorentz-scalar function of $\Delta\tau$. C3 if $W$ is unbounded at small $\Delta\tau$.

**Notes.** This modifies Arc M's σ_τ structure — see N.4 cross-arc implications. Could in principle generate effective σ_τ shifts not present in the Markovian formula; whether it can produce mass-differentiation across rule-types is for N.4 analysis.

### 2.3 N1-C — Multi-scale bandwidth memory

**Description.** Bandwidth content evolves with multiple characteristic memory timescales simultaneously: a fast scale $\tau_\mathrm{mem}^\mathrm{fast}$ (e.g., environment-equilibration) and a slow scale $\tau_\mathrm{mem}^\mathrm{slow}$ (e.g., long-range vacuum coupling). The kernel decomposes:
$$
K(\Delta\tau) = c_\mathrm{fast} \cdot K_\mathrm{fast}(\Delta\tau) + c_\mathrm{slow} \cdot K_\mathrm{slow}(\Delta\tau).
$$
Multiple bands may carry different scale combinations.

**Primitive dependencies.** Primitive 04 (multiple bands admit independent kernel scales); Primitive 11 + 13.

**Potential constraint violations.** C3 if any sub-kernel violates UV-finiteness. C2 if multi-scale structure introduces statistics-class mixing across scales.

**Notes.** Plausibly relevant for hierarchical-coupling regimes (e.g., atomic + cosmological scale separation). Multi-scale structure is well-studied in renormalisation-group analysis.

### 2.4 N1-D — Cross-band memory coupling

**Description.** The memory kernel for one band depends on the history of another band — i.e., $b^\mathrm{int}$ at event $x^\mu$ depends on prior $b^\mathrm{env}$ history, or vice versa:
$$
b_K^\mathrm{int}(x^\mu) = \int K_{\mathrm{int}\leftarrow\mathrm{env}}(\Delta\tau) \cdot b_K^\mathrm{env}(\tau_K - \Delta\tau) \, d\Delta\tau + (\text{Markovian internal contribution}).
$$
This represents non-trivial cross-band history-coupling beyond the four-band decomposition's standard structure.

**Primitive dependencies.** Primitive 04 (four-band structure); Primitive 11; Primitive 13. Possibly Primitive 07 L1 (band-weighting) if cross-band coupling is rule-type-specific.

**Potential constraint violations.** C2 in restricted cases — cross-band coupling between Case-P and Case-R sectors of a multi-rule-type system might mix statistics in problematic ways. Stage N.3 will evaluate whether all cross-band couplings are admissible or only a subset.

**Notes.** Catalogue includes Case-P ↔ Case-R cross-coupling speculatively; Stage N.3 will determine whether such couplings are REFUTED by C2.

### 2.5 N1-E — Vacuum-induced bandwidth memory

**Description.** The bandwidth-memory kernel for a chain is induced by the chain's coupling to the effective vacuum (Arc Q.8). The vacuum's response to chain participation acts as the source of bandwidth-memory: $K(\Delta\tau)$ inherits structure from the vacuum-response kernel rather than being chain-intrinsic.

**Primitive dependencies.** Arc Q.8 effective-vacuum framework; Primitive 04; Primitive 11; Primitive 13. Couples the bandwidth-memory mechanism to the vacuum-response sector V.

**Potential constraint violations.** Inherits constraints from V-sector kernels (see §5). Likely C1 and C3 must be checked at the vacuum-response level.

**Notes.** Most plausible candidate for *FORCED* non-Markovian structure under Stage N.2 evaluation: if vacuum response under UV-FIN requires finite-width kernels (rather than δ-function response), and bandwidth-memory inherits this kernel structure, N1-E could be primitively forced.

---

## 3. N2 — Commitment-Memory Structures

Commitment-memory: the Primitive 10 individuation threshold and Primitive 11 commitment rate at event $x^\mu$ depend on the rule-type's commitment-event history along $\gamma_K$, not only on the current bandwidth state.

### 3.1 N2-A — Thresholds depending on past event density

**Description.** The Primitive 10 individuation threshold at event $x^\mu$ depends on the local density of prior commitment events near $x^\mu$ on $\gamma_K$:
$$
\Theta_K(x^\mu) = \Theta_K^{(0)} + \alpha \cdot \int_{-\infty}^{\tau_K(x^\mu)} W_\Theta(\tau_K(x^\mu) - \tau') \cdot \rho_\mathrm{events}(\tau') \, d\tau',
$$
with $\Theta_K^{(0)}$ the baseline threshold, $\alpha$ a coupling strength, $W_\Theta$ a weighting function, and $\rho_\mathrm{events}$ the local commitment-event density.

**Primitive dependencies.** Primitive 10 (individuation threshold); Primitive 11 (commitment-event density); Primitive 13.

**Potential constraint violations.** C1 if $W_\Theta$ is not Lorentz-scalar. C2 if threshold-shift behaviour differs systematically between Case-P and Case-R in problematic ways.

**Notes.** Most natural realisation of "refractory-period" effects: a chain that has recently undergone many commitment events has a temporarily-elevated threshold.

### 3.2 N2-B — Hysteresis-style commitment (delayed individuation)

**Description.** When a chain's bandwidth crosses the individuation threshold from below, individuation does not occur instantaneously; instead, individuation requires the bandwidth to remain above threshold for a finite memory time $\tau_\mathrm{hys}$. Conversely, individuation persists for $\tau_\mathrm{hys}$ after the bandwidth drops below threshold. This produces hysteresis in the individuation state.

**Primitive dependencies.** Primitive 10; Primitive 11; Primitive 13. The hysteresis mechanism is a structural extension of Primitive 10's threshold-crossing dynamics.

**Potential constraint violations.** C2 in subtle ways — hysteresis could in principle delay Pauli-exclusion enforcement at finite memory range, threatening the spin-statistics theorem's primitive-level FORCED status. Stage N.3 evaluation needed.

**Notes.** Familiar from condensed-matter contexts (magnetic hysteresis, ferroelectric hysteresis). Whether it survives the stricter primitive-level constraint structure of ED is an N.3 question.

### 3.3 N2-C — Memory-weighted commitment spacing

**Description.** The probability of a commitment event at proper time $\tau_K$ depends on the memory-weighted history of recent commitments:
$$
P_\mathrm{commit}(\tau_K) = P_0 \cdot f\left( \int K_\mathrm{spacing}(\tau_K - \tau') \cdot \mathbb{1}_{\mathrm{event\ at\ }\tau'} \, d\tau' \right),
$$
with $f$ a function (e.g., suppressing the rate when recent events are dense).

**Primitive dependencies.** Primitive 11 (commitment events); Primitive 13 (proper-time parameter); Primitive 04 (bandwidth amplitude as $P_0$ source).

**Potential constraint violations.** C3 if $K_\mathrm{spacing}$ has insufficient short-time decay, amplifying high-frequency contributions. C1 if not Lorentz-scalar.

**Notes.** The natural generalisation of Poisson-process commitment to a renewal-process-like structure with memory. Stage N.2 will evaluate whether any primitive forces a specific spacing kernel.

### 3.4 N2-D — Multi-chain commitment correlations

**Description.** The commitment dynamics of chain $K_1$ at event $x^\mu_1$ depend on the recent commitment history of an adjacent chain $K_2$ at events $\{x^\mu_{2,1}, x^\mu_{2,2}, \dots\}$ along $\gamma_{K_2}$. This is multi-chain memory at the commitment level — beyond Primitive 10's instantaneous individuation pairing.

**Primitive dependencies.** Primitive 10 (individuation pairing); Primitive 11 (commitment events on multiple chains); Primitive 13.

**Potential constraint violations.** C1 (multi-chain memory must respect Lorentz covariance across multi-event configurations). C2 (correlation structure must preserve spin-statistics across chains). C3 (correlation kernels must preserve UV-FIN).

**Notes.** Could in principle generalise Bell-correlation analogues (Phase-1) to multi-event temporal-correlation structures. This is closely related to N3 (adjacency-memory).

### 3.5 N2-E — Vacuum-modulated commitment memory

**Description.** Commitment-event rates and thresholds depend on the local effective-vacuum state. A chain in a high-vacuum-fluctuation region experiences modified commitment dynamics relative to a chain in a low-vacuum-fluctuation region. The memory content arises because the vacuum state itself responds with finite-width kernels to perturbations.

**Primitive dependencies.** Primitive 10; Primitive 11; Arc Q.8 effective-vacuum framework. Couples N2 to the V-sector vacuum-response structures.

**Potential constraint violations.** Inherits constraints from V-sector kernels.

**Notes.** Plausibly relevant for cosmological-scale dynamics where local vacuum state varies (e.g., near horizons, in regions of inflationary expansion). A natural Phase-3 hand-off candidate.

---

## 4. N3 — Adjacency-Memory Structures

Adjacency-memory: multi-chain adjacency graphs encode temporal correlations across adjacency-graph evolution. Two chains that have been adjacent for a long time may carry persistent correlation structure beyond their instantaneous state.

### 4.1 N3-A — Time-lagged adjacency graphs

**Description.** The Primitive 10 adjacency relation at event $x^\mu$ between chains $K_1, K_2$ depends not only on instantaneous distinguishability but on their adjacency history over a memory timescale $\tau_\mathrm{adj}$:
$$
A_{K_1 K_2}(x^\mu) = f\left( A_{K_1 K_2}^\mathrm{instant}(x^\mu), \; \int K_\mathrm{adj}(\Delta\tau) \cdot A_{K_1 K_2}^\mathrm{instant}(\tau_K - \Delta\tau) \, d\Delta\tau \right).
$$
Adjacency is a smoothed, memory-bearing relation rather than instantaneous.

**Primitive dependencies.** Primitive 10 (adjacency relation); Primitive 11 (events along multiple chains); Primitive 13.

**Potential constraint violations.** C1 (multi-chain temporal kernel must be Lorentz-scalar). C2 (smoothed adjacency must preserve Pauli exclusion at the structural level).

**Notes.** Generalises the Q.2 R-2 closure (gauge-quotient adjacency-equivalence-class construction) to *adjacency-equivalence-trajectory* structures.

### 4.2 N3-B — History-dependent adjacency weights

**Description.** The strength of adjacency between two chains at event $x^\mu$ is weighted by the duration and continuity of their prior adjacency history:
$$
w_\mathrm{adj}(K_1, K_2; x^\mu) = w_0 + \beta \cdot \int W_\mathrm{adj}(\Delta\tau) \cdot \mathbb{1}_{K_1 \text{ adjacent to } K_2 \text{ at } \tau - \Delta\tau} \, d\Delta\tau.
$$
Long-standing adjacencies carry stronger weight than transient ones.

**Primitive dependencies.** Primitive 10; Primitive 11; Primitive 13. Possibly Primitive 07 L3 (interface content) if adjacency-weight content is rule-type-specific.

**Potential constraint violations.** C3 if $W_\mathrm{adj}$ has insufficient decay.

**Notes.** Naturally produces "entanglement-persistence" effects — chains that have shared participation extensively retain correlation content.

### 4.3 N3-C — Multi-chain correlation kernels

**Description.** Adjacency-memory generalises to multi-chain kernels: the joint participation of three or more chains at event $x^\mu$ depends on the multi-chain history. Higher-order kernels $K(K_1, K_2, K_3; \Delta\tau_1, \Delta\tau_2)$ encode triple-correlation memory.

**Primitive dependencies.** Primitive 10 (multi-chain pairing); Primitive 11 (multi-chain events); Primitive 13.

**Potential constraint violations.** C2 (multi-chain correlation structure must preserve Pauli exclusion in Case-R sub-sectors). C3 (high-order kernels must preserve UV-FIN; high-order memory structure could amplify divergences in continuum approximation).

**Notes.** The generalisation toward $n$-point temporal correlation functions with memory; closely related to non-equilibrium QFT correlation-function structure.

### 4.4 N3-D — Vacuum-mediated adjacency memory

**Description.** Adjacency between two chains is mediated by the effective vacuum's response to their joint participation. The vacuum carries memory of past adjacency configurations and influences current adjacency strength via this memory.

**Primitive dependencies.** Primitive 10; Arc Q.8 effective-vacuum framework. Couples N3 to V-sector vacuum-response structures.

**Potential constraint violations.** Inherits from V-sector kernels.

**Notes.** Analogous to vacuum-mediated forces in standard QFT (e.g., Casimir-Polder forces). Plausibly relevant for cosmological-scale chain correlations.

### 4.5 N3-E — Non-local adjacency propagation

**Description.** Adjacency information propagates along the event manifold with memory: two chains separated by spacelike intervals can share correlated adjacency content if their lightcones intersect at past events where adjacency was established. Non-local in the sense that adjacency at $x^\mu$ depends on adjacency at points outside $x^\mu$'s strict past lightcone.

**Primitive dependencies.** Primitive 02 (chain worldlines); Primitive 10; Primitive 11; Primitive 13.

**Potential constraint violations.** **C1 is the central concern.** Lorentz covariance plus locality (Primitive 11) jointly restrict admissible non-local-in-spacetime structures. Stage N.3 will likely REFUTE this catalogue item or restrict it to specific frame-independent forms.

**Notes.** Catalogued for completeness; expected to be heavily constrained or REFUTED at Stage N.3. Surviving forms (if any) would respect Lorentz covariance while permitting memory across spacelike intervals — this is closely related to the topology of the event manifold and may connect to Phase-3 cosmological-boundary content.

---

## 5. V — Vacuum-Response Structures (S3-Linked)

Vacuum-response: the effective vacuum (Arc Q.8) responds to chain participation with finite-width kernels rather than instantaneous (δ-function) response. This is the most plausible site for *FORCED* non-Markovian content under UV-FIN constraints (Arc N opening memo §7.3).

### 5.1 V1 — Finite-width vacuum memory kernel

**Description.** The effective vacuum's response to a chain's participation perturbation at event $x^\mu$ is a finite-width kernel:
$$
\delta \langle b^\mathrm{env} \rangle_\mathrm{vac}(x^\mu) = \int K_\mathrm{vac}(x^\mu - x'^\mu) \cdot \delta P_\mathrm{chain}(x'^\mu) \, d^4x',
$$
with $K_\mathrm{vac}$ having finite spatial and temporal width set by primitive event-discreteness scale.

**Primitive dependencies.** Arc Q.8 effective-vacuum framework; Primitive 01 (event-discreteness sets scale); Primitive 04 ($b^\mathrm{env}$ as the vacuum-response channel); Primitive 13.

**Potential constraint violations.** C1 satisfied if $K_\mathrm{vac}$ is a Lorentz-scalar function of $x^\mu - x'^\mu$ (i.e., depends only on the invariant $(x - x')^2$). C3 satisfied automatically by primitive-discreteness boundedness.

**Notes.** Most plausibly the FORCED candidate under UV-FIN: a δ-function vacuum response would amplify high-frequency contributions and threaten UV-FIN; primitive-discreteness already imposes finite-width structure. Stage N.2 will evaluate whether V1 is structurally FORCED.

### 5.2 V2 — Exponential-decay vacuum response

**Description.** The vacuum-response kernel has exponential decay in the proper-time-like invariant $\sqrt{-(x - x')^2}$:
$$
K_\mathrm{vac}(x - x') \propto \exp\left(-\sqrt{-(x - x')^2}/\tau_\mathrm{vac}\right),
$$
with characteristic vacuum-response timescale $\tau_\mathrm{vac}$.

**Primitive dependencies.** Arc Q.8; Primitive 13.

**Potential constraint violations.** C1 satisfied (Lorentz-scalar form). C3 satisfied (exponential decay is bounded).

**Notes.** A specific functional form within V1's class. The exponential is structurally natural (it is the Green's function of a damped field equation) but is not the only admissible form.

### 5.3 V3 — Power-law vacuum response

**Description.** The vacuum-response kernel has power-law structure:
$$
K_\mathrm{vac}(x - x') \propto \frac{1}{(-(x - x')^2)^\alpha},
$$
with exponent $\alpha$ to be determined empirically or constrained by C3.

**Primitive dependencies.** Arc Q.8; Primitive 13.

**Potential constraint violations.** **C3 is the central concern.** Power-law kernels with $\alpha \geq$ some critical value amplify high-frequency contributions and violate UV-FIN. Stage N.3 will evaluate which $\alpha$ values survive.

**Notes.** Catalogue includes power-law for completeness; Stage N.3 will likely restrict to $\alpha$ below a critical threshold. Power-law structure is empirically relevant (e.g., long-range correlations in critical systems) but structurally constrained.

### 5.4 V4 — Multi-scale vacuum memory

**Description.** The vacuum-response kernel decomposes into multiple characteristic scales:
$$
K_\mathrm{vac}(\Delta x) = \sum_i c_i \cdot K_i(\Delta x),
$$
with each $K_i$ having a distinct timescale $\tau_i$. Plausibly a fast scale corresponding to event-discreteness, plus slow scales corresponding to coherent vacuum-mode dynamics.

**Primitive dependencies.** Arc Q.8; Primitive 01; Primitive 13.

**Potential constraint violations.** C3 for any divergent sub-kernel.

**Notes.** Generalisation of V1/V2 to multi-scale structure. Natural for cosmological-scale dynamics where vacuum content involves multiple physical timescales.

### 5.5 V5 — Vacuum-induced cross-chain correlations

**Description.** The effective vacuum mediates correlations between separated chains: two chains coupling to the vacuum at events $x^\mu_1, x^\mu_2$ acquire a correlation
$$
\langle \delta b_{K_1}^\mathrm{env}(x^\mu_1) \cdot \delta b_{K_2}^\mathrm{env}(x^\mu_2) \rangle = K_\mathrm{cross}(x^\mu_1 - x^\mu_2)
$$
with finite-width $K_\mathrm{cross}$ inherited from the underlying vacuum structure.

**Primitive dependencies.** Arc Q.8; Primitive 04; Primitive 10 (multi-chain content); Primitive 13.

**Potential constraint violations.** C1 satisfied if $K_\mathrm{cross}$ depends only on Lorentz-scalar combinations of multi-event coordinates. C2 if $K_\mathrm{cross}$ does not preserve spin-statistics across multi-chain configurations.

**Notes.** The vacuum-mediated analogue of N3-D adjacency-memory; structurally coupled. Provides the substrate for vacuum-mediated forces and long-range correlations.

---

## 6. Summary Table

| ID | Description | Primitive dependencies | Potential constraints to check (N.3) |
|---|---|---|---|
| **N1-A** | Finite-width memory kernels in $b^\mathrm{env}$ | 04, 11, 13 | C1, C3 |
| **N1-B** | History-weighted spectral-rate terms in σ_τ | 04, 06, 11, 13 | C1, C3 |
| **N1-C** | Multi-scale bandwidth memory (fast + slow) | 04, 11, 13 | C2, C3 |
| **N1-D** | Cross-band memory coupling (incl. P↔R) | 04, 07-L1, 11, 13 | **C2 (likely tightly constrained)** |
| **N1-E** | Vacuum-induced bandwidth memory | 04, 11, 13 + Q.8 | Inherits V-sector |
| **N2-A** | Thresholds depending on past event density | 10, 11, 13 | C1, C2 |
| **N2-B** | Hysteresis-style commitment (delayed individuation) | 10, 11, 13 | **C2 (tight: spin-statistics preservation)** |
| **N2-C** | Memory-weighted commitment spacing | 04, 11, 13 | C1, C3 |
| **N2-D** | Multi-chain commitment correlations | 10, 11, 13 | C1, C2, C3 |
| **N2-E** | Vacuum-modulated commitment memory | 10, 11 + Q.8 | Inherits V-sector |
| **N3-A** | Time-lagged adjacency graphs | 10, 11, 13 | C1, C2 |
| **N3-B** | History-dependent adjacency weights | 10, 11, 13, possibly 07-L3 | C3 |
| **N3-C** | Multi-chain (3+) correlation kernels | 10, 11, 13 | C2, C3 |
| **N3-D** | Vacuum-mediated adjacency memory | 10 + Q.8 | Inherits V-sector |
| **N3-E** | Non-local adjacency propagation | 02, 10, 11, 13 | **C1 (central — likely heavily constrained)** |
| **V1** | Finite-width vacuum memory kernel | Q.8, 01, 04, 13 | None obvious; **candidate FORCED** |
| **V2** | Exponential-decay vacuum response | Q.8, 13 | None obvious |
| **V3** | Power-law vacuum response | Q.8, 13 | **C3 (critical exponent restriction)** |
| **V4** | Multi-scale vacuum memory | Q.8, 01, 13 | C3 per sub-kernel |
| **V5** | Vacuum-induced cross-chain correlations | Q.8, 04, 10, 13 | C1, C2 |

### 6.1 Notes on the table

- **Bold C-markers** indicate items where Stage N.3 evaluation is expected to be most consequential — these are the strongest REFUTED candidates.
- **V1 marked as candidate FORCED** — flagged for Stage N.2 evaluation under UV-FIN reasoning.
- **Vacuum-coupled items** (N1-E, N2-E, N3-D) inherit constraints from the V-sector; their final status depends on V-sector resolution.
- **N3-E (non-local adjacency propagation)** is the most aggressive catalogue entry; expected to be heavily constrained by C1 at N.3.

---

## 7. Coverage Assessment

### 7.1 Sectors covered

The catalogue spans four sectors:
- **N1 (bandwidth-memory)**: 5 items.
- **N2 (commitment-memory)**: 5 items.
- **N3 (adjacency-memory)**: 5 items.
- **V (vacuum-response)**: 5 items.

Total: 20 catalogue items.

### 7.2 Sectors not covered (intentional)

The following non-Markovian-adjacent structures are *not* catalogued at this stage:

- **Non-Markovian gauge dynamics**: gauge-field memory kernels (e.g., A_μ with finite-width self-coupling). These are admissible under GRH (Arc Q [3]) but functionally collapse into V-sector vacuum-response and N3-D adjacency-memory; redundant with existing items.
- **Non-Markovian Higgs dynamics**: Higgs-sector memory kernels (e.g., scalar VEV with finite-width response). These are H1/H2-Higgs-mechanism-specific and inherit empirical content; not a separate Arc N category.
- **Anyonic-statistics non-Markovian extensions**: REFUTED structurally by Arc R π_1 = ℤ_2 in 3+1D; not catalogued.

### 7.3 Catalogue completeness

The 20 items represent the systematic enumeration of primitive-level non-Markovian structures consistent with ED Primitives 01–13 + Phase-2 closures. New catalogue items can be added at later stages if structural analysis surfaces additional admissible forms; current coverage is judged adequate for Stage N.2 / N.3 evaluation.

---

## 8. Hand-Off

### 8.1 To Stage N.2 (FORCED evaluation)

Stage N.2 (`non_markov_forced.md`) will evaluate each of the 20 catalogue items for primitive-level FORCED status. The most plausible FORCED candidate is **V1 (finite-width vacuum memory kernel)** under UV-FIN reasoning: a δ-function vacuum response is incompatible with primitive event-discreteness + UV-FIN; some finite-width kernel structure is structurally required.

Secondary FORCED candidates (less plausible, but to be evaluated):
- **N1-E (vacuum-induced bandwidth memory)** if V1 is FORCED — inherits forced status via the vacuum-coupling channel.
- **N2-E (vacuum-modulated commitment memory)** similar to N1-E.

Expected N.2 outcome: 1–3 items FORCED (concentrated in V-sector and vacuum-coupled sub-sectors); 17–19 items ADMISSIBLE-NOT-FORCED.

### 8.2 To Stage N.3 (REFUTED evaluation)

Stage N.3 (`non_markov_refuted.md`) will evaluate items against C1/C2/C3 constraints. Expected REFUTED targets:

- **N3-E (non-local adjacency propagation)** — likely heavily restricted by C1 (Lorentz covariance + locality).
- **N2-B (hysteresis-style commitment)** — possibly REFUTED if delayed individuation violates spin-statistics at finite memory range.
- **N1-D (cross-band Case-P ↔ Case-R coupling)** — possibly REFUTED for restricted statistics-class-mixing forms.
- **V3 (power-law vacuum response)** — REFUTED for $\alpha$ above a critical exponent set by UV-FIN.

Expected N.3 outcome: 2–5 items REFUTED in restricted sub-cases; remainder ADMISSIBLE.

### 8.3 To Stage N.4 (cross-arc implications)

Stage N.4 will evaluate the cross-arc consequences of admissible non-Markovian structures for Arc M σ_τ, Arc Q.5 radiative corrections, Arc Q.6 mixing/CP, and Arc Q.8 vacuum structure. Expected back-flow effects:

- **N1-B (history-weighted spectral-rate terms)** modifies Arc M σ_τ structure but does not change Arc M's H1-dominant verdict (form-FORCED, value-INHERITED preserved).
- **V1 + V2 (vacuum-response kernels)** modify Arc Q.5 vacuum-polarisation analysis but do not violate transversality (gauge-invariance preserved).
- **V5 (vacuum-induced cross-chain correlations)** modifies Arc Q.6 Yukawa-induced phase content; specific values remain INHERITED.

### 8.4 To Stage N.5 (synthesis)

Stage N.5 will integrate N.1 (this memo) + N.2 + N.3 + N.4 into a final Arc N verdict.

---

## 9. Cross-References

- Arc N opening: `arc_n_scoping.md` (N.0).
- Phase-2 closures: `phase2_synthesis.md`, `arc_q_synthesis.md`, `chain_mass_synthesis.md`, `arc_r_stage1_synthesis.md`.
- Memory-kernel precursor: `memory_kernel_derivation.md`.
- Downstream placeholders: `non_markov_forced.md` (N.2), `non_markov_refuted.md` (N.3), `non_markov_implications.md` (N.4), `arc_n_synthesis.md` (N.5).

---

## 10. One-Line Summary

**Stage N.1 catalogues 20 admissible non-Markovian structures across four sectors — N1 bandwidth-memory (5 items: finite-width $b^\mathrm{env}$ kernels, history-weighted spectral-rate, multi-scale, cross-band, vacuum-induced), N2 commitment-memory (5 items: density-dependent thresholds, hysteresis, memory-weighted spacing, multi-chain correlations, vacuum-modulated), N3 adjacency-memory (5 items: time-lagged graphs, history-weighted adjacency weights, multi-chain correlations, vacuum-mediated, non-local propagation), V vacuum-response (5 items: finite-width kernels, exponential decay, power-law, multi-scale, cross-chain) — each characterised by primitive dependencies and potential constraint violations (C1 Lorentz, C2 spin-statistics, C3 UV-FIN), with V1 (finite-width vacuum memory kernel) flagged as the most plausible FORCED candidate under UV-FIN reasoning, N3-E (non-local adjacency propagation) flagged as the strongest REFUTED candidate under C1 reasoning, and the catalogue handed off to Stage N.2 for FORCED evaluation, Stage N.3 for REFUTED evaluation, and Stages N.4/N.5 for cross-arc implications and synthesis.**
