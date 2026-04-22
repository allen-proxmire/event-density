# ED Reversible-Sector QFT — Canonical Quantisation and ED-10 Interpretation

**Date.** 2026-04-22.
**Scope.** Working memo, not a scoping pass. Derive, within the strictly reversible slice `D = 0, ζ = 0` of the canonical ED PDE, the corresponding free-scalar quantum field theory, and make explicit how ED-10's "Schrödinger = thin-regime participation dynamics" is cashed out.
**Status.** The calculation is standard; the *interpretation* is the load-bearing contribution. The memo delivers (i) the explicit Hamiltonian structure, (ii) the Fock-space construction, (iii) the Schrödinger-picture evolution, (iv) a clean statement of what ED-10 can and cannot claim on the strength of this result. The reversible slice is a measure-zero boundary of ED's parameter space, so this is a **consistency** result between ED and standard QFT, not a derivation of QM from ED axioms.

---

## 1. Problem Statement

### 1A. The reversible slice, defined precisely

The canonical ED system (`theory/PDE.md` §1):

$$
\partial_t\rho = D\bigl[M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)\bigr] + H v,
\qquad
\tau\,\partial_t v = F[\rho] - \zeta v,
$$

with `H = 1 − D`. The **reversible slice** is the parameter point

$$
D = 0, \qquad \zeta = 0, \qquad \tau = 1, \qquad P_0 > 0, \qquad M_0 > 0,
$$

equivalently, `H = 1` and no damping in the participation channel. In this slice:

- The direct channel `D·F[ρ]` vanishes.
- The participation channel carries all dynamics through `H·v = v`.
- The participation ODE becomes conservative: `∂_t v = F[ρ]` with no decay.

This is the minimal non-dissipative sub-sector of Canon P2+P5.

### 1B. Goal of this memo

- Linearise ED on this slice and identify the harmonic-oscillator-per-mode structure.
- Write the Hamiltonian, identify canonical conjugates.
- Canonically quantise; construct Fock space.
- Recover Schrödinger-picture evolution for wavefunctions.
- Connect to ED-10's identification "Schrödinger = thin-regime participation dynamics."
- State limitations: free real scalar, no gauge, no charge, no spin, no interactions.

### 1C. What this does and does not show

- **Does show.** In the reversible slice, linearised ED is a free massive real scalar field, and its standard canonical quantisation gives Schrödinger-type wavefunction evolution under a free Hamiltonian. ED-10's identification is consistent with this, at the level of free-field QFT.
- **Does not show.** That quantum mechanics is *derived* from ED axioms (we are applying standard quantisation, not deriving it). That interactions, gauge structure, charge, or SM-like matter content emerge (they do not, in the linear free-scalar sector). That the reversible slice describes physical ED systems (it does not — physical ED is dissipative, `D > 0, ζ > 0`).

---

## 2. Reversible-Limit PDE and Linearisation

### 2A. Reduced system

Setting `D = 0, ζ = 0, τ = 1` in the canonical system:

$$
\partial_t\rho = v, \qquad
\partial_t v = F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho).
$$

Equivalently, a single second-order equation for `ρ`:

$$
\partial_t^2 \rho = F[\rho] = M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho).
$$

### 2B. Linearisation around the equilibrium

Expand `ρ = ρ^* + \varphi(x,t)`, `v = \pi(x,t)` (renaming `δρ → φ` and `δv → π` to align with standard QFT notation). At linear order, with `M_0 ≡ M(ρ^*), P_0 ≡ P'(ρ^*), P(ρ^*) = 0`:

$$
\partial_t \varphi = \pi,
\qquad
\partial_t \pi = M_0 \nabla^2\varphi - P_0 \varphi.
$$

Equivalently:

$$
\boxed{\;\; \partial_t^2 \varphi - M_0 \nabla^2 \varphi + P_0 \varphi = 0. \;\;}
$$

This is a **massive Klein-Gordon equation** in non-relativistic form, with sound speed² `= M_0` and mass² `= P_0`. The system is fully conservative at linear order — no damping term.

### 2C. Fourier decomposition

Let `φ(x,t) = V^{−1/2} Σ_k \tilde\varphi_k(t) e^{ik·x}` with discrete `k` in a box of volume `V` (IR regulator) for definiteness; continuum limit `V → ∞` is standard. Then per mode `k`:

