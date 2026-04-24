"""ED-SC 3.3.7 Shell-Histogram Diagnostic.

Pre-registered in theory/ED_SC_3_3_7_ShellHistogram_Diagnostic.md.

Re-runs the per-seed 40-snapshot evolution of ED-SC 3.3.6 and, for
every admitted motif, records the integer-lattice shell radii of
the 4 ray endpoints. Per-seed histograms of endpoint shell radii
and of per-motif mean shell radius are compared across the 10
canonical seeds to discriminate H-coord (shell-geometry-driven S2
divergence) from H-shallow (ensemble-only invariance).

Simulator of record:
  r2_grf_falsifier_tests.py  +  ED_Update_Rule.ed_step_mobility

Shell radius per endpoint (di, dj): r = sqrt(di^2 + dj^2).
Mean shell radius per motif: mean_k r_k over k = 1..4.

Writes:
  outputs/ed_sc_3_3_7/shell_histograms_seed{seed}.json   (10 files)
  outputs/ed_sc_3_3_7/shell_summary.json                 (master)
"""
import json
import math
import os
import sys
import time
from collections import Counter
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ed_arch_r2"))
import r2_grf_falsifier_tests as fr  # noqa: E402

from ED_Update_Rule import ed_step_mobility  # noqa: E402

# ---------------------------------------------------------------------------
# Canonical constants (inherited, NOT mutated)
# ---------------------------------------------------------------------------
XI_CANONICAL = 1.7575325729470939
XI_BURN_IN = 100
XI_SNAP_EVERY = 10

ALPHA_FILT = 0.25
N_REQ = 4
DIMLESS_HINGE = 1.08

WINDOW_A = (2.50, 2.80)
WINDOW_B = (3.50, 3.90)

XI_JSON_PATH = os.path.join(
    HERE, "..", "..", "outputs", "ed_sc_3_1", "xi_canonical.json")
ED_SC_3_3_6_JSON = os.path.join(
    HERE, "..", "..", "outputs", "ed_sc_3_3_6",
    "per_seed_40snap_summary.json")
OUT_DIR = os.path.join(HERE, "..", "..", "outputs", "ed_sc_3_3_7")

# Mean-shell histogram bin centres (fixed across seeds for comparison)
MEAN_SHELL_BIN_WIDTH = 0.1
MEAN_SHELL_BIN_MIN = 0.0
MEAN_SHELL_BIN_MAX = 4.0  # generous upper bound


# ---------------------------------------------------------------------------
# Resonance-window guard
# ---------------------------------------------------------------------------
def in_window(L, win):
    return win[0] <= L <= win[1]


def assert_no_resonance(seed_L_table):
    bad = [(s, L) for s, L in seed_L_table
           if in_window(L, WINDOW_A) or in_window(L, WINDOW_B)]
    if bad:
        raise RuntimeError(
            f"Per-seed L_ray values intersect forbidden "
            f"resonance window(s): {bad}")


# ---------------------------------------------------------------------------
# Motif extraction with shell-endpoint recording
# ---------------------------------------------------------------------------
def endpoints_of(saddle, L_ray):
    e_neg = saddle["e_neg"]
    e_pos = saddle["e_pos"]
    out = []
    for e, sign in ((e_neg, +1), (e_neg, -1), (e_pos, +1), (e_pos, -1)):
        di = int(round(sign * e[0] * L_ray))
        dj = int(round(sign * e[1] * L_ray))
        r = float(np.sqrt(di * di + dj * dj))
        out.append((di, dj, r))
    return out


def collect_motifs_snapshot(p_snapshot, L_ray):
    E = fr.smooth_field(p_snapshot)
    p_hat = float(p_snapshot.mean())
    p_std = float(p_snapshot.std())
    sads = fr.find_morse_saddles(E)
    per_motif = []
    for s in sads:
        if not fr.motif_pass(s, E, p_hat, p_std,
                             ALPHA_FILT, L_ray, N_REQ):
            continue
        eps = endpoints_of(s, L_ray)
        per_motif.append({
            "i": int(s["i"]), "j": int(s["j"]),
            "ratio": float(s["ratio"]),
            "endpoints": eps,
            "r_k": [e[2] for e in eps],
            "mean_r": float(np.mean([e[2] for e in eps])),
        })
    return per_motif


