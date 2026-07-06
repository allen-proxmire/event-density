# What the V5 Kernel Actually Forces — Characterization Scoping + a Candidate Reduction

**Status:** Scoping memo, 2026-07-05. **§3's candidate reduction FAILED the cross-check same day (see banner); demoted to a construction program.** Target = the corpus dive's #2 cross-arc open item: the V5 cross-chain kernel (`Paper_090`) is postulated everywhere and derived nowhere.

> **⚠️ Correction (2026-07-05, cross-check catch — the reduction as first written is NOT valid).** §3 claimed: amplitude-carried correlations + P04 normalization + Tsirelson 1980 ⇒ CHSH ≤ 2√2, PR boxes excluded. **Two errors.** (1) **Paper_063 does not construct the needed object**: it builds a joint amplitude $\Psi^{AB}$ with a non-factorizing correction $\Delta^{AB}_{KL}$ and *stops* — no measurement operators, no CHSH correlator as a second moment, Bell content explicitly out of its scope. My §2(b) hedge ("-type content") was correct and §3 then leaned on it as exact structure anyway. (2) **The math step is wrong as stated**: "second moments of a bounded amplitude" does NOT deliver the unit-vector form $c_{ij}=\langle a_i,b_j\rangle$ Tsirelson's vector theorem needs. That form requires the **measurement-operator structure** — Hermitian operators with *exactly* ±1 eigenvalues (the involution $A^2=I$ is what makes the Gram vectors unit-norm) acting across a genuine tensor/commuting split, which is what yields $\mathcal{C}^2 = 4I - [A_1,A_2]\otimes[B_1,B_2]$ and hence $\|\mathcal{C}\|\le2\sqrt2$. Mere boundedness + bilinearity does not: **Grothendieck's constant $K_G$ exists precisely because generic bounded bilinear forms are NOT tight-vector-representable.** So "PR boxes can't be carried, therefore excluded" was not earned. **What survives:** the §4.3 gauge-law moment-signature observation (verified, suggestive, non-probative); the budget/W_max FORM result (§4, independent of the reduction); and the *sharpening* value — P-V5-Hilbert-Constraint is now unpacked into a precise list of what must actually be constructed (below). **What changes:** §3 is a PROGRAM, not a candidate result; nothing goes near `Paper_069`.

**The honest post-correction statement of the open problem** (this is the characterization's real yield): P-V5-Hilbert-Constraint = three named, unconstructed ingredients. To derive the Tsirelson set from the substrate one must build, from ED primitives: **(i)** measurement operators on the joint participation amplitude with an involution structure (±1 eigenvalues — plausibly P11 commitment outcomes, but not constructed); **(ii)** a cross-party commuting/tensor split of those operators (plausibly P10 chain-distinctness + 063's P-Bipartite-Mapping, but not constructed); **(iii)** the identification of the empirically measured correlator with the amplitude second moment (the Born-rule bridge at bipartite level). Given (i)–(iii), Tsirelson follows by standard math; without them, "amplitude-carried" is *consistent with* the Tsirelson set, not a proof of it. Constructing (i)–(iii) is a genuinely hard open problem, now precisely posed — which is more than the corpus had (one opaque postulate), and less than a result.

---

## 1. The question, sharpened

`Paper_069` rests its entire result — Tsirelson ⊊ no-signaling, PR-boxes excluded, "why quantum and not super-quantum" — on one bare postulate:

> **P-V5-Hilbert-Constraint:** "V5 cross-chain correlation kernel enforces the Hilbert-space inner-product structure on bipartite measurement operators, restricting admissible correlations to the Tsirelson set within the no-signaling polytope." *(069 §2.3; audit row 5, label P.)*

"Enforces the Hilbert-space inner-product structure" is a large, vague thing to postulate. The characterization question: **what does the canonical V5 kernel actually supply toward it, and what is the smallest honest residual postulate?**

## 2. What the sources actually give (verified quotes)

**(a) The canonical kernel (`Paper_090` §3.1, §4):**
$K_{V5}(u_A,t_A;u_B,t_B) = \theta(t_A-t_B)\,F_{V5}(\sigma/\ell_{V5}^2,\,\Delta t/\tau_{V5})$ — **bounded** (§4.2, from P04 non-negativity + finite width), **linear** (§4.1), **retarded** (P11 via V1 T18), **Lorentz-scalar** (§4.4), and — the underused fact — **gauge-covariant with a relative phase** (§4.3):
$$K_{V5} \to e^{i(\alpha(u_A)-\alpha(u_B))} K_{V5}.$$
Envelope shape and all $\tau_{V5}$ values: inherited, not predicted (§3.3, §7.1–7.2).