$$
\partial_t \tilde\varphi_k = \tilde\pi_k,
\qquad
\partial_t \tilde\pi_k = -\Omega^2(k)\,\tilde\varphi_k,
\qquad
\Omega^2(k) \equiv P_0 + M_0 k^2.
$$

Every Fourier mode is a **classical harmonic oscillator** with frequency `Ω(k) = √(P_0 + M_0 k²)`.

Reality of `φ` imposes `\tilde\varphi_{-k} = \tilde\varphi_k^*`, likewise for `\tilde\pi_k`.

### 2D. Dispersion relation

$$
\Omega(k) = \sqrt{P_0 + M_0 k^2}.
$$

- IR (`k → 0`): `Ω(0) = √P_0` — gapped mode of frequency `√P_0` (mass).
- UV (`k → ∞`): `Ω(k) → √M_0 · k` — linear dispersion with sound speed `c_s = √M_0`.

This is the non-relativistic form of a massive KG dispersion; `c_s` is ED's signal speed in the reversible limit (see `theory/ED-Dimensional-01-Ext.md` for the comparison to the dictionary's `c_0 = L_0/T_0`).

---

## 3. Mode Decomposition and Harmonic-Oscillator Structure

### 3A. Hamiltonian form

The linearised classical system admits a Hamiltonian. Choose canonical coordinate `q(x) ≡ φ(x)` and conjugate momentum `p(x) ≡ π(x)`. The classical Hamiltonian is

$$
H_{\rm cl} = \int d^dx \left[\frac{1}{2}\pi(x)^2 + \frac{1}{2} M_0 |\nabla\varphi(x)|^2 + \frac{1}{2} P_0\,\varphi(x)^2\right].
$$

Check Hamilton's equations:
- `∂_t φ = δH/δπ = π` ✓ (matches §2B)
- `∂_t π = −δH/δφ = M_0 ∇²φ − P_0 φ` ✓ (matches §2B)

### 3B. Hamiltonian in Fourier modes

Substitute the Fourier expansion. Using the reality condition and the usual inner-product identity `\int d^dx e^{i(k-k')x} = V \delta_{k,k'}`:

$$
H_{\rm cl} = \sum_k \left[\frac{1}{2}|\tilde\pi_k|^2 + \frac{1}{2}\Omega^2(k)\,|\tilde\varphi_k|^2\right].
$$

For each unordered pair `{k, −k}`, this is two copies of a standard harmonic oscillator (real and imaginary parts of `\tilde\varphi_k`). Equivalently, using real canonical variables (`q_k = √2 Re \tilde\varphi_k`, `p_k = √2 Re \tilde\pi_k` and similarly for imaginary parts, summed only over half the Brillouin zone), we can write

$$
H_{\rm cl} = \sum_{k}\left[\frac{1}{2}p_k^2 + \frac{1}{2}\Omega^2(k)\,q_k^2\right],
$$

summed over a full independent real set of modes. This is explicitly a **sum of decoupled classical harmonic oscillators**, one per mode.

### 3C. Canonical Poisson brackets

Classical: `{φ(x), π(y)} = δ^d(x − y)`; in Fourier modes, `{q_k, p_{k'}} = δ_{k,k'}`, all other brackets vanish.

---

## 4. Canonical Quantisation and Fock Space

### 4A. Promotion to operators

Quantise by promoting `φ, π` to Hermitian field operators `\hat\varphi(x), \hat\pi(x)` with equal-time commutators

$$
[\hat\varphi(x), \hat\pi(y)] = i\hbar\,\delta^d(x-y),
\qquad
[\hat\varphi(x),\hat\varphi(y)] = [\hat\pi(x),\hat\pi(y)] = 0.
$$

Per Fourier mode: `[\hat q_k, \hat p_{k'}] = i\hbar\,\delta_{k,k'}`.

### 4B. Creation / annihilation operators

Define, for each mode,

$$
\hat a_k = \frac{1}{\sqrt{2\hbar\Omega(k)}}\bigl(\Omega(k)\,\hat q_k + i\,\hat p_k\bigr),
\qquad
\hat a_k^\dagger = \frac{1}{\sqrt{2\hbar\Omega(k)}}\bigl(\Omega(k)\,\hat q_k - i\,\hat p_k\bigr).
$$

