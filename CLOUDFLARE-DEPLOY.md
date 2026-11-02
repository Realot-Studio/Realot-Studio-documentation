# Deploy Realot Studio documentation to Cloudflare Pages

The site is a static documentation build plus one Cloudflare Pages Function that provides question-based search.

## Required files

Deploy the complete contents of this folder together. In particular, keep the top-level `functions/` folder beside `index.html`, `search-index.json`, `llms.txt`, and the `docs/` folder. The function file must remain at `functions/api/search.js`; Cloudflare exposes it as `/api/search`.

## Deployment

Use Cloudflare Pages Git integration, or deploy with Wrangler so the Functions directory is included. A plain static drag-and-drop upload does not deploy Pages Functions; if you use a static-only upload, `/api/search` will not exist and AI tools must use the `search-index.json` fallback.

With Wrangler, from the parent directory that contains this site folder, run:

```bash
npx wrangler pages deploy ./docnew --project-name YOUR_CLOUDFLARE_PAGES_PROJECT
```

Replace the folder and project name with your actual deployment values. Do not rename or omit the `functions/` directory.

## Test after deployment

Open this URL, replacing the host with your documentation domain:

```text
https://docs.example.com/api/search?q=make%20an%20enemy%20follow%20the%20player
```

A working endpoint returns JSON containing `results`. Each result includes `title`, `description`, `section`, `url`, `score`, `matchedTerms`, and `snippet`. The returned `url` values are relative to the documentation root.

AI assistants can start with only the documentation homepage URL, fetch `/llms.txt`, and follow its instructions to query `/api/search`. They do not need to know the paths to component or scripting pages in advance.
