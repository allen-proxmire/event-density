# Contributing to Event Density

Thank you for your interest in the Event Density framework.

## Scope

ED is a scientific research project. Contributions are welcome in the following areas:

- **Bug fixes** in the ED-SIM-02 solver or invariant engine.
- **New structural analogues** that test the ED channels against known physical laws.
- **New invariants** or diagnostics for the invariant atlas.
- **Documentation improvements** (clarity, examples, corrections).
- **Performance improvements** (Numba/JAX backends, algorithmic optimisations).
- **Higher-dimensional extensions** (3D/4D analogues).

## What Not to Contribute

- Do not modify the canonical PDE or constitutive functions without discussion.
- Do not add new physics channels (e.g., stochastic forcing, multi-field coupling) to the core solver. These belong in ED-SIM-03.
- Do not add cosmological, quantum, or gravitational claims. ED is a structural framework; physical interpretations must be clearly labelled as analogues.

## Process

1. **Open an issue** describing the proposed change.
2. **Fork the repository** and create a feature branch.
3. **Write tests** for any new functionality.
4. **Run the full test suite:** `pytest edsim/tests/ -v` (112 tests must pass).
5. **Run the reproducibility pipeline:** `python -m edsim certify` (9/9 phases must pass).
6. **Submit a pull request** with a clear description.

## Code Style

- Python 3.10+.
- Type hints for all public functions.
- Docstrings for all public modules, classes, and functions.
- NumPy-style docstrings preferred.
- No external dependencies beyond NumPy, SciPy, and Matplotlib.

## Scientific Standards

- Every analogue must have an explicit falsification condition.
- Every numerical claim must be reproducible from the code.
- Negative results are valuable and should be reported honestly.
- Structural analogies must be clearly distinguished from physical derivations.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
