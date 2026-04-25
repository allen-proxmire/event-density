"""Render Mermaid theorem-dependency diagram via mermaid.ink.

Same paren-encoding + label-quoting trick as the full_ed_architecture renderer:
the canonical .mmd source contains parens inside node labels and edge labels
(e.g. Cl(3,1), (−1)^{2s}, π_1(Q_2)) which Mermaid parsers reject. We patch
the source in memory only — the on-disk .mmd file is unchanged. The visual
output is identical because Mermaid renders &#40; / &#41; as ( / ).
"""
import base64
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "theorem_dependency_graph.mmd"
OUT = HERE / "theorem_dependency_graph_mermaid.png"

source = SRC.read_text(encoding="utf-8")

# Replace parens with HTML entities (visually identical to Mermaid).
patched = source.replace("(", "&#40;").replace(")", "&#41;")

# Quote node labels [...] for renderer compatibility.
def _quote_brackets(match: "re.Match") -> str:
    inner = match.group(1)
    if inner.startswith('"') and inner.endswith('"'):
        return match.group(0)
    inner_escaped = inner.replace('"', '\\"')
    return f'["{inner_escaped}"]'

NODE_LABEL = re.compile(r"\[([^\[\]\n]*)\]")
patched = NODE_LABEL.sub(_quote_brackets, patched)

encoded = base64.urlsafe_b64encode(patched.encode("utf-8")).decode("ascii")
url = f"https://mermaid.ink/img/{encoded}?type=png&width=2400&bgColor=FFFFFF"
print(f"Fetching: {url[:90]}... (encoded len {len(encoded)})", file=sys.stderr)

req = urllib.request.Request(
    url,
    headers={
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "image/png,image/*;q=0.9,*/*;q=0.8",
    },
)
try:
    with urllib.request.urlopen(req, timeout=120) as response:
        data = response.read()
        status = response.status
except urllib.error.HTTPError as e:
    data = e.read()
    status = e.code
    if not data.startswith(b"\x89PNG"):
        print(f"HTTP error: {e.code} {e.reason}", file=sys.stderr)
        print(data[:1000].decode("utf-8", errors="replace"), file=sys.stderr)
        sys.exit(1)
    print(f"HTTP {status} but body is valid PNG ({len(data)} bytes); salvaged.",
          file=sys.stderr)
except urllib.error.URLError as e:
    print(f"URL error: {e}", file=sys.stderr)
    sys.exit(2)

if not data.startswith(b"\x89PNG"):
    print(f"Response is not a PNG (first 64 bytes): {data[:64]!r}", file=sys.stderr)
    sys.exit(3)

OUT.write_bytes(data)
from PIL import Image
with Image.open(OUT) as img:
    print(f"Wrote {OUT} ({img.size[0]}x{img.size[1]})")
