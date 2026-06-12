"""ED-CoarseGrain Round 6 — the conserved-bandwidth bridge test.

Hypothesis (Allen's bridge instinct, crank-safe form): the CoarseGrain arc coarse-grained rho
-- a MONOTONE, NON-conserved deposit (P11 forbids draining it) -- so no continuity equation
could close. ED's actual CONSERVED quantity is BANDWIDTH (P04 four-band budget: commitment
draws from the commitment-reserve band and concentrates it; total conserved). The certified
Bits sim omits this (static scalar bw). Here we implement the P04 conservation faithfully and
coarse-grain the CONSERVED field, asking: does it close into a clean PDE where rho could not?

Faithful, crank-safe model (no new primitive; P04 + the certified Sigma-rule):
- each FRONT carries a reserve B (the commitment-reserve band).
- each step a front commits to its max-Sigma neighbour (certified compute_sigma on the deposited
  field d), DEPOSITS a fixed quantum delta into d (concentration), and carries B-delta onward.
- when reserve < delta the front exhausts (deposits the remainder, dies) = saturation.
- TOTAL bandwidth = sum(deposited d) + sum(front reserves) is CONSERVED by construction.

Tests: (1) conservation holds; (2) continuity d_t(d+m) + div J = 0 (must hold -> sanity that
conservation is implemented); (3) THE REAL TEST -- does the current J CLOSE as a clean
constitutive law J = m*v(grad d) - D grad m, giving a CLOSED PDE? Ensemble + matched coarsening.
"""
from __future__ import annotations
import os, sys
import numpy as np

BITS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Bits")
sys.path.insert(0, BITS)
from simulator import ParticipationGraph, NodeState, StateVector  # noqa: E402
from simulator.sigma import SigmaCoeffs, compute_sigma  # noqa: E402

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5)
DELTA = 1.0       # bandwidth quantum deposited per commit
B0 = 5.0          # initial front reserve (commitment-reserve band)
MINRES = 0.5      # below this the front exhausts


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


def step_bw(sv, g, reserve, S):
    """One conserved-bandwidth step. Returns (new_reserve, jx, jy, dep). Total conserved."""
    jx = np.zeros((S, S)); jy = np.zeros((S, S)); dep = np.zeros((S, S))
    new_reserve = {}
    for u in sorted(reserve.keys()):
        B = reserve[u]
        cands = g.admissible_neighbors(u)
        if not cands:
            sv[u].commit(B); continue                      # nowhere to go: deposit, die
        sig = {v: compute_sigma(u, v, sv, g, COEFFS) for v in cands}
        smax = max(sig.values())
        w = max([v for v in cands if sig[v] == smax], key=lambda v: (g.bw(u, v), v))
        db = min(DELTA, B)
        sv[w].commit(db)                                   # deposit (concentrate) at winner
        Bnew = B - db
        ux, uy, wx, wy = u % S, u // S, w % S, w // S
        jx[uy, ux] += (wx - ux) * B; jy[uy, ux] += (wy - uy) * B   # total-bandwidth flux leaving u
        dep[wy, wx] += db
        if Bnew >= MINRES:
            new_reserve[w] = new_reserve.get(w, 0.0) + Bnew        # carry on (merge: reserves add)
        else:
            sv[w].commit(Bnew)                             # exhaust remainder into deposit, die
    return new_reserve, jx, jy, dep


