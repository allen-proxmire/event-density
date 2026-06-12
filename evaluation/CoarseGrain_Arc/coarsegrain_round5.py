"""ED-CoarseGrain Round 5 — the saturation/extinction fork: does it generate UDM?

Round 4 found the certified substrate does NOT generate the UDM mobility law because the strain
rule gives AVOIDANCE not BLOCKING (a front always commits somewhere -> no mobility degeneracy).
The one untested blocking mechanism is the certified substrate's SATURATION/EXTINCTION threshold:
fronts EXTINGUISH where Sigma falls below threshold, which happens in dense/saturated regions.
That is exactly the blocking UDM needs.

Test: turn extinction ON (extinction_threshold = -2.0, the certified size-sweep value). Measure,
vs background concentration c (built up over time), the EXTINCTION rate e(c) and the effective
mobility mu_eff(c) = (1 - scatter)(1 - e) -- the productive directed transport per surviving front.
If e(c) rises sharply and mu_eff(c) follows the UDM form (1 - c/c_max)^beta (beta~2), then UDM is
the substrate's SATURATION regime. Let the data decide; UDM is the hypothesis. No rule changes
(extinction is a certified, pre-existing Sigma feature; Round 4 simply ran with it off).
"""
from __future__ import annotations
import os, sys
import numpy as np

BITS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Bits")
sys.path.insert(0, BITS)
from simulator import ParticipationGraph, NodeState, StateVector, assign_stratum_ids, step  # noqa: E402
from simulator.sigma import SigmaCoeffs  # noqa: E402


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


def one_run(S, T, g, coeffs, seed, cb):
    """Per-step, binned by background concentration c: [active, extinct, scatter, scatter_tot]."""
    rng = np.random.default_rng(seed)
    sv = StateVector()
    for y in range(S):
        for x in range(S):
            sv[y * S + x] = NodeState(rho=float(rng.uniform(0, 0.3)), orientation=rng.normal(size=2))
    for nid in rng.choice(np.arange(S * S), int(S * S * 0.10), replace=False):
        sv[int(nid)].active = True
    st = assign_stratum_ids(sv, g)
    rec = Rec(); last_dir = {}
    NBINS, CMAX = len(cb[0]), 3.0
    for t in range(T):
        active_before = sv.active_nodes()
        na = len(active_before)
        if na == 0:
            break
        c = sum(s.rho for s in sv.values()) / (S * S)
        b = min(int(c / CMAX * NBINS), NBINS - 1)
        rec.commits = []
        nc = step(sv, g, coeffs, strata=st, recorder=rec, t=t + 1)
        nd = {}; sca = 0; tot = 0
        for u, v in rec.commits:
            d = (v % S - u % S, v // S - u // S)
            if u in last_dir:
                tot += 1; sca += (last_dir[u] != d)
            nd[v] = d
        last_dir = nd
        cb[0][b] += na                       # active fronts
        cb[1][b] += (na - nc)                # extinctions this step = active_before - commits
        cb[2][b] += sca                      # scatter events
        cb[3][b] += tot                      # scatter total


def main():
    S, T, N = 61, 30, 120
    g = grid(S)
    NBINS = 12
    print("=" * 72)
    print(f"ED-CoarseGrain R5 — saturation/extinction -> UDM?  (S={S}, T={T}, N={N})")
    print("=" * 72)

    for thr in (-2.0, -3.0):
        coeffs = SigmaCoeffs(kc=1, ks=1, kg=1, rho_star=0.5, extinction_threshold=thr)
        cb = [np.zeros(NBINS) for _ in range(4)]   # active, extinct, scatter, scatter_tot
        for i in range(N):
            one_run(S, T, g, coeffs, 2000 + i, cb)
        active, extinct, scat, tot = cb
        c_c = (np.arange(NBINS) + 0.5) * 3.0 / NBINS
        e = np.where(active > 0, extinct / np.maximum(active, 1), np.nan)      # extinction rate
        s = np.where(tot > 0, scat / np.maximum(tot, 1), np.nan)              # scatter rate
        mu = (1 - s) * (1 - e)                                                 # effective mobility
        good = active > 2000
        print(f"\n=== extinction_threshold = {thr} ===")
        print(f"   {'conc c':>7} {'active':>9} {'extinct e':>10} {'scatter':>8} {'mu_eff':>8}")
        for b in range(NBINS):
            if active[b] > 0:
                tag = "" if good[b] else "  (low N)"
                print(f"   {c_c[b]:>7.2f} {int(active[b]):>9} {e[b]:>10.3f} {s[b]:>8.3f} {mu[b]:>8.3f}{tag}")
        # does extinction rise with c (blocking)?
        gc, ge, gmu = c_c[good], e[good], np.clip(mu[good], 1e-3, None)
        if len(gc) >= 3:
            rise = ge[-1] - ge[0]
            # UDM fit mu_eff ~ (1 - c/c_max)^beta
            best = None
            for cmax in np.linspace(gc.max() * 1.02, gc.max() * 5, 80):
                X = np.log(np.clip(1 - gc / cmax, 1e-6, None)); Y = np.log(gmu)
                A = np.column_stack([X, np.ones_like(X)]); co, *_ = np.linalg.lstsq(A, Y, rcond=None)
                r2 = 1 - np.sum((Y - A @ co) ** 2) / (np.sum((Y - Y.mean()) ** 2) + 1e-12)
                if best is None or r2 > best[0]:
                    best = (r2, co[0], cmax)
            print(f"   extinction rate rise over c: {ge[0]:.3f} -> {ge[-1]:.3f}  (Delta={rise:+.3f})")
            print(f"   mu_eff range: {gmu.min():.3f}..{gmu.max():.3f}")
            print(f"   UDM fit mu_eff ~ (1 - c/c_max)^beta:  beta={best[1]:.2f}, c_max={best[2]:.2f}, "
                  f"R^2={best[0]:.3f}   (UDM canonical beta~2)")

    print("\n" + "=" * 72)
    print("Read: does extinction rate e RISE with concentration (blocking present)? and does")
    print("effective mobility mu_eff follow the UDM (1-c/c_max)^beta form? -> is UDM the")
    print("certified substrate's SATURATION regime, or unrelated to it?")
    print("=" * 72)
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