Then `[\hat a_k, \hat a_{k'}^\dagger] = \delta_{k,k'}`, all other commutators zero. The mode Hamiltonian becomes

$$
\hat H_k = \hbar\Omega(k)\left(\hat a_k^\dagger \hat a_k + \tfrac{1}{2}\right),
$$

and the total Hamiltonian

$$
\boxed{\;\; \hat H = \sum_k \hbar\Omega(k)\left(\hat a_k^\dagger \hat a_k + \tfrac{1}{2}\right). \;\;}
$$

(The zero-point sum is formally divergent; standard normal-ordering drops it for the free theory.)

### 4C. Fock space

Vacuum: `\hat a_k |0\rangle = 0` for all `k`. Number states:

$$
|n_{k_1}, n_{k_2}, \dots\rangle = \prod_i \frac{(\hat a_{k_i}^\dagger)^{n_{k_i}}}{\sqrt{n_{k_i}!}}\,|0\rangle,
\qquad
\hat N_k\,|n_k\rangle = n_k |n_k\rangle \text{ per mode}.
$$

Full Hilbert space: `ℋ = ⊗_k ℋ_k` where each `ℋ_k` is the infinite-dimensional oscillator Hilbert space. Standard Fock-space construction for a free real scalar.

### 4D. Field operator

$$
\hat\varphi(x,t) = \sum_k \frac{1}{\sqrt{2V\,\Omega(k)/\hbar}}\left[\hat a_k\,e^{i(k\cdot x - \Omega(k)t)} + \hat a_k^\dagger\,e^{-i(k\cdot x - \Omega(k)t)}\right].
$$

It satisfies the Heisenberg equation `iℏ\,\partial_t\hat\varphi = [\hat\varphi, \hat H]`, which reproduces `(∂_t^2 − M_0 ∇^2 + P_0)\hat\varphi = 0` — the quantised Klein-Gordon equation.

### 4E. Number operator and its status

Total number operator `\hat N = \sum_k \hat N_k = \sum_k \hat a_k^\dagger \hat a_k`. Key facts:

- **`[\hat N, \hat H] = 0`.** Each `N_k` commutes with each `H_{k'}` (free theory, no mode coupling). So `N` is a conserved operator of the free theory.
- **No Noether U(1) of the classical field.** The classical Lagrangian `L = (1/2)(\partial_t\varphi)^2 − (1/2)M_0|\nabla\varphi|^2 − (1/2)P_0\varphi^2` is a real scalar theory. It has no internal U(1) symmetry; there is no classical Noether charge corresponding to `\hat N`.
- **`\hat N` is a quantum-side bookkeeping operator.** It counts Fock-space quanta; its conservation reflects the free-theory decoupling of modes (i.e., each `N_k` is separately conserved), not a symmetry principle that survives interactions.
- **Once interactions are added** (higher-order terms from `M(ρ), P(ρ)`, or the P7 triad `M'|\nabla ρ|^2`), `N` stops commuting with `H` — e.g., the `φ³`-type term from expanding `M(ρ)` creates particle production/absorption.

**This is the correct statement of "U(1) = oscillator number" from the prior memo (`Emergent_U1_in_ED_Scoping.md` §4):** it is a Fock-space operator conservation in the free theory, not a gauge symmetry and not a Noether symmetry of the underlying real-scalar field theory.

---

## 5. Schrödinger Evolution and ED-10 Interpretation

### 5A. Schrödinger picture

States `|\Psi(t)\rangle` evolve by

$$
i\hbar\,\partial_t |\Psi(t)\rangle = \hat H\,|\Psi(t)\rangle,
\qquad
|\Psi(t)\rangle = e^{-i\hat H t/\hbar}\,|\Psi(0)\rangle.
$$

This is the standard Schrödinger equation with Hamiltonian `\hat H` of §4B.

### 5B. Single-mode reduction

Restrict to a single Fourier mode `k` (e.g., a standing wave in a cavity, or a single-mode approximation in a trap). The mode Hilbert space is the standard quantum harmonic oscillator (QHO). In the position representation, the wavefunction `\psi_k(q_k, t)` satisfies

