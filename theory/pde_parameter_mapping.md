# PDE-Parameter Mapping Memo

**Date:** 2026-04-24
**Location:** `quantum/effective_theory/pde_parameter_mapping.md`
**Status:** First-pass mapping memo. Addresses Fix 1 from `quantum/primitives/TIGHTENING_PASS_01.md` §7.
**Purpose:** Establish the correspondence between the canonical ED PDE parameters (`D, H, ζ, τ, M(ρ), P(ρ), v`) and the primitive-level objects established in `quantum/primitives/01–13`. Each mapping is classified as **FORCED** (required by existing ED theory or simulator behavior), **CANDIDATE** (defensible from the primitives but not uniquely forced), or **SPECULATIVE** (plausible but requiring Phase 2 derivation).
**Not in scope:** deriving any of the candidate/speculative mappings, executing the Path B / Path C / Phase 4 work, or modifying the primitive files themselves. This memo is the interface document, not the derivation.

---

## 1. The canonical ED PDE

From `theory/D_crit_Resolution_Memo.md §2` and the Dimensional Atlas, the canonical two-channel ED PDE is:

```
∂_t ρ = D · F[ρ] + H · v                     (1a)
∂_t v = (F[ρ] − ζ · v) / τ                   (1b)
F[ρ] = M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ)       (2)
D + H = 1,  D, H ∈ [0, 1]                    (3)
```

With constitutive choices (canon):

- **Mobility:** `M(ρ) = M₀ · (ρ_max − ρ̂)^β`, with `M(ρ*) = M₀ > 0`, `M(ρ_max) = 0` (Canon P4), canonical `β = 2`.
- **Penalty:** `P(ρ)` with `P(ρ*) = 0` (Canon P3), `P'(ρ*) = P₀ > 0`; leading-order expansion `P(ρ) ≈ P₀ · (ρ − ρ*)`.
- **Canon defaults:** `D = 0.3` (convention), `ζ = 0.25` (convention), `τ = 1` (convention), `H = 5` in some memos as external-coupling amplitude.

Seven distinct objects need mapping: `D`, `H`, `ζ`, `τ`, `M(ρ)` with `M₀`, `P(ρ)` with `P₀`, and the field `v(x, t)`.

---

## 2. Mapping summary table

| PDE object | Primitive-level correspondent | Status | Notes |
|---|---|---|---|
| `ρ(x, t)` | ED scalar count-density (Primitive 05) | **FORCED** | Identification per 05 §1–§2; Madelung-anchored to \|ψ\|² in quantum regime via Dimensional Atlas |
| `D` | `Σ b_K² / (Σ b_K)²` — inverse effective multiplicity (Primitives 04 + 08) | **CANDIDATE** | Participation-ratio form; unifies the three drift cases in tightening pass §3.1 |
| `H = 1 − D` | participation-channel weight | **FORCED given D** | Arithmetic identity from (3) |
| `ζ` | dissipation rate of commitment-reserve bandwidth into environmental bandwidth (Primitives 04 + 11) | **SPECULATIVE** | No primitive explicitly defines this rate; most defensible near-term mapping |
| `τ` | participation-bandwidth relaxation timescale against local flow (Primitives 04 + 13) | **CANDIDATE** | In quantum regime, anchored to Compton time via Dimensional Atlas (**FORCED at that anchoring**) |
| `M₀` | bandwidth-weighted gradient response rate at equilibrium ρ* (Primitives 04 + 06) | **SPECULATIVE** | Constitutive form `(1 − ρ̂)^β` is structural; β = 2 is canonical constitutive choice |
| `P₀` | polarity-alignment restoring rate at equilibrium ρ* (Primitives 06 + 09) | **SPECULATIVE** | Linear-order penalty as tension-polarity-restoration tendency |
| `v(x, t)` | polarity-weighted commitment-rate density (Primitives 09 + 11 + 13) | **SPECULATIVE** | Three candidates exist; this is the most defensible given the PDE's driving / damping structure |

The table is the minimum interface. §3–§8 derive each entry.

---

## 3. FORCED mappings

### 3.1 ρ ↔ ED scalar count-density (Primitive 05)

**Status: FORCED.**

