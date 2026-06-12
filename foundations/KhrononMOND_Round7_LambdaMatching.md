# Khronon–MOND — Round 7: The Λ-Matching Computation

**Foundations derivation round — performs the matching named in Round 6 / KM-II §7, to the extent it is honestly performable, and states precisely which part is not. Not a rule proposal, not a corpus edit, not a new primitive.**
**Crank rails (held, with one new discipline):** no value of Λ is derived; the matter-sector hierarchy stays where Paper_038.5 left it; and — the round's governing rule — **matching transports verdict tiers, it does not upgrade them.** A coefficient fixed by matching to a value-inherited result is itself value-inherited; moving a number between description levels cannot launder inheritance into derivation.

---

## 1. The matching condition, stated precisely

The one-Λ thesis (R6): the khronon EFT's vacuum constant is the encoding of the substrate-level V1 boundary integral. The matching condition that makes this operational is **Friedmann-level equality on the shared background**: both descriptions must produce the same expansion history, and since at this order each contributes a *constant* vacuum term, the entire content of the matching is

$$
\rho_\Lambda^{\rm EFT}(\mathcal{W}_0) \;=\; \rho_\Lambda^{\rm substrate}\big({\rm V1\ integral,\ Paper\_038.5}\big).
$$

Two consequences follow before any number is written:

1. **Double-counting is formally dissolved, not merely argued away.** Under matching, the EFT constant is *defined* by the substrate computation — there is no independent EFT vacuum term to add. R6's "category error" diagnosis becomes a procedural fact.
2. **The tier-transport rule applies.** Paper_038.5's value closes at **D-via-I** (Route A4 + Friedmann inheritance: `ρ_Λ = (3/8π)\,Ω_Λ\!\cdot$-normalized `H_0^2 M_P^2`, value-inherited). Whatever `𝒲₀` the matching produces therefore carries **exactly that tier** — fixed, but fixed *at inheritance grade*.

## 2. The scaling identity (derived)

Both faces scale as `H_0^2 c^2/G`, and structurally so:

- **Substrate face:** the integral's *domain* is the SCBU boundary (`R_H = c/H_0` — one factor of the cosmic scale per dimension of the domain normalization) and its *density* is controlled by the Route-A memory scale `ℓ_{V5}(H_0)` — the same `H_0` entering through the kernel side. The closure lands at `ρ_\Lambda \propto H_0^2 M_P^2 = H_0^2 c^2 \hbar/(G\hbar) \sim H_0^2c^2/G`.
- **EFT face:** the foliation sector's only scale is the khronon background rate; its constant term is `(c^4/16\pi G)\,(a_0^2/c^4)\,\mathcal{W}_0` with `a_0 = cH_0/2\pi`, i.e. `\rho_\Lambda^{\rm EFT} \sim \mathcal{W}_0\,H_0^2 c^2/G` up to the `2\pi`-bookkeeping of §4.

**The scaling match is exact and parameter-free**: no scale survives on either side except `H_0` and the Planck combination `c^2/G`. This was guaranteed by the shared SCBU anchor (R6 §2) and is here exhibited at the level of the two expressions themselves. [Derived.]

## 3. The sign check (derived, with one named caveat)

R6's falsifiable edge included sign. The substrate face decides it:

$$
\rho_{\rm vac, V1}(x) \;=\; \frac{1}{2}\int \frac{d^3k}{(2\pi)^3}\,\omega_k\,\big|\hat K_{V1}(k)\big|^2 \;\geq\; 0
$$

— **positive-definite by construction** (a sum of `\tfrac12\omega|K|^2` terms; Paper_038.5 §3.1). Under 038.5's stated proportionality `\Lambda \propto \int_{R_H^3} \rho_{\rm vac,V1}\,d^3x`, the substrate face yields `\Lambda > 0` — **matching the observed sign (de Sitter)**, and thereby *fixing the sign of the EFT constant*: in the `R - 2\Lambda` convention with the foliation term entering as `+(a_0^2/c^4)\mathcal{W}_0`, positivity of Λ requires `\mathcal{W}_0 < 0`. (Consistent in flavor, it may be noted without weight, with the deep-IR sector's negative constant slope — the IR Cancellation of KM-I — both foliation-sector IR constants land negative in this convention.)

**The named caveat:** §3.1's density is positive-definite, but the *full* backreaction sign in 038.5 runs through its curvature-coupling structure (its §3.2 ff., beyond the portion verified here). The sign check is therefore: **passes at the level of the vacuum-energy density and the stated proportionality; the coupling-chain confirmation is part of the ab-initio task (§5).** This could have failed at the density level and did not — a real, non-trivial consistency.

## 4. The coefficient transcription (D-via-I)

With the condition (§1), the scaling (§2), and the sign (§3), the matching fixes `\mathcal{W}_0` uniquely. Writing the EFT term as `(c^4/16\pi G)(a_0^2/c^4)\mathcal{W}_0 \equiv -(c^4/16\pi G)\,2\Lambda`, and the observed `\Lambda = 3\,\Omega_\Lambda H_0^2/c^2`:

