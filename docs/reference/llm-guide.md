# Realot Studio reference for AI assistants

> Practical rules for AI assistants that explain, script, debug and extend Realot Studio projects accurately.

- Source: https://realot-studio.pages.dev/docs/reference/llm-guide.html

## What is Realot Studio?

Realot Studio is a browser-based 2D game engine with a visual editor, an entity/component runtime, JavaScript gameplay scripts, PixiJS rendering and Rapier2D physics. The Hub and editor run as web applications. The hosted build is updated by publishing web files; users do not install a separate engine executable.

## Retrieve the relevant reference first

Given only the documentation homepage URL, fetch `llms.txt` from its root, then send the user question to `api/search?q=...`. Read the closest returned pages; the endpoint supplies their paths, so do not guess URLs. For API questions, also fetch `api/index.json` and the [complete script module member index](../api/script-modules.html). The JSON catalog is generated from source facts and is the authoritative list of supported component fields, enum values and API module members. Read the linked guide for behavior, prerequisites and examples.

## AI Bridge and editor automation

When an MCP-connected assistant needs to inspect or edit the open project, use the [AI Bridge and MCP guide](ai-bridge.html). It lists the current tools, connection requirements and limits. Do not assume the hosted relay is deployed: it requires a Realot operator to configure it. The MCP tool schemas supplied by the live connection are authoritative for parameters.

## Gameplay script model

Inside a script callback, `this` refers to the entity that owns the script. Transform shortcuts such as `this.x` and `this.y` are always available. Component sub-objects such as `this.rigidbody`, `this.sprite` and `this.camera` require their matching components. `this.transform`, `this.state` and `this.myTouch` are available on every entity. Use the [`this` reference](../api/this.html) for the full context model.

## Source and runtime rules

- Use only documented member names in the module allow-lists; unknown member names raise a typed runtime API error. The member index also flags a known allow-list gap: `this.joint.flexibility` is listed but has no working script accessor in the supplied source; set it in the Inspector.
- Check component requirements before suggesting a component-backed API.
- Use `onUpdate(dt)` for frame-time behavior and `onFixedUpdate(dt)` for fixed-step logic.
- Use entity/world coordinates for Transform, mouse/touch world positions, physics hits and navigation waypoints. Screen coordinates are canvas pixels.
- Do not reach into editor implementation files from gameplay scripts. Keep editor-only code and runtime code separate.
- Project scripts execute as page code; imported scripts should be treated as executable content, not as a secure sandbox.

## Editor settings and components

The editor has no single general Settings dialog. Project/backup choices are in File, layer and navigation-area names are in Edit, panel visibility is in Window, and component fields are in the Inspector. The [Editor settings guide](../editor/settings.html) lists all current menu options and stored performance defaults. The [API index](../api/index.html) links all 25 components and their settings.

## Export behavior

- **HTML5:** downloads a standalone web game package.
- **PWA:** adds a manifest and service worker for installation/offline support.
- **Android APK:** the user clicks Export, chooses Android APK, and downloads the built APK when the remote service finishes. The current editor allowance is 3 APK exports in a rolling 14-day period. A failed or cancelled job returns its count. The output is debug-signed, not Play Store production-signed.
- **Desktop:** shown as coming soon in the supplied Export window.

## Project files

The official portable project file uses the `.realot` extension. Users can install Realot Hub as a PWA on a supported desktop browser, then double-click a downloaded `.realot` file to open that project in the editor. Realot can request permission to save changes back to the same file. If PWA file handling is unavailable, users can open the editor and choose **File → Load Project**.