Primitive 05 §1 establishes `ED(R) = |V ∩ R|` at the discrete graph level and `ρ(x) = dED/dV` in the continuum. The ED PDE's ρ is the coarse-grained continuum version of this count. The dual identity under the Dimensional Atlas's quantum-regime anchoring — ρ ↔ |ψ|² via Madelung's theorem — is an FORCED identification within that regime, because Madelung is a mathematical theorem about the free-particle Schrödinger equation (Primitive 05 §7 open question #5 previously flagged this; resolved here).

**No alternative is defensible.** Any other candidate for ρ (e.g., energy density, matter density, number density) is a derived quantity that presupposes this primary identification.

**Amendment required:** Primitive 05 §2 should add one sentence explicitly stating the dual identity (discrete count / quantum-regime |ψ|²). This is on the Fix-2 / Fix-4 list of the tightening pass.

### 3.2 H = 1 − D

**Status: FORCED.**

Arithmetic consequence of (3). The primitive-level interpretation is: `D` is the fraction of `F[ρ]` that advances ρ directly (pure diffusion-channel); `H` is the fraction that advances ρ via the participation channel (through v). The two must sum to 1 because `F[ρ]` is a single quantity being apportioned.

**Primitive-level reading:** `D` is the fraction of `F[ρ]` that commits via the dominant single channel; `H` is the fraction that commits via multi-channel participation coupling. This follows from the D mapping in §4.1.

### 3.3 τ in quantum regime ↔ Compton time

**Status: FORCED within the quantum regime only.**

The Dimensional Atlas (`ED-Dimensional-01_Quantum_Regime.md §2.4`) anchors `T_0 = 2 D_nd ℏ / (mc²)`. For `D_nd = 0.3`, `T_0 = 0.6 · ℏ/(mc²)`. This is a forced anchoring because it follows from `L_0 = ℏ/(mc)` (Compton length), `D_phys = ℏ/(2m)` (Madelung-exact), and `T_0 = L_0² D_nd / D_phys` (nondimensionalization).

In other regimes (Planck, condensed matter, galactic, cosmological — see `ED-Dimensional-01 §9`), `T_0` is anchored differently. The regime-free primitive-level reading of τ is developed in §4.3 below.

---

## 4. CANDIDATE mappings

### 4.1 D ↔ Σ b² / (Σ b)² — the participation-ratio form (Primitives 04 + 08)

**Status: CANDIDATE.**

**Proposal.** At each position x along a chain's trajectory, enumerate the channels K available of the relevant rule-type τ. For each channel, let `b_K(x)` be the bandwidth in that channel (Primitive 04). Define:

```
M_eff(x) = (Σ_K b_K)² / Σ_K b_K²                (4)
D(x) = 1 / M_eff(x) = Σ_K b_K² / (Σ_K b_K)²     (5)
```

This is the participation-ratio form, standard in statistical physics for measuring how concentrated a distribution is into few vs. many modes.

**Properties:**

- `D = 1` when bandwidth is in a single channel (committed regime).
- `D = 1/N` when bandwidth is equidistributed across N channels (maximally thin regime).
- `D = 0.5` when `M_eff = 2` — two effective channels competing.
- Monotonic: concentrating bandwidth into fewer channels always raises D.

**Why CANDIDATE not FORCED:**

The Q-C Boundary paper uses `D` as "effective channel weight" without specifying a functional form. Three functional forms were present in the primitive stack (tightening pass §3.1):

- Primitive 04 §6: `D = b_dominant / b_total` (simple ratio)
- Primitive 07 §6: "channel-dominance variable" (qualitative)
- Primitive 08 §2: `D ≈ 1/M_eff` via participation ratio (5)

Committing to (5) unifies all three at the order-of-magnitude level and matches the intuition of 04 and 07 in limiting cases. But the specific functional choice is not forced by any existing derivation. A different smooth interpolation between `D → 1` (single-channel) and `D → 1/N` (equidistributed) could in principle be defended.

**Effect on D_crit:**

The D_crit resolution memo gives `D_crit(ζ) = √(2−ζ)(2−√(2−ζ))` at reference mode `ε_k · τ = 1`, which at canon-default `ζ = 1/4` yields `D_crit ≈ 0.896`. In the participation-ratio interpretation (5), this corresponds to `M_eff(x_c) ≈ 1.116`, i.e., near-single-channel dominance with only minor contribution from secondary channels. This is a more stringent transition condition than `D = 0.5` (corresponding to `M_eff = 2`) suggested.

