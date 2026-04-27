# MCD.1 — Candidate Action Functionals for Path-of-Easiest-Updating

**Date:** 2026-04-27
**Arc:** Many-Chain Dynamics — second memo (action-functional survey)
**Status:** Six candidate readings (A1–A6) of the path-of-easiest-updating principle defined and evaluated against five structural criteria. **A1 (cost minimization with U = 1 − T) and A5 (geodesic on slow-time metric) are mathematically unified at the single-chain level; both reduce to GR's geodesic principle in slow-time language.** This is structurally clean but raises an honest concern: at the *single-chain* level, the path-of-easiest-updating principle is GR's geodesic principle in different vocabulary, with no new content. **The genuine novelty of MCD must therefore live entirely in the many-chain extension** — specifically, in whether the field equation that determines T from many-chain configurations differs structurally from Einstein's equation. **A4 (general ED-native Lagrangian) provides the framework for the many-chain extension** but does not itself select a specific Lagrangian. **A2 (curvature/gradient minimization) is restrictive but locally consistent. A3 (entropy maximization) is speculative; it requires a substrate-level entropy construction not articulated in ED-07. A6 (hybrids) are open-ended.** **Recommended for MCD.2 derivation: A1+A5 unified as the single-chain principle, with A4 as the framework for many-chain extension.** The arc's prospects depend on whether the many-chain extension produces a non-Einstein nonlinear field equation.
**Predecessor:** MCD.0 (scoping); ED-07 §5.1 (principle of least disruption); GR-3A (eikonal-limit geodesic worldlines).
**Successor:** MCD.2 (Euler-Lagrange-like derivation for the surviving candidate).

---

## 1. The candidates, defined precisely

Each candidate provides a mathematical interpretation of ED-07's qualitative principle: "A system tends to follow the path that minimizes disruption to its internal pattern of becoming." The candidates differ in what functional is extremized and over what variables.

### 1.1 A1 — Minimization of total update cost along a chain

For a chain γ parameterized by τ:

> S[γ] = ∫_γ U(ρ, ∇ρ, T, ∇T, ...) dτ.

Inertial path = arg min S over admissible paths between two endpoints. The integrand `U` is a local "update cost density" expressing how much substrate effort the chain expends per step.

**Concrete sub-candidates for U:**

| Sub-candidate | U | Physical reading |
|---|---|---|
| A1.a | `U = ρ` | High-ρ regions are expensive; chains drift toward low-ρ |
| A1.b | `U = 1/ρ` | Low-ρ regions are expensive; chains drift toward high-ρ |
| A1.c | `U = 1 − T` | Proper-time-like; **matches GR action for free particle** |
| A1.d | `U = |∇T|` | Gradient avoidance; matches ED-07 §5.1 first criterion |
| A1.e | `U = |∇ρ|/ρ` | Relative-gradient cost (scale-invariant) |

**A1.c is structurally privileged.** In GR, the free-particle action is `S = -mc² ∫ dτ_proper`. With slow-time `dτ_proper / dt = √(1 - 2T) ≈ 1 - T`, this gives `S = -mc² ∫ (1 - T) dt`, which is exactly A1.c (up to overall sign and normalization). **Extremization of A1.c over chain paths yields the geodesic equation in the slow-time metric.** This is the GR-3A result re-expressed in MCD vocabulary.

### 1.2 A2 — Minimization of curvature or temporal-tension gradients

> S[γ] = ∫_γ |κ_γ|² dτ    or    S[γ] = ∫_γ |∇T|² dτ    (along the path).

Inertial path minimizes integrated path-curvature, or equivalently the integrated strength of the T-gradient encountered. In flat ED (uniform ρ, ∇T = 0), straight lines are extremal. In non-uniform ED, paths curve to minimize accumulated curvature.

This is more *geometric* than A1: it asks the chain to keep its trajectory smooth, not to minimize a cost-per-step. It does not have a direct GR analogue (the standard GR action does not penalize squared curvature). It is closer to certain higher-derivative gravity theories (e.g., Gauss-Bonnet corrections) than to standard GR.

### 1.3 A3 — Maximization of updating freedom (entropy-like)

> S[γ] = ∫_γ H(ρ, ∇ρ, T, ...) dτ,    inertial path = arg max S.

Where `H` is an entropy-like functional measuring "how many ways the substrate can update at each point." The chain follows paths that preserve maximum updating-flexibility. Possible forms:

- `H = ln ρ` (information-theoretic, Boltzmann-like)
- `H = T · ln T − T` (thermodynamic free-energy-like)
- `H = -ρ · ln ρ` (Gibbs entropy)

