"""ED-ThickRegimeContinuum Round 1 — force the over-damped regime, test PDE closure.

Round 6 (the bridge) showed conservation is necessary-but-not-sufficient: the missing
ingredient for a continuum PDE is SCALE SEPARATION (collision time tau << transport time).
ED's NATURAL regime is the opposite (thin, ballistic, determinate). So this is the
CONSTRUCTIVE test: force the substrate into the dense / over-damped / many-collision regime
and ask whether the conserved bandwidth field b(x,t) then admits a clean diffusion-class PDE
(Fickian J = -D grad b ; mode decay a(t) = a0 exp(-D k^2 t)).

The sharp design (better than "just add noise"): a single regime knob EPS interpolates from
  EPS = 0  -> pure certified Sigma-selection (each carrier hops to the max-Sigma neighbour,
              deterministic tie-break by (bw, node_id) -- the certified determinate substrate)
  EPS = 1  -> pure random scattering (carrier hops to a uniformly random neighbour -- a plain
              conserved-tracer random walk, which is diffusion BY CONSTRUCTION)
We sweep EPS and DENSITY and locate WHERE the current closes into a PDE. That answers the
load-bearing question: does ED have a PDE-generating thick regime while its DETERMINACY is
still doing real work, or only in the limit where Sigma-selection has been ERASED (EPS->1)?

Crank-safety:
- No primitive changed. rho stays MONOTONE (P11) -- no drains, no sources.
- Bandwidth is conserved EXACTLY: carriers (unit bandwidth quanta) are only ever moved, never
  created/destroyed. This is the P04 conserved field, coarse-grained.
- EPS is a REGIME knob (how often a carrier scatters vs follows Sigma), exactly the construction
  paper sec 6a proposed. EPS>0 is NOT the certified substrate; it is the constructed thick-regime
  variant whose whole point is to find ED's PDE limit if one exists, and to price it.
- The vectorised Sigma is validated against the certified simulator.sigma.compute_sigma at startup.
- Let the data decide closure. Report the failure mode honestly if it does not close.
"""
from __future__ import annotations
import os, sys
import numpy as np

BITS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Bits")
sys.path.insert(0, BITS)
from simulator import ParticipationGraph, NodeState, StateVector  # noqa: E402
from simulator.sigma import SigmaCoeffs, compute_sigma  # noqa: E402

KC, KS, KG, RHO_STAR = 1.0, 1.0, 1.0, 0.5
INCR = 0.02   # rho increment per commit (P11 monotone footprint that Sigma reads)
# directions: 0=+x 1=-x 2=+y 3=-y  (nearest-neighbour square lattice; periodic = isotropic
# at leading order for a SCALAR conserved field -- square-lattice anisotropy is 4th-order)
DX = np.array([1, -1, 0, 0]); DY = np.array([0, 0, 1, -1])


def sigma_field(rho):
    """Vectorised certified Sigma for every node and all 4 neighbour directions.

    Sigma(u->v) = KC*Coh(v) - KS*Strain(v) - KG*Grad(u,v)
      Coh(v)   = -(rho_v - rho*)^2     Strain(v) = rho_v     Grad = |rho_v - rho_u|
    Returns S4 with shape (4, S, S): S4[d, y, x] = Sigma of hopping in direction d from (x,y).
    """
    out = np.empty((4,) + rho.shape)
    for d in range(4):
        rv = np.roll(np.roll(rho, -DY[d], 0), -DX[d], 1)   # rho at the neighbour v
        coh = -(rv - RHO_STAR) ** 2
        out[d] = KC * coh - KS * rv - KG * np.abs(rv - rho)
    return out


def drift_dir(rho):
    """Per-node certified determinate choice: argmax Sigma, tie-break by (bw=1, node_id) ->
    highest neighbour node_id among the max-Sigma set. node_id = y*S+x; the +x / +y neighbours
    have larger id than -x / -y, so on a tie the certified rule prefers +y then +x. We replicate
    that exact precedence with a tiny tie-break bonus ordered [+x,-x,+y,-y] -> id rank."""
    S4 = sigma_field(rho)
    S = rho.shape[0]
    # node-id of each neighbour (periodic). rank so higher id wins ties, matching (bw,node_id).
    yy, xx = np.mgrid[0:S, 0:S]
    idrank = np.empty((4, S, S))
    for d in range(4):
        nx = (xx + DX[d]) % S; ny = (yy + DY[d]) % S
        idrank[d] = ny * S + nx
    key = S4 + 1e-9 * (idrank / (S * S))   # Sigma dominates; id breaks exact ties
    return np.argmax(key, axis=0)          # (S,S) in {0,1,2,3}


