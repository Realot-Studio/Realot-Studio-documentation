# SpeechBubble

> Realot Studio SpeechBubble component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/speechbubble.html

> **Scope:** This page documents the SpeechBubble component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top UI → Speech Bubble, or Inspector → Add Component → Speech Bubble.

## What it does

Speech bubble UI attached to an entity, useful for dialogue and NPC callouts.

> **Component setup & editor tools:** SpeechBubble provides an in-scene speech presentation attached to an entity.

## How to add and use SpeechBubble

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **SpeechBubble** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Inspector → SpeechBubble: configure its display properties; use the documented SpeechBubble API to change content at runtime.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `text` | string | Current bubble text. | `Hello!` |
| `visible` | boolean | Whether visible. | `false` |
| `backgroundColor` | hex color string | Bubble background. | `#ffffff` |
| `textColor` | hex color string | Text color. | `#111111` |
| `borderColor` | hex color string | Border color. | `#111111` |
| `borderWidth` | number | Border width. | `2` |
| `fontSize` | number | Font size. | `20` |
| `fontFamily` | string | Font family. | `Arial` |
| `padding` | number | px between the text and the bubble's edge | `12` |
| `cornerRadius` | number | Corner radius. | `10` |
| `maxWidth` | number | px — text wraps at this width | `220` |
| `offsetX` | number | px offset from this entity's own position | `0` |
| `offsetY` | number | negative = above the entity's head (typical) | `-60` |
| `tailDirection` | string | "down" | "up" | "left" | "right" | "none" — which edge the pointer triangle sits on, pointing back at the entity | `down` |
| `tailSize` | number | Tail size. | `14` |
| `hideTimer` | number | Auto-hide countdown in seconds, ticked down by SpeechBubbleSystem while visible; 0 or less means "stays visible until hidden manually" (see this.speechBubble.hide()). | `0` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `maxWidth` | Higher lets a line run longer before wrapping. |
| `offsetY` | Negative values move the bubble upward from the entity in the default screen convention. |
| `padding` | Higher creates more interior space around text. |
| `cornerRadius` | Higher makes corners rounder. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `backgroundColor` | Property (read/write) | Background color. |
| `borderColor` | Property (read/write) | Border color. |
| `borderWidth` | Property (read/write) | Border width. |
| `cornerRadius` | Property (read/write) | Corner radius. |
| `fontFamily` | Property (read/write) | Font family. |
| `fontSize` | Property (read/write) | Font size. |
| `hide()` | Method | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `maxWidth` | Property (read/write) | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `offsetX` | Property (read/write) | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `offsetY` | Property (read/write) | Vertical offset. |
| `padding` | Property (read/write) | Padding. |
| `show(text, duration)` | Method | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `tailDirection` | Property (read/write) | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `tailSize` | Property (read/write) | Tail size. |
| `text` | Property (read/write) | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `textColor` | Property (read/write) | Text color. |
| `visible` | Property (read/write) | The `this.speechBubble` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |

## Examples

```
this.speechBubble.show("Hello!", 2);
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
