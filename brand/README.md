# Anetos brand

The logo and icons of Anetos. Use these files rather than redrawing them.

| File | Use |
|---|---|
| `anetos-logo.svg`, `anetos-logo-dark.svg` | The mark and the name side by side: headers, READMEs (`-dark` on dark backgrounds) |
| `anetos-logo-stacked.svg`, `anetos-logo-stacked-dark.svg` | The name under the mark: square spaces, title slides |
| `anetos-mark.svg` | The mark alone: avatars, small spaces |
| `favicon.svg`, `favicon.ico`, `favicon-32.png` | Browser tabs |
| `apple-touch-icon.png` | iOS home screen (180 px, on white) |
| `icon-512.png` | App manifests, social avatars |

## Colours

| Name | Hex | Use |
|---|---|---|
| Anetos blue | `#4B9AD2` | The mark, on light and dark backgrounds |
| Ink | `#545454` | The name on light backgrounds |
| Light | `#E8E8E8` | The name on dark backgrounds |

## Rules

- Keep the mark's proportions; don't stretch, rotate or outline it.
- Leave clear space around the logo of at least the height of the name's
  capital A.
- On photographs or busy backgrounds, use the dark variant on a solid
  dark panel.

## Sources

`src/build.py` draws the SVGs from the mark's geometry (two legs of equal
thickness at 58° and 63°, the foot parallel to the left leg) and the name
set in Varela Round, converted to outlines; `src/pngs.py` renders the
icons from `favicon.svg`.

```sh
cd src
pip install uharfbuzz fonttools cairosvg pillow
python3 build.py && python3 pngs.py
```

Varela Round is © The Varela Round Project Authors, under the SIL Open Font
License 1.1 (`src/OFL.txt`). The logo, designed by Samiul Hoque, is
licensed with the rest of this repository (Apache-2.0); the name "Anetos"
and the logo identify the project.