def validate_sigma():
    """Assert the vectorised Sigma matches the certified compute_sigma on random nodes."""
    S = 8
    g = ParticipationGraph()
    for y in range(S):
        for x in range(S):
            n = y * S + x; g.add_node(n)
            if x + 1 < S: g.add_edge(n, y * S + x + 1, 1.0)
            if y + 1 < S: g.add_edge(n, (y + 1) * S + x, 1.0)
    rng = np.random.default_rng(0)
    rho = rng.uniform(0, 1.2, (S, S))
    sv = StateVector()
    for y in range(S):
        for x in range(S):
            sv[y * S + x] = NodeState(rho=float(rho[y, x]), orientation=rng.normal(size=2))
    coeffs = SigmaCoeffs(kc=KC, ks=KS, kg=KG, rho_star=RHO_STAR)
    S4 = sigma_field(rho)
    worst = 0.0
    for _ in range(40):
        x = int(rng.integers(0, S - 1)); y = int(rng.integers(0, S - 1))
        u = y * S + x
        for d, v in ((0, u + 1), (2, u + S)):     # +x and +y neighbours exist for x,y<S-1
            ref = compute_sigma(u, v, sv, g, coeffs)
            worst = max(worst, abs(ref - S4[d, y, x]))
    assert worst < 1e-9, f"vectorised Sigma disagrees with certified compute_sigma: {worst:.2e}"
    return worst


def run(S, T, frac, eps, mode_amp, seed):
    """Thick-regime conserved-bandwidth run. Carriers = unit bandwidth quanta (conserved).
    Initial density carries a cosine mode along x so we can watch a Fourier mode relax."""
    rng = np.random.default_rng(seed)
    n = int(frac * S * S)
    k = 2 * np.pi / S                                  # lowest x-mode
    # sample carrier x so density ~ 1 + mode_amp*cos(k x); y uniform
    xs = np.arange(S)
    w = 1.0 + mode_amp * np.cos(k * xs); w /= w.sum()
    X = rng.choice(xs, size=n, p=w).astype(np.int64)
    Y = rng.integers(0, S, n)
    Xu = X.astype(np.float64).copy(); Yu = Y.astype(np.float64).copy()   # unwrapped for MSD
    rho = rng.uniform(0, 0.3, (S, S))
    prev = -np.ones(n, dtype=np.int64)

    amp = []                       # |cos-mode amplitude| of b(x,t)
    msd = []                       # mean square displacement
    persist = []                   # directional persistence p
    fdir = np.zeros(4)             # velocity distribution (isotropy check)
    # pooled coarse-grain samples for Fickian/continuity/diffusion regression
    Bsizes = [b for b in (4, 8, 16) if S % b == 0]
    bsnap = {b: [] for b in Bsizes}; jxs = {b: [] for b in Bsizes}; jys = {b: [] for b in Bsizes}

    for t in range(T):
        dmap = drift_dir(rho)
        det = dmap[Y, X]
        ran = rng.integers(0, 4, n)
        scatter = rng.random(n) < eps
        d = np.where(scatter, ran, det)
        fdir += np.bincount(d, minlength=4)
        if prev[0] != -1 or t > 0:
            persist.append(float(np.mean(d == prev)))
        prev = d

        # bandwidth field b(x,t) and flux J(x,t) BEFORE the move (carrier leaves origin)
        b = np.zeros((S, S)); np.add.at(b, (Y, X), 1.0)
        jx = np.zeros((S, S)); jy = np.zeros((S, S))
        np.add.at(jx, (Y, X), DX[d]); np.add.at(jy, (Y, X), DY[d])
        for B in Bsizes:
            bsnap[B].append(_block(b, B)); jxs[B].append(_block(jx, B)); jys[B].append(_block(jy, B))
        # cosine-mode amplitude of the x-marginal of b
        bx = b.sum(0); amp.append(abs(np.sum(bx * np.exp(-1j * k * xs))) / n)
        msd.append(float(np.mean((Xu - Xu.mean()) ** 2 + (Yu - Yu.mean()) ** 2)))

        # move (periodic) ; deposit monotone rho at destination (P11)
        X = (X + DX[d]) % S; Y = (Y + DY[d]) % S
        Xu += DX[d]; Yu += DY[d]
        np.add.at(rho, (Y, X), INCR)

    return (np.array(amp), np.array(msd), np.array(persist),
            fdir / fdir.sum(), bsnap, jxs, jys, k, Bsizes)


def _block(f, B):
    S = f.shape[0]; Sc = S // B
    return f[:Sc * B, :Sc * B].reshape(Sc, B, Sc, B).sum((1, 3))


def _r2(y, *cols):
    A = np.column_stack(list(cols) + [np.ones_like(y)])
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return 1 - np.sum((y - A @ c) ** 2) / (np.sum((y - y.mean()) ** 2) + 1e-12), c


