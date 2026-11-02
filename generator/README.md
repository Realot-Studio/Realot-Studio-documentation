# Realot Studio documentation generator

Builds the static, crawlable Realot Studio documentation site from `content/` and the engine source facts.

## Build

```bash
python3 tools/extract_source_facts.py <engine-root> source-facts.json
node tools/extract_easings.mjs <engine-root> easings.json
python3 build.py --out .. --origin https://<your-documentation-domain>
```

The default output directory is the parent of `generator/` (the documentation repository root). `--origin` supplies the live site origin for canonical links and absolute sitemap URLs.

## How discovery works

The build creates stable, unversioned documentation URLs, one Markdown twin for each HTML page, `/llms.txt`, `/llms-full.txt`, `/search-index.json`, `/api/index.json`, `/api/manifest.json`, a human search page and crawler metadata. The AI entry point tells an agent how to retrieve the index and rank related topics without knowing the target page path in advance.

Update the existing output in place when the engine changes; do not create version-specific documentation directories or version selector pages.


Cloudflare Pages deployment: keep the top-level `functions/` directory beside the generated site output. It provides `GET /api/search?q=...`, which ranks the generated `search-index.json` and returns the closest pages.