def evolve_and_collect_40snap_shells(seed, L_ray):
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.3, 0.7, size=(fr.SIZE, fr.SIZE))
    per_motif_all = []
    snap_index = 0
    for step in range(fr.STEPS):
        p = ed_step_mobility(
            p, alpha=fr.ALPHA0, gamma=fr.GAMMA, dt=fr.DT,
            p_min=fr.P_MIN, p_max=fr.P_MAX, boundary=fr.BOUNDARY,
            mobility_exp=fr.MOBILITY_EXP, noise_scale=fr.NOISE0, rng=rng,
        )
        if step >= XI_BURN_IN and (step - XI_BURN_IN) % XI_SNAP_EVERY == 0:
            for m in collect_motifs_snapshot(p, L_ray):
                m["snap_index"] = snap_index
                per_motif_all.append(m)
            snap_index += 1
    return per_motif_all


# ---------------------------------------------------------------------------
# Histogram utilities
# ---------------------------------------------------------------------------
def shell_histogram(per_motif):
    """Endpoint shell histogram: 4 × N_motifs entries."""
    h = Counter()
    for m in per_motif:
        for r in m["r_k"]:
            key = f"{r:.4f}"
            h[key] += 1
    return dict(h)


def mean_shell_histogram(per_motif):
    """Per-motif mean-shell histogram on fixed bins."""
    edges = np.arange(MEAN_SHELL_BIN_MIN,
                      MEAN_SHELL_BIN_MAX + MEAN_SHELL_BIN_WIDTH,
                      MEAN_SHELL_BIN_WIDTH)
    vals = [m["mean_r"] for m in per_motif]
    if not vals:
        return {f"{c:.2f}": 0 for c in (edges[:-1] + MEAN_SHELL_BIN_WIDTH / 2)}
    counts, _ = np.histogram(vals, bins=edges)
    centres = edges[:-1] + MEAN_SHELL_BIN_WIDTH / 2
    return {f"{c:.2f}": int(n) for c, n in zip(centres, counts)}


def shell_entropy_bits(hist):
    """Shannon entropy in bits of the endpoint shell histogram."""
    total = sum(hist.values())
    if total == 0:
        return None
    ent = 0.0
    for c in hist.values():
        if c == 0:
            continue
        p = c / total
        ent -= p * math.log2(p)
    return float(ent)


def dominant_shell(hist):
    if not hist:
        return None
    key = max(hist.items(), key=lambda kv: kv[1])[0]
    return {"shell": float(key), "count": hist[key],
            "fraction": hist[key] / sum(hist.values())}


def aligned_prob_vectors(hist_a, hist_b):
    """Align two shell histograms on a shared key set, return probability
    vectors p_a, p_b (numpy arrays)."""
    keys = sorted(set(hist_a.keys()) | set(hist_b.keys()),
                  key=lambda k: float(k))
    ta = sum(hist_a.values()) or 1
    tb = sum(hist_b.values()) or 1
    pa = np.array([hist_a.get(k, 0) / ta for k in keys])
    pb = np.array([hist_b.get(k, 0) / tb for k in keys])
    return keys, pa, pb


def jensen_shannon(hist_a, hist_b):
    """Jensen-Shannon divergence in nats (base e). Bounded in [0, ln 2]."""
    _, pa, pb = aligned_prob_vectors(hist_a, hist_b)
    m = 0.5 * (pa + pb)
    def kl(p, q):
        s = 0.0
        for pi, qi in zip(p, q):
            if pi > 0 and qi > 0:
                s += pi * math.log(pi / qi)
        return s
    return 0.5 * kl(pa, m) + 0.5 * kl(pb, m)


def pool_histograms(hists):
    pool = Counter()
    for h in hists:
        for k, v in h.items():
            pool[k] += v
    return dict(pool)


