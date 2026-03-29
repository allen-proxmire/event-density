"""
edsim.io.checkpoints — Save and load simulation checkpoints.

Checkpoints store the full solver state (rho, v, t, step count) plus
parameters, enabling restart from any saved point.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from ..core.parameters import EDParameters


def save_checkpoint(
    rho: np.ndarray,
    v: float,
    t: float,
    step: int,
    params: EDParameters,
    path: str | Path,
    integrator_state: Any = None,
) -> None:
    """Save a simulation checkpoint to disk.

    Parameters
    ----------
    rho : np.ndarray
        Current density field.
    v : float
        Current participation variable.
    t : float
        Current simulation time.
    step : int
        Current step number.
    params : EDParameters
        Simulation parameters.
    path : str or Path
        Output file path (NPZ format).
    integrator_state : Any, optional
        Serialisable integrator state (e.g., SpectralState arrays).
    """
    # TODO: np.savez with all state + params.to_dict()
    pass


def load_checkpoint(path: str | Path) -> dict:
    """Load a simulation checkpoint from disk.

    Parameters
    ----------
    path : str or Path
        Checkpoint file path.

    Returns
    -------
    dict
        ``{"rho": np.ndarray, "v": float, "t": float, "step": int,
           "params": EDParameters, "integrator_state": Any}``
    """
    # TODO: np.load, reconstruct EDParameters from stored dict
    pass
