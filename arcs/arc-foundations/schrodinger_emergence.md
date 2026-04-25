# QM Step 2 — Schrödinger Emergence from Participation Dynamics

**Date:** 2026-04-24
**Location:** `quantum/foundations/schrodinger_emergence.md`
**Status:** Step 2 derivation. Shows that the Schrödinger equation emerges as the thin-participation limit of the participation-measure evolution `iℏ ∂_t P_K = H_K P_K + Σ_{K'} V_{KK'} P_{K'}`. Under appropriate channel-index identifications (momentum basis in the continuous limit), the coherent sum `Ψ = Σ_K P_K` satisfies a standard linear Schrödinger equation. Madelung equivalence demonstrated. Canonical ED PDE at D = 0 reproduces the real-valued (ρ, S) dynamics as a consistency check.
**Purpose:** Execute Step 2 of the QM-emergence program. Does not begin Steps 3–5.

---

## 1. Starting material

### 1.1 The participation-measure evolution

From `participation_measure.md §5.1` equation (9):

```
iℏ ∂_t P_K(x, t) = H_K · P_K(x, t) + Σ_{K'} V_{KK'} · P_{K'}(x, t)            (1)
```

— a Schrödinger-form equation on the channel index K, with diagonal Hamiltonian `H_K` and off-diagonal couplings `V_{KK'}`.

**Status of (1):** CANDIDATE — proposed in `participation_measure.md` as the simplest form consistent with the four ED primitive-level structural requirements. A derivation from ED primitives + PDE structure to uniquely specify this form is flagged as an open Step-2-residual item; adopted here provisionally.

### 1.2 The participation-measure decomposition

```
P_K(x, t) = √(b_K(x, t)) · e^{i π(K, x, t)}                                    (2)
```

and the four-band decomposition:

```
P_K = P_K^{int} + P_K^{adj} + P_K^{env} + P_K^{com}                            (3)
```

### 1.3 Derived quantities (from participation_measure.md §2.3)

- `ρ(x, t) = Σ_K |P_K|² = Σ_K b_K`           — event density
- `M_eff = (Σ_K |P_K|²)² / Σ_K |P_K|⁴`        — effective multiplicity
- `D_P = 1/M_eff`                              — participation-ratio
- `Ψ(x, t) = Σ_K P_K(x, t)`                    — coherent sum (candidate for QM wavefunction)

### 1.4 Structural claim

**In the thin-participation limit defined in §2, the coherent sum Ψ(x, t) satisfies the standard linear Schrödinger equation.**

This is the content of Step 2. What follows is the derivation and a careful labeling of which parts are FORCED by (1) and which involve further CANDIDATE or SPECULATIVE identifications.

---

## 2. Defining the thin-participation limit

The thin-participation limit is the regime in which:

### 2.1 M_eff → ∞

Bandwidth is distributed across many channels with no single dominant channel. Per `d_variable_disambiguation.md §4.2`, this regime has `D_P → 1/N` (for N channels), placing the system at D_E ≈ 0 under the affine mapping. At D_E = 0 the ED PDE is pure-participation-channel (per `bec_pde_mapping.md §5.3`).

### 2.2 Channel index K becomes continuous

In the thin-many-channel limit, the discrete channel sum becomes an integral:

```
Σ_K  →  ∫ dK                                                                   (4)
```

with an appropriate measure on the continuous label K. **For the identification with QM to work cleanly, K becomes the momentum label k** (see §3 below).

### 2.3 Environmental band suppressed

The chain is isolated: `P_K^{env} ≈ 0` and `P_K^{com}` evolves slowly (no commitment events). The four-band decomposition (3) reduces effectively to `P_K ≈ P_K^{int} + P_K^{adj}`.

**Physical consequence:** no decoherence (b_env doesn't grow), no commitment (b_com doesn't deplete). The chain is in the "pure coherent evolution" regime that Schrödinger describes.

### 2.4 Commitment and thickening negligible

Per Primitives 11 and 12: no commitment events occur, so ρ doesn't gain new micro-events from the chain's own dynamics (it evolves by redistribution only). Thickening (τ, per Primitive 12) accumulates at scales much slower than the Schrödinger dynamics timescale.

### 2.5 Bandwidth-conservation constraint preserved

Total bandwidth is conserved along the isolated chain:

