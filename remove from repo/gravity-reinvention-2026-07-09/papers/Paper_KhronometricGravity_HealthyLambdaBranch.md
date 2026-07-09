> **REDUNDANCY + CORRECTION NOTE (2026-07-09): this paper largely re-derives, more crudely, what the existing GR-II and KM-I papers already establish.** ED's khronometric gravity AND its MOND sector are already worked in `Paper_KM-I_KhrononMOND.md` (with GR-I/GR-II): MOND IS delivered there, via the nonlinear khronon acceleration function `W(A²)` (the standard Zlosnik-Ferreira-Starkman / Blanchet-Marsat aether-MOND construction), with `a₀ = cH₀/2π` inherited (Paper_029), the deep-IR form forced-given-Paper_030, and the lensing/ghost/PPN kill-checks passed. A same-session probe claiming "the khronometric scalar cannot deliver MOND" was testing the *standard quadratic* action, which KM-I explicitly does not use, and rediscovered the `W(A²)` requirement KM-I already employs; that "MOND not delivered" conclusion is **retracted**. This paper's `λ ∈ [0,1/3)` bound and the `c_T=c` placement may add to GR-II, but the paper should be reconciled with (likely folded into or cited against) GR-II/KM-I rather than standing alone. Read against KM-I, not as an independent MOND verdict.**

---

# ED Gravity Is a Healthy One-Parameter Khronometric Deformation of General Relativity: the Arrow as Preferred Frame, GR-Like Tensor Radiation, a MOND Scalar, and λ ∈ [0, 1/3)

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers, gravity arc (curvature emergence)
**Status:** Publication draft (structural consolidation). Consolidates the *dynamical* half of the ED gravity arc: why ED's emergent gravity is a preferred-frame (khronometric) theory, what that fixes (GR-like tensor radiation, a shared light cone, a scalar that supplies MOND), the form of its effective action, and the computation that bounds its one distinctive parameter λ to the healthy low branch [0, 1/3). Standalone; cold-reader accessible. Companion to the kinematics paper (Relational Gravity: the Emergent Metric) and to Paper_027 (Newton's G).
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **This is not a derivation of exact General Relativity.** ED gravity is a *khronometric* (Lorentz-violating, preferred-frame) theory in the Einstein-aether / Hořava class. It shares GR's spin-2 tensor graviton (so its tensor radiation is GR-like), but it carries an extra scalar (khronon) mode and its metric kinetic structure differs from GR's in the trace sector. The Einstein equation is not derived. ED *reduces to* GR at high acceleration and gives MOND at low acceleration; it is not GR.

2. **The khronometric identification is an account-tier structural argument, not a from-nothing derivation.** The claim "ED has a preferred frame (the arrow, P11), therefore its emergent gravity is Lorentz-violating, therefore it is the khronometric class" is a structural identification with a known, standard, observationally-viable class of gravity theories. It is grounded in an established ED fact (the arrow is a genuine preferred frame), but the passage from "preferred frame" to "this specific effective action" uses the standard effective-field-theory logic for such theories, not a bespoke ED derivation of every coupling.

3. **λ is bounded and signed, not pinned to a decimal.** The result `λ ∈ [0, 1/3)` (natural value 0, and `λ ≠ 1` given ED's positive-energy substrate inertia) is a *structural argument*: the exact decomposition and the three reference values are derived, but ED's placement within the interval rests on the association that the substrate's coherence / participation-velocity channel supplies the kinetic term (see #4). The exact point in [0, 1/3), which would fix the precise scalar-mode speed and the MOND interpolation constant, is not computed here; it needs the mode-resolved conservation inertia and is stated as open.

4. **The coherence-to-kinetic map is an association, honestly flagged.** Identifying the effective action's kinetic term with ED's coherence sector (the reversible participation channel) is organized by a non-canonical source (an older ED cosmology manuscript) and the author's "Relation-Boundary-Gradient" reading of the P12 landscape. It is a useful pointer that locates *which* part of the substrate supplies the inertia; it is not a canonical primitive statement. The canonical source is Paper_087. The one piece of the map that is *verified* (the gradient sector → spatial curvature) is marked as such.

5. **c_T = c is a confirmed consistency, not a tuned fit and not a forced prediction.** A shared photon/graviton light cone (the gravity-sector condition c_13 = 0) is a *separate* condition from the matter-sector universality that evades the dipole; ED's minimal setup makes the shared cone natural, and GW170817 confirms it to 10⁻¹⁵. This is offered as a distinctive consistency (a condition ED finds natural, confirmed by observation), not as a free parameter adjusted to data, and not as a coupling ED derives from first principles (the action that would fix c_13 is unbuilt). Its load-bearing assumption (that ED's universality is exact enough to hold c_T = c to that precision through the radiative sector) is stated.

6. **Values are inherited.** Newton's G, the substrate scale ℓ_P, and the MOND acceleration a₀ are inherited from measurement or from Paper_027; this paper derives forms and bounds, not those numbers.

7. **No new primitive is introduced.** The preferred frame is P11 (the arrow), already primitive.

---

## Abstract