$$
i\hbar\,\partial_t\psi_k(q_k, t) = \left[-\frac{\hbar^2}{2}\,\partial_{q_k}^2 + \frac{1}{2}\Omega^2(k)\,q_k^2\right]\psi_k(q_k, t).
$$

This is precisely the Schrödinger equation for a particle in a harmonic potential with frequency `Ω(k)`. Its eigenstates are Hermite-Gauss functions; its dynamics are standard.

### 5C. Multi-mode Schrödinger equation

For the full theory, the wavefunctional `\Psi[\varphi, t]` on configuration space `\{\varphi(x)\}` satisfies

$$
i\hbar\,\partial_t\Psi[\varphi, t] = \int d^dx\left[-\frac{\hbar^2}{2}\frac{\delta^2}{\delta\varphi(x)^2} + \frac{1}{2}M_0|\nabla\varphi|^2 + \frac{1}{2}P_0\varphi^2\right]\Psi[\varphi, t].
$$

This is the Schrödinger-functional form of the free scalar QFT. It factorises across Fourier modes into the product `\Psi = \prod_k \psi_k(q_k, t)`.

### 5D. The ED-10 identification

ED-10 ("Schrödinger = thin-regime participation dynamics") is now cashed out as:

> **ED-10 (explicit form).** In the reversible slice of ED (`D = 0, ζ = 0, H = 1`), the linearised dynamics of `(δρ, δv)` is a free classical real scalar field whose Fourier modes are harmonic oscillators with frequency `Ω(k) = √(P_0 + M_0 k²)`. Canonical quantisation gives a free scalar QFT, with standard Schrödinger-picture evolution for state vectors (§5A) and a single-mode Schrödinger equation (§5B) for wavefunctions in the position representation. The mapping to ED primitives is:
>
> - **Canonical coordinate `q(x)` ↔ ED fluctuation `δρ(x)`** — event-density departure from equilibrium.
> - **Conjugate momentum `p(x)` ↔ ED participation fluctuation `δv(x)`** — rate of change of density.
> - **Mode frequency `Ω(k)` ↔ ED reversible-sector dispersion** `√(P_0 + M_0 k²)`.
> - **Quantum `a_k^\dagger|0\rangle` ↔ one participation quantum of mode `k`** — a localised oscillator excitation in the thin-regime ED sector.

### 5E. Where the identification is tight, where it is loose

- **Tight.** The mathematical statement (linearised reversible ED + canonical quantisation = free scalar QFT with Schrödinger evolution) is textbook and correct.
- **Tight.** The identification of `δv` as canonical momentum conjugate to `δρ` is forced by Hamilton's equations and is unambiguous in the reversible slice.
- **Loose.** The name "Schrödinger" in standard QM usually refers to a *non-relativistic* particle Schrödinger equation, not the Schrödinger-picture evolution of a QFT state. ED-10 is making the latter (field-theoretic) statement, which is trivially true for any free-scalar QFT. **The content of ED-10 is therefore weaker than "ED explains non-relativistic quantum mechanics" — it is the consistency statement "ED's reversible sector admits standard canonical quantisation."**
- **Loose.** The reversible slice is measure zero in the `(D, ζ)` parameter space. Physical ED systems are dissipative (`D > 0` or `ζ > 0`). So the QFT structure here describes a boundary limit, not a generic ED regime. ED-10 should not be read as "all of ED is quantum mechanical" — it is "the reversible limit of ED has the structure of a free scalar QFT."

### 5F. What would be needed to strengthen ED-10

To promote the identification from "consistency" to "derivation" (in the sense of "ED forces QM"), one would need to show:

- Interactions from `M(ρ), P(ρ), M'|\nabla ρ|^2` expanded to higher order preserve unitarity when quantised — **open**; non-trivial for nonlinear scalar theories but standard in the perturbative sense.
- The dissipative sector (`D > 0, ζ > 0`) admits a sensible quantisation — **hard**; dissipative systems require open-system or Schwinger-Keldysh machinery and do not trivially give unitary QM.
- ED's canonical PDE, rather than being quantised by hand, *implies* the quantisation rule (e.g., `[\hat\varphi, \hat\pi] = i\hbar\delta`) from an internal axiom — **not currently in Canon**; `ℏ` enters only through ED-Dimensional-01 as a matching scale.

