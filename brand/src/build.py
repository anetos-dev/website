# Builds the Anetos logo files (the SVGs in the parent folder) from the
# mark's geometry and the name set in Varela Round, as outlines.
#
#   pip install uharfbuzz fonttools && python3 build.py
import math, os
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
FONT = os.path.join(HERE, "VarelaRound-Regular.ttf")

BLUE = "#4B9AD2"
TEXT = "#545454"
TEXT_DARK = "#E8E8E8"

# ---- the mark: H = 100 units ----
SL, SR = 1.6, 2.0          # slopes (rise/run) of the left and right legs
T = 22.4                   # stroke thickness, perpendicular
WL = T * math.sqrt(1 + SL * SL) / SL
WR = T * math.sqrt(1 + SR * SR) / SR
APEX = 100 / SL            # apex x
SHELF = 78.0               # y of the shelf
SHELF_LEFT = 57.5          # x where the foot leaves the shelf
FOOT = 100 - SHELF

iy = (WL + WR) / (1 / SL + 1 / SR)          # inner apex
ix = APEX - iy / SL + WL
pts = [
    (APEX, 0),
    (APEX + SHELF / SR, SHELF),
    (APEX + SHELF / SR - FOOT / SL, 100),
    (SHELF_LEFT - FOOT / SL, 100),
    (SHELF_LEFT, SHELF),
    (APEX + SHELF / SR - WR, SHELF),
    (ix, iy),
    (WL, 100),
    (0, 100),
]
MARK_W = max(p[0] for p in pts)


def fmt(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s if s != "-0" else "0"


def mark_path(dx=0.0, dy=0.0, s=1.0):
    return "M" + " L".join(f"{fmt(dx + x * s)} {fmt(dy + y * s)}" for x, y in pts) + " Z"


# ---- the name, as outlines ----
ttf = TTFont(FONT)
UPM = ttf["head"].unitsPerEm
CAP = ttf["OS/2"].sCapHeight
gs = ttf.getGlyphSet()


def shape(text):
    blob = hb.Blob.from_file_path(FONT)
    face = hb.Face(blob)
    font = hb.Font(face)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    names = [ttf.getGlyphName(i.codepoint) for i in buf.glyph_infos]
    return list(zip(names, buf.glyph_positions))


def text_path(text, x, baseline, cap_height):
    """Outlines of text with its left at x, its baseline at baseline, and
    capitals cap_height tall. Returns (path, width)."""
    s = cap_height / CAP
    pen = SVGPathPen(gs, ntos=fmt)
    pen_x = 0
    glyphs = shape(text)
    for name, pos in glyphs:
        tp = TransformPen(pen, (s, 0, 0, -s, x + (pen_x + pos.x_offset) * s, baseline - pos.y_offset * s))
        gs[name].draw(tp)
        pen_x += pos.x_advance
    # visible extent of the ink
    bp = BoundsPen(gs)
    px = 0
    xmin, xmax = None, None
    for name, pos in glyphs:
        bp.init() if hasattr(bp, "init") else None
        b = BoundsPen(gs)
        gs[name].draw(b)
        if b.bounds:
            lo, hi = px + b.bounds[0], px + b.bounds[2]
            xmin = lo if xmin is None else min(xmin, lo)
            xmax = hi if xmax is None else max(xmax, hi)
        px += pos.x_advance
    return pen.getCommands(), xmin * s, xmax * s


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {fmt(w)} {fmt(h)}" '
            f'role="img" aria-label="{title}">\n<title>{title}</title>\n{body}\n</svg>\n')


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)


# mark alone
write("anetos-mark.svg", svg(MARK_W, 100, f'<path fill="{BLUE}" d="{mark_path()}"/>', "Anetos"))

# horizontal: name beside the mark, baseline on the mark's bottom
CAP_H = 85.5        # cap height, in mark units (sketch)
GAP_H = 33.6
for variant, color in (("", TEXT), ("-dark", TEXT_DARK)):
    tx = MARK_W + GAP_H
    _, lo, hi = text_path("Anetos", 0, 0, CAP_H)
    d, _, _ = text_path("Anetos", tx - lo, 100, CAP_H)
    w = tx + (hi - lo)
    body = f'<path fill="{BLUE}" d="{mark_path()}"/>\n<path fill="{color}" d="{d}"/>'
    write(f"anetos-logo{variant}.svg", svg(w, 100 + 2, body, "Anetos"))

# stacked: name centred under the mark
CAP_S = 31.1
GAP_S = 12.25
for variant, color in (("", TEXT), ("-dark", TEXT_DARK)):
    _, lo, hi = text_path("Anetos", 0, 0, CAP_S)
    tw = hi - lo
    w = max(tw, MARK_W)
    mx = (w - MARK_W) / 2
    base = 100 + GAP_S + CAP_S
    d, _, _ = text_path("Anetos", (w - tw) / 2 - lo, base, CAP_S)
    body = f'<path fill="{BLUE}" d="{mark_path(mx)}"/>\n<path fill="{color}" d="{d}"/>'
    write(f"anetos-logo-stacked{variant}.svg", svg(w, base + 1, body, "Anetos"))

# favicon: the mark in a square, a little padding
pad = 4
side = 100 + 2 * pad
fx = (side - MARK_W) / 2
write("favicon.svg", svg(side, side, f'<path fill="{BLUE}" d="{mark_path(fx, pad)}"/>', "Anetos"))

print("mark width", fmt(MARK_W), "inner apex", fmt(ix), fmt(iy), "WL", fmt(WL), "WR", fmt(WR))
for p in pts:
    print(fmt(p[0]), fmt(p[1]))
