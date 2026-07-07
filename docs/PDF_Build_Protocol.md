# ED Paper Build Protocol — .md to .tex and .pdf

Self-contained protocol for generating the `.tex` and `.pdf` of an Event Density paper from its Markdown source, matching how the existing corpus renders (e.g. `Paper_Continuum_KineticLatticeGas`, the MS and KM papers). Hand this to any session; it needs nothing else.

## Environment

- Windows. Use the **Bash tool** (Git Bash), not Windows Python, for the temp-file step (see Gotcha 1).
- Installed and on PATH: **pandoc 3.9**, **MiKTeX xelatex**. Verify with `pandoc --version` and `xelatex --version` if unsure.
- Shared header: `C:/Users/allen/GitHub/event-density/papers/_pandoc_header.tex` (loads mathtools, enumitem, microtype, booktabs, array). Confirm it exists before building.

## Layout convention (where files go)

- The `.md` and `.pdf` sit in the EDG repo next to their siblings (e.g. `physics-papers/<arc>/`).
- The `.tex` goes to `C:\Users\allen\Desktop\ED Important\ED_tex_files\`.
- PDFs intended for Zenodo go to `C:\Users\allen\Desktop\ED_pdf_files\`.

## The command (run from the paper's folder, Bash tool)

```bash
HDR="C:/Users/allen/GitHub/event-density/papers/_pandoc_header.tex"
TITLE="<the paper title>"
TEXDIR="/c/Users/allen/Desktop/ED Important/ED_tex_files"

# Strip the leading title/author/date block so pandoc metadata drives a centered \maketitle.
# tail -n +7 assumes: line1 "# Title", 2 blank, 3 "**Allen Proxmire**", 4 blank,
# 5 "**<Month Year>**", 6 blank, 7 "**Series:**...". Adjust the cut if the block differs.
tail -n +7 "Paper_X.md" > body_tmp.md

pandoc body_tmp.md -s -H "$HDR" --pdf-engine=xelatex \
  -V geometry:margin=1in -V title="$TITLE" -V author="Allen Proxmire" -V date="<Month Year>" \
  -o "Paper_X.pdf"

pandoc body_tmp.md -s -H "$HDR" \
  -V geometry:margin=1in -V title="$TITLE" -V author="Allen Proxmire" -V date="<Month Year>" \
  -o "$TEXDIR/Paper_X.tex"

rm -f body_tmp.md
```

Note: the recipe writes the temp into the current folder (`body_tmp.md`) rather than `/tmp`, which sidesteps Gotcha 1 entirely. If you prefer `/tmp`, create it with a Bash tool, never with Windows Python.

## Gotcha 1 — the /tmp path mismatch (wasted ~30 min once)

Do NOT create the stripped temp with **Windows Python** `open('/tmp/body.md')`. Windows Python resolves `/tmp` to `C:\tmp`, but `pandoc.exe` resolves `/tmp` to `C:\Users\allen\AppData\Local\Temp`, so pandoc reports the file "does not exist." Make the temp with a **Bash tool** (`tail`/`sed`), so both agree on the path, or write it into the cwd with a relative name as above.

## Gotcha 2 — the real one: author every symbol in MATH MODE

The xelatex build **blanks bare Unicode symbols** (ρ Σ ℓ ∫ ∝ ∼ ≈ ≥ ∇ √ ² ₀ → ∂ …) because the Latin Modern *text* font does not contain them. The entire corpus renders correctly because it was **written in math mode**: the `.md` sources use `$\rho$`, `$\ell_P$`, `$\int dx$`, `$\sim$`, `$R_0$`, `$\nabla$`, `$\partial_t$`, and so on. GitHub also renders `$...$`, so the Markdown stays readable there.

**The magic words, and it is all it takes:** write every symbol as LaTeX math in the `.md` from the start. Not bare `ρ ℓ ∫ ∼ R₀ α₁ ∂_t`, but `$\rho$`, `$\ell_P$`, `$\int dx$`, `$\sim$`, `$R_0$`, `$\alpha_1$`, `$\partial_t$`. Then the plain build above renders everything with zero tricks. Do NOT force a minimal font, fight `newunicodechar`, or add sed/sentinel wraps as the default; those are the "weird PDF routes" to avoid. Just author in math mode like the rest of the corpus.

## Verify every build

1. `grep -c 'missing character' Paper_X.log` (or scan the pandoc/xelatex stderr) must be **0**.
2. Eyeball a math-heavy page: `pdftoppm -f N -l N -r 140 -png Paper_X.pdf <scratchpad>/pg` then Read the PNG. Write the PNG to the session scratchpad directory, NOT `/tmp` (the Read tool cannot see `/tmp`).

## Fallback only — source already has bare Unicode you cannot edit

If a paper's `.md` already contains bare Unicode and you cannot edit the source, wrap the math on the build temp before pandoc using the **sentinel technique**: replace the longest tokens first with placeholders like `\x00i\x00`, then the single symbols, then expand the placeholders last. A naive `.replace` chain breaks by nesting `$...$` (e.g. `d-1` -> `$d-1$` re-entering an already-wrapped `$b^{1/(d-1)}$`, causing a silent LaTeX failure). This is a fallback, not the default. The default is: author in math mode.

## Note for `Paper_RelationalTick_v1.md` specifically

That draft currently mixes ASCII stand-ins (alpha_1, 10^-93, P11) with a few bare Unicode symbols (e.g. `∂_t`). Before building, do a math-mode pass: convert bare symbols and the ASCII stand-ins to LaTeX math (`$\alpha_1$`, `$10^{-93}$`, `$\partial_t$`), then run the plain build above. This keeps it consistent with the corpus and avoids blanked glyphs.
