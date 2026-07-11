"""Assemble the Unification Report: concat sections/S00..S16, strip provenance + draft-notes.

Run from anywhere:  python docs/Unification_Report/build/assemble_report.py
Output: docs/Unification_Report/ED_UnifiedFramework_ASSEMBLED.md  (a STAGED build artifact;
regenerate after any section edit, do not hand-edit).
"""
import re, glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # docs/Unification_Report
SECT = os.path.join(ROOT, "sections")
OUT  = os.path.join(ROOT, "ED_UnifiedFramework_ASSEMBLED.md")

def clean(text):
    # 1. drop the provenance italic line (any italic line containing "Draft v1,")
    text = re.sub(r'(?m)^\*[^\n]*Draft v1,.*$', '', text)
    # 2. drop the trailing draft-notes block (from its preceding --- to EOF)
    text = re.sub(r'(?s)\n?\n---\s*\n+\*Draft notes for finalization:\*.*\Z', '\n', text)
    # 3. drop the FIRST standalone --- line (the title/provenance separator)
    text = re.sub(r'(?m)^---[ \t]*\n', '', text, count=1)
    # 4. collapse 3+ newlines, trim
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'

def main():
    files = sorted(glob.glob(os.path.join(SECT, "S*.md")))
    parts = [clean(open(f, encoding='utf-8').read()) for f in files]
    banner = ("<!-- ASSEMBLED from sections/S00..S16 by build/assemble_report.py. "
              "STAGED artifact - regenerate after any section edit; do not hand-edit. -->\n\n")
    body = banner + "\n\n".join(parts)
    open(OUT, 'w', encoding='utf-8').write(body)
    words = len(re.findall(r'\S+', body))
    print(f"Assembled {len(files)} sections -> {os.path.relpath(OUT, ROOT)}")
    print(f"Total words: {words} (~{words//450}-{words//400} pages)")

if __name__ == "__main__":
    main()
