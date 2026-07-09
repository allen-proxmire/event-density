# Gauge Program · Step 6 — The Yang–Mills Action from the Substrate Coherence-Deficit (closing O-YM2-2)

**Foundations — step 6 (continues `Gauge_02`). Question: why is the gauge-field action ∝ F²? YM-2 (Paper_019) *postulated* this (`P-YM-Action-Coarse-Graining`) and named its derivation the open item O-YM2-2. Result: the substrate's own coherence-deficit on the U(N) plaquette holonomy IS the Wilson plaquette action, which coarse-grains (small-holonomy expansion) to −¼∫Tr(F²). This generalizes the *already-grounded abelian case* — the B4/Maxwell coherence term `cos²(Δφ/2) ≈ 1 − ¼(∇φ)²`, the abelian Wilson plaquette → Maxwell F² (the layers #2 coherent recovery) — to U(N). So `P-YM-Action-Coarse-Graining` is upgraded from P to D at the gauge-program (structural/analytic) tier. The trace-of-holonomy (Wilson) form — which looked like the load-bearing assumption — is itself **derived** (§4.5) from channel indistinguishability (P08, the SU(N)-giving primitive) applied to the per-chain coherence-deficit; the one remaining structural input is the per-chain gauge-coherence cost, abelian-grounded (B4/Maxwell), at the gauge-program tier (not a certified-simulator measurement). The non-abelian self-interaction (f^abc) and Lorentz covariance come for free from the holonomy and the acoustic metric.**

---

## 1. The question

`Gauge_02` derived the *connection and curvature* — ED's channel substrate is a U(N) lattice gauge theory with field strength F = the plaquette holonomy U_□. What it did **not** give is the **action** — why the dynamics are ∝ F². YM-2 supplied it only by postulate (`P-YM-Action-Coarse-Graining`), explicitly flagging O-YM2-2 (derive it). This note derives it from the substrate's coherence dynamics.

## 2. The substrate already penalizes the holonomy deficit (abelian, grounded)

The certified substrate's coherence channel penalizes phase mismatch. In the abelian (U(1)) gauge reading (B4 charge arc + the Maxwell coherent-decomposition, layers #2), the per-edge coherence is
$$\mathrm{Coh}_{\text{edge}} \;=\; \cos^2(\tfrac{\Delta\varphi}{2}) \;\approx\; 1 - \tfrac14(\nabla\varphi)^2 ,$$
so the substrate's **cost** for a phase deficit is `¼(∇φ)²`. Around the smallest loop (a plaquette), the abelian holonomy is `U_□ = e^{i\Phi}` with `Φ = ∮A = a²F` (the loop integral of the connection = the abelian field strength × area), and the loop coherence-deficit is
$$1 - \cos\Phi \;\approx\; \tfrac12\Phi^2 \;=\; \tfrac12 a^4 F^2 ,$$
the **abelian Wilson plaquette action**. Summed over plaquettes → `S ∝ ∫ F_{μν}F^{μν}` = the Maxwell action. **This is already grounded** — it is *why* the layers #2 coherent field tracked Coulomb. The substrate's coherence dynamics *are* the Wilson plaquette weighting, abelian.

## 3. The non-abelian lift

`Gauge_02`: with multiplicity N, the amplitude is `ψ ∈ ℂ^N` and transport is a U(N) link variable; the plaquette holonomy `U_□ ∈ U(N)`. The gauge-invariant coherence of an N-channel amplitude carried around the loop and compared with itself is
$$\mathrm{Coh}_\square \;=\; \tfrac1N\,\mathrm{Re}\,\mathrm{Tr}\,U_\square ,$$
(the natural lift of the abelian `cos Φ = Re\,e^{iΦ}`: trace over the N channels, real part for the coherence). The substrate's plaquette **cost** is the deficit
$$\mathcal{S}_\square \;=\; 1 - \tfrac1N\,\mathrm{Re}\,\mathrm{Tr}\,U_\square .$$
**This is exactly the Wilson plaquette action** — not chosen, but read off the substrate's coherence-deficit, generalizing §2. For N=1 it reduces to the grounded abelian case.

## 4. The coarse-graining → F²

