# ζ Derivation — Commitment-Reserve Dissipation Rate

**Date:** 2026-04-24
**Location:** `quantum/effective_theory/zeta_derivation.md`
**Status:** Derivation memo. Promotes §5.1 of `pde_parameter_mapping.md` from SPECULATIVE toward CANDIDATE. Several modeling choices remain; they are flagged explicitly as CANDIDATE/SPECULATIVE in each section.
**Purpose:** Starting from Primitive 04's four-band bandwidth partition, derive the participation-damping parameter ζ in the canonical PDE (1b) from flux-continuity on the partition and the commitment-rate of Primitive 11. Extract ζ as a ratio of timescales. Work the consequences for `D_crit(ζ)`.

---

## 1. Starting material

### 1.1 The PDE's ζ

The canonical two-channel ED PDE (from `theory/D_crit_Resolution_Memo.md §2`):

```
∂_t ρ = D · F[ρ] + H · v                        (1a)
∂_t v = (F[ρ] − ζ · v) / τ                      (1b)
```

**The role of ζ (FORCED by the PDE structure):** ζ is the dimensionless coefficient of the `−v/τ` term in (1b). It sets the rate at which the participation field v decays toward zero in the absence of F[ρ] forcing. Equivalently: `ζ/τ` is the pure-dissipation rate of v. With `τ` fixed (see `pde_parameter_mapping.md §4.3`), ζ is the dimensionless parameter carrying all of the physical dissipation content.

### 1.2 Primitive 04's four-band partition

**The partition (FORCED by Primitive 04 §1):**

For a chain `C` at position `x`, the local bandwidth budget splits into four bands:

| Band | Symbol | Content |
|---|---|---|
| Internal rule-bandwidth | `b_int` | participation sustaining C's own update rule (identity-maintenance) |
| Adjacency bandwidth | `b_adj` | participation with the immediate participation-adjacent neighborhood |
| Environmental bandwidth | `b_env` | participation with the broader bath beyond the adjacency neighborhood |
| Commitment-reserve bandwidth | `b_com` | participation available for commitment events without disrupting the other three |

Total-budget conservation (Primitive 04 §2, "subject to a conservation-like constraint in the chain's persistence regime"):

```
b_total(C) = b_int + b_adj + b_env + b_com      (2)
```

**Status:** FORCED by Primitive 04's definition. The four-band labels, the non-overlap, and the additive total are all direct from §1.

### 1.3 The v identification (from `pde_parameter_mapping.md §5.4`)

**Candidate identification (SPECULATIVE, per the mapping memo):**

```
v(x, t) = ⟨ π(K, x) · γ_K(x, t) ⟩_K              (3)
```

where `π(K, x) ∈ [−1, 1]` is the polarity of channel K at x (Primitive 09), `γ_K(x, t)` is the commitment rate in channel K (Primitive 11), and the average runs over available channels at x.

For the ζ derivation below, we need only the weaker claim: **v is a local commitment-activity field that draws on b_com at a rate proportional to Γ_com, and decays through bandwidth fluxes that do not feed back into ρ-dynamics.** This weaker claim is CANDIDATE — it follows from v being any commitment-activity-related field, without committing to the specific polarity-weighted form (3).

---

## 2. Flux-continuity on the four-band partition

### 2.1 Conservation structure (CANDIDATE)

For a partitioned conserved quantity, the natural dynamical structure is flux-continuity: each band's content evolves by its net pair-flux with other bands, plus external sources/sinks.

For four bands, there are `C(4,2) = 6` ordered pair-fluxes. Let `J_{X→Y}(x, t)` denote the flux from band X to band Y at position x, time t (units: bandwidth per unit volume per unit time; sign by convention ≥ 0). Then:

```
db_X/dt = Σ_Y (J_{Y→X} − J_{X→Y})               (4)
```

with conservation requiring `Σ_X (db_X/dt) = 0` in the isolated-chain limit (no external source/sink).

**Status: CANDIDATE.** Flux-continuity is the standard structural form for partitioned conserved quantities. Primitive 04 does not derive this form, but it does not contradict it either. Proposing it is defensible; asserting it would be unwarranted until each flux is physically justified.

### 2.2 Non-zero pair-fluxes (CANDIDATE)

Most pair-fluxes are physically meaningful; some are negligible in the chain-persistence regime. Here is the proposed structure, with reasoning:

| Flux | Physical content | Status |
|---|---|---|
| `J_int → adj` | chain rule-updates drive adjacency coupling (continuous during propagation) | CANDIDATE |
| `J_adj → com` | adjacency bandwidth "charges" the commitment reserve as the chain prepares for the next commitment event | CANDIDATE |
| `J_com → int` | at each commitment, part of the reserve consolidates into the next step of the chain's internal rule-bandwidth | CANDIDATE |
| `J_com → env` | at each commitment, part of the reserve disperses into environmental bandwidth | **load-bearing for ζ — CANDIDATE** |
| `J_adj → env` | adjacency coupling continuously loses bandwidth to environment (decoherence of non-commitment interactions) | CANDIDATE |
| `J_int → env` | internal rule-bandwidth loss to environment (chain decay) | **negligible** in stable chain regime |

**Status of the whole table: CANDIDATE.** Each entry is physically motivated but none is derived from Primitive 04's text. A different partition of the non-zero fluxes — e.g., allowing `J_env → adj` in strongly-driven regimes — would be defensible. The structure above is the minimum needed to support the ζ derivation.

### 2.3 The four continuity equations

Writing (4) out for each band:

```
db_int/dt = J_{com→int} − J_{int→adj}                           (5a)
db_adj/dt = J_{int→adj} − J_{adj→com} − J_{adj→env}             (5b)
db_com/dt = J_{adj→com} − J_{com→int} − J_{com→env}             (5c)
db_env/dt = J_{adj→env} + J_{com→env}                           (5d)
```

Adding: `d(b_total)/dt = 0`. ✓ (Conservation-check passes, as required.)

**Status: FORCED given (2) and the flux-set in §2.2.** Once the partition and the non-zero fluxes are chosen, these equations follow by bookkeeping.

---

## 3. Identifying J_{com → env}

### 3.1 Commitment events as the flux source (CANDIDATE)

From Primitive 11 §1–§2: a commitment event is a discrete selection of a channel by a chain, together with the addition of a new micro-event along that channel. Each event:

1. Draws from commitment-reserve bandwidth (Primitive 11 §2: "Γ_commit ~ b_int / commitment-reserve budget").
2. Produces a new micro-event, contributing to ρ (Primitive 05) and ultimately to thickening (Primitive 12).
3. Redistributes the drawn bandwidth into some combination of `b_int` (continuation of chain), `b_adj` (onward adjacency), and `b_env` (dispersion to environment).

Let:

- `Γ_com(x, t)` = commitment-event rate per unit volume at x, t (Primitive 11)
- `Δb_per_event` = bandwidth consumed per commitment event (a normalization; units of bandwidth)
- `α_env ∈ [0, 1]` = fraction of the consumed bandwidth that disperses to environment (the irretrievable part)

Then:

```
J_{com → env}(x, t) = α_env · Γ_com(x, t) · Δb_per_event        (6)
```

**Status: CANDIDATE.**

- `Γ_com` is FORCED as a Primitive-11 quantity; the rate is defined in 11 §2.
- `Δb_per_event` is a CANDIDATE normalization; Primitive 11 does not commit to a specific value. Setting `Δb_per_event = 1` (one unit of bandwidth per commitment) is the natural convention and is adopted below.
- `α_env` is SPECULATIVE in its specific value but CANDIDATE in structure: every commitment must lose *some* fraction to environment (else coherence never decays), and must retain some fraction (else no chain persistence), so `α_env ∈ (0, 1)` is structurally necessary even if the number isn't pinned down.

### 3.2 Substitution into the b_com equation

Plugging (6) into (5c) and setting `Δb_per_event = 1`:

```
db_com/dt = J_{adj→com} − J_{com→int} − α_env · Γ_com           (7)
```

In steady state (`db_com/dt = 0`), the three terms balance:

```
J_{adj→com} = J_{com→int} + α_env · Γ_com                       (8)
```

i.e., the rate at which adjacency bandwidth "charges" the commitment reserve equals the rate at which commitment events consume it — partly into chain continuation (`J_{com→int}`) and partly into environment (`α_env · Γ_com`). This is a sanity check: the commitment-reserve is sustained by adjacency in-flux matching commitment out-flux.

---

## 4. Extracting ζ

### 4.1 The v-dissipation rate

PDE equation (1b): `∂_t v = (F[ρ] − ζ v) / τ`. In the absence of F[ρ] forcing:

```
∂_t v = −(ζ/τ) · v                              (9)
```

— v decays exponentially at rate `ζ/τ`. This is the pure-dissipation rate of v.

**Physical content (CANDIDATE):** the commitment-activity field v decays because the commitment events feeding it are themselves damped when their output disperses into environment rather than feeding back into further ρ-dynamics. The `J_{com→env}` flux is precisely the part of commitment activity that does not feed back.

### 4.2 Identification (CANDIDATE)

Proposal: the pure-dissipation rate of v equals the relative rate at which commitment-reserve bandwidth leaks to environment:

```
ζ/τ = J_{com → env} / b_com                     (10)
```

— i.e., `ζ/τ` is the fractional dissipation rate of b_com into environment per unit time.

**Why this identification:**

- Dimensional check: `J_{com→env}` has units of bandwidth per volume per time; `b_com` has units of bandwidth per volume; the ratio has units of 1/time. Multiplied by `τ` (time), it gives a dimensionless ζ. ✓
- The PDE's ζ is canonically dimensionless; the identification preserves that.
- v is a commitment-activity quantity; the rate at which commitment activity irreversibly disperses is the natural rate of v-decay.

**Substituting (6) into (10):**

```
ζ = τ · α_env · Γ_com / b_com                   (11)
```

This is the proposed ζ-formula.

### 4.3 Equivalent form: ratio of timescales

Define the commitment-dissipation timescale `τ_com`:

```
τ_com ≡ b_com / (α_env · Γ_com)                 (12)
```

— the time for the current commitment-reserve to be fully dissipated to environment at the current commitment rate. Then (11) becomes:

```
ζ = τ / τ_com                                   (13)
```

— ζ is the ratio of participation-relaxation timescale to commitment-dissipation timescale.

**Status of (11)–(13): CANDIDATE.** The derivation chain is:
- (4) flux-continuity structure — CANDIDATE
- (6) commitment-event flux identification — CANDIDATE
- (10) v-dissipation rate identification — CANDIDATE
- (11)–(13) arithmetic — FORCED given the above

The whole chain is no stronger than its weakest link, which is (10).

### 4.4 Canonical simulator value revisited

The canon-default `ζ = 0.25` corresponds under (13) to `τ_com ≈ 4τ` — the commitment-reserve dissipates on a timescale 4× longer than the participation-relaxation timescale. This is a simulator convention, not a derived number.

Under (11) with `Δb_per_event = 1`, ζ = 0.25 corresponds to:

```
α_env · Γ_com · τ / b_com = 0.25                (14)
```

— i.e., at canonical parameters, about 25% of `b_com` dissipates per `τ`, via the fraction `α_env` of commitment events. This is a derived relationship for the canonical point; it does not pin down `α_env`, `Γ_com`, or `b_com` individually.

---

## 5. Regime analysis

### 5.1 Small-ζ limit (τ_com ≫ τ)

When commitments dissipate to environment much more slowly than participation relaxes, ζ → 0. From the D_crit formula:

```
D_crit(0) = 2√2 − 2 ≈ 0.828                     (15)
```

Physical content: the system behaves as if participation damping is absent; the only damping comes from the direct channel `Dε_k`. The Q-C transition is at a slightly lower D than at canonical ζ (0.828 vs. 0.896 at ζ=0.25).

### 5.2 Large-ζ limit (τ_com ≪ τ)

When commitments dissipate to environment faster than participation can relax, ζ → 1. From the D_crit formula:

```
D_crit(1) = 1                                   (16)
```

Physical content: the participation channel is so heavily damped that it effectively never oscillates; the system is effectively single-channel (diffusion-only) and always in the committed regime. No Q-C transition exists because no underdamped regime exists.

### 5.3 Intermediate ζ — Arndt-scale considerations

For Arndt molecular interferometry with Hornberger-Joos-Zeh environmental decoherence rate `Λ` (typically `10³–10⁸ s⁻¹` depending on mass, temperature, residual gas pressure):

**If τ is identified with a Compton-time-like scale:** a molecule of mass `~10⁴ amu` has Compton time `~10⁻³⁴ s`, giving `ζ = Λτ ~ 10⁻³¹–10⁻²⁶` — effectively zero. Then `D_crit ≈ 0.828` (from (15)).