**Status caveat.** ED-07 does not explicitly articulate an entropy principle. A3 would require an additional substrate-level commitment about what entropy means in ED's micro-event ontology. The reading is structurally interesting (statistical-mechanics derivations of action principles are well-established) but introduces machinery that is not yet in the ED canon.

### 1.4 A4 — Extremization of an ED-native action

> S = ∫ L(ρ, T, χ_chain, ∇ρ, ∇T, ∂_τ χ_chain, ...) d⁴x.

Where `χ_chain` is the chain's internal-state coordinate and the integration is over spacetime (not just along the chain's path). This is the field-theoretic action: chains and fields jointly described by a single Lagrangian density `L`.

A4 is a *framework*, not a specific candidate. It contains A1 (with `L` reducing to `U · δ(γ)` for a path-localized chain) and A5 (with `L` containing a metric kinetic term) as special cases. The Lagrangian `L` must be specified before A4 produces concrete predictions.

A4's strength: maximum flexibility for accommodating ED primitives in any combination.
A4's weakness: maximum underdetermination — many possible Lagrangians, requiring further structural commitments to select.

### 1.5 A5 — Geodesic-like updating in slow-time metric

> Inertial path = geodesic of metric `g_μν(T, ∇T)`.

The ED slow-time field T defines (or is associated with) a Lorentzian metric `g_μν` on spacetime, and chains follow geodesics of that metric. Concretely:

> g_00 = −(1 − 2T),     g_ij = (1 + 2T) δ_ij    (weak-field, slow-time)

This is the standard GR weak-field metric with T playing the role of `Φ_GR / c²`. The geodesic equation `d²x^μ/dτ² + Γ^μ_νρ · (dx^ν/dτ) · (dx^ρ/dτ) = 0` describes inertial motion.

**A5 is unified with A1.c** at the single-chain level: extremizing `∫(1 − T) dt` over chain paths produces the geodesic equation of the metric defined above (this is the standard GR derivation of geodesics from the proper-time-action principle). A1.c and A5 are the *same* principle in different vocabularies.

### 1.6 A6 — Hybrid principles

Combinations of A1–A5. Examples:

- **Cost-entropy:** `S = ∫(U − T_param · H) dτ` where `T_param` is a temperature-like parameter. Reduces to A1 at low T_param, to A3 at high T_param.
- **Curvature-entropy:** minimize curvature (A2) subject to entropy bound (A3).
- **Quantum action:** `S_total = S_classical + (ℏ/2π) · S_information` — adds a quantum correction proportional to information-theoretic entropy.

These are interesting but less canonical than A1–A5. They emerge naturally in specific limits (e.g., classical mechanics + quantum corrections) but require additional substrate assumptions to ground.

---

## 2. Structural criteria

Each candidate is evaluated against five criteria.

### 2.1 C1 — Compatibility with ED primitives

The functional is built from ρ, T, ∇ρ, ∇T, chain coordinates χ, and existing ED constants (D_T, λ, c, κ_act). No new fundamental fields or constants.

### 2.2 C2 — Dimensional consistency

The functional has well-defined units expressible in existing ED dimensions. If new constants are needed, they are derivable from existing ones (e.g., the Einstein-like `D_T = c² · κ_act` relation if it holds).

### 2.3 C3 — Locality

The integrand depends only on local fields and their derivatives at the integration point. The principle does not require global knowledge of the chain's full path or of distant field values to evaluate the local cost-density.

### 2.4 C4 — Many-chain extensibility

The principle generalizes from single-chain to many-chain regimes naturally — each chain extremizes its own functional, with coupling entering through fields (ρ, T) that all chains share.

### 2.5 C5 — Potential to generate nonlinear continuum limits

When the many-chain dynamics is coarse-grained to a continuum field equation for T, the resulting equation can be nonlinear in T or in its sources. This is the structural escape route from the DM-arc linearity wall.

---

## 3. Evaluation by candidate

### 3.1 A1 (cost minimization)

| Criterion | Status |
|---|---|
| C1 (ED compatibility) | **High** for A1.c (U = 1 − T uses only T); high for A1.a, A1.b, A1.d, A1.e |
| C2 (dimensional) | **Clean** for A1.c (T dimensionless); other sub-candidates may need normalization constants |
| C3 (locality) | **Local integrand**; path-integral is global but Euler-Lagrange equations are local |
| C4 (many-chain) | **Direct**: each chain extremizes its own ∫U dτ; coupling through T which all chains share |
| C5 (nonlinearity) | **Conditional**: depends on how T is determined from chain configurations. Linear if T satisfies linear PDE with chain-source; nonlinear if T's source structure has self-consistency that produces nonlinearity in the continuum limit |

