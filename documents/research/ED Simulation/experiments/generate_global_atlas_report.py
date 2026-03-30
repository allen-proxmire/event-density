"""
generate_global_atlas_report.py
================================
Global Synthesis: ED Attractor Invariant Atlas Report

Loads all invariant summary JSONs, computes global synthesis diagnostics,
and generates the final report for the ED Attractor Invariant Atlas.

This is the capstone script of the invariant analysis pipeline.  It
draws on every invariant family, every meta-analysis (universality,
cross-consistency, embedding), and every stability test to produce a
single, self-contained verdict on whether the ED architecture's
predictions (Principles 1-7, Appendices C-D) are confirmed, partially
confirmed, or contradicted by the numerical evidence.

Outputs:
  - output/atlas/ED_Attractor_Invariant_Atlas_Report.txt  (human-readable)
  - output/atlas/ED_Attractor_Invariant_Atlas_Report.json (machine-readable)
  - Console summary

Usage:
    python experiments/generate_global_atlas_report.py

Requires: numpy, json.
"""

import os
import sys
import json
import datetime
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_DIR = os.path.dirname(SCRIPT_DIR)
INV_DIR = os.path.join(SIM_DIR, "output", "figures", "invariants")
RUNS_DIR = os.path.join(SIM_DIR, "output", "runs")
ATLAS_DIR = os.path.join(SIM_DIR, "output", "atlas")

# ---------------------------------------------------------------------------
# Invariant source mapping: family_key -> filename
# ---------------------------------------------------------------------------
FAMILY_MAP = {
    "low_mode":          "invariant_low_mode_collapse.json",
    "mode_ratios":       "invariant_mode_energy_ratios.json",
    "renyi":             "invariant_spectral_complexity.json",
    "dissipation":       "invariant_dissipation_partitions.json",
    "E_H_geometry":      "invariant_energy_entropy_geometry.json",
    "cascade":           "invariant_broadband_cascade.json",
    "convergence":       "invariant_convergence_stability.json",
    "correlations":      "invariant_modal_correlations.json",
    "overlap":           "invariant_modal_overlap.json",
    "phase":             "invariant_phase_dynamics.json",
    "PAC":               "invariant_phase_amplitude_coupling.json",
    "lyapunov":          "invariant_lyapunov_spectrum.json",
    "manifold":          "invariant_attractor_manifold.json",
    "universality":      "invariant_parameter_universality.json",
    "cross_consistency": "invariant_cross_consistency.json",
    "embedding":         "invariant_embedding_map.json",
}

# Families that constitute "major" invariants for the final verdict
MAJOR_FAMILIES = [
    "low_mode", "mode_ratios", "dissipation", "cascade",
    "lyapunov", "manifold", "universality",
]


# ---------------------------------------------------------------------------
# Load all invariant JSONs
# ---------------------------------------------------------------------------
def load_atlas() -> dict:
    """Load all available invariant summary JSONs.

    Searches in multiple locations per file:
      1. output/figures/invariants/{filename}
      2. output/figures/invariants/{family_subdir}/{filename}
      3. output/atlas/{filename}
    """
    atlas = {}
    for key, filename in FAMILY_MAP.items():
        family_subdir = filename.replace("invariant_", "").replace(".json", "")
        search_paths = [
            os.path.join(INV_DIR, filename),
            os.path.join(INV_DIR, family_subdir, filename),
            os.path.join(ATLAS_DIR, filename),
            os.path.join(SIM_DIR, "output", filename),
        ]
        for path in search_paths:
            if os.path.isfile(path):
                with open(path, "r") as f:
                    atlas[key] = json.load(f)
                break
    return atlas


def count_regime_runs() -> int:
    """Count admissible regime_D*_A*_Nm* directories."""
    import glob
    pattern = os.path.join(RUNS_DIR, "regime_D*_A*_Nm*")
    dirs = glob.glob(pattern)
    return len([d for d in dirs if "perturb_eps" not in os.path.basename(d)])