$$
\Lambda^{\rm EFT} = -\frac{\mathcal{W}_0\,a_0^2}{2c^4} = -\frac{\mathcal{W}_0 H_0^2}{8\pi^2 c^2}
\;\;\Longrightarrow\;\;
\boxed{\;\mathcal{W}_0 \;=\; -\,24\pi^2\,\Omega_\Lambda \;\approx\; -1.6\times 10^2\;}
$$

(using `\Omega_\Lambda \approx 0.69`). The `2\pi`-bookkeeping deserves its own line: the magnitude depends on which scale the constant is written against. Against `a_0^2` (the khronon's transition scale) it is `24\pi^2\Omega_\Lambda \approx 162`; **against `(cH_0)^2` (the khronon's raw background scale) it is `6\,\Omega_\Lambda \approx 4.1` — genuinely order-unity.** The apparent largeness is the `(2\pi)^2` of Paper_029's `a_0`-definition, not a hierarchy. No naturalness claim is made either way; the number is presented and left to be what it is.

**What this accomplishes, tiered exactly:** the khronon EFT **loses its last free cosmological constant** — `\mathcal{W}_0` is now *fixed*, at **D-via-I** (the tier transported from 038.5's closure, per §1's rule). The EFT's cosmological face is thereby fully specified up to the regulator family's `Θ`-*dependence* (the dial), whose *endpoint* `\mathcal{W}_0 = \mathcal{W}(0, Θ\!\to\!1)`-value is now pinned. Not a derivation of Λ — a determination of the EFT by the substrate-plus-inheritance, which is what matching is.

## 5. What remains open — and the upgraded falsifiable edge

The genuinely open piece is unchanged in identity but sharpened in specification: the **ab-initio substrate evaluation** of the V1 boundary integral — computing `\int_{R_H^3}\rho_{\rm vac,V1}` from the V1 form factor and the Route-A substrate parameters *without* inheriting the observed value, including the curvature-coupling chain (§3's caveat). This is exactly Paper_038.5's RA-OPEN frontier, untouched in difficulty. What this round adds to it is a **target**:

> **The falsifiable edge, upgraded.** R6's edge was qualitative ("sign or beyond-`O(1)` disagreement"). It is now numeric: the ab-initio computation, when performed, must land on `\mathcal{W}_0 = -24\pi^2\Omega_\Lambda` (equivalently `6\,\Omega_\Lambda` in `(cH_0)^2`-units, sign as in §3). Landing elsewhere — wrong sign, or wrong by more than the computation's honest error — would break the one-Λ thesis and expose an internal tension between the substrate and EFT faces. The thesis now has a number to miss.

**The clamps, restated:** no value of Λ derived (the transcription inherits 038.5's D-via-I closure — the tier-transport rule forbids reading §4 as a derivation); the matter-sector cosmological-constant problem untouched; `\Omega_\Lambda` observational; the `O(1)` of the *substrate* integral still uncomputed.

## 6. Verdict, and the ledger after Round 7

**The matching is performed to its honest limit.** The condition is stated (Friedmann-level equality; double-counting procedurally dissolved); the scaling identity is exhibited parameter-free (both faces `H_0^2c^2/G`, by the shared boundary); the sign check **passes** at the density level (positive-definite V1 vacuum ⟹ `Λ > 0` ⟹ observed sign), fixing `\mathcal{W}_0 < 0`; and the coefficient is transcribed — `\mathcal{W}_0 = -24\pi^2\Omega_\Lambda \approx -162` (`= 6\Omega_\Lambda \approx 4.1` against `(cH_0)^2`) — at **D-via-I**, the tier transported, not upgraded. The khronon EFT's cosmological endpoint is now pinned; the regulator family retains only its `Θ`-*shape*. The ab-initio V1 integral remains the open frontier, now with a specific number to hit or miss.

**The cosmology thread's ledger, post-R7:**
- **Derivation-side:** the ab-initio V1 integral (Route-A-class; 038.5's frontier, now with the §5 target) — and the guarded primitives-origin, unchanged.
- **Model-building:** the dial — `𝒲`'s `Θ`-shape under the five filters, with its endpoint now fixed.
- **Observation:** wide binaries; the τ-sector; the CMB on the chosen dial member — *left, per instruction, for later or for someone else.*

---

*Round-7 matching computation. The one-Λ thesis is made operational: Friedmann-level matching defines the EFT constant from the substrate face (double-counting procedurally dissolved); the scaling identity is exact and parameter-free (both faces `H_0^2c^2/G` via the one SCBU boundary); the sign check passes at the density level (positive-definite V1 vacuum ⟹ Λ > 0, fixing `𝒲₀ < 0`, with the coupling-chain confirmation assigned to the ab-initio task); and the coefficient is transcribed, `𝒲₀ = −24π²Ω_Λ ≈ −162` (order-unity, `6Ω_Λ ≈ 4.1`, against the raw background scale `(cH₀)²`) — at D-via-I, the tier transported from Paper_038.5 under the round's governing rule: matching transports tiers, it does not upgrade them. The khronon EFT loses its last free cosmological constant; the ab-initio V1 integral stays open with a numeric target attached; no value of Λ is derived; the matter-sector problem is untouched.*
