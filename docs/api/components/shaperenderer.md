# ShapeRenderer

> Realot Studio ShapeRenderer component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/shaperenderer.html

> **Scope:** This page documents the ShapeRenderer component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Create directly from top GameObject → Shape → Square/Circle/Capsule/Triangle, or Inspector → Add Component → Shape Renderer.

## What it does

Draw a procedural 2D shape without requiring a sprite asset.

> **Component setup & editor tools:** Use ShapeRenderer when you want a procedural shape without importing an image.

## How to add and use ShapeRenderer

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **ShapeRenderer** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Inspector → ShapeRenderer: choose the shape type and edit its dimensions. For triangle/freeform shapes, the corresponding viewport gizmo is used when available.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `shapeType` | ShapeType enum: Square | Circle | Triangle | Capsule | Square, Circle, Triangle or Capsule. | `Square` |
| `width` | number | Square | `100` |
| `height` | number | Square height. | `100` |
| `radius` | number | Circle | `50` |
| `capsuleHalfHeight` | number | Capsule: a "stadium" shape (rectangle with semicircle caps), same halfHeight/radius convention as Collider2D's capsule so the two stay easy to eyeball-match if a user wants a visual capsule over a capsule collider. | `50` |
| `capsuleRadius` | number | Capsule cap radius. | `30` |
| `trianglePoints` | array | Triangle: 3 points in the entity's LOCAL space (same space Collider2D.trianglePoints uses), user-editable via draggable gizmo handles in the Scene view. | `[{x:-50,y:50}, {x:50,y:50}, {x:0,y:-50}]` |
| `fillColor` | hex color string | Fill color. | `#3a8ede` |
| `visualRotation` | number | Visual-only rotation in degrees, added to Transform.rotation when drawing. | `0` |
| `opacity` | number | Opacity. | `1` |
| `outlineEnabled` | boolean | Enable outline. | `false` |
| `outlineColor` | hex color string | Outline color. | `#ffffff` |
| `outlineWidth` | number | Outline width. | `2` |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `capsuleHalfHeight` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `capsuleRadius` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `fillColor` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `height` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `opacity` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `outlineColor` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `outlineEnabled` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `outlineWidth` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `radius` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `shapeType` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `visualRotation` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `width` | Property (read/write) | The `this.shape` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## Examples

```
this.shape.fillColor = "#22c55e";
```

```
this.shape.shapeType = "Circle";
```

```
this.shape.radius = 32;
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
