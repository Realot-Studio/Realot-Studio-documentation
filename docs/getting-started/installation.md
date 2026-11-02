# Use Realot Studio

> Realot Studio is a browser-based engine. Open the hosted site; local hosting is optional.

- Source: https://realot-studio.pages.dev/docs/getting-started/installation.html

## Normal use: open the website

> **No engine installer is required:** Realot Studio runs as a browser application. Open the hosted Realot site in a modern browser and use the Hub to create or open a project. The editor and runtime are delivered as web files; you do not need to download a separate engine installer to use the hosted version.

When the engine owner publishes an update to the hosted site, the new files are available from the same website address. A normal page reload while online retrieves the published files. A previously installed PWA can continue using cached assets offline until it reconnects and refreshes.

## Optional browser installation

On a supported browser and deployment, choose the Hub's **Install app** action or use the browser's own install option. This adds an app-like launcher entry. It is still the same web application and does not create a separate downloadable engine release.

## Optional: host the engine yourself

The supplied engine project is a static web application. To preview a local copy or publish your own deployment, serve the project folder over HTTP(S). For a quick local preview, run this command from the folder containing the engine files:

```
python3 -m http.server 5000
```

Then open `http://localhost:5000/`. Do not open the main HTML file directly with `file://`; browser module, fetch and WebAssembly loading require an HTTP origin.

## Browser requirements

- A modern browser with JavaScript modules and WebAssembly.
- Canvas/WebGL support for the renderer.
- Browser storage for project data and preferences.
- HTTPS for production deployments that need secure browser APIs or PWA installation (localhost is treated as secure for development).

## Android APK export

Android APK export is separate from normal browser use. Realot packages the game in the browser and sends the standalone web export to the configured Android build service. The editor does not run Android Studio, Gradle or an Android SDK locally. See [Android APK export](../export/android.html) for the current workflow.