None of these is in scope for this memo; all are flagged honestly in §7.

---

## 6. Limitations

Explicit list of what this construction does **not** produce:

### 6A. No gauge fields

No vector potential `A_μ`, no field strength `F_{μν}`, no gauge transformation. The theory is a pure real scalar. (See `theory/Emergent_U1_in_ED_Scoping.md` §6–§7.)

### 6B. No charge

No conserved Noether current of any internal U(1). The number operator `\hat N` is a Fock-space bookkeeping operator, not a classical Noether charge. Real scalar fields have no charge.

### 6C. No spin

The field is a scalar (spin 0). No spinors, no Dirac structure, no vector modes. Spin would require additional field content that Canon does not supply.

### 6D. No interactions (at the linear level)

This is a **free** QFT. The P7 triad term `M'(ρ)|\nabla\rho|^2` and higher-order expansions of `P(ρ)` would supply interaction vertices, but:
- At linear order (this memo), they are absent.
- At quadratic order (φ² in the potential), they shift the mass `P_0` — still free.
- At cubic and higher order, they generate interaction vertices; quantisation then requires the full apparatus of perturbative scalar QFT and is a separate project.

### 6E. Free scalar is a boundary limit

`(D, ζ) = (0, 0)` is one point of a parameter space. Moving into the generic underdamped sector (`D > 0, ζ > 0`, still underdamped) adds dissipation, which breaks the Hamiltonian structure and invalidates the canonical-quantisation procedure in the form used here. Quantising dissipative ED would require the Schwinger-Keldysh or Lindblad machinery — a different memo, a different formalism.

### 6F. No claim about `ℏ`

The commutator `[\hat\varphi, \hat\pi] = i\hbar\,\delta` introduces `ℏ` as an external scale. ED does not internally produce `ℏ`; it matches to `ℏ` through the ED-Dimensional-01 dictionary (`L_0 = ℏ/(mc)`, etc.). This memo does not advance the question "where does `ℏ` come from in ED?" — that is an independent question, not scoped here.

### 6G. No `α`, no SM structure, no mass ratios

Explicitly reaffirming the prior scopings (`theory/Fine_Structure_Constant_Scoping.md`, `theory/Species_Mass_Spectrum_Scoping.md`): nothing in this construction produces `α`, species-mass ratios, gauge couplings, or any SM-like content.

---

## 7. Assessment

### 7A. What ED-10 can honestly claim on the strength of this result

- **(Tight)** "In the reversible slice of ED, linearised dynamics is a free real scalar field theory. Canonical quantisation yields the standard Schrödinger-picture evolution of a free scalar QFT. The `(δρ, δv)` pair maps to canonical `(q, p)` at each Fourier mode."
- **(Tight)** "Each Fourier mode of the quantised field is a quantum harmonic oscillator with frequency `Ω(k) = √(P_0 + M_0 k²)`; the wavefunction of each mode satisfies the QHO Schrödinger equation."
- **(Tight)** "The total number operator `\hat N = Σ_k \hat N_k` commutes with the free Hamiltonian and is a conserved bookkeeping quantity, but it is not a Noether charge of a classical symmetry — it is a Fock-space operator."

### 7B. What ED-10 cannot claim

- **(Cannot claim)** "ED derives quantum mechanics." We applied standard quantisation to a classical system; the content is a *consistency*, not a derivation.
- **(Cannot claim)** "ED has an emergent gauge symmetry" or "ED has charge." Neither appears in the free-scalar theory.
- **(Cannot claim)** "Schrödinger's equation for a particle in a potential emerges from ED." What emerges is the Schrödinger-picture evolution of a scalar QFT state, which is structurally different from the single-particle Schrödinger equation used in chemistry and atomic physics.
- **(Cannot claim)** "The full ED is quantum." The QFT structure holds only on the measure-zero reversible slice; generic ED is dissipative and does not admit this form of quantisation without additional machinery.

### 7C. Suggested ED-10 language (for repo-wide use)

Replace the current ED-10 line

> "Schrödinger evolution = thin-regime participation dynamics."

with