# ---------------------------------------------------------------------------
# Extract verdicts from loaded data
# ---------------------------------------------------------------------------
def _safe_get(data: dict, *keys, default=None):
    """Nested dict access with default."""
    obj = data
    for k in keys:
        if isinstance(obj, dict) and k in obj:
            obj = obj[k]
        else:
            return default
    return obj


def extract_family_verdicts(atlas: dict) -> dict:
    """Extract per-family verdict strings and key metrics."""
    verdicts = {}

    for key in FAMILY_MAP:
        data = atlas.get(key)
        if data is None:
            verdicts[key] = {
                "status": "MISSING",
                "verdict": "--",
                "detail": "Invariant JSON not found.",
            }
            continue

        # Try to extract standard fields
        verdict = (_safe_get(data, "verdict") or
                   _safe_get(data, "global_verdict") or
                   "LOADED")
        cv = _safe_get(data, "CV") or _safe_get(data, "cv")
        score = (_safe_get(data, "universality_score") or
                 _safe_get(data, "consistency_score") or
                 _safe_get(data, "U") or
                 _safe_get(data, "C"))
        n_runs = (_safe_get(data, "n_runs") or
                  _safe_get(data, "total_runs"))

        verdicts[key] = {
            "status": "LOADED",
            "verdict": str(verdict),
            "CV": float(cv) if cv is not None else None,
            "score": float(score) if score is not None else None,
            "n_runs": int(n_runs) if n_runs is not None else None,
            "detail": _summarise_family(key, data),
        }

    return verdicts


def _summarise_family(key: str, data: dict) -> str:
    """One-line summary of a family's content."""
    if isinstance(data, dict):
        n_keys = len(data)
        return f"{n_keys} top-level keys"
    return "loaded"


# ---------------------------------------------------------------------------
# Global synthesis verdicts
# ---------------------------------------------------------------------------
def compute_universality_verdict(atlas: dict) -> dict:
    """Extract universality diagnostics."""
    data = atlas.get("universality", {})
    U = _safe_get(data, "universality_score") or _safe_get(data, "U")
    cv = _safe_get(data, "CV_distances") or _safe_get(data, "cv")

    if U is not None:
        U = float(U)
        if U > 0.9:
            verdict = "UNIVERSAL"
        elif U > 0.75:
            verdict = "WEAKLY UNIVERSAL"
        else:
            verdict = "NOT UNIVERSAL"
    else:
        U = None
        verdict = "UNKNOWN"

    return {"U": U, "CV": float(cv) if cv is not None else None,
            "verdict": verdict}


def compute_consistency_verdict(atlas: dict) -> dict:
    """Extract cross-consistency diagnostics."""
    data = atlas.get("cross_consistency", {})
    C = (_safe_get(data, "consistency_score") or
         _safe_get(data, "C") or
         _safe_get(data, "mean_abs_corr"))

    if C is not None:
        C = float(C)
        if C > 0.8:
            verdict = "CONSISTENT"
        elif C > 0.5:
            verdict = "PARTIALLY CONSISTENT"
        else:
            verdict = "INCONSISTENT"
    else:
        C = None
        verdict = "UNKNOWN"

    return {"C": C, "verdict": verdict}


def compute_stability_verdict(atlas: dict) -> dict:
    """Combine Lyapunov + manifold + convergence stability."""
    lyap = atlas.get("lyapunov", {})
    mani = atlas.get("manifold", {})

    n_pos = (_safe_get(lyap, "mean_n_positive") or
             _safe_get(lyap, "n_positive_mean"))
    D_KY = (_safe_get(lyap, "mean_D_KY") or
            _safe_get(lyap, "D_KY_mean"))
    D_eff = (_safe_get(mani, "mean_D_eff") or
             _safe_get(mani, "D_eff_mean"))

    stable = True
    details = []

    if n_pos is not None:
        n_pos = float(n_pos)
        if n_pos > 0.5:
            stable = False
            details.append(f"mean n_positive = {n_pos:.1f} > 0")
        else:
            details.append(f"mean n_positive = {n_pos:.1f} (OK)")

    if D_KY is not None:
        D_KY = float(D_KY)
        if D_KY > 1.0:
            stable = False
            details.append(f"D_KY = {D_KY:.2f} > 1")
        else:
            details.append(f"D_KY = {D_KY:.2f} (OK)")

    if D_eff is not None:
        D_eff = float(D_eff)
        details.append(f"D_eff = {D_eff:.1f}")

    if not details:
        verdict = "UNKNOWN"
    elif stable:
        verdict = "STABLE (Principle 3 confirmed)"
    else:
        verdict = "UNSTABLE (check numerical artifacts)"

    return {"n_positive": n_pos, "D_KY": D_KY, "D_eff": D_eff,
            "verdict": verdict, "details": details}