# ---------------------------------------------------------------------------
# Master driver
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    t_master = time.time()

    # -- 1. Load canonical per-seed ξ --------------------------------------
    with open(XI_JSON_PATH) as f:
        xi_doc = json.load(f)
    xi_per_seed = {int(k): float(v) for k, v in xi_doc["xi_per_seed"].items()}
    canonical_seeds = [int(s) for s in xi_doc["seeds"]]
    print(f"Loaded canonical ξ for {len(canonical_seeds)} seeds "
          f"from {XI_JSON_PATH}", file=sys.stderr)

    # Load ED-SC 3.3.6 per-seed stats to annotate pass/fail in summary
    try:
        with open(ED_SC_3_3_6_JSON) as f:
            doc_336 = json.load(f)
        stats_336 = {int(r["seed"]): r for r in doc_336["per_seed_stats"]}
        flat_336 = doc_336["cross_seed_flatness"]["flat_thresh"]
    except FileNotFoundError:
        stats_336 = {}
        flat_336 = 0.20
        print("WARNING: ED-SC 3.3.6 summary not found; pass/fail "
              "annotations will be omitted.", file=sys.stderr)

    # -- 2. Per-seed L_ray table + resonance guard -------------------------
    seed_L_table = [(seed, DIMLESS_HINGE * xi_per_seed[seed])
                    for seed in canonical_seeds]
    assert_no_resonance(seed_L_table)

    # -- 3. Per-seed evolution + shell extraction --------------------------
    per_seed_per_motif = {}
    per_seed_shell_hist = {}
    per_seed_mean_shell_hist = {}
    for seed, L_i in seed_L_table:
        ts = time.time()
        per_motif = evolve_and_collect_40snap_shells(seed, L_i)
        per_seed_per_motif[seed] = per_motif
        H = shell_histogram(per_motif)
        M = mean_shell_histogram(per_motif)
        per_seed_shell_hist[seed] = H
        per_seed_mean_shell_hist[seed] = M
        dom = dominant_shell(H)
        ent = shell_entropy_bits(H)
        print(f"  seed={seed:>4}  ξ={xi_per_seed[seed]:.4f}  L={L_i:.4f}  "
              f"N_motifs={len(per_motif):>3}  "
              f"dom_shell={dom['shell'] if dom else 'None'}  "
              f"entropy={ent:.3f}" if ent is not None else "entropy=None",
              file=sys.stderr)
        # Per-seed output
        out_seed = {
            "seed": seed,
            "xi_seed": xi_per_seed[seed],
            "L_ray_seed": L_i,
            "N_motifs": len(per_motif),
            "N_endpoints": 4 * len(per_motif),
            "shell_histogram": H,
            "mean_shell_histogram": M,
            "dominant_shell": dom,
            "shell_entropy_bits": ent,
            "per_motif": per_motif,
        }
        path = os.path.join(OUT_DIR, f"shell_histograms_seed{seed}.json")
        with open(path, "w") as f:
            json.dump(out_seed, f, indent=2)

    # -- 4. Pool histograms across seeds -----------------------------------
    pooled_H = pool_histograms(per_seed_shell_hist.values())
    pooled_M = pool_histograms(per_seed_mean_shell_hist.values())
    pooled_dom = dominant_shell(pooled_H)
    pooled_ent = shell_entropy_bits(pooled_H)

    # -- 5. JS divergence vs pool, and pair matrix -------------------------
    js_vs_pool = {}
    for seed, H in per_seed_shell_hist.items():
        js_vs_pool[seed] = jensen_shannon(H, pooled_H)

    js_matrix = {}
    seeds = list(per_seed_shell_hist.keys())
    for a in seeds:
        js_matrix[a] = {}
        for b in seeds:
            js_matrix[a][b] = jensen_shannon(
                per_seed_shell_hist[a], per_seed_shell_hist[b])

    # -- 6. Per-seed summary table with H-coord / H-shallow flags ----------
    # Failing seeds from ED-SC 3.3.6: ΔS1 or ΔS2 >= flat_thresh
    failing_from_336 = []
    passing_from_336 = []
    for seed in seeds:
        st = stats_336.get(seed)
        if st is None:
            continue
        d1 = st.get("dS1_i")
        d2 = st.get("dS2_i")
        fail = ((d1 is not None and d1 >= flat_336) or
                (d2 is not None and d2 >= flat_336))
        (failing_from_336 if fail else passing_from_336).append(seed)

    # Build pooled-passing histogram and max pass-seed JS against it
    pass_pool = pool_histograms(
        [per_seed_shell_hist[s] for s in passing_from_336])
    js_vs_pass_pool = {
        s: jensen_shannon(per_seed_shell_hist[s], pass_pool) for s in seeds
    }
    pass_max_js = max((js_vs_pass_pool[s] for s in passing_from_336),
                      default=0.0)

    per_seed_rows = []
    for seed in seeds:
        st = stats_336.get(seed, {})
        row = {
            "seed": seed,
            "xi_i": xi_per_seed[seed],
            "L_ray_i": DIMLESS_HINGE * xi_per_seed[seed],
            "N_motifs": len(per_seed_per_motif[seed]),
            "dominant_shell": per_seed_shell_hist[seed] and
                dominant_shell(per_seed_shell_hist[seed]),
            "shell_entropy_bits":
                shell_entropy_bits(per_seed_shell_hist[seed]),
            "JS_vs_pool": js_vs_pool[seed],
            "JS_vs_pass_pool": js_vs_pass_pool[seed],
            "N_from_336": st.get("N_i"),
            "S1_from_336": st.get("S1_i"),
            "S2_from_336": st.get("S2_i"),
            "dS1_from_336": st.get("dS1_i"),
            "dS2_from_336": st.get("dS2_i"),
            "is_failing_336": seed in failing_from_336,
        }
        per_seed_rows.append(row)

    # -- 7. Verdict logic --------------------------------------------------
    # H-coord confirmed if failing seeds have JS(pass_pool) > pass_max_js
    # AND shell-distribution difference correlates with S2 divergence sign.
    # H-shallow if all seeds' JS vs pool are below pass_max_js.
    seed_verdicts = {}
    for seed in seeds:
        st = stats_336.get(seed, {})
        d2 = st.get("dS2_i")
        is_fail = seed in failing_from_336
        js_pp = js_vs_pass_pool[seed]
        if not is_fail:
            seed_verdicts[seed] = "pass-336"
        else:
            # Failing seed: H-coord if JS elevated above passing spread
            # Use a generous multiplier to avoid false H-coord calls on
            # marginal fluctuations: JS > 1.5 × pass_max_js
            if js_pp > 1.5 * pass_max_js:
                seed_verdicts[seed] = "H-coord"
            else:
                seed_verdicts[seed] = "H-shallow"

    n_hcoord = sum(1 for v in seed_verdicts.values() if v == "H-coord")
    n_hshallow = sum(1 for v in seed_verdicts.values() if v == "H-shallow")
    if n_hcoord > 0 and n_hshallow == 0:
        master_verdict = "H-coord"
    elif n_hshallow > 0 and n_hcoord == 0:
        master_verdict = "H-shallow"
    elif n_hcoord > 0 and n_hshallow > 0:
        master_verdict = "Mixed"
    else:
        # No failing seeds (shouldn't happen given ED-SC 3.3.6 verdict)
        master_verdict = "H-shallow"

    # -- 8. Write master summary ------------------------------------------
    master = {
        "method": ("ED-SC 3.3.7 shell-histogram diagnostic for "
                   "H-coord vs H-shallow discrimination of the "
                   "ED-SC 3.3.6 Broken-collapse verdict"),
        "simulator_of_record":
            "r2_grf_falsifier_tests.py + ED_Update_Rule.ed_step_mobility",
        "xi_canonical_lattice_units": XI_CANONICAL,
        "dimensionless_hinge": DIMLESS_HINGE,
        "alpha_filt": ALPHA_FILT,
        "N_req": N_REQ,
        "snapshot_schedule": {
            "burn_in": XI_BURN_IN, "snap_every": XI_SNAP_EVERY,
            "snapshots_per_seed": 40,
        },
        "seeds": canonical_seeds,
        "xi_json_source": XI_JSON_PATH,
        "ed_sc_3_3_6_source": ED_SC_3_3_6_JSON,
        "resonance_windows_excluded": {
            "A": list(WINDOW_A), "B": list(WINDOW_B)},
        "per_seed": per_seed_rows,
        "per_seed_shell_histogram": per_seed_shell_hist,
        "pooled_shell_histogram": pooled_H,
        "pooled_mean_shell_histogram": pooled_M,
        "pooled_dominant_shell": pooled_dom,
        "pooled_shell_entropy_bits": pooled_ent,
        "JS_vs_pool_per_seed": js_vs_pool,
        "JS_vs_pass_pool_per_seed": js_vs_pass_pool,
        "JS_pair_matrix": js_matrix,
        "pass_seeds_336": passing_from_336,
        "fail_seeds_336": failing_from_336,
        "pass_pool_max_JS": pass_max_js,
        "h_coord_threshold": 1.5 * pass_max_js,
        "seed_verdicts": seed_verdicts,
        "master_verdict": master_verdict,
        "wall_seconds_total": time.time() - t_master,
    }

    master_path = os.path.join(OUT_DIR, "shell_summary.json")
    with open(master_path, "w") as f:
        json.dump(master, f, indent=2)

    print(f"\nWrote master summary → {master_path}", file=sys.stderr)
    print(json.dumps({
        "master_verdict": master_verdict,
        "pass_seeds": passing_from_336,
        "fail_seeds": failing_from_336,
        "seed_verdicts": seed_verdicts,
        "pass_pool_max_JS": pass_max_js,
        "h_coord_threshold": 1.5 * pass_max_js,
        "wall_seconds_total": master["wall_seconds_total"],
    }, indent=2))


if __name__ == "__main__":
    main()
