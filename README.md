# Realot Studio Documentation

This is the live, source-aligned documentation website for the Realot Studio browser-based 2D game engine.

## Open the documentation

**https://realot-studio-documentation.pages.dev**

This is the Cloudflare Pages project URL. Start at the home page; users and AI assistants can discover every guide and API reference from there. Documentation uses stable, unversioned URLs. When the engine changes, publish the updated documentation to the same site—there is no version selector or documentation download required.

## Site layout

- `index.html`: documentation home page and main landing page.
- `docs/`: human-readable guides and API pages, each with a Markdown twin.
- `search.html`: browser-based full-text search over `search-index.json`.
- `llms.txt`: AI-agent entry point; explains how to discover and search documentation from the site root.
- `llms-full.txt`: complete documentation corpus in Markdown.
- `search-index.json`: full-text page index with titles, descriptions, headings, keywords, page URLs and searchable content.
- `api/index.json`: structured API catalog.
- `sitemap.html` and `sitemap.xml`: human and crawler site maps.
- `generator/`: source page fragments, generator and engine-source extraction tools.

