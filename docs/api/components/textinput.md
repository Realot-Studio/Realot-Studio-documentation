# TextInput

> Realot Studio TextInput component reference: fields, script API, behavior and examples.

- Source: https://realot-studio.pages.dev/docs/api/components/textinput.html

> **Scope:** This page documents the TextInput component in Realot Studio. Runtime fields are serialized scene data; the Script API section lists only members intentionally exposed to game scripts.

> **Where to find it in the editor:** Top UI → Message Input, or Inspector → Add Component → Text Input.

## What it does

Interactive text input control driven by the runtime UI system.

> **Component setup & editor tools:** TextInput creates an editable text-entry control and is typically created from GameObject → UI or the Inspector Add Component picker.

## How to add and use TextInput

**Editor path:** Select the target entity in the **Hierarchy** (left side) → look at the **Inspector** (right side) → click **Add Component** at the bottom of the Inspector → search for **TextInput** → click the component row. The Add Component picker is a centered modal with a search box; it only lists components not already attached.

For components with a dedicated editor tool, the tool is opened or activated from the location described below. Do not assume that adding the component alone activates its editor; some systems require a separate window, panel, or viewport tool.

## Component setup & editor tools

- GameObject → UI → Message Input creates a TextInput entity. You can also select an entity → Inspector → Add Component → Text Input.

### What you should see after adding it

The component appears as its own section in the Inspector. Its serialized settings are listed in the **Component data** table below. If a field is conditional, it appears only when the relevant mode/type is selected. If a field is a runtime state field (for example grounded or resolved velocity), treat it as read-only diagnostic state unless the API reference explicitly documents it as writable.

### How to read the settings

For every setting below, the documentation distinguishes **type**, **default**, **meaning**, and tuning direction where behavior is known. When a value represents a direction, use the engine's coordinate convention documented in [Coordinate system](../../reference/coordinate-system.html); do not substitute Unity/Godot conventions.

## Component data

| Field | Type | Purpose | Default |
| --- | --- | --- | --- |
| `value` | string | Current text. |  |
| `placeholder` | string | Placeholder text. | `Type a message...` |
| `maxLength` | number | Maximum characters. | `200` |
| `fontSize` | number | Font size. | `18` |
| `fontFamily` | string | Font family. | `Arial` |
| `textColor` | hex color string | Text color. | `#111111` |
| `placeholderColor` | hex color string | Placeholder color. | `#999999` |
| `backgroundColor` | hex color string | Background. | `#ffffff` |
| `borderColor` | hex color string | Border. | `#888888` |
| `borderWidth` | number | Border width. | `2` |
| `cornerRadius` | number | Corner radius. | `8` |
| `width` | number | Control width. | `260` |
| `height` | number | Control height. | `40` |
| `padding` | number | Horizontal/vertical padding. | `10` |
| `clearOnSubmit` | boolean | empty the field automatically after Enter — typical chat-box behavior | `true` |
| `focused` | boolean | Live state — see the file header for why these live here rather than in TextInputSystem's private state. | `false` |
| `justSubmitted` | boolean | one-frame pulse: true for exactly one frame after Enter is pressed | `false` |

## Tuning behavior

These are the practical direction-of-change rules for the most important controls on this component.

| Setting | What changing it does |
| --- | --- |
| `maxLength` | Hard cap on typed characters. |
| `width / height` | Changes the visual input box size. |
| `borderWidth` | Higher = thicker border. |
| `padding` | Higher moves the text farther from the box edge. |

## Script API

| Member | Kind | Description |
| --- | --- | --- |
| `backgroundColor` | Property (read/write) | Background color. |
| `borderColor` | Property (read/write) | Border color. |
| `borderWidth` | Property (read/write) | Border width. |
| `clear()` | Method | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `clearOnSubmit` | Property (read/write) | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `cornerRadius` | Property (read/write) | Corner radius. |
| `focused` | Property (read-only) | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `fontFamily` | Property (read/write) | Font family. |
| `fontSize` | Property (read/write) | Font size. |
| `height` | Property (read/write) | Control height. |
| `justSubmitted` | Property (read-only) | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `maxLength` | Property (read/write) | Character cap. |
| `padding` | Property (read/write) | Padding. |
| `placeholder` | Property (read/write) | Placeholder. |
| `placeholderColor` | Property (read/write) | Placeholder color. |
| `textColor` | Property (read/write) | Text color. |
| `value` | Property (read/write) | The `this.textInput` sub-object exposed to user scripts (see scripting/ScriptAPI.js). |
| `width` | Property (read/write) | Control width. |

## Examples

```
if (this.textInput.justSubmitted) {
  sendMessage("Chat", "message", this.textInput.value);
  this.textInput.clear();
}
```

> **Need the full workflow?:** Components: complete workflow covers adding, configuring, testing, combining, and removing components.
