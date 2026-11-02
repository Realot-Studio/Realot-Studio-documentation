# StrokePath

> Realot Studio StrokePath component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/strokepath.html

> **Scope:** This page documents the StrokePath component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top GameObject → 2D Object → Stroke Path. After a Stroke Path exists, the toolbar exposes Path (P); click empty space to append, drag points, and click segments to insert.

## What it does

A variable-thickness strip along placed points — rivers, cables, roads, conveyor belts or walls — with flat color or textured fill.

> **Component setup & editor tools:** StrokePath creates a drawable strip/path; its editing is performed with the Stroke Path viewport tool/gizmo.

## How to add and use StrokePath

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **StrokePath** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Select an entity with StrokePath → use the Stroke Path viewport tool/gizmo to edit path points. Keep the Inspector open for serialized path/material settings.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `points` | array | Two default points (a minimal, visibly-a-path starting shape) rather than one or zero — a single point has no strip to draw at all, so a StrokePath freshly added via the GameObject menu or Add Component window shows \*something\* immediately instead of an invisible/degenerate result the user has to fix before they can… | `[{x:-100,y:0}, {x:100,y:0}]` |
| `thickness` | number | Strip thickness. | `40` |
| `color` | hex color string | Flat fill color, used when useTexture is false. | `#8a8a8a` |
| `opacity` | number | Opacity. | `1` |
| `useTexture` | boolean | Use an image texture along the path instead of a flat fill. | `false` |
| `textureKey` | nullable value | Logical sprite key, resolved to a PIXI.Texture the same way SpriteRenderer.spriteKey is (see runtime/assets/AssetManager.js resolveTexture) — components never hold PIXI objects directly, for the same "stay serializable" reason SpriteRenderer doesn't. | `null` |
| `textureMode` | StrokePathTextureMode enum: stretch | tile | See StrokePathTextureMode above — STRETCH (fit the whole image to the path, may distort) or TILE (repeat at native size, never stretched). | `stretch` |
| `textureTiling` | number | TILE mode only: how many world units of path length one full texture tile covers lengthwise — e.g. | `100` |
| `textureScale` | number | How many times the texture repeats ACROSS the strip's own thickness (perpendicular to the direction of travel) — kept separate from textureTiling (the lengthwise axis) since a texture like a road stripe or brick run almost always needs a different repeat rate across its width than along its length. | `1` |
| `textureOffset` | number | Slides the texture lengthwise along the path without moving any point — e.g. | `0` |
| `textureFlip` | boolean | Mirrors the texture across the path's own centerline (flips which side is "up") without needing a second, mirrored copy of the source image — handy for a texture that's only authored for one direction of travel. | `false` |
| `textureRotation` | number | Rotates the texture, in degrees, around the center of each tile — independent of every other texture setting above, and applied in TEXTURE space (not world space), so it stays a fixed "printed at an angle on the image" look rather than a rotation that would need to track the path's own direction as it turns. | `0` |
| `jointMode` | StrokePathJointMode enum: sharp | bevel | round | See StrokePathJointMode above — SHARP (hard corner), BEVEL (flat chamfer), or ROUND (filled arc). | `round` |
| `capMode` | StrokePathCapMode enum: none | box | round | See StrokePathCapMode above — NONE (flat stop), BOX (flat, but extended slightly past the tip), or ROUND (half-circle cap). | `round` |
| `smoothing` | number | 0-1. Runs the authored `points` through a Catmull-Rom spline resample BEFORE tessellation, turning the raw straight-segment polyline into a smooth curve — same idea as a spline/curve tool in a 3D package, applied to this 2D strip. | `0` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `thickness` | Larger values make the strip wider. |
| `textureTiling` | In TILE mode, larger values make each repeated texture cover more path length, so the image repeats less often. |
| `textureScale` | Higher scales the texture; lower makes it smaller/repeated more densely. |
| `textureOffset` | Changing this over time scrolls the texture along the path. |
| `opacity` | 0 invisible, 1 opaque. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `addPoint(x, y)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `capMode` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `color` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `firstPoint` | Property (read-only) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `getLength()` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `getPoint(index)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `insertPoint(index, x, y)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `jointMode` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `lastPoint` | Property (read-only) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `localToWorld(localX, localY)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `opacity` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `pointCount` | Property (read-only) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `points` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `removePoint(index)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `setPoint(index, x, y)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureFlip` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureKey` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureMode` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureOffset` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureRotation` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureScale` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `textureTiling` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `thickness` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `useTexture` | Property (read/write) | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |
| `worldToLocal(worldX, worldY)` | Method | The `this.strokePath` sub-object exposed to user scripts on any entity that has a StrokePath component. |

## Notes & behavior

- Points are placed with the Path tool in the Scene viewport, then adjusted by dragging a point or clicking a segment to insert a new one between two existing points.
- An open polyline (A to B), not a closed loop.
- Reads/writes on this.strokePath.points always operate on a copy, so mutating a returned array can never silently corrupt the live component; assign it back (or use the point methods) to apply a change.

## Examples

```
this.strokePath.addPoint(this.x, this.y);
```

```
this.strokePath.textureOffset += 20 * time.deltaTime; // flowing river/conveyor look
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