**A1.c is structurally privileged** as the GR-equivalent reading. **A1.d is structurally consistent with ED-07 §5.1's first criterion** ("ED gradient along the path is minimal") and may be more directly motivated from ED-07 than A1.c, but produces different equations of motion. A1.a and A1.b have the wrong sign or wrong directionality compared to ED-07's qualitative criteria.

### 3.2 A2 (curvature/gradient minimization)

| Criterion | Status |
|---|---|
| C1 (ED compatibility) | **Medium**: |∇T|² uses T's gradient, OK; |κ|² uses path geometry, OK but indirect |
| C2 (dimensional) | **Clean** |
| C3 (locality) | **Local** (κ depends on local path geometry; ∇T is local) |
| C4 (many-chain) | **Direct**: similar to A1 |
| C5 (nonlinearity) | **Limited**: A2's higher-derivative structure typically gives higher-order *linear* equations of motion (the linearized Gauss-Bonnet term is linear). Genuine nonlinearity is harder to engineer here |

A2 is locally consistent but does not have an obvious GR or MOND analogue. The motivation from ED-07 is real (§5.1 first criterion mentions gradient minimization) but A1.d captures that more directly.

### 3.3 A3 (entropy maximization)

| Criterion | Status |
|---|---|
| C1 (ED compatibility) | **Low**: ED-07 does not articulate an entropy principle. A3 requires importing thermodynamic / information-theoretic machinery not yet in the ED canon |
| C2 (dimensional) | **Variable**: depends on the choice of H functional; some choices clean, others require new constants |
| C3 (locality) | **Variable**: local for H built from local fields; nonlocal for global entropy constraints |
| C4 (many-chain) | **High**: statistical mechanics is naturally many-chain |
| C5 (nonlinearity) | **High potential**: entropy-based field equations are often inherently nonlinear (e.g., Boltzmann-like). The deep-MOND limit has been derived from entropy principles in some emergent-gravity proposals (Verlinde 2016) |

A3 is the most theoretically interesting from a "produce nonlinearity automatically" standpoint, but the most expensive in terms of new substrate commitments. **It cannot be carried forward without ED-07-level articulation of what entropy means in ED's micro-event ontology.** This is a separable foundational question (a "Phase-2"-flavor task), not a within-MCD task.

### 3.4 A4 (ED-native Lagrangian framework)

| Criterion | Status |
|---|---|
| C1 (ED compatibility) | **High**: standard Lagrangian field theory ported to ED primitives |
| C2 (dimensional) | **Clean** with appropriate Lagrangian construction |
| C3 (locality) | **Local** (standard Lagrangian density) |
| C4 (many-chain) | **Direct**: each chain contributes its own term; field terms produce coupling |
| C5 (nonlinearity) | **Tunable**: A4 admits both linear (free-field + linear coupling) and nonlinear (interaction terms) Lagrangians |

A4 is the **framework** for MCD.2's derivation. It does not select a specific Lagrangian; that selection is what MCD.2 must do, taking input from A1+A5 as the single-chain term and constructing field terms for T's dynamics.

### 3.5 A5 (geodesic on slow-time metric)

