---
title: Anetos — a batteries-included web framework for Go
layout: hextra-home
description: Anetos is a batteries-included web framework for Go — routing, data, accounts, queues, mail, storage, search, AI and translations in one binary, built on net/http.
---

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-badge link="https://github.com/anetos-dev/anetos/blob/main/docs/planning/roadmap.md" >}}
  Pre-release · v0.3 on its way
  {{< icon name="arrow-circle-right" attributes="height=14" >}}
{{< /hextra/hero-badge >}}
</div>

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
  Build web apps in Go, at ease
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-12">
{{< hextra/hero-subtitle >}}
  Routing, data, accounts, queues, mail, storage, search, AI and translations in one framework, built on `net/http`. One binary runs it all.
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-6 hx:flex hx:flex-wrap hx:gap-3">
{{< hextra/hero-button text="Get started" link="https://docs.anetos.dev/getting-started/" >}}
{{< hextra/hero-button text="Read the docs" link="https://docs.anetos.dev/" style="background: transparent; color: inherit; border: 1px solid rgb(156 163 175 / 0.6);" >}}
</div>

<div class="anetos-section">

## From zero to an app with accounts

```sh
go install anetos.dev/anetos/cli/cmd/anetos@latest

anetos new blog && cd blog # templ views, sessions, CSRF, SQLite by default
go tool anetos make:auth   # accounts: password, Google, GitHub, API tokens
go run . migrate
go tool anetos dev         # rebuild and reload on every change

go build -o blog . && ./blog   # web, queue workers and the scheduler, in one binary
```

</div>

<div class="anetos-section">

## Batteries included, Go all the way

<p class="anetos-lead">Typed handlers and models, generated code instead of reflection at run time, and plain <code>net/http</code> underneath: the comfort of Laravel or Rails, without leaving Go's way of doing things.</p>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    icon="switch-horizontal"
    title="HTTP that stays net/http"
    subtitle="A router, typed handlers that bind and validate their input, middleware, sessions, CSRF and htmx-friendly views."
    link="https://docs.anetos.dev/guides/handlers/"
  >}}
  {{< hextra/feature-card
    icon="database"
    title="Data, typed"
    subtitle="A query builder with generated columns, relations without N+1, migrations and seeders on PostgreSQL, MySQL, MariaDB and SQLite."
    link="https://docs.anetos.dev/guides/database/"
  >}}
  {{< hextra/feature-card
    icon="user-group"
    title="Accounts and permissions"
    subtitle="Login with passwords, Google and GitHub, API tokens, email verification, and roles per app or per team."
    link="https://docs.anetos.dev/guides/accounts/"
  >}}
  {{< hextra/feature-card
    icon="lightning-bolt"
    title="Work in the background"
    subtitle="Queues, events, pub/sub listeners and a scheduler, supervised in the same binary — or split by role when you scale."
    link="https://docs.anetos.dev/guides/queues/"
  >}}
  {{< hextra/feature-card
    icon="sparkles"
    title="AI in the app"
    subtitle="Typed model calls, tools that act as the user, streamed answers, stored conversations and budgets: Anthropic, OpenAI and Gemini."
    link="https://docs.anetos.dev/guides/ai/"
  >}}
  {{< hextra/feature-card
    icon="search"
    title="Search"
    subtitle="Full-text, vector and hybrid search in the database you already run, with no separate search server."
    link="https://docs.anetos.dev/guides/search/"
  >}}
  {{< hextra/feature-card
    icon="translate"
    title="Every language, every zone"
    subtitle="Translations in YAML, the visitor's language from the URL or their settings, dates and prices in their locale, times stored in UTC."
    link="https://docs.anetos.dev/guides/translations/"
  >}}
  {{< hextra/feature-card
    icon="mail"
    title="Mail and files"
    subtitle="Templated mail over SMTP or Postmark, and file storage on disk, S3 or Google Cloud Storage with signed URLs."
    link="https://docs.anetos.dev/guides/storage/"
  >}}
  {{< hextra/feature-card
    icon="beaker"
    title="Tests that read like specs"
    subtitle="A test client, fakes for mail, queues, AI and the clock, and database helpers — no server to start."
    link="https://docs.anetos.dev/guides/testing/"
  >}}
{{< /hextra/feature-grid >}}

</div>

<div class="anetos-section">

## Handlers that say what they take

<p class="anetos-lead">Input structs say where each value comes from and how it's checked. The handler gets it ready to use, and returns typed output or an error that becomes the right HTTP response.</p>

```go
// CreateNote binds from JSON or a form; the rules run before the handler.
type CreateNote struct {
	Title string   `json:"title" validate:"required|max:200"`
	Body  string   `json:"body" validate:"max:10000"`
	Tags  []string `json:"tags" validate:"max:5|distinct|alpha_dash"`
}

func (h *Notes) Store(c *web.Ctx, in CreateNote) (web.Responder, error) {
	note := &Note{Title: in.Title, Body: in.Body, Tags: in.Tags}
	if err := db.Create(c, note); err != nil {
		return nil, err
	}
	return web.Created(note), nil // 201, as JSON
}

r.Post("/notes", web.H(h.Store)).Name("notes.store")
```

</div>

<div class="anetos-section">

## Status

<p class="anetos-lead">Anetos is pre-release: v0.3, the first public version, is in progress, and APIs will change until 1.0. Follow along or help on <a href="https://github.com/anetos-dev/anetos">GitHub</a>; the <a href="https://github.com/anetos-dev/anetos/blob/main/docs/planning/roadmap.md">roadmap</a> says what's done and what's next.</p>

</div>
