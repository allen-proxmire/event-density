"""
edsim.performance.benchmarks — Benchmark suite for ED-SIM-02 backends.

Compares NumPy, Numba, and JAX performance for FD operators, implicit
Euler, and ETD-RK4. Prints a formatted table of timings.
"""

from __future__ import annotations

import time

import numpy as np

from ..core.parameters import EDParameters
from ..core.operators import (
    laplacian_fd_2d, grad_squared_fd_2d, operator_F_local_fd_2d,
    laplacian_fd_3d,
)
from .numba_backend import (
    NUMBA_AVAILABLE,
    laplacian_fd_2d_numba, grad_squared_fd_2d_numba,
    laplacian_fd_3d_numba, operator_F_local_fd_2d_numba,
)
from .jax_backend import JAX_AVAILABLE


def _time_fn(fn, *args, n_repeats: int = 10, n_warmup: int = 2) -> float:
    """Time a function call, returning median wall time in milliseconds."""
    # Warmup
    for _ in range(n_warmup):
        fn(*args)

    times = []
    for _ in range(n_repeats):
        t0 = time.perf_counter()
        fn(*args)
        times.append((time.perf_counter() - t0) * 1000)

    return float(np.median(times))


def benchmark_fd_operators(N_2d: int = 128, N_3d: int = 32) -> list[dict]:
    """Benchmark FD Laplacian and grad^2 for NumPy vs Numba.

    Parameters
    ----------
    N_2d : int
        Grid size for 2D benchmarks.
    N_3d : int
        Grid size for 3D benchmarks.

    Returns
    -------
    list[dict]
        Timing results.
    """
    results = []

    # 2D Laplacian
    p2 = EDParameters(d=2, N=(N_2d, N_2d), L=(1.0, 1.0))
    rho2 = np.random.default_rng(0).random(p2.N) * 0.5 + 0.25

    t_np = _time_fn(laplacian_fd_2d, rho2, p2.dx)
    results.append({"op": f"Laplacian 2D ({N_2d}x{N_2d})", "numpy_ms": t_np})

    if NUMBA_AVAILABLE:
        t_nb = _time_fn(laplacian_fd_2d_numba, rho2, p2.dx)
        results[-1]["numba_ms"] = t_nb
        results[-1]["speedup"] = t_np / t_nb if t_nb > 0 else 0

    # 2D grad^2
    t_np = _time_fn(grad_squared_fd_2d, rho2, p2.dx)
    results.append({"op": f"Grad^2 2D ({N_2d}x{N_2d})", "numpy_ms": t_np})

    if NUMBA_AVAILABLE:
        t_nb = _time_fn(grad_squared_fd_2d_numba, rho2, p2.dx)
        results[-1]["numba_ms"] = t_nb
        results[-1]["speedup"] = t_np / t_nb if t_nb > 0 else 0

    # 2D F_local
    t_np = _time_fn(operator_F_local_fd_2d, rho2, p2)
    results.append({"op": f"F_local 2D ({N_2d}x{N_2d})", "numpy_ms": t_np})

    if NUMBA_AVAILABLE:
        t_nb = _time_fn(operator_F_local_fd_2d_numba, rho2, p2)
        results[-1]["numba_ms"] = t_nb
        results[-1]["speedup"] = t_np / t_nb if t_nb > 0 else 0

    # 3D Laplacian
    p3 = EDParameters(d=3, N=(N_3d, N_3d, N_3d), L=(1.0, 1.0, 1.0))
    rho3 = np.random.default_rng(0).random(p3.N) * 0.5 + 0.25

    t_np = _time_fn(laplacian_fd_3d, rho3, p3.dx)
    results.append({"op": f"Laplacian 3D ({N_3d}^3)", "numpy_ms": t_np})

    if NUMBA_AVAILABLE:
        t_nb = _time_fn(laplacian_fd_3d_numba, rho3, p3.dx)
        results[-1]["numba_ms"] = t_nb
        results[-1]["speedup"] = t_np / t_nb if t_nb > 0 else 0

    return results


