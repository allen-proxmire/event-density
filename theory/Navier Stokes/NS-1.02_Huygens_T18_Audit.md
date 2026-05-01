# NS-1.02 — T18 Sharp-Huygens Audit

**Date:** 2026-04-30
**Status:** Audit complete. **Verdict: Route 2.2 FAILS.** T18 does not require sharp Huygens propagation; it tolerates Hadamard-type interior-supported retardation kernels. The PDE-level dimensional-forcing route via T18 does not exist.
**Sources audited:** [`theorems/T18.md`](../../theorems/T18.md), [`arcs/arc-B/arrow_forced.md`](../../arcs/arc-B/arrow_forced.md) (B.2), [`arcs/arc-B/arc_b_synthesis.md`](../../arcs/arc-B/arc_b_synthesis.md) (B.5).

---

## 1. Purpose

This memo executes Step 1 of NS-1: audit whether T18's V1 kernel-retardation derivation forces sharp Huygens behavior (cone-supported propagation) or tolerates Hadamard-type interior support.

The question is binary, and its outcome determines the existence of any purely-PDE-level dimensional-forcing route in NS-1:

- **If T18 forces sharp Huygens** → odd d ≥ 3 forced at PDE/kernel level; Route 2.2 closes; combined with substrate motif viability (Route 2.3) ruling out d ≥ 4, d = 3 is forced.
- **If T18 tolerates Hadamard tails** → Route 2.2 fails; PDE-level dimensional forcing must come from elsewhere (Route 2.1's PDE↔spinor-bundle propagation, if it exists) or B2 closes only at substrate level (Routes 2.3 + 2.4).

The audit was performed against the actual derivation as it lives in the repo, not against any reconstruction.

---

## 2. What T18 Actually States

### 2.1 Headline statement

T18 (V1 Kernel Retardation FORCED): the V1 vacuum-response kernel $K_\mathrm{vac}(x, x')$ is uniquely forced to have support restricted to the forward causal cone:

$$K_\mathrm{vac}(x, x') \neq 0 \;\Longrightarrow\; (x - x') \text{ lies in the forward causal cone}.$$

(B.5 §2.1; B.2 §3.4.3)

### 2.2 The derivation chain (B.2 §3.4, B.5 §3)

**Step 1.** V1 is a *response kernel* (Theorem N1 + Q.8 effective-vacuum factorisation), distinct from the unperturbed Wightman correlator $W$.

**Step 2.** Response kernels are sourced. V1's source is chain bandwidth content; non-chain contributions live in $W$, not V1.

**Step 3.** Chain bandwidth dynamics are forward-only along proper time:
- P11 (commitment-irreversibility): commitment events non-reversible.
- P02 (chain): worldline $\gamma_K$ parameterised by proper time $\tau_K$.
- P13 (proper-time): finite intervals between commitment events, ordered by P11.
- P04 (bandwidth update): bandwidth content $b_K(\tau_K)$ updated forward.

Joint result: chain forward-propagator $U_K(n,m) = 0$ for $n < m$.

**Step 4.** The chain-contribution sum:
$$K_\mathrm{vac}(x, x') = \sum_K \sum_{n \geq m} \mathcal{F}_K(x; \tau_K^{(n)}) \cdot U_K(n, m) \cdot \mathcal{F}_K^\dagger(x'; \tau_K^{(m)}).$$

The $n \geq m$ constraint maps (per chain $K$ with timelike worldline) to $(x - x')$ lying in the forward causal cone of $\gamma_K$. P11 universality across chains ⇒ globally forward-cone-only kernel support.

**Step 5.** Therefore V1 is RETARDED.

### 2.3 Step-by-step cone/dimension audit

| Step | Mechanism | Cone-geometry role | Dimension-sensitive? |
|---|---|---|---|
| 1 | V1 = response kernel (N1 + Q.8) | None | Dimension-agnostic |
| 2 | Response sourced by chain bandwidth | None | Dimension-agnostic |
| 3 | Chain forward propagator $U_K(n,m) = 0$ for $n < m$ | None — pure ordering on $\tau_K$ | **Dimension-agnostic.** Requires only that chains are timelike worldlines parameterised by an ordered proper time. Holds in any (1, d) Lorentzian signature with d ≥ 1. |
| 4 | Forward proper-time ordering ⇒ forward causal cone | **Causal-cone geometry**, not Huygens-cone geometry. Uses only timelike-future-of-x' = J⁺(x'), which exists in any Lorentzian signature. | Dimension-agnostic |
| 5 | Therefore V1 is retarded | None — synthesis | Dimension-agnostic |

**Critical observation.** No step relies on the *fundamental-solution* structure of the wave operator. The cone in T18 is the *Lorentzian causal cone* (defined by signature, not by PDE), not the *Huygens light cone* (defined by sharp wave propagation in odd d ≥ 3).

### 2.4 What N1 fixes about V1's form

Theorem N1 (Arc N): V1 is Lorentz-scalar, finite-width on $\ell_\mathrm{ED}$, sub-power-law-2 decaying. The retarded form is:

$$K_\mathrm{vac}^\mathrm{ret}(x, x') = \theta(t - t') \cdot G(\sigma(x, x') / \ell_\mathrm{ED}^2)$$

where $G$ is a smooth Lorentz-scalar function of the Synge world function $\sigma$. **$G$ is finite-width, supported in a tube around $\sigma = 0$ — i.e., $G$ is interior-supported in the cone, not strictly on the cone surface.**

This is the smoking gun. The V1 form-class is *already* Hadamard-type interior-supported, by construction, before any retardation question arises. The $\theta$-factor restricts $G$ to the forward half (cone interior + null boundary), but $G$ itself is interior-supported.

---

## 3. Kernel Support Analysis

### 3.1 What does T18 actually constrain?

The retarded $\theta(t-t')$ factor restricts kernel support to the closed forward causal cone:

$$\mathrm{supp}\, K_\mathrm{vac}^\mathrm{ret} \subseteq \overline{J^+(x')} = \{x : (x - x') \text{ timelike-or-null forward-pointing}\}.$$

This is the *closed forward causal future* — the entire interior of the forward cone, plus its lightlike boundary. **Not** the lightlike boundary alone.

Sharp Huygens, by contrast, requires support on the lightlike boundary only:

$$\mathrm{supp}\, K_\mathrm{vac}^\mathrm{Huygens} \subseteq \partial J^+(x') = \{x : (x - x') \text{ null forward-pointing}\}.$$

Sharp Huygens is a *strict subset* of forward-causal support. T18 establishes the latter, not the former.

### 3.2 What would break if interior support were allowed?

Walk each step of the T18 derivation and ask: does anything fail if $G(\sigma)$ is interior-supported (Hadamard tail)?

- **Step 1 (response kernel).** Unaffected. Response-kernel character is independent of support details within the cone.
- **Step 2 (sourced contribution).** Unaffected. Sourcing is a definitional fact about V1, not a support fact.
- **Step 3 (forward chain dynamics).** Unaffected. Forward-only chain propagator is purely an ordering statement on $\tau_K$, not a support statement on the cone.
- **Step 4 (chain sum).** Unaffected. The constraint is $n \geq m$, mapping to "$(x - x')$ in forward cone." Whether the kernel populates the *interior* of the forward cone or only its *boundary* is independent of the $n \geq m$ structure.
- **Step 5 (retardation).** Confirmed: forward-cone support, with no further restriction to the boundary.

**Nothing in T18 breaks if interior support is allowed.** T18's mechanism is *cone-side discrimination* (forward vs. backward), not *cone-locus discrimination* (boundary vs. interior).

### 3.3 Direct evidence T18 expects Hadamard tails

Three pieces of textual evidence in the Arc B closure:

1. **N1 form-class fixes V1 as finite-width Lorentz-scalar $G(\sigma/\ell_\mathrm{ED}^2)$** (B.2 §2.1, B.5 §2.1). Smooth $G$ has interior support around $\sigma = 0$ — already Hadamard-type, not delta-on-cone.

2. **Phase-3 GR1 lift uses Hadamard parametrix.** B.5 §5.5 / B.4: "Theorem GR1 (V1 with Synge world function in curved spacetime) lifts cleanly to retarded $K_\mathrm{vac}^\mathrm{curved}$ via Hadamard-parametrix causal-future restriction." Hadamard parametrix is the technical machinery that *explicitly* allows interior-supported tail terms in Green's-function constructions for curved spacetime — it is the standard framework when sharp Huygens fails (curved spacetime in any d, flat spacetime in even d or d ≠ 3). T18's curved-spacetime extension is built on Hadamard structure by name.

3. **CR continuum-approximation correspondence: V1 retarded ↔ $G_R$.** B.5 §5.6 mapping table. The continuum retarded Green's function $G_R$ is supported on the closed forward cone in any d; it is sharp-Huygens-supported only in odd d ≥ 3 (and only in flat spacetime). T18 invokes $G_R$ as the natural continuum correspondent without restriction to d = 3, indicating the framework treats V1 as $G_R$-class (forward-causal) regardless of d.

### 3.4 Does T18 rule out *any* dimensional structure?

Yes — T18's mechanism requires:
- A Lorentzian signature (signature (1, d), d ≥ 1) so that "timelike worldline" and "forward causal cone" are defined.
- An ordered proper-time parameter on chain worldlines (P02 + P13).
- A universal time orientation across the chain ensemble (P11).

These hold in any (1, d) signature for d ≥ 1. **T18 forces nothing about d.**

---

## 4. Dimensional Sensitivity

### 4.1 Does T18 force odd d ≥ 3?

No. The argument routes through chain-level proper-time ordering, not through wave-operator fundamental-solution structure.

**The key disconnect.** Sharp Huygens is a fact about the *fundamental solution* of the wave operator $\Box$ in flat spacetime: in odd d ≥ 3, $G_R^\mathrm{flat}$ is supported on the lightlike boundary $\partial J^+$; in even d or d = 1, $G_R^\mathrm{flat}$ has Hadamard tail support in the interior $J^+$. This dimensional dependence lives at the *PDE-fundamental-solution* level.

T18's argument never touches the fundamental solution of the wave operator. It works at:
- Chain dynamics level (P02, P04, P11, P13)
- Vacuum-response kernel construction level (N1 + Q.8)
- Causal-cone geometry level (Cl(3,1) signature → forward cone exists)

None of these is sensitive to whether the wave operator's fundamental solution has sharp or tail support.

### 4.2 Does T18 force exactly d = 3?

No. The Lorentz signature used in T18 is "Cl(3,1)" — which is forced by R.2.4 *for the spinor bundle*, not by T18 itself. T18 takes the Lorentzian signature as input (any (1, d) suffices) and derives forward-causal kernel support in that signature. The d = 3 specification is upstream of T18, not derived from it.

### 4.3 Is T18 dimension-agnostic?

**Yes, fully.** T18's primitive-level mechanism (P11 + P02 + P04 + P13 → chain forward propagator → forward-cone-only V1) operates identically in (1, 1), (1, 2), (1, 3), (1, 4), …, (1, d) Lorentzian signatures. Replace "Cl(3,1)" with "Cl(1, d)" everywhere and the derivation goes through unchanged.

This is consistent with B.1 §6.3's catalogue verdict (R-3): "**The kernel-arrow argument cannot route through the PDE.**" The arc explicitly disclaims any PDE-level (and therefore any fundamental-solution-level) routing.

### 4.4 Mapping ED primitive structure to PDE-level properties

| ED primitive content | What it forces at PDE level |
|---|---|
| P02 chain (worldlines) | Existence of timelike sub-manifolds |
| P04 bandwidth update | Forward-only chain history |
| P11 commitment-irreversibility | Universal time orientation across chains |
| P13 proper-time intervals | Ordered $\tau_K$ on each chain |
| Cl(3,1) signature (from R.2.4) | Lorentzian causal structure with one timelike, three spacelike directions |
| **Wave-operator fundamental-solution structure (sharp Huygens)** | **Not addressed by T18 or any closed primitive-level theorem in current inventory.** |

The last row is the core finding. ED's primitive set fixes time orientation, causal structure, and chain dynamics — but does not fix the fundamental-solution structure of the wave operator at the level required to discriminate sharp Huygens from Hadamard tails.

---

## 5. Verdict for Route 2.2

**Route 2.2 (Huygens-preservation) FAILS.**

T18 does not force sharp Huygens kernel support. T18 forces *forward-causal* kernel support, which is dimension-agnostic in any (1, d) Lorentzian signature. Hadamard-type interior-supported retardation kernels are fully compatible with T18's derivation; the chain-contribution mechanism does not discriminate boundary support from interior support of the cone.

**No conditional.** The verdict is robust:

- It does not depend on any pending P05/P08/P12 verification (the T18 forcing argument routes through P11 + P02 + P04 + P13 only).
- It does not depend on Phase-3 GR1 lift specifics (the Hadamard parametrix machinery in the GR1 lift is corroborating evidence, not load-bearing).
- It does not depend on the CR continuum-approximation framing (which independently uses $G_R$, a forward-causal-class object that exists in any d).

The verdict closes Route 2.2 cleanly. There is no salvage path — T18 is not a candidate sharp-Huygens forcer.

---

## 6. Implications for NS-1

### 6.1 The dimensional-forcing landscape is now substrate-only

With Route 2.2 closed, NS-1's surviving forcing routes are:

- **Route 2.1 (Cl(3,1) → PDE-level via inseparability argument)** — derivative of R.2.4, requires a propagation step that has not yet been articulated. Operates at the spinor-bundle-PDE interface, not at PDE-fundamental-solution level. Independent open question.
- **Route 2.3 (substrate motif viability)** — substrate-combinatorial, provides d ≤ 3 upper bound with d ≥ 3 lower bound articulated via T20 (d=2 degenerate) + chain-primitive collapse (d=1 degenerate). Independent of T18.
- **Route 2.4 (T19/T20 internal consistency)** — substrate-geometric, conditional on primitive d-agnosticism. Independent of T18.

The PDE/kernel-level layer has *no* surviving route in NS-1. Either Route 2.1 is strengthened to PDE-level forcing via the spinor-bundle propagation step, or B2 closes only at substrate level.

### 6.2 Updated dependency structure

Pre-audit (NS-1 scoping document §3):
- Routes 2.1, 2.2, 2.3, 2.4 span three layers (representation, PDE/kernel, substrate)
- Route 2.2 is the sole purely-PDE-level route
- Concordance across ≥ 3 layers makes B2 overdetermined

Post-audit:
- Routes 2.1, 2.3, 2.4 span two layers (representation, substrate)
- No purely-PDE-level route in current inventory
- Maximum concordance is two-layer (representation + substrate) rather than three-layer
- B2 *can still close*, but only at substrate level + spinor-bundle level, not at PDE-fundamental-solution level

### 6.3 What NS-2 inherits

NS-2 (substrate→NS coarse-graining) inherits a weaker dimensional-forcing footing than the scoping document hoped:

- **No PDE-level forcing of d = 3+1 from T18.** NS-2 cannot assume the substrate→NS coarse-graining is uniquely well-posed at d = 3+1 by appeal to T18.
- **Substrate-level forcing (Routes 2.3 + 2.4)** still closes B2 in the substrate sense if those routes deliver. NS-2 inherits "substrate primitives are coherent at d = 3 and degenerate at d ≠ 3" rather than "the PDE itself only exists at d = 3+1."
- **The Clay statement is dimensional.** The Clay-NS problem is stated in 3+1 specifically. NS-2's job is to derive the NS form from substrate dynamics in 3+1; it does not require independent PDE-level dimensional forcing in order to proceed. The dimensional forcing question is structurally orthogonal to NS-2's form-derivation task.

### 6.4 Substantive finding from the audit

A negative result on Route 2.2 reveals a positive structural fact: **T18's mechanism is fundamentally chain-causal, not wave-operator-causal.** ED's microscopic arrow of time lives at the chain-dynamics layer, not at the PDE-fundamental-solution layer. This is consistent with B.1 §6.3 R-3's catalogue verdict and is, in retrospect, a structurally cleaner reading of how ED produces a microscopic arrow.

The implication for the broader program: any future arc that asks "does X live at PDE-fundamental-solution level?" should expect a similar chain-vs-PDE separation. If sharp Huygens (or any other PDE-fundamental-solution property) is needed elsewhere in the program, it will need its own primitive-level derivation; T18 will not supply it.

---

## 7. Inventory Status

### 7.1 Files updated by this audit

None directly. This memo (`NS-1.02_Huygens_T18_Audit.md`) is the audit deliverable.

### 7.2 Files that should be updated downstream

- **NS-1 scoping document** ([`Dimensional_Forcing_B2_Scoping.md`](Dimensional_Forcing_B2_Scoping.md)): add a "Route 2.2 — CLOSED FAILED 2026-04-30" note in §2.2 and §3, reflecting the post-audit dependency structure of §6.2 above. Routes 2.1, 2.3, 2.4 remain active.
- **NS-1.05 synthesis (when drafted)**: incorporate the negative-Route-2.2 result and report B2 verdict at substrate-level only (assuming Routes 2.3 / 2.4 close affirmatively).
- **Project memory** (`memory/project_navier_stokes_roadmap.md` once the NS arc moves to active status): record Route 2.2 closure as part of NS-1 progress.

### 7.3 Files to confirm exist before next memo

- **`theorems/T19.md`, `theorems/T20.md`** — needed for Route 2.4 audit (NS-1.04). Existence confirmed via roadmap cross-references; full content read pending.
- **ED-Phys-39** — referenced in user notes as showing 4D barely-architectural; file location not yet confirmed in repo. Needed for Route 2.3 audit (NS-1.03). If absent, Route 2.3 must be derived from the seven PDE-uniqueness axioms + substrate primitives directly without an ED-Phys-39 foundation.

### 7.4 No new derivations needed

This audit produced no new theorem candidates and requires no new primitive-level derivations. It is a *negative* result: a route hypothesised in NS-1 scoping is closed off as non-viable.

---

## 8. Recommended Next Steps

In priority order. The negative verdict on Route 2.2 makes Routes 2.3 and 2.4 the load-bearing remaining work; Route 2.1 becomes a secondary backup path.

1. **Draft Memo NS-1.04 — T19/T20 dimensional sensitivity audit.** File: `theory/Navier Stokes/NS-1.04_T19_T20_Dimensional_Audit.md`. Walk through T19's holographic-bound derivation in arbitrary d-spatial; identify where the 4πr² (d = 3) scaling is load-bearing. Walk through T20's dipole-mode derivation in arbitrary d; identify the 2π factor's dimensional specificity. Verdict: how strongly does internal consistency of the substrate-gravity arc force d = 3? This is now the highest-priority remaining audit because (a) Route 2.4 is the most likely to close affirmatively given T19/T20's d=3-specific geometry, and (b) it is mostly a re-reading of already-closed work, low effort relative to Route 2.3's primitive-derivation requirements.

2. **Draft Memo NS-1.03 — substrate motif viability + lower bound.** File: `theory/Navier Stokes/NS-1.03_Substrate_Motif_Viability.md`. Two subsections: (a) primitive-level derivation of factorial dilution / concentration of measure — replace the heuristic C(d) ~ 1/d! with a primitive-anchored argument (concentration of measure on participation-measure setup is the cleanest candidate); (b) d ≥ 3 lower bound articulation, citing T20 dipole-mode degeneracy at d = 2 and chain-primitive collapse at d = 1. This is the heaviest single memo in NS-1; it requires actually doing primitive-level work, not just auditing.

3. **Update [`Dimensional_Forcing_B2_Scoping.md`](Dimensional_Forcing_B2_Scoping.md)** to record Route 2.2's closure-failed verdict in §2.2 (route description), §3 (dependency structure), and §6 (risk assessment). Recommended wording: "Route 2.2 audited 2026-04-30 (NS-1.02). T18 forces forward-causal-cone kernel support, which is dimension-agnostic; sharp Huygens is not required by the derivation and Hadamard interior-supported tails are tolerated. Route 2.2 fails: no purely-PDE-level dimensional-forcing route exists in current inventory. Maximum NS-1 concordance is now two-layer (representation + substrate)."

4. **Defer NS-1.01 (Route 2.1 audit)** to last among the four route audits. Route 2.1's PDE↔spinor-bundle inseparability argument is the most structurally uncertain (it may simply not exist as a forcing argument). Recommend tackling it after Routes 2.3 and 2.4 deliver verdicts, so that NS-1's verdict structure is well-determined either way (substrate-level closure secured or not) before investing effort in the most uncertain route.

### Prerequisites and checks

- Confirm `theorems/T19.md` and `theorems/T20.md` contain the substrate-gravity derivations in usable form. If they are index stubs (as T18.md was), work directly from the arc-SG memos and the substrate-gravity paper at [`papers/ED_substrate_gravity_foundations/`](../../papers/ED_substrate_gravity_foundations/).
- Locate ED-Phys-39 if it lives in the repo (a Glob across the repo for "Phys-39" or "Phys_39" before NS-1.03 begins).
- Audit primitive d-agnosticism for P04 (bandwidth-additivity), chain primitive (P02), and participation-measure construction *before* claiming Route 2.3 or Route 2.4 forcing. This audit is small and should be folded into NS-1.03.

### Closure condition for NS-1 after this memo

NS-1 closes when Routes 2.3 and 2.4 deliver verdicts, plus Route 2.1's spinor-bundle propagation argument is either established or explicitly disclaimed. Synthesis (NS-1.05) is the final memo. Route 2.2's closure here is one of the four route verdicts; three remain.

---

*Audit complete. T18 is not a sharp-Huygens forcer. The PDE-level dimensional-forcing route does not exist in current inventory; B2's path to closure runs through substrate-level routes (2.3, 2.4) with the spinor-bundle route (2.1) as a secondary representation-level path.*
