# Renders the browser and app icons from favicon.svg.
#
#   pip install cairosvg pillow && python3 pngs.py
import cairosvg, io, os
from PIL import Image

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def render(name, w):
    png = cairosvg.svg2png(url=os.path.join(OUT, name), output_width=w, output_height=w)
    return Image.open(io.BytesIO(png)).convert('RGBA')

# browser icons
icons = [render('favicon.svg', s) for s in (16, 32, 48)]
icons[2].save(os.path.join(OUT, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)], append_images=icons[:2])
render('favicon.svg', 32).save(os.path.join(OUT, 'favicon-32.png'))
render('favicon.svg', 512).save(os.path.join(OUT, 'icon-512.png'))

# Apple touch icon: no transparency, the mark on white with room around it
bg = Image.new('RGBA', (180, 180), (255, 255, 255, 255))
m = render('favicon.svg', 140)
bg.paste(m, (20, 18), m)
bg.convert('RGB').save(os.path.join(OUT, 'apple-touch-icon.png'))
print('ok')
