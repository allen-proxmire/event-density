# Contributing to Event Density

Thank you for your interest in the ED research program.

## Getting Started

1. Read the [onboarding guide](ED%20Simulation/reproducibility/docs/onboarding.md)
   for how to run the pipeline and how to extend it.
2. Read the [architecture overview](ED%20Simulation/reproducibility/docs/architecture.md)
   for the system structure and design principles.
3. See the [invariant map](ED%20Simulation/reproducibility/docs/invariant_map.md)
   for a one-page reference of all invariant families.

## Contributor Workflow

1. Create a branch from `main` with a descriptive name.
2. Make your changes (new invariant, experiment, figure, or documentation).
3. Run a quick validation test to check nothing is broken:
   `cd "ED Validation/P1_modal_funnel" && python test_modal_funnel.py`
4. If you modified invariants or the solver, run the minimal scenario:
   `cd "ED Simulation/reproducibility/scenarios/minimal" && python run.py`
5. Open a pull request describing what you changed and why.

## Notes

- The full pipeline takes approximately 2-4 hours on a single core:
  `cd "ED Simulation" && python reproducibility/run_all.py`
  Run it before submitting if your changes affect simulation outputs or
  invariant computations.
- There are no unit tests yet. The validation tests in `ED Validation/`
  and the reproducibility scenarios are the primary verification methods.
- No formal coding style is enforced. Follow the patterns of existing
  scripts (see `ED Simulation/experiments/invariant_spectral_entropy.py`
  as the canonical example).
