"""ED-SC 3.3 Filter-Geometry Scan.

Pre-registered in theory/ED_SC_3_3_FilterGeometry_Scope.md.

Sweeps the motif-filter geometry (α_filt, N_req) across a 5×4 grid
anchored at the certified canonical operating point (ξ=1.7575 lu,
L_ray=1.898 lu, L_ray/ξ=1.08, Regime I), with a 5-point hinge
sub-sweep per cell at L_ray/ξ ∈ {1.00, 1.05, 1.10, 1.15, 1.20}.

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Canonical ξ method: 40-snapshot half-decay (burn-in 100, snap every
10, GR-SC 1.7 density channel) — matches ed_sc_3_1_xi_canonical.py
and ed_sc_3_2_6_resonance_scan_v2.py.

Resonance-window exclusions (per ED-SC 3.2.6 rev. 2):
  Window A: L_ray ∈ [2.50, 2.80]   → forbidden
  Window B: L_ray ∈ [3.50, 3.90]   → forbidden

The hinge sub-sweep L_ray ∈ {1.758, 1.846, 1.934, 2.022, 2.110} lu
(ξ·{1.00,…,1.20}) lies entirely below Window A.

Writes:
  outputs/ed_sc_3_3/pool_alpha{α}_Nreq{N}.csv           (20 files)
  outputs/ed_sc_3_3/summary_alpha{α}_Nreq{N}.json       (20 files)
  outputs/ed_sc_3_3/filter_geometry_summary.json        (1 master)

No simulator constants are mutated. Deterministic given seeds.
"""
import csv
import json
import os
import sys
import time
import numpy as np
from numpy.fft import fft2, ifft2, fftshift

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr  # noqa: E402

from ED_Update_Rule import ed_step_mobility  # noqa: E402

# ---------------------------------------------------------------------------
# Canonical constants (inherited, NOT mutated)
# ---------------------------------------------------------------------------
XI_CANONICAL = 1.7575325729470939
XI_GUARDRAIL_TOL = 0.20
XI_GUARDRAIL_MIN_PASS = 8  # ≥8/10 seeds must pass (see §5.4)
XI_BURN_IN = 100
XI_SNAP_EVERY = 10

# Canonical operating-point L_ray (ED-SC 3.1 rev. 3)
L_RAY_CANONICAL = 1.898  # L_ray/ξ = 1.08

# Resonance-forbidden windows (ED-SC 3.2.6 rev. 2)
WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

# ---------------------------------------------------------------------------
# Filter-geometry grid (20 cells)
# ---------------------------------------------------------------------------
ALPHA_FILT_GRID = [0.10, 0.15, 0.20, 0.25, 0.30]
N_REQ_GRID = [2, 3, 4, 5]

# ---------------------------------------------------------------------------
# Per-cell hinge sub-sweep (5 points)
# ---------------------------------------------------------------------------
HINGE_OVER_XI = [1.00, 1.05, 1.10, 1.15, 1.20]
HINGE_L_RAY = [round(r * XI_CANONICAL, 4) for r in HINGE_OVER_XI]

OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_3")