| Criterion | Status |
|---|---|
| C1 (ED compatibility) | **High**: T is in the canon; the slow-time metric is the standard weak-field GR metric in ED's variables |
| C2 (dimensional) | **Clean** |
| C3 (locality) | **Local** (geodesic equation is local) |
| C4 (many-chain) | **Through metric**: each chain follows its own geodesic; metric is determined by all chains' contributions to T (through some field equation) |
| C5 (nonlinearity) | **Natural** if the field equation for T is nonlinear (matches Einstein's nonlinear field equation in the GR analogy) |

**A5 is unified with A1.c** at the single-chain level. A5's value over A1.c is conceptual: it makes the GR-analogy explicit and the geodesic structure manifest. A5's structural test is whether the field equation determining T from matter has the right form to escape the DM-arc linearity wall. **In standard GR, this equation is Einstein's, which is nonlinear.** Whether ED's substrate physics produces an Einstein-equation analog or something different is the central open question.

### 3.6 A6 (hybrids)

| Criterion | Status |
|---|---|
| C1 (ED compatibility) | **Variable**: depends on hybrid form |
| C2 (dimensional) | **Variable**: often introduces new parameters (e.g., temperature for cost-entropy) |
| C3 (locality) | **Variable** |
| C4 (many-chain) | **Variable** |
| C5 (nonlinearity) | **High potential**, especially for entropy-containing hybrids |

A6 is open-ended. Specific hybrids may be valuable in specific limits (e.g., quantum corrections to classical action) but cannot be evaluated as a class.

---

## 4. Comparison table

| Candidate | C1: ED-compat | C2: Dim | C3: Local | C4: Many-chain | C5: Nonlinearity | Notes |
|---|---|---|---|---|---|---|
| **A1.c** (U = 1 − T) | High | Clean | Local | Direct | Conditional | **GR-equivalent at single-chain level** |
| A1.d (U = \|∇T\|) | High | Clean | Local | Direct | Conditional | Most directly matches ED-07 §5.1 |
| A1.a/b/e | Medium-High | Variable | Local | Direct | Conditional | Less canonical |
| A2 (curvature) | Medium | Clean | Local | Direct | **Limited** | Higher-derivative; linear EOM |
| A3 (entropy) | **Low** | Variable | Variable | High | **High potential** | Requires new substrate commitment |
| A4 (Lagrangian) | High | Clean | Local | Direct | **Tunable** | Framework, not a specific candidate |
| **A5** (geodesic) | High | Clean | Local | Through metric | **Natural** | **Unified with A1.c** |
| A6 (hybrids) | Variable | Variable | Variable | Variable | High | Open-ended |

---

## 5. Survivors

Strict reading of the criteria:

- **A1.c + A5 (unified)** is the cleanest *single-chain* reading. Carries forward as the equation-of-motion candidate for MCD.2.
- **A4** is the *framework* in which A1.c+A5 is embedded for many-chain extension. Carries forward as the Lagrangian-construction container.
- **A1.d** is a structurally distinct alternative most directly motivated by ED-07 §5.1. Carries forward as a sanity check (A1.d should agree with A1.c+A5 in the appropriate limit; if it doesn't, that's a structural problem).
- **A2, A3, A6**: not advanced.
  - A2 fails C5 (nonlinearity is hard to engineer from higher-derivative gravity at the linearized level).
  - A3 fails C1 (requires substrate-level entropy commitment not in ED-07).
  - A6 is too open-ended; specific hybrids may be reconsidered if A1+A5 fails.

---

## 6. Honest discussion

### 6.1 The single-chain trivialization

**A1.c + A5 unified is, at the single-chain level, just GR's geodesic principle in slow-time vocabulary.** This is structurally clean — it shows the path-of-easiest-updating principle is consistent with established GR phenomenology — but it raises an honest concern: at single-chain scale, MCD adds no new physics over GR. The principle of least disruption, formalized this way, IS the principle of extremal proper time.

**This is acceptable for the eikonal regime** (matches GR-3A, which is itself FORCED-conditional in the project memory) but means MCD's contribution must come entirely from **the many-chain extension**. The arc's success or failure depends on whether the field equation for T (which determines the metric and hence the geodesic structure) differs from Einstein's equation in a structurally important way.

### 6.2 The three structural possibilities for many-chain

There are three plausible outcomes for the many-chain field equation:

- **(i) MCD reproduces Einstein's equation exactly.** The path-of-easiest-updating principle, extended to many chains, gives standard GR with T playing the role of the metric perturbation. ED gains an ontologically transparent account of GR but no new gravitational physics; BTFR remains an empirical mystery (since GR doesn't derive BTFR either; ΛCDM uses dark matter halos to fit it).

- **(ii) MCD produces a non-Einstein nonlinear field equation that includes MOND-like deep-regime behavior.** This is the success scenario. The many-chain extension produces nonlinearity of the right form to derive slope-4 BTFR naturally, while reducing to Einstein in the strong-field / dense-bundle limit.

- **(iii) MCD produces a linear field equation (DM-arc linearity wall reappears).** The many-chain coupling is mean-field-like and additive. The continuum limit is the canonical screened-Poisson with kinematic source. C2 fails by inner-disc dominance, slope-2 BTFR. **The arc fails the same way DM.0/1/G failed.**

**MCD.3 is the pivot point** that determines which outcome obtains.

### 6.3 Most promising path to nonlinearity

The most likely route to outcome (ii) is through the **self-consistency** of how chains define and respond to the metric:

- Each chain's energy-momentum (or ED contribution) sources the metric.
- The metric determines each chain's geodesic.
- The geodesics determine where the chain's energy-momentum is concentrated.
- This closure can be nonlinear in the metric.

