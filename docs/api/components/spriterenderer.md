# SpriteRenderer

> Realot Studio SpriteRenderer component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/spriterenderer.html

> **Scope:** This page documents the SpriteRenderer component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Inspector → Add Component → Sprite Renderer; choose or import sprites from bottom Project → Sprites, then assign the Sprite Renderer sprite.

## What it does

Draw a 2D texture sprite for an entity.

> **Component setup & editor tools:** In the Inspector, use the SpriteRenderer section to choose the sprite, then use its visual fields and the Scene viewport to verify the result.

## How to add and use SpriteRenderer

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **SpriteRenderer** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Inspector → SpriteRenderer → sprite field: choose the sprite asset. Use the viewport to see the result. FlipX/FlipY are visual orientation controls; color/opacity change appearance without changing the source asset.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `spriteKey` | nullable value | Asset key for the sprite texture. | `null` |
| `color` | hex color string | Tint color. | `#ffffff` |
| `opacity` | number | Opacity multiplier. | `1` |
| `flipX` | boolean | Mirror horizontally. | `false` |
| `flipY` | boolean | Mirror vertically. | `false` |
| `visualRotation` | number | Visual-only rotation in degrees, added to Transform.rotation when drawing. | `0` |
| `referenceWidth` | nullable value | Optional reference width used by rendering/layout. | `null` |
| `referenceHeight` | nullable value | Optional reference height used by rendering/layout. | `null` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `opacity` | 0 is invisible; 1 is fully opaque; values between are translucent. |
| `flipX / flipY` | Boolean mirror. Flip X changes left/right without changing the Transform position. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `color` | Property (read/write) | Hex tint color. |
| `flipX` | Property (read/write) | Horizontal mirror. |
| `flipY` | Property (read/write) | Vertical mirror. |
| `opacity` | Property (read/write) | The `this.sprite` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `texture` | Property (read/write) | Sprite asset key. |
| `visualRotation` | Property (read/write) | The `this.sprite` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## Examples

```
this.sprite.texture = "target";
```

```
this.sprite.flipX = input.keyDown("ArrowLeft");
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
