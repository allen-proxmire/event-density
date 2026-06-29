# The Horizon Entropy Coefficient: an Honest Attempt at the 1/4 by Event-Counting

**Foundations — black-hole arc. Target: derive the *coefficient* in the Bekenstein–Hawking entropy S = A/(4ℓ_P²), the famous one-quarter, which ED currently INHERITS rather than derives (GR-III gets the *form* S∝A measured; Paper_025/043 the area law). Prompted by AP: count the commitment-events that form a horizon, match to the Planck-area tiling of the saturation surface, derive the 1/4. Result, honestly tiered: NOT closed, but sharpened to one decidable sub-question, with ED already owning half the coefficient and AP's geometric route a clean candidate for the rest.**

## 1. What the coefficient is, sharply

In Planck units, S_BH = A/4. The horizon carries A Planck areas, and the entropy is a *quarter* of that count. Two equivalent readings:
- **One bit per four Planck areas** of horizon, or
- **the bits tile a surface of area A/4** (a quarter of the horizon).

ED's status: the area law S∝A is **measured** (GR-III: the frozen b→0 horizon's count scales with its perimeter, r_h^0.96; Paper_043). The **coefficient is value-inherited.** That one number is the target.

## 2. Route A — thermodynamic: ED already owns HALF the 1/4

ED's vacuum profile (GR-III) is b = 1 − r_s/r, horizon at r = r_s, and the surface gravity is **derived**:
$$ \kappa = \tfrac12\,\frac{db}{dr}\Big|_{r_s} = \frac{1}{2 r_s}. $$
With the thermal relation T = κ/2π and the first law dM = T dS (and r_s = 2M in G=c=1, so M = r_s/2):
$$ dS = \frac{dM}{T} = 4\pi r_s\, dM = 4\pi r_s \cdot \tfrac12\,dr_s = 2\pi r_s\,dr_s \;\Rightarrow\; S = \pi r_s^2 = \frac{4\pi r_s^2}{4} = \frac{A}{4}. $$
So the 1/4 factors into two pieces:
- the **2 in κ = 1/(2r_s)** — *geometric, and ED-derived* (it comes from the ½ in κ = ½ db/dr and the b = 1−r_s/r profile);
- the **2π in T = κ/2π** — the Hawking/Unruh thermal factor, *which ED inherits*, not yet derived from commitment dynamics.

**ED owns half the coefficient (the geometric 2) and inherits half (the thermal 2π).** To close the 1/4 this way, ED must derive T = κ/2π from the substrate's commitment statistics. That is open.

## 3. Route B — geometric event-counting (AP's route): where the 4 could come from for free

AP's insight: maybe S = A/4 is a *geometric* statement about two surfaces, no thermal factor needed. It is, and exactly:
$$ \frac{A}{4} = \frac{4\pi r_s^2}{4} = \pi r_s^2. $$
And $\pi r_s^2$ is **two** familiar things at once:
- the **great-circle disk** of the horizon (a flat cross-section through it), and
- the **sphere of radius r_s/2** (half the horizon radius — because area ∝ r², half the radius is a quarter the area).

So the **4 is the ratio of a sphere to its great circle**: a sphere has area 4× the disk it bounds ($4\pi r^2 = 4\cdot\pi r^2$). The horizon is the full sphere; the entropy equals the *cross-section*.

This reframes the whole coefficient as a counting question with a clean answer either way:

> **On which surface does ED freeze its independent commitment-states — the full horizon sphere, or its great-circle cross-section (equivalently, the half-radius sphere)?**
> - Full horizon sphere → one state per Planck area → **S = A, coefficient 1** (the holographic bound saturated, but 4× the BH value).
> - Great-circle cross-section / half-radius sphere → **S = A/4, coefficient 1/4** (the Bekenstein–Hawking value, for free, geometrically).

AP's "4× the saturation sphere = the horizon" is exactly the second line, and it is geometrically exact.

## 4. The decisive test (the could-say-no)

This is now a *measurement*, not a philosophy. In the GR-III dynamical-bandwidth simulation, the horizon forms as the frozen b→0 A2-cut. **Count the independent frozen commitment-states on it, and divide by the horizon area** in lattice (Planck-proxy) units. That ratio *is* the coefficient ED's substrate produces:
- if it comes out **1/4**, the coefficient is **derived** — a genuine result (the 1/4 is famously hard; string theory earned it for special black holes in the 1990s and it was a landmark);
- if it comes out **1** (one state per Planck area, full sphere), the substrate tiles the whole horizon and the 1/4 must come from the thermal route (§2), i.e. from deriving T = κ/2π;
- any other value is itself a finding.

The honest prior: ED's count plausibly tiles the *full* b→0 surface (giving coefficient ~1), in which case the 1/4 lives in the thermal factor, not the geometry — but AP's cross-section route is the clean alternative and the sim is what decides between them.

## 5. Status

**Not closed, but sharpened.** ED derives the *form* (S∝A, measured) and the *geometric half* of the coefficient (κ = 1/(2r_s), derived). The full 1/4 reduces to **one decidable question**: does the substrate freeze its independent states on the full horizon sphere (coefficient 1, then the 1/4 is the inherited thermal 2π) or on a great-circle cross-section / half-radius sphere (coefficient 1/4, geometric, AP's route)? **Decisive next step:** count frozen states per horizon area in the GR-III sim and read the coefficient off directly. This is the genuine open target AP's event-counting intuition was pointing at, now stated as a one-run could-say-no.