**If τ is identified with an internal-relaxation timescale** (vibrational period, electronic relaxation: `~10⁻¹⁴ to 10⁻¹¹ s`): `ζ = Λτ ~ 10⁻¹¹–10⁻³`. Still small, still near `D_crit ≈ 0.828`.

**If τ is identified with the Talbot time** `T_T = M d_g² / h` (the characteristic interferometer timescale, `~10⁻³ to 10⁻²` s for Arndt's apparatus): `ζ = Λ T_T ~ 10⁰–10⁵`. The large-ζ values don't make physical sense in the PDE; this identification is almost certainly wrong.

**Status of this regime analysis: SPECULATIVE.** The identification of τ in the Arndt regime is not settled. The three candidates (Compton, internal, Talbot) produce ζ spanning 30+ orders of magnitude. Resolving this is a live task for Path C Step 2.

**Best-guess near-term assumption for Path C Step 2:**

τ ↔ internal-relaxation timescale of the molecular species (vibrational or electronic), on the grounds that:

- It matches the primitive-level notion "participation-bandwidth relaxation timescale" (`pde_parameter_mapping.md §4.3`) for a composite chain whose internal rule is set by molecular structure.
- It is experimentally accessible: published vibrational and electronic relaxation times exist for all common Arndt-target molecules.
- It gives `ζ_Arndt ≪ 1` for all relevant regimes, placing `D_crit ≈ 0.83` as the Arndt transition prediction.

This is a CANDIDATE assumption, not a derived value. Committing to it and testing against Arndt data is the actual Path C Step 2 work.

---

## 6. What this derivation achieves and does not achieve

### 6.1 Promoted

**§5.1 of `pde_parameter_mapping.md` is promoted from SPECULATIVE to CANDIDATE.** The ζ formula (11) is now derived from:

- Primitive 04's four-band partition (FORCED)
- A flux-continuity structure across the four bands (CANDIDATE)
- The commitment-event flux (6) (CANDIDATE, with α_env as the remaining free parameter)
- The identification (10) of v-dissipation rate with commitment-reserve-to-environment flux (CANDIDATE)

Four CANDIDATE links, one FORCED foundation. No link is SPECULATIVE after this derivation — each has explicit physical content defensible from the primitives.

### 6.2 Not promoted

**The specific value of α_env is not derived.** It remains a free parameter in (0, 1). Its value determines ζ via (11).

**The identification of τ in a given physical regime is not settled.** §5.3 discussed three candidates spanning 30+ orders of magnitude.

**The flux-continuity structure (4)–(5) is not forced.** A different partition of non-zero fluxes would give a different ζ formula. The structure here is the minimum-complexity version; it has not been cross-checked against simulator behavior or against known limits (e.g., the BCS-Josephson regime, where `ζ` should presumably be small because shared participation dominates).

### 6.3 Residual SPECULATIVE items

Three:

1. `α_env` specific value (structural; derivable in principle from polarity-selection statistics at commitment)
2. `τ` identification for given physical regime (requires Path C Step 2 to resolve)
3. The minimum-complexity flux-set in §2.2 (correctness check against simulator or against analytic cases)

---

## 7. Effect on D_crit and the PDE discriminant

From the D_crit resolution memo, the underdamping discriminant in Regime B is `(D − ζ)² < 4(1 − D)` at reference mode `ε_k · τ = 1`, with:

```
D_crit(ζ) = √(2 − ζ) · (2 − √(2 − ζ))           (17)
```

Plugging in (13) (`ζ = τ/τ_com`):

```
D_crit(τ/τ_com) = √(2 − τ/τ_com) · (2 − √(2 − τ/τ_com))    (18)
```

For `τ ≪ τ_com` (weakly-damped participation): D_crit → 2√2 − 2 ≈ 0.828
For `τ → τ_com`: D_crit → 1
For `τ = τ_com/4` (canonical): D_crit ≈ 0.896

**Consequence:** the Q-C transition `x_c` — the experimental control parameter at which `D(x_c) = D_crit(ζ)` — is a function of `τ_com(x)` and `τ(x)` evaluated at the operating point of the experiment. Both are experimentally accessible in principle:

- `τ` ↔ internal-relaxation timescale of the chain's rule (candidate)
- `τ_com` ↔ `b_com / (α_env · Γ_com)` — a property of the chain's commitment dynamics

The `α_env`-dependence remains; experiments would have to pin it down by fit or by independent physical argument.

---

## 8. Implications for the three downstream programs

### 8.1 Path C Step 2 (Arndt x → D(x))

**Unblocked, partially.** The ζ formula (11) gives an explicit mapping from commitment-rate and commitment-reserve to the PDE damping parameter. Combined with the D = 1/M_eff commitment from `pde_parameter_mapping.md §4.1` and the Arndt scaffold's eight-step derivation, the remaining blockers are:

1. **`α_env` value at Arndt's apparatus** — can be treated as a one-parameter fit in the first-pass retrodiction, with explicit disclosure that the retrodiction is not zero-free-parameter. Or derived from polarity-selection statistics.
2. **τ identification** — best-guess candidate: internal vibrational/electronic relaxation timescale of Arndt's target molecules. Literature values available.
3. **Γ_com at Arndt's apparatus** — has to be estimated from the experimental timescale. One route: identify `Γ_com ~ 1/(Talbot time)` at the transition point and check for consistency.
4. **b_com magnitude** — set by the bandwidth-normalization convention; absorbed into `α_env` definition in first-pass.

**Executable near-term work:** compile published values of (molecular mass, internal relaxation time, Talbot time, Hornberger-Joos-Zeh Λ) for one specific Arndt dataset; compute ζ_Arndt = Λ · τ under the internal-relaxation candidate; compute D_crit(ζ_Arndt); compare to measured `D(x_c)` from visibility-vs-mass curve.

**This is the next executable step toward an actual Arndt retrodiction.** It requires no further theory derivation beyond what this memo provides. It requires literature work and a one-parameter (`α_env`) first-pass.

### 8.2 Path B (QM as thin regime)

**Partially enabled.** The v-dissipation rate structure (10) gives an explicit form for the participation-field damping. Combined with the four-band partition, this provides the ingredients for the thin-regime limit of the PDE:

- In the thin regime (`M_eff ≫ 1`, bandwidth spread across many channels), the commitment rate `Γ_com` is small because each individual commitment is low-probability.
- Therefore `ζ ∝ Γ_com / b_com` is small; participation is weakly damped.
- The underdamping condition `(D − ζ)² < 4(1 − D)` is easily satisfied for small D and small ζ.
- The PDE enters the oscillatory regime characteristic of wavefunction-like dynamics.

The next derivation for Path B is to work out the precise reduction to Madelung form in the `D → 0, ζ → 0, M_eff → ∞` limit. This is a separate derivation, not accomplished here.

### 8.3 Phase 4 (η derivation)

**Partially enabled.** The ζ-via-commitment-flux formula (11) is structurally what the η derivation needs: in the saturated early-universe regime, the polarity-selection rule operates via differential α_env for aligned vs. anti-aligned commitments. Specifically:

- For aligned-tension chains in saturated ED-flow: commitments complete without disrupting the saturation structure; α_env is small. The chain persists; ρ_baryon grows.
- For anti-aligned chains: commitments require participation rearrangement that saturation cannot provide; α_env is large (≈ 1). The chain decoheres; commitments dissipate to environment (radiation) rather than persist as matter.

The η ratio is then, schematically:

```
η ~ (1 − ⟨α_env⟩_aligned) / (1 − ⟨α_env⟩_anti-aligned)
```

— the ratio of persistence-fractions. If `⟨α_env⟩_aligned ≈ 0` and `⟨α_env⟩_anti-aligned ≈ 1 − ε` for small `ε`, then `η ≈ 1/ε` — small.

**This is suggestive but not yet computational.** Computing the actual `⟨α_env⟩` values for the two polarity classes under saturated conditions requires the cosmological-scale ρ-evolution + polarity-selection simulator infrastructure flagged in Primitive 09 §6 (still does not exist). It also requires deriving `α_env` from first principles rather than treating it as a free parameter (§6.3 item 1).

**What this derivation adds to the η program:** a concrete structural form (η as a ratio of polarity-dependent α_env's). The form was not previously written down explicitly.

---

## 9. Open questions

1. **α_env derivation from first principles.** The specific value of the environment-dispersion fraction per commitment event is the single free parameter in (11). Deriving it from polarity-selection statistics (Primitive 09) and commitment-dynamics (Primitive 11) is the next Phase 2 derivation target.

2. **τ regime-dependence.** §5.3 shows three candidate identifications spanning 30+ orders of magnitude. The operational τ for a given physical system needs explicit anchoring. The quantum-regime Compton anchoring (Dimensional Atlas) is FORCED for elementary particles but unclear for composite chains (molecules, Cooper pairs, macroscopic systems).

3. **Flux-set minimality.** Are (5a)–(5d) complete, or are there secondary fluxes (`J_env→adj` in driven regimes, `J_int→com` in rapid-reconfiguration regimes) that matter near the Q-C transition? Simulator cross-check required.

4. **Cross-check against BCS / superconducting regime.** In a superconductor, the chain-complex is macroscopic and non-individuated (Primitive 10); one expects very small ζ (participation dominates; little loss to environment). Does the formula (11) produce small ζ in this regime? Needs explicit working.

5. **Cross-check against Zeno regime.** Very frequent measurements suppress commitment-induced rearrangement; Γ_com should be high but `α_env` also high (environment-forced). Does ζ come out large? Needs working.

6. **The participation-reserve-vs-kinetic identity.** If `v` is polarity-weighted commitment-rate, the PDE's (H · v) term in (1a) feeds this back into ρ-dynamics. The feedback loop through F[ρ] must be consistent with (11)'s identification of the pure-dissipation rate. Explicit loop-closure check needed.

---

## 10. Summary table

| Derivation step | Status | Source |
|---|---|---|
| Four-band partition | FORCED | Primitive 04 §1–§2 |
| Total-bandwidth conservation | FORCED | Primitive 04 §1 |
| Flux-continuity structure (4)–(5) | CANDIDATE | Standard form for partitioned conserved quantities |
| Six-pair flux set (§2.2 table) | CANDIDATE | Physical motivation per band-pair |
| `J_com→env = α_env · Γ_com` (6) | CANDIDATE | Primitive 11 commitment dynamics |
| `Γ_com` as per-volume commitment rate | FORCED | Primitive 11 §2 |
| `Δb_per_event = 1` normalization | CANDIDATE | Convention |
| `α_env ∈ (0, 1)` | FORCED (structural); SPECULATIVE (specific value) | Non-degeneracy of chain persistence and coherence decay |
| `ζ/τ = J_com→env / b_com` (10) | CANDIDATE | Identification of v-dissipation rate with commitment-reserve dissipation |
| `ζ = τ · α_env · Γ_com / b_com` (11) | CANDIDATE (inherited) | Derived from (10) + (6) |
| `ζ = τ/τ_com` (13) | FORCED given (11) | Rewriting |
| `D_crit(ζ)` formula | FORCED | D_crit Resolution Memo §7.1 |
| Effect on Arndt: `ζ_Arndt ≪ 1 → D_crit ≈ 0.83` | SPECULATIVE | Depends on τ identification |
| Structural form of η | SPECULATIVE | Depends on polarity-dependent α_env |

---

## 11. Cross-references

- PDE-parameter mapping: [quantum/effective_theory/pde_parameter_mapping.md](pde_parameter_mapping.md) §5.1.
- Tightening pass: [quantum/primitives/TIGHTENING_PASS_01.md](../primitives/TIGHTENING_PASS_01.md) §3, §7 Fix 1.
- Arndt retrodiction: [quantum/retrodictions/arndt_interferometry.md](../retrodictions/arndt_interferometry.md) §3.1 (Blocker 1, ζ-mapping portion now partially resolved).
- D_crit formula: [theory/D_crit_Resolution_Memo.md](../../theory/D_crit_Resolution_Memo.md) §5.3, §7.1.
- Quantum-regime anchoring: [papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md](../../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md) §2, §6.3.
- Primitive 04 (four-band partition): [quantum/primitives/04_participation_bandwidth.md](../primitives/04_participation_bandwidth.md) §1, §2.
- Primitive 11 (commitment rate): [quantum/primitives/11_commitment.md](../primitives/11_commitment.md) §1–§2.

---

## 12. One-line summary

> **The PDE damping parameter ζ derives as `ζ = τ/τ_com` where `τ_com = b_com/(α_env · Γ_com)` is the commitment-reserve-to-environment dissipation timescale. This promotes the ζ mapping from SPECULATIVE to CANDIDATE, leaves α_env as the single free parameter, suggests Arndt's ζ ≪ 1 (transitions at D_crit ≈ 0.83 rather than 0.896), and provides a concrete structural form for η as a ratio of polarity-dependent environment-dispersion fractions.**