The companion kinematics paper established that a metric emerges from ED's participation graph and is fixed to the weak-field spatial factor `g ~ 1/b` in 3D, with a Gauss's-law Newtonian limit and a MOND-resembling nonlinearity, but a kinematic (acoustic) metric appears not to radiate, which binary-pulsar decay and gravitational-wave inspirals demand. This paper resolves the *dynamical* sector. The resolution turns on one established ED fact: **ED has a preferred frame, the arrow (P11).** An emergent gravity with a preferred frame is Lorentz-violating, and the effective field theory of such a gravity is the **khronometric / Einstein-aether / Hořava class** with the aether four-vector equal to the arrow. This is not a scalar theory: it carries the **spin-2 tensor graviton**, so its tensor radiation is GR-like and matches binary-pulsar orbital decay and LIGO's tensor polarization, plus an extra scalar (khronon) mode. A probe confirms the emergent metric is *not* conformal-only: a non-spherical source develops a genuine traceless spin-2 part (0.000 for a point mass, nonzero and growing with anisotropy for a quadrupolar source), so the point-mass conformal `g ~ 1/b` was a special case and the "scalar-only" reading that motivated an earlier "1/6 falsified" luminosity is retracted (the static probe shows the channel is *present*; its *propagation* as a GR-like graviton follows from the class, not the probe). ED's minimal, universal setup then selects the viable corner, via three *distinct* conditions on *different sectors* (not one mechanism): its universal coupling (equivalence principle, mass = universal bandwidth-influence `Q ∝ M`) structurally kills the scalar *dipole* radiation (the strongest scalar-gravity pulsar test, the one genuinely ED-structural leg); a shared graviton/photon light cone (the separate gravity-sector condition `c_13 = 0`, giving **c_T = c**, consistent with GW170817's 10⁻¹⁵ bound); and small preferred-frame PPN couplings (a third condition, `c_14 → 0`). The dipole evasion is an ED-structural consequence; the shared cone and small PPN are structural conditions ED's minimality makes natural but does not derive (open), so `c_T = c` is a confirmed *consistency*, not a forced prediction. The effective action takes the khronometric form `S = (1/16πG)∫ N√h [K_ij K^ij − λ K² + ξ ³R + η a²]`, and ED's structural conditions give `ξ = 1` (shared light cone) and `η → 0` (equivalence principle), leaving `λ`, the coefficient of `K²`, as the *single* distinctive parameter. We then compute `λ`. The kinetic term decomposes exactly (machine precision) into a shear (spin-2) part and a compression (spin-0, trace) part, and `λ` is nothing but their kinetic-weight ratio, with three derived landmarks: `λ = 0` (compression a normal positive-energy mode, the minimal isotropic substrate), `λ = 1/3` (compression non-dynamical), and `λ = 1` (GR, where compression is a negative-energy conformal ghost, a value *forced* by full four-dimensional diffeomorphism invariance, which a khronometric substrate does not possess). ED's coherence / participation-velocity inertia gives compression and shear equal positive weight, hence the natural value `λ = 0`; bandwidth conservation ties the compression mode to the current, which can only suppress its weight toward `1/3`, never past it into GR's ghost. So **`λ ∈ [0, 1/3)`, natural value 0, `λ ≠ 1` (given ED's positive-energy substrate inertia), the healthy low branch** on which the extra scalar is a well-behaved positive-energy field (the standard khronometric stability window is `λ < 1/3`). The clean unconditional part is that ED is *not forced* to GR's `λ = 1` (a khronometric substrate lacks the 4D diffeomorphism invariance that forces it); the natural value 0 and the `[0, 1/3)` placement are a structural argument resting on a flagged association (that the substrate's coherence channel supplies the kinetic term). Because the shear (tensor) weight is 1 in ED and GR alike, `λ` never touches the tensor sector: ED radiates a GR-like graviton regardless, and `λ` sets only the scalar (khronon) sector, the candidate home for MOND. The honest verdict: **ED gravity is a healthy one-parameter khronometric deformation of GR** with the arrow as its preferred frame, GR-like tensor radiation, a shared light cone (`c_T = c`, consistent with GW170817), a healthy scalar in the sector where galactic MOND would live (that it reproduces MOND is inherited/open), and its one distinctive parameter bounded to `[0, 1/3)`. Open: the exact point in `[0, 1/3)` (needing the mode-resolved conservation inertia), which fixes the precise scalar-mode speed and MOND interpolation constant.

---

## 1. Introduction: the Metric Emerges; Does It Have Dynamics, and of What Class?

The companion kinematics paper answered where ED's geometry comes from: a metric emerges from bandwidth-connectivity, is fixed to `g ~ 1/b` in 3D by the holographic channel-count, obeys a Gauss's-law Newtonian field equation, is relational (lives on graph adjacency), and has a MOND-resembling nonlinearity because the metric is a kinematic read-out of the bandwidth field. That is the *static and linear* story, and it left one sharp tension unresolved: a kinematic (acoustic) metric does not obviously radiate energy as self-propagating spin-2 waves, yet binary-pulsar orbital decay (matched to GR at sub-percent) and gravitational-wave inspirals are *weak-field, radiative* confirmations of dynamical-metric behaviour. This is not deferrable to a strong-field hedge; it is a live weak-field question.

This paper resolves it, and the resolution is not a patch but a reclassification of what *kind* of gravity ED is. One established fact does the work: **ED has a preferred frame, the arrow (P11), the commitment/irreversibility primitive that orders events.** A gravity theory built on an emergent metric that inherits a preferred frame is Lorentz-violating, and Lorentz-violating gravity has a well-developed effective field theory: the Einstein-aether / Hořava / khronometric class, with a dynamical unit timelike vector (the aether) picking out the preferred foliation. Identifying that aether with the arrow places ED in this class. The consequences are specific and largely favourable: such theories carry GR's spin-2 tensor graviton (so they radiate like GR), they admit a shared light cone (so `c_T = c` is natural), and they carry one extra scalar mode whose low-acceleration behaviour is the natural home for MOND.

Section 3 makes the preferred-frame identification. Section 4 shows the emergent metric carries a genuine spin-2 channel (so ED is not a scalar theory). Section 5 shows how ED's minimality places it in the viable radiative corner via three distinct conditions (dipole evasion, `c_T = c`, PPN suppression), only the first of which is ED-structural. Section 6 gives the effective action and reduces it to the single parameter `λ`. Section 7 bounds `λ` to the healthy low branch `[0, 1/3)`. Section 8 gives the honest substrate map behind that bound. Sections 9-11 are limitations, falsifiers, and the position statement.