def one_run(S, T, g, seed, acc):
    rng = np.random.default_rng(seed)
    sv = StateVector()
    for y in range(S):
        for x in range(S):
            sv[y * S + x] = NodeState(rho=float(rng.uniform(0, 0.3)), orientation=rng.normal(size=2))
    reserve = {}
    for nid in rng.choice(np.arange(S * S), int(S * S * 0.12), replace=False):
        reserve[int(nid)] = B0
    total0 = sum(s.rho for s in sv.values()) + sum(reserve.values())
    D, M, JX, JY = [], [], [], []
    drift = 0.0
    for t in range(T):
        if not reserve:
            break
        d = np.array([[sv[y * S + x].rho for x in range(S)] for y in range(S)])
        m = np.zeros((S, S))
        for n, B in reserve.items():
            m[n // S, n % S] += B
        D.append(d); M.append(m)
        reserve, jx, jy, dep = step_bw(sv, g, reserve, S)
        JX.append(jx); JY.append(jy)
        total = sum(s.rho for s in sv.values()) + sum(reserve.values())
        drift = max(drift, abs(total - total0) / total0)
    acc["drift"] = max(acc.get("drift", 0.0), drift)
    return np.array(D), np.array(M), np.array(JX), np.array(JY)


def cg(f, B):
    T, S, _ = f.shape; Tc, Sc = T // B, S // B
    return f[:Tc * B, :Sc * B, :Sc * B].reshape(Tc, B, Sc, B, Sc, B).mean((1, 3, 5))


def r2(y, *cols):
    A = np.column_stack(list(cols) + [np.ones_like(y)])
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return 1 - np.sum((y - A @ c) ** 2) / (np.sum((y - y.mean()) ** 2) + 1e-12), c


def main():
    S, T, N = 61, 18, 100
    g = grid(S)
    acc = {}
    DA = np.zeros((T, S, S)); MA = np.zeros((T, S, S))
    JXA = np.zeros((T, S, S)); JYA = np.zeros((T, S, S))
    cnt = np.zeros(T)
    print("=" * 72)
    print(f"ED-CoarseGrain R6 — conserved-bandwidth bridge test  (S={S}, T={T}, N={N})")
    print("=" * 72)
    for i in range(N):
        D, M, JX, JY = one_run(S, T, g, 4000 + i, acc)
        k = len(D)
        DA[:k] += D; MA[:k] += M; JXA[:k] += JX; JYA[:k] += JY; cnt[:k] += 1
    for a in (DA, MA, JXA, JYA):
        a[cnt > 0] /= cnt[cnt > 0, None, None]
    print(f"\n[conservation]  max relative drift of total bandwidth over a run: {acc['drift']:.2e}"
          f"   ({'CONSERVED' if acc['drift'] < 1e-9 else 'NOT conserved'})")

    for B in (2, 3):
        d, m = cg(DA, B), cg(MA, B)
        jx, jy = cg(JXA, B), cg(JYA, B)
        tot = d + m
        dt_tot = np.gradient(tot, axis=0)
        divJ = np.gradient(jx, axis=2) + np.gradient(jy, axis=1)
        gx_d = np.gradient(d, axis=2); gy_d = np.gradient(d, axis=1)
        gx_m = np.gradient(m, axis=2); gy_m = np.gradient(m, axis=1)
        msk = m > 0.05 * m.max()
        # (2) continuity (sanity): d_t(total) ~ -div J  (must hold if conservation is real)
        sc, _ = r2(dt_tot[msk], -divJ[msk])
        # (3) THE REAL TEST: does the current J close constitutively?
        #     J ~ a * m * grad_d (advection along Sigma-gradient) - D * grad_m (diffusion)
        sx, cx = r2(jx[msk], (m * gx_d)[msk], gx_m[msk])
        sy, cy = r2(jy[msk], (m * gy_d)[msk], gy_m[msk])
        print(f"\n   coarse block B={B} (Dt={B}), {int(msk.sum())} active cells:")
        print(f"     (sanity)  continuity d_t(d+m) ~ -div J        R^2 = {sc:.3f}")
        print(f"     (TEST)    Jx ~ a*m*grad_x d - D*grad_x m       R^2 = {sx:.3f}  "
              f"[a={cx[0]:+.3f}, -D={cx[1]:+.3f}]")
        print(f"     (TEST)    Jy ~ a*m*grad_y d - D*grad_y m       R^2 = {sy:.3f}  "
              f"[a={cy[0]:+.3f}, -D={cy[1]:+.3f}]")

    print("\n" + "=" * 72)
    print("Read: conservation drift ~0 (P04 implemented faithfully); continuity R^2 (sanity);")
    print("constitutive J R^2 = THE TEST -> does the CONSERVED bandwidth close into a clean PDE")
    print("where the non-conserved rho could not?")
    print("=" * 72)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
