"""
edsim.roadmap -- ED-SIM-03 roadmap and forward planning.

Defines the next-generation architecture, research questions,
dependency graph, milestone plan, manuscript outline, and
roadmap document generator.

Submodules
----------
architecture
    ED-SIM-03 component definitions and motivations.
questions
    Open research questions grouped by theme.
dependencies
    Directed acyclic graph of component and question dependencies.
milestones
    Five-phase development plan with tasks and acceptance criteria.
manuscript
    Structured outline for the ED-SIM-03 paper.
generator
    Roadmap document assembly and export.
"""

from .architecture import (
    Component,
    EDSIM3Architecture,
    build_edsim3_architecture,
)
from .questions import (
    Theme,
    ResearchQuestion,
    list_research_questions,
    questions_by_theme,
)
from .dependencies import (
    Node,
    DependencyGraph,
    build_dependency_graph,
)
from .milestones import (
    Task,
    Milestone,
    MilestonePlan,
    build_milestone_plan,
)
from .manuscript import (
    Section,
    ManuscriptOutline,
    build_edsim3_manuscript_outline,
)
from .generator import generate_roadmap

__all__ = [
    # Architecture
    "Component", "EDSIM3Architecture", "build_edsim3_architecture",
    # Questions
    "Theme", "ResearchQuestion", "list_research_questions", "questions_by_theme",
    # Dependencies
    "Node", "DependencyGraph", "build_dependency_graph",
    # Milestones
    "Task", "Milestone", "MilestonePlan", "build_milestone_plan",
    # Manuscript
    "Section", "ManuscriptOutline", "build_edsim3_manuscript_outline",
    # Generator
    "generate_roadmap",
]