In Einstein's equation `G_μν = 8πG T_μν^matter`, the nonlinearity comes from `G_μν` being nonlinear in `g_μν` (via the Christoffel symbols). The chain-derived field equation in ED would have an analogous nonlinearity if the substrate physics correctly produces an Einstein-tensor-like operator.

Whether ED's substrate produces an Einstein-tensor or some structurally distinct operator (perhaps producing MOND-like deep-regime behavior automatically) is the central question for MCD.3.

### 6.4 The ED-Lagrangian construction for MCD.2

For MCD.2 to derive Euler-Lagrange equations, we need an explicit Lagrangian density. The natural construction combines:

> **L = L_chain + L_field + L_coupling**

with:

- **L_chain = -mc²·(1 - T)** for a chain at position γ(τ) in slow-time T (this gives A1.c on extremization, equivalent to A5).
- **L_field = (1/2) · (∇T)² - V(T)** for some potential V (analogous to scalar-field Lagrangian; the screening rate λ corresponds to V'(T) at small T).
- **L_coupling = -κ_act · A(γ, T)** for the chain-T coupling (this is the source term of the canonical-ED PDE in Lagrangian form).

Variation with respect to γ gives the chain equation of motion (recovers A1.c geodesic). Variation with respect to T gives the field equation. **Whether the field equation is linear or nonlinear depends on V(T) and on how A couples chains to T.** The DM-arc treated this as linear; MCD.3 must determine whether ED's substrate physics actually allows a nonlinear coupling.

**This is the structural payoff of A4 as a framework**: it makes explicit that the Lagrangian construction has multiple terms, and the question of whether emergent gravity is nonlinear reduces to the structure of the coupling term `L_coupling`.

---

## 7. Implications for MCD.2

MCD.2 should derive the Euler-Lagrange-like equations for the **A1.c + A5 unified single-chain principle**, embedded in the **A4 Lagrangian framework**. Specifically:

- **For the chain:** vary L = -mc²·(1 - T) along γ(τ) to obtain the geodesic equation in the slow-time metric. This recovers GR-3A's eikonal-limit geodesic worldline.
- **For the field T:** vary L_field + L_coupling to obtain the field equation for T. **This is where the linear-vs-nonlinear question is decided.**

The MCD.2 derivation is structurally lean: standard variational calculus applied to ED-native fields. The mathematical content is established; the structural content (what V and L_coupling look like) is what MCD.2 must specify.

**A1.d as a sanity check:** an alternative principle that minimizes ∫|∇T| should give equations of motion that *agree with A1.c in the eikonal limit* (since both reduce to GR-3A's geodesic) but may differ in non-eikonal regimes. If A1.d gives a different prediction in an empirically-relevant regime, that's a structural disagreement worth diagnosing.

---

## 8. Recommended Next Steps

Three concrete next steps:

1. **MCD.2: Derive Euler-Lagrange equations for A1.c + A5 unified.** Apply standard variational calculus to the ED-Lagrangian construction `L = L_chain + L_field + L_coupling`. Output: chain-trajectory equation (should match GR-3A geodesic in eikonal limit) and field equation for T. **Most importantly, identify whether the field equation is linear or nonlinear in T, and characterize the form of any nonlinearity.** This is the structural pivot — if linear, the DM-arc wall reappears; if nonlinear, MCD.3 has something to work with. **Recommended as immediate next step.**

2. **Read the existing AD evaluation of Event Density** before MCD.2, as recommended in MCD.0 §9. The AD evaluation may already have established constraints on what kinds of Lagrangian constructions are consistent with ED's existing architecture. If certain Lagrangian forms are AD-disqualified, MCD.2 should know that up front.

3. **Hold A3 (entropy maximization) in reserve as a foundational follow-up.** A3 has high nonlinearity potential but requires substrate-level commitments not currently in ED-07. If MCD.2/.3 succeeds with A1+A5+A4, A3 becomes a *separate* foundational question (does ED have a natural entropy structure?) rather than a competing path. If MCD.2/.3 fails (linear-PDE result), A3 becomes a candidate revival route — but only after explicit foundational work to establish the entropy primitive in ED.

The MCD arc's success or failure now hinges on MCD.2's field-equation derivation. **The single-chain principle is structurally trivial (it's GR);** **the genuine novelty must come from how the field is sourced in many-chain regimes.** MCD.2 sets up the question; MCD.3 answers it.

Status: complete.
