# Phase-3 GR — Round 3: Bianchi (C2) and Forcing of F (C3)

**Foundations keystone analysis. Not a rule proposal, not a corpus edit, not a new primitive.**
Tests whether bandwidth-budget conservation + the commitment-rate law force a unique dynamical-bandwidth rule and function as the contracted-Bianchi analogue for `g ~ b⁻¹`.
**Crank rail:** run forward (derive from the primitives + geometry), never backward from Einstein. The point of this round is to find the *honest* location of the obstruction, not to manufacture a closure.

---

## 1. Formalizing the conservation law

The four bands (`b_int, b_adj, b_env, b_com`) are a partition of a **chain's** bandwidth at a locus (`participation_bandwidth.md`). A commitment **redistributes** between bands at that locus (draws from `b_com`, concentrates into the selected channel's `b_int`) — an internal transfer with no net change. The locus total changes only by **flux**: the **adjacency** band exchanges with neighbors via P05 transport, and the **environmental** band exchanges with the environment. So the exact statement is a **local continuity law**, per locus:

> `d/dt [ Σ_bands b(u) ] = − div(adjacency flux via P05) − (environmental exchange)`

It is **local** (per node), with the adjacency band as the inter-node flux and commitment as a *purely internal* band transfer. For an environmentally-isolated subsystem it closes (`d/dt Σb = −div(flux)`); otherwise the env band is a source/sink term. This is the shape of a continuity equation, not a closed global conservation — which is exactly right, because that is the shape of `∇_μ T^μν = 0` (covariant divergence with flux), not of a global "total = const."

## 2. The correction this round forces

The round's framing — "does this conservation law function as the analogue of the contracted-Bianchi identity `∇_μ G^μν = 0`?" — conflates two *different* objects, and separating them is the keystone result:

- **`∇_μ G^μν = 0` (contracted Bianchi) is a *geometric identity*.** It holds *automatically* for **any** metric with a metric-compatible (Levi-Civita) connection — it follows from the second Bianchi identity `dR = 0`. It is *not* a dynamical conservation law and is *not* something ED must derive from bandwidth.
- **`∇_μ T^μν = 0` (matter conservation) is a *dynamical* law.** *This* is what the bandwidth continuity law of §1 is the analogue of.

So the bandwidth conservation law is the **`∇·T = 0` analogue (matter/source conservation), not the `∇·G = 0` analogue (geometric identity).** That reframes the keystone: the question is **not** "is there a Bianchi-analogue conservation law" (there is — bandwidth continuity), but whether the emergent geometry is *genuine enough* that `∇·G = 0` holds for free, and whether matter conservation is *covariant* with respect to that same geometry.

## 3. Bianchi viability

With the correction, the EFE consistency `G ∝ T` (both sides divergence-free in the *same* connection) decomposes into three sub-conditions:

- **(i) `∇·G = 0`:** automatic **iff** `g ~ b⁻¹` is a genuine Riemannian metric with a Levi-Civita connection. ED's metric is bandwidth-built and *coarse-grained* — genuine only in the thick/DCGT regime, and metric-compatibility (`∇g = 0`) is the Round-1 open condition. So `∇·G = 0` is **inherited-for-free in the thick regime if** the metric is genuine — the obstruction is metric-genuineness, **not** the identity.
- **(ii) `∇·T = 0`:** the bandwidth continuity law (§1) is a real, local candidate, compatible with P11 (commitment is an internal transfer; ρ stays monotone) and A1 (local, no nonlocal flux).
- **(iii) covariance:** (i) and (ii) must use the *same* covariant derivative — the matter flux (P05 transport) must be covariant w.r.t. the emergent connection from `g ~ b⁻¹`. Since both the metric *and* P05 transport are built from the bandwidth structure, compatibility is **plausible but unproven**.

**A new gap this round surfaces — signature assembly.** `g ~ b⁻¹` from non-negative bandwidth is naively **Riemannian (positive-definite)** — it is the *spatial* metric. GR needs a **Lorentzian** metric with causal structure; that temporal/causal part is supplied separately by the **V1 retarded kernel** (GR1/T9, arrow from P11/T18). So `g ~ b⁻¹` is *not yet a spacetime metric* — it is the spatial sector, and the full Lorentzian metric is an **unassembled combination of bandwidth (space) + kernel-arrow (time/causality)**. Bianchi for the *spacetime* metric is only meaningful after that assembly.

**Verdict on Bianchi: VIABLE, not established.** The conservation law exists and is the `∇·T` analogue; `∇·G` is automatic for a genuine metric; the residual obstructions are **metric-genuineness/compatibility (thick regime)**, **transport-covariance**, and **signature assembly** — none of which is the *existence of a conservation law*. The keystone is relocated, not closed.

## 4. Is F forced by `Γ_commit ~ b_int / reserve`?

The commitment-rate law fixes the *rate* of band transfer; the four-band semantics fix that the transfer is reserve→concentrated and monotone. Together they force the **shape** of `F`:

- rate `∝ b_int / reserve` (commitment-rate-driven),
- monotone reserve drain (P11-irreversible consumption),
- conservative redistribution (internal transfer; total changes only by §1 flux),
- orientation-blind (reads ρ/b, not orientation).

