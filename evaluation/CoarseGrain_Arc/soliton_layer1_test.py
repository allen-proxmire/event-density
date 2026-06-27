"""Layer-1 live test — SOLITON: can ED's transport hold a localized structure together,
or does a packet just spread?

The arrow thesis places KdV/NLS on layer 1 (structure-preserving, reversible) by CHARACTER.
The could-say-no: does ED actually MAKE a stable localized structure? A soliton is dispersion
(spreading) balanced by a nonlinearity (self-focusing). ED has both ingredients intrinsically:
  - dispersion: finite-kernel-width transport spreads a packet;
  - nonlinearity: the Sigma-rule scores on local rho, and a moving packet deposits its own rho
    -> the packet feels a self-field. No knob is added; the nonlinearity is the substrate's.

Test: seed a localized disk of active worldlines, evolve under the CERTIFIED step(), track the
packet's RMS width(t). Compare a SPARSE packet (weak self-field) vs a DENSE packet (strong
self-field, same disk). Fit width ~ t^p.
  - p ~ 0.5 (diffusive) or ~1 (ballistic), DENSITY-INDEPENDENT  => packet spreads, NO soliton
    (the layer-1-soliton placement is structural only; the certified rule doesn't realize it).
  - DENSE packet width bounded / p_dense << p_sparse              => nonlinear self-trapping,
    dispersion balanced => soliton-like, structure-preservation CONFIRMED, opens the QM door.

Certified rule, intrinsic self-field, no tuned knob. Could-say-no by density-independent spread.
"""
from __future__ import annotations
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coarsegrain_test import init_state, grid, assign_stratum_ids, step, COEFFS


def run_packet(S, T, r0, fill, seed):
    """Seed a disk of radius r0 at center with `fill` fraction of nodes active; track width(t)."""
    sv, _ = init_state(S, "uniform", seed)
    g = grid(S)
    rng = np.random.default_rng(seed + 101)
    cx = cy = S // 2
    disk = [(x, y) for y in range(S) for x in range(S)
            if (x - cx) ** 2 + (y - cy) ** 2 <= r0 * r0]
    k = max(1, int(len(disk) * fill))
    pick = rng.choice(len(disk), size=k, replace=False)
    for i in pick:
        x, y = disk[i]
        sv[y * S + x].active = True
    st = assign_stratum_ids(sv, g)

    widths, counts = [], []
    for t in range(T + 1):
        act = [(n % S, n // S) for n in sv if sv[n].active]
        if not act:
            break
        a = np.array(act, float)
        c = a.mean(axis=0)
        rms = np.sqrt(((a - c) ** 2).sum(axis=1).mean())
        widths.append(rms); counts.append(len(act))
        if t < T:
            if step(sv, g, COEFFS, strata=st) == 0:
                break
    return np.array(widths), np.array(counts)


def fit_p(widths, lo, hi):
    t = np.arange(len(widths))
    m = (t >= lo) & (t <= hi) & (widths > 0)
    if m.sum() < 4:
        return float("nan")
    p, _ = np.polyfit(np.log(t[m]), np.log(widths[m]), 1)
    return float(p)


def main():
    S, T, r0 = 251, 80, 8
    seeds = list(range(1, 13))
    print("=" * 78)
    print("SOLITON layer-1 test — does ED self-trap a packet, or does it just spread?")
    print(f"  (S={S}, T={T}, disk r0={r0}, {len(seeds)} seeds; sparse vs dense self-field)")
    print("=" * 78)

    for label, fill in [("SPARSE (fill=0.05)", 0.05), ("DENSE  (fill=0.90)", 0.90)]:
        W, C = [], []
        for sd in seeds:
            w, c = run_packet(S, T, r0, fill, sd)
            n = min(len(w), T + 1)
            W.append(np.pad(w[:n].astype(float), (0, T + 1 - n), constant_values=np.nan))
            C.append(np.pad(c[:n].astype(float), (0, T + 1 - n), constant_values=np.nan))
        W = np.nanmean(np.array(W), axis=0)
        C = np.nanmean(np.array(C), axis=0)
        p_early = fit_p(W, 2, 15)
        p_late = fit_p(W, 25, 70)
        print(f"\n  {label}")
        print(f"    width:  t=0 {W[0]:.2f} | t=10 {W[10]:.2f} | t=40 {W[40]:.2f} | t={T} {W[min(T,len(W)-1)]:.2f}")
        print(f"    active: t=0 {C[0]:.0f} | t=40 {C[40]:.0f} | t={T} {C[min(T,len(C)-1)]:.0f}")
        print(f"    spread exponent p (width~t^p):  early {p_early:.2f}   late {p_late:.2f}")

    print("\n" + "=" * 78)
    print("READ: density-independent spread (p~0.5-1 both) => packet spreads, NO soliton.")
    print("      dense width bounded / p_dense << p_sparse  => self-trapping, soliton-like.")
    print("=" * 78)


if __name__ == "__main__":
    main()
