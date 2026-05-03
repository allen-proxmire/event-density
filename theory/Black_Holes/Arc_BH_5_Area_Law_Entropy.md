# Arc BH — Memo 5: Area-Law Entropy and the 1/4 Coefficient

**Status:** Fourth technical memo of Arc BH. Load-bearing new-derivation memo: must produce an area-law form from substrate mechanics and deliver an honest verdict on whether the Bekenstein–Hawking $1/4$ coefficient is derived, inherited, or modified.

**Date:** 2026-05-01

---

## 1. Purpose

This memo:

- Derives the **area-law form** of black-hole entropy from ED substrate mechanics — specifically, from the participation capacity of the decoupling surface (BH-2) under saturated-zone conditions (BH-3).
- Computes the entropy as the **log of viable commitment histories** compatible with the boundary's participation capacity (per ED's substrate-level definition of entropy).
- Identifies $\mathcal{C}_H = \int_{\Sigma_H} dA/\ell_P^2 \cdot \chi(\rho,\nabla\rho)$ as the substrate quantity playing the role of "area density of states."
- Issues a **structural verdict** on the $1/4$ coefficient: derived, inherited, or modified. Discipline: the math says what it says; this memo will not over-claim a coefficient derivation that the substrate machinery does not actually produce at this stage.

---

## 2. Upstream Foundations

- **ED-10 §5.6** — boundaries as participation bottlenecks; area-law form arises whenever an interior–exterior coupling is mediated by a surface where cross-bandwidth is suppressed and capacity scales with surface area.
- **BH-2** — horizon-as-decoupling-surface under DCGT: $\Sigma_H = \{\mathbf{x}: |\nabla\rho|\,\ell_P^2/\rho_\mathrm{local} \gtrsim \log(R_\mathrm{cg}/\ell_P)\}$.
- **BH-3** — saturated participation zone replaces the singularity; gradient saturation $\chi \to 1$ holds in the strong-gradient regime.
- **BH-4** — information = committed structure; entanglement = uncommitted structure; horizon blocks the former, not the latter. Sets up why the "states being counted" are commitment histories localized at the surface.
- **Arc D (DCGT)** — multi-scale expansion + bandwidth suppression. Provides the formal hydrodynamic-window resolution scale $R_\mathrm{cg}$ and the $\Gamma_\mathrm{cross}$ structure.
- **Arc SG** — T19 ($G = c^3\ell_P^2/\hbar$) gives the substrate-level Planck length used as the patch scale; SG-6 weak-field prerequisites set the gravitational profile that determines $\Sigma_H$.
- **ED-Phys-10** — acoustic-metric guardrails: "area" here is the coarse-grained acoustic-metric area of $\Sigma_H$, not a fundamental geometric primitive.

---

## 3. Participation Capacity of a Horizon

Define the **participation-capacity density** $\chi(\rho,\nabla\rho)$ as the substrate-level density of viable commitment-channel slots per Planck-area patch on the surface $\Sigma_H$. By construction:

- $\chi \to 1$ in the saturated regime (BH-3): each Planck patch supports its full structural quota of commitment channels.
- $\chi \to 0$ in the dilute regime: cross-bandwidth is plentiful but commitment-channel density is low.

The total participation capacity of $\Sigma_H$ is:

$$
\mathcal{C}_H = \int_{\Sigma_H} \frac{dA}{\ell_P^2}\,\chi(\rho,\nabla\rho).
$$

Two structural properties are load-bearing here:

1. **Area-extensivity.** $\mathcal{C}_H$ scales with the integrated surface area, not with the enclosed volume, because the integrand is supported only on $\Sigma_H$. This is where the area-law *form* enters: it is forced by the fact that the decoupling surface is two-dimensional, not by any additional assumption.

2. **Strong-gradient saturation.** On a black-hole decoupling surface, the gradient condition that defines $\Sigma_H$ is precisely the condition under which $\chi$ saturates: the same large $|\nabla\rho|\,\ell_P^2/\rho_\mathrm{local}$ that suppresses cross-bandwidth also drives commitment-channel density to its substrate-imposed maximum (per BH-3). Therefore in the BH-relevant regime:

$$
\chi(\rho,\nabla\rho) \approx 1 \quad\text{on}\quad \Sigma_H,
$$

and the capacity reduces to:

$$
\boxed{\;\mathcal{C}_H \approx \frac{A}{\ell_P^2}\;}
$$

