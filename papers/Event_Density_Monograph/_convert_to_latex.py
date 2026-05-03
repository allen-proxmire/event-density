#!/usr/bin/env python3
"""Convert Event_Density_Monograph_Integrated.md to Event_Density_Monograph.tex."""

import os
import re
import sys

ROOT = r"C:\Users\allen\GitHub\event-density\papers\Event_Density_Monograph"
SRC = os.path.join(ROOT, "Event_Density_Monograph_Integrated.md")
DST = os.path.join(ROOT, "Event_Density_Monograph.tex")
FIGS_DIR = os.path.join(ROOT, "figures")

# Build figure (chapter-relative) -> filename stem map.
# Chapter figures: map chapter K, figure J -> fig number = chapter_start[K] + (J-1).
chapter_start = {
    1: 1, 2: 5, 3: 10, 4: 16,
    5: 22, 6: 28, 7: 34,
    8: 42, 9: 49, 10: 58,
    11: 66, 12: 75, 13: 85,
    14: 95, 15: 104,
}

# Slug suffixes for fig_NN_<slug>.svg, indexed by fig number 1..133
slugs = {}
for fname in sorted(os.listdir(FIGS_DIR)):
    m = re.match(r"fig_(\d{2,3})_(.+)\.svg$", fname)
    if m:
        n = int(m.group(1))
        slugs[n] = m.group(2)


def fig_key_to_stem(key: str) -> str | None:
    """Map a figure label like '7.3' or 'A.1' or 'C.2' or 'D.1' to fig file stem."""
    m = re.match(r"^(\d+)\.(\d+)$", key)
    if m:
        ch = int(m.group(1))
        j = int(m.group(2))
        if ch in chapter_start:
            n = chapter_start[ch] + (j - 1)
            slug = slugs.get(n)
            if slug:
                return f"fig_{n:02d}_{slug}"
        return None
    # Appendix figure mapping
    appendix_map = {
        # Appendix A
        "A.1": 112, "A.2": 113,
        # Appendix B
        "B.1": 117,
        # Appendix C
        "C.1": 121,
        # Appendix D
        "D.1": 125, "D.2": 126,
    }
    if key in appendix_map:
        n = appendix_map[key]
        slug = slugs.get(n)
        if slug:
            return f"fig_{n:02d}_{slug}"
    return None


def latex_escape(text: str) -> str:
    """Escape LaTeX special chars in body text. Conservative: only chars likely to appear."""
    # Order matters
    repl = [
        ("\\", "\\textbackslash{}"),  # rare in body text
        ("&", "\\&"),
        ("%", "\\%"),
        ("$", "\\$"),
        ("#", "\\#"),
        ("_", "\\_"),
        ("{", "\\{"),
        ("}", "\\}"),
        ("~", "\\textasciitilde{}"),
        ("^", "\\textasciicircum{}"),
    ]
    for a, b in repl:
        text = text.replace(a, b)
    return text


def process_inline(line: str) -> str:
    """Process inline markdown formatting to LaTeX.

    Math $...$ is preserved as-is. Inline code, bold, italic are converted.
    """
    out = []
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if ch == "$":
            # find closing $
            j = line.find("$", i + 1)
            if j == -1:
                out.append(ch)
                i += 1
                continue
            out.append(line[i : j + 1])
            i = j + 1
        elif ch == "`":
            j = line.find("`", i + 1)
            if j == -1:
                out.append(ch)
                i += 1
                continue
            inner = line[i + 1 : j]
            out.append("\\texttt{" + latex_escape_minimal(inner) + "}")
            i = j + 1
        elif line.startswith("**", i):
            j = line.find("**", i + 2)
            if j == -1:
                out.append(line[i:i+2])
                i += 2
                continue
            inner = line[i + 2 : j]
            out.append("\\textbf{" + process_inline(inner) + "}")
            i = j + 2
        elif ch == "*":
            j = line.find("*", i + 1)
            if j == -1:
                out.append(ch)
                i += 1
                continue
            inner = line[i + 1 : j]
            # Avoid empty italic
            if not inner:
                out.append(ch)
                i += 1
                continue
            out.append("\\textit{" + process_inline(inner) + "}")
            i = j + 1
        else:
            # Escape only certain chars in non-math, non-code body
            if ch == "&":
                out.append("\\&")
            elif ch == "%":
                out.append("\\%")
            elif ch == "_":
                # Preserve underscores in obvious filenames/paths
                out.append("\\_")
            elif ch == "#":
                out.append("\\#")
            else:
                out.append(ch)
            i += 1
    return "".join(out)


