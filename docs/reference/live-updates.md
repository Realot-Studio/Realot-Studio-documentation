# Live updates

> How the hosted Realot Studio website and its documentation are updated in place.

- Source: https://realot-studio.pages.dev/docs/reference/live-updates.html

## Browser delivery

Realot Studio is delivered as a web application. The hosted Hub, editor and runtime are loaded from the site's published files. Users do not need to download a new engine installer whenever the site owner publishes an update.

## The website address stays the same

Publishing a new engine build replaces the files served at the existing deployment URL. The same is true of the documentation: its unversioned topic URLs point to the current published documentation.

## Browser and PWA caching

A normal browser visit retrieves the published site files according to the deployment's cache headers. An installed PWA or a browser with the service worker may continue using cached files while offline. Reconnect and reload to allow the new published files to be fetched. A deployment should publish its files atomically and configure cache headers so the HTML entry points and service worker can update.

## Project compatibility is separate

Although the hosted engine is updated in place, saved project archives may contain engine compatibility metadata. When a project saved by a newer engine is opened in an older build, Realot may show a compatibility warning. That project metadata is not a documentation URL version.