# ---------------------------------------------------------------------------
# ξ measurement (verbatim from ed_sc_3_1_xi_canonical.py)
# ---------------------------------------------------------------------------
def xi_halfdecay(field, dx=1.0):
    """GR-SC 1.7 radial half-decay correlation length, density channel."""
    N = field.shape[0]
    f = field - np.mean(field)
    F = fft2(f)
    C = fftshift(np.real(ifft2(F * np.conj(F)))) / (N * N)
    c0 = C[N // 2, N // 2]
    if c0 <= 0:
        return float('nan')
    y, x = np.indices(C.shape)
    r = np.sqrt((x - N // 2) ** 2 + (y - N // 2) ** 2).astype(int)
    rmax = N // 2
    prof = np.empty(rmax)
    for k in range(rmax):
        mask = (r == k)
        prof[k] = C[mask].mean() if mask.any() else 0.0
    prof /= c0
    for k in range(1, rmax):
        if prof[k] <= 0.5:
            if prof[k - 1] == prof[k]:
                return float(k) * dx
            return float(k - 1 + (prof[k - 1] - 0.5)
                         / (prof[k - 1] - prof[k])) * dx
    return float(rmax) * dx


def run_scenario_with_xi(seed):
    """Evolve ED-SIM mobility engine, record 40-snapshot xi, return final."""
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.3, 0.7, size=(fr.SIZE, fr.SIZE))
    xis = []
    for step in range(fr.STEPS):
        p = ed_step_mobility(
            p, alpha=fr.ALPHA0, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=fr.NOISE0, rng=rng,
        )
        if step >= XI_BURN_IN and (step - XI_BURN_IN) % XI_SNAP_EVERY == 0:
            xis.append(xi_halfdecay(p))
    return p, xis


# ---------------------------------------------------------------------------
# Resonance-window guard
# ---------------------------------------------------------------------------
def in_window(L, win):
    return win[0] <= L <= win[1]


def assert_no_resonance():
    """Hard-fail if any planned L_ray falls inside Window A or B."""
    for L in HINGE_L_RAY:
        if in_window(L, WINDOW_A) or in_window(L, WINDOW_B):
            raise RuntimeError(
                f"Planned L_ray={L} lu intersects forbidden "
                f"resonance window A{WINDOW_A} or B{WINDOW_B} — "
                "refusing to launch.")


# ---------------------------------------------------------------------------
# Motif collection (parameterised by α_filt, N_req, L_ray)
# ---------------------------------------------------------------------------
def endpoints_of(saddle, L_ray):
    e_neg = saddle["e_neg"]
    e_pos = saddle["e_pos"]
    out = []
    for e, sign in ((e_neg, +1), (e_neg, -1), (e_pos, +1), (e_pos, -1)):
        di = int(round(sign * e[0] * L_ray))
        dj = int(round(sign * e[1] * L_ray))
        r = float(np.sqrt(di * di + dj * dj))
        out.append([di, dj, r])
    return out


def collect_motifs(field_cache, alpha_filt, n_req, L_ray):
    pooled = []
    per_motif = []
    for seed, (p, E, p_hat, p_std) in field_cache.items():
        sads = fr.find_morse_saddles(E)
        for s in sads:
            if not fr.motif_pass(s, E, p_hat, p_std,
                                 alpha_filt, L_ray, n_req):
                continue
            pooled.append(s["ratio"])
            per_motif.append({
                "seed": int(seed),
                "i": int(s["i"]),
                "j": int(s["j"]),
                "lam_neg": float(s["lam_neg"]),
                "lam_pos": float(s["lam_pos"]),
                "ratio": float(s["ratio"]),
                "L_ray": L_ray,
            })
    return pooled, per_motif


# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------
def bootstrap_median_iqr(values, B=4000, rng_seed=99):
    v = np.asarray([x for x in values if np.isfinite(x)])
    if len(v) < 3:
        return dict(n=int(len(v)), median=None, iqr=None,
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


def hinge_flatness(hinge_points):
    """max |S2_i - S2_j| / mean(S2) across the hinge sub-sweep."""
    s2s = [hp["S2_iqr"] for hp in hinge_points
           if hp["S2_iqr"] is not None and np.isfinite(hp["S2_iqr"])]
    if len(s2s) < 2:
        return None
    mean_s2 = float(np.mean(s2s))
    if mean_s2 == 0:
        return None
    span = float(max(s2s) - min(s2s))
    return span / mean_s2


# ---------------------------------------------------------------------------
# Per-cell driver
# ---------------------------------------------------------------------------
def run_cell(alpha_filt, n_req, field_cache):
    t0 = time.time()
    hinge_points = []
    pool_all = []
    per_motif_all = []
    for ratio, L_ray in zip(HINGE_OVER_XI, HINGE_L_RAY):
        t1 = time.time()
        pooled, per_motif = collect_motifs(
            field_cache, alpha_filt, n_req, L_ray)
        bs = bootstrap_median_iqr(pooled)
        s3 = tail_log_slope(pooled)
        hp = {
            "L_ray_over_xi": ratio,
            "L_ray_lattice_units": L_ray,
            "N_motifs": int(bs["n"]),
            "S1_median": bs["median"],
            "S1_ci16_84": bs["median_ci"],
            "S2_iqr": bs["iqr"],
            "S2_ci16_84": bs["iqr_ci"],
            "S3_tail_slope": s3,
            "wall_seconds": time.time() - t1,
        }
        hinge_points.append(hp)
        pool_all.extend([{"L_ray": L_ray,
                          "L_ray_over_xi": ratio,
                          "ratio": r} for r in pooled])
        per_motif_all.extend(per_motif)
        print(f"  [α={alpha_filt:.2f} N={n_req} L/ξ={ratio:.2f}] "
              f"N={bs['n']} S1={bs['median']} S2={bs['iqr']} "
              f"t={time.time()-t1:.2f}s",
              file=sys.stderr)

    # Pooled statistics across hinge sub-sweep
    pooled_ratios = [row["ratio"] for row in pool_all]
    bs_pool = bootstrap_median_iqr(pooled_ratios)
    s3_pool = tail_log_slope(pooled_ratios)
    flatness = hinge_flatness(hinge_points)

    cell = {
        "alpha_filt": alpha_filt,
        "N_req": n_req,
        "L_ray_canonical_lattice_units": L_RAY_CANONICAL,
        "hinge_over_xi_grid": HINGE_OVER_XI,
        "hinge_L_ray_grid": HINGE_L_RAY,
        "hinge_points": hinge_points,
        "pooled": {
            "N_motifs": int(bs_pool["n"]),
            "S1_median": bs_pool["median"],
            "S1_ci16_84": bs_pool["median_ci"],
            "S2_iqr": bs_pool["iqr"],
            "S2_ci16_84": bs_pool["iqr_ci"],
            "S3_tail_slope": s3_pool,
        },
        "hinge_flatness_rel_span": flatness,
        "hinge_flatness_flag": (flatness is not None and flatness > 0.20),
        "wall_seconds_cell": time.time() - t0,
    }

    # Write per-cell CSV and JSON
    alpha_tag = f"{alpha_filt:.2f}".replace(".", "p")
    csv_path = os.path.join(
        OUT_DIR, f"pool_alpha{alpha_tag}_Nreq{n_req}.csv")
    json_path = os.path.join(
        OUT_DIR, f"summary_alpha{alpha_tag}_Nreq{n_req}.json")

    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["L_ray", "L_ray_over_xi", "ratio"])
        for row in pool_all:
            w.writerow([row["L_ray"], row["L_ray_over_xi"], row["ratio"]])

    with open(json_path, "w") as f:
        json.dump({
            **cell,
            "simulator_of_record":
                "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
            "xi_canonical_lattice_units": XI_CANONICAL,
            "resonance_windows_excluded": {
                "A": list(WINDOW_A), "B": list(WINDOW_B)},
        }, f, indent=2)

    return cell


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    assert_no_resonance()

    t_master = time.time()

    # -- 1. Build shared field cache + canonical 40-snapshot ξ ---------------
    print("Evolving 10 seeds with canonical 40-snapshot xi sampling...",
          file=sys.stderr)
    field_cache = {}
    xi_per_seed = {}
    xi_snapshots_per_seed = {}
    for seed in fr.SEEDS:
        ts = time.time()
        p_final, xis = run_scenario_with_xi(seed)
        xis_finite = [x for x in xis if np.isfinite(x)]
        xi_mean = float(np.mean(xis_finite)) if xis_finite else float('nan')
        xi_per_seed[int(seed)] = xi_mean
        xi_snapshots_per_seed[int(seed)] = xis
        E = fr.smooth_field(p_final)
        field_cache[seed] = (p_final, E,
                             float(p_final.mean()), float(p_final.std()))
        print(f"  seed={seed}  xi={xi_mean:.4f}  "
              f"snaps={len(xis_finite)}  t={time.time()-ts:.1f}s",
              file=sys.stderr)

    n_pass = sum(1 for x in xi_per_seed.values()
                 if np.isfinite(x)
                 and abs(x - XI_CANONICAL) / XI_CANONICAL < XI_GUARDRAIL_TOL)
    xi_guardrail = {
        "method": ("40-snapshot-per-seed canonical average, "
                   "GR-SC 1.7 half-decay, density channel "
                   "(matches ed_sc_3_1_xi_canonical.py)"),
        "burn_in": XI_BURN_IN,
        "snap_every": XI_SNAP_EVERY,
        "tolerance": XI_GUARDRAIL_TOL,
        "xi_canonical": XI_CANONICAL,
        "per_seed": xi_per_seed,
        "per_seed_snapshots": xi_snapshots_per_seed,
        "n_pass": n_pass,
        "min_pass": XI_GUARDRAIL_MIN_PASS,
        "pass": n_pass >= XI_GUARDRAIL_MIN_PASS,
    }

    # -- 2. Iterate the 5×4 cell grid ---------------------------------------
    cells = []
    for alpha_filt in ALPHA_FILT_GRID:
        for n_req in N_REQ_GRID:
            print(f"Cell α={alpha_filt} N_req={n_req} ...",
                  file=sys.stderr)
            cell = run_cell(alpha_filt, n_req, field_cache)
            cells.append(cell)

    # -- 3. Master summary --------------------------------------------------
    # 5 × 4 grid of (S1, S2, verdict) indexed by (α_filt, N_req)
    grid = {}
    resonance_flags = []
    for cell in cells:
        key = f"alpha{cell['alpha_filt']:.2f}_Nreq{cell['N_req']}"
        if cell["hinge_flatness_flag"]:
            flag_reason = (
                "hinge sub-sweep S2 relative span "
                f"{cell['hinge_flatness_rel_span']:.3f} > 0.20 "
                "(possible new resonance)")
            resonance_flags.append({
                "cell": key,
                "alpha_filt": cell["alpha_filt"],
                "N_req": cell["N_req"],
                "reason": flag_reason,
            })
        verdict = (
            "GuardrailFailure" if not xi_guardrail["pass"]
            else ("Refuted" if cell["hinge_flatness_flag"]
                  else "Confirmed"))
        grid[key] = {
            "alpha_filt": cell["alpha_filt"],
            "N_req": cell["N_req"],
            "S1_pooled": cell["pooled"]["S1_median"],
            "S2_pooled": cell["pooled"]["S2_iqr"],
            "S3_pooled": cell["pooled"]["S3_tail_slope"],
            "N_pooled": cell["pooled"]["N_motifs"],
            "hinge_flatness_rel_span": cell["hinge_flatness_rel_span"],
            "hinge_flatness_flag": cell["hinge_flatness_flag"],
            "verdict": verdict,
        }

    out = {
        "method": ("ED-SC 3.3 filter-geometry sweep at certified "
                   "canonical operating point"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "L_ray_canonical_lattice_units": L_RAY_CANONICAL,
        "alpha_filt_grid": ALPHA_FILT_GRID,
        "N_req_grid": N_REQ_GRID,
        "hinge_over_xi_grid": HINGE_OVER_XI,
        "hinge_L_ray_grid": HINGE_L_RAY,
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "seeds": list(fr.SEEDS),
        "canonical_params": {
            "alpha": fr.ALPHA0, "gamma": fr.GAMMA,
            "noise_sigma": fr.NOISE0,
            "mobility_exp": fr.MOBILITY_EXP,
            "steps": fr.STEPS, "size": fr.SIZE,
            "dt": fr.DT,
        },
        "xi_guardrail": xi_guardrail,
        "grid": grid,
        "resonance_flags": resonance_flags,
        "wall_seconds_total": time.time() - t_master,
    }

    master_path = os.path.join(OUT_DIR, "filter_geometry_summary.json")
    with open(master_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\nWrote master summary → {master_path}", file=sys.stderr)
    print(json.dumps({
        "xi_guardrail_pass": xi_guardrail["pass"],
        "n_cells": len(cells),
        "n_resonance_flags": len(resonance_flags),
        "wall_seconds_total": out["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