def analyse(res):
    amp, msd, persist, fd, bsnap, jxs, jys, k, Bsizes = res
    out = {}
    # mode-decay rate gamma: ln amp ~ -gamma t  (diffusion => amp = a0 exp(-D k^2 t))
    a = amp / amp[0]
    win = a > 0.2                                  # fit before noise floor
    tt = np.arange(len(a))[win]
    if len(tt) >= 4:
        g, c = _r2(np.log(a[win]), tt)
        slope = np.polyfit(tt, np.log(a[win]), 1)[0]
        out["gamma"] = -slope; out["decay_r2"] = g
        out["D_mode"] = (-slope) / (k * k)
    else:
        out["gamma"] = np.nan; out["decay_r2"] = np.nan; out["D_mode"] = np.nan
    # MSD exponent: msd ~ t^alpha  (1 diffusive, 2 ballistic)
    m = msd - msd[0]; tm = np.arange(len(m))
    g2 = (m > 0) & (tm > 0)
    out["alpha"] = np.polyfit(np.log(tm[g2]), np.log(m[g2]), 1)[0] if g2.sum() >= 4 else np.nan
    out["persist"] = float(np.mean(persist)) if len(persist) else np.nan
    out["fd"] = fd
    out["aniso"] = float(np.std(fd))               # 0 = isotropic
    # PDE closure, pooled over time, per block size
    out["pde"] = {}
    for B in Bsizes:
        bs = np.array(bsnap[B]); jx = np.array(jxs[B]); jy = np.array(jys[B])
        gx = np.stack([np.gradient(b, axis=1) for b in bs])
        gy = np.stack([np.gradient(b, axis=0) for b in bs])
        lap = np.stack([np.gradient(np.gradient(b, axis=1), axis=1)
                        + np.gradient(np.gradient(b, axis=0), axis=0) for b in bs])
        dtb = np.gradient(bs, axis=0)
        divJ = np.gradient(jx, axis=2) + np.gradient(jy, axis=1)
        msk = bs > 0.05 * bs.max()
        # Fickian: stack both current components vs -grad b  -> single D
        J = np.concatenate([jx[msk], jy[msk]]); G = np.concatenate([-gx[msk], -gy[msk]])
        rf, cf = _r2(J, G)
        rc, _ = _r2(dtb[msk], -divJ[msk])           # continuity (sanity)
        rd, cd = _r2(dtb[msk], lap[msk])            # diffusion eqn
        out["pde"][B] = dict(fick_r2=rf, D_fick=cf[0], cont_r2=rc, diff_r2=rd, D_diff=cd[0])
    return out


def main():
    worst = validate_sigma()
    S, T = 96, 90
    print("=" * 78)
    print(f"ED-ThickRegimeContinuum R1 — force the over-damped regime  (S={S}, T={T})")
    print(f"vectorised Sigma validated vs certified compute_sigma: max|diff|={worst:.1e}")
    print("EPS=0 pure certified Sigma-selection ... EPS=1 pure random scatter (diffusion by constr.)")
    print("=" * 78)
    for frac in (0.5, 2.0):
        print(f"\n############  DENSITY frac = {frac}  ({int(frac*S*S)} carriers, "
              f"{frac:.1f}/node)  ############")
        print(f"{'eps':>5} {'persist':>8} {'aniso':>7} {'MSD_a':>7} {'decayR2':>8} "
              f"{'D_mode':>7} | {'B':>3} {'fickR2':>7} {'D_fick':>7} {'contR2':>7} {'diffR2':>7}")
        for eps in (0.0, 0.25, 0.5, 0.75, 1.0):
            res = run(S, T, frac, eps, mode_amp=0.6, seed=7000 + int(eps * 100))
            a = analyse(res)
            first = True
            for B, p in a["pde"].items():
                head = (f"{eps:>5.2f} {a['persist']:>8.3f} {a['aniso']:>7.3f} "
                        f"{a['alpha']:>7.2f} {a['decay_r2']:>8.3f} {a['D_mode']:>7.3f}"
                        if first else " " * 46)
                print(f"{head} | {B:>3} {p['fick_r2']:>7.3f} {p['D_fick']:>7.3f} "
                      f"{p['cont_r2']:>7.3f} {p['diff_r2']:>7.3f}")
                first = False
    print("\n" + "=" * 78)
    print("Read: as EPS -> 1 (random scatter), persist -> 0.25, aniso -> 0, MSD_a -> 1 (diffusive),")
    print("decayR2 -> 1 (clean exponential mode decay), fickR2 -> 1 (J = -D grad b closes).")
    print("KEY QUESTION: does closure (high fickR2 / diffR2) appear while EPS is SMALL (Sigma still")
    print("steering) -- a genuine ED diffusion limit -- or only at EPS -> 1, where Sigma-determinacy")
    print("has been ERASED and we are left with a plain random walk? That locates the price of the PDE.")
    print("=" * 78)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
