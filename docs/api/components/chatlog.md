# ChatLog

> Realot Studio ChatLog component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/chatlog.html

> **Scope:** This page documents the ChatLog component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top UI → Chat Log, or Inspector → Add Component → Chat Log.

## What it does

Scrollable-style conversation log component for UI dialogue.

> **Component setup & editor tools:** ChatLog provides a dialogue/log display component intended for scripted text updates.

## How to add and use ChatLog

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **ChatLog** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- Inspector → ChatLog: configure the log; use its script-facing API for runtime messages/entries.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `messages` | array | [{ sender, text, senderColor }], oldest first | `[]` |
| `maxMessages` | number | total history kept — oldest dropped once exceeded | `50` |
| `visibleCount` | number | how many of the most recent messages are shown at once | `6` |
| `width` | number | Log width. | `320` |
| `lineHeight` | number | Line height. | `26` |
| `fontSize` | number | Font size. | `16` |
| `fontFamily` | string | Font family. | `Arial` |
| `messageColor` | hex color string | Message color. | `#ffffff` |
| `senderColor` | hex color string | default sender-name color if a message doesn't specify its own | `#ffd700` |
| `backgroundColor` | hex color string | Background. | `#000000` |
| `backgroundOpacity` | number | semi-transparent panel behind the text, typical chat-overlay look | `0.5` |
| `padding` | number | Padding. | `10` |
| `showSender` | boolean | false = just the message text, no "Name: " prefix (good for narration logs) | `true` |
| `screenSpace` | boolean | see TextRenderer.js's file header for the exact meaning — true = fixed UI overlay, false = world-space (e.g. | `true` |
| `visible` | boolean | Visibility. | `true` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `maxMessages` | Total retained history before oldest messages are dropped. |
| `visibleCount` | How many recent messages are shown at once. |
| `backgroundOpacity` | 0 transparent, 1 opaque. |
| `lineHeight` | Higher creates more vertical spacing between messages. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `backgroundColor` | Property (read/write) | Background color. |
| `backgroundOpacity` | Property (read/write) | Background opacity. |
| `clear()` | Method | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `fontFamily` | Property (read/write) | Font family. |
| `fontSize` | Property (read/write) | Font size. |
| `lineHeight` | Property (read/write) | Line height. |
| `maxMessages` | Property (read/write) | Maximum retained messages. |
| `messageColor` | Property (read/write) | Message color. |
| `messages` | Property (read-only) | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `padding` | Property (read/write) | Padding. |
| `screenSpace` | Property (read/write) | Screen-space mode. |
| `send(sender, text, color)` | Method | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `senderColor` | Property (read/write) | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `showSender` | Property (read/write) | The `this.chat` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `visible` | Property (read/write) | Visibility. |
| `visibleCount` | Property (read/write) | Number of visible rows. |
| `width` | Property (read/write) | Panel width. |

## Examples

```
this.chat.send("Guard", "Halt!", "#ef4444");
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
