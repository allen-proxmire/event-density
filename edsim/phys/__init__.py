"""
edsim.phys — Physics experiment layer for Event Density.

Sub-modules
-----------
ED-PHYS-01: diffusion/heat-equation limit
ED-PHYS-02: wave/telegraph limit
ED-PHYS-03: reaction/source limit
ED-PHYS-04: nonlinear pattern formation
"""

from .diffusion_regime import DiffusionRegime, build_diffusion_regime
from .experiments_diffusion import run_gaussian_spread, run_step_relaxation
from .analysis_diffusion import (
    fit_effective_diffusion_coefficient, compare_to_heat_equation,
    DiffusionComparisonResult, run_full_diffusion_study,
)
from .wave_regime import WaveRegime, build_wave_regime
from .experiments_wave import (
    run_uniform_oscillation, run_sine_wave_decay, run_wave_packet,
)
from .analysis_wave import (
    extract_oscillation_params, extract_decay_rate,
    build_dispersion_table, compare_to_telegraph_model,
    run_full_wave_study, WaveStudyResult,
)
from .reaction_regime import ReactionRegime, build_reaction_regime
from .experiments_reaction import (
    run_uniform_decay, run_uniform_growth, run_localised_source,
)
from .analysis_reaction import (
    fit_reaction_rate, compare_to_reaction_model,
    analyse_source_competition, run_full_reaction_study, ReactionStudyResult,
)
from .pattern_regime import PatternRegime, build_pattern_regime
from .experiments_pattern import (
    run_noise_instability, run_filament_instability, run_spot_evolution,
)
from .analysis_pattern import (
    extract_growth_rates, classify_pattern_state,
    measure_transient_complexity, run_full_pattern_study, PatternStudyResult,
)
from .quantum_regime import QuantumRegime, build_quantum_regime
from .experiments_quantum import (
    run_anomalous_spread, run_double_bump_interference, run_oscillatory_envelope,
)
from .analysis_quantum import (
    fit_variance_scaling, detect_interference_features, analyse_envelope,
    run_full_quantum_study, QuantumStudyResult,
)
from .phase_diagram import (
    PhasePoint, PhaseMetrics, PhaseDiagram,
    build_phase_grid, compute_phase_metrics, classify_phase, build_phase_diagram,
)
from .experiments_phase import run_phase_validation, validate_phase_diagram
from .analysis_phase import run_full_phase_study, PhaseStudyResult
from .energy_regime import (
    EnergyRegime, build_energy_regime,
    lyapunov_energy, gradient_energy, penalty_energy,
    participation_energy, boltzmann_entropy, fisher_information, free_energy,
)
from .experiments_energy import (
    run_energy_monotonicity, run_entropy_test, run_gradient_flow_test,
    EnergyTrajectory, GradientFlowTest,
)
from .analysis_energy import (
    check_monotonicity, run_full_energy_study, EnergyStudyResult,
)
from .interpretation_matrix import (
    PhysicalDomain, InterpretationMatrix, build_interpretation_matrix, ED_PROPERTIES,
)
from .analysis_interpretation import (
    identify_plausible_domains, run_full_interpretation_study, InterpretationStudyResult,
)
from .cosmology_regime import CosmologyRegime, build_cosmology_regime
from .experiments_cosmology import (
    run_expansion_analogue, run_horizon_analogue, run_structure_analogue,
)
from .analysis_cosmology import run_full_cosmology_study, CosmologyStudyResult
from .master_interpretation import (
    MasterInterpretation, build_master_interpretation, build_master_report,
)