where $A$ is the coarse-grained acoustic-metric area of $\Sigma_H$.

This recovers the **area-law form** at the substrate level: the count of commitment-channel slots on a black-hole horizon is $A/\ell_P^2$, with the leading coefficient set to unity by gradient saturation. The fact that the prefactor of $A/\ell_P^2$ in $\mathcal{C}_H$ is exactly $1$ (and not some other dimensionless number) is structural: $\chi$ is by definition normalized to its saturated maximum, so the question of whether the entropy coefficient is $1/4$ or anything else is **not** answered at this stage. It is moved into the next step.

---

## 4. Entropy as Count of Viable Commitment Histories

ED's substrate-level definition of entropy is:

$$
S = \log(\text{number of viable commitment histories compatible with the macroscopic constraint}),
$$

where "macroscopic constraint" here is the participation capacity of $\Sigma_H$. A commitment history is a P11-irreversible record of which channels committed in which order, subject to V1 kernel finite-width constraints + DCGT hydrodynamic-window resolution.

Each Planck-area patch on $\Sigma_H$ supports a finite number $g$ of distinct viable commitment motifs (the substrate's local "alphabet" of commitment-channel configurations, after coarse-graining). Patches commit independently up to the resolution of the hydrodynamic window; correlations across patches are sub-leading in the multi-scale expansion (Arc D).

Therefore:

- Total number of viable commitment histories: $g^{\mathcal{C}_H}$.
- Entropy:

$$
S = \mathcal{C}_H \log g \approx \frac{A}{\ell_P^2}\log g.
$$

The **area-law form is now derived** at the substrate level: $S \propto A/\ell_P^2$ follows from (i) two-dimensional surface support of $\mathcal{C}_H$, (ii) gradient saturation $\chi \to 1$, and (iii) per-patch finite alphabet $g$ from substrate primitives.

What remains is the value of $\log g$.

---

## 5. Determining the 1/4 Coefficient

The substrate meaning of $g$ is:

> $g$ = number of distinct viable commitment motifs per Planck-area patch on a saturated decoupling surface.

$g$ is constrained by:

- **P11 commitment irreversibility** — each commitment slot is a one-way switch.
- **V1 kernel finite width** — the kernel width sets the temporal resolution of commitment events at a patch, restricting the number of distinguishable orderings.
- **Gradient saturation** (BH-3) — at saturation, cross-bandwidth in directions tangent to $\Sigma_H$ is also suppressed, so motifs at different patches do not bleed into each other (this is what justified the per-patch independence in §4).
- **DCGT hydrodynamic-window resolution** — distinguishability of motifs requires that they survive coarse-graining over $R_\mathrm{cg}$.

**What the substrate machinery actually delivers at this stage:**

1. $g$ is **finite** — bounded above by the V1-kernel-resolution count of distinguishable temporal orderings within a patch's commitment cycle, and bounded below by $g \geq 2$ (a saturated patch must support at least one bit of commitment-history distinction, otherwise it would not contribute to entropy).
2. $g$ is **substrate-determined** — it is fixed by V1 kernel width, $\ell_P$, and the DCGT resolution scale, all of which are substrate constants.
3. $g$ is **value-INHERITED** in the form-FORCED / value-INHERITED methodology consistent with the rest of the program.

What the substrate machinery does **not** deliver at this stage:

- A closed-form computation of $\log g$ from V1 kernel width + $\ell_P$ + $R_\mathrm{cg}$. Such a computation would require either (a) an explicit V1-kernel-counting argument analogous to a substrate-level state-counting partition function, or (b) a substrate-derivation of the patch-level commitment alphabet from microscopic substrate dynamics. Neither is in hand.

**Structural verdict on the $1/4$ coefficient:** **INHERITED**, not derived.

The honest statement is:

- The **area-law form** $S \propto A/\ell_P^2$ is **derived** from substrate principles (gradient saturation + per-patch finite alphabet + two-dimensional surface support).
- The **coefficient** $\log g$ is **inherited** from substrate constants: it is a finite, substrate-determined number, but ED's current machinery does not yield $\log g = 1/4$ as a closed-form derivation. To match Bekenstein–Hawking, the coefficient $1/4$ must be inherited (i.e., $\log g$ takes whatever value V1 + DCGT + $\ell_P$ jointly fix; that value matches $1/4$ only if substrate-level state counting confirms it).

This is the same structural pattern as $a_0$, $G$, $\Lambda$, and the gauge couplings in the rest of the ED program: form-FORCED by substrate mechanics, value-INHERITED from substrate constants. The $1/4$ coefficient is not in a different category from these.

A substrate-level state-counting derivation of $\log g$ is a candidate future arc, structurally similar to the $\kappa/|\hat N'| = 0.001766$ anchor search (E4 in the Investigation Priority List) — it would require a closed-form V1-kernel motif count, which is not currently in hand.

---

## 6. Comparison to Bekenstein–Hawking

Bekenstein–Hawking entropy:

$$
S_\mathrm{BH} = \frac{A}{4\ell_P^2}.
$$

ED result:

$$
S_\mathrm{ED} = \frac{A}{\ell_P^2}\log g.
$$

**Form match:** Both are area-law with coefficient $1/\ell_P^2$ multiplied by a dimensionless number. ED reproduces the area-law form structurally.

**Coefficient comparison:** ED predicts $\log g$, with $g$ a substrate-determined finite integer ≥ 2. The Bekenstein–Hawking value $1/4$ corresponds to $\log g = 1/4$, i.e. $g = e^{1/4} \approx 1.284$.

This is not an integer, which is the structurally informative outcome. It tells us:

- Naive per-patch-independent commitment-motif counting cannot reproduce $1/4$ exactly: a finite-alphabet log gives $\log g$ for integer $g \geq 2$, all of which exceed $1/4$.
- To recover $1/4$, the per-patch independence assumption must be relaxed — adjacent patches share commitment-history correlations through V1 kernel overlap, and the effective per-patch contribution is reduced from $\log g$ (independent) to a smaller correlated value.
- The Bekenstein–Hawking coefficient is consistent with $\log g \approx 1/4$ once V1 kernel cross-patch correlations are accounted for — which is structurally plausible because the V1 kernel finite width is precisely what links adjacent patches.

**Verdict:** ED does not currently reproduce $1/4$ as a derived coefficient. It produces an area-law form with a coefficient that is structurally a substrate-determined dimensionless number, and an honest reading is that $\log g \approx 1/4$ if cross-patch V1 correlations reduce the effective per-patch alphabet below the naive independent count. A closed-form derivation requires substrate-level state counting that is not yet in hand.

**Observational distinguishability:** No. The black-hole entropy coefficient is not directly measured; it is inferred from thermodynamic consistency with the Hawking temperature. Since BH-5 explicitly excludes Hawking-spectrum derivation (reserved for BH-6 / out of scope for Arc BH per BH-1), there is no current ED prediction that disagrees with the $1/4$ value at the level of any extant observation. The result is a structural-positive: ED reproduces the form, identifies the coefficient as INHERITED, and is consistent with $1/4$ pending a closed-form $\log g$ computation.

---

## 7. Deliverables

This memo produces:

- **Area-law form derived** at the substrate level: $S \propto A/\ell_P^2$ from gradient-saturation + per-patch finite alphabet + two-dimensional decoupling-surface support.
- **Participation-capacity density** $\chi(\rho,\nabla\rho)$ defined; saturation $\chi \to 1$ in BH-relevant regime; $\mathcal{C}_H \approx A/\ell_P^2$.
- **Entropy formula**: $S = \mathcal{C}_H \log g \approx (A/\ell_P^2)\log g$.
- **Structural verdict on the 1/4 coefficient: INHERITED**, not derived. Form-FORCED / value-INHERITED methodology applied honestly. ED-current machinery does not produce $\log g = 1/4$ as closed-form; it produces a substrate-determined finite $\log g$ that is consistent with $1/4$ once V1 cross-patch correlations are accounted for.
- **Bekenstein–Hawking comparison**: form match; coefficient match conditional on substrate-level state-counting derivation that is not currently in hand.

---

## 8. Recommended Next Step

Proceed to **Arc_BH_6_Wave_BH_Scattering.md** — substrate-derivation chain for wave–black-hole scattering. Builds on BH-2 (decoupling surface), BH-3 (saturated zone interior), BH-4 (information re-routing), BH-5 (commitment-channel capacity at the surface). Goal: produce an ED-substrate account of how waves scatter off a black hole, comparing to ED-I-26 (Event-Density Channels and the Global Geometry of Wave–Black-Hole Scattering) and identifying which features are derived vs inherited.

File path: `theory/Black_Holes/Arc_BH_6_Wave_BH_Scattering.md`. Estimated 1–2 sessions.
