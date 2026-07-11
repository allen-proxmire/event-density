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

echo "[2/3] preparing a build copy (emoji -> text markers so xelatex won't choke)..."
# The scorecard uses ✅/📏/⚠️; most xelatex main fonts lack emoji glyphs.
# Map them to bracketed text markers for the PDF (meaning preserved; see the "how to read" block in §2).
BUILD_MD="$ROOT/.assembled_for_pdf.md"
sed -e 's/✅/[OK]/g' -e 's/📏/[inherited]/g' -e 's/⚠️/[open]/g' -e 's/⚠/[open]/g' "$MD" > "$BUILD_MD"

echo "[3/3] pandoc -> PDF (xelatex)..."
pandoc "$BUILD_MD" \
  -o "$PDF" \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V linkcolor=blue -V urlcolor=blue \
  -V mainfont="DejaVu Serif" \
  -V mathfont="DejaVu Serif" \
  --metadata title="Event Density: A Unified Framework for Physics" \
  --metadata author="Allen Proxmire" \
  --metadata date="2026"

rm -f "$BUILD_MD"
echo "done -> $PDF"

# NOTES / known considerations to resolve on first real build:
#  - Fonts: DejaVu covers Greek (α γ λ), arrows (→), ℂ/ℤ, and many symbols. If a glyph
#    still renders as tofu, either swap mainfont to one with wider coverage or add a
#    fallback via a small header-includes LaTeX block (\usepackage{newunicodechar}).
#  - Math: this report uses backtick `inline code` for most symbols and only light $...$
#    display math. Watch the house gotcha: a closing $ immediately before a digit can
#    break pandoc math parsing (workflow_paper_pdf_build). Grep the assembled md for '\$[0-9]'
#    before building if pandoc errors.
#  - Wide tables (scorecard §2, appendices): if they overflow the text block, add
#    `| : longtable / smaller font` handling or rotate; check the first PDF.
