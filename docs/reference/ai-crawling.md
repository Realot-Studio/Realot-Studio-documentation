# AI assistants and documentation search

> How people and AI tools can find accurate Realot Studio documentation from the documentation URL alone.

- Source: https://realot-studio.pages.dev/docs/reference/ai-crawling.html

> **One URL is enough to start:** Fetch llms.txt from the documentation root, then query api/search?q=your%20question . The search endpoint returns the closest matching guides and API pages with the correct relative URLs.

## Pages are directly readable

Each guide is static HTML with the full article text, headings, links, tables and code examples already in the page. JavaScript enhances navigation and search; it is not required to retrieve the documentation content. Every guide also has a Markdown twin at the same path with the `.md` suffix.

## Retrieval workflow

1. Start with the documentation URL you were given. Resolve the site's root, preserving a deployment prefix such as a GitHub Pages repository path.
2. Fetch `llms.txt` from that root. It is a compact map of the documentation sections and retrieval process.
3. Send the full question to `api/search?q=...` using URL encoding. The endpoint searches titles, descriptions, headings, keywords and page text, then ranks the closest matches.
4. Read the top results returned by the endpoint. Each result includes a relative `url`, title, section, relevance score and a useful text snippet. Resolve the returned URL against the documentation root; do not construct page paths yourself.
5. For broad questions, fetch `llms-full.txt`. If the endpoint is unavailable, fetch `search-index.json` and perform the same retrieval locally.
6. For exact engine API questions, fetch `api/index.json` and the human-readable [complete script module index](../api/script-modules.html). The JSON lists component scene fields/defaults, all lifecycle callbacks, enum values, all 24 script API modules and their supported member names, plus global API groups.

The [human search page](../../search.html) uses the same ranking behavior. The endpoint is a relevance-ranked documentation search, not a generative AI model: it returns the closest source pages for the assistant to read and use.

## Machine-readable files

| Path from docs root | Contents |
| --- | --- |
| `llms.txt` | Compact index with exact discovery and retrieval instructions. |
| `llms-full.txt` | Full documentation text in one Markdown file. |
| `api/search?q=...` | Question-based search endpoint. Returns the closest matching pages, snippets, relevance scores and relative URLs. |
| `search-index.json` | Complete page search records, including content text, headings and keywords; fallback for tools that cannot call the endpoint. |
| `api/index.json` | Source-derived component and script API catalog, including every supported module member name and component field/default. |
| `api/manifest.json` | Catalog metadata and counts. |
| `sitemap.xml` | Absolute page URLs when built with the public documentation origin. |
| `robots.txt` | Crawler access policy. |

## Editor automation

For an assistant that needs to operate the currently open editor, use the [AI Bridge and MCP reference](ai-bridge.html). The bridge tools modify live project data; they are distinct from the gameplay scripting API catalog.

## Use engine source as the ground truth

The component field catalog is extracted from the runtime component constructors. The script module member lists come from each API module's exported allow-list. Human explanations complement these lists but should not be treated as permission to call undocumented engine internals. If an API member is absent from the source-derived allow-list, do not recommend it as supported.

The documentation uses stable, unversioned URLs. Publishing an updated engine and documentation replaces the current reference at those same paths; users do not need a separate documentation version download.

## Publishing requirements

Build with the public documentation origin so canonical links and `sitemap.xml` contain absolute URLs. Keep `llms.txt`, `llms-full.txt`, `search-index.json`, `api/index.json`, the HTML guides and their Markdown copies together at the same site root. Deploy the included `functions/api/search.js` with Cloudflare Pages Functions to enable `/api/search`.
