"""ED-SC 3.2.6 Ray-Budget Resonance Scan.

Sub-lattice L_ray scan across the two shoulders detected in ED-SC 3.2.5
(L_ray ≈ 2.64 and L_ray ≈ 3.69 lu). Records ray-endpoint lattice offsets
and shell radii per admitted motif to test the integer-lattice-shell
hypothesis explicitly.

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility
xi_canonical = 1.7575325729470939  (outputs/ed_sc_3_1/xi_canonical.json)

Writes:
  outputs/ed_sc_3_2_6/resonance_summary.json
"""
import json
import os
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr

from ED_Update_Rule import ed_step_mobility

XI_CANONICAL = 1.7575325729470939
XI_GUARDRAIL_TOL = 0.20

# Window A: bracket L_ray ≈ 2.64 (L_ray/xi ≈ 1.50)
GRID_A = [round(2.50 + 0.02 * k, 3) for k in range(16)]   # 2.50..2.80
# Window B: bracket L_ray ≈ 3.69 (L_ray/xi ≈ 2.10)
GRID_B = [round(3.50 + 0.02 * k, 3) for k in range(21)]   # 3.50..3.90

ALPHA_FILT = 0.25
N_REQ = 4


def run_scenario(seed):
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.3, 0.7, size=(fr.SIZE, fr.SIZE))
    for _ in range(fr.STEPS):
        p = ed_step_mobility(
            p, alpha=fr.ALPHA0, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=fr.NOISE0, rng=rng,
        )
    return p


def xi_from_field(p):
    """Radial half-decay of 2D autocorrelation on density field (density channel)."""
    f = p - p.mean()
    F = np.fft.fft2(f)
    ac = np.fft.ifft2(F * np.conj(F)).real
    ac = np.fft.fftshift(ac)
    ac /= ac.max()
    Ny, Nx = ac.shape
    cy, cx = Ny // 2, Nx // 2
    y, x = np.indices(ac.shape)
    r = np.sqrt((y - cy) ** 2 + (x - cx) ** 2)
    r_int = r.astype(int)
    rmax = min(cy, cx)
    radial = np.array([ac[r_int == k].mean() for k in range(rmax)])
    # half-decay crossing
    for k in range(1, rmax):
        if radial[k] <= 0.5:
            # linear interp
            return float((k - 1) + (radial[k - 1] - 0.5) /
                         (radial[k - 1] - radial[k]))
    return float(rmax)


def endpoints_of(saddle, L_ray):
    """Return list of [di, dj, r] for the 4 principal-axis rays."""
    e_neg = saddle["e_neg"]
    e_pos = saddle["e_pos"]
    out = []
    for e, sign in ((e_neg, +1), (e_neg, -1), (e_pos, +1), (e_pos, -1)):
        di = int(round(sign * e[0] * L_ray))
        dj = int(round(sign * e[1] * L_ray))
        r = float(np.sqrt(di * di + dj * dj))
        out.append([di, dj, r])
    return out


def collect_motifs(field_cache, l_ray_val):
    pooled = []
    per_motif = []
    shell_hist = {}
    for seed, (p, E, p_hat, p_std) in field_cache.items():
        sads = fr.find_morse_saddles(E)
        for s in sads:
            if not fr.motif_pass(s, E, p_hat, p_std,
                                 ALPHA_FILT, l_ray_val, N_REQ):
                continue
            ep = endpoints_of(s, l_ray_val)
            pooled.append(s["ratio"])
            per_motif.append({
                "seed": seed, "i": s["i"], "j": s["j"],
                "lam_neg": s["lam_neg"], "lam_pos": s["lam_pos"],
                "ratio": s["ratio"],
                "endpoints": ep,
            })
            for _, _, r in ep:
                key = f"{r:.3f}"
                shell_hist[key] = shell_hist.get(key, 0) + 1
    return pooled, per_motif, shell_hist


def bootstrap_median_iqr(values, B=4000, rng_seed=99):
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 3:
        return dict(n=len(v), median=None, iqr=None,
                    median_ci=[None, None], iqr_ci=[None, None])
    rng = np.random.default_rng(rng_seed)
    meds, iqrs = [], []
    for _ in range(B):
        smp = rng.choice(v, size=len(v), replace=True)
        meds.append(np.median(smp))
        iqrs.append(np.quantile(smp, 0.75) - np.quantile(smp, 0.25))
    return dict(
        n=int(len(v)),
        median=float(np.median(v)),
        iqr=float(np.quantile(v, 0.75) - np.quantile(v, 0.25)),
        median_ci=[float(np.quantile(meds, 0.16)),
                   float(np.quantile(meds, 0.84))],
        iqr_ci=[float(np.quantile(iqrs, 0.16)),
                float(np.quantile(iqrs, 0.84))],
    )


def tail_log_slope(values):
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 8:
        return None
    vs = np.sort(v)
    n = len(vs)
    k = max(4, int(0.4 * n))
    tail = vs[-k:]
    ranks = np.arange(1, k + 1)
    pexc = (k - ranks + 0.5) / n
    mask = pexc > 0
    if mask.sum() < 4:
        return None
    slope, _ = np.polyfit(tail[mask], np.log(pexc[mask]), 1)
    return float(slope)


