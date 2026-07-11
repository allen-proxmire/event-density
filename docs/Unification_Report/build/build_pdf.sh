#!/usr/bin/env bash
# Build the Unification Report PDF (staged; run after AP's review + finalization).
# Regenerates the assembled markdown, then pandoc -> xelatex -> PDF.
#
# Usage:  bash docs/Unification_Report/build/build_pdf.sh
# Requires: python, pandoc, a LaTeX engine with xelatex (TeX Live / MiKTeX).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
MD="$ROOT/ED_UnifiedFramework_ASSEMBLED.md"
PDF="$ROOT/ED_UnifiedFramework_Report.pdf"

echo "[1/3] regenerating assembled markdown..."
python "$HERE/assemble_report.py"

echo "[2/3] preparing a build copy (emoji + a few blackboard-bold -> safe markers)..."
# Unlike the corpus papers (authored in math mode), this report uses bare Unicode +
# backtick-code + scorecard emoji, so per PDF_Build_Protocol.md ("adjust if needed") we
# use installed Unicode fonts (Cambria/Consolas) instead of math-mode-ifying everything.
# The scorecard emoji (✅/📏/⚠️) are in NO text font, so map them to bracket markers
# (meaning preserved; see the "how to read" block in §2). Math symbols Cambria/Consolas
# lack (ℂ ℝ ℍ ℤ ℏ ∀ ∇ ∈ ∓ ∝ ⊗ ⟨ ⟩) are handled by build/report_header.tex (math mode),
# not by sed, so they keep proper typography.
BUILD_MD="$ROOT/.assembled_for_pdf.md"
sed -e 's/✅/[check]/g' -e 's/📏/[inherited]/g' -e 's/⚠️/[open]/g' -e 's/⚠/[open]/g' "$MD" > "$BUILD_MD"

echo "[3/3] pandoc -> PDF (xelatex, shared + report headers, installed Unicode fonts)..."
HDR="/c/Users/allen/GitHub/event-density/papers/_pandoc_header.tex"
RPTHDR="$HERE/report_header.tex"
pandoc "$BUILD_MD" -s -H "$HDR" -H "$RPTHDR" \
  -o "$PDF" \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V colorlinks=true -V linkcolor=blue -V urlcolor=blue \
  -V mainfont="Cambria" \
  -V monofont="Consolas" \
  --metadata title="Event Density: A Unified Framework for Physics" \
  --metadata author="Allen Proxmire" \
  --metadata date="2026"

rm -f "$BUILD_MD"
echo "done -> $PDF"

# NOTES / considerations:
#  - Fonts: Cambria (main) covers Greek (α γ λ Σ), arrows (→), operators (≈ ≥ ≤ ≠ √ ∝ ∂ ∇),
#    sub/superscripts (² ₀ ⁵ ⁻); Consolas (mono) covers the backtick-code Unicode. Emoji and
#    blackboard-bold (ℂ ℤ) are sed-mapped above (no text font has them). If a glyph still
#    renders as tofu, add it to the sed map or set a fallback.
#  - Math gotcha (house): a closing $ immediately before a digit breaks pandoc math. Pre-check
#    with: grep -o '\$[0-9]' "$MD"  (currently none).
#  - Wide tables (scorecard §2, appendices): if they overflow, check the first PDF and reduce
#    font or rotate. The shared header loads booktabs/array for cleaner tables.