Write the plaquette holonomy for a smooth, weakly-curved connection: `U_□ = exp(i a² F_{μν})` with `F_{μν} = ∂_μ A_ν − ∂_ν A_μ + i[A_μ, A_ν]` (the non-abelian field strength — the commutator is automatic from the U(N) non-commutativity of the link product). Expand the trace to second order in the holonomy:
$$\tfrac1N\,\mathrm{Re}\,\mathrm{Tr}\,U_\square \;=\; 1 - \tfrac{a^4}{2N}\,\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu}) + O(a^6),$$
so the substrate plaquette cost is
$$\mathcal{S}_\square \;\approx\; \tfrac{a^4}{2N}\,\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu}).$$
Summing over plaquettes in the continuum (hydrodynamic-window DCGT, `ℓ_ED ≪ R_cg ≪ L_flow`),
$$S \;=\; \sum_\square \mathcal{S}_\square \;\xrightarrow{\text{continuum}}\; \frac{1}{2g^2}\int \mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})\,d^4x \;=\; -\tfrac14\int F^a_{\mu\nu}F^{a\,\mu\nu}\,d^4x,$$
the **Yang–Mills action**, with the coupling `g` set by the coherence coefficient and the effective graph scale `a`. The non-abelian quartic (`g f^{abc}A^b_\mu A^c_\nu` inside F) is built in from the commutator; Lorentz covariance is inherited from the substrate acoustic metric (Paper_017). This is the standard lattice→continuum Wilson expansion — the ED content is that the *substrate's coherence-deficit supplies the Wilson weighting*, rather than it being a chosen action.

## 4.5 The Wilson form is forced by channel indistinguishability (cashing the could-say-no)

§3 lifted the coherence-deficit to `1 − (1/N)Re Tr U_□` as the *natural* non-abelian form. It is in fact **forced**, not assumed, once one more substrate fact is used — the same one that gives SU(N) in the first place.

A single chain carrying amplitude `ψ ∈ ℂ^N` around the plaquette returns as `U_□ψ`; the coherence it retains is the overlap `Re⟨ψ|U_□|ψ⟩`, and the substrate's cost is the **per-chain** deficit `1 − Re⟨ψ|U_□|ψ⟩` (the gauge generalization of the abelian `1 − cos Φ`, §2). This is *state-dependent* — different `ψ` give different costs.

But the N channels are **indistinguishable** (P08): no substrate fact prefers any direction in `ℂ^N`, so the distribution of chain amplitudes is invariant under U(N) — and the only U(N)-invariant distribution on the fiber is **uniform**. The coarse-grained (DCGT) plaquette cost is the *average* of the per-chain deficit over that uniform distribution:
$$\big\langle 1 - \mathrm{Re}\langle\psi|U_\square|\psi\rangle\big\rangle_\psi \;=\; 1 - \mathrm{Re}\,\mathrm{Tr}\!\Big(U_\square\!\int|\psi\rangle\langle\psi|\,d\psi\Big) \;=\; 1 - \tfrac1N\,\mathrm{Re}\,\mathrm{Tr}\,U_\square ,$$
using `∫|ψ⟩⟨ψ| dψ = (1/N)𝟙`. **The trace — the Wilson form — is the fiber-average over indistinguishable channels.** It is not an extra postulate; it follows from P08 (the SU(N)-giving primitive) applied to the per-chain coherence-deficit.

So ED's Yang–Mills action is the **matter-induced effective gauge action**: the cost the gauge configuration imposes on the indistinguishable-channel matter living on it, averaged over that matter (uniform by P08) → the Wilson plaquette action → F². The "trace-of-holonomy" that looked like the load-bearing assumption is derived; only the per-chain cost form remains as input.

## 5. What this closes and what it rests on

**Closes:** O-YM2-2 — `P-YM-Action-Coarse-Graining` is now a **derivation** (D), not a postulate (P): the substrate coherence-deficit on the U(N) plaquette holonomy = the Wilson action, which coarse-grains to −¼Tr(F²). YM-2's audit step 6 strengthens P→D per O-YM2-Revision; the three Appendix components (kinetic F², non-abelian quartic, Lorentz covariance) all follow.

