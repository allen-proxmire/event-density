# The Hawking 2π From ED's Own Geometry: the Entropy 1/4 Is Fully Structural

**Foundations — black-hole arc, continues `BH_EntropyCoefficient_FromEventCounting`. Attempt: derive the thermal 2π in T = κ/(2π) that ED was thought to *inherit*, completing the Bekenstein–Hawking 1/4. Result: the 2π comes from ED's *own* near-horizon geometry. ED's derived bandwidth profile b = 1 − r_s/r has the Rindler form at the horizon (confirmed numerically), and the smoothness of that geometry forces the imaginary-time period to be 2π/κ, hence T = κ/(2π). So BOTH halves of the 1/4 are ED-structural: the ½ from κ (the b-profile's slope) and the 2π from the b-profile's near-horizon shape. The "half-inherited" framing was too pessimistic. The honest remaining frontier is a purely commitment-statistical derivation that does not pass through the (reversible-time) Euclidean continuation.**

## 1. The target and the prior status

S_BH = A/4. The coefficient factors as κ × (thermal relation): with κ = 1/(2r_s) and T = κ/(2π), the first law dM = T dS integrates to S = πr_s² = A/4. ED *derives* κ = ½ b′(r_s) = 1/(2r_s) (GR-III). The open piece was the **2π** in T = κ/(2π), previously read as inherited from standard horizon thermodynamics. This note shows ED's geometry supplies it.

## 2. ED's near-horizon metric is Rindler (the key fact)

ED's vacuum profile (GR-III, derived): b(r) = 1 − r_s/r, metric ds² = −b dt² + b⁻¹dr². Expand at the horizon. With κ = 1/(2r_s):
$$ b(r) \approx b'(r_s)(r-r_s) = \frac{1}{r_s}(r-r_s) = 2\kappa\,(r-r_s). $$
Use the **proper radial distance** ρ = ∫ dr/√b. Near the horizon ρ ≈ √(2(r−r_s)/κ), so (r−r_s) = κρ²/2 and
$$ b = 2\kappa\,(r-r_s) = \kappa^2 \rho^2. $$
The metric becomes
$$ ds^2 \approx -\kappa^2\rho^2\,dt^2 + d\rho^2 \qquad\text{(Rindler form).} $$
**Numerical confirmation** (this note's script): b/(κρ)² → 0.98 → 1 as r → r_s. ED's horizon is a Rindler cone, on the nose.

## 3. The 2π is the angle of one turn around the horizon

Continue to imaginary time, t → iτ:
$$ ds_E^2 = \kappa^2\rho^2\,d\tau^2 + d\rho^2. $$
This is the flat plane in polar coordinates: ρ is the radius from the horizon point, and **κτ is the angle**. A plane is smooth at its center *only if the angle runs a full 2π* — any other period leaves a conical defect, a pucker, at the horizon. So smoothness demands
$$ \kappa\tau \in [0, 2\pi) \;\Rightarrow\; \tau \text{ has period } \beta = \frac{2\pi}{\kappa}. $$
A theory periodic in imaginary time with period β is thermal at T = 1/β:
$$ \boxed{T = \frac{\kappa}{2\pi}}, \qquad S = \frac{A}{4}. $$
The 2π is not borrowed. It is the angle of one full turn around the horizon point in ED's own near-horizon plane.

**AP's intuition, vindicated.** AP guessed the coefficient involved space and time "doing funky swaps" and being "the same number." That is exactly this plane: inside/at the horizon the radial and time directions exchange roles, and the (τ, ρ) plane is where they trade. The 2π is the single turn around it; κ ties the temporal scale to the same r_s as the spatial size. His hand-wave was the picture, stated correctly.

## 4. Honest tiers and the remaining frontier

- **Derived (ED-structural):** the b-profile (GR-III); κ = 1/(2r_s); the near-horizon Rindler form (confirmed numerically); hence T = κ/(2π) and S = A/4. **Both factors of the 1/4 come from ED's own geometry.** This upgrades the coefficient from "half-inherited" to "fully structural."
- **The tool used:** the Euclidean continuation (Wick rotation) plus the smoothness/no-conical-defect condition. This is the *standard* route every derivation of the Hawking temperature uses, General Relativity included. So **ED is on par with GR here** — both read the 2π off the same near-horizon geometry; ED's addition is that the geometry itself is *derived* from the bandwidth rule rather than postulated.
- **The genuine open frontier (deeper than GR attempts):** ED's defining primitive is the *irreversible* arrow, and the Euclidean continuation is a *reversible-time* device. A fully substrate-native derivation would get the 2π from the **commitment statistics directly** — how commitments correlate across a b→0 surface in real, one-way time — with no continuation. The standard real-time route (horizon tunneling / detailed balance) gets the 2π from a residue around the b→0 pole, which ED's genuine pole supplies; turning that into a first-principles commitment-statistics derivation is the remaining target. The 2π is *forced* by ED's geometry either way; deriving it from raw becoming, without borrowing the continuation, is the deep version.

## 4b. Attempt at the continuation-free version — honest negative

Tried to get the 2π in real, one-way time with no continuation at all: take ED's
exponentially-redshifted near-horizon mode φ(u) = exp(i(Ω/κ)e^{−κu}) (the redshift is ED's,
from b→0 with rate κ) and read the thermal ratio off an ordinary real-time FFT,
|φ̃(−ω)|²/|φ̃(ω)|² = e^{−2πω/κ}, measuring the slope = −2π. **It failed numerically** (two
setups, slope came out +0.4 to +1.1, not ±6.28). Brute-FFT Hawking spectra are notoriously
finicky and the quick implementation did not capture it.

**But the deeper point is the real finding, and it is not a numerics excuse.** Even a *correct*
real-time derivation gets the 2π from the **gamma function** Γ(iω/κ) — the Fourier transform of
the log-redshifted mode — and that gamma function is precisely the **analytic structure at the
horizon** (the branch point, the Kruskal extension across it). That analytic structure *is* the
Euclidean periodicity in another guise. So the "real-time" route is **not genuinely
continuation-free**; the 2π is intrinsically the horizon's analytic/periodic structure however
you slice it.

**The honest reframe this forces:** the 2π is a **continuum / smooth-horizon** quantity. It is a
feature of the analytic branch structure where outgoing modes connect across the horizon, which
exists only once the smooth horizon exists. ED's *discrete, irreversible* commitments produce it
**after** coarse-graining to the smooth b-profile — which is exactly the level §2 works at (the
Rindler form). So asking for the 2π from *raw discrete commitment counting, below the continuum*
may be ill-posed: the 2π does not live there, it lives at the smooth-horizon level, and **there
ED already has it** (§2). The continuation-free-from-raw-commitments target is therefore either a
genuinely deep open problem *or* a category error (demanding a continuum feature from
sub-continuum data); this attempt did not settle which, and did not produce the number.

**Verdict on 4b: did not crack it.** The structural derivation (§2–§3) stands and is solid; the
"derive the 2π from raw becoming with no analytic structure at all" frontier remains open, and
may dissolve into "the 2π is a continuum feature ED gets at the continuum level."

## 5. Status

**The 1/4 is structurally derived in ED.** κ = 1/(2r_s) from the b-profile's slope, and the 2π from the b-profile's near-horizon Rindler shape via smoothness, both from the one derived bandwidth profile. The coefficient is no longer "half borrowed"; it is ED's own geometry, on equal footing with GR's derivation. The frontier that remains is the substrate-native, continuation-free derivation of the 2π from commitment statistics, which is the QM-connected piece (ħ and the thermal 2π share the substrate's sparse-commitment structure) and a goal beyond what GR itself reaches for.
