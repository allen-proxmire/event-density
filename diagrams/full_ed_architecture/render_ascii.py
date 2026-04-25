"""Render ASCII diagram to high-resolution PNG using PIL with monospace font."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys

HERE = Path(__file__).parent
TXT = HERE / "full_ed_architecture.txt"
OUT = HERE / "full_ed_architecture_ascii.png"

# Read source
text = TXT.read_text(encoding="utf-8")
lines = text.split("\n")

# Font: try Cascadia Mono / Consolas / DejaVu Sans Mono / fallback
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\CascadiaMono.ttf",
    r"C:\Windows\Fonts\consola.ttf",          # Consolas
    r"C:\Windows\Fonts\lucon.ttf",            # Lucida Console
    r"C:\Windows\Fonts\cour.ttf",             # Courier New
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
]
font_size = 44          # large for >2000px width at ~80 columns
font = None
for path in FONT_CANDIDATES:
    try:
        font = ImageFont.truetype(path, font_size)
        print(f"Using font: {path}", file=sys.stderr)
        break
    except (OSError, IOError):
        continue
if font is None:
    font = ImageFont.load_default()
    print("Warning: falling back to PIL default font", file=sys.stderr)

# Measure line height + max width
dummy_img = Image.new("RGB", (1, 1), "white")
dummy_draw = ImageDraw.Draw(dummy_img)

# Use textbbox to measure
def measure(s):
    bbox = dummy_draw.textbbox((0, 0), s, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

# Approximate uniform line height from a representative ASCII line
_, line_h = measure("M" + "Q" + "g")  # mix of caps + descender
line_h = int(line_h * 1.18)            # 18% leading

# Char width from monospace measurement
char_w, _ = measure("M")

max_cols = max((len(line) for line in lines), default=80)
img_w = char_w * max_cols + 80         # 40px margin each side
img_h = line_h * len(lines) + 60       # 30px top/bottom

# Background: off-white with a thin border
img = Image.new("RGB", (img_w, img_h), (252, 252, 250))
draw = ImageDraw.Draw(img)

# Draw text lines
y = 30
x_origin = 40
for line in lines:
    draw.text((x_origin, y), line, fill=(15, 23, 42), font=font)
    y += line_h

# Save
img.save(OUT, "PNG", optimize=True)
print(f"Wrote {OUT} ({img_w}x{img_h})")
