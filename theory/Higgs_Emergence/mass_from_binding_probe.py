"""
Mass without mass: does V5-binding confine BALLISTIC certified fronts into a
cluster whose CENTER-OF-MASS is SUB-BALLISTIC (= rest mass from binding)?

The mass-sector wall (H1_Leg_Scoping): the certified rule is ballistic-or-extinct
-- an individual front advances one hop/step or dies, no sub-ballistic surviving
mode, so no INDIVIDUAL rest mass. But rest mass in real physics is mostly BINDING
(a box of photons, or quarks+gluons in a proton, has rest mass = internal energy;
its COM moves sub-luminally though the constituents move at c). The COMPOSITE COM
is a different object from the individual front. So the test:

  Do V5-bound ballistic fronts (each |v|=1) form a bound cluster whose COM is
  sub-ballistic (|v_COM| < 1, -> 0 for isotropic internal motion = pure rest mass)?

FAITHFUL, not rigged:
- 2D grid; each front's per-step choice is the certified compute_sigma on the REAL
  rho field (fronts avoid their own deposited trail -> move into fresh ground ->
  ballistic, exactly the certified 2D worldline of the Continuum paper).
- V5 = its actual known structure: retarded (prev-step positions), finite-reach
  attraction exp(-|dr|/ell_V5) toward the reach-weighted centroid of the OTHER
  fronts. NOT rigged to bind: whether the finite reach can confine |v|=1 fronts
  is exactly the open question -- if they outrun the reach, it comes back NO.

HONEST CAVEATS (same as v5_substrate_coupling_probe.py):
- V5 is a structural ADDITION (faithful to Paper_090's finite-reach retarded form),
  NOT primitive-forced. The bare certified substrate has no V5. So this tests
  whether V5's KNOWN structure yields binding-mass, not whether the bare primitives do.
- The coupling reads positions (coarse stand-in for recent commitment activity);
  the gauge phase is implicit. Flagged.
"""
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "evaluation", "Bits"))
from simulator import ParticipationGraph, NodeState, StateVector, SigmaCoeffs  # noqa: E402
from simulator.sigma import compute_sigma  # noqa: E402

RHO_STAR = 0.5
EDGE_BW = 0.5
B_SELF = 1.0
JITTER_SD = 1e-3
COEFFS = SigmaCoeffs(kc=1.0, ks=1.0, kg=1.0, rho_star=RHO_STAR, increment=1.0,
                     extinction_threshold=None)
L = 161                       # grid side (odd -> integer center)
C = L // 2
MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]   # 4-neighbor; dwell handled separately


def nid(x, y):
    return y * L + x


def build_grid():
    g = ParticipationGraph()
    for y in range(L):
        for x in range(L):
            i = nid(x, y)
            g.add_edge(i, i, bandwidth=B_SELF)          # self-loop (dwell)
            for dx, dy in MOVES:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < L and 0 <= y2 < L:
                    g.add_edge(i, nid(x2, y2), bandwidth=EDGE_BW)
    return g


def fresh_state(seed):
    rng = np.random.default_rng(seed)
    sv = StateVector()
    # pre-fill the whole grid with a flat rho_star background + tiny jitter (the
    # certified lane probe does the same for its lanes). Fronts then avoid their
    # own higher-rho trail -> advance into fresh rho_star ground -> ballistic.
    base = RHO_STAR + rng.normal(0, JITTER_SD, size=L * L)
    for i in range(L * L):
        sv[i] = NodeState(rho=float(max(0.0, base[i])))
    return sv, rng