def latex_escape_minimal(text: str) -> str:
    """Minimal escape for content already meant for \\texttt{}."""
    return text.replace("\\", "\\textbackslash{}").replace("{", "\\{").replace("}", "\\}").replace("_", "\\_").replace("#", "\\#").replace("&", "\\&").replace("%", "\\%").replace("$", "\\$")


def convert(md: str) -> str:
    lines = md.splitlines()
    out = []

    # Skip YAML front matter
    if lines and lines[0].strip() == "---":
        end = 1
        while end < len(lines) and lines[end].strip() != "---":
            end += 1
        lines = lines[end + 1 :]

    state_list = False  # currently inside itemize
    state_math = False  # currently inside ```math block
    state_code = False  # currently inside generic code block

    has_seen_part = False

    def flush_list():
        nonlocal state_list
        if state_list:
            out.append("\\end{itemize}")
            state_list = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        bare = line.strip()

        # Code/math fence handling — accept indented fences too
        if bare == "```math":
            flush_list()
            out.append("\\[")
            state_math = True
            i += 1
            continue
        if bare.startswith("```") and state_math:
            out.append("\\]")
            state_math = False
            i += 1
            continue
        if bare.startswith("```") and not state_math and not state_code:
            flush_list()
            out.append("\\begin{verbatim}")
            state_code = True
            i += 1
            continue
        if bare.startswith("```") and state_code:
            out.append("\\end{verbatim}")
            state_code = False
            i += 1
            continue
        if state_math or state_code:
            # Pass through unmodified (lstrip indentation for math display cleanliness)
            if state_math:
                out.append(line.lstrip() if line.lstrip() else line)
            else:
                out.append(line)
            i += 1
            continue

        # Page break
        if stripped == "\\newpage":
            flush_list()
            out.append("\\newpage")
            i += 1
            continue

        # Headings
        # Match ## Chapter N — Title
        m = re.match(r"^## Chapter (\d+) — (.+)$", stripped)
        if m:
            flush_list()
            ch_num = int(m.group(1))
            ch_title = m.group(2)
            out.append("")
            out.append("\\chapter{" + process_inline(ch_title) + "}")
            out.append("\\label{chap:" + str(ch_num) + "}")
            i += 1
            continue

        # ## Appendix X — Title
        m = re.match(r"^## Appendix ([A-D]) — (.+)$", stripped)
        if m:
            flush_list()
            letter = m.group(1)
            title = m.group(2)
            if letter == "A":
                # Begin appendix block on first appendix
                out.append("")
                out.append("\\appendix")
            out.append("\\chapter{Appendix " + letter + " --- " + process_inline(title) + "}")
            out.append("\\label{app:" + letter + "}")
            i += 1
            continue

        # ### subsection
        m = re.match(r"^### (.+)$", stripped)
        if m:
            flush_list()
            out.append("\\section{" + process_inline(m.group(1)) + "}")
            i += 1
            continue

        # #### subsubsection
        m = re.match(r"^#### (.+)$", stripped)
        if m:
            flush_list()
            out.append("\\subsection{" + process_inline(m.group(1)) + "}")
            i += 1
            continue

        # ##### sub-subsubsection
        m = re.match(r"^##### (.+)$", stripped)
        if m:
            flush_list()
            out.append("\\subsubsection{" + process_inline(m.group(1)) + "}")
            i += 1
            continue

        # # Top-level
        m = re.match(r"^# (.+)$", stripped)
        if m:
            flush_list()
            title = m.group(1)
            if title.startswith("Part "):
                out.append("")
                out.append("\\part{" + process_inline(title) + "}")
                has_seen_part = True
            elif title == "Title Page":
                # skip — handled by \maketitle
                # consume rest of title-page content until next heading
                i += 1
                while i < len(lines) and not lines[i].startswith("#"):
                    i += 1
                continue
            elif title in ("Foreword", "How to Read This Monograph", "Closing Note"):
                out.append("\\chapter*{" + process_inline(title) + "}")
                out.append("\\addcontentsline{toc}{chapter}{" + process_inline(title) + "}")
            elif title == "Table of Contents":
                # Don't render the markdown TOC; LaTeX has \tableofcontents at front.
                # Skip section content until next heading.
                i += 1
                while i < len(lines) and not lines[i].startswith("#"):
                    i += 1
                continue
            else:
                out.append("\\chapter*{" + process_inline(title) + "}")
            i += 1
            continue

        # Horizontal rule
        if stripped == "---":
            flush_list()
            out.append("\\bigskip\\hrule\\bigskip")
            i += 1
            continue

        # Bullet list
        m = re.match(r"^- (.+)$", stripped)
        if m:
            if not state_list:
                out.append("\\begin{itemize}")
                state_list = True
            out.append("\\item " + process_inline(m.group(1)))
            i += 1
            continue

        # Numbered list (1. , 2. , …) — convert to enumerate
        m = re.match(r"^(\d+)\. (.+)$", stripped)
        if m:
            if state_list:
                out.append("\\end{itemize}")
                state_list = False
            # Detect enumerate block
            out.append("\\begin{enumerate}")
            while i < len(lines):
                m2 = re.match(r"^(\d+)\. (.+)$", lines[i].rstrip())
                if not m2:
                    break
                out.append("\\item " + process_inline(m2.group(2)))
                i += 1
            out.append("\\end{enumerate}")
            continue

        # Figure description detection: a paragraph starting with **Figure X.Y — caption.**
        m = re.match(r"^\*\*(?:Figure|Table) ([0-9A-D]+\.[0-9]+) — (.+?)\.\*\*\s*(.*)$", stripped)
        if m:
            flush_list()
            key = m.group(1)
            cap_title = m.group(2)
            cap_rest = m.group(3)
            stem = fig_key_to_stem(key)
            label_letter = "Figure" if cap_rest is not None else "Figure"
            # Use word "Figure" or "Table" matching the markdown
            kind_match = re.match(r"^\*\*(Figure|Table)", stripped)
            kind = kind_match.group(1) if kind_match else "Figure"
            if stem:
                out.append("")
                out.append("\\begin{figure}[ht]")
                out.append("\\centering")
                out.append("\\includesvg[width=0.85\\textwidth]{" + stem + "}")
                cap_full = process_inline(cap_title) + ". " + process_inline(cap_rest) if cap_rest else process_inline(cap_title)
                out.append("\\caption*{" + kind + " " + key + " --- " + cap_full + "}")
                out.append("\\label{fig:" + stem + "}")
                out.append("\\end{figure}")
                i += 1
                continue
            # Fall through if no mapping

        # Default: regular paragraph line
        if stripped == "":
            flush_list()
            out.append("")
        else:
            out.append(process_inline(stripped))
        i += 1

    flush_list()
    return "\n".join(out)


