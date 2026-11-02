# HTML5 and PWA export

> Create a standalone HTML5 game or a PWA with a manifest and service worker.

- Source: https://realot-studio.pages.dev/docs/export/web.html

## HTML5

HTML5 export produces a standalone static game package. The ZIP contains an `index.html` entry point, game code, the standalone runtime and the assets required by the project. It does not include the editor or Hub.

## PWA

PWA export adds a web app manifest and service worker to the same standalone game package. The browser can offer installation and offline caching when the deployment meets the browser's PWA requirements.

## Hosting checklist

- Extract the ZIP and keep the entry point, runtime and referenced assets together.
- Serve the package over HTTP(S); do not rely on opening `index.html` directly with `file://`.
- Use HTTPS on a public deployment when browser security rules or PWA installation require a secure origin.
- Test the exported game independently of the editor before sharing it.
