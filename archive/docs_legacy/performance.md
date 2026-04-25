# Performance

ED-SIM-02 provides optional accelerated backends for the core numerical
kernels. The default backend is NumPy; Numba and JAX can be enabled
when installed.

---

## Backends

| Backend | Accelerates | Requirements |
|---------|------------|--------------|
| `numpy` (default) | Nothing extra; pure NumPy/SciPy | None |
| `numba` | FD Laplacian, grad^2, F_local (2D/3D) | `pip install numba` |
| `jax` | ETD-RK4 spectral transforms (2D) | `pip install jax jaxlib` |

### Selecting a Backend

Set the `backend` field on `EDParameters`:

```python
params = EDParameters(
    d=2, N=(128, 128), L=(1.0, 1.0),
    method="implicit_euler",
    backend="numba",    # or "numpy" or "jax"
)
```

If the selected backend is not installed, the platform falls back to
NumPy silently. No code changes are needed.

---

## What Gets Accelerated

### Numba Backend

The Numba backend JIT-compiles the innermost FD stencil loops using
`@njit(parallel=True)`. The accelerated functions are:

- `laplacian_fd_2d`: 5-point stencil with inline Neumann BC handling
- `grad_squared_fd_2d`: central-difference gradient squared
- `operator_F_local_fd_2d`: fused Laplacian + gradient + constitutive
- `laplacian_fd_3d`: 7-point stencil

The fused `F_local` kernel avoids three separate array passes, reducing
memory traffic. Parallelisation over rows/slabs via `prange`.

First call incurs JIT compilation overhead (1-2 seconds). Subsequent
calls use the cached compiled version.

### JAX Backend

The JAX backend provides GPU-capable versions of:

- 2D DCT forward transform
- Spectral Laplacian multiplication
- ETD-RK4 time step

Currently a thin wrapper; full JIT compilation of the ETD-RK4 step
is planned for a future version.

---

## Expected Speedups

Typical speedups on a desktop CPU (measured via `benchmark_fd_operators`):

| Operation | NumPy | Numba | Speedup |
|-----------|-------|-------|---------|
| Laplacian 2D (128x128) | ~0.3 ms | ~0.05 ms | ~6x |
| Grad^2 2D (128x128) | ~0.4 ms | ~0.06 ms | ~7x |
| F_local 2D (128x128) | ~1.2 ms | ~0.15 ms | ~8x |
| Laplacian 3D (32^3) | ~1.5 ms | ~0.3 ms | ~5x |

Speedups increase with grid size. For the small grids used in the
default scenarios (N=32), the overhead of Numba JIT compilation
dominates and NumPy is often faster.

---

## Running Benchmarks

```python
from edsim.performance.benchmarks import run_all_benchmarks
run_all_benchmarks()
```

Or from the command line:

```python
python -c "from edsim.performance.benchmarks import run_all_benchmarks; run_all_benchmarks()"
```

---

## Limitations

1. **Numba compilation**: First call is slow (1-2s). Use `cache=True` to
   persist compiled code across sessions.

2. **JAX precision**: JAX defaults to float32 on GPU. ED-SIM-02 uses
   float64 throughout; ensure `jax.config.update("jax_enable_x64", True)`.

3. **Backend scope**: Only FD operators and ETD-RK4 are accelerated.
   Invariant computation remains NumPy.

4. **Correctness**: Numba and JAX results match NumPy to machine precision
   (< 1e-12 relative error). The test suite validates this.

---

## Reproducibility

Backend selection does not affect invariant outputs beyond floating-point
rounding (< 1e-12). The reproducibility pipeline produces identical
certificates for all backends. The `backend` field is recorded in
`params.to_dict()` so that the exact configuration is always traceable.