## 2. Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| ED has a preferred frame (the arrow, P11) | P / established | Paper_087; the arrow is a genuine preferred frame (irreversibility, event ordering) |
| Emergent gravity with a preferred frame is Lorentz-violating → khronometric class | **grounded / identification** | §3; standard EFT of preferred-frame gravity (Einstein-aether / Hořava), aether = arrow |
| Primitive arrow fixes the foliation; the *dynamical* khronon (b-sourced) propagates the scalar | **structural assumption** | §3; a rigid arrow alone would carry no scalar; the emergent b-fluctuation is assumed dynamical |
| The emergent metric carries a genuine spin-2 channel (non-spherical source) | **present (static probe); propagation from the class** | §4; probe: traceless part 0.000 (point mass), nonzero (quadrupolar); static, not a radiative proof |
| Khronometric class radiates a GR-like spin-2 graviton | **inherited (standard result)** | §4-5; the class carries the tensor graviton; tensor radiation GR-like |
| Scalar *dipole* radiation evaded by universal coupling (equivalence principle) | **ED-structural** | §5; mass = universal `Q ∝ M` → scalar dipole ∝ mass dipole, `D̈ = 0`; probe-confirmed |
| `c_T = c` (shared graviton/photon cone, `c_13 = 0`) | **structural condition (gravity sector), confirmed consistency** | §5; a *separate* condition from matter universality; GW170817 confirms 10⁻¹⁵; not derived |
| Preferred-frame PPN parameters suppressed (`c_14 → 0`) | **structural condition, open** | §5-6; a *third* condition; `α_1 = −4 c_14` on `c_13=0`; `c_14`-smallness natural but not derived |
| Effective action form (khronometric) + reduction to one parameter λ | **grounded / account** | §6; `ξ=1` (light cone), `η→0` (equivalence principle), `λ` = the one distinctive coupling; `λ = 1+c_2` on `c_13=0` |
| Kinetic decomposition `K_ij K^ij − λK² = A² + (1/3−λ)K²`; the three λ landmarks | **derived** | §7; exact algebra (trace/traceless orthogonality) + standard DeWitt / Hořava facts |
| GR's λ=1 forced by 4D diffeomorphism invariance; ED *not forced* to it | **derived (non-circular)** | §7; the conformal-ghost value is a covariance artifact ED's substrate lacks; clean unconditional part |
| λ = 0 natural (isotropic participation-velocity inertia) | **structural argument (association)** | §7-8; Coh → kinetic is a non-canonical association (flagged) |
| λ ∈ [0, 1/3), healthy low branch, λ ≠ 1 | **structural argument (on the positive-energy premise)** | §7; natural 0 (association) + `1/3` = fully-constrained endpoint + positive-energy premise; interior open |
| Grad → spatial curvature (³R) | **verified** | §8; probe: `³R = 2∇²b − (5/2)(∇b)²/b`, the gradient content of `b` |
| Exact point of λ in [0, 1/3); precise scalar speed and MOND constant | **OPEN** | §7-8; needs the mode-resolved conservation inertia |
| Exact GR (Einstein equation) | **NOT CLAIMED** | preamble 1; khronometric, not GR |
| `G`, `ℓ_P`, `a₀` values | **inherited** | preamble 6 |

Every step is P, established, inherited, demonstrated, structural, derived, grounded, verified, a flagged association, or explicitly open / not-claimed. No step claims exact GR or a computed decimal for λ.

## 3. The Arrow Is a Preferred Frame, so ED Gravity Is Khronometric

ED's arrow (P11) is the commitment/irreversibility primitive: it orders events, distinguishes past from future, and is not a coarse-graining artifact but a substrate primitive (the reduction program isolates it as the keystone). A preferred temporal ordering is exactly a *preferred frame*: a physically distinguished foliation of the emergent spacetime into "space at a time." Relativity's local Lorentz invariance has no such distinguished foliation; ED's arrow does. So ED's emergent gravity is **Lorentz-violating at the fundamental level**, with local Lorentz invariance an emergent, approximate symmetry of the low-energy sector rather than an exact one.

Lorentz-violating gravity is not exotic; it has a mature effective field theory. Represent the preferred frame by a dynamical unit timelike vector field `u^μ` (the "aether"), normalized `u^μ u_μ = 1`. The most general two-derivative action coupling `u` to the metric is Einstein-aether theory; when `u` is further required to be hypersurface-orthogonal (to define a global foliation, a "khronon" scalar time function `T` with `u_μ ∝ ∂_μ T`), it is khronometric theory, the low-energy limit of Hořava gravity. **ED's arrow is precisely such a global time function**: it is a universal ordering, hypersurface-orthogonal by construction (all observers share the substrate's commitment order). So the natural identification is

$$ u_\mu \;=\; \text{the arrow (P11)}, \qquad \text{ED gravity} \;\in\; \text{the khronometric class.} $$

This identification is account-tier (preamble 2): it is grounded in the established fact that the arrow is a genuine preferred frame, and it uses the standard EFT of preferred-frame gravity rather than a bespoke ED derivation. But it is highly constraining, because the khronometric class has a fixed field content and a fixed set of observational handles, which the rest of this paper works through. The single most important consequence is immediate: **the khronometric class is not scalar gravity.** It carries the same spin-2 tensor graviton as GR, plus one extra scalar. So the "ED gravity is a scalar theory, therefore falsified by pulsars" worry is dissolved at the level of field content, before any calculation.

