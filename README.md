<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/anetos-logo-dark.svg">
    <img alt="Anetos" src="brand/anetos-logo.svg" width="240">
  </picture>
</p>

# anetos.dev

The source of [anetos.dev](https://anetos.dev), the home page of
[Anetos](https://github.com/anetos-dev/anetos), a batteries-included web
framework for Go. It also answers `go get` for the `anetos.dev/…` import
paths (the `go-import` meta tags that point them at GitHub).

The documentation is at [docs.anetos.dev](https://docs.anetos.dev), built
by [anetos-dev/docs](https://github.com/anetos-dev/docs) from the
framework's repository.

## Working on it

The site is [Hugo](https://gohugo.io) (0.158 or later; it's built with
0.167) and the [Hextra](https://imfing.github.io/hextra/) theme, vendored
in `_vendor/` so builds need no network.

```sh
hugo server          # http://localhost:1313, reloads on save
hugo --gc --minify   # the site, in public/
```

| Path | What |
|---|---|
| `content/_index.md` | The home page |
| `brand/` | The logo and icons (see its README); served under `/brand/` |
| `static/_redirects` | The `go get` paths (`/anetos/…` → `/go/anetos/`) and shortcuts |
| `static/go/` | The `go-import` pages, one per module repository |
| `static/_headers` | Response headers |
| `layouts/home.securitytxt.txt` | `/.well-known/security.txt` (RFC 9116): where to report a vulnerability. Written at each build with an `Expires` 180 days on; `.github/workflows/rebuild.yml` rebuilds the site monthly (Cloudflare Pages deploy hook, secret `CLOUDFLARE_PAGES_DEPLOY_HOOK`) so it never lapses |
| `assets/css/custom.css` | The colours and the home page's sections |

A new Go repository under anetos.dev (`anetos.dev/twilio`, say) needs a
page in `static/go/<name>/` (copy `anetos`'s) and its two lines in
`_redirects`.

To update the theme: `hugo mod get github.com/imfing/hextra@<version> &&
hugo mod vendor`.

## Deployment

Cloudflare Pages builds `main` on every push (and previews for pull
requests): build command `hugo --gc --minify`, output `public`,
environment variable `HUGO_VERSION=0.167.0`.

## License

Apache-2.0, as Anetos.
