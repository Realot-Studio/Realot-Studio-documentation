# TextRenderer

> Realot Studio TextRenderer component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/textrenderer.html

> **Scope:** This page documents the TextRenderer component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top UI menu → Text, or Inspector → Add Component → Text; screen-space text is authored from the same Inspector component.

## What it does

Render text either in world space or as screen-space UI.

> **Component setup & editor tools:** TextRenderer displays text as a screen/world-space rendering component depending on the entity/camera context.

## How to add and use TextRenderer

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **TextRenderer** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Inspector → TextRenderer: edit the text and presentation properties. For runtime changes, use the documented this.text API.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `value` | string | Displayed text. | `Text` |
| `fontSize` | number | Font size. | `32` |
| `color` | hex color string | Text color. | `#ffffff` |
| `fontFamily` | string | Font family name. | `Arial` |
| `bold` | boolean | Bold text. | `false` |
| `italic` | boolean | Italic text. | `false` |
| `align` | string | "left" | "center" | "right" — multi-line text alignment | `left` |
| `anchorX` | number | 0–1, this text's own pivot point (0.5,0.5 = centered on Transform.x/y, matching a sprite's default anchor) | `0.5` |
| `anchorY` | number | Vertical anchor from 0 to 1. | `0.5` |
| `opacity` | number | Opacity. | `1` |
| `screenSpace` | boolean | see file header — true = fixed UI overlay, false = world-space | `true` |
| `wordWrap` | boolean | Enable wrapping. | `false` |
| `wrapWidth` | number | px — only used while wordWrap is true | `300` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `fontSize` | Higher = larger text. |
| `anchorX / anchorY` | 0 = top/left pivot, 0.5 = center, 1 = bottom/right pivot for the text block. |
| `wrapWidth` | Only used when wordWrap is enabled; larger width permits longer lines before wrapping. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `align` | Property (read/write) | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `anchorX` | Property (read/write) | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `anchorY` | Property (read/write) | Vertical anchor. |
| `bold` | Property (read/write) | Bold toggle. |
| `color` | Property (read/write) | Hex text color. |
| `fontFamily` | Property (read/write) | Font family. |
| `fontSize` | Property (read/write) | Font size. |
| `italic` | Property (read/write) | Italic toggle. |
| `opacity` | Property (read/write) | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `screenSpace` | Property (read/write) | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `value` | Property (read/write) | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `wordWrap` | Property (read/write) | Enable word wrapping. |
| `wrapWidth` | Property (read/write) | The `this.text` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## Examples

```
this.text.value = "Score: " + score;
```

```
this.text.screenSpace = true;
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
