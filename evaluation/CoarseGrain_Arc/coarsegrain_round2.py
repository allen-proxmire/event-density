"""ED-CoarseGrain Round 2 — does the (rho, phi, J) transport-deposition system close?

Round 1: rho alone is NOT closed (it is a slaved deposition field; diffusion excluded).
Round 2: track the real dynamical variables -- front-density phi(x,t) and front-current
J(x,t) (from the commit log u->v) -- and test the kinetic closure:
   (deposition)  d_t rho  ~ k * phi
   (continuity)  d_t phi  ~ -div J        (+ sink from front merging/extinction)
   (current)     J        ~ phi v(grad rho) - D grad phi
with v(grad rho), D measured from single-chain statistics. Certified simulator only;
no assumption of diffusion vs eikonal -- the data picks the closure.
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


def run_fields(S, ic, T, seed_frac=0.10, seed=3):
    sv = init_state(S, ic, seed)
    g = grid(S)
    rng = np.random.default_rng(seed + 1)
    ids = np.arange(S * S)
    for nid in rng.choice(ids, int(S * S * seed_frac), replace=False):
        sv[int(nid)].active = True
    st = assign_stratum_ids(sv, g)
    rec = Rec()
    RHO, PHI, JX, JY, DEP = [], [], [], [], []
    for t in range(1, T + 1):
        phi = np.zeros((S, S))
        for n in sv.active_nodes():
            phi[n // S, n % S] += 1
        rec.commits = []
        ncommit = step(sv, g, COEFFS, strata=st, recorder=rec, t=t)
        jx = np.zeros((S, S)); jy = np.zeros((S, S)); dep = np.zeros((S, S))
        for u, v in rec.commits:
            ux, uy, vx, vy = u % S, u // S, v % S, v // S
            jx[uy, ux] += (vx - ux); jy[uy, ux] += (vy - uy)
            dep[vy, vx] += 1
        rho = np.array([[sv[y * S + x].rho for x in range(S)] for y in range(S)])
        RHO.append(rho); PHI.append(phi); JX.append(jx); JY.append(jy); DEP.append(dep)
        if ncommit == 0:
            break
    return (np.array(RHO), np.array(PHI), np.array(JX), np.array(JY), np.array(DEP))


def cg(field, b):
    if field.ndim == 3:
        T, S, _ = field.shape; Sc = S // b
        return field[:, :Sc * b, :Sc * b].reshape(T, Sc, b, Sc, b).mean(axis=(2, 4))
    return field


def r2(y, *cols):
    A = np.column_stack(list(cols) + [np.ones_like(y)])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    return 1 - np.sum((y - pred) ** 2) / (np.sum((y - y.mean()) ** 2) + 1e-12), coef


# ---------- single-chain drift v(grad rho) and diffusion D ----------
def single_chain_drift(S, slope, T=50, reps=8):
    g = grid(S)
    vels = []
    for r in range(reps):
        rng = np.random.default_rng(100 + r)
        sv = StateVector()
        for y in range(S):
            for x in range(S):
                sv[y * S + x] = NodeState(rho=float(0.1 + slope * x),
                                          orientation=rng.normal(size=2))
        c = (S // 2) * S + (S // 2); sv[c].active = True
        st = assign_stratum_ids(sv, g)
        p0 = (S // 2, S // 2); steps = 0
        for t in range(1, T + 1):
            step(sv, g, COEFFS, strata=st)
            a = sv.active_nodes()
            if not a:
                break
            n = a[0]; pend = (n % S, n // S); steps += 1
        vels.append(((pend[0] - p0[0]) / max(steps, 1), (pend[1] - p0[1]) / max(steps, 1)))
    v = np.array(vels).mean(axis=0)
    return np.hypot(*v)


def single_chain_D(S, T=60, reps=30):
    g = grid(S); msd = []
    for r in range(reps):
        rng = np.random.default_rng(500 + r)
        sv = StateVector()
        for y in range(S):
            for x in range(S):
                sv[y * S + x] = NodeState(rho=float(rng.uniform(0, 0.3)),
                                          orientation=rng.normal(size=2))
        c = (S // 2) * S + (S // 2); sv[c].active = True
        st = assign_stratum_ids(sv, g)
        p0 = np.array([S // 2, S // 2]); steps = 0; pend = p0
        for t in range(1, T + 1):
            step(sv, g, COEFFS, strata=st)
            a = sv.active_nodes()
            if not a:
                break
            n = a[0]; pend = np.array([n % S, n // S]); steps += 1
        if steps > 0:
            msd.append(np.sum((pend - p0) ** 2) / steps)
    return np.mean(msd) / 4.0  # MSD = 4 D t (2D)


def main():
    S, T = 121, 40
    print("=" * 72)
    print(f"ED-CoarseGrain R2 — (rho, phi, J) transport-deposition closure  (S={S}, T={T})")
    print("=" * 72)

    # single-chain drift law v(|grad rho|) and diffusion D
    print("\n[single-chain]  drift v vs landscape gradient slope:")
    for slope in (0.0, 0.001, 0.003, 0.006):
        v = single_chain_drift(S, slope)
        print(f"   slope={slope:.3f}  ->  |v| = {v:.3f}  (max 1.0 = ballistic)")
    D = single_chain_D(S)
    print(f"[single-chain]  flat-landscape diffusion  D ~ {D:.3f}  (from MSD = 4 D t)")

    # field closures
    for ic in ("uniform", "gaussian", "gradient"):
        RHO, PHI, JX, JY, DEP = run_fields(S, ic, T)
        b = 4
        rho, phi = cg(RHO, b), cg(PHI, b)
        jx, jy, dep = cg(JX, b), cg(JY, b), cg(DEP, b)
        dt_rho = np.gradient(rho, axis=0)
        dt_phi = np.gradient(phi, axis=0)
        divJ = np.gradient(jx, axis=2) + np.gradient(jy, axis=1)
        gx_r = np.gradient(rho, axis=2); gy_r = np.gradient(rho, axis=1)
        gx_p = np.gradient(phi, axis=2); gy_p = np.gradient(phi, axis=1)
        m = phi > (0.05 * phi.max())  # cells with fronts present

        print(f"\n   IC = {ic}   (coarse {rho.shape[1]}x{rho.shape[2]}, {int(m.sum())} front cells)")
        # deposition law  d_t rho ~ k phi
        s, c = r2(dt_rho[m], phi[m])
        print(f"     deposition   d_t rho ~ k*phi          R^2={s:.3f}   k={c[0]:+.3f}")
        # continuity  d_t phi ~ -div J
        s, c = r2(dt_phi[m], -divJ[m])
        print(f"     continuity   d_t phi ~ -div J          R^2={s:.3f}   slope={c[0]:+.3f}")
        # current closure  Jx ~ a*phi*gx_rho - D*gx_phi  (and Jy)
        sx, cx = r2(jx[m], (phi * gx_r)[m], gx_p[m])
        sy, cy = r2(jy[m], (phi * gy_r)[m], gy_p[m])
        print(f"     current Jx ~ a*phi*grad_x rho - D*grad_x phi   R^2={sx:.3f}  "
              f"[a={cx[0]:+.3f}, -D={cx[1]:+.3f}]")
        print(f"     current Jy ~ a*phi*grad_y rho - D*grad_y phi   R^2={sy:.3f}  "
              f"[a={cy[0]:+.3f}, -D={cy[1]:+.3f}]")

    # scaling: continuity R^2 across block sizes (uniform IC)
    print("\n[scaling]  continuity d_t phi ~ -div J  vs coarse block size (uniform IC):")
    RHO, PHI, JX, JY, DEP = run_fields(S, "uniform", T)
    for b in (2, 4, 6, 8):
        phi = cg(PHI, b); jx = cg(JX, b); jy = cg(JY, b)
        dt_phi = np.gradient(phi, axis=0)
        divJ = np.gradient(jx, axis=2) + np.gradient(jy, axis=1)
        m = phi > (0.05 * phi.max())
        s, _ = r2(dt_phi[m], -divJ[m])
        print(f"   block={b:>2}  coarse {phi.shape[1]:>2}x{phi.shape[2]:<2}  continuity R^2={s:.3f}")

    print("\n" + "=" * 72)
    print("Read: deposition + continuity + current closures -> does (rho,phi,J) form a")
    print("clean kinetic-transport PDE? Scaling -> is it a stable continuum limit?")
    print("=" * 72)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
