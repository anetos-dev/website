# Renders the browser and app icons from favicon.svg, and the social
# preview image (link cards on GitHub, Slack, X…) from the logo.
#
#   pip install cairosvg pillow && python3 pngs.py
import cairosvg, io, os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)


def render(name, w=None, h=None):
    png = cairosvg.svg2png(url=os.path.join(OUT, name), output_width=w, output_height=h)
    return Image.open(io.BytesIO(png)).convert('RGBA')


def square(name, side):
    return render(name, side, side)


# browser icons
icons = [square('favicon.svg', s) for s in (16, 32, 48)]
icons[2].save(os.path.join(OUT, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)], append_images=icons[:2])
icons[0].save(os.path.join(OUT, 'favicon-16x16.png'))
icons[1].save(os.path.join(OUT, 'favicon-32x32.png'))
square('favicon.svg', 192).save(os.path.join(OUT, 'icon-192.png'))
square('favicon.svg', 512).save(os.path.join(OUT, 'icon-512.png'))

# Apple touch icon: no transparency, the mark on white with room around it
bg = Image.new('RGBA', (180, 180), (255, 255, 255, 255))
m = square('favicon.svg', 140)
bg.paste(m, (20, 18), m)
bg.convert('RGB').save(os.path.join(OUT, 'apple-touch-icon.png'))

# Social preview, 1280×640: the logo and the tagline, centred
W, H = 1280, 640
card = Image.new('RGBA', (W, H), (248, 250, 252, 255))
logo = render('anetos-logo.svg', h=150)
card.paste(logo, ((W - logo.width) // 2, 200), logo)
font = ImageFont.truetype(os.path.join(HERE, 'VarelaRound-Regular.ttf'), 40)
tagline = 'A batteries-included web framework for Go'
d = ImageDraw.Draw(card)
tw = d.textlength(tagline, font=font)
d.text(((W - tw) / 2, 410), tagline, font=font, fill=(84, 84, 84, 255))
card.convert('RGB').save(os.path.join(OUT, 'social-preview.png'), optimize=True)
print('ok')
