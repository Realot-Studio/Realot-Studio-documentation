# Engine conventions (RULES.txt)

> The architectural rules that govern how Realot Studio’s own codebase is organized.

- Source: https://realot-studio.pages.dev/docs/reference/rules.html

## Scope

This is the engine’s own internal contract for where code goes and how the three top-level folders relate. It applies to people extending Realot Studio itself; if you’re only writing game scripts, you don’t need it — see Scripting quickstart instead.

## 1. The core rule: runtime never depends on editor

`runtime/` is the actual game engine. `editor/` is the Unity-style level editor UI, a development tool only. `target/` is the standalone game shell, importing only from `runtime/`. No file under `runtime/` may ever import, reference, or depend on anything under `editor/` — not for debugging, not temporarily, not ever. You must be able to delete the `editor/` folder entirely and the game (`standalone runtime play entry point`) keeps working with zero changes. `editor/` may import from `runtime/` — that direction is allowed and expected, since the editor is built on top of the engine.

## 2. One feature = new file(s), not a growing old file

Adding a new component, system, editor panel, scripting API, or asset type creates a new file in the appropriate subfolder. Unrelated functionality is never appended into an existing file just because it’s nearby or already open. If a feature doesn’t fit any existing subfolder, a new subfolder is created (matching the existing lowercase, pluralized naming style) rather than dumping it into an unrelated folder.

| Adding… | Goes in… |
| --- | --- |
| A new gameplay component | runtime/components/YourComponent.js |
| A new gameplay/rendering/physics system | runtime/systems/YourSystem.js |
| A new editor panel | editor/panels/YourPanel.js |
| A new asset type | runtime/assets/YourManager.js |
| A new scripting capability | A method/property on the relevant file in runtime/scripting/components/, or a new file there |

## 3. Components stay plain data

Files under `runtime/components/` hold only plain serializable data (numbers, strings, booleans). No PixiJS objects, no DOM references, no behavior/update logic — behavior belongs in `runtime/systems/`. This is what keeps SceneSerializer.js able to save and load any component generically.

## 4. Rendering is centralized

`runtime/systems/RenderSystem.js` is the only place that creates or updates PixiJS display objects from entity data. Both the editor’s viewport and the standalone target use it, so visuals never drift between edit mode and play mode. Editor-only chrome (grid lines, selection gizmos) may be drawn in its own separate layer on top of the runtime’s render output — that chrome must never be visible in `/target`.

## 5. Scene data flows through the runtime’s public API only

The editor never invents its own scene format or its own copy of scene state. The single source of truth is the live World instance, and the single way to read/write its persisted form is `runtime/scene/SceneSerializer.js`. New scene-level functionality (undo, multi-scene, prefabs) extends the runtime’s `scene/` folder, not the editor’s `state/` folder.

## One API per capability (scripting)

`this.x`, `this.y`, `this.position`, `this.rotation`, `this.translate()`, and `this.visible` are flat shortcuts because Transform has only one shape. Everything else — velocity, physics forces, sprite properties, animation, camera, audio, movement-type tunables — is reached only through its sub-object (`this.rigidbody.*`, `this.sprite.*`, `this.controller.*`, etc). There is deliberately no flat-shortcut duplicate of any of these, because RigidbodyAPI exposes a different shape per body type and ControllerAPI exposes a different shape per controller type — a second flat copy would either duplicate that per-type logic or drift out of sync with it.

> **Source note:** These rules come from the engine repository’s RULES.txt . That file is not included in the client distribution ( project/ contains editor/ , player/ , runtime/ and vendor/ only), so it is documented here rather than linked.