**Amendments required:** Primitive 04 §6 formula and Primitive 07 §6 description should be amended to reference (5). Primitive 08 §2 is already consistent. See tightening pass Fix 2.

### 4.2 H ↔ participation-channel weight via D's complement

**Status: CANDIDATE (inherited from D).**

Given (5):

```
H(x) = 1 − D(x) = 1 − Σ b_K² / (Σ b_K)²         (6)
     = [(Σ b_K)² − Σ b_K²] / (Σ b_K)²
     = 2 Σ_{K < K'} b_K · b_{K'} / (Σ b_K)²     (7)
```

Equation (7) has a clean primitive-level reading: **H is the normalized sum of cross-channel bandwidth products.** When only one channel carries bandwidth, all cross products vanish and H = 0. When bandwidth is equidistributed, cross products are maximal and H → 1 − 1/N.

**Primitive-level content:** H measures how much of the bandwidth is in cross-channel coherence (interference-capable structure) rather than in isolated single-channel commitment. This matches the PDE role of H as "the fraction of F[ρ] that advances via participation coupling."

### 4.3 τ ↔ participation-bandwidth relaxation timescale (Primitives 04 + 13)

**Status: CANDIDATE; FORCED within the quantum regime via §3.3.**

**Proposal.** τ is the characteristic timescale over which a chain's participation bandwidth distribution relaxes toward the distribution demanded by the local flow. More precisely: given a chain whose current bandwidth distribution `{b_K(t)}` departs from the flow-aligned distribution `{b_K^eq(x)}`, τ is the e-folding time for `(b_K − b_K^eq)` to decay.

In the primitive stack, this is the commitment-rate-regulated rhythm (Primitive 11 rate + Primitive 13 relational-timing coupling to the local flow).

**Why CANDIDATE not FORCED:**

Three candidates exist for τ's primitive-level identification:

- **(a)** Chain internal rule-period (Primitive 02 update cycle)
- **(b)** Commitment-event rate inverse: `τ = 1 / Γ_commit` (Primitive 11)
- **(c)** Participation-bandwidth relaxation timescale (combining 04 + 13)

(a) is too narrow — it conflates chain-identity cycle with participation relaxation. (b) is too broad — commitment events happen for many reasons, not all of which are participation-relaxation-driven. (c) is the cleanest match to the PDE's role of τ in (1b): v relaxes toward F[ρ] at rate 1/τ, and the primitive-level relaxation of bandwidth distribution toward flow-equilibrium is the natural candidate.

**Under the quantum-regime anchoring (§3.3), all three candidates collapse to Compton time up to order-unity factors.** The distinction matters more in non-quantum regimes.

---

## 5. SPECULATIVE mappings

These are the load-bearing unknowns. Each requires Phase 2 derivation; each is the most defensible near-term candidate given the primitive stack as it stands.

### 5.1 ζ ↔ dissipation rate of commitment-reserve bandwidth into environment (Primitives 04 + 11)

**Status: SPECULATIVE.**