**Two things must be kept distinct here, and their distinction is load-bearing.** The *primitive* arrow (P11) is a rigid, non-dynamical fact: it fixes that a preferred foliation *exists* and its orientation (the direction of commitment). By itself a rigid background aether would carry no propagating scalar, and then there would be no khronon mode and no MOND sector: a rigid foliation is not enough. What supplies the propagating scalar is the *dynamical* khronon, the emergent time-function whose *fluctuations* are carried by the bandwidth field `b` (the foliation's local rate/shape can vary as `b` varies, exactly the `∂_t b` compression mode of §7). So the identification is really two-layered: the primitive arrow fixes the *existence and orientation* of the preferred frame (the background), and the emergent, `b`-sourced khronon fluctuation is the *dynamical* field that propagates the scalar mode and hosts MOND. This paper treats the dynamical khronon as the fluctuation sector of the emergent foliation carried by `b`; that this emergent khronon is genuinely dynamical (rather than the arrow being purely rigid, which would remove the scalar entirely) is itself a structural assumption of the account, flagged here and revisited in §7 (where the compression mode `∂_t b` *is* that dynamical content) and the falsifiers (§10.1).

## 4. The Emergent Metric Carries a Genuine Spin-2 Channel

The claim that ED carries a tensor graviton must be checked against the emergent metric itself, not merely asserted from the class. The companion paper's `g ~ 1/b` is conformal (`h_ij ∝ δ_ij`, pure trace, spin-0), which *looks* like a scalar theory. But that form was derived only for a *static, spherically-symmetric* source, where isotropy forces the conformal form. A non-spherical source is different: bandwidth then *flows* (a current, not just a density), and the emergent metric can carry a traceless part.

A probe (`spin2_dof_probe.py`) tests this directly. It builds the emergent metric perturbation for sources of varying anisotropy and extracts the traceless (spin-2) component:

- **Point / spherical source:** traceless part `= 0.000` (the conformal special case that motivated the scalar-only misreading).
- **Quadrupolar (binary-like) source:** traceless part nonzero (`+0.005` at the tested anisotropy), growing with source anisotropy.

So the emergent metric is *not* conformal-only: the traceless (spin-2) channel is *kinematically present* for a non-spherical source. This is necessary, not sufficient, for a *radiative* spin-2 degree of freedom: the probe is static (it shows the channel exists), and the *propagation* of that channel as a GR-like graviton follows from the khronometric class identification (§3), not from the probe. What the probe does establish is enough to retire the "scalar-only" reading (a binary's time-varying quadrupole sources a time-varying traceless part, so the metric is not a pure scalar), and with it the earlier "1/6 scalar luminosity, falsified" conclusion, which had dropped the tensor sector entirely (see the companion paper's §6 retraction).

## 5. ED's Minimal, Universal Setup Selects the Viable Corner (Three Conditions, One Naturalness)

The khronometric class is viable only in a corner of its parameter space, bounded by three sharp constraints: no excess (dipole) radiation, `c_T = c` (GW170817), and small preferred-frame effects (PPN). These are *three distinct conditions on different sectors* of the theory, and it is essential not to conflate them: dipole radiation is a *matter-sector* question, the graviton light cone is a *pure gravity+aether* coupling (`c_13`), and the PPN parameters turn on a *further* aether coupling (`c_14`), and `c_13` and `c_14` are independent points in coupling space. ED does **not** derive all three from a single coupling. What ED offers is a *naturalness*: its setup is universal and minimal (the emergent metric is one universal read-out of the bandwidth field `b`, with no independent aether-matter couplings tuned against each other), which makes the minimal corner where all three conditions hold the natural one. Taking the three in turn, and tiering each honestly:

- **Dipole radiation evaded (matter sector, ED-structural).** Scalar gravity generically radiates at *dipole* order, the strongest pulsar killer of scalar-tensor theories. But in ED a mass is a *universal* bandwidth-influence, `Q ∝ M` (all bodies fall alike, because the metric is one universal shadow of `b`, the companion paper's kinematic-metric result), so the scalar dipole moment `D = Σ Q_i x_i = (Q/M) Σ M_i x_i` is proportional to the mass dipole, whose second time-derivative is `d(total momentum)/dt = 0` for an isolated binary. So there is no scalar dipole radiation; the leading scalar multipole is the quadrupole, as in GR (probe: dipole/quadrupole power `~10⁻²²` for universal coupling, reappearing at `~10⁻³` if universality is broken). This is the one leg that is a genuine ED-*structural* consequence: ED passes the strongest scalar-gravity pulsar test because of its equivalence principle.

- **`c_T = c` (tensor-cone condition `c_13 = 0`; a structural condition ED finds natural, confirmed by GW170817).** The tensor graviton's speed equals light's when the aether tensor-sector coupling `c_13 = 0`, i.e. the graviton and photon share a light cone. This is a *gravity-sector* condition, and it does **not** follow from the matter-sector universality that evades the dipole; the two are separate. ED's minimal/universal setup (no relative tilt between the matter and gravity cones) makes the shared cone natural, and GW170817's near-simultaneous gamma-ray and gravitational-wave arrival confirmed `|c_T − c|/c < 10⁻¹⁵`. So this is a *structural condition ED finds natural, confirmed by observation*, a consistency, not a coupling ED derives from first principles (the coarse-grained action that would fix `c_13` is unbuilt). (Load-bearing assumption, preamble 5: ED's universality is exact enough to hold `c_T = c` to that precision through the radiative sector.)

- **PPN suppressed (`c_14 → 0`; a third structural condition, open).** The preferred-frame post-Newtonian parameters `α_1, α_2` encode observable effects of the aether's motion relative to matter; on the `c_13 = 0` slice `α_1 = −4 c_14` (and `α_2` has a related but more complex `c_14`-dependence). The solar-system and pulsar bounds `|α_1| ≲ 10⁻⁴`, `|α_2| ≲ 10⁻⁷` then require `c_14 → 0`, a *third* condition, in the aether sector again. ED's minimality makes small `c_14` natural, but ED does **not** derive it: the smallness of `c_14` is open (§6).

So ED's universal, minimal setup makes the viable corner (`Q ∝ M` universal, `c_13 = 0`, `c_14 → 0`) the natural one, and the sharpest observation (`c_T = c`, GW170817) is consistent with it. This is a *placement by naturalness*, account-tier: only the dipole evasion is an ED-structural consequence; the shared cone and small PPN are separate structural conditions ED finds natural but does not derive. It is not a derivation of the three couplings from one mechanism, and not a computation of exactly where in that corner ED sits, which needs the effective action.

## 6. The Effective Action, Reduced to One Distinctive Parameter

The khronometric effective action, in the preferred foliation with lapse `N`, spatial metric `h_ij`, extrinsic curvature `K_ij`, spatial scalar curvature `³R`, and aether acceleration `a_i = ∂_i \ln N`, is

$$ S \;=\; \frac{1}{16\pi G}\int dt\, d^3x\; N\sqrt{h}\;\Big[\, K_{ij}K^{ij} \;-\; \lambda\, K^2 \;+\; \xi\, {}^3R \;+\; \eta\, a_i a^i \,\Big], $$

with the aether `u` equal to the arrow. GR (in this foliation) is the special point `(λ, ξ, η) = (1, 1, 0)`. ED's structural conditions from §5 point to (they do not *derive*) two of the three couplings:

- **`ξ = 1`** from the shared light cone (`c_13 = 0`, `c_T = c`, consistent with GW170817): the tensor sector matches GR. A structural condition ED finds natural, confirmed by observation, not a derived coupling.
- **`η → 0`** (equivalently `c_14 → 0`): the aether-acceleration coupling, which sources preferred-frame effects, is driven small by the PPN bounds. ED's minimality makes this natural, but its smallness is open (§5), not derived.

That leaves **`λ`**, the coefficient of `K²`, as the *single* distinctive parameter, the one that measures ED's departure from GR. `λ` lives entirely in the scalar (khronon) sector: it sets whether and how the extra scalar mode is dynamical, hence the character of the galactic MOND sector, while the tensor sector (set by `ξ = 1`) radiates like GR regardless. So **ED gravity is, to the extent these two structural conditions hold, a one-parameter khronometric deformation of GR, and that parameter is `λ`.** Bounding it is the subject of §7.

(A note on the two parametrizations, so `λ` is unambiguous. The action above uses the ADM/Hořava `λ` (the `K²` coefficient); the mode-speed and PPN formulas use the Einstein-aether couplings `c_i`. On the relevant slice `c_13 = 0` they are related by `λ = 1 + c_2`, so ED's `λ ∈ [0, 1/3)` (§7) is `c_2 ∈ [−1, −2/3)`, and the ADM healthy branch `λ < 1/3` coincides with the aether no-ghost conditions on the low branch. Note this pins `c_2` to a narrow band, which constrains, and may be in tension with, freely using the residual `c_2` to set the MOND scale `a_0`; that compatibility is open.)

(In the equivalence-principle limit `η → 0`, i.e. aether coupling `c_14 → 0`, the standard scalar-mode speed formula `c_S² = c_2(2 − c_14)/[c_14(2 + 3c_2)]` diverges, so the scalar becomes effectively instantaneous, decoupling from *radiation* while surviving as a *static* field. That is the clean limit: near-pure-tensor, GR-like gravitational waves, plus a static scalar in the sector where galactic MOND would live, with no scalar-wave admixture to over-radiate. The `c_14`-smallness is itself open, and this limit is suggestive, not forced.)

## 7. Computing λ: the Healthy Low Branch, λ ∈ [0, 1/3), Not GR

`λ` is the compression-vs-shear kinetic weighting, and it has an exact handle. Decompose the extrinsic curvature into its trace and traceless parts, `K_ij = A_ij + (1/3) h_ij K`, where `A_ij` is the traceless **shear** (spin-2) and `K` the trace **compression** (spin-0). Then, by exact algebra (this is the orthogonality of the trace/traceless split, true for any symmetric tensor; a probe confirms the identity numerically to machine precision, `6×10⁻¹⁶`, which checks only the algebra, not anything ED-specific),

$$ K_{ij}K^{ij} \;-\; \lambda K^2 \;=\; A_{ij}A^{ij} \;+\; \Big(\tfrac13 - \lambda\Big) K^2. $$

So the shear kinetic weight is `1` and the compression kinetic weight is `w_K = 1/3 − λ`. **`λ` is nothing but the compression-vs-shear weighting**, `λ = 1/3 − w_K`. This gives three derived landmarks, each with a clear physical meaning:

| `λ` | compression weight `w_K` | meaning |
|---|---|---|
| **0** | `+1/3` | compression is a **normal positive-energy mode**, weighted like the shear (the isotropic / identity substrate kinetic term `K_ij K^ij`). Minimal. |
| **1/3** | `0` | compression carries **no** kinetic energy (non-dynamical / fully constrained). |
| **1 (GR)** | `−2/3` | compression is a **negative-energy conformal ghost** (the DeWitt supermetric). |

The load-bearing fact about GR's value: **`λ = 1` is *forced* by full four-dimensional diffeomorphism invariance.** GR's kinetic term is fixed by requiring the action be invariant under all spacetime diffeomorphisms (the Einstein-Hilbert structure), and that requirement makes the trace/conformal mode a negative-norm ghost, rendered harmless by the Hamiltonian constraint. A **khronometric substrate has only spatial diffeomorphisms plus the arrow's preferred time**, not full 4D diffeomorphism invariance, so it is *not* forced to `λ = 1`. `λ` becomes a genuine free parameter set by the substrate's inertia. (This is exactly why Hořava / khronometric gravity carries `λ` as a coupling rather than fixing it to 1.)

ED's placement rests on the substrate inertia, and has three pieces at three different tiers:

- **Derived (non-circular): ED is not *forced* to `λ = 1`.** GR's value is forced by 4D diffeomorphism invariance (above); a khronometric substrate lacks that invariance, so `λ = 1` is not imposed and `λ` is a free parameter. This is clean and does not assume ED differs from GR; it only removes the constraint that would fix `λ = 1`.

- **Natural value `λ = 0` (association-tier).** The kinetic term is supplied by ED's coherence / participation-velocity channel (the reversible participation "velocity" of the substrate; §8, an association). That inertia treats the compression and shear modes alike, giving each a positive kinetic weight with no built-in preference splitting trace from traceless. Equal positive weight is the identity supermetric, `K_ij K^ij`, which is `λ = 0`. So ED's *natural / minimal* value is 0. This is a structural argument resting on the flagged Coh→kinetic association, not a computation.

- **Upper limit `1/3` = the fully-constrained-compression endpoint; the interior is open.** Bandwidth conservation (P04) ties the compression mode `∂_t b` to the current via continuity, `∂_t b + ∇·J = 0`. In the limit where that continuity constraint *fully* removes the compression mode's independent kinetic content, `w_K → 0`, i.e. `λ → 1/3` (the non-dynamical-compression endpoint). So conservation acts in the direction of suppressing the compression weight (0 → 1/3), and the fully-constrained endpoint is `1/3`. The claim that it can only ever suppress (never drive `w_K` negative into GR's conformal ghost) is the *positive-energy-substrate premise*, an assertion (ED's modes are positive-energy), not a theorem; it is what keeps ED off the ghost side. Where in the interior `[0, 1/3)` ED actually sits (how strongly conservation partially constrains the mode) is open.

Combining these:

$$ \boxed{\;\lambda \in [0,\,1/3),\quad \text{natural value } 0,\quad \lambda \neq 1\ \text{given ED's positive-energy substrate inertia}.\;} $$

Three consequences make this a physical result, not a formal one:

1. **The tensor sector is GR-like for any `λ`.** The shear (spin-2) weight is `1` in ED and GR alike; `λ` never touches it. So ED's tensor graviton and its tensor radiation are GR-like *regardless of where `λ` sits in `[0, 1/3)`*. This is why the pulsar and LIGO tensor matches survive the deformation.

2. **`[0, 1/3)` is the *healthy* branch.** The standard khronometric stability result is that the scalar graviton is ghost-free and gradient-stable exactly on the low branch `λ < 1/3` (and on `λ > 1`); the window `1/3 < λ < 1` is unhealthy, and `λ = 1` is GR (scalar non-dynamical). ED's `[0, 1/3)` sits squarely on the healthy low branch, and *not by tuning*: the positive-energy premise plus the conservation-suppression direction are what put it there. So ED's extra scalar (the khronon) is a well-behaved positive-energy field, which is the *candidate* home for the MOND sector; that this scalar actually *reproduces* MOND (rotation curves, baryonic Tully-Fisher) is not shown here and is inherited/open (§10.4).

3. **Not GR (given the premise).** `λ ≠ 1` (on the positive-energy premise) means ED's metric kinetic structure differs from GR's in the trace sector, on the healthy side of it. ED is a genuine deformation of GR, not GR. The clean, unconditional part is weaker but solid: ED is *not forced* to GR's `λ = 1`, so nothing in the khronometric structure requires it to be GR.

**Honest tier (preamble 3).** The decomposition and the three landmarks are derived. "`λ = 0` natural, bounded to `[0, 1/3)`, healthy branch" is a *structural argument* resting on the coherence-to-kinetic association (§8), not a computed decimal. `λ ≠ 1` and the healthy-branch placement are robust given positive-energy substrate modes. The residual, exactly *where* in `[0, 1/3)` (which fixes the precise scalar-mode speed and the MOND interpolation constant), is how strongly conservation suppresses the compression weight, and needs the mode-resolved P04+P05 inertia. That is the one calculation left in ED gravity.

## 8. The Substrate Map Behind the Bound (Honest Provenance)

The `λ` bound rests on a map from the P12 stability landscape `Σ = Coh − Str − Grad` to the effective action, and honesty requires marking which parts of that map are verified and which are association.

Canonical P12 has `a = −∇Σ` (Newton's second law), so **`Σ` is a potential**, and the *kinetic* term (the inertia that makes the geometry radiative) is a separate structure. Organized by the author's "Relation-Boundary-Gradient" reading of `Coh − Str − Grad` and an older, non-canonical ED cosmology manuscript (flagged as an association, not a canonical source, per preamble 4), the map is three-way:

| reading | `Σ` term | effective-action role | status |
|---|---|---|---|
| **Gradient** | Grad | spatial curvature `ξ ³R` | **verified** |
| **Boundary** | Str | potential / mass term | association |
| **Relation** | Coh | the **kinetic** term `K_ij K^ij − λK²` (hence `λ`) | association |

The **verified** piece: the emergent spatial metric is conformal, `h_ij = (1/b)δ_ij`, and its scalar curvature (probe-checked to finite-difference accuracy) is

$$ {}^3R \;=\; 2\nabla^2 b \;-\; \tfrac52\,\frac{(\nabla b)^2}{b}, $$

whose `(\nabla b)^2/b` piece is exactly `Σ`'s **Grad** term (the `∇²b` piece is a boundary total-derivative). So the spatial-curvature term of the action *is* the substrate's gradient penalty. The gradient sector of the map is established.

The **association**: identifying the *kinetic* term (hence `λ`) with `Σ`'s coherence sector is a pointer from the RBG reading and the older manuscript, not a canonical derivation. Its value is that it locates *which* part of the substrate supplies the inertia (the reversible participation channel), which is what sharpens `λ` to the single compression-vs-shear weighting of §7. It also matches that manuscript's finding that the inertial/wave sector dominates near the density ceiling (high acceleration), consistent with "high acceleration → GR/wave regime" (pulsars). But it is an association: the canonical grounding of the coherence kinetic term, and with it the exact point of `λ` in `[0, 1/3)`, is the open work.

## 9. Limitations (honest)

- **Not GR; the deformation parameter is bounded, not pinned.** ED is khronometric, not GR (preamble 1). `λ ∈ [0, 1/3)` is a signed bound with a natural value 0, not a decimal (§7); the exact point needs the mode-resolved conservation inertia and is open.

- **The khronometric identification is account-tier.** "Arrow → preferred frame → khronometric class" is a structural identification with a standard viable class (preamble 2, §3), not a bespoke derivation of every coupling. `ξ = 1` and `η → 0` are structural conditions (§5-6), not first-principles coupling computations; their exact values, and the full BBN / gravitational-Cherenkov fit, need the coarse-grained effective action, which is not built.

- **The coherence-to-kinetic map is an association.** The kinetic sector's identification with `Σ`'s coherence term (§8) is organized by a non-canonical manuscript and the RBG reading. Only the gradient sector (`Grad → ³R`) is verified. Treat the older cosmology manuscript as an association, not a canonical source.

- **`c_T = c` carries a load-bearing assumption.** It is structural and confirmed by GW170817 (§5), but it assumes ED's universality holds to 10⁻¹⁵ through the radiative sector (preamble 5); a radiative detuning of the light cone is not excluded.

- **Values inherited.** `G`, `ℓ_P`, `a₀` are not derived here.

- **Shares the companion paper's layer caveat.** The emergent metric and its spin-2 channel are established in the counting / coarse-grained (layer-2) description; that ED's raw ballistic (layer-1) dynamics coarse-grains to them is attributed, not shown (see the companion paper's §7).

## 10. Falsification Criteria

### 10.1 ED gravity is not khronometric (wrong field content)

**Falsifier sentence:** *A demonstration that ED's emergent gravity does not carry a spin-2 tensor graviton (that the emergent metric has no genuine traceless dynamical channel for a non-spherical source, contrary to §4), or that ED has no preferred frame (contrary to the arrow being a genuine physical foliation), or that ED's khronon is purely rigid (the emergent, b-sourced foliation fluctuation is not in fact dynamical, contrary to the §3 structural assumption, which would remove the scalar mode and the MOND sector entirely), would falsify the khronometric identification and return ED to either a falsified scalar theory or a scalar-less rigid-background theory.*

### 10.2 The light cone is not shared

**Falsifier sentence:** *A gravitational-wave speed differing from `c` beyond the GW170817 bound (`|c_T − c|/c < 10⁻¹⁵`), or a detected scalar-mode (breathing) polarization admixture above LIGO's bounds, would falsify ED's structural `c_T = c` and the equivalence-principle suppression of the scalar radiative sector (§5).*

### 10.3 λ is outside the healthy branch, or is 1

**Falsifier sentence:** *A computation of ED's compression-vs-shear kinetic weighting yielding `λ ≥ 1/3` (the unhealthy window or beyond) would falsify the healthy-low-branch result (§7); yielding `λ = 1` would collapse ED to GR and contradict the khronometric structure (and the observed MOND phenomenology); a negative compression weight (`λ > 1/3` toward a ghost) would falsify the positive-energy-substrate premise.*

### 10.4 The scalar sector does not give MOND

**Falsifier sentence:** *If the healthy scalar (khronon) sector, in its low-acceleration limit, does not reproduce the MOND phenomenology (galactic rotation curves and the baryonic Tully-Fisher relation) but instead requires particle dark matter, the identification of ED's `λ`-sector scalar with the MOND sector (§6-7) is falsified.*

### 10.5 Pulsar decay inconsistent with GR-tensor-dominant radiation

**Falsifier sentence:** *A binary-pulsar orbital-decay rate inconsistent with a GR-tensor-dominant luminosity plus the equivalence-principle-suppressed small scalar-quadrupole correction (an over- or under-radiation outside the viable khronometric window) would falsify ED's placement in that window (§5).*

## 11. Position Statement

**ED gravity is a healthy one-parameter khronometric deformation of General Relativity.** ED has a preferred frame, the arrow (P11), so its emergent gravity is Lorentz-violating and falls in the Einstein-aether / Hořava / khronometric class with the aether equal to the arrow. That class carries GR's spin-2 tensor graviton (the emergent metric develops a genuine traceless part for a non-spherical source, kinematically present in a static probe; its propagation as a graviton follows from the class), so its tensor radiation is GR-like and matches binary pulsars and LIGO. ED's minimal, universal setup selects the viable corner via three *distinct* conditions, not one mechanism: its universal coupling (equivalence principle) structurally evades the scalar dipole catastrophe (the one genuinely ED-structural leg), while a shared graviton/photon light cone (`c_13 = 0`, `c_T = c`, a confirmed consistency against GW170817's 10⁻¹⁵ bound) and small preferred-frame PPN couplings (`c_14 → 0`, open) are separate structural conditions its minimality makes natural but does not derive. The effective action is the khronometric form with `ξ = 1` (light cone) and `η → 0` (equivalence principle), leaving `λ` (the `K²` coefficient) as the single distinctive parameter. Bounding `λ` as the compression-vs-shear kinetic weighting places it on the healthy low branch, `λ ∈ [0, 1/3)`, natural value 0, `λ ≠ 1` given ED's positive-energy substrate inertia (the clean unconditional part being that ED is *not forced* to GR's `λ = 1`, which a 4D diffeomorphism invariance ED's substrate lacks would impose), on which the extra scalar is a well-behaved positive-energy field, the candidate home for galactic MOND (that it reproduces MOND is inherited/open).

**What this paper claims.** The khronometric identification (grounded in the arrow), the spin-2 channel kinematically present (static probe; propagation from the class), the radiative viability with the dipole evaded (ED-structural) and `c_T = c` a confirmed consistency (a structural condition its minimality makes natural), the effective-action form and its reduction to one parameter (grounded), and the bound `λ ∈ [0, 1/3)` on the healthy low branch (derived landmarks + structural placement on the positive-energy premise). Together: **ED gravity is GR at high acceleration and MOND at low acceleration, a healthy Lorentz-violating deformation of GR with a single bounded distinctive parameter.**

**What this paper does not claim.** Exact GR (the Einstein equation is not derived); a computed decimal for `λ` (bounded, not pinned; the exact point is open); first-principles khronometric couplings (`ξ = 1`, `η → 0` are structural conditions, not derived numbers; the coarse-grained effective action is unbuilt); a canonical coherence-to-kinetic map (an association; only `Grad → ³R` is verified); derived values (`G`, `ℓ_P`, `a₀` inherited); or that ED's raw ballistic dynamics reaches these (a layer-2 attribution).

**Series context.** The dynamical companion to the kinematics paper (Relational Gravity: the emergent metric `g ~ 1/b`, Gauss's law, relational character, MOND nonlinearity) and to Paper_027 (Newton's `G`). Where the kinematics paper fixes the geometry and Paper_027 fixes the coefficient, this paper fixes the *dynamical class* (khronometric), its radiative viability (`c_T = c`), and its one distinctive parameter (`λ ∈ [0, 1/3)`). The preferred frame is the arrow the reduction program isolates as the keystone primitive; ED gravity is the shadow that frame casts on the emergent metric.

---

## Appendix: Glossary and Reader Map

### Glossary

- **Khronometric gravity.** The low-energy effective theory of a preferred-frame (Lorentz-violating) gravity, with a global time function (the "khronon") defining a preferred foliation; the hypersurface-orthogonal limit of Einstein-aether theory, and the low-energy limit of Hořava gravity. ED's preferred frame is the arrow (P11).
- **Aether / preferred frame.** A dynamical unit timelike vector `u^μ` picking out "space at a time." In ED, `u^μ` = the arrow, with the §3 caveat that the *primitive* arrow fixes the foliation's existence/orientation (rigid) while the *dynamical* khronon that propagates the scalar mode is the emergent, `b`-sourced fluctuation.
- **Spin-2 tensor graviton.** The two transverse-traceless polarizations of GR's gravitational wave. The khronometric class carries them, so its tensor radiation is GR-like. ED's emergent metric develops the required traceless channel for a non-spherical source (§4).
- **Scalar (khronon) mode.** The one extra propagating mode of khronometric gravity beyond GR's tensor graviton. In ED it is the candidate MOND sector (that it reproduces MOND is inherited/open), and `λ ∈ [0, 1/3)` makes it healthy (positive-energy).
- **`λ` (the compression-vs-shear weighting).** The coefficient of `K²` in the kinetic term; equals `1/3 − w_K` where `w_K` is the compression (trace) mode's kinetic weight relative to the shear. GR is `λ = 1` (a conformal ghost, forced by 4D diffeomorphism invariance); ED is `λ ∈ [0, 1/3)` (healthy, natural value 0).
- **`c_T = c`.** Gravitational-wave speed equal to light speed; a gravity-sector condition (`c_13 = 0`, a shared graviton/photon cone) that ED's minimal setup makes natural, confirmed by GW170817 to 10⁻¹⁵. A consistency, not a coupling ED derives.
- **Universal coupling / equivalence principle.** Mass = universal bandwidth-influence `Q ∝ M`; the emergent metric is one universal read-out of `b`, so all bodies fall alike. This *matter-sector* feature is what structurally evades the scalar dipole. It does *not* by itself give `c_T = c` or small PPN (those are separate gravity-sector conditions, `c_13 = 0` and `c_14 → 0`); ED's minimality makes all three natural, but only the dipole evasion is a direct consequence of the universal coupling.
- **Healthy low branch.** The khronometric stability window `λ < 1/3`, on which the scalar mode is ghost-free and gradient-stable. ED lands here structurally.

### Reader map

*Intuition.* ED has an arrow of time that is real, not emergent, so ED's spacetime has a preferred "now." A gravity built on such a spacetime cannot be exactly Einstein's (which has no preferred now); it is the next thing over, a preferred-frame gravity, and physicists have a well-studied name and toolkit for that: khronometric / Einstein-aether gravity. The good news is that this kind of gravity still has ordinary gravitational waves (the spin-2 graviton), so it passes the pulsar and LIGO tests, and it comes with one extra ingredient, a scalar mode, which is exactly where galactic MOND can live. ED is a *minimal, universal* version of such a gravity, and that minimality makes it land in the small "viable corner" that observations allow. Three separate things have to hold in that corner, and it is worth being precise that they are separate: everything falling the same way (ED's equivalence principle) directly removes the dangerous extra radiation; gravitational waves travelling at the speed of light (which the 2017 neutron-star merger confirmed) is a distinct condition on the gravity sector that ED's minimality makes natural; and keeping the preferred-frame effects tiny is a third such condition. ED does not derive all three from one knob; its minimality makes the corner where all three hold the natural one. The whole theory then comes down to a single number, `λ`, measuring how much the "squeezing" motion of space weighs against the "shearing" motion. GR is *forced* to one value of that number by a symmetry ED does not have; ED is therefore not forced to Einstein's value, and its own inertia and conservation law point to a small healthy range instead, `0 ≤ λ < 1/3`, on the well-behaved side (this last placement resting on how we read ED's inertia, an association, not a bare calculation).

*The distinctive claim.* ED gravity is a healthy one-parameter khronometric deformation of GR: GR-like tensor waves, a shared light cone, and a healthy scalar in the sector where MOND would live (reproduction inherited/open), with its one free parameter bounded to `[0, 1/3)`. It is GR at high acceleration and MOND at low, from one preferred-frame structure.

**Where to look next.**
- *The emergent metric this puts dynamics on:* the kinematics paper (Relational Gravity, `g ~ 1/b`).
- *The coefficient `G`:* Paper_027 (Newton's G).
- *The interference / MOND mechanism in the nonlinear sector:* the P14 / interference-gravity result.
- *The preferred frame as the keystone primitive:* the arrow / minimal-ontology work.

**Open work** (declared): the exact point of `λ` in `[0, 1/3)` (needs the mode-resolved conservation inertia; fixes the precise scalar-mode speed and the MOND interpolation constant); the coarse-grained effective action that would compute ED's khronometric couplings from first principles (rather than fixing them by the structural conditions `ξ = 1`, `η → 0`); and the canonical grounding of the coherence kinetic term (currently an association). The class, the radiative viability, and the one-parameter bound are established; the decimal is the frontier.

---

**End of Paper (Khronometric Gravity).**

*Gravity arc, dynamical companion. ED has a preferred frame (the arrow, P11), so its emergent gravity is Lorentz-violating: the khronometric / Einstein-aether / Hořava class, aether = arrow. This carries GR's spin-2 tensor graviton (the emergent metric develops a genuine traceless part for a non-spherical source, kinematically present in a static probe; propagation from the class), so tensor radiation is GR-like (pulsars, LIGO). ED's minimal, universal setup selects the viable corner via three distinct conditions, not one mechanism: its universal coupling (equivalence principle, `Q ∝ M`) structurally evades the scalar dipole (the one ED-structural leg), while a shared graviton/photon light cone (`c_13 = 0`, `c_T = c`, a confirmed consistency with GW170817) and small preferred-frame PPN (`c_14 → 0`, open) are separate structural conditions its minimality makes natural but does not derive. The effective action is khronometric with `ξ = 1` and `η → 0`, leaving `λ` as the one distinctive parameter. Bounding `λ` (the compression-vs-shear kinetic weighting) places it on the healthy low branch `[0, 1/3)`, natural value 0, `λ ≠ 1` given ED's positive-energy substrate inertia (the clean part being that ED is not *forced* to GR's `λ = 1`, which a 4D diffeomorphism invariance ED lacks would impose). So ED gravity is a healthy one-parameter khronometric deformation of GR: GR at high acceleration, and at low acceleration a healthy scalar in the sector where MOND would live (reproduction inherited/open). Open: the exact point in `[0, 1/3)`. Companion to the kinematics paper and Paper_027.*
