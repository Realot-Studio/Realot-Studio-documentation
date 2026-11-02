# Complete feature workflows

> Use these pages when you need to build an entire subsystem, not just understand one property. Each workflow starts with prerequisites and editor locations, then moves through configuration, scripting, testing and troubleshooting.

- Source: https://realot-studio.pages.dev/docs/editor/complete-feature-workflows.html

### [Navigation authoring](../editor/navigation.html)

Create Nav World 2D, configure bounds/cell size, define areas, paint or derive walkable space, add agents, bake/update navigation and debug the result.

### [Navigation from editor to script](../scripting/navigation-complete.html)

Complete path from scene setup through NavAgent2D, named area masks/costs, navMoveToward/navDriveToward and runtime troubleshooting.

### [Physics authoring](../editor/physics.html)

Build colliders, rigidbodies, joints and character controllers, then tune layers, masks, gravity, damping, slopes and one-way platforms.

### [Physics scripting](../scripting/physics.html)

Use Rigidbody2D, Collider2D, raycasts, forces/impulses, collision state and movement APIs from scripts.

### [Lighting, audio and UI](../editor/lighting-audio-ui.html)

Set up lights/shadows, audio sources/listeners, text and interactive UI components with their editor locations and runtime APIs.

### [Tilemaps and tilesets](../editor/tilemaps.html)

Create tileset data, attach it to a Tilemap, paint, edit tile data and understand the navigation/physics consequences of tile geometry.

### [Assets and animation](../editor/assets-animation.html)

Import/use sprites, build Sprite Animation clips, choose frames, set playback and connect animation state to scripts.

### [Prefabs](../editor/prefabs.html)

Create reusable entity templates, instantiate them, understand overrides, update/revert behavior and runtime spawning.

### [Web/PWA deployment](../export/web.html)

Understand the normal online workflow, standalone web export, PWA behavior and what a deployment must serve.

### [Android APK export](../export/android.html)

Configure the separate build-server workflow and understand what is sent from the browser editor.

## How to use these guides

1. Start with the prerequisites section.
2. Follow the exact editor path instead of guessing which panel contains a control.
3. Configure the minimum working setup first.
4. Only then add optional tuning such as costs, smoothing, avoidance, shadows, custom input or advanced physics.
5. Run the smallest test scene before integrating the subsystem into a large project.
6. If a result is wrong, use the troubleshooting section before changing unrelated settings.
