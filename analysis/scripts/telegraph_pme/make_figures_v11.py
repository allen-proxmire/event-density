"""Generate v1.1 (nonlinear-attempt) figures from the wide-bump run."""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from make_figures import (load, compute_psd, fig_field_snapshots,
                           fig_time_series, fig_psd, fig_harmonic, fig_summary)


if __name__ == "__main__":
    here = Path(__file__).parent
    outdir = here / "v1.1_nonlinear_regime"
    data = load(outdir / "analogue5_H50_nonlinear_wide.npz")

    fig_field_snapshots(data, outdir / "field_snapshots.png")
    fig_time_series(data, outdir / "time_series.png")
    psd_info = fig_psd(data, outdir / "psd.png")
    harmonic_ratio = fig_harmonic(data, outdir / "harmonic.png",
                                    fpeak_v=psd_info["fpeak_v"])
    fig_summary(data, outdir / "summary.png", psd_info, harmonic_ratio)
    print("\nv1.1 figures written.")