**Proposal.** ζ is the dimensionless rate at which commitment-reserve bandwidth `b_com` (Primitive 04's four-band structure) leaks into environmental bandwidth `b_env` per unit τ. Formally:

```
ζ = τ · (db_env/dt)_{commit-driven} / b_com       (8)
```

**Physical content:** each commitment event (Primitive 11) consumes commitment-reserve bandwidth and adds a new micro-event. A fraction of the reserve bandwidth ends up locally concentrated in the new commit (which raises thickening, Primitive 12); the remainder disperses into environmental bandwidth. ζ is the rate of that dispersion.

**Connection to decoherence:** in the standard Hornberger-Joos-Zeh framework, environmental decoherence occurs at rate Λ set by gas-collision, thermal-photon, and internal-state thermalization processes. In ED terms, each of these is a specific channel through which commitment-reserve bandwidth is being lost to modes the chain cannot retain. ζ · Λ^{−1} should recover a universal structural constant if this identification is correct.

**Why SPECULATIVE:**

- No primitive explicitly defines the rate in (8). Primitive 04's four-band structure is a partition, not a dynamical equation; the rate of flux between bands is not specified at the primitive level.
- The ζ-canonical-default 0.25 is a convention; no primitive-level argument derives it.
- The D_crit(ζ) formula's ζ could equally be interpreted as an internal-relaxation rate, a measurement-bandwidth rate, or a polarity-realignment rate. Commitment-reserve-dissipation is the best fit to the PDE's role of ζ in (1b) but not the only one.

**What would promote this to CANDIDATE:** an explicit primitive-level equation relating commitment-reserve dissipation rate to the four-band partition dynamics. This is a Phase 2 derivation target.

### 5.2 M₀ ↔ bandwidth-weighted gradient response rate at equilibrium (Primitives 04 + 06)

**Status: SPECULATIVE.**

**Proposal.** M₀ is the rate at which the local bandwidth-weighted gradient `b^{ij} ∂_j ρ` drives ρ-flow at equilibrium density ρ*. In the PDE, this is the prefactor of `∇²ρ` in the mobility term. At the primitive level, it is the local response coefficient of the ED field to the bandwidth-weighted Laplacian — i.e., how efficiently bandwidth-structure transmits ρ-gradients at equilibrium.

**Density-dependent mobility** `M(ρ) = M₀ (1 − ρ̂)^β` has the property `M(ρ_max) = 0` (Canon P4 saturation). The primitive-level reading: at saturation, the bandwidth kernel `b^{ij}` loses its gradient-transmitting property. This is the ED-specific prediction: probability-density diffusion slows as the density approaches the normalization bound (Dimensional Atlas §6.4 flags this as "ED's strongest prediction or weakest link").

**Constitutive exponent β = 2** is canonical. Primitive-level: the bandwidth kernel's gradient-transmission efficiency falls as the square of the saturation margin. This is a constitutive choice, not a derived quantity.

**Why SPECULATIVE:**

- No primitive derives the specific form `(1 − ρ̂)^β`. Primitive 05 §1 mentions saturation as changing "update behavior," but does not specify the functional form of the change.
- β = 2 is the canonical choice; β = 1 (linear suppression) or β = 3 (cubic) would also be primitive-compatible and would reduce to different PME equations.
- M₀'s absolute magnitude is not pinned down at the primitive level; the Dimensional Atlas fixes it via `M_{0,phys} = M_0 · D_phys / D_nd` in the quantum regime (anchored to Compton scales), but this is a regime-specific anchoring, not a primitive-level identification.

### 5.3 P₀ ↔ polarity-alignment restoring rate at equilibrium (Primitives 06 + 09)

**Status: SPECULATIVE.**

**Proposal.** P₀ is the rate at which departures of ρ from equilibrium ρ* are penalized, reflecting the local tension-polarity (Primitive 09) restoring tendency. A chain at ρ > ρ* has its rule-phase stressed relative to the local flow direction; P₀ is the rate at which this stress drives ρ back toward ρ*.

Linear-order expansion `P(ρ) ≈ P₀ (ρ − ρ*)` gives an RC-decay timescale `τ_RC = 1/(D · P₀)` for probability-density perturbations (Dimensional Atlas §7.1). In quantum regime, this is ~10⁻²¹ s — sub-femtosecond, comparable to electronic relaxation timescales.

**Primitive-level content:** P₀ is the *polarity-restoration rate coefficient*. At ρ*, chains are in the polarity-neutral state relative to local flow; deviations ρ > ρ* mean an accumulation of chains whose rule-phase is either aligned or anti-aligned with the flow, producing a net polarity that the penalty drives back to zero.

**Why SPECULATIVE:**

- Primitive 09 defines polarity but does not specify the restoring-rate structure.
- The canonical range `P₀ ∈ [0.01, 1.0]` is empirical (simulator parameter).
- The connection between tension-polarity and the `P(ρ)` penalty is structurally plausible (both are ED-flow-alignment quantities) but not derived.

### 5.4 v(x, t) ↔ polarity-weighted commitment-rate density (Primitives 09 + 11 + 13)

**Status: SPECULATIVE.**

**Proposal.** The PDE field v is a local, polarity-weighted commitment-rate density. Precisely:

```
v(x, t) = ⟨ π(K, x) · γ_K(x, t) ⟩_K              (9)
```

where `π(K, x) ∈ [−1, 1]` is the polarity of channel K against the local ρ-flow (Primitive 09), `γ_K(x, t)` is the commitment rate in channel K (Primitive 11), and the average runs over available channels at x. Near equilibrium, ⟨v⟩ = 0; non-zero v represents local excess of aligned- or anti-aligned commitment activity.

**Why this candidate:**

- PDE (1b) says v is driven by F[ρ] and damps at rate ζ/τ. Commitment activity is precisely what drives ρ-dynamics (every commitment adds a micro-event). Damping via ζ corresponds to commitment-reserve dissipation (§5.1).
- The feedback term `H · v` in (1a) says non-zero v back-reacts on ρ-evolution. In the proposal, polarity-weighted commitment rate back-reacts on ρ because aligned vs. anti-aligned commitments have different ρ-flow consequences under saturation selection.
- It ties together three primitives (09 polarity, 11 commitment, 13 timing) into a single field — which matches the PDE's role of v as a single mean-field-like quantity.

**Why SPECULATIVE:**

- The ED-Dimensional-01 memo §6.3 explicitly labels v as a "Candidate" interpretation with three alternatives: decoherence-mode amplitude, measurement back-action, environmental-coupling mode. None is uniquely determined.
- Equation (9) is a proposed form, not a derivation. The specific averaging and the precise coupling to F[ρ] are Phase 2 work.
- In the quantum regime, the Dimensional Atlas assigns v units of velocity (`v_phys = v̂ · V₀ = v̂ · c/(2 D_nd) ≈ 1.67c`). The superluminal character is noted as a "scale conversion factor, not a signal speed." In the commitment-rate interpretation, v's units are events-per-volume-per-time; matching to the velocity dimension requires a per-time-per-length normalization, which in turn introduces an additional scale factor. This is not worked out.

### 5.5 Summary of SPECULATIVE class

Four of the seven objects (`ζ, M₀, P₀, v`) are currently SPECULATIVE. This is the operational gap between the primitive stack and the PDE layer. None of the four can be promoted to CANDIDATE without at least one Phase 2 derivation; none is deriving-out-of-reach, but none is done.

---

## 6. Resolving the D(x) drift (tightening pass §3.1)

Per §4.1 above, this memo proposes committing to:

```
D(x) = Σ_K b_K²(x) / (Σ_K b_K(x))²             (10)
```

— the participation-ratio form — and amending Primitive 04 §6 and Primitive 07 §6 to match Primitive 08 §2's formulation.

**Worked consistency check** at the Q-C Boundary transition. The resolution memo gives `D_crit(ζ=1/4) ≈ 0.896`. Under (10), this corresponds to `M_eff ≈ 1.116`, i.e., a single dominant channel carrying ~93% of total bandwidth with the remaining ~7% in secondary channel(s). This is "near-committed regime" — not the "two channels competing" regime that `D = 0.5` / `M_eff = 2` would suggest.

The tightening pass finding that `D_crit = 0.5` is a retired heuristic **still stands under this commitment**; the corrected `D_crit ≈ 0.896` is the operational transition value, and its primitive-level reading is: *the transition occurs when one channel captures 93% or more of the local bandwidth, not when two channels have equal share.*

This is a substantive shift in how the Q-C transition is understood at the primitive level. Phase 2 Path B should use this picture throughout.

---

## 7. Resolving the saturation-definition drift (tightening pass §1.4)

Per tightening pass §5.7, the three framings (05's ρ-magnitude, 06's |∇ρ|-magnitude, 09's joint invocation) are consolidated here as:

**Canonical saturation condition (proposed commitment):**

```
saturated(x) := ρ(x) > ρ_sat  AND  |∇ρ(x)| > κ_sat     (11)
```

with `ρ_sat` and `κ_sat` structural constants to be anchored in Phase 4 as part of the η-derivation program. The joint form captures both primitive framings:

- Primitive 05's framing is the first conjunct: ρ-magnitude above a threshold.
- Primitive 06's framing is the second conjunct: |∇ρ|-magnitude above a threshold.
- Primitive 09's saturated-flow selection operates where **both** conjuncts hold — polarity-selection requires density high enough that rearrangement is constrained (first conjunct) AND gradient steep enough that the direction of flow is unambiguous (second conjunct).

**Physical interpretation of the two constants:**

- `ρ_sat` — the ρ-threshold beyond which new commitment events cannot be accommodated without disrupting existing participation structure. Sets the "ρ_max" of the mobility's `M(ρ_max) = 0` condition. Primitive 05 §7 open question #2.
- `κ_sat` — the |∇ρ|-threshold beyond which the direction of local flow is sharp enough that polarity-selection engages. Primitive 06 §7 open question #2.

**Primitives 05, 06, 09, 11, 12 should cross-reference this shared definition.** This is Fix 3 in the tightening pass prioritization.

---

## 8. Combined mapping picture

Collecting §3–§7, the PDE layer is the thick-regime effective theory of a chain propagating through the participation graph, with:

- ρ counting the density of committed micro-events (Primitive 05)
- D measuring the local concentration of bandwidth into a single dominant channel (Primitives 04 + 08, via participation-ratio (10))
- H measuring the local cross-channel bandwidth structure (complement of D)
- v carrying the local polarity-weighted commitment-rate activity (Primitives 09 + 11 + 13)
- ζ setting the rate at which commitment-reserve bandwidth disperses to environmental bandwidth
- τ setting the participation-relaxation timescale
- M₀ setting the bandwidth-kernel gradient-transmission efficiency at equilibrium
- P₀ setting the polarity-restoration rate at equilibrium
- Saturation operating where (ρ, |∇ρ|) jointly exceed structural thresholds

This is the "Rosetta stone" between the PDE layer and the primitive layer. Three mappings are FORCED, two are CANDIDATE, four are SPECULATIVE.

---

## 9. What must be derived next — prioritized by blocker

### 9.1 For Path B (QM as thin regime)

**Target:** Derive the free-particle Schrödinger equation as the low-D, low-|∇ρ|, high-M_eff limit of the canonical PDE.

**Requires (in order):**

1. **Bandwidth-composition rule** (tightening pass Fix 6): sublinear composition with specified functional form. Blocks Born rule derivation.
2. **D functional form committed** (this memo §4.1 + Fix 2): already proposed (10); needs Primitive 04 / 07 amendments.
3. **v identification** promoted from SPECULATIVE to CANDIDATE (this memo §5.4): requires Phase 2 derivation of the averaging form (9) and the units-matching with the quantum-regime V₀.
4. **Thin-regime PDE limit:** in the regime M_eff ≫ 1 (many channels), D → 0, and (1a) reduces to `∂_t ρ ≈ H · v` — i.e., ρ evolves purely through the participation-channel coupling. Need to show that in this limit (1)–(2) reduce to the Madelung-form fluid equations, which are equivalent to Schrödinger.

Items 1, 2, 3 are prerequisite. Item 4 is the actual Phase 2 derivation.

### 9.2 For Path C Step 2 (Arndt x → D(x))

**Target:** Compute D(x) for Arndt's molecular interferometry system as a function of published control parameters.

**Requires (in order):**

1. **D functional form committed** (this memo §4.1): done if (10) is adopted.
2. **Mapping from Arndt's control parameters to channel bandwidths `{b_K}`.** This is the hypothesis-choice step from the Arndt scaffold §4 Step 2. The cleanest near-term route: use Hornberger-Joos-Zeh decoherence rate `Λ(m, T, p, v_Arndt)` to compute the environmental-bandwidth-band `b_env` as a function of `x`, and derive `b_int, b_adj, b_com` from the four-band partition assuming bandwidth conservation. Then apply (10).
3. **ζ mapping for the Arndt apparatus.** Requires promoting §5.1 from SPECULATIVE to CANDIDATE — which requires the explicit dynamical equation for commitment-reserve dissipation.
4. **D_crit(ζ) evaluation at Arndt's ζ.** Once step 3 is done, plug into D_crit formula from the resolution memo.
5. **Consistency check:** is `D(x_c) = D_crit(ζ_Arndt)` at Arndt's measured transition point?

Items 1 is done. Item 2 is a literature-and-modeling task; the Arndt scaffold already specifies it. Item 3 is the critical Phase 2 blocker. Item 4 is arithmetic. Item 5 is comparison.

**This pathway reveals that Path C Step 2 depends on resolving §5.1 (ζ mapping) first. The Arndt retrodiction therefore cannot precede this specific Phase 2 derivation.**

### 9.3 For Phase 4 (η derivation)

**Target:** Derive η = n_baryon / n_photon ≈ 6 × 10⁻¹⁰ from saturation-era polarity-selection dynamics.

**Requires (in order):**

1. **Saturation condition committed** (this memo §7): joint `(ρ > ρ_sat, |∇ρ| > κ_sat)` form adopted.
2. **Anchored values of ρ_sat, κ_sat** (Phase 4 derivation, likely tied to inflationary-energy scales via the Dimensional Atlas's cosmological regime).
3. **Polarity-selection rate under saturated condition.** This is the fraction of commitment events in which aligned-tension rules successfully instantiate and anti-aligned rules decohere. Requires:
    - **v identification promoted** (§5.4 to CANDIDATE) to track polarity-weighted commitment rate explicitly.
    - **P₀ identification promoted** (§5.3 to CANDIDATE) to track polarity-restoration dynamics.
    - **Cosmological-scale simulator infrastructure** (Primitive 09 §6 notes: does not yet exist).
4. **Computation of surviving-chain / total-commitment ratio** under the dynamics of steps 1–3.

Items 1 is done. Items 2–4 are substantial Phase 4 work; none is close to execution. The infrastructure requirement in item 3 is the largest near-term cost.

### 9.4 Composite blocker ordering

Reading §9.1–§9.3 against each other, the single highest-leverage Phase 2 derivation is:

**Deriving ζ as an explicit dynamical rate from the four-band bandwidth partition.**

This unblocks:
- Path C Step 2 item 3
- Phase 4 item 3 (partially — it also needs v and P₀)
- The D_crit(ζ) formula's anchoring at regime-specific values

Second-highest-leverage:

**Deriving v as a polarity-weighted commitment-rate density from (9) or equivalent.**

This unblocks:
- Path B item 3
- Phase 4 item 3 (remaining portion)

If Fix 1 (this memo) and the two derivations above are completed in sequence, all three downstream programs (Path B, Path C, Phase 4) have their primitive-to-PDE bridge in place.

---

## 10. What this memo does and does not achieve

**Achieves:**

- Establishes a proposed mapping for all seven PDE objects against the primitive stack.
- Classifies each mapping by derivation status (FORCED / CANDIDATE / SPECULATIVE).
- Resolves the D(x) drift identified in the tightening pass (commitment to (10)).
- Resolves the saturation-definition drift (commitment to joint form (11)).
- Identifies the two highest-leverage Phase 2 derivations (ζ and v).

**Does not achieve:**

- None of the four SPECULATIVE mappings is promoted to CANDIDATE by this memo. Each requires explicit Phase 2 derivation.
- The Arndt retrodiction remains blocked on §5.1 (ζ mapping).
- Path B remains blocked on §5.4 (v mapping) and the bandwidth-composition rule (Fix 6).
- Phase 4 remains blocked on §5.3 (P₀ mapping) + cosmological-scale infrastructure.

**The primitive stack is now interface-complete against the PDE layer, but not operationally connected.** The four SPECULATIVE mappings are the operational gap.

---

## 11. Cross-references

- Tightening pass: [quantum/primitives/TIGHTENING_PASS_01.md](../primitives/TIGHTENING_PASS_01.md) §3 (D drift), §5 (missing commitments), §6 (PDE gestures), §7 (prioritized fixes).
- Arndt retrodiction blockers: [quantum/retrodictions/arndt_interferometry.md](../retrodictions/arndt_interferometry.md) §3 (Blocker 1 resolved here at interface level; operational blocker remains in §5.1).
- D_crit resolution: [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md).
- Quantum-regime anchoring: [papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md](../../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md).
- Canonical PDE form: [theory/D_crit_Resolution_Memo.md §2](../../theory/D_crit_Resolution_Memo.md).
- Primitive files: [quantum/primitives/01_micro_event.md](../primitives/01_micro_event.md) through [13_relational_timing.md](../primitives/13_relational_timing.md).

---

## 12. One-line summary

> **The seven PDE-layer objects map as follows: ρ and H (FORCED by Primitive 05 and by D + H = 1); D and τ (CANDIDATE, using the participation-ratio form and the bandwidth-relaxation timescale respectively); ζ, M₀, P₀, v (SPECULATIVE, each requiring one Phase 2 derivation). The D drift is resolved by committing to D = Σb²/(Σb)²; the saturation-definition drift is resolved by committing to the joint form `ρ > ρ_sat AND |∇ρ| > κ_sat`. The two highest-leverage next derivations are ζ (as four-band dissipation rate) and v (as polarity-weighted commitment-rate density). Until those derivations are done, the primitive stack is interface-complete against the PDE but not operationally connected.**
