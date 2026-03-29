"""
edsim.manuscript.build — Assemble the ED-SIM-02 manuscript.

Generates all figures, collects section text, and writes a
complete Markdown manuscript file.
"""

from __future__ import annotations

from pathlib import Path

from .sections import (
    section_title,
    section_abstract,
    section_introduction,
    section_methods,
    section_results,
    section_reproducibility,
    section_conclusion,
    section_references,
)
from .figures import generate_all_figures


def build_manuscript(
    output_path: str = "manuscript/ED-SIM-02.md",
    fig_dir: str = "manuscript/figures",
) -> str:
    """Generate all figures and assemble the full manuscript.

    Steps:
    1. Generate all figures (saving PNGs to fig_dir).
    2. Collect all section Markdown strings.
    3. Insert figure paths into the results section.
    4. Concatenate into a single Markdown document.
    5. Write to output_path.

    Parameters
    ----------
    output_path : str
        Path for the output Markdown file.
    fig_dir : str
        Directory for generated figures.

    Returns
    -------
    str
        Path to the written manuscript file.
    """
    fig_dir_path = Path(fig_dir)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    # Step 1: Generate figures
    print("Generating figures...")
    figure_paths = generate_all_figures(fig_dir_path)
    print(f"  Generated {len(figure_paths)} figures in {fig_dir}")

    # Step 2-3: Collect sections with figure paths
    print("Assembling sections...")
    sections = [
        section_title(),
        section_abstract(),
        section_introduction(),
        section_methods(figure_paths),
        section_results(figure_paths),
        section_reproducibility(),
        section_conclusion(),
        section_references(),
    ]

    # Step 4: Concatenate
    manuscript = "\n".join(sections)

    # Step 5: Write
    output.write_text(manuscript, encoding="utf-8")
    print(f"Manuscript written to {output}")

    return str(output)


def main() -> None:
    """CLI entry point for manuscript generation."""
    path = build_manuscript()
    print(f"Done. Output: {path}")


if __name__ == "__main__":
    main()