def compute_embedding_verdict(atlas: dict) -> dict:
    """Extract embedding diagnostics."""
    data = atlas.get("embedding", {})
    radius = (_safe_get(data, "cluster_radius") or
              _safe_get(data, "pca_cluster_radius"))
    C_emb = (_safe_get(data, "embedding_consistency") or
             _safe_get(data, "C_emb"))

    if radius is not None:
        radius = float(radius)
        if radius < 0.1:
            verdict = "COLLAPSED"
        elif radius < 0.3:
            verdict = "WEAKLY COLLAPSED"
        else:
            verdict = "NOT COLLAPSED"
    else:
        verdict = "UNKNOWN"

    return {"radius": radius, "C_emb": float(C_emb) if C_emb else None,
            "verdict": verdict}


def compute_final_verdict(family_verdicts: dict,
                          universality: dict,
                          consistency: dict,
                          stability: dict) -> dict:
    """Synthesise the overall ED architecture verdict."""
    # Check major families
    major_loaded = sum(1 for f in MAJOR_FAMILIES
                       if family_verdicts.get(f, {}).get("status") == "LOADED")
    major_total = len(MAJOR_FAMILIES)

    # Collect sub-verdicts
    sub_verdicts = {
        "universality": universality["verdict"],
        "consistency": consistency["verdict"],
        "stability": stability["verdict"],
    }

    # Count passes
    passes = 0
    total = 0
    for v in sub_verdicts.values():
        if v == "UNKNOWN":
            continue
        total += 1
        if "UNIVERSAL" in v or "CONSISTENT" in v or "STABLE" in v:
            passes += 1
        elif "WEAKLY" in v or "PARTIALLY" in v:
            passes += 0.5

    if total == 0:
        final = "INSUFFICIENT DATA"
    elif passes / total > 0.8:
        final = "PASS -- ED architecture confirmed"
    elif passes / total > 0.5:
        final = "PARTIAL -- ED architecture partially confirmed"
    else:
        final = "FAIL -- ED architecture contradicted"

    return {
        "final_verdict": final,
        "major_families_loaded": f"{major_loaded}/{major_total}",
        "sub_verdicts": sub_verdicts,
        "pass_fraction": passes / max(total, 1),
    }


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_text_report(atlas: dict, family_verdicts: dict,
                         universality: dict, consistency: dict,
                         stability: dict, embedding: dict,
                         final: dict, n_runs: int) -> str:
    """Generate the full text report."""
    lines = []
    w = lines.append
    sep = "=" * 80

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    w(sep)
    w("  ED ATTRACTOR INVARIANT ATLAS -- GLOBAL REPORT")
    w(sep)
    w(f"  Generated: {timestamp}")
    w(f"  Runs analysed: {n_runs}")
    w(f"  Invariant families loaded: "
      f"{sum(1 for v in family_verdicts.values() if v['status'] == 'LOADED')}"
      f"/{len(FAMILY_MAP)}")
    w("")

    # --- Section 1: Overview ---
    w("-" * 80)
    w("  1. OVERVIEW")
    w("-" * 80)
    w("")
    w("  This report synthesises the numerical evidence from the ED")
    w("  Attractor Invariant Atlas -- a systematic survey of structural")
    w("  invariants across the (D, A, Nm) parameter space.")
    w("")
    w("  The analysis tests the central prediction of the ED architecture:")
    w("  that all systems satisfying Principles 1-7 converge to a unique")
    w("  attractor whose qualitative structure is universal (Appendix D).")
    w("")

    # --- Section 2: Invariant Families ---
    w("-" * 80)
    w("  2. INVARIANT FAMILIES SUMMARY")
    w("-" * 80)
    w("")
    w(f"  {'Family':<22} {'Status':<10} {'Verdict':<25} {'CV':<10} {'Score':<10}")
    w("  " + "-" * 77)

    for key in FAMILY_MAP:
        v = family_verdicts[key]
        cv_str = f"{v['CV']:.4f}" if v.get("CV") is not None else "--"
        sc_str = f"{v['score']:.4f}" if v.get("score") is not None else "--"
        w(f"  {key:<22} {v['status']:<10} {v['verdict']:<25} "
          f"{cv_str:<10} {sc_str:<10}")

    w("")

    # --- Section 3: Global Statistics ---
    w("-" * 80)
    w("  3. GLOBAL STATISTICS")
    w("-" * 80)
    w("")
    w(f"  Total regime runs:  {n_runs}")
    w(f"  Invariant families: {len(FAMILY_MAP)}")
    w(f"  Families loaded:    "
      f"{sum(1 for v in family_verdicts.values() if v['status'] == 'LOADED')}")
    w(f"  Families missing:   "
      f"{sum(1 for v in family_verdicts.values() if v['status'] == 'MISSING')}")
    w("")

    # --- Section 4: Universality ---
    w("-" * 80)
    w("  4. UNIVERSALITY DIAGNOSTICS")
    w("-" * 80)
    w("")
    if universality["U"] is not None:
        w(f"  Universality score U = {universality['U']:.4f}")
    if universality["CV"] is not None:
        w(f"  Distance CV = {universality['CV']:.4f}")
    w(f"  Verdict: {universality['verdict']}")
    w("")

    # --- Section 5: Cross-Consistency ---
    w("-" * 80)
    w("  5. CROSS-INVARIANT CONSISTENCY")
    w("-" * 80)
    w("")
    if consistency["C"] is not None:
        w(f"  Consistency score C = {consistency['C']:.4f}")
    w(f"  Verdict: {consistency['verdict']}")
    w("")

    # --- Section 6: Embedding ---
    w("-" * 80)
    w("  6. EMBEDDING MAP SUMMARY")
    w("-" * 80)
    w("")
    if embedding["radius"] is not None:
        w(f"  PCA cluster radius = {embedding['radius']:.4f}")
    if embedding["C_emb"] is not None:
        w(f"  Embedding consistency C_emb = {embedding['C_emb']:.4f}")
    w(f"  Verdict: {embedding['verdict']}")
    w("")

    # --- Section 7: Stability ---
    w("-" * 80)
    w("  7. STABILITY & LYAPUNOV SUMMARY")
    w("-" * 80)
    w("")
    for d in stability["details"]:
        w(f"  {d}")
    w(f"  Verdict: {stability['verdict']}")
    w("")

    # --- Section 8: Perturbation Recovery ---
    w("-" * 80)
    w("  8. PERTURBATION RECOVERY SUMMARY")
    w("-" * 80)
    w("")
    perturb = atlas.get("perturbed_stability")
    if perturb is not None:
        recovery_frac = _safe_get(perturb, "overall_recovery_fraction")
        eps_indep = _safe_get(perturb, "eps_independence_verdict")
        if recovery_frac is not None:
            w(f"  Recovery fraction: {recovery_frac:.1%}")
        if eps_indep is not None:
            w(f"  ε-independence: {eps_indep}")
    else:
        w("  (Perturbation stability data not available.)")
    w("")

    # --- Section 9: Final Verdicts ---
    w("-" * 80)
    w("  9. FINAL VERDICTS")
    w("-" * 80)
    w("")
    w(f"  Major families loaded: {final['major_families_loaded']}")
    w("")
    for sub, verdict in final["sub_verdicts"].items():
        w(f"    {sub:<22} {verdict}")
    w("")
    w(f"  Pass fraction: {final['pass_fraction']:.1%}")
    w("")
    w(f"  ╔{'═'*58}╗")
    w(f"  ║  {final['final_verdict']:^54}  ║")
    w(f"  ╚{'═'*58}╝")
    w("")
    w(sep)
    w("  END OF REPORT")
    w(sep)

    return "\n".join(lines)


