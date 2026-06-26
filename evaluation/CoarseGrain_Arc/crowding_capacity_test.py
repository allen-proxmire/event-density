"""The crowding/capacity test: does mobility degenerate as the medium fills toward
capacity -- i.e., does the substrate reproduce M(rho) dying at rho_max (the UDM)?

The certified rule penalizes moving INTO dense cells (sigma.py: strain = rho_v). So there
IS a density response, but it needs CONTRAST to act (a uniform background cancels it -- why
the previous test came out flat). Crowding makes the contrast: a localized packet of fronts
deposits rho into its own core, and we watch whether the packet's spreading SLOWS as the
core density it creates rises toward capacity.

  - packet spread R(t) DECELERATES (alpha drops) as core density -> capacity: mobility
    degenerates with density = the UDM M(rho)=(rho_max-rho)^beta read off the substrate.
  - R(t) stays ballistic / speeds up as the core fills: NO degenerate mobility -- the
    strain term drives density-AVOIDANCE (advective expansion), not capacity trapping.
  - R(t) ~ t^0.5 diffusive, amplitude-independent: linear diffusion, not degenerate.

Reports R(t), core density(t), the spread exponent, and (across packet densities) whether
the spreading rate falls with density. Certified Sigma-rule; no new rules.
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from coarsegrain_test import grid, COEFFS  # noqa: E402
BITS = os.path.join(os.path.dirname(HERE), "Bits")
sys.path.insert(0, BITS)
from simulator import NodeState, StateVector, assign_stratum_ids, step  # noqa: E402


def run_packet(S, base, r0, T, seed):
    """Localized packet of active fronts on a low background; returns R(t), core_rho(t)."""
    rng = np.random.default_rng(seed)
    sv = StateVector()
    cx = cy = S // 2
    for y in range(S):
        for x in range(S):
            sv[y * S + x] = NodeState(rho=float(np.clip(base + rng.uniform(-0.05, 0.05), 0, 0.99)),
                                      orientation=rng.normal(size=2))
    g = grid(S)
    core = []
    for y in range(S):
        for x in range(S):
            if (x - cx) ** 2 + (y - cy) ** 2 <= r0 ** 2:
                sv[y * S + x].active = True
                core.append(y * S + x)
    st = assign_stratum_ids(sv, g)
    Rt, rhoc = [], []
    for _ in range(T):
        if step(sv, g, COEFFS, strata=st) == 0:
            break
        act = [n for n in sv if sv[n].active]
        if not act:
            break
        xs = np.array([n % S for n in act], float)
        ys = np.array([n // S for n in act], float)
        R = np.sqrt(((xs - xs.mean()) ** 2 + (ys - ys.mean()) ** 2).mean())
        Rt.append(R)
        rhoc.append(float(np.mean([sv[n].rho for n in core])))
    return np.array(Rt), np.array(rhoc)


def expo(Rt):
    t = np.arange(1, len(Rt) + 1)
    sel = (t >= 4) & (t <= len(Rt) * 0.85) & (Rt > 0)
    if sel.sum() < 4:
        return 0.0
    a, _ = np.polyfit(np.log(t[sel]), np.log(Rt[sel]), 1)
    return float(a)


def main():
    S, T, r0 = 161, 90, 7
    seeds = list(range(1, 9))
    print("=" * 80)
    print(f"CROWDING / CAPACITY TEST — does packet spreading slow as the core fills?  (S={S})")
    print("=" * 80)
    print(f"\n  {'base rho':>8} {'spread exp a':>13} {'core rho: start->end':>24}  regime")
    rows = []
    for base in (0.05, 0.20, 0.35):
        Rts, rhocs, alphas = [], [], []
        for sd in seeds:
            Rt, rhoc = run_packet(S, base, r0, T, sd)
            if len(Rt) > 10:
                Rts.append(Rt); rhocs.append(rhoc); alphas.append(expo(Rt))
        L = min(len(r) for r in Rts)
        Rt = np.mean([r[:L] for r in Rts], axis=0)
        rhoc = np.mean([r[:L] for r in rhocs], axis=0)
        a = float(np.mean(alphas))
        reg = ("ballistic/advective" if a > 0.8 else
               "diffusive" if abs(a - 0.5) < 0.2 else
               "sub-diff (capacity-trapped)" if a < 0.35 else "intermediate")
        print(f"  {base:>8.2f} {a:>13.2f} {rhoc[0]:>11.2f} -> {rhoc[-1]:<10.2f}  {reg}")
        rows.append((base, a, rhoc[0], rhoc[-1], Rt, rhoc))

    # within a single run: does the LOCAL spread exponent fall as the core fills?
    base, a, r_s, r_e, Rt, rhoc = rows[0]
    print(f"\n  Time-resolved (base={base:.2f}): does spreading decelerate as core density rises?")
    n = len(Rt)
    for frac in (0.25, 0.5, 0.75, 1.0):
        i0 = max(1, int(n * (frac - 0.25))); i1 = int(n * frac)
        t = np.arange(i0 + 1, i1 + 1)
        seg = Rt[i0:i1]
        if len(seg) >= 3 and (seg > 0).all():
            la, _ = np.polyfit(np.log(t), np.log(seg), 1)
        else:
            la = float("nan")
        print(f"    window {frac-0.25:.2f}-{frac:.2f}: core rho ~ {rhoc[min(i1,n-1)]:.2f}, local spread exp = {la:.2f}")

    print("\n" + "-" * 80)
    print("READ: spread exponent FALLING as core rho rises (and/or lower exponent at higher")
    print("  base density) = mobility degenerates with density -> the UDM capacity law, off the")
    print("  substrate. Exponent staying high/ballistic = density-AVOIDANCE advection, not")
    print("  capacity trapping -- the strain term pushes fronts out, it doesn't freeze them.")
    print("-" * 80)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