**Rests on (the load-bearing assumption, stated honestly):**
1. **The per-chain gauge-coherence cost is `1 − Re⟨ψ|U_□|ψ⟩`** (the gauge generalization of the abelian `1 − cos Φ`, B4/Maxwell-grounded). Given this, the **trace/Wilson form is derived** (§4.5) — it is the fiber-average forced by channel indistinguishability (P08, the SU(N)-giving primitive), *not* a separate assumption. The one remaining structural input is the per-chain cost form itself, a gauge-program-tier reading (the gauge channels are not in the certified Σ-simulator; the *abelian* case is simulator-grounded via the Maxwell coherent recovery). This is one fewer assumption than §3 first stated.
2. **The coupling `g` and the effective scale `a`** are inherited, not derived (O-YM2-3).
3. **Leading order only** — sub-leading V1/V5 finite-width corrections are O-YM2-1.
4. **The relational graph has no regular spacing `a`** — the small-holonomy expansion needs the holonomy small (weak field / fine graph), which is the continuum limit; valid for any lattice, regular or relational, in that limit.

## 6. Status and falsifier

**Gauge step 6: the Yang–Mills action is derived (structural/analytic tier) from the substrate coherence-deficit on the U(N) plaquette holonomy — the non-abelian generalization of the grounded abelian Maxwell case — closing O-YM2-2 and upgrading YM-2's central postulate P→D.** This shores up the foundation the rest of the YM arc (OS-positivity Paper_020, mass gap Paper_021, Clay synthesis Paper_023) rests on.

**Falsifier (sharpens YM-2 F1):** if the substrate's N-channel coherence functional is shown *not* to take the `Re Tr U_□` form — e.g. channel-diagonal, or weighted so the plaquette cost is not the holonomy deficit — then the Wilson form fails and F² does not follow; the postulate would revert to P (or be refuted). The decisive check is to write the substrate's gauge-coherence functional for an N-channel amplitude explicitly from P04+P07 and confirm it is the trace-of-holonomy deficit.

---

## 7. Verification (2026-07-08, `evaluation/ChiralGauge/ym_action_check.py`)

Both load-bearing MATH steps confirmed numerically, and the physical input tied to grounded structure:
- **(i) The trace/Wilson form is the P08 fiber-average (derived, not assumed).** Fiber-averaging the per-chain deficit `1 − Re⟨ψ|U|ψ⟩` over Haar-uniform `ψ` matches `1 − (1/N)Re Tr U` (1.1112 vs 1.1115 at N=3), confirming `∫|ψ⟩⟨ψ|dψ = 𝟙/N` forces the trace. §4.5 holds.
- **(ii) Small-holonomy → F².** `deficit/a⁴` converges to `Tr(F²)/2N` as `a→0` (clean 4-digit convergence), so `1 − (1/N)Re Tr U_□ → (a⁴/2N)Tr(F²)`. §4 holds.
- **The load-bearing physical input is grounded.** The per-chain cost `1 − Re⟨ψ|U_□|ψ⟩` is exactly the *amplitude-overlap coherence* characterized in the 2026-07-08 V5/P12 work (coherence = overlap of an amplitude with its transported self). So the input is the substrate's coherence structure, not an extra postulate.

**Net verdict: the YM action FORM is derived at structural/analytic tier** (the math checks out; the trace form is P08-forced; the input is the grounded coherence-overlap). Honest residuals unchanged: the non-abelian coherence-cost is a gauge-program-tier lift (the gauge channels are not in the certified Σ-sim; the abelian case is simulator-grounded); `g` and `a` are inherited; the continuum limit leans on DCGT + small-holonomy. So the whole gauge program now reads: **structure (SU(N) form) + gauging (non-abelian, generic) + action (F²) all DERIVED (structural/analytic); the specific group {1,2,3} is a WALL (`Gauge_09`); couplings/scales and electroweak details inherited/open.**

---

*Gauge step 6. Why F²? The substrate coherence-deficit on the U(N) plaquette holonomy, 1 − (1/N)Re Tr U_□, IS the Wilson plaquette action (the non-abelian lift of the abelian B4/Maxwell coherence 1 − cos Φ ≈ ½F², already grounded — the layers #2 coherent recovery). Small-holonomy expansion → (a⁴/2N)Tr(F²) → continuum −¼∫F^aF^a: the Yang–Mills action. Non-abelian quartic from the commutator in F; Lorentz covariance from the acoustic metric. Closes O-YM2-2, upgrades YM-2 step 6 P→D. Load-bearing assumption: the N-channel coherence-deficit is the trace-of-holonomy form (natural lift, abelian case simulator-grounded; non-abelian is analytic, gauge-program tier — not the certified Σ-simulator). g and a inherited; leading order; relational-graph continuum limit = small holonomy. Falsifier: substrate coherence shown not to be the Re Tr U_□ deficit.*
