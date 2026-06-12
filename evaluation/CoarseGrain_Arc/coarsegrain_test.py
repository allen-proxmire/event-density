"""ED-CoarseGrain Round 1 — what continuum law does the certified substrate generate?

Structural fact (verified): the certified Sigma-rule front does NOT branch — a single
active front traces a 1D CHAIN (worldline), depositing rho along a path. So the substrate
is a chain/worldline propagator, not a field-update rule. The continuum question therefore
has two levels:

  (A) SINGLE CHAIN -> a trajectory law (does the worldline follow an extremal/eikonal path
      in the rho-landscape, i.e. Hamilton-Jacobi, rather than diffuse?).
  (B) CHAIN ENSEMBLE -> a density PDE (coarse-grain the rho deposited by many simultaneous
      chains; SINDy-style regress d_t rho on a candidate library; let the data pick the class:
      diffusion ~ Lap(rho), eikonal/transport ~ |grad rho|, PME/UDM ~ (rho_max-rho)-weighted).

No new rules; certified simulator only. The Q-C PDE is treated as a hypothesis, not assumed.
"""
from __future__ import annotations
import os, sys
import numpy as np

BITS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Bits")
sys.path.insert(0, BITS)
from simulator import ParticipationGraph, NodeState, StateVector, assign_stratum_ids, step  # noqa: E402
from simulator.sigma import SigmaCoeffs  # noqa: E402

COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=0.5)  # no extinction: chains propagate


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
    elif ic == "step":
        rho = np.where(xx < cx, 0.1, 0.45).astype(float)
    elif ic == "ring":
        r = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
        rho = 0.45 * np.exp(-((r - S / 5) ** 2) / (2 * (S / 20) ** 2))
    elif ic == "gradient":
        rho = 0.1 + 0.35 * (xx / S)
    else:
        raise ValueError(ic)
    sv = StateVector()
    for y in range(S):
        for x in range(S):
            sv[y * S + x] = NodeState(rho=float(rho[y, x]),
                                      orientation=rng.normal(size=2))
    return sv, rho


def snapshot(sv, S):
    a = np.zeros((S, S))
    for y in range(S):
        for x in range(S):
            a[y, x] = sv[y * S + x].rho
    return a


# ---------- (A) single-chain worldline ----------
def single_chain_trajectory(S, ic, T, seed=1):
    sv, _ = init_state(S, ic, seed)
    c = (S // 2) * S + (S // 2)
    sv[c].active = True
    g = grid(S)
    st = assign_stratum_ids(sv, g)
    path = [(S // 2, S // 2)]
    for t in range(1, T + 1):
        step(sv, g, COEFFS, strata=st)
        act = [n for n in sv if sv[n].active]
        if not act:
            break
        n = act[0]
        path.append((n % S, n // S))
    return np.array(path)


# ---------- (B) chain-ensemble density field ----------
def ensemble_run(S, ic, T, n_seed_frac=0.04, seed=2):
    sv, rho0 = init_state(S, ic, seed)
    g = grid(S)
    rng = np.random.default_rng(seed + 7)
    # seed a sparse set of simultaneous chains (an ensemble of worldlines)
    ids = [y * S + x for y in range(S) for x in range(S)]
    for nid in rng.choice(ids, size=int(len(ids) * n_seed_frac), replace=False):
        sv[nid].active = True
    st = assign_stratum_ids(sv, g)
    frames = [snapshot(sv, S)]
    for t in range(1, T + 1):
        if step(sv, g, COEFFS, strata=st) == 0:
            break
        frames.append(snapshot(sv, S))
    return np.array(frames)  # (T+1, S, S)


def coarse(field, b):
    T, S, _ = field.shape
    Sc = S // b
    return field[:, :Sc * b, :Sc * b].reshape(T, Sc, b, Sc, b).mean(axis=(2, 4))


def regress_pde(rho_cg, rho_max):
    # derivatives
    dt = np.gradient(rho_cg, axis=0)
    gy = np.gradient(rho_cg, axis=1)
    gx = np.gradient(rho_cg, axis=2)
    gmag = np.sqrt(gx ** 2 + gy ** 2)
    lap = (np.gradient(gy, axis=1) + np.gradient(gx, axis=2))
    # restrict to active cells (where dynamics happen) to avoid 0=0 swamping
    m = np.abs(dt) > (0.05 * np.abs(dt).max() + 1e-12)
    y = dt[m]
    feats = {
        "diffusion  Lap(rho)": lap[m],
        "eikonal    |grad rho|": gmag[m],
        "PME        (rho_max-rho)Lap": ((rho_max - rho_cg) * lap)[m],
        "PME2       -|grad|^2": (-(gmag ** 2))[m],
    }

    def r2(cols):
        A = np.column_stack([feats[c] for c in cols] + [np.ones_like(y)])
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        pred = A @ coef
        ss = 1 - np.sum((y - pred) ** 2) / (np.sum((y - y.mean()) ** 2) + 1e-12)
        return ss, coef

    out = {}
    out["diffusion"] = r2(["diffusion  Lap(rho)"])
    out["eikonal"] = r2(["eikonal    |grad rho|"])
    out["diff+eik"] = r2(["diffusion  Lap(rho)", "eikonal    |grad rho|"])
    out["PME(UDM)"] = r2(["PME        (rho_max-rho)Lap", "PME2       -|grad|^2"])
    return out, int(m.sum())


def main():
    S, T = 121, 45
    print("=" * 72)
    print(f"ED-CoarseGrain R1 — continuum law of the certified substrate  (S={S}, T={T})")
    print("=" * 72)

    # (A) single chain
    print("\n[A] SINGLE CHAIN = worldline (does it diffuse, or follow an extremal path?)")
    for ic in ("uniform", "gradient", "gaussian"):
        p = single_chain_trajectory(S, ic, 60)
        disp = p[-1] - p[0]
        steps = len(p) - 1
        net = np.hypot(*disp)
        print(f"   {ic:>9}: {steps:>3} steps, net displacement {net:6.1f}, "
              f"straightness(net/path)={net/max(steps,1):.2f}  "
              f"-> {'ballistic/eikonal' if net/max(steps,1)>0.6 else 'wandering'}")
    print("   (straightness ~1 = ballistic extremal worldline, NOT diffusive random walk)")

    # (B) ensemble density PDE
    print("\n[B] CHAIN ENSEMBLE -> density field; which PDE class does d_t rho obey?")
    rho_max = 2.0  # committed rho grows past init; use a nominal cap for the PME feature
    for ic in ("uniform", "gaussian", "step", "ring"):
        frames = ensemble_run(S, ic, T)
        cg = coarse(frames, 4)
        res, npts = regress_pde(cg, rho_max)
        print(f"\n   IC = {ic}  (coarse 30x30, {npts} active cells)")
        print(f"     {'model':<12}{'R^2':>8}   coefficients")
        for name in ("diffusion", "eikonal", "diff+eik", "PME(UDM)"):
            ss, coef = res[name]
            cs = " ".join(f"{c:+.3f}" for c in coef[:-1])
            print(f"     {name:<12}{ss:>8.3f}   [{cs}]")
        best = max(("diffusion", "eikonal", "diff+eik", "PME(UDM)"),
                   key=lambda k: res[k][0])
        print(f"     -> best single/mixed class: {best} (R^2={res[best][0]:.3f})")

    print("\n" + "=" * 72)
    print("Read: single-chain straightness -> worldline character; ensemble R^2 table ->")
    print("which continuum PDE class the certified substrate actually generates.")
    print("=" * 72)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
