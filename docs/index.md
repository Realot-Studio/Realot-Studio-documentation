# Realot Studio documentation

> Source-aligned documentation for Realot Studio: editor workflows, scripting API, components, physics, navigation and export.

- Source: https://realot-studio.pages.dev/docs/index.html

> **What is Realot Studio?:** A browser-based 2D game engine with a visual editor, JavaScript gameplay scripting, PixiJS rendering and Rapier2D physics. The hosted engine is updated by publishing its web files; users do not need a separate engine installer.

## Start here

### [Open Realot Studio](getting-started/installation.html)

Use the hosted editor or serve the static distribution yourself.

### [Build your first game](getting-started/first-game.html)

Entities, components and a first script in a few steps.

### [Scripting quickstart](getting-started/scripting.html)

onStart, onUpdate, `this` and the component modules.

### [Editor controls](editor/controls.html)

Exact menu paths, panels and keyboard shortcuts.

## Browse by topic

### [Get started](getting-started/installation.html)

Run the editor, build a first game and learn the scripting model.

5 pages

### [Concepts](concepts/architecture.html)

Architecture, the entity–component model, the game loop and coordinates.

4 pages

### [Editor](editor/overview.html)

Every panel, menu path, shortcut and authoring workflow.

13 pages

### [Scripting](scripting/lifecycle.html)

Lifecycle, globals, input, physics, navigation, saving and debugging.

18 pages

### [API reference](api/index.html)

Component fields, script members, option shapes and prerequisites.

6 pages

### [Export & deploy](export/index.html)

HTML5, installable PWA and Android APK builds.

4 pages

### [Reference](reference/tuning-guide.html)

Tuning rules, scene and project formats, live updates and source map.

8 pages

### [AI & machine access](reference/ai-bridge.html)

llms.txt, Markdown twins, JSON catalogs and guidance for assistants.

3 pages

## Component reference

25 components, each documented with serialized fields, defaults, script API and editor location.

[**Transform**Position, rotation and scale. Every spatial entity uses a Transform.](api/components/transform.html)[**SpriteRenderer**Draw a 2D texture sprite for an entity.](api/components/spriterenderer.html)[**ShapeRenderer**Draw a procedural 2D shape without requiring a sprite asset.](api/components/shaperenderer.html)[**TextRenderer**Render text either in world space or as screen-space UI.](api/components/textrenderer.html)[**StrokePath**A variable-thickness strip along placed points — rivers, cables, roads, conveyor belts or walls — with flat color or…](api/components/strokepath.html)[**SpeechBubble**Speech bubble UI attached to an entity, useful for dialogue and NPC callouts.](api/components/speechbubble.html)[**ChatLog**Scrollable-style conversation log component for UI dialogue.](api/components/chatlog.html)[**TextInput**Interactive text input control driven by the runtime UI system.](api/components/textinput.html)[**Joystick**Virtual touch joystick for mobile and pointer-driven control schemes.](api/components/joystick.html)[**Rigidbody2D**2D physics body backed by the engine physics runtime. Dynamic, Kinematic and Static bodies have different script…](api/components/rigidbody2d.html)[**Collider2D**Physics collision shape and contact filtering. A Collider2D is also required for accurate pointer/touch hit tests.](api/components/collider2d.html)[**Joint2D**Connect physics bodies with Fixed, Revolute, Prismatic, Rope or Spring constraints.](api/components/joint2d.html)[**CharacterController**High-level movement modes: Character Controller, Platformer, Top-Down, Car, Follow, Patrol and Free.](api/components/charactercontroller.html)[**SpriteAnimation**Sprite-sheet/clip animation state on a SpriteRenderer.](api/components/spriteanimation.html)[**Camera**Orthographic 2D camera with reference resolutions, responsive scaling, follow, shake and optional pseudo-3D sprite…](api/components/camera.html)[**AudioSource**Play a local audio asset, optionally with distance-based 3D attenuation.](api/components/audiosource.html)[**AudioListener**Defines the hearing area for 3D audio and drives audio enter/leave callbacks.](api/components/audiolistener.html)[**Light**2D light source supporting Directional, Point, Spot, Area, GodRays and Freeform light shapes.](api/components/light.html)[**ShadowCaster**Marks an entity as a shadow occluder for the lighting system.](api/components/shadowcaster.html)[**LightingSettings**Scene-wide lighting quality and mood controls. Attach to one entity; the lighting system reads it scene-wide.](api/components/lightingsettings.html)[**NavAgent2D**Per-agent navigation settings and current path state for NavWorld2D pathfinding.](api/components/navagent2d.html)[**NavWorld2D**Shared navigation world for baked or dynamic 2D pathfinding, with 16 navigation areas.](api/components/navworld2d.html)[**Tileset**Defines a reusable 16-role autotile set. The editor can auto-slice one image or accept separate role images.](api/components/tileset.html)[**Tilemap**Sparse painted tile grid that references a Tileset entity by ID.](api/components/tilemap.html)[**Script**Script component holding a script name, source and enabled state.](api/components/script.html)

## For automated systems

Every page is complete static HTML with a Markdown twin (same URL, `.md`). Machine entry points: [llms.txt](../llms.txt), [llms-full.txt](../llms-full.txt) (all documentation in one file), [search-index.json](../search-index.json), [api/index.json](../api/index.json), [sitemap.xml](../sitemap.xml) and [robots.txt](../robots.txt). See [AI & crawlers](reference/ai-crawling.html).