**(b) The correlations are amplitude-carried (`Paper_063` §1.1):** "when $C_A$ and $C_B$ share substrate-level cross-chain participation amplitude via V5 (Paper_090), the **joint amplitude** is not expressible as a tensor product…" — i.e. the corpus already commits (under its declared P-Bipartite-Mapping) to V5-mediated correlation being the correlation OF a joint participation amplitude $\Psi^{AB}$, with per-chain amplitudes $\Psi^A=\sum_K P_K^A|K\rangle_A$ etc.

**(c) Normalization:** P04/Born structure fixes $b_K=|P_K|^2$ with bounded total bandwidth (U1/U2 chain; `Paper_002` Born rule as used by 069 audit row 2).

## 3. The candidate reduction — **RETRACTED as a result; kept as the program statement (see ⚠️ banner)**

**Claim (candidate):** P-V5-Hilbert-Constraint reduces to one sharper, substrate-native postulate plus standard math:

> **P-V5-Carried (proposed):** every V5 cross-chain correlation is a **second moment of the joint participation amplitude** — $\langle X^A Y^B\rangle_{V5} = \langle \Psi^{AB}|\,\hat X_A \hat Y_B\,|\Psi^{AB}\rangle$-type content, per 063's joint-amplitude commitment; there are no V5 correlations that are not carried by participation content.

**Given P-V5-Carried + P04/Born normalization, the Tsirelson set follows by standard math, with no further postulate:**

1. Any family of correlations that are second moments of a common amplitude has a **positive-semidefinite Gram structure**: writing the correlators as $c_{ij} = \langle a_i, b_j\rangle$ for vectors $a_i, b_j$ in the amplitude space, with $\|a_i\|,\|b_j\| \le 1$ enforced by the P04/Born normalization (bounded bandwidth ⇒ bounded operator content).
2. **Tsirelson's theorem (1980, standard, legitimately inherited):** correlations expressible as inner products of unit-norm vectors satisfy CHSH $\le 2\sqrt 2$; conversely the quantum set realizes exactly these. So the substrate correlations land **in the Tsirelson set**.
3. **PR-box exclusion becomes a theorem, not a decree:** a PR box has CHSH $=4 > 2\sqrt2$, hence is **not representable as inner products of bounded vectors** — i.e. it is provably NOT the second moment of ANY amplitude. Under P-V5-Carried, it therefore cannot occur: not because a rule forbids it, but because **there is nothing that could carry it.**

**Evidence that the canonical kernel is a moment-type object (source-grounded, the §4.3 hook):** a real, gauge-*invariant* joint correlation would transform trivially under local $U(1)$ rotations. The canonical $K_{V5}$ instead transforms as $e^{i(\alpha_A-\alpha_B)}$ — exactly the transformation law of a conjugated-pair second moment $\langle X_A^{\*} X_B\rangle$ (sesquilinear in the two chain slots). The kernel's own declared gauge law is the signature of amplitude-moment structure. This does not *prove* P-V5-Carried, but it means the canonical kernel is already shaped like the object the reduction needs — the postulate names a property the source structure visibly has, rather than inventing one.

**What the reduction buys, stated honestly:**
- FROM: "V5 enforces Hilbert-space inner-product structure" (opaque, math-flavored, un-substrate-like).
- TO: "V5 correlations are **carried** — they are moments of actual shared participation content" (substrate-native, one sentence, physically meaningful) + Tsirelson 1980.
- The "why quantum, not super-quantum" answer becomes an ED-ontology statement: **super-quantum (PR-box) correlations are correlations without a carrier.** ED's substrate is relational — a correlation IS shared participation content — and any carried correlation is Gram/PSD, hence Tsirelson-bounded. The substrate doesn't *forbid* PR boxes; it has no way to *instantiate* them.

**Cross-link (real, not decorative):** this is the same shape as the measured **A1 common-cause result** (`Paper_CommonCauseNotChannel_A1`): ED correlations are common-cause/carried, never free-floating channel content. A1 measured the carried-ness at the classical/capacity level; P-V5-Carried is its amplitude-level sibling. One ontology, two faces.

## 4. The budget face (SCBU / M_crit / monogamy) — what the kernel already forces