def scan_window(label, grid, field_cache):
    out = {}
    L_ratios = []
    for L_ray_val in grid:
        t1 = time.time()
        pooled, per_motif, shell_hist = collect_motifs(field_cache, L_ray_val)
        bs = bootstrap_median_iqr(pooled)
        s3 = tail_log_slope(pooled)
        ratio = L_ray_val / XI_CANONICAL
        L_ratios.append(ratio)
        key = f"Lray_{L_ray_val:.2f}"
        out[key] = {
            "L_ray_lattice_units": L_ray_val,
            "L_ray_over_xi": ratio,
            "N_motifs": int(bs["n"]),
            "S1_median": bs["median"],
            "S1_ci16_84": bs["median_ci"],
            "S2_iqr": bs["iqr"],
            "S2_ci16_84": bs["iqr_ci"],
            "S3_tail_slope": s3,
            "shell_histogram": shell_hist,
            "pool_ratios": pooled,
            "per_motif": per_motif,
            "wall_seconds": time.time() - t1,
        }
        print(f"[{label}|{key}] L/xi={ratio:.3f}  N={bs['n']}  "
              f"S1={bs['median']}  S2={bs['iqr']}  "
              f"t={time.time()-t1:.2f}s", file=sys.stderr)
    return out, L_ratios


def detect_jumps(window):
    """Find L_ray points where |dS2| > 3× median neighbouring derivative."""
    keys = list(window.keys())
    s2 = [window[k]["S2_iqr"] for k in keys]
    Ls = [window[k]["L_ray_lattice_units"] for k in keys]
    if any(v is None for v in s2) or len(s2) < 3:
        return []
    dS2 = [abs(s2[i + 1] - s2[i]) for i in range(len(s2) - 1)]
    med = float(np.median(dS2)) if dS2 else 0.0
    jumps = []
    for i, d in enumerate(dS2):
        if d > 3.0 * med and med > 0:
            jumps.append({"L_ray": Ls[i + 1], "L_ray_prev": Ls[i],
                          "dS2": d, "threshold": 3.0 * med})
    return jumps


def shell_shift(window, jump):
    """Report dominant shell radii on each side of a jump."""
    L_prev = jump["L_ray_prev"]
    L_next = jump["L_ray"]
    k_prev = f"Lray_{L_prev:.2f}"
    k_next = f"Lray_{L_next:.2f}"
    h_prev = window[k_prev]["shell_histogram"]
    h_next = window[k_next]["shell_histogram"]
    def top3(h):
        return sorted(h.items(), key=lambda kv: -kv[1])[:3]
    return {"prev_top3": top3(h_prev), "next_top3": top3(h_next)}


def main():
    t0 = time.time()

    # Build field cache + xi guardrail
    print("Evolving 10 seeds and measuring xi per seed...", file=sys.stderr)
    field_cache = {}
    xi_per_seed = {}
    for seed in fr.SEEDS:
        ts = time.time()
        p = run_scenario(seed)
        E = fr.smooth_field(p)
        field_cache[seed] = (p, E, float(p.mean()), float(p.std()))
        xi_per_seed[seed] = xi_from_field(p)
        print(f"  seed={seed}  xi={xi_per_seed[seed]:.3f}  "
              f"t={time.time()-ts:.1f}s", file=sys.stderr)

    n_pass = sum(1 for x in xi_per_seed.values()
                 if abs(x - XI_CANONICAL) / XI_CANONICAL < XI_GUARDRAIL_TOL)
    xi_guardrail = {
        "tolerance": XI_GUARDRAIL_TOL,
        "xi_canonical": XI_CANONICAL,
        "per_seed": xi_per_seed,
        "n_pass": n_pass,
        "pass": n_pass >= 9,
    }

    # Windows
    print("Window A scan...", file=sys.stderr)
    win_A, Lr_A = scan_window("A", GRID_A, field_cache)
    print("Window B scan...", file=sys.stderr)
    win_B, Lr_B = scan_window("B", GRID_B, field_cache)

    # Jump detection + shell-shift report
    jumps_A = detect_jumps(win_A)
    jumps_B = detect_jumps(win_B)
    for j in jumps_A:
        j["shell_shift"] = shell_shift(win_A, j)
    for j in jumps_B:
        j["shell_shift"] = shell_shift(win_B, j)

    # Verdict:
    #   Confirmed iff at least one jump in each window aligns with a
    #   change of dominant shell radii AND guardrail passes.
    def shells_differ(js):
        for j in js:
            pt = set(k for k, _ in j["shell_shift"]["prev_top3"])
            nt = set(k for k, _ in j["shell_shift"]["next_top3"])
            if pt != nt:
                return True
        return False

    r1_A = len(jumps_A) > 0
    r1_B = len(jumps_B) > 0
    r2_A = shells_differ(jumps_A) if r1_A else False
    r2_B = shells_differ(jumps_B) if r1_B else False

    verdict = ("Confirmed"
               if (xi_guardrail["pass"] and r1_A and r1_B and r2_A and r2_B)
               else "Refuted")

    out = {
        "method": ("Sub-lattice L_ray scan across two shoulders "
                   "(ray-budget resonance diagnostic)"),
        "simulator": ("r2_grf_falsifier_tests.py + "
                      "ED_Update_Rule.ed_step_mobility"),
        "xi_canonical_lattice_units": XI_CANONICAL,
        "xi_guardrail": xi_guardrail,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "seeds": fr.SEEDS,
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE,
        },
        "window_A": {
            "L_ray_grid": GRID_A,
            "L_ray_over_xi_grid": Lr_A,
            "per_grid": win_A,
            "jumps": jumps_A,
        },
        "window_B": {
            "L_ray_grid": GRID_B,
            "L_ray_over_xi_grid": Lr_B,
            "per_grid": win_B,
            "jumps": jumps_B,
        },
        "resonance_verdict": verdict,
        "wall_seconds_total": time.time() - t0,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
