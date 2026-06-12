"""ED-CoarseGrain Round 3 — Boltzmann/lattice-gas closure with a merge (collision) operator.

Round 2: rho~phi deposition holds (R^2~0.3); continuity d_t phi ~ -div J FAILS (R^2~0.04)
and DEGRADES under coarse-graining. Diagnosis: front NUMBER is not conserved -- fronts
MERGE (two -> one when they commit to the same node). So the right object is a kinetic /
lattice-gas equation with a collision (merge) operator, not a simple PDE.

Round 3 tests the kinetic closure:
   (number balance)   d_t phi + div J ~ -M        with M = merge sink
   (free streaming)   directional persistence p   (ballistic free flight vs collisions)
The decisive test: does adding the measured merge sink M turn the failed continuity into a
closed balance -- and does THAT stabilize under coarse-graining? Certified simulator only.
"""
from __future__ import annotations
import os, sys
import numpy as np

BITS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Bits")
sys.path.insert(0, BITS)
from simulator import ParticipationGraph, NodeState, StateVector, assign_stratum_ids, step  # noqa: E402
from simulator.sigma import SigmaCoeffs  # noqa: E402

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5)


def grid(S):
    g = ParticipationGraph()
    for y in range(S):
        for x in range(S):
            nid = y * S + x
            g.add_node(nid)
            if x + 1 < S:
                g.add_edge(nid, y * S + (x + 1), 1.0)
            if y + 1 < S:
                g.add_edge(nid, (y + 1) * S + x, 1.0)
    return g


def init_state(S, ic, seed=0):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:S, 0:S]
    cx = cy = S / 2
    if ic == "uniform":
        rho = rng.uniform(0, 0.3, (S, S))
    elif ic == "gaussian":
        rho = 0.45 * np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * (S / 8) ** 2))
    elif ic == "gradient":
        rho = 0.1 + 0.35 * (xx / S)
    else:
        raise ValueError(ic)
    sv = StateVector()
    for y in range(S):
        for x in range(S):
            sv[y * S + x] = NodeState(rho=float(rho[y, x]), orientation=rng.normal(size=2))
    return sv


class Rec:
    def __init__(self): self.commits = []
    def log_commit(self, t, u, v): self.commits.append((u, v))
    def snapshot(self, t, state): pass


def run(S, ic, T, seed_frac=0.10, seed=3):
    sv = init_state(S, ic, seed)
    g = grid(S)
    rng = np.random.default_rng(seed + 1)
    for nid in rng.choice(np.arange(S * S), int(S * S * seed_frac), replace=False):
        sv[int(nid)].active = True
    st = assign_stratum_ids(sv, g)
    rec = Rec()
    last_dir = {}
    PHI, JX, JY, MERGE = [], [], [], []
    pers_hit = pers_tot = 0
    for t in range(1, T + 1):
        phi = np.zeros((S, S))
        for n in sv.active_nodes():
            phi[n // S, n % S] += 1
        rec.commits = []
        nc = step(sv, g, COEFFS, strata=st, recorder=rec, t=t)
        jx = np.zeros((S, S)); jy = np.zeros((S, S)); dep = np.zeros((S, S))
        new_dir = {}
        for u, v in rec.commits:
            ux, uy, vx, vy = u % S, u // S, v % S, v // S
            d = (vx - ux, vy - uy)
            jx[uy, ux] += d[0]; jy[uy, ux] += d[1]; dep[vy, vx] += 1
            # directional persistence: did the front keep its incoming direction?
            if u in last_dir:
                pers_tot += 1
                pers_hit += (last_dir[u] == d)
            new_dir[v] = d
        last_dir = new_dir
        merge = np.maximum(dep - 1.0, 0.0)  # >=2 arrivals at a node => merge sink
        PHI.append(phi); JX.append(jx); JY.append(jy); MERGE.append(merge)
        if nc == 0:
            break
    p = pers_hit / max(pers_tot, 1)
    return (np.array(PHI), np.array(JX), np.array(JY), np.array(MERGE), p)


def cg(f, b):
    T, S, _ = f.shape; Sc = S // b
    return f[:, :Sc * b, :Sc * b].reshape(T, Sc, b, Sc, b).mean(axis=(2, 4))


def r2(y, *cols):
    A = np.column_stack(list(cols) + [np.ones_like(y)])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return 1 - np.sum((y - A @ coef) ** 2) / (np.sum((y - y.mean()) ** 2) + 1e-12), coef


def main():
    S, T = 121, 40
    print("=" * 72)
    print(f"ED-CoarseGrain R3 — lattice-gas / Boltzmann closure (merge operator)  S={S}")
    print("=" * 72)

    print("\n[free streaming]  directional persistence p = P(next move = last move):")
    for ic in ("uniform", "gaussian", "gradient"):
        *_, p = run(S, ic, T)
        print(f"   {ic:>9}: p = {p:.3f}   "
              f"-> {'ballistic free-flight (rare collisions)' if p > 0.6 else 'collision-dominated'}")

    print("\n[number balance]  does adding the merge sink M close continuity?")
    for ic in ("uniform", "gaussian", "gradient"):
        PHI, JX, JY, MERGE, _ = run(S, ic, T)
        b = 4
        phi, jx, jy, M = cg(PHI, b), cg(JX, b), cg(JY, b), cg(MERGE, b)
        dt_phi = np.gradient(phi, axis=0)
        divJ = np.gradient(jx, axis=2) + np.gradient(jy, axis=1)
        m = phi > (0.05 * phi.max())
        s0, _ = r2(dt_phi[m], -divJ[m])                  # Round-2: no merge
        s1, c1 = r2(dt_phi[m], -divJ[m], -M[m])          # Round-3: + merge sink
        frac_merge = M[m].mean() / max(phi[m].mean(), 1e-9)
        print(f"   IC={ic:>9}:  continuity R^2 = {s0:.3f} (no M)  ->  {s1:.3f} (+M)  "
              f"[merge coef={c1[1]:+.2f}, merge/phi~{frac_merge:.2f}]")

    print("\n[scaling]  merge-closed balance vs block size (gaussian IC):")
    PHI, JX, JY, MERGE, _ = run(S, "gaussian", T)
    for b in (2, 4, 6, 8):
        phi, jx, jy, M = cg(PHI, b), cg(JX, b), cg(JY, b), cg(MERGE, b)
        dt_phi = np.gradient(phi, axis=0)
        divJ = np.gradient(jx, axis=2) + np.gradient(jy, axis=1)
        m = phi > (0.05 * phi.max())
        s0, _ = r2(dt_phi[m], -divJ[m])
        s1, _ = r2(dt_phi[m], -divJ[m], -M[m])
        print(f"   block={b:>2}  coarse {phi.shape[1]:>2}x{phi.shape[2]:<2}  "
              f"R^2 no-M={s0:.3f}   R^2 +M={s1:.3f}")

    print("\n" + "=" * 72)
    print("Read: persistence -> free-flight vs collision regime; 'no M -> +M' R^2 jump ->")
    print("whether the merge (collision) operator closes the kinetic balance; scaling ->")
    print("whether the closed balance is a stable continuum (improves with block size).")
    print("=" * 72)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
