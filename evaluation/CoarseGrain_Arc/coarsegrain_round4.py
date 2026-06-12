"""ED-CoarseGrain Round 4 — quantitative kinetic closure + the substrate->UDM test.

Fixes the Round 1-3 measurement limits (sparse deterministic field, mismatched space-time
coarsening) with (a) ENSEMBLE averaging over N runs, (b) MATCHED space-time coarse-graining
(time window Dt = block B, so a front crosses one coarse cell per coarse step), (c) VELOCITY-
resolved front populations f_d.

Headline test (substrate -> UDM -> FRAP): the certified substrate's STRAIN term makes fronts
avoid high rho. If the kinetic mobility/diffusion D(rho) measured from scattering statistics
follows the Universal-Mobility form  D(rho) = D0 (1 - rho/rho_max)^beta  (canonical beta~2),
then the substrate GENERATES the UDM law -- the over-damped limit connecting substrate to the
FRAP empirical anchor. Let the data decide; UDM is the hypothesis, not the assumption.

Also: matched-coarsening continuity closure (does d_t phi + div J ~ 0 close now?), and a BGK
relaxation-time / equilibrium check. Certified Sigma-substrate only; no rule changes.
"""
from __future__ import annotations
import os, sys
import numpy as np

BITS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Bits")
sys.path.insert(0, BITS)
from simulator import ParticipationGraph, NodeState, StateVector, assign_stratum_ids, step  # noqa: E402
from simulator.sigma import SigmaCoeffs  # noqa: E402

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5)
DIRS = {(1, 0): 0, (-1, 0): 1, (0, 1): 2, (0, -1): 3}  # 4 lattice velocities


def grid(S):
    g = ParticipationGraph()
    for y in range(S):
        for x in range(S):
            n = y * S + x
            g.add_node(n)
            if x + 1 < S:
                g.add_edge(n, y * S + x + 1, 1.0)
            if y + 1 < S:
                g.add_edge(n, (y + 1) * S + x, 1.0)
    return g


class Rec:
    def __init__(self): self.commits = []
    def log_commit(self, t, u, v): self.commits.append((u, v))
    def snapshot(self, t, state): pass


