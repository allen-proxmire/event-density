"""Tests for serialization roundtrips."""

import tempfile
from pathlib import Path

import numpy as np
import pytest

from edsim.core.parameters import EDParameters


class TestParametersRoundtrip:
    def test_to_dict_from_dict(self):
        p = EDParameters(d=2, N=(16, 16), L=(1.0, 1.0), D=0.4, seed=99)
        d = p.to_dict()
        p2 = EDParameters.from_dict(d)
        assert p2.d == p.d
        assert p2.N == p.N
        assert p2.D == p.D
        assert p2.seed == p.seed

    def test_all_fields_preserved(self):
        p = EDParameters(d=3, N=(8, 8, 8), L=(2.0, 2.0, 2.0),
                         D=0.5, H=0.2, beta=3.0, P0=0.5, dt=1e-3, T=2.0)
        d = p.to_dict()
        p2 = EDParameters.from_dict(d)
        for key in d:
            v1 = getattr(p, key)
            v2 = getattr(p2, key)
            if isinstance(v1, float):
                assert abs(v1 - v2) < 1e-15, f"Mismatch on {key}"
            else:
                assert v1 == v2, f"Mismatch on {key}"

    def test_dict_is_json_compatible(self):
        import json
        p = EDParameters(d=2, N=(8, 8), L=(1.0, 1.0))
        d = p.to_dict()
        s = json.dumps(d)
        d2 = json.loads(s)
        p2 = EDParameters.from_dict(d2)
        assert p2.d == p.d


class TestTimeSeries:
    def test_atlas_fields_match_times(self):
        """Run a short simulation and verify all atlas lists have same length."""
        from edsim.experiments.runner import RunConfig, run_simulation
        params = EDParameters(d=2, N=(8, 8), L=(1.0, 1.0),
                              dt=5e-4, T=0.005, k_out=5,
                              method="implicit_euler", bc="neumann")
        config = RunConfig(params=params, ic_type="cosine",
                           ic_kwargs={"A": 0.03, "Nm": 2})
        ts = run_simulation(config)
        n = len(ts.times)
        assert n > 1
        assert len(ts.fields) == n
        assert len(ts.v_history) == n
        assert len(ts.energy) == n
        assert len(ts.complexity) == n
        assert len(ts.mass) == n
        assert len(ts.spectral_entropy) == n
        assert len(ts.modal_hierarchy) == n
        assert len(ts.morphology_fractions) == n
        assert len(ts.R_grad) == n
        assert len(ts.R_pen) == n
        assert len(ts.R_part) == n
        assert len(ts.correlation_length) == n
        assert len(ts.structure_r) == n
        assert len(ts.structure_S2) == n
        assert len(ts.euler_characteristic) == n
        assert len(ts.betti_numbers) == n
