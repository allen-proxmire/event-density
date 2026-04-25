"""Render ASCII kernel-architecture diagram to high-resolution PNG."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys

HERE = Path(__file__).parent
TXT = HERE / "kernel_architecture.txt"
OUT = HERE / "kernel_architecture_ascii.png"

text = TXT.read_text(encoding="utf-8")
lines = text.split("\n")

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\CascadiaMono.ttf",
    r"C:\Windows\Fonts\consola.ttf",
    r"C:\Windows\Fonts\lucon.ttf",
    r"C:\Windows\Fonts\cour.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
]
font_size = 46
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

dummy_img = Image.new("RGB", (1, 1), "white")
dummy_draw = ImageDraw.Draw(dummy_img)

def measure(s):
    bbox = dummy_draw.textbbox((0, 0), s, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

_, line_h = measure("M" + "Q" + "g")
line_h = int(line_h * 1.18)
char_w, _ = measure("M")

max_cols = max((len(line) for line in lines), default=80)
img_w = char_w * max_cols + 80
img_h = line_h * len(lines) + 60

img = Image.new("RGB", (img_w, img_h), (252, 252, 250))
draw = ImageDraw.Draw(img)

y = 30
x_origin = 40
for line in lines:
    draw.text((x_origin, y), line, fill=(15, 23, 42), font=font)
    y += line_h

img.save(OUT, "PNG", optimize=True)
print(f"Wrote {OUT} ({img_w}x{img_h})")