def one_run(S, T, g, seed, rho_bins, t_stats):
    """One ensemble member. Returns per-step fields (f_d, phi, Jx, Jy); accumulates scattering
    stats binned by local committed-rho (rho_bins) AND per-timestep (t_stats: cnt, scatter, conc).
    The per-time stats give mobility vs BACKGROUND concentration (the proper UDM tracer test)."""
    rng = np.random.default_rng(seed)
    sv = StateVector()
    for y in range(S):
        for x in range(S):
            sv[y * S + x] = NodeState(rho=float(rng.uniform(0, 0.3)),
                                      orientation=rng.normal(size=2))
    for nid in rng.choice(np.arange(S * S), int(S * S * 0.10), replace=False):
        sv[int(nid)].active = True
    st = assign_stratum_ids(sv, g)
    rec = Rec()
    last_dir = {}
    FD = np.zeros((T, 4, S, S)); PHI = np.zeros((T, S, S))
    JX = np.zeros((T, S, S)); JY = np.zeros((T, S, S))
    nb = len(rho_bins[0])
    for t in range(T):
        for n in sv.active_nodes():
            d = last_dir.get(n)
            if d is not None:
                FD[t, DIRS[d], n // S, n % S] += 1
            PHI[t, n // S, n % S] += 1
        rec.commits = []
        nc = step(sv, g, COEFFS, strata=st, recorder=rec, t=t + 1)
        nd = {}
        for u, v in rec.commits:
            ux, uy, vx, vy = u % S, u // S, v % S, v // S
            d = (vx - ux, vy - uy)
            JX[t, uy, ux] += d[0]; JY[t, uy, ux] += d[1]
            if u in last_dir:
                rho_u = sv[u].rho
                b = min(int(rho_u / 0.25), nb - 1)
                rho_bins[0][b] += 1; rho_bins[1][b] += (last_dir[u] != d)
                t_stats[0][t] += 1; t_stats[1][t] += (last_dir[u] != d)   # per-time scatter
            nd[v] = d
        last_dir = nd
        # background concentration = mean committed rho over the whole grid this step
        t_stats[2][t] += sum(s.rho for s in sv.values()) / (S * S)
        if nc == 0:
            break
    return FD, PHI, JX, JY


def cg_st(f, B):
    """Matched space-time coarse-grain: block B in space, window Dt=B in time."""
    if f.ndim == 4:  # (T,4,S,S)
        T, K, S, _ = f.shape
        Tc, Sc = T // B, S // B
        return f[:Tc * B, :, :Sc * B, :Sc * B].reshape(Tc, B, K, Sc, B, Sc, B).mean((1, 4, 6))
    T, S, _ = f.shape
    Tc, Sc = T // B, S // B
    return f[:Tc * B, :Sc * B, :Sc * B].reshape(Tc, B, Sc, B, Sc, B).mean((1, 3, 5))


def main():
    S, T, N = 61, 32, 120
    g = grid(S)
    nb = 8
    rho_bins = [np.zeros(nb), np.zeros(nb)]  # [count, n_scatter]
    t_stats = [np.zeros(T), np.zeros(T), np.zeros(T)]  # [cnt, scatter, conc] per timestep
    FD = np.zeros((T, 4, S, S)); PHI = np.zeros((T, S, S))
    JX = np.zeros((T, S, S)); JY = np.zeros((T, S, S))
    print("=" * 72)
    print(f"ED-CoarseGrain R4 — kinetic closure + substrate->UDM test  (S={S}, T={T}, N={N})")
    print("=" * 72)
    for i in range(N):
        fd, phi, jx, jy = one_run(S, T, g, 1000 + i, rho_bins, t_stats)
        FD += fd; PHI += phi; JX += jx; JY += jy
    FD /= N; PHI /= N; JX /= N; JY /= N

    # ---- the PROPER UDM test: mobility vs BACKGROUND concentration (built up over time) ----
    tc, ts, tco = t_stats
    conc = tco / N                                    # mean committed-rho (concentration) vs time
    s_t = np.where(tc > 0, ts / np.maximum(tc, 1), np.nan)   # scatter rate vs time
    mob_t = 1 - s_t                                   # mobility vs time
    print("\n[UDM test]  mobility vs BACKGROUND concentration c (built up over time):")
    print(f"   {'t':>4} {'conc c':>8} {'scatter':>8} {'mobility':>9}")
    for t in range(0, T, max(T // 12, 1)):
        if tc[t] > 0:
            print(f"   {t:>4} {conc[t]:>8.3f} {s_t[t]:>8.3f} {mob_t[t]:>9.3f}")
    good = (tc > 1000) & np.isfinite(mob_t)
    cuse, muse = conc[good], np.clip(mob_t[good], 1e-3, None)
    # fit UDM  mobility ~ (1 - c/c_max)^beta
    bestu = None
    for cmax in np.linspace(cuse.max() * 1.02, cuse.max() * 6, 80):
        X = np.log(np.clip(1 - cuse / cmax, 1e-6, None)); Y = np.log(muse)
        A = np.column_stack([X, np.ones_like(X)]); coef, *_ = np.linalg.lstsq(A, Y, rcond=None)
        r2 = 1 - np.sum((Y - A @ coef) ** 2) / (np.sum((Y - Y.mean()) ** 2) + 1e-12)
        if bestu is None or r2 > bestu[0]:
            bestu = (r2, coef[0], cmax)
    # linear and power-law alternatives for honesty
    rng_mob = muse.max() - muse.min()
    print(f"   mobility range over c: {muse.min():.3f}..{muse.max():.3f}  (span {rng_mob:.3f})")
    print(f"   UDM fit mobility ~ (1 - c/c_max)^beta:  beta={bestu[1]:.2f}, c_max={bestu[2]:.2f}, "
          f"R^2={bestu[0]:.3f}  (UDM canonical beta~2)")

    # ---- headline: mobility / D(rho) from scattering, vs UDM form ----
    cnt, sc = rho_bins
    valid = cnt > 500
    rho_c = (np.arange(nb) + 0.5) * 0.25
    s = np.where(cnt > 0, sc / np.maximum(cnt, 1), np.nan)       # scatter rate
    mob = 1.0 - s                                                # directed fraction (mobility proxy)
    Dr = np.where(s > 0, 1.0 / (4.0 * s), np.nan)               # D ~ v^2 tau/2d, tau=1/s
    print("\n[mobility D(rho)]  scattering rate s, mobility (1-s), D=1/(4s)  vs local committed-rho:")
    print(f"   {'rho':>6} {'N':>9} {'s':>7} {'mobility':>9} {'D':>7}")
    for b in range(nb):
        if cnt[b] > 0:
            print(f"   {rho_c[b]:>6.2f} {int(cnt[b]):>9} {s[b]:>7.3f} {mob[b]:>9.3f} {Dr[b]:>7.3f}"
                  + ("" if valid[b] else "  (low N)"))
    # fit UDM:  mobility ~ (1 - rho/rho_max)^beta   on valid bins
    rv, mv = rho_c[valid], mob[valid]
    mv = np.clip(mv, 1e-3, None)
    best = None
    for rmax in np.linspace(rv.max() * 1.05, rv.max() * 4, 60):
        X = np.log(np.clip(1 - rv / rmax, 1e-6, None)); Y = np.log(mv)
        A = np.column_stack([X, np.ones_like(X)])
        coef, *_ = np.linalg.lstsq(A, Y, rcond=None)
        r2 = 1 - np.sum((Y - A @ coef) ** 2) / (np.sum((Y - Y.mean()) ** 2) + 1e-12)
        if best is None or r2 > best[0]:
            best = (r2, coef[0], rmax)
    print(f"\n   UDM fit  mobility ~ (1 - rho/rho_max)^beta :  beta = {best[1]:.2f}, "
          f"rho_max = {best[2]:.2f},  R^2 = {best[0]:.3f}   (UDM canonical beta~2)")
    # monotonic check
    mono = all(mob[b] >= mob[b + 1] - 0.02 for b in range(nb - 1) if cnt[b] > 500 and cnt[b + 1] > 500)
    print(f"   mobility decreases with rho (UDM-direction): {mono}")

    # ---- matched-coarsen continuity closure (the Round 2/3 fix) ----
    print("\n[continuity]  d_t phi ~ -div J  with MATCHED space-time coarsening + ensemble:")
    for B in (2, 4, 8):
        phi = cg_st(PHI, B); jx = cg_st(JX, B); jy = cg_st(JY, B)
        dt = np.gradient(phi, axis=0)
        divJ = np.gradient(jx, axis=2) + np.gradient(jy, axis=1)
        m = phi > 0.05 * phi.max()
        y, x = dt[m], -divJ[m]
        A = np.column_stack([x, np.ones_like(x)]); c, *_ = np.linalg.lstsq(A, y, rcond=None)
        r2 = 1 - np.sum((y - A @ c) ** 2) / (np.sum((y - y.mean()) ** 2) + 1e-12)
        print(f"   B={B}, Dt={B}  coarse {phi.shape[1]}x{phi.shape[2]}  continuity R^2 = {r2:.3f}"
              f"  (Round 2/3 unmatched: ~0.04-0.11)")

    # ---- BGK: relaxation time tau and equilibrium isotropy ----
    s_mean = np.nansum(sc) / max(np.nansum(cnt), 1)
    tau = 1.0 / max(s_mean, 1e-6)
    fd_tot = FD.sum((0, 2, 3))
    aniso = fd_tot.std() / max(fd_tot.mean(), 1e-9)
    print(f"\n[BGK]  mean scatter rate = {s_mean:.3f} -> relaxation time tau ~ {tau:.2f} steps")
    print(f"       direction populations f_d (ensemble total) = {np.round(fd_tot / fd_tot.sum(), 3)}"
          f"   anisotropy = {aniso:.3f}  ({'near-isotropic eq' if aniso < 0.15 else 'anisotropic'})")

    print("\n" + "=" * 72)
    print("VERDICT inputs: D(rho) form + UDM fit -> substrate->UDM? ; matched continuity R^2 ->")
    print("does the kinetic balance close once measurement is fixed? ; tau, isotropy -> BGK.")
    print("=" * 72)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
