# Realot Studio Documentation

This is the live, source-aligned documentation website for the Realot Studio browser-based 2D game engine.

## Open the documentation

**https://realot-studio.pages.dev**

This is the Cloudflare Pages project URL. Start at the home page; users and AI assistants can discover every guide and API reference from there. Documentation uses stable, unversioned URLs. When the engine changes, publish the updated documentation to the same site—there is no version selector or documentation download required.

## Deploy with Cloudflare Pages

1. Create a Cloudflare Pages project named **`realot-studio`**.
2. Connect this repository (or upload the generated static site).
3. Set the production branch to `main` if deploying from Git.
4. Set the build output directory to the repository root (`/`) when deploying the already-generated site. No framework preset or build command is required for the generated static output.
5. Cloudflare Pages will publish it at **https://realot-studio.pages.dev**. If the project name is different, Cloudflare will issue a different `*.pages.dev` address and the canonical origin must be changed to match.

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

## Rebuild the website

```bash
cd generator
python3 tools/extract_source_facts.py <engine-root> source-facts.json
node tools/extract_easings.mjs <engine-root> easings.json
python3 build.py --out .. --origin https://realot-studio.pages.dev
```

The `--origin` value must match the actual published Cloudflare Pages URL. It generates canonical URLs, absolute sitemap entries and crawler metadata.

## Reference coverage

The component reference is generated from the engine runtime source. It covers all 25 component types and 355 public component fields, including field types and constructor defaults. The script-module reference enumerates all 24 script API modules and 365 names in their source allow-lists, with a visible warning for any allow-listed member that is not implemented. The live AI Bridge catalogue contains all 93 hosted MCP tools and their complete JSON input schemas. Editor menus, panel visibility, tags, physics layers, navigation areas, stored performance defaults, export formats, and the three-APK-exports-per-rolling-14-day allowance are documented separately. The optional local MCP companion source is identified as not wired into the supplied editor startup path. Rebuild from the matching engine source whenever the engine changes; the docs should not be treated as proof that a later engine build has identical APIs.

## AI discovery

Give an AI assistant this root URL:

`https://realot-studio.pages.dev`

It should fetch `/llms.txt`, then `/search-index.json`, search the records' `content` fields for the closest matches, and fetch the selected record's `url` (or its `.md` twin). It does not need a topic-specific path in advance. The same root also exposes `/llms-full.txt`, `/api/index.json`, `/sitemap.xml` and `/robots.txt`.

The search index is static data rather than a hosted semantic-search API; an external assistant can rank the indexed content using its own retrieval system.
