# Event Density Research Program -- Makefile
# Requires: GNU Make + Bash (Git Bash on Windows)
# Usage: make <target>
#
# Targets:
#   all         Run the full reproducibility pipeline
#   validate    Run the 6 principle-verification tests (ED Validation)
#   simulate    Run the 64-point regime-volume experiment (ED Simulation)
#   invariants  Run all 23 invariant + meta-analysis scripts
#   figures     Generate all monograph figures
#   certificate Generate the ED Architecture Certificate
#   check       Run environment and data-integrity checks
#   clean       Remove generated outputs (PNGs, logs -- not run data)

SHELL  := /bin/bash
PYTHON ?= python
SIM    := ED Simulation
VAL    := ED Validation

.PHONY: all pipeline validate simulate invariants figures certificate check clean

# --- Full pipeline (runs all targets in sequence) ---
all: check simulate invariants figures certificate

# --- Python-orchestrated pipeline (alternative to make all) ---
pipeline:
	cd "$(SIM)/reproducibility" && $(PYTHON) run_all.py

# --- Validation (principle tests) ---
validate:
	cd "$(VAL)/P1_modal_funnel"          && $(PYTHON) test_modal_funnel.py
	cd "$(VAL)/P2_DH_complementarity"    && $(PYTHON) test_DH_complementarity.py
	cd "$(VAL)/P3_manifold_collapse"     && $(PYTHON) test_manifold_collapse.py
	cd "$(VAL)/P4_horizon_formation"     && $(PYTHON) test_horizon_formation.py
	cd "$(VAL)/P6_discriminant_boundary" && $(PYTHON) test_discriminant_boundary.py
	cd "$(VAL)/P7_triad_ratio"           && $(PYTHON) test_triad_ratio.py

# --- Simulation (regime volume) ---
simulate:
	cd "$(SIM)" && $(PYTHON) experiments/regime_volume_3d.py

# --- Invariant extraction ---
invariants:
	cd "$(SIM)" && for f in experiments/invariant_*.py; do echo "Running $$f..." && $(PYTHON) "$$f"; done

# --- Figure generation ---
figures:
	cd "$(SIM)" && $(PYTHON) analysis/generate_all_figures.py

# --- Certificate ---
certificate:
	cd "$(SIM)" && $(PYTHON) generate_certificate_figure.py --verdict PASS

# --- Environment checks ---
check:
	cd "$(SIM)/reproducibility/checks" && $(PYTHON) check_environment.py
	cd "$(SIM)/reproducibility/checks" && $(PYTHON) check_data_integrity.py

# --- Clean generated outputs (preserves run data) ---
clean:
	-rm -f "$(SIM)"/output/figures/*.png
	-rm -rf "$(SIM)"/output/figures/*/
	-rm -f "$(SIM)"/output/logs/*
	-rm -f "$(SIM)"/output/atlas/*.png
	-rm -f "$(SIM)"/output/atlas/*.pdf