def benchmark_implicit_euler(N: int = 64, n_steps: int = 10) -> list[dict]:
    """Benchmark implicit Euler for NumPy vs Numba backend.

    Parameters
    ----------
    N : int
        Grid size per axis.
    n_steps : int
        Number of time steps.

    Returns
    -------
    list[dict]
        Timing results.
    """
    from ..experiments.runner import RunConfig, run_simulation

    results = []

    # NumPy backend
    p_np = EDParameters(
        d=2, N=(N, N), L=(1.0, 1.0),
        D=0.3, dt=1e-4, T=n_steps * 1e-4, k_out=n_steps + 1,
        method="implicit_euler", backend="numpy",
    )
    config_np = RunConfig(params=p_np, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})
    t_np = _time_fn(run_simulation, config_np, n_repeats=3, n_warmup=1)
    results.append({
        "op": f"IE {n_steps} steps ({N}x{N})",
        "numpy_ms": t_np,
    })

    # Numba backend (operators are accelerated; integrator loop stays Python)
    if NUMBA_AVAILABLE:
        p_nb = EDParameters(
            d=2, N=(N, N), L=(1.0, 1.0),
            D=0.3, dt=1e-4, T=n_steps * 1e-4, k_out=n_steps + 1,
            method="implicit_euler", backend="numba",
        )
        config_nb = RunConfig(params=p_nb, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})
        t_nb = _time_fn(run_simulation, config_nb, n_repeats=3, n_warmup=1)
        results[-1]["numba_ms"] = t_nb
        results[-1]["speedup"] = t_np / t_nb if t_nb > 0 else 0

    return results


def benchmark_etdrk4(N: int = 64, n_steps: int = 10) -> list[dict]:
    """Benchmark ETD-RK4 for NumPy vs JAX.

    Parameters
    ----------
    N : int
        Grid size per axis.
    n_steps : int
        Number of time steps.

    Returns
    -------
    list[dict]
        Timing results.
    """
    from ..experiments.runner import RunConfig, run_simulation

    results = []

    p_np = EDParameters(
        d=2, N=(N, N), L=(1.0, 1.0),
        D=0.3, dt=1e-4, T=n_steps * 1e-4, k_out=n_steps + 1,
        method="etdrk4", backend="numpy",
    )
    config_np = RunConfig(params=p_np, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})
    t_np = _time_fn(run_simulation, config_np, n_repeats=3, n_warmup=1)
    results.append({
        "op": f"ETD-RK4 {n_steps} steps ({N}x{N})",
        "numpy_ms": t_np,
    })

    if JAX_AVAILABLE:
        p_jax = EDParameters(
            d=2, N=(N, N), L=(1.0, 1.0),
            D=0.3, dt=1e-4, T=n_steps * 1e-4, k_out=n_steps + 1,
            method="etdrk4", backend="jax",
        )
        config_jax = RunConfig(params=p_jax, ic_type="cosine", ic_kwargs={"A": 0.03, "Nm": 2})
        t_jax = _time_fn(run_simulation, config_jax, n_repeats=3, n_warmup=1)
        results[-1]["jax_ms"] = t_jax
        results[-1]["speedup"] = t_np / t_jax if t_jax > 0 else 0

    return results


def run_all_benchmarks(
    N_2d: int = 128,
    N_3d: int = 32,
    ie_N: int = 64,
    ie_steps: int = 10,
    etd_N: int = 64,
    etd_steps: int = 10,
) -> None:
    """Run all benchmarks and print a formatted table.

    Parameters
    ----------
    N_2d, N_3d : int
        Grid sizes for operator benchmarks.
    ie_N, ie_steps : int
        Grid size and steps for implicit Euler benchmark.
    etd_N, etd_steps : int
        Grid size and steps for ETD-RK4 benchmark.
    """
    print("=" * 72)
    print("  ED-SIM-02 Performance Benchmarks")
    print("=" * 72)
    print(f"  Numba available: {NUMBA_AVAILABLE}")
    print(f"  JAX available:   {JAX_AVAILABLE}")
    print()

    all_results = []
    all_results.extend(benchmark_fd_operators(N_2d, N_3d))
    all_results.extend(benchmark_implicit_euler(ie_N, ie_steps))
    all_results.extend(benchmark_etdrk4(etd_N, etd_steps))

    # Print table
    has_numba = any("numba_ms" in r for r in all_results)
    has_jax = any("jax_ms" in r for r in all_results)

    header = f"{'Operation':>35s}  {'NumPy (ms)':>10s}"
    if has_numba:
        header += f"  {'Numba (ms)':>10s}  {'Speedup':>8s}"
    if has_jax:
        header += f"  {'JAX (ms)':>10s}  {'Speedup':>8s}"
    print(header)
    print("-" * len(header))

    for r in all_results:
        line = f"{r['op']:>35s}  {r['numpy_ms']:10.2f}"
        if has_numba:
            nb = r.get("numba_ms")
            sp = r.get("speedup")
            if nb is not None:
                line += f"  {nb:10.2f}  {sp:7.1f}x"
            else:
                line += f"  {'n/a':>10s}  {'':>8s}"
        if has_jax:
            jx = r.get("jax_ms")
            sp = r.get("speedup") if "jax_ms" in r else None
            if jx is not None:
                line += f"  {jx:10.2f}  {sp:7.1f}x"
            else:
                line += f"  {'n/a':>10s}  {'':>8s}"
        print(line)

    print()