> **"In the reversible (thin-regime) sector of ED (`D = 0, ζ = 0, H = 1`), linearised dynamics is a free real scalar field theory whose Fourier modes are classical harmonic oscillators of frequency `Ω(k) = √(P_0 + M_0 k²)`. Canonical quantisation produces a free scalar QFT with standard Schrödinger-picture evolution; single Fourier modes obey the quantum-harmonic-oscillator Schrödinger equation. This is a consistency result between ED's reversible sector and standard QFT, not a derivation of quantum mechanics from ED axioms. ED's primitive `δρ` maps to the canonical coordinate; `δv` maps to the conjugate momentum; a participation quantum is a Fock-space excitation of mode `k`."**

This:
- Preserves ED-10's conceptual direction (reversible sector ↔ QM).
- Removes the overclaim that Schrödinger *per se* is derived.
- Is consistent with the structural obstacles identified in `Fine_Structure_Constant_Scoping.md` and `Emergent_U1_in_ED_Scoping.md`.
- Is robust to the Canon P6 correction (D_crit ≈ 0.896, `D_crit_Resolution_Memo.md`) because the reversible slice lies at `D = 0`, below `D_crit`.

### 7D. Status in the repo

- ED-10 stays in the Interpretations stratum (not a tested prediction).
- This memo supplies the explicit structural backing for the ED-10 identification in the reversible slice.
- No updates to Canon. No new axioms. No new predictions.
- Future work: Follow-ups 2–3 of `Emergent_U1_in_ED_Scoping.md §8D` and the interaction-order extension (nonlinear scalar QFT from P7) remain open but not prioritised.

### 7E. Sanity checks against existing ED material

- `theory/Architectural_Canon.md §6`: the ontology dictionary already includes "Schrödinger evolution = thin-regime participation dynamics" as a consequence of coarse-grained behaviour. This memo provides the explicit construction underlying that statement.
- `theory/ED-Dimensional-01-Ext.md`: `L_0 = ℏ/(mc), T_0 = 0.6 ℏ/(mc^2)` gives a `c_0 = L_0/T_0 = c/0.6`. In this memo's reversible slice, the emergent signal speed is `c_s = √M_0`, set by the mobility at equilibrium. Identifying `c_s` with `c_0` pins `M_0 = (c/0.6)^2 = c^2/0.36` in physical units. **This is a new structural identification worth flagging:** the dictionary's `c_0` is the free-field sound speed of the reversible-slice QFT. It is an algebraic consequence of the dictionary, not a new prediction; but it makes the `c_0 ≠ c` fact sharp and specific rather than vague.
- `theory/Universal_Invariants.md`: the oscillator-sector invariants `Q ≈ 3.5, N_{\rm osc} ≈ 9` are generic-underdamped-regime statements (`D > 0, ζ > 0`). They do not apply to this memo's `(D, ζ) = (0, 0)` slice, where `Q → ∞` (no damping) and oscillations persist indefinitely. No conflict.

---

## 8. Related Memos

- `theory/Architectural_Canon.md` — Canon P1–P7; §6 for the ED-10 ontology dictionary.
- `theory/PDE.md` — canonical PDE and primitives.
- `theory/Emergent_U1_in_ED_Scoping.md` — prior memo; §4E analysed the same `(D, ζ) = (0, 0)` slice and showed conservation of `|ψ|²`; this memo supplies the full QFT extension.
- `theory/Fine_Structure_Constant_Scoping.md` — prior scoping; complementary, establishes that no gauge structure arises from this construction.
- `theory/ED_Geometry_Emergence_Scoping.md` — prior scoping; the analogue-gravity structure in §3A uses the same linearisation; see for cross-reference.
- `theory/D_crit_Resolution_Memo.md` — the reversible slice lies deep in the oscillatory regime (`D = 0 < D_{\rm crit} ≈ 0.896`), so Canon P6's corrected threshold is comfortably respected.
- `theory/ED-Dimensional-01-Ext.md` — dictionary; §7E suggests a tight identification of `c_0` with the free-field sound speed `c_s = √M_0`.

---

**Status.** Working memo. Result is standard free-scalar QFT applied to the reversible slice of ED; the ED-specific content is the interpretation (§5D, §7A–7C). No new axioms, no new predictions. Recommend adopting §7C as the updated ED-10 line in repo-wide documentation (orientation doc, canon, interpretations stratum).