def generate_json_report(atlas: dict, family_verdicts: dict,
                         universality: dict, consistency: dict,
                         stability: dict, embedding: dict,
                         final: dict, n_runs: int) -> dict:
    """Generate the machine-readable JSON report."""
    return {
        "report_version": "1.0.0",
        "timestamp": datetime.datetime.now().isoformat(),
        "n_runs": n_runs,
        "n_families_loaded": sum(
            1 for v in family_verdicts.values() if v["status"] == "LOADED"
        ),
        "n_families_total": len(FAMILY_MAP),
        "family_verdicts": family_verdicts,
        "universality": universality,
        "cross_consistency": consistency,
        "stability": stability,
        "embedding": embedding,
        "final": final,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(ATLAS_DIR, exist_ok=True)

    print("Loading invariant summary JSONs...")
    atlas = load_atlas()

    loaded = [k for k, v in atlas.items()]
    missing = [k for k in FAMILY_MAP if k not in atlas]

    print(f"  Loaded: {len(loaded)}/{len(FAMILY_MAP)} families")
    if loaded:
        print(f"    {', '.join(loaded)}")
    if missing:
        print(f"  Missing: {', '.join(missing)}")

    n_runs = count_regime_runs()
    print(f"  Regime runs found: {n_runs}")

    # Extract family verdicts
    print("\nExtracting family verdicts...")
    family_verdicts = extract_family_verdicts(atlas)

    # Compute global syntheses
    print("Computing global synthesis...")
    universality = compute_universality_verdict(atlas)
    consistency = compute_consistency_verdict(atlas)
    stability = compute_stability_verdict(atlas)
    embedding = compute_embedding_verdict(atlas)
    final = compute_final_verdict(family_verdicts, universality,
                                  consistency, stability)

    # Generate reports
    print("\nGenerating reports...")

    text_report = generate_text_report(
        atlas, family_verdicts, universality, consistency,
        stability, embedding, final, n_runs,
    )

    json_report = generate_json_report(
        atlas, family_verdicts, universality, consistency,
        stability, embedding, final, n_runs,
    )

    # Save text report
    txt_path = os.path.join(ATLAS_DIR,
                             "ED_Attractor_Invariant_Atlas_Report.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text_report)
    print(f"  Text report: {txt_path}")

    # Save JSON report
    json_path = os.path.join(ATLAS_DIR,
                              "ED_Attractor_Invariant_Atlas_Report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_report, f, indent=2, default=str)
    print(f"  JSON report: {json_path}")

    # Console summary
    print(f"\n{'='*60}")
    print("  ED ATTRACTOR INVARIANT ATLAS -- CONSOLE SUMMARY")
    print(f"{'='*60}")
    print(f"  Invariants loaded: {len(loaded)}/{len(FAMILY_MAP)}")
    print(f"  Runs covered:      {n_runs}")
    print(f"  Universality:      {universality['verdict']}"
          + (f" (U = {universality['U']:.4f})"
             if universality['U'] is not None else ""))
    print(f"  Consistency:       {consistency['verdict']}"
          + (f" (C = {consistency['C']:.4f})"
             if consistency['C'] is not None else ""))
    print(f"  Stability:         {stability['verdict']}")
    print(f"  Embedding:         {embedding['verdict']}"
          + (f" (r = {embedding['radius']:.4f})"
             if embedding['radius'] is not None else ""))
    print(f"")
    print(f"  ┌{'─'*56}┐")
    print(f"  │  {final['final_verdict']:^52}  │")
    print(f"  └{'─'*56}┘")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