def main():
    with open(SRC, "r", encoding="utf-8") as f:
        md = f.read()

    body = convert(md)

    preamble = r"""\documentclass[11pt]{book}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\graphicspath{{figures/}}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont{Latin Modern Mono}
\usepackage{microtype}
\usepackage{caption}
\usepackage{newunicodechar}
\newunicodechar{—}{---}
\newunicodechar{–}{--}
\newunicodechar{≈}{$\approx$}
\newunicodechar{≤}{$\leq$}
\newunicodechar{≥}{$\geq$}
\newunicodechar{≠}{$\neq$}
\newunicodechar{∼}{$\sim$}
\newunicodechar{×}{$\times$}
\newunicodechar{·}{$\cdot$}
\newunicodechar{→}{$\rightarrow$}
\newunicodechar{←}{$\leftarrow$}
\newunicodechar{↔}{$\leftrightarrow$}
\newunicodechar{⇒}{$\Rightarrow$}
\newunicodechar{∇}{$\nabla$}
\newunicodechar{∂}{$\partial$}
\newunicodechar{∫}{$\int$}
\newunicodechar{∞}{$\infty$}
\newunicodechar{α}{$\alpha$}
\newunicodechar{β}{$\beta$}
\newunicodechar{γ}{$\gamma$}
\newunicodechar{δ}{$\delta$}
\newunicodechar{ε}{$\epsilon$}
\newunicodechar{ζ}{$\zeta$}
\newunicodechar{η}{$\eta$}
\newunicodechar{θ}{$\theta$}
\newunicodechar{ι}{$\iota$}
\newunicodechar{κ}{$\kappa$}
\newunicodechar{λ}{$\lambda$}
\newunicodechar{μ}{$\mu$}
\newunicodechar{ν}{$\nu$}
\newunicodechar{ξ}{$\xi$}
\newunicodechar{π}{$\pi$}
\newunicodechar{ρ}{$\rho$}
\newunicodechar{σ}{$\sigma$}
\newunicodechar{τ}{$\tau$}
\newunicodechar{υ}{$\upsilon$}
\newunicodechar{φ}{$\phi$}
\newunicodechar{χ}{$\chi$}
\newunicodechar{ψ}{$\psi$}
\newunicodechar{ω}{$\omega$}
\newunicodechar{Γ}{$\Gamma$}
\newunicodechar{Δ}{$\Delta$}
\newunicodechar{Θ}{$\Theta$}
\newunicodechar{Λ}{$\Lambda$}
\newunicodechar{Ξ}{$\Xi$}
\newunicodechar{Π}{$\Pi$}
\newunicodechar{Σ}{$\Sigma$}
\newunicodechar{Φ}{$\Phi$}
\newunicodechar{Ψ}{$\Psi$}
\newunicodechar{Ω}{$\Omega$}
\newunicodechar{ℏ}{$\hbar$}
\newunicodechar{ℓ}{$\ell$}
\newunicodechar{𝓜}{$\mathcal{M}$}
\newunicodechar{𝓤}{$\mathcal{U}$}
\newunicodechar{𝓢}{$\mathcal{S}$}
\newunicodechar{𝓔}{$\mathcal{E}$}
\newunicodechar{𝓞}{$\mathcal{O}$}
\newunicodechar{𝓣}{$\mathcal{T}$}
\newunicodechar{⨂}{$\otimes$}
\newunicodechar{∈}{$\in$}
\newunicodechar{∝}{$\propto$}
\newunicodechar{‐}{-}
\newunicodechar{‑}{-}
\newunicodechar{‒}{-}
\newunicodechar{‘}{`}
\newunicodechar{’}{'}
\newunicodechar{“}{``}
\newunicodechar{”}{''}
\newunicodechar{…}{\ldots}
\newunicodechar{⁻}{$^{-}$}
\newunicodechar{₁}{$_{1}$}
\newunicodechar{₂}{$_{2}$}
\newunicodechar{₀}{$_{0}$}
\newunicodechar{³}{$^{3}$}
\newunicodechar{⁴}{$^{4}$}
\newunicodechar{²}{$^{2}$}

\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  urlcolor=blue,
  citecolor=blue,
  pdftitle={Event Density: A Substrate-Level Architecture of Physics},
  pdfauthor={Allen Proxmire}
}

\title{Event Density: A Substrate-Level Architecture of Physics\\[0.5em]
\large Foundations, Theorems, and Architectural Closure Across Nine Sectors}
\author{Allen Proxmire}
\date{May 2026}

\begin{document}

\frontmatter
\maketitle
\tableofcontents
\mainmatter

"""

    closing = "\n\n\\end{document}\n"

    with open(DST, "w", encoding="utf-8") as f:
        f.write(preamble)
        f.write(body)
        f.write(closing)

    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")


if __name__ == "__main__":
    main()
