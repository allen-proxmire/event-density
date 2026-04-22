# ED-Data-18: BIG-SPARC Activity Test

## Status: AWAITING DATA RELEASE

**BIG-SPARC has not been publicly released.** The Haubner, Lelli et al. (2024, arXiv:2411.13329) paper is a conference proceedings announcement. The catalog (~4000 galaxies with HI rotation curves, WISE photometry, and mass models) is not yet available for download.

When BIG-SPARC is released, run:
```bash
python data/ED-Data-18-BIG-SPARC/scripts/run_bigsparc_test.py
```

## What BIG-SPARC Will Provide

- ~4000 galaxies with Vflat, baryonic mass, and WISE W1/W2/W3 photometry
- WISE W3 (12 um) flux as a uniform SFR proxy for all galaxies
- Enough statistical power (n ~ 2000-4000) to detect rho ~ 0.1 at p < 0.001

This would be the definitive test of ED-Phys-05: at n = 3000 with rho = 0.3, the p-value would be < 10^-6.

## Current State of the Activity Test

> **Interpretation correction (2026-04-17):** ED-Data-12..17 computed the BTFR residual in M-space (Δ_M from an M-on-V fit). At fixed baryonic mass, Δ_M = −B · Δ_V (B ≈ 3.72), so a positive ρ(Δ_M, SFR) is algebraically equivalent to a *negative* ρ(Δ_V, SFR) — the opposite sign of what ED predicts from V-inflation at fixed M. The unified V-space analysis in [`papers/ED-BTFR-Activity/memo.md`](../../papers/ED-BTFR-Activity/memo.md) supersedes the individual-module verdicts below. The measurements in the table are correct as reported; only the interpretation relative to ED reverses.

| Module | Source | n | rho(SFR, Delta) | p | Tertile p |
|--------|--------|---|-----------------|---|-----------|
| ED-Data-12 | T-type | 122 | +0.039 | 0.667 | 0.982 |
| ED-Data-13 | Calibrated | 116 | +0.263 | **0.004** | **0.033** |
| ED-Data-14 | Literature | 51 | +0.247 | 0.081 | 0.514 |
| ED-Data-15 | GSWLC | 0 | N/A | INCOMPATIBLE | — |
| ED-Data-16 | z0MGS (20) | 20 | +0.356 | 0.124 | **0.041** |
| ED-Data-17 | z0MGS (25) | 25 | +0.324 | 0.114 | **0.030** |

**The signal is positive in every module** in the M-space convention used by these modules, which — via the Δ_M = −B · Δ_V identity — corresponds to a negative partial correlation in the V-space direction that ED actually predicts. On module 13's n = 116 sample the V-space mass-controlled partial Spearman is ρ ≈ −0.32 (p ≈ 0.0005), opposite to the ED prediction. BIG-SPARC, when released, will provide enough statistical power (n ~ 2000–4000) to resolve this at high significance.

## Honest Assessment

ED-Phys-05 is **not yet confirmed, not yet falsified**. The data are consistent with a weak positive correlation between star-formation activity and BTFR residuals. BIG-SPARC, when released, will settle this decisively.

## Data Source

- Haubner, K., Lelli, F., et al. 2024, arXiv:2411.13329 (announcement only)
- Expected release: TBD (check https://arxiv.org/abs/2411.13329 for updates)
