"""Render ED program roadmap Mermaid diagram via mermaid.ink.

Produces both white-bg and transparent variants. Same paren-encoding +
label-quoting compatibility shim used in prior renderers.
"""
import base64
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "ed_program_roadmap.mmd"
OUT_WHITE = HERE / "ed_program_roadmap_mermaid.png"
OUT_TR    = HERE / "ed_program_roadmap_mermaid_transparent.png"

source = SRC.read_text(encoding="utf-8")
patched = source.replace("(", "&#40;").replace(")", "&#41;")

NODE_LABEL = re.compile(r"\[([^\[\]\n]*)\]")
def _quote_brackets(match):
    inner = match.group(1)
    if inner.startswith('"') and inner.endswith('"'):
        return match.group(0)
    return f'["{inner.replace(chr(34), chr(92)+chr(34))}"]'
patched = NODE_LABEL.sub(_quote_brackets, patched)

encoded = base64.urlsafe_b64encode(patched.encode("utf-8")).decode("ascii")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
      "AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0.0.0 Safari/537.36")

def fetch(url, attempts=4):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "image/png,image/*;q=0.9,*/*;q=0.8",
    })
    for n in range(attempts):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            body = e.read()
            if body.startswith(b"\x89PNG"):
                print(f"  attempt {n+1}: HTTP {e.code} but PNG body salvaged",
                      file=sys.stderr)
                return body
            print(f"  attempt {n+1}: HTTP {e.code} {e.reason}; sleep+retry",
                  file=sys.stderr)
            time.sleep(8)
        except urllib.error.URLError as e:
            print(f"  attempt {n+1}: URL error {e}; sleep+retry", file=sys.stderr)
            time.sleep(8)
    return None

# White-background variant
url_w = f"https://mermaid.ink/img/{encoded}?type=png&width=2400&bgColor=FFFFFF"
print(f"-> {OUT_WHITE.name}", file=sys.stderr)
data_w = fetch(url_w)
if data_w and data_w.startswith(b"\x89PNG"):
    OUT_WHITE.write_bytes(data_w)
    from PIL import Image
    with Image.open(OUT_WHITE) as img:
        print(f"   wrote {OUT_WHITE.name}  {img.size[0]}x{img.size[1]}  mode={img.mode}",
              file=sys.stderr)
else:
    print(f"   FAILED to render white-bg variant", file=sys.stderr)
    sys.exit(1)

# Transparent variant
url_t = f"https://mermaid.ink/img/{encoded}?type=png&width=2400"
print(f"-> {OUT_TR.name}", file=sys.stderr)
data_t = fetch(url_t)
if data_t and data_t.startswith(b"\x89PNG"):
    OUT_TR.write_bytes(data_t)
    from PIL import Image
    with Image.open(OUT_TR) as img:
        print(f"   wrote {OUT_TR.name}  {img.size[0]}x{img.size[1]}  mode={img.mode}",
              file=sys.stderr)
else:
    print(f"   FAILED to render transparent variant (white-bg already saved)",
          file=sys.stderr)