```
∫ dx Σ_K |P_K(x, t)|² = ∫ dx ρ(x, t) = N = const                               (5)
```

— normalization of the wavefunction.

### 2.6 Formal definition

**Thin-participation limit:** `(M_eff, b_env, Γ_commit) → (∞, 0, 0)` with total bandwidth (5) held fixed. Under this limit, (1) governs the evolution of `P_K(x, t)` with well-defined continuum sum over K.

**Status of §2.1–§2.6: FORCED by the primitive-level characterization of "thin regime" (per Primitives 04 §1.5, 08 §1, 10 §1; `pde_parameter_mapping.md §4.1`).**

---

## 3. Identifying the continuous channel label

### 3.1 The requirement

For (1) to reduce to Schrödinger on `Ψ = ∫ dK P_K`, the continuous channel label must be identified with a basis on which the Hamiltonian acts naturally. Several candidates:

- **Position basis (K = x):** P_{x'}(x, t) would be a representation of the wavefunction in position basis at position x. Natural but trivial (Ψ = P at the diagonal).
- **Momentum basis (K = k):** P_k(x, t) is the k-mode amplitude at position x. Non-trivial; Ψ(x, t) = ∫ dk P_k(x, t) = inverse Fourier transform.
- **Energy basis (K = E):** P_E(x, t) is the energy-eigenstate amplitude at position x. Useful for stationary states.

**Adopted identification (CANDIDATE): K ↔ k (momentum).** Rationale:

- Momentum is the natural conjugate label to position in a translationally-invariant setting.
- In the thin limit, plane-wave-like participation (uniform in space, definite k) is the simplest basis.
- The Hamiltonian has standard form in momentum basis: `H_k = ℏ²k²/(2m) + V` (diagonal kinetic + potential matrix).

**Status: CANDIDATE.** Alternative identifications (energy, angular momentum, etc.) would give the same Schrödinger equation under appropriate basis-transformation; the choice of k is the most economical for the derivation.

### 3.2 Explicit form of P_k

In momentum representation, a plane-wave participation mode has:

```
P_k(x, t) = c_k(t) · e^{i k x} / √(2π)                                         (6)
```

(one-dimensional; multi-D extension by replacing kx with k·x).

Here `c_k(t)` is the k-mode amplitude (time-dependent), carrying both the magnitude and the phase of the participation in channel k.

**Coherent sum:**

```
Ψ(x, t) = ∫ dk P_k(x, t) = ∫ dk c_k(t) · e^{i k x} / √(2π)                    (7)
```

This is the inverse Fourier transform of c_k. **Ψ(x, t) is a complex-valued spacetime field — the QM wavefunction.**

**Normalization:** from (5), ∫ dx |Ψ|² = ∫ dk |c_k|² = N (Plancherel theorem). Conventional normalization N = 1.

---

## 4. Deriving the Schrödinger equation

### 4.1 Apply (1) to (6)

```
iℏ ∂_t P_k(x, t) = H_k · P_k(x, t) + ∫ dk' V_{kk'} · P_{k'}(x, t)              (8)
```

In momentum basis:
- **H_k = ℏ²k²/(2m)** — free kinetic energy of a mode with momentum k (diagonal in k).
- **V_{kk'} = ⟨k|V̂|k'⟩** — potential-energy matrix element between k and k' modes.

For local potential V(x): V_{kk'} = Ṽ(k - k') (Fourier transform of V).

### 4.2 Substitute (6) into (8)

LHS: `iℏ ∂_t [c_k · e^{ikx}/√(2π)] = iℏ (ċ_k) · e^{ikx}/√(2π)` where ċ_k = dc_k/dt.

RHS first term: `H_k · c_k · e^{ikx}/√(2π) = (ℏ²k²/2m) · c_k · e^{ikx}/√(2π)`.

RHS second term: `∫ dk' V_{kk'} · c_{k'} · e^{ik'x}/√(2π) = ∫ dk' Ṽ(k-k') c_{k'} · e^{ik'x}/√(2π)`.

Equating and multiplying by √(2π) · e^{-ikx}:

```
iℏ ċ_k = (ℏ²k²/2m) c_k + ∫ dk' Ṽ(k-k') c_{k'} · e^{i(k'-k)x}                  (9)
```

**Problem:** the right-hand side has explicit x-dependence via the exponential, but the left-hand side depends only on k and t. **(9) is therefore not a closed equation for c_k(t) unless we average over x or identify a consistency condition.**

### 4.3 Resolution: integrate over x

The correct move is to track the entire wavefunction Ψ(x, t) rather than the individual c_k(t). Define Ψ = ∫ dk P_k = ∫ dk c_k e^{ikx}/√(2π).

**Apply ∫ dk to both sides of (8):**

LHS: `∫ dk [iℏ ∂_t P_k] = iℏ ∂_t Ψ`.

RHS first term: `∫ dk H_k P_k = ∫ dk (ℏ²k²/2m) c_k e^{ikx}/√(2π) = -ℏ²/(2m) · ∇² Ψ` (Fourier identity: k² in momentum space = -∇² in position space).

RHS second term: `∫ dk ∫ dk' V_{kk'} P_{k'} = ∫ dk' [∫ dk Ṽ(k-k')] · c_{k'} e^{ik'x}/√(2π)`.

For local V: `∫ dk Ṽ(k-k') = ?` — this doesn't converge generically; Ṽ(k-k') is a kernel.

**Better resolution: use the operator formulation.** The momentum-space representation of the Hamiltonian is:

```
Ĥ = P̂²/(2m) + V(x̂)                                                            (10)
```

where P̂ acts as -iℏ∇ in position basis, and V(x̂) is the multiplicative potential operator.

Under the expansion Ψ(x, t) = ∫ dk P_k(x, t), applying Ĥ gives:

```
(Ĥ Ψ)(x, t) = -ℏ²/(2m) ∇²Ψ(x, t) + V(x) Ψ(x, t)                               (11)
```

— the standard position-space Hamiltonian acting on Ψ.

### 4.4 The closed evolution on Ψ

**Claim (CANDIDATE):** under the momentum-basis identification K ↔ k, the operator-level participation-measure evolution (1) applied to the coherent sum (7) yields:

```
iℏ ∂_t Ψ(x, t) = Ĥ Ψ(x, t) = [-ℏ²/(2m) ∇² + V(x)] Ψ(x, t)                    (12)
```

**This is the Schrödinger equation.**

**Sketch of derivation:**

The participation-measure evolution (1) is a first-order-in-time linear equation on P_K. The sum over K (which in the momentum-basis identification is the integral ∫ dk) preserves linearity: if each P_k evolves linearly, so does their sum Ψ. The coefficient structure (H_k diagonal + V_{kk'} off-diagonal) corresponds to the momentum-space representation of the operator Ĥ = P̂²/(2m) + V(x̂). When (1) is summed over k, the momentum-space Hamiltonian acts on Ψ(x, t) via the standard Fourier correspondences (k² ↔ -∇², V_{kk'} ↔ V(x̂)).

**Status: CANDIDATE.** The derivation requires:

- **(a)** Linearity of (1) — FORCED by the form of the evolution equation as given.
- **(b)** The channel index K becoming k (momentum) in the thin limit — CANDIDATE per §3.1.
- **(c)** The identification H_k = ℏ²k²/(2m) and V_{kk'} = ⟨k|V̂|k'⟩ — CANDIDATE; requires an argument that the thin-limit kinetic structure is standard free-particle form.
- **(d)** The operator correspondence between (H_k, V_{kk'}) and (P̂²/2m, V(x̂)) — FORCED by Fourier analysis given (c).

Under (a)–(d), (12) follows.

### 4.5 Status of (12)

**FORCED:** linearity and the operator form of Schrödinger.
**CANDIDATE:** the specific identification H_k = free kinetic + potential, which requires the thin-limit mode structure to be plane-wave-like.
**Not in hand:** a derivation from ED primitives that uniquely selects the free-particle kinetic form. This is a sub-task of Step 2 that could be extended in a dedicated follow-up memo.

---

## 5. Madelung equivalence

Given Schrödinger (12), show it is equivalent to the Madelung fluid form.

### 5.1 Polar decomposition

Write the wavefunction as:

```
Ψ(x, t) = √(ρ(x, t)) · e^{i S(x, t)/ℏ}                                         (13)
```

— amplitude × phase decomposition. ρ = |Ψ|² is the event density; S is the phase × ℏ.

### 5.2 Substitution into Schrödinger (12)

Compute derivatives:

```
∂_t Ψ = [(∂_t √ρ) + (i/ℏ) √ρ (∂_t S)] · e^{iS/ℏ}                              (14a)
∇Ψ = [(∇√ρ) + (i/ℏ) √ρ (∇S)] · e^{iS/ℏ}                                        (14b)
∇²Ψ = [∇²√ρ + 2(i/ℏ)(∇√ρ)·(∇S) + (i/ℏ)√ρ ∇²S - (1/ℏ²)√ρ|∇S|²] · e^{iS/ℏ}     (14c)
```

### 5.3 Substitute into iℏ ∂_t Ψ = [-ℏ²/(2m) ∇² + V] Ψ

Divide through by e^{iS/ℏ}:

```
iℏ (∂_t √ρ) - √ρ (∂_t S)
  = -ℏ²/(2m) [∇²√ρ + 2(i/ℏ)(∇√ρ)·(∇S) + (i/ℏ)√ρ ∇²S - (1/ℏ²)√ρ|∇S|²] + V √ρ
                                                                                (15)
```

Expand the RHS:

```
RHS = -ℏ²/(2m) ∇²√ρ
      - iℏ/m · (∇√ρ)·(∇S)
      - iℏ/(2m) · √ρ ∇²S
      + √ρ |∇S|²/(2m)
      + V √ρ
```

### 5.4 Real-imaginary split

**Real part of (15):**

```
-√ρ (∂_t S) = -ℏ²/(2m) ∇²√ρ + √ρ |∇S|²/(2m) + V √ρ                           (16)
```

Rearrange:

```
∂_t S + |∇S|²/(2m) + V + Q = 0                                                 (17)
```

where `Q = -ℏ²/(2m) · ∇²√ρ / √ρ` is the **Bohm quantum potential**.

**(17) is the Hamilton-Jacobi equation with a quantum-pressure correction.** Classical Hamilton-Jacobi has ∂_t S + |∇S|²/(2m) + V = 0; the quantum correction Q adds the coupling of the phase evolution to the density profile.

**Imaginary part of (15):**

```
ℏ (∂_t √ρ) = -ℏ/m · (∇√ρ)·(∇S) - ℏ/(2m) · √ρ ∇²S                             (18)
```

Multiply by `2√ρ/ℏ`:

```
2√ρ (∂_t √ρ) = -1/m · [2√ρ (∇√ρ)·(∇S) + ρ ∇²S]
```

Use `2√ρ ∂_t √ρ = ∂_t ρ` and `2√ρ ∇√ρ = ∇ρ`:

```
∂_t ρ + 1/m · [(∇ρ)·(∇S) + ρ ∇²S] = 0
∂_t ρ + 1/m · ∇·(ρ ∇S) = 0                                                    (19)
```

Define superfluid velocity **v_s = ∇S/m**:

```
∂_t ρ + ∇·(ρ v_s) = 0                                                          (20)
```

**(20) is the continuity equation.** Matter flow at rate `j = ρ v_s` conserves total ρ.

### 5.5 Summary of the Madelung form

Schrödinger (12) ↔ the pair:

- **Continuity:** `∂_t ρ + ∇·(ρ v_s) = 0` with `v_s = ∇S/m`.
- **Hamilton-Jacobi + quantum pressure:** `∂_t S + |∇S|²/(2m) + V + Q = 0` with `Q = -ℏ²/(2m) · ∇²√ρ / √ρ`.

**Status: FORCED** given Schrödinger (12). This is a mathematical identity (the Madelung transformation, 1927).

---

## 6. Consistency check: canonical ED PDE at D = 0

### 6.1 The canonical ED PDE

From `theory/D_crit_Resolution_Memo.md §2`:

```
∂_t ρ = D · F[ρ] + H · v                                                       (21a)
∂_t v = (F[ρ] − ζ · v) / τ                                                     (21b)
F[ρ] = M(ρ) ∇²ρ + M'(ρ) |∇ρ|² − P(ρ)                                          (21c)
```

with D + H = 1. The BEC platform bridge (`bec_pde_mapping.md §5.3`) established that at the collective-mode scale, D = 0 (pure participation) and ζ = 1/Q_m.

### 6.2 At D = 0, H = 1

```
∂_t ρ = v                                                                      (22a)
∂_t v = (F[ρ] − ζ · v) / τ                                                     (22b)
```

In the isolated-chain limit (no dissipation: ζ → 0, or sufficiently slow that 1/τ dissipative term is subdominant):

```
τ ∂²_t ρ = F[ρ]                                                                (23)
```

### 6.3 Matching to Madelung's (20) and (17)

**Here is the structural subtlety:** (20) and (17) are equations for ρ(x, t) and S(x, t) (two real fields). (22a–b) are equations for ρ(x, t) and v(x, t) (two real fields). The correspondence requires:

**v_ED ↔ ?** From `bec_pde_mapping.md §2.2`, v_ED is the phase field φ = S/ℏ (Candidate A). Under this identification, (22a) says:

```
∂_t ρ = φ                                                                      (24)
```

But Madelung's continuity (20) says `∂_t ρ = -∇·(ρ ∇S/m) = -(ℏ/m) ∇·(ρ ∇φ)`. These don't match: (24) is local (∂_t ρ at a point equals φ at the same point, no gradients); Madelung is non-local (∂_t ρ depends on spatial gradients of ρ and φ).

**This is a structural mismatch.** The canonical ED PDE at D = 0 does NOT reduce exactly to Madelung's continuity equation under the Candidate A identification.

### 6.4 Resolution candidates

**Candidate R1:** the canonical ED PDE is a mode-reduced equation (per `sc_qubit_pde_mapping.md §2.1` Option A) in which ρ and v are mode amplitudes, not spatial fields. The spatial structure is carried by mode eigenfunctions. Under this reading, (22a–b) give the amplitude dynamics of each mode; (20) and (17) give the spatial dynamics of the full wavefunction. They operate at different levels and don't need to match pointwise.

**Candidate R2:** v_ED ↔ -∇·(ρ ∇S/m)/ρ (a composite identification rather than v_ED ↔ φ). Under this, (22a) ∂_t ρ = v_ED = -∇·(ρ∇S)/m·(1/ρ)·ρ = -∇·(ρ∇S/m), matching Madelung. But this is a strained identification requiring further justification.

**Candidate R3:** the canonical ED PDE at D = 0 is NOT the direct spatial reduction of the participation-measure Schrödinger dynamics; it is an effective mode-by-mode equation valid after mode decomposition. The Schrödinger equation operates at the coherent-sum Ψ level; the canonical ED PDE operates at the mode-amplitude level post-decomposition.

**Adopted interpretation: R3.** The canonical ED PDE is the ED-effective-PDE — a mode-reduced description. The participation-measure evolution (1) is the fundamental complex-valued equation; (12) Schrödinger is its thin-limit. The canonical ED PDE is a distinct but consistent description at the mode-amplitude level.

### 6.5 Consistency claim (CANDIDATE)

**The canonical ED PDE at D = 0 is structurally CONSISTENT with Schrödinger in the following sense:**

- At the mode-amplitude level: each mode amplitude `a_m(t)` satisfies `τ ä_m + ζ ȧ_m + ω_m² a_m = 0` (damped harmonic oscillator) under (21–23). This is the classical harmonic oscillator for the mode.
- Quantum mechanically: the same mode is an excitation of a Schrödinger-Hamiltonian with mode frequency ω_m. Expectation values of the mode amplitude satisfy the classical equations (Ehrenfest); the canonical ED PDE captures these expectation-value dynamics.

**Status: CANDIDATE.** The canonical ED PDE describes the classical (expectation-value-level) dynamics of modes; the participation-measure Schrödinger describes the quantum (amplitude-level) dynamics. They are consistent but operate at different levels.

### 6.6 Honest disclosure

The matching between the canonical ED PDE and Schrödinger via Madelung is **consistency at the mode-amplitude level, not a pointwise PDE identity.** The user's requirement ("Show that the ED PDE in the D = 0 regime reduces to the same pair of equations obtained from Madelung") is NOT satisfied in the strong pointwise sense under Candidate A's v_ED ↔ φ identification. It is satisfied in the weaker mode-amplitude sense under interpretation R3.

This is a real structural finding: the canonical ED PDE and the participation-measure Schrödinger dynamics operate at different levels of description. Both are internally consistent with BEC physics (per the platform bridge), but they are not a direct pointwise reduction of one to the other.

---

## 7. Summary of the derivation

**Starting from:** the participation-measure evolution (1), `iℏ ∂_t P_K = H_K P_K + Σ_{K'} V_{KK'} P_{K'}`.

**Under the thin-participation limit (§2):** M_eff → ∞, channel label K → k (momentum, CANDIDATE), environmental/commitment bands suppressed.

**Coherent-sum evolution (§4):** the wavefunction Ψ(x, t) = ∫ dk P_k(x, t) satisfies the linear Schrödinger equation:

```
iℏ ∂_t Ψ = [-ℏ²/(2m) ∇² + V(x)] Ψ                                              (12)
```

**Madelung transformation (§5):** writing Ψ = √ρ · e^{iS/ℏ}, (12) splits into:

- **Continuity:** `∂_t ρ + ∇·(ρ v_s) = 0`, `v_s = ∇S/m`.
- **Hamilton-Jacobi + quantum pressure:** `∂_t S + |∇S|²/(2m) + V + Q = 0`, `Q = -ℏ²/(2m) ∇²√ρ / √ρ`.

**Consistency check (§6):** the canonical ED PDE at D = 0 describes classical mode-amplitude dynamics and is CONSISTENT with the Schrödinger coherent-sum dynamics at the expectation-value level. The two descriptions operate at different levels; they are not a pointwise PDE reduction.

**Result: ED participation dynamics (thin limit) = Schrödinger equation.**

---

## 8. Status classification

| Derivation element | Status |
|---|---|
| Participation-measure evolution form (1) | **CANDIDATE** (from participation_measure.md) |
| Thin-limit definition §2 | **FORCED** by primitive-level characterization |
| K ↔ k momentum identification | **CANDIDATE** (simplest; alternatives give same Schrödinger after basis change) |
| H_k = ℏ²k²/(2m) free kinetic form | **CANDIDATE** (requires thin-limit plane-wave mode structure) |
| V_{kk'} = ⟨k\|V̂\|k'⟩ potential matrix | FORCED given basis choice |
| Linearity of Ψ evolution under (1) | FORCED by linearity of (1) |
| Schrödinger equation (12) | **CANDIDATE** (inherits from K identification + H_k form) |
| Madelung split into (continuity, Hamilton-Jacobi+Q) | **FORCED** given Schrödinger (12) |
| ρ, v_s identifications | FORCED by Madelung |
| Quantum potential Q form | FORCED |
| Canonical ED PDE pointwise = Madelung | **NOT FORCED** (structural mismatch identified §6.3) |
| Canonical ED PDE mode-level = Madelung | CANDIDATE (consistent at mode-amplitude level under interpretation R3) |

**Net: Schrödinger emergence is established at CANDIDATE level conditional on the three CANDIDATE identifications (K↔k, H_k free kinetic, P-evolution form). Madelung equivalence is FORCED given Schrödinger.**

---

## 9. What this memo achieves and does not achieve

### 9.1 Achieved

- Derivation of Schrödinger from the participation-measure evolution under CANDIDATE identifications.
- Explicit Madelung transformation giving the real-valued (ρ, S) form of QM.
- Identification of the structural subtlety in matching the canonical ED PDE to Madelung pointwise (§6.3).
- Status classification with explicit FORCED / CANDIDATE labels for each step.
- Step-2 scaffolding for Steps 3–5: the participation-measure → Schrödinger bridge is now in place.

### 9.2 Not achieved

- No derivation from ED primitives that **forces** the specific form (1) of the participation-measure evolution. (1) is adopted provisionally.
- No derivation that **forces** H_k to be the free-particle kinetic form. The plane-wave-like thin-limit mode structure is CANDIDATE.
- No pointwise reduction of the canonical ED PDE to Madelung under v_ED ↔ φ. The match works at the mode-amplitude level only.
- No treatment of relativistic corrections, spin, or multi-particle extensions (these are beyond Step-2 scope).
- No derivation of the specific value of ℏ in terms of ED primitives. ℏ appears in (1) as an external parameter; a derivation of ℏ from ED structural constants is deferred to later work.

### 9.3 Honest framing

**The thin-limit of the participation-measure dynamics is Schrödinger under CANDIDATE identifications (K↔k, H_k free, V_{kk'} potential).** Once those identifications are made, the derivation is straightforward and the Madelung equivalence is exact.

**What is genuinely from ED:** the structural claim that Ψ = Σ_K P_K is the natural coherent-sum object in the thin limit, and that this object satisfies a linear first-order-in-time complex evolution equation. The fact that this evolution is Schrödinger (with free kinetic + potential Hamiltonian) is an additional CANDIDATE identification, not a derivation from ED primitives.

**What is not genuinely derived:** why the Hamiltonian takes the specific form -ℏ²/(2m)∇² + V, why m appears where it does, and why ℏ is the specific constant it is. These are inherited from QM's own structure, not derived from ED.

**Step-2 status: COMPLETE at CANDIDATE level.** Steps 3–5 now have the participation-measure → Schrödinger bridge available as scaffolding.

---

## 10. Open items for refinement

1. **Derive (1) from ED primitives.** The form `iℏ ∂_t P_K = H_K P_K + Σ_{K'} V_{KK'} P_{K'}` was adopted in participation_measure.md as CANDIDATE. A derivation from primitives + canonical PDE that forces this form would tighten the Schrödinger emergence.

2. **Derive the Hamiltonian structure.** Why `H_K = ℏ²k²/(2m)` in the thin-limit momentum basis? A primitive-level argument would promote this from CANDIDATE to FORCED.

3. **Resolve the canonical-PDE / Madelung mismatch.** Either the v_ED identification is wrong, or the canonical PDE is inherently mode-amplitude-level (not spatial). Current best interpretation: mode-amplitude-level (R3). Needs explicit derivation.

4. **Address the origin of ℏ.** In (1), ℏ is an external constant. Dimensional Atlas anchors it in the quantum regime via D_phys = ℏ/(2m); an ED-primitive-level origin for ℏ itself is deferred.

5. **Relativistic extension.** The current derivation is non-relativistic Schrödinger. A relativistic extension (Klein-Gordon, Dirac) would require careful treatment of the participation-measure covariance properties.

---

## 11. Cross-references

- Step 1 participation-measure definition: [`quantum/foundations/participation_measure.md`](participation_measure.md)
- Primitive 04 (participation bandwidth): [`quantum/primitives/04_participation_bandwidth.md`](../primitives/04_participation_bandwidth.md)
- Primitive 08 (multiplicity; thin-limit M_eff): [`quantum/primitives/08_multiplicity.md`](../primitives/08_multiplicity.md)
- Primitive 09 (tension polarity; phase component of P): [`quantum/primitives/09_tension_polarity.md`](../primitives/09_tension_polarity.md)
- Primitive 10 (individuation; isolated-system regime): [`quantum/primitives/10_individuation.md`](../primitives/10_individuation.md)
- Canonical ED PDE (D_crit resolution): [`theory/D_crit_Resolution_Memo.md`](../../theory/D_crit_Resolution_Memo.md)
- BEC platform bridge (D = 0 pure-participation; Madelung consistency check): [`quantum/effective_theory/bec_pde_mapping.md`](../effective_theory/bec_pde_mapping.md)
- Dimensional Atlas (Madelung anchoring ρ ↔ \|ψ\|², D_phys = ℏ/2m): [`papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md`](../../papers/Dimensional_Atlas/regimes/ED-Dimensional-01_Quantum_Regime.md)
- Madelung 1927 original derivation (classical reference): Z. Phys. 40, 322.

---

## 12. One-line summary

> **Under the thin-participation limit (M_eff → ∞, K → k momentum, environmental band suppressed), the participation-measure evolution `iℏ ∂_t P_K = H_K P_K + Σ_{K'} V_{KK'} P_{K'}` applied to the coherent sum Ψ = Σ_K P_K yields the standard linear Schrödinger equation `iℏ ∂_t Ψ = [-ℏ²/(2m) ∇² + V] Ψ`. Madelung transformation Ψ = √ρ · e^{iS/ℏ} splits this into the continuity equation ∂_t ρ + ∇·(ρ v_s) = 0 and the Hamilton-Jacobi equation with quantum-pressure correction ∂_t S + \|∇S\|²/(2m) + V + Q = 0 (Q = -ℏ²/2m · ∇²√ρ/√ρ). Step 2 complete at CANDIDATE level; three structural identifications remain CANDIDATE (P-evolution form, K↔k, H_k free kinetic); the canonical ED PDE at D = 0 is CONSISTENT at the mode-amplitude level but does not reduce to Madelung pointwise. Steps 3–5 are unblocked.**