But they do **not** fix `F` uniquely. Underdetermined are: the proportionality constant; the per-event redistribution amount `δ`; and — load-bearing — the **band→edge mapping** (the four bands are *per-chain*; the metric `g ~ b_ij⁻¹` is *per-edge*; identifying the per-chain band dynamics with the per-edge `b_uv` evolution needs an additional principle). So:

> **F is PARTIALLY FORCED** — its qualitative form is forced by `Γ_commit` + four-band semantics; a residual functional family (constant, increment, band↔edge map) remains.

The honest hope, and the crank-safety hinge: the **covariance requirement of §3(iii)** is a strong constraint that may pin the residual freedom — the band↔edge map and transport structure could be *forced* by demanding bandwidth transport be covariant w.r.t. the emergent connection. If so, `Γ_commit ∩ covariance` forces `F` uniquely and the derivation is genuine; if not, choosing within the family to get EFE would be a retrofit. **That intersection is Round 4 and is currently unproven.**

## 5. Constraints → forced properties of F

| Constraint (certified) | Forces on F | Leaves free |
|---|---|---|
| `Γ_commit ~ b_int/reserve` (commitment.md) | rate ∝ b_int/reserve | overall constant |
| P11 irreversibility | monotone reserve drain (one-way) | per-event amount δ |
| P04 four-band redistribution | conservative (internal transfer) | which band feeds `g~b⁻¹` |
| orientation-blind Σ | F reads ρ/∇ρ/b only | — |
| P02 (no edge create/destroy) | acts on existing edges; b→0 = capacity collapse | — |
| **covariance w.r.t. emergent connection (needed for §3iii)** | *would* fix band↔edge map + transport | **unproven — Round 4** |

Five certified constraints fix F's shape; the sixth (covariance) is what would close uniqueness, and it is not yet established.

## 6. Cross-arc consistency

The residual freedom in F is **harmless** for A1/A2/B4 and **load-bearing** only for full EFE:

- **A2 emergent decoupling** — ✅ any F in the admissible family is a monotone drain → `b→0` → emergent (frozen) cut. Family-level property; freedom irrelevant.
- **A1 signature** — ✅ F local; emergent `b→0` cut gives exact-zero capacity. Preserved.
- **B4 orientation-blindness** — ✅ F is commitment/ρ-driven, reads no orientation. B4's active charge remains separately gated (Round 2). Preserved.
- **Phase-3 GR nonlinear closure** — ⚠️ depends on the *specific* F (via covariance/Bianchi) — the one place the underdetermination bites. Conditional on Round 4.

So none of A1/A2/B4 needs F pinned; only EFE closure does — which correctly localizes the remaining work to the geometry side, not the dynamics side.

## 7. Verdicts

- **Bianchi: VIABLE, NOT ESTABLISHED.** The bandwidth continuity law is the `∇·T = 0` analogue (matter conservation), **not** the `∇·G = 0` analogue (which is automatic for a genuine metric). EFE consistency is therefore gated on **metric-genuineness/compatibility (thick regime)**, **transport-covariance**, and **signature assembly (bandwidth-space + kernel-arrow-time)** — geometry-side conditions, not a missing conservation law.
- **F: PARTIALLY FORCED.** `Γ_commit` + four-band semantics force F's qualitative shape (rate ∝ b_int/reserve, monotone, conservative, orientation-blind); a residual family (constant, δ, band↔edge map) remains. Unique forcing would require the covariance condition (Round 4) to pin the band↔edge map — currently unproven.

The net of Rounds 1–3: full EFE emergence is **partially admissible**, the missing extension is **admissible and largely forced** (the un-implemented commitment-reserve dynamics), the matter-conservation half of the consistency is **in hand**, and the obstruction is now precisely localized to a small set of **geometry-side, thick-regime** questions — not to any clash with a certified primitive. That is a much sharper "genuinely open" than the corpus's starting point, and it stays honest: nothing here derives Einstein.

## 8. Round-4 questions

1. **Metric genuineness/compatibility.** Is `g ~ b⁻¹` a genuine Riemannian metric with Levi-Civita connection in the thick/DCGT regime, so `∇·G = 0` holds for free? (If not, EFE is blocked regardless of dynamics.)
2. **Signature assembly.** How do the bandwidth *spatial* metric (P04) and the V1 kernel-arrow *temporal/causal* structure (GR1/T18) assemble into one Lorentzian spacetime metric? Until assembled, "EFE for `g~b⁻¹`" is premature.
3. **Transport-covariance (the uniqueness hinge).** Is P05 bandwidth transport covariant w.r.t. the emergent connection — and does requiring it *force* the band↔edge map (closing C3)?
4. **Joint forcing.** Does `Γ_commit ∩ covariance` force F uniquely (genuine derivation) or only up to a family (retrofit risk)?
5. **Thick-regime corrections.** What is the discrete-scale (DCGT) correction to the EFE-analogue, and does it predict a departure from exact GR (a potential falsifier)?

---

*Round-3 keystone analysis only. Verdict: Bianchi-VIABLE but not established (the conservation law is the `∇·T` analogue, not `∇·G`; the obstruction is geometry-side — metric-genuineness, covariance, signature assembly); F is PARTIALLY FORCED (shape forced by Γ_commit; uniqueness needs the covariance condition of Round 4). No corpus edits, no new primitives, no speculative physics. Nothing here derives the Einstein equations.*