- **Budget FORM:** P04 (bandwidth non-negative, **additive**) + the canonical envelope's boundedness (§4.2) jointly force that total V5 cross-chain weight over any chain's partners is **finite and additive** — the *form* of `Paper_065`'s P-V5-Budget ($W_{\max}$ exists). The *value* $W_{\max}$ stays inherited. So half of the monogamy postulate is already in the canonical kernel; only the number is not.
- **SCBU/M_crit anchor:** the q-compute $N_{V5}$ constituent (M_cap = min(N_bw, N_V5, N_commit), `Paper_053`) and the SCBU multiplicity projection anchor to exactly this finite-additive-budget form. The characterization grounds the *form* of that constituent in P04 + the canonical envelope; the threshold values stay inherited, as SCBU already states.
- **Monogamy:** the same PSD/moment structure underlies known quantum monogamy tradeoffs (standard literature); under P-V5-Carried, monogamy-type constraints inherit the same way the Tsirelson bound does. *(Deliberately no specific inequality cited here — to be added only after checking the exact form against the literature; flagged for the cross-check.)*

## 5. What stays open (the honest residue)

1. **P-V5-Carried is a postulate, smaller but real.** It is NOT derived from P02/P04; it is the ED ontology ("correlations are shared participation") stated as a kernel property. Whether it reduces further is open — and it inherits the **Paper_004 channel-orthogonality gap**: the single-chain inner product's physical-contextuality half is still partially postulated, and the bipartite moment structure sits on top of that chain (U2 → 063 P-Bipartite-Mapping → here). No claim that this closes target A3.
2. **Schmidt-genericity (064's P-V5-Schmidt-Generic)** needs the actual bilocal content $\mathcal{Q}^{AB}$ constructed, which `Paper_090` leaves unspecified (§3.1's integrand is named, not built). The reduction does not touch it.
3. **The dynamics face (HM-Q2/RL-Q2 stress-energy forms)** is a different aspect of "what V5 forces" — untouched here; scope separately.
4. **Envelope shape and all $\tau_{V5}$ values** — inherited, per 090's own §7; nothing here changes that.

## 6. Tier summary

| Claim | Tier |
|---|---|
| Canonical V5 = bounded/linear/retarded/Lorentz/gauge-phase-covariant | SOURCE (090 §3–4, quoted) |
| Correlations amplitude-carried via joint $\Psi^{AB}$ | SOURCE (063 §1.1, under its declared P-Bipartite-Mapping) |
| §4.3 gauge law = sesquilinear-moment transformation signature | STRUCTURAL observation (verified against the formula; suggestive, not probative) |
| **P-V5-Hilbert-Constraint ⟸ P-V5-Carried + P04/Born normalization + Tsirelson 1980** | **CANDIDATE reduction** (standard math legitimately inherited; the residual postulate named and smaller) |
| PR boxes = carrier-less correlations (cannot be any amplitude's moment) | D-conditional on P-V5-Carried (standard math) |
| Budget/W_max FORM from P04 additivity + envelope boundedness | STRUCTURAL (form only; value inherited) |
| "Why quantum not super-quantum" = "correlations must be carried" | ACCOUNT (the ED reading of the reduction) |

## 7. Next steps

1. **Cross-check first** (the session pattern has earned it): verify (a) Tsirelson's-theorem usage (inner-products-of-unit-vectors ⇒ CHSH ≤ 2√2 — Tsirelson 1980; believed solid), (b) that the Gram/PSD argument as sketched carries through for the ±1-observable CHSH setting with the P04 normalization doing the unit-norm work, (c) the monogamy-literature citation before adding any inequality.
2. If it survives: fold into `Paper_069` as a **split of audit row 5** — P-V5-Hilbert-Constraint → P-V5-Carried (P, smaller) + D-via-I steps (Gram/PSD, Tsirelson 1980) — and update 069's preamble item 3, which currently disclaims any substrate-level "why not PR-boxes" answer; under the reduction there IS one, at ACCOUNT tier: *no carrier, no correlation.*
3. Then the deeper question this sets up properly: **can P-V5-Carried itself be derived** from P02 (participation as primitive relation) — "all correlation is participation content" reads like a restatement of P02's ontology; if that identification can be made precise, the Tsirelson result upgrades from postulate-conditional to primitive-conditional. That is the real prize, and it should not be attempted until the cross-check clears the reduction.