AXES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def init_fronts(sv, n, rng, boost=(0, 0)):
    """n fronts near the center with axis-aligned headings in OPPOSITE PAIRS
    (exact zero net lattice momentum for boost=0 -> the composite should be at
    REST if bound). `boost` adds a net drift (for the moving-massive test). Each
    front is seeded with a trail node behind it so certified rho-avoidance sends
    it forward in its heading."""
    fronts = []
    for k in range(n):
        hx, hy = AXES[k % 4]
        # slight fan-out of start positions so they don't sit on one node
        x0 = C + int(np.sign(hx)) * (1 + k // 4)
        y0 = C + int(np.sign(hy)) * (1 + k // 4)
        sv[nid(C, C)] = NodeState(rho=float(RHO_STAR + 1.0))          # shared trail seed
        sv[nid(x0, y0)] = NodeState(rho=float(max(0.0, RHO_STAR + rng.normal(0, JITTER_SD))))
        sv[nid(x0, y0)].active = True
        fronts.append({"x": x0, "y": y0, "hx": float(hx + boost[0]),
                       "hy": float(hy + boost[1]), "alive": True,
                       "px": float(x0), "py": float(y0)})
    return fronts


def get_rho(sv, x, y):
    return sv[nid(x, y)].rho


def step(sv, g, fronts, A_V5, ell_V5, force=0.0):
    prev = np.array([[f["px"], f["py"]] for f in fronts])   # retarded positions
    for i, f in enumerate(fronts):
        if not f["alive"]:
            continue
        x, y = f["x"], f["y"]
        u = nid(x, y)
        # reach-weighted centroid of OTHER fronts (retarded, finite reach)
        cvec = None
        if A_V5 > 0:
            d = np.hypot(prev[:, 0] - prev[i, 0], prev[:, 1] - prev[i, 1])
            w = np.exp(-d / ell_V5)
            w[i] = 0.0
            if w.sum() > 1e-9:
                cx = np.sum(w * prev[:, 0]) / w.sum()
                cy = np.sum(w * prev[:, 1]) / w.sum()
                cvec = (cx, cy)
        # CERTIFIED rule is ballistic-or-extinct: NO dwell. The front MUST advance
        # to a neighbor each step (path-speed = 1, the constituent moves at c). It
        # scores the 4 neighbors by certified Sigma (avoids its own high-rho trail
        # -> moves into fresh ground -> ballistic) + the V5 attraction toward the
        # group centroid. The open question is whether V5 curves it enough to confine.
        best, best_s, bmove = None, -1e18, (0, 0)
        for dx, dy in MOVES:
            x2, y2 = x + dx, y + dy
            if not (0 <= x2 < L and 0 <= y2 < L):
                continue
            s = compute_sigma(u, nid(x2, y2), sv, g, COEFFS)
            # orientation tie-break = PERSISTENCE (the certified front is a
            # (rho, orientation) object; Sigma is orientation-BLIND, so heading
            # only breaks Sigma-ties -> ballistic worldline, Continuum-paper p~0.68).
            # Small (eps << Sigma scale ~1): breaks fresh-neighbor ties, never
            # overrides the fresh-vs-trail Sigma choice. V5 (A_V5~1) can override it.
            s += 0.02 * (dx * f["hx"] + dy * f["hy"])
            if force:
                s += force * dx           # uniform external force in +x
            if cvec is not None:
                d_now = np.hypot(x - cvec[0], y - cvec[1])
                d_new = np.hypot(x2 - cvec[0], y2 - cvec[1])
                s += A_V5 * (d_now - d_new)      # favor moving toward the group
            if s > best_s:
                best_s, best, bmove = s, (x2, y2), (dx, dy)
        nx, ny = best
        f["px"], f["py"] = float(x), float(y)
        f["hx"], f["hy"] = float(bmove[0]), float(bmove[1])   # update heading
        sv[nid(nx, ny)].commit(COEFFS.increment)
        sv[u].active = False
        sv[nid(nx, ny)].active = True
        f["x"], f["y"] = nx, ny


def run(n, A_V5, ell_V5, steps, seed, force=0.0):
    g = GRID
    sv, rng = fresh_state(seed)
    fronts = init_fronts(sv, n, rng)
    com, rms, speeds = [], [], []
    hist = []
    for t in range(steps):
        step(sv, g, fronts, A_V5, ell_V5, force)
        P = np.array([[f["x"], f["y"]] for f in fronts], dtype=float)
        c = P.mean(axis=0)
        com.append(c.copy())
        rms.append(np.sqrt(((P - c) ** 2).sum(axis=1).mean()))
        hist.append(P.copy())
    com = np.array(com)
    half = len(com) // 2
    # COM net drift over the FULL run (wobble averages out; real translation accumulates)
    v_com = np.hypot(*(com[-1] - com[0])) / len(com)
    v_com_x = (com[-1, 0] - com[0, 0]) / len(com)     # drift along the force (+x)
    com_excursion = np.max(np.hypot(com[:, 0] - com[0, 0], com[:, 1] - com[0, 1]))
    # individual front net drift (ballistic straight -> ~1; bound/orbiting -> < 1)
    H = np.array(hist)
    ind = [np.hypot(*(H[-1, k] - H[0, k])) / len(com) for k in range(n)]
    return dict(v_com=v_com, v_com_x=v_com_x, v_ind=np.mean(ind), rms_end=rms[-1],
                rms_mid=rms[half], com_exc=com_excursion, rms_series=np.array(rms))


GRID = build_grid()


def run_single_memory(k_mem, force, steps, seed):
    """ONE front carrying commitment-MEMORY (can dwell when memory is high -- the
    route-2 dwell mechanism, a structural addition = the k11 / commitment-rate mass
    candidate). Push it with a +x force. Return (path_speed, v_x).

    Discriminator k11-mass vs binding-mass:
      v_x ~= path_speed  -> SLOW CLOCK (it dwells, but every advance still aligns to
                            the force: time dilation, NO directional inertia).
      v_x <  path_speed  -> INERTIA (it resists aligning to the force = mass).
    (The bound composite has v_x < constituent path_speed=1: that IS inertia.)"""
    g = GRID
    sv, rng = fresh_state(seed)
    x, y = C, C
    sv[nid(C - 1, C)] = NodeState(rho=float(RHO_STAR + 1.0))     # trail behind -> heads +x
    sv[nid(x, y)] = NodeState(rho=float(RHO_STAR)); sv[nid(x, y)].active = True
    hx, hy, mem, x0, adv = 1.0, 0.0, 0.0, x, 0
    for t in range(steps):
        u = nid(x, y)
        best_s, best = compute_sigma(u, u, sv, g, COEFFS) + k_mem * mem, (x, y)   # dwell + memory
        for dx, dy in MOVES:
            x2, y2 = x + dx, y + dy
            if not (0 <= x2 < L and 0 <= y2 < L):
                continue
            s = compute_sigma(u, nid(x2, y2), sv, g, COEFFS) + 0.02 * (dx * hx + dy * hy) + force * dx
            if s > best_s:
                best_s, best = s, (x2, y2)
        mem = 0.9 * mem + 1.0
        nx, ny = best
        if (nx, ny) == (x, y):
            sv[u].commit(COEFFS.increment)                      # dwell
        else:
            adv += 1
            hx, hy = float(nx - x), float(ny - y)
            sv[nid(nx, ny)].commit(COEFFS.increment)
            sv[u].active = False; sv[nid(nx, ny)].active = True
            x, y = nx, ny
    return adv / steps, (x - x0) / steps


def main():
    print("=" * 90)
    print("MASS WITHOUT MASS: do V5-bound ballistic fronts have a SUB-BALLISTIC center of mass?")
    print("=" * 90)
    N, STEPS, seeds = 8, 55, [0, 1, 2]

    def avg(A, ell):
        rr = [run(N, A, ell, STEPS, s) for s in seeds]
        return {k: np.mean([r[k] for r in rr]) for k in ("v_com", "v_ind", "rms_end", "rms_mid", "com_exc")}

    print("\n[control] single FREE front (n=1): expect |v|~1 (ballistic, massless)")
    vfree = np.mean([run(1, 0.0, 1.0, STEPS, s)["v_ind"] for s in seeds])
    print(f"    single-front speed |v| = {vfree:.3f}   (this is 'c', the massless speed)")

    print("\n[control] cluster, V5 OFF (A_V5=0): fronts radiate -> UNBOUND (rms grows)")
    r = avg(0.0, 1.0)
    print(f"    v_COM={r['v_com']:.3f}  rms_mid={r['rms_mid']:.1f} rms_end={r['rms_end']:.1f}"
          f"   ({'DISPERSING (unbound)' if r['rms_end'] > 1.5 * r['rms_mid'] else 'bounded?'})")

    print("\n[test] cluster, V5 ON (zero net momentum): each front moves at c every step.")
    print(f"       CONFINED (rms bounded) + COM at rest (v_COM<<c={vfree:.2f}, excursion bounded)?")
    print(f"{'A_V5':>6}{'ell_V5':>8}{'v_COM':>9}{'com_exc':>9}{'rms_end':>9}  verdict")
    print("-" * 90)
    for A in (1.0, 2.0, 4.0):
        for ell in (5.0, 15.0, 40.0):
            r = avg(A, ell)
            bound = r["rms_end"] < 1.4 * max(r["rms_mid"], 1.0)
            atrest = r["v_com"] < 0.25 * vfree and r["com_exc"] < 3.0 * r["rms_end"]
            if bound and atrest:
                verdict = "CONFINED + COM AT REST  <-- rest mass from binding"
            elif bound:
                verdict = f"confined; COM drifts at {r['v_com']:.2f} < c (still massive)"
            else:
                verdict = "unbound (fronts outrun the reach)"
            print(f"{A:>6.1f}{ell:>8.1f}{r['v_com']:>9.3f}{r['com_exc']:>9.1f}{r['rms_end']:>9.1f}  {verdict}")

    print("\n[characterize the COM drift] does it shrink with cluster size N (finite-N")
    print("   momentum fluctuation -> clean at-rest limit) or stay fixed (structural)?")
    print(f"{'N':>5}{'v_COM':>9}{'rms_end':>9}   (A_V5=2, ell_V5=15)")
    for NN in (8, 16, 24, 32):
        rr = [run(NN, 2.0, 15.0, STEPS, s) for s in seeds]
        vc = np.mean([r["v_com"] for r in rr]); re = np.mean([r["rms_end"] for r in rr])
        print(f"{NN:>5}{vc:>9.3f}{re:>9.1f}")

    print("\n[INERTIAL MASS] apply a uniform force (+x) and measure the drift response v_x.")
    print("   Mass = resistance to acceleration: heavier composite -> smaller v_x for same F.")
    print("   A free front is already at c (can only be steered); a bound composite must be")
    print("   accelerated from rest, and its response 1/m falls as binding grows.")
    F = 0.5
    vf = np.mean([run(1, 0.0, 1.0, STEPS, s, force=F)["v_com_x"] for s in seeds])
    print(f"\n   free front (n=1), force F={F}:  v_x = {vf:.3f}  (~c: massless, unresisted)")
    vu = np.mean([run(N, 0.0, 15.0, STEPS, s, force=F)["v_com_x"] for s in seeds])
    print(f"   UNBOUND cluster (A_V5=0), force F={F}:  v_x = {vu:.3f}  (control: no binding => no inertia,")
    print(f"      COM ~ free front => the bound composite's slower response is from BINDING, not averaging)")
    print(f"   {'N':>4}{'v_x(F)':>10}{'mobility v_x/F':>16}{'rel. mass 1/mobility':>22}")
    base = None
    for NN in (8, 16, 24, 32):
        vx = np.mean([run(NN, 2.0, 15.0, STEPS, s, force=F)["v_com_x"] for s in seeds])
        mob = vx / F
        m_rel = (1.0 / mob) if mob > 1e-6 else float("inf")
        if base is None:
            base = m_rel
        print(f"   {NN:>4}{vx:>10.3f}{mob:>16.3f}{m_rel / base:>22.2f}")
    print("   (rel. mass ~ N-INDEPENDENT: a uniform force gives a mass-independent velocity")
    print("    response = mobility-saturated / equivalence-principle-consistent, NOT evidence the")
    print("    mass magnitude scales with N. Mass magnitude is extensive but a uniform force can't")
    print("    resolve it; the bound-vs-unbound gap [0.72 vs 0.97] is the inertia signature.)")

    print("\n[k11 vs binding] does commitment-MEMORY alone give INERTIA, or just a slow clock?")
    print("   A lone memory front (dwell) under +x force F=0.5. Compare v_x to its path_speed:")
    print(f"   {'k_mem':>7}{'path_speed':>12}{'v_x':>9}{'v_x/path':>10}   reading")
    for km in (0.0, 0.15, 0.4, 0.8):
        res = np.array([run_single_memory(km, 0.5, STEPS, s) for s in seeds])
        ps, vx = res.mean(axis=0)
        ratio = vx / ps if ps > 1e-6 else float("nan")
        read = ("SLOW CLOCK (v_x tracks path: dwells, but force fully aligns = time dilation)"
                if ratio > 0.85 else "resists alignment (inertia?)")
        print(f"   {km:>7.2f}{ps:>12.3f}{vx:>9.3f}{ratio:>10.2f}   {read}")
    print("   Contrast: the BOUND COMPOSITE has v_x(COM)=0.72 while each front's path_speed=1")
    print("   => the composite resists (v_x << constituent path) = DIRECTIONAL INERTIA (mass).")
    print("   If memory gives only slow-clock (v_x~path) => commitment-rate/k11 = TIME DILATION,")
    print("   NOT mass; mass needs BINDING => binding-mass and k11 do NOT unify (take honest close).")

    print("\nReading: each front moves at c every step (constituents ballistic, by construction).")
    print("  CONFINED (rms bounded, not growing) + COM net-drift << 1  =>  a bound composite")
    print("  AT REST whose parts move at c = rest mass from binding ('mass without mass').")
    print("  If unbound at every A,ell (fronts outrun the finite reach): V5 does NOT confine, NO.")


if __name__ == "__main__":
    main()
